[![Intro to AI Agents](../../../translated_images/ms/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klik imej di atas untuk menonton video untuk pelajaran ini)_

# Pengenalan kepada Ejen AI dan Kes Penggunaan Ejen

Selamat datang ke kursus **Ejen AI untuk Pemula**! Kursus ini memberikan anda pengetahuan asas — dan kod kerja sebenar — untuk mula membina Ejen AI dari awal.

Jom cakap hi di <a href="https://discord.gg/kzRShWzttr" target="_blank">Komuniti Discord Azure AI</a> — ia penuh dengan pelajar dan pembina AI yang gembira untuk menjawab soalan.

Sebelum kita mula membina, mari pastikan kita benar-benar faham apa itu Ejen AI dan bila menggunakan ia adalah wajar.

---

## Pengenalan

Pelajaran ini merangkumi:

- Apa itu Ejen AI, dan jenis-jenis yang wujud
- Jenis tugas yang paling sesuai untuk Ejen AI
- Blok binaan teras yang akan anda gunakan apabila mereka bentuk penyelesaian Agentik

## Matlamat Pembelajaran

Pada akhir pelajaran ini, anda seharusnya boleh:

- Terangkan apa itu Ejen AI dan bagaimana ia berbeza daripada penyelesaian AI biasa
- Tahu bila untuk menggunakan Ejen AI (dan bila tidak)
- Reka bentuk asas penyelesaian Agentik untuk masalah dunia sebenar

---

## Mendefinisikan Ejen AI dan Jenis-Jenis Ejen AI

### Apa itu Ejen AI?

Ini cara mudah untuk memikirkannya:

> **Ejen AI adalah sistem yang membolehkan Model Bahasa Besar (LLM) benar-benar *melakukan sesuatu* — dengan memberikan mereka alat dan pengetahuan untuk bertindak ke atas dunia, bukan sekadar membalas arahan.**

Mari kita perincikan sedikit:

- **Sistem** — Ejen AI bukan hanya satu entiti. Ia adalah koleksi bahagian yang bekerja bersama. Pada terasnya, setiap ejen mempunyai tiga komponen:
  - **Persekitaran** — Ruang tempat ejen itu bekerja. Untuk ejen tempahan perjalanan, ini adalah platform tempahan itu sendiri.
  - **Sensor** — Cara ejen membaca keadaan semasa persekitarannya. Ejen perjalanan kita mungkin memeriksa ketersediaan hotel atau harga penerbangan.
  - **Aktuator** — Cara ejen mengambil tindakan. Ejen perjalanan mungkin menempah bilik, menghantar pengesahan, atau membatalkan tempahan.

![What Are AI Agents?](../../../translated_images/ms/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Model Bahasa Besar** — Ejen wujud sebelum LLM, tetapi LLM adalah apa yang menjadikan ejen moden begitu berkuasa. Mereka boleh memahami bahasa semula jadi, berfikir tentang konteks, dan mengubah permintaan pengguna yang samar menjadi pelan tindakan konkrit.

- **Melaksanakan Tindakan** — Tanpa sistem ejen, LLM hanya menghasilkan teks. Dalam sistem ejen, LLM boleh benar-benar *melaksanakan* langkah — mencari dalam pangkalan data, memanggil API, menghantar mesej.

- **Akses kepada Alat** — Alat apa yang boleh ejen gunakan bergantung pada (1) persekitaran yang ia jalankan dan (2) apa yang pembangun pilih untuk berikan. Ejen perjalanan mungkin boleh mencari penerbangan tetapi tidak boleh mengedit rekod pelanggan — semuanya bergantung pada apa yang anda sambungkan.

- **Memori + Pengetahuan** — Ejen boleh mempunyai memori jangka pendek (perbualan semasa) dan memori jangka panjang (pangkalan data pelanggan, interaksi lalu). Ejen perjalanan mungkin "ingat" bahawa anda lebih suka tempat duduk tingkap.

---

### Jenis-Jenis Ejen AI

Tidak semua ejen dibina sama. Berikut adalah pecahan jenis utama, menggunakan ejen tempahan perjalanan sebagai contoh berjalan:

| **Jenis Ejen** | **Apa Yang Dilakukan** | **Contoh Ejen Perjalanan** |
|---|---|---|
| **Ejen Refleks Mudah** | Mengikut peraturan kod keras — tiada memori, tiada perancangan. | Melihat e-mel aduan → teruskan ke khidmat pelanggan. Itu sahaja. |
| **Ejen Refleks Berasaskan Model** | Menyimpan model dalaman dunia dan mengemas kini apabila perkara berubah. | Menjejak harga penerbangan sejarah dan menandakan laluan yang tiba-tiba mahal. |
| **Ejen Berasaskan Matlamat** | Mempunyai matlamat dan cari cara untuk mencapainya langkah demi langkah. | Menempah perjalanan penuh (penerbangan, kereta, hotel) dari lokasi semasa anda ke destinasi anda. |
| **Ejen Berasaskan Utiliti** | Tidak hanya mencari *satu* penyelesaian — mencari *terbaik* dengan menimbang pertukaran. | Mengimbangi kos dan kemudahan untuk mencari perjalanan yang paling sesuai dengan keutamaan anda. |
| **Ejen Pembelajaran** | Menjadi lebih baik dari masa ke masa dengan belajar daripada maklum balas. | Menyesuaikan cadangan tempahan masa depan berdasarkan keputusan tinjauan selepas perjalanan. |
| **Ejen Hierarki** | Ejen tahap tinggi membahagikan kerja ke tugas-tugas kecil dan menyerahkannya ke ejen tahap bawah. | Permintaan "batal perjalanan" dibahagikan kepada: batal penerbangan, batal hotel, batal sewa kereta — masing-masing dikendalikan oleh sub-ejen. |
| **Sistem Multi-Ejen (MAS)** | Beberapa ejen bebas bekerja bersama (atau bersaing). | Kerjasama: ejen berasingan mengendalikan hotel, penerbangan, dan hiburan. Persaingan: beberapa ejen bersaing untuk mengisi bilik hotel dengan harga terbaik. |

---

## Bila Menggunakan Ejen AI

Hanya kerana anda *boleh* menggunakan Ejen AI tidak bermakna anda harus selalu *menggunakannya*. Berikut adalah situasi di mana ejen benar-benar berguna:

![When to use AI Agents?](../../../translated_images/ms/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Masalah Terbuka** — Apabila langkah untuk menyelesaikan masalah tidak boleh diprogramkan terlebih dahulu. Anda memerlukan LLM untuk cari jalan secara dinamik.
- **Proses Berbilang Langkah** — Tugas yang memerlukan penggunaan alat merentasi beberapa pusingan, bukan hanya carian atau generasi tunggal.
- **Penambahbaikan dari Masa ke Masa** — Apabila anda mahu sistem menjadi lebih pintar berdasarkan maklum balas pengguna atau isyarat persekitaran.

Kita akan mendalami bila (dan bila *tidak*) menggunakan Ejen AI dalam pelajaran **Membina Ejen AI Yang Boleh Dipercayai** kemudian dalam kursus.

---

## Asas Penyelesaian Agentik

### Pembangunan Ejen

Perkara pertama yang anda lakukan apabila membina ejen adalah menentukan *apa yang boleh ia lakukan* — alat, tindakan, dan tingkah lakunya.

Dalam kursus ini, kami menggunakan **Perkhidmatan Ejen AI Azure** sebagai platform utama kami. Ia menyokong:

- Model terbuka seperti OpenAI, Mistral, dan Llama
- Data berlesen dari penyedia seperti Tripadvisor
- Definisi alat OpenAPI 3.0 yang distandardkan

### Corak Agentik

Anda berkomunikasi dengan LLM melalui arahan. Dengan ejen, anda tidak boleh sentiasa mencipta setiap arahan secara manual — ejen perlu bertindak dalam banyak langkah. Di sinilah **Corak Agentik** masuk. Ia adalah strategi boleh guna semula untuk mengarahkan dan mengorkestrasi LLM dengan cara yang lebih boleh diukur dan boleh dipercayai.

Kursus ini disusun berdasarkan corak agentik yang paling biasa dan berguna.

### Rangka Kerja Agentik

Rangka Kerja Agentik memberikan pembangun templat siap sedia, alat, dan infrastruktur untuk membina ejen. Ia memudahkan:

- Menyambungkan alat dan keupayaan
- Memerhati apa yang ejen lakukan (dan debug apabila berlaku kesilapan)
- Bekerjasama antara beberapa ejen

Dalam kursus ini, kami fokus pada **Rangka Kerja Ejen Microsoft (MAF)** untuk membina ejen yang sedia untuk produksi.

---

## Contoh Kod

Sedia untuk melihat ia beraksi? Berikut adalah contoh kod untuk pelajaran ini:

- 🐍 Python: [Rangka Kerja Ejen](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Rangka Kerja Ejen](./code_samples/01-dotnet-agent-framework.md)

---

## Ada Soalan?

Sertai [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) untuk berhubung dengan pelajar lain, hadir sesi pejabat, dan dapatkan soalan Ejen AI anda dijawab oleh komuniti.

---

## Pelajaran Sebelumnya

[Persediaan Kursus](../00-course-setup/README.md)

## Pelajaran Seterusnya

[Meneroka Rangka Kerja Agentik](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidakakuratan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber autoritatif. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->