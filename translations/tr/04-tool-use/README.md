[![İyi AI Ajanları Nasıl Tasarlanır](../../../translated_images/tr/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Bu dersin videosunu izlemek için yukarıdaki görsele tıklayın)_

# Araç Kullanımı Tasarım Deseni

Araçlar ilginçtir çünkü AI ajanlarının daha geniş bir yetenek yelpazesine sahip olmasını sağlar. Ajanın gerçekleştirebileceği sınırlı bir eylem seti yerine, bir araç ekleyerek ajan şimdi çok çeşitli eylemleri gerçekleştirebilir. Bu bölümde AI ajanlarının belirli araçları nasıl kullanarak hedeflerine ulaşabileceğini açıklayan Araç Kullanımı Tasarım Deseni'ne bakacağız.

## Giriş

Bu derste aşağıdaki sorulara yanıt arıyoruz:

- Araç kullanımı tasarım deseni nedir?
- Hangi kullanım senaryolarına uygulanabilir?
- Tasarım desenini uygulamak için gereken öğeler/yapı taşları nelerdir?
- Güvenilir AI ajanları oluşturmak için Araç Kullanımı Tasarım Deseni kullanılırken nelere dikkat edilmelidir?

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra:

- Araç Kullanımı Tasarım Deseni'ni ve amacını tanımlayabileceksiniz.
- Araç Kullanımı Tasarım Deseni'nin uygulanabilir olduğu kullanım senaryolarını belirleyebileceksiniz.
- Tasarım desenini uygulamak için gerekli temel öğeleri anlayabileceksiniz.
- Bu tasarım desenini kullanan AI ajanlarında güvenilirliği sağlamak için dikkate alınması gerekenleri tanıyabileceksiniz.

## Araç Kullanımı Tasarım Deseni Nedir?

**Araç Kullanımı Tasarım Deseni**, LLM'lere belirli hedeflere ulaşmak için harici araçlarla etkileşim kurma yeteneği vermeye odaklanır. Araçlar, bir ajan tarafından eylem gerçekleştirmek üzere çalıştırılabilen koddur. Bir araç, basit bir hesap makinesi fonksiyonu veya hisse senedi fiyatı sorgulama ya da hava durumu tahmini gibi üçüncü taraf bir hizmete API çağrısı olabilir. AI ajanları bağlamında araçlar, **model tarafından üretilen fonksiyon çağrılarına** yanıt olarak ajanlar tarafından çalıştırılmak üzere tasarlanmıştır.

## Hangi kullanım senaryolarına uygulanabilir?

AI Ajanları, karmaşık görevleri tamamlamak, bilgi almak veya karar vermek için araçları kullanabilir. Araç kullanımı tasarım deseni, veri tabanları, web servisleri veya kod yorumlayıcılar gibi harici sistemlerle dinamik etkileşim gerektiren senaryolarda sıklıkla kullanılır. Bu yetenek aşağıdaki farklı kullanım senaryolarında faydalıdır:

- **Dinamik Bilgi Alma:** Ajanlar harici API'leri veya veri tabanlarını sorgulayarak güncel verileri çekebilir (örneğin, veri analizi için SQLite veri tabanını sorgulama, hisse senedi fiyatları ya da hava durumu bilgisi alma).
- **Kod Çalıştırma ve Yorumlama:** Ajanlar matematik problemlerini çözmek, rapor oluşturmak veya simülasyonlar yapmak için kod veya komut dosyaları çalıştırabilir.
- **İş Akışı Otomasyonu:** Görev zamanlayıcılar, e-posta servisleri veya veri boru hatları gibi araçları entegre ederek tekrarlayan veya çok adımlı iş akışlarını otomatikleştirme.
- **Müşteri Desteği:** Ajanlar CRM sistemleri, bilet platformları veya bilgi tabanları ile etkileşime girerek kullanıcı sorgularını çözebilir.
- **İçerik Oluşturma ve Düzenleme:** Ajanlar yazım denetleyiciler, metin özetleyiciler veya içerik güvenliği değerlendirme araçları gibi araçlardan yararlanarak içerik oluşturma görevlerinde yardımcı olabilir.

## Araç kullanımı tasarım desenini uygulamak için gereken öğeler/yapı taşları nelerdir?

Bu yapı taşları, AI ajanının çok çeşitli görevleri yerine getirmesini sağlar. Araç Kullanımı Tasarım Deseni'ni uygulamak için gereken ana öğelere bakalım:

- **Fonksiyon/Araç Şemaları**: Mevcut araçların detaylı tanımları; fonksiyon adı, amacı, gerekli parametreler ve beklenen çıktılar dahil. Bu şemalar, LLM'nin hangi araçların kullanılabilir olduğunu ve geçerli isteklerin nasıl oluşturulacağını anlamasını sağlar.

- **Fonksiyon Çalıştırma Mantığı**: Araçların kullanıcı niyeti ve konuşma bağlamına göre nasıl ve ne zaman çağrılacağını yönetir. Bu, planlayıcı modüller, yönlendirme mekanizmaları veya araç kullanımını dinamik olarak belirleyen koşullu akışları içerebilir.

- **Mesaj Yönetim Sistemi**: Kullanıcı girdileri, LLM yanıtları, araç çağrıları ve araç çıktıları arasındaki konuşma akışını yöneten bileşenler.

- **Araç Entegrasyon Çerçevesi**: Ajanı basit fonksiyonlar ya da karmaşık harici servislerle bağlayan altyapı.

- **Hata Yönetimi ve Doğrulama**: Araç çalıştırma hatalarını ele alma, parametreleri doğrulama ve beklenmedik yanıtları yönetme mekanizmaları.

- **Durum Yönetimi**: Konuşma bağlamını, önceki araç etkileşimlerini ve kalıcı verileri takip ederek çok adımlı etkileşimlerde tutarlılığı sağlar.

Şimdi, Fonksiyon/Araç Çağrısına daha ayrıntılı bakalım.

### Fonksiyon/Araç Çağrısı

Fonksiyon çağrısı, Büyük Dil Modellerinin (LLM'ler) araçlarla etkileşime geçmesini sağlamak için birincil yöntemdir. 'Fonksiyon' ve 'Araç' terimleri bazen birbirinin yerine kullanılır çünkü 'fonksiyonlar' (yeniden kullanılabilir kod blokları) ajanların görevleri gerçekleştirmek için kullandığı 'araçlardır'. Bir fonksiyonun kodunun çalıştırılabilmesi için, LLM'nin kullanıcının talebini fonksiyon açıklamasıyla karşılaştırması gerekir. Bunun için, tüm mevcut fonksiyonların açıklamalarını içeren bir şema LLM'ye gönderilir. LLM, görev için en uygun fonksiyonu seçer ve adını ve argümanlarını döner. Seçilen fonksiyon çalıştırılır, yanıtı LLM'ye gönderilir ve LLM bu bilgiyle kullanıcının isteğine yanıt verir.

Geliştiricilerin ajanlar için fonksiyon çağrısını uygulayabilmesi için şunlara ihtiyaç vardır:

1. Fonksiyon çağrısını destekleyen bir LLM modeli
2. Fonksiyon açıklamalarını içeren bir şema
3. Tanımlanan her fonksiyon için kod

Şimdi bir şehirdeki mevcut zamanı almayı örnek olarak kullanalım:

1. **Fonksiyon çağrısını destekleyen bir LLM başlatın:**

    Tüm modeller fonksiyon çağrısını desteklemez, bu yüzden kullandığınız LLM'nin desteklediğinden emin olun. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> fonksiyon çağrısını destekler. Azure OpenAI istemcisini başlatarak başlayabiliriz.

    ```python
    # Azure OpenAI istemcisini başlatın
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

2. **Bir Fonksiyon Şeması Oluşturun:**

    Sonra fonksiyon adını, fonksiyonun ne yaptığını açıklayan açıklamayı ve fonksiyon parametre isimleri ile açıklamalarını içeren JSON şeması tanımlayacağız.
    Bu şemayı, az önce oluşturulan istemciye ve kullanıcı isteği olan San Francisco'daki zamanı bulmaya ileteceğiz. Önemli olan nokta şudur ki, bir **araç çağrısı** döndürülür, sorunun nihai cevabı değil. Daha önce belirtildiği gibi, LLM görevi için seçtiği fonksiyonun adını ve ona iletilecek argümanları döner.

    ```python
    # Modelin okunması için fonksiyon açıklaması
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
  
    # İlk API çağrısı: Modelden fonksiyonu kullanmasını iste
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
  
3. **Görevi gerçekleştirmek için gereken fonksiyon kodu:**

    LLM hangi fonksiyonun çalıştırılması gerektiğini seçtiği için görevi yerine getiren kod uygulanıp çalıştırılmalıdır.
    Python'da mevcut zamanı almak için kodu uygulayabiliriz. Ayrıca, sonucu almak için response_message'dan fonksiyon adı ve argümanları çıkarmak için kod yazmamız gerekir.

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

Fonksiyon Çağrısı, eğer tüm değilse çoğu ajan araç kullanım tasarımının merkezindedir; ancak sıfırdan uygulaması bazen zor olabilir.
2. Derste öğrendiğimiz gibi, [Agentik Çerçeveler](../../../02-explore-agentic-frameworks) araç kullanımını gerçekleştirmek için önceden oluşturulmuş yapı taşları sağlar.

## Agentik Çerçevelerle Araç Kullanımı Örnekleri

Aşağıda farklı agentik çerçeveler kullanarak Araç Kullanımı Tasarım Deseni'nin nasıl uygulanabileceğine dair örnekler yer almaktadır:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a>, AI ajanları oluşturmak için açık kaynaklı bir AI çerçevesidir. Fonksiyon çağrısını, araçları `@tool` dekoratörü ile Python fonksiyonları olarak tanımlamanıza olanak vererek kolaylaştırır. Çerçeve, model ile kodunuz arasındaki karşılıklı iletişimi otomatik olarak yönetir. Ayrıca, `AzureAIProjectAgentProvider` aracılığıyla Dosya Arama ve Kod Yorumlayıcı gibi önceden oluşturulmuş araçlara erişim sağlar.

Aşağıdaki şema Microsoft Agent Framework ile fonksiyon çağrısı sürecini gösterir:

![function calling](../../../translated_images/tr/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Framework'te araçlar dekoratörlü fonksiyonlar olarak tanımlanır. Daha önce gördüğümüz `get_current_time` fonksiyonunu `@tool` dekoratörünü kullanarak bir araca dönüştürebiliriz. Çerçeve fonksiyon ve parametrelerini otomatik olarak serileştirip şemayı oluşturarak LLM'ye gönderir.

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

# Bir ajan oluştur ve aracı ile çalıştır
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> geliştiricilerin yüksek kaliteli ve genişletilebilir AI ajanları güvenli şekilde oluşturup dağıtmasını ve ölçeklendirmesini sağlayan, altyapı yönetimi gerektirmeyen daha yeni bir agentik çerçevedir. Kurumsal uygulamalar için özellikle uygundur çünkü tam yönetilen ve kurumsal düzeyde güvenlik sağlar.

LLM API'yi doğrudan kullanmaya kıyasla, Azure AI Agent Service bazı avantajlar sunar:

- Otomatik araç çağrısı – bir araç çağrısını ayrıştırma, aracı çağırma ve yanıtı işlemenin sunucu tarafında otomatik yapılması
- Güvenli yönetilen veri – kendi konuşma durumunuzu yönetmek yerine, ihtiyacınız olan tüm bilgileri saklayan thread’lere güvenebilirsiniz
- Kutudan çıkar kullanıma hazır araçlar – Bing, Azure AI Search ve Azure Functions gibi veri kaynaklarınızla etkileşim için araçlar.

Azure AI Agent Service'deki araçlar iki kategoriye ayrılır:

1. Bilgi Araçları:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Arama ile Temellendirme</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Dosya Arama</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Arama</a>

2. Eylem Araçları:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Fonksiyon Çağrısı</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Kod Yorumlayıcı</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI tanımlı araçlar</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service, bu araçları `toolset` olarak birlikte kullanmamıza izin verir. Ayrıca belirli bir konuşmanın mesaj geçmişini izleyen `thread`leri kullanır.

Örneğin, Contoso adlı bir şirkette satış temsilcisi olduğunuzu hayal edin. Satış verilerinizle ilgili soruları yanıtlayabilecek bir sohbet ajanı geliştirmek istiyorsunuz.

Aşağıdaki görsel, Azure AI Agent Service kullanarak satış verilerinizi nasıl analiz edebileceğinizi gösterir:

![Agentic Service In Action](../../../translated_images/tr/agent-service-in-action.34fb465c9a84659e.webp)

Servisle herhangi bir aracı kullanmak için bir istemci oluşturup bir araç veya araç seti tanımlayabiliriz. Pratikte bunu şu Python koduyla yapabiliriz. LLM, toolset'e bakarak kullanıcı tarafından oluşturulan `fetch_sales_data_using_sqlite_query` fonksiyonunu mu yoksa önceden oluşturulmuş Kod Yorumlayıcıyı mı kullanacağına karar verebilecektir.

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

# fetch_sales_data_using_sqlite_query fonksiyonu ile fonksiyon çağırma aracını başlat ve araç setine ekle
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

## Güvenilir AI ajanları oluşturmak için Araç Kullanımı Tasarım Deseni kullanırken nelere dikkat edilmelidir?

LLM’ler tarafından dinamik olarak oluşturulan SQL sorgularında en sık karşılaşılan endişe güvenliktir; özellikle SQL enjeksiyonu veya veritabanını silme, değiştirme gibi kötü niyetli işlemler riski. Bu endişeler geçerli olsa da, veritabanı erişim izinleri uygun şekilde yapılandırılırsa etkili bir şekilde azaltılabilir. Çoğu veritabanında bunun yolu, veritabanının salt okunur olarak yapılandırılmasıdır. PostgreSQL veya Azure SQL gibi hizmetlerde uygulamaya okuma (SELECT) rolü atanmalıdır.

Uygulamayı güvenli bir ortamda çalıştırmak korumayı daha da artırır. Kurumsal senaryolarda, veriler genellikle operasyonel sistemlerden çıkartılıp okunabilir veri tabanı veya veri ambarına kullanıcı dostu şema ile dönüştürülür. Bu yöntem verilerin güvenli, performans ve erişilebilirlik açısından optimize edilmesini sağlar ve uygulamanın sınırlı, salt okunur erişimine izin verir.

## Örnek Kodlar

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Araç Kullanımı Tasarım Desenleri Hakkında Daha Fazla Sorunuz mu Var?

Diğer öğrenenlerle tanışmak, ofis saatlerine katılmak ve AI Ajanları ile ilgili sorularınızı yanıtlamak için [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) sunucusuna katılın.

## Ek Kaynaklar

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Atölyesi</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Çoklu Ajan Atölyesi</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework Genel Bakış</a>

## Önceki Ders

[Agentik Tasarım Desenlerini Anlamak](../03-agentic-design-patterns/README.md)

## Sonraki Ders
[Agentik RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, Yapay Zeka çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluğu sağlamaya çalışsak da, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal, ana dildeki belge yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum farklılıklarından sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->