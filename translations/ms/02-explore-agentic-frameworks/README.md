<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "7120197753abacc827b64ac2d5d6966f",
  "translation_date": "2025-11-13T13:24:28+00:00",
  "source_file": "02-explore-agentic-frameworks/README.md",
  "language_code": "ms"
}
-->
[![Meneroka Rangka Kerja Ejen AI](../../../translated_images/lesson-2-thumbnail.c65f44c93b8558df4d5d407e29970e654629e614f357444a9c27c80feb54c79d.ms.png)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Klik imej di atas untuk menonton video pelajaran ini)_

# Meneroka Rangka Kerja Ejen AI

Rangka kerja ejen AI adalah platform perisian yang direka untuk mempermudah penciptaan, penyebaran, dan pengurusan ejen AI. Rangka kerja ini menyediakan komponen, abstraksi, dan alat yang telah dibina untuk memudahkan pembangunan sistem AI yang kompleks.

Rangka kerja ini membantu pembangun memberi tumpuan kepada aspek unik aplikasi mereka dengan menyediakan pendekatan standard kepada cabaran biasa dalam pembangunan ejen AI. Ia meningkatkan skalabiliti, kebolehcapaian, dan kecekapan dalam membina sistem AI.

## Pengenalan 

Pelajaran ini akan merangkumi:

- Apa itu Rangka Kerja Ejen AI dan apa yang dapat dicapai oleh pembangun dengannya?
- Bagaimana pasukan boleh menggunakan ini untuk membuat prototaip dengan cepat, mengulangi, dan meningkatkan keupayaan ejen mereka?
- Apakah perbezaan antara rangka kerja dan alat yang dicipta oleh Microsoft <a href="https://aka.ms/ai-agents/autogen" target="_blank">AutoGen</a>, <a href="https://aka.ms/ai-agents-beginners/semantic-kernel" target="_blank">Semantic Kernel</a>, dan <a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Azure AI Agent Service</a>?
- Bolehkah saya mengintegrasikan alat ekosistem Azure sedia ada saya secara langsung, atau adakah saya memerlukan penyelesaian yang berdiri sendiri?
- Apa itu perkhidmatan Azure AI Agents dan bagaimana ini membantu saya?

## Matlamat Pembelajaran

Matlamat pelajaran ini adalah untuk membantu anda memahami:

- Peranan Rangka Kerja Ejen AI dalam pembangunan AI.
- Bagaimana memanfaatkan Rangka Kerja Ejen AI untuk membina ejen pintar.
- Keupayaan utama yang diaktifkan oleh Rangka Kerja Ejen AI.
- Perbezaan antara AutoGen, Semantic Kernel, dan Azure AI Agent Service.

## Apa itu Rangka Kerja Ejen AI dan apa yang dapat dicapai oleh pembangun dengannya?

Rangka kerja AI tradisional boleh membantu anda mengintegrasikan AI ke dalam aplikasi anda dan menjadikan aplikasi ini lebih baik dengan cara berikut:

- **Pemperibadian**: AI boleh menganalisis tingkah laku dan keutamaan pengguna untuk memberikan cadangan, kandungan, dan pengalaman yang diperibadikan.
Contoh: Perkhidmatan penstriman seperti Netflix menggunakan AI untuk mencadangkan filem dan rancangan berdasarkan sejarah tontonan, meningkatkan penglibatan dan kepuasan pengguna.
- **Automasi dan Kecekapan**: AI boleh mengautomasi tugas berulang, mempermudah aliran kerja, dan meningkatkan kecekapan operasi.
Contoh: Aplikasi perkhidmatan pelanggan menggunakan chatbot berkuasa AI untuk menangani pertanyaan biasa, mengurangkan masa tindak balas dan membebaskan ejen manusia untuk isu yang lebih kompleks.
- **Pengalaman Pengguna yang Dipertingkatkan**: AI boleh meningkatkan pengalaman pengguna keseluruhan dengan menyediakan ciri pintar seperti pengecaman suara, pemprosesan bahasa semula jadi, dan teks ramalan.
Contoh: Pembantu maya seperti Siri dan Google Assistant menggunakan AI untuk memahami dan bertindak balas terhadap arahan suara, memudahkan pengguna berinteraksi dengan peranti mereka.

