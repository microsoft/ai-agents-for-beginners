[![Istraživanje AI Okvira za Agente](../../../translated_images/hr/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Kliknite na gornju sliku za pregled videozapisa ove lekcije)_

# Istražite Okvire za AI Agente

Okviri za AI agente su softverske platforme dizajnirane za pojednostavljenje stvaranja, implementacije i upravljanja AI agentima. Ovi okviri pružaju programerima unaprijed izrađene komponente, apstrakcije i alate koji pojednostavljuju razvoj složenih AI sustava.

Ovi okviri pomažu programerima da se usredotoče na jedinstvene aspekte svojih aplikacija pružajući standardizirane pristupe uobičajenim izazovima u razvoju AI agenata. Oni poboljšavaju skalabilnost, pristupačnost i učinkovitost u izgradnji AI sustava.

## Uvod

Ova lekcija će obuhvatiti:

- Što su Okviri za AI Agente i što omogućuju programerima da postignu?
- Kako timovi mogu brzo prototipizirati, iterirati i poboljšavati sposobnosti svog agenta?
- Koje su razlike između okvira i alata koje je stvorio Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> i <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Mogu li integrirati postojeće alate iz Azure ekosustava izravno ili trebam samostalna rješenja?
- Što je Azure AI Agents usluga i kako mi pomaže?

## Ciljevi učenja

Ciljevi ove lekcije su pomoći vam da razumijete:

- Ulogu Okvira za AI Agente u razvoju AI.
- Kako iskoristiti Okvire za AI Agente za izgradnju inteligentnih agenata.
- Ključne sposobnosti koje omogućuju Okviri za AI Agente.
- Razlike između Microsoft Agent Frameworka i Azure AI Agent Service.

## Što su Okviri za AI Agente i što omogućuju programerima raditi?

Tradicionalni AI okviri mogu vam pomoći integrirati AI u vaše aplikacije i poboljšati ih na sljedeće načine:

- **Personalizacija**: AI može analizirati ponašanje korisnika i preferencije kako bi pružio personalizirane preporuke, sadržaj i iskustva.  
Primjer: Streaming servisi poput Netflixa koriste AI za predlaganje filmova i serija na temelju povijesti gledanja, povećavajući angažman i zadovoljstvo korisnika.
- **Automatizacija i učinkovitost**: AI može automatizirati ponavljajuće zadatke, pojednostaviti tokove rada i poboljšati operativnu učinkovitost.  
Primjer: Aplikacije za korisničku podršku koriste AI pokretane chatbotove za rukovanje čestim upitima, smanjujući vrijeme odgovora i oslobađajući ljudske agente za složenija pitanja.
- **Poboljšano korisničko iskustvo**: AI može poboljšati opće korisničko iskustvo pružajući inteligentne funkcije poput prepoznavanja glasa, obrade prirodnog jezika i prediktivnog teksta.  
Primjer: Virtualni asistenti poput Siri i Google Assistant koriste AI za razumijevanje i reagiranje na glasovne naredbe, olakšavajući korisnicima interakciju s uređajima.

### Sve to zvuči sjajno, zar ne? Pa zašto nam treba AI Agent Framework?

Okviri za AI agente predstavljaju nešto više od običnih AI okvira. Dizajnirani su za omogućavanje stvaranja inteligentnih agenata koji mogu komunicirati s korisnicima, drugim agentima i okolinom kako bi ostvarili određene ciljeve. Ti agenti mogu pokazivati autonomno ponašanje, donositi odluke i prilagođavati se promjenjivim uvjetima. Pogledajmo neke ključne sposobnosti koje omogućuju Okviri za AI Agente:

- **Suradnja i koordinacija agenata**: Omogućuju stvaranje više AI agenata koji mogu raditi zajedno, komunicirati i koordinirati se za rješavanje složenih zadataka.
- **Automatizacija i upravljanje zadacima**: Pružaju mehanizme za automatizaciju višestupanjskih procesa, dodjelu zadataka i dinamičko upravljanje zadacima među agentima.
- **Kontekstualno razumijevanje i prilagodba**: Opremljuju agente sposobnošću razumijevanja konteksta, prilagođavanja promjenjivim uvjetima i donošenja odluka na temelju informacija u stvarnom vremenu.

Ukratko, agenti vam omogućuju više, podižu automatizaciju na novu razinu i stvaraju inteligentnije sustave koji se mogu prilagođavati i učiti iz svoje okoline.

## Kako brzo prototipizirati, iterirati i poboljšavati sposobnosti agenta?

Ovo je brzo mijenjajuće područje, ali postoje neke stvari koje su zajedničke za većinu AI Okvira za Agente i mogu vam pomoći brzo prototipizirati i iterirati, poput modulskih komponenti, suradničkih alata i učenja u stvarnom vremenu. Pogledajmo ih detaljnije:

- **Korištenje modularnih komponenti**: AI SDK-ovi nude unaprijed izrađene komponente kao što su AI i memorijski konektori, pozivanje funkcija koristeći prirodni jezik ili dodatke koda, predloške prompta i slično.
- **Iskorištavanje suradničkih alata**: Dizajnirajte agente s posebnim ulogama i zadacima, omogućujući im testiranje i usavršavanje suradničkih tijekova rada.
- **Učenje u stvarnom vremenu**: Implementirajte petlje povratne informacije u kojima agenti uče iz interakcija i dinamički prilagođavaju svoje ponašanje.

### Korištenje modularnih komponenti

SDK-ovi poput Microsoft Agent Frameworka nude unaprijed izrađene komponente kao što su AI konektori, definicije alata i upravljanje agentima.

**Kako timovi mogu koristiti ove komponente**: Timovi mogu brzo sastaviti ove komponente kako bi napravili funkcionalan prototip bez potrebe za početkom od nule, što omogućuje brzo eksperimentiranje i iteraciju.

**Kako to funkcionira u praksi**: Možete koristiti unaprijed izrađeni parser za izdvajanje informacija iz korisničkog unosa, memorijski modul za pohranu i dohvat podataka te generator promptova za interakciju s korisnicima, sve bez potrebe za izradom ovih komponenti od početka.

**Primjer koda**. Pogledajmo primjer kako koristiti Microsoft Agent Framework s `AzureAIProjectAgentProvider` da model odgovara na korisnički unos pozivanjem alata:

``` python
# Microsoft Agent Framework Python Primjer

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# Definirajte uzorak funkcije alata za rezervaciju putovanja
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # Primjer izlaza: Vaš let za New York 1. siječnja 2025. uspješno je rezerviran. Sretan put! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Iz ovog primjera vidite kako se može iskoristiti unaprijed izrađeni parser za izdvajanje ključnih informacija iz korisničkog unosa, poput polazišta, odredišta i datuma za zahtjev rezervacije leta. Ovaj modularni pristup vam omogućuje fokus na logiku visokog nivoa.

### Iskorištavanje suradničkih alata

Okviri poput Microsoft Agent Frameworka olakšavaju stvaranje više agenata koji mogu raditi zajedno.

**Kako timovi mogu koristiti ove alate**: Timovi mogu dizajnirati agente s posebnim ulogama i zadacima, omogućujući im testiranje i usavršavanje suradničkih tijekova rada te poboljšanje ukupne učinkovitosti sustava.

**Kako to funkcionira u praksi**: Možete kreirati tim agenata gdje svaki agent ima specijaliziranu funkciju, poput dohvaćanja podataka, analize ili donošenja odluka. Ti agenti mogu komunicirati i dijeliti informacije kako bi ostvarili zajednički cilj, poput odgovaranja na korisnički upit ili izvršenja zadatka.

**Primjer koda (Microsoft Agent Framework)**:

```python
# Kreiranje više agenata koji rade zajedno koristeći Microsoft Agent Framework

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Agent za dohvat podataka
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Agent za analizu podataka
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Pokreni agente redom na zadatku
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

U prethodnom kodu vidite kako možete stvoriti zadatak koji uključuje suradnju više agenata za analizu podataka. Svaki agent obavlja specifičnu funkciju, a zadatak se izvršava koordinacijom agenata kako bi se postigao željeni rezultat. Stvaranjem posvećenih agenata s posebnim ulogama možete poboljšati učinkovitost i izvedbu zadatka.

### Učenje u stvarnom vremenu

Napredni okviri pružaju sposobnosti razumijevanja konteksta i prilagodbe u stvarnom vremenu.

**Kako timovi mogu koristiti ove sposobnosti**: Timovi mogu implementirati petlje povratne informacije u kojima agenti uče iz interakcija i dinamički prilagođavaju svoje ponašanje, što vodi do kontinuiranog poboljšanja i usavršavanja sposobnosti.

**Kako to funkcionira u praksi**: Agent može analizirati povratne informacije korisnika, podatke o okolini i ishod zadataka kako bi ažurirao svoju bazu znanja, prilagodio algoritme donošenja odluka i tijekom vremena poboljšao izvedbu. Ovaj iterativni proces učenja omogućuje agentima da se prilagođavaju promjenjivim uvjetima i preferencijama korisnika, povećavajući ukupnu učinkovitost sustava.

## Koje su razlike između Microsoft Agent Frameworka i Azure AI Agent Service?

Postoji mnogo načina za usporedbu ovih pristupa, no pogledajmo ključne razlike u pogledu dizajna, sposobnosti i ciljanih upotreba:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework pruža pojednostavljeni SDK za izgradnju AI agenata koristeći `AzureAIProjectAgentProvider`. Omogućuje programerima stvaranje agenata koji koriste Azure OpenAI modele s ugrađenim pozivanjem alata, upravljanjem razgovorom i sigurnošću razine poduzeća putem Azure identiteta.

**Primjene**: Izrada AI agenata spremnih za produkciju s korištenjem alata, višestupanjskim tijekovima rada i scenarijima integracije za poduzeća.

Evo nekoliko važnih osnovnih koncepata Microsoft Agent Frameworka:

- **Agenti**. Agent se stvara putem `AzureAIProjectAgentProvider` i konfigurira imenom, uputama i alatima. Agent može:
  - **Obrađivati korisničke poruke** i generirati odgovore koristeći Azure OpenAI modele.
  - **Automatski pozivati alate** na temelju konteksta razgovora.
  - **Održavati stanje razgovora** kroz više interakcija.

  Evo dijela koda koji pokazuje kako stvoriti agenta:

    ```python
    import os
    from agent_framework.azure import AzureAIProjectAgentProvider
    from azure.identity import AzureCliCredential

    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **Alati**. Okvir podržava definiranje alata kao Python funkcija koje agent može automatski pozivati. Alati se registriraju prilikom stvaranja agenta:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = await provider.create_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **Koordinacija više agenata**. Možete stvoriti više agenata s različitim specijalizacijama i koordinirati njihov rad:

    ```python
    planner = await provider.create_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = await provider.create_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Integracija Azure Identiteta**. Okvir koristi `AzureCliCredential` (ili `DefaultAzureCredential`) za sigurnu autentifikaciju bez ključeva, eliminirajući potrebu za upravljanjem API ključevima izravno.

## Azure AI Agent Service

Azure AI Agent Service je noviji dodatak, predstavljen na Microsoft Ignite 2024. Omogućava razvoj i implementaciju AI agenata s fleksibilnijim modelima, poput izravnog pozivanja open-source LLM modela kao što su Llama 3, Mistral i Cohere.

Azure AI Agent Service pruža jače sigurnosne mehanizme i metode pohrane podataka, što ga čini prikladnim za aplikacije poduzeća.

Radi odmah s Microsoft Agent Frameworkom za izgradnju i implementaciju agenata.

Ova je usluga trenutno u javnoj pretpregledu i podržava Python i C# za razvoj agenata.

Koristeći Azure AI Agent Service Python SDK, možemo stvoriti agenta s alatom koji definira korisnik:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Definiraj funkcije alata
def get_specials() -> str:
    """Provides a list of specials from the menu."""
    return """
    Special Soup: Clam Chowder
    Special Salad: Cobb Salad
    Special Drink: Chai Tea
    """

def get_item_price(menu_item: str) -> str:
    """Provides the price of the requested menu item."""
    return "$9.99"


async def main() -> None:
    credential = DefaultAzureCredential()
    project_client = AIProjectClient.from_connection_string(
        credential=credential,
        conn_str="your-connection-string",
    )

    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="Host",
        instructions="Answer questions about the menu.",
        tools=[get_specials, get_item_price],
    )

    thread = project_client.agents.create_thread()

    user_inputs = [
        "Hello",
        "What is the special soup?",
        "How much does that cost?",
        "Thank you",
    ]

    for user_input in user_inputs:
        print(f"# User: '{user_input}'")
        message = project_client.agents.create_message(
            thread_id=thread.id,
            role="user",
            content=user_input,
        )
        run = project_client.agents.create_and_process_run(
            thread_id=thread.id, agent_id=agent.id
        )
        messages = project_client.agents.list_messages(thread_id=thread.id)
        print(f"# Agent: {messages.data[0].content[0].text.value}")


