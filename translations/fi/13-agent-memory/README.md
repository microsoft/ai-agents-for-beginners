<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1923cf93aba522a5f4a493597112a893",
  "translation_date": "2025-09-18T16:15:13+00:00",
  "source_file": "13-agent-memory/README.md",
  "language_code": "fi"
}
-->
# Muisti AI-agentteja varten

Kun keskustellaan AI-agenttien luomisen ainutlaatuisista eduista, kaksi asiaa nousee esiin: kyky käyttää työkaluja tehtävien suorittamiseen ja kyky parantaa itseään ajan myötä. Muisti on keskeinen osa itseään parantavan agentin luomista, joka voi tarjota parempia kokemuksia käyttäjillemme.

Tässä oppitunnissa tarkastelemme, mitä muisti tarkoittaa AI-agenteille ja kuinka voimme hallita ja hyödyntää sitä sovellustemme hyväksi.

## Johdanto

Tämä oppitunti kattaa:

• **AI-agenttien muistin ymmärtäminen**: Mitä muisti on ja miksi se on tärkeää agenteille.

• **Muistin toteuttaminen ja tallentaminen**: Käytännön menetelmiä muistikapasiteetin lisäämiseksi AI-agenteille, keskittyen lyhyt- ja pitkäaikaiseen muistiin.

• **AI-agenttien itseparantaminen**: Kuinka muisti mahdollistaa oppimisen aiemmista vuorovaikutuksista ja parantumisen ajan myötä.

## Oppimistavoitteet

Oppitunnin jälkeen osaat:

• **Erotella AI-agenttien eri muistityypit**, kuten työmuisti, lyhyt- ja pitkäaikainen muisti sekä erikoistuneet muodot, kuten persoonamuisti ja episodinen muisti.

• **Toteuttaa ja hallita lyhyt- ja pitkäaikaista muistia AI-agenteille** käyttämällä Semantic Kernel -kehystä, hyödyntäen työkaluja kuten Mem0 ja Whiteboard-muisti sekä integroimalla Azure AI Searchin kanssa.

• **Ymmärtää itseään parantavien AI-agenttien periaatteet** ja kuinka vahvat muistinhallintajärjestelmät edistävät jatkuvaa oppimista ja sopeutumista.

## AI-agenttien muistin ymmärtäminen

Pohjimmiltaan **muisti AI-agenteille tarkoittaa mekanismeja, jotka mahdollistavat tiedon säilyttämisen ja palauttamisen**. Tämä tieto voi olla yksityiskohtia keskustelusta, käyttäjän mieltymyksiä, aiempia toimia tai jopa opittuja malleja.

Ilman muistia AI-sovellukset ovat usein tilattomia, mikä tarkoittaa, että jokainen vuorovaikutus alkaa alusta. Tämä johtaa toistuvaan ja turhauttavaan käyttäjäkokemukseen, jossa agentti "unohtaa" aiemman kontekstin tai mieltymykset.

### Miksi muisti on tärkeää?

Agentin älykkyys liittyy vahvasti sen kykyyn muistaa ja hyödyntää aiempaa tietoa. Muisti mahdollistaa, että agentit voivat olla:

• **Reflektiivisiä**: Oppia aiemmista toimista ja tuloksista.

• **Vuorovaikutteisia**: Säilyttää kontekstin jatkuvan keskustelun aikana.

• **Proaktiivisia ja reaktiivisia**: Ennakoida tarpeita tai vastata asianmukaisesti historiallisten tietojen perusteella.

• **Autonomisia**: Toimia itsenäisemmin hyödyntämällä tallennettua tietoa.

Muistin toteuttamisen tavoitteena on tehdä agenteista **luotettavampia ja kykenevämpiä**.

### Muistityypit

#### Työmuisti

Ajattele tätä kuin muistilappua, jota agentti käyttää yhden tehtävän tai ajatusprosessin aikana. Se sisältää välittömän tiedon, joka tarvitaan seuraavan askeleen laskemiseen.

AI-agenteille työmuisti tallentaa usein keskustelun olennaisimmat tiedot, vaikka koko keskusteluhistoria olisi pitkä tai katkaistu. Se keskittyy keskeisten elementtien, kuten vaatimusten, ehdotusten, päätösten ja toimien, poimimiseen.

**Työmuistin esimerkki**

Matkavarausagentti voi tallentaa käyttäjän nykyisen pyynnön, kuten "Haluan varata matkan Pariisiin". Tämä erityinen vaatimus pidetään agentin välittömässä kontekstissa ohjaamaan nykyistä vuorovaikutusta.

#### Lyhytaikainen muisti

