[![Hvordan man Designer Gode AI-agenter](../../../translated_images/da/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klik på billedet ovenfor for at se videoen til denne lektion)_

# Designmønster for Brug af Værktøjer

Værktøjer er interessante, fordi de giver AI-agenter mulighed for at have et bredere spektrum af kapaciteter. I stedet for at agenten kun har et begrænset sæt handlinger, den kan udføre, kan agenten nu udføre en bred vifte af handlinger ved at tilføje et værktøj. I dette kapitel vil vi se på designmønsteret for brug af værktøjer, som beskriver, hvordan AI-agenter kan bruge specifikke værktøjer til at opnå deres mål.

## Introduktion

I denne lektion søger vi at besvare følgende spørgsmål:

- Hvad er designmønsteret for brug af værktøjer?
- Hvilke anvendelsestilfælde kan det bruges til?
- Hvilke elementer/byggesten er nødvendige for at implementere designmønsteret?
- Hvilke særlige overvejelser er der ved brug af designmønsteret for at bygge pålidelige AI-agenter?

## Læringsmål

Efter at have gennemført denne lektion vil du kunne:

- Definere designmønsteret for brug af værktøjer og dets formål.
- Identificere anvendelsestilfælde, hvor designmønsteret kan anvendes.
- Forstå de nøgleelementer, der er nødvendige for at implementere designmønsteret.
- Genkende overvejelser for at sikre pålidelighed i AI-agenter, der bruger dette designmønster.

## Hvad er designmønsteret for brug af værktøjer?

**Designmønsteret for brug af værktøjer** fokuserer på at give LLM'er evnen til at interagere med eksterne værktøjer for at nå specifikke mål. Værktøjer er kode, der kan eksekveres af en agent for at udføre handlinger. Et værktøj kan være en simpel funktion som en lommeregner eller et API-kald til en tredjepartstjeneste såsom aktiekurs opslag eller vejrudsigter. I konteksten af AI-agenter er værktøjer designet til at blive eksekveret af agenter som svar på **model-genererede funktionskald**.

## Hvilke anvendelsestilfælde kan det bruges til?

AI-agenter kan udnytte værktøjer til at udføre komplekse opgaver, hente information eller tage beslutninger. Designmønsteret for brug af værktøjer bruges ofte i scenarier, der kræver dynamisk interaktion med eksterne systemer såsom databaser, webtjenester eller kodefortolkere. Denne evne er nyttig til flere forskellige anvendelsestilfælde, herunder:

- **Dynamisk informationshentning:** Agenter kan forespørge eksterne API'er eller databaser for at hente opdaterede data (fx forespørge en SQLite-database til dataanalyse, hente aktiekurser eller vejroplysninger).
- **Kodeeksekvering og fortolkning:** Agenter kan eksekvere kode eller scripts for at løse matematiske problemer, generere rapporter eller udføre simuleringer.
- **Automatisering af arbejdsgange:** Automatisering af gentagne eller flertrinsarbejdsgange ved at integrere værktøjer som opgavestyring, e-mailtjenester eller datapipelines.
- **Kundesupport:** Agenter kan interagere med CRM-systemer, supportplatforme eller vidensdatabaser for at løse brugerhenvendelser.
- **Indholdsgenerering og redigering:** Agenter kan bruge værktøjer som grammatikkontrol, tekstopsummering eller vurderinger af indholdssikkerhed til at hjælpe med opgaver vedrørende indholdsskabelse.

## Hvilke elementer/byggesten er nødvendige for at implementere designmønsteret for brug af værktøjer?

Disse byggesten gør det muligt for AI-agenten at udføre en bred vifte af opgaver. Lad os se på de nøgleelementer, der er nødvendige for at implementere designmønsteret for brug af værktøjer:

- **Funktions-/værktøjs-skemaer**: Detaljerede definitioner af tilgængelige værktøjer, inklusive funktionsnavn, formål, nødvendige parametre og forventede output. Disse skemaer gør det muligt for LLM at forstå, hvilke værktøjer der er tilgængelige, og hvordan man konstruerer gyldige forespørgsler.

- **Funktions-eksekveringslogik**: Styrer, hvordan og hvornår værktøjer bliver kaldt baseret på brugerens intention og samtalekontekst. Dette kan inkludere planlægningsmoduler, routemekanismer eller betingede flows, der dynamisk bestemmer værktøjsbrug.

- **Beskedbehandlingssystem**: Komponenter, der håndterer konversationsflowet mellem brugerinput, LLM-responser, værktøjskald og værktøjsoutput.

- **Værktøjsintegrationsframework**: Infrastruktur, der forbinder agenten til forskellige værktøjer, uanset om de er simple funktioner eller komplekse eksterne tjenester.

- **Fejlhåndtering & validering**: Mekanismer til at håndtere fejl under værktøjseksekvering, validere parametre og håndtere uventede svar.

- **State Management**: Holder styr på samtalekontekst, tidligere værktøjsinteraktioner og persistent data for at sikre konsistens over flere trin i interaktionen.

Næste kigger vi nærmere på funktions-/værktøjskald.
 
### Funktions-/værktøjskald

Funktionskald er den primære måde, hvorpå vi giver store sprogmodeller (LLM'er) mulighed for at interagere med værktøjer. Du vil ofte se 'funktion' og 'værktøj' brugt lidt i flæng, fordi 'funktioner' (blokke af genanvendelig kode) er de 'værktøjer', agenterne bruger til at udføre opgaver. For at en funktionskode kan blive kaldt, skal en LLM sammenligne brugerens forespørgsel med funktionens beskrivelse. For at gøre dette sendes et skema indeholdende beskrivelserne af alle tilgængelige funktioner til LLM'en. LLM vælger derefter den mest passende funktion til opgaven og returnerer dens navn og argumenter. Den valgte funktion kaldes, svaret sendes tilbage til LLM, som bruger informationen til at svare på brugerens forespørgsel.

For at udviklere kan implementere funktionskald for agenter, skal du bruge:

1. En LLM-model, der understøtter funktionskald
2. Et skema indeholdende funktionsbeskrivelser
3. Koden for hver beskrevne funktion

Lad os bruge eksemplet med at få den nuværende tid i en by til at illustrere:

1. **Initialiser en LLM, der understøtter funktionskald:**

    Ikke alle modeller understøtter funktionskald, så det er vigtigt at sikre, at den LLM du bruger gør det.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> understøtter funktionskald. Vi kan starte med at initiere OpenAI-klienten via Azure OpenAI **Responses API** (den stabile `/openai/v1/` endpoint — ingen `api_version` nødvendig). 

    ```python
    # Initialiser OpenAI-klienten til Azure OpenAI (Responses API, v1-endpoint)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Opret et funktionsskema**:

    Dernæst definerer vi et JSON-skema, der indeholder funktionsnavnet, en beskrivelse af, hvad funktionen gør, samt navnene og beskrivelserne af funktionsparametrene.
    Vi sender derefter dette skema til den tidligere oprettede klient sammen med brugerens forespørgsel om at finde tiden i San Francisco. Det vigtige at bemærke er, at et **værktøjskald** er det, der returneres, **ikke** det endelige svar på spørgsmålet. Som nævnt tidligere returnerer LLM navnet på den funktion, den har valgt til opgaven, og de argumenter, der skal sendes med.

    ```python
    # Funktionsbeskrivelse for modellen at læse (Svar API fladt værktøjsformat)
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
  
    # Initial brugerbesked
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # Første API-kald: Bed modellen om at bruge funktionen
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # Responses API returnerer værktøjskald som function_call elementer i response.output.
    # Tilføj dem til samtalen, så modellen har fuld kontekst i næste omgang.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **Den nødvendige funktionskode for at udføre opgaven:**

    Nu hvor LLM har valgt, hvilken funktion der skal køres, skal koden, der udfører opgaven, implementeres og køre.
    Vi kan implementere koden til at hente den aktuelle tid i Python. Vi skal også skrive koden, der udtrækker navn og argumenter fra response_message for at få det endelige resultat.

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
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # Returner værktøjets resultat som et function_call_output-element
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # Andet API-kald: Få det endelige svar fra modellen
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

Funktionskald er kernen i det meste, hvis ikke alt, design af agentværktøjsbrug, men det kan nogle gange være udfordrende at implementere det fra bunden.
Som vi lærte i [Lektion 2](../../../02-explore-agentic-frameworks) giver agentiske frameworks os præbyggede byggesten til at implementere brug af værktøjer.
 
## Eksempler på brug af værktøjer med agentiske frameworks

Her er nogle eksempler på, hvordan du kan implementere designmønsteret for brug af værktøjer ved hjælp af forskellige agentiske frameworks:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> er et open-source AI-framework til at bygge AI-agenter. Det forenkler processen med at bruge funktionskald ved at lade dig definere værktøjer som Python-funktioner med `@tool` dekoratøren. Frameworket håndterer kommunikationen frem og tilbage mellem modellen og din kode. Det giver også adgang til præbyggede værktøjer som fil-søgning og kodefortolker gennem `FoundryChatClient`.

Det følgende diagram illustrerer processen med funktionskald i Microsoft Agent Framework:

![function calling](../../../translated_images/da/functioncalling-diagram.a84006fc287f6014.webp)

I Microsoft Agent Framework defineres værktøjer som dekorerede funktioner. Vi kan konvertere funktionen `get_current_time`, som vi så tidligere, til et værktøj ved at bruge `@tool` dekoratøren. Frameworket vil automatisk serialisere funktionen og dens parametre og skabe det skema, der sendes til LLM.

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Opret klienten
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Opret en agent og kør med værktøjet
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> er et nyere agentisk framework, der er designet til at gøre det muligt for udviklere sikkert at bygge, implementere og skalere AI-agenter af høj kvalitet og med udvidelsesmuligheder uden at skulle håndtere underliggende compute- og lagringsressourcer. Det er særligt nyttigt til enterprise-applikationer, da det er en fuldt administreret service med enterprise-grade sikkerhed.

Sammenlignet med at udvikle direkte med LLM API tilbyder Microsoft Foundry Agent Service nogle fordele, herunder:

- Automatisk kald af værktøjer – ingen grund til at parse et værktøjskald, kalde værktøjet og håndtere svar; alt dette sker nu på serversiden
- Sikkert styrede data – i stedet for at håndtere din egen tilstand i samtaler, kan du stole på tråde til at gemme alle de nødvendige oplysninger
- Værktøjer klar til brug – Værktøjer, du kan bruge til at interagere med dine datakilder, såsom Bing, Azure AI Search og Azure Functions.

Værktøjerne tilgængelige i Microsoft Foundry Agent Service kan opdeles i to kategorier:

1. Vidensværktøjer:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding med Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Fil-søgning</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Handlingsværktøjer:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Funktionskald</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Kodefortolker</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI-definerede værktøjer</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service giver os mulighed for at bruge disse værktøjer sammen som et `værktøjssæt`. Det bruger også `tråde`, som holder styr på historikken af beskeder fra en bestemt samtale.

Forestil dig, at du er en salgsagent i en virksomhed kaldet Contoso. Du vil udvikle en samtaleagent, der kan besvare spørgsmål om dine salgsdata.

Følgende billede illustrerer, hvordan du kan bruge Microsoft Foundry Agent Service til at analysere dine salgsdata:

![Agentic Service In Action](../../../translated_images/da/agent-service-in-action.34fb465c9a84659e.webp)

For at bruge nogen af disse værktøjer med servicen kan vi oprette en klient og definere et værktøj eller værktøjssæt. For at implementere dette praktisk kan vi bruge følgende Python-kode. LLM vil kunne se på værktøjssættet og beslutte, om den skal bruge den brugeroprettede funktion, `fetch_sales_data_using_sqlite_query`, eller den indbyggede Kodefortolker afhængigt af brugerens forespørgsel.

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

# Initialiser funktionskaldsagent med fetch_sales_data_using_sqlite_query funktionen og tilføj den til værktøjssættet
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Initialiser kodefortolker-værktøj og tilføj det til værktøjssættet.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Hvilke særlige overvejelser er der ved at bruge designmønsteret for brug af værktøjer til at bygge pålidelige AI-agenter?

En hyppig bekymring ved SQL, der dynamisk genereres af LLM'er, er sikkerhed, især risikoen for SQL-injektion eller ondsindede handlinger, såsom at slette eller manipulere databasen. Selvom disse bekymringer er berettigede, kan de effektivt afbødes ved korrekt konfiguration af databaseadgangstilladelser. For de fleste databaser indebærer det at konfigurere databasen som skrivebeskyttet. For databaser som PostgreSQL eller Azure SQL bør appen tildeles en skrivebeskyttet (SELECT) rolle.

At køre appen i et sikkert miljø øger beskyttelsen yderligere. I enterprise-scenarier udtrækkes og transformeres data typisk fra driftssystemer til en skrivebeskyttet database eller datalager med et brugervenligt skema. Denne tilgang sikrer, at data er sikre, optimeret til ydeevne og tilgængelighed, og at appen har begrænset, skrivebeskyttet adgang.

## Eksempel-koder

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Har du flere spørgsmål om designmønstre for brug af værktøjer?

Deltag i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for at møde andre lærende, deltage i kontortimer og få besvaret dine spørgsmål om AI-agenter.

## Yderligere ressourcer

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework Oversigt</a>


## Forrige lektion

[Forståelse af Agentiske Designmønstre](../03-agentic-design-patterns/README.md)

## Næste lektion

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->