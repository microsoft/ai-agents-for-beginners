[![Intro to AI Agents](../../../translated_images/fi/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klikkaa yllä olevaa kuvaa katsoaksesi tämän oppitunnin videon)_

# Johdanto tekoälyagentteihin ja agenttien käyttötapauksiin

Tervetuloa **AI Agents for Beginners** -kurssille! Tämä kurssi tarjoaa sinulle perustiedot — sekä toimivan koodin — tekoälyagenttien rakentamisen aloittamiseen alusta alkaen.

Tule tervehtimään <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord -yhteisöön</a> — siellä on paljon oppijoita ja tekoälyn rakentajia, jotka mielellään vastaavat kysymyksiisi.

Ennen kuin ryhdymme rakentamaan, varmistaamme, että ymmärrämme mitä tekoälyagentti *on* ja milloin sen käyttö on järkevää.

---

## Johdanto

Tässä oppitunnissa käsitellään:

- Mitä tekoälyagentit ovat ja millaisia eri tyyppejä on olemassa
- Millaisiin tehtäviin tekoälyagentit soveltuvat parhaiten
- Keskeiset rakennuspalikat, joita käytät suunnitellessasi agenttipohjaista ratkaisua

## Oppimistavoitteet

Tämän oppitunnin jälkeen sinun pitäisi osata:

- Selittää, mitä tekoälyagentti on ja miten se eroaa tavallisesta tekoälyratkaisusta
- Tietää, milloin kannattaa käyttää tekoälyagenttia (ja milloin ei)
- Luoda luonnos perusagenttiratkaisusta todelliseen ongelmaan

---

## Tekoälyagenttien määrittely ja tekoälyagenttityypit

### Mitä tekoälyagentit ovat?

Tässä yksinkertainen tapa ajatella:

> **Tekoälyagentit ovat järjestelmiä, jotka antavat Suurten Kielimallien (LLM) oikeasti *toimia* — antamalla niille työkaluja ja tietoa toimia maailmassa, ei vain vastata kehotteisiin.**

Puretaan tätä hieman:

- **Järjestelmä** — Tekoälyagentti ei ole vain yksi asia. Se on kokoelma osia, jotka toimivat yhdessä. Jokaisella agentilla on ytimenä kolme osaa:
  - **Ympäristö** — Se tila, jossa agentti toimii. Matkavarausagentilla se olisi itse varausalusta.
  - **Anturit** — Kuinka agentti lukee ympäristönsä nykytilaa. Matka-agentti saattaa tarkistaa hotellien saatavuuden tai lentohinnat.
  - **Toimilaitteet** — Kuinka agentti toimii. Matka-agentti saattaa varata huoneen, lähettää vahvistuksen tai peruuttaa varauksen.

![Mitkä ovat tekoälyagentit?](../../../translated_images/fi/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Suuret kielimallit** — Agentteja oli ennenkin, mutta LLM:t tekevät nykyaikaisista agenteista niin tehokkaita. Ne ymmärtävät luonnollista kieltä, pystyvät päättelyyn kontekstin perusteella ja muuttamaan epämääräisen käyttäjäpyynnön konkreettiseksi toimintasuunnitelmaksi.

- **Toimivat toiminnot** — Ilman agenttijärjestelmää LLM tuottaa vain tekstiä. Agenttijärjestelmän sisällä LLM voi oikeasti *suorittaa* vaiheita — hakea tietokannasta, kutsua API:a, lähettää viestin.

- **Pääsy työkaluihin** — Millaisia työkaluja agentti voi käyttää riippuu (1) ympäristöstä, jossa se toimii ja (2) mitä kehittäjä on sille antanut. Matka-agentti voi esim. hakea lentoja mutta ei muokata asiakastietoja — kaikki riippuu kytkennästä.

- **Muisti ja tieto** — Agenteilla voi olla lyhytaikainen muisti (nykyinen keskustelu) ja pitkäaikainen muisti (asiakastietokanta, menneet vuorovaikutukset). Matka-agentti voi "muistaa", että pidät ikkunapaikoista.

---

### Erilaiset tekoälyagenttityypit

Kaikki agentit eivät ole samanlaisia. Tässä keskeisimmät tyypit matkavarausagenttia esimerkkinä käyttäen:

| **Agenttityyppi** | **Mitä se tekee** | **Matkavarausagentti-esimerkki** |
|---|---|---|
| **Yksinkertaiset refleksiagentit** | Noudattaa kovakoodattuja sääntöjä — ei muistia, ei suunnittelua. | Näkee valitusviestin → ohjaa sen asiakaspalveluun. Siinä kaikki. |
| **Mallipohjaiset refleksiagentit** | Pitää sisäistä mallia maailmasta ja päivittää sitä muutosten mukaan. | Seuraa historiallisia lentohintoja ja merkitsee reitit, jotka äkillisesti kallistuvat. |
| **Tavoitepohjaiset agentit** | On mielessään tavoite ja selvittää, miten sitä saavutetaan askel askeleelta. | Varaa kokonaisen matkan (lennot, auton, hotellin) alkaen nykyisestä sijainnistasi päästäksesi kohteeseesi. |
| **Hyötyjohdetut agentit** | Löytää ei vain *ratkaisun* vaan *parhaan* ratkaisun punnitsemalla erilaisia tekijöitä. | Tasapainottaa kustannuksia ja mukavuutta löytääkseen matkan, joka sopii parhaiten mieltymyksiisi. |
| **Oppivat agentit** | Parantuvat ajan myötä saamansa palautteen perusteella. | Muokkaa tulevia varaus-suosituksia matkan jälkeisten kyselyjen tulosten perusteella. |
| **Hierarkkiset agentit** | Ylin agentti jakaa työn alipäiviin ja delegoi alemmille agenteille. | "Peru matka" -pyyntö jaetaan: peru lento, peru hotelli, peru autonvuokraus — jokainen hoidetaan alagentilla. |
| **Moniagenttijärjestelmät (MAS)** | Useita itsenäisiä agenteja, jotka työskentelevät yhdessä (tai kilpailevat). | Yhteistyö: eri agentit hoitavat hotellit, lennot ja viihteen. Kilpailu: useat agentit kilpailevat hotellihuoneiden täyttämisestä parhaaseen hintaan. |

---

## Milloin käyttää tekoälyagentteja

Pelkkä se, että voit käyttää tekoälyagenttia, ei tarkoita, että sinun aina pitäisi. Tässä tilanteet, joissa agentit todella loistavat:

![Milloin käyttää tekoälyagentteja?](../../../translated_images/fi/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Avoimet ongelmat** — Kun ongelman ratkaisutapoja ei voi koodata etukäteen. Tarvitset LLM:n hahmottamaan polun dynaamisesti.
- **Monivaiheiset prosessit** — Tehtävät, jotka vaativat työkalujen käyttöä useassa vaiheessa, ei pelkkää yksittäistä hakua tai generointia.
- **Parantuminen ajan myötä** — Kun haluat järjestelmän älykkääntyvän käyttäjäpalautteen tai ympäristön signaalien perusteella.

Käsittelemme tarkemmin, milloin (ja milloin *ei*) käyttää tekoälyagentteja **Rakentamassa luotettavia tekoälyagentteja** -oppitunnissa myöhemmin kurssilla.

---

## Agenttipohjaisten ratkaisujen perusteet

### Agentin kehitys

Ensimmäinen askel agenttia rakennettaessa on määrittää *mitä se voi tehdä* — sen työkalut, toiminnot ja käyttäytymiset.

Tässä kurssissa käytämme pääalustana **Microsoft Foundry Agent Serviceä**. Se tukee:

- Mallit tarjoajilta kuten OpenAI, Mistral ja Meta (Llama)
- Lisensoidut tiedot tarjoajilta kuten Tripadvisor
- Standardoidut OpenAPI 3.0 -työkalumääritelmät

### Agenttipohjaiset mallit

Kommunikoit LLM:ien kanssa kehotteiden avulla. Agenteissa et voi aina käsin rakentaa jokaista kehotetta — agentin täytyy toimia useiden vaiheiden kautta. Tässä astuvat kuvaan **Agenttipohjaiset mallit**. Ne ovat uudelleenkäytettäviä strategioita LLM:ien kehotteiden laatimiseen ja orkestrointiin skaalautuvasti ja luotettavasti.

Tämä kurssi on rakennettu yleisimpien ja hyödyllisimpien agenttipohjaisten mallien ympärille.

### Agenttipohjaiset kehykset

Agenttipohjaiset kehykset tarjoavat kehittäjille valmiita malleja, työkaluja ja infrastruktuurin agenttien rakentamiseen. Ne helpottavat erityisesti:

- Työkalujen ja ominaisuuksien kytkemistä
- Agentin toiminnan seuraamista (ja virheiden selvittämistä)
- Yhteistyötä useamman agentin välillä

Tässä kurssissa keskitymme **Microsoft Agent Frameworkiin (MAF)** tuotantovalmiiden agenttien rakentamisessa.

---

## Koodiesimerkit

Valmiina näkemään agentin toiminnassa? Tässä oppitunnin koodiesimerkit:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Onko kysyttävää?

Liity [Microsoft Foundry Discordiin](https://discord.com/invite/ATgtXmAS5D) verkostoituaksesi muiden oppijoiden kanssa, osallistuaksesi työaikoihin ja saadaksesi vastauksia tekoälyagenttikysymyksiisi yhteisöltä.


---

## Edellinen oppitunti

[Kurssin aloitus](../00-course-setup/README.md)

## Seuraava oppitunti

[Agenttipohjaisten kehysten tutkiminen](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->