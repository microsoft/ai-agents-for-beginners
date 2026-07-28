# Tietokoneen käyttöhallitusten (CUA) rakentaminen

Tietokoneen käyttöhallitukset voivat olla vuorovaikutuksessa verkkosivustojen kanssa samalla tavalla kuin ihminen: avaamalla selaimen, tutkimalla sivua ja tekemällä seuraavan parhaan toimenpiteen näkemänsä perusteella. Tässä oppitunnissa rakennat selaimen automaatioagentin, joka hakee Airbnb:stä, poimii rakenteellista kohdetietoa ja löytää halvimman majoituksen Tukholmassa.

Oppitunti yhdistää Browser-Use:n tekoälypohjaiseen navigointiin, Playwrightin ja Chrome DevTools Protocolin (CDP) selaimen ohjaukseen, Azure OpenAI:n näkökykyyn perustuvaan päättelyyn sekä Pydanticin rakenteelliseen poimintaan.

## Johdanto

Tässä oppitunnissa käsitellään:

- Ymmärtämään, milloin tietokoneen käyttöhallitukset sopivat paremmin kuin pelkkä API-automaatiota
- Browser-Use:n yhdistämistä Playwrightin ja CDP:n kanssa varmaksi selaimen elinkaaren hallinnaksi
- Azure OpenAI:n näkökyvyn ja rakenteellisen Pydantic-tuotoksen käyttöä dynaamisten verkkosivujen tietojen poimintaan
- Päätöksenteon agentti-ensimmäisen, toimija-ensimmäisen tai hybridiselaimen automaatiotyönkulun välillä

## Oppimistavoitteet

Oppitunnin suorittamisen jälkeen osaat:

- Konfiguroida Browser-Use Azure OpenAI:n ja Playwrightin kanssa
- Rakentaa selaimen automaatiotyönkulun, joka navigoi oikealla verkkosivustolla ja käsittelee dynaamisia käyttöliittymäelementtejä
- Poimia tyyppisidonnaisia tuloksia näkyvästä sivun sisällöstä ja muuntaa ne jälkikäyttöön liiketoimintalogiikassa
- Valita agentin ja toimijamallin välillä sen perusteella, kuinka ennustettava selaimen tehtävä on

## Koodiesimerkki

Tämä oppitunti sisältää yhden muistiinpanon tutoriaalin:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Käynnistää Chromen CDP:n kautta, hakee Airbnb:stä Tukholman kohteita, poimii hinnat Browser-Use:n näkökentän avulla ja palauttaa halvimman vaihtoehdon rakenteellisena tietona.

## Esivaatimukset

- Python 3.12+
- Azure OpenAI -asennus ympäristössäsi määritettynä
- Chrome tai Chromium asennettuna paikallisesti
- Playwrightin riippuvuudet asennettuna
- Perustason tuntemus async Pythonista

## Asennus

