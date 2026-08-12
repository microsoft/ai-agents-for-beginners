[![Prozkoumávání rámců AI agentů](../../../translated_images/cs/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Klikněte na obrázek výše pro zhlédnutí videa této lekce)_

# Prozkoumejte rámce AI agentů

Rámce AI agentů jsou softwarové platformy navržené ke zjednodušení tvorby, nasazení a správy AI agentů. Tyto rámce poskytují vývojářům předem připravené komponenty, abstrakce a nástroje, které zjednodušují vývoj složitých AI systémů.

Tyto rámce pomáhají vývojářům soustředit se na jedinečné aspekty jejich aplikací tím, že poskytují standardizované přístupy ke společným výzvám ve vývoji AI agentů. Zvyšují škálovatelnost, přístupnost a efektivitu při vytváření AI systémů.

## Úvod

Tato lekce pokryje:

- Co jsou rámce AI agentů a co umožňují vývojářům dosáhnout?
- Jak mohou týmy rychle prototypovat, iterovat a zlepšovat schopnosti svých agentů?
- Jaké jsou rozdíly mezi rámci a nástroji vytvořenými Microsoftem (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> a <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Mohu integrovat své stávající nástroje Azure ekosystému přímo, nebo potřebuji samostatná řešení?
- Co je Microsoft Foundry Agent Service a jak mi pomáhá?

## Cíle učení

Cílem této lekce je pomoci vám porozumět:

- Role rámců AI agentů ve vývoji AI.
- Jak využít rámce AI agentů k vytvoření inteligentních agentů.
- Klíčové schopnosti umožněné rámci AI agentů.
- Rozdíly mezi Microsoft Agent Framework a Microsoft Foundry Agent Service.

## Co jsou rámce AI agentů a co umožňují vývojářům dělat?

Tradiční AI rámce vám mohou pomoci integrovat AI do vašich aplikací a zlepšit tyto aplikace následujícími způsoby:

- **Personalizace**: AI může analyzovat uživatelské chování a preference, aby poskytla personalizovaná doporučení, obsah a zážitky.
Příklad: Streamovací služby jako Netflix používají AI k navrhování filmů a pořadů na základě historie sledování, což zvyšuje angažovanost a spokojenost uživatelů.
- **Automatizace a efektivita**: AI může automatizovat opakující se úkoly, zefektivnit pracovní procesy a zlepšit provozní efektivitu.
Příklad: Aplikace zákaznické podpory používají AI chatboty k odbavování běžných dotazů, čímž snižují dobu odezvy a uvolňují lidské agenty pro složitější záležitosti.
- **Vylepšený uživatelský zážitek**: AI může zlepšit celkový uživatelský zážitek poskytnutím inteligentních funkcí jako rozpoznávání hlasu, zpracování přirozeného jazyka a prediktivní text.
Příklad: Virtuální asistenti jako Siri a Google Assistant používají AI k pochopení a reakci na hlasové příkazy, což usnadňuje uživatelům interakci s jejich zařízeními.

### To zní skvěle, tak proč tedy potřebujeme AI Agent Framework?

Rámce AI agentů představují něco víc než jen AI rámce. Jsou navrženy pro tvorbu inteligentních agentů, kteří mohou komunikovat s uživateli, jinými agenty a prostředím, aby dosáhli konkrétních cílů. Tito agenti mohou vykazovat autonomní chování, přijímat rozhodnutí a přizpůsobovat se měnícím se podmínkám. Podívejme se na některé klíčové schopnosti umožněné rámci AI agentů:

- **Spolupráce a koordinace agentů**: Umožňují tvorbu více AI agentů, kteří mohou spolupracovat, komunikovat a koordinovat se k řešení složitých úkolů.
- **Automatizace a řízení úkolů**: Poskytují mechanismy pro automatizaci vícestupňových pracovních postupů, delegování úkolů a dynamické řízení úkolů mezi agenty.
- **Kontextuální porozumění a adaptace**: Vybavují agenty schopností rozumět kontextu, přizpůsobovat se měnícím se prostředím a rozhodovat na základě informací v reálném čase.

Shrnutě, agenti vám umožňují dělat více, posouvat automatizaci na další úroveň a vytvářet inteligentnější systémy, které se umí přizpůsobovat a učit ze svého okolí.

## Jak rychle prototypovat, iterovat a zlepšovat schopnosti agenta?

Toto je rychle se vyvíjející oblast, ale existují některé společné prvky napříč většinou rámců AI agentů, které vám mohou pomoci rychle prototypovat a iterovat, a to zejména modulární komponenty, kolaborativní nástroje a učení v reálném čase. Pojďme se na ně podívat blíže:

- **Používejte modulární komponenty**: AI SDK nabízejí předem připravené komponenty jako AI a paměťové konektory, volání funkcí pomocí přirozeného jazyka nebo pluginy kódu, šablony promptů a další.
- **Využívejte kolaborativní nástroje**: Navrhujte agenty se specifickými rolemi a úkoly, umožňující jim testovat a zdokonalovat spolupracující pracovní postupy.
- **Učte se v reálném čase**: Implementujte zpětné vazby, kde se agenti učí z interakcí a dynamicky upravují své chování.

### Používejte modulární komponenty

SDK jako Microsoft Agent Framework nabízí předem připravené komponenty jako AI konektory, definice nástrojů a správu agentů.

**Jak to mohou týmy využít**: Týmy mohou rychle sestavit tyto komponenty k vytvoření funkčního prototypu bez nutnosti začínat od nuly, což umožňuje rychlé experimentování a iterace.

**Jak to funguje v praxi**: Můžete použít předem připravený parser pro extrakci informací z uživatelského vstupu, paměťový modul pro ukládání a vyhledávání dat a generátor promptů pro interakci s uživateli, vše bez nutnosti vytvářet tyto komponenty od začátku.

**Příklad kódu**. Podívejme se na příklad, jak můžete použít Microsoft Agent Framework s `FoundryChatClient`, aby model reagoval na uživatelský vstup s voláním nástrojů:

``` python
# Microsoft Agent Framework Příklad v Pythonu

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Definujte vzorovou funkci nástroje pro rezervaci cesty
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
    # Příklad výstupu: Váš let do New Yorku dne 1. ledna 2025 byl úspěšně rezervován. Šťastnou cestu! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Z tohoto příkladu můžete vidět, jak můžete využít předem připravený parser k extrahování klíčových informací z uživatelského vstupu, jako jsou místo začátku, cílová destinace a datum požadavku na rezervaci letenky. Tento modulární přístup vám umožňuje soustředit se na logiku na vyšší úrovni.

### Využívejte kolaborativní nástroje

Rámce jako Microsoft Agent Framework usnadňují tvorbu více agentů, kteří mohou spolupracovat.

**Jak to mohou týmy využít**: Týmy mohou navrhovat agenty se specifickými rolemi a úkoly, umožňující testovat a zdokonalovat spolupracující pracovní postupy a zvyšovat celkovou efektivitu systému.

**Jak to funguje v praxi**: Můžete vytvořit tým agentů, kdy každý agent má specializovanou funkci, jako je získávání dat, analýza nebo rozhodování. Tito agenti mohou komunikovat a sdílet informace, aby dosáhli společného cíle, například odpovědi na uživatelský dotaz nebo dokončení úkolu.

**Příklad kódu (Microsoft Agent Framework)**:

```python
# Vytváření více agentů, kteří spolupracují pomocí Microsoft Agent Framework

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Agent pro získávání dat
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Agent pro analýzu dat
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Spouštění agentů postupně na úkolu
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

V předchozím kódu vidíte, jak vytvořit úkol, který vyžaduje spolupráci více agentů při analýze dat. Každý agent vykonává specifickou funkci a úkol je prováděn koordinací agentů s cílem dosáhnout požadovaného výsledku. Vytvářením dedikovaných agentů se specializovanými rolemi můžete zlepšit efektivitu a výkon úkolu.

### Učte se v reálném čase

Pokročilé rámce poskytují schopnosti pro porozumění kontextu a adaptaci v reálném čase.

**Jak to mohou týmy využít**: Týmy mohou implementovat zpětné smyčky, kde se agenti učí z interakcí a dynamicky upravují své chování, což vede k průběžnému zlepšování a zdokonalování schopností.

**Jak to funguje v praxi**: Agenti mohou analyzovat uživatelskou zpětnou vazbu, data z prostředí a výsledky úkolů, aby aktualizovali svou znalostní bázi, upravovali rozhodovací algoritmy a zlepšovali výkon v průběhu času. Tento iterativní proces učení umožňuje agentům přizpůsobovat se měnícím se podmínkám a preferencím uživatelů, což zvyšuje celkovou efektivitu systému.

## Jaké jsou rozdíly mezi Microsoft Agent Framework a Microsoft Foundry Agent Service?

Existuje mnoho způsobů, jak tyto přístupy porovnat, ale pojďme se podívat na některé klíčové rozdíly z hlediska jejich designu, schopností a cílových použití:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework poskytuje zjednodušené SDK pro vytváření AI agentů pomocí `FoundryChatClient`. Umožňuje vývojářům vytvářet agenty, kteří využívají Azure OpenAI modely s vestavěným voláním nástrojů, správou konverzace a bezpečností na úrovni podniku díky Azure identitě.

**Použití**: Vytváření produkčně připravených AI agentů s využitím nástrojů, vícestupňových pracovních postupů a scénářů integrace do podniku.

Zde jsou některé důležité základní koncepty Microsoft Agent Framework:

- **Agenti**. Agent je vytvořen pomocí `FoundryChatClient` a nakonfigurován s názvem, instrukcemi a nástroji. Agent může:
  - **Zpracovávat uživatelské zprávy** a generovat odpovědi pomocí Azure OpenAI modelů.
  - **Automaticky volat nástroje** na základě kontextu konverzace.
  - **Udržovat stav konverzace** přes více interakcí.

  Zde je úryvek kódu ukazující, jak vytvořit agenta:

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

- **Nástroje**. Rámec podporuje definování nástrojů jako Python funkcí, které může agent automaticky vyvolat. Nástroje jsou registrovány při vytváření agenta:

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

- **Koordinace více agentů**. Můžete vytvořit více agentů se specializacemi a koordinovat jejich práci:

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

- **Integrace Azure identity**. Rámec využívá `AzureCliCredential` (nebo `DefaultAzureCredential`) pro zabezpečené přihlašování bez klíčů, což eliminuje potřebu spravovat API klíče přímo.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service je novější služba, představena na Microsoft Ignite 2024. Umožňuje vývoj a nasazení AI agentů s flexibilnějšími modely, například přímým voláním open-source LLM jako Llama 3, Mistral a Cohere.

Microsoft Foundry Agent Service nabízí silnější bezpečnostní mechanismy na úrovni podniku a metody ukládání dat, což jej činí vhodným pro podnikové aplikace.

Funguje bez problémů s Microsoft Agent Frameworkem pro tvorbu a nasazení agentů.

Tato služba je momentálně v Public Preview a podporuje Python a C# pro tvorbu agentů.

Pomocí Python SDK Microsoft Foundry Agent Service můžeme vytvořit agenta s uživatelsky definovaným nástrojem:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Definujte funkce nástroje
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

### Základní koncepty

Microsoft Foundry Agent Service má následující základní koncepty:

- **Agent**. Microsoft Foundry Agent Service se integruje s Microsoft Foundry. V Microsoft Foundry funguje AI Agent jako „chytrá“ mikroslužba, která může odpovídat na otázky (RAG), vykonávat akce nebo zcela automatizovat pracovní postupy. Dosahuje toho kombinací síly generativních AI modelů s nástroji, které mu umožňují přistupovat k reálným datovým zdrojům a pracovat s nimi. Zde je příklad agenta:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    V tomto příkladu je agent vytvořen s modelem `gpt-5-mini`, názvem `my-agent` a instrukcí `You are helpful agent`. Agent je vybaven nástroji a zdroji k vykonávání úloh interpretace kódu.

- **Vlákno a zprávy**. Vlákno je další důležitý koncept. Reprezentuje konverzaci nebo interakci mezi agentem a uživatelem. Vlákna mohou být použita k sledování průběhu konverzace, uložení kontextových informací a správě stavu interakce. Zde je příklad vlákna:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Požádejte agenta, aby vykonal práci na vlákně
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Získejte a zaznamenejte všechny zprávy, abyste viděli odpověď agenta
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    V předchozím kódu je vytvořeno vlákno. Následně je odeslána zpráva do vlákna. Voláním `create_and_process_run` je agent požádán, aby provedl práci ve vlákně. Nakonec jsou zprávy získány a zaznamenány, abychom viděli odpověď agenta. Zprávy ukazují průběh konverzace mezi uživatelem a agentem. Je také důležité pochopit, že zprávy mohou být různého typu, například text, obrázek nebo soubor, což znamená, že práce agenta mohla například vygenerovat obrázek nebo textovou odpověď. Vývojář pak může tyto informace použít k dalšímu zpracování odpovědi nebo její prezentaci uživateli.

- **Integrace s Microsoft Agent Framework**. Microsoft Foundry Agent Service funguje bezproblémově s Microsoft Agent Frameworkem, což znamená, že můžete tvořit agenty pomocí `FoundryChatClient` a nasazovat je přes Agent Service pro produkční scénáře.

**Použití**: Microsoft Foundry Agent Service je navržen pro podnikové aplikace vyžadující bezpečné, škálovatelné a flexibilní nasazení AI agentů.

## Jaký je rozdíl mezi těmito přístupy?
 
Zdá se, že se částečně překrývají, ale existují klíčové rozdíly v designu, schopnostech a cílových použitích:
 
- **Microsoft Agent Framework (MAF)**: Je produkčně připravené SDK pro tvorbu AI agentů. Poskytuje zjednodušené API pro vytváření agentů s voláním nástrojů, správou konverzace a integrací Azure identity.
- **Microsoft Foundry Agent Service**: Je platforma a nasazovací služba v Microsoft Foundry pro agenty. Nabízí zabudované propojení se službami jako Azure OpenAI, Azure AI Search, Bing Search a spouštění kódu.
 
Stále si nejste jisti, kterou zvolit?

### Použití
 
Podívejme se, jestli vám můžeme pomoci s běžnými scénáři použití:
 
> Q: Vytvářím produkční AI agentní aplikace a chci začít rychle
>

>A: Microsoft Agent Framework je skvělá volba. Poskytuje jednoduché, pythonické API přes `FoundryChatClient`, které vám umožní definovat agenty s nástroji a instrukcemi v několika řádcích kódu.

>Q: Potřebuji nasazení na podnikové úrovni s integrací Azure jako Search a spouštění kódu
>
> A: Microsoft Foundry Agent Service je nejlepší volba. Je to platformní služba, která nabízí vestavěné schopnosti pro více modelů, Azure AI Search, Bing Search a Azure Functions. Umožňuje snadno tvořit agenty v portálu Foundry a nasazovat je ve velkém.
 
> Q: Jsem stále zmatený, stačí mi jedna možnost
>
> A: Začněte s Microsoft Agent Framework k vytvoření svých agentů a poté použijte Microsoft Foundry Agent Service, když je potřeba je nasadit a škálovat v produkci. Tento přístup vám umožňuje rychle iterovat na logice agenta a zároveň mít jasnou cestu k podnikové produkci.
 
Shrňme klíčové rozdíly v tabulce:

| Framework | Zaměření | Základní koncepty | Použití |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Zjednodušené SDK agentů s voláním nástrojů | Agenti, Nástroje, Azure identita | Vývoj AI agentů, použití nástrojů, vícestupňové workflow |
| Microsoft Foundry Agent Service | Flexibilní modely, podniková bezpečnost, generování kódu, volání nástrojů | Modularita, Spolupráce, Orchestrace procesů | Bezpečné, škálovatelné a flexibilní nasazení AI agentů |

## Mohu integrovat své stávající nástroje Azure ekosystému přímo, nebo potřebuji samostatná řešení?


Odpověď zní ano, můžete integrovat vaše stávající nástroje z Azure ekosystému přímo s Microsoft Foundry Agent Service, zejména protože byl navržen tak, aby bezproblémově spolupracoval s dalšími službami Azure. Můžete například integrovat Bing, Azure AI Search a Azure Functions. Existuje také hluboká integrace s Microsoft Foundry.

Microsoft Agent Framework se také integruje se službami Azure prostřednictvím `FoundryChatClient` a identity Azure, což vám umožňuje volat služby Azure přímo z vašich agentních nástrojů.

## Ukázkové kódy

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Máte další otázky ohledně AI Agent Frameworků?

Připojte se k [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) a setkejte se s dalšími zájemci, navštěvujte konzultační hodiny a získejte odpovědi na své otázky ohledně AI agentů.

## Reference

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Předchozí lekce

[Úvod do AI agentů a případů užití agentů](../01-intro-to-ai-agents/README.md)

## Další lekce

[Pochopení agentních návrhových vzorů](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->