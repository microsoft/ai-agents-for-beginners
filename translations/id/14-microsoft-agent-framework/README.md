# Menjelajahi Microsoft Agent Framework

![Agent Framework](../../../translated_images/id/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Pendahuluan

Pelajaran ini akan membahas:

- Memahami Microsoft Agent Framework: Fitur Utama dan Nilai  
- Menjelajahi Konsep Kunci Microsoft Agent Framework
- Pola MAF Lanjutan: Workflows, Middleware, dan Memori

## Tujuan Pembelajaran

Setelah menyelesaikan pelajaran ini, Anda akan tahu cara:

- Membangun Agen AI Siap Produksi menggunakan Microsoft Agent Framework
- Menerapkan fitur inti Microsoft Agent Framework ke kasus penggunaan Agentic Anda
- Menggunakan pola lanjutan termasuk workflows, middleware, dan observabilitas

## Contoh Kode 

Contoh kode untuk [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) dapat ditemukan di repositori ini di bawah file `xx-python-agent-framework` dan `xx-dotnet-agent-framework`.

## Memahami Microsoft Agent Framework

![Framework Intro](../../../translated_images/id/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) adalah framework terpadu Microsoft untuk membangun agen AI. Ini menawarkan fleksibilitas untuk menangani berbagai kasus penggunaan agentik yang terlihat baik di lingkungan produksi maupun penelitian termasuk:

- **Orkestrasi Agen Berurutan** dalam skenario di mana workflow langkah demi langkah dibutuhkan.
- **Orkestrasi Paralel** dalam skenario di mana agen perlu menyelesaikan tugas secara bersamaan.
- **Orkestrasi Obrolan Grup** dalam skenario di mana agen dapat berkolaborasi bersama dalam satu tugas.
- **Orkestrasi Penyerahan** dalam skenario di mana agen menyerahkan tugas satu sama lain saat subtugas selesai.
- **Orkestrasi Magnetik** dalam skenario di mana agen pengelola membuat dan memodifikasi daftar tugas dan menangani koordinasi subagen untuk menyelesaikan tugas tersebut.

Untuk menghadirkan Agen AI dalam Produksi, MAF juga menyertakan fitur untuk:

- **Observabilitas** melalui penggunaan OpenTelemetry di mana setiap tindakan Agen AI termasuk pemanggilan alat, langkah orkestrasi, alur pemikiran, dan pemantauan kinerja melalui dashboard Microsoft Foundry.
- **Keamanan** dengan hosting agen secara native di Microsoft Foundry yang mencakup kontrol keamanan seperti akses berbasis peran, penanganan data pribadi, dan keamanan konten bawaan.
- **Daya Tahan** karena utas dan workflow agen dapat dijeda, dilanjutkan, dan pulih dari kesalahan yang memungkinkan proses berjalan lebih lama.
- **Kontrol** karena workflow human in the loop didukung di mana tugas ditandai sebagai memerlukan persetujuan manusia.

Microsoft Agent Framework juga fokus pada interoperabilitas dengan:

- **Bersifat Cloud-agnostik** - Agen dapat dijalankan dalam container, di on-prem, dan di berbagai cloud yang berbeda.
- **Bersifat Provider-agnostik** - Agen dapat dibuat melalui SDK pilihan Anda termasuk Azure OpenAI dan OpenAI
- **Mengintegrasikan Standar Terbuka** - Agen dapat memanfaatkan protokol seperti Agent-to-Agent (A2A) dan Model Context Protocol (MCP) untuk menemukan dan menggunakan agen serta alat lain.
- **Plugin dan Konektor** - Koneksi dapat dibuat ke layanan data dan memori seperti Microsoft Fabric, SharePoint, Pinecone dan Qdrant.

Mari lihat bagaimana fitur-fitur ini diterapkan ke beberapa konsep inti Microsoft Agent Framework.

## Konsep Kunci Microsoft Agent Framework

### Agen

![Agent Framework](../../../translated_images/id/agent-components.410a06daf87b4fef.webp)

**Membuat Agen**

Pembuatan agen dilakukan dengan mendefinisikan layanan inferensi (Penyedia LLM), 
seperangkat instruksi untuk Agen AI ikuti, dan sebuah `nama` yang ditetapkan:

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

Setiap run agen juga dapat memiliki opsi untuk menyesuaikan parameter seperti `max_tokens` yang digunakan agen, `tools` yang dapat dipanggil agen, dan bahkan `model` itu sendiri yang digunakan agen.

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

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Alat disediakan hanya untuk run ini saja )
```

**Utas Agen**

Utas Agen digunakan untuk menangani percakapan multi-turun. Utas dapat dibuat dengan:

- Menggunakan `get_new_thread()` yang memungkinkan utas disimpan dari waktu ke waktu
- Membuat utas secara otomatis saat menjalankan agen dan hanya membuat utas bertahan selama run saat ini.

Untuk membuat utas, kodenya seperti ini:

```python
# Buat sebuah thread baru.
thread = agent.get_new_thread() # Jalankan agen dengan thread tersebut.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Anda kemudian dapat menyerialkan utas untuk disimpan guna digunakan kemudian:

```python
# Buat thread baru.
thread = agent.get_new_thread() 

# Jalankan agen dengan thread tersebut.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serialisasi thread untuk penyimpanan.

serialized_thread = await thread.serialize() 

# Deserialisasi status thread setelah dimuat dari penyimpanan.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware Agen**

Agen berinteraksi dengan alat dan LLM untuk menyelesaikan tugas pengguna. Dalam skenario tertentu, kita ingin menjalankan atau melacak interaksi di antaranya. Middleware agen memungkinkan kita melakukan ini melalui:

*Middleware Fungsi*

Middleware ini memungkinkan kita menjalankan suatu aksi di antara agen dan fungsi/alat yang akan dipanggilnya. Contoh penggunaannya adalah ketika Anda ingin melakukan pencatatan pada panggilan fungsi.

Dalam kode berikut `next` mendefinisikan apakah middleware selanjutnya atau fungsi aktual harus dipanggil.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Pra-pemrosesan: Catat sebelum eksekusi fungsi
    print(f"[Function] Calling {context.function.name}")

    # Lanjut ke middleware atau eksekusi fungsi berikutnya
    await next(context)

    # Pasca-pemrosesan: Catat setelah eksekusi fungsi
    print(f"[Function] {context.function.name} completed")
```

*Middleware Obrolan*

Middleware ini memungkinkan kita menjalankan atau mencatat aksi di antara agen dan permintaan antara LLM.

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

Seperti yang dibahas di pelajaran `Agentic Memory`, memori adalah elemen penting untuk memungkinkan agen beroperasi dalam konteks yang berbeda. MAF menawarkan beberapa jenis memori yang berbeda:

*Penyimpanan dalam Memori*

Ini adalah memori yang disimpan dalam utas selama runtime aplikasi.

```python
# Buat thread baru.
thread = agent.get_new_thread() # Jalankan agen dengan thread tersebut.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Pesan Persisten*

Memori ini digunakan saat menyimpan riwayat percakapan di berbagai sesi. Ini didefinisikan menggunakan `chat_message_store_factory`:

```python
from agent_framework import ChatMessageStore

# Buat toko pesan kustom
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Memori Dinamis*

Memori ini ditambahkan ke konteks sebelum agen dijalankan. Memori ini bisa disimpan di layanan eksternal seperti mem0:

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

Observabilitas penting untuk membangun sistem agentik yang dapat diandalkan dan mudah dipelihara. MAF terintegrasi dengan OpenTelemetry untuk menyediakan tracing dan metrik demi observabilitas yang lebih baik.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # lakukan sesuatu
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Workflow

MAF menawarkan workflow yang merupakan langkah-langkah yang telah ditetapkan untuk menyelesaikan suatu tugas dan memasukkan agen AI sebagai komponen dalam langkah tersebut.

Workflow dibuat dari berbagai komponen yang memungkinkan alur kontrol yang lebih baik. Workflows juga memungkinkan **orkestrasi multi-agen** dan **checkpointing** untuk menyimpan status workflow.

Komponen inti workflow adalah:

**Executor**

Executor menerima pesan input, melakukan tugas yang ditugaskan, dan kemudian menghasilkan pesan output. Ini menggerakkan workflow maju menuju penyelesaian tugas yang lebih besar. Executor dapat berupa agen AI atau logika khusus.

**Edges**

Edges digunakan untuk mendefinisikan alur pesan dalam workflow. Ini dapat berupa:

*Edges Langsung* - Koneksi satu-ke-satu sederhana antara executor:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Edges Kondisional* - Aktif setelah kondisi tertentu terpenuhi. Misalnya, ketika kamar hotel tidak tersedia, executor dapat menyarankan opsi lain.

*Edges Switch-case* - Mengarahkan pesan ke executor berbeda berdasarkan kondisi yang ditetapkan. Misalnya, jika pelanggan perjalanan memiliki akses prioritas, tugas mereka akan ditangani melalui workflow lain.

*Edges Fan-out* - Mengirim satu pesan ke beberapa target.

*Edges Fan-in* - Mengumpulkan beberapa pesan dari executor berbeda dan mengirim ke satu target.

**Events**

Untuk memberikan observabilitas yang lebih baik ke dalam workflow, MAF menawarkan event bawaan untuk eksekusi antara lain:

- `WorkflowStartedEvent`  - Eksekusi workflow dimulai
- `WorkflowOutputEvent` - Workflow menghasilkan output
- `WorkflowErrorEvent` - Workflow mengalami kesalahan
- `ExecutorInvokeEvent`  - Executor mulai memproses
- `ExecutorCompleteEvent`  -  Executor selesai memproses
- `RequestInfoEvent` - Permintaan dikirim

