# Membangun Aplikasi Multi-Agent dengan Microsoft Agent Framework Workflow

Tutorial ini akan memandu Anda memahami dan membangun aplikasi multi-agent menggunakan Microsoft Agent Framework. Kita akan menjelajahi konsep inti dari sistem multi-agent, mendalami arsitektur komponen Workflow dari framework ini, dan mempelajari contoh praktis dalam Python dan .NET untuk berbagai pola workflow.

## 1\. Memahami Sistem Multi-Agent

Agent AI adalah sistem yang melampaui kemampuan Model Bahasa Besar (LLM) standar. Agent ini dapat memahami lingkungannya, membuat keputusan, dan mengambil tindakan untuk mencapai tujuan tertentu. Sistem multi-agent melibatkan beberapa agent yang bekerja sama untuk menyelesaikan masalah yang sulit atau tidak mungkin ditangani oleh satu agent saja.

### Skenario Aplikasi Umum

  * **Penyelesaian Masalah Kompleks**: Memecah tugas besar (misalnya, merencanakan acara perusahaan) menjadi sub-tugas yang ditangani oleh agent khusus (misalnya, agent anggaran, agent logistik, agent pemasaran).
  * **Asisten Virtual**: Agent asisten utama yang mendelegasikan tugas seperti penjadwalan, penelitian, dan pemesanan kepada agent khusus lainnya.
  * **Pembuatan Konten Otomatis**: Workflow di mana satu agent membuat draf konten, agent lain meninjau akurasi dan nada, dan agent ketiga mempublikasikannya.

### Pola Multi-Agent

Sistem multi-agent dapat diorganisasikan dalam beberapa pola, yang menentukan cara mereka berinteraksi:

  * **Sequential (Berurutan)**: Agent bekerja dalam urutan yang telah ditentukan, seperti jalur perakitan. Output dari satu agent menjadi input untuk agent berikutnya.
  * **Concurrent (Bersamaan)**: Agent bekerja secara paralel pada bagian-bagian berbeda dari tugas, dan hasilnya digabungkan di akhir.
  * **Conditional (Bersyarat)**: Workflow mengikuti jalur yang berbeda berdasarkan output dari agent, mirip dengan pernyataan if-then-else.

## 2\. Arsitektur Workflow Microsoft Agent Framework

Sistem workflow dari Agent Framework adalah mesin orkestrasi canggih yang dirancang untuk mengelola interaksi kompleks antara banyak agent. Sistem ini dibangun di atas arsitektur berbasis graf yang menggunakan [model eksekusi gaya Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf), di mana pemrosesan terjadi dalam langkah-langkah tersinkronisasi yang disebut "supersteps."

### Komponen Inti

Arsitektur ini terdiri dari tiga bagian utama:

1.  **Executors**: Unit pemrosesan dasar. Dalam contoh kita, `Agent` adalah jenis executor. Setiap executor dapat memiliki beberapa handler pesan yang secara otomatis dipanggil berdasarkan jenis pesan yang diterima.
2.  **Edges**: Mendefinisikan jalur yang dilalui pesan antar executor. Edges dapat memiliki kondisi, memungkinkan pengalihan informasi secara dinamis melalui graf workflow.
3.  **Workflow**: Komponen ini mengorkestrasi seluruh proses, mengelola executor, edges, dan alur eksekusi secara keseluruhan. Workflow memastikan pesan diproses dalam urutan yang benar dan mengalirkan event untuk observabilitas.

*Sebuah diagram yang menggambarkan komponen inti dari sistem workflow.*

Struktur ini memungkinkan pembangunan aplikasi yang kuat dan skalabel menggunakan pola dasar seperti rantai berurutan, fan-out/fan-in untuk pemrosesan paralel, dan logika switch-case untuk alur bersyarat.

## 3\. Contoh Praktis dan Analisis Kode

Sekarang, mari kita pelajari cara mengimplementasikan berbagai pola workflow menggunakan framework ini. Kita akan melihat kode dalam Python dan .NET untuk setiap contoh.

### Kasus 1: Workflow Berurutan Dasar

Ini adalah pola paling sederhana, di mana output dari satu agent langsung diteruskan ke agent lain. Skenario kita melibatkan agent `FrontDesk` hotel yang memberikan rekomendasi perjalanan, yang kemudian ditinjau oleh agent `Concierge`.

*Diagram workflow dasar FrontDesk -\> Concierge.*

#### Latar Belakang Skenario

Seorang pelancong meminta rekomendasi di Paris.

1.  Agent `FrontDesk`, yang dirancang untuk memberikan jawaban singkat, menyarankan mengunjungi Museum Louvre.
2.  Agent `Concierge`, yang memprioritaskan pengalaman autentik, menerima saran ini. Agent ini meninjau rekomendasi dan memberikan umpan balik, menyarankan alternatif yang lebih lokal dan tidak terlalu turistik.

