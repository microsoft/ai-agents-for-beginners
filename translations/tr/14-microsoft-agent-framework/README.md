# Microsoft Agent Framework'ü Keşfetmek

![Agent Framework](../../../translated_images/tr/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Giriş

Bu ders şunları kapsayacaktır:

- Microsoft Agent Framework'ü Anlamak: Temel Özellikler ve Değeri  
- Microsoft Agent Framework'ün Temel Kavramlarını Keşfetmek
- İleri Seviye MAF Desenleri: İş Akışları, Ara Yazılım ve Bellek

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra şunları bileceksiniz:

- Microsoft Agent Framework kullanarak Üretime Hazır AI Ajanları oluşturmayı
- Microsoft Agent Framework'ün temel özelliklerini ajan kullanımı vakalarınıza uygulamayı
- İş akışları, ara yazılım ve gözlemlenebilirlik dahil olmak üzere gelişmiş desenleri kullanmayı

## Kod Örnekleri

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) için kod örnekleri bu depoda `xx-python-agent-framework` ve `xx-dotnet-agent-framework` dosyaları altında bulunabilir.

## Microsoft Agent Framework'ü Anlamak

![Framework Intro](../../../translated_images/tr/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok), Microsoft'un AI ajanları oluşturmak için birleşik çerçevesidir. Üretim ve araştırma ortamlarında görülen çeşitli ajan kullanımı vakalarına hitap etme esnekliği sunar; bunlar şunlardır:

- Adım adım iş akışlarının gerektiği senaryolarda **Artımlı Ajan orkestrasyonu**.
- Ajanların aynı anda görevleri tamamlaması gereken senaryolarda **Eşzamanlı orkestrasyon**.
- Ajanların birlikte bir görev üzerinde iş birliği yapabildiği senaryolarda **Grup sohbeti orkestrasyonu**.
- Alt görevler tamamlandıkça ajanların işi birbirine devrettiği senaryolarda **Devir Orkestrasyonu**.
- Bir yönetici ajanın görev listesi oluşturup değiştirdiği ve alt ajanların koordinasyonunu sağladığı senaryolarda **Manyetik Orkestrasyon**.

AI Ajanları Üretimde sunmak için MAF ayrıca şu özellikleri içerir:

- AI Ajanın her eylemi, araç çağrısı, orkestrasyon adımları, gerekçelendirme akışları ve Microsoft Foundry panoları üzerinden performans izleme içeren **OpenTelemetry aracılığı ile gözlemlenebilirlik**.
- Rol tabanlı erişim, özel veri işleme ve yerleşik içerik güvenliği gibi güvenlik kontrollerini içeren Microsoft Foundry'de ajanları yerel olarak barındırarak **Güvenlik**.
- Uzun süreli süreçleri mümkün kılan, ajan iş parçacıkları ve iş akışlarının duraklatılmasını, devam ettirilmesini ve hatalardan kurtarılmasını sağlayan **Dayanıklılık**.
- Görevlerin insan onayı gerektirdiği durumda desteklenen **insan döngüsünde kontrol**.

Microsoft Agent Framework aynı zamanda birlikte çalışabilir olmaya odaklanır:

- **Bulut bağımsızlığı** - Ajanlar konteynerlerde, yerel ortamda ve çoklu bulutlarda çalışabilir.
- **Sağlayıcı bağımsızlığı** - Ajanlar tercih edilen SDK'nız üzerinden oluşturulabilir, Azure OpenAI ve OpenAI dahil.
- **Açık Standartların Entegrasyonu** - Ajanlar, diğer ajanları ve araçları keşfetmek ve kullanmak için Agent-to-Agent (A2A) ve Model Context Protocol (MCP) gibi protokolleri kullanabilir.
- **Eklentiler ve Bağlayıcılar** - Microsoft Fabric, SharePoint, Pinecone ve Qdrant gibi veri ve bellek hizmetlerine bağlantılar yapılabilir.

Şimdi bu özelliklerin Microsoft Agent Framework'ün bazı temel kavramlarına nasıl uygulandığına bakalım.

## Microsoft Agent Framework'ün Temel Kavramları

### Ajanlar

![Agent Framework](../../../translated_images/tr/agent-components.410a06daf87b4fef.webp)

**Ajan Oluşturma**

