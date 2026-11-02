[![Agentic RAG](../../../translated_images/ms/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Klik gambar di atas untuk menonton video pelajaran ini)_

# Agentic RAG

Pelajaran ini memberikan gambaran menyeluruh tentang Agentic Retrieval-Augmented Generation (Agentic RAG), sebuah paradigma AI yang sedang berkembang di mana model bahasa besar (LLM) secara autonomi merancang langkah seterusnya sambil menarik maklumat dari sumber luar. Tidak seperti pola pemulihan-statik kemudian-baca, Agentic RAG melibatkan panggilan berulang ke LLM, berselang-seli dengan panggilan alat atau fungsi dan keluaran berstruktur. Sistem menilai hasil, memperhalusi pertanyaan, memanggil alat tambahan jika perlu, dan meneruskan kitaran ini sehingga penyelesaian yang memuaskan dicapai.

## Pengenalan

Pelajaran ini akan merangkumi

- **Memahami Agentic RAG:** Pelajari tentang paradigma AI yang sedang berkembang di mana model bahasa besar (LLM) secara autonomi merancang langkah-langkah seterusnya sambil menarik maklumat dari sumber data luar.
- **Memahami Gaya Pembuat-Pemeriksa Berulang:** Fahami kitaran panggilan berulang ke LLM, berselang-seli dengan panggilan alat atau fungsi dan keluaran berstruktur, direka untuk meningkatkan ketepatan dan mengendalikan pertanyaan yang tidak sempurna.
- **Meneroka Aplikasi Praktikal:** Kenal pasti senario di mana Agentic RAG menonjol, seperti persekitaran yang mengutamakan ketepatan, interaksi pangkalan data yang kompleks, dan aliran kerja yang dipanjangkan.

## Matlamat Pembelajaran

Selepas menamatkan pelajaran ini, anda akan mengetahui cara/memahami:

- **Memahami Agentic RAG:** Pelajari tentang paradigma AI yang sedang berkembang di mana model bahasa besar (LLM) secara autonomi merancang langkah seterusnya sambil menarik maklumat dari sumber data luar.
- **Gaya Pembuat-Pemeriksa Berulang:** Fahami konsep kitaran panggilan berulang ke LLM, berselang-seli dengan panggilan alat atau fungsi dan keluaran berstruktur, direka untuk meningkatkan ketepatan dan mengendalikan pertanyaan yang tidak sempurna.
- **Menguasai Proses Penalaran:** Fahami keupayaan sistem untuk memiliki proses penalarannya, membuat keputusan tentang cara mendekati masalah tanpa bergantung pada laluan yang telah ditakrifkan.
- **Aliran Kerja:** Fahami bagaimana model agentic secara bebas memutuskan untuk mendapatkan laporan trend pasaran, mengenal pasti data pesaing, mengaitkan metrik jualan dalaman, mensintesis penemuan, dan menilai strategi.
- **Kitaran Berulang, Integrasi Alat, dan Memori:** Ketahui tentang kebergantungan sistem pada corak interaksi berulang, mengekalkan keadaan dan memori sepanjang langkah untuk mengelakkan kitaran berulang dan membuat keputusan yang berinformasi.
- **Mengendalikan Mod Kegagalan dan Pembetulan Diri:** Terokai mekanisme pembetulan diri sistem yang mantap, termasuk mengulang dan bertanya semula, menggunakan alat diagnostik, dan beralih kepada pengawasan manusia.
- **Had Keagenan:** Fahami had Agentic RAG, tertumpu pada autonomi khusus domain, kebergantungan infrastruktur, dan penghormatan kepada garis panduan.
- **Kes Penggunaan Praktikal dan Nilai:** Kenal pasti senario di mana Agentic RAG menonjol, seperti persekitaran yang mengutamakan ketepatan, interaksi pangkalan data yang kompleks, dan aliran kerja yang dipanjangkan.
- **Tadbir Urus, Ketelusan, dan Kepercayaan:** Ketahui kepentingan tadbir urus dan ketelusan, termasuk penalaran yang boleh dijelaskan, kawalan bias, dan pengawasan manusia.

## Apa itu Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) adalah paradigma AI yang sedang berkembang di mana model bahasa besar (LLM) secara autonomi merancang langkah seterusnya sambil menarik maklumat dari sumber luar. Tidak seperti pola pemulihan-statik kemudian-baca, Agentic RAG melibatkan panggilan berulang ke LLM, berselang-seli dengan panggilan alat atau fungsi dan keluaran berstruktur. Sistem menilai hasil, memperhalusi pertanyaan, memanggil alat tambahan jika perlu, dan meneruskan kitaran ini sehingga penyelesaian yang memuaskan dicapai. Gaya “pembuat-pemeriksa” berulang ini meningkatkan ketepatan, mengendalikan pertanyaan tidak sempurna, dan memastikan hasil berkualiti tinggi.

Sistem ini secara aktif memiliki proses penalarannya, menulis semula pertanyaan yang gagal, memilih kaedah pemulihan berbeza, dan mengintegrasi pelbagai alat—seperti pencarian vektor dalam Azure AI Search, pangkalan data SQL, atau API tersuai—sebelum memuktamadkan jawapannya. Kualiti yang membezakan sistem agentic ialah keupayaannya memiliki proses penalarannya sendiri. Pelaksanaan RAG tradisional bergantung pada laluan yang telah ditakrifkan, tetapi sistem agentic secara autonomi menentukan urutan langkah berdasarkan kualiti maklumat yang ditemuinya.

## Mendefinisikan Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) adalah paradigma baru dalam pembangunan AI di mana LLM bukan sahaja menarik maklumat dari sumber data luar tetapi juga secara autonomi merancang langkah seterusnya. Berbeza dengan pola pemulihan-statik kemudian-baca atau urutan arahan prompt yang disusun rapi, Agentic RAG melibatkan kitaran panggilan berulang ke LLM, berselang-seli dengan panggilan alat atau fungsi dan keluaran berstruktur. Pada setiap giliran, sistem menilai hasil yang diperolehi, memutuskan sama ada untuk memperhalusi pertanyaan, memanggil alat tambahan jika perlu, dan meneruskan kitaran ini sehingga mencapai solusi yang memuaskan.

Gaya operasi “pembuat-pemeriksa” berulang ini direka untuk meningkatkan ketepatan, mengendalikan pertanyaan yang tidak sempurna kepada pangkalan data berstruktur (contohnya NL2SQL), dan memastikan hasil yang seimbang dan berkualiti tinggi. Daripada hanya bergantung pada rantaian arahan prompt yang direka dengan rapi, sistem secara aktif memiliki proses penalarannya. Ia boleh menulis semula pertanyaan yang gagal, memilih kaedah pemulihan yang berbeza, dan mengintegrasi pelbagai alat—seperti pencarian vektor dalam Azure AI Search, pangkalan data SQL, atau API tersuai—sebelum memuktamadkan jawapannya. Ini menghapuskan keperluan untuk rangka kerja orkestrasi yang terlalu kompleks. Sebaliknya, kitaran yang agak mudah “panggilan LLM → penggunaan alat → panggilan LLM → …” dapat menghasilkan keluaran yang canggih dan berasas kukuh.

![Agentic RAG Core Loop](../../../translated_images/ms/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## Memiliki Proses Penalaran

Kualiti yang membezakan yang menjadikan sesuatu sistem “agentic” adalah keupayaannya memiliki proses penalarannya sendiri. Pelaksanaan RAG tradisional sering bergantung pada manusia yang mendefinisikan laluan untuk model: rantai pemikiran yang merangkum apa yang perlu dipulihkan dan bila.
Tetapi apabila sistem benar-benar agentic, ia membuat keputusan dalaman tentang bagaimana untuk mendekati masalah itu. Ia bukan sekadar melaksanakan skrip; ia secara autonomi menentukan urutan langkah berdasarkan kualiti maklumat yang ditemuinya.
Sebagai contoh, jika ia diminta untuk mencipta strategi pelancaran produk, ia tidak hanya bergantung pada prompt yang menerangkan keseluruhan aliran kerja penyelidikan dan pembuatan keputusan. Sebaliknya, model agentic secara bebas memutuskan untuk:

1. Mendapatkan laporan trend pasaran semasa menggunakan Bing Web Grounding
2. Mengenal pasti data pesaing yang relevan menggunakan Azure AI Search.
3. Mengaitkan metrik jualan dalaman bersejarah menggunakan Azure SQL Database.
4. Mensintesis penemuan ke dalam strategi yang kohesif yang diorkestrakan melalui Azure OpenAI Service.
5. Menilai strategi untuk jurang atau ketidakselarasan, memicu pusingan pemulihan lagi jika perlu.
Semua langkah ini—memperhalusi pertanyaan, memilih sumber, mengulang sehingga “berpuas hati” dengan jawapan—diputuskan oleh model, bukan diwarisi skrip oleh manusia.

## Kitaran Berulang, Integrasi Alat, dan Memori

![Tool Integration Architecture](../../../translated_images/ms/tool-integration.0f569710b5c17c10.webp)

Sistem agentic bergantung pada corak interaksi berulang:

- **Panggilan Awal:** Matlamat pengguna (iaitu prompt pengguna) disampaikan kepada LLM.
- **Panggilan Alat:** Jika model mengenal pasti maklumat yang hilang atau arahan yang samar, ia memilih alat atau kaedah pemulihan—seperti pertanyaan pangkalan data vektor (contohnya Azure AI Search Hybrid search ke atas data peribadi) atau panggilan SQL berstruktur—untuk mengumpul lebih banyak konteks.
- **Penilaian & Pemurnian:** Selepas menilai data yang dikembalikan, model memutuskan sama ada maklumat itu mencukupi. Jika tidak, ia memperhalusi pertanyaan, mencuba alat berbeza, atau menyesuaikan pendekatannya.
- **Ulang sehingga Puas:** Kitaran ini diteruskan sehingga model menentukan ia mempunyai kejelasan dan bukti mencukupi untuk memberikan jawapan akhir yang berasas baik.
- **Memori & Keadaan:** Oleh kerana sistem mengekalkan keadaan dan memori sepanjang langkah, ia boleh mengingati percubaan sebelum ini dan hasilnya, mengelakkan kitaran berulang dan membuat keputusan yang lebih bermaklumat semasa meneruskan.

Lama kelamaan, ini mencipta rasa kefahaman yang berkembang, membolehkan model mengemudi tugas rumit bertahap-tahap tanpa memerlukan campur tangan manusia yang berterusan atau merombak prompt.

## Mengendalikan Mod Kegagalan dan Pembetulan Diri

Autonomi Agentic RAG juga melibatkan mekanisme pembetulan diri yang mantap. Apabila sistem menghadapi jalan buntu—seperti mendapatkan dokumen yang tidak relevan atau menghadapi pertanyaan yang tidak sempurna—ia boleh:

- **Mengulang dan Bertanya Semula:** Daripada mengembalikan jawapan bernilai rendah, model cuba strategi carian baru, menulis semula pertanyaan pangkalan data, atau melihat set data alternatif.
- **Menggunakan Alat Diagnostik:** Sistem mungkin memanggil fungsi tambahan yang direka untuk membantunya memeriksa langkah penalarannya atau mengesahkan ketepatan data yang diperoleh. Alat seperti Azure AI Tracing penting untuk membolehkan pemerhatian dan pemantauan yang mantap.
- **Beralih kepada Pengawasan Manusia:** Untuk senario berisiko tinggi atau yang berulang kali gagal, model mungkin menandakan ketidakpastian dan meminta panduan manusia. Setelah manusia memberikan maklum balas pembetulan, model boleh menggabungkan pengajaran itu untuk masa hadapan.

Pendekatan berulang dan dinamik ini membolehkan model sentiasa memperbaiki diri, memastikan ia bukan sahaja sistem satu tembakan tetapi satu yang belajar daripada kesilapan semasa sesi tertentu.

![Self Correction Mechanism](../../../translated_images/ms/self-correction.da87f3783b7f174b.webp)

## Had Keagenan

Walaupun mempunyai autonomi dalam sesebuah tugas, Agentic RAG tidak setara dengan Kecerdasan Umum Buatan. Keupayaan “agentic”nya terbatas kepada alat, sumber data, dan polisi yang disediakan oleh pembangun manusia. Ia tidak boleh mencipta alatnya sendiri atau melangkaui sempadan domain yang telah ditetapkan. Sebaliknya, ia cemerlang dalam mengorkestrasi sumber-sumber yang ada secara dinamik.
Perbezaan utama daripada bentuk AI yang lebih maju termasuk:

1. **Autonomi Khusus Domain:** Sistem Agentic RAG fokus mencapai matlamat yang ditakrifkan pengguna dalam domain yang diketahui, menggunakan strategi seperti penulisan semula pertanyaan atau pemilihan alat untuk memperbaiki hasil.
2. **Bergantung pada Infrastruktur:** Keupayaan sistem bergantung pada alat dan data yang diintegrasikan oleh pembangun. Ia tidak boleh melepasi batasan ini tanpa campur tangan manusia.
3. **Menghormati Garis Panduan:** Garis panduan etika, peraturan pematuhan, dan polisi perniagaan kekal sangat penting. Kebebasan agen sentiasa terhad oleh langkah keselamatan dan mekanisme pengawasan (harapnya?)

## Kes Penggunaan Praktikal dan Nilai

Agentic RAG menonjol dalam senario yang memerlukan pemurnian berulang dan ketepatan:

1. **Persekitaran Utamakan Ketepatan:** Dalam pemeriksaan pematuhan, analisis regulatori, atau penyelidikan undang-undang, model agentic boleh berulang kali mengesahkan fakta, merujuk kepada pelbagai sumber, dan menulis semula pertanyaan sehingga menghasilkan jawapan yang disemak dengan teliti.
2. **Interaksi Pangkalan Data Kompleks:** Apabila berurusan dengan data berstruktur di mana pertanyaan mungkin sering gagal atau perlu penyesuaian, sistem boleh memperhalusi pertanyaannya secara autonomi menggunakan Azure SQL atau Microsoft Fabric OneLake, memastikan pemulihan akhir selaras dengan niat pengguna.
3. **Aliran Kerja Berpanjangan:** Sesi yang berjalan lebih lama mungkin berkembang apabila maklumat baru muncul. Agentic RAG boleh sentiasa menggabungkan data baru, mengubah strategi apabila ia mempelajari lebih lanjut tentang ruang masalah.

## Tadbir Urus, Ketelusan, dan Kepercayaan

Apabila sistem ini menjadi lebih autonomi dalam penalaran mereka, tadbir urus dan ketelusan adalah penting:

- **Penalaran yang Boleh Dijelaskan:** Model boleh menyediakan jejak audit pertanyaan yang dibuat, sumber yang dirujuk, dan langkah penalaran yang diambil untuk mencapai kesimpulan. Alat seperti Azure AI Content Safety dan Azure AI Tracing / GenAIOps membantu mengekalkan ketelusan dan mengurangkan risiko.
- **Kawalan Bias dan Pemulihan Seimbang:** Pembangun boleh melaras strategi pemulihan untuk memastikan sumber data yang seimbang dan mewakili dipertimbangkan, serta mengaudit keluaran secara berkala untuk mengesan bias atau pola condong menggunakan model tersuai bagi organisasi sains data maju menggunakan Azure Machine Learning.
- **Pengawasan Manusia dan Pematuhan:** Untuk tugasan sensitif, semakan manusia kekal penting. Agentic RAG tidak menggantikan penilaian manusia dalam keputusan berisiko tinggi—ia menyokongnya dengan menyediakan pilihan yang diperiksa dengan lebih teliti.

Mempunyai alat yang menyediakan rekod tindakan yang jelas adalah penting. Tanpanya, menyahpepijat proses berbilang langkah boleh menjadi sangat sukar. Lihat contoh berikut dari Literal AI (syarikat di belakang Chainlit) untuk satu Agent run:

![AgentRunExample](../../../translated_images/ms/AgentRunExample.471a94bc40cbdc0c.webp)

## Kesimpulan

Agentic RAG mewakili evolusi semula jadi dalam cara sistem AI mengendalikan tugas yang kompleks dan berasaskan data. Dengan menggunakan corak interaksi berulang, memilih alat secara autonomi, dan memperhalusi pertanyaan sehingga mencapai hasil berkualiti tinggi, sistem bergerak melangkaui pengikut prompt statik ke arah pembuat keputusan yang lebih adaptif dan sedar konteks. Walaupun masih terhad oleh infrastruktur yang ditakrifkan manusia dan garis panduan etika, kemampuan agentic ini membolehkan interaksi AI yang lebih kaya, dinamik, dan akhirnya lebih berguna untuk perusahaan dan pengguna akhir.

### Ada Lagi Soalan tentang Agentic RAG?

Sertai [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) untuk bertemu dengan pelajar lain, menghadiri waktu pejabat dan mendapatkan jawapan untuk soalan Agen AI anda.

## Sumber Tambahan

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">Melaksanakan Retrieval Augmented Generation (RAG) dengan Azure OpenAI Service: Pelajari cara menggunakan data anda sendiri dengan Azure OpenAI Service. Modul Microsoft Learn ini menyediakan panduan menyeluruh tentang pelaksanaan RAG</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Penilaian aplikasi AI generatif dengan Microsoft Foundry: Artikel ini merangkumi penilaian dan perbandingan model pada set data yang tersedia umum, termasuk aplikasi AI Agentic dan seni bina RAG</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Apa itu Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Panduan Lengkap untuk Agen Berdasarkan Retrieval Augmented Generation – Berita dari generasi RAG</a>

- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: percepat RAG anda dengan penstrukturan semula pertanyaan dan pertanyaan sendiri! Buku Resipi AI Terbuka Sumber Hugging Face</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Menambah Lapisan Agentik kepada RAG</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Masa Depan Pembantu Pengetahuan: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Cara Membina Sistem Agentik RAG</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Menggunakan Perkhidmatan Ejen Microsoft Foundry untuk skala agen AI anda</a>

### Kertas Akademik

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Penambahbaikan Iteratif dengan Maklum Balas Sendiri</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Agen Bahasa dengan Pembelajaran Penguatan Verbal</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Model Bahasa Besar Boleh Membetulkan Diri dengan Kritikan Interaktif Alat</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation: Tinjauan mengenai Agentic RAG</a>

## Ujian Asas Agen Ini (Pilihan)

Selepas anda belajar untuk melancarkan agen dalam [Lesson 16](../16-deploying-scalable-agents/README.md), anda boleh menguji asas `TravelRAGAgent` pelajaran ini — memeriksa bahawa jawapannya kekal berasaskan kepada pangkalan pengetahuan — dengan [`tests/lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json). Lihat [`tests/README.md`](../tests/README.md) untuk cara menjalankannya.

## Pelajaran Sebelumnya

[Corak Reka Bentuk Penggunaan Alat](../04-tool-use/README.md)

## Pelajaran Seterusnya

[Membina Agen AI yang Boleh Dipercayai](../06-building-trustworthy-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->