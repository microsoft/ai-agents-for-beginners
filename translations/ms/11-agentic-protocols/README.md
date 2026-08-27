# Menggunakan Protokol Agentik (MCP, A2A dan NLWeb)

[![Protokol Agentik](../../../translated_images/ms/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Klik imej di atas untuk menonton video pelajaran ini)_

Semakin berkembang penggunaan agen AI, semakin meningkat keperluan protokol yang memastikan standardisasi, keselamatan, dan menyokong inovasi terbuka. Dalam pelajaran ini, kami akan membincangkan 3 protokol yang bertujuan memenuhi keperluan ini - Model Context Protocol (MCP), Agent to Agent (A2A) dan Natural Language Web (NLWeb).

## Pengenalan

Dalam pelajaran ini, kita akan membincangkan:

• Bagaimana **MCP** membolehkan Agen AI mengakses alat dan data luaran untuk menyelesaikan tugasan pengguna.

• Bagaimana **A2A** membolehkan komunikasi dan kerjasama antara agen AI yang berbeza.

• Bagaimana **NLWeb** membawa antara muka bahasa semula jadi kepada mana-mana laman web membolehkan Agen AI menemui dan berinteraksi dengan kandungan.

## Matlamat Pembelajaran

• **Kenal pasti** tujuan utama dan manfaat MCP, A2A, dan NLWeb dalam konteks agen AI.

• **Terangkan** bagaimana setiap protokol memudahkan komunikasi dan interaksi antara LLM, alat, dan agen lain.

• **Kenali** peranan berbeza yang dimainkan oleh setiap protokol dalam membina sistem agentik yang kompleks.

## Model Context Protocol

**Model Context Protocol (MCP)** ialah satu standard terbuka yang menyediakan cara piawai untuk aplikasi menyediakan konteks dan alat kepada LLM. Ini membolehkan "penyesuai universal" untuk pelbagai sumber data dan alat yang boleh disambungkan oleh Agen AI secara konsisten.

Mari kita lihat komponen MCP, manfaat berbanding penggunaan API terus, dan contoh bagaimana agen AI mungkin menggunakan pelayan MCP.

### Komponen Teras MCP

MCP beroperasi pada **senibina klien-pelayan** dan komponen terasnya adalah:

• **Hos** ialah aplikasi LLM (contohnya penyunting kod seperti VSCode) yang memulakan sambungan ke Pelayan MCP.

• **Klien** adalah komponen dalam aplikasi hos yang mengekalkan sambungan satu-ke-satu dengan pelayan.

• **Pelayan** adalah program ringan yang mendedahkan kebolehan tertentu.

Termasuk dalam protokol adalah tiga primitif teras yang merupakan kebolehan Pelayan MCP:

• **Alat**: Tindakan atau fungsi khusus yang boleh dipanggil oleh agen AI untuk melakukan tindakan. Contohnya, perkhidmatan cuaca mungkin mendedahkan alat "dapatkan cuaca", atau pelayan e-dagang mungkin mendedahkan alat "beli produk". Pelayan MCP mengiklan nama, penerangan, dan skema input/output setiap alat dalam senarai kebolehannya.

• **Sumber**: Item data atau dokumen yang boleh dibaca sahaja yang boleh disediakan oleh pelayan MCP, dan klien boleh memperolehnya atas permintaan. Contohnya termasuk kandungan fail, rekod pangkalan data, atau fail log. Sumber boleh berupa teks (seperti kod atau JSON) atau binari (seperti imej atau PDF).

• **Prompts**: Templet yang telah ditetapkan yang menyediakan cadangan prompt, membolehkan aliran kerja yang lebih kompleks.

### Manfaat MCP

MCP menawarkan kelebihan signifikan untuk Agen AI:

• **Penemuan Alat Dinamik**: Agen boleh menerima secara dinamik senarai alat yang tersedia daripada pelayan beserta penerangan tentang fungsinya. Ini berbeza dengan API tradisional, yang sering memerlukan pengkodan statik untuk integrasi, bermakna sebarang perubahan API memerlukan kemas kini kod. MCP menawarkan pendekatan "integrasi sekali", membawa kepada lebih kebolehsuaian.

• **Interoperabiliti Rentas LLM**: MCP berfungsi merentas LLM berbeza, memberikan fleksibiliti untuk bertukar model teras untuk penilaian prestasi lebih baik.

• **Keselamatan Piawai**: MCP termasuk kaedah pengesahan piawai, meningkatkan skala apabila menambah akses ke pelayan MCP tambahan. Ini lebih mudah daripada mengurus pelbagai kekunci dan jenis pengesahan untuk API tradisional yang berlainan.

### Contoh MCP

![Rajah MCP](../../../translated_images/ms/mcp-diagram.e4ca1cbd551444a1.webp)

Bayangkan pengguna ingin menempah penerbangan menggunakan pembantu AI yang dikuasakan oleh MCP.

1. **Sambungan**: Pembantu AI (klien MCP) menyambung ke pelayan MCP yang disediakan oleh syarikat penerbangan.

2. **Penemuan Alat**: Klien bertanya kepada pelayan MCP syarikat penerbangan, "Alat apa yang anda ada?" Pelayan membalas dengan alat seperti "cari penerbangan" dan "tempah penerbangan".

3. **Pemanggilan Alat**: Anda kemudian meminta pembantu AI, "Sila cari penerbangan dari Portland ke Honolulu." Pembantu AI, menggunakan LLMnya, mengenal pasti ia perlu memanggil alat "cari penerbangan" dan menghantar parameter berkaitan (asal, destinasi) ke pelayan MCP.

4. **Pelaksanaan dan Respons**: Pelayan MCP, bertindak sebagai pembalut, membuat panggilan sebenar ke API tempahan dalaman syarikat penerbangan. Kemudian menerima maklumat penerbangan (contohnya, data JSON) dan menghantarnya kembali ke pembantu AI.

5. **Interaksi Lanjutan**: Pembantu AI memaparkan pilihan penerbangan. Setelah anda memilih penerbangan, pembantu mungkin memanggil alat "tempah penerbangan" pada pelayan MCP yang sama, menyiapkan tempahan.

## Protokol Agen-ke-Agen (A2A)

Walaupun MCP memberi tumpuan kepada menyambung LLM ke alat, **Protokol Agent-to-Agent (A2A)** mengambil langkah lebih jauh dengan membolehkan komunikasi dan kerjasama antara agen AI yang berbeza. A2A menghubungkan agen AI merentas organisasi, persekitaran dan tumpukan teknologi berbeza untuk menyelesaikan tugasan bersama.

Kita akan mengkaji komponen dan kelebihan A2A, bersama contoh bagaimana ia boleh digunakan dalam aplikasi pelancongan kita.

### Komponen Teras A2A

A2A menumpukan pada membolehkan komunikasi antara agen dan membolehkan mereka bekerjasama menyelesaikan sub-tugasan pengguna. Setiap komponen protokol menyumbang kepada ini:

#### Kad Agen

Sama seperti bagaimana pelayan MCP berkongsi senarai alat, Kad Agen mempunyai:
- Nama Agen.
- **penerangan tentang tugasan umum** yang dilaksanakannya.
- **senarai kemahiran khusus** dengan penerangan untuk membantu agen lain (atau pengguna manusia) memahami bila dan mengapa mereka ingin memanggil agen itu.
- **URL Penamat semasa** agen.
- **versi** dan **kebolehan** agen seperti respons penstriman dan pemberitahuan tolak.

#### Pelaksana Agen

Pelaksana Agen bertanggungjawab untuk **menyampaikan konteks sembang pengguna kepada agen jauh**, agen jauh memerlukannya untuk memahami tugasan yang perlu diselesaikan. Dalam pelayan A2A, agen menggunakan Model Bahasa Besarnya (LLM) sendiri untuk mengurai permintaan masuk dan melaksanakan tugasan menggunakan alat dalaman mereka sendiri.

#### Artifak

Setelah agen jauh selesai tugasan diminta, hasil kerja itu dibuat sebagai artifak. Artifak **mengandungi hasil kerja agen**, **penerangan apa yang telah diselesaikan**, dan **konteks teks** yang dihantar melalui protokol. Setelah artifak dihantar, sambungan dengan agen jauh ditutup sehingga diperlukan semula.

#### Antrian Acara

Komponen ini digunakan untuk **mengendalikan kemas kini dan menghantar mesej**. Ia sangat penting dalam pengeluaran untuk sistem agentik bagi mengelakkan sambungan antara agen ditutup sebelum tugasan selesai, terutama apabila masa penyelesaian tugasan boleh mengambil masa lama.

### Manfaat A2A

• **Kerjasama Dipertingkatkan**: Ia membolehkan agen dari vendor dan platform berbeza berinteraksi, berkongsi konteks, dan bekerjasama, memudahkan automasi lancar merentas sistem yang biasa tidak bersambung.

• **Fleksibiliti Pemilihan Model**: Setiap agen A2A boleh memilih LLM yang digunakannya untuk melayani permintaan, membenarkan model yang dioptimumkan atau ditala khas per agen, berbeza dengan sambungan LLM tunggal dalam beberapa senario MCP.

• **Pengesahan Terbina Dalam**: Pengesahan diintegrasikan terus ke dalam protokol A2A, menyediakan rangka kerja keselamatan kukuh untuk interaksi agen.

### Contoh A2A

![Rajah A2A](../../../translated_images/ms/A2A-Diagram.8666928d648acc26.webp)

Mari kita kembangkan senario tempahan pelancongan kita, tetapi kali ini menggunakan A2A.

1. **Permintaan Pengguna ke Multi-Agen**: Pengguna berinteraksi dengan klien/agen A2A "Ejen Pelancongan", mungkin dengan berkata, "Sila tempah keseluruhan perjalanan ke Honolulu untuk minggu depan, termasuk penerbangan, hotel, dan kereta sewa".

2. **Orkestrasi oleh Ejen Pelancongan**: Ejen Pelancongan menerima permintaan kompleks ini. Ia menggunakan LLM-nya untuk berfikir tentang tugasan dan menentukan bahawa ia perlu berinteraksi dengan agen khusus lain.

3. **Komunikasi Antara Agen**: Ejen Pelancongan kemudian menggunakan protokol A2A untuk menyambung ke agen hiliran, seperti "Ejen Syarikat Penerbangan", "Ejen Hotel", dan "Ejen Kereta Sewa" yang dibina oleh syarikat berbeza.

4. **Pelaksanaan Tugasan yang Didelegasikan**: Ejen Pelancongan menghantar tugasan tertentu kepada agen khusus ini (contohnya, "Cari penerbangan ke Honolulu," "Tempah hotel," "Sewa kereta"). Setiap agen khusus ini, menjalankan LLM sendiri dan menggunakan alat mereka (yang mungkin juga pelayan MCP), melaksanakan bahagian tempahannya.

5. **Respons Disatukan**: Setelah semua agen hiliran selesai tugasan mereka, Ejen Pelancongan mengumpul hasil (butiran penerbangan, pengesahan hotel, tempahan kereta sewa) dan menghantar respons berbentuk sembang kepada pengguna.

## Natural Language Web (NLWeb)

Laman web telah lama menjadi cara utama untuk pengguna mengakses maklumat dan data di internet.

Mari lihat komponen berbeza NLWeb, manfaat NLWeb dan contoh bagaimana NLWeb berfungsi dengan melihat aplikasi pelancongan kita.

### Komponen NLWeb

- **Aplikasi NLWeb (Kod Perkhidmatan Teras)**: Sistem yang memproses soalan bahasa semula jadi. Ia menghubungkan bahagian platform yang berbeza untuk mencipta respons. Anda boleh fikirkan ia sebagai **enjin yang menggerakkan ciri bahasa semula jadi** laman web.

- **Protokol NLWeb**: Ini ialah **set asas peraturan untuk interaksi bahasa semula jadi** dengan laman web. Ia menghantar balik respons dalam format JSON (sering menggunakan Schema.org). Tujuannya adalah untuk mewujudkan asas mudah bagi “Web AI,” sama seperti HTML membolehkan perkongsian dokumen secara online.

- **Pelayan MCP (Penamat Protokol Model Context)**: Setiap penyediaan NLWeb juga berfungsi sebagai **pelayan MCP**. Ini bermakna ia boleh **berkongsi alat (seperti kaedah “ask”) dan data** dengan sistem AI lain. Dalam praktiknya, ini menjadikan kandungan dan kebolehan laman web boleh digunakan oleh agen AI, membolehkan laman itu menjadi sebahagian daripada “ekosistem agen” yang lebih luas.

- **Model Embedding**: Model ini digunakan untuk **menukar kandungan laman web menjadi perwakilan berangka yang dipanggil vektor** (embedding). Vektor ini menangkap makna dalam cara yang komputer boleh banding dan cari. Ia disimpan dalam pangkalan data khas, dan pengguna boleh memilih model embedding yang mahu digunakan.

- **Pangkalan Data Vektor (Mekanisme Pengambilan)**: Pangkalan data ini **menyimpan embedding kandungan laman web**. Apabila seseorang bertanya soalan, NLWeb menyemak pangkalan data vektor untuk mencari maklumat paling relevan dengan cepat. Ia memberi senarai pantas jawapan yang mungkin, di susun mengikut kesamaan. NLWeb bekerjasama dengan sistem simpanan vektor seperti Qdrant, Snowflake, Milvus, Azure AI Search, dan Elasticsearch.

### NLWeb melalui Contoh

![NLWeb](../../../translated_images/ms/nlweb-diagram.c1e2390b310e5fe4.webp)

Pertimbangkan laman web tempahan pelancongan kita sekali lagi, tetapi kali ini, ia dikuasakan oleh NLWeb.

1. **Pengambilan Data**: Katalog produk sedia ada laman pelancongan (contohnya, senarai penerbangan, penerangan hotel, pakej pelancongan) diformat menggunakan Schema.org atau dimuatkan melalui suapan RSS. Alat NLWeb mengambil data berstruktur ini, membuat embeddings, dan menyimpannya dalam pangkalan data vektor tempatan atau jauh.

2. **Pertanyaan Bahasa Semula Jadi (Manusia)**: Pengguna melawat laman web dan, bukannya melayari menu, menaip dalam antara muka sembang: "Cari hotel mesra keluarga di Honolulu dengan kolam renang untuk minggu depan".

3. **Pemprosesan NLWeb**: Aplikasi NLWeb menerima pertanyaan ini. Ia menghantar pertanyaan ke LLM untuk memahami dan serentak mencari pangkalan data vektor terhadap senarai hotel yang relevan.

4. **Keputusan Tepat**: LLM membantu mentafsir keputusan carian dari pangkalan data, mengenal pasti padanan terbaik berdasarkan kriteria "mesra keluarga," "kolam renang," dan "Honolulu," kemudian memformat respons dalam bahasa semula jadi. Yang penting, respons merujuk hotel sebenar dari katalog laman, mengelakkan maklumat rekaan.

5. **Interaksi Agen AI**: Oleh kerana NLWeb berfungsi sebagai pelayan MCP, agen pelancongan AI luar juga boleh menyambung ke instans NLWeb laman ini. Agen AI boleh menggunakan kaedah `ask` MCP untuk bertanya terus kepada laman web: `ask("Adakah terdapat restoran mesra vegan di kawasan Honolulu yang disyorkan oleh hotel?")`. Instans NLWeb akan memproses ini, menggunakan pangkalan data maklumat restoran (jika dimuatkan), dan memberikan respons JSON berstruktur.

### Ada Lebih Banyak Soalan tentang MCP/A2A/NLWeb?

Sertai [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) untuk bertemu dengan pelajar lain, menghadiri waktu pejabat dan mendapatkan jawapan untuk soalan Agen AI anda.

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