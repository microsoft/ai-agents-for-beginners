# Microsoft Agent Framework'ü Keşfetmek

![Agent Framework](../../../translated_images/tr/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Giriş

Bu ders şunları kapsayacak:

- Microsoft Agent Framework'ü Anlamak: Temel Özellikler ve Değer  
- Microsoft Agent Framework'ün Temel Kavramlarını Keşfetmek
- Gelişmiş MAF Desenleri: İş Akışları, Ara Katman ve Bellek

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra şunları bileceksiniz:

- Microsoft Agent Framework kullanarak Üretime Hazır AI Ajanları oluşturmak
- Microsoft Agent Framework'ün temel özelliklerini Agentik Kullanım Durumlarınıza uygulamak
- İş akışları, ara katman ve gözlemlenebilirlik dahil gelişmiş desenleri kullanmak

## Kod Örnekleri

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) için kod örnekleri bu depoda `xx-python-agent-framework` ve `xx-dotnet-agent-framework` dosyalarında bulunabilir.

## Microsoft Agent Framework'ü Anlamak

![Framework Intro](../../../translated_images/tr/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework), AI ajanları oluşturmak için Microsoft'un birleşik çerçevesidir. Üretim ve araştırma ortamlarında görülen çeşitli agentik kullanım durumlarına esnek çözümler sunar:

- Adım adım iş akışlarının gerekli olduğu senaryolarda **Sekansiyel Ajan orkestrasyonu**.
- Ajanların aynı anda görevleri tamamlaması gereken senaryolarda **Eşzamanlı orkestrasyon**.
- Ajanların tek bir görev üzerinde birlikte çalışabildiği senaryolarda **Grup sohbeti orkestrasyonu**.
- Alt görevler tamamlandıkça ajanların görevi birbirine devrettiği senaryolarda **Devir teslim orkestrasyonu**.
- Yönetici ajanın görev listesi oluşturduğu ve alt ajanların koordinasyonunu sağladığı senaryolarda **Manyetik orkestrasyon**.

Üretimde AI Ajanları sağlamak için MAF ayrıca şunları içerir:

- AI Ajanın her eylemi dahil olmak üzere araç çağrısı, orkestrasyon adımları, akıl yürütme akışları ve Microsoft Foundry panelleriyle performans izleme için OpenTelemetry ile **Gözlemlenebilirlik**.
- Rol bazlı erişim, özel veri işleme ve yerleşik içerik güvenliği gibi güvenlik kontrolleri içeren Microsoft Foundry'de ajanların yerel olarak barındırılmasıyla **Güvenlik**.
- Ajan iş parçacıkları ve iş akışlarının duraklatılıp, devam ettirilebilmesi ve hatalardan kurtarılabilmesiyle **Dayanıklılık**.
- İnsan onayının gereken görevler için destek sağlayan insan destekli iş akışları ile **Kontrol**.

Microsoft Agent Framework ayrıca aşağıdaki şekillerde birlikte çalışabilirliği hedefler:

- **Bulut bağımsız** - Ajanlar konteynerlerde, şirket içi ve birden çok farklı bulutta çalıştırılabilir.
- **Sağlayıcı bağımsız** - Ajanlar tercih ettiğiniz SDK ile oluşturulabilir; Azure OpenAI ve OpenAI dahil.
- **Açık Standartlarla Entegrasyon** - Ajanlar, diğer ajanları ve araçları keşfetmek ve kullanmak için Agent-to-Agent (A2A) ve Model Context Protocol (MCP) gibi protokolleri kullanabilir.
- **Eklentiler ve Bağlayıcılar** - Microsoft Fabric, SharePoint, Pinecone ve Qdrant gibi veri ve bellek hizmetlerine bağlantılar kurulabilir.

Bu özelliklerin Microsoft Agent Framework'ün bazı temel kavramlarına nasıl uygulandığına bakalım.

## Microsoft Agent Framework'ün Temel Kavramları

### Ajanlar

![Agent Framework](../../../translated_images/tr/agent-components.410a06daf87b4fef.webp)

**Ajanları Oluşturma**

