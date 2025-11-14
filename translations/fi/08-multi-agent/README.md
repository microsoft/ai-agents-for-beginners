<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a008c204051cba8d0e253b75f261c41",
  "translation_date": "2025-08-29T17:11:08+00:00",
  "source_file": "08-multi-agent/README.md",
  "language_code": "fi"
}
-->
[![Multi-Agent Design](../../../translated_images/lesson-8-thumbnail.278a3e4a59137d625df92de3f885d2da2a92b1f7017abba25a99fb25edd83a55.fi.png)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Klikkaa yllä olevaa kuvaa nähdäksesi tämän oppitunnin videon)_

# Moniagenttiset suunnittelumallit

Heti kun alat työskennellä projektin parissa, joka sisältää useita agentteja, sinun on otettava huomioon moniagenttinen suunnittelumalli. Kuitenkin voi olla aluksi epäselvää, milloin siirtyä moniagenttiseen malliin ja mitkä sen edut ovat.

## Johdanto

Tässä oppitunnissa pyrimme vastaamaan seuraaviin kysymyksiin:

- Millaisissa tilanteissa moniagenttinen malli on sovellettavissa?
- Mitkä ovat moniagenttisen mallin edut verrattuna yhteen agenttiin, joka suorittaa useita tehtäviä?
- Mitkä ovat moniagenttisen suunnittelumallin toteutuksen rakennuspalikat?
- Miten voimme seurata, kuinka useat agentit ovat vuorovaikutuksessa keskenään?

## Oppimistavoitteet

Tämän oppitunnin jälkeen sinun pitäisi pystyä:

- Tunnistamaan tilanteet, joissa moniagenttinen malli on sovellettavissa.
- Ymmärtämään moniagenttisen mallin edut verrattuna yksittäiseen agenttiin.
- Käsittämään moniagenttisen suunnittelumallin toteutuksen rakennuspalikat.

Mikä on suurempi kokonaiskuva?

*Moniagenttinen malli on suunnittelumalli, joka mahdollistaa useiden agenttien yhteistyön yhteisen tavoitteen saavuttamiseksi.*

Tätä mallia käytetään laajasti eri aloilla, kuten robotiikassa, autonomisissa järjestelmissä ja hajautetussa laskennassa.

## Tilanteet, joissa moniagenttinen malli on sovellettavissa

Millaisissa tilanteissa moniagenttinen malli on hyödyllinen? Vastaus on, että moniagenttista mallia voidaan hyödyntää monissa tilanteissa, erityisesti seuraavissa tapauksissa:

- **Suuret työmäärät**: Suuret työmäärät voidaan jakaa pienempiin tehtäviin ja osoittaa eri agenteille, mikä mahdollistaa rinnakkaisen käsittelyn ja nopeamman valmistumisen. Esimerkkinä tästä on suuri datankäsittelytehtävä.
- **Monimutkaiset tehtävät**: Monimutkaiset tehtävät, kuten suuret työmäärät, voidaan jakaa pienempiin osatehtäviin ja osoittaa eri agenteille, joista kukin erikoistuu tiettyyn tehtävän osa-alueeseen. Hyvä esimerkki tästä on autonomiset ajoneuvot, joissa eri agentit hallitsevat navigointia, esteiden havaitsemista ja viestintää muiden ajoneuvojen kanssa.
- **Monipuolinen asiantuntemus**: Eri agenteilla voi olla monipuolista asiantuntemusta, mikä mahdollistaa tehtävän eri osa-alueiden tehokkaamman käsittelyn kuin yksittäinen agentti. Esimerkkinä tästä on terveydenhuolto, jossa agentit voivat hallita diagnostiikkaa, hoitosuunnitelmia ja potilaan seurantaa.

## Moniagenttisen mallin edut verrattuna yksittäiseen agenttiin

Yksittäinen agenttijärjestelmä voi toimia hyvin yksinkertaisissa tehtävissä, mutta monimutkaisemmissa tehtävissä moniagenttinen malli tarjoaa useita etuja:

