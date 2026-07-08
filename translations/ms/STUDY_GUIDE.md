# Ejen AI untuk Pemula - Panduan Belajar

Gunakan panduan ini sebagai teman praktikal semasa anda melalui kursus. Ia
tidak bertujuan untuk menggantikan pelajaran. Ia membantu anda memutuskan di mana untuk mulakan, apa yang
perlu dicari dalam setiap pelajaran, dan bagaimana menghubungkan idea-idea menjadi demo ejen
kecil yang berfungsi.

Jika ini kali pertama anda di sini, mulakan dengan mudah:

1. Baca [Setup Kursus](./00-course-setup/README.md).
2. Selesaikan Pelajaran 01-06 secara berurutan.
3. Simpan satu idea demo kecil dalam fikiran semasa belajar.
4. Selepas setiap pelajaran, tanyakan: "Apa yang ejen saya boleh lakukan sekarang yang tidak boleh dilakukan
   sebelumnya?"

## Demo Mudah Untuk Disimpan Dalam Fikiran

Cara yang baik untuk belajar ejen adalah mengikuti satu idea demo sepanjang kursus.

Contoh demo: **ejen pembantu kursus**.

Pengguna bertanya:

> "Saya mahu belajar bagaimana ejen menggunakan alat. Cari pelajaran yang betul, ringkaskan apa
> yang harus saya baca terlebih dahulu, dan berikan saya tugas latihan ringkas."

Chatbot biasa boleh menjawab berdasarkan apa yang sudah diketahui. Ejen boleh melakukan lebih:

1. **Baca atau cari fail kursus** untuk mencari pelajaran yang betul.
2. **Gunakan alat** untuk mendapatkan pautan pelajaran, contoh, atau bahan sokongan.
3. **Rancang** laluan pembelajaran ringkas daripada memberikan satu jawapan panjang.
4. **Gunakan konteks** dari perbualan semasa untuk kekal fokus pada
   matlamat pelajar.
5. **Ingat keutamaan berguna** jika aplikasi menyokong ingatan.
6. **Tunjukkan jejak, sitasi, atau log** supaya pengguna boleh memahami apa yang berlaku.
7. **Gunakan kawalan keselamatan** sebelum mengambil tindakan berisiko atau menggunakan data sensitif.

Semasa anda mengkaji setiap pelajaran, kembali ke demo ini dan tanyakan: apa kebolehan baru
yang akan ditambah oleh pelajaran ini?

## Apa Yang Anda Sedang Bangunkan

Pada akhir kursus, anda sepatutnya boleh menerangkan dan membina sistem ejen
yang menggabungkan bahagian-bahagian ini:

| Bahagian | Maksud dalam bahasa biasa | Dalam demo |
|------|------------------------|-------------|
| Model | Enjin penaakulan yang mentafsir permintaan pengguna | Memahami bahawa pelajar mahu pelajaran tentang penggunaan alat |
| Alat | Fungsi, API, fail, pelayar, atau perkhidmatan yang boleh digunakan ejen | Mencari repo atau mendapatkan kandungan pelajaran |
| Pengetahuan | Dokumen atau data yang digunakan untuk menyokong jawapan | Fail README kursus dan bahan pelajaran |
| Konteks | Maklumat yang disertakan dalam panggilan model seterusnya | Matlamat pengguna dan hasil alat |
| Ingatan | Maklumat yang disimpan untuk kegunaan kemudian | Pelajar lebih suka contoh Python praktikal |
| Perancangan | Memecahkan matlamat lebih besar kepada langkah yang lebih kecil | Cari pelajaran, ringkaskan, cadang latihan |
| Orkestrasi | Mengarahkan kerja merentas alat, langkah, atau ejen | Perancang memanggil alat carian, kemudian peringkasan |
| Kepercayaan | Keselamatan, keselamatan, penilaian, dan keterlihatan | Mencatat panggilan alat dan bertanya sebelum tindakan berimpak tinggi |

## Model dan Penyedia

