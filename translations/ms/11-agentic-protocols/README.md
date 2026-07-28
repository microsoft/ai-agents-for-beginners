# Menggunakan Protokol Agentik (MCP, A2A dan NLWeb)

[![Agentic Protocols](../../../translated_images/ms/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Klik imej di atas untuk menonton video pelajaran ini)_

Apabila penggunaan ejen AI berkembang, begitu juga keperluan untuk protokol yang memastikan standardisasi, keselamatan, dan menyokong inovasi terbuka. Dalam pelajaran ini, kita akan membincangkan 3 protokol yang bertujuan memenuhi keperluan ini - Model Context Protocol (MCP), Agent to Agent (A2A) dan Natural Language Web (NLWeb).

## Pengenalan

Dalam pelajaran ini, kita akan membincangkan:

• Bagaimana **MCP** membenarkan Ejen AI mengakses alat dan data luaran untuk melengkapkan tugasan pengguna.

• Bagaimana **A2A** membolehkan komunikasi dan kolaborasi antara pelbagai ejen AI.

• Bagaimana **NLWeb** membawa antara muka bahasa semula jadi ke mana-mana laman web membolehkan Ejen AI menemui dan berinteraksi dengan kandungan.

## Matlamat Pembelajaran

• **Kenal pasti** tujuan teras dan manfaat MCP, A2A, dan NLWeb dalam konteks ejen AI.

• **Terangkan** bagaimana setiap protokol memudahkan komunikasi dan interaksi antara LLM, alat, dan ejen lain.

• **Sedar** peranan berbeza yang dimainkan oleh setiap protokol dalam membina sistem agentik yang kompleks.

## Protokol Konteks Model

**Model Context Protocol (MCP)** adalah standard terbuka yang menyediakan cara standard untuk aplikasi memberikan konteks dan alat kepada LLM. Ini membolehkan "penyesuai universal" ke pelbagai sumber data dan alat yang boleh disambungkan oleh Ejen AI dengan cara yang konsisten.

Mari kita lihat komponen MCP, manfaat berbanding penggunaan API langsung, dan contoh bagaimana ejen AI mungkin menggunakan pelayan MCP.

### Komponen Teras MCP

MCP beroperasi pada **arsitektur klien-pelayan** dan komponen teras adalah:

• **Hos** adalah aplikasi LLM (contoh editor kod seperti VSCode) yang memulakan sambungan ke Pelayan MCP.

• **Klien** adalah komponen dalam aplikasi hos yang mengekalkan sambungan satu-dengan-satu dengan pelayan.

• **Pelayan** adalah program ringan yang mendedahkan keupayaan khusus.

Termasuk dalam protokol adalah tiga primitif utama yang merupakan keupayaan Pelayan MCP:

• **Alat**: Ini adalah tindakan atau fungsi tertentu yang boleh dipanggil oleh ejen AI untuk melaksanakan sesuatu tindakan. Contohnya, perkhidmatan cuaca mungkin mendedahkan alat "dapatkan cuaca", atau pelayan e-dagang mungkin mendedahkan alat "beli produk". Pelayan MCP mengiklan nama, penerangan, dan skema input/output setiap alat dalam senarai keupayaan mereka.

• **Sumber**: Ini adalah item data baca sahaja atau dokumen yang boleh disediakan oleh pelayan MCP, dan klien boleh mengambilnya mengikut permintaan. Contohnya termasuk kandungan fail, rekod pangkalan data, atau fail log. Sumber boleh berupa teks (seperti kod atau JSON) atau binari (seperti imej atau PDF).

• **Prompt**: Ini adalah templat yang telah ditetapkan yang menyediakan cadangan prompt, membolehkan aliran kerja yang lebih kompleks.

### Manfaat MCP

MCP menawarkan kelebihan ketara untuk Ejen AI:

• **Penemuan Alat Dinamik**: Ejen boleh secara dinamik menerima senarai alat tersedia dari pelayan bersama penerangan tentang fungsinya. Ini berbeza dengan API tradisional yang sering memerlukan pengkodan statik untuk integrasi, bermakna apa-apa perubahan API perlu dikemaskini kod. MCP menawarkan pendekatan "integrasi sekali", membawa kepelbagaian yang lebih besar.

• **Keserasian Antara LLM**: MCP berfungsi merentas pelbagai LLM, menyediakan fleksibiliti untuk menukar model teras bagi menilai prestasi yang lebih baik.

• **Keselamatan Standard**: MCP termasuk kaedah pengesahan standard, meningkatkan skalabiliti ketika menambah akses ke pelayan MCP tambahan. Ini lebih mudah daripada menguruskan pelbagai kekunci dan jenis pengesahan bagi pelbagai API tradisional.

### Contoh MCP

![MCP Diagram](../../../translated_images/ms/mcp-diagram.e4ca1cbd551444a1.webp)

Bayangkan seorang pengguna ingin menempah penerbangan menggunakan pembantu AI yang dikuasakan oleh MCP.

1. **Sambungan**: Pembantu AI (klien MCP) menyambung ke pelayan MCP yang disediakan oleh syarikat penerbangan.

2. **Penemuan Alat**: Klien bertanya kepada pelayan MCP syarikat penerbangan, "Apa alat yang tersedia?" Pelayan membalas dengan alat seperti "cari penerbangan" dan "tempah penerbangan".

3. **Pemanggilan Alat**: Anda kemudian meminta pembantu AI, "Sila cari penerbangan dari Portland ke Honolulu." Pembantu AI, menggunakan LLM-nya, mengenal pasti bahawa ia perlu memanggil alat "cari penerbangan" dan memberikan parameter berkaitan (asal, destinasi) kepada pelayan MCP.

4. **Pelaksanaan dan Respons**: Pelayan MCP, bertindak sebagai pembungkus, membuat panggilan sebenar ke API tempahan dalaman syarikat penerbangan. Ia kemudian menerima maklumat penerbangan (contoh data JSON) dan menghantarnya kembali kepada pembantu AI.

5. **Interaksi Lanjutan**: Pembantu AI membentangkan pilihan penerbangan. Setelah anda memilih penerbangan, pembantu mungkin memanggil alat "tempah penerbangan" pada pelayan MCP yang sama, melengkapkan tempahan.

## Protokol Ejen-ke-Ejen (A2A)

Sementara MCP menumpukan pada menyambungkan LLM ke alat, **Protokol Agent-to-Agent (A2A)** membawa lebih jauh dengan membolehkan komunikasi dan kolaborasi antara pelbagai ejen AI. A2A menghubungkan ejen AI merentas organisasi, persekitaran dan teknologi untuk melengkapkan tugasan bersama.

Kita akan meneliti komponen dan manfaat A2A, serta contoh bagaimana ia boleh diaplikasikan dalam aplikasi perjalanan kita.

### Komponen Teras A2A

A2A menumpukan pada membolehkan komunikasi antara ejen dan bekerjasama melengkapkan sub-tugasan pengguna. Setiap komponen protokol menyumbang kepada ini:

#### Kad Ejen

Serupa dengan bagaimana pelayan MCP berkongsi senarai alat, Kad Ejen mempunyai:
- Nama Ejen.
- **penerangan tugasan umum** yang diselesaikan.
- **senarai kemahiran khusus** dengan penerangan untuk membantu ejen lain (atau pengguna manusia) memahami bila dan kenapa mereka ingin memanggil ejen tersebut.
- **URL Titik Akhir semasa** ejen tersebut
- **versi** dan **keupayaan** ejen seperti balasan penstriman dan pemberitahuan push.

#### Pelaksana Ejen

Pelaksana Ejen bertanggungjawab untuk **menyerahkan konteks sembang pengguna kepada ejen jauh**, ejen jauh memerlukan ini untuk memahami tugasan yang perlu dilengkapkan. Dalam pelayan A2A, ejen menggunakan model bahasa besar (LLM) sendiri untuk menganalisis permintaan masuk dan melaksanakan tugasan menggunakan alat dalaman sendiri.

#### Artifak

Setelah ejen jauh menyelesaikan tugasan yang diminta, hasil kerjanya dibuat sebagai artifak. Artifak **mengandungi hasil kerja ejen**, **penerangan apa yang diselesaikan**, dan **konteks teks** yang dihantar melalui protokol. Setelah artifak dihantar, sambungan dengan ejen jauh ditutup sehingga diperlukan lagi.

#### Antrian Acara

Komponen ini digunakan untuk **mengendalikan kemas kini dan penghantaran mesej**. Ia sangat penting dalam produksi bagi sistem agentik untuk mengelakkan sambungan antara ejen ditutup sebelum tugasan selesai, terutamanya apabila masa penyelesaian tugasan boleh mengambil masa lebih lama.

### Manfaat A2A

• **Kolaborasi Dipertingkatkan**: Ia membolehkan ejen dari vendor dan platform berbeza untuk berinteraksi, berkongsi konteks, dan bekerja bersama, memudahkan automasi lancar merentas sistem yang biasanya terpisah.

• **Fleksibiliti Pemilihan Model**: Setiap ejen A2A boleh memilih LLM yang digunakannya untuk melayani permintaan, membolehkan model yang dioptimumkan atau ditala khusus per ejen, berbeza dengan sambungan LLM tunggal dalam beberapa senario MCP.

• **Pengesahan Terbina Dalam**: Pengesahan disepadukan terus dalam protokol A2A, menyediakan rangka kerja keselamatan yang kukuh untuk interaksi ejen.

### Contoh A2A

![A2A Diagram](../../../translated_images/ms/A2A-Diagram.8666928d648acc26.webp)

Mari kita kembangkan senario tempahan perjalanan kita, kali ini menggunakan A2A.

1. **Permintaan Pengguna ke Multi-Ejen**: Pengguna berinteraksi dengan "Ejen Perjalanan" klien/ejen A2A, mungkin dengan berkata, "Sila tempah semua perjalanan ke Honolulu minggu depan, termasuk penerbangan, hotel, dan kereta sewa".

2. **Orkestrasi oleh Ejen Perjalanan**: Ejen Perjalanan menerima permintaan kompleks ini. Ia menggunakan LLMnya untuk berfikir tentang tugasan dan menentukan bahawa ia perlu berinteraksi dengan ejen khusus lain.

3. **Komunikasi Antara Ejen**: Ejen Perjalanan kemudian menggunakan protokol A2A untuk menyambung ke ejen hiliran, seperti “Ejen Syarikat Penerbangan,” “Ejen Hotel,” dan “Ejen Sewa Kereta” yang dicipta oleh syarikat berbeza.

4. **Pelaksanaan Tugasan Didelegasi**: Ejen Perjalanan menghantar tugasan khusus kepada ejen pakar ini (contoh, "Cari penerbangan ke Honolulu," "Tempah hotel," "Sewa kereta"). Setiap ejen khusus ini, yang menjalankan LLM dan menggunakan alat sendiri (yang mungkin juga pelayan MCP), melaksanakan bahagian tempahan khusus mereka.

5. **Respons Disatukan**: Setelah semua ejen hiliran menyelesaikan tugasan mereka, Ejen Perjalanan mengumpul hasil (butiran penerbangan, pengesahan hotel, tempahan sewa kereta) dan menghantar respons gaya sembang yang lengkap kembali kepada pengguna.

## Web Bahasa Semula Jadi (NLWeb)

Laman web telah lama menjadi cara utama bagi pengguna mengakses maklumat dan data di seluruh internet.

Mari kita lihat komponen berbeza NLWeb, manfaat NLWeb dan contoh cara NLWeb berfungsi dengan melihat aplikasi perjalanan kita.

### Komponen NLWeb

- **Aplikasi NLWeb (Kod Perkhidmatan Teras)**: Sistem yang memproses soalan bahasa semula jadi. Ia menyambungkan bahagian berbeza platform untuk mencipta respons. Boleh dianggap sebagai **enjin yang menggerakkan ciri bahasa semula jadi** laman web.

- **Protokol NLWeb**: Ini adalah **set asas peraturan untuk interaksi bahasa semula jadi** dengan laman web. Ia menghantar kembali respons dalam format JSON (sering menggunakan Schema.org). Tujuannya adalah untuk mewujudkan asas mudah untuk "Web AI," sama seperti HTML membolehkan perkongsian dokumen dalam talian.

- **Pelayan MCP (Titik Akhir Model Context Protocol)**: Setiap persediaan NLWeb juga berfungsi sebagai **pelayan MCP**. Ini bermakna ia boleh **berkongsi alat (seperti kaedah "ask") dan data** dengan sistem AI lain. Dalam praktik, ini menjadikan kandungan dan kemampuan laman web boleh digunakan oleh ejen AI, membolehkan laman menjadi sebahagian daripada "ekosistem ejen" yang lebih luas.

- **Model Embedding**: Model ini digunakan untuk **menukar kandungan laman web menjadi representasi numerik yang dipanggil vektor** (embedding). Vektor ini menangkap makna dengan cara yang boleh dibanding dan dicari oleh komputer. Ia disimpan dalam pangkalan data khas, dan pengguna boleh memilih model embedding yang mereka mahu gunakan.

- **Pangkalan Data Vektor (Mekanisme Pengambilan)**: Pangkalan data ini **menyimpan embeddings kandungan laman web**. Apabila seseorang bertanya soalan, NLWeb memeriksa pangkalan data vektor untuk dengan cepat mencari maklumat paling relevan. Ia memberikan senarai jawapan berpotensi dengan pantas, disusun mengikut persamaan. NLWeb bekerja dengan pelbagai sistem penyimpanan vektor seperti Qdrant, Snowflake, Milvus, Azure AI Search, dan Elasticsearch.

### NLWeb melalui Contoh

![NLWeb](../../../translated_images/ms/nlweb-diagram.c1e2390b310e5fe4.webp)

Pertimbangkan laman tempahan perjalanan kita lagi, kali ini ia dikuasakan oleh NLWeb.

1. **Pengambilan Data**: Katalog produk laman perjalanan sedia ada (contoh, senarai penerbangan, penerangan hotel, pakej pelancongan) diformat menggunakan Schema.org atau dimuat melalui RSS feed. Alat NLWeb mengambil data berstruktur ini, mencipta embeddings, dan menyimpannya dalam pangkalan data vektor tempatan atau jauh.

2. **Pertanyaan Bahasa Semula Jadi (Manusia)**: Pengguna melawat laman web dan, bukannya menavigasi menu, menaip ke dalam antara muka sembang: "Cari hotel mesra keluarga di Honolulu dengan kolam renang untuk minggu depan".

3. **Pemprosesan NLWeb**: Aplikasi NLWeb menerima pertanyaan ini. Ia menghantar pertanyaan kepada LLM untuk pemahaman dan serentak mencari pangkalan data vektor untuk senarai hotel yang relevan.

4. **Keputusan Tepat**: LLM membantu mentafsir keputusan carian dari pangkalan data, mengenal pasti padanan terbaik berdasarkan kriteria "mesra keluarga", "kolam renang," dan "Honolulu," kemudian memformat respons bahasa semula jadi. Penting, respons merujuk kepada hotel sebenar dari katalog laman, mengelakkan maklumat rekaan.

5. **Interaksi Ejen AI**: Oleh kerana NLWeb berfungsi sebagai pelayan MCP, ejen perjalanan AI luaran juga boleh menyambung ke instance NLWeb laman web ini. Ejen AI boleh menggunakan kaedah `ask` MCP untuk bertanya terus ke laman web: `ask("Adakah terdapat restoran mesra vegan di kawasan Honolulu yang disyorkan oleh hotel?")`. Instance NLWeb akan memproses ini, menggunakan pangkalan data maklumat restoran (jika dimuatkan), dan mengembalikan respons JSON berstruktur.

### Ada Soalan Lagi tentang MCP/A2A/NLWeb?

Sertai [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) untuk bertemu pembelajar lain, menghadiri waktu pejabat dan dapatkan jawapan untuk soalan tentang AI Agents anda.

## Sumber

- [MCP untuk Pemula](https://aka.ms/mcp-for-beginners)  
- [Dokumentasi MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Repositori NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framework)

## Pelajaran Sebelumnya

[Ejen AI dalam Pengeluaran](../10-ai-agents-production/README.md)

## Pelajaran Seterusnya

[Konteks Kejuruteraan untuk Ejen AI](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->