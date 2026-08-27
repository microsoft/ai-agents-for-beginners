# Meneroka Rangka Kerja Ejen Microsoft  

![Agent Framework](../../../translated_images/ms/lesson-14-thumbnail.90df0065b9d234ee.webp)  

### Pengenalan  

Pelajaran ini akan merangkumi:  

- Memahami Rangka Kerja Ejen Microsoft: Ciri-ciri Utama dan Nilai  
- Meneroka Konsep-Konsep Utama Rangka Kerja Ejen Microsoft  
- Corak MAF Lanjutan: Aliran Kerja, Perisian Perantaraan, dan Memori  

## Matlamat Pembelajaran  

Selepas menamatkan pelajaran ini, anda akan tahu bagaimana untuk:

- Membangunkan Ejen AI Sedia Produksi menggunakan Rangka Kerja Ejen Microsoft  
- Menerapkan ciri-ciri teras Rangka Kerja Ejen Microsoft kepada Kes Penggunaan Ejen anda  
- Menggunakan corak lanjutan termasuk aliran kerja, perisian perantaraan, dan keterlihatan  

## Contoh Kod   

Contoh kod untuk [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) boleh didapati dalam repositori ini di bawah fail `xx-python-agent-framework` dan `xx-dotnet-agent-framework`.  

## Memahami Rangka Kerja Ejen Microsoft  

![Framework Intro](../../../translated_images/ms/framework-intro.077af16617cf130c.webp)  

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) ialah rangka kerja sehenti Microsoft untuk membina ejen AI. Ia menawarkan kelenturan untuk menangani pelbagai jenis kes penggunaan ejen yang dilihat dalam persekitaran produksi dan penyelidikan termasuk:  

- **Orkestrasi Ejen Berurutan** dalam senario di mana aliran kerja langkah demi langkah diperlukan.  
- **Orkestrasi Serentak** dalam senario di mana ejen perlu menyelesaikan tugas pada masa yang sama.  
- **Orkestrasi Sembang Kumpulan** dalam senario di mana ejen boleh bekerjasama bersama untuk satu tugas.  
- **Orkestrasi Penyerahan** dalam senario di mana ejen menyerahkan tugas antara satu sama lain apabila subtugas disiapkan.  
- **Orkestrasi Magnetik** dalam senario di mana ejen pengurus mencipta dan mengubah senarai tugas dan mengendalikan koordinasi ejen sub untuk menyelesaikan tugas tersebut.  

Untuk menyampaikan Ejen AI dalam Produksi, MAF juga telah memasukkan ciri-ciri untuk:  

- **Keterlihatan** melalui penggunaan OpenTelemetry di mana setiap tindakan Ejen AI termasuk panggilan alat, langkah orkestrasi, aliran alasan dan pemantauan prestasi melalui papan pemuka Microsoft Foundry.  
- **Keselamatan** dengan mengehos ejen secara asli di Microsoft Foundry yang termasuk kawalan keselamatan seperti akses berdasarkan peranan, pengendalian data peribadi dan keselamatan kandungan terbina dalam.  
- **Ketahanan** kerana utas dan aliran kerja Ejen boleh dijeda, disambung semula dan pulih dari ralat yang membolehkan proses berjalan lebih lama.  
- **Kawalan** kerana aliran kerja manusia dalam gelung disokong di mana tugasan ditandakan sebagai memerlukan kelulusan manusia.  

Rangka Kerja Ejen Microsoft juga memberi tumpuan kepada keterhubungan dengan:  

- **Bebas Awan** - Ejen boleh dijalankan dalam bekas, secara atas premis dan merentasi pelbagai awan berbeza.  
- **Bebas Penyedia** - Ejen boleh dicipta melalui SDK pilihan anda termasuk Azure OpenAI dan OpenAI  
- **Mengintegrasi Piawaian Terbuka** - Ejen boleh menggunakan protokol seperti Agent-to-Agent(A2A) dan Model Context Protocol (MCP) untuk menemui dan menggunakan ejen dan alat lain.  
- **Plugin dan Penyambung** - Sambungan boleh dibuat ke perkhidmatan data dan memori seperti Microsoft Fabric, SharePoint, Pinecone dan Qdrant.  

