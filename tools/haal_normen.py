#!/usr/bin/env python3
"""Haalt BIO 2.0 op uit de repo `normen`.

`normen` is sinds 02-09-2026 de bron van de normbronnen (besluit in `.github/BESLUITEN.md`). Deze repo
legt daar de bewijssoort op (`bewijs.json`) en leest een kopie in `bronnen/bio2.json`. Een kopie zonder
bewaking wordt binnen een half jaar een tweede waarheid; daarom staat de vingerafdruk van `normen` in de
kopie en meldt `--check` of hij nog klopt.

De kopie bevat alleen nummer, titel en thema. De tekst van de overheidsmaatregel gaat niet mee: het CIP
publiceert onder CC BY-NC-SA 4.0 en dat is niet te verenigen met herdistributie onder EUPL-1.2. Wie de
tekst nodig heeft, gaat naar de bron; het nummer hier is ook het nummer daar.

Gebruik:
    python tools/haal_normen.py            kopieren
    python tools/haal_normen.py --check    melden of de kopie nog klopt (CI)

Alleen standaardbibliotheek.
"""
from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOEL = ROOT / "bronnen" / "bio2.json"
# Lokaal staat normen naast deze repo; in CI wordt hij binnen de workspace uitgecheckt als _normen.
KANDIDATEN = (ROOT.parent / "normen", ROOT / "_normen")
KADER = "bio2"


def normen_map() -> pathlib.Path:
    for pad in KANDIDATEN:
        if (pad / f"{KADER}.json").is_file():
            return pad
    plekken = "\n".join(f"  {p}" for p in KANDIDATEN)
    sys.exit(f"repo normen niet gevonden. Gezocht op:\n{plekken}\n"
             "Zet normen naast deze repo, of check hem uit als _normen.")


def lees(pad: pathlib.Path) -> dict:
    return json.loads(pad.read_text(encoding="utf-8"))


def main(argv: list[str]) -> int:
    alleen_check = "--check" in argv
    bron_map = normen_map()
    bron = lees(bron_map / f"{KADER}.json")

    if alleen_check:
        if not DOEL.is_file():
            print("bronnen/bio2.json ontbreekt; draai python tools/haal_normen.py")
            return 1
        kopie = lees(DOEL)
        if kopie.get("vingerafdruk") != bron["vingerafdruk"]:
            print(f"bronnen/bio2.json: kopie {str(kopie.get('vingerafdruk'))[:12]} != normen "
                  f"{bron['vingerafdruk'][:12]}; draai python tools/haal_normen.py")
            return 1
        print("bronnen/bio2.json loopt gelijk met normen.")
        return 0

    DOEL.parent.mkdir(exist_ok=True)
    DOEL.write_bytes((json.dumps(bron, ensure_ascii=False, indent=1) + "\n").encode("utf-8"))
    print(f"{DOEL}: {len(bron['maatregelen'])} maatregelen uit {bron_map} "
          f"(vingerafdruk {bron['vingerafdruk'][:12]})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
