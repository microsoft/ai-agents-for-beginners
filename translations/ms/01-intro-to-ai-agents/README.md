[![Intro to AI Agents](../../../translated_images/ms/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klik gambar di atas untuk menonton video pelajaran ini)_


# Pengenalan kepada Ejen AI dan Kes Penggunaan Ejen

Selamat datang ke kursus "Ejen AI untuk Pemula"! Kursus ini menyediakan pengetahuan asas dan contoh aplikasi untuk membina Ejen AI.

Sertailah <a href="https://discord.gg/kzRShWzttr" target="_blank">Komuniti Discord Azure AI</a> untuk bertemu dengan pelajar lain dan Pembina Ejen AI serta tanya apa-apa soalan yang anda ada mengenai kursus ini.

Untuk memulakan kursus ini, kita bermula dengan mendapatkan pemahaman yang lebih baik tentang apa itu Ejen AI dan bagaimana kita boleh menggunakannya dalam aplikasi dan aliran kerja yang kita bina.

## Pengenalan

Pelajaran ini merangkumi:

- Apakah Ejen AI dan apakah jenis ejen yang berbeza?
- Apakah kes penggunaan terbaik untuk Ejen AI dan bagaimana mereka boleh membantu kita?
- Apakah beberapa blok binaan asas apabila mereka bentuk Penyelesaian Agenik?

## Matlamat Pembelajaran
Selepas menamatkan pelajaran ini, anda sepatutnya boleh:

- Memahami konsep Ejen AI dan bagaimana ia berbeza daripada penyelesaian AI lain.
- Menggunakan Ejen AI dengan paling cekap.
- Mereka bentuk penyelesaian Agenik secara produktif untuk pengguna dan pelanggan.

## Mendefinisikan Ejen AI dan Jenis Ejen AI

### Apakah Ejen AI?

Ejen AI adalah **sistem** yang membolehkan **Model Bahasa Besar (LLM)** untuk **melakukan tindakan** dengan memperluaskan kebolehan mereka dengan memberi LLM **akses kepada alat** dan **pengetahuan**.

Mari kita pecahkan definisi ini kepada bahagian yang lebih kecil:

- **Sistem** - Penting untuk berfikir tentang ejen bukan hanya sebagai satu komponen tetapi sebagai sistem yang terdiri daripada banyak komponen. Pada tahap asas, komponen Ejen AI adalah:
  - **Persekitaran** - Ruang yang telah ditakrif di mana Ejen AI beroperasi. Sebagai contoh, jika kita mempunyai ejen tempahan perjalanan, persekitarannya boleh jadi sistem tempahan perjalanan yang digunakan oleh ejen AI untuk menyelesaikan tugasan.
  - **Sensor** - Persekitaran mempunyai maklumat dan memberikan maklum balas. Ejen AI menggunakan sensor untuk mengumpul dan mentafsir maklumat ini tentang keadaan semasa persekitaran. Dalam contoh Ejen Tempahan Perjalanan, sistem tempahan perjalanan boleh memberikan maklumat seperti ketersediaan hotel atau harga penerbangan.
  - **Aktuator** - Setelah Ejen AI menerima keadaan semasa persekitaran, untuk tugasan semasa agen menentukan tindakan yang perlu dilakukan untuk mengubah persekitaran. Untuk ejen tempahan perjalanan, ia mungkin untuk menempah bilik yang tersedia untuk pengguna.

![What Are AI Agents?](../../../translated_images/ms/what-are-ai-agents.1ec8c4d548af601a.webp)

**Model Bahasa Besar** - Konsep ejen sudah wujud sebelum penubuhan LLM. Kelebihan membina Ejen AI dengan LLM adalah kebolehan mereka untuk mentafsir bahasa manusia dan data. Kebolehan ini membolehkan LLM mentafsir maklumat persekitaran dan menentukan pelan untuk mengubah persekitaran.

**Melakukan Tindakan** - Di luar sistem Ejen AI, LLM terhad kepada situasi di mana tindakan adalah menjana kandungan atau maklumat berdasarkan arahan pengguna. Dalam sistem Ejen AI, LLM boleh melaksanakan tugasan dengan mentafsir permintaan pengguna dan menggunakan alat yang tersedia dalam persekitarannya.

**Akses Kepada Alat** - Alat yang LLM boleh akses ditentukan oleh 1) persekitaran tempat ia beroperasi dan 2) pembangun Ejen AI. Untuk contoh ejen perjalanan kami, alat ejen adalah terhad oleh operasi yang tersedia dalam sistem tempahan, dan/atau pembangun boleh mengehadkan akses alat ejen kepada penerbangan.

