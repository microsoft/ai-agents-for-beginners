[![Agent AI Terpercaya](../../../translated_images/id/lesson-6-thumbnail.a58ab36c099038d4.webp)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Klik gambar di atas untuk melihat video pelajaran ini)_

# Membangun Agent AI Terpercaya

## Pendahuluan

Pelajaran ini akan membahas:

- Cara membangun dan menerapkan Agent AI yang aman dan efektif
- Pertimbangan keamanan penting saat mengembangkan Agent AI.
- Cara menjaga data dan privasi pengguna saat mengembangkan Agent AI.

## Tujuan Pembelajaran

Setelah menyelesaikan pelajaran ini, Anda akan mengetahui cara untuk:

- Mengidentifikasi dan mengurangi risiko saat membuat Agent AI.
- Menerapkan langkah-langkah keamanan untuk memastikan bahwa data dan akses dikelola dengan tepat.
- Membuat Agent AI yang menjaga privasi data dan memberikan pengalaman pengguna berkualitas.

## Keamanan

Mari kita lihat terlebih dahulu bagaimana membangun aplikasi agentik yang aman. Keamanan berarti bahwa agent AI berfungsi sesuai desain. Sebagai pembangun aplikasi agentik, kita memiliki metode dan alat untuk memaksimalkan keamanan:

### Membangun Kerangka Pesan Sistem

Jika Anda pernah membangun aplikasi AI menggunakan Large Language Models (LLM), Anda tahu pentingnya merancang prompt sistem atau pesan sistem yang kuat. Prompt ini menetapkan aturan meta, instruksi, dan panduan tentang bagaimana LLM akan berinteraksi dengan pengguna dan data.

Untuk Agent AI, prompt sistem bahkan lebih penting karena Agent AI memerlukan instruksi yang sangat spesifik untuk menyelesaikan tugas yang telah kita desain untuk mereka.

Untuk membuat prompt sistem yang dapat diskalakan, kita dapat menggunakan kerangka pesan sistem untuk membangun satu atau lebih agent dalam aplikasi kita:

![Membangun Kerangka Pesan Sistem](../../../translated_images/id/system-message-framework.3a97368c92d11d68.webp)

#### Langkah 1: Buat Pesan Sistem Meta

Prompt meta akan digunakan oleh LLM untuk menghasilkan prompt sistem bagi agent yang kita buat. Kita merancangnya sebagai template sehingga kita dapat dengan efisien membuat beberapa agent jika diperlukan.

Berikut adalah contoh pesan sistem meta yang akan kita berikan ke LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Langkah 2: Buat prompt dasar

Langkah berikutnya adalah membuat prompt dasar untuk menjelaskan Agent AI. Anda harus menyertakan peran agent, tugas yang akan dilakukan agent, dan tanggung jawab lainnya dari agent tersebut.

Berikut adalah contoh:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Langkah 3: Berikan Pesan Sistem Dasar ke LLM

Sekarang kita dapat mengoptimalkan pesan sistem ini dengan menyediakan pesan sistem meta sebagai pesan sistem dan pesan sistem dasar kita.

Ini akan menghasilkan pesan sistem yang lebih baik dirancang untuk membimbing Agent AI kita:

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

Nilai dari kerangka pesan sistem ini adalah kemampuannya untuk memperluas pembuatan pesan sistem dari banyak agent dengan lebih mudah serta meningkatkan pesan sistem Anda dari waktu ke waktu. Jarang Anda memiliki pesan sistem yang berhasil pada percobaan pertama untuk kasus penggunaan lengkap Anda. Mampu melakukan penyempurnaan kecil dan perbaikan dengan mengubah pesan sistem dasar dan menjalankannya melalui sistem akan memungkinkan Anda membandingkan dan mengevaluasi hasil.

## Memahami Ancaman

Untuk membangun agent AI yang dapat dipercaya, penting untuk memahami dan mengurangi risiko dan ancaman terhadap agent AI Anda. Mari kita lihat beberapa ancaman berbeda terhadap agent AI dan bagaimana Anda dapat merencanakan dan mempersiapkannya dengan lebih baik.

![Memahami Ancaman](../../../translated_images/id/understanding-threats.89edeada8a97fc0f.webp)

### Tugas dan Instruksi

**Deskripsi:** Penyerang mencoba mengubah instruksi atau tujuan agent AI melalui pemicu perintah atau manipulasi input.

**Mitigasi**: Lakukan pemeriksaan validasi dan filter input untuk mendeteksi prompt berbahaya sebelum diproses oleh Agent AI. Karena serangan ini biasanya memerlukan interaksi berulang dengan Agent, membatasi jumlah giliran dalam percakapan adalah cara lain untuk mencegah jenis serangan ini.

### Akses ke Sistem Kritis

**Deskripsi**: Jika agent AI memiliki akses ke sistem dan layanan yang menyimpan data sensitif, penyerang dapat mengompromikan komunikasi antara agent dan layanan tersebut. Ini bisa berupa serangan langsung atau upaya tidak langsung untuk mendapatkan informasi tentang sistem melalui agent.

