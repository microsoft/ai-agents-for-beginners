[![AI-agentkaders verkennen](../../../translated_images/nl/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Klik op de afbeelding hierboven om de video van deze les te bekijken)_

# Verken AI-agentkaders

AI-agentkaders zijn softwareplatforms die zijn ontworpen om het maken, inzetten en beheren van AI-agents te vereenvoudigen. Deze kaders bieden ontwikkelaars vooraf gebouwde componenten, abstracties en hulpmiddelen die de ontwikkeling van complexe AI-systemen stroomlijnen.

Deze kaders helpen ontwikkelaars zich te concentreren op de unieke aspecten van hun toepassingen door gestandaardiseerde benaderingen te bieden voor veelvoorkomende uitdagingen in de ontwikkeling van AI-agents. Ze verhogen schaalbaarheid, toegankelijkheid en efficiëntie bij het bouwen van AI-systemen.

## Inleiding 

Deze les behandelt:

- Wat zijn AI-agentkaders en wat kunnen ontwikkelaars ermee bereiken?
- Hoe kunnen teams deze gebruiken om snel te prototypen, itereren en de mogelijkheden van hun agent te verbeteren?
- Wat zijn de verschillen tussen de kaders en tools die door Microsoft zijn gemaakt (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> en het <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Kan ik mijn bestaande Azure-ecosysteemtools rechtstreeks integreren, of heb ik zelfstandige oplossingen nodig?
- Wat is de Azure AI Agents-service en hoe helpt dit mij?

## Leerdoelen

De doelen van deze les zijn om je te helpen begrijpen:

- De rol van AI-agentkaders in AI-ontwikkeling.
- Hoe je AI-agentkaders kunt benutten om intelligente agents te bouwen.
- Belangrijke mogelijkheden die AI-agentkaders mogelijk maken.
- De verschillen tussen het Microsoft Agent Framework en de Azure AI Agent Service.

## Wat zijn AI-agentkaders en wat stellen ze ontwikkelaars in staat te doen?

Traditionele AI-kaders kunnen je helpen AI in je apps te integreren en deze apps op de volgende manieren te verbeteren:

- **Personalisatie**: AI kan gebruikersgedrag en voorkeuren analyseren om gepersonaliseerde aanbevelingen, inhoud en ervaringen te bieden.
Voorbeeld: Streamingdiensten zoals Netflix gebruiken AI om films en series aan te bevelen op basis van kijkgeschiedenis, wat de betrokkenheid en tevredenheid van gebruikers vergroot.
- **Automatisering en efficiëntie**: AI kan repetitieve taken automatiseren, workflows stroomlijnen en operationele efficiëntie verbeteren.
Voorbeeld: Klantenservice-apps gebruiken AI-gestuurde chatbots om veelvoorkomende vragen af te handelen, waardoor reactietijden worden verkort en menselijke medewerkers vrijkomen voor complexere kwesties.
- **Verbeterde gebruikerservaring**: AI kan de algehele gebruikerservaring verbeteren door intelligente functies te bieden zoals spraakherkenning, natuurlijke taalverwerking en voorspellende tekst.
Voorbeeld: Virtuele assistenten zoals Siri en Google Assistant gebruiken AI om spraakopdrachten te begrijpen en te beantwoorden, waardoor het voor gebruikers eenvoudiger wordt om met hun apparaten te communiceren.

### Dat klinkt allemaal goed, maar waarom hebben we het AI Agent Framework nodig?

AI-agentkaders vertegenwoordigen meer dan alleen AI-kaders. Ze zijn ontworpen om het creëren van intelligente agents mogelijk te maken die kunnen communiceren met gebruikers, andere agents en de omgeving om specifieke doelen te bereiken. Deze agents kunnen autonoom gedrag vertonen, beslissingen nemen en zich aanpassen aan veranderende omstandigheden. Laten we naar enkele belangrijke mogelijkheden kijken die AI-agentkaders mogelijk maken:

- **Samenwerking en coördinatie tussen agents**: Maakt het mogelijk meerdere AI-agents te creëren die samen kunnen werken, communiceren en coördineren om complexe taken op te lossen.
- **Taakautomatisering en -beheer**: Biedt mechanismen voor het automatiseren van meerstappige workflows, taaktoewijzing en dynamisch taakbeheer tussen agents.
- **Contextueel begrip en aanpassing**: Voorziet agents van het vermogen om context te begrijpen, zich aan te passen aan veranderende omgevingen en beslissingen te nemen op basis van realtime informatie.

Samengevat stellen agents je in staat meer te doen, automatisering naar een hoger niveau te tillen en meer intelligente systemen te creëren die zich kunnen aanpassen en leren van hun omgeving.

## Hoe snel prototypen, itereren en de mogelijkheden van de agent verbeteren?

Dit is een snel veranderend landschap, maar er zijn enkele gemeenschappelijke elementen in de meeste AI-agentkaders die je kunnen helpen snel te prototypen en te itereren, namelijk modulecomponenten, samenwerkingshulpmiddelen en realtime leren. Laten we hierop ingaan:

- **Gebruik modulaire componenten**: AI-SDK's bieden vooraf gebouwde componenten zoals AI- en geheugenconnectoren, functie-aanroepen via natuurlijke taal of code-plugins, promptsjablonen en meer.
- **Benut samenwerkingshulpmiddelen**: Ontwerp agents met specifieke rollen en taken, zodat ze samenwerkingsworkflows kunnen testen en verfijnen.
- **Leer in realtime**: Implementeer feedbackloops waarin agents leren van interacties en hun gedrag dynamisch aanpassen.

### Gebruik modulaire componenten

SDK's zoals het Microsoft Agent Framework bieden vooraf gebouwde componenten zoals AI-connectoren, tooldefinities en agentbeheer.

**Hoe teams deze kunnen gebruiken**: Teams kunnen deze componenten snel samenstellen om een functioneel prototype te maken zonder vanaf nul te hoeven beginnen, wat snelle experimenten en iteratie mogelijk maakt.

**Hoe dit in de praktijk werkt**: Je kunt een vooraf gebouwde parser gebruiken om informatie uit gebruikersinvoer te halen, een geheugenmodule om gegevens op te slaan en op te halen, en een promptgenerator om met gebruikers te communiceren, allemaal zonder deze componenten zelf te hoeven bouwen.

**Voorbeeldcode**. Laten we kijken naar een voorbeeld van hoe je het Microsoft Agent Framework kunt gebruiken met `AzureAIProjectAgentProvider` zodat het model reageert op gebruikersinvoer met toolaanroepen:

``` python
# Microsoft Agent Framework Python Voorbeeld

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# Definieer een voorbeeldfunctie voor een hulpmiddel om reizen te boeken
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
    # Voorbeelduitvoer: Uw vlucht naar New York op 1 januari 2025 is succesvol geboekt. Goede reis! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Wat je in dit voorbeeld kunt zien is hoe je een vooraf gebouwde parser kunt gebruiken om sleutelgegevens uit gebruikersinvoer te halen, zoals de vertrekplaats, bestemming en datum van een vluchtboekingsverzoek. Deze modulaire aanpak stelt je in staat je te richten op de logica op hoog niveau.

### Benut samenwerkingshulpmiddelen

Kaders zoals het Microsoft Agent Framework vergemakkelijken het creëren van meerdere agents die samen kunnen werken.

**Hoe teams deze kunnen gebruiken**: Teams kunnen agents ontwerpen met specifieke rollen en taken, waardoor ze samenwerkingsworkflows kunnen testen en verfijnen en de algehele systeemefficiëntie kunnen verbeteren.

**Hoe dit in de praktijk werkt**: Je kunt een team van agents creëren waarbij elke agent een gespecialiseerde functie heeft, zoals gegevensopvraging, analyse of besluitvorming. Deze agents kunnen communiceren en informatie delen om een gemeenschappelijk doel te bereiken, zoals het beantwoorden van een gebruikersvraag of het voltooien van een taak.

**Voorbeeldcode (Microsoft Agent Framework)**:

```python
# Meerdere agenten creëren die samenwerken met behulp van het Microsoft Agent Framework

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Gegevensophaalagent
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Gegevensanalyseagent
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Agenten achtereenvolgens uitvoeren voor een taak
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Wat je in de vorige code ziet, is hoe je een taak kunt creëren waarbij meerdere agents samenwerken om gegevens te analyseren. Elke agent voert een specifieke functie uit en de taak wordt uitgevoerd door de agents te coördineren om het gewenste resultaat te bereiken. Door toegewijde agents met gespecialiseerde rollen te maken, kun je de efficiëntie en prestaties van taken verbeteren.

### Leer in realtime

Geavanceerde kaders bieden mogelijkheden voor realtime contextbegrip en aanpassing.

**Hoe teams deze kunnen gebruiken**: Teams kunnen feedbackloops implementeren waarbij agents leren van interacties en hun gedrag dynamisch aanpassen, wat leidt tot continue verbetering en verfijning van mogelijkheden.

**Hoe dit in de praktijk werkt**: Agents kunnen gebruikersfeedback, omgevingsgegevens en taakresultaten analyseren om hun kennisbasis bij te werken, besluitvormingsalgoritmen aan te passen en de prestaties in de loop van de tijd te verbeteren. Dit iteratieve leerproces stelt agents in staat zich aan te passen aan veranderende omstandigheden en gebruikersvoorkeuren, wat de algehele effectiviteit van het systeem verhoogt.

## Wat zijn de verschillen tussen het Microsoft Agent Framework en Azure AI Agent Service?

Er zijn veel manieren om deze benaderingen te vergelijken, maar laten we naar enkele belangrijke verschillen kijken op het gebied van ontwerp, mogelijkheden en beoogde use-cases:

## Microsoft Agent Framework (MAF)

Het Microsoft Agent Framework biedt een gestroomlijnde SDK voor het bouwen van AI-agents met `AzureAIProjectAgentProvider`. Het stelt ontwikkelaars in staat agents te maken die Azure OpenAI-modellen gebruiken met ingebouwde toolaanroepen, gesprekbeheer en enterprise-grade beveiliging via Azure-identiteit.

**Use Cases**: Het bouwen van productieklare AI-agents met toolgebruik, meerstappige workflows en enterprise-integratiescenario's.

Hier zijn enkele belangrijke kernconcepten van het Microsoft Agent Framework:

- **Agents**. Een agent wordt gemaakt via `AzureAIProjectAgentProvider` en geconfigureerd met een naam, instructies en tools. De agent kan:
  - **Gebruikersberichten verwerken** en reacties genereren met behulp van Azure OpenAI-modellen.
  - **Tools aanroepen** op basis van de context van het gesprek.
  - **Gespreksstatus bijhouden** over meerdere interacties.

  Hier is een codefragment dat laat zien hoe je een agent maakt:

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

- **Tools**. Het framework ondersteunt het definiëren van tools als Python-functies die de agent automatisch kan aanroepen. Tools worden geregistreerd bij het creëren van de agent:

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

- **Coördinatie van meerdere agents**. Je kunt meerdere agents maken met verschillende specialisaties en hun werk coördineren:

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

- **Integratie met Azure-identiteit**. Het framework gebruikt `AzureCliCredential` (of `DefaultAzureCredential`) voor veilige, sleutelvrije authenticatie, waardoor het beheer van API-sleutels overbodig wordt.

## Azure AI Agent Service

Azure AI Agent Service is een meer recente toevoeging, geïntroduceerd tijdens Microsoft Ignite 2024. Het maakt de ontwikkeling en uitrol van AI-agents met flexibelere modellen mogelijk, zoals directe aanroepen naar open-source LLM's zoals Llama 3, Mistral en Cohere.

Azure AI Agent Service biedt sterkere enterprise-beveiligingsmechanismen en methoden voor gegevensopslag, waardoor het geschikt is voor enterprise-toepassingen.

Het werkt direct samen met het Microsoft Agent Framework voor het bouwen en uitrollen van agents.

Deze service bevindt zich momenteel in Public Preview en ondersteunt Python en C# voor het bouwen van agents.

Met de Azure AI Agent Service Python SDK kunnen we een agent maken met een door de gebruiker gedefinieerde tool:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Definieer functietools
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

### Kernconcepten

Azure AI Agent Service heeft de volgende kernconcepten:

- **Agent**. Azure AI Agent Service integreert met Microsoft Foundry. Binnen AI Foundry fungeert een AI Agent als een "slimme" microservice die kan worden gebruikt om vragen te beantwoorden (RAG), acties uit te voeren of workflows volledig te automatiseren. Dit bereikt het door de kracht van generatieve AI-modellen te combineren met tools die het agent in staat stellen toegang te krijgen tot en te interacteren met echte gegevensbronnen. Hier is een voorbeeld van een agent:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    In dit voorbeeld wordt een agent gemaakt met het model `gpt-4o-mini`, een naam `my-agent`, en instructies `You are helpful agent`. De agent is uitgerust met tools en bronnen om taken voor code-interpretatie uit te voeren.

- **Thread en berichten**. De thread is een ander belangrijk concept. Het vertegenwoordigt een gesprek of interactie tussen een agent en een gebruiker. Threads kunnen worden gebruikt om de voortgang van een gesprek bij te houden, contextinformatie op te slaan en de status van de interactie te beheren. Hier is een voorbeeld van een thread:

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

    In de vorige code wordt een thread aangemaakt. Daarna wordt een bericht naar de thread verzonden. Door `create_and_process_run` aan te roepen, wordt de agent gevraagd om werk op de thread uit te voeren. Ten slotte worden de berichten opgehaald en gelogd om de reactie van de agent te zien. De berichten geven de voortgang van het gesprek tussen de gebruiker en de agent weer. Het is ook belangrijk te begrijpen dat de berichten verschillende typen kunnen hebben, zoals tekst, afbeelding of bestand; dat wil zeggen dat het werk van de agents bijvoorbeeld heeft geresulteerd in een afbeelding of een tekstuele respons. Als ontwikkelaar kun je deze informatie vervolgens gebruiken om de respons verder te verwerken of aan de gebruiker te presenteren.

- **Integreert met het Microsoft Agent Framework**. Azure AI Agent Service werkt naadloos samen met het Microsoft Agent Framework, wat betekent dat je agents kunt bouwen met `AzureAIProjectAgentProvider` en ze via de Agent Service kunt uitrollen voor productieomgevingen.

**Use Cases**: Azure AI Agent Service is ontworpen voor enterprise-toepassingen die veilige, schaalbare en flexibele uitrol van AI-agents vereisen.

## Wat is het verschil tussen deze benaderingen?
 
Het lijkt misschien alsof er overlap is, maar er zijn enkele belangrijke verschillen in ontwerp, mogelijkheden en beoogde use-cases:
 
- **Microsoft Agent Framework (MAF)**: Is een productieklare SDK voor het bouwen van AI-agents. Het biedt een gestroomlijnde API voor het creëren van agents met toolaanroepen, gesprekbeheer en integratie met Azure-identiteit.
- **Azure AI Agent Service**: Is een platform- en uitrolservice in Azure Foundry voor agents. Het biedt ingebouwde connectiviteit met services zoals Azure OpenAI, Azure AI Search, Bing Search en code-executie.
 
Nog steeds niet zeker welke je moet kiezen?

### Use Cases
 
Laten we kijken of we je kunnen helpen door enkele veelvoorkomende use-cases door te nemen:
 
> Q: Ik bouw productieklare AI-agenttoepassingen en wil snel aan de slag
>

> A: Het Microsoft Agent Framework is een uitstekende keuze. Het biedt een eenvoudige, Python-achtige API via `AzureAIProjectAgentProvider` waarmee je agents met tools en instructies in slechts een paar regels code kunt definiëren.

>Q: Ik heb enterprise-grade uitrol nodig met Azure-integraties zoals Search en code-executie
>
> A: Azure AI Agent Service is de beste keuze. Het is een platformservice die ingebouwde mogelijkheden biedt voor meerdere modellen, Azure AI Search, Bing Search en Azure Functions. Het maakt het eenvoudig om je agents in de Foundry Portal te bouwen en op schaal uit te rollen.
 
> Q: Ik ben nog steeds in de war, geef me gewoon één optie
>
> A: Begin met het Microsoft Agent Framework om je agents te bouwen en gebruik vervolgens Azure AI Agent Service wanneer je ze in productie moet uitrollen en schalen. Deze aanpak stelt je in staat snel te itereren op je agentlogica terwijl je een duidelijk pad naar enterprise-uitrol behoudt.
 
Laten we de belangrijkste verschillen samenvatten in een tabel:

| Framework | Focus | Kernconcepten | Use Cases |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Gestroomlijnde agent-SDK met toolaanroepen | Agents, Tools, Azure Identity | Bouwen van AI-agents, toolgebruik, meerstappige workflows |
| Azure AI Agent Service | Flexibele modellen, enterprise-beveiliging, codegeneratie, toolaanroepen | Modulariteit, Samenwerking, Procesorkestratie | Veilige, schaalbare en flexibele uitrol van AI-agents |

## Kan ik mijn bestaande Azure-ecosysteemtools direct integreren, of heb ik zelfstandige oplossingen nodig?
Het antwoord is ja: je kunt je bestaande Azure-ecosysteemtools rechtstreeks integreren met Azure AI Agent Service, vooral omdat het is gebouwd om naadloos samen te werken met andere Azure-diensten. Je kunt bijvoorbeeld Bing, Azure AI Search en Azure Functions integreren. Er is ook diepe integratie met Microsoft Foundry.

Het Microsoft Agent Framework integreert ook met Azure-diensten via `AzureAIProjectAgentProvider` en Azure identity, waardoor je Azure-diensten rechtstreeks vanuit je agenttools kunt aanroepen.

## Voorbeeldcodes

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Nog meer vragen over AI Agent Frameworks?

Sluit je aan bij de [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) om andere deelnemers te ontmoeten, spreekuren bij te wonen en antwoorden op je vragen over AI Agents te krijgen.

## Referenties

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>

## Vorige les

[Introductie tot AI-agenten en gebruiksscenario's](../01-intro-to-ai-agents/README.md)

## Volgende les

[Agentische ontwerppatronen begrijpen](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vrijwaring**:
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we naar nauwkeurigheid streven, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor kritieke informatie wordt een professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor enige misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->