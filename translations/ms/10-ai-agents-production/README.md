# Ejen AI dalam Pengeluaran: Kebolehlihatan & Penilaian

[![AI Agents in Production](../../../translated_images/ms/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Apabila ejen AI bergerak dari prototaip percubaan kepada aplikasi dunia sebenar, keupayaan untuk memahami tingkah laku mereka, memantau prestasi, dan menilai output mereka secara sistematik menjadi penting.

## Matlamat Pembelajaran

Selepas menamatkan pelajaran ini, anda akan mengetahui cara/memahami:
- Konsep teras kebolehlihatan dan penilaian ejen
- Teknik untuk meningkatkan prestasi, kos, dan keberkesanan ejen
- Apa dan bagaimana menilai ejen AI anda secara sistematik
- Cara mengawal kos semasa mengeluarkan ejen AI ke produksi
- Cara menginstrumen ejen yang dibina dengan Microsoft Agent Framework

Matlamatnya adalah untuk membekalkan anda dengan pengetahuan untuk mengubah ejen "kotak hitam" anda menjadi sistem yang telus, mudah diurus, dan boleh dipercayai.

_**Nota:** Penting untuk mengeluarkan Ejen AI yang selamat dan boleh dipercayai. Lihat juga pelajaran [Membina Ejen AI yang Boleh Dipercayai](./06-building-trustworthy-agents/README.md)._

## Jejak dan Rentang

Alat kebolehlihatan seperti [Langfuse](https://langfuse.com/) atau [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) biasanya mewakili larian ejen sebagai jejak dan rentang.

- **Jejak** mewakili tugas lengkap ejen dari mula hingga selesai (seperti mengendalikan pertanyaan pengguna).
- **Rentang** adalah langkah individu dalam jejak (seperti memanggil model bahasa atau mengambil data).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Tanpa kebolehlihatan, ejen AI boleh dirasakan seperti "kotak hitam" - keadaan dalaman dan penalaran dalaman tidak jelas, menjadikannya sukar untuk mendiagnosis masalah atau mengoptimumkan prestasi. Dengan kebolehlihatan, ejen menjadi "kotak kaca," menawarkan ketelusan yang penting untuk membina kepercayaan dan memastikan mereka beroperasi seperti yang dimaksudkan.

## Kenapa Kebolehlihatan Penting dalam Persekitaran Produksi

Peralihan ejen AI ke persekitaran produksi memperkenalkan set cabaran dan keperluan baru. Kebolehlihatan bukan lagi "bagus untuk ada" tetapi satu keupayaan kritikal:

*   **Penguraian Masalah dan Analisis Punca Utama**: Apabila ejen gagal atau menghasilkan output yang tidak dijangka, alat kebolehlihatan menyediakan jejak yang diperlukan untuk mengenal pasti punca kesilapan. Ini sangat penting dalam ejen kompleks yang mungkin melibatkan pelbagai panggilan LLM, interaksi alat, dan logik bersyarat.
*   **Pengurusan Latensi dan Kos**: Ejen AI sering bergantung pada LLM dan API luaran lain yang dikenakan bayaran per token atau panggilan. Kebolehlihatan membolehkan penjejakan tepat panggilan ini, membantu mengenal pasti operasi yang terlalu perlahan atau mahal. Ini membolehkan pasukan mengoptimumkan arahan, memilih model yang lebih cekap, atau mereka semula aliran kerja untuk mengurus kos operasi dan memastikan pengalaman pengguna yang baik.
*   **Kepercayaan, Keselamatan, dan Pematuhan**: Dalam banyak aplikasi, penting untuk memastikan ejen berkelakuan dengan selamat dan beretika. Kebolehlihatan menyediakan jejak audit tindakan dan keputusan ejen. Ini boleh digunakan untuk mengesan dan mengurangkan isu seperti suntikan arahan, penghasilan kandungan yang membahayakan, atau salah urus maklumat peribadi yang boleh dikenal pasti (PII). Sebagai contoh, anda boleh menyemak jejak untuk memahami mengapa ejen memberikan respons tertentu atau menggunakan alat tertentu.
*   **Kitaran Peningkatan Berterusan**: Data kebolehlihatan adalah asas proses pembangunan secara iteratif. Dengan memantau bagaimana ejen berprestasi dalam dunia sebenar, pasukan boleh mengenal pasti kawasan untuk peningkatan, mengumpul data untuk penyelarasan model, dan mengesahkan impak perubahan. Ini mewujudkan kitaran maklum balas di mana wawasan produksi dari penilaian dalam talian memberi maklumat kepada eksperimen luar talian dan pemurnian, yang membawa kepada prestasi ejen yang semakin baik.

## Metrik Utama yang Perlu Dipantau

Untuk memantau dan memahami tingkah laku ejen, pelbagai metrik dan isyarat harus dipantau. Walaupun metrik khusus mungkin berbeza berdasarkan tujuan ejen, terdapat beberapa metrik yang penting secara amnya.

Berikut adalah beberapa metrik yang paling biasa dipantau oleh alat kebolehlihatan:

**Latensi:** Seberapa cepat ejen memberi respons? Masa menunggu yang lama memberi kesan negatif pada pengalaman pengguna. Anda harus mengukur latensi untuk tugasan dan langkah individu dengan menjejak larian ejen. Contohnya, ejen yang mengambil masa 20 saat untuk semua panggilan model boleh dipercepatkan dengan menggunakan model yang lebih laju atau dengan menjalankan panggilan model secara serentak.

**Kos:** Berapa perbelanjaan bagi setiap larian ejen? Ejen AI bergantung pada panggilan LLM yang dikenakan bayaran per token atau API luaran. Penggunaan alat yang kerap atau pelbagai arahan boleh meningkatkan kos dengan pantas. Contohnya, jika ejen memanggil LLM lima kali untuk peningkatan kualiti yang kecil, anda mesti menilai sama ada kos itu berbaloi atau jika anda boleh mengurangkan bilangan panggilan atau menggunakan model yang lebih murah. Pemantauan masa nyata juga boleh membantu mengenal pasti lonjakan tidak dijangka (contohnya, pepijat yang menyebabkan gelung API berlebihan).

**Ralat Permintaan:** Berapa banyak permintaan yang gagal oleh ejen? Ini boleh termasuk ralat API atau panggilan alat yang gagal. Untuk menjadikan ejen anda lebih tahan terhadap ini dalam produksi, anda kemudiannya boleh menyediakan fallback atau percubaan semula. Contohnya jika penyedia LLM A gagal, anda bertukar ke penyedia LLM B sebagai sandaran.

**Maklum Balas Pengguna:** Melaksanakan penilaian pengguna secara langsung memberikan wawasan berharga. Ini boleh termasuk penilaian eksplisit (👍bagus/👎tidak, ⭐1-5 bintang) atau komen teks. Maklum balas negatif yang konsisten harus memberi amaran kepada anda kerana ini tanda bahawa ejen tidak berfungsi seperti dijangkakan.

**Maklum Balas Pengguna Tidak Eksplisit:** Tingkah laku pengguna memberikan maklum balas tidak langsung walaupun tanpa penilaian eksplisit. Ini boleh termasuk penstrukturan semula soalan segera, pertanyaan berulang atau menekan butang cuba semula. Contohnya, jika anda melihat pengguna berulang kali bertanya soalan yang sama, ini adalah tanda bahawa ejen tidak berfungsi seperti dijangkakan.

**Ketepatan:** Seberapa kerap ejen menghasilkan output yang betul atau diinginkan? Definisi ketepatan berbeza (contohnya, ketepatan penyelesaian masalah, ketepatan pengambilan maklumat, kepuasan pengguna). Langkah pertama adalah menentukan apa yang dikira kejayaan untuk ejen anda. Anda boleh mengesan ketepatan melalui pemeriksaan automatik, skor penilaian, atau label penyelesaian tugasan. Contohnya, menandakan jejak sebagai "berjaya" atau "gagal".

**Metrik Penilaian Automatik:** Anda juga boleh menyediakan penilaian automatik. Contohnya, anda boleh menggunakan LLM untuk menilai output ejen sama ada ia berguna, tepat, atau tidak. Terdapat juga beberapa pustaka sumber terbuka yang membantu anda menilai pelbagai aspek ejen. Contohnya [RAGAS](https://docs.ragas.io/) untuk ejen RAG atau [LLM Guard](https://llm-guard.com/) untuk mengesan bahasa berbahaya atau suntikan arahan.

Dalam praktiknya, gabungan metrik ini memberikan liputan terbaik untuk kesihatan ejen AI. Dalam [notebook contoh](./code_samples/10-expense_claim-demo.ipynb) bab ini, kami akan menunjukkan bagaimana metrik ini kelihatan dalam contoh sebenar tetapi pertama, kita akan belajar bagaimana aliran kerja penilaian tipikal kelihatan.

## Instrumen Ejen Anda

Untuk mengumpul data penjejakan, anda perlu menginstrumen kod anda. Matlamatnya adalah untuk menginstrumen kod ejen bagi mengeluarkan jejak dan metrik yang boleh ditangkap, diproses, dan divisualisasikan oleh platform kebolehlihatan.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) telah muncul sebagai piawaian industri bagi kebolehlihatan LLM. Ia menyediakan set API, SDK, dan alat untuk menjana, mengumpul, dan mengeksport data telemetri.

Terdapat banyak pustaka instrumentasi yang membalut rangka kerja ejen sedia ada dan memudahkan eksport rentang OpenTelemetry ke alat kebolehlihatan. Microsoft Agent Framework berintegrasi secara asli dengan OpenTelemetry. Berikut adalah contoh menginstrumen ejen MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Pelaksanaan ejen dijejak secara automatik
    pass
```

[notebook contoh](./code_samples/10-expense_claim-demo.ipynb) dalam bab ini akan menunjukkan cara menginstrumen ejen MAF anda.

**Penciptaan Rentang Manual:** Walaupun pustaka instrumentasi menyediakan garis dasar yang baik, sering terdapat keadaan di mana maklumat yang lebih terperinci atau tersuai diperlukan. Anda boleh mencipta rentang secara manual untuk menambah logik aplikasi tersuai. Lebih penting, mereka boleh memperkayakan rentang yang dicipta secara automatik atau manual dengan atribut tersuai (juga dikenali sebagai tag atau metadata). Atribut ini boleh termasuk data khusus perniagaan, pengiraan perantaraan, atau sebarang konteks yang mungkin berguna untuk penguraian masalah atau analisis, seperti `user_id`, `session_id`, atau `model_version`.

Contoh mencipta jejak dan rentang secara manual dengan [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Penilaian Ejen

Kebolehlihatan memberikan kita metrik, tetapi penilaian adalah proses menganalisis data itu (dan melaksanakan ujian) untuk menentukan sejauh mana ejen AI berprestasi dan bagaimana ia boleh diperbaiki. Dengan kata lain, setelah anda mempunyai jejak dan metrik itu, bagaimana anda menggunakannya untuk menilai ejen dan membuat keputusan?

Penilaian berkala penting kerana ejen AI sering tidak deterministik dan boleh berkembang (melalui kemas kini atau perubahan tingkah laku model) – tanpa penilaian, anda tidak akan tahu jika "ejen pintar" anda sebenarnya menjalankan tugas dengan baik atau jika ia telah merosot.

Terdapat dua kategori penilaian untuk ejen AI: **penilaian dalam talian** dan **penilaian luar talian**. Kedua-duanya bernilai, dan saling melengkapi. Biasanya kami bermula dengan penilaian luar talian, kerana ini adalah langkah minima yang perlu sebelum menyebarkan sebarang ejen.

### Penilaian Luar Talian

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Ini melibatkan menilai ejen dalam persekitaran terkawal, biasanya menggunakan set data ujian, bukan pertanyaan pengguna secara langsung. Anda menggunakan set data yang dipilih dengan teliti di mana anda tahu apa output yang dijangkakan atau tingkah laku betul, dan kemudian menjalankan ejen anda ke atas set data itu.

Sebagai contoh, jika anda membina ejen menyelesaikan masalah ayat matematik, anda mungkin mempunyai [set data ujian](https://huggingface.co/datasets/gsm8k) sebanyak 100 masalah dengan jawapan diketahui. Penilaian luar talian sering dilakukan semasa pembangunan (dan boleh menjadi sebahagian daripada paip CI/CD) untuk memeriksa peningkatan atau mengelakkan kemerosotan. Kelebihannya ialah ia **boleh diulang dan anda boleh mendapatkan metrik ketepatan yang jelas kerana anda mempunyai kebenaran asas**. Anda juga boleh mensimulasikan pertanyaan pengguna dan mengukur respons ejen terhadap jawapan ideal atau menggunakan metrik automatik seperti yang diterangkan di atas.

Cabaran utama dengan penilaian luar talian adalah memastikan set data ujian anda menyeluruh dan kekal relevan – ejen mungkin berprestasi baik pada set ujian tetap tetapi menghadapi pertanyaan yang sangat berbeza di produksi. Oleh itu, anda perlu mengemas kini set ujian dengan kes tepi dan contoh baharu yang mencerminkan senario dunia sebenar​. Campuran kes "uji asap" kecil dan set penilaian yang lebih besar berguna: set kecil untuk pemeriksaan pantas dan set lebih besar untuk metrik prestasi yang lebih luas​.

### Penilaian Dalam Talian

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Ini merujuk kepada menilai ejen dalam persekitaran sebenar secara langsung, iaitu semasa penggunaan sebenar dalam produksi. Penilaian dalam talian melibatkan pemantauan prestasi ejen pada interaksi pengguna sebenar dan menganalisis hasil secara berterusan.

Sebagai contoh, anda mungkin menjejaki kadar kejayaan, skor kepuasan pengguna, atau metrik lain pada trafik langsung. Kelebihan penilaian dalam talian ialah ia **menangkap perkara yang mungkin anda tidak jangka dalam makmal** – anda boleh memerhati pergeseran model dari masa ke masa (jika keberkesanan ejen merosot semasa corak input berubah) dan menangkap pertanyaan atau situasi tidak dijangka yang tidak ada dalam data ujian anda​. Ia memberikan gambaran sebenar bagaimana ejen berkelakuan di dunia nyata.

Penilaian dalam talian selalunya melibatkan pengumpulan maklum balas pengguna secara implisit dan eksplisit, seperti yang dibincangkan, dan mungkin menjalankan ujian bayang-bayang atau ujian A/B (di mana versi baru ejen berjalan secara seiring untuk dibandingkan dengan yang lama). Cabarannya ialah sukar untuk mendapatkan label atau skor yang boleh dipercayai untuk interaksi langsung – anda mungkin bergantung pada maklum balas pengguna atau metrik hiliran (contohnya, adakah pengguna klik hasil).

### Menggabungkan kedua-duanya

Penilaian dalam talian dan luar talian bukan saling eksklusif; mereka sangat melengkapi. Wawasan dari pemantauan dalam talian (contohnya, jenis pertanyaan pengguna baru di mana ejen berprestasi buruk) boleh digunakan untuk menambah dan memperbaiki set data ujian luar talian. Sebaliknya, ejen yang berprestasi baik dalam ujian luar talian boleh lebih yakin untuk dikeluarkan dan dipantau dalam talian.

Malahan, banyak pasukan mengamalkan kitaran:

_menilai di luar talian -> keluarkan -> pantau dalam talian -> kumpul kes kegagalan baru -> tambah ke set data luar talian -> perbaiki ejen -> ulang_.

## Isu Biasa

Apabila anda mengeluarkan ejen AI ke produksi, anda mungkin menghadapi pelbagai cabaran. Berikut adalah beberapa isu biasa dan penyelesaian yang mungkin:

| **Isu**    | **Penyelesaian Potensi**   |
| ------------- | ------------------ |
| Ejen AI tidak menjalankan tugas secara konsisten | - Perhalusi arahan yang diberikan kepada Ejen AI; jelas tentang objektif.<br>- Kenal pasti di mana membahagikan tugasan kepada sub-tugasan dan mengendalikan mereka oleh pelbagai ejen boleh membantu. |
| Ejen AI terperangkap dalam gelung berterusan  | - Pastikan anda mempunyai terma dan syarat pemberhentian yang jelas supaya Ejen tahu bila untuk menghentikan proses.<br>- Untuk tugasan kompleks yang memerlukan penalaran dan perancangan, gunakan model yang lebih besar dan khusus untuk tugasan penalaran. |
| Panggilan alat Ejen AI tidak berprestasi baik   | - Uji dan sahkan output alat di luar sistem ejen.<br>- Perhalusi parameter yang ditakrif, arahan, dan penamaan alat.  |
| Sistem Multi-Ejen tidak berfungsi secara konsisten | - Perhalusi arahan yang diberikan kepada setiap ejen supaya spesifik dan berbeza antara satu sama lain.<br>- Bina sistem hierarki menggunakan ejen "penghala" atau pengawal untuk menentukan ejen yang betul. |

Banyak isu ini boleh dikenalpasti dengan lebih berkesan jika kebolehlihatan disediakan. Jejak dan metrik yang kita bincangkan sebelum ini membantu menunjukkan dengan tepat di mana dalam aliran kerja ejen masalah berlaku, menjadikan penguraian masalah dan pengoptimuman lebih cekap.

## Mengurus Kos
Berikut adalah beberapa strategi untuk mengurus kos penyebaran ejen AI ke dalam pengeluaran:

**Menggunakan Model Lebih Kecil:** Model Bahasa Kecil (SLM) boleh berprestasi baik pada kes penggunaan ejen tertentu dan akan mengurangkan kos dengan ketara. Seperti yang dinyatakan sebelum ini, membina sistem penilaian untuk menentukan dan membandingkan prestasi berbanding model lebih besar adalah cara terbaik untuk memahami bagaimana prestasi SLM pada kes penggunaan anda. Pertimbangkan menggunakan SLM untuk tugas yang lebih mudah seperti pengelasan niat atau pengekstrakan parameter, manakala model yang lebih besar disimpan untuk penalaran yang kompleks.

**Menggunakan Model Router:** Strategi yang serupa adalah menggunakan kepelbagaian model dan saiz. Anda boleh menggunakan LLM/SLM atau fungsi tanpa pelayan untuk menghala permintaan berdasarkan kerumitan ke model yang paling sesuai. Ini juga akan membantu mengurangkan kos sambil memastikan prestasi pada tugas yang betul. Sebagai contoh, hala pertanyaan ringkas kepada model yang lebih kecil dan lebih pantas, dan hanya gunakan model besar yang mahal untuk tugas penalaran kompleks.

**Mengcache Respons:** Mengenal pasti permintaan dan tugas biasa dan menyediakan respons sebelum ia melalui sistem ejen anda adalah cara yang baik untuk mengurangkan jumlah permintaan yang serupa. Anda juga boleh melaksanakan satu aliran untuk mengenal pasti sejauh mana permintaan itu serupa dengan permintaan yang dicache menggunakan model AI yang lebih asas. Strategi ini boleh mengurangkan kos dengan ketara untuk soalan yang sering ditanya atau aliran kerja yang biasa.

## Mari kita lihat bagaimana ini berfungsi dalam praktik

Dalam [notebook contoh bahagian ini](./code_samples/10-expense_claim-demo.ipynb), kita akan lihat contoh bagaimana kita boleh menggunakan alat pengamatan untuk memantau dan menilai ejen kita.


### Ada Soalan Lagi tentang Ejen AI dalam Pengeluaran?

Sertai [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) untuk bertemu dengan pelajar lain, menghadiri waktu pejabat dan dapatkan jawapan untuk soalan Ejen AI anda.

## Pelajaran Sebelumnya

[Corak Reka Bentuk Metakognisi](../09-metacognition/README.md)

## Pelajaran Seterusnya

[Protokol Agentic](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat kritikal, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab ke atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->