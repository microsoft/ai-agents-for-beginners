# Memori untuk Agen AI 
[![Agent Memory](../../../translated_images/id/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Saat membahas manfaat unik dari pembuatan Agen AI, dua hal yang terutama dibahas: kemampuan untuk memanggil alat untuk menyelesaikan tugas dan kemampuan untuk meningkatkan diri seiring waktu. Memori adalah dasar dari pembuatan agen yang dapat meningkatkan diri sendiri yang dapat menciptakan pengalaman yang lebih baik bagi pengguna kami.

Dalam pelajaran ini, kita akan melihat apa itu memori untuk Agen AI dan bagaimana kita dapat mengelolanya serta menggunakannya untuk keuntungan aplikasi kita.

## Pendahuluan

Pelajaran ini akan membahas:

• **Memahami Memori Agen AI**: Apa itu memori dan mengapa itu penting bagi agen.

• **Mengimplementasikan dan Menyimpan Memori**: Metode praktis untuk menambahkan kemampuan memori pada agen AI Anda, dengan fokus pada memori jangka pendek dan jangka panjang.

• **Membuat Agen AI Meningkatkan Diri Sendiri**: Bagaimana memori memungkinkan agen untuk belajar dari interaksi masa lalu dan meningkat seiring waktu.

## Implementasi yang Tersedia

Pelajaran ini mencakup dua tutorial notebook yang komprehensif:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Mengimplementasikan memori menggunakan Mem0 dan Azure AI Search dengan Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Mengimplementasikan memori terstruktur menggunakan Cognee, secara otomatis membangun grafik pengetahuan yang didukung oleh embeddings, memvisualisasikan grafik, dan pengambilan cerdas

## Tujuan Pembelajaran

Setelah menyelesaikan pelajaran ini, Anda akan mengetahui cara untuk:

• **Membedakan antara berbagai jenis memori agen AI**, termasuk memori kerja, jangka pendek, dan jangka panjang, serta bentuk khusus seperti persona dan memori episodik.

• **Mengimplementasikan dan mengelola memori jangka pendek dan jangka panjang untuk agen AI** menggunakan Microsoft Agent Framework, memanfaatkan alat seperti Mem0, Cognee, memori Whiteboard, dan integrasi dengan Azure AI Search.

• **Memahami prinsip di balik agen AI yang meningkatkan diri sendiri** dan bagaimana sistem manajemen memori yang kuat berkontribusi pada pembelajaran dan adaptasi yang berkelanjutan.

## Memahami Memori Agen AI

Pada intinya, **memori untuk agen AI merujuk pada mekanisme yang memungkinkan mereka menyimpan dan mengingat informasi**. Informasi ini bisa berupa detail spesifik tentang percakapan, preferensi pengguna, tindakan sebelumnya, atau bahkan pola yang dipelajari.

Tanpa memori, aplikasi AI sering kali tidak menyimpan status, artinya setiap interaksi dimulai dari awal. Ini menyebabkan pengalaman pengguna yang berulang dan membuat frustrasi di mana agen "melupakan" konteks atau preferensi sebelumnya.

### Mengapa Memori Penting?

kecerdasan agen sangat terkait dengan kemampuannya untuk mengingat dan memanfaatkan informasi masa lalu. Memori memungkinkan agen untuk menjadi:

• **Reflektif**: Belajar dari tindakan dan hasil masa lalu.

• **Interaktif**: Mempertahankan konteks selama percakapan yang sedang berlangsung.

• **Proaktif dan Reaktif**: Mengantisipasi kebutuhan atau merespons secara tepat berdasarkan data historis.

• **Otonom**: Beroperasi lebih mandiri dengan memanfaatkan pengetahuan yang tersimpan.

Tujuan pengimplementasian memori adalah untuk membuat agen lebih **andal dan kapabel**.

### Jenis Memori

#### Memori Kerja

Anggap ini sebagai selembar kertas coret-coret yang digunakan agen selama satu tugas atau proses berpikir yang berlangsung. Memori ini menyimpan informasi langsung yang diperlukan untuk menghitung langkah selanjutnya.

Untuk agen AI, memori kerja sering menangkap informasi yang paling relevan dari sebuah percakapan, bahkan jika riwayat obrolan penuh sangat panjang atau terpotong. Fokusnya adalah mengekstrak elemen kunci seperti kebutuhan, proposal, keputusan, dan tindakan.

**Contoh Memori Kerja**

Dalam agen pemesanan perjalanan, memori kerja mungkin menangkap permintaan saat ini dari pengguna, seperti "Saya ingin memesan perjalanan ke Paris". Kebutuhan spesifik ini disimpan dalam konteks langsung agen untuk memandu interaksi saat ini.

#### Memori Jangka Pendek

Jenis memori ini menyimpan informasi selama durasi satu percakapan atau sesi. Ini adalah konteks obrolan saat ini, memungkinkan agen merujuk kembali ke giliran sebelumnya dalam dialog.

Dalam contoh SDK Python [Microsoft Agent Framework](https://github.com/microsoft/agent-framework), ini dipetakan ke `AgentSession`, yang dibuat dengan `agent.create_session()`. Sesi ini adalah memori jangka pendek bawaan framework: ia menjaga konteks percakapan tetap tersedia selama sesi yang sama digunakan kembali, tetapi konteks itu tidak dipertahankan ketika sesi berakhir atau aplikasi di-restart. Gunakan memori jangka panjang untuk fakta dan preferensi yang perlu bertahan antar sesi, biasanya melalui basis data, indeks vektor, atau penyimpanan persisten lainnya.

**Contoh Memori Jangka Pendek**

Jika seorang pengguna bertanya, "Berapa biaya penerbangan ke Paris?" dan kemudian melanjutkan dengan "Bagaimana dengan akomodasi di sana?", memori jangka pendek memastikan agen tahu bahwa "di sana" merujuk pada "Paris" dalam percakapan yang sama.

#### Memori Jangka Panjang

Ini adalah informasi yang bertahan selama beberapa percakapan atau sesi. Memori ini memungkinkan agen mengingat preferensi pengguna, interaksi historis, atau pengetahuan umum dalam jangka waktu yang lama. Ini penting untuk personalisasi.

**Contoh Memori Jangka Panjang**

Memori jangka panjang mungkin menyimpan bahwa "Ben menyukai ski dan aktivitas luar ruangan, suka kopi dengan pemandangan gunung, dan ingin menghindari jalur ski tingkat lanjut karena cedera sebelumnya". Informasi ini, yang dipelajari dari interaksi sebelumnya, mempengaruhi rekomendasi dalam sesi perencanaan perjalanan berikutnya, menjadikannya sangat personal.

#### Memori Persona

Jenis memori khusus ini membantu agen mengembangkan "kepribadian" atau "persona" yang konsisten. Memori ini memungkinkan agen mengingat detail tentang dirinya sendiri atau perannya yang dimaksudkan, sehingga interaksi menjadi lebih lancar dan terfokus.

**Contoh Memori Persona**
Jika agen perjalanan dirancang sebagai "perencana ski ahli," memori persona mungkin memperkuat peran ini, mempengaruhi responsnya agar selaras dengan nada dan pengetahuan seorang ahli.

#### Memori Workflow/Episodik

Memori ini menyimpan urutan langkah yang diambil agen selama tugas kompleks, termasuk keberhasilan dan kegagalan. Ini seperti mengingat "episode" khusus atau pengalaman masa lalu untuk belajar darinya.

**Contoh Memori Episodik**

Jika agen mencoba memesan penerbangan tertentu tapi gagal karena ketidaktersediaan, memori episodik dapat merekam kegagalan ini, memungkinkan agen mencoba alternatif penerbangan atau memberi tahu pengguna tentang masalah dengan cara yang lebih tepat pada usaha berikutnya.

#### Memori Entitas

Ini melibatkan ekstraksi dan penyimpanan entitas spesifik (seperti orang, tempat, atau benda) dan peristiwa dari percakapan. Memori ini memungkinkan agen membangun pemahaman terstruktur tentang elemen kunci yang dibahas.

**Contoh Memori Entitas**

Dari percakapan mengenai perjalanan sebelumnya, agen mungkin mengekstraksi "Paris," "Menara Eiffel," dan "makan malam di restoran Le Chat Noir" sebagai entitas. Dalam interaksi berikutnya, agen dapat mengingat "Le Chat Noir" dan menawarkan untuk membuat reservasi baru di sana.

#### Structured RAG (Retrieval Augmented Generation)

Meskipun RAG adalah teknik yang lebih luas, "Structured RAG" disorot sebagai teknologi memori yang kuat. Teknik ini mengekstrak informasi padat dan terstruktur dari berbagai sumber (percakapan, email, gambar) dan menggunakannya untuk meningkatkan presisi, recall, dan kecepatan dalam respons. Berbeda dengan RAG klasik yang hanya mengandalkan kesamaan semantik, Structured RAG bekerja dengan struktur inheren dari informasi.

**Contoh Structured RAG**

Alih-alih hanya mencocokkan kata kunci, Structured RAG dapat mem-parsing detail penerbangan (tujuan, tanggal, waktu, maskapai) dari email dan menyimpannya secara terstruktur. Ini memungkinkan pertanyaan yang tepat seperti "Penerbangan apa yang saya pesan ke Paris pada hari Selasa?"

## Mengimplementasikan dan Menyimpan Memori

Mengimplementasikan memori untuk agen AI melibatkan proses sistematis **manajemen memori**, yang mencakup pembuatan, penyimpanan, pengambilan, integrasi, pembaruan, dan bahkan "lupa" (atau penghapusan) informasi. Pengambilan adalah aspek yang sangat penting.

### Alat Memori Khusus

#### Mem0

Salah satu cara untuk menyimpan dan mengelola memori agen adalah dengan menggunakan alat khusus seperti Mem0. Mem0 berfungsi sebagai lapisan memori persisten, memungkinkan agen mengingat interaksi relevan, menyimpan preferensi pengguna dan konteks faktual, serta belajar dari keberhasilan dan kegagalan dari waktu ke waktu. Ide di sini adalah bahwa agen tanpa status berubah menjadi agen dengan status.

Ini bekerja melalui **pipeline memori dua fase: ekstraksi dan pembaruan**. Pertama, pesan yang ditambahkan ke utas agen dikirim ke layanan Mem0, yang menggunakan Large Language Model (LLM) untuk meringkas riwayat percakapan dan mengekstrak memori baru. Selanjutnya, fase pembaruan yang digerakkan oleh LLM menentukan apakah memori ini akan ditambahkan, dimodifikasi, atau dihapus, menyimpannya dalam penyimpanan data hibrid yang bisa mencakup database vektor, grafik, dan key-value. Sistem ini juga mendukung berbagai jenis memori dan dapat memasukkan memori grafik untuk mengelola hubungan antar entitas.

#### Cognee

Pendekatan kuat lainnya adalah menggunakan **Cognee**, memori semantik sumber terbuka untuk agen AI yang mengubah data terstruktur dan tidak terstruktur menjadi grafik pengetahuan yang dapat diquery dengan didukung oleh embeddings. Cognee menyediakan **arsitektur penyimpanan ganda** yang menggabungkan pencarian kesamaan vektor dengan hubungan grafik, memungkinkan agen memahami tidak hanya informasi apa yang mirip, tetapi bagaimana konsep saling berhubungan.

Cognee unggul dalam **pengambilan hybrid** yang memadukan kesamaan vektor, struktur grafik, dan penalaran LLM - mulai dari pencarian potongan mentah hingga tanya jawab yang sadar grafik. Sistem mempertahankan **memori hidup** yang berkembang dan tumbuh sementara tetap bisa diquery sebagai satu grafik yang terhubung, mendukung konteks sesi jangka pendek dan memori persisten jangka panjang.

Tutorial notebook Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) menunjukkan bagaimana membangun lapisan memori terpadu ini, dengan contoh praktis mengimpor berbagai sumber data, memvisualisasikan grafik pengetahuan, dan melakukan query dengan strategi pencarian berbeda yang disesuaikan dengan kebutuhan agen tertentu.

### Menyimpan Memori dengan RAG

Selain alat memori khusus seperti Mem0, Anda dapat memanfaatkan layanan pencarian yang kuat seperti **Azure AI Search sebagai backend untuk menyimpan dan mengambil memori**, terutama untuk Structured RAG.

Ini memungkinkan Anda mengaitkan respons agen dengan data Anda sendiri, memastikan jawaban lebih relevan dan akurat. Azure AI Search dapat digunakan untuk menyimpan memori perjalanan spesifik pengguna, katalog produk, atau pengetahuan domain lainnya.

Azure AI Search mendukung kemampuan seperti **Structured RAG**, yang unggul dalam mengekstrak dan mengambil informasi padat dan terstruktur dari kumpulan data besar seperti riwayat percakapan, email, atau bahkan gambar. Ini memberikan "presisi dan recall superhuman" dibandingkan pendekatan teks chunking dan embedding tradisional.

## Membuat Agen AI Meningkatkan Diri Sendiri

Pola umum untuk agen yang meningkatkan diri sendiri melibatkan pengenalan **"agen pengetahuan"**. Agen terpisah ini mengamati percakapan utama antara pengguna dan agen utama. Perannya adalah:

1. **Mengidentifikasi informasi berharga**: Menentukan apakah bagian percakapan layak disimpan sebagai pengetahuan umum atau preferensi pengguna spesifik.

2. **Ekstrak dan ringkas**: Mencairkan pembelajaran atau preferensi penting dari percakapan.

3. **Simpan di basis pengetahuan**: Mempertahankan informasi yang diambil ini, sering kali dalam database vektor, agar dapat diambil kembali nanti.

4. **Lengkapi kueri masa depan**: Ketika pengguna memulai kueri baru, agen pengetahuan mengambil informasi yang relevan dan menambahkannya ke prompt pengguna, memberikan konteks penting kepada agen utama (mirip RAG).

### Optimalisasi untuk Memori

• **Manajemen Latensi**: Untuk menghindari memperlambat interaksi pengguna, model yang lebih murah dan lebih cepat dapat digunakan awalnya untuk dengan cepat memeriksa apakah informasi layak disimpan atau diambil, baru kemudian memanggil proses ekstraksi/pengambilan yang lebih kompleks jika perlu.

• **Pemeliharaan Basis Pengetahuan**: Untuk basis pengetahuan yang terus berkembang, informasi yang jarang digunakan dapat dipindahkan ke "cold storage" untuk mengelola biaya.

## Punya Pertanyaan Lebih Lanjut Tentang Memori Agen?

Bergabunglah dengan [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) untuk bertemu dengan pelajar lain, mengikuti jam kantor, dan mendapatkan jawaban atas pertanyaan Anda tentang Agen AI.
## Pelajaran Sebelumnya

[Context Engineering for AI Agents](../12-context-engineering/README.md)

## Pelajaran Berikutnya

[Exploring Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->