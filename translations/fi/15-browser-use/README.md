# Tietokoneen käyttöagenttien (CUA) rakentaminen

Tietokoneen käyttöagentit voivat olla vuorovaikutuksessa verkkosivustojen kanssa samalla tavalla kuin ihmiset: avaamalla selaimen, tarkastelemalla sivua ja tekemällä seuraavan parhaan toimenpiteen havaintojensa perusteella. Tässä oppitunnissa rakennat selainautomaattisen agentin, joka hakee Airbnb:stä, poimii jäsenneltyä tietoa listauksista ja tunnistaa Tukholman halvimman majoituksen.

Oppitunti yhdistää Browser-Use:n tekoälypohjaiseen navigointiin, Playwrightin ja Chrome DevTools Protocolin (CDP) selainohjaukseen, Azure OpenAI:n näkökykyyn perustuvaan päättelyyn sekä Pydanticin jäsenneltyyn tiedonpoimintaan.

## Johdanto

Tässä oppitunnissa käydään läpi:

- Milloin tietokoneen käyttöagentit sopivat paremmin kuin pelkkä API-automaatio
- Browser-Use:n yhdistäminen Playwrightiin ja CDP:hen luotettavan selainelinkaaren hallintaan
- Azure OpenAI:n näkökyvyn ja jäsennellyn Pydantic-vastauksen käyttäminen listatietojen poimintaan dynaamisilta verkkosivuilta
- Päätöksenteko agentti-, toimija- tai hybridi selainautomaatiotyönkulun välillä

## Oppimistavoitteet

Oppitunnin jälkeen osaat:

- Määrittää Browser-Use:n Azure OpenAI:n ja Playwrightin kanssa
- Rakentaa selainautomaatiotyönkulun, joka navigoi aidolla verkkosivustolla ja käsittelee dynaamisia käyttöliittymäelementtejä
- Poimia tyypitettyjä tuloksia näkyvistä sivusisällöistä ja käyttää niitä jatkotoimissa
- Valita agentti- ja toimijamallit selaintehtävän ennustettavuuden perusteella

## Koodiesimerkki

Tämä oppitunti sisältää yhden muistikirjatutoriaalin:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Käynnistää Chrome-istunnon CDP:n kautta, hakee Airbnb:stä Tukholman listauksia, poimii hinnat Browser-Use:n näkökyvyllä ja palauttaa halvimman vaihtoehdon jäsenneltynä datana.

## Esivaatimukset

- Python 3.12+
- Azure OpenAI -käyttöönotto ympäristössäsi määritettynä
- Chrome tai Chromium asennettuna paikallisesti
- Playwright-riippuvuudet asennettuina
- Perustason tutustuminen asynkroniseen Pythoniin

## Asennus

