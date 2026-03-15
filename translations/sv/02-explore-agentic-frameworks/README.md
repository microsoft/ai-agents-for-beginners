[![Utforska AI-agentramverk](../../../translated_images/sv/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Klicka på bilden ovan för att se videon av denna lektion)_

# Utforska AI-agentramverk

AI-agentramverk är programvaruplattformar utformade för att förenkla skapandet, driftsättningen och hanteringen av AI-agenter. Dessa ramverk förser utvecklare med färdiga komponenter, abstraktioner och verktyg som effektiviserar utvecklingen av komplexa AI-system.

Dessa ramverk hjälper utvecklare att fokusera på de unika aspekterna av sina applikationer genom att erbjuda standardiserade tillvägagångssätt för vanliga utmaningar i utvecklingen av AI-agenter. De förbättrar skalbarhet, tillgänglighet och effektivitet vid byggandet av AI-system.

## Introduktion 

Denna lektion kommer att täcka:

- Vad är AI-agentramverk och vad möjliggör de för utvecklare?
- Hur kan team använda dessa för att snabbt prototypa, iterera och förbättra sina agenters förmågor?
- Vad är skillnaderna mellan ramverken och verktygen skapade av Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> och <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Kan jag integrera mina befintliga Azure-ekosystemverktyg direkt, eller behöver jag fristående lösningar?
- Vad är Azure AI Agents service och hur hjälper det mig?

## Lärandemål

Målen med denna lektion är att hjälpa dig förstå:

- Agentramverks roll i AI-utveckling.
- Hur man utnyttjar AI-agentramverk för att bygga intelligenta agenter.
- Nyckelfunktioner som möjliggörs av AI-agentramverk.
- Skillnaderna mellan Microsoft Agent Framework och Azure AI Agent Service.

## Vad är AI-agentramverk och vad möjliggör de för utvecklare?

Traditionella AI-ramverk kan hjälpa dig att integrera AI i dina appar och göra dessa appar bättre på följande sätt:

- **Personalisering**: AI kan analysera användarbeteende och preferenser för att erbjuda personliga rekommendationer, innehåll och upplevelser.
Exempel: Streamingtjänster som Netflix använder AI för att föreslå filmer och serier baserat på visningshistorik, vilket ökar användarengagemang och tillfredsställelse.
- **Automatisering och effektivitet**: AI kan automatisera repetitiva uppgifter, effektivisera arbetsflöden och förbättra operationell effektivitet.
Exempel: Kundtjänstappar använder AI-drivna chattbotar för att hantera vanliga förfrågningar, minska svarstider och frigöra mänskliga agenter för mer komplexa ärenden.
- **Förbättrad användarupplevelse**: AI kan förbättra den övergripande användarupplevelsen genom att tillhandahålla intelligenta funktioner som röstigenkänning, naturlig språkbehandling och prediktiv text.
Exempel: Virtuella assistenter som Siri och Google Assistant använder AI för att förstå och svara på röstkommandon, vilket gör det enklare för användare att interagera med sina enheter.

### Det låter bra, men varför behöver vi AI Agent Framework?

AI-agentramverk representerar något mer än bara AI-ramverk. De är utformade för att möjliggöra skapandet av intelligenta agenter som kan interagera med användare, andra agenter och miljön för att uppnå specifika mål. Dessa agenter kan uppvisa autonomt beteende, fatta beslut och anpassa sig till förändrade förhållanden. Här är några nyckelfunktioner som AI-agentramverk möjliggör:

- **Agent-samarbete och koordinering**: Möjliggör skapandet av flera AI-agenter som kan arbeta tillsammans, kommunicera och koordinera för att lösa komplexa uppgifter.
- **Uppgiftsautomatisering och hantering**: Erbjuder mekanismer för att automatisera flerstegsarbetsflöden, uppgiftsdelegering och dynamisk uppgiftshantering mellan agenter.
- **Kontextuell förståelse och anpassning**: Utrusta agenter med förmågan att förstå kontext, anpassa sig till förändrade miljöer och fatta beslut baserat på realtidsinformation.

Sammanfattningsvis gör agenter att du kan göra mer, ta automatisering till nästa nivå och skapa mer intelligenta system som kan anpassa sig och lära av sin omgivning.

## Hur kan man snabbt prototypa, iterera och förbättra agentens förmågor?

Detta är ett snabbt föränderligt landskap, men det finns några saker som är vanliga över de flesta AI-agentramverk som kan hjälpa dig att snabbt prototypa och iterera, nämligen modulära komponenter, samarbetsverktyg och realtidsinlärning. Låt oss fördjupa oss i dessa:

- **Använd modulära komponenter**: AI-SDK:er erbjuder färdiga komponenter såsom AI- och minneskopplingar, funktionsanrop med naturligt språk eller kod-plugins, promptmallar och mer.
- **Utnyttja samarbetsverktyg**: Designa agenter med specifika roller och uppgifter, så att de kan testa och förfina samarbetsarbetsflöden.
- **Lär i realtid**: Implementera feedbackloopar där agenter lär sig från interaktioner och justerar sitt beteende dynamiskt.

### Använd modulära komponenter

SDK:er som Microsoft Agent Framework erbjuder färdiga komponenter såsom AI-anslutningar, verktygsdefinitioner och agenthantering.

**Hur team kan använda dessa**: Team kan snabbt sätta ihop dessa komponenter för att skapa en funktionell prototyp utan att börja från början, vilket möjliggör snabb experimentering och iteration.

**Hur det fungerar i praktiken**: Du kan använda en förbyggd parser för att extrahera information från användarinmatning, en minnesmodul för att lagra och hämta data, och en promptgenerator för att interagera med användare, allt utan att behöva bygga dessa komponenter från grunden.

**Exempel på kod**. Låt oss titta på ett exempel på hur du kan använda Microsoft Agent Framework med `AzureAIProjectAgentProvider` för att få modellen att svara på användarinmatning med verktygsanrop:

``` python
# Microsoft Agent Framework Python-exempel

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# Definiera en exempelverktygsfunktion för att boka resa
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
    # Exempelutdata: Din flygning till New York den 1 januari 2025 har bokats framgångsrikt. Trevlig resa! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Vad du kan se från detta exempel är hur du kan utnyttja en förbyggd parser för att extrahera nyckelinformation från användarinmatning, såsom avreseort, destination och datum för en flygbokningsförfrågan. Detta modulära tillvägagångssätt låter dig fokusera på den övergripande logiken.

### Utnyttja samarbetsverktyg

Ramverk som Microsoft Agent Framework underlättar skapandet av flera agenter som kan arbeta tillsammans.

**Hur team kan använda dessa**: Team kan designa agenter med specifika roller och uppgifter, vilket gör det möjligt att testa och förfina samarbetsarbetsflöden och förbättra den övergripande systemeffektiviteten.

**Hur det fungerar i praktiken**: Du kan skapa ett team av agenter där varje agent har en specialiserad funktion, såsom datahämtning, analys eller beslutsfattande. Dessa agenter kan kommunicera och dela information för att uppnå ett gemensamt mål, till exempel besvara en användarfråga eller slutföra en uppgift.

**Exempel på kod (Microsoft Agent Framework)**:

```python
# Skapa flera agenter som arbetar tillsammans med Microsoft Agent Framework

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Dataåtervinningsagent
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Dataanalysagent
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Kör agenter i följd på en uppgift
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Vad du ser i föregående kod är hur du kan skapa en uppgift som involverar flera agenter som arbetar tillsammans för att analysera data. Varje agent utför en specifik funktion, och uppgiften genomförs genom att koordinera agenterna för att uppnå önskat resultat. Genom att skapa dedikerade agenter med specialiserade roller kan du förbättra uppgiftens effektivitet och prestanda.

### Lär i realtid

Avancerade ramverk tillhandahåller möjligheter för realtidsförståelse av kontext och anpassning.

**Hur team kan använda dessa**: Team kan implementera feedbackloopar där agenter lär sig från interaktioner och justerar sitt beteende dynamiskt, vilket leder till kontinuerlig förbättring och förfining av förmågorna.

**Hur det fungerar i praktiken**: Agenter kan analysera användarfeedback, miljödata och uppgiftsresultat för att uppdatera sin kunskapsbas, justera beslutsalgoritmer och förbättra prestandan över tid. Denna iterativa inlärningsprocess gör att agenter kan anpassa sig till förändrade förhållanden och användarpreferenser, vilket förbättrar systemets effektivitet.

## Vad är skillnaderna mellan Microsoft Agent Framework och Azure AI Agent Service?

Det finns många sätt att jämföra dessa tillvägagångssätt, men låt oss titta på några viktiga skillnader när det gäller deras design, kapabiliteter och riktade användningsfall:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework erbjuder ett strömlinjeformat SDK för att bygga AI-agenter med `AzureAIProjectAgentProvider`. Det gör det möjligt för utvecklare att skapa agenter som använder Azure OpenAI-modeller med inbyggda verktygsanrop, konversationshantering och företagsklassad säkerhet genom Azure-identifiering.

**Användningsfall**: Bygga produktionsklara AI-agenter med verktygsanvändning, flerstegsarbetsflöden och scenarier för företagsintegration.

Här är några viktiga kärnbegrepp i Microsoft Agent Framework:

- **Agenter**. En agent skapas via `AzureAIProjectAgentProvider` och konfigureras med ett namn, instruktioner och verktyg. Agenten kan:
  - **Bearbeta användarmeddelanden** och generera svar med hjälp av Azure OpenAI-modeller.
  - **Anropa verktyg** automatiskt baserat på konversationskontext.
  - **Behålla konversationstillstånd** över flera interaktioner.

  Här är ett kodutdrag som visar hur man skapar en agent:

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

- **Verktyg**. Ramverket stödjer att definiera verktyg som Python-funktioner som agenten kan anropa automatiskt. Verktyg registreras när agenten skapas:

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

- **Koordinering mellan flera agenter**. Du kan skapa flera agenter med olika specialiseringar och koordinera deras arbete:

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

- **Azure-identitetsintegration**. Ramverket använder `AzureCliCredential` (eller `DefaultAzureCredential`) för säker, nyckelfri autentisering, vilket eliminerar behovet av att hantera API-nycklar direkt.

## Azure AI Agent Service

Azure AI Agent Service är en nyare tilläggstjänst, introducerad på Microsoft Ignite 2024. Den möjliggör utveckling och driftsättning av AI-agenter med mer flexibla modeller, såsom att direkt anropa open-source LLMs som Llama 3, Mistral och Cohere.

Azure AI Agent Service erbjuder starkare företags-säkerhetsmekanismer och datalagringsmetoder, vilket gör den lämplig för företagsapplikationer.

Den fungerar direkt med Microsoft Agent Framework för att bygga och distribuera agenter.

Denna tjänst är för närvarande i Public Preview och stödjer Python och C# för att bygga agenter.

Genom att använda Azure AI Agent Service Python SDK kan vi skapa en agent med ett användardefinierat verktyg:

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

### Kärnbegrepp

Azure AI Agent Service har följande kärnbegrepp:

- **Agent**. Azure AI Agent Service integreras med Microsoft Foundry. Inom AI Foundry fungerar en AI Agent som en "smart" mikrotjänst som kan användas för att besvara frågor (RAG), utföra åtgärder eller helt automatisera arbetsflöden. Detta uppnås genom att kombinera kraften i generativa AI-modeller med verktyg som gör det möjligt för agenten att få tillgång till och interagera med verkliga datakällor. Här är ett exempel på en agent:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    I detta exempel skapas en agent med modellen `gpt-4o-mini`, ett namn `my-agent`, och instruktionerna `You are helpful agent`. Agenten är utrustad med verktyg och resurser för att utföra uppgifter som tolkning av kod.

- **Thread och meddelanden**. Thread är ett annat viktigt begrepp. Det representerar en konversation eller interaktion mellan en agent och en användare. Threads kan användas för att följa konversationens framsteg, lagra kontextinformation och hantera interaktionens tillstånd. Här är ett exempel på en thread:

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

    I den föregående koden skapas en thread. Därefter skickas ett meddelande till tråden. Genom att kalla `create_and_process_run` ombeds agenten utföra arbete i tråden. Slutligen hämtas och loggas meddelandena för att se agentens svar. Meddelandena visar konversationens framsteg mellan användaren och agenten. Det är också viktigt att förstå att meddelandena kan vara av olika typer såsom text, bild eller fil, det vill säga att agenternas arbete till exempel har resulterat i en bild eller ett textsvar. Som utvecklare kan du sedan använda denna information för att vidarebearbeta svaret eller presentera det för användaren.

- **Integreras med Microsoft Agent Framework**. Azure AI Agent Service fungerar sömlöst med Microsoft Agent Framework, vilket innebär att du kan bygga agenter med `AzureAIProjectAgentProvider` och distribuera dem via Agent Service för produktionsscenarier.

**Användningsfall**: Azure AI Agent Service är utformad för företagsapplikationer som kräver säker, skalbar och flexibel driftsättning av AI-agenter.

## Vad är skillnaden mellan dessa tillvägagångssätt?
 
Det verkar som om det finns överlappningar, men det finns några viktiga skillnader när det gäller deras design, kapabiliteter och riktade användningsfall:
 
- **Microsoft Agent Framework (MAF)**: Är ett produktionsklart SDK för att bygga AI-agenter. Det tillhandahåller ett strömlinjeformat API för att skapa agenter med verktygsanrop, konversationshantering och Azure-identitetsintegration.
- **Azure AI Agent Service**: Är en plattform och driftsättningstjänst i Azure Foundry för agenter. Den erbjuder inbyggd anslutning till tjänster som Azure OpenAI, Azure AI Search, Bing Search och kodkörning.
 
Är du fortfarande osäker på vilken du ska välja?

### Användningsfall
 
Låt oss se om vi kan hjälpa dig genom att gå igenom några vanliga användningsfall:
 
> Q: Jag bygger produktions-AI-agentapplikationer och vill komma igång snabbt
>

>A: Microsoft Agent Framework är ett utmärkt val. Det erbjuder ett enkelt, Pythoniskt API via `AzureAIProjectAgentProvider` som låter dig definiera agenter med verktyg och instruktioner på bara några rader kod.

>Q: Jag behöver företagsklassad driftsättning med Azure-integrationer som Search och kodkörning
>
> A: Azure AI Agent Service är det bästa valet. Det är en plattformstjänst som erbjuder inbyggda möjligheter för flera modeller, Azure AI Search, Bing Search och Azure Functions. Det gör det enkelt att bygga dina agenter i Foundry-portalen och driftsätta dem i stor skala.
 
> Q: Jag är fortfarande förvirrad, ge mig bara ett alternativ
>
> A: Börja med Microsoft Agent Framework för att bygga dina agenter, och använd sedan Azure AI Agent Service när du behöver driftsätta och skala dem i produktion. Detta tillvägagångssätt låter dig iterera snabbt på agentlogiken samtidigt som du har en tydlig väg till företagsdriftsättning.
 
Låt oss sammanfatta de viktigaste skillnaderna i en tabell:

| Framework | Fokus | Kärnkoncept | Användningsfall |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Strömlinjeformat SDK för agenter med verktygsanrop | Agenter, Verktyg, Azure Identity | Bygga AI-agenter, verktygsanvändning, flerstegsarbetsflöden |
| Azure AI Agent Service | Flexibla modeller, företagsäkerhet, Kodgenerering, Verktygsanrop | Modularitet, Samarbete, Processorkestrering | Säker, skalbar och flexibel driftsättning av AI-agenter |

## Kan jag integrera mina befintliga Azure-ekosystemverktyg direkt, eller behöver jag fristående lösningar?
Svaret är ja — du kan integrera dina befintliga verktyg i Azure-ekosystemet direkt med Azure AI Agent Service, särskilt eftersom den är byggd för att fungera sömlöst med andra Azure-tjänster. Du kan till exempel integrera Bing, Azure AI Search och Azure Functions. Det finns också djup integration med Microsoft Foundry.

Microsoft Agent Framework integreras också med Azure-tjänster via `AzureAIProjectAgentProvider` och Azure-identitet, vilket låter dig anropa Azure-tjänster direkt från dina agentverktyg.

## Kodexempel

- Python: [Agentramverk](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agentramverk](./code_samples/02-dotnet-agent-framework.md)

## Har du fler frågor om AI-agentramverk?

Gå med i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) för att träffa andra studerande, delta i kontorstid och få svar på dina frågor om AI-agenter.

## Referenser

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent-tjänst</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI-svar</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent-tjänst</a>

## Föregående lektion

[Introduktion till AI-agenter och användningsfall för agenter](../01-intro-to-ai-agents/README.md)

## Nästa lektion

[Förstå agentiska designmönster](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Ansvarsfriskrivning:
Detta dokument har översatts med hjälp av AI-översättningstjänsten Co-op Translator (https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet bör du vara medveten om att automatiska översättningar kan innehålla fel eller brister. Originaldokumentet på ursprungsspråket ska betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->