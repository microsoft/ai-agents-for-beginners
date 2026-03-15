# Memori untuk Ejen AI  
[![Agent Memory](../../../translated_images/ms/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Apabila membincangkan manfaat unik mencipta Ejen AI, dua perkara utama sering dibincangkan: keupayaan memanggil alat untuk melengkapkan tugas dan keupayaan untuk memperbaiki diri dari masa ke masa. Memori adalah asas kepada penciptaan ejen yang boleh memperbaiki diri sendiri yang dapat mencipta pengalaman yang lebih baik untuk pengguna kita.

Dalam pelajaran ini, kita akan melihat apa itu memori untuk Ejen AI dan bagaimana kita boleh menguruskannya serta menggunakannya untuk manfaat aplikasi kita.

## Pengenalan

Pelajaran ini akan merangkumi:

• **Memahami Memori Ejen AI**: Apa itu memori dan mengapa ia penting untuk ejen.

• **Melaksanakan dan Menyimpan Memori**: Kaedah praktikal untuk menambah keupayaan memori kepada ejen AI anda, dengan fokus pada memori jangka pendek dan jangka panjang.

• **Menjadikan Ejen AI Memperbaiki Diri Sendiri**: Bagaimana memori membolehkan ejen belajar daripada interaksi lalu dan memperbaiki dari masa ke masa.

## Pelaksanaan Tersedia

Pelajaran ini termasuk dua tutorial nota yang komprehensif:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Melaksanakan memori menggunakan Mem0 dan Azure AI Search dengan Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Melaksanakan memori berstruktur menggunakan Cognee, secara automatik membina graf ilmu yang disokong oleh embeddings, memvisualisasikan graf, dan pengambilan pintar

## Matlamat Pembelajaran

Selepas menamatkan pelajaran ini, anda akan tahu bagaimana untuk:

• **Membezakan antara pelbagai jenis memori ejen AI**, termasuk memori kerja, jangka pendek, dan jangka panjang, serta bentuk khusus seperti memori persona dan episodik.

• **Melaksanakan dan mengurus memori jangka pendek dan jangka panjang untuk ejen AI** menggunakan Microsoft Agent Framework, menggunakan alat seperti Mem0, Cognee, memori Whiteboard, dan integrasi dengan Azure AI Search.

• **Memahami prinsip di sebalik ejen AI yang memperbaiki diri sendiri** dan bagaimana sistem pengurusan memori yang kukuh menyumbang kepada pembelajaran dan penyesuaian berterusan.

## Memahami Memori Ejen AI

Pada intinya, **memori untuk ejen AI merujuk kepada mekanisme yang membolehkan mereka menyimpan dan mengingati maklumat**. Maklumat ini boleh menjadi butiran spesifik tentang perbualan, keutamaan pengguna, tindakan lalu, atau malah corak yang telah dipelajari.

Tanpa memori, aplikasi AI selalunya tidak mempunyai status, bermaksud setiap interaksi bermula dari awal. Ini menyebabkan pengalaman pengguna yang berulang dan mengecewakan di mana ejen "lupa" konteks atau keutamaan sebelumnya.

### Mengapa Memori Penting?

Kecerdasan ejen sangat berkait rapat dengan keupayaannya untuk mengingat dan menggunakan maklumat lalu. Memori membolehkan ejen menjadi:

• **Reflektif**: Belajar dari tindakan dan hasil lalu.

• **Interaktif**: Mengekalkan konteks dalam perbualan yang berterusan.

• **Proaktif dan Reaktif**: Mengunjurkan keperluan atau bertindak balas dengan sesuai berdasarkan data sejarah.

• **Autonomi**: Beroperasi lebih bebas dengan mengakses pengetahuan yang disimpan.

Matlamat melaksanakan memori adalah untuk menjadikan ejen lebih **boleh dipercayai dan berkebolehan**.

### Jenis Memori

#### Memori Kerja

Fikirkan ini sebagai sehelai kertas nota yang digunakan ejen semasa menjalankan satu tugas atau proses pemikiran berterusan. Ia menyimpan maklumat segera yang diperlukan untuk mengira langkah seterusnya.

Untuk ejen AI, memori kerja selalunya menangkap maklumat paling relevan daripada perbualan, walaupun sejarah sembang penuh panjang atau dipotong. Ia memberi tumpuan kepada mengekstrak elemen utama seperti keperluan, cadangan, keputusan, dan tindakan.

**Contoh Memori Kerja**

Dalam ejen tempahan perjalanan, memori kerja mungkin menangkap permintaan pengguna semasa, seperti "Saya mahu menempah perjalanan ke Paris". Keperluan khusus ini disimpan dalam konteks segera ejen untuk membimbing interaksi semasa.

#### Memori Jangka Pendek

Jenis memori ini menyimpan maklumat untuk tempoh satu perbualan atau sesi sahaja. Ia adalah konteks sembang semasa, membolehkan ejen merujuk kembali kepada pusingan perbualan sebelumnya.

**Contoh Memori Jangka Pendek**

Jika pengguna bertanya, "Berapa kos penerbangan ke Paris?" dan kemudian bertanya lagi, "Bagaimana pula dengan penginapan di sana?", memori jangka pendek memastikan ejen tahu "sana" merujuk kepada "Paris" dalam perbualan yang sama.

#### Memori Jangka Panjang

Ini adalah maklumat yang kekal merentas pelbagai perbualan atau sesi. Ia membolehkan ejen mengingati keutamaan pengguna, interaksi sejarah, atau pengetahuan umum sepanjang tempoh yang panjang. Ini penting untuk personalisasi.

**Contoh Memori Jangka Panjang**

Memori jangka panjang mungkin menyimpan bahawa "Ben suka bermain ski dan aktiviti luar, suka kopi dengan pemandangan gunung, dan mahu mengelak cerun ski lanjutan kerana kecederaan lalu". Maklumat ini, yang diperoleh daripada interaksi terdahulu, mempengaruhi cadangan dalam sesi perancangan perjalanan masa hadapan, menjadikannya sangat diperibadikan.

#### Memori Persona

Jenis memori khusus ini membantu ejen membangunkan "personaliti" atau "persona" yang konsisten. Ia membolehkan ejen mengingati butiran tentang dirinya atau peranan yang dimaksudkan, menjadikan interaksi lebih lancar dan fokus.

**Contoh Memori Persona**

Jika ejen perjalanan direka sebagai "perancang ski pakar," memori persona mungkin mengukuhkan peranan ini, mempengaruhi responsnya untuk selaras dengan nada dan pengetahuan pakar.

#### Memori Aliran Kerja/Episodik

Memori ini menyimpan urutan langkah yang diambil ejen semasa menjalankan tugas kompleks, termasuk kejayaan dan kegagalan. Ia seperti mengingati "episod" spesifik atau pengalaman lalu untuk belajar daripadanya.

**Contoh Memori Episodik**

Jika ejen cuba menempah penerbangan tertentu tetapi gagal kerana tiada tempat, memori episodik boleh merekod kegagalan ini, membolehkan ejen mencuba penerbangan alternatif atau memaklumkan pengguna tentang isu itu dengan lebih bermaklumat dalam cubaan berikutnya.

#### Memori Entiti

Ini melibatkan mengekstrak dan mengingati entiti spesifik (seperti orang, tempat, atau benda) dan peristiwa daripada perbualan. Ia membolehkan ejen membina pemahaman berstruktur tentang elemen penting yang dibincangkan.

**Contoh Memori Entiti**

Daripada perbualan mengenai perjalanan lalu, ejen mungkin mengekstrak "Paris," "Menara Eiffel," dan "makan malam di restoran Le Chat Noir" sebagai entiti. Dalam interaksi masa depan, ejen boleh mengingati "Le Chat Noir" dan menawarkan untuk membuat tempahan baru di sana.

#### RAG Berstruktur (Penjanaan Beraugmen Pengambilan)

Walaupun RAG adalah teknik yang lebih luas, "RAG Berstruktur" diserlahkan sebagai teknologi memori yang kuat. Ia mengekstrak maklumat berstruktur yang padat daripada pelbagai sumber (perbualan, emel, imej) dan menggunakannya untuk meningkatkan ketepatan, pengambilan, dan kelajuan respons. Berbeza dengan RAG klasik yang bergantung hanya pada kesamaan semantik, RAG Berstruktur berfungsi dengan struktur maklumat yang sedia ada.

**Contoh RAG Berstruktur**

Daripada hanya memadankan kata kunci, RAG Berstruktur boleh memecahkan maklumat penerbangan (destinasi, tarikh, masa, syarikat penerbangan) daripada emel dan menyimpannya secara berstruktur. Ini membolehkan pertanyaan tepat seperti "Penerbangan apa yang saya tempah ke Paris pada hari Selasa?"

## Melaksanakan dan Menyimpan Memori

Melaksanakan memori untuk ejen AI melibatkan proses sistematik **pengurusan memori**, yang termasuk menjana, menyimpan, mengambil, mengintegrasi, mengemas kini, dan juga "melupakan" (atau memadam) maklumat. Pengambilan adalah aspek yang sangat penting.

### Alat Memori Khusus

#### Mem0

Salah satu cara untuk menyimpan dan mengurus memori ejen adalah menggunakan alat khusus seperti Mem0. Mem0 berfungsi sebagai lapisan memori berterusan, membolehkan ejen mengingati interaksi yang berkaitan, menyimpan keutamaan pengguna dan konteks faktual, serta belajar daripada kejayaan dan kegagalan dari masa ke masa. Idea di sini ialah ejen tanpa status berubah menjadi ejen dengan status.

Ia berfungsi melalui **tahap memori dua fasa: pengekstrakan dan kemaskini**. Pertama, mesej yang ditambah ke thread ejen dihantar ke perkhidmatan Mem0, yang menggunakan Model Bahasa Besar (LLM) untuk meringkaskan sejarah perbualan dan mengekstrak memori baru. Seterusnya, fasa kemaskini yang dikendalikan LLM menentukan sama ada untuk menambah, mengubah suai, atau memadam memori ini, menyimpannya dalam stor data hibrid yang boleh merangkumi pangkalan data vektor, graf, dan nilai-kunci. Sistem ini juga menyokong pelbagai jenis memori dan boleh memasukkan memori graf untuk menguruskan hubungan antara entiti.

#### Cognee

Satu lagi pendekatan berkuasa ialah menggunakan **Cognee**, memori semantik sumber terbuka untuk ejen AI yang menukar data berstruktur dan tidak berstruktur menjadi graf ilmu yang boleh dicari yang disokong oleh embeddings. Cognee menyediakan **arsitektur dua stor** yang menggabungkan carian kesamaan vektor dengan hubungan graf, membolehkan ejen memahami bukan sahaja apa maklumat yang serupa, tetapi bagaimana konsep saling berkaitan.

Ia cemerlang dalam **pengambilan hibrid** yang menggabungkan kesamaan vektor, struktur graf, dan penaakulan LLM - dari pencarian chunk mentah hingga menjawab soalan berasaskan graf. Sistem ini mengekalkan **memori hidup** yang berkembang dan bertambah sambil kekal boleh dicari sebagai satu graf bersambung, menyokong konteks sesi jangka pendek dan memori berterusan jangka panjang.

Tutorial nota Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) menunjukkan bagaimana membina lapisan memori bersatu ini, dengan contoh praktikal memproses pelbagai sumber data, memvisualisasikan graf ilmu, dan membuat pertanyaan dengan pelbagai strategi carian yang disesuaikan untuk keperluan ejen tertentu.

### Menyimpan Memori dengan RAG

Selain alat memori khusus seperti Mem0, anda boleh menggunakan perkhidmatan carian yang kukuh seperti **Azure AI Search sebagai backend untuk menyimpan dan mengambil memori**, terutamanya untuk RAG Berstruktur.

Ini membolehkan anda menguatkan respons ejen anda dengan data anda sendiri, memastikan jawapan lebih relevan dan tepat. Azure AI Search boleh digunakan untuk menyimpan memori perjalanan khusus pengguna, katalog produk, atau apa-apa pengetahuan domain khusus lain.

Azure AI Search menyokong keupayaan seperti **RAG Berstruktur**, yang cemerlang dalam mengekstrak dan mengambil maklumat berstruktur yang padat daripada set data besar seperti sejarah perbualan, emel, atau imej. Ini menyediakan "ketepatan dan pengambilan luar biasa melebihi manusia" berbanding pendekatan pencacahan teks dan embeddings tradisional.

## Menjadikan Ejen AI Memperbaiki Diri Sendiri

Corak biasa untuk ejen yang memperbaiki diri melibatkan memperkenalkan **"ejen ilmu"**. Ejen berasingan ini memerhati perbualan utama antara pengguna dan ejen utama. Peranannya adalah untuk:

1. **Kenal pasti maklumat berharga**: Menentukan sama ada sebarang bahagian perbualan patut disimpan sebagai ilmu umum atau keutamaan pengguna khusus.

2. **Ekstrak dan ringkaskan**: Memadatkan pembelajaran atau keutamaan penting dari perbualan.

3. **Simpan dalam pangkalan ilmu**: Menyimpan maklumat yang diekstrak ini, selalunya dalam pangkalan data vektor, supaya ia boleh diambil kemudian.

4. **Menguatkan pertanyaan akan datang**: Apabila pengguna memulakan pertanyaan baru, ejen ilmu mengambil maklumat relevan yang disimpan dan menyertakannya ke dalam arahan pengguna, menyediakan konteks penting kepada ejen utama (serupa dengan RAG).

### Pengoptimuman untuk Memori

• **Pengurusan Latensi**: Untuk mengelakkan melambatkan interaksi pengguna, model yang lebih murah dan pantas boleh digunakan pada mulanya untuk memeriksa dengan cepat jika maklumat itu berbaloi untuk disimpan atau diambil, hanya menggunakan proses ekstrak/pengambilan yang lebih kompleks apabila perlu.

• **Penyelenggaraan Pangkalan Ilmu**: Untuk pangkalan ilmu yang berkembang, maklumat yang kurang kerap digunakan boleh dipindahkan ke "penyimpanan sejuk" bagi mengurus kos.

## Ada Lagi Soalan Mengenai Memori Ejen?

Sertai [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) untuk berjumpa dengan pelajar lain, menghadiri waktu pejabat dan dapatkan jawapan untuk soalan Anda mengenai Ejen AI.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk mencapai ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->