# Kontekstisuunnittelu tekoälyagentteja varten

[![Context Engineering](../../../translated_images/fi/lesson-12-thumbnail.ed19c94463e774d4.webp)](https://youtu.be/F5zqRV7gEag)

> _(Napsauta yllä olevaa kuvaa nähdäksesi tämän oppitunnin videon)_

On tärkeää ymmärtää sen sovelluksen monimutkaisuus, jota varten rakennat tekoälyagenttia, jotta voit tehdä siitä luotettavan. Meidän täytyy rakentaa tekoälyagentteja, jotka hallitsevat tehokkaasti tietoa monimutkaisten tarpeiden ratkaisemiseksi pelkän kehotteiden suunnittelun sijaan.

Tässä oppitunnissa tarkastelemme, mitä kontekstisuunnittelu on ja sen roolia tekoälyagenttien rakentamisessa.

## Johdanto

Tämä oppitunti kattaa:

• **Mitä kontekstisuunnittelu on** ja miksi se eroaa kehotteiden suunnittelusta.

• **Strategioita tehokkaaseen kontekstisuunnitteluun**, mukaan lukien kuinka kirjoittaa, valita, pakata ja eristää tietoa.

• **Yleisiä kontekstin virheitä**, jotka voivat saada tekoälyagenttisi raiteiltaan ja kuinka korjata ne.

## Oppimistavoitteet

Oppitunnin suorittamisen jälkeen ymmärrät, miten:

• **Määritellään kontekstisuunnittelu** ja erotetaan se kehotteiden suunnittelusta.

• **Tunnistetaan keskeiset kontekstin osat** suurten kielimallien (LLM) sovelluksissa.

• **Käytetään strategioita kontekstin kirjoittamiseen, valintaan, pakkaukseen ja eristämiseen** agentin suorituskyvyn parantamiseksi.

• **Tunnistetaan yleiset kontekstin virheet** kuten myrkytys, häirintä, sekaannus ja ristiriita, ja toteutetaan lieventämistekniikoita.

## Mitä on kontekstisuunnittelu?

Tekoälyagenteille konteksti ohjaa tekoälyagentin suunnittelua tiettyjen toimien suorittamiseen. Kontekstisuunnittelu on käytäntö varmistaa, että tekoälyagentilla on oikea tieto seuraavan tehtävän vaiheen suorittamiseen. Konteksti-ikkuna on rajallinen kooltaan, joten agentin rakentajina meidän täytyy rakentaa järjestelmiä ja prosesseja tiedon lisäämisen, poistamisen ja tiivistämisen hallitsemiseksi konteksti-ikkunassa.

### Kehote- vs kontekstisuunnittelu

Kehotesuunnittelu keskittyy yhteen staattiseen ohjejoukkoon, jolla ohjataan tekoälyagentteja säännöillä. Kontekstisuunnittelu puolestaan käsittelee dynaamisen tietojoukon hallintaa, mukaan lukien alkuperäinen kehote, jotta tekoälyagentilla on tarpeellinen tieto ajan mittaan. Kontekstisuunnittelun pääidea on tehdä tästä prosessista toistettavaa ja luotettavaa.

### Kontekstin tyypit

[![Types of Context](../../../translated_images/fi/context-types.fc10b8927ee43f06.webp)](https://youtu.be/F5zqRV7gEag)

On tärkeää muistaa, että konteksti ei ole vain yksi asia. Tiedot, joita tekoälyagentti tarvitsee, voivat tulla monista eri lähteistä, ja meidän tehtävämme on varmistaa, että agentilla on pääsy näihin lähteisiin:

Kontekstin tyypit, joita tekoälyagentin täytyy hallita, ovat:

• **Ohjeet:** Nämä ovat kuin agentin "säännöt" – kehotteet, järjestelmäviestit, muutama esimerkkikehote (näyttäen tekoälylle, miten tehdä jotain) ja kuvaus käytettävistä työkaluista. Tämä on kohta, jossa kehotteiden suunnittelu yhdistyy kontekstisuunnitteluun.

• **Tieto:** Kattaa faktat, tietokannoista haetun tiedon tai agentin keräämät pitkäaikaiset muistot. Tämä sisältää myös Retrieval Augmented Generation (RAG) -järjestelmän integroinnin, jos agentin täytyy käyttää erilaisia tietovarastoja ja -tietokantoja.

• **Työkalut:** Ulkoisten toimintojen, rajapintojen (API) ja MCP-palvelimien määrittelyt, joita agentti voi kutsua, sekä niistä saadut palautteet (tulokset).

• **Keskusteluhistoria:** Käyttäjän kanssa käytävä jatkuva vuoropuhelu. Ajan myötä keskustelut pitenevät ja monimutkaistuvat, mikä vie tilaa konteksti-ikkunassa.

• **Käyttäjäasetukset:** Tietoa käyttäjän mieltymyksistä ja inhoista ajan kuluessa. Näitä voidaan tallentaa ja käyttää avainten päätösten tukena käyttäjälle.

## Strategiat tehokkaaseen kontekstisuunnitteluun

### Suunnittelustrategiat

[![Context Engineering Best Practices](../../../translated_images/fi/best-practices.f4170873dc554f58.webp)](https://youtu.be/F5zqRV7gEag)

Hyvä kontekstisuunnittelu alkaa hyvällä suunnittelulla. Tässä on lähestymistapa, joka auttaa sinua alkamaan ajatella, miten soveltaa kontekstisuunnittelun käsitettä:

1. **Määrittele selkeät tulokset** – Tehtävien tulokset, joihin tekoälyagentteja käytetään, tulisi määritellä selkeästi. Vastaa kysymykseen – "Millainen maailma on, kun tekoälyagentti on suorittanut tehtävänsä?" Toisin sanoen, mikä muutos, tieto tai vastaus käyttäjälle pitäisi olla vuorovaikutuksen jälkeen.

2. **Kartoit konteksti** – Kun olet määritellyt tekoälyagentin tulokset, sinun täytyy vastata kysymykseen "Mitä tietoa tekoälyagentti tarvitsee tämän tehtävän suorittamiseen?" Näin voit alkaa kartoittaa, mistä tämä tieto löytyy.

3. **Luo kontekstiputkia** – Nyt kun tiedät, mistä tieto löytyy, sinun täytyy vastata kysymykseen "Miten agentti saa tämän tiedon?" Tämä voidaan tehdä eri tavoin, kuten RAG-järjestelmän, MCP-palvelimien ja muiden työkalujen avulla.

### Käytännön strategiat

Suunnittelu on tärkeää, mutta kun tieto alkaa virrata agentin konteksti-ikkunaan, meillä täytyy olla käytännön strategioita sen hallintaan:

#### Kontekstin hallinta

Vaikka jotkin tiedot lisätään konteksti-ikkunaan automaattisesti, kontekstisuunnittelu tarkoittaa aktiivisempaa roolia tämän tiedon hallinnassa, mikä voidaan tehdä muutamilla strategioilla:

 1. **Agentin muistilehtiö**
 Tämä antaa tekoälyagentille mahdollisuuden tehdä muistiinpanoja ajankohtaiseen tehtävään ja käyttäjän vuorovaikutuksiin yhdellä istunnolla. Muistilehtiön tulisi sijaita konteksti-ikkunan ulkopuolella tiedostossa tai ajonaikaisessa objektissa, jonka agentti voi myöhemmin hakea tämän istunnon aikana tarvittaessa.

 2. **Muistot**
 Muistilehtiöt ovat hyviä tietojen hallintaan yhden istunnon kontekstin ulkopuolella. Muistot mahdollistavat agenttien tallentaa ja hakea relevanttia tietoa useiden istuntojen yli. Tämä voi sisältää tiivistelmiä, käyttäjäasetuksia ja palautetta parannuksia varten tulevaisuudessa.

 3. **Kontekstin pakkaaminen**
 Kun konteksti-ikkuna kasvaa ja lähestyy rajaa, voidaan käyttää tekniikoita kuten tiivistämistä ja karsimista. Tämä tarkoittaa joko vain tärkeimpien tietojen säilyttämistä tai vanhempien viestien poistamista.

 4. **Moniagenttijärjestelmät**
 Moniagenttijärjestelmien kehittäminen on eräänlaista kontekstisuunnittelua, koska jokaisella agentilla on oma konteksti-ikkunansa. Miten tämä konteksti jaetaan ja välitetään eri agenteille, on toinen asia, jonka täytyy suunnitella näitä järjestelmiä rakennettaessa.

 5. **Hiekkalaatikkoympäristöt**
 Jos agentin täytyy suorittaa koodia tai käsitellä suuria tietomääriä dokumentissa, tämä voi käyttää paljon tokeneita tulosten käsittelyyn. Sen sijaan, että kaikki tallennettaisiin konteksti-ikkunaan, agentti voi käyttää hiekkalaatikkoympäristöä, joka pystyy suorittamaan koodin ja lukemaan vain tulokset ja muun relevantin tiedon.

 6. **Ajonaikaiset tilaobjektit**
 Tämä tehdään luomalla tietopaketteja toimintojen hallintaan tilanteissa, joissa agentin täytyy päästä käsiksi tiettyihin tietoihin. Monimutkaisessa tehtävässä tämä mahdollistaa agentin tallentaa kunkin alitehtävän tulokset vaihe vaiheelta, jolloin konteksti pysyy yhteydessä vain kyseiseen alitehtävään.

#### Kontekstin tarkastelu

Kun olet käyttänyt yhtä näistä strategioista, kannattaa tarkistaa, mitä seuraava mallin kutsu todella sai. Käytännöllinen virheenkorjauskysymys on:

> Latasiko agentti liikaa kontekstia, väärää kontekstia vai puuttuiko siltä tarvitsemaansa kontekstia?

Et tarvitse tallentaa raakakehotteita, työkalujen tuotosdataa tai muistojen sisältöjä vastataksesi tähän kysymykseen. Tuotannossa kannattaa käyttää pieniä kontekstin tarkastuslokeja, jotka tallentavat lukumäärät, tunnisteet, hajautukset ja politiikkalabelit:

- **Valinta:** Seuraa, kuinka monta ehdokaspalasta, työkalua tai muistia harkittiin, kuinka monta valittiin ja mikä sääntö tai pisteytys poisti muut valinnat.

- **Pakkaus:** Tallenna lähdeväli tai jäljitunnus, tiivistelmän tunnus, arvioitu tokenien määrä ennen ja jälkeen pakkaamisen sekä oliko raakasisältö poissuljettu seuraavasta kutsusta.

- **Eristäminen:** Merkitse, mikä alitehtävä suoritettiin erillisessä agentissa, istunnossa tai hiekkalaatikossa, mikä rajattu tiivistelmä palautettiin ja pysyikö suuri työkalutuotos vanhemman agentin kontekstin ulkopuolella.

- **Muisti ja RAG:** Tallenna hakudokumenttien tunnukset, muistojen tunnukset, pisteet, valitut tunnukset ja sensuurin tila koko noudetun tekstin sijaan.

- **Turvallisuus ja yksityisyys:** Käytä mieluummin hajautuksia, tunnuksia, tokenien määriä ja politiikkalabeleita kuin arkaluonteista kehotetekstiä, työkalujen argumentteja, työkalun tuloksia tai käyttäjän muistojen sisältöjä.

Tavoite ei ole säilyttää enemmän kontekstia, vaan jättää riittävästi todisteita, jotta kehittäjä voi kertoa, mikä kontekstistrategia käynnistettiin ja muutiko se seuraavaa mallin kutsua tarkoitetulla tavalla.

### Esimerkki kontekstisuunnittelusta

Oletetaan, että haluamme tekoälyagentin **"Varaamaan minulle matkan Pariisiin."**

• Yksinkertainen agentti, joka käyttää vain kehotteiden suunnittelua, voisi vastata: **"Hyvä on, milloin haluaisit mennä Pariisiin?"** Se käsitteli vain suoraan esitetyn kysymyksesi.

• Agentti, joka käyttää tässä käsiteltyjä kontekstisuunnittelustrategioita, tekisi paljon enemmän. Ennen vastaamista sen järjestelmä voisi:

  ◦ **Tarkistaa kalenterisi** vapaita päiviä varten (noutamassa reaaliaikaista tietoa).

  ◦ **Muistaa menneet matkustusmieltymykset** (pitkäaikaismuistista) kuten suosikkilentoyhtiösi, budjettisi tai haluatko suoria lentoja.

  ◦ **Tunnistaa käytettävissä olevat työkalut** lento- ja hotellivarauksiin.

- Sitten esimerkkivastaus voisi olla: "Hei [Nimesi]! Näen, että olet vapaa lokakuun ensimmäisellä viikolla. Haetaanko suoria lentoja Pariisiin lentoyhtiöllä [Suosittu lentoyhtiö] tavanomaisella budjetillasi [Budjetti]?" Tämä rikkaampi, kontekstitietoinen vastaus osoittaa kontekstisuunnittelun voiman.

## Yleiset kontekstin virheet

### Kontekstin myrkytys

**Mitä se on:** Kun harhaluulo (LLM:n tuottama väärä tieto) tai virhe pääsee kontekstiin ja sitä viitataan toistuvasti, jolloin agentti pyrkii mahdottomiin tavoitteisiin tai kehittää järjettömiä strategioita.

**Mitä tehdä:** Ota käyttöön **kontekstin validointi** ja **eristys**. Vahvista tiedot ennen kuin ne lisätään pitkäaikaismuistiin. Jos mahdollinen myrkytys havaitaan, aloita uusia kontekstiketjuja estämään huonon tiedon leviämistä.

**Matkavarausesimerkki:** Agenttisi kuvittelee **suorat lennot pieneltä paikalliselta lentokentältä kaukaiseen kansainväliseen kaupunkiin**, jossa ei oikeasti ole kansainvälisiä lentoja. Tämä olematon lentotieto tallentuu kontekstiin. Myöhemmin, kun pyydät agenttia varaamaan, se yrittää jatkuvasti löytää lippuja tälle mahdottomalle reitille, mikä johtaa toistuviin virheisiin.

**Ratkaisu:** Tee vaihe, joka **vahvistaa lennon olemassaolon ja reitit reaaliaikaisella API:lla** _ennen_ lentotiedon lisäämistä agentin työkontekstiin. Jos validointi epäonnistuu, virheellinen tieto erotetaan eristykseen eikä sitä käytetä enää.

### Kontekstin häirintä

**Mitä se on:** Kun konteksti kasvaa niin suureksi, että malli keskittyy liikaa kertynyttä historiaa kohtaan sen sijaan, että käyttäisi koulutuksessa oppimaansa, mikä johtaa toistuviin tai hyödyttömiin toimiin. Mallit voivat alkaa tehdä virheitä jo ennen kuin konteksti-ikkuna on täynnä.

**Mitä tehdä:** Käytä **kontekstin tiivistämistä**. Pakkaa kerätty tieto säännöllisesti lyhyemmiksi tiivistelmiksi, säilyttäen tärkeät yksityiskohdat ja poistamalla toistuva historia. Tämä auttaa "nollaamaan" keskittymisen.

**Matkavarausesimerkki:** Olet keskustellut unelmalomakohteistasi pitkään, mukaan lukien yksityiskohtainen kertomus rinkkaillulta matkalta kaksi vuotta sitten. Kun pyydät lopulta **"löydä minulle halpa lento ensi kuulle"**, agentti juuttuu vanhoihin, epäolennaisiin yksityiskohtiin ja jatkaa kyselyitä rinkkailutarvikkeistasi tai menneistä matkasuunnitelmistasi, unohtaen nykyisen pyyntösi.

**Ratkaisu:** Tietyn määrän vuorovaikutuksia jälkeen tai kun konteksti kasvaa liian suureksi, agentin tulisi **tiivistää keskustelun viimeisimmät ja olennaisimmat osat** – keskittyen nykyisiin matkustuspäiviisi ja kohteeseesi – ja käyttää tätä tiivistettyä kokonaista seuraavassa LLM-kutsussa, hyläten vähemmän relevantin historiallisen keskustelun.

### Kontekstin sekaannus

**Mitä se on:** Kun tarpeettoman suuri määrä kontekstia, usein lukuisien käytettävissä olevien työkalujen muodossa, saa mallin tuottamaan huonoja vastauksia tai kutsumaan epäolennaisia työkaluja. Pienemmät mallit ovat erityisen alttiita tälle.

**Mitä tehdä:** Ota käyttöön **työkalujen kuormanhallinta** RAG-tekniikoilla. Tallenna työkalujen kuvaukset vektoripohjaiseen tietokantaan ja valitse _vain_ kaikkein relevantimmat työkalut kutakin tehtävää varten. Tutkimukset osoittavat, että työkalujen valinta kannattaa rajata alle 30 kappaleeseen.

**Matkavarausesimerkki:** Agentillasi on pääsy kymmeniin työkaluihin: `book_flight`, `book_hotel`, `rent_car`, `find_tours`, `currency_converter`, `weather_forecast`, `restaurant_reservations` jne. Kysyt, **"Mikä on paras tapa liikkua Pariisissa?"** Työkalujen suuren määrän vuoksi agentti sekoaa ja yrittää kutsua `book_flight` _Pariisin sisällä_ tai `rent_car` vaikka suosisit julkista liikennettä, koska työkalujen kuvaukset voivat mennä päällekkäin tai se ei pysty erottamaan parasta työkalua.

**Ratkaisu:** Käytä **RAG:ia työkalukuvauksissa**. Kun kysyt Pariisissa liikkumisesta, järjestelmä hakee dynaamisesti _vain_ olennaisimmat työkalut kuten `rent_car` tai `public_transport_info` kyselysi perusteella, esitellen kohdennetun "työkalupakkauksen" LLM:lle.

### Kontekstin ristiriita

**Mitä se on:** Kun kontekstissa on ristiriitaista tietoa, mikä johtaa epäjohdonmukaiseen päättelyyn tai huonoihin lopullisiin vastauksiin. Tämä tapahtuu usein, kun tieto saapuu vaiheittain ja varhaiset virheelliset oletukset jäävät kontekstiin.

**Mitä tehdä:** Käytä **kontekstin karsintaa** ja **uloslatausta**. Karsinta tarkoittaa vanhentuneen tai ristiriitaisen tiedon poistamista uusien tietojen saapuessa. Uloslataus antaa mallille erillisen "muistilehtiö"-työtilan tiedon käsittelyyn ilman, että pääkontekstiin kerääntyy hälyä.
**Matkavarauksen esimerkki:** Aluksi kerrot agentillesi, **"Haluan lentää economy-luokassa."** Keskustelun myöhemmässä vaiheessa muutat mielesi ja sanot, **"Itse asiassa tällä matkalla mennään business-luokassa."** Jos molemmat ohjeet pysyvät kontekstissa, agentti saattaa saada ristiriitaisia hakutuloksia tai hämmentyä siitä, kumpaa mieltymystä tulisi priorisoida.

**Ratkaisu:** Ota käyttöön **kontekstin karsiminen**. Kun uusi ohje on ristiriidassa vanhan kanssa, vanha ohje poistetaan tai korvataan selvästi kontekstissa. Vaihtoehtoisesti agentti voi käyttää **muistiinpanoalustaa** ristiriitaisten mieltymysten sovittamiseen ennen päätöksen tekemistä, varmistamalla, että ainoastaan lopullinen, yhdenmukainen ohje ohjaa sen toimia.

## Onko sinulla lisää kysymyksiä kontekstitekniikasta?

Liity [Microsoft Foundry Discordiin](https://discord.com/invite/ATgtXmAS5D) tavata muita oppijoita, osallistua toimistotunteihin ja saada vastauksia tekoälyagenttien kysymyksiisi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->