### Kedengarannya hebat, jadi mengapa kita memerlukan Rangka Kerja Ejen AI?

Rangka kerja ejen AI mewakili sesuatu yang lebih daripada sekadar rangka kerja AI. Ia direka untuk membolehkan penciptaan ejen pintar yang boleh berinteraksi dengan pengguna, ejen lain, dan persekitaran untuk mencapai matlamat tertentu. Ejen ini boleh menunjukkan tingkah laku autonomi, membuat keputusan, dan menyesuaikan diri dengan keadaan yang berubah. Mari kita lihat beberapa keupayaan utama yang diaktifkan oleh Rangka Kerja Ejen AI:

- **Kerjasama dan Koordinasi Ejen**: Membolehkan penciptaan pelbagai ejen AI yang boleh bekerjasama, berkomunikasi, dan berkoordinasi untuk menyelesaikan tugas yang kompleks.
- **Automasi dan Pengurusan Tugas**: Menyediakan mekanisme untuk mengautomasi aliran kerja berbilang langkah, delegasi tugas, dan pengurusan tugas dinamik antara ejen.
- **Pemahaman dan Penyesuaian Kontekstual**: Melengkapkan ejen dengan keupayaan untuk memahami konteks, menyesuaikan diri dengan persekitaran yang berubah, dan membuat keputusan berdasarkan maklumat masa nyata.

Secara ringkasnya, ejen membolehkan anda melakukan lebih banyak perkara, membawa automasi ke tahap seterusnya, mencipta sistem yang lebih pintar yang boleh menyesuaikan diri dan belajar daripada persekitaran mereka.

## Bagaimana untuk membuat prototaip dengan cepat, mengulangi, dan meningkatkan keupayaan ejen?

Ini adalah landskap yang bergerak pantas, tetapi terdapat beberapa perkara yang biasa di kebanyakan Rangka Kerja Ejen AI yang boleh membantu anda membuat prototaip dan mengulangi dengan cepat iaitu komponen modular, alat kolaboratif, dan pembelajaran masa nyata. Mari kita selami ini:

- **Gunakan Komponen Modular**: SDK AI menawarkan komponen yang telah dibina seperti penyambung AI dan Memori, panggilan fungsi menggunakan bahasa semula jadi atau plugin kod, templat arahan, dan banyak lagi.
- **Manfaatkan Alat Kolaboratif**: Reka bentuk ejen dengan peranan dan tugas tertentu, membolehkan mereka menguji dan memperbaiki aliran kerja kolaboratif.
- **Belajar dalam Masa Nyata**: Laksanakan gelung maklum balas di mana ejen belajar daripada interaksi dan menyesuaikan tingkah laku mereka secara dinamik.

### Gunakan Komponen Modular

SDK seperti Microsoft Semantic Kernel dan LangChain menawarkan komponen yang telah dibina seperti penyambung AI, templat arahan, dan pengurusan memori.

**Bagaimana pasukan boleh menggunakan ini**: Pasukan boleh dengan cepat menyusun komponen ini untuk mencipta prototaip yang berfungsi tanpa bermula dari awal, membolehkan eksperimen dan pengulangan yang pantas.

**Bagaimana ia berfungsi dalam amalan**: Anda boleh menggunakan parser yang telah dibina untuk mengekstrak maklumat daripada input pengguna, modul memori untuk menyimpan dan mendapatkan data, dan penjana arahan untuk berinteraksi dengan pengguna, semuanya tanpa perlu membina komponen ini dari awal.

**Contoh kod**. Mari kita lihat contoh bagaimana anda boleh menggunakan Penyambung AI yang telah dibina dengan Semantic Kernel Python dan .Net yang menggunakan panggilan fungsi automatik untuk membolehkan model bertindak balas terhadap input pengguna:

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

Apa yang anda boleh lihat daripada contoh ini ialah bagaimana anda boleh memanfaatkan parser yang telah dibina untuk mengekstrak maklumat utama daripada input pengguna, seperti asal, destinasi, dan tarikh permintaan tempahan penerbangan. Pendekatan modular ini membolehkan anda memberi tumpuan kepada logik tahap tinggi.

### Manfaatkan Alat Kolaboratif

Rangka kerja seperti CrewAI, Microsoft AutoGen, dan Semantic Kernel memudahkan penciptaan pelbagai ejen yang boleh bekerjasama.

