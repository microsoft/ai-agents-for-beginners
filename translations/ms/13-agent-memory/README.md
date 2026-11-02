# Memori untuk Ejen AI 
[![Agent Memory](../../../translated_images/ms/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Apabila membincangkan manfaat unik dalam mencipta Ejen AI, dua perkara utama dibincangkan: keupayaan untuk memanggil alat bagi menyelesaikan tugas dan keupayaan untuk memperbaiki diri dari masa ke masa. Memori adalah asas dalam mencipta ejen yang mampu memperbaiki diri yang dapat menghasilkan pengalaman lebih baik untuk pengguna kita.

Dalam pelajaran ini, kita akan melihat apa itu memori untuk Ejen AI dan bagaimana kita boleh menguruskannya dan menggunakannya demi manfaat aplikasi kita.

## Pengenalan

Pelajaran ini akan merangkumi:

• **Memahami Memori Ejen AI**: Apa itu memori dan mengapa ia penting untuk ejen.

• **Melaksanakan dan Menyimpan Memori**: Kaedah praktikal untuk menambah kemampuan memori ke dalam ejen AI anda, dengan fokus pada memori jangka pendek dan jangka panjang.

• **Menjadikan Ejen AI Memperbaiki Diri Sendiri**: Bagaimana memori membolehkan ejen belajar dari interaksi lalu dan memperbaiki diri dari masa ke masa.

## Pelaksanaan Sedia Ada

Pelajaran ini termasuk dua tutorial buku nota komprehensif:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Melaksanakan memori menggunakan Mem0 dan Azure AI Search dengan Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Melaksanakan memori berstruktur menggunakan Cognee, secara automatik membina graf pengetahuan yang disokong oleh embeddings, memvisualisasikan graf, dan pengambilan pintar

## Matlamat Pembelajaran

Selepas menamatkan pelajaran ini, anda akan tahu bagaimana untuk:

• **Membezakan antara pelbagai jenis memori ejen AI**, termasuk memori kerja, jangka pendek, dan jangka panjang, serta bentuk khusus seperti persona dan memori episodik.

• **Melaksanakan dan mengurus memori jangka pendek dan jangka panjang untuk ejen AI** menggunakan Microsoft Agent Framework, memanfaatkan alat seperti Mem0, Cognee, memori papan putih, dan mengintegrasikan dengan Azure AI Search.

• **Memahami prinsip di sebalik ejen AI yang memperbaiki diri sendiri** dan bagaimana sistem pengurusan memori yang mantap menyumbang kepada pembelajaran dan penyesuaian berterusan.

## Memahami Memori Ejen AI

Pada intinya, **memori untuk ejen AI merujuk kepada mekanisme yang membolehkan mereka mengekalkan dan mengingati maklumat**. Maklumat ini boleh jadi butiran khusus tentang perbualan, keutamaan pengguna, tindakan lalu, atau corak yang dipelajari.

Tanpa memori, aplikasi AI biasanya tidak mempunyai status, yang bermaksud setiap interaksi bermula dari kosong. Ini menyebabkan pengalaman pengguna yang berulang dan mengecewakan di mana ejen "lupa" konteks atau keutamaan sebelumnya.

### Mengapa Memori Penting?

Kecerdasan ejen sangat berkait rapat dengan keupayaannya untuk mengingati dan menggunakan maklumat lalu. Memori membolehkan ejen menjadi:

• **Reflektif**: Belajar dari tindakan dan hasil lalu.

• **Interaktif**: Mengekalkan konteks sepanjang perbualan yang sedang berlangsung.

• **Proaktif dan Reaktif**: Mengantisipasi keperluan atau bertindak balas secara sesuai berdasarkan data sejarah.

• **Autonomi**: Beroperasi lebih berdikari dengan memanfaatkan pengetahuan tersimpan.

Matlamat pelaksanaan memori ialah menjadikan ejen lebih **boleh dipercayai dan berupaya**.

### Jenis Memori

#### Memori Kerja

Anggaplah ini sebagai sekeping kertas konsep yang digunakan ejen semasa satu tugas atau proses pemikiran yang sedang berlangsung. Ia memegang maklumat segera yang diperlukan untuk mengira langkah seterusnya.

Untuk ejen AI, memori kerja sering menampung maklumat paling relevan daripada perbualan, walaupun sejarah chat penuh adalah panjang atau dipotong. Ia memberi tumpuan pada pengambilan elemen utama seperti keperluan, cadangan, keputusan, dan tindakan.

**Contoh Memori Kerja**

Dalam ejen tempahan perjalanan, memori kerja mungkin menangkap permintaan semasa pengguna, seperti "Saya mahu menempah perjalanan ke Paris". Keperluan khusus ini disimpan dalam konteks segera ejen untuk membimbing interaksi semasa.

#### Memori Jangka Pendek

Jenis memori ini mengekalkan maklumat sepanjang satu perbualan atau sesi tunggal. Ia adalah konteks chat semasa, membolehkan ejen merujuk kembali kepada giliran perbualan sebelumnya.

Dalam contoh SDK Python [Microsoft Agent Framework](https://github.com/microsoft/agent-framework), ini dipetakan kepada `AgentSession`, yang dibuat dengan `agent.create_session()`. Sesi ini adalah memori jangka pendek terbina dalam rangka kerja: ia mengekalkan konteks perbualan semasa sesi yang sama digunakan kembali, tetapi konteks itu tidak disimpan apabila sesi tamat atau aplikasi dimulakan semula. Gunakan memori jangka panjang untuk fakta dan keutamaan yang perlu bertahan merentas sesi, biasanya melalui pangkalan data, indeks vektor, atau storan berterusan lain.

**Contoh Memori Jangka Pendek**

Jika pengguna bertanya, "Berapa kos penerbangan ke Paris?" dan kemudian bertanya, "Bagaimana pula dengan penginapan di sana?", memori jangka pendek memastikan ejen tahu "di sana" merujuk kepada "Paris" dalam perbualan yang sama.

#### Memori Jangka Panjang

Ini adalah maklumat yang bertahan merentas beberapa perbualan atau sesi. Ia membolehkan ejen mengingati keutamaan pengguna, interaksi sejarah, atau pengetahuan umum selama tempoh yang panjang. Ini penting untuk penyesuaian peribadi.

**Contoh Memori Jangka Panjang**

Memori jangka panjang mungkin menyimpan bahawa "Ben menikmati bermain ski dan aktiviti luar, suka kopi dengan pemandangan gunung, dan mahu elakkan lereng ski lanjutan akibat kecederaan lalu". Maklumat ini, yang dipelajari dari interaksi sebelumnya, mempengaruhi cadangan dalam sesi perancangan perjalanan akan datang, menjadikannya sangat diperibadikan.

#### Memori Persona

Jenis memori khusus ini membantu ejen membina "personaliti" atau "persona" yang konsisten. Ia membolehkan ejen mengingati butiran tentang dirinya atau peranan yang diinginkan, menjadikan interaksi lebih lancar dan fokus.

**Contoh Memori Persona**
Jika ejen perjalanan direka sebagai "perancang ski pakar," memori persona mungkin menguatkan peranan ini, mempengaruhi tindak balasnya selaras dengan nada dan pengetahuan seorang pakar.

#### Memori Alur Kerja/Episodik

Memori ini menyimpan urutan langkah yang diambil ejen semasa tugas kompleks, termasuk kejayaan dan kegagalan. Ia seperti mengingati "episod" tertentu atau pengalaman lalu untuk belajar daripadanya.

**Contoh Memori Episodik**

Jika ejen cuba menempah penerbangan tertentu tetapi gagal kerana tidak tersedia, memori episodik boleh merekodkan kegagalan ini, membolehkan ejen mencuba penerbangan alternatif atau memaklumkan pengguna tentang isu itu dengan cara yang lebih bermaklumat semasa cubaan berikutnya.

#### Memori Entiti

Ini melibatkan mengekstrak dan mengingati entiti khusus (seperti orang, tempat, atau barang) dan peristiwa dari perbualan. Ia membolehkan ejen membina pemahaman berstruktur tentang elemen utama yang dibincangkan.

**Contoh Memori Entiti**

Dari perbualan tentang perjalanan lalu, ejen mungkin mengekstrak "Paris," "Menara Eiffel," dan "makan malam di restoran Le Chat Noir" sebagai entiti. Dalam interaksi masa depan, ejen boleh mengingati "Le Chat Noir" dan menawarkan untuk membuat tempahan baru di sana.

#### Structured RAG (Generasi Diperkaya Pengambilan)

Walaupun RAG adalah teknik yang lebih luas, "Structured RAG" diketengahkan sebagai teknologi memori yang powerfull. Ia mengekstrak maklumat yang padat dan berstruktur dari pelbagai sumber (perbualan, e-mel, imej) dan menggunakannya untuk meningkatkan ketepatan, pengambilan, dan kelajuan dalam tindak balas. Berbeza dengan RAG klasik yang bergantung hanya pada kesamaan semantik, Structured RAG berfungsi dengan struktur maklumat yang melekat.

**Contoh Structured RAG**

Daripada hanya memadankan kata kunci, Structured RAG boleh mengurai butiran penerbangan (destinasi, tarikh, masa, syarikat penerbangan) dari e-mel dan menyimpannya secara berstruktur. Ini membolehkan pertanyaan tepat seperti "Penerbangan apa yang saya tempah ke Paris pada hari Selasa?"

## Melaksanakan dan Menyimpan Memori

Melaksanakan memori untuk ejen AI melibatkan proses sistematik **pengurusan memori**, yang termasuk menjana, menyimpan, mengambil, mengintegrasi, mengemas kini, dan bahkan "melupakan" (atau memadam) maklumat. Pengambilan adalah aspek yang amat penting.

### Alat Memori Khusus

#### Mem0

Salah satu cara untuk menyimpan dan mengurus memori ejen adalah menggunakan alat khusus seperti Mem0. Mem0 berfungsi sebagai lapisan memori berterusan, membolehkan ejen mengingati interaksi berkaitan, menyimpan keutamaan pengguna dan konteks faktual, dan belajar dari kejayaan serta kegagalan dari masa ke masa. Idea di sini ialah ejen tidak berstatus menjadi berstatus.

Ia berfungsi melalui **saluran memori dua fasa: pengestrakan dan kemas kini**. Pertama, mesej yang ditambah ke dalam rangkaian ejen dihantar ke perkhidmatan Mem0, yang menggunakan Model Bahasa Besar (LLM) untuk meringkaskan sejarah perbualan dan mengekstrak memori baru. Kemudian, fasa kemas kini dipacu LLM menentukan sama ada untuk menambah, mengubah, atau memadam memori ini, menyimpannya dalam stor data hibrid yang boleh merangkumi pangkalan data vektor, graf, dan kunci-nilai. Sistem ini juga menyokong pelbagai jenis memori dan boleh menggabungkan memori graf untuk mengurus hubungan antara entiti.

#### Cognee

Pendekatan kuat lain adalah menggunakan **Cognee**, memori semantik sumber terbuka untuk ejen AI yang mengubah data berstruktur dan tidak berstruktur menjadi graf pengetahuan yang boleh dipertanyakan disokong oleh embeddings. Cognee menyediakan **arsitektur penyimpanan berganda** yang menggabungkan carian kesamaan vektor dengan hubungan graf, membolehkan ejen memahami bukan sahaja maklumat yang serupa, tetapi bagaimana konsep berkaitan antara satu sama lain.

Ia unggul dalam **pengambilan hibrid** yang menggabungkan kesamaan vektor, struktur graf, dan penaakulan LLM - dari pencarian bahagian mentah hingga menjawab soalan berasaskan graf. Sistem ini mengekalkan **memori hidup** yang berkembang dan bertambah sambil kekal boleh dipertanyakan sebagai satu graf yang berhubung, menyokong konteks sesi jangka pendek dan memori berterusan jangka panjang.

Tutorial buku nota Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) menunjukkan pembinaan lapisan memori bersatu ini, dengan contoh praktikal mengambil pelbagai sumber data, memvisualisasikan graf pengetahuan, dan bertanya dengan strategi carian berbeza yang disesuaikan dengan keperluan ejen tertentu.

### Menyimpan Memori dengan RAG

Selain alat memori khusus seperti Mem0, anda boleh memanfaatkan perkhidmatan carian mantap seperti **Azure AI Search sebagai backend untuk menyimpan dan mengambil memori**, terutama untuk Structured RAG.

Ini membolehkan anda menyandarkan jawapan ejen anda dengan data anda sendiri, memastikan jawapan yang lebih relevan dan tepat. Azure AI Search boleh digunakan untuk menyimpan memori perjalanan khusus pengguna, katalog produk, atau apa-apa pengetahuan domain lain.

Azure AI Search menyokong keupayaan seperti **Structured RAG**, yang unggul dalam mengekstrak dan mengambil maklumat padat dan berstruktur dari dataset besar seperti sejarah perbualan, e-mel, atau imej. Ini memberikan "ketepatan dan pengambilan superhuman" berbanding pendekatan pemecahan teks dan embedding tradisional.

## Menjadikan Ejen AI Memperbaiki Diri Sendiri

Corak biasa untuk ejen yang memperbaiki diri sendiri melibatkan pengenalan **"ejen pengetahuan"**. Ejen berasingan ini mengawasi perbualan utama antara pengguna dan ejen utama. Peranannya ialah untuk:

1. **Kenal pasti maklumat berharga**: Tentukan jika mana-mana bahagian perbualan perlu disimpan sebagai pengetahuan umum atau keutamaan pengguna spesifik.

2. **Ekstrak dan rumuskan**: Menyatukan pembelajaran atau keutamaan penting dari perbualan.

3. **Simpan dalam pangkalan pengetahuan**: Kekalkan maklumat yang dikutip ini, seringkali dalam pangkalan data vektor supaya ia boleh diambil kemudian.

4. **Tambah baik pertanyaan masa depan**: Apabila pengguna memulakan pertanyaan baru, ejen pengetahuan mengambil maklumat tersimpan yang relevan dan menambahkannya ke petikan pengguna, menyediakan konteks penting kepada ejen utama (serupa dengan RAG).

### Pengoptimuman untuk Memori

• **Pengurusan Latensi**: Untuk mengelakkan perlahan interaksi pengguna, model lebih murah dan pantas boleh digunakan pada mulanya untuk memeriksa dengan cepat jika maklumat berharga untuk disimpan atau diambil, hanya melibatkan proses ekstrak/pengambilan yang lebih kompleks jika perlu.

• **Penyelenggaraan Pangkalan Pengetahuan**: Untuk pangkalan pengetahuan yang semakin berkembang, maklumat yang kurang kerap digunakan boleh dipindahkan ke "stok sejuk" untuk menguruskan kos.

## Ada Soalan Lagi Mengenai Memori Ejen?

Sertai [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) untuk bertemu dengan pelajar lain, menghadiri waktu pejabat dan dapatkan jawapan untuk soalan anda tentang Ejen AI.
## Pelajaran Sebelumnya

[Reka Bentuk Konteks untuk Ejen AI](../12-context-engineering/README.md)

## Pelajaran Seterusnya

[Meneroka Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->