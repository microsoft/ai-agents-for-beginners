# Ejen AI untuk Pemula - Panduan Pembelajaran

Gunakan panduan ini sebagai rakan praktikal semasa anda menjalani kursus. Ia
bukan bertujuan untuk menggantikan pelajaran. Ia membantu anda memutuskan dari mana untuk bermula, apa yang
perlu dicari dalam setiap pelajaran, dan bagaimana menghubungkan idea-idea ke dalam demo ejen
yang kecil dan berfungsi.

Jika ini kali pertama anda di sini, mulakan dengan yang ringkas:

1. Baca [Persediaan Kursus](./00-course-setup/README.md).
2. Lengkapkan Pelajaran 01-06 secara berurutan.
3. Simpan satu idea demo kecil dalam fikiran semasa anda belajar.
4. Selepas setiap pelajaran, tanya: "Apa yang ejen saya boleh lakukan sekarang yang tidak dapat dibuat
   sebelum ini?"

## Demo Ringkas Untuk Disimpan Dalam Fikiran

Cara yang baik untuk belajar ejen adalah dengan mengikuti satu idea demo sepanjang kursus.

Contoh demo: **ejen pembantu kursus**.

Pengguna bertanya:

> "Saya mahu belajar bagaimana ejen menggunakan alat. Cari pelajaran yang sesuai, ringkaskan apa
> yang perlu saya baca dahulu, dan berikan saya tugasan latihan pendek."

Chatbot biasa boleh menjawab dari apa yang sudah diketahui. Ejen boleh buat lebih:

1. **Baca atau cari fail kursus** untuk menemui pelajaran yang sesuai.
2. **Gunakan alat** untuk mendapatkan pautan pelajaran, contoh, atau bahan sokongan.
3. **Rancang** laluan pembelajaran pendek dan bukannya memberikan satu jawapan panjang.
4. **Gunakan konteks** dari perbualan semasa untuk kekal fokus pada
   matlamat pelajar.
5. **Ingat keutamaan berguna** jika aplikasi menyokong memori.
6. **Tunjukkan jejak, petikan, atau log** supaya pengguna boleh memahami apa yang berlaku.
7. **Gunakan pengawal keselamatan** sebelum mengambil tindakan berisiko atau menggunakan data sensitif.

Semasa anda belajar setiap pelajaran, kembali ke demo ini dan tanya: apakah kemampuan baru
yang akan ditambah oleh pelajaran ini?

## Apa Yang Anda Sedang Bangunkan

Pada akhir kursus, anda seharusnya dapat menerangkan dan membina sistem ejen
yang menggabungkan bahagian-bahagian berikut:

| Bahagian | Maksud dalam bahasa biasa | Dalam demo |
|------|------------------------|-------------|
| Model | Enjin penaakulan yang mentafsir permintaan pengguna | Memahami bahawa pelajar mahu pelajaran tentang penggunaan alat |
| Alat | Fungsi, API, fail, pelayar, atau perkhidmatan yang boleh digunakan oleh ejen | Mencari repo atau mendapatkan kandungan pelajaran |
| Pengetahuan | Dokumen atau data yang digunakan untuk mendasari jawapan | Fail README kursus dan bahan pelajaran |
| Konteks | Maklumat yang termasuk dalam panggilan model seterusnya | Matlamat pengguna dan hasil alat |
| Memori | Maklumat yang disimpan untuk kegunaan kemudian | Pelajar lebih suka contoh hands-on Python |
| Perancangan | Memecahkan matlamat besar kepada langkah kecil | Cari pelajaran, ringkaskan, cadangkan latihan |
| Orkestra | Mengarahkan kerja melalui alat, langkah, atau ejen | Perancang memanggil alat carian, kemudian penyimpul |
| Kepercayaan | Keselamatan, keselamatan, penilaian, dan pengurusan pemerhatian | Merekod panggilan alat dan bertanya sebelum tindakan berimpak tinggi |

## Model dan Penyedia

Contoh kod kursus menggunakan **Microsoft Agent Framework (MAF)** dan mensasarkan **Azure OpenAI Responses API** — API yang disyorkan pada masa hadapan, yang menggabungkan penyelesaian perbualan, panggilan alat, input multimodal, dan perbualan berkeadaan dalam satu permukaan API sahaja. Anda boleh sambungkan sama ada melalui projek **Microsoft Foundry** (dengan `FoundryChatClient`) atau terus ke Azure OpenAI (dengan `OpenAIChatClient`).

