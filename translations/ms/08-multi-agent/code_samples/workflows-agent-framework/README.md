# Membangun Aplikasi Multi-Ejen dengan Aliran Kerja Microsoft Agent Framework

Tutorial ini akan membimbing anda melalui pemahaman dan pembinaan aplikasi multi-ejen menggunakan Microsoft Agent Framework. Kami akan meneroka konsep teras sistem multi-ejen, menyelami seni bina komponen Aliran Kerja framework, dan melalui contoh praktikal dalam Python dan .NET untuk pelbagai corak aliran kerja.

## 1\. Memahami Sistem Multi-Ejen

Ejen AI ialah sistem yang melebihi keupayaan Model Bahasa Besar (LLM) standard. Ia boleh melihat persekitarannya, membuat keputusan, dan mengambil tindakan untuk mencapai matlamat tertentu. Sistem multi-ejen melibatkan beberapa ejen ini yang bekerjasama menyelesaikan masalah yang sukar atau mustahil untuk ejen tunggal tangani secara bersendirian.

### Senario Aplikasi Biasa

  * **Penyelesaian Masalah Kompleks**: Memecahkan tugasan besar (contohnya, merancang acara syarikat secara menyeluruh) kepada sub-tugasan yang lebih kecil yang dikendalikan oleh ejen khusus (contohnya, ejen bajet, ejen logistik, ejen pemasaran).
  * **Pembantu Maya**: Ejen pembantu utama mendelegasikan tugasan seperti penjadualan, penyelidikan dan tempahan kepada ejen khusus lain.
  * **Penciptaan Kandungan Automatik**: Aliran kerja di mana satu ejen merangka kandungan, satu lagi menyemak ketepatan dan nada, dan satu lagi menerbitkannya.

### Corak Multi-Ejen

Sistem multi-ejen boleh disusun dalam beberapa corak, yang menentukan bagaimana mereka berinteraksi:

  * **Berturutan**: Ejen bekerja dalam urutan yang telah ditetapkan, seperti barisan pemasangan. Output satu ejen menjadi input untuk ejen berikutnya.
  * **Selari**: Ejen bekerja serentak pada bahagian tugasan yang berbeza, dan hasil mereka digabung pada akhirnya.
  * **Bersyarat**: Aliran kerja mengikuti laluan berbeza berdasarkan output ejen, mirip kepada pernyataan if-then-else.

## 2\. Seni Bina Aliran Kerja Microsoft Agent Framework

Sistem aliran kerja Agent Framework ialah enjin orkestrasi canggih yang direka untuk mengurus interaksi kompleks antara pelbagai ejen. Ia dibina pada seni bina berasaskan graf yang menggunakan [model pelaksanaan gaya Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf), di mana pemprosesan berlaku dalam langkah serentak yang dipanggil "supersteps."

### Komponen Teras

Seni bina terdiri daripada tiga bahagian utama:

1.  **Pelaksana**: Ini adalah unit pemprosesan asas. Dalam contoh kami, `Agent` ialah sejenis pelaksana. Setiap pelaksana boleh mempunyai beberapa pengendali mesej yang dipanggil secara automatik berdasarkan jenis mesej yang diterima.
2.  **Tepi**: Ini menentukan laluan mesej antara pelaksana. Tepi boleh mempunyai syarat, membenarkan penghalaan maklumat secara dinamik melalui graf aliran kerja.
3.  **Aliran Kerja**: Komponen ini mengatur keseluruhan proses, mengurus pelaksana, tepi, dan aliran pelaksanaan keseluruhan. Ia memastikan mesej diproses dalam urutan betul dan menstrim acara untuk pemerhatian.

*Rajah yang menggambarkan komponen teras sistem aliran kerja.*

Struktur ini membolehkan pembinaan aplikasi yang kukuh dan boleh diskala menggunakan corak asas seperti rantai berturutan, fan-out/fan-in untuk pemprosesan selari, dan logik suis-kes untuk aliran bersyarat.

## 3\. Contoh Praktikal dan Analisis Kod

Sekarang, mari kita terokai bagaimana melaksanakan corak aliran kerja yang berbeza menggunakan framework. Kami akan melihat kod Python dan .NET untuk setiap contoh.

### Kes 1: Aliran Kerja Berturutan Asas

Ini adalah corak paling mudah, di mana output satu ejen dipindahkan terus kepada ejen lain. Senario kami melibatkan ejen `FrontDesk` hotel yang membuat cadangan perjalanan, yang kemudian disemak oleh ejen `Concierge`.

