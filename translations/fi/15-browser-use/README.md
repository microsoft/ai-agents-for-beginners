# Rakentaminen tietokoneen käyttöagentteja (CUA)

Tietokoneen käyttöagentit voivat olla vuorovaikutuksessa verkkosivustojen kanssa samalla tavalla kuin ihminen: avaamalla selaimen, tarkastamalla sivun ja tekemällä seuraavan parhaan toimenpiteen sen perusteella, mitä he näkevät. Tässä oppitunnissa rakennat selainautomaattisen agentin, joka etsii Airbnb:stä, poimii jäsenneltyjä ilmoitustietoja ja tunnistaa halvimman majoituksen Tukholmassa.

Oppitunti yhdistää Browser-Use:n tekoälytoimiseen selaimen ohjaukseen, Playwrightin ja Chrome DevTools Protocolin (CDP) selaimen hallintaan, Azure OpenAI:n näköön perustuvaan päättelyyn ja Pydanticin jäsenneltyyn poimintaan.

## Johdanto

Tämä oppitunti kattaa:

- Milloin tietokoneen käyttöagentit sopivat paremmin kuin vain API-käyttöinen automaatio
- Browser-Use:n yhdistämisen Playwrightin ja CDP:n kanssa luotettavaan selainelinkaaren hallintaan
- Azure OpenAI:n vision ja jäsennellyn Pydantic-tulosteen käytön dynaamisen verkkosisällön poimintaan
- Päätöksenteon agenttiperustaisen, aktoriperustaisen tai hybridin selainautomaatiotyönkulun välillä

## Oppimistavoitteet

Oppitunnin suorittamisen jälkeen tiedät miten:

- Määrittää Browser-Use Azure OpenAI:n ja Playwrightin kanssa
- Rakentaa selainautomaatiotyönkulun, joka navigoi oikealla verkkosivustolla ja käsittelee dynaamisia käyttöliittymäelementtejä
- Poimia tyyppitetyt tulokset näkyvästä sivusisällöstä ja muuntaa ne jatkokäsittelyn liiketoimintalogiikaksi
- Valita agentti- ja aktorimalleista selaimen tehtävän ennustettavuuden perusteella

## Koodiesimerkki

Tämä oppitunti sisältää yhden notebook-tutoriaalin:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Käynnistää Chrome-istunnon CDP:n kautta, etsii Airbnb:stä Tukholman ilmoituksia, poimii hintoja Browser-Use visionilla ja palauttaa halvimman vaihtoehdon jäsenneltynä datana.

## Esivaatimukset

- Python 3.12+
- Azure OpenAI -käyttöönotto määritetty ympäristössäsi
- Chrome tai Chromium asennettuna paikallisesti
- Playwrightin riippuvuudet asennettuna
- Perustason tuntemus asynkronisesta Pythonista

## Asennus