Ajan oluşturma, çıkarım servisini (LLM Sağlayıcısı), AI Ajanının takip etmesi gereken talimatlar setini ve atanmış bir `name` belirleyerek yapılır:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Yukarıdaki `Azure OpenAI` kullanıyor, ancak ajanlar `Microsoft Foundry Agent Service` dahil çeşitli servislerle oluşturulabilir:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` API'leri

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

veya büyük bağlam pencereleri (204K token'a kadar) ile OpenAI uyumlu API sağlayan [MiniMax](https://platform.minimaxi.com/):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

veya A2A protokolü kullanan uzak ajanlar:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Ajanları Çalıştırma**

Ajanlar, akışsız veya akışlı yanıtlar için `.run` veya `.run_stream` yöntemleriyle çalıştırılır.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Her ajan çalıştırma, `max_tokens` gibi parametreleri, ajan tarafından çağrılabilen `tools` ve ajan için kullanılan `model` gibi özelleştirme seçeneklerine sahip olabilir.

Bu, belirli modellerin veya araçların kullanıcının görevini tamamlamak için gerekli olduğu durumlarda faydalıdır.

**Araçlar**

Araçlar hem ajan tanımlanırken hem de ajan çalıştırılırken tanımlanabilir:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Bir ChatAgent doğrudan oluşturulurken

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

ve ayrıca ajan çalıştırılırken:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Bu çalışma için sağlanan araç sadece )
```

**Ajan İş Parçacıkları**

Ajan İş Parçacıkları çok turlu konuşmaları yönetmek için kullanılır. İş parçacıkları ya:

- `get_new_thread()` kullanılarak zaman içinde kaydedilebilir şekilde oluşturulur
- Ajan çalıştırılırken otomatik olarak oluşturulur ve iş parçacığı sadece mevcut çalışma boyunca devam eder.

İş parçacığı oluşturmak için kod şöyle olur:

```python
# Yeni bir iş parçacığı oluşturun.
thread = agent.get_new_thread() # İş parçacığı ile ajanı çalıştırın.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Daha sonra iş parçacığını saklamak için serileştirebilirsiniz:

```python
# Yeni bir iş parçacığı oluşturun.
thread = agent.get_new_thread() 

# Ajansı iş parçacığı ile çalıştırın.

response = await agent.run("Hello, how are you?", thread=thread) 

# İş parçacığını depolama için serileştirin.

serialized_thread = await thread.serialize() 

# Depolamadan yükledikten sonra iş parçacığı durumunu serileştirmeden çıkarın.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Ajan Ara Katmanı**

Ajanlar, kullanıcıların görevlerini tamamlamak için araçlar ve LLM'lerle etkileşir. Belirli senaryolarda bu etkileşimlerin arasında işlem yapmak veya izlemek isteriz. Ajan ara katmanı bunu şu şekilde sağlar:

*Fonksiyon Ara Katmanı*

Bu ara katman, ajan ile çağıracağı fonksiyon/araç arasında bir işlem yapmamıza izin verir. Örneğin fonksiyon çağrısı üzerinde loglama yapmak istenebilir.

Aşağıdaki kodda `next`, sonraki ara katman mı yoksa gerçek fonksiyonun mu çağrılacağını belirler.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Ön işleme: Fonksiyon çalıştırılmadan önce log kaydı
    print(f"[Function] Calling {context.function.name}")

    # Sonraki ara yazılıma veya fonksiyon çalıştırmaya devam et
    await next(context)

    # Son işlem: Fonksiyon çalıştırıldıktan sonra log kaydı
    print(f"[Function] {context.function.name} completed")
```

*Sohbet Ara Katmanı*

Bu ara katman, ajan ile LLM arasındaki istekler arasında işlem yapmamıza veya log tutmamıza olanak sağlar.

Bu, AI servisine gönderilen `messages` gibi önemli bilgileri içerir.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Ön işleme: AI çağrısından önce kayıt tut
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Bir sonraki ara katman veya AI hizmetine devam et
    await next(context)

    # Son işlem: AI yanıtından sonra kayıt tut
    print("[Chat] AI response received")

```

**Ajan Belleği**

`Agentic Memory` dersinde anlatıldığı gibi, bellek ajanın farklı bağlamlar üzerinde çalışmasını sağlayan önemli bir öğedir. MAF çeşitli bellek türleri sunar:

*Bellek İçi Depolama*

Bu, uygulama çalışma zamanı sırasında iş parçacıklarında tutulan bellektir.

