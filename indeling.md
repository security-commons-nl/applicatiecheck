# Indeling: welk bewijs per maatregel

Van de 148 overheidsmaatregelen in BIO2 kan een gekochte applicatie er 28 geheel of gedeeltelijk zelf aantonen uit configuratie (A) of log (B). Voor 20 ligt het bewijs in een document of schermafbeelding (C), en 100 liggen buiten de applicatie (D). Peildatum 2026-09-02; status van elke rij: *voorlopig*.

> Per overheidsmaatregel: uit welk soort bewijs een applicatie hem kan aantonen (A, B, C) of dat het bewijs buiten de applicatie ligt (D). Kader: CIP BIO Thema-uitwerking Softwarepakketten (gekochte applicatie); ASVS-verwijzingen via OpenCRE als aanwijzing wat het bewijs moet bevatten. Status voorlopig: ingedeeld op titel, thema en BIO2-tekst, nog niet per maatregel bevestigd door een vakgenoot met een zaaksysteem ernaast.

Bron van de maatregelen: `bronnen/bio2.json`, BIO2 v1.3 definitief - 9 januari 2026 (cisochat, commit `0d2de8b9`). De teksten van de maatregelen staan daar; hier staan nummer, titel en de indeling.

| Soort | Betekenis | Aantal (eerste soort) |
|---|---|---|
| **A** | Configuratie-export: wat is ingesteld. Regel per veld, parser per applicatie. | 24 |
| **B** | Logsample: wat er gebeurt. Structuurtoets op de laatste 24 uur of 1000 regels; geen gedragsmeting. | 4 |
| **C** | Document of schermafbeelding: wat A en B niet raken. AI-extractie, altijd met menselijke bevestiging. | 20 |
| **D** | Niet uit de applicatie: proces en organisatie. Het instrument zegt dit hardop. | 100 |

## A. Configuratie-export (24)

