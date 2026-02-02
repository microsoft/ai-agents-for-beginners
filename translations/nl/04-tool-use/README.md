[![Hoe Ontwerp je Goede AI-agenten](../../../translated_images/nl/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klik op de afbeelding hierboven om de video van deze les te bekijken)_

# Tool Use Design Pattern

Tools zijn interessant omdat ze AI-agenten in staat stellen een breder scala aan mogelijkheden te hebben. In plaats van dat de agent een beperkte set acties kan uitvoeren, kan de agent door het toevoegen van een tool nu een breed scala aan acties uitvoeren. In dit hoofdstuk bekijken we het Tool Use Design Pattern, dat beschrijft hoe AI-agenten specifieke tools kunnen gebruiken om hun doelen te bereiken.

## Inleiding

In deze les willen we de volgende vragen beantwoorden:

- Wat is het tool use design pattern?
- Voor welke use cases kan het toegepast worden?
- Wat zijn de elementen/bouwstenen die nodig zijn om het design pattern te implementeren?
- Wat zijn de speciale overwegingen bij het gebruik van het Tool Use Design Pattern om betrouwbare AI-agenten te bouwen?

## Leerdoelen

Na het voltooien van deze les kun je:

- Het Tool Use Design Pattern definiëren en het doel ervan uitleggen.
- Use cases identificeren waar het Tool Use Design Pattern toepasbaar is.
- De belangrijkste elementen begrijpen die nodig zijn om het design pattern te implementeren.
- Overwegingen herkennen om betrouwbaarheid te waarborgen in AI-agenten die dit design pattern gebruiken.

## Wat is het Tool Use Design Pattern?

Het **Tool Use Design Pattern** richt zich op het geven van de mogelijkheid aan LLM's om te interacteren met externe tools om specifieke doelen te bereiken. Tools zijn code die door een agent uitgevoerd kan worden om acties uit te voeren. Een tool kan een eenvoudige functie zijn zoals een rekenmachine, of een API-aanroep naar een externe dienst zoals het opzoeken van aandelenkoersen of een weersvoorspelling. In de context van AI-agenten zijn tools ontworpen om te worden uitgevoerd door agenten als reactie op **door het model gegenereerde functieaanroepen**.

## Voor welke use cases kan het toegepast worden?

AI-agenten kunnen tools benutten om complexe taken te voltooien, informatie op te halen of beslissingen te nemen. Het tool use design pattern wordt vaak gebruikt in scenario's die dynamische interactie met externe systemen vereisen, zoals databases, webservices of code-interpreters. Deze mogelijkheid is nuttig voor verschillende use cases, waaronder:

- **Dynamisch Informatie Opvragen:** Agenten kunnen externe API's of databases raadplegen om actuele gegevens op te halen (bijv. het raadplegen van een SQLite-database voor data-analyse, ophalen van aandelenkoersen of weerinformatie).
- **Code Uitvoering en Interpretatie:** Agenten kunnen code of scripts uitvoeren om wiskundige problemen op te lossen, rapporten te genereren of simulaties uit te voeren.
- **Automatisering van Workflows:** Het automatiseren van repetitieve of meervoudige stappen in workflows door integratie van tools zoals taakplanners, e-maildiensten of datapijplijnen.
- **Klantenservice:** Agenten kunnen interacteren met CRM-systemen, ticketplatforms of kennisbanken om gebruikersvragen op te lossen.
- **Contentgeneratie en -bewerking:** Agenten kunnen tools gebruiken zoals grammaticacontrole, tekstsamenvatters of tools voor het evalueren van contentveiligheid om te assisteren bij het creëren van content.

## Wat zijn de elementen/bouwstenen die nodig zijn om het tool use design pattern te implementeren?

Deze bouwstenen stellen de AI-agent in staat een breed scala aan taken uit te voeren. Laten we de belangrijkste elementen bekijken die nodig zijn om het Tool Use Design Pattern te implementeren:

- **Functie-/Toolschemas:** Gedetailleerde definities van beschikbare tools, inclusief functienaam, doel, vereiste parameters en verwachte outputs. Deze schemas stellen de LLM in staat te begrijpen welke tools beschikbaar zijn en hoe geldige verzoeken geconstrueerd moeten worden.

- **Logica voor Functie-uitvoering:** Regelt hoe en wanneer tools worden aangeroepen op basis van de intentie van de gebruiker en de context van het gesprek. Dit kan plannermodules, routeringsmechanismen of conditionele stromen bevatten die toolgebruik dynamisch bepalen.

- **Berichtenafhandelingssysteem:** Componenten die de conversatiestroom beheren tussen gebruikersinvoer, LLM-antwoorden, toolaanroepen en tooluitvoer.

- **Tool Integratie Framework:** Infrastructuur die de agent verbindt met diverse tools, of het nu eenvoudige functies of complexe externe diensten zijn.

- **Foutafhandeling & Validatie:** Mechanismen om fouten bij tooluitvoering af te handelen, parameters te valideren en onverwachte reacties te beheren.

- **State Management:** Houdt de gesprekcontext, eerdere toolinteracties en persistente data bij om consistentie te waarborgen bij meerdere gespreksrondes.

Laten we nu Functie-/Tool-aanroepen nader bekijken.

### Functie-/Tool-aanroepen

Functie-aanroepen zijn de primaire manier waarop we Large Language Models (LLM's) in staat stellen te interacteren met tools. Je ziet 'Functie' en 'Tool' vaak door elkaar gebruikt omdat 'functies' (herbruikbare codeblokken) de 'tools' zijn die agenten gebruiken om taken uit te voeren. Om de code van een functie aan te roepen, moet een LLM het verzoek van de gebruiker vergelijken met de beschrijving van de functies. Hiervoor wordt een schema met de beschrijvingen van alle beschikbare functies naar de LLM gestuurd. De LLM selecteert vervolgens de meest geschikte functie voor de taak en retourneert de naam en argumenten. De geselecteerde functie wordt uitgevoerd, het antwoord wordt teruggestuurd naar de LLM, die deze informatie gebruikt om te reageren op het verzoek van de gebruiker.

Voor ontwikkelaars die functie-aanroepen voor agenten willen implementeren, is het nodig:

1. Een LLM-model dat functie-aanroepen ondersteunt
2. Een schema met functiebeschrijvingen
3. De code voor elke beschreven functie

Laten we als voorbeeld het opvragen van de huidige tijd in een stad nemen:

1. **Initieer een LLM die functie-aanroepen ondersteunt:**

    Niet alle modellen ondersteunen functie-aanroepen, dus het is belangrijk te controleren of jouw LLM dat doet. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> ondersteunt functie-aanroepen. We beginnen met het opzetten van de Azure OpenAI client.

    ```python
    # Initialiseer de Azure OpenAI-client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

2. **Maak een Functie-schema**:

    Vervolgens definiëren we een JSON-schema dat de functienaam, beschrijving van wat de functie doet, en de namen en beschrijvingen van de functieparameters bevat.
    We sturen dit schema mee aan de eerder gemaakte client, samen met het gebruikersverzoek om de tijd in San Francisco op te vragen. Het is belangrijk om te beseffen dat een **tool call** wordt geretourneerd, **niet** het uiteindelijke antwoord op de vraag. Zoals eerder genoemd retourneert de LLM de naam van de functie die voor de taak is geselecteerd, en de argumenten die aan die functie worden doorgegeven.

    ```python
    # Functiebeschrijving voor het model om te lezen
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
  
    # Initiële gebruikersbericht
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Eerste API-aanroep: Vraag het model de functie te gebruiken
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Verwerk de reactie van het model
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
3. **De functiecode die nodig is om de taak uit te voeren:**

    Nu de LLM heeft gekozen welke functie moet worden uitgevoerd, moet de code die de taak uitvoert geïmplementeerd en uitgevoerd worden.
    We kunnen de code schrijven om de huidige tijd op te vragen in Python. Ook moeten we de code schrijven om de naam en argumenten uit het response_message te halen om het eindresultaat te verkrijgen.

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
     # Functieaanroepen afhandelen
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
  
      # Tweede API-aanroep: Verkrijg de definitieve respons van het model
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

Functie-aanroepen vormen het hart van de meeste, zo niet alle agent tool use designs, maar het implementeren hiervan vanaf nul kan soms uitdagend zijn.
Zoals we leerden in [Les 2](../../../02-explore-agentic-frameworks) bieden agentische frameworks kant-en-klare bouwstenen om tool gebruik te implementeren.
 
## Voorbeelden van Tool Use met Agentische Frameworks

Hier zijn enkele voorbeelden van hoe je het Tool Use Design Pattern kunt implementeren met verschillende agentische frameworks:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> is een open-source AI-framework voor .NET-, Python- en Java-ontwikkelaars die met Large Language Models (LLM's) werken. Het vereenvoudigt het gebruik van functie-aanroepen door je functies en hun parameters automatisch te beschrijven aan het model via een proces genaamd <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serialisatie</a>. Ook wordt de terugkerende communicatie tussen het model en je code afgehandeld. Een ander voordeel van het gebruik van een agentisch framework zoals Semantic Kernel is dat je toegang hebt tot vooraf gebouwde tools zoals <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">Bestandszoeken</a> en <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Code Interpreter</a>.

Het onderstaande diagram illustreert het proces van functieaanroepen met Semantic Kernel:

![function calling](../../../translated_images/nl/functioncalling-diagram.a84006fc287f6014.webp)

In Semantic Kernel worden functies/tools <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugins</a> genoemd. We kunnen de `get_current_time` functie die we eerder zagen omzetten in een plugin door het in een klasse te plaatsen met de functie erin. We kunnen ook de `kernel_function` decorator importeren, die de beschrijving van de functie bevat. Wanneer je dan een kernel creëert met de GetCurrentTimePlugin, serialiseert de kernel automatisch de functie en de parameters, en creëert zo het schema dat naar de LLM wordt gestuurd.

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

# Maak de kernel aan
kernel = Kernel()

# Maak de plugin aan
get_current_time_plugin = GetCurrentTimePlugin(location)

# Voeg de plugin toe aan de kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> is een nieuwer agentisch framework dat is ontworpen om ontwikkelaars in staat te stellen veilige, hoogwaardige en uitbreidbare AI-agenten te bouwen, te implementeren en te schalen zonder dat ze zich bezig hoeven te houden met de onderliggende compute- en opslagmiddelen. Het is vooral nuttig voor enterprise-toepassingen omdat het een volledig beheerde service is met enterprise-grade beveiliging.

Vergeleken met het rechtstreeks ontwikkelen met de LLM API biedt Azure AI Agent Service enkele voordelen, waaronder:

- Automatisch tool-aanroepen – geen noodzaak om een tool call te parsen, de tool aan te roepen en het antwoord te verwerken; dit gebeurt nu server-side
- Veilig beheerde data – in plaats van zelf state te beheren gebruik je threads die alle benodigde informatie bewaren
- Tools direct beschikbaar – Tools waarmee je kunt interacteren met je datasources, zoals Bing, Azure AI Search en Azure Functions.

De tools die beschikbaar zijn in Azure AI Agent Service kunnen worden onderverdeeld in twee categorieën:

1. Knowledge Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grondslag via Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Bestandszoeken</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Action Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Functie-aanroepen</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI gedefinieerde tools</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

De Agent Service stelt ons in staat deze tools samen te gebruiken als een `toolset`. Het maakt ook gebruik van `threads` die de geschiedenis van berichten van een specifiek gesprek bijhouden.

Stel je voor dat je een sales agent bent bij een bedrijf genaamd Contoso. Je wilt een conversatie-agent ontwikkelen die vragen over je verkoopdata kan beantwoorden.

De volgende afbeelding illustreert hoe je Azure AI Agent Service zou kunnen gebruiken om je verkoopgegevens te analyseren:

![Agentic Service In Action](../../../translated_images/nl/agent-service-in-action.34fb465c9a84659e.webp)

Om een van deze tools met de service te gebruiken kunnen we een client creëren en een tool of toolset definiëren. Om dit praktisch te implementeren kunnen we de volgende Python-code gebruiken. De LLM kan de toolset bekijken en beslissen of de door de gebruiker gemaakte functie `fetch_sales_data_using_sqlite_query` wordt aangeroepen, of de vooraf gebouwde Code Interpreter, afhankelijk van het gebruikersverzoek.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query functie die te vinden is in een fetch_sales_data_functions.py bestand.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initialiseer toolset
toolset = ToolSet()

# Initialiseer functie oproepagent met de fetch_sales_data_using_sqlite_query functie en voeg deze toe aan de toolset
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Initialiseer Code Interpreter tool en voeg deze toe aan de toolset.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Wat zijn de speciale overwegingen bij het gebruik van het Tool Use Design Pattern om betrouwbare AI-agenten te bouwen?

Een veelvoorkomende zorg bij SQL die dynamisch door LLM's wordt gegenereerd, is beveiliging, met name het risico op SQL-injectie of kwaadaardige acties, zoals het verwijderen of wijzigen van de database. Hoewel deze zorgen terecht zijn, kunnen ze effectief worden verminderd door het juist configureren van de toegangsrechten tot de database. Voor de meeste databases houdt dit in dat de database als alleen-lezen wordt ingesteld. Voor databaseservices zoals PostgreSQL of Azure SQL moet de app een alleen-lezen (SELECT) rol krijgen toegewezen.
Het uitvoeren van de app in een beveiligde omgeving verhoogt de bescherming verder. In bedrijfsscenario's worden gegevens doorgaans geëxtraheerd en getransformeerd uit operationele systemen naar een alleen-lezen database of datawarehouse met een gebruiksvriendelijk schema. Deze aanpak zorgt ervoor dat de gegevens veilig zijn, geoptimaliseerd voor prestaties en toegankelijkheid, en dat de app beperkte, alleen-lezen toegang heeft.

## Voorbeeldcodes

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Meer vragen over het gebruik van design patterns voor de tool?

Word lid van de [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) om andere leerlingen te ontmoeten, deel te nemen aan spreekuren en je vragen over AI Agents beantwoord te krijgen.

## Aanvullende Bronnen

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Function Calling Tutorial</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## Vorige Les

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## Volgende Les

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat automatische vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal wordt beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt een professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor enige misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->