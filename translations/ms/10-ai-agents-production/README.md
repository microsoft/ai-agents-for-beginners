# Ejen AI dalam Pengeluaran: Keterlihatan & Penilaian

[![Ejen AI dalam Pengeluaran](../../../translated_images/ms/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Apabila ejen AI bergerak dari prototaip eksperimen kepada aplikasi dunia sebenar, keupayaan untuk memahami tingkah laku mereka, memantau prestasi mereka, dan menilai output mereka secara sistematik menjadi penting.

## Matlamat Pembelajaran

Selepas menamatkan pelajaran ini, anda akan tahu bagaimana untuk/mahu memahami:
- Konsep teras keterlihatan dan penilaian ejen
- Teknik untuk meningkatkan prestasi, kos, dan keberkesanan ejen
- Apa dan bagaimana menilai ejen AI anda secara sistematik
- Bagaimana mengawal kos semasa mengaplikasikan ejen AI ke dalam pengeluaran
- Cara menginstrumentasikan ejen yang dibina dengan Microsoft Agent Framework

Matlamatnya adalah untuk melengkapkan anda dengan pengetahuan untuk mengubah ejen "kotak hitam" anda menjadi sistem yang telus, boleh diurus, dan boleh dipercayai.

_**Nota:** Adalah penting untuk mengaplikasikan Ejen AI yang selamat dan boleh dipercayai. Lihat juga pelajaran [Membina Ejen AI yang Boleh Dipercayai](../06-building-trustworthy-agents/README.md)._

## Jejak dan Julat

Alat keterlihatan seperti [Langfuse](https://langfuse.com/) atau [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) biasanya mewakili larian ejen sebagai jejak dan julat.

- **Jejak** mewakili satu tugasan lengkap ejen dari mula hingga akhir (seperti mengendalikan pertanyaan pengguna).
- **Julat** adalah langkah individu dalam jejak (seperti memanggil model bahasa atau mengambil data).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Tanpa keterlihatan, ejen AI boleh dirasakan seperti "kotak hitam" — keadaan dalaman dan alasanannya tidak jelas, menjadikannya sukar untuk mendiagnosis isu atau mengoptimumkan prestasi. Dengan keterlihatan, ejen menjadi "kotak kaca," yang menawarkan ketelusan yang penting untuk membina kepercayaan dan memastikan ia beroperasi seperti yang dimaksudkan.

## Mengapa Keterlihatan Penting dalam Persekitaran Pengeluaran

Memindahkan ejen AI ke persekitaran pengeluaran memperkenalkan satu set cabaran dan keperluan baru. Keterlihatan bukan lagi "nice-to-have" tetapi keupayaan kritikal:

*   **Pengimbasan Ralat dan Analisis Punca Asal**: Apabila ejen gagal atau menghasilkan output yang tidak dijangka, alat keterlihatan menyediakan jejak yang diperlukan untuk mengenal pasti punca ralat. Ini amat penting dalam ejen yang kompleks yang mungkin melibatkan banyak panggilan LLM, interaksi alat, dan logik bersyarat.
*   **Pengurusan Latensi dan Kos**: Ejen AI sering bergantung kepada LLM dan API luar lain yang dikenakan bayaran per token atau panggilan. Keterlihatan membolehkan penjejakan tepat panggilan-panggilan ini, membantu mengenal pasti operasi yang terlalu lambat atau mahal. Ini membolehkan pasukan mengoptimumkan arahan, memilih model yang lebih cekap, atau mereka bentuk semula aliran kerja untuk menguruskan kos operasi dan memastikan pengalaman pengguna yang baik.
*   **Kepercayaan, Keselamatan, dan Pematuhan**: Dalam banyak aplikasi, penting untuk memastikan ejen berkelakuan selamat dan beretika. Keterlihatan menyediakan jejak audit tindakan dan keputusan ejen. Ini boleh digunakan untuk mengesan dan mengurangkan isu seperti suntikan arahan, penghasilan kandungan berbahaya, atau pengendalian maklumat peribadi yang tidak betul (PII). Contohnya, anda boleh menyemak jejak untuk memahami mengapa ejen memberikan respons tertentu atau menggunakan alat khusus.
*   **Gelung Penambahbaikan Berterusan**: Data keterlihatan adalah asas proses pembangunan berulang. Dengan memantau bagaimana ejen berprestasi di dunia nyata, pasukan boleh mengenal pasti bidang untuk penambahbaikan, mengumpul data untuk melaraskan model, dan mengesahkan impak perubahan. Ini mewujudkan gelung maklum balas di mana pandangan pengeluaran dari penilaian dalam talian memaklumkan percubaan dan penambahbaikan luar talian, membawa kepada prestasi ejen yang semakin baik.

## Metrik Utama untuk Dipantau

Untuk memantau dan memahami tingkah laku ejen, pelbagai metrik dan isyarat harus dijejaki. Walaupun metrik khusus mungkin berbeza bergantung pada tujuan ejen, beberapa adalah penting secara umum.

Berikut adalah beberapa metrik yang paling biasa dipantau oleh alat keterlihatan:

**Latensi:** Seberapa cepat ejen memberi respons? Masa menunggu yang lama memberi kesan negatif kepada pengalaman pengguna. Anda harus mengukur latensi untuk tugasan dan langkah individu dengan menjejaki larian ejen. Contohnya, ejen yang mengambil 20 saat untuk semua panggilan model boleh dipercepatkan dengan menggunakan model yang lebih cepat atau menjalankan panggilan model secara selari.

**Kos:** Berapakah perbelanjaan setiap larian ejen? Ejen AI bergantung pada panggilan LLM yang dikenakan bayaran per token atau API luar. Penggunaan alat yang kerap atau beberapa arahan boleh meningkatkan kos dengan cepat. Contohnya, jika ejen memanggil LLM lima kali untuk peningkatan kualiti yang kecil, anda mesti menilai sama ada kos itu berbaloi atau anda boleh mengurangkan bilangan panggilan atau menggunakan model yang lebih murah. Pemantauan masa nyata juga boleh membantu mengenal pasti lonjakan tak dijangka (contohnya, pepijat yang menyebabkan gelung API berlebihan).

**Ralat Permintaan:** Berapa banyak permintaan yang gagal oleh ejen? Ini boleh termasuk ralat API atau panggilan alat yang gagal. Untuk menjadikan ejen anda lebih tahan terhadap ini dalam pengeluaran, anda boleh mengatur fallback atau cuba semula. Contohnya, jika penyedia LLM A tidak berfungsi, anda bertukar kepada penyedia LLM B sebagai sandaran.

**Maklum Balas Pengguna:** Melaksanakan penilaian pengguna secara langsung menyediakan pandangan yang berharga. Ini boleh termasuk penilaian eksplisit (👍suka/👎tidak suka, ⭐1-5 bintang) atau komen berbentuk teks. Maklum balas negatif yang berterusan harus memberi amaran kerana ini adalah tanda bahawa ejen tidak berfungsi seperti yang dijangka.

**Maklum Balas Pengguna Tidak Eksplisit:** Tingkah laku pengguna memberikan maklum balas tidak langsung walaupun tanpa penilaian eksplisit. Ini boleh termasuk pengubahan soalan segera, pertanyaan berulang atau menekan butang cuba semula. Contohnya, jika anda melihat pengguna berulang kali bertanya soalan yang sama, ini adalah tanda bahawa ejen tidak berfungsi seperti yang dijangka.

**Ketepatan:** Berapa kerap ejen menghasilkan output yang betul atau diingini? Definisi ketepatan berbeza-beza (contohnya, ketepatan penyelesaian masalah, ketepatan pengambilan maklumat, kepuasan pengguna). Langkah pertama adalah untuk mentakrifkan apa yang dianggap kejayaan untuk ejen anda. Anda boleh menjejaki ketepatan melalui pemeriksaan automatik, skor penilaian, atau label penyempurnaan tugasan. Contohnya, menandakan jejak sebagai "berjaya" atau "gagal".

**Metrik Penilaian Automatik:** Anda juga boleh mengatur penilaian automatik. Contohnya, anda boleh menggunakan LLM untuk menilai output ejen seperti sama ada ia membantu, tepat, atau tidak. Terdapat juga beberapa perpustakaan sumber terbuka yang membantu anda menilai pelbagai aspek ejen. Contohnya, [RAGAS](https://docs.ragas.io/) untuk ejen RAG atau [LLM Guard](https://llm-guard.com/) untuk mengesan bahasa berbahaya atau suntikan arahan.

Dalam praktik, gabungan metrik ini memberikan liputan terbaik tentang kesihatan ejen AI. Dalam [notebook contoh](./code_samples/10-expense_claim-demo.ipynb) bab ini, kami akan menunjukkan bagaimana metrik ini kelihatan dalam contoh sebenar tetapi pertama, kita akan belajar bagaimana aliran kerja penilaian biasa kelihatan.

## Instrumentasikan Ejen Anda

Untuk mengumpulkan data penjejakan, anda perlu menginstrumentasikan kod anda. Matlamatnya adalah untuk menginstrumentasikan kod ejen agar mengeluarkan jejak dan metrik yang boleh ditangkap, diproses, dan divisualisasikan oleh platform keterlihatan.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) telah menjadi piawaian industri untuk keterlihatan LLM. Ia menyediakan set API, SDK, dan alat untuk menjana, mengumpul, dan mengeksport data telemetri.

Terdapat banyak perpustakaan instrumentasi yang membungkus rangka kerja ejen sedia ada dan memudahkan pengeksportan julat OpenTelemetry ke alat keterlihatan. Microsoft Agent Framework berintegrasi dengan OpenTelemetry secara asli. Berikut adalah contoh instrumentasi ejen MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Pelaksanaan ejen dikesan secara automatik
    pass
```

[notebook contoh](./code_samples/10-expense_claim-demo.ipynb) dalam bab ini akan menunjukkan cara menginstrumentasikan ejen MAF anda.

**Penciptaan Julat Manual:** Walaupun perpustakaan instrumentasi menyediakan asas yang baik, sering terdapat kes di mana maklumat yang lebih terperinci atau khusus diperlukan. Anda boleh mencipta julat secara manual untuk menambah logik aplikasi tersuai. Lebih penting, anda boleh memperkayakan julat yang dicipta secara automatik atau manual dengan atribut tersuai (juga dikenali sebagai tag atau metadata). Atribut ini boleh termasuk data khusus perniagaan, pengiraan pertengahan, atau apa-apa konteks yang mungkin berguna untuk penyahpepijatan atau analisis, seperti `user_id`, `session_id`, atau `model_version`.

Contoh penciptaan jejak dan julat secara manual menggunakan [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Penilaian Ejen

Keterlihatan memberi kita metrik, tetapi penilaian adalah proses menganalisis data itu (dan melakukan ujian) untuk menentukan sejauh mana ejen AI berprestasi dan bagaimana ia boleh diperbaiki. Dengan kata lain, setelah anda mempunyai jejak dan metrik tersebut, bagaimana anda menggunakannya untuk menilai ejen dan membuat keputusan?

Penilaian berkala penting kerana ejen AI sering tidak deterministik dan boleh berkembang (melalui kemas kini atau perubahan tingkah laku model) – tanpa penilaian, anda tidak akan tahu sama ada “ejen pintar” anda sebenarnya menjalankan tugas dengan baik atau jika ia telah merosot.

Terdapat dua kategori penilaian untuk ejen AI: **penilaian dalam talian** dan **penilaian luar talian**. Kedua-duanya bernilai dan saling melengkapi. Kami biasanya mulakan dengan penilaian luar talian, kerana ini adalah langkah minimum yang diperlukan sebelum mengaplikasikan mana-mana ejen.

### Penilaian Luar Talian

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Ini melibatkan menilai ejen dalam persekitaran terkawal, biasanya menggunakan set data ujian, bukannya pertanyaan pengguna secara langsung. Anda menggunakan set data terpilih di mana anda tahu apa output yang dijangka atau tingkah laku yang betul, dan kemudian jalankan ejen anda ke atasnya.

Sebagai contoh, jika anda membina ejen masalah matematik perkataan, anda mungkin mempunyai [set data ujian](https://huggingface.co/datasets/gsm8k) dengan 100 masalah dengan jawapan diketahui. Penilaian luar talian sering dilakukan semasa pembangunan (dan boleh menjadi sebahagian daripada saluran CI/CD) untuk memeriksa penambahbaikan atau melindungi daripada kemerosotan. Kelebihannya ialah ia **boleh diulang dan anda boleh mendapatkan metrik ketepatan yang jelas kerana anda mempunyai kebenaran asas**. Anda juga boleh mensimulasikan pertanyaan pengguna dan mengukur respons ejen terhadap jawapan ideal atau menggunakan metrik automatik seperti yang diterangkan di atas.

Cabaran utama penilaian luar talian ialah memastikan set data ujian anda komprehensif dan kekal relevan – ejen mungkin berprestasi baik pada set ujian tetap tetapi menghadapi pertanyaan yang sangat berbeza dalam pengeluaran. Oleh itu, anda harus memastikan set ujian dikemas kini dengan kes tepi dan contoh baru yang mencerminkan senario dunia nyata. Campuran kes “ujian asap” kecil dan set penilaian yang lebih besar adalah berguna: set kecil untuk pemeriksaan cepat dan set lebih besar untuk metrik prestasi yang lebih luas.

### Penilaian Dalam Talian

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Ini merujuk kepada menilai ejen dalam persekitaran sebenar yang hidup, iaitu semasa penggunaan sebenar dalam pengeluaran. Penilaian dalam talian melibatkan pemantauan prestasi ejen pada interaksi pengguna sebenar dan menganalisis hasil secara berterusan.

Contohnya, anda boleh menjejaki kadar kejayaan, skor kepuasan pengguna, atau metrik lain pada trafik langsung. Kelebihan penilaian dalam talian ialah ia **menangkap perkara yang mungkin tidak anda jangka dalam persekitaran makmal** – anda boleh memerhati pergeseran model dari masa ke masa (jika keberkesanan ejen merosot apabila corak input berubah) dan menangkap pertanyaan atau situasi tak dijangka yang tidak ada dalam data ujian anda. Ia memberikan gambaran sebenar bagaimana ejen berkelakuan di alam nyata.

Penilaian dalam talian sering melibatkan pengumpulan maklum balas pengguna tidak eksplisit dan eksplisit, seperti yang dibincangkan, dan mungkin menjalankan ujian bayangan atau ujian A/B (di mana versi baru ejen dijalankan secara selari untuk membandingkan dengan versi lama). Cabarannya ialah sukar untuk mendapatkan label atau skor yang boleh dipercayai untuk interaksi langsung – anda mungkin bergantung pada maklum balas pengguna atau metrik huluan (contohnya, sama ada pengguna mengklik hasil).

### Menggabungkan Kedua-duanya

Penilaian dalam talian dan luar talian tidak saling eksklusif; ia sangat melengkapi antara satu sama lain. Pandangan daripada pemantauan dalam talian (contohnya, jenis pertanyaan pengguna baru di mana ejen berprestasi kurang baik) boleh digunakan untuk menambah baik dan memperbaiki set data ujian luar talian. Sebaliknya, ejen yang berprestasi baik dalam ujian luar talian kemudian boleh diaplikasikan dengan lebih yakin dan dipantau secara dalam talian.

Malah, banyak pasukan mengguna pakai gelung:

_nilai luar talian -> terapkan -> pantau dalam talian -> kumpul kes kegagalan baru -> tambah ke set data luar talian -> perhalusi ejen -> ulang_.

## Isu Biasa

Apabila anda mengaplikasikan ejen AI ke pengeluaran, anda mungkin menghadapi pelbagai cabaran. Berikut adalah beberapa isu biasa dan penyelesaian yang berpotensi:

| **Isu**    | **Penyelesaian Berpotensi**   |
| ------------- | ------------------ |
| Ejen AI tidak menjalankan tugasan dengan konsisten | - Perhalusi arahan yang diberikan kepada Ejen AI; jelas tentang objektif.<br>- Kenal pasti di mana pembahagian tugasan kepada sub-tugasan dan pengendalian oleh banyak ejen boleh membantu. |
| Ejen AI terperangkap dalam gelung berterusan  | - Pastikan anda mempunyai syarat dan terma pemberhentian yang jelas supaya Ejen tahu bila harus menghentikan proses.<br>- Untuk tugasan kompleks yang memerlukan penalaran dan perancangan, gunakan model yang lebih besar yang khusus untuk tugasan penalaran. |
| Panggilan alat oleh Ejen AI tidak berprestasi baik   | - Uji dan sahkan output alat di luar sistem ejen.<br>- Perhalusi parameter, arahan, dan penamaan alat yang ditetapkan.  |
| Sistem Multi-Ejen tidak berprestasi konsisten | - Perhalusi arahan yang diberikan kepada setiap ejen untuk memastikan ia spesifik dan berbeza antara satu sama lain.<br>- Bina sistem hierarki menggunakan ejen "routing" atau pengawal untuk menentukan ejen yang betul. |

Banyak isu ini boleh dikenal pasti dengan lebih berkesan dengan adanya keterlihatan. Jejak dan metrik yang kita bincangkan sebelum ini membantu mengenal pasti dengan tepat di mana dalam aliran kerja ejen masalah berlaku, menjadikan penyahpepijatan dan pengoptimuman lebih cekap.

## Menguruskan Kos


Berikut adalah beberapa strategi untuk menguruskan kos penggunaan ejen AI ke dalam pengeluaran:

**Menggunakan Model Lebih Kecil:** Model Bahasa Kecil (SLM) boleh berfungsi dengan baik untuk beberapa kes penggunaan ejen tertentu dan akan mengurangkan kos dengan ketara. Seperti yang disebutkan sebelum ini, membina sistem penilaian untuk menentukan dan membandingkan prestasi berbanding model yang lebih besar adalah cara terbaik untuk memahami sejauh mana SLM akan berprestasi pada kes penggunaan anda. Pertimbangkan menggunakan SLM untuk tugasan yang lebih mudah seperti pengelasan niat atau ekstraksi parameter, sementara menyimpan model yang lebih besar untuk penalaran yang kompleks.

**Menggunakan Model Penghala:** Strategi serupa adalah menggunakan kepelbagaian model dan saiz. Anda boleh menggunakan LLM/SLM atau fungsi tanpa pelayan untuk menghala permintaan berdasarkan kerumitan kepada model yang paling sesuai. Ini juga akan membantu mengurangkan kos sambil memastikan prestasi pada tugasan yang betul. Contohnya, hala pertanyaan mudah kepada model yang lebih kecil dan pantas, dan hanya gunakan model besar yang mahal untuk tugasan penalaran yang kompleks.

**Menyimpan Respons dalam Cache:** Mengenal pasti permintaan dan tugasan yang biasa serta menyediakan respons sebelum ia melalui sistem ejen anda adalah cara yang baik untuk mengurangkan jumlah permintaan yang serupa. Anda juga boleh melaksanakan aliran untuk mengenal pasti sejauh mana permintaan itu serupa dengan permintaan yang disimpan dalam cache menggunakan model AI yang lebih asas. Strategi ini boleh mengurangkan kos dengan ketara untuk soalan yang kerap ditanya atau aliran kerja yang biasa.

## Mari lihat bagaimana ini berfungsi dalam amalan

Dalam [notebook contoh bahagian ini](./code_samples/10-expense_claim-demo.ipynb), kita akan melihat contoh bagaimana kita boleh menggunakan alat pemerhatian untuk memantau dan menilai ejen kita.


### Ada Soalan Lagi tentang Ejen AI dalam Pengeluaran?

Sertai [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) untuk bertemu dengan pelajar lain, menghadiri waktu pejabat dan dapatkan jawapan untuk soalan Ejen AI anda.

## Pelajaran Sebelumnya

[Corak Reka Bentuk Metakognisi](../09-metacognition/README.md)

## Pelajaran Seterusnya

[Protokol Ejen](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->