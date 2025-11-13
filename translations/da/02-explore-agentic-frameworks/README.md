<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7120197753abacc827b64ac2d5d6966f",
  "translation_date": "2025-11-13T12:48:53+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "da"
}
-->
[![Udforsk AI Agent Frameworks](../../../translated_images/lesson-2-thumbnail.c65f44c93b8558df4d5d407e29970e654629e614f357444a9c27c80feb54c79d.da.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Klik på billedet ovenfor for at se videoen til denne lektion)_

# Udforsk AI Agent Frameworks

AI agent frameworks er softwareplatforme designet til at forenkle oprettelse, implementering og styring af AI-agenter. Disse frameworks giver udviklere forudbyggede komponenter, abstraktioner og værktøjer, der gør det lettere at udvikle komplekse AI-systemer.

Disse frameworks hjælper udviklere med at fokusere på de unikke aspekter af deres applikationer ved at tilbyde standardiserede løsninger på almindelige udfordringer inden for AI-agentudvikling. De forbedrer skalerbarhed, tilgængelighed og effektivitet i opbygningen af AI-systemer.

## Introduktion 

Denne lektion vil dække:

- Hvad er AI Agent Frameworks, og hvad gør de det muligt for udviklere at opnå?
- Hvordan kan teams bruge dem til hurtigt at prototype, iterere og forbedre deres agents kapaciteter?
- Hvad er forskellene mellem de frameworks og værktøjer, der er skabt af Microsoft <a href="https://aka.ms/ai-agents/autogen" target="_blank">AutoGen</a>, <a href="https://aka.ms/ai-agents-beginners/semantic-kernel" target="_blank">Semantic Kernel</a>, og <a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a>?
- Kan jeg integrere mine eksisterende Azure-økosystemværktøjer direkte, eller har jeg brug for selvstændige løsninger?
- Hvad er Azure AI Agents service, og hvordan hjælper det mig?

## Læringsmål

Målene med denne lektion er at hjælpe dig med at forstå:

- AI Agent Frameworks' rolle i AI-udvikling.
- Hvordan man udnytter AI Agent Frameworks til at bygge intelligente agenter.
- Nøglefunktioner, der muliggøres af AI Agent Frameworks.
- Forskellene mellem AutoGen, Semantic Kernel og Azure AI Agent Service.

## Hvad er AI Agent Frameworks, og hvad gør de det muligt for udviklere at gøre?

Traditionelle AI Frameworks kan hjælpe dig med at integrere AI i dine apps og forbedre disse apps på følgende måder:

- **Personalisering**: AI kan analysere brugeradfærd og præferencer for at give personlige anbefalinger, indhold og oplevelser.
Eksempel: Streamingtjenester som Netflix bruger AI til at foreslå film og serier baseret på visningshistorik, hvilket øger brugerengagement og tilfredshed.
- **Automatisering og effektivitet**: AI kan automatisere gentagne opgaver, strømline arbejdsgange og forbedre operationel effektivitet.
Eksempel: Kundeserviceapps bruger AI-drevne chatbots til at håndtere almindelige forespørgsler, reducere svartider og frigøre menneskelige agenter til mere komplekse problemer.
- **Forbedret brugeroplevelse**: AI kan forbedre den samlede brugeroplevelse ved at tilbyde intelligente funktioner som stemmegenkendelse, naturlig sprogbehandling og forudsigende tekst.
Eksempel: Virtuelle assistenter som Siri og Google Assistant bruger AI til at forstå og reagere på stemmekommandoer, hvilket gør det lettere for brugere at interagere med deres enheder.

### Det lyder alt sammen godt, ikke? Så hvorfor har vi brug for AI Agent Frameworks?

AI Agent Frameworks repræsenterer noget mere end blot AI frameworks. De er designet til at muliggøre oprettelsen af intelligente agenter, der kan interagere med brugere, andre agenter og miljøet for at opnå specifikke mål. Disse agenter kan udvise autonom adfærd, træffe beslutninger og tilpasse sig skiftende forhold. Lad os se på nogle nøglefunktioner, der muliggøres af AI Agent Frameworks:

- **Agent-samarbejde og koordinering**: Muliggør oprettelsen af flere AI-agenter, der kan arbejde sammen, kommunikere og koordinere for at løse komplekse opgaver.
- **Automatisering og opgavestyring**: Tilbyder mekanismer til automatisering af flertrins arbejdsgange, opgavefordeling og dynamisk opgavestyring blandt agenter.
- **Kontekstforståelse og tilpasning**: Udstyrer agenter med evnen til at forstå kontekst, tilpasse sig skiftende miljøer og træffe beslutninger baseret på realtidsinformation.

Så kort sagt giver agenter dig mulighed for at gøre mere, tage automatisering til næste niveau og skabe mere intelligente systemer, der kan tilpasse sig og lære af deres miljø.

## Hvordan hurtigt prototype, iterere og forbedre agentens kapaciteter?

Dette er et hurtigt udviklende område, men der er nogle ting, der er fælles for de fleste AI Agent Frameworks, som kan hjælpe dig med hurtigt at prototype og iterere, nemlig modulkomponenter, samarbejdsværktøjer og realtidslæring. Lad os dykke ned i disse:

- **Brug modulkomponenter**: AI SDK'er tilbyder forudbyggede komponenter som AI- og hukommelsesforbindelser, funktionkald ved hjælp af naturligt sprog eller kodeplugins, promptskabeloner og mere.
- **Udnyt samarbejdsværktøjer**: Design agenter med specifikke roller og opgaver, hvilket gør det muligt at teste og forfine samarbejdsarbejdsgange.
- **Lær i realtid**: Implementer feedbacksløjfer, hvor agenter lærer af interaktioner og justerer deres adfærd dynamisk.

### Brug modulkomponenter

SDK'er som Microsoft Semantic Kernel og LangChain tilbyder forudbyggede komponenter som AI-forbindelser, promptskabeloner og hukommelsesstyring.

**Hvordan teams kan bruge disse**: Teams kan hurtigt samle disse komponenter for at skabe en funktionel prototype uden at starte fra bunden, hvilket muliggør hurtig eksperimentering og iteration.

**Hvordan det fungerer i praksis**: Du kan bruge en forudbygget parser til at udtrække information fra brugerinput, en hukommelsesmodul til at gemme og hente data og en promptgenerator til at interagere med brugere, alt sammen uden at skulle bygge disse komponenter fra bunden.

**Eksempelkode**. Lad os se på eksempler på, hvordan du kan bruge en forudbygget AI Connector med Semantic Kernel Python og .Net, der bruger auto-funktionskald til at få modellen til at reagere på brugerinput:

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

Hvad du kan se fra dette eksempel er, hvordan du kan udnytte en forudbygget parser til at udtrække nøgleinformation fra brugerinput, såsom oprindelse, destination og dato for en flybookingforespørgsel. Denne modulære tilgang giver dig mulighed for at fokusere på den overordnede logik.

### Udnyt samarbejdsværktøjer

Frameworks som CrewAI, Microsoft AutoGen og Semantic Kernel gør det muligt at oprette flere agenter, der kan arbejde sammen.

**Hvordan teams kan bruge disse**: Teams kan designe agenter med specifikke roller og opgaver, hvilket gør det muligt at teste og forfine samarbejdsarbejdsgange og forbedre den samlede systemeffektivitet.

**Hvordan det fungerer i praksis**: Du kan oprette et team af agenter, hvor hver agent har en specialiseret funktion, såsom datahentning, analyse eller beslutningstagning. Disse agenter kan kommunikere og dele information for at opnå et fælles mål, såsom at besvare en brugerforespørgsel eller fuldføre en opgave.

**Eksempelkode (AutoGen)**:

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

Hvad du ser i den tidligere kode er, hvordan du kan oprette en opgave, der involverer flere agenter, der arbejder sammen for at analysere data. Hver agent udfører en specifik funktion, og opgaven udføres ved at koordinere agenterne for at opnå det ønskede resultat. Ved at oprette dedikerede agenter med specialiserede roller kan du forbedre opgaveeffektiviteten og ydeevnen.

### Lær i realtid

Avancerede frameworks giver muligheder for realtids kontekstforståelse og tilpasning.

**Hvordan teams kan bruge disse**: Teams kan implementere feedbacksløjfer, hvor agenter lærer af interaktioner og justerer deres adfærd dynamisk, hvilket fører til kontinuerlig forbedring og forfining af kapaciteter.

**Hvordan det fungerer i praksis**: Agenter kan analysere brugerfeedback, miljødata og opgaveudfald for at opdatere deres vidensbase, justere beslutningsalgoritmer og forbedre ydeevnen over tid. Denne iterative læringsproces gør det muligt for agenter at tilpasse sig skiftende forhold og brugerpræferencer, hvilket forbedrer den samlede systemeffektivitet.

## Hvad er forskellene mellem frameworks AutoGen, Semantic Kernel og Azure AI Agent Service?

Der er mange måder at sammenligne disse frameworks på, men lad os se på nogle nøgleforskelle med hensyn til deres design, kapaciteter og målgrupper:

## AutoGen

AutoGen er et open-source framework udviklet af Microsoft Research's AI Frontiers Lab. Det fokuserer på hændelsesdrevne, distribuerede *agentiske* applikationer, der muliggør flere LLM'er og SLM'er, værktøjer og avancerede multi-agent designmønstre.

AutoGen er bygget omkring kernekonceptet agenter, som er autonome enheder, der kan opfatte deres miljø, træffe beslutninger og tage handlinger for at opnå specifikke mål. Agenter kommunikerer via asynkrone beskeder, hvilket gør det muligt for dem at arbejde uafhængigt og parallelt, hvilket forbedrer systemets skalerbarhed og responsivitet.

<a href="https://en.wikipedia.org/wiki/Actor_model" target="_blank">Agenter er baseret på aktørmodellen</a>. Ifølge Wikipedia er en aktør _den grundlæggende byggesten for samtidig beregning. Som svar på en besked, den modtager, kan en aktør: træffe lokale beslutninger, oprette flere aktører, sende flere beskeder og bestemme, hvordan den skal reagere på den næste besked, den modtager_.

**Anvendelsesområder**: Automatisering af kodegenerering, dataanalysetasks og opbygning af brugerdefinerede agenter til planlægnings- og forskningsfunktioner.

Her er nogle vigtige kernekoncepter i AutoGen:

- **Agenter**. En agent er en softwareenhed, der:
  - **Kommunikerer via beskeder**, disse beskeder kan være synkrone eller asynkrone.
  - **Vedligeholder sin egen tilstand**, som kan ændres af indkommende beskeder.
  - **Udfører handlinger** som svar på modtagne beskeder eller ændringer i dens tilstand. Disse handlinger kan ændre agentens tilstand og producere eksterne effekter, såsom opdatering af beskedlogfiler, afsendelse af nye beskeder, udførelse af kode eller foretage API-kald.
    
  Her har du en kort kodeeksempel, hvor du opretter din egen agent med chatfunktioner:

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
    
    I den tidligere kode er `MyAgent` blevet oprettet og arver fra `RoutedAgent`. Den har en beskedhåndterer, der udskriver indholdet af beskeden og derefter sender et svar ved hjælp af `AssistantAgent`-delegeringen. Bemærk især, hvordan vi tildeler `self._delegate` en instans af `AssistantAgent`, som er en forudbygget agent, der kan håndtere chatkompletteringer.


    Lad os informere AutoGen om denne agenttype og starte programmet:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    I den tidligere kode registreres agenterne med runtime, og derefter sendes en besked til agenten, hvilket resulterer i følgende output:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Multi-agenter**. AutoGen understøtter oprettelsen af flere agenter, der kan arbejde sammen for at opnå komplekse opgaver. Agenter kan kommunikere, dele information og koordinere deres handlinger for at løse problemer mere effektivt. For at oprette et multi-agent system kan du definere forskellige typer agenter med specialiserede funktioner og roller, såsom datahentning, analyse, beslutningstagning og brugerinteraktion. Lad os se, hvordan en sådan oprettelse ser ud, så vi får en fornemmelse af det:

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

    I den tidligere kode har vi en `GroupChatManager`, der er registreret med runtime. Denne manager er ansvarlig for at koordinere interaktionerne mellem forskellige typer agenter, såsom forfattere, illustratorer, redaktører og brugere.

- **Agent Runtime**. Frameworket giver et runtime-miljø, der muliggør kommunikation mellem agenter, administrerer deres identiteter og livscyklusser og håndhæver sikkerheds- og privatlivsgrænser. Dette betyder, at du kan køre dine agenter i et sikkert og kontrolleret miljø, hvilket sikrer, at de kan interagere sikkert og effektivt. Der er to runtime-miljøer af interesse:
  - **Stand-alone runtime**. Dette er et godt valg for enkeltprocesapplikationer, hvor alle agenter er implementeret i det samme programmeringssprog og kører i den samme proces. Her er en illustration af, hvordan det fungerer:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-standalone.svg" target="_blank">Stand-alone runtime</a>   
Applikationsstak

    *agenter kommunikerer via beskeder gennem runtime, og runtime administrerer agenternes livscyklus*

  - **Distribueret agent runtime**, er velegnet til multiprocesapplikationer, hvor agenter kan være implementeret i forskellige programmeringssprog og køre på forskellige maskiner. Her er en illustration af, hvordan det fungerer:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-distributed.svg" target="_blank">Distribueret runtime</a>

## Semantic Kernel + Agent Framework

Semantic Kernel er en virksomheds-klar AI Orchestration SDK. Det består af AI- og hukommelsesforbindelser sammen med et Agent Framework.

Lad os først dække nogle kernekomponenter:

- **AI Connectors**: Dette er en grænseflade til eksterne AI-tjenester og datakilder til brug i både Python og C#.

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

    Her har du et simpelt eksempel på, hvordan du kan oprette en kernel og tilføje en chatkompletteringstjeneste. Semantic Kernel opretter en forbindelse til en ekstern AI-tjeneste, i dette tilfælde Azure OpenAI Chat Completion.

- **Plugins**: Disse indkapsler funktioner, som en applikation kan bruge. Der er både færdiglavede plugins og brugerdefinerede, som du kan oprette. Et relateret koncept er "prompt-funktioner." I stedet for at give naturlige sprogkoder til funktionskald, udsender du visse funktioner til modellen. Baseret på den aktuelle chatkontekst kan modellen vælge at kalde en af disse funktioner for at fuldføre en anmodning eller forespørgsel. Her er et eksempel:

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

    Her har du først en skabelonprompt `skPrompt`, der giver plads til brugerens inputtekst, `$userInput`. Derefter opretter du kernel-funktionen `SummarizeText` og importerer den derefter i kernel med plugin-navnet `SemanticFunctions`. Bemærk navnet på funktionen, der hjælper Semantic Kernel med at forstå, hvad funktionen gør, og hvornår den skal kaldes.

- **Native funktion**: Der er også native funktioner, som frameworket kan kalde direkte for at udføre opgaven. Her er et eksempel på en sådan funktion, der henter indholdet fra en fil:

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

- **Hukommelse**: Abstraherer og forenkler kontekststyring for AI-apps. Ideen med hukommelse er, at dette er noget, LLM'en bør vide om. Du kan gemme denne information i en vektorstore, som ender med at være en in-memory database eller en vektordatabase eller lignende. Her er et eksempel på et meget forenklet scenarie, hvor *fakta* tilføjes til hukommelsen:

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

Disse fakta gemmes derefter i hukommelsessamlingen `SummarizedAzureDocs`. Dette er et meget forenklet eksempel, men du kan se, hvordan du kan gemme information i hukommelsen, som LLM kan bruge.

Så det er grundlæggende om Semantic Kernel-frameworket, hvad med Agent Framework?

## Azure AI Agent Service

Azure AI Agent Service er en nyere tilføjelse, introduceret på Microsoft Ignite 2024. Det giver mulighed for udvikling og implementering af AI-agenter med mere fleksible modeller, såsom direkte kald til open-source LLM'er som Llama 3, Mistral og Cohere.

Azure AI Agent Service tilbyder stærkere sikkerhedsmekanismer og metoder til datalagring, hvilket gør det velegnet til virksomhedsapplikationer.

Det fungerer direkte med multi-agent orkestreringsframeworks som AutoGen og Semantic Kernel.

Denne service er i øjeblikket i Public Preview og understøtter Python og C# til opbygning af agenter.

Ved hjælp af Semantic Kernel Python kan vi oprette en Azure AI Agent med et brugerdefineret plugin:

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

### Kernekoncepter

Azure AI Agent Service har følgende kernekoncepter:

- **Agent**. Azure AI Agent Service integreres med Azure AI Foundry. Inden for AI Foundry fungerer en AI Agent som en "intelligent" mikrotjeneste, der kan bruges til at besvare spørgsmål (RAG), udføre handlinger eller fuldstændigt automatisere arbejdsprocesser. Det opnår dette ved at kombinere kraften fra generative AI-modeller med værktøjer, der giver det mulighed for at få adgang til og interagere med virkelige datakilder. Her er et eksempel på en agent:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    I dette eksempel oprettes en agent med modellen `gpt-4o-mini`, et navn `my-agent` og instruktioner `You are helpful agent`. Agenten er udstyret med værktøjer og ressourcer til at udføre opgaver som kodefortolkning.

- **Tråd og beskeder**. Tråden er et andet vigtigt koncept. Den repræsenterer en samtale eller interaktion mellem en agent og en bruger. Tråde kan bruges til at spore fremskridt i en samtale, gemme kontekstinformation og administrere tilstanden af interaktionen. Her er et eksempel på en tråd:

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

    I den tidligere kode oprettes en tråd. Derefter sendes en besked til tråden. Ved at kalde `create_and_process_run` bliver agenten bedt om at udføre arbejde på tråden. Til sidst hentes og logges beskederne for at se agentens svar. Beskederne angiver fremskridtene i samtalen mellem brugeren og agenten. Det er også vigtigt at forstå, at beskederne kan være af forskellige typer såsom tekst, billede eller fil, hvilket betyder, at agentens arbejde har resulteret i for eksempel et billede eller et tekstsvar. Som udvikler kan du derefter bruge denne information til yderligere at behandle svaret eller præsentere det for brugeren.

- **Integration med andre AI-frameworks**. Azure AI Agent Service kan interagere med andre frameworks som AutoGen og Semantic Kernel, hvilket betyder, at du kan bygge dele af din app i et af disse frameworks og for eksempel bruge Agent Service som en orkestrator, eller du kan bygge alt i Agent Service.

**Anvendelsesområder**: Azure AI Agent Service er designet til virksomhedsapplikationer, der kræver sikker, skalerbar og fleksibel AI-agent implementering.

## Hvad er forskellen mellem disse frameworks?

Det lyder som om, der er meget overlap mellem disse frameworks, men der er nogle nøgleforskelle i forhold til deres design, kapaciteter og målgrupper:

- **AutoGen**: Er et eksperimenteringsframework fokuseret på banebrydende forskning inden for multi-agent systemer. Det er det bedste sted at eksperimentere og prototype avancerede multi-agent systemer.
- **Semantic Kernel**: Er et produktionsklart agentbibliotek til opbygning af virksomhedsagentiske applikationer. Fokuserer på hændelsesdrevne, distribuerede agentiske applikationer, der muliggør flere LLM'er og SLM'er, værktøjer og enkelt-/multi-agent designmønstre.
- **Azure AI Agent Service**: Er en platform og implementeringstjeneste i Azure Foundry for agenter. Det tilbyder opbygning af forbindelser til tjenester understøttet af Azure Foundry som Azure OpenAI, Azure AI Search, Bing Search og kodeudførelse.

Stadig ikke sikker på, hvilken du skal vælge?

### Anvendelsesområder

Lad os se, om vi kan hjælpe dig ved at gennemgå nogle almindelige anvendelsesområder:

> Q: Jeg eksperimenterer, lærer og bygger proof-of-concept agentapplikationer, og jeg vil kunne bygge og eksperimentere hurtigt
>

>A: AutoGen ville være et godt valg til dette scenarie, da det fokuserer på hændelsesdrevne, distribuerede agentiske applikationer og understøtter avancerede multi-agent designmønstre.

> Q: Hvad gør AutoGen til et bedre valg end Semantic Kernel og Azure AI Agent Service til dette anvendelsesområde?
>
> A: AutoGen er specifikt designet til hændelsesdrevne, distribuerede agentiske applikationer, hvilket gør det velegnet til automatisering af kodegenerering og dataanalyseopgaver. Det giver de nødvendige værktøjer og kapaciteter til effektivt at bygge komplekse multi-agent systemer.

>Q: Det lyder som om Azure AI Agent Service også kunne fungere her, det har værktøjer til kodegenerering og mere?

>
> A: Ja, Azure AI Agent Service er en platformtjeneste for agenter og tilføjer indbyggede kapaciteter for flere modeller, Azure AI Search, Bing Search og Azure Functions. Det gør det nemt at bygge dine agenter i Foundry Portal og implementere dem i stor skala.

> Q: Jeg er stadig forvirret, giv mig bare én mulighed
>
> A: Et godt valg er at bygge din applikation i Semantic Kernel først og derefter bruge Azure AI Agent Service til at implementere din agent. Denne tilgang giver dig mulighed for nemt at gemme dine agenter, mens du udnytter kraften til at bygge multi-agent systemer i Semantic Kernel. Derudover har Semantic Kernel en connector i AutoGen, hvilket gør det nemt at bruge begge frameworks sammen.

Lad os opsummere de vigtigste forskelle i en tabel:

| Framework | Fokus | Kernekoncepter | Anvendelsesområder |
| --- | --- | --- | --- |
| AutoGen | Hændelsesdrevne, distribuerede agentiske applikationer | Agenter, Personas, Funktioner, Data | Kodegenerering, dataanalyseopgaver |
| Semantic Kernel | Forståelse og generering af menneskelignende tekstindhold | Agenter, Moduler, Samarbejde | Naturlig sprogforståelse, indholdsgenerering |
| Azure AI Agent Service | Fleksible modeller, virksomhedsikkerhed, Kodegenerering, Værktøjskald | Modularitet, Samarbejde, Procesorkestrering | Sikker, skalerbar og fleksibel AI-agent implementering |

Hvad er det ideelle anvendelsesområde for hver af disse frameworks?

## Kan jeg integrere mine eksisterende Azure-økosystemværktøjer direkte, eller har jeg brug for selvstændige løsninger?

Svaret er ja, du kan integrere dine eksisterende Azure-økosystemværktøjer direkte med Azure AI Agent Service, især fordi det er bygget til at fungere problemfrit med andre Azure-tjenester. Du kunne for eksempel integrere Bing, Azure AI Search og Azure Functions. Der er også dyb integration med Azure AI Foundry.

For AutoGen og Semantic Kernel kan du også integrere med Azure-tjenester, men det kan kræve, at du kalder Azure-tjenester fra din kode. En anden måde at integrere på er at bruge Azure SDK'er til at interagere med Azure-tjenester fra dine agenter. Derudover, som nævnt, kan du bruge Azure AI Agent Service som en orkestrator for dine agenter bygget i AutoGen eller Semantic Kernel, hvilket giver nem adgang til Azure-økosystemet.

## Eksempelkoder

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Har du flere spørgsmål om AI Agent Frameworks?

Deltag i [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) for at møde andre lærende, deltage i kontortimer og få svar på dine spørgsmål om AI-agenter.

## Referencer

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/" target="_blank">Semantic Kernel og AutoGen</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-python" target="_blank">Semantic Kernel Python Agent Framework</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp" target="_blank">Semantic Kernel .Net Agent Framework</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>
- <a href="https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121" target="_blank">Brug af Azure AI Agent Service med AutoGen / Semantic Kernel til at bygge en multi-agent løsning</a>

## Forrige Lektion

[Introduktion til AI-agenter og anvendelsesområder](../01-intro-to-ai-agents/README.md)

## Næste Lektion

[Forståelse af agentiske designmønstre](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->