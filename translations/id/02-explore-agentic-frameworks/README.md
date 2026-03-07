[![Menjelajahi Kerangka Agen AI](../../../translated_images/id/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Klik gambar di atas untuk menonton video pelajaran ini)_

# Jelajahi Kerangka Agen AI

Kerangka kerja agen AI adalah platform perangkat lunak yang dirancang untuk menyederhanakan pembuatan, penyebaran, dan pengelolaan agen AI. Kerangka kerja ini menyediakan komponen pra-bangun, abstraksi, dan alat yang memudahkan pengembangan sistem AI yang kompleks.

Kerangka kerja ini membantu pengembang memusatkan perhatian pada aspek unik dari aplikasi mereka dengan menyediakan pendekatan standar untuk tantangan umum dalam pengembangan agen AI. Mereka meningkatkan skalabilitas, aksesibilitas, dan efisiensi dalam membangun sistem AI.

## Pengenalan 

Pelajaran ini akan membahas:

- Apa itu Kerangka Agen AI dan apa yang dapat dicapai pengembang dengannya?
- Bagaimana tim dapat menggunakan ini untuk dengan cepat membuat prototipe, iterasi, dan meningkatkan kemampuan agen mereka?
- Apa perbedaan antara kerangka kerja dan alat yang dibuat oleh Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Layanan Agen AI Azure</a> dan the <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Kerangka Agen Microsoft</a>)?
- Bisakah saya mengintegrasikan alat ekosistem Azure saya yang sudah ada secara langsung, atau apakah saya memerlukan solusi mandiri?
- Apa itu layanan Azure AI Agents dan bagaimana ini membantu saya?

## Tujuan pembelajaran

Tujuan pelajaran ini adalah untuk membantu Anda memahami:

- Peran Kerangka Agen AI dalam pengembangan AI.
- Cara memanfaatkan Kerangka Agen AI untuk membangun agen cerdas.
- Kemampuan utama yang diaktifkan oleh Kerangka Agen AI.
- Perbedaan antara Kerangka Agen Microsoft dan Layanan Agen AI Azure.

## Apa itu Kerangka Agen AI dan apa yang memungkinkan pengembang lakukan?

Kerangka AI tradisional dapat membantu Anda mengintegrasikan AI ke dalam aplikasi Anda dan membuat aplikasi tersebut lebih baik dalam cara-cara berikut:

- **Personalisasi**: AI dapat menganalisis perilaku dan preferensi pengguna untuk memberikan rekomendasi, konten, dan pengalaman yang dipersonalisasi.
Contoh: Layanan streaming seperti Netflix menggunakan AI untuk menyarankan film dan acara berdasarkan riwayat tontonan, meningkatkan keterlibatan dan kepuasan pengguna.
- **Otomatisasi dan Efisiensi**: AI dapat mengotomatisasi tugas berulang, menyederhanakan alur kerja, dan meningkatkan efisiensi operasional.
Contoh: Aplikasi layanan pelanggan menggunakan chatbot bertenaga AI untuk menangani pertanyaan umum, mengurangi waktu respons dan membebaskan agen manusia untuk masalah yang lebih kompleks.
- **Peningkatan Pengalaman Pengguna**: AI dapat meningkatkan pengalaman pengguna secara keseluruhan dengan menyediakan fitur cerdas seperti pengenalan suara, pemrosesan bahasa alami, dan teks prediktif.
Contoh: Asisten virtual seperti Siri dan Google Assistant menggunakan AI untuk memahami dan merespons perintah suara, memudahkan pengguna berinteraksi dengan perangkat mereka.

### Kedengarannya hebat, jadi mengapa kita membutuhkan Kerangka Agen AI?

Kerangka Agen AI mewakili sesuatu yang lebih dari sekadar kerangka AI. Mereka dirancang untuk memungkinkan pembuatan agen cerdas yang dapat berinteraksi dengan pengguna, agen lain, dan lingkungan untuk mencapai tujuan tertentu. Agen-agen ini dapat menunjukkan perilaku otonom, membuat keputusan, dan beradaptasi dengan kondisi yang berubah. Mari kita lihat beberapa kemampuan kunci yang diaktifkan oleh Kerangka Agen AI:

