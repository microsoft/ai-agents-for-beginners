# Menggunakan Protokol Agentik (MCP, A2A dan NLWeb)

[![Agentic Protocols](../../../translated_images/ms/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Klik imej di atas untuk menonton video pelajaran ini)_

Seiring dengan peningkatan penggunaan agen AI, keperluan untuk protokol yang memastikan pensuisian piawai, keselamatan, dan menyokong inovasi terbuka juga meningkat. Dalam pelajaran ini, kita akan membincangkan 3 protokol yang berusaha memenuhi keperluan ini - Protokol Konteks Model (MCP), Agent ke Agent (A2A) dan Web Bahasa Semulajadi (NLWeb).

## Pengenalan

Dalam pelajaran ini, kita akan membincangkan:

• Bagaimana **MCP** membenarkan Agen AI mengakses alat dan data luar untuk menyelesaikan tugasan pengguna.

• Bagaimana **A2A** membolehkan komunikasi dan kerjasama antara agen AI yang berbeza.

• Bagaimana **NLWeb** membawa antara muka bahasa semulajadi ke laman web apa pun untuk membolehkan Agen AI menemui dan berinteraksi dengan kandungan tersebut.

## Matlamat Pembelajaran

• **Kenal pasti** tujuan utama dan manfaat MCP, A2A, dan NLWeb dalam konteks agen AI.

• **Terangkan** bagaimana setiap protokol memudahkan komunikasi dan interaksi antara LLM, alat, dan agen lain.

• **Kenali** peranan berbeza yang dimainkan oleh setiap protokol dalam membina sistem agentik yang kompleks.

## Protokol Konteks Model

**Protokol Konteks Model (MCP)** ialah piawai terbuka yang menyediakan cara piawai bagi aplikasi untuk memberikan konteks dan alat kepada LLM. Ini membolehkan "penyesuai universal" ke pelbagai sumber data dan alat yang boleh disambungkan oleh Agen AI dengan cara yang konsisten.

Mari kita lihat komponen MCP, manfaat berbanding penggunaan API secara langsung, dan contoh cara agen AI mungkin menggunakan pelayan MCP.

### Komponen Teras MCP

MCP beroperasi pada **arsitektur klien-pelayan** dan komponen terasnya adalah:

• **Hos** ialah aplikasi LLM (contohnya penyunting kod seperti VSCode) yang memulakan sambungan ke Pelayan MCP.

• **Klien** ialah komponen dalam aplikasi hos yang mengekalkan sambungan satu-satu dengan pelayan.

• **Pelayan** ialah program ringan yang mendedahkan kemampuan khusus.

Termasuk dalam protokol adalah tiga primitif teras yang merupakan kemampuan Pelayan MCP:

• **Alat**: Ini adalah tindakan atau fungsi berasingan yang boleh dipanggil oleh agen AI untuk melakukan tindakan. Contohnya, perkhidmatan cuaca mungkin mendedahkan alat "dapatkan cuaca", atau pelayan e-dagang mungkin mendedahkan alat "beli produk". Pelayan MCP mengiklankan nama, keterangan, dan skema input/output setiap alat dalam senarai kemampuan mereka.

• **Sumber**: Ini adalah item data atau dokumen baca sahaja yang boleh disediakan oleh pelayan MCP, dan klien boleh memperolehinya bila-bila masa diperlukan. Contohnya termasuk kandungan fail, rekod pangkalan data, atau fail log. Sumber boleh berupa teks (seperti kod atau JSON) atau binari (seperti imej atau PDF).

• **Prompt**: Ini adalah templat pradefinisi yang menyediakan cadangan prompt yang membolehkan aliran kerja lebih kompleks.

### Manfaat MCP

MCP menawarkan kelebihan penting untuk Agen AI:

• **Penemuan Alat Dinamik**: Agen boleh menerima senarai alat tersedia dari pelayan secara dinamik bersama dengan keterangan fungsi mereka. Ini berbeza dengan API tradisional, yang biasanya memerlukan pengekodan statik untuk integrasi, yang bermaksud sebarang perubahan API memerlukan kemaskini kod. MCP menawarkan pendekatan "integrasikan sekali", menjadikan ia lebih mudah disesuaikan.

• **Interoperabiliti Merentas LLM**: MCP berfungsi merentas pelbagai LLM, menyediakan fleksibiliti untuk menukar model teras demi penilaian prestasi yang lebih baik.

• **Keselamatan Piawai**: MCP termasuk kaedah pengesahan piawai, meningkatkan kebolehskalaan apabila menambah akses kepada lebih banyak pelayan MCP. Ini lebih mudah berbanding menguruskan kekunci dan jenis pengesahan yang berbeza untuk pelbagai API tradisional.

### Contoh MCP

![MCP Diagram](../../../translated_images/ms/mcp-diagram.e4ca1cbd551444a1.webp)

Bayangkan seorang pengguna mahu menempah penerbangan melalui pembantu AI yang dikuasakan oleh MCP.

1. **Sambungan**: Pembantu AI (klien MCP) menyambung ke pelayan MCP yang disediakan oleh syarikat penerbangan.

2. **Penemuan Alat**: Klien bertanya kepada pelayan MCP syarikat penerbangan, "Apakah alat yang anda ada?" Pelayan menjawab dengan alat seperti "cari penerbangan" dan "tempah penerbangan".

3. **Panggilan Alat**: Anda kemudian bertanya kepada pembantu AI, "Sila cari penerbangan dari Portland ke Honolulu." Pembantu AI, menggunakan LLMnya, mengenal pasti bahawa ia perlu memanggil alat "cari penerbangan" dan menghantar parameter berkaitan (asal, destinasi) ke pelayan MCP.

4. **Pelaksanaan dan Respons**: Pelayan MCP, bertindak sebagai pembungkus, membuat panggilan sebenar ke API tempahan dalaman syarikat penerbangan. Ia kemudian menerima maklumat penerbangan (contohnya data JSON) dan menghantarnya kembali kepada pembantu AI.

5. **Interaksi Lanjutan**: Pembantu AI memaparkan pilihan penerbangan. Setelah anda memilih penerbangan, pembantu mungkin memanggil alat "tempah penerbangan" pada pelayan MCP yang sama, melengkapkan tempahan.

## Protokol Agent-ke-Agent (A2A)

Manakala MCP menumpukan pada sambungan LLM ke alat, **protokol Agent-ke-Agent (A2A)** membawa satu langkah lebih jauh dengan membolehkan komunikasi dan kerjasama antara agen AI yang berbeza. A2A menghubungkan agen AI merentasi organisasi, persekitaran dan teknologi yang berbeza untuk menyelesaikan tugasan bersama.

Kita akan melihat komponen dan manfaat A2A, serta contoh cara ia boleh digunakan dalam aplikasi perjalanan kita.

### Komponen Teras A2A

A2A menumpukan pada membolehkan komunikasi antara agen dan menjadikan mereka bekerjasama menyelesaikan sub-tugas pengguna. Setiap komponen protokol menyumbang kepada ini:

#### Kad Agen

Serupa dengan bagaimana pelayan MCP berkongsi senarai alat, Kad Agen mempunyai:
- Nama Agen.
- **penerangan tugasan umum** yang ia selesaikan.
- **senarai kemahiran khusus** dengan penerangan untuk membantu agen lain (atau pengguna manusia) memahami bila dan mengapa mereka perlu memanggil agen itu.
- **URL Titik Akhir semasa** agen itu
- **versi** dan **keupayaan** agen seperti respons penstriman dan notifikasi push.

#### Pelaksana Agen

Pelaksana Agen bertanggungjawab untuk **menghantar konteks perbualan pengguna kepada agen jauh**, agen jauh memerlukan ini untuk memahami tugasan yang perlu diselesaikan. Dalam pelayan A2A, agen menggunakan sendiri Model Bahasa Besar (LLM) untuk menganalisis permintaan masuk dan melaksanakan tugasan menggunakan alat dalaman mereka sendiri.

#### Artifak

Setelah agen jauh menyelesaikan tugasan yang diminta, hasil kerja mereka dihasilkan sebagai artifak.  Artifak **mengandungi keputusan kerja agen**, **penerangan apa yang telah diselesaikan**, dan **konteks teks** yang dihantar melalui protokol. Setelah artifak dihantar, sambungan dengan agen jauh ditutup sehingga diperlukan lagi.

#### Barisan Acara

Komponen ini digunakan untuk **mengendalikan kemas kini dan menghantar mesej**. Ia amat penting dalam pengeluaran untuk sistem agentik bagi menghalang sambungan antara agen ditutup sebelum tugasan selesai, terutamanya apabila masa penyelesaian tugasan boleh mengambil masa lama.

### Manfaat A2A

• **Kerjasama Dipertingkat**: Ia membolehkan agen dari vendor dan platform berbeza untuk berinteraksi, berkongsi konteks, dan bekerjasama, memudahkan automasi lancar merentasi sistem yang biasanya tidak berkait.

• **Fleksibiliti Pemilihan Model**: Setiap agen A2A boleh menentukan LLM yang digunakannya untuk melayani permintaan, membolehkan model dioptimumkan atau disesuaikan bagi setiap agen, berbeza dengan sambungan LLM tunggal dalam sesetengah senario MCP.

• **Pengesahan Terbina Dalam**: Pengesahan dimasukkan terus ke dalam protokol A2A, menyediakan rangka keselamatan kukuh untuk interaksi agen.

### Contoh A2A

![A2A Diagram](../../../translated_images/ms/A2A-Diagram.8666928d648acc26.webp)

Mari kita kembangkan senario tempahan perjalanan kita, kali ini menggunakan A2A.

1. **Permintaan Pengguna kepada Multi-Agen**: Seorang pengguna berinteraksi dengan klien/agen "Ejen Perjalanan" A2A, mungkin dengan berkata, "Sila tempah satu perjalanan penuh ke Honolulu untuk minggu depan, termasuk penerbangan, hotel, dan kereta sewa".

2. **Pengurusan oleh Ejen Perjalanan**: Ejen Perjalanan menerima permintaan kompleks ini. Ia menggunakan LLMnya untuk berfikir tentang tugasan dan menentukan bahawa ia perlu berinteraksi dengan agen khusus lain.

3. **Komunikasi Antara Agen**: Ejen Perjalanan kemudian menggunakan protokol A2A untuk menyambung ke agen hiliran, seperti "Ejen Syarikat Penerbangan," "Ejen Hotel," dan "Ejen Sewa Kereta" yang dibina oleh syarikat berbeza.

4. **Pelaksanaan Tugasan Didelegasikan**: Ejen Perjalanan menghantar tugasan khusus kepada agen ini (contohnya, "Cari penerbangan ke Honolulu," "Tempah hotel," "Sewa kereta"). Setiap agen khusus ini, menjalankan LLM sendiri dan menggunakan alat mereka sendiri (yang mungkin merupakan pelayan MCP sendiri), melaksanakan bahagian tempahan masing-masing.

5. **Respons Tersusun**: Setelah semua agen hiliran menyelesaikan tugasan mereka, Ejen Perjalanan menyusun keputusan (butiran penerbangan, pengesahan hotel, tempahan kereta sewa) dan menghantar respons berformat perbualan yang lengkap kembali kepada pengguna.

## Web Bahasa Semulajadi (NLWeb)

Laman web telah lama menjadi cara utama pengguna mengakses maklumat dan data di seluruh internet.

Mari kita lihat komponen berbeza NLWeb, manfaat NLWeb dan contoh bagaimana NLWeb berfungsi dengan melihat aplikasi perjalanan kita.

### Komponen NLWeb

- **Aplikasi NLWeb (Kod Perkhidmatan Teras)**: Sistem yang memproses soalan bahasa semulajadi. Ia menghubungkan bahagian berbeza platform untuk mencipta respons. Anda boleh menganggapnya sebagai **enjin yang menggerakkan ciri bahasa semulajadi** sebuah laman web.

- **Protokol NLWeb**: Ini adalah **set peraturan asas untuk interaksi bahasa semulajadi** dengan laman web. Ia menghantar kembali respons dalam format JSON (sering menggunakan Schema.org). Tujuannya adalah untuk mencipta asas mudah bagi “Web AI,” sama seperti HTML memungkinkan perkongsian dokumen secara dalam talian.

- **Pelayan MCP (Titik Akhir Protokol Konteks Model)**: Setiap tetapan NLWeb juga berfungsi sebagai **pelayan MCP**. Ini bermakna ia boleh **berkongsi alat (seperti kaedah “ask”) dan data** dengan sistem AI lain. Dalam praktiknya, ini menjadikan kandungan dan kemampuan laman web boleh digunakan oleh agen AI, membolehkan laman itu menjadi sebahagian daripada “ekosistem agen” yang lebih luas.

- **Model Embedding**: Model ini digunakan untuk **menukar kandungan laman web menjadi representasi nombor yang dipanggil vektor** (embedding). Vektor ini menangkap makna dengan cara yang komputer boleh banding dan cari. Ia disimpan dalam pangkalan data khas, dan pengguna boleh memilih model embedding yang mereka mahu gunakan.

- **Pangkalan Data Vektor (Mekanisme Pengambilan)**: Pangkalan data ini **menyimpan embedding kandungan laman web**. Apabila seseorang bertanya soalan, NLWeb memeriksa pangkalan data vektor untuk mencari maklumat paling relevan dengan cepat. Ia memberikan senarai jawapan yang mungkin dengan ranking berdasarkan kesamaan. NLWeb bekerjasama dengan sistem penyimpanan vektor seperti Qdrant, Snowflake, Milvus, Azure AI Search, dan Elasticsearch.

### NLWeb dengan Contoh

![NLWeb](../../../translated_images/ms/nlweb-diagram.c1e2390b310e5fe4.webp)

Pertimbangkan laman tempahan perjalanan kita sekali lagi, tetapi kali ini, ia dikuasakan oleh NLWeb.

1. **Pengambilan Data**: Katalog produk sedia ada laman perjalanan (contohnya, senarai penerbangan, keterangan hotel, pakej pelancongan) diformatkan menggunakan Schema.org atau dimuatkan melalui RSS feed. Alat NLWeb mengambil data berstruktur ini, mencipta embeddings, dan menyimpannya dalam pangkalan data vektor tempatan atau jauh.

2. **Pertanyaan Bahasa Semulajadi (Manusia)**: Seorang pengguna melawat laman web dan, daripada melayari menu, menaip ke dalam antara muka perbualan: "Cari hotel mesra keluarga di Honolulu dengan kolam renang untuk minggu depan".

3. **Pemprosesan NLWeb**: Aplikasi NLWeb menerima pertanyaan ini. Ia menghantar pertanyaan ke LLM untuk pemahaman dan secara serentak mencari pangkalan data vektornya untuk senarai hotel yang relevan.

4. **Keputusan Tepat**: LLM membantu menafsirkan hasil carian daripada pangkalan data, mengenal pasti padanan terbaik berdasarkan kriteria "mesra keluarga," "kolam renang," dan "Honolulu," dan kemudian memformat respons bahasa semulajadi. Yang penting, respons merujuk kepada hotel sebenar dari katalog laman web, mengelakkan maklumat direka.

5. **Interaksi Agen AI**: Oleh kerana NLWeb berfungsi sebagai pelayan MCP, agen perjalanan AI luaran juga boleh menyambung ke contoh NLWeb laman web ini. Agen AI boleh menggunakan kaedah `ask` MCP untuk bertanya terus kepada laman web: `ask("Adakah terdapat restoran mesra vegan di kawasan Honolulu yang disyorkan oleh hotel?")`. Contoh NLWeb akan memproses ini, menggunakan pangkalan data maklumat restoran (jika dimuat), dan mengembalikan respons JSON yang terstruktur.

### Ada Soalan Lagi tentang MCP/A2A/NLWeb?

Sertailah [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) untuk berjumpa dengan pelajar lain, menghadiri waktu pejabat dan dapatkan jawapan untuk soalan Agen AI anda.

## Sumber

- [MCP untuk Pemula](https://aka.ms/mcp-for-beginners)  
- [Dokumentasi MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Repositori NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Rangka Kerja Agen Microsoft](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python)

## Pelajaran Sebelumnya

[Agen AI dalam Pengeluaran](../10-ai-agents-production/README.md)

## Pelajaran Seterusnya

[Kejuruteraan Konteks untuk Agen AI](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->