Mari kita lihat bagaimana ciri-ciri ini diterapkan pada beberapa konsep teras Rangka Kerja Ejen Microsoft.  

## Konsep Utama Rangka Kerja Ejen Microsoft  

### Ejen  

![Agent Framework](../../../translated_images/ms/agent-components.410a06daf87b4fef.webp)  

**Mencipta Ejen**  

Penciptaan ejen dilakukan dengan mentakrifkan perkhidmatan inferens (Penyedia LLM), satu  
set arahan untuk Ejen AI ikuti, dan `nama` yang ditetapkan:  

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```
  
Di atas menggunakan `Azure OpenAI` tetapi ejen boleh dicipta menggunakan pelbagai perkhidmatan termasuk `Microsoft Foundry Agent Service`:  

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
  
atau [MiniMax](https://platform.minimaxi.com/), yang menyediakan API yang serasi OpenAI dengan tetingkap konteks besar (sehingga 204K token):  

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```
  
atau ejen jauh menggunakan protokol A2A:  

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```
  
**Menjalankan Ejen**  

Ejen dijalankan menggunakan kaedah `.run` atau `.run_stream` untuk tindak balas tidak penstriman atau penstriman.  

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```
  
```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```
  
Setiap larian ejen juga boleh mempunyai pilihan untuk menyesuaikan parameter seperti `max_tokens` yang digunakan oleh ejen, `tools` yang boleh dipanggil oleh ejen, dan bahkan `model` itu sendiri yang digunakan untuk ejen.  

Ini berguna dalam kes di mana model atau alat tertentu diperlukan untuk menyelesaikan tugas pengguna.  

**Alat**  

Alat boleh ditakrifkan semasa mentakrif ejen:  

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Apabila membuat ChatAgent secara langsung

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```
  
dan juga semasa menjalankan ejen:  

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Alat disediakan untuk larian ini sahaja )
```
  
**Utas Ejen**  

Utas Ejen digunakan untuk mengendalikan perbualan pelbagai giliran. Utas boleh dicipta dengan:  

- Menggunakan `get_new_thread()` yang membolehkan utas disimpan dari masa ke masa  
- Mencipta utas secara automatik semasa menjalankan ejen dan hanya menjadikan utas itu bertahan sepanjang larian semasa.  

Untuk mencipta utas, kodnya seperti berikut:  

```python
# Cipta utas baru.
thread = agent.get_new_thread() # Jalankan ejen dengan utas tersebut.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```
  
Anda boleh kemudian menyusunkan utas untuk disimpan bagi kegunaan kemudian:  

```python
# Cipta benang baru.
thread = agent.get_new_thread() 

# Jalankan agen dengan benang.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serikan benang untuk penyimpanan.

serialized_thread = await thread.serialize() 

# Deserikan keadaan benang selepas memuatkan dari storan.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```
  
**Perisian Perantaraan Ejen**  

Ejen berinteraksi dengan alat dan LLM untuk menyelesaikan tugasan pengguna. Dalam sesetengah senario, kita mahu melaksanakan atau menjejaki di antara interaksi tersebut. Perisian perantaraan ejen membolehkan kita melakukan ini melalui:  

*Perisian Perantaraan Fungsi*  

Perisian perantaraan ini membolehkan kita melaksanakan tindakan di antara ejen dan fungsi/alat yang akan dipanggilnya. Contohnya bila anda mahu melakukan sedikit log pada panggilan fungsi.  

Dalam kod di bawah `next` menentukan sama ada perisian perantaraan seterusnya atau fungsi sebenar harus dipanggil.  

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
  
*Perisian Perantaraan Sembang*  

Perisian perantaraan ini membolehkan kita melaksanakan atau mencatat tindakan di antara ejen dan permintaan antara LLM.  

Ini mengandungi maklumat penting seperti `méssages` yang dihantar ke perkhidmatan AI.  

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

Seperti yang dibincangkan dalam pelajaran `Agentic Memory`, memori adalah elemen penting untuk membolehkan ejen beroperasi dalam konteks berbeza. MAF menawarkan beberapa jenis memori:  

*Penyimpanan Dalam Memori*  

Ini adalah memori yang disimpan dalam utas semasa masa jalan aplikasi.  

```python
# Cipta utas baru.
thread = agent.get_new_thread() # Jalankan agen dengan utas tersebut.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```
  