Contoh kod kursus menggunakan **Microsoft Agent Framework (MAF)** dan menyasarkan **Azure OpenAI Responses API** — API yang disyorkan ke hadapan, yang menggabungkan lengkapkan sembang, panggilan alat, input multimodal, dan perbualan berstatus dalam satu permukaan API. Anda sambungkan sama ada melalui projek **Microsoft Foundry** (dengan `FoundryChatClient`) atau terus ke Azure OpenAI (dengan `OpenAIChatClient`).

Semasa anda menjalani pelajaran, anda mempunyai beberapa pilihan penyedia:

- **Microsoft Foundry / Azure OpenAI (Responses API)** — laluan utama yang digunakan dalam pelajaran. Log masuk dengan `az login` untuk pengesahan Entra ID tanpa kunci.
- **Foundry Local** — jalankan model sepenuhnya di peranti melalui API yang serasi OpenAI (tiada awan, tiada kunci API). Sesuai untuk eksperimen luar talian atau tanpa kos. Lihat [Setup Kursus](./00-course-setup/README.md).
- **MiniMax** — penyedia serasi OpenAI dengan model konteks besar, boleh digunakan sebagai alternatif ganti.

> **Nota:** GitHub Models sudah tidak digunakan (akan diberhentikan Julai 2026) dan tidak menyokong Responses API. Contoh telah dikemas kini untuk menggunakan Azure OpenAI / Microsoft Foundry sebaliknya.

## Pilih Laluan Pembelajaran Anda

Anda boleh mengambil kursus penuh secara berurutan, atau lompat ke laluan berdasarkan apa yang anda mahu
bina.

| Jika matlamat anda adalah untuk... | Mula dengan | Kemudian pelajari |
|-----------------------|------------|------------|
| Memahami apa itu ejen | 01, 02, 03 | 04, 05, 06 |
| Membina ejen yang menggunakan alat | 04 | 05, 07, 14 |
| Membina ejen berasaskan RAG | 05 | 04, 06, 12 |
| Merangka aliran kerja berbilang langkah | 07 | 08, 09, 14 |
| Memahami sistem multi-ejen | 08 | 07, 09, 11 |
| Mempersiapkan ejen untuk pengeluaran | 06, 10 | 12, 13, 18 |
| Meneroka protokol dan automasi pelayar | 11, 15 | 10, 18 |

Petua: jika anda baru dalam dunia ejen, jangan langkau Pelajaran 01-06. Ia memberi anda
kosa kata yang anda perlukan untuk baki kursus.

## Panduan Pelajaran demi Pelajaran

| Pelajaran | Apa yang anda pelajari | Cuba ini selepas pelajaran |
|--------|----------------|---------------------------|
| [01 - Pengenalan kepada Ejen AI](./01-intro-to-ai-agents/README.md) | Apa yang membezakan ejen daripada chatbot asas. | Terangkan idea demo anda sebagai ejen, bukan sekadar aplikasi chat. |
| [02 - Rangka Kerja Agenik](./02-explore-agentic-frameworks/README.md) | Bagaimana rangka kerja membantu dengan model, alat, status, dan aliran kerja. | Kenal pasti bahagian demo anda yang akan diurus oleh rangka kerja. |
| [03 - Corak Reka Bentuk Agenik](./03-agentic-design-patterns/README.md) | Corak biasa untuk mereka bentuk tingkah laku ejen. | Lukis perjalanan pengguna sebelum menulis kod. |
| [04 - Penggunaan Alat](./04-tool-use/README.md) | Bagaimana ejen memanggil alat untuk mendapatkan data atau mengambil tindakan. | Tentukan satu alat yang diperlukan oleh ejen demo anda. |
| [05 - Agenik RAG](./05-agentic-rag/README.md) | Bagaimana pengambilan mengukuhkan jawapan ejen dalam dokumen atau data. | Putuskan sumber pengetahuan yang harus dicari oleh demo anda. |
| [06 - Ejen Yang Boleh Dipercayai](./06-building-trustworthy-agents/README.md) | Cara menambah kawalan keselamatan, pengawasan, dan tingkah laku lebih selamat. | Tambah satu peraturan tentang bila ejen harus bertanya kepada pengguna terlebih dahulu. |
| [07 - Reka Bentuk Perancangan](./07-planning-design/README.md) | Bagaimana ejen memecahkan matlamat besar kepada langkah lebih kecil. | Tulis pelan tiga langkah untuk permintaan demo anda. |

