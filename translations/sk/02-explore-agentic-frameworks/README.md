[![Preskúmanie rámcov pre AI agentov](../../../translated_images/sk/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Kliknite na obrázok vyššie pre zobrazenie videa tejto lekcie)_

# Preskúmanie rámcov pre AI agentov

Rámce pre AI agentov sú softvérové platformy navrhnuté na zjednodušenie vytvárania, nasadenia a správy AI agentov. Tieto rámce poskytujú vývojárom predpripravené komponenty, abstrakcie a nástroje, ktoré zefektívňujú vývoj zložitých AI systémov.

Pomáhajú vývojárom sústrediť sa na jedinečné aspekty ich aplikácií tým, že poskytujú štandardizované prístupy k bežným výzvam vo vývoji AI agentov. Zvyšujú škálovateľnosť, prístupnosť a efektivitu pri tvorbe AI systémov.

## Úvod

Táto lekcia bude preberať:

- Čo sú rámce AI agentov a čo umožňujú vývojárom dosiahnuť?
- Ako môžu tímy rýchlo prototypovať, iterovať a zlepšovať schopnosti svojho agenta?
- Aké sú rozdiely medzi rámcami a nástrojmi vytvorenými spoločnosťou Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> a <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Môžem integrovať moje existujúce nástroje z Azure ekosystému priamo, alebo potrebujem samostatné riešenia?
- Čo je Microsoft Foundry Agent Service a ako mi pomáha?

## Ciele učenia

Cieľmi tejto lekcie je pomôcť vám pochopiť:

- Úlohu rámcov AI agentov vo vývoji AI.
- Ako využiť rámce AI agentov na tvorbu inteligentných agentov.
- Kľúčové schopnosti umožnené rámcami AI agentov.
- Rozdiely medzi Microsoft Agent Framework a Microsoft Foundry Agent Service.

## Čo sú rámce AI agentov a čo umožňujú vývojárom robiť?

Tradičné rámce AI vám môžu pomôcť integrovať AI do vašich aplikácií a zlepšiť ich nasledovnými spôsobmi:

- **Personalizácia**: AI môže analyzovať správanie a preferencie používateľov, aby poskytla personalizované odporúčania, obsah a zážitky.
Príklad: Streamingové služby ako Netflix používajú AI na návrh filmov a seriálov na základe histórie sledovania, čo zvyšuje zapojenie a spokojnosť používateľov.
- **Automatizácia a efektivita**: AI môže automatizovať opakujúce sa úlohy, zefektívniť pracovné postupy a zlepšiť prevádzkovú efektivitu.
Príklad: Aplikácie zákazníckej podpory využívajú AI chatovacích botov na spracovanie bežných otázok, čím skracujú dobu odozvy a uvoľňujú ľudských agentov na riešenie zložitejších problémov.
- **Vylepšený používateľský zážitok**: AI môže zlepšiť celkový používateľský zážitok poskytovaním inteligentných funkcií, ako je rozpoznávanie hlasu, spracovanie prirodzeného jazyka a prediktívny text.
Príklad: Virtuálni asistenti ako Siri a Google Assistant využívajú AI na pochopenie a reagovanie na hlasové príkazy, čo uľahčuje používateľom interakciu so zariadeniami.

### To všetko znie skvele, tak prečo potrebujeme rámec AI agentov?

Rámce AI agentov predstavujú niečo viac než len AI rámce. Sú navrhnuté tak, aby umožnili tvorbu inteligentných agentov, ktorí môžu komunikovať s používateľmi, inými agentmi a prostredím za účelom dosiahnutia konkrétnych cieľov. Títo agenti môžu prejavovať autonómne správanie, robiť rozhodnutia a prispôsobovať sa meniacim sa podmienkam. Pozrime sa na niektoré kľúčové schopnosti umožnené rámcami AI agentov:

- **Spolupráca a koordinácia agentov**: Umožňujú tvorbu viacerých AI agentov, ktorí môžu spolupracovať, komunikovať a koordinovať sa pri riešení zložitých úloh.
- **Automatizácia a riadenie úloh**: Poskytujú mechanizmy pre automatizáciu viacstupňových pracovných postupov, delegovanie úloh a dynamické riadenie úloh medzi agentmi.
- **Kontextové porozumenie a adaptácia**: Vybavujú agentov schopnosťou porozumieť kontextu, prispôsobiť sa meniacim sa podmienkam a robiť rozhodnutia na základe informácií v reálnom čase.

Takže zhrnuté, agenti vám umožňujú robiť viac, posunúť automatizáciu na vyššiu úroveň a vytvárať inteligentnejšie systémy, ktoré sa môžu učiť a prispôsobovať zo svojho prostredia.

## Ako rýchlo prototypovať, iterovať a zlepšovať schopnosti agenta?

Toto je rýchlo sa meniace prostredie, ale existujú určité spoločné prvky vo väčšine rámcov AI agentov, ktoré vám môžu pomôcť rýchlo prototypovať a iterovať, konkrétne modulárne komponenty, kolaboratívne nástroje a učenie v reálnom čase. Pozrime sa na ne:

- **Používajte modulárne komponenty**: AI SDK ponúkajú predpripravené komponenty ako AI a pamäťové konektory, volanie funkcií pomocou prirodzeného jazyka alebo kódových pluginov, šablóny výziev a ďalšie.
- **Využite kolaboratívne nástroje**: Navrhujte agentov so špecifickými rolami a úlohami, čo im umožní testovať a zdokonaľovať kolaboratívne pracovné postupy.
- **Učte sa v reálnom čase**: Implementujte spätné väzby, kde sa agenti učia z interakcií a dynamicky prispôsobujú svoje správanie.

### Používajte modulárne komponenty

SDK ako Microsoft Agent Framework ponúkajú predpripravené komponenty ako AI konektory, definície nástrojov a správu agentov.

**Ako to môžu tím používať**: Tímy môžu rýchlo skladať tieto komponenty na vytvorenie funkčného prototypu bez začínania od nuly, čo umožňuje rýchle experimentovanie a iteráciu.

**Ako to funguje v praxi**: Môžete použiť predpripravený parser na extrakciu informácií zo vstupu používateľa, pamäťový modul na ukladanie a získavanie dát a generátor výziev na interakciu s používateľmi, to všetko bez potreby stavať tieto komponenty od nuly.

**Príklad kódu**. Pozrime sa na príklad, ako používať Microsoft Agent Framework s `FoundryChatClient`, aby model odpovedal na vstup používateľa s volaním nástrojov:

``` python
# Príklad Microsoft Agent Framework v Pythone

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Definujte ukážkovú funkciu nástroja na rezerváciu cestovania
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
    # Príklad výstupu: Váš let do New Yorku dňa 1. januára 2025 bol úspešne rezervovaný. Šťastnú cestu! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Z tohto príkladu vidíte, ako možno využiť predpripravený parser na extrakciu kľúčových informácií zo vstupu používateľa, ako je pôvod, cieľ a dátum požiadavky na rezerváciu letu. Tento modulárny prístup vám umožňuje sústrediť sa na logiku na vysokej úrovni.

### Využite kolaboratívne nástroje

Rámce ako Microsoft Agent Framework uľahčujú tvorbu viacerých agentov, ktorí môžu spolupracovať.

**Ako to môžu tím používať**: Tímy môžu navrhovať agentov so špecifickými rolami a úlohami, čo im umožňuje testovať a zlepšovať kolaboratívne pracovné postupy a zvýšiť celkovú efektivitu systému.

**Ako to funguje v praxi**: Môžete vytvoriť tím agentov, kde každý agent má špecializovanú funkciu, napríklad získavanie dát, analýzu či rozhodovanie. Títo agenti môžu komunikovať a zdieľať informácie, aby dosiahli spoločný cieľ, napríklad odpovedať na používateľskú otázku alebo splniť úlohu.

**Príklad kódu (Microsoft Agent Framework)**:

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

# Spustiť agentov postupne na úlohe
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

V predchádzajúcom kóde vidíte, ako vytvoriť úlohu, ktorá zahŕňa spoluprácu viacerých agentov pri analýze dát. Každý agent vykonáva špecifickú funkciu a úloha sa realizuje koordináciou agentov na dosiahnutie požadovaného výsledku. Vytvorením špecializovaných agentov môžete zlepšiť efektivitu a výkonnosť úloh.

### Učte sa v reálnom čase

Pokročilé rámce poskytujú schopnosti pre pochopenie kontextu a adaptáciu v reálnom čase.

**Ako to môžu tím používať**: Tímy môžu implementovať spätné väzby, kde sa agenti učia z interakcií a dynamicky prispôsobujú svoje správanie, čo vedie k neustálemu zlepšovaniu a zdokonaľovaniu schopností.

**Ako to funguje v praxi**: Agenti môžu analyzovať spätnú väzbu používateľov, environmentálne dáta a výsledky úloh, aby aktualizovali svoju databázu znalostí, prispôsobili algoritmy rozhodovania a zlepšovali výkonnosť v priebehu času. Tento iteratívny proces učenia umožňuje agentom adaptovať sa na meniace sa podmienky a preferencie používateľov, čím sa zvyšuje celková efektivita systému.

## Aké sú rozdiely medzi Microsoft Agent Framework a Microsoft Foundry Agent Service?

Existuje mnoho spôsobov, ako tieto prístupy porovnať, ale pozrime sa na niektoré kľúčové rozdiely v dizajne, schopnostiach a cieľových prípadoch použitia:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework poskytuje zjednodušené SDK na tvorbu AI agentov pomocou `FoundryChatClient`. Umožňuje vývojárom vytvárať agentov, ktorí využívajú Azure OpenAI modely s integrovaným volaním nástrojov, správou konverzácií a bezpečnosťou na úrovni podnikov prostredníctvom Azure identity.

**Použitie**: Tvorba produkčne pripravených AI agentov s využitím nástrojov, viacstupňových pracovných postupov a scenárov podnikovej integrácie.

Tu sú niektoré základné koncepty Microsoft Agent Framework:

- **Agenti**. Agent je vytvorený cez `FoundryChatClient` a nastavený s menom, inštrukciami a nástrojmi. Agent môže:
  - **Spracovávať používateľské správy** a generovať odpovede pomocou Azure OpenAI modelov.
  - **Automaticky volať nástroje** na základe kontextu konverzácie.
  - **Udržiavať stav konverzácie** cez viacero interakcií.

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

- **Nástroje**. Framework podporuje definovanie nástrojov ako Python funkcií, ktoré môže agent automaticky vyvolať. Nástroje sa registrujú pri vytváraní agenta:

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

- **Koordinácia viacerých agentov**. Môžete vytvoriť viacerých agentov s rôznymi špecializáciami a koordinovať ich prácu:

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

- **Integrácia Azure Identity**. Framework používa `AzureCliCredential` (alebo `DefaultAzureCredential`) pre bezpečnú autentifikáciu bez kľúčov, čím odstraňuje potrebu správy API kľúčov priamo.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service je novší prírastok, predstavený na Microsoft Ignite 2024. Umožňuje vývoj a nasadenie AI agentov s flexibilnejšími modelmi, ako je priame volanie open-source LLM, napríklad Llama 3, Mistral a Cohere.

Microsoft Foundry Agent Service poskytuje silnejšie mechanizmy podnikovej bezpečnosti a metódy ukladania dát, vďaka čomu je vhodný pre podnikové aplikácie.

Funguje ihneď v kombinácii s Microsoft Agent Framework pre tvorbu a nasadenie agentov.

Táto služba je momentálne v Public Preview a podporuje Python a C# na tvorbu agentov.

Pomocou Python SDK Microsoft Foundry Agent Service môžeme vytvoriť agenta s užívateľsky definovaným nástrojom:

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

### Základné koncepty

Microsoft Foundry Agent Service má nasledujúce základné koncepty:

- **Agent**. Microsoft Foundry Agent Service integruje Microsoft Foundry. V rámci Microsoft Foundry pôsobí AI Agent ako "inteligentná" mikroslužba, ktorá môže odpovedať na otázky (RAG), vykonávať akcie alebo úplne automatizovať pracovné postupy. Dosahuje to kombináciou generatívnej AI s nástrojmi umožňujúcimi prístup a interakciu so zdrojmi reálnych dát. Tu je príklad agenta:

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

- **Vlákno a správy**. Vlákno je ďalším dôležitým konceptom. Predstavuje konverzáciu alebo interakciu medzi agentom a používateľom. Vlákna sa používajú na sledovanie priebehu konverzácie, ukladanie kontextových informácií a správu stavu interakcie. Tu je príklad vlákna:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Požiadajte agenta, aby vykonal prácu na vlákne
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Načítajte a zaznamenajte všetky správy, aby ste videli odpoveď agenta
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    V predchádzajúcom kóde je vytvorené vlákno. Následne je do vlákna odoslaná správa. Volaním `create_and_process_run` je agent požiadaný, aby vykonal prácu na vlákne. Nakoniec sú správy načítané a zaznamenané, aby sa videla odpoveď agenta. Správy indikujú priebeh konverzácie medzi používateľom a agentom. Je tiež dôležité pochopiť, že správy môžu byť rôznych typov, napríklad text, obrázok alebo súbor, teda agent vykonal prácu, ktorá napríklad vyprodukovala obrázok alebo textovú odpoveď. Ako vývojár potom môžete tieto informácie ďalej spracovať alebo ich prezentovať používateľovi.

- **Integrácia s Microsoft Agent Framework**. Microsoft Foundry Agent Service funguje bezproblémovo s Microsoft Agent Framework, čo znamená, že môžete vytvárať agentov pomocou `FoundryChatClient` a nasadzovať ich cez Agent Service pre produkčné scenáre.

**Použitie**: Microsoft Foundry Agent Service je navrhnutý pre podnikové aplikácie, ktoré vyžadujú bezpečné, škálovateľné a flexibilné nasadenie AI agentov.

## Aký je rozdiel medzi týmito prístupmi?
 
Znie to, ako by bolo spoločné, ale existujú niektoré kľúčové rozdiely v dizajne, schopnostiach a cieľových prípadoch použitia:
 
- **Microsoft Agent Framework (MAF)**: Je produkčná SDK na tvorbu AI agentov. Poskytuje zjednodušené API na vytváranie agentov s volaním nástrojov, správou konverzácie a integráciou Azure identity.
- **Microsoft Foundry Agent Service**: Je platforma a služba nasadenia v Microsoft Foundry pre agentov. Ponúka vstavané prepojenia na služby ako Azure OpenAI, Azure AI Search, Bing Search a vykonávanie kódu.
 
Ešte si nie ste istí, ktorý vybrať?

### Prípady použitia
 
Pozrime sa, či vám pomôžeme prejsť niektoré bežné prípady použitia:
 
> Otázka: Vyvíjam produkčné AI agent aplikácie a chcem rýchlo začať
>

>Odpoveď: Microsoft Agent Framework je skvelá voľba. Poskytuje jednoduché, Pythonické API cez `FoundryChatClient`, ktoré vám umožní definovať agentov s nástrojmi a inštrukciami v len niekoľkých riadkoch kódu.

>Otázka: Potrebujem podnikové nasadenie so službami Azure, ako sú Search a vykonávanie kódu
>
> Odpoveď: Microsoft Foundry Agent Service je najvhodnejší. Je to platformová služba, ktorá poskytuje vstavané schopnosti pre viaceré modely, Azure AI Search, Bing Search a Azure Functions. Uľahčuje tvorbu agentov v Foundry portáli a ich nasadenie vo veľkom.
 
> Otázka: Stále som zmätený, dajte mi len jednu možnosť
>
> Odpoveď: Začnite s Microsoft Agent Framework na tvorbu agentov a potom použite Microsoft Foundry Agent Service, keď budete potrebovať nasadiť ich a škálovať v produkcii. Tento prístup vám umožňuje rýchlo iterovať na logike agenta a mať jasnú cestu k podnikovej implementácii.
 
Zhrňme kľúčové rozdiely v tabuľke:

| Framework | Zameranie | Základné koncepty | Prípady použitia |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Zjednodušené SDK pre agentov s volaním nástrojov | Agenti, Nástroje, Azure Identity | Tvorba AI agentov, využitie nástrojov, viacstupňové pracovné postupy |
| Microsoft Foundry Agent Service | Flexibilné modely, podniková bezpečnosť, generovanie kódu, volanie nástrojov | Modularita, Spolupráca, Orchestrácia procesov | Bezpečné, škálovateľné a flexibilné nasadenie AI agentov |

## Môžem integrovať moje existujúce nástroje z Azure ekosystému priamo, alebo potrebujem samostatné riešenia?


Odpoveď je áno, môžete integrovať svoje existujúce nástroje z ekosystému Azure priamo so službou Microsoft Foundry Agent Service najmä preto, že bola vybudovaná tak, aby bezproblémovo spolupracovala s ostatnými službami Azure. Môžete napríklad integrovať Bing, Azure AI Search a Azure Functions. Existuje tiež hlboká integrácia s Microsoft Foundry.

Microsoft Agent Framework sa tiež integruje so službami Azure cez `FoundryChatClient` a Azure identity, čo vám umožňuje volať služby Azure priamo z vašich nástrojov agenta.

## Ukážkové kódy

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Máte ďalšie otázky o AI Agent Frameworkoch?

Pridajte sa na [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), aby ste sa stretli s ďalšími študentmi, zúčastnili sa úradných hodín a získali odpovede na svoje otázky o AI agentoch.

## Referencie

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Predchádzajúca lekcia

[Úvod do AI agentov a prípadov použitia agentov](../01-intro-to-ai-agents/README.md)

## Nasledujúca lekcia

[Pochopenie agentových návrhových vzorov](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->