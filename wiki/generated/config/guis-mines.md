# guis/mines.yml

GUI YAML controls presentation. The visual gallery explains how these files map to the in-game inventories.

**Source:** [`src/main/resources/guis/mines.yml`](https://github.com/Sfg246/RelicPRisonDocs/blob/main/snapshots/resources/guis/mines.yml)

**Documented leaves:** 7

| Setting | Type | Packaged default | Recommended starting point | What it changes | Risk / common mistake |
| --- | --- | --- | --- | --- | --- |
| `file-version` | number | `2` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `file-version` for this section of guis/mines.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `title` | string | `&8Mines &7• &bWarp Directory` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `title` for this section of guis/mines.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `size` | number | `54` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Configures `size` for this section of guis/mines.yml. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `contextual-mine-materials` | boolean | `true` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Selects the Minecraft/custom material or block identifier used here. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `enabled-mine-material` | string | `DIAMOND_PICKAXE` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Selects the Minecraft/custom material or block identifier used here. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `disabled-mine-material` | string | `RED_STAINED_GLASS_PANE` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Selects the Minecraft/custom material or block identifier used here. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |
| `filler-material` | string | `BLACK_STAINED_GLASS_PANE` | Keep the packaged default for the first successful staging run; tune only with a specific reason. | Selects the Minecraft/custom material or block identifier used here. | Wrong type or unsupported value can fail validation/reload or change gameplay unexpectedly. |

::: tip Safe editing loop
Back up first, change one idea at a time, reload only supported modules, then run `/rp validate` and `/rp diagnose`. Use a full restart for storage/backend changes or anything the plugin documents as startup-only.
:::