| Nr | Titel | Soort | Bron | Wat het bewijs moet bevatten | ASVS | Motivering |
|---|---|---|---|---|---|---|
| 5.15.01 | Toegangsbeveiliging | A | eigen | Instellingen voor toegestane herkomst: SSO-eis via de centrale identity provider, IP- of zonebeperking, apparaatvereiste. | V4 | De vertrouwde zone zelf is infrastructuur; wat de applicatie eist van wie binnenkomt staat in de configuratie. |
| 5.16.01 | Identiteitsbeheer | A + B | eigen | Accountlijst: unieke, persoonsgebonden accounts, koppeling aan de centrale identity provider, geen gedeelde accounts; in de log: aanmaken en verwijderen van accounts. | V2.1 | De tekst in de bron (AdES, registratie internetfacing) wijkt af van de titel; ingedeeld op de ISO-maatregel identiteitsbeheer. |
| 5.16.02 | Identiteitsbeheer | A + B | eigen | Als 5.16.01; daarnaast de registratie van de applicatie als internetfacing voorziening (D, buiten de applicatie). | V2.1 | Zie 5.16.01. |
| 5.17.01 | Authenticatie-informatie | A + B | eigen | MFA-instelling (afgedwongen voor alle accounts, of per rol), wachtwoordbeleid, lockout; in de log: inlogs zonder tweede factor. | V2.2, V2.8 | De instelling bewijst de opzet, de log bewijst of hij ook werkt. |
| 5.17.02 | Authenticatie-informatie | A + B | eigen | Als 5.17.01, met de twee MFA-vormen die BIO2 noemt. | V2.2, V2.8 | Zie 5.17.01. |
| 5.17.03 | Authenticatie-informatie | A + B | eigen | Als 5.17.01; specifiek voor beheeraccounts en via internet bereikbare toegang. | V2.2, V2.8 | Zie 5.17.01. |
| 5.18.01 | Toegangsrechten | A + B | eigen | Rollen- en autorisatiematrix (wie mag wat), lijst van accounts met rol; in de log: toekennen en intrekken van rechten, laatste inlog per account (inactieve accounts met rechten). | V4.1 | De tekst in de bron herhaalt de MFA-tekst van 5.17; ingedeeld op de ISO-maatregel toegangsrechten. |
| 5.18.02 | Toegangsrechten | A + B | eigen | Als 5.18.01; de periodieke beoordeling zelf is proces (D). | V4.1 | Zie 5.18.01. |
| 5.33.01 | Beschermen van registraties | A + C | eigen | Bewaartermijnen en vernietigingsregels zoals ingesteld in de applicatie (koppeling aan de selectielijst), en of ze actief zijn. |  | Voor een zaaksysteem de kern van de Archiefwet; de instelling is aantoonbaar, de toets op werking is proces. |
| 8.02.01 | Speciale toegangsrechten | A + B | eigen | Lijst van accounts met beheerrol of speciale bevoegdheid; in de log: gebruik van die bevoegdheden. De kwartaalbeoordeling zelf is proces (D). | V4.3 | Opzet en bestaan komen uit de applicatie; de beoordeling niet. |
| 8.03.01 | Beperking toegang tot informatie | A | eigen | Autorisatiemodel voor informatie met specifiek belang: afgeschermde zaaktypen of vertrouwelijkheidsniveaus en welke rollen daarbij mogen. | V4.1 | Isolatie van gevoelige informatie is in een zaaksysteem een instelling. |
| 8.03.02 | Beperking toegang tot informatie | A + B | eigen | Rollenmatrix op need-to-know; in de log: toegang tot afgeschermde zaken door rollen die dat niet nodig hebben. | V4.1, V4.2 | De matrix bewijst de opzet; de log laat zien of de afscherming standhoudt. |
| 8.05.01 | Beveiligde authenticatie | A + B | eigen | Inloginstellingen: MFA, sessieduur en inactiviteitsvergrendeling, lockout na mislukte pogingen, neutrale foutmeldingen; leveranciersaccounts met einddatum en rechten; in de log: inlogpogingen en leveranciersgebruik. | V2, V3 | De BIO2-tekst gaat over leverancierstoegang; de ISO-maatregel over beveiligde authenticatie in het algemeen. Beide zijn instelling plus log. |
| 8.07.01 | Bescherming tegen malware | A + C | eigen | Instelling dat uploads en downloads door de malwarescan gaan; bij een SaaS-dienst de verklaring van de leverancier. | V12.4 | Een zaaksysteem ontvangt bestanden van buiten; of die gescand worden is een instelling of een dienstbelofte. |
| 8.08.01 | Beheer van technische kwetsbaarheden | A + C | leverancier | Versienummer in de applicatie tegen de laatste release van de leverancier; releasenotes en patch-SLA van de leverancier. | V14.2 | Of de applicatie bij is, is deterministisch te zien zodra de releaselijst bekend is. |
| 8.09.01 | Configuratiebeheer | A | eigen | De configuratie-export zelf, als vastgelegde baseline; een tweede export laat afwijkingen zien. | V14.1 | Configuratiebeheer is precies wat een export bewijst: dit is de stand, en dit is er sindsdien veranderd. |
| 8.10.01 | Wissen van informatie | A + B | eigen | Vernietigings- en retentie-instellingen; in de log: uitgevoerde vernietigingsacties met resultaat. |  | Wissen van informatie is in een zaaksysteem een geconfigureerde en gelogde handeling. |
| 8.15.03 | Logging | A | eigen | Instelling welke logtypen aan staan (bijvoorbeeld audittypen per module); het organisatiebrede overzicht is D. | V7.1 | Per applicatie is het overzicht een instelling. |
| 8.15.04 | Logging | A | eigen | Retentie-instelling per logtype; de risicoafweging erachter is D. | V7.1 | De termijn staat in de configuratie; of hij risicogericht is, beslist een mens. |
| 8.15.05 | Logging | A | eigen | Instelling dat de log naar een aparte of onveranderbare opslag gaat en wie de audittabel mag wijzigen; de melding als incident is D. | V7.3 | Bescherming van de log is een instelling; de opvolging niet. |
| 8.18.01 | Gebruik van speciale systeemhulpmiddelen | A + B | eigen | Wie toegang heeft tot de beheeromgeving (rollen); in de log: gebruik van beheerfuncties. | V4.3 | Systeemhulpmiddelen van een applicatie zijn de beheerconsole en de importfuncties. |
| 8.21.04 | Beveiliging van netwerkdiensten | A | eigen | Transportversleuteling: alleen HTTPS, TLS-versies en cipher-instellingen, HSTS; extern toetsbaar met een TLS-scan. | V9.1 | Voor een webapplicatie is versleuteld transport een instelling die je ook van buiten kunt meten. |
| 8.24.01 | Gebruik van cryptografie | A + C | eigen | Encryptie-instellingen (opslag, transport, algoritmen, sleutelbeheer bij de leverancier); het cryptografiebeleid is D. | V6 | Het beleid is organisatie; wat de applicatie toepast is configuratie of een leveranciersverklaring. |
| 8.31.01 | Scheiding van ontwikkel-, test- en productieomgevingen | A + C | eigen | Aanwezigheid en instellingen van een gescheiden testomgeving (productievlag, koppelingen); afwijkingen met goedkeuring zijn D. |  | De scheiding is aantoonbaar als omgeving; de discipline is proces. |

## B. Logsample (4)

