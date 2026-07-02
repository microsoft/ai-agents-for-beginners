[![Hvordan designe gode AI-agenter](../../../translated_images/no/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klikk på bildet over for å se video av denne leksjonen)_

# Designmønster for bruk av verktøy

Verktøy er interessante fordi de gir AI-agenter et bredere spekter av muligheter. I stedet for at agenten har et begrenset sett med handlinger den kan utføre, kan agenten nå utføre et bredt spekter av handlinger ved å legge til et verktøy. I dette kapitlet vil vi se på Designmønsteret for bruk av verktøy, som beskriver hvordan AI-agenter kan bruke spesifikke verktøy for å oppnå sine mål.

## Introduksjon

I denne leksjonen ønsker vi å besvare følgende spørsmål:

- Hva er designmønsteret for bruk av verktøy?
- Hvilke bruksområder kan det brukes til?
- Hvilke elementer/byggeklosser trengs for å implementere designmønsteret?
- Hvilke spesielle hensyn må tas ved bruk av designmønsteret for å bygge pålitelige AI-agenter?

## Læringsmål

Etter å ha fullført denne leksjonen vil du kunne:

- Definere designmønsteret for bruk av verktøy og dets formål.
- Identifisere bruksområder der designmønsteret for bruk av verktøy er aktuelt.
- Forstå de viktigste elementene som trengs for å implementere designmønsteret.
- Gjenkjenne hensyn for å sikre pålitelighet i AI-agenter som bruker dette designmønsteret.

## Hva er designmønsteret for bruk av verktøy?

**Designmønsteret for bruk av verktøy** fokuserer på å gi LLM-er muligheten til å samhandle med eksterne verktøy for å oppnå spesifikke mål. Verktøy er kode som kan kjøres av en agent for å utføre handlinger. Et verktøy kan være en enkel funksjon som en kalkulator, eller et API-kall til en tredjepartstjeneste som aksjekursoppslag eller værmelding. I sammenheng med AI-agenter er verktøy designet for å bli kjørt av agenter som svar på **funksjonsanrop generert av modellen**.

## Hvilke bruksområder kan det brukes til?

AI-agenter kan bruke verktøy for å fullføre komplekse oppgaver, hente informasjon eller ta beslutninger. Designmønsteret for bruk av verktøy brukes ofte i scenarier som krever dynamisk interaksjon med eksterne systemer, som databaser, webtjenester eller kodeinterpreterere. Denne evnen er nyttig for flere ulike bruksområder, inkludert:

- **Dynamisk informasjonsinnhenting:** Agenter kan spørre eksterne API-er eller databaser for å hente oppdaterte data (f.eks. spørsmål til en SQLite-database for dataanalyse, hente aksjekurser eller værinformasjon).
- **Kodekjøring og tolkning:** Agenter kan kjøre kode eller skript for å løse matematiske problemer, generere rapporter eller utføre simuleringer.
- **Automatisering av arbeidsflyt:** Automatisering av repeterende eller flertrinns arbeidsflyter ved å integrere verktøy som tidsplanleggere, e-posttjenester eller datapipelines.
- **Kundesupport:** Agenter kan samhandle med CRM-systemer, billetteringsplattformer eller kunnskapsbaser for å løse brukerhenvendelser.
- **Innholdsproduksjon og redigering:** Agenter kan bruke verktøy som grammatikkontroll, tekstoppsummering eller innholdssikkerhetsevaluering for å hjelpe til med innholdsproduksjon.

## Hvilke elementer/byggeklosser trengs for å implementere designmønsteret for bruk av verktøy?

Disse byggeklossene gjør det mulig for AI-agenten å utføre et bredt spekter av oppgaver. La oss se på de viktigste elementene som trengs for å implementere Designmønsteret for bruk av verktøy:

- **Funksjon-/verktøyskjemas:** Detaljerte definisjoner av tilgjengelige verktøy, inkludert funksjonsnavn, formål, nødvendige parametere og forventede utdata. Disse skjemaene gjør det mulig for LLM å forstå hvilke verktøy som er tilgjengelige og hvordan man konstruerer gyldige forespørsler.

- **Logikk for funksjonsutførelse:** Styrer hvordan og når verktøy kalles basert på brukerens intensjon og samtalekontekst. Dette kan inkludere planleggingsmoduler, rutingmekanismer eller betingede flyter som bestemmer verktøybruk dynamisk.

- **Meldingshåndteringssystem:** Komponenter som administrerer samtaleflyten mellom brukerinput, LLM-responser, verktøysamtaler og verktøyutdata.

- **Verktøyintegrasjonsrammeverk:** Infrastruktur som kobler agenten til ulike verktøy, enten det er enkle funksjoner eller komplekse eksterne tjenester.

- **Feilhåndtering og validering:** Mekanismer for å håndtere feil i verktøyutførelse, validere parametere og håndtere uventede svar.

- **Tilstandshåndtering:** Sporer samtalekontekst, tidligere verktøyinteraksjoner og vedvarende data for å sikre konsistens på tvers av flerstegsinteraksjoner.

Neste steg er å se nærmere på Funksjons-/verktøysanrop.

### Funksjons-/verktøysanrop

Funksjonsanrop er den primære måten vi gjør det mulig for store språkmodeller (LLM) å samhandle med verktøy. Du vil ofte se 'funksjon' og 'verktøy' brukt om hverandre fordi 'funksjoner' (blokker med gjenbrukbar kode) er 'verktøyene' agenter bruker for å utføre oppgaver. For at en funksjonskode skal kunne kalles, må en LLM sammenligne brukerens forespørsel med funksjonens beskrivelse. For å gjøre dette sendes et skjema som inneholder beskrivelsene av alle tilgjengelige funksjoner til LLM. LLM velger deretter den mest passende funksjonen til oppgaven og returnerer navnet og argumentene for den. Den valgte funksjonen kalles, og svaret sendes tilbake til LLM, som bruker informasjonen til å svare på brukerens forespørsel.

For at utviklere skal kunne implementere funksjonsanrop for agenter, trenger du:

1. En LLM-modell som støtter funksjonsanrop
2. Et skjema som inneholder funksjonsbeskrivelser
3. Koden for hver funksjon som er beskrevet

La oss illustrere med eksempelet å hente nåværende tid i en by:

1. **Initialiser en LLM som støtter funksjonsanrop:**

    Ikke alle modeller støtter funksjonsanrop, så det er viktig å sjekke at LLM-en du bruker gjør det. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> støtter funksjonsanrop. Vi kan begynne med å initialisere Azure OpenAI-klienten.

    ```python
    # Initialiser Azure OpenAI-klienten
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Lag et funksjonsskjema:**

    Deretter definerer vi et JSON-skjema som inneholder funksjonsnavn, beskrivelse av hva funksjonen gjør, samt navn og beskrivelser av funksjonsparametrene.
    Vi sender dette skjemaet til klienten vi opprettet tidligere, sammen med brukerens forespørsel om å finne tiden i San Francisco. Det som er viktig å merke seg er at et **verktøysamtale** returneres, **ikke** det endelige svaret på spørsmålet. Som nevnt tidligere returnerer LLM navnet på funksjonen den valgte for oppgaven og argumentene som skal gis funksjonen.

    ```python
    # Funksjonsbeskrivelse for modellen å lese
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
  
    # Initial brukerbeskjed
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Første API-kall: Be modellen bruke funksjonen
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Behandle modellens svar
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Den nødvendige funksjonskoden for å utføre oppgaven:**

    Nå som LLM har valgt hvilken funksjon som skal kjøres, må koden som utfører oppgaven implementeres og kjøres.
    Vi kan implementere koden for å hente nåværende tid i Python. Vi må også skrive kode for å trekke ut navn og argumenter fra response_message for å få det endelige resultatet.

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
  
      # Andre API-kall: Hent det endelige svaret fra modellen
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

Funksjonsanrop er kjernen i det meste, om ikke all agentverktøybruk, men det kan tidvis være utfordrende å implementere fra bunnen av.
Som vi lærte i [Leksjon 2](../../../02-explore-agentic-frameworks) gir agentrammeverk oss forhåndsbygde byggeklosser for å implementere verktøybruk.

## Eksempler på bruk av verktøy med agentrammeverk

Her er noen eksempler på hvordan du kan implementere designmønsteret for bruk av verktøy ved å bruke ulike agentrammeverk:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> er et åpen kildekode AI-rammeverk for å bygge AI-agenter. Det forenkler prosessen med å bruke funksjonsanrop ved at du kan definere verktøy som Python-funksjoner med `@tool` dekoratøren. Rammeverket håndterer kommunikasjonen frem og tilbake mellom modellen og koden din. Det gir også tilgang til forhåndsbygde verktøy som Fil-søk og Kodeinterpreter gjennom `AzureAIProjectAgentProvider`.

Følgende diagram illustrerer prosessen med funksjonsanrop med Microsoft Agent Framework:

![function calling](../../../translated_images/no/functioncalling-diagram.a84006fc287f6014.webp)

I Microsoft Agent Framework er verktøy definert som dekorerte funksjoner. Vi kan konvertere funksjonen `get_current_time` vi så tidligere til et verktøy ved å bruke `@tool` dekoratøren. Rammeverket vil automatisk serialisere funksjonen og dens parametere, og lage skjemaet som sendes til LLM.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Opprett klienten
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Opprett en agent og kjør med verktøyet
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> er et nyere agentrammeverk som er designet for å gi utviklere mulighet til å sikkert bygge, distribuere og skalere høy-kvalitets, og utvidbare AI-agenter uten å måtte administrere underliggende databehandling og lagringsressurser. Det er spesielt nyttig for bedriftsapplikasjoner siden det er en fullt administrert tjeneste med sikkerhet på bedriftsnivå.

Sammenlignet med å utvikle direkte med LLM API, gir Azure AI Agent Service noen fordeler, blant annet:

- Automatisk verktøysanrop – ingen behov for å analysere et verktøysanrop, kalle verktøyet og håndtere svaret; alt dette gjøres nå på serversiden
- Sikkert administrerte data – i stedet for å administrere din egen samtalestatus kan du stole på tråder for å lagre all informasjon du trenger
- Ferdige verktøy – Verktøy du kan bruke for å samhandle med datakildene dine, som Bing, Azure AI Search og Azure Functions.

Verktøyene som er tilgjengelige i Azure AI Agent Service kan deles i to kategorier:

1. Kunnskapsverktøy:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grunnlag med Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Fil-søk</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Handlingsverktøy:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Funksjonsanrop</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Kodeinterpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Verktøy definert av OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agenttjenesten lar oss bruke disse verktøyene sammen som en `toolset`. Den bruker også `tråder` som holder oversikt over meldingshistorikken fra en bestemt samtale.

Tenk deg at du er en salgagent i et selskap kalt Contoso. Du ønsker å utvikle en samtaleagent som kan svare på spørsmål om salgsdataene dine.

Bildet under illustrerer hvordan du kan bruke Azure AI Agent Service for å analysere salgsdataene dine:

![Agentic Service In Action](../../../translated_images/no/agent-service-in-action.34fb465c9a84659e.webp)

For å bruke noen av disse verktøyene med tjenesten kan vi opprette en klient og definere et verktøy eller et verktøysett. For å implementere dette praktisk kan vi bruke følgende Python-kode. LLM vil kunne se på toolsettet og avgjøre om den skal bruke den brukerlagde funksjonen `fetch_sales_data_using_sqlite_query`, eller den forhåndsbygde kodeinterpreteren avhengig av brukerens forespørsel.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query-funksjon som kan finnes i en fil som heter fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initialiser verktøysett
toolset = ToolSet()

# Initialiser funksjonskallagent med fetch_sales_data_using_sqlite_query-funksjonen og legg den til verktøysettet
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Initialiser kodeinterpreterverktøy og legg det til verktøysettet.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Hvilke spesielle hensyn må tas for å bruke designmønsteret for verktøybruk til å bygge pålitelige AI-agenter?

En vanlig bekymring med SQL dynamisk generert av LLM-er er sikkerhet, spesielt risikoen for SQL-injeksjon eller skadelige handlinger, slik som å slette eller tukle med databasen. Selv om disse bekymringene er gyldige, kan de effektivt dempes ved riktig konfigurasjon av database-tilgangstillatelser. For de fleste databaser innebærer dette å konfigurere databasen som skrivebeskyttet (read-only). For databasetjenester som PostgreSQL eller Azure SQL bør appen få tildelt en lese- (SELECT) rolle.

Å kjøre appen i et sikkert miljø øker beskyttelsen ytterligere. I bedrifts-scenarier blir data vanligvis hentet ut og transformert fra operative systemer til en skrivebeskyttet database eller datalager med et brukervennlig skjema. Denne tilnærmingen sikrer at dataene er sikre, optimalisert for ytelse og tilgjengelighet, og at appen har begrenset, skrivebeskyttet tilgang.

## Eksempelkoder

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Har du flere spørsmål om designmønsteret for bruk av verktøy?

Bli med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for å møte andre lærende, delta på kontortimer og få svar på dine spørsmål om AI-agenter.

## Tilleggsressurser

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Workshop for Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Oversikt over Microsoft Agent Framework</a>

## Forrige leksjon

[Forstå agentiske designmønstre](../03-agentic-design-patterns/README.md)

## Neste leksjon
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->