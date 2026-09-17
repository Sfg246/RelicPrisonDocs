from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path

source = Path(sys.argv[1]).resolve()
dest = Path(sys.argv[2]).resolve()
source_wiki = source / "wiki"
wiki = dest / "wiki"

if wiki.exists():
    shutil.rmtree(wiki)
shutil.copytree(source_wiki, wiki, ignore=shutil.ignore_patterns("node_modules", "dist", "cache"))

for name in ("CHANGELOG.md", "KNOWN-LIMITATIONS-1.0.0.md"):
    shutil.copy2(source / name, dest / name)

snapshots = dest / "snapshots" / "resources"
if snapshots.parent.exists():
    shutil.rmtree(snapshots.parent)
shutil.copytree(source / "src" / "main" / "resources", snapshots)
(snapshots / "plugin.yml").unlink(missing_ok=True)

# Keep generated YAML docs self-contained using public configuration snapshots.
p = wiki / "scripts" / "generate-config-reference.mjs"
s = p.read_text(encoding="utf-8")
s = s.replace("const resourcesRoot = path.resolve(wikiRoot, '../src/main/resources')", "const resourcesRoot = path.resolve(wikiRoot, '../snapshots/resources')")
s = s.replace("const repoBase = 'https://github.com/Sfg246/RelicPrison/blob/main/src/main/resources/'", "const repoBase = 'https://github.com/Sfg246/RelicPRisonDocs/blob/main/snapshots/resources/'")
s = s.replace("from `src/main/resources`", "from the released configuration snapshots in `snapshots/resources`")
s = s.replace("`src/main/resources/${pretty(file)}`", "`snapshots/resources/${pretty(file)}`")
s = s.replace("packaged YAML as the source of truth", "released configuration snapshots as the public source of truth")
p.write_text(s, encoding="utf-8")

# Keep the API signature pages generated during migration, but never require Java source publicly.
pkg_path = wiki / "package.json"
pkg = json.loads(pkg_path.read_text(encoding="utf-8"))
pkg["name"] = "relicprison-public-docs"
pkg["scripts"]["docs:generate"] = "npm run docs:generate:assets && npm run docs:generate:config && npm run docs:generate:status"
pkg["scripts"].pop("docs:generate:api", None)
pkg_path.write_text(json.dumps(pkg, indent=2) + "\n", encoding="utf-8")
(wiki / "scripts" / "generate-api-reference.mjs").unlink(missing_ok=True)

for api_file in (wiki / "generated" / "api").glob("*.md"):
    text = api_file.read_text(encoding="utf-8")
    text = re.sub(r"\[View source\]\(https://github\.com/Sfg246/RelicPrison/[^\n]+\)\n\n", "_Public API signature snapshot from RelicPrison 1.0.0._\n\n", text)
    text = text.replace("Generated from the public Java API package during every documentation build.", "Snapshot generated from the RelicPrison 1.0.0 API before the implementation repository was made private.")
    text = text.replace("Generated from `api/event`. Event names are never hand-maintained here, so newly committed public events automatically appear in the docs build.", "Snapshot generated from the RelicPrison 1.0.0 public event API before the implementation repository was made private.")
    api_file.write_text(text, encoding="utf-8")

# Point VitePress at the new public repository and GitHub Pages path.
config = wiki / ".vitepress" / "config.mjs"
text = config.read_text(encoding="utf-8")
text = text.replace("const productionBase = '/RelicPrison'", "const productionBase = '/RelicPRisonDocs'")
text = text.replace("https://sfg246.github.io/RelicPrison/", "https://sfg246.github.io/RelicPRisonDocs/")
text = text.replace("https://sfg246.github.io/RelicPrison/social-card.svg", "https://sfg246.github.io/RelicPRisonDocs/social-card.svg")
text = text.replace("socialLinks: [{ icon: 'github', link: 'https://github.com/Sfg246/RelicPrison' }]", "socialLinks: [{ icon: 'github', link: 'https://github.com/Sfg246/RelicPRisonDocs' }]")
text = text.replace("{ text: 'Support', link: 'https://github.com/Sfg246/RelicPrison/issues' }", "{ text: 'Support', link: 'https://github.com/Sfg246/RelicPRisonDocs/issues' }")
text = text.replace("pattern: 'https://github.com/Sfg246/RelicPrison/edit/main/wiki/:path'", "pattern: 'https://github.com/Sfg246/RelicPRisonDocs/edit/main/wiki/:path'")
text = text.replace("message: 'Source-driven RelicPrison documentation'", "message: 'Public RelicPrison documentation'")
text = text.replace("copyright: 'Defaults and generated references are built from the live repository.'", "copyright: 'Configuration references are built from released public snapshots; plugin implementation remains private.'")
config.write_text(text, encoding="utf-8")

# Replace the old public Pages origin anywhere it appears in public text files.
text_exts = {".md", ".mjs", ".js", ".json", ".txt", ".svg", ".xml", ".yml", ".yaml"}
for f in wiki.rglob("*"):
    if not f.is_file() or f.suffix.lower() not in text_exts:
        continue
    try:
        t = f.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    t = t.replace("https://sfg246.github.io/RelicPrison/", "https://sfg246.github.io/RelicPRisonDocs/")
    f.write_text(t, encoding="utf-8")

# Do not advertise private source or free GitHub release binaries.
(wiki / "releases" / "index.md").write_text("""# Release & Download Status

<div class=\"release-hero\">
<strong>Current release:</strong> <code>RelicPrison 1.0.0</code><br><br>
<span class=\"status-pill\">Paper 1.21.5–26.2 startup tested</span>
<span class=\"status-pill\">Java 25</span>
<span class=\"status-pill\">Stable / final</span>
</div>

## Release status

`1.0.0` is the official stable RelicPrison release. The exact release JAR has been startup-tested on Paper `1.21.5`, `1.21.6`, `1.21.7`, `1.21.8`, `1.21.9`, `1.21.10`, `1.21.11`, `26.1.1`, `26.1.2`, and `26.2` using Java 25.

Paper `1.21.4` and older are not advertised as supported by the current 1.0.0 JAR.

## Where do I download RelicPrison?

RelicPrison is distributed through its official marketplace listing. The plugin source repository and release binaries are private and are not distributed through this documentation repository.

This repository contains documentation, released configuration snapshots, and public API signature references only.

## Before installing

1. Use Paper within the documented startup-tested range.
2. Use Java 25.
3. Install Vault, LuckPerms, and a Vault-compatible economy provider.
4. Verify optional integrations before enabling them on a production server.
5. Read the manual verification boundaries in [Known Limitations](/known-limitations).

See [1.0.0 Release Notes](/releases/1.0.0), [Compatibility Matrix](/reference/compatibility), and [Known Limitations](/known-limitations).
""", encoding="utf-8")

(dest / "README.md").write_text("""# RelicPrison Documentation

Public website and documentation source for RelicPrison.

**Documentation:** https://sfg246.github.io/RelicPRisonDocs/

This repository intentionally contains **no RelicPrison implementation source code and no paid plugin JARs**. The plugin implementation is maintained separately in a private repository.

## What is public here

- Installation and setup guides
- System documentation
- Commands, permissions, placeholders, and compatibility references
- Released configuration snapshots used by the generated YAML reference
- Public API signature snapshots
- Upgrade, troubleshooting, recovery, and release documentation

The VitePress website source lives in [`wiki/`](wiki/README.md).
""", encoding="utf-8")

(dest / ".gitignore").write_text("wiki/node_modules/\nwiki/.vitepress/cache/\nwiki/.vitepress/dist/\n.DS_Store\n", encoding="utf-8")
