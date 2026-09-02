"""bewijs.json dekt elke overheidsmaatregel uit de BIO2-kopie precies één keer, met geldige waarden,
en de afgeleiden (indeling.md, bronnen/bio2.json) lopen gelijk met hun bron."""
import json
import pathlib
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
    titels = {m["id"]: m["titel"] for m in BIO2["maatregelen"]}
    for r in BEWIJS["maatregelen"]:
        assert r["titel"] == titels[r["id"]], f"{r['id']}: titel wijkt af van de bron"


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


def test_bewijs_verwijst_naar_dezelfde_bio2_versie():
    assert BEWIJS["bron_bio2"]["commit"] == BIO2["bron"]["commit"]
    assert BEWIJS["bron_bio2"]["versie"] == BIO2["bron"]["versie"]


def test_indeling_md_loopt_gelijk():
    uit = subprocess.run([sys.executable, str(REPO / "tools" / "bouw_indeling.py"), "--check"],
                         capture_output=True, text=True)
    assert uit.returncode == 0, uit.stdout + uit.stderr


def test_bio2_kopie_loopt_gelijk_met_cisochat_als_die_er_is():
    uit = subprocess.run([sys.executable, str(REPO / "tools" / "haal_bio2.py"), "--check"],
                         capture_output=True, text=True)
    assert uit.returncode == 0, uit.stdout + uit.stderr
