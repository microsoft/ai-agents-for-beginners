# Agenttiprotokollien käyttäminen (MCP, A2A ja NLWeb)

[![Agenttiprotokollat](../../../translated_images/fi/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Klikkaa yllä olevaa kuvaa nähdäksesi tämän oppitunnin videon)_

Kun tekoälyagenttien käyttö kasvaa, myös protokollien tarve, jotka varmistavat standardoinnin, turvallisuuden ja tukevat avointa innovointia, kasvaa. Tässä oppitunnissa käymme läpi kolme protokollaa, jotka pyrkivät täyttämään tämän tarpeen – Model Context Protocol (MCP), Agent to Agent (A2A) ja Natural Language Web (NLWeb).

## Johdanto

Tässä oppitunnissa käsittelemme:

• Miten **MCP** mahdollistaa tekoälyagenttien pääsyn ulkoisiin työkaluihin ja dataan käyttäjän tehtävien suorittamiseksi.

• Miten **A2A** mahdollistaa viestinnän ja yhteistyön eri tekoälyagenttien välillä.

• Miten **NLWeb** tuo luonnollisen kielen käyttöliittymät mille tahansa verkkosivustolle mahdollistaen tekoälyagenttien löytää ja olla vuorovaikutuksessa sisällön kanssa.

## Oppimistavoitteet

• **Tunnistaa** MCP:n, A2A:n ja NLWebin keskeinen tarkoitus ja hyödyt tekoälyagenttien kontekstissa.

• **Selittää**, miten kukin protokolla edistää viestintää ja vuorovaikutusta LLM:ien, työkalujen ja muiden agenttien välillä.

• **Tunnistaa** kunkin protokollan eri roolit monimutkaisten agenttijärjestelmien rakentamisessa.

## Model Context Protocol

**Model Context Protocol (MCP)** on avoin standardi, joka tarjoaa standardoidun tavan sovelluksille antaa konteksti ja työkalut LLM:ille. Tämä mahdollistaa "universaalin sovittimen" eri tietolähteisiin ja työkaluihin, joihin tekoälyagentit voivat yhdistää yhtenäisellä tavalla.

Katsotaan MCP:n osat, MCP:n suorat API-käyttöihin verrattavat hyödyt ja esimerkki siitä, miten tekoälyagentit saattavat käyttää MCP-palvelinta.

### MCP:n ydinkomponentit

MCP toimii **asiakas-palvelinarkkitehtuurilla** ja ydinkomponentit ovat:

• **Isännät** ovat LLM-sovelluksia (esimerkiksi koodieditori kuten VSCode), jotka aloittavat yhteydet MCP-palvelimelle.

• **Asiakkaat** ovat osia isäntäohjelmassa, jotka ylläpitävät yhden-yhteen-yhteyksiä palvelimiin.

• **Palvelimet** ovat kevyitä ohjelmia, jotka tarjoavat tiettyjä toimintoja.

Protokollaan sisältyy kolme ydinalkeellista kyvykkyyttä, jotka ovat MCP-palvelimen tarjonnat:

• **Työkalut**: Nämä ovat erillisiä toimintoja tai komentoja, joita tekoälyagentti voi kutsua suorittaakseen toiminnon. Esimerkiksi sääpalvelu voi tarjota "hae sää" -työkalun, tai verkkokauppapalvelin voi tarjota "osta tuote" -työkalun. MCP-palvelimet ilmoittavat kunkin työkalun nimen, kuvauksen ja syöte-/tuloskaavan kyvykkyyslistassa.

• **Resurssit**: Nämä ovat vain luku -tietokohteita tai asiakirjoja, joita MCP-palvelin voi tarjota, ja asiakkaat voivat hakea niitä tarpeen mukaan. Esimerkkejä ovat tiedostojen sisällöt, tietokantatietueet tai lokitiedostot. Resurssit voivat olla tekstiä (kuten koodia tai JSONia) tai binääristä (kuten kuvia tai PDF-tiedostoja).

• **Kehotteet**: Nämä ovat ennalta määriteltyjä malleja, jotka tarjoavat ehdotettuja kehotteita monimutkaisempia työnkulkuja varten.

### MCP:n edut

MCP tarjoaa merkittäviä etuja tekoälyagenteille:

• **Dynaaminen työkalujen löytäminen**: Agentit voivat dynaamisesti saada luettelon käytettävissä olevista työkaluista palvelimelta sekä kuvauksen niiden toiminnasta. Tämä eroaa perinteisistä API:sta, jotka usein vaativat staattista koodausta integraatioille, eli mikä tahansa API-muutos vaatii koodin päivityksen. MCP tarjoaa "integroi kerran" -lähestymistavan, joka johtaa suurempaan sopeutumiskykyyn.

• **Yhteensopivuus eri LLM:ien kanssa**: MCP toimii eri LLM:ien välillä, tarjoten joustavuutta vaihtaa ydinsovellusta paremman suorituskyvyn arvioimiseksi.

• **Standardoitu turvallisuus**: MCP sisältää standardoidun tunnistusmenetelmän, parantaen skaalautuvuutta, kun lisätään pääsyä useampiin MCP-palvelimiin. Tämä on yksinkertaisempaa kuin erilaisten avainten ja tunnistustyyppien hallinta eri perinteisille API:lle.

### MCP-esimerkki

![MCP-kaavio](../../../translated_images/fi/mcp-diagram.e4ca1cbd551444a1.webp)

Kuvitellaan, että käyttäjä haluaa varata lennon tekoälyavustajan avulla, joka käyttää MCP:tä.

1. **Yhteys**: Tekoälyavustaja (MCP-asiakas) yhdistää lentoyhtiön tarjoamaan MCP-palvelimeen.

2. **Työkalujen löytäminen**: Asiakas kysyy lentoyhtiön MCP-palvelimelta, "Mitä työkaluja teillä on saatavilla?" Palvelin vastaa työkaluluettelolla, kuten "etsi lennot" ja "varaa lento".

3. **Työkalun kutsuminen**: Käyttäjä pyytää tekoälyavustajaa: "Etsi lento Portlandista Honoluluhun." Tekoälyavustaja, käyttäen LLM:äänsä, tunnistaa tarvitsevansa kutsua "etsi lennot" -työkalua ja välittää asiaankuuluvat parametrit (lähtöpaikka, kohde) MCP-palvelimelle.

4. **Suoritus ja vastaus**: MCP-palvelin, toimien kääreprogrammana, tekee varsinaisen kutsun lentoyhtiön sisäiseen varaus-API:in. Se vastaanottaa lentotiedot (esim. JSON-muodossa) ja lähettää ne takaisin tekoälyavustajalle.

5. **Lisävuorovaikutus**: Tekoälyavustaja esittää lentovaihtoehdot. Kun käyttäjä valitsee lennon, avustaja saattaa kutsua saman MCP-palvelimen "varaa lento" -työkalun, jolloin varaus tehdään.

## Agentista agenttiin -protokolla (A2A)

Kun MCP keskittyy yhdistämään LLM:t työkaluihin, **Agentista agenttiin (A2A) -protokolla** vie asiaa pidemmälle mahdollistamalla viestinnän ja yhteistyön eri tekoälyagenttien välillä. A2A yhdistää tekoälyagentit eri organisaatioiden, ympäristöjen ja teknologioiden välillä suorittaakseen yhteisen tehtävän.

Tarkastelemme A2A:n komponentteja ja hyötyjä sekä esimerkkiä siitä, miten sitä voisi käyttää matkailusovelluksessamme.

### A2A:n ydinkomponentit

A2A keskittyy mahdollistamaan agenttien välisen viestinnän ja heidän yhteistyön käyttäjän alitehtävän suorittamiseksi. Jokainen protokollakomponentti osallistuu tähän:

#### Agenttikortti

Vastaavasti kuin MCP-palvelin jakaa työkaluluettelon, Agenttikortissa on:
- Agentin nimi.
- **yleisten tehtävien kuvaus**, joita se suorittaa.
- **luettelo erityistaidoista** kuvauksineen, jotka auttavat muita agenteja (tai jopa ihmiskäyttäjiä) ymmärtämään, milloin ja miksi agenttia kannattaa kutsua.
- Agentin **nykyinen päätepisteen URL**.
- Agentin **versio** ja **kyvykkyydet**, kuten suoravirtaistusvastaukset ja push-ilmoitukset.

#### Agenttikäsittelijä

Agenttikäsittelijä vastaa **käyttäjän keskustelukontekstin välittämisestä etäagentille**, koska etäagentti tarvitsee tämän ymmärtääkseen tehtävän, joka tulee suorittaa. A2A-palvelimessa agentti käyttää omaa suurta kielimalliaan (LLM) tulkitakseen saapuvat pyynnöt ja suorittaakseen tehtävät omilla sisäisillä työkaluillaan.

#### Artefakti

Kun etäagentti on suorittanut pyydetyn tehtävän, sen tuotoksesta luodaan artefakti. Artefakti **sisältää agentin työn tuloksen**, **kuvauksen suoritetusta tehtävästä** ja **tekstuaalisen kontekstin**, joka lähetetään protokollan kautta. Kun artefakti on lähetetty, yhteys etäagenttiin suljetaan, kunnes sitä tarvitaan uudelleen.

#### Tapahtumajono

Tätä komponenttia käytetään **päivitysten käsittelystä ja viestien välittämiseen**. Se on erityisen tärkeä tuotannossa agenttipohjaisissa järjestelmissä estämään yhteyden sulkeutuminen agenttien välillä ennen tehtävän valmistumista, varsinkin kun tehtävän suorittaminen voi kestää pidempään.

### A2A:n edut

• **Parempi yhteistyö**: Mahdollistaa eri toimittajien ja alustojen agenttien keskinäisen vuorovaikutuksen, kontekstin jakamisen ja yhteistyön helpottaen saumattomia automaatioita perinteisesti erillisten järjestelmien välillä.

• **Mallin valinnan joustavuus**: Jokainen A2A-agentti voi päättää, mitä LLM-mallia se käyttää pyyntöjensä käsittelyyn, mahdollistaen optimoidut tai hienosäädetyt mallit per agentti, toisin kuin yksi LLM-yhteys joissain MCP-skenaarioissa.

• **Sisäänrakennettu tunnistus**: Tunnistus on suoraan integroitu A2A-protokollaan tarjoten vahvan turvallisuuskehyksen agenttien vuorovaikutuksille.

### A2A-esimerkki

![A2A-kaavio](../../../translated_images/fi/A2A-Diagram.8666928d648acc26.webp)

Laajennetaan matkavarausskenaariota, mutta tällä kertaa käyttäen A2A:ta.

1. **Käyttäjän pyyntö monien agenttien järjestelmälle**: Käyttäjä keskustelee "Matka-agentin" A2A-asiakas/agentin kanssa, esimerkiksi sanomalla: "Varaa koko matka Honoluluhun ensi viikoksi, mukaan lukien lennot, hotelli ja vuokra-auto".

2. **Matka-agentin orkestrointi**: Matka-agentti vastaanottaa tämän monimutkaisen pyynnön. Se käyttää LLM:äänsä pohtiakseen tehtävää ja määrittääkseen, että sen täytyy olla vuorovaikutuksessa muiden erikoistuneiden agenttien kanssa.

3. **Agenttien välinen viestintä**: Matka-agentti käyttää A2A-protokollaa yhdistääkseen alemman tason agentteihin, kuten "Lentoyhtiö-agenttiin", "Hotelli-agenttiin" ja "Vuokra-auto-agenttiin", jotka on luonut eri yritykset.

4. **Valtuutettu tehtävän suoritus**: Matka-agentti lähettää nämä erityiset tehtävät erikoistuneille agenteille (esim. "Löydä lennot Honoluluun," "Varaa hotelli," "Vuokraa auto"). Kukin näistä erikoistuneista agenteista, joilla on oma LLM ja omat työkalut (jotka voivat olla itse MCP-palvelimia), suorittaa oman osan varauksesta.

5. **Kokoava vastaus**: Kun kaikki alemman tason agentit ovat suorittaneet tehtävänsä, Matka-agentti kokoaa tulokset (lento-, hotelli- ja vuokra-autovahvistukset) ja lähettää yhteenvedon chat-tyyppisen vastauksen käyttäjälle.

## Natural Language Web (NLWeb)

Verkkosivustot ovat pitkään olleet pääasiallinen tapa, jolla käyttäjät pääsevät käsiksi informaatioon ja dataan internetissä.

Tarkastellaan NLWebin eri komponentteja, NLWebin etuja ja esimerkkiä siitä, miten NLWeb toimii matkailusovelluksessamme.

### NLWebin komponentit

- **NLWeb-sovellus (ydinpalvelinkoodi)**: Järjestelmä, joka käsittelee luonnollisen kielen kysymyksiä. Se yhdistää alustan eri osat luodakseen vastauksia. Voit ajatella sitä verkkosivuston **luonnollisen kielen toimintojen moottorina**.

- **NLWeb-protokolla**: Tämä on **perussarja sääntöjä luonnollisen kielen vuorovaikutukselle** verkkosivuston kanssa. Se palauttaa vastaukset JSON-muodossa (usein käyttäen Schema.org-mallia). Sen tarkoitus on luoda yksinkertainen perusta "tekoälyverkolle", samalla tavalla kuin HTML mahdollisti dokumenttien jakamisen verkossa.

- **MCP-palvelin (Model Context Protocol -päätepiste)**: Jokainen NLWeb-asennus toimii myös **MCP-palvelimena**. Tämä tarkoittaa, että se voi **jakaa työkaluja (kuten “ask” -menetelmän) ja dataa** muiden tekoälyjärjestelmien kanssa. Käytännössä tämä tekee verkkosivuston sisällöstä ja ominaisuuksista käytettävissä olevia tekoälyagenteille mahdollistaen sivuston osaksi laajempaa "agenttiekosysteemiä".

- **Upotusmallit**: Näitä malleja käytetään **muuntamaan verkkosivuston sisältö numeerisiksi esityksiksi, joita kutsutaan vektoreiksi (upotuksiksi)**. Nämä vektorit kuvaavat merkityksiä tavalla, jota tietokoneet voivat vertailla ja hakea. Ne tallennetaan erikoistuneeseen tietokantaan, ja käyttäjät voivat valita, mitä upotusmallia he haluavat käyttää.

- **Vektoritietokanta (hakumekanismi)**: Tämä tietokanta **tallentaa verkkosivuston sisällön upotukset**. Kun joku kysyy kysymyksen, NLWeb tarkistaa vektoritietokannan löytääkseen nopeasti asiaankuuluvimman tiedon. Se antaa nopean luettelon mahdollisista vastauksista, järjestettynä samankaltaisuuden mukaan. NLWeb tukee erilaisia vektoritallennusjärjestelmiä, kuten Qdrant, Snowflake, Milvus, Azure AI Search ja Elasticsearch.

### NLWeb-esimerkki

![NLWeb](../../../translated_images/fi/nlweb-diagram.c1e2390b310e5fe4.webp)

Tarkastellaan taas matkailuvaraussivustoamme, mutta tällä kertaa sitä pyörittää NLWeb.

1. **Datan vastaanotto**: Matkailusivuston olemassa olevat tuotekatalogit (esim. lentolistan tiedot, hotellien kuvaukset, matkapakettien tiedot) muotoillaan Schema.orgin avulla tai ladataan RSS-syötteiden kautta. NLWebin työkalut vastaanottavat tämän jäsennellyn datan, luovat upotuksia ja tallentavat ne paikalliseen tai etätietokantaan.

2. **Luonnollisen kielen kysely (ihminen)**: Käyttäjä vierailee sivustolla ja sen sijaan, että navigoi valikoissa, kirjoittaa chat-käyttöliittymään: "Etsi minulle perheystävällinen hotelli Honolulusta uima-altaalla ensi viikoksi".

3. **NLWebin käsittely**: NLWeb-sovellus vastaanottaa tämän kyselyn, lähettää sen ymmärtämiseksi LLM:lle sekä samanaikaisesti hakee vektoritietokannasta asiaankuuluvat hotellit.

4. **Tarkat tulokset**: LLM auttaa tulkitsemaan hakutuloksia tietokannasta, tunnistaa parhaat vastineet perusteilla "perheystävällinen", "uima-allas" ja "Honolulu" ja muodostaa luonnollisen kielen vastauksen. Vastaus viittaa aidosti sivuston hotelliluetteloon, välttäen keksittyä tietoa.

5. **Tekoälyagentin vuorovaikutus**: Koska NLWeb toimii MCP-palvelimena, ulkoinen tekoälymatka-agentti voisi myös yhdistää tähän NLWeb-instanssiin. Tekoälyagentti voisi käyttää `ask`-MCP-menetelmää kysyä suoraan verkkosivulta: `ask("Onko Honolulun alueella hotelli suosittelemia vegaanisia ravintoloita?")`. NLWeb prosessoi tämän, hyödyntäen ravintolatietokantaansa (jos se on ladattu) ja palauttaa rakenteellisen JSON-vastauksen.

### Lisää kysymyksiä MCP/A2A/NLWebistä?

Liity [Microsoft Foundry Discordiin](https://discord.com/invite/ATgtXmAS5D) tavata muita oppijoita, osallistua toimistoaikoihin ja saada vastauksia tekoälyagentteihin liittyviin kysymyksiin.

## Resurssit

- [MCP aloittelijoille](https://aka.ms/mcp-for-beginners)  
- [MCP Dokumentaatio](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python)

## Edellinen oppitunti

[Tekoälyagentit tuotannossa](../10-ai-agents-production/README.md)

## Seuraava oppitunti

[Kontekniikka tekoälyagenteille](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->