## Pola MAF Lanjutan

Bagian di atas membahas konsep kunci Microsoft Agent Framework. Saat Anda membangun agen lebih kompleks, berikut adalah beberapa pola lanjutan yang perlu dipertimbangkan:

- **Komposisi Middleware**: Menggabungkan beberapa handler middleware (logging, otentikasi, pembatasan laju) menggunakan middleware fungsi dan obrolan untuk kontrol lebih rinci atas perilaku agen.
- **Checkpointing Workflow**: Gunakan event workflow dan serialisasi untuk menyimpan dan melanjutkan proses agen yang berjalan lama.
- **Pemilihan Alat Dinamis**: Menggabungkan RAG atas deskripsi alat dengan pendaftaran alat MAF untuk hanya menampilkan alat relevan per query.
- **Penyerahan Multi-Agen**: Gunakan edges workflow dan routing kondisional untuk mengatur penyerahan antar agen khusus.

## Hosting Agen LangChain / LangGraph di Microsoft Foundry

Microsoft Agent Framework bersifat **framework-interoperable** — Anda tidak terbatas pada agen yang ditulis dengan MAF. Jika Anda sudah memiliki agen yang dibangun dengan **LangChain** atau **LangGraph**, Anda dapat menjalankannya sebagai **agen yang di-host Microsoft Foundry** sehingga Foundry mengelola runtime, sesi, scaling, identitas, dan titik akhir protokol untuk Anda, sementara logika agen Anda tetap di LangGraph.

Ini dilakukan dengan paket `langchain_azure_ai.agents.hosting`, yang mengekspos grafik LangGraph yang sudah dikompilasi melalui protokol yang sama yang digunakan agen Foundry.

**1. Pasang extra hosting:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Extra `hosting` ini memasang perpustakaan protokol Foundry: `azure-ai-agentserver-responses` (endpoint `/responses` kompatibel OpenAI) dan `azure-ai-agentserver-invocations` (endpoint `/invocations` generik).

**2. Pilih protokol hosting:**

| Protokol | Kelas Host | Endpoint | Digunakan saat |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Ingin chat kompatibel OpenAI, streaming, riwayat respons, dan threading percakapan — default yang direkomendasikan untuk agen percakapan. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Membutuhkan bentuk JSON khusus, endpoint gaya webhook, atau pemrosesan non-percakapan. |

Karena **Responses API adalah API utama untuk pengembangan agen gaya Foundry**, mulai dengan `ResponsesHostServer` untuk kebanyakan agen.

**3. Konfigurasi variabel lingkungan** (`az login` terlebih dahulu agar `DefaultAzureCredential` bisa mengautentikasi):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-4.1"
```

Saat agen nanti dijalankan sebagai agen yang di-host di Foundry, platform secara otomatis menyuntikkan `FOUNDRY_PROJECT_ENDPOINT`.

**4. Mengekspos agen LangGraph melalui protokol Responses:**

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
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-4.1")
    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    # ChatOpenAI di sini menargetkan endpoint Foundry proyek yang kompatibel dengan OpenAI (Responses).
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

**Perilaku kunci:**

- **Percakapan**: Klien melanjutkan percakapan dengan melewatkan `previous_response_id` atau ID `conversation`. Jika grafik Anda dikompilasi dengan checkpointer LangGraph, Foundry mengaitkan status percakapan dengan checkpoint (gunakan checkpointer tahan lama di produksi; `MemorySaver` cukup untuk pengujian lokal).
- **Human-in-the-loop**: Jika grafik Anda menggunakan `interrupt()` dari LangGraph, `ResponsesHostServer` menampilkan interrupt tertunda sebagai item `function_call` / `mcp_approval_request` Responses, dan klien melanjutkan dengan `function_call_output` / `mcp_approval_response` yang cocok.
- **Deploy ke Foundry**: Gunakan Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokal, membutuhkan Docker), lalu `azd provision` dan `azd deploy`. Deploy agen yang di-host membutuhkan peran **Foundry Project Manager**.

Versi yang bisa dijalankan dari contoh ini ada di [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Untuk panduan lengkap (protokol Invocations, skema permintaan khusus, dan pemecahan masalah), lihat [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Contoh Kode 

Contoh kode untuk Microsoft Agent Framework dapat ditemukan di repositori ini di bawah file `xx-python-agent-framework` dan `xx-dotnet-agent-framework`.

## Punya Pertanyaan Lebih Lanjut Tentang Microsoft Agent Framework?

Bergabunglah dengan [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) untuk bertemu dengan pelajar lain, menghadiri jam kantor dan mendapatkan jawaban atas pertanyaan AI Agents Anda.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->