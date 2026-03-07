[![Corak Reka Bentuk Perancangan](../../../translated_images/ms/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Klik gambar di atas untuk menonton video pelajaran ini)_

# Reka Bentuk Perancangan

## Pengenalan

Pelajaran ini akan merangkumi

* Menentukan matlamat keseluruhan yang jelas dan memecahkan tugas kompleks kepada tugas yang boleh diurus.
* Memanfaatkan output berstruktur untuk respons yang lebih boleh dipercayai dan boleh dibaca mesin.
* Menerapkan pendekatan berorientasikan peristiwa untuk mengendalikan tugas dinamik dan input yang tidak dijangka.

## Matlamat Pembelajaran

Selepas menyelesaikan pelajaran ini, anda akan memahami tentang:

* Mengenal pasti dan menetapkan matlamat keseluruhan untuk ejen AI, memastikan ia jelas mengetahui apa yang perlu dicapai.
* Memecahkan tugas kompleks kepada subtugas yang boleh diurus dan menyusunnya ke dalam urutan logik.
* Membekalkan ejen dengan alat yang betul (contohnya, alat carian atau alat analitik data), memutuskan bila dan bagaimana ia digunakan, dan menangani situasi tidak dijangka yang timbul.
* Menilai hasil subtugas, mengukur prestasi, dan mengulang tindakan untuk meningkatkan output akhir.

## Menetapkan Matlamat Keseluruhan dan Memecah Tugas

![Menetapkan Matlamat dan Tugas](../../../translated_images/ms/defining-goals-tasks.d70439e19e37c47a.webp)

Kebanyakan tugas dunia sebenar terlalu kompleks untuk ditangani dalam satu langkah. Ejen AI memerlukan objektif ringkas untuk membimbing perancangan dan tindakannya. Sebagai contoh, pertimbangkan matlamat:

    "Hasilkan jadual perjalanan 3 hari."

Walaupun mudah dinyatakan, ia masih memerlukan penambahbaikan. Semakin jelas matlamat, semakin baik ejen (dan mana-mana rakan manusia) dapat menumpukan perhatian untuk mencapai hasil yang betul, seperti membuat itinerari yang komprehensif dengan pilihan penerbangan, cadangan hotel, dan saranan aktiviti.

### Pemecahan Tugas

Tugas besar atau rumit menjadi lebih mudah diurus apabila dibahagikan kepada subtugas yang lebih kecil dan berorientasikan matlamat.
Untuk contoh jadual perjalanan, anda boleh memecahkan matlamat kepada:

* Tempahan Penerbangan
* Tempahan Hotel
* Sewa Kereta
* Personalisasi

Setiap subtugas kemudian boleh ditangani oleh ejen atau proses khusus. Satu ejen mungkin mengkhusus dalam mencari tawaran penerbangan terbaik, satu lagi menumpukan pada tempahan hotel, dan sebagainya. Ejen penyelarasan atau "hiliran" kemudian boleh menyusun hasil ini menjadi satu itinerari yang padu untuk pengguna akhir.

Pendekatan modular ini juga membolehkan penambahbaikan berperingkat. Sebagai contoh, anda boleh menambah ejen khusus untuk Cadangan Makanan atau Saranan Aktiviti Tempatan dan memperhalusi itinerari dari semasa ke semasa.

### Output Berstruktur

Model Bahasa Besar (LLM) boleh menjana output berstruktur (contohnya JSON) yang lebih mudah untuk diurai dan diproses oleh ejen atau perkhidmatan hiliran. Ini amat berguna dalam konteks multi-ejen, di mana kita boleh melaksanakan tugas-tugas ini selepas output perancangan diterima.

Petikan Python berikut menunjukkan ejen perancangan mudah yang memecahkan matlamat kepada subtugas dan menjana pelan berstruktur:

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

# Model Subtugas Perjalanan
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # Kami ingin menetapkan tugasan kepada ejen

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Tentukan mesej pengguna
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

### Ejen Perancang dengan Orkestrasi Multi-Ejen

Dalam contoh ini, Ejen Penghala Semantik menerima permintaan pengguna (contohnya, "Saya memerlukan rancangan hotel untuk perjalanan saya.").

Perancang kemudian:

* Menerima Rancangan Hotel: Perancang mengambil mesej pengguna dan, berdasarkan arahan sistem (termasuk butiran ejen yang tersedia), menjana rancangan perjalanan berstruktur.
* Menyenaraikan Ejen dan Alat Mereka: daftar ejen menyimpan senarai ejen (contohnya, untuk penerbangan, hotel, sewa kereta, dan aktiviti) bersama fungsi atau alat yang mereka tawarkan.
* Menghala Pelan ke Ejen Berkaitan: Bergantung pada bilangan subtugas, perancang sama ada menghantar mesej terus kepada ejen khusus (untuk senario satu tugas) atau menyelaraskan melalui pengurus sembang kumpulan untuk kerjasama multi-ejen.
* Merumuskan Hasil: Akhirnya, perancang merumuskan pelan yang dijana untuk kejelasan.
Contoh kod Python berikut menggambarkan langkah-langkah ini:

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

# Model Subtugas Perjalanan

class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum # kami ingin menugaskan tugas kepada ejen

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Cipta klien

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

from pprint import pprint

# Tentukan mesej pengguna

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

# Cetak kandungan respons selepas memuatkannya sebagai JSON

pprint(json.loads(response_content))
```

What follows is the output from the previous code and you can then use this structured output to route to `assigned_agent` and summarize the travel plan to the end user.

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

An example notebook with the previous code sample is available [here](07-python-agent-framework.ipynb).

### Perancangan Iteratif

Sesetengah tugas memerlukan interaksi dua hala atau perancangan semula, di mana hasil satu subtugas mempengaruhi yang seterusnya. Sebagai contoh, jika ejen menemui format data yang tidak dijangka semasa menempah penerbangan, ia mungkin perlu menyesuaikan strateginya sebelum beralih ke tempahan hotel.

Selain itu, maklum balas pengguna (contohnya, seorang manusia memilih mereka lebih suka penerbangan yang lebih awal) boleh mencetuskan perancangan semula separa. Pendekatan dinamik dan iteratif ini memastikan bahawa penyelesaian akhir selaras dengan kekangan dunia sebenar dan keutamaan pengguna yang berkembang.

e.g sample code

```python
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential
#.. sama seperti kod sebelumnya dan teruskan sejarah pengguna, rancangan semasa

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
# .. rancang semula dan hantar tugasan kepada ejen masing-masing
```

Untuk perancangan yang lebih menyeluruh, lihat juga Magnetic One <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Catatan Blog</a> untuk menyelesaikan tugas kompleks.

## Ringkasan

Dalam artikel ini kami telah melihat contoh bagaimana kita boleh mencipta perancang yang boleh memilih secara dinamik ejen yang tersedia yang ditakrifkan. Output Perancang memecahkan tugas dan menetapkan ejen supaya ia boleh dijalankan. Diasumsikan ejen mempunyai akses kepada fungsi/alat yang diperlukan untuk melaksanakan tugas. Selain ejen, anda boleh memasukkan corak lain seperti refleksi, perumus, dan sembang pusingan untuk menyesuaikan lagi.

## Sumber Tambahan

Magentic One - Sistem multi-ejen umum untuk menyelesaikan tugas kompleks dan telah mencapai keputusan yang mengagumkan pada pelbagai penanda aras ejen yang mencabar. Rujukan: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. Dalam pelaksanaan ini pengorkestra mencipta pelan khusus tugasan dan mendelegasikan tugasan ini kepada ejen yang tersedia. Selain merancang, pengorkestra juga menggunakan mekanisme penjejakan untuk memantau kemajuan tugasan dan merancang semula apabila diperlukan.

### Ada Lagi Soalan tentang Corak Reka Bentuk Perancangan?

Sertai [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) untuk berjumpa dengan pelajar lain, menghadiri waktu pejabat dan mendapatkan jawapan kepada soalan Ejen AI anda.

## Pelajaran Sebelumnya

[Membina Ejen AI yang Boleh Dipercayai](../06-building-trustworthy-agents/README.md)

## Pelajaran Seterusnya

[Corak Reka Bentuk Multi-Ejen](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Penafian:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI Co-op Translator (https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi ralat atau ketidaktepatan. Dokumen asal dalam bahasa asalnya hendaklah dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, disyorkan mendapatkan penterjemahan profesional oleh penterjemah manusia. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsiran yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->