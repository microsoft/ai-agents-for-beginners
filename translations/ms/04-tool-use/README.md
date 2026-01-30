[![Bagaimana Reka Bentuk Ejen AI yang Baik](../../../translated_images/ms/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klik imej di atas untuk melihat video pelajaran ini)_

# Corak Reka Bentuk Penggunaan Alat

Alat adalah menarik kerana ia membenarkan ejen AI mempunyai julat keupayaan yang lebih luas. Daripada ejen hanya mempunyai set tindakan terhad yang boleh dilakukan, dengan menambah alat, ejen kini boleh melakukan pelbagai tindakan. Dalam bab ini, kita akan melihat Corak Reka Bentuk Penggunaan Alat, yang menerangkan bagaimana ejen AI boleh menggunakan alat khusus untuk mencapai matlamat mereka.

## Pengenalan

Dalam pelajaran ini, kami ingin menjawab soalan-soalan berikut:

- Apakah corak reka bentuk penggunaan alat?
- Apakah kes penggunaan yang boleh ia diterapkan?
- Apakah elemen/blok binaan yang diperlukan untuk melaksanakan corak reka bentuk ini?
- Apakah pertimbangan khusus untuk menggunakan Corak Reka Bentuk Penggunaan Alat bagi membina ejen AI yang boleh dipercayai?

## Matlamat Pembelajaran

Selepas menamatkan pelajaran ini, anda akan dapat:

- Mentakrifkan Corak Reka Bentuk Penggunaan Alat dan tujuannya.
- Mengenal pasti kes penggunaan di mana Corak Reka Bentuk Penggunaan Alat sesuai digunakan.
- Memahami elemen utama yang diperlukan untuk melaksanakan corak reka bentuk ini.
- Mengenal pasti pertimbangan untuk memastikan kebolehpercayaan ejen AI yang menggunakan corak reka bentuk ini.

## Apakah Corak Reka Bentuk Penggunaan Alat?

**Corak Reka Bentuk Penggunaan Alat** memberi fokus kepada memberikan LLM keupayaan untuk berinteraksi dengan alat luar untuk mencapai matlamat tertentu. Alat adalah kod yang boleh dijalankan oleh ejen untuk melakukan tindakan. Alat boleh berupa fungsi mudah seperti kalkulator, atau panggilan API ke perkhidmatan pihak ketiga seperti carian harga saham atau ramalan cuaca. Dalam konteks ejen AI, alat direka untuk dijalankan oleh ejen sebagai tindak balas kepada **panggilan fungsi yang dijana oleh model**.

## Apakah kes penggunaan yang boleh ia diterapkan?

Ejen AI boleh menggunakan alat untuk melengkapkan tugas kompleks, mendapatkan maklumat, atau membuat keputusan. Corak reka bentuk penggunaan alat sering digunakan dalam senario yang memerlukan interaksi dinamik dengan sistem luar, seperti pangkalan data, perkhidmatan web, atau pemapar kod. Keupayaan ini berguna untuk pelbagai kes penggunaan termasuk:

- **Pengambilan Maklumat Dinamik:** Ejen boleh membuat pertanyaan API luar atau pangkalan data untuk mendapatkan data terkini (contohnya, menyoal pangkalan data SQLite untuk analisis data, mendapatkan harga saham atau maklumat cuaca).
- **Pelaksanaan dan Tafsiran Kod:** Ejen boleh menjalankan kod atau skrip untuk menyelesaikan masalah matematik, menjana laporan, atau melaksanakan simulasi.
- **Automasi Aliran Kerja:** Mengautomasikan tugasan berulang atau aliran kerja berbilang langkah dengan mengintegrasikan alat seperti penjadual tugas, perkhidmatan e-mel, atau saluran data.
- **Sokongan Pelanggan:** Ejen boleh berinteraksi dengan sistem CRM, platform tiket, atau pangkalan ilmu untuk menyelesaikan pertanyaan pengguna.
- **Penjanaan dan Penyuntingan Kandungan:** Ejen boleh menggunakan alat seperti pemeriksa tatabahasa, peringkas teks, atau penilai keselamatan kandungan untuk membantu dalam tugasan penciptaan kandungan.

## Apakah elemen/blok binaan yang diperlukan untuk melaksanakan corak reka bentuk penggunaan alat?

Blok binaan ini membolehkan ejen AI melakukan pelbagai tugas. Mari kita lihat elemen utama yang diperlukan untuk melaksanakan Corak Reka Bentuk Penggunaan Alat:

- **Skema Fungsi/Alat**: Definisi terperinci tentang alat yang tersedia, termasuk nama fungsi, tujuan, parameter diperlukan, dan output yang dijangkakan. Skema ini membolehkan LLM memahami alat mana yang ada dan bagaimana untuk membina permintaan yang sah.

- **Logik Pelaksanaan Fungsi**: Mengawal bagaimana dan bila alat dipanggil berdasarkan niat pengguna dan konteks perbualan. Ini mungkin termasuk modul perancang, mekanisme penghalaan, atau aliran bersyarat yang menentukan penggunaan alat secara dinamik.

- **Sistem Pengendalian Mesej**: Komponen yang mengurus aliran perbualan antara input pengguna, respons LLM, panggilan alat, dan output alat.

- **Rangka Kerja Integrasi Alat**: Infrastruktur yang menghubungkan ejen dengan pelbagai alat, sama ada fungsi mudah atau perkhidmatan luar yang kompleks.

- **Pengendalian Ralat & Pengesahan**: Mekanisme untuk mengurus kegagalan pelaksanaan alat, mengesahkan parameter, dan mengendalikan respons yang tidak dijangka.

- **Pengurusan Keadaan**: Mengesan konteks perbualan, interaksi alat sebelumnya, dan data persisten untuk memastikan konsistensi dalam interaksi berbilang pusingan.

Seterusnya, mari kita lihat Panggilan Fungsi/Alat dengan lebih terperinci.
 
### Panggilan Fungsi/Alat

Panggilan fungsi adalah cara utama kita membolehkan Model Bahasa Besar (LLM) berinteraksi dengan alat. Anda sering akan melihat 'Fungsi' dan 'Alat' digunakan secara bergantian kerana 'fungsi' (blok kod yang boleh digunakan semula) adalah 'alat' yang ejen gunakan untuk melaksanakan tugasan. Untuk kod fungsi dijalankan, LLM mesti membandingkan permintaan pengguna dengan penerangan fungsi. Untuk melakukan ini, skema yang mengandungi penerangan semua fungsi yang tersedia dihantar kepada LLM. LLM kemudian memilih fungsi yang paling sesuai untuk tugasan dan mengembalikan nama serta argumennya. Fungsi yang dipilih dilaksanakan, responsnya dihantar kembali kepada LLM, yang menggunakan maklumat itu untuk membalas permintaan pengguna.

Untuk pembangun melaksanakan panggilan fungsi bagi ejen, anda memerlukan:

1. Model LLM yang menyokong panggilan fungsi
2. Skema yang mengandungi penerangan fungsi
3. Kod untuk setiap fungsi yang diterangkan

Mari kita gunakan contoh mendapatkan masa semasa di sebuah bandar untuk menggambarkan:

1. **Inisialisasi LLM yang menyokong panggilan fungsi:**

    Tidak semua model menyokong panggilan fungsi, jadi penting untuk menyemak sama ada LLM yang anda gunakan menyokongnya. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> menyokong panggilan fungsi. Kita boleh mulakan dengan memulakan klien Azure OpenAI.

    ```python
    # Mulakan klien Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Cipta Skema Fungsi:**

    Seterusnya kita akan mentakrifkan skema JSON yang mengandungi nama fungsi, penerangan tentang apa yang dilakukan fungsi tersebut, serta nama dan penerangan parameter fungsi.
    Kemudian kita akan menghantar skema ini ke klien yang telah dicipta sebelum ini, bersama-sama dengan permintaan pengguna untuk mencari masa di San Francisco. Yang penting diperhatikan ialah **panggilan alat** ialah apa yang dikembalikan, **bukan** jawapan akhir kepada soalan. Seperti yang disebut sebelumnya, LLM mengembalikan nama fungsi yang dipilih untuk tugasan, dan argumen yang akan dihantar kepadanya.

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
  
      # Proses respons model
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

    Setelah LLM memilih fungsi mana yang perlu dijalankan, kod yang melaksanakan tugasan perlu ditulis dan dijalankan.
    Kita boleh melaksanakan kod untuk mendapatkan masa semasa dalam Python. Kita juga perlu menulis kod untuk mengekstrak nama dan argumen daripada response_message untuk mendapatkan hasil akhir.

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
  
      # Panggilan API kedua: Dapatkan respons terakhir daripada model
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

Panggilan Fungsi adalah teras kepada kebanyakan, jika tidak semua, reka bentuk penggunaan alat ejen, namun melaksanakan panggilan fungsi dari awal kadangkala boleh mencabar.
Seperti yang kita pelajari dalam [Pelajaran 2](../../../02-explore-agentic-frameworks), rangka kerja agentik menyediakan blok binaan siap untuk melaksanakan penggunaan alat.
 
## Contoh Penggunaan Alat dengan Rangka Kerja Agentik

Berikut adalah beberapa contoh bagaimana anda boleh melaksanakan Corak Reka Bentuk Penggunaan Alat menggunakan pelbagai rangka kerja agentik:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> adalah rangka kerja AI sumber terbuka untuk pembangun .NET, Python, dan Java yang bekerja dengan Model Bahasa Besar (LLM). Ia memudahkan proses menggunakan panggilan fungsi dengan secara automatik menerangkan fungsi anda dan parameter kepada model melalui proses yang dipanggil <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serialisasi</a>. Ia juga mengendalikan komunikasi dua hala antara model dan kod anda. Kelebihan lain menggunakan rangka kerja agentik seperti Semantic Kernel ialah ia membolehkan anda mengakses alat pra-bina seperti <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">Carian Fail</a> dan <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Penafsir Kod</a>.

Rajah berikut menggambarkan proses panggilan fungsi dengan Semantic Kernel:

![panggilan fungsi](../../../translated_images/ms/functioncalling-diagram.a84006fc287f6014.webp)

Dalam Semantic Kernel, fungsi/alat dipanggil <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugin</a>. Kita boleh menukar fungsi `get_current_time` yang kita lihat sebelum ini menjadi plugin dengan menukarnya menjadi kelas yang mengandungi fungsi tersebut. Kita juga boleh mengimport dekorator `kernel_function`, yang mengambil penerangan fungsi sebagai input. Apabila anda kemudian mencipta kernel dengan GetCurrentTimePlugin, kernel secara automatik akan menyerialkan fungsi dan parameternya, mencipta skema untuk dihantar ke LLM dalam proses.

```python
from semantic_kernel.functions import kernel_function

class GetCurrentTimePlugin:
    async def __init__(self, location):
        self.location = location

    @kernel_function(
        description="Get the current time for a given location"
    )
    def get_current_time(location: str = ""):
        ...

```

```python 
from semantic_kernel import Kernel

# Cipta kernel
kernel = Kernel()

# Cipta pemalam
get_current_time_plugin = GetCurrentTimePlugin(location)

# Tambah pemalam ke kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### Perkhidmatan Ejen Azure AI

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Perkhidmatan Ejen Azure AI</a> adalah rangka kerja agentik yang lebih baru yang direka untuk membolehkan pembangun membina, menyebarkan, dan skala ejen AI yang berkualiti tinggi dan boleh dikembangkan dengan selamat tanpa perlu mengurus sumber pengiraan dan simpanan asas. Ia sangat berguna untuk aplikasi perusahaan kerana ia perkhidmatan yang diurus sepenuhnya dengan keselamatan tahap perusahaan.

Dibandingkan dengan pembangunan menggunakan API LLM secara langsung, Perkhidmatan Ejen Azure AI menyediakan beberapa kelebihan, termasuk:

- Panggilan alat automatik – tiada keperluan untuk mengurai panggilan alat, melaksanakan alat, dan mengendalikan respons; semua ini kini dilakukan di sisi pelayan
- Data yang diurus dengan selamat – bukannya mengurus keadaan perbualan sendiri, anda boleh bergantung kepada threads untuk menyimpan semua maklumat yang diperlukan
- Alat sedia pakai – Alat yang anda boleh gunakan untuk berinteraksi dengan sumber data anda, seperti Bing, Azure AI Search, dan Azure Functions.

Alat yang tersedia dalam Perkhidmatan Ejen Azure AI boleh dibahagikan kepada dua kategori:

1. Alat Pengetahuan:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Pengesan dengan Carian Bing</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Carian Fail</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Alat Tindakan:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Panggilan Fungsi</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Penafsir Kod</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Alat yang Didefinisikan OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Perkhidmatan Ejen membolehkan kita menggunakan alat ini bersama sebagai satu `toolset`. Ia juga menggunakan `threads` yang menyimpan sejarah mesej daripada satu perbualan tertentu.

Bayangkan anda seorang ejen jualan di sebuah syarikat bernama Contoso. Anda ingin membangunkan ejen perbualan yang boleh menjawab soalan tentang data jualan anda.

Imej berikut menggambarkan bagaimana anda boleh menggunakan Perkhidmatan Ejen Azure AI untuk menganalisis data jualan anda:

![Perkhidmatan Agentik Dalam Tindakan](../../../translated_images/ms/agent-service-in-action.34fb465c9a84659e.webp)

Untuk menggunakan mana-mana alat ini dengan perkhidmatan tersebut kita boleh mencipta klien dan mentakrifkan alat atau set alat. Untuk melaksanakan ini secara praktikal, kita boleh menggunakan kod Python berikut. LLM akan dapat melihat set alat dan memutuskan sama ada menggunakan fungsi ciptaan pengguna, `fetch_sales_data_using_sqlite_query`, atau Penafsir Kod pra-bina bergantung pada permintaan pengguna.

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

# Inisialisasi ejen pemanggilan fungsi dengan fungsi fetch_sales_data_using_sqlite_query dan menambahkannya ke set alat
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inisialisasi alat Penafsir Kod dan menambahkannya ke set alat.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Apakah pertimbangan khusus untuk menggunakan Corak Reka Bentuk Penggunaan Alat bagi membina ejen AI yang boleh dipercayai?

Kebimbangan biasa dengan SQL yang dijana secara dinamik oleh LLM adalah keselamatan, terutama risiko suntikan SQL atau tindakan berniat jahat, seperti menjatuhkan atau mengubah pangkalan data. Walaupun kebimbangan ini sah, ia boleh diatasi dengan berkesan dengan mengkonfigurasi kebenaran akses pangkalan data dengan betul. Untuk kebanyakan pangkalan data, ini melibatkan mengkonfigurasi pangkalan data sebagai baca sahaja. Bagi perkhidmatan pangkalan data seperti PostgreSQL atau Azure SQL, aplikasi harus diberikan peranan baca sahaja (SELECT).
Menjalankan aplikasi dalam persekitaran yang selamat meningkatkan perlindungan. Dalam senario perusahaan, data biasanya diekstrak dan diubah suai daripada sistem operasi ke pangkalan data hanya baca atau gudang data dengan skema yang mesra pengguna. Pendekatan ini memastikan data selamat, dioptimumkan untuk prestasi dan kebolehcapaian, serta aplikasi mempunyai akses terhad hanya baca.

## Kod Contoh

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Ada Lebih Banyak Soalan tentang Corak Reka Bentuk Penggunaan Alat?

Sertai [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) untuk berjumpa dengan pelajar lain, menghadiri waktu pejabat dan mendapatkan jawapan bagi soalan AI Agents anda.

## Sumber Tambahan

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Bengkel Perkhidmatan Azure AI Agents</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Bengkel Multi-Ejen Penulis Kreatif Contoso</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Tutorial Panggilan Fungsi Semantic Kernel</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Penterjemah Kod Semantic Kernel</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Alat Autogen</a>

## Pelajaran Sebelumnya

[Memahami Corak Reka Bentuk Agentik](../03-agentic-design-patterns/README.md)

## Pelajaran Seterusnya

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya hendaklah dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh penterjemah manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->