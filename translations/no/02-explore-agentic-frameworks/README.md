<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7120197753abacc827b64ac2d5d6966f",
  "translation_date": "2025-11-13T12:53:26+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "no"
}
-->
[![Utforsker AI-agentrammeverk](../../../translated_images/lesson-2-thumbnail.c65f44c93b8558df4d5d407e29970e654629e614f357444a9c27c80feb54c79d.no.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Klikk på bildet ovenfor for å se videoen til denne leksjonen)_

# Utforsk AI-agentrammeverk

AI-agentrammeverk er programvareplattformer designet for å forenkle opprettelse, distribusjon og administrasjon av AI-agenter. Disse rammeverkene gir utviklere forhåndsbygde komponenter, abstraksjoner og verktøy som effektiviserer utviklingen av komplekse AI-systemer.

Disse rammeverkene hjelper utviklere med å fokusere på de unike aspektene ved applikasjonene sine ved å tilby standardiserte tilnærminger til vanlige utfordringer i utviklingen av AI-agenter. De forbedrer skalerbarhet, tilgjengelighet og effektivitet i byggingen av AI-systemer.

## Introduksjon 

Denne leksjonen vil dekke:

- Hva er AI-agentrammeverk, og hva gjør de det mulig for utviklere å oppnå?
- Hvordan kan team bruke disse til raskt å prototype, iterere og forbedre agentens evner?
- Hva er forskjellene mellom rammeverkene og verktøyene laget av Microsoft <a href="https://aka.ms/ai-agents/autogen" target="_blank">AutoGen</a>, <a href="https://aka.ms/ai-agents-beginners/semantic-kernel" target="_blank">Semantic Kernel</a>, og <a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a>?
- Kan jeg integrere mine eksisterende Azure-økosystemverktøy direkte, eller trenger jeg frittstående løsninger?
- Hva er Azure AI Agents-tjenesten, og hvordan hjelper den meg?

## Læringsmål

Målene med denne leksjonen er å hjelpe deg med å forstå:

- Rollen til AI-agentrammeverk i AI-utvikling.
- Hvordan utnytte AI-agentrammeverk for å bygge intelligente agenter.
- Nøkkelfunksjoner muliggjort av AI-agentrammeverk.
- Forskjellene mellom AutoGen, Semantic Kernel og Azure AI Agent Service.

## Hva er AI-agentrammeverk, og hva gjør de det mulig for utviklere å gjøre?

Tradisjonelle AI-rammeverk kan hjelpe deg med å integrere AI i appene dine og gjøre disse appene bedre på følgende måter:

- **Personalisering**: AI kan analysere brukeradferd og preferanser for å gi personlige anbefalinger, innhold og opplevelser.
Eksempel: Strømmetjenester som Netflix bruker AI til å foreslå filmer og serier basert på visningshistorikk, noe som øker brukerengasjement og tilfredshet.
- **Automatisering og effektivitet**: AI kan automatisere repeterende oppgaver, effektivisere arbeidsflyter og forbedre operasjonell effektivitet.
Eksempel: Kundeserviceapper bruker AI-drevne chatboter til å håndtere vanlige forespørsler, redusere responstider og frigjøre menneskelige agenter for mer komplekse problemer.
- **Forbedret brukeropplevelse**: AI kan forbedre den generelle brukeropplevelsen ved å tilby intelligente funksjoner som stemmegjenkjenning, naturlig språkbehandling og prediktiv tekst.
Eksempel: Virtuelle assistenter som Siri og Google Assistant bruker AI til å forstå og svare på stemmekommandoer, noe som gjør det enklere for brukere å samhandle med enhetene sine.

### Det høres flott ut, ikke sant? Så hvorfor trenger vi AI-agentrammeverk?

AI-agentrammeverk representerer noe mer enn bare AI-rammeverk. De er designet for å muliggjøre opprettelsen av intelligente agenter som kan samhandle med brukere, andre agenter og miljøet for å oppnå spesifikke mål. Disse agentene kan utvise autonom oppførsel, ta beslutninger og tilpasse seg endrede forhold. La oss se på noen nøkkelfunksjoner muliggjort av AI-agentrammeverk:

- **Agent-samarbeid og koordinering**: Muliggjør opprettelsen av flere AI-agenter som kan samarbeide, kommunisere og koordinere for å løse komplekse oppgaver.
- **Oppgaveautomatisering og -administrasjon**: Gir mekanismer for å automatisere flertrinns arbeidsflyter, oppgdelegasjon og dynamisk oppgaveadministrasjon blant agenter.
- **Kontekstuell forståelse og tilpasning**: Utstyrer agenter med evnen til å forstå kontekst, tilpasse seg endrede miljøer og ta beslutninger basert på sanntidsinformasjon.

Så oppsummert lar agenter deg gjøre mer, ta automatisering til neste nivå, og skape mer intelligente systemer som kan tilpasse seg og lære av miljøet sitt.

## Hvordan raskt prototype, iterere og forbedre agentens evner?

Dette er et landskap i rask utvikling, men det er noen ting som er felles for de fleste AI-agentrammeverk som kan hjelpe deg med å raskt prototype og iterere, nemlig modulkomponenter, samarbeidsverktøy og sanntidslæring. La oss dykke inn i disse:

- **Bruk modulkomponenter**: AI SDK-er tilbyr forhåndsbygde komponenter som AI- og minnekoblinger, funksjonskall ved bruk av naturlig språk eller kodeplugins, promptmaler og mer.
- **Utnytt samarbeidsverktøy**: Design agenter med spesifikke roller og oppgaver, slik at de kan teste og forbedre samarbeidsarbeidsflyter.
- **Lær i sanntid**: Implementer tilbakemeldingssløyfer der agenter lærer av interaksjoner og justerer oppførselen dynamisk.

### Bruk modulkomponenter

SDK-er som Microsoft Semantic Kernel og LangChain tilbyr forhåndsbygde komponenter som AI-koblinger, promptmaler og minnehåndtering.

**Hvordan team kan bruke disse**: Team kan raskt sette sammen disse komponentene for å lage en funksjonell prototype uten å starte fra bunnen av, noe som muliggjør rask eksperimentering og iterasjon.

**Hvordan det fungerer i praksis**: Du kan bruke en forhåndsbygd parser for å trekke ut informasjon fra brukerinput, en minnemodul for å lagre og hente data, og en promptgenerator for å samhandle med brukere, alt uten å måtte bygge disse komponentene fra bunnen av.

**Eksempelkode**. La oss se på eksempler på hvordan du kan bruke en forhåndsbygd AI-kobling med Semantic Kernel Python og .Net som bruker autofunksjonskall for å få modellen til å svare på brukerinput:

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

Det du kan se fra dette eksemplet er hvordan du kan utnytte en forhåndsbygd parser for å trekke ut nøkkelinformasjon fra brukerinput, som opprinnelse, destinasjon og dato for en flybestillingsforespørsel. Denne modulære tilnærmingen lar deg fokusere på den overordnede logikken.

### Utnytt samarbeidsverktøy

Rammeverk som CrewAI, Microsoft AutoGen og Semantic Kernel legger til rette for opprettelsen av flere agenter som kan samarbeide.

**Hvordan team kan bruke disse**: Team kan designe agenter med spesifikke roller og oppgaver, slik at de kan teste og forbedre samarbeidsarbeidsflyter og forbedre den generelle systemeffektiviteten.

**Hvordan det fungerer i praksis**: Du kan opprette et team av agenter der hver agent har en spesialisert funksjon, som datainnhenting, analyse eller beslutningstaking. Disse agentene kan kommunisere og dele informasjon for å oppnå et felles mål, som å svare på en brukerforespørsel eller fullføre en oppgave.

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

Det du ser i den forrige koden er hvordan du kan opprette en oppgave som involverer flere agenter som samarbeider om å analysere data. Hver agent utfører en spesifikk funksjon, og oppgaven utføres ved å koordinere agentene for å oppnå ønsket resultat. Ved å opprette dedikerte agenter med spesialiserte roller kan du forbedre oppgaveeffektiviteten og ytelsen.

### Lær i sanntid

Avanserte rammeverk gir muligheter for sanntidsforståelse av kontekst og tilpasning.

**Hvordan team kan bruke disse**: Team kan implementere tilbakemeldingssløyfer der agenter lærer av interaksjoner og justerer oppførselen dynamisk, noe som fører til kontinuerlig forbedring og raffinering av evner.

**Hvordan det fungerer i praksis**: Agenter kan analysere brukerfeedback, miljødata og oppgaveutfall for å oppdatere kunnskapsbasen, justere beslutningsalgoritmer og forbedre ytelsen over tid. Denne iterative læringsprosessen gjør det mulig for agenter å tilpasse seg endrede forhold og brukerpreferanser, noe som forbedrer den generelle systemeffektiviteten.

## Hva er forskjellene mellom rammeverkene AutoGen, Semantic Kernel og Azure AI Agent Service?

Det finnes mange måter å sammenligne disse rammeverkene på, men la oss se på noen nøkkelforskjeller når det gjelder deres design, funksjoner og målgrupper:

## AutoGen

AutoGen er et åpen kildekode-rammeverk utviklet av Microsoft Research's AI Frontiers Lab. Det fokuserer på hendelsesdrevne, distribuerte *agentiske* applikasjoner, som muliggjør flere LLM-er og SLM-er, verktøy og avanserte designmønstre for multi-agent.

AutoGen er bygget rundt kjernekonseptet agenter, som er autonome enheter som kan oppfatte miljøet sitt, ta beslutninger og utføre handlinger for å oppnå spesifikke mål. Agenter kommuniserer gjennom asynkrone meldinger, slik at de kan arbeide uavhengig og parallelt, noe som forbedrer systemets skalerbarhet og responsivitet.

<a href="https://en.wikipedia.org/wiki/Actor_model" target="_blank">Agenter er basert på aktørmodellen</a>. Ifølge Wikipedia er en aktør _den grunnleggende byggesteinen for samtidig beregning. Som svar på en melding den mottar, kan en aktør: ta lokale beslutninger, opprette flere aktører, sende flere meldinger og bestemme hvordan den skal svare på neste melding den mottar_.

**Bruksområder**: Automatisering av kodegenerering, dataanalysetasks og bygging av tilpassede agenter for planleggings- og forskningsfunksjoner.

Her er noen viktige kjernekonsepter for AutoGen:

- **Agenter**. En agent er en programvareenhet som:
  - **Kommuniserer via meldinger**, disse meldingene kan være synkrone eller asynkrone.
  - **Opprettholder sin egen tilstand**, som kan endres av innkommende meldinger.
  - **Utfører handlinger** som svar på mottatte meldinger eller endringer i sin tilstand. Disse handlingene kan endre agentens tilstand og produsere eksterne effekter, som å oppdatere meldingslogger, sende nye meldinger, utføre kode eller gjøre API-kall.
    
  Her har du en kort kodebit der du oppretter din egen agent med chat-funksjoner:

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
    
    I den forrige koden har `MyAgent` blitt opprettet og arver fra `RoutedAgent`. Den har en meldingshåndterer som skriver ut innholdet i meldingen og deretter sender et svar ved hjelp av `AssistantAgent`-delegeringen. Legg spesielt merke til hvordan vi tildeler `self._delegate` en instans av `AssistantAgent`, som er en forhåndsbygd agent som kan håndtere chat-kompletteringer.


    La oss informere AutoGen om denne agenttypen og starte programmet:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    I den forrige koden registreres agentene med runtime, og deretter sendes en melding til agenten, noe som resulterer i følgende utdata:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Multi-agenter**. AutoGen støtter opprettelsen av flere agenter som kan samarbeide for å oppnå komplekse oppgaver. Agenter kan kommunisere, dele informasjon og koordinere handlingene sine for å løse problemer mer effektivt. For å opprette et multi-agent-system kan du definere forskjellige typer agenter med spesialiserte funksjoner og roller, som datainnhenting, analyse, beslutningstaking og brukerinteraksjon. La oss se hvordan en slik opprettelse ser ut for å få en følelse av det:

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

    I den forrige koden har vi en `GroupChatManager` som er registrert med runtime. Denne manageren er ansvarlig for å koordinere interaksjonene mellom forskjellige typer agenter, som forfattere, illustratører, redaktører og brukere.

- **Agent-runtime**. Rammeverket gir et runtime-miljø, muliggjør kommunikasjon mellom agenter, administrerer deres identiteter og livssykluser, og håndhever sikkerhets- og personverngrenser. Dette betyr at du kan kjøre agentene dine i et sikkert og kontrollert miljø, og sikre at de kan samhandle trygt og effektivt. Det finnes to runtime-alternativer av interesse:
  - **Frittstående runtime**. Dette er et godt valg for enkeltprosess-applikasjoner der alle agenter er implementert i samme programmeringsspråk og kjører i samme prosess. Her er en illustrasjon av hvordan det fungerer:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-standalone.svg" target="_blank">Frittstående runtime</a>   
Applikasjonsstabel

    *agenter kommuniserer via meldinger gjennom runtime, og runtime administrerer livssyklusen til agenter*

  - **Distribuert agent-runtime**, er egnet for flerprosess-applikasjoner der agenter kan være implementert i forskjellige programmeringsspråk og kjøre på forskjellige maskiner. Her er en illustrasjon av hvordan det fungerer:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-distributed.svg" target="_blank">Distribuert runtime</a>

## Semantic Kernel + Agent Framework

Semantic Kernel er en bedriftsklar AI Orchestration SDK. Den består av AI- og minnekoblinger, sammen med et Agent Framework.

La oss først dekke noen kjernekomponenter:

- **AI-koblinger**: Dette er et grensesnitt med eksterne AI-tjenester og datakilder for bruk i både Python og C#.

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

    Her har du et enkelt eksempel på hvordan du kan opprette en kernel og legge til en chat-kompletteringstjeneste. Semantic Kernel oppretter en forbindelse til en ekstern AI-tjeneste, i dette tilfellet Azure OpenAI Chat Completion.

- **Plugins**: Disse innkapsler funksjoner som en applikasjon kan bruke. Det finnes både ferdige plugins og tilpassede som du kan opprette. Et relatert konsept er "prompt-funksjoner." I stedet for å gi naturlige språkledetråder for funksjonskall, kringkaster du visse funksjoner til modellen. Basert på den nåværende chat-konteksten kan modellen velge å kalle en av disse funksjonene for å fullføre en forespørsel eller et spørsmål. Her er et eksempel:

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

    Her har du først en malprompt `skPrompt` som gir rom for brukeren til å legge inn tekst, `$userInput`. Deretter oppretter du kernel-funksjonen `SummarizeText` og importerer den deretter inn i kernel med plugin-navnet `SemanticFunctions`. Merk navnet på funksjonen som hjelper Semantic Kernel med å forstå hva funksjonen gjør og når den skal kalles.

- **Native-funksjon**: Det finnes også native-funksjoner som rammeverket kan kalle direkte for å utføre oppgaven. Her er et eksempel på en slik funksjon som henter innhold fra en fil:

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

- **Minne**: Abstraherer og forenkler kontekstadministrasjon for AI-apper. Ideen med minne er at dette er noe LLM-en bør vite om. Du kan lagre denne informasjonen i en vektorlagring som ender opp med å være en in-memory database eller en vektordatabase eller lignende. Her er et eksempel på et veldig forenklet scenario der *fakta* legges til minnet:

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

Disse faktaene lagres deretter i minnesamlingen `SummarizedAzureDocs`. Dette er et veldig forenklet eksempel, men du kan se hvordan du kan lagre informasjon i minnet for at LLM skal kunne bruke det.

Så det er det grunnleggende om Semantic Kernel-rammeverket, hva med Agent Framework?

## Azure AI Agent Service

Azure AI Agent Service er en nyere tilleggstjeneste, introdusert på Microsoft Ignite 2024. Den muliggjør utvikling og distribusjon av AI-agenter med mer fleksible modeller, som for eksempel direkte kall til open-source LLM-er som Llama 3, Mistral og Cohere.

Azure AI Agent Service tilbyr sterkere sikkerhetsmekanismer for bedrifter og metoder for datalagring, noe som gjør den egnet for bedriftsapplikasjoner.

Den fungerer umiddelbart med orkestreringsrammeverk for flere agenter som AutoGen og Semantic Kernel.

Denne tjenesten er for øyeblikket i offentlig forhåndsvisning og støtter Python og C# for å bygge agenter.

Ved å bruke Semantic Kernel Python kan vi lage en Azure AI Agent med et brukerdefinert plugin:

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

### Kjernebegreper

Azure AI Agent Service har følgende kjernebegreper:

- **Agent**. Azure AI Agent Service integreres med Azure AI Foundry. Innenfor AI Foundry fungerer en AI-agent som en "smart" mikrotjeneste som kan brukes til å svare på spørsmål (RAG), utføre handlinger eller fullstendig automatisere arbeidsflyter. Den oppnår dette ved å kombinere kraften til generative AI-modeller med verktøy som lar den få tilgang til og samhandle med virkelige datakilder. Her er et eksempel på en agent:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    I dette eksemplet opprettes en agent med modellen `gpt-4o-mini`, et navn `my-agent`, og instruksjoner `You are helpful agent`. Agenten er utstyrt med verktøy og ressurser for å utføre oppgaver som tolkning av kode.

- **Tråd og meldinger**. Tråden er et annet viktig begrep. Den representerer en samtale eller interaksjon mellom en agent og en bruker. Tråder kan brukes til å spore fremdriften i en samtale, lagre kontekstinformasjon og administrere tilstanden til interaksjonen. Her er et eksempel på en tråd:

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

    I den forrige koden opprettes en tråd. Deretter sendes en melding til tråden. Ved å kalle `create_and_process_run` blir agenten bedt om å utføre arbeid på tråden. Til slutt hentes meldingene og logges for å se agentens svar. Meldingen indikerer fremdriften i samtalen mellom brukeren og agenten. Det er også viktig å forstå at meldingene kan være av forskjellige typer, som tekst, bilde eller fil, som betyr at agentens arbeid har resultert i for eksempel et bilde eller et tekstsvar. Som utvikler kan du deretter bruke denne informasjonen til å viderebehandle svaret eller presentere det for brukeren.

- **Integreres med andre AI-rammeverk**. Azure AI Agent Service kan samhandle med andre rammeverk som AutoGen og Semantic Kernel, noe som betyr at du kan bygge deler av appen din i ett av disse rammeverkene og for eksempel bruke Agent Service som en orkestrator, eller du kan bygge alt i Agent Service.

**Bruksområder**: Azure AI Agent Service er designet for bedriftsapplikasjoner som krever sikker, skalerbar og fleksibel distribusjon av AI-agenter.

## Hva er forskjellen mellom disse rammeverkene?

Det kan virke som om det er mye overlapp mellom disse rammeverkene, men det er noen viktige forskjeller når det gjelder design, funksjonalitet og målgrupper:

- **AutoGen**: Er et eksperimenteringsrammeverk fokusert på banebrytende forskning på systemer med flere agenter. Det er det beste stedet å eksperimentere og prototype avanserte systemer med flere agenter.
- **Semantic Kernel**: Er et produksjonsklart agentbibliotek for å bygge agentapplikasjoner for bedrifter. Fokuserer på hendelsesdrevne, distribuerte agentapplikasjoner, som muliggjør flere LLM-er og SLM-er, verktøy og designmønstre for enkelt-/flere agenter.
- **Azure AI Agent Service**: Er en plattform og distribusjonstjeneste i Azure Foundry for agenter. Den tilbyr tilkobling til tjenester støttet av Azure Foundry som Azure OpenAI, Azure AI Search, Bing Search og kodeutførelse.

Fortsatt usikker på hvilken du skal velge?

### Bruksområder

La oss se om vi kan hjelpe deg ved å gå gjennom noen vanlige bruksområder:

> Spørsmål: Jeg eksperimenterer, lærer og bygger proof-of-concept agentapplikasjoner, og jeg vil kunne bygge og eksperimentere raskt
>

>Svar: AutoGen vil være et godt valg for dette scenariet, da det fokuserer på hendelsesdrevne, distribuerte agentapplikasjoner og støtter avanserte designmønstre for flere agenter.

> Spørsmål: Hva gjør AutoGen til et bedre valg enn Semantic Kernel og Azure AI Agent Service for dette bruksområdet?
>
> Svar: AutoGen er spesifikt designet for hendelsesdrevne, distribuerte agentapplikasjoner, noe som gjør det godt egnet for å automatisere kodegenerering og dataanalysetjenester. Det gir nødvendige verktøy og funksjoner for å bygge komplekse systemer med flere agenter effektivt.

>Spørsmål: Det høres ut som Azure AI Agent Service også kunne fungere her, den har verktøy for kodegenerering og mer?

>
> Svar: Ja, Azure AI Agent Service er en plattformtjeneste for agenter og har innebygde funksjoner for flere modeller, Azure AI Search, Bing Search og Azure Functions. Det gjør det enkelt å bygge agentene dine i Foundry Portal og distribuere dem i stor skala.

> Spørsmål: Jeg er fortsatt forvirret, kan du bare gi meg ett alternativ?
>
> Svar: Et godt valg er å bygge applikasjonen din i Semantic Kernel først og deretter bruke Azure AI Agent Service til å distribuere agenten din. Denne tilnærmingen lar deg enkelt vedlikeholde agentene dine samtidig som du utnytter kraften til å bygge systemer med flere agenter i Semantic Kernel. I tillegg har Semantic Kernel en kobling i AutoGen, noe som gjør det enkelt å bruke begge rammeverkene sammen.

La oss oppsummere de viktigste forskjellene i en tabell:

| Rammeverk | Fokus | Kjernebegreper | Bruksområder |
| --- | --- | --- | --- |
| AutoGen | Hendelsesdrevne, distribuerte agentapplikasjoner | Agenter, Personas, Funksjoner, Data | Kodegenerering, dataanalysetjenester |
| Semantic Kernel | Forståelse og generering av menneskelignende tekstinnhold | Agenter, Moduler, Samarbeid | Naturlig språkforståelse, innholdsgenerering |
| Azure AI Agent Service | Fleksible modeller, sikkerhet for bedrifter, Kodegenerering, Verktøykall | Modularitet, Samarbeid, Prosessorkestrering | Sikker, skalerbar og fleksibel distribusjon av AI-agenter |

Hva er det ideelle bruksområdet for hvert av disse rammeverkene?

## Kan jeg integrere mine eksisterende Azure-økosystemverktøy direkte, eller trenger jeg frittstående løsninger?

Svaret er ja, du kan integrere dine eksisterende Azure-økosystemverktøy direkte med Azure AI Agent Service, spesielt fordi den er bygget for å fungere sømløst med andre Azure-tjenester. Du kan for eksempel integrere Bing, Azure AI Search og Azure Functions. Det er også dyp integrasjon med Azure AI Foundry.

For AutoGen og Semantic Kernel kan du også integrere med Azure-tjenester, men det kan kreve at du kaller Azure-tjenestene fra koden din. En annen måte å integrere på er å bruke Azure SDK-er for å samhandle med Azure-tjenester fra agentene dine. I tillegg, som nevnt, kan du bruke Azure AI Agent Service som en orkestrator for agentene dine bygget i AutoGen eller Semantic Kernel, noe som gir enkel tilgang til Azure-økosystemet.

## Eksempelkoder

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Har du flere spørsmål om AI Agent Frameworks?

Bli med i [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) for å møte andre lærere, delta på kontortid og få svar på spørsmålene dine om AI-agenter.

## Referanser

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/" target="_blank">Semantic Kernel og AutoGen</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-python" target="_blank">Semantic Kernel Python Agent Framework</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp" target="_blank">Semantic Kernel .Net Agent Framework</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>
- <a href="https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121" target="_blank">Bruke Azure AI Agent Service med AutoGen / Semantic Kernel for å bygge en løsning med flere agenter</a>

## Forrige leksjon

[Introduksjon til AI-agenter og bruksområder](../01-intro-to-ai-agents/README.md)

## Neste leksjon

[Forstå designmønstre for agenter](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->