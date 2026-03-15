[![Polanya Desain Perencanaan](../../../translated_images/id/lesson-7-thumbnail.f7163ac557bea123.webp)](https://youtu.be/kPfJ2BrBCMY?si=9pYpPXp0sSbK91Dr)

> _(Klik gambar di atas untuk melihat video pelajaran ini)_

# Perencanaan Desain

## Pendahuluan

Pelajaran ini akan membahas

* Mendefinisikan tujuan keseluruhan yang jelas dan memecah tugas kompleks menjadi tugas yang dapat dikelola.
* Memanfaatkan output terstruktur untuk tanggapan yang lebih dapat diandalkan dan dapat dibaca mesin.
* Menerapkan pendekatan berbasis peristiwa untuk menangani tugas dinamis dan input tak terduga.

## Tujuan Pembelajaran

Setelah menyelesaikan pelajaran ini, Anda akan memahami tentang:

* Mengidentifikasi dan menetapkan tujuan keseluruhan untuk agen AI, memastikan agen tersebut dengan jelas mengetahui apa yang harus dicapai.
* Menguraikan tugas kompleks menjadi subtugas yang dapat dikelola dan mengorganisasikannya ke dalam urutan logis.
* Melengkapi agen dengan alat yang tepat (misalnya, alat pencarian atau alat analitik data), memutuskan kapan dan bagaimana alat tersebut digunakan, serta menangani situasi tak terduga yang muncul.
* Mengevaluasi hasil subtugas, mengukur kinerja, dan mengulangi tindakan untuk meningkatkan output akhir.

## Mendefinisikan Tujuan Keseluruhan dan Memecah Tugas

![Mendefinisikan Tujuan dan Tugas](../../../translated_images/id/defining-goals-tasks.d70439e19e37c47a.webp)

Sebagian besar tugas dunia nyata terlalu kompleks untuk ditangani dalam satu langkah. Agen AI membutuhkan tujuan singkat untuk membimbing perencanaan dan tindakannya. Misalnya, pertimbangkan tujuan:

    "Membuat rencana perjalanan selama 3 hari."

Meskipun sederhana untuk dikatakan, tujuan ini masih perlu penyempurnaan. Semakin jelas tujuan, semakin baik agen (dan kolaborator manusia) dapat fokus pada mencapai hasil yang tepat, seperti membuat rencana perjalanan lengkap dengan opsi penerbangan, rekomendasi hotel, dan saran aktivitas.

### Pemecahan Tugas

Tugas besar atau rumit menjadi lebih mudah diatur saat dibagi menjadi subtugas yang berorientasi tujuan.
Untuk contoh rencana perjalanan, Anda dapat memecah tujuan menjadi:

* Pemesanan Penerbangan
* Pemesanan Hotel
* Penyewaan Mobil
* Personalisasi

Setiap subtugas kemudian dapat dikerjakan oleh agen atau proses khusus. Satu agen mungkin mengkhususkan diri dalam mencari penawaran penerbangan terbaik, agen lain fokus pada pemesanan hotel, dan seterusnya. Agen pengoordinasi atau "downstream" dapat kemudian menyatukan hasil ini ke dalam satu rencana perjalanan yang terpadu untuk pengguna akhir.

Pendekatan modular ini juga memungkinkan peningkatan bertahap. Misalnya, Anda dapat menambahkan agen khusus untuk Rekomendasi Makanan atau Saran Aktivitas Lokal dan menyempurnakan rencana perjalanan dari waktu ke waktu.

### Output Terstruktur

Model Bahasa Besar (LLM) dapat menghasilkan output terstruktur (misalnya JSON) yang lebih mudah untuk diurai dan diproses oleh agen atau layanan downstream. Ini sangat berguna dalam konteks multi-agen, di mana kita dapat menindaklanjuti tugas-tugas ini setelah output perencanaan diterima.

Cuplikan kode Python berikut menunjukkan agen perencanaan sederhana yang memecah tujuan menjadi subtugas dan menghasilkan rencana terstruktur:

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

# Model SubTugas Perjalanan
class TravelSubTask(BaseModel):
    task_details: str
    assigned_agent: AgentEnum  # kami ingin menetapkan tugas kepada agen

class TravelPlan(BaseModel):
    main_task: str
    subtasks: List[TravelSubTask]
    is_greeting: bool

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

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

### Agen Perencanaan dengan Orkestrasi Multi-Agen

Dalam contoh ini, Agen Pengarah Semantik (Semantic Router Agent) menerima permintaan pengguna (misalnya, "Saya butuh rencana hotel untuk perjalanan saya.").

Perencana kemudian:

* Menerima Rencana Hotel: Perencana mengambil pesan pengguna dan, berdasarkan prompt sistem (termasuk detail agen yang tersedia), menghasilkan rencana perjalanan terstruktur.
* Mendaftar Agen dan Alatnya: Daftar agen memuat agen-agen (misalnya, untuk penerbangan, hotel, penyewaan mobil, dan aktivitas) beserta fungsi atau alat yang mereka tawarkan.
* Mengarahkan Rencana ke Agen yang Bersangkutan: Tergantung pada jumlah subtugas, perencana mengirim pesan langsung ke agen khusus (untuk skenario tugas tunggal) atau mengoordinasikan melalui pengelola grup chat untuk kolaborasi multi-agen.
* Merangkum Hasil: Akhirnya, perencana merangkum rencana yang dihasilkan untuk kejelasan.
Kode Python berikut mengilustrasikan langkah-langkah ini:

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

from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Buat klien

provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

from pprint import pprint

# Definisikan pesan pengguna

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

Yang berikut adalah output dari kode sebelumnya dan Anda dapat menggunakan output terstruktur ini untuk diarahkan ke `assigned_agent` dan merangkum rencana perjalanan kepada pengguna akhir.

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

Notebook contoh dengan kode sebelumnya tersedia [di sini](07-python-agent-framework.ipynb).

### Perencanaan Iteratif

Beberapa tugas memerlukan proses bolak-balik atau perencanaan ulang, di mana hasil dari satu subtugas memengaruhi yang berikutnya. Misalnya, jika agen menemukan format data tak terduga saat memesan penerbangan, ia mungkin perlu menyesuaikan strateginya sebelum melanjutkan ke pemesanan hotel.

Selain itu, umpan balik pengguna (misalnya, manusia yang memutuskan mereka lebih memilih penerbangan lebih awal) dapat memicu perencanaan ulang sebagian. Pendekatan dinamis dan iteratif ini memastikan solusi akhir sesuai dengan kendala dunia nyata dan preferensi pengguna yang berubah.

contoh kode

```python
from agent_framework.azure import AzureAIProjectAgentProvider
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
# .. rencanakan ulang dan kirimkan tugas ke agen masing-masing
```

Untuk perencanaan yang lebih komprehensif, lihat <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Blogpost Magnetic One</a> untuk menyelesaikan tugas kompleks.

## Ringkasan

Dalam artikel ini kita telah melihat contoh bagaimana kita dapat membuat perencana yang dapat memilih agen yang tersedia secara dinamis sesuai definisi. Output dari Perencana memecah tugas dan menetapkan agen sehingga tugas dapat dilaksanakan. Diasumsikan agen memiliki akses ke fungsi/alat yang diperlukan untuk melakukan tugas. Selain agen Anda juga dapat memasukkan pola lain seperti refleksi, perangkum, dan obrolan giliran untuk menyesuaikan lebih lanjut.

## Sumber Daya Tambahan

Magentic One - Sistem multi-agen generalis untuk menyelesaikan tugas kompleks dan telah mencapai hasil mengesankan dalam berbagai tolok ukur agenik yang menantang. Referensi: <a href="https://www.microsoft.com/research/articles/magentic-one-a-generalist-multi-agent-system-for-solving-complex-tasks" target="_blank">Magentic One</a>. Dalam implementasi ini, pengoordinasi membuat rencana khusus tugas dan mendelegasikan tugas-tugas ini ke agen yang tersedia. Selain perencanaan, pengoordinasi juga menggunakan mekanisme pelacakan untuk memantau kemajuan tugas dan melakukan perencanaan ulang sesuai kebutuhan.

### Punya Pertanyaan Lebih Lanjut tentang Pola Desain Perencanaan?

Bergabunglah dengan [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) untuk bertemu dengan pelajar lain, menghadiri sesi tanya jawab, dan mendapatkan jawaban untuk pertanyaan Anda tentang Agen AI.

## Pelajaran Sebelumnya

[Membangun Agen AI Terpercaya](../06-building-trustworthy-agents/README.md)

## Pelajaran Selanjutnya

[Pola Desain Multi-Agen](../08-multi-agent/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk menjaga keakuratan, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh penerjemah manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang salah yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->