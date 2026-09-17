# guis/admin.yml

GUI YAML controls presentation. The visual gallery explains how these files map to the in-game inventories.

**Source:** [`src/main/resources/guis/admin.yml`](https://github.com/Sfg246/RelicPRisonDocs/blob/main/snapshots/resources/guis/admin.yml)

**Documented leaves:** 13

| Setting | Type | Packaged default | Recommended starting point | What it changes | Risk / common mistake |
| --- | --- | --- | --- | --- | --- |
| `file-version` | number | `2` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `file-version` for this section of guis/admin.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `title` | string | `&8Admin &7• &cControl Center` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `title` for this section of guis/admin.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `submenus.mine-manager` | string | `&8Admin &7• &bMine Manager` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `mine-manager` for this section of guis/admin.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `submenus.composition-editor` | string | `&8Admin &7• &aComposition` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `composition-editor` for this section of guis/admin.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `submenus.reset-settings-editor` | string | `&8Admin &7• &cReset Settings` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `reset-settings-editor` for this section of guis/admin.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `submenus.rank-editor` | string | `&8Admin &7• &bRank Editor` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `rank-editor` for this section of guis/admin.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `submenus.prestige-editor` | string | `&8Admin &7• &dPrestige Editor` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `prestige-editor` for this section of guis/admin.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `submenus.sell-price-editor` | string | `&8Admin &7• &6Sell Prices` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Sets an economy amount used by the related action. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `submenus.booster-manager` | string | `&8Admin &7• &dBoosters` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `booster-manager` for this section of guis/admin.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `submenus.block-event-editor` | string | `&8Admin &7• &cBlock Events` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `block-event-editor` for this section of guis/admin.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `submenus.integration-status` | string | `&8Admin &7• &bIntegrations` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `integration-status` for this section of guis/admin.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `submenus.diagnostics` | string | `&8Admin &7• &bDiagnostics` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `diagnostics` for this section of guis/admin.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `submenus.player-progression-manager` | string | `&8Admin &7• &bPlayers` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `player-progression-manager` for this section of guis/admin.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |

::: tip Safe editing loop
Back up first, change one idea at a time, reload only supported modules, then run `/rp validate` and `/rp diagnose`. Use a full restart for storage/backend changes or anything the plugin documents as startup-only.
:::
