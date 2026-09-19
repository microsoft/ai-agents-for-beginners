# Microsoft Agent Framework'ü Keşfetmek

![Agent Framework](../../../translated_images/tr/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Giriş

Bu ders şunları kapsayacaktır:

- Microsoft Agent Framework'ü Anlamak: Temel Özellikler ve Değer  
- Microsoft Agent Framework'ün Temel Kavramlarını Keşfetmek
- Gelişmiş MAF Desenleri: İş Akışları, Middleware ve Bellek

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra şunları bileceksiniz:

- Microsoft Agent Framework kullanarak Üretime Hazır AI Ajanları oluşturmak
- Microsoft Agent Framework'ün temel özelliklerini Ajanik Kullanım Durumlarınıza uygulamak
- İş akışları, middleware ve gözlemlenebilirlik dahil gelişmiş desenleri kullanmak

## Kod Örnekleri 

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) için kod örnekleri bu depoda `xx-python-agent-framework` ve `xx-dotnet-agent-framework` dosyaları altında bulunabilir.

## Microsoft Agent Framework'ü Anlamak

![Framework Intro](../../../translated_images/tr/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python), Microsoft'un AI ajanları oluşturmak için birleşik çerçevesidir. Üretim ve araştırma ortamlarında görülen çeşitli ajanik kullanım durumlarını ele alacak esnekliği sunar:

- **Sıralı Ajan orkestrasyonu**: Adım adım iş akışlarının gerektiği senaryolarda.
- **Eşzamanlı orkestrasyon**: Ajanların aynı anda görevleri tamamlaması gereken senaryolarda.
- **Grup sohbeti orkestrasyonu**: Ajanların birlikte tek bir görev üzerinde işbirliği yapabildikleri senaryolarda.
- **Görev devri orkestrasyonu**: Alt görevler tamamlandıkça ajanların görevleri birbirine devrettiği senaryolarda.
- **Manyetik orkestrasyon**: Yönetici ajanın bir görev listesi oluşturup değiştirdiği ve alt ajanların koordinasyonunu sağladığı senaryolarda.

AI Ajanları Üretimde sunabilmek için MAF ayrıca şu özelliklere de sahiptir:

- **Gözlemlenebilirlik**: Microsoft Foundry panoları üzerinden araç çağrısı, orkestrasyon adımları, mantık akışları ve performans izleme dahil her AI Ajan action'ı OpenTelemetry kullanılarak izlenir.
- **Güvenlik**: Ajanlar, rol tabanlı erişim, özel veri işleme ve yerleşik içerik güvenliği gibi güvenlik kontrollerini içeren Microsoft Foundry üzerinde yerel olarak barındırılır.
- **Dayanıklılık**: Ajan iş parçacıkları ve iş akışları duraklatılabilir, devam ettirilebilir ve hatalardan kurtarılabilir; böylece uzun süre çalışan süreçlere imkan tanır.
- **Kontrol**: İnsan denetimli iş akışları desteklenir ve görevler insan onayı gerektirir olarak işaretlenebilir.

Microsoft Agent Framework ayrıca birlikte çalışabilirliğe odaklanmıştır:

- **Bulut-bağımsız olmak** - Ajanlar konteynerlerde, yerelde ve birden fazla farklı bulut üzerinde çalışabilir.
- **Sağlayıcı-bağımsız olmak** - Ajanlar tercih ettiğiniz SDK kullanılarak oluşturulabilir; Azure OpenAI ve OpenAI dahil.
- **Açık Standartları Entegre etmek** - Ajanlar Agent-to-Agent (A2A) ve Model Context Protocol (MCP) gibi protokolleri kullanarak diğer ajanları ve araçları keşfedip kullanabilir.
- **Eklentiler ve Bağlayıcılar** - Bağlantılar Microsoft Fabric, SharePoint, Pinecone ve Qdrant gibi veri ve bellek servislerine yapılabilir.

Şimdi Microsoft Agent Framework'ün bazı temel kavramlarına bu özelliklerin nasıl uygulandığına bakalım.

## Microsoft Agent Framework'ün Temel Kavramları

### Ajanlar

![Agent Framework](../../../translated_images/tr/agent-components.410a06daf87b4fef.webp)

**Ajan Oluşturma**