Semasa anda mengikuti pelajaran, terdapat beberapa pilihan penyedia:

- **Microsoft Foundry / Azure OpenAI (Responses API)** — laluan utama yang digunakan dalam pelajaran. Log masuk dengan `az login` untuk pengesahan Entra ID tanpa kunci.
- **Foundry Lokal** — menjalankan model sepenuhnya dalam peranti melalui API yang serasi dengan OpenAI (tiada awan, tiada kunci API). Sesuai untuk eksperimen luar talian atau tanpa kos. Lihat [Persediaan Kursus](./00-course-setup/README.md).
- **MiniMax** — penyedia yang serasi dengan OpenAI dengan model konteks besar, boleh digunakan sebagai alternatif gantian.

> **Nota:** GitHub Models sudah tidak digunakan (berhenti beroperasi Julai 2026) dan tidak menyokong Responses API. Contoh telah dikemas kini untuk menggunakan Azure OpenAI / Microsoft Foundry sebaliknya.

## Pilih Laluan Pembelajaran Anda

Anda boleh mengikuti keseluruhan kursus secara berurutan, atau lompat ke laluan berdasarkan apa yang anda mahu
bina.

| Jika matlamat anda adalah untuk... | Mula dengan | Kemudian belajar |
|-----------------------|------------|------------|
| Fahami apa itu ejen | 01, 02, 03 | 04, 05, 06 |
| Bina ejen yang menggunakan alat | 04 | 05, 07, 14 |
| Bina ejen berasaskan RAG | 05 | 04, 06, 12 |
| Reka bentuk aliran kerja pelbagai langkah | 07 | 08, 09, 14 |
| Fahami sistem multi-ejen | 08 | 07, 09, 11 |
| Sediakan ejen untuk pengeluaran | 06, 10 | 12, 13, 16, 18 |
| Lancar dan tambah skala ejen di Foundry | 10, 16 | 06, 13, 18 |
| Bina ejen tempatan / offline-pertama | 17 | 04, 05, 11 |
| Terokai protokol dan automasi pelayar | 11, 15 | 10, 18 |

Petua: jika anda baru dalam ejen, jangan langkau Pelajaran 01-06. Ia memberikan anda
perbendaharaan kata yang anda perlukan untuk baki kursus.

## Panduan Pelajaran demi Pelajaran

| Pelajaran | Apa yang anda pelajari | Cuba ini selepas pelajaran |
|--------|----------------|---------------------------|
| [01 - Pengenalan kepada Ejen AI](./01-intro-to-ai-agents/README.md) | Apa yang membezakan ejen dari chatbot asas. | Terangkan idea demo anda sebagai ejen, bukan sekadar aplikasi sembang. |
| [02 - Rangka Kerja Ejenik](./02-explore-agentic-frameworks/README.md) | Bagaimana rangka kerja membantu dengan model, alat, keadaan, dan aliran kerja. | Kenal pasti bahagian demo anda yang akan diurus oleh rangka kerja. |
| [03 - Corak Rekabentuk Ejenik](./03-agentic-design-patterns/README.md) | Corak biasa untuk mereka bentuk tingkah laku ejen. | Lukis perjalanan pengguna sebelum menulis kod. |
| [04 - Penggunaan Alat](./04-tool-use/README.md) | Bagaimana ejen memanggil alat untuk mendapatkan data atau mengambil tindakan. | Tetapkan satu alat yang diperlukan oleh ejen demo anda. |
| [05 - RAG Ejenik](./05-agentic-rag/README.md) | Bagaimana pengambilan maklumat mendasari jawapan ejen dalam dokumen atau data. | Tentukan sumber pengetahuan yang harus dicari oleh demo anda. |