#### Analisis Implementasi Python

Dalam contoh Python, kita pertama-tama mendefinisikan dan membuat dua agent, masing-masing dengan instruksi spesifik.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Define agent roles and instructions
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Create agent instances
reviewer_agent = chat_client.create_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.create_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Selanjutnya, `WorkflowBuilder` digunakan untuk membangun graf. `front_desk_agent` ditetapkan sebagai titik awal, dan sebuah edge dibuat untuk menghubungkan output-nya ke `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Akhirnya, workflow dijalankan dengan prompt awal dari pengguna.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### Analisis Implementasi .NET (C#)

Implementasi .NET mengikuti logika yang sangat mirip. Pertama, konstanta didefinisikan untuk nama dan instruksi agent.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Agent dibuat menggunakan `OpenAIClient`, lalu `WorkflowBuilder` mendefinisikan alur berurutan dengan menambahkan edge dari `frontDeskAgent` ke `reviewerAgent`.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = openAIClient.GetChatClient(github_model_id).CreateAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

Workflow kemudian dijalankan dengan pesan pengguna, dan hasilnya dialirkan kembali.

### Kasus 2: Workflow Berurutan Multi-Langkah

Pola ini memperluas urutan dasar untuk menyertakan lebih banyak agent. Pola ini ideal untuk proses yang memerlukan beberapa tahap penyempurnaan atau transformasi.

#### Latar Belakang Skenario

Seorang pengguna memberikan gambar ruang tamu dan meminta penawaran harga furnitur.

1.  **Sales-Agent**: Mengidentifikasi item furnitur dalam gambar dan membuat daftar.
2.  **Price-Agent**: Mengambil daftar item dan memberikan rincian harga, termasuk opsi anggaran, menengah, dan premium.
3.  **Quote-Agent**: Menerima daftar harga dan memformatnya menjadi dokumen penawaran resmi dalam Markdown.

*Diagram workflow Sales -\> Price -\> Quote.*

#### Analisis Implementasi Python

Tiga agent didefinisikan, masing-masing dengan peran khusus. Workflow dibangun menggunakan `add_edge` untuk membuat rantai: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Input adalah `ChatMessage` yang mencakup teks dan URI gambar. Framework menangani pengiriman output dari setiap agent ke agent berikutnya dalam urutan hingga penawaran akhir dihasilkan.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# The user message contains both text and an image
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Run the workflow
async for event in workflow.run_stream(message):
    ...
```

#### Analisis Implementasi .NET (C#)

Contoh .NET mencerminkan versi Python. Tiga agent (`salesagent`, `priceagent`, `quoteagent`) dibuat. `WorkflowBuilder` menghubungkan mereka secara berurutan.

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);
AIAgent priceagent  = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);
AIAgent quoteagent = openAIClient.GetChatClient(github_model_id).CreateAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

Pesan pengguna dibuat dengan data gambar (sebagai byte) dan prompt teks. Metode `InProcessExecution.StreamAsync` memulai workflow, dan output akhir diambil dari stream.

### Kasus 3: Workflow Bersamaan

Pola ini digunakan ketika tugas dapat dilakukan secara bersamaan untuk menghemat waktu. Pola ini melibatkan "fan-out" ke beberapa agent dan "fan-in" untuk menggabungkan hasil.

#### Latar Belakang Skenario

Seorang pengguna meminta rencana perjalanan ke Seattle.

1.  **Dispatcher (Fan-Out)**: Permintaan pengguna dikirim ke dua agent secara bersamaan.
2.  **Researcher-Agent**: Meneliti atraksi, cuaca, dan pertimbangan utama untuk perjalanan ke Seattle pada bulan Desember.
3.  **Plan-Agent**: Secara independen membuat rencana perjalanan harian yang terperinci.
4.  **Aggregator (Fan-In)**: Output dari peneliti dan perencana dikumpulkan dan disajikan bersama sebagai hasil akhir.

*Diagram workflow bersamaan Researcher dan Planner.*

#### Analisis Implementasi Python

`ConcurrentBuilder` menyederhanakan pembuatan pola ini. Anda cukup mencantumkan agent yang berpartisipasi, dan builder secara otomatis membuat logika fan-out dan fan-in yang diperlukan.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Framework memastikan bahwa `research_agent` dan `plan_agent` dijalankan secara paralel, dan output akhir mereka dikumpulkan ke dalam daftar.

#### Analisis Implementasi .NET (C#)

Dalam .NET, pola ini memerlukan definisi yang lebih eksplisit. Executor khusus (`ConcurrentStartExecutor` dan `ConcurrentAggregationExecutor`) dibuat untuk menangani logika fan-out dan fan-in.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

