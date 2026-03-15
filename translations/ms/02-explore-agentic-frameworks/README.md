[![Meneroka Rangka Kerja Ejen AI](../../../translated_images/ms/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Klik imej di atas untuk menonton video bagi pelajaran ini)_

# Terokai Rangka Kerja Ejen AI

Rangka kerja ejen AI adalah platform perisian yang direka untuk mempermudah penciptaan, penyebaran, dan pengurusan ejen AI. Rangka kerja ini menyediakan komponen siap pakai, abstraksi, dan alat yang memudahkan pembangunan sistem AI yang kompleks.

Rangka kerja ini membantu pembangun memberi tumpuan kepada aspek unik aplikasi mereka dengan menyediakan pendekatan standard terhadap cabaran biasa dalam pembangunan ejen AI. Ia meningkatkan skala, kebolehcapaian, dan kecekapan dalam membina sistem AI.

## Pengenalan 

Pelajaran ini akan merangkumi:

- Apa itu Rangka Kerja Ejen AI dan apa yang membolehkan pembangun capai?
- Bagaimana pasukan boleh menggunakan ini untuk prototaip dengan cepat, iterasi, dan memperbaiki keupayaan ejen mereka?
- Apakah perbezaan antara rangka kerja dan alat yang dibina oleh Microsoft (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Perkhidmatan Ejen AI Azure</a> dan <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Rangka Kerja Ejen Microsoft</a>)?
- Bolehkah saya mengintegrasikan alat ekosistem Azure saya sedia ada secara langsung, atau adakah saya memerlukan penyelesaian berdiri sendiri?
- Apakah Perkhidmatan Ejen AI Azure dan bagaimana ia membantu saya?

## Matlamat Pembelajaran

Matlamat pelajaran ini adalah untuk membantu anda memahami:

- Peranan Rangka Kerja Ejen AI dalam pembangunan AI.
- Cara memanfaatkan Rangka Kerja Ejen AI untuk membina ejen pintar.
- Keupayaan utama yang dibolehkan oleh Rangka Kerja Ejen AI.
- Perbezaan antara Rangka Kerja Ejen Microsoft dan Perkhidmatan Ejen AI Azure.

## Apa itu Rangka Kerja Ejen AI dan apa yang mereka benarkan pembangun lakukan?

Rangka Kerja AI tradisional boleh membantu anda mengintegrasikan AI ke dalam aplikasi anda dan menjadikan aplikasi ini lebih baik dengan cara berikut:

- **Personalisasi**: AI boleh menganalisis tingkah laku dan keutamaan pengguna untuk menyediakan cadangan, kandungan, dan pengalaman yang diperibadikan.
Contoh: Perkhidmatan penstriman seperti Netflix menggunakan AI untuk mencadangkan filem dan rancangan berdasarkan sejarah tontonan, meningkatkan penglibatan dan kepuasan pengguna.
- **Automasi dan Kecekapan**: AI boleh mengautomasi tugas berulang, melancarkan aliran kerja, dan meningkatkan kecekapan operasi.
Contoh: Aplikasi perkhidmatan pelanggan menggunakan chatbot bertenaga AI untuk mengendalikan pertanyaan biasa, mengurangkan masa tindak balas dan membebaskan ejen manusia untuk isu yang lebih kompleks.
- **Pengalaman Pengguna yang Ditingkatkan**: AI boleh memperbaiki pengalaman pengguna keseluruhan dengan menyediakan ciri pintar seperti pengecaman suara, pemprosesan bahasa semula jadi, dan teks ramalan.
Contoh: Pembantu maya seperti Siri dan Google Assistant menggunakan AI untuk memahami dan memberi respons kepada arahan suara, memudahkan pengguna berinteraksi dengan peranti mereka.

### Semua itu kedengaran hebat, jadi mengapa kita perlukan Rangka Kerja Ejen AI?

Rangka kerja Ejen AI mewakili sesuatu yang lebih daripada hanya rangka kerja AI. Ia direka untuk membolehkan penciptaan ejen pintar yang boleh berinteraksi dengan pengguna, ejen lain, dan persekitaran untuk mencapai matlamat khusus. Ejen ini boleh menunjukkan tingkah laku autonomi, membuat keputusan, dan menyesuaikan diri dengan keadaan yang berubah. Mari kita lihat beberapa keupayaan utama yang dibolehkan oleh Rangka Kerja Ejen AI:

- **Kerjasama dan Penyelarasan Ejen**: Membolehkan penciptaan pelbagai ejen AI yang boleh bekerja bersama, berkomunikasi, dan bekerjasama menyelesaikan tugasan kompleks.
- **Automasi dan Pengurusan Tugasan**: Menyediakan mekanisme untuk mengautomasi aliran kerja berbilang langkah, delegasi tugasan, dan pengurusan tugasan dinamik di kalangan ejen.
- **Pemahaman Kontekstual dan Penyesuaian**: Melengkapkan ejen dengan keupayaan untuk memahami konteks, menyesuaikan diri dengan persekitaran yang berubah, dan membuat keputusan berdasarkan maklumat masa nyata.

Jadi kesimpulannya, ejen membolehkan anda melakukan lebih banyak, membawa automasi ke tahap seterusnya, dan mencipta sistem yang lebih pintar yang boleh menyesuaikan diri dan belajar dari persekitaran mereka.

## Bagaimana untuk prototaip dengan cepat, iterasi, dan memperbaiki keupayaan ejen?

Ini adalah landskap yang bergerak pantas, tetapi terdapat beberapa perkara yang biasa dalam kebanyakan Rangka Kerja Ejen AI yang boleh membantu anda prototaip dan iterasi dengan pantas iaitu komponen modul, alat kolaboratif, dan pembelajaran masa nyata. Mari kita selami ini:

- **Gunakan Komponen Modular**: SDK AI menawarkan komponen siap pakai seperti penyambung AI dan Memori, pemanggilan fungsi menggunakan bahasa semula jadi atau plugin kod, templat prompt, dan lain-lain.
- **Manfaatkan Alat Kolaboratif**: Reka ejen dengan peranan dan tugasan tertentu, membolehkan mereka menguji dan memperbaiki aliran kerja kolaboratif.
- **Belajar Secara Masa Nyata**: Laksanakan gelung maklum balas di mana ejen belajar daripada interaksi dan melaraskan tingkah laku mereka secara dinamik.

### Gunakan Komponen Modular

SDK seperti Rangka Kerja Ejen Microsoft menawarkan komponen siap pakai seperti penyambung AI, definisi alat, dan pengurusan ejen.

**Bagaimana pasukan boleh menggunakan ini**: Pasukan boleh menggabungkan komponen ini dengan cepat untuk mencipta prototaip berfungsi tanpa perlu bermula dari awal, membolehkan eksperimen dan iterasi yang pantas.

**Bagaimana ia berfungsi dalam praktik**: Anda boleh menggunakan parser siap pakai untuk mengekstrak maklumat daripada input pengguna, modul memori untuk menyimpan dan mendapatkan data, dan penjana prompt untuk berinteraksi dengan pengguna, semuanya tanpa perlu membina komponen ini dari awal.

**Contoh kod**. Mari lihat contoh bagaimana anda boleh menggunakan Rangka Kerja Ejen Microsoft dengan `AzureAIProjectAgentProvider` untuk membuat model memberi respons kepada input pengguna dengan pemanggilan alat:

``` python
# Contoh Microsoft Agent Framework Python

import asyncio
import os
from typing import Annotated

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential


# Definisikan fungsi alat contoh untuk menempah perjalanan
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
    # Contoh keluaran: Penerbangan anda ke New York pada 1 Januari 2025 telah berjaya ditempah. Selamat melancong! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Apa yang anda lihat dari contoh ini adalah bagaimana anda boleh memanfaatkan parser siap pakai untuk mengekstrak maklumat utama daripada input pengguna, seperti asal, destinasi, dan tarikh permintaan tempahan penerbangan. Pendekatan modular ini membolehkan anda memberi tumpuan kepada logik aras tinggi.

### Manfaatkan Alat Kolaboratif

Rangka kerja seperti Rangka Kerja Ejen Microsoft memudahkan penciptaan pelbagai ejen yang boleh bekerjasama.

**Bagaimana pasukan boleh menggunakan ini**: Pasukan boleh mereka ejen dengan peranan dan tugasan tertentu, membolehkan mereka menguji dan memperbaiki aliran kerja kolaboratif serta meningkatkan kecekapan sistem keseluruhan.

**Bagaimana ia berfungsi dalam praktik**: Anda boleh mencipta satu pasukan ejen di mana setiap ejen mempunyai fungsi khusus, seperti pengambilan data, analisis, atau membuat keputusan. Ejen ini boleh berkomunikasi dan berkongsi maklumat untuk mencapai matlamat bersama, seperti menjawab pertanyaan pengguna atau menyelesaikan tugasan.

**Contoh kod (Rangka Kerja Ejen Microsoft)**:

```python
# Mewujudkan pelbagai ejen yang bekerjasama menggunakan Rangka Kerja Ejen Microsoft

import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Ejen Pengambilan Data
agent_retrieve = await provider.create_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Ejen Analisis Data
agent_analyze = await provider.create_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Jalankan ejen secara berurutan pada tugas
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Apa yang anda lihat dalam kod sebelumnya adalah bagaimana anda boleh mencipta tugasan yang melibatkan pelbagai ejen yang bekerjasama untuk menganalisis data. Setiap ejen melaksanakan fungsi khusus, dan tugasan dijalankan dengan menyelaraskan ejen untuk mencapai hasil yang dikehendaki. Dengan mencipta ejen khas dengan peranan khusus, anda boleh meningkatkan kecekapan dan prestasi tugasan.

### Belajar Secara Masa Nyata

Rangka kerja canggih menyediakan keupayaan untuk memahami dan menyesuaikan konteks masa nyata.

**Bagaimana pasukan boleh menggunakan ini**: Pasukan boleh melaksanakan gelung maklum balas di mana ejen belajar daripada interaksi dan melaraskan tingkah laku mereka secara dinamik, membawa kepada peningkatan berterusan dan penyempurnaan keupayaan.

**Bagaimana ia berfungsi dalam praktik**: Ejen boleh menganalisis maklum balas pengguna, data persekitaran, dan hasil tugasan untuk mengemas kini asas pengetahuan mereka, melaraskan algoritma membuat keputusan, dan meningkatkan prestasi dari masa ke masa. Proses pembelajaran iteratif ini membolehkan ejen menyesuaikan diri dengan keadaan dan keutamaan pengguna yang berubah, meningkatkan keberkesanan sistem secara keseluruhan.

## Apakah perbezaan antara Rangka Kerja Ejen Microsoft dan Perkhidmatan Ejen AI Azure?

Terdapat banyak cara untuk membandingkan pendekatan ini, tetapi mari kita lihat beberapa perbezaan utama dari segi reka bentuk, keupayaan, dan kes penggunaan sasaran:

## Rangka Kerja Ejen Microsoft (MAF)

Rangka Kerja Ejen Microsoft menyediakan SDK yang dipermudahkan untuk membina ejen AI menggunakan `AzureAIProjectAgentProvider`. Ia membolehkan pembangun mencipta ejen yang memanfaatkan model Azure OpenAI dengan pemanggilan alat terbina dalam, pengurusan perbualan, dan keselamatan setaraf perusahaan melalui identiti Azure.

**Kes Penggunaan**: Membina ejen AI sedia untuk pengeluaran dengan penggunaan alat, aliran kerja berbilang langkah, dan senario integrasi perusahaan.

Berikut adalah beberapa konsep teras penting dalam Rangka Kerja Ejen Microsoft:

- **Ejen**. Ejen dicipta melalui `AzureAIProjectAgentProvider` dan dikonfigurasikan dengan nama, arahan, dan alat. Ejen boleh:
  - **Memproses mesej pengguna** dan menjana respons menggunakan model Azure OpenAI.
  - **Memanggil alat** secara automatik berdasarkan konteks perbualan.
  - **Mengekalkan keadaan perbualan** merentasi berbilang interaksi.

  Berikut adalah petikan kod yang menunjukkan cara mencipta ejen:

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

- **Alat**. Rangka kerja menyokong definisi alat sebagai fungsi Python yang boleh dipanggil ejen secara automatik. Alat didaftarkan semasa mencipta ejen:

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

- **Penyelarasan Pelbagai Ejen**. Anda boleh mencipta pelbagai ejen dengan kepakaran berbeza dan menyelaras kerja mereka:

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

- **Integrasi Identiti Azure**. Rangka kerja menggunakan `AzureCliCredential` (atau `DefaultAzureCredential`) untuk pengesahan selamat tanpa kunci, menghapuskan keperluan mengurus kunci API secara langsung.

## Perkhidmatan Ejen AI Azure

Perkhidmatan Ejen AI Azure adalah tambahan yang lebih baharu, diperkenalkan di Microsoft Ignite 2024. Ia membolehkan pembangunan dan penyebaran ejen AI dengan model yang lebih fleksibel, seperti memanggil terus LLM sumber terbuka seperti Llama 3, Mistral, dan Cohere.

Perkhidmatan Ejen AI Azure menyediakan mekanisme keselamatan perusahaan yang lebih kukuh dan kaedah penyimpanan data, menjadikannya sesuai untuk aplikasi perusahaan.

Ia berfungsi terus dengan Rangka Kerja Ejen Microsoft untuk membina dan menyebarkan ejen.

Perkhidmatan ini kini berada dalam Pratonton Awam dan menyokong Python serta C# untuk membina ejen.

Menggunakan SDK Python Perkhidmatan Ejen AI Azure, kita boleh mencipta ejen dengan alat yang ditakrifkan pengguna:

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

### Konsep teras

Perkhidmatan Ejen AI Azure mempunyai konsep teras berikut:

- **Ejen**. Perkhidmatan Ejen AI Azure berintegrasi dengan Microsoft Foundry. Dalam AI Foundry, Ejen AI bertindak sebagai "mikroservis pintar" yang boleh digunakan untuk menjawab soalan (RAG), melaksanakan tindakan, atau mengautomasikan aliran kerja sepenuhnya. Ia mencapai ini dengan menggabungkan kuasa model AI generatif dengan alat yang membolehkannya mengakses dan berinteraksi dengan sumber data dunia nyata. Berikut adalah contoh ejen:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-4o-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    Dalam contoh ini, ejen dicipta dengan model `gpt-4o-mini`, nama `my-agent`, dan arahan `You are helpful agent`. Ejen dilengkapi dengan alat dan sumber untuk melaksanakan tugas interpretasi kod.

- **Benang dan mesej**. Benang adalah konsep penting lain. Ia mewakili perbualan atau interaksi antara ejen dan pengguna. Benang boleh digunakan untuk menjejak kemajuan perbualan, menyimpan maklumat konteks, dan mengurus keadaan interaksi. Berikut adalah contoh benang:

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

    Dalam kod sebelumnya, benang dicipta. Selepas itu, mesej dihantar ke benang. Dengan memanggil `create_and_process_run`, ejen diminta melaksanakan kerja pada benang tersebut. Akhir sekali, mesej diambil dan dicatat untuk melihat respons ejen. Mesej menunjukkan kemajuan perbualan antara pengguna dan ejen. Penting juga untuk difahami bahawa mesej boleh mempunyai jenis berbeza seperti teks, imej, atau fail, iaitu kerja ejen telah menghasilkan contohnya imej atau respons teks. Sebagai pembangun, anda kemudian boleh menggunakan maklumat ini untuk memproses respons lebih lanjut atau menyampaikannya kepada pengguna.

- **Berintegrasi dengan Rangka Kerja Ejen Microsoft**. Perkhidmatan Ejen AI Azure berfungsi lancar dengan Rangka Kerja Ejen Microsoft, bermakna anda boleh membina ejen menggunakan `AzureAIProjectAgentProvider` dan menyebarkannya melalui Perkhidmatan Ejen untuk senario pengeluaran.

**Kes Penggunaan**: Perkhidmatan Ejen AI Azure direka untuk aplikasi perusahaan yang memerlukan penyebaran ejen AI yang selamat, berskala, dan fleksibel.

## Apakah perbezaan antara pendekatan ini?

Nampak macam ada persilangan, tetapi terdapat beberapa perbezaan utama dari segi reka bentuk, keupayaan, dan kes penggunaan sasaran:

- **Rangka Kerja Ejen Microsoft (MAF)**: Adalah SDK sedia untuk pengeluaran bagi membina ejen AI. Ia menyediakan API yang dipermudahkan untuk mencipta ejen dengan pemanggilan alat, pengurusan perbualan, dan integrasi identiti Azure.
- **Perkhidmatan Ejen AI Azure**: Adalah platform dan perkhidmatan penyebaran dalam Azure Foundry untuk ejen. Ia menawarkan sambungan terbina kepada perkhidmatan seperti Azure OpenAI, Azure AI Search, Bing Search dan pelaksanaan kod.

Masih tak pasti mana satu hendak pilih?

### Kes Penggunaan

Mari kita lihat jika kami boleh membantu anda dengan melalui beberapa kes penggunaan biasa:

> S: Saya membina aplikasi ejen AI pengeluaran dan mahu bermula dengan cepat  
>

>J: Rangka Kerja Ejen Microsoft adalah pilihan terbaik. Ia menyediakan API yang ringkas dan Pythonic melalui `AzureAIProjectAgentProvider` yang membolehkan anda mentakrifkan ejen dengan alat dan arahan dalam beberapa baris kod sahaja.

>S: Saya perlukan penyebaran setaraf perusahaan dengan integrasi Azure seperti Search dan pelaksanaan kod  
>
> J: Perkhidmatan Ejen AI Azure adalah pilihan terbaik. Ia adalah perkhidmatan platform yang menyediakan keupayaan terbina untuk pelbagai model, Azure AI Search, Bing Search dan Fungsi Azure. Ia memudahkan pembinaan ejen dalam Portal Foundry dan penyebaran mereka secara berskala.

> S: Saya masih keliru, beri saya satu pilihan sahaja  
>
> J: Mulakan dengan Rangka Kerja Ejen Microsoft untuk membina ejen anda, dan kemudian gunakan Perkhidmatan Ejen AI Azure apabila anda perlu menyebar dan menskala mereka dalam pengeluaran. Pendekatan ini membolehkan anda iterasi dengan cepat pada logik ejen sambil mempunyai laluan jelas ke penyebaran perusahaan.

Mari ringkaskan perbezaan utama dalam jadual:

| Rangka Kerja | Tumpuan | Konsep Teras | Kes Penggunaan |
| --- | --- | --- | --- |
| Rangka Kerja Ejen Microsoft | SDK ejen yang dipermudahkan dengan pemanggilan alat | Ejen, Alat, Identiti Azure | Membina ejen AI, penggunaan alat, aliran kerja berbilang langkah |
| Perkhidmatan Ejen AI Azure | Model fleksibel, keselamatan perusahaan, Penjanaan Kod, Pemanggilan Alat | Modulariti, Kolaborasi, Orkestrasi Proses | Penyebaran ejen AI yang selamat, berskala, dan fleksibel |

## Bolehkah saya mengintegrasikan alat ekosistem Azure saya sedia ada secara langsung, atau adakah saya memerlukan penyelesaian berdiri sendiri?
Jawapannya ialah ya, anda boleh mengintegrasikan alat ekosistem Azure sedia ada anda terus dengan Perkhidmatan Ejen AI Azure terutamanya, kerana ia telah dibina untuk berfungsi dengan lancar bersama perkhidmatan Azure yang lain. Anda boleh contohnya mengintegrasikan Bing, Azure AI Search, dan Azure Functions. Terdapat juga integrasi mendalam dengan Microsoft Foundry.

Rangka Kerja Ejen Microsoft juga mengintegrasikan dengan perkhidmatan Azure melalui `AzureAIProjectAgentProvider` dan identiti Azure, membolehkan anda memanggil perkhidmatan Azure terus dari alat ejen anda.

## Kod Contoh

- Python: [Agent Framework](./code_samples/02-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## Ada Soalan Lagi tentang Rangka Kerja Ejen AI?

Sertai [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) untuk berjumpa dengan pelajar lain, menghadiri waktu pejabat dan dapatkan jawapan bagi soalan Ejen AI anda.

## Rujukan

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Perkhidmatan Ejen Azure</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Rangka Kerja Ejen Microsoft - Maklum Balas Azure OpenAI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Perkhidmatan Ejen AI Azure</a>

## Pelajaran Sebelumnya

[Pengantar kepada Ejen AI dan Kes Penggunaan Ejen](../01-intro-to-ai-agents/README.md)

## Pelajaran Seterusnya

[Memahami Corak Reka Bentuk Ejen](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sah dan utama. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau tafsiran yang salah yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->