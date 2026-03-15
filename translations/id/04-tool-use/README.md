[![Cara Merancang Agen AI yang Baik](../../../translated_images/id/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klik gambar di atas untuk menonton video pelajaran ini)_

# Pola Desain Penggunaan Alat

Alat menarik karena memungkinkan agen AI memiliki rentang kemampuan yang lebih luas. Alih-alih agen hanya memiliki seperangkat tindakan terbatas yang dapat dilakukan, dengan menambahkan alat, agen kini dapat melakukan berbagai tindakan yang luas. Dalam bab ini, kita akan melihat Pola Desain Penggunaan Alat, yang menjelaskan bagaimana agen AI dapat menggunakan alat khusus untuk mencapai tujuan mereka.

## Pendahuluan

Dalam pelajaran ini, kita akan mencari jawaban atas pertanyaan berikut:

- Apa itu pola desain penggunaan alat?
- Untuk kasus penggunaan apa saja pola ini dapat diterapkan?
- Elemen/bangunan dasar apa saja yang dibutuhkan untuk mengimplementasikan pola desain ini?
- Pertimbangan khusus apa saja dalam menggunakan Pola Desain Penggunaan Alat untuk membangun agen AI yang dapat dipercaya?

## Tujuan Pembelajaran

Setelah menyelesaikan pelajaran ini, Anda akan dapat:

- Mendefinisikan Pola Desain Penggunaan Alat dan tujuannya.
- Mengidentifikasi kasus penggunaan di mana Pola Desain Penggunaan Alat dapat diterapkan.
- Memahami elemen kunci yang dibutuhkan untuk mengimplementasikan pola desain.
- Mengenali pertimbangan untuk memastikan kepercayaan pada agen AI yang menggunakan pola desain ini.

## Apa itu Pola Desain Penggunaan Alat?

**Pola Desain Penggunaan Alat** berfokus pada memberi kemampuan pada LLM untuk berinteraksi dengan alat eksternal guna mencapai tujuan tertentu. Alat adalah kode yang dapat dijalankan oleh agen untuk melakukan tindakan. Alat bisa berupa fungsi sederhana seperti kalkulator, atau panggilan API ke layanan pihak ketiga seperti pencarian harga saham atau prakiraan cuaca. Dalam konteks agen AI, alat dirancang untuk dijalankan oleh agen sebagai respons terhadap **pemanggilan fungsi yang dihasilkan model**.

## Untuk kasus penggunaan apa saja pola ini dapat diterapkan?

Agen AI dapat memanfaatkan alat untuk menyelesaikan tugas kompleks, mengambil informasi, atau membuat keputusan. Pola desain penggunaan alat sering digunakan dalam skenario yang membutuhkan interaksi dinamis dengan sistem eksternal, seperti basis data, layanan web, atau interpreter kode. Kemampuan ini berguna untuk sejumlah kasus penggunaan berbeda termasuk:

- **Pengambilan Informasi Dinamis:** Agen dapat melakukan kueri ke API eksternal atau basis data untuk mengambil data terbaru (misalnya, mengkueri basis data SQLite untuk analisis data, mengambil harga saham atau informasi cuaca).
- **Eksekusi dan Interpretasi Kode:** Agen dapat menjalankan kode atau skrip untuk memecahkan masalah matematika, membuat laporan, atau melakukan simulasi.
- **Otomasi Alur Kerja:** Mengotomatiskan alur kerja berulang atau multi-langkah dengan mengintegrasikan alat seperti penjadwal tugas, layanan email, atau pipeline data.
- **Dukungan Pelanggan:** Agen dapat berinteraksi dengan sistem CRM, platform tiket, atau basis pengetahuan untuk menyelesaikan pertanyaan pengguna.
- **Pembuatan dan Penyuntingan Konten:** Agen dapat memanfaatkan alat seperti pemeriksa tata bahasa, peringkas teks, atau evaluator keamanan konten untuk membantu tugas pembuatan konten.

## Elemen/bangunan dasar apa saja yang dibutuhkan untuk mengimplementasikan pola desain penggunaan alat?

Bangunan dasar ini memungkinkan agen AI untuk melakukan berbagai tugas. Mari kita lihat elemen kunci yang dibutuhkan untuk menerapkan Pola Desain Penggunaan Alat:

- **Skema Fungsi/Alat**: Definisi rinci alat yang tersedia, termasuk nama fungsi, tujuan, parameter yang diperlukan, dan keluaran yang diharapkan. Skema ini memungkinkan LLM memahami alat apa yang tersedia dan bagaimana menyusun permintaan yang valid.

- **Logika Eksekusi Fungsi**: Mengatur bagaimana dan kapan alat dipanggil berdasarkan niat pengguna dan konteks percakapan. Ini bisa meliputi modul perencana, mekanisme pengalihan, atau alur kondisional yang menentukan penggunaan alat secara dinamis.

- **Sistem Penanganan Pesan**: Komponen yang mengelola alur percakapan antara masukan pengguna, respons LLM, panggilan alat, dan keluaran alat.

- **Kerangka Integrasi Alat**: Infrastruktur yang menghubungkan agen ke berbagai alat, baik berupa fungsi sederhana atau layanan eksternal kompleks.

- **Penanganan Kesalahan & Validasi**: Mekanisme untuk menangani kegagalan dalam eksekusi alat, memvalidasi parameter, dan mengelola respons tak terduga.

- **Manajemen Status**: Melacak konteks percakapan, interaksi alat sebelumnya, dan data persisten untuk memastikan konsistensi sepanjang interaksi multi-tahap.

Selanjutnya, mari kita lihat lebih detail tentang Panggilan Fungsi/Alat.
 
### Panggilan Fungsi/Alat

Panggilan fungsi adalah cara utama kita memungkinkan Model Bahasa Besar (LLM) berinteraksi dengan alat. Anda sering akan melihat 'Fungsi' dan 'Alat' digunakan secara bergantian karena 'fungsi' (blok kode yang dapat digunakan ulang) adalah 'alat' yang digunakan agen untuk menjalankan tugas. Agar kode fungsi dapat dipanggil, sebuah LLM harus membandingkan permintaan pengguna dengan deskripsi fungsi tersebut. Untuk melakukan ini, skema yang berisi deskripsi semua fungsi yang tersedia dikirim ke LLM. LLM kemudian memilih fungsi yang paling sesuai untuk tugas tersebut dan mengembalikan nama serta argumennya. Fungsi yang dipilih dipanggil, responsnya dikirim kembali ke LLM, yang menggunakan informasi tersebut untuk menanggapi permintaan pengguna.

Untuk pengembang yang ingin mengimplementasikan panggilan fungsi untuk agen, Anda memerlukan:

1. Model LLM yang mendukung panggilan fungsi
2. Skema yang berisi deskripsi fungsi
3. Kode untuk setiap fungsi yang dijelaskan

Mari gunakan contoh mengambil waktu saat ini di sebuah kota untuk mengilustrasikan:

1. **Inisialisasi LLM yang mendukung panggilan fungsi:**

    Tidak semua model mendukung panggilan fungsi, jadi penting untuk memastikan LLM yang Anda gunakan mendukungnya. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> mendukung panggilan fungsi. Kita dapat memulai dengan menginisialisasi klien Azure OpenAI. 

    ```python
    # Inisialisasi klien Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Buat Skema Fungsi**:

    Selanjutnya kita akan mendefinisikan skema JSON yang berisi nama fungsi, deskripsi tentang apa yang dilakukan fungsi, serta nama dan deskripsi parameter fungsi.
    Kita kemudian akan mengirimkan skema ini ke klien yang dibuat sebelumnya, bersama dengan permintaan pengguna untuk mencari waktu di San Francisco. Yang penting dicatat adalah bahwa **panggilan alat** adalah yang dikembalikan, **bukan** jawaban akhir dari pertanyaan. Seperti yang disebutkan sebelumnya, LLM mengembalikan nama fungsi yang dipilih untuk tugas tersebut, beserta argumen yang akan diberikan ke fungsi itu.

    ```python
    # Deskripsi fungsi untuk model membaca
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
  
    # Pesan pengguna awal
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

    Setelah LLM memilih fungsi yang perlu dijalankan, kode yang menjalankan tugas tersebut harus diimplementasikan dan dijalankan.
    Kita dapat mengimplementasikan kode untuk mendapatkan waktu saat ini dengan Python. Kita juga perlu menulis kode untuk mengekstrak nama dan argumen dari respons_message untuk mendapatkan hasil akhir.

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
     # Tangani pemanggilan fungsi
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

Panggilan Fungsi adalah inti dari sebagian besar, jika tidak semua, desain penggunaan alat agen, namun mengimplementasikannya dari awal terkadang bisa menantang.
Seperti yang kita pelajari di [Pelajaran 2](../../../02-explore-agentic-frameworks), kerangka kerja agentic menyediakan blok bangunan yang sudah dibuat untuk mengimplementasikan penggunaan alat.
 
## Contoh Penggunaan Alat dengan Kerangka Agentic

Berikut beberapa contoh bagaimana Anda dapat mengimplementasikan Pola Desain Penggunaan Alat menggunakan berbagai kerangka agentic:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> adalah kerangka kerja AI sumber terbuka untuk membangun agen AI. Ia menyederhanakan proses penggunaan panggilan fungsi dengan memungkinkan Anda mendefinisikan alat sebagai fungsi Python dengan dekorator `@tool`. Kerangka ini mengelola komunikasi bolak-balik antara model dan kode Anda. Ia juga menyediakan akses ke alat pra-bangun seperti Pencarian File dan Interpreter Kode melalui `AzureAIProjectAgentProvider`.

Diagram berikut menggambarkan proses pemanggilan fungsi dengan Microsoft Agent Framework:

![function calling](../../../translated_images/id/functioncalling-diagram.a84006fc287f6014.webp)

Dalam Microsoft Agent Framework, alat didefinisikan sebagai fungsi yang didekorasi. Kita dapat mengonversi fungsi `get_current_time` yang kita lihat sebelumnya menjadi alat dengan menggunakan dekorator `@tool`. Kerangka ini akan secara otomatis melakukan serialisasi fungsi dan parameternya, membuat skema untuk dikirimkan ke LLM.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Buat klien
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Buat agen dan jalankan dengan alat tersebut
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> adalah kerangka agentic yang lebih baru yang dirancang untuk memberdayakan pengembang membangun, menerapkan, dan menskalakan agen AI berkualitas tinggi dan dapat diperluas secara aman tanpa perlu mengelola sumber daya komputasi dan penyimpanan yang mendasari. Ini sangat berguna untuk aplikasi perusahaan karena merupakan layanan yang sepenuhnya dikelola dengan keamanan tingkat perusahaan.

Jika dibandingkan dengan pengembangan menggunakan API LLM secara langsung, Azure AI Agent Service menawarkan beberapa keunggulan, antara lain:

- Panggilan alat otomatis – tanpa perlu mengurai panggilan alat, memanggil alat, dan menangani respons; semua ini kini dilakukan di sisi server
- Data dikelola secara aman – alih-alih mengelola status percakapan sendiri, Anda dapat mengandalkan thread untuk menyimpan semua informasi yang Anda butuhkan
- Alat bawaan – Alat yang dapat Anda gunakan untuk berinteraksi dengan sumber data Anda, seperti Bing, Azure AI Search, dan Azure Functions.

Alat yang tersedia di Azure AI Agent Service dapat dibagi menjadi dua kategori:

1. Alat Pengetahuan:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding dengan Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Pencarian File</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Alat Aksi:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Function Calling</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Code Interpreter</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Alat yang didefinisikan OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Layanan Agen memungkinkan kita menggunakan alat-alat ini bersama-sama sebagai `toolset`. Ia juga menggunakan `threads` yang melacak riwayat pesan dari percakapan tertentu.

Bayangkan Anda adalah agen penjualan di perusahaan bernama Contoso. Anda ingin mengembangkan agen percakapan yang dapat menjawab pertanyaan tentang data penjualan Anda.

Gambar berikut menggambarkan bagaimana Anda dapat menggunakan Azure AI Agent Service untuk menganalisis data penjualan Anda:

![Agentic Service In Action](../../../translated_images/id/agent-service-in-action.34fb465c9a84659e.webp)

Untuk menggunakan salah satu alat ini dengan layanan, kita dapat membuat klien dan mendefinisikan alat atau kumpulan alat. Untuk mengimplementasikannya secara praktis, kita dapat menggunakan kode Python berikut. LLM akan dapat melihat toolset dan memutuskan apakah akan menggunakan fungsi yang dibuat pengguna, `fetch_sales_data_using_sqlite_query`, atau Code Interpreter pra-bangun tergantung permintaan pengguna.

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

# Inisialisasi alat Interpreter Kode dan menambahkannya ke toolset.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Pertimbangan khusus apa saja dalam menggunakan Pola Desain Penggunaan Alat untuk membangun agen AI yang dapat dipercaya?

Kekhawatiran umum terkait SQL yang dihasilkan secara dinamis oleh LLM adalah keamanan, khususnya risiko injeksi SQL atau tindakan berbahaya, seperti menghapus atau merusak basis data. Meskipun kekhawatiran ini valid, mereka dapat diatasi secara efektif dengan mengonfigurasi izin akses basis data dengan benar. Untuk sebagian besar basis data, ini melibatkan mengonfigurasi basis data sebagai hanya-baca. Untuk layanan basis data seperti PostgreSQL atau Azure SQL, aplikasi harus diberikan peran hanya-baca (SELECT).

Menjalankan aplikasi di lingkungan yang aman semakin meningkatkan perlindungan. Dalam skenario perusahaan, data biasanya diekstraksi dan ditransformasikan dari sistem operasional ke basis data atau gudang data hanya-baca dengan skema yang mudah digunakan. Pendekatan ini memastikan data aman, dioptimalkan untuk performa dan aksesibilitas, serta aplikasi memiliki akses terbatas hanya-baca.

## Contoh Kode

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Punya Pertanyaan Lebih Lanjut tentang Pola Desain Penggunaan Alat?

Bergabunglah dengan [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) untuk berkenalan dengan pembelajar lain, menghadiri jam kantor, dan mendapatkan jawaban atas pertanyaan tentang Agen AI Anda.

## Sumber Daya Tambahan

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Workshop Layanan Azure AI Agents</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Workshop Multi-Agen Penulis Kreatif Contoso</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Ikhtisar Microsoft Agent Framework</a>

## Pelajaran Sebelumnya

[Memahami Pola Desain Agentic](../03-agentic-design-patterns/README.md)

## Pelajaran Selanjutnya
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya agar terjemahannya akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau interpretasi yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->