# Membangun Aplikasi Multi-Agen dengan Alur Kerja Microsoft Agent Framework

Tutorial ini akan memandu Anda memahami dan membangun aplikasi multi-agen menggunakan Microsoft Agent Framework. Kami akan mengeksplorasi konsep inti dari sistem multi-agen, menyelami arsitektur komponen Alur Kerja dari framework ini, dan memandu Anda melalui contoh praktis dalam Python dan .NET untuk berbagai pola alur kerja.

## 1\. Memahami Sistem Multi-Agen

Agen AI adalah sistem yang melampaui kemampuan Model Bahasa Besar (LLM) standar. Agen tersebut dapat memahami lingkungannya, membuat keputusan, dan mengambil tindakan untuk mencapai tujuan tertentu. Sistem multi-agen melibatkan beberapa agen ini yang bekerja sama untuk menyelesaikan masalah yang sulit atau tidak mungkin ditangani oleh satu agen saja.

### Skenario Aplikasi Umum

  * **Pemecahan Masalah Kompleks**: Memecah tugas besar (misalnya, merencanakan acara perusahaan) menjadi sub-tugas yang lebih kecil yang ditangani oleh agen spesialis (misalnya, agen anggaran, agen logistik, agen pemasaran).
  * **Asisten Virtual**: Agen asisten utama yang mendelegasikan tugas seperti penjadwalan, riset, dan pemesanan kepada agen spesialis lain.
  * **Pembuatan Konten Otomatis**: Sebuah alur kerja di mana satu agen membuat draft konten, agen lain meninjau untuk akurasi dan nada, dan agen ketiga mempublikasikannya.

### Pola Multi-Agen

Sistem multi-agen dapat diorganisasikan dalam beberapa pola yang menentukan bagaimana mereka berinteraksi:

  * **Berurutan**: Agen bekerja dalam urutan yang telah ditentukan, seperti lini perakitan. Output dari satu agen menjadi input bagi agen berikutnya.
  * **Paralel**: Agen bekerja secara bersamaan pada bagian berbeda dari sebuah tugas, dan hasil mereka digabungkan di akhir.
  * **Kondisional**: Alur kerja mengikuti jalur berbeda berdasarkan output dari agen, mirip dengan pernyataan if-then-else.

## 2\. Arsitektur Alur Kerja Microsoft Agent Framework

Sistem alur kerja Agent Framework adalah mesin orkestrasi canggih yang dirancang untuk mengelola interaksi kompleks antara beberapa agen. Ini dibangun dengan arsitektur berbasis grafik yang menggunakan [model eksekusi gaya Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf), di mana pemrosesan berlangsung dalam langkah sinkron yang disebut "supersteps."

### Komponen Inti

Arsitektur terdiri dari tiga bagian utama:

1.  **Executor**: Unit pemrosesan dasar. Dalam contoh kami, `Agent` adalah tipe executor. Setiap executor dapat memiliki banyak penangkap pesan yang otomatis dipanggil berdasarkan tipe pesan yang diterima.
2.  **Edges**: Menentukan jalur pesan antara executor. Edges dapat memiliki kondisi, memungkinkan routing informasi dinamis melalui grafik alur kerja.
3.  **Workflow**: Komponen ini mengorkestrasi seluruh proses, mengelola executor, edges, dan keseluruhan aliran eksekusi. Ini memastikan bahwa pesan diproses dalam urutan yang benar dan menyiarkan event untuk observabilitas.

*Diagram yang menggambarkan komponen inti dari sistem alur kerja.*

Struktur ini memungkinkan membangun aplikasi yang kokoh dan skalabel menggunakan pola fundamental seperti rantai berurutan, fan-out/fan-in untuk pemrosesan paralel, dan logika switch-case untuk aliran kondisional.

## 3\. Contoh Praktis dan Analisis Kode

Sekarang, mari kita jelajahi cara mengimplementasikan berbagai pola alur kerja menggunakan framework ini. Kita akan melihat kode Python dan .NET untuk setiap contoh.

### Kasus 1: Alur Kerja Berurutan Dasar

Ini adalah pola paling sederhana, di mana output satu agen langsung diteruskan ke agen lain. Skenario kita melibatkan agen `FrontDesk` hotel yang memberikan rekomendasi perjalanan, yang kemudian ditinjau oleh agen `Concierge`.

