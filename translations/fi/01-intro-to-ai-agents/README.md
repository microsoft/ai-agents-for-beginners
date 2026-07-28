[![Intro to AI Agents](../../../translated_images/fi/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klikkaa yllä olevaa kuvaa katsoaksesi tämän oppitunnin videon)_

# Johdanto tekoälyagentteihin ja agenttien käyttötapauksiin

Tervetuloa **AI Agents for Beginners** -kurssille! Tämä kurssi antaa sinulle perustiedot — ja oikeaa toimivaa koodia — aloittaaksesi tekoälyagenttien rakentamisen alusta alkaen.

Tule sanomaan hei <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord -yhteisöön</a> — siellä on paljon oppijoita ja tekoälyn rakentajia, jotka mielellään vastaavat kysymyksiin.

Ennen kuin ryhdymme rakentamaan, varmistetaan, että ymmärrämme oikeasti, mitä tekoälyagentti *on* ja milloin sen käyttö on järkevää.

---

## Johdanto

Tässä oppitunnissa käsittelemme:

- Mitä tekoälyagentit ovat ja erilaiset olemassa olevat tyypit
- Minkälaisissa tehtävissä tekoälyagentit sopivat parhaiten käytettäväksi
- Keskeiset rakennuspalikat, joita käytät agenttiratkaisua suunnitellessasi

## Oppimistavoitteet

Tämän oppitunnin lopussa sinun tulisi osata:

- Selittää, mitä tekoälyagentti on ja miten se eroaa tavallisesta tekoälyratkaisusta
- Tietää, milloin kannattaa käyttää tekoälyagenttia (ja milloin ei)
- Laatia perussuunnitelma agenttiratkaisulle todelliseen ongelmaan

---

## Tekoälyagenttien määrittely ja tekoälyagenttien tyypit

### Mitä tekoälyagentit ovat?

Tässä yksinkertainen tapa ajatella asiaa:

> **Tekoälyagentit ovat järjestelmiä, jotka antavat suurille kielimalleille (LLM) mahdollisuuden *toimia* — tarjoamalla niille työkaluja ja tietoa toimia maailman kanssa, eivät vain vastata kehotteisiin.**

Puretaanpa tätä hieman:

- **Järjestelmä** — Tekoälyagentti ei ole vain yksi asia. Se on useiden osien kokonaisuus, joka työskentelee yhdessä. Jokaisella agentilla on ytimessään kolme osaa:
  - **Ympäristö** — Se tila, jossa agentti toimii. Matkavarauksen agentille tämä olisi itse varausalusta.
  - **Sensorit** — Kuinka agentti lukee ympäristönsä nykytilanteen. Matka-agentti voisi tarkistaa hotellien saatavuuden tai lentojen hinnat.
  - **Toimijat** — Kuinka agentti ottaa toimenpiteitä. Matka-agentti voisi varata huoneen, lähettää vahvistuksen tai peruuttaa varauksen.

![What Are AI Agents?](../../../translated_images/fi/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Suuret kielimallit** — Agentit ovat olleet olemassa ennen LLM:iä, mutta LLM:t tekevät nykyaikaisista agenteista niin tehokkaita. Ne voivat ymmärtää luonnollista kieltä, tehdä johtopäätöksiä kontekstista ja muuttaa epämääräisen käyttäjäpyynnön konkreettiseksi toimintasuunnitelmaksi.

- **Toimien suorittaminen** — Ilman agenttijärjestelmää LLM vain tuottaa tekstiä. Agenttijärjestelmässä LLM voi todella *suorittaa* toimenpiteitä — kuten hakea tietokannasta, kutsua API:a, lähettää viestin.

- **Työkalujen käyttö** — Mitä työkaluja agentti voi käyttää riippuu (1) ympäristöstä, jossa se toimii ja (2) mitä kehittäjä päättää sille antaa. Matka-agentti saattaa pystyä hakemaan lentoja, mutta ei muokkaamaan asiakastietoja — kaikki riippuu siitä, miten sen yhdistät.

- **Muisti ja tieto** — Agentit voivat omata sekä lyhytaikaisen muistin (käynnissä oleva keskustelu) että pitkäaikaisen muistin (asiakastietokanta, aiemmat vuorovaikutukset). Matka-agentti voi "muistaa", että suosittelet ikkunapaikkoja lennolla.

---

### Tekoälyagenttien eri tyypit

Kaikki agentit eivät ole samanlaisia. Tässä on päätyyppien erittely käyttäen matkavarauksen agenttia esimerkkinä:

| **Agenttityyppi** | **Mitä se tekee** | **Matka-agentin esimerkki** |
|---|---|---|
| **Yksinkertaiset refleksiagentit** | Seuraa kovakoodattuja sääntöjä — ei muistia, ei suunnittelua. | Näkee valituskirjeen → välittää sen asiakaspalveluun. Siinä kaikki. |
| **Mallipohjaiset refleksiagentit** | Pitää sisäistä mallia maailmasta ja päivittää sitä muutosten mukaan. | Seuraa historiallisia lentohintoja ja merkitsee reitit, jotka yhtäkkiä kallistuivat. |
| **Tavoitepohjaiset agentit** | Omistaa tavoitteen ja päättää miten saavuttaa sen askel askeleelta. | Varataa koko matkan (lennot, auto, hotelli) nykyisestä sijainnistasi määränpäähäsi. |
| **Hyötyarvopohjaiset agentit** | Ei löydä vain *yhtä* ratkaisua — etsii *parhaan* punnitsemalla vaihtoehtojen hyvät ja huonot puolet. | Tasapainottaa kustannukset ja mukavuuden löytääkseen matkan, joka parhaiten sopii preferensseihisi. |
| **Oppivat agentit** | Paranee ajan myötä oppimalla palautteesta. | Säätää tulevia varausehdotuksia matkan jälkeisen kyselyn tulosten perusteella. |
| **Hierarkkiset agentit** | Korkeamman tason agentti jakaa työn osa-tehtäviin ja delegoi alemmille agenteille. | "Peruuta matka" -pyyntö jaetaan: peruuta lento, peruuta hotelli, peruuta autonvuokraus — kukin hoidetaan alagentilla. |
| **Moniagenttijärjestelmät (MAS)** | Useita itsenäisiä agentteja, jotka työskentelevät yhdessä (tai kilpaillen). | Yhteistyö: eri agentit vastaavat hotelleista, lennoista ja viihteestä. Kilpailu: useat agentit kilpailevat hotellihuoneiden täyttämisestä parhaaseen hintaan. |

---

## Milloin käyttää tekoälyagentteja

Pelkkä mahdollisuus käyttää tekoälyagenttia ei tarkoita, että tulisi aina käyttää. Tässä tilanteet, joissa agentit todella loistavat:

![When to use AI Agents?](../../../translated_images/fi/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Avoimet ongelmat** — Kun ongelman ratkaisemisen vaiheet eivät ole ennalta ohjelmoitavissa. Tarvitset LLM:n ratkaisemaan polun dynaamisesti.
- **Monivaiheiset prosessit** — Tehtävät, jotka vaativat työkalujen käyttöä useissa vaiheissa, eivät pelkästään yhdessä haussa tai tuotannossa.
- **Parantuminen ajan myötä** — Kun haluat järjestelmän oppivan käyttäjäpalautteen tai ympäristön signaalien perusteella.

Perehdymme tarkemmin siihen, milloin (ja milloin *ei*) käyttää tekoälyagentteja **Luotettavien tekoälyagenttien rakentaminen** -oppitunnissa myöhemmin kurssilla.

---

## Agenttiratkaisujen perusteet

### Agentin kehitys

Ensimmäinen vaihe agenttia rakennettaessa on määritellä *mitä se osaa tehdä* — sen työkalut, toiminnot ja käyttäytymismallit.

Tässä kurssissa käytämme pääalustana **Microsoft Foundry Agent Serviceä**. Se tukee:

- Tarjoajien kuten OpenAI, Mistral ja Meta (Llama) malleja
- Lisensoitua dataa tarjoajilta kuten Tripadvisor
- Standardoituja OpenAPI 3.0 -työkalumääritelmiä

### Agenttityylit

Kommunikoit LLM:ien kanssa kehotteiden avulla. Agenttien kanssa kaikkia kehotteita ei voi aina tehdä käsityönä — agentin täytyy toimia monissa vaiheissa. Tässä **Agenttityylit** ovat hyödyllisiä. Ne ovat uudelleenkäytettäviä strategioita kehotteiden ja LLM:ien orkestrointiin skaalautuvalla ja luotettavalla tavalla.

Tämä kurssi rakentuu yleisimpien ja hyödyllisimpien agenttityylien ympärille.

### Agenttikehikot

Agenttikehikot tarjoavat kehittäjille valmiita malleja, työkaluja ja infrastruktuuria agenttien rakentamiseen. Ne helpottavat:

- Työkalujen ja kykyjen yhdistämistä
- Havainnointia, mitä agentti tekee (ja virheenkorjausta, jos jokin menee pieleen)
- Yhteistyötä monen agentin välillä

Tässä kurssissa keskitymme **Microsoft Agent Frameworkiin (MAF)** tuotantovalmiiden agenttien rakentamisessa.

---

## Koodiesimerkit

Valmiina näkemään toimintaa? Tässä ovat tämän oppitunnin koodiesimerkit:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Onko sinulla kysyttävää?

Liity [Microsoft Foundry Discordiin](https://discord.com/invite/ATgtXmAS5D) yhdistääksesi muihin oppijoihin, osallistuaksesi toimistoaikoihin ja saadaksesi tekoälyagenttiisi liittyviä vastauksia yhteisöltä.


---

## Agentin savutestaus (valinnainen)

Kun opit ottamaan agentteja käyttöön [Oppitunnissa 16](../16-deploying-scalable-agents/README.md), voit lisätä nopean jälkiasennustarkastuksen tälle oppitunnin `TravelAgent` -agentille valmiin katalogin [`tests/lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) avulla. Katso [`tests/README.md`](../tests/README.md) ohjeet sen suorittamiseen.

---

## Edellinen oppitunti

[Kurssin aloitus](../00-course-setup/README.md)

## Seuraava oppitunti

[Agenttikehikkojen tutkiminen](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->