```python
# Yeni bir iş parçacığı oluşturun.
thread = agent.get_new_thread() # İş parçacığıyla ajanı çalıştırın.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Kalıcı Mesajlar*

Bu bellek farklı oturumlar boyunca konuşma geçmişini saklamak için kullanılır. `chat_message_store_factory` ile tanımlanır:

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

Bu bellek, ajanlar çalıştırılmadan önce bağlama eklenir. Mem0 gibi harici servislerde saklanabilir:

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

Gözlemlenebilirlik, güvenilir ve sürdürülebilir agentik sistemler oluşturmak için önemlidir. MAF, daha iyi gözlemlenebilirlik için OpenTelemetry ile izleme ve sayaçlar sağlar.

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

MAF, bir görevi tamamlamak için önceden tanımlanmış adımlardan oluşan iş akışları sunar ve bu adımlar içinde AI ajanları bileşen olarak bulunur.

İş akışları, daha iyi kontrol akışı sağlayan farklı bileşenlerden oluşur. İş akışları ayrıca **çoklu ajan orkestrasyonu** ve iş akışı durumlarını kaydetmek için **checkpointing** sağlar.

Bir iş akışının temel bileşenleri:

**Yürütücüler**

Yürütücüler, giriş mesajları alır, atanan görevleri gerçekleştirir ve çıktı mesajı üretir. Bu, iş akışını daha büyük görevin tamamlanmasına doğru ilerletir. Yürütücüler AI ajan veya özel mantık olabilir.

**Kenarlar**

Kenarlar, bir iş akışında mesajların akışını tanımlamak için kullanılır. Bunlar:

*Doğrudan Kenarlar* - Yürütücüler arasında basit birebir bağlantılar:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Şarta Bağlı Kenarlar* - Belirli koşullar gerçekleştiğinde aktif olur. Örneğin otel odaları yoksa başka seçenekler önerilir.

*Anahtar-Kutusu Kenarları* - Tanımlı koşullara göre mesajları farklı yürütücülere yönlendirir. Örneğin, seyahat müşterisinin öncelikli erişimi varsa görevleri başka bir iş akışı ile yönetilir.

*Çoklu Gönderen Kenarlar* - Bir mesajı birden çok hedefe gönderir.

*Çoklu Alan Kenarlar* - Farklı yürütücülerden gelen birden fazla mesajı toplar ve tek hedefe gönderir.

**Olaylar**

İş akışlarına daha iyi gözlemlenebilirlik sağlamak için MAF, yürütme sırasında yerleşik olaylar sunar:

- `WorkflowStartedEvent`  - İş akışı yürütmesi başlıyor
- `WorkflowOutputEvent` - İş akışı çıktı üretiyor
- `WorkflowErrorEvent` - İş akışı hata ile karşılaşıyor
-  `ExecutorInvokeEvent`  - Yürütücü işlemeye başlıyor
- `ExecutorCompleteEvent`  -  Yürütücü işini tamamlıyor
- `RequestInfoEvent` - Bir istek yapılıyor

## Gelişmiş MAF Desenleri

Yukarıdaki bölümler Microsoft Agent Framework'ün temel kavramlarını kapsar. Daha karmaşık ajanlar oluşturdukça göz önünde bulundurmanız gereken bazı gelişmiş desenler:

- **Ara Katman Birleştirme**: Fonksiyon ve sohbet ara katmanları kullanarak çoklu ara katman işleyicilerini (loglama, kimlik doğrulama, oran sınırlaması) zincirleyin ve ajan davranışı üzerinde ince ayar kontrolü sağlayın.
- **İş Akışı Checkpointing**: Uzun süreli ajan süreçlerini kaydetmek ve devam ettirmek için iş akışı olayları ve serileştirme kullanın.
- **Dinamik Araç Seçimi**: Sorgu başına yalnızca ilgili araçları sunmak için MAF'nin araç kaydı ile RAG'yi araç açıklamaları üzerinde birleştirin.
- **Çoklu Ajan Devir Teslimi**: Uzmanlaşmış ajanlar arasında devir teslimi orkestre etmek için iş akışı kenarları ve koşullu yönlendirmeyi kullanın.

## Microsoft Foundry'de LangChain / LangGraph Ajanlarını Barındırma

Microsoft Agent Framework **çerçeve-uyumlu**dur — MAF ile yazılmış ajanlarla sınırlı değilsiniz. Eğer zaten **LangChain** veya **LangGraph** ile oluşturulmuş bir ajanınız varsa, bunu **Microsoft Foundry tarafından barındırılan ajan** olarak çalıştırabilirsiniz; böylece Foundry çalışma zamanı, oturumlar, ölçeklendirme, kimlik ve protokol uç noktalarını yönetirken, ajan mantığınız LangGraph içinde kalır.

Bu, aynı protokoller üzerinden derlenmiş bir LangGraph grafiği sunan `langchain_azure_ai.agents.hosting` paketi ile yapılır.

**1. Hosting ekstra paketini yükleyin:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` ekstra paketi Foundry protokol kütüphanelerini yükler: `azure-ai-agentserver-responses` (OpenAI uyumlu `/responses` uç noktası) ve `azure-ai-agentserver-invocations` (genel `/invocations` uç noktası).

