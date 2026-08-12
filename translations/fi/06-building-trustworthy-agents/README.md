[![Luotettavat tekoälyagentit](../../../translated_images/fi/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Napsauta yllä olevaa kuvaa nähdäksesi tämän oppitunnin videon)_

# Luotettavien tekoälyagenttien rakentaminen

## Johdanto

Tämä oppitunti kattaa:

- Kuinka rakentaa ja ottaa käyttöön turvallisia ja tehokkaita tekoälyagentteja
- Tärkeät tietoturvaseikat tekoälyagenttien kehittämisessä.
- Kuinka ylläpitää tietojen ja käyttäjien yksityisyyttä tekoälyagentteja kehittäessäsi.

## Oppimistavoitteet

Oppitunnin suorittamisen jälkeen osaat:

- Tunnistaa ja vähentää riskejä tekoälyagentteja luodessasi.
- Toteuttaa tietoturvatoimenpiteitä varmistaaksesi, että tiedot ja käyttöoikeudet ovat asianmukaisesti hallinnassa.
- Luoda tekoälyagentteja, jotka ylläpitävät tietosuojaa ja tarjoavat laadukkaan käyttäjäkokemuksen.

## Turvallisuus

Tarkastellaan ensin turvallisten agenttisovellusten rakentamista. Turvallisuus tarkoittaa, että tekoälyagentti toimii suunnitellusti. Agenttisovellusten rakentajina meillä on menetelmiä ja työkaluja turvallisuuden maksimoimiseksi:

### Järjestelmäviestikehyksen rakentaminen

Jos olet koskaan rakentanut tekoälysovellusta käyttäen suuria kielimalleja (LLM), tiedät kuinka tärkeää on suunnitella vankka järjestelmäkehotus tai järjestelmäviesti. Nämä kehotteet määrittelevät metarajat, ohjeet ja säännöt siitä, miten LLM toimii käyttäjän ja datan kanssa.

Tekoälyagenteille järjestelmäkehotus on vieläkin tärkeämpi, sillä agenttien täytyy saada hyvin täsmälliset ohjeet suorittaakseen heidän tehtävänsä.

Luodaksemme skaalautuvia järjestelmäkehotuksia voimme käyttää järjestelmäviestikehystä, jolla rakennamme yhden tai useamman agentin sovellukseemme:

![Järjestelmäviestikehyksen rakentaminen](../../../translated_images/fi/system-message-framework.3a97368c92d11d68.webp)

#### Vaihe 1: Luo metajärjestelmäviesti

Meta-kehotusta käyttää LLM luodakseen järjestelmäkehotukset agenteille, joita luomme. Suunnittelemme sen malliksi, jotta voimme tehokkaasti luoda useita agentteja tarvittaessa.

Tässä on esimerkki meta-järjestelmäviestistä, jonka antaisimme LLM:lle:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Vaihe 2: Luo peruskehotus

Seuraava vaihe on luoda peruskehotus, joka kuvaa tekoälyagentin. Sen tulisi sisältää agentin rooli, agentin suorittamat tehtävät ja muut agentin vastuut.

Tässä on esimerkki:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Vaihe 3: Anna perusjärjestelmäviesti LLM:lle

Nyt voimme optimoida tämän järjestelmäviestin antamalla meta-järjestelmäviestin järjestelmäviestinä yhdessä perusjärjestelmäviestin kanssa.

Tämä tuottaa paremmin suunnitellun järjestelmäviestin opastamaan tekoälyagenttejamme:

```markdown
**Company Name:** Contoso Travel  
**Role:** Travel Agent Assistant

**Objective:**  
You are an AI-powered travel agent assistant for Contoso Travel, specializing in booking flights and providing exceptional customer service. Your main goal is to assist customers in finding, booking, and managing their flights, all while ensuring that their preferences and needs are met efficiently.

**Key Responsibilities:**

1. **Flight Lookup:**
    
    - Assist customers in searching for available flights based on their specified destination, dates, and any other relevant preferences.
    - Provide a list of options, including flight times, airlines, layovers, and pricing.
2. **Flight Booking:**
    
    - Facilitate the booking of flights for customers, ensuring that all details are correctly entered into the system.
    - Confirm bookings and provide customers with their itinerary, including confirmation numbers and any other pertinent information.
3. **Customer Preference Inquiry:**
    
    - Actively ask customers for their preferences regarding seating (e.g., aisle, window, extra legroom) and preferred times for flights (e.g., morning, afternoon, evening).
    - Record these preferences for future reference and tailor suggestions accordingly.
4. **Flight Cancellation:**
    
    - Assist customers in canceling previously booked flights if needed, following company policies and procedures.
    - Notify customers of any necessary refunds or additional steps that may be required for cancellations.
5. **Flight Monitoring:**
    
    - Monitor the status of booked flights and alert customers in real-time about any delays, cancellations, or changes to their flight schedule.
    - Provide updates through preferred communication channels (e.g., email, SMS) as needed.

**Tone and Style:**

- Maintain a friendly, professional, and approachable demeanor in all interactions with customers.
- Ensure that all communication is clear, informative, and tailored to the customer's specific needs and inquiries.

**User Interaction Instructions:**

- Respond to customer queries promptly and accurately.
- Use a conversational style while ensuring professionalism.
- Prioritize customer satisfaction by being attentive, empathetic, and proactive in all assistance provided.

**Additional Notes:**

- Stay updated on any changes to airline policies, travel restrictions, and other relevant information that could impact flight bookings and customer experience.
- Use clear and concise language to explain options and processes, avoiding jargon where possible for better customer understanding.

This AI assistant is designed to streamline the flight booking process for customers of Contoso Travel, ensuring that all their travel needs are met efficiently and effectively.

```

#### Vaihe 4: Toista ja paranna

Tämän järjestelmäviestikehyksen arvo on siinä, että voit helpommin skaalata useiden agenttien järjestelmäviestien luomista sekä parantaa viestejäsi ajan myötä. Harvoin sinulla on järjestelmäviesti, joka toimii täydellisesti ensimmäisellä kerralla koko käyttötapaukseesi. Pienet muutokset ja parannukset perusjärjestelmäviestiin, jonka jälkeen suoritat järjestelmän kautta, antavat sinun vertailla ja arvioida tuloksia.

## Uhkien ymmärtäminen

Rakentaaksesi luotettavia tekoälyagentteja on tärkeää ymmärtää ja vähentää riskejä ja uhkia tekoälyagentillesi. Katsotaan joitain erilaisia uhkia tekoälyagenteille ja kuinka voit paremmin suunnitella ja varautua niihin.

![Uhkien ymmärtäminen](../../../translated_images/fi/understanding-threats.89edeada8a97fc0f.webp)

### Tehtävän ja ohjeen manipulointi

**Kuvaus:** Hyökkääjät yrittävät muuttaa tekoälyagentin ohjeita tai tavoitteita kehotteiden tai syötteiden manipuloinnin kautta.

**Ehkäisy:** Suorita validointitarkastuksia ja syötteen suodattimia tunnistaaksesi mahdollisesti vaaralliset kehotteet ennen kuin tekoälyagentti käsittelee niitä. Koska nämä hyökkäykset vaativat yleensä toistuvaa vuorovaikutusta agentin kanssa, keskustelukertojen rajoittaminen on toinen tapa estää tällaisia hyökkäyksiä.

### Pääsy kriittisiin järjestelmiin

**Kuvaus:** Jos tekoälyagentilla on pääsy järjestelmiin ja palveluihin, jotka tallentavat arkaluontoista tietoa, hyökkääjät voivat vaarantaa viestinnän agentin ja näiden palveluiden välillä. Nämä voivat olla suoria hyökkäyksiä tai epäsuoria yrityksiä saada tietoa näistä järjestelmistä agentin kautta.

**Ehkäisy:** Tekoälyagenttien pääsy järjestelmiin tulisi rajoittaa vain tarpeelliseen, jotta tällaiset hyökkäykset estetään. Myös viestinnän agentin ja järjestelmän välillä tulisi olla turvallista. Todentaminen ja käyttöoikeuksien hallinta ovat lisäkeinoja suojata näitä tietoja.

### Resurssien ja palveluiden ylikuormitus

**Kuvaus:** Tekoälyagentit voivat käyttää erilaisia työkaluja ja palveluita tehtävien suorittamiseen. Hyökkääjät voivat käyttää tätä kykyä hyökätäkseen näihin palveluihin lähettämällä suuren määrän pyyntöjä tekoälyagentin kautta, mikä voi johtaa järjestelmän kaatumisiin tai korkeisiin kustannuksiin.

**Ehkäisy:** Ota käyttöön käytännöt, jotka rajoittavat tekoälyagentin tekemien pyyntöjen määrää palvelulle. Keskustelukertojen ja tekoälyagentille tehtyjen pyyntöjen rajoittaminen on toinen tapa estää tällaiset hyökkäykset.

### Tietokannan myrkytys

**Kuvaus:** Tämä hyökkäys ei kohdistu suoraan tekoälyagenttiin vaan tietokantaan ja muihin palveluihin, joita agentti käyttää. Se voi tarkoittaa datan tai informaation korruptiota, jota agentti käyttää tehtävänsä suorittamiseen, mikä johtaa puolueellisiin tai ei-toivottuihin vastauksiin käyttäjälle.

**Ehkäisy:** Tarkasta säännöllisesti data, jota tekoälyagentti käyttää työnkuluissaan. Varmista, että pääsy tähän dataan on turvallinen ja että muutokset tekee vain luotetut henkilöt estääksesi tämän tyyppiset hyökkäykset.

### Virheketjuuntuminen

**Kuvaus:** Tekoälyagentit käyttävät erilaisia työkaluja ja palveluita tehtävien suorittamiseen. Hyökkääjien aiheuttamat virheet voivat johtaa muiden agenttiin kytkettyjen järjestelmien vikoihin, laajentaen hyökkäystä ja vaikeuttaen ongelmien ratkaisemista.

**Ehkäisy:** Yksi keino välttää tämä on saada tekoälyagentti toimimaan rajatussa ympäristössä, kuten tehtävä Docker-kontissa, jotta suorat järjestelmähyökkäykset estetään. Varakeinot ja yrityslogiikka virheisiin vastaamiseksi ovat myös keinoja estää laajempia järjestelmävikojärjestelmiä.

## Ihminen silmukassa

Toinen tehokas tapa rakentaa luotettavia tekoälyagenttijärjestelmiä on käyttää ihmistä silmukassa. Tämä luo prosessin, jossa käyttäjät voivat antaa palautetta agenteille suoritusvaiheen aikana. Käyttäjät toimivat ikään kuin agenteina monen agentin järjestelmässä ja voivat hyväksyä tai keskeyttää käynnissä olevan prosessin.

![Ihminen silmukassa](../../../translated_images/fi/human-in-the-loop.5f0068a678f62f4f.webp)

Tässä on koodiesimerkki Microsoft Agent Frameworkista, joka näyttää kuinka tämä konsepti toteutetaan:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Luo tarjoaja, jossa on ihmisen hyväksyntävaihe
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Luo agentti, jossa on ihmisen hyväksyntävaihe
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Käyttäjä voi tarkistaa ja hyväksyä vastauksen
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Yhteenveto

Luotettavien tekoälyagenttien rakentaminen vaatii huolellista suunnittelua, vahvoja tietoturvatoimia ja jatkuvaa kehitystä. Rakentamalla rakenteellisia meta-kehotsusjärjestelmiä, ymmärtämällä mahdolliset uhat ja soveltamalla ehkäisystrategioita kehittäjät voivat luoda turvallisia ja tehokkaita tekoälyagentteja. Lisäksi ihmisen silmukassa -lähestymistavan käyttöönotto varmistaa, että tekoälyagentit pysyvät käyttäjien tarpeiden mukaisina samalla kun riskit minimoidaan. Tekoälyn kehittyessä ennakoivan tietoturvan, yksityisyyden ja eettisten näkökulmien ylläpitäminen on avain luottamuksen ja luotettavuuden edistämiseen tekoälyä hyödyntävissä järjestelmissä.

## Koodiesimerkit

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Askel askeleelta -esittely meta-kehotsusjärjestelmäviestikehyksestä.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Toiminnan edeltävät hyväksyntäportit, riskiluokittelu ja auditointilokit luotettaville agenteille.

### Onko sinulla lisää kysymyksiä luotettavien tekoälyagenttien rakentamisesta?

Liity [Microsoft Foundry Discordiin](https://discord.com/invite/ATgtXmAS5D) tavata muita oppijoita, osallistua ajanvarausistuntoihin ja saada vastauksia tekoälyagenttikysymyksiisi.

## Lisäresurssit

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Vastuullisen tekoälyn yleiskatsaus</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Generatiivisten tekoälymallien ja tekoälysovellusten arviointi</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Turvallisuusjärjestelmäviestit</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Riskinarviointimalli</a>

## Edellinen oppitunti

[Agenttinen RAG](../05-agentic-rag/README.md)

## Seuraava oppitunti

[Suunnittelumalli](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->