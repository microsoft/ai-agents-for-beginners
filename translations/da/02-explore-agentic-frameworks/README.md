[![Udforskning af AI-agentrammer](../../../translated_images/da/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Klik på billedet ovenfor for at se video af denne lektion)_

# Udforsk AI-agentrammer

AI-agentrammer er softwareplatforme designet til at forenkle oprettelsen, implementeringen og styringen af AI-agenter. Disse rammer giver udviklere forudbyggede komponenter, abstraktioner og værktøjer, der effektiviserer udviklingen af komplekse AI-systemer.

Disse rammer hjælper udviklere med at fokusere på de unikke aspekter af deres applikationer ved at tilbyde standardiserede tilgange til almindelige udfordringer i AI-agentudvikling. De forbedrer skalerbarhed, tilgængelighed og effektivitet i opbygningen af AI-systemer.

## Introduktion

Denne lektion vil dække:

- Hvad er AI-agentrammer, og hvad gør de det muligt for udviklere at opnå?
- Hvordan kan teams bruge disse til hurtigt at prototype, iterere og forbedre agentens kapaciteter?
- Hvad er forskellene mellem rammerne og værktøjerne skabt af Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> og <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Kan jeg integrere mine eksisterende Azure-økosystemværktøjer direkte, eller har jeg brug for selvstændige løsninger?
- Hvad er Azure AI Agents service, og hvordan hjælper den mig?

## Læringsmål

Målene med denne lektion er at hjælpe dig med at forstå:

- AI-agentrammers rolle i AI-udvikling.
- Hvordan man udnytter AI-agentrammer til at bygge intelligente agenter.
- Nøglefunktioner muligg jort af AI-agentrammer.
- Forskellene mellem Microsoft Agent Framework og Azure AI Agent Service.

## Hvad er AI-agentrammer, og hvad gør de udviklere i stand til?

Traditionelle AI-rammer kan hjælpe dig med at integrere AI i dine apps og gøre disse apps bedre på følgende måder:

- **Personalisering**: AI kan analysere brugeradfærd og præferencer for at give personlige anbefalinger, indhold og oplevelser.  
Eksempel: Streamingtjenester som Netflix bruger AI til at foreslå film og shows baseret på seerhistorik, hvilket øger brugerengagement og tilfredshed.  
- **Automation og effektivitet**: AI kan automatisere gentagne opgaver, strømline arbejdsgange og forbedre operationel effektivitet.  
Eksempel: Kundeservice-apps bruger AI-drevne chatbots til at håndtere almindelige forespørgsler, reducere svartider og frigøre menneskelige agenter til mere komplekse problemer.  
- **Forbedret brugeroplevelse**: AI kan forbedre den overordnede brugeroplevelse ved at tilbyde intelligente funktioner såsom stemmegenkendelse, naturlig sprogbehandling og forudsigende tekst.  
Eksempel: Virtuelle assistenter som Siri og Google Assistant bruger AI til at forstå og reagere på stemmekommandoer, hvilket gør det lettere for brugere at interagere med deres enheder.

### Det lyder godt, ikke? Så hvorfor har vi brug for AI-agentrammen?

AI-agentrammer repræsenterer mere end blot AI-rammer. De er designet til at muliggøre oprettelsen af intelligente agenter, der kan interagere med brugere, andre agenter og miljøet for at nå specifikke mål. Disse agenter kan udvise autonom adfærd, træffe beslutninger og tilpasse sig skiftende forhold. Lad os se på nogle nøglefunktioner, der muliggøres af AI-agentrammer:

- **Agent samarbejde og koordinering**: Muliggør oprettelsen af flere AI-agenter, der kan arbejde sammen, kommunikere og koordinere for at løse komplekse opgaver.
- **Opgaveautomatisering og styring**: Tilbyder mekanismer til automatisering af arbejdsprocesser med flere trin, opgavedeling og dynamisk opgavestyring blandt agenter.
- **Kontextforståelse og tilpasning**: Udstyrer agenter med evnen til at forstå kontekst, tilpasse sig skiftende miljøer og træffe beslutninger baseret på realtidsinformation.

Sammenfattende giver agenter dig mulighed for at gøre mere, løfte automatisering til næste niveau, og skabe mere intelligente systemer, der kan tilpasse sig og lære fra deres omgivelser.

## Hvordan kan man hurtigt prototype, iterere og forbedre agentens kapaciteter?

Dette er et hurtigt udviklende område, men der er nogle ting, der er fælles på tværs af de fleste AI-agentrammer, som kan hjælpe dig med hurtigt at prototype og iterere – nemlig modulære komponenter, samarbejdsværktøjer og realtidslæring. Lad os dykke ned i disse:

- **Brug modulære komponenter**: AI SDK'er tilbyder forudbyggede komponenter som AI- og hukommelsesforbindelser, funktion kald ved brug af naturligt sprog eller kode plugins, prompt-skabeloner og mere.
- **Udnyt samarbejdsværktøjer**: Design agenter med specifikke roller og opgaver, så de kan teste og forfine samarbejdsarbejdsgange.
- **Lær i realtid**: Implementer feedback-sløjfer, hvor agenter lærer af interaktioner og tilpasser deres adfærd dynamisk.

### Brug modulære komponenter

SDK'er som Microsoft Agent Framework tilbyder forudbyggede komponenter såsom AI-forbindelser, værktøjsdefinitioner og agentstyring.

**Hvordan teams kan bruge dem**: Teams kan hurtigt samle disse komponenter for at skabe en funktionel prototype uden at starte fra bunden, hvilket muliggør hurtige eksperimenter og iterationer.

**Hvordan det fungerer i praksis**: Du kan bruge en forudbygget parser til at udtrække information fra brugerinput, en hukommelsesmodul til at gemme og hente data samt en prompt-generator til at interagere med brugere – alt sammen uden at skulle bygge disse komponenter fra bunden.

**Eksempel kode**. Lad os se på et eksempel på, hvordan du kan bruge Microsoft Agent Framework med `AzureAIProjectAgentProvider` til at få modellen til at svare på brugerinput med værktøjskald:

``` python
# Microsoft Agent Framework Python Eksempel

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# Definer en eksempel værktøjsfunktion til at booke rejser
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # Eksempel output: Din flyrejse til New York den 1. januar 2025 er blevet succesfuldt booket. God rejse! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```
  
Det, du kan se fra dette eksempel, er, hvordan du kan udnytte en forudbygget parser til at udtrække nøgleinformation fra brugerinput, såsom oprindelse, destination og dato for en flybooking-forespørgsel. Denne modulære tilgang giver dig mulighed for at fokusere på det overordnede logikniveau.

### Udnyt samarbejdsværktøjer

Rammer som Microsoft Agent Framework gør det muligt at skabe flere agenter, der kan arbejde sammen.

**Hvordan teams kan bruge dem**: Teams kan designe agenter med specifikke roller og opgaver, så de kan teste og forfine samarbejdsarbejdsgange og forbedre systemets samlede effektivitet.

**Hvordan det fungerer i praksis**: Du kan oprette et team af agenter, hvor hver agent har en specialiseret funktion, såsom dataindhentning, analyse eller beslutningstagning. Disse agenter kan kommunikere og dele information for at nå et fælles mål, såsom at besvare en brugerforespørgsel eller fuldføre en opgave.

**Eksempel kode (Microsoft Agent Framework)**:

```python
# Opretter flere agenter, der arbejder sammen ved hjælp af Microsoft Agent Framework

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Dataindsamlingsagent
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Dataanalyseagent
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Kør agenter i rækkefølge på en opgave
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```
  
Det, du ser i den foregående kode, er, hvordan du kan skabe en opgave, der involverer flere agenter, som arbejder sammen om at analysere data. Hver agent udfører en specifik funktion, og opgaven udføres ved at koordinere agenternes arbejde for at opnå det ønskede resultat. Ved at skabe dedikerede agenter med specialiserede roller kan du forbedre opgaveeffektivitet og ydeevne.

### Lær i realtid

Avancerede rammer tilbyder muligheder for realtids-kontekstforståelse og tilpasning.

**Hvordan teams kan bruge det**: Teams kan implementere feedback-sløjfer, hvor agenter lærer af interaktioner og justerer deres adfærd dynamisk, hvilket fører til løbende forbedring og finjustering af kapaciteter.

**Hvordan det fungerer i praksis**: Agenter kan analysere brugerfeedback, miljødata og opgaveudfald for at opdatere deres vidensbase, justere beslutningstagende algoritmer og forbedre ydeevnen over tid. Denne iterative læringsproces gør, at agenter kan tilpasse sig skiftende forhold og brugerpræferencer og dermed øge systemets samlede effektivitet.

## Hvad er forskellene mellem Microsoft Agent Framework og Azure AI Agent Service?

Der er mange måder at sammenligne disse tilgange på, men lad os se på nogle nøgleforskelle med hensyn til design, kapaciteter og målrettede anvendelsestilfælde:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework tilbyder et strømlinet SDK til at bygge AI-agenter ved hjælp af `AzureAIProjectAgentProvider`. Det gør udviklere i stand til at skabe agenter, der udnytter Azure OpenAI-modeller med indbygget værktøjskald, samtalestyring og virksomhedsgradssikkerhed gennem Azure-identitet.

**Anvendelsestilfælde**: Opbygning af produktionsklar AI-agenter med værktøjsbrug, arbejdsprocesser med flere trin og virksomhedsintegrationsscenarier.

Her er nogle vigtige kernekoncepter i Microsoft Agent Framework:

- **Agenter**. En agent oprettes via `AzureAIProjectAgentProvider` og konfigureres med navn, instruktioner og værktøjer. Agenten kan:
  - **Behandle brugermeddelelser** og generere svar ved brug af Azure OpenAI-modeller.
  - **Automatisk kalde værktøjer** baseret på samtalekonteksten.
  - **Opretholde samtalestatus** på tværs af flere interaktioner.

  Her er et kodeeksempel, der viser, hvordan man opretter en agent:

    ```python
    import os
    from agent_framework.azure import AzureAIProjectAgentProvider
    from azure.identity import AzureCliCredential

    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```
  
- **Værktøjer**. Frameworket understøtter definition af værktøjer som Python-funktioner, som agenten kan kalde automatisk. Værktøjer registreres ved oprettelse af agenten:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = await provider.create_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```
  
- **Multi-agent koordinering**. Du kan oprette flere agenter med forskellige specialiseringer og koordinere deres arbejde:

    ```python
    planner = await provider.create_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = await provider.create_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```
  
- **Azure-identitetsintegration**. Frameworket bruger `AzureCliCredential` (eller `DefaultAzureCredential`) til sikker, nøglefri autentifikation, hvilket eliminerer behovet for at administrere API-nøgler direkte.

## Azure AI Agent Service

Azure AI Agent Service er en nyere tilføjelse, introduceret ved Microsoft Ignite 2024. Den giver mulighed for udvikling og implementering af AI-agenter med mere fleksible modeller, som for eksempel direkte kald til open source LLM'er som Llama 3, Mistral og Cohere.

Azure AI Agent Service tilbyder stærkere sikkerhedsmekanismer for virksomheder og datalagringsmetoder, hvilket gør det velegnet til virksomhedsapplikationer.

Den fungerer ud af boksen sammen med Microsoft Agent Framework til at bygge og implementere agenter.

Denne service er i øjeblikket i Public Preview og understøtter Python og C# til opbygning af agenter.

Ved hjælp af Azure AI Agent Service Python SDK kan vi oprette en agent med et brugertilpasset værktøj:

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
  
### Kernekoncepter

Azure AI Agent Service har følgende kernekoncepter:

- **Agent**. Azure AI Agent Service integreres med Microsoft Foundry. Inden for AI Foundry fungerer en AI-agent som en "smart" mikrotjeneste, der kan bruges til at besvare spørgsmål (RAG), udføre handlinger eller fuldstændigt automatisere arbejdsprocesser. Det opnås ved at kombinere kraften i generative AI-modeller med værktøjer, der giver adgang til og mulighed for interaktion med virkelige datakilder. Her er et eksempel på en agent:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```
  
    I dette eksempel oprettes en agent med modellen `gpt-4o-mini`, navnet `my-agent` og instruktionerne `You are helpful agent`. Agenten er udstyret med værktøjer og ressourcer til at udføre kodefortolkningsopgaver.

- **Tråd og beskeder**. Tråden er et andet vigtigt koncept. Den repræsenterer en samtale eller interaktion mellem en agent og en bruger. Tråde kan bruges til at følge samtalens forløb, gemme kontekstinformation og styre interaktionens tilstand. Her er et eksempel på en tråd:

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
  
    I den foregående kode oprettes en tråd. Derefter sendes en besked til tråden. Ved at kalde `create_and_process_run` bliver agenten bedt om at udføre arbejde på tråden. Endelig hentes og logges beskederne for at se agentens svar. Beskederne angiver samtalens forløb mellem brugeren og agenten. Det er også vigtigt at forstå, at beskederne kan være af forskellige typer såsom tekst, billede eller fil, hvilket betyder, at agentens arbejde for eksempel har resulteret i et billede eller et tekstsvar. Som udvikler kan du bruge denne information til yderligere behandling af svaret eller præsentere det for brugeren.

- **Integration med Microsoft Agent Framework**. Azure AI Agent Service fungerer problemfrit sammen med Microsoft Agent Framework, hvilket betyder, at du kan bygge agenter ved hjælp af `AzureAIProjectAgentProvider` og implementere dem via Agent Service til produktionsscenarier.

**Anvendelsestilfælde**: Azure AI Agent Service er designet til virksomhedsapplikationer, der kræver sikker, skalerbar og fleksibel AI-agentimplementering.

## Hvad er forskellen mellem disse tilgange?

Der er tilsyneladende overlap, men der er nogle nøgleforskelle i design, kapaciteter og målrettede anvendelsestilfælde:

- **Microsoft Agent Framework (MAF)**: Er et produktionsklart SDK til opbygning af AI-agenter. Det tilbyder et strømlinet API til oprettelse af agenter med værktøjskald, samtalestyring og Azure-identitetsintegration.
- **Azure AI Agent Service**: Er en platform og implementeringstjeneste i Azure Foundry til agenter. Den tilbyder indbygget forbindelse til tjenester som Azure OpenAI, Azure AI Search, Bing Search og kodeudførelse.

Er du stadig i tvivl om, hvilken du skal vælge?

### Anvendelsestilfælde

Lad os se, om vi kan hjælpe dig ved at gennemgå nogle almindelige anvendelsestilfælde:

> Q: Jeg bygger produktionsapplikationer med AI-agenter og vil hurtigt i gang  
>

> A: Microsoft Agent Framework er et godt valg. Det tilbyder et enkelt, Python-venligt API via `AzureAIProjectAgentProvider`, der lader dig definere agenter med værktøjer og instruktioner med få kodelinjer.

> Q: Jeg har brug for implementering i virksomhedsgrad med Azure-integrationer som Search og kodeudførelse  
>
> A: Azure AI Agent Service er det bedste valg. Det er en platformtjeneste, der tilbyder indbyggede funktioner til flere modeller, Azure AI Search, Bing Search og Azure Functions. Det gør det nemt at bygge dine agenter i Foundry-portalen og implementere dem i stor skala.

> Q: Jeg er stadig forvirret, giv mig bare én mulighed  
>
> A: Start med Microsoft Agent Framework til at bygge dine agenter, og brug derefter Azure AI Agent Service, når du skal implementere og skalere dem i produktion. Denne tilgang lader dig iterere hurtigt på agentlogikken, samtidig med at du har en klar vej til virksomhedens implementering.

Lad os opsummere de vigtigste forskelle i en tabel:

| Framework | Fokus | Kernekoncepter | Anvendelsestilfælde |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Strømlinet agent-SDK med værktøjskald | Agenter, Værktøjer, Azure-identitet | Bygning af AI-agenter, værktøjsbrug, arbejdsprocesser med flere trin |
| Azure AI Agent Service | Fleksible modeller, virksomhedssikkerhed, kodegenerering, værktøjskald | Modularitet, samarbejde, procesorkestrering | Sikker, skalerbar og fleksibel AI-agentimplementering |

## Kan jeg integrere mine eksisterende Azure-økosystemværktøjer direkte, eller har jeg brug for selvstændige løsninger?
Svaret er ja, du kan integrere dine eksisterende Azure-økosystemværktøjer direkte med Azure AI Agent Service, især fordi den er bygget til at fungere problemfrit med andre Azure-tjenester. Du kan for eksempel integrere Bing, Azure AI Search og Azure Functions. Der er også dyb integration med Microsoft Foundry.

Microsoft Agent Framework integrerer også med Azure-tjenester gennem `AzureAIProjectAgentProvider` og Azure-identitet, hvilket gør det muligt at kalde Azure-tjenester direkte fra dine agentværktøjer.

## Sample Codes

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Har du flere spørgsmål om AI Agent Frameworks?

Deltag i [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) for at møde andre lærende, deltage i kontortimer og få svar på dine spørgsmål om AI-agenter.

## Referencer

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>

## Forrige lektion

[Introduction to AI Agents and Agent Use Cases](../01-intro-to-ai-agents/README.md)

## Næste lektion

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->