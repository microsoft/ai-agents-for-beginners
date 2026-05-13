[![Intro to AI Agents](../../../translated_images/ms/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klik imej di atas untuk menonton video bagi pelajaran ini)_

# Pengenalan kepada Ejen AI dan Kes Penggunaan Ejen

Selamat datang ke kursus **Ejen AI untuk Pemula**! Kursus ini memberikan anda pengetahuan asas — dan kod yang berfungsi — untuk mula membina Ejen AI dari awal.

Jom ucapkan hai di <a href="https://discord.gg/kzRShWzttr" target="_blank">Komuniti Azure AI Discord</a> — ia dipenuhi dengan pelajar dan pembina AI yang gembira untuk menjawab soalan.

Sebelum kita mula membina, mari pastikan kita benar-benar faham apa itu Ejen AI dan bila ia masuk akal untuk digunakan.

---

## Pengenalan

Pelajaran ini merangkumi:

- Apa itu Ejen AI, dan jenis-jenis yang wujud
- Tugas-tugas yang paling sesuai untuk Ejen AI
- Blok binaan utama yang akan anda gunakan ketika mereka bentuk penyelesaian Agentic

## Matlamat Pembelajaran

Menjelang akhir pelajaran ini, anda sepatutnya boleh:

- Terangkan apa itu Ejen AI dan bagaimana ia berbeza daripada penyelesaian AI biasa
- Tahu bila untuk menggunakan Ejen AI (dan bila tidak)
- Lakarkan reka bentuk penyelesaian Agentic asas untuk masalah dunia sebenar

---

## Mendefinisikan Ejen AI dan Jenis-jenis Ejen AI

### Apa itu Ejen AI?

Ini cara mudah untuk memikirkannya:

> **Ejen AI adalah sistem yang membolehkan Model Bahasa Besar (LLM) benar-benar *melakukan sesuatu* — dengan memberikan mereka alat dan pengetahuan untuk bertindak ke atas dunia, bukan hanya memberi respon kepada arahan.**

Mari kita terangkan sedikit:

- **Sistem** — Ejen AI bukan hanya satu perkara. Ia adalah satu kumpulan bahagian yang bekerjasama. Pada asasnya, setiap ejen mempunyai tiga komponen:
  - **Persekitaran** — Ruang tempat ejen bertugas. Untuk ejen tempahan perjalanan, ini adalah platform tempahan itu sendiri.
  - **Sensor** — Cara ejen membaca keadaan semasa persekitarannya. Ejen perjalanan kita mungkin memeriksa ketersediaan hotel atau harga penerbangan.
  - **Aktuator** — Cara ejen bertindak. Ejen perjalanan mungkin menempah bilik, menghantar pengesahan, atau membatalkan tempahan.

![What Are AI Agents?](../../../translated_images/ms/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Model Bahasa Besar** — Ejen wujud sebelum LLM, tetapi LLM membuat ejen moden sangat berkuasa. Mereka boleh memahami bahasa semula jadi, membuat rasional tentang konteks, dan mengubah permintaan umum pengguna menjadi pelan tindakan konkrit.

- **Melakukan Tindakan** — Tanpa sistem ejen, LLM hanya menjana teks. Dalam sistem ejen, LLM boleh benar-benar *melaksanakan* langkah — mencari dalam pangkalan data, memanggil API, menghantar mesej.

- **Akses kepada Alat** — Alat apa yang ejen boleh gunakan bergantung pada (1) persekitaran di mana ia beroperasi dan (2) apa yang pembangun pilih untuk diberikan kepadanya. Ejen perjalanan mungkin boleh mencari penerbangan tetapi tidak boleh mengubah rekod pelanggan — semuanya bergantung pada apa yang anda sambungkan.

- **Memori + Pengetahuan** — Ejen boleh mempunyai memori jangka pendek (perbualan semasa) dan memori jangka panjang (pangkalan data pelanggan, interaksi lalu). Ejen perjalanan mungkin "mengingati" bahawa anda suka tempat duduk berdekatan tingkap.

---

### Jenis-Jenis Ejen AI

Tidak semua ejen dibina sama. Berikut adalah pecahan jenis utama, menggunakan contoh ejen tempahan perjalanan sebagai contoh berjalan:

| **Jenis Ejen** | **Fungsi** | **Contoh Ejen Perjalanan** |
|---|---|---|
| **Ejen Refleks Mudah** | Mengikut peraturan yang telah ditulis — tiada memori, tiada perancangan. | Melihat e-mel aduan → teruskan kepada perkhidmatan pelanggan. Itu sahaja. |
| **Ejen Refleks Berasaskan Model** | Menyimpan model dalaman dunia dan mengemaskininya apabila keadaan berubah. | Mengesan harga penerbangan sejarah dan menanda laluan yang tiba-tiba mahal. |
| **Ejen Berasaskan Matlamat** | Mempunyai matlamat dan mencari cara mencapainya langkah demi langkah. | Menempah perjalanan penuh (penerbangan, kereta, hotel) bermula dari lokasi anda sekarang ke destinasi anda. |
| **Ejen Berasaskan Kebolehgunaan** | Tidak hanya mencari *satu* penyelesaian — cari *yang terbaik* dengan menilai pertukaran. | Menyeimbangkan kos berbanding kemudahan untuk mencari perjalanan yang paling sesuai dengan keutamaan anda. |
| **Ejen Pembelajaran** | Menjadi lebih baik dari masa ke masa dengan pembelajaran dari maklum balas. | Melaraskan cadangan tempahan masa depan berdasarkan hasil tinjauan selepas perjalanan. |
| **Ejen Hierarki** | Ejen tahap tinggi memecah kerja menjadi subtugas dan mendelegasikan kepada ejen tahap rendah. | Permintaan "batalkan perjalanan" dibahagikan kepada: batalkan penerbangan, batalkan hotel, batalkan sewaan kereta — setiap satu dikendali oleh sub-ejen. |
| **Sistem Multi-Ejen (MAS)** | Beberapa ejen bebas bekerja bersama (atau bersaing). | Kerjasama: ejen berbeza mengendalikan hotel, penerbangan, dan hiburan. Persaingan: beberapa ejen bersaing untuk mengisi bilik hotel pada harga terbaik. |

---

## Bila untuk Menggunakan Ejen AI

Hanya kerana anda *boleh* menggunakan Ejen AI tidak bermakna anda selalu *perlu*. Berikut adalah situasi di mana ejen benar-benar berguna:

![When to use AI Agents?](../../../translated_images/ms/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Masalah Terbuka** — Apabila langkah untuk menyelesaikan masalah tidak boleh dipratetapkan. Anda memerlukan LLM untuk mencari jalan secara dinamik.
- **Proses Berbilang Langkah** — Tugas yang memerlukan menggunakan alat merentasi beberapa giliran, bukan hanya satu carian atau penjanaan.
- **Penambahbaikan dari Masa ke Masa** — Apabila anda mahu sistem menjadi lebih pintar berdasarkan maklum balas pengguna atau isyarat persekitaran.

Kita akan meneroka lebih mendalam bila (dan bila *tidak*) menggunakan Ejen AI dalam pelajaran **Membina Ejen AI Yang Boleh Dipercayai** nanti dalam kursus ini.

---

## Asas Penyelesaian Agentic

### Pembangunan Ejen

Perkara pertama yang anda buat apabila membina ejen adalah mentakrifkan *apa yang boleh ia lakukan* — alatnya, tindakannya, dan tingkah lakunya.

Dalam kursus ini, kami menggunakan **Perkhidmatan Ejen AI Azure** sebagai platform utama. Ia menyokong:

- Model dari penyedia seperti OpenAI, Mistral, dan Meta (Llama)
- Data berlesen dari penyedia seperti Tripadvisor
- Definisi alat OpenAPI 3.0 yang piawai

### Corak Agentic

Anda berkomunikasi dengan LLM melalui arahan. Dengan ejen, anda tidak boleh sentiasa membuat setiap arahan secara manual — ejen perlu bertindak merentasi banyak langkah. Di sinilah **Corak Agentic** masuk. Ia adalah strategi yang boleh digunakan semula untuk memberi arahan dan mengatur LLM dengan cara yang lebih mudah skala dan boleh dipercayai.

Kursus ini disusun berasaskan corak agentic yang paling umum dan berguna.

### Rangka Kerja Agentic

Rangka Kerja Agentic menyediakan pembangun template, alat, dan infrastruktur siap guna untuk membina ejen. Ia memudahkan untuk:

- Menyambungkan alat dan keupayaan
- Memerhati apa yang dilakukan ejen (dan membaik pulih apabila terjadi ralat)
- Bekerjasama merentasi pelbagai ejen

Dalam kursus ini, kami fokus pada **Rangka Kerja Ejen Microsoft (MAF)** untuk membina ejen yang sedia untuk pengeluaran.

---

## Contoh Kod

Sedia untuk melihat ia beraksi? Berikut adalah contoh kod untuk pelajaran ini:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Ada Soalan?

Sertai [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) untuk berhubung dengan pelajar lain, hadiri waktu pejabat, dan dapatkan soalan anda tentang Ejen AI dijawab oleh komuniti.

---

## Pelajaran Sebelumnya

[Persediaan Kursus](../00-course-setup/README.md)

## Pelajaran Seterusnya

[Meneroka Rangka Kerja Agentic](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->