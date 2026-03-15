[![Hoe ontwerp je goede AI-agenten](../../../translated_images/nl/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klik op de afbeelding hierboven om de video van deze les te bekijken)_

# Tool Use Design Pattern

Tools zijn interessant omdat ze AI-agenten een breder scala aan mogelijkheden bieden. In plaats van dat de agent een beperkte set acties kan uitvoeren, kan de agent door het toevoegen van een tool nu een breed scala aan acties uitvoeren. In dit hoofdstuk bekijken we het Tool Use Design Pattern, dat beschrijft hoe AI-agenten specifieke tools kunnen gebruiken om hun doelen te bereiken.

## Introductie

In deze les willen we de volgende vragen beantwoorden:

- Wat is het tool use design pattern?
- Voor welke gebruikssituaties kan het worden toegepast?
- Wat zijn de elementen/bouwstenen die nodig zijn om het ontwerp patroon te implementeren?
- Welke speciale overwegingen zijn er bij het gebruik van het Tool Use Design Pattern om betrouwbare AI-agenten te bouwen?

## Leerdoelen

Na het voltooien van deze les kun je:

- Het Tool Use Design Pattern definiëren en het doel ervan uitleggen.
- Gebruikssituaties identificeren waarbij het Tool Use Design Pattern toepasbaar is.
- De belangrijkste elementen begrijpen die nodig zijn om het ontwerp patroon te implementeren.
- Overwegingen herkennen voor het waarborgen van de betrouwbaarheid van AI-agenten die dit ontwerp patroon gebruiken.

## Wat is het Tool Use Design Pattern?

Het **Tool Use Design Pattern** richt zich op het geven van LLM’s de mogelijkheid om te interageren met externe tools om specifieke doelen te bereiken. Tools zijn code die door een agent kan worden uitgevoerd om handelingen te verrichten. Een tool kan een eenvoudige functie zijn, zoals een rekenmachine, of een API-aanroep naar een externe service zoals het opzoeken van aandelenkoersen of het weerbericht. In de context van AI-agenten zijn tools ontworpen om te worden uitgevoerd door agenten als reactie op **door het model gegenereerde functie-aanroepen**.

## Voor welke gebruikssituaties kan het worden toegepast?

AI-agenten kunnen tools gebruiken om complexe taken te voltooien, informatie op te halen of beslissingen te nemen. Het tool use design pattern wordt vaak toegepast in scenario’s die dynamische interactie met externe systemen vereisen, zoals databases, webservices of code-interpreters. Deze mogelijkheid is nuttig voor verschillende use-cases, waaronder:

- **Dynamische informatie-opvraging:** Agenten kunnen externe API’s of databases raadplegen om up-to-date data op te halen (bijv. een SQLite-database raadplegen voor data-analyse, aandelenkoersen of weersinformatie opvragen).
- **Code-uitvoering en -interpretatie:** Agenten kunnen code of scripts uitvoeren om wiskundige problemen op te lossen, rapporten te genereren of simulaties uit te voeren.
- **Workflow-automatisering:** Het automatiseren van repetitieve of multi-stap workflows door integratie van tools zoals taakplanners, e-maildiensten of datapijplijnen.
- **Klantenservice:** Agenten kunnen interacteren met CRM-systemen, ticketplatforms of kennisbanken om gebruikersvragen op te lossen.
- **Contentcreatie en -bewerking:** Agenten kunnen tools gebruiken zoals grammaticacontrole, tekstsamenvatting of contentveiligheidsevaluatoren om contentcreatietaken te ondersteunen.

## Wat zijn de elementen/bouwstenen die nodig zijn om het tool use design pattern te implementeren?

Deze bouwstenen stellen de AI-agent in staat om een breed scala aan taken uit te voeren. Laten we kijken naar de belangrijkste elementen die nodig zijn om het Tool Use Design Pattern te implementeren:

- **Functie-/Toolschemas**: Gedetailleerde definities van beschikbare tools, inclusief functienaam, doel, vereiste parameters en verwachte outputs. Deze schemas stellen het LLM in staat te begrijpen welke tools beschikbaar zijn en hoe geldige verzoeken worden opgebouwd.

- **Functie-uitvoeringslogica**: Bepaalt hoe en wanneer tools worden aangeroepen op basis van de intentie van de gebruiker en de conversatiecontext. Dit kan planner-modules, routeringsmechanismen of conditionele flows bevatten die het gebruik van tools dynamisch bepalen.

- **Berichtverwerkingssysteem**: Componenten die de gespreksstroom beheren tussen gebruikersinvoer, LLM-reacties, tool-aanroepen en tool-uitvoer.

- **Tool-integratiekader**: Infrastructuur die de agent verbindt met verschillende tools, of het nu eenvoudige functies zijn of complexe externe services.

- **Foutafhandeling & Validatie**: Mechanismen om fouten in tooluitvoering af te handelen, parameters te valideren en onverwachte reacties te beheren.

- **State Management**: Houdt de gesprekscontext, eerdere toolinteracties en persistente data bij om consistentie te waarborgen bij multi-turn interacties.

Laten we vervolgens in detail kijken naar functie-/tool-aanroepen.
 
### Functie-/Tool-aanroepen

Functie-aanroepen zijn de primaire manier waarop we grote taalmodellen (LLM’s) in staat stellen te interacteren met tools. Je zult vaak zien dat 'Functie' en 'Tool' door elkaar worden gebruikt, omdat 'functies' (herbruikbare codeblokken) de 'tools' zijn die agenten gebruiken om taken uit te voeren. Om de code van een functie aan te roepen, moet een LLM het verzoek van de gebruiker vergelijken met de omschrijving van de functies. Hiervoor wordt een schema met de beschrijvingen van alle beschikbare functies naar het LLM gestuurd. Het LLM selecteert vervolgens de meest geschikte functie voor de taak en geeft de naam en argumenten ervan terug. De geselecteerde functie wordt aangeroepen, de reactie wordt teruggestuurd naar het LLM, dat deze informatie gebruikt om te reageren op het verzoek van de gebruiker.

Voor ontwikkelaars die functie-aanroepen voor agenten willen implementeren, is het volgende nodig:

1. Een LLM-model dat functie-aanroepen ondersteunt
2. Een schema met functieomschrijvingen
3. De code voor elke beschreven functie

Laten we het voorbeeld van het opvragen van de huidige tijd in een stad gebruiken om dit te illustreren:

1. **Initialiseer een LLM die functie-aanroepen ondersteunt:**

    Niet alle modellen ondersteunen functie-aanroepen, dus het is belangrijk te controleren of het LLM dat je gebruikt dit wel doet. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> ondersteunt functie-aanroepen. We kunnen beginnen door de Azure OpenAI client te initialiseren.

    ```python
    # Initialiseer de Azure OpenAI-client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Maak een Functie Schema aan**:

    Vervolgens definiëren we een JSON-schema dat de functienaam bevat, een beschrijving van wat de functie doet, en de namen en beschrijvingen van de functieparameters.
    We geven dit schema door aan de eerder gemaakte client, samen met de gebruikersvraag om de tijd op te vragen in San Francisco. Belangrijk om op te merken is dat er een **tool call** wordt geretourneerd, **niet** het uiteindelijke antwoord op de vraag. Zoals eerder vermeld, geeft het LLM de naam van de functie die het voor de taak heeft geselecteerd terug, samen met de argumenten die eraan worden doorgegeven.

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
  
    # Eerste API-aanroep: Vraag het model om de functie te gebruiken
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Verwerk het antwoord van het model
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **De benodigde functiecode om de taak uit te voeren:**

    Nu dat het LLM heeft gekozen welke functie moet worden uitgevoerd, moet de code die de taak uitvoert worden geïmplementeerd en uitgevoerd.
    We kunnen de code om de huidige tijd op te halen in Python implementeren. We moeten ook code schrijven om de naam en argumenten uit het response_message te extraheren om het eindresultaat te verkrijgen.

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
     # Behandel functieaanroepen
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

Functie-aanroepen vormen de kern van het merendeel, zo niet alle agent tool use design patronen, maar het implementeren ervan vanaf nul kan soms uitdagend zijn.
Zoals we leerden in [Les 2](../../../02-explore-agentic-frameworks) bieden agentic frameworks kant-en-klare bouwstenen om tool gebruik te implementeren.
 
## Tool Use Voorbeelden met Agentic Frameworks

Hier zijn enkele voorbeelden van hoe je het Tool Use Design Pattern kunt toepassen met verschillende agentic frameworks:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> is een open-source AI-framework voor het bouwen van AI-agenten. Het vereenvoudigt het gebruik van functie-aanroepen door je toe te staan tools te definiëren als Python-functies met de `@tool` decorator. Het framework regelt de communicatie tussen het model en je code. Het biedt ook toegang tot kant-en-klare tools zoals File Search en Code Interpreter via de `AzureAIProjectAgentProvider`.

Het volgende diagram illustreert het proces van functie-aanroepen met het Microsoft Agent Framework:

![function calling](../../../translated_images/nl/functioncalling-diagram.a84006fc287f6014.webp)

In het Microsoft Agent Framework worden tools gedefinieerd als gedecoreerde functies. We kunnen de `get_current_time` functie die we eerder zagen omzetten in een tool door de `@tool` decorator te gebruiken. Het framework zal automatisch de functie en zijn parameters serialiseren en het schema creëren om naar het LLM te sturen.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Maak de client aan
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Maak een agent aan en voer deze uit met de tool
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> is een nieuwere agentic framework dat is ontworpen om ontwikkelaars in staat te stellen veilig hoogwaardige en uitbreidbare AI-agenten te bouwen, te implementeren en op te schalen zonder dat ze de onderliggende compute- en opslagresources hoeven te beheren. Het is met name nuttig voor enterprise toepassingen omdat het een volledig beheerde dienst met enterprise-grade beveiliging is.

Vergeleken met het direct ontwikkelen met de LLM API, biedt Azure AI Agent Service enkele voordelen, waaronder:

- Automatische tool-aanroepen – geen noodzaak om een tool-aanroep te parsen, de tool aan te roepen en de respons te verwerken; dit wordt nu server-side afgehandeld
- Veilig beheerde data – in plaats van zelf de conversatiestatus te beheren, kun je vertrouwen op threads om alle benodigde informatie op te slaan
- Klaar-voor-gebruik tools – tools die je kunt gebruiken om met je databronnen te interacteren, zoals Bing, Azure AI Search en Azure Functions.

De tools die beschikbaar zijn in Azure AI Agent Service kunnen in twee categorieën worden verdeeld:

1. Kennis Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Verankering met Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Bestandszoeker</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Actie Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Functie-aanroepen</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI gedefinieerde tools</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

De Agent Service maakt het mogelijk om deze tools samen te gebruiken als een `toolset`. Het maakt ook gebruik van `threads` die de historie van berichten van een bepaald gesprek bijhouden.

Stel je voor dat je een salesagent bent bij een bedrijf genaamd Contoso. Je wilt een conversatie-agent ontwikkelen die vragen over je verkoopdata kan beantwoorden.

De volgende afbeelding illustreert hoe je Azure AI Agent Service kunt gebruiken om je verkoopdata te analyseren:

![Agentic Service In Action](../../../translated_images/nl/agent-service-in-action.34fb465c9a84659e.webp)

Om een van deze tools met de service te gebruiken, kunnen we een client aanmaken en een tool of toolset definiëren. Om dit praktisch te implementeren gebruiken we de volgende Python-code. Het LLM kan naar de toolset kijken en beslissen of het de door de gebruiker gemaakte functie `fetch_sales_data_using_sqlite_query` gebruikt of de kant-en-klare Code Interpreter, afhankelijk van het gebruikersverzoek.

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

# Initialiseer gereedschapsset
toolset = ToolSet()

# Initialiseer functie aanroep agent met de fetch_sales_data_using_sqlite_query functie en voeg deze toe aan de gereedschapsset
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Initialiseer Code Interpreter gereedschap en voeg deze toe aan de gereedschapsset.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Welke speciale overwegingen zijn er bij het gebruik van het Tool Use Design Pattern om betrouwbare AI-agenten te bouwen?

Een veelvoorkomende zorg bij door LLM’s dynamisch gegenereerde SQL is veiligheid, met name het risico op SQL-injectie of kwaadaardige acties zoals het verwijderen of manipuleren van de database. Hoewel deze zorgen terecht zijn, kunnen ze effectief worden gemitigeerd door de juiste configuratie van database toegangsrechten. Voor de meeste databases betekent dit het configureren van de database als alleen-lezen. Voor databaseservices zoals PostgreSQL of Azure SQL moet de applicatie een alleen-lezen (SELECT) rol toegewezen krijgen.

Het uitvoeren van de app in een veilige omgeving versterkt de bescherming verder. In enterprise-scenario’s worden gegevens meestal geëxtraheerd en getransformeerd uit operationele systemen naar een alleen-lezen database of datawarehouse met een gebruiksvriendelijk schema. Deze aanpak zorgt ervoor dat de data veilig is, geoptimaliseerd voor prestaties en toegankelijkheid, en dat de app beperkte, alleen-lezen toegang heeft.

## Voorbeeldcodes

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Meer vragen over het Tool Use Design Pattern?

Word lid van de [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) om in contact te komen met andere leerlingen, kantooruren bij te wonen en je vragen over AI-agenten beantwoord te krijgen.

## Aanvullende bronnen

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework Overzicht</a>

## Vorige les

[Begrijpen van Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## Volgende les
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat automatische vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de originele taal moet als gezaghebbende bron worden beschouwd. Voor essentiële informatie wordt een professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor enige misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->