- **Kolaborasi dan Koordinasi Agen**: Memungkinkan pembuatan beberapa agen AI yang dapat bekerja sama, berkomunikasi, dan berkoordinasi untuk menyelesaikan tugas yang kompleks.
- **Otomatisasi dan Manajemen Tugas**: Menyediakan mekanisme untuk mengotomatisasi alur kerja multi-langkah, pendelegasian tugas, dan manajemen tugas dinamis antar agen.
- **Pemahaman Kontekstual dan Adaptasi**: Membekali agen dengan kemampuan untuk memahami konteks, beradaptasi dengan lingkungan yang berubah, dan membuat keputusan berdasarkan informasi waktu nyata.

Jadi, singkatnya, agen memungkinkan Anda melakukan lebih banyak, membawa otomatisasi ke tingkat berikutnya, menciptakan sistem yang lebih cerdas yang dapat beradaptasi dan belajar dari lingkungan mereka.

## Bagaimana cara membuat prototipe, iterasi, dan meningkatkan kemampuan agen dengan cepat?

Ini adalah lanskap yang bergerak cepat, tetapi ada beberapa hal yang umum di sebagian besar Kerangka Agen AI yang dapat membantu Anda membuat prototipe dan iterasi dengan cepat yaitu komponen modular, alat kolaboratif, dan pembelajaran waktu nyata. Mari kita bahas ini:

- **Gunakan Komponen Modular**: SDK AI menawarkan komponen pra-bangun seperti konektor AI dan Memori, pemanggilan fungsi menggunakan bahasa alami atau plugin kode, template prompt, dan lainnya.
- **Manfaatkan Alat Kolaboratif**: Rancang agen dengan peran dan tugas spesifik, memungkinkan mereka menguji dan menyempurnakan alur kerja kolaboratif.
- **Belajar secara Waktu Nyata**: Terapkan loop umpan balik di mana agen belajar dari interaksi dan menyesuaikan perilaku mereka secara dinamis.

### Gunakan Komponen Modular

SDK seperti Kerangka Agen Microsoft menawarkan komponen pra-bangun seperti konektor AI, definisi alat, dan manajemen agen.

**Bagaimana tim dapat menggunakan ini**: Tim dapat dengan cepat merakit komponen ini untuk membuat prototipe fungsional tanpa memulai dari nol, memungkinkan eksperimen dan iterasi yang cepat.

**Bagaimana cara kerjanya dalam praktik**: Anda dapat menggunakan parser pra-bangun untuk mengekstrak informasi dari input pengguna, modul memori untuk menyimpan dan mengambil data, dan generator prompt untuk berinteraksi dengan pengguna, semuanya tanpa harus membangun komponen ini dari awal.

**Contoh kode**. Mari kita lihat contoh bagaimana Anda dapat menggunakan Kerangka Agen Microsoft dengan `AzureAIProjectAgentProvider` agar model merespons input pengguna dengan pemanggilan alat:

