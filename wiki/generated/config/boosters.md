# boosters.yml

The table is generated from the current packaged YAML, so defaults stay synchronized with the source.

**Source:** [`src/main/resources/boosters.yml`](https://github.com/Sfg246/RelicPRisonDocs/blob/main/snapshots/resources/boosters.yml)

**Documented leaves:** 14

| Setting | Type | Packaged default | Recommended starting point | What it changes | Risk / common mistake |
| --- | --- | --- | --- | --- | --- |
| `file-version` | number | `2` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `file-version` for this section of boosters.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `settings.stacking-mode` | string | `MULTIPLY_ALL` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `stacking-mode` for this section of boosters.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `settings.maximum-final-multiplier` | number | `100` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Sets a safety or capacity limit for the related system. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `settings.maximum-booster-multiplier` | number | `25` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Sets a safety or capacity limit for the related system. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `settings.maximum-duration-seconds` | number | `2592000` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Sets a safety or capacity limit for the related system. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `settings.offline-time-continues` | boolean | `true` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `offline-time-continues` for this section of boosters.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `settings.strength-stacks` | boolean | `false` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `strength-stacks` for this section of boosters.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `settings.duration-stacks` | boolean | `true` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `duration-stacks` for this section of boosters.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `item.material` | string | `NETHER_STAR` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Selects the Minecraft/custom material or block identifier used here. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `item.name` | string | `&d&l{multiplier}x {type} Sell Booster` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `name` for this section of boosters.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `item.lore` | list | `["&7Duration: &f{duration}","&7Type: &f{type}","","&eRight-click to activate."]` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `lore` for this section of boosters.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `item.custom-model-data` | number | `0` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `custom-model-data` for this section of boosters.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `permission-multipliers.relicprison.multiplier.vip` | number | `1.1` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `vip` for this section of boosters.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `permission-multipliers.relicprison.multiplier.mvp` | number | `1.2` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `mvp` for this section of boosters.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |

::: tip Safe editing loop
Back up first, change one idea at a time, reload only supported modules, then run `/rp validate` and `/rp diagnose`. Use a full restart for storage/backend changes or anything the plugin documents as startup-only.
:::