| [08 - Reka Bentuk Pelbagai Agen](./08-multi-agent/README.md) | Bilakah untuk membahagikan kerja antara agen khusus. | Tentukan sama ada demo anda memerlukan satu agen atau beberapa agen. |
| [09 - Metakognisi](./09-metacognition/README.md) | Bagaimana agen boleh menyemak dan memperbaiki output mereka sendiri. | Tambah pemeriksaan kendiri terakhir sebelum agen memberi respons. |
| [10 - Agen AI dalam Pengeluaran](./10-ai-agents-production/README.md) | Apa yang berubah apabila agen berpindah dari demo ke pengeluaran. | Senaraikan apa yang anda akan pantau: kualiti, kos, kelewatan, kegagalan. |
| [11 - Protokol Agenik](./11-agentic-protocols/README.md) | Bagaimana protokol menghubungkan agen ke alat dan agen lain. | Kenal pasti di mana protokol standard boleh memudahkan integrasi. |
| [12 - Kejuruteraan Konteks](./12-context-engineering/README.md) | Bagaimana memilih, memangkas, mengasing dan mengurus konteks. | Tentukan apa yang patut dimasukkan dalam arahan dan apa yang harus dikecualikan. |
| [13 - Memori Agen](./13-agent-memory/README.md) | Bagaimana agen boleh menyimpan maklumat berguna sepanjang interaksi. | Pilih satu keutamaan selamat yang demo anda boleh ingat. |
| [14 - Rangka Kerja Agen Microsoft](./14-microsoft-agent-framework/README.md) | Blok binaan khusus rangka kerja untuk agen dan aliran kerja, serta hosting agen LangChain/LangGraph di Microsoft Foundry. | Peta langkah demo anda kepada konsep rangka kerja. |
| [15 - Agen Penggunaan Komputer](./15-browser-use/README.md) | Bagaimana agen boleh berinteraksi dengan pelayar atau permukaan UI, termasuk contoh dunia nyata seperti Microsoft Project Opal. | Pilih satu tugas pelayar yang masih memerlukan pengesahan pengguna. |
| [18 - Memastikan Keselamatan Agen AI](./18-securing-ai-agents/README.md) | Bagaimana menjadikan tindakan agen lebih boleh diaudit dan bukti gangguan. | Tentukan tindakan mana dalam demo anda yang harus direkod atau diberikan resit. |

Pelajaran 16 dan 17 disenaraikan dalam README utama sebagai akan datang tidak lama lagi. Tambahkan ia ke
pelan pembelajaran anda apabila kandungan pelajaran tersedia.

## Idea Utama Dalam Istilah Mesra Pemula

### Alat

Alat adalah sesuatu yang boleh dipanggil oleh agen untuk melakukan kerja di luar model. Alat yang baik
mempunyai nama yang jelas, tugas yang terhad, input berjenis, output boleh diramalkan, dan cara yang selamat
untuk gagal.

Untuk demo pembantu kursus, alat mungkin:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG dan Pengetahuan

RAG membantu agen menjawab berdasarkan bahan sumber dan bukan meneka. Dalam
kursus ini, bahan sumber tersebut mungkin README pelajaran, contoh kod, atau sumber luar
yang dipautkan dari pelajaran.

Gunakan RAG apabila jawapan sepatutnya berasaskan dokumen, data, atau fail projek semasa.


### Perancangan

Perancangan berguna apabila permintaan mempunyai lebih dari satu langkah. Pastikan rancangan ringkas dan
cukup jelas untuk pembangun atau pengguna memeriksa.

Untuk demo, rancangan mungkin:

