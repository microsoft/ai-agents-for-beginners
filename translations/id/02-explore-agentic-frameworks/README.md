[![Menjelajahi Kerangka Kerja Agen AI](../../../translated_images/id/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Klik gambar di atas untuk melihat video pelajaran ini)_

# Jelajahi Kerangka Kerja Agen AI

Kerangka kerja agen AI adalah platform perangkat lunak yang dirancang untuk menyederhanakan pembuatan, penyebaran, dan pengelolaan agen AI. Kerangka kerja ini menyediakan pengembang dengan komponen yang sudah dibuat sebelumnya, abstraksi, dan alat yang mempermudah pengembangan sistem AI yang kompleks.

Kerangka kerja ini membantu pengembang fokus pada aspek unik dari aplikasi mereka dengan menyediakan pendekatan standar untuk tantangan umum dalam pengembangan agen AI. Mereka meningkatkan skalabilitas, aksesibilitas, dan efisiensi dalam membangun sistem AI.

## Pendahuluan 

Pelajaran ini akan membahas:

- Apa itu Kerangka Kerja Agen AI dan apa yang memungkinkan pengembang untuk capai?
- Bagaimana tim dapat menggunakan ini untuk cepat membuat prototipe, iterasi, dan meningkatkan kemampuan agen mereka?
- Apa perbedaan antara kerangka kerja dan alat yang dibuat oleh Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> dan <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)?
- Bisakah saya mengintegrasikan alat ekosistem Azure saya yang sudah ada secara langsung, atau apakah saya memerlukan solusi mandiri?
- Apa itu Microsoft Foundry Agent Service dan bagaimana ini membantu saya?

## Tujuan Pembelajaran

Tujuan dari pelajaran ini adalah membantu Anda memahami:

- Peran Kerangka Kerja Agen AI dalam pengembangan AI.
- Cara memanfaatkan Kerangka Kerja Agen AI untuk membangun agen cerdas.
- Kemampuan utama yang diaktifkan oleh Kerangka Kerja Agen AI.
- Perbedaan antara Microsoft Agent Framework dan Microsoft Foundry Agent Service.

## Apa itu Kerangka Kerja Agen AI dan apa yang memungkinkan pengembang lakukan?

Kerangka kerja AI tradisional dapat membantu Anda mengintegrasikan AI ke dalam aplikasi Anda dan membuat aplikasi tersebut lebih baik dengan cara berikut:

- **Personalisasi**: AI dapat menganalisis perilaku dan preferensi pengguna untuk memberikan rekomendasi, konten, dan pengalaman yang dipersonalisasi.
Contoh: Layanan streaming seperti Netflix menggunakan AI untuk menyarankan film dan acara berdasarkan riwayat tontonan, meningkatkan keterlibatan dan kepuasan pengguna.
- **Automasi dan Efisiensi**: AI dapat mengotomatisasi tugas berulang, menyederhanakan alur kerja, dan meningkatkan efisiensi operasional.
Contoh: Aplikasi layanan pelanggan menggunakan chatbot bertenaga AI untuk menangani pertanyaan umum, mengurangi waktu respons dan membebaskan agen manusia untuk masalah yang lebih kompleks.
- **Peningkatan Pengalaman Pengguna**: AI dapat meningkatkan pengalaman pengguna secara keseluruhan dengan menyediakan fitur cerdas seperti pengenalan suara, pemrosesan bahasa alami, dan teks prediktif.
Contoh: Asisten virtual seperti Siri dan Google Assistant menggunakan AI untuk memahami dan merespons perintah suara, mempermudah pengguna berinteraksi dengan perangkat mereka.

### Semua itu terdengar hebat, jadi mengapa kita perlu Kerangka Kerja Agen AI?

