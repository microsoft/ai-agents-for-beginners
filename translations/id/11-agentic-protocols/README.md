# Menggunakan Protokol Agenik (MCP, A2A dan NLWeb)

[![Protokol Agenik](../../../translated_images/id/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Klik gambar di atas untuk menonton video pelajaran ini)_

Seiring bertumbuhnya penggunaan agen AI, kebutuhan akan protokol yang menjamin standardisasi, keamanan, dan mendukung inovasi terbuka juga meningkat. Dalam pelajaran ini, kita akan membahas 3 protokol yang berupaya memenuhi kebutuhan ini - Model Context Protocol (MCP), Agent to Agent (A2A) dan Natural Language Web (NLWeb).

## Pengantar

Dalam pelajaran ini, kita akan membahas:

• Bagaimana **MCP** memungkinkan Agen AI mengakses alat dan data eksternal untuk menyelesaikan tugas pengguna.

• Bagaimana **A2A** memungkinkan komunikasi dan kolaborasi antar agen AI yang berbeda.

• Bagaimana **NLWeb** menghadirkan antarmuka bahasa alami ke situs web mana pun sehingga Agen AI dapat menemukan dan berinteraksi dengan konten.

## Tujuan Pembelajaran

• **Mengidentifikasi** tujuan inti dan manfaat MCP, A2A, dan NLWeb dalam konteks agen AI.

• **Menjelaskan** bagaimana setiap protokol memfasilitasi komunikasi dan interaksi antara LLM, alat, dan agen lain.

• **Mengenali** peran berbeda yang dimainkan setiap protokol dalam membangun sistem agenik yang kompleks.

## Protokol Konteks Model

Protokol Konteks Model (MCP) adalah standar terbuka yang menyediakan cara yang distandarisasi bagi aplikasi untuk memberikan konteks dan alat ke LLM. Ini memungkinkan sebuah "penyesuai universal" ke berbagai sumber data dan alat yang dapat dihubungkan Agen AI secara konsisten.

Mari kita lihat komponen MCP, manfaat dibandingkan penggunaan API langsung, dan contoh bagaimana Agen AI mungkin menggunakan server MCP.

### Komponen Inti MCP

MCP beroperasi pada **arsitektur klien-server** dan komponen intinya adalah:

• **Hosts** adalah aplikasi LLM (misalnya editor kode seperti VSCode) yang memulai koneksi ke Server MCP.

• **Clients** adalah komponen dalam aplikasi host yang mempertahankan koneksi satu-ke-satu dengan server.

• **Servers** adalah program ringan yang mengekspos kemampuan tertentu.

Termasuk dalam protokol adalah tiga primitif inti yang merupakan kemampuan Server MCP:

• **Tools**: Ini adalah tindakan atau fungsi terpisah yang dapat dipanggil agen AI untuk melakukan suatu aksi. Misalnya, layanan cuaca mungkin mengekspos alat "get weather", atau server e-commerce mungkin mengekspos alat "purchase product". Server MCP mengumumkan nama setiap alat, deskripsi, dan skema input/output dalam daftar kapabilitas mereka.

• **Resources**: Ini adalah item data atau dokumen baca-saja yang dapat disediakan server MCP, dan klien dapat mengambilnya sesuai permintaan. Contohnya termasuk isi file, catatan basis data, atau file log. Resources dapat berupa teks (seperti kode atau JSON) atau biner (seperti gambar atau PDF).

• **Prompts**: Ini adalah templat yang telah ditentukan yang memberikan saran prompt, memungkinkan alur kerja yang lebih kompleks.

### Manfaat MCP

MCP menawarkan keuntungan signifikan bagi Agen AI:

• **Dynamic Tool Discovery**: Agen dapat secara dinamis menerima daftar alat yang tersedia dari server beserta deskripsi tentang apa yang mereka lakukan. Hal ini berbeda dengan API tradisional, yang sering membutuhkan pengkodean statis untuk integrasi, sehingga setiap perubahan API memerlukan pembaruan kode. MCP menawarkan pendekatan "integrate once", yang menghasilkan adaptabilitas lebih besar.

• **Interoperabilitas Antar LLM**: MCP bekerja lintas LLM yang berbeda, memberikan fleksibilitas untuk mengganti model inti guna dievaluasi demi kinerja yang lebih baik.

• **Keamanan Standar**: MCP mencakup metode otentikasi standar, meningkatkan skalabilitas saat menambahkan akses ke server MCP tambahan. Ini lebih sederhana daripada mengelola berbagai kunci dan jenis otentikasi untuk berbagai API tradisional.

### Contoh MCP

![Diagram MCP](../../../translated_images/id/mcp-diagram.e4ca1cbd551444a1.webp)

Bayangkan seorang pengguna ingin memesan penerbangan menggunakan asisten AI yang didukung oleh MCP.

1. **Koneksi**: Asisten AI (klien MCP) terhubung ke server MCP yang disediakan oleh maskapai penerbangan.

2. **Penemuan Alat**: Klien menanyakan kepada server MCP maskapai, "Alat apa yang Anda miliki?" Server merespons dengan alat seperti "search flights" dan "book flights".

3. **Pemanggilan Alat**: Anda lalu meminta asisten AI, "Tolong cari penerbangan dari Portland ke Honolulu." Asisten AI, menggunakan LLM-nya, mengidentifikasi bahwa perlu memanggil alat 'search flights' dan meneruskan parameter relevan (origin, destination) ke server MCP.

4. **Eksekusi dan Respons**: Server MCP, berperan sebagai pembungkus, melakukan panggilan aktual ke API pemesanan internal maskapai. Kemudian menerima informasi penerbangan (misalnya, data JSON) dan mengirimkannya kembali ke asisten AI.

5. **Interaksi Lanjutan**: Asisten AI menyajikan opsi penerbangan. Setelah Anda memilih penerbangan, asisten mungkin memanggil alat 'book flight' pada server MCP yang sama, menyelesaikan pemesanan.

## Protokol Agen-ke-Agen (A2A)

Sementara MCP berfokus pada menghubungkan LLM ke alat, protokol **Agent-to-Agent (A2A)** melangkah lebih jauh dengan memungkinkan komunikasi dan kolaborasi antara agen AI yang berbeda. A2A menghubungkan agen AI di berbagai organisasi, lingkungan, dan tumpukan teknologi untuk menyelesaikan tugas bersama.

Kita akan memeriksa komponen dan manfaat A2A, bersama dengan contoh bagaimana hal itu dapat diterapkan dalam aplikasi perjalanan kita.

### Komponen Inti A2A

A2A berfokus pada memungkinkan komunikasi antar agen dan membuat mereka bekerja bersama untuk menyelesaikan subtugas pengguna. Setiap komponen protokol berkontribusi terhadap hal ini:

#### Kartu Agen

Mirip dengan cara server MCP membagikan daftar alat, sebuah Kartu Agen memiliki:
- Nama Agen .
- Sebuah **deskripsi tentang tugas umum** yang diselesaikannya.
- Sebuah **daftar keterampilan spesifik** dengan deskripsi untuk membantu agen lain (atau bahkan pengguna manusia) memahami kapan dan mengapa mereka ingin memanggil agen tersebut.
- **URL Endpoint** saat ini agen
- **versi** dan **kapabilitas** agen seperti respon streaming dan notifikasi push.

#### Eksekutor Agen

Eksekutor Agen bertanggung jawab untuk **meneruskan konteks obrolan pengguna ke agen jarak jauh**, agen jarak jauh membutuhkan ini untuk memahami tugas yang harus diselesaikan. Di server A2A, sebuah agen menggunakan Large Language Model (LLM)-nya sendiri untuk mengurai permintaan yang masuk dan mengeksekusi tugas menggunakan alat internalnya sendiri.

#### Artefak

Setelah agen jarak jauh menyelesaikan tugas yang diminta, produk kerjanya dibuat sebagai artefak.  Sebuah artefak **mengandung hasil kerja agen**, sebuah **deskripsi tentang apa yang diselesaikan**, dan **konteks teks** yang dikirim melalui protokol. Setelah artefak dikirim, koneksi dengan agen jarak jauh ditutup sampai dibutuhkan lagi.

#### Antrian Peristiwa

Komponen ini digunakan untuk **menangani pembaruan dan meneruskan pesan**. Ini sangat penting dalam produksi untuk sistem agenik agar mencegah koneksi antar agen ditutup sebelum tugas selesai, terutama ketika waktu penyelesaian tugas dapat memakan waktu lebih lama.

### Manfaat A2A

• **Kolaborasi yang Ditingkatkan**: Memungkinkan agen dari vendor dan platform berbeda untuk berinteraksi, berbagi konteks, dan bekerja bersama, memfasilitasi otomatisasi mulus di seluruh sistem yang secara tradisional terpisah.

• **Fleksibilitas Pemilihan Model**: Setiap agen A2A dapat memutuskan LLM mana yang digunakannya untuk melayani permintaan, memungkinkan model yang dioptimalkan atau dilatih khusus per agen, berbeda dengan satu koneksi LLM dalam beberapa skenario MCP.

• **Otentikasi Bawaan**: Otentikasi terintegrasi langsung ke dalam protokol A2A, menyediakan kerangka keamanan yang kuat untuk interaksi agen.

### Contoh A2A

![Diagram A2A](../../../translated_images/id/A2A-Diagram.8666928d648acc26.webp)

Mari kita kembangkan skenario pemesanan perjalanan kita, tetapi kali ini menggunakan A2A.

1. **Permintaan Pengguna ke Multi-Agen**: Seorang pengguna berinteraksi dengan klien/agen A2A "Agen Perjalanan", mungkin dengan mengatakan, "Tolong pesan seluruh perjalanan ke Honolulu untuk minggu depan, termasuk penerbangan, hotel, dan mobil sewaan".

2. **Orkestrasi oleh Agen Perjalanan**: Agen Perjalanan menerima permintaan kompleks ini. Ia menggunakan LLM-nya untuk menalar tentang tugas dan menentukan bahwa ia perlu berinteraksi dengan agen khusus lainnya.

3. **Komunikasi Antar-Agen**: Agen Perjalanan kemudian menggunakan protokol A2A untuk terhubung ke agen hilir, seperti "Agen Maskapai", "Agen Hotel", dan "Agen Rental Mobil" yang dibuat oleh perusahaan berbeda.

4. **Pelaksanaan Tugas yang Didelegasikan**: Agen Perjalanan mengirim tugas spesifik ke agen khusus ini (misalnya, "Cari penerbangan ke Honolulu," "Pesan hotel," "Sewa mobil"). Masing-masing agen khusus ini, menjalankan LLM mereka sendiri dan memanfaatkan alat mereka sendiri (yang bisa saja berupa server MCP), melaksanakan bagian spesifik pemesanan.

5. **Respons Terkonsolidasi**: Setelah semua agen hilir menyelesaikan tugas mereka, Agen Perjalanan mengkompilasi hasilnya (detail penerbangan, konfirmasi hotel, pemesanan sewa mobil) dan mengirimkan respons bergaya obrolan yang komprehensif kembali ke pengguna.

## Web Bahasa Alami (NLWeb)

Situs web telah lama menjadi cara utama bagi pengguna untuk mengakses informasi dan data di seluruh internet.

Mari kita lihat komponen berbeda dari NLWeb, manfaat NLWeb dan contoh bagaimana NLWeb kami bekerja dengan melihat aplikasi perjalanan kami.

### Komponen NLWeb

- **NLWeb Application (Core Service Code)**: Sistem yang memproses pertanyaan bahasa alami. Ia menghubungkan bagian-bagian berbeda dari platform untuk membuat respons. Anda dapat menganggapnya sebagai **mesin yang menggerakkan fitur bahasa alami** dari sebuah situs web.

- **NLWeb Protocol**: Ini adalah **sekumpulan aturan dasar untuk interaksi bahasa alami** dengan sebuah situs web. Ia mengirimkan kembali respons dalam format JSON (sering menggunakan Schema.org). Tujuannya adalah menciptakan fondasi sederhana untuk "AI Web," sama seperti HTML memungkinkan berbagi dokumen secara online.

- **MCP Server (Model Context Protocol Endpoint)**: Setiap pengaturan NLWeb juga berfungsi sebagai **server MCP**. Ini berarti ia dapat **membagikan alat (seperti metode “ask”) dan data** dengan sistem AI lain. Dalam praktiknya, ini membuat konten dan kemampuan situs web dapat digunakan oleh agen AI, memungkinkan situs menjadi bagian dari "ekosistem agen" yang lebih luas.

- **Embedding Models**: Model-model ini digunakan untuk **mengubah konten situs web menjadi representasi numerik yang disebut vektor** (embeddings). Vektor-vektor ini menangkap makna dengan cara yang dapat dibandingkan dan dicari oleh komputer. Mereka disimpan di sebuah basis data khusus, dan pengguna dapat memilih model embedding mana yang ingin mereka gunakan.

- **Vector Database (Retrieval Mechanism)**: Basis data ini **menyimpan embeddings dari konten situs web**. Ketika seseorang mengajukan pertanyaan, NLWeb memeriksa basis data vektor untuk dengan cepat menemukan informasi yang paling relevan. Ia memberikan daftar jawaban yang mungkin dengan cepat, diurutkan berdasarkan kesamaan. NLWeb bekerja dengan berbagai sistem penyimpanan vektor seperti Qdrant, Snowflake, Milvus, Azure AI Search, dan Elasticsearch.

### Contoh NLWeb

![NLWeb](../../../translated_images/id/nlweb-diagram.c1e2390b310e5fe4.webp)

Pertimbangkan kembali situs pemesanan perjalanan kita, tetapi kali ini, ia didukung oleh NLWeb.

1. **Ingest Data**: Katalog produk yang sudah ada di situs perjalanan (mis., daftar penerbangan, deskripsi hotel, paket tur) diformat menggunakan Schema.org atau dimuat melalui feed RSS. Alat NLWeb mengambil data terstruktur ini, membuat embeddings, dan menyimpannya di basis data vektor lokal atau jarak jauh.

2. **Query Bahasa Alami (Manusia)**: Seorang pengguna mengunjungi situs dan, alih-alih menavigasi menu, mengetik ke dalam antarmuka obrolan: "Temukan hotel ramah keluarga di Honolulu dengan kolam renang untuk minggu depan".

3. **Pemrosesan NLWeb**: Aplikasi NLWeb menerima kueri ini. Ia mengirimkan kueri ke sebuah LLM untuk pemahaman dan secara bersamaan mencari basis data vektornya untuk daftar hotel yang relevan.

4. **Hasil Akurat**: LLM membantu menafsirkan hasil pencarian dari basis data, mengidentifikasi kecocokan terbaik berdasarkan kriteria "ramah keluarga," "kolam renang," dan "Honolulu", lalu memformat respons dalam bahasa alami. Yang penting, respons merujuk pada hotel nyata dari katalog situs, menghindari informasi yang dibuat-buat.

5. **Interaksi Agen AI**: Karena NLWeb berfungsi sebagai server MCP, agen perjalanan AI eksternal juga dapat terhubung ke instance NLWeb situs ini. Agen AI tersebut kemudian dapat menggunakan metode MCP `ask` untuk mengkueri situs secara langsung: `ask("Are there any vegan-friendly restaurants in the Honolulu area recommended by the hotel?")`. Instance NLWeb akan memproses ini, memanfaatkan basis data informasi restorannya (jika dimuat), dan mengembalikan respons JSON yang terstruktur.

### Punya Pertanyaan Lebih Lanjut tentang MCP/A2A/NLWeb?

Bergabunglah dengan [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) untuk bertemu dengan pembelajar lain, menghadiri sesi jam kantor dan mendapatkan pertanyaan Agen AI Anda dijawab.

## Sumber Daya

- [MCP untuk Pemula](https://aka.ms/mcp-for-beginners)  
- [Dokumentasi MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Repo NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Kerangka Agen Microsoft](https://aka.ms/ai-agents-beginners/agent-framewrok)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Penafian:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI Co-op Translator (https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi penting, disarankan melakukan terjemahan profesional oleh penerjemah manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->