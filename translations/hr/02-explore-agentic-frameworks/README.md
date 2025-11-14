<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "86b9c2b24da3b3e61711182ffa72601c",
  "translation_date": "2025-09-29T22:59:53+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "hr"
}
-->
[![Istraživanje okvira za AI agente](../../../translated_images/lesson-2-thumbnail.c65f44c93b8558df4d5d407e29970e654629e614f357444a9c27c80feb54c79d.hr.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Kliknite na sliku iznad za video lekcije)_

# Istražite okvire za AI agente

Okviri za AI agente su softverske platforme osmišljene kako bi pojednostavile stvaranje, implementaciju i upravljanje AI agentima. Ovi okviri pružaju programerima unaprijed izrađene komponente, apstrakcije i alate koji olakšavaju razvoj složenih AI sustava.

Ovi okviri pomažu programerima da se usmjere na jedinstvene aspekte svojih aplikacija pružajući standardizirane pristupe uobičajenim izazovima u razvoju AI agenata. Poboljšavaju skalabilnost, pristupačnost i učinkovitost u izgradnji AI sustava.

## Uvod

Ova lekcija obuhvaća:

- Što su okviri za AI agente i što omogućuju programerima da postignu?
- Kako timovi mogu koristiti ove okvire za brzo prototipiranje, iteraciju i poboljšanje sposobnosti svojih agenata?
- Koje su razlike između okvira i alata koje je stvorio Microsoft <a href="https://aka.ms/ai-agents/autogen" target="_blank">AutoGen</a>, <a href="https://aka.ms/ai-agents-beginners/semantic-kernel" target="_blank">Semantic Kernel</a> i <a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a>?
- Mogu li integrirati svoje postojeće alate iz Azure ekosustava izravno ili trebam samostalna rješenja?
- Što je Azure AI Agents Service i kako mi to pomaže?

## Ciljevi učenja

Ciljevi ove lekcije su pomoći vam da razumijete:

- Ulogu okvira za AI agente u razvoju AI-a.
- Kako iskoristiti okvire za AI agente za izgradnju inteligentnih agenata.
- Ključne sposobnosti koje omogućuju okviri za AI agente.
- Razlike između AutoGen, Semantic Kernel i Azure AI Agent Service.

## Što su okviri za AI agente i što omogućuju programerima da rade?

Tradicionalni AI okviri mogu vam pomoći integrirati AI u vaše aplikacije i poboljšati ih na sljedeće načine:

- **Personalizacija**: AI može analizirati ponašanje korisnika i preferencije kako bi pružio personalizirane preporuke, sadržaj i iskustva.
Primjer: Streaming servisi poput Netflixa koriste AI za predlaganje filmova i serija na temelju povijesti gledanja, povećavajući angažman i zadovoljstvo korisnika.
- **Automatizacija i učinkovitost**: AI može automatizirati ponavljajuće zadatke, pojednostaviti tijekove rada i poboljšati operativnu učinkovitost.
Primjer: Aplikacije za korisničku podršku koriste AI chatbotove za rješavanje uobičajenih upita, smanjujući vrijeme odgovora i oslobađajući ljudske agente za složenije probleme.
- **Poboljšano korisničko iskustvo**: AI može poboljšati ukupno korisničko iskustvo pružanjem inteligentnih značajki poput prepoznavanja glasa, obrade prirodnog jezika i prediktivnog teksta.
Primjer: Virtualni asistenti poput Siri i Google Assistant koriste AI za razumijevanje i odgovaranje na glasovne naredbe, olakšavajući korisnicima interakciju s njihovim uređajima.

### Zvuči odlično, zar ne? Pa zašto nam trebaju okviri za AI agente?

Okviri za AI agente predstavljaju nešto više od samih AI okvira. Osmišljeni su za stvaranje inteligentnih agenata koji mogu komunicirati s korisnicima, drugim agentima i okruženjem kako bi postigli određene ciljeve. Ovi agenti mogu pokazivati autonomno ponašanje, donositi odluke i prilagođavati se promjenjivim uvjetima. Pogledajmo neke ključne sposobnosti koje omogućuju okviri za AI agente:

- **Suradnja i koordinacija agenata**: Omogućuju stvaranje više AI agenata koji mogu raditi zajedno, komunicirati i koordinirati kako bi riješili složene zadatke.
- **Automatizacija i upravljanje zadacima**: Pružaju mehanizme za automatizaciju višekoraknih tijekova rada, delegiranje zadataka i dinamičko upravljanje zadacima među agentima.
- **Razumijevanje konteksta i prilagodba**: Opremaju agente sposobnošću razumijevanja konteksta, prilagodbe promjenjivim okruženjima i donošenja odluka na temelju informacija u stvarnom vremenu.

Dakle, u sažetku, agenti vam omogućuju da postignete više, podignete automatizaciju na višu razinu i stvorite inteligentnije sustave koji se mogu prilagoditi i učiti iz svog okruženja.

## Kako brzo prototipirati, iterirati i poboljšati sposobnosti agenata?

Ovo je područje koje se brzo razvija, ali postoje neke zajedničke stvari kod većine okvira za AI agente koje vam mogu pomoći da brzo prototipirate i iterirate, poput modularnih komponenti, suradničkih alata i učenja u stvarnom vremenu. Pogledajmo detaljnije:

- **Koristite modularne komponente**: AI SDK-ovi nude unaprijed izrađene komponente poput AI i Memory konektora, pozivanja funkcija pomoću prirodnog jezika ili kodnih dodataka, predložaka upita i više.
- **Iskoristite suradničke alate**: Dizajnirajte agente s određenim ulogama i zadacima, omogućujući im testiranje i usavršavanje suradničkih tijekova rada.
- **Učite u stvarnom vremenu**: Implementirajte povratne petlje gdje agenti uče iz interakcija i dinamički prilagođavaju svoje ponašanje.

### Koristite modularne komponente

SDK-ovi poput Microsoft Semantic Kernel i LangChain nude unaprijed izrađene komponente poput AI konektora, predložaka upita i upravljanja memorijom.

**Kako timovi mogu koristiti ove komponente**: Timovi mogu brzo sastaviti ove komponente kako bi stvorili funkcionalni prototip bez potrebe za početkom od nule, omogućujući brzo eksperimentiranje i iteraciju.

**Kako to funkcionira u praksi**: Možete koristiti unaprijed izrađeni parser za izdvajanje informacija iz korisničkog unosa, modul memorije za pohranu i dohvaćanje podataka te generator upita za interakciju s korisnicima, sve bez potrebe za izradom ovih komponenti od nule.

**Primjer koda**. Pogledajmo primjere kako možete koristiti unaprijed izrađeni AI konektor sa Semantic Kernel Python i .Net koji koristi automatsko pozivanje funkcija kako bi model odgovorio na korisnički unos:

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

Iz ovog primjera možete vidjeti kako možete iskoristiti unaprijed izrađeni parser za izdvajanje ključnih informacija iz korisničkog unosa, poput polazišta, odredišta i datuma zahtjeva za rezervaciju leta. Ovaj modularni pristup omogućuje vam da se usredotočite na logiku višeg nivoa.

### Iskoristite suradničke alate

Okviri poput CrewAI, Microsoft AutoGen i Semantic Kernel olakšavaju stvaranje više agenata koji mogu raditi zajedno.

**Kako timovi mogu koristiti ove alate**: Timovi mogu dizajnirati agente s određenim ulogama i zadacima, omogućujući im testiranje i usavršavanje suradničkih tijekova rada te poboljšanje ukupne učinkovitosti sustava.

**Kako to funkcionira u praksi**: Možete stvoriti tim agenata gdje svaki agent ima specijaliziranu funkciju, poput dohvaćanja podataka, analize ili donošenja odluka. Ovi agenti mogu komunicirati i dijeliti informacije kako bi postigli zajednički cilj, poput odgovaranja na korisnički upit ili dovršavanja zadatka.

**Primjer koda (AutoGen)**:

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

U prethodnom kodu možete vidjeti kako možete stvoriti zadatak koji uključuje više agenata koji rade zajedno na analizi podataka. Svaki agent obavlja određenu funkciju, a zadatak se izvršava koordinacijom agenata kako bi se postigao željeni rezultat. Stvaranjem posvećenih agenata sa specijaliziranim ulogama možete poboljšati učinkovitost i performanse zadatka.

### Učite u stvarnom vremenu

Napredni okviri pružaju mogućnosti za razumijevanje konteksta u stvarnom vremenu i prilagodbu.

**Kako timovi mogu koristiti ove mogućnosti**: Timovi mogu implementirati povratne petlje gdje agenti uče iz interakcija i dinamički prilagođavaju svoje ponašanje, što dovodi do kontinuiranog poboljšanja i usavršavanja sposobnosti.

**Kako to funkcionira u praksi**: Agenti mogu analizirati povratne informacije korisnika, podatke iz okruženja i rezultate zadataka kako bi ažurirali svoju bazu znanja, prilagodili algoritme donošenja odluka i poboljšali performanse tijekom vremena. Ovaj iterativni proces učenja omogućuje agentima da se prilagode promjenjivim uvjetima i preferencijama korisnika, poboljšavajući ukupnu učinkovitost sustava.

## Koje su razlike između okvira AutoGen, Semantic Kernel i Azure AI Agent Service?

Postoji mnogo načina za usporedbu ovih okvira, ali pogledajmo neke ključne razlike u smislu njihovog dizajna, sposobnosti i ciljanih slučajeva upotrebe:

## AutoGen

AutoGen je open-source okvir koji je razvio Microsoft Research's AI Frontiers Lab. Fokusira se na aplikacije temeljene na događajima i distribuirane *agentne* aplikacije, omogućujući više LLM-ova i SLM-ova, alata i naprednih dizajnerskih obrazaca za više agenata.

AutoGen je izgrađen oko osnovnog koncepta agenata, koji su autonomni entiteti koji mogu percipirati svoje okruženje, donositi odluke i poduzimati radnje kako bi postigli određene ciljeve. Agenti komuniciraju putem asinkronih poruka, omogućujući im da rade neovisno i paralelno, poboljšavajući skalabilnost i odzivnost sustava.

<a href="https://en.wikipedia.org/wiki/Actor_model" target="_blank">Agenti se temelje na modelu glumca</a>. Prema Wikipediji, glumac je _osnovni građevni blok za istovremeno računanje. Kao odgovor na poruku koju primi, glumac može: donositi lokalne odluke, stvarati više glumaca, slati više poruka i odrediti kako će odgovoriti na sljedeću primljenu poruku_.

**Slučajevi upotrebe**: Automatizacija generiranja koda, zadaci analize podataka i izgradnja prilagođenih agenata za funkcije planiranja i istraživanja.

Evo nekih važnih osnovnih koncepata AutoGen-a:

- **Agenti**. Agent je softverski entitet koji:
  - **Komunicira putem poruka**, ove poruke mogu biti sinkrone ili asinkrone.
  - **Održava vlastito stanje**, koje se može mijenjati dolaznim porukama.
  - **Izvodi radnje** kao odgovor na primljene poruke ili promjene u svom stanju. Ove radnje mogu mijenjati stanje agenta i proizvoditi vanjske učinke, poput ažuriranja dnevnika poruka, slanja novih poruka, izvršavanja koda ili pozivanja API-ja.
    
  Evo kratkog isječka koda u kojem stvarate vlastitog agenta s mogućnostima chata:

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
    
U prethodnom kodu, `MyAgent` je stvoren i nasljeđuje od `RoutedAgent`. Ima rukovatelja poruka koji ispisuje sadržaj poruke, a zatim šalje odgovor koristeći delegat `AssistantAgent`. Posebno obratite pažnju na to kako dodjeljujemo `self._delegate` instancu `AssistantAgent`, koji je unaprijed izrađeni agent koji može upravljati završetkom chata.

Pustimo AutoGen da sazna o ovom tipu agenta i pokrenemo program:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

U prethodnom kodu agenti su registrirani s runtime-om, a zatim je poruka poslana agentu, što rezultira sljedećim izlazom:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Više agenata**. AutoGen podržava stvaranje više agenata koji mogu raditi zajedno kako bi postigli složene zadatke. Agenti mogu komunicirati, dijeliti informacije i koordinirati svoje radnje kako bi učinkovitije rješavali probleme. Za stvaranje sustava s više agenata možete definirati različite vrste agenata sa specijaliziranim funkcijama i ulogama, poput dohvaćanja podataka, analize, donošenja odluka i interakcije s korisnicima. Pogledajmo kako takvo stvaranje izgleda:

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

U prethodnom kodu imamo `GroupChatManager` koji je registriran s runtime-om. Ovaj menadžer odgovoran je za koordinaciju interakcija između različitih tipova agenata, poput pisaca, ilustratora, urednika i korisnika.

- **Agent Runtime**. Okvir pruža runtime okruženje, omogućujući komunikaciju između agenata, upravljanje njihovim identitetima i životnim ciklusima te provođenje sigurnosnih i privatnih granica. To znači da možete pokrenuti svoje agente u sigurnom i kontroliranom okruženju, osiguravajući da mogu sigurno i učinkovito komunicirati. Postoje dva zanimljiva runtime-a:
  - **Samostalni runtime**. Ovo je dobar izbor za aplikacije s jednim procesom gdje su svi agenti implementirani u istom programskom jeziku i pokrenuti u istom procesu. Evo ilustracije kako to funkcionira:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-standalone.svg" target="_blank">Samostalni runtime</a>   
Aplikacijski sloj

    *agenti komuniciraju putem poruka kroz runtime, a runtime upravlja životnim ciklusom agenata*

  - **Distribuirani runtime agenata**, prikladan je za aplikacije s više procesa gdje agenti mogu biti implementirani u različitim programskim jezicima i pokrenuti na različitim strojevima. Evo ilustracije kako to funkcionira:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-distributed.svg" target="_blank">Distribuirani runtime</a>

## Semantic Kernel + Agent Framework

Semantic Kernel je AI Orchestration SDK spreman za poduzeća. Sastoji se od AI i memory konektora, zajedno s okvirom za agente.

Prvo pokrijmo neke osnovne komponente:

- **AI konektori**: Ovo je sučelje s vanjskim AI uslugama i izvorima podataka za upotrebu u Pythonu i C#.

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

Ovdje imate jednostavan primjer kako možete stvoriti kernel i dodati uslugu za završetak chata. Semantic Kernel stvara vezu s vanjskom AI uslugom, u ovom slučaju Azure OpenAI Chat Completion.

- **Dodaci (Plugins)**: Oni obuhvaćaju funkcije koje aplikacija može koristiti. Postoje gotovi dodaci i prilagođeni koje možete stvoriti. Povezani koncept su "funkcije upita". Umjesto da pružate prirodne jezične upute za pozivanje funkcija, emitirate određene funkcije modelu. Na temelju trenutnog konteksta chata, model može odlučiti pozvati jednu od ovih funkcija kako bi dovršio zahtjev ili upit. Evo primjera:

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

Ovdje prvo imate predložak upita `skPrompt` koji ostavlja prostor za unos korisnika, `$userInput`. Zatim stvarate kernel funkciju `SummarizeText` i zatim je uvozite u kernel s nazivom dodatka `SemanticFunctions`. Obratite pažnju na naziv funkcije koji pomaže Semantic Kernelu razumjeti što funkcija radi i kada bi je trebalo pozvati.

- **Izvorne funkcije**: Postoje i izvorne funkcije koje okvir može izravno pozvati kako bi obavio zadatak. Evo primjera takve funkcije koja dohvaća sadržaj iz datoteke:

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

- **Memorija**: Apstrahira i pojednostavljuje upravljanje kontekstom za AI aplikacije. Ideja s memorijom je da je to nešto što bi LLM trebao znati. Možete pohraniti ove informacije u vektorsku pohranu koja završava kao memorijska baza podataka ili vektorska baza podataka ili slično. Evo primjera vrlo pojednostavljenog scenarija gdje se *činjenice* dodaju u memoriju:

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

Te činjenice se zatim pohranjuju u memorijsku kolekciju `SummarizedAzureDocs`. Ovo je vrlo pojednostavljen primjer, ali možete vidjeti kako možete pohraniti informacije u memoriju za korištenje od strane LLM-a.

To su osnove okvira Semantic Kernel, a što je s Agent Frameworkom?

## Azure AI Agent Service

Azure AI Agent Service je noviji dodatak, predstavljen na Microsoft Ignite 2024. Omogućuje razvoj i implementaciju AI agenata s fleksibilnijim modelima, poput direktnog pozivanja open-source LLM-ova kao što su Llama 3, Mistral i Cohere.

Azure AI Agent Service pruža jače mehanizme sigurnosti za poduzeća i metode pohrane podataka, što ga čini prikladnim za poslovne aplikacije.

Radi odmah nakon instalacije s okvirima za orkestraciju više agenata poput AutoGen i Semantic Kernel.

Ova usluga trenutno je u javnom pregledu i podržava Python i C# za izradu agenata.

Koristeći Semantic Kernel Python, možemo stvoriti Azure AI Agent s korisnički definiranim dodatkom:

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

Azure AI Agent Service ima sljedeće osnovne koncepte:

- **Agent**. Azure AI Agent Service integrira se s Azure AI Foundry. Unutar AI Foundryja, AI agent djeluje kao "pametan" mikroservis koji se može koristiti za odgovaranje na pitanja (RAG), obavljanje radnji ili potpuno automatiziranje tijekova rada. To postiže kombiniranjem snage generativnih AI modela s alatima koji mu omogućuju pristup i interakciju s izvorima podataka iz stvarnog svijeta. Evo primjera agenta:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    U ovom primjeru, agent je stvoren s modelom `gpt-4o-mini`, imenom `my-agent` i uputama `You are helpful agent`. Agent je opremljen alatima i resursima za obavljanje zadataka interpretacije koda.

- **Nit i poruke**. Nit je još jedan važan koncept. Predstavlja razgovor ili interakciju između agenta i korisnika. Niti se mogu koristiti za praćenje napretka razgovora, pohranu informacija o kontekstu i upravljanje stanjem interakcije. Evo primjera niti:

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

    U prethodnom kodu, stvorena je nit. Nakon toga, poruka je poslana niti. Pozivanjem `create_and_process_run`, agentu se traži da obavi posao na niti. Na kraju, poruke se dohvaćaju i bilježe kako bi se vidio odgovor agenta. Poruke ukazuju na napredak razgovora između korisnika i agenta. Također je važno razumjeti da poruke mogu biti različitih vrsta, poput teksta, slike ili datoteke, što znači da je rad agenta rezultirao, na primjer, slikom ili tekstualnim odgovorom. Kao programer, možete koristiti te informacije za daljnju obradu odgovora ili njegovo predstavljanje korisniku.

- **Integracija s drugim AI okvirima**. Azure AI Agent Service može komunicirati s drugim okvirima poput AutoGen i Semantic Kernel, što znači da možete izgraditi dio svoje aplikacije u jednom od tih okvira, a na primjer koristiti Agent Service kao orkestrator ili možete sve izgraditi unutar Agent Servicea.

**Primjene**: Azure AI Agent Service je dizajniran za poslovne aplikacije koje zahtijevaju sigurnu, skalabilnu i fleksibilnu implementaciju AI agenata.

## Koja je razlika između ovih okvira?

Čini se da postoji puno preklapanja između ovih okvira, ali postoje ključne razlike u njihovom dizajnu, mogućnostima i ciljnim primjenama:

- **AutoGen**: Eksperimentalni okvir usmjeren na najnovija istraživanja o sustavima s više agenata. Najbolji je za eksperimentiranje i prototipiranje sofisticiranih sustava s više agenata.
- **Semantic Kernel**: Proizvodno spremna biblioteka agenata za izgradnju poslovnih aplikacija temeljenih na agentima. Fokusira se na aplikacije temeljene na događajima, distribuirane aplikacije s agentima, omogućujući više LLM-ova i SLM-ova, alate i dizajnerske obrasce za jednog ili više agenata.
- **Azure AI Agent Service**: Platforma i usluga implementacije u Azure Foundryju za agente. Nudi povezivanje s uslugama koje podržava Azure, poput Azure OpenAI, Azure AI Search, Bing Search i izvršavanje koda.

Još uvijek niste sigurni koji odabrati?

### Primjene

Pogledajmo možemo li vam pomoći prolaskom kroz neke uobičajene primjene:

> P: Eksperimentiram, učim i gradim aplikacije s agentima kao dokaz koncepta, i želim brzo graditi i eksperimentirati
>

> O: AutoGen bi bio dobar izbor za ovaj scenarij, jer se fokusira na aplikacije temeljene na događajima, distribuirane aplikacije s agentima i podržava napredne dizajnerske obrasce za više agenata.

> P: Što AutoGen čini boljim izborom od Semantic Kernel i Azure AI Agent Service za ovu primjenu?
>
> O: AutoGen je posebno dizajniran za aplikacije temeljene na događajima, distribuirane aplikacije s agentima, što ga čini vrlo prikladnim za automatizaciju zadataka generiranja koda i analize podataka. Pruža potrebne alate i mogućnosti za učinkovitu izgradnju složenih sustava s više agenata.

> P: Čini se da bi Azure AI Agent Service također mogao raditi ovdje, ima alate za generiranje koda i više?
>
> O: Da, Azure AI Agent Service je platforma za agente i dodaje ugrađene mogućnosti za više modela, Azure AI Search, Bing Search i Azure Functions. Olakšava izgradnju vaših agenata u Foundry Portalu i njihovu implementaciju na velikoj skali.

> P: Još uvijek sam zbunjen, samo mi dajte jednu opciju
>
> O: Odličan izbor je prvo izgraditi svoju aplikaciju u Semantic Kernelu, a zatim koristiti Azure AI Agent Service za implementaciju vašeg agenta. Ovaj pristup omogućuje vam jednostavno trajno pohranjivanje vaših agenata dok koristite snagu za izgradnju sustava s više agenata u Semantic Kernelu. Osim toga, Semantic Kernel ima konektor u AutoGen, što olakšava korištenje oba okvira zajedno.

Sažmimo ključne razlike u tablici:

| Okvir | Fokus | Osnovni koncepti | Primjene |
| --- | --- | --- | --- |
| AutoGen | Aplikacije temeljene na događajima, distribuirane aplikacije s agentima | Agenti, Osobe, Funkcije, Podaci | Generiranje koda, zadaci analize podataka |
| Semantic Kernel | Razumijevanje i generiranje teksta nalik ljudskom | Agenti, Modularne komponente, Suradnja | Razumijevanje prirodnog jezika, generiranje sadržaja |
| Azure AI Agent Service | Fleksibilni modeli, sigurnost za poduzeća, Generiranje koda, Pozivanje alata | Modularnost, Suradnja, Orkestracija procesa | Sigurna, skalabilna i fleksibilna implementacija AI agenata |

Koja je idealna primjena za svaki od ovih okvira?

## Mogu li direktno integrirati svoje postojeće alate iz Azure ekosustava ili trebam samostalna rješenja?

Odgovor je da, možete direktno integrirati svoje postojeće alate iz Azure ekosustava s Azure AI Agent Serviceom, posebno zato što je izgrađen da radi besprijekorno s drugim Azure uslugama. Na primjer, mogli biste integrirati Bing, Azure AI Search i Azure Functions. Također postoji duboka integracija s Azure AI Foundryjem.

Za AutoGen i Semantic Kernel također možete integrirati s Azure uslugama, ali to može zahtijevati da pozivate Azure usluge iz svog koda. Drugi način integracije je korištenje Azure SDK-ova za interakciju s Azure uslugama iz vaših agenata. Osim toga, kao što je spomenuto, možete koristiti Azure AI Agent Service kao orkestrator za svoje agente izgrađene u AutoGen ili Semantic Kernelu, što bi omogućilo jednostavan pristup Azure ekosustavu.

### Imate još pitanja o okvirima za AI agente?

Pridružite se [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) kako biste se povezali s drugim učenicima, prisustvovali uredskim satima i dobili odgovore na svoja pitanja o AI agentima.

## Reference

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/" target="_blank">Semantic Kernel i AutoGen</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-python" target="_blank">Semantic Kernel Python Agent Framework</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp" target="_blank">Semantic Kernel .Net Agent Framework</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a>
- <a href="https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121" target="_blank">Korištenje Azure AI Agent Servicea s AutoGen / Semantic Kernelom za izgradnju rješenja s više agenata</a>

## Prethodna lekcija

[Uvod u AI agente i primjene agenata](../01-intro-to-ai-agents/README.md)

## Sljedeća lekcija

[Razumijevanje dizajnerskih obrazaca za agente](../03-agentic-design-patterns/README.md)

---

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.