**2. Bir hosting protokolü seçin:**

| Protokol | Sunucu Sınıfı | Uç Nokta | Kullanım Durumu |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | OpenAI uyumlu sohbet, akış, yanıt geçmişi ve konuşma iş parçacığı için — konuşma ajanları için önerilen varsayılan. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Özel JSON şekli, webhook tarzı uç nokta veya konuşma dışı işlemler için. |

Çünkü **Responses API Foundry'deki ajan tarzı geliştirme için birincil API'dir**, çoğu ajan için `ResponsesHostServer` ile başlayın.

**3. Ortam değişkenlerini yapılandırın** (`az login` yapın ki `DefaultAzureCredential` kimlik doğrulaması yapabilsin):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Daha sonra ajan Foundry'de barındırılan ajan olarak çalıştığında, platform otomatik olarak `FOUNDRY_PROJECT_ENDPOINT` değişkenini enjekte eder.

**4. Responses protokolü üzerinden bir LangGraph ajanı açığa çıkarın:**

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

    # ChatOpenAI burada Foundry projesinin OpenAI uyumlu (Yanıtlar) uç noktasını hedeflemektedir.
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

Bunu yerel olarak `python main.py` ile çalıştırın, sonra `http://localhost:8088/responses` adresine Responses isteği gönderin.

**Ana davranışlar:**

- **Konuşmalar**: İstemciler `previous_response_id` veya `conversation` ID'si geçerek bir konuşmayı devam ettirir. Grafiğiniz LangGraph checkpointer ile derlenmişse, Foundry konuşma durumunu checkpoint'e anahtarlar (üretimde dayanıklı checkpointer kullanın; `MemorySaver` yerel test için yeterlidir).
- **İnsan döngüsü içinde**: Grafiğiniz LangGraph `interrupt()` kullanıyorsa, `ResponsesHostServer` bekleyen kesintiyi Responses `function_call` / `mcp_approval_request` öğesi olarak sunar ve istemciler eşleşen `function_call_output` / `mcp_approval_response` ile devam eder.
- **Foundry'e Dağıtım**: Azure Developer CLI kullanın — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (yerel, Docker gerektirir), ardından `azd provision` ve `azd deploy`. Barındırılan ajan dağıtımı **Foundry Proje Yöneticisi** rolü gerektirir.

Bu örneğin çalışır bir versiyonu [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) içinde yer alır. Tam yürüyüş (Invocations protokolü, özel istek şemaları ve sorun giderme) için, [Foundry barındırılan ajanlar olarak LangGraph ajanlarını barındır](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) sayfasına bakın.

## Kod Örnekleri

Microsoft Agent Framework için kod örnekleri bu depoda `xx-python-agent-framework` ve `xx-dotnet-agent-framework` dosyalarında bulunabilir.

## Microsoft Agent Framework hakkında daha fazla sorunuz mu var?

Diğer öğrenenlerle tanışmak, danışmanlık saatlerine katılmak ve AI Ajanları ile ilgili sorularınızı sormak için [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)'a katılın.
## Önceki Ders

[AI Ajanları için Bellek](../13-agent-memory/README.md)

## Sonraki Ders

[Bilgisayar Kullanım Ajanları (CUA) Oluşturma](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->