``` python
# Contoh Python Microsoft Agent Framework

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# Definisikan fungsi alat contoh untuk memesan perjalanan
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # Contoh keluaran: Penerbangan Anda ke New York pada 1 Januari 2025 telah berhasil dipesan. Selamat jalan! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Apa yang dapat Anda lihat dari contoh ini adalah bagaimana Anda dapat memanfaatkan parser pra-bangun untuk mengekstrak informasi kunci dari input pengguna, seperti asal, tujuan, dan tanggal permintaan pemesanan penerbangan. Pendekatan modular ini memungkinkan Anda fokus pada logika tingkat tinggi.

### Manfaatkan Alat Kolaboratif

Kerangka seperti Kerangka Agen Microsoft memfasilitasi pembuatan beberapa agen yang dapat bekerja bersama.

**Bagaimana tim dapat menggunakan ini**: Tim dapat merancang agen dengan peran dan tugas khusus, memungkinkan mereka menguji dan menyempurnakan alur kerja kolaboratif dan meningkatkan efisiensi sistem secara keseluruhan.

**Bagaimana cara kerjanya dalam praktik**: Anda dapat membuat tim agen di mana setiap agen memiliki fungsi khusus, seperti pengambilan data, analisis, atau pengambilan keputusan. Agen-agen ini dapat berkomunikasi dan berbagi informasi untuk mencapai tujuan bersama, seperti menjawab kueri pengguna atau menyelesaikan tugas.

**Contoh kode (Kerangka Agen Microsoft)**:

```python
# Membuat beberapa agen yang bekerja sama menggunakan Microsoft Agent Framework

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Agen Pengambilan Data
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Agen Analisis Data
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Menjalankan agen secara berurutan pada sebuah tugas
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Apa yang Anda lihat dalam kode sebelumnya adalah bagaimana Anda dapat membuat tugas yang melibatkan beberapa agen yang bekerja sama untuk menganalisis data. Setiap agen melakukan fungsi tertentu, dan tugas dieksekusi dengan mengoordinasikan agen untuk mencapai hasil yang diinginkan. Dengan membuat agen khusus dengan peran yang terfokus, Anda dapat meningkatkan efisiensi dan kinerja tugas.

### Belajar secara Waktu Nyata

Kerangka lanjutan menyediakan kemampuan untuk pemahaman konteks waktu nyata dan adaptasi.

**Bagaimana tim dapat menggunakan ini**: Tim dapat menerapkan loop umpan balik di mana agen belajar dari interaksi dan menyesuaikan perilaku mereka secara dinamis, menghasilkan peningkatan dan penyempurnaan kemampuan secara berkelanjutan.

**Bagaimana cara kerjanya dalam praktik**: Agen dapat menganalisis umpan balik pengguna, data lingkungan, dan hasil tugas untuk memperbarui basis pengetahuan mereka, menyesuaikan algoritma pengambilan keputusan, dan meningkatkan kinerja dari waktu ke waktu. Proses pembelajaran iteratif ini memungkinkan agen beradaptasi dengan kondisi yang berubah dan preferensi pengguna, meningkatkan efektivitas sistem secara keseluruhan.

## Apa perbedaan antara Kerangka Agen Microsoft dan Layanan Agen AI Azure?

Ada banyak cara untuk membandingkan pendekatan ini, tetapi mari kita lihat beberapa perbedaan kunci dalam hal desain, kemampuan, dan kasus penggunaan yang ditargetkan:

## Kerangka Agen Microsoft (MAF)

Kerangka Agen Microsoft menyediakan SDK yang disederhanakan untuk membangun agen AI menggunakan `AzureAIProjectAgentProvider`. Ini memungkinkan pengembang membuat agen yang memanfaatkan model Azure OpenAI dengan pemanggilan alat bawaan, manajemen percakapan, dan keamanan tingkat perusahaan melalui identitas Azure.

**Kasus Penggunaan**: Membangun agen AI siap-produksi dengan penggunaan alat, alur kerja multi-langkah, dan skenario integrasi perusahaan.

Berikut adalah beberapa konsep inti penting dari Kerangka Agen Microsoft:

- **Agen**. Agen dibuat melalui `AzureAIProjectAgentProvider` dan dikonfigurasi dengan nama, instruksi, dan alat. Agen dapat:
  - **Memproses pesan pengguna** dan menghasilkan respons menggunakan model Azure OpenAI.
  - **Memanggil alat** secara otomatis berdasarkan konteks percakapan.
  - **Mempertahankan status percakapan** di berbagai interaksi.

  Berikut cuplikan kode yang menunjukkan cara membuat agen:

    ```python
    import os
    from agent_framework.azure import AzureAIProjectAgentProvider
    from azure.identity import AzureCliCredential

    provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())
    agent = await provider.create_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **Alat**. Kerangka mendukung pendefinisian alat sebagai fungsi Python yang dapat dipanggil otomatis oleh agen. Alat didaftarkan saat membuat agen:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = await provider.create_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **Koordinasi Multi-Agen**. Anda dapat membuat beberapa agen dengan spesialisasi berbeda dan mengoordinasikan kerja mereka:

    ```python
    planner = await provider.create_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = await provider.create_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Integrasi Identitas Azure**. Kerangka menggunakan `AzureCliCredential` (atau `DefaultAzureCredential`) untuk otentikasi aman tanpa kunci, menghilangkan kebutuhan untuk mengelola kunci API secara langsung.

