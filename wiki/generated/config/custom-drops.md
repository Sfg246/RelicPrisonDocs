# custom-drops.yml

The table is generated from the current packaged YAML, so defaults stay synchronized with the source.

**Source:** [`src/main/resources/custom-drops.yml`](https://github.com/Sfg246/RelicPRisonDocs/blob/main/snapshots/resources/custom-drops.yml)

**Documented leaves:** 15

| Setting | Type | Packaged default | Recommended starting point | What it changes | Risk / common mistake |
| --- | --- | --- | --- | --- | --- |
| `file-version` | number | `3` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `file-version` for this section of custom-drops.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `custom-drops.ancient-fragment.enabled` | boolean | `false` | Begin with the packaged default, then enable features one at a time on staging. | Turns this feature or behavior on or off. | Enabling a dependency-backed feature before its dependency is ready can fail validation or behavior checks. |
| `custom-drops.ancient-fragment.priority` | number | `100` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `priority` for this section of custom-drops.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `custom-drops.ancient-fragment.exclusive` | boolean | `false` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `exclusive` for this section of custom-drops.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `custom-drops.ancient-fragment.blocks` | list | `["DIAMOND_ORE","EMERALD_ORE"]` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `blocks` for this section of custom-drops.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `custom-drops.ancient-fragment.mines` | list | `["diamond","emerald","immortal"]` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `mines` for this section of custom-drops.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `custom-drops.ancient-fragment.minimum-prestige` | string | `diamond` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Sets the lower bound used by the related system. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `custom-drops.ancient-fragment.permissions` | list | `[]` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Names the permission node checked for the related action. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `custom-drops.ancient-fragment.chance` | number | `0.25` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `chance` for this section of custom-drops.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `custom-drops.ancient-fragment.fortune-applicable` | boolean | `false` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `fortune-applicable` for this section of custom-drops.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `custom-drops.ancient-fragment.per-action-item-limit` | number | `64` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Sets a safety or capacity limit for the related system. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `custom-drops.ancient-fragment.per-action-command-limit` | number | `8` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Sets a safety or capacity limit for the related system. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `custom-drops.ancient-fragment.rewards.items[0].id` | string | `itemsadder:relics:ancient_fragment` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Stores the stable identifier used to reference this object. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `custom-drops.ancient-fragment.rewards.items[0].amount` | number | `1` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `amount` for this section of custom-drops.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `custom-drops.ancient-fragment.rewards.commands` | list | `[]` | Start empty, then add only commands you have tested for duplicate/retry behavior. | Configures `commands` for this section of custom-drops.yml. | Third-party commands cannot participate in RelicPrison’s SQL transaction and may not be exactly-once. |

::: tip Safe editing loop
Back up first, change one idea at a time, reload only supported modules, then run `/rp validate` and `/rp diagnose`. Use a full restart for storage/backend changes or anything the plugin documents as startup-only.
:::
