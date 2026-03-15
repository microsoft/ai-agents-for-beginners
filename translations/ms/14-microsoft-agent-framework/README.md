# Meneroka Microsoft Agent Framework

![Rangka Kerja Ejen](../../../translated_images/ms/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Pengenalan

Pelajaran ini akan merangkumi:

- Memahami Microsoft Agent Framework: Ciri Utama dan Nilai  
- Meneroka Konsep Utama Microsoft Agent Framework
- Corak MAF Lanjutan: Aliran Kerja, Perantara, dan Memori

## Matlamat Pembelajaran

Selepas melengkapkan pelajaran ini, anda akan mengetahui cara untuk:

- Membina Ejen AI Sedia Untuk Pengeluaran menggunakan Microsoft Agent Framework
- Mengaplikasikan ciri teras Microsoft Agent Framework kepada kes penggunaan ejen anda
- Menggunakan corak lanjutan termasuk aliran kerja, perantara, dan keterlihatan

## Contoh Kod 

Contoh kod untuk [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) boleh didapati dalam repositori ini di bawah fail `xx-python-agent-framework` dan `xx-dotnet-agent-framework`.

## Memahami Microsoft Agent Framework

![Pengenalan Rangka Kerja](../../../translated_images/ms/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) adalah rangka kerja bersatu Microsoft untuk membina ejen AI. Ia menawarkan fleksibiliti untuk menangani pelbagai jenis kes penggunaan ejen yang dilihat dalam persekitaran pengeluaran dan penyelidikan termasuk:

- **Penyelarasan Ejen Berurutan** dalam senario di mana aliran kerja langkah demi langkah diperlukan.
- **Orkestrasi Serentak** dalam senario di mana ejen perlu menyelesaikan tugas pada masa yang sama.
- **Orkestrasi Sembang Berkumpulan** dalam senario di mana ejen boleh bekerjasama bersama pada satu tugas.
- **Orkestrasi Penyerahan Tugas** dalam senario di mana ejen menyerahkan tugas antara satu sama lain apabila sub-tugas diselesaikan.
- **Orkestrasi Magnetik** dalam senario di mana ejen pengurus mencipta dan mengubah suai senarai tugas dan mengendalikan koordinasi subejen untuk menyelesaikan tugas.

Untuk menyampaikan Ejen AI dalam Pengeluaran, MAF juga menyertakan ciri untuk:

- **Observabiliti** melalui penggunaan OpenTelemetry di mana setiap tindakan Ejen AI termasuk panggilan alat, langkah orkestrasi, aliran penalaran dan pemantauan prestasi melalui papan pemuka Microsoft Foundry.
- **Keselamatan** dengan mengehos ejen secara asli di Microsoft Foundry yang merangkumi kawalan keselamatan seperti kawalan akses berasaskan peranan, pengendalian data peribadi dan keselamatan kandungan terbenam.
- **Daya Tahan** kerana benang ejen dan aliran kerja boleh dijeda, disambung semula dan pulih daripada ralat yang membolehkan proses berjalan lebih lama.
- **Kawalan** kerana aliran kerja 'manusia dalam gelung' disokong di mana tugas ditandakan sebagai memerlukan kelulusan manusia.

Microsoft Agent Framework juga memberi tumpuan kepada interoperabiliti dengan:

- **Awan-agnostik** - Ejen boleh dijalankan dalam kontena, secara on-prem dan merentasi pelbagai awan berbeza.
- **Penyedia-agnostik** - Ejen boleh dicipta melalui SDK pilihan anda termasuk Azure OpenAI dan OpenAI
- **Mengintegrasikan Piawaian Terbuka** - Ejen boleh menggunakan protokol seperti Agent-to-Agent(A2A) dan Model Context Protocol (MCP) untuk menemui dan menggunakan ejen serta alat lain.
- **Pemalam dan Penyambung** - Sambungan boleh dibuat kepada perkhidmatan data dan memori seperti Microsoft Fabric, SharePoint, Pinecone dan Qdrant.

Mari lihat bagaimana ciri-ciri ini diterapkan kepada beberapa konsep teras Microsoft Agent Framework.

## Konsep Utama Microsoft Agent Framework

### Ejen

![Komponen Ejen](../../../translated_images/ms/agent-components.410a06daf87b4fef.webp)

**Mewujudkan Ejen**

Penciptaan ejen dilakukan dengan mentakrifkan perkhidmatan inferens (LLM Provider), satu set arahan untuk Ejen AI ikuti, dan `name` yang ditetapkan:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Di atas menggunakan `Azure OpenAI` tetapi ejen boleh dicipta menggunakan pelbagai perkhidmatan termasuk `Microsoft Foundry Agent Service`:

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

atau ejen jauh menggunakan protokol A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Menjalankan Ejen**

Ejen dijalankan menggunakan kaedah `.run` atau `.run_stream` untuk respons tidak-menstrim atau menstrim.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Setiap larian ejen juga boleh mempunyai pilihan untuk mengubah suai parameter seperti `max_tokens` yang digunakan oleh ejen, `tools` yang boleh dipanggil oleh ejen, dan malah `model` itu sendiri yang digunakan untuk ejen.

Ini berguna dalam kes di mana model atau alat tertentu diperlukan untuk menyelesaikan tugas pengguna.

**Alat**

Alat boleh ditakrifkan semasa mendefinisikan ejen:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Apabila membuat ChatAgent secara langsung

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

dan juga semasa menjalankan ejen:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Alat disediakan hanya untuk penggunaan kali ini )
```

**Benang Ejen**

Benang Ejen digunakan untuk mengendalikan perbualan berbilang pusingan. Benang boleh dicipta sama ada dengan:

- Menggunakan `get_new_thread()` yang membolehkan benang disimpan dari semasa ke semasa
- Mencipta benang secara automatik semasa menjalankan ejen dan hanya membiarkan benang itu wujud semasa larian semasa.

Untuk mencipta benang, kodnya kelihatan seperti ini:

```python
# Cipta benang baru.
thread = agent.get_new_thread() # Jalankan ejen dengan benang itu.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Anda kemudian boleh serialize benang itu untuk disimpan bagi kegunaan kemudian:

```python
# Buat benang baru.
thread = agent.get_new_thread() 

# Jalankan ejen dengan benang tersebut.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serialkan benang untuk penyimpanan.

serialized_thread = await thread.serialize() 

# Nyah-serialkan keadaan benang selepas dimuatkan dari penyimpanan.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Perantara Ejen**

Ejen berinteraksi dengan alat dan LLM untuk menyelesaikan tugas pengguna. Dalam beberapa senario, kita ingin melaksanakan atau menjejak interaksi di antara tindakan ini. Perantara ejen membolehkan kita melakukan ini melalui:

*Perantara Fungsi*

Perantara ini membolehkan kita melaksanakan satu tindakan di antara ejen dan fungsi/alat yang akan dipanggil. Contoh penggunaan ialah apabila anda ingin melakukan log pada panggilan fungsi.

Dalam kod di bawah `next` menentukan sama ada perantara seterusnya atau fungsi sebenar patut dipanggil.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Pra-pemprosesan: Log sebelum pelaksanaan fungsi
    print(f"[Function] Calling {context.function.name}")

    # Teruskan ke middleware seterusnya atau ke pelaksanaan fungsi
    await next(context)

    # Pasca-pemprosesan: Log selepas pelaksanaan fungsi
    print(f"[Function] {context.function.name} completed")
```

*Perantara Sembang*

Perantara ini membolehkan kita melaksanakan atau merekod tindakan di antara ejen dan permintaan kepada LLM.

Ini mengandungi maklumat penting seperti `messages` yang dihantar ke perkhidmatan AI.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Pra-pemprosesan: Log sebelum panggilan AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Teruskan ke middleware seterusnya atau perkhidmatan AI
    await next(context)

    # Pasca-pemprosesan: Log selepas respons AI
    print("[Chat] AI response received")

```

**Memori Ejen**

Seperti yang diliputi dalam pelajaran `Agentic Memory`, memori adalah elemen penting untuk membolehkan ejen beroperasi dalam konteks yang berbeza. MAF menawarkan beberapa jenis memori yang berbeza:

*Penyimpanan Dalam Memori*

Ini adalah memori yang disimpan dalam benang semasa runtime aplikasi.

```python
# Cipta utas baru.
thread = agent.get_new_thread() # Jalankan ejen dengan utas tersebut.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Mesej Berterusan*

Memori ini digunakan apabila menyimpan sejarah perbualan merentasi sesi yang berbeza. Ia ditakrifkan menggunakan `chat_message_store_factory` :

