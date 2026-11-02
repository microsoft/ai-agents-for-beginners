# Agenttiprotokollien käyttö (MCP, A2A ja NLWeb)

[![Agenttiprotokollat](../../../translated_images/fi/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Napsauta yllä olevaa kuvaa nähdäksesi tämän oppitunnin videon)_

Kun tekoälyagenttien käyttö kasvaa, kasvaa myös tarve protokollille, jotka varmistavat standardoinnin, turvallisuuden ja tukevat avointa innovointia. Tässä oppitunnissa käsittelemme 3 protokollaa, jotka pyrkivät vastaamaan tähän tarpeeseen - Model Context Protocol (MCP), Agent to Agent (A2A) ja Natural Language Web (NLWeb).

## Johdanto

Tässä oppitunnissa käsittelemme:

• Miten **MCP** antaa tekoälyagenteille pääsyn ulkoisiin työkaluihin ja datoihin käyttäjän tehtävien suorittamista varten.

•  Miten **A2A** mahdollistaa viestinnän ja yhteistyön eri tekoälyagenttien välillä.

• Miten **NLWeb** tuo luonnollisen kielen käyttöliittymät mille tahansa verkkosivustolle, mahdollistaen tekoälyagenttien löytävän ja vuorovaikuttavan sisällön kanssa.

## Oppimistavoitteet

• **Tunnistaa** MCP:n, A2A:n ja NLWebin keskeiset tarkoitukset ja hyödyt tekoälyagenttien yhteydessä.

• **Selittää** miten kukin protokolla helpottaa viestintää ja vuorovaikutusta LLM:ien, työkalujen ja muiden agenttien välillä.

• **Tunnistaa** kunkin protokollan erilliset roolit monimutkaisten agenttijärjestelmien rakentamisessa.

## Model Context Protocol

**Model Context Protocol (MCP)** on avoin standardi, joka tarjoaa standardoidun tavan sovelluksille tarjota konteksti ja työkalut LLM:ille. Tämä mahdollistaa "universaalin sovittimen" eri datalähteisiin ja työkaluihin, joihin tekoälyagentit voivat yhdistää johdonmukaisella tavalla.

Tarkastellaan MCP:n komponentteja, etuja verrattuna suoraan API-käyttöön ja esimerkkiä siitä, miten tekoälyagentit voisivat käyttää MCP-palvelinta.

### MCP:n ydinosa-alueet

MCP toimii **asiakas-palvelin -arkkitehtuurilla** ja ydinosa-alueet ovat:

• **Isännät** ovat LLM-sovelluksia (esim. koodieditori kuten VSCode), jotka aloittavat yhteydet MCP-palvelimeen.

• **Asiakkaat** ovat isäntä-sovelluksen osia, jotka ylläpitävät yksi-yhteen-yhteyksiä palvelimiin.

• **Palvelimet** ovat kevyitä ohjelmia, jotka tarjoavat tiettyjä kyvykkyyksiä.

Protokollaan kuuluu kolme ydinalkioita, jotka ovat MCP-palvelimen kyvykkyyksiä:

• **Työkalut**: Nämä ovat erillisiä toimintoja, joita tekoälyagentti voi kutsua suoritettavaksi. Esimerkiksi sääpalvelu voisi tarjota "hae sää" työkalun, tai verkkokauppapalvelin "osta tuote" työkalun. MCP-palvelimet ilmoittavat kunkin työkalun nimen, kuvauksen ja syöte/uloskäyntiskaemat kyvykkyyslistauksessaan.

• **Resurssit**: Nämä ovat vain-luku -dataa tai dokumentteja, joita MCP-palvelin voi tarjota ja asiakkaat voivat noutaa niitä tarpeen mukaan. Esimerkkejä ovat tiedostojen sisällöt, tietokantarekisterit tai lokitiedostot. Resurssit voivat olla tekstiä (kuten koodi tai JSON) tai binaaritiedostoja (kuten kuvia tai PDF:iä).

• **Kehotukset**: Nämä ovat valmiiksi määriteltyjä malleja, jotka tarjoavat ehdotettuja kehotuksia monimutkaisempiin työnkulkuihin.

### MCP:n edut

MCP tarjoaa merkittäviä etuja tekoälyagenteille:

• **Dynaaminen työkalujen löytäminen**: Agentit voivat dynaamisesti saada listan palvelimen saatavilla olevista työkaluista sekä kuvaukset niiden toiminnasta. Tämä eroaa perinteisistä API:sta, jotka usein vaativat staattista koodinmuokkausta integraatioihin, jolloin API-muutokset vaativat koodin päivitystä. MCP tarjoaa "integroi kerran" -lähestymistavan, mikä mahdollistaa paremman mukautuvuuden.

• **Yhteentoimivuus eri LLM:ien välillä**: MCP toimii eri LLM:ien kanssa ja antaa joustavuutta vaihtaa ydinsovelluksia paremman suorituskyvyn etsimiseksi.

• **Standardoitu turvallisuus**: MCP sisältää standardoidun tunnistautumismenetelmän, mikä parantaa laajennettavuutta lisätessä pääsyä muihin MCP-palvelimiin. Tämä on yksinkertaisempaa verrattuna erilaisten avainten ja autentikointityyppien hallintaan eri perinteisissä API:ssa.

### MCP Esimerkki

![MCP Diagram](../../../translated_images/fi/mcp-diagram.e4ca1cbd551444a1.webp)

Kuvitellaan käyttäjä, joka haluaa varata lennon AI-avustajan avulla, joka käyttää MCP:tä.

1. **Yhteys**: AI-avustaja (MCP-asiakas) yhdistää MCP-palvelimeen, jonka on tarjonnut lentoyhtiö.

2. **Työkalujen löytäminen**: Asiakas kysyy lentoyhtiön MCP-palvelimelta: "Mitä työkaluja teillä on saatavilla?" Palvelin vastaa työkaluilla kuten "etsi lentoja" ja "varaa lentoja".

3. **Työkalun kutsuminen**: Käyttäjä pyytää AI-avustajaa: "Etsi lento Portlandista Honoluluun." AI-avustaja, käyttäen LLM:ää, tunnistaa tarvitsevansa kutsua "etsi lentoja" työkalua ja antaa asiaankuuluvat parametrit (lähtöpaikka, määränpää) MCP-palvelimelle.

4. **Suoritus ja vastaus**: MCP-palvelin, toimiessaan välikerroksena, tekee varsinaisen kutsun lentoyhtiön sisäiseen varaus-API:in. Se vastaanottaa lentotiedot (esim. JSON-dataa) ja lähettää ne takaisin AI-avustajalle.

5. **Jatkuva vuorovaikutus**: AI-avustaja esittelee lento vaihtoehdot. Kun käyttäjä valitsee lennon, avustaja voi kutsua "varaa lento" työkalua samalta MCP-palvelimelta ja viimeistellä varauksen.

## Agentti-agentille -protokolla (A2A)

Kun MCP keskittyy yhdistämään LLM:iä työkaluihin, **Agentti-agentille (A2A) -protokolla** vie asian askeleen pidemmälle mahdollistamalla viestinnän ja yhteistyön eri tekoälyagenttien välillä. A2A yhdistää tekoälyagentit eri organisaatioiden, ympäristöjen ja teknologioiden välillä suorittamaan yhteisiä tehtäviä.

Tutkimme A2A:n komponentteja ja hyötyjä sekä annamme esimerkin sen käytöstä matkavarauksen sovelluksessa.

### A2A:n ydinosa-alueet

A2A keskittyy agenttien väliseen viestintään ja yhteistyöhön käyttäjän alatehtävän suorittamiseksi. Jokainen protokollan osa osallistuu tähän:

#### Agenttikortti

Samalla tavalla kuin MCP-palvelin jakaa työkalulistan, Agenttikortti sisältää:
- Agentin nimen.
- Yleisen kuvauksen tehtävistä, joita se suorittaa.
- Luettelon erityisistä taidoista kuvausten kanssa, jotka auttavat muita agentteja (tai ihmiskäyttäjiä) ymmärtämään, milloin ja miksi kyseistä agenttia halutaan kutsua.
- Agentin nykyisen loppupiste-URL:in.
- Agentin version ja kyvykkyydet, kuten suoratoistovastaukset ja push-ilmoitukset.

#### Agenttisuorittaja

Agenttisuorittaja vastaa **saattamaan käyttäjän chatin kontekstin etäagentille**, joka tarvitsee tämän tehtävän ymmärtämiseksi. A2A-palvelimessa agentti käyttää omaa suurta kielimalliaan (LLM) saapuvien pyyntöjen tulkitsemiseen ja tehtävien suorittamiseen sisäisillä työkaluillaan.

#### Artefakti

Kun etäagentti on suorittanut pyydetyn tehtävän, sen työtuote luodaan artefaktina. Artefakti **sisältää agentin työn tuloksen**, **kuvauksen suorituksesta** ja **teksti-kontekstin**, joka lähetetään protokollan kautta. Kun artefakti on lähetetty, yhteys etäagenttiin suljetaan, kunnes taas tarvitaan.

#### Tapahtumajono

Tätä komponenttia käytetään **päivitysten käsittelyyn ja viestien välitykseen**. Se on erityisen tärkeä tuotannossa agenttipohjaisissa järjestelmissä estämään yhteyden katkeaminen agenttien välillä ennen tehtävän valmistumista, varsinkin kun tehtävän suorittaminen voi kestää kauan.

### A2A:n edut

• **Parannettu yhteistyö**: Se mahdollistaa eri myyjien ja alustojen agenttien vuorovaikutuksen, kontekstin jakamisen ja yhteistyön, mikä helpottaa saumattomia automaatioita perinteisesti erillisten järjestelmien välillä.

• **Mallin valinnan joustavuus**: Jokainen A2A-agentti voi päättää, mitä LLM:ää se käyttää pyyntöjensä palvelemiseen, mahdollistaen optimoidut tai hienosäädetyt mallit per agentti, toisin kuin joissakin MCP-skenaarioissa yksi LLM-yhteys.

• **Sisäänrakennettu tunnistautuminen**: Tunnistautuminen on integroitu suoraan A2A-protokollaan, tarjoten vahvan turvallisuuskehyksen agenttien vuorovaikutuksille.

### A2A Esimerkki

![A2A Diagram](../../../translated_images/fi/A2A-Diagram.8666928d648acc26.webp)

Laajennetaan matkavarauksen tilannettamme, mutta tällä kertaa käyttäen A2A:ta.

1. **Käyttäjän pyyntö monille agenteille**: Käyttäjä keskustelee "Matka-agentin" A2A-asiakkaan/agentin kanssa, ehkä sanomalla: "Varaa koko matka Honoluluun ensi viikoksi, mukaan lukien lennot, hotelli ja vuokra-auto".

2. **Matka-agentin orkestrointi**: Matka-agentti vastaanottaa tämän monimutkaisen pyynnön. Se käyttää LLM:ään harkitakseen tehtävää ja päättää, että sen täytyy olla vuorovaikutuksessa muiden erikoistuneiden agenttien kanssa.

3. **Agenttien välinen viestintä**: Matka-agentti käyttää A2A-protokollaa yhdistääkseen alavirta-agentteihin, kuten "Lentoyhtiö-agenttiin", "Hotelli-agenttiin" ja "Vuokra-auton agenttiin", jotka ovat eri yritysten luomia.

4. **Valtuutettu tehtävän suoritus**: Matka-agentti lähettää erityisiä tehtäviä näille erikoistuneille agenteille (esim. "Etsi lentoja Honoluluun", "Varaa hotelli", "Vuokraa auto"). Kukin näistä erikoistuneista agenteista, jotka käyttävät omia LLM:iään ja työkalujaan (jotka voivat olla MCP-palvelimia itseäänkin), suorittaa varauksen oman osansa.

5. **Yhteen koottu vastaus**: Kun kaikki alavirta-agentit ovat suorittaneet tehtävänsä, Matka-agentti kokoaa tulokset (lentotiedot, hotellivahvistus, vuokra-auton varaus) ja lähettää käyttäjälle kattavan, chat-tyyppisen vastauksen.

## Natural Language Web (NLWeb)

Verkkosivustot ovat pitkään olleet käyttäjien ensisijainen tapa päästä käsiksi tietoon ja dataan internetissä.

Tarkastellaan NLWebin eri komponentteja, sen hyötyjä ja esimerkkiä siitä, miten NLWeb toimii matkailusovelluksessamme.

### NLWebin komponentit

- **NLWeb-sovellus (ydinpalvelukoodi)**: Järjestelmä, joka käsittelee luonnollisen kielen kysymyksiä. Se yhdistää alustan eri osat vastauksien luomiseksi. Voit ajatella sitä verkkosivuston luonnollisen kielen ominaisuuksien **moottorina**.

- **NLWeb-protokolla**: Tämä on **perussarja sääntöjä luonnollisen kielen vuorovaikutukselle** verkkosivuston kanssa. Se palauttaa vastaukset JSON-muodossa (usein käyttäen Schema.org:ia). Sen tarkoitus on luoda yksinkertainen pohja "tekoälyverkolle", samalla tavalla kuin HTML teki dokumenttien jakamisen verkossa mahdolliseksi.

- **MCP-palvelin (Model Context Protocol -loppupiste)**: Jokainen NLWeb-asennus toimii myös **MCP-palvelimena**. Tämä tarkoittaa, että se voi **jakaa työkaluja (kuten "kysy" -menetelmä) ja dataa** muiden tekoälyjärjestelmien kanssa. Käytännössä tämä tekee verkkosivuston sisällöstä ja kyvyistä käytettäviä tekoälyagenteille, mahdollistaen sivuston osaksi laajempaa "agenttiekosysteemiä."

- **Upotusmallit**: Näitä malleja käytetään **muuntamaan verkkosivuston sisältö numeerisiksi esityksiksi, niin kutsutuiksi vektoreiksi (upotuksiksi).** Nämä vektorit vangitsevat merkityksen siten, että tietokoneet voivat vertailla ja hakea niitä. Ne tallennetaan erityiseen tietokantaan ja käyttäjät voivat valita, mitä upotusmallia haluavat käyttää.

- **Vektoritietokanta (haku mekanismi)**: Tämä tietokanta **tallentaa verkkosivuston sisällön upotukset.** Kun joku esittää kysymyksen, NLWeb tarkistaa vektoritietokannan nopeasti löytääkseen olennaisimman tiedon. Se antaa nopean listan mahdollisista vastauksista, järjestettynä samankaltaisuuden mukaan. NLWeb toimii eri vektoritallennusjärjestelmien kanssa, kuten Qdrant, Snowflake, Milvus, Azure AI Search ja Elasticsearch.

### NLWeb esimerkin kautta

![NLWeb](../../../translated_images/fi/nlweb-diagram.c1e2390b310e5fe4.webp)

Otetaan taas matkailusivustomme, mutta tällä kertaa sen taustalla on NLWeb.

1. **Datan tuonti**: Matkailusivuston olemassa olevat tuotekatalogit (esim. lentoluettelot, hotellikuvaukset, retkipaketit) on muotoiltu Schema.org -mukaan tai ladattu RSS-syötteiden kautta. NLWebin työkalut lukevat tämän rakenteellisen datan, luovat upotukset ja tallentavat ne paikalliseen tai etäiseen vektoritietokantaan.

2. **Luonnollisen kielen kysely (ihminen)**: Käyttäjä vierailee sivustolla ja sen sijaan, että selaa valikoita, kirjoittaa chat-käyttöliittymään: "Löydä minulle perheystävällinen hotelli Honolulusta, jossa on uima-allas ensi viikolle".

3. **NLWeb käsittely**: NLWeb-sovellus vastaanottaa tämän kyselyn. Se lähettää kyselyn LLM:lle ymmärtämistä varten ja samanaikaisesti etsii vektoritietokannastaan relevantteja hotellitarjouksia.

4. **Tarkat tulokset**: LLM auttaa tulkitsemaan haun tulokset tietokannasta, tunnistaa parhaat vastaavuudet "perheystävällinen," "uima-allas" ja "Honolulu" kriteerien perusteella ja muotoilee luonnollisen kielen vastauksen. Olennaista on, että vastaus viittaa todellisiin hotellitietoihin sivuston katalogista, välttäen keksittyä informaatiota.

5. **Tekoälyagentin vuorovaikutus**: Koska NLWeb toimii MCP-palvelimena, ulkoinen tekoälymatka-agentti voisi myös yhdistää tähän verkkosivuston NLWeb-instanssiin. Tekoälyagentti voisi käyttää `ask` MCP-metodia kysyäkseen sivustolta suoraan: `ask("Onko Honolulun alueella hotelli suositellut vegaanisia ravintoloita?")`. NLWeb käsittelisi tämän hyödyntäen ravintolatietokantansa (jos ladattu) ja palauttaisi rakenteellisen JSON-vastauksen.

### Lisäkysymyksiä MCP/A2A/NLWebistä?

Liity [Microsoft Foundry Discordiin](https://discord.com/invite/ATgtXmAS5D) tavata muita oppijoita, osallistua toimistoaikoihin ja saada vastauksia tekoälyagenttien kysymyksiin.

## Resurssit

- [MCP aloittelijoille](https://aka.ms/mcp-for-beginners)  
- [MCP-dokumentaatio](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python)

## Edellinen oppitunti

[Tekoälyagentit tuotannossa](../10-ai-agents-production/README.md)

## Seuraava oppitunti

[Konteksti-insinöörityö tekoälyagenteille](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->