**Bagaimana pasukan boleh menggunakan ini**: Pasukan boleh mereka bentuk ejen dengan peranan dan tugas tertentu, membolehkan mereka menguji dan memperbaiki aliran kerja kolaboratif dan meningkatkan kecekapan sistem keseluruhan.

**Bagaimana ia berfungsi dalam amalan**: Anda boleh mencipta pasukan ejen di mana setiap ejen mempunyai fungsi khusus, seperti pengambilan data, analisis, atau membuat keputusan. Ejen ini boleh berkomunikasi dan berkongsi maklumat untuk mencapai matlamat bersama, seperti menjawab pertanyaan pengguna atau menyelesaikan tugas.

**Contoh kod (AutoGen)**:

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

Apa yang anda lihat dalam kod sebelumnya ialah bagaimana anda boleh mencipta tugas yang melibatkan pelbagai ejen bekerjasama untuk menganalisis data. Setiap ejen melaksanakan fungsi tertentu, dan tugas itu dilaksanakan dengan menyelaraskan ejen untuk mencapai hasil yang diinginkan. Dengan mencipta ejen berdedikasi dengan peranan khusus, anda boleh meningkatkan kecekapan dan prestasi tugas.

### Belajar dalam Masa Nyata

Rangka kerja maju menyediakan keupayaan untuk memahami konteks masa nyata dan penyesuaian.

**Bagaimana pasukan boleh menggunakan ini**: Pasukan boleh melaksanakan gelung maklum balas di mana ejen belajar daripada interaksi dan menyesuaikan tingkah laku mereka secara dinamik, membawa kepada peningkatan berterusan dan penambahbaikan keupayaan.

**Bagaimana ia berfungsi dalam amalan**: Ejen boleh menganalisis maklum balas pengguna, data persekitaran, dan hasil tugas untuk mengemas kini pangkalan pengetahuan mereka, menyesuaikan algoritma membuat keputusan, dan meningkatkan prestasi dari semasa ke semasa. Proses pembelajaran berulang ini membolehkan ejen menyesuaikan diri dengan keadaan yang berubah dan keutamaan pengguna, meningkatkan keberkesanan sistem keseluruhan.

## Apakah perbezaan antara rangka kerja AutoGen, Semantic Kernel dan Azure AI Agent Service?

Terdapat banyak cara untuk membandingkan rangka kerja ini, tetapi mari kita lihat beberapa perbezaan utama dari segi reka bentuk, keupayaan, dan kes penggunaan sasaran:

## AutoGen

AutoGen adalah rangka kerja sumber terbuka yang dibangunkan oleh Microsoft Research's AI Frontiers Lab. Ia memberi tumpuan kepada aplikasi *agentic* yang didorong oleh peristiwa dan diedarkan, membolehkan pelbagai LLM dan SLM, alat, dan corak reka bentuk ejen berbilang maju.

AutoGen dibina di sekitar konsep teras ejen, iaitu entiti autonomi yang boleh memahami persekitaran mereka, membuat keputusan, dan mengambil tindakan untuk mencapai matlamat tertentu. Ejen berkomunikasi melalui mesej tak segerak, membolehkan mereka bekerja secara bebas dan selari, meningkatkan skalabiliti dan responsif sistem.

<a href="https://en.wikipedia.org/wiki/Actor_model" target="_blank">Ejen adalah berdasarkan model pelakon</a>. Menurut Wikipedia, pelakon adalah _blok asas pengiraan serentak. Sebagai tindak balas kepada mesej yang diterima, pelakon boleh: membuat keputusan tempatan, mencipta lebih banyak pelakon, menghantar lebih banyak mesej, dan menentukan bagaimana untuk bertindak balas terhadap mesej seterusnya yang diterima_.

**Kes Penggunaan**: Mengautomasi penjanaan kod, tugas analisis data, dan membina ejen tersuai untuk fungsi perancangan dan penyelidikan.

Berikut adalah beberapa konsep teras penting AutoGen:

- **Ejen**. Ejen adalah entiti perisian yang:
  - **Berkomunikasi melalui mesej**, mesej ini boleh menjadi segerak atau tak segerak.
  - **Mengekalkan keadaan sendiri**, yang boleh diubah oleh mesej masuk.
  - **Melaksanakan tindakan** sebagai tindak balas kepada mesej yang diterima atau perubahan dalam keadaannya. Tindakan ini boleh mengubah keadaan ejen dan menghasilkan kesan luaran, seperti mengemas kini log mesej, menghantar mesej baru, melaksanakan kod, atau membuat panggilan API.
    
  Berikut adalah potongan kod pendek di mana anda mencipta ejen anda sendiri dengan keupayaan Chat:

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
    
    Dalam kod sebelumnya, `MyAgent` telah dicipta dan mewarisi daripada `RoutedAgent`. Ia mempunyai pengendali mesej yang mencetak kandungan mesej dan kemudian menghantar respons menggunakan delegasi `AssistantAgent`. Perhatikan terutamanya bagaimana kita menetapkan kepada `self._delegate` satu instance `AssistantAgent` yang merupakan ejen yang telah dibina yang boleh mengendalikan penyelesaian chat.


    Mari kita maklumkan kepada AutoGen tentang jenis ejen ini dan mulakan program seterusnya:

    ```python
    
    # main.py
    runtime = SingleThreadedAgentRuntime()
    await MyAgent.register(runtime, "my_agent", lambda: MyAgent())

    runtime.start()  # Start processing messages in the background.
    await runtime.send_message(MyMessageType("Hello, World!"), AgentId("my_agent", "default"))
    ```

    Dalam kod sebelumnya ejen didaftarkan dengan runtime dan kemudian mesej dihantar kepada ejen yang menghasilkan output berikut:

    ```text
    # Output from the console:
    my_agent received message: Hello, World!
    my_assistant received message: Hello, World!
    my_assistant responded: Hello! How can I assist you today?
    ```

- **Ejen Berbilang**. AutoGen menyokong penciptaan pelbagai ejen yang boleh bekerjasama untuk mencapai tugas yang kompleks. Ejen boleh berkomunikasi, berkongsi maklumat, dan menyelaraskan tindakan mereka untuk menyelesaikan masalah dengan lebih cekap. Untuk mencipta sistem ejen berbilang, anda boleh menentukan jenis ejen yang berbeza dengan fungsi dan peranan khusus, seperti pengambilan data, analisis, membuat keputusan, dan interaksi pengguna. Mari kita lihat bagaimana penciptaan sedemikian kelihatan supaya kita mendapat gambaran mengenainya:

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

    Dalam kod sebelumnya kita mempunyai `GroupChatManager` yang didaftarkan dengan runtime. Pengurus ini bertanggungjawab untuk menyelaraskan interaksi antara jenis ejen yang berbeza, seperti penulis, ilustrator, editor, dan pengguna.

- **Runtime Ejen**. Rangka kerja menyediakan persekitaran runtime, membolehkan komunikasi antara ejen, mengurus identiti dan kitaran hayat mereka, dan menguatkuasakan sempadan keselamatan dan privasi. Ini bermakna anda boleh menjalankan ejen anda dalam persekitaran yang selamat dan terkawal, memastikan mereka boleh berinteraksi dengan selamat dan cekap. Terdapat dua runtime yang menarik:
  - **Runtime berdiri sendiri**. Ini adalah pilihan yang baik untuk aplikasi proses tunggal di mana semua ejen dilaksanakan dalam bahasa pengaturcaraan yang sama dan berjalan dalam proses yang sama. Berikut adalah ilustrasi bagaimana ia berfungsi:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-standalone.svg" target="_blank">Runtime berdiri sendiri</a>   
Tumpukan aplikasi

    *ejen berkomunikasi melalui mesej melalui runtime, dan runtime menguruskan kitaran hayat ejen*

  - **Runtime ejen diedarkan**, sesuai untuk aplikasi berbilang proses di mana ejen mungkin dilaksanakan dalam bahasa pengaturcaraan yang berbeza dan berjalan pada mesin yang berbeza. Berikut adalah ilustrasi bagaimana ia berfungsi:
  
    <a href="https://microsoft.github.io/autogen/stable/_images/architecture-distributed.svg" target="_blank">Runtime diedarkan</a>

## Semantic Kernel + Rangka Kerja Ejen

Semantic Kernel adalah SDK Orkestrasi AI yang sedia untuk perusahaan. Ia terdiri daripada penyambung AI dan memori, bersama dengan Rangka Kerja Ejen.