- **Erikoistuminen**: Jokainen agentti voi erikoistua tiettyyn tehtävään. Yksittäisen agentin erikoistumisen puute tarkoittaa, että agentti voi tehdä kaikkea, mutta saattaa hämmentyä monimutkaisen tehtävän edessä. Se voi esimerkiksi päätyä tekemään tehtävän, johon se ei ole parhaiten soveltuva.
- **Skalautuvuus**: Järjestelmiä on helpompi laajentaa lisäämällä agentteja kuin ylikuormittamalla yhtä agenttia.
- **Vikasietoisuus**: Jos yksi agentti epäonnistuu, muut voivat jatkaa toimintaansa, mikä varmistaa järjestelmän luotettavuuden.

Otetaan esimerkki: varataan matka käyttäjälle. Yksittäinen agenttijärjestelmä joutuisi käsittelemään kaikki matkanvarausprosessin osa-alueet, kuten lentojen etsimisen, hotellien varaamisen ja vuokra-autojen varaamisen. Tämän saavuttamiseksi yksittäisellä agentilla pitäisi olla työkalut kaikkien näiden tehtävien hoitamiseen. Tämä voisi johtaa monimutkaiseen ja monoliittiseen järjestelmään, jota on vaikea ylläpitää ja laajentaa. Moniagenttinen järjestelmä sen sijaan voisi sisältää eri agentteja, jotka erikoistuvat lentojen etsimiseen, hotellien varaamiseen ja vuokra-autoihin. Tämä tekisi järjestelmästä modulaarisemman, helpommin ylläpidettävän ja skaalautuvan.

Vertaa tätä pieneen perheyrityksenä toimivaan matkatoimistoon ja franchising-mallilla toimivaan matkatoimistoon. Perheyrityksessä yksi agentti hoitaisi kaikki matkanvarausprosessin osa-alueet, kun taas franchising-mallissa eri agentit hoitaisivat eri osa-alueet.

## Moniagenttisen suunnittelumallin toteutuksen rakennuspalikat

Ennen kuin voit toteuttaa moniagenttisen suunnittelumallin, sinun on ymmärrettävä mallin rakennuspalikat.

Tehdään tämä konkreettisemmaksi tarkastelemalla jälleen esimerkkiä käyttäjän matkan varaamisesta. Tässä tapauksessa rakennuspalikat sisältäisivät:

- **Agenttien välinen viestintä**: Lentojen etsimiseen, hotellien varaamiseen ja vuokra-autoihin erikoistuneiden agenttien on kommunikoitava ja jaettava tietoa käyttäjän mieltymyksistä ja rajoitteista. Sinun on päätettävä viestinnän protokollat ja menetelmät. Tämä tarkoittaa konkreettisesti sitä, että lentojen etsintään erikoistuneen agentin on kommunikoitava hotellien varaamiseen erikoistuneen agentin kanssa varmistaakseen, että hotelli varataan samoille päiville kuin lento. Tämä tarkoittaa, että agenttien on jaettava tietoa käyttäjän matkustuspäivistä, mikä tarkoittaa, että sinun on päätettävä *mitkä agentit jakavat tietoa ja miten he jakavat tietoa*.
- **Koordinointimekanismit**: Agenttien on koordinoitava toimiaan varmistaakseen, että käyttäjän mieltymykset ja rajoitteet täyttyvät. Käyttäjän mieltymys voisi olla, että hän haluaa hotellin lähellä lentokenttää, kun taas rajoite voisi olla, että vuokra-autoja on saatavilla vain lentokentällä. Tämä tarkoittaa, että hotellien varaamiseen erikoistuneen agentin on koordinoitava vuokra-autojen varaamiseen erikoistuneen agentin kanssa varmistaakseen, että käyttäjän mieltymykset ja rajoitteet täyttyvät. Tämä tarkoittaa, että sinun on päätettävä *miten agentit koordinoivat toimiaan*.
- **Agenttien arkkitehtuuri**: Agenttien on oltava sisäisesti rakenteeltaan sellaisia, että ne voivat tehdä päätöksiä ja oppia vuorovaikutuksestaan käyttäjän kanssa. Tämä tarkoittaa, että lentojen etsintään erikoistuneen agentin on oltava sisäisesti rakenteeltaan sellainen, että se voi tehdä päätöksiä siitä, mitä lentoja suositella käyttäjälle. Tämä tarkoittaa, että sinun on päätettävä *miten agentit tekevät päätöksiä ja oppivat vuorovaikutuksestaan käyttäjän kanssa*. Esimerkkejä siitä, miten agentti oppii ja parantaa toimintaansa, voisi olla, että lentojen etsintään erikoistunut agentti käyttää koneoppimismallia suositellakseen lentoja käyttäjälle hänen aiempien mieltymystensä perusteella.
- **Näkyvyys moniagenttiseen vuorovaikutukseen**: Sinun on oltava näkyvyys siihen, miten useat agentit ovat vuorovaikutuksessa keskenään. Tämä tarkoittaa, että sinulla on oltava työkaluja ja tekniikoita agenttien toiminnan ja vuorovaikutuksen seuraamiseen. Tämä voisi olla esimerkiksi lokitus- ja seurantatyökaluja, visualisointityökaluja ja suorituskykymittareita.
- **Moniagenttiset mallit**: Moniagenttisten järjestelmien toteuttamiseen on olemassa erilaisia malleja, kuten keskitetyt, hajautetut ja hybridimallit. Sinun on päätettävä, mikä malli sopii parhaiten käyttötapaukseesi.
- **Ihmisen osallistuminen**: Useimmissa tapauksissa mukana on ihminen, ja sinun on ohjeistettava agentteja, milloin pyytää ihmisen väliintuloa. Tämä voisi olla esimerkiksi käyttäjän pyytäessä tiettyä hotellia tai lentoa, jota agentit eivät ole suositelleet, tai pyytäessä vahvistusta ennen lennon tai hotellin varaamista.

