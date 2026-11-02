# Microsoft Agent Framework Workflow ile Çoklu Ajan Uygulamaları Geliştirme

Bu eğitim, Microsoft Agent Framework kullanarak çoklu ajan uygulamalarını anlamanıza ve oluşturmanıza rehberlik edecektir. Çoklu ajan sistemlerinin temel kavramlarını keşfedecek, framework'ün Workflow bileşeninin mimarisine dalacak ve farklı iş akışı desenleri için hem Python hem de .NET'te pratik örnekler üzerinde ilerleyeceğiz.

## 1\. Çoklu Ajan Sistemlerini Anlamak

Bir Yapay Zeka Ajanı, standart Büyük Dil Modeli'nin (LLM) yeteneklerinin ötesine geçen bir sistemdir. Çevresini algılayabilir, kararlar verebilir ve belirli hedeflere ulaşmak için eylemler gerçekleştirebilir. Çoklu ajan sistemi, tek bir ajanın tek başına halledemeyeceği bir problemi çözmek için iş birliği yapan birden fazla ajanı içerir.

### Yaygın Uygulama Senaryoları

  * **Karmaşık Problem Çözme**: Büyük bir görevi (ör. şirket çapında bir etkinlik planlaması) uzmanlaşmış ajanların (ör. bütçe ajanı, lojistik ajanı, pazarlama ajanı) yönettiği küçük alt görevlere bölmek.
  * **Sanal Asistanlar**: Öncelikli bir asistan ajanın takvim düzenleme, araştırma ve rezervasyon gibi görevleri diğer uzman ajanlara devretmesi.
  * **Otomatik İçerik Oluşturma**: Bir ajanın içerik taslağı hazırladığı, başka bir ajanın doğruluk ve ton açısından değerlendirme yaptığı ve üçüncü bir ajanın yayınladığı bir iş akışı.

### Çoklu Ajan Desenleri

Çoklu ajan sistemleri, etkileşim biçimlerini belirleyen çeşitli desenlerde organize edilebilir:

  * **Ardışık**: Ajanlar, bir montaj hattı gibi önceden belirlenmiş sırayla çalışır. Bir ajanın çıktısı, bir sonraki ajanın girdisi olur.
  * **Eşzamanlı**: Ajanlar, bir görevin farklı bölümleri üzerinde paralel olarak çalışır ve sonuçları sonunda birleştirilir.
  * **Koşullu**: İş akışı, bir ajanın çıktısına bağlı olarak if-then-else ifadesine benzer farklı yollar izler.

## 2\. Microsoft Agent Framework Workflow Mimarisi