*Rajah aliran kerja asas FrontDesk -\> Concierge.*

#### Latar Belakang Senario

Seorang pengembara meminta cadangan di Paris.

1.  Ejen `FrontDesk`, yang direka untuk ringkas, mencadangkan melawat Muzium Louvre.
2.  Ejen `Concierge`, yang mengutamakan pengalaman autentik, menerima cadangan ini. Ia menyemak cadangan dan memberi maklum balas, mencadangkan alternatif yang lebih tempatan dan kurang pelancong.

#### Analisis Pelaksanaan Python

Dalam contoh Python, kami mula-mula mentakrif dan mencipta dua ejen, masing-masing dengan arahan khusus.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Takrifkan peranan ejen dan arahan
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Cipta contoh ejen
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Seterusnya, `WorkflowBuilder` digunakan untuk membina graf. `front_desk_agent` ditetapkan sebagai titik mula, dan satu tepi dibuat untuk menyambungkan outputnya kepada `reviewer_agent`.

```python
# 01.python-agent-framework-aliran-kerja-ghmodel-asas.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Akhirnya, aliran kerja dijalankan dengan prompt pengguna awal.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run melaksanakan aliran kerja; get_outputs() memulangkan hasil pelaksana output.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### Analisis Pelaksanaan .NET (C\#)

Pelaksanaan .NET mengikuti logik yang sangat serupa. Pertama, konstanta ditakrifkan untuk nama dan arahan ejen.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Ejen dicipta menggunakan `AzureOpenAIClient` (API Respons), kemudian `WorkflowBuilder` menentukan aliran berturutan dengan menambah tepi dari `frontDeskAgent` ke `reviewerAgent`.

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

Aliran kerja kemudiannya dijalankan dengan mesej pengguna, dan hasilnya distrim balik.

### Kes 2: Aliran Kerja Berturutan Berbilang Langkah

Corak ini melanjutkan urutan asas untuk merangkumi lebih banyak ejen. Ia sesuai untuk proses yang memerlukan beberapa peringkat penyempurnaan atau transformasi.

#### Latar Belakang Senario

Seorang pengguna menyediakan imej ruang tamu dan meminta sebut harga perabot.

1.  **Ejen Jualan**: Mengenal pasti item perabot dalam imej dan mencipta senarai.
2.  **Ejen Harga**: Mengambil senarai item dan memberi pecahan harga terperinci, termasuk pilihan bajet, sederhana, dan premium.
3.  **Ejen Sebut Harga**: Menerima senarai berharga dan memformatnya menjadi dokumen sebut harga rasmi dalam Markdown.

*Rajah aliran kerja Jualan -\> Harga -\> Sebut Harga.*

#### Analisis Pelaksanaan Python

Tiga ejen ditakrifkan, masing-masing dengan peranan khusus. Aliran kerja dibina menggunakan `add_edge` untuk mencipta rantaian: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Cipta tiga ejen khusus
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Bina aliran kerja berurutan
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Input ialah `ChatMessage` yang mengandungi teks dan URI imej. Framework mengendalikan penghantaran output setiap ejen ke ejen seterusnya dalam urutan sehingga sebut harga akhir dijana.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Mesej pengguna mengandungi kedua-dua teks dan imej
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# Jalankan aliran kerja
events = await workflow.run(message)
```

#### Analisis Pelaksanaan .NET (C\#)

Contoh .NET mencerminkan versi Python. Tiga ejen (`salesagent`, `priceagent`, `quoteagent`) dicipta. `WorkflowBuilder` menghubungkan mereka secara berturutan.

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

Mesej pengguna dibina dengan data imej (dalam bentuk bait) dan prompt teks. Kaedah `InProcessExecution.StreamAsync` memulakan aliran kerja, dan output akhir dirakam dari strim.

### Kes 3: Aliran Kerja Selari

Corak ini digunakan apabila tugasan boleh dilakukan serentak untuk menjimatkan masa. Ia melibatkan "fan-out" ke banyak ejen dan "fan-in" untuk menggabungkan hasil.

#### Latar Belakang Senario

Seorang pengguna meminta merancang perjalanan ke Seattle.

1.  **Penghantar (Fan-Out)**: Permintaan pengguna dihantar kepada dua ejen serentak.
2.  **Ejen Penyelidik**: Menyelidik tarikan, cuaca, dan pertimbangan utama untuk perjalanan ke Seattle pada Disember.
3.  **Ejen Perancang**: Secara bebas mencipta jadual perjalanan hari demi hari yang terperinci.
4.  **Penggabung (Fan-In)**: Output daripada penyelidik dan perancang dikumpulkan dan dipersembahkan bersama sebagai hasil akhir.

