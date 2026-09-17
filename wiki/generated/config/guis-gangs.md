# guis/gangs.yml

GUI YAML controls presentation. The visual gallery explains how these files map to the in-game inventories.

**Source:** [`src/main/resources/guis/gangs.yml`](https://github.com/Sfg246/RelicPRisonDocs/blob/main/snapshots/resources/guis/gangs.yml)

**Documented leaves:** 15

| Setting | Type | Packaged default | Recommended starting point | What it changes | Risk / common mistake |
| --- | --- | --- | --- | --- | --- |
| `title` | string | `&8Gang &7• &dHeadquarters` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `title` for this section of guis/gangs.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `members-title` | string | `&8Gang &7• &aMembers` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `members-title` for this section of guis/gangs.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `member-title` | string | `&8Gang &7• &aMember Profile` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `member-title` for this section of guis/gangs.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `ranks-title` | string | `&8Gang &7• &eRanks` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `ranks-title` for this section of guis/gangs.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `rank-edit-title` | string | `&8Gang &7• &eRank Editor` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `rank-edit-title` for this section of guis/gangs.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `rank-permissions-title` | string | `&8Gang &7• &eRank Permissions` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Names the permission node checked for the related action. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `upgrades-title` | string | `&8Gang &7• &6Upgrades` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `upgrades-title` for this section of guis/gangs.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `bank-title` | string | `&8Gang &7• &6Bank` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `bank-title` for this section of guis/gangs.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `stats-title` | string | `&8Gang &7• &bStatistics` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `stats-title` for this section of guis/gangs.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `contributions-title` | string | `&8Gang &7• &bContributions` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `contributions-title` for this section of guis/gangs.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `boosters-title` | string | `&8Gang &7• &dBoosters` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `boosters-title` for this section of guis/gangs.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `missions-title` | string | `&8Gang &7• &eMissions` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `missions-title` for this section of guis/gangs.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `leaderboards-title` | string | `&8Gang &7• &bLeaderboards` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `leaderboards-title` for this section of guis/gangs.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `settings-title` | string | `&8Gang &7• &eSettings` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `settings-title` for this section of guis/gangs.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `audit-title` | string | `&8Gang &7• &bAudit Log` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `audit-title` for this section of guis/gangs.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |

::: tip Safe editing loop
Back up first, change one idea at a time, reload only supported modules, then run `/rp validate` and `/rp diagnose`. Use a full restart for storage/backend changes or anything the plugin documents as startup-only.
:::
