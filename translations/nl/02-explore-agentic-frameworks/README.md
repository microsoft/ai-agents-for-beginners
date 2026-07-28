[![Verkenning van AI Agent Frameworks](../../../translated_images/nl/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Klik op de afbeelding hierboven om de video van deze les te bekijken)_

# Verken AI Agent Frameworks

AI agent frameworks zijn softwareplatforms die zijn ontworpen om het creëren, implementeren en beheren van AI-agenten te vereenvoudigen. Deze frameworks bieden ontwikkelaars kant-en-klare componenten, abstracties en hulpmiddelen die de ontwikkeling van complexe AI-systemen stroomlijnen.

Deze frameworks helpen ontwikkelaars zich te concentreren op de unieke aspecten van hun toepassingen door gestandaardiseerde benaderingen te bieden voor veelvoorkomende uitdagingen bij de ontwikkeling van AI-agenten. Ze verbeteren schaalbaarheid, toegankelijkheid en efficiëntie bij het bouwen van AI-systemen.

## Introductie 

Deze les behandelt:

- Wat zijn AI Agent Frameworks en wat stellen ze ontwikkelaars in staat te bereiken?
- Hoe kunnen teams deze gebruiken om snel prototypes te maken, te itereren en de mogelijkheden van hun agent te verbeteren?
- Wat zijn de verschillen tussen de frameworks en tools ontwikkeld door Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> en het <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Kan ik mijn bestaande Azure-ecosysteemtools direct integreren, of heb ik zelfstandige oplossingen nodig?
- Wat is Microsoft Foundry Agent Service en hoe helpt dit mij?

## Leerdoelen

De doelen van deze les zijn je te helpen begrijpen:

- De rol van AI Agent Frameworks in AI-ontwikkeling.
- Hoe AI Agent Frameworks te benutten om intelligente agenten te bouwen.
- Belangrijke mogelijkheden die AI Agent Frameworks bieden.
- De verschillen tussen het Microsoft Agent Framework en Microsoft Foundry Agent Service.

## Wat zijn AI Agent Frameworks en wat stellen ze ontwikkelaars in staat te doen?

Traditionele AI-frameworks kunnen je helpen AI in je apps te integreren en deze apps op de volgende manieren te verbeteren:

- **Personalisatie**: AI kan gebruikersgedrag en voorkeuren analyseren om gepersonaliseerde aanbevelingen, inhoud en ervaringen te bieden.
Voorbeeld: Streamingdiensten zoals Netflix gebruiken AI om films en shows voor te stellen op basis van kijkgeschiedenis, wat de betrokkenheid en tevredenheid van gebruikers verhoogt.
- **Automatisering en efficiëntie**: AI kan repetitieve taken automatiseren, workflows stroomlijnen en operationele efficiëntie verbeteren.
Voorbeeld: Klantenservice-apps gebruiken AI-gestuurde chatbots om veelvoorkomende vragen af te handelen, waardoor responstijden worden verkort en menselijke agenten beschikbaar blijven voor complexere problemen.
- **Verbeterde gebruikerservaring**: AI kan de algehele gebruikerservaring verbeteren door intelligente functies te bieden zoals spraakherkenning, natuurlijke taalverwerking en voorspellende tekst.
Voorbeeld: Virtuele assistenten zoals Siri en Google Assistant gebruiken AI om spraakopdrachten te begrijpen en erop te reageren, wat gebruikers helpt gemakkelijker met hun apparaten te communiceren.

### Dat klinkt allemaal geweldig, waarom hebben we dan het AI Agent Framework nodig?

AI Agent frameworks zijn meer dan alleen AI-frameworks. Ze zijn ontworpen om de creatie van intelligente agenten mogelijk te maken die kunnen interacteren met gebruikers, andere agenten en de omgeving om specifieke doelen te bereiken. Deze agenten kunnen autonoom gedrag vertonen, beslissingen nemen en zich aanpassen aan veranderende omstandigheden. Laten we enkele belangrijke mogelijkheden bekijken die AI Agent Frameworks bieden:

- **Samenwerking en coördinatie tussen agenten**: Maakt de creatie van meerdere AI-agenten mogelijk die samen kunnen werken, communiceren en coördineren om complexe taken op te lossen.
- **Automatisering en management van taken**: Biedt mechanismen om multi-stap workflows te automatiseren, taken te delegeren en dynamisch taakbeheer tussen agenten mogelijk te maken.
- **Contextueel begrip en aanpassing**: Voorziet agenten van het vermogen om context te begrijpen, zich aan te passen aan veranderende omgevingen en beslissingen te nemen op basis van real-time informatie.

Samengevat stellen agenten je in staat meer te doen, automatisering naar een hoger niveau te tillen, en meer intelligente systemen te creëren die zich kunnen aanpassen en leren van hun omgeving.

## Hoe snel een prototype maken, itereren, en de mogelijkheden van de agent verbeteren?

Dit is een snel veranderend landschap, maar er zijn enkele gemeenschappelijke elementen in de meeste AI Agent Frameworks die je helpen snel te prototypen en te itereren, namelijk modulecomponenten, samenwerkingshulpmiddelen en real-time leren. Laten we deze nader bekijken:

- **Gebruik Modulaire Componenten**: AI SDK's bieden kant-en-klare componenten zoals AI- en geheugenkoppelingen, functienaamroepen via natuurlijke taal of codeplugins, promptsjablonen en meer.
- **Benut Samenwerkingshulpmiddelen**: Ontwerp agenten met specifieke rollen en taken zodat ze samenwerkingsworkflows kunnen testen en verfijnen.
- **Leer in Real-Time**: Implementeer feedbackloops waarin agenten leren van interacties en hun gedrag dynamisch aanpassen.

### Gebruik Modulaire Componenten

SDK's zoals het Microsoft Agent Framework bieden kant-en-klare componenten zoals AI-koppelingen, tooldefinities en agentbeheer.

**Hoe teams deze kunnen gebruiken**: Teams kunnen deze componenten snel samenstellen om een functioneel prototype te creëren zonder vanaf nul te beginnen, wat snelle experimentatie en iteratie mogelijk maakt.

**Hoe het in de praktijk werkt**: Je kunt een kant-en-klare parser gebruiken om informatie uit gebruikersinvoer te halen, een geheugenmodule om gegevens op te slaan en op te halen en een promptgenerator om met gebruikers te communiceren, allemaal zonder deze componenten zelf te hoeven bouwen.

**Voorbeeldcode**. Laten we een voorbeeld bekijken van het gebruik van het Microsoft Agent Framework met `FoundryChatClient` om het model te laten reageren op gebruikersinvoer met toolaanroepen:

``` python
# Microsoft Agent Framework Python Voorbeeld

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Definieer een voorbeeldtoolfunctie om reizen te boeken
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
    # Voorbeelduitvoer: Uw vlucht naar New York op 1 januari 2025 is succesvol geboekt. Goede reis! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Wat je in dit voorbeeld ziet, is hoe je een kant-en-klare parser kunt gebruiken om sleutelgegevens uit gebruikersinvoer te extraheren, zoals de oorsprong, bestemming en datum van een vluchtaanvraag. Deze modulaire benadering stelt je in staat je te richten op de hoofdlijnen van de logica.

### Benut Samenwerkingshulpmiddelen

Frameworks zoals het Microsoft Agent Framework maken het mogelijk om meerdere agenten te creëren die samenwerken.

**Hoe teams deze kunnen gebruiken**: Teams kunnen agenten ontwerpen met specifieke rollen en taken, waardoor ze samenwerkingsworkflows kunnen testen en verfijnen en de algehele systeemefficiëntie verbeteren.

**Hoe het in de praktijk werkt**: Je kunt een team van agenten creëren waarbij elke agent een gespecialiseerde functie heeft, zoals gegevensophaling, analyse of besluitvorming. Deze agenten communiceren en delen informatie om een gemeenschappelijk doel te bereiken, zoals het beantwoorden van een gebruikersvraag of het voltooien van een taak.

**Voorbeeldcode (Microsoft Agent Framework)**:

```python
# Meerdere agenten maken die samenwerken met het Microsoft Agent Framework

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Gegevensopvraagagent
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Gegevensanalyse-agent
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Agenten achtereenvolgens op een taak uitvoeren
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Wat je in de vorige code ziet, is hoe je een taak kunt creëren die meerdere agenten samen laat werken om gegevens te analyseren. Elke agent voert een specifieke functie uit, en de taak wordt uitgevoerd door de agenten te coördineren om het gewenste resultaat te bereiken. Door toegewijde agenten met gespecialiseerde rollen te creëren, kun je de efficiëntie en prestaties van taken verbeteren.

### Leer in Real-Time

Geavanceerde frameworks bieden mogelijkheden voor real-time contextbegrip en aanpassing.

**Hoe teams deze kunnen gebruiken**: Teams kunnen feedbackloops implementeren waarbij agenten leren van interacties en hun gedrag dynamisch aanpassen, wat leidt tot continue verbetering en verfijning van mogelijkheden.

**Hoe het in de praktijk werkt**: Agenten kunnen gebruikersfeedback, omgevingsdata en taakresultaten analyseren om hun kennisbasis bij te werken, besluitvormingsalgoritmen aan te passen en prestaties na verloop van tijd te verbeteren. Dit iteratieve leerproces stelt agenten in staat zich aan te passen aan veranderende omstandigheden en gebruikersvoorkeuren, waardoor de algehele systeemeffectiviteit wordt verbeterd.

## Wat zijn de verschillen tussen het Microsoft Agent Framework en Microsoft Foundry Agent Service?

Er zijn vele manieren om deze benaderingen te vergelijken, maar laten we enkele belangrijke verschillen bekijken qua ontwerp, mogelijkheden en doelgebruik:

## Microsoft Agent Framework (MAF)

Het Microsoft Agent Framework biedt een gestroomlijnde SDK voor het bouwen van AI-agenten met `FoundryChatClient`. Het stelt ontwikkelaars in staat agenten te creëren die Azure OpenAI-modellen gebruiken met ingebouwde tool-aanroepen, gesprekbeheer en bedrijfsbeveiliging via Azure-identiteit.

**Gebruiksscenario's**: Productieklaar bouwen van AI-agenten met toolgebruik, multi-stap workflows en scenario's voor integratie met ondernemingen.

Hier zijn enkele belangrijke kernconcepten van het Microsoft Agent Framework:

- **Agenten**. Een agent wordt aangemaakt via `FoundryChatClient` en geconfigureerd met een naam, instructies en tools. De agent kan:
  - **Gebruikersberichten verwerken** en antwoorden genereren met Azure OpenAI-modellen.
  - **Tools aanroepen** automatisch op basis van de gesprekscontext.
  - **Gespreksstatus bijhouden** over meerdere interacties.

  Hier is een codevoorbeeld dat laat zien hoe je een agent creëert:

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

- **Tools**. Het framework ondersteunt het definiëren van tools als Python-functies die de agent automatisch kan aanroepen. Tools worden geregistreerd tijdens het aanmaken van de agent:

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

- **Coördinatie tussen meerdere agenten**. Je kunt meerdere agenten met verschillende specialisaties creëren en hun werk coördineren:

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

- **Integratie van Azure Identity**. Het framework gebruikt `AzureCliCredential` (of `DefaultAzureCredential`) voor veilige, keyless authenticatie, waardoor het beheer van API-sleutels niet nodig is.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service is een recentere toevoeging, geïntroduceerd op Microsoft Ignite 2024. Het maakt ontwikkeling en implementatie van AI-agenten mogelijk met flexibelere modellen, zoals het direct aanroepen van open-source LLM's zoals Llama 3, Mistral en Cohere.

Microsoft Foundry Agent Service biedt sterkere beveiligingsmechanismen voor ondernemingen en dat opslagmethoden, wat het geschikt maakt voor bedrijfsapplicaties.

Het werkt direct samen met het Microsoft Agent Framework voor het bouwen en implementeren van agenten.

Deze service bevindt zich momenteel in Public Preview en ondersteunt Python en C# voor het bouwen van agenten.

Met de Microsoft Foundry Agent Service Python SDK kunnen we een agent creëren met een door de gebruiker gedefinieerde tool:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Definieer hulpmiddel functies
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

### Kernconcepten

Microsoft Foundry Agent Service heeft de volgende kernconcepten:

- **Agent**. Microsoft Foundry Agent Service is geïntegreerd met Microsoft Foundry. Binnen Microsoft Foundry fungeert een AI Agent als een "slimme" microservice die gebruikt kan worden om vragen te beantwoorden (RAG), handelingen uit te voeren of workflows volledig te automatiseren. Dit bereikt het door de kracht van generatieve AI-modellen te combineren met tools die toegang geven tot en interactie mogelijk maken met real-world data bronnen. Hier is een voorbeeld van een agent:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    In dit voorbeeld wordt een agent aangemaakt met het model `gpt-5-mini`, de naam `my-agent`, en de instructies `You are helpful agent`. De agent is uitgerust met tools en bronnen om taken voor code-interpretatie uit te voeren.

- **Thread en berichten**. De thread is een ander belangrijk concept. Het vertegenwoordigt een gesprek of interactie tussen een agent en een gebruiker. Threads kunnen worden gebruikt om de voortgang van een gesprek te volgen, contextinformatie op te slaan en de staat van de interactie te beheren. Hier is een voorbeeld van een thread:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Vraag de agent om werk uit te voeren op de draad
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Haal alle berichten op en log ze om de reactie van de agent te zien
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    In de voorgaande code wordt een thread aangemaakt. Daarna wordt een bericht naar de thread gestuurd. Door `create_and_process_run` aan te roepen, wordt de agent gevraagd werk uit te voeren op de thread. Ten slotte worden de berichten opgehaald en gelogd om de reactie van de agent te zien. De berichten geven de voortgang van het gesprek tussen gebruiker en agent aan. Het is ook belangrijk om te begrijpen dat berichten van verschillende typen kunnen zijn, zoals tekst, afbeelding of bestand. Dat betekent dat het werk van de agent bijvoorbeeld heeft geleid tot een afbeelding of een tekstuele reactie. Als ontwikkelaar kun je deze informatie gebruiken om de reactie verder te verwerken of aan de gebruiker te presenteren.

- **Integratie met het Microsoft Agent Framework**. Microsoft Foundry Agent Service werkt naadloos samen met het Microsoft Agent Framework, wat betekent dat je agenten kunt bouwen met `FoundryChatClient` en deze via de Agent Service kunt implementeren voor productieomgevingen.

**Gebruiksscenario's**: Microsoft Foundry Agent Service is ontworpen voor bedrijfsapplicaties waarbij veilige, schaalbare en flexibele AI-agentimplementatie vereist is.

## Wat is het verschil tussen deze benaderingen?
 
Het lijkt misschien dat er overlap is, maar er zijn enkele belangrijke verschillen in ontwerp, mogelijkheden en doelgebruik:
 
- **Microsoft Agent Framework (MAF)**: Is een productieklare SDK voor het bouwen van AI-agenten. Het biedt een gestroomlijnde API voor het creëren van agenten met tool-aanroep, gesprekbeheer en integratie van Azure-identiteit.
- **Microsoft Foundry Agent Service**: Is een platform- en implementatieservice in Microsoft Foundry voor agenten. Het biedt ingebouwde connectiviteit met diensten zoals Azure OpenAI, Azure AI Search, Bing Search en code-executie.
 
Weet je nog steeds niet welke je moet kiezen?

### Gebruiksscenario's
 
Laten we eens kijken of we je kunnen helpen met enkele veelvoorkomende gebruikssituaties:
 
> V: Ik bouw productieklare AI-agentapplicaties en wil snel aan de slag
>

>A: Het Microsoft Agent Framework is een goede keuze. Het biedt een eenvoudige, Python-achtige API via `FoundryChatClient` waarmee je agenten met tools en instructies in slechts enkele regels code kunt definiëren.

>V: Ik heb implementatie op ondernemingsniveau nodig met Azure-integraties zoals Search en code-executie
>
> A: Microsoft Foundry Agent Service is de beste optie. Het is een platformdienst die ingebouwde mogelijkheden biedt voor meerdere modellen, Azure AI Search, Bing Search en Azure Functions. Het maakt het eenvoudig om je agenten in de Foundry Portal te bouwen en op grote schaal te implementeren.
 
> V: Ik ben nog steeds in de war, geef me gewoon één optie
>
> A: Begin met het Microsoft Agent Framework om je agenten te bouwen en gebruik vervolgens Microsoft Foundry Agent Service wanneer je ze in productie wilt implementeren en opschalen. Deze aanpak stelt je in staat snel te itereren op je agentlogica met een duidelijke route naar implementatie op ondernemingsniveau.
 
Laten we de belangrijkste verschillen samenvatten in een tabel:

| Framework | Focus | Kernconcepten | Gebruiksscenario's |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Gestroomlijnde agent SDK met tool-aanroep | Agenten, Tools, Azure Identity | Bouwen van AI-agenten, toolgebruik, multi-stap workflows |
| Microsoft Foundry Agent Service | Flexibele modellen, enterprise beveiliging, codegeneratie, tool-aanroep | Modulariteit, Samenwerking, Procesorkestratie | Veilige, schaalbare en flexibele implementatie van AI-agenten |

## Kan ik mijn bestaande Azure-ecosysteemtools direct integreren, of heb ik zelfstandige oplossingen nodig?


Het antwoord is ja, je kunt je bestaande Azure-ecosysteemtools direct integreren met de Microsoft Foundry Agent Service, vooral omdat deze zo is gebouwd dat hij naadloos samenwerkt met andere Azure-services. Je kunt bijvoorbeeld Bing, Azure AI Search en Azure Functions integreren. Er is ook een diepe integratie met Microsoft Foundry.

Het Microsoft Agent Framework integreert ook met Azure-services via `FoundryChatClient` en Azure-identiteit, waardoor je Azure-services direct kunt aanroepen vanuit je agenttools.

## Voorbeeldcodes

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Meer vragen over AI Agent Frameworks?

Word lid van de [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) om andere leerders te ontmoeten, deel te nemen aan office hours en antwoorden te krijgen op je vragen over AI Agents.

## Referenties

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Vorige les

[Introductie tot AI Agents en Agent Use Cases](../01-intro-to-ai-agents/README.md)

## Volgende les

[Begrip van agentische ontwerppatronen](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->