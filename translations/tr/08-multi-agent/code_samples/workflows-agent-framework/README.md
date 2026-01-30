# Microsoft Agent Framework Workflow ile Çoklu Ajan Uygulamaları Geliştirme

Bu eğitim, Microsoft Agent Framework kullanarak çoklu ajan uygulamalarını anlamanızı ve geliştirmenizi sağlayacak. Çoklu ajan sistemlerinin temel kavramlarını keşfedecek, framework'ün Workflow bileşeninin mimarisine dalacak ve farklı iş akışı modelleri için hem Python hem de .NET'te pratik örnekler üzerinden ilerleyeceğiz.

## 1\. Çoklu Ajan Sistemlerini Anlamak

Bir AI Ajanı, standart bir Büyük Dil Modeli (LLM) yeteneklerinin ötesine geçen bir sistemdir. Çevresini algılayabilir, kararlar alabilir ve belirli hedeflere ulaşmak için eylemler gerçekleştirebilir. Çoklu ajan sistemi, birden fazla ajanın bir araya gelerek tek bir ajanın başa çıkamayacağı bir problemi çözmek için iş birliği yaptığı bir yapıdır.

### Yaygın Uygulama Senaryoları

  * **Karmaşık Problem Çözme**: Büyük bir görevi (örneğin, şirket çapında bir etkinlik planlama) daha küçük alt görevlere ayırmak ve bu görevleri uzmanlaşmış ajanlara devretmek (örneğin, bütçe ajanı, lojistik ajanı, pazarlama ajanı).
  * **Sanal Asistanlar**: Bir ana asistan ajanın, takvim oluşturma, araştırma ve rezervasyon gibi görevleri diğer uzmanlaşmış ajanlara devretmesi.
  * **Otomatik İçerik Üretimi**: Bir ajanın içerik taslağı oluşturduğu, diğerinin doğruluk ve ton açısından gözden geçirdiği ve üçüncüsünün yayınladığı bir iş akışı.

### Çoklu Ajan Modelleri

Çoklu ajan sistemleri, etkileşim biçimlerini belirleyen çeşitli modellerde düzenlenebilir:

  * **Sıralı**: Ajanlar önceden belirlenmiş bir sırayla çalışır, bir ajanın çıktısı bir sonraki ajanın girdisi olur.
  * **Eşzamanlı**: Ajanlar bir görevin farklı bölümleri üzerinde paralel olarak çalışır ve sonuçlar sonunda birleştirilir.
  * **Koşullu**: İş akışı, bir ajanın çıktısına bağlı olarak farklı yollar izler, tıpkı bir if-then-else ifadesi gibi.

## 2\. Microsoft Agent Framework Workflow Mimarisini Anlamak

Agent Framework'ün iş akışı sistemi, birden fazla ajanın karmaşık etkileşimlerini yönetmek için tasarlanmış gelişmiş bir orkestrasyon motorudur. "Süper adımlar" olarak adlandırılan senkronize adımlarda işlem yapılan [Pregel tarzı bir yürütme modeli](https://kowshik.github.io/JPregel/pregel_paper.pdf) üzerine kuruludur.

### Temel Bileşenler

Mimari üç ana bölümden oluşur:

1.  **Executors**: Temel işlem birimleridir. Örneklerimizde, bir `Agent` bir tür executor'dır. Her executor, alınan mesaj türüne göre otomatik olarak çağrılan birden fazla mesaj işleyiciye sahip olabilir.
2.  **Edges**: Mesajların executor'lar arasında izlediği yolu tanımlar. Edges koşullara sahip olabilir, bu da iş akışı grafiği boyunca bilgilerin dinamik olarak yönlendirilmesine olanak tanır.
3.  **Workflow**: Tüm süreci orkestre eden bu bileşen, executor'ları, edges'leri ve genel yürütme akışını yönetir. Mesajların doğru sırada işlenmesini sağlar ve gözlemlenebilirlik için olayları yayınlar.

*İş akışı sisteminin temel bileşenlerini gösteren bir diyagram.*

Bu yapı, sıralı zincirler, paralel işlem için fan-out/fan-in ve koşullu akışlar için switch-case mantığı gibi temel modelleri kullanarak sağlam ve ölçeklenebilir uygulamalar oluşturmayı mümkün kılar.

## 3\. Pratik Örnekler ve Kod Analizi

Şimdi framework kullanarak farklı iş akışı modellerini nasıl uygulayacağımızı inceleyelim. Her örnek için hem Python hem de .NET kodlarına bakacağız.

### Örnek 1: Temel Sıralı İş Akışı

