# storage.yml

The table is generated from the current packaged YAML, so defaults stay synchronized with the source.

**Source:** [`src/main/resources/storage.yml`](https://github.com/Sfg246/RelicPRisonDocs/blob/main/snapshots/resources/storage.yml)

**Documented leaves:** 16

| Setting | Type | Packaged default | Recommended starting point | What it changes | Risk / common mistake |
| --- | --- | --- | --- | --- | --- |
| `file-version` | number | `1` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `file-version` for this section of storage.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `type` | string | `SQLITE` | SQLITE for a single server; MYSQL for deliberately shared multi-server data. | Chooses the persistence backend used by RelicPrison. | Changing database type without a migration plan can make existing data appear missing. |
| `sqlite.file` | string | `player-data.db` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `file` for this section of storage.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `mysql.host` | string | `localhost` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `host` for this section of storage.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `mysql.port` | number | `3306` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `port` for this section of storage.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `mysql.database` | string | `relicprison` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `database` for this section of storage.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `mysql.username` | string | `relicprison` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `username` for this section of storage.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `mysql.password` | string | `change-me` | Use a real secret when MySQL is enabled. | Configures `password` for this section of storage.yml. | Never commit a production database password to Git. |
| `mysql.parameters` | string | `useSSL=false&allowPublicKeyRetrieval=true&serverTimezone=UTC` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `parameters` for this section of storage.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `mysql.pool-size` | number | `6` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `pool-size` for this section of storage.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `queue.capacity` | number | `10000` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `capacity` for this section of storage.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `queue.retry-count` | number | `3` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `retry-count` for this section of storage.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `queue.retry-delay-millis` | number | `250` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Controls a duration or timing value for this behavior. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `player-loading.timeout-seconds` | number | `15` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Controls how long RelicPrison waits before the operation/session is treated as timed out. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `save-interval-seconds` | number | `20` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Controls how often the related task or action is scheduled. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `shutdown-flush-timeout-seconds` | number | `10` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Controls how long RelicPrison waits before the operation/session is treated as timed out. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |

::: tip Safe editing loop
Back up first, change one idea at a time, reload only supported modules, then run `/rp validate` and `/rp diagnose`. Use a full restart for storage/backend changes or anything the plugin documents as startup-only.
:::
