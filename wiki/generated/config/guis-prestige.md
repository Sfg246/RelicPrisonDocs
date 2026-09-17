# guis/prestige.yml

GUI YAML controls presentation. The visual gallery explains how these files map to the in-game inventories.

**Source:** [`src/main/resources/guis/prestige.yml`](https://github.com/Sfg246/RelicPRisonDocs/blob/main/snapshots/resources/guis/prestige.yml)

**Documented leaves:** 3

| Setting | Type | Packaged default | Recommended starting point | What it changes | Risk / common mistake |
| --- | --- | --- | --- | --- | --- |
| `file-version` | number | `2` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `file-version` for this section of guis/prestige.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `title` | string | `&8Progression &7• &dPrestige` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `title` for this section of guis/prestige.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `prestige-confirm-title` | string | `&4&lConfirm Prestige` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `prestige-confirm-title` for this section of guis/prestige.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |

::: tip Safe editing loop
Back up first, change one idea at a time, reload only supported modules, then run `/rp validate` and `/rp diagnose`. Use a full restart for storage/backend changes or anything the plugin documents as startup-only.
:::