**Memori+Pengetahuan** - Memori boleh bersifat jangka pendek dalam konteks perbualan antara pengguna dan ejen. Jangka panjang, di luar maklumat yang disediakan oleh persekitaran, Ejen AI juga boleh mendapatkan pengetahuan dari sistem lain, perkhidmatan, alat, dan juga ejen lain. Dalam contoh ejen perjalanan, pengetahuan ini boleh jadi maklumat tentang keutamaan perjalanan pengguna yang terletak dalam pangkalan data pelanggan.

### Jenis-jenis ejen berbeza

Sekarang yang kita ada definisi umum tentang Ejen AI, mari lihat beberapa jenis ejen spesifik dan bagaimana mereka akan digunakan pada ejen tempahan perjalanan.

| **Jenis Ejen**                | **Penerangan**                                                                                                                       | **Contoh**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Ejen Refleks Mudah**        | Melakukan tindakan segera berdasarkan peraturan yang telah ditetapkan.                                                              | Ejen perjalanan mentafsir konteks e-mel dan memajukan aduan perjalanan kepada perkhidmatan pelanggan.                                                                                                                        |
| **Ejen Refleks Berasaskan Model** | Melakukan tindakan berdasarkan model dunia dan perubahan pada model tersebut.                                                         | Ejen perjalanan memberi keutamaan pada laluan dengan perubahan harga besar berdasarkan akses kepada data harga sejarah.                                                                                                    |
| **Ejen Berasaskan Matlamat**  | Membuat pelan untuk mencapai matlamat tertentu dengan mentafsir matlamat dan menentukan tindakan untuk mencapainya.                  | Ejen perjalanan menempah perjalanan dengan menentukan keperluan susunan perjalanan (kereta, pengangkutan awam, penerbangan) dari lokasi semasa ke destinasi.                                                                    |
| **Ejen Berasaskan Utiliti**   | Mengambil kira keutamaan dan menilai pertukaran secara numerikal untuk menentukan cara mencapai matlamat.                            | Ejen perjalanan memaksimumkan utiliti dengan menilai kemudahan berbanding kos semasa menempah perjalanan.                                                                                                                     |
| **Ejen Pembelajar**           | Memperbaiki dari semasa ke semasa dengan memberi maklum balas dan melaraskan tindakan mengikutnya.                                    | Ejen perjalanan memperbaiki dengan menggunakan maklum balas pelanggan dari tinjauan selepas perjalanan untuk membuat pelarasan tempahan masa depan.                                                                          |
| **Ejen Hierarki**             | Mempunyai pelbagai ejen dalam sistem bertingkat, dengan ejen peringkat tinggi memecahkan tugasan kepada tugasan kecil untuk ejen peringkat rendah melengkapkan. | Ejen perjalanan membatalkan perjalanan dengan membahagikan tugasan kepada tugasan kecil (contohnya, membatalkan tempahan khusus) dan membiarkan ejen peringkat rendah melengkapkan tugasan tersebut, melaporkan kembali kepada ejen peringkat tinggi. |
| **Sistem Multi-Ejen (MAS)**   | Ejen melengkapkan tugasan secara berdikari, sama ada secara koperatif atau kompetitif.                                               | Koperatif: Pelbagai ejen menempah perkhidmatan perjalanan tertentu seperti hotel, penerbangan, dan hiburan. Kompetitif: Pelbagai ejen mengurus dan bersaing ke atas kalendar tempahan hotel bersama untuk menempah pelanggan ke hotel tersebut.  |