Tämä muistityyppi säilyttää tiedon yhden keskustelun tai istunnon ajan. Se on nykyisen keskustelun konteksti, joka mahdollistaa agentin viittaamisen aiempiin vuoropuhelun käänteisiin.

**Lyhytaikaisen muistin esimerkki**

Jos käyttäjä kysyy: "Paljonko lento Pariisiin maksaisi?" ja jatkaa: "Entä majoitus siellä?", lyhytaikainen muisti varmistaa, että agentti tietää "siellä" viittaavan "Pariisiin" saman keskustelun aikana.

#### Pitkäaikainen muisti

Tämä on tietoa, joka säilyy useiden keskustelujen tai istuntojen ajan. Se mahdollistaa agenttien muistamaan käyttäjän mieltymykset, historialliset vuorovaikutukset tai yleisen tiedon pitkällä aikavälillä. Tämä on tärkeää personoinnin kannalta.

**Pitkäaikaisen muistin esimerkki**

Pitkäaikainen muisti voi tallentaa, että "Ben nauttii laskettelusta ja ulkoilusta, pitää kahvista vuoristonäkymällä ja haluaa välttää vaativia laskettelurinteitä aiemman loukkaantumisen vuoksi". Tämä tieto, joka on opittu aiemmista vuorovaikutuksista, vaikuttaa suosituksiin tulevissa matkasuunnittelusessioissa, tehden niistä erittäin henkilökohtaisia.

#### Persoonamuisti

Tämä erikoistunut muistityyppi auttaa agenttia kehittämään johdonmukaisen "persoonallisuuden" tai "roolin". Se mahdollistaa agentin muistamaan yksityiskohtia itsestään tai tarkoitetusta roolistaan, tehden vuorovaikutuksesta sujuvampaa ja keskittyneempää.

**Pitkäaikaisen muistin esimerkki**

Jos matkavarausagentti on suunniteltu olemaan "laskettelusuunnittelun asiantuntija", persoonamuisti voi vahvistaa tätä roolia, vaikuttaen sen vastauksiin asiantuntijan sävyllä ja tiedoilla.

#### Työprosessi/Episodinen muisti

Tämä muisti tallentaa agentin suorittamien monimutkaisten tehtävien vaiheet, mukaan lukien onnistumiset ja epäonnistumiset. Se on kuin muistaminen erityisistä "episodeista" tai aiemmista kokemuksista oppimista varten.

**Episodisen muistin esimerkki**

Jos agentti yritti varata tietyn lennon, mutta epäonnistui saatavuuden vuoksi, episodinen muisti voisi tallentaa tämän epäonnistumisen, jolloin agentti voi yrittää vaihtoehtoisia lentoja tai informoida käyttäjää ongelmasta paremmin seuraavalla kerralla.

#### Entiteettimuisti

Tämä liittyy tiettyjen entiteettien (kuten ihmisten, paikkojen tai asioiden) ja tapahtumien poimimiseen ja muistamiseen keskusteluista. Se mahdollistaa agentin rakentamaan rakenteellisen ymmärryksen keskeisistä elementeistä, joista on keskusteltu.

**Entiteettimuistin esimerkki**

Keskustelusta aiemmasta matkasta agentti voi poimia "Pariisi", "Eiffel-torni" ja "illallinen Le Chat Noir -ravintolassa" entiteetteinä. Tulevassa vuorovaikutuksessa agentti voisi muistaa "Le Chat Noir" ja tarjota uutta varausta sinne.

#### Rakenteellinen RAG (Retrieval Augmented Generation)

Vaikka RAG on laajempi tekniikka, "Rakenteellinen RAG" korostetaan tehokkaana muistiteknologiana. Se poimii tiheää, rakenteellista tietoa eri lähteistä (keskustelut, sähköpostit, kuvat) ja käyttää sitä tarkkuuden, muistamisen ja nopeuden parantamiseen vastauksissa. Toisin kuin klassinen RAG, joka perustuu pelkästään semanttiseen samankaltaisuuteen, Rakenteellinen RAG toimii tiedon sisäisen rakenteen kanssa.

**Rakenteellisen RAG:n esimerkki**

Sen sijaan, että vain etsisi avainsanoja, Rakenteellinen RAG voisi jäsentää lentotiedot (kohde, päivämäärä, aika, lentoyhtiö) sähköpostista ja tallentaa ne rakenteellisesti. Tämä mahdollistaa tarkat kyselyt, kuten "Minkä lennon varasin Pariisiin tiistaina?"

## Muistin toteuttaminen ja tallentaminen

