# Memori untuk Ejen AI 
[![Agent Memory](../../../translated_images/ms/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Apabila membincangkan faedah unik mencipta Ejen AI, dua perkara utama dibincangkan: keupayaan untuk memanggil alat untuk menyiapkan tugasan dan keupayaan untuk memperbaiki diri dari semasa ke semasa. Memori adalah asas untuk mencipta ejen yang memperbaiki diri yang boleh menghasilkan pengalaman yang lebih baik untuk pengguna kita.

Dalam pelajaran ini, kita akan melihat apa itu memori untuk Ejen AI dan bagaimana kita dapat mengurus serta menggunakannya demi manfaat aplikasi kita.

## Pengenalan

Pelajaran ini akan merangkumi:

• **Memahami Memori Ejen AI**: Apa itu memori dan mengapa ia penting untuk ejen.

• **Melaksanakan dan Menyimpan Memori**: Kaedah praktikal untuk menambah ciri memori pada ejen AI anda, dengan fokus pada memori jangka pendek dan jangka panjang.

• **Menjadikan Ejen AI Memperbaiki Diri**: Bagaimana memori membolehkan ejen belajar daripada interaksi lalu dan bertambah baik dari masa ke masa.

## Pelaksanaan yang Tersedia

Pelajaran ini merangkumi dua tutorial buku nota komprehensif:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Melaksanakan memori menggunakan Mem0 dan Azure AI Search dengan Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Melaksanakan memori berstruktur menggunakan Cognee, membina graf pengetahuan secara automatik yang disokong oleh embeddings, memvisualisasikan graf, dan pengambilan pintar

## Matlamat Pembelajaran

Selepas menamatkan pelajaran ini, anda akan tahu bagaimana untuk:

• **Membezakan antara pelbagai jenis memori ejen AI**, termasuk memori kerja, jangka pendek, dan jangka panjang, serta bentuk khusus seperti memori persona dan episodik.

• **Melaksanakan dan mengurus memori jangka pendek dan jangka panjang untuk ejen AI** menggunakan Microsoft Agent Framework, memanfaatkan alat seperti Mem0, Cognee, memori Whiteboard, dan mengintegrasi dengan Azure AI Search.

• **Memahami prinsip di sebalik ejen AI yang memperbaiki diri** dan bagaimana sistem pengurusan memori yang kukuh menyumbang kepada pembelajaran dan penyesuaian berterusan.

## Memahami Memori Ejen AI

Pada intinya, **memori untuk ejen AI merujuk kepada mekanisme yang membolehkan mereka mengekalkan dan mengimbas maklumat**. Maklumat ini boleh berupa butiran spesifik mengenai perbualan, keutamaan pengguna, tindakan lalu, atau bahkan corak yang dipelajari.

Tanpa memori, aplikasi AI sering kali tidak berstatus, bermakna setiap interaksi bermula dari kosong. Ini menyebabkan pengalaman pengguna yang berulang dan mengecewakan di mana ejen "lupa" konteks atau keutamaan sebelumnya.

### Kenapa Memori Penting?

Kecerdasan ejen sangat berkait rapat dengan keupayaannya untuk mengimbas dan menggunakan maklumat lalu. Memori membolehkan ejen untuk:

• **Reflektif**: Belajar daripada tindakan dan hasil lalu.

• **Interaktif**: Mengekalkan konteks sepanjang perbualan yang sedang berlangsung.

• **Proaktif dan Reaktif**: Menjangkakan keperluan atau bertindak balas dengan sesuai berdasarkan data sejarah.

• **Autonomi**: Beroperasi lebih berdikari dengan merujuk pengetahuan yang disimpan.

Matlamat melaksanakan memori adalah menjadikan ejen lebih **boleh dipercayai dan berupaya**.

### Jenis-Jenis Memori

#### Memori Kerja

Fikirkan ini sebagai sehelai kertas coretan yang digunakan oleh ejen semasa tugasan atau proses pemikiran yang sedang berlangsung. Ia menyimpan maklumat segera yang diperlukan untuk mengira langkah seterusnya.

Untuk ejen AI, memori kerja biasanya menangkap maklumat paling relevan daripada perbualan, walaupun sejarah sembang penuh panjang atau dipendekkan. Ia memfokuskan pada pengambilan elemen penting seperti keperluan, cadangan, keputusan, dan tindakan.

**Contoh Memori Kerja**

Dalam ejen tempahan perjalanan, memori kerja mungkin menangkap permintaan semasa pengguna, seperti "Saya mahu menempah perjalanan ke Paris". Keperluan khusus ini disimpan dalam konteks segera ejen untuk membimbing interaksi semasa.

#### Memori Jangka Pendek

Jenis memori ini menyimpan maklumat untuk tempoh satu perbualan atau sesi sahaja. Ia adalah konteks sembang semasa, membolehkan ejen merujuk kembali kepada giliran sebelumnya dalam dialog.

Dalam sampel SDK Python [Microsoft Agent Framework](https://github.com/microsoft/agent-framework), ini dipetakan kepada `AgentSession`, yang diwujudkan dengan `agent.create_session()`. Sesi ini adalah memori jangka pendek terbina dalam framework: ia menyimpan konteks perbualan yang tersedia selagi sesi yang sama digunakan semula, tetapi konteks itu tidak disimpan apabila sesi berakhir atau aplikasi dimulakan semula. Gunakan memori jangka panjang untuk fakta dan keutamaan yang perlu kekal merentasi sesi, biasanya melalui pangkalan data, indeks vektor atau penyimpanan kekal lain.

**Contoh Memori Jangka Pendek**

Jika pengguna bertanya, "Berapa kos penerbangan ke Paris?" dan kemudian mengikut dengan "Bagaimana pula dengan penginapan di sana?", memori jangka pendek memastikan ejen tahu "di sana" merujuk kepada "Paris" dalam perbualan yang sama.

#### Memori Jangka Panjang

Ini adalah maklumat yang kekal merentasi pelbagai perbualan atau sesi. Ia membolehkan ejen mengingati keutamaan pengguna, interaksi sejarah, atau pengetahuan umum dalam jangka masa panjang. Ini penting untuk personalisasi.

**Contoh Memori Jangka Panjang**

Memori jangka panjang mungkin menyimpan bahawa "Ben suka bermain ski dan aktiviti luar, gemar kopi dengan pemandangan gunung, dan mahu mengelak cerun ski lanjutan kerana kecederaan lalu". Maklumat ini, yang dipelajari dari interaksi sebelum ini, mempengaruhi cadangan dalam sesi perancangan perjalanan akan datang, menjadikannya sangat diperibadikan.

#### Memori Persona

Jenis memori khusus ini membantu ejen membangunkan "personaliti" atau "persona" yang konsisten. Ia membolehkan ejen mengingati butiran tentang dirinya atau peranan yang dimaksudkan, menjadikan interaksi lebih lancar dan fokus.

**Contoh Memori Persona**  
Jika ejen perjalanan direka sebagai "perancang ski pakar," memori persona boleh menguatkan peranan ini, mempengaruhi jawapan yang selaras dengan nada dan pengetahuan seorang pakar.

#### Memori Aliran Kerja/Episodik

Memori ini menyimpan urutan langkah yang diambil ejen semasa tugasan kompleks, termasuk kejayaan dan kegagalan. Ia seperti mengingati "episod" atau pengalaman lalu khusus untuk belajar daripadanya.

**Contoh Memori Episodik**

Jika ejen cuba menempah penerbangan tertentu tetapi gagal kerana ketidaktersediaan, memori episodik boleh merekodkan kegagalan ini, membolehkan ejen mencuba penerbangan alternatif atau memberitahu pengguna tentang isu tersebut dengan lebih berinformasi dalam cubaan berikutnya.

#### Memori Entiti

Ini melibatkan pengekstrakan dan mengingati entiti tertentu (seperti orang, tempat, atau benda) dan peristiwa dari perbualan. Ia membolehkan ejen membina pemahaman berstruktur mengenai elemen penting yang dibincangkan.

**Contoh Memori Entiti**

Daripada perbualan mengenai perjalanan lalu, ejen mungkin mengekstrak "Paris," "Menara Eiffel," dan "makan malam di restoran Le Chat Noir" sebagai entiti. Dalam interaksi akan datang, ejen boleh mengingati "Le Chat Noir" dan menawarkan untuk membuat tempahan baru di sana.

#### RAG Berstruktur (Retrieval Augmented Generation)

Walaupun RAG adalah teknik yang lebih luas, "RAG Berstruktur" diketengahkan sebagai teknologi memori yang kuat. Ia mengekstrak maklumat padat dan berstruktur dari pelbagai sumber (perbualan, emel, gambar) dan menggunakannya untuk meningkatkan ketepatan, keupayaan ingatan, dan kelajuan dalam respons. Berbeza dengan RAG klasik yang bergantung sepenuhnya pada kesamaan semantik, RAG Berstruktur beroperasi dengan struktur maklumat yang ada.

**Contoh RAG Berstruktur**

Daripada hanya memadankan kata kunci, RAG Berstruktur boleh menguraikan butiran penerbangan (destinasi, tarikh, masa, syarikat penerbangan) daripada emel dan menyimpannya secara berstruktur. Ini membolehkan pertanyaan tepat seperti "Penerbangan apa yang saya tempah ke Paris pada hari Selasa?"

## Melaksanakan dan Menyimpan Memori

Melaksanakan memori untuk ejen AI melibatkan proses sistematik **pengurusan memori**, yang merangkumi menjana, menyimpan, mengambil, mengintegrasi, mengemaskini, dan bahkan "melupakan" (atau memadam) maklumat. Pengambilan maklumat adalah aspek yang sangat penting.

### Alat Memori Khusus

#### Mem0

Salah satu cara untuk menyimpan dan mengurus memori ejen adalah menggunakan alat khusus seperti Mem0. Mem0 berfungsi sebagai lapisan memori kekal, membolehkan ejen mengingati interaksi relevan, menyimpan keutamaan pengguna dan konteks fakta, serta belajar daripada kejayaan dan kegagalan dari masa ke masa. Idea di sini ialah ejen tanpa status berubah menjadi ejen berstatus.

Ia beroperasi melalui **saluran memori dua fasa: ekstraksi dan kemaskini**. Pertama, mesej yang ditambah ke thread ejen dihantar ke perkhidmatan Mem0, yang menggunakan Model Bahasa Besar (LLM) untuk meringkaskan sejarah perbualan dan mengekstrak memori baru. Kemudian, fasa kemaskini yang dikawal LLM menentukan sama ada untuk menambah, mengubah, atau memadam memori tersebut, menyimpannya dalam stor data hibrid yang boleh merangkumi pangkalan data vektor, graf, dan kunci-nilai. Sistem ini juga menyokong pelbagai jenis memori dan boleh menggabungkan memori graf untuk mengurus hubungan antara entiti.

#### Cognee

Pendekatan berkuasa lain ialah menggunakan **Cognee**, memori semantik sumber terbuka untuk ejen AI yang menukar data berstruktur dan tidak berstruktur kepada graf pengetahuan yang boleh ditanya yang disokong oleh embeddings. Cognee menyediakan **arsitektur stor dua** yang menggabungkan carian kesamaan vektor dengan hubungan graf, membolehkan ejen memahami bukan sahaja apa maklumat yang serupa, tetapi bagaimana konsep berkait antara satu sama lain.

Ia cemerlang dalam **pengambilan hibrid** yang menggabungkan kesamaan vektor, struktur graf, dan penalaran LLM - dari carian kepingan mentah hingga menjawab soalan yang sedar graf. Sistem mengekalkan **memori hidup** yang berkembang dan bertambah sambil kekal boleh ditanya sebagai satu graf yang bersambung, menyokong konteks sesi jangka pendek dan memori jangka panjang yang kekal.

Tutorial buku nota Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) menunjukkan cara membina lapisan memori bersatu ini, dengan contoh praktikal mengimport pelbagai sumber data, memvisualisasikan graf pengetahuan, dan bertanya dengan strategi carian berlainan yang disesuaikan kepada keperluan ejen tertentu.

### Menyimpan Memori dengan RAG

Selain alat memori khusus seperti mem0, anda boleh menggunakan perkhidmatan carian kukuh seperti **Azure AI Search sebagai backend untuk menyimpan dan mendapatkan semula memori**, terutamanya untuk RAG berstruktur.

Ini membolehkan anda memberi asas kepada jawapan ejen dengan data anda sendiri, memastikan jawapan yang lebih relevan dan tepat. Azure AI Search boleh digunakan untuk menyimpan memori perjalanan khusus pengguna, katalog produk, atau apa-apa pengetahuan khusus domain lain.

Azure AI Search menyokong kebolehan seperti **RAG Berstruktur**, yang cemerlang dalam mengekstrak dan mengambil semula maklumat padat dan berstruktur daripada set data besar seperti sejarah perbualan, emel, atau malahan gambar. Ini menyediakan "ketepatan dan capaian super manusia" berbanding pendekatan pengekodan dan pemecahan teks tradisional.

## Membuat Ejen AI Memperbaiki Diri Sendiri

Corak biasa untuk ejen yang memperbaiki diri melibatkan memperkenalkan **"ejen pengetahuan"**. Ejen berasingan ini memerhati perbualan utama antara pengguna dan ejen utama. Peranannya adalah untuk:

1. **Kenal pasti maklumat bernilai**: Tentukan jika mana-mana bahagian perbualan berbaloi disimpan sebagai pengetahuan am atau keutamaan pengguna khusus.

2. **Ekstrak dan ringkaskan**: Meringkaskan pembelajaran penting atau keutamaan daripada perbualan.

3. **Simpan dalam pangkalan pengetahuan**: Menyimpan maklumat yang diekstrak ini, biasanya dalam pangkalan data vektor, supaya boleh diperoleh semula kemudian.

4. **Tambahkan pada pertanyaan masa depan**: Apabila pengguna memulakan pertanyaan baru, ejen pengetahuan mengambil maklumat tersimpan yang relevan dan menambahkannya pada arahan pengguna, menyediakan konteks penting kepada ejen utama (serupa dengan RAG).

### Pengoptimuman untuk Memori

• **Pengurusan Latensi**: Untuk mengelakkan memperlahankan interaksi pengguna, model yang lebih murah dan cepat boleh digunakan terlebih dahulu untuk pantas memeriksa sama ada maklumat berbaloi disimpan atau diambil, hanya mengaktifkan proses ekstraksi/pengambilan yang lebih kompleks bila perlu.

• **Penyelenggaraan Pangkalan Pengetahuan**: Untuk pangkalan pengetahuan yang semakin besar, maklumat yang kurang kerap digunakan boleh dipindahkan ke "stor sejuk" untuk mengurus kos.

## Ada Soalan Lagi Tentang Memori Ejen?

Sertai [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) untuk bertemu dengan pembelajar lain, menghadiri sesi kaunseling dan mendapatkan jawapan bagi soalan Anda tentang Ejen AI.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->