// Custom executor to broadcast the message to all agents
public class ConcurrentStartExecutor() : ...
{
    public async ValueTask HandleAsync(string message, IWorkflowContext context)
    {
        // Send message to all connected agents
        await context.SendMessageAsync(new ChatMessage(ChatRole.User, message));
        // Send a token to start processing
        await context.SendMessageAsync(new TurnToken(emitEvents: true));
    }
}

// Custom executor to collect results
public class ConcurrentAggregationExecutor() : ...
{
    private readonly List<ChatMessage> _messages = [];
    public async ValueTask HandleAsync(ChatMessage message, IWorkflowContext context)
    {
        this._messages.Add(message);
        // Once both agents have responded, yield the final output
        if (this._messages.Count == 2)
        {
            ...
            await context.YieldOutputAsync(formattedMessages);
        }
    }
}
```

`WorkflowBuilder` kemudian menggunakan `AddFanOutEdge` dan `AddFanInEdge` untuk membangun graf dengan executor khusus ini dan agent.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Kasus 4: Workflow Bersyarat

Workflow bersyarat memperkenalkan logika bercabang, memungkinkan sistem mengambil jalur berbeda berdasarkan hasil antara.

#### Latar Belakang Skenario

Workflow ini mengotomatisasi pembuatan dan publikasi tutorial teknis.

1.  **Evangelist-Agent**: Menulis draf tutorial berdasarkan outline dan URL yang diberikan.
2.  **ContentReviewer-Agent**: Meninjau draf. Agent ini memeriksa apakah jumlah kata lebih dari 200.
3.  **Cabang Bersyarat**:
      * **Jika Disetujui (`Yes`)**: Workflow dilanjutkan ke `Publisher-Agent`.
      * **Jika Ditolak (`No`)**: Workflow berhenti dan memberikan alasan penolakan.
4.  **Publisher-Agent**: Jika draf disetujui, agent ini menyimpan konten ke file Markdown.

#### Analisis Implementasi Python

Contoh ini menggunakan fungsi khusus, `select_targets`, untuk mengimplementasikan logika bersyarat. Fungsi ini diteruskan ke `add_multi_selection_edge_group` dan mengarahkan workflow berdasarkan field `review_result` dari output reviewer.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# This function determines the next step based on the review result
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # If approved, proceed to the 'save_draft' executor
        return [save_draft_id]
    else:
        # If rejected, proceed to the 'handle_review' executor to report failure
        return [handle_review_id]

# The workflow builder uses the selection function for routing
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # The multi-selection edge implements the conditional logic
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Executor khusus seperti `to_reviewer_result` digunakan untuk mem-parsing output JSON dari agent dan mengonversinya menjadi objek bertipe kuat yang dapat diperiksa oleh fungsi seleksi.

#### Analisis Implementasi .NET (C#)

Versi .NET menggunakan pendekatan serupa dengan fungsi kondisi. Sebuah `Func<object?, bool>` didefinisikan untuk memeriksa properti `Result` dari objek `ReviewResult`.

```csharp
// 04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb

// This function creates a lambda for the condition check
public Func<object?, bool> GetCondition(string expectedResult) =>
        reviewResult => reviewResult is ReviewResult review && review.Result == expectedResult;

// The workflow is built with conditional edges
var workflow = new WorkflowBuilder(draftExecutor)
            .AddEdge(draftExecutor, contentReviewerExecutor)
            // Add an edge to the publisher only if the review result is "Yes"
            .AddEdge(contentReviewerExecutor, publishExecutor, condition: GetCondition(expectedResult: "Yes"))
            // Add an edge to the reviewer feedback executor if the result is "No"
            .AddEdge(contentReviewerExecutor, sendReviewerExecutor, condition: GetCondition(expectedResult: "No"))
            .Build();
```

Parameter `condition` dari metode `AddEdge` memungkinkan `WorkflowBuilder` membuat jalur bercabang. Workflow hanya akan mengikuti edge ke `publishExecutor` jika kondisi `GetCondition(expectedResult: "Yes")` mengembalikan nilai true. Jika tidak, workflow mengikuti jalur ke `sendReviewerExecutor`.

## Kesimpulan

Microsoft Agent Framework Workflow menyediakan fondasi yang kuat dan fleksibel untuk mengorkestrasi sistem multi-agent yang kompleks. Dengan memanfaatkan arsitektur berbasis graf dan komponen intinya, pengembang dapat merancang dan mengimplementasikan workflow canggih dalam Python maupun .NET. Apakah aplikasi Anda memerlukan pemrosesan berurutan sederhana, eksekusi paralel, atau logika bersyarat yang dinamis, framework ini menawarkan alat untuk membangun solusi AI yang kuat, skalabel, dan aman secara tipe.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.