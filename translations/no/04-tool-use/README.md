[![Hvordan designe gode AI-agenter](../../../translated_images/no/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klikk på bildet over for å se videoen av denne leksjonen)_

# Verktøybruk Designmønster

Verktøy er interessante fordi de gir AI-agenter et bredere spekter av evner. I stedet for at agenten har et begrenset sett med handlinger den kan utføre, kan agenten nå utføre et bredt spekter av handlinger ved å legge til et verktøy. I dette kapitlet skal vi se på Verktøybruk Designmønster, som beskriver hvordan AI-agenter kan bruke spesifikke verktøy for å nå sine mål.

## Introduksjon

I denne leksjonen ønsker vi å svare på følgende spørsmål:

- Hva er verktøybruk designmønsteret?
- Hvilke bruksområder kan det anvendes på?
- Hva er elementene/bygningsblokkene som trengs for å implementere designmønsteret?
- Hva er spesielle hensyn ved bruk av Verktøybruk Designmønster for å bygge pålitelige AI-agenter?

## Læringsmål

Etter å ha fullført denne leksjonen vil du kunne:

- Definere Verktøybruk Designmønster og dets formål.
- Identifisere bruksområder hvor Verktøybruk Designmønster er anvendelig.
- Forstå nøkkel-elementene som trengs for å implementere designmønsteret.
- Gjenkjenne hensyn for å sikre pålitelighet i AI-agenter som bruker dette designmønsteret.

## Hva er Verktøybruk Designmønster?

**Verktøybruk Designmønster** fokuserer på å gi LLM-er muligheten til å samhandle med eksterne verktøy for å oppnå spesifikke mål. Verktøy er kode som kan utføres av en agent for å utføre handlinger. Et verktøy kan være en enkel funksjon som en kalkulator, eller et API-kall til en tredjepartstjeneste som aksjekursinnhenting eller værmelding. I konteksten av AI-agenter er verktøy designet for å bli utført av agenter som svar på **modell-genererte funksjonskall**.

## Hvilke bruksområder kan det anvendes på?

AI-agenter kan benytte verktøy for å fullføre komplekse oppgaver, hente informasjon eller ta beslutninger. Verktøybruk designmønster brukes ofte i scenarioer som krever dynamisk interaksjon med eksterne systemer, som databaser, webtjenester eller kodefortolkere. Denne evnen er nyttig for en rekke ulike bruksområder, inkludert:

- **Dynamisk informasjonsinnhenting:** Agenter kan spørre eksterne API-er eller databaser for å hente oppdatert data (f.eks. å spørre en SQLite-database for dataanalyse, hente aksjekurser eller værinformasjon).
- **Kodeutførelse og fortolkning:** Agenter kan kjøre kode eller skript for å løse matematiske problemer, generere rapporter eller utføre simuleringer.
- **Automatisering av arbeidsflyt:** Automatisere repetitive eller flertrinns arbeidsflyter ved å integrere verktøy som tidsplanleggere, e-posttjenester eller datapipelines.
- **Kundesupport:** Agenter kan samhandle med CRM-systemer, billettplattformer eller kunnskapsbaser for å løse brukerhenvendelser.
- **Innholdsgenerering og redigering:** Agenter kan bruke verktøy som grammatikkontroll, tekstoppsummering eller innholdssikkerhetsvurderinger for å hjelpe med innholdsproduksjon.

## Hva er elementene/bygningsblokkene som trengs for å implementere verktøybruk designmønster?

Disse bygningsblokkene lar AI-agenten utføre et bredt spekter av oppgaver. La oss se på nøkelelementene som trengs for å implementere Verktøybruk Designmønster:

- **Funksjon/Verktøy Skjemaer:** Detaljerte definisjoner av tilgjengelige verktøy, inkludert funksjonsnavn, formål, nødvendige parametere og forventede utdata. Disse skjemaene lar LLM forstå hvilke verktøy som er tilgjengelige og hvordan å konstruere gyldige forespørsler.

- **Funksjonsutførelseslogikk:** Styrer hvordan og når verktøy kalles basert på brukerens intensjon og samtalekontekst. Dette kan inkludere planleggingsmoduler, rutingsmekanismer eller betingede flyter som dynamisk bestemmer verktøybruk.

- **Meldingshåndteringssystem:** Komponenter som administrerer samtaleflyten mellom brukerinput, LLM-svar, verktøykall og verktøyutdata.

- **Verktøyintegrasjonsrammeverk:** Infrastruktur som kobler agenten til ulike verktøy, enten det er enkle funksjoner eller komplekse eksterne tjenester.

- **Feilhåndtering & Validering:** Mekanismer for å håndtere feil i verktøyutførelse, validere parametere og håndtere uventede svar.

- **Statusstyring:** Sporer samtalekontekst, tidligere verktøyinteraksjoner og persistente data for å sikre konsistens på tvers av flerstegskommunikasjon.

La oss nå se nærmere på Funksjons-/Verktøykalling.
 
### Funksjons-/Verktøykalling

Funksjonskalling er hovedmåten vi gjør det mulig for store språkmodeller (LLM) å samhandle med verktøy. Du vil ofte se 'Funksjon' og 'Verktøy' brukt om hverandre fordi 'funksjoner' (blokker av gjenbrukbar kode) er 'verktøyene' agenter bruker for å utføre oppgaver. For at koden til en funksjon skal kunne kalles, må en LLM sammenligne brukerens forespørsel med funksjonens beskrivelse. For å gjøre dette sendes et skjema som inneholder beskrivelsene av alle tilgjengelige funksjoner til LLM. LLM velger så den mest passende funksjonen for oppgaven og returnerer dens navn og argumenter. Den valgte funksjonen kalles, svaret sendes tilbake til LLM, som bruker informasjonen til å svare brukerens forespørsel.

For utviklere som vil implementere funksjonskalling for agenter, trenger du:

1. En LLM-modell som støtter funksjonskalling
2. Et skjema med funksjonsbeskrivelser
3. Koden for hver funksjon som er beskrevet

La oss bruke eksempelet med å hente gjeldende tid i en by for å illustrere:

1. **Initialiser en LLM som støtter funksjonskalling:**

    Ikke alle modeller støtter funksjonskalling, så det er viktig å sjekke at LLM-en du bruker gjør det.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> støtter funksjonskalling. Vi kan starte med å initiere OpenAI-klienten mot Azure OpenAI **Responses API** (det stabile `/openai/v1/` endepunktet — ingen `api_version` nødvendig). 

    ```python
    # Initialiser OpenAI-klienten for Azure OpenAI (Responses API, v1-endepunkt)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Lag et Funksjonsskjema**:

    Deretter definerer vi et JSON-skjema som inneholder funksjonsnavnet, beskrivelse av hva funksjonen gjør, og navn og beskrivelser av funksjonsparametrene.
    Vi tar så dette skjemaet og sender det til klienten som ble opprettet tidligere, sammen med brukerens forespørsel om å finne tiden i San Francisco. Det som er viktig å merke seg er at et **verktøykall** er det som returneres, **ikke** det endelige svaret på spørsmålet. Som nevnt tidligere returnerer LLM navnet på funksjonen den valgte for oppgaven, og argumentene som vil bli sendt til den.

    ```python
    # Funksjonsbeskrivelse for modellen å lese (Responses API flat verktøyformat)
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
  
    # Første melding fra brukeren
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # Første API-kall: Be modellen om å bruke funksjonen
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # Responses API returnerer verktøykall som function_call-elementer i response.output.
    # Legg dem til i samtalen slik at modellen har full kontekst i neste runde.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **Funksjonskoden som kreves for å utføre oppgaven:**

    Nå som LLM har valgt hvilken funksjon som må kjøres, må koden som utfører oppgaven implementeres og utføres.
    Vi kan implementere koden for å hente gjeldende tid i Python. Vi må også skrive koden for å hente ut navn og argumenter fra response_message for å få det endelige resultatet.

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
    # Håndter funksjonskall
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # Returner verktøyresultatet som et function_call_output-element
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # Andre API-kall: Hent det endelige svaret fra modellen
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

Funksjonskalling er kjernen i de fleste, om ikke alle, agentverktøybrukdesign, men det kan noen ganger være utfordrende å implementere det fra bunnen av.
Som vi lærte i [Leksjon 2](../../../02-explore-agentic-frameworks) gir agentiske rammeverk oss forhåndsbygde bygningsblokker for å implementere verktøybruk.
 
## Eksempler på verktøybruk med agentiske rammeverk

Her er noen eksempler på hvordan du kan implementere Verktøybruk Designmønster ved bruk av forskjellige agentiske rammeverk:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> er et åpen kildekode AI-rammeverk for å bygge AI-agenter. Det forenkler prosessen med å bruke funksjonskalling ved at du kan definere verktøy som Python-funksjoner med `@tool` dekoratør. Rammeverket håndterer kommunikasjonen frem og tilbake mellom modellen og koden din. Det gir også tilgang til forhåndsbygde verktøy som Fil-søk og Kodefortolker gjennom `FoundryChatClient`.

Følgende diagram illustrerer prosessen med funksjonskalling med Microsoft Agent Framework:

![funksjonskalling](../../../translated_images/no/functioncalling-diagram.a84006fc287f6014.webp)

I Microsoft Agent Framework defineres verktøy som dekorerte funksjoner. Vi kan konvertere funksjonen `get_current_time` vi så tidligere til et verktøy ved å bruke `@tool` dekoratøren. Rammeverket vil automatisk serialisere funksjonen og dens parametere, og lage skjemaet som sendes til LLM.

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Opprett klienten
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Opprett en agent og kjør med verktøyet
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> er et nyere agentisk rammeverk designet for å gjøre det mulig for utviklere å sikkert bygge, distribuere og skalere høykvalitets og utvidbare AI-agenter uten å måtte håndtere underliggende databehandling og lagringsressurser. Det er spesielt nyttig for bedriftsapplikasjoner siden det er en fullstendig administrert tjeneste med bedriftsgradert sikkerhet.

Sammenlignet med utvikling direkte med LLM API, gir Microsoft Foundry Agent Service noen fordeler, inkludert:

- Automatisk verktøykalling – ingen behov for å analysere et verktøykall, kalle verktøyet og håndtere svaret; alt dette gjøres nå på serversiden
- Sikkert administrerte data – i stedet for å håndtere din egen samtalestatus, kan du stole på tråder for å lagre all informasjon du trenger
- Umiddelbart tilgjengelige verktøy – Verktøy du kan bruke til å samhandle med datakilder, som Bing, Azure AI Search og Azure Functions.

Verktøyene tilgjengelige i Microsoft Foundry Agent Service kan deles inn i to kategorier:

1. Kunnskapsverktøy:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Forankring med Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Fil-søk</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Aksjonsverktøy:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Funksjonskalling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Kodefortolker</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI-definerte verktøy</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agenttjenesten lar oss bruke disse verktøyene sammen som et `toolset`. Den bruker også `threads` som holder oversikt over meldingshistorikken fra en bestemt samtale.

Forestill deg at du er en salgsagent i et selskap som heter Contoso. Du vil utvikle en samtaleagent som kan svare på spørsmål om salgstallene dine.

Følgende bilde illustrerer hvordan du kan bruke Microsoft Foundry Agent Service til å analysere salgstallene dine:

![Agenttjeneste i aksjon](../../../translated_images/no/agent-service-in-action.34fb465c9a84659e.webp)

For å bruke noen av disse verktøyene med tjenesten kan vi lage en klient og definere et verktøy eller verktøysett. For å implementere dette praktisk kan vi bruke følgende Python-kode. LLM vil kunne se på verktøysettet og avgjøre om den skal bruke brukeropprettet funksjon, `fetch_sales_data_using_sqlite_query`, eller den forhåndsbygde Kodefortolkeren basert på brukerens forespørsel.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query funksjon som kan finnes i en fil kalt fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initialiser verktøysett
toolset = ToolSet()

# Initialiser funksjonsanropsagent med fetch_sales_data_using_sqlite_query funksjonen og legg den til i verktøysettet
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Initialiser kodeinterpreterverktøy og legg det til i verktøysettet.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Hva er spesielle hensyn ved bruk av Verktøybruk Designmønster for å bygge pålitelige AI-agenter?

En vanlig bekymring med SQL som dynamisk genereres av LLM-er er sikkerhet, spesielt risikoen for SQL-injeksjon eller ondsinnede handlinger, som å slette eller tukle med databasen. Selv om disse bekymringene er gyldige, kan de effektivt reduseres ved å konfigurere database-tilgangstillatelser riktig. For de fleste databaser innebærer dette å konfigurere databasen som skrivebeskyttet. For databaseservicer som PostgreSQL eller Azure SQL bør appen tildeles en lese-only (SELECT) rolle.

Å kjøre appen i et sikkert miljø forbedrer beskyttelsen ytterligere. I bedriftscenarioer blir data vanligvis hentet ut og transformert fra operative systemer inn i en skrivebeskyttet database eller datavarehus med et brukervennlig skjema. Denne tilnærmingen sikrer at dataene er sikre, optimalisert for ytelse og tilgjengelighet, og at appen har begrenset, skrivebeskyttet tilgang.

## Eksempelkoder

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Har du flere spørsmål om Verktøybruk Designmønstre?

Bli med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for å møte andre lærende, delta på kontortid og få svar på dine AI-agent-spørsmål.

## Ytterligere ressurser

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework Oversikt</a>


## Røyktesting av denne agenten (valgfritt)

Etter at du har lært å distribuere agenter i [Leksjon 16](../16-deploying-scalable-agents/README.md), kan du røykteste denne leksjonens `TravelToolAgent` (kaller den fortsatt verktøyene sine og svarer?) med [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json). Se [`tests/README.md`](../tests/README.md) for hvordan du kjører den.

## Forrige leksjon

[Forstå agentiske designmønstre](../03-agentic-design-patterns/README.md)

## Neste leksjon

[Agentisk RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->