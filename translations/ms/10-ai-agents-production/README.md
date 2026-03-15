# Ejen AI dalam Pengeluaran: Kebolehamatan & Penilaian

[![Ejen AI dalam Pengeluaran](../../../translated_images/ms/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Apabila ejen AI beralih dari prototaip eksperimen ke aplikasi dunia sebenar, keupayaan untuk memahami tingkah laku mereka, memantau prestasi mereka, dan menilai keluaran mereka secara sistematik menjadi penting.

## Matlamat Pembelajaran

Selepas menyelesaikan pelajaran ini, anda akan mengetahui cara/faham:
- Konsep teras kebolehamatan dan penilaian ejen
- Teknik untuk meningkatkan prestasi, kos, dan keberkesanan ejen
- Apa dan bagaimana untuk menilai ejen AI anda secara sistematik
- Bagaimana untuk mengawal kos ketika menggunakan ejen AI dalam pengeluaran
- Cara menginstrumentasi ejen yang dibina dengan Microsoft Agent Framework

Matlamatnya adalah untuk melengkapkan anda dengan pengetahuan untuk mengubah "kotak hitam" ejen anda menjadi sistem yang telus, boleh diurus, dan boleh dipercayai.

_**Nota:** Penting untuk menggunakan Ejen AI yang selamat dan boleh dipercayai. Lihat juga pelajaran [Membina Ejen AI yang Boleh Dipercayai](./06-building-trustworthy-agents/README.md)._

## Jejak dan Rentang

Alat kebolehamatan seperti [Langfuse](https://langfuse.com/) atau [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) biasanya mewakili larian ejen sebagai jejak dan rentang.

- **Jejak** mewakili tugasan lengkap ejen dari mula hingga selesai (seperti mengendalikan pertanyaan pengguna).
- **Rentang** adalah langkah individu dalam jejak (seperti memanggil model bahasa atau mendapatkan data).

![Pokok jejak dalam Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Tanpa kebolehamatan, ejen AI boleh terasa seperti "kotak hitam" - keadaan dalaman dan alasanannya tidak jelas, menjadikannya sukar untuk mendiagnosis masalah atau mengoptimumkan prestasi. Dengan kebolehamatan, ejen menjadi "kotak kaca," menawarkan ketelusan yang penting untuk membina kepercayaan dan memastikan mereka beroperasi seperti yang diingini.

## Mengapa Kebolehamatan Penting dalam Persekitaran Pengeluaran

Peralihan ejen AI ke persekitaran pengeluaran membawa cabaran dan keperluan baru. Kebolehamatan bukan lagi "baik untuk dimiliki" tetapi satu keupayaan penting:

*   **Penyahpepijatan dan Analisis Punca Akar:** Apabila ejen gagal atau menghasilkan output yang tidak dijangka, alat kebolehamatan menyediakan jejak yang diperlukan untuk mengenal pasti sumber ralat. Ini sangat penting dalam ejen yang kompleks yang mungkin melibatkan pelbagai panggilan LLM, interaksi alat, dan logik bersyarat.
*   **Pengurusan Latensi dan Kos:** Ejen AI sering bergantung kepada LLM dan API luaran lain yang dicaj per token atau per panggilan. Kebolehamatan membolehkan penjejakan tepat panggilan ini, membantu mengenal pasti operasi yang terlalu perlahan atau mahal. Ini membolehkan pasukan mengoptimumkan prompt, memilih model yang lebih cekap, atau mereka semula aliran kerja untuk mengurus kos operasi dan memastikan pengalaman pengguna yang baik.
*   **Kepercayaan, Keselamatan, dan Pematuhan:** Dalam banyak aplikasi, penting untuk memastikan ejen berkelakuan dengan selamat dan beretika. Kebolehamatan menyediakan jejak audit tindakan dan keputusan ejen. Ini boleh digunakan untuk mengesan dan mengurangkan isu seperti suntikan prompt, penghasilan kandungan berbahaya, atau pengendalian maklumat peribadi yang salah (PII). Contohnya, anda boleh menyemak jejak untuk memahami mengapa ejen memberikan respons tertentu atau menggunakan alat spesifik.
*   **Gelung Penambahbaikan Berterusan:** Data kebolehamatan adalah asas kepada proses pembangunan iteratif. Dengan memantau bagaimana ejen berprestasi dalam dunia sebenar, pasukan boleh mengenal pasti bidang untuk penambahbaikan, mengumpul data untuk melaras model, dan mengesahkan impak perubahan. Ini mencipta gelung maklum balas di mana pandangan pengeluaran dari penilaian dalam talian memaklumkan eksperimen luar talian dan penambahbaikan, membawa kepada prestasi ejen yang semakin baik.

## Metik Utama untuk Dipantau

Untuk memantau dan memahami tingkah laku ejen, pelbagai metik dan isyarat harus dipantau. Walaupun metik khusus mungkin berbeza bergantung pada tujuan ejen, beberapa adalah penting secara universal.

Berikut adalah beberapa metik yang paling biasa dipantau oleh alat kebolehamatan:

**Latensi:** Seberapa cepat ejen memberi respons? Masa menunggu yang panjang memberi kesan negatif pada pengalaman pengguna. Anda harus mengukur latensi untuk tugasan dan langkah individu dengan menjejak larian ejen. Contohnya, ejen yang mengambil masa 20 saat untuk semua panggilan model boleh dipercepatkan dengan menggunakan model yang lebih laju atau dengan menjalankan panggilan model secara selari.

**Kos:** Berapakah kos per larian ejen? Ejen AI bergantung pada panggilan LLM yang dicaj per token atau API luaran. Penggunaan alat yang kerap atau pelbagai prompt boleh meningkatkan kos dengan cepat. Sebagai contoh, jika ejen memanggil LLM lima kali untuk peningkatan kualiti marginal, anda mesti menilai sama ada kos itu wajar atau boleh mengurangkan jumlah panggilan atau menggunakan model yang lebih murah. Pemantauan masa nyata juga boleh membantu mengenal pasti lonjakan tidak dijangka (contohnya, pepijat yang menyebabkan gelung API berlebihan).

**Ralat Permintaan:** Berapa banyak permintaan yang gagal oleh ejen? Ini boleh termasuk ralat API atau panggilan alat yang gagal. Untuk menjadikan ejen anda lebih tahan terhadap ini dalam pengeluaran, anda boleh menyediakan mekanisme gantian atau cubaan semula. Contohnya jika penyedia LLM A tidak berfungsi, anda beralih ke penyedia LLM B sebagai sandaran.

**Maklum Balas Pengguna:** Melaksanakan penilaian pengguna secara langsung memberikan pandangan bernilai. Ini boleh termasuk penarafan eksplisit (👍setuju/👎tidak setuju, ⭐1-5 bintang) atau komen teks. Maklum balas negatif yang konsisten harus memberi amaran kerana ini tanda ejen tidak berfungsi seperti dijangkakan.

**Maklum Balas Pengguna Secara Tidak Langsung:** Tingkah laku pengguna memberikan maklum balas tidak langsung walaupun tanpa penarafan eksplisit. Ini boleh termasuk segera memformulasikan semula soalan, pertanyaan berulang atau menekan butang cuba semula. Contohnya jika anda melihat pengguna berulang kali bertanya soalan yang sama, ini tanda ejen tidak berfungsi seperti dijangkakan.

**Ketepatan:** Seberapa kerap ejen menghasilkan output yang betul atau diingini? Definisi ketepatan berbeza (contohnya, ketepatan penyelesaian masalah, ketepatan pencarian maklumat, kepuasan pengguna). Langkah pertama adalah untuk mentakrifkan apa yang dianggap kejayaan untuk ejen anda. Anda boleh mengesan ketepatan melalui pemeriksaan automatik, skor penilaian, atau label penyelesaian tugasan. Contohnya, menandakan jejak sebagai "berjaya" atau "gagal".

**Metik Penilaian Automatik:** Anda juga boleh menyediakan penilaian automatik. Contohnya, anda boleh menggunakan LLM untuk menilai output ejen sama ada ia membantu, tepat, atau tidak. Terdapat juga beberapa perpustakaan sumber terbuka yang membantu anda menilai aspek berbeza ejen. Contohnya [RAGAS](https://docs.ragas.io/) untuk ejen RAG atau [LLM Guard](https://llm-guard.com/) untuk mengesan bahasa berbahaya atau suntikan prompt.

Dalam praktik, gabungan metik ini memberikan liputan terbaik tentang kesihatan ejen AI. Dalam [notebook contoh](./code_samples/10-expense_claim-demo.ipynb) bab ini, kami akan tunjukkan bagaimana metik ini kelihatan dalam contoh nyata tetapi pertama, kita akan pelajari bagaimana aliran kerja penilaian biasa.

## Instrumentasi Ejen Anda

Untuk mengumpul data jejak, anda perlu menginstrumentasi kod anda. Matlamatnya adalah untuk menginstrumentasi kod ejen supaya menghasilkan jejak dan metik yang boleh ditangkap, diproses, dan divisualisasi oleh platform kebolehamatan.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) telah muncul sebagai standard industri untuk kebolehamatan LLM. Ia menyediakan set API, SDK, dan alat untuk menjana, mengumpul, dan mengeksport data telemetri.

Terdapat banyak perpustakaan instrumentasi yang membungkus rangka kerja ejen sedia ada dan memudahkan eksport rentang OpenTelemetry ke alat kebolehamatan. Microsoft Agent Framework berintegrasi secara asli dengan OpenTelemetry. Berikut adalah contoh instrumen ejen MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Pelaksanaan ejen dijejak secara automatik
    pass
```

[notebook contoh](./code_samples/10-expense_claim-demo.ipynb) dalam bab ini akan menunjukkan bagaimana untuk menginstrumentasi ejen MAF anda.

**Penciptaan Rentang Manual:** Walaupun perpustakaan instrumentasi menyediakan asas yang baik, seringkali terdapat kes di mana maklumat lebih terperinci atau khusus diperlukan. Anda boleh mencipta rentang secara manual untuk menambah logik aplikasi tersendiri. Lebih penting, mereka boleh memperkayakan rentang yang diwujudkan secara automatik atau manual dengan atribut tersuai (juga dikenali sebagai tag atau metadata). Atribut ini boleh termasuk data khusus perniagaan, pengiraan perantaraan, atau konteks yang berguna untuk penyahpepijatan atau analisis, seperti `user_id`, `session_id`, atau `model_version`.

Contoh mencipta jejak dan rentang secara manual dengan [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Penilaian Ejen

Kebolehamatan memberikan kita metik, tetapi penilaian adalah proses menganalisis data tersebut (dan melaksanakan ujian) untuk menentukan sejauh mana prestasi ejen AI dan bagaimana ia boleh diperbaiki. Dengan kata lain, setelah anda mempunyai jejak dan metik itu, bagaimana anda menggunakannya untuk menilai ejen dan membuat keputusan?

Penilaian berkala penting kerana ejen AI kerap tidak deterministik dan boleh berkembang (melalui kemas kini atau perubahan tingkah laku model) - tanpa penilaian, anda tidak akan tahu jika “ejen pintar” anda benar-benar menjalankan tugas dengan baik atau telah mengalami kemerosotan.

Terdapat dua kategori penilaian untuk ejen AI: **penilaian dalam talian** dan **penilaian luar talian**. Kedua-duanya berharga dan saling melengkapi. Biasanya kita mulakan dengan penilaian luar talian, kerana ini adalah langkah minimum yang diperlukan sebelum menggunakan mana-mana ejen.

### Penilaian Luar Talian

![Item set data dalam Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Ini melibatkan penilaian ejen dalam persekitaran terkawal, biasanya menggunakan dataset ujian, bukan pertanyaan pengguna secara langsung. Anda menggunakan dataset terpilih di mana anda tahu output yang dijangkakan atau tingkah laku yang betul, kemudian jalankan ejen anda pada dataset tersebut.

Contohnya, jika anda membina ejen masalah kata matematik, anda mungkin mempunyai [dataset ujian](https://huggingface.co/datasets/gsm8k) dengan 100 masalah dan jawapan yang diketahui. Penilaian luar talian sering dilakukan semasa pembangunan (dan boleh menjadi sebahagian dari aliran CI/CD) untuk memeriksa penambahbaikan atau mengelakkan regresi. Kelebihannya adalah ia **boleh diulang dan anda boleh memperoleh metik ketepatan yang jelas kerana anda ada fakta sebenar**. Anda juga boleh mensimulasikan pertanyaan pengguna dan mengukur respons ejen dengan jawapan ideal atau menggunakan metik automatik seperti yang diterangkan tadi.

Cabaran utama dengan penilaian luar talian ialah memastikan dataset ujian anda komprehensif dan kekal relevan – ejen mungkin berprestasi baik pada set ujian tetap tetapi menghadapi pertanyaan yang sangat berbeza dalam pengeluaran. Oleh itu, anda harus menjaga set ujian agar sentiasa dikemas kini dengan kes edge baru dan contoh yang mencerminkan senario dunia sebenar. Campuran kes ujian kecil "uji asap" dan set penilaian besar berguna: set kecil untuk pemeriksaan cepat dan set lebih besar untuk metrik prestasi yang lebih luas.

### Penilaian Dalam Talian

![Gambaran metrik kebolehamatan](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Ini merujuk kepada penilaian ejen dalam persekitaran langsung dan sebenar, iaitu semasa penggunaan sebenar dalam pengeluaran. Penilaian dalam talian melibatkan pemantauan prestasi ejen pada interaksi pengguna sebenar dan menganalisis hasil secara berterusan.

Sebagai contoh, anda mungkin menjejaki kadar kejayaan, skor kepuasan pengguna, atau metik lain pada trafik langsung. Kelebihan penilaian dalam talian adalah ia **menangkap perkara yang mungkin anda tidak jangka dalam suasana makmal** – anda boleh memerhati perubahan model dari masa ke masa (jika keberkesanan ejen merosot apabila corak input berubah) dan menangkap pertanyaan atau situasi tidak dijangka yang tidak terdapat dalam data ujian anda. Ia memberikan gambaran sebenar bagaimana ejen berkelakuan dalam persekitaran sebenar.

Penilaian dalam talian sering melibatkan pengumpulan maklum balas pengguna secara langsung dan tidak langsung, seperti dibincangkan, dan kemungkinan menjalankan ujian bayangan atau ujian A/B (di mana versi baru ejen berjalan secara selari untuk dibandingkan dengan versi lama). Cabarannya ialah sukar untuk mendapatkan label atau skor yang boleh dipercayai untuk interaksi langsung – anda mungkin bergantung pada maklum balas pengguna atau metrik hiliran (contohnya, adakah pengguna klik hasil).

### Menggabungkan Kedua-duanya

Penilaian dalam talian dan luar talian tidak saling eksklusif; mereka sangat saling melengkapi. Pandangan dari pemantauan dalam talian (contohnya, jenis pertanyaan pengguna baru di mana ejen berprestasi buruk) boleh digunakan untuk menambah dan memperbaiki dataset ujian luar talian. Sebaliknya, ejen yang berprestasi baik dalam ujian luar talian boleh digunakan dengan lebih yakin dan dipantau dalam talian.

Malahan, banyak pasukan menggunakan gelung:

_penilaian luar talian -> guna -> pantau dalam talian -> kumpul kes kegagalan baru -> tambah ke dataset luar talian -> perbaiki ejen -> ulang._

## Isu Biasa

Apabila anda menggunakan ejen AI dalam pengeluaran, anda mungkin menghadapi pelbagai cabaran. Berikut adalah beberapa isu biasa dan penyelesaian berpotensi:

| **Isu**    | **Penyelesaian Potensi**   |
| ------------- | ------------------ |
| Ejen AI tidak melaksanakan tugasan secara konsisten | - Perhalusi prompt yang diberikan kepada Ejen AI; jelas pada objektif.<br>- Kenal pasti bila membahagi tugasan kepada subtugas dan mengendalikannya oleh pelbagai ejen boleh membantu. |
| Ejen AI terjebak dalam gelung berterusan  | - Pastikan anda mempunyai terma dan syarat penamatan yang jelas supaya Ejen tahu bila untuk menghentikan proses.<br>- Untuk tugasan kompleks yang memerlukan penaakulan dan perancangan, gunakan model lebih besar yang khusus untuk tugasan penaakulan. |
| Panggilan alat ejen AI tidak berprestasi baik   | - Uji dan sahkan output alat di luar sistem ejen.<br>- Perhalusi parameter, prompt, dan penamaan alat yang ditentukan.  |
| Sistem Berbilang Ejen tidak berprestasi secara konsisten | - Perhalusi prompt yang diberikan kepada setiap ejen untuk memastikan ia spesifik dan berbeza antara satu sama lain.<br>- Bina sistem hierarki menggunakan ejen "penghalaan" atau pengawal untuk menentukan ejen yang betul. |

Banyak isu ini boleh dikenalpasti dengan lebih berkesan dengan kebolehamatan disediakan. Jejak dan metik yang kita bincangkan sebelum ini membantu mengenal pasti dengan tepat di mana dalam aliran kerja ejen masalah berlaku, menjadikan penyahpepijatan dan pengoptimuman lebih cekap.

## Menguruskan Kos
Berikut adalah beberapa strategi untuk menguruskan kos penyebaran agen AI ke produksi:

**Menggunakan Model Lebih Kecil:** Model Bahasa Kecil (SLMs) boleh berfungsi dengan baik pada beberapa kes penggunaan agentik tertentu dan akan mengurangkan kos dengan ketara. Seperti yang disebutkan tadi, membina sistem penilaian untuk menentukan dan membandingkan prestasi berbanding model yang lebih besar adalah cara terbaik untuk memahami sejauh mana SLM akan berfungsi pada kes penggunaan anda. Pertimbangkan menggunakan SLM untuk tugas yang lebih mudah seperti klasifikasi niat atau ekstraksi parameter, sambil mengekalkan model yang lebih besar untuk penalaran kompleks.

**Menggunakan Model Router:** Strategi yang serupa adalah menggunakan kepelbagaian model dan saiz. Anda boleh menggunakan LLM/SLM atau fungsi tanpa pelayan untuk mengarahkan permintaan berdasarkan kerumitan kepada model yang paling sesuai. Ini juga akan membantu mengurangkan kos sambil memastikan prestasi pada tugas yang betul. Contohnya, arahkan pertanyaan mudah kepada model yang lebih kecil dan lebih pantas, dan hanya gunakan model besar yang mahal untuk tugas penalaran kompleks.

**Caching Respons:** Mengenal pasti permintaan dan tugas biasa serta menyediakan responsnya sebelum ia melalui sistem agentik anda adalah cara yang baik untuk mengurangkan jumlah permintaan yang serupa. Anda juga boleh melaksanakan satu aliran untuk mengenal pasti betapa serupanya sesuatu permintaan dengan permintaan yang telah dicache menggunakan model AI yang lebih asas. Strategi ini boleh mengurangkan kos dengan ketara untuk soalan yang sering ditanya atau aliran kerja biasa.

## Mari lihat bagaimana ini berfungsi dalam praktik

Dalam [contoh notebook bahagian ini](./code_samples/10-expense_claim-demo.ipynb), kita akan melihat contoh bagaimana kita boleh menggunakan alat kebolehlihatan untuk memantau dan menilai agen kita.


### Ada Lagi Soalan tentang Agen AI di Produksi?

Sertai [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) untuk bertemu dengan pelajar lain, menghadiri waktu pejabat dan mendapatkan jawapan untuk soalan anda tentang Agen AI.

## Pelajaran Sebelumnya

[Corak Reka Bentuk Metakognisi](../09-metacognition/README.md)

## Pelajaran Seterusnya

[Protokol Agentik](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat kritikal, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->