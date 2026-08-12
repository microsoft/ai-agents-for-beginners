[![Cara Mereka Bentuk Ejen AI yang Baik](../../../translated_images/ms/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Klik gambar di atas untuk menonton video pelajaran ini)_

# Corak Reka Bentuk Penggunaan Alat

Alat adalah menarik kerana ia membolehkan ejen AI mempunyai julat keupayaan yang lebih luas. Daripada ejen itu hanya mempunyai set tindakan terhad yang boleh dilaksanakan, dengan menambah alat, ejen kini boleh melaksanakan pelbagai tindakan. Dalam bab ini, kita akan melihat Corak Reka Bentuk Penggunaan Alat, yang menerangkan bagaimana ejen AI boleh menggunakan alat tertentu untuk mencapai matlamat mereka.

## Pengenalan

Dalam pelajaran ini, kita ingin menjawab soalan-soalan berikut:

- Apakah corak reka bentuk penggunaan alat?
- Apakah kes penggunaan yang boleh ia diterapkan?
- Apakah elemen/blok binaan yang diperlukan untuk melaksana corak reka bentuk ini?
- Apakah pertimbangan khas bagi menggunakan Corak Reka Bentuk Penggunaan Alat untuk membina ejen AI yang boleh dipercayai?

## Matlamat Pembelajaran

Selepas menamatkan pelajaran ini, anda akan dapat:

- Mentakrifkan Corak Reka Bentuk Penggunaan Alat dan tujuan penggunaannya.
- Mengenal pasti kes penggunaan di mana Corak Reka Bentuk Penggunaan Alat boleh diterapkan.
- Memahami elemen utama yang diperlukan untuk melaksanakan corak reka bentuk ini.
- Mengenal pasti pertimbangan untuk memastikan kebolehpercayaan dalam ejen AI yang menggunakan corak reka bentuk ini.

## Apakah itu Corak Reka Bentuk Penggunaan Alat?

**Corak Reka Bentuk Penggunaan Alat** memberi fokus kepada memberikan model bahasa besar (LLM) kebolehan untuk berinteraksi dengan alat luaran bagi mencapai matlamat khusus. Alat adalah kod yang boleh dilaksanakan oleh ejen untuk melakukan tindakan. Alat boleh menjadi fungsi mudah seperti kalkulator, atau panggilan API kepada perkhidmatan pihak ketiga seperti semakan harga saham atau ramalan cuaca. Dalam konteks ejen AI, alat direka untuk dilaksanakan oleh ejen sebagai tindak balas kepada **panggilan fungsi yang dijana model**.

## Apakah kes penggunaan yang boleh ia diterapkan?

Ejen AI boleh menggunakan alat untuk menyelesaikan tugas kompleks, mendapatkan maklumat, atau membuat keputusan. Corak reka bentuk penggunaan alat sering digunakan dalam senario yang memerlukan interaksi dinamik dengan sistem luaran, seperti pangkalan data, perkhidmatan web, atau penafsir kod. Keupayaan ini berguna untuk beberapa kes penggunaan yang berbeza termasuk:

- **Pengambilan Maklumat Dinamik:** Ejen boleh membuat pertanyaan ke API luaran atau pangkalan data untuk mendapatkan data terkini (contoh: membuat pertanyaan ke pangkalan data SQLite untuk analisis data, mendapatkan harga saham atau maklumat cuaca).
- **Pelaksanaan dan Tafsiran Kod:** Ejen boleh melaksanakan kod atau skrip untuk menyelesaikan masalah matematik, menjana laporan, atau melakukan simulasi.
- **Automasi Aliran Kerja:** Mengautomasikan tugas berulang atau aliran kerja berbilang langkah dengan mengintegrasi alat seperti penjadual tugas, perkhidmatan emel, atau saluran data.
- **Sokongan Pelanggan:** Ejen boleh berinteraksi dengan sistem CRM, platform tiket, atau pangkalan pengetahuan untuk menyelesaikan pertanyaan pengguna.
- **Penciptaan dan Penyuntingan Kandungan:** Ejen boleh menggunakan alat seperti pemeriksa tatabahasa, peringkas teks, atau penilai keselamatan kandungan untuk membantu dalam tugasan penciptaan kandungan.

## Apakah elemen/blok binaan yang diperlukan untuk melaksanakan corak reka bentuk penggunaan alat?

Blok binaan ini membolehkan ejen AI melaksanakan pelbagai tugasan. Mari kita lihat elemen utama yang diperlukan untuk melaksanakan Corak Reka Bentuk Penggunaan Alat:

- **Skema Fungsi/Alat**: Definisi terperinci alat yang tersedia, termasuk nama fungsi, tujuan, parameter diperlukan, dan output yang dijangka. Skema ini membolehkan LLM memahami alat apa yang tersedia dan bagaimana membina permintaan yang sah.

- **Logik Pelaksanaan Fungsi**: Mengawal bagaimana dan bila alat dipanggil berdasarkan niat pengguna dan konteks perbualan. Ini mungkin termasuk modul perancang, mekanisme perutean, atau aliran bersyarat yang menentukan penggunaan alat secara dinamik.

- **Sistem Pengendalian Mesej**: Komponen yang mengurus aliran perbualan antara input pengguna, respons LLM, panggilan alat, dan output alat.

- **Rangka Kerja Integrasi Alat**: Infrastruktur yang menghubungkan ejen dengan pelbagai alat, sama ada fungsi mudah atau perkhidmatan luaran yang kompleks.

- **Pengendalian Ralat & Pengesahan**: Mekanisme untuk mengendalikan kegagalan dalam pelaksanaan alat, mengesahkan parameter, dan menguruskan respons yang tidak dijangka.

- **Pengurusan Keadaan**: Mengesan konteks perbualan, interaksi alat sebelum ini, dan data berterusan untuk memastikan konsistensi dalam interaksi berbilang giliran.

Seterusnya, mari kita lihat secara lebih terperinci mengenai Panggilan Fungsi/Alat.
 
### Panggilan Fungsi/Alat

Panggilan fungsi adalah cara utama kita membolehkan Model Bahasa Besar (LLM) berinteraksi dengan alat. Anda sering akan melihat 'Fungsi' dan 'Alat' digunakan secara bergantian kerana 'fungsi' (blok kod yang boleh digunakan semula) adalah 'alat' yang digunakan oleh ejen untuk melaksanakan tugasan. Untuk kod fungsi dilaksanakan, LLM mesti membandingkan permintaan pengguna dengan deskripsi fungsi. Untuk ini, satu skema yang mengandungi deskripsi semua fungsi yang tersedia dihantar kepada LLM. LLM kemudiannya memilih fungsi yang paling sesuai untuk tugasan itu dan mengembalikan nama serta argumennya. Fungsi yang dipilih dilaksanakan, responsnya dihantar kembali kepada LLM, yang menggunakan maklumat itu untuk menjawab permintaan pengguna.

Bagi pembangun untuk melaksanakan panggilan fungsi untuk ejen, anda memerlukan:

1. Model LLM yang menyokong panggilan fungsi
2. Skema yang mengandungi deskripsi fungsi
3. Kod untuk setiap fungsi yang diterangkan

Mari gunakan contoh mendapatkan masa semasa di sebuah bandar untuk menggambarkan:

1. **Inisialisasi LLM yang menyokong panggilan fungsi:**

    Tidak semua model menyokong panggilan fungsi, jadi penting untuk memeriksa bahawa LLM yang anda gunakan menyokongnya.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> menyokong panggilan fungsi. Kita boleh mula dengan memulakan pelanggan OpenAI terhadap Azure OpenAI **Responses API** (endpoint stabil `/openai/v1/` — tiada `api_version` diperlukan). 

    ```python
    # Inisialisasi klien OpenAI untuk Azure OpenAI (API Respons, titik akhir v1)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Cipta Skema Fungsi**:

    Seterusnya kita akan mentakrifkan skema JSON yang mengandungi nama fungsi, penerangan tentang apa yang dilakukan oleh fungsi, dan nama serta penerangan parameter fungsi.
    Kita kemudian akan mengambil skema ini dan menghantarnya kepada pelanggan yang dicipta sebelum ini, bersama dengan permintaan pengguna untuk mendapatkan masa di San Francisco. Apa yang penting untuk dicatat ialah **panggilan alat** yang dikembalikan, **bukan** jawapan akhir kepada soalan. Seperti yang disebutkan sebelum ini, LLM mengembalikan nama fungsi yang dipilihnya untuk tugasan itu, dan argumen yang akan diserahkan kepadanya.

    ```python
    # Huraian fungsi untuk model membaca (format alat rata API Respons)
    tools = [
        {
            "type": "function",
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
    ]
    ```
   
    ```python
  
    # Mesej pengguna awal
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # Panggilan API pertama: Minta model menggunakan fungsi itu
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # API Respon mengembalikan panggilan alat sebagai item function_call dalam response.output.
    # Tambahkan mereka ke perbualan supaya model mempunyai konteks penuh pada giliran seterusnya.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **Kod fungsi yang diperlukan untuk melaksanakan tugasan:**

    Setelah LLM memilih fungsi yang perlu dijalankan, kod yang melaksanakan tugasan itu perlu diimplementasikan dan dijalankan.
    Kita boleh melaksanakan kod untuk mendapatkan masa semasa dalam Python. Kita juga perlu menulis kod untuk mengekstrak nama dan argumen dari response_message untuk mendapatkan keputusan akhir.

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
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # Pulangkan hasil alat sebagai item function_call_output
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # Panggilan API kedua: Dapatkan respons akhir dari model
    final_response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        store=False,
    )

    return final_response.output_text
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

Panggilan Fungsi adalah teras kepada kebanyakan, jika tidak semua, reka bentuk penggunaan alat ejen, namun mengimplementasikannya dari awal kadangkala boleh menjadi mencabar.
Seperti yang kita pelajari dalam [Pelajaran 2](../../../02-explore-agentic-frameworks), rangka kerja ejenik menyediakan blok binaan siap untuk melaksanakan penggunaan alat.
 
## Contoh Penggunaan Alat dengan Rangka Kerja Agenik

Berikut adalah beberapa contoh bagaimana anda boleh melaksanakan Corak Reka Bentuk Penggunaan Alat menggunakan pelbagai rangka kerja ejenik:

### Rangka Kerja Ejen Microsoft

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Rangka Kerja Ejen Microsoft</a> adalah rangka kerja AI sumber terbuka untuk membina ejen AI. Ia memudahkan proses penggunaan panggilan fungsi dengan membenarkan anda mentakrifkan alat sebagai fungsi Python dengan dekorator `@tool`. Rangka kerja ini mengendalikan komunikasi dua hala antara model dan kod anda. Ia juga menyediakan akses ke alat siap seperti Carian Fail dan Penafsir Kod melalui `FoundryChatClient`.

Rajah berikut menerangkan proses panggilan fungsi dengan Rangka Kerja Ejen Microsoft:

![function calling](../../../translated_images/ms/functioncalling-diagram.a84006fc287f6014.webp)

Dalam Rangka Kerja Ejen Microsoft, alat didefinisikan sebagai fungsi yang dihiasi. Kita boleh menukar fungsi `get_current_time` yang dilihat tadi menjadi alat dengan menggunakan dekorator `@tool`. Rangka kerja akan secara automatik mensiri fungsi dan parameternya, mencipta skema untuk dihantar kepada LLM.

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Cipta klien
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Cipta agen dan jalankan dengan alat tersebut
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Perkhidmatan Ejen Microsoft Foundry

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Perkhidmatan Ejen Microsoft Foundry</a> adalah rangka kerja ejenik yang lebih baru yang direka untuk memperkasakan pembangun membina, menyebar dan mengembangkan ejen AI yang bermutu tinggi dan boleh dikembangkan dengan selamat tanpa perlu mengurus sumber pengkomputeran dan penyimpanan asas. Ia amat berguna untuk aplikasi perusahaan kerana ia adalah perkhidmatan yang dikendalikan sepenuhnya dengan keselamatan tahap perusahaan.

Jika dibandingkan dengan membangunkan terus dengan API LLM, Perkhidmatan Ejen Microsoft Foundry menyediakan beberapa kelebihan, termasuk:

- Panggilan alat automatik – tiada perlu mengurai panggilan alat, melaksanakan alat, dan mengendalikan respons; semua ini kini dilakukan di sisi pelayan
- Data yang diurus dengan selamat – bukannya mengurus keadaan perbualan sendiri, anda boleh bergantung pada threads untuk menyimpan segala maklumat yang diperlukan
- Alat sedia guna – Alat yang anda boleh gunakan untuk berinteraksi dengan sumber data anda, seperti Bing, Azure AI Search, dan Azure Functions.

Alat yang tersedia dalam Perkhidmatan Ejen Microsoft Foundry boleh dibahagikan kepada dua kategori:

1. Alat Pengetahuan:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Pengukuhan dengan Carian Bing</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Carian Fail</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Carian Azure AI</a>

2. Alat Tindakan:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Panggilan Fungsi</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Penafsir Kod</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Alat yang ditakrif OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Perkhidmatan Ejen membolehkan kita menggunakan alat ini bersama sebagai `toolset`. Ia juga menggunakan `threads` yang menyimpan sejarah mesej dari perbualan tertentu.

Bayangkan anda adalah ejen jualan di sebuah syarikat bernama Contoso. Anda ingin membina ejen perbualan yang boleh menjawab soalan tentang data jualan anda.

Imej berikut menerangkan bagaimana anda boleh menggunakan Perkhidmatan Ejen Microsoft Foundry untuk menganalisis data jualan anda:

![Agentic Service In Action](../../../translated_images/ms/agent-service-in-action.34fb465c9a84659e.webp)

Untuk menggunakan mana-mana alat ini dengan perkhidmatan, kita boleh mencipta pelanggan dan mentakrifkan alat atau toolset. Untuk melaksanakannya secara praktikal, kita boleh menggunakan kod Python berikut. LLM akan boleh melihat toolset dan memutuskan sama ada menggunakan fungsi yang dicipta pengguna, `fetch_sales_data_using_sqlite_query`, atau Penafsir Kod sedia ada bergantung pada permintaan pengguna.

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

# Memulakan set alat
toolset = ToolSet()

# Memulakan agen pemanggil fungsi dengan fungsi fetch_sales_data_using_sqlite_query dan menambahkannya ke dalam set alat
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Memulakan alat Penafsir Kod dan menambahkannya ke dalam set alat.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Apakah pertimbangan khas bagi menggunakan Corak Reka Bentuk Penggunaan Alat untuk membina ejen AI yang boleh dipercayai?

Kebimbangan biasa dengan SQL yang dijana secara dinamik oleh LLM ialah keselamatan, terutamanya risiko suntikan SQL atau tindakan berniat jahat, seperti memadam atau mengubah pangkalan data. Walaupun kebimbangan ini sah, ia boleh diatasi dengan berkesan melalui konfigurasi kebenaran akses pangkalan data yang betul. Bagi kebanyakan pangkalan data, ini melibatkan konfigurasi pangkalan data sebagai baca sahaja. Bagi perkhidmatan pangkalan data seperti PostgreSQL atau Azure SQL, aplikasi harus diberikan peranan baca sahaja (SELECT).

Menjalankan aplikasi dalam persekitaran yang selamat menambahbaik perlindungan lagi. Dalam senario perusahaan, data biasanya diekstrak dan diubah dari sistem operasi ke dalam pangkalan data baca sahaja atau gudang data dengan skema mesra pengguna. Pendekatan ini memastikan bahawa data adalah selamat, dioptimumkan untuk prestasi dan kebolehaksesan, dan aplikasi mempunyai akses terhad yang hanya boleh membaca.

## Kod Contoh

- Python: [Rangka Kerja Ejen](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Rangka Kerja Ejen](./code_samples/04-dotnet-agent-framework.md)

## Ada Soalan Lain mengenai Corak Reka Bentuk Penggunaan Alat?

Sertailah [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) untuk bertemu dengan pelajar lain, menghadiri sesi pejabat dan mendapatkan jawapan bagi soalan tentang Ejen AI anda.

## Sumber Tambahan

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Bengkel Perkhidmatan Ejen Azure AI</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Bengkel Multi-Ejen Contoso Creative Writer</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Gambaran Keseluruhan Rangka Kerja Ejen Microsoft</a>


## Ujian Asas Ejen Ini (Pilihan)

Selepas anda belajar untuk menyebarkan ejen dalam [Lesson 16](../16-deploying-scalable-agents/README.md), anda boleh membuat ujian asas untuk `TravelToolAgent` dalam pelajaran ini (adakah ia masih memanggil alat dan menjawab?) dengan menggunakan [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json). Lihat [`tests/README.md`](../tests/README.md) untuk cara menjalankannya.

## Pelajaran Sebelumnya

[Memahami Corak Reka Bentuk Agen](../03-agentic-design-patterns/README.md)

## Pelajaran Seterusnya

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->