<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7c3b7bd1b3528074d8b6a7c5ad33b6f",
  "translation_date": "2025-11-18T17:49:12+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "nl"
}
-->
[![Hoe ontwerp je goede AI-agenten](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.nl.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klik op de afbeelding hierboven om de video van deze les te bekijken)_

# Tool Use Design Pattern

Tools zijn interessant omdat ze AI-agenten in staat stellen een breder scala aan mogelijkheden te hebben. In plaats van dat de agent een beperkte set acties kan uitvoeren, kan de agent met een tool nu een breed scala aan acties uitvoeren. In dit hoofdstuk bekijken we het Tool Use Design Pattern, dat beschrijft hoe AI-agenten specifieke tools kunnen gebruiken om hun doelen te bereiken.

## Introductie

In deze les willen we de volgende vragen beantwoorden:

- Wat is het Tool Use Design Pattern?
- Voor welke toepassingen kan het worden gebruikt?
- Wat zijn de elementen/bouwstenen die nodig zijn om het design pattern te implementeren?
- Welke speciale overwegingen zijn er bij het gebruik van het Tool Use Design Pattern om betrouwbare AI-agenten te bouwen?

## Leerdoelen

Na het voltooien van deze les kun je:

- Het Tool Use Design Pattern definiëren en het doel ervan uitleggen.
- Toepassingen identificeren waar het Tool Use Design Pattern van toepassing is.
- De belangrijkste elementen begrijpen die nodig zijn om het design pattern te implementeren.
- Overwegingen herkennen om betrouwbaarheid te waarborgen in AI-agenten die dit design pattern gebruiken.

## Wat is het Tool Use Design Pattern?

Het **Tool Use Design Pattern** richt zich op het geven van LLMs de mogelijkheid om te communiceren met externe tools om specifieke doelen te bereiken. Tools zijn code die door een agent kan worden uitgevoerd om acties uit te voeren. Een tool kan een eenvoudige functie zijn, zoals een rekenmachine, of een API-aanroep naar een externe service, zoals het opvragen van aandelenkoersen of weersvoorspellingen. In de context van AI-agenten zijn tools ontworpen om door agenten te worden uitgevoerd als reactie op **modelgegenereerde functieaanroepen**.

## Voor welke toepassingen kan het worden gebruikt?

AI-agenten kunnen tools gebruiken om complexe taken uit te voeren, informatie op te halen of beslissingen te nemen. Het Tool Use Design Pattern wordt vaak gebruikt in scenario's die dynamische interactie met externe systemen vereisen, zoals databases, webservices of code-interpreters. Deze mogelijkheid is nuttig voor verschillende toepassingen, waaronder:

- **Dynamische informatieopvraging:** Agenten kunnen externe API's of databases raadplegen om actuele gegevens op te halen (bijv. het opvragen van een SQLite-database voor data-analyse, het ophalen van aandelenkoersen of weersinformatie).
- **Code-uitvoering en interpretatie:** Agenten kunnen code of scripts uitvoeren om wiskundige problemen op te lossen, rapporten te genereren of simulaties uit te voeren.
- **Workflow-automatisering:** Het automatiseren van repetitieve of meerstaps-workflows door tools zoals taakplanners, e-mailservices of datastromen te integreren.
- **Klantenservice:** Agenten kunnen communiceren met CRM-systemen, ticketplatforms of kennisbanken om gebruikersvragen op te lossen.
- **Contentcreatie en -bewerking:** Agenten kunnen tools zoals grammaticacontrole, tekstsamenvatting of contentveiligheidsevaluators gebruiken om te helpen bij contentcreatietaken.

## Wat zijn de elementen/bouwstenen die nodig zijn om het Tool Use Design Pattern te implementeren?

Deze bouwstenen stellen de AI-agent in staat een breed scala aan taken uit te voeren. Laten we de belangrijkste elementen bekijken die nodig zijn om het Tool Use Design Pattern te implementeren:

- **Functie-/Toolschemas:** Gedetailleerde definities van beschikbare tools, inclusief functienaam, doel, vereiste parameters en verwachte outputs. Deze schemas stellen de LLM in staat te begrijpen welke tools beschikbaar zijn en hoe geldige verzoeken te construeren.

- **Functie-uitvoeringslogica:** Regelt hoe en wanneer tools worden aangeroepen op basis van de intentie van de gebruiker en de context van het gesprek. Dit kan plannermodules, routeringsmechanismen of conditionele stromen omvatten die het gebruik van tools dynamisch bepalen.

- **Berichtenafhandelingssysteem:** Componenten die de conversatiestroom beheren tussen gebruikersinvoer, LLM-reacties, toolaanroepen en tooloutputs.

- **Toolintegratiekader:** Infrastructuur die de agent verbindt met verschillende tools, of het nu eenvoudige functies of complexe externe services zijn.

- **Foutafhandeling en validatie:** Mechanismen om fouten in tooluitvoering af te handelen, parameters te valideren en onverwachte reacties te beheren.

- **Statusbeheer:** Houdt de context van het gesprek, eerdere toolinteracties en persistente gegevens bij om consistentie te waarborgen bij interacties met meerdere beurten.

Laten we vervolgens Functie-/Toolaanroepen in meer detail bekijken.

### Functie-/Toolaanroepen

Functieaanroepen zijn de primaire manier waarop we Large Language Models (LLMs) in staat stellen om met tools te communiceren. Je zult vaak 'Functie' en 'Tool' door elkaar zien gebruikt, omdat 'functies' (blokken herbruikbare code) de 'tools' zijn die agenten gebruiken om taken uit te voeren. Om de code van een functie aan te roepen, moet een LLM het verzoek van de gebruiker vergelijken met de beschrijving van de functie. Hiervoor wordt een schema met de beschrijvingen van alle beschikbare functies naar de LLM gestuurd. De LLM selecteert vervolgens de meest geschikte functie voor de taak en retourneert de naam en argumenten. De geselecteerde functie wordt aangeroepen, de reactie wordt teruggestuurd naar de LLM, die de informatie gebruikt om te reageren op het verzoek van de gebruiker.

Om functieaanroepen voor agenten te implementeren, heb je nodig:

1. Een LLM-model dat functieaanroepen ondersteunt
2. Een schema met functiebeschrijvingen
3. De code voor elke beschreven functie

Laten we het voorbeeld gebruiken van het verkrijgen van de huidige tijd in een stad om dit te illustreren:

1. **Initialiseer een LLM die functieaanroepen ondersteunt:**

    Niet alle modellen ondersteunen functieaanroepen, dus het is belangrijk om te controleren of de LLM die je gebruikt dit doet. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> ondersteunt functieaanroepen. We kunnen beginnen met het initiëren van de Azure OpenAI-client.

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Maak een Functieschema:**

    Vervolgens definiëren we een JSON-schema dat de functienaam, beschrijving van wat de functie doet, en de namen en beschrijvingen van de functieparameters bevat. We nemen dit schema en sturen het naar de eerder gemaakte client, samen met het verzoek van de gebruiker om de tijd in San Francisco te vinden. Wat belangrijk is om op te merken, is dat een **toolaanroep** wordt geretourneerd, **niet** het uiteindelijke antwoord op de vraag. Zoals eerder vermeld, retourneert de LLM de naam van de functie die is geselecteerd voor de taak en de argumenten die eraan worden doorgegeven.

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
  
1. **De functiecode die nodig is om de taak uit te voeren:**

    Nu de LLM heeft gekozen welke functie moet worden uitgevoerd, moet de code die de taak uitvoert worden geïmplementeerd en uitgevoerd. We kunnen de code implementeren om de huidige tijd in Python te verkrijgen. We moeten ook de code schrijven om de naam en argumenten uit het response_message te halen om het uiteindelijke resultaat te krijgen.

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

Functieaanroepen vormen de kern van de meeste, zo niet alle ontwerpen voor toolgebruik door agenten, maar het implementeren ervan vanaf nul kan soms uitdagend zijn. Zoals we hebben geleerd in [Les 2](../../../02-explore-agentic-frameworks) bieden agentic frameworks ons vooraf gebouwde bouwstenen om toolgebruik te implementeren.

## Voorbeelden van Toolgebruik met Agentic Frameworks

Hier zijn enkele voorbeelden van hoe je het Tool Use Design Pattern kunt implementeren met verschillende agentic frameworks:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> is een open-source AI-framework voor .NET-, Python- en Java-ontwikkelaars die werken met Large Language Models (LLMs). Het vereenvoudigt het proces van functieaanroepen door automatisch je functies en hun parameters te beschrijven aan het model via een proces genaamd <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serialiseren</a>. Het beheert ook de communicatie tussen het model en je code. Een ander voordeel van het gebruik van een agentic framework zoals Semantic Kernel is dat het je toegang geeft tot vooraf gebouwde tools zoals <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">File Search</a> en <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Code Interpreter</a>.

Het volgende diagram illustreert het proces van functieaanroepen met Semantic Kernel:

![functieaanroepen](../../../translated_images/functioncalling-diagram.a84006fc287f60140cc0a484ff399acd25f69553ea05186981ac4d5155f9c2f6.nl.png)

In Semantic Kernel worden functies/tools <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugins</a> genoemd. We kunnen de `get_current_time`-functie die we eerder zagen omzetten in een plugin door er een klasse van te maken met de functie erin. We kunnen ook de `kernel_function`-decorator importeren, die de beschrijving van de functie accepteert. Wanneer je vervolgens een kernel maakt met de GetCurrentTimePlugin, serialiseert de kernel automatisch de functie en haar parameters, waardoor het schema wordt gemaakt om naar de LLM te sturen.

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

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> is een nieuwere agentic framework dat is ontworpen om ontwikkelaars in staat te stellen veilig hoogwaardige en uitbreidbare AI-agenten te bouwen, implementeren en schalen zonder dat ze de onderliggende compute- en opslagbronnen hoeven te beheren. Het is bijzonder nuttig voor zakelijke toepassingen, omdat het een volledig beheerde service is met beveiliging op ondernemingsniveau.

In vergelijking met ontwikkelen met de LLM API rechtstreeks biedt Azure AI Agent Service enkele voordelen, waaronder:

- Automatische toolaanroepen – geen noodzaak om een toolaanroep te parseren, de tool aan te roepen en de reactie af te handelen; dit wordt nu allemaal server-side gedaan.
- Veilig beheerde gegevens – in plaats van je eigen conversatiestatus te beheren, kun je vertrouwen op threads om alle informatie op te slaan die je nodig hebt.
- Kant-en-klare tools – Tools die je kunt gebruiken om te communiceren met je gegevensbronnen, zoals Bing, Azure AI Search en Azure Functions.

De tools die beschikbaar zijn in Azure AI Agent Service kunnen worden onderverdeeld in twee categorieën:

1. Kennis Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding met Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Actie Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Functieaanroepen</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI gedefinieerde tools</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

De Agent Service stelt ons in staat om deze tools samen te gebruiken als een `toolset`. Het maakt ook gebruik van `threads` die de geschiedenis van berichten uit een bepaalde conversatie bijhouden.

Stel je voor dat je een verkoopagent bent bij een bedrijf genaamd Contoso. Je wilt een conversatieagent ontwikkelen die vragen over je verkoopgegevens kan beantwoorden.

De volgende afbeelding illustreert hoe je Azure AI Agent Service kunt gebruiken om je verkoopgegevens te analyseren:

![Agentic Service In Action](../../../translated_images/agent-service-in-action.34fb465c9a84659edd3003f8cb62d6b366b310a09b37c44e32535021fbb5c93f.nl.jpg)

Om een van deze tools met de service te gebruiken, kunnen we een client maken en een tool of toolset definiëren. Om dit praktisch te implementeren, kunnen we de volgende Python-code gebruiken. De LLM kan naar de toolset kijken en beslissen of de door de gebruiker gemaakte functie, `fetch_sales_data_using_sqlite_query`, of de vooraf gebouwde Code Interpreter wordt gebruikt, afhankelijk van het verzoek van de gebruiker.

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

## Wat zijn de speciale overwegingen voor het gebruik van het Tool Use Design Pattern om betrouwbare AI-agenten te bouwen?

Een veelvoorkomende zorg bij SQL die dynamisch wordt gegenereerd door LLMs is beveiliging, met name het risico op SQL-injectie of kwaadaardige acties, zoals het verwijderen of manipuleren van de database. Hoewel deze zorgen geldig zijn, kunnen ze effectief worden verminderd door de toegangsrechten van de database correct te configureren. Voor de meeste databases houdt dit in dat de database wordt geconfigureerd als alleen-lezen. Voor databaseservices zoals PostgreSQL of Azure SQL moet de app een alleen-lezen (SELECT) rol toegewezen krijgen.
Het uitvoeren van de app in een veilige omgeving biedt extra bescherming. In zakelijke scenario's wordt data meestal geëxtraheerd en getransformeerd van operationele systemen naar een alleen-lezen database of datawarehouse met een gebruiksvriendelijke schema. Deze aanpak zorgt ervoor dat de data veilig is, geoptimaliseerd voor prestaties en toegankelijkheid, en dat de app beperkte, alleen-lezen toegang heeft.

## Voorbeeldcodes

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Heb je meer vragen over het gebruik van Tool Use Design Patterns?

Word lid van de [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) om andere leerlingen te ontmoeten, deel te nemen aan spreekuren en je vragen over AI Agents beantwoord te krijgen.

## Aanvullende bronnen

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Function Calling Tutorial</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## Vorige les

[Begrijpen van Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## Volgende les

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->