*Rajah aliran kerja selari Penyelidik dan Perancang.*

#### Analisis Pelaksanaan Python

`ConcurrentBuilder` memudahkan penciptaan corak ini. Anda hanya perlu senaraikan ejen yang terlibat, dan pembina secara automatik mencipta logik fan-out dan fan-in yang diperlukan.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder mengendalikan logik fan-out/fan-in
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Jalankan aliran kerja
events = await workflow.run("Plan a trip to Seattle in December")
```

Framework memastikan `research_agent` dan `plan_agent` dijalankan serentak, dan output akhir mereka dikumpulkan ke dalam senarai.

#### Analisis Pelaksanaan .NET (C\#)

Dalam .NET, corak ini memerlukan takrif lebih eksplisit. Pelaksana khusus (`ConcurrentStartExecutor` dan `ConcurrentAggregationExecutor`) dicipta untuk mengendalikan logik fan-out dan fan-in.

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

`WorkflowBuilder` kemudiannya menggunakan `AddFanOutEdge` dan `AddFanInEdge` untuk membina graf dengan pelaksana khusus dan ejen ini.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Kes 4: Aliran Kerja Bersyarat

Aliran kerja bersyarat memperkenalkan logik cabang, membenarkan sistem mengambil laluan berbeza berdasarkan keputusan sementara.

#### Latar Belakang Senario

Aliran kerja ini mengautomasikan penciptaan dan penerbitan tutorial teknikal.

1.  **Ejen Penginjil**: Menulis draf tutorial berdasarkan garis panduan dan URL yang diberikan.
2.  **Ejen Penyemak Kandungan**: Menyemak draf. Ia memeriksa jika jumlah perkataan melebihi 200 perkataan.
3.  **Cabang Bersyarat**:
      * **Jika Diluluskan (`Ya`)**: Aliran kerja diteruskan ke `Publisher-Agent`.
      * **Jika Ditolak (`Tidak`)**: Aliran kerja berhenti dan mengeluarkan alasan penolakan.
4.  **Ejen Penerbit**: Jika draf diluluskan, ejen ini menyimpan kandungan ke fail Markdown.

#### Analisis Pelaksanaan Python

Contoh ini menggunakan fungsi tersuai, `select_targets`, untuk melaksanakan logik bersyarat. Fungsi ini diserahkan ke `add_multi_selection_edge_group` dan mengarahkan aliran kerja berdasarkan medan `review_result` dari output penyemak.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Fungsi ini menentukan langkah seterusnya berdasarkan keputusan ulasan
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Jika diluluskan, teruskan ke pelaksana 'save_draft'
        return [save_draft_id]
    else:
        # Jika ditolak, teruskan ke pelaksana 'handle_review' untuk melaporkan kegagalan
        return [handle_review_id]

# Pembina aliran kerja menggunakan fungsi pemilihan untuk perutean
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Tepi pemilihan pelbagai melaksanakan logik bersyarat
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

Pelaksana tersuai seperti `to_reviewer_result` digunakan untuk mengurai output JSON dari ejen dan menukarnya menjadi objek berjenis kukuh yang boleh diperiksa fungsi pemilihan.

#### Analisis Pelaksanaan .NET (C\#)

Versi .NET menggunakan pendekatan serupa dengan fungsi syarat. `Func<object?, bool>` ditakrifkan untuk memeriksa sifat `Result` objek `ReviewResult`.

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

Parameter `condition` kaedah `AddEdge` membenarkan `WorkflowBuilder` mencipta laluan bercabang. Aliran kerja hanya akan mengikuti tepi ke `publishExecutor` jika syarat `GetCondition(expectedResult: "Yes")` mengembalikan benar. Jika tidak, ia mengikuti laluan ke `sendReviewerExecutor`.

## Kesimpulan

Microsoft Agent Framework Workflow menyediakan asas yang kukuh dan fleksibel untuk mengatur sistem multi-ejen yang kompleks. Dengan memanfaatkan seni bina berasaskan graf dan komponen terasnya, pembangun boleh mereka bentuk dan melaksanakan aliran kerja canggih dalam Python dan .NET. Sama ada aplikasi anda memerlukan pemprosesan berturutan mudah, pelaksanaan selari, atau logik bersyarat dinamik, framework ini menawarkan alat untuk membina penyelesaian berkuasa, boleh diskala, dan selamat jenis yang dikuasakan oleh AI.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->