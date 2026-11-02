[![Agentic RAG](../../../translated_images/id/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Klik gambar di atas untuk melihat video pelajaran ini)_

# Agentic RAG

Pelajaran ini memberikan gambaran komprehensif tentang Agentic Retrieval-Augmented Generation (Agentic RAG), paradigma AI yang sedang berkembang di mana model bahasa besar (LLM) secara mandiri merencanakan langkah berikutnya sambil menarik informasi dari sumber eksternal. Berbeda dengan pola pengambilan data statis lalu membaca, Agentic RAG melibatkan panggilan iteratif ke LLM, diselingi dengan pemanggilan alat atau fungsi serta output terstruktur. Sistem mengevaluasi hasil, menyempurnakan kueri, memanggil alat tambahan jika diperlukan, dan melanjutkan siklus ini sampai solusi yang memuaskan tercapai.

## Pendahuluan

Pelajaran ini akan membahas

- **Memahami Agentic RAG:** Pelajari tentang paradigma AI yang sedang berkembang di mana model bahasa besar (LLM) secara mandiri merencanakan langkah selanjutnya sambil menarik informasi dari sumber data eksternal.
- **Memahami Gaya Iteratif Maker-Checker:** Pahami siklus panggilan iteratif ke LLM, diselingi pemanggilan alat atau fungsi dan output terstruktur, yang dirancang untuk meningkatkan ketepatan dan menangani kueri yang salah bentuk.
- **Mengeksplorasi Aplikasi Praktis:** Kenali skenario di mana Agentic RAG unggul, seperti lingkungan dengan prioritas ketepatan, interaksi basis data yang kompleks, dan alur kerja yang diperpanjang.

## Tujuan Pembelajaran

Setelah menyelesaikan pelajaran ini, Anda akan mengetahui/memahami:

- **Memahami Agentic RAG:** Pelajari tentang paradigma AI yang sedang berkembang di mana model bahasa besar (LLM) secara mandiri merencanakan langkah selanjutnya sambil menarik informasi dari sumber data eksternal.
- **Gaya Iteratif Maker-Checker:** Pahami konsep siklus panggilan iteratif ke LLM, diselingi pemanggilan alat atau fungsi dan output terstruktur, yang dirancang untuk meningkatkan ketepatan dan menangani kueri yang salah bentuk.
- **Menguasai Proses Penalaran:** Memahami kemampuan sistem untuk menguasai proses penalarannya sendiri, membuat keputusan tentang bagaimana mendekati masalah tanpa bergantung pada jalur yang sudah ditentukan sebelumnya.
- **Alur Kerja:** Memahami bagaimana model agentic secara mandiri memutuskan untuk mengambil laporan tren pasar, mengidentifikasi data pesaing, mengkorelasikan metrik penjualan internal, menyintesis temuan, dan mengevaluasi strategi.
- **Siklus Iteratif, Integrasi Alat, dan Memori:** Pelajari tentang ketergantungan sistem pada pola interaksi berulang, mempertahankan status dan memori antar langkah untuk menghindari pengulangan siklus dan membuat keputusan yang lebih tepat.
- **Menangani Mode Kegagalan dan Koreksi Diri:** Jelajahi mekanisme koreksi diri yang kuat dari sistem, termasuk iterasi dan pengulangan kueri, penggunaan alat diagnostik, dan pengawasan manusia sebagai cadangan.
- **Batasan Agen:** Pahami batasan Agentic RAG, berfokus pada otonomi spesifik domain, ketergantungan pada infrastruktur, dan penghormatan terhadap batasan keamanan.
- **Kasus Penggunaan dan Nilai Praktis:** Kenali skenario di mana Agentic RAG unggul, seperti lingkungan dengan prioritas ketepatan, interaksi basis data yang kompleks, dan alur kerja yang diperpanjang.
- **Tata Kelola, Transparansi, dan Kepercayaan:** Pelajari tentang pentingnya tata kelola dan transparansi, termasuk penalaran yang dapat dijelaskan, kontrol bias, dan pengawasan manusia.

## Apa itu Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) adalah paradigma AI yang sedang berkembang di mana model bahasa besar (LLM) secara mandiri merencanakan langkah berikutnya sambil menarik informasi dari sumber eksternal. Berbeda dengan pola pengambilan data statis lalu membaca, Agentic RAG melibatkan panggilan iteratif ke LLM, diselingi dengan pemanggilan alat atau fungsi serta output terstruktur. Sistem mengevaluasi hasil, menyempurnakan kueri, memanggil alat tambahan jika diperlukan, dan melanjutkan siklus ini sampai solusi yang memuaskan tercapai. Gaya “maker-checker” iteratif ini meningkatkan ketepatan, menangani kueri yang salah bentuk, dan memastikan hasil berkualitas tinggi.

Sistem secara aktif menguasai proses penalarannya, menulis ulang kueri yang gagal, memilih metode pengambilan berbeda, dan mengintegrasikan beberapa alat—seperti pencarian vektor di Azure AI Search, basis data SQL, atau API khusus—sebelum memfinalisasi jawabannya. Kualitas pembeda dari sistem agentic adalah kemampuannya untuk menguasai proses penalarannya sendiri. Implementasi RAG tradisional bergantung pada jalur yang sudah ditentukan, tetapi sistem agentic secara mandiri menentukan urutan langkah berdasarkan kualitas informasi yang ditemukan.

## Mendefinisikan Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) adalah paradigma yang sedang berkembang dalam pengembangan AI di mana LLM tidak hanya menarik informasi dari sumber data eksternal tetapi juga secara mandiri merencanakan langkah berikutnya. Berbeda dengan pola pengambilan data statis lalu membaca atau urutan prompt yang diskrip dengan hati-hati, Agentic RAG melibatkan siklus panggilan iteratif ke LLM, diselingi dengan pemanggilan alat atau fungsi dan output terstruktur. Pada setiap putaran, sistem mengevaluasi hasil yang diperoleh, memutuskan apakah akan menyempurnakan kueri, memanggil alat tambahan jika perlu, dan melanjutkan siklus ini sampai mendapatkan solusi memuaskan.

Gaya operasi “maker-checker” iteratif ini dirancang untuk meningkatkan ketepatan, menangani kueri yang salah bentuk ke basis data terstruktur (mis. NL2SQL), dan memastikan hasil yang seimbang serta berkualitas tinggi. Alih-alih hanya bergantung pada rantai prompt yang dirancang dengan cermat, sistem secara aktif menguasai proses penalarannya. Sistem dapat menulis ulang kueri yang gagal, memilih metode pengambilan berbeda, dan mengintegrasikan beberapa alat—seperti pencarian vektor di Azure AI Search, basis data SQL, atau API khusus—sebelum memfinalisasi jawabannya. Ini menghapus kebutuhan pada kerangka kerja orkestrasi yang terlalu kompleks. Sebaliknya, siklus sederhana “panggilan LLM → penggunaan alat → panggilan LLM → …” dapat menghasilkan keluaran yang canggih dan berdasar kuat.

![Agentic RAG Core Loop](../../../translated_images/id/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## Menguasai Proses Penalaran

Kualitas pembeda yang menjadikan suatu sistem “agentic” adalah kemampuannya menguasai proses penalarannya sendiri. Implementasi RAG tradisional seringkali bergantung pada manusia untuk menentukan jalur bagi model: sebuah rantai pemikiran yang menguraikan apa yang harus diambil dan kapan.
Namun saat sistem benar-benar agentic, ia secara internal memutuskan bagaimana mendekati masalah. Ini bukan hanya mengeksekusi skrip; ini secara mandiri menentukan urutan langkah berdasarkan kualitas informasi yang ditemukan.
Misalnya, jika diminta membuat strategi peluncuran produk, sistem tidak hanya bergantung pada prompt yang menguraikan seluruh alur riset dan pengambilan keputusan. Sebaliknya, model agentic secara mandiri memutuskan untuk:

1. Mengambil laporan tren pasar terkini menggunakan Bing Web Grounding
2. Mengidentifikasi data pesaing relevan menggunakan Azure AI Search.
3. Mengkorelasikan metrik penjualan internal historis menggunakan Azure SQL Database.
4. Mensintesis temuan menjadi strategi padu yang diorkestrasi melalui Azure OpenAI Service.
5. Mengevaluasi strategi untuk menemukan celah atau inkonsistensi, memicu pengambilan ulang data jika diperlukan.
Semua langkah ini—penyempurnaan kueri, pemilihan sumber, iterasi sampai “puas” dengan jawaban—diputuskan oleh model, bukan diskrip oleh manusia.

## Siklus Iteratif, Integrasi Alat, dan Memori

![Tool Integration Architecture](../../../translated_images/id/tool-integration.0f569710b5c17c10.webp)

Sistem agentic bergantung pada pola interaksi berulang:

- **Panggilan Awal:** Tujuan pengguna (alias prompt pengguna) disampaikan ke LLM.
- **Pemanggilan Alat:** Jika model mengidentifikasi informasi yang hilang atau instruksi ambigu, ia memilih alat atau metode pengambilan—seperti query basis data vektor (mis. Azure AI Search dengan pencarian hybrid atas data pribadi) atau panggilan SQL terstruktur—untuk mengumpulkan konteks lebih.
- **Penilaian & Penyempurnaan:** Setelah meninjau data yang dikembalikan, model memutuskan apakah informasi cukup. Jika tidak, model menyempurnakan kueri, mencoba alat berbeda, atau mengubah pendekatan.
- **Ulangi Sampai Puas:** Siklus ini berlanjut sampai model menentukan bahwa ia memiliki kejelasan dan bukti cukup untuk memberi jawaban akhir yang bernalar baik.
- **Memori & Status:** Karena sistem mempertahankan status dan memori antar langkah, ia dapat mengingat upaya sebelumnya dan hasilnya, menghindari siklus pengulangan, serta membuat keputusan yang lebih tepat saat melanjutkan.

Seiring waktu, ini menciptakan rasa pemahaman yang berkembang, memungkinkan model menavigasi tugas kompleks multi-langkah tanpa memerlukan campur tangan manusia terus-menerus atau merombak prompt.

## Menangani Mode Kegagalan dan Koreksi Diri

Otonomi Agentic RAG juga melibatkan mekanisme koreksi diri yang tangguh. Ketika sistem menemui jalan buntu—seperti mengambil dokumen yang tidak relevan atau menemui kueri yang salah bentuk—ia dapat:

- **Mengiterasi dan Melakukan Pengulangan Kueri:** Alih-alih mengembalikan respons bernilai rendah, model mencoba strategi pencarian baru, menulis ulang kueri basis data, atau melihat set data alternatif.
- **Menggunakan Alat Diagnostik:** Sistem dapat memanggil fungsi tambahan yang dirancang untuk membantunya memeriksa langkah penalarannya atau mengonfirmasi ketepatan data yang diambil. Alat seperti Azure AI Tracing akan penting untuk memungkinkan observabilitas dan monitoring yang tangguh.
- **Cadangan pada Pengawasan Manusia:** Untuk skenario kritis atau yang sering gagal berulang, model mungkin menandai ketidakpastian dan meminta panduan manusia. Setelah manusia memberikan umpan balik korektif, model dapat menggabungkan pelajaran tersebut ke depan.

Pendekatan iteratif dan dinamis ini memungkinkan model terus meningkat, menjamin bahwa ini bukan hanya sistem sekali pakai, tapi yang belajar dari kesalahan selama sesi berlangsung.

![Self Correction Mechanism](../../../translated_images/id/self-correction.da87f3783b7f174b.webp)

## Batasan Agen

Meskipun memiliki otonomi dalam suatu tugas, Agentic RAG tidak setara dengan Kecerdasan Buatan Umum (Artificial General Intelligence). Kapabilitas “agentic”-nya terbatas pada alat, sumber data, dan kebijakan yang disediakan oleh pengembang manusia. Sistem tidak bisa menciptakan alat sendiri atau keluar dari batas domain yang ditetapkan. Sebaliknya, sistem unggul dalam mengorkestrasi sumber daya secara dinamis.
Perbedaan utama dari bentuk AI yang lebih maju meliputi:

1. **Otonomi Spesifik Domain:** Sistem Agentic RAG fokus mencapai tujuan yang ditetapkan pengguna dalam domain yang dikenal, menggunakan strategi seperti penulisan ulang kueri atau pemilihan alat untuk meningkatkan hasil.
2. **Bergantung pada Infrastruktur:** Kapabilitas sistem tergantung pada alat dan data yang diintegrasikan oleh pengembang. Sistem tidak dapat melewati batas ini tanpa intervensi manusia.
3. **Menghormati Batasan Keamanan:** Pedoman etika, aturan kepatuhan, dan kebijakan bisnis tetap sangat penting. Kebebasan agen selalu dibatasi oleh langkah keamanan dan mekanisme pengawasan (semoga?).

## Kasus Penggunaan dan Nilai Praktis

Agentic RAG unggul dalam skenario yang membutuhkan penyempurnaan iteratif dan presisi:

1. **Lingkungan dengan Prioritas Ketepatan:** Dalam pemeriksaan kepatuhan, analisis regulasi, atau riset hukum, model agentic dapat berulang kali memverifikasi fakta, berkonsultasi ke berbagai sumber, dan menulis ulang kueri sampai menghasilkan jawaban yang sangat tervalidasi.
2. **Interaksi Basis Data Kompleks:** Saat menangani data terstruktur di mana kueri sering gagal atau perlu penyesuaian, sistem dapat secara mandiri menyempurnakan kueri menggunakan Azure SQL atau Microsoft Fabric OneLake, memastikan pengambilan akhir sesuai dengan maksud pengguna.
3. **Alur Kerja Perpanjangan:** Sesi yang berjalan lebih lama mungkin berkembang seiring munculnya informasi baru. Agentic RAG dapat terus menerus menggabungkan data baru, mengubah strategi saat mempelajari lebih banyak tentang ruang masalah.

## Tata Kelola, Transparansi, dan Kepercayaan

Saat sistem ini menjadi lebih otonom dalam penalarannya, tata kelola dan transparansi menjadi sangat penting:

- **Penalaran yang Dapat Dijelaskan:** Model dapat menyediakan jejak audit kueri yang dibuat, sumber yang dikonsultasi, dan langkah penalaran yang diambil untuk mencapai kesimpulan. Alat seperti Azure AI Content Safety dan Azure AI Tracing / GenAIOps dapat membantu menjaga transparansi dan mengurangi risiko.
- **Kontrol Bias dan Pengambilan yang Seimbang:** Pengembang dapat mengatur strategi pengambilan untuk memastikan sumber data yang seimbang dan representatif diperhitungkan, serta secara teratur mengaudit keluaran untuk mendeteksi bias atau pola yang miring menggunakan model kustom untuk organisasi data science maju dengan Azure Machine Learning.
- **Pengawasan Manusia dan Kepatuhan:** Untuk tugas sensitif, ulasan manusia tetap penting. Agentic RAG tidak menggantikan penilaian manusia dalam keputusan berisiko tinggi—tetapi memperkuat dengan memberikan opsi yang lebih tervalidasi secara menyeluruh.

Memiliki alat yang menyediakan catatan jelas tentang aksi sangat penting. Tanpa itu, debug proses multi-langkah bisa sangat sulit. Lihat contoh berikut dari Literal AI (perusahaan di balik Chainlit) untuk jalannya Agent:

![AgentRunExample](../../../translated_images/id/AgentRunExample.471a94bc40cbdc0c.webp)

## Kesimpulan

Agentic RAG mewakili evolusi alami dalam cara sistem AI menangani tugas kompleks yang intensif data. Dengan mengadopsi pola interaksi berulang, secara mandiri memilih alat, dan menyempurnakan kueri sampai mencapai hasil bermutu tinggi, sistem melampaui pengikutan prompt statis menjadi pengambil keputusan yang lebih adaptif dan sadar konteks. Meskipun masih dibatasi oleh infrastruktur dan pedoman etika yang ditentukan manusia, kapabilitas agentic ini memungkinkan interaksi AI yang lebih kaya, dinamis, dan pada akhirnya lebih berguna bagi perusahaan dan pengguna akhir.

### Punya Pertanyaan Lebih Lanjut tentang Agentic RAG?

Bergabunglah dengan [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) untuk bertemu dengan pembelajar lain, menghadiri jam kantor, dan mendapatkan jawaban atas pertanyaan Anda tentang AI Agents.

## Sumber Tambahan

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">Implementasi Retrieval Augmented Generation (RAG) dengan Azure OpenAI Service: Pelajari cara menggunakan data Anda sendiri dengan Azure OpenAI Service. Modul Microsoft Learn ini menyediakan panduan komprehensif tentang implementasi RAG</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Evaluasi aplikasi generative AI dengan Microsoft Foundry: Artikel ini membahas evaluasi dan perbandingan model pada dataset publik, termasuk aplikasi Agentic AI dan arsitektur RAG</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Apa itu Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Panduan Lengkap untuk Agent-Based Retrieval Augmented Generation – Berita dari generation RAG</a>

- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: tingkatkan RAG Anda dengan reformulasi kueri dan kueri mandiri! Buku Masak AI Open-Source Hugging Face</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Menambahkan Lapisan Agentic ke RAG</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Masa Depan Asisten Pengetahuan: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Cara Membangun Sistem Agentic RAG</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Menggunakan Layanan Agen Microsoft Foundry untuk meningkatkan skala agen AI Anda</a>

### Makalah Akademik

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Penyempurnaan Iteratif dengan Umpan Balik Diri</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Agen Bahasa dengan Pembelajaran Penguatan Verbal</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Model Bahasa Besar Dapat Memperbaiki Diri dengan Kritik Interaktif Alat</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation: Survei mengenai Agentic RAG</a>

## Pengujian Awal Agen Ini (Opsional)

Setelah Anda belajar menerapkan agen di [Pelajaran 16](../16-deploying-scalable-agents/README.md), Anda dapat melakukan pengujian awal `TravelRAGAgent` pelajaran ini — memeriksa bahwa jawabannya tetap berlandaskan pada basis pengetahuan — dengan [`tests/lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json). Lihat [`tests/README.md`](../tests/README.md) untuk cara menjalankannya.

## Pelajaran Sebelumnya

[Pola Desain Penggunaan Alat](../04-tool-use/README.md)

## Pelajaran Berikutnya

[Membangun Agen AI yang Dapat Dipercaya](../06-building-trustworthy-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->