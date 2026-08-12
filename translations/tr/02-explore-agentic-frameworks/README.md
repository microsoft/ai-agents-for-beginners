[![Yapay Zeka Ajan Çerçevelerini Keşfetmek](../../../translated_images/tr/lesson-2-thumbnail.c65f44c93b8558df.webp)](https://youtu.be/ODwF-EZo_O8?si=1xoy_B9RNQfrYdF7)

> _(Dersi videoda izlemek için yukarıdaki resme tıklayın)_

# Yapay Zeka Ajan Çerçevelerini Keşfet

Yapay zeka ajan çerçeveleri, yapay zeka ajanlarının oluşturulmasını, dağıtılmasını ve yönetilmesini basitleştirmek için tasarlanmış yazılım platformlarıdır. Bu çerçeveler, geliştiricilere karmaşık yapay zeka sistemlerinin geliştirilmesini kolaylaştıran önceden oluşturulmuş bileşenler, soyutlamalar ve araçlar sağlar.

Bu çerçeveler, geliştiricilerin yapay zeka ajan geliştirmedeki yaygın zorluklara standartlaştırılmış yaklaşımlar sunarak, uygulamalarının benzersiz yönlerine odaklanmasına yardımcı olur. Yapay zeka sistemleri oluştururken ölçeklenebilirlik, erişilebilirlik ve verimliliği artırırlar.

## Giriş 

Bu ders şunları kapsayacaktır:

- Yapay Zeka Ajan Çerçeveleri nedir ve geliştiricilere ne kazandırır?
- Takımlar, ajanlarının yeteneklerini hızlıca prototip oluşturmak, yinelemek ve geliştirmek için bunları nasıl kullanabilir?
- Microsoft tarafından oluşturulan çerçeveler ve araçlar arasındaki farklar nelerdir? (<a href="https://aka.ms/ai-agents-beginners/ai-agent-service" target="_blank">Microsoft Foundry Agent Service</a> ve <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework</a>)
- Var olan Azure ekosistem araçlarımı doğrudan entegre edebilir miyim yoksa bağımsız çözümlere mi ihtiyacım var?
- Microsoft Foundry Agent Service nedir ve bana nasıl yardımcı olur?

## Öğrenme hedefleri

Bu dersin hedefleri şunlardır:

- Yapay Zeka Ajan Çerçevelerinin yapay zeka geliştirmedeki rolünü anlamak.
- Yapay zeka ajanları oluşturmak için Yapay Zeka Ajan Çerçevelerinden nasıl yararlanılacağını öğrenmek.
- Yapay Zeka Ajan Çerçevelerinin sağladığı temel yetenekleri keşfetmek.
- Microsoft Agent Framework ile Microsoft Foundry Agent Service arasındaki farkları anlamak.

## Yapay Zeka Ajan Çerçeveleri nedir ve geliştiricilere ne yapma imkanı verir?

Geleneksel Yapay Zeka Çerçeveleri, yapay zekayı uygulamalarınıza entegre etmeniize ve bu uygulamaları şu şekillerde geliştirmeye yardımcı olabilir:

- **Kişiselleştirme**: AI, kullanıcı davranışlarını ve tercihlerini analiz ederek kişiselleştirilmiş öneriler, içerikler ve deneyimler sunabilir.
Örnek: Netflix gibi yayın hizmetleri, izleme geçmişine göre film ve dizi önerileri yaparak kullanıcı etkileşimini ve memnuniyetini artırır.
- **Otomasyon ve Verimlilik**: AI, tekrarlayan işleri otomatikleştirir, iş akışlarını kolaylaştırır ve operasyonel verimliliği artırır.
Örnek: Müşteri hizmetleri uygulamaları, yaygın soruları yanıtlamak için yapay zeka destekli sohbet botları kullanarak yanıt sürelerini kısaltır ve insan temsilcilerini karmaşık sorunlara odaklanmaya yönlendirir.
- **Geliştirilmiş Kullanıcı Deneyimi**: AI, ses tanıma, doğal dil işleme ve tahmin metni gibi akıllı özellikler sunarak genel kullanıcı deneyimini iyileştirir.
Örnek: Siri ve Google Assistant gibi sanal asistanlar, sesli komutları anlayıp yanıtlayarak kullanıcıların cihazlarıyla daha kolay etkileşim kurmasını sağlar.

### Bunlar güzel ama neden Yapay Zeka Ajan Çerçevesine ihtiyacımız var?

Yapay Zeka Ajan çerçeveleri sadece AI çerçeveleri olmaktan daha fazlasıdır. Kullanıcılarla, diğer ajanlarla ve ortamla etkileşim kurabilen ve belirli hedeflere ulaşabilen akıllı ajanların oluşturulmasını sağlarlar. Bu ajanlar otonom davranabilir, karar verebilir ve değişen koşullara uyum sağlayabilir. İşte AI Ajan Çerçevelerinin sağladığı kilit yetenekler:

- **Ajan İşbirliği ve Koordinasyonu**: Birden fazla yapay zeka ajanının birlikte çalışmasını, iletişim kurmasını ve karmaşık görevleri koordine etmesini sağlar.
- **Görev Otomasyonu ve Yönetimi**: Çok adımlı iş akışlarının otomasyonu, görev devri ve ajanlar arası dinamik görev yönetimi için mekanizmalar sağlar.
- **Bağlamsal Anlama ve Uyarlama**: Ajanlara bağlamı anlama, değişen ortamlara uyum sağlama ve gerçek zamanlı bilgilere göre karar verme yeteneği kazandırır.

Özetle, ajanlar size daha fazlasını yapma, otomasyonu ileri seviyeye taşıma, çevrelerinden öğrenerek uyum sağlayabilen daha zeki sistemler oluşturma imkanı sunar.

## Ajanın yeteneklerini nasıl hızlıca prototip yapabilir, yineleyebilir ve geliştirebiliriz?

Bu alan hızla gelişiyor ancak çoğu Yapay Zeka Ajan Çerçevesinde modüler bileşenler, işbirliği araçları ve gerçek zamanlı öğrenme gibi yaygın özellikler bulunuyor. Bu konulara bakalım:

- **Modüler Bileşenler Kullanın**: AI SDK’ları, AI ve Bellek bağlayıcıları, doğal dil veya kod eklentileriyle fonksiyon çağırma, istem şablonları gibi önceden oluşturulmuş bileşenler sunar.
- **İşbirliği Araçlarından Yararlanın**: Belirli roller ve görevler ile ajan tasarlayarak işbirlikçi iş akışlarını test edin ve geliştirin.
- **Gerçek Zamanlı Öğrenin**: Ajanların etkileşimlerden öğrenip davranışlarını dinamik olarak ayarladığı geri bildirim döngüleri uygulayın.

### Modüler Bileşenler Kullanın

Microsoft Agent Framework gibi SDK’lar AI bağlayıcıları, araç tanımları ve ajan yönetimi gibi önceden oluşturulmuş bileşenler sunar.

**Takımlar nasıl kullanabilir**: Takımlar, bu bileşenleri sıfırdan başlamak zorunda kalmadan hızla bir fonksiyonel prototip oluşturmak için birleştirebilir ve deney yapıp yineleyebilir.

**Uygulamada çalışma şekli**: Kullanıcı girdisinden bilgi çıkarmak için önceden oluşturulmuş bir ayrıştırıcı kullanabilir, verileri depolayıp geri getirmeniz için bir bellek modülü ve kullanıcılarla etkileşim için bir istem üreteci kullanabilirsiniz, tüm bunları sıfırdan geliştirmeden.

**Örnek kod**. Microsoft Agent Framework'ü `FoundryChatClient` ile kullanarak modelin araç çağırarak kullanıcı girdisine yanıt vermesini gösteren örneğe bakalım:

``` python
# Microsoft Agent Framework Python Örneği

import asyncio
import os

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential


# Seyahat rezervasyonu yapmak için örnek bir araç fonksiyonu tanımlayın
@tool(approval_mode="never_require")
def book_flight(date: str, location: str) -> str:
    """Book travel given location and date."""
    return f"Travel was booked to {location} on {date}"


async def main():
    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="travel_agent",
        instructions="Help the user book travel. Use the book_flight tool when ready.",
        tools=[book_flight],
    )

    response = await agent.run("I'd like to go to New York on January 1, 2025")
    print(response)
    # Örnek çıktı: 1 Ocak 2025'te New York'a olan uçuşunuz başarıyla rezerve edildi. İyi yolculuklar! ✈️🗽


if __name__ == "__main__":
    asyncio.run(main())
```

Bu örnekten görebileceğiniz, kullanıcı girdisinden uçuş rezervasyon talebinin kalkış, varış ve tarih gibi anahtar bilgileri çıkarmak için önceden oluşturulmuş bir ayrıştırıcı nasıl kullanılabileceğidir. Bu modüler yaklaşım, üst düzey mantığa odaklanmanızı sağlar.

### İşbirliği Araçlarından Yararlanın

Microsoft Agent Framework gibi çerçeveler, birlikte çalışabilen birden fazla ajan oluşturmayı kolaylaştırır.

**Takımlar nasıl kullanabilir**: Takımlar, belirli roller ve görevler ile ajanlar tasarlayabilir; bu da işbirlikçi iş akışlarını test etmelerini, iyileştirmelerini ve sistem verimliliğini artırmalarını sağlar.

**Uygulamada çalışma şekli**: Veri alma, analiz veya karar verme gibi uzmanlıkları olan ajanlardan oluşan bir takım oluşturabilirsiniz. Bu ajanlar iletişim kurarak ve bilgileri paylaşarak ortak hedeflere, örneğin bir kullanıcı sorgusunu yanıtlamaya ya da bir görevi tamamlamaya çalışır.

**Örnek kod (Microsoft Agent Framework)**:

```python
# Microsoft Agent Framework kullanarak birlikte çalışan birden fazla ajan oluşturma

import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Veri Alma Ajanı
agent_retrieve = provider.as_agent(
    name="dataretrieval",
    instructions="Retrieve relevant data using available tools.",
    tools=[retrieve_tool],
)

# Veri Analizi Ajanı
agent_analyze = provider.as_agent(
    name="dataanalysis",
    instructions="Analyze the retrieved data and provide insights.",
    tools=[analyze_tool],
)

# Görev üzerinde ajanları sırayla çalıştırma
retrieval_result = await agent_retrieve.run("Retrieve sales data for Q4")
analysis_result = await agent_analyze.run(f"Analyze this data: {retrieval_result}")
print(analysis_result)
```

Önceki kodda gördüğünüz, birden fazla ajanın birlikte veri analizi yaptığı bir görevin nasıl oluşturulduğudur. Her ajan belirli bir işlevi yerine getirir ve istenen sonuca ulaşmak için koordineli olarak çalışırlar. Uzmanlaşmış rollerle özel ajanlar yaratarak görev verimliliğini ve performansını artırabilirsiniz.

### Gerçek Zamanlı Öğrenin

Gelişmiş çerçeveler gerçek zamanlı bağlam anlama ve uyarlama özellikleri sunar.

**Takımlar nasıl kullanabilir**: Takımlar, ajanların etkileşimden öğrenip davranışlarını dinamik olarak ayarladığı geri bildirim döngülerini uygulayabilir; böylece sürekli iyileştirme ve gelişim sağlanır.

**Uygulamada çalışma şekli**: Ajanlar, kullanıcı geri bildirimi, çevresel veriler ve görev sonuçlarını analiz edip bilgi tabanını güncelleyebilir, karar verme algoritmalarını ayarlayabilir ve performansı zamanla artırabilir. Bu yinelemeli öğrenme süreci ajanların değişen koşullara ve kullanıcı tercihlerine uyum sağlamasını ve böylece sistemin genel etkinliğini artırmasını sağlar.

## Microsoft Agent Framework ve Microsoft Foundry Agent Service arasındaki farklar nelerdir?

Bu yaklaşımları birçok açıdan karşılaştırabiliriz ama tasarım, yetenekler ve hedef kullanım alanları açısından bazı temel farklara bakalım:

## Microsoft Agent Framework (MAF)

Microsoft Agent Framework, `FoundryChatClient` kullanarak AI ajanları oluşturmak için sadeleştirilmiş bir SDK sunar. Geliştiricilerin Azure OpenAI modellerini, yerleşik araç çağrısını, sohbet yönetimini ve Azure kimlik doğrulamasıyla kurumsal düzey güvenliği kullanarak ajan oluşturmasını sağlar.

**Kullanım Alanları**: Araç kullanımı, çok adımlı iş akışları ve kurumsal entegrasyon senaryolarıyla üretime hazır AI ajanları oluşturmak.

İşte Microsoft Agent Framework'ün bazı önemli temel kavramları:

- **Ajanlar**. Bir ajan `FoundryChatClient` üzerinden ad, talimatlar ve araçlarla yapılandırılarak oluşturulur. Ajan şunları yapabilir:
  - **Kullanıcı mesajlarını işle** ve Azure OpenAI modellerini kullanarak yanıt oluştur.
  - **Konuşma bağlamına göre araçları otomatik çağır.**
  - **Birden fazla etkileşim boyunca sohbet durumunu koru.**

  İşte bir ajan oluşturmayı gösteren kod parçası:

    ```python
    import os
    from agent_framework.foundry import FoundryChatClient
    from azure.identity import AzureCliCredential

    provider = FoundryChatClient(
        project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
        model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
        credential=AzureCliCredential(),
    )
    agent = provider.as_agent(
        name="my_agent",
        instructions="You are a helpful assistant.",
    )

    response = await agent.run("Hello, World!")
    print(response)
    ```

- **Araçlar**. Çerçeve, ajanların otomatik çağırabileceği Python fonksiyonları olarak araç tanımlamanıza olanak verir. Araçlar ajan oluşturulurken kaydedilir:

    ```python
    def get_weather(location: str) -> str:
        """Get the current weather for a location."""
        return f"The weather in {location} is sunny, 72\u00b0F."

    agent = provider.as_agent(
        name="weather_agent",
        instructions="Help users check the weather.",
        tools=[get_weather],
    )
    ```

- **Çoklu Ajan Koordinasyonu**. Farklı uzmanlıklara sahip birden fazla ajan oluşturup çalışmalarını koordine edebilirsiniz:

    ```python
    planner = provider.as_agent(
        name="planner",
        instructions="Break down complex tasks into steps.",
    )

    executor = provider.as_agent(
        name="executor",
        instructions="Execute the planned steps using available tools.",
        tools=[execute_tool],
    )

    plan = await planner.run("Plan a trip to Paris")
    result = await executor.run(f"Execute this plan: {plan}")
    ```

- **Azure Kimlik Entegrasyonu**. Çerçeve, API anahtarlarını doğrudan yönetme gereksinimini ortadan kaldıran güvenli ve anahtarsız kimlik doğrulama için `AzureCliCredential` (veya `DefaultAzureCredential`) kullanır.

## Microsoft Foundry Agent Service

Microsoft Foundry Agent Service, Microsoft Ignite 2024’te tanıtılan daha yeni bir hizmettir. Llama 3, Mistral ve Cohere gibi açık kaynaklı büyük dil modellerini doğrudan çağırma gibi daha esnek modellerle yapay zeka ajanlarının geliştirilip dağıtılmasını sağlar.

Microsoft Foundry Agent Service, genellikle kurumsal uygulamalar için uygun olan daha güçlü kurumsal güvenlik mekanizmaları ve veri saklama yöntemleri sunar. 

Microsoft Agent Framework ile kutudan çıktığı gibi çalışıp, ajanların oluşturulması ve dağıtımı için birlikte kullanılabilir.

Bu hizmet şu anda Genel Önizlemede olup, ajan oluşturma için Python ve C# dillerini desteklemektedir.

Microsoft Foundry Agent Service Python SDK ile kullanıcı tanımlı araçlara sahip ajan oluşturabiliriz:

```python
import asyncio
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

# Araç fonksiyonlarını tanımlayın
def get_specials() -> str:
    """Provides a list of specials from the menu."""
    return """
    Special Soup: Clam Chowder
    Special Salad: Cobb Salad
    Special Drink: Chai Tea
    """

def get_item_price(menu_item: str) -> str:
    """Provides the price of the requested menu item."""
    return "$9.99"


async def main() -> None:
    credential = DefaultAzureCredential()
    project_client = AIProjectClient.from_connection_string(
        credential=credential,
        conn_str="your-connection-string",
    )

    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="Host",
        instructions="Answer questions about the menu.",
        tools=[get_specials, get_item_price],
    )

    thread = project_client.agents.create_thread()

    user_inputs = [
        "Hello",
        "What is the special soup?",
        "How much does that cost?",
        "Thank you",
    ]

    for user_input in user_inputs:
        print(f"# User: '{user_input}'")
        message = project_client.agents.create_message(
            thread_id=thread.id,
            role="user",
            content=user_input,
        )
        run = project_client.agents.create_and_process_run(
            thread_id=thread.id, agent_id=agent.id
        )
        messages = project_client.agents.list_messages(thread_id=thread.id)
        print(f"# Agent: {messages.data[0].content[0].text.value}")


if __name__ == "__main__":
    asyncio.run(main())
```

### Temel kavramlar

Microsoft Foundry Agent Service aşağıdaki temel kavramlara sahiptir:

- **Ajan**. Microsoft Foundry Agent Service Microsoft Foundry ile entegredir. Burada bir AI Ajan "akıllı" mikro hizmet olarak hareket eder; soruları yanıtlamak (RAG), işlem yapmak veya iş akışlarını tamamen otomatikleştirmek için kullanılabilir. Bu, üretken AI modellerinin gücünü gerçek dünya veri kaynaklarına erişim ve etkileşim sağlayan araçlarla birleştirerek başarılır. İşte bir ajan örneği:

    ```python
    agent = project_client.agents.create_agent(
        model="gpt-5-mini",
        name="my-agent",
        instructions="You are helpful agent",
        tools=code_interpreter.definitions,
        tool_resources=code_interpreter.resources,
    )
    ```

    Bu örnekte, `gpt-5-mini` modeli, `my-agent` adlı bir isim ve `You are helpful agent` talimatıyla bir ajan oluşturuluyor. Ajan, kod yorumlama görevlerini yerine getirmek için araçlar ve kaynaklarla donatılmıştır.

- **İleti dizisi (Thread) ve mesajlar**. İleti dizisi önemli bir kavramdır; bir ajan ile kullanıcı arasındaki konuşma veya etkileşimi temsil eder. İleti dizileri, konuşma ilerleyişini izlemek, bağlam bilgisini depolamak ve etkileşim durumunu yönetmek için kullanılır. İşte bir ileti dizisi örneği:

    ```python
    thread = project_client.agents.create_thread()
    message = project_client.agents.create_message(
        thread_id=thread.id,
        role="user",
        content="Could you please create a bar chart for the operating profit using the following data and provide the file to me? Company A: $1.2 million, Company B: $2.5 million, Company C: $3.0 million, Company D: $1.8 million",
    )
    
    # Ajanın iş parçacığı üzerinde çalışma yapmasını isteyin
    run = project_client.agents.create_and_process_run(thread_id=thread.id, agent_id=agent.id)
    
    # Ajanın yanıtını görmek için tüm mesajları alın ve kaydedin
    messages = project_client.agents.list_messages(thread_id=thread.id)
    print(f"Messages: {messages}")
    ```

    Önceki kodda bir ileti dizisi oluşturulur. Daha sonra bu diziye mesaj gönderilir. `create_and_process_run` çağrılarak ajan dizide işlem yapmaya yönlendirilir. Son olarak, mesajlar alınır ve ajanın yanıtı görmek için kaydedilir. Mesajlar, kullanıcı ile ajan arasındaki konuşmanın ilerleyişini gösterir. Ayrıca, mesaj türlerinin metin, resim veya dosya gibi farklı olabileceği anlaşılmalıdır; örneğin ajan çalışması sonucu resim veya metin yanıtı ortaya çıkabilir. Geliştirici olarak bu bilgiyi yanıtın işlenmesi veya kullanıcıya sunulması için kullanabilirsiniz.

- **Microsoft Agent Framework ile entegrasyon**. Microsoft Foundry Agent Service, Microsoft Agent Framework ile sorunsuz çalışır; yani `FoundryChatClient` kullanarak ajan oluşturabilir ve bunları üretim senaryoları için Agent Service üzerinden dağıtabilirsiniz.

**Kullanım Alanları**: Microsoft Foundry Agent Service, güvenli, ölçeklenebilir ve esnek AI ajan dağıtımı gerektiren kurumsal uygulamalar için tasarlanmıştır.

## Bu yaklaşımlar arasındaki fark nedir?
 
Bazı örtüşmeler olsa da, tasarım, yetenekler ve hedef kullanım alanları açısından bazı temel farklar vardır:
 
- **Microsoft Agent Framework (MAF)**: AI ajanları oluşturmak için üretime hazır bir SDK’dır. Ajan oluşturma, araç çağrısı, sohbet yönetimi ve Azure kimlik entegrasyonu için sade API sağlar.
- **Microsoft Foundry Agent Service**: Microsoft Foundry’daki bir platform ve dağıtım hizmetidir. Azure OpenAI, Azure AI Search, Bing Search ve kod yürütme gibi hizmetlere yerleşik bağlantı sunar.
 
Hangi seçeneği seçeceğinizden hala emin değilseniz?

### Kullanım durumları
 
Bazı yaygın kullanım durumlarını inceleyerek size yardımcı olalım:
 
> S: Üretime hazır AI ajan uygulamaları geliştiriyorum ve hızlıca başlamak istiyorum
>

> C: Microsoft Agent Framework harika bir seçimdir. `FoundryChatClient` ile birkaç satırda araçlar ve talimatlar içeren ajanları tanımlayabileceğiniz basit, Python tarzı bir API sunar.

> S: Arama ve kod yürütme gibi Azure entegrasyonları ile kurumsal düzeyde dağıtım gerekiyor
>
> C: Microsoft Foundry Agent Service en iyi uyum sağlar. Birden fazla model, Azure AI Search, Bing Search ve Azure Functions için yerleşik yetenekler sunan bir platform hizmetidir. Ajanlarınızı Foundry Portal’da kolayca oluşturup ölçekli olarak dağıtabilirsiniz.
 
> S: Hala kararsızım, sadece bir seçenek söyle
>
> C: Ajanlarınızı oluşturmak için Microsoft Agent Framework ile başlayın, ardından üretimde dağıtmak ve ölçeklendirmek gerektiğinde Microsoft Foundry Agent Service'i kullanın. Bu yaklaşım, ajan mantığınız üzerinde hızlı yinelemenize olanak sağlarken kurumsal dağıtıma giden net bir yol sunar.
 
Önemli farkları bir tabloda özetleyelim:

| Çerçeve | Odağı | Temel Kavramlar | Kullanım Alanları |
| --- | --- | --- | --- |
| Microsoft Agent Framework | Araç çağrılı sadeleştirilmiş ajan SDK’sı | Ajanlar, Araçlar, Azure Kimlik | Yapay zeka ajanları oluşturma, araç kullanımı, çok adımlı iş akışları |
| Microsoft Foundry Agent Service | Esnek modeller, kurumsal güvenlik, Kod üretimi, Araç çağrısı | Modülerlik, İşbirliği, Proses Orkestrasyonu | Güvenli, ölçeklenebilir ve esnek AI ajan dağıtımı |

## Var olan Azure ekosistem araçlarımı doğrudan entegre edebilir miyim, yoksa bağımsız çözümlere mi ihtiyacım var?


Cevap evet, mevcut Azure ekosistemi araçlarınızı özellikle Microsoft Foundry Agent Service ile doğrudan entegre edebilirsiniz, çünkü bu servis diğer Azure hizmetleri ile sorunsuz çalışacak şekilde tasarlanmıştır. Örneğin Bing, Azure AI Search ve Azure Functions'ı entegre edebilirsiniz. Ayrıca Microsoft Foundry ile derin bir entegrasyon vardır.

Microsoft Agent Framework ayrıca `FoundryChatClient` ve Azure kimliği üzerinden Azure hizmetleri ile entegre olarak, ajan araçlarınızdan doğrudan Azure hizmetlerini çağırmanızı sağlar.

## Örnek Kodlar

- Python: [Agent Framework (Microsoft Foundry)](./code_samples/02-python-agent-framework.ipynb)
- Python: [Agent Framework (Azure OpenAI Responses API)](./code_samples/02-python-agent-framework-azure-openai.ipynb)
- .NET: [Agent Framework](./code_samples/02-dotnet-agent-framework.md)

## AI Ajan Çerçeveleri hakkında Daha Fazla Sorunuz mu Var?

Diğer öğrenenlerle tanışmak, ofis saatlerine katılmak ve AI Ajanlarıyla ilgili sorularınızı sormak için [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) kanalına katılın.

## Referanslar

- <a href="https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357" target="_blank">Azure Agent Service</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/responses" target="_blank">Microsoft Agent Framework - Azure OpenAI Responses</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a>

## Önceki Ders

[AI Ajanlara ve Ajan Kullanım Senaryolarına Giriş](../01-intro-to-ai-agents/README.md)

## Sonraki Ders

[Ajansal Tasarım Desenlerini Anlama](../03-agentic-design-patterns/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->