## Näkyvyys moniagenttiseen vuorovaikutukseen

On tärkeää, että sinulla on näkyvyys siihen, miten useat agentit ovat vuorovaikutuksessa keskenään. Tämä näkyvyys on olennaista virheiden korjaamisessa, optimoinnissa ja järjestelmän kokonaistehokkuuden varmistamisessa. Tämän saavuttamiseksi sinulla on oltava työkaluja ja tekniikoita agenttien toiminnan ja vuorovaikutuksen seuraamiseen. Tämä voisi olla esimerkiksi lokitus- ja seurantatyökaluja, visualisointityökaluja ja suorituskykymittareita.

Esimerkiksi käyttäjän matkan varaamisen tapauksessa sinulla voisi olla hallintapaneeli, joka näyttää kunkin agentin tilan, käyttäjän mieltymykset ja rajoitteet sekä agenttien väliset vuorovaikutukset. Tämä hallintapaneeli voisi näyttää käyttäjän matkustuspäivät, lentojen etsintään erikoistuneen agentin suositukset, hotellien varaamiseen erikoistuneen agentin suositukset ja vuokra-autojen varaamiseen erikoistuneen agentin suositukset. Tämä antaisi sinulle selkeän kuvan siitä, miten agentit ovat vuorovaikutuksessa keskenään ja täyttyvätkö käyttäjän mieltymykset ja rajoitteet.

Tarkastellaan kutakin näistä näkökohdista tarkemmin.

- **Lokitus- ja seurantatyökalut**: Haluat, että jokainen agentin suorittama toiminto kirjataan. Lokimerkintä voisi sisältää tietoa toiminnon suorittaneesta agentista, suoritetusta toiminnosta, toiminnon suorittamisen ajankohdasta ja toiminnon lopputuloksesta. Tätä tietoa voidaan sitten käyttää virheiden korjaamiseen, optimointiin ja muuhun.
- **Visualisointityökalut**: Visualisointityökalut voivat auttaa sinua näkemään agenttien väliset vuorovaikutukset intuitiivisemmalla tavalla. Esimerkiksi sinulla voisi olla kaavio, joka näyttää tiedon kulun agenttien välillä. Tämä voisi auttaa tunnistamaan pullonkauloja, tehottomuuksia ja muita järjestelmän ongelmia.
- **Suorituskykymittarit**: Suorituskykymittarit voivat auttaa sinua seuraamaan moniagenttisen järjestelmän tehokkuutta. Esimerkiksi voit seurata tehtävän suorittamiseen kulunutta aikaa, suoritetujen tehtävien määrää aikayksikköä kohden ja agenttien antamien suositusten tarkkuutta. Tämä tieto voi auttaa sinua tunnistamaan parannuskohteita ja optimoimaan järjestelmää.

## Moniagenttiset mallit

Tarkastellaan joitakin konkreettisia malleja, joita voimme käyttää moniagenttisten sovellusten luomiseen. Tässä muutamia kiinnostavia malleja, joita kannattaa harkita:

