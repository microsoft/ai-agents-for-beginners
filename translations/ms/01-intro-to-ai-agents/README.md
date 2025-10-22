<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1e40fe956ff79462a02a17080b125041",
  "translation_date": "2025-08-29T18:09:53+00:00",
  "source_file": "01-intro-to-ai-agents/README.md",
  "language_code": "ms"
}
-->
[![Pengenalan kepada Ejen AI](../../../translated_images/lesson-1-thumbnail.d21b2c34b32d35bbc7f1b4a40a81b031970b6076b4e0c59fb006cf818cac5d4a.ms.png)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klik imej di atas untuk menonton video pelajaran ini)_

# Pengenalan kepada Ejen AI dan Kes Penggunaan Ejen

Selamat datang ke kursus "Ejen AI untuk Pemula"! Kursus ini menyediakan pengetahuan asas dan contoh aplikasi untuk membina Ejen AI.

Sertai [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) untuk bertemu dengan pelajar lain dan pembina Ejen AI serta ajukan sebarang soalan yang anda ada tentang kursus ini.

Untuk memulakan kursus ini, kita akan memahami dengan lebih baik apa itu Ejen AI dan bagaimana kita boleh menggunakannya dalam aplikasi dan aliran kerja yang kita bina.

## Pengenalan

Pelajaran ini merangkumi:

- Apa itu Ejen AI dan apakah jenis-jenis ejen yang berbeza?
- Apakah kes penggunaan terbaik untuk Ejen AI dan bagaimana ia boleh membantu kita?
- Apakah beberapa blok binaan asas dalam mereka bentuk Penyelesaian Ejenik?

## Matlamat Pembelajaran
Selepas melengkapkan pelajaran ini, anda seharusnya dapat:

- Memahami konsep Ejen AI dan bagaimana ia berbeza daripada penyelesaian AI lain.
- Menggunakan Ejen AI dengan lebih cekap.
- Mereka bentuk penyelesaian ejenik secara produktif untuk pengguna dan pelanggan.

## Mendefinisikan Ejen AI dan Jenis-Jenis Ejen AI

### Apa itu Ejen AI?

Ejen AI ialah **sistem** yang membolehkan **Model Bahasa Besar (LLM)** untuk **melakukan tindakan** dengan memperluaskan keupayaan mereka melalui pemberian **akses kepada alat** dan **pengetahuan** kepada LLM.

Mari kita pecahkan definisi ini kepada bahagian yang lebih kecil:

- **Sistem** - Penting untuk melihat ejen bukan hanya sebagai satu komponen tetapi sebagai sistem yang terdiri daripada banyak komponen. Pada tahap asas, komponen Ejen AI adalah:
  - **Persekitaran** - Ruang yang ditakrifkan di mana Ejen AI beroperasi. Sebagai contoh, jika kita mempunyai Ejen Tempahan Perjalanan, persekitarannya boleh menjadi sistem tempahan perjalanan yang digunakan oleh Ejen AI untuk melengkapkan tugas.
  - **Sensor** - Persekitaran mempunyai maklumat dan memberikan maklum balas. Ejen AI menggunakan sensor untuk mengumpul dan mentafsir maklumat tentang keadaan semasa persekitaran. Dalam contoh Ejen Tempahan Perjalanan, sistem tempahan perjalanan boleh memberikan maklumat seperti ketersediaan hotel atau harga penerbangan.
  - **Aktuator** - Setelah Ejen AI menerima keadaan semasa persekitaran, untuk tugas semasa, ejen menentukan tindakan yang perlu dilakukan untuk mengubah persekitaran. Untuk ejen tempahan perjalanan, ia mungkin menempah bilik yang tersedia untuk pengguna.

![Apa Itu Ejen AI?](../../../translated_images/what-are-ai-agents.1ec8c4d548af601a3a78c6c02e5c355d19c06a4a74fe93e3609a1d08e8c15689.ms.png)

**Model Bahasa Besar** - Konsep ejen telah wujud sebelum penciptaan LLM. Kelebihan membina Ejen AI dengan LLM adalah keupayaan mereka untuk mentafsir bahasa manusia dan data. Keupayaan ini membolehkan LLM mentafsir maklumat persekitaran dan menentukan rancangan untuk mengubah persekitaran.

