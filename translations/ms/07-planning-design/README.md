[![Planning Design Pattern](../../../translated_images/ms/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Klik imej di atas untuk menonton video pembelajaran ini)_

# Reka Bentuk Perancangan

## Pengenalan

Pelajaran ini akan meliputi

* Menetapkan matlamat keseluruhan yang jelas dan memecahkan tugasan kompleks kepada tugasan yang boleh diurus.
* Memanfaatkan output berstruktur untuk tindak balas yang lebih boleh dipercayai dan boleh dibaca oleh mesin.
* Menerapkan pendekatan berasaskan acara untuk mengendalikan tugasan dinamik dan input yang tidak dijangka.

## Matlamat Pembelajaran

Selepas melengkapkan pelajaran ini, anda akan memahami tentang:

* Mengenal pasti dan menetapkan matlamat keseluruhan untuk agen AI, memastikan ia jelas mengetahui apa yang perlu dicapai.
* Menguraikan tugasan kompleks kepada subtugasan yang boleh diurus dan menyusunnya dalam urutan logik.
* Melengkapkan agen dengan alat yang betul (contohnya, alat pencarian atau alat analitik data), memutuskan bila dan bagaimana digunakan, serta menangani keadaan tidak dijangka yang timbul.
* Menilai hasil subtugasan, mengukur prestasi, dan mengulangi tindakan untuk meningkatkan output akhir.

## Menetapkan Matlamat Keseluruhan dan Memecahkan Tugasan

![Menetapkan Matlamat dan Tugasan](../../../translated_images/ms/defining-goals-tasks.d70439e19e37c47a.webp)

Kebanyakan tugasan dunia nyata terlalu kompleks untuk diselesaikan dalam satu langkah. Agen AI memerlukan objektif yang ringkas untuk membimbing perancangan dan tindakannya. Contohnya, pertimbangkan matlamat:

    "Jana jadual perjalanan selama 3 hari."

Walaupun mudah untuk dinyatakan, ia masih memerlukan penambahbaikan. Semakin jelas matlamat, semakin baik agen (dan mana-mana kolaborator manusia) boleh menumpukan perhatian untuk mencapai hasil yang tepat, seperti mencipta jadual lengkap dengan pilihan penerbangan, cadangan hotel, dan saranan aktiviti.

### Penguraian Tugasan

Tugasan besar atau rumit menjadi lebih mudah diurus apabila dibahagikan kepada subtugasan yang berorientasikan matlamat yang lebih kecil.
Untuk contoh jadual perjalanan, anda boleh menguraikan matlamat kepada:

* Tempahan Penerbangan
* Tempahan Hotel
* Penyewaan Kereta
* Personalisasi

Setiap subtugasan kemudian boleh diurus oleh agen atau proses khusus. Satu agen mungkin pakar dalam mencari tawaran penerbangan terbaik, agen lain memfokus pada tempahan hotel, dan begitu seterusnya. Agen penyelaras atau "hulur ke bawah" boleh mengumpulkan hasil ini menjadi satu jadual kohesif untuk pengguna akhir.

Pendekatan modular ini juga membolehkan peningkatan secara berperingkat. Contohnya, anda boleh menambah agen khusus untuk Cadangan Makanan atau Cadangan Aktiviti Tempatan dan memperhalusi jadual perjalanan dari masa ke masa.

### Output Berstruktur

Model Bahasa Besar (LLM) boleh menghasilkan output berstruktur (contohnya JSON) yang lebih mudah untuk agen atau perkhidmatan huluan mengurai dan memprosesnya. Ini sangat berguna dalam konteks multi-agen, di mana kita boleh bertindak atas tugasan ini selepas output perancangan diterima.

Petikan Python berikut menunjukkan agen perancang yang mudah menguraikan matlamat kepada subtugasan dan menjana rancangan berstruktur:

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

# Model SubTugas Perjalanan
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # kami ingin menetapkan tugas kepada ejen

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Definisikan mesej pengguna
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

### Agen Perancang dengan Orkestrasi Multi-Agen

Dalam contoh ini, Agen Penghala Semantik menerima permintaan pengguna (contohnya, "Saya perlukan rancangan hotel untuk perjalanan saya.").

Perancang kemudian:

* Menerima Rancangan Hotel: Perancang mengambil mesej pengguna dan, berdasarkan arahan sistem (termasuk butiran agen yang tersedia), menjana rancangan perjalanan berstruktur.
* Menyenaraikan Agen dan Alat Mereka: Daftar agen memegang senarai agen (contohnya, untuk penerbangan, hotel, penyewaan kereta, dan aktiviti) bersama fungsi atau alat yang mereka tawarkan.
* Mengarahkan Rancangan kepada Agen Berkaitan: Bergantung pada bilangan subtugasan, perancang sama ada menghantar mesej terus ke agen khusus (untuk senario tugasan tunggal) atau menyelaraskan melalui pengurus kumpulan sembang untuk kolaborasi multi-agen.
* Merumuskan Hasil: Akhir sekali, perancang merumuskan rancangan yang dijana untuk kejelasan.
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

# Model SubTugas Perjalanan

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

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Cipta klien

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

from pprint import pprint

# Tetapkan mesej pengguna

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

Berikut adalah output dari kod sebelumnya dan anda boleh menggunakan output berstruktur ini untuk mengarahkan kepada `assigned_agent` dan merumuskan rancangan perjalanan kepada pengguna akhir.

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

Contoh buku nota dengan contoh kod sebelum ini boleh didapati [di sini](./code_samples/07-python-agent-framework.ipynb).

### Perancangan Berulang

Sesetengah tugasan memerlukan interaksi berulang atau perancangan semula, di mana hasil satu subtugasan mempengaruhi seterusnya. Contohnya, jika agen menemui format data yang tidak dijangka semasa menempah penerbangan, ia mungkin perlu menyesuaikan strateginya sebelum beralih ke tempahan hotel.

Selain itu, maklum balas pengguna (contohnya manusia memilih penerbangan lebih awal) boleh mencetuskan perancangan semula sebahagian. Pendekatan dinamik dan berulang ini memastikan penyelesaian akhir selaras dengan kekangan dunia nyata dan keutamaan pengguna yang berubah.

contohnya kod sampel

```python
import os
from agent_framework.foundry import FoundryChatClient
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

Untuk perancangan yang lebih komprehensif, sila lihat <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogpost</a> Magnetic One untuk menyelesaikan tugasan kompleks.

## Ringkasan

Dalam artikel ini, kita telah melihat contoh bagaimana kita boleh mencipta perancang yang boleh memilih agen yang tersedia secara dinamik. Output Perancang menguraikan tugasan dan menetapkan agen supaya ia dapat dilaksanakan. Diasumsikan agen mempunyai akses kepada fungsi/alat yang diperlukan untuk melaksanakan tugasan. Selain daripada agen, anda boleh memasukkan corak lain seperti refleksi, pereka rumusan, dan sembang pusingan robin untuk penyesuaian lebih lanjut.

## Sumber Tambahan

Magnetic One - Sistem multi-agen generalis untuk menyelesaikan tugasan kompleks dan telah mencapai keputusan mengagumkan pada pelbagai penanda aras agen sukar. Rujukan: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>. Dalam pelaksanaan ini, pengarah orkestrasi mencipta rancangan khusus tugasan dan mendelegasikan tugasan ini kepada agen yang ada. Selain perancangan, pengarah orkestrasi juga menggunakan mekanisme penjejakan untuk memantau kemajuan tugasan dan merancang semula jika diperlukan.

### Ada Soalan Lagi tentang Corak Reka Bentuk Perancangan?

Sertai [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) untuk bertemu dengan pelajar lain, menghadiri jam pejabat dan mendapatkan jawapan untuk soalan Agen AI anda.

## Pelajaran Sebelumnya

[Membina Agen AI yang Boleh Dipercayai](../06-building-trustworthy-agents/README.md)

## Pelajaran Seterusnya

[Corak Reka Bentuk Multi-Agen](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->