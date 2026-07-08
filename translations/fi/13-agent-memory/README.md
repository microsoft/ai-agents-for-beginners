# Muisti tekoälyagentteille
[![Agent Memory](../../../translated_images/fi/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Kun keskustellaan tekoälyagenttien ainutlaatuisista eduista, kaksi asiaa nousevat päällimmäisinä esiin: kyky käyttää työkaluja tehtävien suorittamiseen ja kyky kehittyä ajan myötä. Muisti on itsensä parantavan agentin luomisen perusta, joka pystyy luomaan parempia käyttökokemuksia käyttäjillemme.

Tässä oppitunnissa tarkastelemme, mitä muisti tarkoittaa tekoälyagenteille ja miten voimme hallita sitä ja käyttää sitä sovellustemme hyödyksi.

## Johdanto

Tämä oppitunti kattaa:

• **Tekoälyagentin muistin ymmärtäminen**: Mitä muisti on ja miksi se on olennaista agenteille.

• **Muistin toteuttaminen ja tallentaminen**: Käytännön menetelmät muistin lisäämiseksi tekoälyagenteille, keskittyen lyhyt- ja pitkäkestoiseen muistiin.

• **Tekoälyagenttien itsensä parantaminen**: Miten muisti mahdollistaa agenttien oppimisen menneistä vuorovaikutuksista ja kehittymisen ajan myötä.

## Saatavilla olevat toteutukset

Tämä oppitunti sisältää kaksi kattavaa muistia käsittelevää muistiinpanotutoriaalia:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Toteuttaa muistin käyttäen Mem0:aa ja Azure AI Searchia Microsoft Agent Frameworkilla

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Toteuttaa jäsennellyn muistin Cognee:lla, automaattisesti rakentaen tietämysgraafin embeddings-pohjaisesti, visualisoiden verkkoa ja älykkään palautuksen

## Oppimistavoitteet

Tämän oppitunnin jälkeen osaat:

• **Erotella eri tekoälyagentin muistin tyypit** mukaan lukien työmuisti, lyhytkestoinen ja pitkäkestoinen muisti sekä erikoistuneet muodot kuten persona- ja episodinen muisti.

• **Toteuttaa ja hallita lyhyt- ja pitkäkestoista muistia tekoälyagenteille** käyttäen Microsoft Agent Frameworkia ja hyödyntäen työkaluja kuten Mem0, Cognee, Whiteboard-muistia sekä integroimalla Azure AI Searchiin.

• **Ymmärtää itsensä parantavien tekoälyagenttien periaatteet** ja miten vankat muistin hallintajärjestelmät edesauttavat jatkuvaa oppimista ja sopeutumista.

## Tekoälyagentin muistin ymmärtäminen

Ydinasiallisesti **tekoälyagenttien muisti viittaa mekanismeihin, jotka antavat niiden säilyttää ja palauttaa tietoa**. Tämä tieto voi olla yksityiskohtia keskustelusta, käyttäjän mieltymyksiä, aiempia toimintoja tai opittuja kaavoja.

Ilman muistia tekoälysovellukset ovat usein tilattomia, eli jokainen vuorovaikutus alkaa alusta. Tämä johtaa toistuviin ja turhauttaviin käyttökokemuksiin, joissa agentti "unohtaa" aiemman kontekstin tai mieltymykset.

### Miksi muisti on tärkeä?

Agentin älykkyys liittyy syvästi sen kykyyn palauttaa ja käyttää aiempaa tietoa. Muisti mahdollistaa agenttien olevan:

• **Heijastelevia**: Oppimaan menneistä toimista ja tuloksista.

• **Vuorovaikutteisia**: Säilyttämään kontekstin käydyssä keskustelussa.

• **Etenevä ja reaktiivinen**: Ennakoimaan tarpeita tai reagoimaan asianmukaisesti aiemman datan perusteella.

• **Autonomisia**: Toimimaan itsenäisemmin hyödyntämällä tallennettua tietoa.

Muistin toteuttamisen tavoitteena on tehdä agenteista **luotettavampia ja kykenevämpiä**.

### Muistin tyypit

#### Työmuisti

Ajattele tätä kuin luonnospaperia, jota agentti käyttää yksittäisen käynnissä olevan tehtävän tai ajatusprosessin aikana. Se pitää väliaikaisesti tallessa sen hetken tiedot seuraavaa askelta varten.

Tekoälyagenteille työmuisti tallentaa usein olennaisimmat tiedot keskustelusta, vaikka koko keskusteluhistoria olisi pitkä tai katkaistu. Se keskittyy keskeisiin elementteihin kuten vaatimuksiin, ehdotuksiin, päätöksiin ja toimiin.

**Työmuistin esimerkki**

Matkanvarausagentissa työmuisti voisi tallentaa käyttäjän nykyisen pyynnön, esimerkiksi "Haluan varata matkan Pariisiin". Tämä erityinen vaatimus säilyy agentin välittömässä kontekstissa ohjaamaan nykyistä vuorovaikutusta.

#### Lyhytkestoinen muisti

Tämä muistin tyyppi säilyttää tietoa yhden keskustelun tai istunnon ajan. Se on nykyisen keskustelun konteksti, jonka avulla agentti voi viitata aiempiin vuoroihin dialogissa.

Microsoftin Agent Frameworkin Python SDK -näytteissä tämä vastaa `AgentSession`-oliota, joka luodaan `agent.create_session()`-komennolla. Istunto on frameworkin sisäänrakennettu lyhytkestoinen muisti: se pitää keskustelukontekstin aktiivisena kyseisen istunnon ajan, mutta se ei tallennu istunnon päättyessä tai sovelluksen käynnistyessä uudelleen. Käytä pitkäkestoista muistia faktoille ja mieltymyksille, jotka pitää säilyä istuntojen yli, tyypillisesti tietokannan, vektori-indeksin tai muun pysyvän tallennustilan kautta.

**Lyhytkestoisen muistin esimerkki**

Jos käyttäjä kysyy: "Paljonko lento Pariisiin maksaa?" ja jatkaa myöhemmin "Entä majoitus siellä?", lyhytkestoinen muisti varmistaa, että agentti ymmärtää "sieltä" viittaavan "Pariisiin" saman keskustelun aikana.

#### Pitkäkestoinen muisti

Tämä on tietoa, joka säilyy useiden keskusteluiden tai istuntojen yli. Se antaa agenteille mahdollisuuden muistaa käyttäjän mieltymykset, historialliset vuorovaikutukset tai yleisen tiedon pitkällä aikavälillä. Tämä on tärkeää personoinnissa.

**Pitkäkestoisen muistin esimerkki**

Pitkäkestoinen muisti saattaa tallentaa esimerkiksi, että "Ben nauttii laskettelusta ja ulkoilusta, pitää kahvista vuoristonäkymällä ja haluaa välttää edistyneitä rinteitä aiemman vamman vuoksi". Tämä tieto, opittu aiemmista vuorovaikutuksista, vaikuttaa tulevan matkan suunnittelun suosituksiin tehden niistä erittäin henkilökohtaisia.

#### Persona-muisti

Tämä erikoistunut muistin muoto auttaa agenttia kehittämään yhtenäisen "persoonallisuuden" tai "roolin". Se antaa agentille mahdollisuuden muistaa tietoja itsestään tai roolistaan, tehden vuorovaikutuksesta sujuvampaa ja kohdennetumpaa.

**Persona-muistin esimerkki**
Jos matkatoimistoagentti on suunniteltu olevan "asiantuntijalaskettelusuunnittelija", persona-muisti voi vahvistaa tämän roolin, vaikuttaen vastauksiin asiantuntijan sävyn ja tiedon mukaisesti.

#### Työnkulku/Episodinen muisti

Tämä muisti tallentaa agentin tekemien monimutkaisten tehtävien sarjan vaiheet, mukaan lukien onnistumiset ja epäonnistumiset. Se on kuin muistaisi tiettyjä "jaksoja" tai menneitä kokemuksia oppiakseen niistä.

**Episodisen muistin esimerkki**

Jos agentti yritti varata tietyn lennon, mutta epäonnistui sen saatavuuden puutteen vuoksi, episodinen muisti voisi tallentaa tämän epäonnistumisen, jolloin agentti voi kokeilla vaihtoehtoisia lentoja tai informoida käyttäjää ongelmasta paremmin seuraavalla yrityksellä.

#### Entiteettimuisti

Tämä käsittää erityisten entiteettien (kuten ihmiset, paikat tai asiat) ja tapahtumien poimimisen ja muistamisen keskusteluista. Se antaa agentille mahdollisuuden rakentaa jäsennelty ymmärrys käsitellyistä keskeisistä elementeistä.

**Entiteettimuistin esimerkki**

Keskustelusta menneestä matkasta agentti voi poimia entiteetteinä "Pariisin", "Eiffel-tornin" ja "illallisen Le Chat Noir -ravintolassa". Tulevassa vuorovaikutuksessa agentti voisi muistaa "Le Chat Noirin" ja tarjoutua tekemään uuden varauksen sinne.

#### Jäsennelty RAG (Retrieval Augmented Generation)

Vaikka RAG on laajempi tekniikka, "Jäsennelty RAG" korostuu tehokkaana muistitekniikkana. Se poimii tiivistä, jäsenneltyä tietoa eri lähteistä (keskustelut, sähköpostit, kuvat) ja käyttää sitä tarkkuuden, haun ja reagoinnin nopeuden parantamiseen. Toisin kuin klassinen RAG, joka perustuu pelkkään semanttiseen samankaltaisuuteen, Jäsennelty RAG hyödyntää tiedon omaa rakennetta.

**Jäsennellyn RAG:n esimerkki**

Sen sijaan, että pelkästään etsittäisiin avainsanoja, Jäsennelty RAG voisi jäsentää lentotiedot (kohde, päivämäärä, aika, lentoyhtiö) sähköpostista ja tallentaa ne rakenteellisessa muodossa. Tämä mahdollistaa tarkat kyselyt kuten "Mikä lento varattiin Pariisiin tiistaina?"

## Muistin toteuttaminen ja tallentaminen

Muistin toteuttaminen tekoälyagenteille sisältää systemaattisen **muistinhallinnan** prosessin, johon kuuluu tiedon luominen, tallentaminen, hakeminen, integrointi, päivittäminen ja jopa "unohtaminen" (tai poistaminen). Tiedon haku on erityisen tärkeässä roolissa.

### Erikoistuneet muistityökalut

#### Mem0

Yksi tapa tallentaa ja hallita agentin muistia on käyttää erikoistuneita työkaluja kuten Mem0. Mem0 toimii pysyvänä muistikerroksena, joka antaa agenteille mahdollisuuden palauttaa merkitykselliset vuorovaikutukset, tallentaa käyttäjän mieltymykset ja faktuaalisen kontekstin sekä oppia menestyksistä ja epäonnistumisista ajan myötä. Ajatus on, että tilattomat agentit muuttuvat tilallisiksi.

Se toimii **kahden vaiheen muistiputken** kautta: poiminta ja päivitys. Ensiksi agentin ketjuun lisätyt viestit lähetetään Mem0-palveluun, joka käyttää suurta kielimallia (LLM) keskusteluhistorian tiivistämiseen ja uusien muistojen poimintaan. Tämän jälkeen LLM-pohjainen päivitysvaihe päättää, lisätäänkö, muokataanko vai poistetaanko nämä muistot, tallentaen ne hybriditietokantaan, joka voi sisältää vektori-, graafi- ja avain-arvo-tietokantoja. Tämä järjestelmä tukee myös eri muistityyppejä ja voi sisältää graafimuistin hallitsemaan enteettien välisiä suhteita.

#### Cognee

Toinen voimakas lähestymistapa on käyttää **Cognee**a, avoimen lähdekoodin semanttista muistia tekoälyagenteille, joka muuttaa jäsennellyn ja jäsentämättömän datan kyseltäviksi tietämysgraafeiksi embeddings-pohjaisesti. Cognee tarjoaa **kaksoistallennusarkkitehtuurin**, joka yhdistää vektorisamankaltaisuushakua graafisuhteisiin, antaen agenteille kyvyn ymmärtää paitsi mitä tieto on samankaltaista, myös miten käsitteet liittyvät toisiinsa.

Se loistaa **hybridihakujen** toteutuksissa, jotka yhdistävät vektorihakuja, graafirakenteita ja LLM-päättelyä - raakadatan etsinnästä graafitietoiseen kysymyksenasetteluun. Järjestelmä ylläpitää **elävää muistia**, joka kehittyy ja kasvaa mutta pysyy kyseltävänä yhtenäisenä graafina, tukeen sekä lyhytkestoista istuntokontrkstia että pitkäkestoista pysyvää muistia.

Cognee-muistiinpanotutoriaali ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstroi tämän yhdistetyn muistikerroksen rakentamista, käytännön esimerkkien kera, jotka sisältävät monimuotoisten datalähteiden syöttämisen, tietämysgraafin visualisoinnin ja erilaisilla hakustrategioilla kyselyjen tekemisen, jotka on räätälöity erityistarpeisiin.

### Muistin tallentaminen RAG:lla

Erikoistuneiden muistityökalujen kuten Mem0 lisäksi voit hyödyntää tehokkaita hakupalveluja kuten **Azure AI Searchia muistin tallennuksen ja haun taustalla**, erityisesti jäsennellyssä RAG:ssa.

Tämä antaa mahdollisuuden juurruttaa agenttisi vastaukset omaan dataasi, varmistaen relevantimmat ja tarkimmat vastaukset. Azure AI Searchia voi käyttää tallentamaan käyttäjäkohtaisia matkamuistoja, tuotekatalogeja tai muuta alakohtaista tietämystä.

Azure AI Search tukee ominaisuuksia kuten **Jäsenneltyä RAG:ia**, joka loistaa tiiviin, jäsennellyn tiedon poiminnassa ja haussa suurista aineistoista kuten keskusteluhistoriat, sähköpostit tai jopa kuvat. Tämä tarjoaa "ihmistä ylittävän tarkkuuden ja haun" verrattuna perinteisiin tekstikappaleiden ja embedding-menetelmiin.

## Tekoälyagenttien itsensä parantaminen

Yleinen malli itsensä parantaville agenteille sisältää **”tietämysagentin”** käyttöönoton. Tämä erillinen agentti tarkkailee pääasiallisen agentin ja käyttäjän välistä keskustelua. Sen rooli on:

1. **Tunnistaa arvokas tieto**: Päätellä, onko keskustelun osa syytä tallentaa yleiseksi tiedoksi tai erityiseksi käyttäjän mieltymykseksi.

2. **Poimia ja tiivistää**: Erottaa keskustelusta olennaisen oppimisen tai mieltymyksen.

3. **Tallentaa tietämyspohjaan**: Säilyttää tämän poimitun tiedon, usein vektoripohjaiseen tietokantaan, jotta se voidaan hakea myöhemmin.

4. **Tukea tulevia kyselyjä**: Kun käyttäjä aloittaa uuden kyselyn, tietämysagentti hakee siihen liittyvät tallennetut tiedot ja liittää ne käyttäjän kehotteeseen, tarjoten tärkeän kontekstin pääasialliselle agentille (samankaltainen kuin RAG).

### Muistin optimoinnit

• **Viiveen hallinta**: Käyttämään aluksi halvempaa, nopeampaa mallia nopeasti arvioimaan tiedon arvokkuutta tallentamisen tai haun kannalta, kutsuen monimutkaisempaa poiminta-/hakuprosessia vain tarpeen tullen.

• **Tietämyspohjan ylläpito**: Kasvavalle tietämyspohjalle harvemmin käytetty tieto voidaan siirtää "kylmään varastoon" kustannusten hallitsemiseksi.

## Onko sinulla lisää kysymyksiä agentin muistista?

Liity [Microsoft Foundry Discordiin](https://discord.com/invite/ATgtXmAS5D) tavata muita oppijoita, osallistua toimistoaikoihin ja saada vastauksia tekoälyagenttien kysymyksiin.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->