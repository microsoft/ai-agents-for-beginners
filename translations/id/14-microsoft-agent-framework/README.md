# Menjelajahi Microsoft Agent Framework

![Agent Framework](../../../translated_images/id/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Pendahuluan

Pelajaran ini akan membahas:

- Memahami Microsoft Agent Framework: Fitur Utama dan Nilainya  
- Menjelajahi Konsep Utama Microsoft Agent Framework
- Pola Lanjutan MAF: Alur Kerja, Middleware, dan Memori

## Tujuan Pembelajaran

Setelah menyelesaikan pelajaran ini, Anda akan mengetahui cara:

- Membangun Agen AI Siap Produksi menggunakan Microsoft Agent Framework
- Menerapkan fitur inti Microsoft Agent Framework ke Kasus Penggunaan Agent Anda
- Menggunakan pola lanjutan termasuk alur kerja, middleware, dan observabilitas

## Contoh Kode 

Contoh kode untuk [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) dapat ditemukan di repositori ini di bawah file `xx-python-agent-framework` dan `xx-dotnet-agent-framework`.

## Memahami Microsoft Agent Framework

![Framework Intro](../../../translated_images/id/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) adalah kerangka kerja terpadu Microsoft untuk membangun agen AI. Ia menawarkan fleksibilitas untuk menangani berbagai kasus penggunaan agentik yang terlihat di lingkungan produksi dan penelitian termasuk:

- **Orkestrasi Agen Berurutan** dalam skenario di mana alur kerja langkah-demi-langkah diperlukan.
- **Orkestrasi Konkuren** dalam skenario di mana agen harus menyelesaikan tugas secara bersamaan.
- **Orkestrasi Obrolan Grup** dalam skenario di mana agen dapat berkolaborasi bersama pada satu tugas.
- **Orkestrasi Penyerahan** dalam skenario di mana agen menyerahkan tugas satu sama lain saat subtugas selesai.
- **Orkestrasi Magnetik** dalam skenario di mana agen manajer membuat dan memodifikasi daftar tugas serta mengelola koordinasi subagen untuk menyelesaikan tugas.

Untuk menyajikan Agen AI di Produksi, MAF juga menyertakan fitur untuk:

- **Observabilitas** melalui penggunaan OpenTelemetry di mana setiap aksi Agen AI termasuk pemanggilan alat, langkah orkestrasi, alur penalaran, dan pemantauan kinerja melalui dasbor Microsoft Foundry.
- **Keamanan** dengan hosting agen secara native di Microsoft Foundry yang mencakup kontrol keamanan seperti akses berbasis peran, penanganan data pribadi, dan keamanan konten bawaan.
- **Daya Tahan** karena thread dan alur kerja Agen dapat dijeda, dilanjutkan, dan pulih dari kesalahan yang memungkinkan proses berjalan lebih lama.
- **Kontrol** karena alur kerja human in the loop didukung di mana tugas ditandai memerlukan persetujuan manusia.

Microsoft Agent Framework juga fokus pada interoperabilitas dengan cara:

- **Bersifat Cloud-agnostik** - Agen dapat berjalan di kontainer, on-premise, dan di berbagai cloud yang berbeda.
- **Bersifat Provider-agnostik** - Agen dapat dibuat melalui SDK favorit Anda termasuk Azure OpenAI dan OpenAI.
- **Mengintegrasikan Standar Terbuka** - Agen dapat menggunakan protokol seperti Agent-to-Agent (A2A) dan Model Context Protocol (MCP) untuk menemukan dan menggunakan agen serta alat lain.
- **Plugin dan Konektor** - Koneksi dapat dibuat ke layanan data dan memori seperti Microsoft Fabric, SharePoint, Pinecone, dan Qdrant.

Mari kita lihat bagaimana fitur-fitur ini diterapkan ke beberapa konsep inti Microsoft Agent Framework.

## Konsep Utama Microsoft Agent Framework

### Agen

![Agent Framework](../../../translated_images/id/agent-components.410a06daf87b4fef.webp)

**Membuat Agen**

Pembuatan agen dilakukan dengan mendefinisikan layanan inferensi (Penyedia LLM),  
seperangkat instruksi yang harus diikuti Agen AI, dan `name` yang diberikan:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Di atas menggunakan `Azure OpenAI` tetapi agen dapat dibuat menggunakan berbagai layanan termasuk `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

API OpenAI `Responses`, `ChatCompletion`

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

atau [MiniMax](https://platform.minimaxi.com/), yang menyediakan API kompatibel OpenAI dengan jendela konteks besar (hingga 204K token):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

atau agen jarak jauh menggunakan protokol A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Menjalankan Agen**

Agen dijalankan menggunakan metode `.run` atau `.run_stream` untuk respons non-streaming atau streaming.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Setiap jalannya agen juga bisa memiliki opsi untuk menyesuaikan parameter seperti `max_tokens` yang digunakan agen, `tools` yang bisa dipanggil agen, dan bahkan `model` yang digunakan agen itu sendiri.

Ini berguna dalam kasus di mana model atau alat tertentu diperlukan untuk menyelesaikan tugas pengguna.

**Alat**

Alat dapat didefinisikan baik saat mendefinisikan agen:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Saat membuat ChatAgent secara langsung

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

dan juga saat menjalankan agen:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Alat yang disediakan hanya untuk penggunaan kali ini )
```

**Thread Agen**

Thread Agen digunakan untuk menangani percakapan multi-giliran. Thread dapat dibuat dengan:

- Menggunakan `get_new_thread()` yang memungkinkan thread disimpan dari waktu ke waktu
- Membuat thread secara otomatis saat menjalankan agen dan hanya mempertahankan thread selama jalannya saat ini.

Untuk membuat thread, kodenya seperti ini:

```python
# Buat thread baru.
thread = agent.get_new_thread() # Jalankan agen dengan thread tersebut.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Kemudian Anda bisa serialisasi thread untuk disimpan guna penggunaan nanti:

```python
# Buat thread baru.
thread = agent.get_new_thread() 

# Jalankan agen dengan thread.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serialisasi thread untuk penyimpanan.

serialized_thread = await thread.serialize() 

# Deserialisasi status thread setelah memuat dari penyimpanan.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware Agen**

Agen berinteraksi dengan alat dan LLM untuk menyelesaikan tugas pengguna. Dalam beberapa situasi, kita ingin menjalankan atau melacak di antara interaksi ini. Middleware agen memungkinkan kita melakukan ini melalui:

*Middleware Fungsi*

Middleware ini memungkinkan kita mengeksekusi tindakan antara agen dan fungsi/alat yang akan dipanggilnya. Contohnya adalah saat Anda ingin melakukan pencatatan pada panggilan fungsi.

Dalam kode di bawah `next` mendefinisikan apakah middleware berikutnya atau fungsi aktual harus dipanggil.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Pra-pemrosesan: Catat sebelum eksekusi fungsi
    print(f"[Function] Calling {context.function.name}")

    # Lanjutkan ke middleware berikutnya atau eksekusi fungsi
    await next(context)

    # Pasca-pemrosesan: Catat setelah eksekusi fungsi
    print(f"[Function] {context.function.name} completed")
```

*Middleware Obrolan*

Middleware ini memungkinkan kita mengeksekusi atau mencatat tindakan antara agen dan permintaan antar LLM.

Ini berisi informasi penting seperti `messages` yang dikirim ke layanan AI.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Pra-pemrosesan: Catat sebelum panggilan AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Lanjutkan ke middleware atau layanan AI berikutnya
    await next(context)

    # Pasca-pemrosesan: Catat setelah respons AI
    print("[Chat] AI response received")

```

**Memori Agen**

Seperti yang dibahas dalam pelajaran `Agentic Memory`, memori adalah elemen penting agar agen dapat beroperasi dalam konteks yang berbeda. MAF menawarkan beberapa jenis memori:

*Penyimpanan Dalam Memori*

Ini adalah memori yang disimpan di thread selama runtime aplikasi.

```python
# Buat thread baru.
thread = agent.get_new_thread() # Jalankan agen dengan thread tersebut.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Pesan Persisten*

Memori ini digunakan saat menyimpan riwayat percakapan di berbagai sesi. Ditetapkan menggunakan `chat_message_store_factory` :

```python
from agent_framework import ChatMessageStore

# Membuat penyimpanan pesan khusus
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Memori Dinamis*

Memori ini ditambahkan ke konteks sebelum agen dijalankan. Memori ini dapat disimpan di layanan eksternal seperti mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Menggunakan Mem0 untuk kemampuan memori tingkat lanjut
memory_provider = Mem0Provider(
    api_key="your-mem0-api-key",
    user_id="user_123",
    application_id="my_app"
)

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a helpful assistant with memory.",
    context_providers=memory_provider
)

