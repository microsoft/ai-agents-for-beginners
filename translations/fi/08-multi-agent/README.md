[![Moni-agenttinen suunnittelumalli](../../../translated_images/fi/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Napsauta yllä olevaa kuvaa katsoaksesi tämän oppitunnin videon)_

# Moni-agenttiset suunnittelumallit

Heti kun aloitat työskentelyn projektissa, joka sisältää useita agenteja, sinun täytyy ottaa huomioon moni-agenttinen suunnittelumalli. Kuitenkin ei välttämättä ole heti selvää, milloin siirtyä moni-agentteihin ja mitkä ovat edut.

## Johdanto

Tässä oppitunnissa pyrimme vastaamaan seuraaviin kysymyksiin:

- Missä tilanteissa moni-agentit ovat sovellettavissa?
- Mitkä ovat edut moni-agenttien käyttämisessä sen sijaan, että yksi yksittäinen agentti hoitaisi useita tehtäviä?
- Mitkä ovat moni-agenttisen suunnittelumallin toteuttamisen rakennuspalikat?
- Miten saamme näkyvyyden siihen, miten useat agentit ovat vuorovaikutuksessa keskenään?

## Oppimistavoitteet

Tämän oppitunnin jälkeen sinun tulisi pystyä:

- Tunnistamaan tilanteet, joissa moni-agentit soveltuvat.
- Tunnustamaan moni-agenttien käytön edut yksittäiseen agenttiin verrattuna.
- Ymmärtämään moni-agenttisen suunnittelumallin toteuttamisen rakennuspalikat.

Mikä on isompi kuva?

*Moni-agentit ovat suunnittelumalli, joka mahdollistaa useiden agenttien työskentelyn yhdessä yhteisen tavoitteen saavuttamiseksi*.

Tätä mallia käytetään laajalti monilla aloilla, kuten robotiikassa, autonomisissa järjestelmissä ja hajautetussa tietojenkäsittelyssä.

## Tilanteet, joissa moni-agentit soveltuvat

Missä tilanteissa moni-agenttien käyttö on hyvä ratkaisu? Vastaus on, että on monia tilanteita, joissa useiden agenttien käyttö on hyödyllistä, erityisesti seuraavissa tapauksissa:

- **Suuret työkuormat**: Suuret työkuormat voidaan jakaa pienemmiksi tehtäviksi ja kohdistaa eri agenteille, mahdollistaen rinnakkaisen käsittelyn ja nopeamman valmistumisen. Esimerkkinä tästä on suuri datankäsittelytehtävä.
- **Monimutkaiset tehtävät**: Monimutkaiset tehtävät, kuten suuret työkuormat, voidaan pilkkoa pienemmiksi osatehtäviksi ja kohdistaa eri agenteille, jotka erikoistuvat tehtävän tietyille osa-alueille. Esimerkkinä tästä ovat autonomiset ajoneuvot, joissa eri agentit hallitsevat navigaatiota, esteiden tunnistusta sekä viestintää muiden ajoneuvojen kanssa.
- **Monipuolinen asiantuntemus**: Eri agenteilla voi olla erilaista asiantuntemusta, joka mahdollistaa tehtävän eri osa-alueiden tehokkaamman hoitamisen kuin yhdellä agentilla. Tähän soveltuu esimerkiksi terveydenhuolto, jossa agentit voivat hallita diagnostiikkaa, hoitosuunnitelmia ja potilaan seurantaa.

## Edut, kun käytetään moni-agentteja verrattuna yhteen agenttiin

Yksittäinen agenttijärjestelmä voi toimia hyvin yksinkertaisissa tehtävissä, mutta monimutkaisemmissa tehtävissä useiden agenttien käyttäminen tarjoaa useita etuja:

- **Erikoistuminen**: Jokainen agentti voi erikoistua tiettyyn tehtävään. Yksittäisen agentin puuttuessa erikoistumista agentti voi hoitaa kaiken, mutta saattaa hämmentyä monimutkaisen tehtävän edessä. Se voi esimerkiksi päätyä suorittamaan tehtävän, johon se ei ole parhaiten soveltuva.
- **Laajennettavuus**: Järjestelmän laajentaminen on helpompaa lisäämällä agentteja kuin lataamalla yksittäistä agenttia liikaa.
- **Virheensietokyky**: Jos yksi agentti epäonnistuu, muut voivat jatkaa toimintaansa varmistaen järjestelmän luotettavuuden.

Otetaan esimerkki: varataan matka käyttäjälle. Yksittäisen agenttijärjestelmän pitäisi hoitaa kaikki matkanvarausprosessin osa-alueet, lennon etsimisestä hotellien ja vuokra-autojen varaamiseen. Yhden agentin saavuttamiseksi sillä pitäisi olla työkaluja kaikkien näiden tehtävien hoitamiseen. Tämä voisi johtaa monimutkaiseen ja monoliittiseen järjestelmään, joka on vaikea ylläpitää ja laajentaa. Toisaalta moni-agenttijärjestelmässä voisi olla eri agentteja, jotka ovat erikoistuneet lentojen löytämiseen, hotellien varaamiseen ja vuokra-autoihin. Tämä tekisi järjestelmästä modulaarisemman, helpommin ylläpidettävän ja laajennettavan.

Vertaa tätä matkatoimistoon, joka toimii paikallisena perheyrityksenä versus matkatoimistoon, joka toimii franchise-toimipisteenä. Paikallisessa yrityksessä yksi agentti hoitaisi kaikki matkanvarauksen osa-alueet, kun taas franchisessa eri agentit hoitaisivat eri osa-alueita.

## Moni-agenttisen suunnittelumallin toteuttamisen rakennuspalikat

Ennen kuin voit toteuttaa moni-agenttisen suunnittelumallin, sinun täytyy ymmärtää mallin rakennuspalikat.

Tehdään tämä konkreettisemmaksi katsomalla uudelleen esimerkkiä matkan varaamisesta käyttäjälle. Tässä tapauksessa rakennuspalikat olisivat:

- **Agenttien välinen viestintä**: Lentoja etsivien agenttien, hotellien ja vuokra-autojen varausten agenttien täytyy kommunikoida ja jakaa tietoa käyttäjän mieltymyksistä ja rajoituksista. Sinun tulee päättää viestinnän protokollat ja menetelmät. Konkreettisesti tämä tarkoittaa, että lentoja etsivän agentin täytyy kommunikoida hotellivarauksen agentin kanssa varmistaakseen, että hotelli on varattu samoille päiville kuin lento. Tämä tarkoittaa, että agenttien täytyy jakaa tietoa käyttäjän matkustuspäivistä, eli sinun pitää päättää *mitkä agentit jakavat tietoa ja miten he jakavat tietoa*.
- **Koordinointimekanismit**: Agenttien täytyy koordinoida toimiaan varmistaakseen, että käyttäjän mieltymykset ja rajoitukset täyttyvät. Käyttäjän mieltymys voisi olla, että hän haluaa hotellin lähellä lentokenttää, kun taas rajoitus voisi olla, että vuokra-autot ovat saatavilla vain lentokentältä. Tämä tarkoittaa, että hotellien varaamisen agentin täytyy tehdä yhteistyötä vuokra-autojen varaamisen agentin kanssa varmistaakseen, että käyttäjän mieltymykset ja rajoitukset täyttyvät. Tällöin sinun tulee päättää *miten agentit koordinoivat toimiaan*.
- **Agenttien arkkitehtuuri**: Agenteilla täytyy olla sisäinen rakenne tehdä päätöksiä ja oppia käyttäjän kanssa käydyistä vuorovaikutuksista. Tämä tarkoittaa, että lentoja etsivän agentin täytyy pystyä tekemään päätöksiä siitä, mitä lentoja suositellaan käyttäjälle. Sinun täytyy päättää *miten agentit tekevät päätöksiä ja oppivat käyttäjän kanssa käydyistä vuorovaikutuksista*. Esimerkkeinä siitä, miten agentti oppii ja paranee, voisi olla, että lentoja etsivä agentti käyttäisi koneoppimismallia suositellakseen lentoja aiempien mieltymysten perusteella.
- **Näkyvyys moni-agenttiseen vuorovaikutukseen**: Sinun täytyy saada näkyvyys siihen, miten useat agentit ovat vuorovaikutuksessa keskenään. Tämä tarkoittaa, että sinulla täytyy olla työkaluja ja tekniikoita agenttien toimintojen ja vuorovaikutusten seuraamiseen. Tämä voi olla lokitus- ja monitorointityökaluja, visualisointityökaluja ja suorituskykymittareita.
- **Moni-agenttiset mallit**: On olemassa erilaisia malleja moni-agenttijärjestelmien toteutukseen, kuten keskitettyjä, hajautettuja ja hybridejä arkkitehtuureja. Sinun täytyy päättää malli, joka parhaiten sopii käyttötarkoitukseesi.
- **Ihminen prosessissa**: Useimmissa tapauksissa mukana on ihminen, ja sinun täytyy ohjeistaa agenteille, milloin pyytää ihmisen väliintuloa. Tämä voi olla esimerkiksi käyttäjä, joka pyytää tiettyä hotellia tai lentoa, jota agentit eivät ole suositelleet, tai pyytää vahvistusta ennen lennon tai hotellin varaamista.

## Näkyvyys moni-agenttiseen vuorovaikutukseen

On tärkeää saada näkyvyys siihen, miten monet agentit ovat vuorovaikutuksessa keskenään. Tämä näkyvyys on oleellinen virheiden korjaamiseksi, optimoinniksi ja koko järjestelmän tehokkuuden varmistamiseksi. Saavuttaaksesi tämän sinun täytyy olla työkaluja ja tekniikoita agenttien toimintojen ja vuorovaikutusten seuraamiseen. Tämä voi olla lokitus- ja monitorointityökaluja, visualisointityökaluja ja suorituskykymittareita.

Esimerkiksi käyttäjän matkan varaamisen tapauksessa sinulla voisi olla hallintapaneeli, joka näyttää kunkin agentin tilan, käyttäjän mieltymykset ja rajoitukset sekä agenttien väliset vuorovaikutukset. Tämä hallintapaneeli voisi näyttää käyttäjän matkustuspäivät, lentoagentin suosittelemat lennot, hotelliagentin suosittelemat hotellit ja vuokra-autojen agentin suosittelemat autot. Tämä antaisi selkeän kuvan siitä, miten agentit ovat vuorovaikutuksessa ja täyttyvätkö käyttäjän mieltymykset ja rajoitukset.

Katsotaan kutakin näistä osa-alueista tarkemmin.

- **Lokitus- ja monitorointityökalut**: Haluat kirjata ylös jokaisen agentin suorittaman toimenpiteen. Lokimerkintä voisi sisältää tiedon agentista, joka suoritti toimenpiteen, tehdystä toimenpiteestä, ajankohdasta ja tuloksesta. Näitä tietoja voidaan käyttää virheiden korjaukseen, optimointiin ja muuhun.

- **Visualisointityökalut**: Visualisointityökalut voivat auttaa näkemään agenttien väliset vuorovaikutukset intuitiivisemmin. Esimerkiksi voitaisiin käyttää kaaviota, joka näyttää tiedon kulun agenttien välillä. Tämä voi auttaa tunnistamaan pullonkauloja, tehottomuuksia ja muita järjestelmän ongelmia.

- **Suorituskykymittarit**: Suorituskykymittarit voivat auttaa seuraamaan moni-agenttijärjestelmän tehokkuutta. Esimerkiksi voit seurata tehtävän suoritusajan, tehtävien määrän aikayksikköä kohti ja agenttien antamien suositusten tarkkuutta. Nämä tiedot voivat auttaa löytämään parannuskohteita ja optimoimaan järjestelmää.

## Moni-agenttiset mallit

Sukelletaan konkreettisiin malleihin, joita voimme käyttää moni-agenttisovellusten luomiseen. Tässä muutamia mielenkiintoisia malleja harkittavaksi:

### Ryhmäkeskustelu

Tämä malli on hyödyllinen, kun haluat luoda ryhmäkeskustelusovelluksen, jossa useat agentit voivat kommunikoida keskenään. Tyypillisiä käyttötapauksia ovat tiimityöskentely, asiakastuki ja sosiaalinen verkostoituminen.

Tässä mallissa kukin agentti edustaa käyttäjää ryhmäkeskustelussa, ja viestejä vaihdetaan agenttien välillä viestintäprotokollaa käyttäen. Agentit voivat lähettää viestejä ryhmäkeskusteluun, vastaanottaa viestejä ryhmäkeskustelusta ja vastata muiden agenttien viesteihin.

Tämä malli voidaan toteuttaa käyttämällä keskitettyä arkkitehtuuria, jossa kaikki viestit kulkevat keskuspalvelimen kautta, tai hajautettua arkkitehtuuria, jossa viestit vaihdetaan suoraan.

![Ryhmäkeskustelu](../../../translated_images/fi/multi-agent-group-chat.ec10f4cde556babd.webp)

### Tehtävien välitys

Tämä malli on hyödyllinen, kun haluat luoda sovelluksen, jossa useat agentit voivat siirtää tehtäviä toisilleen.

Tyypillisiä käyttötapauksia ovat asiakastuki, tehtävien hallinta ja työnkulun automatisointi.

Tässä mallissa kukin agentti edustaa tehtävää tai työvaihetta, ja agentit voivat siirtää tehtäviä muille agentille ennalta määrättyjen sääntöjen mukaan.

![Tehtävän välitys](../../../translated_images/fi/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Yhteistyö suodatus

Tämä malli on hyödyllinen, kun haluat luoda sovelluksen, jossa useat agentit voivat tehdä yhteistyötä suositusten antamiseksi käyttäjille.

Syynä moni-agenttien yhteistyöhön on se, että jokaisella agentilla voi olla erilainen asiantuntemus ja ne voivat osallistua suositusprosessiin eri tavoin.

Otetaan esimerkki, jossa käyttäjä haluaa suosituksen parhaasta osakkeesta ostettavaksi pörssissä.

- **Alan asiantuntija**: Yksi agentti voisi olla asiantuntija tietyllä alalla.
- **Tekninen analyysi**: Toinen agentti voisi olla asiantuntija teknisessä analyysissä.
- **Perusanalyysi**: ja kolmas agentti voisi olla asiantuntija perusanalyysissä. Yhteistyöllä nämä agentit voivat tarjota käyttäjälle kattavamman suosituksen.

![Suositus](../../../translated_images/fi/multi-agent-filtering.d959cb129dc9f608.webp)

## Tilanne: Hyvityksen käsittelyprosessi

Kuvitellaan tilanne, jossa asiakas yrittää saada hyvitystä tuotteesta. Tässä prosessissa voi olla mukana useita agenteja, mutta jaetaan ne prosessikohtaisiin agenteihin ja yleisiin agenteihin, joita voidaan käyttää muissa prosesseissa.

**Hyvityksiä koskevat agentit**:

Seuraavat agentit voisivat olla mukana hyvitysprosessissa:

- **Asiakasta edustava agentti**: Tämä agentti edustaa asiakasta ja on vastuussa hyvitysprosessin aloittamisesta.
- **Myyjää edustava agentti**: Tämä agentti edustaa myyjää ja vastaa hyvityksen käsittelystä.
- **Maksuagentti**: Tämä agentti edustaa maksuprosessia ja vastaa asiakkaan maksun hyvittämisestä.
- **Ratkaisuprosessin agentti**: Tämä agentti edustaa ratkaisuprosessia ja vastaa kaikista hyvitysprosessin aikana ilmenneistä ongelmista.
- **Sääntöjen noudattamista valvova agentti**: Tämä agentti edustaa sääntöjen noudattamista ja varmistaa, että hyvitysprosessi noudattaa määräyksiä ja käytäntöjä.

**Yleiset agentit**:

Näitä agenteja voidaan käyttää muissa liiketoiminnan osissa.

- **Toimitusagentti**: Tämä agentti edustaa toimitusprosessia ja vastaa tuotteen lähettämisestä myyjälle. Tätä agenttia voidaan käyttää sekä hyvitysprosessissa että tuotteiden yleisessä toimituksessa esimerkiksi ostosten yhteydessä.
- **Palautteenantaja-agentti**: Tämä agentti edustaa palautetoimintoa ja vastaa asiakkaan palautteiden keräämisestä. Palautetta voidaan antaa milloin tahansa, ei pelkästään hyvitysprosessin aikana.
- **Eskalaatioagentti**: Tämä agentti edustaa eskalaatioprosessia ja vastaa ongelmien viemisestä korkeammalle tukitasolle. Tällaisen agentin voi käyttää missä tahansa prosessissa, jossa ongelmia täytyy eskaloida.
- **Ilmoitusagentti**: Tämä agentti edustaa ilmoitusprosessia ja vastaa ilmoitusten lähettämisestä asiakkaalle hyvitysprosessin eri vaiheissa.
- **Analytiikka-agentti**: Tämä agentti edustaa analytiikkaprosessia ja analysoi hyvitysprosessiin liittyvää dataa.
- **Auditointiagentti**: Tämä agentti edustaa auditointiprosessia ja vastaa hyvitysprosessin tarkastamisesta oikeellisuuden varmistamiseksi.
- **Raportointiantti**: Tämä agentti edustaa raportointiprosessia ja vastaa hyvitysprosessin raporttien tuottamisesta.
- **Tietämyksenantti**: Tämä agentti edustaa tietämyspohjaa ja vastaa hyvitysprosessiin liittyvän tiedon ylläpidosta. Tämä agentti voisi olla asiantunteva sekä hyvitysten että muiden liiketoiminnan osa-alueiden suhteen.
- **Turva-agentti**: Tämä agentti edustaa turvallisuusprosessia ja varmistaa hyvitysprosessin turvallisuuden.
- **Laatuagentti**: Tämä agentti edustaa laatuprosessia ja vastaa hyvitysprosessin laadun varmistamisesta.

Aiemmin lueteltiin melko monta agenttia, sekä hyvitysprosessille että yleisille agenteille, joita voidaan käyttää liiketoiminnan muissa osissa. Toivottavasti tämä antaa sinulle kuvan siitä, miten voit päättää, mitä agentteja käyttää moni-agenttijärjestelmässäsi.

## Tehtävä

Suunnittele moni-agenttijärjestelmä asiakastukiprosessille. Tunnista prosessissa mukana olevat agentit, niiden roolit ja vastuut sekä miten ne ovat vuorovaikutuksessa keskenään. Ota huomioon sekä asiakastukeen erityisesti liittyvät agentit että yleiset agentit, joita voidaan käyttää liiketoimintasi muissa osissa.


> Mieti hetki ennen kuin luet seuraavan ratkaisun, saatat tarvita enemmän agenteja kuin luulet.

> VINKKI: Mieti asiakastuen eri vaiheita ja ota myös huomioon minkä tahansa järjestelmän tarvitsemat agentit.

## Ratkaisu

[Ratkaisu](./solution/solution.md)

## Tietojen tarkistus

### Kysymys 1

Mikä tilanne sopii parhaiten monen agentin järjestelmälle?

- [ ] A1: Tukibotti vastaa yleisiin kysymyksiin käyttäen yhtä tietokantaa ja pientä työkalusarjaa.
- [ ] A2: Hyvityskäsittelyprosessi vaatii erilliset petosten, maksujen ja vaatimustenmukaisuuden roolit, joilla kaikilla on omat työkalunsa, ja tulokset on koordinoitava.
- [ ] A3: Sama yksinkertainen luokituspyyntö saapuu tuhansia kertoja tunnissa.

### Kysymys 2

Milloin yksi agentti on yleensä parempi valinta?

- [ ] A1: Tehtävä voidaan hoitaa yhdellä ohje- ja työkalusarjalla ilman erikoisvaihtoja.
- [ ] A2: Agentilla on käytössään enemmän kuin yksi työkalu.
- [ ] A3: Työnkulku vaatii erilliset roolit eri käyttöoikeuksilla ja itsenäisillä tarkastuspoluilla.

[Ratkaisun testi](./solution/solution-quiz.md)

## Yhteenveto

Tässä oppitunnissa olemme tarkastelleet monen agentin suunnittelumallia, mukaan lukien tilanteet, joissa monen agentin käyttö on tarkoituksenmukaista, monen agentin etuja verrattuna yksittäiseen agenttiin, monen agentin mallin toteuttamisen rakennuspalikat sekä miten saada näkyvyyttä agenttien väliseen vuorovaikutukseen.

### Onko sinulla lisää kysymyksiä monen agentin suunnittelumallista?

Liity [Microsoft Foundry Discordiin](https://discord.com/invite/ATgtXmAS5D) tavata muita oppijoita, osallistua toimistoaikoihin ja saada vastauksia AI-agentteja koskeviin kysymyksiisi.

## Lisäresurssit

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework dokumentaatio</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Agenttisuunnittelumallit</a>


## Edellinen oppitunti

[Suunnittelun suunnittelu](../07-planning-design/README.md)

## Seuraava oppitunti

[Metakognitio AI-agenteissa](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->