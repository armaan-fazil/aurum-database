"""Rebuild manifest.json after adding, changing or removing files.

Run from the repo folder:  python tools/make_manifest.py
Aurum downloads manifest.json during a sync and fetches only the files whose SHA-256 changed.
Files under media/ and farm/ replace the app's own; cache/images/ fills its picture cache (item icons, mod art, wiki pictures).
"""
import hashlib
import json
import os
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOP = ("media", "farm", "cache")
EXT = (".png", ".jpg", ".jpeg", ".webp", ".gif", ".mp4", ".webm", ".svg", ".json")

files = {}
for top in TOP:
    for dp, _, fs in os.walk(os.path.join(ROOT, top)):
        for f in sorted(fs):
            if not f.lower().endswith(EXT):
                continue
            p = os.path.join(dp, f)
            rel = os.path.relpath(p, ROOT).replace(os.sep, "/")
            with open(p, "rb") as fh:
                data = fh.read()
            files[rel] = {"sha256": hashlib.sha256(data).hexdigest(), "size": len(data)}

out = {"updated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "files": dict(sorted(files.items()))}
with open(os.path.join(ROOT, "manifest.json"), "w", encoding="utf-8") as fh:
    json.dump(out, fh, indent=1)
print(f"manifest.json: {len(files)} files, {sum(v['size'] for v in files.values()) / 1e6:.1f} MB")
