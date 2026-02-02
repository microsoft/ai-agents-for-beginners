[![İyi AI Ajanları Nasıl Tasarlanır](../../../translated_images/tr/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Bu dersin videosunu izlemek için yukarıdaki görsele tıklayın)_

# Araç Kullanım Tasarım Deseni

Araçlar ilginçtir çünkü AI ajanlarının daha geniş bir yetenek yelpazesine sahip olmalarını sağlar. Ajanın gerçekleştirebileceği sınırlı bir eylem seti yerine, bir araç ekleyerek, ajan artık çok çeşitli eylemler gerçekleştirebilir. Bu bölümde, AI ajanlarının hedeflerine ulaşmak için belirli araçları nasıl kullanabileceğini tanımlayan Araç Kullanım Tasarım Deseni'ne bakacağız.

## Giriş

Bu derste şu soruları yanıtlamaya çalışıyoruz:

- Araç kullanım tasarım deseni nedir?
- Hangi kullanım durumlarında uygulanabilir?
- Tasarım desenini uygulamak için gereken öğeler/yapı taşları nelerdir?
- Güvenilir AI ajanları oluşturmak için Araç Kullanım Tasarım Deseni'ni kullanırken özel olarak dikkat edilmesi gereken hususlar nelerdir?

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra şunları yapabileceksiniz:

- Araç Kullanım Tasarım Deseni'ni ve amacını tanımlamak.
- Bu tasarım deseninin uygulanabilir olduğu kullanım durumlarını belirlemek.
- Tasarım desenini uygulamak için gereken temel öğeleri anlamak.
- Bu tasarım desenini kullanan AI ajanlarında güvenilirliği sağlamak için dikkat edilmesi gerekenleri fark etmek.

## Araç Kullanım Tasarım Deseni Nedir?

**Araç Kullanım Tasarım Deseni**, LLM'lere belirli hedeflere ulaşmak için dış araçlarla etkileşim kurma yeteneği kazandırmaya odaklanır. Araçlar, bir ajanın eylemler gerçekleştirmek için çalıştırabileceği kod parçalarıdır. Bir araç, hesap makinesi gibi basit bir işlev olabileceği gibi, hisse senedi fiyat sorgulama veya hava durumu tahmini gibi üçüncü taraf bir hizmete yapılan API çağrısı da olabilir. AI ajanları bağlamında, araçlar **model tarafından oluşturulan fonksiyon çağrıları**na yanıt olarak ajanlar tarafından çalıştırılmak üzere tasarlanmıştır.

## Hangi kullanım durumlarında uygulanabilir?

AI Ajanları karmaşık görevleri tamamlamak, bilgi almak veya karar vermek için araçlardan yararlanabilir. Araç kullanım tasarım deseni, veritabanları, web servisleri veya kod yorumlayıcıları gibi dış sistemlerle dinamik etkileşim gerektiren senaryolarda sıkça kullanılır. Bu yetenek, aşağıdaki farklı kullanım durumları için faydalıdır:

- **Dinamik Bilgi Alma:** Ajanlar, güncel verileri almak için dış API'leri veya veritabanlarını sorgulayabilir (örn. veri analiz için SQLite veritabanı sorgulama, hisse senedi fiyatları veya hava durumu bilgisi alma).
- **Kod Çalıştırma ve Yorumlama:** Ajanlar matematiksel problemleri çözmek, raporlar üretmek veya simülasyonlar yapmak için kod veya betikler çalıştırabilir.
- **İş Akışı Otomasyonu:** Görev zamanlayıcılar, e-posta servisleri veya veri boru hatları gibi araçları entegre ederek tekrarlayan veya çok adımlı iş akışlarını otomatikleştirme.
- **Müşteri Desteği:** Ajanlar CRM sistemleri, bilet platformları veya bilgi tabanları ile etkileşimde bulunarak kullanıcı sorularını çözebilir.
- **İçerik Oluşturma ve Düzenleme:** Ajanlar, içerik oluşturma görevlerinde yardımcı olmak için dilbilgisi denetleyicileri, metin özetleyicileri veya içerik güvenliği değerlendiricileri gibi araçlardan faydalanabilir.

## Araç kullanım tasarım desenini uygulamak için gereken öğeler/yapı taşları nelerdir?

Bu yapı taşları, AI ajanın çok çeşitli görevleri gerçekleştirmesine olanak tanır. Araç Kullanım Tasarım Deseni'ni uygulamak için gereken ana öğelere bakalım:

- **Fonksiyon/Araç Şemaları**: Kullanılabilir araçların fonksiyon adı, amacı, gerekli parametreler ve beklenen çıktılar dahil olmak üzere detaylı tanımları. Bu şemalar, LLM'nin hangi araçların mevcut olduğunu ve geçerli istekleri nasıl oluşturacağını anlamasını sağlar.

- **Fonksiyon Çalıştırma Mantığı**: Araçların ne zaman ve nasıl çağrılacağını, kullanıcının niyeti ve sohbet bağlamına göre yönetir. Bu, planlayıcı modüller, yönlendirme mekanizmaları veya araç kullanımını dinamik olarak belirleyen koşullu akışlar içerebilir.

- **Mesaj Yönetim Sistemi**: Kullanıcı girdileri, LLM yanıtları, araç çağrıları ve araç çıktıları arasındaki konuşma akışını yöneten bileşenler.

- **Araç Entegrasyon Çerçevesi**: Ajanı basit fonksiyonlar veya karmaşık dış hizmetler olsun çeşitli araçlara bağlayan alt yapı.

- **Hata Yönetimi & Doğrulama**: Araç çalıştırmadaki hataları yönetme, parametreleri doğrulama ve beklenmedik yanıtları ele alma mekanizmaları.

- **Durum Yönetimi**: Çok adımlı etkileşimlerde tutarlılığı sağlamak için konuşma bağlamını, önceki araç etkileşimlerini ve kalıcı veriyi takip eder.

Sonra, Fonksiyon/Araç Çağrısını daha ayrıntılı inceleyelim.

### Fonksiyon/Araç Çağrısı

Fonksiyon çağrısı, Büyük Dil Modelleri'nin (LLM'ler) araçlarla etkileşim kurmalarını sağlayan temel yoldur. Genellikle 'Fonksiyon' ve 'Araç' terimleri birbirinin yerine kullanılır çünkü 'fonksiyonlar' (yeniden kullanılabilir kod blokları) ajanların görevleri yerine getirmek için kullandığı 'araçlardır'. Bir fonksiyonun kodunun çalıştırılabilmesi için, LLM kullanıcının isteğini fonksiyonun açıklamasıyla karşılaştırmalıdır. Bunun için tüm mevcut fonksiyonların açıklamalarını içeren bir şema LLM'ye gönderilir. LLM daha sonra görev için en uygun fonksiyonu seçer ve ismini ile argümanlarını döner. Seçilen fonksiyon çalıştırılır, yanıtı LLM'ye iletilir ve LLM bu bilgiyi kullanarak kullanıcı isteğine yanıt verir.

