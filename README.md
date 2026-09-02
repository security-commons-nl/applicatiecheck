# Applicatiecheck

Toont uit de applicatie zelf aan wat de BIO2 van een kritische applicatie vraagt: de configuratie-export
en een logsample worden deterministisch getoetst, AI helpt alleen bij het lezen van bewijs, en een mens
beslist. Voor ISO's en CISO's bij publieke organisaties die een zaaksysteem, financieel pakket of ander
kritisch systeem periodiek willen toetsen zonder vinkjeslijst.

Status: concept. Ontwerp en bewijsmodel; nog geen werkende code. Deze pagina is het ontwerp.

## Voor wie

ISO's en CISO's die een kritische applicatie in eigen beheer of bij een leverancier hebben en willen weten
wat die applicatie zélf kan aantonen van de BIO2, en wat je er nooit uit gaat halen. Functioneel beheerders
die de export leveren. Later ook leveranciers, die met hetzelfde instrument hun bewijs kunnen aanleveren
bij inkoop.

## Snel starten

Er is nog niets te draaien. Lees het ontwerp hieronder. Herken je het, heb je een export of een
logfragment van een zaaksysteem dat je geanonimiseerd kunt delen, of weet je waarom dit niet gaat werken:
open een issue met het label `idee` of een
[discussion](https://github.com/security-commons-nl/.github/discussions).

## Bijdragen

Zie de [CONTRIBUTING](https://github.com/security-commons-nl/.github/blob/main/CONTRIBUTING.md) van de
organisatie: daar staat per project een formulier, ook zonder Git-ervaring.

## Licentie

EUPL-1.2, zie [LICENSE](LICENSE).

## Het idee

De BIO2 schrijft voor kritische applicaties een reeks maatregelen voor: wie erin mag, hoe je inlogt, wat er
gelogd wordt, hoe lang de log bewaard blijft, of de klok klopt, of gegevens versleuteld zijn. Of een
applicatie daaraan voldoet wordt nu getoetst met een vragenlijst aan de beheerder of de leverancier. Het
antwoord is dan een vinkje, en een vinkje is geen bewijs.

De applicatie zelf weet het beter. Een configuratie-export zegt wat er is ingesteld. Een logfragment zegt
wat er gebeurt. Wie die twee naast de maatregel legt, kan voor een deel van de maatregelen zonder
interpretatie zeggen: dit is aangetoond, dit is gedeeltelijk aangetoond, en dit is uit de applicatie niet
aantoonbaar. Dat laatste hardop zeggen is net zo veel waard als het eerste.

Applicatiecheck doet precies dat, in de browser, met de bron in JSON en de regels leesbaar voor iedereen
die ze wil bekritiseren. Zelfde snit als de [zelfcheck](https://security-commons-nl.github.io/aanvalspaden/)
en de [CSIR Assessment Tool](https://security-commons-nl.github.io/csir-assessment-tool/): één HTML-bestand,
geen server, geen account, en het bewijs verlaat je eigen apparaat niet.

## Wat het niet is

Het landschap is al bezet, en dit instrument past ertussen zonder iets te dubbelen.

| Vraag | Woont in | Applicatiecheck doet dat niet |
|---|---|---|
| Wat zegt mijn Entra, firewall en SIEM over mijn organisatie? | [aanvalspaden/meting](https://github.com/security-commons-nl/aanvalspaden) | De eenheid is hier één applicatie, niet het landschap. |
| Hoe beheer ik mijn ISMS, risico's en de bestuurlijke rapportage? | je eigen managementsysteem | Applicatiecheck levert bewijs als dossier; de commons houdt geen register bij. |
| Hoe maak ik een héle norm uitvoerbaar, met een regeltaal? | [policy-as-code](https://github.com/security-commons-nl/policy-as-code) | Dit is de eerste concrete uitwerking van dat idee, voor één kader en één eenheid. |
| Hoe richt ik logging, toegang of cryptografie goed in? | [kennisbank](https://security-commons-nl.github.io/kennisbank/) | Applicatiecheck stelt vast, de kennisbank legt uit hoe. |

## Vier soorten bewijs

Van de 148 maatregelen in de BIO2 is een minderheid uit een applicatie af te leiden. Het instrument legt
per maatregel vast welke soort bewijs geldt, en die indeling is het eerste product, ook zonder tool: zie
[indeling.md](indeling.md), gegenereerd uit `bewijs.json`.

| Bewijssoort | Wat het bewijst | Deterministisch | Waar AI mag helpen |
|---|---|---|---|
| **A. Configuratie-export** | wat is ingesteld: rollen, wachtwoord- en sessiebeleid, MFA, logvelden, encryptie | regel per veld, parser per applicatie | een onbekend exportformaat naar feiten vertalen |
| **B. Logsample** | wat er gebeurt: wie, wat, wanneer, uitkomst; tijdstempels; wat er níet in hoort | veldencheck, tijdstempel en tijdzone, PII-scan, tijdspanne | niets, hooguit de bevinding formuleren |
| **C. Document of schermafbeelding** | wat A en B niet raken | nee | extractie naar feiten, altijd met menselijke bevestiging |
| **D. Niet uit de applicatie** | proces en organisatie: beleid, eigenaarschap, beoordeling van logs, wijzigingsbeheer | n.v.t. | n.v.t.; het instrument zegt eerlijk "hier niet aantoonbaar" |

Waar A en B elkaar raken, geldt B als het hardste bewijs. Een instelling "audit logging: aan" bewijst
maatregel 8.15 (Logging) niet; een logfragment met de verplichte velden wel. Hetzelfde geldt voor 8.17
(Kloksynchronisatie) en deels voor 8.05 (Beveiligde authenticatie) en 5.18 (Toegangsrechten): daar zit
het bewijs in wat er gebeurd is, niet in wat er is ingesteld.

Een logsample is een **structuurtoets**, geen gedragsmeting. De laatste vierentwintig uur of de laatste
duizend regels zijn genoeg om te zien of de verplichte velden er staan, of de tijdstempel bruikbaar is en
of er geen wachtwoorden of burgerservicenummers in de log lekken. Of er ook naar de log wordt gekeken (8.16)
en of de retentie klopt over maanden, is werk voor de SIEM en voor de meting in `aanvalspaden`.

## Drie ontwerpregels

1. **AI extraheert en formuleert, oordeelt nooit.** Een taalmodel mag een schermafbeelding of een
   onbekend exportformaat omzetten naar gestructureerde feiten, en mag een bevinding leesbaar opschrijven.
   Het oordeel "aangetoond, gedeeltelijk, niet aantoonbaar" is een regel over die feiten, en die regel staat
   in de repo. Een auditor moet kunnen nalezen waar het vinkje vandaan komt.
2. **Bewijs levert bewijs vóór een maatregel, nooit "voldoet aan".** Dezelfde richting als de
   normverankering in `aanvalspaden`: het instrument zegt wat dit bewijs ondersteunt, niet dat de
   organisatie aan de BIO voldoet. Dat oordeel blijft bij de mens die het dossier tekent.
3. **Bewijs verlaat het apparaat niet.** Alles rekent in de browser. Wie AI wil inzetten, gebruikt een
   eigen sleutel of de bestaande proxy van de commons, en een logsample gaat eerst door dezelfde
   anonimisering als in [anonimizer-browser](https://security-commons-nl.github.io/anonimizer-browser/)
   voordat er iets naar een model gaat.

## Wat eruit komt

Een dossier per applicatie, per maatregel: het nummer en de titel uit BIO 2.0, de bewijssoort, het bewijs
met een hash en een peildatum, de uitkomst van de regel, een verantwoordelijke, en waar de uitkomst afwijkt
een onderbouwing (comply or explain). De tekst van de maatregel staat er niet bij: die is van het CIP
(CC BY-NC-SA) en wordt niet meegepubliceerd; het nummer verwijst naar de bron. Het dossier is te bewaren als bestand en uit te draaien, zoals bij de
CSIR Assessment Tool. Wat de applicatie niet kan aantonen staat er ook in, met de reden, zodat het dossier
compleet is en niet alleen flatteus.

## Hoe het gebouwd wordt

- **Eén bron voor de maatregelen:** de repo [`normen`](https://github.com/security-commons-nl/normen),
  gekopieerd met `tools/haal_normen.py` en met de vingerafdruk van de bron erin; `--check` blokkeert in CI
  als de kopie achterloopt. Alleen nummer, titel en thema; de tekst blijft bij het CIP.
- **Regels als data:** per maatregel een leesbare regel in JSON (welke velden, welke waarden, welke
  bewijssoort), met een referentie-implementatie in Python en dezelfde regel in de pagina. Een test bewaakt
  dat beide hetzelfde antwoord geven.
- **Parser per applicatie:** een exportformaat is per pakket anders. De eerste parser volgt de eerste
  toepassing (zie hieronder); een generiek CSV/JSON-formaat vangt de rest tot er meer parsers zijn.
- **Testmateriaal is synthetisch of geanonimiseerd.** Een echte export van een productiesysteem komt niet
  in deze repo, ook niet als fixture. Wie er een wil delen, haalt hem eerst door de anonimizer (statuut A9).

## Eerste toepassing

Een zaaksysteem. Rollen, autorisaties en de auditlog zijn daar rijk, de export komt meestal uit het
beheerdersportaal van de leverancier, en bijna elke gemeente heeft er een. Wat de eerste parser precies
leest, wordt vastgelegd in het bouwplan in de
[plannen van de organisatie](https://github.com/security-commons-nl/.github/tree/main/plannen).

## Meedenken

Drie vragen waar we het antwoord nog niet op hebben:

- Welke van de 148 maatregelen horen bij A, B, C of D? Een eerste, voorlopige indeling staat in
  [indeling.md](indeling.md) (bron: `bewijs.json`); wie er een zaaksysteem naast legt, ziet vast dingen die
  wij missen.
- Hoe ziet een configuratie-export van jouw zaaksysteem eruit, en mag een geanonimiseerde versie als
  fixture dienen?
- Regels in JSON, of een bestaande regeltaal? De eerste is leesbaar voor niet-ontwikkelaars, de tweede
  is uitwisselbaar. We beginnen met de eerste tot iemand aantoont dat het knelt.

Open een issue met het label `idee` of een
[discussion](https://github.com/security-commons-nl/.github/discussions). Open source onder EUPL-1.2.
