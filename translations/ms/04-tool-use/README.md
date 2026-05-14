[![How to Design Good AI Agents](../../../translated_images/ms/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klik imej di atas untuk menonton video pelajaran ini)_

# Corak Reka Bentuk Penggunaan Alat

Alat adalah menarik kerana ia membolehkan ejen AI mempunyai julat keupayaan yang lebih luas. Daripada ejen hanya mempunyai satu set tindakan terhad yang boleh dilakukannya, dengan menambah alat, ejen kini boleh melaksanakan pelbagai jenis tindakan. Dalam bab ini, kita akan lihat Corak Reka Bentuk Penggunaan Alat, yang menerangkan bagaimana ejen AI boleh menggunakan alat khusus untuk mencapai matlamat mereka.

## Pengenalan

Dalam pelajaran ini, kita ingin menjawab soalan-soalan berikut:

- Apakah corak reka bentuk penggunaan alat?
- Apakah kes penggunaan yang boleh ia digunakan?
- Apakah elemen/blok binaan yang diperlukan untuk melaksanakan corak reka bentuk ini?
- Apakah pertimbangan khas untuk menggunakan Corak Reka Bentuk Penggunaan Alat bagi membina ejen AI yang boleh dipercayai?

## Matlamat Pembelajaran

Selepas menamatkan pelajaran ini, anda akan dapat:

- Mentakrif Corak Reka Bentuk Penggunaan Alat dan tujuannya.
- Mengenal pasti kes penggunaan di mana Corak Reka Bentuk Penggunaan Alat sesuai digunakan.
- Memahami elemen utama yang diperlukan untuk melaksanakan corak reka bentuk ini.
- Mengenal pasti pertimbangan untuk memastikan kebolehpercayaan dalam ejen AI yang menggunakan corak reka bentuk ini.

## Apakah Corak Reka Bentuk Penggunaan Alat?

**Corak Reka Bentuk Penggunaan Alat** memberi tumpuan kepada memberikan LLM keupayaan untuk berinteraksi dengan alat luaran bagi mencapai matlamat tertentu. Alat adalah kod yang boleh dijalankan oleh ejen untuk melaksanakan tindakan. Alat boleh berupa fungsi mudah seperti kalkulator, atau panggilan API ke perkhidmatan pihak ketiga seperti pencarian harga saham atau ramalan cuaca. Dalam konteks ejen AI, alat direka untuk dijalankan oleh ejen sebagai tindak balas kepada **panggilan fungsi yang dijana model**.

## Apakah kes penggunaan yang boleh ia digunakan?

Ejen AI boleh menggunakan alat untuk menyelesaikan tugasan kompleks, mendapatkan maklumat, atau membuat keputusan. Corak reka bentuk penggunaan alat sering digunakan dalam senario yang memerlukan interaksi dinamik dengan sistem luaran, seperti pangkalan data, perkhidmatan web, atau penterjemah kod. Keupayaan ini berguna untuk pelbagai kes penggunaan termasuk:

- **Pemerolehan Maklumat Dinamik:** Ejen boleh melakukan pertanyaan kepada API luaran atau pangkalan data untuk mendapatkan data terkini (contohnya, bertanya pada pangkalan data SQLite untuk analisis data, mendapatkan harga saham atau maklumat cuaca).
- **Pelaksanaan dan Penafsiran Kod:** Ejen boleh menjalankan kod atau skrip untuk menyelesaikan masalah matematik, menjana laporan, atau melakukan simulasi.
- **Automasi Aliran Kerja:** Automasi aliran kerja berulang atau berbilang langkah dengan mengintegrasi alat seperti penjadual tugas, perkhidmatan emel, atau saluran data.
- **Sokongan Pelanggan:** Ejen boleh berinteraksi dengan sistem CRM, platform tiket, atau pangkalan pengetahuan untuk menyelesaikan pertanyaan pengguna.
- **Penjanaan dan Penyuntingan Kandungan:** Ejen boleh menggunakan alat seperti pemeriksa tatabahasa, peringkas teks, atau penilai keselamatan kandungan untuk membantu tugasan penciptaan kandungan.

## Apakah elemen/blok binaan yang diperlukan untuk melaksanakan corak reka bentuk penggunaan alat?

Blok binaan ini membolehkan ejen AI melaksanakan pelbagai jenis tugasan. Mari lihat elemen utama yang diperlukan untuk melaksanakan Corak Reka Bentuk Penggunaan Alat:

- **Skema Fungsi/Alat**: Definisi terperinci alat yang tersedia, termasuk nama fungsi, tujuan, parameter yang diperlukan, dan keluaran yang dijangka. Skema ini membolehkan LLM memahami alat yang ada dan bagaimana membina permintaan yang sah.

- **Logik Pelaksanaan Fungsi**: Mengawal bila dan bagaimana alat digunakan berdasarkan niat pengguna dan konteks perbualan. Ini mungkin termasuk modul perancang, mekanisme penghalaan, atau aliran bersyarat yang menentukan penggunaan alat secara dinamik.

- **Sistem Pengendalian Mesej**: Komponen yang mengurus aliran perbualan antara input pengguna, respons LLM, panggilan alat, dan keluaran alat.

- **Rangka Kerja Integrasi Alat**: Infrastruktur yang menghubungkan ejen kepada pelbagai alat, sama ada fungsi mudah atau perkhidmatan luaran yang kompleks.

- **Pengendalian Ralat & Pengesahan**: Mekanisme untuk mengendalikan kegagalan pelaksanaan alat, mengesahkan parameter, dan mengurus respons tidak dijangka.

- **Pengurusan Keadaan**: Melacak konteks perbualan, interaksi alat terdahulu, dan data berterusan untuk memastikan konsistensi sepanjang interaksi berbilang pusingan.

Seterusnya, mari kita lihat Panggilan Fungsi/Alat dengan lebih terperinci.

### Panggilan Fungsi/Alat

Panggilan fungsi adalah cara utama kita membolehkan Model Bahasa Besar (LLM) berinteraksi dengan alat. Anda sering akan melihat 'Fungsi' dan 'Alat' digunakan secara bergantian kerana 'fungsi' (blok kod yang boleh digunakan semula) adalah 'alat' yang digunakan ejen untuk melaksanakan tugasan. Untuk kod fungsi dilaksanakan, LLM mesti membandingkan permintaan pengguna dengan keterangan fungsi. Untuk melakukan ini, satu skema yang mengandungi keterangan semua fungsi yang ada dihantar ke LLM. LLM kemudian memilih fungsi yang paling sesuai untuk tugasan tersebut dan mengembalikan namanya dan argumennya. Fungsi terpilih itu kemudian dijalankan, responsnya dihantar kembali ke LLM, yang menggunakan maklumat tersebut untuk membalas permintaan pengguna.

Untuk pembangun melaksanakan panggilan fungsi untuk ejen, anda memerlukan:

1. Model LLM yang menyokong panggilan fungsi
2. Skema yang mengandungi keterangan fungsi
3. Kod untuk setiap fungsi yang diterangkan

Mari gunakan contoh mendapatkan waktu semasa di sebuah bandar untuk menggambarkan:

1. **Inisialisasi LLM yang menyokong panggilan fungsi:**

    Tidak semua model menyokong panggilan fungsi, jadi penting untuk memeriksa bahawa LLM yang anda gunakan menyokongnya. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> menyokong panggilan fungsi. Kita boleh mulakan dengan memulakan klien Azure OpenAI.

    ```python
    # Inisialisasi klien Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Buat Skema Fungsi**:

    Seterusnya kita akan mentakrifkan skema JSON yang mengandungi nama fungsi, penerangan apa yang dibuat oleh fungsi itu, dan nama serta penerangan parameter fungsi tersebut.
    Kita kemudian akan mengambil skema ini dan memberikannya kepada klien yang dibuat tadi, bersama permintaan pengguna untuk mencari waktu di San Francisco. Yang penting untuk diperhatikan ialah panggilan **alat** adalah apa yang dikembalikan, **bukan** jawapan akhir kepada soalan. Seperti yang disebutkan sebelum ini, LLM mengembalikan nama fungsi yang dipilih untuk tugasan itu dan argumen yang akan dipassing kepadanya.

    ```python
    # Penerangan fungsi untuk model baca
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_time",
                "description": "Get the current time in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city name, e.g. San Francisco",
                        },
                    },
                    "required": ["location"],
                },
            }
        }
    ]
    ```
   
    ```python
  
    # Mesej pengguna awal
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Panggilan API pertama: Minta model menggunakan fungsi
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Proses jawapan model
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Kod fungsi yang diperlukan untuk melaksanakan tugasan:**

    Kini LLM telah memilih fungsi yang perlu dijalankan, kod yang melaksanakan tugasan perlu diterapkan dan dilaksanakan.
    Kita boleh melaksanakan kod untuk mendapatkan waktu semasa dalam Python. Kita juga perlu menulis kod untuk mengekstrak nama dan argumen daripada response_message untuk mendapatkan keputusan akhir.

    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

     ```python
     # Mengendalikan panggilan fungsi
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # Panggilan API kedua: Dapatkan respons akhir dari model
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

Panggilan Fungsi adalah teras kepada kebanyakan, jika tidak semua, reka bentuk penggunaan alat ejen, namun melaksanakannya dari awal boleh menjadi mencabar.
Seperti yang kita pelajari dalam [Pelajaran 2](../../../02-explore-agentic-frameworks), rangka kerja agentic menyediakan kita dengan blok binaan siap pakai untuk melaksanakan penggunaan alat.

## Contoh Penggunaan Alat dengan Rangka Kerja Agentic

Berikut adalah beberapa contoh bagaimana anda boleh melaksanakan Corak Reka Bentuk Penggunaan Alat menggunakan rangka kerja agentic yang berbeza:

### Rangka Kerja Ejen Microsoft

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Rangka Kerja Ejen Microsoft</a> adalah rangka kerja AI sumber terbuka untuk membina ejen AI. Ia mempermudah proses penggunaan panggilan fungsi dengan membenarkan anda mentakrifkan alat sebagai fungsi Python dengan penghias `@tool`. Rangka kerja ini mengendalikan komunikasi dua hala antara model dan kod anda. Ia juga menyediakan akses kepada alat siap guna seperti Carian Fail dan Penafsir Kod melalui `AzureAIProjectAgentProvider`.

Rajah berikut menggambarkan proses panggilan fungsi dengan Rangka Kerja Ejen Microsoft:

![function calling](../../../translated_images/ms/functioncalling-diagram.a84006fc287f6014.webp)

Dalam Rangka Kerja Ejen Microsoft, alat ditakrifkan sebagai fungsi yang dihias. Kita boleh menukar fungsi `get_current_time` yang kita lihat sebelum ini menjadi alat dengan menggunakan penghias `@tool`. Rangka kerja akan secara automatik menserialkan fungsi dan parameternya, mencipta skema untuk dihantar ke LLM.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Cipta klien
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Cipta agen dan jalankan dengan alat tersebut
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Perkhidmatan Ejen AI Azure

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Perkhidmatan Ejen AI Azure</a> adalah rangka kerja agentic yang lebih baru yang direka untuk memberi kuasa kepada pembangun untuk membina, menggulung keluar, dan menskalakan ejen AI berkualiti tinggi dan boleh diperluas dengan selamat tanpa perlu mengurus sumber pengkomputeran dan storan asas. Ia amat berguna untuk aplikasi perusahaan kerana ia adalah perkhidmatan yang dikendalikan sepenuhnya dengan keselamatan bertaraf perusahaan.

Jika dibandingkan dengan pembangunan menggunakan API LLM secara langsung, Perkhidmatan Ejen AI Azure menyediakan beberapa kelebihan, termasuk:

- Panggilan alat automatik – tiada keperluan untuk mengurai panggilan alat, melaksanakan alat tersebut, dan mengendalikan respons; semua ini kini dilakukan di sisi pelayan
- Pengurusan data selamat – daripada menguruskan keadaan perbualan sendiri, anda boleh bergantung pada threads untuk menyimpan semua maklumat yang anda perlukan
- Alat sedia ada – Alat yang boleh anda gunakan untuk berinteraksi dengan sumber data anda, seperti Bing, Azure AI Search, dan Azure Functions.

Alat yang tersedia dalam Perkhidmatan Ejen AI Azure boleh dibahagikan kepada dua kategori:

1. Alat Pengetahuan:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding dengan Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Carian Fail</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Alat Tindakan:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Panggilan Fungsi</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Penafsir Kod</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Alat yang ditakrifkan OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Perkhidmatan Ejen membolehkan kita menggunakan alat ini bersamaan sebagai `toolset`. Ia juga menggunakan `threads` yang menjejaki sejarah mesej dari perbualan tertentu.

Bayangkan anda adalah ejen jualan di sebuah syarikat bernama Contoso. Anda ingin membangunkan ejen perbualan yang boleh menjawab soalan mengenai data jualan anda.

Imej berikut menggambarkan bagaimana anda boleh menggunakan Perkhidmatan Ejen AI Azure untuk menganalisis data jualan anda:

![Agentic Service In Action](../../../translated_images/ms/agent-service-in-action.34fb465c9a84659e.webp)

Untuk menggunakan mana-mana alat ini dengan perkhidmatan, kita boleh mencipta klien dan mentakrifkan alat atau toolset. Untuk melaksanakan ini secara praktikal, kita boleh menggunakan kod Python berikut. LLM akan dapat melihat toolset ini dan memutuskan sama ada untuk menggunakan fungsi pengguna `fetch_sales_data_using_sqlite_query`, atau Penafsir Kod siap guna bergantung pada permintaan pengguna.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fungsi fetch_sales_data_using_sqlite_query yang boleh didapati dalam fail fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Inisialisasi set alat
toolset = ToolSet()

# Inisialisasi agen pemanggil fungsi dengan fungsi fetch_sales_data_using_sqlite_query dan menambahkannya ke set alat
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inisialisasi Alat Interpreter Kod dan menambahkannya ke set alat.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Apakah pertimbangan khas untuk menggunakan Corak Reka Bentuk Penggunaan Alat bagi membina ejen AI yang boleh dipercayai?

Kebimbangan biasa dengan SQL yang dijana secara dinamik oleh LLM adalah keselamatan, terutamanya risiko suntikan SQL atau tindakan berniat jahat, seperti menjatuhkan atau memanipulasi pangkalan data. Walaupun kebimbangan ini sah, ia boleh diatasi dengan berkesan dengan mengkonfigurasi kebenaran akses pangkalan data dengan betul. Untuk kebanyakan pangkalan data, ini melibatkan menetapkan pangkalan data sebagai baca sahaja. Untuk perkhidmatan pangkalan data seperti PostgreSQL atau Azure SQL, aplikasi harus diberikan peranan baca sahaja (SELECT).

Menjalankan aplikasi dalam persekitaran yang selamat juga meningkatkan perlindungan. Dalam senario perusahaan, data biasanya diekstrak dan diubah dari sistem operasi ke dalam pangkalan data baca sahaja atau gudang data dengan skema yang mesra pengguna. Pendekatan ini memastikan data selamat, dioptimumkan untuk prestasi dan kebolehcapaian, dan aplikasi mempunyai akses terhad, baca sahaja.

## Kod Contoh

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Ada Soalan Lagi tentang Corak Reka Bentuk Penggunaan Alat?

Sertai [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) untuk berjumpa dengan pelajar lain, menghadiri sesi office hours dan mendapatkan jawapan mengenai soalan AI Agen anda.

## Sumber Tambahan

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Bengkel Perkhidmatan Ejen AI Azure</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Bengkel Multi-Ejen Penulis Kreatif Contoso</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Gambaran Keseluruhan Rangka Kerja Ejen Microsoft</a>

## Pelajaran Sebelumnya

[Memahami Corak Reka Bentuk Agentic](../03-agentic-design-patterns/README.md)

## Pelajaran Seterusnya
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->