Muistin toteuttaminen AI-agenteille sisältää systemaattisen prosessin **muistinhallinnasta**, joka sisältää tiedon tuottamisen, tallentamisen, hakemisen, integroimisen, päivittämisen ja jopa "unohtamisen" (tai poistamisen). Hakeminen on erityisen tärkeä osa.

### Erikoistuneet muistityökalut

Yksi tapa tallentaa ja hallita agentin muistia on käyttää erikoistuneita työkaluja, kuten Mem0. Mem0 toimii pysyvänä muistikerroksena, joka mahdollistaa agenttien muistamaan olennaiset vuorovaikutukset, tallentamaan käyttäjän mieltymykset ja faktuaalisen kontekstin sekä oppimaan onnistumisista ja epäonnistumisista ajan myötä. Ajatuksena on, että tilattomat agentit muuttuvat tilallisiksi.

Se toimii **kaksivaiheisella muistiputkella: poiminta ja päivitys**. Ensin agentin ketjuun lisätyt viestit lähetetään Mem0-palveluun, joka käyttää suurta kielimallia (LLM) keskusteluhistorian tiivistämiseen ja uusien muistojen poimimiseen. Tämän jälkeen LLM-vetoinen päivitysvaihe päättää, lisätäänkö, muokataanko vai poistetaanko nämä muistot, tallentaen ne hybriditietokantaan, joka voi sisältää vektori-, graafi- ja avain-arvo-tietokantoja. Tämä järjestelmä tukee myös erilaisia muistityyppejä ja voi sisältää graafimuistin entiteettien välisten suhteiden hallintaan.

### Muistin tallentaminen RAG:n avulla

Erikoistuneiden muistityökalujen, kuten Mem0:n, lisäksi voit hyödyntää tehokkaita hakupalveluita, kuten **Azure AI Search muistojen tallentamiseen ja hakemiseen**, erityisesti rakenteellista RAG:ia varten.

Tämä mahdollistaa agentin vastausten perustamisen omaan dataasi, varmistaen relevantimmat ja tarkemmat vastaukset. Azure AI Searchia voidaan käyttää käyttäjäkohtaisen matkamuistin, tuotekatalogien tai minkä tahansa muun alakohtaisen tiedon tallentamiseen.

Azure AI Search tukee ominaisuuksia, kuten **Rakenteellinen RAG**, joka erottuu tiheän, rakenteellisen tiedon poimimisessa ja hakemisessa suurista tietoaineistoista, kuten keskusteluhistorioista, sähköposteista tai jopa kuvista. Tämä tarjoaa "ylin tarkkuus ja muistaminen" verrattuna perinteisiin tekstin pilkkomis- ja upotusmenetelmiin.

## AI-agenttien itseparantaminen

Yleinen kaava itseään parantaville agenteille sisältää **"tietoagentin"** käyttöönoton. Tämä erillinen agentti tarkkailee pääkeskustelua käyttäjän ja ensisijaisen agentin välillä. Sen rooli on:

1. **Tunnistaa arvokas tieto**: Päätellä, onko keskustelusta jokin osa tallentamisen arvoista yleisenä tietona tai käyttäjän mieltymyksenä.

2. **Poimia ja tiivistää**: Tislaa keskustelusta olennaiset opit tai mieltymykset.

3. **Tallentaa tietokantaan**: Säilyttää poimittu tieto, usein vektoripohjaisessa tietokannassa, jotta se voidaan hakea myöhemmin.

4. **Laajentaa tulevia kyselyitä**: Kun käyttäjä aloittaa uuden kyselyn, tietoagentti hakee relevantin tallennetun tiedon ja liittää sen käyttäjän pyyntöön, tarjoten tärkeän kontekstin ensisijaiselle agentille (samanlainen kuin RAG).

### Muistin optimoinnit

• **Viiveen hallinta**: Käyttäjävuorovaikutusten hidastumisen välttämiseksi voidaan aluksi käyttää halvempaa ja nopeampaa mallia nopeasti tarkistamaan, onko tieto arvokasta tallentaa tai hakea, ja vasta monimutkaisempi poiminta/hakuprosessi otetaan käyttöön tarvittaessa.

• **Tietokannan ylläpito**: Kasvavaa tietokantaa varten harvemmin käytetty tieto voidaan siirtää "kylmäsäilytykseen" kustannusten hallitsemiseksi.

## Onko sinulla lisää kysymyksiä kontekstisuunnittelusta?

Liity [Azure AI Foundry Discordiin](https://aka.ms/ai-agents/discord) tapaamaan muita oppijoita, osallistumaan toimistoaikoihin ja saamaan vastauksia AI-agentteihin liittyviin kysymyksiisi.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.