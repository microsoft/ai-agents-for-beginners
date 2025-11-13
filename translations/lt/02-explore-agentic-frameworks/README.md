<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7120197753abacc827b64ac2d5d6966f",
  "translation_date": "2025-11-13T14:45:28+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "lt"
}
-->
[![AI Agentūrų Kūrimo Sistemų Tyrinėjimas](../../../translated_images/lesson-2-thumbnail.c65f44c93b8558df4d5d407e29970e654629e614f357444a9c27c80feb54c79d.lt.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Spustelėkite aukščiau esančią nuotrauką, kad peržiūrėtumėte šios pamokos vaizdo įrašą)_

# AI Agentūrų Kūrimo Sistemų Tyrinėjimas

AI agentūrų kūrimo sistemos yra programinės įrangos platformos, skirtos supaprastinti AI agentų kūrimą, diegimą ir valdymą. Šios sistemos suteikia kūrėjams iš anksto sukurtus komponentus, abstrakcijas ir įrankius, kurie palengvina sudėtingų AI sistemų kūrimą.

Šios sistemos padeda kūrėjams susitelkti į unikalius jų programų aspektus, pateikdamos standartizuotus sprendimus dažniausiai pasitaikantiems AI agentų kūrimo iššūkiams. Jos didina AI sistemų mastelį, prieinamumą ir efektyvumą.

## Įvadas

Šioje pamokoje aptarsime:

- Kas yra AI agentūrų kūrimo sistemos ir ką jos leidžia pasiekti kūrėjams?
- Kaip komandos gali naudoti šias sistemas greitam prototipų kūrimui, iteracijai ir agentų galimybių tobulinimui?
- Kokie yra skirtumai tarp Microsoft sukurtų sistemų <a href="https://aka.ms/ai-agents/autogen" target="_blank">AutoGen</a>, <a href="https://aka.ms/ai-agents-beginners/semantic-kernel" target="_blank">Semantic Kernel</a> ir <a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a>?
- Ar galiu tiesiogiai integruoti savo esamus Azure ekosistemos įrankius, ar man reikia atskirų sprendimų?
- Kas yra Azure AI Agents paslauga ir kaip ji man padeda?

## Mokymosi tikslai

Šios pamokos tikslai yra padėti jums suprasti:

- AI agentūrų kūrimo sistemų vaidmenį AI kūrime.
- Kaip pasinaudoti AI agentūrų kūrimo sistemomis kuriant intelektualius agentus.
- Pagrindines galimybes, kurias suteikia AI agentūrų kūrimo sistemos.
- Skirtumus tarp AutoGen, Semantic Kernel ir Azure AI Agent Service.

## Kas yra AI agentūrų kūrimo sistemos ir ką jos leidžia pasiekti kūrėjams?

Tradicinės AI kūrimo sistemos gali padėti integruoti AI į jūsų programas ir pagerinti jas šiais būdais:

- **Personalizacija**: AI gali analizuoti vartotojų elgesį ir pageidavimus, kad pateiktų suasmenintas rekomendacijas, turinį ir patirtis.  
Pavyzdys: Transliacijos paslaugos, tokios kaip Netflix, naudoja AI, kad pasiūlytų filmus ir laidas pagal peržiūrų istoriją, taip didindamos vartotojų įsitraukimą ir pasitenkinimą.
- **Automatizavimas ir efektyvumas**: AI gali automatizuoti pasikartojančias užduotis, optimizuoti darbo eigas ir pagerinti operacinį efektyvumą.  
Pavyzdys: Klientų aptarnavimo programos naudoja AI valdomus pokalbių robotus, kad atsakytų į dažniausiai užduodamus klausimus, sumažindamos atsakymo laiką ir leisdamos žmonėms spręsti sudėtingesnes problemas.
- **Patobulinta vartotojo patirtis**: AI gali pagerinti bendrą vartotojo patirtį, suteikdama intelektualias funkcijas, tokias kaip balso atpažinimas, natūralios kalbos apdorojimas ir prognozuojantis tekstas.  
Pavyzdys: Virtualūs asistentai, tokie kaip Siri ir Google Assistant, naudoja AI, kad suprastų ir atsakytų į balso komandas, palengvindami vartotojams sąveiką su jų įrenginiais.

### Skamba puikiai, tiesa? Tai kodėl mums reikia AI agentūrų kūrimo sistemų?

AI agentūrų kūrimo sistemos yra daugiau nei tik AI kūrimo sistemos. Jos skirtos kurti intelektualius agentus, kurie gali sąveikauti su vartotojais, kitais agentais ir aplinka, siekdami konkrečių tikslų. Šie agentai gali demonstruoti autonominį elgesį, priimti sprendimus ir prisitaikyti prie besikeičiančių sąlygų. Pažvelkime į pagrindines galimybes, kurias suteikia AI agentūrų kūrimo sistemos:

- **Agentų bendradarbiavimas ir koordinavimas**: Leidžia kurti kelis AI agentus, kurie gali dirbti kartu, bendrauti ir koordinuoti veiksmus, kad išspręstų sudėtingas užduotis.
- **Užduočių automatizavimas ir valdymas**: Suteikia mechanizmus, skirtus automatizuoti daugiapakopes darbo eigas, užduočių delegavimą ir dinaminį užduočių valdymą tarp agentų.
- **Kontekstinis supratimas ir prisitaikymas**: Aprūpina agentus gebėjimu suprasti kontekstą, prisitaikyti prie besikeičiančios aplinkos ir priimti sprendimus remiantis realaus laiko informacija.

Apibendrinant, agentai leidžia jums pasiekti daugiau, perkelti automatizavimą į kitą lygį, kurti intelektualesnes sistemas, kurios gali prisitaikyti ir mokytis iš savo aplinkos.

## Kaip greitai kurti prototipus, iteruoti ir tobulinti agentų galimybes?

Tai sparčiai besikeičianti sritis, tačiau yra keletas bendrų dalykų daugelyje AI agentūrų kūrimo sistemų, kurie gali padėti greitai kurti prototipus ir iteruoti, būtent modulinių komponentų naudojimas, bendradarbiavimo įrankiai ir mokymasis realiuoju laiku. Pažvelkime į tai detaliau:

- **Naudokite modulinius komponentus**: AI SDK siūlo iš anksto sukurtus komponentus, tokius kaip AI ir atminties jungtys, funkcijų kvietimas naudojant natūralią kalbą ar kodo papildinius, šablonus ir kt.
- **Pasinaudokite bendradarbiavimo įrankiais**: Kurkite agentus su konkrečiais vaidmenimis ir užduotimis, leidžiančiais testuoti ir tobulinti bendradarbiavimo darbo eigas.
- **Mokykitės realiuoju laiku**: Įgyvendinkite grįžtamojo ryšio ciklus, kuriuose agentai mokosi iš sąveikų ir dinamiškai koreguoja savo elgesį.

### Naudokite modulinius komponentus

Tokie SDK kaip Microsoft Semantic Kernel ir LangChain siūlo iš anksto sukurtus komponentus, tokius kaip AI jungtys, šablonai ir atminties valdymas.

**Kaip komandos gali tai naudoti**: Komandos gali greitai surinkti šiuos komponentus, kad sukurtų veikiantį prototipą, nepradėdamos nuo nulio, leidžiant greitai eksperimentuoti ir iteruoti.

**Kaip tai veikia praktikoje**: Galite naudoti iš anksto sukurtą analizatorių, kad išgautumėte informaciją iš vartotojo įvesties, atminties modulį duomenims saugoti ir atkurti, bei šablonų generatorių sąveikai su vartotojais, viso to nereikėdami kurti nuo nulio.

**Kodo pavyzdys**. Pažvelkime į pavyzdžius, kaip galite naudoti iš anksto sukurtą AI jungtį su Semantic Kernel Python ir .Net, kuris naudoja automatinį funkcijų kvietimą, kad modelis atsakytų į vartotojo įvestį:

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

Iš šio pavyzdžio matote, kaip galite pasinaudoti iš anksto sukurtu analizatoriumi, kad išgautumėte pagrindinę informaciją iš vartotojo įvesties, pvz., skrydžio užsakymo užklausos kilmę, paskirties vietą ir datą. Šis modulinis požiūris leidžia jums susitelkti į aukšto lygio logiką.

### Pasinaudokite bendradarbiavimo įrankiais

Tokios sistemos kaip CrewAI, Microsoft AutoGen ir Semantic Kernel palengvina kelių agentų, galinčių dirbti kartu, kūrimą.

**Kaip komandos gali tai naudoti**: Komandos gali kurti agentus su konkrečiais vaidmenimis ir užduotimis, leidžiančiais testuoti ir tobulinti bendradarbiavimo darbo eigas bei pagerinti bendrą sistemos efektyvumą.

**Kaip tai veikia praktikoje**: Galite sukurti agentų komandą, kur kiekvienas agentas turi specializuotą funkciją, pvz., duomenų gavimą, analizę ar sprendimų priėmimą. Šie agentai gali bendrauti ir dalintis informacija, kad pasiektų bendrą tikslą, pvz., atsakytų į vartotojo užklausą ar atliktų užduotį.

**Kodo pavyzdys (AutoGen)**:

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

Ankstesniame kode matote, kaip galite sukurti užduotį, kurioje dalyvauja keli agentai, dirbantys kartu analizuoti duomenis. Kiekvienas agentas atlieka konkrečią funkciją, o užduotis vykdoma koordinuojant agentus, kad būtų pasiektas norimas rezultatas. Kurdami specializuotus agentus su konkrečiais vaidmenimis, galite pagerinti užduočių efektyvumą ir našumą.

### Mokykitės realiuoju laiku

Pažangios sistemos suteikia galimybes realiuoju laiku suprasti kontekstą ir prisitaikyti.

**Kaip komandos gali tai naudoti**: Komandos gali įgyvendinti grįžtamojo ryšio ciklus, kuriuose agentai mokosi iš sąveikų ir dinamiškai koreguoja savo elgesį, taip nuolat tobulindami ir tobulindami savo galimybes.

**Kaip tai veikia praktikoje**: Agentai gali analizuoti vartotojų atsiliepimus, aplinkos duomenis ir užduočių rezultatus, kad atnaujintų savo žinių bazę, koreguotų sprendimų priėmimo algoritmus ir laikui bėgant pagerintų našumą. Šis iteracinis mokymosi procesas leidžia agentams prisitaikyti prie besikeičiančių sąlygų ir vartotojų pageidavimų, didinant bendrą sistemos efektyvumą.

## Kokie yra skirtumai tarp AutoGen, Semantic Kernel ir Azure AI Agent Service sistemų?

Yra daug būdų palyginti šias sistemas, tačiau pažvelkime į pagrindinius skirtumus jų dizaino, galimybių ir tikslinių naudojimo atvejų atžvilgiu:

## AutoGen

AutoGen yra atvirojo kodo sistema, sukurta Microsoft Research AI Frontiers Lab. Ji orientuota į įvykių valdomas, paskirstytas *agentines* programas, leidžiančias naudoti kelis LLM ir SLM, įrankius bei pažangius kelių agentų dizaino modelius.

AutoGen pagrindas yra agentų koncepcija – autonominiai vienetai, galintys suvokti savo aplinką, priimti sprendimus ir imtis veiksmų, siekdami konkrečių tikslų. Agentai bendrauja asinchroniniais pranešimais, leidžiančiais jiems dirbti nepriklausomai ir lygiagrečiai, didinant sistemos mastelį ir atsaką.

<a href="https://en.wikipedia.org/wiki/Actor_model" target="_blank">Agentai yra pagrįsti aktoriaus modeliu</a>. Pagal Vikipediją, aktorius yra _pagrindinis lygiagrečios skaičiavimo vienetas. Atsakydamas į gautą pranešimą, aktorius gali: priimti vietinius sprendimus, sukurti daugiau aktorių, siųsti daugiau pranešimų ir nustatyti, kaip reaguoti į kitą gautą pranešimą_.

**Naudojimo atvejai**: Kodo generavimo automatizavimas, duomenų analizės užduotys ir individualių agentų kūrimas planavimo bei tyrimų funkcijoms.

Štai keletas svarbių AutoGen pagrindinių koncepcijų:

- **Agentai**. Agentas yra programinės įrangos vienetas, kuris:
  - **Bendrauja per pranešimus**, kurie gali būti sinchroniniai arba asinchroniniai.
  - **Palaiko savo būseną**, kurią gali keisti gaunami pranešimai.
  - **Atlieka veiksmus** reaguodamas į gautus pranešimus ar būsenos pokyčius. Šie veiksmai gali keisti agento būseną ir sukelti išorinius efektus, pvz., atnaujinti pranešimų žurnalus, siųsti naujus pranešimus, vykdyti kodą ar atlikti API užklausas.

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
  
    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```
  
    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```
  
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
  

## Semantic Kernel + Agent Framework

Semantic Kernel yra įmonėms pritaikytas AI orkestravimo SDK. Jį sudaro AI ir atminties jungtys bei Agent Framework.

Pirmiausia aptarkime pagrindinius komponentus:

- **AI jungtys**: Sąsaja su išorinėmis AI paslaugomis ir duomenų šaltiniais Python ir C# kalbomis.

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
  

- **Papildiniai**: Apima funkcijas, kurias gali naudoti programa. Yra tiek paruoštų papildinių, tiek galimybė kurti savo.  

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
  

- **Natūralios funkcijos**: Framework gali tiesiogiai kviesti funkcijas užduotims atlikti.  

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
  

- **Atmintis**: Supaprastina konteksto valdymą AI programoms.  

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
  
Šie faktai tada saugomi atminties kolekcijoje `SummarizedAzureDocs`. Tai labai supaprastintas pavyzdys, bet galite matyti, kaip galima saugoti informaciją atmintyje, kad LLM galėtų ją naudoti.

Tai yra pagrindai apie Semantic Kernel sistemą, o kaip dėl Agent Framework?

## Azure AI Agent Service

Azure AI Agent Service yra naujesnis papildymas, pristatytas Microsoft Ignite 2024 renginyje. Jis leidžia kurti ir diegti AI agentus su lankstesniais modeliais, pavyzdžiui, tiesiogiai naudojant atvirojo kodo LLM, tokius kaip Llama 3, Mistral ir Cohere.

Azure AI Agent Service suteikia stipresnius įmonės saugumo mechanizmus ir duomenų saugojimo metodus, todėl jis tinkamas naudoti įmonių programose.

Jis veikia iš karto su kelių agentų orkestravimo sistemomis, tokiomis kaip AutoGen ir Semantic Kernel.

Ši paslauga šiuo metu yra viešojoje peržiūroje ir palaiko Python bei C# agentų kūrimui.

Naudodami Semantic Kernel Python, galime sukurti Azure AI Agent su vartotojo apibrėžtu įskiepiu:

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

### Pagrindinės sąvokos

Azure AI Agent Service turi šias pagrindines sąvokas:

- **Agentas**. Azure AI Agent Service integruojasi su Azure AI Foundry. AI Foundry viduje AI agentas veikia kaip „protinga“ mikropaslauga, kuri gali atsakyti į klausimus (RAG), atlikti veiksmus arba visiškai automatizuoti darbo eigas. Tai pasiekiama derinant generatyvinių AI modelių galią su įrankiais, leidžiančiais pasiekti ir sąveikauti su realaus pasaulio duomenų šaltiniais. Štai agento pavyzdys:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    Šiame pavyzdyje sukuriamas agentas su modeliu `gpt-4o-mini`, pavadinimu `my-agent` ir instrukcijomis `You are helpful agent`. Agentas aprūpintas įrankiais ir ištekliais, kad galėtų atlikti kodo interpretavimo užduotis.

- **Gija ir žinutės**. Gija yra dar viena svarbi sąvoka. Ji atspindi pokalbį ar sąveiką tarp agento ir vartotojo. Gijos gali būti naudojamos pokalbio eigai sekti, konteksto informacijai saugoti ir sąveikos būsenai valdyti. Štai gijos pavyzdys:

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

    Ankstesniame kode sukuriama gija. Po to į giją siunčiama žinutė. Iškvietus `create_and_process_run`, agentas prašomas atlikti darbą gijoje. Galiausiai žinutės yra gaunamos ir registruojamos, kad būtų matomas agento atsakymas. Žinutės rodo pokalbio eigą tarp vartotojo ir agento. Taip pat svarbu suprasti, kad žinutės gali būti skirtingų tipų, pavyzdžiui, tekstas, vaizdas ar failas, tai yra, agento darbas gali sukurti, pavyzdžiui, vaizdą ar teksto atsakymą. Kaip kūrėjas, galite naudoti šią informaciją tolesniam atsakymo apdorojimui ar pateikimui vartotojui.

- **Integracija su kitomis AI sistemomis**. Azure AI Agent Service gali sąveikauti su kitomis sistemomis, tokiomis kaip AutoGen ir Semantic Kernel, tai reiškia, kad galite dalį savo programos kurti vienoje iš šių sistemų, o, pavyzdžiui, naudoti Agent Service kaip orkestratorių arba viską kurti Agent Service.

**Naudojimo atvejai**: Azure AI Agent Service yra skirtas įmonių programoms, kurioms reikalingas saugus, mastelio keičiamas ir lankstus AI agentų diegimas.

## Kuo skiriasi šios sistemos?

Atrodo, kad šios sistemos turi daug bendro, tačiau yra keletas pagrindinių skirtumų jų dizaino, galimybių ir tikslinių naudojimo atvejų atžvilgiu:

- **AutoGen**: Tai eksperimentinė sistema, orientuota į pažangius tyrimus apie kelių agentų sistemas. Tai geriausia vieta eksperimentuoti ir kurti sudėtingas kelių agentų sistemas.
- **Semantic Kernel**: Tai gamybai paruošta agentų biblioteka, skirta kurti įmonių agentines programas. Ji orientuota į įvykių valdomas, paskirstytas agentines programas, leidžiančias naudoti kelis LLM ir SLM, įrankius bei vieno/daugelio agentų dizaino modelius.
- **Azure AI Agent Service**: Tai platforma ir diegimo paslauga Azure Foundry agentams. Ji siūlo ryšio su Azure paslaugomis, tokiomis kaip Azure OpenAI, Azure AI Search, Bing Search ir kodo vykdymas, galimybes.

Vis dar nežinote, kurią pasirinkti?

### Naudojimo atvejai

Pažiūrėkime, ar galime jums padėti, peržiūrėdami keletą dažnų naudojimo atvejų:

> K: Eksperimentuoju, mokausi ir kuriu koncepcijos įrodymo agentų programas, ir noriu greitai kurti bei eksperimentuoti.
>

>A: AutoGen būtų geras pasirinkimas šiam scenarijui, nes jis orientuotas į įvykių valdomas, paskirstytas agentines programas ir palaiko pažangius kelių agentų dizaino modelius.

> K: Kodėl AutoGen yra geresnis pasirinkimas nei Semantic Kernel ir Azure AI Agent Service šiam naudojimo atvejui?
>
> A: AutoGen yra specialiai sukurtas įvykių valdomoms, paskirstytoms agentinėms programoms, todėl jis puikiai tinka automatizuoti kodo generavimo ir duomenų analizės užduotis. Jis suteikia reikalingus įrankius ir galimybes efektyviai kurti sudėtingas kelių agentų sistemas.

> K: Atrodo, kad Azure AI Agent Service taip pat galėtų čia veikti, jis turi įrankius kodo generavimui ir daugiau?
>
> A: Taip, Azure AI Agent Service yra platformos paslauga agentams ir turi įmontuotas galimybes keliems modeliams, Azure AI Search, Bing Search ir Azure Functions. Tai leidžia lengvai kurti agentus Foundry portale ir diegti juos masteliu.

> K: Vis dar nesuprantu, tiesiog duokite vieną pasirinkimą.
>
> A: Puikus pasirinkimas yra pirmiausia kurti savo programą Semantic Kernel, o tada naudoti Azure AI Agent Service agentui diegti. Šis požiūris leidžia lengvai išsaugoti savo agentus, tuo pačiu pasinaudojant galimybe kurti kelių agentų sistemas Semantic Kernel. Be to, Semantic Kernel turi jungtį AutoGen, todėl lengva naudoti abi sistemas kartu.

Apibendrinkime pagrindinius skirtumus lentelėje:

| Sistema | Fokusas | Pagrindinės sąvokos | Naudojimo atvejai |
| --- | --- | --- | --- |
| AutoGen | Įvykių valdomos, paskirstytos agentinės programos | Agentai, Personos, Funkcijos, Duomenys | Kodo generavimas, duomenų analizės užduotys |
| Semantic Kernel | Žmogaus kalbos supratimas ir generavimas | Agentai, Moduliniai komponentai, Bendradarbiavimas | Natūralios kalbos supratimas, turinio generavimas |
| Azure AI Agent Service | Lankstūs modeliai, įmonės saugumas, Kodo generavimas, Įrankių naudojimas | Modularumas, Bendradarbiavimas, Procesų orkestracija | Saugus, mastelio keičiamas ir lankstus AI agentų diegimas |

Koks yra idealus kiekvienos iš šių sistemų naudojimo atvejis?

## Ar galiu tiesiogiai integruoti savo esamus Azure ekosistemos įrankius, ar man reikia atskirų sprendimų?

Atsakymas yra taip, galite tiesiogiai integruoti savo esamus Azure ekosistemos įrankius su Azure AI Agent Service, ypač todėl, kad jis buvo sukurtas veikti sklandžiai su kitomis Azure paslaugomis. Pavyzdžiui, galite integruoti Bing, Azure AI Search ir Azure Functions. Taip pat yra gilios integracijos su Azure AI Foundry.

AutoGen ir Semantic Kernel taip pat galite integruoti su Azure paslaugomis, tačiau gali reikėti iškviesti Azure paslaugas iš savo kodo. Kitas būdas integruoti yra naudoti Azure SDK, kad sąveikautumėte su Azure paslaugomis iš savo agentų. Be to, kaip jau buvo minėta, galite naudoti Azure AI Agent Service kaip orkestratorių savo agentams, sukurtiems AutoGen ar Semantic Kernel, kas suteiktų lengvą prieigą prie Azure ekosistemos.

## Pavyzdiniai kodai

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Turite daugiau klausimų apie AI Agent Frameworks?

Prisijunkite prie [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), kad susitiktumėte su kitais besimokančiais, dalyvautumėte konsultacijose ir gautumėte atsakymus į savo klausimus apie AI agentus.

## Nuorodos

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/" target="_blank">Semantic Kernel ir AutoGen</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-python" target="_blank">Semantic Kernel Python Agent Framework</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp" target="_blank">Semantic Kernel .Net Agent Framework</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a>
- <a href="https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121" target="_blank">Naudojant Azure AI Agent Service su AutoGen / Semantic Kernel kuriant kelių agentų sprendimą</a>

## Ankstesnė pamoka

[Įvadas į AI agentus ir jų naudojimo atvejus](../01-intro-to-ai-agents/README.md)

## Kita pamoka

[Agentinio dizaino modelių supratimas](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:  
Šis dokumentas buvo išverstas naudojant AI vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors stengiamės užtikrinti tikslumą, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba turėtų būti laikomas autoritetingu šaltiniu. Kritinei informacijai rekomenduojama naudoti profesionalų žmogaus vertimą. Mes neprisiimame atsakomybės už nesusipratimus ar neteisingus aiškinimus, atsiradusius dėl šio vertimo naudojimo.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->