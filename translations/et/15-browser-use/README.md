# Arvutikasutusagentide (CUA) loomine

Arvutikasutusagentidel on võimalik veebisaitide külge reageerida samal moel nagu inimesel: avades brauseri, lehte uurides ja järgmist parimat tegevust valides. Selles õppetükis ehitate brauseri automatiseerimisagendi, mis otsib Airbnb-st, ekstraheerib struktuurset kuulutusteavet ja tuvastab Stockholmi odavaima peatumise.

Õppetükk ühendab Browser-Use AI-põhise navigeerimise jaoks, Playwrighti ja Chrome DevTools protokolli (CDP) brauserijuhtimiseks, Azure OpenAI nägemisvõimelise järeldamise jaoks ning Pydanticu struktuurse ekstraktsiooni jaoks.

## Sissejuhatus

Selles õppetükis käsitleme:

- Selle mõistmist, millal sobivad arvutikasutusagentid API-põhise automatiseerimise asemel paremini
- Browser-Use ühendamist Playwrighti ja CDP-ga usaldusväärseks brauseri elutsükli halduseks
- Azure OpenAI nägemise ja struktuurse Pydanticu väljundiga dünaamilistelt veebilehtedelt kuulutusteabe ekstraktsiooni
- Otsustamist, millal kasutada agenti-eesmärk, tegija-eesmärk või hübriidset brauseri automatiseerimise töövoogu

## Õpieesmärgid

Pärast selle õppetüki lõpetamist oskad:

- Konfigureerida Browser-Use koos Azure OpenAI ja Playwrightiga
- Luua brauseri automatiseerimise töövoog, mis navigeerib reaalsel veebisaidil ja haldab dünaamilisi kasutajaliidese elemente
- Ekstraheerida tüübitud tulemusi nähtavast lehekülje sisust ja muuta need edasiseks äriloogikaks
- Valida agent- ja tegijamustreid selle põhjal, kui ennustatav brauseri ülesanne on

## Koodinäide

Selles õppetükis on üks märkmiku juhend:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Käivitab CDP toega Chrome’i sessiooni, otsib Airbnb-st Stockholmi kuulutusi, ekstraheerib hinnad Browser-Use nägemise abil ja tagastab odavaima valiku struktuurandmetena.

## Eeldused

- Python 3.12+
- Azure OpenAI juurutus seadistatud teie keskkonnas
- Chrome või Chromium paigaldatud kohalikult
- Playwrighti sõltuvused paigaldatud
- Põhiline tuttavus asünkroonse Pythoniga

## Seadistus