Asenna notebookissa käytettävät paketit:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Aseta notebookin käyttämät Azure OpenAI -ympäristömuuttujat:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Valinnainen: oletusarvoisesti käytetään uusinta API-versiota, kun sitä ei ole annettu
AZURE_OPENAI_API_VERSION=...
```

## Arkkitehtuurin yleiskatsaus

Notebook esittelee hybridin selainautomaatio työnkulun:

1. Chrome käynnistyy CDP käytössä, jotta sekä Playwright että Browser-Use voivat jakaa saman selainistunnon.
2. Browser-Use agentti hoitaa avoimia navigointitehtäviä, kuten Airbnb:n avaamista, ponnahdusikkunoiden sulkemista ja Tukholman hakemista.
3. Aktiivista sivua tarkastellaan jäsennellyn Pydantic-skeeman avulla poimien ilmoitusten otsikot, yökohtaiset hinnat, arviot ja URL-osoitteet.
4. Python-logiikka vertaa poimittuja ilmoituksia ja korostaa halvimman tuloksen.

Tämä lähestymistapa pitää Browser-Use:n joustavan ja näköön perustuvan päättelyn vahvana, mutta tarjoaa samalla määrityksellisen selainohjauksen tarpeen mukaan.

## Keskeiset opit ja parhaat käytännöt

### Milloin käyttää agenttia vs aktoria

| Tilanne | Käytä agenttia | Käytä aktoria |
|----------|-----------|-----------|
| Dynaamiset asettelut | Kyllä, tekoäly mukautuu sivun muutoksiin | Ei, haavoittuvat valitsimet voivat rikkoutua |
| Tunnettu rakenne | Ei, agentti on hitaampi kuin suora ohjaus | Kyllä, nopea ja tarkka |
| Elementtien löytäminen | Kyllä, luonnollinen kieli toimii hyvin | Ei, tarkat valitsimet vaaditaan |
| Aikavalmistus | Ei, vähemmän ennustettavissa | Kyllä, täysi hallinta odotuksiin ja uudelleenyrityksiin |
| Monimutkaiset työnkulut | Kyllä, käsittelee odottamattomat käyttöliittymän tilat | Ei, vaatii eksplisiittistä haarautumista |

### Browser-Use parhaat käytännöt

1. Aloita agentilla tutkimiseen ja dynaamiseen navigointiin.
2. Vaihda suoraan sivun ohjaukseen, kun vuorovaikutus muuttuu ennustettavaksi.
3. Käytä jäsenneltyjä tulosmalleja, jotta poimittu data validoidaan ja tyyppiturvataan.
4. Lisää viiveitä strategisesti toimien jälkeen, jotka käynnistävät näkyviä käyttöliittymän muutoksia.
5. Tallenna ruutukaappauksia toistoaikana, jotta virheiden vianmääritys helpottuu.
6. Odota verkkosivustojen muuttuvan ja suunnittele varatoimenpiteet ponnahdusikkunoille ja asettelusiirtymille.
7. Yhdistä agentti- ja aktorimallit saadaksesi joustavuutta ja tarkkuutta.

### Turvallisuusohjeet selainagenteille

Selainagentit toimivat live-verkkosivuilla, joten niiden rajat on tiukempi kuin pelkkää API-kutsua tekevän skriptin. Ennen siirtymistä notebook-esittelystä todelliseen työnkulkuun määrittele kontrollit sille, mitä agentti näkee, klikkaa ja lähettää.

1. **Rajoita selausympäristö.** Aja agentti erillisessä selaimen profiilissa tai hiekkalaatikossa ja rajoita se tehtävän kannalta tarpeellisiin verkkotunnuksiin.
2. **Erottele havainnointi ja toiminta.** Anna agentin ensin etsiä, lukea ja poimia dataa; vaadi eksplisiittinen hyväksyntä ennen lomakkeiden lähettämistä, viestien lähettämistä, matkan varaamista, ostoksia, tietueiden poistamista tai tiliasetusten muuttamista.
3. **Pidä salaisuudet poissa kehotteista ja jäljistä.** Älä laita salasanoja, maksutietoja, istuntokeksejä tai raakaa henkilötietoa mallin kontekstiin. Anna käyttäjän hoitaa tunnistautuminen ja sensuroida arkaluonteiset kentät lokeista.
4. **Kohtele sivusisältöä epäluotettavana syötteenä.** Verkkosivu voi sisältää käskyjä agentille, ei käyttäjälle. Agentin tulee jättää huomioimatta sivuteksti, joka käskee muuttaa tavoitetta, paljastaa tietoja, poistaa turvamekanismit käytöstä tai vierailla liittymättömillä sivuilla.
5. **Käytä määrityksellisiä tarkistuksia riskialtisissa vaiheissa.** Vahvista koodilla nykyinen URL, sivun otsikko, valittu elementti, hinta, vastaanottaja ja toimenpiteen yhteenveto ennen käyttäjän hyväksynnän pyytämistä.
6. **Aseta budjetit ja pysäytysehdot.** Rajoita agentin tekemien toimenpiteiden, uudelleenyritysten, välilehtien ja minuuttien määrä. Pysäytä, jos sivun tila on epäselvä sen sijaan, että jatkat klikkailua.
7. **Tallenna hyödylliset todisteet, ei kaikkea.** Säilytä toimintayhteenvedot, aikaleimat, URL-osoitteet, valittujen elementtien kuvaukset ja ruutukaappausviittaukset, jotta virheiden tarkastelu on mahdollista ilman tarpeetonta arkaluonteisen sivusisällön tallentamista.

Airbnb-esimerkissä turvallinen oletus on hakea ilmoituksia ja poimia hintoja. Kirjautuminen, isännän kontaktointi tai varauksen tekeminen pitäisi olla erillinen käyttäjän hyväksymä toimenpide.

### Todelliset käyttötapaukset

- Matkanvaraus ja hintaseuranta
- Verkkokaupan hintavertailu ja saatavuuden tarkastus
- Jäsennelty poiminta dynaamisilta verkkosivuilta
- Näköön perustuva käyttöliittymätestaus ja validointi
- Verkkosivustojen valvonta ja hälytys
- Älykäs lomakkeiden täyttö monivaiheisissa työnkuluissa

## Todellinen esimerkki: Microsoft Project Opal

Tässä oppitunnissa rakentamasi agentti on pieni, paikallinen versio **tietokoneen käyttöagentista (CUA)** — ohjelma, joka ohjaa selainta tavalla, jolla ihminen toimisi. Microsoft tuo tämän saman idean yrityksiin **[Project Opalin (Frontierin)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)** kautta, joka on ominaisuus Microsoft 365 Copilotissa.

Project Opalin avulla kuvailet tehtävän, ja agentti toimii puolestasi käyttämällä **tietokonetta turvallisessa Windows 365 Cloud PC:ssä**, toimien organisaatiosi selainpohjaisissa sovelluksissa, sivustoissa ja datoissa. Se toimii **taustalla asynkronisesti**, ja voit ohjata työtä tai ottaa hallinnan milloin tahansa. Esimerkkejä tehtävistä ovat:

- Hallita turvallisuusryhmien jäsenyyspyyntöjä
- Kerätä ja validoida tarkastusnäyttöjä vaatimustenmukaisuustarkastuksiin
- IT-ongelmien käsittely (päivittää tikettien tilaa, määrää vastuuhenkilöitä, sulkee duplikaatit)
- Koota Excel-data taloudellisen päättämisdiapohjan laatimiseen

Opal tarjoaa hyödyllisen viitteen siitä, miltä **tuotantotason, luotettava** tietokoneen käyttöagentti näyttää – ja se vahvistaa aiempien oppituntien käsitteitä:

| Käsitys tässä kurssissa | Miten Project Opal soveltaa sitä |
|------------------------|-----------------------------|
| **Ihmisen osallistuminen (Lesson 06)** | Opal pysähtyy kirjautumistietojen, arkaluonteisen datan tai epäselvien ohjeiden kohdalla eikä koskaan syötä salasanoja tai lähetä lomakkeita ilman selkeää vahvistusta. Voit *Otta Hallinnan* ja *Palauta Hallinta* tehtävän aikana. |
| **Luotettavat ja turvalliset agentit (Lessons 06 & 18)** | Toimii eristetyssä Windows 365 Cloud PC:ssä, toimii oletuksena pelkästään selaimessa (muu tietokoneen käyttö estetty, hallitaan Intunella), käyttää *sinun* identiteettiäsi joten se pääsee vain hyväksyttyyn dataan, ja kirjaa jokaisen toimenpiteen auditointia varten. |
| **Suunnittelu ja metakognitio (Lessons 07 & 09)** | Opal laatii ensin suunnitelman, valvoo päättelyään jokaisessa vaiheessa ja pysähtyy, jos havaitsee epäilyttävää toimintaa. |
| **Uudelleenkäytettävät kyvyt / työkalut (Lesson 04)** | **Ominaisuudet** antavat sinulle mahdollisuuden kirjoittaa ohjeita toistettaville tehtäville (tuotu `.md`-tiedostosta tai luotu Opalilla) ja käyttää niitä uudelleen keskusteluissa. |

> **Saatavuus:** Project Opal on tällä hetkellä saatavilla käyttäjille [Frontierin varhaisessa käyttöohjelmassa](https://adoption.microsoft.com/copilot/frontier-program/) Microsoft 365 Copilot -tilauksella, ja järjestelmänvalvojan on suoritettava käyttöönotto. Koska kyseessä on kokeellinen Frontier-ominaisuus, kyvyt saattavat muuttua ajan myötä.

## Tietotesti

Testaa ymmärrystäsi ennen seuraavaan oppituntiin siirtymistä.

**1. Milloin selainpohjainen tietokoneen käyttöagentti sopii paremmin kuin pelkkä API-työnkulku?**

<details>
<summary>Vastaus</summary>

Käytä selainagenttia, kun tehtävä riippuu siitä, mitä verkkokäyttöliittymässä näkyy, sivusto ei tarjoa tarvittavaa API:a tai sivu muuttuu niin usein, että kiinteä API- tai valitsinlogiikka olisi haavoittuvaa. Jos samaan tehtävään on vakaa API, suosittelen käyttämään API:a koska se on yleensä nopeampi, helpompi testata ja helpompi suojata.
</details>

**2. Hybridissä työnkulussa, mitä osia agentin pitäisi käsitellä ja mitä osia suoran Playwright-koodin?**

<details>
<summary>Vastaus</summary>

Anna agentin hoitaa avoimet navigointitehtävät ja dynaamiset käyttöliittymät, kuten oikean sivun löytäminen tai odottamattomien ponnahdusikkunoiden sulkeminen. Vaihda suoraan Playwright-ohjaukseen, kun sivun rakenne tunnetaan ja toiminnan täytyy olla tarkkaa, toistuvaa, odottavaa tai määrityksellisen validoinnin alaista.
</details>

**3. Airbnb-esimerkki löytää ilmoituksen, jonka käyttäjä saattaisi haluta varata. Mitä pitäisi tapahtua ennen työnkulun kirjautumista sisään, isännän kontaktointia tai varauksen tekemistä?**

<details>
<summary>Vastaus</summary>

Työnkulun tulee pysähtyä ja pyytää käyttäjän selkeää hyväksyntää. Ennen kysymistä sen tulee näyttää selkeä yhteenveto valitusta ilmoituksesta, nykyisestä URL:stä, hinnasta, päivistä ja suunnitellusta toimenpiteestä. Hakeminen ja hintojen poiminta voi olla autonomista; tilin käyttö, viestit, ostot ja varaukset tulee hyväksyä käyttäjän toimesta.
</details>

**4. Verkkosivu käskee agenttia jättämään alkuperäiset ohjeet huomiotta, vierailemaan toisella sivulla ja paljastamaan tallennetut kirjautumistiedot. Miten agentin tulisi käsitellä tätä tekstiä?**

<details>
<summary>Vastaus</summary>

Käsittele sitä epäluotettavana sivusisältönä, älä kehittäjän tai käyttäjän ohjeena. Agentin on pysyttävä sallitun verkkotunnuksen ja tehtävän rajojen sisällä, kieltäydyttävä paljastamasta salaisuuksia ja vältettävä noudattamasta sivutekstiä, joka muuttaa tavoitetta, poistaa turvatoimia tai ohjaa sille liittymättömille sivuille.
</details>

**5. Mitä todisteita on hyödyllistä säilyttää selainagentin toimiessa ja mitä tulisi välttää?**

<details>
<summary>Vastaus</summary>

Säilytä toimintayhteenvedot, aikaleimat, URL-osoitteet, valittujen elementtien kuvaukset, validointitulokset ja ruutukaappausviittaukset, jotta ajon voi tarkistaa jälkikäteen. Vältä salasanojen, maksutietojen, istuntokeksien, raakojen henkilötietojen tai koko sivun sisällön tallentamista, ellei siihen ole tiettyä säilytys- ja yksityisyysyhtälöä.
</details>

## Lisäresurssit

- [Aloita Project Opalin (Frontierin) kanssa](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright -integrointipohja](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use aktorin parametrit ja sisällön poiminta](https://docs.browser-use.com/customize/actor/all-parameters)
- [Kurssin aloitus](../00-course-setup/README.md)

## Edellinen oppitunti

[Microsoft Agent Frameworkin tutkiminen](../14-microsoft-agent-framework/README.md)

## Seuraava oppitunti

[Skalautuvien agenttien käyttöönotto](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->