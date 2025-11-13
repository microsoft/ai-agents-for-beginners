<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7120197753abacc827b64ac2d5d6966f",
  "translation_date": "2025-11-13T12:58:17+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "fi"
}
-->
[![Tutustu AI-agenttikehyksiin](../../../translated_images/lesson-2-thumbnail.c65f44c93b8558df4d5d407e29970e654629e614f357444a9c27c80feb54c79d.fi.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Klikkaa yllä olevaa kuvaa nähdäksesi tämän oppitunnin videon)_

# Tutustu AI-agenttikehyksiin

AI-agenttikehykset ovat ohjelmistoalustoja, jotka on suunniteltu helpottamaan AI-agenttien luomista, käyttöönottoa ja hallintaa. Nämä kehykset tarjoavat kehittäjille valmiita komponentteja, abstraktioita ja työkaluja, jotka yksinkertaistavat monimutkaisten AI-järjestelmien kehittämistä.

Kehykset auttavat kehittäjiä keskittymään sovellustensa ainutlaatuisiin piirteisiin tarjoamalla standardoituja lähestymistapoja AI-agenttien kehittämisen yleisiin haasteisiin. Ne parantavat skaalautuvuutta, saavutettavuutta ja tehokkuutta AI-järjestelmien rakentamisessa.

## Johdanto

Tämä oppitunti käsittelee:

- Mitä AI-agenttikehykset ovat ja mitä ne mahdollistavat kehittäjille?
- Kuinka tiimit voivat käyttää näitä nopeasti prototyyppien luomiseen, iterointiin ja agenttien kyvykkyyksien parantamiseen?
- Mitkä ovat erot Microsoftin <a href="https://aka.ms/ai-agents/autogen" target="_blank">AutoGen</a>, <a href="https://aka.ms/ai-agents-beginners/semantic-kernel" target="_blank">Semantic Kernel</a> ja <a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a> -kehysten ja työkalujen välillä?
- Voinko integroida olemassa olevat Azure-ekosysteemin työkalut suoraan, vai tarvitsenko erillisiä ratkaisuja?
- Mikä on Azure AI Agents -palvelu ja miten se auttaa minua?

## Oppimistavoitteet

Tämän oppitunnin tavoitteena on auttaa sinua ymmärtämään:

- AI-agenttikehysten rooli AI-kehityksessä.
- Kuinka hyödyntää AI-agenttikehyksiä älykkäiden agenttien rakentamisessa.
- AI-agenttikehysten mahdollistamat keskeiset kyvykkyydet.
- Erot AutoGenin, Semantic Kernelin ja Azure AI Agent Servicen välillä.

## Mitä AI-agenttikehykset ovat ja mitä ne mahdollistavat kehittäjille?

Perinteiset AI-kehykset voivat auttaa sinua integroimaan AI:n sovelluksiisi ja parantamaan näitä sovelluksia seuraavilla tavoilla:

- **Personointi**: AI voi analysoida käyttäjän käyttäytymistä ja mieltymyksiä tarjotakseen personoituja suosituksia, sisältöä ja kokemuksia.  
Esimerkki: Suoratoistopalvelut, kuten Netflix, käyttävät AI:ta ehdottaakseen elokuvia ja ohjelmia katseluhistorian perusteella, mikä parantaa käyttäjän sitoutumista ja tyytyväisyyttä.
- **Automaatio ja tehokkuus**: AI voi automatisoida toistuvia tehtäviä, virtaviivaistaa työnkulkuja ja parantaa operatiivista tehokkuutta.  
Esimerkki: Asiakaspalvelusovellukset käyttävät AI-pohjaisia chatbotteja käsittelemään yleisiä kyselyitä, mikä lyhentää vastausaikoja ja vapauttaa ihmisiä monimutkaisempien ongelmien hoitamiseen.
- **Parannettu käyttäjäkokemus**: AI voi parantaa kokonaisvaltaista käyttäjäkokemusta tarjoamalla älykkäitä ominaisuuksia, kuten puheentunnistusta, luonnollisen kielen käsittelyä ja ennakoivaa tekstinsyöttöä.  
Esimerkki: Virtuaaliassistentit, kuten Siri ja Google Assistant, käyttävät AI:ta ymmärtääkseen ja vastatakseen puhekomentoihin, mikä helpottaa käyttäjien vuorovaikutusta laitteidensa kanssa.

### Kuulostaa hyvältä, mutta miksi tarvitsemme AI-agenttikehyksen?

AI-agenttikehykset edustavat jotain enemmän kuin pelkät AI-kehykset. Ne on suunniteltu mahdollistamaan älykkäiden agenttien luominen, jotka voivat olla vuorovaikutuksessa käyttäjien, muiden agenttien ja ympäristön kanssa saavuttaakseen tiettyjä tavoitteita. Nämä agentit voivat osoittaa autonomista käyttäytymistä, tehdä päätöksiä ja sopeutua muuttuviin olosuhteisiin. Katsotaanpa joitakin AI-agenttikehysten mahdollistamia keskeisiä kyvykkyyksiä:

- **Agenttien yhteistyö ja koordinointi**: Mahdollistaa useiden AI-agenttien luomisen, jotka voivat työskennellä yhdessä, kommunikoida ja koordinoida ratkaistakseen monimutkaisia tehtäviä.
- **Tehtävien automaatio ja hallinta**: Tarjoaa mekanismeja monivaiheisten työnkulkujen automatisointiin, tehtävien delegointiin ja dynaamiseen tehtävien hallintaan agenttien kesken.
- **Kontekstin ymmärtäminen ja sopeutuminen**: Varustaa agentit kyvyllä ymmärtää konteksti, sopeutua muuttuviin ympäristöihin ja tehdä päätöksiä reaaliaikaisen tiedon perusteella.

Yhteenvetona voidaan todeta, että agentit mahdollistavat enemmän, vievät automaation seuraavalle tasolle ja luovat älykkäämpiä järjestelmiä, jotka voivat sopeutua ja oppia ympäristöstään.

## Kuinka nopeasti prototyyppien luominen, iterointi ja agenttien kyvykkyyksien parantaminen onnistuu?

Tämä on nopeasti kehittyvä ala, mutta on joitakin asioita, jotka ovat yhteisiä useimmille AI-agenttikehyksille ja jotka voivat auttaa sinua nopeasti prototyyppien luomisessa ja iteroinnissa, kuten modulaariset komponentit, yhteistyötyökalut ja reaaliaikainen oppiminen. Tarkastellaan näitä tarkemmin:

- **Käytä modulaarisia komponentteja**: AI-SDK:t tarjoavat valmiita komponentteja, kuten AI- ja muistiliittimiä, funktiokutsuja luonnollisella kielellä tai koodiplugineilla, kehotemalleja ja paljon muuta.
- **Hyödynnä yhteistyötyökaluja**: Suunnittele agentteja, joilla on erityiset roolit ja tehtävät, mikä mahdollistaa yhteistyötyönkulkujen testaamisen ja parantamisen.
- **Opi reaaliajassa**: Toteuta palautesilmukoita, joissa agentit oppivat vuorovaikutuksista ja mukauttavat käyttäytymistään dynaamisesti.

### Käytä modulaarisia komponentteja

SDK:t, kuten Microsoft Semantic Kernel ja LangChain, tarjoavat valmiita komponentteja, kuten AI-liittimiä, kehotemalleja ja muistinhallintaa.

**Kuinka tiimit voivat käyttää näitä**: Tiimit voivat nopeasti koota nämä komponentit toimivan prototyypin luomiseksi ilman, että heidän tarvitsee aloittaa tyhjästä, mikä mahdollistaa nopean kokeilun ja iteroinnin.

**Kuinka tämä toimii käytännössä**: Voit käyttää valmiiksi rakennettua parseria käyttäjän syötteen tiedon eristämiseen, muistimoduulia tiedon tallentamiseen ja hakemiseen sekä kehotegeneraattoria vuorovaikutukseen käyttäjien kanssa, kaikki ilman, että sinun tarvitsee rakentaa näitä komponentteja alusta alkaen.

**Esimerkkikoodi**. Katsotaan esimerkkejä siitä, kuinka voit käyttää valmiiksi rakennettua AI-liitintä Semantic Kernel Pythonilla ja .Netillä, joka käyttää automaattista funktiokutsua mallin vastaamiseen käyttäjän syötteeseen:

``` python
# Semantic Kernel Python Example

import asyncio
from typing import Annotated

from semantic_kernel.connectors.ai import FunctionChoiceBehavior
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, AzureChatPromptExecutionSettings
from semantic_kernel.contents import ChatHistory
from semantic_kernel.functions import kernel_function
from semantic_kernel.kernel import Kernel

# Define a ChatHistory object to hold the conversation's context
chat_history = ChatHistory()
chat_history.add_user_message("I'd like to go to New York on January 1, 2025")


# Define a sample plugin that contains the function to book travel
class BookTravelPlugin:
    """A Sample Book Travel Plugin"""

    @kernel_function(name="book_flight", description="Book travel given location and date")
    async def book_flight(
        self, date: Annotated[str, "The date of travel"], location: Annotated[str, "The location to travel to"]
    ) -> str:
        return f"Travel was booked to {location} on {date}"

# Create the Kernel
kernel = Kernel()

# Add the sample plugin to the Kernel object
kernel.add_plugin(BookTravelPlugin(), plugin_name="book_travel")

# Define the Azure OpenAI AI Connector
chat_service = AzureChatCompletion(
    deployment_name="YOUR_DEPLOYMENT_NAME", 
    api_key="YOUR_API_KEY", 
    endpoint="https://<your-resource>.azure.openai.com/",
)

# Define the request settings to configure the model with auto-function calling
request_settings = AzureChatPromptExecutionSettings(function_choice_behavior=FunctionChoiceBehavior.Auto())


async def main():
    # Make the request to the model for the given chat history and request settings
    # The Kernel contains the sample that the model will request to invoke
    response = await chat_service.get_chat_message_content(
        chat_history=chat_history, settings=request_settings, kernel=kernel
    )
    assert response is not None

    """
    Note: In the auto function calling process, the model determines it can invoke the 
    `BookTravelPlugin` using the `book_flight` function, supplying the necessary arguments. 
    
    For example:

    "tool_calls": [
        {
            "id": "call_abc123",
            "type": "function",
            "function": {
                "name": "BookTravelPlugin-book_flight",
                "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
            }
        }
    ]

    Since the location and date arguments are required (as defined by the kernel function), if the 
    model lacks either, it will prompt the user to provide them. For instance:

    User: Book me a flight to New York.
    Model: Sure, I'd love to help you book a flight. Could you please specify the date?
    User: I want to travel on January 1, 2025.
    Model: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels!
    """

    print(f"`{response}`")
    # Example AI Model Response: `Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽`

    # Add the model's response to our chat history context
    chat_history.add_assistant_message(response.content)


if __name__ == "__main__":
    asyncio.run(main())
```
```csharp
// Semantic Kernel C# example

using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;
using System.ComponentModel;
using Microsoft.SemanticKernel.Connectors.AzureOpenAI;

ChatHistory chatHistory = [];
chatHistory.AddUserMessage("I'd like to go to New York on January 1, 2025");

var kernelBuilder = Kernel.CreateBuilder();
kernelBuilder.AddAzureOpenAIChatCompletion(
    deploymentName: "NAME_OF_YOUR_DEPLOYMENT",
    apiKey: "YOUR_API_KEY",
    endpoint: "YOUR_AZURE_ENDPOINT"
);
kernelBuilder.Plugins.AddFromType<BookTravelPlugin>("BookTravel"); 
var kernel = kernelBuilder.Build();

var settings = new AzureOpenAIPromptExecutionSettings()
{
    FunctionChoiceBehavior = FunctionChoiceBehavior.Auto()
};

var chatCompletion = kernel.GetRequiredService<IChatCompletionService>();

var response = await chatCompletion.GetChatMessageContentAsync(chatHistory, settings, kernel);

/*
Behind the scenes, the model recognizes the tool to call, what arguments it already has (location) and (date)
{

"tool_calls": [
    {
        "id": "call_abc123",
        "type": "function",
        "function": {
            "name": "BookTravelPlugin-book_flight",
            "arguments": "{'location': 'New York', 'date': '2025-01-01'}"
        }
    }
]
*/

Console.WriteLine(response.Content);
chatHistory.AddMessage(response!.Role, response!.Content!);

// Example AI Model Response: Your flight to New York on January 1, 2025, has been successfully booked. Safe travels! ✈️🗽

// Define a plugin that contains the function to book travel
public class BookTravelPlugin
{
    [KernelFunction("book_flight")]
    [Description("Book travel given location and date")]
    public async Task<string> BookFlight(DateTime date, string location)
    {
        return await Task.FromResult( $"Travel was booked to {location} on {date}");
    }
}
```
  
Tässä esimerkissä näet, kuinka voit hyödyntää valmiiksi rakennettua parseria käyttäjän syötteen keskeisten tietojen, kuten lähtöpaikan, määränpään ja lentovarauksen päivämäärän, eristämiseen. Tämä modulaarinen lähestymistapa mahdollistaa keskittymisen korkean tason logiikkaan.

### Hyödynnä yhteistyötyökaluja

Kehykset, kuten CrewAI, Microsoft AutoGen ja Semantic Kernel, helpottavat useiden agenttien luomista, jotka voivat työskennellä yhdessä.

**Kuinka tiimit voivat käyttää näitä**: Tiimit voivat suunnitella agentteja, joilla on erityiset roolit ja tehtävät, mikä mahdollistaa yhteistyötyönkulkujen testaamisen ja parantamisen sekä järjestelmän tehokkuuden parantamisen.

**Kuinka tämä toimii käytännössä**: Voit luoda agenttitiimin, jossa jokaisella agentilla on erikoistunut tehtävä, kuten tiedonhaku, analyysi tai päätöksenteko. Nämä agentit voivat kommunikoida ja jakaa tietoa saavuttaakseen yhteisen tavoitteen, kuten käyttäjän kyselyyn vastaamisen tai tehtävän suorittamisen.

**Esimerkkikoodi (AutoGen)**:

```python
# creating agents, then create a round robin schedule where they can work together, in this case in order

# Data Retrieval Agent
# Data Analysis Agent
# Decision Making Agent

agent_retrieve = AssistantAgent(
    name="dataretrieval",
    model_client=model_client,
    tools=[retrieve_tool],
    system_message="Use tools to solve tasks."
)

agent_analyze = AssistantAgent(
    name="dataanalysis",
    model_client=model_client,
    tools=[analyze_tool],
    system_message="Use tools to solve tasks."
)

# conversation ends when user says "APPROVE"
termination = TextMentionTermination("APPROVE")

user_proxy = UserProxyAgent("user_proxy", input_func=input)

team = RoundRobinGroupChat([agent_retrieve, agent_analyze, user_proxy], termination_condition=termination)

stream = team.run_stream(task="Analyze data", max_turns=10)
# Use asyncio.run(...) when running in a script.
await Console(stream)
```
  
Edellisessä koodissa näet, kuinka voit luoda tehtävän, joka sisältää useita agentteja, jotka työskentelevät yhdessä analysoidakseen dataa. Jokainen agentti suorittaa tietyn tehtävän, ja tehtävä toteutetaan koordinoimalla agenttien toimintaa halutun lopputuloksen saavuttamiseksi. Luomalla erikoistuneita agentteja voit parantaa tehtävän tehokkuutta ja suorituskykyä.

### Opi reaaliajassa

Edistyneet kehykset tarjoavat kyvykkyyksiä reaaliaikaiseen kontekstin ymmärtämiseen ja sopeutumiseen.

**Kuinka tiimit voivat käyttää näitä**: Tiimit voivat toteuttaa palautesilmukoita, joissa agentit oppivat vuorovaikutuksista ja mukauttavat käyttäytymistään dynaamisesti, mikä johtaa jatkuvaan parantamiseen ja kyvykkyyksien hienosäätöön.

**Kuinka tämä toimii käytännössä**: Agentit voivat analysoida käyttäjäpalautetta, ympäristötietoja ja tehtävän tuloksia päivittääkseen tietokantaansa, mukauttaakseen päätöksentekoalgoritmejaan ja parantaakseen suorituskykyään ajan myötä. Tämä iteratiivinen oppimisprosessi mahdollistaa agenttien sopeutumisen muuttuviin olosuhteisiin ja käyttäjän mieltymyksiin, mikä parantaa järjestelmän kokonaistehokkuutta.

## Mitkä ovat erot AutoGenin, Semantic Kernelin ja Azure AI Agent Servicen välillä?

Näitä kehyksiä voidaan verrata monin tavoin, mutta tarkastellaan joitakin keskeisiä eroja niiden suunnittelussa, kyvykkyyksissä ja kohdekäyttötapauksissa:

## AutoGen

AutoGen on Microsoft Researchin AI Frontiers Labin kehittämä avoimen lähdekoodin kehys. Se keskittyy tapahtumapohjaisiin, hajautettuihin *agenttisiin* sovelluksiin, jotka mahdollistavat useiden LLM:ien ja SLM:ien, työkalujen ja edistyneiden monen agentin suunnittelumallien käytön.

AutoGen perustuu agenttien ydinideaan, jotka ovat autonomisia yksiköitä, jotka voivat havaita ympäristönsä, tehdä päätöksiä ja ryhtyä toimiin saavuttaakseen tiettyjä tavoitteita. Agentit kommunikoivat asynkronisten viestien kautta, mikä mahdollistaa niiden itsenäisen ja rinnakkaisen työskentelyn, parantaen järjestelmän skaalautuvuutta ja reagointikykyä.

<a href="https://en.wikipedia.org/wiki/Actor_model" target="_blank">Agentit perustuvat näyttelijämalliin</a>. Wikipedian mukaan näyttelijä on _perusosa rinnakkaisessa laskennassa. Vastauksena vastaanottamaansa viestiin näyttelijä voi: tehdä paikallisia päätöksiä, luoda lisää näyttelijöitä, lähettää lisää viestejä ja päättää, miten vastata seuraavaan vastaanotettuun viestiin_.

**Käyttötapaukset**: Koodin generoinnin automatisointi, data-analyysitehtävät ja räätälöityjen agenttien rakentaminen suunnittelu- ja tutkimustoimintoihin.

Tässä on joitakin AutoGenin keskeisiä käsitteitä:

- **Agentit**. Agentti on ohjelmistoyksikkö, joka:  
  - **Kommunikoi viestien kautta**, jotka voivat olla synkronisia tai asynkronisia.  
  - **Ylläpitää omaa tilaansa**, jota saapuvat viestit voivat muuttaa.  
  - **Suorittaa toimia** vastauksena vastaanotettuihin viesteihin tai tilansa muutoksiin. Nämä toimet voivat muuttaa agentin tilaa ja tuottaa ulkoisia vaikutuksia, kuten viestilokien päivittämistä, uusien viestien lähettämistä, koodin suorittamista tai API-kutsujen tekemistä.  

  Tässä on lyhyt koodiesimerkki, jossa luot oman agentin chat-ominaisuuksilla:

    ```python
    from autogen_agentchat.agents import AssistantAgent
    from autogen_agentchat.messages import TextMessage
    from autogen_ext.models.openai import OpenAIChatCompletionClient


    class MyAgent(RoutedAgent):
        def __init__(self, name: str) -> None:
            super().__init__(name)
            model_client = OpenAIChatCompletionClient(model="gpt-4o")
            self._delegate = AssistantAgent(name, model_client=model_client)
    
        @message_handler
        async def handle_my_message_type(self, message: MyMessageType, ctx: MessageContext) -> None:
            print(f"{self.id.type} received message: {message.content}")
            response = await self._delegate.on_messages(
                [TextMessage(content=message.content, source="user")], ctx.cancellation_token
            )
            print(f"{self.id.type} responded: {response.chat_message.content}")
    ```
  
Edellisessä koodissa `MyAgent` on luotu ja perii `RoutedAgent`-luokan. Sillä on viestinkäsittelijä, joka tulostaa viestin sisällön ja lähettää sitten vastauksen `AssistantAgent`-edustajan avulla. Huomaa erityisesti, kuinka `self._delegate`-muuttujalle annetaan `AssistantAgent`-instanssi, joka on valmiiksi rakennettu agentti, joka voi käsitellä chat-vastauksia.

AutoGenille ilmoitetaan tästä agenttityypistä ja ohjelma käynnistetään seuraavaksi:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```
  
Edellisessä koodissa agentit rekisteröidään ajonaikaan ja sitten agentille lähetetään viesti, mikä johtaa seuraavaan tulokseen:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```
  
- **Moniagenttisuus**. AutoGen tukee useiden agenttien luomista, jotka voivat työskennellä yhdessä saavuttaakseen monimutkaisia tehtäviä. Agentit voivat kommunikoida, jakaa tietoa ja koordinoida toimiaan ongelmien ratkaisemiseksi tehokkaammin. Moniagenttijärjestelmän luomiseksi voit määritellä eri tyyppisiä agentteja, joilla on erikoistuneita tehtäviä ja rooleja, kuten tiedonhaku, analyysi, päätöksenteko ja käyttäjän vuorovaikutus. Katsotaanpa, miltä tällainen luominen näyttää:

    ```python
    editor_description = "Editor for planning and reviewing the content."

    # Example of declaring an Agent
    editor_agent_type = await EditorAgent.register(
    runtime,
    editor_topic_type,  # Using topic type as the agent type.
    lambda: EditorAgent(
        description=editor_description,
        group_chat_topic_type=group_chat_topic_type,
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        ),
    )

    # remaining declarations shortened for brevity

    # Group chat
    group_chat_manager_type = await GroupChatManager.register(
    runtime,
    "group_chat_manager",
    lambda: GroupChatManager(
        participant_topic_types=[writer_topic_type, illustrator_topic_type, editor_topic_type, user_topic_type],
        model_client=OpenAIChatCompletionClient(
            model="gpt-4o-2024-08-06",
            # api_key="YOUR_API_KEY",
        ),
        participant_descriptions=[
            writer_description, 
            illustrator_description, 
            editor_description, 
            user_description
        ],
        ),
    )
    ```
  
Edellisessä koodissa meillä on `GroupChatManager`, joka on rekisteröity ajonaikaan. Tämä manageri vastaa eri agenttityyppien, kuten kirjoittajien, kuvittajien, toimittajien ja käyttäjien, vuorovaikutuksen koordinoinnista.

- **Agenttien ajonaika**. Kehys tarjoaa ajonaikaympäristön, joka mahdollistaa agenttien välisen viestinnän, hallitsee niiden identiteettejä ja elinkaaria sekä valvoo turvallisuus- ja yksityisyysrajoja. Tämä tarkoittaa, että voit ajaa agenttejasi turvallisessa ja hallitussa ympäristössä, varmistaen, että ne voivat olla vuorovaikutuksessa turvallisesti ja tehokkaasti. Kiinnostavia ajonaikoja ovat:  
  - **Itsenäinen ajonaika**. Tämä on hyvä valinta yksiprosessisovelluksille, joissa kaikki agentit on toteutettu samalla ohjelmointikielellä ja ne toimivat samassa prosessissa. Tässä on havainnollistus siitä, miten se toimii:  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-standalone.svg" target="_blank">Itsenäinen ajonaika</a>  
Sovelluspino  
    *agentit kommunikoivat viestien kautta ajonaikaan, ja ajonaika hallitsee agenttien elinkaarta*  
  - **Hajautettu agenttien ajonaika**, joka sopii moniprosessisovelluksiin, joissa agentit voivat olla toteutettu eri ohjelmointikielillä ja toimia eri koneilla. Tässä on havainnollistus siitä, miten se toimii:  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-distributed.svg" target="_blank">Hajautettu ajonaika</a>

## Semantic Kernel + Agent Framework

Semantic Kernel on yritysvalmis AI Orchestration SDK. Se koostuu AI- ja muistiliittimistä sekä Agent Frameworkista.

Käsitellään ensin joitakin keskeisiä komponentteja:

- **AI-liittimet**: Tämä on rajapinta ulkoisiin AI-palveluihin ja tietolähteisiin käytettäväksi sekä Pythonissa että C#:ssa.

  ```python
  # Semantic Kernel Python
  from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
  from semantic_kernel.kernel import Kernel

  kernel = Kernel()
  kernel.add_service(
    AzureChatCompletion(
        deployment_name="your-deployment-name",
        api_key="your-api-key",
        endpoint="your-endpoint",
    )
  )
  ```  
  
    ```csharp
    // Semantic Kernel C#
    using Microsoft.SemanticKernel;

    // Create kernel
    var builder = Kernel.CreateBuilder();
    
    // Add a chat completion service:
    builder.Services.AddAzureOpenAIChatCompletion(
        "your-resource-name",
        "your-endpoint",
        "your-resource-key",
        "deployment-model");
    var kernel = builder.Build();
    ```
  
Tässä on yksinkertainen esimerkki siitä, kuinka voit luoda kernelin ja lisätä chat-vastauspalvelun. Semantic Kernel luo yhteyden ulkoiseen AI-palveluun, tässä tapauksessa Azure OpenAI Chat Completioniin.

- **Pluginit**: Nämä kapseloivat funktioita, joita sovellus voi käyttää. On sekä valmiita plugineja että mukautettuja, joita voit luoda. Liittyvä käsite on "kehotefunktiot". Sen sijaan, että tarjoaisit luonnollisen kielen vihjeitä funktion kutsumiseen, lähetät tiettyjä funktioita mallille. Nykyisen chat
Nämä tiedot tallennetaan muistikokoelmaan `SummarizedAzureDocs`. Tämä on hyvin yksinkertaistettu esimerkki, mutta voit nähdä, kuinka tietoa voidaan tallentaa muistiin LLM:n käyttöä varten.

Siinä olivat Semantic Kernel -kehysjärjestelmän perusteet, mutta entä Agent Framework?

## Azure AI Agent Service

Azure AI Agent Service on uudempi lisäys, joka esiteltiin Microsoft Ignite 2024 -tapahtumassa. Sen avulla voidaan kehittää ja ottaa käyttöön AI-agentteja joustavammilla malleilla, kuten suoraan käyttämällä avoimen lähdekoodin LLM-malleja, kuten Llama 3, Mistral ja Cohere.

Azure AI Agent Service tarjoaa vahvempia yritystason tietoturvamekanismeja ja tietojen tallennusmenetelmiä, mikä tekee siitä sopivan yrityssovelluksiin.

Se toimii heti valmiina monen agentin orkestrointikehysten, kuten AutoGenin ja Semantic Kernelin, kanssa.

Tämä palvelu on tällä hetkellä julkisessa esikatselussa ja tukee Pythonia ja C#:a agenttien rakentamiseen.

Käyttämällä Semantic Kernel Pythonia voimme luoda Azure AI Agentin käyttäjän määrittelemällä lisäosalla:

```python
import asyncio
from typing import Annotated

from azure.identity.aio import DefaultAzureCredential

from semantic_kernel.agents import AzureAIAgent, AzureAIAgentSettings, AzureAIAgentThread
from semantic_kernel.contents import ChatMessageContent
from semantic_kernel.contents import AuthorRole
from semantic_kernel.functions import kernel_function


# Define a sample plugin for the sample
class MenuPlugin:
    """A sample Menu Plugin used for the concept sample."""

    @kernel_function(description="Provides a list of specials from the menu.")
    def get_specials(self) -> Annotated[str, "Returns the specials from the menu."]:
        return """
        Special Soup: Clam Chowder
        Special Salad: Cobb Salad
        Special Drink: Chai Tea
        """

    @kernel_function(description="Provides the price of the requested menu item.")
    def get_item_price(
        self, menu_item: Annotated[str, "The name of the menu item."]
    ) -> Annotated[str, "Returns the price of the menu item."]:
        return "$9.99"


async def main() -> None:
    ai_agent_settings = AzureAIAgentSettings.create()

    async with (
        DefaultAzureCredential() as creds,
        AzureAIAgent.create_client(
            credential=creds,
            conn_str=ai_agent_settings.project_connection_string.get_secret_value(),
        ) as client,
    ):
        # Create agent definition
        agent_definition = await client.agents.create_agent(
            model=ai_agent_settings.model_deployment_name,
            name="Host",
            instructions="Answer questions about the menu.",
        )

        # Create the AzureAI Agent using the defined client and agent definition
        agent = AzureAIAgent(
            client=client,
            definition=agent_definition,
            plugins=[MenuPlugin()],
        )

        # Create a thread to hold the conversation
        # If no thread is provided, a new thread will be
        # created and returned with the initial response
        thread: AzureAIAgentThread | None = None

        user_inputs = [
            "Hello",
            "What is the special soup?",
            "How much does that cost?",
            "Thank you",
        ]

        try:
            for user_input in user_inputs:
                print(f"# User: '{user_input}'")
                # Invoke the agent for the specified thread
                response = await agent.get_response(
                    messages=user_input,
                    thread_id=thread,
                )
                print(f"# {response.name}: {response.content}")
                thread = response.thread
        finally:
            await thread.delete() if thread else None
            await client.agents.delete_agent(agent.id)


if __name__ == "__main__":
    asyncio.run(main())
```

### Keskeiset käsitteet

Azure AI Agent Servicellä on seuraavat keskeiset käsitteet:

- **Agentti**. Azure AI Agent Service integroituu Azure AI Foundryyn. AI Foundryssa AI-agentti toimii "älykkäänä" mikropalveluna, jota voidaan käyttää vastaamaan kysymyksiin (RAG), suorittamaan toimintoja tai täysin automatisoimaan työnkulkuja. Tämä saavutetaan yhdistämällä generatiivisten AI-mallien voima työkaluihin, jotka mahdollistavat pääsyn ja vuorovaikutuksen todellisten tietolähteiden kanssa. Tässä esimerkki agentista:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    Tässä esimerkissä agentti luodaan mallilla `gpt-4o-mini`, nimellä `my-agent` ja ohjeilla `You are helpful agent`. Agentti varustetaan työkaluilla ja resursseilla koodin tulkintatehtävien suorittamiseen.

- **Keskusteluketju ja viestit**. Keskusteluketju on toinen tärkeä käsite. Se edustaa keskustelua tai vuorovaikutusta agentin ja käyttäjän välillä. Keskusteluketjuja voidaan käyttää keskustelun etenemisen seuraamiseen, kontekstin tallentamiseen ja vuorovaikutuksen tilan hallintaan. Tässä esimerkki keskusteluketjusta:

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

    Edellisessä koodissa luodaan keskusteluketju. Sen jälkeen ketjuun lähetetään viesti. Kutsumalla `create_and_process_run` agenttia pyydetään suorittamaan tehtävä ketjussa. Lopuksi viestit haetaan ja kirjataan, jotta nähdään agentin vastaus. Viestit osoittavat keskustelun etenemisen käyttäjän ja agentin välillä. On myös tärkeää ymmärtää, että viestit voivat olla eri tyyppisiä, kuten tekstiä, kuvia tai tiedostoja, jotka ovat agentin työn tuloksena syntyneitä, esimerkiksi kuva tai tekstivastaus. Kehittäjänä voit käyttää näitä tietoja jatkokäsittelyyn tai esittää ne käyttäjälle.

- **Integroituu muihin AI-kehyksiin**. Azure AI Agent Service voi olla vuorovaikutuksessa muiden kehysten, kuten AutoGenin ja Semantic Kernelin, kanssa, mikä tarkoittaa, että voit rakentaa osan sovelluksestasi jossakin näistä kehyksistä ja esimerkiksi käyttää Agent Serviceä orkestroijana tai rakentaa kaiken Agent Servicen sisällä.

**Käyttötapaukset**: Azure AI Agent Service on suunniteltu yrityssovelluksiin, jotka vaativat turvallista, skaalautuvaa ja joustavaa AI-agenttien käyttöönottoa.

## Mitä eroa näillä kehyksillä on?

Vaikuttaa siltä, että näillä kehyksillä on paljon päällekkäisyyksiä, mutta niiden suunnittelussa, ominaisuuksissa ja kohdekäyttötapauksissa on joitakin keskeisiä eroja:

- **AutoGen**: On kokeilukehys, joka keskittyy huippututkimukseen monen agentin järjestelmistä. Se on paras paikka kokeilla ja prototyyppien rakentamiseen kehittyneistä monen agentin järjestelmistä.
- **Semantic Kernel**: On tuotantovalmis agenttikirjasto yritysagenttisovellusten rakentamiseen. Keskittyy tapahtumapohjaisiin, hajautettuihin agenttisovelluksiin, jotka mahdollistavat useiden LLM- ja SLM-mallien, työkalujen sekä yhden/monta agenttia sisältävien suunnittelumallien käytön.
- **Azure AI Agent Service**: On Azure Foundryn alusta ja käyttöönottopalvelu agenteille. Tarjoaa yhteyden rakentamisen Azure Foundryn tukemiin palveluihin, kuten Azure OpenAI, Azure AI Search, Bing Search ja koodin suoritus.

Etkö vieläkään tiedä, minkä valita?

### Käyttötapaukset

Katsotaanpa, voimmeko auttaa sinua käymällä läpi joitakin yleisiä käyttötapauksia:

> K: Kokeilen, opettelen ja rakennan proof-of-concept-agenttisovelluksia, ja haluan pystyä rakentamaan ja kokeilemaan nopeasti
>

>V: AutoGen olisi hyvä valinta tähän tilanteeseen, koska se keskittyy tapahtumapohjaisiin, hajautettuihin agenttisovelluksiin ja tukee kehittyneitä monen agentin suunnittelumalleja.

> K: Miksi AutoGen on parempi valinta kuin Semantic Kernel ja Azure AI Agent Service tässä käyttötapauksessa?
>
> V: AutoGen on erityisesti suunniteltu tapahtumapohjaisiin, hajautettuihin agenttisovelluksiin, mikä tekee siitä hyvin sopivan koodin generointiin ja data-analyysitehtäviin. Se tarjoaa tarvittavat työkalut ja ominaisuudet monimutkaisten monen agentin järjestelmien rakentamiseen tehokkaasti.

> K: Kuulostaa siltä, että Azure AI Agent Service voisi toimia tässä myös, sillä siinä on työkaluja koodin generointiin ja muuhun?
>
> V: Kyllä, Azure AI Agent Service on agenttien alusta ja tarjoaa sisäänrakennettuja ominaisuuksia useille malleille, Azure AI Searchille, Bing Searchille ja Azure Functionsille. Se tekee agenttien rakentamisesta Foundry-portaalissa helppoa ja mahdollistaa niiden käyttöönoton laajassa mittakaavassa.

> K: Olen edelleen hämmentynyt, anna vain yksi vaihtoehto
>
> V: Erinomainen valinta on rakentaa sovelluksesi ensin Semantic Kernelissä ja käyttää sitten Azure AI Agent Serviceä agenttisi käyttöönottoon. Tämä lähestymistapa mahdollistaa agenttien helpon säilyttämisen samalla, kun hyödynnetään Semantic Kernelin voimaa monen agentin järjestelmien rakentamiseen. Lisäksi Semantic Kernelillä on liitin AutoGenissä, mikä tekee näiden kehysten yhteiskäytöstä helppoa.

Tiivistetään keskeiset erot taulukkoon:

| Kehys | Painopiste | Keskeiset käsitteet | Käyttötapaukset |
| --- | --- | --- | --- |
| AutoGen | Tapahtumapohjaiset, hajautetut agenttisovellukset | Agentit, Persoonat, Funktiot, Data | Koodin generointi, data-analyysitehtävät |
| Semantic Kernel | Ihmismäisen tekstisisällön ymmärtäminen ja generointi | Agentit, Modulaariset komponentit, Yhteistyö | Luonnollisen kielen ymmärtäminen, sisällön generointi |
| Azure AI Agent Service | Joustavat mallit, yritystason tietoturva, Koodin generointi, Työkalujen käyttö | Modulaarisuus, Yhteistyö, Prosessien orkestrointi | Turvallinen, skaalautuva ja joustava AI-agenttien käyttöönotto |

Mikä on ihanteellinen käyttötapaus kullekin näistä kehyksistä?

## Voinko integroida olemassa olevat Azure-ekosysteemin työkaluni suoraan vai tarvitsenko erillisiä ratkaisuja?

Vastaus on kyllä, voit integroida olemassa olevat Azure-ekosysteemin työkalusi suoraan Azure AI Agent Serviceen erityisesti, koska se on rakennettu toimimaan saumattomasti muiden Azure-palveluiden kanssa. Voit esimerkiksi integroida Bingin, Azure AI Searchin ja Azure Functionsin. Lisäksi siinä on syvä integraatio Azure AI Foundryn kanssa.

AutoGenin ja Semantic Kernelin osalta voit myös integroida Azure-palveluihin, mutta se saattaa vaatia Azure-palveluiden kutsumista koodistasi. Toinen tapa integroida on käyttää Azure SDK:ta vuorovaikutukseen Azure-palveluiden kanssa agenteistasi. Lisäksi, kuten mainittiin, voit käyttää Azure AI Agent Serviceä orkestroijana AutoGenissä tai Semantic Kernelissä rakennettuihin agentteihin, mikä mahdollistaa helpon pääsyn Azure-ekosysteemiin.

## Esimerkkikoodit

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Onko sinulla lisää kysymyksiä AI Agent Frameworkeista?

Liity [Azure AI Foundry Discordiin](https://aka.ms/ai-agents/discord) tapaamaan muita oppijoita, osallistumaan toimistoaikoihin ja saamaan vastauksia AI-agentteihin liittyviin kysymyksiisi.

## Viitteet

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/" target="_blank">Semantic Kernel ja AutoGen</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-python" target="_blank">Semantic Kernel Python Agent Framework</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp" target="_blank">Semantic Kernel .Net Agent Framework</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a>
- <a href="https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121" target="_blank">Azure AI Agent Servicen käyttö AutoGenin / Semantic Kernelin kanssa monen agentin ratkaisun rakentamiseen</a>

## Edellinen oppitunti

[Johdatus AI-agentteihin ja agenttien käyttötapauksiin](../01-intro-to-ai-agents/README.md)

## Seuraava oppitunti

[Agenttisuunnittelumallien ymmärtäminen](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäisellä kielellä tulisi katsoa ensisijaiseksi lähteeksi. Kriittisen tiedon osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa väärinkäsityksistä tai virhetulkinnoista, jotka johtuvat tämän käännöksen käytöstä.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->