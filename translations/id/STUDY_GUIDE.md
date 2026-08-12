# Agen AI untuk Pemula - Panduan Belajar

Gunakan panduan ini sebagai pendamping praktis saat Anda menjalani kursus. Ini
tidak dimaksudkan untuk menggantikan pelajaran. Ini membantu Anda memutuskan dari mana memulai, apa yang harus
dicari di setiap pelajaran, dan bagaimana menghubungkan ide-ide menjadi demo agen kecil yang berfungsi.


Jika ini pertama kalinya Anda di sini, mulailah dengan sederhana:

1. Baca [Pengaturan Kursus](./00-course-setup/README.md).
2. Selesaikan Pelajaran 01-06 secara berurutan.
3. Tetap pegang satu ide demo kecil saat Anda belajar.
4. Setelah setiap pelajaran, tanyakan: "Apa yang sekarang bisa dilakukan agen saya yang sebelumnya tidak bisa?"


## Demo Sederhana untuk Diingat

Cara yang baik untuk belajar agen adalah mengikuti satu ide demo sepanjang kursus.

Contoh demo: **agen pembantu kursus**.

Pengguna bertanya:

> "Saya ingin belajar bagaimana agen menggunakan alat. Temukan pelajaran yang tepat, ringkas apa yang
> harus saya baca terlebih dahulu, dan berikan saya tugas latihan singkat."

Chatbot biasa dapat menjawab dari apa yang sudah diketahuinya. Agen bisa melakukan lebih:

1. **Membaca atau mencari file kursus** untuk menemukan pelajaran yang tepat.
2. **Menggunakan alat** untuk mengambil tautan pelajaran, contoh, atau bahan pendukung.
3. **Merencanakan** jalur pembelajaran singkat daripada memberikan jawaban panjang.
4. **Menggunakan konteks** dari percakapan saat ini untuk tetap fokus pada tujuan pembelajar.
5. **Mengingat preferensi berguna** jika aplikasi mendukung memori.
6. **Menampilkan jejak, kutipan, atau log** agar pengguna dapat memahami apa yang terjadi.
7. **Menerapkan batasan** sebelum mengambil tindakan berisiko atau menggunakan data sensitif.


Saat Anda mempelajari setiap pelajaran, kembalilah ke demo ini dan tanyakan: kemampuan baru apa
yang akan ditambahkan pelajaran ini?

## Apa yang Anda Bangun

Pada akhir kursus, Anda harus bisa menjelaskan dan membangun sistem agen
yang menggabungkan bagian-bagian berikut:

| Bagian | Arti dalam bahasa sederhana | Dalam demo |
|------|------------------------|-------------|
| Model | Mesin penalaran yang mengartikan permintaan pengguna | Memahami bahwa pembelajar ingin pelajaran tentang penggunaan alat |
| Tools | Fungsi, API, file, browser, atau layanan yang dapat digunakan agen | Mencari di repo atau mengambil konten pelajaran |
| Knowledge | Dokumen atau data yang digunakan sebagai dasar jawaban | File README kursus dan bahan pelajaran |
| Context | Informasi yang disertakan dalam panggilan model berikutnya | Tujuan pengguna dan hasil alat |
| Memory | Informasi yang disimpan untuk penggunaan nanti | Pembelajar lebih suka contoh Python langsung |
| Planning | Memecah tujuan besar menjadi langkah kecil | Menemukan pelajaran, merangkum, menyarankan latihan |
| Orchestration | Mengarahkan kerja di antara alat, langkah, atau agen | Perencana memanggil alat pencarian, lalu peringkas |
| Trust | Keamanan, evaluasi, dan observabilitas | Mencatat panggilan alat dan bertanya sebelum tindakan berdampak tinggi |

## Model dan Penyedia

Contoh kode kursus menggunakan **Microsoft Agent Framework (MAF)** dan menargetkan **Azure OpenAI Responses API** — API yang direkomendasikan ke depan, yang menggabungkan chat completions, pemanggilan alat, input multimodal, dan percakapan berstatus dalam satu permukaan API. Anda terhubung baik melalui proyek **Microsoft Foundry** (dengan `FoundryChatClient`) atau langsung ke Azure OpenAI (dengan `OpenAIChatClient`).


