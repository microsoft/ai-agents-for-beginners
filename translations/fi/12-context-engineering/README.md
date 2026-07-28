# Kontekstisuunnittelu tekoälyagentteja varten

[![Kontekstisuunnittelu](../../../translated_images/fi/lesson-12-thumbnail.ed19c94463e774d4.webp)](https://youtu.be/F5zqRV7gEag)

> _(Klikkaa yllä olevaa kuvaa nähdäksesi tämän oppitunnin videon)_

On tärkeää ymmärtää sen sovelluksen monimutkaisuus, jota varten tekoälyagentti rakennetaan, jotta voidaan luoda luotettava agentti. Meidän täytyy rakentaa tekoälyagentteja, jotka hallitsevat tiedon tehokkaasti ja pystyvät vastaamaan monimutkaisiin tarpeisiin, jotka menevät kehotteiden suunnittelun ulkopuolelle.

Tässä oppitunnissa tarkastelemme, mitä kontekstisuunnittelu on ja mitä roolia se näyttelee tekoälyagenttien rakentamisessa.

## Johdanto

Tämä oppitunti kattaa:

• **Mitä kontekstisuunnittelu on** ja miksi se poikkeaa kehotteiden suunnittelusta.

• **Tehokkaan kontekstisuunnittelun strategiat**, mukaan lukien miten kirjoittaa, valita, pakata ja erotella tietoa.

• **Yleiset kontekstivirheet**, jotka voivat estää tekoälyagenttisi toimintaa, ja kuinka ne korjataan.

## Oppimistavoitteet

Oppitunnin suorittamisen jälkeen ymmärrät miten:

• **Määritellään kontekstisuunnittelu** ja erotetaan se kehotteiden suunnittelusta.

• **Tunnistetaan kontekstin keskeiset osat** suurten kielimallien (LLM) sovelluksissa.

• **Sovelletaan strategioita kontekstin kirjoittamiseksi, valitsemiseksi, pakkaamiseksi ja eristämiseksi** agentin suorituskyvyn parantamiseksi.

• **Tunnistetaan tavalliset kontekstivirheet** kuten myrkytys, häiriö, sekaannus ja ristiriita sekä toteutetaan niiden lieventämistekniikat.

## Mitä on kontekstisuunnittelu?

Tekoälyagenteille konteksti on se, mikä ohjaa agentin suunnittelua suorittaa tiettyjä toimia. Kontekstisuunnittelu tarkoittaa käytäntöä varmistaa, että tekoälyagentilla on oikea tieto seuraavan tehtävävaiheen suorittamiseen. Konteksti-ikkuna on kooltaan rajallinen, joten agenttien kehittäjinä meidän täytyy rakentaa järjestelmiä ja prosesseja tiedon lisäämisen, poistamisen ja tiivistämisen hallitsemiseksi konteksti-ikkunassa.

### Kehote- ja kontekstisuunnittelu

Kehotesuunnittelu keskittyy yhteen staattiseen ohjeistukseen ohjaamaan tekoälyagentteja sääntöjen avulla. Kontekstisuunnittelu puolestaan hallitsee dynaamista tietomäärää, mukaan lukien alkuperäinen kehotus, varmistaakseen, että tekoälyagentilla on tarvittavat tiedot ajan mittaan. Kontekstisuunnittelun päätavoite on tehdä tämä prosessi toistettavaksi ja luotettavaksi.

### Kontekstin tyypit

[![Kontekstin tyypit](../../../translated_images/fi/context-types.fc10b8927ee43f06.webp)](https://youtu.be/F5zqRV7gEag)

On tärkeää muistaa, että konteksti ei ole vain yksi asia. Tekoälyagentin tarvitsema tieto voi tulla monista eri lähteistä, ja meidän tehtävämme on varmistaa agentin pääsy näihin lähteisiin:

Kontekstin tyypit, joita tekoälyagentin täytyy ehkä hallita, sisältävät:

• **Ohjeet:** Nämä ovat agentin ”sääntöjä” – kehotteita, järjestelmäviestejä, muutama esimerkkitapaus (näyttää tekoälylle miten tehdä jokin asia) ja työkalujen kuvauksia, joita se voi käyttää. Tämä on alue, jossa kehotteiden suunnittelu yhdistyy kontekstisuunnitteluun.

• **Tiedot:** Sisältää faktoja, tietokannoista haettua tietoa tai pitkäaikaismuistia, jota agentti on kertynyt. Ayhteen voi kuulua myös hakua vahvistava generointijärjestelmä (RAG), jos agentin pitää päästä eri tietovarastoihin ja tietokantoihin käsiksi.

• **Työkalut:** Nämä ovat ulkoisten funktioiden, API:en ja MCP-palvelinten määritelmiä, joita agentti voi kutsua, ja niiden käytöstä saatua palautetta (tuloksia).

• **Keskusteluhistoria:** Käyttäjän kanssa käyty jatkuva vuoropuhelu. Ajan kuluessa nämä keskustelut pitenevät ja monimutkaistuvat, mikä vie tilaa konteksti-ikkunassa.

• **Käyttäjän mieltymykset:** Ajan myötä opittua tietoa käyttäjän mieltymyksistä tai ei-mieltymyksistä. Näitä voidaan tallentaa ja käyttää päätöksiä tehtäessä käyttäjän avuksi.

## Tehokkaan kontekstisuunnittelun strategiat

### Suunnittelustrategiat

[![Kontekstisuunnittelun parhaat käytännöt](../../../translated_images/fi/best-practices.f4170873dc554f58.webp)](https://youtu.be/F5zqRV7gEag)

Hyvä kontekstisuunnittelu alkaa hyvällä suunnittelulla. Tässä on lähestymistapa, joka auttaa sinua aloittamaan kontekstisuunnittelun soveltamisen:

1. **Määrittele selkeät tulokset** – Tekoälyagentille annettujen tehtävien tulokset tulee määritellä selkeästi. Vastaa kysymykseen – ”Miltä maailma näyttää, kun tekoälyagentti on suorittanut tehtävänsä?” Toisin sanoen, mitä muutosta, tietoa tai vastausta käyttäjä saa hyväksi agentin kanssa vuorovaikutuksen jälkeen.
2. **Kartoitä konteksti** – Kun olet määritellyt agentin tehtävien tulokset, sinun täytyy vastata kysymykseen ”Mitä tietoa agentti tarvitsee tehtävän suorittamiseen?”. Tällä tavoin voit alkaa kartoittaa, mistä tämä tieto löytyy.
3. **Luo kontekstiputket** – Kun tiedät, mistä tieto löytyy, täytyy pohtia ”Miten agentti saa tämän tiedon?”. Tämä voidaan toteuttaa esimerkiksi RAG-järjestelmillä, MCP-palvelimilla ja muilla työkaluilla.

### Käytännölliset strategiat

Suunnittelu on tärkeää, mutta kun tieto alkaa virrata agentin konteksti-ikkunaan, tarvitsemme käytännöllisiä strategioita sen hallintaan:

#### Kontekstin hallinta

Vaikka jotkut tiedot lisätään konteksti-ikkunaan automaattisesti, kontekstisuunnittelu tarkoittaa aktiivisempaa tiedon hallintaa, joka voidaan toteuttaa muutamilla strategioilla:

 1. **Agentin muistiinpanoalue**
 Tämä mahdollistaa tekoälyagentille muistiinpanojen tekemisen tärkeistä tiedoista kyseisen istunnon aikana. Sen tulisi sijaita konteksti-ikkunan ulkopuolella tiedostossa tai ajonaikaisessa objektissa, johon agentti voi tarvittaessa palata istunnon aikana.

 2. **Muistot**
 Muistiinpanot sopivat tiedon hallintaan yksittäisen istunnon ulkopuolella. Muistot mahdollistavat agenttien tallentaa ja hakea relevanttia tietoa useiden istuntojen yli. Tämä voi sisältää yhteenvetoja, käyttäjän mieltymyksiä ja palautetta tulevia parannuksia varten.

 3. **Kontekstin pakkaaminen**
  Kun konteksti-ikkuna kasvaa ja on lähellä rajaansa, voidaan käyttää tekniikoita kuten tiivistämistä ja karsintaa. Tämä tarkoittaa tärkeimmän tiedon säilyttämistä tai vanhempien viestien poistamista.
  
 4. **Moniagenttijärjestelmät**
  Moniagenttijärjestelmän kehittäminen on kontekstisuunnittelua, koska jokaisella agentilla on oma konteksti-ikkunansa. Miten tämä konteksti jaetaan ja välitetään eri agenteille on myös suunniteltava, kun rakennetaan näitä järjestelmiä.
  
 5. **Hiekkalaatikkoympäristöt**
  Jos agentin täytyy suorittaa koodia tai prosessoida suuria tietomääriä dokumentissa, se voi vaatia paljon tokeneita tulosten käsittelyyn. Sen sijaan, että kaikki tieto olisi tallennettuna konteksti-ikkunaan, agentti voi käyttää hiekkalaatikkoympäristöä, joka suorittaa koodin ja lukee vain tulokset ja muut olennaiset tiedot.
  
 6. **Ajonaikaiset tilakontit**
   Tämä tehdään luomalla tietokontteja hallitsemaan tilanteita, joissa agentin täytyy päästä tiettyihin tietoihin käsiksi. Monimutkaisissa tehtävissä tämä mahdollistaa agentin tallentaa jokaisen alitehtävän tulokset vaihe vaiheelta ja pitää konteksti sidottuna vain kyseiseen alitehtävään.

#### Kontekstin tarkastelu

Kun olet käyttänyt jonkin näistä strategioista, on hyvä tarkistaa, mitä seuraava mallikutsu todellisuudessa sai. Hyvä virheenkorjauskysymys on:

> Latasiko agentti liikaa kontekstia, väärää kontekstia vai jäikö tarvittava konteksti puuttumaan?

Et tarvitse tallentaa raakakehotteita, työkalujen tulosteita tai muistisisältöä vastataksesi tuohon kysymykseen. Tuotannossa suositaan pieniä kontekstin tarkastuslokeja, jotka tallentavat määriä, tunnuksia, hajautteita ja politiikan merkintöjä:

- **Valinta:** Seuraa kuinka monta ehdokaslohkoa, työkalua tai muistia harkittiin, kuinka monta valittiin ja mikä sääntö tai pistemäärä suodatettiin muut pois.
- **Pakkaaminen:** Tallenna lähdealue tai jäljitunnus, yhteenvetotunnus, arvioitu tokenien määrä ennen ja jälkeen pakkaamisen, ja jätettiinkö raakasisältö pois seuraavasta kutsusta.
- **Eristäminen:** Merkitse mikä alitehtävä suoritettiin erillisellä agentilla, istunnolla tai hiekkalaatikossa, mikä rajattu yhteenveto palautettiin, ja pysyikö suuri työkalun tulostus vanhemman agentin ulkopuolella.
- **Muisti ja RAG:** Tallenna haun dokumenttitunnukset, muistotunnukset, pistemäärät, valitut tunnukset ja sensuurin tila täydellisen haetun tekstin sijaan.
- **Turvallisuus ja yksityisyys:** Suosi hajautteita, tunnuksia, tokenipusseja ja politiikan merkintöjä arkaluonteisen kehotetekstin, työkalujen argumenttien, tulosten tai käyttäjän muistojen sijaan.

Tavoite ei ole säilyttää enemmän kontekstia, vaan jättää riittävästi todisteita, jotta kehittäjä voi selvittää, mikä kontekstistrategia käytettiin ja muutiko se seuraavaa mallikutsua tarkoitetulla tavalla.

### Esimerkki kontekstisuunnittelusta

Kuvitellaan, että haluamme tekoälyagentin, joka **”Varaisi minulle matkan Pariisiin.”**

• Yksinkertainen agentti, joka käyttää vain kehotteiden suunnittelua, voisi vain vastata: **”Selvä, milloin haluaisit mennä Pariisiin?”**. Se käsitteli kysymyksesi suoraan juuri silloin, kun käyttäjä sitä kysyi.

• Agentti, joka käyttää tässä käsiteltyjä kontekstisuunnittelun strategioita, tekisi paljon enemmän. Ennen vastaamista järjestelmä voisi:

  ◦ **Tarkistaa kalenterisi** saatavilla olevien päivämäärien osalta (hakea reaaliaikaista dataa).

 ◦ **Muistaa aiemmat matkustusehdotuksesi** (pitkäaikaismuistista) kuten suosikkilentoyhtiösi, budjetin tai suoran lennon mieltymyksen.

 ◦ **Tunnistaa käytettävissä olevat työkalut** lento- ja hotellivarausta varten.

- Sitten esimerkkivastauksena voisi olla: ”Hei [Nimesi]! Näen, että olet vapaa lokakuun ensimmäisellä viikolla. Haluatko, että etsin suoria lentoja Pariisiin [Suosikkilentoyhtiö] ja normaalissa budjetissasi [Budjetti]?” Tämä rikkaampi, kontekstia huomioiva vastaus osoittaa kontekstisuunnittelun voimaa.

## Yleisiä kontekstivirheitä

### Kontekstin myrkytys

**Mitä se on:** Kun harhahallusinaatio (LLM:n tuottama virheellinen tieto) tai virhe pääsee kontekstiin ja siihen viitataan toistuvasti, mikä saa agentin tavoittelemään mahdottomia päämääriä tai kehittämään järjettömiä strategioita.

**Mitä tehdä:** Toteuta **kontekstin validoiminen** ja **eristäminen**. Vahvista tiedon oikeellisuus ennen sen lisäämistä pitkäaikaismuistiin. Jos mahdollinen myrkytys havaitaan, aloita uudet kontekstiketjut estämään virheellisen tiedon leviäminen.

**Matkavarauksen esimerkki:** Agenttisi tuo harhaanjohtavasti esiin **suoran lennon pienen paikallislentokentän ja kaukana sijaitsevan kansainvälisen kaupungin välillä**, joka ei todellisuudessa tarjoa kansainvälisiä lentoja. Tämä olematon lentotieto tallentuu kontekstiin. Kun pyydät agenttia varaamaan matkan, se yrittää jatkuvasti etsiä lippuja tälle mahdottomalle reitille, mikä aiheuttaa toistuvia virheitä.

**Ratkaisu:** Toteuta vaihe, joka **tarkistaa lennon olemassaolon ja reitit reaaliaikaisella API:lla** _ennen_ kuin lentotiedot lisätään agentin työkontekstiin. Jos tarkistus epäonnistuu, virheellinen tieto laitetaan "eristykseen" eikä sitä käytetä enää.

### Kontekstihäiriö

**Mitä se on:** Kun konteksti kasvaa niin suureksi, että malli keskittyy liikaa kertyneeseen historiaan eikä siihen, mitä se on oppinut koulutuksessa, mikä johtaa toistuviin tai epäavuliaisiin toimintoihin. Mallit voivat alkaa tehdä virheitä jo ennen kuin konteksti-ikkuna on täynnä.

**Mitä tehdä:** Käytä **kontekstin tiivistystä**. Purista ajoittain kertyneen tiedon tiiviimpiin yhteenvetoihin, säilyttäen tärkeät tiedot ja jättämällä pois epäolennaisen historian. Tämä auttaa "nollaamaan" keskittymisen.

**Matkavarauksen esimerkki:** Olet keskustellut pitkään monista unelmakohteista sisältäen yksityiskohtaisen kuvauksen vaelluksestasi kaksi vuotta sitten. Kun lopulta pyydät **”etsi minulle halpa lento ensi kuulle”**, agentti jumittuu vanhoihin, epäolennaisiin tietoihin ja kysyy jatkuvasti reppuvälineistäsi tai aiemmista reittisuunnitelmista, unohtaen nykyisen pyynnön.

**Ratkaisu:** Tietyn määrän vuorovaikutuksia jälkeen tai kontekstin kasvaessa liikaa agentin tulisi **tiivistää keskustelun viimeisimmät ja oleellisimmat osat** – keskittyen tämänhetkisiin matkapäiviin ja kohteeseen – ja käyttää tätä tiivistelmää seuraavassa LLM-kutsussa, hyläten vähemmän olennaisen historiakeskustelun.

### Kontekstin sekaannus

**Mitä se on:** Kun tarpeettoman suuri konteksti, usein liian monien käytettävissä olevien työkalujen muodossa, saa mallin tuottamaan huonoja vastauksia tai kutsumaan epäolennaisia työkaluja. Pienemmät mallit ovat tähän erityisen alttiita.

**Mitä tehdä:** Toteuta **työkalujen hallinta** RAG-tekniikoilla. Tallenna työkalujen kuvaukset vektoritietokantaan ja valitse _vain_ tehtävään relevantit työkalut. Tutkimukset osoittavat, että työkalujen määrän rajoittaminen alle 30:n on tehokasta.

**Matkavarauksen esimerkki:** Agentilla on käytössään kymmeniä työkaluja: `book_flight`, `book_hotel`, `rent_car`, `find_tours`, `currency_converter`, `weather_forecast`, `restaurant_reservations` jne. Kysyt, **"Mikä on paras tapa liikkua Pariisissa?"** Suuren työkalumäärän vuoksi agentti hämmentyy ja yrittää kutsua `book_flight` _Pariisin sisällä_ tai `rent_car` vaikka suosittelet joukkoliikennettä, koska työkalukuvausten tiedot voivat mennä päällekkäin tai agentti ei pysty valitsemaan parasta.

**Ratkaisu:** Käytä **RAGia työkalukuvausten päällä**. Kun kysyt liikkumistavasta Pariisissa, järjestelmä hakee *vain* relevantit työkalut kuten `rent_car` tai `public_transport_info` kyselysi perusteella, esittäen fokusoidun työkalusarjan LLM:lle.

### Kontekstin ristiriita

**Mitä se on:** Kun ristiriitaista tietoa on kontekstissa, mikä johtaa epäjohdonmukaiseen päättelyyn tai huonoihin lopullisiin vastauksiin. Tämä tapahtuu usein, kun tietoa saapuu vaiheittain ja aikaiset, väärät oletukset jäävät kontekstiin.

**Mitä tehdä:** Käytä **kontekstin karsimista** ja **siirtämistä pois**. Karsiminen tarkoittaa vanhentuneen tai ristiriitaisen tiedon poistamista uusien tietojen saapuessa. Siirtäminen pois antaa mallille erillisen "muistiinpanotyötilan" tiedon käsittelyyn ilman pääkontekstin sotkemista.


**Matkavarauksen esimerkki:** Kerrot agentillesi aluksi, **"Haluan lentää economy-luokassa."** Myöhemmin keskustelun aikana muutat mieltäsi ja sanot, **"Oikeastaan, tehdään tälle matkalle business-luokka."** Jos molemmat ohjeet pysyvät kontekstissa, agentti saattaa saada ristiriitaisia hakutuloksia tai hämmentyä siitä, kumpaa mieltymystä pitää ensisijaisena.

**Ratkaisu:** Toteuta **kontekstin karsinta**. Kun uusi ohje on ristiriidassa vanhan kanssa, vanhempi ohje poistetaan tai korvataan eksplisiittisesti kontekstissa. Vaihtoehtoisesti agentti voi käyttää **muistiinpanoalustaa** (scratchpad) ristiriitaisten mieltymysten sovittamiseen ennen päätöksentekoa, varmistaen, että vain lopullinen ja johdonmukainen ohje ohjaa sen toimintaa.

## Onko sinulla lisää kysymyksiä kontekstisuunnittelusta?

Liity [Microsoft Foundry Discordiin](https://discord.com/invite/ATgtXmAS5D) tavata muita oppijoita, osallistua toimistoaikoihin ja saada vastauksia AI-agenttien kysymyksiin.
## Edellinen oppitunti

[Agenttien protokollat](../11-agentic-protocols/README.md)

## Seuraava oppitunti

[Muisti AI-agenteille](../13-agent-memory/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->