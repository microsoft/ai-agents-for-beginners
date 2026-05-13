[![Intro to AI Agents](../../../translated_images/id/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klik gambar di atas untuk menonton video pelajaran ini)_

# Pengenalan Agen AI dan Kasus Penggunaan Agen

Selamat datang di kursus **Agen AI untuk Pemula**! Kursus ini memberikan Anda pengetahuan dasar — dan kode kerja nyata — untuk mulai membangun Agen AI dari nol.

Mari sapa di <a href="https://discord.gg/kzRShWzttr" target="_blank">Komunitas Discord Azure AI</a> — penuh dengan pembelajar dan pembangun AI yang senang menjawab pertanyaan.

Sebelum kita mulai membangun, mari pastikan kita benar-benar memahami apa itu Agen AI *dan* kapan masuk akal untuk menggunakannya.

---

## Pengenalan

Pelajaran ini mencakup:

- Apa itu Agen AI, dan berbagai jenis yang ada
- Jenis tugas apa yang paling cocok untuk Agen AI
- Blok bangunan inti yang akan Anda gunakan saat merancang solusi Agen

## Tujuan Pembelajaran

Pada akhir pelajaran ini, Anda seharusnya dapat:

- Menjelaskan apa itu Agen AI dan bagaimana bedanya dari solusi AI biasa
- Mengetahui kapan harus menggunakan Agen AI (dan kapan tidak)
- Membuat sketsa desain solusi Agen dasar untuk masalah dunia nyata

---

## Mendefinisikan Agen AI dan Jenis-Jenis Agen AI

### Apa itu Agen AI?

Berikut cara sederhana untuk memikirkannya:

> **Agen AI adalah sistem yang membiarkan Large Language Models (LLMs) *melakukan sesuatu* — dengan memberi mereka alat dan pengetahuan untuk bertindak di dunia, bukan hanya merespons perintah.**

Mari uraikan sedikit:

- **Sistem** — Agen AI bukan hanya satu hal. Ini adalah kumpulan bagian yang bekerja bersama. Pada intinya, setiap agen memiliki tiga bagian:
  - **Lingkungan** — Ruang tempat agen bekerja. Untuk agen pemesanan perjalanan, ini adalah platform pemesanan itu sendiri.
  - **Sensor** — Cara agen membaca kondisi lingkungan saat ini. Agen perjalanan kita mungkin memeriksa ketersediaan hotel atau harga penerbangan.
  - **Aktuator** — Cara agen mengambil tindakan. Agen perjalanan bisa memesan kamar, mengirim konfirmasi, atau membatalkan reservasi.

![What Are AI Agents?](../../../translated_images/id/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Large Language Models** — Agen sudah ada sebelum LLM, tapi LLMlah yang membuat agen modern sangat kuat. Mereka bisa memahami bahasa alami, memikirkan konteks, dan mengubah permintaan pengguna yang samar menjadi rencana tindakan yang konkret.

- **Melakukan Tindakan** — Tanpa sistem agen, LLM hanya menghasilkan teks. Dalam sistem agen, LLM benar-benar bisa *menjalankan* langkah-langkah — mencari database, memanggil API, mengirim pesan.

- **Akses ke Alat** — Alat apa yang bisa digunakan agen tergantung pada (1) lingkungan tempat ia berjalan dan (2) apa yang diberikan pengembang. Agen perjalanan mungkin bisa mencari penerbangan tapi tidak bisa mengedit data pelanggan — semuanya tergantung apa yang Anda sambungkan.

- **Memori + Pengetahuan** — Agen bisa punya memori jangka pendek (percakapan saat ini) dan memori jangka panjang (database pelanggan, interaksi sebelumnya). Agen perjalanan mungkin "mengingat" Anda lebih suka kursi jendela.

---

### Jenis-Jenis Agen AI

Tidak semua agen dibuat sama. Berikut rincian jenis utama, menggunakan agen pemesanan perjalanan sebagai contoh:

| **Jenis Agen** | **Apa yang Dilakukan** | **Contoh Agen Perjalanan** |
|---|---|---|
| **Agen Refleks Sederhana** | Mengikuti aturan yang sudah diprogram — tanpa memori, tanpa perencanaan. | Melihat email keluhan → meneruskannya ke layanan pelanggan. Itu saja. |
| **Agen Refleks Berbasis Model** | Memiliki model internal dunia dan memperbaruinya saat ada perubahan. | Melacak harga penerbangan historis dan memberi tanda rute yang tiba-tiba mahal. |
| **Agen Berbasis Tujuan** | Punya tujuan dan mencari cara mencapainya langkah demi langkah. | Memesan perjalanan lengkap (penerbangan, mobil, hotel) dari lokasi Anda sekarang ke tujuan. |
| **Agen Berbasis Utilitas** | Tidak hanya mencari *satu* solusi — tapi yang *terbaik* dengan menimbang kelebihan dan kekurangan. | Menyeimbangkan biaya vs. kenyamanan untuk menemukan perjalanan yang paling sesuai preferensi Anda. |
| **Agen Pembelajar** | Menjadi lebih baik seiring waktu dengan belajar dari umpan balik. | Menyesuaikan rekomendasi pemesanan berikutnya berdasarkan hasil survei pasca-perjalanan. |
| **Agen Hierarkis** | Agen tingkat tinggi membagi kerja menjadi subtugas dan mendelegasikan ke agen tingkat rendah. | Permintaan "batalkan perjalanan" dibagi menjadi: batalkan penerbangan, batalkan hotel, batalkan sewa mobil — masing-masing dikerjakan sub-agen. |
| **Sistem Multi-Agen (MAS)** | Beberapa agen independen bekerja sama (atau bersaing). | Kerjasama: agen terpisah mengelola hotel, penerbangan, dan hiburan. Kompetitif: agen bersaing mengisi kamar hotel dengan harga terbaik. |

---

## Kapan Menggunakan Agen AI

Hanya karena Anda *bisa* menggunakan Agen AI tidak berarti Anda harus selalu menggunakannya. Berikut situasi di mana agen sangat efektif:

![When to use AI Agents?](../../../translated_images/id/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Masalah Terbuka** — Ketika langkah untuk menyelesaikan masalah tidak bisa diprogram sebelumnya. Anda membutuhkan LLM untuk mencari jalannya secara dinamis.
- **Proses Multi-Langkah** — Tugas yang memerlukan penggunaan alat di beberapa tahap, tidak cuma sekali lihat atau buat.
- **Peningkatan Seiring Waktu** — Ketika Anda ingin sistem menjadi lebih pintar berdasarkan masukan pengguna atau sinyal lingkungan.

Kita akan mendalami kapan (dan kapan *tidak*) menggunakan Agen AI di pelajaran **Membangun Agen AI yang Dapat Dipercaya** nanti di kursus ini.

---

## Dasar-Dasar Solusi Agen

### Pengembangan Agen

Hal pertama yang dilakukan saat membangun agen adalah mendefinisikan *apa yang bisa dilakukannya* — alat, tindakan, dan perilakunya.

Di kursus ini, kita menggunakan **Azure AI Agent Service** sebagai platform utama. Ini mendukung:

- Model dari penyedia seperti OpenAI, Mistral, dan Meta (Llama)
- Data berlisensi dari penyedia seperti Tripadvisor
- Definisi alat standar OpenAPI 3.0

### Pola Agen

Anda berkomunikasi dengan LLM melalui prompt. Dengan agen, Anda tidak selalu bisa membuat tiap prompt secara manual — agen harus bertindak dalam banyak langkah. Di sinilah **Pola Agen** berperan. Ini adalah strategi yang bisa digunakan ulang untuk memanggil dan mengorkestrasi LLM dengan cara yang lebih skalabel dan andal.

Kursus ini disusun berdasarkan pola agen yang paling umum dan berguna.

### Kerangka Agen

Kerangka Agen memberikan pengembang template, alat, dan infrastruktur siap pakai untuk membangun agen. Ini memudahkan untuk:

- Menghubungkan alat dan kapabilitas
- Mengamati apa yang dilakukan agen (dan memperbaiki saat terjadi masalah)
- Bekerja sama antar banyak agen

Di kursus ini, kita fokus pada **Microsoft Agent Framework (MAF)** untuk membangun agen yang siap produksi.

---

## Contoh Kode

Siap melihatnya secara langsung? Berikut contoh kode untuk pelajaran ini:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Punya Pertanyaan?

Bergabunglah di [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) untuk terhubung dengan pembelajar lain, menghadiri sesi office hours, dan mendapatkan jawaban atas pertanyaan Agen AI Anda dari komunitas.

---

## Pelajaran Sebelumnya

[Course Setup](../00-course-setup/README.md)

## Pelajaran Berikutnya

[Exploring Agentic Frameworks](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->