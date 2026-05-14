[![Hoe Ontwerp je Goede AI Agents](../../../translated_images/nl/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klik op de afbeelding hierboven om de video van deze les te bekijken)_

# Ontwerp Patroon voor Gereedschap Gebruik

Gereedschappen zijn interessant omdat ze AI-agenten een bredere reeks mogelijkheden geven. In plaats van dat de agent een beperkte set acties kan uitvoeren, kan de agent door het toevoegen van een gereedschap nu een breed scala aan acties uitvoeren. In dit hoofdstuk bekijken we het Ontwerp Patroon voor Gereedschap Gebruik, dat beschrijft hoe AI-agenten specifieke gereedschappen kunnen gebruiken om hun doelen te bereiken.

## Introductie

In deze les willen we de volgende vragen beantwoorden:

- Wat is het ontwerp patroon voor gereedschap gebruik?
- Voor welke toepassingsgevallen kan het worden toegepast?
- Wat zijn de elementen/bouwstenen die nodig zijn om het ontwerp patroon te implementeren?
- Wat zijn de bijzondere overwegingen bij het gebruik van het Ontwerp Patroon voor Gereedschap Gebruik om betrouwbare AI-agenten te bouwen?

## Leerdoelen

Na het afronden van deze les kun je:

- Het Ontwerp Patroon voor Gereedschap Gebruik en het doel ervan definiëren.
- Toepassingsgevallen identificeren waar het Ontwerp Patroon voor Gereedschap Gebruik toepasbaar is.
- De belangrijkste elementen begrijpen die nodig zijn om het ontwerp patroon te implementeren.
- Overwegingen herkennen voor het waarborgen van betrouwbaarheid in AI-agenten die dit ontwerp patroon gebruiken.

## Wat is het Ontwerp Patroon voor Gereedschap Gebruik?

Het **Ontwerp Patroon voor Gereedschap Gebruik** richt zich op het geven van de mogelijkheid aan LLM's om te interacteren met externe gereedschappen om specifieke doelen te bereiken. Gereedschappen zijn code die door een agent kan worden uitgevoerd om acties uit te voeren. Een gereedschap kan een eenvoudige functie zijn zoals een rekenmachine, of een API-aanroep naar een dienst van derden zoals het opzoeken van aandelenkoersen of het weerbericht. In de context van AI-agenten zijn gereedschappen ontworpen om te worden uitgevoerd door agenten als reactie op **door het model gegenereerde functieverzoeken**.

## Voor welke toepassingsgevallen kan het worden toegepast?

AI-agenten kunnen gereedschappen gebruiken om complexe taken te voltooien, informatie op te halen of beslissingen te nemen. Het ontwerp patroon voor gereedschap gebruik wordt vaak toegepast in scenario's die dynamische interactie met externe systemen vereisen, zoals databases, webservices of code-interpreters. Deze mogelijkheid is nuttig voor een aantal verschillende toepassingsgevallen, waaronder:

- **Dynamische Informatieverzameling:** Agenten kunnen externe API's of databases raadplegen om up-to-date gegevens op te halen (bijv. het raadplegen van een SQLite database voor data-analyse, het ophalen van aandelenkoersen of weersinformatie).
- **Code Uitvoering en Interpretatie:** Agenten kunnen code of scripts uitvoeren om wiskundige problemen op te lossen, rapporten te genereren of simulaties uit te voeren.
- **Workflow Automatisering:** Het automatiseren van repetitieve of multi-staps workflows door het integreren van gereedschappen zoals taakplanners, e-maildiensten of datapijplijnen.
- **Klantenondersteuning:** Agenten kunnen interacteren met CRM-systemen, ticketingsystemen of kennisbanken om gebruikersvragen op te lossen.
- **Contentcreatie en Bewerking:** Agenten kunnen gebruikmaken van gereedschappen zoals grammatica-controleurs, tekstsamenvatters of contentveiligheidsevaluators om te helpen bij contentcreatietaken.

## Wat zijn de elementen/bouwstenen die nodig zijn om het ontwerp patroon voor gereedschap gebruik te implementeren?

Deze bouwstenen stellen de AI-agent in staat een breed scala van taken uit te voeren. Laten we de belangrijkste elementen bekijken die nodig zijn om het Ontwerp Patroon voor Gereedschap Gebruik te implementeren:

- **Functie/Gereedschap Schema's**: Gedetailleerde definities van beschikbare gereedschappen, inclusief functienaam, doel, vereiste parameters en verwachte outputs. Deze schema's maken het LLM mogelijk te begrijpen welke gereedschappen beschikbaar zijn en hoe geldige verzoeken te construeren.

- **Functie Uitvoeringslogica**: Bepaalt hoe en wanneer gereedschappen worden aangeroepen op basis van de intentie van de gebruiker en de context van het gesprek. Dit kan onder meer planner-modules, routeringsmechanismen of conditionele stromen omvatten die het gereedschap gebruik dynamisch bepalen.

- **Berichten Afhandelingssysteem**: Componenten die de conversatiestroom beheren tussen gebruikersinvoer, LLM-reacties, gereedschapsoproepen en gereedschapsuitvoer.

- **Gereedschap Integratie Framework**: Infrastructuur die de agent verbindt met diverse gereedschappen, of dit nu eenvoudige functies of complexe externe diensten zijn.

- **Foutafhandeling & Validatie**: Mechanismen om fouten bij gereedschapsuitvoering af te handelen, parameters te valideren en onverwachte reacties te beheren.

- **Statusbeheer**: Houdt de gesprekcontext, eerdere gereedschapsinteracties en persistente data bij om consistentie over meerdere gespreksturns te waarborgen.

Vervolgens bekijken we Functie-/Gereedschapsoproep nader.

### Functie-/Gereedschapsoproep

Functieoproep is de primaire manier waarop we Large Language Models (LLM's) in staat stellen te interacteren met gereedschappen. Je zult vaak zien dat 'Functie' en 'Gereedschap' door elkaar worden gebruikt omdat 'functies' (herbruikbare codeblokken) de 'gereedschappen' zijn die agenten gebruiken om taken uit te voeren. Om de code van een functie aan te roepen, moet een LLM de gebruikersvraag vergelijken met de functiebeschrijving. Hiervoor wordt een schema met beschrijvingen van alle beschikbare functies naar het LLM gestuurd. Het LLM selecteert vervolgens de meest geschikte functie voor de taak en retourneert de naam en argumenten. De geselecteerde functie wordt aangeroepen, het antwoord wordt teruggestuurd naar het LLM, dat deze informatie gebruikt om te reageren op de gebruikersvraag.

Voor ontwikkelaars die functieoproepen voor agenten willen implementeren, zijn nodig:

1. Een LLM-model dat functieoproepen ondersteunt
2. Een schema met functiebeschrijvingen
3. De code voor elke beschreven functie

Laten we het voorbeeld gebruiken van het opvragen van de huidige tijd in een stad om dit te illustreren:

1. **Initialiseer een LLM die functieoproepen ondersteunt:**

    Niet alle modellen ondersteunen functieoproepen, dus het is belangrijk te controleren of het LLM dat je gebruikt dit doet. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> ondersteunt functieoproepen. We kunnen beginnen met het initialiseren van de Azure OpenAI-client. 

    ```python
    # Initialiseer de Azure OpenAI-client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Maak een Functie Schema**:

    Vervolgens definiëren we een JSON-schema dat de functienaam bevat, de beschrijving van wat de functie doet, en de namen en beschrijvingen van de functieparameters.
    We geven dit schema door aan de eerder aangemaakte client, samen met de gebruikersvraag om de tijd in San Francisco te vinden. Wat belangrijk is om op te merken, is dat een **gereedschapsoproep** wordt geretourneerd, **niet** het definitieve antwoord op de vraag. Zoals eerder vermeld geeft het LLM de naam van de geselecteerde functie en de argumenten die eraan doorgegeven worden.

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
  
    # Initiële gebruikersboodschap
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Eerste API-aanroep: Vraag het model de functie te gebruiken
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
  
1. **De functicode die nodig is om de taak uit te voeren:**

    Nu het LLM heeft gekozen welke functie moet worden uitgevoerd, moet de code die de taak uitvoert geïmplementeerd en uitgevoerd worden.
    We kunnen de code implementeren om de huidige tijd op te halen in Python. We moeten ook de code schrijven om de naam en argumenten uit het response_message te extraheren om het eindresultaat te krijgen.

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
     # Afhandeling van functieverzoeken
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
  
      # Tweede API-aanroep: Krijg de definitieve reactie van het model
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

Functieoproep staat centraal in de meeste, zo niet alle ontwerpen voor gereedschap gebruik door agenten, maar het kan soms uitdagend zijn om het zelf te implementeren.
Zoals we hebben geleerd in [Les 2](../../../02-explore-agentic-frameworks) bieden agentische frameworks kant-en-klare bouwstenen om gereedschap gebruik te implementeren.
 
## Voorbeelden van Gereedschap Gebruik met Agentische Frameworks

Hier zijn enkele voorbeelden van hoe je het Ontwerp Patroon voor Gereedschap Gebruik kunt implementeren met verschillende agentische frameworks:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> is een open-source AI-framework voor het bouwen van AI-agenten. Het vereenvoudigt het gebruik van functieoproepen door je toe te staan gereedschappen te definiëren als Python-functies met de `@tool` decorator. Het framework regelt de communicatie tussen het model en je code heen en weer. Het biedt ook toegang tot vooraf gebouwde gereedschappen zoals Bestandzoeker en Code Interpreter via de `AzureAIProjectAgentProvider`.

Het volgende diagram illustreert het proces van functieoproepen met het Microsoft Agent Framework:

![function calling](../../../translated_images/nl/functioncalling-diagram.a84006fc287f6014.webp)

In het Microsoft Agent Framework worden gereedschappen gedefinieerd als gedecoreerde functies. We kunnen de eerder geziene `get_current_time` functie omzetten naar een gereedschap door gebruik te maken van de `@tool` decorator. Het framework serialiseert automatisch de functie en de parameters, en creëert het schema om naar het LLM te sturen.

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

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> is een nieuwer agentisch framework dat is ontworpen om ontwikkelaars in staat te stellen veilig hoogwaardige, schaalbare en uitbreidbare AI-agenten te bouwen zonder dat ze de onderliggende compute- en opslagresources hoeven te beheren. Het is bijzonder nuttig voor enterprise toepassingen omdat het een volledig beheerde service met enterprise-grade beveiliging is.

Vergeleken met directe ontwikkeling met de LLM API biedt Azure AI Agent Service enkele voordelen, waaronder:

- Automatische gereedschapsoproepen – geen noodzaak om een gereedschapsoproep te parseren, het gereedschap aan te roepen en de reactie af te handelen; dit gebeurt nu server-side
- Veilig beheerde data – in plaats van eigen gespreksstatus te beheren, kun je vertrouwen op threads om alle benodigde informatie op te slaan
- Gereedschappen klaar voor gebruik – Gereedschappen die je kunt gebruiken om te interacteren met je data bronnen, zoals Bing, Azure AI Search en Azure Functions.

De gereedschappen die beschikbaar zijn in Azure AI Agent Service kunnen worden onderverdeeld in twee categorieën:

1. Kennisgereedschappen:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Verankering met Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Bestandzoeker</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Actiegereedschappen:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Functieoproep</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI gedefinieerde gereedschappen</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

De Agent Service stelt ons in staat deze gereedschappen samen te gebruiken als een `toolset`. Het maakt ook gebruik van `threads` die de geschiedenis van berichten van een specifieke conversatie bijhouden.

Stel je bent een verkoopagent bij een bedrijf genaamd Contoso. Je wilt een conversatie-agent ontwikkelen die vragen over je verkoopdata kan beantwoorden.

De volgende afbeelding illustreert hoe je Azure AI Agent Service kunt gebruiken om je verkoopdata te analyseren:

![Agentic Service In Action](../../../translated_images/nl/agent-service-in-action.34fb465c9a84659e.webp)

Om een van deze gereedschappen met de service te gebruiken, kunnen we een client maken en een gereedschap of toolset definiëren. Om dit praktisch te implementeren kunnen we onderstaande Python-code gebruiken. Het LLM kan naar de toolset kijken en beslissen of het de door een gebruiker gemaakte functie, `fetch_sales_data_using_sqlite_query`, of de kant-en-klare Code Interpreter zal gebruiken afhankelijk van het verzoek van de gebruiker.

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

# Initialiseer Code Interpreter gereedschap en voeg het toe aan de gereedschapsset.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Wat zijn de bijzondere overwegingen bij het gebruik van het Ontwerp Patroon voor Gereedschap Gebruik om betrouwbare AI-agenten te bouwen?

Een veelgehoorde zorg bij dynamisch door LLMs gegenereerde SQL is beveiliging, met name het risico op SQL-injectie of kwaadaardige acties zoals het verwijderen of manipuleren van de database. Hoewel deze zorgen terecht zijn, kunnen ze effectief worden beperkt door database toegangsrechten correct te configureren. Voor de meeste databases betekent dit het configureren van de database als alleen-lezen. Voor databaseservices zoals PostgreSQL of Azure SQL moet de app een alleen-lezen (SELECT) rol krijgen toegewezen.

Het draaien van de app in een beveiligde omgeving versterkt de bescherming verder. In zakelijke scenario's wordt data meestal geëxtraheerd en getransformeerd uit operationele systemen naar een alleen-lezen database of datawarehouse met een gebruiksvriendelijk schema. Deze aanpak zorgt ervoor dat de data veilig is, geoptimaliseerd voor prestaties en toegankelijkheid, en dat de app beperkte, alleen-lezen toegang heeft.

## Voorbeeldcodes

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Meer Vragen over het Ontwerp Patroon voor Gereedschap Gebruik?

Word lid van de [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) om andere leerlingen te ontmoeten, deel te nemen aan office hours en je vragen over AI Agents beantwoord te krijgen.

## Aanvullende Bronnen

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework Overzicht</a>

## Vorige Les

[Begrip van Agentische Ontwerppatronen](../03-agentic-design-patterns/README.md)

## Volgende Les
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->