Paigalda märkmikus kasutatud paketid:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Määra märkmiku poolt kasutatavad Azure OpenAI keskkonnamuutujad:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Valikuline: jäetakse vahele, kasutatakse vaikimisi uusimat API versiooni
AZURE_OPENAI_API_VERSION=...
```

## Arhitektuuri ülevaade

Märkmik demonstreerib hübriidset brauseri automatiseerimise töövoogu:

1. Chrome käivitatakse CDP-ga, nii et nii Playwright kui ka Browser-Use saavad jagada sama brauseri sessiooni.
2. Browser-Use agent tegeleb avara navigeerimisülesandega, nagu Airbnb avamine, hüpikaknate sulgemine ja Stockholmi otsimine.
3. Aktiivset lehte uuritakse struktuurse Pydanticu skeemi abil, et ekstraheerida kuulutuste pealkirjad, ööhinnad, hinnangud ja URL-id.
4. Python loogika võrdleb ekstraheeritud kuulutusi ja tähistab odavaima tulemuse.

See lähenemine säilitab paindliku, nägemispõhise järeldamise, mille poolest Browser-Use hea on, andes samas deterministliku brauserijuhtimise, kui seda on vaja.

## Peamised järeldused ja parimad praktikad

### Millal kasutada agendit vs tegijat

| Stsenaarium | Kasuta agenti | Kasuta tegijat |
|----------|-----------|-----------|
| Dünaamilised paigutused | Jah, tehisintellekt kohandub lehe muutustega hästi | Ei, haprad selektorid võivad puruneda |
| Tuntud struktuur | Ei, agent on aeglasem kui otsene juhtimine | Jah, kiire ja täpne |
| Elementide leidmine | Jah, loomulik keel töötab hästi | Ei, vaja on täpseid selektoreid |
| Ajajuhtimine | Ei, vähem ennustatav | Jah, täielik kontroll ootamiste ja katsete üle |
| Kompleksed töövood | Jah, käsitleb ootamatuid kasutajaliidese olekuid | Ei, nõuab selget harundamist |

### Browser-Use parimad praktikad

1. Alusta agentidega avastamiseks ja dünaamiliseks navigeerimiseks.
2. Lülitu otse lehe kontrollile, kui interaktsioon muutub ennustatavaks.
3. Kasuta struktureeritud väljundmudeleid, et ekstraheeritud andmed oleksid valideeritud ja tüübikindlad.
4. Lisa viivitused strateegiliselt pärast tegevusi, mis käivitavad nähtavaid kasutajaliidese muutusi.
5. Tee ekraanipilte, kui iteratsioon käib, nii on vigade leidmine lihtsam.
6. Ole valmis veebisaitide muudatusteks ja kujunda varuplaanid hüpikakende ja paigutuse nihkumiste jaoks.
7. Kasuta nii agenti kui tegija mustreid, et saada nii paindlikkust kui täpsust.

### Tootmaailma rakendused

- Reisitõrgete ja hindade jälgimine
- E-kaubanduse hindade võrdlus ja saadavuse kontroll
- Struktureeritud ekstraktsioon dünaamilistelt veebilehtedelt
- Nägemuspõhine kasutajaliidese testimine ja kontrollimine
- Veebisaitide jälgimine ja teavitamine
- Nutikas vormide täitmine mitmeastmelistes voogudes

## Tootmaailma näide: Microsoft Project Opal

Agent, keda selles õppetükis ehitad, on väike kohalik versioon **arvutikasutusagendist (CUA)** — programm, mis juhib brauserit nagu inimene. Microsoft toob seda ideed ettevõtetesse läbi **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, mis on Microsoft 365 Copiloti funktsioon.

Project Opali abil kirjeldad ülesande ja agent töötab sinu nimel, kasutades **arvutikasutust turvalises Windows 365 Cloud PC-s**, töötades organisatsiooni brauseripõhiste rakenduste, saitide ja andmetega. See töötab **asünkroonselt taustal**, ja sa saad igal ajal tegevust suunata või kontrolli üle võtta. Näited töödest:

- Turvagruppide liikmeks liitumise taotluste haldamine
- Audititõendite kogumine ja valideerimine vastavuskontrolliks
- IT intsidentide triage (piletite staatuse uuendamine, omanike määramine, dubleeritud sulgemine)
- Exceli andmete kogumine finantsaruandele

Opal on hea näide sellest, milline näeb välja **tootmiskõlblik, usaldusväärne** arvutikasutusagent — ja see tugevdab varasemate õppetükkide kontseptsioone:

| Selle kursuse kontseptsioon | Kuidas Project Opal seda rakendab |
|------------------------|-----------------------------|
| **Inimene tsüklis** (õppetükk 06) | Opal peatub sisselogimise, tundlike andmete või ebaselgete juhiste ootamiseks ning ei sisesta paroole ega esita vorme ilma selgesõnalise kinnituseta. Sa saad *Kontrolli võtta* ja *Kontrolli tagasi anda* töö keskel. |
| **Usaldusväärsed ja turvalised agendid** (õppetükid 06 ja 18) | Töötab isoleeritud Windows 365 Cloud PC-s, on vaikimisi ainult brauseri juurdepääsuga (muud arvutile ligipääsud blokeeritud, juhitud Intune’iga), kasutab *sinu* identiteeti, et pääseda ligi vaid lubatud andmetele, ja logib iga tegevuse auditeeritavuse tagamiseks. |
| **Planeerimine ja metakognitsioon** (õppetükid 07 ja 09) | Opal genereerib esmalt tööplaani, seejärel juhib iseenda järeldusi iga sammu juures ja peatub, kui tuvastab kahtlast tegevust. |
| **Taaskasutatavad võimed / tööriistad** (õppetükk 04) | **Oskused** võimaldavad kirjutada juhiseid korduvateks töödeks (importida `.md` failist või luua Opaliga) ja kasutada neid erinevates vestlustes. |

> **Saadavus:** Project Opal on praegu kasutajatele saadaval [Frontier varajase juurdepääsu programmis](https://adoption.microsoft.com/copilot/frontier-program/) Microsoft 365 Copiloti tellimusega ning administraator peab seadistuse lõpetama. Kuna tegemist on katselise Frontier funktsiooniga, võivad võimed aja jooksul muutuda.

## Lisamaterjalid

- [Alustamine Project Opal (Frontier)ga](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwrighti integratsiooni mall](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use tegija parameetrid ja sisu ekstraheerimine](https://docs.browser-use.com/customize/actor/all-parameters)
- [Kursuse seadistamine](../00-course-setup/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->