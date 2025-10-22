<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "498802b4c3c3cc486b86f27a12cebb34",
  "translation_date": "2025-08-29T18:04:09+00:00",
  "source_file": "06-building-trustworthy-agents/README.md",
  "language_code": "id"
}
-->
[![Trustworthy AI Agents](../../../translated_images/lesson-6-thumbnail.a58ab36c099038d4f786c2b0d5d6e89f41f4c2ecc05ab10b67bced2695eeb218.id.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Klik gambar di atas untuk menonton video pelajaran ini)_

# Membangun Agen AI yang Dapat Dipercaya

## Pendahuluan

Pelajaran ini akan membahas:

- Cara membangun dan menerapkan Agen AI yang aman dan efektif.
- Pertimbangan keamanan penting saat mengembangkan Agen AI.
- Cara menjaga privasi data dan pengguna saat mengembangkan Agen AI.

## Tujuan Pembelajaran

Setelah menyelesaikan pelajaran ini, Anda akan mengetahui cara:

- Mengidentifikasi dan mengurangi risiko saat membuat Agen AI.
- Menerapkan langkah-langkah keamanan untuk memastikan data dan akses dikelola dengan baik.
- Membuat Agen AI yang menjaga privasi data dan memberikan pengalaman pengguna yang berkualitas.

## Keamanan

Mari kita mulai dengan membahas cara membangun aplikasi agen yang aman. Keamanan berarti bahwa Agen AI berfungsi sesuai dengan desainnya. Sebagai pembuat aplikasi agen, kita memiliki metode dan alat untuk memaksimalkan keamanan:

### Membangun Kerangka Pesan Sistem

Jika Anda pernah membangun aplikasi AI menggunakan Large Language Models (LLMs), Anda pasti tahu pentingnya merancang prompt sistem atau pesan sistem yang kuat. Prompt ini menetapkan aturan meta, instruksi, dan pedoman tentang bagaimana LLM akan berinteraksi dengan pengguna dan data.

Untuk Agen AI, prompt sistem menjadi lebih penting karena Agen AI memerlukan instruksi yang sangat spesifik untuk menyelesaikan tugas yang telah kita rancang untuk mereka.

Untuk membuat prompt sistem yang dapat diskalakan, kita dapat menggunakan kerangka pesan sistem untuk membangun satu atau lebih agen dalam aplikasi kita:

![Building a System Message Framework](../../../translated_images/system-message-framework.3a97368c92d11d6814577b03cd128ec8c71a5fd1e26f341835cfa5df59ae87ae.id.png)

#### Langkah 1: Buat Meta Pesan Sistem

Meta prompt akan digunakan oleh LLM untuk menghasilkan prompt sistem bagi agen yang kita buat. Kita merancangnya sebagai template sehingga kita dapat dengan efisien membuat beberapa agen jika diperlukan.

Berikut adalah contoh meta pesan sistem yang akan kita berikan kepada LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Langkah 2: Buat Prompt Dasar

Langkah berikutnya adalah membuat prompt dasar untuk mendeskripsikan Agen AI. Anda harus menyertakan peran agen, tugas yang akan diselesaikan agen, dan tanggung jawab lainnya.

Berikut adalah contohnya:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Langkah 3: Berikan Pesan Sistem Dasar ke LLM

Sekarang kita dapat mengoptimalkan pesan sistem ini dengan memberikan meta pesan sistem sebagai pesan sistem dan pesan sistem dasar kita.

Ini akan menghasilkan pesan sistem yang lebih baik untuk memandu Agen AI kita:

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

Nilai dari kerangka pesan sistem ini adalah kemampuannya untuk mempermudah pembuatan pesan sistem untuk beberapa agen serta meningkatkan pesan sistem Anda seiring waktu. Jarang sekali Anda akan memiliki pesan sistem yang langsung berfungsi untuk semua kasus penggunaan Anda. Dengan melakukan penyesuaian kecil dan perbaikan pada pesan sistem dasar dan menjalankannya melalui sistem, Anda dapat membandingkan dan mengevaluasi hasilnya.

## Memahami Ancaman

Untuk membangun Agen AI yang dapat dipercaya, penting untuk memahami dan mengurangi risiko serta ancaman terhadap Agen AI Anda. Mari kita lihat beberapa ancaman terhadap Agen AI dan cara Anda dapat merencanakan serta mempersiapkannya dengan lebih baik.

![Understanding Threats](../../../translated_images/understanding-threats.89edeada8a97fc0f7053558567d5dd27c0c333b74e47fffdde490fa6777a4c17.id.png)

### Tugas dan Instruksi

**Deskripsi:** Penyerang mencoba mengubah instruksi atau tujuan Agen AI melalui prompt atau manipulasi input.

**Mitigasi:** Lakukan pemeriksaan validasi dan filter input untuk mendeteksi prompt yang berpotensi berbahaya sebelum diproses oleh Agen AI. Karena serangan ini biasanya memerlukan interaksi yang sering dengan Agen, membatasi jumlah giliran dalam percakapan adalah cara lain untuk mencegah jenis serangan ini.

### Akses ke Sistem Kritis

**Deskripsi:** Jika Agen AI memiliki akses ke sistem dan layanan yang menyimpan data sensitif, penyerang dapat mengkompromikan komunikasi antara agen dan layanan ini. Ini bisa berupa serangan langsung atau upaya tidak langsung untuk mendapatkan informasi tentang sistem ini melalui agen.

**Mitigasi:** Agen AI sebaiknya hanya memiliki akses ke sistem berdasarkan kebutuhan untuk mencegah jenis serangan ini. Komunikasi antara agen dan sistem juga harus aman. Menerapkan autentikasi dan kontrol akses adalah cara lain untuk melindungi informasi ini.

### Overloading Sumber Daya dan Layanan

**Deskripsi:** Agen AI dapat mengakses berbagai alat dan layanan untuk menyelesaikan tugas. Penyerang dapat memanfaatkan kemampuan ini untuk menyerang layanan tersebut dengan mengirimkan volume permintaan yang tinggi melalui Agen AI, yang dapat menyebabkan kegagalan sistem atau biaya tinggi.

**Mitigasi:** Terapkan kebijakan untuk membatasi jumlah permintaan yang dapat dilakukan Agen AI ke suatu layanan. Membatasi jumlah giliran percakapan dan permintaan ke Agen AI Anda adalah cara lain untuk mencegah jenis serangan ini.

### Peracunan Basis Pengetahuan

**Deskripsi:** Jenis serangan ini tidak menargetkan Agen AI secara langsung tetapi menargetkan basis pengetahuan dan layanan lain yang akan digunakan Agen AI. Ini bisa melibatkan merusak data atau informasi yang akan digunakan Agen AI untuk menyelesaikan tugas, yang mengarah pada respons yang bias atau tidak diinginkan kepada pengguna.

**Mitigasi:** Lakukan verifikasi rutin terhadap data yang akan digunakan Agen AI dalam alur kerjanya. Pastikan bahwa akses ke data ini aman dan hanya dapat diubah oleh individu terpercaya untuk menghindari jenis serangan ini.

### Kesalahan Berantai

**Deskripsi:** Agen AI mengakses berbagai alat dan layanan untuk menyelesaikan tugas. Kesalahan yang disebabkan oleh penyerang dapat menyebabkan kegagalan sistem lain yang terhubung dengan Agen AI, sehingga serangan menjadi lebih luas dan sulit untuk diatasi.

**Mitigasi:** Salah satu metode untuk menghindari ini adalah dengan membuat Agen AI beroperasi di lingkungan terbatas, seperti melakukan tugas di dalam kontainer Docker, untuk mencegah serangan langsung ke sistem. Membuat mekanisme fallback dan logika pengulangan ketika sistem tertentu merespons dengan kesalahan adalah cara lain untuk mencegah kegagalan sistem yang lebih besar.

## Human-in-the-Loop

Cara efektif lainnya untuk membangun sistem Agen AI yang dapat dipercaya adalah dengan menggunakan Human-in-the-loop. Ini menciptakan alur di mana pengguna dapat memberikan umpan balik kepada Agen selama proses berjalan. Pengguna pada dasarnya bertindak sebagai agen dalam sistem multi-agen dengan memberikan persetujuan atau penghentian proses yang sedang berjalan.

![Human in The Loop](../../../translated_images/human-in-the-loop.5f0068a678f62f4fc8373d5b78c4c22f35d9e4da35c93f66c3b634c1774eff34.id.png)

Berikut adalah cuplikan kode menggunakan AutoGen untuk menunjukkan bagaimana konsep ini diterapkan:

```python

# Create the agents.
model_client = OpenAIChatCompletionClient(model="gpt-4o-mini")
assistant = AssistantAgent("assistant", model_client=model_client)
user_proxy = UserProxyAgent("user_proxy", input_func=input)  # Use input() to get user input from console.

# Create the termination condition which will end the conversation when the user says "APPROVE".
termination = TextMentionTermination("APPROVE")

# Create the team.
team = RoundRobinGroupChat([assistant, user_proxy], termination_condition=termination)

# Run the conversation and stream to the console.
stream = team.run_stream(task="Write a 4-line poem about the ocean.")
# Use asyncio.run(...) when running in a script.
await Console(stream)

```

## Kesimpulan

Membangun Agen AI yang dapat dipercaya memerlukan desain yang hati-hati, langkah-langkah keamanan yang kuat, dan iterasi yang berkelanjutan. Dengan menerapkan sistem meta prompting yang terstruktur, memahami potensi ancaman, dan menerapkan strategi mitigasi, pengembang dapat menciptakan Agen AI yang aman dan efektif. Selain itu, mengintegrasikan pendekatan human-in-the-loop memastikan bahwa Agen AI tetap selaras dengan kebutuhan pengguna sambil meminimalkan risiko. Seiring perkembangan AI, menjaga sikap proaktif terhadap keamanan, privasi, dan pertimbangan etika akan menjadi kunci untuk membangun kepercayaan dan keandalan dalam sistem berbasis AI.

### Punya Pertanyaan Lebih Lanjut tentang Membangun Agen AI yang Dapat Dipercaya?

Bergabunglah dengan [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) untuk bertemu dengan pelajar lain, menghadiri jam konsultasi, dan mendapatkan jawaban atas pertanyaan Anda tentang Agen AI.

## Sumber Daya Tambahan

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Tinjauan AI yang Bertanggung Jawab</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluasi model AI generatif dan aplikasi AI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Pesan sistem keamanan</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Template Penilaian Risiko</a>

## Pelajaran Sebelumnya

[Agentic RAG](../05-agentic-rag/README.md)

## Pelajaran Selanjutnya

[Planning Design Pattern](../07-planning-design/README.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang timbul dari penggunaan terjemahan ini.