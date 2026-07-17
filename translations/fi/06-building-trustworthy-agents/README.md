[![Luotettavat tekoälyagentit](../../../translated_images/fi/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Napsauta yllä olevaa kuvaa katsoaksesi tämän oppitunnin videon)_

# Luotettavien tekoälyagenttien rakentaminen

## Johdanto

Tässä oppitunnissa käsitellään:

- Kuinka rakentaa ja ottaa käyttöön turvallisia ja tehokkaita tekoälyagentteja
- Tärkeitä turvallisuusnäkökohtia tekoälyagenttien kehittämisessä
- Kuinka ylläpitää tietojen ja käyttäjän yksityisyyttä tekoälyagentteja kehitettäessä

## Oppimistavoitteet

Oppitunnin suorittamisen jälkeen osaat:

- Tunnistaa ja lieventää riskejä tekoälyagentteja luodessa
- Toteuttaa turvallisuustoimia varmistaaksesi, että tiedot ja pääsy on asianmukaisesti hallittu
- Luoda tekoälyagentteja, jotka ylläpitävät tietosuojaa ja tarjoavat laadukkaan käyttäjäkokemuksen

## Turvallisuus

Katsotaan ensin, kuinka rakennetaan turvallisia agenttipohjaisia sovelluksia. Turvallisuus tarkoittaa, että tekoälyagentti toimii suunnitellulla tavalla. Agenttipohjaisten sovellusten rakentajina meillä on menetelmiä ja työkaluja turvallisuuden maksimoimiseksi:

### Järjestelmäviestikehyksen rakentaminen

Jos olet joskus rakentanut tekoälysovelluksen käyttämällä suuria kielimalleja (LLM), tiedät, kuinka tärkeää on suunnitella vakaa järjestelmäkehotus tai järjestelmäviesti. Nämä kehotteet määrittelevät meta-säännöt, ohjeet ja suuntaviivat siihen, miten LLM toimii käyttäjän ja tietojen kanssa.

Tekoälyagenteille järjestelmäkehotus on vielä tärkeämpi, koska tekoälyagenttien tarvitsee saada erittäin tarkat ohjeet suorittaakseen niille suunnittelemamme tehtävät.

Laajennettavien järjestelmäkehotteiden luomiseksi voimme käyttää järjestelmäviestikehystä, jolla rakennetaan yksi tai useampi agentti sovelluksessamme:

![Järjestelmäviestikehyksen rakentaminen](../../../translated_images/fi/system-message-framework.3a97368c92d11d68.webp)

#### Vaihe 1: Luo meta-järjestelmäviesti

Meta-kehotusta käytetään LLM:llä generoimaan järjestelmäviestit luomillemme agenteille. Suunnittelemme sen mallipohjaksi, jotta voimme tehokkaasti luoda useita agentteja tarvittaessa.

Tässä esimerkki meta-järjestelmäviestistä, jonka antaisimme LLM:lle:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Vaihe 2: Luo peruskehotus

Seuraava vaihe on luoda peruskehotus tekoälyagentin kuvaamiseksi. Siihen tulisi sisällyttää agentin rooli, tehtävät, jotka agentti suorittaa, ja muut agentin vastuut.

Tässä esimerkki:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Vaihe 3: Anna perusjärjestelmäviesti LLM:lle

Nyt voimme optimoida tämän järjestelmäviestin antamalla meta-järjestelmäviestin järjestelmäviestinä ja perusjärjestelmäviestimme.

Tämä tuottaa paremmin suunnitellun järjestelmäviestin, joka ohjaa tekoälyagenttejamme:

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

#### Vaihe 4: Iteroi ja paranna

Tämän järjestelmäviestikehyksen arvo on siinä, että voimme laajentaa järjestelmäviestien luomista useilta agenteilta helpommin sekä parantaa viestejäsi ajan kuluessa. On harvinaista, että sinulla on järjestelmäviesti, joka toimii täydellisesti ensimmäisellä kerralla koko käyttötapauksessasi. Pienten hienosäätöjen tekeminen vaihtamalla perusjärjestelmäviestiä ja ajamalla se järjestelmän läpi antaa mahdollisuuden vertailla ja arvioida tuloksia.

## Uhkat ja niiden ymmärtäminen

Luotettavien tekoälyagenttien rakentamiseksi on tärkeää ymmärtää ja lieventää tekoälyagenttiin kohdistuvia riskejä ja uhkia. Katsotaan joitakin erilaisia uhkia tekoälyagenteille ja kuinka voit paremmin suunnitella ja valmistautua niihin.

![Uhkat ja niiden ymmärtäminen](../../../translated_images/fi/understanding-threats.89edeada8a97fc0f.webp)

### Tehtävän ja ohjeiden muokkaus

**Kuvaus:** Hyökkääjät pyrkivät muuttamaan tekoälyagentin ohjeita tai tavoitteita kehotteiden avulla tai manipuloimalla syötteitä.

**Lieventäminen:** Suorita validointitarkastuksia ja syötteiden suodatusta tunnistaaksesi mahdollisesti vaaralliset kehotteet ennen kuin tekoälyagentti käsittelee ne. Koska nämä hyökkäykset vaativat tyypillisesti toistuvaa vuorovaikutusta agentin kanssa, keskustelukierrosten rajoittaminen on toinen tapa estää tämän tyyppisiä hyökkäyksiä.

### Pääsy kriittisiin järjestelmiin

**Kuvaus:** Jos tekoälyagentilla on pääsy järjestelmiin ja palveluihin, jotka tallentavat arkaluonteisia tietoja, hyökkääjät voivat kompromettoida agentin ja näiden palveluiden välisen viestinnän. Näitä voivat olla suorat hyökkäykset tai epäsuorat yritykset saada tietoa näistä järjestelmistä agentin kautta.

**Lieventäminen:** Tekoälyagenttien tulisi saada pääsy järjestelmiin vain tarpeen mukaan estääkseen tämän tyyppiset hyökkäykset. Viestinnän agentin ja järjestelmän välillä tulisi myös olla turvallista. Tunnistautumisen ja pääsynhallinnan toteuttaminen on toinen tapa suojata nämä tiedot.

### Resurssien ja palvelujen ylikuormitus

**Kuvaus:** Tekoälyagentit voivat käyttää erilaisia työkaluja ja palveluja tehtävien suorittamiseen. Hyökkääjät voivat hyödyntää tätä kykyä hyökkäämällä näihin palveluihin lähettämällä suuren määrän pyyntöjä tekoälyagentin kautta, mikä voi johtaa järjestelmän toimintahäiriöihin tai suuriin kustannuksiin.

**Lieventäminen:** Toteuta käytäntöjä, jotka rajoittavat pyyntöjen määrää, joita tekoälyagentti voi tehdä palvelulle. Keskustelukierrosten ja pyyntöjen määrän rajoittaminen agentille on toinen tapa estää tämän tyyppisiä hyökkäyksiä.

### Tietopohjan myrkyttäminen

**Kuvaus:** Tämä hyökkäystyyppi ei kohdistu suoraan tekoälyagenttiin, vaan tietopohjaan ja muihin palveluihin, joita agentti käyttää. Tämä voi tarkoittaa tietojen tai informaation turmelemista, jota agentti käyttää tehtävän suorittamiseen, mikä johtaa vinoutuneisiin tai ei-toivottuihin vastauksiin käyttäjälle.

**Lieventäminen:** Suorita säännöllinen datan varmennus, jota tekoälyagentti käyttää työprosesseissaan. Varmista, että pääsy tähän dataan on turvallista eikä sitä muuta kuin luotetut henkilöt, jotta tämän tyyppinen hyökkäys vältetään.

### Ketjureaktiovirheet

**Kuvaus:** Tekoälyagentit käyttävät erilaisia työkaluja ja palveluja tehtävien suorittamiseen. Hyökkääjän aiheuttamat virheet voivat johtaa muiden järjestelmien, joihin agentti on yhteydessä, toimintahäiriöihin, mikä laajentaa hyökkäystä ja vaikeuttaa ongelman selvittämistä.

**Lieventäminen:** Yksi tapa välttää tämä on saada tekoälyagentti toimimaan rajoitetussa ympäristössä, kuten suoriutumaan tehtävistä Docker-kontissa, mikä estää suorat järjestelmähyökkäykset. Varajärjestelmien ja uudelleenyrittämisen käyttöönotto, kun tietyt järjestelmät ilmoittavat virheestä, on toinen tapa estää laajempia järjestelmäongelmia.

## Ihminen mukaan prosessiin (Human-in-the-Loop)

Toinen tehokas tapa rakentaa luotettavia tekoälyagenttijärjestelmiä on käyttää ihmistä prosessissa mukana. Tämä luo virtauksen, jossa käyttäjät voivat antaa palautetta agenteille suorituksen aikana. Käyttäjät toimivat ikään kuin agenteina monen agentin järjestelmässä ja voivat antaa hyväksynnän tai lopettaa käynnissä olevan prosessin.

![Ihminen prosessissa mukana](../../../translated_images/fi/human-in-the-loop.5f0068a678f62f4f.webp)

Tässä esimerkki Microsoft Agent Frameworkin koodinpätkästä, jolla tämä konsepti toteutetaan:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Luo tarjoaja ihmisvasteisen hyväksynnän kanssa
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Luo toimija ihmisen hyväksymisvaiheella
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Käyttäjä voi tarkastella ja hyväksyä vastauksen
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Yhteenveto

Luotettavien tekoälyagenttien rakentaminen vaatii huolellista suunnittelua, vahvoja turvallisuustoimia ja jatkuvaa parantamista. Rakentamalla rakenteellisia meta-kehotusjärjestelmiä, ymmärtämällä potentiaaliset uhat ja soveltamalla lieventämisstrategioita kehittäjät voivat luoda tekoälyagentteja, jotka ovat sekä turvallisia että tehokkaita. Lisäksi ihmisen mukaan ottaminen prosessiin varmistaa, että tekoälyagentit pysyvät käyttäjien tarpeiden mukaisina riskejä minimoiden. Kun tekoäly kehittyy, ennakoivaa otetta turvallisuuden, yksityisyyden ja eettisten näkökohtien suhteen tarvitaan luottamuksen ja luotettavuuden edistämiseksi tekoälypohjaisissa järjestelmissä.

## Koodiesimerkit

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Askeltainen esitys meta-kehotusjärjestelmäviestikehyksestä.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Ennakkohyväksyntäportit, riskiluokitus ja auditointiloki luotettaville agenteille.

### Onko sinulla lisäkysymyksiä luotettavien tekoälyagenttien rakentamisesta?

Liity [Microsoft Foundry Discord -kanavalle](https://aka.ms/ai-agents/discord) tavata muita oppijoita, osallistua toimistoaikoihin ja saada vastauksia tekoälyagenttikysymyksiisi.

## Lisäresurssit

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Vastuullisen tekoälyn yleiskatsaus</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Generatiivisten tekoälymallien ja tekoälysovellusten arviointi</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Turvallisuusjärjestelmäviestit</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Riskinarviointimalli</a>

## Edellinen oppitunti

[Agenttipohjainen RAG](../05-agentic-rag/README.md)

## Seuraava oppitunti

[Suunnittelumallin suunnittelu](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->