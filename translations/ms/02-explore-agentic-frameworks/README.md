[![Meneroka Rangka Kerja Agen AI](../../../translated_images/ms/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Klik gambar di atas untuk menonton video pelajaran ini)_

# Terokai Rangka Kerja Agen AI

Rangka kerja agen AI adalah platform perisian yang direka untuk memudahkan penciptaan, penyebaran, dan pengurusan agen AI. Rangka kerja ini menyediakan komponen siap guna, abstraksi, dan alat kepada pembangun yang mempermudah pembangunan sistem AI yang kompleks.

Rangka kerja ini membantu pembangun memberi tumpuan kepada aspek unik aplikasi mereka dengan menyediakan pendekatan piawai untuk cabaran biasa dalam pembangunan agen AI. Ia meningkatkan kebolehlapangan, kemudahan capaian, dan kecekapan dalam membina sistem AI.

## Pengenalan 

Pelajaran ini akan meliputi:

- Apakah Rangka Kerja Agen AI dan apa yang dapat dicapai oleh pembangun?
- Bagaimana pasukan boleh menggunakan ini untuk membuat prototaip dengan cepat, mengulangi, dan memperbaiki keupayaan agen mereka?
- Apakah perbezaan antara rangka kerja dan alat yang dibuat oleh Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> dan <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Bolehkah saya mengintegrasikan alat ekosistem Azure sedia ada saya secara langsung, atau adakah saya perlu penyelesaian berdiri sendiri?
- Apakah Microsoft Foundry Agent Service dan bagaimana ia membantu saya?

## Matlamat pembelajaran

Matlamat pelajaran ini adalah untuk membantu anda memahami:

- Peranan Rangka Kerja Agen AI dalam pembangunan AI.
- Cara memanfaatkan Rangka Kerja Agen AI untuk membina agen pintar.
- Keupayaan utama yang diaktifkan oleh Rangka Kerja Agen AI.
- Perbezaan antara Microsoft Agent Framework dan Microsoft Foundry Agent Service.

## Apakah Rangka Kerja Agen AI dan apa yang dapat dilakukan oleh pembangun?

Rangka Kerja AI Tradisional dapat membantu anda mengintegrasikan AI ke dalam aplikasi anda dan memperbaiki aplikasi ini dengan cara berikut:

- **Personalisasi**: AI dapat menganalisis tingkah laku dan keutamaan pengguna untuk memberikan cadangan, kandungan, dan pengalaman yang diperibadikan.
Contoh: Perkhidmatan penstriman seperti Netflix menggunakan AI untuk mencadangkan filem dan rancangan berdasarkan sejarah tontonan, meningkatkan penglibatan dan kepuasan pengguna.
- **Automasi dan Kecekapan**: AI dapat mengautomasi tugas berulang, mempermudah aliran kerja, dan meningkatkan kecekapan operasi.
Contoh: Aplikasi perkhidmatan pelanggan menggunakan chatbot bertenaga AI untuk mengendalikan pertanyaan biasa, mengurangkan masa tindak balas dan membebaskan agen manusia untuk isu yang lebih kompleks.
- **Pengalaman Pengguna yang Ditingkatkan**: AI dapat meningkatkan pengalaman pengguna secara keseluruhan dengan menyediakan ciri pintar seperti pengecaman suara, pemprosesan bahasa semulajadi, dan teks ramalan.
Contoh: Pembantu maya seperti Siri dan Google Assistant menggunakan AI untuk memahami dan bertindak balas terhadap arahan suara, memudahkan pengguna berinteraksi dengan peranti mereka.

### Semuanya kedengaran hebat, jadi mengapa kita memerlukan Rangka Kerja Agen AI?

Rangka kerja Agen AI mewakili sesuatu yang lebih daripada sekadar rangka kerja AI biasa. Ia direka untuk membolehkan penciptaan agen pintar yang boleh berinteraksi dengan pengguna, agen lain, dan persekitaran untuk mencapai matlamat tertentu. Agen ini boleh menunjukkan tingkah laku autonomi, membuat keputusan, dan menyesuaikan diri dengan keadaan yang berubah. Mari kita lihat beberapa keupayaan utama yang diaktifkan oleh Rangka Kerja Agen AI:

- **Kerjasama dan Penyelarasan Agen**: Membolehkan penciptaan pelbagai agen AI yang boleh bekerja bersama, berkomunikasi, dan menyelaraskan untuk menyelesaikan tugas kompleks.
- **Automasi dan Pengurusan Tugas**: Menyediakan mekanisme untuk mengautomasi aliran kerja berbilang langkah, delegasi tugas, dan pengurusan tugas dinamik di kalangan agen.
- **Pemahaman Konteks dan Penyesuaian**: Melengkapi agen dengan keupayaan untuk memahami konteks, menyesuaikan diri dengan persekitaran yang berubah, dan membuat keputusan berdasarkan maklumat masa nyata.

Jadi ringkasnya, agen membolehkan anda melakukan lebih banyak, membawa automasi ke tahap seterusnya, untuk mencipta sistem yang lebih pintar yang boleh menyesuaikan diri dan belajar dari persekitaran mereka.

## Bagaimana untuk membuat prototaip dengan cepat, mengulangi, dan memperbaiki keupayaan agen?

Ini adalah landskap yang bergerak pantas, tetapi terdapat beberapa perkara yang biasa dalam kebanyakan Rangka Kerja Agen AI yang dapat membantu anda membuat prototaip dengan cepat dan mengulangi, iaitu komponen modul, alat kolaboratif, dan pembelajaran masa nyata. Mari kita teliti ini:

- **Gunakan Komponen Modular**: SDK AI menawarkan komponen siap guna seperti penyambung AI dan Memori, panggilan fungsi menggunakan bahasa semulajadi atau pemalam kod, templat arahan, dan banyak lagi.
- **Manfaatkan Alat Kolaboratif**: Reka agen dengan peranan dan tugas tertentu, membolehkan mereka menguji dan memperkemaskan aliran kerja kolaboratif.
- **Belajar Secara Masa Nyata**: Laksanakan gelung maklum balas di mana agen belajar dari interaksi dan melaraskan tingkah laku mereka secara dinamik.

### Gunakan Komponen Modular

SDK seperti Microsoft Agent Framework menawarkan komponen siap bina seperti penyambung AI, definisi alat, dan pengurusan agen.

**Bagaimana pasukan boleh menggunakan ini**: Pasukan boleh dengan cepat menyusun komponen ini untuk mencipta prototaip berfungsi tanpa perlu memulakan dari kosong, membolehkan eksperimen dan pengulangan yang pantas.

**Bagaimana ia berfungsi dalam praktik**: Anda boleh menggunakan parser siap bina untuk mengekstrak maklumat daripada input pengguna, modul memori untuk menyimpan dan mengambil data, dan penjana arahan untuk berinteraksi dengan pengguna, semua tanpa perlu membina komponen ini dari awal.

**Contoh kod**. Mari kita lihat contoh bagaimana anda boleh menggunakan Microsoft Agent Framework dengan `FoundryChatClient` untuk membuat model bertindak balas kepada input pengguna dengan panggilan alat:

``` python
# Contoh Microsoft Agent Framework Python

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Definisikan fungsi alat contoh untuk menempah perjalanan
@tool(approval_mode="never_require")
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # Contoh output: Penerbangan anda ke New York pada 1 Januari 2025 telah berjaya ditempah. Selamat jalan! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Apa yang anda dapat lihat dari contoh ini adalah bagaimana anda boleh memanfaatkan parser siap bina untuk mengekstrak maklumat utama dari input pengguna, seperti asal, destinasi, dan tarikh permintaan tempahan penerbangan. Pendekatan modular ini membolehkan anda memberi tumpuan kepada logik peringkat tinggi.

### Manfaatkan Alat Kolaboratif

Rangka kerja seperti Microsoft Agent Framework memudahkan penciptaan pelbagai agen yang boleh bekerja bersama.

**Bagaimana pasukan boleh menggunakan ini**: Pasukan boleh mereka agen dengan peranan dan tugas khusus, membolehkan mereka menguji dan memperkemaskan aliran kerja kolaboratif serta meningkatkan kecekapan sistem keseluruhan.

**Bagaimana ia berfungsi dalam praktik**: Anda boleh mencipta satu pasukan agen di mana setiap agen mempunyai fungsi khusus, seperti pengambilan data, analisis, atau membuat keputusan. Agen ini boleh berkomunikasi dan berkongsi maklumat untuk mencapai matlamat bersama, seperti menjawab pertanyaan pengguna atau menyelesaikan tugas.

**Contoh kod (Microsoft Agent Framework)**:

```python
# Mewujudkan pelbagai ejen yang bekerja bersama menggunakan Rangka Kerja Ejen Microsoft

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Ejen Pengambilan Data
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Ejen Analisis Data
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Menjalankan ejen secara berurutan dalam satu tugasan
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Apa yang anda lihat dalam kod sebelumnya adalah bagaimana anda boleh mencipta tugasan yang melibatkan pelbagai agen bekerja bersama untuk menganalisis data. Setiap agen melakukan fungsi khusus, dan tugasan dilaksanakan dengan menyelaras agen-agen tersebut untuk mencapai hasil yang dikehendaki. Dengan mencipta agen khusus dengan peranan khusus, anda boleh meningkatkan kecekapan dan prestasi tugasan.

### Belajar Secara Masa Nyata

Rangka kerja canggih menyediakan keupayaan untuk pemahaman konteks masa nyata dan penyesuaian.

**Bagaimana pasukan boleh menggunakan ini**: Pasukan boleh melaksanakan gelung maklum balas di mana agen belajar dari interaksi dan melaraskan tingkah laku mereka secara dinamik, membawa kepada peningkatan berterusan dan penambahbaikan keupayaan.

**Bagaimana ia berfungsi dalam praktik**: Agen boleh menganalisis maklum balas pengguna, data persekitaran, dan hasil tugasan untuk mengemas kini pangkalan pengetahuan mereka, melaraskan algoritma membuat keputusan, dan meningkatkan prestasi dari masa ke masa. Proses pembelajaran iteratif ini membolehkan agen menyesuaikan diri dengan keadaan dan keutamaan pengguna yang berubah, meningkatkan keberkesanan sistem keseluruhan.

## Apakah perbezaan antara Microsoft Agent Framework dan Microsoft Foundry Agent Service?

Terdapat banyak cara untuk membandingkan pendekatan ini, tetapi mari lihat beberapa perbezaan utama dari segi reka bentuk, keupayaan, dan kes kegunaan sasaran:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework menyediakan SDK yang dipermudahkan untuk membina agen AI menggunakan `FoundryChatClient`. Ia membolehkan pembangun mencipta agen yang menggunakan model Azure OpenAI dengan panggilan alat terbina dalam, pengurusan perbualan, dan keselamatan tahap perusahaan melalui identiti Azure.

**Kes Penggunaan**: Membina agen AI yang sudah sedia untuk produksi dengan penggunaan alat, aliran kerja berbilang langkah, dan senario integrasi perusahaan.

Berikut adalah beberapa konsep teras penting Microsoft Agent Framework:

- **Agen**. Agen dicipta melalui `FoundryChatClient` dan dikonfigurasikan dengan nama, arahan, dan alat. Agen boleh:
  - **Memproses mesej pengguna** dan menjana respons menggunakan model Azure OpenAI.
  - **Memanggil alat** secara automatik berdasarkan konteks perbualan.
  - **Mengekalkan keadaan perbualan** merentasi pelbagai interaksi.

  Berikut adalah cuplikan kod yang menunjukkan bagaimana untuk mencipta agen:

    ```python
    import os
    from agent_framework.foundry import FoundryChatClient
    from azure.identity import AzureCliCredential

    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **Alat**. Rangka kerja menyokong mendefinisikan alat sebagai fungsi Python yang boleh dipanggil oleh agen secara automatik. Alat didaftarkan ketika mencipta agen:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = provider.as_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **Penyelarasan Multi-Agen**. Anda boleh mencipta pelbagai agen dengan pengkhususan berbeza dan menyelaraskan kerja mereka:

    ```python
    planner = provider.as_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = provider.as_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Integrasi Identiti Azure**. Rangka kerja menggunakan `AzureCliCredential` (atau `DefaultAzureCredential`) untuk pengesahan selamat tanpa kunci, menghilangkan keperluan menguruskan kunci API secara langsung.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service adalah penambahan terkini, diperkenalkan di Microsoft Ignite 2024. Ia membolehkan pembangunan dan penyebaran agen AI dengan model yang lebih fleksibel, seperti memanggil secara langsung LLM sumber terbuka seperti Llama 3, Mistral, dan Cohere.

Microsoft Foundry Agent Service menyediakan mekanisme keselamatan perusahaan yang lebih kuat dan kaedah penyimpanan data, menjadikannya sesuai untuk aplikasi perusahaan.

Ia berfungsi terus dengan Microsoft Agent Framework untuk membina dan menyebarkan agen.

Perkhidmatan ini kini dalam Pratonton Awam dan menyokong Python dan C# untuk membina agen.

Menggunakan SDK Python Microsoft Foundry Agent Service, kita boleh mencipta agen dengan alat yang ditakrif pengguna:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Takrifkan fungsi alat
def get_specials() -> str:
    """Provides a list of specials from the menu."""
    return """
    Special Soup: Clam Chowder
    Special Salad: Cobb Salad
    Special Drink: Chai Tea
    """

def get_item_price(menu_item: str) -> str:
    """Provides the price of the requested menu item."""
    return "$9.99"


async def main() -> None:
    credential = DefaultAzureCredential()
    project_client = AIProjectClient.from_connection_string(
        credential=credential,
        conn_str="your-connection-string",
    )

    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="Host",
        instructions="Answer questions about the menu.",
        tools=[get_specials, get_item_price],
    )

    thread = project_client.agents.create_thread()

    user_inputs = [
        "Hello",
        "What is the special soup?",
        "How much does that cost?",
        "Thank you",
    ]

    for user_input in user_inputs:
        print(f"# User: '{user_input}'")
        message = project_client.agents.create_message(
            thread_id=thread.id,
            role="user",
            content=user_input,
        )
        run = project_client.agents.create_and_process_run(
            thread_id=thread.id, agent_id=agent.id
        )
        messages = project_client.agents.list_messages(thread_id=thread.id)
        print(f"# Agent: {messages.data[0].content[0].text.value}")


