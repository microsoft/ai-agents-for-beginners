<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1e40fe956ff79462a02a17080b125041",
  "translation_date": "2025-08-29T17:59:10+00:00",
  "source_file": "01-intro-to-ai-agents/README.md",
  "language_code": "id"
}
-->
[![Intro to AI Agents](../../../translated_images/lesson-1-thumbnail.d21b2c34b32d35bbc7f1b4a40a81b031970b6076b4e0c59fb006cf818cac5d4a.id.png)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klik gambar di atas untuk menonton video pelajaran ini)_

# Pengantar AI Agents dan Penggunaan Kasus Agen

Selamat datang di kursus "AI Agents untuk Pemula"! Kursus ini memberikan pengetahuan dasar dan contoh penerapan untuk membangun AI Agents.

Bergabunglah dengan komunitas untuk bertemu dengan pelajar lain dan pembangun AI Agent, serta ajukan pertanyaan yang Anda miliki tentang kursus ini.

Untuk memulai kursus ini, kita akan memahami lebih dalam tentang apa itu AI Agents dan bagaimana kita dapat menggunakannya dalam aplikasi dan alur kerja yang kita bangun.

## Pengantar

Pelajaran ini mencakup:

- Apa itu AI Agents dan apa saja jenis-jenis agen yang ada?
- Kasus penggunaan apa yang paling cocok untuk AI Agents dan bagaimana mereka dapat membantu kita?
- Apa saja elemen dasar dalam merancang Solusi Agen?

## Tujuan Pembelajaran
Setelah menyelesaikan pelajaran ini, Anda seharusnya dapat:

- Memahami konsep AI Agent dan bagaimana mereka berbeda dari solusi AI lainnya.
- Menggunakan AI Agents secara efisien.
- Merancang solusi agen secara produktif untuk pengguna dan pelanggan.

## Definisi AI Agents dan Jenis-Jenis AI Agents

### Apa itu AI Agents?

AI Agents adalah **sistem** yang memungkinkan **Large Language Models (LLMs)** untuk **melakukan tindakan** dengan memperluas kemampuan mereka melalui akses ke **alat** dan **pengetahuan**.

Mari kita pecah definisi ini menjadi bagian-bagian kecil:

- **Sistem** - Penting untuk memikirkan agen bukan hanya sebagai satu komponen tunggal, tetapi sebagai sistem yang terdiri dari banyak komponen. Pada tingkat dasar, komponen AI Agent meliputi:
  - **Lingkungan** - Ruang yang didefinisikan di mana AI Agent beroperasi. Misalnya, jika kita memiliki AI Agent pemesanan perjalanan, lingkungan tersebut bisa berupa sistem pemesanan perjalanan yang digunakan AI Agent untuk menyelesaikan tugas.
  - **Sensor** - Lingkungan memiliki informasi dan memberikan umpan balik. AI Agents menggunakan sensor untuk mengumpulkan dan menafsirkan informasi tentang keadaan lingkungan saat ini. Dalam contoh Agen Pemesanan Perjalanan, sistem pemesanan perjalanan dapat memberikan informasi seperti ketersediaan hotel atau harga tiket pesawat.
  - **Aktuator** - Setelah AI Agent menerima keadaan lingkungan saat ini, untuk tugas yang sedang berlangsung, agen menentukan tindakan apa yang harus dilakukan untuk mengubah lingkungan. Dalam contoh agen pemesanan perjalanan, tindakan tersebut mungkin adalah memesan kamar yang tersedia untuk pengguna.

![Apa itu AI Agents?](../../../translated_images/what-are-ai-agents.1ec8c4d548af601a3a78c6c02e5c355d19c06a4a74fe93e3609a1d08e8c15689.id.png)

**Large Language Models** - Konsep agen sudah ada sebelum penciptaan LLMs. Keuntungan membangun AI Agents dengan LLMs adalah kemampuan mereka untuk menafsirkan bahasa manusia dan data. Kemampuan ini memungkinkan LLMs untuk menafsirkan informasi lingkungan dan mendefinisikan rencana untuk mengubah lingkungan.