## Layanan Agen AI Azure

Layanan Agen AI Azure adalah tambahan yang lebih baru, diperkenalkan di Microsoft Ignite 2024. Layanan ini memungkinkan pengembangan dan penyebaran agen AI dengan model yang lebih fleksibel, seperti memanggil langsung LLM open-source seperti Llama 3, Mistral, dan Cohere.

Layanan Agen AI Azure menyediakan mekanisme keamanan perusahaan yang lebih kuat dan metode penyimpanan data, menjadikannya cocok untuk aplikasi perusahaan.

Ini bekerja langsung bersama Kerangka Agen Microsoft untuk membangun dan menyebarkan agen.

Layanan ini saat ini dalam Pratinjau Publik dan mendukung Python dan C# untuk membangun agen.

Dengan menggunakan SDK Python Layanan Agen AI Azure, kita dapat membuat agen dengan alat yang didefinisikan pengguna:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Mendefinisikan fungsi alat
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
        model="gpt-4o-mini",
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

Layanan Agen AI Azure memiliki konsep inti berikut:

- **Agen**. Layanan Agen AI Azure terintegrasi dengan Microsoft Foundry. Dalam AI Foundry, Agen AI bertindak sebagai mikroservice "pintar" yang dapat digunakan untuk menjawab pertanyaan (RAG), melakukan tindakan, atau sepenuhnya mengotomatisasi alur kerja. Ini dicapai dengan menggabungkan kekuatan model generatif dengan alat yang memungkinkan akses dan interaksi dengan sumber data dunia nyata. Berikut contoh agen:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    Dalam contoh ini, agen dibuat dengan model `gpt-4o-mini`, nama `my-agent`, dan instruksi `You are helpful agent`. Agen dilengkapi dengan alat dan sumber daya untuk melakukan tugas interpretasi kode.

- **Thread dan pesan**. Thread adalah konsep penting lainnya. Ini mewakili percakapan atau interaksi antara agen dan pengguna. Thread dapat digunakan untuk melacak kemajuan percakapan, menyimpan informasi konteks, dan mengelola status interaksi. Berikut contoh thread:

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

    Dalam kode sebelumnya, sebuah thread dibuat. Setelah itu, sebuah pesan dikirim ke thread. Dengan memanggil `create_and_process_run`, agen diminta untuk melakukan pekerjaan pada thread. Akhirnya, pesan-pesan diambil dan dicatat untuk melihat respons agen. Pesan-pesan tersebut menunjukkan kemajuan percakapan antara pengguna dan agen. Penting juga untuk memahami bahwa pesan dapat berupa berbagai tipe seperti teks, gambar, atau file, misalnya pekerjaan agen menghasilkan sebuah gambar atau respons teks. Sebagai pengembang, Anda kemudian dapat menggunakan informasi ini untuk memproses lebih lanjut respons tersebut atau menyajikannya kepada pengguna.

- **Terintegrasi dengan Kerangka Agen Microsoft**. Layanan Agen AI Azure bekerja mulus dengan Kerangka Agen Microsoft, yang berarti Anda dapat membangun agen menggunakan `AzureAIProjectAgentProvider` dan menyebarkannya melalui Agent Service untuk skenario produksi.

**Kasus Penggunaan**: Layanan Agen AI Azure dirancang untuk aplikasi perusahaan yang membutuhkan penyebaran agen AI yang aman, skalabel, dan fleksibel.

## Apa perbedaan antara pendekatan ini?
 
Memang terdengar ada tumpang tindih, tetapi ada beberapa perbedaan kunci dalam hal desain, kemampuan, dan kasus penggunaan yang ditargetkan:
 
