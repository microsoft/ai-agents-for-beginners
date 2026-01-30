[![Hvordan man designer gode AI-agenter](../../../translated_images/da/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klik på billedet ovenfor for at se videoen til denne lektion)_

# Designmønster for brug af værktøjer

Værktøjer er interessante, fordi de giver AI-agenter en bredere række af muligheder. I stedet for at agenten kun har et begrænset sæt handlinger, den kan udføre, kan agenten via tilføjelsen af et værktøj nu udføre en lang række handlinger. I dette kapitel ser vi på designmønsteret for brug af værktøjer, som beskriver, hvordan AI-agenter kan bruge specifikke værktøjer til at nå deres mål.

## Introduktion

I denne lektion vil vi besvare følgende spørgsmål:

- Hvad er designmønsteret for brug af værktøjer?
- Hvilke anvendelsestilfælde kan det anvendes på?
- Hvad er elementerne/opbygningsklodserne, der er nødvendige for at implementere designmønsteret?
- Hvilke særlige overvejelser er der ved brug af designmønsteret for brug af værktøjer til at bygge troværdige AI-agenter?

## Læringsmål

Efter at have gennemført denne lektion vil du kunne:

- Definere designmønsteret for brug af værktøjer og dets formål.
- Identificere anvendelsestilfælde, hvor designmønsteret for brug af værktøjer er relevant.
- Forstå de vigtigste elementer, der skal til for at implementere designmønsteret.
- Genkende overvejelser for at sikre troværdighed i AI-agenter, der anvender dette designmønster.

## Hvad er designmønsteret for brug af værktøjer?

**Designmønsteret for brug af værktøjer** fokuserer på at give LLM'er evnen til at interagere med eksterne værktøjer for at nå specifikke mål. Værktøjer er kode, der kan udføres af en agent for at udføre handlinger. Et værktøj kan være en simpel funktion som en lommeregner eller et API-kald til en tredjepartstjeneste, såsom opslag af aktiekurser eller vejrprognoser. I sammenhæng med AI-agenter designes værktøjer til at blive udført af agenter som svar på **modelgenererede funktionskald**.

## Hvilke anvendelsestilfælde kan det anvendes på?

AI-agenter kan bruge værktøjer til at udføre komplekse opgaver, hente information eller træffe beslutninger. Designmønsteret for brug af værktøjer anvendes ofte i scenarier, der kræver dynamisk interaktion med eksterne systemer som databaser, webservices eller kodefortolkere. Denne evne er nyttig til en række forskellige anvendelsestilfælde, herunder:

- **Dynamisk informationsindhentning:** Agenter kan forespørge eksterne API'er eller databaser for at hente opdaterede data (f.eks. forespørgsler til en SQLite-database for dataanalyse, hentning af aktiekurser eller vejrdata).
- **Kodeeksekvering og fortolkning:** Agenter kan køre kode eller scripts for at løse matematiske problemer, generere rapporter eller gennemføre simuleringer.
- **Automatisering af arbejdsgange:** Automatisering af gentagne eller flerstegsarbejdsgange ved at integrere værktøjer som opgavestyring, e-mailtjenester eller datapipelines.
- **Kundesupport:** Agenter kan interagere med CRM-systemer, supportsystemer eller vidensbaser for at besvare brugerspørgsmål.
- **Indholdsproduktion og redigering:** Agenter kan anvende værktøjer som grammatikkontrol, tekstopsummatorer eller indholdssikkerhedsvurderinger til at assistere med opgaver inden for indholdsskabelse.

## Hvad er elementerne/opbygningsklodserne, der er nødvendige for at implementere designmønsteret for brug af værktøjer?

Disse opbygningsklodser gør det muligt for AI-agenten at udføre mange forskellige opgaver. Lad os se på nøgleelementerne, der kræves for at implementere designmønsteret for brug af værktøjer:

- **Funktions-/værktøjsskemaer**: Detaljerede definitioner af tilgængelige værktøjer, inklusiv funktionsnavn, formål, nødvendige parametre og forventede output. Disse skemaer giver LLM'en mulighed for at forstå, hvilke værktøjer der findes, og hvordan gyldige anmodninger konstrueres.

- **Logik til funktionsudførelse**: Styrer hvordan og hvornår værktøjer aktiveres baseret på brugerens hensigt og samtalekontekst. Dette kan inkludere planlægningsmoduler, rute-mekanismer eller betingede flows, der dynamisk bestemmer værktøjsanvendelse.

- **Beskedhåndteringssystem**: Komponenter, der styrer den samtalemæssige flow mellem brugerinput, LLM-svar, værktøjskald og værktøjsoutput.

- **Værktøjsintegrationsrammeværk**: Infrastruktur, der forbinder agenten med forskellige værktøjer, hvad enten det er simple funktioner eller komplekse eksterne tjenester.

- **Fejlhåndtering & validering**: Mekanismer til håndtering af fejl ved udførelse af værktøjer, validering af parametre og styring af uventede svar.

- **Tilstandsstyring**: Holder styr på samtalekontekst, tidligere værktøjsinteraktioner og persistent data for at sikre konsistens på tværs af flettsvedede interaktioner.

Lad os nu se nærmere på funktions-/værktøjskald.

### Funktions-/værktøjskald

Funktionskald er den primære måde, hvorpå vi gør det muligt for store sprogmodeller (LLM'er) at interagere med værktøjer. Du vil ofte se 'Funktion' og 'Værktøj' brugt om hinanden, fordi 'funktioner' (genanvendelige kodeblokke) er de 'værktøjer', som agenter bruger til at udføre opgaver. For at en funktionskode kan kaldes, skal en LLM sammenligne brugerens forespørgsel med funktionens beskrivelse. Til dette formål sendes et skema, der indeholder beskrivelserne af alle tilgængelige funktioner, til LLM'en. LLM'en vælger derefter den mest passende funktion til opgaven og returnerer dens navn og argumenter. Den valgte funktion kaldes, dens svar sendes tilbage til LLM'en, som bruger oplysningerne til at svare på brugerens forespørgsel.

For at udviklere kan implementere funktionskald til agenter, skal du bruge:

1. En LLM-model, der understøtter funktionskald
2. Et skema med funktionsbeskrivelser
3. Koden for hver beskrevne funktion

Lad os bruge eksemplet med at få den aktuelle tid i en by til at illustrere:

1. **Initialiser en LLM, der understøtter funktionskald:**

    Ikke alle modeller understøtter funktionskald, så det er vigtigt at sikre, at den LLM, du bruger, gør det. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> understøtter funktionskald. Vi kan starte med at initialisere Azure OpenAI-klienten.

    ```python
    # Initialiser Azure OpenAI-klienten
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Opret et funktionsskema**:

    Dernæst definerer vi et JSON-skema, der indeholder funktionsnavnet, en beskrivelse af, hvad funktionen gør, og navnene og beskrivelserne af funktionsparametrene. 
    Vi sender så dette skema til klienten, som vi oprettede tidligere, sammen med brugerens forespørgsel om at finde tiden i San Francisco. Det vigtige at bemærke er, at et **værktøjskald** er det, der returneres, **ikke** det endelige svar på spørgsmålet. Som nævnt tidligere returnerer LLM'en navnet på den funktion, den valgte til opgaven, og argumenterne, der skal gives til den.

    ```python
    # Funktionsbeskrivelse for modellen at læse
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
  
    # Startbesked fra bruger
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Første API-kald: Bed modellen om at bruge funktionen
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Behandl modellens svar
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Funktionskoden, der er nødvendig for at udføre opgaven:**

    Nu hvor LLM'en har valgt, hvilken funktion der skal udføres, skal den kode, der udfører opgaven, implementeres og eksekveres.
    Vi kan implementere koden til at hente den aktuelle tid i Python. Vi skal også skrive koden, der udtrækker navnet og argumenterne fra response_message for at få det endelige resultat.

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
     # Håndter funktionskald
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
  
      # Andet API-kald: Hent det endelige svar fra modellen
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

Funktionskald er kernen i det meste, hvis ikke al, agentværktøjsbrug, men det kan til tider være udfordrende at implementere det fra bunden.
Som vi lærte i [Lektion 2](../../../02-explore-agentic-frameworks) giver agentiske frameworks os forbyggede opbygningsklodser til at implementere værktøjsbrug.
 
## Eksempler på værktøjsbrug med agentiske frameworks

Her er nogle eksempler på, hvordan du kan implementere designmønsteret for brug af værktøjer ved hjælp af forskellige agentiske frameworks:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> er et open source AI-framework for .NET, Python og Java-udviklere, der arbejder med store sprogmodeller (LLM'er). Det forenkler processen med at bruge funktionskald ved automatisk at beskrive dine funktioner og deres parametre for modellen gennem en proces kaldet <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serialisering</a>. Det håndterer også kommunikationen frem og tilbage mellem modellen og din kode. En anden fordel ved at bruge et agentisk framework som Semantic Kernel er, at det giver dig adgang til forbyggede værktøjer som <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">Filsøgning</a> og <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Kodefortolker</a>.

Følgende diagram illustrerer processen med funktionskald i Semantic Kernel:

![funktionskald](../../../translated_images/da/functioncalling-diagram.a84006fc287f6014.webp)

I Semantic Kernel kaldes funktioner/værktøjer <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugins</a>. Vi kan omskrive funktionen `get_current_time`, som vi så tidligere, til en plugin ved at gøre den til en klasse med funktionen i sig. Vi kan også importere `kernel_function` dekoratoren, som tager beskrivelsen af funktionen som input. Når du derefter opretter en kernel med GetCurrentTimePlugin, vil kernen automatisk serialisere funktionen og dens parametre, hvilket i processen skaber det skema, der sendes til LLM'en.

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

# Opret kernen
kernel = Kernel()

# Opret plugin'et
get_current_time_plugin = GetCurrentTimePlugin(location)

# Tilføj plugin'et til kernen
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> er et nyere agentisk framework, der er designet til at hjælpe udviklere med sikkert at bygge, implementere og skalere AI-agenter af høj kvalitet og med udvidelsesmuligheder uden behov for at administrere underliggende beregnings- og lagringsressourcer. Det er særligt nyttigt til virksomhedsapplikationer, da det er en fuldt administreret tjeneste med virksomhedsgrad-sikkerhed.

Sammenlignet med at udvikle direkte med LLM API'en, tilbyder Azure AI Agent Service nogle fordele, herunder:

- Automatisk værktøjskald – ingen grund til at parse et værktøjskald, udføre værktøjet og håndtere svaret; alt dette sker nu serverside
- Sikkert administrerede data – i stedet for selv at styre samtalens tilstand kan du stole på threads til at gemme alle nødvendige oplysninger
- Værktøjer klar til brug – værktøjer, som du kan bruge til at interagere med dine datakilder, såsom Bing, Azure AI Search og Azure Functions.

Værktøjerne, der er tilgængelige i Azure AI Agent Service, kan deles op i to kategorier:

1. Vidensværktøjer:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding med Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Filsøgning</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Handlingsværktøjer:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Funktionskald</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Kodefortolker</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI-definerede værktøjer</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service gør det muligt at bruge disse værktøjer sammen som et `toolset`. Det benytter også `threads`, som holder styr på historikken af beskeder fra en given samtale.

Forestil dig, at du er salgsagent hos en virksomhed kaldet Contoso. Du ønsker at udvikle en samtaleagent, der kan besvare spørgsmål om dine salgsdata.

Følgende billede illustrerer, hvordan du kunne bruge Azure AI Agent Service til at analysere dine salgsdata:

![Agent Service i aktion](../../../translated_images/da/agent-service-in-action.34fb465c9a84659e.webp)

For at bruge et af disse værktøjer med servicen kan vi oprette en klient og definere et værktøj eller værktøjssæt. For at implementere dette praktisk kan vi bruge følgende Python-kode. LLM'en vil kunne se på værktøjssættet og beslutte, om den skal anvende den brugerdefinerede funktion `fetch_sales_data_using_sqlite_query` eller den forbyggede Kodefortolker afhængigt af brugerens forespørgsel.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query-funktion, som kan findes i en fetch_sales_data_functions.py-fil.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initialiser værktøjssæt
toolset = ToolSet()

# Initialiser funktionskaldsagent med fetch_sales_data_using_sqlite_query-funktionen og tilføj den til værktøjssættet
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Initialiser Code Interpreter-værktøj og tilføj det til værktøjssættet.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Hvilke særlige overvejelser er der ved brug af designmønsteret for brug af værktøjer til at bygge troværdige AI-agenter?

En almindelig bekymring ved dynamisk genereret SQL af LLM'er er sikkerhed, især risikoen for SQL-injektion eller skadelige handlinger som at slette eller manipulere databasen. Selvom disse bekymringer er gyldige, kan de effektivt afhjælpes ved korrekt konfiguration af adgangstilladelser til databasen. For de fleste databaser indebærer dette at konfigurere databasen som skrivebeskyttet. For databaser som PostgreSQL eller Azure SQL bør applikationen tildeles en skrivebeskyttet (SELECT) rolle.
At køre appen i et sikkert miljø øger beskyttelsen yderligere. I erhvervsscenarier udtrækkes og transformeres data typisk fra operationelle systemer til en skrivebeskyttet database eller datalager med et brugervenligt skema. Denne tilgang sikrer, at dataene er sikre, optimeret til ydeevne og tilgængelighed, og at appen har begrænset, skrivebeskyttet adgang.

## Sample Codes

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Har du flere spørgsmål om brugen af designmønstre i værktøjet?

Deltag i [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) for at møde andre lærende, deltage i kontortimer og få svar på dine spørgsmål om AI-agenter.

## Yderligere ressourcer

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Function Calling Tutorial</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## Forrige lektion

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## Næste lektion

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på originalsproget skal betragtes som den autoritative kilde. For vigtig information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->