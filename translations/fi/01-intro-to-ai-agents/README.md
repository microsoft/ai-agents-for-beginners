[![Intro to AI Agents](../../../translated_images/fi/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Napsauta yllä olevaa kuvaa katsoaksesi tämän oppitunnin videon)_

# Johdatus tekoälyagentteihin ja agenttien käyttötapauksiin

Tervetuloa **AI Agents for Beginners** -kurssille! Tämä kurssi antaa sinulle perustiedot — ja oikeaa toimivaa koodia — aloittaaksesi tekoälyagenttien rakentamisen alusta asti.

Tule juttelemaan <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord -yhteisöön</a> — siellä on paljon oppijoita ja tekoälyn rakentajia, jotka vastaavat mielellään kysymyksiin.

Ennen kuin ryhdymme rakentamaan, varmistetaan, että ymmärrämme, mitä tekoälyagentti *on* ja milloin niitä kannattaa käyttää.

---

## Johdanto

Tässä oppitunnissa käymme läpi:

- Mitä tekoälyagentit ovat ja millaisia tyyppejä on olemassa
- Minkälaisia tehtäviä tekoälyagentit parhaiten soveltuvat hoitamaan
- Agenttipohjaisen ratkaisun keskeiset rakennusosat

## Oppimistavoitteet

Oppitunnin lopussa sinun tulisi osata:

- Selittää, mitä tekoälyagentti on ja miten se eroaa tavallisesta tekoälyratkaisusta
- Tietää, milloin kannattaa käyttää tekoälyagenttia (ja milloin ei)
- Luonnostella perusagenttipohjainen ratkaisumalli todelliseen ongelmaan

---

## Tekoälyagenttien määritelmät ja agenttityypit

### Mitä tekoälyagentit ovat?

Tämä on yksinkertainen tapa ajatella asiaa:

> **Tekoälyagentit ovat järjestelmiä, jotka antavat suurten kielimallien (LLM) oikeasti *tehdä asioita* — antamalla niille työkaluja ja tietoa toimia maailmassa, eivät vain vastata kehotteisiin.**

Puretaan tätä vähän tarkemmin:

- **Järjestelmä** — Tekoälyagentti ei ole pelkkä yksittäinen asia. Se on osista koostuva kokonaisuus. Jokaisella agentilla on kolme ydinosaa:
  - **Ympäristö** — tila, jossa agentti toimii. Matkavarausagentilla tämä olisi varausalusta.
  - **Anturit** — miten agentti lukee ympäristön tämänhetkistä tilaa. Matkatoimisto voisi tarkistaa hotellien saatavuuden tai lentojen hinnat.
  - **Toimijat** — miten agentti toimii. Matkatoimisto voi varata huoneen, lähettää vahvistuksen tai peruuttaa varauksen.

![What Are AI Agents?](../../../translated_images/fi/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Suuret kielimallit** — Agentteja oli myös ennen LLM:iä, mutta LLM:t tekevät nykyagentit niin voimakkaiksi. Ne ymmärtävät luonnollista kieltä, pystyvät päättelyyn kontekstin perusteella ja muuttamaan epämääräisen käyttäjäpyynnön konkreettiseksi toimintasuunnitelmaksi.

- **Toimien suorittaminen** — Ilman agenttijärjestelmää LLM tuottaa vain tekstiä. Agenttijärjestelmän sisällä LLM voi oikeasti *suorittaa* vaiheita — etsiä tietokannasta, kutsua API:a, lähettää viestin.

- **Pääsy työkaluihin** — Mitä työkaluja agentti voi käyttää riippuu (1) ympäristöstä, jossa se toimii ja (2) mitä kehittäjä on sille antanut käyttöön. Matka-agentti voi etsiä lentoja, mutta ei muokata asiakastietoja — kaikki riippuu siitä, mitä yhdistät.

- **Muisti + Tieto** — Agentit voivat muistella lyhytaikaisesti (keskustelun nykytila) ja pitkäaikaisesti (asiakastietokanta, aiemmat vuorovaikutukset). Matka-agentti voi ”muistaa”, että suosittelet ikkunapaikkoja.

---

### Tekoälyagenttien eri tyypit

Kaikki agentit eivät ole samanlaisia. Tässä on yleisimmät tyypit esimerkkinä matkavarausagentti:

| **Agenttityyppi** | **Mitä se tekee** | **Matkavarausagentin esimerkki** |
|---|---|---|
| **Yksinkertaiset refleksagentit** | Seuraa ennalta määriteltyjä sääntöjä — ei muistia eikä suunnittelua. | Näkee valitusviestin → välittää sen asiakaspalveluun. Siinä kaikki. |
| **Mallipohjaiset refleksagentit** | Pitää sisäistä mallia maailmasta ja päivittää sitä muutosten mukaan. | Seuraa lentojen historiallisia hintoja ja merkkaa reitit, jotka ovat yhtäkkiä kalliita. |
| **Tavoitepohjaiset agentit** | On tavoite mielessään ja päättää askel askeleelta, miten se saavutetaan. | Varaat koko matkan (lennot, auto, hotelli) lähtien sijainnistasi määränpäähän. |
| **Hyötypohjaiset agentit** | Ei etsi vain *yhtä* ratkaisua — etsii *parhaan* punnitsemalla vaihtoehtoja. | Tasapainottaa kustannukset ja mukavuuden löytääkseen eniten suosimasi matkan. |
| **Oppivat agentit** | Paranee ajan myötä oppimalla palautteesta. | Säätää tulevia varaussuosituksia matkakyselyn tulosten mukaan. |
| **Hierarkkiset agentit** | Korkean tason agentti jakaa tehtävän osiin ja delegoi alemman tason agenteille. | ”Peru matka” jaetaan: peru lento, peru hotelli, peru autonvuokraus — jokainen käsitellään erikseen. |
| **Moniagenttijärjestelmät (MAS)** | Useat itsenäiset agentit työskentelevät yhdessä (tai kilpailevat). | Yhteistyö: erilliset agentit hoitavat hotellit, lennot ja viihteen. Kilpailu: useat agentit kilpailevat hotelleiden hinnoista. |

---

## Milloin käyttää tekoälyagentteja

Pelkkä se, että voit käyttää tekoälyagenttia, ei tarkoita, että aina kannattaa. Tässä ovat tilanteet, joissa agentit todella loistavat:

![When to use AI Agents?](../../../translated_images/fi/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Avoimet ongelmat** — Kun ongelman ratkaisuvaiheet eivät ole ennakkoon ohjelmoitavissa. LLM:n täytyy löytää polku dynaamisesti.
- **Monimutkaiset prosessit** — Tehtävät, jotka vaativat työkalujen käyttöä useissa vuoroissa, eivät vain yksittäinen haku tai generointi.
- **Parantuminen ajan myötä** — Kun haluat järjestelmän oppivan käyttäjäpalautteen tai ympäristön signaalien perusteella.

Syvennymme tarkemmin, milloin (ja milloin ei) tekoälyagentteja kannattaa käyttää **Building Trustworthy AI Agents** -oppitunnissa myöhemmin kurssilla.

---

## Agenttipohjaisten ratkaisujen perusteet

### Agentin kehitys

Ensimmäinen asia agenttia rakentaessa on määritellä *mitä se osaa tehdä* — sen työkalut, toiminnot ja käyttäytyminen.

Tässä kurssissa käytämme pääalustana **Azure AI Agent Serviceä**, joka tukee:

- Malleja toimittajilta kuten OpenAI, Mistral ja Meta (Llama)
- Lisensoituja tietoja toimittajilta kuten Tripadvisor
- Standardoituja OpenAPI 3.0 -työkalumääritelmiä

### Agenttipatternit

Viestität LLM:ien kanssa kehotteiden avulla. Agenttien kanssa et voi aina käsin laatia jokaista kehotetta — agentin on suoritettava toimintoja monessa vaiheessa. Tässä tulevat kuvaan **Agenttipatternit**. Ne ovat uudelleenkäytettäviä tapoja kehotteiden ja LLM:n orkestroimiseen skaalautuvalla ja luotettavalla tavalla.

Tämä kurssi rakentuu yleisimpien ja hyödyllisimpien agenttipatternien ympärille.

### Agenttikehykset

Agenttikehykset antavat kehittäjille valmiit mallit, työkalut ja infrastruktuurin agenttien rakentamiseen. Niiden avulla on helpompi:

- Yhdistää työkalut ja ominaisuudet
- Tarkkailla, mitä agentti tekee (ja debugata virheitä)
- Tehdä yhteistyötä useiden agenttien kesken

Tässä kurssissa keskitymme **Microsoft Agent Frameworkiin (MAF)** tuotantovalmiiden agenttien rakentamiseen.

---

## Koodiesimerkit

Valmiina näkemään sen toiminnassa? Tässä oppitunnin koodiesimerkit:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Onko Kysymyksiä?

Liity [Microsoft Foundry Discordiin](https://aka.ms/ai-agents/discord) yhteydenpitoa varten muiden oppijoiden kanssa, osallistu toimistoaikoihin ja saa tekoälyagenttikysymyksiisi vastauksia yhteisöltä.

---

## Edellinen oppitunti

[Kurssin aloitus](../00-course-setup/README.md)

## Seuraava oppitunti

[Agenttikehysten tutkiminen](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->