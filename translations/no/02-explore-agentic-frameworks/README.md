[![Utforske AI Agent-rammeverk](../../../translated_images/no/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Klikk på bildet over for å se video av denne leksjonen)_

# Utforske AI Agent-rammeverk

AI agent-rammeverk er programvareplattformer designet for å forenkle oppretting, distribusjon og administrasjon av AI-agenter. Disse rammeverkene gir utviklere forhåndsbygde komponenter, abstraksjoner og verktøy som effektiviserer utviklingen av komplekse AI-systemer.

Disse rammeverkene hjelper utviklere med å fokusere på de unike aspektene ved sine applikasjoner ved å tilby standardiserte tilnærminger til vanlige utfordringer i utvikling av AI-agenter. De øker skalerbarhet, tilgjengelighet og effektivitet i byggingen av AI-systemer.

## Introduksjon 

Denne leksjonen vil dekke:

- Hva er AI Agent-rammeverk og hva kan utviklere oppnå med dem?
- Hvordan kan team bruke disse til å raskt prototype, iterere og forbedre agentens kapasiteter?
- Hva er forskjellene mellom rammeverkene og verktøyene laget av Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> og <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Kan jeg integrere mine eksisterende Azure-økosystemverktøy direkte, eller trenger jeg frittstående løsninger?
- Hva er Microsoft Foundry Agent Service, og hvordan hjelper dette meg?

## Læringsmål

Målet med denne leksjonen er å hjelpe deg å forstå:

- Rollen til AI Agent-rammeverk i AI-utvikling.
- Hvordan utnytte AI Agent-rammeverk til å bygge intelligente agenter.
- Nøkkelfunksjoner muliggjort av AI Agent-rammeverk.
- Forskjellene mellom Microsoft Agent Framework og Microsoft Foundry Agent Service.

## Hva er AI Agent-rammeverk og hva muliggjør de for utviklere?

Tradisjonelle AI-rammeverk kan hjelpe deg med å integrere AI i appene dine og gjøre disse appene bedre på følgende måter:

- **Personalisering**: AI kan analysere brukerens atferd og preferanser for å gi personlige anbefalinger, innhold og opplevelser.
Eksempel: Strømmetjenester som Netflix bruker AI til å foreslå filmer og serier basert på seerhistorikk, noe som øker brukerengasjement og tilfredshet.
- **Automatisering og effektivitet**: AI kan automatisere repeterende oppgaver, strømlinjeforme arbeidsflyter og forbedre operasjonell effektivitet.
Eksempel: Kundeserviceapper bruker AI-drevne chatboter til å håndtere vanlige henvendelser, redusere responstider og frigjøre menneskelige agenter til mer komplekse saker.
- **Forbedret brukeropplevelse**: AI kan forbedre den totale brukeropplevelsen ved å tilby intelligente funksjoner som talegjenkjenning, naturlig språkbehandling og prediktiv tekst.
Eksempel: Virtuelle assistenter som Siri og Google Assistant bruker AI til å forstå og svare på talekommandoer, noe som gjør det enklere for brukere å samhandle med sine enheter.

### Det høres jo flott ut, men hvorfor trenger vi AI Agent-rammeverket?

AI Agent-rammeverk representerer mer enn bare AI-rammeverk. De er designet for å muliggjøre opprettelse av intelligente agenter som kan samhandle med brukere, andre agenter og miljøet for å oppnå spesifikke mål. Disse agentene kan vise autonom oppførsel, ta beslutninger og tilpasse seg endrede forhold. La oss se på noen nøkkelfunksjoner muliggjort av AI Agent-rammeverk:

- **Agent-samarbeid og koordinering**: Muliggjør opprettelse av flere AI-agenter som kan jobbe sammen, kommunisere og koordinere for å løse komplekse oppgaver.
- **Oppgaveautomatisering og styring**: Tilbyr mekanismer for automatisering av flertrinns arbeidsflyter, oppgavedelegering og dynamisk oppgavestyring mellom agenter.
- **Kontekstuell forståelse og tilpasning**: Utstyrer agenter med evnen til å forstå kontekst, tilpasse seg endrende omgivelser og ta beslutninger basert på sanntidsinformasjon.

Så, oppsummert, lar agenter deg gjøre mer, ta automatisering til neste nivå, og skape mer intelligente systemer som kan tilpasse seg og lære av sitt miljø.

## Hvordan prototype raskt, iterere og forbedre agentens kapasiteter?

Dette er et raskt bevegelig landskap, men det finnes noen felles elementer i de fleste AI Agent-rammeverk som kan hjelpe deg med å prototype og iterere raskt, nemlig modulære komponenter, samarbeidende verktøy og sanntidslæring. La oss gå gjennom disse:

- **Bruk modulære komponenter**: AI SDK-er tilbyr forhåndsbygde komponenter som AI- og minnekonnektorer, funksjonskalling med naturlig språk eller kode-plugins, promptmaler og mer.
- **Utnytt samarbeidsverktøy**: Design agenter med spesifikke roller og oppgaver, slik at de kan teste og forbedre samarbeidende arbeidsflyter.
- **Lær i sanntid**: Implementer tilbakemeldingssløyfer der agenter lærer av interaksjoner og justerer sin oppførsel dynamisk.

### Bruk modulære komponenter

SDK-er som Microsoft Agent Framework tilbyr forhåndsbygde komponenter som AI-konnektorer, verktøysdefinisjoner og agentadministrasjon.

**Hvordan team kan bruke disse**: Team kan raskt sette sammen disse komponentene for å lage en funksjonell prototype uten å starte fra bunnen, noe som muliggjør rask eksperimentering og iterasjon.

**Hvordan det fungerer i praksis**: Du kan bruke en forhåndsbygget parser for å hente ut informasjon fra brukerinput, en minnemodul for å lagre og hente data, og en promptgenerator for å interagere med brukere, alt uten å måtte bygge disse komponentene fra bunnen.

**Eksempelkode**. La oss se på et eksempel på hvordan du kan bruke Microsoft Agent Framework med `FoundryChatClient` for å få modellen til å svare på brukerinput med verktøyskalling:

``` python
# Microsoft Agent Framework Python-eksempel

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Definer en eksempelverktøyfunksjon for å bestille reise
@tool(approval_mode="never_require")
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # Eksempelutgang: Din flyreise til New York den 1. januar 2025 er vellykket bestilt. God tur! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Det du kan se i dette eksempelet er hvordan du kan utnytte en forhåndsbygget parser for å hente ut nøkkelinformasjon fra brukerinput, som opprinnelse, destinasjon og dato for en flybestilling. Denne modulære tilnærmingen lar deg fokusere på den overordnede logikken.

### Utnytt samarbeidsverktøy

Rammeverk som Microsoft Agent Framework legger til rette for å lage flere agenter som kan jobbe sammen.

**Hvordan team kan bruke disse**: Team kan designe agenter med bestemte roller og oppgaver, slik at de kan teste og forbedre samarbeidende arbeidsflyter og øke den samlede systemeffektiviteten.

**Hvordan det fungerer i praksis**: Du kan lage et team av agenter hvor hver agent har en spesialisert funksjon, som datainnhenting, analyse eller beslutningstaking. Disse agentene kan kommunisere og dele informasjon for å oppnå et felles mål, som å svare på en brukerhenvendelse eller fullføre en oppgave.

**Eksempelkode (Microsoft Agent Framework)**:

```python
# Oppretter flere agenter som samarbeider ved bruk av Microsoft Agent Framework

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Datauttrekksagent
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Dataanalyseagent
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Kjør agenter sekvensielt på en oppgave
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Det du ser i koden over, er hvordan du kan lage en oppgave som involverer flere agenter som jobber sammen for å analysere data. Hver agent utfører en bestemt funksjon, og oppgaven utføres ved å koordinere agentene for å oppnå ønsket resultat. Ved å lage dedikerte agenter med spesialiserte roller kan du forbedre oppgaveeffektiviteten og ytelsen.

### Lær i sanntid

Avanserte rammeverk tilbyr funksjoner for sanntids kontekstforståelse og tilpasning.

**Hvordan team kan bruke disse**: Team kan implementere tilbakemeldingssløyfer der agenter lærer fra interaksjoner og justerer sin oppførsel dynamisk, noe som fører til kontinuerlig forbedring og finjustering av kapasiteter.

**Hvordan det fungerer i praksis**: Agenter kan analysere brukertilbakemeldinger, miljødata og oppgaveutfall for å oppdatere sin kunnskapsbase, justere beslutningsalgoritmer og forbedre ytelsen over tid. Denne iterative læringsprosessen gjør at agenter kan tilpasse seg endrede forhold og brukerpreferanser, noe som øker systemets totale effektivitet.

## Hva er forskjellene mellom Microsoft Agent Framework og Microsoft Foundry Agent Service?

Det finnes mange måter å sammenligne disse tilnærmingene på, men la oss se på noen nøkkelforskjeller med hensyn til design, kapasiteter og målrettede bruksområder:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework tilbyr en strømlinjeformet SDK for å bygge AI-agenter ved bruk av `FoundryChatClient`. Det gjør det mulig for utviklere å lage agenter som benytter Azure OpenAI-modeller med innebygd verktøyskalling, samtalehåndtering og sikkerhet av bedriftsklasse gjennom Azure-identitet.

**Bruksområder**: Bygging av produksjonsklare AI-agenter med verktøysbruk, flertrinns arbeidsflyter og integrasjonsscenarier for bedrifter.

Her er noen viktige kjernebegreper i Microsoft Agent Framework:

- **Agenter**. En agent opprettes via `FoundryChatClient` og konfigureres med navn, instruksjoner og verktøy. Agenten kan:
  - **Behandle brukermeldinger** og generere svar ved hjelp av Azure OpenAI-modeller.
  - **Kalle verktøy** automatisk basert på samtalekontekst.
  - **Opprettholde samtalestatus** over flere interaksjoner.

  Her er et kodeeksempel som viser hvordan man oppretter en agent:

    ```python
    import os
    from agent_framework.foundry import FoundryChatClient
    from azure.identity import AzureCliCredential

    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **Verktøy**. Rammeverket støtter definisjon av verktøy som Python-funksjoner som agenten kan kalle automatisk. Verktøy registreres når agenten opprettes:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = provider.as_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **Multi-agent-koordinering**. Du kan opprette flere agenter med ulike spesialiseringer og koordinere deres arbeid:

    ```python
    planner = provider.as_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = provider.as_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Azure Identity-integrasjon**. Rammeverket bruker `AzureCliCredential` (eller `DefaultAzureCredential`) for sikker, nøkkelfri autentisering, noe som eliminerer behovet for å administrere API-nøkler direkte.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service er et nyere tillegg, introdusert på Microsoft Ignite 2024. Det gjør det mulig å utvikle og distribuere AI-agenter med mer fleksible modeller, som direkte kaller open-source LLM-er som Llama 3, Mistral og Cohere.

Microsoft Foundry Agent Service tilbyr sterkere sikkerhetsmekanismer for bedrifter og datalagringsmetoder, noe som gjør det egnet til bedriftsapplikasjoner. 

Det fungerer sømløst sammen med Microsoft Agent Framework for å bygge og distribuere agenter.

Denne tjenesten er for tiden i offentlig forhåndsvisning og støtter Python og C# for agentbygging.

Ved å bruke Microsoft Foundry Agent Service Python SDK kan vi opprette en agent med et brukertilpasset verktøy:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Definer verktøyfunksjoner
def get_specials() -> str:
    """Provides a list of specials from the menu."""
    return """
    Special Soup: Clam Chowder
    Special Salad: Cobb Salad
    Special Drink: Chai Tea
    """

def get_item_price(menu_item: str) -> str:
    """Provides the price of the requested menu item."""
    return "$9.99"


async def main() -> None:
    credential = DefaultAzureCredential()
    project_client = AIProjectClient.from_connection_string(
        credential=credential,
        conn_str="your-connection-string",
    )

    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="Host",
        instructions="Answer questions about the menu.",
        tools=[get_specials, get_item_price],
    )

    thread = project_client.agents.create_thread()

    user_inputs = [
        "Hello",
        "What is the special soup?",
        "How much does that cost?",
        "Thank you",
    ]

    for user_input in user_inputs:
        print(f"# User: '{user_input}'")
        message = project_client.agents.create_message(
            thread_id=thread.id,
            role="user",
            content=user_input,
        )
        run = project_client.agents.create_and_process_run(
            thread_id=thread.id, agent_id=agent.id
        )
        messages = project_client.agents.list_messages(thread_id=thread.id)
        print(f"# Agent: {messages.data[0].content[0].text.value}")