**Melakukan Tindakan** - Di luar sistem AI Agent, LLMs terbatas pada situasi di mana tindakan yang dilakukan adalah menghasilkan konten atau informasi berdasarkan permintaan pengguna. Di dalam sistem AI Agent, LLMs dapat menyelesaikan tugas dengan menafsirkan permintaan pengguna dan menggunakan alat yang tersedia di lingkungan mereka.

**Akses ke Alat** - Alat yang dapat diakses oleh LLM ditentukan oleh 1) lingkungan tempat mereka beroperasi dan 2) pengembang AI Agent. Dalam contoh agen perjalanan, alat agen terbatas pada operasi yang tersedia dalam sistem pemesanan, dan/atau pengembang dapat membatasi akses alat agen ke penerbangan.

**Memori+Pengetahuan** - Memori dapat bersifat jangka pendek dalam konteks percakapan antara pengguna dan agen. Jangka panjang, di luar informasi yang diberikan oleh lingkungan, AI Agents juga dapat mengambil pengetahuan dari sistem, layanan, alat, dan bahkan agen lain. Dalam contoh agen perjalanan, pengetahuan ini bisa berupa informasi tentang preferensi perjalanan pengguna yang terdapat dalam basis data pelanggan.

### Jenis-Jenis Agen

Sekarang kita memiliki definisi umum tentang AI Agents, mari kita lihat beberapa jenis agen spesifik dan bagaimana mereka dapat diterapkan pada agen pemesanan perjalanan.

| **Jenis Agen**                | **Deskripsi**                                                                                                                       | **Contoh**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Simple Reflex Agents**      | Melakukan tindakan langsung berdasarkan aturan yang telah ditentukan sebelumnya.                                                      | Agen perjalanan menafsirkan konteks email dan meneruskan keluhan perjalanan ke layanan pelanggan.                                                                                                                          |
| **Model-Based Reflex Agents** | Melakukan tindakan berdasarkan model dunia dan perubahan pada model tersebut.                                                         | Agen perjalanan memprioritaskan rute dengan perubahan harga signifikan berdasarkan akses ke data harga historis.                                                                                                             |
| **Goal-Based Agents**         | Membuat rencana untuk mencapai tujuan tertentu dengan menafsirkan tujuan dan menentukan tindakan untuk mencapainya.                    | Agen perjalanan memesan perjalanan dengan menentukan pengaturan perjalanan yang diperlukan (mobil, transportasi umum, penerbangan) dari lokasi saat ini ke tujuan.                                                                                |
| **Utility-Based Agents**      | Mempertimbangkan preferensi dan menimbang trade-off secara numerik untuk menentukan cara mencapai tujuan.                              | Agen perjalanan memaksimalkan utilitas dengan menimbang kenyamanan vs. biaya saat memesan perjalanan.                                                                                                                                          |
| **Learning Agents**           | Meningkatkan kemampuan seiring waktu dengan merespons umpan balik dan menyesuaikan tindakan sesuai kebutuhan.                                                              | Agen perjalanan meningkatkan kemampuan dengan menggunakan umpan balik pelanggan dari survei pasca-perjalanan untuk membuat penyesuaian pada pemesanan di masa depan.                                                                                                               |
| **Hierarchical Agents**       | Menampilkan beberapa agen dalam sistem bertingkat, dengan agen tingkat atas membagi tugas menjadi subtugas untuk diselesaikan oleh agen tingkat bawah. | Agen perjalanan membatalkan perjalanan dengan membagi tugas menjadi subtugas (misalnya, membatalkan pemesanan tertentu) dan meminta agen tingkat bawah menyelesaikannya, lalu melaporkan kembali ke agen tingkat atas.                                     |
| **Multi-Agent Systems (MAS)** | Agen menyelesaikan tugas secara independen, baik secara kooperatif maupun kompetitif.                                                 | Kooperatif: Beberapa agen memesan layanan perjalanan tertentu seperti hotel, penerbangan, dan hiburan. Kompetitif: Beberapa agen mengelola dan bersaing atas kalender pemesanan hotel bersama untuk memesan pelanggan ke hotel. |

