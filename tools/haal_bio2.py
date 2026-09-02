"""Maakt bronnen/bio2.json uit de gedeelde BIO2-dataset van cisochat.

De dataset van cisochat is de bron: 148 overheidsmaatregelen, genummerd volgens de structuur van
ISO 27002:2022 (8.15.01 hoort bij ISO-maatregel 8.15). Applicatiecheck werkt per overheidsmaatregel,
want dat is het niveau waarop een dossier wordt gelezen; daarom blijven alle 148 apart staan.

Wat wordt overgenomen: nummer, titel, thema (de IV-standaard uit BIO2), het ISO-nummer en de tekst
van de overheidsmaatregel zelf (die is van CIP en openbaar). Wat niet: de tekst van de ISO-maatregel,
die is auteursrechtelijk beschermd en we hebben hem niet nodig.

Aanroep:
    python tools/haal_bio2.py            schrijft bronnen/bio2.json
    python tools/haal_bio2.py --check    faalt als de kopie afwijkt van de bron (CI)
"""
from __future__ import annotations

import json
import pathlib
import re
import subprocess
import sys

HIER = pathlib.Path(__file__).resolve().parent
REPO = HIER.parent
UIT = REPO / "bronnen" / "bio2.json"
# tools -> applicatiecheck -> de werkmap met alle repo's ernaast.
STANDAARD_BRON = REPO.parent / "cisochat" / "data" / "bio2.json"


def iso_nummer(sub_id: str) -> str:
    """8.15.01 hoort bij ISO-maatregel 8.15."""
    hoofdstuk, maatregel, _ = sub_id.split(".")
    return f"{int(hoofdstuk)}.{int(maatregel)}"


def schoon(tekst: str | None) -> str:
    """Teksten in de bron bevatten afbreekregels en losse aanhalingstekens uit de oorspronkelijke tabel."""
    return re.sub(r"\s+", " ", tekst or "").strip().rstrip("'")


def commit_van(pad: pathlib.Path) -> str:
    """De commit waar de bron uit komt, zodat een kopie te herleiden is."""
    try:
        uit = subprocess.run(
            ["git", "-C", str(pad.parent), "log", "-1", "--format=%H", "--", pad.name],
            capture_output=True, text=True, timeout=10,
        )
        return uit.stdout.strip() or "onbekend"
    except (OSError, subprocess.SubprocessError):
        return "onbekend"


def bouw(bron_pad: pathlib.Path) -> dict:
    bron = json.loads(bron_pad.read_text(encoding="utf-8"))
    maatregelen = [
        {
            "id": c["id"],
            "iso": iso_nummer(c["id"]),
            "titel": schoon(c["titel"]),
            "thema": schoon(c.get("iv_standaard")) or "Overig",
            "overheidsmaatregel": schoon(c.get("overheidsmaatregel")),
        }
        for c in bron["controls"]
    ]
    return {
        "kader": "bio2",
        "titel": "BIO 2.0",
        "toelichting": (
            "De 148 overheidsmaatregelen van BIO 2.0, elk met nummer, titel, thema en de tekst van de "
            "overheidsmaatregel. De ISO-tekst staat er niet bij; die is auteursrechtelijk beschermd."
        ),
        "bron": {
            "naam": bron.get("bron", "Centrum Informatiebeveiliging en Privacybescherming (CIP)"),
            "versie": bron.get("versie", "BIO2 v1.3"),
            "herkomst": "security-commons-nl/cisochat, data/bio2.json",
            "commit": commit_van(bron_pad),
            "let_op": "Gegenereerd met tools/haal_bio2.py. Wijzig de dataset in cisochat, niet dit bestand.",
        },
        "maatregelen": maatregelen,
    }


def main() -> int:
    argv = [a for a in sys.argv[1:] if not a.startswith("--")]
    check = "--check" in sys.argv
    bron_pad = pathlib.Path(argv[0]) if argv else STANDAARD_BRON
    if not bron_pad.exists():
        if check:
            print(f"bron niet gevonden ({bron_pad}); controle overgeslagen")
            return 0
        sys.exit(f"bron niet gevonden: {bron_pad}")
    data = bouw(bron_pad)
    tekst = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    if check:
        huidig = UIT.read_text(encoding="utf-8") if UIT.exists() else ""
        # De commit-hash mag verschillen (die staat alleen ter herleiding); de inhoud niet.
        strip = lambda t: re.sub(r'"commit": "[^"]*"', '"commit": ""', t)
        if strip(huidig) != strip(tekst):
            print("bronnen/bio2.json loopt achter op cisochat/data/bio2.json; draai tools/haal_bio2.py")
            return 1
        print("bronnen/bio2.json loopt gelijk met de bron")
        return 0
    UIT.parent.mkdir(exist_ok=True)
    UIT.write_text(tekst, encoding="utf-8")
    print(f"{UIT}: {len(data['maatregelen'])} maatregelen uit {bron_pad} (commit {data['bron']['commit'][:8]})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
