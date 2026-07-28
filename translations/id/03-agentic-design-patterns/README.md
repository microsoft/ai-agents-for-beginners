[![Bagaimana Merancang Agen AI yang Baik](../../../translated_images/id/lesson-3-thumbnail.1092dd7a8f1074a5.webp)](https://youtu.be/m9lM8qqoOEA?si=4KimounNKvArQQ0K)

> _(Klik gambar di atas untuk melihat video pelajaran ini)_
# Prinsip Desain Agen AI

## Pendahuluan

Ada banyak cara untuk memikirkan pembangunan Sistem Agen AI. Mengingat bahwa ambiguitas adalah fitur dan bukan kesalahan dalam desain Generative AI, terkadang sulit bagi insinyur untuk mengetahui dari mana harus memulai. Kami telah membuat serangkaian Prinsip Desain UX yang berfokus pada manusia untuk memungkinkan pengembang membangun sistem agen yang berpusat pada pelanggan guna memenuhi kebutuhan bisnis mereka. Prinsip desain ini bukanlah arsitektur yang bersifat preskriptif tetapi lebih merupakan titik awal bagi tim yang mendefinisikan dan membangun pengalaman agen.

Secara umum, agen harus:

- Memperluas dan meningkatkan kapasitas manusia (brainstorming, memecahkan masalah, otomatisasi, dll.)
- Mengisi kekurangan pengetahuan (membantu saya mempercepat pemahaman domain pengetahuan, penerjemahan, dll.)
- Memfasilitasi dan mendukung kolaborasi dengan cara yang kita sebagai individu preferensikan untuk bekerja dengan orang lain
- Membuat kita menjadi versi diri yang lebih baik (misalnya, pelatih hidup/penugas tugas, membantu kita belajar regulasi emosi dan keterampilan kesadaran, membangun ketahanan, dll.)

## Pelajaran Ini Akan Membahas

- Apa itu Prinsip Desain Agen
- Beberapa pedoman yang harus diikuti saat menerapkan prinsip desain ini
- Contoh penggunaan prinsip desain

## Tujuan Pembelajaran

Setelah menyelesaikan pelajaran ini, Anda akan mampu:

1. Menjelaskan apa itu Prinsip Desain Agen
2. Menjelaskan pedoman untuk menggunakan Prinsip Desain Agen
3. Memahami cara membangun agen menggunakan Prinsip Desain Agen

## Prinsip Desain Agen

![Prinsip Desain Agen](../../../translated_images/id/agentic-design-principles.1cfdf8b6d3cc73c2.webp)

### Agen (Ruang)

Ini adalah lingkungan di mana agen beroperasi. Prinsip-prinsip ini menginformasikan bagaimana kita merancang agen untuk berinteraksi di dunia fisik dan digital.

- **Menghubungkan, bukan meruntuhkan** – membantu menghubungkan orang dengan orang lain, acara, dan pengetahuan yang dapat ditindaklanjuti untuk memungkinkan kolaborasi dan hubungan.
- Agen membantu menghubungkan acara, pengetahuan, dan orang.
- Agen membawa orang lebih dekat bersama. Mereka tidak dirancang untuk menggantikan atau merendahkan orang.
- **Mudah diakses namun kadang tak terlihat** – agen sebagian besar beroperasi di latar belakang dan hanya memberi dorongan saat relevan dan tepat.
  - Agen mudah ditemukan dan diakses oleh pengguna yang berwenang di perangkat atau platform apa pun.
  - Agen mendukung input dan output multimodal (suara, suara, teks, dll.).
  - Agen dapat dengan mulus berpindah antara latar depan dan latar belakang; antara proaktif dan reaktif, tergantung pengindraan kebutuhan pengguna.
  - Agen bisa beroperasi dalam bentuk tak terlihat, namun jalur proses latar belakang dan kolaborasinya dengan Agen lain transparan dan dapat dikendalikan oleh pengguna.

### Agen (Waktu)

Ini adalah bagaimana agen beroperasi sepanjang waktu. Prinsip-prinsip ini menginformasikan bagaimana kita merancang agen yang berinteraksi melintasi masa lalu, sekarang, dan masa depan.

- **Masa Lalu**: Merefleksikan sejarah yang mencakup keadaan dan konteks.
  - Agen menyediakan hasil yang lebih relevan berdasarkan analisis data sejarah yang lebih kaya selain hanya acara, orang, atau keadaan.
  - Agen membuat hubungan dari acara masa lalu dan secara aktif merefleksikan memori untuk berinteraksi dengan situasi saat ini.
- **Sekarang**: Memberi dorongan lebih dari sekadar pemberitahuan.
  - Agen mewujudkan pendekatan komprehensif dalam berinteraksi dengan orang. Ketika suatu acara terjadi, Agen melampaui notifikasi statis atau formalitas statis lainnya. Agen dapat menyederhanakan alur atau secara dinamis menghasilkan petunjuk untuk mengarahkan perhatian pengguna pada saat yang tepat.
  - Agen menyampaikan informasi berdasarkan konteks lingkungan, perubahan sosial dan budaya, serta disesuaikan dengan tujuan pengguna.
  - Interaksi agen dapat bertahap, berkembang/meningkatkan kompleksitas untuk memberdayakan pengguna dalam jangka panjang.
- **Masa Depan**: Beradaptasi dan berkembang.
  - Agen beradaptasi pada berbagai perangkat, platform, dan modalitas.
  - Agen menyesuaikan diri dengan perilaku pengguna, kebutuhan aksesibilitas, dan dapat dikustomisasi secara bebas.
  - Agen dibentuk dan berkembang melalui interaksi pengguna yang terus-menerus.

### Agen (Inti)

Ini adalah elemen kunci dalam inti desain agen.

- **Terima ketidakpastian tetapi bangun kepercayaan**.
  - Tingkat ketidakpastian Agen tertentu diharapkan. Ketidakpastian adalah elemen kunci dalam desain agen.
  - Kepercayaan dan transparansi adalah lapisan dasar desain Agen.
  - Manusia mengendalikan kapan Agen aktif/mati dan status Agen selalu terlihat jelas.

## Pedoman untuk Menerapkan Prinsip Ini

Saat Anda menggunakan prinsip desain sebelumnya, gunakan pedoman berikut:

1. **Transparansi**: Beritahu pengguna bahwa AI terlibat, bagaimana cara kerjanya (termasuk tindakan masa lalu), dan bagaimana memberi umpan balik serta memodifikasi sistem.
2. **Kontrol**: Memungkinkan pengguna menyesuaikan, menentukan preferensi dan personalisasi, serta mengendalikan sistem dan atributnya (termasuk kemampuan untuk melupakan).
3. **Konsistensi**: Usahakan pengalaman multimodal yang konsisten di berbagai perangkat dan titik akhir. Gunakan elemen UI/UX yang familiar bila memungkinkan (misalnya, ikon mikrofon untuk interaksi suara) dan kurangi beban kognitif pelanggan sebanyak mungkin (misalnya, jawaban ringkas, bantuan visual, dan konten ‘Pelajari Lebih Lanjut’).

## Cara Merancang Agen Perjalanan menggunakan Prinsip dan Pedoman Ini

Bayangkan Anda merancang Agen Perjalanan, berikut cara Anda dapat memikirkan penggunaan Prinsip dan Pedoman Desain:

1. **Transparansi** – Beri tahu pengguna bahwa Agen Perjalanan adalah Agen yang didukung AI. Berikan beberapa instruksi dasar untuk memulai (misalnya, pesan "Halo", contoh perintah). Dokumentasikan dengan jelas di halaman produk. Tampilkan daftar permintaan yang telah diajukan pengguna sebelumnya. Jelaskan cara memberi umpan balik (jempol atas dan bawah, tombol Kirim Umpan Balik, dll.). Jelaskan jika Agen memiliki batasan penggunaan atau topik.
2. **Kontrol** – Pastikan jelas bagaimana pengguna dapat memodifikasi Agen setelah dibuat dengan hal-hal seperti Sistem Prompt. Izinkan pengguna memilih seberapa verbose Agen, gaya tulisannya, dan batasan topik pembicaraan Agen. Biarkan pengguna melihat dan menghapus file atau data terkait, perintah, dan percakapan sebelumnya.
3. **Konsistensi** – Pastikan ikon untuk Bagikan Perintah, tambahkan file atau foto dan tag seseorang atau sesuatu adalah standar dan mudah dikenali. Gunakan ikon penjepit kertas untuk menunjukkan unggah/berbagi file dengan Agen, dan ikon gambar untuk menunjukkan unggahan grafik.

## Kode Contoh

- Python: [Kerangka Agen](./code_samples/03-python-agent-framework.ipynb)
- .NET: [Kerangka Agen](./code_samples/03-dotnet-agent-framework.md)


## Punya Pertanyaan Lebih Lanjut tentang Pola Desain Agen AI?

Bergabunglah dengan [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) untuk bertemu dengan pelajar lain, menghadiri jam kantor, dan mendapatkan jawaban atas pertanyaan tentang Agen AI Anda.

## Sumber Daya Tambahan

- <a href="https://openai.com" target="_blank">Praktik untuk Mengatur Sistem AI Agen | OpenAI</a>
- <a href="https://microsoft.com" target="_blank">Proyek Toolkit HAX - Microsoft Research</a>
- <a href="https://responsibleaitoolbox.ai" target="_blank">Kotak Peralatan AI Bertanggung Jawab</a>

## Pelajaran Sebelumnya

[Menjelajahi Kerangka Agen](../02-explore-agentic-frameworks/README.md)

## Pelajaran Selanjutnya

[Pola Desain Penggunaan Alat](../04-tool-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->