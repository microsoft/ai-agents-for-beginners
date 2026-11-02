# Muisti tekoälyagentteja varten 
[![Agent Memory](../../../translated_images/fi/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Kun puhutaan tekoälyagenttien ainutlaatuisista eduista, keskustellaan pääasiassa kahdesta asiasta: kyvystä kutsua työkaluja tehtävien suorittamiseksi ja kyvystä parantaa itseään ajan myötä. Muisti on itsensä parantavan agentin luomisen perusta, joka voi tarjota parempia kokemuksia käyttäjillemme.

Tässä oppitunnissa tarkastelemme, mitä muisti tarkoittaa tekoälyagenteille ja kuinka voimme hallita sitä ja käyttää sitä sovellustemme hyödyksi.

## Johdanto

Tässä oppitunnissa käsitellään:

• **Tekoälyagentin muistin ymmärtäminen**: Mitä muisti on ja miksi se on keskeinen agentteja varten.

• **Muistin toteuttaminen ja tallentaminen**: Käytännön menetelmät muistikykenevyys lisäämiseksi tekoälyagentteihisi, keskittyen lyhyen ja pitkän aikavälin muistiin.

• **Tekoälyagenttien itseparantaminen**: Kuinka muisti mahdollistaa agenttien oppimisen aiemmista vuorovaikutuksista ja parantamisen ajan mittaan.

## Saatavilla olevat toteutukset

Tämä oppitunti sisältää kaksi kattavaa muistikirjaopastusta:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Toteuttaa muistin käyttämällä Mem0:aa ja Azure AI Searchia Microsoft Agent Frameworkin kanssa

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Toteuttaa jäsennellyn muistin käyttämällä Cogneeta, itsestään rakentuva tietämyskaavio upotusten pohjalta, kaavion visualisointi ja älykäs haku

## Oppimistavoitteet

Oppitunnin suorittamisen jälkeen osaat:

• **Erotella erilaiset tekoälyagentin muistin tyypit**, mukaan lukien työmuisti, lyhytaikainen ja pitkäaikainen muisti sekä erikoistuneet muodot kuten persoonamuisti ja episodimuisti.

• **Toteuttaa ja hallita lyhytaikaista ja pitkäaikaista muistia tekoälyagenteille** käyttämällä Microsoft Agent Frameworkia, hyödyntäen työkaluja kuten Mem0, Cognee, Whiteboard-muisti ja integrointi Azure AI Searchiin.

• **Ymmärtää itseään parantavien tekoälyagenttien periaatteet** ja kuinka vahvat muistinhallintajärjestelmät edesauttavat jatkuvaa oppimista ja sopeutumista.

## Tekoälyagentin muistin ymmärtäminen

Ydinsisältönä **tekoälyagentin muisti viittaa mekanismeihin, joiden avulla agentit voivat säilyttää ja hakea tietoa**. Tämä tieto voi olla keskustelun yksityiskohtia, käyttäjän mieltymyksiä, aiempia toimintoja tai jopa opittuja malleja.

Ilman muistia tekoälysovellukset ovat usein tilattomia, mikä tarkoittaa, että jokainen vuorovaikutus aloitetaan alusta eikä aiempaa kontekstia tai mieltymyksiä muisteta.

### Miksi muisti on tärkeää?

Agentin älykkyys liittyy syvästi kykyynsä muistaa ja hyödyntää aiempaa tietoa. Muistin avulla agentit voivat olla:

• **Pohdiskelevia**: Oppimassa aiemmista toiminnoista ja tuloksista.

• **Vuorovaikutteisia**: Ylläpitämään kontekstia käynnissä olevan keskustelun aikana.

• **Proaktiivisia ja reaktiivisia**: Ennakoimaan tarpeita tai vastaamaan tilanteen mukaan historiatiedon perusteella.

• **Autonomisia**: Toimimaan itsenäisemmin hyödyntämällä tallennettua tietoa.

Muistin toteuttamisen tavoitteena on tehdä agenteista **luotettavampia ja kykenevämpiä**.

### Muistin tyypit

#### Työmuisti

Ajattele työmuistia muistilappuna, jota agentti käyttää yhdessä meneillään olevassa tehtävässä tai ajatteluprosessissa. Se pitää hallussaan välittömän tiedon, joka tarvitaan seuraavaan vaiheeseen.

Tekoälyagenteilla työmuisti tallentaa yleensä olennaisimmat tiedot keskustelusta, vaikka koko chat-historia olisi pitkä tai katkaistu. Keskitytään keskeisiin elementteihin kuten vaatimukset, ehdotukset, päätökset ja toiminnot.

**Työmuistin esimerkki**

Matkavarausagentissa työmuisti voisi tallentaa käyttäjän nykyisen pyynnön, kuten "Haluan varata matkan Pariisiin". Tämä erityinen vaatimus pidetään agentin välittömässä kontekstissa, ohjaamaan nykyistä vuorovaikutusta.

#### Lyhytaikainen muisti

Tämä muistin tyyppi säilyttää tietoa yhden keskustelun tai istunnon ajan. Se on nykyisen chatin konteksti, jonka avulla agentti voi viitata aiempiin vuorovaikutuksen vaiheisiin.

[Microsoft Agent Framework](https://github.com/microsoft/agent-framework) Python SDK:n esimerkeissä tämä vastaa `AgentSession`-oliota, joka luodaan `agent.create_session()` -funktiolla. Istunto toimii kehyksen sisäisenä lyhytaikaisena muistina: se pitää keskustelukontekstia saatavilla kun samaa istuntoa käytetään uudelleen, mutta tätä kontekstia ei säilytetä istunnon päätyttyä tai sovelluksen uudelleenkäynnistyksessä. Pitkäaikaiseen muistiin tallennetaan faktat ja mieltymykset, jotka pitää säilyttää istuntojen yli, yleensä tietokannan, vektori-indeksin tai muun pysyvän tallennustilan avulla.

**Lyhytaikaisen muistin esimerkki**

Jos käyttäjä kysyy: "Paljonko lento Pariisiin maksaa?" ja sen jälkeen jatkaa: "Entä majoitus sinne?", lyhytaikainen muisti varmistaa, että agentti tietää "sinne" viittaavan "Pariisiin" samassa keskustelussa.

#### Pitkäaikainen muisti

Tämä on tietoa, joka säilyy useiden keskustelujen tai istuntojen ajan. Se antaa agentille mahdollisuuden muistaa käyttäjän mieltymykset, aiemmat vuorovaikutukset tai yleisen tiedon pitkällä aikavälillä. Tämä on tärkeää henkilökohtaisessa palvelussa.

**Pitkäaikaisen muistin esimerkki**

Pitkäaikainen muisti voisi tallentaa tiedon, että "Ben pitää hiihtämisestä ja ulkoilusta, hän tykkää kahvista vuoristonäkymällä ja haluaa välttää vaativia hiihtorinteitä aiemman vamman vuoksi". Tämä tieto, opittu aiemmista vuorovaikutuksista, vaikuttaa suosituksiin tulevissa matkan suunnittelun istunnoissa, tehden niistä hyvin henkilökohtaisia.

#### Persoonamuisti

Tämä erikoistunut muistityyppi auttaa agenttia kehittämään johdonmukaisen "persoonallisuuden" tai "hahmon". Se antaa agentille mahdollisuuden muistaa tietoja itsestään tai roolistaan, tehden vuorovaikutuksesta sujuvampaa ja tarkennettua.

**Persoonamuistin esimerkki**
Jos matkatoimisto on suunniteltu olemaan "asiantunteva hiihtosuunnittelija", persoonamuisti voi vahvistaa tätä roolia vaikuttaen vastauksiin asiantuntijan äänensävyllä ja tiedoilla.

#### Työnkulku-/episodimuisti

Tämä muisti tallentaa agentin tekemien vaiheiden sarjan monimutkaisessa tehtävässä, mukaan lukien onnistumiset ja epäonnistumiset. Se on kuin muistaa tiettyjä "jaksoja" tai aiempia kokemuksia oppiakseen niistä.

**Episodimuistin esimerkki**

Jos agentti yritti varata tietyn lennon, mutta yritys epäonnistui saatavuusongelman vuoksi, episodimuisti voisi tallentaa tämän epäonnistumisen, antaen agentille mahdollisuuden kokeilla vaihtoehtoisia lentoja tai tiedottaa käyttäjälle asiasta paremmin seuraavalla yrityksellä.

#### Entiteettimuisti

Tämä sisältää keskeisten entiteettien (kuten ihmisten, paikkojen tai esineiden) ja tapahtumien poiminnan ja muistamisen keskusteluista. Se antaa agentin rakentaa jäsennellyn ymmärryksen käsitellyistä keskeisistä elementeistä.

**Entiteettimuistin esimerkki**

Keskustelusta aiemmasta matkasta agentti saattaa poimia "Pariisin", "Eiffel-tornin" ja "illallisen Le Chat Noir -ravintolassa" entiteeteiksi. Tulevassa vuorovaikutuksessa agentti voisi muistaa "Le Chat Noir":n ja tarjoutua tekemään uuden varauksen sinne.

#### Jäsennelty RAG (Retrieval Augmented Generation)

Vaikka RAG on laajempi tekniikka, "Jäsennelty RAG" korostetaan tehokkaana muistiteknologiana. Se poimii tiivistä, jäsenneltyä tietoa eri lähteistä (keskustelut, sähköpostit, kuvat) ja käyttää sitä vastausten tarkkuuden, haun ja nopeuden parantamiseen. Toisin kuin klassinen RAG, joka perustuu pelkkään semanttiseen samankaltaisuuteen, Jäsennelty RAG käyttää tiedon sisäistä rakennetta.

**Jäsennetyn RAG:in esimerkki**

Pelkkien avainsanojen vastaamisen sijaan Jäsennelty RAG voisi purkaa lentotiedot (kohde, päivämäärä, aika, lentoyhtiö) sähköpostista ja tallentaa ne jäsennellyllä tavalla. Tämä mahdollistaa tarkat haut kuten "Mikä lento varasin Pariisiin tiistaina?"

## Muistin toteuttaminen ja tallentaminen

Muistin toteuttaminen tekoälyagenteille sisältää järjestelmällisen prosessin, joka sisältää **muistinhallinnan**: tiedon luomisen, tallentamisen, hakemisen, integroinnin, päivittämisen ja jopa "unohtamisen" (tai poistamisen). Hakeminen on erityisen tärkeä osa.

### Erikoistuneet muistit työkalut

#### Mem0

Yksi tapa tallentaa ja hallita agentin muistia on käyttää erikoistuneita työkaluja kuten Mem0. Mem0 toimii pysyvänä muistikerroksena, jonka avulla agentit voivat muistella olennaisia vuorovaikutuksia, tallentaa käyttäjän mieltymyksiä ja tosiasiallista kontekstia sekä oppia onnistumisista ja epäonnistumisista ajan myötä. Ajatus on, että tilattomat agentit muuttuvat tilallisiksi.

Se toimii **kaksivaiheisella muistiputkella: poiminta ja päivitys**. Ensin viestit, jotka lisätään agentin ketjuun, lähetetään Mem0-palveluun, joka käyttää suurta kielimallia (LLM) keskusteluhistorian tiivistämiseen ja uusien muistojen poimimiseen. Sen jälkeen LLM-ohjattu päivitysvaihe päättää, lisätäänkö, muokataanko tai poistetaanko nämä muistot, tallentaen ne hybridi tietokantaan, joka voi sisältää vektori-, graafi- ja avain-arvo -tietokantoja. Tämä järjestelmä tukee myös erilaisia muistityyppejä ja voi integroida graafimuistin hallitsemaan entiteettien välisiä suhteita.

#### Cognee

Toinen tehokas lähestymistapa on käyttää **Cogneeta**, avoimen lähdekoodin semanttista muistia tekoälyagenteille, joka muuntaa rakenteellista ja rakenteetonta dataa kyselykelpoisiksi tietämyskaavioiksi, joita tukee upotukset. Cognee tarjoaa **kaksikerroksisen arkkitehtuurin**, joka yhdistää vektorihakemisen graafisuhteisiin, mahdollistaen agenttien ymmärtää paitsi mitä tieto on samankaltaista, myös miten käsitteet liittyvät toisiinsa.

Se loistaa **hybridihakemisessa**, joka yhdistelee vektorisamanlaisuutta, graafirakennetta ja LLM-päättelyä - raakapoiminnasta graafitietoiseen kysymysten ratkaisuun. Järjestelmä ylläpitää **elävää muistia**, joka kehittyy ja kasvaa mutta pysyy kyselykelpoisena yhtenä yhdistettynä kaaviona, tukien sekä lyhytaikaista istuntokontekstia että pitkäaikaista pysyvää muistia.

Cognee-muistikirjaopastus ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) havainnollistaa tämän yhtenäisen muistikerroksen rakentamista käytännön esimerkkien avulla, joissa eri datalähteitä sisään syötetään, tietämyskaavio visualisoidaan ja kyselyitä tehdään erilaisilla hakumenetelmillä, jotka on räätälöity tiettyjen agenttitarpeiden mukaan.

### Muistin tallentaminen RAG:lla

Erityistyökalujen kuten Mem0 lisäksi voit hyödyntää vankkoja hakupalveluita kuten **Azure AI Searchia muistojen tallentamisen ja hakemisen taustajärjestelmänä**, erityisesti jäsennetylle RAG:lle.

Tämä antaa mahdollisuuden perustaa agentin vastaukset omiin tietoihisi varmistaen osuvammat ja tarkemmat vastaukset. Azure AI Search voi tallentaa käyttäjäkohtaisia matkamuistoja, tuotekatalogeja tai muuta erityisalaista tietoa.

Azure AI Search tukee ominaisuuksia kuten **Jäsennelty RAG**, joka loistaa tiiviin, jäsennetyn tiedon poiminnassa ja haussa suurista tietokokonaisuuksista kuten keskusteluhistoriat, sähköpostit tai kuvat. Tämä tarjoaa "yliluonnollisen tarkkuuden ja haun" verrattuna perinteisiin tekstin paloitteluun ja upotuksiin.

## Tekoälyagenttien itseparantaminen

Yleinen malli itseparantaville agenteille sisältää **"tietämysagentin"** käyttöönoton. Tämä erillinen agentti tarkkailee varsinaisen agentin ja käyttäjän välistä pääkeskustelua. Sen rooli on:

1. **Tunnistaa arvokas tieto**: Selvittää, kannattaako jokin keskustelun osa tallentaa yleisenä tietona tai tiettynä käyttäjän mieltymyksenä.

2. **Uuttaminen ja tiivistäminen**: Erotella keskustelun oleellinen oppi tai mieltymys.

3. **Tallentaminen tietämyspohjaan**: Säilyttää poimittu tieto, usein vektoritietokannassa, jotta se voidaan hakea myöhemmin.

4. **Lisätä tuleviin hakuihin**: Kun käyttäjä tekee uuden haun, tietämysagentti hakee relevantin tallennetun tiedon ja liittää sen käyttäjän kehotteeseen, tarjoten tärkeän kontekstin pääagentille (samankaltainen kuin RAG).

### Muistin optimoinnit

• **Viiveen hallinta**: Välttää hidastamasta käyttäjävuorovaikutuksia käyttämällä aluksi halvempi ja nopeampi malli nopeasti tarkistamaan, onko tieto tallentamisen tai haun arvoista, käyttämällä monimutkaisempaa poiminta-/hakuprosessia vain tarvittaessa.

• **Tietämyskantan ylläpito**: Kasvavassa tietämyskannassa harvemmin käytetyt tiedot voidaan siirtää "kylmäsäilytykseen" kustannusten hallintaamiseksi.

## Onko sinulla lisää kysymyksiä agentin muistista?

Liity [Microsoft Foundry Discordiin](https://discord.com/invite/ATgtXmAS5D) tavata muita oppijoita, osallistua toimistotunteihin ja saada vastaukset tekoälyagenttien kysymyksiisi.
## Edellinen oppitunti

[Konstekstin suunnittelu tekoälyagenteille](../12-context-engineering/README.md)

## Seuraava oppitunti

[Microsoft Agent Frameworkin tutkiminen](../14-microsoft-agent-framework/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->