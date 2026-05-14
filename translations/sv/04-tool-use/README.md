[![Hur man designar bra AI-agenter](../../../translated_images/sv/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klicka på bilden ovan för att se videon av denna lektion)_

# Designmönster för verktygsanvändning

Verktyg är intressanta eftersom de tillåter AI-agenter att ha en bredare uppsättning möjligheter. Istället för att agenten har en begränsad mängd åtgärder den kan utföra, kan agenten nu utföra ett stort antal åtgärder genom att lägga till ett verktyg. I detta kapitel ska vi titta på designmönstret för verktygsanvändning, som beskriver hur AI-agenter kan använda specifika verktyg för att uppnå sina mål.

## Introduktion

I denna lektion vill vi besvara följande frågor:

- Vad är designmönstret för verktygsanvändning?
- Vilka användningsfall kan det tillämpas på?
- Vilka element/byggstenar behövs för att implementera designmönstret?
- Vilka särskilda överväganden finns för att använda designmönstret för verktygsanvändning för att bygga pålitliga AI-agenter?

## Lärandemål

Efter att ha slutfört denna lektion kommer du att kunna:

- Definiera designmönstret för verktygsanvändning och dess syfte.
- Identifiera användningsfall där designmönstret för verktygsanvändning är tillämpligt.
- Förstå de viktigaste elementen som behövs för att implementera designmönstret.
- Känna igen överväganden för att säkerställa pålitlighet hos AI-agenter som använder detta designmönster.

## Vad är designmönstret för verktygsanvändning?

**Designmönstret för verktygsanvändning** fokuserar på att ge LLM:er möjligheten att interagera med externa verktyg för att nå specifika mål. Verktyg är kod som kan köras av en agent för att utföra åtgärder. Ett verktyg kan vara en enkel funktion som en räknare, eller ett API-anrop till en tredjepartstjänst som att slå upp aktiekurser eller väderprognos. I sammanhanget AI-agenter är verktyg designade för att köras av agenter som svar på **modellgenererade funktionsanrop**.

## Vilka användningsfall kan det tillämpas på?

AI-agenter kan använda verktyg för att slutföra komplexa uppgifter, hämta information eller fatta beslut. Designmönstret för verktygsanvändning används ofta i scenarier som kräver dynamisk interaktion med externa system, såsom databaser, webbtjänster eller kodtolkare. Denna förmåga är användbar för flera olika användningsfall, bland annat:

- **Dynamisk informationshämtning:** Agenter kan fråga externa API:er eller databaser för att hämta aktuella data (t.ex. att fråga en SQLite-databas för dataanalys, hämta aktiekurser eller väderinformation).
- **Kodkörning och tolkning:** Agenter kan köra kod eller skript för att lösa matematiska problem, generera rapporter eller utföra simuleringar.
- **Automatisering av arbetsflöden:** Automatisera repetitiva eller flerstegsarbetsflöden genom att integrera verktyg som schemaläggare, e-posttjänster eller datapipelines.
- **Kundsupport:** Agenter kan interagera med CRM-system, ärendehanteringsplattformar eller kunskapsdatabaser för att lösa användarfrågor.
- **Innehållsgenerering och redigering:** Agenter kan använda verktyg som grammatikkontroller, textsammanfattare eller verktyg för utvärdering av innehållssäkerhet för att assistera vid innehållsskapande.

## Vilka element/byggstenar behövs för att implementera designmönstret för verktygsanvändning?

Dessa byggstenar tillåter AI-agenten att utföra en rad olika uppgifter. Låt oss titta på de viktigaste elementen som behövs för att implementera designmönstret för verktygsanvändning:

- **Funktions-/Verktygsscheman**: Detaljerade definitioner av tillgängliga verktyg, inklusive funktionsnamn, syfte, nödvändiga parametrar och förväntade utdata. Dessa scheman gör det möjligt för LLM att förstå vilka verktyg som finns tillgängliga och hur man konstruerar giltiga förfrågningar.

- **Logik för funktionskörning**: Styr hur och när verktyg anropas baserat på användarens avsikt och samtalskontext. Detta kan inkludera planeringsmoduler, styrmekanismer eller villkorliga flöden som dynamiskt avgör verktygsanvändning.

- **Meddelandeshanteringssystem**: Komponenter som hanterar samtalsflödet mellan användarinmatningar, LLM-svar, verktygsanrop och verktygsutdata.

- **Verktygsintegrationsramverk**: Infrastruktur som kopplar agenten till olika verktyg, oavsett om de är enkla funktioner eller komplexa externa tjänster.

- **Felhanteing och validering**: Mekanismer för att hantera fel vid verktygskörning, validera parametrar och hantera oväntade svar.

- **Tillståndshantering**: Spårar samtalskontext, tidigare verktygsväxlingar och bestående data för att säkerställa konsekvens över flerstegsinteraktioner.

Nästa steg är att titta närmare på funktions- och verktygsanrop.

### Funktions-/Verktygsanrop

Funktionsanrop är det primära sättet vi gör det möjligt för stora språkmodeller (LLM) att interagera med verktyg. Du kommer ofta att se "funktion" och "verktyg" användas synonymt eftersom "funktioner" (återanvändbara kodblock) är de "verktyg" som agenter använder för att utföra uppgifter. För att kunna anropa en funktions kod måste en LLM jämföra användarens förfrågan med funktionens beskrivning. För att göra detta skickas ett schema som innehåller beskrivningarna av alla tillgängliga funktioner till LLM:n. LLM väljer sedan den mest lämpliga funktionen för uppgiften och returnerar dess namn och argument. Den valda funktionen anropas, dess svar skickas tillbaka till LLM:n som använder informationen för att svara på användarens fråga.

För utvecklare som vill implementera funktionsanrop för agenter krävs:

1. En LLM-modell som stöder funktionsanrop
2. Ett schema som innehåller funktionsbeskrivningar
3. Koden för varje beskrivna funktion

Låt oss använda exemplet att ta reda på aktuell tid i en stad för att illustrera:

1. **Initiera en LLM som stöder funktionsanrop:**

    Inte alla modeller stödjer funktionsanrop, så det är viktigt att kontrollera att den LLM du använder gör det. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> stöder funktionsanrop. Vi kan börja med att initiera Azure OpenAI-klienten.

    ```python
    # Initiera Azure OpenAI-klienten
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Skapa ett funktionsschema**:

    Nästa steg är att definiera ett JSON-schema som innehåller funktionsnamnet, beskrivningen av vad funktionen gör och namnen och beskrivningarna av funktionsparametrarna.
    Vi skickar sedan detta schema till klienten som vi skapade tidigare, tillsammans med användarens förfrågan att ta reda på tiden i San Francisco. Det viktiga att notera är att det som returneras är ett **verktygsanrop**, **inte** det slutgiltiga svaret på frågan. Som nämnts tidigare returnerar LLM namnet på den funktion den valt för uppgiften och argumenten som ska skickas till den.

    ```python
    # Funktionsbeskrivning för modellen att läsa
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_time",
                "description": "Get the current time in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city name, e.g. San Francisco",
                        },
                    },
                    "required": ["location"],
                },
            }
        }
    ]
    ```
   
    ```python
  
    # Inledande användarmeddelande
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Första API-anropet: Be modellen använda funktionen
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Bearbeta modellens svar
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Funktionskoden som krävs för att utföra uppgiften:**

    Nu när LLM har valt vilken funktion som måste köras behöver koden som utför uppgiften implementeras och köras.
    Vi kan implementera koden för att hämta aktuell tid i Python. Vi behöver också skriva koden för att extrahera namn och argument från response_message för att få det slutgiltiga resultatet.

    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

     ```python
     # Hantera funktionsanrop
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # Andra API-anropet: Hämta det slutgiltiga svaret från modellen
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

Funktionsanrop är kärnan i de flesta, om inte alla, agenters verktygsanvändningsdesign men att implementera det från grunden kan ibland vara utmanande.
Som vi lärde oss i [Lektion 2](../../../02-explore-agentic-frameworks) erbjuder agentbaserade ramverk oss förbyggda byggstenar för att implementera verktygsanvändning.

## Exempel på verktygsanvändning med agentbaserade ramverk

Här är några exempel på hur du kan implementera designmönstret för verktygsanvändning med olika agentbaserade ramverk:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> är ett open source-ramverk för att bygga AI-agenter. Det förenklar processen med funktionsanrop genom att låta dig definiera verktyg som Python-funktioner med `@tool`-dekorationen. Ramverket hanterar kommunikationen fram och tillbaka mellan modellen och din kod. Det erbjuder också tillgång till förbyggda verktyg som Fil-sökning och Kodtolkare via `AzureAIProjectAgentProvider`.

Följande diagram illustrerar processen för funktionsanrop med Microsoft Agent Framework:

![funktionsanrop](../../../translated_images/sv/functioncalling-diagram.a84006fc287f6014.webp)

I Microsoft Agent Framework definieras verktyg som dekorerade funktioner. Vi kan konvertera funktionen `get_current_time` som vi såg tidigare till ett verktyg genom att använda `@tool`-dekorationen. Ramverket serialiserar automatiskt funktionen och dess parametrar, och skapar schemat som skickas till LLM.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Skapa klienten
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Skapa en agent och kör med verktyget
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> är ett nyare agentbaserat ramverk designat för att ge utvecklare möjlighet att säkert bygga, distribuera och skala högkvalitativa och utbyggbara AI-agenter utan att behöva hantera underliggande dator- och lagringsresurser. Det är särskilt användbart för företagsapplikationer eftersom det är en helt hanterad tjänst med företagsklassad säkerhet.

Jämfört med att utveckla direkt med LLM API erbjuder Azure AI Agent Service vissa fördelar, inklusive:

- Automatisk funktionsanrop – inget behov att analysera ett verktygsanrop, anropa verktyget och hantera svaret; allt detta görs nu på serversidan
- Säkert hanterad data – istället för att hantera ditt eget samtalstillstånd kan du förlita dig på threads för att lagra all information du behöver
- Verktyg som fungerar direkt – Verktyg du kan använda för att interagera med dina datakällor, såsom Bing, Azure AI Search och Azure Functions.

Verktygen som finns tillgängliga i Azure AI Agent Service kan delas in i två kategorier:

1. Kunskapsverktyg:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grundning med Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Fil-sökning</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Åtgärdsverktyg:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Funktionsanrop</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Kodtolkare</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI-definierade verktyg</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agenttjänsten gör det möjligt för oss att använda dessa verktyg tillsammans som ett `toolset`. Den använder även `threads` som håller reda på historiken av meddelanden från ett särskilt samtal.

Föreställ dig att du är en säljagent på ett företag som heter Contoso. Du vill utveckla en konverserande agent som kan svara på frågor om din försäljningsdata.

Följande bild illustrerar hur du kan använda Azure AI Agent Service för att analysera din försäljningsdata:

![Agenttjänsten i aktion](../../../translated_images/sv/agent-service-in-action.34fb465c9a84659e.webp)

För att använda något av dessa verktyg med tjänsten kan vi skapa en klient och definiera ett verktyg eller verktygssats. För att praktiskt genomföra detta kan vi använda följande Python-kod. LLM:n kan titta på verktygssatsen och avgöra om den ska använda den användarskapade funktionen `fetch_sales_data_using_sqlite_query` eller den förbyggda Kodtolkaren, beroende på användarförfrågan.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query-funktion som kan hittas i filen fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initiera verktygssats
toolset = ToolSet()

# Initiera agent för funktionsanrop med funktionen fetch_sales_data_using_sqlite_query och lägg till den i verktygssatsen
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Initiera kodtolkningsverktyg och lägg till det i verktygssatsen.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Vilka är de särskilda övervägandena för att använda designmönstret för verktygsanvändning för att bygga pålitliga AI-agenter?

En vanlig oro med SQL som dynamiskt genereras av LLM:er är säkerhet, särskilt risken för SQL-injektion eller illvilliga åtgärder, som att ta bort eller manipulera databasen. Även om dessa farhågor är giltiga kan de effektivt mildras genom att korrekt konfigurera databastillgångsrättigheter. För de flesta databaser innebär detta att databasen konfigureras som skrivskyddad. För databastjänster som PostgreSQL eller Azure SQL bör appen tilldelas en skrivskyddad (SELECT) roll.

Att köra appen i en säker miljö förbättrar skyddet ytterligare. I företagsmiljöer extraheras och omvandlas data vanligtvis från operativa system till en skrivskyddad databas eller datalager med ett användarvänligt schema. Denna metod säkerställer att data är säker, optimerad för prestanda och tillgänglighet, samt att appen har begränsad, skrivskyddad åtkomst.

## Exempelkoder

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Fler frågor om designmönstren för verktygsanvändning?

Gå med i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) för att träffa andra som lär sig, delta i kontorstider och få svar på dina frågor om AI-agenter.

## Ytterligare resurser

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Översikt Microsoft Agent Framework</a>

## Föregående lektion

[Förståelse för agentbaserade designmönster](../03-agentic-design-patterns/README.md)

## Nästa lektion
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->