if __name__ == "__main__":
    asyncio.run(main())
```

### Konsep teras

Microsoft Foundry Agent Service mempunyai konsep teras berikut:

- **Agen**. Microsoft Foundry Agent Service berintegrasi dengan Microsoft Foundry. Dalam Microsoft Foundry, Agen AI bertindak sebagai mikroservis "pintar" yang boleh digunakan untuk menjawab soalan (RAG), melaksanakan tindakan, atau mengautomasi aliran kerja sepenuhnya. Ia mencapai ini dengan menggabungkan kuasa model AI generatif dengan alat yang membolehkannya mengakses dan berinteraksi dengan sumber data dunia sebenar. Berikut adalah contoh agen:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    Dalam contoh ini, agen dicipta dengan model `gpt-5-mini`, nama `my-agent`, dan arahan `You are helpful agent`. Agen dilengkapi dengan alat dan sumber untuk melaksanakan tugasan interpretasi kod.

- **Thread dan mesej**. Thread adalah konsep penting lain. Ia mewakili perbualan atau interaksi antara agen dan pengguna. Thread boleh digunakan untuk mengesan kemajuan perbualan, menyimpan maklumat konteks, dan menguruskan keadaan interaksi. Berikut adalah contoh thread:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Minta ejen untuk melakukan kerja pada utas
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Dapatkan dan catat semua mesej untuk melihat respons ejen
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    Dalam kod sebelum ini, suatu thread dicipta. Selepas itu, mesej dihantar ke thread. Dengan memanggil `create_and_process_run`, agen diminta untuk melaksanakan kerja dalam thread tersebut. Akhirnya, mesej diambil dan direkodkan untuk melihat respons agen. Mesej menunjukkan kemajuan perbualan antara pengguna dan agen. Ia juga penting untuk memahami bahawa mesej boleh dalam pelbagai jenis seperti teks, imej, atau fail, yang merupakan hasil kerja agen, contohnya imej atau respons teks. Sebagai pembangun, anda boleh menggunakan maklumat ini untuk memproses respons lebih lanjut atau menyampaikannya kepada pengguna.

- **Integrasi dengan Microsoft Agent Framework**. Microsoft Foundry Agent Service berfungsi dengan lancar dengan Microsoft Agent Framework, yang bermaksud anda boleh membina agen menggunakan `FoundryChatClient` dan menyebarkannya melalui Agent Service untuk senario produksi.

**Kes Penggunaan**: Microsoft Foundry Agent Service direka untuk aplikasi perusahaan yang memerlukan penyebaran agen AI yang selamat, boleh skala, dan fleksibel.

## Apakah perbezaan antara pendekatan ini?
 
Nampaknya ada pertindihan, tetapi terdapat beberapa perbezaan utama dari segi reka bentuk, keupayaan, dan kes kegunaan sasaran:
 
- **Microsoft Agent Framework (MAF)**: Adalah SDK yang sedia untuk produksi bagi membina agen AI. Ia menyediakan API yang dipermudahkan untuk mencipta agen dengan panggilan alat, pengurusan perbualan, dan integrasi identiti Azure.
- **Microsoft Foundry Agent Service**: Adalah platform dan perkhidmatan penyebaran dalam Microsoft Foundry untuk agen. Ia menawarkan sambungan terbina dalam kepada perkhidmatan seperti Azure OpenAI, Azure AI Search, Bing Search dan pelaksanaan kod.
 
Masih tidak pasti mana satu untuk dipilih?

### Kes Penggunaan
 
Mari kita lihat jika kami boleh membantu dengan melalui beberapa kes penggunaan biasa:
 
> S: Saya sedang membina aplikasi agen AI produksi dan mahu bermula dengan cepat
>

>J: Microsoft Agent Framework adalah pilihan yang baik. Ia menyediakan API yang mudah dan Pythonik melalui `FoundryChatClient` yang membolehkan anda mentakrifkan agen dengan alat dan arahan dalam hanya beberapa baris kod.

>S: Saya perlukan penyebaran tahap perusahaan dengan integrasi Azure seperti Search dan pelaksanaan kod
>
> J: Microsoft Foundry Agent Service adalah pilihan terbaik. Ia adalah perkhidmatan platform yang menyediakan keupayaan terbina dalam untuk pelbagai model, Azure AI Search, Bing Search dan Azure Functions. Ia memudahkan anda membina agen dalam Foundry Portal dan menyebarkannya pada skala besar.
 
> S: Saya masih keliru, berikan saya satu pilihan sahaja
>
> J: Mulakan dengan Microsoft Agent Framework untuk membina agen anda, kemudian gunakan Microsoft Foundry Agent Service apabila anda perlu menyebar dan menskalakan mereka dalam produksi. Pendekatan ini membolehkan anda mengulangi logik agen dengan pantas sambil mempunyai laluan jelas ke penyebaran perusahaan.
 
Mari kita ringkaskan perbezaan utama dalam jadual:

| Rangka Kerja | Fokus | Konsep Teras | Kes Penggunaan |
| --- | --- | --- | --- |
| Microsoft Agent Framework | SDK agen yang dipermudahkan dengan panggilan alat | Agen, Alat, Identiti Azure | Membina agen AI, penggunaan alat, aliran kerja berbilang langkah |
| Microsoft Foundry Agent Service | Model fleksibel, keselamatan perusahaan, penjanaan Kod, panggilan alat | Modulariti, Kolaborasi, Orkestrasi Proses | Penyebaran agen AI yang selamat, boleh skala, dan fleksibel |

## Bolehkah saya mengintegrasikan alat ekosistem Azure sedia ada saya secara langsung, atau adakah saya perlu penyelesaian berdiri sendiri?


Jawapannya adalah ya, anda boleh mengintegrasikan alat ekosistem Azure sedia ada anda terus dengan Perkhidmatan Ejen Microsoft Foundry terutamanya, kerana ia telah dibina untuk berfungsi dengan lancar dengan perkhidmatan Azure lain. Anda boleh contohnya mengintegrasikan Bing, Azure AI Search, dan Azure Functions. Terdapat juga integrasi mendalam dengan Microsoft Foundry.

Rangka Kerja Ejen Microsoft juga mengintegrasi dengan perkhidmatan Azure melalui `FoundryChatClient` dan identiti Azure, membolehkan anda memanggil perkhidmatan Azure terus dari alat ejen anda.

## Contoh Kod

- Python: [Rangka Kerja Ejen (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Rangka Kerja Ejen (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Rangka Kerja Ejen](./code_samples/02-dotnet-agent-framework.md)

## Ada Lagi Soalan tentang Rangka Kerja Ejen AI?

Sertai [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) untuk berjumpa dengan pelajar lain, menghadiri waktu pejabat dan dapatkan jawapan untuk soalan Ejen AI anda.

## Rujukan

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Perkhidmatan Ejen Azure</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Rangka Kerja Ejen Microsoft - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Perkhidmatan Ejen Microsoft Foundry</a>

## Pelajaran Sebelumnya

[Pengenalan kepada Ejen AI dan Kes Penggunaan Ejen](../01-intro-to-ai-agents/README.md)

## Pelajaran Seterusnya

[Memahami Corak Rekabentuk Agenik](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->