Geliştiricilerin ajanlar için fonksiyon çağrısını uygulayabilmesi için şunlara ihtiyaç vardır:

1. Fonksiyon çağrısını destekleyen bir LLM modeli
2. Fonksiyon açıklamalarını içeren bir şema
3. Tanımlanan her fonksiyon için kod

Bir şehre ait güncel saati alma örneğiyle açıklayalım:

1. **Fonksiyon çağrısını destekleyen bir LLM başlatın:**

    Her model fonksiyon çağrısını desteklemez, bu yüzden kullandığınız LLM'nin desteklediğinden emin olmak önemlidir. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> fonksiyon çağrısını destekler. Azure OpenAI istemcisini başlatarak başlayabiliriz.

    ```python
    # Azure OpenAI istemcisini başlat
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Bir Fonksiyon Şeması Oluşturun:**

    Sonra fonksiyon adı, fonksiyonun ne yaptığına dair açıklama ile fonksiyon parametrelerinin isimlerini ve açıklamalarını içeren bir JSON şeması tanımlayacağız. 
    Bu şemayı, kullanıcı isteği (San Francisco saatini bulmak gibi) ile birlikte daha önce oluşturulan istemciye göndeririz. Önemli olan, **araç çağrısının** döndürüldüğüdür, **sorunun nihai cevabı değil**. Daha önce belirtildiği gibi, LLM görevi için seçtiği fonksiyonun adını ve ona geçirilecek argümanları döner.

    ```python
    # Modelin okuyabilmesi için işlev açıklaması
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_time",
                "description": "Get the current time in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city name, e.g. San Francisco",
                        },
                    },
                    "required": ["location"],
                },
            }
        }
    ]
    ```
   
    ```python
  
    # İlk kullanıcı mesajı
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # İlk API çağrısı: Modelden fonksiyonu kullanmasını isteyin
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Modelin yanıtını işleyin
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Görevi gerçekleştirmek için gereken fonksiyon kodu:**

    Şimdi LLM'nin hangi fonksiyonun çalıştırılması gerektiğini seçtiğine göre, görevi gerçekleştiren kod uygulanmalı ve çalıştırılmalıdır.
    Mevcut saati almak için Python'da kodu yazabiliriz. Sonuçta, response_message'dan fonksiyon adı ve argümanları alacak kodu da yazmamız gerekir.

    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

     ```python
     # Fonksiyon çağrılarını işleyin
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # İkinci API çağrısı: Modelden nihai yanıtı alın
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

Fonksiyon Çağrısı, çoğu ya da tüm ajan araç kullanım tasarımının merkezindedir ancak sıfırdan uygulaması bazen zor olabilir.
[2. Ders](../../../02-explore-agentic-frameworks)’de öğrendiğimiz gibi, ajan çerçeveleri araç kullanımını uygulamak için önceden hazırlanmış yapı taşları sağlar.

## Ajan Çerçeveleri ile Araç Kullanım Örnekleri

Farklı ajan çerçevelerini kullanarak Araç Kullanım Tasarım Deseni'ni nasıl uygulayabileceğinize dair birkaç örnek:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a>, Büyük Dil Modelleri (LLM) ile çalışan .NET, Python ve Java geliştiricileri için açık kaynaklı bir AI çerçevesidir. Fonksiyon çağrısı kullanımını kolaylaştırır; fonksiyonlarınızı ve parametrelerini <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serileştirme</a> adlı bir işlemle modele otomatik olarak tanıtır. Ayrıca model ile kodunuz arasındaki karşılıklı iletişimi yönetir. Semantic Kernel gibi ajan çerçevelerinin bir diğer avantajı da <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">Dosya Arama</a> ve <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Kod Yorumlayıcı</a> gibi önceden hazırlanmış araçlara erişim sağlamasıdır.

Aşağıdaki diyagram Semantic Kernel ile fonksiyon çağrısı sürecini göstermektedir:

![function calling](../../../translated_images/tr/functioncalling-diagram.a84006fc287f6014.webp)

Semantic Kernel'de fonksiyonlar/araçlar <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Eklenti (Plugin)</a> olarak adlandırılır. Daha önce gördüğümüz `get_current_time` fonksiyonunu, fonksiyonu içeren bir sınıfa dönüştürerek bir eklenti haline getirebiliriz. Ayrıca fonksiyonun açıklamasını alan `kernel_function` dekoratörünü import edebiliriz. Ardından GetCurrentTimePlugin ile bir kernel oluşturdukça, kernel fonksiyonu ve parametrelerini otomatik olarak serileştirip modeli göndermek üzere şema oluşturur.

```python
from semantic_kernel.functions import kernel_function

