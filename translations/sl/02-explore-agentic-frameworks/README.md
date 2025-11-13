<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7120197753abacc827b64ac2d5d6966f",
  "translation_date": "2025-11-13T14:28:22+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "sl"
}
-->
[![Raziskovanje okvirov za AI agente](../../../translated_images/lesson-2-thumbnail.c65f44c93b8558df4d5d407e29970e654629e614f357444a9c27c80feb54c79d.sl.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Kliknite na zgornjo sliko za ogled videa te lekcije)_

# Raziskovanje okvirov za AI agente

Okviri za AI agente so programske platforme, zasnovane za poenostavitev ustvarjanja, uvajanja in upravljanja AI agentov. Ti okviri razvijalcem ponujajo vnaprej pripravljene komponente, abstrakcije in orodja, ki olajšajo razvoj kompleksnih AI sistemov.

Ti okviri razvijalcem omogočajo, da se osredotočijo na edinstvene vidike svojih aplikacij, saj zagotavljajo standardizirane pristope k pogostim izzivom pri razvoju AI agentov. Izboljšujejo skalabilnost, dostopnost in učinkovitost pri gradnji AI sistemov.

## Uvod

Ta lekcija bo zajemala:

- Kaj so okviri za AI agente in kaj omogočajo razvijalcem?
- Kako lahko ekipe z njihovo pomočjo hitro prototipirajo, iterirajo in izboljšujejo zmogljivosti svojih agentov?
- Kakšne so razlike med okviri in orodji, ki jih je ustvaril Microsoft <a href="https://aka.ms/ai-agents/autogen" target="_blank">AutoGen</a>, <a href="https://aka.ms/ai-agents-beginners/semantic-kernel" target="_blank">Semantic Kernel</a> in <a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a>?
- Ali lahko neposredno integriram obstoječa orodja iz ekosistema Azure ali potrebujem samostojne rešitve?
- Kaj je storitev Azure AI Agents in kako mi lahko pomaga?

## Cilji učenja

Cilji te lekcije so, da razumete:

- Vlogo okvirov za AI agente pri razvoju AI.
- Kako izkoristiti okvire za AI agente za gradnjo inteligentnih agentov.
- Ključne zmogljivosti, ki jih omogočajo okviri za AI agente.
- Razlike med AutoGen, Semantic Kernel in Azure AI Agent Service.

## Kaj so okviri za AI agente in kaj omogočajo razvijalcem?

Tradicionalni AI okviri vam lahko pomagajo integrirati AI v vaše aplikacije in jih izboljšati na naslednje načine:

- **Personalizacija**: AI lahko analizira vedenje in preference uporabnikov ter ponudi personalizirana priporočila, vsebine in izkušnje.  
Primer: Pretakalne storitve, kot je Netflix, uporabljajo AI za predlaganje filmov in oddaj na podlagi zgodovine ogledov, kar povečuje angažiranost in zadovoljstvo uporabnikov.
- **Avtomatizacija in učinkovitost**: AI lahko avtomatizira ponavljajoče se naloge, poenostavi delovne tokove in izboljša operativno učinkovitost.  
Primer: Aplikacije za podporo strankam uporabljajo AI-poganjane klepetalne bote za obravnavo pogostih vprašanj, kar skrajša odzivne čase in sprosti človeške agente za bolj kompleksne težave.
- **Izboljšana uporabniška izkušnja**: AI lahko izboljša celotno uporabniško izkušnjo z zagotavljanjem inteligentnih funkcij, kot so prepoznavanje glasu, obdelava naravnega jezika in prediktivno besedilo.  
Primer: Virtualni asistenti, kot sta Siri in Google Assistant, uporabljajo AI za razumevanje in odzivanje na glasovne ukaze, kar uporabnikom olajša interakcijo z napravami.

### To vse zveni odlično, kajne, zakaj torej potrebujemo okvir za AI agente?

Okviri za AI agente predstavljajo nekaj več kot le AI okviri. Zasnovani so za omogočanje ustvarjanja inteligentnih agentov, ki lahko komunicirajo z uporabniki, drugimi agenti in okoljem za dosego specifičnih ciljev. Ti agenti lahko izkazujejo avtonomno vedenje, sprejemajo odločitve in se prilagajajo spreminjajočim se razmeram. Oglejmo si nekaj ključnih zmogljivosti, ki jih omogočajo okviri za AI agente:

- **Sodelovanje in koordinacija agentov**: Omogočajo ustvarjanje več AI agentov, ki lahko sodelujejo, komunicirajo in koordinirajo za reševanje kompleksnih nalog.
- **Avtomatizacija in upravljanje nalog**: Zagotavljajo mehanizme za avtomatizacijo večstopenjskih delovnih tokov, delegiranje nalog in dinamično upravljanje nalog med agenti.
- **Razumevanje konteksta in prilagoditev**: Opremljajo agente z zmožnostjo razumevanja konteksta, prilagajanja spreminjajočim se okoljem in sprejemanja odločitev na podlagi informacij v realnem času.

Skratka, agenti vam omogočajo več, dvigujejo avtomatizacijo na višjo raven in ustvarjajo bolj inteligentne sisteme, ki se lahko prilagajajo in učijo iz svojega okolja.

## Kako hitro prototipirati, iterirati in izboljšati zmogljivosti agenta?

To je hitro razvijajoče se področje, vendar obstajajo nekatere skupne značilnosti večine okvirov za AI agente, ki vam lahko pomagajo hitro prototipirati in iterirati, in sicer modularne komponente, orodja za sodelovanje in učenje v realnem času. Poglobimo se v te:

- **Uporabite modularne komponente**: AI SDK-ji ponujajo vnaprej pripravljene komponente, kot so AI in Memory konektorji, klicanje funkcij z uporabo naravnega jezika ali vtičnikov za kodo, predloge za pozive in drugo.
- **Izkoristite orodja za sodelovanje**: Oblikujte agente s specifičnimi vlogami in nalogami, kar omogoča testiranje in izboljšanje sodelovalnih delovnih tokov.
- **Učite se v realnem času**: Implementirajte povratne zanke, kjer se agenti učijo iz interakcij in dinamično prilagajajo svoje vedenje.

### Uporabite modularne komponente

SDK-ji, kot sta Microsoft Semantic Kernel in LangChain, ponujajo vnaprej pripravljene komponente, kot so AI konektorji, predloge za pozive in upravljanje spomina.

**Kako jih lahko ekipe uporabijo**: Ekipe lahko hitro sestavijo te komponente za ustvarjanje funkcionalnega prototipa brez potrebe po začetku iz nič, kar omogoča hitro eksperimentiranje in iteracijo.

**Kako to deluje v praksi**: Uporabite lahko vnaprej pripravljen razčlenjevalnik za pridobivanje informacij iz uporabniškega vnosa, modul za spomin za shranjevanje in pridobivanje podatkov ter generator pozivov za interakcijo z uporabniki, vse to brez potrebe po gradnji teh komponent iz nič.

**Primer kode**. Oglejmo si primere, kako lahko uporabite vnaprej pripravljen AI konektor s Semantic Kernel Python in .Net, ki uporablja samodejno klicanje funkcij za odziv modela na uporabniški vnos:

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

Iz tega primera lahko vidite, kako lahko izkoristite vnaprej pripravljen razčlenjevalnik za pridobivanje ključnih informacij iz uporabniškega vnosa, kot so izvor, cilj in datum zahteve za rezervacijo leta. Ta modularni pristop vam omogoča, da se osredotočite na logiko na višji ravni.

### Izkoristite orodja za sodelovanje

Okviri, kot so CrewAI, Microsoft AutoGen in Semantic Kernel, omogočajo ustvarjanje več agentov, ki lahko sodelujejo.

**Kako jih lahko ekipe uporabijo**: Ekipe lahko oblikujejo agente s specifičnimi vlogami in nalogami, kar omogoča testiranje in izboljšanje sodelovalnih delovnih tokov ter izboljšanje celotne učinkovitosti sistema.

**Kako to deluje v praksi**: Ustvarite lahko ekipo agentov, kjer ima vsak agent specializirano funkcijo, kot so pridobivanje podatkov, analiza ali sprejemanje odločitev. Ti agenti lahko komunicirajo in delijo informacije za dosego skupnega cilja, kot je odgovor na uporabniško vprašanje ali dokončanje naloge.

**Primer kode (AutoGen)**:

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

V prejšnji kodi vidite, kako lahko ustvarite nalogo, ki vključuje več agentov, ki sodelujejo pri analizi podatkov. Vsak agent opravlja specifično funkcijo, naloga pa se izvaja s koordinacijo agentov za dosego želenega rezultata. Z ustvarjanjem namenskih agentov s specializiranimi vlogami lahko izboljšate učinkovitost in zmogljivost nalog.

### Učite se v realnem času

Napredni okviri omogočajo razumevanje konteksta in prilagajanje v realnem času.

**Kako jih lahko ekipe uporabijo**: Ekipe lahko implementirajo povratne zanke, kjer se agenti učijo iz interakcij in dinamično prilagajajo svoje vedenje, kar vodi do nenehnega izboljševanja in izpopolnjevanja zmogljivosti.

**Kako to deluje v praksi**: Agenti lahko analizirajo povratne informacije uporabnikov, podatke o okolju in rezultate nalog za posodobitev svoje baze znanja, prilagoditev algoritmov za sprejemanje odločitev in izboljšanje zmogljivosti skozi čas. Ta iterativni proces učenja omogoča agentom, da se prilagodijo spreminjajočim se razmeram in preferencam uporabnikov, kar izboljšuje celotno učinkovitost sistema.

## Kakšne so razlike med okviri AutoGen, Semantic Kernel in Azure AI Agent Service?

Obstaja veliko načinov za primerjavo teh okvirov, vendar si oglejmo nekaj ključnih razlik glede na njihovo zasnovo, zmogljivosti in ciljne primere uporabe:

## AutoGen

AutoGen je odprtokodni okvir, ki ga je razvil Microsoft Research's AI Frontiers Lab. Osredotoča se na dogodkovno vodene, porazdeljene *agentne* aplikacije, ki omogočajo več LLM-jev in SLM-jev, orodij ter napredne vzorce oblikovanja več agentov.

AutoGen temelji na osnovnem konceptu agentov, ki so avtonomni subjekti, ki lahko zaznavajo svoje okolje, sprejemajo odločitve in ukrepajo za dosego specifičnih ciljev. Agenti komunicirajo prek asinhronih sporočil, kar jim omogoča, da delujejo neodvisno in vzporedno, kar izboljšuje skalabilnost in odzivnost sistema.

<a href="https://en.wikipedia.org/wiki/Actor_model" target="_blank">Agenti temeljijo na modelu akterja</a>. Po Wikipediji je akter _osnovni gradnik sočasnega računalništva. Kot odgovor na prejeto sporočilo lahko akter: sprejme lokalne odločitve, ustvari več akterjev, pošlje več sporočil in določi, kako se odzvati na naslednje prejeto sporočilo_.

**Primeri uporabe**: Avtomatizacija generiranja kode, naloge analize podatkov in gradnja prilagojenih agentov za funkcije načrtovanja in raziskovanja.

Tukaj je nekaj pomembnih osnovnih konceptov AutoGen:

- **Agenti**. Agent je programski subjekt, ki:
  - **Komunicira prek sporočil**, ta sporočila so lahko sinhrona ali asinhrona.
  - **Vzdržuje svoje stanje**, ki ga lahko spremenijo dohodna sporočila.
  - **Izvaja dejanja** kot odgovor na prejeta sporočila ali spremembe svojega stanja. Ta dejanja lahko spremenijo stanje agenta in povzročijo zunanje učinke, kot so posodobitev dnevnikov sporočil, pošiljanje novih sporočil, izvajanje kode ali klicanje API-jev.
    
  Tukaj je kratek del kode, v katerem ustvarite svojega agenta s funkcijami za klepet:

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
    
    V prejšnji kodi je bil ustvarjen `MyAgent`, ki deduje iz `RoutedAgent`. Ima obdelovalec sporočil, ki natisne vsebino sporočila in nato pošlje odgovor z uporabo delegata `AssistantAgent`. Posebej opazite, kako dodelimo `self._delegate` instanco `AssistantAgent`, ki je vnaprej pripravljen agent, ki lahko obravnava zaključke klepeta.


    Nato obvestimo AutoGen o tej vrsti agenta in zaženemo program:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    V prejšnji kodi so agenti registrirani v okolju izvajanja, nato pa je agentu poslano sporočilo, kar povzroči naslednji izhod:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Več agentov**. AutoGen podpira ustvarjanje več agentov, ki lahko sodelujejo pri doseganju kompleksnih nalog. Agenti lahko komunicirajo, delijo informacije in usklajujejo svoja dejanja za učinkovitejše reševanje problemov. Za ustvarjanje sistema z več agenti lahko definirate različne vrste agentov s specializiranimi funkcijami in vlogami, kot so pridobivanje podatkov, analiza, sprejemanje odločitev in interakcija z uporabniki. Poglejmo, kako takšna ustvaritev izgleda:

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

    V prejšnji kodi imamo `GroupChatManager`, ki je registriran v okolju izvajanja. Ta upravitelj je odgovoren za usklajevanje interakcij med različnimi vrstami agentov, kot so pisci, ilustratorji, uredniki in uporabniki.

- **Okolje izvajanja agentov**. Okvir zagotavlja okolje izvajanja, ki omogoča komunikacijo med agenti, upravlja njihove identitete in življenjske cikle ter zagotavlja varnostne in zasebnostne meje. To pomeni, da lahko svoje agente zaženete v varnem in nadzorovanem okolju, kar zagotavlja, da lahko varno in učinkovito sodelujejo. Obstajata dve zanimivi okolji izvajanja:
  - **Samostojno okolje izvajanja**. To je dobra izbira za aplikacije z enim procesom, kjer so vsi agenti implementirani v istem programskem jeziku in tečejo v istem procesu. Tukaj je ilustracija, kako deluje:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-standalone.svg" target="_blank">Samostojno okolje izvajanja</a>   
Aplikacijski sklad

    *agenti komunicirajo prek sporočil skozi okolje izvajanja, ki upravlja življenjski cikel agentov*

  - **Porazdeljeno okolje izvajanja**, je primerno za aplikacije z več procesi, kjer so agenti lahko implementirani v različnih programskih jezikih in tečejo na različnih strojih. Tukaj je ilustracija, kako deluje:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-distributed.svg" target="_blank">Porazdeljeno okolje izvajanja</a>

## Semantic Kernel + Okvir za agente

Semantic Kernel je SDK za orkestracijo AI, pripravljen za podjetja. Sestavljajo ga AI in spominski konektorji ter okvir za agente.

Najprej pokrijmo nekaj osnovnih komponent:

- **AI konektorji**: To je vmesnik z zunanjimi AI storitvami in viri podatkov za uporabo v Pythonu in C#.

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

    Tukaj imate preprost primer, kako lahko ustvarite jedro in dodate storitev za zaključevanje klepeta. Semantic Kernel ustvari povezavo z zunanjo AI storitvijo, v tem primeru Azure OpenAI Chat Completion.

- **Vtičniki**: Ti vključujejo funkcije, ki jih lahko aplikacija uporablja. Obstajajo tako pripravljeni vtičniki kot tudi prilagojeni, ki jih lahko ustvarite. Soroden koncept so "funkcije pozivov". Namesto da bi modelu podali naravne jezikovne namige za klic funkcij, določite določene funkcije, ki jih model lahko pokliče glede na trenutni kontekst klepeta. Tukaj je primer:

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

    Tukaj imate najprej predlogo poziva `skPrompt`, ki omogoča uporabniku, da vnese besedilo, `$userInput`. Nato ustvarite funkcijo jedra `SummarizeText` in jo nato uvozite v jedro z imenom vtičnika `SemanticFunctions`. Opazite ime funkcije, ki pomaga Semantic Kernelu razumeti, kaj funkcija počne in kdaj jo je treba poklicati.

- **Domača funkcija**: Obstajajo tudi domače funkcije, ki jih okvir lahko neposredno pokliče za izvedbo naloge. Tukaj je primer takšne funkcije, ki pridobi vsebino iz datoteke:

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

- **Spomin**: Abstrahira in poenostavi upravljanje konteksta za AI aplikacije. Ideja spomina je, da je to nekaj, kar bi moral LLM vedeti. Te informacije lahko shranite v vektorsko shrambo, ki je lahko pomnilniška baza podatkov, vektorska baza podatkov ali podobno. Tukaj je primer zelo poenostavljenega scenarija, kjer se *dejstva* dodajo v spomin:

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

Te dejstva so nato shranjena v zbirki podatkov `SummarizedAzureDocs`. To je zelo poenostavljen primer, vendar lahko vidite, kako lahko shranite informacije v pomnilnik, da jih LLM uporabi.

Torej, to so osnove okvira Semantic Kernel, kaj pa Agent Framework?

## Azure AI Agent Service

Azure AI Agent Service je novejši dodatek, predstavljen na Microsoft Ignite 2024. Omogoča razvoj in uvajanje AI agentov z bolj prilagodljivimi modeli, kot je neposredno klicanje odprtokodnih LLM-jev, kot so Llama 3, Mistral in Cohere.

Azure AI Agent Service zagotavlja močnejše mehanizme za varnost v podjetjih in metode shranjevanja podatkov, kar ga naredi primernega za poslovne aplikacije.

Deluje takoj z večagentnimi orkestracijskimi okviri, kot sta AutoGen in Semantic Kernel.

Ta storitev je trenutno v javni predogledni različici in podpira Python ter C# za gradnjo agentov.

Z uporabo Semantic Kernel Python lahko ustvarimo Azure AI agenta z uporabniško določenim vtičnikom:

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

### Osnovni koncepti

Azure AI Agent Service vključuje naslednje osnovne koncepte:

- **Agent**. Azure AI Agent Service se integrira z Azure AI Foundry. Znotraj AI Foundry deluje AI agent kot "pameten" mikrostoritev, ki se lahko uporablja za odgovarjanje na vprašanja (RAG), izvajanje dejanj ali popolno avtomatizacijo delovnih tokov. To doseže z združevanjem moči generativnih AI modelov z orodji, ki mu omogočajo dostop do resničnih virov podatkov in interakcijo z njimi. Tukaj je primer agenta:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    V tem primeru je agent ustvarjen z modelom `gpt-4o-mini`, imenom `my-agent` in navodili `You are helpful agent`. Agent je opremljen z orodji in viri za izvajanje nalog interpretacije kode.

- **Nit in sporočila**. Nit je še en pomemben koncept. Predstavlja pogovor ali interakcijo med agentom in uporabnikom. Niti se lahko uporabljajo za sledenje napredku pogovora, shranjevanje informacij o kontekstu in upravljanje stanja interakcije. Tukaj je primer niti:

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

    V prejšnji kodi je ustvarjena nit. Nato je sporočilo poslano v nit. Z uporabo `create_and_process_run` je agentu naročeno, da opravi delo na niti. Na koncu so sporočila pridobljena in zabeležena, da se vidi agentov odgovor. Sporočila kažejo napredek pogovora med uporabnikom in agentom. Pomembno je tudi razumeti, da so sporočila lahko različnih vrst, kot so besedilo, slika ali datoteka, kar pomeni, da je agentovo delo rezultiralo na primer v sliki ali besedilnem odgovoru. Kot razvijalec lahko nato uporabite te informacije za nadaljnjo obdelavo odgovora ali njegovo predstavitev uporabniku.

- **Integracija z drugimi AI okviri**. Azure AI Agent Service lahko komunicira z drugimi okviri, kot sta AutoGen in Semantic Kernel, kar pomeni, da lahko del svoje aplikacije zgradite v enem od teh okvirov, na primer z uporabo Agent Service kot orkestratorja, ali pa vse zgradite v Agent Service.

**Primeri uporabe**: Azure AI Agent Service je zasnovan za poslovne aplikacije, ki zahtevajo varno, skalabilno in prilagodljivo uvajanje AI agentov.

## Kakšna je razlika med temi okviri?

Zdi se, da je med temi okviri veliko prekrivanja, vendar obstajajo ključne razlike glede njihove zasnove, zmogljivosti in ciljnih primerov uporabe:

- **AutoGen**: Je eksperimentalni okvir, osredotočen na najnovejše raziskave o večagentnih sistemih. Je najboljše mesto za eksperimentiranje in prototipiranje naprednih večagentnih sistemov.
- **Semantic Kernel**: Je proizvodno pripravljen knjižnični agent za gradnjo poslovnih agentnih aplikacij. Osredotoča se na dogodkovno vodene, razpršene agentne aplikacije, ki omogočajo več LLM-jev in SLM-jev, orodij ter enojne/večagentne vzorce oblikovanja.
- **Azure AI Agent Service**: Je platforma in storitev uvajanja v Azure Foundry za agente. Ponuja povezljivost z storitvami, ki jih podpira Azure, kot so Azure OpenAI, Azure AI Search, Bing Search in izvajanje kode.

Še vedno niste prepričani, katero izbrati?

### Primeri uporabe

Poglejmo, če vam lahko pomagamo z nekaj pogostimi primeri uporabe:

> V: Eksperimentiram, se učim in gradim dokaz koncepta agentnih aplikacij, želim pa hitro graditi in eksperimentirati
>

> O: AutoGen bi bil dobra izbira za ta scenarij, saj se osredotoča na dogodkovno vodene, razpršene agentne aplikacije in podpira napredne večagentne vzorce oblikovanja.

> V: Kaj naredi AutoGen boljšo izbiro kot Semantic Kernel in Azure AI Agent Service za ta primer uporabe?
>
> O: AutoGen je posebej zasnovan za dogodkovno vodene, razpršene agentne aplikacije, zaradi česar je zelo primeren za avtomatizacijo nalog generiranja kode in analize podatkov. Ponuja potrebna orodja in zmogljivosti za učinkovito gradnjo kompleksnih večagentnih sistemov.

> V: Zdi se, da bi Azure AI Agent Service lahko deloval tudi tukaj, saj ima orodja za generiranje kode in več?
>
> O: Da, Azure AI Agent Service je platformna storitev za agente in ima vgrajene zmogljivosti za več modelov, Azure AI Search, Bing Search in Azure Functions. Omogoča enostavno gradnjo vaših agentov v Foundry Portalu in njihovo uvajanje na velikem obsegu.

> V: Še vedno sem zmeden, samo dajte mi eno možnost
>
> O: Odlična izbira je, da najprej zgradite svojo aplikacijo v Semantic Kernel in nato uporabite Azure AI Agent Service za uvajanje vašega agenta. Ta pristop vam omogoča, da enostavno ohranite svoje agente, hkrati pa izkoristite moč za gradnjo večagentnih sistemov v Semantic Kernel. Poleg tega ima Semantic Kernel povezovalnik v AutoGen, kar omogoča enostavno uporabo obeh okvirov skupaj.

Povzemimo ključne razlike v tabeli:

| Okvir | Osredotočenost | Osnovni koncepti | Primeri uporabe |
| --- | --- | --- | --- |
| AutoGen | Dogodkovno vodene, razpršene agentne aplikacije | Agenti, Osebnosti, Funkcije, Podatki | Generiranje kode, naloge analize podatkov |
| Semantic Kernel | Razumevanje in generiranje besedil, podobnih človeškim | Agenti, Modularne komponente, Sodelovanje | Razumevanje naravnega jezika, generiranje vsebine |
| Azure AI Agent Service | Prilagodljivi modeli, varnost v podjetjih, Generiranje kode, Klicanje orodij | Modularnost, Sodelovanje, Orkestracija procesov | Varno, skalabilno in prilagodljivo uvajanje AI agentov |

Kateri je idealen primer uporabe za vsak od teh okvirov?

## Ali lahko neposredno integriram svoje obstoječe Azure ekosistemske storitve ali potrebujem samostojne rešitve?

Odgovor je da, lahko neposredno integrirate svoje obstoječe Azure ekosistemske storitve z Azure AI Agent Service, še posebej, ker je bil zasnovan za brezhibno delovanje z drugimi Azure storitvami. Na primer, lahko integrirate Bing, Azure AI Search in Azure Functions. Obstaja tudi globoka integracija z Azure AI Foundry.

Za AutoGen in Semantic Kernel lahko prav tako integrirate z Azure storitvami, vendar boste morda morali klicati Azure storitve iz svoje kode. Drug način integracije je uporaba Azure SDK-jev za interakcijo z Azure storitvami iz vaših agentov. Poleg tega, kot je bilo omenjeno, lahko uporabite Azure AI Agent Service kot orkestrator za vaše agente, zgrajene v AutoGen ali Semantic Kernel, kar omogoča enostaven dostop do Azure ekosistema.

## Vzorčne kode

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Imate več vprašanj o AI Agent Frameworks?

Pridružite se [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), da se povežete z drugimi učenci, udeležite uradnih ur in dobite odgovore na svoja vprašanja o AI agentih.

## Reference

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/" target="_blank">Semantic Kernel in AutoGen</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-python" target="_blank">Semantic Kernel Python Agent Framework</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp" target="_blank">Semantic Kernel .Net Agent Framework</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>
- <a href="https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121" target="_blank">Uporaba Azure AI Agent Service z AutoGen / Semantic Kernel za gradnjo večagentne rešitve</a>

## Prejšnja lekcija

[Uvod v AI agente in primere uporabe agentov](../01-intro-to-ai-agents/README.md)

## Naslednja lekcija

[Razumevanje vzorcev oblikovanja agentov](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem maternem jeziku naj se šteje za avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->