Ajan oluşturma, çıkarım servisi (LLM Sağlayıcısı), AI Ajan'ın izleyeceği
talimatlar seti ve atanmış bir `name` tanımlanarak yapılır:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Yukarıdaki örnek `Azure OpenAI` kullanmakta ama ajanlar `Microsoft Foundry Agent Service` dahil çeşitli servislerle oluşturulabilir:

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

veya büyük bağlam pencereleri (204K token'a kadar) sunan OpenAI uyumlu API sağlayan [MiniMax](https://platform.minimaxi.com/) ile:

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

veya A2A protokolü kullanarak uzaktaki ajanlar ile:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Ajanları Çalıştırma**

Ajanlar, yayın veya yayın akışı yanıtları için `.run` veya `.run_stream` metodlarıyla çalıştırılır.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Her ajan çalıştırma, ajan tarafından kullanılan `max_tokens`, çağrılabilecek `tools` ve hatta kullanılan `model` gibi parametreleri özelleştirmek için seçeneklere sahip olabilir.

Bu, kullanıcının görevinin tamamlanması için belirli model veya araçların gerektiği durumlarda faydalıdır.

**Araçlar**

Araçlar ajan tanımı yapılırken de tanımlanabilir:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Bir ChatAgent doğrudan oluşturulurken

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

ve ajan çalıştırılırken de:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Sadece bu çalışma için sağlanan araç )
```

**Ajan İş Parçacıkları**

Ajan İş Parçacıkları çoklu tur konuşmaları yönetmek için kullanılır. İş parçacıkları şu şekilde oluşturulabilir:

- Zaman içinde iş parçacığını kaydetmeyi sağlayan `get_new_thread()` kullanarak
- Bir ajan çalıştırılırken otomatik olarak oluşturulan ve sadece mevcut çalışma süresince devam eden iş parçacığı oluşturarak.

İş parçacığı oluşturma kodu aşağıdaki gibidir:

```python
# Yeni bir iş parçacığı oluşturun.
thread = agent.get_new_thread() # İş parçacığı ile ajanı çalıştırın.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Ardından iş parçacığını daha sonra kullanmak üzere serileştirebilirsiniz:

```python
# Yeni bir iş parçacığı oluştur.
thread = agent.get_new_thread() 

# İş parçacığı ile ajanı çalıştır.

response = await agent.run("Hello, how are you?", thread=thread) 

# Depolama için iş parçacığını serileştir.

serialized_thread = await thread.serialize() 

# Depolamadan yükledikten sonra iş parçacığı durumunu deserialize et.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Ajan Middleware**

Ajanlar, kullanıcının görevlerini tamamlamak için araçlar ve LLM'lerle etkileşir. Belirli senaryolarda bu etkileşimlerin arasında işlem yapmak veya izlemek isteyebiliriz. Ajan middleware bu işlemleri şöyle mümkün kılar:

*Fonksiyon Middleware'i*

Bu middleware, ajan ile çağrılacak fonksiyon/araç arasında bir eylemin gerçekleşmesini sağlar. Bir örnek olarak, fonksiyon çağrısı üzerine bazı loglama yapmak isteyebilirsiniz.

Aşağıdaki koddaki `next`, bir sonraki middleware veya gerçek fonksiyonun çağrılıp çağrılmayacağını tanımlar.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Ön işleme: Fonksiyon çalıştırılmadan önce loglama
    print(f"[Function] Calling {context.function.name}")

    # Bir sonraki middleware veya fonksiyon çalıştırmaya devam et
    await next(context)

    # Son işlem: Fonksiyon çalıştırıldıktan sonra loglama
    print(f"[Function] {context.function.name} completed")
```

*Sohbet Middleware'i*

Bu middleware, ajan ile LLM arasındaki istekler arasında bir işlem ya da loglama yapılmasını sağlar.

Bu, AI servisine gönderilen `messages` gibi önemli bilgileri içerir.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Ön işleme: AI çağrısından önce kayıt tut
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Bir sonraki ara katmana veya AI servisine devam et
    await next(context)

    # Son işlem: AI yanıtından sonra kayıt tut
    print("[Chat] AI response received")

