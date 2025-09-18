<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aff92c6f019b4627ca9399c6e3882e17",
  "translation_date": "2025-09-18T15:19:41+00:00",
  "source_file": "11-agentic-protocols/README.md",
  "language_code": "ms"
}
-->
# Menggunakan Protokol Agen (MCP, A2A dan NLWeb)

[![Protokol Agen](../../../translated_images/lesson-11-thumbnail.b6c742949cf1ce2aa0255968d287b31c99b51dfa9c9beaede7c3fbed90e8fcfb.ms.png)](https://youtu.be/X-Dh9R3Opn8)

> _(Klik imej di atas untuk menonton video pelajaran ini)_

Dengan peningkatan penggunaan agen AI, keperluan untuk protokol yang memastikan penyeragaman, keselamatan, dan menyokong inovasi terbuka juga meningkat. Dalam pelajaran ini, kita akan membincangkan 3 protokol yang bertujuan memenuhi keperluan ini - Model Context Protocol (MCP), Agent to Agent (A2A) dan Natural Language Web (NLWeb).

## Pengenalan

Dalam pelajaran ini, kita akan membincangkan:

• Bagaimana **MCP** membolehkan agen AI mengakses alat dan data luaran untuk menyelesaikan tugas pengguna.

• Bagaimana **A2A** memudahkan komunikasi dan kerjasama antara agen AI yang berbeza.

• Bagaimana **NLWeb** membawa antara muka bahasa semula jadi ke mana-mana laman web, membolehkan agen AI menemui dan berinteraksi dengan kandungan.

## Matlamat Pembelajaran

• **Kenal pasti** tujuan utama dan manfaat MCP, A2A, dan NLWeb dalam konteks agen AI.

• **Terangkan** bagaimana setiap protokol memudahkan komunikasi dan interaksi antara LLM, alat, dan agen lain.

• **Kenali** peranan unik setiap protokol dalam membina sistem agen yang kompleks.

## Model Context Protocol

**Model Context Protocol (MCP)** adalah standard terbuka yang menyediakan cara seragam untuk aplikasi memberikan konteks dan alat kepada LLM. Ini membolehkan "penyesuai universal" untuk sumber data dan alat yang berbeza yang boleh dihubungkan oleh agen AI dengan cara yang konsisten.

Mari kita lihat komponen MCP, manfaat berbanding penggunaan API langsung, dan contoh bagaimana agen AI mungkin menggunakan pelayan MCP.

### Komponen Teras MCP

MCP beroperasi pada **senibina klien-pelayan** dan komponen terasnya adalah:

• **Hosts** adalah aplikasi LLM (contohnya editor kod seperti VSCode) yang memulakan sambungan ke pelayan MCP.

• **Clients** adalah komponen dalam aplikasi host yang mengekalkan sambungan satu-ke-satu dengan pelayan.

• **Servers** adalah program ringan yang mendedahkan keupayaan tertentu.

Termasuk dalam protokol adalah tiga primitif teras yang merupakan keupayaan pelayan MCP:

• **Tools**: Ini adalah tindakan atau fungsi diskret yang boleh dipanggil oleh agen AI untuk melaksanakan tindakan. Contohnya, perkhidmatan cuaca mungkin mendedahkan alat "dapatkan cuaca", atau pelayan e-dagang mungkin mendedahkan alat "beli produk". Pelayan MCP mengiklankan nama, deskripsi, dan skema input/output setiap alat dalam senarai keupayaan mereka.

• **Resources**: Ini adalah item data atau dokumen yang hanya boleh dibaca yang boleh disediakan oleh pelayan MCP, dan klien boleh mengambilnya atas permintaan. Contohnya termasuk kandungan fail, rekod pangkalan data, atau fail log. Sumber boleh berupa teks (seperti kod atau JSON) atau binari (seperti imej atau PDF).

• **Prompts**: Ini adalah templat yang telah ditentukan yang menyediakan cadangan prompt, membolehkan aliran kerja yang lebih kompleks.

### Manfaat MCP

MCP menawarkan kelebihan yang ketara untuk agen AI:

• **Penemuan Alat Dinamik**: Agen boleh menerima senarai alat yang tersedia dari pelayan secara dinamik bersama dengan deskripsi tentang apa yang mereka lakukan. Ini berbeza dengan API tradisional, yang sering memerlukan pengkodan statik untuk integrasi, bermakna sebarang perubahan API memerlukan kemas kini kod. MCP menawarkan pendekatan "integrasi sekali", yang membawa kepada penyesuaian yang lebih besar.

• **Interoperabiliti Merentas LLM**: MCP berfungsi merentas LLM yang berbeza, memberikan fleksibiliti untuk menukar model teras untuk menilai prestasi yang lebih baik.

• **Keselamatan Standard**: MCP termasuk kaedah pengesahan standard, meningkatkan skalabiliti apabila menambah akses kepada pelayan MCP tambahan. Ini lebih mudah daripada menguruskan kunci dan jenis pengesahan yang berbeza untuk pelbagai API tradisional.

### Contoh MCP

![Rajah MCP](../../../translated_images/mcp-diagram.e4ca1cbd551444a12e1f0eb300191a036ab01124fce71c864fe9cb7f4ac2a15d.ms.png)

Bayangkan seorang pengguna ingin menempah penerbangan menggunakan pembantu AI yang dikuasakan oleh MCP.

1. **Sambungan**: Pembantu AI (klien MCP) menyambung ke pelayan MCP yang disediakan oleh syarikat penerbangan.

2. **Penemuan Alat**: Klien bertanya kepada pelayan MCP syarikat penerbangan, "Alat apa yang anda ada?" Pelayan menjawab dengan alat seperti "cari penerbangan" dan "tempah penerbangan".

3. **Pemanggilan Alat**: Anda kemudian meminta pembantu AI, "Sila cari penerbangan dari Portland ke Honolulu." Pembantu AI, menggunakan LLM-nya, mengenal pasti bahawa ia perlu memanggil alat "cari penerbangan" dan menghantar parameter yang relevan (asal, destinasi) kepada pelayan MCP.

4. **Pelaksanaan dan Respons**: Pelayan MCP, bertindak sebagai pembungkus, membuat panggilan sebenar kepada API tempahan dalaman syarikat penerbangan. Ia kemudian menerima maklumat penerbangan (contohnya, data JSON) dan menghantarnya kembali kepada pembantu AI.

5. **Interaksi Lanjutan**: Pembantu AI menyampaikan pilihan penerbangan. Setelah anda memilih penerbangan, pembantu mungkin memanggil alat "tempah penerbangan" pada pelayan MCP yang sama, menyelesaikan tempahan.

## Protokol Agent-to-Agent (A2A)

Sementara MCP memberi tumpuan kepada menghubungkan LLM kepada alat, **Protokol Agent-to-Agent (A2A)** melangkah lebih jauh dengan membolehkan komunikasi dan kerjasama antara agen AI yang berbeza. A2A menghubungkan agen AI merentas organisasi, persekitaran, dan teknologi untuk menyelesaikan tugas bersama.

Kita akan mengkaji komponen dan manfaat A2A, bersama dengan contoh bagaimana ia boleh digunakan dalam aplikasi perjalanan kita.

### Komponen Teras A2A

A2A memberi tumpuan kepada membolehkan komunikasi antara agen dan membolehkan mereka bekerjasama untuk menyelesaikan subtugas pengguna. Setiap komponen protokol menyumbang kepada ini:

#### Kad Agen

Serupa dengan bagaimana pelayan MCP berkongsi senarai alat, Kad Agen mempunyai:
- Nama Agen.
- **Deskripsi tugas umum** yang diselesaikannya.
- **Senarai kemahiran khusus** dengan deskripsi untuk membantu agen lain (atau bahkan pengguna manusia) memahami bila dan mengapa mereka ingin memanggil agen tersebut.
- **URL Endpoint semasa** agen.
- **Versi** dan **keupayaan** agen seperti respons streaming dan pemberitahuan push.

#### Pelaksana Agen

Pelaksana Agen bertanggungjawab untuk **menyampaikan konteks perbualan pengguna kepada agen jauh**, agen jauh memerlukan ini untuk memahami tugas yang perlu diselesaikan. Dalam pelayan A2A, agen menggunakan Model Bahasa Besar (LLM) sendiri untuk menganalisis permintaan masuk dan melaksanakan tugas menggunakan alat dalaman mereka sendiri.

#### Artefak

Setelah agen jauh menyelesaikan tugas yang diminta, hasil kerjanya dicipta sebagai artefak. Artefak **mengandungi hasil kerja agen**, **deskripsi tentang apa yang telah diselesaikan**, dan **konteks teks** yang dihantar melalui protokol. Setelah artefak dihantar, sambungan dengan agen jauh ditutup sehingga ia diperlukan lagi.

#### Barisan Acara

Komponen ini digunakan untuk **mengendalikan kemas kini dan menyampaikan mesej**. Ia amat penting dalam pengeluaran untuk sistem agenik untuk mengelakkan sambungan antara agen daripada ditutup sebelum tugas selesai, terutamanya apabila masa penyelesaian tugas boleh mengambil masa yang lebih lama.

### Manfaat A2A

• **Kerjasama Dipertingkatkan**: Ia membolehkan agen dari vendor dan platform yang berbeza berinteraksi, berkongsi konteks, dan bekerjasama, memudahkan automasi lancar merentas sistem yang secara tradisional terputus.

• **Fleksibiliti Pemilihan Model**: Setiap agen A2A boleh memutuskan model LLM yang digunakan untuk melayani permintaannya, membolehkan model yang dioptimumkan atau disesuaikan untuk setiap agen, tidak seperti sambungan LLM tunggal dalam beberapa senario MCP.

• **Pengesahan Terbina Dalam**: Pengesahan diintegrasikan terus ke dalam protokol A2A, menyediakan rangka kerja keselamatan yang kukuh untuk interaksi agen.

### Contoh A2A

![Rajah A2A](../../../translated_images/A2A-Diagram.8666928d648acc2687db4093d7b09ea2a595622f8fe18194a026ee55fc23af8e.ms.png)

Mari kita kembangkan senario tempahan perjalanan kita, tetapi kali ini menggunakan A2A.

1. **Permintaan Pengguna kepada Multi-Agen**: Seorang pengguna berinteraksi dengan "Agen Perjalanan" klien/agen A2A, mungkin dengan mengatakan, "Sila tempah perjalanan lengkap ke Honolulu untuk minggu depan, termasuk penerbangan, hotel, dan kereta sewa."

2. **Orkestrasi oleh Agen Perjalanan**: Agen Perjalanan menerima permintaan kompleks ini. Ia menggunakan LLM-nya untuk membuat keputusan tentang tugas dan menentukan bahawa ia perlu berinteraksi dengan agen khusus lain.

3. **Komunikasi Antara Agen**: Agen Perjalanan kemudian menggunakan protokol A2A untuk menyambung kepada agen hiliran, seperti "Agen Syarikat Penerbangan," "Agen Hotel," dan "Agen Kereta Sewa" yang dicipta oleh syarikat yang berbeza.

4. **Pelaksanaan Tugas yang Didelegasikan**: Agen Perjalanan menghantar tugas khusus kepada agen khusus ini (contohnya, "Cari penerbangan ke Honolulu," "Tempah hotel," "Sewa kereta"). Setiap agen khusus ini, menjalankan LLM mereka sendiri dan menggunakan alat mereka sendiri (yang mungkin pelayan MCP sendiri), melaksanakan bahagian khusus tempahan mereka.

5. **Respons Terkonsolidasi**: Setelah semua agen hiliran menyelesaikan tugas mereka, Agen Perjalanan menyusun hasilnya (butiran penerbangan, pengesahan hotel, tempahan kereta sewa) dan menghantar respons gaya perbualan yang komprehensif kembali kepada pengguna.

## Natural Language Web (NLWeb)

Laman web telah lama menjadi cara utama bagi pengguna untuk mengakses maklumat dan data di seluruh internet.

Mari kita lihat komponen NLWeb yang berbeza, manfaat NLWeb dan contoh bagaimana NLWeb berfungsi dengan melihat aplikasi perjalanan kita.

### Komponen NLWeb

- **Aplikasi NLWeb (Kod Perkhidmatan Teras)**: Sistem yang memproses soalan bahasa semula jadi. Ia menghubungkan bahagian-bahagian platform yang berbeza untuk mencipta respons. Anda boleh menganggapnya sebagai **enjin yang menggerakkan ciri bahasa semula jadi** laman web.

- **Protokol NLWeb**: Ini adalah **set peraturan asas untuk interaksi bahasa semula jadi** dengan laman web. Ia menghantar respons dalam format JSON (sering menggunakan Schema.org). Tujuannya adalah untuk mencipta asas mudah untuk "AI Web," sama seperti HTML memungkinkan perkongsian dokumen dalam talian.

- **Pelayan MCP (Endpoint Model Context Protocol)**: Setiap tetapan NLWeb juga berfungsi sebagai **pelayan MCP**. Ini bermakna ia boleh **berkongsi alat (seperti kaedah "tanya") dan data** dengan sistem AI lain. Dalam praktiknya, ini menjadikan kandungan dan keupayaan laman web boleh digunakan oleh agen AI, membolehkan laman web menjadi sebahagian daripada "ekosistem agen" yang lebih luas.

- **Model Embedding**: Model ini digunakan untuk **menukar kandungan laman web kepada representasi berangka yang dipanggil vektor** (embedding). Vektor ini menangkap makna dengan cara komputer boleh membandingkan dan mencari. Mereka disimpan dalam pangkalan data khas, dan pengguna boleh memilih model embedding yang mereka mahu gunakan.

- **Pangkalan Data Vektor (Mekanisme Pengambilan)**: Pangkalan data ini **menyimpan embedding kandungan laman web**. Apabila seseorang bertanya soalan, NLWeb memeriksa pangkalan data vektor untuk mencari maklumat yang paling relevan dengan cepat. Ia memberikan senarai jawapan yang mungkin, diurutkan mengikut kesamaan. NLWeb berfungsi dengan sistem penyimpanan vektor yang berbeza seperti Qdrant, Snowflake, Milvus, Azure AI Search, dan Elasticsearch.

### NLWeb dengan Contoh

![NLWeb](../../../translated_images/nlweb-diagram.c1e2390b310e5fe4b245b86690ac6c49c26e355da5ab124128c8675d58cc9b07.ms.png)

Pertimbangkan laman web tempahan perjalanan kita sekali lagi, tetapi kali ini, ia dikuasakan oleh NLWeb.

1. **Pengambilan Data**: Katalog produk sedia ada laman web perjalanan (contohnya, senarai penerbangan, deskripsi hotel, pakej lawatan) diformatkan menggunakan Schema.org atau dimuatkan melalui suapan RSS. Alat NLWeb mengambil data berstruktur ini, mencipta embedding, dan menyimpannya dalam pangkalan data vektor tempatan atau jauh.

2. **Pertanyaan Bahasa Semula Jadi (Manusia)**: Seorang pengguna melawat laman web dan, bukannya menavigasi menu, menaip ke dalam antara muka sembang: "Cari saya hotel mesra keluarga di Honolulu dengan kolam renang untuk minggu depan".

3. **Pemprosesan NLWeb**: Aplikasi NLWeb menerima pertanyaan ini. Ia menghantar pertanyaan kepada LLM untuk memahami dan secara serentak mencari pangkalan data vektornya untuk senarai hotel yang relevan.

4. **Hasil Tepat**: LLM membantu menafsirkan hasil carian dari pangkalan data, mengenal pasti padanan terbaik berdasarkan kriteria "mesra keluarga," "kolam renang," dan "Honolulu," dan kemudian memformatkan respons bahasa semula jadi. Yang penting, respons merujuk kepada hotel sebenar dari katalog laman web, mengelakkan maklumat yang direka.

5. **Interaksi Agen AI**: Oleh kerana NLWeb berfungsi sebagai pelayan MCP, agen perjalanan AI luaran juga boleh menyambung ke instans NLWeb laman web ini. Agen AI boleh menggunakan kaedah `tanya` MCP untuk bertanya kepada laman web secara langsung: `tanya("Adakah terdapat restoran mesra vegan di kawasan Honolulu yang disyorkan oleh hotel?")`. Instans NLWeb akan memproses ini, memanfaatkan pangkalan data maklumat restoran (jika dimuatkan), dan mengembalikan respons JSON berstruktur.

### Ada Lagi Soalan tentang MCP/A2A/NLWeb?

Sertai [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) untuk bertemu dengan pelajar lain, menghadiri waktu pejabat, dan mendapatkan jawapan kepada soalan agen AI anda.

## Sumber

- [MCP untuk Pemula](https://aka.ms/mcp-for-beginners)  
- [Dokumentasi MCP](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Repositori NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Panduan Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.