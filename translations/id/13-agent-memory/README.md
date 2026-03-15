# Memori untuk Agen AI 
[![Memori Agen](../../../translated_images/id/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Saat membahas manfaat unik dari membuat Agen AI, dua hal yang paling sering dibicarakan: kemampuan untuk memanggil alat untuk menyelesaikan tugas dan kemampuan untuk meningkat seiring waktu. Memori berada di dasar pembuatan agen yang dapat memperbaiki diri sendiri sehingga dapat menciptakan pengalaman yang lebih baik bagi pengguna kita.

Dalam pelajaran ini, kita akan melihat apa itu memori untuk Agen AI dan bagaimana kita dapat mengelolanya serta menggunakannya untuk keuntungan aplikasi kita.

## Introduction

Pelajaran ini akan membahas:

• **Understanding AI Agent Memory**: Apa itu memori dan mengapa itu penting bagi agen.

• **Implementing and Storing Memory**: Metode praktis untuk menambahkan kemampuan memori ke agen AI Anda, dengan fokus pada memori jangka pendek dan jangka panjang.

• **Making AI Agents Self-Improving**: Bagaimana memori memungkinkan agen belajar dari interaksi masa lalu dan meningkat seiring waktu.

## Available Implementations

Pelajaran ini mencakup dua tutorial notebook yang komprehensif:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Mengimplementasikan memori menggunakan Mem0 dan Azure AI Search dengan Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Mengimplementasikan memori terstruktur menggunakan Cognee, secara otomatis membangun knowledge graph yang didukung oleh embeddings, memvisualisasikan graf, dan pengambilan cerdas

## Learning Goals

Setelah menyelesaikan pelajaran ini, Anda akan tahu bagaimana:

• **Membedakan antara berbagai jenis memori agen AI**, termasuk working, short-term, dan long-term memory, serta bentuk khusus seperti persona dan episodic memory.

• **Mengimplementasikan dan mengelola memori jangka pendek dan jangka panjang untuk agen AI** menggunakan Microsoft Agent Framework, memanfaatkan alat seperti Mem0, Cognee, Whiteboard memory, dan integrasi dengan Azure AI Search.

• **Memahami prinsip di balik agen AI yang dapat memperbaiki diri sendiri** dan bagaimana sistem manajemen memori yang kuat berkontribusi pada pembelajaran dan adaptasi berkelanjutan.

## Understanding AI Agent Memory

Pada intinya, **memori untuk agen AI mengacu pada mekanisme yang memungkinkan mereka menyimpan dan mengingat informasi**. Informasi ini bisa berupa detail spesifik tentang percakapan, preferensi pengguna, tindakan sebelumnya, atau bahkan pola yang dipelajari.

Tanpa memori, aplikasi AI seringkali bersifat stateless, yang berarti setiap interaksi dimulai dari awal. Ini menyebabkan pengalaman pengguna yang repetitif dan membuat frustrasi di mana agen "lupa" konteks atau preferensi sebelumnya.

### Why is Memory Important?

kecerdasan agen sangat terkait dengan kemampuannya untuk mengingat dan memanfaatkan informasi masa lalu. Memori memungkinkan agen menjadi:

• **Reflective**: Belajar dari tindakan dan hasil masa lalu.

• **Interactive**: Mempertahankan konteks selama percakapan yang sedang berlangsung.

• **Proactive and Reactive**: Mengantisipasi kebutuhan atau merespons dengan tepat berdasarkan data historis.

• **Autonomous**: Beroperasi lebih mandiri dengan menarik pengetahuan yang tersimpan.

Tujuan mengimplementasikan memori adalah untuk membuat agen lebih **andal dan mampu**.

### Types of Memory

#### Working Memory

Anggap ini seperti selembar kertas catatan yang digunakan agen selama satu tugas atau proses berpikir yang sedang berlangsung. Ini menyimpan informasi segera yang diperlukan untuk menghitung langkah berikutnya.

Untuk agen AI, working memory sering menangkap informasi paling relevan dari percakapan, bahkan jika riwayat obrolan penuh panjang atau terpotong. Ini berfokus pada ekstraksi elemen kunci seperti persyaratan, proposal, keputusan, dan tindakan.

**Working Memory Example**

Dalam agen pemesanan perjalanan, working memory mungkin menangkap permintaan pengguna saat ini, seperti "Saya ingin memesan perjalanan ke Paris". Kebutuhan spesifik ini disimpan dalam konteks langsung agen untuk memandu interaksi saat ini.

#### Short Term Memory

Jenis memori ini menyimpan informasi untuk durasi satu percakapan atau sesi. Ini adalah konteks obrolan saat ini, memungkinkan agen merujuk kembali ke giliran sebelumnya dalam dialog.

**Short Term Memory Example**

Jika seorang pengguna bertanya, "Berapa biaya penerbangan ke Paris?" dan kemudian melanjutkan dengan "Bagaimana dengan akomodasi di sana?", short-term memory memastikan agen tahu bahwa "di sana" merujuk ke "Paris" dalam percakapan yang sama.

#### Long Term Memory

Ini adalah informasi yang bertahan di berbagai percakapan atau sesi. Ini memungkinkan agen mengingat preferensi pengguna, interaksi historis, atau pengetahuan umum selama periode yang panjang. Ini penting untuk personalisasi.

**Long Term Memory Example**

Memori jangka panjang mungkin menyimpan bahwa "Ben menyukai bermain ski dan aktivitas luar ruangan, suka kopi dengan pemandangan pegunungan, dan ingin menghindari lintasan ski tingkat lanjut karena cedera masa lalu". Informasi ini, yang dipelajari dari interaksi sebelumnya, memengaruhi rekomendasi di sesi perencanaan perjalanan di masa depan, membuatnya sangat dipersonalisasi.

#### Persona Memory

Jenis memori khusus ini membantu agen mengembangkan "kepribadian" atau "persona" yang konsisten. Ini memungkinkan agen mengingat detail tentang dirinya sendiri atau peran yang dimaksudkan, membuat interaksi lebih lancar dan terfokus.

**Persona Memory Example**
Jika agen perjalanan dirancang untuk menjadi "perencana ski ahli," persona memory mungkin memperkuat peran ini, memengaruhi tanggapannya agar selaras dengan nada dan pengetahuan seorang ahli.

#### Workflow/Episodic Memory

Memori ini menyimpan urutan langkah yang diambil agen selama tugas kompleks, termasuk keberhasilan dan kegagalan. Ini seperti mengingat "episode" spesifik atau pengalaman masa lalu untuk belajar darinya.

**Episodic Memory Example**

Jika agen berusaha memesan penerbangan tertentu tetapi gagal karena tidak tersedia, episodic memory dapat merekam kegagalan ini, memungkinkan agen mencoba penerbangan alternatif atau memberi tahu pengguna tentang masalah tersebut dengan cara yang lebih terinformasi saat percobaan berikutnya.

#### Entity Memory

Ini melibatkan ekstraksi dan pengingatan entitas spesifik (seperti orang, tempat, atau benda) dan kejadian dari percakapan. Ini memungkinkan agen membangun pemahaman terstruktur tentang elemen kunci yang dibahas.

**Entity Memory Example**

Dari percakapan tentang perjalanan masa lalu, agen mungkin mengekstrak "Paris," "Menara Eiffel," dan "makan malam di restoran Le Chat Noir" sebagai entitas. Dalam interaksi di masa depan, agen dapat mengingat "Le Chat Noir" dan menawarkan untuk membuat reservasi baru di sana.

#### Structured RAG (Retrieval Augmented Generation)

Sementara RAG adalah teknik yang lebih luas, "Structured RAG" disorot sebagai teknologi memori yang kuat. Ini mengekstrak informasi padat dan terstruktur dari berbagai sumber (percakapan, email, gambar) dan menggunakannya untuk meningkatkan presisi, recall, dan kecepatan dalam tanggapan. Berbeda dengan RAG klasik yang hanya mengandalkan kesamaan semantik, Structured RAG bekerja dengan struktur informasi itu sendiri.

**Structured RAG Example**

Alih-alih hanya mencocokkan kata kunci, Structured RAG dapat mem-parsing detail penerbangan (tujuan, tanggal, waktu, maskapai) dari sebuah email dan menyimpannya secara terstruktur. Ini memungkinkan kueri yang tepat seperti "Penerbangan apa yang saya pesan ke Paris pada hari Selasa?"

## Implementing and Storing Memory

Mengimplementasikan memori untuk agen AI melibatkan proses sistematis dari **manajemen memori**, yang mencakup menghasilkan, menyimpan, mengambil, mengintegrasikan, memperbarui, dan bahkan "melupakan" (atau menghapus) informasi. Pengambilan (retrieval) adalah aspek yang sangat penting.

### Specialized Memory Tools

#### Mem0

Salah satu cara untuk menyimpan dan mengelola memori agen adalah menggunakan alat khusus seperti Mem0. Mem0 berfungsi sebagai lapisan memori persisten, memungkinkan agen mengingat interaksi yang relevan, menyimpan preferensi pengguna dan konteks faktual, serta belajar dari keberhasilan dan kegagalan dari waktu ke waktu. Ide di sini adalah bahwa agen yang tadinya stateless berubah menjadi stateful.

Ini bekerja melalui **two-phase memory pipeline: extraction and update**. Pertama, pesan yang ditambahkan ke thread agen dikirim ke layanan Mem0, yang menggunakan sebuah Large Language Model (LLM) untuk meringkas riwayat percakapan dan mengekstrak memori baru. Selanjutnya, fase pembaruan yang digerakkan oleh LLM menentukan apakah akan menambahkan, memodifikasi, atau menghapus memori ini, menyimpannya dalam penyimpanan hibrida yang dapat mencakup basis data vektor, graf, dan key-value. Sistem ini juga mendukung berbagai jenis memori dan dapat memasukkan graph memory untuk mengelola hubungan antar entitas.

#### Cognee

Pendekatan kuat lainnya adalah menggunakan **Cognee**, memori semantik open-source untuk agen AI yang mengubah data terstruktur dan tidak terstruktur menjadi knowledge graph yang dapat di-query dan didukung oleh embeddings. Cognee menyediakan **dual-store architecture** yang menggabungkan pencarian kesamaan vektor dengan hubungan graf, memungkinkan agen memahami bukan hanya informasi apa yang serupa, tetapi juga bagaimana konsep saling terkait.

Cognee unggul dalam **hybrid retrieval** yang memadukan kesamaan vektor, struktur graf, dan penalaran LLM - dari pencarian potongan mentah hingga tanya jawab yang menyadari graf. Sistem ini mempertahankan **living memory** yang berevolusi dan tumbuh sambil tetap dapat di-query sebagai satu graf yang terhubung, mendukung konteks sesi jangka pendek dan memori persisten jangka panjang.

Tutorial notebook Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) menunjukkan pembangunan lapisan memori terpadu ini, dengan contoh praktis mengimpor berbagai sumber data, memvisualisasikan knowledge graph, dan melakukan kueri dengan strategi pencarian berbeda yang disesuaikan dengan kebutuhan agen tertentu.

### Storing Memory with RAG

Selain alat memori khusus seperti mem0 , Anda dapat memanfaatkan layanan pencarian yang tangguh seperti **Azure AI Search as a backend for storing and retrieving memories**, terutama untuk Structured RAG.

Ini memungkinkan Anda membumikan tanggapan agen dengan data Anda sendiri, memastikan jawaban yang lebih relevan dan akurat. Azure AI Search dapat digunakan untuk menyimpan memori perjalanan spesifik pengguna, katalog produk, atau pengetahuan domain khusus lainnya.

Azure AI Search mendukung kemampuan seperti **Structured RAG**, yang unggul dalam mengekstrak dan mengambil informasi padat dan terstruktur dari kumpulan data besar seperti riwayat percakapan, email, atau bahkan gambar. Ini memberikan "presisi dan recall superhuman" dibandingkan pendekatan pemecahan teks dan embedding tradisional.

## Making AI Agents Self-Improve

Pola umum untuk agen yang dapat memperbaiki diri melibatkan pengenalan sebuah **"knowledge agent"**. Agen terpisah ini mengamati percakapan utama antara pengguna dan agen utama. Perannya adalah untuk:

1. **Identify valuable information**: Menentukan apakah ada bagian dari percakapan yang layak disimpan sebagai pengetahuan umum atau preferensi pengguna tertentu.

2. **Extract and summarize**: Mendistilasi pembelajaran atau preferensi penting dari percakapan.

3. **Store in a knowledge base**: Menyimpan informasi yang diekstrak ini, seringkali dalam database vektor, sehingga dapat diambil nanti.

4. **Augment future queries**: Ketika pengguna memulai kueri baru, knowledge agent mengambil informasi yang relevan dan menambahkannya ke prompt pengguna, memberikan konteks penting kepada agen utama (mirip dengan RAG).

### Optimizations for Memory

• **Latency Management**: Untuk menghindari memperlambat interaksi pengguna, model yang lebih murah dan lebih cepat dapat digunakan awalnya untuk memeriksa dengan cepat apakah informasi tersebut berharga untuk disimpan atau diambil, hanya memanggil proses ekstraksi/pengambilan yang lebih kompleks ketika diperlukan.

• **Knowledge Base Maintenance**: Untuk basis pengetahuan yang terus tumbuh, informasi yang kurang sering digunakan dapat dipindahkan ke "cold storage" untuk mengelola biaya.

## Got More Questions About Agent Memory?

Join the [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) to meet with other learners, attend office hours and get your AI Agents questions answered.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Penafian:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI Co-op Translator (https://github.com/Azure/co-op-translator). Meskipun kami berupaya mencapai ketepatan, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang penting, disarankan menggunakan terjemahan profesional oleh penerjemah manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->