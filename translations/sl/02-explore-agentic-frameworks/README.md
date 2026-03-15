[![Raziskovanje ogrodij AI agentov](../../../translated_images/sl/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Kliknite zgornjo sliko, da si ogledate video te lekcije)_

# Raziščite ogrodja AI agentov

Ogrodja za AI agente so programske platforme, zasnovane za poenostavitev ustvarjanja, uvajanja in upravljanja AI agentov. Ta ogrodja razvijalcem nudijo vnaprej pripravljene komponente, abstrakcije in orodja, ki poenostavijo razvoj kompleksnih AI sistemov.

Ta ogrodja razvijalcem omogočajo, da se osredotočijo na edinstvene vidike svojih aplikacij z zagotavljanjem standardiziranih pristopov k pogostim izzivom pri razvoju AI agentov. Izboljšujejo skalabilnost, dostopnost in učinkovitost pri gradnji AI sistemov.

## Uvod 

V tej lekciji bomo obravnavali:

- Kaj so ogrodja za AI agente in kaj razvijalcem omogočajo doseči?
- Kako lahko ekipe z njimi hitro prototipirajo, iterirajo in izboljšajo zmožnosti svojih agentov?
- Kakšne so razlike med ogrodji in orodji, ki jih je ustvaril Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> in <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Ali lahko neposredno integriram obstočna orodja iz Azure ekosistema ali potrebujem samostojne rešitve?
- Kaj je Azure AI Agent Service in kako mi to pomaga?

## Cilji učenja

Cilji te lekcije so, da vam pomagajo razumeti:

- Vlogo ogrodij za AI agente pri razvoju AI.
- Kako izkoristiti ogrodja za AI agente za gradnjo inteligentnih agentov.
- Ključne zmožnosti, ki jih omogočajo ogrodja za AI agente.
- Razlike med Microsoft Agent Framework in Azure AI Agent Service.

## Kaj so ogrodja za AI agente in kaj razvijalcem omogočajo?

Tradicionalna AI ogrodja vam lahko pomagajo integrirati AI v vaše aplikacije in jih izboljšati na naslednje načine:

- **Personalizacija**: AI lahko analizira vedenje in preference uporabnikov ter zagotovi personalizirana priporočila, vsebino in izkušnje.
Primer: Vsebine za pretakanje, kot je Netflix, uporabljajo AI za predlaganje filmov in oddaj glede na zgodovino gledanja, s čimer povečajo vključenost in zadovoljstvo uporabnikov.
- **Avtomatizacija in učinkovitost**: AI lahko avtomatizira ponavljajoča se opravila, poenostavi delovne tokove in izboljša operativno učinkovitost.
Primer: Aplikacije za podporo strankam uporabljajo AI-poganjane klepetalnike za obravnavo pogostih poizvedb, s čimer zmanjšajo čase odziva in sprostijo človeške agente za bolj zapletene zadeve.
- **Izboljšana uporabniška izkušnja**: AI lahko izboljša splošno uporabniško izkušnjo z inteligentnimi funkcijami, kot so prepoznavanje glasu, obdelava naravnega jezika in prediktivno besedilo.
Primer: Virtualni asistenti, kot sta Siri in Google Assistant, uporabljajo AI za razumevanje in odzivanje na glasovne ukaze, kar uporabnikom olajša interakcijo z napravami.

### Vse to se sliši odlično, zakaj torej potrebujemo ogrodje AI agentov?

Ogrodja za AI agente predstavljajo nekaj več kot le AI ogrodja. Namenjena so omogočanju ustvarjanja inteligentnih agentov, ki lahko komunicirajo z uporabniki, drugimi agenti in okoljem, da dosežejo določene cilje. Ti agenti lahko kažejo avtonomno vedenje, sprejemajo odločitve in se prilagajajo spreminjajočim se razmeram. Oglejmo si nekaj ključnih zmožnosti, ki jih omogočajo ogrodja za AI agente:

- **Sodelovanje in koordinacija agentov**: Omogočajo ustvarjanje več AI agentov, ki lahko sodelujejo, komunicirajo in se usklajujejo pri reševanju kompleksnih nalog.
- **Avtomatizacija opravil in upravljanje**: Zagotavljajo mehanizme za avtomatizacijo večstopenjskih delovnih tokov, dodeljevanje opravil in dinamično upravljanje opravil med agenti.
- **Kontekstualno razumevanje in prilagajanje**: Opremljajo agente z zmožnostjo razumevanja konteksta, prilagajanja spreminjajočim se okoljem in sprejemanja odločitev na podlagi informacij v realnem času.

Torej povzetek: agenti vam omogočajo več — pripeljejo avtomatizacijo na višjo raven in ustvarijo bolj inteligentne sisteme, ki se lahko prilagajajo in učijo iz svojega okolja.

## Kako hitro prototipirati, iterirati in izboljšati sposobnosti agenta?

To je hitro spreminjajoče se področje, vendar obstajajo nekateri elementi, skupni večini ogrodij za AI agente, ki vam lahko pomagajo hitro prototipirati in iterirati, predvsem modularne komponente, orodja za sodelovanje in učenje v realnem času. Poglobimo se v to:

- **Uporabite modularne komponente**: AI SDK-ji ponujajo vnaprej pripravljene komponente, kot so AI in memorijski konektorji, klicanje funkcij z uporabo naravnega jezika ali vtičniki kode, predloge pozivov in več.
- **Izkoristite orodja za sodelovanje**: Oblikujte agente z določenimi vlogami in nalogami, kar jim omogoča testiranje in izboljševanje sodelovalnih delovnih tokov.
- **Učenje v realnem času**: Implementirajte povratne zanke, kjer se agenti učijo iz interakcij in dinamično prilagajajo svoje vedenje.

### Uporabite modularne komponente

SDK-ji, kot je Microsoft Agent Framework, ponujajo vnaprej pripravljene komponente, kot so AI konektorji, definicije orodij in upravljanje agentov.

**Kako lahko ekipe to uporabijo**: Ekipe lahko hitro sestavijo te komponente za ustvarjanje funkcionalnega prototipa brez začetka iz nič, kar omogoča hitro eksperimentiranje in iteracijo.

**Kako to deluje v praksi**: Uporabite lahko vnaprej pripravljen parser za izvleček informacij iz uporabnikovega vnosa, modul za pomnjenje za shranjevanje in pridobivanje podatkov ter generator pozivov za interakcijo z uporabniki, vse brez gradnje teh komponent iz nič.

**Primer kode**. Poglejmo primer, kako lahko uporabite Microsoft Agent Framework z `AzureAIProjectAgentProvider`, da model odgovori na uporabnikov vnos s klicanjem orodij:

``` python
# Microsoft Agent Framework Python Primer

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# Določi funkcijo orodja za rezervacijo potovanja
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
    # Primer izpisa: Vaš let v New York 1. januarja 2025 je bil uspešno rezerviran. Varno pot! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Kar lahko vidite iz tega primera, je, kako lahko izkoristite vnaprej pripravljen parser za izvleček ključnih informacij iz uporabnikovega vnosa, kot so izhodišče, cilj in datum zahteve za rezervacijo leta. Ta modularni pristop vam omogoča, da se osredotočite na logiko na višji ravni.

### Izkoristite orodja za sodelovanje

Ogrodja, kot je Microsoft Agent Framework, olajšajo ustvarjanje več agentov, ki lahko sodelujejo.

**Kako lahko ekipe to uporabijo**: Ekipe lahko oblikujejo agente z določenimi vlogami in nalogami, kar jim omogoča testiranje in izboljševanje sodelovalnih delovnih tokov ter izboljšanje splošne učinkovitosti sistema.

**Kako to deluje v praksi**: Ustvarite lahko ekipo agentov, kjer ima vsak agent specializirano funkcijo, kot so pridobivanje podatkov, analiza ali sprejemanje odločitev. Ti agenti lahko medsebojno komunicirajo in si delijo informacije, da dosežejo skupni cilj, kot je odgovor na uporabnikovo vprašanje ali dokončanje naloge.

**Primer kode (Microsoft Agent Framework)**:

```python
# Ustvarjanje več agentov, ki sodelujejo z uporabo Microsoft Agent Framework

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Agent za pridobivanje podatkov
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Agent za analizo podatkov
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Zaženi agente zaporedno za nalogo
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

V prejšnji kodi lahko vidite, kako ustvarite nalogo, ki vključuje več agentov, ki sodelujejo pri analizi podatkov. Vsak agent opravlja določeno funkcijo, naloga pa se izvaja z usklajevanjem agentov za dosego želenega rezultata. Z ustvarjanjem namenskih agentov s specializiranimi vlogami lahko izboljšate učinkovitost in zmogljivost nalog.

### Učenje v realnem času

Napredna ogrodja nudijo zmožnosti za razumevanje konteksta v realnem času in prilagajanje.

**Kako lahko ekipe to uporabijo**: Ekipe lahko implementirajo povratne zanke, kjer se agenti učijo iz interakcij in dinamično prilagajajo svoje vedenje, kar vodi v neprekinjeno izboljševanje in izpopolnjevanje zmožnosti.

**Kako to deluje v praksi**: Agenti lahko analizirajo povratne informacije uporabnikov, podatke iz okolja in rezultate opravil, da posodobijo svojo bazo znanja, prilagodijo algoritme za sprejemanje odločitev in sčasoma izboljšajo zmogljivost. Ta iterativni proces učenja omogoča agentom prilagajanje spreminjajočim se pogojem in preferencam uporabnikov ter izboljšanje splošne učinkovitosti sistema.

## Kakšne so razlike med Microsoft Agent Framework in Azure AI Agent Service?

Obstaja več načinov za primerjavo teh pristopov, poglejmo pa nekaj ključnih razlik glede na njihovo zasnovo, zmožnosti in ciljne primere uporabe:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework ponuja poenostavljen SDK za gradnjo AI agentov z uporabo `AzureAIProjectAgentProvider`. Omogoča razvijalcem ustvarjanje agentov, ki izkoriščajo modele Azure OpenAI z vgrajenim klicanjem orodij, upravljanjem pogovorov in varnostjo na ravni podjetja prek Azure identitete.

**Primeri uporabe**: Gradnja produkcijsko pripravljenih AI agentov z uporabo orodij, večstopenjskimi delovnimi toku in scenariji integracije v podjetju.

Tu so nekateri pomembni osnovni koncepti Microsoft Agent Framework:

- **Agents**. Agent je ustvarjen preko `AzureAIProjectAgentProvider` in konfiguriran z imenom, navodili in orodji. Agent lahko:
  - **Obdeluje uporabnikova sporočila** in generira odgovore z uporabo modelov Azure OpenAI.
  - **Samodejno kliče orodja** glede na kontekst pogovora.
  - **Vzdržuje stanje pogovora** čez več interakcij.

  Tukaj je odlomek kode, ki prikazuje, kako ustvariti agenta:

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

- **Tools**. Ogrodje podpira definiranje orodij kot Python funkcij, ki jih agent lahko samodejno kliče. Orodja se registrirajo ob ustvarjanju agenta:

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

- **Koordinacija več agentov**. Ustvarite lahko več agentov z različnimi specializacijami in koordinirate njihovo delo:

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

- **Integracija Azure Identity**. Ogrodje uporablja `AzureCliCredential` (ali `DefaultAzureCredential`) za varno, brezključavarsko avtentikacijo, s čimer odpravlja potrebo po neposrednem upravljanju API ključev.

## Azure AI Agent Service

Azure AI Agent Service je novejša pridobitev, predstavljena na Microsoft Ignite 2024. Omogoča razvoj in uvajanje AI agentov z bolj prilagodljivimi modeli, kot so neposredno klicanje odprtokodnih LLM-jev, kot so Llama 3, Mistral in Cohere.

Azure AI Agent Service zagotavlja močnejše mehanizme varnosti za podjetja in metode shranjevanja podatkov, zaradi česar je primeren za podjetniške aplikacije.

Deluje iz škatle skupaj z Microsoft Agent Framework za gradnjo in uvajanje agentov.

Storitev je trenutno v javnem pregledu (Public Preview) in podpira Python ter C# za gradnjo agentov.

Z uporabo Python SDK-ja Azure AI Agent Service lahko ustvarimo agenta z orodjem, ki ga definira uporabnik:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Določi funkcije orodja
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

Azure AI Agent Service ima naslednje osnovne koncepte:

- **Agent**. Azure AI Agent Service se integrira z Microsoft Foundry. Znotraj AI Foundry deluje AI Agent kot "pametna" mikro storitev, ki jo je mogoče uporabiti za odgovarjanje na vprašanja (RAG), izvajanje dejanj ali popolno avtomatizacijo delovnih tokov. To doseže z združitvijo moči generativnih AI modelov z orodji, ki mu omogočajo dostop do virov podatkov iz resničnega sveta in interakcijo z njimi. Tukaj je primer agenta:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    V tem primeru je agent ustvarjen z modelom `gpt-4o-mini`, imenom `my-agent` in navodili `You are helpful agent`. Agent je opremljen z orodji in viri za izvajanje nalog interpretacije kode.

- **Thread and messages**. Thread (nit) je še en pomemben koncept. Predstavlja pogovor ali interakcijo med agentom in uporabnikom. Nit lahko uporabite za sledenje napredku pogovora, shranjevanje kontekstnih informacij in upravljanje stanja interakcije. Tukaj je primer niti:

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

    V prejšnji kodi je bila ustvarjena nit. Nato je bilo poslano sporočilo v nit. Z klicem `create_and_process_run` je agentu naloženo, da izvede delo na niti. Na koncu so sporočila pridobljena in zabeležena, da se vidi agentov odgovor. Sporočila kažejo potek pogovora med uporabnikom in agentom. Pomembno je tudi razumeti, da so sporočila lahko različnih vrst, kot so besedilo, slika ali datoteka — na primer agentovo delo je lahko rezultiralo v sliki ali besedilnem odgovoru. Kot razvijalec lahko te informacije uporabite za nadaljnjo obdelavo odgovora ali njegovo prikazovanje uporabniku.

- **Integracija z Microsoft Agent Framework**. Azure AI Agent Service deluje brezhibno z Microsoft Agent Framework, kar pomeni, da lahko agente gradite z `AzureAIProjectAgentProvider` in jih uvajate prek Agent Service za produkcijske scenarije.

**Primeri uporabe**: Azure AI Agent Service je zasnovana za podjetniške aplikacije, ki zahtevajo varno, skalabilno in prilagodljivo uvajanje AI agentov.

## Kakšna je razlika med tema pristopoma?
 
Zdi se, da obstaja prekrivanje, vendar so ključne razlike glede na zasnovo, zmožnosti in ciljne primere uporabe:
 
- **Microsoft Agent Framework (MAF)**: Je produkcijsko pripravljen SDK za gradnjo AI agentov. Nudi poenostavljen API za ustvarjanje agentov s klicanjem orodij, upravljanjem pogovorov in integracijo Azure identitete.
- **Azure AI Agent Service**: Je platforma in storitev za uvajanje v Azure Foundry za agente. Ponuja vgrajeno povezljivost do storitev, kot so Azure OpenAI, Azure AI Search, Bing Search in izvajanje kode.
 
Še vedno niste prepričani, katerega izbrati?

### Primeri uporabe
 
> Q: I'm building production AI agent applications and want to get started quickly
>
> 
>A: The Microsoft Agent Framework is a great choice. It provides a simple, Pythonic API via `AzureAIProjectAgentProvider` that lets you define agents with tools and instructions in just a few lines of code.
>
>Q: I need enterprise-grade deployment with Azure integrations like Search and code execution
>
> A: Azure AI Agent Service is the best fit. It's a platform service that provides built-in capabilities for multiple models, Azure AI Search, Bing Search and Azure Functions. It makes it easy to build your agents in the Foundry Portal and deploy them at scale.
> 
> Q: I'm still confused, just give me one option
>
> A: Start with the Microsoft Agent Framework to build your agents, and then use Azure AI Agent Service when you need to deploy and scale them in production. This approach lets you iterate quickly on your agent logic while having a clear path to enterprise deployment.
 
Povzamimo ključne razlike v tabeli:

| Framework | Focus | Core Concepts | Use Cases |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Poenostavljen SDK za agente s klicanjem orodij | Agents, Tools, Azure Identity | Gradnja AI agentov, uporaba orodij, večstopenjski delovni tokovi |
| Azure AI Agent Service | Prilagodljivi modeli, varnost za podjetja, generiranje kode, klicanje orodij | Modularnost, sodelovanje, orkestracija procesov | Varno, skalabilno in prilagodljivo uvajanje AI agentov |

## Ali lahko neposredno integriram obstočna orodja iz Azure ekosistema ali potrebujem samostojne rešitve?
Odgovor je da — lahko neposredno integrirate obstoječa orodja iz svojega Azure ekosistema z Azure AI Agent Service, saj je ta zasnovana za nemoteno delovanje z drugimi Azure storitvami. Na primer, lahko integrirate Bing, Azure AI Search in Azure Functions. Prav tako obstaja globoka integracija z Microsoft Foundry.

Microsoft Agent Framework se prav tako integrira z Azure storitvami preko `AzureAIProjectAgentProvider` in Azure identitete, kar vam omogoča klicanje Azure storitev neposredno iz orodij vašega agenta.

## Vzorčne kode

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Imate več vprašanj o okvirih AI agentov?

Pridružite se [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), da se srečate z drugimi učenci, udeležite uradnih ur in dobite odgovore na vprašanja o AI agentih.

## Viri

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Storitev Azure Agent</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Odgovori</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Storitev Azure AI Agent</a>

## Prejšnja lekcija

[Uvod v AI agente in primere uporabe agentov](../01-intro-to-ai-agents/README.md)

## Naslednja lekcija

[Razumevanje agentnih oblikovnih vzorcev](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Izjava o omejitvi odgovornosti:
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco Co-op Translator (https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, upoštevajte, da avtomatizirani prevodi morda vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Nismo odgovorni za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->