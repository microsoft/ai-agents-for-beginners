[![Planlama Tasarım Deseni](../../../translated_images/tr/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Bu dersin videosunu izlemek için yukarıdaki resme tıklayın)_

# Planlama Tasarımı

## Giriş

Bu ders şunları kapsayacaktır

* Açık bir genel hedef tanımlamak ve karmaşık bir görevi yönetilebilir görevlere bölmek.
* Daha güvenilir ve makine tarafından okunabilir yanıtlar için yapılandırılmış çıktıyı kullanmak.
* Dinamik görevleri ve beklenmedik girdileri yönetmek için olay tabanlı bir yaklaşım uygulamak.

## Öğrenme Hedefleri

Bu dersi tamamladıktan sonra aşağıdakileri anlayacaksınız:

* Bir AI ajanı için genel bir hedef belirlemek ve ajanın neyi başarması gerektiğini açıkça bilmesini sağlamak.
* Karmaşık bir görevi yönetilebilir alt görevlere bölmek ve bunları mantıklı bir sıraya koymak.
* Ajanları doğru araçlarla donatmak (ör. arama araçları veya veri analitiği araçları), ne zaman ve nasıl kullanılacağını kararlaştırmak ve beklenmedik durumlarla başa çıkmak.
* Alt görev sonuçlarını değerlendirmek, performansı ölçmek ve nihai çıktıyı iyileştirmek için eylemleri tekrarlamak.

## Genel Hedefi Tanımlama ve Görevi Bölme

![Hedefleri ve Görevleri Tanımlama](../../../translated_images/tr/defining-goals-tasks.d70439e19e37c47a.webp)

Çoğu gerçek dünya görevi, tek adımda ele alınamayacak kadar karmaşıktır. Bir AI ajanının planlamasını ve eylemlerini yönlendirmek için özlü bir hedefi olmalıdır. Örneğin, aşağıdaki hedefi düşünün:

    "3 günlük seyahat programı oluştur."

Basitçe ifade edilse de yine de ayrıntılandırılması gerekir. Hedef ne kadar net olursa, ajan (ve varsa insan işbirlikçileri) doğru sonucu elde etmeye o kadar iyi odaklanabilir; örneğin kapsamlı bir program oluşturmak, uçuş seçenekleri, otel önerileri ve etkinlik tavsiyeleri içeren.

### Görev Parçalama

Büyük veya karmaşık görevler, daha küçük, hedef odaklı alt görevlere bölündüğünde daha yönetilebilir hale gelir.
Seyahat programı örneğinde, hedefi şu alt görevlere bölmek mümkündür:

* Uçuş Rezervasyonu
* Otel Rezervasyonu
* Araç Kiralama
* Kişiselleştirme

Her alt görev, özelleşmiş ajanlar veya süreçler tarafından ele alınabilir. Bir ajan en iyi uçuş fırsatlarını aramaya odaklanabilirken, diğeri otel rezervasyonlarına yoğunlaşabilir. Ardından bir koordinatör ya da “aşağı akış” ajan bu sonuçları birleştirerek kullanıcının kullanımına sunar.

Bu modüler yaklaşım, aşamalı geliştirmelere de olanak tanır. Örneğin, Yemek Önerileri veya Yerel Etkinlik Tavsiyeleri için özel ajanlar ekleyip zamanla programı iyileştirebilirsiniz.

### Yapılandırılmış Çıktı

Büyük Dil Modelleri (LLM'ler), aşağı akış ajanları veya servislerinin kolayca ayrıştırıp işleyebileceği yapılandırılmış çıktı (örneğin JSON) üretebilir. Bu, planlama çıktısı alındıktan sonra bu görevleri harekete geçirebildiğimiz çok ajanlı senaryolarda özellikle faydalıdır.

Aşağıdaki Python örneği, basit bir planlayıcı ajanın bir hedefi alt görevlere bölmesini ve yapılandırılmış bir plan oluşturmasını göstermektedir:

```python
from pydantic import BaseModel
from enum import Enum
from typing import List, Optional, Union
import json
import os
from typing import Optional
from pprint import pprint
from agent_framework.foundry import FoundryChatClient
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

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

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

### Çok Ajanlı Orkestrasyon ile Planlama Ajanı

Bu örnekte, Semantik Yönlendirici Ajan kullanıcı isteği alır (örneğin, "Seyahatim için otel planına ihtiyacım var.").

Planlayıcı şunları yapar:

* Otel Planını Almak: Planlayıcı, kullanıcı mesajını alır ve sistem istemine (mevcut ajan detayları dahil) dayanarak yapılandırılmış bir seyahat planı oluşturur.
* Ajanları ve Araçlarını Listelemek: Ajan dizini, ajanların (örneğin uçuş, otel, araç kiralama, etkinlikler için) ve sundukları fonksiyonların veya araçların listesini tutar.
* Planı İlgili Ajanlara Yönlendirmek: Alt görev sayısına bağlı olarak, planlayıcı mesajı doğrudan ilgili ajana (tek görev senaryoları için) ya da çok ajanlı işbirliği için grup sohbet yöneticisi aracılığıyla iletir.
* Sonucu Özetlemek: Son olarak planlayıcı, oluşturulan planı açıklık için özetler.
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

# Seyahat AltGörev Modeli

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # Görevi ajana atamak istiyoruz

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# İstemciyi oluştur

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

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

Aşağıda önceki kodun çıktısı vardır ve bu yapılandırılmış çıktıyı `assigned_agent` konusuna yönlendirmek ve seyahat planını kullanıcıya özetlemek için kullanabilirsiniz.

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

Önceki kod örneği içeren örnek bir not defteri [burada](./code_samples/07-python-agent-framework.ipynb) bulunmaktadır.

### Yinelemeli Planlama

Bazı görevler, bir alt görevin sonucu diğerini etkilediğinde ileri geri ya da yeniden planlama gerektirir. Örneğin, ajan uçuş rezervasyonu sırasında beklenmedik bir veri formatı keşfederse, otel rezervasyonuna geçmeden önce stratejisini uyarlaması gerekebilir.

Ayrıca, kullanıcı geri bildirimi (örneğin, bir insanın daha erken bir uçuş tercih etmesi) kısmi bir yeniden planlamayı tetikleyebilir. Bu dinamik, yinelemeli yaklaşım, nihai çözümün gerçek dünya kısıtlamalarına ve değişen kullanıcı tercihlerine uyum sağlamasını garanti eder.

örnek kod

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
#.. önceki kodla aynı ve kullanıcı geçmişini, mevcut planı ilet

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
# .. yeniden planla ve görevleri ilgili ajanlara gönder
```

Daha kapsamlı planlama için, karmaşık görevlerin çözümü için <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a> Blog yazısını inceleyebilirsiniz.

## Özet

Bu yazıda, tanımlı ajanlar arasından dinamik olarak seçim yapabilen bir planlayıcı nasıl oluşturulabileceğine dair bir örnek inceledik. Planlayıcının çıktısı görevleri parçalar ve bu görevlerin yerine getirilmesi için ajanları atar. Ajanların görevi yerine getirmek için gerekli fonksiyon/araçlara erişimi olduğu varsayılır. Ajanlara ek olarak, refleksiyon, özetleyici ve round robin sohbet gibi diğer desenler de dahil edilerek daha fazla kişiselleştirme yapılabilir.

## Ek Kaynaklar

Magentic One - Karmaşık görevleri çözmek için genel amaçlı çok ajanlı sistemdir ve birçok zorlayıcı ajanik kıyaslama testinde etkileyici sonuçlar elde etmiştir. Referans: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. Bu uygulamada orkestratör, göreve özel planlar yapar ve bu görevleri mevcut ajanlara devreder. Planlamanın yanı sıra orkestratör, görev ilerlemesini izlemek için bir takip mekanizması kullanır ve gerekirse yeniden planlama yapar.

### Planlama Tasarım Deseni hakkında daha fazla sorunuz mu var?

Diğer öğrenenlerle tanışmak, ofis saatlerine katılmak ve AI Ajanlarınızla ilgili sorularınızı yanıtlamak için [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)'a katılın.

## Önceki Ders

[Güvenilir AI Ajanları Oluşturmak](../06-building-trustworthy-agents/README.md)

## Sonraki Ders

[Çoklu Ajan Tasarım Deseni](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->