| Nr | Titel | Soort | Bron | Wat het bewijs moet bevatten | ASVS | Motivering |
|---|---|---|---|---|---|---|
| 8.15.01 | Logging | B | eigen | Logsample waarin elke regel actie, object, resultaat, oorsprong, identiteit en tijdstip bevat. | V7.1 | De hardste B: de velden staan in de BIO2-tekst en zijn deterministisch te toetsen op een sample. |
| 8.15.02 | Logging | B | eigen | Logsample zonder wachtwoorden, tokens, sessiesleutels of burgerservicenummers; dezelfde scan als de anonimizer. | V7.1 | Wat er niet in mag staan is deterministisch te vinden. |
| 8.17.01 | Kloksynchronisatie | B | eigen | Logsample met tijdstempels in een eenduidig formaat met tijdzone, in monotone volgorde, zonder onverklaarbare sprongen ten opzichte van de exporttijd. | V7.1 | Kloksynchronisatie is alleen uit gedrag aantoonbaar; de NTP-instelling is infrastructuur. |
| 8.18.02 | Gebruik van speciale systeemhulpmiddelen | B + A | eigen | Beheeracties in de log; retentie-instelling van dat logtype op minimaal een half jaar. | V7.1 | BIO2 noemt de termijn; die is een instelling, het loggen zelf is gedrag. |

## C. Document of schermafbeelding (20)

| Nr | Titel | Soort | Bron | Wat het bewijs moet bevatten | ASVS | Motivering |
|---|---|---|---|---|---|---|
| 5.13.01 | Labelen van informatie | C | eigen | Schermafbeelding van de labelinstelling (vertrouwelijkheidsaanduiding per zaak of document) als de applicatie die kent. |  | Labelen is een organisatiemaatregel; alleen de ondersteuning in de applicatie is aantoonbaar. |
| 5.20.03 | Adresseren van informatiebeveiliging in leveranciersovereenkomsten | C | leverancier | Assurance-rapport of certificaat van een onafhankelijke derde met een scope die de dienst dekt (ISAE 3402, ISO 27001-certificaat met verklaring van toepasselijkheid, pentestrapport). |  | De leverancier toont aan; het instrument registreert het bewijs met peildatum en scope. |
| 8.07.04 | Bescherming tegen malware | C | leverancier | Verklaring of rapport van de leverancier dat ontvangen bestanden gescand worden voor opslag. |  | Bij een gehoste applicatie ligt de scan bij de leverancier. |
| 8.08.02 | Beheer van technische kwetsbaarheden | C | leverancier | Patchbeleid en risicoafweging van de leverancier; eigen risicoafweging bij uitstel (D). |  | De afweging zelf is proces; het beleid van de leverancier is een document. |
| 8.08.03 | Beheer van technische kwetsbaarheden | C | leverancier | Als 8.08.02: welke mitigerende maatregelen de leverancier neemt als een patch niet binnen een week kan. |  | Zie 8.08.02. |
| 8.08.04 | Beheer van technische kwetsbaarheden | C | leverancier | Recent pentest- of kwetsbaarheidsrapport over de applicatie, met scope en datum. |  | Een rapport is document-bewijs; het instrument registreert datum en scope, niet de inhoud. |
| 8.08.05 | Beheer van technische kwetsbaarheden | C | leverancier | Pentestrapport per release of major update van een internetfacing applicatie. |  | Zie 8.08.04. |
| 8.08.06 | Beheer van technische kwetsbaarheden | C | leverancier | Gepubliceerde CVD-procedure van de leverancier; de eigen CVD-procedure is D. |  | Bij een gekocht pakket komt een kwetsbaarheidsmelding bij de leverancier binnen. |
| 8.11.01 | Maskeren van gegevens | C | eigen | Schermafbeelding van maskering of pseudonimisering waar de applicatie die toepast (bijvoorbeeld BSN in overzichten, testomgeving). | V8.3 | Niet elk pakket kent maskering; waar het bestaat is het een instelling, anders niet aantoonbaar. |
| 8.13.03 | Back-up van informatie | C | leverancier | Beschrijving van de back-uplocatie en scheiding van de productielocatie; bij eigen hosting de back-upconfiguratie (A). |  | Back-up van een gehoste applicatie is een dienstbelofte van de leverancier. |
| 8.13.04 | Back-up van informatie | C | eigen | Verslag van de laatste hersteltest, met datum en uitkomst. |  | De test is proces; het verslag is document-bewijs met peildatum. |
| 8.14.01 | Redundantie van informatieverwerkende faciliteiten | C | leverancier | Architectuur- of SLA-beschrijving van redundantie bij de leverancier. |  | Redundantie zit in de hostinglaag, niet in de applicatieconfiguratie. |
| 8.16.03 | Monitoren van activiteiten | C | eigen | Schermafbeelding of exportregel die laat zien dat de applicatielog naar de SIEM gaat; de monitoring zelf is landschap (security-posture-tool). |  | Applicatiecheck ziet alleen of de aansluiting er is. |
| 8.25.01 | Beveiligen tijdens de ontwikkelcyclus | C | leverancier | Verklaring of certificering van de leverancier over de beveiligde ontwikkelcyclus (SSDLC). |  | Bij een gekocht pakket ligt de ontwikkelcyclus bij de leverancier. |
| 8.27.01 | Veilige systeemarchitectuur en technische uitgangspunten | C | leverancier | Architectuurbeschrijving of verklaring over security by design en by default. |  | Zie 8.25.01. |
| 8.28.01 | Veilig coderen | C | leverancier | Verklaring over veilig coderen (richtlijnen, code review, statische analyse). |  | Zie 8.25.01. |
| 8.29.01 | Testen van de beveiliging tijdens ontwikkeling en acceptatie | C | eigen | Testverslag van de laatste acceptatietest, met datum en resultaten. |  | Het verslag is document-bewijs; de methodiek is proces. |
| 8.30.01 | Uitbestede systeemontwikkeling | C | leverancier | Contractuele bepaling of verklaring dat de interne ontwikkelmaatregelen gelden voor uitbestede ontwikkeling. |  | Zie 8.25.01. |
| 8.31.02 | Scheiding van ontwikkel-, test- en productieomgevingen | C | eigen | Testverslag bij significante wijzigingen; zie 8.29.01. |  | Zie 8.31.01. |
| 8.33.01 | Testgegevens | C | eigen | Schermafbeelding of instelling die laat zien dat testgegevens geanonimiseerd of synthetisch zijn. |  | Waar de applicatie anonimisering voor test ondersteunt is het een instelling; anders niet aantoonbaar. |

