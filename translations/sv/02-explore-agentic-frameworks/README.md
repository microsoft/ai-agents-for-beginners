<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7120197753abacc827b64ac2d5d6966f",
  "translation_date": "2025-11-13T12:43:53+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "sv"
}
-->
[![Utforska AI-agentramverk](../../../translated_images/lesson-2-thumbnail.c65f44c93b8558df4d5d407e29970e654629e614f357444a9c27c80feb54c79d.sv.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Klicka på bilden ovan för att se videon för denna lektion)_

# Utforska AI-agentramverk

AI-agentramverk är mjukvaruplattformar som är utformade för att förenkla skapandet, implementeringen och hanteringen av AI-agenter. Dessa ramverk erbjuder utvecklare förbyggda komponenter, abstraktioner och verktyg som effektiviserar utvecklingen av komplexa AI-system.

Ramverken hjälper utvecklare att fokusera på de unika aspekterna av sina applikationer genom att tillhandahålla standardiserade lösningar på vanliga utmaningar inom AI-agentutveckling. De förbättrar skalbarhet, tillgänglighet och effektivitet vid byggandet av AI-system.

## Introduktion 

Denna lektion kommer att behandla:

- Vad är AI-agentramverk och vad möjliggör de för utvecklare att uppnå?
- Hur kan team använda dessa för att snabbt skapa prototyper, iterera och förbättra sin agents kapabiliteter?
- Vilka är skillnaderna mellan ramverken och verktygen skapade av Microsoft <a href="https://aka.ms/ai-agents/autogen" target="_blank">AutoGen</a>, <a href="https://aka.ms/ai-agents-beginners/semantic-kernel" target="_blank">Semantic Kernel</a>, och <a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a>?
- Kan jag integrera mina befintliga Azure-ekosystemverktyg direkt, eller behöver jag fristående lösningar?
- Vad är Azure AI Agents-tjänsten och hur hjälper den mig?

## Lärandemål

Målen med denna lektion är att hjälpa dig förstå:

- AI-agentramverks roll inom AI-utveckling.
- Hur man utnyttjar AI-agentramverk för att bygga intelligenta agenter.
- Nyckelkapabiliteter som möjliggörs av AI-agentramverk.
- Skillnaderna mellan AutoGen, Semantic Kernel och Azure AI Agent Service.

## Vad är AI-agentramverk och vad möjliggör de för utvecklare att göra?

Traditionella AI-ramverk kan hjälpa dig att integrera AI i dina appar och förbättra dessa appar på följande sätt:

- **Personalisering**: AI kan analysera användarbeteende och preferenser för att ge personliga rekommendationer, innehåll och upplevelser.
Exempel: Streamingtjänster som Netflix använder AI för att föreslå filmer och serier baserat på tittarhistorik, vilket ökar användarengagemang och tillfredsställelse.
- **Automatisering och effektivitet**: AI kan automatisera repetitiva uppgifter, effektivisera arbetsflöden och förbättra operativ effektivitet.
Exempel: Kundtjänstappar använder AI-drivna chatbotar för att hantera vanliga frågor, vilket minskar svarstider och frigör mänskliga agenter för mer komplexa ärenden.
- **Förbättrad användarupplevelse**: AI kan förbättra den övergripande användarupplevelsen genom att tillhandahålla intelligenta funktioner som röstigenkänning, naturlig språkbehandling och förutsägande text.
Exempel: Virtuella assistenter som Siri och Google Assistant använder AI för att förstå och svara på röstkommandon, vilket gör det enklare för användare att interagera med sina enheter.

### Det låter ju bra, så varför behöver vi AI-agentramverk?

AI-agentramverk representerar något mer än bara AI-ramverk. De är utformade för att möjliggöra skapandet av intelligenta agenter som kan interagera med användare, andra agenter och miljön för att uppnå specifika mål. Dessa agenter kan uppvisa autonomt beteende, fatta beslut och anpassa sig till förändrade förhållanden. Låt oss titta på några nyckelkapabiliteter som möjliggörs av AI-agentramverk:

- **Agenters samarbete och koordinering**: Möjliggör skapandet av flera AI-agenter som kan arbeta tillsammans, kommunicera och koordinera för att lösa komplexa uppgifter.
- **Automatisering och hantering av uppgifter**: Tillhandahåller mekanismer för att automatisera flerstegsarbetsflöden, delegera uppgifter och dynamiskt hantera uppgifter mellan agenter.
- **Kontextuell förståelse och anpassning**: Utrustar agenter med förmågan att förstå kontext, anpassa sig till förändrade miljöer och fatta beslut baserat på realtidsinformation.

Sammanfattningsvis möjliggör agenter att göra mer, att ta automatisering till nästa nivå, att skapa mer intelligenta system som kan anpassa sig och lära sig från sin miljö.

## Hur snabbt skapa prototyper, iterera och förbättra agentens kapabiliteter?

Detta är ett snabbt föränderligt landskap, men det finns några saker som är gemensamma för de flesta AI-agentramverk som kan hjälpa dig att snabbt skapa prototyper och iterera, nämligen modulkomponenter, samarbetsverktyg och realtidslärande. Låt oss dyka in i dessa:

- **Använd modulkomponenter**: AI-SDK:er erbjuder förbyggda komponenter såsom AI- och minnesanslutningar, funktionsanrop med naturligt språk eller kodplugins, promptmallar och mer.
- **Utnyttja samarbetsverktyg**: Designa agenter med specifika roller och uppgifter, vilket gör det möjligt att testa och förfina samarbetsarbetsflöden.
- **Lär i realtid**: Implementera feedbackloopar där agenter lär sig från interaktioner och justerar sitt beteende dynamiskt.

### Använd modulkomponenter

SDK:er som Microsoft Semantic Kernel och LangChain erbjuder förbyggda komponenter såsom AI-anslutningar, promptmallar och minneshantering.

**Hur team kan använda dessa**: Team kan snabbt sätta ihop dessa komponenter för att skapa en fungerande prototyp utan att börja från grunden, vilket möjliggör snabb experimentering och iteration.

**Hur det fungerar i praktiken**: Du kan använda en förbyggd parser för att extrahera information från användarinmatning, en minnesmodul för att lagra och hämta data, och en promptgenerator för att interagera med användare, allt utan att behöva bygga dessa komponenter från grunden.

**Exempel på kod**. Låt oss titta på exempel på hur du kan använda en förbyggd AI-anslutning med Semantic Kernel Python och .Net som använder autofunktionsanrop för att få modellen att svara på användarinmatning:

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

Vad du kan se från detta exempel är hur du kan utnyttja en förbyggd parser för att extrahera nyckelinformation från användarinmatning, såsom ursprung, destination och datum för en flygbokningsförfrågan. Denna modulära metod gör att du kan fokusera på den övergripande logiken.

### Utnyttja samarbetsverktyg

Ramverk som CrewAI, Microsoft AutoGen och Semantic Kernel underlättar skapandet av flera agenter som kan arbeta tillsammans.

**Hur team kan använda dessa**: Team kan designa agenter med specifika roller och uppgifter, vilket gör det möjligt att testa och förfina samarbetsarbetsflöden och förbättra den övergripande systemeffektiviteten.

**Hur det fungerar i praktiken**: Du kan skapa ett team av agenter där varje agent har en specialiserad funktion, såsom datainsamling, analys eller beslutsfattande. Dessa agenter kan kommunicera och dela information för att uppnå ett gemensamt mål, såsom att svara på en användarförfrågan eller slutföra en uppgift.

**Exempel på kod (AutoGen)**:

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

Vad du ser i föregående kod är hur du kan skapa en uppgift som involverar flera agenter som arbetar tillsammans för att analysera data. Varje agent utför en specifik funktion, och uppgiften utförs genom att koordinera agenterna för att uppnå önskat resultat. Genom att skapa dedikerade agenter med specialiserade roller kan du förbättra uppgiftseffektiviteten och prestandan.

### Lär i realtid

Avancerade ramverk tillhandahåller kapabiliteter för realtidskontextförståelse och anpassning.

**Hur team kan använda dessa**: Team kan implementera feedbackloopar där agenter lär sig från interaktioner och justerar sitt beteende dynamiskt, vilket leder till kontinuerlig förbättring och förfining av kapabiliteter.

**Hur det fungerar i praktiken**: Agenter kan analysera användarfeedback, miljödata och uppgiftsresultat för att uppdatera sin kunskapsbas, justera beslutsalgoritmer och förbättra prestandan över tid. Denna iterativa inlärningsprocess gör det möjligt för agenter att anpassa sig till förändrade förhållanden och användarpreferenser, vilket förbättrar den övergripande systemeffektiviteten.

## Vilka är skillnaderna mellan ramverken AutoGen, Semantic Kernel och Azure AI Agent Service?

Det finns många sätt att jämföra dessa ramverk, men låt oss titta på några nyckelskillnader när det gäller deras design, kapabiliteter och målgrupper:

## AutoGen

AutoGen är ett open-source ramverk utvecklat av Microsoft Research's AI Frontiers Lab. Det fokuserar på händelsedrivna, distribuerade *agentiska* applikationer, vilket möjliggör flera LLM:er och SLM:er, verktyg och avancerade multi-agent designmönster.

AutoGen är byggt kring kärnkonceptet agenter, som är autonoma enheter som kan uppfatta sin miljö, fatta beslut och vidta åtgärder för att uppnå specifika mål. Agenter kommunicerar via asynkrona meddelanden, vilket gör att de kan arbeta självständigt och parallellt, vilket förbättrar systemets skalbarhet och responsivitet.

<a href="https://en.wikipedia.org/wiki/Actor_model" target="_blank">Agenter är baserade på aktörsmodellen</a>. Enligt Wikipedia är en aktör _den grundläggande byggstenen för samtidig beräkning. Som svar på ett meddelande den tar emot kan en aktör: fatta lokala beslut, skapa fler aktörer, skicka fler meddelanden och bestämma hur den ska svara på nästa meddelande den tar emot_.

**Användningsområden**: Automatisering av kodgenerering, dataanalysuppgifter och byggande av skräddarsydda agenter för planerings- och forskningsfunktioner.

Här är några viktiga kärnkoncept för AutoGen:

- **Agenter**. En agent är en mjukvaruenhet som:
  - **Kommunicerar via meddelanden**, dessa meddelanden kan vara synkrona eller asynkrona.
  - **Bibehåller sin egen tillstånd**, som kan modifieras av inkommande meddelanden.
  - **Utför åtgärder** som svar på mottagna meddelanden eller förändringar i dess tillstånd. Dessa åtgärder kan modifiera agentens tillstånd och producera externa effekter, såsom att uppdatera meddelandeloggar, skicka nya meddelanden, köra kod eller göra API-anrop.
    
  Här har du en kort kodsnutt där du skapar din egen agent med chattkapabiliteter:

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
    
    I föregående kod har `MyAgent` skapats och ärver från `RoutedAgent`. Den har en meddelandehanterare som skriver ut innehållet i meddelandet och sedan skickar ett svar med hjälp av `AssistantAgent`-delegeringen. Notera särskilt hur vi tilldelar `self._delegate` en instans av `AssistantAgent`, som är en förbyggd agent som kan hantera chattkompletteringar.


    Låt oss informera AutoGen om denna agenttyp och starta programmet:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    I föregående kod registreras agenterna med runtime och sedan skickas ett meddelande till agenten, vilket resulterar i följande output:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Multi-agenter**. AutoGen stödjer skapandet av flera agenter som kan arbeta tillsammans för att uppnå komplexa uppgifter. Agenter kan kommunicera, dela information och koordinera sina åtgärder för att lösa problem mer effektivt. För att skapa ett multi-agent system kan du definiera olika typer av agenter med specialiserade funktioner och roller, såsom datainsamling, analys, beslutsfattande och användarinteraktion. Låt oss se hur en sådan skapelse ser ut så vi får en känsla av det:

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

    I föregående kod har vi en `GroupChatManager` som registreras med runtime. Denna manager ansvarar för att koordinera interaktionerna mellan olika typer av agenter, såsom författare, illustratörer, redaktörer och användare.

- **Agent Runtime**. Ramverket tillhandahåller en runtime-miljö, möjliggör kommunikation mellan agenter, hanterar deras identiteter och livscykler, och upprätthåller säkerhets- och integritetsgränser. Detta innebär att du kan köra dina agenter i en säker och kontrollerad miljö, vilket säkerställer att de kan interagera säkert och effektivt. Det finns två intressanta runtime-alternativ:
  - **Fristående runtime**. Detta är ett bra val för enkelprocessapplikationer där alla agenter implementeras i samma programmeringsspråk och körs i samma process. Här är en illustration av hur det fungerar:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-standalone.svg" target="_blank">Fristående runtime</a>   
Applikationsstack

    *agenter kommunicerar via meddelanden genom runtime, och runtime hanterar agenternas livscykel*

  - **Distribuerad agent-runtime**, är lämplig för multiprocessapplikationer där agenter kan implementeras i olika programmeringsspråk och köras på olika maskiner. Här är en illustration av hur det fungerar:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-distributed.svg" target="_blank">Distribuerad runtime</a>

## Semantic Kernel + Agent Framework

Semantic Kernel är en företagsklar AI Orchestration SDK. Den består av AI- och minnesanslutningar, tillsammans med ett Agent Framework.

Låt oss först täcka några kärnkomponenter:

- **AI-anslutningar**: Detta är ett gränssnitt med externa AI-tjänster och datakällor för användning i både Python och C#.

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

    Här har du ett enkelt exempel på hur du kan skapa en kernel och lägga till en chattkompletteringstjänst. Semantic Kernel skapar en anslutning till en extern AI-tjänst, i detta fall Azure OpenAI Chat Completion.

- **Plugins**: Dessa kapslar in funktioner som en applikation kan använda. Det finns både färdiga plugins och anpassade som du kan skapa. Ett relaterat koncept är "promptfunktioner." Istället för att ge naturliga språkledtrådar för funktionsanrop, sänder du vissa funktioner till modellen. Baserat på den aktuella chattkontexten kan modellen välja att kalla en av dessa funktioner för att slutföra en begäran eller fråga. Här är ett exempel:

  ```python
  from semantic_kernel.connectors.ai.open_ai.services.azure_chat_completion import AzureChatCompletion


  async def main():
      from semantic_kernel.functions import KernelFunctionFromPrompt
      from semantic_kernel.kernel import Kernel

      kernel = Kernel()
      kernel.add_service(AzureChatCompletion())

      user_input = input("User Input:> ")

      kernel_function = KernelFunctionFromPrompt(
          function_name="SummarizeText",
          prompt="""
          Summarize the provided unstructured text in a sentence that is easy to understand.
          Text to summarize: {{$user_input}}
          """,
      )

      response = await kernel_function.invoke(kernel=kernel, user_input=user_input)
      print(f"Model Response: {response}")

      """
      Sample Console Output:

      User Input:> I like dogs
      Model Response: The text expresses a preference for dogs.
      """


  if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
  ```

    ```csharp
    var userInput = Console.ReadLine();

    // Define semantic function inline.
    string skPrompt = @"Summarize the provided unstructured text in a sentence that is easy to understand.
                        Text to summarize: {{$userInput}}";
    
    // create the function from the prompt
    KernelFunction summarizeFunc = kernel.CreateFunctionFromPrompt(
        promptTemplate: skPrompt,
        functionName: "SummarizeText"
    );

    //then import into the current kernel
    kernel.ImportPluginFromFunctions("SemanticFunctions", [summarizeFunc]);

    ```

    Här har du först en mallprompt `skPrompt` som lämnar utrymme för användaren att mata in text, `$userInput`. Sedan skapar du kernel-funktionen `SummarizeText` och importerar den sedan till kernel med plugin-namnet `SemanticFunctions`. Notera namnet på funktionen som hjälper Semantic Kernel att förstå vad funktionen gör och när den ska kallas.

- **Native function**: Det finns också inbyggda funktioner som ramverket kan kalla direkt för att utföra uppgiften. Här är ett exempel på en sådan funktion som hämtar innehållet från en fil:

    ```csharp
    public class NativeFunctions {

        [SKFunction, Description("Retrieve content from local file")]
        public async Task<string> RetrieveLocalFile(string fileName, int maxSize = 5000)
        {
            string content = await File.ReadAllTextAsync(fileName);
            if (content.Length <= maxSize) return content;
            return content.Substring(0, maxSize);
        }
    }
    
    //Import native function
    string plugInName = "NativeFunction";
    string functionName = "RetrieveLocalFile";

   //To add the functions to a kernel use the following function
    kernel.ImportPluginFromType<NativeFunctions>();

    ```

- **Minne**: Abstraherar och förenklar kontexthantering för AI-appar. Idén med minne är att detta är något LLM bör känna till. Du kan lagra denna information i en vektorlagring som slutar vara en in-memory databas eller en vektordatabas eller liknande. Här är ett exempel på ett mycket förenklat scenario där *fakta* läggs till i minnet:

    ```csharp
    var facts = new Dictionary<string,string>();
    facts.Add(
        "Azure Machine Learning; https://learn.microsoft.com/azure/machine-learning/",
        @"Azure Machine Learning is a cloud service for accelerating and
        managing the machine learning project lifecycle. Machine learning professionals,
        data scientists, and engineers can use it in their day-to-day workflows"
    );
    
    facts.Add(
        "Azure SQL Service; https://learn.microsoft.com/azure/azure-sql/",
        @"Azure SQL is a family of managed, secure, and intelligent products
        that use the SQL Server database engine in the Azure cloud."
    );
    
    string memoryCollectionName = "SummarizedAzureDocs";
    
    foreach (var fact in facts) {
        await memoryBuilder.SaveReferenceAsync(
            collection: memoryCollectionName,
            description: fact.Key.Split(";")[1].Trim(),
            text: fact.Value,
            externalId: fact.Key.Split(";")[2].Trim(),
            externalSourceName: "Azure Documentation"
        );
    }
    ```

Dessa fakta lagras sedan i minnessamlingen `SummarizedAzureDocs`. Detta är ett mycket förenklat exempel, men du kan se hur information kan lagras i minnet för att LLM ska kunna använda det.

Så det är grunderna i Semantic Kernel-ramverket, men vad sägs om Agent Framework?

## Azure AI Agent Service

Azure AI Agent Service är en nyare tillägg, introducerad på Microsoft Ignite 2024. Det möjliggör utveckling och distribution av AI-agenter med mer flexibla modeller, såsom att direkt anropa öppna LLM:er som Llama 3, Mistral och Cohere.

Azure AI Agent Service erbjuder starkare säkerhetsmekanismer för företag och metoder för datalagring, vilket gör det lämpligt för företagsapplikationer.

Det fungerar direkt med orkestreringsramverk för flera agenter som AutoGen och Semantic Kernel.

Denna tjänst är för närvarande i Public Preview och stöder Python och C# för att bygga agenter.

Med Semantic Kernel Python kan vi skapa en Azure AI Agent med ett användardefinierat plugin:

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

### Grundläggande koncept

Azure AI Agent Service har följande grundläggande koncept:

- **Agent**. Azure AI Agent Service integreras med Azure AI Foundry. Inom AI Foundry fungerar en AI-agent som en "smart" mikrotjänst som kan användas för att besvara frågor (RAG), utföra uppgifter eller helt automatisera arbetsflöden. Den uppnår detta genom att kombinera kraften hos generativa AI-modeller med verktyg som gör det möjligt att få tillgång till och interagera med verkliga datakällor. Här är ett exempel på en agent:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    I detta exempel skapas en agent med modellen `gpt-4o-mini`, namnet `my-agent` och instruktionerna `You are helpful agent`. Agenten är utrustad med verktyg och resurser för att utföra kodtolkningsuppgifter.

- **Tråd och meddelanden**. Tråden är ett annat viktigt koncept. Den representerar en konversation eller interaktion mellan en agent och en användare. Trådar kan användas för att spåra framstegen i en konversation, lagra kontextinformation och hantera tillståndet för interaktionen. Här är ett exempel på en tråd:

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

    I den tidigare koden skapas en tråd. Därefter skickas ett meddelande till tråden. Genom att anropa `create_and_process_run` ombeds agenten att utföra arbete på tråden. Slutligen hämtas och loggas meddelandena för att se agentens svar. Meddelandena visar framstegen i konversationen mellan användaren och agenten. Det är också viktigt att förstå att meddelandena kan vara av olika typer, såsom text, bild eller fil, vilket innebär att agentens arbete har resulterat i exempelvis en bild eller ett textrespons. Som utvecklare kan du sedan använda denna information för att vidare bearbeta svaret eller presentera det för användaren.

- **Integreras med andra AI-ramverk**. Azure AI Agent Service kan interagera med andra ramverk som AutoGen och Semantic Kernel, vilket innebär att du kan bygga delar av din app i ett av dessa ramverk och till exempel använda Agent Service som en orkestrator eller bygga allt i Agent Service.

**Användningsområden**: Azure AI Agent Service är utformad för företagsapplikationer som kräver säker, skalbar och flexibel distribution av AI-agenter.

## Vad är skillnaden mellan dessa ramverk?

Det verkar som att det finns mycket överlapp mellan dessa ramverk, men det finns några viktiga skillnader när det gäller deras design, kapabiliteter och målgrupper:

- **AutoGen**: Är ett experimentellt ramverk som fokuserar på banbrytande forskning om system med flera agenter. Det är den bästa platsen för att experimentera och prototypa sofistikerade system med flera agenter.
- **Semantic Kernel**: Är ett produktionsklart agentbibliotek för att bygga företagsapplikationer med agenter. Fokuserar på händelsedrivna, distribuerade applikationer med agenter, vilket möjliggör flera LLM:er och SLM:er, verktyg och designmönster för enskilda/flera agenter.
- **Azure AI Agent Service**: Är en plattform och distributionstjänst i Azure Foundry för agenter. Den erbjuder anslutning till tjänster som stöds av Azure Foundry, såsom Azure OpenAI, Azure AI Search, Bing Search och kodexekvering.

Fortfarande osäker på vilken du ska välja?

### Användningsområden

Låt oss se om vi kan hjälpa dig genom att gå igenom några vanliga användningsområden:

> Q: Jag experimenterar, lär mig och bygger proof-of-concept-applikationer med agenter, och jag vill kunna bygga och experimentera snabbt
>

>A: AutoGen skulle vara ett bra val för detta scenario, eftersom det fokuserar på händelsedrivna, distribuerade applikationer med agenter och stöder avancerade designmönster för flera agenter.

> Q: Vad gör AutoGen till ett bättre val än Semantic Kernel och Azure AI Agent Service för detta användningsområde?
>
> A: AutoGen är specifikt utformat för händelsedrivna, distribuerade applikationer med agenter, vilket gör det väl lämpat för att automatisera kodgenerering och dataanalysuppgifter. Det erbjuder de nödvändiga verktygen och kapabiliteterna för att bygga komplexa system med flera agenter effektivt.

>Q: Det låter som att Azure AI Agent Service också skulle fungera här, det har verktyg för kodgenerering och mer?

>
> A: Ja, Azure AI Agent Service är en plattformstjänst för agenter och har inbyggda kapabiliteter för flera modeller, Azure AI Search, Bing Search och Azure Functions. Det gör det enkelt att bygga dina agenter i Foundry Portal och distribuera dem i stor skala.

> Q: Jag är fortfarande förvirrad, ge mig bara ett alternativ
>
> A: Ett bra val är att bygga din applikation i Semantic Kernel först och sedan använda Azure AI Agent Service för att distribuera din agent. Denna metod gör det enkelt att bevara dina agenter samtidigt som du utnyttjar kraften att bygga system med flera agenter i Semantic Kernel. Dessutom har Semantic Kernel en anslutning i AutoGen, vilket gör det enkelt att använda båda ramverken tillsammans.

Låt oss sammanfatta de viktigaste skillnaderna i en tabell:

| Ramverk | Fokus | Grundläggande koncept | Användningsområden |
| --- | --- | --- | --- |
| AutoGen | Händelsedrivna, distribuerade applikationer med agenter | Agenter, Personas, Funktioner, Data | Kodgenerering, dataanalysuppgifter |
| Semantic Kernel | Förstå och generera mänskligt liknande textinnehåll | Agenter, Modulära komponenter, Samarbete | Naturlig språkförståelse, innehållsgenerering |
| Azure AI Agent Service | Flexibla modeller, företagsäkerhet, Kodgenerering, Verktygsanrop | Modularitet, Samarbete, Processorkestrering | Säker, skalbar och flexibel distribution av AI-agenter |

Vad är det ideala användningsområdet för vart och ett av dessa ramverk?

## Kan jag integrera mina befintliga Azure-verktyg direkt, eller behöver jag fristående lösningar?

Svaret är ja, du kan integrera dina befintliga Azure-verktyg direkt med Azure AI Agent Service, särskilt eftersom det har byggts för att fungera sömlöst med andra Azure-tjänster. Du kan till exempel integrera Bing, Azure AI Search och Azure Functions. Det finns också en djup integration med Azure AI Foundry.

För AutoGen och Semantic Kernel kan du också integrera med Azure-tjänster, men det kan kräva att du anropar Azure-tjänster från din kod. Ett annat sätt att integrera är att använda Azure SDK:er för att interagera med Azure-tjänster från dina agenter. Dessutom, som nämnts, kan du använda Azure AI Agent Service som en orkestrator för dina agenter byggda i AutoGen eller Semantic Kernel, vilket skulle ge enkel åtkomst till Azure-ekosystemet.

## Exempelkoder

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Har du fler frågor om AI Agent Frameworks?

Gå med i [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) för att träffa andra lärande, delta i öppet hus och få svar på dina frågor om AI-agenter.

## Referenser

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/" target="_blank">Semantic Kernel och AutoGen</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-python" target="_blank">Semantic Kernel Python Agent Framework</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp" target="_blank">Semantic Kernel .Net Agent Framework</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>
- <a href="https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121" target="_blank">Använda Azure AI Agent Service med AutoGen / Semantic Kernel för att bygga en lösning med flera agenter</a>

## Föregående lektion

[Introduktion till AI-agenter och användningsområden](../01-intro-to-ai-agents/README.md)

## Nästa lektion

[Förstå designmönster för agenter](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->