class GetCurrentTimePlugin:
    async def __init__(self, location):
        self.location = location

    @kernel_function(
        description="Get the current time for a given location"
    )
    def get_current_time(location: str = ""):
        ...

```

```python 
from semantic_kernel import Kernel

# Çekirdeği oluştur
kernel = Kernel()

# Eklentiyi oluştur
get_current_time_plugin = GetCurrentTimePlugin(location)

# Eklentiyi çekirdeğe ekle
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Hizmeti

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Hizmeti</a>, geliştiricilerin temel hesaplama ve depolama kaynaklarını yönetmeye gerek kalmadan yüksek kaliteli ve genişletilebilir AI ajanları güvenli bir şekilde oluşturmasını, dağıtmasını ve ölçeklendirmesini sağlayan daha yeni bir ajan çerçevesidir. Bu hizmet, özellikle kurumsal uygulamalar için uygun olup, tam yönetilen ve kurumsal güvenlik seviyesine sahiptir.

LLM API doğrudan geliştirilmeye kıyasla, Azure AI Agent Hizmeti aşağıdaki avantajları sunar:

- Otomatik araç çağrısı – araç çağrısını çözümleme, aracı çalıştırma ve yanıtı yönetme gereksinimini ortadan kaldırır; tüm bunlar artık sunucu tarafında yapılır.
- Güvenli şekilde yönetilen veriler – sohbet durumu yönetmek yerine, ihtiyacınız olan tüm verileri depolamak için thread’lere güvenebilirsiniz.
- Kutudan çıkar çıkmaz hazır araçlar – Bing, Azure AI Arama ve Azure Fonksiyonları gibi veri kaynaklarınızla etkileşim kurabileceğiniz araçlar.

