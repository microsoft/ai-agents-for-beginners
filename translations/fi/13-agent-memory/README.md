# Muisti tekoälyagenteille  
[![Agent Memory](../../../translated_images/fi/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Kun keskustellaan tekoälyagenttien ainutlaatuisista eduista, esiin nousevat pääasiassa kaksi asiaa: kyky kutsua työkaluja tehtävien suorittamiseen ja kyky parantua ajan myötä. Muisti on itsensä parantavan agentin luomisen perusta, mikä mahdollistaa parempien käyttäjäkokemusten luomisen.

Tässä oppitunnissa tarkastelemme, mitä muisti tarkoittaa tekoälyagenteille ja miten voimme hallita sitä ja hyödyntää sitä sovellustemme eduiksi.

## Johdanto

Tämä oppitunti käsittelee:

• **Tekoälyagentin muistin ymmärtäminen**: Mikä muisti on ja miksi se on agenteille tärkeää.

• **Muistin toteutus ja tallennus**: Käytännön menetelmät lisätä muistitoimintoja tekoälyagenteillesi, keskittyen lyhytaikaiseen ja pitkäaikaiseen muistiin.

• **Tekoälyagenttien itsensä parantaminen**: Miten muisti mahdollistaa agenttien oppimisen aiemmista vuorovaikutuksista ja kehittymisen ajan myötä.

## Saatavilla olevat toteutukset

Tässä oppitunnissa on kaksi kattavaa muistikirjatutoriaalia:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Toteuttaa muistin käyttäen Mem0:aa ja Azure AI Searchia Microsoft Agent Frameworkin kanssa

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Toteuttaa rakenteellisen muistin käyttämällä Cogneetä, joka rakentaa automaattisesti upotuksiin pohjautuvan tietämyskaavion, visualisoi kaavion ja tarjoaa älykkään hakutoiminnon

## Oppimistavoitteet

Oppitunnin suorittamisen jälkeen osaat:

• **Erotella erilaisia tekoälyagenttien muistityyppejä**, kuten työmuistin, lyhytaikaisen ja pitkäaikaisen muistin sekä erikoistuneet muodot kuten persoonamuisti ja episodi-muisti.

• **Toteuttaa ja hallita lyhyt- ja pitkäaikaista muistia tekoälyagenteille** käyttäen Microsoft Agent Frameworkia ja hyödyntäen työkaluja kuten Mem0, Cognee, Whiteboard-muisti sekä Azure AI Searchin integrointia.

• **Ymmärtää itsensä parantavien tekoälyagenttien periaatteet** ja miten vahvat muistinhallintajärjestelmät tukevat jatkuvaa oppimista ja sopeutumista.

## Tekoälyagentin muistin ymmärtäminen

Ytimessä **tekoälyagenttien muisti viittaa mekanismeihin, jotka mahdollistavat tiedon säilyttämisen ja palauttamisen**. Tämä tieto voi olla yksityiskohtia keskustelusta, käyttäjän mieltymyksiä, aiempia toimia tai jopa opittuja malleja.

Ilman muistia tekoälysovellukset ovat usein tilattomia, eli jokainen vuorovaikutus alkaa tyhjältä pöydältä. Tämä johtaa toisteiseen ja turhauttavaan käyttökokemukseen, jossa agentti "unohtaa" aiemman kontekstin tai mieltymykset.

### Miksi muisti on tärkeä?

Agentin älykkyys kytkeytyy voimakkaasti sen kykyyn palauttaa ja hyödyntää aiempaa tietoa. Muisti mahdollistaa agenttien olevan:

• **Pohdiskelevia**: Oppimaan menneistä toimista ja tuloksista.

• **Vuorovaikutteisia**: Säilyttämään kontekstin käynnissä olevan keskustelun aikana.

• **Ennakoivia ja reaktiivisia**: Ennakoimaan tarpeita tai vastaamaan sopivasti historiallisten tietojen perusteella.

• **Autonomisia**: Toimimaan itsenäisemmin käyttämällä tallennettua tietoa.

Muistin toteuttamisen tavoitteena on tehdä agenteista **luotettavampia ja kyvykkäämpiä**.

### Muistityypit

#### Työmuisti

Ajattele tätä kuin muistilappua, jota agentti käyttää yhden käynnissä olevan tehtävän tai ajatusprosessin aikana. Se pitää väliaikaisesti tallessa tietoa, jota tarvitaan seuraavan askeleen laskemiseksi.

Tekoälyagenteilla työmuisti tallentaa usein keskustelun olennaisimmat tiedot, vaikka koko chat-historia olisi pitkä tai katkaistu. Se keskittyy poimimaan keskeiset osat kuten vaatimukset, ehdotukset, päätökset ja toimenpiteet.

**Työmuistin esimerkki**

Matkavarausagentilla työmuisti saattaa tallentaa käyttäjän tämänhetkisen pyynnön, kuten "Haluan varata matkan Pariisiin". Tämä tarkka vaatimus pidetään agentin välittömässä kontekstissa ohjaamaan nykyistä keskustelua.

#### Lyhytaikainen muisti

Tämä muistityyppi säilyttää tietoa yhden keskustelun tai istunnon ajan. Se on nykyisen keskustelun konteksti, joka antaa agentin viitata aiempiin vuorovaikutuksen osiin.

[Microsoft Agent Frameworkin](https://github.com/microsoft/agent-framework) Python SDK -esimerkeissä tämä vastaa `AgentSession`ia, joka luodaan `agent.create_session()`-komennolla. Istunto on kehyksen sisäänrakennettu lyhytaikainen muisti: se pitää keskustelun kontekstin käytettävissä, kun samaa istuntoa käytetään uudelleen, mutta kontekstia ei tallenneta pysyvästi istunnon loputtua tai sovelluksen uudelleenkäynnistyksessä. Käytä pitkäaikaista muistia faktoihin ja mieltymyksiin, jotka pitää säilyttää istuntojen välillä, yleensä tietokannan, vektori-indeksin tai muun pysyvän tallennuksen avulla.

**Lyhytaikaisen muistin esimerkki**

Jos käyttäjä kysyy "Kuinka paljon lennot Pariisiin maksavat?" ja jatkaa "Entä majoitus siellä?", lyhytaikainen muisti varmistaa, että agentti tietää "siellä" tarkoittavan "Pariisia" saman keskustelun aikana.

#### Pitkäaikainen muisti

Tämä on tietoa, joka säilyy useiden keskustelujen tai istuntojen yli. Se mahdollistaa agenttien muistavan käyttäjän mieltymykset, aiemmat vuorovaikutukset tai yleisen tiedon pidemmällä aikavälillä. Tämä on tärkeää personoinnissa.

**Pitkäaikaisen muistin esimerkki**

Pitkäaikainen muisti voi tallentaa, että "Ben nauttii laskettelusta ja ulkoilusta, pitää kahvista vuoristomaisemalla ja haluaa välttää haastavia laskettelurinteitä aiemman vamman vuoksi". Tämä tieto, opittu aiemmista keskusteluista, vaikuttaa suosituksiin tulevissa matkanjärjestelyissä tehden niistä hyvin räätälöityjä.

#### Persoonamuisti

Tämä erikoistunut muistityyppi auttaa agenttia kehittämään johdonmukaisen "persoonallisuuden" tai "hahmon". Se antaa agentille mahdollisuuden muistaa tietoja itsestään tai suunnitellusta roolistaan, tehden vuorovaikutuksesta sujuvampaa ja keskittyneempää.

**Persoonamuistin esimerkki**  
Jos matkatoimistoagentti on suunniteltu "asiantuntijalaskettelusuunnittelijaksi", persoonamuisti voi vahvistaa tätä roolia ja vaikuttaa sen vastauksiin asiantuntijatyyppisen sävyn ja tiedon mukaisesti.

#### Työnkulku-/episodimuisti

Tämä muisti tallentaa sarjan askeleita, jotka agentti suorittaa monimutkaisen tehtävän aikana, sisältäen onnistumiset ja epäonnistumiset. Se on kuin menneiden "jaksojen" tai kokemusten muistamista oppimista varten.

**Episodimuistin esimerkki**

Jos agentti yritti varata tietyn lennon, mutta epäonnistui saatavuussyistä, episodimuisti voi kirjata tämän epäonnistumisen, jolloin agentti voi kokeilla vaihtoehtoisia lentoja tai informoida käyttäjää ongelmasta paremmin seuraavalla yrityksellä.

#### Entiteettimuisti

Tämä käsittää keskusteluista johdettavien tiettyjen entiteettien (kuten henkilöiden, paikkojen tai esineiden) ja tapahtumien tunnistamisen ja muistamisen. Se antaa agentille mahdollisuuden rakentaa jäsennelty ymmärrys keskustelun keskeisistä elementeistä.

**Entiteettimuistin esimerkki**

Keskustelusta menneestä matkasta agentti voi poimia entiteetit kuten "Pariisi", "Eiffel-torni" ja "illallinen Le Chat Noir -ravintolassa". Tulevissa vuorovaikutuksissa agentti voi muistaa "Le Chat Noir" ja tarjota uutta pöytävarausta sinne.

#### Rakenteellinen RAG (Retrieval Augmented Generation)

Vaikka RAG on laajempi tekniikka, "Rakenteellinen RAG" korostetaan voimakkaana muistiteknologiana. Se poimii tiivistä, jäsenneltyä tietoa eri lähteistä (keskustelut, sähköpostit, kuvat) ja käyttää sitä parantaakseen tarkkuutta, palautusta ja vastausten nopeutta. Toisin kuin klassinen RAG, joka perustuu pelkästään semanttiseen samankaltaisuuteen, Rakenteellinen RAG toimii tiedon rakenteen perusteella.

**Rakenteellisen RAG:n esimerkki**

Sen sijaan, että haettaisiin pelkkiä avainsanoja, Rakenteellinen RAG voi jäsentää lennon tiedot (kohde, päivämäärä, aika, lentoyhtiö) sähköpostista ja tallentaa ne rakenteellisesti. Tämä mahdollistaa tarkat haut kuten "Minkä lennon varasin Pariisiin tiistaina?"

## Muistin toteutus ja tallennus

Muistin toteuttaminen tekoälyagenteille on järjestelmällinen prosessi, joka sisältää **muistinhallinnan**: tiedon generoinnin, tallentamisen, hakemisen, integroinnin, päivittämisen ja jopa "unohtamisen" (tai poistamisen). Hakeminen on tästä erityisen tärkeä osa.

### Erikoistuneet muistityökalut

#### Mem0

Yksi tapa tallentaa ja hallita agentin muistia on käyttää erikoistuneita työkaluja kuten Mem0. Mem0 toimii pysyvänä muistikerroksena, joka antaa agenteille mahdollisuuden palauttaa mieleen olennaisia vuorovaikutuksia, tallentaa käyttäjän mieltymykset ja faktatiedot sekä oppia onnistumisista ja epäonnistumisista ajan myötä. Ideana on, että tilattomat agentit muuttuvat tilallisiksi.

Se toimii **kaksivaiheisella muistiputkella: poiminnalla ja päivityksellä**. Ensiksi agentin keskusteluketjuun lisätyt viestit lähetetään Mem0-palveluun, joka käyttää suurta kielimallia (LLM) tiivistämään keskusteluhistorian ja poimimaan uusia muistoja. Sen jälkeen LLM-ohjattu päivitysvaihe päättää, lisätäänkö, muutetaanko vai poistetaanko nämä muistot, ja tallentaa ne hybriditietokantaan, joka voi sisältää vektori-, kaavio- ja avain-arvo-tietokantoja. Järjestelmä tukee myös erilaisia muistityyppejä ja voi hyödyntää kaaviomuistia entiteettisuhteiden hallintaan.

#### Cognee

Toinen tehokas lähestymistapa on käyttää **Cogneetä**, avoimen lähdekoodin semanttista muistia tekoälyagenteille, joka muuntaa jäsennellyn ja jäsentämättömän datan kyseltäviksi tietämyskaavioiksi upotusten tukemana. Cognee tarjoaa **kahden tallennuksen arkkitehtuurin**, joka yhdistää vektorisamankaltaishakuun graafisuhteet, antaen agenteille kyvyn ymmärtää, mitä tieto on samankaltaista ja miten käsitteet liittyvät toisiinsa.

Se on erinomainen **hybridihakutoiminnossaan**, joka yhdistää vektorisamankaltaisuuden, kaaviorakenteen ja LLM-päättelyn — raakadatapalanhausta kaaviotietoiseen kysymysten ratkaisuun. Järjestelmä ylläpitää **elävää muistia**, joka kehittyy ja kasvaa samalla kun se pysyy haettavana yhtenä yhdistettynä kaaviona, tukien sekä lyhytaikaista istuntokontekstia että pitkäaikaista pysyvää muistia.

Cogneen muistikirjatutoriaali ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) esittelee tämän yhdistetyn muistikerroksen rakentamista käytännön esimerkeillä eri datalähteiden tuomisesta, tietämyskaavion visualisoinnista ja erilaisilla hakustrategioilla kyselyjen tekemisestä agentin tarpeisiin räätälöitynä.

### Muistin tallennus RAG:n avulla

Erikoistuneiden muistityökalujen kuten mem0:n lisäksi voit hyödyntää vahvoja hakupalveluja, kuten **Azure AI Searchia muistin tallennuksen ja hakemisen taustajärjestelmänä**, erityisesti rakenteelliseen RAG:iin.

Tämä mahdollistaa, että agentin vastaukset perustuvat omiin tietoihisi, mikä takaa relevantimmat ja tarkimmat vastaukset. Azure AI Searchia voidaan käyttää tallentamaan käyttäjäkohtaiset matkamuistot, tuotekatalogit tai muu toimialakohtainen tieto.

Azure AI Search tukee ominaisuuksia kuten **Rakenteellinen RAG**, joka poimii ja hakee tiivistä, jäsenneltyä tietoa suurista aineistoista kuten keskusteluhistoriat, sähköpostit tai jopa kuvat. Tämä tarjoaa "ihmistä ylittävän tarkkuuden ja palautuksen" verrattuna perinteiseen tekstin paloitukseen ja upotuksiin.

## Tekoälyagenttien itsensä parantaminen

Itsensä parantavien agenttien yleinen malli sisältää **"tietämyksenantin"** käyttöönoton. Tämä erillinen agentti seuraa pääkeskustelua käyttäjän ja pääagentin välillä. Sen tehtäviä ovat:

1. **Arvokkaan tiedon tunnistaminen**: Määritellä, onko keskustelun osa talletettavissa yleiseksi tiedoksi tai erityiseksi käyttäjän mieltymykseksi.

2. **Tiedon poimiminen ja tiivistäminen**: Erotella keskustelusta keskeinen oppi tai mieltymys.

3. **Tallentaminen tietokantaan**: Säilyttää poimittu tieto, usein vektoritietokantaan, jotta se voidaan hakea myöhemmin.

4. **Tulevien kyselyiden tarkentaminen**: Kun käyttäjä aloittaa uuden kyselyn, tietämyksenantaja hakee relevantin tallennetun tiedon ja liittää sen käyttäjän kehotteeseen, tarjoten tärkeän kontekstin pääagentille (kuten RAG).

### Muistin optimoinnit

• **Viiveen hallinta**: Käyttäjävuorovaikutuksen hidastumisen välttämiseksi voidaan aluksi käyttää edullisempaa, nopeampaa mallia tarkistamaan nopeasti onko tieto tallentamisen tai hakemisen arvoista, ja monimutkaisempi poiminta/haku käynnistetään vain tarvittaessa.

• **Tietämyskannan ylläpito**: Kasvavalle tietämyskannalle harvemmin käytetty tieto voidaan siirtää "kylmään säilytykseen" kustannusten hallitsemiseksi.

## Lisäkysymyksiä agenttimuistista?

Liity [Microsoft Foundry Discordiin](https://aka.ms/ai-agents/discord) tavata muita oppijoita, osallistua toimistoaikoihin ja saada vastauksia tekoälyagenttien kysymyksiin.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->