[![How to Design Good AI Agents](../../../translated_images/da/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klik på billedet ovenfor for at se videoen til denne lektion)_

# Designmønster for brug af værktøjer

Værktøjer er interessante, fordi de giver AI-agenter en bredere vifte af evner. I stedet for at agenten har et begrænset sæt handlinger, den kan udføre, kan agenten ved at tilføje et værktøj nu udføre en lang række handlinger. I dette kapitel vil vi se på designmønsteret for brug af værktøjer, som beskriver, hvordan AI-agenter kan bruge specifikke værktøjer til at nå deres mål.

## Introduktion

I denne lektion søger vi at besvare følgende spørgsmål:

- Hvad er designmønsteret for brug af værktøjer?
- Hvilke anvendelsestilfælde kan det anvendes til?
- Hvilke elementer/building blocks er nødvendige for at implementere designmønsteret?
- Hvilke særlige overvejelser er der ved brug af designmønsteret for værktøjsbrug til at bygge troværdige AI-agenter?

## Læringsmål

Efter at have gennemført denne lektion vil du kunne:

- Definere designmønsteret for brug af værktøjer og dets formål.
- Identificere anvendelsestilfælde, hvor designmønsteret for brug af værktøjer er relevant.
- Forstå nøgleelementerne, der er nødvendige for at implementere designmønsteret.
- Genkende overvejelser for at sikre troværdighed i AI-agenter, der bruger dette designmønster.

## Hvad er designmønsteret for brug af værktøjer?

**Designmønsteret for brug af værktøjer** fokuserer på at give LLM'er mulighed for at interagere med eksterne værktøjer for at nå specifikke mål. Værktøjer er kode, der kan udføres af en agent for at udføre handlinger. Et værktøj kan være en simpel funktion som en lommeregner eller et API-kald til en tredjepartstjeneste såsom aktiekursopslag eller vejrudsigt. I konteksten af AI-agenter er værktøjer designet til at blive udført af agenter som svar på **modelgenererede funktionskald**.

## Hvilke anvendelsestilfælde kan det anvendes til?

AI-agenter kan udnytte værktøjer til at udføre komplekse opgaver, hente information eller træffe beslutninger. Designmønsteret for værktøjsbrug bruges ofte i scenarier, der kræver dynamisk interaktion med eksterne systemer, som databaser, webtjenester eller kodefortolkere. Denne evne er nyttig for en række forskellige anvendelsestilfælde, herunder:

- **Dynamisk informationsindhentning:** Agenter kan forespørge eksterne API'er eller databaser for at hente opdaterede data (f.eks. forespørge en SQLite-database til dataanalyse, hente aktiekurser eller vejrdata).
- **Kodekørsel og fortolkning:** Agenter kan udføre kode eller scripts for at løse matematiske problemer, generere rapporter eller udføre simuleringer.
- **Automatisering af arbejdsgange:** Automatisering af gentagne eller flerstegs arbejdsgange ved at integrere værktøjer som opgavestyring, e-mailtjenester eller datapipelines.
- **Kundesupport:** Agenter kan interagere med CRM-systemer, supportsystemer eller vidensbaser for at løse brugerhenvendelser.
- **Indholdsproduktion og redigering:** Agenter kan bruge værktøjer som grammatikkontrol, tekstopsummere eller indholdssikkerhedsvurderinger til at hjælpe med opgaver inden for indholdsskabelse.

## Hvilke elementer/building blocks er nødvendige for at implementere designmønsteret for brug af værktøjer?

Disse byggesten gør det muligt for AI-agenten at udføre et bredt spektrum af opgaver. Lad os se på nøgleelementerne nødvendige for at implementere designmønsteret for brug af værktøjer:

- **Funktions-/værktøjsskemaer**: Detaljerede definitioner af tilgængelige værktøjer, inklusiv funktionsnavn, formål, nødvendige parametre og forventede output. Disse skemaer gør det muligt for LLM at forstå, hvilke værktøjer der er tilgængelige, og hvordan man konstruerer gyldige forespørgsler.

- **Funktionsudførelseslogik**: Styrer hvordan og hvornår værktøjer kaldes baseret på brugerens hensigt og samtalekontekst. Dette kan inkludere planlægningsmoduler, routeringsmekanismer eller betingede flows, der dynamisk bestemmer brugen af værktøjer.

- **Beskedhåndteringssystem**: Komponenter, der håndterer den samtalemæssige flow mellem brugerinput, LLM-svar, værktøjskald og værktøjsoutput.

- **Værktøjsintegrationsramme**: Infrastruktur, der forbinder agenten til forskellige værktøjer, uanset om de er simple funktioner eller komplekse eksterne tjenester.

- **Fejlhåndtering & validering**: Mekanismer til at håndtere fejl i værktøjsudførelse, validere parametre og håndtere uventede svar.

- **State Management**: Holder styr på samtalekontekst, tidligere værktøjsinteraktioner og vedvarende data for at sikre konsistens på tværs af flere samtaleskridt.

Lad os nu se nærmere på Funktions-/værktøjskald.

### Funktions-/værktøjskald

Funktionskald er den primære måde, hvorpå vi giver store sprogmodeller (LLM'er) mulighed for at interagere med værktøjer. Du vil ofte se 'Funktion' og 'Værktøj' brugt om hinanden, fordi 'funktioner' (blokke af genanvendelig kode) er de 'værktøjer', som agenter bruger til at udføre opgaver. For at kunne påkalde en funktions kode, skal en LLM sammenligne brugerens anmodning med funktionens beskrivelse. For at gøre dette sendes et skema, der indeholder beskrivelser af alle tilgængelige funktioner, til LLM'en. LLM'en vælger derefter den mest passende funktion til opgaven og returnerer dens navn og argumenter. Den valgte funktion kaldes, dens svar sendes tilbage til LLM, som bruger informationen til at besvare brugerens anmodning.

For udviklere, der vil implementere funktionskald for agenter, skal du bruge:

1. En LLM-model, der understøtter funktionskald
2. Et skema, der indeholder funktionsbeskrivelser
3. Koden for hver beskrevne funktion

Lad os bruge eksemplet med at få det aktuelle klokkeslæt i en by til at illustrere:

1. **Initialiser en LLM, der understøtter funktionskald:**

    Ikke alle modeller understøtter funktionskald, så det er vigtigt at kontrollere, at den LLM du bruger gør det. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> understøtter funktionskald. Vi kan starte med at initialisere Azure OpenAI-klienten.

    ```python
    # Initialiser Azure OpenAI-klienten
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

2. **Opret et funktionsskema:**

    Næste trin er at definere et JSON-skema, der indeholder funktionsnavn, beskrivelse af hvad funktionen gør, samt navne og beskrivelser af funktionsparametre.
    Vi sender derefter dette skema til den tidligere oprettede klient sammen med brugerens anmodning om at finde tiden i San Francisco. Det vigtige at bemærke er, at et **værktøjskald** er det, der returneres, **ikke** det endelige svar på spørgsmålet. Som tidligere nævnt returnerer LLM navnet på den valgte funktion til opgaven og de argumenter, der skal sendes til den.

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
  
    # Initial brugerbesked
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Første API-opkald: Bed modellen om at bruge funktionen
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
  
3. **Den kode, der kræves for at udføre opgaven:**

    Nu hvor LLM har valgt, hvilken funktion der skal køres, skal koden, der udfører opgaven, implementeres og køres.
    Vi kan implementere koden til at hente det aktuelle klokkeslæt i Python. Vi skal også skrive kode til at udtrække navn og argumenter fra response_message for at få det endelige resultat.

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

Funktionskald er kernen i det meste, hvis ikke al, agentværktøjsbrug, men at implementere det fra bunden kan nogle gange være udfordrende.
Som vi lærte i [Lektion 2](../../../02-explore-agentic-frameworks) giver agentiske frameworks os forudbyggede byggesten til at implementere værktøjsbrug.
 
## Eksempler på værktøjsbrug med agentiske frameworks

Her er nogle eksempler på, hvordan du kan implementere designmønsteret for værktøjsbrug ved hjælp af forskellige agentiske frameworks:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> er et open source AI-framework til at bygge AI-agenter. Det forenkler processen med at bruge funktionskald ved at give dig mulighed for at definere værktøjer som Python-funktioner med `@tool` dekoratøren. Frameworket håndterer frem- og tilbagekommunikationen mellem modellen og din kode. Det giver også adgang til forudbyggede værktøjer som Fil-søgning og Kodefortolker via `AzureAIProjectAgentProvider`.

Følgende diagram illustrerer processen for funktionskald med Microsoft Agent Framework:

![function calling](../../../translated_images/da/functioncalling-diagram.a84006fc287f6014.webp)

I Microsoft Agent Framework defineres værktøjer som dekorerede funktioner. Vi kan omdanne `get_current_time` funktionen, som vi så tidligere, til et værktøj ved at bruge `@tool` dekoratøren. Frameworket vil automatisk serialisere funktionen og dens parametre og skabe skemaet, der sendes til LLM.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Opret klienten
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Opret en agent og kør med værktøjet
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> er et nyere agentisk framework designet til at give udviklere mulighed for sikkert at bygge, implementere og skalere AI-agenter af høj kvalitet og udvidelsesmuligheder uden at skulle håndtere underliggende computermæssige og lagringsmæssige ressourcer. Det er særligt nyttigt til virksomhedsapplikationer, da det er en fuldt administreret service med sikkerhed på virksomhedsniveau.

Sammenlignet med udvikling direkte med LLM API'en giver Azure AI Agent Service nogle fordele, herunder:

- Automatisk værktøjskald – du behøver ikke at analysere et værktøjskald, kalde værktøjet og håndtere svaret; alt dette gøres nu server-side.
- Sikkert administrerede data – i stedet for selv at styre samtalestatus kan du stole på threads til at gemme alle nødvendige oplysninger.
- Færdigbyggede værktøjer – værktøjer du kan bruge til at interagere med dine datakilder som Bing, Azure AI Search og Azure Functions.

De tilgængelige værktøjer i Azure AI Agent Service kan opdeles i to kategorier:

1. Videnværktøjer:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding med Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Fil-søgning</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Handlingsværktøjer:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Funktionskald</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Kodefortolker</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI-definerede værktøjer</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service gør det muligt for os at bruge disse værktøjer sammen som et `toolset`. Den benytter også `threads`, som holder styr på historikken af beskeder fra en bestemt samtale.

Forestil dig, at du er salgsagent hos et firma kaldet Contoso. Du ønsker at udvikle en samtaleagent, der kan besvare spørgsmål om dine salgsdata.

Følgende billede illustrerer, hvordan du kunne bruge Azure AI Agent Service til at analysere dine salgsdata:

![Agentic Service In Action](../../../translated_images/da/agent-service-in-action.34fb465c9a84659e.webp)

For at bruge nogen af disse værktøjer med servicen kan vi oprette en klient og definere et værktøj eller toolset. For praktisk implementering kan vi bruge følgende Python-kode. LLM'en vil kunne kigge på toolsettet og afgøre, om den skal bruge den brugeroprettede funktion `fetch_sales_data_using_sqlite_query` eller den forudbyggede Kodefortolker, afhængigt af brugerens anmodning.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query-funktion, som kan findes i en fil ved navn fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initialiser værktøjssæt
toolset = ToolSet()

# Initialiser funktionskaldende agent med funktionen fetch_sales_data_using_sqlite_query og tilføj den til værktøjssættet
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Initialiser Kodefortolker-værktøj og tilføj det til værktøjssættet.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Hvilke særlige overvejelser er der ved brug af designmønsteret for værktøjsbrug til at bygge troværdige AI-agenter?

En almindelig bekymring ved SQL dynamisk genereret af LLM'er er sikkerhed, især risikoen for SQL-injektion eller skadelige handlinger, såsom sletning eller manipulation af databasen. Selvom disse bekymringer er berettigede, kan de effektivt afbødes ved korrekt konfiguration af databasens adgangstilladelser. For de fleste databaser indebærer dette at konfigurere databasen som skrivebeskyttet. For databaser som PostgreSQL eller Azure SQL bør app’en tildeles en rolle med læseadgang (SELECT).

At køre app’en i et sikkert miljø øger yderligere beskyttelsen. I virksomhedsscenarier udtrækkes og transformeres data normalt fra operationelle systemer til en skrivebeskyttet database eller datalager med et brugervenligt skema. Denne tilgang sikrer, at data er sikre, optimeret til ydeevne og tilgængelighed, og at app’en kun har begrænset, skrivebeskyttet adgang.

## Eksempelkoder

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Flere spørgsmål om designmønsteret for værktøjsbrug?

Deltag i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) for at møde andre lærende, deltage i åbne kontortimer og få svar på dine spørgsmål om AI-agenter.

## Yderligere ressourcer

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework Oversigt</a>

## Forrige lektion

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## Næste lektion
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->