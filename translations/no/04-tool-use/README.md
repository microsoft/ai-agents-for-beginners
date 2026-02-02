[![Hvordan designe gode AI-agenter](../../../translated_images/no/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klikk på bildet ovenfor for å se videoen av denne leksjonen)_

# Verktøybruk Designmønster

Verktøy er interessante fordi de lar AI-agenter ha et bredere spekter av ferdigheter. I stedet for at agenten har et begrenset sett med handlinger den kan utføre, kan agenten nå utføre et bredt spekter av handlinger ved å legge til et verktøy. I dette kapitlet skal vi se på Verktøybruk Designmønster, som beskriver hvordan AI-agenter kan bruke spesifikke verktøy for å oppnå sine mål.

## Introduksjon

I denne leksjonen ønsker vi å besvare følgende spørsmål:

- Hva er verktøybruk designmønster?
- Hvilke bruksområder kan det anvendes på?
- Hvilke elementer/byggeklosser trengs for å implementere designmønsteret?
- Hvilke spesielle hensyn må tas for å bruke Verktøybruk Designmønster for å bygge tillitsverdige AI-agenter?

## Læringsmål

Etter å ha fullført denne leksjonen vil du kunne:

- Definere Verktøybruk Designmønster og dets formål.
- Identifisere bruksområder hvor Verktøybruk Designmønster er anvendelig.
- Forstå nøkkel-elementene som trengs for å implementere designmønsteret.
- Gjenkjenne hensyn for å sikre tillit i AI-agenter som bruker dette designmønsteret.

## Hva er Verktøybruk Designmønster?

**Verktøybruk Designmønster** fokuserer på å gi LLM-er muligheten til å samhandle med eksterne verktøy for å oppnå spesifikke mål. Verktøy er kode som kan kjøres av en agent for å utføre handlinger. Et verktøy kan være en enkel funksjon som en kalkulator, eller et API-kall til en tredjepartstjeneste som aksjekursoppslag eller værmelding. I sammenheng med AI-agenter er verktøy designet for å bli utført av agenter som svar på **modell-genererte funksjonskall**.

## Hvilke bruksområder kan det anvendes på?

AI-agenter kan utnytte verktøy for å fullføre komplekse oppgaver, hente informasjon eller ta beslutninger. Verktøybruk designmønster brukes ofte i scenarier som krever dynamisk interaksjon med eksterne systemer, som databaser, webtjenester eller kodefortolkere. Denne evnen er nyttig for flere ulike bruksområder, inkludert:

- **Dynamisk informasjonsinnhenting:** Agenter kan forespørre eksterne APIer eller databaser for å hente oppdatert data (f.eks. forespørsler til en SQLite-database for dataanalyse, hente aksjekurser eller værinformasjon).
- **Kodekjøring og fortolkning:** Agenter kan kjøre kode eller skript for å løse matematiske problemer, generere rapporter eller utføre simuleringer.
- **Arbeidsflytautomatisering:** Automatisering av repeterende eller flertrinns arbeidsprosesser ved å integrere verktøy som oppgaveplanleggere, e-posttjenester eller datapipelines.
- **Kundesupport:** Agenter kan samhandle med CRM-systemer, billettplattform eller kunnskapsbaser for å løse brukerhenvendelser.
- **Innholdsgenerering og redigering:** Agenter kan bruke verktøy som grammatikkontroll, tekstoppsummering eller evaluering av innholdssikkerhet for å bistå i innholdsskaping.

## Hvilke elementer/byggeklosser trengs for å implementere verktøybruk designmønster?

Disse byggeklossene gjør det mulig for AI-agenten å utføre et bredt spekter av oppgaver. La oss se på de viktige elementene som trengs for å implementere Verktøybruk Designmønster:

- **Funksjon/Verktøy-skjemaer**: Detaljerte definisjoner av tilgjengelige verktøy, inkludert funksjonsnavn, formål, nødvendige parametre og forventede utdata. Disse skjemaene gjør det mulig for LLM å forstå hvilke verktøy som er tilgjengelige og hvordan man konstruerer gyldige forespørsler.

- **Funksjonsutførelseslogikk**: Styrer hvordan og når verktøy påkalles basert på brukerens intensjon og samtalekontekst. Dette kan inkludere planleggingsmoduler, rutemekanismer eller betingede flyter som bestemmer verktøybruk dynamisk.

- **Meldingshåndteringssystem**: Komponenter som håndterer samtaleflyten mellom brukerinnspill, LLM-svar, verktøysamtaler og verktøyutdata.

- **Verktøyintegrasjonsrammeverk**: Infrastruktur som kobler agenten til ulike verktøy, enten det er enkle funksjoner eller komplekse eksterne tjenester.

- **Feilhåndtering og validering**: Mekanismer for å håndtere feil i verktøyutførelse, validere parametre og håndtere uventede svar.

- **Tilstandsadministrasjon**: Sporer samtalekontekst, tidligere verktøysamhandlinger og vedvarende data for å sikre konsistens gjennom flertrinnsinteraksjoner.

Neste skal vi se nærmere på Funksjons-/Verktøypåcalling.

### Funksjons-/Verktøypåcalling

Funksjonspåcalling er hovedmåten vi gjør det mulig for store språkmodeller (LLM) å samhandle med verktøy. Du vil ofte se «Funksjon» og «Verktøy» brukt om hverandre fordi «funksjoner» (blokker av gjenbrukbar kode) er de «verktøyene» agentene bruker for å utføre oppgaver. For at koden i en funksjon skal kunne påkalles, må en LLM sammenligne brukerens forespørsel med funksjonens beskrivelse. For å gjøre dette sendes et skjema som inneholder beskrivelsene av alle tilgjengelige funksjoner til LLM. LLM velger så den mest passende funksjonen for oppgaven og returnerer funksjonsnavnet og argumentene. Den valgte funksjonen påkalles, svaret sendes tilbake til LLM, som bruker informasjonen for å svare på brukerens forespørsel.

For utviklere som skal implementere funksjonspåcalling for agenter trenger du:

1. En LLM-modell som støtter funksjonspåcalling
2. Et skjema som inneholder funksjonsbeskrivelser
3. Koden for hver funksjon som er beskrevet

La oss bruke eksempelet med å hente nåværende tid i en by for å illustrere:

1. **Initialiser en LLM som støtter funksjonspåcalling:**

    Ikke alle modeller støtter funksjonspåcalling, så det er viktig å sjekke at LLM-en du bruker gjør det. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> støtter funksjonspåcalling. Vi kan starte med å initiere Azure OpenAI-klienten. 

    ```python
    # Initialiser Azure OpenAI-klienten
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Opprett et funksjonsskjema**:

    Deretter definerer vi et JSON-skjema som inneholder funksjonsnavn, beskrivelse av hva funksjonen gjør, og navn og beskrivelser av funksjonsparametrene.
    Vi tar så dette skjemaet og sender det til klienten vi opprettet tidligere, sammen med brukerens forespørsel om å finne tiden i San Francisco. Det viktige å merke seg er at et **verktøypårop** returneres, **ikke** det endelige svaret på spørsmålet. Som nevnt tidligere, returnerer LLM navnet på funksjonen den valgte for oppgaven, og argumentene som skal sendes til den.

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
  
1. **Funksjonskoden som kreves for å utføre oppgaven:**

    Nå som LLM har valgt hvilken funksjon som må kjøres, må koden som utfører oppgaven implementeres og kjøres.
    Vi kan implementere koden for å hente nåværende tid i Python. Vi må også skrive kode for å hente ut navnet og argumentene fra response_message for å få det endelige resultatet.

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
  
      # Andre API-kall: Hent den endelige responsen fra modellen
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

Funksjonspåcalling er kjernen i de fleste, om ikke alle, agenters verktøybruk design, men å implementere det fra bunnen av kan noen ganger være utfordrende.
Som vi lærte i [Leksjon 2](../../../02-explore-agentic-frameworks) gir agentiske rammeverk oss ferdigbygde byggeklosser for å implementere verktøybruk.
 
## Verktøybruk Eksempler med Agentiske Rammeverk

Her er noen eksempler på hvordan du kan implementere Verktøybruk Designmønster ved hjelp av ulike agentiske rammeverk:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> er et åpen-kildekode AI-rammeverk for .NET, Python og Java-utviklere som jobber med store språkmodeller (LLM). Det forenkler prosessen med å bruke funksjonspåcalling ved automatisk å beskrive funksjonene dine og parametrene deres for modellen gjennom en prosess kalt <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serialisering</a>. Det håndterer også kommunikasjonen frem og tilbake mellom modellen og koden din. En annen fordel med å bruke et agentisk rammeverk som Semantic Kernel, er at det gir tilgang til ferdigbygde verktøy som <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">Fil-søk</a> og <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Kodefortolker</a>.

Følgende diagram illustrerer prosessen med funksjonspåcalling med Semantic Kernel:

![function calling](../../../translated_images/no/functioncalling-diagram.a84006fc287f6014.webp)

I Semantic Kernel kalles funksjoner/verktøy <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plug-ins</a>. Vi kan konvertere `get_current_time`-funksjonen vi så tidligere til en plug-in ved å gjøre den om til en klasse med funksjonen i seg. Vi kan også importere `kernel_function`-dekoratøren, som tar inn beskrivelsen av funksjonen. Når du oppretter en kernel med GetCurrentTimePlugin, vil kjernen automatisk serialisere funksjonen og parameterne, og lage skjemaet som sendes til LLM i prosessen.

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

# Opprett kjernen
kernel = Kernel()

# Opprett pluginen
get_current_time_plugin = GetCurrentTimePlugin(location)

# Legg pluginen til kjernen
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> er et nyere agentisk rammeverk designet for å gjøre det mulig for utviklere å sikkert bygge, distribuere og skalere høykvalitets og utvidbare AI-agenter uten å måtte håndtere underliggende databehandling og lagringsressurser. Det er særlig nyttig for bedriftsapplikasjoner siden det er en fullt administrert tjeneste med sikkerhet på bedriftsnivå.

Sammenlignet med å utvikle direkte med LLM-API, gir Azure AI Agent Service noen fordeler, inkludert:

- Automatisk verktøypåcalling – ingen behov for å analysere et verktøypårop, påkalle verktøyet og håndtere svaret; alt dette gjøres nå på serversiden
- Sikkert administrerte data – i stedet for å administrere egen samtaletilstand, kan du stole på threads for å lagre all informasjon du trenger
- Ferdige verktøy – verktøy du kan bruke for å samhandle med datakilder som Bing, Azure AI Search og Azure Functions.

Verktøyene som er tilgjengelige i Azure AI Agent Service kan deles inn i to kategorier:

1. Kunnskapsverktøy:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grunnlag med Bing-søk</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Fil-søk</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Handlingsverktøy:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Funksjonspåcalling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Kodefortolker</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI-definerte verktøy</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agenttjenesten gjør det mulig å bruke disse verktøyene sammen som et `toolset`. Den benytter også `threads` som holder orden på meldingshistorikk fra en spesifikk samtale.

Forestill deg at du er salgskonsulent i et selskap som heter Contoso. Du ønsker å utvikle en samtaleagent som kan svare på spørsmål om salgsdataene dine.

Følgende bilde illustrerer hvordan du kan bruke Azure AI Agent Service til å analysere salgsdataene dine:

![Agentic Service In Action](../../../translated_images/no/agent-service-in-action.34fb465c9a84659e.webp)

For å bruke noen av disse verktøyene med tjenesten kan vi opprette en klient og definere et verktøy eller verktøysett. For å implementere dette praktisk kan vi bruke følgende Python-kode. LLM vil kunne se på verktøysettet og avgjøre om den skal bruke den brukerlagde funksjonen `fetch_sales_data_using_sqlite_query` eller den forhåndsbygde kodefortolkeren avhengig av brukerens forespørsel.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query-funksjon som finnes i en fetch_sales_data_functions.py-fil.
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

# Initialiser Code Interpreter-verktøyet og legg det til i verktøysettet.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Hvilke spesielle hensyn må tas for å bruke Verktøybruk Designmønster for å bygge tillitsverdige AI-agenter?

En vanlig bekymring med SQL som genereres dynamisk av LLM-er er sikkerhet, spesielt risikoen for SQL-injeksjon eller ondsinnede handlinger, som å slette eller tukle med databasen. Selv om disse bekymringene er gyldige, kan de effektivt dempes ved riktig konfigurasjon av database-tilgangstillatelser. For de fleste databaser innebærer dette å konfigurere databasen som skrivebeskyttet. For databaser som PostgreSQL eller Azure SQL bør appen tildeles en lese- (SELECT) rolle.
Å kjøre appen i et sikkert miljø øker beskyttelsen ytterligere. I bedrifts-scenarier blir data typisk hentet ut og transformert fra operative systemer til en skrivebeskyttet database eller datalager med et brukervennlig skjema. Denne tilnærmingen sikrer at dataene er sikre, optimalisert for ytelse og tilgjengelighet, og at appen har begrenset, skrivebeskyttet tilgang.

## Sample Codes

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Got More Questions about the Tool Use Design Patterns?

Join the [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) to meet with other learners, attend office hours and get your AI Agents questions answered.

## Additional Resources

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Function Calling Tutorial</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## Previous Lesson

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## Next Lesson

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved bruk av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på sitt opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som følge av bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->