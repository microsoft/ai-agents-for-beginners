# Muisti tekoälyagenteille 
[![Agentin muisti](../../../translated_images/fi/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Kun keskustellaan tekoälyagenttien ainutlaatuisista eduista, kaksi asiaa nousevat päällimmäisinä esiin: kyky kutsua työkaluja tehtävien suorittamiseen ja kyky parantaa toimintaa ajan myötä. Muisti on perustana itseään parantavan agentin luomiselle, joka voi tarjota parempia käyttäjäkokemuksia.

Tässä oppitunnissa tarkastelemme, mitä muisti tarkoittaa tekoälyagenteille ja miten voimme hallita sitä ja käyttää sitä sovellustemme hyväksi.

## Johdanto

Tämä oppitunti kattaa:

• **Tekoälyagenttien muistin ymmärtäminen**: Mitä muisti on ja miksi se on olennaista agenteille.

• **Muistin toteuttaminen ja tallentaminen**: Käytännön menetelmät muistiominaisuuksien lisäämiseksi agentteihisi, keskittyen lyhyen ja pitkän aikavälin muistiin.

• **Tekoälyagenttien itseään parantamisen tekeminen**: Miten muisti mahdollistaa agenttien oppimisen aiemmista vuorovaikutuksista ja parantumisen ajan myötä.

## Saatavilla olevat toteutukset

Tämä oppitunti sisältää kaksi kattavaa muistikirjaopasta:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Toteuttaa muistin käyttäen Mem0:aa ja Azure AI Searchia Microsoft Agent Frameworkin kanssa

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Toteuttaa jäsennellyn muistin käyttäen Cogneea, rakentaa automaattisesti upotuksiin perustuvan tietämyskaavion, visualisoi kaavion ja tarjoaa älykkään hakutoiminnan

## Oppimistavoitteet

Oppitunnin suorittamisen jälkeen osaat:

• **Erottaa eri tyyppiset tekoälyagenttien muistit**, mukaan lukien työmuisti, lyhyen aikavälin muisti ja pitkäaikaismuisti, sekä erikoistuneet muodot kuten persoona- ja episodimuisti.

• **Toteuttaa ja hallita lyhyen ja pitkän aikavälin muistia tekoälyagenteille** käyttäen Microsoft Agent Frameworkia, hyödyntäen työkaluja kuten Mem0, Cognee, Whiteboard-muisti ja integroiden Azure AI Searchin.

• **Ymmärtää itseään parantavien tekoälyagenttien periaatteet** ja miten vankka muistinhallintajärjestelmä edistää jatkuvaa oppimista ja sopeutumista.

## Tekoälyagenttien muistin ymmärtäminen

Ytimeltään **tekoälyagenttien muisti tarkoittaa mekanismeja, jotka sallivat niiden säilyttää ja palauttaa tietoa**. Tämä tieto voi olla yksityiskohtia keskustelusta, käyttäjäasetuksia, aiempia toimia tai jopa opittuja malleja.

Ilman muistia tekoälysovellukset ovat usein tilattomia, eli jokainen vuorovaikutus alkaa alusta. Tämä johtaa toistuviin ja turhauttaviin käyttäjäkokemuksiin, joissa agentti "unohtaa" aiemman kontekstin tai mieltymykset.

### Miksi muisti on tärkeää?

agentin älykkyys liittyy syvästi sen kykyyn palauttaa ja hyödyntää aiempaa tietoa. Muisti mahdollistaa agenttien olevan:

• **Pohdiskelevia**: Oppimista aiemmista toimista ja tuloksista.

• **Interaktiivisia**: Kontekstin ylläpitämistä käynnissä olevan keskustelun aikana.

• **Eteneviä ja reagoivia**: Tarpeiden ennakointia tai asianmukaista reagointia historiallisten tietojen perusteella.

• **Autonomisia**: Toimimaan itsenäisemmin hyödyntämällä säilöttyä tietoa.

Muistin toteuttamisen tavoitteena on tehdä agenteista **luotettavampia ja kykenevämpiä**.

### Muistin tyypit

#### Työmuisti

Ajattele tätä kuin luonnospaperia, jota agentti käyttää yksittäisen käynnissä olevan tehtävän tai ajatusprosessin aikana. Se pitää väliaikaisesti tallessa tietoa, joka tarvitaan seuraavan askeleen laskemiseen.

Tekoälyagenteille työmuisti usein kaappaa keskustelusta kaikkein olennaisimmat tiedot, vaikka koko keskusteluhistoria olisi pitkä tai katkaistu. Se keskittyy poimimaan avaintekijöitä kuten vaatimuksia, ehdotuksia, päätöksiä ja toimia.

**Työmuistin esimerkki**

Matkanvarausagentissa työmuisti saattaa tallentaa käyttäjän nykyisen pyynnön, kuten "Haluan varata matkan Pariisiin". Tämä tietty vaatimus pidetään agentin välittömässä kontekstissa ohjaamaan nykyistä vuorovaikutusta.

#### Lyhytaikainen muisti

Tämä muistityyppi säilyttää tietoa yhden keskustelun tai istunnon ajan. Se on nykyisen chatin konteksti, minkä ansiosta agentti voi viitata aiempiin vuoroihin vuoropuhelussa.

**Lyhytaikaisen muistin esimerkki**

Jos käyttäjä kysyy "Paljonko lento Pariisiin maksaisi?" ja sitten jatkaa "Entä majoitus siellä?", lyhytaikainen muisti varmistaa, että agentti tietää, että "siellä" viittaa samaan keskusteluun kuuluvaan "Parisiin".

#### Pitkäaikainen muisti

Tämä on tietoa, joka säilyy useiden keskustelujen tai istuntojen yli. Se antaa agenteille mahdollisuuden muistaa käyttäjän mieltymykset, historialliset vuorovaikutukset tai yleisen tiedon pidemmällä aikavälillä. Tämä on tärkeää personoinnissa.

**Pitkäaikaisen muistin esimerkki**

Pitkäaikainen muisti voi tallentaa, että "Ben pitää hiihtämisestä ja ulkoilusta, tykkää kahvista vuoristonäkymällä ja haluaa välttää vaativia laskettelurinteitä aiemman vamman vuoksi". Tämä aiemmista vuorovaikutuksista opittu tieto vaikuttaa suosituksiin tulevissa matkan suunnittelusessioissa ja tekee niistä erittäin henkilökohtaisia.

#### Persoona-muisti

Tämä erikoistunut muistityyppi auttaa agenttia kehittämään yhtenäisen "persoonallisuuden" tai roolin. Se antaa agentin muistaa yksityiskohtia itsestään tai tarkoitetusta roolistaan, tehden vuorovaikutuksista sujuvampia ja kohdennettuja.

**Persoona-muistin esimerkki**
Jos matka-agentti on suunniteltu olemaan "asiantuntija hiihtosuunnittelija", persoona-muisti voi vahvistaa tätä roolia ja vaikuttaa vastauksiin niin, että ne vastaavat asiantuntijan sävyä ja tietämystä.

#### Työnkulku-/episodimuisti

Tämä muisti tallentaa sarjan vaiheita, joita agentti suorittaa monimutkaisessa tehtävässä, mukaan lukien onnistumiset ja epäonnistumiset. Se on kuin tiettyjen "jaksojen" tai aiempien kokemusten muistamista oppimista varten.

**Episodimuistin esimerkki**

Jos agentti yritti varata tietyn lennon mutta se epäonnistui saatavuuden puutteen vuoksi, episodimuisti voisi tallentaa tämän epäonnistumisen, jolloin agentti voi yrittää vaihtoehtoisia lentoja tai informoida käyttäjää ongelmasta paremmin seuraavalla yrityksellä.

#### Entiteettimuisti

Tämä sisältää tiettyjen entiteettien (kuten ihmisten, paikkojen tai asioiden) ja tapahtumien poimimista ja muistamista keskusteluista. Se antaa agentille mahdollisuuden rakentaa jäsennelty ymmärrys keskustelun keskeisistä elementeistä.

**Entiteettimuistin esimerkki**

Keskustelusta menneestä matkasta agentti saattaa poimia entiteeteiksi "Pariisi", "Eiffel-torni" ja "illallinen Le Chat Noir -ravintolassa". Tulevassa vuorovaikutuksessa agentti voisi muistaa "Le Chat Noir" ja tarjoutua tekemään uuden varauksen sinne.

#### Jäsennelty RAG (Retrieval Augmented Generation)

Vaikka RAG on laajempi tekniikka, "jäsennelty RAG" korostetaan tehokkaana muistiteknologiana. Se poimii tiivistä, jäsenneltyä tietoa eri lähteistä (keskustelut, sähköpostit, kuvat) ja käyttää sitä parantaakseen tarkkuutta, palautusta ja vasteiden nopeutta. Toisin kuin perinteinen RAG, joka nojaa pelkästään semanttiseen samankaltaisuuteen, jäsennelty RAG hyödyntää tiedon sisäistä rakennetta.

**Jäsennellyn RAG:n esimerkki**

Pelkkien avainsanojen vertailun sijaan jäsennelty RAG voisi jäsentää lennon tiedot (kohde, päivämäärä, aika, lentoyhtiö) sähköpostista ja tallentaa ne rakenteellisella tavalla. Tämä mahdollistaa täsmällisiä kyselyjä kuten "Minkä lennon varasin Pariisiin tiistaina?"

## Muistin toteuttaminen ja tallentaminen

Muistin toteuttaminen tekoälyagenteille sisältää järjestelmällisen prosessin **muistinhallintaa**, joka kattaa muistien luomisen, tallentamisen, hakemisen, integroinnin, päivittämisen ja jopa "unohtamisen" (tai poistamisen). Haku on erityisen ratkaiseva osa.

### Erikoistuneet muistityökalut

#### Mem0

Yksi tapa tallentaa ja hallita agentin muistia on käyttää erikoistuneita työkaluja kuten Mem0. Mem0 toimii pysyvänä muistikerroksena, jonka avulla agentit voivat palauttaa relevantteja vuorovaikutuksia, tallentaa käyttäjäasetuksia ja faktuaalista kontekstia sekä oppia onnistumisista ja epäonnistumisista ajan myötä. Ajatuksena on, että tilattomat agentit muuttuvat tilallisiksi.

Se toimii **kahden vaiheen muistiputken kautta: poiminta ja päivitys**. Ensin agentin ketjuun lisätyt viestit lähetetään Mem0-palveluun, joka käyttää Large Language Model (LLM) -mallia keskusteluhistorian tiivistämiseen ja uusien muistien poimintaan. Tämän jälkeen LLM-ohjattu päivitysvaihe päättää, lisätäänkö, muokataanko vai poistetaanko näitä muistoja, tallentaen ne hybridiin tietokantaan, joka voi sisältää vektori-, graafi- ja avain-arvo -tietokantoja. Tämä järjestelmä tukee myös erilaisia muistityyppejä ja voi sisällyttää graafimuistin entiteettien välisen suhteen hallintaan.

#### Cognee

Toinen tehokas lähestymistapa on käyttää **Cognee**a, avointa lähdekoodia olevaa semanttista muistia tekoälyagenteille, joka muuntaa jäsennellyn ja jäsentämättömän datan kyseltäviksi tietämyskaavioiksi, joita tukevat upotukset. Cognee tarjoaa **kaksoistallennusarkkitehtuurin**, joka yhdistää vektorisimilariteetinhakuun ja graafirakenteisiin perustuvat suhteet, mahdollistaen agenttien ymmärtää paitsi mikä tieto on samankaltaista, myös miten käsitteet liittyvät toisiinsa.

Se loistaa **hybridihakussa**, joka yhdistää vektorisamanlaisuuden, graafirakenteen ja LLM-päättelyn - raakadatan hakiusta graafitietoiseen kysymyksenratkaisuun. Järjestelmä ylläpitää **elävää muistia**, joka kehittyy ja kasvaa samalla kun se pysyy kyseltävänä yhtenä yhdistettynä kaaviona, tukien sekä lyhyen aikavälin istuntokontekstia että pitkäaikaista pysyvää muistia.

Cognee-muistikirjaopas ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstroi tämän yhdistetyn muistikerroksen rakentamista, käytännön esimerkein moninaisten datalähteiden vastaanottamisesta, tietämyskaavion visualisoinnista ja erilaisten hakustrategioiden soveltamisesta agentin tarpeiden mukaisesti.

### Muistin tallentaminen RAG:lla

Erikoistuneiden muistityökalujen kuten Mem0:n lisäksi voit hyödyntää vankkoja hakupalveluja kuten **Azure AI Searchia muistien tallennuksen ja hakemisen taustajärjestelmänä**, erityisesti jäsenneltyä RAGia varten.

Tämä antaa sinun perustaa agentin vastaukset omaan dataasi, varmistaen osuvammat ja tarkemmat vastaukset. Azure AI Searchia voidaan käyttää tallentamaan käyttäjäkohtaisia matkamuistoja, tuotekatalogeja tai mitä tahansa muuta toimialakohtaista tietoa.

Azure AI Search tukee ominaisuuksia kuten **jäsennelty RAG**, joka erottuu kyvyllään poimia ja hakea tiivistä, jäsenneltyä tietoa suurista tietoaineistoista kuten keskusteluhistoriasta, sähköposteista tai jopa kuvista. Tämä tarjoaa "inhimillistä ylittävää" tarkkuutta ja palautuskykyä verrattuna perinteisiin tekstin paloitteluun ja upotuksiin perustuviin lähestymistapoihin.

## Tekoälyagenttien itseään parantaminen

Yleinen malli itseään parantaville agenteille sisältää **"tietämysagentin"** käyttöönoton. Tämä erillinen agentti seuraa pääkeskustelua käyttäjän ja ensisijaisen agentin välillä. Sen rooli on:

1. **Tunnistaa arvokas tieto**: Päätellä, onko keskustelun osa tallentamisen arvoista yleisenä tietona tai tiettynä käyttäjämieltymyksenä.

2. **Poimia ja tiivistää**: Uuttää keskustelusta oleellinen oppi tai mieltymys.

3. **Tallentaa tietokantaan**: Säilyttää tämä poimittu tieto usein vektoritietokannassa, jotta se voidaan hakea myöhemmin.

4. **Täydentää tulevia kyselyjä**: Kun käyttäjä aloittaa uuden kyselyn, tietämysagentti hakee relevanttia tallennettua tietoa ja liittää sen käyttäjän kehotteeseen, tarjoten ensisijaiselle agentille tärkeän kontekstin (samankaltainen kuin RAG).

### Optimoinnit muistiin

• **Latenssin hallinta**: Käyttäjävuorovaikutusten hidastumisen välttämiseksi voi käyttää halvempa, nopeampaa mallia tarkistamaan nopeasti, onko tieto tallentamisen tai hakemisen arvoista, ja kutsua monimutkaisempi poiminta/hakuprosessi vain tarvittaessa.

• **Tietokannan ylläpito**: Kasvavassa tietokannassa harvemmin käytetty tieto voidaan siirtää "kylmäsäilytykseen" kustannusten hallitsemiseksi.

## Onko sinulla lisää kysymyksiä agenttien muistista?

Liity [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) -yhteisöön tavata muita oppijoita, osallistua toimistoaikoihin ja saada vastauksia AI Agents -kysymyksiisi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Vastuuvapauslauseke:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen omaa kieltä pidetään määräävänä lähteenä. Tärkeän tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinkäsityksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->