```

**Ajan Belleği**

`Agentic Memory` dersinde anlatıldığı gibi, bellek ajanların farklı bağlamlar içinde çalışabilmesi için önemli bir bileşendir. MAF farklı tipte bellekler sunar:

*Anlık Bellek Depolaması*

Bu, uygulama çalışma zamanında iş parçacıklarında saklanan bellektir.

```python
# Yeni bir iş parçacığı oluşturun.
thread = agent.get_new_thread() # İş parçacığı ile ajanı çalıştırın.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Kalıcı Mesajlar*

Bu bellek, farklı oturumlar arasında konuşma geçmişini saklamak için kullanılır. `chat_message_store_factory` ile tanımlanır:

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

Bu bellek, ajanlar çalıştırılmadan önce bağlama eklenir. Bu bellekler mem0 gibi harici servislerde saklanabilir:

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

Gözlemlenebilirlik, güvenilir ve sürdürülebilir ajanik sistemler kurmak için önemlidir. MAF, daha iyi gözlemlenebilirlik için OpenTelemetry ile izleme ve sayaçlar sağlar.

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

MAF, bir görevi tamamlamak için önceden tanımlı adımlar sunan iş akışları sağlar ve bu adımlar içinde AI ajanları bileşen olarak bulunur.

İş akışları, daha iyi kontrol akışı sağlayan farklı bileşenlerden oluşur. Ayrıca **çoklu ajan orkestrasyonu** ve iş akışı durumlarını kaydetmek için **checkpointing** sağlar.

Bir iş akışının temel bileşenleri:

**Yürütücüler**

Yürütücüler gelen mesajları alır, atanan görevleri yapar ve çıktı mesajı üretir. Bu, iş akışını büyük görevin tamamlanmasına doğru ilerletir. Yürütücüler AI ajan veya özel mantık olabilir.

**Kenarlar**

Kenarlar iş akışındaki mesaj akışını tanımlamak için kullanılır. Bunlar şu türlerde olabilir:

*Doğrudan Kenarlar* - Yürütücüler arasında basit birebir bağlantılar:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Koşullu Kenarlar* - Belirli koşul karşılandığında etkinleşir. Örneğin, otel odaları müsait değilse, bir yürütücü diğer seçenekleri önerebilir.

*Switch-case Kenarlar* - Mesajları tanımlı koşullara göre farklı yürütücülere yönlendirir. Örneğin, seyahat müşterisi öncelikli erişime sahipse ve görevleri başka bir iş akışıyla ele alınacaksa.

*Yayılma (Fan-out) Kenarlar* - Tek bir mesajı birden çok hedefe gönderir.

*Toplanma (Fan-in) Kenarlar* - Farklı yürütücülerden gelen çoklu mesajları tek hedefe toplar.

**Olaylar**

İş akışlarına daha iyi gözlemlenebilirlik sağlamak için, MAF yürütmeye ilişkin yerleşik olaylar sunar:

- `WorkflowStartedEvent`  - İş akışı yürütmesi başlar
- `WorkflowOutputEvent` - İş akışı çıktı üretir
- `WorkflowErrorEvent` - İş akışı hata ile karşılaşır
- `ExecutorInvokeEvent`  - Yürütücü işlemeye başlar
- `ExecutorCompleteEvent`  - Yürütücü işlemi bitirir
- `RequestInfoEvent` - Bir istek yapılır

## Gelişmiş MAF Desenleri

Yukarıdaki bölümler Microsoft Agent Framework'ün ana kavramlarını kapsar. Daha karmaşık ajanlar oluştururken dikkate alabileceğiniz bazı gelişmiş desenler şunlardır:

- **Middleware Bileşimi**: Fonksiyon ve sohbet middleware kullanarak çoklu middleware işleyicilerini (loglama, kimlik doğrulama, hız sınırlama) zincirleyin ve ajan davranışı üzerinde ince ayar yapın.
- **İş Akışı Checkpointing**: Uzun süreli ajan süreçlerini kaydetmek ve devam ettirmek için iş akışı olayları ve serileştirme kullanın.
- **Dinamik Araç Seçimi**: Araç açıklamaları üzerinde RAG'i MAF'nin araç kaydıyla birleştirerek her sorgu için yalnızca ilgili araçları sunun.
- **Çoklu Ajan Görev Devri**: İş akışı kenarları ve koşullu yönlendirme kullanarak uzmanlaşmış ajanlar arasında görev devrini orkestre edin.

## Microsoft Foundry Üzerinde LangChain / LangGraph Ajanlarını Barındırmak

