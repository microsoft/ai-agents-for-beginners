<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "498802b4c3c3cc486b86f27a12cebb34",
  "translation_date": "2025-08-29T17:11:59+00:00",
  "source_file": "06-building-trustworthy-agents/README.md",
  "language_code": "fi"
}
-->
[![Luotettavat tekoälyagentit](../../../translated_images/lesson-6-thumbnail.a58ab36c099038d4f786c2b0d5d6e89f41f4c2ecc05ab10b67bced2695eeb218.fi.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Klikkaa yllä olevaa kuvaa katsoaksesi tämän oppitunnin videon)_

# Luotettavien tekoälyagenttien rakentaminen

## Johdanto

Tässä oppitunnissa käsitellään:

- Kuinka rakentaa ja ottaa käyttöön turvallisia ja tehokkaita tekoälyagentteja.
- Tärkeitä turvallisuusnäkökohtia tekoälyagenttien kehittämisessä.
- Kuinka ylläpitää tietojen ja käyttäjien yksityisyyttä tekoälyagentteja kehitettäessä.

## Oppimistavoitteet

Tämän oppitunnin jälkeen osaat:

- Tunnistaa ja vähentää riskejä tekoälyagentteja luodessasi.
- Toteuttaa turvallisuustoimenpiteitä varmistaaksesi, että tiedot ja käyttöoikeudet hallitaan asianmukaisesti.
- Luoda tekoälyagentteja, jotka säilyttävät tietosuojan ja tarjoavat laadukkaan käyttäjäkokemuksen.

## Turvallisuus

Aloitetaan tarkastelemalla, kuinka rakentaa turvallisia agenttipohjaisia sovelluksia. Turvallisuus tarkoittaa, että tekoälyagentti toimii suunnitellusti. Agenttipohjaisten sovellusten kehittäjinä meillä on käytössämme menetelmiä ja työkaluja turvallisuuden maksimoimiseksi:

### Järjestelmäviestikehyksen rakentaminen

Jos olet koskaan rakentanut tekoälysovelluksen käyttäen suuria kielimalleja (LLM), tiedät, kuinka tärkeää on suunnitella vankka järjestelmäkehotus tai -viesti. Nämä kehotteet määrittävät säännöt, ohjeet ja suuntaviivat sille, miten LLM on vuorovaikutuksessa käyttäjän ja datan kanssa.

Tekoälyagenttien kohdalla järjestelmäkehotus on vielä tärkeämpi, koska agentit tarvitsevat erittäin tarkkoja ohjeita suorittaakseen niille suunnitellut tehtävät.

Jotta voimme luoda skaalautuvia järjestelmäkehotteita, voimme käyttää järjestelmäviestikehystä rakentaessamme yhtä tai useampaa agenttia sovellukseemme:

![Järjestelmäviestikehyksen rakentaminen](../../../translated_images/system-message-framework.3a97368c92d11d6814577b03cd128ec8c71a5fd1e26f341835cfa5df59ae87ae.fi.png)

#### Vaihe 1: Luo metajärjestelmäviesti

Metakehotetta käytetään LLM:ssä luomaan järjestelmäkehotteet niille agenteille, jotka luomme. Suunnittelemme sen malliksi, jotta voimme tehokkaasti luoda useita agentteja tarvittaessa.

Tässä on esimerkki metajärjestelmäviestistä, jonka voisimme antaa LLM:lle:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Vaihe 2: Luo peruskehotus

Seuraava vaihe on luoda peruskehotus, joka kuvaa tekoälyagentin. Sinun tulisi sisällyttää agentin rooli, tehtävät, jotka agentti suorittaa, ja muut agentin vastuut.

Tässä on esimerkki:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Vaihe 3: Anna perusjärjestelmäviesti LLM:lle

Nyt voimme optimoida tämän järjestelmäviestin antamalla metajärjestelmäviestin järjestelmäviestinä ja perusjärjestelmäviestimme.

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

#### Vaihe 4: Iteroi ja paranna

Tämän järjestelmäviestikehyksen arvo on siinä, että se helpottaa useiden agenttien järjestelmäviestien luomista ja mahdollistaa järjestelmäviestien parantamisen ajan myötä. On harvinaista, että järjestelmäviesti toimii täydellisesti ensimmäisellä kerralla koko käyttötapauksessa. Pienet muutokset ja parannukset perusjärjestelmäviestiin ja sen ajaminen järjestelmän läpi mahdollistavat tulosten vertailun ja arvioinnin.

## Uhkien ymmärtäminen

Luotettavien tekoälyagenttien rakentamiseksi on tärkeää ymmärtää ja vähentää tekoälyagenttiin kohdistuvia riskejä ja uhkia. Tarkastellaan joitakin erilaisia uhkia ja sitä, kuinka voit paremmin suunnitella ja valmistautua niihin.

![Uhka-analyysi](../../../translated_images/understanding-threats.89edeada8a97fc0f7053558567d5dd27c0c333b74e47fffdde490fa6777a4c17.fi.png)

### Tehtävät ja ohjeet

**Kuvaus:** Hyökkääjät yrittävät muuttaa tekoälyagentin ohjeita tai tavoitteita kehotteiden tai syötteiden manipuloinnin kautta.

**Torjunta:** Suorita validointitarkistuksia ja syötteen suodatuksia havaitaksesi mahdollisesti vaaralliset kehotteet ennen niiden käsittelyä tekoälyagentin toimesta. Koska nämä hyökkäykset vaativat yleensä toistuvaa vuorovaikutusta agentin kanssa, keskustelukertojen rajoittaminen on toinen tapa estää tällaisia hyökkäyksiä.

### Pääsy kriittisiin järjestelmiin

**Kuvaus:** Jos tekoälyagentilla on pääsy järjestelmiin ja palveluihin, jotka sisältävät arkaluonteisia tietoja, hyökkääjät voivat vaarantaa agentin ja näiden palveluiden välisen viestinnän. Tämä voi olla suoria hyökkäyksiä tai epäsuoria yrityksiä saada tietoa näistä järjestelmistä agentin kautta.

**Torjunta:** Tekoälyagenteilla tulisi olla pääsy järjestelmiin vain tarpeen mukaan tällaisten hyökkäysten estämiseksi. Agentin ja järjestelmän välinen viestintä tulisi myös suojata. Autentikoinnin ja käyttöoikeuksien hallinnan toteuttaminen on toinen tapa suojata tätä tietoa.

### Resurssien ja palveluiden ylikuormitus

**Kuvaus:** Tekoälyagentit voivat käyttää erilaisia työkaluja ja palveluita tehtävien suorittamiseen. Hyökkääjät voivat käyttää tätä kykyä hyökätäkseen näihin palveluihin lähettämällä suuren määrän pyyntöjä tekoälyagentin kautta, mikä voi johtaa järjestelmäkatkoksiin tai korkeisiin kustannuksiin.

**Torjunta:** Ota käyttöön käytäntöjä, jotka rajoittavat tekoälyagentin tekemien pyyntöjen määrää palveluun. Keskustelukertojen ja pyyntöjen rajoittaminen tekoälyagentille on toinen tapa estää tällaisia hyökkäyksiä.

### Tietopohjan myrkyttäminen

**Kuvaus:** Tämäntyyppinen hyökkäys ei kohdistu suoraan tekoälyagenttiin, vaan sen käyttämään tietopohjaan ja muihin palveluihin. Tämä voi sisältää datan tai tiedon korruptoimisen, jota tekoälyagentti käyttää tehtävän suorittamiseen, mikä johtaa puolueellisiin tai ei-toivottuihin vastauksiin käyttäjälle.

**Torjunta:** Suorita säännöllisiä tarkistuksia datalle, jota tekoälyagentti käyttää työnkulussaan. Varmista, että pääsy tähän dataan on suojattu ja että vain luotetut henkilöt voivat muuttaa sitä tällaisen hyökkäyksen estämiseksi.

### Virheiden ketjuuntuminen

**Kuvaus:** Tekoälyagentit käyttävät erilaisia työkaluja ja palveluita tehtävien suorittamiseen. Hyökkääjien aiheuttamat virheet voivat johtaa muiden järjestelmien epäonnistumiseen, joihin tekoälyagentti on yhteydessä, mikä tekee hyökkäyksestä laajemman ja vaikeammin korjattavan.

**Torjunta:** Yksi tapa välttää tämä on antaa tekoälyagentin toimia rajoitetussa ympäristössä, kuten suorittaa tehtäviä Docker-kontissa, estääkseen suorat järjestelmähyökkäykset. Takaisinkytkentämekanismien ja uudelleenyrittämislogiikan luominen, kun tietyt järjestelmät vastaavat virheellä, on toinen tapa estää laajempia järjestelmäkatkoksia.

## Ihminen mukana prosessissa

Toinen tehokas tapa rakentaa luotettavia tekoälyagenttijärjestelmiä on käyttää ihmistä mukana prosessissa. Tämä luo työnkulun, jossa käyttäjät voivat antaa palautetta agenteille niiden suorittaessa tehtäviä. Käyttäjät toimivat käytännössä agenteina monen agentin järjestelmässä ja voivat hyväksyä tai keskeyttää käynnissä olevan prosessin.

![Ihminen mukana prosessissa](../../../translated_images/human-in-the-loop.5f0068a678f62f4fc8373d5b78c4c22f35d9e4da35c93f66c3b634c1774eff34.fi.png)

Tässä on koodiesimerkki AutoGenin avulla, joka näyttää, kuinka tämä konsepti toteutetaan:

```python

# Create the agents.
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
assistant = AssistantAgent("assistant", model_client=model_client)
user_proxy = UserProxyAgent("user_proxy", input_func=input)  # Use input() to get user input from console.

# Create the termination condition which will end the conversation when the user says "APPROVE".
termination = TextMentionTermination("APPROVE")

# Create the team.
team = RoundRobinGroupChat([assistant, user_proxy], termination_condition=termination)

# Run the conversation and stream to the console.
stream = team.run_stream(task="Write a 4-line poem about the ocean.")
# Use asyncio.run(...) when running in a script.
await Console(stream)

```

## Yhteenveto

Luotettavien tekoälyagenttien rakentaminen vaatii huolellista suunnittelua, vahvoja turvallisuustoimenpiteitä ja jatkuvaa iterointia. Rakentamalla rakenteellisia metakehotusjärjestelmiä, ymmärtämällä mahdollisia uhkia ja soveltamalla torjuntastrategioita kehittäjät voivat luoda tekoälyagentteja, jotka ovat sekä turvallisia että tehokkaita. Lisäksi ihmisen mukanaolon sisällyttäminen prosessiin varmistaa, että tekoälyagentit pysyvät käyttäjien tarpeiden mukaisina ja minimoivat riskit. Tekoälyn kehittyessä edelleen turvallisuuden, yksityisyyden ja eettisten näkökohtien proaktiivinen huomioiminen on avainasemassa luottamuksen ja luotettavuuden edistämisessä tekoälypohjaisissa järjestelmissä.

### Onko sinulla lisää kysymyksiä luotettavien tekoälyagenttien rakentamisesta?

Liity [Azure AI Foundry Discordiin](https://aka.ms/ai-agents/discord) tavataksesi muita oppijoita, osallistuaksesi toimistoaikoihin ja saadaksesi vastauksia tekoälyagentteihin liittyviin kysymyksiisi.

## Lisäresurssit

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Vastuullisen tekoälyn yleiskatsaus</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Generatiivisten tekoälymallien ja tekoälysovellusten arviointi</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Turvallisuusjärjestelmäviestit</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Riskinarviointimalli</a>

## Edellinen oppitunti

[Agenttipohjainen RAG](../05-agentic-rag/README.md)

## Seuraava oppitunti

[Suunnittelumalli](../07-planning-design/README.md)

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.