**Melakukan Tindakan** - Di luar sistem Ejen AI, LLM terhad kepada situasi di mana tindakannya adalah menghasilkan kandungan atau maklumat berdasarkan arahan pengguna. Dalam sistem Ejen AI, LLM boleh menyelesaikan tugas dengan mentafsir permintaan pengguna dan menggunakan alat yang tersedia dalam persekitarannya.

**Akses kepada Alat** - Alat yang boleh diakses oleh LLM ditentukan oleh 1) persekitaran di mana ia beroperasi dan 2) pembangun Ejen AI. Untuk contoh ejen perjalanan kita, alat ejen terhad kepada operasi yang tersedia dalam sistem tempahan, dan/atau pembangun boleh mengehadkan akses alat ejen kepada penerbangan sahaja.

**Memori+Pengetahuan** - Memori boleh menjadi jangka pendek dalam konteks perbualan antara pengguna dan ejen. Dalam jangka panjang, di luar maklumat yang disediakan oleh persekitaran, Ejen AI juga boleh mendapatkan pengetahuan daripada sistem, perkhidmatan, alat, dan bahkan ejen lain. Dalam contoh ejen perjalanan, pengetahuan ini boleh menjadi maklumat tentang keutamaan perjalanan pengguna yang terletak dalam pangkalan data pelanggan.

### Jenis-Jenis Ejen yang Berbeza

Sekarang kita mempunyai definisi umum tentang Ejen AI, mari kita lihat beberapa jenis ejen tertentu dan bagaimana ia boleh digunakan dalam ejen tempahan perjalanan.

| **Jenis Ejen**                | **Penerangan**                                                                                                                       | **Contoh**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Ejen Refleks Mudah**        | Melakukan tindakan segera berdasarkan peraturan yang telah ditetapkan.                                                                | Ejen perjalanan mentafsir konteks e-mel dan memajukan aduan perjalanan kepada perkhidmatan pelanggan.                                                                                                                          |
| **Ejen Refleks Berasaskan Model** | Melakukan tindakan berdasarkan model dunia dan perubahan pada model tersebut.                                                          | Ejen perjalanan memprioritaskan laluan dengan perubahan harga yang ketara berdasarkan akses kepada data harga sejarah.                                                                                                             |
| **Ejen Berasaskan Matlamat**  | Membuat rancangan untuk mencapai matlamat tertentu dengan mentafsir matlamat dan menentukan tindakan untuk mencapainya.                | Ejen perjalanan menempah perjalanan dengan menentukan keperluan perjalanan (kereta, pengangkutan awam, penerbangan) dari lokasi semasa ke destinasi.                                                                                |
| **Ejen Berasaskan Utiliti**   | Mengambil kira keutamaan dan menimbang pertukaran secara numerik untuk menentukan cara mencapai matlamat.                              | Ejen perjalanan memaksimumkan utiliti dengan menimbang kemudahan vs. kos semasa menempah perjalanan.                                                                                                                                          |
| **Ejen Pembelajaran**         | Meningkatkan prestasi dari masa ke masa dengan bertindak balas terhadap maklum balas dan menyesuaikan tindakan sewajarnya.             | Ejen perjalanan bertambah baik dengan menggunakan maklum balas pelanggan daripada tinjauan selepas perjalanan untuk membuat penyesuaian pada tempahan masa depan.                                                                                                               |
| **Ejen Hierarki**             | Menampilkan pelbagai ejen dalam sistem bertingkat, dengan ejen peringkat lebih tinggi memecahkan tugas kepada subtugas untuk diselesaikan oleh ejen peringkat lebih rendah. | Ejen perjalanan membatalkan perjalanan dengan membahagikan tugas kepada subtugas (contohnya, membatalkan tempahan tertentu) dan membiarkan ejen peringkat lebih rendah menyelesaikannya, melaporkan kembali kepada ejen peringkat lebih tinggi.                                     |
| **Sistem Multi-Ejen (MAS)**   | Ejen melengkapkan tugas secara bebas, sama ada secara kerjasama atau persaingan.                                                      | Kerjasama: Pelbagai ejen menempah perkhidmatan perjalanan tertentu seperti hotel, penerbangan, dan hiburan. Persaingan: Pelbagai ejen mengurus dan bersaing dalam kalendar tempahan hotel yang dikongsi untuk menempah pelanggan ke dalam hotel. |

