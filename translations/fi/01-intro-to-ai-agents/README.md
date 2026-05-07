[![Intro to AI Agents](../../../translated_images/fi/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Napsauta yllä olevaa kuvaa katsoaksesi tämän oppitunnin videon)_

# Johdanto tekoälyagentteihin ja agenttien käyttötapauksiin

Tervetuloa **AI Agents for Beginners** -kurssille! Tämä kurssi antaa sinulle perustiedot — ja toimivan koodin — aloittaaksesi tekoälyagenttien rakentamisen alusta alkaen.

Tule tervehtimään <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord -yhteisöön</a> — se on täynnä oppijoita ja tekoälyn rakentajia, jotka mielellään vastaavat kysymyksiin.

Ennen kuin ryhdymme rakentamaan, varmistetaan, että ymmärrämme, mitä tekoälyagentti *on* ja milloin sitä on järkevää käyttää.

---

## Johdanto

Tämä oppitunti käsittelee:

- Mitä tekoälyagentit ovat ja millaisia erilaisia tyyppejä on olemassa
- Minkälaisissa tehtävissä tekoälyagentit sopivat parhaiten käytettäväksi
- Perusrakenteet, joita käytät suunnitellessasi agenttipohjaista ratkaisua

## Oppimistavoitteet

Tämän oppitunnin lopussa sinun pitäisi pystyä:

- Selittämään, mikä tekoälyagentti on ja miten se eroaa tavallisesta tekoälyratkaisusta
- Tietämään, milloin kannattaa käyttää tekoälyagenttia (ja milloin ei)
- Luonnostelemaan perusagenttipohjainen ratkaisusuunnitelma oikean maailman ongelmaan

---

## Tekoälyagenttien määrittely ja agenttityypit

### Mitä ovat tekoälyagentit?

Tässä yksinkertainen tapa ajatella:

> **Tekoälyagentit ovat järjestelmiä, jotka antavat suurille kielimalleille (LLM) mahdollisuuden todella *tehdä asioita* — antamalla niille työkaluja ja tietoa toimia maailmassa, ei vain vastata kehotteisiin.**

Puretaanpa tätä hieman:

- **Järjestelmä** — Tekoälyagentti ei ole pelkkä yksittäinen asia. Se on osien kokoelma, jotka toimivat yhdessä. Jokaisella agentilla on ytimessään kolme osaa:
  - **Ympäristö** — Se tila, jossa agentti toimii. Matkavarauksen agentille tämä olisi varausalusta itse.
  - **Sensorit** — Kuinka agentti lukee ympäristön nykytilan. Matka-agentti voi tarkistaa hotellien saatavuuden tai lentojen hinnat.
  - **Toimilaitteet** — Kuinka agentti ottaa toimia. Agentti voi varata huoneen, lähettää vahvistuksen tai peruuttaa varauksen.

![What Are AI Agents?](../../../translated_images/fi/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Suuret kielimallit** — Agentteja oli ennen LLM:ää, mutta LLM:t tekevät moderneista agenteista niin voimakkaita. Ne ymmärtävät luonnollista kieltä, voivat järkeillä kontekstista ja muuttaa epämääräisen käyttäjäpyynnön konkreettiseksi toimintasuunnitelmaksi.

- **Toimintojen suorittaminen** — Ilman agenttijärjestelmää LLM tuottaa vain tekstiä. Agenttijärjestelmän sisällä LLM voi todella *suorittaa* vaiheita — hakea tietokannasta, kutsua rajapintaa, lähettää viestin.

- **Työkalujen käyttöoikeus** — Mitä työkaluja agentti voi käyttää, riippuu (1) siitä ympäristöstä, jossa se toimii ja (2) mitä kehittäjä on sille antanut. Matka-agentti voi etsiä lentoja, mutta ei muokata asiakastietoja — kaikki riippuu siitä, miten se on kytketty.

- **Muisti + tieto** — Agenteilla voi olla lyhytaikaista muistia (käynnissä oleva keskustelu) ja pitkäaikaista muistia (asiakastietokanta, aiemmat vuorovaikutukset). Matka-agentti voi "muistaa", että suosittelet ikkunapaikkoja.

---

### Erilaiset tekoälyagenttityypit

Kaikki agentit eivät ole rakennettu samalla tavalla. Tässä on päätyypit, käyttäen esimerkkinä matkavarausagenttia:

| **Agenttityyppi** | **Mitä se tekee** | **Matkavarausagentin esimerkki** |
|---|---|---|
| **Yksinkertaiset refleksiajurit** | Noudattaa kovakoodattuja sääntöjä — ei muistia, ei suunnittelua. | Näkee valitusviestin → ohjaa sen asiakaspalveluun. Siinä kaikki. |
| **Mallipohjaiset refleksiajurit** | Pitää sisäistä mallia maailmasta ja päivittää sitä muutosten mukaan. | Seuraa lentojen hintahistoriaa ja huomauttaa reiteistä, jotka ovat yhtäkkiä kalliita. |
| **Tavoitepohjaiset agentit** | On asettanut tavoitteen ja selvittää askel askeleelta miten siihen päästään. | Varaa kokonaisen matkan (lennot, auto, hotelli) lähtien nykyisestä sijainnistasi määränpäähän. |
| **Hyötypohjaiset agentit** | Ei löydä vain *jonkin* ratkaisun — löytää *parhaan* painottamalla erilaisia tekijöitä. | Tasapainottaa kustannukset ja mukavuuden löytääkseen matkan, joka parhaiten vastaa mieltymyksiäsi. |
| **Oppivat agentit** | Paranee ajan myötä oppimalla palautteesta. | Säätelee tulevia varaus-ehdotuksia matkan jälkeisten kyselyiden perusteella. |
| **Hierarkkiset agentit** | Korkeamman tason agentti jakaa työtä alatehtäviin ja delegoi alemmille agenteille. | "Peruuta matka" -pyyntö jaetaan: peruuta lento, peruuta hotelli, peruuta autovuokraus — jokainen hoidettu alagentilla. |
| **Multi-agenttijärjestelmät (MAS)** | Useita itsenäisiä agentteja toimimassa yhdessä (tai kilpaillen). | Yhteistyöllinen: erilliset agentit hoitavat hotellit, lennot ja viihteen. Kilpaileva: useat agentit kilpailevat hotellihuoneista parhaalla hinnalla. |

---

## Milloin käyttää tekoälyagentteja

Se, että voit käyttää tekoälyagenttia, ei tarkoita, että sinun aina pitäisi. Tässä tilanteissa agentit todella loistavat:

![When to use AI Agents?](../../../translated_images/fi/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Avoimet ongelmat** — Kun ongelman ratkaisemisen askeleita ei voi ohjelmoida etukäteen. Tarvitset LLM:n selvittämään polun dynaamisesti.
- **Monivaiheiset prosessit** — Tehtävät, jotka vaativat työkalujen käyttöä useissa vuoroissa, ei vain yksittäistä haun tai tekstin generointia.
- **Parantuminen ajan myötä** — Kun haluat järjestelmän älykkäämmäksi käyttäjäpalautteen tai ympäristön signaalien perusteella.

Tutkimme syvemmin, milloin (ja milloin *ei*) tule käyttää tekoälyagentteja myöhemmin kurssin oppitunnissa **Luotettavien tekoälyagenttien rakentaminen**.

---

## Agenttipohjaisten ratkaisujen perusasiat

### Agenttikehitys

Ensimmäinen asia agenttia rakentaessa on määritellä *mitä se voi tehdä* — sen työkalut, toiminnot ja käytökset.

Tällä kurssilla käytämme pääalustana **Azure AI Agent Serviceä**. Se tukee:

- Avoimia malleja, kuten OpenAI, Mistral ja Llama
- Lisensoitua dataa palveluntarjoajilta, kuten Tripadvisor
- Standardisoituja OpenAPI 3.0 -työkalumääritelmiä

### Agenttipohjaiset mallit

Viestität LLM:ien kanssa kehotteiden avulla. Agenteilla jokainen kehotteen käsin tekeminen ei ole aina mahdollista — agentin pitää pystyä toimimaan monissa vaiheissa. Siinä tulevat mukaan **agenttipohjaiset mallit**. Ne ovat uudelleenkäytettäviä strategioita LLM:ien ohjaukseen ja orkestrointiin laajemmalla, luotettavammalla tavalla.

Tämä kurssi rakentuu yleisimpien ja hyödyllisimpien agenttipohjaisten mallien ympärille.

### Agenttie kehykset

Agenttikehykset tarjoavat kehittäjille valmiita malleja, työkaluja ja infrastruktuuria agenttien rakentamiseen. Ne helpottavat:

- Työkalujen ja ominaisuuksien liittämistä
- Tarkkailemaan, mitä agentti tekee (ja vianmääritystä virhetilanteissa)
- Yhteistyötä useiden agenttien kesken

Tällä kurssilla keskitymme **Microsoft Agent Frameworkiin (MAF)** tuotantovalmiiden agenttien rakentamiseen.

---

## Koodiesimerkit

Valmiina näkemään käytännössä? Tässä tämän oppitunnin koodiesimerkit:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Onko kysyttävää?

Liity [Microsoft Foundry Discordiin](https://aka.ms/ai-agents/discord) verkostoituaksesi muiden oppijoiden kanssa, osallistu toimistoaikoihin ja saa tekoälyagenttikysymyksiisi vastauksia yhteisöltä.

---

## Edellinen oppitunti

[Kurssin aloitus](../00-course-setup/README.md)

## Seuraava oppitunti

[Agenttikehysten tutkiminen](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty tekoälypohjaisella käännöspalvelulla [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen omalla kielellä katsotaan viralliseksi lähteeksi. Tärkeiden tietojen osalta suositellaan ammattimaista ihmiskääntäjää. Emme ole vastuussa tämän käännöksen käytöstä mahdollisesti aiheutuvista väärinymmärryksistä tai virhetulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->