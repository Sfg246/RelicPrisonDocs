# backups.yml

The table is generated from the current packaged YAML, so defaults stay synchronized with the source.

**Source:** [`src/main/resources/backups.yml`](https://github.com/Sfg246/RelicPRisonDocs/blob/main/snapshots/resources/backups.yml)

**Documented leaves:** 5

| Setting | Type | Packaged default | Recommended starting point | What it changes | Risk / common mistake |
| --- | --- | --- | --- | --- | --- |
| `file-version` | number | `1` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `file-version` for this section of backups.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `automatic.enabled` | boolean | `true` | Begin with the packaged default, then enable features one at a time on staging. | Turns this feature or behavior on or off. | Enabling a dependency-backed feature before its dependency is ready can fail validation or behavior checks. |
| `automatic.interval-minutes` | number | `1440` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Controls how often the related task or action is scheduled. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `automatic.type` | string | `full` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `type` for this section of backups.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `retention.keep` | number | `20` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `keep` for this section of backups.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |

::: tip Safe editing loop
Back up first, change one idea at a time, reload only supported modules, then run `/rp validate` and `/rp diagnose`. Use a full restart for storage/backend changes or anything the plugin documents as startup-only.
:::
