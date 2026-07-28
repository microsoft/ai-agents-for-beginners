# Meneroka Rangka Kerja Ejen Microsoft

![Agent Framework](../../../translated_images/ms/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Pengenalan

Pelajaran ini akan meliputi:

- Memahami Rangka Kerja Ejen Microsoft: Ciri Utama dan Nilai  
- Meneroka Konsep Utama Rangka Kerja Ejen Microsoft
- Corak MAF Lanjutan: Aliran Kerja, Perantara, dan Memori

## Matlamat Pembelajaran

Selepas menamatkan pelajaran ini, anda akan tahu bagaimana untuk:

- Membina Ejen AI yang Sedia untuk Pengeluaran menggunakan Rangka Kerja Ejen Microsoft
- Menerapkan ciri teras Rangka Kerja Ejen Microsoft ke dalam Kes Penggunaan Ejen anda
- Menggunakan corak lanjutan termasuk aliran kerja, perantara, dan pemerhatian

## Contoh Kod 

Contoh kod untuk [Rangka Kerja Ejen Microsoft (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) boleh didapati dalam repositori ini di bawah fail `xx-python-agent-framework` dan `xx-dotnet-agent-framework`.

## Memahami Rangka Kerja Ejen Microsoft

![Framework Intro](../../../translated_images/ms/framework-intro.077af16617cf130c.webp)

[Rangka Kerja Ejen Microsoft (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) adalah rangka kerja bersepadu Microsoft untuk membina ejen AI. Ia menawarkan fleksibiliti untuk menangani pelbagai kes penggunaan ejen yang dilihat di persekitaran pengeluaran dan penyelidikan termasuk:

- **Orkestrasi Ejen Bersiri** dalam senario di mana aliran kerja langkah demi langkah diperlukan.
- **Orkestrasi Serentak** dalam senario di mana ejen perlu menyelesaikan tugas pada masa yang sama.
- **Orkestrasi Sembang Kumpulan** dalam senario di mana ejen boleh bekerjasama dalam satu tugas.
- **Orkestrasi Penyerahan** dalam senario di mana ejen menyerahkan tugas antara satu sama lain apabila subtugas diselesaikan.
- **Orkestrasi Magnetik** dalam senario di mana ejen pengurus mencipta dan mengubah senarai tugas serta mengendalikan penyelarasan ejen kecil untuk melengkapkan tugas tersebut.

Untuk memberikan Ejen AI dalam Pengeluaran, MAF juga telah memasukkan ciri untuk:

- **Pemerhatian** melalui penggunaan OpenTelemetry di mana setiap tindakan Ejen AI termasuk panggilan alat, langkah orkestrasi, aliran penaakulan dan pemantauan prestasi melalui papan pemuka Microsoft Foundry.
- **Keselamatan** dengan mengehoskan ejen secara asli di Microsoft Foundry yang merangkumi kawalan keselamatan seperti akses berasaskan peranan, pengendalian data peribadi dan keselamatan kandungan terbina dalam.
- **Ketahanan** kerana jejari dan aliran kerja Ejen boleh berhenti, sambung semula dan pulih daripada ralat yang membolehkan proses berjalan lebih lama.
- **Kawalan** kerana aliran kerja manusia dalam gelung disokong di mana tugas ditandakan sebagai memerlukan kelulusan manusia.

Rangka Kerja Ejen Microsoft juga memfokuskan pada kebolehoperasian dengan:

- **Bersifat Awan-agnostik** - Ejen boleh dijalankan dalam bekas, di premis dan merentasi pelbagai awan yang berbeza.
- **Bersifat Penyedia-agnostik** - Ejen boleh dicipta melalui SDK pilihan anda termasuk Azure OpenAI dan OpenAI
- **Mengintegrasi Standard Terbuka** - Ejen boleh menggunakan protokol seperti Agent-to-Agent(A2A) dan Model Context Protocol (MCP) untuk menemui dan menggunakan ejen serta alat lain.
- **Plugin dan Penyambung** - Sambungan boleh dibuat ke perkhidmatan data dan memori seperti Microsoft Fabric, SharePoint, Pinecone dan Qdrant.

Mari lihat bagaimana ciri-ciri ini diterapkan pada beberapa konsep teras Rangka Kerja Ejen Microsoft.

## Konsep Utama Rangka Kerja Ejen Microsoft

### Ejen

![Agent Framework](../../../translated_images/ms/agent-components.410a06daf87b4fef.webp)

**Mencipta Ejen**

Penciptaan ejen dilakukan dengan menentukan perkhidmatan inferens (Penyedia LLM), satu
set arahan untuk Ejen AI ikuti, dan `nama` yang diberikan:

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

atau [MiniMax](https://platform.minimaxi.com/), yang menyediakan API serasi OpenAI dengan tetingkap konteks besar (sehingga 204K token):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

atau ejen jauh menggunakan protokol A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Menjalankan Ejen**

Ejen dijalankan menggunakan kaedah `.run` atau `.run_stream` untuk respons bukan streaming atau streaming.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Setiap larian ejen juga boleh mempunyai pilihan untuk menyesuaikan parameter seperti `max_tokens` yang digunakan oleh ejen, `tools` yang boleh dipanggil oleh ejen, malah `model` itu sendiri yang digunakan untuk ejen.

Ini berguna dalam kes model atau alat tertentu diperlukan untuk melengkapkan tugas pengguna.

**Alat**

Alat boleh ditakrifkan semasa menentukan ejen:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Apabila membuat ChatAgent secara langsung

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

dan juga semasa menjalankan ejen:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Alat disediakan hanya untuk larian ini )
```

**Jejari Ejen**

Jejari Ejen digunakan untuk mengendalikan perbualan multi-pusingan. Jejari boleh dicipta sama ada dengan:

- Menggunakan `get_new_thread()` yang membolehkan jejari disimpan dari masa ke masa
- Mencipta jejari secara automatik semasa menjalankan ejen dan hanya menjadikan jejari itu wujud sepanjang larian semasa.

Untuk mencipta jejari, kodnya nampak seperti ini:

```python
# Cipta benang baru.
thread = agent.get_new_thread() # Jalankan ejen dengan benang tersebut.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Anda kemudian boleh menyimpan secara bersiri jejari untuk disimpan bagi kegunaan kemudian:

```python
# Cipta benang baru.
thread = agent.get_new_thread() 

# Jalankan ejen dengan benang tersebut.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serealkan benang untuk penyimpanan.

serialized_thread = await thread.serialize() 

# Deserialkan keadaan benang selepas dimuatkan dari penyimpanan.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Perantara Ejen**

Ejen berinteraksi dengan alat dan LLM untuk melengkapkan tugas pengguna. Dalam senario tertentu, kita mahu melaksanakan atau mengesan interaksi antara ini. Perantara ejen membolehkan kita melakukan ini melalui:

*Perantara Fungsi*

Perantara ini membolehkan kita melaksanakan tindakan antara ejen dan fungsi/alat yang akan dipanggil. Contoh bila ini digunakan ialah apabila anda mahu membuat log panggilan fungsi.

Dalam kod di bawah `next` mentakrifkan jika perantara seterusnya atau fungsi sebenar harus dipanggil.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Pra-pemprosesan: Log sebelum pelaksanaan fungsi
    print(f"[Function] Calling {context.function.name}")

    # Teruskan ke middleware seterusnya atau pelaksanaan fungsi
    await next(context)

    # Pasca-pemprosesan: Log selepas pelaksanaan fungsi
    print(f"[Function] {context.function.name} completed")
```

*Perantara Sembang*

Perantara ini membolehkan kita melaksanakan atau merekod tindakan antara ejen dan permintaan antara LLM .

Ini mengandungi maklumat penting seperti `mesej` yang dihantar ke perkhidmatan AI.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Pra-pemprosesan: Log sebelum panggilan AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Teruskan ke middleware atau perkhidmatan AI seterusnya
    await next(context)

    # Pasca-pemprosesan: Log selepas respons AI
    print("[Chat] AI response received")

```

**Memori Ejen**

Seperti yang dibincangkan dalam pelajaran `Memori Ejenik`, memori adalah unsur penting untuk membolehkan ejen beroperasi dalam konteks berbeza. MAF menawarkan beberapa jenis memori yang berbeza:

*Penyimpanan Dalam Memori*

Ini adalah memori yang disimpan dalam jejari semasa runtime aplikasi.

```python
# Cipta benang baru.
thread = agent.get_new_thread() # Jalankan ejen dengan benang tersebut.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Mesej Kekal*

Memori ini digunakan apabila menyimpan sejarah perbualan merentasi sesi berbeza. Ia ditakrifkan menggunakan `chat_message_store_factory` :

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

**Pemerhatian Ejen**


Observabiliti adalah penting untuk membina sistem agentik yang boleh dipercayai dan mudah diselenggara. MAF berintegrasi dengan OpenTelemetry untuk menyediakan penjejakan dan meter bagi observabiliti yang lebih baik.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # buat sesuatu
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Aliran Kerja

MAF menawarkan aliran kerja yang merupakan langkah-langkah yang telah ditetapkan untuk menyelesaikan tugas dan termasuk agen AI sebagai komponen dalam langkah-langkah tersebut.

Aliran kerja terdiri daripada komponen yang berbeza yang membolehkan kawalan aliran yang lebih baik. Aliran kerja juga membenarkan **orkestrasi multi-agen** dan **penanda checkpoint** untuk menyimpan status aliran kerja.

Komponen teras aliran kerja adalah:

**Pelaksana**

Pelaksana menerima mesej input, melaksanakan tugas yang diberikan, dan kemudian menghasilkan mesej output. Ini menggerakkan aliran kerja ke hadapan ke arah menyelesaikan tugasan yang lebih besar. Pelaksana boleh jadi agen AI atau logik tersuai.

**Sisi**

Sisi digunakan untuk menentukan aliran mesej dalam aliran kerja. Ini boleh menjadi:

*Sisi Langsung* - Sambungan satu-ke-satu ringkas antara pelaksana:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Sisi Bersyarat* - Diaktifkan selepas syarat tertentu dipenuhi. Contohnya, apabila bilik hotel tidak tersedia, pelaksana boleh mencadangkan pilihan lain.

*Sisi Suis-kes* - Menghala mesej kepada pelaksana berbeza berdasarkan syarat yang ditetapkan. Contohnya, jika pelanggan perjalanan mempunyai akses keutamaan dan tugas mereka akan dikendalikan melalui aliran kerja lain.

*Sisi Fan-out* - Hantar satu mesej kepada pelbagai sasaran.

*Sisi Fan-in* - Kumpul pelbagai mesej dari pelaksana berbeza dan hantar kepada satu sasaran.

**Acara**

Untuk menyediakan observabiliti yang lebih baik dalam aliran kerja, MAF menawarkan acara terbina dalam untuk pelaksanaan termasuk:

- `WorkflowStartedEvent`  - Pelaksanaan aliran kerja bermula
- `WorkflowOutputEvent` - Aliran kerja menghasilkan output
- `WorkflowErrorEvent` - Aliran kerja mengalami ralat
- `ExecutorInvokeEvent`  - Pelaksana mula memproses
- `ExecutorCompleteEvent`  -  Pelaksana selesai memproses
- `RequestInfoEvent` - Permintaan dikeluarkan

## Corak MAF Lanjutan

Bahagian di atas merangkumi konsep utama Microsoft Agent Framework. Apabila anda membina agen yang lebih kompleks, berikut adalah beberapa corak lanjutan yang boleh dipertimbangkan:

- **Komposisi Middleware**: Rantai beberapa pengendali middleware (log, pengesahan, had kadar) menggunakan fungsi dan middleware sembang untuk kawalan terperinci ke atas tingkah laku agen.
- **Penanda Checkpoint Aliran Kerja**: Gunakan acara aliran kerja dan penyerialan untuk menyimpan dan menyambung semula proses agen yang berjalan lama.
- **Pemilihan Alat Dinamik**: Gabungkan RAG ke atas penerangan alat dengan pendaftaran alat MAF untuk membentangkan hanya alat yang relevan bagi setiap pertanyaan.
- **Penyerahan Multi-Agen**: Gunakan sisi aliran kerja dan penghalaan bersyarat untuk mengorkestrasi penyerahan antara agen khusus.

## Menghoskan Agen LangChain / LangGraph pada Microsoft Foundry

Microsoft Agent Framework adalah **rangka kerja-interoperasi** — anda tidak terhad kepada agen yang ditulis dengan MAF. Jika anda sudah mempunyai agen yang dibina dengan **LangChain** atau **LangGraph**, anda boleh menjalankannya sebagai **agen yang dihoskan Microsoft Foundry** supaya Foundry menguruskan masa jalan, sesi, penskalaan, identiti, dan titik hujung protokol untuk anda, sementara logik agen anda kekal dalam LangGraph.

Ini dilakukan dengan pakej `langchain_azure_ai.agents.hosting`, yang mendedahkan graf LangGraph yang dikompilasi melalui protokol yang sama seperti agen yang dihoskan Foundry gunakan.

**1. Pasang ekstra hosting:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Ekstra `hosting` memasang perpustakaan protokol Foundry: `azure-ai-agentserver-responses` (titik hujung `/responses` yang serasi OpenAI) dan `azure-ai-agentserver-invocations` (titik hujung `/invocations` generik).

**2. Pilih protokol hosting:**

| Protokol | Kelas Hos | Titik Hujung | Gunakan apabila |
|----------|-----------|-------------|------------------|
| **Respons** | `ResponsesHostServer` | `/responses` | Anda mahukan sembang, penstriman, sejarah respons, dan penjejakan perbualan yang serasi OpenAI — lalai yang disyorkan untuk agen perbualan. |
| **Panggilan** | `InvocationsHostServer` | `/invocations` | Anda memerlukan bentuk JSON tersuai, titik hujung gaya webhook, atau pemprosesan bukan perbualan. |

Oleh kerana **API Respons adalah API utama untuk pembangunan gaya agen dalam Foundry**, mulakan dengan `ResponsesHostServer` untuk kebanyakan agen.

**3. Konfigurasikan pembolehubah persekitaran** (`az login` dahulu supaya `DefaultAzureCredential` boleh mengesahkan):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Apabila agen kemudian berjalan sebagai agen dihoskan di Foundry, platform secara automatik menyuntik `FOUNDRY_PROJECT_ENDPOINT`.

**4. Dedahkan agen LangGraph melalui protokol Respons:**

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

    # ChatOpenAI di sini menyasarkan titik hujung (Responses) yang serasi OpenAI dari projek Foundry.
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

Jalankan secara tempatan dengan `python main.py`, kemudian hantar permintaan Respons ke `http://localhost:8088/responses`.

**Tingkah laku utama:**

- **Perbualan**: Pelanggan meneruskan perbualan dengan menghantar `previous_response_id` atau ID `conversation`. Jika graf anda dikompilasi dengan cekpoin LangGraph, Foundry mengikat status perbualan kepada checkpoint (gunakan cekpoin tahan lama dalam produksi; `MemorySaver` sesuai untuk ujian tempatan).
- **Manusia dalam gelung**: Jika graf anda menggunakan LangGraph `interrupt()`, `ResponsesHostServer` memaparkan interupsi yang sedang menunggu sebagai item `function_call` / `mcp_approval_request` Respons, dan pelanggan meneruskan dengan `function_call_output` / `mcp_approval_response` yang sepadan.
- **Dideploy ke Foundry**: Gunakan Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (tempatan, memerlukan Docker), kemudian `azd provision` dan `azd deploy`. Pelaksanaan agen yang dihoskan memerlukan peranan **Pengurus Projek Foundry**.

Versi boleh dijalankan bagi contoh ini terdapat dalam [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Untuk panduan lengkap (protokol Panggilan, skema permintaan tersuai, dan penyelesaian masalah), lihat [Hoskan agen LangGraph sebagai agen dihoskan Foundry](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Contoh Kod 

Contoh kod untuk Microsoft Agent Framework boleh didapati dalam repositori ini di bawah fail `xx-python-agent-framework` dan `xx-dotnet-agent-framework`.

## Ada Soalan Lanjut Mengenai Microsoft Agent Framework?

Sertai [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) untuk bertemu dengan pelajar lain, menghadiri waktu pejabat dan dapatkan jawapan bagi soalan AI Agents anda.
## Pelajaran Sebelumnya

[Memori untuk AI Agents](../13-agent-memory/README.md)

## Pelajaran Seterusnya

[Membina Agen Penggunaan Komputer (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->