### Ryhmäkeskustelu

Tämä malli on hyödyllinen, kun haluat luoda ryhmäkeskustelusovelluksen, jossa useat agentit voivat kommunikoida keskenään. Tyypillisiä käyttötapauksia tälle mallille ovat tiimiyhteistyö, asiakastuki ja sosiaalinen verkostoituminen.

Tässä mallissa jokainen agentti edustaa käyttäjää ryhmäkeskustelussa, ja viestejä vaihdetaan agenttien välillä viestintäprotokollan avulla. Agentit voivat lähettää viestejä ryhmäkeskusteluun, vastaanottaa viestejä ryhmäkeskustelusta ja vastata muiden agenttien viesteihin.

Tämä malli voidaan toteuttaa käyttämällä keskitettyä arkkitehtuuria, jossa kaikki viestit reititetään keskitetyn palvelimen kautta, tai hajautettua arkkitehtuuria, jossa viestit vaihdetaan suoraan.

![Ryhmäkeskustelu](../../../translated_images/multi-agent-group-chat.ec10f4cde556babd7b450fd01e1a0fac1f9788c27d3b9e54029377bb1bdd1db6.fi.png)

### Tehtävän siirto

Tämä malli on hyödyllinen, kun haluat luoda sovelluksen, jossa useat agentit voivat siirtää tehtäviä toisilleen.

Tyypillisiä käyttötapauksia tälle mallille ovat asiakastuki, tehtävien hallinta ja työnkulun automatisointi.

Tässä mallissa jokainen agentti edustaa tehtävää tai työnkulun vaihetta, ja agentit voivat siirtää tehtäviä toisilleen ennalta määriteltyjen sääntöjen perusteella.

![Tehtävän siirto](../../../translated_images/multi-agent-hand-off.4c5fb00ba6f8750a0754bf29d49fa19d578080c61da40416df84d866bcdd87a3.fi.png)

### Yhteistyöhön perustuva suodatus

Tämä malli on hyödyllinen, kun haluat luoda sovelluksen, jossa useat agentit voivat tehdä yhteistyötä suositusten antamiseksi käyttäjille.

Miksi haluaisit useiden agenttien tekevän yhteistyötä? Koska jokaisella agentilla voi olla eri asiantuntemusta ja he voivat osallistua suositusprosessiin eri tavoin.

Otetaan esimerkki, jossa käyttäjä haluaa suosituksen parhaasta osakkeesta ostettavaksi osakemarkkinoilla.

- **Toimialan asiantuntija**: Yksi agentti voisi olla asiantuntija tietyllä toimialalla.
- **Tekninen analyysi**: Toinen agentti voisi olla asiantuntija teknisessä analyysissä.
- **Perusanalyysi**: Ja kolmas agentti voisi olla asiantuntija perusanalyysissä. Yhteistyön avulla nämä agentit voivat antaa käyttäjälle kattavamman suosituksen.

![Suositus](../../../translated_images/multi-agent-filtering.d959cb129dc9f60826916f0f12fe7a8339b532f5f236860afb8f16b63ea10dc2.fi.png)

## Tilanne: Hyvitysprosessi

Tarkastellaan tilannetta, jossa asiakas yrittää saada hyvitystä tuotteesta. Prosessissa voi olla mukana useita agentteja, mutta jaetaan ne hyvitysprosessiin erikoistuneisiin agenteihin ja yleisiin agenteihin, joita voidaan käyttää muissa prosesseissa.

**Hyvitysprosessiin erikoistuneet agentit**:

Seuraavat agentit voisivat olla mukana hyvitysprosessissa:

- **Asiakasagentti**: Tämä agentti edustaa asiakasta ja on vastuussa hyvitysprosessin aloittamisesta.
- **Myyjäagentti**: Tämä agentti edustaa myyjää ja on vastuussa hyvityksen käsittelystä.
- **Maksuagentti**: Tämä agentti edustaa maksuprosessia ja on vastuussa asiakkaan maksun hyvittämisestä.
- **Ratkaisuagentti**: Tämä agentti edustaa ratkaisuprosessia ja on vastuussa mahdollisten ongelmien ratkaisemisesta hyvitysprosessin aikana.
- **Sääntöjenmukaisuusagentti**: Tämä agentti edustaa sääntöjenmukaisuusprosessia ja on vastuussa siitä, että hyvitysprosessi noudattaa säädöksiä ja käytäntöjä.