*Diagram alur kerja dasar FrontDesk -\> Concierge.*

#### Latar Belakang Skenario

Seorang pelancong meminta rekomendasi di Paris.

1.  Agen `FrontDesk`, yang dirancang untuk ringkas, menyarankan mengunjungi Museum Louvre.
2.  Agen `Concierge`, yang mengutamakan pengalaman otentik, menerima saran ini. Dia meninjau rekomendasi dan memberikan umpan balik, menyarankan alternatif yang lebih lokal dan tidak terlalu turistik.

#### Analisis Implementasi Python

Dalam contoh Python, kita pertama mendefinisikan dan membuat dua agen, masing-masing dengan instruksi spesifik.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Definisikan peran dan instruksi agen
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Buat instansi agen
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Selanjutnya, `WorkflowBuilder` digunakan untuk membangun grafik. `front_desk_agent` ditetapkan sebagai titik awal, dan dibuat edge yang menghubungkan outputnya ke `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Akhirnya, alur kerja dieksekusi dengan prompt awal dari pengguna.

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
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Agen dibuat menggunakan `AzureOpenAIClient` (Responses API), lalu `WorkflowBuilder` mendefinisikan alur berurutan dengan menambahkan edge dari `frontDeskAgent` ke `reviewerAgent`.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

// Create AIAgent instances
AIAgent reviewerAgent = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(
    name:ReviewerAgentName,instructions:ReviewerAgentInstructions);
AIAgent frontDeskAgent  = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(
    name:FrontDeskAgentName,instructions:FrontDeskAgentInstructions);

// Build the workflow
var workflow = new WorkflowBuilder(frontDeskAgent)
            .AddEdge(frontDeskAgent, reviewerAgent)
            .Build();
```

Alur kerja kemudian dijalankan dengan pesan dari pengguna, dan hasilnya dialirkan kembali.

### Kasus 2: Alur Kerja Berurutan Multi-Langkah

Pola ini memperluas urutan dasar dengan lebih banyak agen. Ini ideal untuk proses yang memerlukan beberapa tahap penyempurnaan atau transformasi.

#### Latar Belakang Skenario

Seorang pengguna menyediakan gambar ruang tamu dan meminta penawaran furnitur.

1.  **Sales-Agent**: Mengidentifikasi barang furnitur dalam gambar dan membuat daftar.
2.  **Price-Agent**: Mengambil daftar barang dan memberikan rincian harga, termasuk opsi anggaran, menengah, dan premium.
3.  **Quote-Agent**: Menerima daftar berharga dan memformatnya menjadi dokumen penawaran formal dalam Markdown.

*Diagram alur kerja Sales -\> Price -\> Quote.*

#### Analisis Implementasi Python

Tiga agen didefinisikan, masing-masing dengan peran khusus. Alur kerja dibuat menggunakan `add_edge` untuk membuat rantai: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Buat tiga agen khusus
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Bangun alur kerja berurutan
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Input adalah `ChatMessage` yang mencakup teks dan URI gambar. Framework menangani penerusan output setiap agen ke agen berikutnya dalam urutan sampai penawaran akhir dibuat.

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

Contoh .NET mencerminkan versi Python. Tiga agen (`salesagent`, `priceagent`, `quoteagent`) dibuat. `WorkflowBuilder` menautkan mereka secara berurutan.

```csharp
// 02.dotnet-agent-framework-workflow-ghmodel-sequential.ipynb

// Create agent instances
AIAgent salesagent = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(...);
AIAgent priceagent  = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(...);
AIAgent quoteagent = azureClient.GetOpenAIResponseClient(deployment).CreateAIAgent(...);

// Build the workflow by adding edges sequentially
var workflow = new WorkflowBuilder(salesagent)
            .AddEdge(salesagent,priceagent)
            .AddEdge(priceagent, quoteagent)
            .Build();
```

Pesan pengguna dibangun dengan data gambar (dalam bentuk byte) dan teks prompt. Metode `InProcessExecution.StreamAsync` memulai alur kerja, dan output akhir ditangkap dari stream.

### Kasus 3: Alur Kerja Paralel

Pola ini digunakan saat tugas dapat dilakukan secara bersamaan untuk menghemat waktu. Melibatkan "fan-out" ke beberapa agen dan "fan-in" untuk menggabungkan hasil.

