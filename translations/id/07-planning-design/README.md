[![Planning Design Pattern](../../../translated_images/id/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Klik gambar di atas untuk menonton video pelajaran ini)_

# Perencanaan Desain

## Pendahuluan

Pelajaran ini akan membahas

* Mendefinisikan tujuan keseluruhan yang jelas dan memecah tugas kompleks menjadi tugas-tugas yang dapat dikelola.
* Memanfaatkan output terstruktur untuk respons yang lebih dapat diandalkan dan dapat dibaca mesin.
* Menerapkan pendekatan berbasis acara untuk menangani tugas dinamis dan input tak terduga.

## Tujuan Pembelajaran

Setelah menyelesaikan pelajaran ini, Anda akan memahami tentang:

* Mengidentifikasi dan menetapkan tujuan keseluruhan untuk agen AI, memastikan agen tersebut tahu dengan jelas apa yang harus dicapai.
* Memecah tugas kompleks menjadi subtugas yang dapat dikelola dan mengaturnya dalam urutan logis.
* Melengkapi agen dengan alat yang tepat (misalnya, alat pencarian atau alat analitik data), memutuskan kapan dan bagaimana alat tersebut digunakan, serta menangani situasi tak terduga yang muncul.
* Mengevaluasi hasil subtugas, mengukur performa, dan mengulang tindakan untuk meningkatkan output akhir.

## Mendefinisikan Tujuan Keseluruhan dan Memecah Tugas

![Defining Goals and Tasks](../../../translated_images/id/defining-goals-tasks.d70439e19e37c47a.webp)

Sebagian besar tugas dunia nyata terlalu kompleks untuk ditangani dalam satu langkah. Agen AI membutuhkan tujuan yang ringkas untuk memandu perencanaan dan tindakannya. Misalnya, pertimbangkan tujuan:

    "Buat rencana perjalanan selama 3 hari."

Meskipun sederhana untuk diucapkan, tujuan ini masih perlu diperjelas. Semakin jelas tujuan, semakin baik agen (dan kolaborator manusia) dapat fokus mencapai hasil yang tepat, seperti membuat rencana perjalanan komprehensif dengan opsi penerbangan, rekomendasi hotel, dan saran aktivitas.

### Pemecahan Tugas

Tugas besar atau rumit menjadi lebih mudah dikelola ketika dibagi menjadi subtugas yang lebih kecil dan berorientasi tujuan.
Untuk contoh rencana perjalanan, Anda dapat memecah tujuan menjadi:

* Pemesanan Penerbangan
* Pemesanan Hotel
* Penyewaan Mobil
* Personalisasi

Setiap subtugas kemudian dapat ditangani oleh agen atau proses khusus. Satu agen mungkin mengkhususkan diri dalam mencari penawaran penerbangan terbaik, agen lain fokus pada pemesanan hotel, dan seterusnya. Agen pengoordinasi atau “downstream” kemudian dapat menyusun hasil ini menjadi satu rencana perjalanan yang kohesif untuk pengguna akhir.

Pendekatan modular ini juga memungkinkan peningkatan bertahap. Misalnya, Anda dapat menambahkan agen khusus untuk Rekomendasi Makanan atau Saran Aktivitas Lokal dan menyempurnakan rencana perjalanan dari waktu ke waktu.

### Output Terstruktur

Model Bahasa Besar (LLM) dapat menghasilkan output terstruktur (misalnya JSON) yang lebih mudah untuk diurai dan diproses oleh agen atau layanan downstream. Ini sangat berguna dalam konteks multi-agen, di mana kita dapat menindaklanjuti tugas ini setelah menerima output perencanaan.

Potongan kode Python berikut menunjukkan agen perencana sederhana yang memecah tujuan menjadi subtugas dan menghasilkan rencana terstruktur:

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
    assigned_agent: AgentEnum  # kami ingin menetapkan tugas kepada agen

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Definisikan pesan pengguna
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

### Agen Perencana dengan Orkestrasi Multi-Agen

Dalam contoh ini, Agen Semantic Router menerima permintaan pengguna (misalnya, "Saya perlu rencana hotel untuk perjalanan saya.").

Kemudian perencana:

* Menerima Rencana Hotel: Perencana mengambil pesan pengguna dan, berdasarkan prompt sistem (termasuk detail agen yang tersedia), menghasilkan rencana perjalanan terstruktur.
* Mendaftar Agen dan Alatnya: Registri agen memegang daftar agen (misalnya untuk penerbangan, hotel, sewa mobil, dan aktivitas) beserta fungsi atau alat yang mereka tawarkan.
* Mengarahkan Rencana ke Agen Terkait: Bergantung pada jumlah subtugas, perencana mengirim pesan langsung ke agen khusus (untuk skenario tugas tunggal) atau mengoordinasi melalui pengelola chat grup untuk kolaborasi multi-agen.
* Merangkum Hasil: Akhirnya, perencana merangkum rencana yang dihasilkan untuk kejelasan.
Contoh kode Python berikut menggambarkan langkah-langkah ini:

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
    assigned_agent: AgentEnum # kami ingin menetapkan tugas kepada agen

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool
import json
import os
from typing import Optional

from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Buat klien

provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

from pprint import pprint

# Tentukan pesan pengguna

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

# Cetak konten respons setelah memuatnya sebagai JSON

pprint(json.loads(response_content))
```

Berikut adalah output dari kode sebelumnya dan Anda kemudian dapat menggunakan output terstruktur ini untuk mengarahkan ke `assigned_agent` dan merangkum rencana perjalanan kepada pengguna akhir.

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

Notebook contoh dengan kode sebelumnya tersedia [di sini](./code_samples/07-python-agent-framework.ipynb).

### Perencanaan Iteratif

Beberapa tugas membutuhkan interaksi bolak-balik atau perencanaan ulang, di mana hasil dari satu subtugas memengaruhi berikutnya. Misalnya, jika agen menemukan format data tak terduga saat memesan penerbangan, ia mungkin perlu menyesuaikan strateginya sebelum melanjutkan ke pemesanan hotel.

Selain itu, umpan balik pengguna (misalnya manusia memutuskan mereka lebih suka penerbangan lebih awal) dapat memicu perencanaan ulang sebagian. Pendekatan dinamis dan iteratif ini memastikan solusi akhir sesuai dengan kendala dunia nyata dan preferensi pengguna yang berkembang.

contoh kode

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential
#.. sama seperti kode sebelumnya dan teruskan riwayat pengguna, rencana saat ini

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
# .. rencanakan ulang dan kirim tugas ke agen masing-masing
```

Untuk perencanaan yang lebih komprehensif, lihat blog <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a> untuk menyelesaikan tugas kompleks.

## Ringkasan

Dalam artikel ini kita telah melihat contoh bagaimana kita dapat membuat perencana yang dapat secara dinamis memilih agen yang tersedia yang telah didefinisikan. Output dari Perencana memecah tugas dan menetapkan agen sehingga mereka dapat dieksekusi. Diasumsikan agen memiliki akses ke fungsi/alat yang diperlukan untuk menjalankan tugas. Selain agen, Anda dapat memasukkan pola lain seperti refleksi, perangkum, dan chat round robin untuk menyesuaikan lebih lanjut.

## Sumber Daya Tambahan

Magnetic One - Sistem multi-agen generalis untuk menyelesaikan tugas kompleks dan telah mencapai hasil mengesankan pada beberapa tolok ukur agentik yang menantang. Referensi: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magnetic One</a>. Dalam implementasi ini, orkestrator membuat rencana khusus tugas dan mendelegasikan tugas-tugas ini ke agen yang tersedia. Selain perencanaan, orkestrator juga menggunakan mekanisme pelacakan untuk memantau kemajuan tugas dan merencanakan ulang jika diperlukan.

### Punya Pertanyaan Lebih Lanjut tentang Pola Perencanaan?

Bergabunglah dengan [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) untuk bertemu dengan pelajar lain, menghadiri jam kantor, dan mendapatkan jawaban atas pertanyaan tentang Agen AI Anda.

## Pelajaran Sebelumnya

[Membangun Agen AI yang Dapat Dipercaya](../06-building-trustworthy-agents/README.md)

## Pelajaran Selanjutnya

[Pola Desain Multi-Agen](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->