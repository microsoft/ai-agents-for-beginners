[![Istraživanje AI okvira za agente](../../../translated_images/hr/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Kliknite na gornju sliku za pregled video lekcije)_

# Istražite AI okvire za agente

AI okviri za agente su softverske platforme dizajnirane za pojednostavljenje kreiranja, implementacije i upravljanja AI agentima. Ovi okviri developerima pružaju unaprijed izrađene komponente, apstrakcije i alate koji ubrzavaju razvoj složenih AI sustava.

Ovi okviri pomažu developerima da se usredotoče na jedinstvene aspekte svojih aplikacija pružajući standardizirane pristupe čestim izazovima u razvoju AI agenata. Oni povećavaju skalabilnost, dostupnost i učinkovitost u izgradnji AI sustava.

## Uvod

Ova lekcija će obuhvatiti:

- Što su AI okviri za agente i što omogućuju developerima?
- Kako timovi mogu koristiti ove okvire za brzo prototipiranje, iteriranje i poboljšanje sposobnosti svojih agenata?
- Koje su razlike između okvira i alata koje je stvorio Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> i <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Mogu li integrirati svoje postojeće alate iz Azure ekosustava izravno ili trebam samostalna rješenja?
- Što je Azure AI Agents service i kako mi to pomaže?

## Ciljevi učenja

Ciljevi ove lekcije su pomoći vam da razumijete:

- Ulogu AI okvira za agente u razvoju AI-ja.
- Kako iskoristiti AI okvire za agente za izgradnju inteligentnih agenata.
- Ključne mogućnosti koje omogućuju AI okviri za agente.
- Razlike između Microsoft Agent Frameworka i Azure AI Agent Servicea.

## Što su AI okviri za agente i što omogućuju developerima?

Tradicionalni AI okviri mogu pomoći u integraciji AI-ja u vaše aplikacije i poboljšanju tih aplikacija na sljedeće načine:

- **Personalizacija**: AI može analizirati ponašanje i preferencije korisnika te pružiti personalizirane preporuke, sadržaj i iskustva.
Primjer: Streaming servisi poput Netflixa koriste AI da predlažu filmove i emisije temeljem povijesti gledanja, čime povećavaju angažman i zadovoljstvo korisnika.
- **Automatizacija i učinkovitost**: AI može automatizirati ponavljajuće zadatke, pojednostaviti radne tijekove i poboljšati operativnu učinkovitost.
Primjer: Aplikacije za korisničku podršku koriste AI chatbote za rješavanje čestih upita, smanjujući vrijeme odgovora i oslobađajući ljudske agente za složenije probleme.
- **Poboljšano korisničko iskustvo**: AI može poboljšati ukupno korisničko iskustvo pružajući inteligentne funkcije poput prepoznavanja glasa, obrade prirodnog jezika i prediktivnog teksta.
Primjer: Virtualni asistenti poput Siri i Google Assistanta koriste AI za razumijevanje i odgovaranje na glasovne naredbe, olakšavajući korisnicima interakciju s uređajima.

### Sve to zvuči sjajno, ali zašto nam treba AI okvira za agente?

AI okviri za agente predstavljaju više od običnih AI okvira. Oni su dizajnirani za omogućavanje kreiranja inteligentnih agenata koji mogu komunicirati s korisnicima, drugim agentima i okolinom kako bi postigli specifične ciljeve. Ti agenti mogu pokazivati autonomno ponašanje, donositi odluke i prilagođavati se promjenjivim uvjetima. Pogledajmo neke ključne mogućnosti koje omogućuju AI okviri za agente:

- **Suradnja i koordinacija agenata**: Omogućuju kreiranje više AI agenata koji mogu raditi zajedno, komunicirati i koordinirati se za rješavanje složenih zadataka.
- **Automatizacija i upravljanje zadacima**: Pružaju mehanizme za automatizaciju višestupanjskih radnih toka, delegiranje zadataka i dinamičko upravljanje zadacima među agentima.
- **Kontekstualno razumijevanje i prilagodba**: Opremljuju agente sposobnošću razumijevanja konteksta, prilagodbe promjenjivoj okolini i donošenja odluka na temelju informacija u stvarnom vremenu.

Ukratko, agenti vam omogućuju više, vode automatizaciju na višu razinu te stvaraju inteligentnije sustave koji mogu učiti i prilagođavati se svojoj okolini.

## Kako brzo prototipirati, iterirati i poboljšati sposobnosti agenta?

Ovo je brzo mijenjajuće područje, ali postoje neke zajedničke stvari kod većine AI okvira za agente koje vam mogu pomoći da brzo prototipirate i iterirate: modularne komponente, alati za suradnju i učenje u stvarnom vremenu. Pogledajmo to detaljnije:

- **Koristite modularne komponente**: AI SDK-ovi nude unaprijed izrađene komponente poput AI i memorijskih konektora, poziva funkcija pomoću prirodnog jezika ili dodataka za kod, predložaka za naredbe i više.
- **Iskoristite alate za suradnju**: Dizajnirajte agente s određenim ulogama i zadacima, omogućujući testiranje i usavršavanje suradničkih radnih tijekova.
- **Učite u stvarnom vremenu**: Implementirajte povratne petlje u kojima agenti uče iz interakcija i dinamički prilagođavaju svoje ponašanje.

### Koristite modularne komponente

SDK-ovi poput Microsoft Agent Frameworka nude unaprijed izrađene komponente poput AI konektora, definicija alata i upravljanja agentima.

**Kako to koriste timovi**: Timovi mogu brzo sastaviti ove komponente da kreiraju funkcionalni prototip bez početka od nule, omogućujući brze eksperimente i iteracije.

**Kako to funkcionira u praksi**: Možete koristiti unaprijed izrađeni parser za izdvajanje informacija iz korisničkog unosa, memorijsku komponentu za pohranu i dohvat podataka, te generator naredbi za interakciju s korisnicima, sve bez potrebe za izradom ovih komponenti od početka.

**Primjer koda**. Pogledajmo primjer kako koristiti Microsoft Agent Framework s `AzureAIProjectAgentProvider` kako bi model odgovorio na korisnički unos pozivajući alat:

``` python
# Primjer Microsoft Agent Frameworka u Pythonu

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# Definirajte primjer funkcije alata za rezervaciju putovanja
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

Iz ovog primjera vidite kako iskoristiti unaprijed izrađeni parser za izdvajanje ključnih informacija iz korisničkog unosa, poput polazišta, odredišta i datuma zahtjeva za rezervaciju leta. Ovaj modularni pristup vam omogućava da se usredotočite na višerazinsku logiku.

### Iskoristite alate za suradnju

Okviri poput Microsoft Agent Frameworka olakšavaju stvaranje više agenata koji mogu raditi zajedno.

**Kako to koriste timovi**: Timovi mogu dizajnirati agente s određenim ulogama i zadacima, omogućujući testiranje i usavršavanje suradničkih radnih tijekova te poboljšanje ukupne učinkovitosti sustava.

**Kako to funkcionira u praksi**: Možete stvoriti tim agenata gdje svaki agent ima specijaliziranu funkciju, poput dohvaćanja podataka, analize ili donošenja odluka. Ti agenti mogu međusobno komunicirati i dijeliti informacije kako bi postigli zajednički cilj, poput odgovora na korisnički upit ili dovršetka zadatka.

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

# Pokretanje agenata redom na zadatku
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Kôd prikazuje kako stvoriti zadatak koji uključuje rad više agenata na analizi podataka. Svaki agent obavlja specifičnu funkciju, a zadatak se izvršava koordinacijom agenata radi postizanja željenog cilja. Kreiranjem agenata s posebnim ulogama možete poboljšati učinkovitost i izvedbu zadatka.

### Učite u stvarnom vremenu

Napredni okviri pružaju mogućnosti za razumijevanje konteksta i prilagodbu u stvarnom vremenu.

**Kako to koriste timovi**: Timovi mogu implementirati povratne petlje u kojima agenti uče iz interakcija i dinamički prilagođavaju svoje ponašanje, što vodi do kontinuiranog poboljšanja i usavršavanja sposobnosti.

**Kako to funkcionira u praksi**: Agent može analizirati korisničke povratne informacije, podatke iz okoline i rezultate zadataka kako bi ažurirao bazu znanja, prilagodio algoritme donošenja odluka i s vremenom poboljšao izvedbu. Ovaj iterativni proces učenja omogućuje agentima da se prilagođavaju promjenjivim uvjetima i preferencijama korisnika, povećavajući ukupnu učinkovitost sustava.

## Koje su razlike između Microsoft Agent Frameworka i Azure AI Agent Servicea?

Postoji mnogo načina za usporedbu ovih pristupa, ali pogledajmo glavne razlike u dizajnu, mogućnostima i ciljnim scenarijima uporabe:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework pruža pojednostavljeni SDK za izgradnju AI agenata koristeći `AzureAIProjectAgentProvider`. Omogućuje developerima kreiranje agenata koji koriste Azure OpenAI modele s ugrađenim pozivima alata, upravljanjem razgovorom i sigurnošću razine poduzeća putem Azure identiteta.

**Scenariji uporabe**: Izgradnja produkcijski spremnih AI agenata s upotrebom alata, višestupanjskim radnim tokovima i scenarijima integracije u poduzeću.

Evo nekoliko važnih osnovnih koncepata Microsoft Agent Frameworka:

- **Agenti**. Agent se kreira putem `AzureAIProjectAgentProvider` i konfigurira s imenom, uputama i alatima. Agent može:
  - **Obraditi korisničke poruke** i generirati odgovore koristeći Azure OpenAI modele.
  - **Automatski pozivati alate** na temelju konteksta razgovora.
  - **Održavati stanje razgovora** kroz više interakcija.

  Evo primjera koda koji prikazuje kako stvoriti agenta:

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

- **Alati**. Okvir podržava definiranje alata kao Python funkcija koje agent može automatski pozivati. Alati se registriraju tijekom kreiranja agenta:

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

- **Integracija Azure identiteta**. Okvir koristi `AzureCliCredential` (ili `DefaultAzureCredential`) za sigurnu autentikaciju bez ključeva, uklanjajući potrebu za upravljanjem API ključevima.

## Azure AI Agent Service

Azure AI Agent Service je noviji dodatak, predstavljen na Microsoft Ignite 2024. Omogućuje razvoj i implementaciju AI agenata s fleksibilnijim modelima, poput izravnog pozivanja open-source LLM-ova poput Llama 3, Mistral i Cohere.

Azure AI Agent Service pruža snažnije mehanizme sigurnosti poduzeća i metode pohrane podataka, čineći ga prikladnim za aplikacije u poduzeću.

Radi odmah s Microsoft Agent Frameworkom za izgradnju i implementaciju agenata.

Ova usluga trenutno je u javnoj preview verziji i podržava Python i C# za izgradnju agenata.

Koristeći Azure AI Agent Service Python SDK možemo kreirati agenta s korisnički definiranim alatom:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Definirajte funkcije alata
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

- **Agent**. Azure AI Agent Service integrira se s Microsoft Foundry platformom. Unutar AI Foundry, AI agent djeluje kao "pametna" mikro usluga koja može odgovarati na pitanja (RAG), izvršavati akcije ili u potpunosti automatizirati radne tokove. To postiže kombiniranjem moći generativnih AI modela s alatima koji mu omogućuju pristup i interakciju s izvorima stvarnih podataka. Evo primjera agenta:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    U ovom primjeru agent je kreiran s modelom `gpt-4o-mini`, imenom `my-agent` i uputama `You are helpful agent`. Agent je opremljen alatima i resursima za zadatke interpretacije koda.

- **Tema i poruke**. Tema je još jedan važan koncept. Predstavlja razgovor ili interakciju između agenta i korisnika. Teme se mogu koristiti za praćenje tijeka razgovora, pohranu kontekstualnih informacija i upravljanje stanjem interakcije. Evo primjera teme:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Ask the agent to perform work on the thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Fetch and log all messages to see the agent's response
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    U prethodnom kodu kreirana je tema. Nakon toga šalje se poruka temi. Pozivom `create_and_process_run`, agentu se traži da izvrši rad u okviru teme. Na kraju se dohvaćaju i bilježe poruke kako bi se vidio odgovor agenta. Poruke ukazuju na tijek razgovora između korisnika i agenta. Važno je razumjeti da poruke mogu biti različitih tipova poput teksta, slike ili datoteke, što znači da je rad agenata rezultirao, na primjer, slikom ili tekstualnim odgovorom. Kao developer taj podatak možete dalje obraditi ili prikazati korisniku.

- **Integracija s Microsoft Agent Frameworkom**. Azure AI Agent Service besprijekorno radi s Microsoft Agent Frameworkom, što znači da možete graditi agente koristeći `AzureAIProjectAgentProvider` i implementirati ih kroz Agent Service za produkcijske scenarije.

**Scenariji uporabe**: Azure AI Agent Service je dizajniran za aplikacije u poduzeću koje zahtijevaju sigurnu, skalabilnu i fleksibilnu implementaciju AI agenata.

## Koja je razlika između ovih pristupa?

Zvuči kao da postoji preklapanje, ali postoje ključne razlike u dizajnu, mogućnostima i ciljnim scenarijima:

- **Microsoft Agent Framework (MAF)**: Produkcijski spreman SDK za gradnju AI agenata. Pruža pojednostavljeni API za kreiranje agenata s pozivima alata, upravljanjem razgovorima i integracijom Azure identiteta.
- **Azure AI Agent Service**: Platforma i servis za implementaciju agenata unutar Azure Foundrya. Nudi ugrađenu povezanost sa servisima poput Azure OpenAI, Azure AI Search, Bing Search i izvršavanjem koda.

Još uvijek niste sigurni što odabrati?

### Scenariji uporabe

Pogledajmo mogu li vam pomoći s nekim uobičajenim scenarijima:

> P: Gradim produkcijske AI agent aplikacije i želim brzo započeti
>

> O: Microsoft Agent Framework je izvrstan izbor. Pruža jednostavan, Pythonov API preko `AzureAIProjectAgentProvider` koji vam omogućuje definiranje agenata s alatima i uputama u samo nekoliko redaka koda.

> P: Trebam implementaciju razine poduzeća s Azure integracijama poput Search i izvršavanja koda
>
> O: Azure AI Agent Service je najbolji izbor. To je platformski servis koji nudi ugrađene sposobnosti za više modela, Azure AI Search, Bing Search i Azure Functions. Omogućuje jednostavno kreiranje agenata u Foundry portalu i implementaciju u velikom opsegu.

> P: Još sam zbunjen, dajte mi samo jednu opciju
>
> O: Počnite s Microsoft Agent Frameworkom za izgradnju agenata, a zatim koristite Azure AI Agent Service kad trebate implementirati i skalirati agente u produkciji. Ovaj pristup omogućava brzu iteraciju logike agenata dok istovremeno imate jasan put do implementacije u poduzeću.

Sažmimo ključne razlike u tablici:

| Okvir | Fokus | Osnovni koncepti | Scenariji uporabe |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Pojednostavljeni SDK za agente s pozivom alata | Agenti, alati, Azure identitet | Izgradnja AI agenata, korištenje alata, višestupanjski radni tokovi |
| Azure AI Agent Service | Fleksibilni modeli, sigurnost za poduzeće, generiranje koda, poziv alata | Modularnost, suradnja, orkestracija procesa | Sigurna, skalabilna i fleksibilna implementacija AI agenata |

## Mogu li integrirati svoje postojeće alate iz Azure ekosustava izravno ili trebam samostalna rješenja?
Odgovor je da, možete integrirati svoje postojeće alate Azure ekosustava izravno s Azure AI Agent Service, posebno jer je izgrađen da besprijekorno surađuje s drugim Azure uslugama. Na primjer, mogli biste integrirati Bing, Azure AI Search i Azure Functions. Postoji i duboka integracija s Microsoft Foundry.

Microsoft Agent Framework također se integrira s Azure uslugama putem `AzureAIProjectAgentProvider` i Azure identiteta, što vam omogućuje da izravno pozivate Azure usluge iz svojih alata za agente.

## Primjeri koda

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Imate li dodatnih pitanja o AI Agent Framework-ima?

Pridružite se [Microsoft Foundry Discordu](https://aka.ms/ai-agents/discord) kako biste se povezali s drugim učenicima, sudjelovali u radnom vremenu i dobili odgovore na svoja pitanja o AI Agentima.

## Reference

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI odgovori</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>

## Prethodna lekcija

[Uvod u AI agente i primjere uporabe agenata](../01-intro-to-ai-agents/README.md)

## Sljedeća lekcija

[Razumijevanje uzoraka dizajna agenata](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge prijevoda [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporučuje se stručni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazume ili pogrešna tumačenja nastala korištenjem ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->