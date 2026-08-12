# Membangun Aplikasi Multi-Agen dengan Microsoft Agent Framework Workflow

Tutorial ini akan memandu Anda melalui pemahaman dan pembangunan aplikasi multi-agen menggunakan Microsoft Agent Framework. Kami akan menjelajahi konsep inti sistem multi-agen, menyelami arsitektur komponen Workflow dalam framework, dan membahas contoh praktis dalam Python dan .NET untuk berbagai pola workflow.

## 1\. Memahami Sistem Multi-Agen

Agen AI adalah sistem yang melampaui kemampuan Model Bahasa Besar (LLM) standar. Ia dapat memahami lingkungannya, membuat keputusan, dan mengambil tindakan untuk mencapai tujuan tertentu. Sistem multi-agen melibatkan beberapa agen yang bekerja sama untuk menyelesaikan masalah yang sulit atau tidak mungkin ditangani oleh satu agen saja.

### Skenario Aplikasi Umum

  * **Penyelesaian Masalah Kompleks**: Memecah tugas besar (misalnya, merencanakan acara perusahaan) menjadi sub-tugas yang lebih kecil yang ditangani oleh agen khusus (misalnya, agen anggaran, agen logistik, agen pemasaran).
  * **Asisten Virtual**: Agen asisten utama yang mendelegasikan tugas seperti penjadwalan, riset, dan pemesanan ke agen lain yang khusus.
  * **Pembuatan Konten Otomatis**: Workflow di mana satu agen membuat draf konten, agen lainnya mengulas untuk akurasi dan nada, dan yang ketiga mempublikasikannya.

### Pola Multi-Agen

Sistem multi-agen dapat diorganisasi dalam beberapa pola, yang menentukan bagaimana mereka berinteraksi:

  * **Berurutan**: Agen bekerja dalam urutan yang telah ditentukan, seperti jalur perakitan. Output dari satu agen menjadi input untuk agen berikutnya.
  * **Konkuren**: Agen bekerja secara paralel pada bagian tugas yang berbeda, dan hasil mereka dikumpulkan pada akhir proses.
  * **Kondisional**: Workflow mengikuti jalur berbeda berdasarkan output agen, mirip dengan pernyataan if-then-else.

## 2\. Arsitektur Microsoft Agent Framework Workflow

Sistem workflow pada Agent Framework adalah mesin orkestrasi canggih yang dirancang untuk mengelola interaksi kompleks antara banyak agen. Sistem ini dibangun dengan arsitektur berbasis graf yang menggunakan [model eksekusi gaya Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf), di mana pemrosesan terjadi dalam langkah sinkron yang disebut "supersteps."

### Komponen Inti

Arsitektur ini terdiri dari tiga bagian utama:

1.  **Executor**: Unit pemrosesan fundamental. Dalam contoh kami, `Agent` adalah tipe executor. Setiap executor dapat memiliki beberapa pengelola pesan yang secara otomatis dipanggil berdasarkan tipe pesan yang diterima.
2.  **Edges**: Mendefinisikan jalur yang dilalui pesan antara executor. Edge dapat memiliki kondisi, memungkinkan pengalihan informasi secara dinamis melalui graf workflow.
3.  **Workflow**: Komponen yang mengorkestrasi seluruh proses, mengelola executor, edges, dan aliran eksekusi secara keseluruhan. Ini memastikan pesan diproses dalam urutan yang benar dan menyalurkan event untuk pengamatan.

*Diagram yang menggambarkan komponen inti dari sistem workflow.*

Struktur ini memungkinkan pembangunan aplikasi yang kuat dan skalabel menggunakan pola fundamental seperti rantai berurutan, fan-out/fan-in untuk pemrosesan paralel, dan logika switch-case untuk alur kondisional.

## 3\. Contoh Praktis dan Analisis Kode

Sekarang, mari kita jelajahi bagaimana mengimplementasikan berbagai pola workflow menggunakan framework ini. Kami akan melihat kode Python dan .NET untuk setiap contoh.

### Kasus 1: Workflow Berurutan Dasar

Ini adalah pola paling sederhana, di mana output dari satu agen langsung diteruskan ke agen lain. Skenarionya melibatkan agen hotel `FrontDesk` yang memberikan rekomendasi perjalanan, yang kemudian ditinjau oleh agen `Concierge`.

*Diagram workflow dasar FrontDesk -\> Concierge.*