| [06 - Ejen Boleh Dipercayai](./06-building-trustworthy-agents/README.md) | Cara untuk menambah pagar pengawal, pengawasan, dan tingkah laku yang lebih selamat. | Tambah satu peraturan untuk bila ejen harus bertanya kepada pengguna terlebih dahulu. |
| [07 - Reka Bentuk Perancangan](./07-planning-design/README.md) | Bagaimana ejen memecahkan matlamat yang lebih besar kepada langkah-langkah yang lebih kecil. | Tulis pelan tiga langkah untuk permintaan demo anda. |
| [08 - Reka Bentuk Multi-Ejen](./08-multi-agent/README.md) | Bila untuk membahagikan kerja kepada ejen yang pakar khusus. | Tentukan sama ada demo anda memerlukan satu ejen atau beberapa ejen. |
| [09 - Metakognisi](./09-metacognition/README.md) | Bagaimana ejen boleh mengkaji dan memperbaiki keluaran mereka sendiri. | Tambah pemeriksaan sendiri terakhir sebelum ejen memberi respons. |
| [10 - Ejen AI dalam Pengeluaran](./10-ai-agents-production/README.md) | Apa yang berubah apabila ejen bergerak dari demo ke pengeluaran. | Senaraikan apa yang anda akan pantau: kualiti, kos, kelewatan, kegagalan. |
| [11 - Protokol Ejenik](./11-agentic-protocols/README.md) | Bagaimana protokol menghubungkan ejen kepada alat dan ejen lain. | Kenal pasti di mana protokol standard boleh memudahkan integrasi. |
| [12 - Kejuruteraan Konteks](./12-context-engineering/README.md) | Cara memilih, memotong, mengasingkan, dan mengurus konteks. | Tentukan apa yang patut dimasukkan dalam arahan dan apa yang harus dikeluarkan. |
| [13 - Memori Ejen](./13-agent-memory/README.md) | Bagaimana ejen boleh menyimpan maklumat berguna sepanjang interaksi. | Pilih satu keutamaan selamat yang demo anda boleh ingat. |
| [14 - Rangka Kerja Ejen Microsoft](./14-microsoft-agent-framework/README.md) | Blok binaan khusus rangka kerja untuk ejen dan aliran kerja, serta pengehosan ejen LangChain/LangGraph pada Microsoft Foundry. | Peta langkah demo anda kepada konsep rangka kerja. |
| [15 - Ejen Penggunaan Komputer](./15-browser-use/README.md) | Bagaimana ejen boleh berinteraksi dengan pelayar atau permukaan UI, termasuk contoh dunia nyata seperti Microsoft Project Opal. | Pilih satu tugasan pelayar yang masih memerlukan pengesahan pengguna. |
| [16 - Melancarkan Ejen Skala Besar](./16-deploying-scalable-agents/README.md) | Cara membawa ejen dari prototaip kepada pelancaran yang boleh diskala dan boleh diperhatikan di Microsoft Foundry (ejen dihoskan, penghalaan model, penyimpanan cache, pintu pemeriksaan, ujian asap). | Senaraikan kebimbangan pengeluaran yang demo anda masih perlukan: pengehosan, penghalaan, kos, penilaian. |
| [17 - Mewujudkan Ejen AI Tempatan](./17-creating-local-ai-agents/README.md) | Cara membina ejen berfokuskan tempatan yang berjalan sepenuhnya pada mesin anda menggunakan Foundry Local dan Qwen (alat tempatan, RAG tempatan, MCP tempatan). | Tentukan bahagian mana demo anda patut kekal peribadi dan berjalan secara tempatan. |
| [18 - Mengamankan Ejen AI](./18-securing-ai-agents/README.md) | Cara menjadikan tindakan ejen lebih boleh diaudit dan bukti pengubahsuaian. | Tentukan apa tindakan dalam demo anda yang perlu direkod atau menerima resit. |

## Mengesahkan Ejen yang Dilancarkan dengan Ujian Asap

Apabila anda melancarkan ejen (Pelajaran 16), **ujian asap** adalah pemeriksaan pertama termurah
untuk memastikan pelancaran itu benar-benar memberi jawapan. Repositori ini menyediakan katalog sedia untuk dijalankan
di bawah [tests/](./tests/README.md) untuk ejen boleh lancar dalam Pelajaran
01, 04, 05, dan 16, yang dipasang dengan

[AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) GitHub
Tindakan. Jalankan ia dari tab **Actions** selepas melaksanakan agen pelajaran.
Ujian asap adalah pintu pertama — penilaian luar talian dan dalam talian (Pelajaran 10 dan 16)
memberitahu anda sejauh mana *baik* agen tersebut.

## Idea Utama Dalam Istilah Mesra Pemula

### Alat

Alat adalah sesuatu yang boleh dipanggil oleh agen untuk melakukan kerja di luar model. Alat yang baik
mempunyai nama yang jelas, tugasan yang terhad, input yang ditaip, output yang boleh diramal, dan cara yang selamat
untuk gagal.

Untuk demo pembantu kursus, alat mungkin seperti:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG dan Pengetahuan

RAG membantu agen menjawab dari bahan sumber dan bukannya meneka. Dalam
kursus ini, bahan sumber itu boleh berupa README pelajaran, contoh kod, atau sumber luaran
yang dipautkan dari pelajaran.

