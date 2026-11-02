[![Agen AI Terpercaya](../../../translated_images/id/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Klik gambar di atas untuk menonton video pelajaran ini)_

# Membangun Agen AI yang Terpercaya

## Pendahuluan

Pelajaran ini akan membahas:

- Cara membangun dan menyebarkan Agen AI yang aman dan efektif
- Pertimbangan keamanan penting saat mengembangkan Agen AI.
- Cara menjaga privasi data dan pengguna saat mengembangkan Agen AI.

## Tujuan Pembelajaran

Setelah menyelesaikan pelajaran ini, Anda akan mengetahui cara untuk:

- Mengidentifikasi dan mengurangi risiko saat membuat Agen AI.
- Menerapkan langkah-langkah keamanan untuk memastikan bahwa data dan akses dikelola dengan benar.
- Membuat Agen AI yang menjaga privasi data dan memberikan pengalaman pengguna yang berkualitas.

## Keamanan

Mari kita lihat terlebih dahulu cara membangun aplikasi agen yang aman. Keamanan berarti bahwa agen AI beroperasi sesuai dengan desainnya. Sebagai pembuat aplikasi agen, kami memiliki metode dan alat untuk memaksimalkan keamanan:

### Membangun Kerangka Pesan Sistem

Jika Anda pernah membangun aplikasi AI menggunakan Large Language Models (LLM), Anda tahu pentingnya merancang prompt sistem atau pesan sistem yang kuat. Prompt ini menetapkan aturan meta, instruksi, dan pedoman bagaimana LLM akan berinteraksi dengan pengguna dan data.

Untuk Agen AI, prompt sistem jauh lebih penting karena Agen AI akan membutuhkan instruksi yang sangat spesifik untuk menyelesaikan tugas yang telah kita rancang untuk mereka.

Untuk membuat prompt sistem yang dapat diskalakan, kita dapat menggunakan kerangka pesan sistem untuk membangun satu atau lebih agen dalam aplikasi kita:

![Membangun Kerangka Pesan Sistem](../../../translated_images/id/system-message-framework.3a97368c92d11d68.webp)

#### Langkah 1: Buat Pesan Sistem Meta

Meta prompt akan digunakan oleh LLM untuk menghasilkan prompt sistem bagi agen yang kita buat. Kami merancangnya sebagai template agar dapat membuat beberapa agen secara efisien jika diperlukan.

Berikut adalah contoh pesan sistem meta yang akan kami berikan ke LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Langkah 2: Buat prompt dasar

Langkah berikutnya adalah membuat prompt dasar untuk mendeskripsikan Agen AI. Anda harus menyertakan peran agen, tugas yang akan diselesaikan agen, dan tanggung jawab lain dari agen tersebut.

Berikut adalah contohnya:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Langkah 3: Berikan Pesan Sistem Dasar ke LLM

Sekarang kita dapat mengoptimalkan pesan sistem ini dengan memberikan pesan sistem meta sebagai pesan sistem dan pesan sistem dasar kita.

Ini akan menghasilkan pesan sistem yang lebih baik untuk membimbing agen AI kita:

```markdown
**Company Name:** Contoso Travel  
**Role:** Travel Agent Assistant

**Objective:**  
You are an AI-powered travel agent assistant for Contoso Travel, specializing in booking flights and providing exceptional customer service. Your main goal is to assist customers in finding, booking, and managing their flights, all while ensuring that their preferences and needs are met efficiently.

**Key Responsibilities:**

1. **Flight Lookup:**
    
    - Assist customers in searching for available flights based on their specified destination, dates, and any other relevant preferences.
    - Provide a list of options, including flight times, airlines, layovers, and pricing.
2. **Flight Booking:**
    
    - Facilitate the booking of flights for customers, ensuring that all details are correctly entered into the system.
    - Confirm bookings and provide customers with their itinerary, including confirmation numbers and any other pertinent information.
3. **Customer Preference Inquiry:**
    
    - Actively ask customers for their preferences regarding seating (e.g., aisle, window, extra legroom) and preferred times for flights (e.g., morning, afternoon, evening).
    - Record these preferences for future reference and tailor suggestions accordingly.
4. **Flight Cancellation:**
    
    - Assist customers in canceling previously booked flights if needed, following company policies and procedures.
    - Notify customers of any necessary refunds or additional steps that may be required for cancellations.
5. **Flight Monitoring:**
    
    - Monitor the status of booked flights and alert customers in real-time about any delays, cancellations, or changes to their flight schedule.
    - Provide updates through preferred communication channels (e.g., email, SMS) as needed.

**Tone and Style:**

- Maintain a friendly, professional, and approachable demeanor in all interactions with customers.
- Ensure that all communication is clear, informative, and tailored to the customer's specific needs and inquiries.

**User Interaction Instructions:**

- Respond to customer queries promptly and accurately.
- Use a conversational style while ensuring professionalism.
- Prioritize customer satisfaction by being attentive, empathetic, and proactive in all assistance provided.

**Additional Notes:**

- Stay updated on any changes to airline policies, travel restrictions, and other relevant information that could impact flight bookings and customer experience.
- Use clear and concise language to explain options and processes, avoiding jargon where possible for better customer understanding.

This AI assistant is designed to streamline the flight booking process for customers of Contoso Travel, ensuring that all their travel needs are met efficiently and effectively.

```

#### Langkah 4: Iterasi dan Perbaikan

Nilai dari kerangka pesan sistem ini adalah kemampuan untuk mempermudah pembuatan pesan sistem dari beberapa agen sekaligus serta memperbaiki pesan sistem Anda seiring waktu. Jarang sekali Anda memiliki pesan sistem yang langsung berfungsi sempurna untuk keseluruhan kasus penggunaan Anda. Dengan dapat melakukan penyesuaian kecil dan perbaikan dengan mengubah pesan sistem dasar dan menjalankannya melalui sistem akan memungkinkan Anda membandingkan dan mengevaluasi hasilnya.

## Memahami Ancaman

Untuk membangun agen AI yang terpercaya, penting untuk memahami dan mengurangi risiko serta ancaman terhadap agen AI Anda. Mari kita lihat beberapa ancaman berbeda terhadap agen AI dan bagaimana Anda bisa lebih baik merencanakan dan mempersiapkannya.

![Memahami Ancaman](../../../translated_images/id/understanding-threats.89edeada8a97fc0f.webp)

### Tugas dan Instruksi

**Deskripsi:** Penyerang mencoba mengubah instruksi atau tujuan agen AI melalui prompting atau memanipulasi input.

**Mitigasi**: Laksanakan pemeriksaan validasi dan filter input untuk mendeteksi prompt yang berpotensi berbahaya sebelum diproses oleh Agen AI. Karena serangan ini umumnya memerlukan interaksi sering dengan Agen, membatasi jumlah giliran dalam percakapan adalah cara lain untuk mencegah jenis serangan ini.

### Akses ke Sistem Kritis

**Deskripsi**: Jika agen AI memiliki akses ke sistem dan layanan yang menyimpan data sensitif, penyerang dapat mengompromikan komunikasi antara agen dan layanan ini. Ini bisa berupa serangan langsung atau upaya tidak langsung untuk mendapatkan informasi tentang sistem tersebut melalui agen.

**Mitigasi**: Agen AI harus memiliki akses ke sistem hanya sesuai kebutuhan untuk mencegah jenis serangan ini. Komunikasi antara agen dan sistem juga harus aman. Menerapkan autentikasi dan kontrol akses adalah cara lain untuk melindungi informasi ini.

### Beban Berlebih pada Sumber Daya dan Layanan

**Deskripsi:** Agen AI dapat mengakses alat dan layanan berbeda untuk menyelesaikan tugas. Penyerang dapat menggunakan kemampuan ini untuk menyerang layanan dengan mengirimkan volume permintaan yang tinggi melalui Agen AI, yang dapat menyebabkan kegagalan sistem atau biaya tinggi.

**Mitigasi:** Terapkan kebijakan untuk membatasi jumlah permintaan yang dapat dibuat agen AI ke suatu layanan. Membatasi jumlah giliran percakapan dan permintaan ke agen AI Anda adalah cara lain untuk mencegah jenis serangan ini.

### Pengotretan Basis Pengetahuan

**Deskripsi:** Jenis serangan ini tidak langsung menargetkan agen AI tetapi menargetkan basis pengetahuan dan layanan lain yang digunakan oleh agen AI. Ini bisa melibatkan korupsi data atau informasi yang digunakan agen AI untuk menyelesaikan tugas, yang mengakibatkan respons bias atau tidak diinginkan kepada pengguna.

**Mitigasi:** Lakukan verifikasi data secara rutin yang akan digunakan agen AI dalam alur kerjanya. Pastikan bahwa akses ke data ini aman dan hanya dapat diubah oleh individu terpercaya untuk menghindari jenis serangan ini.

### Kesalahan Berantai

**Deskripsi:** Agen AI mengakses berbagai alat dan layanan untuk menyelesaikan tugas. Kesalahan yang disebabkan oleh penyerang dapat menyebabkan kegagalan sistem lain yang terhubung dengan agen AI, membuat serangan menjadi lebih luas dan lebih sulit ditangani.

**Mitigasi**: Salah satu metode untuk menghindari hal ini adalah agar Agen AI beroperasi dalam lingkungan terbatas, seperti melakukan tugas di dalam kontainer Docker, untuk mencegah serangan langsung ke sistem. Membuat mekanisme cadangan dan logika pengulangan saat sistem tertentu merespons dengan kesalahan adalah cara lain untuk mencegah kegagalan sistem yang lebih besar.

## Human-in-the-Loop

Cara efektif lain untuk membangun sistem Agen AI yang terpercaya adalah dengan menggunakan Human-in-the-loop. Ini menciptakan alur dimana pengguna dapat memberikan umpan balik kepada Agen selama proses berjalan. Pengguna secara esensial bertindak sebagai agen dalam sistem multi-agen dengan memberikan persetujuan atau penghentian proses yang sedang berjalan.

![Human in The Loop](../../../translated_images/id/human-in-the-loop.5f0068a678f62f4f.webp)

Berikut adalah potongan kode menggunakan Microsoft Agent Framework untuk menunjukkan bagaimana konsep ini diterapkan:

```python
import os
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

# Buat penyedia dengan persetujuan dari manusia dalam prosesnya
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Buat agen dengan langkah persetujuan dari manusia
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Pengguna dapat meninjau dan menyetujui respon tersebut
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Kesimpulan

Membangun agen AI yang terpercaya memerlukan desain yang cermat, langkah keamanan yang kuat, dan iterasi berkelanjutan. Dengan menerapkan sistem meta prompt terstruktur, memahami potensi ancaman, dan menerapkan strategi mitigasi, pengembang dapat menciptakan agen AI yang aman dan efektif. Selain itu, dengan mengintegrasikan pendekatan human-in-the-loop memastikan agen AI tetap selaras dengan kebutuhan pengguna sekaligus meminimalkan risiko. Seiring dengan perkembangan AI, menjaga sikap proaktif terhadap keamanan, privasi, dan pertimbangan etis akan menjadi kunci dalam membangun kepercayaan dan keandalan pada sistem yang digerakkan oleh AI.

## Contoh Kode

- [`code_samples/06-system-message-framework.ipynb`](code_samples/06-system-message-framework.ipynb): Demonstrasi langkah demi langkah kerangka pesan sistem meta prompt.
- [`code_samples/06-human-in-the-loop.ipynb`](code_samples/06-human-in-the-loop.ipynb): Gerbang persetujuan pra-aksi, pengelompokan risiko, dan pencatatan audit untuk agen yang terpercaya.

### Ada Pertanyaan Lebih Lanjut tentang Membangun Agen AI yang Terpercaya?

Bergabunglah dengan [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) untuk bertemu dengan pembelajar lainnya, mengikuti jam kantor, dan mendapatkan jawaban atas pertanyaan Anda tentang Agen AI.

## Sumber Daya Tambahan

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Tinjauan AI Bertanggung Jawab</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluasi model AI generatif dan aplikasi AI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Pesan sistem untuk keamanan</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Template Penilaian Risiko</a>

## Pelajaran Sebelumnya

[Agentic RAG](../05-agentic-rag/README.md)

## Pelajaran Berikutnya

[Pola Desain Perencanaan](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->