Agent Framework’ün iş akışı sistemi, birden fazla ajan arasındaki karmaşık etkileşimleri yönetmek için tasarlanmış gelişmiş bir orkestrasyon motorudur. İşlem, [Pregel tarzı yürütme modeli](https://kowshik.github.io/JPregel/pregel_paper.pdf) kullanan grafik tabanlı bir mimari üzerine kuruludur; burada işlem "süperadımlar" olarak adlandırılan senkronize adımlarda gerçekleşir.

### Temel Bileşenler

Mimari üç ana bölümden oluşur:

1.  **Yürütücüler**: Bunlar temel işleme birimleridir. Örneklerimizde bir `Agent` bir yürütücü türüdür. Her yürütücünün, alınan mesaj türüne göre otomatik çağrılan birden çok mesaj işleyicisi olabilir.
2.  **Kenarlar**: Mesajların yürütücüler arasında izlediği yolu tanımlar. Kenarlar koşullara sahip olabilir, bu da bilgi akışının iş akışı grafiğinde dinamik yönlendirilmesini sağlar.
3.  **İş Akışı**: Tüm süreci yöneten bileşendir, yürütücüleri, kenarları ve yürütmenin genel akışını yönetir. Mesajların doğru sırayla işlenmesini sağlar ve gözlemlenebilirlik için olay akışları yayınlar.

*İş akışı sisteminin temel bileşenlerini gösteren bir diyagram.*

Bu yapı, ardışık zincirler, paralel işlem için fan-out/fan-in ve koşullu akışlar için switch-case mantığı gibi temel desenler kullanarak sağlam ve ölçeklenebilir uygulamalar geliştirmeye olanak tanır.

## 3\. Pratik Örnekler ve Kod Analizi

Şimdi, framework kullanarak farklı iş akışı desenlerini nasıl uygulayacağımıza göz atalım. Her örnek için Python ve .NET kodlarına bakacağız.

### Durum 1: Temel Ardışık İş Akışı

Bu en basit desendir; bir ajanın çıktısı doğrudan diğerine aktarılır. Senaryomuzda, seyahat önerisi yapan bir otel `FrontDesk` ajanı vardır, ardından `Concierge` ajanı bu öneriyi inceler.

*Temel FrontDesk -\> Concierge iş akışı diyagramı.*

#### Senaryo Arka Planı

Bir yolcu Paris'te öneri ister.

1.  Kısa olması amaçlanan `FrontDesk` ajanı Louvre Müzesi'ni gezmeyi önerir.
2.  Otantik deneyimlere önem veren `Concierge` ajanı bu öneriyi alır, inceler ve daha yerel, turistik olmayan bir alternatif önerir.

#### Python Uygulama Analizi

Python örneğinde, önce her biri özel talimatlara sahip iki ajan tanımlanır ve oluşturulur.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

# Ajan rollerini ve talimatlarını tanımla
REVIEWER_NAME = "Concierge"
REVIEWER_INSTRUCTIONS = """
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...
    """

FRONTDESK_NAME = "FrontDesk"
FRONTDESK_INSTRUCTIONS = """
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...
    """

# Ajan örnekleri oluştur
reviewer_agent = chat_client.as_agent(
    instructions=(REVIEWER_INSTRUCTIONS),
    name=REVIEWER_NAME,
)

front_desk_agent = chat_client.as_agent(
    instructions=(FRONTDESK_INSTRUCTIONS),
    name=FRONTDESK_NAME,
)
```

Ardından, `WorkflowBuilder` grafik oluşturmak için kullanılır. `front_desk_agent` başlangıç noktası olarak ayarlanır ve çıktısını `reviewer_agent` ile bağlamak için bir kenar oluşturulur.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

workflow = WorkflowBuilder(start_executor=front_desk_agent).add_edge(front_desk_agent, reviewer_agent).build()
```

Son olarak, iş akışı başlangıç kullanıcı istemi ile çalıştırılır.

```python
# 01.python-agent-framework-workflow-ghmodel-basic.ipynb

result =''
# run iş akışını çalıştırır; get_outputs() çıkış yürütücüsünün sonucunu döner.
events = await workflow.run('I would like to go to Paris.')
outputs = events.get_outputs()
result = outputs[0].text if outputs else ''
```

#### .NET (C\#) Uygulama Analizi

.NET uygulaması çok benzer bir mantık izler. Önce ajan isimleri ve talimatları için sabitler tanımlanır.

```csharp
// 01.dotnet-agent-framework-workflow-ghmodel-basic.ipynb

const string ReviewerAgentName = "Concierge";
const string ReviewerAgentInstructions = @"
    You are a hotel concierge who has opinions about providing the most local and authentic experiences for travelers...";

const string FrontDeskAgentName = "FrontDesk";
const string FrontDeskAgentInstructions = @"""
    You are a Front Desk Travel Agent with ten years of experience and are known for brevity...";
```

Ajanlar, `AzureOpenAIClient` (Yanıtlar API) kullanılarak oluşturulur ve ardından `WorkflowBuilder` `frontDeskAgent`'ten `reviewerAgent`'a ardışık akışı tanımlamak için bir kenar ekler.

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

İş akışı, kullanıcının mesajı ile çalıştırılır ve sonuçlar akış olarak geri iletilir.

### Durum 2: Çok Adımlı Ardışık İş Akışı

Bu desen temel sıralamayı daha fazla ajan içerecek şekilde genişletir. Birden çok aşamalı inceleme veya dönüşüm gerektiren süreçler için idealdir.

#### Senaryo Arka Planı

Bir kullanıcı, bir oturma odasının resmini sağlar ve mobilya teklifi ister.

1.  **Satış-Ajanı**: Resimdeki mobilya öğelerini tanımlar ve liste oluşturur.
2.  **Fiyat-Ajanı**: Listeyi alır ve bütçe, orta seviye ve premium seçenekler dahil detaylı fiyatlandırma yapar.
3.  **Teklif-Ajanı**: Fiyatlandırılmış listeyi alır ve resmi bir Markdown teklif dokümanı olarak formatlar.

*Satış -\> Fiyat -\> Teklif iş akışı diyagramı.*

#### Python Uygulama Analizi

Üç ajan, her biri özel bir işleve sahip olarak tanımlanır. İş akışı, `add_edge` ile `sales_agent` -\> `price_agent` -\> `quote_agent` zinciri oluşturularak inşa edilir.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Üç özel ajan oluşturun
sales_agent = chat_client.as_agent(...)
price_agent = chat_client.as_agent(...)
quote_agent = chat_client.as_agent(...)

# Ardışık iş akışını oluşturun
workflow = WorkflowBuilder(start_executor=sales_agent).add_edge(sales_agent, price_agent).add_edge(price_agent, quote_agent).build()
```

Girdi, metin ve resim URI'sini içeren bir `ChatMessage`'dir. Framework, her ajanın çıktısını sonraki ajana zincir boyunca geçirmeyi yönetir ve son teklif oluşturulur.

```python
# 02.python-agent-framework-workflow-ghmodel-sequential.ipynb

# Kullanıcı mesajı hem metin hem de resim içeriyor
message = ChatMessage(
        role=Role.USER,
        contents=[
            TextContent(text="Please find the relevant furniture..."),
            DataContent(uri=image_uri, media_type="image/png")
        ]
)

# İş akışını çalıştır
events = await workflow.run(message)
```

#### .NET (C\#) Uygulama Analizi

.NET örneği, Python sürümünü yansıtır. Üç ajan (`salesagent`, `priceagent`, `quoteagent`) oluşturulur. `WorkflowBuilder` onları ardışık olarak bağlar.

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

Kullanıcının mesajı, hem resim verisi (bayt olarak) hem de metin istemi ile oluşturulur. `InProcessExecution.RunStreamingAsync` yöntemi iş akışını başlatır ve son çıktı akıştan alınır.

### Durum 3: Eşzamanlı İş Akışı

Bu desen, görevlerin aynı anda yapılabileceği durumlarda zamandan tasarruf etmek için kullanılır. Birden fazla ajana "fan-out" ve sonuçları toplamak için "fan-in" içerir.

#### Senaryo Arka Planı

Bir kullanıcı Seattle'a seyahat planlaması ister.

1.  **Gönderici (Fan-Out)**: Kullanıcı isteği aynı anda iki ajana gönderilir.
2.  **Araştırmacı-Ajan**: Seattle'da Aralık ayında gezilecek yerler, hava durumu ve önemli hususları araştırır.
3.  **Planlayıcı-Ajan**: Ayrı olarak ayrıntılı günlük seyahat programı hazırlamaktadır.
4.  **Toplayıcı (Fan-In)**: Araştırmacı ve planlayıcıdan gelen sonuçlar toplanır ve birlikte nihai sonuç olarak sunulur.

*Eşzamanlı Araştırmacı ve Planlayıcı iş akışı diyagramı.*

#### Python Uygulama Analizi

`ConcurrentBuilder`, bu desenin oluşturulmasını basitleştirir. Katılımcı ajanları listelemeniz yeterlidir; builder gerekli fan-out ve fan-in mantığını otomatik oluşturur.

```python
# 03.python-agent-framework-workflow-ghmodel-concurrent.ipynb

research_agent = chat_client.as_agent(name="Researcher-Agent", ...)
plan_agent = chat_client.as_agent(name="Plan-Agent", ...)

# ConcurrentBuilder kümelenme/genleşme mantığını yönetir
workflow = ConcurrentBuilder().participants([research_agent, plan_agent]).build()

# İş akışını çalıştırın
events = await workflow.run("Plan a trip to Seattle in December")
```

Framework, `research_agent` ve `plan_agent`ın paralel çalışmasını sağlar ve nihai çıktılar bir listeye toplanır.

#### .NET (C\#) Uygulama Analizi

.NET’te bu desen daha açık bir tanım gerektirir. Fan-out ve fan-in mantığını işlemek için özel yürütücüler (`ConcurrentStartExecutor` ve `ConcurrentAggregationExecutor`) oluşturulur.

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

Sonra `WorkflowBuilder`, bu özel yürütücüler ve ajanlarla grafiği inşa etmek için `AddFanOutEdge` ve `AddFanInEdge` yöntemlerini kullanır.

```csharp
// 03.dotnet-agent-framework-workflow-ghmodel-concurrent.ipynb

var workflow = new WorkflowBuilder(startExecutor)
            .AddFanOutEdge(startExecutor, targets: [researcherAgent, plannerAgent])
            .AddFanInEdge(aggregationExecutor, sources: [researcherAgent, plannerAgent])
            .WithOutputFrom(aggregationExecutor)
            .Build();
```

### Durum 4: Koşullu İş Akışı

Koşullu iş akışları, ara sonuçlara bağlı olarak sistemin farklı yollar izlemesine olanak tanıyan dallanma mantığını tanıtır.

#### Senaryo Arka Planı

Bu iş akışı, teknik bir eğitici oluşturma ve yayınlama sürecini otomatikleştirir.

1.  **Evangelist-Ajan**: Verilen bir taslak ve URL'ler temelinde eğitici taslağı yazar.
2.  **ContentReviewer-Ajan**: Taslağı inceler. Kelime sayısının 200'ün üzerinde olup olmadığını kontrol eder.
3.  **Koşullu Dal**:
      * **Onaylandıysa (`Evet`)**: İş akışı `Publisher-Agent`'a devam eder.
      * **Reddedildiyse (`Hayır`)**: İş akışı durur ve reddedilme nedeni çıktı olarak verilir.
4.  **Publisher-Agent**: Taslak onaylanırsa, bu ajan içeriği bir Markdown dosyası olarak kaydeder.

#### Python Uygulama Analizi

Bu örnek, koşullu mantığı uygulamak için `select_targets` adlı özel bir fonksiyon kullanır. Bu fonksiyon `add_multi_selection_edge_group`'a aktarılır ve anonim seçici olarak review_result alanına göre iş akışının yönlendirilmesini sağlar.

```python
# 04.python-agent-framework-workflow-aifoundry-condition.ipynb

# Bu fonksiyon, inceleme sonucuna göre bir sonraki adımı belirler
def select_targets(review: ReviewResult, target_ids: list[str]) -> list[str]:
    handle_review_id, save_draft_id = target_ids
    if review.review_result == "Yes":
        # Onaylanırsa, 'save_draft' yürütücüsüne geçilir
        return [save_draft_id]
    else:
        # Reddedilirse, başarısızlık bildirmek için 'handle_review' yürütücüsüne geçilir
        return [handle_review_id]

# İş akışı oluşturucu yönlendirme için seçim fonksiyonunu kullanır
workflow = (
    WorkflowBuilder()
        .set_start_executor(evangelist_agent)
        .add_edge(evangelist_agent, reviewer_agent)
        .add_edge(reviewer_agent, to_reviewer_result)
        # Çoklu seçim kenarı, koşullu mantığı uygular
        .add_multi_selection_edge_group(
            to_reviewer_result,
            [handle_review, save_draft],
            selection_func=select_targets,
        )
        .add_edge(save_draft, publisher_agent)
        .build()
)
```

`to_reviewer_result` gibi özel yürütücüler, ajanlardan JSON çıktısını ayrıştırıp seçim fonksiyonunun inceleyebileceği güçlü yazımlı objelere dönüştürmek için kullanılır.

#### .NET (C\#) Uygulama Analizi

.NET sürümü, koşul fonksiyonuyla benzer bir yaklaşım kullanır. `ReviewResult` nesnesinin `Result` özelliğini kontrol eden bir `Func<object?, bool>` tanımlanır.

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

`AddEdge` metodunun `condition` parametresi, `WorkflowBuilder`'ın dallanma yolu oluşturmasını sağlar. İş akışı, koşul `GetCondition(expectedResult: "Yes")` doğruysa `publishExecutor` kenarını izler; aksi halde `sendReviewerExecutor` yolunu takip eder.

## Sonuç

Microsoft Agent Framework Workflow, karmaşık çoklu ajan sistemlerini orkestre etmek için sağlam ve esnek bir temel sağlar. Grafik tabanlı mimarisi ve temel bileşenleri sayesinde, geliştiriciler hem Python hem de .NET'te gelişmiş iş akışları tasarlayıp uygulayabilirler. Uygulamanız basit ardışık işlem, paralel yürütme veya dinamik koşullu mantık gerektirsin, framework güçlü, ölçeklenebilir ve tip güvenli yapay zeka destekli çözümler oluşturmak için araçlar sunar.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->