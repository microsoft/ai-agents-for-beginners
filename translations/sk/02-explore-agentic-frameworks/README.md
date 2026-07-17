[![Preskúmanie rámcov AI agentov](../../../translated_images/sk/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Kliknite na obrázok vyššie pre zobrazenie videa tejto lekcie)_

# Preskúmajte rámce AI agentov

Rámce AI agentov sú softvérové platformy navrhnuté na zjednodušenie tvorby, nasadzovania a správy AI agentov. Tieto rámce poskytujú vývojárom predpripravené komponenty, abstrakcie a nástroje, ktoré zefektívňujú vývoj komplexných AI systémov.

Tieto rámce pomáhajú vývojárom sústrediť sa na jedinečné aspekty ich aplikácií tým, že poskytujú štandardizované prístupy k bežným výzvam pri vývoji AI agentov. Zvyšujú škálovateľnosť, prístupnosť a efektivitu pri budovaní AI systémov.

## Úvod

Táto lekcia pokryje:

- Čo sú rámce AI agentov a čo umožňujú vývojárom dosiahnuť?
- Ako môžu tímy tieto rámce využiť na rýchle prototypovanie, iteráciu a zlepšovanie schopností svojho agenta?
- Aké sú rozdiely medzi rámcami a nástrojmi vytvorenými spoločnosťou Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> a <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Môžem integrovať svoje existujúce nástroje Azure ekosystému priamo, alebo potrebujem samostatné riešenia?
- Čo je Microsoft Foundry Agent Service a ako mi pomáha?

## Ciele učenia

Cieľmi tejto lekcie sú pomôcť vám pochopiť:

- Úlohu rámcov AI agentov vo vývoji AI.
- Ako využiť rámce AI agentov na tvorbu inteligentných agentov.
- Kľúčové schopnosti, ktoré rámce AI agentov umožňujú.
- Rozdiely medzi Microsoft Agent Framework a Microsoft Foundry Agent Service.

## Čo sú rámce AI agentov a čo umožňujú vývojárom robiť?

Tradičné rámce AI vám môžu pomôcť integrovať AI do vašich aplikácií a zlepšiť tieto aplikácie nasledujúcimi spôsobmi:

- **Personalizácia**: AI môže analyzovať správanie a preferencie používateľa, aby poskytla personalizované odporúčania, obsah a zážitky.
Príklad: Streamingové služby ako Netflix používajú AI na navrhovanie filmov a seriálov podľa histórie sledovania, čím zvyšujú angažovanosť a spokojnosť používateľa.
- **Automatizácia a efektivita**: AI dokáže automatizovať rutinné úlohy, zefektívniť pracovné toky a zlepšiť prevádzkovú efektivitu.
Príklad: Aplikácie zákazníckej podpory používajú chatovacích botov poháňaných AI na vybavovanie bežných otázok, čím skracujú časy odpovedí a uvoľňujú ľudských agentov pre komplexnejšie problémy.
- **Vylepšený používateľský zážitok**: AI môže zlepšiť celkový používateľský zážitok poskytovaním inteligentných funkcií ako rozpoznávanie hlasu, spracovanie prirodzeného jazyka a predikčný text.
Príklad: Virtuálni asistenti ako Siri a Google Assistant používajú AI na porozumenie a reagovanie na hlasové príkazy, čo uľahčuje používateľom interakciu s ich zariadeniami.

### To všetko znie skvele, tak prečo potrebujeme rámec AI agentov?

Rámce AI agentov predstavujú niečo viac než len rámce pre AI. Sú navrhnuté na umožnenie tvorby inteligentných agentov, ktorí môžu interagovať s používateľmi, inými agentmi a prostredím na dosiahnutie konkrétnych cieľov. Títo agenti môžu vykazovať autonómne správanie, robiť rozhodnutia a prispôsobovať sa meniacim sa podmienkam. Pozrime sa na niektoré kľúčové schopnosti, ktoré rámce AI agentov umožňujú:

- **Spolupráca a koordinácia agentov**: Umožňujú tvorbu viacerých AI agentov, ktorí môžu spolupracovať, komunikovať a koordinovať sa pri riešení zložitých úloh.
- **Automatizácia a riadenie úloh**: Poskytujú mechanizmy na automatizáciu viackrokových pracovných tokov, delegovanie úloh a dynamické riadenie úloh medzi agentmi.
- **Kontextové chápanie a adaptácia**: Vybavujú agentov schopnosťou rozumieť kontextu, prispôsobovať sa meniacim sa prostrediam a robiť rozhodnutia na základe informácií v reálnom čase.

Takže v súhrne, agenti vám umožňujú robiť viac, posunúť automatizáciu na vyššiu úroveň, vytvoriť inteligentnejšie systémy, ktoré sa môžu prispôsobovať a učiť sa zo svojho prostredia.

## Ako rýchlo prototypovať, iterovať a zlepšovať schopnosti agenta?

Toto je rýchlo sa meniacou oblasťou, ale existujú niektoré spoločné prvky v väčšine rámcov AI agentov, ktoré vám pomôžu rýchlo prototypovať a iterovať, predovšetkým modulárne komponenty, kolaboratívne nástroje a učenie v reálnom čase. Pozrime sa na ne bližšie:

- **Používajte modulárne komponenty**: AI SDK ponúkajú predpripravené komponenty ako AI a pamäťové konektory, volanie funkcií pomocou prirodzeného jazyka alebo kódových pluginov, šablóny promptov a ďalšie.
- **Využite kolaboratívne nástroje**: Navrhujte agentov so špecifickými úlohami a rolami, čo im umožní testovať a zdokonaľovať kolaboratívne pracovné toky.
- **Učte sa v reálnom čase**: Implementujte spätnoväzobné slučky, kde sa agenti učia z interakcií a dynamicky upravujú svoje správanie.

### Používajte modulárne komponenty

SDK ako Microsoft Agent Framework ponúka predpripravené komponenty, ako sú AI konektory, definície nástrojov a správa agentov.

**Ako to môžu tímy využívať**: Tímy môžu rýchlo zostaviť tieto komponenty na vytvorenie funkčného prototypu bez začíname od nuly, čo umožňuje rýchle experimentovanie a iteráciu.

**Ako to funguje v praxi**: Môžete použiť predpripravený parser na extrahovanie informácií z užívateľského vstupu, pamäťový modul na ukladanie a vyhľadávanie dát a generátor promptov pre interakciu s používateľmi, všetko bez nutnosti vytvárať tieto komponenty od základov.

**Príklad kódu**. Pozrime sa na príklad, ako môžete použiť Microsoft Agent Framework s `FoundryChatClient`, aby model reagoval na vstup používateľa volaním nástrojov:

``` python
# Príklad Microsoft Agent Framework v Pythone

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Definujte ukážkovú nástrojovú funkciu na rezerváciu cestovania
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

Z tohto príkladu vidíte, ako využiť predpripravený parser na extrakciu kľúčových informácií z užívateľského vstupu, ako je pôvod, cieľ a dátum požiadavky na rezerváciu letu. Tento modulárny prístup vám umožní sústrediť sa na logiku na vyššej úrovni.

### Využite kolaboratívne nástroje

Rámce ako Microsoft Agent Framework uľahčujú tvorbu viacerých agentov, ktorí môžu spolupracovať.

**Ako to môžu tímy využívať**: Tímy môžu navrhovať agentov so špecifickými úlohami a rolami, čo im umožňuje testovať a zdokonaľovať kolaboratívne pracovné toky a zlepšiť celkovú efektivitu systému.

**Ako to funguje v praxi**: Môžete vytvoriť tím agentov, kde každý agent má špecializovanú funkciu, ako je získavanie dát, analýza alebo rozhodovanie. Títo agenti môžu komunikovať a zdieľať informácie na dosiahnutie spoločného cieľa, napríklad odpovedať na dotaz používateľa alebo dokončiť úlohu.

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

# Agent na získavanie dát
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Agent na analýzu dát
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Spustiť agentov postupne pre úlohu
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

V predchádzajúcom kóde vidíte, ako môžete vytvoriť úlohu zahŕňajúcu viacerých agentov, ktorí spolupracujú na analýze dát. Každý agent vykonáva špecifickú funkciu a úloha sa vykonáva koordináciou agentov na dosiahnutie požadovaného výsledku. Vytvorením dedikovaných agentov so špecializovanými rolami môžete zlepšiť efektivitu a výkon úloh.

### Učte sa v reálnom čase

Pokročilé rámce poskytujú schopnosti pre porozumenie kontextu a adaptáciu v reálnom čase.

**Ako to môžu tímy využívať**: Tímy môžu implementovať spätnoväzobné slučky, kde sa agenti učia z interakcií a dynamicky upravujú svoje správanie, čo vedie k neustálemu zlepšovaniu a zdokonaľovaniu schopností.

**Ako to funguje v praxi**: Agenti môžu analyzovať spätnú väzbu používateľov, dátové prostredie a výsledky úloh na aktualizáciu svojej znalostnej bázy, úpravu algoritmov rozhodovania a zvyšovanie výkonu v čase. Tento iteratívny proces učenia umožňuje agentom prispôsobovať sa meniacim sa podmienkam a preferenciám používateľov, čím sa zvyšuje celková efektívnosť systému.

## Aké sú rozdiely medzi Microsoft Agent Framework a Microsoft Foundry Agent Service?

Existuje mnoho spôsobov, ako tieto prístupy porovnať, ale pozrime sa na niektoré kľúčové rozdiely z hľadiska dizajnu, schopností a cieľových prípadov použitia:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework poskytuje zjednodušené SDK na tvorbu AI agentov pomocou `FoundryChatClient`. Umožňuje vývojárom vytvárať agentov, ktorí využívajú modely Azure OpenAI s integrovaným volaním nástrojov, správou konverzácií a podnikovej úrovne zabezpečenia cez Azure identity.

**Prípady použitia**: Tvorba produkčne pripravených AI agentov s využitím nástrojov, viacstupňových pracovných tokov a scenárov integrácie v podniku.

Tu sú niektoré dôležité základné koncepty Microsoft Agent Framework:

- **Agenti**. Agent je vytváraný cez `FoundryChatClient` a konfigurovaný menom, inštrukciami a nástrojmi. Agent môže:
  - **Spracovávať správy používateľov** a generovať odpovede pomocou modelov Azure OpenAI.
  - **Automaticky volať nástroje** na základe kontextu konverzácie.
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

- **Nástroje**. Rámec podporuje definíciu nástrojov ako Python funkcií, ktoré môže agent automaticky vyvolať. Nástroje sa registrujú pri vytváraní agenta:

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

- **Integrácia Azure identity**. Rámec používa `AzureCliCredential` (alebo `DefaultAzureCredential`) pre bezpečnú autentifikáciu bez nutnosti spravovať API kľúče priamo.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service je novší prírastok, predstavený na Microsoft Ignite 2024. Umožňuje vývoj a nasadenie AI agentov s flexibilnejšími modelmi, napríklad priame volanie open-source LLM ako Llama 3, Mistral a Cohere.

Microsoft Foundry Agent Service poskytuje silnejšie mechanizmy podnikovej bezpečnosti a metódy ukladania dát, vďaka čomu je vhodný pre podnikové aplikácie.

Funguje okamžite s Microsoft Agent Framework pre tvorbu a nasadenie agentov.

Táto služba je momentálne vo verejnom náhľade a podporuje Python a C# na tvorbu agentov.

Pomocou Microsoft Foundry Agent Service Python SDK môžeme vytvoriť agenta s nástrojom definovaným používateľom:

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

### Základné koncepty

Microsoft Foundry Agent Service má tieto základné koncepty:

- **Agent**. Microsoft Foundry Agent Service sa integruje s Microsoft Foundry. V Microsoft Foundry AI agent funguje ako "inteligentná" mikroservisná služba, ktorú možno použiť na odpovedanie na otázky (RAG), vykonávanie akcií alebo úplnú automatizáciu pracovných tokov. Dosahuje to kombináciou sily generatívnych AI modelov s nástrojmi, ktoré mu umožňujú pristupovať a interagovať s reálnymi zdrojmi dát. Tu je príklad agenta:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4.1-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    V tomto príklade je agent vytvorený s modelom `gpt-4.1-mini`, menom `my-agent` a inštrukciami `You are helpful agent`. Agent je vybavený nástrojmi a zdrojmi na vykonávanie úloh interpretácie kódu.

- **Vlákno a správy**. Vlákno je ďalší dôležitý koncept. Reprezentuje konverzáciu alebo interakciu medzi agentom a používateľom. Vlákna sa používajú na sledovanie priebehu konverzácie, ukladanie kontextových informácií a riadenie stavu interakcie. Tu je príklad vlákna:

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

    V predchádzajúcom kóde bolo vytvorené vlákno. Následne bola do vlákna odoslaná správa. Volaním `create_and_process_run` je agent požiadaný o vykonanie práce na vlákne. Nakoniec sa správy načítajú a zaznamenajú, aby bolo vidieť odpoveď agenta. Správy odrážajú priebeh konverzácie medzi používateľom a agentom. Je tiež dôležité pochopiť, že správy môžu byť rôzneho typu, ako text, obrázok alebo súbor, teda práca agenta môže napríklad vyústiť do obrázka alebo textovej odpovede. Ako vývojár potom môžete tieto informácie ďalej spracovávať alebo ich prezentovať používateľovi.

- **Integrácia s Microsoft Agent Framework**. Microsoft Foundry Agent Service pracuje bezproblémovo s Microsoft Agent Framework, čo znamená, že môžete vytvárať agentov pomocou `FoundryChatClient` a nasadzovať ich cez Agent Service pre produkčné scenáre.

**Prípady použitia**: Microsoft Foundry Agent Service je určený pre podnikové aplikácie, ktoré vyžadujú bezpečné, škálovateľné a flexibilné nasadenie AI agentov.

## Aký je rozdiel medzi týmito prístupmi?
 
Znie to, akoby tu bol prekrývajúci sa priestor, ale existujú niektoré kľúčové rozdiely z hľadiska dizajnu, schopností a cieľových prípadov použitia:
 
- **Microsoft Agent Framework (MAF)**: Je produkčne pripravené SDK na tvorbu AI agentov. Poskytuje zjednodušené API na vytváranie agentov s volaním nástrojov, správou konverzácií a integráciou identity Azure.
- **Microsoft Foundry Agent Service**: Je platforma a služba nasadenia v Microsoft Foundry pre agentov. Ponúka zabudované prepojenie na služby ako Azure OpenAI, Azure AI Search, Bing Search a vykonávanie kódu.
 
Ešte si nie ste istí, ktorý si vybrať?

### Prípady použitia
 
Poďme sa pozrieť, či vám pomôžeme prejsť niektorými bežnými prípadmi použitia:
 
> Otázka: Staviam produkčné AI agent aplikácie a chcem začať rýchlo
>

>Odpoveď: Microsoft Agent Framework je skvelá voľba. Poskytuje jednoduché, pythonické API cez `FoundryChatClient`, ktoré vám umožní definovať agentov s nástrojmi a inštrukciami len v niekoľkých riadkoch kódu.

>Otázka: Potrebujem nasadenie na podnikovej úrovni s integráciou Azure služieb ako Search a vykonávanie kódu
>
> Odpoveď: Microsoft Foundry Agent Service je najvhodnejší. Je to platformová služba, ktorá poskytuje zabudované schopnosti pre viaceré modely, Azure AI Search, Bing Search a Azure Functions. Uľahčuje tvorbu vašich agentov v Foundry Portáli a ich škálovanie.
 
> Otázka: Som stále zmätený, len mi dajte jednu možnosť
>
> Odpoveď: Začnite s Microsoft Agent Framework na tvorbu agentov a potom použite Microsoft Foundry Agent Service, keď potrebujete nasadiť a škálovať ich v produkcii. Tento prístup umožňuje rýchlu iteráciu logiky agenta a zároveň jasnú cestu k podnikovej produkcii.
 
Zhrňme kľúčové rozdiely v tabuľke:

| Rámec | Zameranie | Základné koncepty | Prípady použitia |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Zjednodušené SDK pre agentov s volaním nástrojov | Agenti, Nástroje, Azure Identity | Tvorba AI agentov, využívanie nástrojov, viacstupňové pracovné toky |
| Microsoft Foundry Agent Service | Flexibilné modely, podniková bezpečnosť, generovanie kódu, volanie nástrojov | Modularita, Kolaborácia, Orchestrace procesov | Bezpečné, škálovateľné a flexibilné nasadenie AI agentov |

## Môžem integrovať svoje existujúce nástroje Azure ekosystému priamo, alebo potrebujem samostatné riešenia?


Odpoveď je áno, môžete integrovať svoje existujúce nástroje ekosystému Azure priamo so službou Microsoft Foundry Agent Service najmä preto, že bola navrhnutá tak, aby bezproblémovo spolupracovala s ostatnými službami Azure. Môžete napríklad integrovať Bing, Azure AI Search a Azure Functions. Existuje aj hlboká integrácia s Microsoft Foundry.

Rámec Microsoft Agent Framework sa taktiež integruje so službami Azure cez `FoundryChatClient` a Azure identity, čo umožňuje volať služby Azure priamo zo svojich nástrojov agenta.

## Ukážkové Kódy

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Máte Viac Otázok o AI Agent Frameworkoch?

Pripojte sa k [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kde sa stretnete s ďalšími študentmi, môžete navštíviť konzultačné hodiny a získať odpovede na vaše otázky týkajúce sa AI Agentov.

## Referencie

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Predchádzajúca Lekcia

[Úvod do AI Agentov a Prípadov Ich Použitia](../01-intro-to-ai-agents/README.md)

## Nasledujúca Lekcia

[Pochopenie Agentických Dizajnových Vzorov](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->