if __name__ == "__main__":
    asyncio.run(main())
```

### Osnovni koncepti

Azure AI Agent Service ima sljedeće osnovne koncepte:

- **Agent**. Azure AI Agent Service integrira se s Microsoft Foundryjem. Unutar AI Foundryja, AI agent djeluje kao "pametna" mikroservisna jedinica koja se može koristiti za odgovaranje na pitanja (RAG), izvođenje akcija ili potpunu automatizaciju tijekova rada. To ostvaruje kombiniranjem moći generativnih AI modela s alatima koji mu omogućuju pristup i interakciju s izvorima podataka iz stvarnog svijeta. Evo primjera agenta:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    U ovom primjeru agent je stvoren s modelom `gpt-4o-mini`, imenom `my-agent` i uputama `You are helpful agent`. Agent je opremljen alatima i resursima za izvođenje zadataka interpretacije koda.

- **Niti i poruke**. Nit je još jedan važan koncept. Ona predstavlja razgovor ili interakciju između agenta i korisnika. Niti se mogu koristiti za praćenje tijeka razgovora, pohranu kontekstualnih informacija i upravljanje stanjem interakcije. Evo primjera niti:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Zatražite od agenta da obavi posao na threadu
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Dohvatite i zabilježite sve poruke da vidite odgovor agenta
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    U prethodnom kodu stvorena je nit. Potom se šalje poruka niti. Pozivom `create_and_process_run` agentu se traži da obavi rad na niti. Na kraju se dohvaćaju i zapisuju poruke da bi se vidio odgovor agenta. Poruke prikazuju tijek razgovora između korisnika i agenta. Također je važno razumjeti da poruke mogu biti različitih tipova poput teksta, slike ili datoteke, što znači da je rad agenta mogao rezultat dovesti do na primjer slike ili tekstualnog odgovora. Kao programer možete ovu informaciju dalje obraditi ili je prikazati korisniku.

- **Integracija s Microsoft Agent Frameworkom**. Azure AI Agent Service savršeno surađuje s Microsoft Agent Frameworkom, što znači da možete graditi agente koristeći `AzureAIProjectAgentProvider` i implementirati ih kroz Agent Service za produkcijske scenarije.

**Primjene**: Azure AI Agent Service je osmišljen za aplikacije poduzeća koje zahtijevaju sigurnu, skalabilnu i fleksibilnu implementaciju AI agenata.

## Koja je razlika između ovih pristupa?

Čini se da postoji preklapanje, ali postoje ključne razlike u pogledu dizajna, sposobnosti i ciljanih slučajeva upotrebe:

- **Microsoft Agent Framework (MAF)**: Produkcijski spreman SDK za izgradnju AI agenata. Pruža pojednostavljeni API za stvaranje agenata s pozivanjem alata, upravljanjem razgovorom i integracijom Azure identiteta.
- **Azure AI Agent Service**: Platforma i usluga implementacije u Azure Foundryju za agente. Nudi ugrađenu povezivost s uslugama poput Azure OpenAI, Azure AI Search, Bing Search i izvršavanje koda.

Još niste sigurni koju odabrati?

### Primjeri upotrebe

Pogledajmo ako vam možemo pomoći kroz neke uobičajene slučajeve:

> P: Izrađujem produkcijske AI aplikacije s agentima i želim brzo početi
>

>O: Microsoft Agent Framework je odličan izbor. Pruža jednostavan, Python pristup putem `AzureAIProjectAgentProvider` koji vam omogućuje definiranje agenata s alatima i uputama u samo nekoliko redaka koda.

> P: Trebam implementaciju razine poduzeća s Azure integracijama poput Search i izvršavanja koda
>
>O: Azure AI Agent Service je najbolji izbor. To je platformska usluga s ugrađenim mogućnostima za više modela, Azure AI Search, Bing Search i Azure Functions. Omogućuje jednostavnu izgradnju agenata u Foundry Portalu i njihovu implementaciju u velikom opsegu.
 
> P: Još sam zbunjen, samo mi dajte jednu opciju
>
>O: Počnite s Microsoft Agent Frameworkom da izgradite svoje agente, a zatim koristite Azure AI Agent Service kad trebate implementirati i skalirati na produkciji. Ovaj pristup omogućuje vam brzu iteraciju na logici agenta uz jasan put do implementacije na razini poduzeća.

Sažmimo ključne razlike u tablici:

| Okvir | Fokus | Osnovni Koncepti | Primjene |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Pojednostavljeni SDK za agente s pozivanjem alata | Agenti, Alati, Azure Identitet | Izgradnja AI agenata, korištenje alata, višestupanjski tijekovi rada |
| Azure AI Agent Service | Fleksibilni modeli, sigurnost za poduzeća, generiranje koda, pozivanje alata | Modularnost, Suradnja, Orkestracija procesa | Sigurna, skalabilna i fleksibilna implementacija AI agenata |

## Mogu li integrirati svoje postojeće alate iz Azure ekosustava izravno ili trebam samostalna rješenja?
Odgovor je da, možete integrirati svoje postojeće alate iz Azure ekosustava izravno s Azure AI Agent Service, posebno jer je izgrađen da besprijekorno radi s drugim Azure uslugama. Na primjer, mogli biste integrirati Bing, Azure AI Search i Azure Functions. Postoji i duboka integracija s Microsoft Foundry.

Microsoft Agent Framework također se integrira s Azure uslugama putem `AzureAIProjectAgentProvider` i Azure identiteta, omogućujući vam da pozivate Azure usluge izravno iz svojih agentnih alata.

## Primjeri koda

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Imate li još pitanja o AI Agent Framework-ovima?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) kako biste upoznali druge učenike, sudjelovali na konzultacijama i dobili odgovore na svoja pitanja o AI agentima.

## Reference

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>

## Prethodna lekcija

[Uvod u AI agente i primjene agenata](../01-intro-to-ai-agents/README.md)

## Sljedeća lekcija

[Razumijevanje agentnih dizajnerskih obrazaca](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->