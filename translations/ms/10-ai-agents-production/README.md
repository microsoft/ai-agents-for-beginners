# Ejen AI dalam Pengeluaran: Kebolehlihatan & Penilaian

[![Ejen AI dalam Pengeluaran](../../../translated_images/ms/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Apabila ejen AI bergerak dari prototaip eksperimen ke aplikasi dunia sebenar, keupayaan untuk memahami tingkah laku mereka, memantau prestasi mereka, dan secara sistematik menilai output mereka menjadi penting.

## Matlamat Pembelajaran

Selepas menamatkan pelajaran ini, anda akan tahu cara/faham:
- Konsep teras kebolehlihatan dan penilaian ejen
- Teknik untuk meningkatkan prestasi, kos, dan keberkesanan ejen
- Apa dan bagaimana menilai ejen AI anda secara sistematik
- Bagaimana mengawal kos apabila melaksanakan ejen AI ke pengeluaran
- Cara menginstrumen ejen yang dibina dengan Microsoft Agent Framework

Matlamatnya adalah untuk melengkapkan anda dengan pengetahuan untuk mengubah ejen "kotak hitam" anda menjadi sistem yang telus, boleh diurus, dan boleh dipercayai.

_**Nota:** Penting untuk melaksanakan Ejen AI yang selamat dan boleh dipercayai. Lihat juga pelajaran [Membina Ejen AI yang Boleh Dipercayai](../06-building-trustworthy-agents/README.md)._

## Jejak dan Rentang

Alat kebolehlihatan seperti [Langfuse](https://langfuse.com/) atau [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) biasanya mewakili larian ejen sebagai jejak dan rentang.

- **Jejak** mewakili tugas ejen lengkap dari awal hingga selesai (seperti mengendalikan pertanyaan pengguna).
- **Rentang** adalah langkah individu dalam jejak (seperti memanggil model bahasa atau mendapatkan data).

![Pohon jejak dalam Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Tanpa kebolehlihatan, ejen AI boleh terasa seperti "kotak hitam" - keadaan dalaman dan alasanannya tidak jelas, menjadikannya sukar untuk mendiagnosis masalah atau mengoptimumkan prestasi. Dengan kebolehlihatan, ejen menjadi "kotak kaca," menawarkan ketelusan yang penting untuk membina kepercayaan dan memastikan mereka beroperasi seperti yang dimaksudkan. 

## Mengapa Kebolehlihatan Penting dalam Persekitaran Pengeluaran

Peralihan ejen AI ke persekitaran pengeluaran memperkenalkan set cabaran dan keperluan baru. Kebolehlihatan bukan lagi "barang mewah" tetapi satu keupayaan kritikal:

*   **Pembuangan Ralat dan Analisis Punca**: Apabila ejen gagal atau menghasilkan output yang tidak dijangka, alat kebolehlihatan menyediakan jejak yang diperlukan untuk mengenal pasti punca ralat. Ini sangat penting dalam ejen kompleks yang mungkin melibatkan panggilan LLM berbilang, interaksi alat, dan logik bersyarat.
*   **Pengurusan Latensi dan Kos**: Ejen AI sering bergantung pada LLM dan API luaran lain yang dikenakan bayaran per token atau per panggilan. Kebolehlihatan membolehkan penjejakan tepat panggilan ini, membantu mengenal pasti operasi yang terlalu perlahan atau mahal. Ini membolehkan pasukan mengoptimumkan arahan, memilih model yang lebih cekap, atau mereka bentuk semula aliran kerja untuk mengawal kos operasi dan memastikan pengalaman pengguna yang baik.
*   **Kepercayaan, Keselamatan, dan Pemenuhan**: Dalam banyak aplikasi, penting untuk memastikan ejen berkelakuan selamat dan beretika. Kebolehlihatan menyediakan rekod audit tindakan dan keputusan ejen. Ini boleh digunakan untuk mengesan dan mengurangkan isu seperti suntikan arahan, penghasilan kandungan berbahaya, atau pengendalian maklumat peribadi yang tidak betul (PII). Contohnya, anda boleh menyemak jejak untuk memahami mengapa ejen memberikan respons tertentu atau menggunakan alat tertentu.
*   **Gelung Penambahbaikan Berterusan**: Data kebolehlihatan adalah asas proses pembangunan iteratif. Dengan memantau bagaimana ejen berfungsi di dunia nyata, pasukan boleh mengenal pasti kawasan untuk penambahbaikan, mengumpul data untuk penalaan model, dan mengesahkan impak perubahan. Ini mencipta gelung maklum balas di mana pandangan pengeluaran dari penilaian dalam talian memaklumkan eksperimen luar talian dan penambahbaikan, membawa kepada prestasi ejen yang semakin baik.

## Metrik Utama untuk Jejak

Untuk memantau dan memahami tingkah laku ejen, pelbagai metrik dan isyarat harus dijejaki. Walaupun metrik tertentu mungkin berbeza berdasarkan tujuan ejen, beberapa adalah penting secara universal.

Berikut adalah beberapa metrik paling biasa yang dipantau oleh alat kebolehlihatan:

**Latensi:** Betapa cepat ejen memberi respons? Masa menunggu yang lama memberi kesan negatif kepada pengalaman pengguna. Anda harus mengukur latensi untuk tugas dan langkah individu dengan menjejaki larian ejen. Sebagai contoh, ejen yang mengambil 20 saat untuk semua panggilan model boleh dipercepat dengan menggunakan model lebih pantas atau menjalankan panggilan model secara selari.

**Kos:** Berapakah perbelanjaan bagi setiap larian ejen? Ejen AI bergantung pada panggilan LLM yang dikenakan bayaran per token atau API luaran. Penggunaan alat yang kerap atau banyak arahan boleh meningkatkan kos dengan cepat. Contohnya, jika ejen memanggil LLM lima kali untuk penambahbaikan kualiti kecil, anda mesti menilai sama ada kos itu berbaloi atau boleh mengurangkan bilangan panggilan atau menggunakan model yang lebih murah. Pemantauan masa nyata juga boleh membantu mengenal pasti lonjakan tidak dijangka (contohnya, pepijat yang menyebabkan gelung API berlebihan).

**Ralat Permintaan:** Berapa banyak permintaan yang gagal oleh ejen? Ini boleh termasuk ralat API atau panggilan alat yang gagal. Untuk menjadikan ejen anda lebih kukuh terhadap ini dalam pengeluaran, anda boleh menyediakan mekanisme sandaran atau cuba semula. Contohnya, jika penyedia LLM A tidak berfungsi, anda beralih ke penyedia LLM B sebagai sandaran.

**Maklum Balas Pengguna:** Melaksanakan penilaian langsung pengguna memberikan pandangan berharga. Ini boleh termasuk penarafan jelas (👍thumbs-up/👎down, ⭐1-5 bintang) atau komen bertulis. Maklum balas negatif berterusan harus memberi amaran kepada anda kerana ini tanda ejen tidak berfungsi seperti dijangka. 

**Maklum Balas Pengguna Tidak Langsung:** Tingkah laku pengguna memberikan maklum balas tidak langsung walaupun tanpa penarafan jelas. Ini boleh termasuk menyusun semula soalan dengan segera, pertanyaan berulang, atau menekan butang cuba semula. Contohnya, jika anda melihat pengguna berulang kali menanyakan soalan yang sama, ini tanda ejen tidak berfungsi seperti dijangka.

**Ketepatan:** Berapa kerap ejen menghasilkan output yang betul atau diingini? Definisi ketepatan berbeza (contohnya, ketepatan penyelesaian masalah, ketepatan pengambilan maklumat, kepuasan pengguna). Langkah pertama adalah mendefinisikan apa yang dilihat sebagai kejayaan untuk ejen anda. Anda boleh menjejak ketepatan melalui pemeriksaan automatik, skor penilaian, atau label penyelesaian tugas. Contohnya, menandakan jejak sebagai "berjaya" atau "gagal". 

**Metrik Penilaian Automatik:** Anda juga boleh menyediakan penilaian automatik. Contohnya, anda boleh menggunakan LLM untuk menilai output ejen sama ada ia membantu, tepat, atau tidak. Terdapat juga beberapa perpustakaan sumber terbuka yang membantu anda menilai aspek berbeza ejen. Contohnya, [RAGAS](https://docs.ragas.io/) untuk ejen RAG atau [LLM Guard](https://llm-guard.com/) untuk mengesan bahasa berbahaya atau suntikan arahan. 

Dalam praktik, gabungan metrik ini memberikan liputan terbaik mengenai kesihatan ejen AI. Dalam [notebook contoh](./code_samples/10-expense_claim-demo.ipynb) bab ini, kami akan tunjukkan bagaimana metrik ini kelihatan dalam contoh sebenar tetapi pertama, kita akan belajar bagaimana aliran kerja penilaian tipikal kelihatan.

## Instrumenkan Ejen Anda

Untuk mengumpul data jejak, anda perlu menginstrumen kod anda. Matlamatnya adalah untuk menginstrumen kod ejen agar mengeluarkan jejak dan metrik yang boleh dirakam, diproses, dan divisualisasikan oleh platform kebolehlihatan.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) telah muncul sebagai standard industri untuk kebolehlihatan LLM. Ia menyediakan set API, SDK, dan alat untuk menjana, mengumpul, dan mengeksport data telemetri. 

Terdapat banyak perpustakaan instrumen yang membungkus rangka kerja ejen sedia ada dan memudahkan penghantaran rentang OpenTelemetry ke alat kebolehlihatan. Microsoft Agent Framework berintegrasi secara asli dengan OpenTelemetry. Berikut adalah contoh menginstrumen ejen MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Pelaksanaan ejen dijejak secara automatik
    pass
```

[notebook contoh](./code_samples/10-expense_claim-demo.ipynb) dalam bab ini akan menunjukkan cara menginstrumen ejen MAF anda.

**Penciptaan Rentang Manual:** Walaupun perpustakaan instrumen menyediakan asas yang baik, sering terdapat kes di mana maklumat lebih terperinci atau tersuai diperlukan. Anda boleh mencipta rentang secara manual untuk menambah logik aplikasi tersuai. Lebih penting, anda boleh memperkayakan rentang yang dicipta secara automatik atau manual dengan atribut tersuai (juga dikenali sebagai tag atau metadata). Atribut ini boleh merangkumi data khusus perniagaan, pengiraan perantaraan, atau konteks yang mungkin berguna untuk pembuangan ralat atau analisis, seperti `user_id`, `session_id`, atau `model_version`.

Contoh penciptaan jejak dan rentang secara manual dengan [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3): 

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Penilaian Ejen

Kebolehlihatan memberikan kita metrik, tetapi penilaian adalah proses menganalisis data itu (dan melakukan ujian) untuk menentukan sejauh mana ejen AI berprestasi dan bagaimana ia boleh diperbaiki. Dengan kata lain, setelah anda mempunyai jejak dan metrik itu, bagaimana anda gunakannya untuk menilai ejen dan membuat keputusan? 

Penilaian berkala penting kerana ejen AI sering tidak deterministik dan boleh berkembang (melalui kemas kini atau perubahan tingkah laku model) – tanpa penilaian, anda tidak akan tahu jika "ejen pintar" anda sebenarnya melakukan tugas dengan baik atau jika ia telah merosot.

Terdapat dua kategori penilaian untuk ejen AI: **penilaian dalam talian** dan **penilaian luar talian**. Kedua-duanya bernilai, dan saling melengkapi. Biasanya kita bermula dengan penilaian luar talian, kerana ini adalah langkah minimum perlu sebelum melaksanakan mana-mana ejen.

### Penilaian Luar Talian

![Item dataset dalam Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Ini melibatkan menilai ejen dalam suasana terkawal, biasanya menggunakan dataset ujian, bukan pertanyaan pengguna langsung. Anda menggunakan dataset yang dikurasi di mana anda tahu output yang dijangka atau tingkah laku yang betul, dan kemudian menjalankan ejen anda ke atas dataset itu. 

Sebagai contoh, jika anda membina ejen soalan kata matematik, anda mungkin mempunyai [dataset ujian](https://huggingface.co/datasets/gsm8k) dengan 100 masalah yang diketahui jawapannya. Penilaian luar talian sering dilakukan semasa pembangunan (dan boleh menjadi sebahagian daripada pipeline CI/CD) untuk memeriksa penambahbaikan atau mengelakkan kemerosotan. Kelebihannya ialah ia **boleh diulang dan anda boleh mendapatkan metrik ketepatan yang jelas kerana anda mempunyai kebenaran dasar**. Anda juga boleh mensimulasikan pertanyaan pengguna dan mengukur respons ejen terhadap jawapan ideal atau menggunakan metrik automatik seperti yang diterangkan di atas. 

Cabaran utama dengan penilaian luar talian ialah memastikan dataset ujian anda komprehensif dan kekal relevan – ejen mungkin berprestasi baik pada set ujian tetap tetapi menghadapi pertanyaan sangat berbeza dalam pengeluaran. Oleh itu, anda harus mengemas kini set ujian dengan kes sempadan baru dan contoh yang mencerminkan senario dunia sebenar​. Campuran kes “uji asap” kecil dan set penilaian lebih besar berguna: set kecil untuk semakan cepat dan set lebih besar untuk metrik prestasi lebih luas​.

### Penilaian Dalam Talian 

![Gambaran metrik kebolehlihatan](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Ini merujuk kepada penilaian ejen dalam persekitaran langsung, dunia sebenar, iaitu semasa penggunaan sebenar dalam pengeluaran. Penilaian dalam talian melibatkan pemantauan prestasi ejen pada interaksi pengguna sebenar dan menganalisis hasil secara berterusan. 

Contohnya, anda mungkin menjejaki kadar kejayaan, skor kepuasan pengguna, atau metrik lain pada trafik langsung. Kelebihan penilaian dalam talian ialah ia **menangkap perkara yang mungkin tidak anda jangkakan dalam persekitaran makmal** – anda boleh memerhatikan pergeseran model dari masa ke masa (jika keberkesanan ejen merosot kerana corak input berubah) dan menangkap pertanyaan atau situasi tidak dijangka yang tidak ada dalam data ujian​. Ia memberikan gambaran sebenar bagaimana ejen berkelakuan di alam liar. 

Penilaian dalam talian selalunya melibatkan pengumpulan maklum balas pengguna tersirat dan nyata, seperti dibincangkan, dan mungkin menjalankan ujian bayang atau ujian A/B (di mana versi baru ejen dijalankan secara selari untuk dibandingkan dengan yang lama). Cabarannya ialah sukar untuk mendapatkan label atau skor yang boleh dipercayai untuk interaksi langsung – anda mungkin bergantung pada maklum balas pengguna atau metrik hiliran (seperti adakah pengguna mengklik hasil).

### Menggabungkan kedua-duanya

Penilaian dalam talian dan luar talian tidak saling eksklusif; ia sangat saling melengkapi. Pandangan daripada pemantauan dalam talian (contohnya, jenis pertanyaan pengguna baru di mana ejen berprestasi rendah) boleh digunakan untuk menambah dan memperbaiki dataset ujian luar talian. Sebaliknya, ejen yang berprestasi baik dalam ujian luar talian boleh dilaksanakan dengan lebih yakin dan dipantau dalam talian. 

Malahan, banyak pasukan mengamalkan gelung: 

_nilai luar talian -> laksanakan -> pantau dalam talian -> kumpul kes kegagalan baru -> tambah ke dataset luar talian -> haluskan ejen -> ulang_.

## Isu Biasa

Semasa melaksanakan ejen AI ke pengeluaran, anda mungkin menghadapi pelbagai cabaran. Berikut adalah beberapa isu biasa dan penyelesaian berpotensi:

| **Isu**    | **Penyelesaian Berpotensi**   |
| ------------- | ------------------ |
| Ejen AI tidak menjalankan tugas secara konsisten | - Perhalusi arahan yang diberikan kepada Ejen AI; jelaskan objektif.<br>- Kenal pasti jika membahagikan tugas kepada subtugas dan mengendalikannya oleh beberapa ejen boleh membantu. |
| Ejen AI berhadapan dengan gelung berterusan  | - Pastikan anda mempunyai terma dan syarat pemberhentian yang jelas supaya Ejen tahu bila hendak hentikan proses.<br>- Untuk tugas kompleks yang memerlukan penalaran dan perancangan, gunakan model lebih besar yang khusus untuk tugas penalaran. |
| Panggilan alat ejen AI tidak berprestasi baik   | - Uji dan sahkan output alat di luar sistem ejen.<br>- Perhalusi parameter yang ditetapkan, arahan, dan penamaan alat.  |
| Sistem Multi-Ejen tidak berprestasi konsisten | - Perhalusi arahan yang diberikan kepada setiap ejen untuk pastikan ia spesifik dan berbeza antara satu sama lain.<br>- Bina sistem hierarki menggunakan ejen "routing" atau pengawal untuk menentukan ejen yang betul. |

Banyak isu ini boleh dikenal pasti dengan lebih berkesan apabila kebolehlihatan disediakan. Jejak dan metrik yang kita bincangkan sebelum ini membantu mengenal pasti dengan tepat di mana masalah berlaku dalam aliran kerja ejen, menjadikan pembuangan ralat dan pengoptimuman lebih cekap.

## Mengurus Kos


Berikut adalah beberapa strategi untuk menguruskan kos penggunaan ejen AI ke dalam pengeluaran:

**Menggunakan Model yang Lebih Kecil:** Model Bahasa Kecil (SLM) boleh berfungsi dengan baik untuk beberapa kes penggunaan agen dan akan mengurangkan kos dengan ketara. Seperti yang disebutkan sebelum ini, membina sistem penilaian untuk menentukan dan membandingkan prestasi berbanding model yang lebih besar adalah cara terbaik untuk memahami seberapa baik SLM akan berfungsi pada kes penggunaan anda. Pertimbangkan menggunakan SLM untuk tugas yang lebih mudah seperti klasifikasi niat atau pengambilan parameter, sambil menempah model yang lebih besar untuk penalaran kompleks.

**Menggunakan Model Penghala (Router):** Strategi yang serupa adalah menggunakan kepelbagaian model dan saiz. Anda boleh menggunakan LLM/SLM atau fungsi tanpa server untuk menghala permintaan berdasarkan kerumitan ke model yang paling sesuai. Ini juga akan membantu mengurangkan kos sambil memastikan prestasi pada tugas yang betul. Contohnya, menghala pertanyaan mudah ke model yang lebih kecil dan lebih pantas, dan hanya menggunakan model besar yang mahal untuk tugas penalaran yang kompleks.

**Menyimpan Respons dalam Cache:** Mengenal pasti permintaan dan tugas yang biasa serta menyediakan respons sebelum melalui sistem agen anda adalah cara yang baik untuk mengurangkan jumlah permintaan yang serupa. Anda juga boleh melaksanakan aliran untuk mengenal pasti bagaimana serupa sesuatu permintaan dengan permintaan cache anda menggunakan model AI yang lebih asas. Strategi ini boleh mengurangkan kos dengan ketara untuk soalan lazim atau aliran kerja biasa.

## Mari lihat bagaimana ini berfungsi dalam amalan

Dalam [notebook contoh bagi seksyen ini](./code_samples/10-expense_claim-demo.ipynb), kita akan melihat contoh bagaimana kita boleh menggunakan alat pemerhatian untuk memantau dan menilai ejen kita.


### Ada Lebih Banyak Soalan tentang Ejen AI dalam Pengeluaran?

Sertai [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) untuk berjumpa dengan pelajar lain, menghadiri waktu pejabat dan mendapatkan jawapan bagi soalan mengenai Ejen AI anda.

## Pelajaran Sebelumnya

[Corak Reka Bentuk Metakognisi](../09-metacognition/README.md)

## Pelajaran Seterusnya

[Protokol Agen](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->