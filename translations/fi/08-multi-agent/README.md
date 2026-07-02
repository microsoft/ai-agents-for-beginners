[![Multi-Agent Design](../../../translated_images/fi/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Napsauta yllä olevaa kuvaa nähdäksesi tämän oppitunnin videon)_

# Moni-agenttisuunnittelumallit

Heti kun aloitat projektin, joka sisältää useita agenteja, sinun on otettava huomioon moni-agenttisuunnittelumalli. Ei kuitenkaan välttämättä ole heti selvää, milloin siirtyä moni-agenteihin ja mitkä ovat niiden edut.

## Johdanto

Tässä oppitunnissa pyrimme vastaamaan seuraaviin kysymyksiin:

- Missä tilanteissa moni-agenteja voidaan käyttää?
- Mitkä ovat moni-agenttien käytön edut verrattuna siihen, että yksi yksittäinen agentti hoitaa useita tehtäviä?
- Mitkä ovat moni-agenttisuunnittelumallin toteuttamisen rakennuspalikat?
- Miten voimme saada näkyvyyden siihen, miten useat agentit ovat vuorovaikutuksessa keskenään?

## Oppimistavoitteet

Tämän oppitunnin jälkeen sinun pitäisi osata:

- Tunnistaa tilanteet, joissa moni-agenteja voidaan käyttää
- Tunnistaa moni-agenttien käytön edut verrattuna yksittäiseen agenttiin.
- Ymmärtää moni-agenttisuunnittelumallin toteuttamisen rakennuspalikat.

Mikä on laajempi kokonaiskuva?

*Moni agenttia on suunnittelumalli, joka mahdollistaa useiden agenttien yhteistyön yhteisen tavoitteen saavuttamiseksi*.

Tätä mallia käytetään laajasti eri aloilla, kuten robotiikassa, autonomisissa järjestelmissä ja hajautetussa laskennassa.

## Tilanteet, joissa moni-agenteja voidaan käyttää

Missä tilanteissa moni-agenttien käyttö on hyvä ratkaisu? Vastaus on, että on monia tilanteita, joissa useiden agenttien käyttäminen on hyödyllistä, erityisesti seuraavissa tapauksissa:

- **Suuret työkuormat**: Suuret työtehtävät voidaan jakaa pienempiin tehtäviin ja jakaa eri agenteille, mikä mahdollistaa rinnakkaisen käsittelyn ja nopeamman valmistumisen. Tällainen esimerkki on suuri datankäsittelytehtävä.
- **Monimutkaiset tehtävät**: Monimutkaiset tehtävät, kuten suuret työkuormat, voidaan pilkkoa pienempiin alatehtäviin ja jakaa eri agenteille, jotka erikoistuvat tiettyyn tehtävän osa-alueeseen. Hyvä esimerkki tästä on autonomiset ajoneuvot, joissa eri agentit hoitavat navigaatiota, esteiden havaitsemista ja kommunikaatiota muiden ajoneuvojen kanssa.
- **Monipuolinen asiantuntemus**: Eri agentit voivat omata monipuolista asiantuntemusta, mikä mahdollistaa tehtävän eri osa-alueiden tehokkaamman hoitamisen kuin yksittäisellä agentilla. Tässä tapauksessa hyvä esimerkki on terveydenhuolto, jossa agentit voivat hallita diagnostiikkaa, hoitosuunnitelmia ja potilasseurantaa.

## Edut moni-agenttien käytöstä yksittäiseen agenttiin verrattuna

Yksittäinen agenttijärjestelmä voi toimia hyvin yksinkertaisissa tehtävissä, mutta monimutkaisemmissa tehtävissä useiden agenttien käyttö voi tarjota useita etuja:

- **Erikoistuminen**: Jokainen agentti voi erikoistua tiettyyn tehtävään. Yksittäisen agentin erikoistumisen puute tarkoittaa, että agentti osaa tehdä kaikkea, mutta voi hämmentyä monimutkaisen tehtävän edessä. Se voi esimerkiksi päätyä tekemään tehtävän, johon se ei ole parhaiten soveltuva.
- **Skaalautuvuus**: Järjestelmän on helpompi skaalata lisäämällä agentteja sen sijaan, että ylikuormitetaan yksittäistä agenttia.
- **Vikasietoisuus**: Jos yksi agentti epäonnistuu, muut voivat jatkaa toimintaansa, mikä varmistaa järjestelmän luotettavuuden.

Otetaan esimerkki: varataan matka käyttäjälle. Yksittäisen agenttijärjestelmän tulisi hoitaa kaikki matkan varaamiseen liittyvät asiat, lentoihin löytymisestä hotelli- ja vuokra-autojen varaamiseen. Yksittäisen agentin pitäisi pystyä käsittelemään kaikki nämä tehtävät, mikä voisi johtaa monimutkaiseen ja monoliittiseen järjestelmään, jota on vaikea ylläpitää ja skaalata. Moni-agenttijärjestelmässä voisi olla erilaisia agentteja, jotka erikoistuvat lentojen etsimiseen, hotellien varaamiseen ja vuokra-autojen järjestämiseen. Tämä tekisi järjestelmästä modulaarisemman, helpommin ylläpidettävän ja skaalautuvan.

Vertaa tätä matkatoimistoon, joka toimii perheyrityksenä verrattuna matkatoimistoon, joka toimii franchising-periaatteella. Perheyrityksessä yksi agentti hoitaisi kaikki matkan varaamisen osa-alueet, kun taas franchisingissa eri agentit hoitaisivat eri osa-alueita.

## Moni-agenttisuunnittelumallin toteuttamisen rakennuspalikat

Ennen kuin voit toteuttaa moni-agenttisuunnittelumallin, sinun tulee ymmärtää mallin rakennuspalikat.

Tehdään tämä konkreettisemmaksi katsomalla uudelleen esimerkkiä käyttäjän matkan varaamisesta. Tässä tapauksessa rakennuspalikat voisivat olla:

- **Agenttien välinen kommunikaatio**: Lennon etsintään, hotellin varaamiseen ja vuokra-autojen järjestämiseen erikoistuneiden agenttien tulee kommunikoida ja jakaa tietoa käyttäjän mieltymyksistä ja rajoitteista. Sinun tulee päättää protokollat ja menetelmät tälle kommunikaatiolle. Konkreettisesti tämä tarkoittaa, että lentoagentin pitää kommunikoida hotelli-agentin kanssa varmistaakseen, että hotelli varataan samoille päiville kuin lento. Tämä tarkoittaa, että agenttien tulee jakaa tietoa käyttäjän matkustuspäivistä, mikä puolestaan tarkoittaa, että sinun täytyy päättää *mitkä agentit jakavat tietoa ja miten heidän tietojensa jakaminen tapahtuu*.
- **Koordinointimekanismit**: Agenttien tulee koordinoida toimintaansa varmistaakseen, että käyttäjän mieltymykset ja rajoitteet täyttyvät. Käyttäjän mieltymys voi olla, että hotelli on lähellä lentokenttää, kun taas rajoite voi olla se, että vuokra-autot ovat vain lentokentällä. Tämä tarkoittaa, että hotellin varaamiseen erikoistuneen agentin pitää koordinoida toimintaansa vuokra-autojen varaamiseen erikoistuneen agentin kanssa. Sinun täytyy siis päättää *miten agentit koordinoivat toimintaansa*.
- **Agenttien arkkitehtuuri**: Agenteilla tulee olla sisäinen rakenne päätöksentekoa ja käyttäjän kanssa käytävistä vuorovaikutuksista oppimista varten. Tämä tarkoittaa, että lentoagentilla tulee olla sisäinen rakenne, joka mahdollistaa päätösten tekemisen suositeltavista lennoista. Sinun tulee päättää *miten agentit tekevät päätöksiä ja oppivat vuorovaikutuksista käyttäjän kanssa*. Esimerkkinä agentin oppimisesta ja kehittymisestä voisi olla, että lentoagentti käyttää koneoppimismallia suositellakseen lentoja käyttäjälle aiempien mieltymysten perusteella.
- **Näkyvyys moni-agenttien vuorovaikutukseen**: Sinun tulee saada näkyvyys siihen, miten useat agentit ovat vuorovaikutuksessa keskenään. Tämä tarkoittaa, että sinulla tulee olla työkaluja ja tekniikoita agenttien toiminnan ja vuorovaikutusten seuraamiseen. Tämä voi olla esimerkiksi lokitus- ja monitorointityökaluina, visualisointityökaluina sekä suorituskykymittareina.
- **Moni-agenttikaaviot**: On olemassa eri kaavioita moni-agenttijärjestelmien toteuttamiseen, kuten keskitetty, hajautettu ja hybridiratkaisuja. Sinun tulee päättää, mikä malli parhaiten sopii käyttötarkoitukseesi.
- **Ihminen kehityksen osana**: Useimmissa tapauksissa ihmisen tulee olla mukana ja sinun tulee ohjeistaa agentteja, milloin pyytää ihmisen väliintuloa. Tämä voi olla esimerkiksi silloin, kun käyttäjä pyytää tiettyä hotellia tai lentoa, jota agentit eivät ole suositelleet, tai pyytää vahvistusta ennen lentojen tai hotellin varaamista.

## Näkyvyys moni-agenttien vuorovaikutukseen

On tärkeää, että sinulla on selkeä näkyvyys siihen, miten useat agentit ovat vuorovaikutuksessa keskenään. Tämä näkyvyys on välttämätön virheiden jäljittämiseksi, optimoinniksi ja järjestelmän tehokkuuden varmistamiseksi. Tätä varten sinun tulee olla työkaluja ja menetelmiä agenttien toiminnan ja vuorovaikutusten seurantaan. Tämä voi olla esimerkiksi lokitus- ja monitorointityökalujen, visualisointityökalujen sekä suorituskykymittareiden muodossa.

Esimerkiksi käyttäjän matkan varaamisen tapauksessa voitaisiin olla käyttöliittymä, joka näyttää kunkin agentin tilan, käyttäjän mieltymykset ja rajoitteet sekä agenttien välisen vuorovaikutuksen. Tämä näkymä voisi näyttää käyttäjän matkustuspäivät, lentoagentin suosittelemat lennot, hotelliagentin suosittelemat hotellit ja vuokra-autojen agentin suosittelemat autot. Näin saisit selkeän kuvan siitä, miten agentit ovat vuorovaikutuksessa ja täyttyvätkö käyttäjän mieltymykset ja rajoitukset.

Tarkastellaan kutakin näistä osa-alueista tarkemmin.

- **Lokitus- ja monitorointityökalut**: Haluat, että jokaisesta agentin suorittamasta toiminnosta tehdään lokimerkintä. Lokimerkintä voi tallentaa tiedon, mikä agentti suoritti toiminnon, mikä toiminto oli, milloin se suoritettiin ja mikä oli lopputulos. Tätä tietoa voidaan käyttää virheiden jäljittämiseen ja optimointiin.
- **Visualisointityökalut**: Visualisointityökalut auttavat hahmottamaan agenttien välisen vuorovaikutuksen intuitiivisemmalla tavalla. Esimerkiksi voisi olla graafi, joka näyttää tiedonkulun agenttien välillä. Tämä auttaa tunnistamaan pullonkaulat, tehottomuudet ja muita järjestelmän ongelmakohtia.
- **Suorituskykymittarit**: Suorituskykymittarit auttavat seuraamaan moni-agenttijärjestelmän tehokkuutta. Voit esimerkiksi mitata tehtävän suorittamiseen kulunutta aikaa, tehtävien määrää aikayksikköä kohden ja agenttien tekemiä suositusten tarkkuutta. Näiden avulla voit tunnistaa parannuskohteita ja optimoida järjestelmää.

## Moni-agenttikaaviot

Katsotaanpa joitakin konkreettisia malleja moni-agenttisovellusten luomiseksi. Tässä muutamia kiinnostavia malleja:

### Ryhmäkeskustelu

Tämä malli on hyödyllinen, kun haluat luoda ryhmäkeskustelusovelluksen, jossa useat agentit voivat kommunikoida keskenään. Tyypillisiä käyttötapauksia ovat tiimityö, asiakastuki ja sosiaalinen verkostoituminen.

Tässä mallissa kukin agentti edustaa käyttäjää ryhmäkeskustelussa, ja viestit lähetetään agenttien välillä viestintäprotokollaa käyttäen. Agentit voivat lähettää viestejä ryhmäkeskusteluun, vastaanottaa viestejä sieltä ja vastata muiden agenttien viesteihin.

Malli voidaan toteuttaa keskitetyn arkkitehtuurin avulla, jossa kaikki viestit kulkevat keskitetyn palvelimen kautta, tai hajautetun arkkitehtuurin avulla, jossa viestit vaihdetaan suoraan agenttien välillä.

![Group chat](../../../translated_images/fi/multi-agent-group-chat.ec10f4cde556babd.webp)

### Tehtävien siirto

Tämä malli on hyödyllinen, kun haluat luoda sovelluksen, jossa useat agentit voivat siirtää tehtäviä keskenään.

Tyypillisiä käyttötapauksia ovat asiakastuki, tehtävien hallinta ja työnkulkujen automaatio.

Tässä mallissa kukin agentti edustaa tehtävää tai työvaihetta, ja agentit voivat siirtää tehtäviä toisille agenteille ennalta määriteltyjen sääntöjen mukaisesti.

![Hand off](../../../translated_images/fi/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Yhteistyössä suodatus

Tämä malli on hyödyllinen, kun haluat luoda sovelluksen, jossa useat agentit voivat tehdä yhteistyötä käyttäjille suunnattujen suositusten tekemiseksi.

Miksi haluat, että useat agentit tekevät yhteistyötä? Koska jokainen agentti voi omata erilaista asiantuntemusta ja voi osallistua suositusprosessiin eri tavoin.

Otetaan esimerkki, jossa käyttäjä haluaa suosituksen parhaasta osakkeesta ostettavaksi pörssissä.

- **Toimialan asiantuntija**: Yksi agentti voi olla asiantuntija tietyllä toimialalla.
- **Tekninen analyysi**: Toinen agentti voi olla teknisen analyysin asiantuntija.
- **Perusanalyysi**: Ja toinen agentti voi olla perusanalyysin asiantuntija. Yhteistyössä nämä agentit voivat tarjota käyttäjälle kattavamman suosituksen.

![Recommendation](../../../translated_images/fi/multi-agent-filtering.d959cb129dc9f608.webp)

## Tilanne: Hyvitysprosessi

Kuvitellaan tilanne, jossa asiakas yrittää saada hyvitystä tuotteesta. Tässä prosessissa voi olla mukana useita agentteja, mutta jaetaan ne tässä tapauksessa hyvitysprosessiin erikoistuneisiin agenteihin ja yleisiin agenteihin, joita voidaan käyttää muissa prosesseissa.

**Hyvitysprosessiin erikoistuneet agentit**:

Seuraavat agentit saattavat olla mukana hyvitysprosessissa:

- **Asiakasagentti**: Tämä agentti edustaa asiakasta ja on vastuussa hyvitysprosessin käynnistämisestä.
- **Myyjäagentti**: Tämä agentti edustaa myyjää ja vastaa hyvityksen käsittelystä.
- **Maksuagentti**: Tämä agentti edustaa maksuprosessia ja vastaa asiakkaan maksun hyvittämisestä.
- **Ratkaisuagentti**: Tämä agentti edustaa ratkaisuprosessia ja vastaa mahdollisten hyvitysprosessin aikana ilmenevien ongelmien ratkaisemisesta.
- **Noudattavuusagentti**: Tämä agentti valvoo, että hyvitysprosessi noudattaa säädöksiä ja politiikkoja.

**Yleiset agentit**:

Näitä agenteja voidaan käyttää yrityksen muilla toimialoilla.

- **Toimitusagentti**: Tämä agentti edustaa toimitusprosessia ja vastaa tuotteen palauttamisesta myyjälle. Tätä agenttia voidaan käyttää sekä hyvitysprosessissa että yleisessä tuotteen toimituksessa esimerkiksi ostotapahtuman yhteydessä.
- **Palauteagentti**: Tämä agentti edustaa palautteen keruuprosessia ja vastaa palautteen keräämisestä asiakkaalta. Palautetta voidaan kerätä milloin tahansa, ei pelkästään hyvitysprosessin aikana.
- **Eskalaatioagentti**: Tämä agentti vastaa ongelmien eskaloinnista korkeammalle tukitasolle. Tätä agenttilajia voi käyttää missä tahansa prosessissa, jossa ongelman eskalaatio on tarpeen.
- **Ilmoitusagentti**: Tämä agentti vastaa ilmoitusten lähettämisestä asiakkaalle hyvitysprosessin eri vaiheissa.
- **Analytiikkaagentti**: Tämä agentti vastaa hyvitysprosessiin liittyvien tietojen analysoinnista.
- **Auditointiagentti**: Tämä agentti vastaa hyvitysprosessin auditoinnista varmistaakseen, että se suoritetaan oikein.
- **Raportointagentti**: Tämä agentti vastaa raporttien laatimisesta hyvitysprosessista.
- **Tietämyksagentti**: Tämä agentti vastaa tietämyspohjan ylläpidosta hyvitysprosessiin liittyvien tietojen osalta. Tämä agentti voi olla asiantunteva sekä hyvityksissä että yrityksen muissa liiketoiminnan osa-alueissa.
- **Turvaagentti**: Tämä agentti vastaa hyvitysprosessin turvallisuudesta.
- **Laatuagentti**: Tämä agentti vastaa hyvitysprosessin laadun varmistamisesta.

Edellä listatuissa agenteissa on paljon sekä hyvitysprosessiin erikoistuneita että yleisiä agentteja, joita voidaan käyttää yrityksen muissa osissa. Toivottavasti tämä antaa sinulle käsityksen, miten voit päättää, mitä agenteja kannattaa käyttää moni-agenttijärjestelmässäsi.

## Tehtävä

Suunnittele moni-agenttijärjestelmä asiakastukiprosessille. Tunnista prosessiin osallistuvat agentit, niiden roolit ja vastuut sekä miten ne ovat vuorovaikutuksessa keskenään. Pohdi sekä asiakastukiprosessiin erikoistuneita että yleisiä agentteja, joita voidaan käyttää muissa yrityksesi osissa.
> Mieti hetki ennen kuin luet seuraavan ratkaisun, saatat tarvita enemmän agenteja kuin luulet.

> VINKKI: Mieti asiakastuen eri vaiheita ja ota myös huomioon kaikki järjestelmään tarvittavat agentit.

## Ratkaisu

[Solution](./solution/solution.md)

## Tietotarkistukset

Kysymys: Milloin tulisi harkita monen agentin käyttöä?

- [ ] A1: Kun sinulla on pieni työkuorma ja yksinkertainen tehtävä.
- [ ] A2: Kun sinulla on suuri työkuorma
- [ ] A3: Kun sinulla on yksinkertainen tehtävä.

[Solution quiz](./solution/solution-quiz.md)

## Yhteenveto

Tässä oppitunnissa olemme tarkastelleet moniagenttisuunnittelumallia, mukaan lukien tilanteet, joissa moniagentteja voidaan käyttää, moniagenttien käytön edut yksittäiseen agenttiin verrattuna, moniagenttisuunnittelumallin toteutuksen perusosat sekä kuinka saada näkyvyyttä useiden agenttien väliseen vuorovaikutukseen.

### Lisää kysymyksiä moniagenttisuunnittelumallista?

Liity [Microsoft Foundry Discordiin](https://discord.com/invite/ATgtXmAS5D) tavata muita oppijoita, osallistua toimistotunteihin ja saada vastauksia tekoälyagenttien kysymyksiisi.

## Lisäresurssit

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework -dokumentaatio</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Agenttisuunnittelumallit</a>


## Edellinen oppitunti

[Planning Design](../07-planning-design/README.md)

## Seuraava oppitunti

[Metacognition in AI Agents](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->