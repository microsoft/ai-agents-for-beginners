[![Utforske AI-agentrammeverk](../../../translated_images/no/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Klikk på bildet ovenfor for å se videoen til denne leksjonen)_

# Utforsk AI-agentrammeverk

AI-agentrammeverk er programvareplattformer designet for å forenkle opprettelsen, distribusjonen og administrasjonen av AI-agenter. Disse rammeverkene gir utviklere ferdigbygde komponenter, abstraksjoner og verktøy som effektiviserer utviklingen av komplekse AI-systemer.

Disse rammeverkene hjelper utviklere med å fokusere på de unike aspektene ved deres applikasjoner ved å tilby standardiserte tilnærminger til vanlige utfordringer i AI-agentutvikling. De forbedrer skalerbarhet, tilgjengelighet og effektivitet i bygging av AI-systemer.

## Innledning 

Denne leksjonen vil dekke:

- Hva er AI-agentrammeverk og hva gjør de utviklere i stand til å oppnå?
- Hvordan kan team bruke disse for å raskt prototype, iterere og forbedre agentens evner?
- Hva er forskjellene mellom rammeverkene og verktøyene laget av Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> og <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Kan jeg integrere mine eksisterende Azure-økosystemverktøy direkte, eller trenger jeg frittstående løsninger?
- Hva er Microsoft Foundry Agent Service og hvordan hjelper det meg?

## Læringsmål

Målet med denne leksjonen er å hjelpe deg å forstå:

- Rollen til AI-agentrammeverk i AI-utvikling.
- Hvordan bruke AI-agentrammeverk for å bygge intelligente agenter.
- Nøkkelfunksjoner som muliggjøres av AI-agentrammeverk.
- Forskjellene mellom Microsoft Agent Framework og Microsoft Foundry Agent Service.

## Hva er AI-agentrammeverk og hva gjør de utviklere i stand til å gjøre?

Tradisjonelle AI-rammeverk kan hjelpe deg med å integrere AI i appene dine og forbedre disse appene på følgende måter:

- **Personalisering**: AI kan analysere brukeradferd og preferanser for å tilby personlige anbefalinger, innhold og opplevelser.
Eksempel: Strømmetjenester som Netflix bruker AI for å foreslå filmer og serier basert på seerhistorikk, noe som øker brukerengasjement og tilfredshet.
- **Automatisering og effektivitet**: AI kan automatisere repeterende oppgaver, strømlinjeforme arbeidsflyter og forbedre driftseffektiviteten.
Eksempel: Kundeserviceapper bruker AI-drevne chatbots for å håndtere vanlige forespørsler, redusere responstid og frigjøre menneskelige agenter til mer komplekse saker.
- **Forbedret brukeropplevelse**: AI kan forbedre den totale brukeropplevelsen ved å tilby intelligente funksjoner som stemmegjenkjenning, naturlig språkbehandling og prediktiv tekst.
Eksempel: Virtuelle assistenter som Siri og Google Assistant bruker AI for å forstå og svare på stemmekommandoer, noe som gjør det enklere for brukere å samhandle med enhetene sine.

### Det høres jo flott ut, så hvorfor trenger vi AI-agentrammeverket?

AI-agentrammeverk representerer noe mer enn bare AI-rammeverk. De er designet for å muliggjøre opprettelse av intelligente agenter som kan samhandle med brukere, andre agenter og miljøet for å oppnå spesifikke mål. Disse agentene kan utvise autonom oppførsel, fatte beslutninger og tilpasse seg endrede forhold. La oss se på noen nøkkelfunksjoner som muliggjøres av AI-agentrammeverk:

- **Agent-samarbeid og koordinering**: Muliggjør opprettelse av flere AI-agenter som kan jobbe sammen, kommunisere og koordinere for å løse komplekse oppgaver.
- **Automatisering og administrasjon av oppgaver**: Gir mekanismer for automatisering av flertrinns arbeidsflyter, oppgavedeling og dynamisk oppgavehåndtering blant agenter.
- **Kontekstuelt forståelse og tilpasning**: Utstyrer agenter med evne til å forstå kontekst, tilpasse seg endrede miljøer og fatte beslutninger basert på sanntidsinformasjon.

Kort oppsummert lar agenter deg gjøre mer, ta automatisering til neste nivå, og skape mer intelligente systemer som kan tilpasse seg og lære av sitt miljø.

## Hvordan raskt prototype, iterere og forbedre agentens evner?

Dette er et raskt bevegende landskap, men det finnes noen ting som er felles for de fleste AI-agentrammeverk som kan hjelpe deg å raskt prototype og iterere, nemlig modulære komponenter, samarbeidsverktøy og læring i sanntid. La oss dykke ned i disse:

- **Bruk modulære komponenter**: AI SDK-er tilbyr ferdigbygde komponenter som AI- og minnekoblinger, funksjonskall ved hjelp av naturlig språk eller kode-plugins, promptmaler og mer.
- **Utnytt samarbeidsverktøy**: Design agenter med spesifikke roller og oppgaver, som gjør det mulig å teste og forbedre samarbeidsarbeidsflyter.
- **Lær i sanntid**: Implementer tilbakemeldingssløyfer hvor agenter lærer av interaksjoner og justerer sin oppførsel dynamisk.

### Bruk modulære komponenter

SDK-er som Microsoft Agent Framework tilbyr ferdigbygde komponenter som AI-koblinger, verktøydefinisjoner og agentadministrasjon.

**Hvordan team kan bruke disse**: Team kan raskt sette sammen disse komponentene for å lage en funksjonell prototype uten å starte fra bunnen, noe som tillater rask eksperimentering og iterasjon.

**Hvordan det fungerer i praksis**: Du kan bruke en ferdigbygget parser for å trekke ut informasjon fra brukerinnspill, en minnemodul for å lagre og hente data, og en promptgenerator for å samhandle med brukere, alt uten å måtte bygge disse komponentene fra bunnen.

**Eksempelkode**. La oss se på et eksempel på hvordan du kan bruke Microsoft Agent Framework med `FoundryChatClient` for å få modellen til å svare på brukerinnspill med verktøykall:

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
    # Eksempelutdata: Din flyreise til New York den 1. januar 2025 er vellykket bestilt. God reise! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Det du kan se fra dette eksempelet er hvordan du kan utnytte en ferdigbygget parser til å trekke ut nøkkelinformasjon fra brukerinnspill, som opprinnelse, destinasjon og dato for en flybestillingsforespørsel. Denne modulære tilnærmingen lar deg fokusere på den overordnede logikken.

### Utnytt samarbeidsverktøy

Rammeverk som Microsoft Agent Framework legger til rette for opprettelse av flere agenter som kan jobbe sammen.

**Hvordan team kan bruke disse**: Team kan designe agenter med spesifikke roller og oppgaver, som gjør det mulig å teste og finpusse samarbeidsarbeidsflyter og forbedre systemets totale effektivitet.

**Hvordan det fungerer i praksis**: Du kan lage et team av agenter hvor hver agent har en spesialisert funksjon, som datauthenting, analyse eller beslutningstaking. Disse agentene kan kommunisere og dele informasjon for å oppnå et felles mål, som å svare på en brukerhenvendelse eller fullføre en oppgave.

**Eksempelkode (Microsoft Agent Framework)**:

```python
# Opprette flere agenter som samarbeider ved hjelp av Microsoft Agent Framework

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Datautvinningsagent
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

# Kjør agenter i rekkefølge på en oppgave
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Det du ser i forrige kode er hvordan du kan opprette en oppgave som involverer flere agenter som jobber sammen om å analysere data. Hver agent utfører en spesifikk funksjon, og oppgaven utføres ved å koordinere agentene for å oppnå ønsket resultat. Ved å opprette dedikerte agenter med spesialiserte roller, kan du forbedre oppgavens effektivitet og ytelse.

### Lær i sanntid

Avanserte rammeverk tilbyr funksjoner for sanntids kontekstforståelse og tilpasning.

**Hvordan team kan bruke disse**: Team kan implementere tilbakemeldingssløyfer hvor agenter lærer fra interaksjoner og justerer sin oppførsel dynamisk, noe som fører til kontinuerlig forbedring og finjustering av evner.

**Hvordan det fungerer i praksis**: Agenter kan analysere brukerfeedback, miljødata og oppgaveutfall for å oppdatere kunnskapsbasen, justere beslutningsalgoritmer og forbedre ytelsen over tid. Denne iterative læringsprosessen gjør at agenter kan tilpasse seg endringer i forhold og brukerpreferanser, og øker den totale systemeffektiviteten.

## Hva er forskjellene mellom Microsoft Agent Framework og Microsoft Foundry Agent Service?

Det finnes mange måter å sammenligne disse tilnærmingene på, men la oss se på noen viktige forskjeller når det gjelder design, funksjoner og målrettede bruksområder:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework tilbyr en strømlinjeformet SDK for å bygge AI-agenter ved bruk av `FoundryChatClient`. Det gjør utviklere i stand til å lage agenter som utnytter Azure OpenAI-modeller med innebygd verktøykall, samtalehåndtering og bedriftsklasse sikkerhet via Azure-identitet.

**Bruksområder**: Lage produksjonsklare AI-agenter med verktøybruk, flertrinns arbeidsflyter og bedriftsintegrasjonsscenarier.

Her er noen viktige kjernebegreper i Microsoft Agent Framework:

- **Agenter**. En agent opprettes via `FoundryChatClient` og konfigureres med navn, instruksjoner og verktøy. Agenten kan:
  - **Behandle brukerbeskjeder** og generere svar ved hjelp av Azure OpenAI-modeller.
  - **Kalle verktøy** automatisk basert på samtalekontekst.
  - **Opprettholde samtaletilstand** over flere interaksjoner.

  Her er et kodeutdrag som viser hvordan man oppretter en agent:

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

- **Verktøy**. Rammeverket støtter definisjon av verktøy som Python-funksjoner som agenten kan påkalle automatisk. Verktøy registreres ved oppretting av agenten:

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

- **Multi-agent koordinering**. Du kan opprette flere agenter med ulike spesialiseringer og koordinere deres arbeid:

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

- **Azure Identity-integrasjon**. Rammeverket bruker `AzureCliCredential` (eller `DefaultAzureCredential`) for sikker, nøkkelfri autentisering, hvilket eliminerer behovet for å håndtere API-nøkler direkte.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service er et nyere tilskudd, introdusert på Microsoft Ignite 2024. Det muliggjør utvikling og distribusjon av AI-agenter med mer fleksible modeller, som direkte kall til open-source LLM-er som Llama 3, Mistral og Cohere.

Microsoft Foundry Agent Service tilbyr sterkere bedriftsikkerhetsmekanismer og data-lagringsmetoder, som gjør det egnet for virksomhetsapplikasjoner.

Det fungerer sømløst sammen med Microsoft Agent Framework for bygging og distribusjon av agenter.

Denne tjenesten er for øyeblikket i Public Preview og støtter Python og C# for agentutvikling.

Ved å bruke Microsoft Foundry Agent Service Python SDK kan vi lage en agent med et brukerdefinert verktøy:

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
        model="gpt-5-mini",
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

### Kjernebegreper

Microsoft Foundry Agent Service har følgende kjernebegreper:

- **Agent**. Microsoft Foundry Agent Service integrerer med Microsoft Foundry. Innen Microsoft Foundry fungerer en AI-Agent som en "smart" mikrotjeneste som kan brukes til å svare på spørsmål (RAG), utføre handlinger eller fullstendig automatisere arbeidsflyter. Det oppnår dette ved å kombinere kraften i generative AI-modeller med verktøy som lar den få tilgang til og samhandle med virkelige datakilder. Her er et eksempel på en agent:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    I dette eksemplet opprettes en agent med modellen `gpt-5-mini`, navnet `my-agent` og instruksjonene `You are helpful agent`. Agenten er utstyrt med verktøy og ressurser for å utføre kode-tolkingsoppgaver.

- **Tråd og meldinger**. Tråden er et annet viktig konsept. Den representerer en samtale eller interaksjon mellom en agent og en bruker. Tråder kan brukes til å spore fremgangen i en samtale, lagre kontekstinformasjon, og håndtere tilstanden til interaksjonen. Her er et eksempel på en tråd:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Be agenten om å utføre arbeid på tråden
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Hent og loggfør alle meldinger for å se agentens respons
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    I forrige kode opprettes en tråd. Deretter sendes en melding til tråden. Ved å kalle `create_and_process_run` blir agenten bedt om å utføre arbeid i tråden. Til slutt hentes meldingene og loggføres for å se agentens respons. Meldingene indikerer fremdriften i samtalen mellom bruker og agent. Det er også viktig å forstå at meldingene kan være av forskjellige typer som tekst, bilde eller fil, det vil si at agentens arbeid har resultert i for eksempel et bilde eller et tekstsvar. Som utvikler kan du da bruke denne informasjonen til å viderebehandle responsen eller presentere den til brukeren.

- **Integrerer med Microsoft Agent Framework**. Microsoft Foundry Agent Service fungerer sømløst med Microsoft Agent Framework, noe som betyr at du kan bygge agenter med `FoundryChatClient` og distribuere dem gjennom Agent Service for produksjonsscenarier.

**Bruksområder**: Microsoft Foundry Agent Service er designet for bedriftsapplikasjoner som krever sikker, skalerbar og fleksibel AI-agentdistribusjon.

## Hva er forskjellen mellom disse tilnærmingene?
 
Det kan høres ut som det er overlapp, men det finnes noen viktige forskjeller i design, funksjonalitet og målrettede bruksområder:
 
- **Microsoft Agent Framework (MAF)**: Er en produksjonsklar SDK for bygging av AI-agenter. Den tilbyr et strømlinjeformet API for å lage agenter med verktøykall, samtalehåndtering og Azure-identitetsintegrasjon.
- **Microsoft Foundry Agent Service**: Er en plattform og distribusjonstjeneste i Microsoft Foundry for agenter. Den tilbyr innebygd tilkobling til tjenester som Azure OpenAI, Azure AI Search, Bing Search og kodekjøring.
 
Er du fortsatt usikker på hvilken du skal velge?

### Bruksområder
 
La oss se om vi kan hjelpe deg ved å gå gjennom noen vanlige brukstilfeller:
 
> Q: Jeg bygger produksjonsklare AI-agentapplikasjoner og vil komme raskt i gang
>

>A: Microsoft Agent Framework er et godt valg. Det tilbyr et enkelt, Python-vennlig API via `FoundryChatClient` som lar deg definere agenter med verktøy og instruksjoner i bare noen få kodelinjer.

>Q: Jeg trenger bedriftsklasse distribusjon med Azure-integrasjoner som Search og kodekjøring
>
> A: Microsoft Foundry Agent Service passer best. Det er en plattformtjeneste som tilbyr innebygde funksjoner for flere modeller, Azure AI Search, Bing Search og Azure Functions. Det gjør det enkelt å bygge agentene dine i Foundry-portalen og distribuere dem i stor skala.
 
> Q: Jeg er fortsatt forvirret, gi meg bare ett valg
>
> A: Start med Microsoft Agent Framework for å bygge agentene dine, og bruk deretter Microsoft Foundry Agent Service når du trenger å distribuere og skalere dem i produksjon. Denne tilnærmingen lar deg iterere raskt på agentlogikken mens du har en klar vei til bedriftsdistribusjon.
 
La oss oppsummere nøkkelforskjellene i en tabell:

| Rammeverk | Fokus | Kjernebegreper | Bruksområder |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Strømlinjeformet agent-SDK med verktøykall | Agenter, Verktøy, Azure Identity | Bygge AI-agenter, verktøybruk, flertrinns arbeidsflyter |
| Microsoft Foundry Agent Service | Fleksible modeller, bedriftsikkerhet, kodegenerering, verktøykall | Modularitet, Samarbeid, Prosessorchestrering | Sikker, skalerbar og fleksibel AI-agentdistribusjon |

## Kan jeg integrere mine eksisterende Azure-økosystemverktøy direkte, eller trenger jeg frittstående løsninger?


Svaret er ja, du kan integrere dine eksisterende Azure-økosystemverktøy direkte med Microsoft Foundry Agent Service spesielt, siden det er bygget for å fungere sømløst med andre Azure-tjenester. Du kan for eksempel integrere Bing, Azure AI Search og Azure Functions. Det er også dyp integrasjon med Microsoft Foundry.

Microsoft Agent Framework integreres også med Azure-tjenester gjennom `FoundryChatClient` og Azure-identitet, som lar deg kalle Azure-tjenester direkte fra agentverktøyene dine.

## Eksempelkoder

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Flere spørsmål om AI Agent Frameworks?

Bli med i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for å møte andre som lærer, delta på kontortimer og få svar på spørsmål om AI-agenter.

## Referanser

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Forrige leksjon

[Introduksjon til AI-agenter og bruksområder for agenter](../01-intro-to-ai-agents/README.md)

## Neste leksjon

[Forstå else av agentdrevne designmønstre](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->