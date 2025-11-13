<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7120197753abacc827b64ac2d5d6966f",
  "translation_date": "2025-11-13T14:00:11+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "ro"
}
-->
[![Explorarea Cadrelor pentru Agenți AI](../../../translated_images/lesson-2-thumbnail.c65f44c93b8558df4d5d407e29970e654629e614f357444a9c27c80feb54c79d.ro.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Faceți clic pe imaginea de mai sus pentru a viziona videoclipul acestei lecții)_

# Explorarea Cadrelor pentru Agenți AI

Cadrele pentru agenți AI sunt platforme software concepute pentru a simplifica crearea, implementarea și gestionarea agenților AI. Aceste cadre oferă dezvoltatorilor componente pre-construite, abstracții și instrumente care eficientizează dezvoltarea sistemelor AI complexe.

Aceste cadre ajută dezvoltatorii să se concentreze pe aspectele unice ale aplicațiilor lor, oferind abordări standardizate pentru provocările comune în dezvoltarea agenților AI. Ele îmbunătățesc scalabilitatea, accesibilitatea și eficiența în construirea sistemelor AI.

## Introducere

Această lecție va acoperi:

- Ce sunt cadrele pentru agenți AI și ce permit dezvoltatorilor să realizeze?
- Cum pot echipele să le folosească pentru a prototipa rapid, a itera și a îmbunătăți capabilitățile agenților lor?
- Care sunt diferențele între cadrele și instrumentele create de Microsoft <a href="https://aka.ms/ai-agents/autogen" target="_blank">AutoGen</a>, <a href="https://aka.ms/ai-agents-beginners/semantic-kernel" target="_blank">Semantic Kernel</a> și <a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a>?
- Pot să integrez direct instrumentele existente din ecosistemul Azure sau am nevoie de soluții independente?
- Ce este serviciul Azure AI Agents și cum mă ajută acesta?

## Obiectivele învățării

Obiectivele acestei lecții sunt să vă ajute să înțelegeți:

- Rolul cadrelor pentru agenți AI în dezvoltarea AI.
- Cum să utilizați cadrele pentru agenți AI pentru a construi agenți inteligenți.
- Capabilitățile cheie oferite de cadrele pentru agenți AI.
- Diferențele dintre AutoGen, Semantic Kernel și Azure AI Agent Service.

## Ce sunt cadrele pentru agenți AI și ce permit dezvoltatorilor să facă?

Cadrele AI tradiționale vă pot ajuta să integrați AI în aplicațiile dvs. și să le îmbunătățiți în următoarele moduri:

- **Personalizare**: AI poate analiza comportamentul și preferințele utilizatorilor pentru a oferi recomandări, conținut și experiențe personalizate.  
Exemplu: Servicii de streaming precum Netflix folosesc AI pentru a sugera filme și emisiuni pe baza istoricului de vizionare, sporind implicarea și satisfacția utilizatorilor.
- **Automatizare și eficiență**: AI poate automatiza sarcinile repetitive, eficientiza fluxurile de lucru și îmbunătăți eficiența operațională.  
Exemplu: Aplicațiile de servicii pentru clienți folosesc chatboți alimentați de AI pentru a gestiona întrebările comune, reducând timpii de răspuns și eliberând agenții umani pentru probleme mai complexe.
- **Experiență îmbunătățită a utilizatorului**: AI poate îmbunătăți experiența generală a utilizatorului prin furnizarea de funcții inteligente, cum ar fi recunoașterea vocală, procesarea limbajului natural și textul predictiv.  
Exemplu: Asistenții virtuali precum Siri și Google Assistant folosesc AI pentru a înțelege și răspunde comenzilor vocale, facilitând interacțiunea utilizatorilor cu dispozitivele lor.

### Sună grozav, nu-i așa? Atunci de ce avem nevoie de cadrele pentru agenți AI?

Cadrele pentru agenți AI reprezintă mai mult decât cadrele AI obișnuite. Ele sunt concepute pentru a permite crearea de agenți inteligenți care pot interacționa cu utilizatorii, alți agenți și mediul pentru a atinge obiective specifice. Acești agenți pot manifesta comportament autonom, pot lua decizii și se pot adapta la condiții în schimbare. Să analizăm câteva capabilități cheie oferite de cadrele pentru agenți AI:

- **Colaborare și coordonare între agenți**: Permite crearea mai multor agenți AI care pot lucra împreună, comunica și coordona pentru a rezolva sarcini complexe.
- **Automatizarea și gestionarea sarcinilor**: Oferă mecanisme pentru automatizarea fluxurilor de lucru în mai mulți pași, delegarea sarcinilor și gestionarea dinamică a sarcinilor între agenți.
- **Înțelegere contextuală și adaptare**: Echiparea agenților cu abilitatea de a înțelege contextul, de a se adapta la medii în schimbare și de a lua decizii bazate pe informații în timp real.

Pe scurt, agenții vă permit să faceți mai mult, să duceți automatizarea la nivelul următor, să creați sisteme mai inteligente care se pot adapta și învăța din mediul lor.

## Cum să prototipăm rapid, să iterăm și să îmbunătățim capabilitățile agenților?

Acesta este un domeniu în continuă evoluție, dar există câteva lucruri comune în majoritatea cadrelor pentru agenți AI care vă pot ajuta să prototipați și să iterați rapid, cum ar fi componentele modulare, instrumentele colaborative și învățarea în timp real. Să le explorăm:

- **Utilizați componente modulare**: SDK-urile AI oferă componente pre-construite, cum ar fi conectori AI și de memorie, apelarea funcțiilor folosind limbaj natural sau pluginuri de cod, șabloane de solicitări și altele.
- **Valorificați instrumentele colaborative**: Proiectați agenți cu roluri și sarcini specifice, permițându-le să testeze și să rafineze fluxurile de lucru colaborative.
- **Învățați în timp real**: Implementați bucle de feedback în care agenții învață din interacțiuni și își ajustează comportamentul dinamic.

### Utilizați componente modulare

SDK-uri precum Microsoft Semantic Kernel și LangChain oferă componente pre-construite, cum ar fi conectori AI, șabloane de solicitări și gestionarea memoriei.

**Cum pot echipele să le folosească**: Echipele pot asambla rapid aceste componente pentru a crea un prototip funcțional fără a începe de la zero, permițând experimentarea și iterarea rapidă.

**Cum funcționează în practică**: Puteți utiliza un parser pre-construit pentru a extrage informații din intrările utilizatorului, un modul de memorie pentru a stoca și a recupera date și un generator de solicitări pentru a interacționa cu utilizatorii, toate acestea fără a fi nevoie să construiți aceste componente de la zero.

**Exemplu de cod**. Să analizăm exemple despre cum puteți utiliza un conector AI pre-construit cu Semantic Kernel Python și .Net care folosește apelarea automată a funcțiilor pentru ca modelul să răspundă la intrările utilizatorului:

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
  
Din acest exemplu puteți vedea cum puteți valorifica un parser pre-construit pentru a extrage informații cheie din intrările utilizatorului, cum ar fi originea, destinația și data unei cereri de rezervare a unui zbor. Această abordare modulară vă permite să vă concentrați pe logica de nivel înalt.

### Valorificați instrumentele colaborative

Cadre precum CrewAI, Microsoft AutoGen și Semantic Kernel facilitează crearea mai multor agenți care pot lucra împreună.

**Cum pot echipele să le folosească**: Echipele pot proiecta agenți cu roluri și sarcini specifice, permițându-le să testeze și să rafineze fluxurile de lucru colaborative și să îmbunătățească eficiența generală a sistemului.

**Cum funcționează în practică**: Puteți crea o echipă de agenți în care fiecare agent are o funcție specializată, cum ar fi recuperarea datelor, analiza sau luarea deciziilor. Acești agenți pot comunica și împărtăși informații pentru a atinge un obiectiv comun, cum ar fi răspunsul la o întrebare a utilizatorului sau finalizarea unei sarcini.

**Exemplu de cod (AutoGen)**:

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
  
În codul anterior, puteți vedea cum puteți crea o sarcină care implică mai mulți agenți care lucrează împreună pentru a analiza date. Fiecare agent îndeplinește o funcție specifică, iar sarcina este executată prin coordonarea agenților pentru a atinge rezultatul dorit. Creând agenți dedicați cu roluri specializate, puteți îmbunătăți eficiența și performanța sarcinilor.

### Învățați în timp real

Cadrele avansate oferă capabilități pentru înțelegerea contextului în timp real și adaptare.

**Cum pot echipele să le folosească**: Echipele pot implementa bucle de feedback în care agenții învață din interacțiuni și își ajustează comportamentul dinamic, ducând la îmbunătățirea continuă și rafinarea capabilităților.

**Cum funcționează în practică**: Agenții pot analiza feedback-ul utilizatorilor, datele de mediu și rezultatele sarcinilor pentru a-și actualiza baza de cunoștințe, a ajusta algoritmii de luare a deciziilor și a îmbunătăți performanța în timp. Acest proces de învățare iterativă permite agenților să se adapteze la condiții în schimbare și preferințele utilizatorilor, sporind eficiența generală a sistemului.

## Care sunt diferențele dintre cadrele AutoGen, Semantic Kernel și Azure AI Agent Service?

Există multe moduri de a compara aceste cadre, dar să analizăm câteva diferențe cheie în ceea ce privește designul, capabilitățile și cazurile de utilizare țintă:

## AutoGen

AutoGen este un cadru open-source dezvoltat de Microsoft Research's AI Frontiers Lab. Se concentrează pe aplicații *agentice* distribuite, bazate pe evenimente, permițând mai multe LLM-uri și SLM-uri, instrumente și modele avansate de design multi-agent.

AutoGen este construit în jurul conceptului de bază al agenților, care sunt entități autonome ce pot percepe mediul lor, lua decizii și întreprinde acțiuni pentru a atinge obiective specifice. Agenții comunică prin mesaje asincrone, permițându-le să lucreze independent și în paralel, sporind scalabilitatea și receptivitatea sistemului.

<a href="https://en.wikipedia.org/wiki/Actor_model" target="_blank">Agenții se bazează pe modelul actorului</a>. Conform Wikipedia, un actor este _blocul de bază al calculului concurent. Ca răspuns la un mesaj primit, un actor poate: lua decizii locale, crea mai mulți actori, trimite mai multe mesaje și determina cum să răspundă următorului mesaj primit_.

**Cazuri de utilizare**: Automatizarea generării de cod, sarcini de analiză a datelor și construirea de agenți personalizați pentru funcții de planificare și cercetare.

Iată câteva concepte de bază importante ale AutoGen:

- **Agenți**. Un agent este o entitate software care:
  - **Comunică prin mesaje**, acestea putând fi sincronizate sau asincronizate.
  - **Își menține propriul stat**, care poate fi modificat de mesajele primite.
  - **Întreprinde acțiuni** ca răspuns la mesajele primite sau la schimbările din starea sa. Aceste acțiuni pot modifica starea agentului și pot produce efecte externe, cum ar fi actualizarea jurnalelor de mesaje, trimiterea de noi mesaje, executarea de cod sau efectuarea de apeluri API.

  Aici aveți un scurt fragment de cod în care creați propriul agent cu capabilități de chat:

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
  
  În codul anterior, `MyAgent` a fost creat și moștenește din `RoutedAgent`. Are un handler de mesaje care afișează conținutul mesajului și apoi trimite un răspuns folosind delegatul `AssistantAgent`. Observați în special cum atribuim lui `self._delegate` o instanță a `AssistantAgent`, care este un agent pre-construit capabil să gestioneze completările de chat.

  Să informăm AutoGen despre acest tip de agent și să pornim programul:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```
  
  În codul anterior, agenții sunt înregistrați cu runtime-ul, iar apoi un mesaj este trimis agentului, rezultând următoarea ieșire:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```
  
- **Multi-agenți**. AutoGen suportă crearea mai multor agenți care pot lucra împreună pentru a atinge sarcini complexe. Agenții pot comunica, împărtăși informații și coordona acțiunile lor pentru a rezolva probleme mai eficient. Pentru a crea un sistem multi-agent, puteți defini diferite tipuri de agenți cu funcții și roluri specializate, cum ar fi recuperarea datelor, analiza, luarea deciziilor și interacțiunea cu utilizatorii. Să vedem cum arată o astfel de creație:

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
  
  În codul anterior, avem un `GroupChatManager` care este înregistrat cu runtime-ul. Acest manager este responsabil pentru coordonarea interacțiunilor dintre diferite tipuri de agenți, cum ar fi scriitori, ilustratori, editori și utilizatori.

- **Runtime-ul agentului**. Cadrul oferă un mediu de runtime, permițând comunicarea între agenți, gestionând identitățile și ciclurile lor de viață și impunând limite de securitate și confidențialitate. Aceasta înseamnă că puteți rula agenții dvs. într-un mediu sigur și controlat, asigurându-vă că pot interacționa în siguranță și eficient. Există două runtime-uri de interes:
  - **Runtime independent**. Aceasta este o alegere bună pentru aplicații cu un singur proces, unde toți agenții sunt implementați în același limbaj de programare și rulează în același proces. Iată o ilustrare a modului în care funcționează:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-standalone.svg" target="_blank">Runtime independent</a>  
    Stiva aplicației

    *agenții comunică prin mesaje prin runtime, iar runtime-ul gestionează ciclul de viață al agenților*

  - **Runtime distribuit al agenților**, este potrivit pentru aplicații multi-proces, unde agenții pot fi implementați în diferite limbaje de programare și pot rula pe mașini diferite. Iată o ilustrare a modului în care funcționează:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-distributed.svg" target="_blank">Runtime distribuit</a>

## Semantic Kernel + Cadru pentru Agenți

Semantic Kernel este un SDK de orchestrare AI pregătit pentru întreprinderi. Acesta constă din conectori AI și de memorie, împreună cu un Cadru pentru Agenți.

Să acoperim mai întâi câteva componente de bază:

- **Conectori AI**: Aceasta este o interfață cu servicii AI externe și surse de date pentru utilizare atât în Python, cât și în C#.

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
  
  Aici aveți un exemplu simplu despre cum puteți crea un kernel și adăuga un serviciu de completare a chat-ului. Semantic Kernel creează o conexiune la un serviciu AI extern, în acest caz, Azure OpenAI Chat Completion.

- **Pluginuri**: Acestea encapsulează funcții pe care o aplicație le poate utiliza. Există atât pluginuri gata făcute, cât și unele personalizate pe care le puteți crea. Un concept asociat este "funcțiile de solicitare". În loc să oferiți indicii în limbaj natural pentru invocarea funcțiilor, difuzați anumite funcții către model. Pe baza contextului actual al chat-ului, modelul poate alege să apeleze una dintre aceste funcții pentru a completa o cerere sau o întrebare. Iată un exemplu:

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
  
  Aici, aveți mai întâi un șablon de solicitare `skPrompt` care lasă loc pentru ca utilizatorul să introducă text, `$userInput`. Apoi creați funcția kernel `SummarizeText` și o importați în kernel cu numele pluginului `SemanticFunctions`. Observați numele funcției care ajută Semantic Kernel să înțeleagă ce face funcția și când ar trebui să fie apelată.

- **Funcție nativă**: Există și funcții native pe care cadrul le poate apela direct pentru a îndeplini sarcina. Iată un exemplu de astfel de funcție care recuperează conținutul dintr-un fișier:

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
  
- **Memorie**: Abstractizează și simplifică gestionarea contextului pentru aplicațiile AI. Ideea cu memoria este că aceasta este
Aceste informații sunt apoi stocate în colecția de memorie `SummarizedAzureDocs`. Acesta este un exemplu foarte simplificat, dar poți vedea cum poți stoca informații în memorie pentru ca LLM să le utilizeze.

Acestea sunt elementele de bază ale framework-ului Semantic Kernel, dar ce putem spune despre Agent Framework?

## Serviciul Azure AI Agent

Serviciul Azure AI Agent este o adăugare mai recentă, introdusă la Microsoft Ignite 2024. Acesta permite dezvoltarea și implementarea agenților AI cu modele mai flexibile, cum ar fi apelarea directă a LLM-urilor open-source precum Llama 3, Mistral și Cohere.

Serviciul Azure AI Agent oferă mecanisme mai puternice de securitate pentru întreprinderi și metode de stocare a datelor, ceea ce îl face potrivit pentru aplicații de tip enterprise.

Funcționează direct cu framework-uri de orchestrare multi-agent, cum ar fi AutoGen și Semantic Kernel.

Acest serviciu este în prezent în Public Preview și suportă Python și C# pentru construirea agenților.

Folosind Semantic Kernel Python, putem crea un agent Azure AI cu un plugin definit de utilizator:

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

### Concepte de bază

Serviciul Azure AI Agent are următoarele concepte de bază:

- **Agent**. Serviciul Azure AI Agent se integrează cu Azure AI Foundry. În cadrul AI Foundry, un agent AI acționează ca un microserviciu "inteligent" care poate fi utilizat pentru a răspunde la întrebări (RAG), a efectua acțiuni sau a automatiza complet fluxuri de lucru. Acest lucru este realizat prin combinarea puterii modelelor generative AI cu instrumente care îi permit să acceseze și să interacționeze cu surse de date din lumea reală. Iată un exemplu de agent:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    În acest exemplu, un agent este creat cu modelul `gpt-4o-mini`, un nume `my-agent` și instrucțiuni `You are helpful agent`. Agentul este echipat cu instrumente și resurse pentru a efectua sarcini de interpretare a codului.

- **Thread și mesaje**. Thread-ul este un alt concept important. Reprezintă o conversație sau o interacțiune între un agent și un utilizator. Thread-urile pot fi utilizate pentru a urmări progresul unei conversații, a stoca informații de context și a gestiona starea interacțiunii. Iată un exemplu de thread:

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

    În codul anterior, este creat un thread. Ulterior, un mesaj este trimis către thread. Prin apelarea `create_and_process_run`, agentul este solicitat să efectueze o sarcină pe thread. În final, mesajele sunt preluate și înregistrate pentru a vedea răspunsul agentului. Mesajele indică progresul conversației dintre utilizator și agent. Este, de asemenea, important de înțeles că mesajele pot fi de diferite tipuri, cum ar fi text, imagine sau fișier, ceea ce înseamnă că munca agentului a rezultat, de exemplu, într-o imagine sau un răspuns text. Ca dezvoltator, poți folosi aceste informații pentru a procesa răspunsul sau pentru a-l prezenta utilizatorului.

- **Integrare cu alte framework-uri AI**. Serviciul Azure AI Agent poate interacționa cu alte framework-uri precum AutoGen și Semantic Kernel, ceea ce înseamnă că poți construi o parte din aplicația ta într-unul dintre aceste framework-uri și, de exemplu, să folosești serviciul Agent ca orchestrator sau poți construi totul în serviciul Agent.

**Cazuri de utilizare**: Serviciul Azure AI Agent este conceput pentru aplicații de tip enterprise care necesită implementarea agenților AI într-un mod sigur, scalabil și flexibil.

## Care sunt diferențele dintre aceste framework-uri?

Pare că există multe suprapuneri între aceste framework-uri, dar există câteva diferențe cheie în ceea ce privește designul, capabilitățile și cazurile de utilizare țintă:

- **AutoGen**: Este un framework de experimentare axat pe cercetarea de vârf în sisteme multi-agent. Este cel mai potrivit pentru experimentarea și prototiparea sistemelor multi-agent sofisticate.
- **Semantic Kernel**: Este o bibliotecă de agenți pregătită pentru producție, destinată construirii aplicațiilor agentice de tip enterprise. Se concentrează pe aplicații agentice distribuite, bazate pe evenimente, permițând utilizarea mai multor LLM-uri și SLM-uri, instrumente și modele de design single/multi-agent.
- **Azure AI Agent Service**: Este o platformă și un serviciu de implementare în Azure Foundry pentru agenți. Oferă conectivitate la servicii suportate de Azure, cum ar fi Azure OpenAI, Azure AI Search, Bing Search și execuția de cod.

Încă nu ești sigur ce să alegi?

### Cazuri de utilizare

Să vedem dacă te putem ajuta trecând prin câteva cazuri de utilizare comune:

> Î: Experimentez, învăț și construiesc aplicații agent proof-of-concept și vreau să pot construi și experimenta rapid.
>

> R: AutoGen ar fi o alegere bună pentru acest scenariu, deoarece se concentrează pe aplicații agentice distribuite, bazate pe evenimente, și suportă modele avansate de design multi-agent.

> Î: Ce face ca AutoGen să fie o alegere mai bună decât Semantic Kernel și Azure AI Agent Service pentru acest caz de utilizare?
>
> R: AutoGen este conceput special pentru aplicații agentice distribuite, bazate pe evenimente, ceea ce îl face potrivit pentru automatizarea sarcinilor de generare de cod și analiză de date. Oferă instrumentele și capabilitățile necesare pentru a construi eficient sisteme multi-agent complexe.

> Î: Pare că și Azure AI Agent Service ar putea funcționa aici, are instrumente pentru generarea de cod și altele?
>
> R: Da, Azure AI Agent Service este o platformă pentru agenți și adaugă capabilități integrate pentru mai multe modele, Azure AI Search, Bing Search și Azure Functions. Este ușor să construiești agenții în Foundry Portal și să îi implementezi la scară.

> Î: Sunt încă confuz, dă-mi doar o opțiune.
>
> R: O alegere excelentă este să îți construiești aplicația în Semantic Kernel mai întâi și apoi să folosești Azure AI Agent Service pentru a implementa agentul. Această abordare îți permite să îți păstrezi agenții cu ușurință, în timp ce beneficiezi de puterea de a construi sisteme multi-agent în Semantic Kernel. În plus, Semantic Kernel are un conector în AutoGen, ceea ce face ușor să folosești ambele framework-uri împreună.

Să rezumăm diferențele cheie într-un tabel:

| Framework | Focus | Concepte de bază | Cazuri de utilizare |
| --- | --- | --- | --- |
| AutoGen | Aplicații agentice distribuite, bazate pe evenimente | Agenți, Personaje, Funcții, Date | Generare de cod, sarcini de analiză de date |
| Semantic Kernel | Înțelegerea și generarea de conținut asemănător limbajului uman | Agenți, Componente Modulare, Colaborare | Înțelegerea limbajului natural, generarea de conținut |
| Azure AI Agent Service | Modele flexibile, securitate enterprise, Generare de cod, Apelare de instrumente | Modularitate, Colaborare, Orchestrare de procese | Implementarea agenților AI într-un mod sigur, scalabil și flexibil |

Care este cazul ideal de utilizare pentru fiecare dintre aceste framework-uri?

## Pot să integrez direct instrumentele existente din ecosistemul Azure sau am nevoie de soluții independente?

Răspunsul este da, poți integra direct instrumentele existente din ecosistemul Azure cu Azure AI Agent Service, mai ales pentru că a fost construit să funcționeze perfect cu alte servicii Azure. De exemplu, ai putea integra Bing, Azure AI Search și Azure Functions. Există, de asemenea, o integrare profundă cu Azure AI Foundry.

Pentru AutoGen și Semantic Kernel, poți, de asemenea, să integrezi cu serviciile Azure, dar poate fi necesar să apelezi serviciile Azure din codul tău. O altă modalitate de integrare este utilizarea SDK-urilor Azure pentru a interacționa cu serviciile Azure din agenții tăi. În plus, așa cum s-a menționat, poți folosi Azure AI Agent Service ca orchestrator pentru agenții construiți în AutoGen sau Semantic Kernel, ceea ce ar oferi acces ușor la ecosistemul Azure.

## Exemple de cod

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Ai mai multe întrebări despre framework-urile AI Agent?

Alătură-te [Discord-ului Azure AI Foundry](https://aka.ms/ai-agents/discord) pentru a întâlni alți cursanți, a participa la ore de consultanță și a primi răspunsuri la întrebările tale despre AI Agents.

## Referințe

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/" target="_blank">Semantic Kernel și AutoGen</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-python" target="_blank">Semantic Kernel Python Agent Framework</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp" target="_blank">Semantic Kernel .Net Agent Framework</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>
- <a href="https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121" target="_blank">Utilizarea Azure AI Agent Service cu AutoGen / Semantic Kernel pentru a construi o soluție multi-agent</a>

## Lecția anterioară

[Introducere în AI Agents și cazuri de utilizare](../01-intro-to-ai-agents/README.md)

## Lecția următoare

[Înțelegerea modelelor de design agentic](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm responsabilitatea pentru neînțelegerile sau interpretările greșite care pot apărea din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->