if __name__ == "__main__":
    asyncio.run(main())
```

### Kjerneteknologier

Microsoft Foundry Agent Service har følgende kjernebegreper:

- **Agent**. Microsoft Foundry Agent Service integreres med Microsoft Foundry. Innen Microsoft Foundry fungerer en AI Agent som en "smart" mikrotjeneste som kan brukes til å svare på spørsmål (RAG), utføre handlinger eller fullstendig automatisere arbeidsflyter. Dette oppnås ved å kombinere kraften til generative AI-modeller med verktøy som gjør det mulig å få tilgang til og samhandle med virkelige datakilder. Her er et eksempel på en agent:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    I dette eksempelet opprettes en agent med modellen `gpt-4o-mini`, navnet `my-agent` og instruksjonene `You are helpful agent`. Agenten er utstyrt med verktøy og ressurser for å utføre kode-interpretasjonsoppgaver.

- **Tråd og meldinger**. Tråden er et annet viktig begrep. Den representerer en samtale eller interaksjon mellom en agent og en bruker. Tråder kan brukes til å følge samtalens fremdrift, lagre kontekstinformasjon og administrere tilstanden til interaksjonen. Her er et eksempel på en tråd:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Be agenten utføre arbeid på tråden
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Hent og logg alle meldinger for å se agentens respons
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    I forrige kode opprettes en tråd. Deretter sendes en melding til tråden. Ved å kalle `create_and_process_run` blir agenten bedt om å utføre arbeid på tråden. Til slutt hentes og logges meldingene for å se agentens svar. Meldingene viser samtalens fremdrift mellom bruker og agent. Det er også viktig å forstå at meldingene kan ha forskjellige typer, som tekst, bilde eller fil, altså at agentens arbeid har resultert i for eksempel et bilde eller en tekstrespons. Som utvikler kan du bruke denne informasjonen til videre behandling av responsen eller presentasjon for brukeren.

- **Integrasjon med Microsoft Agent Framework**. Microsoft Foundry Agent Service fungerer sømløst med Microsoft Agent Framework, som betyr at du kan bygge agenter med `FoundryChatClient` og distribuere dem via Agent Service for produksjonsscenarier.

**Bruksområder**: Microsoft Foundry Agent Service er designet for bedriftsapplikasjoner som krever sikker, skalerbar og fleksibel AI-agentdistribusjon.

## Hva er forskjellen på disse tilnærmingene?
 
Det kan høres ut som det er overlapp, men det finnes noen nøkkelforskjeller når det gjelder design, kapasiteter og målrettede bruksområder:
 
- **Microsoft Agent Framework (MAF)**: Er en produksjonsklar SDK for bygging av AI-agenter. Den tilbyr en strømlinjeformet API for å lage agenter med verktøyskalling, samtalehåndtering og Azure-identitetsintegrasjon.
- **Microsoft Foundry Agent Service**: Er en plattform- og distribusjonstjeneste i Microsoft Foundry for agenter. Den tilbyr innebygd tilkobling til tjenester som Azure OpenAI, Azure AI Search, Bing Search og kode-eksekvering.
 
Er du fortsatt usikker på hva du skal velge?

### Bruksområder
 
La oss se om vi kan hjelpe deg ved å gå gjennom noen vanlige brukstilfeller:
 
> Q: Jeg bygger produksjonsklare AI-agentapplikasjoner og vil komme i gang raskt
>

> A: Microsoft Agent Framework er et godt valg. Det tilbyr en enkel, Python-inspirert API via `FoundryChatClient` som lar deg definere agenter med verktøy og instruksjoner i bare noen få kodelinjer.

> Q: Jeg trenger distribusjon av bedriftsklasse med Azure-integrasjoner som Search og kodeeksekvering
>
> A: Microsoft Foundry Agent Service er det beste valget. Det er en plattformtjeneste som tilbyr innebygde funksjoner for flere modeller, Azure AI Search, Bing Search og Azure Functions. Det gjør det enkelt å bygge agentene dine i Foundry Portal og distribuere dem i stor skala.
 
> Q: Jeg er fortsatt usikker, gi meg bare ett alternativ
>
> A: Start med Microsoft Agent Framework for å bygge agentene dine, og bruk deretter Microsoft Foundry Agent Service når du trenger å distribuere og skalere dem i produksjon. Denne tilnærmingen lar deg iterere raskt på agentlogikken mens du har en klar vei til bedriftsdistribusjon.
 
La oss oppsummere nøkkelforskjellene i en tabell:

| Rammeverk | Fokus | Kjerneteknologier | Bruksområder |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Strømlinjeformet agent-SDK med verktøyskalling | Agenter, Verktøy, Azure Identity | Bygging av AI-agenter, verktøybruk, flertrinns arbeidsflyter |
| Microsoft Foundry Agent Service | Fleksible modeller, bedriftsikkerhet, kodegenerering, verktøyskalling | Modularitet, Samarbeid, Prosesstyring | Sikker, skalerbar og fleksibel distribusjon av AI-agenter |

## Kan jeg integrere mine eksisterende Azure-økosystemverktøy direkte, eller trenger jeg frittstående løsninger?


Svaret er ja, du kan integrere dine eksisterende Azure-økosystemverktøy direkte med Microsoft Foundry Agent Service spesielt, da den er bygget for å fungere sømløst med andre Azure-tjenester. Du kan for eksempel integrere Bing, Azure AI Search og Azure Functions. Det finnes også dyp integrasjon med Microsoft Foundry.

Microsoft Agent Framework integreres også med Azure-tjenester gjennom `FoundryChatClient` og Azure-identitet, noe som lar deg kalle Azure-tjenester direkte fra agentverktøyene dine.

## Eksempelkoder

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Har du flere spørsmål om AI Agent Frameworks?

Bli med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for å møte andre som lærer, delta på kontortid og få svar på spørsmål om AI-agenter.

## Referanser

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Forrige leksjon

[Introduksjon til AI-agenter og agentbrukstilfeller](../01-intro-to-ai-agents/README.md)

## Neste leksjon

[Forstå agentiske designmønstre](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->