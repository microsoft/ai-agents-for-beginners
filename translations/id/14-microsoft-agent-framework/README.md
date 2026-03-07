# Menjelajahi Microsoft Agent Framework

![Agent Framework](../../../translated_images/id/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Pendahuluan

Pelajaran ini akan membahas:

- Memahami Microsoft Agent Framework: Fitur Utama dan Nilainya  
- Menjelajahi Konsep Utama Microsoft Agent Framework
- Pola MAF Lanjutan: Alur Kerja, Middleware, dan Memori

## Tujuan Pembelajaran

Setelah menyelesaikan pelajaran ini, Anda akan tahu bagaimana untuk:

- Membangun Agen AI Siap Produksi menggunakan Microsoft Agent Framework
- Menerapkan fitur inti Microsoft Agent Framework pada Use Cases Agentic Anda
- Menggunakan pola lanjutan termasuk alur kerja, middleware, dan observabilitas

## Contoh Kode 

Contoh kode untuk [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) dapat ditemukan di repositori ini di bawah file `xx-python-agent-framework` dan `xx-dotnet-agent-framework`.

## Memahami Microsoft Agent Framework

![Framework Intro](../../../translated_images/id/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) adalah framework terpadu Microsoft untuk membangun agen AI. Ini menawarkan fleksibilitas untuk menangani berbagai macam use case agentik yang terlihat baik dalam lingkungan produksi maupun riset termasuk:

- **Orkestrasi Agen Secuensial** dalam skenario di mana alur kerja langkah demi langkah dibutuhkan.
- **Orkestrasi Konkuren** dalam skenario di mana agen harus menyelesaikan tugas secara bersamaan.
- **Orkestrasi Grup Chat** dalam skenario di mana agen dapat berkolaborasi bersama pada satu tugas.
- **Orkestrasi Penyerahan Tugas** dalam skenario di mana agen menyerahkan tugas satu sama lain saat subtugas selesai.
- **Orkestrasi Magnetik** dalam skenario di mana agen pengelola membuat dan memodifikasi daftar tugas dan menangani koordinasi subagen untuk menyelesaikan tugas.

Untuk mengantarkan Agen AI dalam Produksi, MAF juga menyertakan fitur untuk:

- **Observabilitas** melalui penggunaan OpenTelemetry di mana setiap aksi Agen AI termasuk pemanggilan alat, langkah orkestrasi, alur pemikiran dan pemantauan kinerja melalui dashboard Microsoft Foundry.
- **Keamanan** dengan host agen secara native di Microsoft Foundry yang mencakup kontrol keamanan seperti akses berbasis peran, penanganan data privat dan keamanan konten bawaan.
- **Ketahanan** karena thread dan alur kerja Agen dapat dijeda, dilanjutkan, dan pulih dari kesalahan yang memungkinkan proses berjalan lebih lama.
- **Kontrol** karena alur kerja human in the loop didukung di mana tugas ditandai sebagai memerlukan persetujuan manusia.

Microsoft Agent Framework juga fokus pada interoperabilitas dengan:

- **Bersifat Cloud-agnostic** - Agen dapat berjalan di kontainer, on-premise dan di berbagai cloud yang berbeda.
- **Bersifat Provider-agnostic** - Agen dapat dibuat melalui SDK pilihan Anda termasuk Azure OpenAI dan OpenAI
- **Integrasi Standar Terbuka** - Agen dapat memanfaatkan protokol seperti Agent-to-Agent (A2A) dan Model Context Protocol (MCP) untuk menemukan dan menggunakan agen serta alat lain.
- **Plugin dan Konektor** - Koneksi dapat dibuat ke layanan data dan memori seperti Microsoft Fabric, SharePoint, Pinecone, dan Qdrant.

Mari kita lihat bagaimana fitur-fitur ini diterapkan ke beberapa konsep inti Microsoft Agent Framework.

## Konsep Utama Microsoft Agent Framework

### Agen

![Agent Framework](../../../translated_images/id/agent-components.410a06daf87b4fef.webp)

**Membuat Agen**

Pembuatan agen dilakukan dengan mendefinisikan layanan inference (Penyedia LLM),  
sekumpulan instruksi yang diikuti Agen AI, dan sebuah `name` yang ditetapkan:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Di atas menggunakan `Azure OpenAI` tetapi agen dapat dibuat menggunakan berbagai layanan termasuk `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, API `ChatCompletion`

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
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

Setiap run agen juga bisa memiliki opsi untuk menyesuaikan parameter seperti `max_tokens` yang digunakan oleh agen, `tools` yang bisa dipanggil agen, dan bahkan `model` yang digunakan untuk agen.

Ini berguna dalam kasus di mana model atau alat tertentu dibutuhkan untuk menyelesaikan tugas pengguna.

**Tools**

Alat dapat didefinisikan baik saat mendefinisikan agen:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Saat membuat ChatAgent secara langsung

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

dan juga saat menjalankan agen:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Alat disediakan hanya untuk sesi ini )
```

**Thread Agen**

Thread Agen digunakan untuk menangani percakapan multi-putaran. Thread dapat dibuat dengan:

- Menggunakan `get_new_thread()` yang memungkinkan thread disimpan seiring waktu
- Membuat thread secara otomatis saat menjalankan agen dan hanya membuat thread itu berlangsung selama run saat ini.

Untuk membuat thread, kode terlihat seperti ini:

```python
# Buat thread baru.
thread = agent.get_new_thread() # Jalankan agen dengan thread tersebut.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Anda kemudian dapat serialisasi thread untuk disimpan guna digunakan kemudian:

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

Agen berinteraksi dengan alat dan LLM untuk menyelesaikan tugas pengguna. Dalam situasi tertentu, kita ingin mengeksekusi atau melacak interaksi di antara mereka. Middleware agen memungkinkan kita melakukan ini melalui:

*Function Middleware*

Middleware ini memungkinkan kita mengeksekusi aksi di antara agen dan fungsi/alat yang akan dipanggilnya. Contohnya adalah saat Anda ingin melakukan logging pada panggilan fungsi.

Dalam kode di bawah `next` mendefinisikan apakah middleware berikutnya atau fungsi sebenarnya yang harus dipanggil.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Pra-pemrosesan: Catat sebelum eksekusi fungsi
    print(f"[Function] Calling {context.function.name}")

    # Lanjut ke middleware berikutnya atau eksekusi fungsi
    await next(context)

    # Pasca-pemrosesan: Catat setelah eksekusi fungsi
    print(f"[Function] {context.function.name} completed")
```

*Chat Middleware*

Middleware ini memungkinkan kita mengeksekusi atau mencatat aksi di antara agen dan permintaan antara LLM.

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

Seperti yang dibahas dalam pelajaran `Agentic Memory`, memori adalah elemen penting untuk memungkinkan agen beroperasi dalam konteks yang berbeda. MAF menawarkan beberapa jenis memori:

*Penyimpanan Dalam Memori*

Ini adalah memori yang disimpan dalam thread selama runtime aplikasi.

```python
# Buat sebuah thread baru.
thread = agent.get_new_thread() # Jalankan agen dengan thread tersebut.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Pesan Persisten*

Memori ini digunakan saat menyimpan riwayat percakapan lintas sesi berbeda. Ini didefinisikan menggunakan `chat_message_store_factory` :

```python
from agent_framework import ChatMessageStore

# Buat penyimpanan pesan khusus
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

# Menggunakan Mem0 untuk kemampuan memori lanjutan
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

Observabilitas penting untuk membangun sistem agentik yang dapat diandalkan dan mudah dipelihara. MAF terintegrasi dengan OpenTelemetry untuk menyediakan tracing dan meter untuk observabilitas yang lebih baik.

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

MAF menawarkan alur kerja yang merupakan langkah-langkah yang sudah terdefinisi sebelumnya untuk menyelesaikan tugas dan memasukkan agen AI sebagai komponen dalam langkah-langkah tersebut.

Alur kerja terdiri dari berbagai komponen yang memungkinkan alur kontrol yang lebih baik. Alur kerja juga memungkinkan **orkestrasi multi-agen** dan **checkpointing** untuk menyimpan state alur kerja.

Komponen inti sebuah alur kerja adalah:

**Executor**

Executor menerima pesan input, melaksanakan tugas yang ditugaskan, dan kemudian menghasilkan pesan output. Ini menggerakkan alur kerja menuju penyelesaian tugas yang lebih besar. Executor bisa berupa agen AI atau logika khusus.

**Edges**

Edges digunakan untuk mendefinisikan alur pesan dalam sebuah alur kerja. Ini bisa berupa:

*Edges Langsung* - Koneksi satu-ke-satu sederhana antara executor:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Edges Kondisional* - Diaktifkan setelah kondisi tertentu terpenuhi. Contohnya, ketika kamar hotel tidak tersedia, executor dapat menyarankan opsi lain.

*Edges Switch-case* - Mengarahkan pesan ke executor yang berbeda berdasarkan kondisi yang ditentukan. Misalnya, jika pelanggan travel memiliki akses prioritas dan tugasnya akan ditangani melalui alur kerja lain.

*Edges Fan-out* - Mengirim satu pesan ke beberapa target.

*Edges Fan-in* - Mengumpulkan beberapa pesan dari executor berbeda dan mengirim ke satu target.

**Events**

Untuk menyediakan observabilitas yang lebih baik ke alur kerja, MAF menawarkan event bawaan untuk eksekusi termasuk:

- `WorkflowStartedEvent`  - Eksekusi alur kerja dimulai
- `WorkflowOutputEvent` - Alur kerja menghasilkan output
- `WorkflowErrorEvent` - Alur kerja mengalami kesalahan
- `ExecutorInvokeEvent`  - Executor mulai memproses
- `ExecutorCompleteEvent`  -  Executor selesai memproses
- `RequestInfoEvent` - Permintaan dikeluarkan

## Pola MAF Lanjutan

Bagian-bagian di atas membahas konsep utama Microsoft Agent Framework. Saat Anda membangun agen yang lebih kompleks, berikut beberapa pola lanjutan yang perlu dipertimbangkan:

- **Kombinasi Middleware**: Rangkai beberapa handler middleware (logging, otentikasi, pembatasan laju) menggunakan middleware fungsi dan obrolan untuk kontrol perilaku agen yang lebih terperinci.
- **Checkpointing Alur Kerja**: Gunakan event alur kerja dan serialisasi untuk menyimpan dan melanjutkan proses agen yang berjalan lama.
- **Seleksi Alat Dinamis**: Gabungkan RAG melalui deskripsi alat dengan pendaftaran alat MAF untuk menyajikan hanya alat yang relevan per kueri.
- **Penyerahan Multi-Agen**: Gunakan edges alur kerja dan routing kondisional untuk mengorkestrasi penyerahan tugas antar agen khusus.

## Contoh Kode 

Contoh kode untuk Microsoft Agent Framework dapat ditemukan di repositori ini di bawah file `xx-python-agent-framework` dan `xx-dotnet-agent-framework`.

## Punya Pertanyaan Lebih Lanjut Tentang Microsoft Agent Framework?

Bergabunglah dengan [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) untuk bertemu dengan pelajar lain, menghadiri jam kantor dan mendapatkan jawaban atas pertanyaan Anda tentang Agen AI.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan terjemahan yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan jasa terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->