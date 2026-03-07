[![Pengenalan Agen AI](../../../translated_images/id/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klik gambar di atas untuk menonton video pelajaran ini)_


# Pengenalan Agen AI dan Kasus Penggunaan Agen

Selamat datang di kursus "AI Agents for Beginners"! Kursus ini menyediakan pengetahuan dasar dan contoh terapan untuk membangun Agen AI.

Bergabunglah dengan <a href="https://discord.gg/kzRShWzttr" target="_blank">Komunitas Discord Azure AI</a> untuk bertemu pelajar lain dan Pembuat Agen AI serta mengajukan pertanyaan apa pun tentang kursus ini.

Untuk memulai kursus ini, kita mulai dengan memahami lebih baik apa itu Agen AI dan bagaimana kita dapat menggunakannya dalam aplikasi dan alur kerja yang kita bangun.

## Pengenalan

Pelajaran ini mencakup:

- Apa itu Agen AI dan apa saja tipe agen yang berbeda?
- Kasus penggunaan apa yang paling cocok untuk Agen AI dan bagaimana mereka dapat membantu kita?
- Apa saja blok bangunan dasar saat merancang Solusi Agentik?

## Tujuan Pembelajaran
Setelah menyelesaikan pelajaran ini, Anda seharusnya dapat:

- Memahami konsep Agen AI dan bagaimana mereka berbeda dari solusi AI lainnya.
- Menerapkan Agen AI secara paling efisien.
- Mendesain solusi agentik secara produktif untuk pengguna dan pelanggan.

## Mendefinisikan Agen AI dan Tipe Agen AI

### Apa itu Agen AI?

Agen AI adalah **sistem** yang memungkinkan **Model Bahasa Besar(LLMs)** untuk **melakukan tindakan** dengan memperluas kemampuan mereka dengan memberi LLM akses ke **alat** dan **pengetahuan**.

Mari kita pecah definisi ini menjadi bagian-bagian yang lebih kecil:

- **Sistem** - Penting untuk memikirkan agen bukan hanya sebagai satu komponen tetapi sebagai sistem dari banyak komponen. Pada tingkat dasar, komponen Agen AI adalah:
  - **Lingkungan** - Ruang terdefinisi tempat Agen AI beroperasi. Misalnya, jika kita memiliki Agen pemesanan perjalanan, lingkungan bisa berupa sistem pemesanan perjalanan yang digunakan Agen AI untuk menyelesaikan tugas.
  - **Sensor** - Lingkungan memiliki informasi dan memberikan umpan balik. Agen AI menggunakan sensor untuk mengumpulkan dan menafsirkan informasi ini tentang keadaan lingkungan saat ini. Dalam contoh Agen Pemesanan Perjalanan, sistem pemesanan dapat memberikan informasi seperti ketersediaan hotel atau harga penerbangan.
  - **Aktuator** - Setelah Agen AI menerima keadaan lingkungan saat ini, untuk tugas saat ini agen menentukan tindakan apa yang dilakukan untuk mengubah lingkungan. Untuk agen pemesanan perjalanan, mungkin tindakan tersebut adalah memesan kamar yang tersedia untuk pengguna.

![Apa Itu Agen AI?](../../../translated_images/id/what-are-ai-agents.1ec8c4d548af601a.webp)

**Model Bahasa Besar** - Konsep agen ada sebelum penciptaan LLM. Keuntungan membangun Agen AI dengan LLM adalah kemampuan mereka untuk menafsirkan bahasa manusia dan data. Kemampuan ini memungkinkan LLM menafsirkan informasi lingkungan dan menentukan rencana untuk mengubah lingkungan.

**Melakukan Tindakan** - Di luar sistem Agen AI, LLM terbatas pada situasi di mana tindakan adalah menghasilkan konten atau informasi berdasarkan prompt pengguna. Di dalam sistem Agen AI, LLM dapat menyelesaikan tugas dengan menafsirkan permintaan pengguna dan menggunakan alat yang tersedia di lingkungan mereka.

**Akses ke Alat** - Alat apa yang dapat diakses oleh LLM ditentukan oleh 1) lingkungan tempatnya beroperasi dan 2) pengembang Agen AI. Untuk contoh agen perjalanan kita, alat agen dibatasi oleh operasi yang tersedia di sistem pemesanan, dan/atau pengembang dapat membatasi akses alat agen ke penerbangan.

**Memori+Pengetahuan** - Memori bisa bersifat jangka pendek dalam konteks percakapan antara pengguna dan agen. Dalam jangka panjang, di luar informasi yang disediakan oleh lingkungan, Agen AI juga dapat mengambil pengetahuan dari sistem, layanan, alat, dan bahkan agen lain. Dalam contoh agen perjalanan, pengetahuan ini bisa berupa informasi preferensi perjalanan pengguna yang tersimpan di basis data pelanggan.

### Jenis-jenis agen

Sekarang kita memiliki definisi umum Agen AI, mari kita lihat beberapa tipe agen spesifik dan bagaimana mereka diterapkan pada agen pemesanan perjalanan.

