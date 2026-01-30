# Membina Aplikasi Multi-Ejen dengan Microsoft Agent Framework Workflow

Tutorial ini akan membimbing anda memahami dan membina aplikasi multi-ejen menggunakan Microsoft Agent Framework. Kita akan meneroka konsep asas sistem multi-ejen, menyelami seni bina komponen Workflow dalam rangka kerja ini, dan melalui contoh praktikal dalam Python dan .NET untuk pelbagai corak workflow.

## 1\. Memahami Sistem Multi-Ejen

Ejen AI adalah sistem yang melangkaui kemampuan Model Bahasa Besar (LLM) biasa. Ia boleh memahami persekitarannya, membuat keputusan, dan mengambil tindakan untuk mencapai matlamat tertentu. Sistem multi-ejen melibatkan beberapa ejen ini bekerjasama untuk menyelesaikan masalah yang sukar atau mustahil untuk ditangani oleh satu ejen sahaja.

### Senario Aplikasi Biasa

  * **Penyelesaian Masalah Kompleks**: Memecahkan tugas besar (contohnya, merancang acara syarikat) kepada tugas kecil yang dikendalikan oleh ejen khusus (contohnya, ejen bajet, ejen logistik, ejen pemasaran).
  * **Pembantu Maya**: Ejen pembantu utama mendelegasikan tugas seperti penjadualan, penyelidikan, dan tempahan kepada ejen khusus lain.
  * **Penciptaan Kandungan Automatik**: Workflow di mana satu ejen merangka kandungan, ejen lain menyemak ketepatan dan nada, dan ejen ketiga menerbitkannya.

### Corak Multi-Ejen

Sistem multi-ejen boleh diatur dalam beberapa corak, yang menentukan cara mereka berinteraksi:

  * **Berkurutan**: Ejen bekerja dalam urutan yang telah ditetapkan, seperti barisan pemasangan. Output satu ejen menjadi input untuk ejen seterusnya.
  * **Serentak**: Ejen bekerja secara selari pada bahagian tugas yang berbeza, dan hasilnya digabungkan pada akhir.
  * **Bersyarat**: Workflow mengikuti laluan yang berbeza berdasarkan output ejen, serupa dengan pernyataan if-then-else.

## 2\. Seni Bina Microsoft Agent Framework Workflow