Asenna muistiinpanossa käytetyt paketit:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Aseta Azure OpenAI:n ympäristömuuttujat, joita muistiinpano käyttää:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Valinnainen: oletuksena viimeisin API-versio, jos jätetään pois
AZURE_OPENAI_API_VERSION=...
```

## Arkkitehtuurin yleiskatsaus

Muistiinpano demonstroi hybridiselaimen automaatiotyönkulkua:

1. Chrome käynnistyy CDP päällä, jotta sekä Playwright että Browser-Use voivat jakaa saman selaimesession.
2. Browser-Use-agentti hoitaa avoimena pysyviä navigointitehtäviä, kuten Airbnb:n avaamista, ponnahdusikkunoiden sulkemista ja hakua Tukholmalle.
3. Aktiivinen sivu tutkitaan rakenteellisella Pydantic-kaavalla poimien ilmoitusten otsikot, yökohtaiset hinnat, arvostelut ja URL-osoitteet.
4. Python-logiikka vertaa poimittuja tietoja ja korostaa halvimman tuloksen.

Tämä lähestymistapa säilyttää Browser-Use:n joustavan, näkökykyyn perustuvan päättelyn, mutta antaa samalla määrityspoikkeamatonta selaimen hallintaa tarpeen mukaan.

## Keskeiset opit ja parhaat käytännöt

### Milloin käyttää agenttia vs. toimijaa

| Tilanne | Käytä agenttia | Käytä toimijaa |
|----------|-----------|-----------|
| Dynaamiset asettelut | Kyllä, tekoäly mukautuu sivun muutoksiin | Ei, hauraat selektorit voivat rikkoutua |
| Tunnettu rakenne | Ei, agentti on hitaampi kuin suora ohjaus | Kyllä, nopea ja tarkka |
| Elementtien löytäminen | Kyllä, luonnollinen kieli toimii hyvin | Ei, tarkat selektorit vaaditaan |
| Aikahallinta | Ei, vähemmän ennustettava | Kyllä, täydellinen hallinta odotuksissa ja yrityksissä |
| Monimutkaiset työnkulut | Kyllä, käsittelee odottamattomia käyttöliittymän tiloja | Ei, vaatii eksplisiittiset haarautumiset |

### Browser-Use parhaat käytännöt

1. Aloita agentilla tutkimiseen ja dynaamiseen navigointiin.
2. Vaihda suoraan sivun hallintaan, kun vuorovaikutuksesta tulee ennustettavaa.
3. Käytä rakenteellisia tuotemalleja, jotta poimittu data validoidaan ja on tyypinmukaista.
4. Lisää viiveitä strategisesti toimien jälkeen, jotka laukaisevat näkyvät käyttöliittymän muutokset.
5. Ota ruutukaappauksia toistuvasti, jotta virheiden selvitys helpottuu.
6. Odota verkkosivustojen muuttuvan ja suunnittele varautumissuunnitelmat ponnahdusikkunoille ja asettelujen muutoksille.
7. Yhdistä agentti- ja toimijamallit saadaksesi sekä joustavuutta että tarkkuutta.

### Turvakaiteet selainagenteille

Selainagentit toimivat live-verkkosivustoilla, joten niiden rajat tarvitsevat olla tiukemmat kuin pelkän tunnetun API:n kutsuvan skriptin. Ennen kuin siirryt muistiinpanon demosta oikeaan työnkulkuun, määrittele ohjaukset siitä, mitä agentti voi nähdä, klikata ja lähettää.

1. **Määrittele selausympäristö.** Suorita agentti omassa selainprofiilissa tai hiekkalaatikossa ja rajoita se tehtävän vaatimiin domaineihin.
2. **Erottele havainnointi toiminnasta.** Anna agentin ensin etsiä, lukea ja poimia tietoa; vaadi eksplisiittinen hyväksyntä ennen lomakkeiden lähettämistä, viestien lähettämistä, matkavarauksia, ostoksia, tietueiden poistoa tai tiliasetusten muuttamista.
3. **Pidä salaisuudet pois käskyistä ja jäljistä.** Älä laita salasanoja, maksutietoja, istuntokeksejä tai raakaa henkilökohtaista dataa mallin kontekstiin. Anna käyttäjän hoitaa todennus ja sensuroida arkaluontoiset kentät lokitiedoista.
4. **Kohtele sivun sisältöä epäluotettavana syötteenä.** Verkkosivusto voi sisältää ohjeita, jotka on tarkoitettu agentille, ei käyttäjälle. Agentin tulee sivuuttaa sivuteksti, joka pyytää muuttamaan tavoitettaan, paljastamaan tietoja, poistamaan turvatoimia tai vierailemaan epäolennaisilla sivustoilla.
5. **Käytä määrityspoikkeamatonta tarkistusta riskialttiissa vaiheissa.** Varmista nykyinen URL-osoite, sivun otsikko, valittu kohde, hinta, vastaanottaja ja toimenpiteen yhteenveto koodilla ennen kuin pyydät käyttäjää hyväksymään lopullisen vaiheen.
6. **Aseta budjetit ja pysäytysehdot.** Määrittele toimien, yritysten, välilehtien ja agentin käyttämien minuuttien enimmäismäärät. Lopeta, jos sivun tila on epäselvä sen sijaan, että jatkaisit klikkailua.
7. **Tallenna hyödylliset todisteet, ei kaikkea.** Säilytä toimintayhteenvedot, aikaleimat, URL:t, valittujen elementtien kuvaukset ja ruutukaappausviitteet, jotta virheitä voi tarkastella ilman tarpeetonta arkaluontoista sivusisältöä.

Airbnb-esimerkissä turvallinen oletusarvo on hakea ilmoituksia ja poimia hintoja. Kirjautuminen, isäntään ottaminen yhteyttä tai varauksen tekeminen tulisi olla erillinen, käyttäjän hyväksymä toimenpide.

### Käytännön sovellukset

- Matkavaraukset ja hintojen seuranta
- Verkkokaupan hintavertailu ja saatavuustarkastukset
- Rakenteellinen poiminta dynaamisilta verkkosivuilta
- Näkökykyyn perustuva käyttöliittymän testaus ja validointi
- Verkkosivuston seuranta ja hälytykset
- Älykäs lomakkeiden täyttö monivaiheisissa prosesseissa

## Käytännön esimerkki: Microsoft Project Opal

Tässä oppitunnissa rakentamasi agentti on pieni, paikallinen versio **tietokoneen käyttöhallituksesta (CUA)** — ohjelmasta, joka ohjaa selainta kuten ihminen. Microsoft tuo tätä samaa ideaa yritysmaailmaan **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, Microsoft 365 Copilotin ominaisuus.

Project Opalissa kuvaat tehtävän ja agentti työskentelee puolestasi käyttäen **tietokoneen käyttöä turvallisessa Windows 365 Cloud PC:ssä**, toimiessaan organisaatiosi selaimella käytettävien sovellusten, sivustojen ja datan kautta. Se toimii **asynkronisesti taustalla**, ja voit ohjata työtä tai ottaa hallinnan milloin tahansa. Esimerkkejä tehtävistä ovat:

- Turvaryhmäjäsenyyspyyntöjen hallinta
- Tarkastusnäyttöjen kerääminen ja validoiminen vaatimustenmukaisuudessa
- IT-ongelmien käsittely (lippujen tilan päivitys, vastuuhenkilöiden määritys, kaksoiskappaleiden sulkeminen)
- Excel-datan kokoaminen talousraporttipakettiin

Opal on hyödyllinen esimerkki siitä, millainen on **tuotantotason, luotettava** tietokoneen käyttöhallitus — ja vahvistaa aiemmista oppitunneista tuttuja käsitteitä:

| Kurssin käsite | Miten Project Opal soveltaa sitä |
|------------------------|-----------------------------|
| **Ihminen silmukassa** (Oppitunti 06) | Opal pysähtyy kirjautumistietojen, arkaluonteisen datan tai epäselvien ohjeiden kohdalla, eikä syötä salasanoja tai lähetä lomakkeita ilman nimenomaista vahvistusta. Voit *ottaa hallinnan* ja *palauttaa hallinnan* kesken tehtävän. |
| **Luotettavat ja turvalliset agentit** (Oppitunnit 06 & 18) | Toimii eristetyssä Windows 365 Cloud PC:ssä, on oletuksena vain selainkäyttöinen (muut tietokoneen käyttö estetty Intunen avulla), käyttää *sinun* identiteettiäsi joten se pääsee vain valtuuttamiisi kohteisiin, ja kirjaa jokaisen toiminnon auditointia varten. |
| **Suunnittelu ja metakognitio** (Oppitunnit 07 & 09) | Opal laatii ensin suunnitelman tehtävälle, sitten valvoo omaa päättelyään jokaisessa vaiheessa ja pysähtyy, jos havaitsee epäilyttävää toimintaa. |
| **Uudelleenkäytettävät kyvyt / työkalut** (Oppitunti 04) | **Taidot** antavat sinun kirjoittaa ohjeita toistuville tehtäville (.md-tiedostosta tuotuja tai Opalilla laadittuja) ja käyttää niitä uudestaan keskusteluissa. |

> **Saatavuus:** Project Opal on tällä hetkellä käytettävissä [Frontierin varhaiskäyttöohjelmassa](https://adoption.microsoft.com/copilot/frontier-program/) Microsoft 365 Copilot -tilaajille, ja järjestelmänvalvojan tulee suorittaa käyttöönotto. Koska kyseessä on kokeellinen Frontier-ominaisuus, sen toiminnot voivat muuttua ajan myötä.

## Lisäresurssit

- [Aloita Project Opalin kanssa (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright -integraatiomalli](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use toimijan parametrit ja sisällön poiminta](https://docs.browser-use.com/customize/actor/all-parameters)
- [Kurssin alustus](../00-course-setup/README.md)

## Edellinen oppitunti

[Microsoft Agent Frameworkin tutkiminen](../14-microsoft-agent-framework/README.md)

## Seuraava oppitunti

[Skalautuvien agenttien käyttöönotto](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->