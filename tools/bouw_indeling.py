"""Schrijft indeling.md uit bewijs.json: de tabel per bewijssoort, leesbaar op de pagina.

bewijs.json is de bron en wordt met de hand bijgehouden; indeling.md is een afgeleide en wordt
gecommit omdat de site-build alleen Markdown leest.

Aanroep:
    python tools/bouw_indeling.py            schrijft indeling.md
    python tools/bouw_indeling.py --check    faalt als indeling.md niet meer bij bewijs.json past (CI)
"""
from __future__ import annotations

import json
import pathlib
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
BRON = REPO / "bewijs.json"
UIT = REPO / "indeling.md"
VOLGORDE = ["A", "B", "C", "D"]
KOPPEN = {
    "A": "A. Configuratie-export",
    "B": "B. Logsample",
    "C": "C. Document of schermafbeelding",
    "D": "D. Niet uit de applicatie",
}


def laad() -> dict:
    return json.loads(BRON.read_text(encoding="utf-8"))


def cel(tekst: str) -> str:
    return tekst.replace("|", "\\|").replace("\n", " ").strip()


def bouw(data: dict) -> str:
    rijen = data["maatregelen"]
    telling = {s: sum(1 for r in rijen if r["soort"][0] == s) for s in VOLGORDE}
    met_ab = sum(1 for r in rijen if set(r["soort"]) & {"A", "B"})
    regels = [
        "# Indeling: welk bewijs per maatregel",
        "",
        f"Van de {len(rijen)} overheidsmaatregelen in BIO2 kan een gekochte applicatie er {met_ab} geheel of "
        f"gedeeltelijk zelf aantonen uit configuratie (A) of log (B). Voor {telling['C']} ligt het bewijs in een "
        f"document of schermafbeelding (C), en {telling['D']} liggen buiten de applicatie (D). "
        f"Peildatum {data['peildatum']}; status van elke rij: *{rijen[0]['status']}*.",
        "",
        "> " + data["toelichting"],
        "",
        f"Bron van de maatregelen: `{data['bron_bio2']['bestand']}`, {data['bron_bio2']['versie']} "
        f"(kopie uit [normen](https://github.com/security-commons-nl/normen), vingerafdruk "
        f"`{data['bron_bio2']['vingerafdruk'][:12]}`). Hier staan nummer, titel, thema en de indeling; de "
        "tekst van een overheidsmaatregel staat bij het CIP (CC BY-NC-SA), niet in de commons.",
        "",
        f"Kolom CIP: het object uit de {data['bron_cip']['titel']} ({data['bron_cip']['versie']}) dat de maatregel "
        "raakt; B = beleid, U = uitvoering, C = control. Alleen objectnummers, geen overgenomen tekst (CC BY-NC-SA).",
        "",
        "| Soort | Betekenis | Aantal (eerste soort) |",
        "|---|---|---|",
    ]
    for s in VOLGORDE:
        regels.append(f"| **{s}** | {cel(data['soorten'][s])} | {telling[s]} |")
    regels.append("")
    for s in VOLGORDE:
        groep = [r for r in rijen if r["soort"][0] == s]
        regels += [f"## {KOPPEN[s]} ({len(groep)})", ""]
        if s == "D":
            regels += ["| Nr | Titel | Thema | CIP | Waarom niet uit de applicatie |", "|---|---|---|---|---|"]
            for r in groep:
                regels.append(f"| {r['id']} | {cel(r['titel'])} | {cel(r['thema'])} | {r.get('cip', '')} | {cel(r['motivering'])} |")
        else:
            regels += ["| Nr | Titel | Soort | Bron | Wat het bewijs moet bevatten | ASVS | CIP | Motivering |",
                       "|---|---|---|---|---|---|---|---|"]
            for r in groep:
                regels.append(
                    f"| {r['id']} | {cel(r['titel'])} | {' + '.join(r['soort'])} | {r['bron']} | "
                    f"{cel(r['bewijs'])} | {cel(r['asvs'])} | {r.get('cip', '')} | {cel(r['motivering'])} |"
                )
        regels.append("")
    regels += [
        "## Meedenken",
        "",
        "Elke rij is een voorstel. Klopt een indeling niet voor jouw zaaksysteem, of ontbreekt bewijs dat de "
        "applicatie wél kan leveren: open een issue met het nummer van de maatregel in de titel. De bron is "
        "`bewijs.json`; deze pagina wordt daaruit gegenereerd met `tools/bouw_indeling.py`.",
        "",
    ]
    return "\n".join(regels)


def main() -> int:
    tekst = bouw(laad())
    if "--check" in sys.argv:
        huidig = UIT.read_text(encoding="utf-8") if UIT.exists() else ""
        if huidig != tekst:
            print("indeling.md loopt achter op bewijs.json; draai tools/bouw_indeling.py")
            return 1
        print("indeling.md loopt gelijk met bewijs.json")
        return 0
    UIT.write_text(tekst, encoding="utf-8")
    print(f"{UIT}: {tekst.count(chr(10))} regels")
    return 0


if __name__ == "__main__":
    sys.exit(main())
