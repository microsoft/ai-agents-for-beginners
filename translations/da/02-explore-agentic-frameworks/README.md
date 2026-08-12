[![Udforskning af AI-agentrammer](../../../translated_images/da/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Klik på billedet ovenfor for at se videoen af denne lektion)_

# Udforsk AI Agent-rammer

AI-agentrammer er softwareplatforme designet til at forenkle oprettelsen, udrulningen og styringen af AI-agenter. Disse rammer giver udviklere forudbyggede komponenter, abstraktioner og værktøjer, der effektiviserer udviklingen af komplekse AI-systemer.

Disse rammer hjælper udviklere med at fokusere på de unikke aspekter af deres applikationer ved at tilbyde standardiserede tilgange til almindelige udfordringer i AI-agentudvikling. De forbedrer skalerbarhed, tilgængelighed og effektivitet i opbygningen af AI-systemer.

## Introduktion 

Denne lektion vil dække:

- Hvad er AI Agent-rammer, og hvad kan de hjælpe udviklere med at opnå?
- Hvordan kan teams bruge disse til hurtigt at prototype, iterere og forbedre deres agenters kapaciteter?
- Hvad er forskellene mellem rammerne og værktøjerne skabt af Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> og <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Kan jeg integrere mine eksisterende Azure-økosystemværktøjer direkte, eller har jeg brug for selvstændige løsninger?
- Hvad er Microsoft Foundry Agent Service, og hvordan hjælper det mig?

## Læringsmål

Målet med denne lektion er at hjælpe dig med at forstå:

- AI Agent-rammers rolle i AI-udvikling.
- Hvordan man udnytter AI Agent-rammer til at bygge intelligente agenter.
- Vigtige funktionaliteter, der muliggøres af AI Agent-rammer.
- Forskellene mellem Microsoft Agent Framework og Microsoft Foundry Agent Service.

## Hvad er AI Agent-rammer, og hvad gør de muligt for udviklere?

Traditionelle AI-rammer kan hjælpe dig med at integrere AI i dine apps og gøre disse apps bedre på følgende måder:

- **Personalisering**: AI kan analysere brugeradfærd og præferencer for at tilbyde personlige anbefalinger, indhold og oplevelser.
Eksempel: Streamingtjenester som Netflix bruger AI til at foreslå film og shows baseret på seerhistorik, hvilket øger brugerengagement og tilfredshed.
- **Automatisering og effektivitet**: AI kan automatisere gentagne opgaver, strømline arbejdsgange og forbedre driftseffektiviteten.
Eksempel: Kundeserviceapps bruger AI-drevne chatbots til at håndtere almindelige forespørgsler, reducere svartider og frigøre menneskelige agenter til mere komplekse problemer.
- **Forbedret brugeroplevelse**: AI kan forbedre den samlede brugeroplevelse ved at levere intelligente funktioner som stemmegenkendelse, naturlig sprogbehandling og forudsigende tekst.
Eksempel: Virtuelle assistenter som Siri og Google Assistant bruger AI til at forstå og reagere på stemmekommandoer, hvilket gør det lettere for brugere at interagere med deres enheder.

### Det lyder jo fantastisk, men hvorfor har vi så brug for AI Agent-rammer?

AI Agent-rammer repræsenterer mere end blot AI-rammer. De er designet til at muliggøre skabelsen af intelligente agenter, der kan interagere med brugere, andre agenter og omgivelser for at nå specifikke mål. Disse agenter kan udvise autonom adfærd, træffe beslutninger og tilpasse sig skiftende betingelser. Lad os se på nogle nøglefunktioner, der muliggøres af AI Agent-rammer:

- **Agent-samarbejde og koordinering**: Muliggør oprettelse af flere AI-agenter, der kan arbejde sammen, kommunikere og koordinere for at løse komplekse opgaver.
- **Automatisering og styring af opgaver**: Tilbyder mekanismer til automatisering af flertrinsarbejdsgange, opgavedelegering og dynamisk opgavestyring mellem agenter.
- **Kontekstuel forståelse og tilpasning**: Udstyrer agenter med evnen til at forstå kontekst, tilpasse sig skiftende miljøer og træffe beslutninger baseret på realtidsinformation.

Sammenfattende tillader agenter dig at gøre mere, løfte automatisering til næste niveau og skabe mere intelligente systemer, der kan tilpasse og lære af deres omgivelser.

## Hvordan kan man hurtigt prototype, iterere og forbedre agentens kapaciteter?

Dette er et hurtigt bevægeligt område, men der er nogle fælles elementer i de fleste AI Agent-rammer, som kan hjælpe dig med hurtig prototyping og iteration, nemlig modulære komponenter, samarbejdsværktøjer og realtidslæring. Lad os dykke ned i disse:

- **Brug modulære komponenter**: AI SDK'er tilbyder forbyggede komponenter såsom AI- og Hukommelsesforbindelser, funktionskald via naturligt sprog eller kodeplugins, promptskabeloner og mere.
- **Udnyt samarbejdsværktøjer**: Design agenter med specifikke roller og opgaver, som muliggør test og forbedring af samarbejdsgange.
- **Lær i realtid**: Implementer feedbacksløjfer, hvor agenter lærer fra interaktioner og dynamisk tilpasser deres adfærd.

### Brug modulære komponenter

SDK'er som Microsoft Agent Framework tilbyder forbyggede komponenter såsom AI-forbindelser, værktøjsdefinitioner og agentstyring.

**Hvordan teams kan bruge disse**: Teams kan hurtigt samle disse komponenter for at skabe en fungerende prototype uden at starte fra bunden, hvilket muliggør hurtig eksperimentering og iteration.

**Hvordan det fungerer i praksis**: Du kan bruge en forbygget parser til at udtrække information fra brugerinput, en hukommelsesmodul til at gemme og hente data, og en promptgenerator til at interagere med brugere – alt sammen uden at skulle bygge disse komponenter fra bunden.

**Eksempelkode**. Lad os se på et eksempel på, hvordan du kan bruge Microsoft Agent Framework med `FoundryChatClient` for at få modellen til at reagere på brugerinput med værktøjskald:

``` python
# Microsoft Agent Framework Python Eksempel

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Definer en eksempelværktøjsfunktion til at bestille rejser
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
    # Eksempeluddata: Din flyrejse til New York den 1. januar 2025 er blevet succesfuldt bestilt. God rejse! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Hvad du kan se fra dette eksempel, er hvordan du kan udnytte en forbygget parser til at udtrække nøgleinformation fra brugerinput, såsom afgangssted, destination og dato for en flybookingsanmodning. Denne modulære tilgang gør det muligt at fokusere på den overordnede logik.

### Udnyt samarbejdsværktøjer

Rammer som Microsoft Agent Framework faciliterer oprettelsen af flere agenter, som kan arbejde sammen.

**Hvordan teams kan bruge disse**: Teams kan designe agenter med specifikke roller og opgaver, hvilket giver mulighed for at teste og forbedre samarbejdsgange og øge den samlede systemeffektivitet.

**Hvordan det fungerer i praksis**: Du kan skabe et team af agenter, hvor hver agent har en specialiseret funktion, såsom dataindsamling, analyse eller beslutningstagning. Disse agenter kan kommunikere og dele information for at opnå et fælles mål, f.eks. at besvare en brugerhenvendelse eller udføre en opgave.

**Eksempelkode (Microsoft Agent Framework)**:

```python
# Oprettelse af flere agenter, der arbejder sammen ved hjælp af Microsoft Agent Framework

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Dataindsamlingsagent
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

# Kør agenter i rækkefølge på en opgave
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Hvad du ser i den foregående kode, er hvordan du kan oprette en opgave, der involverer flere agenter, som arbejder sammen om at analysere data. Hver agent udfører en specifik funktion, og opgaven eksekveres ved at koordinere agenterne for at opnå det ønskede resultat. Ved at skabe dedikerede agenter med specialiserede roller kan du forbedre opgaveeffektiviteten og ydeevnen.

### Lær i realtid

Avancerede rammer tilbyder kapaciteter til realtidsforståelse af kontekst og tilpasning.

**Hvordan teams kan bruge disse**: Teams kan implementere feedbacksløjfer, hvor agenter lærer af interaktioner og dynamisk tilpasser deres adfærd, hvilket fører til kontinuerlig forbedring og finjustering af kapaciteter.

**Hvordan det fungerer i praksis**: Agenter kan analysere brugerfeedback, miljødata og opgaveudfald for at opdatere deres videnbase, justere beslutningsalgoritmer og forbedre ydeevne over tid. Denne iterative læringsproces gør det muligt for agenter at tilpasse sig skiftende betingelser og brugerpræferencer, hvilket forbedrer systemets generelle effektivitet.

## Hvad er forskellene mellem Microsoft Agent Framework og Microsoft Foundry Agent Service?

Der findes mange måder at sammenligne disse tilgange på, men lad os se på nogle nøgleforskelle i design, funktionalitet og målrettede anvendelsestilfælde:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework tilbyder en strømlinet SDK til opbygning af AI-agenter ved hjælp af `FoundryChatClient`. Det giver udviklere mulighed for at skabe agenter, der udnytter Azure OpenAI-modeller med indbygget værktøjskald, samtalehåndtering og virksomhedssikkerhed via Azure-identitet.

**Brugstilfælde**: Opbygning af produktionsklare AI-agenter med brug af værktøjer, flertrinsarbejdsgange og integration til erhvervsscenarier.

Her er nogle vigtige kernekoncepter for Microsoft Agent Framework:

- **Agenter**. En agent oprettes via `FoundryChatClient` og konfigureres med et navn, instruktioner og værktøjer. Agenten kan:
  - **Behandle brugermeddelelser** og generere svar ved hjælp af Azure OpenAI-modeller.
  - **Kalde værktøjer** automatisk baseret på samtalekontekst.
  - **Vedligeholde samtalestatus** på tværs af flere interaktioner.

  Her er et kodeeksempel, der viser, hvordan man opretter en agent:

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

- **Værktøjer**. Rammen understøtter definition af værktøjer som Python-funktioner, som agenten kan påkalde automatisk. Værktøjerne registreres, når agenten oprettes:

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

- **Multi-agent koordinering**. Du kan oprette flere agenter med forskellige specialiseringer og koordinere deres arbejde:

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

- **Integration med Azure-identitet**. Rammen bruger `AzureCliCredential` (eller `DefaultAzureCredential`) til sikker, nøglefri autentifikation, hvilket eliminerer behovet for direkte håndtering af API-nøgler.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service er en nyere tilføjelse, præsenteret ved Microsoft Ignite 2024. Det muliggør udvikling og udrulning af AI-agenter med mere fleksible modeller, såsom direkte opkald til open-source LLM'er som Llama 3, Mistral og Cohere.

Microsoft Foundry Agent Service tilbyder stærkere virksomhedssikkerhedsmekanismer og datalagringsmetoder, hvilket gør det egnet til erhvervsapplikationer.

Det fungerer out-of-the-box med Microsoft Agent Framework til opbygning og udrulning af agenter.

Denne tjeneste er aktuelt i offentlig preview og understøtter Python og C# til at bygge agenter.

Med Microsoft Foundry Agent Service Python SDK kan vi oprette en agent med et brugerdefineret værktøj:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Definer værktøjsfunktioner
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

### Kernekoncepter

Microsoft Foundry Agent Service har følgende kernekoncepter:

- **Agent**. Microsoft Foundry Agent Service integreres med Microsoft Foundry. Indenfor Microsoft Foundry agerer en AI Agent som en "smart" mikrotjeneste, der kan bruges til at besvare spørgsmål (RAG), udføre handlinger eller fuldstændigt automatisere arbejdsgange. Det opnås ved at kombinere kraften fra generative AI-modeller med værktøjer, der tillader adgang til og interaktion med virkelige datakilder. Her er et eksempel på en agent:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    I dette eksempel oprettes en agent med modellen `gpt-5-mini`, navn `my-agent` og instruktionen `You are helpful agent`. Agenten er udstyret med værktøjer og ressourcer til at udføre kodefortolkningsopgaver.

- **Tråd og beskeder**. Tråden er et andet vigtigt koncept. Den repræsenterer en samtale eller interaktion mellem en agent og en bruger. Tråde kan bruges til at spore samtalens forløb, gemme kontekstinformation og styre tilstanden i interaktionen. Her er et eksempel på en tråd:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Bed agenten om at udføre arbejde på tråden
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Hent og log alle beskeder for at se agentens svar
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    I den tidligere kode oprettes en tråd. Derefter sendes en besked til tråden. Ved at kalde `create_and_process_run` bliver agenten bedt om at arbejde på tråden. Til sidst hentes og logges beskederne for at se agentens respons. Beskederne indikerer samtalens fremdrift mellem bruger og agent. Det er også vigtigt at forstå, at beskeder kan være af forskellige typer som tekst, billede eller fil, hvilket betyder, at agentens arbejde f.eks. har resulteret i et billede eller en tekstbesked. Som udvikler kan du derefter bruge denne information til yderligere at behandle svaret eller præsentere det for brugeren.

- **Integrerer med Microsoft Agent Framework**. Microsoft Foundry Agent Service arbejder ubesværet sammen med Microsoft Agent Framework, hvilket betyder, at du kan bygge agenter ved hjælp af `FoundryChatClient` og udrulle dem via Agent Service til produktionsscenarier.

**Brugstilfælde**: Microsoft Foundry Agent Service er designet til virksomhedsapplikationer, der kræver sikker, skalerbar og fleksibel AI-agentudrulning.

## Hvad er forskellen mellem disse tilgange?
 
Det lyder som om, der er overlap, men der er nogle nøgleforskelle i design, funktionalitet og målrettede brugstilfælde:
 
- **Microsoft Agent Framework (MAF)**: Er en produktionsklar SDK til opbygning af AI-agenter. Den tilbyder en strømlinet API til at skabe agenter med værktøjskald, samtalehåndtering og Azure-identitetsintegration.
- **Microsoft Foundry Agent Service**: Er en platform og udrulningstjeneste i Microsoft Foundry for agenter. Den tilbyder indbygget forbindelse til tjenester som Azure OpenAI, Azure AI Search, Bing Search og kodeeksekvering.
 
Er du stadig usikker på, hvilken du skal vælge?

### Brugstilfælde
 
Lad os se, om vi kan hjælpe dig ved at gennemgå nogle almindelige brugstilfælde:
 
> Spørgsmål: Jeg bygger produktions-AI-agentapplikationer og vil hurtigt i gang
>

>Svar: Microsoft Agent Framework er et godt valg. Det tilbyder en enkel, pythonisk API via `FoundryChatClient`, som lader dig definere agenter med værktøjer og instruktioner på blot få linjer kode.

>Spørgsmål: Jeg har brug for virksomhedsklar udrulning med Azure-integrationer som Search og kodeeksekvering
>
>Svar: Microsoft Foundry Agent Service er det bedste valg. Det er en platformsservice, der tilbyder indbyggede kapaciteter til flere modeller, Azure AI Search, Bing Search og Azure Functions. Det gør det nemt at bygge dine agenter i Foundry-portalen og udrulle dem i stor skala.
 
> Spørgsmål: Jeg er stadig forvirret, giv mig bare én mulighed
>
> Svar: Start med Microsoft Agent Framework for at bygge dine agenter, og brug derefter Microsoft Foundry Agent Service, når du skal udrulle og skalere dem i produktion. Denne tilgang lader dig hurtigt iterere på agentlogikken samtidig med at du har en klar vej til udrulning i virksomheder.
 
Lad os opsummere nøgleforskellene i en tabel:

| Ramme | Fokus | Kernekoncepter | Brugstilfælde |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Strømlinet agent-SDK med værktøjskald | Agenter, Værktøjer, Azure-identitet | Opbygning af AI-agenter, brug af værktøjer, flertrinsarbejdsgange |
| Microsoft Foundry Agent Service | Fleksible modeller, virksomhedssikkerhed, kodegenerering, værktøjskald | Modularitet, Samarbejde, Procesorkestrering | Sikker, skalerbar og fleksibel AI-agentudrulning |

## Kan jeg integrere mine eksisterende Azure-økosystemværktøjer direkte, eller har jeg brug for selvstændige løsninger?


Svaret er ja, du kan integrere dine eksisterende Azure-økosystemværktøjer direkte med Microsoft Foundry Agent Service, især fordi den er bygget til at arbejde problemfrit sammen med andre Azure-tjenester. Du kan for eksempel integrere Bing, Azure AI Search og Azure Functions. Der er også dyb integration med Microsoft Foundry.

Microsoft Agent Framework integrerer også med Azure-tjenester gennem `FoundryChatClient` og Azure-identitet, hvilket giver dig mulighed for at kalde Azure-tjenester direkte fra dine agentværktøjer.

## Eksempelkoder

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Har du flere spørgsmål om AI Agent Frameworks?

Deltag i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for at møde andre lærende, deltage i kontortimer og få svar på dine spørgsmål om AI-agenter.

## Referencer

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Forrige lektion

[Introduktion til AI-agenter og agentbrugsscenarier](../01-intro-to-ai-agents/README.md)

## Næste lektion

[Forståelse af agentiske designmønstre](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->