Azure AI Agent Hizmetinde mevcut araçlar iki kategoriye ayrılır:

1. Bilgi Araçları:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Arama ile Temellendirme</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Dosya Arama</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Arama</a>

2. Eylem Araçları:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Fonksiyon Çağrısı</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Kod Yorumlayıcı</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI ile tanımlı araçlar</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Fonksiyonları</a>

Agent Service, bu araçları bir `araç seti (toolset)` olarak birlikte kullanmamıza olanak tanır. Ayrıca belirli bir konuşmanın mesaj geçmişini takip eden `thread`leri kullanır.

Contoso adlı bir şirkette satış temsilcisi olduğunuzu hayal edin. Satış verilerinizle ilgili soruları yanıtlayabilen bir konuşma ajanı geliştirmek istiyorsunuz.

Aşağıdaki görsel, Azure AI Agent Hizmeti’ni kullanarak satış verilerinizi nasıl analiz edebileceğinizi göstermektedir:

![Agentic Service In Action](../../../translated_images/tr/agent-service-in-action.34fb465c9a84659e.webp)

Servisle bu araçlardan herhangi birini kullanmak için bir istemci yaratarak bir araç veya araç seti tanımlayabiliriz. Bunu pratikte uygulamak için aşağıdaki Python kodunu kullanabiliriz. LLM, araç setine bakarak kullanıcı tarafından oluşturulan `fetch_sales_data_using_sqlite_query` fonksiyonunu mu yoksa önceden oluşturulmuş Kod Yorumlayıcı’yı mı kullanacağına karar verecektir.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_functions.py dosyasında bulunan fetch_sales_data_using_sqlite_query fonksiyonu.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Araç setini başlat
toolset = ToolSet()

# fetch_sales_data_using_sqlite_query fonksiyonu ile işlev çağırma ajanını başlat ve araç setine ekle
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Kod Yorumlayıcı aracını başlat ve araç setine ekle.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Güvenilir AI ajanları oluşturmak için Araç Kullanım Tasarım Deseni’ni kullanırken özel olarak dikkat edilmesi gerekenler nelerdir?

LLM'ler tarafından dinamik oluşturulan SQL ile ilgili yaygın bir endişe güvenliktir; özellikle SQL enjeksiyonu riski veya veritabanını silme/tahrif etme gibi kötü niyetli eylemler söz konusudur. Bu endişeler geçerlidir ancak veritabanı erişim izinlerinin doğru yapılandırılmasıyla etkili şekilde azaltılabilir. Çoğu veritabanı için bu, veritabanının salt okunur (read-only) olarak yapılandırılması anlamına gelir. PostgreSQL veya Azure SQL gibi veritabanı hizmetlerinde, uygulamaya salt okunur (SELECT) rolü atanmalıdır.
Uygulamayı güvenli bir ortamda çalıştırmak korumayı daha da artırır. Kurumsal senaryolarda, veriler genellikle operasyonel sistemlerden çıkarılır ve kullanımı kolay bir şemaya sahip salt okunur bir veritabanı veya veri ambarına dönüştürülür. Bu yaklaşım, verilerin güvenli, performans ve erişilebilirlik için optimize edilmiş olmasını sağlar ve uygulamanın kısıtlı, salt okunur erişime sahip olmasını garanti eder.

## Örnek Kodlar

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Araç Kullanımı Tasarım Kalıpları Hakkında Daha Fazla Sorunuz mu Var?

Diğer öğrenenlerle tanışmak, çalışma saatlerine katılmak ve AI Agent sorularınızı cevaplamak için [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord)’a katılın.

## Ek Kaynaklar

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Function Calling Tutorial</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## Önceki Ders

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## Sonraki Ders

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek herhangi bir yanlış anlama veya yanlış yorumlamadan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->