Asenna muistikirjassa käytetyt paketit:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Aseta muistikirjan käyttämät Azure OpenAI -ympäristömuuttujat:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Valinnainen: oletuksena käytetään uusinta API-versiota, jos se jätetään pois
AZURE_OPENAI_API_VERSION=...
```

## Arkkitehtuurin yleiskatsaus

Muistikirja havainnollistaa hybridi selainautomaatiotyönkulkua:

1. Chrome käynnistyy CDP-yhteydellä, jotta sekä Playwright että Browser-Use voivat jakaa saman selainistunnon.
2. Browser-Use-agentti hoitaa avoimia navigointitehtäviä, kuten Airbnb:n avaamisen, ponnahdusikkunoiden sulkemisen ja Tukholman haun.
3. Aktiivinen sivu tarkastetaan jäsennellyn Pydantic-skeeman avulla, jotta listauksen otsikot, yökohtaiset hinnat, arvostelut ja URL-osoitteet voidaan poimia.
4. Python-logiikka vertaa poimittuja listauksia ja korostaa halvimman vaihtoehdon.

Tämä lähestymistapa säilyttää Browser-Use:n joustavuuden näkökykyyn perustuvan päättelyn osalta samalla, kun se tarjoaa määrityksellisen selainohjauksen tarpeen mukaan.

## Keskeiset opit ja parhaat käytännöt

### Milloin käyttää agenttia vs. toimijaa

| Tilanne | Käytä agenttia | Käytä toimijaa |
|----------|-----------|-----------|
| Dynaamiset asettelut | Kyllä, tekoäly mukautuu sivun muutoksiin | Ei, hauraita valitsimia voi rikkoutua |
| Tunnettu rakenne | Ei, agentti on hitaampi kuin suora ohjaus | Kyllä, nopea ja tarkka |
| Elementtien löytäminen | Kyllä, luonnollinen kieli toimii hyvin | Ei, tarkat valitsimet vaaditaan |
| Ajanhallinta | Ei, vähemmän ennustettava | Kyllä, täydellinen hallinta odotuksissa ja uudelleenyrityksissä |
| Monimutkaiset työnkulut | Kyllä, käsittelee odottamattomia UI-tiloja | Ei, vaatii eksplisiittistä haarautumista |

### Browser-Use:n parhaat käytännöt

1. Aloita agentilla tutkimiseen ja dynaamiseen navigointiin.
2. Vaihda suoraan sivun ohjaukseen, kun vuorovaikutuksesta tulee ennustettavaa.
3. Käytä jäsenneltyjä tulosmalleja, jotta poimittu data validoidaan ja tyypitetään turvallisesti.
4. Lisää viiveitä strategisesti toimintojen jälkeen, jotka laukaisevat näkyviä käyttöliittymän muutoksia.
5. Ota kuvakaappauksia toistettaessa, jotta virheiden jäljittäminen helpottuu.
6. Odota verkkosivujen muutoksia ja suunnittele varasuunnitelmat ponnahdusikkunoille sekä asettelun vaihteluille.
7. Yhdistä agentti- ja toimijamallit saadaksesi sekä joustavuutta että tarkkuutta.

### Käytännön sovellukset

- Matkavaraukset ja hintaseuranta
- Verkkokaupan hintavertailut ja saatavuustarkistukset
- Jäsennelty tiedon poiminta dynaamisilta verkkosivuilta
- Näkökykyä hyödyntävä käyttöliittymän testaus ja varmennus
- Verkkosivujen seuranta ja hälytykset
- Älykäs lomakkeiden täyttäminen monivaiheisissa prosesseissa

## Käytännön esimerkki: Microsoft Project Opal

Tässä oppitunnissa rakentamasi agentti on pieni paikallinen versio **tietokoneen käyttöagentista (CUA)** — ohjelmasta, joka ohjaa selainta kuten ihminen. Microsoft tuo saman idean yrityskäyttöön **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, Microsoft 365 Copilotin ominaisuuteen.

Project Opalin avulla kuvailet tehtävän, ja agentti toimii puolestasi käyttäen **tietokoneen käyttöä suojatussa Windows 365 Cloud PC:ssä**, toimiden organisaatiosi selauspohjaisissa sovelluksissa, sivustoissa ja tiedoissa. Se toimii **asynkronisesti taustalla**, ja voit ohjata työtä tai ottaa hallinnan milloin tahansa. Esimerkkitehtäviä ovat:

- Turvaryhmäjäsenyyspyynnöt
- Tarkastusnäyttöjen kerääminen ja validointi vaatimustenmukaisuuden tarkastuksia varten
- IT-ongelmien lajittelu (lipputilan päivitys, vastuuhenkilöiden määritys, duplikaattien sulkeminen)
- Excel-datan kokoaminen talouden sulkukansioksi

Opal on hyödyllinen referenssi siitä, millainen **tuotantotason, luotettava** tietokoneen käyttöagentti on — ja se vahvistaa aiemmissa oppitunneissa esitettyjä konsepteja:

| Kurssin käsite | Miten Project Opal soveltaa sitä |
|------------------------|-----------------------------|
| **Ihminen mukana prosessissa** (Oppitunti 06) | Opal pysähtyy kirjautumistietoja, arkaluontoista dataa tai epämääräisiä ohjeita varten, eikä koskaan syötä salasanoja tai lähetä lomakkeita vahvistuksen ilman. Voit *ottaa hallinnan* ja *palauttaa hallinnan* kesken tehtävän. |
| **Luotettavat ja turvalliset agentit** (Oppitunnit 06 & 18) | Toimii eristetyssä Windows 365 Cloud PC:ssä, on oletuksena selaimella käytettävä (muu tietokoneen käyttö estetty Intunen avulla), käyttää *sinun* identiteettiäsi, joten pääsee vain sinulle sallittuihin resursseihin ja kirjaa kaikki toimet auditointia varten. |
| **Suunnittelu & metakognitio** (Oppitunnit 07 & 09) | Opal laatii ensin suunnitelman tehtävään, valvoo päättelyään jokaisessa vaiheessa ja pysähtyy epäilyttävien toimintojen havaitessaan. |
| **Uudelleenkäytettävät taidot / työkalut** (Oppitunti 04) | **Skills** antaa mahdollisuuden kirjoittaa toistuvien tehtävien ohjeet (tuodaan `.md`-tiedostosta tai luodaan Opalilla) ja käyttää niitä uudelleen keskusteluissa. |

> **Saatavuus:** Project Opal on tällä hetkellä käytettävissä [Frontier early access program -ohjelmaan](https://adoption.microsoft.com/copilot/frontier-program/) osallistuvilla Microsoft 365 Copilot -tilaajilla, ja järjestelmänvalvojan tulee suorittaa asennus. Koska se on kokeellinen Frontier-ominaisuus, ominaisuudet voivat muuttua ajan myötä.

## Lisäresurssit

- [Aloita Project Opalin (Frontier) käyttö](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use:n Playwright-integraatiomalli](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use toimijan parametrit ja sisällön poiminta](https://docs.browser-use.com/customize/actor/all-parameters)
- [Kurssin asennus](../00-course-setup/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->