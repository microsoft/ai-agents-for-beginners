[![Intro to AI Agents](../../../translated_images/id/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klik gambar di atas untuk menonton video pelajaran ini)_

# Pengenalan ke AI Agents dan Kasus Penggunaan Agen

Selamat datang di kursus **AI Agents untuk Pemula**! Kursus ini memberikan Anda pengetahuan dasar — dan kode kerja nyata — untuk mulai membangun AI Agents dari awal.

Mari sapa di <a href="https://discord.gg/kzRShWzttr" target="_blank">Komunitas Discord Azure AI</a> — penuh dengan pelajar dan pembangun AI yang senang menjawab pertanyaan.

Sebelum kita mulai membangun, mari pastikan kita benar-benar mengerti apa itu AI Agent dan kapan masuk akal untuk menggunakannya.

---

## Pengenalan

Pelajaran ini mencakup:

- Apa itu AI Agents, dan berbagai jenis yang ada
- Jenis-jenis tugas yang paling cocok untuk AI Agents
- Komponen inti yang akan Anda gunakan saat merancang solusi Agentic

## Tujuan Pembelajaran

Di akhir pelajaran ini, Anda harus dapat:

- Menjelaskan apa itu AI Agent dan bagaimana bedanya dengan solusi AI biasa
- Mengetahui kapan harus menggunakan AI Agent (dan kapan tidak)
- Membuat sketsa desain solusi Agentic dasar untuk masalah dunia nyata

---

## Mendefinisikan AI Agents dan Jenis AI Agents

### Apa itu AI Agents?

Ini cara sederhana untuk memikirkannya:

> **AI Agents adalah sistem yang memungkinkan Large Language Models (LLM) benar-benar *melakukan sesuatu* — dengan memberi mereka alat dan pengetahuan untuk bertindak di dunia, bukan hanya merespons prompt.**

Mari uraikan sedikit:

- **Sistem** — AI Agent bukan hanya satu hal. Ini kumpulan bagian yang bekerja bersama. Di inti, setiap agen memiliki tiga bagian:
  - **Lingkungan** — Ruang tempat agen bekerja. Untuk agen pemesanan perjalanan, ini adalah platform pemesanan itu sendiri.
  - **Sensor** — Bagaimana agen membaca keadaan lingkungan saat ini. Agen perjalanan kita mungkin memeriksa ketersediaan hotel atau harga penerbangan.
  - **Aktuator** — Bagaimana agen mengambil tindakan. Agen perjalanan bisa memesan kamar, mengirim konfirmasi, atau membatalkan reservasi.

![Apa Itu AI Agents?](../../../translated_images/id/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Large Language Models** — Agen sudah ada sebelum LLM, tapi LLM-lah yang membuat agen modern sangat kuat. Mereka dapat memahami bahasa alami, menalar konteks, dan mengubah permintaan pengguna yang samar menjadi rencana tindakan konkret.

- **Melakukan Tindakan** — Tanpa sistem agen, LLM hanya menghasilkan teks. Dalam sistem agen, LLM bisa benar-benar *menjalankan* langkah-langkah — mencari di database, memanggil API, mengirim pesan.

- **Akses ke Alat** — Alat apa yang bisa digunakan agen tergantung pada (1) lingkungan tempat ia dijalankan dan (2) apa yang dipilih pengembang untuk diberikan. Agen perjalanan mungkin bisa mencari penerbangan tapi tidak mengedit catatan pelanggan — semuanya tergantung bagaimana Anda menghubungkannya.

- **Memori + Pengetahuan** — Agen bisa punya memori jangka pendek (percakapan saat ini) dan memori jangka panjang (database pelanggan, interaksi sebelumnya). Agen perjalanan bisa "mengingat" Anda lebih suka kursi di dekat jendela.

---

### Jenis-jenis AI Agents

Tidak semua agen dibuat sama. Berikut ini adalah rincian jenis utama, menggunakan agen pemesanan perjalanan sebagai contoh:

| **Jenis Agen** | **Apa yang Dilakukan** | **Contoh Agen Perjalanan** |
|---|---|---|
| **Simple Reflex Agents** | Mengikuti aturan keras— tanpa memori, tanpa perencanaan. | Melihat email keluhan → meneruskannya ke layanan pelanggan. Itu saja. |
| **Model-Based Reflex Agents** | Memiliki model internal dunia dan memperbaruinya saat ada perubahan. | Melacak harga penerbangan historis dan menandai jalur yang tiba-tiba mahal. |
| **Goal-Based Agents** | Memiliki tujuan dan mencari cara mencapainya langkah demi langkah. | Memesan perjalanan lengkap (penerbangan, mobil, hotel) dari posisi Anda sekarang hingga tujuan Anda. |
| **Utility-Based Agents** | Tidak hanya menemukan *sebuah* solusi — mencari yang *terbaik* dengan mempertimbangkan trade-off. | Menyeimbangkan biaya vs. kenyamanan untuk menemukan perjalanan yang terbaik sesuai preferensi Anda. |
| **Learning Agents** | Menjadi lebih baik seiring waktu dengan belajar dari umpan balik. | Menyesuaikan rekomendasi pemesanan di masa depan berdasarkan hasil survei setelah perjalanan. |
| **Hierarchical Agents** | Agen tingkat tinggi memecah pekerjaan menjadi subtugas dan mendelegasikan ke agen tingkat rendah. | Permintaan "batalkan perjalanan" dipecah menjadi: batalkan penerbangan, batalkan hotel, batalkan sewa mobil — masing-masing ditangani oleh sub-agen. |
| **Multi-Agent Systems (MAS)** | Beberapa agen independen bekerja sama (atau bersaing). | Kooperatif: agen terpisah mengelola hotel, penerbangan, dan hiburan. Kompetitif: beberapa agen bersaing untuk mengisi kamar hotel dengan harga terbaik. |

---

## Kapan Menggunakan AI Agents

Hanya karena Anda *bisa* menggunakan AI Agent bukan berarti Anda *selalu harus* menggunakannya. Berikut situasi dimana agen sangat berguna:

![Kapan menggunakan AI Agents?](../../../translated_images/id/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Masalah Terbuka** — Ketika langkah untuk menyelesaikan masalah tidak bisa diprogram sebelumnya. Anda perlu agar LLM menemukan jalur secara dinamis.
- **Proses Multi-Langkah** — Tugas yang perlu menggunakan alat di beberapa langkah, bukan hanya lookup atau generasi tunggal.
- **Perbaikan Seiring Waktu** — Saat Anda ingin sistem menjadi lebih pintar berdasarkan umpan balik pengguna atau sinyal lingkungan.

Kita akan membahas lebih dalam kapan (dan kapan *tidak*) menggunakan AI Agents di pelajaran **Membangun AI Agents yang Dapat Dipercaya** nanti di kursus ini.

---

## Dasar-dasar Solusi Agentic

### Pengembangan Agen

Hal pertama yang Anda lakukan saat membangun agen adalah mendefinisikan *apa yang bisa dilakukan* — alat, aksi, dan perilakunya.

Dalam kursus ini, kami menggunakan **Azure AI Agent Service** sebagai platform utama. Layanan ini mendukung:

- Model terbuka seperti OpenAI, Mistral, dan Llama
- Data berlisensi dari penyedia seperti Tripadvisor
- Definisi alat OpenAPI 3.0 yang standar

### Pola Agentic

Anda berkomunikasi dengan LLM melalui prompt. Dengan agen, Anda tidak selalu dapat membuat setiap prompt secara manual — agen perlu mengambil tindakan dalam banyak langkah. Di sinilah **Pola Agentic** berguna. Mereka adalah strategi yang dapat digunakan ulang untuk memberi prompt dan mengatur LLM dengan cara yang lebih skalabel dan dapat diandalkan.

Kursus ini disusun berdasarkan pola agentic yang paling umum dan berguna.

### Kerangka Agentic

Kerangka Agentic memberi pengembang templat, alat, dan infrastruktur yang siap pakai untuk membangun agen. Mereka memudahkan:

- Menghubungkan alat dan kapabilitas
- Memantau apa yang dilakukan agen (dan debugging saat terjadi kesalahan)
- Berkolaborasi antar banyak agen

Dalam kursus ini, kami fokus pada **Microsoft Agent Framework (MAF)** untuk membangun agen siap produksi.

---

## Contoh Kode

Siap melihatnya langsung? Berikut contoh kode untuk pelajaran ini:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Ada Pertanyaan?

Bergabunglah dengan [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) untuk terhubung dengan pelajar lain, menghadiri sesi tanya jawab, dan mendapatkan jawaban atas pertanyaan AI Agent Anda dari komunitas.

---

## Pelajaran Sebelumnya

[Pengaturan Kursus](../00-course-setup/README.md)

## Pelajaran Selanjutnya

[Mengeksplorasi Kerangka Agentic](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk keakuratan, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber otoritatif. Untuk informasi yang penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->