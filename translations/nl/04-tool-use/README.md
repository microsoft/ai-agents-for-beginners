[![Hoe Ontwerp je Goede AI-Agenten](../../../translated_images/nl/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klik op de afbeelding hierboven om de video van deze les te bekijken)_

# Tool Gebruik Ontwerppatroon

Tools zijn interessant omdat ze AI-agenten een breder scala aan mogelijkheden bieden. In plaats van dat de agent een beperkte set acties kan uitvoeren, kan de agent door het toevoegen van een tool nu een breed scala aan acties uitvoeren. In dit hoofdstuk bekijken we het Tool Gebruik Ontwerppatroon, dat beschrijft hoe AI-agenten specifieke tools kunnen gebruiken om hun doelen te bereiken.

## Introductie

In deze les willen we de volgende vragen beantwoorden:

- Wat is het tool gebruik ontwerppatroon?
- Op welke toepassingsgevallen kan het worden toegepast?
- Wat zijn de elementen/bouwstenen die nodig zijn om het ontwerppatroon te implementeren?
- Wat zijn de speciale overwegingen bij het gebruik van het Tool Gebruik Ontwerppatroon om betrouwbare AI-agenten te bouwen?

## Leerdoelen

Na het voltooien van deze les kun je:

- Het Tool Gebruik Ontwerppatroon definiëren en het doel ervan begrijpen.
- Toepassingsgevallen identificeren waarin het Tool Gebruik Ontwerppatroon van toepassing is.
- De belangrijkste elementen begrijpen die nodig zijn om het ontwerppatroon te implementeren.
- Overwegingen herkennen om betrouwbaarheid te waarborgen in AI-agenten die dit ontwerppatroon gebruiken.

## Wat is het Tool Gebruik Ontwerppatroon?

Het **Tool Gebruik Ontwerppatroon** richt zich op het geven van LLM's de mogelijkheid om te interageren met externe tools om specifieke doelen te bereiken. Tools zijn code die door een agent kan worden uitgevoerd om acties uit te voeren. Een tool kan een eenvoudige functie zijn zoals een rekenmachine, of een API-aanroep naar een externe service zoals aandelenkoersen of weersvoorspellingen. In de context van AI-agenten zijn tools ontworpen om door agenten te worden uitgevoerd als reactie op **modelgegenereerde functieaanroepen**.

## Voor welke toepassingen kan het worden gebruikt?

AI-agenten kunnen tools benutten om complexe taken te voltooien, informatie op te halen of beslissingen te nemen. Het tool gebruik ontwerppatroon wordt vaak gebruikt in scenario's die dynamische interactie met externe systemen vereisen, zoals databases, webdiensten of code-interpreters. Deze mogelijkheid is nuttig voor verschillende toepassingsgevallen, waaronder:

- **Dynamische Informatieopvraging:** Agenten kunnen externe API's of databases raadplegen om actuele gegevens op te halen (bijv. het raadplegen van een SQLite-database voor data-analyse, het ophalen van aandelenkoersen of weersinformatie).
- **Code-uitvoering en interpretatie:** Agenten kunnen code of scripts uitvoeren om wiskundige problemen op te lossen, rapporten te genereren of simulaties uit te voeren.
- **Workflow Automatisering:** Het automatiseren van repetitieve of meerstapswerkstromen door tools zoals taakplanners, e-maildiensten of datapijplijnen te integreren.
- **Klantenondersteuning:** Agenten kunnen interageren met CRM-systemen, ticketsystemen of kennisbanken om gebruikersvragen op te lossen.
- **Contentgeneratie en -bewerking:** Agenten kunnen tools gebruiken zoals grammaticacontroleurs, tekstsamenvatters of contentveiligheidsbeoordelaars om te assisteren bij contentcreatie taken.

## Wat zijn de elementen/bouwstenen die nodig zijn om het tool gebruik ontwerppatroon te implementeren?

Deze bouwstenen stellen de AI-agent in staat om een breed scala aan taken uit te voeren. Laten we de belangrijkste elementen bekijken die nodig zijn om het Tool Gebruik Ontwerppatroon te implementeren:

- **Functie/Tool Schema's**: Gedetailleerde definities van beschikbare tools, inclusief functienaam, doel, vereiste parameters en verwachte outputs. Deze schema's stellen de LLM in staat te begrijpen welke tools beschikbaar zijn en hoe geldige verzoeken te construeren.

- **Functie Uitvoeringslogica**: Regelt hoe en wanneer tools worden aangeroepen op basis van de intentie van de gebruiker en de context van het gesprek. Dit kan planner modules, routeringsmechanismen of conditionele stromen omvatten die het gebruik van tools dynamisch bepalen.

- **Berichtenafhandelingssysteem**: Componenten die de conversatiestroom beheren tussen gebruikersinvoer, LLM-reacties, tool-aanroepen en tool-uitvoer.

- **Tool Integratiekader**: Infrastructuur die de agent verbindt met verschillende tools, of het nu eenvoudige functies of complexe externe services zijn.

- **Foutafhandeling & Validatie**: Mechanismen om falen in tooluitvoering af te handelen, parameters te valideren en onverwachte reacties te beheren.

- **Statusbeheer**: Houdt de gesprekscontext, eerdere toolinteracties en persistente gegevens bij om consistentie te waarborgen over meerledige interacties.

Laten we nu Functie-/Toolaanroepen iets nader bekijken.
 
### Functie-/Toolaanroepen

Functieaanroepen zijn de primaire manier waarop we Large Language Models (LLM's) in staat stellen te interageren met tools. Je zult vaak 'Functie' en 'Tool' door elkaar gebruikt zien omdat 'functies' (herbruikbare codeblokken) de 'tools' zijn die agenten gebruiken om taken uit te voeren. Om de code van een functie aan te roepen, moet een LLM het verzoek van de gebruiker vergelijken met de beschrijving van de functies. Hiervoor wordt een schema met de beschrijvingen van alle beschikbare functies naar de LLM gestuurd. De LLM selecteert de meest geschikte functie voor de taak en retourneert de naam en argumenten ervan. De geselecteerde functie wordt aangeroepen, het antwoord wordt teruggestuurd naar de LLM, die deze informatie gebruikt om te reageren op het verzoek van de gebruiker.

Voor ontwikkelaars die functieaanroepen voor agenten willen implementeren, heb je nodig:

1. Een LLM-model dat functieaanroepen ondersteunt
2. Een schema met functiebeschrijvingen
3. De code voor elke beschreven functie

Laten we het voorbeeld gebruiken van het opvragen van de huidige tijd in een stad ter illustratie:

1. **Initialiseer een LLM die functieaanroepen ondersteunt:**

    Niet alle modellen ondersteunen functieaanroepen, dus het is belangrijk te controleren of de LLM die je gebruikt dat doet.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> ondersteunt functieaanroepen. We kunnen starten met het initiëren van de OpenAI-client tegen de Azure OpenAI **Responses API** (de stabiele `/openai/v1/` endpoint — geen `api_version` nodig). 

    ```python
    # Initialiseer de OpenAI-client voor Azure OpenAI (Responses API, v1-eindpunt)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Maak een Functie Schema**:

    Vervolgens definiëren we een JSON-schema dat de functienaam bevat, een beschrijving van wat de functie doet, en de namen en beschrijvingen van de functieparameters.
    We zullen dit schema vervolgens aan de eerder aangemaakte client doorgeven, samen met het gebruikersverzoek om de tijd in San Francisco te vinden. Wat belangrijk is om te weten, is dat er een **toolaanroep** wordt geretourneerd, **niet** het definitieve antwoord op de vraag. Zoals eerder vermeld retourneert de LLM de naam van de functie die hij voor de taak heeft geselecteerd en de argumenten die aan die functie worden doorgegeven.

    ```python
    # Functiebeschrijving voor het model om te lezen (Responses API vlak gereedschapsformaat)
    tools = [
        {
            "type": "function",
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
    ]
    ```
   
    ```python
  
    # Initiële gebruikersboodschap
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # Eerste API-aanroep: Vraag het model om de functie te gebruiken
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # De Responses API retourneert tool-aanroepen als function_call-items in response.output.
    # Voeg ze toe aan het gesprek zodat het model de volledige context heeft bij de volgende beurt.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **De functicode die nodig is om de taak uit te voeren:**

    Nu de LLM heeft gekozen welke functie moet worden uitgevoerd, moet de code die de taak uitvoert worden geïmplementeerd en uitgevoerd.
    We kunnen de code om de huidige tijd op te halen in Python implementeren. We moeten ook code schrijven om de naam en argumenten uit het response_message te halen om het uiteindelijke resultaat te krijgen.

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
    # Verwerk functieaanroepen
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # Retourneer het gereedschapsresultaat als een functie_aanroep_uitvoer item
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # Tweede API-aanroep: Krijg de definitieve reactie van het model
    final_response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        store=False,
    )

    return final_response.output_text
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

Functieaanroepen vormen de kern van de meeste, zo niet alle agent-tool gebruik ontwerpen, maar de implementatie ervan helemaal zelf maken kan soms uitdagend zijn.
Zoals geleerd in [Les 2](../../../02-explore-agentic-frameworks) bieden agentische frameworks kant-en-klare bouwstenen voor toolgebruik.
 
## Tool Gebruik Voorbeelden met Agentische Frameworks

Hier zijn enkele voorbeelden van hoe je het Tool Gebruik Ontwerppatroon kunt implementeren met verschillende agentische frameworks:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> is een open-source AI-framework voor het bouwen van AI-agenten. Het vereenvoudigt het proces van functieaanroepen door je toe te staan tools te definiëren als Python-functies met de `@tool` decorator. Het framework verzorgt de communicatie heen en weer tussen het model en je code. Daarnaast biedt het toegang tot kant-en-klare tools zoals Bestandzoeken en Code Interpreter via `FoundryChatClient`.

Het volgende diagram illustreert het proces van functieaanroepen met het Microsoft Agent Framework:

![functieaanroepen](../../../translated_images/nl/functioncalling-diagram.a84006fc287f6014.webp)

In het Microsoft Agent Framework worden tools gedefinieerd als gedecoreerde functies. We kunnen de functie `get_current_time` die we eerder zagen omzetten in een tool door de `@tool` decorator te gebruiken. Het framework zal automatisch de functie en de parameters serialiseren, waardoor het schema wordt gemaakt dat naar de LLM wordt gestuurd.

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Maak de client aan
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Maak een agent aan en voer deze uit met het hulpmiddel
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> is een nieuwer agentisch framework dat is ontworpen om ontwikkelaars in staat te stellen veilig hoogwaardige, uitbreidbare AI-agenten te bouwen, implementeren en schalen zonder dat zij de onderliggende reken- en opslagmiddelen hoeven te beheren. Het is vooral nuttig voor bedrijfsapplicaties doordat het een volledig beheerste service is met beveiliging op ondernemingsniveau.

Vergeleken met ontwikkeling met de LLM API direct biedt Microsoft Foundry Agent Service enkele voordelen, waaronder:

- Automatische functieaanroepen – geen noodzaak om een toolaanroep te ontleden, de tool aan te roepen en het antwoord af te handelen; dit wordt nu server-side afgehandeld
- Beveiligd beheerde data – in plaats van zelf de gespreksstatus te beheren, kun je vertrouwen op threads die alle benodigde informatie bewaren
- Kant-en-klare tools – tools die je kunt gebruiken om met je databronnen te interacteren, zoals Bing, Azure AI Search en Azure Functions.

De beschikbare tools in Microsoft Foundry Agent Service zijn onder te verdelen in twee categorieën:

1. Kennis Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Aansluiting met Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Bestandszoekfunctie</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Actie Tools:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Functieaanroepen</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI gedefinieerde tools</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

De Agent Service stelt ons in staat deze tools gezamenlijk als een `toolset` te gebruiken. Het maakt ook gebruik van `threads` die de geschiedenis van berichten uit een specifiek gesprek bijhouden.

Stel je voor dat je een verkoopagent bent bij een bedrijf genaamd Contoso. Je wilt een conversatie-agent ontwikkelen die vragen over je verkoopgegevens kan beantwoorden.

De volgende afbeelding illustreert hoe je Microsoft Foundry Agent Service zou kunnen gebruiken om je verkoopgegevens te analyseren:

![Agentiedienst in Actie](../../../translated_images/nl/agent-service-in-action.34fb465c9a84659e.webp)

Om een van deze tools met de service te gebruiken, kunnen we een client aanmaken en een tool of toolset definiëren. Om dit praktisch te implementeren kunnen we de volgende Python-code gebruiken. De LLM kan dan kijken naar de toolset en besluiten of hij de door de gebruiker gemaakte functie `fetch_sales_data_using_sqlite_query` gebruikt, of de kant-en-klare Code Interpreter, afhankelijk van de gebruikersvraag.

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

# Initialiseer function calling agent met de fetch_sales_data_using_sqlite_query functie en voeg deze toe aan de toolset
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Initialiseer Code Interpreter tool en voeg deze toe aan de toolset.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Wat zijn de speciale overwegingen bij het gebruik van het Tool Gebruik Ontwerppatroon om betrouwbare AI-agenten te bouwen?

Een veelvoorkomende zorg bij dynamisch door LLM's gegenereerde SQL is de veiligheid, met name het risico op SQL-injectie of kwaadaardige acties zoals het verwijderen of manipuleren van de database. Hoewel deze zorgen terecht zijn, kunnen ze effectief worden verminderd door de toegangsrechten van de database correct te configureren. Voor de meeste databases houdt dit in dat de database als alleen-lezen wordt ingesteld. Voor databaseservices zoals PostgreSQL of Azure SQL moet de app een alleen-lezen (SELECT) rol toegewezen krijgen.

Het draaien van de app in een veilige omgeving verhoogt de bescherming nog verder. In bedrijfsscenario's worden gegevens doorgaans extraheerd en getransformeerd vanuit operationele systemen naar een alleen-lezen database of datawarehouse met een gebruiksvriendelijk schema. Deze aanpak zorgt ervoor dat de data veilig, geoptimaliseerd voor prestaties en toegankelijkheid is, en dat de app beperkte, alleen-lezen toegang heeft.

## Voorbeeldcodes

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Meer vragen over het Tool Gebruik Ontwerppatroon?

Sluit je aan bij de [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) om andere leerlingen te ontmoeten, kantooruren bij te wonen en je vragen over AI-agenten beantwoord te krijgen.

## Aanvullende bronnen

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework Overzicht</a>


## Deze Agent Smoke-Testen (Optioneel)

Nadat je hebt geleerd om agents te implementeren in [Les 16](../16-deploying-scalable-agents/README.md), kun je deze les zijn `TravelToolAgent` smoke-testen (roept hij nog steeds zijn tools aan en antwoordt hij?) met [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json). Zie [`tests/README.md`](../tests/README.md) voor hoe je het kunt uitvoeren.

## Vorige Les

[Begrip van Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## Volgende Les

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->