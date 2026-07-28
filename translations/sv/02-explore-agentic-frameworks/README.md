[![Utforska AI Agentramverk](../../../translated_images/sv/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Klicka på bilden ovan för att se videon för denna lektion)_

# Utforska AI Agentramverk

AI agentramverk är mjukvaruplattformar utformade för att förenkla skapandet, distributionen och hanteringen av AI-agenter. Dessa ramverk erbjuder utvecklare förbyggda komponenter, abstraktioner och verktyg som effektiviserar utvecklingen av komplexa AI-system.

Dessa ramverk hjälper utvecklare att fokusera på de unika aspekterna av deras applikationer genom att erbjuda standardiserade tillvägagångssätt för vanliga utmaningar inom AI-agentutveckling. De förbättrar skalbarhet, tillgänglighet och effektivitet vid skapandet av AI-system.

## Introduktion

Den här lektionen kommer att täcka:

- Vad är AI Agentramverk och vad möjliggör de för utvecklare?
- Hur kan team använda dessa för att snabbt prototypa, iterera och förbättra sina agenters kapacitet?
- Vad är skillnaderna mellan ramverken och verktygen skapade av Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> och <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Kan jag integrera mina befintliga verktyg i Azure-ekosystemet direkt, eller behöver jag fristående lösningar?
- Vad är Microsoft Foundry Agent Service och hur hjälper det mig?

## Lärandemål

Målen med denna lektion är att hjälpa dig förstå:

- AI Agentramverks roll inom AI-utveckling.
- Hur man utnyttjar AI Agentramverk för att bygga intelligenta agenter.
- Nyckelkapaciteter som möjliggörs av AI Agentramverk.
- Skillnaderna mellan Microsoft Agent Framework och Microsoft Foundry Agent Service.

## Vad är AI Agentramverk och vad möjliggör de för utvecklare?

Traditionella AI-ramverk kan hjälpa dig att integrera AI i dina appar och förbättra dessa appar på följande sätt:

- **Personalisering**: AI kan analysera användarbeteende och preferenser för att erbjuda personliga rekommendationer, innehåll och upplevelser.
Exempel: Streamingtjänster som Netflix använder AI för att föreslå filmer och serier baserat på tittarhistorik, vilket ökar användarengagemang och nöjdhet.
- **Automatisering och effektivitet**: AI kan automatisera repetitiva uppgifter, effektivisera arbetsflöden och förbättra verksamhetens effektivitet.
Exempel: Kundtjänstappar använder AI-drivna chattbotar för att hantera vanliga frågor, vilket minskar svarstider och frigör mänskliga agenter för mer komplexa ärenden.
- **Förbättrad användarupplevelse**: AI kan förbättra den övergripande användarupplevelsen genom att erbjuda intelligenta funktioner som röstigenkänning, naturlig språkbehandling och prediktiv text.
Exempel: Virtuella assistenter som Siri och Google Assistant använder AI för att förstå och svara på röstkommandon, vilket gör det enklare för användare att interagera med sina enheter.

### Det låter ju fantastiskt, men varför behöver vi då AI Agentramverk?

AI Agentramverk representerar något mer än bara AI-ramverk. De är utformade för att möjliggöra skapandet av intelligenta agenter som kan interagera med användare, andra agenter och miljön för att uppnå specifika mål. Dessa agenter kan uppvisa autonomt beteende, fatta beslut och anpassa sig till förändrade förhållanden. Låt oss titta på några viktiga kapaciteter som AI Agentramverk möjliggör:

- **Agent-samarbete och samordning**: Möjliggör skapandet av flera AI-agenter som kan arbeta tillsammans, kommunicera och koordinera för att lösa komplexa uppgifter.
- **Uppgiftsautomatisering och hantering**: Erbjuder mekanismer för att automatisera flerstegsarbetsflöden, delegering av uppgifter och dynamisk uppgiftshantering mellan agenter.
- **Kontextuell förståelse och anpassning**: Utrusta agenter med förmågan att förstå kontext, anpassa sig till förändrade miljöer och fatta beslut baserade på realtidsinformation.

Sammanfattningsvis låter agenter dig göra mer, ta automatiseringen till nästa nivå och skapa mer intelligenta system som kan anpassa sig och lära från sin miljö.

## Hur kan man snabbt prototypa, iterera och förbättra agentens kapacitet?

Detta är ett snabbt föränderligt område, men det finns vissa gemensamma saker i de flesta AI Agentramverk som kan hjälpa dig att snabbt prototypa och iterera, nämligen modulära komponenter, samarbetsverktyg och realtidsinlärning. Låt oss fördjupa oss i dessa:

- **Använd modulära komponenter**: AI SDK:er erbjuder förbyggda komponenter som AI- och minneskopplingar, funktionsanrop via naturligt språk eller kodplugins, promptmallar och mer.
- **Utnyttja samarbetsverktyg**: Designa agenter med specifika roller och uppgifter, vilket gör det möjligt för dem att testa och förbättra samarbetsarbetsflöden.
- **Lär dig i realtid**: Implementera återkopplingsslingor där agenter lär sig av interaktioner och justerar sitt beteende dynamiskt.

### Använd modulära komponenter

SDK:er som Microsoft Agent Framework erbjuder förbyggda komponenter som AI-kopplingar, verktygsdefinitioner och agenthantering.

**Hur team kan använda dessa**: Team kan snabbt sätta ihop dessa komponenter för att skapa en funktionell prototyp utan att börja från början, vilket möjliggör snabb experimentering och iteration.

**Hur det fungerar i praktiken**: Du kan använda en förbyggd parser för att extrahera information från användarinmatning, en minnesmodul för att lagra och hämta data, och en promptgenerator för att interagera med användare, allt utan att behöva bygga dessa komponenter från början.

**Exempelkod**. Låt oss titta på ett exempel på hur du kan använda Microsoft Agent Framework med `FoundryChatClient` för att få modellen att svara på användarinmatning med verktygsanrop:

``` python
# Microsoft Agent Framework Python Exempel

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Definiera en exempelverktygsfunktion för att boka resor
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
    # Exempelutskrift: Din flygning till New York den 1 januari 2025 har bokats framgångsrikt. Trevlig resa! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Vad du kan se i detta exempel är hur du kan utnyttja en förbyggd parser för att extrahera nyckelinformation från användarinmatning, såsom ursprung, destination och datum för en flygbokningsförfrågan. Detta modulära tillvägagångssätt låter dig fokusera på den övergripande logiken.

### Utnyttja samarbetsverktyg

Ramverk som Microsoft Agent Framework underlättar skapandet av flera agenter som kan arbeta tillsammans.

**Hur team kan använda dessa**: Team kan designa agenter med specifika roller och uppgifter, vilket gör det möjligt för dem att testa och förbättra samarbetsarbetsflöden och förbättra systemets totala effektivitet.

**Hur det fungerar i praktiken**: Du kan skapa ett team av agenter där varje agent har en specialiserad funktion, såsom datainsamling, analys eller beslutsfattande. Dessa agenter kan kommunicera och dela information för att nå ett gemensamt mål, som att besvara en användarfråga eller slutföra en uppgift.

**Exempelkod (Microsoft Agent Framework)**:

```python
# Skapar flera agenter som arbetar tillsammans med Microsoft Agent Framework

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Datahämtningagent
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Dataanalysagent
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Kör agenter i följd på en uppgift
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Det du ser i föregående kod är hur du kan skapa en uppgift som involverar flera agenter som samarbetar för att analysera data. Varje agent utför en specifik funktion, och uppgiften genomförs genom att koordinera agenterna för att nå önskat resultat. Genom att skapa dedikerade agenter med specialiserade roller kan du förbättra uppgiftens effektivitet och prestanda.

### Lär i realtid

Avancerade ramverk erbjuder kapaciteter för kontextförståelse och anpassning i realtid.

**Hur team kan använda dessa**: Team kan implementera återkopplingsslingor där agenter lär sig från interaktioner och dynamiskt anpassar sitt beteende, vilket leder till kontinuerlig förbättring och förfining av kapaciteter.

**Hur det fungerar i praktiken**: Agenter kan analysera användarfeedback, miljödata och uppgiftsresultat för att uppdatera sin kunskapsbas, justera beslutalgoritmer och förbättra prestanda över tid. Denna iterativa inlärningsprocess möjliggör för agenter att anpassa sig till förändrade förhållanden och användarpreferenser, vilket förbättrar systemets totala effektivitet.

## Vad är skillnaderna mellan Microsoft Agent Framework och Microsoft Foundry Agent Service?

Det finns många sätt att jämföra dessa tillvägagångssätt, men låt oss titta på några viktiga skillnader vad gäller design, kapaciteter och målgruppsanvändningsområden:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework erbjuder ett strömlinjeformat SDK för att bygga AI-agenter med `FoundryChatClient`. Det möjliggör för utvecklare att skapa agenter som använder Azure OpenAI-modeller med inbyggd verktygsanrop, konversationshantering och företagsklassad säkerhet via Azure-identitet.

**Användningsområden**: Bygga produktionsfärdiga AI-agenter med verktygsanvändning, flerstegsarbetsflöden och företagsintegrationsscenarier.

Här är några viktiga kärnbegrepp i Microsoft Agent Framework:

- **Agenter**. En agent skapas via `FoundryChatClient` och konfigureras med ett namn, instruktioner och verktyg. Agenten kan:
  - **Bearbeta användarmeddelanden** och generera svar med Azure OpenAI-modeller.
  - **Automatiskt anropa verktyg** baserat på konversationskontext.
  - **Upprätthålla konversationsstatus** över flera interaktioner.

  Här är en kodsnutt som visar hur man skapar en agent:

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

- **Verktyg**. Ramverket stödjer att definiera verktyg som Python-funktioner som agenten kan anropa automatiskt. Verktyg registreras när agenten skapas:

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

- **Samordning av flera agenter**. Du kan skapa flera agenter med olika specialiseringar och samordna deras arbete:

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

- **Azure Identity-integration**. Ramverket använder `AzureCliCredential` (eller `DefaultAzureCredential`) för säker, nyckellös autentisering, vilket eliminerar behovet av att hantera API-nycklar direkt.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service är ett nyare tillskott, introducerat på Microsoft Ignite 2024. Det möjliggör utveckling och distribution av AI-agenter med mer flexibla modeller, såsom direkt anrop till open-source LLM:er som Llama 3, Mistral och Cohere.

Microsoft Foundry Agent Service erbjuder starkare företagsäkerhetsmekanismer och datalagringsmetoder, vilket gör det lämpligt för företagsapplikationer.

Det fungerar direkt tillsammans med Microsoft Agent Framework för att bygga och distribuera agenter.

Tjänsten är för närvarande i publik förhandsgranskning och stödjer Python och C# för att bygga agenter.

Med Microsoft Foundry Agent Service Python SDK kan vi skapa en agent med ett användardefinierat verktyg:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Definiera verktygsfunktioner
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

### Kärnbegrepp

Microsoft Foundry Agent Service har följande kärnbegrepp:

- **Agent**. Microsoft Foundry Agent Service integreras med Microsoft Foundry. Inom Microsoft Foundry fungerar en AI Agent som en "smart" mikrotjänst som kan användas för att svara på frågor (RAG), utföra åtgärder eller helt automatisera arbetsflöden. Det uppnås genom att kombinera kraften i generativa AI-modeller med verktyg som låter den få tillgång till och interagera med verkliga datakällor. Här är ett exempel på en agent:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    I detta exempel skapas en agent med modellen `gpt-5-mini`, namnet `my-agent` och instruktionen `You are helpful agent`. Agenten utrustas med verktyg och resurser för att utföra kodtolkningsuppgifter.

- **Tråd och meddelanden**. Tråden är ett annat viktigt begrepp. Den representerar en konversation eller interaktion mellan en agent och en användare. Trådar kan användas för att följa konversationens förlopp, lagra kontextinformation och hantera interaktionens status. Här är ett exempel på en tråd:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Be agenten utföra arbete på tråden
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Hämta och logga alla meddelanden för att se agentens svar
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    I den föregående koden skapas en tråd. Därefter skickas ett meddelande till tråden. Genom att kalla på `create_and_process_run` uppmanas agenten att utföra arbete på tråden. Slutligen hämtas och loggas meddelandena för att se agentens svar. Meddelandena indikerar konversationens framsteg mellan användaren och agenten. Det är också viktigt att förstå att meddelandena kan vara av olika typer, såsom text, bild eller fil, vilket innebär att agentens arbete har resulterat i till exempel en bild eller ett textsvar. Som utvecklare kan du då använda denna information för att vidare bearbeta svaret eller presentera det för användaren.

- **Integrerar med Microsoft Agent Framework**. Microsoft Foundry Agent Service fungerar sömlöst med Microsoft Agent Framework, vilket innebär att du kan bygga agenter med `FoundryChatClient` och distribuera dem via Agent Service för produktionsscenarier.

**Användningsområden**: Microsoft Foundry Agent Service är utformad för företagsapplikationer som kräver säker, skalbar och flexibel AI-agentdistribution.

## Vad är skillnaden mellan dessa tillvägagångssätt?
 
Det låter som att det finns överlapp, men det finns några viktiga skillnader vad gäller design, kapaciteter och målgruppsanvändningsområden:
 
- **Microsoft Agent Framework (MAF)**: Är ett produktionsklart SDK för att bygga AI-agenter. Det erbjuder ett strömlinjeformat API för att skapa agenter med verktygsanrop, konversationshantering och Azure-identitetsintegration.
- **Microsoft Foundry Agent Service**: Är en plattform och distributionstjänst i Microsoft Foundry för agenter. Den erbjuder inbyggd anslutning till tjänster som Azure OpenAI, Azure AI Search, Bing Search och kodexekvering.
 
Är du fortfarande osäker på vilken du ska välja?

### Användningsområden
 
Låt oss se om vi kan hjälpa dig genom att gå igenom några vanliga användningsområden:
 
> F: Jag bygger produktionsfärdiga AI-agentapplikationer och vill komma igång snabbt
>

>S: Microsoft Agent Framework är ett utmärkt val. Det erbjuder ett enkelt, Python-likt API via `FoundryChatClient` som låter dig definiera agenter med verktyg och instruktioner på bara några rader kod.

>F: Jag behöver företagsklassad distribution med Azure-integrationer som Search och kodexekvering
>
> S: Microsoft Foundry Agent Service passar bäst. Det är en plattformstjänst som erbjuder inbyggda kapaciteter för flera modeller, Azure AI Search, Bing Search och Azure Functions. Det gör det enkelt att bygga dina agenter i Foundry Portalen och distribuera dem i stor skala.
 
> F: Jag är fortfarande förvirrad, ge mig bara ett alternativ
>
> S: Börja med Microsoft Agent Framework för att bygga dina agenter, och använd sedan Microsoft Foundry Agent Service när du behöver distribuera och skala dem i produktion. Denna strategi låter dig iterera snabbt på din agentlogik samtidigt som du har en tydlig väg till företagsdistribution.
 
Låt oss sammanfatta de viktigaste skillnaderna i en tabell:

| Ramverk | Fokus | Kärnbegrepp | Användningsområden |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Strömlinjeformat agent-SDK med verktygsanrop | Agenter, Verktyg, Azure-Identitet | Bygga AI-agenter, verktygsanvändning, flerstegsarbetsflöden |
| Microsoft Foundry Agent Service | Flexibla modeller, företagsäkerhet, kodgenerering, verktygsanrop | Modularitet, Samarbete, Processorkestrering | Säker, skalbar och flexibel AI-agentdistribution |

## Kan jag integrera mina befintliga verktyg i Azure-ekosystemet direkt, eller behöver jag fristående lösningar?


Svaret är ja, du kan integrera dina befintliga Azure-ekosystemverktyg direkt med Microsoft Foundry Agent Service, särskilt eftersom det har byggts för att fungera sömlöst med andra Azure-tjänster. Du kan till exempel integrera Bing, Azure AI Search och Azure Functions. Det finns också djup integration med Microsoft Foundry.

Microsoft Agent Framework integreras också med Azure-tjänster via `FoundryChatClient` och Azure-identifiering, vilket låter dig anropa Azure-tjänster direkt från dina agentverktyg.

## Exempel på kod

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Fler frågor om AI Agent Frameworks?

Gå med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) för att träffa andra lärande, delta i kontorstid och få dina frågor om AI-agenter besvarade.

## Referenser

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Föregående lektion

[Introduktion till AI-agenter och agentanvändningsfall](../01-intro-to-ai-agents/README.md)

## Nästa lektion

[Förstå agentiska designmönster](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->