1. Cari pelajaran berkaitan penggunaan alat.
2. Ringkaskan pelajaran yang paling berkaitan.
3. Cadangkan satu tugasan latihan.

### Konteks

Konteks adalah apa yang model lihat sekarang. Konteks terlalu sedikit boleh membuat agen
terlepas butiran penting. Konteks terlalu banyak boleh menjadikan agen lebih perlahan, lebih mahal,
atau mudah keliru.

Kejuruteraan konteks yang baik bermakna memilih maklumat yang betul untuk model seterusnya

panggilan.

### Memori

Memori adalah maklumat yang disimpan untuk kegunaan kemudian. Jangan simpan segala-galanya. Simpan maklumat
hanya apabila ia berguna, selamat, dan mudah untuk dikemas kini atau dipadam.

Sebagai contoh, mengingati "pelajar lebih suka contoh Python" mungkin berguna.
Mengingati data peribadi yang sensitif biasanya tidak.

### Penilaian dan Kebolehperhhatian

Penilaian bertanya: adakah ejen melakukan perkara yang betul?

Kebolehperhhatian bertanya: bolehkah kita melihat bagaimana ia berlaku?

Untuk ejen pengeluaran, jejak panggilan model, panggilan alat, konteks yang diperoleh,
kelewatan, kos, kegagalan, dan maklum balas pengguna.

### Kepercayaan dan Keselamatan

Ejen yang boleh dipercayai memerlukan lebih daripada arahan yang membantu. Gunakan alat hak istimewa terendah,
kelulusan manusia untuk tindakan berimpak tinggi, penyuntingan data di mana perlu, dan log atau
resit untuk tindakan yang mesti diaudit.

## Rutin Semakan 15 Minit

Gunakan rutin ini selepas setiap pelajaran:

1. **Ringkaskan pelajaran dalam satu ayat.**
2. **Namakan keupayaan ejen yang baru.** Contohnya: penggunaan alat, pengambilan,
   perancangan, memori, kebolehperhhatian, atau keselamatan.
3. **Tambahkannya ke demo pembantu kursus.** Apa yang berubah dalam demo sekarang?
4. **Cari risikonya.** Apa yang boleh menjadi salah jika keupayaan ini disalahgunakan?
5. **Tulis satu soalan ujian.** Bagaimana anda akan memeriksa bahawa ejen berkelakuan baik?

## Semakan Kendiri Pantas

Sebelum meneruskan, cuba jawab soalan-soalan ini:

1. Apa yang boleh dilakukan oleh ejen yang chatbot biasa tidak boleh lakukan sendiri?
2. Alat apa yang perlu dimiliki oleh ejen anda dahulu, dan kenapa?
3. Sumber ilmu apa yang harus menjadi asas jawapan ejen?
4. Konteks apa yang harus disertakan dalam panggilan model seterusnya?
5. Apa yang harus diingati oleh ejen, dan apa yang harus dielakkan daripada disimpan?
6. Bila ejen harus meminta kelulusan manusia?
7. Log, jejak, atau resit apa yang akan membantu anda membaiki atau mengaudit ejen kemudian?

## Cadangan Latihan Capstone

Pada akhir kursus, bina satu ejen kecil yang membantu pelajar meneroka
repositori ini.

Versi minimum:

- Terima topik dari pengguna.
- Cari pelajaran yang paling relevan.
- Ringkaskan apa yang perlu dibaca terlebih dahulu.
- Cadangkan satu tugasan amali.
- Tunjukkan fail pelajaran atau pautan yang digunakan.

Versi tambahbaik:

- Ingat bahasa pengaturcaraan pilihan pelajar.
- Gunakan pelan ringkas sebelum menjawab.
- Tambah langkah semak kendiri sebelum jawapan akhir.
- Log panggilan alat dan sumber yang diperoleh.
- Minta pengesahan sebelum membuka pelayar atau tugas automasi UI.

Ini memberikan anda cara kecil tetapi realistik untuk melatih alat, RAG, perancangan,
konteks, memori, kebolehperhhatian, dan kepercayaan dalam satu projek.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->