#### Latar Belakang Skenario

Seorang pengguna meminta merencanakan perjalanan ke Seattle.

1.  **Dispatcher (Fan-Out)**: Permintaan pengguna dikirim ke dua agen secara bersamaan.
2.  **Researcher-Agent**: Meneliti atraksi, cuaca, dan pertimbangan utama untuk perjalanan ke Seattle di bulan Desember.
3.  **Plan-Agent**: Secara mandiri membuat rencana perjalanan rinci hari demi hari.
4.  **Aggregator (Fan-In)**: Output dari peneliti dan perencana dikumpulkan dan disajikan bersama sebagai hasil akhir.

*Diagram alur kerja paralel Researcher dan Planner.*

#### Analisis Implementasi Python

`ConcurrentBuilder` mempermudah pembuatan pola ini. Anda hanya perlu mendaftarkan agen yang berpartisipasi, dan builder secara otomatis membuat logika fan-out dan fan-in yang diperlukan.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder menangani logika fan-out/fan-in
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Jalankan alur kerja
events = await workflow.run("Plan a trip to Seattle in December")
```

Framework memastikan bahwa `research_agent` dan `plan_agent` berjalan paralel, dan output akhir mereka dikumpulkan menjadi sebuah daftar.

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

`WorkflowBuilder` kemudian menggunakan `AddFanOutEdge` dan `AddFanInEdge` untuk membangun grafik dengan executor kustom ini dan agen-agen tersebut.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Kasus 4: Alur Kerja Kondisional

Alur kerja kondisional memperkenalkan logika cabang, memungkinkan sistem mengambil jalur berbeda berdasarkan hasil sementara.

#### Latar Belakang Skenario

Alur kerja ini mengotomatisasi pembuatan dan publikasi tutorial teknis.

1.  **Evangelist-Agent**: Menulis draft tutorial berdasarkan kerangka dan URL yang diberikan.
2.  **ContentReviewer-Agent**: Meninjau draft. Memeriksa jika jumlah kata lebih dari 200 kata.
3.  **Cabang Kondisional**:
      * **Jika Disetujui (`Ya`)**: Alur kerja lanjut ke `Publisher-Agent`.
      * **Jika Ditolak (`Tidak`)**: Alur kerja berhenti dan mengeluarkan alasan penolakan.
4.  **Publisher-Agent**: Jika draft disetujui, agen ini menyimpan konten ke file Markdown.

#### Analisis Implementasi Python

Contoh ini menggunakan fungsi kustom, `select_targets`, untuk mengimplementasikan logika kondisional. Fungsi ini diberikan ke `add_multi_selection_edge_group` dan mengarahkan alur kerja berdasarkan field `review_result` dari output reviewer.

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

# Pembuat workflow menggunakan fungsi seleksi untuk pengalihan
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

Executor kustom seperti `to_reviewer_result` digunakan untuk mengurai output JSON dari agen dan mengubahnya menjadi objek bertipe kuat yang bisa diperiksa oleh fungsi seleksi.

#### Analisis Implementasi .NET (C\#)

Versi .NET menggunakan pendekatan serupa dengan fungsi kondisi. `Func<object?, bool>` didefinisikan untuk memeriksa properti `Result` dari objek `ReviewResult`.

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

Parameter `condition` dari metode `AddEdge` memungkinkan `WorkflowBuilder` membuat jalur bercabang. Alur kerja hanya mengikuti edge ke `publishExecutor` jika kondisi `GetCondition(expectedResult: "Yes")` mengembalikan true. Jika tidak, mengikuti jalur ke `sendReviewerExecutor`.

## Kesimpulan

Microsoft Agent Framework Workflow menyediakan fondasi yang kokoh dan fleksibel untuk mengorkestrasi sistem multi-agen yang kompleks. Dengan memanfaatkan arsitektur berbasis grafik dan komponen inti, pengembang dapat merancang dan mengimplementasikan alur kerja canggih dalam Python dan .NET. Apakah aplikasi Anda memerlukan pemrosesan berurutan sederhana, eksekusi paralel, atau logika kondisional dinamis, framework ini menawarkan alat untuk membangun solusi AI yang kuat, skalabel, dan aman tipe.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->