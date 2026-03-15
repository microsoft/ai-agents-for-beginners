[![Prozkoumání rámců AI agentů](../../../translated_images/cs/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Klikněte na obrázek výše pro zobrazení videa této lekce)_

# Prozkoumejte rámce AI agentů

Rámce pro AI agenty jsou softwarové platformy navržené tak, aby zjednodušily vytváření, nasazení a správu AI agentů. Tyto rámce poskytují vývojářům předpřipravené komponenty, abstrakce a nástroje, které zjednodušují vývoj složitých AI systémů.

Tyto rámce pomáhají vývojářům soustředit se na jedinečné aspekty jejich aplikací tím, že poskytují standardizované přístupy k běžným výzvám při vývoji AI agentů. Zvyšují škálovatelnost, dostupnost a efektivitu při vytváření AI systémů.

## Úvod 

Tato lekce pokryje:

- Co jsou rámce AI agentů a čeho mohou vývojáři dosáhnout?
- Jak mohou týmy tyto rámce využít k rychlému prototypování, iteraci a zlepšování schopností svého agenta?
- Jaké jsou rozdíly mezi rámci a nástroji vytvořenými společností Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> a <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Mohu integrovat své stávající nástroje z Azure ekosystému přímo, nebo potřebuji samostatná řešení?
- Co je Azure AI Agent Service a jak mi to pomáhá?

## Cíle učení

Cíle této lekce jsou vám pomoci porozumět:

- Role rámců AI agentů ve vývoji AI.
- Jak využít rámce AI agentů k vytváření inteligentních agentů.
- Klíčové schopnosti, které rámce AI agentů umožňují.
- Rozdíly mezi Microsoft Agent Framework a Azure AI Agent Service.

## Co jsou rámce AI agentů a co vývojářům umožňují dělat?

Tradiční AI rámce vám mohou pomoci integrovat AI do vašich aplikací a vylepšit tyto aplikace následujícími způsoby:

- **Personalizace**: AI může analyzovat chování a preference uživatelů a poskytovat personalizovaná doporučení, obsah a zkušenosti.
Příklad: Streamingové služby jako Netflix používají AI k doporučování filmů a pořadů na základě historie sledování, čímž zvyšují zapojení a spokojenost uživatelů.
- **Automatizace a efektivita**: AI může automatizovat opakující se úkoly, zjednodušit pracovní postupy a zlepšit provozní efektivitu.
Příklad: Aplikace zákaznické podpory využívají chatboty poháněné AI k řešení běžných dotazů, což zkracuje dobu odezvy a uvolňuje lidské agenty pro složitější problémy.
- **Vylepšená uživatelská zkušenost**: AI může zlepšit celkovou uživatelskou zkušenost tím, že poskytuje inteligentní funkce, jako je rozpoznávání hlasu, zpracování přirozeného jazyka a prediktivní psaní.
Příklad: Virtuální asistenti jako Siri a Google Assistant používají AI k porozumění a reakci na hlasové příkazy, což usnadňuje uživatelům interakci s jejich zařízeními.

### To zní skvěle, tak proč potřebujeme AI Agent Framework?

Rámce pro AI agenty představují něco víc než jen AI frameworky. Jsou navrženy tak, aby umožnily vytváření inteligentních agentů, kteří mohou komunikovat s uživateli, jinými agenty a prostředím za účelem dosažení konkrétních cílů. Tito agenti mohou vykazovat autonomní chování, přijímat rozhodnutí a přizpůsobovat se měnícím se podmínkám. Pojďme se podívat na některé klíčové schopnosti, které rámce AI agentů umožňují:

- **Spolupráce a koordinace agentů**: Umožňují vytváření více AI agentů, kteří mohou spolupracovat, komunikovat a koordinovat se při řešení složitých úkolů.
- **Automatizace a řízení úkolů**: Poskytují mechanismy pro automatizaci vícekrokových pracovních postupů, delegování úkolů a dynamické řízení úkolů mezi agenty.
- **Kontextuální porozumění a adaptace**: Vybavují agenty schopností porozumět kontextu, přizpůsobit se měnícím se podmínkám a přijímat rozhodnutí na základě informací v reálném čase.

Shrnuto, agenti vám umožňují dělat více, posunout automatizaci na vyšší úroveň a vytvářet inteligentnější systémy, které se mohou přizpůsobovat a učit se z jejich prostředí.

## Jak rychle prototypovat, iterovat a zlepšovat schopnosti agenta?

Toto je rychle se vyvíjející oblast, ale existují některé společné prvky napříč většinou rámců AI agentů, které vám mohou pomoci rychle prototypovat a iterovat — konkrétně modulární komponenty, nástroje pro spolupráci a učení v reálném čase. Pojďme se na ně podívat:

- **Používejte modulární komponenty**: AI SDK poskytují předpřipravené komponenty jako AI a paměťové konektory, volání funkcí pomocí přirozeného jazyka nebo pluginů v kódu, šablony promptů a další.
- **Využijte nástroje pro spolupráci**: Navrhujte agenty se specifickými rolemi a úkoly, což jim umožní testovat a zdokonalovat kolaborativní pracovní postupy.
- **Učte se v reálném čase**: Implementujte zpětnovazební smyčky, kde se agenti učí z interakcí a dynamicky upravují své chování.

### Používejte modulární komponenty

SDK jako Microsoft Agent Framework nabízejí předpřipravené komponenty, jako jsou AI konektory, definice nástrojů a řízení agentů.

**Jak to mohou týmy využít**: Týmy mohou rychle sestavit tyto komponenty k vytvoření funkčního prototypu bez nutnosti začínat od nuly, což umožňuje rychlé experimentování a iteraci.

**Jak to funguje v praxi**: Můžete použít předpřipravený parser k extrahování informací z uživatelského vstupu, modul paměti k ukládání a načítání dat a generátor promptů k interakci s uživateli, to vše bez nutnosti vytvářet tyto komponenty od nuly.

**Ukázkový kód**. Podívejme se na příklad, jak můžete použít Microsoft Agent Framework s `AzureAIProjectAgentProvider`, aby model odpovídal na uživatelský vstup s voláním nástrojů:

``` python
# Microsoft Agent Framework Příklad v Pythonu

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# Definujte ukázkovou funkci nástroje pro rezervaci cesty
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
    # Příklad výstupu: Váš let do New Yorku dne 1. ledna 2025 byl úspěšně rezervován. Šťastnou cestu! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Z toho, co vidíte v tomto příkladu, je patrné, jak můžete využít předpřipravený parser k extrahování klíčových informací z uživatelského vstupu, jako je odlet, cíl a datum žádosti o rezervaci letu. Tento modulární přístup vám umožňuje soustředit se na logiku na vyšší úrovni.

### Využijte nástroje pro spolupráci

Rámce jako Microsoft Agent Framework usnadňují vytváření více agentů, kteří mohou spolupracovat.

**Jak to mohou týmy využít**: Týmy mohou navrhovat agenty se specifickými rolemi a úkoly, což jim umožní testovat a zdokonalovat kolaborativní pracovní postupy a zlepšovat celkovou efektivitu systému.

**Jak to funguje v praxi**: Můžete vytvořit tým agentů, kde každý agent má specializovanou funkci, například získávání dat, analýzu nebo rozhodování. Tito agenti mohou komunikovat a sdílet informace, aby dosáhli společného cíle, například odpovědět na dotaz uživatele nebo dokončit úkol.

**Ukázkový kód (Microsoft Agent Framework)**:

```python
# Vytváření více agentů, kteří spolupracují pomocí Microsoft Agent Framework

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Agent pro získávání dat
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Agent pro analýzu dat
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Spouštění agentů sekvenčně na úkolu
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

V předchozím kódu vidíte, jak můžete vytvořit úkol, který zahrnuje více agentů spolupracujících na analýze dat. Každý agent provádí specifickou funkci a úkol je vykonáván koordinací agentů k dosažení požadovaného výsledku. Vytvářením dedikovaných agentů se specializovanými rolemi můžete zlepšit efektivitu a výkon při plnění úkolů.

### Učte se v reálném čase

Pokročilé rámce poskytují schopnosti pro porozumění kontextu a adaptaci v reálném čase.

**Jak to mohou týmy využít**: Týmy mohou implementovat zpětnovazební smyčky, kde se agenti učí z interakcí a dynamicky upravují své chování, což vede k průběžnému zlepšování a zdokonalování schopností.

**Jak to funguje v praxi**: Agenti mohou analyzovat zpětnou vazbu od uživatelů, environmentální data a výsledky úkolů a aktualizovat tak svou znalostní bázi, upravovat algoritmy rozhodování a zlepšovat výkon v čase. Tento iterativní proces učení umožňuje agentům přizpůsobit se měnícím se podmínkám a preferencím uživatelů, čímž zvyšuje celkovou účinnost systému.

## Jaké jsou rozdíly mezi Microsoft Agent Framework a Azure AI Agent Service?

Existuje mnoho způsobů, jak tyto přístupy porovnat, ale pojďme se podívat na některé klíčové rozdíly z hlediska jejich návrhu, schopností a cílových případů použití:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework poskytuje zjednodušené SDK pro vytváření AI agentů pomocí `AzureAIProjectAgentProvider`. Umožňuje vývojářům vytvářet agenty, kteří využívají modely Azure OpenAI s vestavěným voláním nástrojů, správou konverzací a zabezpečením na úrovni podniku prostřednictvím Azure identity.

**Případy použití**: Vytváření produkčně připravených AI agentů s využitím nástrojů, vícekrokových pracovních postupů a scénářů integrace do podnikových prostředí.

Zde jsou některé důležité základní koncepty Microsoft Agent Framework:

- **Agents**. Agent je vytvořen pomocí `AzureAIProjectAgentProvider` a nakonfigurován s názvem, instrukcemi a nástroji. Agent může:
  - **Zpracovávat uživatelské zprávy** a generovat odpovědi pomocí modelů Azure OpenAI.
  - **Volat nástroje** automaticky na základě kontextu konverzace.
  - **Udržovat stav konverzace** napříč více interakcemi.

  Zde je ukázka kódu, která ukazuje, jak vytvořit agenta:

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

- **Tools**. Rámec podporuje definování nástrojů jako Python funkcí, které může agent automaticky volat. Nástroje jsou registrovány při vytváření agenta:

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

- **Koordinace více agentů**. Můžete vytvořit více agentů s různou specializací a koordinovat jejich práci:

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

- **Integrace Azure Identity**. Rámec používá `AzureCliCredential` (nebo `DefaultAzureCredential`) pro zabezpečené přihlášení bez klíčů, čímž eliminuje potřebu spravovat API klíče přímo.

## Azure AI Agent Service

Azure AI Agent Service je novější přírůstek, představený na Microsoft Ignite 2024. Umožňuje vývoj a nasazení AI agentů s flexibilnějšími modely, například přímým voláním open-source LLM jako Llama 3, Mistral a Cohere.

Azure AI Agent Service poskytuje silnější mechanismy zabezpečení pro podniky a metody ukládání dat, díky čemuž je vhodný pro podnikové aplikace.

Funguje zkrátka out-of-the-box s Microsoft Agent Framework pro vytváření a nasazení agentů.

Tato služba je v současnosti ve veřejné ukázce (Public Preview) a podporuje Python a C# pro vytváření agentů.

Pomocí Python SDK služby Azure AI Agent Service můžeme vytvořit agenta s uživatelsky definovaným nástrojem:

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

### Základní koncepty

Azure AI Agent Service má následující základní koncepty:

- **Agent**. Azure AI Agent Service se integruje s Microsoft Foundry. V rámci AI Foundry funguje AI Agent jako "chybná" mikroservisa, která může být použita k odpovídání na dotazy (RAG), provádění akcí nebo úplné automatizaci pracovních postupů. Dosahuje toho kombinováním generativních AI modelů s nástroji, které mu umožňují přistupovat a interagovat se zdroji reálných dat. Zde je příklad agenta:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    V tomto příkladu je agent vytvořen s modelem `gpt-4o-mini`, názvem `my-agent` a instrukcemi `You are helpful agent`. Agent je vybaven nástroji a zdroji pro vykonávání úloh interpretace kódu.

- **Thread and messages**. Thread (vlákno) je dalším důležitým konceptem. Představuje konverzaci nebo interakci mezi agentem a uživatelem. Vlákna lze použít ke sledování průběhu konverzace, ukládání kontextových informací a správě stavu interakce. Zde je příklad vlákna:

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

    V předchozím kódu je vytvořeno vlákno. Poté je do vlákna odeslána zpráva. Zavoláním `create_and_process_run` je agent požádán, aby na vlákně vykonal práci. Nakonec jsou zprávy načteny a zaznamenány, aby bylo vidět odpověď agenta. Zprávy ukazují průběh konverzace mezi uživatelem a agentem. Je také důležité pochopit, že zprávy mohou být různých typů, jako je text, obrázek nebo soubor; to znamená, že práce agentů může mít například za výsledek obrázek nebo textovou odpověď. Jako vývojář pak můžete tyto informace dále zpracovat nebo je zobrazit uživateli.

- **Integrace s Microsoft Agent Framework**. Azure AI Agent Service funguje bezproblémově s Microsoft Agent Framework, což znamená, že můžete agenty vytvářet pomocí `AzureAIProjectAgentProvider` a nasazovat je prostřednictvím Agent Service pro produkční scénáře.

**Případy použití**: Azure AI Agent Service je navržena pro podnikové aplikace, které vyžadují bezpečné, škálovatelné a flexibilní nasazení AI agentů.

## Jaký je rozdíl mezi těmito přístupy?
 
Zní to, jako by existovalo překrytí, ale jsou zde některé klíčové rozdíly z hlediska jejich návrhu, schopností a cílových případů použití:
 
- **Microsoft Agent Framework (MAF)**: Je to produkčně připravené SDK pro vytváření AI agentů. Poskytuje zjednodušené API pro vytváření agentů s voláním nástrojů, správou konverzací a integrací Azure identity.
- **Azure AI Agent Service**: Je to platforma a služba pro nasazení v Azure Foundry určená pro agenty. Nabízí vestavěné připojení k službám jako Azure OpenAI, Azure AI Search, Bing Search a spuštění kódu.
 
Stále si nejste jisti, kterou možnost zvolit?

### Případy použití
 
Pojďme se podívat, jestli vám můžeme pomoci tím, že projdeme některé běžné případy použití:
 
> Q: Vytvářím produkční aplikace s AI agenty a chci začít rychle
>

>A: Microsoft Agent Framework je skvělá volba. Poskytuje jednoduché, Pythonické API přes `AzureAIProjectAgentProvider`, které vám umožní definovat agenty s nástroji a instrukcemi jen v několika řádcích kódu.

>Q: Potřebuji nasazení na podnikové úrovni s integracemi Azure, jako jsou Search a spuštění kódu
>
> A: Azure AI Agent Service je nejlepší volba. Je to platformní služba, která poskytuje vestavěné schopnosti pro více modelů, Azure AI Search, Bing Search a Azure Functions. Umožňuje snadno vytvářet agenty v Foundry Portalu a nasazovat je ve velkém měřítku.
 
> Q: Pořád jsem zmatený, dejte mi prosím jednu možnost
>
> A: Začněte s Microsoft Agent Framework pro vytváření agentů a poté použijte Azure AI Agent Service, když budete potřebovat jejich nasazení a škálování v produkci. Tento přístup vám umožní rychle iterovat na logice agenta a zároveň mít jasnou cestu k podnikovému nasazení.
 
Shrňme klíčové rozdíly v tabulce:

| Rámec | Zaměření | Základní koncepty | Případy použití |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Zjednodušené SDK pro agenty s voláním nástrojů | Agenti, Nástroje, Azure Identity | Vytváření AI agentů, používání nástrojů, vícekrokové pracovní postupy |
| Azure AI Agent Service | Flexibilní modely, podnikové zabezpečení, generování kódu, volání nástrojů | Modularita, Spolupráce, Orchestrace procesů | Bezpečné, škálovatelné a flexibilní nasazení AI agentů |

## Mohu integrovat své stávající nástroje z Azure ekosystému přímo, nebo potřebuji samostatná řešení?
Odpověď zní ano — můžete integrovat své stávající nástroje z ekosystému Azure přímo se službou Azure AI Agent Service, protože byla navržena tak, aby bezproblémově spolupracovala s dalšími službami Azure. Například můžete integrovat Bing, Azure AI Search a Azure Functions. Existuje také hluboká integrace s Microsoft Foundry.

Microsoft Agent Framework se také integruje se službami Azure prostřednictvím `AzureAIProjectAgentProvider` a identity Azure, což vám umožňuje volat služby Azure přímo z vašich nástrojů agenta.

## Ukázkové kódy

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Máte další otázky ohledně rámců AI agentů?

Připojte se k [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), setkejte se s dalšími studenty, zúčastněte se konzultačních hodin a získejte odpovědi na své otázky týkající se AI agentů.

## Odkazy

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Služba Azure AI Agent</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Odpovědi</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Služba Azure AI Agent</a>

## Předchozí lekce

[Úvod do AI agentů a případů použití](../01-intro-to-ai-agents/README.md)

## Následující lekce

[Porozumění agentním návrhovým vzorům](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Prohlášení o vyloučení odpovědnosti:
Tento dokument byl přeložen pomocí AI překladatelské služby Co-op Translator (https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro kritické informace doporučujeme profesionální lidský překlad. Za jakákoli nedorozumění nebo chybné výklady vyplývající z použití tohoto překladu neneseme odpovědnost.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->