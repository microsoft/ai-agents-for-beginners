[![Planning Design Pattern](../../../translated_images/tr/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Bu dersin videosunu izlemek için yukarıdaki resme tıklayın)_

# Planlama Tasarımı

## Giriş

Bu ders şunları kapsayacaktır

* Net bir genel hedef tanımlamak ve karmaşık bir görevi yönetilebilir görevlere bölmek.
* Daha güvenilir ve makine tarafından okunabilir yanıtlar için yapılandırılmış çıktıyı kullanmak.
* Dinamik görevleri ve beklenmeyen girdileri yönetmek için olay tabanlı bir yaklaşım uygulamak.

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra şunları anlayabileceksiniz:

* Bir AI ajanı için genel bir hedef belirlemek ve net bir şekilde neyin başarılması gerektiğini anlamasını sağlamak.
* Karmaşık bir görevi yönetilebilir alt görevlere ayırmak ve bunları mantıklı bir sıraya göre düzenlemek.
* Ajanları doğru araçlarla (örneğin, arama araçları veya veri analizi araçları) donatmak, ne zaman ve nasıl kullanılacağına karar vermek ve ortaya çıkan beklenmeyen durumları yönetmek.
* Alt görev sonuçlarını değerlendirmek, performansı ölçmek ve nihai çıktıyı iyileştirmek için eylemleri yinelemek.

## Genel Hedefin Tanımlanması ve Görevin Parçalanması

![Defining Goals and Tasks](../../../translated_images/tr/defining-goals-tasks.d70439e19e37c47a.webp)

Çoğu gerçek dünya görevi tek adımda ele alınamayacak kadar karmaşıktır. Bir AI ajanının planlamasını ve eylemlerini yönlendirmek için özlü bir hedefe ihtiyacı vardır. Örneğin, şu hedefi ele alalım:

    "3 günlük bir seyahat programı oluştur."

Basitçe ifade edilse de, hâlâ detaylandırılması gerekir. Hedef ne kadar net olursa, ajan (ve herhangi bir insan işbirlikçisi) doğru sonuca odaklanabilir, örneğin uçuş seçenekleri, otel önerileri ve etkinlik tavsiyeleri içeren kapsamlı bir program hazırlamak.

### Görev Parçalama

Büyük veya karmaşık görevler, daha küçük, hedefe yönelik alt görevlere bölündüğünde daha yönetilebilir hale gelir.
Seyahat programı örneğinde, hedefi şu alt görevlere ayırabilirsiniz:

* Uçak Rezervasyonu
* Otel Rezervasyonu
* Araç Kiralama
* Kişiselleştirme

Her alt görev sonrasında ilgili ajanlar veya süreçler tarafından ele alınabilir. Bir ajan en iyi uçuş fırsatlarını aramakta uzmanlaşırken, diğeri otel rezervasyonlarına odaklanabilir. Koordine eden veya “aşağı yönlü” bir ajan ise bu sonuçları kullanıcıya sunulacak tutarlı bir programa dönüştürebilir.

Bu modüler yaklaşım, kademeli iyileştirmelere de olanak sağlar. Örneğin, Yemek Önerileri veya Yerel Aktivite Tavsiyeleri gibi özel ajanlar ekleyebilir ve programı zamanla geliştirebilirsiniz.

### Yapılandırılmış Çıktı

Büyük Dil Modelleri (LLM'ler), aşağı akış ajanları veya servislerin daha kolay çözümleyip işleyebileceği yapılandırılmış çıktılar (ör. JSON) üretebilir. Bu, özellikle planlama çıktısı alındıktan sonra görevlerin eyleme dönüştürüldüğü çok ajanlı bağlamlarda faydalıdır.

Aşağıdaki Python örneği, basit bir planlama ajanının bir hedefi alt görevlere bölerek yapılandırılmış bir plan oluşturmasını göstermektedir:

```python
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Union
import json
import os
from typing import Optional
from pprint import pprint
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# Seyahat AltGörev Modeli
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # Görevi ajana atamak istiyoruz

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Kullanıcı mesajını tanımla
system_prompt = """You are a planner agent.
    Your job is to decide which agents to run based on the user's request.
    Provide your response in JSON format with the following structure:
{'main_task': 'Plan a family trip from Singapore to Melbourne.',
 'subtasks': [{'assigned_agent': 'flight_booking',
               'task_details': 'Book round-trip flights from Singapore to '
                               'Melbourne.'}
    Below are the available agents specialised in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(input=user_message, instructions=system_prompt)

response_content = response.output_text
pprint(json.loads(response_content))
```

### Çok Ajanlı Orkestrasyonlu Planlama Ajanı

Bu örnekte, bir Semantik Yönlendirici Ajan kullanıcıdan gelen isteği alır (örneğin, "Seyahatim için otel planına ihtiyacım var.").

Planlayıcı ise:

* Otel Planını Alır: Planlayıcı, kullanıcı mesajını alır ve (kullanılabilir ajan bilgileri içeren bir sistem istemine dayanarak) yapılandırılmış bir seyahat planı oluşturur.
* Ajanları ve Araçlarını Listeler: Ajan kaydı, uçuş, otel, araç kiralama ve etkinlikler için ajanlar ve sundukları fonksiyonlar/araçlar listesini tutar.
* Planı İlgili Ajanlara Yönlendirir: Alt görev sayısına bağlı olarak, planlayıcı mesajı doğrudan ilgili ajana (tek görev durumunda) ya da çok ajanlı işbirliği için bir grup sohbet yöneticisi aracılığıyla koordine eder.
* Sonucu Özetler: Son olarak, planlayıcı oluşturulan planı açıklık için özetler.
Aşağıdaki Python kod örneği bu adımları göstermektedir:

```python

from pydantic import BaseModel

from enum import Enum
from typing import List, Optional, Union

class AgentEnum(str, Enum):
    FlightBooking = "flight_booking"
    HotelBooking = "hotel_booking"
    CarRental = "car_rental"
    ActivitiesBooking = "activities_booking"
    DestinationInfo = "destination_info"
    DefaultAgent = "default_agent"
    GroupChatManager = "group_chat_manager"

# Seyahat Alt Görev Modeli

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # Görevi ajan'a atamak istiyoruz

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# İstemciyi oluştur

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

from pprint import pprint

# Kullanıcı mesajını tanımla

system_prompt = """You are a planner agent.
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(input=user_message, instructions=system_prompt)

response_content = response.output_text

# Yanıt içeriğini JSON olarak yükledikten sonra yazdır

pprint(json.loads(response_content))
```

Sonraki çıktı önceki koddan gelir ve bu yapılandırılmış çıktıyı `assigned_agent`'a yönlendirip seyahat planını son kullanıcıya özetlemek için kullanabilirsiniz.

```json
{
    "is_greeting": "False",
    "main_task": "Plan a family trip from Singapore to Melbourne.",
    "subtasks": [
        {
            "assigned_agent": "flight_booking",
            "task_details": "Book round-trip flights from Singapore to Melbourne."
        },
        {
            "assigned_agent": "hotel_booking",
            "task_details": "Find family-friendly hotels in Melbourne."
        },
        {
            "assigned_agent": "car_rental",
            "task_details": "Arrange a car rental suitable for a family of four in Melbourne."
        },
        {
            "assigned_agent": "activities_booking",
            "task_details": "List family-friendly activities in Melbourne."
        },
        {
            "assigned_agent": "destination_info",
            "task_details": "Provide information about Melbourne as a travel destination."
        }
    ]
}
```

Önceki kod örneğiyle ilgili örnek defter [burada](07-python-agent-framework.ipynb) mevcuttur.

### Yinelemeli Planlama

Bazı görevler, bir alt görevin sonucu diğerini etkilediğinde ileri geri veya yeniden planlama gerektirir. Örneğin, ajan uçuş rezervasyonu sırasında beklenmeyen bir veri formatı tespit ederse, otel rezervasyonuna geçmeden önce stratejisini uyarlaması gerekebilir.

Ek olarak, kullanıcı geri bildirimi (örneğin, bir insanın daha erken bir uçuş tercih etmesi) kısmi bir yeniden planlamayı tetikleyebilir. Bu dinamik ve yinelemeli yaklaşım, nihai çözümün gerçek dünya kısıtlamalarına ve gelişen kullanıcı tercihleriyle uyumlu olmasını sağlar.

örnek kod

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. önceki kodla aynı ve kullanıcı geçmişini, mevcut planı iletin

system_prompt = """You are a planner agent to optimize the
    Your job is to decide which agents to run based on the user's request.
    Below are the available agents specialized in different tasks:
    - FlightBooking: For booking flights and providing flight information
    - HotelBooking: For booking hotels and providing hotel information
    - CarRental: For booking cars and providing car rental information
    - ActivitiesBooking: For booking activities and providing activity information
    - DestinationInfo: For providing information about destinations
    - DefaultAgent: For handling general requests"""

user_message = "Create a travel plan for a family of 2 kids from Singapore to Melbourne"

response = client.create_response(
    input=user_message,
    instructions=system_prompt,
    context=f"Previous travel plan - {TravelPlan}",
)
# .. yeniden plan yap ve görevleri ilgili ajanlara gönder
```

Daha kapsamlı planlama için karmaşık görevleri çözmek üzere Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blog yazısını</a> inceleyebilirsiniz.

## Özet

Bu makalede, tanımlanan mevcut ajanları dinamik olarak seçebilen bir planlayıcı oluşturma örneğine baktık. Planlayıcının çıktısı görevleri parçalayarak ajanlara atar ve bunların yürütülmesini sağlar. Ajanların, görevi yerine getirmek için gereken fonksiyon/araçlara erişimi olduğu varsayılır. Ajanlara ek olarak, yansıma, özetleyici ve round robin sohbet gibi diğer desenler de özelleştirme için eklenebilir.

## Ek Kaynaklar

Magentic One - Karmaşık görevleri çözmek için genel amaçlı çok ajanlı sistemdir ve pek çok zorlu ajan benchmark'ında etkileyici sonuçlar elde etmiştir. Referans: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. Bu uygulamada orkestratör görev bazlı planlar oluşturur ve bu görevleri kullanılabilir ajanlara devreder. Planlamanın yanı sıra, orkestratör görev ilerlemesini izlemek ve gerektiğinde yeniden planlamak için bir takip mekanizması kullanır.

### Planlama Tasarım Deseni ile İlgili Daha Fazla Sorunuz mu Var?

Diğer öğrenenlerle tanışmak, ofis saatlerine katılmak ve AI Ajanları ile ilgili sorularınızı cevaplamak için [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) topluluğuna katılın.

## Önceki Ders

[Güvenilir AI Ajanları Oluşturmak](../06-building-trustworthy-agents/README.md)

## Sonraki Ders

[Çok Ajanlı Tasarım Deseni](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, ana dilindeki haliyle yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucunda ortaya çıkabilecek yanlış anlamalar veya yorumlar nedeniyle sorumluluk kabul edilmemektedir.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->