## Bila Menggunakan Ejen AI

Dalam bahagian awal, kami menggunakan kes penggunaan Ejen Perjalanan untuk menerangkan bagaimana jenis ejen berbeza boleh digunakan dalam senario tempahan perjalanan yang berbeza. Kami akan terus menggunakan aplikasi ini sepanjang kursus.

Mari kita lihat jenis kes penggunaan yang paling sesuai digunakan oleh Ejen AI:

![When to use AI Agents?](../../../translated_images/ms/when-to-use-ai-agents.54becb3bed74a479.webp)


- **Masalah Terbuka** - membenarkan LLM menentukan langkah-langkah yang diperlukan untuk menyelesaikan tugasan kerana ia tidak selalu boleh dikodkan secara keras dalam aliran kerja.
- **Proses Berbilang Langkah** - tugasan yang memerlukan tahap kerumitan di mana Ejen AI perlu menggunakan alat atau maklumat dalam beberapa pusingan dan bukannya ambilan satu kali.  
- **Penambahbaikan dari Masa ke Masa** - tugasan di mana ejen boleh memperbaiki dari masa ke masa dengan menerima maklum balas dari persekitarannya atau pengguna untuk menyediakan utiliti yang lebih baik.

Kami membincangkan lebih banyak pertimbangan menggunakan Ejen AI dalam pelajaran Membina Ejen AI yang Boleh Dipercayai.

## Asas Penyelesaian Agenik

### Pembangunan Ejen

Langkah pertama dalam mereka bentuk sistem Ejen AI adalah menentukan alat, tindakan, dan tingkah laku. Dalam kursus ini, kami menumpukan pada penggunaan **Perkhidmatan Ejen Azure AI** untuk mentakrif Ejen kami. Ia menawarkan ciri seperti:

- Pemilihan Model Terbuka seperti OpenAI, Mistral, dan Llama
- Penggunaan Data Berlesen melalui penyedia seperti Tripadvisor
- Penggunaan alat OpenAPI 3.0 yang distandardkan

### Corak Agenik

Komunikasi dengan LLM adalah melalui arahan. Memandangkan sifat separa autonomi Ejen AI, ia tidak selalu mungkin atau diperlukan untuk memberi arahan semula kepada LLM selepas perubahan dalam persekitaran. Kami menggunakan **Corak Agenik** yang membolehkan kami memberi arahan kepada LLM dalam beberapa langkah dengan cara yang lebih skala.

Kursus ini dibahagikan kepada beberapa corak Agenik popular terkini.

### Rangka Kerja Agenik

Rangka Kerja Agenik membolehkan pembangun melaksanakan corak agenik melalui kod. Rangka kerja ini menawarkan templat, pemalam, dan alat untuk kolaborasi Ejen AI yang lebih baik. Manfaat ini menyediakan kebolehan untuk pemerhatian dan penyelesaian masalah sistem Ejen AI dengan lebih baik.

Dalam kursus ini, kami akan meneroka Rangka Kerja Ejen Microsoft (MAF) untuk membina ejen AI yang sedia untuk produksi.

## Kod Contoh

- Python: [Rangka Kerja Ejen](./code_samples/01-python-agent-framework.ipynb)
- .NET: [Rangka Kerja Ejen](./code_samples/01-dotnet-agent-framework.md)

## Ada Lagi Soalan tentang Ejen AI?

Sertai [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) untuk bertemu dengan pelajar lain, hadir waktu pejabat dan dapatkan jawapan untuk soalan Ejen AI anda.

## Pelajaran Sebelum Ini

[Persiapan Kursus](../00-course-setup/README.md)

## Pelajaran Seterusnya

[Meneroka Rangka Kerja Agenik](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->