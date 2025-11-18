<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7c3b7bd1b3528074d8b6a7c5ad33b6f",
  "translation_date": "2025-11-18T17:43:10+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "no"
}
-->
[![Hvordan designe gode AI-agenter](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.no.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klikk på bildet ovenfor for å se videoen til denne leksjonen)_

# Designmønster for verktøybruk

Verktøy er interessante fordi de gir AI-agenter muligheten til å ha et bredere spekter av ferdigheter. I stedet for at agenten har et begrenset sett med handlinger den kan utføre, kan den nå utføre et bredt spekter av handlinger ved å legge til et verktøy. I dette kapittelet skal vi se på designmønsteret for verktøybruk, som beskriver hvordan AI-agenter kan bruke spesifikke verktøy for å oppnå sine mål.

## Introduksjon

I denne leksjonen skal vi besvare følgende spørsmål:

- Hva er designmønsteret for verktøybruk?
- Hvilke bruksområder kan det anvendes på?
- Hvilke elementer/byggesteiner trengs for å implementere designmønsteret?
- Hvilke spesielle hensyn må tas for å bruke designmønsteret for verktøybruk til å bygge pålitelige AI-agenter?

## Læringsmål

Etter å ha fullført denne leksjonen, vil du kunne:

- Definere designmønsteret for verktøybruk og dets formål.
- Identifisere bruksområder der designmønsteret for verktøybruk er relevant.
- Forstå de viktigste elementene som trengs for å implementere designmønsteret.
- Gjenkjenne hensyn for å sikre pålitelighet i AI-agenter som bruker dette designmønsteret.

## Hva er designmønsteret for verktøybruk?

**Designmønsteret for verktøybruk** fokuserer på å gi LLM-er muligheten til å samhandle med eksterne verktøy for å oppnå spesifikke mål. Verktøy er kode som kan utføres av en agent for å utføre handlinger. Et verktøy kan være en enkel funksjon, som en kalkulator, eller et API-kall til en tredjepartstjeneste, som aksjekursoppslag eller værmelding. I sammenheng med AI-agenter er verktøy designet for å bli utført av agenter som svar på **modellgenererte funksjonskall**.

## Hvilke bruksområder kan det anvendes på?

AI-agenter kan bruke verktøy for å fullføre komplekse oppgaver, hente informasjon eller ta beslutninger. Designmønsteret for verktøybruk brukes ofte i scenarier som krever dynamisk interaksjon med eksterne systemer, som databaser, webtjenester eller kodefortolkere. Denne evnen er nyttig for en rekke bruksområder, inkludert:

- **Dynamisk informasjonsinnhenting:** Agenter kan hente oppdatert data fra eksterne API-er eller databaser (f.eks. spørring mot en SQLite-database for dataanalyse, henting av aksjekurser eller værinformasjon).
- **Kodeutførelse og fortolkning:** Agenter kan utføre kode eller skript for å løse matematiske problemer, generere rapporter eller utføre simuleringer.
- **Automatisering av arbeidsflyt:** Automatisering av repeterende eller flertrinns arbeidsflyter ved å integrere verktøy som oppgaveplanleggere, e-posttjenester eller datapipelines.
- **Kundesupport:** Agenter kan samhandle med CRM-systemer, ticketing-plattformer eller kunnskapsbaser for å løse brukerforespørsler.
- **Innholdsproduksjon og redigering:** Agenter kan bruke verktøy som grammatikkontroll, tekstsammendrag eller innholdssikkerhetsvurderinger for å bistå med innholdsproduksjon.

## Hvilke elementer/byggesteiner trengs for å implementere designmønsteret for verktøybruk?

Disse byggesteinene gjør det mulig for AI-agenten å utføre et bredt spekter av oppgaver. La oss se på de viktigste elementene som trengs for å implementere designmønsteret for verktøybruk:

- **Funksjons-/verktøyskjemaer**: Detaljerte definisjoner av tilgjengelige verktøy, inkludert funksjonsnavn, formål, nødvendige parametere og forventede utdata. Disse skjemaene gjør det mulig for LLM-en å forstå hvilke verktøy som er tilgjengelige og hvordan man konstruerer gyldige forespørsler.

- **Logikk for funksjonsutførelse**: Styrer hvordan og når verktøy aktiveres basert på brukerens intensjon og samtalekontekst. Dette kan inkludere planleggingsmoduler, rutemekanismer eller betingede flyter som dynamisk bestemmer verktøybruk.

- **System for meldinghåndtering**: Komponenter som administrerer samtaleflyten mellom brukerinnspill, LLM-responser, verktøykall og verktøyutdata.

- **Integrasjonsrammeverk for verktøy**: Infrastruktur som kobler agenten til ulike verktøy, enten de er enkle funksjoner eller komplekse eksterne tjenester.

- **Feilhåndtering og validering**: Mekanismer for å håndtere feil i verktøyutførelse, validere parametere og administrere uventede responser.

- **Tilstandshåndtering**: Sporer samtalekontekst, tidligere verktøyinteraksjoner og vedvarende data for å sikre konsistens på tvers av flertrinnsinteraksjoner.

La oss nå se nærmere på funksjons-/verktøykall.

### Funksjons-/verktøykall

Funksjonskall er den primære måten vi gjør det mulig for store språkmodeller (LLM-er) å samhandle med verktøy. Du vil ofte se 'Funksjon' og 'Verktøy' brukt om hverandre fordi 'funksjoner' (blokker med gjenbrukbar kode) er 'verktøyene' agenter bruker for å utføre oppgaver. For at en funksjonskode skal kunne utføres, må en LLM sammenligne brukerens forespørsel med funksjonsbeskrivelsen. For å gjøre dette sendes et skjema som inneholder beskrivelsene av alle tilgjengelige funksjoner til LLM-en. LLM-en velger deretter den mest passende funksjonen for oppgaven og returnerer dens navn og argumenter. Den valgte funksjonen utføres, og responsen sendes tilbake til LLM-en, som bruker informasjonen til å svare på brukerens forespørsel.

For utviklere som ønsker å implementere funksjonskall for agenter, trenger du:

1. En LLM-modell som støtter funksjonskall
2. Et skjema som inneholder funksjonsbeskrivelser
3. Koden for hver funksjon som er beskrevet

La oss bruke eksempelet med å finne gjeldende tid i en by for å illustrere:

1. **Initialiser en LLM som støtter funksjonskall:**

    Ikke alle modeller støtter funksjonskall, så det er viktig å sjekke at LLM-en du bruker gjør det. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> støtter funksjonskall. Vi kan starte med å initiere Azure OpenAI-klienten.

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Opprett et funksjonsskjema:**

    Deretter definerer vi et JSON-skjema som inneholder funksjonsnavnet, beskrivelsen av hva funksjonen gjør, og navnene og beskrivelsene av funksjonsparametrene. Vi tar deretter dette skjemaet og sender det til klienten som ble opprettet tidligere, sammen med brukerens forespørsel om å finne tiden i San Francisco. Det som er viktig å merke seg er at et **verktøykall** er det som returneres, **ikke** det endelige svaret på spørsmålet. Som nevnt tidligere, returnerer LLM-en navnet på funksjonen den valgte for oppgaven, og argumentene som vil bli sendt til den.

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
  
1. **Koden for funksjonen som kreves for å utføre oppgaven:**

    Nå som LLM-en har valgt hvilken funksjon som må kjøres, må koden som utfører oppgaven implementeres og utføres. Vi kan implementere koden for å finne gjeldende tid i Python. Vi må også skrive koden for å hente navnet og argumentene fra response_message for å få det endelige resultatet.

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

Funksjonskall er kjernen i de fleste, om ikke alle, agentverktøydesign, men å implementere det fra bunnen av kan noen ganger være utfordrende. Som vi lærte i [Leksjon 2](../../../02-explore-agentic-frameworks) gir agentiske rammeverk oss forhåndsbygde byggesteiner for å implementere verktøybruk.

## Eksempler på verktøybruk med agentiske rammeverk

Her er noen eksempler på hvordan du kan implementere designmønsteret for verktøybruk ved hjelp av ulike agentiske rammeverk:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> er et åpen kildekode AI-rammeverk for .NET-, Python- og Java-utviklere som jobber med store språkmodeller (LLM-er). Det forenkler prosessen med å bruke funksjonskall ved automatisk å beskrive funksjonene dine og deres parametere til modellen gjennom en prosess kalt <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serialisering</a>. Det håndterer også kommunikasjonen mellom modellen og koden din. En annen fordel med å bruke et agentisk rammeverk som Semantic Kernel er at det gir tilgang til forhåndsbygde verktøy som <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">Fil-søk</a> og <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Kodefortolker</a>.

Følgende diagram illustrerer prosessen med funksjonskall med Semantic Kernel:

![funksjonskall](../../../translated_images/functioncalling-diagram.a84006fc287f60140cc0a484ff399acd25f69553ea05186981ac4d5155f9c2f6.no.png)

I Semantic Kernel kalles funksjoner/verktøy <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugins</a>. Vi kan konvertere `get_current_time`-funksjonen vi så tidligere til en plugin ved å gjøre den om til en klasse med funksjonen i den. Vi kan også importere `kernel_function`-dekoratoren, som tar inn beskrivelsen av funksjonen. Når du deretter oppretter en kernel med GetCurrentTimePlugin, vil kernel automatisk serialisere funksjonen og dens parametere, og opprette skjemaet som sendes til LLM-en i prosessen.

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

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> er et nyere agentisk rammeverk som er designet for å gi utviklere muligheten til å bygge, distribuere og skalere høykvalitets og utvidbare AI-agenter på en sikker måte, uten å måtte administrere de underliggende ressursene for beregning og lagring. Det er spesielt nyttig for bedriftsapplikasjoner siden det er en fullt administrert tjeneste med sikkerhet på bedriftsnivå.

Sammenlignet med å utvikle direkte med LLM-API-en, gir Azure AI Agent Service noen fordeler, inkludert:

- Automatisk verktøykall – ingen behov for å analysere et verktøykall, utføre verktøyet og håndtere responsen; alt dette gjøres nå på serversiden
- Sikkert administrert data – i stedet for å administrere din egen samtaletilstand, kan du stole på tråder for å lagre all informasjonen du trenger
- Ferdigbygde verktøy – Verktøy som du kan bruke til å samhandle med datakildene dine, som Bing, Azure AI Search og Azure Functions.

Verktøyene som er tilgjengelige i Azure AI Agent Service kan deles inn i to kategorier:

1. Kunnskapsverktøy:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grunnlegging med Bing-søk</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Fil-søk</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Handlingsverktøy:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Funksjonskall</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Kodefortolker</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI-definerte verktøy</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service lar oss bruke disse verktøyene sammen som et `toolset`. Det benytter også `threads` som holder oversikt over historikken til meldinger fra en bestemt samtale.

Tenk deg at du er en salgsagent i et selskap som heter Contoso. Du ønsker å utvikle en samtaleagent som kan svare på spørsmål om salgsdataene dine.

Følgende bilde illustrerer hvordan du kan bruke Azure AI Agent Service til å analysere salgsdataene dine:

![Agentisk tjeneste i aksjon](../../../translated_images/agent-service-in-action.34fb465c9a84659edd3003f8cb62d6b366b310a09b37c44e32535021fbb5c93f.no.jpg)

For å bruke noen av disse verktøyene med tjenesten kan vi opprette en klient og definere et verktøy eller verktøysett. For å implementere dette praktisk kan vi bruke følgende Python-kode. LLM-en vil kunne se på verktøysettet og avgjøre om den skal bruke den brukerskapte funksjonen, `fetch_sales_data_using_sqlite_query`, eller den forhåndsbygde kodefortolkeren, avhengig av brukerens forespørsel.

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

## Hvilke spesielle hensyn må tas for å bruke designmønsteret for verktøybruk til å bygge pålitelige AI-agenter?

En vanlig bekymring med SQL dynamisk generert av LLM-er er sikkerhet, spesielt risikoen for SQL-injeksjon eller skadelige handlinger, som å slette eller manipulere databasen. Selv om disse bekymringene er gyldige, kan de effektivt reduseres ved å konfigurere databaseadgangstillatelser riktig. For de fleste databaser innebærer dette å konfigurere databasen som skrivebeskyttet. For databasesystemer som PostgreSQL eller Azure SQL, bør appen tildeles en skrivebeskyttet (SELECT) rolle.
Å kjøre appen i et sikkert miljø forbedrer beskyttelsen ytterligere. I bedriftsmiljøer blir data vanligvis hentet ut og transformert fra operasjonelle systemer til en skrivebeskyttet database eller et datavarehus med et brukervennlig skjema. Denne tilnærmingen sikrer at dataene er sikre, optimalisert for ytelse og tilgjengelighet, og at appen har begrenset, skrivebeskyttet tilgang.

## Eksempelkoder

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Har du flere spørsmål om designmønstre for verktøybruk?

Bli med i [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) for å møte andre lærende, delta på kontortid og få svar på spørsmålene dine om AI-agenter.

## Tilleggsressurser

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Function Calling Tutorial</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## Forrige leksjon

[Forstå agentiske designmønstre](../03-agentic-design-patterns/README.md)

## Neste leksjon

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->