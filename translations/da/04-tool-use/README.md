[![Hvordan man designer gode AI-agenter](../../../translated_images/da/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klik på billedet ovenfor for at se videoen til denne lektion)_

# Tool Use Design Pattern

Værktøjer er interessante, fordi de giver AI-agenter mulighed for at have et bredere udvalg af kapaciteter. I stedet for at agenten kun har et begrænset sæt handlinger, den kan udføre, kan den med et værktøj nu udføre en lang række handlinger. I dette kapitel vil vi se på Tool Use Design Pattern, som beskriver, hvordan AI-agenter kan bruge specifikke værktøjer for at opnå deres mål.

## Introduktion

I denne lektion søger vi at besvare følgende spørgsmål:

- Hvad er Tool Use Design Pattern?
- Hvilke brugstilfælde kan den anvendes til?
- Hvilke elementer/byggesten er nødvendige for at implementere designmønstret?
- Hvilke særlige overvejelser er der ved at bruge Tool Use Design Pattern til at bygge pålidelige AI-agenter?

## Læringsmål

Efter at have gennemført denne lektion vil du være i stand til at:

- Definere Tool Use Design Pattern og dets formål.
- Identificere brugstilfælde, hvor Tool Use Design Pattern er anvendeligt.
- Forstå de nøgleelementer, der er nødvendige for at implementere designmønstret.
- Genkende overvejelser for at sikre pålidelighed i AI-agenter, der bruger dette designmønster.

## Hvad er Tool Use Design Pattern?

**Tool Use Design Pattern** fokuserer på at give LLM'er muligheden for at interagere med eksterne værktøjer for at opnå specifikke mål. Værktøjer er kode, som en agent kan udføre for at foretage handlinger. Et værktøj kan være en simpel funktion som en lommeregner eller et API-kald til en tredjepartstjeneste som aktiekurstjek eller vejrudsigt. I forbindelse med AI-agenter er værktøjerne designet til at blive udført af agenter som svar på **modelgenererede funktionskald**.

## Hvilke brugstilfælde kan den anvendes til?

AI-agenter kan udnytte værktøjer til at udføre komplekse opgaver, hente information eller træffe beslutninger. Tool Use Design Pattern bruges ofte i scenarier, der kræver dynamisk interaktion med eksterne systemer, såsom databaser, webtjenester eller kodefortolkere. Denne evne er nyttig i flere forskellige brugstilfælde, herunder:

- **Dynamisk informationshentning:** Agenter kan forespørge eksterne API'er eller databaser for at hente opdaterede data (f.eks. forespørgsler i en SQLite-database til dataanalyse, hentning af aktiekurser eller vejrdata).
- **Kodeeksekvering og fortolkning:** Agenter kan udføre kode eller scripts for at løse matematiske problemer, generere rapporter eller lave simuleringer.
- **Workflow-automatisering:** Automatisering af gentagne eller flertrinsarbejdsgange ved at integrere værktøjer som opgaveplanlæggere, e-mail-tjenester eller datapipelines.
- **Kundesupport:** Agenter kan interagere med CRM-systemer, supportsystemer eller vidensbaser for at løse brugerforespørgsler.
- **Indholdsgenerering og redigering:** Agenter kan bruge værktøjer som grammatikcheckere, tekstopsummatorer eller indholdssikkerhedsvurderinger til at hjælpe med indholdsopgaver.

## Hvilke elementer/byggesten er nødvendige for at implementere Tool Use Design Pattern?

Disse byggesten gør det muligt for AI-agenten at udføre et bredt spektrum af opgaver. Lad os se på de vigtigste elementer, der er nødvendige for at implementere Tool Use Design Pattern:

- **Funktions-/værktøjsskemaer**: Detaljerede definitioner af tilgængelige værktøjer, inklusive funktionsnavn, formål, nødvendige parametre og forventede outputs. Disse skemaer gør det muligt for LLM at forstå, hvilke værktøjer der er tilgængelige, og hvordan man konstruerer gyldige forespørgsler.

- **Funktionsudførelseslogik**: Styrer hvornår og hvordan værktøjer påkaldes baseret på brugerens hensigt og samtalekontekst. Dette kan inkludere planlægningsmoduler, rutealgoritmer eller betingede flow, der dynamisk bestemmer værktøjsbrug.

- **Beskedhåndteringssystem**: Komponenter der håndterer samtaleflowet mellem brugerinput, LLM-svar, værktøjskald og værktøjsoutput.

- **Værktøjsintegrationsrammeværk**: Infrastruktur, der forbinder agenten med forskellige værktøjer, hvad enten det er simple funktioner eller komplekse eksterne tjenester.

- **Fejlhåndtering og validering**: Mekanismer til at håndtere fejl i værktøjsudførelse, validere parametre og håndtere uventede svar.

- **Tilstandsstyring**: Holder styr på samtalekontekst, tidligere værktøjsinteraktioner og persistent data for at sikre konsistens på tværs af flertrinsinteraktioner.

Lad os nu se nærmere på Funktions-/værktøjskald.
 
### Funktions-/værktøjskald

Funktionskald er den primære måde, hvorpå vi gør det muligt for Large Language Models (LLM'er) at interagere med værktøjer. Du vil ofte se 'Function' og 'Tool' brugt om hinanden, fordi 'funktioner' (genanvendelige kodeblokke) er de 'værktøjer', agenter bruger til at udføre opgaver. For at en funktions kode kan påkaldes, skal LLM sammenligne brugerens forespørgsel med funktionens beskrivelse. Til det sendes et skema, der indeholder beskrivelserne af alle tilgængelige funktioner, til LLM'en. LLM'en vælger derefter den mest passende funktion til opgaven og returnerer dens navn og argumenter. Den valgte funktion påkaldes, dens svar sendes tilbage til LLM'en, som bruger informationen til at svare på brugerens forespørgsel.

For udviklere, der vil implementere funktionskald til agenter, skal du bruge:

1. En LLM-model, der understøtter funktionskald
2. Et skema med funktionsbeskrivelser
3. Koden til hver beskrevne funktion

Lad os bruge eksemplet med at hente det aktuelle klokkeslæt i en by til at illustrere:

1. **Initialiser en LLM, der understøtter funktionskald:**

    Ikke alle modeller understøtter funktionskald, så det er vigtigt at tjekke, at den LLM, du bruger, gør.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> understøtter funktionskald. Vi kan starte med at initialisere OpenAI klienten mod Azure OpenAI **Responses API** (den stabile `/openai/v1/` endpoint — uden `api_version`). 

    ```python
    # Initialiser OpenAI-klienten til Azure OpenAI (Responses API, v1-endpoint)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Opret et funktionsskema**:

    Dernæst definerer vi et JSON-skema, der indeholder funktionsnavn, beskrivelse af hvad funktionen gør, samt navnene og beskrivelserne af funktionsparametrene.
    Vi sender så dette skema til klienten, som vi oprettede tidligere, sammen med brugerens forespørgsel om at finde tiden i San Francisco. Det vigtige at bemærke er, at et **værktøjskald** er det, der returneres, **ikke** det endelige svar på spørgsmålet. Som nævnt tidligere returnerer LLM navnet på den funktion, den valgte til opgaven, samt argumenterne, der passerer til den.

    ```python
    # Funktionsbeskrivelse for modellen at læse (Responses API flat tool format)
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
  
    # Initielt brugermeddelelse
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
    # Tilføj dem til samtalen, så modellen har fuld kontekst ved næste omgang.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **Funktionens kode, der skal udføre opgaven:**

    Nu, hvor LLM har valgt, hvilken funktion der skal køres, skal koden, der udfører opgaven, implementeres og udføres.
    Vi kan implementere koden til at hente det aktuelle klokkeslæt i Python. Vi skal også skrive koden til at udtrække navn og argumenter fra response_message for at få det endelige resultat.

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

    # Andet API-kald: Hent det endelige svar fra modellen
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

Funktionskald er kernen i de fleste, hvis ikke alle, agent-værktøjsbrugsmønstre, men implementering fra bunden kan nogle gange være udfordrende.
Som vi lærte i [Lektion 2](../../../02-explore-agentic-frameworks) giver agentiske frameworks os færdige byggesten til at implementere værktøjsbrug.
 
## Værktøjsbrugs Eksempler med Agentiske Frameworks

Her er nogle eksempler på, hvordan du kan implementere Tool Use Design Pattern ved brug af forskellige agentiske frameworks:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> er et open-source AI-framework til at bygge AI-agenter. Det forenkler processen med at bruge funktionskald ved at lade dig definere værktøjer som Python-funktioner med `@tool` dekorationen. Frameworket håndterer kommunikationen frem og tilbage mellem modellen og din kode. Det giver også adgang til færdigbyggede værktøjer som File Search og Code Interpreter via `FoundryChatClient`.

Følgende diagram illustrerer processen med funktionskald i Microsoft Agent Framework:

![function calling](../../../translated_images/da/functioncalling-diagram.a84006fc287f6014.webp)

I Microsoft Agent Framework defineres værktøjer som decorerede funktioner. Vi kan omdanne `get_current_time` funktionen, vi så tidligere, til et værktøj ved at bruge `@tool` dekoratoren. Frameworket vil automatisk serialisere funktionen og dens parametre og skabe det skema, der sendes til LLM.

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

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> er et nyere agentisk framework, der er designet til at give udviklere mulighed for sikkert at bygge, implementere og skalere AI-agenter af høj kvalitet og udvidelige AI-agenter uden at skulle administrere den underliggende compute- og lagringsressourcer. Det er særlig nyttigt til virksomhedsapplikationer, da det er en fuldt administreret service med sikkerhed i virksomhedskvalitet.

Sammenlignet med udvikling direkte med LLM API'en tilbyder Microsoft Foundry Agent Service flere fordele, herunder:

- Automatisk værktøjskald – ingen behov for at parse et værktøjskald, påkalde værktøjet og håndtere svaret; alt dette håndteres nu server-side
- Sikkert administrerede data – i stedet for at styre din egen samtalestatus, kan du stole på threads til at gemme al den information, du har brug for
- Værktøjer klar til brug – værktøjer, du kan bruge til at interagere med dine datakilder, som Bing, Azure AI Search og Azure Functions.

De værktøjer, der er tilgængelige i Microsoft Foundry Agent Service, kan opdeles i to kategorier:

1. Vidensværktøjer:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding med Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">File Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Handlingsværktøjer:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Funktionskald</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI-definerede værktøjer</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service gør det muligt at bruge disse værktøjer samlet som en `toolset`. Den bruger også `threads`, som holder styr på historikken af beskeder fra en bestemt samtale.

Forestil dig, at du er salgsagent i en virksomhed kaldet Contoso. Du ønsker at udvikle en samtaleagent, der kan besvare spørgsmål om dine salgsdata.

Følgende billede illustrerer, hvordan du kunne bruge Microsoft Foundry Agent Service til at analysere dine salgsdata:

![Agentisk Service i Aktion](../../../translated_images/da/agent-service-in-action.34fb465c9a84659e.webp)

For at bruge nogle af disse værktøjer med servicen kan vi oprette en klient og definere et værktøj eller en toolset. For at implementere dette praktisk kan vi bruge følgende Python-kode. LLM vil kunne se på toolset'et og beslutte, om den skal bruge den brugerdefinerede funktion `fetch_sales_data_using_sqlite_query` eller den indbyggede Code Interpreter, afhængigt af brugerens forespørgsel.

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

# Initialiser funktionskaldsagent med funktionen fetch_sales_data_using_sqlite_query og tilføj den til værktøjssættet
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Initialiser kodefortolker værktøj og tilføj det til værktøjssættet.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Hvilke særlige overvejelser er der ved at bruge Tool Use Design Pattern til at bygge pålidelige AI-agenter?

En almindelig bekymring ved dynamisk SQL genereret af LLM'er er sikkerhed, især risikoen for SQL-injektion eller skadelige handlinger som at droppe eller manipulere med databasen. Selvom disse bekymringer er berettigede, kan de effektivt imødegås ved korrekt konfiguration af databaseadgangstilladelser. For de fleste databaser indebærer det at konfigurere databasen som skrivebeskyttet. For databaseservices som PostgreSQL eller Azure SQL bør appen tildeles en skrivebeskyttet (SELECT) rolle.

Kørsel af appen i et sikkert miljø forbedrer beskyttelsen yderligere. I virksomheds-scenarier bliver data typisk ekstraheret og transformeret fra operationelle systemer til en skrivebeskyttet database eller datawarehouse med et brugervenligt skema. Denne tilgang sikrer, at data er sikre, optimeret til ydeevne og tilgængelighed, og at appen har begrænset, skrivebeskyttet adgang.

## Eksempelkoder

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Har du flere spørgsmål om Tool Use Design Pattern?

Deltag i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for at møde andre lærende, deltage i kontortimer og få besvaret dine spørgsmål om AI-agenter.

## Yderligere ressourcer

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework Oversigt</a>


## Røgtest af denne agent (valgfrit)

Efter du har lært at implementere agenter i [Lektion 16](../16-deploying-scalable-agents/README.md), kan du røgteste denne lektions `TravelToolAgent` (kalder den stadig sine værktøjer og svarer?) med [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json). Se [`tests/README.md`](../tests/README.md) for, hvordan du kører den.

## Forrige lektion

[Forståelse af agentiske designmønstre](../03-agentic-design-patterns/README.md)

## Næste lektion

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->