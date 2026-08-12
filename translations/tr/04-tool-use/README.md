[![İyi AI Ajanları Nasıl Tasarlanır](../../../translated_images/tr/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Dersi izlemek için yukarıdaki görsele tıklayın)_

# Araç Kullanımı Tasarım Deseni

Araçlar, AI ajanlarının daha geniş bir yetenek yelpazesine sahip olmasını sağladıkları için ilginçtir. Ajanın gerçekleştirebileceği sınırlı bir eylem seti yerine, bir araç ekleyerek ajan şimdi çok çeşitli eylemleri gerçekleştirebilir. Bu bölümde, AI ajanlarının hedeflerine ulaşmak için belirli araçları nasıl kullanabileceğini tanımlayan Araç Kullanımı Tasarım Deseni'ne bakacağız.

## Giriş

Bu derste şu soruları yanıtlamaya çalışıyoruz:

- Araç kullanımı tasarım deseni nedir?
- Hangi kullanım durumlarına uygulanabilir?
- Tasarım desenini uygulamak için gereken öğeler/yapı taşları nelerdir?
- Güvenilir AI ajanları oluşturmak için Araç Kullanımı Tasarım Deseni'ni kullanırken özel dikkat edilmesi gereken noktalar nelerdir?

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra şunları yapabileceksiniz:

- Araç Kullanımı Tasarım Deseni ve amacını tanımlamak.
- Araç Kullanımı Tasarım Deseni'nin uygulanabilir olduğu kullanım durumlarını belirlemek.
- Tasarım desenini uygulamak için gerekli temel öğeleri anlamak.
- Bu tasarım desenini kullanan AI ajanlarında güvenilirlik sağlamak için dikkate alınması gereken hususları tanımak.

## Araç Kullanımı Tasarım Deseni Nedir?

**Araç Kullanımı Tasarım Deseni**, LLM'lere belirli hedeflere ulaşmak için dış araçlarla etkileşim kurma yeteneği kazandırmaya odaklanır. Araçlar, bir ajan tarafından eylem gerçekleştirmek için çalıştırılabilen koddur. Bir araç, hesap makinesi gibi basit bir fonksiyon veya hisse senedi fiyatı sorgulama ya da hava durumu tahmini gibi üçüncü taraf bir hizmete API çağrısı olabilir. AI ajanları bağlamında, araçlar **model tarafından oluşturulan fonksiyon çağrılarına** yanıt olarak ajanlar tarafından çalıştırılacak şekilde tasarlanmıştır.

## Hangi kullanım durumlarına uygulanabilir?

AI Ajanları, karmaşık görevleri tamamlamak, bilgi almak veya karar vermek için araçlardan yararlanabilir. Araç kullanımı tasarım deseni, veritabanları, web servisleri veya kod yorumlayıcılar gibi dış sistemlerle dinamik etkileşim gerektiren senaryolarda sıklıkla kullanılır. Bu yetenek, çeşitli kullanım durumlarında faydalıdır, örneğin:

- **Dinamik Bilgi Alımı:** Ajanlar güncel verileri almak için dış API'lere veya veritabanlarına sorgu yapabilir (örneğin, veri analizi için SQLite veritabanı sorgulama, hisse senedi fiyatları veya hava durumu bilgisi çekme).
- **Kod Çalıştırma ve Yorumlama:** Ajanlar matematiksel problemleri çözmek, raporlar oluşturmak veya simülasyonlar yapmak için kod veya betik çalıştırabilir.
- **İş Akışı Otomasyonu:** Görev zamanlayıcılar, e-posta servisleri veya veri hatları gibi araçları entegre ederek tekrarlayan veya çok adımlı iş akışlarını otomatikleştirme.
- **Müşteri Desteği:** Ajanlar CRM sistemleri, biletleme platformları veya bilgi tabanları ile etkileşime girerek kullanıcı sorularını çözebilir.
- **İçerik Oluşturma ve Düzenleme:** Ajanlar dilbilgisi denetleyicileri, metin özetleyiciler veya içerik güvenliği değerlendirme araçları gibi araçlardan yararlanarak içerik oluşturma görevlerinde yardımcı olabilir.

## Araç kullanımı tasarım desenini uygulamak için gereken öğeler/yapı taşları nelerdir?

Bu yapı taşları, AI ajanının geniş bir görev yelpazesi gerçekleştirmesine olanak tanır. Araç Kullanımı Tasarım Deseni'ni uygulamak için gereken temel öğelere bakalım:

- **Fonksiyon/Araç Şemaları:** Mevcut araçların ayrıntılı tanımları; fonksiyon adı, amacı, gereken parametreler ve beklenen çıktılar dahil. Bu şemalar, LLM'nin hangi araçların mevcut olduğunu ve geçerli isteklerin nasıl oluşturulacağını anlamasını sağlar.

- **Fonksiyon Çalıştırma Mantığı:** Araçların kullanıcı niyeti ve konuşma bağlamına göre ne zaman ve nasıl çağrılacağını belirler. Bu, planlayıcı modüller, yönlendirme mekanizmaları veya araç kullanımını dinamik olarak belirleyen koşullu akışlar içerebilir.

- **Mesaj Yönetim Sistemi:** Kullanıcı girdileri, LLM yanıtları, araç çağrıları ve araç çıktıları arasındaki konuşma akışını yöneten bileşenler.

- **Araç Entegrasyon Çerçevesi:** Ajanı, basit fonksiyonlar veya karmaşık dış hizmetler olsun çeşitli araçlara bağlayan altyapı.

- **Hata Yönetimi ve Doğrulama:** Araç çalıştırma hatalarını yönetmek, parametreleri doğrulamak ve beklenmedik yanıtları ele almak için mekanizmalar.

- **Durum Yönetimi:** Çok turlu etkileşimlerde tutarlılığı sağlamak için konuşma bağlamını, önceki araç etkileşimlerini ve kalıcı verileri izler.

Şimdi, Fonksiyon/Araç Çağrısını daha ayrıntılı ele alalım.
 
### Fonksiyon/Araç Çağrısı

Fonksiyon çağrısı, Büyük Dil Modellerinin (LLM) araçlarla etkileşime girmesini sağlayan temel yoldur. Genellikle 'Fonksiyon' ve 'Araç' terimleri birbirinin yerine kullanılır çünkü ajanların görevleri yürütmek için kullandığı 'araçlar', yeniden kullanılabilir kod blokları olan 'fonksiyonlardır'. Bir fonksiyonun kodunun çağrılması için, LLM'nin kullanıcı talebini fonksiyon açıklamasıyla karşılaştırması gerekir. Bunun için tüm mevcut fonksiyonların açıklamalarını içeren bir şema LLM'ye gönderilir. LLM, görev için en uygun fonksiyonu seçer ve adını ve argümanlarını döndürür. Seçilen fonksiyon çağrılır; yanıtı LLM'ye geri gönderilir ve LLM bu bilgiyi kullanıcı talebine yanıt vermek için kullanır.

Geliştiricilerin ajanlar için fonksiyon çağrısını uygulamaları için gerekli olanlar:

1. Fonksiyon çağrısını destekleyen bir LLM modeli
2. Fonksiyon açıklamalarını içeren bir şema
3. Açıklanan her fonksiyonun kodu

Şimdi şehre ait güncel zamanı alma örneği ile açıklayalım:

1. **Fonksiyon çağrısını destekleyen bir LLM başlatın:**

    Her model fonksiyon çağrısını desteklemeyebilir, bu yüzden kullandığınız LLM'nin desteklediğini kontrol etmek önemlidir. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> fonksiyon çağrısını destekler. Azure OpenAI **Responses API**'ye karşı OpenAI istemcisini başlatarak başlayabiliriz (stabil `/openai/v1/` uç noktası — `api_version` gerekmez).

    ```python
    # Azure OpenAI (Yanıtlar API'si, v1 uç noktası) için OpenAI istemcisini başlatın
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Bir Fonksiyon Şeması Oluşturun**:

    Sonra, fonksiyonun adı, fonksiyonun ne yaptığına dair açıklama ve fonksiyon parametrelerinin isimleri ile açıklamalarını içeren bir JSON şeması tanımlayacağız.
    Bu şemayı, önceden oluşturduğumuz istemciye ve kullanıcının San Francisco'da zamanı bulma talebine ileteceğiz. Önemli olan nokta, bir **araç çağrısı**nın döndürülmesidir, **sorunun kesin cevabı değil**. Daha önce belirtildiği gibi, LLM göreve uygun fonksiyonun adını ve bu fonksiyona geçirilecek argümanları döndürür.

    ```python
    # Modelin okuması için fonksiyon açıklaması (Yanıtlar API düz araç formatı)
    tools = [
        {
            "type": "function",
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
    ]
    ```
   
    ```python
  
    # Başlangıç kullanıcı mesajı
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # İlk API çağrısı: Modelden fonksiyonu kullanmasını isteyin
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # Responses API, araç çağrılarını response.output içinde function_call öğeleri olarak döndürür.
    # Bunları sohbete ekleyin, böylece model bir sonraki turda tam bağlama sahip olur.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **Görevi yerine getirecek fonksiyon kodu:**

    LLM hangi fonksiyonun çalıştırılacağını seçtikten sonra görevi yerine getirecek kodun uygulanması ve çalıştırılması gerekir.
    Python ile mevcut zamanı alma kodunu uygulayabiliriz. Yanıttan fonksiyon adını ve argümanlarını çıkaracak kodu da yazmamız gerekiyor.

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
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # Araç sonucunu function_call_output öğesi olarak döndürün
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # İkinci API çağrısı: Modelden son yanıtı alın
    final_response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        store=False,
    )

    return final_response.output_text
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

Fonksiyon Çağrısı, çoğu araç kullanımı tasarımının temelidir; ancak sıfırdan uygulamak bazen zorlu olabilir.
[Ders 2](../../../02-explore-agentic-frameworks) 'de öğrendiğimiz gibi, ajan çerçeveleri bize araç kullanımını uygulamak için önceden hazırlanmış yapı taşları sağlar.
 
## Ajan Çerçeveleri ile Araç Kullanımı Örnekleri

Araç Kullanımı Tasarım Deseni'ni farklı ajan çerçeveleri kullanarak nasıl uygulayabileceğinize dair bazı örnekler:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a>, AI ajanları oluşturmak için açık kaynaklı bir AI çerçevesidir. `@tool` dekoratörü ile araçları Python fonksiyonları olarak tanımlamanıza izin vererek fonksiyon çağrısı kullanımını kolaylaştırır. Çerçeve, model ile kodunuz arasındaki iletişimi yönetir. Ayrıca File Search ve Code Interpreter gibi önceden oluşturulmuş araçlara `FoundryChatClient` üzerinden erişim sağlar.

Aşağıdaki diyagram Microsoft Agent Framework ile fonksiyon çağrısı sürecini göstermektedir:

![fonksiyon çağrısı](../../../translated_images/tr/functioncalling-diagram.a84006fc287f6014.webp)

Microsoft Agent Framework'te araçlar dekoratörlü fonksiyonlar olarak tanımlanır. Daha önce gördüğümüz `get_current_time` fonksiyonunu `@tool` dekoratörü kullanarak araca dönüştürebiliriz. Çerçeve otomatik olarak fonksiyonu ve parametrelerini serileştirerek LLM'ye gönderilecek şemayı oluşturur.

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# İstemciyi oluştur
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Bir ajan oluştur ve araç ile çalıştır
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>, geliştiricilerin temel bilişim ve depolama kaynaklarını yönetmeden yüksek kaliteli ve genişletilebilir AI ajanları güvenli bir şekilde oluşturup dağıtmasını ve ölçeklemesini sağlamak için tasarlanmış daha yeni bir ajan çerçevesidir. Özellikle kurumsal uygulamalar için kullanışlıdır çünkü tam yönetilen bir hizmettir ve kurumsal düzeyde güvenlik sağlar.

LLM API'yi doğrudan kullanmakla karşılaştırıldığında Microsoft Foundry Agent Service şu avantajları sunar:

- Otomatik araç çağırma – araç çağrısını ayrıştırmaya, aracı çalıştırmaya ve yanıtı yönetmeye gerek yok; tümü artık sunucu tarafında yapılır
- Güvenli yönetilen veriler – kendi konuşma durumunuzu yönetmek yerine, ihtiyacınız olan tüm bilgileri saklamak için thread'lere güvenebilirsiniz
- Kutudan çıktığı gibi araçlar – Bing, Azure AI Search ve Azure Functions gibi veri kaynaklarınızla etkileşim kurabileceğiniz araçlar

Microsoft Foundry Agent Service içinde mevcut araçlar iki kategoriye ayrılabilir:

1. Bilgi Araçları:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Araması ile Donatım</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Dosya Arama</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Araması</a>

2. Eylem Araçları:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Fonksiyon Çağrısı</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Kod Yorumlayıcı</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI tanımlı araçlar</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service, bu araçları birlikte bir `toolset` olarak kullanmamıza olanak sağlar. Ayrıca belirli bir konuşmadan gelen mesaj geçmişini izleyen `threads` mekanizmasını kullanır.

Contoso adlı bir şirkette satış temsilcisi olduğunuzu hayal edin. Satış verilerinizle ilgili soruları yanıtlayabilen bir sohbet ajanı geliştirmek istiyorsunuz.

Aşağıdaki görsel, Microsoft Foundry Agent Service kullanarak satış verilerinizi nasıl analiz edebileceğinizi göstermektedir:

![Agentic Service Uygulamada](../../../translated_images/tr/agent-service-in-action.34fb465c9a84659e.webp)

Bu araçlardan herhangi birini kullanmak için bir istemci oluşturabilir ve bir araç veya araç seti tanımlayabiliriz. Bunu pratikte uygulamak için aşağıdaki Python kodunu kullanabiliriz. LLM araç setine bakarak, kullanıcı talebine bağlı olarak kullanıcı tarafından oluşturulan `fetch_sales_data_using_sqlite_query` fonksiyonunu mu yoksa önceden oluşturulmuş Kod Yorumlayıcıyı mı kullanacağına karar verecektir.

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
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Güvenilir AI ajanları oluşturmak için Araç Kullanımı Tasarım Deseni'ni kullanırken özel dikkate alınması gerekenler nelerdir?

LLM'ler tarafından dinamik olarak oluşturulan SQL'de yaygın bir endişe güvenliktir; özellikle SQL enjeksiyonu riski veya veritabanını düşürmek ya da üzerinde değişiklik yapmak gibi kötü niyetli işlemler. Bu endişeler geçerli olmakla birlikte, veritabanı erişim izinlerini doğru yapılandırarak etkili bir şekilde önlenebilir. Çoğu veritabanında bunun için veritabanının salt okunur olarak yapılandırılması gerekir. PostgreSQL veya Azure SQL gibi veritabanı hizmetlerinde uygulamaya salt okunur (SELECT) rolü atanmalıdır.

Uygulamanın güvenli bir ortamda çalıştırılması da korumayı artırır. Kurumsal senaryolarda, veriler genellikle operasyonel sistemlerden çıkarılır ve kullanıcı dostu bir şema ile salt okunur bir veritabanı veya veri ambarına dönüştürülür. Bu yaklaşım, verilerin güvenli, performans ve erişilebilirlik açısından optimize edilmiş olmasını sağlar ve uygulamanın kısıtlı, salt okunur erişime sahip olmasını temin eder.

## Örnek Kodlar

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Araç Kullanımı Tasarım Desenleri hakkında daha fazla sorunuz mu var?

Sorularınızı sormak, diğer öğrenenlerle tanışmak ve ofis saatlerine katılmak için [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)'a katılın.

## Ek Kaynaklar

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Atölyesi</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Çok Ajanlı Atölyesi</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework Genel Bakış</a>


## Bu Ajanı Duman Testi Yapmak (Opsiyonel)

[Ders 16](../16-deploying-scalable-agents/README.md) içinde ajanların nasıl dağıtılacağını öğrendikten sonra, bu dersin `TravelToolAgent`'ını (hala araçlarını çağırıp cevap veriyor mu?) [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) ile duman testinden geçirebilirsiniz. Nasıl çalıştırılacağı için [`tests/README.md`](../tests/README.md) dosyasına bakın.

## Önceki Ders

[Ajan Tasarım Kalıplarını Anlamak](../03-agentic-design-patterns/README.md)

## Sonraki Ders

[Ajan RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->