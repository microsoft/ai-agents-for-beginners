[![Istraživanje AI Agent Frameworka](../../../translated_images/hr/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Kliknite na gornju sliku za pregled videa ove lekcije)_

# Istražite AI Agent Frameworke

AI agent frameworki su softverske platforme dizajnirane za pojednostavljivanje stvaranja, implementacije i upravljanja AI agentima. Ovi frameworki pružaju programerima unaprijed izrađene komponente, apstrakcije i alate koji olakšavaju razvoj složenih AI sustava.

Ovi frameworki pomažu programerima da se fokusiraju na jedinstvene aspekte svojih aplikacija pružajući standardizirane pristupe uobičajenim izazovima u razvoju AI agenata. Povećavaju skalabilnost, pristupačnost i učinkovitost u izgradnji AI sustava.

## Uvod

Ova lekcija će obuhvatiti:

- Što su AI Agent Frameworki i što omogućuju programerima postići?
- Kako timovi mogu koristiti te frameworke za brzo prototipiranje, iteraciju i poboljšanje sposobnosti svojih agenata?
- Koje su razlike između frameworka i alata koje je stvorio Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> i <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Mogu li integrirati alate mog postojećeg Azure ekosustava izravno ili trebam samostalna rješenja?
- Što je Microsoft Foundry Agent Service i kako mi pomaže?

## Ciljevi učenja

Ciljevi ove lekcije su vam pomoći razumjeti:

- Ulogu AI Agent Frameworka u razvoju AI-ja.
- Kako iskoristiti AI Agent Frameworke za izgradnju inteligentnih agenata.
- Ključne mogućnosti koje omogućuju AI Agent Frameworki.
- Razlike između Microsoft Agent Frameworka i Microsoft Foundry Agent Servicea.

## Što su AI Agent Frameworki i što omogućuju programerima?

Tradicionalni AI Frameworki vam mogu pomoći integrirati AI u vaše aplikacije i učiniti ih boljima na sljedeće načine:

- **Personalizacija**: AI može analizirati ponašanje i preferencije korisnika kako bi pružio personalizirane preporuke, sadržaj i iskustva.
Primjer: Streaming servisi poput Netflixa koriste AI za predlaganje filmova i emisija temeljenih na povijesti gledanja, povećavajući angažman i zadovoljstvo korisnika.
- **Automatizacija i učinkovitost**: AI može automatizirati ponavljajuće zadatke, pojednostaviti radne tokove i poboljšati operativnu učinkovitost.
Primjer: Aplikacije za korisničku podršku koriste AI chatbotove za rješavanje čestih upita, skraćujući vrijeme odgovora i oslobađajući ljudske agente za složenije probleme.
- **Poboljšano korisničko iskustvo**: AI može unaprijediti ukupno korisničko iskustvo pružajući inteligentne značajke poput prepoznavanja glasa, obrade prirodnog jezika i prediktivnog teksta.
Primjer: Virtualni asistenti poput Siri i Google Assistant koriste AI za razumijevanje i reagiranje na glasovne naredbe, olakšavajući korisnicima interakciju s uređajima.

### Sve to zvuči sjajno, ali zašto nam treba AI Agent Framework?

AI Agent frameworki predstavljaju nešto više od samih AI frameworka. Dizajnirani su za omogućavanje stvaranja inteligentnih agenata koji mogu komunicirati s korisnicima, drugim agentima i okolinom kako bi postigli određene ciljeve. Ti agenti mogu pokazivati autonomno ponašanje, donositi odluke i prilagođavati se promjenama u uvjetima. Pogledajmo neke ključne mogućnosti koje omogućuju AI Agent Frameworki:

- **Suradnja i koordinacija agenata**: Omogućuju stvaranje više AI agenata koji mogu surađivati, komunicirati i koordinirati se za rješavanje složenih zadataka.
- **Automatizacija i upravljanje zadacima**: Pružaju mehanizme za automatizaciju višekorakih radnih tokova, delegaciju zadataka i dinamičko upravljanje zadacima među agentima.
- **Kontekstualno razumijevanje i prilagodba**: Opremaju agente sposobnošću razumijevanja konteksta, prilagodbe promjenjivim okolnostima i donošenja odluka na temelju trenutnih informacija.

Ukratko, agenti vam omogućuju više: podizanje automatizacije na višu razinu i stvaranje inteligentnijih sustava koji se mogu prilagođavati i učiti iz svoje okoline.

## Kako brzo prototipirati, iterirati i poboljšavati sposobnosti agenata?

Ovo je brzo dinamično područje, no postoje neke zajedničke značajke u većini AI Agent Frameworka koje vam mogu pomoći da brzo prototipirate i iterirate, kao što su modularne komponente, suradnički alati i učenje u stvarnom vremenu. Pogledajmo ih detaljnije:

- **Koristite modularne komponente**: AI SDK-ovi nude unaprijed izrađene komponente poput AI i Memory konektora, poziva funkcija pomoću prirodnog jezika ili dodataka koda, predložaka prompta i drugih.
- **Iskoristite suradničke alate**: Dizajnirajte agente s određenim ulogama i zadacima, što im omogućuje testiranje i usavršavanje suradničkih radnih tokova.
- **Učite u stvarnom vremenu**: Implementirajte petlje povratnih informacija gdje agenti uče iz interakcija i dinamički prilagođavaju svoje ponašanje.

### Koristite modularne komponente

SDK-ovi poput Microsoft Agent Frameworka nude unaprijed izrađene komponente poput AI konektora, definicija alata i upravljanja agentima.

**Kako timovi to mogu koristiti**: Timovi mogu brzo sastaviti ove komponente da bi stvorili funkcionalni prototip bez potrebe za početkom od nule, što omogućuje brzo eksperimentiranje i iteraciju.

**Kako to funkcionira u praksi**: Možete koristiti unaprijed izrađeni parser za izdvajanje informacija iz korisničkog unosa, memorijski modul za pohranu i dohvat podataka te generator prompta za interakciju s korisnicima, sve bez potrebe za izgradnjom tih komponenti od nule.

**Primjer koda**. Pogledajmo primjer kako možete koristiti Microsoft Agent Framework s `FoundryChatClient` da model odgovara na korisnički unos pozivanjem alata:

``` python
# Microsoft Agent Framework Python primjer

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Definirajte primjer funkcije alata za rezervaciju putovanja
@tool(approval_mode="never_require")
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # Primjer izlaza: Vaš let za New York 1. siječnja 2025. uspješno je rezerviran. Sigurno putovanje! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Iz ovog primjera vidite kako možete iskoristiti unaprijed izrađeni parser za izdvajanje ključnih informacija iz korisničkog unosa, poput početka, odredišta i datuma zahtjeva za rezervaciju leta. Ovaj modularni pristup omogućuje vam da se fokusirate na logiku na višoj razini.

### Iskoristite suradničke alate

Frameworki poput Microsoft Agent Frameworka olakšavaju stvaranje više agenata koji mogu surađivati.

**Kako timovi to mogu koristiti**: Timovi mogu dizajnirati agente s posebnim ulogama i zadacima, omogućujući im testiranje i usavršavanje suradničkih radnih tokova te povećanje ukupne učinkovitosti sustava.

**Kako to funkcionira u praksi**: Možete stvoriti tim agenata gdje svaki agent ima specijaliziranu funkciju, poput dohvaćanja podataka, analize ili donošenja odluka. Ti agenti mogu komunicirati i dijeliti informacije kako bi postigli zajednički cilj, poput odgovora na korisnički upit ili izvršenja zadatka.

**Primjer koda (Microsoft Agent Framework)**:

```python
# Kreiranje više agenata koji rade zajedno koristeći Microsoft Agent Framework

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Agent za dohvat podataka
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Agent za analizu podataka
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Pokretanje agenata jedan za drugim na zadatku
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

U prethodnom kodu vidite kako stvoriti zadatak koji uključuje više agenata koji surađuju na analizi podataka. Svaki agent obavlja određenu funkciju, a zadatak se izvršava koordiniranjem agenata kako bi se postigao željeni ishod. Stvaranjem posvećenih agenata sa specijaliziranim ulogama možete poboljšati učinkovitost i performanse zadataka.

### Učite u stvarnom vremenu

Napredni frameworki pružaju mogućnosti za razumijevanje konteksta i prilagodbu u stvarnom vremenu.

**Kako timovi to mogu koristiti**: Timovi mogu implementirati petlje povratnih informacija gdje agenti uče iz interakcija i dinamički prilagođavaju svoje ponašanje, što vodi kontinuiranom poboljšanju i usavršavanju sposobnosti.

**Kako to funkcionira u praksi**: Agenti mogu analizirati povratne informacije korisnika, podatke o okolišu i ishode zadataka kako bi ažurirali svoju bazu znanja, prilagodili algoritme donošenja odluka i poboljšali izvedbu tijekom vremena. Ovaj iterativni proces učenja omogućuje agentima da se prilagođavaju promjenjivim uvjetima i preferencijama korisnika, čime se poboljšava ukupna učinkovitost sustava.

## Koje su razlike između Microsoft Agent Frameworka i Microsoft Foundry Agent Servicea?

Postoji mnogo načina za usporedbu ovih pristupa, ali pogledajmo neke ključne razlike u pogledu njihovog dizajna, mogućnosti i ciljnih slučajeva uporabe:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework pruža pojednostavljeni SDK za izgradnju AI agenata koristeći `FoundryChatClient`. Omogućuje programerima stvaranje agenata koji koriste Azure OpenAI modele s ugrađenim pozivanjem alata, upravljanjem razgovorom i sigurnošću na razini poduzeća putem Azure identiteta.

**Slučajevi upotrebe**: Izgradnja AI agenata spremnih za proizvodnju s korištenjem alata, višekoraka radnih tokova i scenarija integracije poduzeća.

Evo nekoliko važnih osnovnih pojmova Microsoft Agent Frameworka:

- **Agenti**. Agent se stvara pomoću `FoundryChatClient` i konfigurira s imenom, uputama i alatima. Agent može:
  - **Obrađivati poruke korisnika** i generirati odgovore koristeći Azure OpenAI modele.
  - **Automatski pozivati alate** na temelju konteksta razgovora.
  - **Održavati stanje razgovora** kroz više interakcija.

  Evo primjera koda koji pokazuje kako stvoriti agenta:

    ```python
    import os
    from agent_framework.foundry import FoundryChatClient
    from azure.identity import AzureCliCredential

    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **Alati**. Framework podržava definiciju alata kao Python funkcija koje agent može automatski pozivati. Alati se registriraju prilikom stvaranja agenta:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = provider.as_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **Koordinacija više agenata**. Možete stvoriti više agenata s različitim specijalizacijama i koordinirati njihov rad:

    ```python
    planner = provider.as_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = provider.as_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Integracija Azure identiteta**. Framework koristi `AzureCliCredential` (ili `DefaultAzureCredential`) za sigurnu autentifikaciju bez ključeva, čime se uklanja potreba za izravnim upravljanjem API ključevima.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service je noviji dodatak, predstavljen na Microsoft Ignite 2024. Omogućuje razvoj i implementaciju AI agenata s fleksibilnijim modelima, kao što je izravno pozivanje open-source LLM-ova poput Llama 3, Mistral i Cohere.

Microsoft Foundry Agent Service pruža snažnije sigurnosne mehanizme za poduzeća i metode pohrane podataka, što ga čini prikladnim za poduzećne aplikacije.

On radi odmah s Microsoft Agent Frameworkom za izgradnju i implementaciju agenata.

Ova usluga je trenutno u javnoj pretpregledu i podržava Python i C# za izgradnju agenata.

Korištenjem Microsoft Foundry Agent Service Python SDK-a možemo stvoriti agenta s korisnički definiranim alatom:

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
        model="gpt-5-mini",
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

### Osnovni pojmovi

Microsoft Foundry Agent Service ima sljedeće osnovne pojmove:

- **Agent**. Microsoft Foundry Agent Service integrira se s Microsoft Foundryjem. Unutar Microsoft Foundryja, AI agent djeluje kao "pametna" mikrousluga koja se može koristiti za odgovaranje na pitanja (RAG), izvršavanje akcija ili potpuno automatiziranje radnih tokova. To postiže kombiniranjem moći generativnih AI modela s alatima koji mu omogućuju pristup i interakciju s stvarnim izvorima podataka. Evo primjera agenta:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    U ovom primjeru agent je stvoren s modelom `gpt-5-mini`, imenom `my-agent` i uputama `You are helpful agent`. Agent je opremljen alatima i resursima za izvršavanje zadataka interpretacije koda.

- **Tema i poruke**. Tema je još jedan važan pojam. Predstavlja razgovor ili interakciju između agenta i korisnika. Temama se može pratiti napredak razgovora, pohranjivati kontekstualne informacije i upravljati stanjem interakcije. Evo primjera teme:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Zamolite agenta da izvrši rad na niti
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Dohvatite i zabilježite sve poruke kako biste vidjeli odgovor agenta
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    U prethodnom kodu tema je stvorena. Zatim se šalje poruka temi. Pozivom `create_and_process_run`, agent se traži da izvedbe rad na temi. Na kraju se poruke dohvaćaju i zapisuju kako bi se vidio odgovor agenta. Poruke pokazuju napredak razgovora između korisnika i agenta. Također je važno razumjeti da poruke mogu biti različitih vrsta, poput teksta, slike ili datoteke, što znači da je rad agenta rezultirao, na primjer, slikom ili tekstualnim odgovorom. Kao programer, možete koristiti te informacije za daljnju obradu odgovora ili njegovo prikazivanje korisniku.

- **Integracija s Microsoft Agent Frameworkom**. Microsoft Foundry Agent Service radi besprijekorno s Microsoft Agent Frameworkom, što znači da možete graditi agente koristeći `FoundryChatClient` i implementirati ih putem Agent Servicea za produkcijske scenarije.

**Slučajevi upotrebe**: Microsoft Foundry Agent Service je dizajniran za poduzećne aplikacije koje zahtijevaju sigurnu, skalabilnu i fleksibilnu implementaciju AI agenata.

## Koja je razlika između ovih pristupa?
 
Zvuči kao da postoji preklapanje, ali postoje neke ključne razlike u pogledu njihovog dizajna, mogućnosti i ciljnih slučajeva uporabe:
 
- **Microsoft Agent Framework (MAF)**: Je SDK spreman za produkciju za izgradnju AI agenata. Pruža pojednostavljeni API za stvaranje agenata s pozivanjem alata, upravljanjem razgovorom i integracijom Azure identiteta.
- **Microsoft Foundry Agent Service**: Je platforma i servis za implementaciju u Microsoft Foundryju za agente. Nudi ugrađenu povezanost s uslugama poput Azure OpenAI, Azure AI Search, Bing Search i izvršavanjem koda.
 
Još niste sigurni koju odabrati?

### Slučajevi upotrebe
 
Pogledajmo možemo li vam pomoći kroz neke uobičajene slučajeve:
 
> P: Gradim produkcijske AI agent aplikacije i želim brzo početi
>

>O: Microsoft Agent Framework je izvrstan izbor. Pruža jednostavan, pythonovski API putem `FoundryChatClient` koji vam omogućuje definiranje agenata s alatima i uputama u samo nekoliko linija koda.

>P: Trebam implementaciju na razini poduzeća s Azure integracijama poput Searcha i izvršavanja koda
>
> O: Microsoft Foundry Agent Service je najbolji izbor. To je platforma koja nudi ugrađene mogućnosti za više modela, Azure AI Search, Bing Search i Azure Functions. Omogućuje jednostavno izgradnju vaših agenata u Foundry portalu i široku implementaciju.
 
> P: Još sam zbunjen, dajte mi samo jednu opciju
>
> O: Započnite s Microsoft Agent Frameworkom za izgradnju svojih agenata, a zatim koristite Microsoft Foundry Agent Service kad ih trebate implementirati i skalirati u produkciji. Ovaj pristup omogućava vam brzu iteraciju logike agenta, a pritom imate jasan put prema implementaciji u poduzeću.
 
Sažmimo ključne razlike u tablici:

| Framework | Fokus | Osnovni pojmovi | Slučajevi upotrebe |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Pojednostavljeni agent SDK s pozivanjem alata | Agenti, Alati, Azure identitet | Izgradnja AI agenata, korištenje alata, višekorak radni tokovi |
| Microsoft Foundry Agent Service | Fleksibilni modeli, sigurnost za poduzeća, generiranje koda, pozivanje alata | Modularnost, Suradnja, Orkestracija procesa | Sigurna, skalabilna i fleksibilna implementacija AI agenata |

## Mogu li integrirati moje postojeće Azure ekosustavne alate izravno ili trebam samostalna rješenja?


Odgovor je da, možete integrirati svoje postojeće alate unutar Azure ekosustava izravno s Microsoft Foundry Agent Servisom posebno, jer je izgrađen za besprijekoran rad s drugim Azure uslugama. Na primjer, mogli biste integrirati Bing, Azure AI Search i Azure Functions. Postoji i duboka integracija s Microsoft Foundry.

Microsoft Agent Framework također se integrira s Azure uslugama putem `FoundryChatClient` i Azure identiteta, omogućujući vam da pozivate Azure usluge izravno iz vaših alata za agente.

## Primjeri Koda

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Imate li Više Pitanja o AI Agent Framework-ovima?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) kako biste se susreli s drugim učenicima, prisustvovali uredskim satima i dobili odgovore na svoja pitanja o AI Agentima.

## Reference

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Odgovori</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Prethodna Lekcija

[Uvod u AI Agente i Upotrebu Agenata](../01-intro-to-ai-agents/README.md)

## Sljedeća Lekcija

[Razumijevanje Agentnih Dizajn Obrasca](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->