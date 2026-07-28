[![Intro to AI Agents](../../../translated_images/id/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klik gambar di atas untuk menonton video pelajaran ini)_

# Pengantar kepada Agen AI dan Kasus Penggunaan Agen

Selamat datang di kursus **Agen AI untuk Pemula**! Kursus ini memberikan Anda pengetahuan dasar — dan kode kerja nyata — untuk mulai membangun Agen AI dari awal.

Datang dan sapa di <a href="https://discord.gg/kzRShWzttr" target="_blank">Komunitas Discord Azure AI</a> — yang penuh dengan pembelajar dan pembuat AI yang senang membantu menjawab pertanyaan.

Sebelum kita mulai membangun, mari pastikan kita benar-benar memahami apa itu Agen AI dan kapan masuk akal untuk menggunakannya.

---

## Pengantar

Pelajaran ini membahas:

- Apa itu Agen AI, dan jenis-jenis agen yang ada
- Jenis tugas apa yang paling cocok untuk Agen AI
- Komponen inti yang akan Anda gunakan saat merancang solusi Agenik

## Tujuan Pembelajaran

Pada akhir pelajaran ini, Anda harus dapat:

- Menjelaskan apa itu Agen AI dan bagaimana bedanya dari solusi AI biasa
- Mengetahui kapan harus menggunakan Agen AI (dan kapan tidak)
- Membuat sketsa desain solusi Agenik dasar untuk masalah dunia nyata

---

## Mendefinisikan Agen AI dan Jenis-jenis Agen AI

### Apa itu Agen AI?

Berikut adalah cara sederhana untuk memikirkannya:

> **Agen AI adalah sistem yang memungkinkan Large Language Models (LLM) benar-benar *melakukan sesuatu* — dengan memberikan mereka alat dan pengetahuan untuk bertindak di dunia, bukan hanya merespons perintah.**

Mari kita uraikan sedikit:

- **Sistem** — Agen AI bukan hanya satu hal. Ini adalah kumpulan bagian yang bekerja bersama. Pada intinya, setiap agen memiliki tiga bagian:
  - **Lingkungan** — Ruang tempat agen bekerja. Untuk agen pemesanan perjalanan, ini adalah platform pemesanan itu sendiri.
  - **Sensor** — Bagaimana agen membaca kondisi lingkungan saat ini. Agen perjalanan kita mungkin memeriksa ketersediaan hotel atau harga penerbangan.
  - **Aktuator** — Bagaimana agen mengambil tindakan. Agen perjalanan mungkin memesan kamar, mengirim konfirmasi, atau membatalkan reservasi.

![Apa Itu Agen AI?](../../../translated_images/id/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Large Language Models** — Agen sudah ada sebelum LLM, tapi LLM yang membuat agen modern sangat kuat. Mereka bisa memahami bahasa alami, berpikir tentang konteks, dan mengubah permintaan pengguna yang samar menjadi rencana tindakan konkret.

- **Melakukan Tindakan** — Tanpa sistem agen, LLM hanya menghasilkan teks. Dalam sistem agen, LLM benar-benar bisa *menjalankan* langkah-langkah — mencari di database, memanggil API, mengirim pesan.

- **Akses ke Alat** — Alat apa yang bisa digunakan agen tergantung pada (1) lingkungan tempat ia berjalan dan (2) apa yang diberikan pengembang. Agen perjalanan mungkin bisa mencari penerbangan tapi tidak mengedit data pelanggan — semuanya tergantung pada apa yang Anda sambungkan.

- **Memori + Pengetahuan** — Agen bisa memiliki memori jangka pendek (percakapan saat ini) dan memori jangka panjang (database pelanggan, interaksi sebelumnya). Agen perjalanan bisa "mengingat" bahwa Anda lebih suka tempat duduk di dekat jendela.

---

### Jenis-jenis Agen AI

Tidak semua agen dibuat sama. Berikut ini adalah rincian tipe utama, menggunakan agen pemesanan perjalanan sebagai contoh:

| **Jenis Agen** | **Apa yang Dilakukan** | **Contoh Agen Perjalanan** |
|---|---|---|
| **Simple Reflex Agents** | Mengikuti aturan yang sudah dikode — tanpa memori, tanpa perencanaan. | Melihat email keluhan → meneruskannya ke layanan pelanggan. Itu saja. |
| **Model-Based Reflex Agents** | Memiliki model internal dunia dan memperbaruinya saat terjadi perubahan. | Melacak harga penerbangan historis dan memberi tahu rute yang tiba-tiba mahal. |
| **Goal-Based Agents** | Memiliki tujuan dan mencari cara mencapainya langkah demi langkah. | Memesan perjalanan lengkap (penerbangan, mobil, hotel) mulai dari lokasi Anda saat ini ke tujuan. |
| **Utility-Based Agents** | Tidak hanya mencari *sebuah* solusi — tapi mencari *solusi terbaik* dengan mempertimbangkan kompromi. | Menyeimbangkan biaya vs. kenyamanan untuk menemukan perjalanan yang paling sesuai dengan preferensi Anda. |
| **Learning Agents** | Menjadi lebih baik dari waktu ke waktu dengan belajar dari umpan balik. | Menyesuaikan rekomendasi pemesanan di masa depan berdasarkan hasil survei setelah perjalanan. |
| **Hierarchical Agents** | Agen tingkat tinggi membagi pekerjaan menjadi subtugas dan mendelegasikan ke agen tingkat bawah. | Permintaan "batalkan perjalanan" dibagi menjadi: batalkan penerbangan, batalkan hotel, batalkan sewa mobil — masing-masing ditangani oleh sub-agen. |
| **Multi-Agent Systems (MAS)** | Beberapa agen independen bekerja bersama (atau bersaing). | Kooperatif: agen terpisah menangani hotel, penerbangan, dan hiburan. Kompetitif: beberapa agen bersaing mengisi kamar hotel dengan harga terbaik. |

---

## Kapan Menggunakan Agen AI

Hanya karena Anda *bisa* menggunakan Agen AI bukan berarti selalu *harus*. Berikut situasi di mana agen benar-benar unggul:

![Kapan Menggunakan Agen AI?](../../../translated_images/id/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Masalah Terbuka** — Ketika langkah-langkah untuk menyelesaikan masalah tidak bisa diprogram sebelumnya. Anda butuh LLM untuk menentukan jalur secara dinamis.
- **Proses Multi-Langkah** — Tugas yang memerlukan penggunaan alat dalam beberapa putaran, bukan hanya pencarian atau generasi tunggal.
- **Peningkatan Seiring Waktu** — Ketika Anda ingin sistem menjadi lebih pintar berdasarkan umpan balik pengguna atau sinyal lingkungan.

Kita akan membahas lebih dalam kapan (dan kapan *tidak*) menggunakan Agen AI dalam pelajaran **Membangun Agen AI yang Dapat Dipercaya** di kursus ini.

---

## Dasar-dasar Solusi Agenik

### Pengembangan Agen

Hal pertama yang Anda lakukan saat membangun agen adalah mendefinisikan *apa yang bisa dilakukannya* — alat, aksi, dan perilakunya.

Dalam kursus ini, kami menggunakan **Microsoft Foundry Agent Service** sebagai platform utama. Ini mendukung:

- Model dari penyedia seperti OpenAI, Mistral, dan Meta (Llama)
- Data berlisensi dari penyedia seperti Tripadvisor
- Definisi alat OpenAPI 3.0 yang distandarisasi

### Pola Agenik

Anda berkomunikasi dengan LLM lewat prompt. Dengan agen, Anda tidak selalu bisa membuat setiap prompt secara manual — agen perlu mengambil tindakan dalam banyak langkah. Di sinilah **Pola Agenik** berguna. Mereka adalah strategi yang dapat digunakan ulang untuk membuat prompt dan mengorkestrasi LLM secara lebih skalabel dan dapat diandalkan.

Kursus ini disusun berdasarkan pola agenik yang paling umum dan berguna.

### Kerangka Agenik

Kerangka Agenik memberikan pengembang template, alat, dan infrastruktur siap pakai untuk membangun agen. Mereka memudahkan untuk:

- Menghubungkan alat dan kapabilitas
- Mengamati apa yang dilakukan agen (dan melakukan debugging saat terjadi kesalahan)
- Bekerja sama antar banyak agen

Dalam kursus ini, kami fokus pada **Microsoft Agent Framework (MAF)** untuk membangun agen siap produksi.

---

## Contoh Kode

Siap melihatnya beraksi? Berikut adalah contoh kode untuk pelajaran ini:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Ada Pertanyaan?

Bergabunglah dengan [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) untuk terhubung dengan pembelajar lain, menghadiri jam kantor, dan mendapatkan jawaban untuk pertanyaan Agen AI Anda dari komunitas.


---

## Smoke-Testing Agen Ini (Opsional)

Setelah Anda belajar mendeploy agen di [Lesson 16](../16-deploying-scalable-agents/README.md), Anda dapat menambahkan pemeriksaan kesehatan cepat pasca-deploy untuk `TravelAgent` pelajaran ini dengan katalog siap pakai [`tests/lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json). Lihat [`tests/README.md`](../tests/README.md) untuk cara menjalankannya.

---

## Pelajaran Sebelumnya

[Penyiapan Kursus](../00-course-setup/README.md)

## Pelajaran Berikutnya

[Menjelajahi Kerangka Agenik](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->