[![Luotettavat tekoälyagentit](../../../translated_images/fi/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Napsauta yllä olevaa kuvaa nähdäksesi tämän oppitunnin videon)_

# Luotettavien tekoälyagenttien rakentaminen

## Johdanto

Tässä oppitunnissa käsitellään:

- Kuinka rakentaa ja ottaa käyttöön turvallisia ja tehokkaita tekoälyagentteja
- Tärkeitä turvallisuusnäkökohtia tekoälyagenttien kehittämisessä
- Kuinka ylläpitää tietojen ja käyttäjän yksityisyyttä tekoälyagentteja kehitettäessä

## Oppimistavoitteet

Oppitunnin suorittamisen jälkeen osaat:

- Tunnistaa ja lieventää riskejä tekoälyagentteja luodessa
- Toteuttaa turvallisuustoimenpiteitä varmistaaksesi, että tiedot ja käyttöoikeudet hallitaan asianmukaisesti
- Luoda tekoälyagentteja, jotka säilyttävät tietosuojan ja tarjoavat laadukkaan käyttäjäkokemuksen

## Turvallisuus

Aloitetaan turvallisten agenttisovellusten rakentamisesta. Turvallisuus tarkoittaa, että tekoälyagentti toimii suunnitellusti. Agenttisovellusten rakentajilla on käytössä menetelmiä ja työkaluja turvallisuuden maksimoimiseksi:

### Järjestelmäviestikehyksen rakentaminen

Jos olet koskaan rakentanut tekoälysovellusta käyttämällä suuria kielimalleja (LLM), tiedät kuinka tärkeää on suunnitella vankka järjestelmäkehotus tai järjestelmäviesti. Nämä kehotukset asettavat metan säännöt, ohjeistukset ja suuntaviivat sille, miten LLM vuorovaikuttaa käyttäjän ja tietojen kanssa.

Tekoälyagenttien tapauksessa järjestelmäkehotus on vielä tärkeämpi, koska tekoälyagentit tarvitsevat hyvin täsmällisiä ohjeita suorittaakseen meille suunnitellut tehtävät.

Voimme luoda skaalautuvia järjestelmäkehotuksia käyttämällä järjestelmäviestikehystä rakentaaksemme yhden tai useamman agentin sovellukseemme:

![Järjestelmäviestikehyksen rakentaminen](../../../translated_images/fi/system-message-framework.3a97368c92d11d68.webp)

#### Vaihe 1: Luo meta-järjestelmäviesti

Meta-kehotusta käyttää LLM luodakseen järjestelmäkehotukset luomillemme agenteille. Suunnittelemme sen malliksi, jotta voimme tehokkaasti luoda useita agenteja tarvittaessa.

Tässä esimerkki meta-järjestelmäviestistä, jonka antaisimme LLM:lle:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Vaihe 2: Luo peruskehotus

Seuraava vaihe on luoda peruskehotus kuvaamaan tekoälyagenttia. Sen tulisi sisältää agentin rooli, agentin suorittamat tehtävät sekä muut agentin vastuut.

Tässä esimerkki:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Vaihe 3: Anna perusjärjestelmäviesti LLM:lle

Nyt voimme optimoida tämän järjestelmäviestin antamalla meta-järjestelmäviestin järjestelmäviestinä ja perusjärjestelmäviestimme.

Tämä tuottaa järjestelmäviestin, joka on paremmin suunniteltu ohjaamaan tekoälyagenttejamme:

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

Tämän järjestelmäviestikehyksen arvo on kyky skaalata järjestelmäviestien luomista useilta agenteilta helpommaksi sekä parantaa järjestelmäviestejäsi ajan kuluessa. On harvinaista, että sinulla on järjestelmäviesti, joka toimii täydellisesti ensimmäisellä kerralla koko käyttötapaukseesi. Pienten säätöjen ja parannusten tekeminen muuttamalla perusjärjestelmäviestiä ja suorittamalla se järjestelmän läpi antaa sinun vertailla ja arvioida tuloksia.

## Uhkien ymmärtäminen

Rakentaaksesi luotettavia tekoälyagentteja on tärkeää ymmärtää ja lieventää tekoälyagenttiin kohdistuvia riskejä ja uhkia. Tarkastellaan muutamia erilaisia uhkia tekoälyagenteille ja miten voit paremmin suunnitella ja valmistautua niihin.

![Uhkien ymmärtäminen](../../../translated_images/fi/understanding-threats.89edeada8a97fc0f.webp)

### Tehtävät ja ohjeet

**Kuvaus:** Hyökkääjät yrittävät muuttaa tekoälyagentin ohjeita tai tavoitteita kehotuksilla tai syötteiden manipuloinnilla.

**Lieventäminen:** Suorita validointitarkastuksia ja syötesuodattimia havaitaksesi mahdollisesti vaaralliset kehotukset ennen kuin tekoälyagentti käsittelee ne. Koska nämä hyökkäykset vaativat tyypillisesti usein tapahtuvaa vuorovaikutusta agentin kanssa, keskustelukierrosten määrän rajoittaminen on toinen tapa estää tämän tyyppisiä hyökkäyksiä.

### Pääsy kriittisiin järjestelmiin

**Kuvaus:** Jos tekoälyagentilla on pääsy järjestelmiin ja palveluihin, jotka säilyttävät arkaluontoisia tietoja, hyökkääjät voivat vaarantaa agentin ja näiden palveluiden välisen viestinnän. Nämä voivat olla suoria hyökkäyksiä tai epäsuoria yrityksiä saada tietoa näistä järjestelmistä agentin kautta.

**Lieventäminen:** Tekoälyagenttien tulisi saada pääsy järjestelmiin vain tarpeen mukaan tämän tyyppisten hyökkäysten estämiseksi. Myös agentin ja järjestelmän välinen viestintä tulisi olla suojattua. Todennuksen ja pääsynhallinnan toteuttaminen on toinen tapa suojata tätä tietoa.

### Resurssien ja palveluiden ylikuormitus

**Kuvaus:** Tekoälyagentit voivat käyttää erilaisia työkaluja ja palveluita suorittaakseen tehtäviä. Hyökkääjät voivat käyttää tätä kykyä hyökätäkseen näihin palveluihin lähettämällä suuren määrän pyyntöjä tekoälyagentin kautta, mikä saattaa johtaa järjestelmävioihin tai korkeisiin kustannuksiin.

**Lieventäminen:** Toteuta käytännöt, jotka rajoittavat tekoälyagentin lähettämien pyyntöjen määrää palveluun. Keskustelukierrosten ja pyyntöjen rajoittaminen tekoälyagentille on toinen tapa estää tämän tyyppisiä hyökkäyksiä.

### Tietopohjan myrkyttäminen

**Kuvaus:** Tämä hyökkäystyyppi ei kohdistu suoraan tekoälyagenttiin vaan tietopohjaan ja muihin palveluihin, joita tekoälyagentti käyttää. Se voi tarkoittaa tietojen tai informaatioiden korruptiota, joita tekoälyagentti käyttää tehtävän suorittamiseksi, mikä voi johtaa vinoutuneisiin tai ei-toivottuihin vastauksiin käyttäjälle.

**Lieventäminen:** Suorita säännöllinen tietojen tarkistus, joita tekoälyagentti käyttää työnkuluissaan. Varmista, että pääsy näihin tietoihin on suojattu ja että niitä muokkaavat vain luotetut henkilöt tämän tyyppisen hyökkäyksen välttämiseksi.

### Ketjuttuvat virheet

**Kuvaus:** Tekoälyagentit käyttävät erilaisia työkaluja ja palveluita tehtävien suorittamiseen. Hyökkääjien aiheuttamat virheet voivat johtaa muiden järjestelmien, joihin tekoälyagentti on yhteydessä, vikoihin, jolloin hyökkäys leviää ja sen jäljittäminen vaikeutuu.

**Lieventäminen:** Yksi tapa välttää tämä on pitää tekoälyagentti toiminnassa rajatussa ympäristössä, kuten suoritettuna Docker-säilössä, estäen suorat järjestelmähyökkäykset. Varausmekanismien ja uudelleenyrityksen loogisten toimintojen luominen, kun tietyt järjestelmät vastaavat virheellä, on toinen tapa estää laajempia järjestelmäkatkoksia.

## Ihminen prosessissa

Toinen tehokas tapa rakentaa luotettavia tekoälyagenttijärjestelmiä on käyttää ihmistä prosessissa. Tämä luo virtauksen, jossa käyttäjät voivat antaa palautetta agenteille ajon aikana. Käyttäjät toimivat ikään kuin agenteina moni-agenttijärjestelmässä hyväksymällä tai lopettamalla käynnissä olevan prosessin.

![Ihminen prosessissa](../../../translated_images/fi/human-in-the-loop.5f0068a678f62f4f.webp)

Tässä on esimerkki koodipätkä Microsoft Agent Frameworkin käytöstä, joka havainnollistaa, miten tämä konsepti toteutetaan:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Luo tarjoaja ihmisen hallitseman hyväksynnän kanssa
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Luo agentti ihmisen hyväksymisvaiheella
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

Luotettavien tekoälyagenttien rakentaminen vaatii huolellista suunnittelua, vankkoja turvallisuustoimenpiteitä ja jatkuvaa iterointia. Rakentamalla rakenteellisia meta-kehotusjärjestelmiä, ymmärtämällä mahdollisia uhkia ja soveltamalla lieventämisstrategioita, kehittäjät voivat luoda tekoälyagentteja, jotka ovat sekä turvallisia että tehokkaita. Lisäksi ihmisen sisällyttäminen prosessiin varmistaa, että tekoälyagentit pysyvät käyttäjien tarpeiden kanssa linjassa minimoiden samalla riskejä. Tekoälyn kehittyessä entisestään on proaktiivinen turvallisuus-, yksityisyys- ja eettinen ote avain luottamuksen ja luotettavuuden edistämiseen tekoälypohjaisissa järjestelmissä.

### Onko sinulla lisää kysymyksiä luotettavien tekoälyagenttien rakentamisesta?

Liity [Microsoft Foundry Discordiin](https://aka.ms/ai-agents/discord) tapaamaan muita oppijoita, osallistumaan tilaisuuksiin ja saamaan vastauksia tekoälyagenttikysymyksiisi.

## Lisäresurssit

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Vastuullinen tekoäly - yleiskatsaus</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Generatiivisten tekoälymallien ja tekoälysovellusten arviointi</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Turvallisuusjärjestelmäviestit</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Riskinarviointipohja</a>

## Edellinen oppitunti

[Agenttinen RAG](../05-agentic-rag/README.md)

## Seuraava oppitunti

[Suunnittelumalli suunnittelu](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty tekoälypohjaisella käännöspalvelulla [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäinen asiakirja omalla kielellään on ensisijainen ja virallinen lähde. Tärkeissä asioissa suosittelemme ammattimaista ihmiskäännöstä. Emme ole vastuussa tästä käännöksestä johtuvista mahdollisista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->