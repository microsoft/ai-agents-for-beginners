[![Moni-agenttisuunnittelumallit](../../../translated_images/fi/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Klikkaa yllä olevaa kuvaa katsoaksesi tämän oppitunnin videon)_

# Moni-agenttisuunnittelumallit

Heti kun alat työstää projektia, joka sisältää useita agenteja, sinun tulee ottaa huomioon moni-agenttisuunnittelumalli. Ei kuitenkaan välttämättä ole heti selvää, milloin siirtyä moni-agenteihin ja mitkä ovat niiden edut.

## Johdanto

Tässä oppitunnissa pyrimme vastaamaan seuraaviin kysymyksiin:

- Missä tilanteissa moni-agentteja voi soveltaa?
- Mitkä ovat moni-agenttien käytön edut verrattuna yhteen agenttiin, joka tekee useita tehtäviä?
- Mitkä ovat moni-agenttisuunnittelumallin toteuttamisen rakennuspalikat?
- Miten näemme, miten moni agentti on vuorovaikutuksessa keskenään?

## Oppimistavoitteet

Tämän oppitunnin jälkeen sinun tulisi osata:

- Tunnistaa tilanteet, joissa moni-agentteja voi käyttää
- Tunnistaa moni-agenttien edut yksittäiseen agenttiin verrattuna
- Ymmärtää moni-agenttisuunnittelumallin toteuttamisen rakennuspalikat

Mikä on laajempi kokonaiskuva?

*Moni agentti on suunnittelumalli, joka mahdollistaa useiden agenttien työskentelyn yhdessä yhteisen tavoitteen saavuttamiseksi*.

Tätä mallia käytetään laajasti eri aloilla, mukaan lukien robotiikka, autonomiset järjestelmät ja hajautettu laskenta.

## Tilanteet, joissa moni-agentteja voi soveltaa

Missä tilanteissa moni-agentit ovat hyvä valinta? Vastaus on, että on monia tilanteita, joissa useiden agenttien käyttö on hyödyllistä, erityisesti seuraavissa tapauksissa:

- **Suuret työkuormat**: Suuret työmäärät voidaan jakaa pienempiin tehtäviin ja jakaa eri agenteille, mikä mahdollistaa rinnakkaiskäsittelyn ja nopeamman valmistumisen. Esimerkiksi suuri datankäsittelytehtävä.
- **Monimutkaiset tehtävät**: Kuten suurissa työkuormissa, monimutkaiset tehtävät voidaan pilkkoa pienempiin osatehtäviin ja jakaa eri agenteille, joista kukin erikoistuu tiettyyn tehtävän osa-alueeseen. Hyvä esimerkki on autonomisissa ajoneuvoissa, joissa erilaiset agentit hallitsevat navigointia, esteiden havaitsemista ja viestintää muiden ajoneuvojen kanssa.
- **Monimuotoinen asiantuntijuus**: Eri agenteilla voi olla erilaista asiantuntijuutta, mikä mahdollistaa erilaisten tehtävän osa-alueiden tehokkaamman hoitamisen kuin yksittäisagentti. Tässä tapauksessa hyvä esimerkki on terveydenhuolto, jossa agentit voivat hallita diagnostiikkaa, hoitosuunnitelmia ja potilasseurantaa.

## Moni-agenttien käytön edut yksittäiseen agenttiin verrattuna

Yksittäinen agenttijärjestelmä voi toimia hyvin yksinkertaisissa tehtävissä, mutta monimutkaisemmissa tehtävissä moni-agenttien käyttö voi tarjota useita etuja:

- **Erikoistuminen**: Jokainen agentti voi erikoistua tiettyyn tehtävään. Yksittäisessä agentissa erikoistumisen puute tarkoittaa, että agentti voi tehdä kaikkea, mutta saattaa hämmentyä monimutkaisesta tehtävästä. Se voisi esimerkiksi päätyä tekemään tehtävän, johon se ei ole parhaiten soveltuva.
- **Skaalautuvuus**: Järjestelmiä on helpompi skaalata lisäämällä uusia agentteja kuin ylikuormittamalla yksittäistä agenttia.
- **Vikankestävyys**: Jos yksi agentti epäonnistuu, toiset voivat jatkaa toimintaansa, mikä takaa järjestelmän luotettavuuden.

Otetaan esimerkki: varataan käyttäjälle matka. Yksittäinen agenttijärjestelmä joutuisi hoitamaan kaikki matkanvarausprosessin osa-alueet, lentojen löytämisestä hotellien ja vuokra-autojen varaamiseen. Tämän saavuttamiseksi agentilla pitäisi olla työkaluja kaikkien näiden tehtävien hoitamiseen. Tämä voisi johtaa monimutkaiseen ja monoliittiseen järjestelmään, jota on vaikea ylläpitää ja skaalata. Moni-agenttijärjestelmässä voi olla eri agentteja, jotka ovat erikoistuneet löytämään lentoja, varaamaan hotelleja ja vuokra-autoja. Tämä tekisi järjestelmästä modulaarisemman, helpommin ylläpidettävän ja skaalautuvan.

Vertaa tätä matkatoimistoon, joka toimii pienenä perheyrityksenä verrattuna matkatoimistoon, joka toimii franchising-periaatteella. Perheyrityksessä yksi agentti hoitaisi kaikki matkanvarauksen osa-alueet, kun taas franchisingissa eri agentit hoitaisivat eri osa-alueita.

## Moni-agenttisuunnittelumallin toteuttamisen rakennuspalikat

Ennen kuin voit toteuttaa moni-agenttisuunnittelumallin, sinun tulee ymmärtää, mitkä ovat mallin rakennuspalikat.

Tehdään tästä konkreettisempaa katsomalla uudelleen esimerkkiä käyttäjän matkan varaamisesta. Tässä tapauksessa rakennuspalikat sisältäisivät:

- **Agenttien välinen viestintä**: Lentojen etsintään, hotellien ja vuokra-autojen varaamiseen liittyvien agenttien tulee viestiä ja jakaa tietoa käyttäjän mieltymyksistä ja rajoitteista. Sinun täytyy päättää, mitä protokollia ja menetelmiä käytetään tähän viestintään. Konkreettisesti tämä tarkoittaa, että lentojen etsintäagentin pitää viestiä hotellivarausagentin kanssa varmistaakseen, että hotelli on varattu samoille päivämäärille kuin lento. Tämä tarkoittaa, että agenttien täytyy jakaa tietoa käyttäjän matka-ajankohdista, eli sinun täytyy päättää *mitkä agentit jakavat tietoa ja miten tietoa jaetaan*.
- **Koordinointimekanismit**: Agenttien on koordinoitava toimintaansa varmistaakseen, että käyttäjän mieltymykset ja rajoitukset täyttyvät. Käyttäjän mieltymys voi olla esimerkiksi hotelli lähellä lentokenttää, kun taas rajoitus voi olla vuokra-autojen saatavuus vain lentokentällä. Tämä tarkoittaa, että hotellivarausagentin on koordinoitava vuokra-autoagentin kanssa käyttäjän mieltymysten ja rajoitteiden täyttämiseksi. Sinun täytyy siis päättää *miten agentit koordinoivat toimintaansa*.
- **Agenttirakenne**: Agenteilla täytyy olla sisäinen rakenne, jolla ne tekevät päätöksiä ja oppivat vuorovaikutuksistaan käyttäjän kanssa. Tämä tarkoittaa, että lentojen etsintäagentin on oltava rakennettu siten, että se voi tehdä päätöksiä suositeltavista lennoista käyttäjälle. Sinun täytyy päättää *miten agentit tekevät päätöksiä ja oppivat vuorovaikutuksistaan käyttäjän kanssa*. Esimerkki agentin oppimisesta voi olla se, että lentojen etsintäagentti käyttää koneoppimismallia suositellakseen lentoja käyttäjän aiempien mieltymysten perusteella.
- **Näkyvyys moni-agenttien vuorovaikutukseen**: Sinun on nähtävä, miten useat agentit ovat vuorovaikutuksessa keskenään. Tämä tarkoittaa, että tarvitset työkaluja ja tekniikoita agenttien toiminnan ja vuorovaikutusten seuraamiseen. Tämä voi olla esimerkiksi lokitus- ja valvontatyökaluja, visualisointityökaluja ja suorituskykymittareita.
- **Moni-agenttimallit**: On eri malleja moni-agenttijärjestelmien toteuttamiseen, kuten keskitetyt, hajautetut ja hybridirakenteet. Sinun pitää valita malli, joka parhaiten sopii käyttötarkoitukseesi.
- **Ihminen mukana prosessissa**: Useimmissa tapauksissa ihminen on mukana prosessissa, ja agentteja pitää ohjeistaa, milloin pyytää ihmisen väliintuloa. Tämä voi olla esimerkiksi käyttäjä pyytämässä tiettyä hotellia tai lentoa, jota agentit eivät ole suositelleet, tai pyytäessä varmistusta ennen lennon tai hotellin varaamista.

## Näkyvyys moni-agenttien vuorovaikutukseen

On tärkeää, että näet, miten useat agentit ovat vuorovaikutuksessa keskenään. Tämä näkyvyys on olennaista virheenkorjauksessa, optimoinnissa ja koko järjestelmän toimivuuden varmistamisessa. Tämän saavuttamiseksi tarvitset työkaluja ja tekniikoita agenttien toimintojen ja vuorovaikutusten seuraamiseen. Tämä voi olla esimerkiksi lokitus- ja valvontatyökaluja, visualisointityökaluja ja suorituskykymittareita.

Esimerkiksi käyttäjän matkan varaamisen tapauksessa voit käyttää kojelautaa, joka näyttää kunkin agentin tilan, käyttäjän mieltymykset ja rajoitteet sekä agenttien väliset vuorovaikutukset. Tämä kojelauta voisi näyttää käyttäjän matkapäivät, lentojen suositukset lentoagentilta, hotellien suositukset hotelliagentilta ja vuokra-autojen suositukset vuokra-autoagentilta. Tämä antaisi selkeän näkymän siitä, miten agentit ovat vuorovaikutuksessa ja täyttyvätkö käyttäjän mieltymykset ja rajoitteet.

Katsotaanpa näitä osa-alueita tarkemmin:

- **Lokitus- ja valvontatyökalut**: Haluat kirjata muistiin jokaisen agentin tekemän toiminnon. Lokiaineisto voi sisältää tiedot agentista, joka toimi, tehdyistä toimista, toiminta-ajankohdasta ja toiminnon tuloksesta. Näitä voidaan käyttää virheiden korjaukseen, optimointiin ja muihin tarkoituksiin.

- **Visualisointityökalut**: Visualisointityökalut auttavat näkemään agenttien väliset vuorovaikutukset intuitiivisemmalla tavalla. Esimerkiksi voit käyttää graafia, joka näyttää informaation kulun agenttien välillä. Tämä voi auttaa tunnistamaan pullonkauloja, tehottomuuksia ja muita järjestelmän ongelmia.

- **Suorituskykymittarit**: Suorituskykymittarit auttavat seuraamaan moni-agenttijärjestelmän tehokkuutta. Esimerkiksi voit mitata tehtävän suorittamiseen kulunutta aikaa, valmiiden tehtävien määrää aikayksikköä kohden sekä agenttien antamien suositusten tarkkuutta. Tämä tieto auttaa löytämään parannuskohteita ja optimoimaan järjestelmää.

## Moni-agenttimallit

Tutustutaan muutamiin konkreettisiin malleihin, joita voimme käyttää moni-agenttisovelluksissa. Tässä muutamia mielenkiintoisia malleja harkittavaksi:

### Ryhmäkeskustelu

Tämä malli sopii, kun haluat luoda ryhmäkeskustelusovelluksen, jossa useat agentit voivat viestiä keskenään. Tyypillisiä käyttötapauksia ovat tiimityö, asiakastuki ja sosiaalinen verkostoituminen.

Tässä mallissa jokainen agentti edustaa käyttäjää ryhmäkeskustelussa, ja viestit vaihdetaan agenttien välillä viestintäprotokollan avulla. Agentit voivat lähettää viestejä ryhmäkeskusteluun, vastaanottaa niistä viestejä ja vastata muiden agenttien viesteihin.

Tätä mallia voidaan toteuttaa keskitetyn arkkitehtuurin avulla, jossa kaikki viestit kulkevat keskuspalvelimen kautta, tai hajautetun arkkitehtuurin avulla, jossa viestit vaihdetaan suoraan.

![Ryhmäkeskustelu](../../../translated_images/fi/multi-agent-group-chat.ec10f4cde556babd.webp)

### Tehtävien siirto

Tämä malli soveltuu sovelluksiin, joissa useat agentit voivat siirtää tehtäviä toisilleen.

Tyypillisiä käyttötapauksia ovat asiakastuki, tehtävien hallinta ja työnkulun automaatio.

Tässä mallissa jokainen agentti edustaa tehtävää tai vaihetta työnkulussa, ja agentit voivat siirtää tehtäviä eteenpäin ennalta määriteltyjen sääntöjen mukaisesti.

![Tehtävien siirto](../../../translated_images/fi/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Yhteistyö suodatus

Tämä malli soveltuu sovelluksiin, joissa useat agentit tekevät yhteistyötä käyttäjille tehtävien suositusten tekemisessä.

Miksi haluamme useiden agenttien tekevän yhteistyötä? Koska jokaisella agentilla voi olla erilainen asiantuntijuus, ja he voivat osallistua suositusprosessiin eri tavoilla.

Otetaan esimerkki, jossa käyttäjä haluaa suosituksen parhaasta osakkeesta osakemarkkinoilla.

- **Toimiala-asiantuntija**: Yksi agentti voi olla asiantuntija tietyllä toimialalla.
- **Tekninen analyysi**: Toinen agentti voi olla asiantuntija teknisessä analyysissä.
- **Perusanalyysi**: Kolmas agentti voi olla asiantuntija perusanalyysissä. Näiden agenttien yhteistyöllä käyttäjälle voidaan tarjota kattavampi suositus.

![Suositus](../../../translated_images/fi/multi-agent-filtering.d959cb129dc9f608.webp)

## Tapaus: Hyvityksen käsittelyprosessi

Kuvitellaan tilanne, jossa asiakas pyrkii saamaan hyvitystä tuotteesta. Tässä prosessissa voi olla mukana useita agentteja, mutta jaetaan ne prosessiin erikoistuneisiin agenteihin ja yleisiin agenteihin, joita voidaan käyttää muuallakin liiketoiminnassa.

**Hyvitykseen erikoistuneet agentit**:

Seuraavat agentit voivat olla osallisina hyvitysprosessissa:

- **Asiakasagentti**: Edustaa asiakasta ja vastaa hyvitysprosessin aloittamisesta.
- **Myyjäagentti**: Edustaa myyjää ja vastaa hyvityksen käsittelystä.
- **Maksuagentti**: Vastaa asiakkaan maksun hyvittämisestä.
- **Ratkaisijaagentti**: Vastaa prosessin aikana mahdollisesti ilmenneiden ongelmien ratkaisemisesta.
- **Sääntöjen noudattamisen agentti**: Vastaa siitä, että hyvitysprosessi noudattaa sääntöjä ja politiikkoja.

**Yleiset agentit**:

Näitä agentteja voidaan käyttää yrityksen muissa osissa.

- **Toimitusagentti**: Vastaa tuotteen palauttamisesta myyjälle. Tätä agenttia voi käyttää sekä hyvitysprosessissa että yleisessä tuotteiden toimituksessa esimerkiksi ostotapahtuman yhteydessä.
- **Palautteenantaja-agentti**: Vastaa asiakkaan palautteen keräämisestä. Palaute voidaan ottaa vastaan milloin tahansa, ei pelkästään hyvitysprosessin aikana.
- **Eskalointiagentti**: Vastaa ongelmien eskaloinnista korkeammalle tukitasolle. Tätä agenttia voi käyttää missä tahansa prosessissa, jossa ongelmia tarvitsee eskaloida.
- **Ilmoitusagentti**: Vastaa ilmoitusten lähettämisestä asiakkaalle hyvitysprosessin eri vaiheissa.
- **Analytiikka-agentti**: Vastaa hyvitysprosessiin liittyvän datan analysoinnista.
- **Auditointiantti**: Vastaa hyvitysprosessin tarkastamisesta ja varmistaa, että se toteutetaan oikein.
- **Raportointiagentti**: Vastaa hyvitysprosessista tehtävien raporttien laatimisesta.
- **Tietoagentti**: Vastaa hyvitysprosessia koskevan tietämyksen ylläpidosta. Tämä agentti voi tuntea sekä hyvitykset että yrityksen muut osa-alueet.
- **Turva-agentti**: Vastaa hyvitysprosessin tietoturvasta.
- **Laatuagentti**: Vastaa siitä, että hyvitysprosessi täyttää laatuvaatimukset.

Edellä on lueteltu melko paljon agentteja sekä hyvitysprosessiin erikoistuneita että yleisiä agentteja, joita voidaan käyttää liiketoiminnan eri osissa. Toivottavasti tämä antaa sinulle käsityksen siitä, miten voit valita agentit moni-agenttijärjestelmääsi.

## Tehtävä

Suunnittele moni-agenttijärjestelmä asiakastukiprosessille. Tunnista prosessiin liittyvät agentit, heidän roolinsa ja vastuunsa sekä miten he ovat vuorovaikutuksessa keskenään. Huomioi sekä asiakastukiprosessiin erikoistuneet agentit että yleiset agentit, joita voidaan käyttää yrityksesi muissa osissa.
> Mieti hetki ennen kuin luet seuraavan ratkaisun, saatat tarvita enemmän agentteja kuin uskotkaan.

> VINKKI: Pohdi asiakastukiprosessin eri vaiheita ja ota myös huomioon järjestelmää varten tarvittavat agentit.

## Ratkaisu

[Ratkaisu](./solution/solution.md)

## Tietämyksen tarkistukset

Kysymys: Milloin sinun tulisi harkita monen agentin käyttöä?

- [ ] A1: Kun sinulla on pieni työkuorma ja yksinkertainen tehtävä.
- [ ] A2: Kun sinulla on suuri työkuorma
- [ ] A3: Kun sinulla on yksinkertainen tehtävä.

[Ratkaisukysely](./solution/solution-quiz.md)

## Yhteenveto

Tässä oppitunnissa olemme tarkastelleet monen agentin suunnittelukaavaa, mukaan lukien tilanteet, joissa monien agenttien käyttö on sovellettavissa, monien agenttien käytön edut yhden agentin sijaan, monen agentin suunnittelukaavan toteuttamisen rakennuspalikat sekä miten saada näkyvyyttä siihen, miten useat agentit ovat vuorovaikutuksessa keskenään.

### Onko sinulla lisää kysymyksiä monen agentin suunnittelukaavasta?

Liity [Microsoft Foundry Discordiin](https://aka.ms/ai-agents/discord) tapaamaan muita oppijoita, osallistumaan työaikoihin ja saamaan vastauksia tekoälyagenttien kysymyksiisi.

## Lisäresurssit

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework -dokumentaatio</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Agenttisuunnittelumallit</a>

## Edellinen oppitunti

[Suunnittelun suunnittelu](../07-planning-design/README.md)

## Seuraava oppitunti

[Metakognitio tekoälyagenteissa](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty tekoälypohjaisella käännöspalvelulla [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, ota huomioon, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ota vastuuta tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->