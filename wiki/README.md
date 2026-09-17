# RelicPrison Public Wiki

This directory contains the public VitePress documentation site for RelicPrison.

## Local development

```bash
cd wiki
npm install
npm run docs:dev
```

## Production build

```bash
cd wiki
npm run docs:build
```

The build regenerates the YAML reference from the released configuration snapshots in `snapshots/resources`, refreshes release-status pages from the public changelog/limitations files, and then builds VitePress.

The generated API pages are public signature snapshots from RelicPrison 1.0.0. The plugin implementation source, private engineering notes, tests, and paid JARs are intentionally not stored in this repository.