Kerangka kerja Agen AI mewakili sesuatu yang lebih dari sekadar kerangka kerja AI. Mereka dirancang untuk memungkinkan pembuatan agen cerdas yang dapat berinteraksi dengan pengguna, agen lain, dan lingkungan untuk mencapai tujuan tertentu. Agen ini dapat menunjukkan perilaku otonom, mengambil keputusan, dan beradaptasi dengan kondisi yang berubah. Mari kita lihat beberapa kemampuan utama yang diaktifkan oleh Kerangka Kerja Agen AI:

- **Kolaborasi dan Koordinasi Agen**: Memungkinkan pembuatan banyak agen AI yang dapat bekerja sama, berkomunikasi, dan berkoordinasi untuk menyelesaikan tugas kompleks.
- **Automasi dan Manajemen Tugas**: Menyediakan mekanisme untuk mengotomatisasi alur kerja multi-langkah, delegasi tugas, dan manajemen tugas dinamis di antara agen.
- **Pemahaman Kontekstual dan Adaptasi**: Membekali agen dengan kemampuan untuk memahami konteks, beradaptasi dengan lingkungan yang berubah, dan mengambil keputusan berdasarkan informasi waktu nyata.

Jadi, singkatnya, agen memungkinkan Anda melakukan lebih banyak, membawa otomasi ke tingkat berikutnya, untuk menciptakan sistem yang lebih cerdas yang dapat beradaptasi dan belajar dari lingkungan mereka.

## Bagaimana cara cepat membuat prototipe, iterasi, dan meningkatkan kemampuan agen?

Ini adalah lanskap yang bergerak cepat, tetapi ada beberapa hal yang umum di sebagian besar Kerangka Kerja Agen AI yang dapat membantu Anda membuat prototipe dan iterasi dengan cepat, yaitu komponen modul, alat kolaboratif, dan pembelajaran waktu nyata. Mari kita selami ini:

- **Gunakan Komponen Modular**: SDK AI menawarkan komponen yang sudah dibuat sebelumnya seperti konektor AI dan Memori, pemanggilan fungsi menggunakan bahasa alami atau plugin kode, template prompt, dan lainnya.
- **Manfaatkan Alat Kolaboratif**: Rancang agen dengan peran dan tugas spesifik, memungkinkan mereka untuk menguji dan menyempurnakan alur kerja kolaboratif.
- **Belajar secara Real-Time**: Terapkan loop umpan balik di mana agen belajar dari interaksi dan menyesuaikan perilaku mereka secara dinamis.

### Gunakan Komponen Modular

SDK seperti Microsoft Agent Framework menawarkan komponen yang sudah dibuat seperti konektor AI, definisi alat, dan manajemen agen.

**Bagaimana tim dapat menggunakan ini**: Tim dapat dengan cepat merakit komponen ini untuk membuat prototipe fungsional tanpa memulai dari nol, memungkinkan eksperimen dan iterasi yang cepat.

**Bagaimana cara kerjanya dalam praktik**: Anda dapat menggunakan parser yang sudah dibuat untuk mengekstrak informasi dari masukan pengguna, modul memori untuk menyimpan dan mengambil data, dan generator prompt untuk berinteraksi dengan pengguna, semuanya tanpa harus membangun komponen ini dari awal.

**Contoh kode**. Mari kita lihat contoh bagaimana Anda dapat menggunakan Microsoft Agent Framework dengan `FoundryChatClient` untuk membuat model merespons masukan pengguna dengan pemanggilan alat:

``` python
# Contoh Microsoft Agent Framework Python

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Definisikan fungsi alat contoh untuk memesan perjalanan
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
    # Contoh output: Penerbangan Anda ke New York pada 1 Januari 2025 telah berhasil dipesan. Selamat jalan! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Apa yang Anda lihat dari contoh ini adalah bagaimana Anda dapat memanfaatkan parser yang sudah dibuat untuk mengekstrak informasi kunci dari masukan pengguna, seperti asal, tujuan, dan tanggal permintaan pemesanan penerbangan. Pendekatan modular ini memungkinkan Anda fokus pada logika tingkat tinggi.

### Manfaatkan Alat Kolaboratif

Kerangka kerja seperti Microsoft Agent Framework memfasilitasi pembuatan banyak agen yang dapat bekerja sama.

**Bagaimana tim dapat menggunakan ini**: Tim dapat merancang agen dengan peran dan tugas spesifik, memungkinkan mereka menguji dan menyempurnakan alur kerja kolaboratif serta meningkatkan efisiensi sistem secara keseluruhan.

**Bagaimana cara kerjanya dalam praktik**: Anda dapat membuat tim agen di mana setiap agen memiliki fungsi khusus, seperti pengambilan data, analisis, atau pengambilan keputusan. Agen-agen ini dapat berkomunikasi dan berbagi informasi untuk mencapai tujuan bersama, seperti menjawab pertanyaan pengguna atau menyelesaikan tugas.

**Contoh kode (Microsoft Agent Framework)**:

```python
# Membuat beberapa agen yang bekerja bersama menggunakan Microsoft Agent Framework

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Agen Pengambilan Data
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Agen Analisis Data
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Menjalankan agen secara berurutan pada sebuah tugas
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Apa yang Anda lihat pada kode sebelumnya adalah bagaimana Anda dapat membuat tugas yang melibatkan beberapa agen bekerja sama untuk menganalisis data. Setiap agen melakukan fungsi khusus, dan tugas dieksekusi dengan mengoordinasikan agen untuk mencapai hasil yang diinginkan. Dengan membuat agen khusus dengan peran khusus, Anda dapat meningkatkan efisiensi dan kinerja tugas.

### Belajar secara Real-Time

Kerangka kerja canggih menyediakan kemampuan untuk pemahaman dan adaptasi konteks secara real-time.

**Bagaimana tim dapat menggunakan ini**: Tim dapat menerapkan loop umpan balik di mana agen belajar dari interaksi dan menyesuaikan perilaku mereka secara dinamis, menghasilkan peningkatan dan penyempurnaan kemampuan secara terus-menerus.

**Bagaimana cara kerjanya dalam praktik**: Agen dapat menganalisis umpan balik pengguna, data lingkungan, dan hasil tugas untuk memperbarui basis pengetahuan mereka, menyesuaikan algoritme pengambilan keputusan, dan meningkatkan kinerja seiring waktu. Proses pembelajaran iteratif ini memungkinkan agen beradaptasi dengan kondisi yang berubah dan preferensi pengguna, meningkatkan efektivitas sistem secara keseluruhan.

## Apa perbedaan antara Microsoft Agent Framework dan Microsoft Foundry Agent Service?

Ada banyak cara untuk membandingkan pendekatan ini, tetapi mari kita lihat beberapa perbedaan utama dari segi desain, kemampuan, dan kasus penggunaan yang ditargetkan:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework menyediakan SDK yang ringkas untuk membangun agen AI menggunakan `FoundryChatClient`. Ini memungkinkan pengembang membuat agen yang memanfaatkan model Azure OpenAI dengan pemanggilan alat bawaan, manajemen percakapan, dan keamanan tingkat perusahaan melalui identitas Azure.

**Kasus Penggunaan**: Membangun agen AI siap produksi dengan penggunaan alat, alur kerja multi-langkah, dan skenario integrasi perusahaan.

Berikut adalah beberapa konsep inti penting dari Microsoft Agent Framework:

- **Agen**. Sebuah agen dibuat melalui `FoundryChatClient` dan dikonfigurasi dengan nama, instruksi, dan alat. Agen dapat:
  - **Memproses pesan pengguna** dan menghasilkan tanggapan menggunakan model Azure OpenAI.
  - **Memanggil alat** secara otomatis berdasarkan konteks percakapan.
  - **Mempertahankan status percakapan** di beberapa interaksi.

  Berikut adalah cuplikan kode yang menunjukkan cara membuat agen:

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

- **Alat**. Kerangka kerja mendukung definisi alat sebagai fungsi Python yang dapat dipanggil agen secara otomatis. Alat didaftarkan saat membuat agen:

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