**Mitigasi**: Agent AI harus memiliki akses ke sistem hanya berdasarkan kebutuhan untuk mencegah jenis serangan ini. Komunikasi antara agent dan sistem juga harus aman. Menerapkan otentikasi dan kontrol akses adalah cara lain untuk melindungi informasi ini.

### Beban Berlebih pada Sumber Daya dan Layanan

**Deskripsi:** Agent AI dapat mengakses berbagai alat dan layanan untuk menyelesaikan tugas. Penyerang dapat menggunakan kemampuan ini untuk menyerang layanan dengan mengirimkan volume permintaan tinggi melalui Agent AI, yang dapat menyebabkan kegagalan sistem atau biaya tinggi.

**Mitigasi:** Terapkan kebijakan untuk membatasi jumlah permintaan yang dapat dibuat Agent AI ke suatu layanan. Membatasi jumlah giliran percakapan dan permintaan ke Agent AI Anda adalah cara lain untuk mencegah jenis serangan ini.

### Keracunan Basis Pengetahuan

**Deskripsi:** Jenis serangan ini tidak langsung menargetkan Agent AI tetapi menargetkan basis pengetahuan dan layanan lain yang akan digunakan Agent AI. Ini bisa melibatkan merusak data atau informasi yang digunakan Agent AI untuk menyelesaikan tugas, yang mengarah pada respons yang bias atau tidak diinginkan kepada pengguna.

**Mitigasi:** Lakukan verifikasi rutin terhadap data yang akan digunakan Agent AI dalam alur kerjanya. Pastikan akses ke data ini aman dan hanya diubah oleh individu terpercaya untuk menghindari jenis serangan ini.

### Kesalahan Berjenjang

**Deskripsi:** Agent AI mengakses berbagai alat dan layanan untuk menyelesaikan tugas. Kesalahan yang disebabkan oleh penyerang dapat menyebabkan kegagalan sistem lain yang terhubung dengan agent tersebut, sehingga serangan menjadi lebih meluas dan sulit ditangani.

**Mitigasi**: Salah satu metode untuk menghindari hal ini adalah agar Agent AI beroperasi di lingkungan terbatas, seperti menjalankan tugas dalam container Docker, untuk mencegah serangan langsung ke sistem. Membuat mekanisme fallback dan logika percobaan ulang ketika sistem tertentu merespons dengan kesalahan adalah cara lain untuk mencegah kegagalan sistem yang lebih besar.

## Manusia dalam Rantai (Human-in-the-Loop)

Cara efektif lain untuk membangun sistem Agent AI terpercaya adalah menggunakan Human-in-the-loop. Ini menciptakan aliran di mana pengguna dapat memberikan umpan balik kepada Agent selama proses berjalan. Pengguna secara esensial bertindak sebagai agent dalam sistem multi-agent dan memberikan persetujuan atau menghentikan proses yang sedang berjalan.

![Manusia dalam Rantai](../../../translated_images/id/human-in-the-loop.5f0068a678f62f4f.webp)

Berikut ini adalah potongan kode yang menggunakan Microsoft Agent Framework untuk menunjukkan bagaimana konsep ini diimplementasikan:

```python
import os
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

# Buat penyedia dengan persetujuan manusia dalam proses
provider = AzureAIProjectAgentProvider(
    credential=AzureCliCredential(),
)

# Buat agen dengan langkah persetujuan manusia
response = provider.create_response(
    input="Write a 4-line poem about the ocean.",
    instructions="You are a helpful assistant. Ask for user approval before finalizing.",
)

# Pengguna dapat meninjau dan menyetujui respons
print(response.output_text)
user_input = input("Do you approve? (APPROVE/REJECT): ")
if user_input == "APPROVE":
    print("Response approved.")
else:
    print("Response rejected. Revising...")
```

## Kesimpulan

Membangun agent AI terpercaya membutuhkan desain yang cermat, langkah-langkah keamanan yang kuat, dan iterasi berkelanjutan. Dengan menerapkan sistem meta prompting yang terstruktur, memahami ancaman potensial, dan menerapkan strategi mitigasi, pengembang dapat membuat agent AI yang aman dan efektif. Selain itu, mengadopsi pendekatan human-in-the-loop memastikan agent AI tetap selaras dengan kebutuhan pengguna sekaligus meminimalkan risiko. Seiring AI terus berkembang, mempertahankan sikap proaktif terhadap keamanan, privasi, dan pertimbangan etis akan menjadi kunci untuk membangun kepercayaan dan keandalan dalam sistem yang digerakkan oleh AI.

### Punya Pertanyaan Lebih Lanjut tentang Membangun Agent AI Terpercaya?

Bergabunglah dengan [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) untuk bertemu dengan pelajar lain, menghadiri jam kantor, dan mendapatkan jawaban atas pertanyaan Agent AI Anda.

## Sumber Daya Tambahan

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Gambaran AI Bertanggung Jawab</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluasi model AI generatif dan aplikasi AI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Pesan sistem keamanan</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Template Penilaian Risiko</a>

## Pelajaran Sebelumnya

[Agentic RAG](../05-agentic-rag/README.md)

## Pelajaran Berikutnya

[Polanya Desain Perencanaan](../07-planning-design/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->