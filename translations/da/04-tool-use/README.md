<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7c3b7bd1b3528074d8b6a7c5ad33b6f",
  "translation_date": "2025-11-18T17:40:51+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "da"
}
-->
[![Sådan designer man gode AI-agenter](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.da.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klik på billedet ovenfor for at se videoen til denne lektion)_

# Designmønster for værktøjsbrug

Værktøjer er interessante, fordi de giver AI-agenter mulighed for at have et bredere udvalg af funktioner. I stedet for at agenten kun har et begrænset sæt handlinger, den kan udføre, kan den med et værktøj udføre en lang række handlinger. I dette kapitel vil vi se på designmønsteret for værktøjsbrug, som beskriver, hvordan AI-agenter kan bruge specifikke værktøjer til at nå deres mål.

## Introduktion

I denne lektion vil vi forsøge at besvare følgende spørgsmål:

- Hvad er designmønsteret for værktøjsbrug?
- Hvilke anvendelsesområder kan det bruges til?
- Hvilke elementer/byggesten er nødvendige for at implementere designmønsteret?
- Hvilke særlige overvejelser er der ved brug af designmønsteret for værktøjsbrug til at bygge pålidelige AI-agenter?

## Læringsmål

Efter at have gennemført denne lektion vil du kunne:

- Definere designmønsteret for værktøjsbrug og dets formål.
- Identificere anvendelsesområder, hvor designmønsteret for værktøjsbrug er relevant.
- Forstå de nøgleelementer, der er nødvendige for at implementere designmønsteret.
- Genkende overvejelser for at sikre pålidelighed i AI-agenter, der bruger dette designmønster.

## Hvad er designmønsteret for værktøjsbrug?

**Designmønsteret for værktøjsbrug** fokuserer på at give LLM'er mulighed for at interagere med eksterne værktøjer for at opnå specifikke mål. Værktøjer er kode, der kan udføres af en agent for at udføre handlinger. Et værktøj kan være en simpel funktion som en lommeregner eller et API-kald til en tredjepartstjeneste som f.eks. aktiekursopslag eller vejrudsigter. I AI-agenters kontekst er værktøjer designet til at blive udført af agenter som svar på **modelgenererede funktionskald**.

## Hvilke anvendelsesområder kan det bruges til?

AI-agenter kan udnytte værktøjer til at udføre komplekse opgaver, hente information eller træffe beslutninger. Designmønsteret for værktøjsbrug anvendes ofte i scenarier, der kræver dynamisk interaktion med eksterne systemer, såsom databaser, webtjenester eller kodefortolkere. Denne evne er nyttig i en række forskellige anvendelsesområder, herunder:

- **Dynamisk informationshentning:** Agenter kan forespørge eksterne API'er eller databaser for at hente opdaterede data (f.eks. forespørge en SQLite-database for dataanalyse, hente aktiekurser eller vejrinformation).
- **Kodeudførelse og fortolkning:** Agenter kan udføre kode eller scripts for at løse matematiske problemer, generere rapporter eller udføre simuleringer.
- **Automatisering af arbejdsgange:** Automatisering af gentagne eller flertrins arbejdsgange ved at integrere værktøjer som opgaveplanlæggere, e-mail-tjenester eller datapipelines.
- **Kundesupport:** Agenter kan interagere med CRM-systemer, ticketing-platforme eller vidensbaser for at løse brugerforespørgsler.
- **Indholdsgenerering og redigering:** Agenter kan udnytte værktøjer som grammatikcheckere, tekstsammenfatningsværktøjer eller indholdssikkerhedsvurderinger til at hjælpe med indholdsskabelse.

## Hvilke elementer/byggesten er nødvendige for at implementere designmønsteret for værktøjsbrug?

Disse byggesten gør det muligt for AI-agenten at udføre en lang række opgaver. Lad os se på de nøgleelementer, der er nødvendige for at implementere designmønsteret for værktøjsbrug:

- **Funktions-/værktøjsskemaer:** Detaljerede definitioner af tilgængelige værktøjer, herunder funktionsnavn, formål, nødvendige parametre og forventede output. Disse skemaer gør det muligt for LLM at forstå, hvilke værktøjer der er tilgængelige, og hvordan man konstruerer gyldige forespørgsler.

- **Logik for funktionsudførelse:** Styrer, hvordan og hvornår værktøjer aktiveres baseret på brugerens hensigt og samtalekontekst. Dette kan omfatte planlægningsmoduler, routingmekanismer eller betingede flows, der dynamisk bestemmer værktøjsbrug.

- **System til håndtering af beskeder:** Komponenter, der styrer samtaleflowet mellem brugerinput, LLM-svar, værktøjskald og værktøjsoutput.

- **Integrationsramme for værktøjer:** Infrastruktur, der forbinder agenten med forskellige værktøjer, uanset om de er simple funktioner eller komplekse eksterne tjenester.

- **Fejlhåndtering og validering:** Mekanismer til at håndtere fejl i værktøjsudførelse, validere parametre og håndtere uventede svar.

- **Tilstandshåndtering:** Sporer samtalekontekst, tidligere værktøjsinteraktioner og vedvarende data for at sikre konsistens på tværs af interaktioner med flere omgange.

Lad os derefter se nærmere på funktions-/værktøjskald.

### Funktions-/værktøjskald

Funktionskald er den primære måde, vi gør det muligt for store sprogmodeller (LLM'er) at interagere med værktøjer. Du vil ofte se 'Funktion' og 'Værktøj' brugt i flæng, fordi 'funktioner' (blokke af genanvendelig kode) er de 'værktøjer', agenter bruger til at udføre opgaver. For at en funktions kode kan udføres, skal en LLM sammenligne brugerens forespørgsel med funktionens beskrivelse. For at gøre dette sendes et skema, der indeholder beskrivelserne af alle tilgængelige funktioner, til LLM'en. LLM'en vælger derefter den mest passende funktion til opgaven og returnerer dens navn og argumenter. Den valgte funktion udføres, dens svar sendes tilbage til LLM'en, som bruger informationen til at svare på brugerens forespørgsel.

For at udviklere kan implementere funktionskald for agenter, skal du bruge:

1. En LLM-model, der understøtter funktionskald
2. Et skema, der indeholder funktionsbeskrivelser
3. Koden for hver beskrevet funktion

Lad os bruge eksemplet med at få den aktuelle tid i en by til at illustrere:

1. **Initialiser en LLM, der understøtter funktionskald:**

    Ikke alle modeller understøtter funktionskald, så det er vigtigt at tjekke, at den LLM, du bruger, gør det. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> understøtter funktionskald. Vi kan starte med at initialisere Azure OpenAI-klienten.

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Opret et funktionsskema:**

    Dernæst definerer vi et JSON-skema, der indeholder funktionsnavnet, en beskrivelse af, hvad funktionen gør, og navnene og beskrivelserne af funktionsparametrene. Vi tager derefter dette skema og sender det til den tidligere oprettede klient sammen med brugerens forespørgsel om at finde tiden i San Francisco. Det er vigtigt at bemærke, at et **værktøjskald** er, hvad der returneres, **ikke** det endelige svar på spørgsmålet. Som nævnt tidligere returnerer LLM navnet på den funktion, den har valgt til opgaven, og de argumenter, der vil blive sendt til den.

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
  
1. **Den nødvendige funktionskode til at udføre opgaven:**

    Nu hvor LLM har valgt, hvilken funktion der skal køres, skal koden, der udfører opgaven, implementeres og udføres. Vi kan implementere koden til at få den aktuelle tid i Python. Vi skal også skrive koden til at udtrække navnet og argumenterne fra response_message for at få det endelige resultat.

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

Funktionskald er kernen i de fleste, hvis ikke alle, agentværktøjsdesign, men det kan nogle gange være udfordrende at implementere det fra bunden. Som vi lærte i [Lektion 2](../../../02-explore-agentic-frameworks) giver agentiske rammer os forudbyggede byggesten til at implementere værktøjsbrug.

## Eksempler på værktøjsbrug med agentiske rammer

Her er nogle eksempler på, hvordan du kan implementere designmønsteret for værktøjsbrug ved hjælp af forskellige agentiske rammer:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> er en open source AI-ramme for .NET-, Python- og Java-udviklere, der arbejder med store sprogmodeller (LLM'er). Den forenkler processen med at bruge funktionskald ved automatisk at beskrive dine funktioner og deres parametre til modellen gennem en proces kaldet <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serialisering</a>. Den håndterer også kommunikationen frem og tilbage mellem modellen og din kode. En anden fordel ved at bruge en agentisk ramme som Semantic Kernel er, at den giver dig adgang til forudbyggede værktøjer som <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">File Search</a> og <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Code Interpreter</a>.

Følgende diagram illustrerer processen med funktionskald med Semantic Kernel:

![funktionskald](../../../translated_images/functioncalling-diagram.a84006fc287f60140cc0a484ff399acd25f69553ea05186981ac4d5155f9c2f6.da.png)

I Semantic Kernel kaldes funktioner/værktøjer <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugins</a>. Vi kan konvertere `get_current_time`-funktionen, vi så tidligere, til et plugin ved at gøre den til en klasse med funktionen i den. Vi kan også importere dekoratoren `kernel_function`, som tager beskrivelsen af funktionen. Når du derefter opretter en kernel med GetCurrentTimePlugin, vil kernelen automatisk serialisere funktionen og dens parametre og skabe skemaet til at sende til LLM'en i processen.

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

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> er en nyere agentisk ramme, der er designet til at give udviklere mulighed for sikkert at bygge, implementere og skalere AI-agenter af høj kvalitet og med udvidelsesmuligheder uden at skulle administrere de underliggende computer- og lagerressourcer. Den er særligt nyttig til virksomhedsapplikationer, da det er en fuldt administreret tjeneste med sikkerhed på virksomhedsniveau.

Sammenlignet med at udvikle direkte med LLM API'en giver Azure AI Agent Service nogle fordele, herunder:

- Automatisk værktøjskald – ingen grund til at analysere et værktøjskald, aktivere værktøjet og håndtere svaret; alt dette håndteres nu server-side.
- Sikkert administrerede data – i stedet for at administrere din egen samtaletilstand kan du stole på tråde til at gemme al den information, du har brug for.
- Forudbyggede værktøjer – Værktøjer, som du kan bruge til at interagere med dine datakilder, såsom Bing, Azure AI Search og Azure Functions.

De værktøjer, der er tilgængelige i Azure AI Agent Service, kan opdeles i to kategorier:

1. Vidensværktøjer:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding med Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Handlingsværktøjer:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Funktionskald</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI-definerede værktøjer</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service giver os mulighed for at bruge disse værktøjer sammen som et `toolset`. Den bruger også `threads`, som holder styr på historikken for beskeder fra en bestemt samtale.

Forestil dig, at du er en salgsagent i en virksomhed kaldet Contoso. Du vil udvikle en samtaleagent, der kan besvare spørgsmål om dine salgsdata.

Følgende billede illustrerer, hvordan du kunne bruge Azure AI Agent Service til at analysere dine salgsdata:

![Agentisk service i aktion](../../../translated_images/agent-service-in-action.34fb465c9a84659edd3003f8cb62d6b366b310a09b37c44e32535021fbb5c93f.da.jpg)

For at bruge nogen af disse værktøjer med tjenesten kan vi oprette en klient og definere et værktøj eller et værktøjssæt. For at implementere dette praktisk kan vi bruge følgende Python-kode. LLM'en vil kunne se på værktøjssættet og beslutte, om den skal bruge den brugeroprettede funktion, `fetch_sales_data_using_sqlite_query`, eller den forudbyggede Code Interpreter afhængigt af brugerens forespørgsel.

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

## Hvilke særlige overvejelser er der ved brug af designmønsteret for værktøjsbrug til at bygge pålidelige AI-agenter?

En almindelig bekymring med SQL, der dynamisk genereres af LLM'er, er sikkerhed, især risikoen for SQL-injektion eller ondsindede handlinger, såsom at slette eller manipulere databasen. Selvom disse bekymringer er valide, kan de effektivt afhjælpes ved korrekt konfiguration af databaseadgangstilladelser. For de fleste databaser indebærer dette at konfigurere databasen som skrivebeskyttet. For databaseservices som PostgreSQL eller Azure SQL bør appen tildeles en skrivebeskyttet (SELECT) rolle.
At køre appen i et sikkert miljø forbedrer beskyttelsen yderligere. I virksomhedsscenarier bliver data typisk udtrukket og transformeret fra operationelle systemer til en skrivebeskyttet database eller datalager med et brugervenligt skema. Denne tilgang sikrer, at dataene er sikre, optimeret til ydeevne og tilgængelighed, og at appen har begrænset, skrivebeskyttet adgang.

## Eksempelkoder

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Har du flere spørgsmål om værktøjets designmønstre?

Deltag i [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) for at møde andre lærende, deltage i kontortimer og få svar på dine spørgsmål om AI-agenter.

## Yderligere ressourcer

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Function Calling Tutorial</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## Forrige lektion

[Forståelse af agentiske designmønstre](../03-agentic-design-patterns/README.md)

## Næste lektion

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->