Mari kita mula-mula merangkumi beberapa komponen teras:

- **Penyambung AI**: Ini adalah antara muka dengan perkhidmatan AI luaran dan sumber data untuk digunakan dalam Python dan C#.

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

    Di sini anda mempunyai contoh mudah bagaimana anda boleh mencipta kernel dan menambah perkhidmatan penyelesaian chat. Semantic Kernel mencipta sambungan kepada perkhidmatan AI luaran, dalam kes ini, Azure OpenAI Chat Completion.

- **Plugin**: Ini merangkumi fungsi yang boleh digunakan oleh aplikasi. Terdapat plugin yang telah sedia ada dan plugin tersuai yang boleh anda cipta. Konsep berkaitan adalah "fungsi arahan." Daripada memberikan petunjuk bahasa semula jadi untuk pemanggilan fungsi, anda menyiarkan fungsi tertentu kepada model. Berdasarkan konteks chat semasa, model mungkin memilih untuk memanggil salah satu fungsi ini untuk melengkapkan permintaan atau pertanyaan. Berikut adalah contoh:

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

    Di sini, anda mula-mula mempunyai templat arahan `skPrompt` yang meninggalkan ruang untuk pengguna memasukkan teks, `$userInput`. Kemudian anda mencipta fungsi kernel `SummarizeText` dan kemudian mengimportnya ke dalam kernel dengan nama plugin `SemanticFunctions`. Perhatikan nama fungsi yang membantu Semantic Kernel memahami apa yang dilakukan oleh fungsi dan bila ia harus dipanggil.

- **Fungsi Asli**: Terdapat juga fungsi asli yang boleh dipanggil oleh rangka kerja secara langsung untuk melaksanakan tugas. Berikut adalah contoh fungsi sedemikian yang mendapatkan kandungan daripada fail:

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

- **Memori**: Abstrak dan mempermudah pengurusan konteks untuk aplikasi AI. Idea dengan memori adalah bahawa ini adalah sesuatu yang harus diketahui oleh LLM. Anda boleh menyimpan maklumat ini dalam stor vektor yang akhirnya menjadi pangkalan data dalam memori atau pangkalan data vektor atau serupa. Berikut adalah contoh senario yang sangat dipermudahkan di mana *fakta* ditambahkan ke dalam memori:

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

Fakta-fakta ini kemudian disimpan dalam koleksi memori `SummarizedAzureDocs`. Ini adalah contoh yang sangat ringkas, tetapi anda dapat melihat bagaimana maklumat boleh disimpan dalam memori untuk digunakan oleh LLM.

Jadi, itulah asas rangka kerja Semantic Kernel, bagaimana pula dengan Agent Framework?

## Perkhidmatan Azure AI Agent

Perkhidmatan Azure AI Agent adalah tambahan yang lebih baru, diperkenalkan di Microsoft Ignite 2024. Ia membolehkan pembangunan dan penyebaran agen AI dengan model yang lebih fleksibel, seperti memanggil LLM sumber terbuka secara langsung seperti Llama 3, Mistral, dan Cohere.

Perkhidmatan Azure AI Agent menyediakan mekanisme keselamatan perusahaan yang lebih kuat dan kaedah penyimpanan data, menjadikannya sesuai untuk aplikasi perusahaan.

Ia berfungsi secara langsung dengan rangka kerja orkestrasi multi-agen seperti AutoGen dan Semantic Kernel.

Perkhidmatan ini kini dalam Pratonton Awam dan menyokong Python dan C# untuk membina agen.

Menggunakan Semantic Kernel Python, kita boleh mencipta Azure AI Agent dengan plugin yang ditentukan pengguna:

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

### Konsep Teras

Perkhidmatan Azure AI Agent mempunyai konsep teras berikut:

- **Agen**. Perkhidmatan Azure AI Agent berintegrasi dengan Azure AI Foundry. Dalam AI Foundry, Agen AI bertindak sebagai mikroservis "pintar" yang boleh digunakan untuk menjawab soalan (RAG), melaksanakan tindakan, atau mengautomasikan aliran kerja sepenuhnya. Ia mencapai ini dengan menggabungkan kuasa model AI generatif dengan alat yang membolehkannya mengakses dan berinteraksi dengan sumber data dunia nyata. Berikut adalah contoh agen:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    Dalam contoh ini, agen dicipta dengan model `gpt-4o-mini`, nama `my-agent`, dan arahan `You are helpful agent`. Agen ini dilengkapi dengan alat dan sumber untuk melaksanakan tugas interpretasi kod.

