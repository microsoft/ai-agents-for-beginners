<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d7c3b7bd1b3528074d8b6a7c5ad33b6f",
  "translation_date": "2025-11-18T17:27:36+00:00",
  "source_file": "04-tool-use/README.md",
  "language_code": "tr"
}
-->
[![İyi AI Ajanları Nasıl Tasarlanır](../../../translated_images/lesson-4-thumbnail.546162853cb3daffd64edd92014f274103f76360dfb39fc6e6ee399494da38fd.tr.png)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Bu dersin videosunu izlemek için yukarıdaki görsele tıklayın)_

# Araç Kullanımı Tasarım Deseni

Araçlar ilginçtir çünkü AI ajanlarının daha geniş bir yetenek yelpazesine sahip olmasını sağlar. Ajanın gerçekleştirebileceği sınırlı bir eylem seti yerine, bir araç ekleyerek ajan artık çok çeşitli eylemler gerçekleştirebilir. Bu bölümde, AI ajanlarının belirli araçları kullanarak hedeflerine nasıl ulaşabileceğini açıklayan Araç Kullanımı Tasarım Deseni'ni inceleyeceğiz.

## Giriş

Bu derste şu soruları yanıtlamayı hedefliyoruz:

- Araç kullanımı tasarım deseni nedir?
- Hangi kullanım durumlarına uygulanabilir?
- Tasarım desenini uygulamak için gereken unsurlar/yapı taşları nelerdir?
- Güvenilir AI ajanları oluşturmak için Araç Kullanımı Tasarım Deseni'ni kullanırken özel hususlar nelerdir?

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra:

- Araç Kullanımı Tasarım Deseni'ni ve amacını tanımlayabileceksiniz.
- Araç Kullanımı Tasarım Deseni'nin uygulanabilir olduğu kullanım durumlarını belirleyebileceksiniz.
- Tasarım desenini uygulamak için gereken temel unsurları anlayabileceksiniz.
- Bu tasarım desenini kullanan AI ajanlarında güvenilirliği sağlama hususlarını tanıyabileceksiniz.

## Araç Kullanımı Tasarım Deseni Nedir?

**Araç Kullanımı Tasarım Deseni**, LLM'lere belirli hedeflere ulaşmak için harici araçlarla etkileşim kurma yeteneği kazandırmaya odaklanır. Araçlar, bir ajanın eylemleri gerçekleştirmek için çalıştırabileceği kodlardır. Bir araç, bir hesap makinesi gibi basit bir fonksiyon veya bir üçüncü taraf hizmetine yapılan bir API çağrısı (örneğin, hisse senedi fiyatı sorgulama veya hava durumu tahmini) olabilir. AI ajanları bağlamında, araçlar **model tarafından oluşturulan fonksiyon çağrılarına** yanıt olarak ajanlar tarafından çalıştırılmak üzere tasarlanmıştır.

## Hangi kullanım durumlarına uygulanabilir?

AI ajanları, karmaşık görevleri tamamlamak, bilgi almak veya kararlar vermek için araçlardan yararlanabilir. Araç kullanımı tasarım deseni, genellikle veritabanları, web hizmetleri veya kod yorumlayıcılar gibi harici sistemlerle dinamik etkileşim gerektiren senaryolarda kullanılır. Bu yetenek, aşağıdaki gibi çeşitli kullanım durumları için faydalıdır:

- **Dinamik Bilgi Alma:** Ajanlar, güncel verileri almak için harici API'leri veya veritabanlarını sorgulayabilir (örneğin, SQLite veritabanını veri analizi için sorgulama, hisse senedi fiyatlarını veya hava durumu bilgilerini alma).
- **Kod Çalıştırma ve Yorumlama:** Ajanlar, matematiksel problemleri çözmek, raporlar oluşturmak veya simülasyonlar yapmak için kod veya betikleri çalıştırabilir.
- **İş Akışı Otomasyonu:** Görev zamanlayıcılar, e-posta hizmetleri veya veri hatları gibi araçları entegre ederek tekrarlayan veya çok adımlı iş akışlarını otomatikleştirme.
- **Müşteri Desteği:** Ajanlar, CRM sistemleri, biletleme platformları veya bilgi tabanları ile etkileşim kurarak kullanıcı sorularını çözebilir.
- **İçerik Üretimi ve Düzenleme:** Ajanlar, dilbilgisi denetleyicileri, metin özetleyiciler veya içerik güvenliği değerlendiriciler gibi araçlardan yararlanarak içerik oluşturma görevlerine yardımcı olabilir.