*Mesej Kekal*  

Memori ini digunakan apabila menyimpan sejarah perbualan merentasi sesi berbeza. Ia ditakrifkan menggunakan `chat_message_store_factory`:  

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
  
**Keterlihatan Ejen**  

Keterlihatan penting untuk membina sistem ejen yang boleh dipercayai dan mudah diselenggara. MAF mengintegrasikan dengan OpenTelemetry untuk menyediakan penjejakan dan meter bagi keterlihatan yang lebih baik.  

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

MAF menawarkan aliran kerja yang merupakan langkah yang telah ditetapkan untuk menyelesaikan satu tugas dan termasuk ejen AI sebagai komponen dalam langkah tersebut.  

Aliran kerja terdiri daripada komponen berbeza yang membenarkan kawalan aliran yang lebih baik. Aliran kerja juga membolehkan **orkestrasi pelbagai ejen** dan **penandaan semula** untuk menyimpan status aliran kerja.  

Komponen teras aliran kerja adalah:  

**Pelaksana**  

Pelaksana menerima mesej input, melaksanakan tugasan yang diberikan, dan kemudian menghasilkan mesej output. Ini menggerakkan aliran kerja ke arah menyelesaikan tugas lebih besar. Pelaksana boleh menjadi sama ada ejen AI atau logik khusus.  

**Sisi**  

Sisi digunakan untuk mentakrifkan aliran mesej dalam aliran kerja. Ini boleh jadi:  

*Sisi Terus* - Sambungan satu-ke-satu mudah antara pelaksana:  

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```
  
*Sisi Bersyarat* - Diaktifkan selepas syarat tertentu dipenuhi. Contohnya, apabila bilik hotel tidak tersedia, pelaksana boleh mencadangkan pilihan lain.  

*Sisi Tukar-Kes* - Menghala mesej ke pelaksana berbeza berdasarkan syarat yang ditetapkan. Contohnya, jika pelanggan pelancongan mempunyai akses keutamaan dan tugasan mereka akan diurus melalui aliran kerja lain.  

*Sisi Penyaluran* - Hantar satu mesej ke pelbagai sasaran.  

*Sisi Pengumpulan* - Kumpul pelbagai mesej daripada pelaksana berbeza dan hantar kepada satu sasaran.  

**Peristiwa**  

Untuk menyediakan keterlihatan yang lebih baik ke dalam aliran kerja, MAF menawarkan peristiwa terbina dalam untuk pelaksanaan termasuk:  

- `WorkflowStartedEvent`  - Pelaksanaan aliran kerja bermula  
- `WorkflowOutputEvent` - Aliran kerja menghasilkan output  
- `WorkflowErrorEvent` - Aliran kerja menghadapi ralat  
- `ExecutorInvokeEvent`  - Pelaksana mula memproses  
- `ExecutorCompleteEvent`  -  Pelaksana selesai memproses  
- `RequestInfoEvent` - Permintaan dikeluarkan  

## Corak MAF Lanjutan  

Bahagian di atas merangkumi konsep utama Rangka Kerja Ejen Microsoft. Semasa anda membina ejen yang lebih kompleks, berikut adalah beberapa corak lanjutan yang perlu dipertimbangkan:  

- **Komposisi Perisian Perantaraan**: Menggabungkan berbilang pengendali perisian perantaraan (log, pengesahan, sekatan kadar) menggunakan perisian perantaraan fungsi dan sembang untuk kawalan perilaku ejen yang halus.  
- **Penandaan Semula Aliran Kerja**: Gunakan peristiwa aliran kerja dan penyusunan untuk menyimpan dan menyambung semula proses ejen yang berjalan lama.  
- **Pemilihan Alat Dinamik**: Gabungkan RAG ke atas penerangan alat dengan pendaftaran alat MAF untuk mempersembahkan hanya alat yang relevan bagi setiap pertanyaan.  
- **Penyerahan Pelbagai Ejen**: Gunakan sisi aliran kerja dan penghalaan bersyarat untuk mengatur penyerahan antara ejen khusus.  

## Mengehos Ejen LangChain / LangGraph pada Microsoft Foundry  

Rangka Kerja Ejen Microsoft adalah **interoperabel rangka kerja** — anda tidak terhad kepada ejen yang ditulis dengan MAF sahaja. Jika anda sudah mempunyai ejen yang dibina dengan **LangChain** atau **LangGraph**, anda boleh menjalankannya sebagai **ejen yang dihoskan Microsoft Foundry** supaya Foundry menguruskan runtime, sesi, penalaan skala, identiti dan titik akhir protokol untuk anda, sementara logik ejen kekal dalam LangGraph.  

Ini dilakukan dengan pakej `langchain_azure_ai.agents.hosting`, yang mendedahkan graf LangGraph terkompilasi melalui protokol yang sama yang digunakan oleh ejen hos Foundry.  

**1. Pasang tambahan hosting:**  

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```
  
