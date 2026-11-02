# Ejen AI dalam Pengeluaran: Kebolehlihatan & Penilaian

[![Ejen AI dalam Pengeluaran](../../../translated_images/ms/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Apabila ejen AI bergerak dari prototaip eksperimental ke aplikasi dunia nyata, keupayaan untuk memahami tingkah laku mereka, memantau prestasi mereka, dan menilai output mereka secara sistematik menjadi penting.

## Matlamat Pembelajaran

Selepas menyelesaikan pelajaran ini, anda akan mengetahui/bermaksud untuk:
- Konsep asas kebolehlihatan dan penilaian ejen
- Teknik untuk meningkatkan prestasi, kos, dan keberkesanan ejen
- Apa dan bagaimana menilai ejen AI anda secara sistematik
- Bagaimana mengawal kos apabila melaksanakan ejen AI dalam pengeluaran
- Bagaimana menginstrumen ejen yang dibina dengan Microsoft Agent Framework

Matlamatnya adalah untuk membekalkan anda dengan pengetahuan untuk mengubah ejen “kotak hitam” anda menjadi sistem yang telus, boleh diurus, dan boleh dipercayai.

_**Nota:** Adalah penting untuk melancarkan Ejen AI yang selamat dan boleh dipercayai. Lihat pelajaran [Membina Ejen AI Boleh Dipercayai](../06-building-trustworthy-agents/README.md) juga._

## Jejak dan Sepan

Alat kebolehlihatan seperti [Langfuse](https://langfuse.com/) atau [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) biasanya mewakili larian ejen sebagai jejak dan sepan.

- **Jejak** mewakili tugas ejen lengkap dari mula hingga selesai (seperti mengendalikan pertanyaan pengguna).
- **Sepan** adalah langkah individu dalam jejak tersebut (seperti memanggil model bahasa atau mengambil data).

![Pohon jejak dalam Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Tanpa kebolehlihatan, ejen AI boleh terasa seperti “kotak hitam” - keadaan dalaman dan alasanannya tidak jelas, menjadikannya sukar untuk mendiagnosis isu atau mengoptimumkan prestasi. Dengan kebolehlihatan, ejen menjadi “kotak kaca,” menawarkan ketelusan yang penting untuk membina kepercayaan dan memastikan mereka beroperasi seperti yang dimaksudkan.

## Mengapa Kebolehlihatan Penting dalam Persekitaran Pengeluaran

Peralihan ejen AI ke persekitaran pengeluaran memperkenalkan satu set cabaran dan keperluan baru. Kebolehlihatan bukan lagi hanya “bagus untuk ada” tetapi satu keupayaan kritikal:

*   **Penyahpepijatan dan Analisis Punca Asal**: Apabila ejen gagal atau menghasilkan output yang tidak dijangka, alat kebolehlihatan memberikan jejak yang diperlukan untuk mengenal pasti sumber ralat. Ini sangat penting dalam ejen kompleks yang mungkin melibatkan pelbagai panggilan LLM, interaksi alat, dan logik bersyarat.
*   **Pengurusan Laten dan Kos**: Ejen AI sering bergantung pada LLM dan API luar yang dikenakan bayaran per token atau per panggilan. Kebolehlihatan membolehkan penjejakan tepat panggilan ini, membantu mengenal pasti operasi yang terlalu lambat atau mahal. Ini membolehkan pasukan mengoptimumkan arahan prompt, memilih model yang lebih cekap, atau mereka semula aliran kerja untuk mengurus kos operasi dan memastikan pengalaman pengguna yang baik.
*   **Kepercayaan, Keselamatan, dan Pematuhan**: Dalam banyak aplikasi, penting untuk memastikan ejen bertindak dengan selamat dan beretika. Kebolehlihatan menyediakan jejak audit tindakan dan keputusan ejen. Ini boleh digunakan untuk mengesan dan mengurangkan isu seperti suntikan prompt, penghasilan kandungan yang merbahaya, atau pengendalian maklumat peribadi yang salah (PII). Contohnya, anda boleh menyemak jejak untuk memahami mengapa ejen memberikan respons tertentu atau menggunakan alat tertentu.
*   **Gelung Peningkatan Berterusan**: Data kebolehlihatan adalah asas proses pembangunan iteratif. Dengan memantau bagaimana ejen berprestasi dalam dunia sebenar, pasukan boleh mengenal pasti bidang untuk penambahbaikan, mengumpul data untuk penalaan model, dan mengesahkan impak perubahan. Ini mewujudkan gelung maklum balas di mana wawasan pengeluaran dari penilaian dalam talian memaklumkan eksperimen luar talian dan penambahbaikan, yang membawa kepada prestasi ejen yang semakin baik.

## Metrik Utama Untuk Jejak

Untuk memantau dan memahami tingkah laku ejen, pelbagai metrik dan isyarat harus dijejak. Walaupun metrik tertentu mungkin berbeza berdasarkan tujuan ejen, beberapa adalah penting secara universal.

Berikut adalah beberapa metrik paling biasa yang dipantau oleh alat kebolehlihatan:

**Laten:** Berapa cepat ejen memberi respons? Masa menunggu yang lama memberi kesan negatif terhadap pengalaman pengguna. Anda harus mengukur laten untuk tugas dan langkah individu dengan menjejak larian ejen. Contohnya, ejen yang mengambil masa 20 saat untuk semua panggilan model boleh dipercepat dengan menggunakan model yang lebih pantas atau dengan menjalankan panggilan model secara selari.

**Kos:** Berapakah perbelanjaan setiap larian ejen? Ejen AI bergantung pada panggilan LLM yang dikenakan bayaran per token atau API luar. Penggunaan alat yang kerap atau prompt berganda boleh dengan cepat meningkatkan kos. Sebagai contoh, jika ejen memanggil LLM lima kali untuk peningkatan kualiti marginal, anda mesti menilai sama ada kos itu berbaloi atau jika anda boleh mengurangkan bilangan panggilan atau menggunakan model yang lebih murah. Pemantauan masa nyata juga boleh membantu mengenal pasti lonjakan tak dijangka (contohnya, pepijat yang menyebabkan gelung API berlebihan).

**Ralat Permintaan:** Berapa banyak permintaan yang gagal dilakukan oleh ejen? Ini boleh termasuk ralat API atau panggilan alat yang gagal. Untuk menjadikan ejen anda lebih kukuh terhadap ini dalam pengeluaran, anda kemudian boleh menyediakan penyelesaian penggantian atau cubaan semula. Contohnya jika penyedia LLM A tidak berfungsi, anda beralih kepada penyedia LLM B sebagai sandaran.

**Maklum Balas Pengguna:** Melaksanakan penilaian pengguna secara langsung memberikan pandangan berharga. Ini boleh merangkumi penarafan eksplisit (👍setuju/👎tidak setuju, ⭐1-5 bintang) atau komen teks. Maklum balas negatif yang konsisten harus memberi amaran kerana ini tanda ejen tidak berfungsi seperti yang dijangkakan.

**Maklum Balas Pengguna Tidak Langsung:** Tingkah laku pengguna memberi maklum balas tidak langsung walaupun tanpa penarafan eksplisit. Ini boleh merangkumi penjanaan semula soalan segera, pertanyaan berulang atau klik butang cuba semula. Contohnya jika anda melihat pengguna bertanya soalan yang sama berulang kali, ini adalah tanda ejen tidak berfungsi seperti yang dijangkakan.

**Ketepatan:** Berapa kerap ejen menghasilkan output yang betul atau diingini? Definisi ketepatan berbeza-beza (contohnya, ketepatan penyelesaian masalah, ketepatan maklumat, kepuasan pengguna). Langkah pertama ialah mendefinisikan apa itu kejayaan untuk ejen anda. Anda boleh menjejak ketepatan melalui pemeriksaan automatik, skor penilaian, atau label penyelesaian tugas. Contohnya, menandakan jejak sebagai "berjaya" atau "gagal".

**Metrik Penilaian Automatik:** Anda juga boleh menyediakan evaluasi automatik. Sebagai contoh, anda boleh menggunakan LLM untuk menilai output ejen contohnya jika ia membantu, tepat, atau tidak. Terdapat juga beberapa perpustakaan sumber terbuka yang membantu anda menilai aspek berbeza ejen. Contohnya [RAGAS](https://docs.ragas.io/) untuk ejen RAG atau [LLM Guard](https://github.com/protectai/llm-guard) untuk mengesan bahasa merbahaya atau suntikan prompt.

Dalam praktiknya, gabungan metrik ini memberi liputan terbaik untuk kesihatan ejen AI. Dalam [notebook contoh](./code_samples/10-expense_claim-demo.ipynb) dalam bab ini, kami akan menunjukkan bagaimana metrik ini kelihatan dalam contoh sebenar tetapi pertama, kita akan belajar bagaimana aliran kerja penilaian tipikal kelihatan.

## Instrumen Ejen Anda

Untuk mengumpul data jejak, anda perlu menginstrumen kod anda. Matlamatnya adalah untuk menginstrumen kod ejen supaya mengeluarkan jejak dan metrik yang boleh ditangkap, diproses, dan divisualisasikan oleh platform kebolehlihatan.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) muncul sebagai standard industri untuk kebolehlihatan LLM. Ia menyediakan satu set API, SDK, dan alat untuk menjana, mengumpul, dan mengeksport data telemetri.

Terdapat banyak perpustakaan instrumentasi yang membungkus rangka kerja ejen sedia ada dan memudahkan pengeksportan sepan OpenTelemetry ke alat kebolehlihatan. Microsoft Agent Framework berintegrasi secara asli dengan OpenTelemetry. Berikut adalah contoh penginstrumentasian ejen MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agent execution is traced automatically
    pass
```

[notebook contoh](./code_samples/10-expense_claim-demo.ipynb) dalam bab ini akan menunjukkan cara menginstrumen ejen MAF anda.

**Penciptaan Sepan Manual:** Walaupun perpustakaan instrumentasi menyediakan asas yang baik, sering terdapat kes di mana maklumat yang lebih terperinci atau khusus diperlukan. Anda boleh mencipta sepan secara manual untuk menambah logik aplikasi khusus. Lebih penting, mereka boleh memperkayakan sepan yang dicipta secara automatik atau manual dengan atribut khusus (juga dikenali sebagai tag atau metadata). Atribut ini boleh merangkumi data khusus perniagaan, pengiraan pertengahan, atau sebarang konteks yang mungkin berguna untuk penyahpepijatan atau analisis, seperti `user_id`, `session_id`, atau `model_version`.

Contoh penciptaan jejak dan sepan secara manual dengan [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Penilaian Ejen

Kebolehlihatan memberi kita metrik, tetapi penilaian adalah proses menganalisis data itu (dan melakukan ujian) untuk menentukan sejauh mana ejen AI berprestasi dan bagaimana ia boleh diperbaiki. Dengan kata lain, setelah anda mempunyai jejak dan metrik tersebut, bagaimana anda menggunakannya untuk menilai ejen dan membuat keputusan?

Penilaian berkala penting kerana ejen AI sering tidak deterministik dan boleh berkembang (melalui kemas kini atau perubahan tingkah laku model) – tanpa penilaian, anda tidak akan tahu jika “ejen pintar” anda benar-benar menjalankan tugasnya dengan baik atau jika ia menurun prestasi.

Terdapat dua kategori penilaian untuk ejen AI: **penilaian dalam talian** dan **penilaian luar talian**. Kedua-duanya bernilai, dan saling melengkapkan. Biasanya kita mulakan dengan penilaian luar talian, kerana ini adalah langkah minimum yang perlu sebelum melancarkan mana-mana ejen.

### Penilaian Luar Talian

![Item dataset dalam Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Ini melibatkan menilai ejen dalam persekitaran terkawal, biasanya menggunakan dataset ujian, bukan pertanyaan pengguna langsung. Anda menggunakan dataset terpilih di mana anda tahu apa output dijangka atau tingkah laku betul, dan kemudian menjalankan ejen anda pada dataset tersebut.

Contohnya, jika anda membina ejen menyelesaikan masalah kata matematik, anda mungkin mempunyai [dataset ujian](https://huggingface.co/datasets/openai/gsm8k) dengan 100 masalah beserta jawapan yang diketahui. Penilaian luar talian sering dilakukan semasa pembangunan (dan boleh menjadi sebahagian daripada pipeline CI/CD) untuk memeriksa peningkatan atau mencegah kejatuhan prestasi. Kelebihannya adalah ia **boleh diulang dan anda boleh mendapat metrik ketepatan yang jelas kerana anda mempunyai kebenaran asas**. Anda juga mungkin mensimulasikan pertanyaan pengguna dan mengukur respons ejen terhadap jawapan ideal atau menggunakan metrik automatik seperti yang diterangkan di atas.

Cabaran utama dengan penilaian luar talian ialah memastikan dataset ujian anda komprehensif dan kekal relevan – ejen mungkin berprestasi baik pada set ujian tetap tetapi menghadapi pertanyaan yang sangat berbeza dalam pengeluaran. Oleh itu, anda harus sentiasa mengemas kini set ujian dengan kes tepi baru dan contoh yang mencerminkan senario dunia nyata. Campuran kes ujian “smoke test” kecil dan set penilaian besar berguna: set kecil untuk pemeriksaan cepat dan set besar untuk metrik prestasi yang lebih luas.

### Penilaian Dalam Talian

![Gambaran keseluruhan metrik kebolehlihatan](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Ini merujuk kepada menilai ejen dalam persekitaran langsung, dunia nyata, iaitu semasa penggunaan sebenar dalam pengeluaran. Penilaian dalam talian melibatkan pemantauan prestasi ejen pada interaksi pengguna sebenar dan menganalisis keputusan secara berterusan.

Contohnya, anda mungkin menjejaki kadar kejayaan, skor kepuasan pengguna, atau metrik lain pada trafik langsung. Kelebihan penilaian dalam talian adalah ia **menangkap perkara yang mungkin tidak anda jangka dalam persekitaran makmal** – anda boleh memerhati pergeseran model dari masa ke masa (jika keberkesanan ejen menurun apabila corak input berubah) dan menangkap pertanyaan atau situasi yang tidak dijangkakan yang tidak terdapat dalam data ujian anda. Ia memberikan gambaran sebenar bagaimana ejen berkelakuan di lapangan.

Penilaian dalam talian sering melibatkan pengumpulan maklum balas pengguna tidak langsung dan langsung, seperti dibincangkan, dan mungkin menjalankan ujian bayang atau ujian A/B (di mana versi baru ejen berjalan sebaris untuk dibandingkan dengan versi lama). Cabarannya adalah agak sukar mendapatkan label atau skor yang boleh dipercayai untuk interaksi langsung – anda mungkin bergantung pada maklum balas pengguna atau metrik hiliran (seperti jika pengguna mengklik hasil).

### Menggabungkan Kedua-duanya

Penilaian dalam talian dan luar talian tidak saling eksklusif; mereka sangat melengkapi antara satu sama lain. Wawasan daripada pemantauan dalam talian (contohnya, jenis pertanyaan pengguna baru di mana ejen berprestasi buruk) boleh digunakan untuk menambah dan memperbaiki dataset ujian luar talian. Sebaliknya, ejen yang berprestasi baik dalam ujian luar talian boleh kemudian lebih yakin dilancarkan dan dipantau secara dalam talian.

Malah, banyak pasukan mengamalkan satu kitaran:

_nilai luar talian -> lancar -> pantau dalam talian -> kumpul kes kegagalan baru -> tambah ke dataset luar talian -> halus ejen -> ulang_.

## Isu Biasa

Semasa anda melancarkan ejen AI ke pengeluaran, anda mungkin menghadapi pelbagai cabaran. Berikut adalah beberapa isu biasa dan penyelesaian potensialnya:

| **Isu**    | **Penyelesaian Potensial**   |
| ------------- | ------------------ |
| Ejen AI tidak melaksanakan tugas secara konsisten | - Perhalusi prompt yang diberikan kepada Ejen AI; jelaskan objektif.<br>- Kenal pasti di mana pembahagian tugas kepada sub-tugas dan pengendalian oleh beberapa ejen boleh membantu. |
| Ejen AI terperangkap dalam gelung berterusan  | - Pastikan anda mempunyai terma dan syarat pemberhentian yang jelas supaya Ejen tahu bila untuk berhenti proses.<br>- Untuk tugas kompleks yang memerlukan penaakulan dan perancangan, gunakan model yang lebih besar yang khusus untuk tugas penaakulan. |
| Panggilan alat Ejen AI tidak berfungsi dengan baik   | - Uji dan sahkan output alat di luar sistem ejen.<br>- Perhalusi parameter, prompt, dan penamaan alat yang ditetapkan.  |
| Sistem Multi-Ejen tidak berfungsi secara konsisten | - Perhalusi prompt yang diberikan kepada setiap ejen untuk memastikan ia khusus dan berbeza antara satu sama lain.<br>- Bina sistem hierarki menggunakan ejen "routing" atau pengawal untuk menentukan ejen yang betul. |

Banyak isu ini boleh dikenal pasti dengan lebih berkesan dengan kebolehlihatan yang disediakan. Jejak dan metrik yang kita bincangkan sebelum ini membantu mengenal pasti dengan tepat di mana masalah berlaku dalam aliran kerja ejen, menjadikan penyahpepijatan dan pengoptimuman lebih cekap.

## Mengurus Kos

Berikut adalah beberapa strategi untuk mengurus kos melancarkan ejen AI ke pengeluaran:

**Menggunakan Model Lebih Kecil:** Model Bahasa Kecil (SLM) boleh berprestasi baik pada kes penggunaan agentik tertentu dan akan mengurangkan kos dengan ketara. Seperti yang disebutkan sebelum ini, membina sistem penilaian untuk menentukan dan membandingkan prestasi berbanding model yang lebih besar adalah cara terbaik untuk memahami sejauh mana SLM akan berfungsi dalam kes penggunaan anda. Pertimbangkan menggunakan SLM untuk tugasan yang lebih mudah seperti klasifikasi niat atau pengekstrakan parameter, sementara mengekalkan model yang lebih besar untuk pemikiran kompleks.

**Menggunakan Model Penghala:** Strategi yang serupa adalah menggunakan kepelbagaian model dan saiz. Anda boleh menggunakan LLM/SLM atau fungsi tanpa pelayan untuk menghala permintaan berdasarkan kerumitan kepada model yang paling sesuai. Ini juga akan membantu mengurangkan kos sambil memastikan prestasi pada tugasan yang betul. Contohnya, alihkan pertanyaan mudah ke model yang lebih kecil dan pantas, dan hanya gunakan model besar yang mahal untuk tugasan pemikiran kompleks.

**Menyimpan Respons dalam Cache:** Mengenal pasti permintaan dan tugasan biasa serta menyediakan respons sebelum mereka melalui sistem agentik anda adalah cara yang baik untuk mengurangkan jumlah permintaan serupa. Anda juga boleh melaksanakan aliran untuk mengenal pasti sejauh mana permintaan itu serupa dengan permintaan cache anda menggunakan model AI yang lebih asas. Strategi ini boleh mengurangkan kos dengan ketara untuk soalan yang sering ditanya atau aliran kerja biasa.

## Mari lihat bagaimana ini berfungsi dalam praktik

Dalam [notebook contoh bahagian ini](./code_samples/10-expense_claim-demo.ipynb), kita akan melihat contoh bagaimana kita boleh menggunakan alat pemerhatian untuk memantau dan menilai agen kita.


### Ada Lebih Banyak Soalan tentang Ejen AI dalam Pengeluaran?

Sertai [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) untuk berjumpa dengan pembelajar lain, menghadiri waktu pejabat dan dapatkan jawapan untuk soalan Ejen AI anda.

## Pelajaran Sebelumnya

[Corak Reka Bentuk Metakognisi](../09-metacognition/README.md)

## Pelajaran Seterusnya

[Protokol Agentik](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->