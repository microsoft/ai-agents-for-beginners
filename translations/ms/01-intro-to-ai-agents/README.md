[![Pengenalan kepada Ejen AI](../../../translated_images/ms/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klik gambar di atas untuk menonton video bagi pelajaran ini)_

# Pengenalan kepada Ejen AI dan Kes Penggunaan Ejen

Selamat datang ke kursus **Ejen AI untuk Pemula**! Kursus ini memberi anda pengetahuan asas — dan kod sebenar yang berfungsi — untuk mula membina Ejen AI dari awal.

Datanglah sapa di <a href="https://discord.gg/kzRShWzttr" target="_blank">Komuniti Discord Azure AI</a> — penuh dengan pelajar dan pembina AI yang bersedia menjawab soalan.

Sebelum kita mula membina, mari pastikan kita benar-benar faham apa itu Ejen AI *dan* bila ia sesuai digunakan.

---

## Pengenalan

Pelajaran ini merangkumi:

- Apa itu Ejen AI, dan jenis-jenis yang wujud
- Tugas-tugas yang paling sesuai untuk Ejen AI
- Blok pembinaan teras yang anda akan gunakan bila mereka bentuk penyelesaian Agentik

## Matlamat Pembelajaran

Pada akhir pelajaran ini, anda sepatutnya boleh:

- Terangkan apa itu Ejen AI dan bagaimana ia berbeza daripada penyelesaian AI biasa
- Tahu bila untuk gunakan Ejen AI (dan bila tidak)
- Lukiskan reka bentuk penyelesaian Agentik asas untuk masalah dunia nyata

---

## Mendefinisikan Ejen AI dan Jenis-jenis Ejen AI

### Apa itu Ejen AI?

Berikut adalah cara mudah untuk memikirkannya:

> **Ejen AI adalah sistem yang membenarkan Model Bahasa Besar (LLM) benar-benar *melakukan sesuatu* — dengan memberikan alat dan pengetahuan untuk bertindak ke atas dunia, bukan sekadar memberi respons kepada arahan.**

Mari kita jelaskan sikit:

- **Sistem** — Ejen AI bukan hanya satu perkara. Ia adalah koleksi bahagian yang bekerja bersama. Pada dasarnya, setiap ejen mempunyai tiga bahagian:
  - **Persekitaran** — Ruang di mana ejen beroperasi. Untuk ejen tempahan perjalanan, ini adalah platform tempahan itu sendiri.
  - **Sensor** — Bagaimana ejen membaca keadaan semasa persekitarannya. Ejen perjalanan kita mungkin semak ketersediaan hotel atau harga penerbangan.
  - **Aktuator** — Bagaimana ejen mengambil tindakan. Ejen perjalanan mungkin menempah bilik, menghantar pengesahan, atau membatalkan tempahan.

![Apa Itu Ejen AI?](../../../translated_images/ms/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Model Bahasa Besar** — Ejen wujud sebelum LLM, tetapi LLMlah yang menjadikan ejen moden sangat berkuasa. Mereka boleh memahami bahasa semula jadi, berfikir tentang konteks, dan menukar permintaan samar pengguna menjadi pelan tindakan yang konkrit.

- **Melakukan Tindakan** — Tanpa sistem ejen, LLM hanya menjana teks. Dalam sistem ejen, LLM sebenarnya boleh *melaksanakan* langkah — mencari dalam pangkalan data, memanggil API, menghantar mesej.

- **Akses kepada Alat** — Alat yang ejen boleh gunakan bergantung pada (1) persekitaran ia beroperasi dan (2) apa yang pembangun pilih untuk berikan kepadanya. Ejen perjalanan mungkin boleh mencari penerbangan tetapi tidak boleh mengubah rekod pelanggan — semua bergantung pada bagaimana anda sambungkan.

- **Memori + Pengetahuan** — Ejen boleh mempunyai memori jangka pendek (perbualan semasa) dan memori jangka panjang (pangkalan data pelanggan, interaksi lalu). Ejen perjalanan mungkin "ingat" bahawa anda lebih suka tempat duduk tepi tingkap.

---

### Jenis-jenis Ejen AI

Tidak semua ejen dibina sama. Berikut adalah pecahan jenis utama, menggunakan contoh ejen tempahan perjalanan:

| **Jenis Ejen** | **Apa Yang Dilakukan** | **Contoh Ejen Perjalanan** |
|---|---|---|
| **Ejen Reflex Mudah** | Mengikuti peraturan yang telah diprogramkan — tiada memori, tiada perancangan. | Melihat emel aduan → teruskan ke perkhidmatan pelanggan. Itu sahaja. |
| **Ejen Reflex Berasaskan Model** | Menyimpan model dalaman dunia dan mengemas kini bila ada perubahan. | Memantau harga penerbangan historikal dan menandai laluan yang tiba-tiba mahal. |
| **Ejen Berasaskan Matlamat** | Ada matlamat dan mencari cara untuk mencapainya langkah demi langkah. | Menempah perjalanan lengkap (penerbangan, kereta, hotel) dari lokasi semasa anda ke destinasi. |
| **Ejen Berasaskan Utiliti** | Tidak hanya cari *sebuah* penyelesaian — cari yang *terbaik* dengan menilai pertukaran. | Menyeimbangkan kos vs. kemudahan untuk mencari perjalanan dengan skor terbaik mengikut keutamaan anda. |
| **Ejen Pembelajaran** | Menjadi lebih baik dari masa ke masa dengan belajar dari maklum balas. | Menyesuaikan cadangan tempahan masa depan berdasarkan keputusan tinjauan pasca-perjalanan. |
| **Ejen Hierarki** | Ejen peringkat tinggi pecahkan kerja kepada subtugas dan agihkan kepada ejen lebih rendah. | Permintaan "batalkan perjalanan" dibahagi kepada: batalkan penerbangan, batalkan hotel, batalkan sewa kereta — setiap satu dikendalikan oleh sub-ejen. |
| **Sistem Multi-Ejen (MAS)** | Beberapa ejen bebas bekerjasama (atau bersaing). | Kerjasama: ejen berasingan mengendalikan hotel, penerbangan, hiburan. Persaingan: beberapa ejen bersaing mengisi bilik hotel dengan harga terbaik. |

---

## Bila Untuk Menggunakan Ejen AI

Hanya kerana anda *boleh* menggunakan Ejen AI tidak bermakna anda sentiasa *perlu*. Berikut adalah situasi di mana ejen benar-benar menonjol:

![Bila untuk menggunakan Ejen AI?](../../../translated_images/ms/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Masalah Terbuka** — Bila langkah penyelesaian masalah tidak boleh dipratugaskan. Anda perlukan LLM cari jalan secara dinamik.
- **Proses Berbilang Langkah** — Tugas yang memerlukan menggunakan alat sepanjang beberapa giliran, bukan hanya satu carian atau penjanaan. 
- **Peningkatan dari Masa ke Masa** — Bila anda mahu sistem menjadi lebih pintar berdasarkan maklum balas pengguna atau isyarat persekitaran.

Kita akan selami bila (dan bila *tidak*) guna Ejen AI dalam pelajaran **Membina Ejen AI yang Boleh Dipercayai** nanti dalam kursus.

---

## Asas Penyelesaian Agentik

### Pembangunan Ejen

Perkara pertama yang anda lakukan apabila membina ejen adalah menentukan *apa yang ia boleh lakukan* — alat, tindakan, dan tingkah laku.

Dalam kursus ini, kami menggunakan **Microsoft Foundry Agent Service** sebagai platform utama. Ia menyokong:

- Model dari penyedia seperti OpenAI, Mistral, dan Meta (Llama)
- Data berlesen dari penyedia seperti Tripadvisor
- Definisi alat OpenAPI 3.0 yang dikendalikan secara standard

### Corak Agentik

Anda berkomunikasi dengan LLM melalui arahan. Dengan ejen, anda tidak boleh selalu buat setiap arahan secara manual — ejen perlu bertindak dalam banyak langkah. Di sinilah **Corak Agentik** masuk. Ia adalah strategi boleh guna semula untuk memacu dan mengatur LLM secara lebih skala dan boleh dipercayai.

Kursus ini disusun berdasarkan corak agentik yang paling biasa dan berguna.

### Rangka Kerja Agentik

Rangka Kerja Agentik memberi pembangun templat, alat, dan infrastruktur siap untuk membina ejen. Ia memudahkan:

- Sambungkan alat dan keupayaan
- Perhatikan apa yang ejen lakukan (dan baiki bila ada masalah)
- Bekerjasama antara pelbagai ejen

Dalam kursus ini, tumpuan kami adalah pada **Microsoft Agent Framework (MAF)** untuk membina ejen yang sedia untuk pengeluaran.

---

## Contoh Kod

Sedia untuk melihat ia beraksi? Berikut adalah contoh kod untuk pelajaran ini:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Ada Soalan?

Sertailah [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) untuk berhubung dengan pelajar lain, hadiri waktu pejabat, dan dapatkan soalan tentang Ejen AI anda dijawab oleh komuniti.


---

## Ujian Asas Ejen Ini (Pilihan)

Setelah anda belajar untuk mengatur ejen dalam [Pelajaran 16](../16-deploying-scalable-agents/README.md), anda boleh tambah pemeriksaan kesihatan pantas selepas penyebaran untuk `TravelAgent` di pelajaran ini dengan katalog siap pakai [`tests/lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json). Lihat [`tests/README.md`](../tests/README.md) untuk cara menjalankannya.

---

## Pelajaran Sebelumnya

[Persediaan Kursus](../00-course-setup/README.md)

## Pelajaran Seterusnya

[Meneroka Rangka Kerja Agentik](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->