- **Koordinasi Multi-Agen**. Anda dapat membuat banyak agen dengan spesialisasi berbeda dan mengoordinasikan pekerjaan mereka:

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

- **Integrasi Identitas Azure**. Kerangka kerja menggunakan `AzureCliCredential` (atau `DefaultAzureCredential`) untuk autentikasi tanpa kunci yang aman, menghilangkan kebutuhan mengelola kunci API secara langsung.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service adalah tambahan yang lebih baru, diperkenalkan pada Microsoft Ignite 2024. Ini memungkinkan pengembangan dan penyebaran agen AI dengan model yang lebih fleksibel, seperti memanggil langsung LLM open-source seperti Llama 3, Mistral, dan Cohere.

Microsoft Foundry Agent Service menyediakan mekanisme keamanan perusahaan yang lebih kuat dan metode penyimpanan data, menjadikannya cocok untuk aplikasi perusahaan.

Ini bekerja langsung dengan Microsoft Agent Framework untuk membangun dan menyebarkan agen.

Layanan ini saat ini dalam Pratinjau Publik dan mendukung Python dan C# untuk membangun agen.

Dengan menggunakan Microsoft Foundry Agent Service Python SDK, kita dapat membuat agen dengan alat yang ditentukan pengguna:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Definisikan fungsi alat
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

### Konsep inti

Microsoft Foundry Agent Service memiliki konsep inti berikut:

- **Agen**. Microsoft Foundry Agent Service terintegrasi dengan Microsoft Foundry. Dalam Microsoft Foundry, Agen AI berperan sebagai microservice "pintar" yang dapat digunakan untuk menjawab pertanyaan (RAG), melakukan tindakan, atau sepenuhnya mengotomatisasi alur kerja. Ini dicapai dengan menggabungkan kekuatan model AI generatif dengan alat yang memungkinkan akses dan interaksi dengan sumber data dunia nyata. Berikut adalah contoh agen:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    Dalam contoh ini, agen dibuat dengan model `gpt-5-mini`, nama `my-agent`, dan instruksi `You are helpful agent`. Agen dilengkapi dengan alat dan sumber daya untuk melakukan tugas interpretasi kode.

- **Thread dan pesan**. Thread adalah konsep penting lainnya. Ini merepresentasikan percakapan atau interaksi antara agen dan pengguna. Thread dapat digunakan untuk melacak kemajuan percakapan, menyimpan informasi konteks, dan mengelola status interaksi. Berikut adalah contoh thread:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Minta agen untuk melakukan pekerjaan pada thread
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Ambil dan catat semua pesan untuk melihat respons agen
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    Dalam kode sebelumnya, sebuah thread dibuat. Setelah itu, sebuah pesan dikirim ke thread tersebut. Dengan memanggil `create_and_process_run`, agen diminta untuk melakukan pekerjaan pada thread. Akhirnya, pesan diambil dan dicatat untuk melihat tanggapan agen. Pesan-pesan menunjukkan kemajuan percakapan antara pengguna dan agen. Penting juga untuk memahami bahwa pesan dapat berupa berbagai jenis seperti teks, gambar, atau file, yang merupakan hasil kerja agen misalnya gambar atau tanggapan teks. Sebagai pengembang, Anda kemudian dapat menggunakan informasi ini untuk memproses lebih lanjut tanggapan atau menyajikannya kepada pengguna.

- **Terintegrasi dengan Microsoft Agent Framework**. Microsoft Foundry Agent Service bekerja mulus dengan Microsoft Agent Framework, yang berarti Anda dapat membangun agen menggunakan `FoundryChatClient` dan menyebarkannya melalui Agent Service untuk skenario produksi.

**Kasus Penggunaan**: Microsoft Foundry Agent Service dirancang untuk aplikasi perusahaan yang memerlukan penyebaran agen AI yang aman, skalabel, dan fleksibel.

## Apa perbedaan antara pendekatan ini?
 
Memang terdengar ada tumpang tindih, tetapi ada beberapa perbedaan utama dari segi desain, kemampuan, dan kasus penggunaan yang ditargetkan:
 
