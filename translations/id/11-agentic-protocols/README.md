# Menggunakan Protokol Agentic (MCP, A2A dan NLWeb)

[![Agentic Protocols](../../../translated_images/id/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Klik gambar di atas untuk melihat video dari pelajaran ini)_

Seiring pertumbuhan penggunaan agen AI, kebutuhan akan protokol yang menjamin standarisasi, keamanan, dan mendukung inovasi terbuka juga meningkat. Dalam pelajaran ini, kita akan membahas 3 protokol yang bertujuan memenuhi kebutuhan ini - Model Context Protocol (MCP), Agent to Agent (A2A) dan Natural Language Web (NLWeb).

## Pendahuluan

Dalam pelajaran ini, kita akan membahas:

• Bagaimana **MCP** memungkinkan Agen AI mengakses alat dan data eksternal untuk menyelesaikan tugas pengguna.

• Bagaimana **A2A** memungkinkan komunikasi dan kolaborasi antar agen AI yang berbeda.

• Bagaimana **NLWeb** menghadirkan antarmuka bahasa alami ke situs web manapun sehingga Agen AI dapat menemukan dan berinteraksi dengan konten.

## Tujuan Pembelajaran

• **Mengidentifikasi** tujuan inti dan manfaat MCP, A2A, dan NLWeb dalam konteks agen AI.

• **Menjelaskan** bagaimana masing-masing protokol memfasilitasi komunikasi dan interaksi antara LLM, alat, dan agen lain.

• **Mengenali** peran berbeda yang dimainkan setiap protokol dalam membangun sistem agen kompleks.

## Model Context Protocol

**Model Context Protocol (MCP)** adalah standar terbuka yang menyediakan cara standar bagi aplikasi untuk menyediakan konteks dan alat kepada LLM. Ini memungkinkan "adaptor universal" ke berbagai sumber data dan alat yang dapat dihubungkan oleh Agen AI secara konsisten.

Mari kita lihat komponen MCP, manfaat dibanding penggunaan API langsung, dan contoh bagaimana agen AI dapat menggunakan server MCP.

### Komponen Inti MCP

MCP beroperasi dengan **arsitektur klien-server** dan komponen intinya adalah:

• **Host** adalah aplikasi LLM (misalnya editor kode seperti VSCode) yang memulai koneksi ke Server MCP.

• **Klien** adalah komponen dalam aplikasi host yang mempertahankan koneksi satu-ke-satu dengan server.

• **Server** adalah program ringan yang menyediakan kapabilitas spesifik.

Termasuk dalam protokol adalah tiga primitif inti yang menjadi kapabilitas Server MCP:

• **Alat**: Ini adalah tindakan atau fungsi terpisah yang dapat dipanggil oleh agen AI untuk melakukan aksi. Contohnya, layanan cuaca mungkin menyediakan alat "dapatkan cuaca", atau server e-commerce menyediakan alat "beli produk". Server MCP mengiklankan nama, deskripsi, dan skema masukan/keluaran setiap alat dalam daftar kapabilitasnya.

• **Sumber Daya**: Item data atau dokumen baca-saja yang dapat disediakan oleh server MCP dan dapat diambil oleh klien sesuai permintaan. Contohnya mencakup isi file, rekaman database, atau file log. Sumber daya bisa berupa teks (seperti kode atau JSON) atau binari (seperti gambar atau PDF).

• **Prompt**: Template yang sudah ditentukan sebelumnya yang memberikan saran prompt, memungkinkan alur kerja yang lebih kompleks.

### Manfaat MCP

MCP menawarkan keuntungan signifikan untuk Agen AI:

• **Penemuan Alat Dinamis**: Agen dapat secara dinamis menerima daftar alat yang tersedia dari server beserta deskripsi fungsi mereka. Ini berbeda dengan API tradisional yang biasanya memerlukan pengkodean statis untuk integrasi, sehingga setiap perubahan API butuh pembaruan kode. MCP menawarkan pendekatan "integrasi sekali", menghasilkan adaptabilitas lebih besar.

• **Interoperabilitas Antar LLM**: MCP bekerja lintas LLM yang berbeda, menyediakan fleksibilitas untuk mengganti model inti guna evaluasi performa lebih baik.

• **Standarisasi Keamanan**: MCP mencakup metode autentikasi standar, meningkatkan skalabilitas ketika menambah akses ke server MCP lain. Ini lebih sederhana dibanding mengelola berbagai kunci dan tipe autentikasi untuk berbagai API tradisional.

### Contoh MCP

![MCP Diagram](../../../translated_images/id/mcp-diagram.e4ca1cbd551444a1.webp)

Bayangkan seorang pengguna ingin memesan penerbangan menggunakan asisten AI yang didukung MCP.

1. **Koneksi**: Asisten AI (klien MCP) terhubung ke server MCP yang disediakan oleh maskapai penerbangan.

2. **Penemuan Alat**: Klien menanyakan ke server MCP maskapai, "Alat apa yang Anda miliki?" Server merespons dengan alat seperti "cari penerbangan" dan "pesan penerbangan".

3. **Pemanggilan Alat**: Anda kemudian meminta asisten AI, "Tolong cari penerbangan dari Portland ke Honolulu." Asisten AI menggunakan LLM-nya mengidentifikasi perlunya memanggil alat "cari penerbangan" dan mengirim parameter terkait (asal, tujuan) ke server MCP.

4. **Eksekusi dan Respon**: Server MCP, sebagai pembungkus, melakukan panggilan aktual ke API pemesanan internal maskapai. Server mendapat informasi penerbangan (misal data JSON) dan mengembalikannya ke asisten AI.

5. **Interaksi Lanjutan**: Asisten AI menyajikan opsi penerbangan. Setelah Anda memilih penerbangan, asisten dapat memanggil alat "pesan penerbangan" pada server MCP yang sama untuk menyelesaikan pemesanan.

## Protokol Agent-to-Agent (A2A)

Sementara MCP fokus menyambungkan LLM ke alat, **protokol Agent-to-Agent (A2A)** melangkah lebih jauh dengan memungkinkan komunikasi dan kolaborasi antar agen AI yang berbeda. A2A menghubungkan agen AI dari organisasi, lingkungan, dan tumpukan teknologi berbeda untuk menyelesaikan tugas bersama.

Kita akan membahas komponen dan manfaat A2A, beserta contoh penerapannya dalam aplikasi perjalanan kita.

### Komponen Inti A2A

A2A fokus pada memungkinkan komunikasi antar agen dan membuat mereka bekerja bersama menyelesaikan subtugas pengguna. Setiap komponen protokol berkontribusi pada ini:

#### Kartu Agen

Seperti bagaimana server MCP berbagi daftar alat, Kartu Agen memiliki:
- Nama Agen.
- **deskripsi tugas umum** yang diselesaikannya.
- **daftar keterampilan spesifik** dengan deskripsi untuk membantu agen lain (atau pengguna manusia) memahami kapan dan mengapa memanggil agen tersebut.
- **URL Endpoint saat ini** dari agen.
- **versi** dan **kapabilitas** agen seperti streaming respon dan notifikasi push.

#### Eksekutor Agen

Eksekutor Agen bertanggung jawab **mengoper konteks chat pengguna ke agen jarak jauh**, agen jarak jauh perlu ini untuk memahami tugas yang harus diselesaikan. Dalam server A2A, agen menggunakan LLM-nya sendiri untuk memparsing permintaan masuk dan menjalankan tugas dengan alat internalnya.

#### Artefak

Setelah agen jarak jauh menyelesaikan tugas yang diminta, hasil kerjanya dibuat sebagai artefak. Artefak **berisi hasil kerja agen**, **deskripsi apa yang diselesaikan**, dan **konteks teks** yang dikirim melalui protokol. Setelah artefak dikirim, koneksi dengan agen jarak jauh ditutup sampai diperlukan lagi.

#### Antrian Acara

Komponen ini dipakai untuk **menangani pembaruan dan meneruskan pesan**. Ini sangat penting di produksi untuk sistem agentik agar mencegah koneksi antar agen tertutup sebelum tugas selesai, terutama saat penyelesaian tugas bisa berlangsung lama.

### Manfaat A2A

• **Kolaborasi Lebih Baik**: Memungkinkan agen dari vendor dan platform berbeda berinteraksi, berbagi konteks, dan bekerja sama, memudahkan otomasi lancar di sistem yang biasanya terpisah.

• **Fleksibilitas Pemilihan Model**: Setiap agen A2A dapat memilih LLM yang digunakannya untuk melayani permintaan, memungkinkan model yang dioptimalkan atau disesuaikan per agen, berbeda dengan koneksi LLM tunggal pada beberapa skenario MCP.

• **Autentikasi Terintegrasi**: Autentikasi terintegrasi langsung ke protokol A2A, menyediakan kerangka keamanan kuat untuk interaksi agen.

### Contoh A2A

![A2A Diagram](../../../translated_images/id/A2A-Diagram.8666928d648acc26.webp)

Mari kita kembangkan skenario pemesanan perjalanan kita, tapi kali ini menggunakan A2A.

1. **Permintaan Pengguna ke Multi-Agen**: Pengguna berinteraksi dengan agen-klien A2A "Travel Agent", misalnya dengan berkata, "Tolong pesan seluruh perjalanan ke Honolulu untuk minggu depan, termasuk penerbangan, hotel, dan sewa mobil".

2. **Orkestrasi oleh Travel Agent**: Travel Agent menerima permintaan kompleks ini. Ia menggunakan LLM-nya untuk menalar tugas dan memastikan perlu berinteraksi dengan agen spesialis lain.

3. **Komunikasi Antar Agen**: Travel Agent lalu menggunakan protokol A2A untuk terhubung dengan agen hilir, seperti "Airline Agent", "Hotel Agent", dan "Car Rental Agent" yang dibuat oleh perusahaan berbeda.

4. **Eksekusi Tugas yang Didelegasikan**: Travel Agent mengirim tugas spesifik ke agen spesialis ini (misal, "Cari penerbangan ke Honolulu", "Pesan hotel", "Sewa mobil"). Masing-masing agen spesialis, yang menjalankan LLM dan menggunakan alat sendiri (mungkin juga server MCP), menyelesaikan bagian pemesanan spesifiknya.

5. **Respon Terpadu**: Setelah semua agen hilir menyelesaikan tugasnya, Travel Agent mengkompilasi hasil (detail penerbangan, konfirmasi hotel, pemesanan sewa mobil) dan mengirimkan respon gaya chat lengkap ke pengguna.

## Natural Language Web (NLWeb)

Situs web telah lama menjadi cara utama bagi pengguna mengakses informasi dan data di internet.

Mari kita lihat komponen berbeda dari NLWeb, manfaat NLWeb dan contoh bagaimana NLWeb bekerja melalui aplikasi perjalanan kita.

### Komponen NLWeb

- **Aplikasi NLWeb (Kode Layanan Inti)**: Sistem yang memproses pertanyaan bahasa alami. Ia menghubungkan bagian-bagian platform berbeda untuk menghasilkan respon. Anda dapat memikirkannya sebagai **mesin yang menggerakkan fitur bahasa alami** dari sebuah situs web.

- **Protokol NLWeb**: Ini adalah **sekumpulan aturan dasar untuk interaksi bahasa alami** dengan situs web. Mengirimkan balik respon dalam format JSON (sering menggunakan Schema.org). Tujuannya membuat dasar sederhana bagi “AI Web,” sama seperti HTML memungkinkan berbagi dokumen online.

- **Server MCP (Model Context Protocol Endpoint)**: Setiap setup NLWeb juga bekerja sebagai **server MCP**. Ini berarti dapat **berbagi alat (seperti metode “ask”) dan data** dengan sistem AI lainnya. Dalam praktik, ini membuat konten dan kemampuan situs web dapat digunakan oleh agen AI, memungkinkan situs menjadi bagian dari “ekosistem agen” yang lebih luas.

- **Model Embedding**: Model ini digunakan untuk **mengubah konten situs web menjadi representasi numerik yang disebut vektor** (embedding). Vektor ini menangkap makna dengan cara komputer dapat membandingkan dan mencari. Mereka disimpan dalam database khusus, dan pengguna bisa memilih model embedding yang ingin dipakai.

- **Database Vektor (Mekanisme Pengambilan)**: Database ini **menyimpan embedding konten situs web**. Saat seseorang mengajukan pertanyaan, NLWeb memeriksa database vektor untuk menemukan informasi paling relevan dengan cepat. Memberikan daftar jawaban cepat, diurutkan berdasarkan kesamaan. NLWeb bekerja dengan berbagai sistem penyimpanan vektor seperti Qdrant, Snowflake, Milvus, Azure AI Search, dan Elasticsearch.

### NLWeb dengan Contoh

![NLWeb](../../../translated_images/id/nlweb-diagram.c1e2390b310e5fe4.webp)

Pertimbangkan kembali situs web pemesanan perjalanan kita, tetapi kali ini didukung oleh NLWeb.

1. **Ingesti Data**: Katalog produk situs perjalanan yang sudah ada (misal daftar penerbangan, deskripsi hotel, paket tur) diformat menggunakan Schema.org atau dimuat lewat RSS feed. Alat NLWeb mengolah data terstruktur ini, membuat embedding, dan menyimpannya di database vektor lokal atau jarak jauh.

2. **Query Bahasa Alami (Manusia)**: Seorang pengguna mengunjungi situs dan, daripada menavigasi menu, mengetik ke antarmuka chat: "Cari hotel ramah keluarga di Honolulu dengan kolam renang untuk minggu depan".

3. **Pemrosesan NLWeb**: Aplikasi NLWeb menerima query ini. Ia mengirim query ke LLM untuk memahami sambil mencari di database vektor untuk daftar hotel relevan.

4. **Hasil Akurat**: LLM membantu menginterpretasi hasil pencarian database, mengidentifikasi kecocokan terbaik berdasarkan kriteria "ramah keluarga", "kolam renang", dan "Honolulu", lalu memformat jawaban bahasa alami. Penting, jawaban merujuk ke hotel nyata dari katalog situs, menghindari informasi yang dibuat-buat.

5. **Interaksi Agen AI**: Karena NLWeb berperan sebagai server MCP, agen AI perjalanan eksternal juga dapat terhubung ke instance NLWeb situs ini. Agen AI kemudian bisa menggunakan metode `ask` MCP untuk menanyakan langsung ke situs: `ask("Apakah ada restoran vegan yang direkomendasikan oleh hotel di area Honolulu?")`. Instance NLWeb akan memproses ini, memanfaatkan database informasi restoran (jika dimuat), dan mengembalikan respon JSON terstruktur.

### Punya Pertanyaan Lebih Lanjut tentang MCP/A2A/NLWeb?

Bergabunglah dengan [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) untuk bertemu dengan pembelajar lain, menghadiri jam kantor, dan mendapatkan jawaban atas pertanyaan Agen AI Anda.

## Sumber Daya

- [MCP untuk Pemula](https://aka.ms/mcp-for-beginners)  
- [Dokumentasi MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Repo NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framework)

## Pelajaran Sebelumnya

[AI Agents dalam Produksi](../10-ai-agents-production/README.md)

## Pelajaran Berikutnya

[Rekayasa Konteks untuk Agen AI](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->