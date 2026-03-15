[![Udforsk AI-agentrammer](../../../translated_images/da/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Klik på billedet ovenfor for at se videoen til denne lektion)_

# Udforsk AI-agentrammer

AI-agentrammer er softwareplatforme designet til at forenkle oprettelsen, udrulningen og styringen af AI-agenter. Disse rammer giver udviklere færdigbyggede komponenter, abstraktioner og værktøjer, der gør udviklingen af komplekse AI-systemer mere effektiv.

Disse rammer hjælper udviklere med at fokusere på de unikke aspekter af deres applikationer ved at tilbyde standardiserede tilgange til almindelige udfordringer i udviklingen af AI-agenter. De øger skalerbarhed, tilgængelighed og effektivitet ved opbygning af AI-systemer.

## Introduktion 

Denne lektion dækker:

- Hvad er AI-agentrammer, og hvad gør de muligt for udviklere?
- Hvordan kan teams bruge disse til hurtigt at prototype, iterere og forbedre agentens evner?
- Hvad er forskellene mellem de rammer og værktøjer, der er lavet af Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> og the <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Kan jeg integrere mine eksisterende Azure-økosystemværktøjer direkte, eller har jeg brug for selvstændige løsninger?
- Hvad er Azure AI Agents service, og hvordan hjælper den mig?

## Læringsmål

Målet med denne lektion er at hjælpe dig med at forstå:

- Rollen for AI-agentrammer i AI-udvikling.
- Hvordan man udnytter AI-agentrammer til at bygge intelligente agenter.
- Centrale kapabiliteter, som AI-agentrammer muliggør.
- Forskellene mellem Microsoft Agent Framework og Azure AI Agent Service.

## Hvad er AI Agent Frameworks og hvad gør de muligt for udviklere?

Traditionelle AI-rammer kan hjælpe dig med at integrere AI i dine apps og forbedre dem på følgende måder:

- **Personalization**: AI kan analysere brugeradfærd og præferencer for at give personlige anbefalinger, indhold og oplevelser.
Eksempel: Streamingtjenester som Netflix bruger AI til at foreslå film og serier baseret på seerhistorik, hvilket øger brugerengagement og tilfredshed.
- **Automation and Efficiency**: AI kan automatisere gentagne opgaver, strømline arbejdsgange og forbedre operationel effektivitet.
Eksempel: Kundeserviceapps bruger AI-drevne chatbots til at håndtere almindelige forespørgsler, hvilket reducerer svartider og frigør menneskelige agenter til mere komplekse problemer.
- **Enhanced User Experience**: AI kan forbedre den samlede brugeroplevelse ved at levere intelligente funktioner såsom stemmegenkendelse, naturlig sprogbehandling og forudsigende tekst.
Eksempel: Virtuelle assistenter som Siri og Google Assistant bruger AI til at forstå og svare på stemmekommandoer, hvilket gør det lettere for brugere at interagere med deres enheder.

### That all sounds great right, so why do we need the AI Agent Framework?

AI-agentrammer repræsenterer mere end blot AI-rammer. De er designet til at muliggøre oprettelsen af intelligente agenter, der kan interagere med brugere, andre agenter og miljøet for at nå specifikke mål. Disse agenter kan udvise autonom adfærd, træffe beslutninger og tilpasse sig ændrede forhold. Lad os se på nogle nøglekapabiliteter, som AI-agentrammer muliggør:

- **Agent Collaboration and Coordination**: Muliggør oprettelse af flere AI-agenter, der kan arbejde sammen, kommunikere og koordinere for at løse komplekse opgaver.
- **Task Automation and Management**: Tilbyder mekanismer til automatisering af multi-trins arbejdsgange, opgavedelegering og dynamisk opgavestyring blandt agenter.
- **Contextual Understanding and Adaptation**: Udruster agenter med evnen til at forstå kontekst, tilpasse sig skiftende miljøer og træffe beslutninger baseret på realtidsinformation.

Så kort sagt, agenter giver dig mulighed for at gøre mere, tage automatisering til næste niveau og skabe mere intelligente systemer, der kan tilpasse sig og lære af deres omgivelser.

## Hvordan kan man hurtigt prototype, iterere og forbedre agentens evner?

Dette er et hurtigt udviklende område, men der er nogle ting, der er fælles på tværs af de fleste AI-agentrammer, som kan hjælpe dig med hurtigt at prototype og iterere, nemlig modulære komponenter, samarbejdsværktøjer og realtidslæring. Lad os dykke ned i disse:

- **Use Modular Components**: AI-SDK'er tilbyder færdigbyggede komponenter såsom AI- og hukommelsesforbindelser, funktionskald ved hjælp af naturligt sprog eller kodeplugins, promptskabeloner og mere.
- **Leverage Collaborative Tools**: Design agenter med specifikke roller og opgaver, så de kan teste og forfine samarbejdsarbejdsgange.
- **Learn in Real-Time**: Implementer feedback loops, hvor agenter lærer af interaktioner og justerer deres adfærd dynamisk.

### Brug modulære komponenter

SDK'er som Microsoft Agent Framework tilbyder færdigbyggede komponenter såsom AI-connectors, værktøjsdefinitioner og agentstyring.

**Hvordan teams kan bruge disse**: Teams kan hurtigt samle disse komponenter for at skabe en funktionel prototype uden at starte fra bunden, hvilket muliggør hurtig eksperimenteren og iteration.

**Hvordan det virker i praksis**: Du kan bruge en færdigbygget parser til at udtrække information fra brugerinput, en hukommelsesmodul til at gemme og hente data, og en promptgenerator til at interagere med brugere — alt sammen uden at skulle bygge disse komponenter fra bunden.

**Eksempelkode**. Lad os se på et eksempel på, hvordan du kan bruge Microsoft Agent Framework med `AzureAIProjectAgentProvider` for at få modellen til at svare på brugerinput med tool calling:

``` python
# Microsoft Agent Framework Python Eksempel

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# Definer en prøveværktøjsfunktion til at booke rejser
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
    # Eksempel output: Din flyrejse til New York den 1. januar 2025 er blevet booket succesfuldt. God rejse! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Hvad du kan se fra dette eksempel er, hvordan du kan udnytte en færdigbygget parser til at udtrække nøgleinformation fra brugerinput, såsom afgangssted, destination og dato for en flybookingsforespørgsel. Denne modulære tilgang giver dig mulighed for at fokusere på den overordnede logik.

### Udnyt samarbejdsværktøjer

Rammer som Microsoft Agent Framework faciliterer oprettelsen af flere agenter, der kan arbejde sammen.

**Hvordan teams kan bruge disse**: Teams kan designe agenter med specifikke roller og opgaver, så de kan teste og forfine samarbejdsarbejdsgange og forbedre den samlede systemeffektivitet.

**Hvordan det virker i praksis**: Du kan oprette et team af agenter, hvor hver agent har en specialiseret funktion, såsom dataindsamling, analyse eller beslutningstagning. Disse agenter kan kommunikere og dele information for at nå et fælles mål, såsom at besvare en brugerhenvendelse eller fuldføre en opgave.

**Eksempelkode (Microsoft Agent Framework)**:

```python
# Opretter flere agenter, der arbejder sammen ved hjælp af Microsoft Agent Framework

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Datahentningsagent
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

Hvad du ser i den tidligere kode er, hvordan du kan oprette en opgave, der involverer flere agenter, der arbejder sammen for at analysere data. Hver agent udfører en specifik funktion, og opgaven udføres ved at koordinere agenternes arbejde for at opnå det ønskede resultat. Ved at oprette dedikerede agenter med specialiserede roller kan du forbedre opgaveeffektivitet og ydeevne.

### Lær i realtid

Avancerede rammer tilbyder muligheder for realtidsforståelse af kontekst og tilpasning.

**Hvordan teams kan bruge disse**: Teams kan implementere feedbacksløjfer, hvor agenter lærer af interaktioner og justerer deres adfærd dynamisk, hvilket fører til kontinuerlig forbedring og forfining af kapabiliteter.

**Hvordan det virker i praksis**: Agenter kan analysere brugerfeedback, miljødata og opgaveudfald for at opdatere deres videnbase, justere beslutningsalgoritmer og forbedre ydeevnen over tid. Denne iterative læringsproces gør det muligt for agenter at tilpasse sig skiftende forhold og brugerpræferencer, hvilket øger systemets effektivitet.

## Hvad er forskellene mellem Microsoft Agent Framework og Azure AI Agent Service?

Der er mange måder at sammenligne disse tilgange på, men lad os se på nogle nøgleforskelle hvad angår design, kapabiliteter og målrettede brugsscenarier:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework tilbyder et strømlinet SDK til at bygge AI-agenter ved hjælp af `AzureAIProjectAgentProvider`. Det gør det muligt for udviklere at skabe agenter, der udnytter Azure OpenAI-modeller med indbygget værktøjskald, samtalestyring og virksomheds-grade sikkerhed gennem Azure-identitet.

**Brugsscenarier**: Bygning af produktionsklare AI-agenter med værktøjsbrug, flertrinsarbejdsgange og enterprise-integration.

Her er nogle vigtige kernekoncepter i Microsoft Agent Framework:

- **Agents**. En agent oprettes via `AzureAIProjectAgentProvider` og konfigureres med et navn, instruktioner og værktøjer. Agenten kan:
  - **Process user messages** og generere svar ved hjælp af Azure OpenAI-modeller.
  - **Call tools** automatisk baseret på samtalekonteksten.
  - **Maintain conversation state** på tværs af flere interaktioner.

  Her er en kodeeksempel, der viser, hvordan man opretter en agent:

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

- **Tools**. Rammen understøtter definition af værktøjer som Python-funktioner, som agenten kan kalde automatisk. Værktøjer registreres ved oprettelse af agenten:

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

- **Multi-Agent Coordination**. Du kan oprette flere agenter med forskellige specialiseringer og koordinere deres arbejde:

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

- **Azure Identity Integration**. Rammen bruger `AzureCliCredential` (eller `DefaultAzureCredential`) for sikker, nøglefri autentificering, hvilket eliminerer behovet for direkte at håndtere API-nøgler.

## Azure AI Agent Service

Azure AI Agent Service er en mere recent tilføjelse, introduceret ved Microsoft Ignite 2024. Den tillader udvikling og udrulning af AI-agenter med mere fleksible modeller, såsom direkte kald til open-source LLM'er som Llama 3, Mistral og Cohere.

Azure AI Agent Service tilbyder stærkere virksomhedssikkerhedsmekanismer og datalagringsmetoder, hvilket gør den velegnet til enterprise-applikationer. 

Den fungerer direkte sammen med Microsoft Agent Framework til at bygge og udrulle agenter.

Denne service er i Public Preview og understøtter Python og C# til opbygning af agenter.

Ved hjælp af Azure AI Agent Service Python SDK kan vi oprette en agent med et brugerdefineret værktøj:

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

- **Agent**. Azure AI Agent Service integrerer med Microsoft Foundry. Inden for AI Foundry fungerer en AI-agent som en "smart" mikrotjeneste, der kan bruges til at svare på spørgsmål (RAG), udføre handlinger eller fuldstændigt automatisere arbejdsgange. Det opnår dette ved at kombinere generative AI-modellers kraft med værktøjer, der giver den adgang til og mulighed for at interagere med virkelige datakilder. Her er et eksempel på en agent:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    I dette eksempel oprettes en agent med modellen `gpt-4o-mini`, et navn `my-agent`, og instruktionerne `You are helpful agent`. Agenten er udstyret med værktøjer og ressourcer til at udføre kodefortolkningsopgaver.

- **Thread and messages**. Tråden er et andet vigtigt koncept. Den repræsenterer en samtale eller interaktion mellem en agent og en bruger. Tråde kan bruges til at spore fremdriften i en samtale, gemme kontekstinformation og håndtere interaktionens tilstand. Her er et eksempel på en tråd:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Ask the agent to perform work on the thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Fetch and log all messages to see the agent's response
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    I den tidligere kode oprettes en tråd. Derefter sendes en besked til tråden. Ved at kalde `create_and_process_run` bliver agenten bedt om at udføre arbejde på tråden. Endelig hentes og logges beskederne for at se agentens svar. Beskederne angiver fremdriften i samtalen mellem brugeren og agenten. Det er også vigtigt at forstå, at beskederne kan være af forskellige typer såsom tekst, billede eller fil, det vil sige, at agenternes arbejde for eksempel har resulteret i et billede eller et tekstsvar. Som udvikler kan du derefter bruge disse oplysninger til yderligere at behandle svaret eller præsentere det for brugeren.

- **Integrates with the Microsoft Agent Framework**. Azure AI Agent Service fungerer problemfrit sammen med Microsoft Agent Framework, hvilket betyder, at du kan bygge agenter ved hjælp af `AzureAIProjectAgentProvider` og udrulle dem gennem Agent Service til produktionsscenarier.

**Brugsscenarier**: Azure AI Agent Service er designet til enterprise-applikationer, der kræver sikker, skalerbar og fleksibel udrulning af AI-agenter.

## Hvad er forskellen mellem disse tilgange?
 
Det kan lyde som om der er overlap, men der er nogle nøgleforskelle med hensyn til design, kapabiliteter og målrettede brugsscenarier:
 
- **Microsoft Agent Framework (MAF)**: Er et produktionsklart SDK til at bygge AI-agenter. Det tilbyder et strømlinet API til at skabe agenter med værktøjskald, samtalestyring og Azure-identitetsintegration.
- **Azure AI Agent Service**: Er en platform og udrulningstjeneste i Azure Foundry til agenter. Den tilbyder indbygget forbindelser til tjenester som Azure OpenAI, Azure AI Search, Bing Search og kodeeksekvering.
 
Er du stadig ikke sikker på, hvilken du skal vælge?

### Brugsscenarier
 
Lad os se, om vi kan hjælpe dig ved at gennemgå nogle almindelige brugsscenarier:
 
> Q: I'm building production AI agent applications and want to get started quickly
>
>A: Microsoft Agent Framework er et fremragende valg. Det giver et simpelt, Python-venligt API via `AzureAIProjectAgentProvider`, der lader dig definere agenter med værktøjer og instruktioner på kun få linjer kode.

>Q: I need enterprise-grade deployment with Azure integrations like Search and code execution
>
> A: Azure AI Agent Service er det bedste valg. Det er en platformtjeneste, der tilbyder indbyggede kapabiliteter for flere modeller, Azure AI Search, Bing Search og Azure Functions. Det gør det nemt at bygge dine agenter i Foundry-portalen og udrulle dem i stor skala.
 
> Q: I'm still confused, just give me one option
>
> A: Start med Microsoft Agent Framework for at bygge dine agenter, og brug derefter Azure AI Agent Service, når du har brug for at udrulle og skalere dem i produktion. Denne tilgang lader dig iterere hurtigt på din agentlogik, samtidig med at du har en klar vej til enterprise-udrulning.
 
Lad os opsummere de vigtigste forskelle i en tabel:

| Framework | Fokus | Kernekoncepter | Anvendelsestilfælde |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Strømlinet agent-SDK med værktøjskald | Agenter, Værktøjer, Azure-identitet | Opbygning af AI-agenter, værktøjsbrug, flertrinsarbejdsgange |
| Azure AI Agent Service | Fleksible modeller, virksomhedssikkerhed, kodegenerering, værktøjskald | Modularitet, Samarbejde, Procesorkestrering | Sikker, skalerbar og fleksibel udrulning af AI-agenter |

## Kan jeg integrere mine eksisterende Azure-økosystemværktøjer direkte, eller har jeg brug for selvstændige løsninger?
Svaret er ja, du kan integrere dine eksisterende Azure-økosystemværktøjer direkte med Azure AI Agent Service, især da den er bygget til at arbejde problemfrit sammen med andre Azure-tjenester. Du kan for eksempel integrere Bing, Azure AI Search og Azure Functions. Der er også dyb integration med Microsoft Foundry.

Microsoft Agent Framework integreres også med Azure-tjenester gennem `AzureAIProjectAgentProvider` og Azure-identitet, hvilket lader dig kalde Azure-tjenester direkte fra dine agentværktøjer.

## Eksempelkoder

- Python: [Agent-rammeværk](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent-rammeværk](./code_samples/02-dotnet-agent-framework.md)

## Har du flere spørgsmål om AI-agentframeworks?

Deltag i [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) for at møde andre lærende, deltage i kontortimer og få svar på dine spørgsmål om AI-agenter.

## Referencer

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent-tjeneste</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI-svar</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent-tjeneste</a>

## Forrige lektion

[Introduktion til AI-agenter og agentbrugstilfælde](../01-intro-to-ai-agents/README.md)

## Næste lektion

[Forstå agentiske designmønstre](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi stræber efter nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på originalsproget bør betragtes som den autoritative kilde. For kritiske oplysninger anbefales en professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->