Microsoft Agent Framework **çerçeve-uyumlu**dur — yalnızca MAF ile yazılmış ajanlarla sınırlı değilsiniz. Zaten **LangChain** veya **LangGraph** ile yazılmış bir ajana sahipseniz, bunu **Microsoft Foundry tarafından barındırılan ajan** olarak çalıştırabilirsiniz; böylece Foundry çalışma zamanı, oturumlar, ölçeklendirme, kimlik ve protokol uç noktalarını yönetirken, ajan mantığınız LangGraph'da kalır.

Bu, Foundry’nin barındırdığı ajanların kullandığı protokoller üzerinden derlenmiş LangGraph grafiği sunan `langchain_azure_ai.agents.hosting` paketi ile yapılır.

**1. Hosting eklentisini kurun:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

`hosting` eklentisi Foundry protokol kütüphanelerini yükler: `azure-ai-agentserver-responses` (OpenAI uyumlu `/responses` uç noktası) ve `azure-ai-agentserver-invocations` (genel `/invocations` uç noktası).

**2. Bir hosting protokolü seçin:**

| Protokol | Host sınıfı | Uç Nokta | Kullanım Durumu |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | OpenAI uyumlu sohbet, yayın akışı, yanıt geçmişi ve sohbet iş parçacığına ihtiyacınız varsa — konuşma ajanları için önerilen varsayılan. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Özel JSON yapısı, webhook tarzı uç nokta veya konuşma dışı işlem gerekiyorsa. |

Çünkü **Responses API, Foundry'de ajan tarzı geliştirme için birincil API**dir, çoğu ajan için `ResponsesHostServer` ile başlayın.

**3. Ortam değişkenlerini yapılandırın** (`az login` yapın ki `DefaultAzureCredential` kimlik doğrulaması yapabilsin):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Ajan daha sonra Foundry'de barındırılan ajan olarak çalıştığında, platform `FOUNDRY_PROJECT_ENDPOINT` değerini otomatik olarak enjekte eder.

**4. Responses protokolü üzerinden bir LangGraph ajanı sunun:**

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

    # ChatOpenAI burada Foundry projesinin OpenAI uyumlu (Yanıtlar) uç noktasını hedefliyor.
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

Yerelde `python main.py` ile çalıştırın, sonra `http://localhost:8088/responses` adresine bir Responses isteği gönderin.

**Ana davranışlar:**

- **Konuşmalar**: İstemciler, `previous_response_id` veya `conversation` ID göndererek bir konuşmayı sürdürür. Grafiğiniz LangGraph checkpointer ile derlendiyse, Foundry konuşma durumunu checkpointer ile eşler (üretimde dayanıklı checkpointer kullanın; yerel test için `MemorySaver` yeterlidir).
- **İnsan arayüzünde müdahale**: Grafiğiniz LangGraph `interrupt()` kullanıyorsa, `ResponsesHostServer` bekleyen kesintiyi bir Responses `function_call` / `mcp_approval_request` öğesi olarak gösterir ve istemciler eşleşen `function_call_output` / `mcp_approval_response` ile devam eder.
- **Foundry'ye dağıtım**: Azure Developer CLI kullanın — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (yerel, Docker gerektirir), sonra `azd provision` ve `azd deploy`. Barındırılan ajan dağıtımı için **Foundry Proje Yöneticisi** rolü gereklidir.

Bu örneğin çalıştırılabilir versiyonu [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py) dosyasında. Tam kılavuz (Invocations protokolü, özel istek şemaları ve sorun giderme) için [Foundry barındırılan ajanlar olarak LangGraph ajanlarını barındırma](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) sayfasına bakın.

## Kod Örnekleri 

Microsoft Agent Framework için kod örnekleri bu depoda `xx-python-agent-framework` ve `xx-dotnet-agent-framework` dosyaları altında bulunabilir.

## Microsoft Agent Framework Hakkında Daha Fazla Sorunuz mu Var?

Diğer öğrenenlerle tanışmak, danışma saatlerine katılmak ve AI Ajanlar ile ilgili sorularınızı sormak için [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)'a katılın.
## Önceki Ders

[AI Ajanlar için Bellek](../13-agent-memory/README.md)

## Sonraki Ders

[Bilgisayar Kullanım Ajanları (CUA) Oluşturmak](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->