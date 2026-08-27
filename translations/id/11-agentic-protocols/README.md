# Menggunakan Protokol Agenik (MCP, A2A dan NLWeb)

[![Protokol Agenik](../../../translated_images/id/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Klik gambar di atas untuk menonton video pelajaran ini)_

Seiring dengan meningkatnya penggunaan agen AI, semakin besar pula kebutuhan akan protokol yang memastikan standarisasi, keamanan, dan mendukung inovasi terbuka. Dalam pelajaran ini, kita akan membahas 3 protokol yang berupaya memenuhi kebutuhan ini - Model Context Protocol (MCP), Agent to Agent (A2A) dan Natural Language Web (NLWeb).

## Pendahuluan

Dalam pelajaran ini, kita akan membahas:

• Bagaimana **MCP** memungkinkan Agen AI mengakses alat dan data eksternal untuk menyelesaikan tugas pengguna.

• Bagaimana **A2A** memungkinkan komunikasi dan kolaborasi antar agen AI yang berbeda.

• Bagaimana **NLWeb** membawa antarmuka bahasa alami ke situs web mana pun yang memungkinkan Agen AI menemukan dan berinteraksi dengan konten.

## Tujuan Pembelajaran

• **Mengidentifikasi** tujuan inti dan manfaat MCP, A2A, dan NLWeb dalam konteks agen AI.

• **Menjelaskan** bagaimana masing-masing protokol memfasilitasi komunikasi dan interaksi antara LLM, alat, dan agen lainnya.

• **Mengenali** peran berbeda yang dimainkan setiap protokol dalam membangun sistem agenik yang kompleks.

## Model Context Protocol

**Model Context Protocol (MCP)** adalah standar terbuka yang menyediakan cara standar untuk aplikasi memberikan konteks dan alat ke LLM. Ini memungkinkan sebuah "adaptor universal" ke berbagai sumber data dan alat yang dapat dihubungkan oleh Agen AI secara konsisten.

Mari kita lihat komponen MCP, manfaatnya dibandingkan penggunaan API langsung, dan contoh bagaimana agen AI dapat menggunakan server MCP.

### Komponen Inti MCP

MCP beroperasi pada **arsitektur klien-server** dan komponen inti adalah:

• **Host** adalah aplikasi LLM (misalnya editor kode seperti VSCode) yang memulai koneksi ke Server MCP.

• **Klien** adalah komponen dalam aplikasi host yang memelihara koneksi satu-ke-satu dengan server.

• **Server** adalah program ringan yang mengekspose kemampuan tertentu.

Termasuk dalam protokol ada tiga primitif inti yang merupakan kemampuan Server MCP:

• **Alat**: Ini adalah tindakan atau fungsi terpisah yang dapat dipanggil agen AI untuk melakukan aksi. Misalnya, layanan cuaca mungkin mengekspose alat "dapatkan cuaca", atau server e-commerce mengekspose alat "beli produk". Server MCP mengiklankan nama, deskripsi, dan skema input/output dari tiap alat dalam daftar kemampuannya.

• **Sumber Daya**: Ini adalah data atau dokumen baca-saja yang dapat disediakan oleh server MCP, dan klien dapat mengambilnya sesuai kebutuhan. Contohnya termasuk isi file, catatan database, atau berkas log. Sumber daya bisa berupa teks (seperti kode atau JSON) atau biner (seperti gambar atau PDF).

• **Prompt**: Ini adalah template yang sudah ditentukan yang menyediakan saran prompt, memungkinkan alur kerja yang lebih kompleks.

### Manfaat MCP

MCP menawarkan keuntungan signifikan bagi Agen AI:

• **Penemuan Alat Dinamis**: Agen dapat secara dinamis menerima daftar alat yang tersedia dari server beserta deskripsi fungsinya. Ini berbeda dengan API tradisional yang sering membutuhkan pengkodean statis untuk integrasi, sehingga setiap perubahan API mengharuskan pembaruan kode. MCP menawarkan pendekatan "integrasi sekali", yang memberikan adaptabilitas lebih besar.

• **Interoperabilitas Antar LLM**: MCP bekerja lintas LLM yang berbeda, menyediakan fleksibilitas untuk mengganti model inti guna evaluasi performa yang lebih baik.

• **Keamanan Standar**: MCP menyertakan metode autentikasi standar, meningkatkan skalabilitas saat menambahkan akses ke server MCP tambahan. Ini lebih sederhana dibanding mengelola berbagai kunci dan jenis autentikasi untuk berbagai API tradisional.

### Contoh MCP

![Diagram MCP](../../../translated_images/id/mcp-diagram.e4ca1cbd551444a1.webp)

Bayangkan seorang pengguna ingin memesan penerbangan menggunakan asisten AI yang didukung oleh MCP.

1. **Koneksi**: Asisten AI (klien MCP) terhubung ke server MCP yang disediakan oleh maskapai penerbangan.

2. **Penemuan Alat**: Klien menanyakan ke server MCP maskapai, "Alat apa saja yang Anda miliki?" Server merespon dengan alat seperti "cari penerbangan" dan "pesan penerbangan".

3. **Pemanggilan Alat**: Anda kemudian meminta asisten AI, "Tolong cari penerbangan dari Portland ke Honolulu." Asisten AI, menggunakan LLM-nya, mengidentifikasi bahwa ia perlu memanggil alat "cari penerbangan" dan mengirimkan parameter relevan (asal, tujuan) ke server MCP.

4. **Eksekusi dan Respon**: Server MCP, bertindak sebagai pembungkus, melakukan panggilan sebenarnya ke API pemesanan internal maskapai. Lalu menerima informasi penerbangan (misalnya data JSON) dan mengirimkannya kembali ke asisten AI.

5. **Interaksi Lanjutan**: Asisten AI menampilkan pilihan penerbangan. Setelah Anda memilih penerbangan, asisten mungkin memanggil alat "pesan penerbangan" pada server MCP yang sama, menyelesaikan pemesanan.

## Protokol Agen-ke-Agen (A2A)

Sementara MCP fokus pada menghubungkan LLM ke alat, **Protokol Agen-ke-Agen (A2A)** melangkah lebih jauh dengan memungkinkan komunikasi dan kolaborasi antar agen AI yang berbeda. A2A menghubungkan agen AI di berbagai organisasi, lingkungan, dan tumpukan teknologi untuk menyelesaikan tugas bersama.

Kita akan memeriksa komponen dan manfaat A2A, beserta contoh penerapannya pada aplikasi perjalanan kita.

### Komponen Inti A2A

A2A fokus pada mengaktifkan komunikasi antara agen dan membuat mereka bekerja sama menyelesaikan subtugas pengguna. Setiap komponen protokol berkontribusi pada hal ini:

#### Kartu Agen

Mirip dengan bagaimana server MCP membagikan daftar alat, Kartu Agen memiliki:
- Nama Agen.
- **deskripsi tugas umum** yang diselesaikannya.
- **daftar keterampilan spesifik** dengan deskripsi untuk membantu agen lain (atau pengguna manusia) memahami kapan dan mengapa mereka ingin memanggil agen tersebut.
- **URL Endpoint saat ini** dari agen
- **versi** dan **kemampuan** agen seperti streaming respons dan notifikasi push.

#### Eksekutor Agen

Eksekutor Agen bertugas untuk **mengoper konteks percakapan pengguna ke agen remote**, agen remote memerlukan ini agar memahami tugas yang harus diselesaikan. Dalam server A2A, seorang agen menggunakan Large Language Model (LLM) miliknya untuk mengurai permintaan yang masuk dan mengeksekusi tugas menggunakan alat internalnya.

#### Artefak

Setelah agen remote menyelesaikan tugas yang diminta, hasil kerjanya dibuat sebagai artefak. Artefak **mengandung hasil kerja agen**, **deskripsi tentang apa yang diselesaikan**, dan **konteks teks** yang dikirimkan melalui protokol. Setelah artefak dikirim, koneksi dengan agen remote ditutup sampai dibutuhkan lagi.

#### Antrian Event

Komponen ini digunakan untuk **menangani pembaruan dan mengirim pesan**. Ini sangat penting dalam produksi untuk sistem agenik agar mencegah koneksi antar agen ditutup sebelum tugas selesai, terutama saat waktu penyelesaian tugas bisa lama.

### Manfaat A2A

• **Kolaborasi yang Ditingkatkan**: Memungkinkan agen dari vendor dan platform berbeda untuk berinteraksi, berbagi konteks, dan bekerja sama, memfasilitasi otomatisasi lancar lintas sistem yang secara tradisional terpisah.

• **Fleksibilitas Pemilihan Model**: Setiap agen A2A bisa menentukan LLM mana yang digunakannya untuk melayani permintaan, memungkinkan model yang dioptimalkan atau khusus per agen, berbeda dengan koneksi LLM tunggal di beberapa skenario MCP.

• **Autentikasi Terintegrasi**: Autentikasi langsung terintegrasi ke dalam protokol A2A, menyediakan kerangka keamanan yang kuat untuk interaksi agen.

### Contoh A2A

![Diagram A2A](../../../translated_images/id/A2A-Diagram.8666928d648acc26.webp)

Mari kita perluas skenario pemesanan perjalanan kita, kali ini menggunakan A2A.

1. **Permintaan Pengguna ke Multi-Agen**: Seorang pengguna berinteraksi dengan agen/klien A2A "Agen Perjalanan", mungkin dengan mengatakan, "Tolong pesan seluruh perjalanan ke Honolulu untuk minggu depan, termasuk penerbangan, hotel, dan sewa mobil".

2. **Orkestrasi oleh Agen Perjalanan**: Agen Perjalanan menerima permintaan kompleks ini. Ia menggunakan LLM-nya untuk memikirkan tugas dan menentukan bahwa dia perlu berinteraksi dengan agen khusus lainnya.

3. **Komunikasi Antar Agen**: Agen Perjalanan kemudian menggunakan protokol A2A untuk terhubung ke agen hilir, seperti "Agen Maskapai", "Agen Hotel", dan "Agen Sewa Mobil" yang dibuat oleh perusahaan berbeda.

4. **Eksekusi Tugas yang Delegasi**: Agen Perjalanan mengirim tugas khusus ke agen khusus ini (misalnya, "Cari penerbangan ke Honolulu", "Pesan hotel", "Sewa mobil"). Masing-masing agen khusus ini, menjalankan LLM mereka sendiri dan menggunakan alat mereka sendiri (yang bisa berupa server MCP), melakukan bagian pemesanan mereka.

5. **Respon Terpadu**: Setelah semua agen hilir menyelesaikan tugasnya, Agen Perjalanan menyusun hasil (detail penerbangan, konfirmasi hotel, pemesanan sewa mobil) dan mengirimkan respon gaya chat yang komprehensif kembali ke pengguna.

## Natural Language Web (NLWeb)

Situs web telah lama menjadi cara utama bagi pengguna untuk mengakses informasi dan data di internet.

Mari kita lihat komponen berbeda dari NLWeb, manfaat NLWeb dan contoh bagaimana NLWeb bekerja dengan melihat aplikasi perjalanan kita.

### Komponen NLWeb

- **Aplikasi NLWeb (Kode Layanan Inti)**: Sistem yang memproses pertanyaan bahasa alami. Ia menghubungkan bagian berbeda dari platform untuk membuat jawaban. Anda bisa menganggapnya sebagai **mesin yang menggerakkan fitur bahasa alami** sebuah situs web.

- **Protokol NLWeb**: Ini adalah **set aturan dasar untuk interaksi bahasa alami** dengan situs web. Mengirimkan balik respon dalam format JSON (sering menggunakan Schema.org). Tujuannya membuat fondasi sederhana untuk "AI Web", sama seperti HTML memungkinkan berbagi dokumen secara online.

- **Server MCP (Titik Akhir Model Context Protocol)**: Setiap pengaturan NLWeb juga berfungsi sebagai **server MCP**. Ini berarti dapat **berbagi alat (seperti metode “ask”) dan data** dengan sistem AI lain. Dalam praktiknya, ini membuat konten dan kemampuan situs web dapat digunakan oleh agen AI, memungkinkan situs menjadi bagian dari “ekosistem agen” yang lebih luas.

- **Model Embedding**: Model ini digunakan untuk **mengubah konten situs web menjadi representasi angka yang disebut vektor** (embedding). Vektor ini menangkap makna dengan cara yang bisa dibandingkan dan dicari oleh komputer. Mereka disimpan dalam database khusus, dan pengguna dapat memilih model embedding yang ingin digunakan.

- **Database Vektor (Mekanisme Pengambilan)**: Database ini **menyimpan embedding konten situs web**. Ketika seseorang mengajukan pertanyaan, NLWeb memeriksa database vektor untuk dengan cepat menemukan informasi paling relevan. Ia memberikan daftar jawaban yang cepat, diurutkan berdasarkan kemiripan. NLWeb bekerja dengan berbagai sistem penyimpanan vektor seperti Qdrant, Snowflake, Milvus, Azure AI Search, dan Elasticsearch.

### NLWeb dengan Contoh

![NLWeb](../../../translated_images/id/nlweb-diagram.c1e2390b310e5fe4.webp)

Pertimbangkan situs pemesanan perjalanan kita lagi, tetapi kali ini, didukung oleh NLWeb.

1. **Pengambilan Data**: Katalog produk situs perjalanan yang ada (misalnya, daftar penerbangan, deskripsi hotel, paket tur) diformat menggunakan Schema.org atau dimuat melalui feed RSS. Alat NLWeb mengambil data terstruktur ini, membuat embedding, dan menyimpannya di database vektor lokal atau jarak jauh.

2. **Kueri Bahasa Alami (Manusia)**: Seorang pengguna mengunjungi situs dan, alih-alih menavigasi menu, mengetik di antarmuka chat: "Cari hotel ramah keluarga di Honolulu dengan kolam renang untuk minggu depan".

3. **Pemrosesan NLWeb**: Aplikasi NLWeb menerima kueri ini. Ia mengirim kueri ke LLM untuk pemahaman dan secara bersamaan mencari database vektor untuk daftar hotel yang relevan.

4. **Hasil Akurat**: LLM membantu menginterpretasi hasil pencarian dari database, mengidentifikasi kecocokan terbaik berdasarkan kriteria "ramah keluarga," "kolam renang," dan "Honolulu," lalu memformat respon bahasa alami. Yang penting, respon merujuk ke hotel aktual dari katalog situs, menghindari informasi yang dibuat-buat.

5. **Interaksi Agen AI**: Karena NLWeb berfungsi sebagai server MCP, agen perjalanan AI eksternal juga dapat terhubung ke instansi NLWeb situs ini. Agen AI kemudian bisa menggunakan metode `ask` MCP untuk mengajukan pertanyaan langsung ke situs: `ask("Apakah ada restoran ramah vegan di area Honolulu yang direkomendasikan oleh hotel?")`. Instansi NLWeb akan memproses ini, memanfaatkan database informasi restoran (jika dimuat), dan mengembalikan respon JSON terstruktur.

### Punya Pertanyaan Lebih Lanjut tentang MCP/A2A/NLWeb?

Bergabunglah dengan [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) untuk bertemu pelajar lain, menghadiri jam kantor, dan mendapatkan jawaban atas pertanyaan Agen AI Anda.

## Sumber Daya

- [MCP untuk Pemula](https://aka.ms/mcp-for-beginners)  
- [Dokumentasi MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Repo NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python)

## Pelajaran Sebelumnya

[Agen AI dalam Produksi](../10-ai-agents-production/README.md)

## Pelajaran Selanjutnya

[Rekayasa Konteks untuk Agen AI](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->