- **Thread dan mesej**. Thread adalah konsep penting yang lain. Ia mewakili perbualan atau interaksi antara agen dan pengguna. Thread boleh digunakan untuk menjejaki kemajuan perbualan, menyimpan maklumat konteks, dan menguruskan keadaan interaksi. Berikut adalah contoh thread:

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

    Dalam kod sebelumnya, thread dicipta. Selepas itu, mesej dihantar ke thread. Dengan memanggil `create_and_process_run`, agen diminta untuk melaksanakan kerja pada thread. Akhirnya, mesej diambil dan direkodkan untuk melihat respons agen. Mesej menunjukkan kemajuan perbualan antara pengguna dan agen. Penting juga untuk memahami bahawa mesej boleh terdiri daripada pelbagai jenis seperti teks, imej, atau fail, yang mana kerja agen menghasilkan, contohnya, imej atau respons teks. Sebagai pembangun, anda boleh menggunakan maklumat ini untuk memproses respons lebih lanjut atau menyampaikannya kepada pengguna.

- **Berintegrasi dengan rangka kerja AI lain**. Perkhidmatan Azure AI Agent boleh berinteraksi dengan rangka kerja lain seperti AutoGen dan Semantic Kernel, yang bermaksud anda boleh membina sebahagian aplikasi anda dalam salah satu rangka kerja ini dan contohnya menggunakan perkhidmatan Agen sebagai pengatur atau anda boleh membina semuanya dalam perkhidmatan Agen.

**Kes Penggunaan**: Perkhidmatan Azure AI Agent direka untuk aplikasi perusahaan yang memerlukan penyebaran agen AI yang selamat, boleh diskalakan, dan fleksibel.

## Apakah perbezaan antara rangka kerja ini?

Nampaknya terdapat banyak persamaan antara rangka kerja ini, tetapi terdapat beberapa perbezaan utama dari segi reka bentuk, keupayaan, dan kes penggunaan sasaran:

- **AutoGen**: Adalah rangka kerja eksperimen yang memberi tumpuan kepada penyelidikan terkini mengenai sistem multi-agen. Ia adalah tempat terbaik untuk bereksperimen dan membuat prototaip sistem multi-agen yang canggih.
- **Semantic Kernel**: Adalah perpustakaan agen yang sedia untuk pengeluaran untuk membina aplikasi agen perusahaan. Memberi tumpuan kepada aplikasi agen yang didorong oleh acara, diedarkan, membolehkan pelbagai LLM dan SLM, alat, dan corak reka bentuk agen tunggal/multi.
- **Azure AI Agent Service**: Adalah platform dan perkhidmatan penyebaran dalam Azure Foundry untuk agen. Ia menawarkan sambungan kepada perkhidmatan yang disokong oleh Azure seperti Azure OpenAI, Azure AI Search, Bing Search dan pelaksanaan kod.

Masih tidak pasti mana yang hendak dipilih?

### Kes Penggunaan

Mari kita lihat jika kita boleh membantu anda dengan melalui beberapa kes penggunaan biasa:

> S: Saya sedang bereksperimen, belajar dan membina aplikasi agen bukti konsep, dan saya mahu dapat membina dan bereksperimen dengan cepat
>

>J: AutoGen akan menjadi pilihan yang baik untuk senario ini, kerana ia memberi tumpuan kepada aplikasi agen yang didorong oleh acara, diedarkan dan menyokong corak reka bentuk multi-agen yang canggih.

> S: Apa yang menjadikan AutoGen pilihan yang lebih baik daripada Semantic Kernel dan Azure AI Agent Service untuk kes penggunaan ini?
>
> J: AutoGen direka khusus untuk aplikasi agen yang didorong oleh acara, diedarkan, menjadikannya sangat sesuai untuk mengautomasikan penjanaan kod dan tugas analisis data. Ia menyediakan alat dan keupayaan yang diperlukan untuk membina sistem multi-agen yang kompleks dengan cekap.

>S: Nampaknya Azure AI Agent Service juga boleh berfungsi di sini, ia mempunyai alat untuk penjanaan kod dan banyak lagi?

