[![Preskúmanie rámcov AI agentov](../../../translated_images/sk/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Kliknite na obrázok vyššie pre zobrazenie videa tejto lekcie)_

# Preskúmanie rámcov AI agentov

Rámce AI agentov sú softvérové platformy navrhnuté na zjednodušenie vytvárania, nasadenia a správy AI agentov. Tieto rámce poskytujú vývojárom predpripravené komponenty, abstrakcie a nástroje, ktoré zefektívňujú vývoj zložitých AI systémov.

Tieto rámce pomáhajú vývojárom sústrediť sa na jedinečné aspekty svojich aplikácií tým, že poskytujú štandardizované prístupy k bežným výzvam vo vývoji AI agentov. Zvyšujú škálovateľnosť, dostupnosť a efektivitu pri tvorbe AI systémov.

## Úvod

Táto lekcia pokryje:

- Čo sú rámce AI agentov a čo umožňujú vývojárom dosiahnuť?
- Ako môžu tímy tieto rámce využiť na rýchle prototypovanie, iterovanie a zlepšovanie schopností svojho agenta?
- Aké sú rozdiely medzi rámcami a nástrojmi vytvorenými Microsoftom (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> a <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Môžem integrovať svoje existujúce nástroje Azure ekosystému priamo, alebo potrebujem samostatné riešenia?
- Čo je Microsoft Foundry Agent Service a ako mi pomáha?

## Výučbové ciele

Ciele tejto lekcie sú pomôcť vám pochopiť:

- Úlohu rámcov AI agentov vo vývoji AI.
- Ako využiť rámce AI agentov na vytváranie inteligentných agentov.
- Kľúčové schopnosti umožnené rámcami AI agentov.
- Rozdiely medzi Microsoft Agent Framework a Microsoft Foundry Agent Service.

## Čo sú rámce AI agentov a čo umožňujú vývojárom robiť?

Tradičné rámce AI vám môžu pomôcť integrovať AI do vašich aplikácií a zlepšiť tieto aplikácie nasledujúcimi spôsobmi:

- **Personalizácia**: AI môže analyzovať správanie a preferencie používateľa a poskytovať personalizované odporúčania, obsah a zážitky.
Príklad: Streamingové služby ako Netflix používajú AI na odporúčanie filmov a relácií na základe histórie prezerania, čím zvyšujú zapojenie a spokojnosť používateľov.
- **Automatizácia a efektivita**: AI môže automatizovať opakujúce sa úlohy, zefektívniť pracovné postupy a zlepšiť prevádzkovú efektivitu.
Príklad: Aplikácie zákazníckeho servisu využívajú AI chatbotov na vybavovanie bežných otázok, čím skracujú čas odozvy a uvoľňujú ľudských agentov pre zložitejšie problémy.
- **Zlepšený používateľský zážitok**: AI môže zlepšiť celkový používateľský zážitok poskytovaním inteligentných funkcií, ako je rozpoznávanie hlasu, spracovanie prirodzeného jazyka a predikcia textu.
Príklad: Virtuálni asistenti ako Siri a Google Assistant používajú AI na pochopenie a odpovedanie na hlasové príkazy, čo uľahčuje interakciu používateľov so zariadeniami.

### To všetko znie skvele, tak prečo potrebujeme rámec AI agenta?

Rámce AI agentov predstavujú niečo viac než len AI rámce. Sú navrhnuté na umožnenie vytvárania inteligentných agentov, ktorí môžu interagovať s používateľmi, inými agentmi a prostredím za účelom dosiahnutia konkrétnych cieľov. Títo agenti môžu prejavovať autonómne správanie, robiť rozhodnutia a prispôsobovať sa meniacim sa podmienkam. Pozrime sa na niektoré kľúčové schopnosti umožnené rámcami AI agentov:

- **Spolupráca a koordinácia agentov**: Umožňujú vytváranie viacerých AI agentov, ktorí môžu spolupracovať, komunikovať a koordinovať sa na riešení zložitých úloh.
- **Automatizácia a manažment úloh**: Poskytujú mechanizmy na automatizáciu viacstupňových pracovných postupov, delegovanie úloh a dynamický manažment úloh medzi agentmi.
- **Kontextové porozumenie a adaptácia**: Vybavujú agentov schopnosťou chápať kontext, prispôsobovať sa meniacemu sa prostrediu a robiť rozhodnutia na základe informácií v reálnom čase.

Zhrnuté a podčiarknuté, agenti vám umožňujú robiť viac, posunúť automatizáciu na vyššiu úroveň, vytvárať inteligentnejšie systémy, ktoré sa môžu prispôsobovať a učiť sa zo svojho prostredia.

## Ako rýchlo prototypovať, iterovať a zlepšovať schopnosti agenta?

Toto je rýchlo sa meniace prostredie, ale existujú niektoré spoločné veci vo väčšine rámcov AI agentov, ktoré vám pomôžu rýchlo prototypovať a iterovať, a to predovšetkým modulárne komponenty, kolaboratívne nástroje a učenie v reálnom čase. Poďme sa na to pozrieť:

- **Používajte modulárne komponenty**: AI SDK ponúkajú predpripravené komponenty ako AI a pamäťové konektory, volanie funkcií pomocou prirodzeného jazyka alebo kódových pluginov, predlohy promptov a ďalšie.
- **Využívajte kolaboratívne nástroje**: Navrhujte agentov so špecifickými úlohami a rolami, čo im umožňuje testovať a zdokonaľovať kolaboratívne pracovné postupy.
- **Učte sa v reálnom čase**: Implementujte spätnoväzobné slučky, kde sa agenti učia z interakcií a dynamicky prispôsobujú svoje správanie.

### Používajte modulárne komponenty

SDK ako Microsoft Agent Framework ponúkajú predpripravené komponenty, ako AI konektory, definície nástrojov a správu agentov.

**Ako môžu tímy tieto používať**: Tímy môžu rýchlo zostaviť tieto komponenty na vytvorenie funkčného prototypu bez nutnosti začínať od nuly, čo umožňuje rýchle experimentovanie a iterovanie.

**Ako to funguje v praxi**: Môžete použiť predpripravený parser na extrahovanie informácií z užívateľského vstupu, pamäťový modul na ukladanie a získavanie dát a generátor promptov na interakciu s používateľmi, to všetko bez nutnosti vytvárať tieto komponenty od začiatku.

**Ukážkový kód**. Pozrime sa na príklad, ako použiť Microsoft Agent Framework s `FoundryChatClient` na reagovanie modelu na užívateľský vstup s volaním nástrojov:

``` python
# Príklad Microsoft Agent Framework v Pythone

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Definujte ukážkovú funkciu nástroja na rezerváciu cesty
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
    # Príklad výstupu: Váš let do New Yorku na 1. januára 2025 bol úspešne rezervovaný. Šťastnú cestu! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Z tohto príkladu vidíte, ako môžete využiť predpripravený parser na extrahovanie kľúčových informácií z užívateľského vstupu, napríklad počiatočné miesto, cieľ a dátum požiadavky na rezerváciu letu. Tento modulárny prístup vám umožňuje zamerať sa na logiku na vysokej úrovni.

### Využívajte kolaboratívne nástroje

Rámce ako Microsoft Agent Framework umožňujú vytváranie viacerých agentov, ktorí môžu spolupracovať.

**Ako môžu tímy tieto používať**: Tímy môžu navrhovať agentov so špecifickými rolami a úlohami, čo im umožňuje testovať a zdokonaľovať kolaboratívne pracovné postupy a zvyšovať celkovú efektivitu systému.

**Ako to funguje v praxi**: Môžete vytvoriť tím agentov, kde každý agent má špecializovanú funkciu, napríklad získavanie dát, analýzu alebo rozhodovanie. Títo agenti môžu komunikovať a zdieľať informácie na dosiahnutie spoločného cieľa, ako je zodpovedanie otázky používateľa alebo dokončenie úlohy.

**Ukážkový kód (Microsoft Agent Framework)**:

```python
# Vytváranie viacerých agentov, ktorí spolupracujú pomocou Microsoft Agent Framework

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Agent na získavanie údajov
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Agent na analýzu údajov
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Spustiť agentov v poradí na úlohe
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

V predchádzajúcom kóde vidíte, ako vytvoriť úlohu, ktorá zahŕňa viacerých agentov pracujúcich spolu na analýze dát. Každý agent vykonáva špecifickú funkciu a úloha je realizovaná koordináciou agentov na dosiahnutie požadovaného výsledku. Vytvorením špecializovaných agentov so špecifickými rolami môžete zvýšiť efektivitu a výkon úlohy.

### Učte sa v reálnom čase

Pokročilé rámce poskytujú schopnosti na porozumenie kontextu a adaptáciu v reálnom čase.

**Ako môžu tímy tieto používať**: Tímy môžu implementovať spätnoväzobné slučky, kde sa agenti učia z interakcií a dynamicky prispôsobujú svoje správanie, čo vedie k neustálemu zlepšovaniu a zdokonaľovaniu schopností.

**Ako to funguje v praxi**: Agenti môžu analyzovať spätnú väzbu používateľov, dáta z prostredia a výsledky úloh na aktualizáciu svojej znalostnej základne, úpravu rozhodovacích algoritmov a zlepšenie výkonu v priebehu času. Tento iteratívny učebný proces umožňuje agentom prispôsobovať sa meniacim sa podmienkam a preferenciám používateľov, čím sa zvyšuje celková efektívnosť systému.

## Aké sú rozdiely medzi Microsoft Agent Framework a Microsoft Foundry Agent Service?

Existuje mnoho spôsobov, ako tieto prístupy porovnať, ale pozrime sa na niektoré kľúčové rozdiely z hľadiska ich dizajnu, schopností a cieľových prípadov použitia:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework poskytuje zjednodušené SDK na vytváranie AI agentov pomocou `FoundryChatClient`. Umožňuje vývojárom vytvárať agentov, ktorí využívajú modely Azure OpenAI s vstavaným volaním nástrojov, správou konverzácie a podnikových bezpečnostných prvkov cez Azure identitu.

**Prípady použitia**: Vytváranie AI agentov pripravených na produkciu s využívaním nástrojov, multi-krokové pracovné postupy a scenáre podnikovej integrácie.

Tu sú niektoré dôležité základné koncepty Microsoft Agent Framework:

- **Agenti**. Agent sa vytvára cez `FoundryChatClient` a konfiguruje sa s menom, inštrukciami a nástrojmi. Agent môže:
  - **Spracovávať správy používateľa** a generovať odpovede pomocou modelov Azure OpenAI.
  - **Volat nástroje** automaticky na základe kontextu konverzácie.
  - **Udržiavať stav konverzácie** počas viacerých interakcií.

  Tu je ukážka kódu, ako vytvoriť agenta:

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

- **Nástroje**. Rámec podporuje definovanie nástrojov ako Python funkcie, ktoré môže agent automaticky vyvolať. Nástroje sa registrovali pri vytváraní agenta:

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

- **Koordinácia viacerých agentov**. Môžete vytvoriť viacerých agentov so špecializáciami a koordinovať ich prácu:

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

- **Integrácia Azure Identity**. Rámec využíva `AzureCliCredential` (alebo `DefaultAzureCredential`) pre bezpečnú autentifikáciu bez potreby spravovať API kľúče priamo.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service je novší doplnok predstavený na Microsoft Ignite 2024. Umožňuje vývoj a nasadenie AI agentov s flexibilnejšími modelmi, ako je priame volanie open-source LLM ako Llama 3, Mistral a Cohere.

Microsoft Foundry Agent Service poskytuje silnejšie podnikové bezpečnostné mechanizmy a metódy ukladania dát, čo ho robí vhodným pre podnikové aplikácie. 

Funguje priamo s Microsoft Agent Frameworkom na vytváranie a nasadenie agentov.

Táto služba je momentálne v verejnej Preview a podporuje Python a C# na tvorbu agentov.

Pomocou Microsoft Foundry Agent Service Python SDK môžeme vytvoriť agenta s používateľom definovaným nástrojom:

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

### Základné koncepty

Microsoft Foundry Agent Service má tieto základné koncepty:

- **Agent**. Microsoft Foundry Agent Service sa integruje s Microsoft Foundry. V rámci Microsoft Foundry AI Agent funguje ako "inteligentná" mikroslužba, ktorá môže odpovedať na otázky (RAG), vykonávať akcie alebo úplne automatizovať pracovné postupy. Dosahuje to kombináciou sily generatívnych AI modelov s nástrojmi, ktoré jej umožňujú pristupovať a interagovať s real-world dátovými zdrojmi. Tu je príklad agenta:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    V tomto príklade je agent vytvorený s modelom `gpt-5-mini`, menom `my-agent` a inštrukciami `You are helpful agent`. Agent je vybavený nástrojmi a zdrojmi na vykonávanie úloh interpretácie kódu.

- **Vlákno a správy**. Vlákno je ďalší dôležitý koncept. Reprezentuje konverzáciu alebo interakciu medzi agentom a používateľom. Vlákna môžu byť použité na sledovanie priebehu konverzácie, ukladanie kontextových informácií a správu stavu interakcie. Tu je príklad vlákna:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Požiadať agenta, aby vykonal prácu na vlákne
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Načítať a zaznamenať všetky správy, aby sa videla agentova odpoveď
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    V predchádzajúcom kóde sa vytvorilo vlákno. Následne sa do vlákna poslalo správa. Volaním `create_and_process_run` je agent požiadaný o vykonanie práce vo vlákne. Nakoniec sa správy načítajú a zaznamenajú, aby sme videli reakciu agenta. Správy ukazujú priebeh konverzácie medzi používateľom a agentom. Je tiež dôležité pochopiť, že správy môžu byť rôznych typov, ako text, obrázok alebo súbor, čo znamená, že práca agenta mohla viesť napríklad k výstupu vo forme obrázka alebo textu. Ako vývojár môžete tieto informácie ďalej spracovať alebo ich prezentovať používateľovi.

- **Integrácia s Microsoft Agent Framework**. Microsoft Foundry Agent Service pracuje bezproblémovo s Microsoft Agent Frameworkom, čo znamená, že môžete vytvárať agentov pomocou `FoundryChatClient` a nasadzovať ich prostredníctvom Agent Service pre produkčné scenáre.

**Prípady použitia**: Microsoft Foundry Agent Service je navrhnutý pre podnikové aplikácie, ktoré vyžadujú bezpečné, škálovateľné a flexibilné nasadenie AI agentov.

## Aký je rozdiel medzi týmito prístupmi?
 
Znie to, akoby sa prekrývali, ale existujú kľúčové rozdiely z hľadiska dizajnu, schopností a cieľových aplikácií:
 
- **Microsoft Agent Framework (MAF)**: Je produkčné SDK na budovanie AI agentov. Poskytuje zjednodušené API na vytváranie agentov s volaním nástrojov, správou konverzácie a integráciou Azure identity.
- **Microsoft Foundry Agent Service**: Je platforma a služba nasadenia v Microsoft Foundry pre agentov. Ponúka vstavané prepojenia na služby ako Azure OpenAI, Azure AI Search, Bing Search a vykonávanie kódu.
 
Stále si nie ste istí, ktorý si vybrať?

### Prípady použitia
 
Pozrime sa, či vám môže pomôcť prejsť niektoré bežné prípady:
 
> Otázka: Budujem produkčné AI agent aplikácie a chcem začať rýchlo
>

> Odpoveď: Microsoft Agent Framework je vynikajúca voľba. Poskytuje jednoduché, pythonické API cez `FoundryChatClient`, ktoré vám umožní definovať agentov s nástrojmi a inštrukciami v iba niekoľkých riadkoch kódu.

> Otázka: Potrebujem podnikové nasadenie s Azure integráciami ako Search a vykonávanie kódu
>
> Odpoveď: Microsoft Foundry Agent Service je na to najvhodnejší. Je to platformová služba, ktorá poskytuje vstavané kapacity pre viaceré modely, Azure AI Search, Bing Search a Azure Functions. Uľahčuje vytváranie agentov v Foundry Portáli a ich nasadenie vo veľkom meradle.
 
> Otázka: Stále som zmätený, dajte mi jednu možnosť
>
> Odpoveď: Začnite s Microsoft Agent Framework na tvorbu agentov a potom použite Microsoft Foundry Agent Service, keď ich budete chcieť nasadiť a škálovať do produkcie. Tento prístup vám umožní rýchlo iterovať na logike agenta a zároveň mať jasnú cestu k podnikovému nasadeniu.
 
Zhrňme kľúčové rozdiely v tabuľke:

| Rámec | Zameranie | Základné koncepty | Prípady použitia |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Zjednodušené SDK pre agentov s volaním nástrojov | Agenti, Nástroje, Azure Identity | Budovanie AI agentov, použitie nástrojov, viacstupňové workflow |
| Microsoft Foundry Agent Service | Flexibilné modely, podniková bezpečnosť, generovanie kódu, volanie nástrojov | Modularita, Spolupráca, Orchestrácia procesov | Bezpečné, škálovateľné a flexibilné nasadenie AI agentov |

## Môžem integrovať svoje existujúce nástroje Azure ekosystému priamo, alebo potrebujem samostatné riešenia?


Odpoveď je áno, môžete integrovať svoje existujúce nástroje v rámci Azure ekosystému priamo s Microsoft Foundry Agent Service, najmä preto, že bol vybudovaný tak, aby bez problémov spolupracoval s ostatnými Azure službami. Napríklad môžete integrovať Bing, Azure AI Search a Azure Functions. Existuje tiež hlboká integrácia s Microsoft Foundry.

Microsoft Agent Framework sa tiež integruje so službami Azure cez `FoundryChatClient` a Azure identity, čo vám umožňuje volať Azure služby priamo z vašich agentových nástrojov.

## Ukážkové kódy

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Máte ďalšie otázky o AI Agent Frameworkoch?

Pridajte sa do [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), aby ste sa stretli s inými študentmi, zúčastnili sa konzultačných hodín a získali odpovede na svoje otázky týkajúce sa AI agentov.

## Referencie

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Predchádzajúca lekcia

[Úvod do AI agentov a ich použitia](../01-intro-to-ai-agents/README.md)

## Nasledujúca lekcia

[Pochopenie agentických dizajnových vzorov](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->