Gunakan RAG apabila jawapan perlu berasaskan dokumen, data, atau fail projek semasa.


### Perancangan

Perancangan berguna apabila permintaan mempunyai lebih daripada satu langkah. Kekalkan rancangan ringkas dan
cukup jelas untuk pemeriksaan oleh pembangun atau pengguna.

Untuk demo, rancangan mungkin:

1. Cari pelajaran yang berkaitan dengan penggunaan alat.
2. Ringkaskan pelajaran yang paling relevan.
3. Cadangkan satu tugasan latihan.

### Konteks

Konteks adalah apa yang model lihat sekarang. Konteks yang terlalu sedikit boleh
menyebabkan agen terlepas butiran penting. Konteks yang terlalu banyak boleh menyebabkan agen menjadi perlahan, lebih mahal,
atau mudah keliru.

Kejuruteraan konteks yang baik bermaksud memilih maklumat yang betul untuk panggilan model seterusnya.


### Memori

Memori adalah maklumat yang disimpan untuk kegunaan kemudian. Jangan simpan segala-galanya. Simpan maklumat
hanya apabila ia berguna, selamat, dan mudah untuk dikemas kini atau dipadam.

Contohnya, mengingati "pelajar lebih suka contoh Python" mungkin berguna.
Mengingati data peribadi sensitif biasanya tidak.

### Penilaian dan Kebolehlihatan

Penilaian bertanya: adakah agen melakukan perkara yang betul?

Kebolehlihatan bertanya: bolehkah kita lihat bagaimana ia berlaku?

Untuk agen produksi, rekodkan panggilan model, panggilan alat, konteks yang diperoleh,
kelewatan, kos, kegagalan, dan maklum balas pengguna.

### Kepercayaan dan Keselamatan

Agen yang boleh dipercayai memerlukan lebih daripada arahan yang membantu. Gunakan alat kebenaran terhad,
kelulusan manusia untuk tindakan berimpak tinggi, penyuntingan data jika perlu, dan log atau
resit untuk tindakan yang mesti diaudit.

## Rutin Semakan 15 Minit

Gunakan rutin ini selepas setiap pelajaran:

1. **Ringkaskan pelajaran dalam satu ayat.**
2. **Namakan keupayaan agen yang baru.** Contohnya: penggunaan alat, pengambilan,
   perancangan, memori, kebolehlihatan, atau keselamatan.
3. **Tambahkannya ke demo pembantu kursus.** Apa perubahan dalam demo sekarang?
4. **Cari risikonya.** Apa yang boleh salah jika keupayaan ini disalahgunakan?
5. **Tulis satu soalan ujian.** Bagaimana anda memeriksa bahawa agen bertindak dengan baik?

## Semakan Diri Cepat

Sebelum bergerak ke hadapan, cubalah menjawab soalan-soalan ini:

1. Apa yang boleh dilakukan oleh agen yang tidak boleh dilakukan oleh chatbot biasa dengan sendiri?
2. Alat apa yang diperlukan oleh agen anda terlebih dahulu, dan mengapa?
3. Sumber pengetahuan apa yang sepatutnya menjadi asas jawapan agen?
4. Konteks apa yang perlu dimasukkan dalam panggilan model seterusnya?

5. Apa yang harus agen ingat, dan apa yang harus dielakkan daripada disimpan?
6. Bila agen harus meminta kelulusan manusia?
7. Log, jejak, atau resit apa yang boleh membantu anda menyahpepijat atau mengaudit agen kemudian?


## Cadangan Latihan Capstone

Pada akhir kursus, bina ejen kecil yang membantu pelajar menavigasi
repositori ini.

Versi minimum:

- Terima topik dari pengguna.
- Cari pelajaran yang paling relevan.
- Ringkaskan apa yang perlu dibaca dahulu.
- Cadangkan satu tugasan amali.
- Tunjukkan fail pelajaran atau pautan yang telah digunakan.

Versi lanjutan:

- Ingat bahasa pengaturcaraan pilihan pelajar.
- Gunakan pelan mudah sebelum menjawab.
- Tambah langkah semak kendiri sebelum respons terakhir.
- Log panggilan alat dan sumber yang diperoleh.
- Minta pengesahan sebelum membuka pelayar atau tugasan automasi UI.

Ini memberi anda cara kecil tetapi realistik untuk melatih alat, RAG, perancangan,
konteks, memori, kebolehlihatan, dan kepercayaan dalam satu projek.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->