[![İyi AI Ajanları Nasıl Tasarlanır](../../../translated_images/tr/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Dersi izlemek için yukarıdaki görsele tıklayın)_

# Araç Kullanım Tasarım Deseni

Araçlar ilginçtir çünkü AI ajanlarının çok daha geniş bir yetenek yelpazesine sahip olmasını sağlarlar. Ajanın gerçekleştirebileceği sınırlı bir eylem seti yerine, bir araç ekleyerek ajan artık çok çeşitli eylemler gerçekleştirebilir. Bu bölümde, AI ajanlarının belirli hedeflere ulaşmak için nasıl belirli araçları kullanabileceğini açıklayan Araç Kullanım Tasarım Deseni'ni inceleyeceğiz.

## Giriş

Bu derste aşağıdaki sorulara cevap arayacağız:

- Araç kullanım tasarım deseni nedir?
- Hangi kullanım durumlarına uygulanabilir?
- Tasarım desenini uygulamak için gereken öğeler/yapı taşları nelerdir?
- Güvenilir AI ajanları oluşturmak için Araç Kullanım Tasarım Deseni'ni kullanırken hangi özel hususlar dikkate alınmalıdır?

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra:

- Araç Kullanım Tasarım Deseni ve amacını tanımlayabileceksiniz.
- Araç Kullanım Tasarım Deseni'nin uygulanabilir olduğu kullanım durumlarını tanımlayabileceksiniz.
- Tasarım desenini uygulamak için gerekli temel öğeleri anlayabileceksiniz.
- Bu tasarım desenini kullanan AI ajanlarında güvenilirlik sağlamak için dikkat edilmesi gerekenleri fark edebileceksiniz.

## Araç Kullanım Tasarım Deseni Nedir?

**Araç Kullanım Tasarım Deseni**, LLM'lere belirli hedeflere ulaşmak için dış araçlarla etkileşim kurma yeteneği kazandırmaya odaklanır. Araçlar, bir ajan tarafından eylem gerçekleştirmek üzere çalıştırılabilen kodlardır. Bir araç, hesap makinesi gibi basit bir fonksiyon olabileceği gibi, hisse senedi fiyatı sorgulama veya hava durumu tahmini gibi üçüncü taraf bir hizmete API çağrısı da olabilir. AI ajanları bağlamında araçlar, **model tarafından oluşturulan fonksiyon çağrılarına** yanıt olarak ajanlar tarafından yürütülmek üzere tasarlanmıştır.

## Hangi kullanım durumlarına uygulanabilir?

AI Ajanları, karmaşık görevleri tamamlamak, bilgi almak veya karar vermek için araçlardan yararlanabilir. Araç kullanım tasarım deseni, veritabanları, web servisleri veya kod yorumlayıcıları gibi dış sistemlerle dinamik etkileşim gerektiren durumlarda sıklıkla kullanılır. Bu yetenek şu gibi farklı kullanım durumları için faydalıdır:

- **Dinamik Bilgi Edinme:** Ajanlar dış API'leri veya veritabanlarını sorgulayarak güncel verileri alabilir (örneğin, veri analizi için SQLite veritabanını sorgulamak, hisse senedi fiyatları veya hava durumu bilgisi almak).
- **Kod Yürütme ve Yorumlama:** Ajanlar matematiksel problemleri çözmek, raporlar oluşturmak veya simülasyonlar yapmak için kod veya betikler çalıştırabilir.
- **İş Akışı Otomasyonu:** Görev zamanlayıcılar, e-posta servisleri veya veri boru hatları gibi araçları entegre ederek tekrarlayan veya çok aşamalı iş akışlarını otomatikleştirmek.
- **Müşteri Desteği:** Ajanlar, kullanıcı sorgularını çözmek için CRM sistemleri, bilet platformları veya bilgi tabanlarıyla etkileşim kurabilir.
- **İçerik Üretimi ve Düzenleme:** Ajanlar dilbilgisi denetleyicileri, metin özetleyiciler veya içerik güvenliği değerlendiriciler gibi araçları kullanarak içerik oluşturma görevlerine yardımcı olabilir.

## Araç kullanım tasarım desenini uygulamak için gereken öğeler/yapı taşları nelerdir?

Bu yapı taşları, AI ajanının çok çeşitli görevleri gerçekleştirmesini sağlar. Araç Kullanım Tasarım Deseni'ni uygulamak için gereken temel öğelere bakalım:

- **Fonksiyon/Araç Şemaları**: Kullanılabilir araçların fonksiyon adı, amacı, gerekli parametreler ve beklenen çıktılarını içeren ayrıntılı tanımları. Bu şemalar, LLM'nin hangi araçların mevcut olduğunu ve geçerli isteklerin nasıl oluşturulacağını anlamasını sağlar.

- **Fonksiyon Çalıştırma Mantığı**: Kullanıcının niyeti ve konuşma bağlamına göre araçların ne zaman ve nasıl çağrılacağını belirler. Bu, planlayıcı modüller, yönlendirme mekanizmaları veya dinamik araç kullanımını belirleyen koşullu akışları içerebilir.

- **Mesaj İşleme Sistemi**: Kullanıcı girdileri, LLM yanıtları, araç çağrıları ve araç çıktıları arasındaki konuşma akışını yöneten bileşenler.

- **Araç Entegrasyon Çerçevesi**: Ajanı, basit fonksiyonlar veya karmaşık dış hizmetler olsun çeşitli araçlara bağlayan altyapı.

- **Hata Yönetimi & Doğrulama**: Araç yürütme hatalarını ele alan, parametreleri doğrulayan ve beklenmeyen yanıtları yöneten mekanizmalar.

- **Durum Yönetimi**: Çok turlu etkileşimlerde tutarlılığı sağlamak için konuşma bağlamını, önceki araç etkileşimlerini ve kalıcı verileri takip eder.

Şimdi Fonksiyon/Araç Çağrısını daha ayrıntılı inceleyelim.

### Fonksiyon/Araç Çağrısı

Fonksiyon çağrısı, Büyük Dil Modellerinin (LLM'lerin) araçlarla etkileşimini mümkün kılan temel yoldur. 'Fonksiyon' ve 'Araç' terimlerinin sıkça birbirinin yerine kullanıldığını göreceksiniz çünkü 'fonksiyonlar' (tekrar kullanılabilir kod blokları) ajanların görevleri yerine getirmek için kullandığı 'araçlardır'. Bir fonksiyonun kodunun çağrılabilmesi için LLM, kullanıcının isteğini fonksiyonun tanımıyla karşılaştırmalıdır. Bunu yapmak için, mevcut tüm fonksiyonların açıklamalarını içeren bir şema LLM'ye gönderilir. LLM, göreve en uygun fonksiyonu seçer ve fonksiyon adı ile argümanlarını döndürür. Seçilen fonksiyon çağrılır, yanıtı LLM'ye gönderilir ve LLM, bilgiyi kullanarak kullanıcının isteğine yanıt verir.

Geliştiricilerin ajanlar için fonksiyon çağrısını uygulayabilmesi için şunlar gerekir:

1. Fonksiyon çağrısını destekleyen bir LLM modeli
2. Fonksiyon açıklamalarını içeren bir şema
3. Tanımlanan her fonksiyon için kod

Şimdi bir şehre ait mevcut saatin alınması örneğiyle anlatalım:

1. **Fonksiyon çağrısını destekleyen bir LLM başlatın:**

    Tüm modeller fonksiyon çağrısını desteklemez, bu nedenle kullandığınız LLM'nin desteklediğinden emin olmak önemlidir.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> fonksiyon çağrısını destekler. Azure OpenAI istemcisini başlatarak başlayabiliriz.

    ```python
    # Azure OpenAI istemcisini başlatın
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Bir Fonksiyon Şeması Oluşturun**:

    Bir sonraki adım, fonksiyonun adını, fonksiyonun ne yaptığının açıklamasını ve fonksiyon parametrelerinin adlarını ve açıklamalarını içeren JSON şeması tanımlamaktır.
    Bu şemayı daha önce oluşturulan istemciye, San Francisco saatini bulmak için kullanıcının talebi ile birlikte göndereceğiz. Önemli olan, **geri dönenin bir araç çağrısı** olmasıdır, sorunun nihai cevabı **değil**. Daha önce belirtildiği gibi, LLM göreve seçtiği fonksiyonun adını ve ona iletilecek argümanları döndürür.

    ```python
    # Modelin okuyabilmesi için fonksiyon açıklaması
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
  
    # İlk API çağrısı: Modelden işlevi kullanmasını iste
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Modelin yanıtını işle
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

    Artık LLM hangi fonksiyonun çalıştırılması gerektiğini seçtiğine göre, görevi yerine getiren kod uygulanmalı ve çalıştırılmalıdır.
    Python'da mevcut saati almak için kodu yazabiliriz. Sonucu elde etmek için yanıttan fonksiyon adını ve argümanları çıkarmak için de kod yazmamız gerekecek.

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
  
      # İkinci API çağrısı: Modelden son yanıtı alın
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

Fonksiyon Çağrısı, neredeyse tüm ajan araç kullanım tasarımlarının merkezindedir, ancak sıfırdan uygulamak bazen zor olabilir.
[Lesson 2](../../../02-explore-agentic-frameworks) dersinde öğrendiğimiz gibi, ajan çerçeveleri araç kullanımını uygulamak için önceden inşa edilmiş yapı taşları sağlar.
 
## Ajanik Çerçevelerle Araç Kullanımına Örnekler

Farklı ajanik çerçevelerle Araç Kullanım Tasarım Deseni'ni nasıl uygulayabileceğinize dair bazı örnekler:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a>, AI ajanları oluşturmak için açık kaynaklı bir AI çerçevesidir. `@tool` dekoratörü ile araçları Python fonksiyonları olarak tanımlamanıza izin vererek fonksiyon çağrısını kolaylaştırır. Çerçeve, model ile kodunuz arasındaki karşılıklı iletişimi yönetir. Ayrıca AzureAIProjectAgentProvider aracılığıyla Dosya Arama ve Kod Yorumlayıcı gibi önceden oluşturulmuş araçlara erişim sağlar.

Aşağıdaki diyagram, Microsoft Agent Framework ile fonksiyon çağrısı sürecini gösterir:

![function calling](../../../translated_images/tr/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Framework'te araçlar dekoratörlü fonksiyonlar olarak tanımlanır. Daha önce gördüğümüz `get_current_time` fonksiyonunu, `@tool` dekoratörünü kullanarak bir araca dönüştürebiliriz. Çerçeve fonksiyon ve parametrelerini otomatik olarak serileştirerek LLM'ye gönderilecek şemayı oluşturur.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# İstemciyi oluştur
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Bir ajan oluştur ve araçla çalıştır
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a>, geliştiricilerin temel bilgi işlem ve depolama kaynaklarını yönetmeden yüksek kaliteli, genişletilebilir AI ajanları güvenli bir şekilde oluşturup dağıtmasını ve ölçeklendirmesini sağlamak için tasarlanmış daha yeni bir ajanik çerçevedir. Özellikle kurumsal uygulamalar için uygundur çünkü tam yönetilen ve kurumsal sınıf güvenlik sunan bir hizmettir.

Doğrudan LLM API ile geliştirmeye kıyasla Azure AI Agent Service bazı avantajlar sunar, örneğin:

- Otomatik araç çağrısı – araç çağrısını ayrıştırma, aracı çağırma ve yanıtı işleme ihtiyacı olmadan, tümü sunucu tarafında gerçekleştirilir
- Güvenli veri yönetimi – kendi konuşma durumunuzu yönetmek yerine, tüm ihtiyaç duyduğunuz bilgileri depolamak için `threads` kullanılabilir
- Hazır araçlar – Bing, Azure AI Search ve Azure Functions gibi veri kaynaklarınızla etkileşimde bulunmanıza olanak tanıyan araçlar.

Azure AI Agent Service'deki araçlar iki kategoriye ayrılır:

1. Bilgi Araçları:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Arama ile Dayandırma</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Dosya Arama</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Arama</a>

2. Eylem Araçları:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Fonksiyon Çağrısı</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Kod Yorumlayıcı</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI tanımlı araçlar</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service, bu araçları birlikte bir `toolset` olarak kullanmamıza olanak tanır. Ayrıca belirli bir konuşmanın mesaj geçmişini takip eden `threads` yapısını kullanır.

Contoso adlı bir şirkette satış temsilcisi olduğunuzu hayal edin. Satış verilerinizle ilgili soruları yanıtlayabilen bir konuşma ajanı geliştirmek istiyorsunuz.

Aşağıdaki resim, Azure AI Agent Service kullanarak satış verilerinizi nasıl analiz edebileceğinizi gösterir:

![Agentic Service In Action](../../../translated_images/tr/agent-service-in-action.34fb465c9a84659e.webp)

Hizmetle herhangi bir aracı kullanmak için bir istemci oluşturup bir araç veya araç seti tanımlayabiliriz. Bunu pratik olarak uygulamak için aşağıdaki Python kodunu kullanabiliriz. LLM, araç setine bakarak kullanıcının isteğine göre kullanıcı tarafından oluşturulan `fetch_sales_data_using_sqlite_query` fonksiyonunu veya önceden oluşturulmuş Kod Yorumlayıcıyı kullanmaya karar verebilir.

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

# fetch_sales_data_using_sqlite_query fonksiyonu ile fonksiyon çağrı ajanını başlat ve araç setine ekle
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Kod Yorumlayıcı aracını başlat ve araç setine ekle.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Güvenilir AI ajanları oluşturmak için Araç Kullanım Tasarım Deseni’ni kullanırken özel olarak nelere dikkat edilmeli?

LLM'ler tarafından dinamik olarak oluşturulan SQL ile ilgili yaygın bir endişe, özellikle SQL enjeksiyonu veya veritabanına zarar verme gibi kötü niyetli eylemler riskidir. Bu endişeler geçerli olmakla birlikte, veritabanı erişim izinlerinin doğru yapılandırılmasıyla etkili biçimde azaltılabilir. Çoğu veritabanı için bu, veritabanının salt okunur olarak yapılandırılması anlamına gelir. PostgreSQL veya Azure SQL gibi veritabanı servislerinde uygulamaya salt okunur (SELECT) rolü atanmalıdır.

Uygulamanın güvenli bir ortamda çalıştırılması korumayı daha da artırır. Kurumsal senaryolarda, veriler genellikle operasyonel sistemlerden kullanıcı dostu bir şemaya sahip salt okunur bir veritabanına veya veri ambarına çıkarılır ve dönüştürülür. Bu yaklaşım verilerin güvenli, performans ve erişilebilirlik açısından optimize edilmiş olmasını sağlar ve uygulamanın sınırlı, salt okunur erişime sahip olmasını garanti eder.

## Örnek Kodlar

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Araç Kullanım Tasarım Deseni hakkında Daha Fazla Sorunuz mu Var?

Diğer öğrenenlerle tanışmak, ofis saatlerine katılmak ve AI Ajanları sorularınızı yanıtlamak için [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)’a katılın.

## Ek Kaynaklar

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Atölyesi</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Çok Ajanlı Atölye</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework Genel Bakış</a>

## Önceki Ders

[Agentik Tasarım Desenlerini Anlamak](../03-agentic-design-patterns/README.md)

## Sonraki Ders
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->