Ajan oluşturma, çıkarım servisini (LLM Sağlayıcısı), AI Ajanın izlemesi gereken talimatlar setini ve atanan bir `isim` tanımlayarak yapılır:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Yukarıdaki `Azure OpenAI` kullanmaktadır ancak ajanlar `Microsoft Foundry Agent Service` dahil çeşitli servisler kullanılarak oluşturulabilir:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` API'ları

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

veya A2A protokolü kullanarak uzak ajanlar:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Ajanları Çalıştırmak**

Ajanlar, yayınlamayan veya yayın yapan yanıtlar için `.run` veya `.run_stream` metodları kullanılarak çalıştırılır.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Her ajan çalıştırmada ayrıca ajan tarafından kullanılan `max_tokens`, ajan tarafından çağrılabilen `tools` ve hatta ajanın kullandığı `model` gibi parametreler özelleştirilebilir.

Bu, kullanıcının görevini tamamlamak için belirli modeller veya araçların gerekli olduğu durumlarda faydalıdır.

**Araçlar**

Araçlar hem ajan tanımlanırken tanımlanabilir:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Bir ChatAgent doğrudan oluşturulurken

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

hem de ajan çalıştırılırken:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Yalnızca bu çalıştırma için sağlanan araç )
```

**Ajan İş Parçacıkları**

Ajan İş Parçacıkları çok turlu konuşmaları yönetmek için kullanılır. İş parçacıkları şu yollarla oluşturulabilir:

- İş parçacığını zamanla kaydetmeye olanak tanıyan `get_new_thread()` kullanılarak
- Bir ajan çalıştırılırken otomatik olarak bir iş parçacığı oluşturmak ve iş parçacığının sadece mevcut çalışma sırasında var olması.

Bir iş parçacığı oluşturmak için kod şöyle görünür:

```python
# Yeni bir iş parçacığı oluştur.
thread = agent.get_new_thread() # İstemciyi iş parçacığı ile çalıştır.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Daha sonra iş parçacığını ileride kullanmak üzere seri hale getirebilirsiniz:

```python
# Yeni bir iş parçacığı oluşturun.
thread = agent.get_new_thread() 

# İş parçacığı ile ajanı çalıştırın.

response = await agent.run("Hello, how are you?", thread=thread) 

# Depolama için iş parçacığını seri hale getirin.

serialized_thread = await thread.serialize() 

# Depolamadan yüklendikten sonra iş parçacığı durumunu seriden çıkarın.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Ajan Ara Yazılımı**

Ajanlar, kullanıcının görevlerini tamamlamak için araçlar ve LLM’lerle etkileşir. Bazı senaryolarda bu etkileşimler arasında yürütme veya izleme yapmak isteriz. Ajan ara yazılımı bunu şu şekilde mümkün kılar:

*Fonksiyon Ara Yazılımı*

Bu ara yazılım, ajan ile çağıracağı fonksiyon/araç arasında bir eylemin yürütülmesini sağlar. Örneğin fonksiyon çağrısı üzerinde bazı kayıt işlemleri yapmak istenebilir.

Aşağıdaki kodda `next` bir sonraki ara yazılımın mı yoksa gerçek fonksiyonun mu çağrılacağını tanımlar.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Ön işleme: Fonksiyon çalıştırılmadan önce loglama
    print(f"[Function] Calling {context.function.name}")

    # Sonraki middleware veya fonksiyon çalıştırmaya devam et
    await next(context)

    # Son işlem: Fonksiyon çalıştırıldıktan sonra loglama
    print(f"[Function] {context.function.name} completed")
```

*Chat Ara Yazılımı*

Bu ara yazılım, ajan ile LLM arasında yapılan istekler arasında bir eylemin yürütülmesini veya kaydedilmesini sağlar.

Gönderilen `messages` gibi önemli bilgileri içerir.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Ön işleme: AI çağrısından önce günlük kaydı
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Sonraki ara yazılıma veya AI hizmetine devam et
    await next(context)

    # Son işlem: AI yanıtından sonra günlük kaydı
    print("[Chat] AI response received")

```

**Ajan Belleği**

`Agentic Memory` dersinde ele alındığı gibi, bellek, ajanın farklı bağlamlarda çalışmasını sağlamak için önemli bir unsurdur. MAF çeşitli bellek türleri sunar:

*Bellek İçi Depolama*

Bu, uygulama çalışırken iş parçacıklarında saklanan bellektir.

```python
# Yeni bir iş parçacığı oluşturun.
thread = agent.get_new_thread() # Ajanı iş parçacığı ile çalıştırın.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Kalıcı Mesajlar*

Bu bellek, farklı oturumlarda sohbet geçmişini saklamak için kullanılır. `chat_message_store_factory` ile tanımlanır:

```python
from agent_framework import ChatMessageStore

# Özel bir mesaj deposu oluşturun
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Dinamik Bellek*