Bu en basit modeldir; bir ajanın çıktısı doğrudan diğerine aktarılır. Senaryomuzda, bir otel `FrontDesk` ajanı seyahat önerisi yapar ve bu öneri bir `Concierge` ajanı tarafından gözden geçirilir.

*Temel FrontDesk -\> Concierge iş akışı diyagramı.*

#### Senaryo Arka Planı

Bir gezgin Paris'te bir öneri ister.

1.  Kısa öneriler sunmak için tasarlanmış `FrontDesk` ajanı Louvre Müzesi'ni ziyaret etmeyi önerir.
2.  Daha otantik deneyimlere öncelik veren `Concierge` ajanı bu öneriyi alır. Öneriyi gözden geçirir ve daha yerel, daha az turistik bir alternatif önerir.

#### Python Uygulama Analizi

Python örneğinde, önce iki ajan tanımlanır ve oluşturulur, her biri belirli talimatlarla.

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

Sonra, `WorkflowBuilder` kullanılarak grafik oluşturulur. `front_desk_agent` başlangıç noktası olarak ayarlanır ve çıktısını `reviewer_agent`a bağlayan bir edge oluşturulur.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder().set_start_executor(front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Son olarak, iş akışı kullanıcıdan gelen ilk istemle çalıştırılır.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# The run_stream method executes the workflow and streams events.
async for event in workflow.run_stream('I would like to go to Paris.'):
    if isinstance(event, WorkflowEvent):
        result += str(event.data)
```

#### .NET (C\#) Uygulama Analizi

.NET uygulaması çok benzer bir mantığı takip eder. Önce ajanların isimleri ve talimatları için sabitler tanımlanır.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are an are hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Ajanlar bir `OpenAIClient` kullanılarak oluşturulur ve ardından `WorkflowBuilder` sıralı akışı tanımlamak için `frontDeskAgent` ile `reviewerAgent` arasında bir edge ekler.

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

İş akışı, kullanıcının mesajıyla çalıştırılır ve sonuçlar geri akışla yayınlanır.

### Örnek 2: Çok Adımlı Sıralı İş Akışı

Bu model, temel sıralı iş akışını daha fazla ajan ekleyerek genişletir. Birden fazla aşama gerektiren süreçler için idealdir.

#### Senaryo Arka Planı

Bir kullanıcı bir oturma odası fotoğrafı gönderir ve mobilya fiyat teklifi ister.

1.  **Sales-Agent**: Görüntüdeki mobilya öğelerini tanımlar ve bir liste oluşturur.
2.  **Price-Agent**: Öğelerin listesini alır ve bütçe, orta seviye ve premium seçenekler dahil olmak üzere ayrıntılı bir fiyat dökümü sağlar.
3.  **Quote-Agent**: Fiyatlandırılmış listeyi alır ve Markdown formatında resmi bir teklif belgesi oluşturur.

*Sales -\> Price -\> Quote iş akışı diyagramı.*

#### Python Uygulama Analizi

Üç ajan tanımlanır, her biri özel bir role sahiptir. İş akışı, `add_edge` kullanılarak bir zincir oluşturur: `sales_agent` -\> `price_agent` -\> `quote_agent`.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Create three specialized agents
sales_agent = chat_client.create_agent(...)
price_agent = chat_client.create_agent(...)
quote_agent = chat_client.create_agent(...)

# Build the sequential workflow
workflow = WorkflowBuilder().set_start_executor(sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Girdi, hem metin hem de görüntü URI'sini içeren bir `ChatMessage`dir. Framework, her ajanın çıktısını sırayla bir sonrakine aktarır ve nihai teklif oluşturulana kadar devam eder.

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

#### .NET (C\#) Uygulama Analizi

.NET örneği Python versiyonunu yansıtır. Üç ajan (`salesagent`, `priceagent`, `quoteagent`) oluşturulur. `WorkflowBuilder` bunları sıralı olarak bağlar.

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

Kullanıcının mesajı, hem görüntü verilerini (byte olarak) hem de metin istemini içerir. `InProcessExecution.StreamAsync` yöntemi iş akışını başlatır ve nihai çıktı akıştan alınır.

### Örnek 3: Eşzamanlı İş Akışı

Bu model, zaman tasarrufu sağlamak için görevlerin aynı anda gerçekleştirilebildiği durumlarda kullanılır. Birden fazla ajana "fan-out" yapılır ve sonuçlar "fan-in" ile birleştirilir.

#### Senaryo Arka Planı

Bir kullanıcı Seattle'a bir gezi planlamasını ister.

1.  **Dispatcher (Fan-Out)**: Kullanıcının isteği aynı anda iki ajana gönderilir.
2.  **Researcher-Agent**: Seattle'da Aralık ayında gezilecek yerler, hava durumu ve önemli hususları araştırır.
3.  **Plan-Agent**: Bağımsız olarak ayrıntılı bir günlük seyahat planı oluşturur.
4.  **Aggregator (Fan-In)**: Araştırmacı ve planlayıcıdan gelen çıktılar toplanır ve nihai sonuç olarak sunulur.

*Eşzamanlı Researcher ve Planner iş akışı diyagramı.*

#### Python Uygulama Analizi

`ConcurrentBuilder`, bu modelin oluşturulmasını basitleştirir. Katılan ajanları listelemeniz yeterlidir ve builder gerekli fan-out ve fan-in mantığını otomatik olarak oluşturur.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.create_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.create_agent(name="Plan-Agent", ...)

# ConcurrentBuilder handles the fan-out/fan-in logic
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# Run the workflow
events = await workflow.run("Plan a trip to Seattle in December")
```

Framework, `research_agent` ve `plan_agent`ın paralel olarak çalışmasını sağlar ve nihai çıktıları bir listeye toplar.

#### .NET (C\#) Uygulama Analizi

.NET'te bu model daha açık bir tanım gerektirir. Fan-out ve fan-in mantığını yönetmek için özel executor'lar (`ConcurrentStartExecutor` ve `ConcurrentAggregationExecutor`) oluşturulur.

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

`WorkflowBuilder`, bu özel executor'lar ve ajanlarla grafiği oluşturmak için `AddFanOutEdge` ve `AddFanInEdge` kullanır.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Örnek 4: Koşullu İş Akışı

Koşullu iş akışları, ara sonuçlara bağlı olarak farklı yollar izlenmesine olanak tanıyan dallanma mantığını tanıtır.

#### Senaryo Arka Planı

Bu iş akışı, teknik bir eğitimin oluşturulmasını ve yayınlanmasını otomatikleştirir.

1.  **Evangelist-Agent**: Verilen bir taslak ve URL'lere dayanarak eğitimin taslağını yazar.
2.  **ContentReviewer-Agent**: Taslağı gözden geçirir. Kelime sayısının 200'den fazla olup olmadığını kontrol eder.
3.  **Koşullu Dal**:
      * **Onaylanırsa (`Evet`)**: İş akışı `Publisher-Agent`a devam eder.
      * **Reddedilirse (`Hayır`)**: İş akışı durur ve reddedilme nedenini çıktılar.
4.  **Publisher-Agent**: Taslak onaylanırsa, bu ajan içeriği bir Markdown dosyasına kaydeder.

#### Python Uygulama Analizi

Bu örnek, koşullu mantığı uygulamak için özel bir `select_targets` fonksiyonu kullanır. Bu fonksiyon, `add_multi_selection_edge_group`a geçirilir ve iş akışını `review_result` alanına göre yönlendirir.

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

`to_reviewer_result` gibi özel executor'lar, ajanlardan gelen JSON çıktısını ayrıştırmak ve seçim fonksiyonunun inceleyebileceği güçlü tipte nesnelere dönüştürmek için kullanılır.

#### .NET (C\#) Uygulama Analizi

.NET versiyonu benzer bir yaklaşım kullanır ve bir koşul fonksiyonu tanımlar. `Func<object?, bool>` tanımlanır ve `ReviewResult` nesnesinin `Result` özelliğini kontrol eder.

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

`AddEdge` metodunun `condition` parametresi, `WorkflowBuilder`ın bir dallanma yolu oluşturmasına olanak tanır. İş akışı yalnızca `GetCondition(expectedResult: "Yes")` koşulu doğru dönerse `publishExecutor`a gider. Aksi takdirde `sendReviewerExecutor` yolunu izler.

## Sonuç

Microsoft Agent Framework Workflow, karmaşık, çoklu ajan sistemlerini orkestre etmek için sağlam ve esnek bir temel sağlar. Grafik tabanlı mimarisi ve temel bileşenleri sayesinde, geliştiriciler hem Python hem de .NET'te sofistike iş akışları tasarlayıp uygulayabilir. Uygulamanız basit sıralı işlem, paralel yürütme veya dinamik koşullu mantık gerektirse de, framework güçlü, ölçeklenebilir ve tip güvenli AI destekli çözümler oluşturmak için gerekli araçları sunar.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayın. Belgenin orijinal dili, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul etmiyoruz.