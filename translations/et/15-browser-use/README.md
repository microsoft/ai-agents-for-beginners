# Arvutikasutusagentide (CUA) loomine

Arvutikasutusagentid saavad veebisaiti kasutada samamoodi nagu inimene: avades brauseri, uurides lehte ja tehes järgmiseks parima toimingu selle põhjal, mida nad näevad. Selles õppetükis ehitate brauseri automaatika agendi, mis otsib Airbnbst, ekstraktib struktureeritud kuulutuste andmed ja tuvastab Stockholmis odavaima majutuse.

Õppetükk ühendab Browser-Use'i AI-põhise navigeerimise jaoks, Playwrighti ja Chrome DevTools Protokolli (CDP) brauserijuhtimiseks, Azure OpenAI nägemisvõimelise mõtlemise jaoks ning Pydanticu struktureeritud andmete väljavõtmiseks.

## Sissejuhatus

Selles õppetükis käsitletakse:

- Millal on arvutikasutusagentid paremad võrreldes ainult API-põhise automatiseerimisega
- Kuidas ühendada Browser-Use Playwrighti ja CDP-ga usaldusväärse brauseri elutsükli haldamiseks
- Kuidas kasutada Azure OpenAI nägemist ja Pydanticu struktureeritud väljundit dünaamiliste veebilehtede kuulutuste andmete väljavõtmiseks
- Millal valida agent-esimene, näitleja-esimene või hübriidne brauseri automaatikatöövoog

## Õpieesmärgid

Õppetüki lõpetamisel oskad:

- Konfigureerida Browser-Use koos Azure OpenAI ja Playwrightiga
- Luua brauseri automaatikatöövoog, mis navigeerib reaalse veebisaidi ja käsitleb dünaamilisi kasutajaliidese elemente
- Ekstraktida tüübitud tulemusi nähtavast lehe sisust ja teisendada need edasiseks ärilogikaks
- Valida agentide ja näitlejate vahel sõltuvalt sellest, kui ennustatav brauseri ülesanne on

## Koodi näidis

Selle õppetüki juurde kuulub üks märkmikunäidis:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Käivitab Chrome'i seansi CDP kaudu, otsib Airbnb's Stockholmi kuulutusi, ekstraktib hindu Browser-Use'i nägemisega ja tagastab odavaima valiku struktureeritud andmetena.

## Eeltingimused

- Python 3.12+
- Azure OpenAI juurutus, mis on seadistatud teie keskkonnas
- Chrome või Chromium paigaldatud kohalikult
- Playwrighti sõltuvused paigaldatud
- Põhiteadmised asünkroonsest Pythonist

## Seadistamine