## Araç kullanımı tasarım desenini uygulamak için gereken unsurlar/yapı taşları nelerdir?

Bu yapı taşları, AI ajanının çok çeşitli görevleri gerçekleştirmesini sağlar. Araç Kullanımı Tasarım Deseni'ni uygulamak için gereken temel unsurlara bakalım:

- **Fonksiyon/Arac Şemaları**: Kullanılabilir araçların ayrıntılı tanımları, fonksiyon adı, amacı, gerekli parametreler ve beklenen çıktılar dahil. Bu şemalar, LLM'nin hangi araçların mevcut olduğunu ve geçerli istekleri nasıl oluşturacağını anlamasını sağlar.

- **Fonksiyon Çalıştırma Mantığı**: Kullanıcının niyetine ve konuşma bağlamına göre araçların nasıl ve ne zaman çağrılacağını yönetir. Bu, planlayıcı modüller, yönlendirme mekanizmaları veya araç kullanımını dinamik olarak belirleyen koşullu akışları içerebilir.

- **Mesaj İşleme Sistemi**: Kullanıcı girdileri, LLM yanıtları, araç çağrıları ve araç çıktıları arasındaki konuşma akışını yöneten bileşenler.

- **Araç Entegrasyon Çerçevesi**: Ajanı basit fonksiyonlardan karmaşık harici hizmetlere kadar çeşitli araçlara bağlayan altyapı.

- **Hata Yönetimi ve Doğrulama**: Araç çalıştırma hatalarını yönetmek, parametreleri doğrulamak ve beklenmeyen yanıtları ele almak için mekanizmalar.

- **Durum Yönetimi**: Konuşma bağlamını, önceki araç etkileşimlerini ve çoklu dönüşlü etkileşimlerde tutarlılığı sağlamak için kalıcı verileri izler.

Şimdi Fonksiyon/Arac Çağrısını daha ayrıntılı inceleyelim.

### Fonksiyon/Arac Çağrısı

Fonksiyon çağrısı, Büyük Dil Modelleri'nin (LLM'ler) araçlarla etkileşim kurmasını sağlamanın birincil yoludur. 'Fonksiyon' ve 'Araç' terimlerini genellikle birbirinin yerine kullanıldığını göreceksiniz çünkü 'fonksiyonlar' (yeniden kullanılabilir kod blokları), ajanların görevleri yerine getirmek için kullandığı 'araçlardır'. Bir fonksiyonun kodunun çalıştırılabilmesi için, LLM'nin kullanıcı isteğini fonksiyon açıklamasına karşı karşılaştırması gerekir. Bunun için, mevcut tüm fonksiyonların açıklamalarını içeren bir şema LLM'ye gönderilir. LLM, görev için en uygun fonksiyonu seçer ve adını ve argümanlarını döndürür. Seçilen fonksiyon çalıştırılır, yanıtı LLM'ye geri gönderilir ve LLM bu bilgiyi kullanıcının isteğine yanıt vermek için kullanır.

Ajanlar için fonksiyon çağrısını uygulamak isteyen geliştiriciler şunlara ihtiyaç duyar:

1. Fonksiyon çağrısını destekleyen bir LLM modeli
2. Fonksiyon açıklamalarını içeren bir şema
3. Açıklanan her fonksiyonun kodu

San Francisco'daki mevcut zamanı almak örneğini kullanarak açıklayalım:

1. **Fonksiyon çağrısını destekleyen bir LLM başlatın:**

    Tüm modeller fonksiyon çağrısını desteklemez, bu yüzden kullandığınız LLM'nin bunu desteklediğinden emin olmak önemlidir. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> fonksiyon çağrısını destekler. Azure OpenAI istemcisini başlatarak başlayabiliriz.

    ```python
    # Initialize the Azure OpenAI client
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Bir Fonksiyon Şeması Oluşturun:**

    Ardından, fonksiyon adı, fonksiyonun ne yaptığına dair açıklama ve fonksiyon parametrelerinin adları ve açıklamalarını içeren bir JSON şeması tanımlayacağız. Bu şemayı, San Francisco'daki zamanı bulmak için kullanıcının isteğiyle birlikte daha önce oluşturulan istemciye ileteceğiz. Önemli olan, dönen şeyin **araç çağrısı** olduğu, sorunun nihai cevabı **olmadığıdır**. Daha önce belirtildiği gibi, LLM görev için seçtiği fonksiyonun adını ve ona iletilecek argümanları döndürür.

    ```python
    # Function description for the model to read
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
  
    # Initial user message
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # First API call: Ask the model to use the function
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Process the model's response
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Görevi yerine getirmek için gereken fonksiyon kodu:**

    Artık LLM hangi fonksiyonun çalıştırılması gerektiğini seçtiğine göre, görevi yerine getirecek kodun uygulanması ve çalıştırılması gerekiyor. 
    Python'da mevcut zamanı almak için kodu uygulayabiliriz. Ayrıca, nihai sonucu almak için response_message'dan ad ve argümanları çıkarmak için kod yazmamız gerekecek.

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
     # Handle function calls
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
  
      # Second API call: Get the final response from the model
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

Fonksiyon Çağrısı, ajan araç kullanımı tasarımının çoğunun, hatta tamamının merkezindedir, ancak sıfırdan uygulamak bazen zor olabilir. 
[2. Derste](../../../02-explore-agentic-frameworks) öğrendiğimiz gibi, ajan çerçeveleri bize araç kullanımını uygulamak için önceden oluşturulmuş yapı taşları sağlar.

## Ajan Çerçeveleri ile Araç Kullanımı Örnekleri

Farklı ajan çerçevelerini kullanarak Araç Kullanımı Tasarım Deseni'ni nasıl uygulayabileceğinize dair bazı örnekler:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a>, Büyük Dil Modelleri (LLM'ler) ile çalışan .NET, Python ve Java geliştiricileri için açık kaynaklı bir AI çerçevesidir. Fonksiyon çağrısını kullanma sürecini, fonksiyonlarınızı ve parametrelerini modele otomatik olarak açıklayan bir süreç olan <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serileştirme</a> yoluyla basitleştirir. Ayrıca model ile kodunuz arasındaki iletişimi yönetir. Semantic Kernel gibi bir ajan çerçevesi kullanmanın bir diğer avantajı, <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">Dosya Arama</a> ve <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Kod Yorumlayıcı</a> gibi önceden oluşturulmuş araçlara erişim sağlamasıdır.

Aşağıdaki diyagram, Semantic Kernel ile fonksiyon çağrısı sürecini göstermektedir:

![fonksiyon çağrısı](../../../translated_images/functioncalling-diagram.a84006fc287f60140cc0a484ff399acd25f69553ea05186981ac4d5155f9c2f6.tr.png)

Semantic Kernel'de fonksiyonlar/araçlar <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">Eklentiler</a> olarak adlandırılır. Daha önce gördüğümüz `get_current_time` fonksiyonunu bir sınıfa dönüştürerek bir eklentiye dönüştürebiliriz. Ayrıca, fonksiyonun açıklamasını alan `kernel_function` dekoratörünü içe aktarabiliriz. GetCurrentTimePlugin ile bir çekirdek oluşturduğunuzda, çekirdek fonksiyonu ve parametrelerini otomatik olarak serileştirir ve sürecin bir parçası olarak LLM'ye gönderilecek şemayı oluşturur.

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

# Create the kernel
kernel = Kernel()

# Create the plugin
get_current_time_plugin = GetCurrentTimePlugin(location)

# Add the plugin to the kernel
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a>, geliştiricilerin yüksek kaliteli ve genişletilebilir AI ajanlarını güvenli bir şekilde oluşturmasını, dağıtmasını ve ölçeklendirmesini sağlayan, temel hesaplama ve depolama kaynaklarını yönetme gereksinimi olmadan tasarlanmış daha yeni bir ajan çerçevesidir. Özellikle kurumsal uygulamalar için kullanışlıdır çünkü tamamen yönetilen bir hizmettir ve kurumsal düzeyde güvenlik sunar.

LLM API ile doğrudan geliştirmeye kıyasla, Azure AI Agent Service bazı avantajlar sağlar, bunlar arasında:

- Otomatik araç çağrısı – bir araç çağrısını ayrıştırma, aracı çağırma ve yanıtı işleme gereksinimi yoktur; tüm bunlar artık sunucu tarafında yapılır.
- Güvenli bir şekilde yönetilen veri – kendi konuşma durumunuzu yönetmek yerine, ihtiyacınız olan tüm bilgileri saklamak için diyalogları kullanabilirsiniz.
- Hazır araçlar – Bing, Azure AI Search ve Azure Functions gibi veri kaynaklarınızla etkileşim kurmak için kullanabileceğiniz araçlar.

Azure AI Agent Service'deki araçlar iki kategoriye ayrılabilir:

1. Bilgi Araçları:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Bing Arama ile Temellendirme</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Dosya Arama</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Eylem Araçları:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Fonksiyon Çağrısı</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Kod Yorumlayıcı</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">OpenAPI tanımlı araçlar</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service, bu araçları bir `araç seti` olarak birlikte kullanmamıza olanak tanır. Ayrıca, belirli bir konuşmadan gelen mesajların geçmişini takip eden `diyalogları` kullanır.

Contoso adlı bir şirkette satış temsilcisi olduğunuzu hayal edin. Satış verilerinizle ilgili soruları yanıtlayabilecek bir konuşma ajanı geliştirmek istiyorsunuz.

Aşağıdaki görsel, Azure AI Agent Service'i kullanarak satış verilerinizi nasıl analiz edebileceğinizi göstermektedir:

![Agentic Service In Action](../../../translated_images/agent-service-in-action.34fb465c9a84659edd3003f8cb62d6b366b310a09b37c44e32535021fbb5c93f.tr.jpg)

Bu hizmetle herhangi bir aracı kullanmak için bir istemci oluşturabilir ve bir araç veya araç seti tanımlayabilirsiniz. Bunu pratikte uygulamak için aşağıdaki Python kodunu kullanabiliriz. LLM, araç setine bakarak kullanıcı tarafından oluşturulan `fetch_sales_data_using_sqlite_query` fonksiyonunu veya önceden oluşturulmuş Kod Yorumlayıcıyı kullanıcı isteğine bağlı olarak kullanıp kullanmayacağına karar verebilir.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # fetch_sales_data_using_sqlite_query function which can be found in a fetch_sales_data_functions.py file.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Initialize function calling agent with the fetch_sales_data_using_sqlite_query function and adding it to the toolset
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset = ToolSet()
toolset.add(fetch_data_function)

# Initialize Code Interpreter tool and adding it to the toolset. 
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset = ToolSet()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Güvenilir AI ajanları oluşturmak için Araç Kullanımı Tasarım Deseni'ni kullanırken özel hususlar nelerdir?

LLM'ler tarafından dinamik olarak oluşturulan SQL ile ilgili yaygın bir endişe, özellikle SQL enjeksiyonu veya veritabanını silme veya değiştirme gibi kötü niyetli eylemler riskidir. Bu endişeler geçerli olsa da, veritabanı erişim izinlerini doğru bir şekilde yapılandırarak etkili bir şekilde azaltılabilir. Çoğu veritabanı için bu, veritabanını salt okunur olarak yapılandırmayı içerir. PostgreSQL veya Azure SQL gibi veritabanı hizmetleri için uygulamaya salt okunur (SELECT) rol atanmalıdır.
Uygulamayı güvenli bir ortamda çalıştırmak, korumayı daha da artırır. Kurumsal senaryolarda, veriler genellikle operasyonel sistemlerden alınır ve kullanıcı dostu bir şema ile salt okunur bir veritabanına veya veri ambarına dönüştürülür. Bu yaklaşım, verilerin güvenli, performans ve erişilebilirlik açısından optimize edilmiş olmasını ve uygulamanın sınırlı, salt okunur erişime sahip olmasını sağlar.

## Örnek Kodlar

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Araç Kullanım Tasarım Kalıpları Hakkında Daha Fazla Sorunuz mu Var?

Diğer öğrenicilerle tanışmak, ofis saatlerine katılmak ve AI Agents ile ilgili sorularınızı yanıtlamak için [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) topluluğuna katılın.

## Ek Kaynaklar

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Azure AI Agents Service Workshop</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Semantic Kernel Function Calling Tutorial</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Semantic Kernel Code Interpreter</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Autogen Tools</a>

## Önceki Ders

[Agentic Tasarım Kalıplarını Anlamak](../03-agentic-design-patterns/README.md)

## Sonraki Ders

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal dilindeki hali yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlama veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->