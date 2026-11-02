# Menggunakan Protokol Agentic (MCP, A2A dan NLWeb)

[![Agentic Protocols](../../../translated_images/id/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Klik gambar di atas untuk melihat video pelajaran ini)_

Seiring meningkatnya penggunaan agen AI, kebutuhan akan protokol yang memastikan standarisasi, keamanan, dan mendukung inovasi terbuka juga meningkat. Dalam pelajaran ini, kita akan membahas 3 protokol yang bertujuan memenuhi kebutuhan ini - Model Context Protocol (MCP), Agent to Agent (A2A) dan Natural Language Web (NLWeb).

## Pendahuluan

Dalam pelajaran ini, kita akan membahas:

• Bagaimana **MCP** memungkinkan Agen AI mengakses alat dan data eksternal untuk menyelesaikan tugas pengguna.

• Bagaimana **A2A** memungkinkan komunikasi dan kolaborasi antar agen AI yang berbeda.

• Bagaimana **NLWeb** menghadirkan antarmuka bahasa alami ke situs web mana pun sehingga Agen AI dapat menemukan dan berinteraksi dengan konten tersebut.

## Tujuan Pembelajaran

• **Mengidentifikasi** tujuan inti dan manfaat MCP, A2A, dan NLWeb dalam konteks agen AI.

• **Menjelaskan** bagaimana setiap protokol memfasilitasi komunikasi dan interaksi antara LLM, alat, dan agen lain.

• **Mengenali** peran berbeda yang dimainkan setiap protokol dalam membangun sistem agentic yang kompleks.

## Model Context Protocol

**Model Context Protocol (MCP)** adalah standar terbuka yang menyediakan cara standar bagi aplikasi untuk menyediakan konteks dan alat ke LLM. Ini memungkinkan "adaptor universal" ke berbagai sumber data dan alat yang dapat dihubungkan oleh Agen AI dengan cara yang konsisten.

Mari kita lihat komponen MCP, manfaatnya dibandingkan penggunaan API langsung, dan contoh bagaimana agen AI mungkin menggunakan server MCP.

### Komponen Inti MCP

MCP beroperasi dengan **arsitektur klien-server** dan komponen intinya adalah:

• **Hosts** adalah aplikasi LLM (misalnya editor kode seperti VSCode) yang memulai koneksi ke Server MCP.

• **Clients** adalah komponen di dalam aplikasi host yang menjaga koneksi satu-ke-satu dengan server.

• **Servers** adalah program ringan yang mengekspos kemampuan spesifik.

Termasuk dalam protokol adalah tiga primitif inti yang merupakan kemampuan Server MCP:

• **Tools**: Ini adalah tindakan atau fungsi diskrit yang dapat dipanggil oleh agen AI untuk melakukan aksi. Misalnya, layanan cuaca mungkin mengekspos alat "dapatkan cuaca", atau server e-commerce mungkin mengekspos alat "beli produk". Server MCP mengiklankan nama, deskripsi, dan skema input/output dari setiap alat yang mereka miliki.

• **Resources**: Ini adalah item data baca-saja atau dokumen yang dapat disediakan oleh server MCP, dan klien dapat mengambilnya saat diminta. Contohnya termasuk isi file, catatan basis data, atau file log. Resources dapat berupa teks (seperti kode atau JSON) atau biner (seperti gambar atau PDF).

• **Prompts**: Ini adalah template yang telah ditentukan sebelumnya yang menyediakan saran prompt, memungkinkan alur kerja yang lebih kompleks.

### Manfaat MCP

MCP menawarkan keuntungan signifikan bagi Agen AI:

• **Penemuan Alat Dinamis**: Agen dapat secara dinamis menerima daftar alat yang tersedia dari server beserta deskripsi fungsinya. Ini berbeda dengan API tradisional, yang biasanya memerlukan pengkodean statis untuk integrasi, sehingga setiap perubahan API memerlukan pembaruan kode. MCP menawarkan pendekatan "integrasi sekali", yang menghasilkan adaptabilitas yang lebih besar.

• **Interoperabilitas Antar LLM**: MCP berfungsi lintas LLM berbeda, memberikan fleksibilitas untuk mengganti model inti guna evaluasi kinerja yang lebih baik.

• **Keamanan Standar**: MCP mencakup metode autentikasi standar, meningkatkan skalabilitas saat menambahkan akses ke server MCP tambahan. Ini lebih sederhana daripada mengelola berbagai kunci dan tipe autentikasi untuk berbagai API tradisional.

### Contoh MCP

![MCP Diagram](../../../translated_images/id/mcp-diagram.e4ca1cbd551444a1.webp)

Bayangkan seorang pengguna ingin memesan tiket pesawat menggunakan asisten AI yang didukung MCP.

1. **Koneksi**: Asisten AI (klien MCP) terhubung ke server MCP yang disediakan oleh maskapai penerbangan.

2. **Penemuan Alat**: Klien bertanya ke server MCP maskapai, "Alat apa yang Anda miliki?" Server membalas dengan alat seperti "cari penerbangan" dan "pesan penerbangan".

3. **Pemanggilan Alat**: Pengguna kemudian meminta asisten AI, "Tolong cari penerbangan dari Portland ke Honolulu." Asisten AI, menggunakan LLM-nya, mengidentifikasi bahwa perlu memanggil alat "cari penerbangan" dan mengirimkan parameter yang relevan (asal, tujuan) ke server MCP.

4. **Eksekusi dan Respon**: Server MCP, berperan sebagai pembungkus, membuat panggilan sebenarnya ke API pemesanan internal maskapai. Kemudian menerima informasi penerbangan (misalnya data JSON) dan mengirimkannya kembali ke asisten AI.

5. **Interaksi Lanjutan**: Asisten AI menyajikan pilihan penerbangan. Setelah Anda memilih penerbangan, asisten bisa memanggil alat "pesan penerbangan" pada server MCP yang sama untuk menyelesaikan pemesanan.

## Protokol Agent-ke-Agent (A2A)

Sementara MCP fokus pada menghubungkan LLM ke alat, **Protokol Agent-ke-Agent (A2A)** melangkah lebih jauh dengan memungkinkan komunikasi dan kolaborasi antar agen AI yang berbeda. A2A menghubungkan agen AI di berbagai organisasi, lingkungan, dan tumpukan teknologi untuk menyelesaikan tugas bersama.

Kita akan memeriksa komponen dan manfaat A2A, serta contoh bagaimana protokol ini dapat diterapkan dalam aplikasi perjalanan kita.

### Komponen Inti A2A

A2A fokus pada memungkinkan komunikasi antar agen dan menjadikan mereka bekerja sama menyelesaikan subtugas pengguna. Setiap komponen protokol berkontribusi untuk ini:

#### Kartu Agen

Mirip dengan bagaimana server MCP berbagi daftar alat, Kartu Agen memiliki:
- Nama Agen.
- **deskripsi tugas umum** yang diselesaikan.
- **daftar keterampilan khusus** dengan deskripsi untuk membantu agen lain (atau bahkan pengguna manusia) memahami kapan dan mengapa mereka ingin memanggil agen tersebut.
- **URL Endpoint saat ini** dari agen
- **versi** dan **kemampuan** agen seperti streaming respons dan notifikasi push.

#### Eksekutor Agen

Eksekutor Agen bertanggung jawab untuk **mengoper konteks obrolan pengguna ke agen jarak jauh**, agen jarak jauh memerlukan ini untuk memahami tugas yang harus diselesaikan. Dalam server A2A, agen menggunakan Large Language Model (LLM)-nya sendiri untuk mengurai permintaan yang masuk dan mengeksekusi tugas menggunakan alat internalnya sendiri.

#### Artefak

Setelah agen jarak jauh menyelesaikan tugas yang diminta, produk kerjanya dibuat sebagai artefak. Artefak **mengandung hasil pekerjaan agen**, **deskripsi apa yang telah diselesaikan**, dan **konteks teks** yang dikirim melalui protokol. Setelah artefak dikirim, koneksi dengan agen jarak jauh ditutup sampai diperlukan lagi.

#### Antrian Event

Komponen ini digunakan untuk **menangani pembaruan dan mengoper pesan**. Ini sangat penting dalam produksi untuk sistem agentic agar mencegah koneksi antar agen ditutup sebelum tugas selesai, terutama ketika penyelesaian tugas memerlukan waktu lama.

### Manfaat A2A

• **Kolaborasi yang Ditingkatkan**: Memungkinkan agen dari vendor dan platform berbeda untuk berinteraksi, berbagi konteks, dan bekerja sama, memfasilitasi otomatisasi tanpa hambatan di sistem yang biasanya terpisah.

• **Fleksibilitas Pemilihan Model**: Setiap agen A2A bisa memutuskan LLM mana yang digunakan untuk melayani permintaannya, memungkinkan model yang dioptimalkan atau disesuaikan per agen, berbeda dengan koneksi LLM tunggal di beberapa skenario MCP.

• **Autentikasi Terintegrasi**: Autentikasi terintegrasi langsung dalam protokol A2A, memberikan kerangka keamanan kuat untuk interaksi agen.

### Contoh A2A

![A2A Diagram](../../../translated_images/id/A2A-Diagram.8666928d648acc26.webp)

Mari kita kembangkan skenario pemesanan perjalanan kita, tapi kali ini menggunakan A2A.

1. **Permintaan Pengguna ke Multi-Agen**: Seorang pengguna berinteraksi dengan client/agen A2A "Travel Agent", misalnya dengan mengatakan, "Tolong pesan seluruh perjalanan ke Honolulu untuk minggu depan, termasuk penerbangan, hotel, dan mobil sewaan".

2. **Orkestrasi oleh Travel Agent**: Travel Agent menerima permintaan kompleks ini. Ia menggunakan LLM-nya untuk menganalisis tugas dan menentukan perlu berinteraksi dengan agen khusus lainnya.

3. **Komunikasi Antar-Agen**: Travel Agent kemudian menggunakan protokol A2A untuk terhubung dengan agen di hilir, seperti "Airline Agent", "Hotel Agent", dan "Car Rental Agent" yang dibuat oleh perusahaan berbeda.

4. **Pelaksanaan Tugas yang Didelegasikan**: Travel Agent mengirimkan tugas spesifik ke agen khusus ini (misalnya, "Cari penerbangan ke Honolulu", "Pesan hotel", "Sewa mobil"). Masing-masing agen khusus ini, yang menjalankan LLM sendiri dan menggunakan alatnya sendiri (yang bisa jadi adalah server MCP juga), melakukan bagian pemesanan masing-masing.

5. **Respons Terpadu**: Setelah semua agen di hilir menyelesaikan tugasnya, Travel Agent mengompilasi hasilnya (detail penerbangan, konfirmasi hotel, pemesanan sewa mobil) dan mengirim respons gaya obrolan yang komprehensif kembali ke pengguna.

## Natural Language Web (NLWeb)

Situs web telah lama menjadi cara utama bagi pengguna untuk mengakses informasi dan data di seluruh internet.

Mari kita lihat komponen berbeda dari NLWeb, manfaat NLWeb, dan contoh cara kerja NLWeb dengan melihat aplikasi perjalanan kita.

### Komponen NLWeb

- **Aplikasi NLWeb (Kode Layanan Inti)**: Sistem yang memproses pertanyaan bahasa alami. Ia menghubungkan bagian-bagian berbeda dari platform untuk membuat respons. Anda bisa menganggapnya sebagai **mesin yang menggerakkan fitur bahasa alami** dari situs web.

- **Protokol NLWeb**: Ini adalah **sekumpulan aturan dasar untuk interaksi bahasa alami** dengan sebuah situs web. Ia mengirim balik respons dalam format JSON (sering menggunakan Schema.org). Tujuannya adalah membuat fondasi sederhana untuk “AI Web,” sama seperti HTML memungkinkan berbagi dokumen secara online.

- **Server MCP (Model Context Protocol Endpoint)**: Setiap setup NLWeb juga berfungsi sebagai **server MCP**. Ini berarti dapat **berbagi alat (seperti metode “ask”) dan data** dengan sistem AI lain. Dalam praktiknya, ini membuat konten dan kemampuan situs web dapat digunakan oleh agen AI, sehingga situs menjadi bagian dari “ekosistem agen” yang lebih luas.

- **Model Embedding**: Model ini digunakan untuk **mengonversi konten situs web ke representasi numerik yang disebut vektor** (embedding). Vektor ini menangkap makna dengan cara yang dapat dibandingkan dan dicari oleh komputer. Mereka disimpan dalam basis data khusus, dan pengguna dapat memilih model embedding yang ingin digunakan.

- **Basis Data Vektor (Mekanisme Pengambilan)**: Basis data ini **menyimpan embedding dari konten situs web**. Saat seseorang bertanya, NLWeb memeriksa basis data vektor untuk menemukan informasi yang paling relevan dengan cepat. Memberikan daftar jawaban yang cepat, yang diurutkan berdasarkan kesamaan. NLWeb bekerja dengan berbagai sistem penyimpanan vektor seperti Qdrant, Snowflake, Milvus, Azure AI Search, dan Elasticsearch.

### NLWeb dengan Contoh

![NLWeb](../../../translated_images/id/nlweb-diagram.c1e2390b310e5fe4.webp)

Pertimbangkan situs web pemesanan perjalanan kita lagi, tapi kali ini, didukung oleh NLWeb.

1. **Ingesti Data**: Katalog produk situs perjalanan yang ada (misalnya daftar penerbangan, deskripsi hotel, paket tur) diformat menggunakan Schema.org atau dimuat melalui feed RSS. Alat NLWeb mengolah data terstruktur ini, membuat embedding, dan menyimpannya di basis data vektor lokal atau jarak jauh.

2. **Query Bahasa Alami (Manusia)**: Seorang pengguna mengunjungi situs dan, alih-alih menavigasi menu, mengetik di antarmuka obrolan: "Cari hotel ramah keluarga di Honolulu dengan kolam renang untuk minggu depan".

3. **Pemrosesan NLWeb**: Aplikasi NLWeb menerima pertanyaan ini. Ia mengirim kueri ke LLM untuk memahami dan sekaligus mencari di basis data vektor untuk daftar hotel yang relevan.

4. **Hasil Akurat**: LLM membantu menginterpretasikan hasil pencarian dari basis data, mengidentifikasi kecocokan terbaik berdasarkan kriteria "ramah keluarga", "kolam renang", dan "Honolulu", kemudian memformat respons bahasa alami. Yang paling penting, respons merujuk pada hotel aktual dari katalog situs, menghindari informasi palsu.

5. **Interaksi Agen AI**: Karena NLWeb berfungsi sebagai server MCP, agen perjalanan AI eksternal juga dapat terhubung ke instance NLWeb situs ini. Agen AI dapat menggunakan metode `ask` MCP untuk menanyakan situs secara langsung: `ask("Apakah ada restoran vegan yang direkomendasikan oleh hotel di area Honolulu?")`. Instance NLWeb akan memproses ini, memanfaatkan database informasi restoran (jika dimuat), dan mengembalikan respons JSON terstruktur.

### Ingin Bertanya Lebih Lanjut tentang MCP/A2A/NLWeb?

Bergabunglah dengan [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) untuk bertemu dengan pelajar lain, menghadiri jam kantor, dan mendapatkan jawaban atas pertanyaan Agen AI Anda.

## Sumber Daya

- [MCP for Beginners](https://aka.ms/mcp-for-beginners)  
- [MCP Documentation](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python)

## Pelajaran Sebelumnya

[AI Agents in Production](../10-ai-agents-production/README.md)

## Pelajaran Berikutnya

[Context Engineering for AI Agents](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->