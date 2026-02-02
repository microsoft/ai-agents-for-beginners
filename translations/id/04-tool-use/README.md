[![Cara Merancang Agen AI yang Baik](../../../translated_images/id/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klik gambar di atas untuk menonton video pelajaran ini)_

# Pola Desain Penggunaan Alat

Alat menarik karena memungkinkan agen AI memiliki rentang kemampuan yang lebih luas. Alih-alih agen memiliki seperangkat tindakan terbatas yang dapat dilakukan, dengan menambahkan alat, agen kini dapat melakukan berbagai tindakan. Dalam bab ini, kita akan melihat Pola Desain Penggunaan Alat, yang menjelaskan bagaimana agen AI dapat menggunakan alat spesifik untuk mencapai tujuan mereka.

## Pendahuluan

Dalam pelajaran ini, kami berusaha menjawab pertanyaan berikut:

- Apa itu pola desain penggunaan alat?
- Untuk kasus penggunaan apa saja pola ini dapat diterapkan?
- Apa elemen/blok bangunan yang dibutuhkan untuk menerapkan pola desain ini?
- Apa pertimbangan khusus saat menggunakan Pola Desain Penggunaan Alat untuk membangun agen AI yang dapat dipercaya?

## Tujuan Pembelajaran

Setelah menyelesaikan pelajaran ini, Anda akan dapat:

- Mendefinisikan Pola Desain Penggunaan Alat dan tujuannya.
- Mengidentifikasi kasus penggunaan di mana Pola Desain Penggunaan Alat berlaku.
- Memahami elemen kunci yang dibutuhkan untuk menerapkan pola desain tersebut.
- Mengenali pertimbangan untuk memastikan kepercayaan pada agen AI yang menggunakan pola desain ini.

## Apa itu Pola Desain Penggunaan Alat?

**Pola Desain Penggunaan Alat** berfokus pada memberikan kemampuan kepada LLM untuk berinteraksi dengan alat eksternal guna mencapai tujuan tertentu. Alat adalah kode yang dapat dijalankan oleh agen untuk melakukan tindakan. Alat bisa berupa fungsi sederhana seperti kalkulator, atau panggilan API ke layanan pihak ketiga seperti pencarian harga saham atau prakiraan cuaca. Dalam konteks agen AI, alat dirancang untuk dijalankan oleh agen sebagai respons terhadap **panggilan fungsi yang dihasilkan model**.

## Untuk kasus penggunaan apa saja pola ini dapat diterapkan?

Agen AI dapat memanfaatkan alat untuk menyelesaikan tugas kompleks, mengambil informasi, atau membuat keputusan. Pola desain penggunaan alat sering dipakai dalam skenario yang membutuhkan interaksi dinamis dengan sistem eksternal, seperti basis data, layanan web, atau interpreter kode. Kemampuan ini berguna untuk sejumlah kasus penggunaan berbeda termasuk:

- **Pengambilan Informasi Dinamis:** Agen dapat mengquery API eksternal atau basis data untuk mengambil data terbaru (misalnya, mengquery basis data SQLite untuk analisis data, mengambil harga saham atau informasi cuaca).
- **Eksekusi dan Interpretasi Kode:** Agen dapat menjalankan kode atau skrip untuk menyelesaikan masalah matematika, menghasilkan laporan, atau melakukan simulasi.
- **Otomasi Alur Kerja:** Mengotomatiskan alur kerja berulang atau multi-langkah dengan mengintegrasikan alat seperti penjadwal tugas, layanan email, atau pipeline data.
- **Dukungan Pelanggan:** Agen bisa berinteraksi dengan sistem CRM, platform tiket, atau basis pengetahuan untuk menyelesaikan pertanyaan pengguna.
- **Pembuatan dan Penyuntingan Konten:** Agen dapat memanfaatkan alat seperti pemeriksa tata bahasa, peringkas teks, atau evaluator keamanan konten untuk membantu tugas pembuatan konten.

## Apa elemen/blok bangunan yang dibutuhkan untuk menerapkan pola desain penggunaan alat?

Blok bangunan ini memungkinkan agen AI melakukan berbagai tugas. Mari kita lihat elemen kunci yang dibutuhkan untuk menerapkan Pola Desain Penggunaan Alat:

- **Skema Fungsi/Alat**: Definisi rinci alat yang tersedia, termasuk nama fungsi, tujuan, parameter yang diperlukan, dan keluaran yang diharapkan. Skema ini memungkinkan LLM memahami alat apa saja yang tersedia dan bagaimana menyusun permintaan yang valid.

- **Logika Eksekusi Fungsi**: Mengatur bagaimana dan kapan alat dipanggil berdasarkan niat pengguna dan konteks percakapan. Ini mungkin mencakup modul perencana, mekanisme pengalihan, atau alur kondisional yang menentukan penggunaan alat secara dinamis.

- **Sistem Penanganan Pesan**: Komponen yang mengelola alur percakapan antara input pengguna, respons LLM, panggilan alat, dan keluaran alat.

- **Kerangka Integrasi Alat**: Infrastruktur yang menghubungkan agen dengan berbagai alat, baik itu fungsi sederhana atau layanan eksternal yang kompleks.

- **Penanganan Kesalahan & Validasi**: Mekanisme untuk menangani kegagalan eksekusi alat, memvalidasi parameter, dan mengelola respons tak terduga.

- **Manajemen Status**: Melacak konteks percakapan, interaksi alat sebelumnya, dan data persisten untuk memastikan konsistensi dalam interaksi multi-gilir.

Selanjutnya, mari kita lihat lebih rinci tentang Pemanggilan Fungsi/Alat.
 
### Pemanggilan Fungsi/Alat

Pemanggilan fungsi adalah cara utama kita memungkinkan Large Language Models (LLM) untuk berinteraksi dengan alat. Anda akan sering melihat 'Fungsi' dan 'Alat' digunakan secara bergantian karena 'fungsi' (blok kode yang dapat dipakai ulang) adalah 'alat' yang digunakan agen untuk menjalankan tugas. Agar kode fungsi dapat dipanggil, LLM harus membandingkan permintaan pengguna dengan deskripsi fungsi tersebut. Untuk ini, sebuah skema yang berisi deskripsi seluruh fungsi yang tersedia dikirim ke LLM. LLM kemudian memilih fungsi paling tepat untuk tugas tersebut dan mengembalikan nama serta argumennya. Fungsi yang dipilih dijalankan, responsnya dikirim kembali ke LLM, yang menggunakan informasi itu untuk menanggapi permintaan pengguna.

Untuk pengembang yang ingin menerapkan pemanggilan fungsi bagi agen, Anda akan membutuhkan:

1. Model LLM yang mendukung pemanggilan fungsi  
2. Skema yang berisi deskripsi fungsi  
3. Kode untuk setiap fungsi yang dideskripsikan  

Mari kita pakai contoh mendapatkan waktu saat ini di sebuah kota untuk ilustrasi:

1. **Inisialisasi LLM yang mendukung pemanggilan fungsi:**

    Tidak semua model mendukung pemanggilan fungsi, jadi penting memeriksa apakah LLM yang Anda gunakan melakukannya. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> mendukung pemanggilan fungsi. Kita bisa mulai dengan menginisiasi klien Azure OpenAI. 

    ```python
    # Inisialisasi klien Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Buat Skema Fungsi:**

    Selanjutnya kita akan mendefinisikan skema JSON yang berisi nama fungsi, deskripsi apa yang dilakukan fungsi tersebut, serta nama dan deskripsi parameter fungsi.
    Skema ini kemudian kita kirim ke klien yang dibuat sebelumnya, bersama dengan permintaan pengguna untuk mencari waktu di San Francisco. Yang penting dicatat adalah **panggilan alat** yang dikembalikan, **bukan** jawaban akhir atas pertanyaan. Seperti yang disebutkan sebelumnya, LLM mengembalikan nama fungsi yang dipilih untuk tugas tersebut, serta argumen yang akan diteruskan kepadanya.

    ```python
    # Deskripsi fungsi untuk dibaca model
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
  
    # Pesan awal pengguna
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Panggilan API pertama: Minta model untuk menggunakan fungsi
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
  
1. **Kode fungsi yang diperlukan untuk menjalankan tugas:**

    Setelah LLM memilih fungsi yang perlu dijalankan, kode yang menjalankan tugas harus diimplementasikan dan dieksekusi.
    Kita bisa mengimplementasikan kode untuk mendapatkan waktu saat ini menggunakan Python. Kita juga perlu menulis kode untuk mengekstrak nama dan argumen dari response_message guna memperoleh hasil akhir.

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
     # Menangani pemanggilan fungsi
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

Pemanggilan Fungsi adalah inti dari sebagian besar, jika tidak semua, desain penggunaan alat agen, namun mengimplementasikannya dari awal kadang bisa menjadi tantangan.
Seperti yang kita pelajari di [Pelajaran 2](../../../02-explore-agentic-frameworks), kerangka kerja agen memberikan blok bangunan yang sudah jadi untuk menerapkan penggunaan alat.
 
## Contoh Penggunaan Alat dengan Kerangka Kerja Agen

Berikut beberapa contoh bagaimana Anda dapat menerapkan Pola Desain Penggunaan Alat menggunakan kerangka kerja agen berbeda:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> adalah kerangka AI open-source untuk pengembang .NET, Python, dan Java yang bekerja dengan Large Language Models (LLM). Ini menyederhanakan proses menggunakan pemanggilan fungsi dengan secara otomatis mendeskripsikan fungsi dan parameternya kepada model melalui proses yang disebut <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serialisasi</a>. Ia juga menangani komunikasi bolak-balik antara model dan kode Anda. Keunggulan lain menggunakan kerangka agen seperti Semantic Kernel adalah memungkinkan Anda mengakses alat yang sudah jadi seperti <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">Pencarian File</a> dan <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Interpreter Kode</a>.

Diagram berikut mengilustrasikan proses pemanggilan fungsi dengan Semantic Kernel:

![function calling](../../../translated_images/id/functioncalling-diagram.a84006fc287f6014.webp)

Dalam Semantic Kernel fungsi/alat disebut <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Plugin</a>. Kita dapat mengonversi fungsi `get_current_time` yang kita lihat sebelumnya menjadi plugin dengan mengubahnya menjadi kelas yang berisi fungsi tersebut. Kita juga bisa mengimpor dekorator `kernel_function`, yang menerima deskripsi fungsi. Saat Anda membuat kernel dengan GetCurrentTimePlugin, kernel akan secara otomatis melakukan serialisasi fungsi dan parameternya, membuat skema untuk dikirim ke LLM dalam prosesnya.

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

# Buat kernel
kernel = Kernel()

# Buat plugin
get_current_time_plugin = GetCurrentTimePlugin(location)

# Tambahkan plugin ke kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### Layanan Agen Azure AI

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Layanan Agen Azure AI</a> adalah kerangka agen baru yang dirancang untuk memberdayakan pengembang membangun, menyebarkan, dan menskalakan agen AI berkualitas tinggi dan dapat diperluas dengan aman tanpa perlu mengelola sumber daya komputasi dan penyimpanan dasar. Ini sangat berguna untuk aplikasi perusahaan karena merupakan layanan yang sepenuhnya dikelola dengan keamanan berkelas perusahaan.

Jika dibandingkan dengan pengembangan langsung menggunakan API LLM, Layanan Agen Azure AI menawarkan beberapa keuntungan, antara lain:

- Pemanggilan alat otomatis – tidak perlu mengurai panggilan alat, memanggil alat, dan menangani respons; semua ini dilakukan di sisi server
- Data yang dikelola secara aman – alih-alih mengelola status percakapan sendiri, Anda dapat mengandalkan thread untuk menyimpan semua informasi yang dibutuhkan
- Alat siap pakai – Alat yang dapat digunakan untuk berinteraksi dengan sumber data Anda, seperti Bing, Azure AI Search, dan Azure Functions.

Alat yang tersedia di Layanan Agen Azure AI dapat dibagi menjadi dua kategori:

1. Alat Pengetahuan:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding dengan Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Pencarian File</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Alat Aksi:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Pemanggilan Fungsi</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Interpreter Kode</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Alat yang didefinisikan OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Layanan Agen memungkinkan kita menggunakan alat-alat ini bersama sebagai `toolset`. Layanan ini juga memanfaatkan `thread` yang melacak riwayat pesan dari percakapan tertentu.

Bayangkan Anda adalah agen penjualan di perusahaan bernama Contoso. Anda ingin mengembangkan agen percakapan yang dapat menjawab pertanyaan tentang data penjualan Anda.

Gambar berikut mengilustrasikan bagaimana Anda bisa menggunakan Layanan Agen Azure AI untuk menganalisis data penjualan Anda:

![Agentic Service In Action](../../../translated_images/id/agent-service-in-action.34fb465c9a84659e.webp)

Untuk menggunakan salah satu alat ini dengan layanan, kita dapat membuat klien dan menentukan alat atau toolset. Untuk menerapkannya secara praktis, kita dapat menggunakan kode Python berikut. LLM akan dapat melihat toolset dan memutuskan apakah menggunakan fungsi buatan pengguna, `fetch_sales_data_using_sqlite_query`, atau Interpreter Kode bawaan tergantung pada permintaan pengguna.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fungsi fetch_sales_data_using_sqlite_query yang dapat ditemukan di file fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Inisialisasi toolset
toolset = ToolSet()

# Inisialisasi agen pemanggil fungsi dengan fungsi fetch_sales_data_using_sqlite_query dan menambahkannya ke toolset
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inisialisasi alat Code Interpreter dan menambahkannya ke toolset.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Apa pertimbangan khusus saat menggunakan Pola Desain Penggunaan Alat untuk membangun agen AI yang dapat dipercaya?

Kekhawatiran umum dengan SQL yang dihasilkan dinamis oleh LLM adalah keamanan, khususnya risiko injeksi SQL atau tindakan berbahaya, seperti menghapus atau mengubah basis data. Walaupun kekhawatiran ini valid, hal tersebut dapat diatasi secara efektif dengan mengonfigurasi hak akses basis data dengan benar. Untuk sebagian besar basis data, ini melibatkan pengaturan basis data sebagai hanya baca. Untuk layanan basis data seperti PostgreSQL atau Azure SQL, aplikasi harus diberikan peran hanya baca (SELECT).
Menjalankan aplikasi di lingkungan yang aman semakin meningkatkan perlindungan. Dalam skenario perusahaan, data biasanya diambil dan diubah dari sistem operasional ke dalam basis data atau gudang data yang hanya dapat dibaca dengan skema yang ramah pengguna. Pendekatan ini memastikan bahwa data aman, dioptimalkan untuk kinerja dan aksesibilitas, serta aplikasi memiliki akses terbatas hanya untuk membaca.

## Sample Codes

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Punya Pertanyaan Lebih Lanjut tentang Pola Desain Penggunaan Alat?

Bergabunglah dengan [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) untuk bertemu dengan pelajar lain, mengikuti jam kantor, dan mendapatkan jawaban atas pertanyaan tentang AI Agents Anda.

## Sumber Daya Tambahan

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Workshop Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Workshop Multi-Agent Penulis Kreatif Contoso</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Tutorial Pemanggilan Fungsi Semantic Kernel</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Interpreter Kode Semantic Kernel</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Alat Autogen</a>

## Pelajaran Sebelumnya

[Memahami Pola Desain Agentik](../03-agentic-design-patterns/README.md)

## Pelajaran Selanjutnya

[Agentik RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya menjaga akurasi, harap diperhatikan bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang salah yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->