# guis/progression.yml

GUI YAML controls presentation. The visual gallery explains how these files map to the in-game inventories.

**Source:** [`src/main/resources/guis/progression.yml`](https://github.com/Sfg246/RelicPRisonDocs/blob/main/snapshots/resources/guis/progression.yml)

**Documented leaves:** 4

| Setting | Type | Packaged default | Recommended starting point | What it changes | Risk / common mistake |
| --- | --- | --- | --- | --- | --- |
| `file-version` | number | `2` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `file-version` for this section of guis/progression.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `title` | string | `&8Progression &7• &bRanks` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `title` for this section of guis/progression.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `rankup-confirm-title` | string | `&4&lConfirm Rankup` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `rankup-confirm-title` for this section of guis/progression.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `rankup-max-confirm-title` | string | `&4&lConfirm Rankup Max` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Sets a safety or capacity limit for the related system. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |

::: tip Safe editing loop
Back up first, change one idea at a time, reload only supported modules, then run `/rp validate` and `/rp diagnose`. Use a full restart for storage/backend changes or anything the plugin documents as startup-only.
:::