#### Latar Belakang Skenario

Seorang pelancong meminta rekomendasi di Paris.

1.  Agen `FrontDesk`, yang didesain singkat, menyarankan kunjungan ke Museum Louvre.
2.  Agen `Concierge`, yang memprioritaskan pengalaman otentik, menerima saran ini. Ia meninjau rekomendasi dan memberikan masukan, menyarankan alternatif yang lebih lokal dan kurang turistik.

#### Analisis Implementasi Python

Dalam contoh Python, pertama kami mendefinisikan dan membuat dua agen, masing-masing dengan instruksi spesifik.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Tentukan peran agen dan instruksi
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Buat instance agen
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Selanjutnya, `WorkflowBuilder` digunakan untuk membangun graf. Agen `front_desk_agent` ditetapkan sebagai titik awal, dan edge dibuat untuk menghubungkan outputnya ke `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Akhirnya, workflow dieksekusi dengan prompt pengguna awal.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run menjalankan alur kerja; get_outputs() mengembalikan hasil dari eksekutor output.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### Analisis Implementasi .NET (C\#)

Implementasi .NET mengikuti logika yang sangat mirip. Pertama, konstanta didefinisikan untuk nama dan instruksi agen.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Agen dibuat menggunakan `AzureOpenAIClient` (Responses API), kemudian `WorkflowBuilder` mendefinisikan aliran berurutan dengan menambahkan edge dari `frontDeskAgent` ke `reviewerAgent`.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = azureClient.GetChatClient(deployment).AsAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = azureClient.GetChatClient(deployment).AsAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

Workflow kemudian dijalankan dengan pesan pengguna, dan hasilnya dialirkan kembali.

### Kasus 2: Workflow Berurutan Multi-Langkah

Pola ini memperluas urutan dasar dengan memasukkan lebih banyak agen. Cocok untuk proses yang memerlukan beberapa tahap penyempurnaan atau transformasi.

#### Latar Belakang Skenario

Pengguna menyediakan gambar ruang tamu dan meminta kutipan furnitur.

1.  **Sales-Agent**: Mengidentifikasi barang furnitur dalam gambar dan membuat daftar.
2.  **Price-Agent**: Mengambil daftar barang dan memberikan rincian harga, termasuk opsi anggaran, menengah, dan premium.
3.  **Quote-Agent**: Menerima daftar berharga dan memformatnya dalam dokumen kutipan resmi dalam Markdown.

*Diagram workflow Sales -\> Price -\> Quote.*

#### Analisis Implementasi Python

Tiga agen didefinisikan, masing-masing dengan peran khusus. Workflow dibangun menggunakan `add_edge` untuk membuat rantai: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Buat tiga agen khusus
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Bangun alur kerja berurutan
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Input-nya adalah `ChatMessage` yang mencakup teks dan URI gambar. Framework menangani penerusan output setiap agen ke agen berikutnya dalam urutan sampai kutipan akhir dihasilkan.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Pesan pengguna berisi teks dan gambar
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Jalankan alur kerja
events = await workflow.run(message)
```

#### Analisis Implementasi .NET (C\#)

Contoh .NET mencerminkan versi Python. Tiga agen (`salesagent`, `priceagent`, `quoteagent`) dibuat. `WorkflowBuilder` menghubungkan mereka secara berurutan.

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = azureClient.GetChatClient(deployment).AsAIAgent(...);
AIAgent priceagent  = azureClient.GetChatClient(deployment).AsAIAgent(...);
AIAgent quoteagent = azureClient.GetChatClient(deployment).AsAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

Pesan pengguna dibuat dengan data gambar (dalam byte) dan prompt teks. Metode `InProcessExecution.RunStreamingAsync` memulai workflow, dan output akhir diambil dari stream.

### Kasus 3: Workflow Konkuren

Pola ini digunakan saat tugas dapat dijalankan bersamaan untuk menghemat waktu. Melibatkan "fan-out" ke beberapa agen dan "fan-in" untuk menggabungkan hasil.

#### Latar Belakang Skenario

Seorang pengguna meminta perencanaan perjalanan ke Seattle.

