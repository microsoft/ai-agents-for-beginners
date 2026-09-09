# Arvutikasutusagentide (CUA) loomine

Arvutikasutusagendid saavad veebisaitidega suhelda samamoodi nagu inimene: avades brauseri, uurides lehte ja võttes järgmise parima tegevuse, mis põhineb nähtud informatsioonil. Selles õppetükis ehitate brauseri automatiseerimisagendi, mis otsib Airbnbst, võtab välja struktureeritud kuulutuste andmed ja tuvastab Stockholmi odavaima peatumiskoha.

Õppetükk ühendab Browser-Use'i AI-põhise navigeerimise jaoks, Playwrighti ja Chrome DevTools Protocoli (CDP) brauseri juhtimiseks, Azure OpenAI visiooni-põhise järeldamise jaoks ja Pydanticut struktureeritud ekstraheerimiseks.

## Sissejuhatus

See õppetükk käsitleb:

- Arusaamist, millal arvutikasutusagendid sobivad paremini kui ainult API-põhine automatiseerimine
- Browser-Use'i ühendamist Playwrighti ja CDP-ga usaldusväärseks brauseri elutsükli haldamiseks
- Azure OpenAI visiooni ja Pydanticu struktureeritud väljundi kasutamist dünaamiliste veebilehtede kuulutuste andmete ekstraheerimiseks
- Otsustamist, millal kasutada agendi-eesmärkset, näitleja-eesmärkset või hübriidset brauseri automatiseerimise töövoogu

## Õpieesmärgid

Pärast selle õppetüki läbimist oskad:

- Konfigureerida Browser-Use'i koos Azure OpenAI ja Playwrightiga
- Luua brauseri automatiseerimise töövoogu, mis navigeerib reaalsel veebisaidil ja käsitleb dünaamilisi kasutajaliidese elemente
- Ekstraheerida tüübistatud tulemused nähtavast lehekülje sisust ja kasutada neid äriloogikas
- Valida agendi- või näitlejamustreid vastavalt brauseri ülesande ennustatavusele

## Koodinäide

See õppetükk sisaldab üht märkmikujuhist:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Käivitab Chrome'i seansi CDP kaudu, otsib Airbnbst Stockholmi kuulutusi, ekstraheerib hindu Browser-Use visiooniga ja tagastab odavaima valiku struktureeritud andmetena.

## Eeltingimused

- Python 3.12+
- Azure OpenAI juurutus konfigureeritud teie keskkonnas
- Kohalikult installitud Chrome või Chromium
- Playwrighti sõltuvused installitud
- Põhiline tuttavus asünkroonse Pythoniga

## Seadistamine