- **Kerangka Agen Microsoft (MAF)**: Adalah SDK siap-produksi untuk membangun agen AI. Ini menyediakan API yang disederhanakan untuk membuat agen dengan pemanggilan alat, manajemen percakapan, dan integrasi identitas Azure.
- **Layanan Agen AI Azure**: Adalah platform dan layanan penyebaran di Azure Foundry untuk agen. Ini menawarkan konektivitas bawaan ke layanan seperti Azure OpenAI, Azure AI Search, Bing Search, dan eksekusi kode.
 
Masih ragu mana yang harus dipilih?

### Kasus Penggunaan
 
Mari kita lihat apakah kita bisa membantu Anda dengan melalui beberapa kasus penggunaan umum:
 
> Q: Saya membangun aplikasi agen AI produksi dan ingin mulai dengan cepat
>

>A: Kerangka Agen Microsoft adalah pilihan yang bagus. Ini menyediakan API Python yang sederhana melalui `AzureAIProjectAgentProvider` yang memungkinkan Anda mendefinisikan agen dengan alat dan instruksi hanya dalam beberapa baris kode.

>Q: Saya membutuhkan penyebaran kelas-perusahaan dengan integrasi Azure seperti Search dan eksekusi kode
>
> A: Layanan Agen AI Azure adalah yang paling cocok. Ini adalah layanan platform yang menyediakan kapabilitas bawaan untuk berbagai model, Azure AI Search, Bing Search dan Azure Functions. Ini memudahkan membangun agen Anda di Portal Foundry dan menyebarkannya dalam skala besar.
 
> Q: Saya masih bingung, beri saya satu opsi saja
>
> A: Mulailah dengan Kerangka Agen Microsoft untuk membangun agen Anda, lalu gunakan Layanan Agen AI Azure ketika Anda perlu menyebarkan dan menskalakan mereka di produksi. Pendekatan ini memungkinkan Anda beriterasi dengan cepat pada logika agen sambil memiliki jalur yang jelas menuju penyebaran perusahaan.
 
Mari kita rangkum perbedaan kunci dalam sebuah tabel:

| Framework | Fokus | Konsep Inti | Kasus Penggunaan |
| --- | --- | --- | --- |
| Microsoft Agent Framework | SDK agen yang disederhanakan dengan pemanggilan alat | Agen, Alat, Identitas Azure | Membangun agen AI, penggunaan alat, alur kerja multi-langkah |
| Azure AI Agent Service | Model yang fleksibel, keamanan perusahaan, Pembuatan kode, Pemanggilan alat | Modularitas, Kolaborasi, Orkestrasi Proses | Penyebaran agen AI yang aman, skalabel, dan fleksibel |

## Bisakah saya mengintegrasikan alat ekosistem Azure saya yang sudah ada secara langsung, atau apakah saya memerlukan solusi mandiri?
Jawabannya adalah ya, Anda dapat mengintegrasikan alat ekosistem Azure yang sudah ada langsung dengan Azure AI Agent Service, karena layanan ini dibangun untuk bekerja mulus dengan layanan Azure lainnya. Anda misalnya dapat mengintegrasikan Bing, Azure AI Search, dan Azure Functions. Ada juga integrasi mendalam dengan Microsoft Foundry.

The Microsoft Agent Framework also integrates with Azure services through `AzureAIProjectAgentProvider` and Azure identity, letting you call Azure services directly from your agent tools.

## Contoh Kode

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Punya Pertanyaan Lebih Lanjut tentang AI Agent Frameworks?

Bergabunglah dengan [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) untuk bertemu pembelajar lain, menghadiri jam konsultasi dan mendapatkan jawaban atas pertanyaan AI Agents Anda.

## Referensi

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent service</a>

## Pelajaran Sebelumnya

[Pengantar Agen AI dan Kasus Penggunaan Agen](../01-intro-to-ai-agents/README.md)

## Pelajaran Berikutnya

[Memahami Pola Desain Agen](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan terjemahan yang akurat, harap diingat bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidaktepatan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan terjemahan profesional oleh penerjemah manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul akibat penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->