```

**Observabilitas Agen**

Observabilitas penting untuk membangun sistem agentik yang andal dan mudah dipelihara. MAF terintegrasi dengan OpenTelemetry untuk menyediakan trace dan meter guna observabilitas yang lebih baik.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # melakukan sesuatu
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Alur Kerja

MAF menawarkan alur kerja yang merupakan langkah-langkah yang telah ditentukan untuk menyelesaikan sebuah tugas dan memasukkan agen AI sebagai komponen dalam langkah-langkah tersebut.

Alur kerja terdiri dari berbagai komponen yang memungkinkan alur kontrol yang lebih baik. Alur kerja juga memungkinkan **orkestrasi multi-agen** dan **checkpointing** untuk menyimpan status alur kerja.

Komponen inti dari alur kerja adalah:

**Eksekutor**

Eksekutor menerima pesan input, melaksanakan tugas yang diberikan, lalu menghasilkan pesan output. Ini memajukan alur kerja menuju penyelesaian tugas besar. Eksekutor bisa berupa agen AI atau logika kustom.

**Edges (Sisi)**

Edges digunakan untuk mendefinisikan aliran pesan dalam alur kerja. Ini bisa berupa:

*Edges Langsung* - Koneksi satu-ke-satu sederhana antara eksekutor:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Edges Bersyarat* - Diaktifkan setelah kondisi tertentu terpenuhi. Misalnya, saat kamar hotel tidak tersedia, eksekutor bisa menyarankan opsi lain.

*Edges Switch-case* - Mengarahkan pesan ke eksekutor berbeda berdasarkan kondisi yang ditentukan. Misalnya, jika pelanggan perjalanan memiliki akses prioritas dan tugas mereka akan ditangani melalui alur kerja lain.

*Edges Fan-out* - Mengirim satu pesan ke beberapa target.

*Edges Fan-in* - Mengumpulkan beberapa pesan dari eksekutor berbeda dan mengirim ke satu target.

**Events (Peristiwa)**

Untuk memberikan observabilitas yang lebih baik pada alur kerja, MAF menyediakan peristiwa bawaan untuk eksekusi termasuk:

- `WorkflowStartedEvent`  - Mulai eksekusi alur kerja
- `WorkflowOutputEvent` - Alur kerja menghasilkan output
- `WorkflowErrorEvent` - Alur kerja mengalami kesalahan
- `ExecutorInvokeEvent`  - Eksekutor mulai memproses
- `ExecutorCompleteEvent`  -  Eksekutor selesai memproses
- `RequestInfoEvent` - Permintaan dikeluarkan

## Pola Lanjutan MAF

Bagian-bagian di atas membahas konsep utama Microsoft Agent Framework. Saat Anda membangun agen yang lebih kompleks, berikut beberapa pola lanjutan yang dapat dipertimbangkan:

- **Komposisi Middleware**: Rangkai beberapa handler middleware (logging, otentikasi, pembatasan laju) menggunakan middleware fungsi dan obrolan untuk kontrol yang lebih halus terhadap perilaku agen.
- **Checkpointing Alur Kerja**: Gunakan peristiwa alur kerja dan serialisasi untuk menyimpan dan melanjutkan proses agen yang berjalan lama.
- **Pemilihan Alat Dinamis**: Gabungkan RAG atas deskripsi alat dengan pendaftaran alat MAF untuk menampilkan hanya alat yang relevan per kueri.
- **Penyerahan Multi-Agen**: Gunakan sisi alur kerja dan pengalihan bersyarat untuk mengorkestrasi penyerahan antar agen khusus.

## Hosting Agen LangChain / LangGraph di Microsoft Foundry

Microsoft Agent Framework adalah **framework-interoperable** — Anda tidak terbatas pada agen yang ditulis dengan MAF. Jika Anda sudah memiliki agen yang dibangun dengan **LangChain** atau **LangGraph**, Anda dapat menjalankannya sebagai **agen hosting Microsoft Foundry** sehingga Foundry mengelola runtime, sesi, skalabilitas, identitas, dan endpoint protokol untuk Anda, sementara logika agen Anda tetap di LangGraph.

Ini dilakukan dengan paket `langchain_azure_ai.agents.hosting`, yang mengekspos grafik LangGraph terkompilasi melalui protokol yang sama yang digunakan agen hosting Foundry.

**1. Instal hosting extra:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Extra `hosting` menginstal pustaka protokol Foundry: `azure-ai-agentserver-responses` (endpoint `/responses` kompatibel OpenAI) dan `azure-ai-agentserver-invocations` (endpoint `/invocations` generik).

**2. Pilih protokol hosting:**

| Protocol | Kelas Host | Endpoint | Gunakan ketika |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Anda ingin obrolan, streaming, riwayat respons, dan threading percakapan yang kompatibel OpenAI — default yang direkomendasikan untuk agen percakapan. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Anda memerlukan bentuk JSON khusus, endpoint gaya webhook, atau pemrosesan non-percakapan. |

Karena **Responses API adalah API utama untuk pengembangan agen di Foundry**, mulai dengan `ResponsesHostServer` untuk sebagian besar agen.

**3. Konfigurasikan variabel lingkungan** (`az login` terlebih dahulu agar `DefaultAzureCredential` dapat mengautentikasi):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Saat agen nanti berjalan sebagai agen hosting di Foundry, platform secara otomatis menyuntikkan `FOUNDRY_PROJECT_ENDPOINT`.

**4. Ekspos agen LangGraph melalui protokol Responses:**

```python
import os

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_azure_ai.agents.hosting import ResponsesHostServer

