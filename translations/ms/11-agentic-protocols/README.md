# Menggunakan Protokol Agentik (MCP, A2A dan NLWeb)

[![Agentic Protocols](../../../translated_images/ms/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Klik imej di atas untuk menonton video pelajaran ini)_

Seiring dengan peningkatan penggunaan ejen AI, keperluan untuk protokol yang memastikan penyeragaman, keselamatan, dan sokongan inovasi terbuka juga meningkat. Dalam pelajaran ini, kita akan membincangkan 3 protokol yang bertujuan memenuhi keperluan ini - Model Context Protocol (MCP), Agent to Agent (A2A) dan Natural Language Web (NLWeb).

## Pengenalan

Dalam pelajaran ini, kita akan membincangkan:

• Bagaimana **MCP** membolehkan Ejen AI mengakses alat dan data luaran untuk menyelesaikan tugas pengguna.

• Bagaimana **A2A** membolehkan komunikasi dan kolaborasi antara ejen AI yang berbeza.

• Bagaimana **NLWeb** membawa antara muka bahasa semula jadi kepada mana-mana laman web membolehkan Ejen AI mencari dan berinteraksi dengan kandungan.

## Matlamat Pembelajaran

• **Kenali** tujuan utama dan faedah MCP, A2A, dan NLWeb dalam konteks ejen AI.

• **Terangkan** bagaimana setiap protokol memudahkan komunikasi dan interaksi antara LLM, alat, dan ejen lain.

• **Kenal pasti** peranan berbeza yang dimainkan setiap protokol dalam membina sistem agentik yang kompleks.

## Model Context Protocol

**Model Context Protocol (MCP)** ialah piawaian terbuka yang menyediakan cara terseragam untuk aplikasi memberikan konteks dan alat kepada LLM. Ini membolehkan "penyesuai sejagat" kepada pelbagai sumber data dan alat yang boleh disambungkan oleh Ejen AI secara konsisten.

Mari kita lihat komponen MCP, faedah berbanding penggunaan API langsung, dan contoh bagaimana ejen AI mungkin menggunakan pelayan MCP.

### Komponen Teras MCP

MCP beroperasi pada **arsitektur klien-pelayan** dan komponen terasnya ialah:

• **Hos** ialah aplikasi LLM (contohnya penyunting kod seperti VSCode) yang memulakan sambungan kepada Pelayan MCP.

• **Klien** ialah komponen dalam aplikasi hos yang mengekalkan sambungan satu-ke-satu dengan pelayan.

• **Pelayan** ialah program ringan yang mendedahkan keupayaan khusus.

Termasuk dalam protokol ialah tiga primitif teras yang merupakan keupayaan Pelayan MCP:

• **Alat**: Ini ialah tindakan atau fungsi berasingan yang boleh dipanggil oleh ejen AI untuk melaksanakan tindakan. Contohnya, perkhidmatan cuaca mungkin mendedahkan alat "dapatkan cuaca", atau pelayan e-dagang mungkin mendedahkan alat "beli produk". Pelayan MCP mengiklankan nama, penerangan, dan skema input/output setiap alat dalam senarai keupayaan mereka.

• **Sumber**: Ini ialah item data atau dokumen baca sahaja yang boleh disediakan oleh pelayan MCP, dan klien boleh memintanya mengikut keperluan. Contoh termasuk kandungan fail, rekod pangkalan data, atau fail log. Sumber boleh berupa teks (seperti kod atau JSON) atau binari (seperti imej atau PDF).

• **Prompt**: Ini ialah templat yang telah ditetapkan yang menyediakan cadangan prompt, membolehkan aliran kerja yang lebih kompleks.

### Faedah MCP

MCP menawarkan kelebihan ketara untuk Ejen AI:

• **Penemuan Alat Dinamik**: Ejen boleh menerima senarai alat yang tersedia secara dinamik dari pelayan bersama dengan penerangan apa yang dilakukan. Ini berbeza dengan API tradisional yang kerap memerlukan pengkodan statik untuk integrasi, bermakna setiap perubahan API perlu kemaskini kod. MCP menawarkan pendekatan "integrasi sekali", menghasilkan lebih banyak penyesuaian.

• **Keserasian Merentasi LLM**: MCP berfungsi dengan pelbagai LLM, memberikan fleksibiliti untuk menukar model teras bagi menilai prestasi yang lebih baik.

• **Keselamatan Terseragam**: MCP termasuk kaedah pengesahan standard, memperbaiki kebolehskalaan apabila menambah akses kepada pelayan MCP lain. Ini lebih mudah berbanding mengurus kunci berbeza dan jenis pengesahan untuk pelbagai API tradisional.

### Contoh MCP

![MCP Diagram](../../../translated_images/ms/mcp-diagram.e4ca1cbd551444a1.webp)

Bayangkan seorang pengguna mahu menempah penerbangan menggunakan pembantu AI yang dikuasai oleh MCP.

1. **Sambungan**: Pembantu AI (klien MCP) menyambung ke pelayan MCP yang disediakan oleh sebuah syarikat penerbangan.

2. **Penemuan Alat**: Klien bertanya kepada pelayan MCP syarikat penerbangan, "Apakah alat yang anda ada?" Pelayan bertindak balas dengan alat seperti "cari penerbangan" dan "tempah penerbangan".

3. **Pemanggilan Alat**: Anda kemudian meminta pembantu AI, "Tolong cari penerbangan dari Portland ke Honolulu." Pembantu AI, menggunakan LLM-nya, mengenal pasti bahawa ia perlu memanggil alat "cari penerbangan" dan menghantar parameter berkaitan (asal, destinasi) ke pelayan MCP.

4. **Pelaksanaan dan Respons**: Pelayan MCP, bertindak sebagai pembalut, membuat panggilan sebenar ke API tempahan dalaman syarikat penerbangan. Ia kemudian menerima maklumat penerbangan (contohnya data JSON) dan menghantarnya kembali ke pembantu AI.

5. **Interaksi Lanjutan**: Pembantu AI membentangkan pilihan penerbangan. Setelah anda memilih penerbangan, pembantu mungkin memanggil alat "tempah penerbangan" pada pelayan MCP yang sama, menyelesaikan tempahan.

## Protokol Agent-to-Agent (A2A)

Walaupun MCP memberi tumpuan kepada menyambungkan LLM kepada alat, protokol **Agent-to-Agent (A2A)** melangkah lebih jauh dengan membolehkan komunikasi dan kolaborasi antara ejen AI yang berbeza. A2A menghubungkan ejen AI merentasi organisasi, persekitaran, dan teknologi untuk menyelesaikan tugas bersama.

Kita akan meneliti komponen dan faedah A2A, bersama contoh bagaimana ia boleh digunakan dalam aplikasi perjalanan kita.

### Komponen Teras A2A

A2A memberi tumpuan kepada membolehkan komunikasi antara ejen dan menjadikan mereka bekerjasama untuk menyelesaikan sub-tugas pengguna. Setiap komponen protokol menyumbang kepada ini:

#### Kad Ejen

Seperti bagaimana pelayan MCP berkongsi senarai alat, Kad Ejen mempunyai:
- Nama Ejen.
- **penerangan tentang tugas umum** yang dilaksanakannya.
- **senarai kemahiran khusus** dengan penerangan untuk membantu ejen lain (atau pengguna manusia) memahami bila dan kenapa mereka ingin memanggil ejen itu.
- **URL Titik Akhir** ejen semasa
- **versi** dan **keupayaan** ejen seperti respons penstriman dan notifikasi tolak.

#### Pelaksana Ejen

Pelaksana Ejen bertanggungjawab untuk **menyampaikan konteks sembang pengguna kepada ejen jauh**, ejen jauh memerlukan ini untuk memahami tugas yang perlu diselesaikan. Dalam pelayan A2A, ejen menggunakan LLM-nya sendiri untuk memproses permintaan masuk dan melaksanakan tugas menggunakan alat dalaman sendiri.

#### Artefak

Setelah ejen jauh selesai melaksanakan tugas yang diminta, hasil kerjanya disimpan sebagai artefak. Artefak **mengandungi hasil kerja ejen**, **penerangan tentang apa yang telah dilaksanakan**, dan **konteks teks** yang dihantar melalui protokol. Setelah artefak dihantar, sambungan dengan ejen jauh ditutup sehingga diperlukan semula.

#### Barisan Acara

Komponen ini digunakan untuk **mengendalikan kemas kini dan menyampaikan mesej**. Ia sangat penting dalam produksi bagi sistem agentik untuk mengelakkan sambungan antara ejen ditutup sebelum tugas diselesaikan, terutamanya apabila masa penyelesaian tugas mungkin mengambil masa lebih lama.

### Faedah A2A

• **Kolaborasi Dipertingkatkan**: Ia membolehkan ejen dari vendor dan platform berbeza berinteraksi, berkongsi konteks, dan bekerjasama, memudahkan automasi lancar merentasi sistem yang sebelum ini terpisah.

• **Fleksibiliti Pemilihan Model**: Setiap ejen A2A boleh menentukan LLM yang digunakannya untuk melayani permintaan, membolehkan model dioptimumkan atau disesuaikan per ejen, tidak seperti sambungan LLM tunggal dalam beberapa senario MCP.

• **Pengesahan Terbina Dalam**: Pengesahan diintegrasikan terus dalam protokol A2A, menyediakan rangka kerja keselamatan kukuh untuk interaksi ejen.

### Contoh A2A

![A2A Diagram](../../../translated_images/ms/A2A-Diagram.8666928d648acc26.webp)

Mari kita kembangkan senario tempahan perjalanan kita, tetapi kali ini menggunakan A2A.

1. **Permintaan Pengguna kepada Multi-Ejen**: Seorang pengguna berinteraksi dengan klien/ejen "Ejen Perjalanan" A2A, mungkin dengan berkata, "Tolong tempah perjalanan lengkap ke Honolulu untuk minggu depan, termasuk penerbangan, hotel, dan kereta sewa".

2. **Pengurusan oleh Ejen Perjalanan**: Ejen Perjalanan menerima permintaan kompleks ini. Ia menggunakan LLM-nya untuk memikirkan tugas dan menentukan bahawa ia perlu berinteraksi dengan ejen khusus lain.

3. **Komunikasi Antara Ejen**: Ejen Perjalanan kemudiannya menggunakan protokol A2A untuk sambung ke ejen hilir, seperti "Ejen Penerbangan", "Ejen Hotel", dan "Ejen Sewa Kereta" yang dibuat oleh syarikat berbeza.

4. **Pelaksanaan Tugasan Bertugas**: Ejen Perjalanan menghantar tugasan spesifik kepada ejen khusus ini (contohnya, "Cari penerbangan ke Honolulu," "Tempah hotel," "Sewa kereta"). Setiap ejen khusus ini, menggunakan LLM sendiri dan alat sendiri (yang mungkin pelayan MCP sendiri), melaksanakan bahagian tempahan masing-masing.

5. **Respons Disatukan**: Setelah semua ejen hilir menyelesaikan tugas mereka, Ejen Perjalanan menyusun hasil (butiran penerbangan, pengesahan hotel, tempahan sewa kereta) dan menghantar respons lengkap gaya sembang kembali kepada pengguna.

## Natural Language Web (NLWeb)

Laman web telah lama menjadi cara utama bagi pengguna mengakses maklumat dan data di internet.

Mari kita lihat komponen berbeza NLWeb, faedah NLWeb dan contoh bagaimana NLWeb berfungsi dengan melihat aplikasi perjalanan kita.

### Komponen NLWeb

- **Aplikasi NLWeb (Kod Perkhidmatan Teras)**: Sistem yang memproses soalan bahasa semula jadi. Ia menghubungkan bahagian platform yang berbeza untuk mencipta respons. Anda boleh menganggapnya sebagai **enjin yang menggerakkan ciri bahasa semula jadi** sebuah laman web.

- **Protokol NLWeb**: Ini ialah **set peraturan asas untuk interaksi bahasa semula jadi** dengan laman web. Ia menghantar respons dalam format JSON (sering menggunakan Schema.org). Tujuannya adalah untuk mencipta asas mudah untuk “Web AI,” sama seperti HTML membolehkan perkongsian dokumen secara dalam talian.

- **Pelayan MCP (Titik Akhir Model Context Protocol)**: Setiap penyediaan NLWeb juga berfungsi sebagai **pelayan MCP**. Ini bermakna ia boleh **berkongsi alat (seperti kaedah “ask”) dan data** dengan sistem AI lain. Dalam praktiknya, ini menjadikan kandungan dan keupayaan laman web boleh digunakan oleh ejen AI, membolehkan laman menjadi sebahagian daripada “ekosistem ejen” yang lebih luas.

- **Model Embedding**: Model ini digunakan untuk **menukar kandungan laman web menjadi representasi berangka yang dipanggil vektor** (embedding). Vektor itu menangkap makna dengan cara komputer boleh banding dan cari. Ia disimpan dalam pangkalan data khusus, dan pengguna boleh memilih model embedding yang mereka ingin gunakan.

- **Pangkalan Data Vektor (Mekanisme Pengambilan)**: Pangkalan data ini **menyimpan embedding kandungan laman web**. Apabila seseorang bertanya, NLWeb memeriksa pangkalan data vektor untuk dengan cepat mencari maklumat paling relevan. Ia memberikan senarai jawapan mungkin yang pantas, diperingkatkan berdasarkan kesamaan. NLWeb berfungsi dengan sistem storan vektor berbeza seperti Qdrant, Snowflake, Milvus, Azure AI Search, dan Elasticsearch.

### NLWeb dengan Contoh

![NLWeb](../../../translated_images/ms/nlweb-diagram.c1e2390b310e5fe4.webp)

Pertimbangkan laman web tempahan perjalanan kita sekali lagi, tetapi kali ini, ia dikuasakan oleh NLWeb.

1. **Pengambilan Data**: Katalog produk laman perjalanan yang sudah sedia ada (contohnya, senarai penerbangan, penerangan hotel, pakej lawatan) diformat menggunakan Schema.org atau dimuat melalui suapan RSS. Alat NLWeb mengambil data berstruktur ini, mencipta embedding, dan menyimpannya dalam pangkalan data vektor tempatan atau jauh.

2. **Pertanyaan Bahasa Semula Jadi (Manusia)**: Seorang pengguna melawat laman web dan, daripada melayari menu, menaip ke antara muka sembang: "Cari hotel mesra keluarga di Honolulu dengan kolam renang untuk minggu depan".

3. **Pemprosesan NLWeb**: Aplikasi NLWeb menerima pertanyaan ini. Ia menghantar pertanyaan kepada LLM untuk memahami dan serentak mencari di pangkalan data vektor bagi senarai hotel yang relevan.

4. **Keputusan Tepat**: LLM membantu mentafsir hasil carian dari pangkalan data, mengenal pasti padanan terbaik berdasarkan kriteria "mesra keluarga," "kolam renang," dan "Honolulu," kemudian memformat respons bahasa semula jadi. Penting, respons merujuk kepada hotel sebenar dari katalog laman web, mengelakkan maklumat yang direka-reka.

5. **Interaksi Ejen AI**: Oleh kerana NLWeb berfungsi sebagai pelayan MCP, ejen perjalanan AI luaran juga boleh menyambung ke contoh NLWeb laman web ini. Ejen AI kemudian boleh menggunakan kaedah `ask` MCP untuk bertanya terus ke laman web: `ask("Adakah terdapat restoran mesra vegan di kawasan Honolulu yang disyorkan oleh hotel?")`. Contoh NLWeb akan memproses soalan ini, menggunakan pangkalan data maklumat restoran (jika dimuat), dan memulangkan respons JSON berstruktur.

### Ada Soalan Lagi tentang MCP/A2A/NLWeb?

Sertai [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) untuk bertemu dengan pelajar lain, hadir waktu pejabat dan dapatkan jawapan kepada soalan AI Agents anda.

## Sumber

- [MCP untuk Pemula](https://aka.ms/mcp-for-beginners)  
- [Dokumentasi MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Repositori NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Rangka Kerja Ejen Microsoft](https://aka.ms/ai-agents-beginners/agent-framewrok)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->