```python
from agent_framework import ChatMessageStore

# Cipta stor mesej tersuai
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Memori Dinamik*

Memori ini ditambah ke konteks sebelum ejen dijalankan. Memori ini boleh disimpan dalam perkhidmatan luaran seperti mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Menggunakan Mem0 untuk keupayaan memori lanjutan
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

**Observabiliti Ejen**

Observabiliti penting untuk membina sistem ejen yang boleh dipercayai dan diselenggara. MAF berintegrasi dengan OpenTelemetry untuk menyediakan penjejakan dan pengukur bagi observabiliti yang lebih baik.

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

### Aliran Kerja

MAF menawarkan aliran kerja yang merupakan langkah pra-takrif untuk menyelesaikan tugas dan memasukkan ejen AI sebagai komponen dalam langkah-langkah tersebut.

Aliran kerja terdiri daripada pelbagai komponen yang membolehkan aliran kawalan yang lebih baik. Aliran kerja juga membolehkan **orkestrasi berbilang ejen** dan **penandaan semula (checkpointing)** untuk menyimpan keadaan aliran kerja.

Komponen teras aliran kerja adalah:

**Pelaksana**

Pelaksana menerima mesej input, melaksanakan tugas yang diberikan kepada mereka, dan kemudian menghasilkan mesej keluaran. Ini menggerakkan aliran kerja ke hadapan untuk menyelesaikan tugas yang lebih besar. Pelaksana boleh menjadi ejen AI atau logik tersuai.

**Tepi**

Tepi digunakan untuk mendefinisikan aliran mesej dalam aliran kerja. Ini boleh menjadi:

*Tepi Langsung* - Sambungan ringkas satu-ke-satu antara pelaksana:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Tepi Bersyarat* - Diaktifkan selepas sesuatu syarat dipenuhi. Sebagai contoh, apabila bilik hotel tidak tersedia, seorang pelaksana boleh mencadangkan pilihan lain.

*Tepi Tukar-kes* - Menghala mesej kepada pelaksana yang berbeza berdasarkan syarat yang ditakrifkan. Sebagai contoh, jika pelanggan perjalanan mempunyai akses keutamaan dan tugasan mereka akan diuruskan melalui aliran kerja lain.

*Tepi Fan-out* - Hantar satu mesej kepada berbilang sasaran.

*Tepi Fan-in* - Mengumpulkan berbilang mesej dari pelaksana yang berbeza dan menghantar kepada satu sasaran.

**Acara**

Untuk memberi observabiliti yang lebih baik ke dalam aliran kerja, MAF menawarkan acara terbina dalam untuk pelaksanaan termasuk:

- `WorkflowStartedEvent`  - Pelaksanaan aliran kerja bermula
- `WorkflowOutputEvent` - Aliran kerja menghasilkan output
- `WorkflowErrorEvent` - Aliran kerja menghadapi ralat
- `ExecutorInvokeEvent`  - Pelaksana mula memproses
- `ExecutorCompleteEvent`  -  Pelaksana menyelesaikan pemprosesan
- `RequestInfoEvent` - A request is issued

## Corak MAF Lanjutan

Bahagian di atas merangkumi konsep utama Microsoft Agent Framework. Semasa anda membina ejen yang lebih kompleks, berikut adalah beberapa corak lanjutan yang perlu dipertimbangkan:

- **Komposisi Perantara**: Rantai beberapa pengendali perantara (pencatatan, pengesahan, had-kadar) menggunakan perantara fungsi dan sembang untuk kawalan terperinci ke atas tingkah laku ejen.
- **Penandaan Semula Aliran Kerja (Workflow Checkpointing)**: Gunakan acara aliran kerja dan serialisasi untuk menyimpan dan menyambung semula proses ejen yang berjalan lama.
- **Pemilihan Alat Dinamik**: Gabungkan RAG ke atas keterangan alat dengan pendaftaran alat MAF untuk membentangkan hanya alat yang relevan bagi setiap pertanyaan.
- **Penyerahan Pelbagai Ejen**: Gunakan tepi aliran kerja dan routing bersyarat untuk mengorkestrakan penyerahan antara ejen khusus.

## Contoh Kod 

Contoh kod untuk Microsoft Agent Framework boleh didapati dalam repositori ini di bawah fail `xx-python-agent-framework` dan `xx-dotnet-agent-framework`.

## Ada Lebih Banyak Soalan Mengenai Microsoft Agent Framework?

Sertai [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) untuk berjumpa dengan pelajar lain, menghadiri waktu pejabat dan dapatkan jawapan bagi soalan anda tentang Ejen AI.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Penafian:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI Co-op Translator (https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk mencapai ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi ralat atau ketidaktepatan. Dokumen asal dalam bahasa asalnya hendaklah dianggap sebagai sumber rujukan yang muktamad. Untuk maklumat kritikal, disyorkan terjemahan profesional oleh penterjemah manusia. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsiran yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->