## Bila Menggunakan Ejen AI

Dalam bahagian sebelumnya, kita menggunakan kes penggunaan Ejen Perjalanan untuk menjelaskan bagaimana jenis-jenis ejen yang berbeza boleh digunakan dalam pelbagai senario tempahan perjalanan. Kita akan terus menggunakan aplikasi ini sepanjang kursus.

Mari kita lihat jenis kes penggunaan yang paling sesuai untuk Ejen AI:

![Bila Menggunakan Ejen AI?](../../../translated_images/when-to-use-ai-agents.54becb3bed74a479f5caca9c951132ce81d482a6704bcd22e5a600dbabc9434e.ms.png)

- **Masalah Terbuka** - membolehkan LLM menentukan langkah-langkah yang diperlukan untuk melengkapkan tugas kerana ia tidak selalu boleh dikodkan secara tetap ke dalam aliran kerja.
- **Proses Berbilang Langkah** - tugas yang memerlukan tahap kerumitan di mana Ejen AI perlu menggunakan alat atau maklumat dalam beberapa giliran dan bukan hanya satu kali pengambilan.  
- **Peningkatan dari Masa ke Masa** - tugas di mana ejen boleh bertambah baik dari masa ke masa dengan menerima maklum balas sama ada daripada persekitarannya atau pengguna untuk memberikan utiliti yang lebih baik.

Kami akan membincangkan lebih banyak pertimbangan menggunakan Ejen AI dalam pelajaran Membina Ejen AI yang Boleh Dipercayai.

## Asas Penyelesaian Ejenik

### Pembangunan Ejen

Langkah pertama dalam mereka bentuk sistem Ejen AI adalah untuk menentukan alat, tindakan, dan tingkah laku. Dalam kursus ini, kami memberi tumpuan kepada penggunaan **Azure AI Agent Service** untuk mentakrifkan Ejen kami. Ia menawarkan ciri seperti:

- Pemilihan Model Terbuka seperti OpenAI, Mistral, dan Llama
- Penggunaan Data Berlesen melalui penyedia seperti Tripadvisor
- Penggunaan alat OpenAPI 3.0 yang standard

### Corak Ejenik

Komunikasi dengan LLM adalah melalui arahan. Memandangkan sifat separa autonomi Ejen AI, tidak selalu mungkin atau diperlukan untuk mengarahkan semula LLM secara manual selepas perubahan dalam persekitaran. Kami menggunakan **Corak Ejenik** yang membolehkan kami mengarahkan LLM dalam beberapa langkah dengan cara yang lebih berskala.

Kursus ini dibahagikan kepada beberapa corak Ejenik popular semasa.

### Rangka Kerja Ejenik

Rangka Kerja Ejenik membolehkan pembangun melaksanakan corak ejenik melalui kod. Rangka kerja ini menawarkan templat, pemalam, dan alat untuk kolaborasi Ejen AI yang lebih baik. Manfaat ini menyediakan keupayaan untuk pemerhatian dan penyelesaian masalah sistem Ejen AI yang lebih baik.

Dalam kursus ini, kami akan meneroka rangka kerja AutoGen yang berasaskan penyelidikan dan rangka kerja Ejen yang sedia untuk pengeluaran daripada Semantic Kernel.

### Ada Lagi Soalan tentang Ejen AI?

Sertai [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) untuk bertemu dengan pelajar lain, menghadiri waktu pejabat, dan mendapatkan jawapan kepada soalan anda tentang Ejen AI.

## Pelajaran Sebelumnya

[Persediaan Kursus](../00-course-setup/README.md)

## Pelajaran Seterusnya

[Meneroka Rangka Kerja Ejenik](../02-explore-agentic-frameworks/README.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.