1.  **Dispatcher (Fan-Out)**: Permintaan pengguna dikirim ke dua agen secara bersamaan.
2.  **Researcher-Agent**: Meneliti atraksi, cuaca, dan pertimbangan utama untuk perjalanan ke Seattle pada bulan Desember.
3.  **Plan-Agent**: Secara mandiri membuat rencana perjalanan harian terperinci.
4.  **Aggregator (Fan-In)**: Output dari peneliti dan perencana dikumpulkan dan disajikan bersama sebagai hasil akhir.

*Diagram workflow konkuren Researcher dan Planner.*

#### Analisis Implementasi Python

`ConcurrentBuilder` mempermudah pembuatan pola ini. Anda hanya menyebutkan agen yang terlibat, dan builder otomatis membuat logika fan-out dan fan-in yang diperlukan.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder menangani logika fan-out/fan-in
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Jalankan workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Framework memastikan bahwa `research_agent` dan `plan_agent` dieksekusi paralel, dan output akhir mereka dikumpulkan ke dalam sebuah daftar.

#### Analisis Implementasi .NET (C\#)

Di .NET, pola ini memerlukan definisi yang lebih eksplisit. Executor kustom (`ConcurrentStartExecutor` dan `ConcurrentAggregationExecutor`) dibuat untuk menangani logika fan-out dan fan-in.

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

`WorkflowBuilder` kemudian menggunakan `AddFanOutEdge` dan `AddFanInEdge` untuk membangun graf dengan executor khusus dan agen-agen tersebut.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Kasus 4: Workflow Kondisional

Workflow kondisional memperkenalkan logika cabang, memungkinkan sistem mengambil jalur berbeda berdasarkan hasil antara.

#### Latar Belakang Skenario

Workflow ini mengotomatisasi pembuatan dan publikasi tutorial teknis.

1.  **Evangelist-Agent**: Menulis draf tutorial berdasarkan outline dan URL yang diberikan.
2.  **ContentReviewer-Agent**: Meninjau draf. Memeriksa apakah jumlah kata melebihi 200 kata.
3.  **Cabang Kondisional**:
      * **Jika Disetujui (`Yes`)**: Workflow melanjutkan ke `Publisher-Agent`.
      * **Jika Ditolak (`No`)**: Workflow berhenti dan mengeluarkan alasan penolakan.
4.  **Publisher-Agent**: Jika draf disetujui, agen ini menyimpan konten ke file Markdown.

#### Analisis Implementasi Python

Contoh ini menggunakan fungsi kustom, `select_targets`, untuk mengimplementasikan logika kondisional. Fungsi ini dipassing ke `add_multi_selection_edge_group` dan mengarahkan workflow berdasarkan field `review_result` dari output reviewer.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Fungsi ini menentukan langkah selanjutnya berdasarkan hasil tinjauan
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Jika disetujui, lanjutkan ke eksekutor 'save_draft'
        return [save_draft_id]
    else:
        # Jika ditolak, lanjutkan ke eksekutor 'handle_review' untuk melaporkan kegagalan
        return [handle_review_id]

# Pembuat alur kerja menggunakan fungsi seleksi untuk routing
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Edge multi-seleksi mengimplementasikan logika kondisional
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Executor khusus seperti `to_reviewer_result` digunakan untuk mengurai output JSON dari agen dan mengubahnya menjadi objek bertipe kuat yang dapat diperiksa oleh fungsi seleksi.

#### Analisis Implementasi .NET (C\#)

Versi .NET menggunakan pendekatan serupa dengan fungsi kondisi. Sebuah `Func<object?, bool>` didefinisikan untuk memeriksa properti `Result` dalam objek `ReviewResult`.

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

Parameter `condition` dari metode `AddEdge` memungkinkan `WorkflowBuilder` membuat jalur cabang. Workflow hanya mengikuti edge ke `publishExecutor` jika kondisi `GetCondition(expectedResult: "Yes")` bernilai true. Jika tidak, ia mengikuti jalur ke `sendReviewerExecutor`.

## Kesimpulan

Microsoft Agent Framework Workflow menyediakan fondasi yang kuat dan fleksibel untuk mengorkestrasi sistem multi-agen yang kompleks. Dengan memanfaatkan arsitektur berbasis graf dan komponen inti, pengembang dapat merancang dan mengimplementasikan workflow canggih dalam Python maupun .NET. Apakah aplikasi Anda membutuhkan pemrosesan berurutan sederhana, eksekusi paralel, atau logika kondisional dinamis, framework ini menawarkan alat untuk membangun solusi AI yang kuat, skalabel, dan aman tipe.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->