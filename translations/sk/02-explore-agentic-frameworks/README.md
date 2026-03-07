[![Preskúmanie rámcov pre AI agentov](../../../translated_images/sk/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Kliknite na obrázok vyššie pre zobrazenie videa tejto lekcie)_

# Preskúmajte rámce pre AI agentov

Rámce pre AI agentov sú softvérové platformy navrhnuté na zjednodušenie vytvárania, nasadzovania a správy AI agentov. Tieto rámce poskytujú vývojárom predpripravené komponenty, abstrakcie a nástroje, ktoré zefektívňujú vývoj zložitých AI systémov.

Tieto rámce pomáhajú vývojárom zamerať sa na jedinečné aspekty ich aplikácií tým, že poskytujú štandardizované prístupy k bežným výzvam vo vývoji AI agentov. Zvyšujú škálovateľnosť, prístupnosť a efektivitu pri budovaní AI systémov.

## Introduction 

Táto lekcia pokryje:

- Čo sú rámce pre AI agentov a čo umožňujú vývojárom dosiahnuť?
- Ako môžu tímy použiť tieto rámce na rýchle prototypovanie, iterovanie a zlepšovanie schopností svojho agenta?
- Aké sú rozdiely medzi rámcami a nástrojmi vytvorenými spoločnosťou Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> a <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Môžem integrovať svoje existujúce nástroje v rámci Azure ekosystému priamo, alebo potrebujem samostatné riešenia?
- Čo je Azure AI Agents service a ako mi to pomáha?

## Learning goals

Ciele tejto lekcie sú pomôcť vám pochopiť:

- Úlohu rámcov pre AI agentov vo vývoji AI.
- Ako využiť rámce pre AI agentov na vytváranie inteligentných agentov.
- Kľúčové schopnosti, ktoré rámce pre AI agentov umožňujú.
- Rozdiely medzi Microsoft Agent Framework a Azure AI Agent Service.

## What are AI Agent Frameworks and what do they enable developers to do?

Tradičné AI rámce vám môžu pomôcť integrovať AI do vašich aplikácií a zlepšiť tieto aplikácie nasledujúcimi spôsobmi:

- **Personalizácia**: AI dokáže analyzovať správanie používateľov a ich preferencie, aby poskytla personalizované odporúčania, obsah a zážitky.
Príklad: Streamovacie služby ako Netflix používajú AI na navrhovanie filmov a relácií na základe histórie sledovania, čím zvyšujú angažovanosť a spokojnosť používateľov.
- **Automatizácia a efektivita**: AI môže automatizovať opakujúce sa úlohy, zefektívniť pracovné toky a zlepšiť prevádzkovú efektivitu.
Príklad: Aplikácie zákazníckej podpory používajú chatboty poháňané AI na riešenie bežných otázok, čím skráťia doby odpovedí a uvoľnia ľudských agentov na riešenie zložitejších problémov.
- **Vylepšený používateľský zážitok**: AI môže zlepšiť celkový používateľský zážitok poskytovaním inteligentných funkcií, ako je rozpoznávanie hlasu, spracovanie prirodzeného jazyka a prediktívny text.
Príklad: Virtuálni asistenti ako Siri a Google Assistant používajú AI na porozumenie a reagovanie na hlasové príkazy, čo uľahčuje používateľom interakciu s ich zariadeniami.

### That all sounds great right, so why do we need the AI Agent Framework?

Rámce pre AI agentov predstavujú niečo viac než len AI rámce. Sú navrhnuté tak, aby umožnili tvorbu inteligentných agentov, ktorí môžu komunikovať s používateľmi, inými agentmi a prostredím s cieľom dosiahnuť konkrétne ciele. Títo agenti môžu vykazovať autonómne správanie, prijímať rozhodnutia a prispôsobovať sa meniacim sa podmienkam. Pozrime sa na niektoré kľúčové schopnosti, ktoré rámce pre AI agentov umožňujú:

- **Spolupráca a koordinácia agentov**: Umožňujú vytváranie viacerých AI agentov, ktorí môžu spolupracovať, komunikovať a koordinovať sa pri riešení zložitých úloh.
- **Automatizácia a riadenie úloh**: Poskytujú mechanizmy na automatizáciu viacstupňových pracovných tokov, delegovanie úloh a dynamické riadenie úloh medzi agentmi.
- **Kontextuálne porozumenie a adaptácia**: Vybavujú agentov schopnosťou porozumieť kontextu, prispôsobiť sa meniacemu sa prostrediu a prijímať rozhodnutia na základe informácií v reálnom čase.

Takže v skratke, agenti vám umožňujú robiť viac, posunúť automatizáciu na vyššiu úroveň a vytvoriť inteligentnejšie systémy, ktoré sa dokážu prispôsobiť a učiť sa zo svojho prostredia.

## How to quickly prototype, iterate, and improve the agent’s capabilities?

Toto je rýchlo sa meniacae odvetvie, ale existujú určité spoločné prvky vo väčšine rámcov pre AI agentov, ktoré vám môžu pomôcť rýchlo prototypovať a iterovať, a to modulárne komponenty, kolaboratívne nástroje a učenie v reálnom čase. Pozrime sa na ne podrobnejšie:

- **Používajte modulárne komponenty**: AI SDK poskytujú predpripravené komponenty, ako sú AI a Memory konektory, volanie funkcií pomocou prirodzeného jazyka alebo pluginov v kóde, šablóny promptov a ďalšie.
- **Využite kolaboratívne nástroje**: Navrhnite agentov s konkrétnymi rolami a úlohami, aby mohli testovať a zdokonaľovať kolaboratívne pracovné toky.
- **Učte sa v reálnom čase**: Implementujte spätné väzby, v ktorých sa agenti učia z interakcií a dynamicky upravujú svoje správanie.

### Use Modular Components

SDK ako Microsoft Agent Framework ponúkajú predpripravené komponenty, ako sú AI konektory, definície nástrojov a správa agentov.

**Ako to môžu tímy využiť**: Tímy môžu rýchlo zostaviť tieto komponenty na vytvorenie funkčného prototypu bez začínania od nuly, čo umožňuje rýchlé experimentovanie a iterácie.

**Ako to funguje v praxi**: Môžete použiť predpripravený parser na extrakciu informácií z používateľského vstupu, modul pamäte na ukladanie a získavanie dát a generátor promptov na interakciu s používateľmi, to všetko bez potreby budovať tieto komponenty od začiatku.

**Example code**. Pozrime sa na príklad, ako môžete použiť Microsoft Agent Framework s `AzureAIProjectAgentProvider`, aby model reagoval na používateľský vstup s volaním nástrojov:

``` python
# Príklad Python rámca Microsoft Agent

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# Definujte vzorovú nástrojovú funkciu na rezerváciu cesty
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
    # Ukážkový výstup: Váš let do New Yorku na 1. januára 2025 bol úspešne rezervovaný. Šťastnú cestu! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Z toho, čo vidíte v tomto príklade, je zrejmé, ako môžete využiť predpripravený parser na extrakciu kľúčových informácií z používateľského vstupu, ako sú pôvod, cieľ a dátum žiadosti o rezerváciu letu. Tento modulárny prístup vám umožní sústrediť sa na logiku na vysokej úrovni.

### Leverage Collaborative Tools

Rámce ako Microsoft Agent Framework uľahčujú vytváranie viacerých agentov, ktorí môžu spolupracovať.

**Ako to môžu tímy využiť**: Tímy môžu navrhovať agentov s konkrétnymi rolami a úlohami, čo im umožní testovať a zdokonaľovať kolaboratívne pracovné toky a zvyšovať celkovú efektivitu systému.

**Ako to funguje v praxi**: Môžete vytvoriť tím agentov, kde každý agent má špecializovanú funkciu, ako je získavanie dát, analýza alebo rozhodovanie. Títo agenti môžu komunikovať a zdieľať informácie, aby dosiahli spoločný cieľ, napríklad odpovedanie na používateľský dotaz alebo dokončenie úlohy.

**Example code (Microsoft Agent Framework)**:

```python
# Vytváranie viacerých agentov, ktorí spolupracujú pomocou Microsoft Agent Framework

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Agent na získavanie údajov
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Agent na analýzu údajov
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Spustenie agentov postupne na úlohe
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

V predchádzajúcom kóde vidíte, ako môžete vytvoriť úlohu, ktorá zahŕňa viacerých agentov spolupracujúcich na analýze dát. Každý agent vykonáva konkrétnu funkciu a úloha sa vykonáva koordináciou agentov s cieľom dosiahnuť požadovaný výsledok. Vytváraním venovaných agentov so špecializovanými rolami môžete zlepšiť efektivitu a výkon úloh.

### Learn in Real-Time

Pokročilé rámce poskytujú schopnosti na pochopenie kontextu v reálnom čase a adaptáciu.

**Ako to môžu tímy využiť**: Tímy môžu implementovať spätné väzby, kde sa agenti učia z interakcií a dynamicky upravujú svoje správanie, čo vedie k neustálemu zlepšovaniu a doladeniu schopností.

**Ako to funguje v praxi**: Agenti môžu analyzovať spätnú väzbu od používateľov, dátové informácie z prostredia a výsledky úloh, aby aktualizovali svoju databázu znalostí, upravili algoritmy rozhodovania a zlepšili výkon v priebehu času. Tento iteratívny proces učenia umožňuje agentom prispôsobiť sa meniacim sa podmienkam a preferenciám používateľov, čím sa zvyšuje celková efektívnosť systému.

## What are the differences between the Microsoft Agent Framework and Azure AI Agent Service?

Existuje mnoho spôsobov, ako tieto prístupy porovnať, ale poďme sa pozrieť na niektoré kľúčové rozdiely z hľadiska ich dizajnu, schopností a cieľových prípadov použitia:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework poskytuje zjednodušené SDK na vytváranie AI agentov pomocou `AzureAIProjectAgentProvider`. Umožňuje vývojárom vytvárať agentov, ktorí využívajú Azure OpenAI modely s vstavaným volaním nástrojov, správou konverzácií a bezpečnosťou na podnikovej úrovni cez Azure identity.

**Prípady použitia**: Vytváranie produkčne pripravených AI agentov s používaním nástrojov, viacstupňovými pracovnými tokmi a scenármi podnikovej integrácie.

Tu sú niektoré dôležité základné koncepty Microsoft Agent Framework:

- **Agents**. Agent sa vytvára cez `AzureAIProjectAgentProvider` a konfiguruje sa so špecifikovaním mena, inštrukcií a nástrojov. Agent môže:
  - **Spracovávať používateľské správy** a generovať odpovede pomocou Azure OpenAI modelov.
  - **Automaticky volať nástroje** na základe kontextu konverzácie.
  - **Udržiavať stav konverzácie** naprieč viacerými interakciami.

  Tu je ukážka kódu, ktorá ukazuje, ako vytvoriť agenta:

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

- **Tools**. Rámec podporuje definovanie nástrojov ako Python funkcií, ktoré môže agent automaticky zavolať. Nástroje sa registrujú pri vytváraní agenta:

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

- **Koordinácia viacerých agentov**. Môžete vytvoriť viacerých agentov s rôznymi špecializáciami a koordinovať ich prácu:

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

- **Integrácia Azure Identity**. Rámec používa `AzureCliCredential` (alebo `DefaultAzureCredential`) na bezpečnú autentifikáciu bez kľúčov, čím eliminuje potrebu spravovať API kľúče priamo.

## Azure AI Agent Service

Azure AI Agent Service je novší doplnok, predstavený na Microsoft Ignite 2024. Umožňuje vývoj a nasadzovanie AI agentov s flexibilnejšími modelmi, ako je priame volanie open-source LLM ako Llama 3, Mistral a Cohere.

Azure AI Agent Service poskytuje silnejšie mechanizmy podnikovej bezpečnosti a metódy ukladania dát, čo z neho robí vhodné riešenie pre podnikové aplikácie.

Funguje okamžite s Microsoft Agent Framework pre vytváranie a nasadzovanie agentov.

Táto služba je v súčasnosti v Public Preview a podporuje Python a C# na vytváranie agentov.

Použitím Python SDK Azure AI Agent Service môžeme vytvoriť agenta s používateľom definovaným nástrojom:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Definujte funkcie nástroja
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

### Core concepts

Azure AI Agent Service má nasledujúce základné koncepty:

- **Agent**. Azure AI Agent Service sa integruje s Microsoft Foundry. V rámci AI Foundry funguje AI Agent ako "chybná" mikroslužba, ktorú je možné použiť na odpovedanie na otázky (RAG), vykonávanie akcií alebo úplnú automatizáciu pracovných tokov. Dosahuje to kombinovaním sily generatívnych AI modelov s nástrojmi, ktoré mu umožňujú pristupovať a interagovať s reálnymi zdrojmi údajov. Tu je príklad agenta:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    V tomto príklade je agent vytvorený s modelom `gpt-4o-mini`, menom `my-agent` a inštrukciami `You are helpful agent`. Agent je vybavený nástrojmi a zdrojmi na vykonávanie úloh interpretácie kódu.

- **Thread and messages**. Thread je ďalší dôležitý koncept. Predstavuje konverzáciu alebo interakciu medzi agentom a používateľom. Thready sa dajú použiť na sledovanie priebehu konverzácie, ukladanie kontextových informácií a riadenie stavu interakcie. Tu je príklad threadu:

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

    V predchádzajúcom kóde je vytvorený thread. Následne je do threadu odoslaná správa. Volaním `create_and_process_run` je agent požiadaný, aby na threade vykonal prácu. Nakoniec sú správy získané a zaznamenané, aby sa videla odpoveď agenta. Správy naznačujú priebeh konverzácie medzi používateľom a agentom. Je tiež dôležité pochopiť, že správy môžu byť rôznych typov, ako text, obrázok alebo súbor — to znamená, že práca agentov mala za výsledok napríklad obrázok alebo textovú odpoveď. Ako vývojár potom môžete tieto informácie ďalej spracovať alebo zobraziť používateľovi.

- **Integruje sa s Microsoft Agent Framework**. Azure AI Agent Service funguje bezproblémovo s Microsoft Agent Framework, čo znamená, že môžete vytvárať agentov pomocou `AzureAIProjectAgentProvider` a nasadzovať ich cez Agent Service pre produkčné scenáre.

**Prípady použitia**: Azure AI Agent Service je navrhnutá pre podnikové aplikácie, ktoré vyžadujú bezpečné, škálovateľné a flexibilné nasadzovanie AI agentov.

## What's the difference between these approaches?
 
Znie to, že existuje prekrytie, ale sú tu niektoré kľúčové rozdiely z hľadiska ich dizajnu, schopností a cieľových prípadov použitia:
 
- **Microsoft Agent Framework (MAF)**: Je to produkčne pripravené SDK na vytváranie AI agentov. Poskytuje zjednodušené API na vytváranie agentov s volaním nástrojov, správou konverzácií a integráciou Azure identity.
- **Azure AI Agent Service**: Je to platforma a nasadzovacia služba v Azure Foundry pre agentov. Ponúka vstavané konektivity k službám ako Azure OpenAI, Azure AI Search, Bing Search a vykonávanie kódu.
 
Stále si nie ste istí, ktorý si vybrať?

### Use Cases
 
Pozrime sa, či vám môžeme pomôcť prejsť niektoré bežné prípady použitia:
 
> Q: Stavám produkčne AI agent aplikácie a chcem začať rýchlo
>

>A: Microsoft Agent Framework je skvelá voľba. Poskytuje jednoduché, "pythonic" API cez `AzureAIProjectAgentProvider`, ktoré vám umožní definovať agentov s nástrojmi a inštrukciami v len niekoľkých riadkoch kódu.

>Q: Potrebujem nasadenie na podnikovej úrovni s integráciami Azure ako Search a vykonávanie kódu
>
> A: Azure AI Agent Service je najvhodnejšie. Je to platformová služba, ktorá poskytuje vstavané schopnosti pre viacero modelov, Azure AI Search, Bing Search a Azure Functions. Uľahčuje vytváranie agentov v Foundry Portáli a ich nasadzovanie v škálovateľnom režime.
 
> Q: Stále som zmätený, len mi dajte jednu možnosť
>
> A: Začnite s Microsoft Agent Framework na vytváranie vašich agentov a potom použite Azure AI Agent Service, keď budete potrebovať ich nasadiť a škálovať v produkcii. Tento prístup vám umožní rýchlo iterovať na logike agenta a zároveň mať jasnú cestu k podnikovej nasaditeľnosti.
 
Zhrňme kľúčové rozdiely v tabuľke:

| Framework | Focus | Core Concepts | Use Cases |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Streamlined agent SDK with tool calling | Agents, Tools, Azure Identity | Building AI agents, tool use, multi-step workflows |
| Azure AI Agent Service | Flexible models, enterprise security, Code generation, Tool calling | Modularity, Collaboration, Process Orchestration | Secure, scalable, and flexible AI agent deployment |

## Can I integrate my existing Azure ecosystem tools directly, or do I need standalone solutions?
Odpoveď je áno, môžete integrovať svoje existujúce nástroje v ekosystéme Azure priamo so službou Azure AI Agent Service, najmä preto, že bola navrhnutá na bezproblémovú spoluprácu s ostatnými službami Azure. Môžete napríklad integrovať Bing, Azure AI Search a Azure Functions. Existuje tiež hlboká integrácia s Microsoft Foundry.

The Microsoft Agent Framework also integrates with Azure services through `AzureAIProjectAgentProvider` and Azure identity, letting you call Azure services directly from your agent tools.

## Ukážky kódu

- Python: [Rámec agenta](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Rámec agenta](./code_samples/02-dotnet-agent-framework.md)

## Máte ďalšie otázky o rámcoch AI agentov?

Pridajte sa na [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), aby ste sa stretli s ostatnými študentmi, zúčastnili sa konzultačných hodín a získali odpovede na svoje otázky o AI agentech.

## Referencie

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Služba Azure Agent</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI odpovede</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Služba Azure AI Agent</a>

## Predchádzajúca lekcia

[Úvod do AI agentov a ich prípadov použitia](../01-intro-to-ai-agents/README.md)

## Nasledujúca lekcia

[Porozumenie agentickým návrhovým vzorom](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Vyhlásenie o zodpovednosti:
Tento dokument bol preložený pomocou AI prekladateľskej služby Co-op Translator (https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, berte na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by sa mal považovať za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->