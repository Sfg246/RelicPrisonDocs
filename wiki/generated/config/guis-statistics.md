# guis/statistics.yml

GUI YAML controls presentation. The visual gallery explains how these files map to the in-game inventories.

**Source:** [`src/main/resources/guis/statistics.yml`](https://github.com/Sfg246/RelicPRisonDocs/blob/main/snapshots/resources/guis/statistics.yml)

**Documented leaves:** 3

| Setting | Type | Packaged default | Recommended starting point | What it changes | Risk / common mistake |
| --- | --- | --- | --- | --- | --- |
| `file-version` | number | `2` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `file-version` for this section of guis/statistics.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `title` | string | `&8Profile &7• &bStatistics` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `title` for this section of guis/statistics.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `leaderboard-title` | string | `&8Statistics &7• &bLeaderboard` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `leaderboard-title` for this section of guis/statistics.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |

::: tip Safe editing loop
Back up first, change one idea at a time, reload only supported modules, then run `/rp validate` and `/rp diagnose`. Use a full restart for storage/backend changes or anything the plugin documents as startup-only.
:::
