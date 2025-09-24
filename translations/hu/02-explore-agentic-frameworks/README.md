<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a9631d0898fc3c6ecbb3a8a0da7aaba3",
  "translation_date": "2025-08-29T20:12:41+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "hu"
}
-->
[![Az AI ügynök keretrendszerek felfedezése](../../../translated_images/lesson-2-thumbnail.c65f44c93b8558df4d5d407e29970e654629e614f357444a9c27c80feb54c79d.hu.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Kattints a fenti képre a leckéhez tartozó videó megtekintéséhez)_

# AI ügynök keretrendszerek felfedezése

Az AI ügynök keretrendszerek olyan szoftverplatformok, amelyek célja az AI ügynökök létrehozásának, telepítésének és kezelésének egyszerűsítése. Ezek a keretrendszerek előre elkészített komponenseket, absztrakciókat és eszközöket biztosítanak a fejlesztők számára, amelyek megkönnyítik a komplex AI rendszerek fejlesztését.

Ezek a keretrendszerek segítenek a fejlesztőknek, hogy az alkalmazásaik egyedi aspektusaira koncentráljanak, miközben szabványos megközelítéseket kínálnak az AI ügynök fejlesztésének gyakori kihívásaira. Javítják a skálázhatóságot, hozzáférhetőséget és hatékonyságot az AI rendszerek építésében.

## Bevezetés

Ez a lecke az alábbiakat tárgyalja:

- Mik azok az AI ügynök keretrendszerek, és mit tesznek lehetővé a fejlesztők számára?
- Hogyan használhatják a csapatok ezeket az ügynök képességeinek gyors prototípus-készítésére, iterálására és fejlesztésére?
- Miben különböznek a Microsoft által létrehozott keretrendszerek és eszközök egymástól?
- Integrálhatom-e közvetlenül a meglévő Azure ökoszisztéma eszközeimet, vagy különálló megoldásokra van szükségem?
- Mi az Azure AI Agents szolgáltatás, és hogyan segít nekem?

## Tanulási célok

A lecke célja, hogy segítsen megérteni:

- Az AI ügynök keretrendszerek szerepét az AI fejlesztésben.
- Hogyan lehet kihasználni az AI ügynök keretrendszereket intelligens ügynökök építésére.
- Az AI ügynök keretrendszerek által biztosított kulcsfontosságú képességeket.
- Az AutoGen, Semantic Kernel és Azure AI Agent Service közötti különbségeket.

## Mik azok az AI ügynök keretrendszerek, és mit tesznek lehetővé a fejlesztők számára?

A hagyományos AI keretrendszerek segíthetnek az AI integrálásában az alkalmazásokba, és az alábbi módokon javíthatják ezeket az alkalmazásokat:

- **Személyre szabás**: Az AI elemezheti a felhasználói viselkedést és preferenciákat, hogy személyre szabott ajánlásokat, tartalmakat és élményeket nyújtson.
Példa: A streaming szolgáltatások, mint például a Netflix, AI-t használnak filmek és sorozatok ajánlására a megtekintési előzmények alapján, növelve a felhasználói elköteleződést és elégedettséget.
- **Automatizálás és hatékonyság**: Az AI automatizálhatja az ismétlődő feladatokat, egyszerűsítheti a munkafolyamatokat, és javíthatja az operatív hatékonyságot.
Példa: Az ügyfélszolgálati alkalmazások AI-alapú chatbotokat használnak a gyakori kérdések kezelésére, csökkentve a válaszidőt és felszabadítva az emberi ügynököket a bonyolultabb problémákra.
- **Felhasználói élmény javítása**: Az AI javíthatja az általános felhasználói élményt intelligens funkciók, például hangfelismerés, természetes nyelvi feldolgozás és prediktív szöveg segítségével.
Példa: A virtuális asszisztensek, mint például Siri és Google Assistant, AI-t használnak a hangparancsok megértésére és válaszadására, megkönnyítve a felhasználók számára az eszközeikkel való interakciót.

### Ez mind nagyszerűen hangzik, igaz? Akkor miért van szükség az AI ügynök keretrendszerre?

Az AI ügynök keretrendszerek többek, mint egyszerű AI keretrendszerek. Ezeket arra tervezték, hogy lehetővé tegyék intelligens ügynökök létrehozását, amelyek képesek interakcióba lépni a felhasználókkal, más ügynökökkel és a környezettel, hogy meghatározott célokat érjenek el. Ezek az ügynökök autonóm viselkedést mutathatnak, döntéseket hozhatnak, és alkalmazkodhatnak a változó körülményekhez. Nézzük meg az AI ügynök keretrendszerek által biztosított kulcsfontosságú képességeket:

- **Ügynökök együttműködése és koordinációja**: Lehetővé teszi több AI ügynök létrehozását, amelyek együtt dolgozhatnak, kommunikálhatnak és koordinálhatják tevékenységeiket összetett feladatok megoldására.
- **Feladat automatizálás és kezelés**: Mechanizmusokat biztosít a több lépésből álló munkafolyamatok automatizálására, feladatok delegálására és dinamikus feladatkezelésre az ügynökök között.
- **Kontekstuális megértés és alkalmazkodás**: Felruházza az ügynököket a kontextus megértésének, a változó környezethez való alkalmazkodásnak és a valós idejű információk alapján történő döntéshozatal képességével.

Összefoglalva, az ügynökök lehetővé teszik, hogy többet érjünk el, az automatizálást magasabb szintre emeljük, és intelligensebb rendszereket hozzunk létre, amelyek képesek alkalmazkodni és tanulni a környezetükből.

## Hogyan lehet gyorsan prototípust készíteni, iterálni és javítani az ügynök képességeit?

Ez egy gyorsan változó terület, de vannak olyan közös elemek, amelyek a legtöbb AI ügynök keretrendszerben megtalálhatók, és segíthetnek a gyors prototípus-készítésben és iterálásban, például moduláris komponensek, együttműködési eszközök és valós idejű tanulás. Nézzük meg ezeket részletesebben:

- **Moduláris komponensek használata**: Az AI SDK-k előre elkészített komponenseket kínálnak, mint például AI és memória csatlakozók, funkcióhívások természetes nyelv vagy kód pluginok segítségével, prompt sablonok és még sok más.
- **Együttműködési eszközök kihasználása**: Ügynökök tervezése specifikus szerepekkel és feladatokkal, lehetővé téve az együttműködési munkafolyamatok tesztelését és finomítását.
- **Valós idejű tanulás**: Visszacsatolási hurkok megvalósítása, ahol az ügynökök tanulnak az interakciókból, és dinamikusan módosítják viselkedésüket.

### Moduláris komponensek használata

Az olyan SDK-k, mint a Microsoft Semantic Kernel és LangChain, előre elkészített komponenseket kínálnak, például AI csatlakozókat, prompt sablonokat és memória kezelést.

**Hogyan használhatják a csapatok ezeket**: A csapatok gyorsan összeállíthatják ezeket a komponenseket, hogy működő prototípust hozzanak létre anélkül, hogy nulláról kellene kezdeniük, lehetővé téve a gyors kísérletezést és iterálást.

**Hogyan működik a gyakorlatban**: Használhat egy előre elkészített elemzőt a felhasználói bemenetből származó információk kinyerésére, egy memória modult az adatok tárolására és visszakeresésére, valamint egy prompt generátort a felhasználókkal való interakcióhoz, mindezt anélkül, hogy ezeket a komponenseket nulláról kellene felépíteni.

**Példa kód**. Nézzünk meg példákat arra, hogyan használhatunk egy előre elkészített AI csatlakozót a Semantic Kernel Python és .Net segítségével, amely automatikus funkcióhívást használ a modell felhasználói bemenetre adott válaszához:

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

A fenti példából látható, hogyan lehet egy előre elkészített elemzőt használni a felhasználói bemenetből származó kulcsfontosságú információk kinyerésére, például egy repülőjegy foglalási kérés eredetére, céljára és dátumára. Ez a moduláris megközelítés lehetővé teszi, hogy a magas szintű logikára koncentráljunk.

### Együttműködési eszközök kihasználása

Az olyan keretrendszerek, mint a CrewAI, Microsoft AutoGen és Semantic Kernel, megkönnyítik több ügynök létrehozását, amelyek együtt dolgozhatnak.

**Hogyan használhatják a csapatok ezeket**: A csapatok specifikus szerepekkel és feladatokkal rendelkező ügynököket tervezhetnek, lehetővé téve az együttműködési munkafolyamatok tesztelését és finomítását, valamint az általános rendszerhatékonyság javítását.

**Hogyan működik a gyakorlatban**: Létrehozhat egy ügynökcsapatot, ahol minden ügynöknek van egy speciális funkciója, például adatlekérés, elemzés vagy döntéshozatal. Ezek az ügynökök kommunikálhatnak és megoszthatják az információkat, hogy közös célt érjenek el, például válaszoljanak egy felhasználói kérdésre vagy teljesítsenek egy feladatot.

**Példa kód (AutoGen)**:

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

A fenti kódban látható, hogyan lehet létrehozni egy feladatot, amely több ügynök együttműködését igényli az adatok elemzéséhez. Minden ügynök egy adott funkciót lát el, és a feladatot az ügynökök koordinálásával hajtják végre a kívánt eredmény elérése érdekében. Dedikált, speciális szerepekkel rendelkező ügynökök létrehozásával javítható a feladat hatékonysága és teljesítménye.

### Valós idejű tanulás

A fejlett keretrendszerek valós idejű kontextus megértési és alkalmazkodási képességeket biztosítanak.

**Hogyan használhatják a csapatok ezeket**: A csapatok visszacsatolási hurkokat valósíthatnak meg, ahol az ügynökök tanulnak az interakciókból, és dinamikusan módosítják viselkedésüket, ami folyamatos javulást és képességek finomítását eredményezi.

**Hogyan működik a gyakorlatban**: Az ügynökök elemezhetik a felhasználói visszajelzéseket, környezeti adatokat és feladat eredményeket, hogy frissítsék tudásbázisukat, módosítsák döntéshozatali algoritmusaikat, és idővel javítsák teljesítményüket. Ez az iteratív tanulási folyamat lehetővé teszi az ügynökök számára, hogy alkalmazkodjanak a változó körülményekhez és felhasználói preferenciákhoz, javítva az általános rendszerhatékonyságot.

## Miben különböznek az AutoGen, Semantic Kernel és Azure AI Agent Service keretrendszerek?

Számos módon összehasonlíthatók ezek a keretrendszerek, de nézzük meg néhány kulcsfontosságú különbséget a tervezésük, képességeik és célzott felhasználási eseteik szempontjából:

## AutoGen

Az AutoGen egy nyílt forráskódú keretrendszer, amelyet a Microsoft Research AI Frontiers Lab fejlesztett ki. Az eseményvezérelt, elosztott *agentikus* alkalmazásokra összpontosít, lehetővé téve több LLM és SLM, eszközök, valamint fejlett több ügynökös tervezési minták használatát.

Az AutoGen az ügynökök alapfogalmára épül, amelyek autonóm entitások, amelyek érzékelhetik környezetüket, döntéseket hozhatnak, és cselekedhetnek meghatározott célok elérése érdekében. Az ügynökök aszinkron üzeneteken keresztül kommunikálnak, lehetővé téve számukra, hogy függetlenül és párhuzamosan dolgozzanak, növelve a rendszer skálázhatóságát és reagálóképességét.

A Wikipedia szerint egy aktor _a párhuzamos számítás alapvető építőköve. Az általa kapott üzenetre válaszul az aktor képes: helyi döntéseket hozni, további aktorokat létrehozni, több üzenetet küldeni, és meghatározni, hogyan reagáljon a következő kapott üzenetre_.

**Felhasználási esetek**: Kódgenerálás automatizálása, adat-elemzési feladatok, és egyedi ügynökök létrehozása tervezési és kutatási funkciókhoz.

Az AutoGen néhány fontos alapfogalma:

- **Ügynökök**. Az ügynök egy szoftver entitás, amely:
  - **Üzeneteken keresztül kommunikál**, ezek az üzenetek lehetnek szinkron vagy aszinkron.
  - **Fenntartja saját állapotát**, amelyet a beérkező üzenetek módosíthatnak.
  - **Cselekvéseket hajt végre** a kapott üzenetekre vagy az állapotában bekövetkezett változásokra válaszul. Ezek a cselekvések módosíthatják az ügynök állapotát, és külső hatásokat eredményezhetnek, például üzenetnaplók frissítését, új üzenetek küldését, kód végrehajtását vagy API-hívások végrehajtását.

  Itt van egy rövid kódrészlet, amelyben létrehozunk egy saját ügynököt Chat képességekkel:

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

    A fenti kódban létrehoztuk a `MyAgent`-t, amely örökli a `RoutedAgent`-et. Van egy üzenetkezelője, amely kinyomtatja az üzenet tartalmát, majd választ küld az `AssistantAgent` delegált segítségével. Különösen figyeljünk arra, hogy a `self._delegate`-hez hozzárendeljük az `AssistantAgent` egy példányát, amely egy előre elkészített ügynök, amely képes kezelni a chat befejezéseket.

    Ezután értesítsük az AutoGen-t az ügynöktípusról, és indítsuk el a programot:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    A fenti kódban az ügynökök regisztrálva vannak a futtatási környezetben, majd egy üzenetet küldünk az ügynöknek, amely az alábbi kimenetet eredményezi:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Több ügynök**. Az AutoGen támogatja több ügynök létrehozását, amelyek együtt dolgozhatnak összetett feladatok elvégzésére. Az ügynökök kommunikálhatnak, megoszthatják az információkat, és koordinálhatják tevékenységeiket, hogy hatékonyabban oldják meg a problémákat. Több ügynökös rendszer létrehozásához különböző típusú ügynököket definiálhatunk, amelyeknek speciális funkcióik és szerepeik vannak, például adatlekérés, elemzés, döntéshozatal és felhasználói interakció. Nézzük meg, hogyan néz ki egy ilyen létrehozás:

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

    A fenti kódban van egy `GroupChatManager`, amely regisztrálva van a futtatási környezetben. Ez a menedzser felelős a különböző típusú ügyn
## Azure AI Agent Service

Az Azure AI Agent Service egy újabb fejlesztés, amelyet a Microsoft Ignite 2024 rendezvényen mutattak be. Lehetővé teszi AI-ügynökök fejlesztését és telepítését rugalmasabb modellekkel, például nyílt forráskódú LLM-ek, mint a Llama 3, Mistral és Cohere közvetlen hívásával.

Az Azure AI Agent Service erősebb vállalati biztonsági mechanizmusokat és adatkezelési módszereket kínál, így ideális vállalati alkalmazásokhoz.

Kész megoldásként működik többügynökös orkestrációs keretrendszerekkel, mint az AutoGen és a Semantic Kernel.

Ez a szolgáltatás jelenleg nyilvános előzetes verzióban érhető el, és Python és C# nyelveket támogat az ügynökök fejlesztéséhez.

A Semantic Kernel Python segítségével létrehozhatunk egy Azure AI Agentet egy felhasználó által definiált plugin segítségével:

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

### Alapfogalmak

Az Azure AI Agent Service az alábbi alapfogalmakat tartalmazza:

- **Ügynök**. Az Azure AI Agent Service integrálódik az Azure AI Foundry-val. Az AI Foundry-n belül az AI-ügynök egy "intelligens" mikroszolgáltatásként működik, amely kérdések megválaszolására (RAG), műveletek végrehajtására vagy teljes munkafolyamatok automatizálására használható. Ezt úgy éri el, hogy kombinálja a generatív AI modellek erejét olyan eszközökkel, amelyek lehetővé teszik számára a valós adatforrások elérését és kezelését. Íme egy példa egy ügynökre:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    Ebben a példában egy ügynök jön létre a `gpt-4o-mini` modellel, `my-agent` névvel és `You are helpful agent` utasításokkal. Az ügynök eszközökkel és erőforrásokkal van felszerelve, hogy kódértelmezési feladatokat végezzen.

- **Szálak és üzenetek**. A szál egy másik fontos fogalom. Ez egy ügynök és egy felhasználó közötti beszélgetést vagy interakciót képvisel. A szálak használhatók a beszélgetés előrehaladásának nyomon követésére, kontextusinformációk tárolására és az interakció állapotának kezelésére. Íme egy példa egy szálra:

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

    Az előző kódban létrejön egy szál. Ezután egy üzenetet küldenek a szálba. A `create_and_process_run` hívásával az ügynököt arra kérik, hogy végezzen munkát a szálon. Végül az üzeneteket lekérik és naplózzák, hogy lássák az ügynök válaszát. Az üzenetek jelzik a beszélgetés előrehaladását a felhasználó és az ügynök között. Fontos megérteni, hogy az üzenetek különböző típusúak lehetnek, például szöveg, kép vagy fájl, amelyet az ügynök munkája eredményezett, például egy kép vagy szöveges válasz. Fejlesztőként ezeket az információkat felhasználhatja a válasz további feldolgozására vagy a felhasználó számára történő bemutatására.

- **Integráció más AI keretrendszerekkel**. Az Azure AI Agent Service képes más keretrendszerekkel, például az AutoGen és a Semantic Kernel együttműködni, ami azt jelenti, hogy az alkalmazás egy részét ezekben a keretrendszerekben építheti fel, például az Agent Service-t használva orkestrátorként, vagy mindent az Agent Service-ben építhet.

**Felhasználási esetek**: Az Azure AI Agent Service olyan vállalati alkalmazásokhoz készült, amelyek biztonságos, skálázható és rugalmas AI-ügynök telepítést igényelnek.

## Mi a különbség ezek között a keretrendszerek között?

Úgy tűnik, hogy sok átfedés van ezek között a keretrendszerek között, de vannak kulcsfontosságú különbségek a tervezésük, képességeik és célzott felhasználási eseteik tekintetében:

- **AutoGen**: Egy kísérleti keretrendszer, amely a többügynökös rendszerek élvonalbeli kutatására összpontosít. Ez a legjobb hely a kifinomult többügynökös rendszerek kísérletezésére és prototípusának elkészítésére.
- **Semantic Kernel**: Egy gyártásra kész ügynökkönyvtár vállalati ügynöki alkalmazások építéséhez. Az eseményvezérelt, elosztott ügynöki alkalmazásokra összpontosít, lehetővé téve több LLM és SLM, eszközök, valamint egy- és többügynökös tervezési minták használatát.
- **Azure AI Agent Service**: Egy platform és telepítési szolgáltatás az Azure Foundry-ban ügynökök számára. Lehetővé teszi a kapcsolódást az Azure Found által támogatott szolgáltatásokhoz, mint például az Azure OpenAI, Azure AI Search, Bing Search és kódvégrehajtás.

Még mindig nem biztos benne, melyiket válassza?

### Felhasználási esetek

Nézzük meg, hogy segíthetünk-e néhány gyakori felhasználási eset áttekintésével:

> K: Kísérletezek, tanulok és proof-of-concept ügynöki alkalmazásokat építek, és gyorsan szeretnék építeni és kísérletezni.

> V: Az AutoGen jó választás lenne ebben az esetben, mivel az eseményvezérelt, elosztott ügynöki alkalmazásokra összpontosít, és támogatja a fejlett többügynökös tervezési mintákat.

> K: Miért jobb választás az AutoGen, mint a Semantic Kernel és az Azure AI Agent Service ebben az esetben?

> V: Az AutoGen kifejezetten eseményvezérelt, elosztott ügynöki alkalmazásokra lett tervezve, így jól illeszkedik a kódgenerálási és adat-elemzési feladatok automatizálásához. Megadja a szükséges eszközöket és képességeket a komplex többügynökös rendszerek hatékony felépítéséhez.

> K: Úgy hangzik, hogy az Azure AI Agent Service is működhet itt, hiszen vannak eszközei kódgeneráláshoz és más feladatokhoz?

> V: Igen, az Azure AI Agent Service egy platformszolgáltatás ügynökök számára, és beépített képességeket kínál több modellhez, Azure AI Search-hez, Bing Search-hez és Azure Functions-höz. Könnyűvé teszi az ügynökök építését a Foundry Portálban és azok skálázott telepítését.

> K: Még mindig zavaros, csak adj egy opciót.

> V: Egy nagyszerű választás az alkalmazás építése a Semantic Kernel-ben, majd az ügynök telepítése az Azure AI Agent Service segítségével. Ez a megközelítés lehetővé teszi az ügynökök egyszerű tárolását, miközben kihasználja a Semantic Kernel-ben történő többügynökös rendszerek építésének erejét. Ezenkívül a Semantic Kernel rendelkezik egy csatlakozóval az AutoGen-ben, ami megkönnyíti a két keretrendszer együttes használatát.

Foglaljuk össze a kulcsfontosságú különbségeket egy táblázatban:

| Keretrendszer | Fókusz | Alapfogalmak | Felhasználási esetek |
| --- | --- | --- | --- |
| AutoGen | Eseményvezérelt, elosztott ügynöki alkalmazások | Ügynökök, Személyiségek, Funkciók, Adatok | Kódgenerálás, adat-elemzési feladatok |
| Semantic Kernel | Emberi-szerű szöveges tartalom megértése és generálása | Ügynökök, Moduláris komponensek, Együttműködés | Természetes nyelv megértése, tartalomgenerálás |
| Azure AI Agent Service | Rugalmas modellek, vállalati biztonság, Kódgenerálás, Eszközök hívása | Modularitás, Együttműködés, Folyamat-orkestráció | Biztonságos, skálázható és rugalmas AI-ügynök telepítés |

Mi az ideális felhasználási eset ezekhez a keretrendszerekhez?

## Integrálhatom közvetlenül a meglévő Azure ökoszisztéma eszközeimet, vagy különálló megoldásokra van szükségem?

A válasz igen, közvetlenül integrálhatja meglévő Azure ökoszisztéma eszközeit, különösen az Azure AI Agent Service segítségével, mivel ezt úgy tervezték, hogy zökkenőmentesen működjön más Azure szolgáltatásokkal. Például integrálhatja a Binget, az Azure AI Search-t és az Azure Functions-t. Mély integráció is elérhető az Azure AI Foundry-val.

Az AutoGen és a Semantic Kernel esetében szintén integrálhatja az Azure szolgáltatásokat, de ehhez szükség lehet az Azure szolgáltatások hívására a kódjából. Egy másik módja az integrációnak az Azure SDK-k használata, hogy az ügynökökön keresztül kommunikáljon az Azure szolgáltatásokkal. Ezenkívül, ahogy említettük, az Azure AI Agent Service-t használhatja orkestrátorként az AutoGen-ben vagy Semantic Kernel-ben épített ügynökök számára, ami egyszerű hozzáférést biztosít az Azure ökoszisztémához.

### További kérdései vannak az AI Agent keretrendszerekkel kapcsolatban?

Csatlakozzon az [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) közösséghez, hogy találkozzon más tanulókkal, részt vegyen fogadóórákon, és választ kapjon az AI ügynökökkel kapcsolatos kérdéseire.

## Hivatkozások

## Előző lecke

[Bevezetés az AI ügynökökbe és felhasználási esetekbe](../01-intro-to-ai-agents/README.md)

## Következő lecke

[Az ügynöki tervezési minták megértése](../03-agentic-design-patterns/README.md)

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével került lefordításra. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.