Paigalda märkmikus kasutatavad paketid:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Määra Azure OpenAI keskkonnamuutujad, mida märkmik kasutab:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Valikuline: vaikimisi kasutatakse, kui see on välja jäetud, uusimat API versiooni
AZURE_OPENAI_API_VERSION=...
```

## Arhitektuuri ülevaade

Märkmik demonstreerib hübriidset brauseri automaatikatöövoogu:

1. Chrome käivitatakse CDP-ga lubatult, nii et nii Playwright kui Browser-Use saavad jagada sama brauseriseanssi.
2. Browser-Use agent käsitleb avatud navigeerimise ülesandeid, nagu Airbnb avamine, hüpikakende sulgemine ja Stockholm otsimine.
3. Aktiivset lehte uuritakse struktureeritud Pydanticu skeemiga, et ekstraktida kuulutuste pealkirjad, ööhind, hinnangud ja URL-ide aadressid.
4. Python'i loogika võrdleb ekstraheeritud kuulutusi ja tõstab esile odavaima tulemuse.

See lähenemine hoiab paindlikku, nägemisel põhinevat mõtlemist, milles Browser-Use on hea, andes samal ajal deterministliku brauserijuhtimise, kui seda on vaja.

## Põhisõnumid ja parimad tavad

### Millal kasutada agenti ja millal näitlejat

| Stsenaarium | Kasutaja Agent | Kasutaja Näitleja |
|-----------|---------------|------------------|
| Dünaamilised paigutused | Jah, AI suudab kohaneda lehe muutustega | Ei, habraste selektoritega võib tekkida vigu |
| Teada struktuur | Ei, agent on aeglasem kui otsene juhtimine | Jah, kiire ja täpne |
| Elementide leidmine | Jah, loomulik keel toimib hästi | Ei, vaja täpseid selektoreid |
| Ajajuhtimine | Ei, vähem ennustatav | Jah, täielik kontroll oote- ja kordusprotsesside üle |
| Kompleksne töövoog | Jah, suudab käsitleda ootamatuid kasutajaliidese seisundeid | Ei, vajab selget harundamist |

### Browser-Use parimad tavad

1. Alusta agentiga uurimiseks ja dünaamiliseks navigeerimiseks.
2. Lülitu otsesele lehe juhtimisele, kui tegevus muutub ennustatavaks.
3. Kasuta struktureeritud väljundimudeleid, et ekstraktitud andmed oleksid valideeritud ja tüübikindlad.
4. Lisa viivitusi strateegiliselt pärast toiminguid, mis põhjustavad nähtavaid kasutajaliidese muutusi.
5. Tee kohapealisi ekraanipilte, et ebaõnnestumiste tõrkeotsing oleks lihtsam.
6. Oota veebilehtede muutusi ja kujunda varuplaanid hüpikakende ja paigutuse nihkumiste jaoks.
7. Sega agentide ja näitlejate malle, et saada nii paindlikkust kui täpsust.

### Brauseri agentide ohutuspiirangud

Brauseri agentidel on tegemist otsevooga veebilehtedel, seega vajavad nad rangemaid piire kui stsenaarium, mis kutsub ainult tuntud API-d. Enne märkmikust reaalsesse töövoogu liikumist määra kontrollid selle üle, mida agent võib näha, klõpsata ja esitada.

1. **Määra sirvimiskeskkonna ulatus.** Käivita agent spetsiaalses brauseriprofiilis või liivakastis ja piira see ainult vajaminevatele domeenidele.
2. **Eralda vaatlus tegevusest.** Lase agendil esmalt otsida, lugeda ja ekstraktida andmeid; nõua selget heakskiidu enne, kui ta esitab vorme, saadab sõnumeid, broneerib reise, teeb oste, kustutab kirjeid või muudab konto sätteid.
3. **Hoia saladused väljaspool päringuid ja jälgi.** Ära pane paroolide, makseteabe, sessiooniküpsiste või töötlemata isikuandmeid mudeli konteksti. Lase kasutajal autentimiseks üle võtta ja sensitiivsed väljad logidest eemaldada.
4. **Lähtu lehe sisust kui usaldamata sisendist.** Veebileht võib sisaldada agenti suunavaid juhiseid, mis pole mõeldud kasutajale. Agent peaks ignoreerima lehekeeles olevaid käske eesmärgi muutmiseks, andmete avalikustamiseks, kaitsete keelamiseks või mitteseotud saitide külastamiseks.
5. **Kasuta deterministlikke kontrolle riskantsete sammude ümber.** Kontrolli koodi abil enne lõpliku sammu kinnitamist, kas praegune URL, lehe pealkiri, valitud element, hind, saaja ja toimingu kokkuvõte vastab ootustele.
6. **Sea eelarved ja peatustingimused.** Piira agenti tegevuste, korduste, sakkide ja kasutusaegade arvu. Peatu, kui lehe seisund on ebamäärane, selle asemel et edasi klõpsata.
7. **Salvesta kasulikud tõendid, mitte kõik.** Hoia toimingute kokkuvõtteid, ajatemplisid, URL-e, valitud elementide kirjeldusi ja ekraanipiltide viiteid, et vigade korral oleks võimalik läbivaatust teha ilma ebavajalikku tundlikku lehe sisu salvestamata.

Airbnb näites on turvaline vaikeseade otsida kuulutusi ja ekstraktida hindu. Sisselogimine, hostiga ühenduse võtmine või broneeringu tegemine peaks olema kasutaja poolt kinnitatud eraldi toiming.

### Reaalse maailma rakendused

- Reisibroneerimine ja hinnaseire
- E-kaubanduse hindade võrdlus ja saadavuse kontroll
- Struktureeritud andmete väljavõtt dünaamilistelt veebisaitidelt
- Nägemispõhine kasutajaliidese testimine ja kontroll
- Veebilehtede jälgimine ja hoiatused
- Nutikas vormide täitmine mitmeastmelistes töövoogudes

## Reaalse maailma näide: Microsoft Project Opal

Selles õppetükis ehitatav agent on väike, kohalik versioon **arvutikasutusagentist (CUA)** — programmist, mis juhib brauserit samamoodi nagu inimene. Microsoft toob sama idee ettevõtete jaoks läbi **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, mis on Microsoft 365 Copiloti funktsioon.

Projekti Opal abil kirjeldate ülesannet ja agent töötab teie nimel, kasutades **arvutikasutust turvalisel Windows 365 Cloud PC-l**, toimides teie organisatsiooni brauseripõhistes rakendustes, saitidel ja andmetel. See töötab **asünkroonselt taustal** ning saate tööd suunata või kontrolli igal ajal võtta. Näitena:

- Turvagruppide liikmeteenuste haldamine
- Audititõendite kogumine ja valideerimine vastavusülevaadete jaoks
- IT intsidentide triage (piletite staatuste uuendamine, omanike määramine, duplikaatide sulgemine)
- Exceli andmete kogumine finantsaruandeks

Opal on hea näide sellest, kuidas näeb välja **tootmisklassi, usaldusväärne** arvutikasutusagent — ning kinnitab varem õpitud kontseptsioone:

| Selle kursuse kontseptsioon | Kuidas Project Opal seda rakendab |
|--------------------------|-------------------------------|
| **Inimene-silmuses** (Õppetükk 06) | Opal peatub sisselogimisteavet, tundlikke andmeid või ebaselgeid juhiseid ootama ja ei sisesta paroole ega esita vorme ilma selge kinnituseta. Saad *Kontrolli võtta* ja *Kontrolli tagastada* töö käigus. |
| **Usaldusväärsed & turvalised agentid** (Õppetükid 06 & 18) | Jookseb isoleeritud Windows 365 Cloud PC-s, vaikimisi ainult brauseripõhine (muu arvutikasutus Intune'i kaudu blokeeritud), kasutab **sinu** identiteeti, nii et pääseb ligi vaid lubatud ressurssidele ja logib kõik toimingud auditeeritavuse tagamiseks. |
| **Planeerimine & metakognitsioon** (Õppetükid 07 & 09) | Opal koostab esmalt tööplaani ja järelevalvab iga sammu juures oma mõtlemist, peatudes kahtlaste tegevuste korral. |
| **Taaskasutatavad oskused / tööriistad** (Õppetükk 04) | **Oskused** võimaldavad kirjutada korduvate tööde juhiseid (.md failidest imporditud või Opalis loodud) ning neid vestluste vahel taaskasutada. |

> **Saadavus:** Project Opal on hetkel kasutajatele saadaval [Frontieri varajase juurdepääsu programmis](https://adoption.microsoft.com/copilot/frontier-program/) Microsoft 365 Copilot tellimusega ja teie administraator peab seadistuse lõpule viima. Kuna tegemist on katsefunktsiooniga, võivad võimekused aja jooksul muutuda.

## Täiendavad ressursid

- [Alustamine Project Opal'iga (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwrighti integratsioonimall](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use'i näitleja parameetrid ja sisu väljavõtt](https://docs.browser-use.com/customize/actor/all-parameters)
- [Kursuse seadistus](../00-course-setup/README.md)

## Eelmine õppetükk

[Microsoft Agent Frameworki uurimine](../14-microsoft-agent-framework/README.md)

## Järgmine õppetükk

[Skaleeritavate agentide juurutamine](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->