Saat Anda mengerjakan pelajaran, Anda memiliki beberapa opsi penyedia:

- **Microsoft Foundry / Azure OpenAI (Responses API)** — jalur utama yang digunakan di seluruh pelajaran. Masuk dengan `az login` untuk autentikasi Entra ID tanpa kunci.
- **Foundry Local** — jalankan model sepenuhnya di perangkat melalui API kompatibel OpenAI (tanpa cloud, tanpa kunci API). Ideal untuk eksperimen offline atau tanpa biaya. Lihat [Course Setup](./00-course-setup/README.md).
- **MiniMax** — penyedia kompatibel OpenAI dengan model konteks besar, dapat digunakan sebagai alternatif pengganti.

> **Catatan:** GitHub Models sudah tidak digunakan lagi (akan dihentikan Juli 2026) dan tidak mendukung Responses API. Contoh telah diperbarui untuk menggunakan Azure OpenAI / Microsoft Foundry.

## Pilih Jalur Pembelajaran Anda

Anda dapat mengikuti seluruh kursus secara berurutan, atau lompat ke jalur berdasarkan apa yang ingin Anda
bangun.

| Jika tujuan Anda adalah... | Mulai dengan | Kemudian pelajari |
|-----------------------|------------|------------|
| Memahami apa itu agen | 01, 02, 03 | 04, 05, 06 |
| Membangun agen yang menggunakan alat | 04 | 05, 07, 14 |
| Membangun agen berbasis RAG | 05 | 04, 06, 12 |
| Mendesain alur kerja multi-langkah | 07 | 08, 09, 14 |
| Memahami sistem multi-agen | 08 | 07, 09, 11 |
| Mempersiapkan agen untuk produksi | 06, 10 | 12, 13, 16, 18 |
| Menyebarkan dan menskalakan agen di Foundry | 10, 16 | 06, 13, 18 |
| Membangun agen lokal / pertama offline | 17 | 04, 05, 11 |
| Menjelajahi protokol dan otomatisasi browser | 11, 15 | 10, 18 |

Tip: jika Anda baru dengan agen, jangan lewatkan Pelajaran 01-06. Mereka memberikan
kosa kata yang Anda perlukan untuk sisa kursus.

## Panduan Per Pelajaran

| Pelajaran | Apa yang Anda pelajari | Coba ini setelah pelajaran |
|--------|----------------|---------------------------|
| [01 - Intro to AI Agents](./01-intro-to-ai-agents/README.md) | Apa yang membuat agen berbeda dari chatbot dasar. | Jelaskan ide demo Anda sebagai agen, bukan hanya aplikasi obrolan. |
| [02 - Agentic Frameworks](./02-explore-agentic-frameworks/README.md) | Bagaimana framework membantu dengan model, alat, status, dan alur kerja. | Identifikasi bagian mana dari demo Anda yang akan dikelola oleh framework. |
| [03 - Agentic Design Patterns](./03-agentic-design-patterns/README.md) | Pola umum untuk merancang perilaku agen. | Rancang perjalanan pengguna sebelum menulis kode. |
| [04 - Tool Use](./04-tool-use/README.md) | Bagaimana agen memanggil alat untuk mendapatkan data atau mengambil tindakan. | Definisikan satu alat yang akan diperlukan agen demo Anda. |
| [05 - Agentic RAG](./05-agentic-rag/README.md) | Bagaimana retrieval mendasari jawaban agen pada dokumen atau data. | Putuskan sumber pengetahuan apa yang harus dicari demo Anda. |

