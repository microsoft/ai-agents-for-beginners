# Agenttiprotokollien käyttäminen (MCP, A2A ja NLWeb)

[![Agenttiprotokollat](../../../translated_images/fi/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Napsauta yllä olevaa kuvaa katsoaksesi tämän oppitunnin videon)_

Kun tekoälyagenttien käyttö kasvaa, myös protokollien tarve, jotka varmistavat standardoinnin, turvallisuuden ja tukevat avointa innovaatiota, kasvaa. Tässä oppitunnissa käsittelemme kolmea protokollaa, jotka pyrkivät vastaamaan tähän tarpeeseen - Model Context Protocol (MCP), Agent to Agent (A2A) ja Natural Language Web (NLWeb).

## Johdanto

Tässä oppitunnissa käymme läpi:

• Kuinka **MCP** mahdollistaa tekoälyagenttien pääsyn ulkoisiin työkaluihin ja dataan käyttäjän tehtävien suorittamiseksi.

• Kuinka **A2A** mahdollistaa viestinnän ja yhteistyön eri tekoälyagenttien välillä.

• Kuinka **NLWeb** tuo luonnollisen kielen rajapinnat mille tahansa verkkosivustolle, mahdollistaen tekoälyagenttien sisällön löytämisen ja vuorovaikutuksen sen kanssa.

## Oppimistavoitteet

• **Tunnistaa** MCP:n, A2A:n ja NLWebin ydintarkoitus ja hyödyt tekoälyagenttien yhteydessä.

• **Selittää** miten kukin protokolla helpottaa viestintää ja vuorovaikutusta LLM:ien, työkalujen ja muiden agenttien välillä.

• **Tunnistaa** kunkin protokollan erityiset roolit monimutkaisten agenttijärjestelmien rakentamisessa.

## Model Context Protocol

**Model Context Protocol (MCP)** on avoin standardi, joka tarjoaa standardoidun tavan sovelluksille tarjota kontekstia ja työkaluja LLM:ille. Tämä mahdollistaa "universaalin sovittimen" eri tietolähteisiin ja työkaluihin, joihin tekoälyagentit voivat yhdistää johdonmukaisella tavalla.

Tarkastellaan MCP:n komponentteja, etuja suoraan API-käyttöön verrattuna ja esimerkkiä siitä, miten tekoälyagentit voisivat käyttää MCP-palvelinta.

### MCP:n ydinkomponentit

MCP toimii **asiakas-palvelin -arkkitehtuurilla** ja ydinkomponentit ovat:

• **Isännät** ovat LLM-sovelluksia (esimerkiksi koodieditori kuten VSCode), jotka aloittavat yhteydet MCP-palvelimelle.

• **Asiakkaat** ovat isäntäsovelluksen komponentteja, jotka ylläpitävät yksittäisiä yhteyksiä palvelimiin.

• **Palvelimet** ovat kevyitä ohjelmia, jotka tarjoavat tiettyjä kykyjä.

Protokollassa on kolme ydinprimitiveä, jotka ovat MCP-palvelimen kyvykkyyksiä:

• **Työkalut**: Nämä ovat erillisiä toimintoja tai toimintoja, joita tekoälyagentti voi kutsua suorittaakseen tehtävän. Esimerkiksi sääpalvelu voisi tarjota "hanki sää" -työkalun, tai verkkokaupan palvelin voisi tarjota "osta tuote" -työkalun. MCP-palvelimet ilmoittavat kunkin työkalun nimen, kuvauksen ja input/output-skeeman kykyluettelossaan.

• **Resurssit**: Nämä ovat vain-luku -tietokohteita tai dokumentteja, joita MCP-palvelin voi tarjota, ja asiakkaat voivat hakea niitä tarpeen mukaan. Esimerkkejä ovat tiedostojen sisällöt, tietokantarekisterit tai lokitiedostot. Resurssit voivat olla tekstiä (kuten koodi tai JSON) tai binäärisiä (kuten kuvat tai PDF:t).

• **Kehotteet**: Nämä ovat ennalta määriteltyjä malleja, jotka tarjoavat ehdotettuja kehotteita tai keinoja, mahdollistaen monimutkaisempia työnkulkuja.

### MCP:n edut

MCP tarjoaa merkittäviä etuja tekoälyagenteille:

• **Dynaaminen työkalujen löytäminen**: Agentit voivat dynaamisesti saada listan käytettävissä olevista työkaluista palvelimelta, mukaan lukien kuvaukset niiden toiminnoista. Tämä poikkeaa perinteisistä API:ista, joissa usein tarvitaan staattista koodausta integraatioihin, jolloin API:n muutos vaatii koodin päivitystä. MCP tarjoaa "integroi kerran" -lähestymistavan, joka johtaa suurempaan mukautuvuuteen.

• **Yhteentoimivuus eri LLM:ien välillä**: MCP toimii eri LLM:ien välillä, tarjoten joustavuutta vaihtaa ydinmalleja paremman suorituskyvyn arvioimiseksi.

• **Standardoitu turvallisuus**: MCP sisältää standardoidun tunnistautumistavan, mikä parantaa skaalautuvuutta lisättäessä pääsyä lisä-MCP-palvelimiin. Tämä on yksinkertaisempaa kuin hallita erilaisia avaimia ja autentikointityyppejä eri perinteisille API:lle.

### MCP-esimerkki

![MCP Diagram](../../../translated_images/fi/mcp-diagram.e4ca1cbd551444a1.webp)

Kuvitellaan, että käyttäjä haluaa varata lennon AI-avustajan avulla, joka käyttää MCP:tä.

1. **Yhteys**: AI-avustaja (MCP-asiakas) muodostaa yhteyden MCP-palvelimeen, jonka tarjoaa lentoyhtiö.

2. **Työkalujen löytäminen**: Asiakas kysyy lentoyhtiön MCP-palvelimelta: "Mitä työkaluja teillä on käytettävissä?" Palvelin vastaa työkaluilla kuten "etsi lentoja" ja "varaa lentoja".

3. **Työkalun kutsuminen**: Sitten pyydät AI-avustajaa: "Etsi lento Portlandista Honoluluun." AI-avustaja, käyttäen LLM:äänsä, havaitsee, että sen täytyy kutsua "etsi lentoja" -työkalu ja välittää MCP-palvelimelle asiaankuuluvat parametrit (lähtöpaikka, kohde).

4. **Suoritus ja vastaus**: MCP-palvelin, toimiessaan kääreohjelmana, tekee varsinaisen kutsun lentoyhtiön sisäiseen varaus-API:in. Se saa lento-informaation (esimerkiksi JSON-data) ja lähettää sen takaisin AI-avustajalle.

5. **Lisävuorovaikutus**: AI-avustaja esittää lentovaihtoehdot. Kun valitset lennon, avustaja voi kutsua "varaa lento" -työkalua samassa MCP-palvelimessa, jolloin varaus tehdään.

## Agentti-agentille-protokolla (A2A)

Kun MCP keskittyy yhdistämään LLM:t työkaluihin, **Agentti-agentille (A2A) -protokolla** vie tätä askeleen pidemmälle mahdollistamalla viestinnän ja yhteistyön eri tekoälyagenttien välillä. A2A yhdistää tekoälyagentit eri organisaatioiden, ympäristöjen ja teknologiapinojen yli suorittamaan yhteisen tehtävän.

Tutkimme A2A:n komponentteja ja etuja sekä esimerkkiä, miten sitä voitaisiin soveltaa matkailusovelluksessamme.

### A2A:n ydinkomponentit

A2A keskittyy mahdollistamaan agenttien välistä viestintää ja heidän yhteistyötä käyttäjän osatehtävän suorittamisessa. Jokainen protokollan komponentti avustaa tässä:

#### Agenttikortti

Samoin kuin MCP-palvelin jakaa listan työkaluista, Agenttikortissa on:
- Agentin nimi.
- **kuvaus yleisistä tehtävistä**, joita se suorittaa.
- **lista erityisistä taidoista** kuvauksineen, jotka auttavat muita agenteja (tai ihmiskäyttäjiä) ymmärtämään, milloin ja miksi heidän kannattaa kutsua kyseistä agenttia.
- Agentin **nykyinen päätepisteen URL-osoite**.
- Agentin **versio** ja **kyvykkyydet** kuten reaaliaikaiset vastaukset ja push-ilmoitukset.

#### Agentin suorittaja

Agentin suorittaja on vastuussa **käyttäjän chatin kontekstin välittämisestä etäagentille**, koska etäagentin täytyy ymmärtää suoritettava tehtävä. A2A-palvelimessa agentti käyttää omaa suurta kielimalliaan (LLM) käsitelläkseen saapuvia pyyntöjä ja suorittaakseen tehtäviä omien sisäisten työkalujensa avulla.

#### Artefakti

Kun etäagentti on suorittanut pyydetyn tehtävän, sen työtuote luodaan artefaktina. Artefakti **sisältää agentin työn tuloksen**, **kuvauksen suoritetusta tehtävästä** ja **tekstikontextin**, joka lähetetään protokollan kautta. Kun artefakti on lähetetty, yhteys etäagenttiin suljetaan kunnes se tarvitaan uudelleen.

#### Tapahtumajono

Tätä komponenttia käytetään **päivitysten käsittelyyn ja viestien välitykseen**. Se on erityisen tärkeä tuotannossa agenttiperusteisissa järjestelmissä, jotta yhteys agenttien välillä ei katkea ennen tehtävän valmistumista, erityisesti kun tehtävien suorittaminen kestää pidempään.

### A2A:n edut

• **Parannettu yhteistyö**: Se mahdollistaa eri tarjoajien ja alustojen agenttien vuorovaikutuksen, kontekstin jakamisen ja yhteistyön, mahdollistaen saumatonta automaatiota perinteisesti erillisten järjestelmien välillä.

• **Mallin valinnan joustavuus**: Jokainen A2A-agentti voi päättää, mitä LLM:ää se käyttää palvelupyynnöissään, mahdollistaen optimoidut tai hienosäädetyt mallit agenttikohtaisesti, toisin kuin joissain MCP-skenaarioissa käytettävä yksittäinen LLM-yhteys.

• **Sisäänrakennettu tunnistautuminen**: Tunnistautuminen on suoraan integroitu A2A-protokollaan, tarjoten vahvan turvallisuuskehikon agenttien vuorovaikutuksille.

### A2A-esimerkki

![A2A Diagram](../../../translated_images/fi/A2A-Diagram.8666928d648acc26.webp)

Laajennetaan matkavarauksen esimerkkiämme, mutta tällä kertaa käyttäen A2A:ta.

1. **Käyttäjän pyyntö multi-agentille**: Käyttäjä käy vuoropuhelua "Matka-agentti" A2A-asiakas/agentin kanssa esimerkiksi sanoen: "Varaa kokonainen matka Honoluluun ensi viikoksi, sisältäen lennot, hotellin ja vuokra-auton".

2. **Matka-agentin orkestrointi**: Matka-agentti vastaanottaa monimutkaisen pyynnön. Se käyttää LLM:äänsä päättääkseen, että sen täytyy tehdä yhteistyötä muiden erikoistuneiden agenttien kanssa.

3. **Agenttien välinen viestintä**: Matka-agentti käyttää A2A-protokollaa yhdistääkseen alemmat agentit, kuten "Lentoyhtiö-agentin", "Hotelli-agentin" ja "Autovuokra-agentin", jotka ovat eri yritysten luomia.

4. **Tehtävän delegointi**: Matka-agentti lähettää erityisiä tehtäviä näille erikoistuneille agenteille (esim. "Etsi lentoja Honoluluun", "Varaa hotelli", "Vuokraa auto"). Kukin näistä erikoistuneista agenteista, käyttäen omia LLM:ejään ja omia työkalujaan (joista osa voi olla MCP-palvelimia), suorittaa oman osansa varauksesta.

5. **Yhdistetty vastaus**: Kun kaikki alemmat agentit ovat suorittaneet tehtävänsä, Matka-agentti kokoaa tulokset (lentotiedot, hotellivahvistuksen, autonvuokrausvarauksen) ja lähettää käyttäjälle kattavan, chat-tyyppisen vastauksen.

## Natural Language Web (NLWeb)

Verkkosivustot ovat pitkään olleet ensisijainen tapa käyttäjille päästä käsiksi internetin tietoihin ja dataan.

Tarkastellaan NLWebin eri komponentteja, sen etuja ja esimerkkiä siitä, miten NLWeb toimii matkailusovelluksessamme.

### NLWebin komponentit

- **NLWeb-sovellus (ydinpalvelu koodina)**: Järjestelmä, joka käsittelee luonnollisen kielen kysymyksiä. Se yhdistää alustan eri osat vastauksien luomiseksi. Voit ajatella sitä verkkosivuston luonnollisen kielen ominaisuuksia pyörittävänä **moottorina**.

- **NLWeb-protokolla**: Tämä on **perussääntöjoukko luonnollisen kielen vuorovaikutukseen** verkkosivuston kanssa. Se palauttaa vastauksia JSON-muodossa (usein käyttäen Schema.orgia). Sen tarkoituksena on luoda yksinkertainen pohja “tekoälywebille”, samalla tavalla kuin HTML mahdollisti dokumenttien jakamisen verkossa.

- **MCP-palvelin (Model Context Protocol -päätepiste)**: Jokainen NLWeb-asennus toimii myös **MCP-palvelimena**. Tämä tarkoittaa, että se voi **jakaa työkaluja (kuten “ask”-menetelmän) ja dataa** muiden tekoälyjärjestelmien kanssa. Käytännössä tämä tekee verkkosivuston sisällöstä ja toiminnoista käytettävissä olevia tekoälyagenteille, mahdollistaen sivuston osaksi laajempaa “agenttiekosysteemiä.”

- **Embeddings-mallit**: Näitä malleja käytetään **muuntamaan verkkosivuston sisältö numeerisiin esityksiin, joita kutsutaan vektoreiksi** (embedding). Nämä vektorit tallentavat merkityksen tavalla, jota tietokoneet voivat vertailla ja hakea. Ne tallennetaan erityiseen tietokantaan, ja käyttäjät voivat valita käytettävän embedding-mallin.

- **Vektoritietokanta (hakulogiikka)**: Tämä tietokanta **säilyttää verkkosivuston sisällön embeddingit**. Kun joku esittää kysymyksen, NLWeb tarkistaa vektoritietokannan löytääkseen nopeasti relevantit tiedot. Se antaa nopean listan mahdollisista vastauksista, järjestettynä samankaltaisuuden mukaan. NLWeb toimii eri vektorivarastojärjestelmien kuten Qdrant, Snowflake, Milvus, Azure AI Search ja Elasticsearch kanssa.

### NLWeb esimerkin avulla

![NLWeb](../../../translated_images/fi/nlweb-diagram.c1e2390b310e5fe4.webp)

Otetaan uudelleen matkavarauksen verkkosivusto, mutta tällä kertaa se käyttää NLWebiä.

1. **Datan sisäänajo**: Matkailusivuston olemassa olevat tuoteluettelot (esim. lentolistaukset, hotellikuvaukset, retkipaketit) muokataan Schema.org -muotoon tai ladataan RSS-syötteillä. NLWebin työkalut ottavat vastaan tämän rakenteellisen datan, luovat embeddingit ja tallentavat ne paikalliseen tai etäiseen vektoritietokantaan.

2. **Luonnollisen kielen kysely (ihminen)**: Käyttäjä käy sivustolla ja suoraan kirjoittaa chat-rajapintaan: "Etsi minulle perheystävällinen hotelli Honolulusta, jossa on uima-allas ensi viikolle".

3. **NLWeb-käsittely**: NLWeb-sovellus vastaanottaa tämän kyselyn. Se lähettää kyselyn LLM:lle ymmärtämistä varten ja samanaikaisesti hakee vektoritietokannastaan relevantteja hotellitarjouksia.

4. **Tarkat tulokset**: LLM auttaa tulkitsemaan tietokannan hakutuloksia, tunnistaa parhaat vastineet kriteerien "perheystävällinen", "uima-allas" ja "Honolulu" perusteella ja muotoilee luonnollisen kielen vastauksen. Vastaus viittaa todellisiin hotelleihin sivuston luettelosta, välttäen keksittyä tietoa.

5. **Tekoälyagentin vuorovaikutus**: Koska NLWeb toimii MCP-palvelimena, ulkoinen tekoälymatka-agentti voisi myös yhdistää tähän sivuston NLWeb-instanssiin. Agentti voisi kutsua `ask` MCP-metodia kysyäkseen suoraan sivustolta: `ask("Onko hotellin suosittelemia vegaaniystävällisiä ravintoloita Honolulun alueella?")`. NLWeb käsittelisi tämän ja käyttäisi ravintoladataan perustuvaa tietokantaansa (jos ladattu) palauttaen jäsennellyn JSON-vastauksen.

### Lisää kysymyksiä MCP/A2A/NLWebistä?

Liity [Microsoft Foundry Discordiin](https://discord.com/invite/ATgtXmAS5D) tavataaksesi muita oppijoita, osallistuaksesi toimistoaikoihin ja saadaksesi vastauksia tekoälyagenttikysymyksiisi.

## Resurssit

- [MCP aloittelijoille](https://aka.ms/mcp-for-beginners)  
- [MCP-dokumentaatio](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb-repositorio](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framework)

## Edellinen oppitunti

[Tekoälyagentit tuotannossa](../10-ai-agents-production/README.md)

## Seuraava oppitunti

[Kontekstisuunnittelu tekoälyagenteille](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->