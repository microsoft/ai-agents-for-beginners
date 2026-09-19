# Meneroka Rangka Kerja Ejen Microsoft

![Agent Framework](../../../translated_images/ms/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Pengenalan

Pelajaran ini akan meliputi:

- Memahami Rangka Kerja Ejen Microsoft: Ciri-ciri Utama dan Nilai  
- Meneroka Konsep Utama Rangka Kerja Ejen Microsoft
- Corak MAF Lanjutan: Aliran Kerja, Middleware, dan Memori

## Matlamat Pembelajaran

Selepas menamatkan pelajaran ini, anda akan mengetahui cara untuk:

- Membangunkan Ejen AI Sedia untuk Pengeluaran menggunakan Rangka Kerja Ejen Microsoft
- Mengaplikasikan ciri teras Rangka Kerja Ejen Microsoft kepada Kes Penggunaan Ejen anda
- Menggunakan corak lanjutan termasuk aliran kerja, middleware, dan boleh perhatikan (observability)

## Contoh Kod 

Contoh kod untuk [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) boleh didapati dalam repositori ini di bawah fail `xx-python-agent-framework` dan `xx-dotnet-agent-framework`.

## Memahami Rangka Kerja Ejen Microsoft

![Framework Intro](../../../translated_images/ms/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) adalah rangka kerja sehenti Microsoft untuk membina ejen AI. Ia menawarkan fleksibiliti untuk menangani pelbagai kes penggunaan ejen yang dilihat dalam persekitaran produksi dan penyelidikan termasuk:

- **Pengaturan Ejen Bersiri** dalam senario di mana aliran kerja langkah demi langkah diperlukan.
- **Pengaturan Serentak** dalam senario di mana ejen perlu menyelesaikan tugasan pada masa yang sama.
- **Pengaturan Perbualan Kumpulan** dalam senario di mana ejen boleh bekerjasama dalam satu tugasan.
- **Pengaturan Pemindahan** dalam senario di mana ejen menyerahkan tugasan antara satu sama lain apabila subtugasan selesai.
- **Pengaturan Magnetik** dalam senario di mana ejen pengurus mencipta dan mengubah senarai tugasan serta mengatur penyelarasan subejen untuk melengkapkan tugasan.

Untuk menyampaikan Ejen AI dalam Produksi, MAF juga mempunyai ciri untuk:

- **Boleh Perhatikan (Observability)** melalui penggunaan OpenTelemetry di mana setiap tindakan Ejen AI termasuk panggilan alat, langkah pengaturan, aliran alasan dan pemantauan prestasi melalui papan pemuka Microsoft Foundry.
- **Keselamatan** dengan mengehos ejen secara asli pada Microsoft Foundry yang merangkumi kawalan keselamatan seperti akses berasaskan peranan, pengendalian data peribadi dan keselamatan kandungan terbina dalam.
- **Ketahanan** kerana thread dan aliran kerja Ejen boleh dijeda, disambung semula dan pulih dari ralat yang membolehkan proses berjalan lebih lama.
- **Kawalan** kerana aliran kerja manusia dalam gelung disokong di mana tugasan ditandakan memerlukan kelulusan manusia.

Rangka Kerja Ejen Microsoft juga memberi tumpuan kepada kebolehsambungan dengan:

- **Bebas Awan (Cloud-agnostic)** - Ejen boleh dijalankan dalam bekas, di premis dan merentasi pelbagai awan berbeza.
- **Bebas Penyedia (Provider-agnostic)** - Ejen boleh dicipta melalui SDK pilihan anda termasuk Azure OpenAI dan OpenAI
- **Mengintegrasi Standard Terbuka** - Ejen boleh menggunakan protokol seperti Agent-to-Agent (A2A) dan Protokol Konteks Model (MCP) untuk menemui dan menggunakan ejen dan alat lain.
- **Plugin dan Penyambung** - Sambungan boleh dibuat ke perkhidmatan data dan memori seperti Microsoft Fabric, SharePoint, Pinecone dan Qdrant.

Mari kita lihat bagaimana ciri-ciri ini digunakan dalam beberapa konsep teras Rangka Kerja Ejen Microsoft.

## Konsep Utama Rangka Kerja Ejen Microsoft

### Ejen

![Agent Framework](../../../translated_images/ms/agent-components.410a06daf87b4fef.webp)

**Mencipta Ejen**

Penciptaan ejen dilakukan dengan mentakrifkan perkhidmatan inferens (Penyedia LLM), 
satu set arahan untuk diikuti oleh Ejen AI, dan `nama` yang diberikan:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Kod di atas menggunakan `Azure OpenAI` tetapi ejen boleh dicipta menggunakan pelbagai perkhidmatan termasuk `Microsoft Foundry Agent Service`:

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

atau [MiniMax](https://platform.minimaxi.com/), yang menyediakan API serasi OpenAI dengan tetingkap konteks besar (sehingga 204K token):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

atau ejen jarak jauh menggunakan protokol A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Menjalankan Ejen**

Ejen dijalankan menggunakan kaedah `.run` atau `.run_stream` untuk respons bukan penstriman atau penstriman.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Setiap larian ejen juga boleh mempunyai pilihan untuk mengubah parameter seperti `max_tokens` yang digunakan oleh ejen, `tools` yang boleh dipanggil oleh ejen, dan juga `model` yang digunakan bagi ejen tersebut.

Ini berguna dalam kes di mana model atau alat tertentu diperlukan untuk menyelesaikan tugasan pengguna.

**Alat**

Alat boleh ditakrifkan semasa mentakrifkan ejen:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Apabila membuat ChatAgent secara langsung

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

dan juga semasa menjalankan ejen:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Alat disediakan untuk larian ini sahaja )
```

**Thread Ejen**

Thread Ejen digunakan untuk mengendalikan perbualan berbilang pusingan. Thread boleh dicipta dengan:

- Menggunakan `get_new_thread()` yang membolehkan thread disimpan dari masa ke masa
- Mencipta thread secara automatik apabila menjalankan ejen dan thread hanya wujud sepanjang larian semasa.

Kod untuk mencipta thread adalah seperti berikut:

```python
# Cipta satu utas baru.
thread = agent.get_new_thread() # Jalankan ejen dengan utas itu.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Anda kemudian boleh menyusun serialize thread untuk disimpan bagi kegunaan kemudian:

```python
# Cipta benang baru.
thread = agent.get_new_thread() 

# Jalankan ejen dengan benang tersebut.

response = await agent.run("Hello, how are you?", thread=thread) 

# Siri benang untuk penyimpanan.

serialized_thread = await thread.serialize() 

# Nyah siri keadaan benang selepas memuat dari penyimpanan.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware Ejen**

Ejen berinteraksi dengan alat dan LLM untuk menyelesaikan tugasan pengguna. Dalam beberapa scenario, kita mahu menjalankan atau melacak interaksi antara itu. Middleware ejen membolehkan kita untuk melakukan ini melalui:

*Middleware Fungsi*

Middleware ini membolehkan tindakan dilakukan antara ejen dan fungsi/alat yang akan dipanggil. Contohnya adalah apabila anda mahu merekod log panggilan fungsi.

Dalam kod di bawah `next` menentukan sama ada middleware seterusnya atau fungsi sebenar dipanggil.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Pralaksanaan: Log sebelum pelaksanaan fungsi
    print(f"[Function] Calling {context.function.name}")

    # Teruskan ke middleware seterusnya atau pelaksanaan fungsi
    await next(context)

    # Pasca-pemprosesan: Log selepas pelaksanaan fungsi
    print(f"[Function] {context.function.name} completed")
```

*Middleware Perbualan*

Middleware ini membolehkan tindakan atau pencatatan dilakukan antara ejen dan permintaan antara LLM.

Ini mengandungi maklumat penting seperti `messige` yang dihantar ke perkhidmatan AI.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Pra-pemprosesan: Log sebelum panggilan AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Terus ke middleware atau perkhidmatan AI seterusnya
    await next(context)

    # Pasca-pemprosesan: Log selepas maklum balas AI
    print("[Chat] AI response received")

```

**Memori Ejen**

Seperti yang dibincangkan dalam pelajaran `Memori Agenik`, memori adalah elemen penting untuk membolehkan ejen beroperasi atas konteks yang berbeza. MAF menawarkan beberapa jenis memori yang berbeza:

*Penyimpanan Dalam Memori*

Ini adalah memori yang disimpan dalam thread semasa runtime aplikasi.

```python
# Buat benang baru.
thread = agent.get_new_thread() # Jalankan ejen dengan benang tersebut.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Mesej Kekal*

Memori ini digunakan apabila menyimpan sejarah perbualan merentasi sesi yang berbeza. Ia ditakrifkan menggunakan `chat_message_store_factory`:

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

Memori ini ditambah ke dalam konteks sebelum ejen dijalankan. Memori ini boleh disimpan dalam perkhidmatan luar seperti mem0:

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

**Kebolehpantauan Ejen (Observability)**

Kebolehpantauan adalah penting untuk membina sistem ejen yang boleh dipercayai dan mudah diselenggara. MAF mengintegrasi dengan OpenTelemetry untuk menyediakan penjejakan dan pengukuran bagi kebolehpantauan yang lebih baik.

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

MAF menawarkan aliran kerja yang merupakan langkah yang telah ditetapkan untuk melengkapkan tugasan dan termasuk ejen AI sebagai komponen dalam langkah tersebut.

Aliran kerja terdiri daripada pelbagai komponen yang membolehkan aliran kawalan yang lebih baik. Aliran kerja juga membolehkan **pengaturan banyak ejen** dan **penandaan cekmatan** untuk menyimpan keadaan aliran kerja.

Komponen teras aliran kerja adalah:

**Pelaksana**

Pelaksana menerima mesej input, melaksanakan tugasan yang diberikan, dan menghasilkan mesej output. Ini menggerakkan aliran kerja maju ke arah menyelesaikan tugasan yang lebih besar. Pelaksana boleh sama ada ejen AI atau logik khusus.

**Tepi**

Tepi digunakan untuk mentakrifkan aliran mesej dalam aliran kerja. Ini boleh terdiri daripada:

*Tepi Langsung* - Sambungan satu-ke-satu mudah antara pelaksana:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Tepi Bersyarat* - Diaktifkan selepas syarat tertentu dipenuhi. Contohnya, apabila bilik hotel tidak tersedia, pelaksana boleh mencadangkan pilihan lain.

*Tepi Suis* - Mengarahkan mesej ke pelaksana yang berbeza berdasarkan syarat ditetapkan. Contoh, jika pelanggan perjalanan mempunyai akses keutamaan, tugasan mereka akan diurus melalui aliran kerja yang lain.

*Tepi Fan-out* - Hantar satu mesej ke pelbagai sasaran.

*Tepi Fan-in* - Kumpul beberapa mesej dari pelaksana yang berbeza dan hantar ke satu sasaran.

**Peristiwa**

Untuk menyediakan kebolehpantauan yang lebih baik ke dalam aliran kerja, MAF menawarkan peristiwa terbina dalam untuk pelaksanaan termasuk:

- `WorkflowStartedEvent`  - Pelaksanaan aliran kerja bermula
- `WorkflowOutputEvent` - Aliran kerja menghasilkan output
- `WorkflowErrorEvent` - Aliran kerja menghadapi ralat
- `ExecutorInvokeEvent`  - Pelaksana mula memproses
- `ExecutorCompleteEvent`  -  Pelaksana selesai memproses
- `RequestInfoEvent` - Permintaan dikeluarkan

## Corak MAF Lanjutan

Bahagian di atas merangkumi konsep utama Rangka Kerja Ejen Microsoft. Semasa anda membina ejen yang lebih kompleks, ini adalah beberapa corak lanjutan yang boleh dipertimbangkan:

- **Gabungan Middleware**: Rangkai beberapa pengendali middleware (pencatatan, pengesahan, pengehad kadar) menggunakan middleware fungsi dan perbualan untuk kawalan halus ke atas tingkah laku ejen.
- **Penandaan Cekpoint Aliran Kerja**: Gunakan peristiwa aliran kerja dan penyusunan semula untuk menyimpan dan menyambung semula proses ejen yang berjalan lama.
- **Pemilihan Alat Dinamik**: Gabungkan RAG atas penerangan alat dengan pendaftaran alat MAF untuk hanya mempersembahkan alat berkaitan setiap pertanyaan.
- **Pemindahan Pelbagai Ejen**: Gunakan tepi aliran kerja dan laluan bersyarat untuk mengatur pemindahan antara ejen khusus.

## Mengehos Ejen LangChain / LangGraph pada Microsoft Foundry

Rangka Kerja Ejen Microsoft adalah **kerangka-interoperable** — anda tidak terhad kepada ejen yang ditulis dengan MAF. Jika anda sudah mempunyai ejen yang dibina dengan **LangChain** atau **LangGraph**, anda boleh menjalankannya sebagai **ejen dihoskan Microsoft Foundry** supaya Foundry mengurus runtime, sesi, penskalaan, identiti, dan titik akhir protokol untuk anda, sementara logik ejen anda kekal dalam LangGraph.

Ini dilakukan dengan pakej `langchain_azure_ai.agents.hosting`, yang mendedahkan graf LangGraph yang telah disusun di atas protokol yang sama digunakan oleh ejen yang dihoskan Foundry.

**1. Pasang tambahan hosting:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Tambahan `hosting` memasang perpustakaan protokol Foundry: `azure-ai-agentserver-responses` (titik akhir `/responses` yang serasi dengan OpenAI) dan `azure-ai-agentserver-invocations` (titik akhir `/invocations` generik).

**2. Pilih protokol hosting:**

| Protokol | Kelas Host | Titik Akhir | Gunakan apabila |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Anda mahukan chat, penstriman, sejarah respons, dan penyusunan perbualan yang serasi dengan OpenAI — lalai yang disyorkan untuk ejen perbualan. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Anda memerlukan bentuk JSON tersuai, titik akhir gaya webhook, atau pemprosesan bukan perbualan. |

Oleh kerana **API Responses adalah API utama untuk pembangunan gaya ejen di Foundry**, mulakan dengan `ResponsesHostServer` untuk kebanyakan ejen.

**3. Konfigurasikan pemboleh ubah persekitaran** (`az login` dahulu supaya `DefaultAzureCredential` boleh mengesahkan):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Apabila ejen dijalankan kemudian sebagai ejen dihoskan dalam Foundry, platform secara automatik menyuntik `FOUNDRY_PROJECT_ENDPOINT`.

**4. Dedahkan ejen LangGraph di atas protokol Responses:**

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

    # ChatOpenAI di sini mensasarkan titik akhir OpenAI-compatible (Responses) projek Foundry.
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

Jalankan secara setempat dengan `python main.py`, kemudian hantar permintaan Responses ke `http://localhost:8088/responses`.

**Tingkah laku utama:**

- **Perbualan**: Pelanggan menyambung perbualan dengan menghantar `previous_response_id` atau ID `conversation`. Jika graf anda disusun dengan LangGraph checkpointer, Foundry mengaitkan keadaan perbualan dengan cekpoint itu (gunakan checkpointer tahan lama dalam pengeluaran; `MemorySaver` sesuai untuk ujian setempat).
- **Manusia dalam gelung**: Jika graf anda menggunakan `interrupt()` LangGraph, `ResponsesHostServer` memaparkan gangguan tertunda sebagai item `function_call` / `mcp_approval_request` Responses, dan pelanggan menyambung dengan output `function_call_output` / `mcp_approval_response` yang sepadan.
- **Mengimplementasikan ke Foundry**: Gunakan Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (tempatan, memerlukan Docker), kemudian `azd provision` dan `azd deploy`. Penempatan ejen dihoskan memerlukan peranan **Pengurus Projek Foundry**.

Versi boleh dijalankan contoh ini boleh didapati dalam [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Untuk panduan penuh (protokol Invocations, skema permintaan tersuai, dan penyelesaian masalah), lihat [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Contoh Kod 

Contoh kod untuk Rangka Kerja Ejen Microsoft boleh didapati dalam repositori ini di bawah fail `xx-python-agent-framework` dan `xx-dotnet-agent-framework`.

## Ada Soalan Lagi Mengenai Rangka Kerja Ejen Microsoft?

Sertai [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) untuk bertemu dengan pembelajar lain, hadiri waktu pejabat dan dapatkan jawapan untuk soalan Ejen AI anda.
## Pelajaran Sebelumnya

[Memori untuk Ejen AI](../13-agent-memory/README.md)

## Pelajaran Seterusnya

[Membangunkan Ejen Penggunaan Komputer (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->