Bu bellek, ajanlar çalıştırılmadan önce bağlama eklenir. Bu bellek dış hizmetlerde, örneğin mem0 gibi, saklanabilir:

```python
from agent_framework.mem0 import Mem0Provider

# Gelişmiş bellek yetenekleri için Mem0 kullanılıyor
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

**Ajan Gözlemlenebilirliği**

Gözlemlenebilirlik, güvenilir ve sürdürülebilir ajan sistemleri kurmak için önemlidir. MAF, daha iyi gözlemlenebilirlik için izlemeyi ve sayaçları sağlamak üzere OpenTelemetry ile entegre olur.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # bir şey yap
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### İş Akışları

MAF, AI ajanların bileşen olarak kullanıldığı, bir görevi tamamlamak için önceden tanımlanmış adımlardan oluşan iş akışları sunar.

İş akışları, daha iyi kontrol akışı sağlayan çeşitli bileşenlerden oluşur. İş akışları ayrıca **çok ajanlı orkestrasyon** ve iş akış durumu kaydetmek için **checkpointing** özelliği sağlar.

Bir iş akışının temel bileşenleri şunlardır:

**Yürütücüler**

Yürütücüler giriş mesajları alır, atanan görevlerini yerine getirir ve bir çıkış mesajı üretir. Bu, iş akışını daha büyük görevin tamamlanmasına doğru ilerletir. Yürütücüler AI ajanı veya özel mantık olabilir.

**Kenarlar**

Kenarlar, iş akışındaki mesaj akışını tanımlamak için kullanılır. Bunlar şunlar olabilir:

*Doğrudan Kenarlar* - Yürütücüler arasında basit birebir bağlantılar:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Koşullu Kenarlar* - Belirli bir koşul karşılandığında etkinleşir. Örneğin, otel odaları yoksa, bir yürütücü başka seçenekler önerebilir.

*Switch-case Kenarlar* - Tanımlı koşullara göre mesajları farklı yürütücülere yönlendirir. Örneğin, seyahat müşterisi öncelikli erişime sahipse ve görevleri başka bir iş akışından yönetiliyorsa.

*Fan-out Kenarlar* - Bir mesajı birden çok hedefe gönderir.

*Fan-in Kenarlar* - Farklı yürütücülerden birden çok mesajı toplar ve tek bir hedefe gönderir.

**Olaylar**

İş akışlarında daha iyi gözlemlenebilirlik sağlamak için MAF, yürütme için yerleşik olaylar sunar:

- `WorkflowStartedEvent`  - İş akışı yürütmesi başlar
- `WorkflowOutputEvent` - İş akışı çıktı üretir
- `WorkflowErrorEvent` - İş akışı hata ile karşılaşır
- `ExecutorInvokeEvent`  - Yürütücü işlemeye başlar
- `ExecutorCompleteEvent`  - Yürütücü işlemeyi tamamlar
- `RequestInfoEvent` - Bir istek yapılır

## İleri Seviye MAF Desenleri

Yukarıdaki bölümler Microsoft Agent Framework'ün temel kavramlarını kapsar. Daha karmaşık ajanlar oluştururken göz önünde bulundurabileceğiniz bazı ileri desenler:

- **Ara Yazılım Bileşimi**: Ajan davranışını ince ayarla kontrol etmek için fonksiyon ve sohbet ara yazılımlarını kullanarak (kayıt, kimlik doğrulama, hız sınırlama) birden fazla ara yazılım işleyicisini zincirleme.
- **İş Akışı Checkpointing**: Uzun süre çalışan ajan süreçlerini kaydetmek ve devam ettirmek için iş akışı olaylarını ve serileştirmeyi kullanma.
- **Dinamik Araç Seçimi**: Sorguya özel sadece ilgili araçları sunmak için araç açıklamaları üzerinde RAG ve MAF'nın araç kaydını birleştirin.
- **Çoklu Ajan Devir Teslimi**: Uzmanlaşmış ajanlar arasında devirleri orkestre etmek için iş akışı kenarları ve koşullu yönlendirmeyi kullanma.

## Kod Örnekleri

Microsoft Agent Framework için kod örnekleri bu depoda `xx-python-agent-framework` ve `xx-dotnet-agent-framework` dosyaları altında bulunabilir.

## Microsoft Agent Framework Hakkında Daha Fazla Sorunuz Mu Var?

Diğer öğrenenlerle tanışmak, çalışma saatlerine katılmak ve AI Ajanları ile ilgili sorularınızı sormak için [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)'a katılın.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi ana dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı nedeniyle oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->