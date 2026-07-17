[![Istraživanje AI Agent Okvira](../../../translated_images/hr/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Kliknite na gornju sliku za pregled video lekcije)_

# Istražite AI Agent Okvire

AI agent okviri su softverske platforme dizajnirane za pojednostavljenje stvaranja, implementacije i upravljanja AI agentima. Ti okviri pružaju programerima unaprijed izgrađene komponente, apstrakcije i alate koji ubrzavaju razvoj složenih AI sustava.

Ovi okviri pomažu programerima da se usredotoče na jedinstvene aspekte svojih aplikacija pružajući standardizirane pristupe uobičajenim izazovima u razvoju AI agenata. Povećavaju skalabilnost, pristupačnost i učinkovitost u izgradnji AI sustava.

## Uvod

Ova lekcija će pokriti:

- Što su AI Agent Okviri i što omogućuju programerima?
- Kako timovi mogu koristiti ove okvire za brzo prototipiranje, iteraciju i poboljšavanje sposobnosti agenta?
- Koje su razlike između okvira i alata koje je izradio Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> i <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Mogu li izravno integrirati svoje postojeće alate iz Azure ekosustava ili trebam samostalna rješenja?
- Što je Microsoft Foundry Agent Service i kako mi pomaže?

## Ciljevi učenja

Ciljevi ove lekcije su pomoći vam da razumijete:

- Ulogu AI Agent Okvira u razvoju AI-ja.
- Kako iskoristiti AI Agent Okvire za izgradnju inteligentnih agenata.
- Ključne mogućnosti omogućene AI Agent Okvirima.
- Razlike između Microsoft Agent Frameworka i Microsoft Foundry Agent Servicea.

## Što su AI Agent Okviri i što omogućuju programerima?

Tradicionalni AI okviri mogu vam pomoći integrirati AI u vaše aplikacije i poboljšati ih na sljedeće načine:

- **Personalizacija**: AI može analizirati ponašanje i preferencije korisnika kako bi pružio personalizirane preporuke, sadržaj i iskustva.
Primjer: Streaming servisi kao Netflix koriste AI za predlaganje filmova i emisija na temelju povijesti gledanja, čime povećavaju angažman i zadovoljstvo korisnika.
- **Automatizacija i učinkovitost**: AI može automatizirati repetitivne zadatke, pojednostaviti radne tokove i poboljšati operativnu učinkovitost.
Primjer: Aplikacije za korisničku podršku koriste AI-pokretane chatbote za obradu čestih upita, smanjujući vrijeme odgovora i oslobađajući ljudske agente za složenije probleme.
- **Poboljšano korisničko iskustvo**: AI može unaprijediti ukupno korisničko iskustvo pružajući inteligentne značajke poput prepoznavanja glasa, obrade prirodnog jezika i prediktivnog teksta.
Primjer: Virtualni asistenti poput Siri i Google Assistanta koriste AI za razumijevanje i odgovaranje na glasovne naredbe, čime olakšavaju korisnicima interakciju s uređajima.

### Sve to zvuči sjajno, zar ne? Zašto nam onda treba AI Agent Framework?

AI Agent okviri predstavljaju nešto više od običnih AI okvira. Dizajnirani su za omogućavanje stvaranja inteligentnih agenata koji mogu komunicirati s korisnicima, drugim agentima i okolinom kako bi postigli određene ciljeve. Ti agenti mogu pokazivati autonomno ponašanje, donositi odluke i prilagođavati se promjenjivim uvjetima. Pogledajmo neke ključne mogućnosti omogućene AI Agent Okvirima:

- **Suradnja i koordinacija agenata**: Omogućuju stvaranje više AI agenata koji mogu međusobno surađivati, komunicirati i koordinirati se za rješavanje složenih zadataka.
- **Automatizacija i upravljanje zadacima**: Pružaju mehanizme za automatizaciju višestepenih radnih tokova, delegaciju zadataka i dinamičko upravljanje zadacima među agentima.
- **Kontekstualno razumijevanje i prilagodba**: Opremaju agente sposobnošću razumijevanja konteksta, prilagodbe promjenjivim uvjetima i donošenja odluka na temelju informacija u stvarnom vremenu.

Ukratko, agenti vam omogućuju više - da dignete automatizaciju na višu razinu, da stvorite inteligentnije sustave koji se mogu prilagođavati i učiti iz okoline.

## Kako brzo prototipizirati, iterirati i poboljšavati sposobnosti agenta?

Ovo je brzo mijenjajuće područje, ali postoje neke zajedničke značajke kod većine AI Agent Okvira koje vam mogu pomoći brzo prototipizirati i iterirati, poput modularnih komponenti, alata za suradnju i učenja u stvarnom vremenu. Pogledajmo ih:

- **Koristite modularne komponente**: AI SDK-ovi nude unaprijed izgrađene komponente poput AI i memorijskih konektora, pozivanja funkcija pomoću prirodnog jezika ili dodataka za kod, predložaka za upute i više.
- **Iskoristite alate za suradnju**: Dizajnirajte agente sa specifičnim ulogama i zadacima, omogućujući im testiranje i usavršavanje suradničkih radnih tokova.
- **Učite u stvarnom vremenu**: Implementirajte povratne petlje u kojima agenti uče iz interakcija i dinamički prilagođavaju svoje ponašanje.

### Koristite modularne komponente

SDK-ovi poput Microsoft Agent Frameworka nude unaprijed izrađene komponente poput AI konektora, definicija alata i upravljanja agentima.

**Kako timovi mogu koristiti ove**: Timovi mogu brzo sastaviti ove komponente za stvaranje funkcionalnog prototipa bez početka od nule, što omogućuje brzo eksperimentiranje i iteraciju.

**Kako to funkcionira u praksi**: Možete koristiti unaprijed izrađeni parser za izdvajanje informacija iz korisničkog unosa, memorijski modul za spremanje i dohvat podataka te generator uputa za interakciju s korisnicima, sve bez izgradnje ovih komponenti od nule.

**Primjer koda**. Pogledajmo primjer kako koristiti Microsoft Agent Framework s `FoundryChatClient` da model odgovara na korisnički unos pozivanjem alata:

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
    # Primjer izlaza: Vaš let za New York 1. siječnja 2025. je uspješno rezerviran. Sretan put! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Ono što možete vidjeti u ovom primjeru jest kako iskoristiti unaprijed izrađeni parser za izdvajanje ključnih informacija iz korisničkog unosa, poput podrijetla, odredišta i datuma zahtjeva za rezervaciju leta. Ovaj modularni pristup vam omogućuje da se usredotočite na visokorazinsku logiku.

### Iskoristite alate za suradnju

Okviri poput Microsoft Agent Frameworka olakšavaju stvaranje više agenata koji mogu međusobno surađivati.

**Kako timovi mogu koristiti ove**: Timovi mogu dizajnirati agente s posebnim ulogama i zadacima, omogućujući im testirati i usavršavati suradničke radne tokove te poboljšati ukupnu učinkovitost sustava.

**Kako to funkcionira u praksi**: Možete stvoriti tim agenata gdje svaki agent ima specijaliziranu funkciju, poput dohvaćanja podataka, analize ili donošenja odluka. Ti agenti mogu međusobno komunicirati i dijeliti informacije kako bi postigli zajednički cilj, poput odgovora na korisnički upit ili dovršetka zadatka.

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

# Agent za dohvaćanje podataka
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

# Pokreni agente redom na zadatku
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Ono što vidite u prethodnom kodu jest kako se može stvoriti zadatak koji uključuje rad više agenata na analizi podataka. Svaki agent izvodi određenu funkciju, a zadatak se izvršava koordinacijom agenata radi postizanja željenog ishoda. Stvaranjem posvećenih agenata sa specijaliziranim ulogama možete poboljšati učinkovitost i performanse zadatka.

### Učite u stvarnom vremenu

Napredni okviri pružaju mogućnosti za razumijevanje i prilagodbu konteksta u stvarnom vremenu.

**Kako timovi mogu koristiti ove**: Timovi mogu implementirati povratne petlje u kojima agenti uče iz interakcija i dinamički prilagođavaju svoje ponašanje, što vodi do kontinuiranog poboljšanja i usavršavanja sposobnosti.

**Kako to funkcionira u praksi**: Agenti mogu analizirati korisničku povratnu informaciju, podatke o okolišu i rezultate zadataka kako bi ažurirali svoju bazu znanja, prilagodili algoritme donošenja odluka i s vremenom poboljšali performanse. Ovaj iterativni proces učenja omogućuje agentima da se prilagođavaju promjenjivim uvjetima i korisničkim preferencijama, povećavajući ukupnu učinkovitost sustava.

## Koje su razlike između Microsoft Agent Frameworka i Microsoft Foundry Agent Servicea?

Postoji mnogo načina za usporedbu ovih pristupa, ali pogledajmo neke ključne razlike u pogledu dizajna, mogućnosti i ciljane primjene:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework pruža pojednostavljeni SDK za izgradnju AI agenata pomoću `FoundryChatClient`. Omogućuje programerima stvaranje agenata koji koriste Azure OpenAI modele s ugrađenim pozivanjem alata, upravljanjem razgovorima i sigurnošću na razini poduzeća putem Azure identiteta.

**Primjene**: Izgradnja proizvodno spremnih AI agenata s korištenjem alata, višestepenih radnih tokova i scenarija integracije s poduzećem.

Evo nekoliko važnih osnovnih pojmova Microsoft Agent Frameworka:

- **Agenti**. Agent se stvara putem `FoundryChatClient` i konfigurira s imenom, uputama i alatima. Agent može:
  - **Obrađivati korisničke poruke** i generirati odgovore koristeći Azure OpenAI modele.
  - **Automatski pozivati alate** na temelju konteksta razgovora.
  - **Održavati stanje razgovora** kroz više interakcija.

  Evo isječka koda koji prikazuje kako stvoriti agenta:

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

- **Alati**. Okvir podržava definiranje alata kao Python funkcija koje agent može automatski pozivati. Alati se registriraju prilikom stvaranja agenta:

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

- **Koordinacija višestrukih agenata**. Možete stvoriti više agenata sa različitim specijalizacijama i koordinirati njihov rad:

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

- **Integracija Azure identiteta**. Okvir koristi `AzureCliCredential` (ili `DefaultAzureCredential`) za sigurnu autentifikaciju bez ključeva, eliminirajući potrebu za upravljanjem API ključevima izravno.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service je noviji dodatak, predstavljen na Microsoft Ignite 2024. Omogućuje razvoj i implementaciju AI agenata s fleksibilnijim modelima, kao što je izravno pozivanje open-source LLM-ova poput Llama 3, Mistral i Cohere.

Microsoft Foundry Agent Service pruža snažnije mehanizme sigurnosti poduzeća i metode pohrane podataka, što ga čini pogodnim za poduzetničke aplikacije.

Radi odmah s Microsoft Agent Frameworkom za izgradnju i implementaciju agenata.

Ova usluga je trenutno u javnoj verziji (Public Preview) i podržava Python i C# za izgradnju agenata.

Koristeći Microsoft Foundry Agent Service Python SDK, možemo stvoriti agenta s korisnički definiranim alatom:

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
        model="gpt-4.1-mini",
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

- **Agent**. Microsoft Foundry Agent Service integrira se s Microsoft Foundryjem. Unutar Microsoft Foundry, AI Agent djeluje kao "pametan" mikroservis koji može odgovarati na pitanja (RAG), obavljati radnje ili potpuno automatizirati radne tokove. To postiže kombiniranjem snage generativnih AI modela s alatima koji mu omogućuju pristup i interakciju s izvornim podacima iz stvarnog svijeta. Evo primjera agenta:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4.1-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    U ovom primjeru, agent je kreiran s modelom `gpt-4.1-mini`, imenom `my-agent` i uputama `You are helpful agent`. Agent je opremljen alatima i resursima za obavljanje zadataka tumačenja koda.

- **Thread i poruke**. Thread je još jedan važan pojam. Predstavlja razgovor ili interakciju između agenta i korisnika. Threadovi se mogu koristiti za praćenje napretka razgovora, pohranu kontekstualnih informacija i upravljanje stanjem interakcije. Evo primjera thread-a:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Zamolite agenta da izvrši rad na temi
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Dohvatite i zabilježite sve poruke kako biste vidjeli odgovor agenta
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    U prethodnom kodu je kreiran thread. Nakon toga, šalje se poruka u thread. Pozivanjem `create_and_process_run`, agent se traži da izvrši rad na threadu. Na kraju se poruke dohvaćaju i bilježe kako bi se vidio odgovor agenta. Poruke pokazuju napredak razgovora između korisnika i agenta. Također je važno razumjeti da poruke mogu biti različitih tipova, poput teksta, slike ili datoteke, što znači da je rad agenta rezultirao, na primjer, slikom ili tekstualnim odgovorom. Kao programer, tada možete koristiti ove informacije za daljnju obradu odgovora ili njegovo prikazivanje korisniku.

- **Integrira se s Microsoft Agent Frameworkom**. Microsoft Foundry Agent Service besprijekorno surađuje s Microsoft Agent Frameworkom, što znači da možete graditi agente pomoću `FoundryChatClient` i implementirati ih kroz Agent Service za produkcijske scenarije.

**Primjene**: Microsoft Foundry Agent Service je dizajniran za poduzetničke aplikacije koje zahtijevaju sigurnu, skalabilnu i fleksibilnu implementaciju AI agenata.

## Koja je razlika između ovih pristupa?
 
Zvuči kao da postoji preklapanje, ali postoje neke ključne razlike u pogledu dizajna, mogućnosti i ciljane uporabe:
 
- **Microsoft Agent Framework (MAF)**: Je proizvodno spreman SDK za izgradnju AI agenata. Pruža pojednostavljeni API za stvaranje agenata s pozivanjem alata, upravljanjem razgovorima i integracijom Azure identiteta.
- **Microsoft Foundry Agent Service**: Je platforma i usluga implementacije u Microsoft Foundryju za agente. Nudi ugrađenu konektivnost s uslugama kao što su Azure OpenAI, Azure AI Search, Bing Search i izvršavanje koda.
 
Još uvijek niste sigurni koji odabrati?

### Primjene
 
Pogledajmo može li vam pomoći pregled nekih uobičajenih slučajeva korištenja:
 
> P: Izrađujem proizvodne AI aplikacije agenata i želim brzo započeti
>

>O: Microsoft Agent Framework je izvrstan izbor. Pruža jednostavan, Pythonovski API preko `FoundryChatClient` koji vam dopušta definiranje agenata s alatima i uputama u samo nekoliko redaka koda.

>P: Trebam implementaciju razine poduzeća s Azure integracijama poput Search i izvršavanja koda
>
> O: Microsoft Foundry Agent Service je najbolji izbor. To je platforma koja pruža ugrađene mogućnosti za višestruke modele, Azure AI Search, Bing Search i Azure Functions. Omogućuje vam da lako gradite agente u Foundry portalu i implementirate ih na velikoj skali.
 
> P: Još sam zbunjen, samo mi dajte jednu opciju
>
> O: Počnite s Microsoft Agent Frameworkom za izgradnju agenata, a zatim koristite Microsoft Foundry Agent Service kad trebate implementirati i skalirati u produkciji. Ovaj pristup omogućuje vam brzo iteriranje na logici agenta uz jasan put do implementacije na razini poduzeća.
 
Sažmimo ključne razlike u tablici:

| Okvir | Fokus | Osnovni Pojmovi | Primjene |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Pojednostavljeni SDK za agente s pozivanjem alata | Agenti, Alati, Azure Identitet | Izgradnja AI agenata, korištenje alata, višestepeni radni tokovi |
| Microsoft Foundry Agent Service | Fleksibilni modeli, sigurnost poduzeća, generiranje koda, pozivanje alata | Modularnost, Suradnja, Orkestracija procesa | Sigurna, skalabilna i fleksibilna implementacija AI agenata |

## Mogu li izravno integrirati svoje postojeće alate iz Azure ekosustava ili trebam samostalna rješenja?


Odgovor je da, možete izravno integrirati svoje postojeće alate iz Azure ekosustava s Microsoft Foundry Agent Service, posebno jer je izgrađen da besprijekorno radi s drugim Azure uslugama. Na primjer, možete integrirati Bing, Azure AI Search i Azure Functions. Također postoji duboka integracija s Microsoft Foundry.

Microsoft Agent Framework također se integrira s Azure uslugama putem `FoundryChatClient` i Azure identiteta, što vam omogućuje izravno pozivanje Azure usluga iz vaših agent alata.

## Primjeri koda

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Imate li još pitanja o AI Agent Frameworkovima?

Pridružite se [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) da se susretnete s drugim učenicima, sudjelujete na uredskim satima i dobijete odgovore na svoja pitanja o AI Agentima.

## Reference

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Prethodna lekcija

[Uvod u AI agente i primjenu agenata](../01-intro-to-ai-agents/README.md)

## Sljedeća lekcija

[Razumijevanje agentnih dizajnerskih obrazaca](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->