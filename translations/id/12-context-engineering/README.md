# Rekayasa Konteks untuk Agen AI

[![Context Engineering](../../../translated_images/id/lesson-12-thumbnail.ed19c94463e774d4.webp)](https://youtu.be/F5zqRV7gEag)

> _(Klik gambar di atas untuk menonton video pelajaran ini)_

Memahami kompleksitas aplikasi yang Anda bangun untuk agen AI sangat penting untuk membuat agen yang andal. Kita perlu membangun Agen AI yang secara efektif mengelola informasi untuk memenuhi kebutuhan kompleks yang melampaui rekayasa prompt.

Dalam pelajaran ini, kita akan melihat apa itu rekayasa konteks dan perannya dalam membangun agen AI.

## Pengantar

Pelajaran ini akan membahas:

• **Apa itu Rekayasa Konteks** dan mengapa itu berbeda dari rekayasa prompt.

• **Strategi untuk Rekayasa Konteks yang efektif**, termasuk cara menulis, memilih, mengompresi, dan mengisolasi informasi.

• **Kegagalan Konteks Umum** yang dapat menggagalkan agen AI Anda dan cara memperbaikinya.

## Tujuan Pembelajaran

Setelah menyelesaikan pelajaran ini, Anda akan memahami cara untuk:

• **Mendefinisikan rekayasa konteks** dan membedakannya dari rekayasa prompt.

• **Mengidentifikasi komponen kunci konteks** dalam aplikasi Model Bahasa Besar (LLM).

• **Menerapkan strategi untuk menulis, memilih, mengompresi, dan mengisolasi konteks** guna meningkatkan kinerja agen.

• **Mengenali kegagalan konteks umum** seperti kontaminasi, gangguan, kebingungan, dan benturan, serta menerapkan teknik mitigasinya.

## Apa Itu Rekayasa Konteks?

Untuk Agen AI, konteks adalah yang mendorong perencanaan Agen AI untuk mengambil tindakan tertentu. Rekayasa Konteks adalah praktik memastikan Agen AI memiliki informasi yang tepat untuk menyelesaikan langkah selanjutnya dari tugas. Jendela konteks memiliki batas ukuran, jadi sebagai pembangun agen kita perlu membangun sistem dan proses untuk mengelola penambahan, penghapusan, dan pemadatan informasi dalam jendela konteks.

### Rekayasa Prompt vs Rekayasa Konteks

Rekayasa prompt berfokus pada satu set instruksi statis untuk secara efektif membimbing Agen AI dengan serangkaian aturan. Rekayasa konteks adalah cara mengelola set informasi yang dinamis, termasuk prompt awal, untuk memastikan Agen AI memiliki apa yang dibutuhkannya seiring waktu. Ide utama dari rekayasa konteks adalah membuat proses ini dapat diulang dan andal.

### Jenis-Jenis Konteks

[![Types of Context](../../../translated_images/id/context-types.fc10b8927ee43f06.webp)](https://youtu.be/F5zqRV7gEag)

Penting untuk diingat bahwa konteks bukan hanya satu hal. Informasi yang dibutuhkan Agen AI dapat berasal dari berbagai sumber dan terserah pada kita untuk memastikan agen memiliki akses ke sumber-sumber ini:

Jenis konteks yang mungkin perlu dikelola oleh agen AI meliputi:

• **Instruksi:** Ini seperti "aturan" agen — prompt, pesan sistem, contoh few-shot (menunjukkan kepada AI cara melakukan sesuatu), dan deskripsi alat yang bisa digunakan. Inilah tempat fokus rekayasa prompt bergabung dengan rekayasa konteks.

• **Pengetahuan:** Ini mencakup fakta, informasi yang diambil dari basis data, atau memori jangka panjang yang telah dikumpulkan agen. Ini termasuk mengintegrasikan sistem Retrieval Augmented Generation (RAG) jika agen membutuhkan akses ke berbagai sumber pengetahuan dan basis data.

• **Alat:** Ini adalah definisi fungsi eksternal, API, dan Server MCP yang dapat dipanggil agen, bersama dengan umpan balik (hasil) yang diperoleh dari penggunaannya.

• **Riwayat Percakapan:** Dialog yang sedang berlangsung dengan pengguna. Seiring berjalannya waktu, percakapan ini menjadi lebih panjang dan kompleks yang berarti mereka mengambil ruang di jendela konteks.

• **Preferensi Pengguna:** Informasi yang dipelajari tentang kesukaan atau ketidaksukaan pengguna seiring waktu. Ini bisa disimpan dan dipanggil saat membuat keputusan penting untuk membantu pengguna.

## Strategi untuk Rekayasa Konteks yang Efektif

### Strategi Perencanaan

[![Context Engineering Best Practices](../../../translated_images/id/best-practices.f4170873dc554f58.webp)](https://youtu.be/F5zqRV7gEag)

Rekayasa konteks yang baik dimulai dengan perencanaan yang baik. Berikut adalah pendekatan yang akan membantu Anda mulai berpikir tentang cara menerapkan konsep rekayasa konteks:

1. **Tentukan Hasil yang Jelas** - Hasil dari tugas yang akan diberikan kepada Agen AI harus didefinisikan dengan jelas. Jawab pertanyaan - "Bagaimana dunia akan terlihat ketika Agen AI menyelesaikan tugasnya?" Dengan kata lain, perubahan, informasi, atau respons apa yang harus dimiliki pengguna setelah berinteraksi dengan Agen AI.
2. **Pemetaan Konteks** - Setelah Anda menentukan hasil Agen AI, Anda perlu menjawab pertanyaan "Informasi apa yang dibutuhkan Agen AI untuk menyelesaikan tugas ini?". Dengan cara ini Anda dapat mulai memetakan konteks dari mana informasi itu dapat ditemukan.
3. **Buat Pipeline Konteks** - Sekarang setelah Anda tahu di mana informasi itu, Anda perlu menjawab pertanyaan "Bagaimana Agen akan mendapatkan informasi ini?". Ini dapat dilakukan dengan berbagai cara termasuk RAG, penggunaan server MCP dan alat lainnya.

### Strategi Praktis

Perencanaan itu penting tetapi setelah informasi mulai mengalir ke jendela konteks agen kita, kita perlu memiliki strategi praktis untuk mengelolanya:

#### Mengelola Konteks

Sementara beberapa informasi akan ditambahkan ke jendela konteks secara otomatis, rekayasa konteks adalah tentang mengambil peran yang lebih aktif terhadap informasi ini yang dapat dilakukan dengan beberapa strategi:

 1. **Catatan Agen (Agent Scratchpad)**
 Ini memungkinkan Agen AI membuat catatan informasi relevan tentang tugas saat ini dan interaksi pengguna selama satu sesi. Ini harus berada di luar jendela konteks dalam sebuah file atau objek runtime yang dapat diambil kembali oleh agen selama sesi ini jika diperlukan.

 2. **Memori**
 Scratchpad bagus untuk mengelola informasi di luar jendela konteks satu sesi. Memori memungkinkan agen menyimpan dan mengambil kembali informasi relevan di berbagai sesi. Ini bisa mencakup ringkasan, preferensi pengguna, dan umpan balik untuk perbaikan di masa depan.

 3. **Mengompresi Konteks**
  Setelah jendela konteks tumbuh dan mendekati batasnya, teknik seperti meringkas dan memangkas dapat digunakan. Ini termasuk menyimpan hanya informasi yang paling relevan atau menghapus pesan lebih lama.
  
 4. **Sistem Multi-Agen**
  Mengembangkan sistem multi-agen adalah bentuk rekayasa konteks karena setiap agen memiliki jendela konteksnya sendiri. Bagaimana konteks itu dibagikan dan diteruskan ke agen yang berbeda adalah hal lain yang harus direncanakan ketika membangun sistem ini.
  
 5. **Lingkungan Sandbox**
  Jika agen perlu menjalankan beberapa kode atau memproses sejumlah besar informasi dalam dokumen, ini dapat memakan banyak token untuk memproses hasilnya. Alih-alih menyimpan semuanya dalam jendela konteks, agen dapat menggunakan lingkungan sandbox yang dapat menjalankan kode ini dan hanya membaca hasil serta informasi relevan lainnya.
  
 6. **Objek Status Runtime**
   Ini dilakukan dengan membuat kontainer informasi untuk mengelola situasi ketika Agen perlu memiliki akses ke informasi tertentu. Untuk tugas yang kompleks, ini akan memungkinkan Agen menyimpan hasil setiap sub-tugas langkah demi langkah, memungkinkan konteks tetap terhubung hanya ke sub-tugas tersebut.

#### Memeriksa Konteks

Setelah Anda menerapkan salah satu strategi ini, ada baiknya memeriksa apa yang sebenarnya diterima panggilan model berikutnya. Pertanyaan debugging yang berguna adalah:

> Apakah agen memuat terlalu banyak konteks, konteks yang salah, atau melewatkan konteks yang dibutuhkan?

Anda tidak perlu mencatat prompt mentah, output alat, atau isi memori untuk menjawab pertanyaan itu. Dalam produksi, lebih baik menggunakan catatan inspeksi konteks kecil yang menangkap jumlah, id, hash, dan label kebijakan:

- **Pemilihan:** Lacak berapa banyak potongan kandidat, alat, atau memori yang dipertimbangkan, berapa banyak yang dipilih, dan aturan atau skor mana yang menyebabkan lainnya difilter keluar.
- **Kompresi:** Catat rentang sumber atau id jejak, id ringkasan, perkiraan jumlah token sebelum dan sesudah kompresi, dan apakah konten mentah dikecualikan dari panggilan berikutnya.
- **Isolasi:** Catat sub-tugas mana yang dijalankan di agen, sesi, atau sandbox terpisah, ringkasan terbatas yang dikembalikan, dan apakah output alat besar tetap di luar konteks agen induk.
- **Memori dan RAG:** Simpan id dokumen pengambilan, id memori, skor, id terpilih, dan status penyuntingan alih-alih teks hasil lengkap yang diambil.
- **Keamanan dan privasi:** Lebih baik menggunakan hash, id, jumlah token, dan label kebijakan daripada teks prompt sensitif, argumen alat, hasil alat, atau isi memori pengguna.

Tujuannya bukan untuk menyimpan lebih banyak konteks. Melainkan meninggalkan cukup bukti sehingga pengembang dapat mengetahui strategi konteks mana yang dijalankan dan apakah itu mengubah panggilan model berikutnya dengan cara yang diinginkan.

### Contoh Rekayasa Konteks

Misalkan kita ingin agen AI **"Pesankan saya perjalanan ke Paris."**

• Agen sederhana yang hanya menggunakan rekayasa prompt mungkin hanya merespons: **"Baik, kapan Anda ingin pergi ke Paris?"**. Ia hanya memproses pertanyaan langsung Anda saat pengguna bertanya.

• Agen yang menggunakan strategi rekayasa konteks yang dibahas akan melakukan lebih banyak lagi. Sebelum merespons, sistemnya mungkin:

  ◦ **Periksa kalender Anda** untuk tanggal tersedia (mengambil data waktu nyata).

 ◦ **Ingat preferensi perjalanan masa lalu** (dari memori jangka panjang) seperti maskapai favorit, anggaran, atau apakah Anda lebih memilih penerbangan langsung.

 ◦ **Identifikasi alat yang tersedia** untuk pemesanan penerbangan dan hotel.

- Lalu, contoh respons bisa jadi: "Hai [Nama Anda]! Saya lihat Anda bebas minggu pertama Oktober. Apakah saya harus mencari penerbangan langsung ke Paris dengan [Maskapai Favorit] dalam anggaran biasa Anda [Anggaran]?" Respons yang lebih kaya dan sadar konteks ini menunjukkan kekuatan rekayasa konteks.

## Kegagalan Konteks Umum

### Kontaminasi Konteks

**Apa itu:** Ketika halusinasi (informasi palsu yang dihasilkan oleh LLM) atau kesalahan masuk ke dalam konteks dan sering dirujuk, menyebabkan agen mengejar tujuan yang mustahil atau mengembangkan strategi yang tidak masuk akal.

**Apa yang dilakukan:** Terapkan **validasi konteks** dan **karantina**. Validasi informasi sebelum ditambahkan ke memori jangka panjang. Jika terdeteksi potensi kontaminasi, mulai benang konteks baru untuk mencegah penyebaran informasi buruk.

**Contoh Pemesanan Perjalanan:** Agen Anda berhalusinasi sebuah **penerbangan langsung dari bandara lokal kecil ke kota internasional jauh** yang sebenarnya tidak menawarkan penerbangan internasional. Detail penerbangan yang tidak ada ini disimpan dalam konteks. Kemudian, saat Anda meminta agen untuk memesan, agen terus mencoba menemukan tiket untuk rute yang mustahil ini, menyebabkan kesalahan berulang.

**Solusi:** Terapkan langkah yang **memvalidasi keberadaan dan rute penerbangan dengan API waktu nyata** _sebelum_ menambahkan detail penerbangan ke konteks kerja agen. Jika validasi gagal, informasi salah itu "dikarantina" dan tidak digunakan lebih lanjut.

### Gangguan Konteks

**Apa itu:** Ketika konteks menjadi sangat besar sehingga model terlalu fokus pada riwayat yang terkumpul daripada menggunakan apa yang dipelajari selama pelatihan, yang mengakibatkan tindakan yang berulang atau tidak membantu. Model bisa mulai melakukan kesalahan bahkan sebelum jendela konteks penuh.

**Apa yang dilakukan:** Gunakan **ringkasan konteks**. Secara periodik kompres informasi yang terkumpul menjadi ringkasan yang lebih pendek, mempertahankan detail penting sambil menghapus riwayat yang berulang. Ini membantu "mengatur ulang" fokus.

**Contoh Pemesanan Perjalanan:** Anda telah membahas berbagai tujuan perjalanan impian untuk waktu yang lama, termasuk recounting rinci perjalanan backpacking Anda dua tahun lalu. Ketika Anda akhirnya meminta **"carikan saya penerbangan murah untuk bulan depan,"** agen terjebak dalam detail lama yang tidak relevan dan terus bertanya tentang perlengkapan backpacking atau itinerary masa lalu, mengabaikan permintaan Anda saat ini.

**Solusi:** Setelah sejumlah putaran tertentu atau ketika konteks tumbuh terlalu besar, agen harus **meringkas bagian percakapan yang paling baru dan relevan** – fokus pada tanggal dan tujuan perjalanan Anda saat ini – dan menggunakan ringkasan terkondensasi itu untuk panggilan LLM berikutnya, membuang riwayat chat yang kurang relevan.

### Kebingungan Konteks

**Apa itu:** Ketika konteks yang tidak perlu, sering dalam bentuk terlalu banyak alat yang tersedia, menyebabkan model menghasilkan respons buruk atau memanggil alat yang tidak relevan. Model yang lebih kecil sangat rentan terhadap ini.

**Apa yang dilakukan:** Terapkan **manajemen pemuatan alat** menggunakan teknik RAG. Simpan deskripsi alat dalam basis data vektor dan pilih _hanya_ alat yang paling relevan untuk setiap tugas spesifik. Penelitian menunjukkan membatasi pilihan alat kurang dari 30.

**Contoh Pemesanan Perjalanan:** Agen Anda memiliki akses ke puluhan alat: `book_flight`, `book_hotel`, `rent_car`, `find_tours`, `currency_converter`, `weather_forecast`, `restaurant_reservations`, dll. Anda bertanya, **"Bagaimana cara terbaik berkeliling Paris?"** Karena banyaknya alat, agen bingung dan mencoba memanggil `book_flight` _di dalam_ Paris, atau `rent_car` meskipun Anda lebih suka transportasi umum, karena deskripsi alat mungkin tumpang tindih atau agen tidak bisa membedakan yang terbaik.

**Solusi:** Gunakan **RAG terhadap deskripsi alat**. Saat Anda bertanya tentang berkeliling Paris, sistem secara dinamis mengambil _hanya_ alat yang paling relevan seperti `rent_car` atau `public_transport_info` berdasarkan permintaan Anda, menyajikan "loadout" alat yang terfokus ke LLM.

### Benturan Konteks

**Apa itu:** Ketika informasi yang bertentangan ada dalam konteks, menyebabkan penalaran yang tidak konsisten atau respons akhir yang buruk. Ini sering terjadi ketika informasi datang secara bertahap, dan asumsi awal yang salah tetap ada dalam konteks.

**Apa yang dilakukan:** Gunakan **pemangkasan konteks** dan **offloading**. Pemangkasan berarti menghapus informasi yang usang atau bertentangan saat detail baru datang. Offloading memberi model ruang kerja "scratchpad" terpisah untuk memproses informasi tanpa mengacaukan konteks utama.


**Contoh Pemesanan Perjalanan:** Awalnya Anda memberi tahu agen Anda, **"Saya ingin terbang kelas ekonomi."** Kemudian dalam percakapan, Anda berubah pikiran dan berkata, **"Sebenarnya, untuk perjalanan ini, mari kita pilih kelas bisnis."** Jika kedua instruksi tersebut tetap ada dalam konteks, agen mungkin menerima hasil pencarian yang bertentangan atau bingung preferensi mana yang harus diutamakan.

**Solusi:** Terapkan **pemangkasan konteks**. Ketika instruksi baru bertentangan dengan instruksi lama, instruksi yang lebih tua dihapus atau secara eksplisit digantikan dalam konteks. Sebagai alternatif, agen dapat menggunakan **scratchpad** untuk menyelaraskan preferensi yang bertentangan sebelum membuat keputusan, memastikan hanya instruksi akhir yang konsisten yang menjadi panduan tindakannya.

## Punya Pertanyaan Lebih Lanjut Tentang Rekayasa Konteks?

Bergabunglah dengan [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) untuk bertemu dengan pelajar lain, menghadiri jam kantor, dan mendapatkan jawaban untuk pertanyaan Agen AI Anda.
## Pelajaran Sebelumnya

[Agentic Protocols](../11-agentic-protocols/README.md)

## Pelajaran Berikutnya

[Memory for AI Agents](../13-agent-memory/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->