| [06 - Agen Terpercaya](./06-building-trustworthy-agents/README.md) | Cara menambahkan pembatas, pengawasan, dan perilaku yang lebih aman. | Tambahkan satu aturan kapan agen harus menanyakan pengguna terlebih dahulu. |
| [07 - Desain Perencanaan](./07-planning-design/README.md) | Cara agen memecah tujuan besar menjadi langkah-langkah kecil. | Tulis rencana tiga langkah untuk permintaan demo Anda. |
| [08 - Desain Multi-Agen](./08-multi-agent/README.md) | Kapan membagi pekerjaan ke agen yang terspesialisasi. | Tentukan apakah demo Anda membutuhkan satu agen atau beberapa. |
| [09 - Metakognisi](./09-metacognition/README.md) | Bagaimana agen dapat meninjau dan memperbaiki output mereka sendiri. | Tambahkan pemeriksaan diri terakhir sebelum agen merespons. |
| [10 - Agen AI dalam Produksi](./10-ai-agents-production/README.md) | Apa yang berubah saat agen berpindah dari demo ke produksi. | Daftar apa yang akan Anda pantau: kualitas, biaya, latency, kegagalan. |
| [11 - Protokol Agentic](./11-agentic-protocols/README.md) | Bagaimana protokol menghubungkan agen ke alat dan agen lain. | Identifikasi di mana protokol standar dapat menyederhanakan integrasi. |
| [12 - Rekayasa Konteks](./12-context-engineering/README.md) | Cara memilih, memangkas, mengisolasi, dan mengelola konteks. | Tentukan apa yang perlu ada di prompt dan apa yang harus dikeluarkan. |
| [13 - Memori Agen](./13-agent-memory/README.md) | Bagaimana agen dapat menyimpan informasi berguna di berbagai interaksi. | Pilih satu preferensi aman yang demo Anda bisa ingat. |
| [14 - Microsoft Agent Framework](./14-microsoft-agent-framework/README.md) | Blok bangunan khusus framework untuk agen dan alur kerja, plus hosting agen LangChain/LangGraph di Microsoft Foundry. | Petakan langkah demo Anda ke konsep framework. |
| [15 - Agen Penggunaan Komputer](./15-browser-use/README.md) | Bagaimana agen dapat berinteraksi dengan browser atau antarmuka pengguna, termasuk contoh nyata seperti Microsoft Project Opal. | Pilih satu tugas browser yang masih harus memerlukan konfirmasi pengguna. |
| [16 - Menyebarkan Agen yang Skalabel](./16-deploying-scalable-agents/README.md) | Cara membawa agen dari prototipe ke penyebaran produksi yang skalabel dan dapat diamati di Microsoft Foundry (agen yang dihosting, pengalihan model, caching, gerbang evaluasi, tes asap). | Daftar kekhawatiran produksi yang demo Anda masih perlukan: hosting, pengalihan, biaya, evaluasi. |
| [17 - Membuat Agen AI Lokal](./17-creating-local-ai-agents/README.md) | Cara membangun agen lokal-pertama yang berjalan sepenuhnya di mesin Anda dengan Foundry Local dan Qwen (alat lokal, RAG lokal, MCP lokal). | Tentukan bagian mana dari demo Anda yang harus tetap privat dan berjalan secara lokal. |
| [18 - Mengamankan Agen AI](./18-securing-ai-agents/README.md) | Cara membuat tindakan agen lebih dapat diaudit dan sulit dimanipulasi. | Tentukan tindakan apa dalam demo Anda yang harus dicatat atau diberi tanda terima. |

## Memvalidasi Agen yang Disebarkan dengan Tes Asap

Ketika Anda menyebarkan agen (Pelajaran 16), **tes asap** adalah pemeriksaan pertama yang paling murah
untuk memastikan penyebaran benar-benar menjawab. Repositori ini menyediakan katalog siap pakai
di bawah [tests/](./tests/README.md) untuk agen yang dapat disebarkan di Pelajaran
01, 04, 05, dan 16, yang terhubung ke

[AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) GitHub
Action. Jalankan dari tab **Actions** setelah menerapkan agen pelajaran.
Smoke test adalah gerbang pertama — evaluasi offline dan online (Pelajaran 10 dan 16)
memberi tahu Anda seberapa *baik* agen tersebut.

## Ide Utama Dalam Istilah Ramah Pemula

### Alat

Sebuah alat adalah sesuatu yang dapat dipanggil oleh agen untuk melakukan pekerjaan di luar model. Alat yang baik
memiliki nama yang jelas, pekerjaan yang sempit, input bertipe, output yang dapat diprediksi, dan cara gagal yang aman.


Untuk demo pembantu kursus, alat mungkin:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG dan Pengetahuan

RAG membantu agen menjawab dari materi sumber daripada menebak. Dalam
kursus ini, materi sumber itu bisa berupa README pelajaran, contoh kode, atau sumber daya eksternal
yang terhubung dari pelajaran.

