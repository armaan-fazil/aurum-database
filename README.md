# aurum-database

Pictures, clips and logos for **Aurum**, the offline Warframe market and farming app.

Every copy of Aurum checks this repo during a sync: it downloads `manifest.json` and then only the
files that are new or changed, into its own `database/assets/` folder. Those copies are shown in
place of the ones bundled with the app, so adding or fixing a picture here updates every copy of
Aurum on its next sync, with no new release. Aurum never contacts this repo outside a sync.

## Layout

The folders mirror Aurum's `ui/` folder:

- `media/guides/` – guide pictures (`.png`) and clips (`.mp4`), named after the slot key shown in the
  guide's placeholder, e.g. `kuva-larvling.png`, `kuva-escape.mp4`.
- `media/` – weekly-activity backgrounds and other app pictures.
- `farm/logos/` – syndicate logos for the Farming page.
- `cache/images/` – pictures Aurum would otherwise download itself (warframe.market item icons, mod art in `art/`,
  wiki pictures in `weekly/`). A copy of Aurum takes them from here during a sync and only goes to the market or
  the wiki for pictures that aren't here yet. Fill it from a PC with **Upload Pictures to Repo (Windows).bat** in the
  Aurum folder (needs Git; it signs in through your browser the first time).

## Adding or changing a file

1. Put the file in the right folder with the right name (clips: H.264 `.mp4`, kept short).
2. Blur other players' names, chat and anything private first.
3. Run `python tools/make_manifest.py` to rebuild `manifest.json`.
4. Commit and push. Copies of Aurum pick it up on their next sync.

Removing a file here (and rebuilding the manifest) makes Aurum delete its synced copy and fall back to
the bundled one, if there is one.