## D. Niet uit de applicatie (100)

| Nr | Titel | Thema | Waarom niet uit de applicatie |
|---|---|---|---|
| 5.01.01 | Informatiebeveiligingsbeleid | IV-beleid | Organisatorische maatregel (IV-beleid); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.01.02 | Beleidsregels voor informatie beveiliging | IV-beleid | Organisatorische maatregel (IV-beleid); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.02.01 | Rollen en verantwoordelijkheden bij informatiebeveiliging | IV-beleid | Organisatorische maatregel (IV-beleid); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.02.02 | Rollen en verantwoordelijkheden bij informatiebeveiliging | IV-beleid | Organisatorische maatregel (IV-beleid); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.03.01 | Functiescheiding | IV-beleid | Organisatorische maatregel (IV-beleid); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. BIO2 kent hier geen overheidsmaatregel; de ISO-maatregel geldt. |
| 5.04.01 | Managementverantwoordelijkheden | Screening, bewustzijn & opleiding | Organisatorische maatregel (Screening, bewustzijn & opleiding); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.04.02 | Managementverantwoordelijkheden | Screening, bewustzijn & opleiding | Organisatorische maatregel (Screening, bewustzijn & opleiding); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.04.03 | Managementverantwoordelijkheden | Screening, bewustzijn & opleiding | Organisatorische maatregel (Screening, bewustzijn & opleiding); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.05.01 | Contact met overheidsinstanties | IV-beleid | Organisatorische maatregel (IV-beleid); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.06.01 | Contact met speciale belangengroepen | IV-beleid | Organisatorische maatregel (IV-beleid); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. BIO2 kent hier geen overheidsmaatregel; de ISO-maatregel geldt. |
| 5.07.01 | Informatie en analyses over dreigingen | IV-beleid | Organisatorische maatregel (IV-beleid); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. BIO2 kent hier geen overheidsmaatregel; de ISO-maatregel geldt. |
| 5.08.01 | Informatiebeveiliging in projectmanagement | Informatiebeveiliging binnen projecten | Organisatorische maatregel (Informatiebeveiliging binnen projecten); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.09.01 | Inventarisatie van informatie en andere gerelateerde bedrijfsmiddelen | Bedrijfsmiddelenbeheer | Organisatorische maatregel (Bedrijfsmiddelenbeheer); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.10.01 | Aanvaardbaar gebruik van informatie en andere gerelateerde bedrijfsmiddelen | Bedrijfsmiddelenbeheer | Organisatorische maatregel (Bedrijfsmiddelenbeheer); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. BIO2 kent hier geen overheidsmaatregel; de ISO-maatregel geldt. |
| 5.11.01 | Retourneren van bedrijfsmiddelen | Bedrijfsmiddelenbeheer | Organisatorische maatregel (Bedrijfsmiddelenbeheer); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. BIO2 kent hier geen overheidsmaatregel; de ISO-maatregel geldt. |
| 5.12.01 | Classificeren van informatie | Informatie classificatie | Organisatorische maatregel (Informatie classificatie); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.14.01 | Overdragen van informatie | Informatie classificatie | Organisatorische maatregel (Informatie classificatie); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.14.02 | Overdragen van informatie | Informatie classificatie | Organisatorische maatregel (Informatie classificatie); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.14.03 | Overdragen van informatie | Informatie classificatie | Organisatorische maatregel (Informatie classificatie); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.14.04 | Overdragen van informatie | Informatie classificatie | Organisatorische maatregel (Informatie classificatie); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.14.05 | Overdragen van informatie | Informatie classificatie | Organisatorische maatregel (Informatie classificatie); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.19.01 | Informatiebeveiliging in leveranciersrelaties | Leveranciersbeheer - Inkoop | Organisatorische maatregel (Leveranciersbeheer - Inkoop); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.20.01 | Adresseren van informatiebeveiliging in leveranciersovereenkomsten | Leveranciersbeheer - Inkoop | Organisatorische maatregel (Leveranciersbeheer - Inkoop); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.20.02 | Adresseren van informatiebeveiliging in leveranciersovereenkomsten | Leveranciersbeheer - Inkoop | Organisatorische maatregel (Leveranciersbeheer - Inkoop); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.21.02 | Beheren van informatiebeveiliging in de ICT-toeleveringsketen | Leveranciersbeheer - Inkoop | Organisatorische maatregel (Leveranciersbeheer - Inkoop); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.21.03 | Beheren van informatiebeveiliging in de ICT-toeleveringsketen | Leveranciersbeheer - contractbeheer | Organisatorische maatregel (Leveranciersbeheer - contractbeheer); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.21.04 | Beheren van informatiebeveiliging in de ICT-toeleveringsketen | Leveranciersbeheer - contractbeheer | Organisatorische maatregel (Leveranciersbeheer - contractbeheer); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.22.01 | Monitoren, beoordelen en het beheren van wijzigingen van leveranciersdiensten | Leveranciersbeheer - contractbeheer | Organisatorische maatregel (Leveranciersbeheer - contractbeheer); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.22.02 | Monitoren, beoordelen en het beheren van wijzigingen van leveranciersdiensten | Leveranciersbeheer - contractbeheer | Organisatorische maatregel (Leveranciersbeheer - contractbeheer); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.23.01 | Informatiebeveiliging voor het gebruik van clouddiensten | Leveranciersbeheer - contractbeheer | Organisatorische maatregel (Leveranciersbeheer - contractbeheer); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.24.01 | Plannen en voorbereiden van het beheer van informatie-beveiligingsincidenten | Security Incident Management | Organisatorische maatregel (Security Incident Management); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.24.02 | Plannen en voorbereiden van het beheer van informatie-beveiligingsincidenten | Security Incident Management | Organisatorische maatregel (Security Incident Management); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.24.03 | Plannen en voorbereiden van het beheer van informatie-beveiligingsincidenten | Security Incident Management | Organisatorische maatregel (Security Incident Management); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.24.04 | Plannen en voorbereiden van het beheer van informatie-beveiligingsincidenten | Security Incident Management | Organisatorische maatregel (Security Incident Management); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.24.05 | Plannen en voorbereiden van het beheer van informatie-beveiligingsincidenten | Security Incident Management | Organisatorische maatregel (Security Incident Management); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.24.06 | Plannen en voorbereiden van het beheer van informatie-beveiligingsincidenten | Security Incident Management | Organisatorische maatregel (Security Incident Management); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.24.07 | Plannen en voorbereiden van het beheer van informatie-beveiligingsincidenten | Security Incident Management | Organisatorische maatregel (Security Incident Management); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.25.01 | Beoordelen van en besluiten over informatiebeveiligingsgebeurtenissen | Security Incident Management | Organisatorische maatregel (Security Incident Management); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.26.01 | Reageren op informatiebeveiligings-incidenten | Security Incident Management | Organisatorische maatregel (Security Incident Management); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. BIO2 kent hier geen overheidsmaatregel; de ISO-maatregel geldt. |
| 5.27.01 | Leren van informatiebeveiligingsincidenten | Security Incident Management | Organisatorische maatregel (Security Incident Management); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.27.02 | Verzamelen van bewijsmateriaal | Security Incident Management | Organisatorische maatregel (Security Incident Management); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.28.01 | Verzamelen van bewijsmateriaal | Security Incident Management | Organisatorische maatregel (Security Incident Management); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.29.01 | Informatiebeveiliging tijdens een verstoring | Business Continuity & Disaster Recovery | Organisatorische maatregel (Business Continuity & Disaster Recovery); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. BIO2 kent hier geen overheidsmaatregel; de ISO-maatregel geldt. |
| 5.30.01 | ICT-gereedheid voor bedrijfscontinuïteit | Business Continuity & Disaster Recovery | Organisatorische maatregel (Business Continuity & Disaster Recovery); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.30.02 | ICT-gereedheid voor bedrijfscontinuïteit | Business Continuity & Disaster Recovery | Organisatorische maatregel (Business Continuity & Disaster Recovery); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.31.01 | Wettelijke, statutaire, regelgevende en contractuele eisen | IT-Compliance | Organisatorische maatregel (IT-Compliance); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. BIO2 kent hier geen overheidsmaatregel; de ISO-maatregel geldt. |
| 5.32.01 | Intellectuele-eigendomsrechten | IT-Compliance | Organisatorische maatregel (IT-Compliance); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. BIO2 kent hier geen overheidsmaatregel; de ISO-maatregel geldt. |
| 5.34.01 | Privacy en bescherming van persoonsgegevens | IT-Compliance | Organisatorische maatregel (IT-Compliance); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. BIO2 kent hier geen overheidsmaatregel; de ISO-maatregel geldt. |
| 5.35.02 | Onafhankelijke beoordeling van informatiebeveiliging | IV-beleid | Organisatorische maatregel (IV-beleid); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 5.36.01 | Naleving van beleid, regels en normen voor informatiebeveiliging | IV-beleid | Organisatorische maatregel (IV-beleid); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |
| 6.02.01 | Arbeidsovereenkomst | Screening, bewustzijn & opleiding | Personele maatregel (Screening, bewustzijn & opleiding); niet uit de applicatie aantoonbaar. |
| 6.03.01 | Bewustwording van, opleiding en training in informatiebeveiliging | Screening, bewustzijn & opleiding | Personele maatregel (Screening, bewustzijn & opleiding); niet uit de applicatie aantoonbaar. |
| 6.03.02 | Bewustwording van, opleiding en training in informatiebeveiliging | Screening, bewustzijn & opleiding | Personele maatregel (Screening, bewustzijn & opleiding); niet uit de applicatie aantoonbaar. |
| 6.03.03 | Bewustwording van, opleiding en training in informatiebeveiliging | Screening, bewustzijn & opleiding | Personele maatregel (Screening, bewustzijn & opleiding); niet uit de applicatie aantoonbaar. |
| 6.04.01 | Disciplinaire procedure | Screening, bewustzijn & opleiding | Personele maatregel (Screening, bewustzijn & opleiding); niet uit de applicatie aantoonbaar. BIO2 kent hier geen overheidsmaatregel; de ISO-maatregel geldt. |
| 6.05.01 | Verantwoordelijkheden na beëindiging of wijziging van het dienstverband | Screening, bewustzijn & opleiding | Personele maatregel (Screening, bewustzijn & opleiding); niet uit de applicatie aantoonbaar. BIO2 kent hier geen overheidsmaatregel; de ISO-maatregel geldt. |
| 6.06.01 | Vertrouwelijkheids- of geheimhoudingsovereenkomsten | Screening, bewustzijn & opleiding | Personele maatregel (Screening, bewustzijn & opleiding); niet uit de applicatie aantoonbaar. BIO2 kent hier geen overheidsmaatregel; de ISO-maatregel geldt. |
| 6.07.01 | Werken op afstand | Logische toegangsbeveiliging | Personele maatregel (Logische toegangsbeveiliging); niet uit de applicatie aantoonbaar. BIO2 kent hier geen overheidsmaatregel; de ISO-maatregel geldt. |
| 6.08.01 | Melden van informatiebeveiligings-gebeurtenissen | Security Incident Management | Personele maatregel (Security Incident Management); niet uit de applicatie aantoonbaar. |
| 7.01.01 | Fysieke beveiligingszones | Fysieke toegang & beveiliging | Fysieke maatregel (Fysieke toegang & beveiliging); niet uit de applicatie aantoonbaar. |
| 7.01.02 | Fysieke beveiligingszones | Fysieke toegang & beveiliging | Fysieke maatregel (Fysieke toegang & beveiliging); niet uit de applicatie aantoonbaar. |
| 7.02.01 | Fysieke toegangsbeveiliging | Fysieke toegang & beveiliging | Fysieke maatregel (Fysieke toegang & beveiliging); niet uit de applicatie aantoonbaar. |
| 7.05.01 | Beschermen tegen fysieke en omgevingsdreigingen | Fysieke toegang & beveiliging | Fysieke maatregel (Fysieke toegang & beveiliging); niet uit de applicatie aantoonbaar. BIO2 kent hier geen overheidsmaatregel; de ISO-maatregel geldt. |
| 7.06.01 | Werken in beveiligde zones | Bedrijfsmiddelenbeheer | Fysieke maatregel (Bedrijfsmiddelenbeheer); niet uit de applicatie aantoonbaar. BIO2 kent hier geen overheidsmaatregel; de ISO-maatregel geldt. |
| 7.07.01 | ‘Clear desk’ en ‘clear screen’ | IT-Compliance | Fysieke maatregel (IT-Compliance); niet uit de applicatie aantoonbaar. |
| 7.08.01 | Plaatsen en beschermen van apparatuur | Bedrijfsmiddelenbeheer | Fysieke maatregel (Bedrijfsmiddelenbeheer); niet uit de applicatie aantoonbaar. BIO2 kent hier geen overheidsmaatregel; de ISO-maatregel geldt. |
| 7.09.01 | Beveiligen van bedrijfsmiddelen buiten het terrein | Bedrijfsmiddelenbeheer | Fysieke maatregel (Bedrijfsmiddelenbeheer); niet uit de applicatie aantoonbaar. BIO2 kent hier geen overheidsmaatregel; de ISO-maatregel geldt. |
| 7.10.01 | Opslagmedia | Afvoer en hergebruik gegevensdragers | Fysieke maatregel (Afvoer en hergebruik gegevensdragers); niet uit de applicatie aantoonbaar. |
| 7.10.02 | Opslagmedia | Afvoer en hergebruik gegevensdragers | Fysieke maatregel (Afvoer en hergebruik gegevensdragers); niet uit de applicatie aantoonbaar. |
| 7.10.03 | Opslagmedia | Afvoer en hergebruik gegevensdragers | Fysieke maatregel (Afvoer en hergebruik gegevensdragers); niet uit de applicatie aantoonbaar. |
| 7.11.01 | Nutsvoorzieningen | Bedrijfsmiddelenbeheer | Fysieke maatregel (Bedrijfsmiddelenbeheer); niet uit de applicatie aantoonbaar. BIO2 kent hier geen overheidsmaatregel; de ISO-maatregel geldt. |
| 7.12.01 | Beveiligen van bekabeling | Fysieke toegang & beveiliging | Fysieke maatregel (Fysieke toegang & beveiliging); niet uit de applicatie aantoonbaar. BIO2 kent hier geen overheidsmaatregel; de ISO-maatregel geldt. |
| 7.13.01 | Onderhoud van apparatuur | Bedrijfsmiddelenbeheer | Fysieke maatregel (Bedrijfsmiddelenbeheer); niet uit de applicatie aantoonbaar. BIO2 kent hier geen overheidsmaatregel; de ISO-maatregel geldt. |
| 7.14.01 | Veilig verwijderen of hergebruiken van apparatuur | Afvoer en hergebruik gegevensdragers | Fysieke maatregel (Afvoer en hergebruik gegevensdragers); niet uit de applicatie aantoonbaar. BIO2 kent hier geen overheidsmaatregel; de ISO-maatregel geldt. |
| 8.01.01 | User endpoint devices | Mobile Device Management | Technologische maatregel die bij een gekochte applicatie in de infrastructuur, de werkplek of het proces ligt (Mobile Device Management), niet in de applicatieconfiguratie. |
| 8.01.02 | User endpoint devices | Mobile Device Management | Technologische maatregel die bij een gekochte applicatie in de infrastructuur, de werkplek of het proces ligt (Mobile Device Management), niet in de applicatieconfiguratie. |
| 8.04.01 | Toegangsbeveiliging op broncode | Logische toegangsbeveiliging | Broncode is bij een gekocht pakket niet van de organisatie; bij zelfbouw is dit C (leverancier of eigen ontwikkelteam). |
| 8.06.01 | Capaciteitsbeheer | IT-Compliance | Technologische maatregel die bij een gekochte applicatie in de infrastructuur, de werkplek of het proces ligt (IT-Compliance), niet in de applicatieconfiguratie. BIO2 kent hier geen overheidsmaatregel; de ISO-maatregel geldt. |
| 8.07.02 | Bescherming tegen malware | Vulnerability & patchmanagement | Technologische maatregel die bij een gekochte applicatie in de infrastructuur, de werkplek of het proces ligt (Vulnerability & patchmanagement), niet in de applicatieconfiguratie. |
| 8.07.03 | Bescherming tegen malware | Vulnerability & patchmanagement | Technologische maatregel die bij een gekochte applicatie in de infrastructuur, de werkplek of het proces ligt (Vulnerability & patchmanagement), niet in de applicatieconfiguratie. |
| 8.12.01 | Voorkomen van gegevenslekken (data leakage prevention) | IT-Compliance | Technologische maatregel die bij een gekochte applicatie in de infrastructuur, de werkplek of het proces ligt (IT-Compliance), niet in de applicatieconfiguratie. BIO2 kent hier geen overheidsmaatregel; de ISO-maatregel geldt. |
| 8.13.01 | Back-up van informatie | Back-up & Recovery | Technologische maatregel die bij een gekochte applicatie in de infrastructuur, de werkplek of het proces ligt (Back-up & Recovery), niet in de applicatieconfiguratie. |
| 8.13.02 | Back-up van informatie | Back-up & Recovery | Technologische maatregel die bij een gekochte applicatie in de infrastructuur, de werkplek of het proces ligt (Back-up & Recovery), niet in de applicatieconfiguratie. |
| 8.15.06 | Logging | Logging & monitoring | Technologische maatregel die bij een gekochte applicatie in de infrastructuur, de werkplek of het proces ligt (Logging & monitoring), niet in de applicatieconfiguratie. |
| 8.16.01 | Monitoren van activiteiten | Logging & monitoring | Technologische maatregel die bij een gekochte applicatie in de infrastructuur, de werkplek of het proces ligt (Logging & monitoring), niet in de applicatieconfiguratie. |
| 8.16.02 | Monitoren van activiteiten | Logging & monitoring | Technologische maatregel die bij een gekochte applicatie in de infrastructuur, de werkplek of het proces ligt (Logging & monitoring), niet in de applicatieconfiguratie. |
| 8.16.04 | Monitoren van activiteiten | Logging & monitoring | Technologische maatregel die bij een gekochte applicatie in de infrastructuur, de werkplek of het proces ligt (Logging & monitoring), niet in de applicatieconfiguratie. |
| 8.19.01 | Installeren van software op operationele systemen | Wijzigingsbeheer | Technologische maatregel die bij een gekochte applicatie in de infrastructuur, de werkplek of het proces ligt (Wijzigingsbeheer), niet in de applicatieconfiguratie. |
| 8.20.01 | Beveiliging netwerkcomponenten | Netwerkbeveiliging | Technologische maatregel die bij een gekochte applicatie in de infrastructuur, de werkplek of het proces ligt (Netwerkbeveiliging), niet in de applicatieconfiguratie. |
| 8.20.02 | Beveiliging netwerkcomponenten | Netwerkbeveiliging | Technologische maatregel die bij een gekochte applicatie in de infrastructuur, de werkplek of het proces ligt (Netwerkbeveiliging), niet in de applicatieconfiguratie. |
| 8.21.01 | Beveiliging van netwerkdiensten | Netwerkbeveiliging | Technologische maatregel die bij een gekochte applicatie in de infrastructuur, de werkplek of het proces ligt (Netwerkbeveiliging), niet in de applicatieconfiguratie. |
| 8.21.02 | Beveiliging van netwerkdiensten | Netwerkbeveiliging | Technologische maatregel die bij een gekochte applicatie in de infrastructuur, de werkplek of het proces ligt (Netwerkbeveiliging), niet in de applicatieconfiguratie. |
| 8.21.03 | Beveiliging van netwerkdiensten | Netwerkbeveiliging | Technologische maatregel die bij een gekochte applicatie in de infrastructuur, de werkplek of het proces ligt (Netwerkbeveiliging), niet in de applicatieconfiguratie. |
| 8.22.01 | Netwerksegmentatie | Netwerkbeveiliging | Technologische maatregel die bij een gekochte applicatie in de infrastructuur, de werkplek of het proces ligt (Netwerkbeveiliging), niet in de applicatieconfiguratie. |
| 8.23.01 | Toepassen van webfilters | Netwerkbeveiliging | Technologische maatregel die bij een gekochte applicatie in de infrastructuur, de werkplek of het proces ligt (Netwerkbeveiliging), niet in de applicatieconfiguratie. BIO2 kent hier geen overheidsmaatregel; de ISO-maatregel geldt. |
| 8.26.01 | Toepassingsbeveiligingseisen | Secure Software Development | Technologische maatregel die bij een gekochte applicatie in de infrastructuur, de werkplek of het proces ligt (Secure Software Development), niet in de applicatieconfiguratie. BIO2 kent hier geen overheidsmaatregel; de ISO-maatregel geldt. |
| 8.32.01 | Wijzigingsbeheer | Wijzigingsbeheer | Technologische maatregel die bij een gekochte applicatie in de infrastructuur, de werkplek of het proces ligt (Wijzigingsbeheer), niet in de applicatieconfiguratie. |
| 8.32.02 | Wijzigingsbeheer | Wijzigingsbeheer | Technologische maatregel die bij een gekochte applicatie in de infrastructuur, de werkplek of het proces ligt (Wijzigingsbeheer), niet in de applicatieconfiguratie. |
| 8.34.01 | Bescherming van informatiesystemen tijdens audits | IT-Compliance | Technologische maatregel die bij een gekochte applicatie in de infrastructuur, de werkplek of het proces ligt (IT-Compliance), niet in de applicatieconfiguratie. BIO2 kent hier geen overheidsmaatregel; de ISO-maatregel geldt. |
| 5.24.08 | Coordinated Vulnerability Disclosure | Overig | Organisatorische maatregel (Overig); het bewijs ligt bij beleid, proces of contract, niet in de applicatie. |

## Meedenken

Elke rij is een voorstel. Klopt een indeling niet voor jouw zaaksysteem, of ontbreekt bewijs dat de applicatie wél kan leveren: open een issue met het nummer van de maatregel in de titel. De bron is `bewijs.json`; deze pagina wordt daaruit gegenereerd met `tools/bouw_indeling.py`.