Installi märkmikus kasutatavad paketid:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Märkmiku segajas kasutatavate Azure OpenAI keskkonnamuutujate seadistamine:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Valikuline: vaikimisi kasutatakse, kui versiooni ei ole määratud, kõige uuemat API versiooni
AZURE_OPENAI_API_VERSION=...
```

## Arhitektuuri ülevaade

Märkmik tutvustab hübriidset brauseri automatiseerimise töövoogu:

1. Chrome käivitub CDP-ga lubatult, nii saavad nii Playwright kui Browser-Use kasutada sama brauseriseanssi.
2. Browser-Use agent tegeleb avatud navigeerimisülesannetega, nagu Airbnb avamine, hüpikakende sulgemine ja Stockholmi otsimine.
3. Aktiivset lehte kontrollitakse struktureeritud Pydanticu skeemiga, et võtta välja kuulutuste pealkirjad, ööhind, hinnangud ja URLid.
4. Python loogika võrdleb ekstraheeritud kuulutusi ja tõstab esile odavaima tulemuse.

See lähenemine säilitab Browser-Use'i paindliku, visioonipõhise järeldamise, andes samas deterministliku brauserijuhtimise, kui see on vajalik.

## Olulised võtmekohad ja head praktikad

### Millal kasutada agenti vs näitlejat

| Scenario | Kasuta Agenti | Kasuta Näitlejat |
|----------|-----------|-----------|
| Dünaamilised paigutused | Jah, tehisintellekt suudab kohaneda lehe muudatustega | Ei, haprad valijad võivad puruneda |
| Tuntud struktuur | Ei, agent on aeglasem kui otsene juhtimine | Jah, kiire ja täpne |
| Elementide leidmine | Jah, loomuliku keele kasutamine toimib hästi | Ei, vaja täpseid valijaid |
| Ajakontroll | Ei, vähem ennustatav | Jah, täielik kontroll ootamiste ja korduste üle |
| Komplekssed töövood | Jah, käsitleb ootamatuid UI olekuid | Ei, nõuab selget harundamist |

### Browser-Use head praktikad

1. Alusta agentiga uurimiseks ja dünaamiliseks navigeerimiseks.
2. Vaheta otse lehekülje juhtimisele, kui interaktsioon muutub ennustatavaks.
3. Kasuta struktureeritud väljundmudeleid, et ekstraheeritud andmed oleksid valideeritud ja tüübikindlad.
4. Lisa strateegiliselt viivitusi pärast tegevusi, mis käivitavad nähtavaid UI muudatusi.
5. Tee iteratsiooni ajal ekraanipilte, et vigade leidmine oleks lihtsam.
6. Oota veebisaitide muutumist ja planeeri varuplaanid hüpikakende ja paigutuse nihkete jaoks.
7. Sega agentide ja näitlejate mustreid, et saada nii paindlikkus kui täpsus.

### Brauseri agentide turvapiirded

Brauseri agendid töötavad live-veebisaitidel, seega vajavad nad rangemaid piire kui ainult tuntud API kutsuv skript. Enne märkmiku demosid reaalse töövoo käivitamist defineeri piirangud, mida agent võib näha, klõpsata ja esitada.

1. **Piira sirvimise keskkonda.** Kasuta agenti pühendatud brauseriprofiilis või liivakastis ning jäta ligipääs ainult vajalikule domeenidele.
2. **Eralda vaatlus tegevusest.** Lase agentil esmalt otsida, lugeda ja andmeid ekstraheerida; nõua vormide esitamist, sõnumite saatmist, reisibroneeringute tegemist, ostude sooritamist, kirje kustutamist või konto seadete muutmist enne selgesõnalist kasutaja kinnitust.
3. **Ära pane paroole ega tundlikke andmeid nõudmistele ega logidesse.** Ära sisesta paroole, makseandmeid, sessiooniküpsiseid ega isikutuvastuse andmeid mudeli konteksti. Lase kasutajal autentimiseks sekkuda ja redact'i tundlikud väljad läbi logide.
4. **Kohtu lehe sisu kui ebausaldusväärse sisendiga.** Veebileht võib sisaldada juhiseid, mis on mõeldud agendile, mitte kasutajale. Agent peaks ignoreerima lehe teksti, mis palub muuta eesmärki, avaldada andmeid, keelata kaitsemeetmeid või külastada mitteseotud saite.
5. **Kasuta riskantsete sammude juures deterministlikke kontrollpunkte.** Kontrolli koodi abil kehtivat URLi, lehe pealkirja, valitud eset, hinda, saajat ja tegevuse kokkuvõtet enne kasutajalt lõpliku kinnituse küsimist.
6. **Sea eelarved ja peatamistingimused.** Piira tegevuste, korduste, vahelehtede ja minutite arvu, mida agent kasutab. Peata tegevus, kui lehe olek on kahtlane, mitte jätka klõpsamist.
7. **Salvesta kasulikud tõendid, mitte kõike.** Hoia tegevuste kokkuvõtteid, ajatempleid, URL-e, valitud elementide kirjeldusi ja ekraanipiltide viiteid, et ebaõnnestumisi saaks hiljem läbivaadata ilma tundlikku sisu liigse salvestamiseta.

Airbnb näites on turvaline vaikimisi otsida kuulutusi ja võtta hindu. Sisselogimine, hostiga ühenduse võtmine või broneeringu sooritamine peaks olema eraldi kasutajakinnitusega tegevus.

### Reaalse maailma rakendused

- Reisibroneeringute ja hindade jälgimine
- E-kaubanduse hindade võrdlus ja saadavuse kontroll
- Struktureeritud ekstraheerimine dünaamilistelt veebisaitidelt
- Visioonipõhine kasutajaliidese testimine ja kontrollimine
- Veebisaitide jälgimine ja hoiatused
- Nutikas vormi täitmine mitmeastmelistes töövoogudes

## Reaalse maailma näide: Microsoft Project Opal

Agent, mille selles õppetükis ehitate, on väike kohalik versioon **arvutikasutusagentist (CUA)** — programm, mis juhib brauserit samamoodi nagu inimene. Microsoft toob sama idee ettevõtetesse läbi **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, mis on Microsoft 365 Copiloti võimekus.

Project Opaliga kirjeldad ülesannet ja agent töötab sinu eest kasutades **arvutikasutust turvalisel Windows 365 Cloud PC-l**, toimides organisatsiooni brauseripõhistes rakendustes, saitidel ja andmetel. See töötab **taustal asünkroonselt** ja saad soovikorral tööd juhendada või üle võtta. Näited töökohustustest:

- Turvagruppide liikmesuse taotluste haldamine
- Audititõendite kogumine ja valideerimine vastavuskontrollide jaoks
- IT intsidentide sorteerimine (pileti staatuse uuendamine, omanike määramine, duplikaatide sulgemine)
- Exceli andmete koostamine finantsaruandesse

Opal on kasulik näide sellest, milline näeb välja **tööstuslik ja usaldusväärne** arvutikasutusagent — ja see kinnitab varasemate õppetükkide kontseptsioone:

| Kursuse kontseptsioon | Kuidas Project Opal seda rakendab |
|------------------------|-----------------------------|
| **Inimene tsüklis** (Õppetükk 06) | Opal peatub sisselogimise, tundlike andmete ja ebamääraste juhiste puhul ning ei sisesta paroole ega esita vorme ilma selgesõnalise kinnituseta. Sa saad tegevuse keskel *kontrolli võtta* ja *kontrolli tagastada*. |
| **Usaldusväärsed ja turvalised agendid** (Õppetükid 06 ja 18) | Töötab isoleeritud Windows 365 Cloud PC-s, on vaikimisi brauseripõhine (muud arvutiosa ligipääs on keelatud Intune’i kaudu), kasutab *sinu* identiteeti ja pääseb ligi vaid lubatud ressurssidele ning logib iga tegevuse auditeerimiseks. |
| **Planeerimine ja metakognitsioon** (Õppetükid 07 ja 09) | Opal genereerib esmalt tööplaani, seejärel jälgib enda järeldusi igal sammul ja peatub, kui tuvastab kahtlast käitumist. |
| **Taaskasutatavad võimekused / tööriistad** (Õppetükk 04) | **Oskused** võimaldavad sul kirjutada korduvate ülesannete juhiseid (imporditud `.md` failist või Opalis loodud) ja taaskasutada neid vestlustes. |

> **Saadavus:** Project Opal on hetkel saadaval [Frontieri varajase ligipääsu programmis](https://adoption.microsoft.com/copilot/frontier-program/) Microsoft 365 Copiloti tellimusega ning seadistuse peab administraator lõpetama. Kuna tegemist on eksperimendi Frontier funktsiooniga, võivad võimekused ajas muutuda.

## Teadmiste kontroll

Kontrolli oma teadmisi enne järgmise õppetüki juurde liikumist.

**1. Millal on brauseripõhine arvutikasutusagent sobivam kui ainult API-põhine töövoog?**

<details>
<summary>Vastus</summary>

Kasuta brauseri agenti, kui ülesanne sõltub veebikasutajaliidese nähtavusest, sait ei paku vajalikku API-d või leht muutub nii tihti, et fikseeritud API või valijate loogika oleks ebastabiilne. Kui stabiilne API on olemas sama ülesande jaoks, eelistage tavaliselt API-t, sest see on kiirem, lihtsam testida ja turvalisem.
</details>

**2. Hübriidtöövoos, milliseid osi peaks agent käsitlema ja milliseid osi Peaks otsene Playwrighti kood käsitlema?**

<details>
<summary>Vastus</summary>

Lase agendil tegeleda avatud navigeerimise ja dünaamiliste UI olekutega, nagu õige lehe leidmine või ootamatute hüpikute sulgemine. Lülitu Playwrighti otsesele juhtimisele, kui lehe struktuur on teada ja tegevus nõuab täpsust, kordusi, ootamist või deterministlikku valideerimist.
</details>

**3. Airbnb näidis leiab kuulutuse, mida kasutaja võib soovida broneerida. Mis peaks juhtuma enne, kui töövoog logib sisse, võtab ühendust hostiga või lõpetab broneeringu?**

<details>
<summary>Vastus</summary>

Töövoog peaks peatuma ja küsima selgesõnalist kasutajakinnitust. Enne päringu esitamist tuleks kuvada valitud kuulutuse, praeguse URL-i, hinna, kuupäevade ja kavandatud tegevuse selge kokkuvõte. Otsimine ja hindade ekstraheerimine võib toimuda autonoomselt; konto ligipääs, sõnumid, ostud ja broneeringud peaksid olema kasutaja poolt kinnitatud.
</details>

**4. Veebileht ütleb agendile, et ignoreeriks oma algseid juhiseid, külasta teist saiti ja avaldaks salvestatud mandaadid. Kuidas peaks agent seda teksti kohtlema?**

<details>
<summary>Vastus</summary>

Kohtu sellega kui ebausaldusväärse lehe sisuga, mitte arendaja või kasutaja juhisena. Agent peaks jääma lubatud domeeni ja ülesande ulatusse, keelduma saladuste avaldamisest ning hoiduma lehe teksti järgimisest, mis muudab eesmärki, keelab kaitsemeetmeid või suunab seotud välistesse saitidesse.
</details>

**5. Millised tõendid on kasulikud brauseri agendi töö jooksul hoida ja milliseid tuleks vältida?**

<details>
<summary>Vastus</summary>

Hoia tegevuste kokkuvõtteid, ajatempleid, URL-e, valitud elementide kirjeldusi, valideerimistulemusi ja ekraanipiltide viiteid, et töö tulemust hiljem kontrollida. Väldi paroolide, makseandmete, sessiooniküpsiste, isikuandmete või täielike lehesisude salvestamist, välja arvatud juhul, kui on konkreetne säilitamise ja privaatsuse põhjus.
</details>

## Täiendavad ressursid

- [Alustamine Project Opaliga (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright integratsiooni mall](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use näitleja parameetrid ja sisuekraanimine](https://docs.browser-use.com/customize/actor/all-parameters)
- [Kursuse seadistamine](../00-course-setup/README.md)

## Eelmine õppetükk

[Microsoft Agent Frameworki uurimine](../14-microsoft-agent-framework/README.md)

## Järgmine õppetükk

[Skaalautuvate agentide juurutamine](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->