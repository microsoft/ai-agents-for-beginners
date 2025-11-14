<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "498802b4c3c3cc486b86f27a12cebb34",
  "translation_date": "2025-08-29T18:16:53+00:00",
  "source_file": "06-building-trustworthy-agents/README.md",
  "language_code": "ms"
}
-->
[![Trustworthy AI Agents](../../../translated_images/lesson-6-thumbnail.a58ab36c099038d4f786c2b0d5d6e89f41f4c2ecc05ab10b67bced2695eeb218.ms.png)](https://youtu.be/iZKkMEGBCUQ?si=Q-kEbcyHUMPoHp8L)

> _(Klik imej di atas untuk menonton video pelajaran ini)_

# Membina Ejen AI yang Boleh Dipercayai

## Pengenalan

Pelajaran ini akan merangkumi:

- Cara membina dan melancarkan Ejen AI yang selamat dan berkesan
- Pertimbangan keselamatan penting semasa membangunkan Ejen AI
- Cara mengekalkan privasi data dan pengguna semasa membangunkan Ejen AI

## Matlamat Pembelajaran

Selepas menyelesaikan pelajaran ini, anda akan tahu cara untuk:

- Mengenal pasti dan mengurangkan risiko semasa mencipta Ejen AI.
- Melaksanakan langkah keselamatan untuk memastikan data dan akses diuruskan dengan betul.
- Mencipta Ejen AI yang mengekalkan privasi data dan memberikan pengalaman pengguna yang berkualiti.

## Keselamatan

Mari kita lihat terlebih dahulu cara membina aplikasi ejen yang selamat. Keselamatan bermaksud bahawa ejen AI berfungsi seperti yang direka. Sebagai pembangun aplikasi ejen, kita mempunyai kaedah dan alat untuk memaksimumkan keselamatan:

### Membina Rangka Kerja Mesej Sistem

Jika anda pernah membina aplikasi AI menggunakan Model Bahasa Besar (LLM), anda pasti tahu betapa pentingnya mereka bentuk arahan sistem atau mesej sistem yang kukuh. Arahan ini menetapkan peraturan meta, arahan, dan garis panduan tentang bagaimana LLM akan berinteraksi dengan pengguna dan data.

Bagi Ejen AI, arahan sistem adalah lebih penting kerana Ejen AI memerlukan arahan yang sangat spesifik untuk menyelesaikan tugas yang telah kita reka untuk mereka.

Untuk mencipta arahan sistem yang boleh diskalakan, kita boleh menggunakan rangka kerja mesej sistem untuk membina satu atau lebih ejen dalam aplikasi kita:

![Building a System Message Framework](../../../translated_images/system-message-framework.3a97368c92d11d6814577b03cd128ec8c71a5fd1e26f341835cfa5df59ae87ae.ms.png)

#### Langkah 1: Cipta Mesej Sistem Meta

Arahan meta akan digunakan oleh LLM untuk menjana arahan sistem bagi ejen yang kita cipta. Kita mereka bentuknya sebagai templat supaya kita boleh mencipta pelbagai ejen dengan cekap jika diperlukan.

Berikut adalah contoh mesej sistem meta yang akan kita berikan kepada LLM:

```plaintext
You are an expert at creating AI agent assistants. 
You will be provided a company name, role, responsibilities and other
information that you will use to provide a system prompt for.
To create the system prompt, be descriptive as possible and provide a structure that a system using an LLM can better understand the role and responsibilities of the AI assistant. 
```

#### Langkah 2: Cipta Arahan Asas

Langkah seterusnya adalah mencipta arahan asas untuk menerangkan Ejen AI. Anda harus memasukkan peranan ejen, tugas yang akan diselesaikan oleh ejen, dan tanggungjawab lain ejen.

Berikut adalah contoh:

```plaintext
You are a travel agent for Contoso Travel that is great at booking flights for customers. To help customers you can perform the following tasks: lookup available flights, book flights, ask for preferences in seating and times for flights, cancel any previously booked flights and alert customers on any delays or cancellations of flights.  
```

#### Langkah 3: Berikan Mesej Sistem Asas kepada LLM

Sekarang kita boleh mengoptimumkan mesej sistem ini dengan memberikan mesej sistem meta sebagai mesej sistem dan mesej sistem asas kita.

Ini akan menghasilkan mesej sistem yang lebih baik untuk membimbing ejen AI kita:

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

#### Langkah 4: Iterasi dan Penambahbaikan

Nilai rangka kerja mesej sistem ini adalah untuk memudahkan penciptaan mesej sistem untuk pelbagai ejen serta meningkatkan mesej sistem anda dari semasa ke semasa. Jarang sekali anda akan mempunyai mesej sistem yang berfungsi dengan sempurna pada kali pertama untuk keseluruhan kes penggunaan anda. Dengan membuat perubahan kecil dan penambahbaikan pada mesej sistem asas dan menjalankannya melalui sistem, anda boleh membandingkan dan menilai hasilnya.

## Memahami Ancaman

Untuk membina ejen AI yang boleh dipercayai, adalah penting untuk memahami dan mengurangkan risiko dan ancaman kepada ejen AI anda. Mari kita lihat beberapa ancaman yang berbeza kepada ejen AI dan cara anda boleh merancang dan bersedia dengan lebih baik untuk menghadapinya.

![Understanding Threats](../../../translated_images/understanding-threats.89edeada8a97fc0f7053558567d5dd27c0c333b74e47fffdde490fa6777a4c17.ms.png)

### Tugas dan Arahan

**Penerangan:** Penyerang cuba mengubah arahan atau matlamat ejen AI melalui arahan atau manipulasi input.

**Mitigasi**: Laksanakan pemeriksaan pengesahan dan penapis input untuk mengesan arahan yang berpotensi berbahaya sebelum diproses oleh Ejen AI. Oleh kerana serangan ini biasanya memerlukan interaksi yang kerap dengan Ejen, mengehadkan bilangan giliran dalam perbualan adalah cara lain untuk mencegah serangan jenis ini.

### Akses kepada Sistem Kritikal

**Penerangan**: Jika ejen AI mempunyai akses kepada sistem dan perkhidmatan yang menyimpan data sensitif, penyerang boleh menjejaskan komunikasi antara ejen dan perkhidmatan ini. Ini boleh menjadi serangan langsung atau percubaan tidak langsung untuk mendapatkan maklumat tentang sistem ini melalui ejen.

**Mitigasi**: Ejen AI hanya sepatutnya mempunyai akses kepada sistem berdasarkan keperluan sahaja untuk mencegah serangan jenis ini. Komunikasi antara ejen dan sistem juga harus selamat. Melaksanakan pengesahan dan kawalan akses adalah cara lain untuk melindungi maklumat ini.

### Beban Berlebihan pada Sumber dan Perkhidmatan

**Penerangan:** Ejen AI boleh mengakses pelbagai alat dan perkhidmatan untuk menyelesaikan tugas. Penyerang boleh menggunakan keupayaan ini untuk menyerang perkhidmatan ini dengan menghantar sejumlah besar permintaan melalui Ejen AI, yang boleh menyebabkan kegagalan sistem atau kos yang tinggi.

**Mitigasi:** Laksanakan dasar untuk mengehadkan bilangan permintaan yang boleh dibuat oleh ejen AI kepada perkhidmatan. Mengehadkan bilangan giliran perbualan dan permintaan kepada ejen AI anda adalah cara lain untuk mencegah serangan jenis ini.

### Keracunan Pangkalan Pengetahuan

**Penerangan:** Serangan jenis ini tidak menyasarkan ejen AI secara langsung tetapi menyasarkan pangkalan pengetahuan dan perkhidmatan lain yang akan digunakan oleh ejen AI. Ini boleh melibatkan merosakkan data atau maklumat yang akan digunakan oleh ejen AI untuk menyelesaikan tugas, yang membawa kepada respons yang berat sebelah atau tidak diingini kepada pengguna.

**Mitigasi:** Lakukan pengesahan secara berkala terhadap data yang akan digunakan oleh ejen AI dalam aliran kerjanya. Pastikan akses kepada data ini selamat dan hanya diubah oleh individu yang dipercayai untuk mengelakkan serangan jenis ini.

### Ralat Berantai

**Penerangan:** Ejen AI mengakses pelbagai alat dan perkhidmatan untuk menyelesaikan tugas. Ralat yang disebabkan oleh penyerang boleh menyebabkan kegagalan sistem lain yang dihubungkan dengan ejen AI, menyebabkan serangan menjadi lebih meluas dan sukar untuk diselesaikan.

**Mitigasi**: Satu kaedah untuk mengelakkan ini adalah dengan membenarkan Ejen AI beroperasi dalam persekitaran yang terhad, seperti melaksanakan tugas dalam bekas Docker, untuk mencegah serangan sistem langsung. Mencipta mekanisme sandaran dan logik cubaan semula apabila sistem tertentu memberikan respons ralat adalah cara lain untuk mencegah kegagalan sistem yang lebih besar.

## Manusia dalam Gelung (Human-in-the-Loop)

Satu lagi cara yang berkesan untuk membina sistem Ejen AI yang boleh dipercayai adalah dengan menggunakan pendekatan Manusia dalam Gelung. Ini mencipta aliran di mana pengguna dapat memberikan maklum balas kepada Ejen semasa proses berjalan. Pengguna pada dasarnya bertindak sebagai ejen dalam sistem berbilang ejen dengan memberikan kelulusan atau penamatan proses yang sedang berjalan.

![Human in The Loop](../../../translated_images/human-in-the-loop.5f0068a678f62f4fc8373d5b78c4c22f35d9e4da35c93f66c3b634c1774eff34.ms.png)

Berikut adalah petikan kod menggunakan AutoGen untuk menunjukkan bagaimana konsep ini dilaksanakan:

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

Membina ejen AI yang boleh dipercayai memerlukan reka bentuk yang teliti, langkah keselamatan yang kukuh, dan iterasi berterusan. Dengan melaksanakan sistem meta arahan yang berstruktur, memahami ancaman yang berpotensi, dan menerapkan strategi mitigasi, pembangun dapat mencipta ejen AI yang selamat dan berkesan. Selain itu, menggabungkan pendekatan manusia dalam gelung memastikan bahawa ejen AI tetap selaras dengan keperluan pengguna sambil meminimumkan risiko. Apabila AI terus berkembang, mengekalkan sikap proaktif terhadap keselamatan, privasi, dan pertimbangan etika akan menjadi kunci untuk memupuk kepercayaan dan kebolehpercayaan dalam sistem yang dipacu AI.

### Ada Lagi Soalan tentang Membina Ejen AI yang Boleh Dipercayai?

Sertai [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) untuk bertemu dengan pelajar lain, menghadiri waktu pejabat, dan mendapatkan jawapan kepada soalan anda tentang Ejen AI.

## Sumber Tambahan

- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">Gambaran keseluruhan AI yang bertanggungjawab</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Penilaian model AI generatif dan aplikasi AI</a>
- <a href="https://learn.microsoft.com/azure/ai-services/openai/concepts/system-message?context=%2Fazure%2Fai-studio%2Fcontext%2Fcontext&tabs=top-techniques" target="_blank">Mesej sistem keselamatan</a>
- <a href="https://blogs.microsoft.com/wp-content/uploads/prod/sites/5/2022/06/Microsoft-RAI-Impact-Assessment-Template.pdf?culture=en-us&country=us" target="_blank">Templat Penilaian Risiko</a>

## Pelajaran Sebelumnya

[Agentic RAG](../05-agentic-rag/README.md)

## Pelajaran Seterusnya

[Perancangan Corak Reka Bentuk](../07-planning-design/README.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.