- **Microsoft Agent Framework (MAF)**: Adalah SDK siap produksi untuk membangun agen AI. Menyediakan API yang ringkas untuk membuat agen dengan pemanggilan alat, manajemen percakapan, dan integrasi identitas Azure.
- **Microsoft Foundry Agent Service**: Adalah platform dan layanan penyebaran di Microsoft Foundry untuk agen. Menawarkan konektivitas bawaan ke layanan seperti Azure OpenAI, Azure AI Search, Bing Search, dan eksekusi kode.
 
Masih bingung memilih yang mana?

### Kasus Penggunaan
 
Mari kita lihat apakah kami bisa membantu Anda dengan membahas beberapa kasus penggunaan umum:
 
> T: Saya membangun aplikasi agen AI produksi dan ingin memulai dengan cepat
>

>J: Microsoft Agent Framework adalah pilihan tepat. Menyediakan API Python yang sederhana melalui `FoundryChatClient` yang memungkinkan Anda mendefinisikan agen dengan alat dan instruksi hanya dengan beberapa baris kode.

>T: Saya memerlukan penyebaran tingkat perusahaan dengan integrasi Azure seperti Search dan eksekusi kode
>
> J: Microsoft Foundry Agent Service adalah yang paling cocok. Ini adalah layanan platform yang menyediakan kemampuan bawaan untuk beberapa model, Azure AI Search, Bing Search, dan Azure Functions. Memudahkan membangun agen Anda di Foundry Portal dan menyebarkannya secara skala.
 
> T: Saya masih bingung, beri saya satu opsi saja
>
> J: Mulailah dengan Microsoft Agent Framework untuk membangun agen Anda, lalu gunakan Microsoft Foundry Agent Service saat Anda perlu menyebarkan dan menskalakan mereka di produksi. Pendekatan ini memungkinkan Anda iterasi cepat pada logika agen sambil memiliki jalur jelas ke penyebaran perusahaan.
 
Mari kita rangkum perbedaan kunci dalam sebuah tabel:

| Kerangka Kerja | Fokus | Konsep Inti | Kasus Penggunaan |
| --- | --- | --- | --- |
| Microsoft Agent Framework | SDK agen yang ringkas dengan pemanggilan alat | Agen, Alat, Identitas Azure | Membangun agen AI, penggunaan alat, alur kerja multi-langkah |
| Microsoft Foundry Agent Service | Model fleksibel, keamanan perusahaan, Generasi kode, Pemanggilan alat | Modularitas, Kolaborasi, Orkestrasi Proses | Penyebaran agen AI yang aman, skalabel, dan fleksibel |

## Bisakah saya mengintegrasikan alat ekosistem Azure saya yang sudah ada langsung, atau saya perlu solusi mandiri?


Jawabannya adalah ya, Anda dapat mengintegrasikan alat ekosistem Azure yang sudah ada langsung dengan Microsoft Foundry Agent Service terutama, karena layanan ini dibangun untuk bekerja mulus dengan layanan Azure lainnya. Anda bisa misalnya mengintegrasikan Bing, Azure AI Search, dan Azure Functions. Ada juga integrasi mendalam dengan Microsoft Foundry.

Microsoft Agent Framework juga terintegrasi dengan layanan Azure melalui `FoundryChatClient` dan identitas Azure, memungkinkan Anda memanggil layanan Azure langsung dari alat agen Anda.

## Contoh Kode

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Punya Pertanyaan Lebih Lanjut tentang AI Agent Frameworks?

Bergabunglah dengan [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) untuk bertemu dengan pembelajar lain, mengikuti jam kantor, dan mendapatkan jawaban untuk pertanyaan AI Agents Anda.

## Referensi

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Pelajaran Sebelumnya

[Pengenalan AI Agents dan Kasus Penggunaan Agen](../01-intro-to-ai-agents/README.md)

## Pelajaran Selanjutnya

[Memahami Pola Desain Agentik](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->