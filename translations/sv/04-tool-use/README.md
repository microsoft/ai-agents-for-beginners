<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7c3b7bd1b3528074d8b6a7c5ad33b6f",
  "translation_date": "2025-11-18T17:37:47+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "sv"
}
-->
[![Hur man designar bra AI-agenter](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.sv.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klicka på bilden ovan för att se videon för denna lektion)_

# Designmönster för verktygsanvändning

Verktyg är intressanta eftersom de gör det möjligt för AI-agenter att ha ett bredare utbud av förmågor. Istället för att agenten har en begränsad uppsättning åtgärder den kan utföra, kan den genom att lägga till ett verktyg nu utföra en mängd olika åtgärder. I detta kapitel kommer vi att titta på designmönstret för verktygsanvändning, som beskriver hur AI-agenter kan använda specifika verktyg för att uppnå sina mål.

## Introduktion

I denna lektion försöker vi besvara följande frågor:

- Vad är designmönstret för verktygsanvändning?
- Vilka användningsområden kan det tillämpas på?
- Vilka är de element/byggstenar som behövs för att implementera designmönstret?
- Vilka är de särskilda övervägandena för att använda designmönstret för verktygsanvändning för att bygga pålitliga AI-agenter?

## Lärandemål

Efter att ha slutfört denna lektion kommer du att kunna:

- Definiera designmönstret för verktygsanvändning och dess syfte.
- Identifiera användningsområden där designmönstret för verktygsanvändning är tillämpligt.
- Förstå de viktigaste elementen som behövs för att implementera designmönstret.
- Känna igen överväganden för att säkerställa tillförlitlighet i AI-agenter som använder detta designmönster.

## Vad är designmönstret för verktygsanvändning?

**Designmönstret för verktygsanvändning** fokuserar på att ge LLM:er förmågan att interagera med externa verktyg för att uppnå specifika mål. Verktyg är kod som kan köras av en agent för att utföra åtgärder. Ett verktyg kan vara en enkel funktion som en kalkylator eller ett API-anrop till en tredjepartstjänst, som att hämta aktiekurser eller väderprognoser. I AI-agenters sammanhang är verktyg designade för att köras av agenter som svar på **modellgenererade funktionsanrop**.

## Vilka användningsområden kan det tillämpas på?

AI-agenter kan använda verktyg för att slutföra komplexa uppgifter, hämta information eller fatta beslut. Designmönstret för verktygsanvändning används ofta i scenarier som kräver dynamisk interaktion med externa system, såsom databaser, webbtjänster eller kodtolkare. Denna förmåga är användbar för ett antal olika användningsområden, inklusive:

- **Dynamisk informationshämtning:** Agenter kan fråga externa API:er eller databaser för att hämta uppdaterad data (t.ex. fråga en SQLite-databas för dataanalys, hämta aktiekurser eller väderinformation).
- **Kodkörning och tolkning:** Agenter kan köra kod eller skript för att lösa matematiska problem, generera rapporter eller utföra simuleringar.
- **Arbetsflödesautomatisering:** Automatisera repetitiva eller flerstegsarbetsflöden genom att integrera verktyg som schemaläggare, e-posttjänster eller datapipelines.
- **Kundsupport:** Agenter kan interagera med CRM-system, ärendehanteringsplattformar eller kunskapsbaser för att lösa användarfrågor.
- **Innehållsgenerering och redigering:** Agenter kan använda verktyg som grammatikgranskare, textsammanfattare eller innehållssäkerhetsutvärderare för att hjälpa till med innehållsskapande uppgifter.

## Vilka är de element/byggstenar som behövs för att implementera designmönstret för verktygsanvändning?

Dessa byggstenar gör det möjligt för AI-agenten att utföra en mängd olika uppgifter. Låt oss titta på de viktigaste elementen som behövs för att implementera designmönstret för verktygsanvändning:

- **Funktions-/verktygsscheman:** Detaljerade definitioner av tillgängliga verktyg, inklusive funktionsnamn, syfte, nödvändiga parametrar och förväntade utdata. Dessa scheman gör det möjligt för LLM att förstå vilka verktyg som är tillgängliga och hur man konstruerar giltiga förfrågningar.

- **Logik för funktionskörning:** Styr hur och när verktyg anropas baserat på användarens avsikt och samtalskontext. Detta kan inkludera planeringsmoduler, routningsmekanismer eller villkorliga flöden som dynamiskt avgör verktygsanvändning.

- **Meddelandehanteringssystem:** Komponenter som hanterar samtalsflödet mellan användarinmatningar, LLM-svar, verktygsanrop och verktygsutdata.

- **Integrationsramverk för verktyg:** Infrastruktur som kopplar agenten till olika verktyg, oavsett om de är enkla funktioner eller komplexa externa tjänster.

- **Felfunktion och validering:** Mekanismer för att hantera fel i verktygskörning, validera parametrar och hantera oväntade svar.

- **Tillståndshantering:** Spårar samtalskontext, tidigare verktygsinteraktioner och ihållande data för att säkerställa konsekvens över flera interaktioner.

Låt oss nu titta närmare på funktions-/verktygsanrop.

### Funktions-/verktygsanrop

Funktionsanrop är det primära sättet vi gör det möjligt för stora språkmodeller (LLM:er) att interagera med verktyg. Du kommer ofta att se "funktion" och "verktyg" användas omväxlande eftersom "funktioner" (block av återanvändbar kod) är de "verktyg" som agenter använder för att utföra uppgifter. För att en funktions kod ska anropas måste en LLM jämföra användarens förfrågan med funktionens beskrivning. För att göra detta skickas ett schema som innehåller beskrivningarna av alla tillgängliga funktioner till LLM. LLM väljer sedan den mest lämpliga funktionen för uppgiften och returnerar dess namn och argument. Den valda funktionen anropas, dess svar skickas tillbaka till LLM, som använder informationen för att svara på användarens förfrågan.

För att utvecklare ska kunna implementera funktionsanrop för agenter behöver du:

1. En LLM-modell som stöder funktionsanrop
2. Ett schema som innehåller funktionsbeskrivningar
3. Koden för varje funktion som beskrivs

Låt oss använda exemplet att få aktuell tid i en stad för att illustrera:

1. **Initiera en LLM som stöder funktionsanrop:**

    Alla modeller stöder inte funktionsanrop, så det är viktigt att kontrollera att LLM:en du använder gör det. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> stöder funktionsanrop. Vi kan börja med att initiera Azure OpenAI-klienten.

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Skapa ett funktionsschema:**

    Därefter definierar vi ett JSON-schema som innehåller funktionsnamnet, en beskrivning av vad funktionen gör och namnen och beskrivningarna av funktionsparametrarna. Vi tar sedan detta schema och skickar det till den tidigare skapade klienten, tillsammans med användarens förfrågan att hitta tiden i San Francisco. Det som är viktigt att notera är att ett **verktygsanrop** är vad som returneras, **inte** det slutliga svaret på frågan. Som nämnts tidigare returnerar LLM namnet på den funktion som valts för uppgiften och de argument som kommer att skickas till den.

    ```python
    # Function description for the model to read
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
  
    # Initial user message
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # First API call: Ask the model to use the function
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Process the model's response
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Den funktionskod som krävs för att utföra uppgiften:**

    Nu när LLM har valt vilken funktion som behöver köras måste koden som utför uppgiften implementeras och köras. Vi kan implementera koden för att få aktuell tid i Python. Vi måste också skriva koden för att extrahera namnet och argumenten från response_message för att få det slutliga resultatet.

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
     # Handle function calls
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
  
      # Second API call: Get the final response from the model
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

Funktionsanrop är kärnan i de flesta, om inte alla, agenters design för verktygsanvändning, men att implementera det från grunden kan ibland vara utmanande. Som vi lärde oss i [Lektion 2](../../../02-explore-agentic-frameworks) ger agentiska ramverk oss förbyggda byggstenar för att implementera verktygsanvändning.

## Exempel på verktygsanvändning med agentiska ramverk

Här är några exempel på hur du kan implementera designmönstret för verktygsanvändning med olika agentiska ramverk:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> är ett open-source AI-ramverk för .NET-, Python- och Java-utvecklare som arbetar med stora språkmodeller (LLM:er). Det förenklar processen för att använda funktionsanrop genom att automatiskt beskriva dina funktioner och deras parametrar för modellen genom en process som kallas <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serialisering</a>. Det hanterar också kommunikationen fram och tillbaka mellan modellen och din kod. En annan fördel med att använda ett agentiskt ramverk som Semantic Kernel är att det låter dig komma åt förbyggda verktyg som <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">File Search</a> och <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Code Interpreter</a>.

Följande diagram illustrerar processen för funktionsanrop med Semantic Kernel:

![funktionsanrop](../../../translated_images/functioncalling-diagram.a84006fc287f60140cc0a484ff399acd25f69553ea05186981ac4d5155f9c2f6.sv.png)

I Semantic Kernel kallas funktioner/verktyg <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugins</a>. Vi kan konvertera `get_current_time`-funktionen vi såg tidigare till ett plugin genom att göra det till en klass med funktionen i den. Vi kan också importera dekoratorn `kernel_function`, som tar in beskrivningen av funktionen. När du sedan skapar en kernel med GetCurrentTimePlugin kommer kerneln automatiskt att serialisera funktionen och dess parametrar, vilket skapar schemat som skickas till LLM i processen.

```python
from semantic_kernel.functions import kernel_function

class GetCurrentTimePlugin:
    async def __init__(self, location):
        self.location = location

    @kernel_function(
        description="Get the current time for a given location"
    )
    def get_current_time(location: str = ""):
        ...

```

```python 
from semantic_kernel import Kernel

# Create the kernel
kernel = Kernel()

# Create the plugin
get_current_time_plugin = GetCurrentTimePlugin(location)

# Add the plugin to the kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> är ett nyare agentiskt ramverk som är designat för att ge utvecklare möjlighet att säkert bygga, distribuera och skala högkvalitativa och utbyggbara AI-agenter utan att behöva hantera de underliggande beräknings- och lagringsresurserna. Det är särskilt användbart för företagsapplikationer eftersom det är en fullt hanterad tjänst med säkerhet i företagsklass.

Jämfört med att utveckla direkt med LLM API erbjuder Azure AI Agent Service vissa fördelar, inklusive:

- Automatiska verktygsanrop – inget behov av att tolka ett verktygsanrop, anropa verktyget och hantera svaret; allt detta görs nu på serversidan
- Säkert hanterad data – istället för att hantera ditt eget samtalstillstånd kan du förlita dig på trådar för att lagra all information du behöver
- Förbyggda verktyg – Verktyg som du kan använda för att interagera med dina datakällor, såsom Bing, Azure AI Search och Azure Functions.

Verktygen som finns tillgängliga i Azure AI Agent Service kan delas in i två kategorier:

1. Kunskapsverktyg:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grundning med Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Åtgärdsverktyg:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Funktionsanrop</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI-definierade verktyg</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agenttjänsten gör det möjligt för oss att använda dessa verktyg tillsammans som en `toolset`. Den använder också `threads` som håller reda på historiken av meddelanden från ett visst samtal.

Föreställ dig att du är en säljagent på ett företag som heter Contoso. Du vill utveckla en konversationsagent som kan svara på frågor om din försäljningsdata.

Följande bild illustrerar hur du kan använda Azure AI Agent Service för att analysera din försäljningsdata:

![Agenttjänst i aktion](../../../translated_images/agent-service-in-action.34fb465c9a84659edd3003f8cb62d6b366b310a09b37c44e32535021fbb5c93f.sv.jpg)

För att använda något av dessa verktyg med tjänsten kan vi skapa en klient och definiera ett verktyg eller en verktygssamling. För att implementera detta praktiskt kan vi använda följande Python-kod. LLM kommer att kunna titta på verktygssamlingen och avgöra om den ska använda den användarskapade funktionen, `fetch_sales_data_using_sqlite_query`, eller den förbyggda Code Interpreter beroende på användarens förfrågan.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query function which can be found in a fetch_sales_data_functions.py file.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initialize function calling agent with the fetch_sales_data_using_sqlite_query function and adding it to the toolset
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset = ToolSet()
toolset.add(fetch_data_function)

# Initialize Code Interpreter tool and adding it to the toolset. 
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset = ToolSet()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Vilka är de särskilda övervägandena för att använda designmönstret för verktygsanvändning för att bygga pålitliga AI-agenter?

En vanlig oro med SQL som dynamiskt genereras av LLM:er är säkerhet, särskilt risken för SQL-injektion eller skadliga åtgärder, såsom att radera eller manipulera databasen. Även om dessa farhågor är giltiga kan de effektivt mildras genom att korrekt konfigurera databasens åtkomstbehörigheter. För de flesta databaser innebär detta att konfigurera databasen som skrivskyddad. För databastjänster som PostgreSQL eller Azure SQL bör appen tilldelas en skrivskyddad (SELECT) roll.
Att köra appen i en säker miljö förbättrar skyddet ytterligare. I företagsmiljöer extraheras och transformeras data vanligtvis från operativa system till en skrivskyddad databas eller ett datalager med ett användarvänligt schema. Detta tillvägagångssätt säkerställer att data är säkra, optimerade för prestanda och tillgänglighet, och att appen har begränsad, skrivskyddad åtkomst.

## Exempelkod

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Har du fler frågor om designmönster för verktygsanvändning?

Gå med i [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) för att träffa andra som lär sig, delta i öppet hus och få svar på dina frågor om AI-agenter.

## Ytterligare resurser

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Function Calling Tutorial</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## Föregående lektion

[Förstå agentiska designmönster](../03-agentic-design-patterns/README.md)

## Nästa lektion

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->