| **Agent Type**                | **Description**                                                                                                                       | **Example**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Simple Reflex Agents**      | Perform immediate actions based on predefined rules.                                                                                  | Travel agent interprets the context of the email and forwards travel complaints to customer service.                                                                                                                          |
| **Model-Based Reflex Agents** | Perform actions based on a model of the world and changes to that model.                                                              | Travel agent prioritizes routes with significant price changes based on access to historical pricing data.                                                                                                             |
| **Goal-Based Agents**         | Create plans to achieve specific goals by interpreting the goal and determining actions to reach it.                                  | Travel agent books a journey by determining necessary travel arrangements (car, public transit, flights) from the current location to the destination.                                                                                |
| **Utility-Based Agents**      | Consider preferences and weigh tradeoffs numerically to determine how to achieve goals.                                               | Travel agent maximizes utility by weighing convenience vs. cost when booking travel.                                                                                                                                          |
| **Learning Agents**           | Improve over time by responding to feedback and adjusting actions accordingly.                                                        | Travel agent improves by using customer feedback from post-trip surveys to make adjustments to future bookings.                                                                                                               |
| **Hierarchical Agents**       | Feature multiple agents in a tiered system, with higher-level agents breaking tasks into subtasks for lower-level agents to complete. | Travel agent cancels a trip by dividing the task into subtasks (for example, canceling specific bookings) and having lower-level agents complete them, reporting back to the higher-level agent.                                     |
| **Multi-Agent Systems (MAS)** | Agents complete tasks independently, either cooperatively or competitively.                                                           | Cooperative: Multiple agents book specific travel services such as hotels, flights, and entertainment. Competitive: Multiple agents manage and compete over a shared hotel booking calendar to book customers into the hotel. |

## Kapan Menggunakan Agen AI

Di bagian sebelumnya, kami menggunakan kasus penggunaan Agen Perjalanan untuk menjelaskan bagaimana tipe agen yang berbeda dapat digunakan dalam skenario pemesanan perjalanan yang berbeda. Kami akan terus menggunakan aplikasi ini sepanjang kursus.

Mari lihat jenis kasus penggunaan yang paling cocok untuk Agen AI:

![Kapan Menggunakan Agen AI?](../../../translated_images/id/when-to-use-ai-agents.54becb3bed74a479.webp)


- **Masalah Terbuka (Open-Ended Problems)** - membiarkan LLM menentukan langkah yang dibutuhkan untuk menyelesaikan tugas karena ini tidak selalu dapat dikodekan secara kaku ke dalam alur kerja.
- **Proses Multi-Langkah** - tugas yang memerlukan tingkat kompleksitas di mana Agen AI perlu menggunakan alat atau informasi selama beberapa langkah alih-alih pengambilan sekali jalan.
- **Peningkatan Seiring Waktu** - tugas di mana agen dapat meningkat seiring waktu dengan menerima umpan balik dari lingkungan atau pengguna untuk memberikan utilitas yang lebih baik.

Kami membahas lebih banyak pertimbangan penggunaan Agen AI pada pelajaran Membangun Agen AI yang Dapat Dipercaya.

## Dasar-dasar Solusi Agentik

### Pengembangan Agen

Langkah pertama dalam merancang sistem Agen AI adalah mendefinisikan alat, tindakan, dan perilaku. Dalam kursus ini, kami fokus menggunakan **Azure AI Agent Service** untuk mendefinisikan Agen kami. Layanan ini menawarkan fitur seperti:

- Pemilihan Model Terbuka seperti OpenAI, Mistral, dan Llama
- Penggunaan Data Berlisensi melalui penyedia seperti Tripadvisor
- Penggunaan alat OpenAPI 3.0 yang distandarisasi

### Pola Agentik

Komunikasi dengan LLM dilakukan melalui prompt. Mengingat sifat semi-otonom Agen AI, tidak selalu mungkin atau diperlukan untuk memprompt ulang LLM secara manual setelah terjadi perubahan pada lingkungan. Kami menggunakan **Pola Agentik** yang memungkinkan kami memprompt LLM selama beberapa langkah dengan cara yang lebih dapat diskalakan.

Kursus ini dibagi menjadi beberapa pola Agentik populer saat ini.

### Kerangka Agentik

Kerangka Agentik memungkinkan pengembang mengimplementasikan pola agentik melalui kode. Kerangka ini menawarkan template, plugin, dan alat untuk kolaborasi Agen AI yang lebih baik. Manfaat ini memberikan kemampuan untuk observabilitas dan pemecahan masalah sistem Agen AI yang lebih baik.

Dalam kursus ini, kita akan mengeksplorasi Microsoft Agent Framework (MAF) untuk membangun agen AI yang siap produksi.

## Contoh Kode

- Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

## Punya Pertanyaan Lain tentang Agen AI?

Bergabunglah dengan [Discord Microsoft Foundry](https://aka.ms/ai-agents/discord) untuk bertemu pelajar lain, menghadiri jam konsultasi, dan mendapatkan jawaban atas pertanyaan Anda tentang Agen AI.

## Previous Lesson

[Pengaturan Kursus](../00-course-setup/README.md)

## Next Lesson

[Menjelajahi Kerangka Agentik](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Penafian:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI Co-op Translator (https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidaktepatan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan terjemahan profesional oleh penerjemah manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->