Gunakan RAG ketika jawaban harus didasarkan pada dokumen, data, atau file proyek saat ini.




cukup terlihat agar pengembang atau pengguna dapat memeriksa.


Untuk demo, rencana bisa berupa:

1. Temukan pelajaran yang terkait dengan penggunaan alat.
2. Ringkas pelajaran yang paling relevan.
3. Rekomendasikan satu tugas latihan.

### Konteks

Konteks adalah apa yang dilihat model saat ini. Konteks yang terlalu sedikit dapat membuat agen
melewatkan detail penting. Konteks yang terlalu banyak dapat membuat agen lebih lambat, lebih mahal,
atau lebih mudah bingung.

Rekayasa konteks yang baik berarti memilih informasi yang tepat untuk panggilan model berikutnya.




hanya ketika berguna, aman, dan mudah diperbarui atau dihapus.


Misalnya, mengingat "pelajar lebih suka contoh Python" mungkin berguna.
Mengingat data pribadi yang sensitif biasanya tidak.

### Evaluasi dan Observabilitas

Evaluasi bertanya: apakah agen melakukan hal yang benar?

Observabilitas bertanya: bisakah kita melihat bagaimana itu terjadi?

Untuk agen produksi, catat panggilan model, panggilan alat, konteks yang diambil,
latensi, biaya, kegagalan, dan umpan balik pengguna.

### Kepercayaan dan Keamanan

Agen yang dapat dipercaya membutuhkan lebih dari sekadar prompt yang membantu. Gunakan alat dengan hak istimewa paling rendah,
persetujuan manusia untuk tindakan berdampak tinggi, redaksi data jika diperlukan, dan log atau
tanda terima untuk tindakan yang harus diaudit.

## Rutinitas Tinjauan 15 Menit

Gunakan rutinitas ini setelah setiap pelajaran:

1. **Ringkas pelajaran dalam satu kalimat.**
2. **Sebutkan kemampuan agen baru.** Contoh: penggunaan alat, pengambilan,
   perencanaan, memori, observabilitas, atau keamanan.
3. **Tambahkan ke demo pembantu kursus.** Apa yang berubah di demo sekarang?
4. **Cari risikonya.** Apa yang bisa salah jika kemampuan ini disalahgunakan?
5. **Tulis satu pertanyaan uji.** Bagaimana Anda memeriksa bahwa agen berperilaku baik?

## Pemeriksaan Diri Cepat

Sebelum melanjutkan, coba jawab pertanyaan ini:

1. Apa yang dapat dilakukan agen yang tidak dapat dilakukan chatbot biasa sendiri?
2. Alat apa yang paling dibutuhkan agen Anda, dan kenapa?
3. Sumber pengetahuan apa yang harus mendasari jawaban agen?
4. Konteks apa yang harus dimasukkan dalam panggilan model berikutnya?

5. Apa yang harus diingat oleh agen, dan apa yang harus dihindari untuk disimpan?
6. Kapan agen harus meminta persetujuan manusia?
7. Log, jejak, atau tanda terima apa yang akan membantu Anda dalam men-debug atau mengaudit agen nanti?


## Latihan Capstone yang Disarankan

Di akhir kursus, buatlah agen kecil yang membantu pembelajar menavigasi
repositori ini.

Versi minimum:

- Menerima topik dari pengguna.
- Menemukan pelajaran yang paling relevan.
- Merangkum apa yang harus dibaca terlebih dahulu.
- Menyarankan satu tugas praktik langsung.
- Menampilkan file pelajaran atau tautan yang digunakan.

Versi lanjutan:

- Mengingat bahasa pemrograman favorit pembelajar.
- Menggunakan rencana sederhana sebelum menjawab.
- Menambahkan langkah pemeriksaan diri sebelum respons akhir.
- Mencatat pemanggilan alat dan sumber yang diperoleh.
- Meminta konfirmasi sebelum membuka browser atau tugas otomasi UI.

Ini memberi Anda cara kecil namun realistis untuk melatih alat, RAG, perencanaan,
konteks, memori, keterlihatan, dan kepercayaan dalam satu proyek.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->