## Kapan Menggunakan AI Agents

Pada bagian sebelumnya, kita menggunakan kasus penggunaan Agen Perjalanan untuk menjelaskan bagaimana jenis-jenis agen yang berbeda dapat digunakan dalam berbagai skenario pemesanan perjalanan. Kita akan terus menggunakan aplikasi ini sepanjang kursus.

Mari kita lihat jenis-jenis kasus penggunaan yang paling cocok untuk AI Agents:

![Kapan menggunakan AI Agents?](../../../translated_images/when-to-use-ai-agents.54becb3bed74a479f5caca9c951132ce81d482a6704bcd22e5a600dbabc9434e.id.png)

- **Masalah Terbuka** - memungkinkan LLM untuk menentukan langkah-langkah yang diperlukan untuk menyelesaikan tugas karena tidak selalu dapat dihardcode ke dalam alur kerja.
- **Proses Multi-Langkah** - tugas yang membutuhkan tingkat kompleksitas di mana AI Agent perlu menggunakan alat atau informasi selama beberapa langkah, bukan hanya pengambilan satu kali.  
- **Peningkatan Seiring Waktu** - tugas di mana agen dapat meningkatkan kemampuan seiring waktu dengan menerima umpan balik dari lingkungan atau pengguna untuk memberikan utilitas yang lebih baik.

Kami akan membahas lebih banyak pertimbangan dalam menggunakan AI Agents pada pelajaran Membangun AI Agents yang Dapat Dipercaya.

## Dasar-Dasar Solusi Agen

### Pengembangan Agen

Langkah pertama dalam merancang sistem AI Agent adalah mendefinisikan alat, tindakan, dan perilaku. Dalam kursus ini, kami fokus pada penggunaan **Azure AI Agent Service** untuk mendefinisikan Agen kami. Layanan ini menawarkan fitur seperti:

- Pemilihan Model Terbuka seperti OpenAI, Mistral, dan Llama
- Penggunaan Data Berlisensi melalui penyedia seperti Tripadvisor
- Penggunaan alat OpenAPI 3.0 yang terstandarisasi

### Pola Agen

Komunikasi dengan LLM dilakukan melalui prompt. Mengingat sifat semi-otonom AI Agents, tidak selalu memungkinkan atau diperlukan untuk mem-prompt ulang LLM secara manual setelah ada perubahan di lingkungan. Kami menggunakan **Pola Agen** yang memungkinkan kami untuk mem-prompt LLM selama beberapa langkah dengan cara yang lebih skalabel.

Kursus ini dibagi menjadi beberapa pola agen populer saat ini.

### Kerangka Agen

Kerangka Agen memungkinkan pengembang untuk menerapkan pola agen melalui kode. Kerangka ini menawarkan template, plugin, dan alat untuk kolaborasi AI Agent yang lebih baik. Manfaat ini memberikan kemampuan untuk observabilitas dan pemecahan masalah sistem AI Agent yang lebih baik.

Dalam kursus ini, kami akan mengeksplorasi kerangka AutoGen yang berbasis penelitian dan kerangka Agent yang siap produksi dari Semantic Kernel.

### Punya Pertanyaan Lebih Lanjut tentang AI Agents?

Bergabunglah dengan [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) untuk bertemu dengan pelajar lain, menghadiri jam kantor, dan mendapatkan jawaban atas pertanyaan Anda tentang AI Agents.

## Pelajaran Sebelumnya

[Pengaturan Kursus](../00-course-setup/README.md)

## Pelajaran Selanjutnya

[Mengeksplorasi Kerangka Agen](../02-explore-agentic-frameworks/README.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.