_AZURE_AI_SCOPE = "https://ai.azure.com/.default"


def build_chat_model() -> ChatOpenAI:
    project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"].rstrip("/")
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-5-mini")
    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    # ChatOpenAI di sini menargetkan endpoint OpenAI-kompatibel (Responses) dari proyek Foundry.
    return ChatOpenAI(
        model=deployment,
        base_url=str(openai_client.base_url),
        api_key=token_provider,
    )


def main() -> None:
    graph = create_agent(build_chat_model(), tools=[])
    port = int(os.environ.get("PORT", "8088"))
    ResponsesHostServer(graph).run(port=port)


if __name__ == "__main__":
    main()
```

Jalankan secara lokal dengan `python main.py`, lalu kirim permintaan Responses ke `http://localhost:8088/responses`.

**Perilaku utama:**

- **Percakapan**: Klien melanjutkan percakapan dengan meneruskan `previous_response_id` atau ID `conversation`. Jika grafik Anda dikompilasi dengan checkpointer LangGraph, Foundry mengaitkan status percakapan ke checkpoint (gunakan checkpointer tahan lama dalam produksi; `MemorySaver` cukup untuk pengujian lokal).
- **Human-in-the-loop**: Jika grafik Anda menggunakan LangGraph `interrupt()`, `ResponsesHostServer` menampilkan interupsi tertunda sebagai item `function_call` / `mcp_approval_request` Responses, dan klien melanjutkan dengan `function_call_output` / `mcp_approval_response` yang cocok.
- **Deploy ke Foundry**: Gunakan Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokal, memerlukan Docker), lalu `azd provision` dan `azd deploy`. Deploy agen hosting memerlukan peran **Foundry Project Manager**.

Versi contoh yang bisa dijalankan ada di [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Untuk walkthrough lengkap (protokol Invocations, skema permintaan kustom, dan pemecahan masalah), lihat [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Contoh Kode 

Contoh kode untuk Microsoft Agent Framework dapat ditemukan di repositori ini di bawah file `xx-python-agent-framework` dan `xx-dotnet-agent-framework`.

## Ada Pertanyaan Lebih Lanjut Tentang Microsoft Agent Framework?

Bergabunglah dengan [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) untuk bertemu dengan pelajar lain, menghadiri jam kantor, dan mendapatkan jawaban atas pertanyaan AI Agents Anda.
## Pelajaran Sebelumnya

[Memori untuk AI Agents](../13-agent-memory/README.md)

## Pelajaran Berikutnya

[Membangun Agen Pengguna Komputer (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->