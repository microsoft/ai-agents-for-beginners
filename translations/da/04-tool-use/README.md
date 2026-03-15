[![Hvordan man designer gode AI-agenter](../../../translated_images/da/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klik på billedet ovenfor for at se videoen til denne lektion)_

# Mønster for brug af værktøjer

Værktøjer er interessante, fordi de giver AI-agenter en bredere vifte af muligheder. I stedet for at agenten har et begrænset sæt handlinger, den kan udføre, kan agenten nu udføre en bred vifte af handlinger ved at tilføje et værktøj. I dette kapitel vil vi se nærmere på mønsteret for brug af værktøjer, som beskriver, hvordan AI-agenter kan bruge specifikke værktøjer til at nå deres mål.

## Introduktion

I denne lektion vil vi besvare følgende spørgsmål:

- Hvad er mønsteret for brug af værktøjer?
- Hvilke anvendelsestilfælde kan det anvendes på?
- Hvilke elementer/opbygningsblokke er nødvendige for at implementere mønsteret?
- Hvilke særlige overvejelser er der ved at bruge mønsteret for brug af værktøjer til at opbygge pålidelige AI-agenter?

## Læringsmål

Efter at have gennemført denne lektion vil du kunne:

- Definere mønsteret for brug af værktøjer og dets formål.
- Identificere anvendelsestilfælde hvor mønsteret for brug af værktøjer kan anvendes.
- Forstå nøgleelementerne nødvendige for at implementere mønsteret.
- Genkende overvejelser for at sikre pålidelighed i AI-agenter, der bruger dette mønster.

## Hvad er mønsteret for brug af værktøjer?

**Mønstret for brug af værktøjer** fokuserer på at give LLM'er mulighed for at interagere med eksterne værktøjer for at opnå specifikke mål. Værktøjer er kode, der kan udføres af en agent for at udføre handlinger. Et værktøj kan være en simpel funktion som en lommeregner eller et API-kald til en tredjepartstjeneste som aktiekursopslag eller vejrudsigt. I forbindelse med AI-agenter er værktøjer designet til at blive udført af agenter som svar på **modelgenererede funktionskald**.

## Hvilke anvendelsestilfælde kan det anvendes på?

AI-agenter kan udnytte værktøjer til at udføre komplekse opgaver, hente information eller træffe beslutninger. Mønstret for brug af værktøjer anvendes ofte i scenarier, der kræver dynamisk interaktion med eksterne systemer som databaser, webtjenester eller kodefortolkere. Denne evne er nyttig for flere forskellige anvendelsestilfælde, herunder:

- **Dynamisk informationshentning:** Agenter kan forespørge eksterne API'er eller databaser for at hente opdaterede data (f.eks. forespørgsel til en SQLite database til dataanalyse, hentning af aktiekurser eller vejrinformation).
- **Kodeudførelse og fortolkning:** Agenter kan køre kode eller scripts for at løse matematiske problemer, generere rapporter eller udføre simuleringer.
- **Automatisering af arbejdsgange:** Automatisering af repetitive eller flertrins arbejdsgange ved integration af værktøjer som opgavestyring, e-mail-tjenester eller datapipelines.
- **Kundesupport:** Agenter kan interagere med CRM-systemer, supportsystemer eller vidensdatabaser for at løse brugerforespørgsler.
- **Indholdsgenerering og redigering:** Agenter kan udnytte værktøjer som grammatikkontrol, tekstopsummering eller indholdssikkerhedsvurderinger til at assistere med opgaver inden for indholdsskabelse.

## Hvilke elementer/opbygningsblokke er nødvendige for at implementere mønsteret for brug af værktøjer?

Disse opbygningsblokke tillader AI-agenten at udføre en bred vifte af opgaver. Lad os se på nøgleelementerne, der er nødvendige for at implementere mønsteret for brug af værktøjer:

- **Funktion-/værktøjsskemaer**: Detaljerede definitioner af tilgængelige værktøjer, inklusive funktionsnavn, formål, nødvendige parametre og forventede output. Disse skemaer gør det muligt for LLM'en at forstå, hvilke værktøjer der er tilgængelige, og hvordan man konstruerer gyldige forespørgsler.

- **Logik for funktionsudførelse**: Styrer hvordan og hvornår værktøjer bliver kaldt på baggrund af brugerens hensigt og samtalekontekst. Dette kan inkludere planlægningsmoduler, rute-mekanismer eller betingede flows, som dynamisk bestemmer brugen af værktøjer.

- **Beskedhåndteringssystem**: Komponenter, der styrer samtaleforløbet mellem brugerinput, LLM-svar, værktøjskald og værktøjsoutput.

- **Værktøjsintegrationsrammeværk**: Infrastruktur, der forbinder agenten til forskellige værktøjer, hvad enten det er simple funktioner eller komplekse eksterne tjenester.

- **Fejlhåndtering & validering**: Mekanismer til at håndtere fejl i værktøjsudførelse, validere parametre og håndtere uventede svar.

- **Tilstandsstyring**: Sporer samtalekontekst, tidligere værktøjsinteraktioner og vedvarende data for at sikre konsistens på tværs af flere samtalerunder.

Lad os nu se nærmere på Funktions-/værktøjskald.

### Funktions-/værktøjskald

Funktionskald er den primære måde, hvorpå vi gør det muligt for store sprogmodeller (LLM'er) at interagere med værktøjer. Man vil ofte se 'Funktion' og 'Værktøj' brugt i flæng, fordi 'funktioner' (blokke af genanvendelig kode) er de 'værktøjer', agenter bruger til at udføre opgaver. For at en funktions kode kan påkaldes, skal LLM'en sammenligne brugerens anmodning med funktionens beskrivelse. Til dette sendes et skema indeholdende beskrivelser af alle tilgængelige funktioner til LLM'en. LLM'en vælger så den mest passende funktion til opgaven og returnerer dens navn og argumenter. Den valgte funktion påkaldes, og dens svar sendes tilbage til LLM'en, som bruger informationen til at svare på brugerens anmodning.

For at udviklere kan implementere funktionskald for agenter, skal følgende være på plads:

1. En LLM-model, der understøtter funktionskald  
2. Et skema indeholdende funktionsbeskrivelser  
3. Koden til hver beskrevet funktion

Lad os bruge eksemplet med at hente det aktuelle klokkeslæt i en by som illustration:

1. **Initier en LLM, der understøtter funktionskald:**

    Ikke alle modeller understøtter funktionskald, så det er vigtigt at tjekke, at den LLM, du bruger, gør det. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> understøtter funktionskald. Vi kan starte med at initialisere Azure OpenAI klienten.

    ```python
    # Initialiser Azure OpenAI-klienten
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Opret et funktionsskema**:

    Dernæst definerer vi et JSON-skema, der indeholder funktionsnavnet, beskrivelse af hvad funktionen gør, samt navne og beskrivelser af funktionsparametrene. Vi sender så dette skema til klienten, som vi tidligere oprettede, sammen med brugerens anmodning om at finde tiden i San Francisco. Det vigtige at bemærke er, at et **værktøjskald** er det, der returneres, **ikke** det endelige svar på spørgsmålet. Som nævnt tidligere returnerer LLM navnet på den funktion, den har valgt til opgaven, og argumenterne, der skal sendes til den.

    ```python
    # Funktionsbeskrivelse til modellen at læse
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
  
    # Indledende brugermeddelelse
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
  
1. **Funktionskoden, der kræves for at udføre opgaven:**

    Nu hvor LLM'en har valgt, hvilken funktion der skal køres, skal koden, der udfører opgaven, implementeres og eksekveres. Vi kan implementere koden til at hente det aktuelle klokkeslæt i Python. Vi skal også skrive koden til at udtrække navn og argumenter fra response_message for at få det endelige resultat.

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
  
      # Andet API-kald: Få det endelige svar fra modellen
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

Funktionskald er kerneelementet i de fleste, hvis ikke alle agentværktøjsbrugsmønstre, men det kan nogle gange være udfordrende at implementere fra bunden.  
Som vi lærte i [Lektion 2](../../../02-explore-agentic-frameworks) leverer agentiske rammer præbyggede opbygningsblokke til implementering af værktøjsbrug.

## Eksempler på brug af værktøjer med agentiske rammer

Her er nogle eksempler på, hvordan du kan implementere mønsteret for brug af værktøjer ved hjælp af forskellige agentiske rammer:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> er en open source AI-ramme til opbygning af AI-agenter. Det forenkler processen med funktionskald ved at give dig mulighed for at definere værktøjer som Python-funktioner med `@tool`-dekorationen. Frameworket håndterer kommunikationen frem og tilbage mellem modellen og din kode. Det giver også adgang til forudbyggede værktøjer som fil- og kodefortolkning gennem `AzureAIProjectAgentProvider`.

Følgende diagram illustrerer processen ved funktionskald med Microsoft Agent Framework:

![function calling](../../../translated_images/da/functioncalling-diagram.a84006fc287f6014.webp)

I Microsoft Agent Framework defineres værktøjer som dekorerede funktioner. Vi kan konvertere `get_current_time`-funktionen, vi så tidligere, til et værktøj ved at bruge `@tool`-dekorationen. Frameworket vil automatisk serialisere funktionen og dens parametre, hvilket skaber det skema, der sendes til LLM'en.

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

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> er en nyere agentisk ramme, der er designet til at give udviklere mulighed for sikkert at opbygge, implementere og skalere AI-agenter af høj kvalitet og med udvidelsesmuligheder uden at skulle håndtere de underliggende compute- og lagringsressourcer. Det er særligt nyttigt for enterprise-applikationer, da det er en fuldt administreret tjeneste med enterprise-sikkerhed i topklasse.

Sammenlignet med direkte udvikling med LLM API, giver Azure AI Agent Service flere fordele, herunder:

- Automatisk værktøjskald – ingen behov for at parse værktøjskald, kalde værktøjet og håndtere svar; alt dette udføres nu server-side  
- Sikkert administrerede data – i stedet for at håndtere egen samtalestatus kan du stole på tråde til at gemme alle nødvendige oplysninger  
- Værktøjer klar til brug – værktøjer som du kan bruge til at interagere med dine datakilder, som Bing, Azure AI Search og Azure Functions.

Værktøjerne i Azure AI Agent Service kan opdeles i to kategorier:

1. Vidensværktøjer:  
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding med Bing Search</a>  
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Fil-søgning</a>  
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Handlingsværktøjer:  
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Funktionskald</a>  
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Kodefortolker</a>  
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI-definerede værktøjer</a>  
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service giver os mulighed for at bruge disse værktøjer sammen som et `værktøjssæt`. Det benytter også `tråde`, der holder styr på historikken af beskeder fra en bestemt samtale.

Forestil dig, at du er en salgsagent hos et firma, der hedder Contoso. Du ønsker at udvikle en samtaleagent, der kan besvare spørgsmål om dine salgsdata.

Følgende billede illustrerer, hvordan du kan bruge Azure AI Agent Service til at analysere dine salgsdata:

![Agentic Service In Action](../../../translated_images/da/agent-service-in-action.34fb465c9a84659e.webp)

For at bruge nogle af disse værktøjer med tjenesten kan vi oprette en klient og definere et værktøj eller et værktøjssæt. For at implementere dette praktisk kan vi bruge følgende Python-kode. LLM'en vil kunne se på værktøjssættet og beslutte, om den skal bruge den brugeroprettede funktion, `fetch_sales_data_using_sqlite_query`, eller den forudbyggede Kodefortolker afhængigt af brugerens anmodning.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query funktion, som kan findes i en fetch_sales_data_functions.py fil.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initialiser værktøjssæt
toolset = ToolSet()

# Initialiser funktion kaldende agent med fetch_sales_data_using_sqlite_query funktionen og tilføj den til værktøjssættet
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Initialiser Code Interpreter værktøj og tilføj det til værktøjssættet.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Hvilke særlige overvejelser er der ved brug af mønsteret for brug af værktøjer til at opbygge pålidelige AI-agenter?

En almindelig bekymring ved SQL dynamisk genereret af LLM'er er sikkerhed, især risikoen for SQL-injektion eller ondsindede handlinger som at slette eller manipulere databasen. Selvom disse bekymringer er gyldige, kan de effektivt afbødes ved korrekt konfiguration af databaseadgangstilladelser. For de fleste databaser indebærer det at konfigurere databasen som skrivebeskyttet. For databaser som PostgreSQL eller Azure SQL bør appen tildeles en skrivebeskyttet (SELECT) rolle.

At køre appen i et sikkert miljø øger yderligere beskyttelsen. I enterprise-scenarier bliver data typisk udtrukket og transformeret fra operationelle systemer til en skrivebeskyttet database eller datalager med et brugervenligt skema. Denne tilgang sikrer, at dataene er sikre, optimeret til ydeevne og tilgængelighed, og at appen har begrænset, skrivebeskyttet adgang.

## Eksempelkoder

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)  
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Har du flere spørgsmål om mønstrene for brug af værktøjer?

Deltag i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) for at møde andre lærende, deltage i kontortimer og få svar på dine spørgsmål om AI-agenter.

## Yderligere ressourcer

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>  
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>  
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework Oversigt</a>

## Forrige lektion

[Forstå agentiske designmønstre](../03-agentic-design-patterns/README.md)

## Næste lektion
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på originalsproget bør betragtes som den autoritative kilde. For kritiske oplysninger anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller misfortolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->