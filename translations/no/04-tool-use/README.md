[![Hvordan designe gode AI-agenter](../../../translated_images/no/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klikk på bildet over for å se videoen av denne leksjonen)_

# Designmønster for verktøybruk

Verktøy er interessante fordi de gir AI-agenter et bredere spekter av muligheter. I stedet for at agenten har et begrenset sett med handlinger den kan utføre, kan agenten nå utføre et bredt spekter av handlinger ved å legge til et verktøy. I dette kapitlet skal vi se på designmønsteret for verktøybruk, som beskriver hvordan AI-agenter kan bruke spesifikke verktøy for å oppnå sine mål.

## Introduksjon

I denne leksjonen ønsker vi å besvare følgende spørsmål:

- Hva er designmønsteret for verktøybruk?
- Hvilke brukstilfeller kan det anvendes på?
- Hva er elementene/byggeklossene som trengs for å implementere designmønsteret?
- Hva er spesielt å ta hensyn til når man bruker designmønsteret for verktøybruk for å bygge pålitelige AI-agenter?

## Læringsmål

Etter å ha fullført denne leksjonen vil du kunne:

- Definere designmønsteret for verktøybruk og dets hensikt.
- Identifisere brukstilfeller hvor designmønsteret for verktøybruk er anvendelig.
- Forstå de viktigste elementene som trengs for å implementere designmønsteret.
- Gjenkjenne hensyn for å sikre pålitelighet i AI-agenter som bruker dette designmønsteret.

## Hva er designmønsteret for verktøybruk?

**Designmønsteret for verktøybruk** fokuserer på å gi LLM-er muligheten til å samhandle med eksterne verktøy for å oppnå spesifikke mål. Verktøy er kode som kan kjøres av en agent for å utføre handlinger. Et verktøy kan være en enkel funksjon, som en kalkulator, eller et API-kall til en tredjepartstjeneste, som aksjekursoppslag eller værmelding. I konteksten av AI-agenter er verktøy designet for å bli utført av agenter som svar på **funksjonskall generert av modellen**.

## Hvilke brukstilfeller kan det anvendes på?

AI-agenter kan bruke verktøy for å fullføre komplekse oppgaver, hente informasjon eller ta beslutninger. Designmønsteret for verktøybruk brukes ofte i scenarier som krever dynamisk interaksjon med eksterne systemer, som databaser, webtjenester eller kodefortolkere. Denne evnen er nyttig for flere brukstilfeller, inkludert:

- **Dynamisk informasjonsinnhenting:** Agenter kan spørre eksterne API-er eller databaser for å hente oppdatert data (f.eks. spørre en SQLite-database for dataanalyse, hente aksjekurser eller værinformasjon).
- **Kodekjøring og fortolkning:** Agenter kan kjøre kode eller skript for å løse matematiske problemer, generere rapporter eller utføre simuleringer.
- **Automatisering av arbeidsflyt:** Automatisere repeterende eller flerstegs arbeidsflyter ved å integrere verktøy som oppgaveplanleggere, e-posttjenester eller datapipelines.
- **Kundesupport:** Agenter kan samhandle med CRM-systemer, supportsystemer eller kunnskapsbaser for å løse brukerhenvendelser.
- **Innholdsgenerering og redigering:** Agenter kan bruke verktøy som grammatikkontroll, tekstsummering eller innholdsikkerhetsevaluering til å assistere ved innholdsskaping.

## Hva er elementene/byggeklossene som trengs for å implementere designmønsteret for verktøybruk?

Disse byggeklossene gjør at AI-agenten kan utføre et bredt spekter av oppgaver. La oss se på hovedkomponentene som kreves for å implementere designmønsteret for verktøybruk:

- **Funksjons-/Verktøyskjemaer**: Detaljerte definisjoner av tilgjengelige verktøy, inkludert funksjonsnavn, formål, nødvendige parametere og forventede resultater. Disse skjemaene gjør at LLM kan forstå hvilke verktøy som er tilgjengelige og hvordan man konstruerer gyldige forespørsler.

- **Logikk for funksjonskjøring**: Styrer hvordan og når verktøy påkalles basert på brukerens intensjon og samtalekontekst. Dette kan inkludere planleggingsmoduler, rutemekanismer eller betingede flyter som bestemmer verktøybruk dynamisk.

- **Meldingshåndteringssystem**: Komponenter som styrer samtaleflyten mellom brukerinnspill, LLM-responser, verktøykall og verktøyutdata.

- **Integrasjonsrammeverk for verktøy**: Infrastruktur som kobler agenten til forskjellige verktøy, enten det er enkle funksjoner eller komplekse eksterne tjenester.

- **Feilhåndtering og validering**: Mekanismer for å håndtere feil ved utførelse av verktøy, validere parametere og håndtere uventede svar.

- **Tilstandsstyring**: Sporer samtalekontekst, tidligere verktøyinteraksjoner og vedvarende data for å sikre konsistens over flere samtalerunder.

Nå skal vi se nærmere på funksjons-/verktøykall.

### Funksjons-/Verktøykall

Funksjonskall er hovedmåten vi gjør det mulig for store språkmodeller (LLM) å samhandle med verktøy på. Du vil ofte se 'Funksjon' og 'Verktøy' brukt om hverandre fordi 'funksjoner' (blokker av gjenbrukbar kode) er 'verktøyene' som agenter bruker for å utføre oppgaver. For at en funksjonskode skal kunne påkalles må en LLM sammenligne brukerens forespørsel med funksjonens beskrivelse. For å gjøre dette sendes et skjema som inneholder beskrivelsene av alle tilgjengelige funksjoner til LLM. LLM velger så den mest passende funksjonen for oppgaven og returnerer navnet og argumentene. Den valgte funksjonen påkalles, svaret sendes tilbake til LLM, som bruker informasjonen for å svare på brukerens forespørsel.

For at utviklere skal implementere funksjonskall for agenter, trenger man:

1. En LLM-modell som støtter funksjonskall
2. Et skjema som inneholder funksjonsbeskrivelser
3. Koden for hver beskrevet funksjon

La oss bruke eksempelet på å hente nåværende tid i en by for å illustrere:

1. **Initialiser en LLM som støtter funksjonskall:**

    Ikke alle modeller støtter funksjonskall, så det er viktig å sjekke at LLM-en du bruker gjør det.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> støtter funksjonskall. Vi kan starte med å initiere Azure OpenAI-klienten.

    ```python
    # Initialiser Azure OpenAI-klienten
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Lag et funksjonsskjema**:

    Deretter definerer vi et JSON-skjema som inneholder funksjonsnavnet, beskrivelse av hva funksjonen gjør, og navn og beskrivelser av funksjonsparametere.
    Vi tar så dette skjemaet og sender det til klienten som ble opprettet tidligere, sammen med brukerens forespørsel om å finne tiden i San Francisco. Det viktige å merke seg er at et **verktøykall** er det som returneres, **ikke** det endelige svaret på spørsmålet. Som nevnt tidligere returnerer LLM navnet på funksjonen den valgte for oppgaven, og argumentene som skal sendes til den.

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
  
    # Første brukerbeskjed
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Første API-kall: Be modellen om å bruke funksjonen
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
  
1. **Funksjonskoden som kreves for å utføre oppgaven:**

    Nå som LLM har valgt hvilken funksjon som skal kjøres, må koden som utfører oppgaven implementeres og kjøres.
    Vi kan implementere koden for å hente nåværende tid i Python. Vi må også skrive kode for å ekstrahere navn og argumenter fra response_message for å få sluttresultatet.

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

Funksjonskall er kjernen i de fleste, om ikke alle, agentverktøybruk-design, men det kan noen ganger være utfordrende å implementere fra bunnen av.
Som vi lærte i [Leksjon 2](../../../02-explore-agentic-frameworks) gir agentiske rammeverk oss ferdige byggeklosser for å implementere verktøybruk.
 
## Eksempler på verktøybruk med agentiske rammeverk

Her er noen eksempler på hvordan du kan implementere designmønsteret for verktøybruk ved å bruke ulike agentiske rammeverk:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> er et åpen kildekode AI-rammeverk for å bygge AI-agenter. Det forenkler prosessen med å bruke funksjonskall ved å la deg definere verktøy som Python-funksjoner med `@tool`-dekoratøren. Rammeverket håndterer kommunikasjonen frem og tilbake mellom modellen og koden din. Det gir også tilgang til ferdigbygde verktøy som fil-søk og kodefortolker via `AzureAIProjectAgentProvider`.

Følgende diagram illustrerer prosessen med funksjonskall i Microsoft Agent Framework:

![function calling](../../../translated_images/no/functioncalling-diagram.a84006fc287f6014.webp)

I Microsoft Agent Framework defineres verktøy som dekorerte funksjoner. Vi kan gjøre om `get_current_time`-funksjonen fra tidligere til et verktøy ved å bruke `@tool`-dekoratøren. Rammeverket vil automatisk serialisere funksjonen og dens parametere, og lage skjemaet som sendes til LLM.

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

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> er et nyere agentisk rammeverk som er designet for å hjelpe utviklere med å sikkert bygge, distribuere og skalere AI-agenter av høy kvalitet og utvidbarhet uten å måtte administrere den underliggende beregnings- og lagringsinfrastrukturen. Det er spesielt nyttig for bedriftsapplikasjoner siden det er en fullt administrert tjeneste med bedriftsnivå sikkerhet.

Sammenlignet med utvikling direkte med LLM API, gir Azure AI Agent Service flere fordeler, inkludert:

- Automatisk verktøykalling – ingen behov for å tolke et verktøykall, påkalle verktøyet og håndtere responsen; alt dette skjer nå på serversiden
- Sikkert administrerte data – i stedet for å håndtere egen samtalestatus, kan du stole på tråder for å lagre all nødvendig informasjon
- Ferdige verktøy – verktøy som kan brukes til å samhandle med datakilder, slik som Bing, Azure AI Search og Azure Functions.

Verktøyene tilgjengelig i Azure AI Agent Service kan deles inn i to kategorier:

1. Kunnskapsverktøy:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grunnlag med Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Fil-søk</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Handlingsverktøy:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Funksjonskall</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Kodefortolker</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI-definerte verktøy</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agenttjenesten gjør det mulig å bruke disse verktøyene sammen som en `toolset`. Den bruker også `threads` som holder orden på meldingshistorikken for en bestemt samtale.

Tenk deg at du er en salgsagent i et selskap kalt Contoso. Du ønsker å utvikle en samtaleagent som kan svare på spørsmål om salgsdataene dine.

Følgende bilde illustrerer hvordan du kunne bruke Azure AI Agent Service til å analysere dine salgsdata:

![Agentic Service In Action](../../../translated_images/no/agent-service-in-action.34fb465c9a84659e.webp)

For å bruke noen av disse verktøyene med tjenesten kan vi opprette en klient og definere et verktøy eller en toolset. For å implementere dette praktisk kan vi bruke følgende Python-kode. LLM vil kunne se på toolset og avgjøre om den skal bruke brukerdefinert funksjon, `fetch_sales_data_using_sqlite_query`, eller den forhåndsbygde Kodefortolkeren avhengig av brukerens forespørsel.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query-funksjon som finnes i en fil kalt fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initialiser verktøysett
toolset = ToolSet()

# Initialiser funksjonskallagent med fetch_sales_data_using_sqlite_query-funksjonen og legg den til i verktøysettet
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Initialiser Kode Interpreter-verktøyet og legg det til i verktøysettet.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Hva er spesielle hensyn ved bruk av designmønsteret for verktøybruk for å bygge pålitelige AI-agenter?

En vanlig bekymring med SQL som dynamisk genereres av LLM-er er sikkerhet, spesielt risikoen for SQL-injeksjon eller ondsinnede handlinger, som å slette eller tukle med databasen. Selv om disse bekymringene er gyldige, kan de effektivt avbøtes ved riktig konfigurasjon av databasetilgangstillatelser. For de fleste databaser innebærer dette å konfigurere databasen som skrivebeskyttet. For database-tjenester som PostgreSQL eller Azure SQL bør appen tildeles en lese- og velgesrolle (SELECT).

Å kjøre appen i et sikkert miljø gir ytterligere beskyttelse. I bedrifts-scenarier ekstraheres og transformeres data vanligvis fra operasjonelle systemer til en skrivebeskyttet database eller datavarehus med et brukervennlig skjema. Denne tilnærmingen sikrer at dataene er sikre, optimalisert for ytelse og tilgjengelighet, og at appen har begrenset, skrivebeskyttet tilgang.

## Eksempelkoder

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Har du flere spørsmål om designmønsteret for verktøybruk?

Bli med i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) for å møte andre lærende, delta på Q&A-timer og få svar på dine AI Agents-spørsmål.

## Tilleggsressurser

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Oversikt over Microsoft Agent Framework</a>

## Forrige leksjon

[Forstå agentiske designmønstre](../03-agentic-design-patterns/README.md)

## Neste leksjon
[Agentisk RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->