>
> J: Ya, Azure AI Agent Service adalah perkhidmatan platform untuk agen dan menambah keupayaan terbina dalam untuk pelbagai model, Azure AI Search, Bing Search dan Azure Functions. Ia memudahkan untuk membina agen anda di Foundry Portal dan menyebarkannya pada skala.
 
> S: Saya masih keliru, berikan saya satu pilihan sahaja
>
> J: Pilihan yang hebat adalah untuk membina aplikasi anda dalam Semantic Kernel terlebih dahulu dan kemudian menggunakan Azure AI Agent Service untuk menyebarkan agen anda. Pendekatan ini membolehkan anda dengan mudah mengekalkan agen anda sambil memanfaatkan kuasa untuk membina sistem multi-agen dalam Semantic Kernel. Selain itu, Semantic Kernel mempunyai penyambung dalam AutoGen, menjadikannya mudah untuk menggunakan kedua-dua rangka kerja bersama-sama.

Mari kita ringkaskan perbezaan utama dalam jadual:

| Rangka Kerja | Fokus | Konsep Teras | Kes Penggunaan |
| --- | --- | --- | --- |
| AutoGen | Aplikasi agen yang didorong oleh acara, diedarkan | Agen, Persona, Fungsi, Data | Penjanaan kod, tugas analisis data |
| Semantic Kernel | Memahami dan menjana kandungan teks seperti manusia | Agen, Komponen Modular, Kolaborasi | Pemahaman bahasa semula jadi, penjanaan kandungan |
| Azure AI Agent Service | Model fleksibel, keselamatan perusahaan, Penjanaan kod, Panggilan alat | Modulariti, Kolaborasi, Orkestrasi Proses | Penyebaran agen AI yang selamat, boleh diskalakan, dan fleksibel |

Apakah kes penggunaan ideal untuk setiap rangka kerja ini?

## Bolehkah saya mengintegrasikan alat ekosistem Azure sedia ada saya secara langsung, atau adakah saya memerlukan penyelesaian yang berdiri sendiri?

Jawapannya adalah ya, anda boleh mengintegrasikan alat ekosistem Azure sedia ada anda secara langsung dengan Azure AI Agent Service terutamanya, kerana ia dibina untuk berfungsi dengan lancar dengan perkhidmatan Azure yang lain. Sebagai contoh, anda boleh mengintegrasikan Bing, Azure AI Search, dan Azure Functions. Terdapat juga integrasi mendalam dengan Azure AI Foundry.

Untuk AutoGen dan Semantic Kernel, anda juga boleh mengintegrasikan dengan perkhidmatan Azure, tetapi ia mungkin memerlukan anda memanggil perkhidmatan Azure dari kod anda. Cara lain untuk mengintegrasikan adalah dengan menggunakan SDK Azure untuk berinteraksi dengan perkhidmatan Azure dari agen anda. Selain itu, seperti yang disebutkan, anda boleh menggunakan Azure AI Agent Service sebagai pengatur untuk agen anda yang dibina dalam AutoGen atau Semantic Kernel yang akan memberikan akses mudah ke ekosistem Azure.

## Kod Contoh

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Ada Lagi Soalan tentang Rangka Kerja AI Agent?

Sertai [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) untuk bertemu dengan pelajar lain, menghadiri waktu pejabat dan mendapatkan jawapan kepada soalan AI Agents anda.

## Rujukan

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/" target="_blank">Semantic Kernel dan AutoGen</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-python" target="_blank">Semantic Kernel Python Agent Framework</a>
- <a href="https://learn.microsoft.com/semantic-kernel/frameworks/agent/?pivots=programming-language-csharp" target="_blank">Semantic Kernel .Net Agent Framework</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>
- <a href="https://techcommunity.microsoft.com/blog/educatordeveloperblog/using-azure-ai-agent-service-with-autogen--semantic-kernel-to-build-a-multi-agen/4363121" target="_blank">Menggunakan Azure AI Agent Service dengan AutoGen / Semantic Kernel untuk membina penyelesaian multi-agen</a>

## Pelajaran Sebelumnya

[Pengenalan kepada AI Agents dan Kes Penggunaan Agen](../01-intro-to-ai-agents/README.md)

## Pelajaran Seterusnya

[Memahami Corak Reka Bentuk Agen](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->