**Yleiset agentit**:

Nämä agentit voivat olla käytössä muilla liiketoiminnan osa-alueilla.

- **Kuljetusagentti**: Tämä agentti edustaa kuljetusprosessia ja on vastuussa tuotteen lähettämisestä takaisin myyjälle. Tämä agentti voi olla käytössä sekä hyvitysprosessissa että tuotteen yleisessä kuljetuksessa esimerkiksi ostotilanteessa.
- **Palauteagentti**: Tämä agentti edustaa palautteenkeruuprosessia ja on vastuussa asiakkaan palautteen keräämisestä. Palautetta voidaan kerätä milloin tahansa, ei vain hyvitysprosessin aikana.
- **Eskalaatioagentti**: Tämä agentti edustaa eskalaatioprosessia ja on vastuussa ongelmien eskaloimisesta korkeammalle tukitasolle. Tämän tyyppistä agenttia voidaan käyttää missä tahansa prosessissa, jossa ongelma täytyy eskaloida.
- **Ilmoitusagentti**: Tämä agentti edustaa ilmoitusprosessia ja on vastuussa ilmoitusten lähettämisestä asiakkaalle hyvitysprosessin eri vaiheissa.
- **Analytiikkaagentti**: Tämä agentti edustaa analytiikkaprosessia ja on vastuussa hyvitysprosessiin liittyvien tietojen analysoinnista.
- **Auditointiagentti**: Tämä agentti edustaa auditointiprosessia ja on vastuussa hyvitysprosessin auditoinnista varmistaakseen, että se toteutetaan oikein.
- **Raportointiagentti**: Tämä agentti edustaa raportointiprosessia ja on vastuussa hyvitysprosessin raporttien luomisesta.
- **Tietoagentti**: Tämä agentti edustaa tietoprosessia ja
Suunnittele monitoimijajärjestelmä asiakastukiprosessia varten. Tunnista prosessiin liittyvät toimijat, heidän roolinsa ja vastuunsa sekä miten he ovat vuorovaikutuksessa keskenään. Ota huomioon sekä asiakastukiprosessiin liittyvät toimijat että yleiset toimijat, joita voidaan käyttää muissa liiketoiminnan osissa.

> Mieti hetki ennen kuin luet seuraavan ratkaisun, saatat tarvita enemmän toimijoita kuin aluksi ajattelet.

> TIP: Mieti asiakastukiprosessin eri vaiheita ja myös toimijoita, joita tarvitaan missä tahansa järjestelmässä.

## Ratkaisu

[Ratkaisu](./solution/solution.md)

## Tietotarkistukset

Kysymys: Milloin kannattaa harkita monitoimijoiden käyttöä?

- [ ] A1: Kun sinulla on pieni työmäärä ja yksinkertainen tehtävä.
- [ ] A2: Kun sinulla on suuri työmäärä.
- [ ] A3: Kun sinulla on yksinkertainen tehtävä.

[Ratkaisun tietovisa](./solution/solution-quiz.md)

## Yhteenveto

Tässä oppitunnissa olemme tarkastelleet monitoimijasuunnittelumallia, mukaan lukien tilanteet, joissa monitoimijat ovat soveltuvia, monitoimijoiden käytön edut verrattuna yksittäiseen toimijaan, monitoimijasuunnittelumallin toteutuksen rakennuspalikat sekä miten saada näkyvyyttä siihen, miten useat toimijat ovat vuorovaikutuksessa keskenään.

### Onko sinulla lisää kysymyksiä monitoimijasuunnittelumallista?

Liity [Azure AI Foundry Discordiin](https://aka.ms/ai-agents/discord) tavataksesi muita oppijoita, osallistuaksesi toimistotunteihin ja saadaksesi vastauksia AI-toimijoihin liittyviin kysymyksiisi.

## Lisäresurssit

## Edellinen oppitunti

[Suunnittelun suunnittelu](../07-planning-design/README.md)

## Seuraava oppitunti

[Metakognitio AI-toimijoissa](../09-metacognition/README.md)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskääntämistä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinkäsityksistä tai virhetulkinnoista.