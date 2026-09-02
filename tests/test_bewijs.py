"""bewijs.json dekt elke overheidsmaatregel uit de BIO2-kopie precies één keer, met geldige waarden,
en de afgeleiden (indeling.md, bronnen/bio2.json) lopen gelijk met hun bron."""
import json
import pathlib
import re
import subprocess
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
BEWIJS = json.loads((REPO / "bewijs.json").read_text(encoding="utf-8"))
BIO2 = json.loads((REPO / "bronnen" / "bio2.json").read_text(encoding="utf-8"))
SOORTEN = {"A", "B", "C", "D"}
BRONNEN = {"eigen", "leverancier", "nvt"}


def test_elke_maatregel_precies_een_keer():
    ids = [r["id"] for r in BEWIJS["maatregelen"]]
    assert len(ids) == len(set(ids)), "dubbele nummers in bewijs.json"
    assert set(ids) == {m["id"] for m in BIO2["maatregelen"]}, "bewijs.json en bronnen/bio2.json dekken niet dezelfde maatregelen"


def test_titels_volgen_de_bron():
    """Vergelijkt op genormaliseerde witruimte.

    Zestig van de 148 titels in normen dragen nog de afbreekregels van de oorspronkelijke CIP-tabel
    ("Rollen en verantwoordelijkheden bij \ninformatiebeveiliging"). Hier staan ze op een regel, want een
    titel met een harde newline is niet te tonen in een tabel. Twee titels dragen daarnaast een losse
    afsluitende apostrof ("User endpoint devices'"); die valt onder dezelfde normalisatie. Wordt normen
    opgeschoond, dan blijft deze test groen; de vingerafdruk bewaakt de inhoud byte-exact.
    """
    plat = lambda t: re.sub(r"\s+", " ", t).strip().rstrip("'")
    titels = {m["id"]: m["titel"] for m in BIO2["maatregelen"]}
    for r in BEWIJS["maatregelen"]:
        assert plat(r["titel"]) == plat(titels[r["id"]]), f"{r['id']}: titel wijkt af van de bron"


def test_waarden_geldig():
    for r in BEWIJS["maatregelen"]:
        assert r["soort"] and set(r["soort"]) <= SOORTEN, f"{r['id']}: onbekende soort {r['soort']}"
        assert len(r["soort"]) == len(set(r["soort"])), f"{r['id']}: dubbele soort"
        assert r["bron"] in BRONNEN, f"{r['id']}: onbekende bron {r['bron']}"
        assert r["status"] in {"voorlopig", "bevestigd"}, f"{r['id']}: onbekende status"


def test_a_b_c_zeggen_wat_het_bewijs_moet_bevatten():
    for r in BEWIJS["maatregelen"]:
        if r["soort"][0] == "D":
            assert r["bron"] == "nvt" and not r["bewijs"], f"{r['id']}: D hoort geen bewijs te noemen"
        else:
            assert r["bewijs"], f"{r['id']}: {r['soort'][0]} zonder beschrijving van het bewijs"
            assert r["bron"] != "nvt", f"{r['id']}: {r['soort'][0]} zonder bron (eigen of leverancier)"
        assert r["motivering"], f"{r['id']}: geen motivering"


def test_bewijs_verwijst_naar_dezelfde_bio2_kopie():
    assert BEWIJS["bron_bio2"]["vingerafdruk"] == BIO2["vingerafdruk"]
    assert BEWIJS["bron_bio2"]["versie"] == BIO2["versie"]


def test_geen_tekst_van_het_cip_in_de_repo():
    """Het CIP publiceert onder CC BY-NC-SA; dat is niet te verenigen met EUPL-herdistributie.

    Nummers, titels en thema's blijven (die zijn van iedereen); de tekst van een overheidsmaatregel en
    de ISO-tekst niet. Besluit 02-09-2026. Deze test blokkeert een terugval.
    """
    verboden = ("overheidsmaatregel", "iso_maatregel", "risico")
    for m in BIO2["maatregelen"]:
        assert set(m) == {"id", "titel", "thema"}, f"{m['id']}: onverwachte velden {sorted(set(m) - {'id', 'titel', 'thema'})}"
    for veld in verboden:
        assert f'"{veld}"' not in (REPO / "bronnen" / "bio2.json").read_text(encoding="utf-8"), veld


def test_indeling_md_loopt_gelijk():
    uit = subprocess.run([sys.executable, str(REPO / "tools" / "bouw_indeling.py"), "--check"],
                         capture_output=True, text=True)
    assert uit.returncode == 0, uit.stdout + uit.stderr


def test_bio2_kopie_loopt_gelijk_met_normen():
    """Draait alleen als de repo normen ernaast staat; CI checkt hem uit als _normen."""
    if not any((p / "bio2.json").is_file() for p in (REPO.parent / "normen", REPO / "_normen")):
        return
    uit = subprocess.run([sys.executable, str(REPO / "tools" / "haal_normen.py"), "--check"],
                         capture_output=True, text=True)
    assert uit.returncode == 0, uit.stdout + uit.stderr