Tambahan `hosting` memasang perpustakaan protokol Foundry: `azure-ai-agentserver-responses` (titik akhir `/responses` yang serasi OpenAI) dan `azure-ai-agentserver-invocations` (titik akhir `/invocations` generik).  

**2. Pilih protokol hosting:**  

| Protokol | Kelas Hos | Titik Akhir | Gunakan apabila |  
|----------|-----------|----------|----------|  
| **Responses** | `ResponsesHostServer` | `/responses` | Anda mahukan sembang serasi OpenAI, aliran penstriman, sejarah respons, dan pengurusan perbualan — lalai yang disyorkan bagi ejen perbualan. |  
| **Invocations** | `InvocationsHostServer` | `/invocations` | Anda memerlukan bentuk JSON khusus, titik akhir gaya webhook, atau pemprosesan bukan perbualan. |  

Kerana **API Responses adalah API utama untuk pembangunan gaya ejen di Foundry**, mulakan dengan `ResponsesHostServer` untuk kebanyakan ejen.  

**3. Konfigurasikan pembolehubah persekitaran** (`az login` dahulu supaya `DefaultAzureCredential` boleh mengesahkan):  

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```
  
Apabila ejen nanti dijalankan sebagai ejen hos di Foundry, platform secara automatik menyuntik `FOUNDRY_PROJECT_ENDPOINT`.  

**4. Dedahkan ejen LangGraph melalui protokol Responses:**  

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

    # ChatOpenAI di sini menyasarkan titik akhir (Responses) yang serasi dengan OpenAI bagi projek Foundry.
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
  
Jalankan secara tempatan dengan `python main.py`, kemudian hantar permintaan Responses ke `http://localhost:8088/responses`.  

**Kelakuan utama:**  

- **Perbualan**: Pelanggan menyambung perbualan dengan menghantar `previous_response_id` atau ID `conversation`. Jika graf anda dikompilasi dengan penanda semak LangGraph, Foundry mengikat status perbualan ke penanda semak (gunakan penanda semak tahan lama dalam produksi; `MemorySaver` baik untuk ujian tempatan).  
- **Manusia dalam gelung**: Jika graf anda menggunakan LangGraph `interrupt()`, `ResponsesHostServer` memaparkan gangguan tertunda sebagai item `function_call` / `mcp_approval_request` Responses, dan pelanggan menyambung dengan `function_call_output` / `mcp_approval_response` yang sepadan.  
- **Sebarkan ke Foundry**: Gunakan Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (tempatan, perlukan Docker), kemudian `azd provision` dan `azd deploy`. Penyebaran ejen hos memerlukan peranan **Foundry Project Manager**.  

Versi yang boleh dijalankan bagi contoh ini terdapat di [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Untuk panduan penuh (protokol Invocations, skema permintaan tersuai, dan penyelesaian masalah), lihat [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).  

## Contoh Kod   

Contoh kod untuk Rangka Kerja Ejen Microsoft boleh didapati dalam repositori ini di bawah fail `xx-python-agent-framework` dan `xx-dotnet-agent-framework`.  

## Ada Soalan Lagi Tentang Rangka Kerja Ejen Microsoft?  

Sertai [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) untuk bertemu dengan pelajar lain, menghadiri waktu pejabat dan dapatkan jawapan kepada soalan Ejen AI anda.  
## Pelajaran Sebelumnya  

[Memori untuk Ejen AI](../13-agent-memory/README.md)  

## Pelajaran Seterusnya  

[Membangunkan Ejen Pengguna Komputer (CUA)](../15-browser-use/README.md)  

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->