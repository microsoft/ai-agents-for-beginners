# Agenttiprotokollien käyttäminen (MCP, A2A ja NLWeb)

[![Agenttiprotokollat](../../../translated_images/fi/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Klikkaa yllä olevaa kuvaa nähdäksesi tämän oppitunnin videon)_

Kun tekoälyagenttien käyttö kasvaa, kasvaa myös tarve protokollille, jotka varmistavat standardoinnin, turvallisuuden ja tukevat avointa innovaatiota. Tässä oppitunnissa käsittelemme 3 protokollaa, jotka pyrkivät vastaamaan tähän tarpeeseen - Model Context Protocol (MCP), Agent to Agent (A2A) ja Natural Language Web (NLWeb).

## Johdanto

Tässä oppitunnissa käsittelemme:

• Kuinka **MCP** mahdollistaa tekoälyagenteille pääsyn ulkoisiin työkaluihin ja datoihin käyttäjän tehtävien suorittamiseksi.

• Kuinka **A2A** mahdollistaa viestinnän ja yhteistyön eri tekoälyagenttien välillä.

• Kuinka **NLWeb** tuo luonnollisen kielen rajapinnat mille tahansa verkkosivustolle mahdollistaen tekoälyagenttien löytää ja olla vuorovaikutuksessa sisällön kanssa.

## Oppimistavoitteet

• **Tunnistaa** MCP:n, A2A:n ja NLWebin ydin tarkoitus ja hyödyt tekoälyagenttien kontekstissa.

• **Selittää** kuinka kukin protokolla helpottaa viestintää ja vuorovaikutusta LLM:ien, työkalujen ja muiden agenttien välillä.

• **Tunnistaa** kunkin protokollan erilliset roolit monimutkaisten agenttijärjestelmien rakentamisessa.

## Model Context Protocol

**Model Context Protocol (MCP)** on avoin standardi, joka tarjoaa standardoidun tavan sovelluksille tarjota konteksti ja työkaluja LLM:ille. Tämä mahdollistaa "universaalin sovittimen" erilaisiin datalähteisiin ja työkaluihin, joihin tekoälyagentit voivat yhdistää yhtenäisellä tavalla.

Tarkastellaan MCP:n komponentteja, etuja verrattuna suoraan API:n käyttöön ja esimerkkiä siitä, miten tekoälyagentit voisivat käyttää MCP-palvelinta.

### MCP:n keskeiset komponentit

MCP toimii **asiakas-palvelin -arkkitehtuurissa** ja keskeiset komponentit ovat:

• **Isännät** ovat LLM-sovelluksia (esim. koodieditori kuten VSCode), jotka aloittavat yhteydet MCP-palvelimeen.

• **Asiakkaat** ovat isäntäsovelluksen osia, jotka ylläpitävät yksi-yhteen -yhteyksiä palvelimien kanssa.

• **Palvelimet** ovat kevyitä ohjelmia, jotka paljastavat tiettyjä toiminnallisuuksia.

Protokollaan kuuluu kolme ydinalkeista, jotka ovat MCP-palvelimen kyvykkyyksiä:

• **Työkalut**: Nämä ovat erillisiä toimintoja tai toiminnallisuuksia, joita tekoälyagentti voi kutsua suorittaakseen toiminnon. Esimerkiksi sääpalvelu voi tarjota "hae sää" -työkalun, tai verkkokaupan palvelin voi tarjota "osta tuote" -työkalun. MCP-palvelimet mainostavat kunkin työkalun nimen, kuvauksen ja syöte-/tuloskeeman ominaisuuksissaan.

• **Resurssit**: Nämä ovat vain luku -tiedon kohteita tai dokumentteja, joita MCP-palvelin voi tarjota, ja asiakkaat voivat hakea niitä tarvittaessa. Esimerkkejä ovat tiedostojen sisältö, tietokantarekisterit tai lokitiedostot. Resurssit voivat olla tekstiä (kuten koodia tai JSONia) tai binaaritiedostoja (kuten kuvia tai PDF-tiedostoja).

• **Kehote**: Nämä ovat ennalta määriteltyjä mallipohjia, jotka tarjoavat ehdotettuja kehotteita, mahdollistavat monimutkaisempien työnkulkujen rakentamisen.

### MCP:n edut

MCP tarjoaa merkittäviä etuja tekoälyagenteille:

• **Dynaaminen työkalujen löytyminen**: Agentit voivat dynaamisesti saada palvelimelta listan saatavilla olevista työkaluista sekä kuvaukset niiden toiminnoista. Tämä eroaa perinteisistä API:ista, jotka usein vaativat staattista ohjelmointia integraatioihin, jolloin API:n muutokset vaativat koodin päivityksiä. MCP tarjoaa "integroi kerran" -lähestymistavan, joka johtaa suurempaan joustavuuteen.

• **Yhteentoimivuus eri LLM:ien välillä**: MCP toimii eri LLM:ien kanssa ja tarjoaa joustavuutta vaihtaa ydinten malleja paremman suorituskyvyn arvioimiseksi.

• **Standardoitu turvallisuus**: MCP sisältää vakioidun tunnistautumismenetelmän, mikä parantaa skaalautuvuutta lisäämällä pääsyn uudelle MCP-palvelimelle. Tämä on yksinkertaisempaa kuin hallita eri avaimia ja tunnistautumistapoja eri perinteisille API:ille.

### MCP-esimerkki

![MCP Kuvakaavio](../../../translated_images/fi/mcp-diagram.e4ca1cbd551444a1.webp)

Kuvitellaan, että käyttäjä haluaa varata lennon tekoälyavustajalla, joka toimii MCP:n avulla.

1. **Yhteys**: Tekoälyavustaja (MCP-asiakas) yhdistää lentoyhtiön tarjoamaan MCP-palvelimeen.

2. **Työkalujen löytäminen**: Asiakas kysyy lentoyhtiön MCP-palvelimelta: "Mitä työkaluja teillä on saatavilla?" Palvelin vastaa työkaluilla kuten "etsi lentoja" ja "varaa lentoja".

3. **Työkalun kutsuminen**: Käyttäjä pyytää tekoälyavustajaa: "Etsi lento Portlandista Honoluluun." Tekoälyavustaja käyttää LLM:ään tunnistaakseen, että sen täytyy kutsua "etsi lentoja" -työkalua ja välittää tarvittavat parametrit (lähtöpaikka, määränpää) MCP-palvelimelle.

4. **Suoritus ja vastaus**: MCP-palvelin, toimiessaan välikerroksena, tekee varsinaisen kutsun lentoyhtiön sisäiseen varaus-API:iin. Se vastaanottaa lentotiedot (esim. JSON-datana) ja lähettää ne takaisin tekoälyavustajalle.

5. **Lisävuorovaikutus**: Tekoälyavustaja esittää lentovaihtoehdot. Kun käyttäjä valitsee lennon, avustaja saattaa kutsua saman MCP-palvelimen "varaa lento" -työkalua viimeistellen varauksen.

## Agentti-agentille protokolla (A2A)

MCP keskittyy yhdistämään LLM:it työkaluihin, kun taas **Agent-to-Agent (A2A) protokolla** vie tämän askeleen pidemmälle mahdollistamalla viestinnän ja yhteistyön eri tekoälyagenttien välillä. A2A yhdistää tekoälyagentteja eri organisaatioiden, ympäristöjen ja teknologioiden välillä suorittamaan yhteisen tehtävän.

Tarkastelemme A2A:n komponentteja, etuja ja esimerkkiä sen soveltamisesta matkailusovelluksessa.

### A2A:n keskeiset komponentit

A2A keskittyy mahdollistamaan agenttien välisen viestinnän ja heidän yhteistyönsä käyttäjän osa-tehtävän suorittamiseksi. Protokollan kukin komponentti tukee tätä:

#### Agenttikortti

Samoin kuin MCP-palvelin jakaa listan työkaluista, Agenttikortti sisältää:
- Agentin nimen.
- **kuvauksen yleisistä tehtävistä**, joita se suorittaa.
- **luettelon erityistaidoista** kuvauksineen auttamaan muita agenteja (tai ihmiskäyttäjiä) ymmärtämään milloin ja miksi kutsua kyseistä agenttia.
- Agentin **nykyinen päätepiste-URL**.
- Agentin **versio** ja **kyvykkyydet** kuten striimaavat vastaukset ja push-ilmoitukset.

#### Agentin suoritin

Agentin suoritin on vastuussa **käyttäjän keskustelukontekstin välittämisestä etäagentille**, etäagentti tarvitsee tämän ymmärtääkseen suoritettavan tehtävän. A2A -palvelimessa agentti käyttää omaa LLM:ään tulkitakseen saapuvat pyynnöt ja suorittaakseen tehtäviä käyttäen omia sisäisiä työkalujaan.

#### Artefakti

Kun etäagentti on suorittanut pyydetyn tehtävän, sen työtuote luodaan artefaktiksi. Artefakti **sisältää agentin työn tuloksen**, **kuvauksen suoritetusta tehtävästä** ja protokollan kautta lähetettävän **tekstikontekstin**. Kun artefakti on lähetetty, yhteys etäagenttiin suljetaan, kunnes sitä tarvitaan uudelleen.

#### Tapahtumajono

Tätä komponenttia käytetään **päivitysten ja viestien käsittelyyn**. Se on erityisen tärkeä tuotannossa agenttipohjaisissa järjestelmissä estämään yhteyden sulkeutuminen agenttien välillä ennen tehtävän valmistumista, etenkin kun tehtävien suorittaminen voi kestää kauan.

### A2A:n edut

• **Parannettu yhteistyö**: Mahdollistaa eri myyjien ja alustojen agenttien vuorovaikutuksen, kontekstin jakamisen ja yhteisen työn, helpottaen saumattomia automaatioita perinteisesti erillisten järjestelmien välillä.

• **Mallin valinnan joustavuus**: Kukin A2A-agentti voi päättää käytettävän LLM:n palvellakseen pyyntöjään, mahdollistaen optimoidut tai hienosäädetyt mallit agenttikohtaisesti, toisin kuin joissakin MCP-skenaarioissa käytetty yksittäinen LLM-yhteys.

• **Sisäänrakennettu tunnistus**: Tunnistautuminen on integroitu suoraan A2A-protokollaan, tarjoten vahvan turvallisuuskehyksen agenttien vuorovaikutuksille.

### A2A-esimerkki

![A2A Kuvakaavio](../../../translated_images/fi/A2A-Diagram.8666928d648acc26.webp)

Laajennetaan matkavarauksen esimerkkiamme käyttäen tällä kertaa A2A:ta.

1. **Käyttäjän pyyntö moniagentille**: Käyttäjä on vuorovaikutuksessa "Matka-agentin" A2A-asiakas/agentin kanssa, esimerkiksi sanomalla: "Varaa koko matka Honoluluun ensi viikoksi, mukaan lukien lennot, hotelli ja vuokra-auto".

2. **Matka-agentin orkestrointi**: Matka-agentti vastaanottaa monimutkaisen pyynnön. Se käyttää LLM:ään harkitakseen tehtävää ja päättää tarvitsevansa yhteistyötä muiden erikoistuneiden agenttien kanssa.

3. **Agenttien välinen viestintä**: Matka-agentti käyttää A2A-protokollaa yhdistääkseen alavirran agentteihin, kuten "Lentoyhtiö-agenttiin", "Hotelli-agenttiin" ja "Vuokra-auto-agenttiin", jotka ovat eri yritysten luomia.

4. **Tehtävien delegointi**: Matka-agentti lähettää erityistehtäviä näille erikoistuneille agenteille (esim. "Etsi lennot Honoluluun", "Varaa hotelli", "Vuokraa auto"). Kukin agentti käyttää omaa LLM:ään ja omia työkalujaan (jotka voivat olla MCP-palvelimia), ja suorittaa oman osansa varauksesta.

5. **Yhdistetty vastaus**: Kun kaikki alavirran agentit ovat suorittaneet tehtävänsä, Matka-agentti kokoaa tulokset (lentotiedot, hotellivahvistuksen, vuokra-autovaraus) ja lähettää monipuolisen, chat-tyyppisen vastauksen käyttäjälle.

## Natural Language Web (NLWeb)

Verkkosivustot ovat pitkään olleet ensisijainen tapa käyttäjille hakea tietoa ja dataa internetissä.

Tarkastellaan NLWebin eri komponentteja, NLWebin etuja ja esimerkkiä siitä, miten NLWeb toimii matkailusovelluksessamme.

### NLWebin komponentit

- **NLWeb-sovellus (ydinpalvelin)**: Järjestelmä, joka käsittelee luonnollisen kielen kysymyksiä. Se yhdistää alustaratkaisuja luodakseen vastauksia. Voit ajatella sitä **moottorina, joka pyörittää verkkosivuston luonnollisen kielen ominaisuuksia**.

- **NLWeb-protokolla**: Tämä on **perus sääntökokoelma luonnollisen kielen vuorovaikutukseen** verkkosivuston kanssa. Se palauttaa vastauksia JSON-muodossa (usein käyttäen Schema.org-standardia). Sen tarkoitus on luoda yksinkertainen perusta "tekoälyverkolle" samalla tavalla kuin HTML mahdollisti tiedostojen jakamisen verkossa.

- **MCP-palvelin (Model Context Protocol -päätepiste)**: Jokainen NLWeb-asennus toimii myös **MCP-palvelimena**. Tämä tarkoittaa, että se voi **jakaa työkaluja (kuten "ask"-menetelmän) ja dataa** muiden tekoälyjärjestelmien kanssa. Käytännössä tämä tekee verkkosivun sisällöstä ja toiminnoista käytettävissä olevia tekoälyagenteille, mahdollistaen sivuston osaksi laajempaa "agenttiekosysteemiä".

- **Upotemallit (Embedding Models)**: Näitä malleja käytetään **muuntamaan verkkosivuston sisältö numeerisiksi esityksiksi eli vektoreiksi (upotuksiksi)**. Nämä vektorit tallentavat merkitystä tietokoneiden vertailtavaksi ja hakua varten. Ne tallennetaan erityiseen tietokantaan, ja käyttäjät voivat valita, mitä upotemallia haluavat käyttää.

- **Vektoritietokanta (hakulogiikka)**: Tämä tietokanta **säilyttää verkkosivun sisällön upotukset**. Kun joku esittää kysymyksen, NLWeb hakee vektoritietokannasta nopeasti eniten merkityksellistä tietoa ja antaa nopeasti mahdollisten vastausten listan vastaavuuden mukaan. NLWeb toimii eri vektoritallennusjärjestelmien kanssa kuten Qdrant, Snowflake, Milvus, Azure AI Search ja Elasticsearch.

### NLWeb esimerkkinä

![NLWeb](../../../translated_images/fi/nlweb-diagram.c1e2390b310e5fe4.webp)

Kuvitellaan uudelleen matkavarauksen verkkosivusto, mutta tällä kertaa NLWebin voimin.

1. **Datan syöttäminen**: Matkailusivuston olemassa olevat tuoteluettelot (esim. lentolistat, hotellikuvaukset, retkipaketit) on muotoiltu Schema.org-standardin mukaisesti tai ladattu RSS-syötteiden kautta. NLWebin työkalut syöttävät tämän rakenteellisen datan, luovat upotukset ja tallentavat ne paikalliseen tai etäiseen vektoritietokantaan.

2. **Luonnollisen kielen kysely (ihminen)**: Käyttäjä vierailee sivustolla ja kirjoittaa chat-rajapintaan: "Löydä minulle perheystävällinen hotelli Honolulusta uima-altaalla ensi viikoksi".

3. **NLWebin käsittely**: NLWeb-sovellus vastaanottaa kyselyn. Se lähettää sen LLM:lle ymmärrystä varten ja samanaikaisesti hakee vektoritietokannasta asiaankuuluvia hotellitarjouksia.

4. **Tarkat tulokset**: LLM auttaa tulkitsemaan hakutulokset, tunnistaa parhaat osumat perustuen kriteereihin "perheystävällinen", "uima-allas" ja "Honolulu" ja muotoilee luonnollisen kielen vastauksen. Vastauksessa viitataan todellisiin hotelleihin sivuston katalogista, vältellen keksittyä tietoa.

5. **Tekoälyagentin vuorovaikutus**: Koska NLWeb toimii MCP-palvelimena, ulkoinen tekoälymatka-agentti voi yhdistää suoraan tämän verkkosivuston NLWeb-instanssiin. Agentti saisi käyttää `ask`-MCP-metodia kyselyn tekemiseen: `ask("Onko Honolulun alueella hotelleihin suositeltuja vegaaniystävällisiä ravintoloita?")`. NLWeb käsittelisi tämän, hyödyntäen ravintoladataa (jos se on ladattu) ja palauttaisi jäsennellyn JSON-vastauksen.

### Lisää kysymyksiä MCP/A2A/NLWebistä?

Liity [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) -kanavalle tapaamaan muita opiskelijoita, osallistumaan toimistoaikoihin ja saamaan vastauksia tekoälyagenttikysymyksiisi.

## Resurssit

- [MCP aloittelijoille](https://aka.ms/mcp-for-beginners)  
- [MCP-dokumentaatio](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb repo](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framework)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->