Sistem workflow dalam Agent Framework adalah enjin orkestrasi canggih yang direka untuk mengurus interaksi kompleks antara pelbagai ejen. Ia dibina berdasarkan seni bina berasaskan graf yang menggunakan [model pelaksanaan gaya Pregel](https://kowshik.github.io/JPregel/pregel_paper.pdf), di mana pemprosesan berlaku dalam langkah-langkah yang diselaraskan yang dipanggil "supersteps."

### Komponen Utama

Seni bina ini terdiri daripada tiga bahagian utama:

1.  **Executor**: Unit pemprosesan asas. Dalam contoh kita, `Agent` adalah jenis executor. Setiap executor boleh mempunyai beberapa pengendali mesej yang dipanggil secara automatik berdasarkan jenis mesej yang diterima.
2.  **Edges**: Menentukan laluan mesej antara executor. Edges boleh mempunyai syarat, membolehkan penghalaan maklumat secara dinamik melalui graf workflow.
3.  **Workflow**: Komponen ini mengorkestrasi keseluruhan proses, mengurus executor, edges, dan aliran pelaksanaan secara keseluruhan. Ia memastikan mesej diproses dalam urutan yang betul dan menstrimkan acara untuk pemerhatian.

*Rajah yang menggambarkan komponen utama sistem workflow.*

Struktur ini membolehkan pembinaan aplikasi yang kukuh dan boleh diskalakan menggunakan corak asas seperti rantai berurutan, fan-out/fan-in untuk pemprosesan selari, dan logik switch-case untuk aliran bersyarat.

## 3\. Contoh Praktikal dan Analisis Kod

Sekarang, mari kita terokai cara melaksanakan pelbagai corak workflow menggunakan rangka kerja ini. Kita akan melihat kod Python dan .NET untuk setiap contoh.

### Kes 1: Workflow Berurutan Asas

Ini adalah corak paling mudah, di mana output satu ejen dihantar terus kepada ejen lain. Senario kita melibatkan ejen `FrontDesk` hotel yang membuat cadangan perjalanan, yang kemudian disemak oleh ejen `Concierge`.

*Rajah workflow asas FrontDesk -\> Concierge.*

#### Latar Belakang Senario

Seorang pelancong meminta cadangan di Paris.

1.  Ejen `FrontDesk`, yang direka untuk ringkas, mencadangkan melawat Muzium Louvre.
2.  Ejen `Concierge`, yang mengutamakan pengalaman autentik, menerima cadangan ini. Ia menyemak cadangan dan memberikan maklum balas, mencadangkan alternatif yang lebih tempatan dan kurang pelancong.

#### Analisis Pelaksanaan Python

Dalam contoh Python, kita mula-mula mentakrifkan dan mencipta dua ejen, masing-masing dengan arahan tertentu.

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

Seterusnya, `WorkflowBuilder` digunakan untuk membina graf. `front_desk_agent` ditetapkan sebagai titik permulaan, dan edge dibuat untuk menghubungkan outputnya kepada `reviewer_agent`.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Akhirnya, workflow dilaksanakan dengan arahan awal pengguna.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### Analisis Pelaksanaan .NET (C\#)

Pelaksanaan .NET mengikuti logik yang sangat serupa. Mula-mula, konstanta ditakrifkan untuk nama ejen dan arahan mereka.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Ejen dicipta menggunakan `OpenAIClient`, dan kemudian `WorkflowBuilder` mentakrifkan aliran berurutan dengan menambah edge dari `frontDeskAgent` ke `reviewerAgent`.

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

Workflow kemudian dijalankan dengan mesej pengguna, dan hasilnya distrim kembali.

### Kes 2: Workflow Berurutan Multi-Langkah

Corak ini memperluaskan urutan asas untuk memasukkan lebih banyak ejen. Ia sesuai untuk proses yang memerlukan beberapa tahap penapisan atau transformasi.

#### Latar Belakang Senario

Seorang pengguna memberikan imej ruang tamu dan meminta sebut harga perabot.

1.  **Sales-Agent**: Mengenal pasti item perabot dalam imej dan mencipta senarai.
2.  **Price-Agent**: Mengambil senarai item dan memberikan pecahan harga terperinci, termasuk pilihan bajet, pertengahan, dan premium.
3.  **Quote-Agent**: Menerima senarai berharga dan memformatnya menjadi dokumen sebut harga rasmi dalam Markdown.

*Rajah workflow Sales -\> Price -\> Quote.*

#### Analisis Pelaksanaan Python

Tiga ejen ditakrifkan, masing-masing dengan peranan khusus. Workflow dibina menggunakan `add_edge` untuk mencipta rantai: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Input adalah `ChatMessage` yang merangkumi teks dan URI imej. Rangka kerja mengendalikan penghantaran output setiap ejen kepada ejen seterusnya dalam urutan sehingga sebut harga akhir dihasilkan.

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

#### Analisis Pelaksanaan .NET (C\#)

Contoh .NET mencerminkan versi Python. Tiga ejen (`salesagent`, `priceagent`, `quoteagent`) dicipta. `WorkflowBuilder` menghubungkan mereka secara berurutan.

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

Mesej pengguna dibina dengan data imej (sebagai byte) dan arahan teks. Kaedah `InProcessExecution.StreamAsync` memulakan workflow, dan output akhir ditangkap dari aliran.

### Kes 3: Workflow Serentak

Corak ini digunakan apabila tugas boleh dilakukan serentak untuk menjimatkan masa. Ia melibatkan "fan-out" kepada beberapa ejen dan "fan-in" untuk menggabungkan hasilnya.

#### Latar Belakang Senario

Seorang pengguna meminta untuk merancang perjalanan ke Seattle.

1.  **Dispatcher (Fan-Out)**: Permintaan pengguna dihantar kepada dua ejen pada masa yang sama.
2.  **Researcher-Agent**: Menyelidik tarikan, cuaca, dan pertimbangan utama untuk perjalanan ke Seattle pada bulan Disember.
3.  **Plan-Agent**: Secara bebas mencipta jadual perjalanan terperinci hari demi hari.
4.  **Aggregator (Fan-In)**: Output dari penyelidik dan perancang dikumpulkan dan disampaikan bersama sebagai hasil akhir.

*Rajah workflow serentak Researcher dan Planner.*

#### Analisis Pelaksanaan Python

`ConcurrentBuilder` memudahkan penciptaan corak ini. Anda hanya menyenaraikan ejen yang terlibat, dan builder secara automatik mencipta logik fan-out dan fan-in yang diperlukan.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Rangka kerja memastikan bahawa `research_agent` dan `plan_agent` dilaksanakan secara selari, dan output akhir mereka dikumpulkan ke dalam senarai.

#### Analisis Pelaksanaan .NET (C\#)

Dalam .NET, corak ini memerlukan definisi yang lebih eksplisit. Executor khusus (`ConcurrentStartExecutor` dan `ConcurrentAggregationExecutor`) dicipta untuk mengendalikan logik fan-out dan fan-in.

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

`WorkflowBuilder` kemudian menggunakan `AddFanOutEdge` dan `AddFanInEdge` untuk membina graf dengan executor khusus ini dan ejen.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Kes 4: Workflow Bersyarat

Workflow bersyarat memperkenalkan logik bercabang, membolehkan sistem mengambil laluan yang berbeza berdasarkan hasil perantaraan.

#### Latar Belakang Senario

Workflow ini mengautomasi penciptaan dan penerbitan tutorial teknikal.

1.  **Evangelist-Agent**: Menulis draf tutorial berdasarkan garis besar dan URL yang diberikan.
2.  **ContentReviewer-Agent**: Menyemak draf. Ia memeriksa sama ada jumlah perkataan melebihi 200 perkataan.
3.  **Cabang Bersyarat**:
      * **Jika Diluluskan (`Yes`)**: Workflow diteruskan kepada `Publisher-Agent`.
      * **Jika Ditolak (`No`)**: Workflow berhenti dan outputkan sebab penolakan.
4.  **Publisher-Agent**: Jika draf diluluskan, ejen ini menyimpan kandungan ke fail Markdown.

#### Analisis Pelaksanaan Python

Contoh ini menggunakan fungsi khusus, `select_targets`, untuk melaksanakan logik bersyarat. Fungsi ini diberikan kepada `add_multi_selection_edge_group` dan mengarahkan workflow berdasarkan medan `review_result` dari output penyemak.

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

Executor khusus seperti `to_reviewer_result` digunakan untuk menganalisis output JSON dari ejen dan menukarnya menjadi objek yang ditaip kuat yang boleh diperiksa oleh fungsi pemilihan.

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

Parameter `condition` kaedah `AddEdge` membolehkan `WorkflowBuilder` mencipta laluan bercabang. Workflow hanya akan mengikuti edge ke `publishExecutor` jika syarat `GetCondition(expectedResult: "Yes")` mengembalikan nilai benar. Jika tidak, ia mengikuti laluan ke `sendReviewerExecutor`.

## Kesimpulan

Microsoft Agent Framework Workflow menyediakan asas yang kukuh dan fleksibel untuk mengorkestrasi sistem multi-ejen yang kompleks. Dengan memanfaatkan seni bina berasaskan graf dan komponen utamanya, pembangun boleh mereka bentuk dan melaksanakan workflow yang canggih dalam Python dan .NET. Sama ada aplikasi anda memerlukan pemprosesan berurutan yang mudah, pelaksanaan selari, atau logik bersyarat yang dinamik, rangka kerja ini menawarkan alat untuk membina penyelesaian AI yang berkuasa, boleh diskalakan, dan selamat jenis.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.