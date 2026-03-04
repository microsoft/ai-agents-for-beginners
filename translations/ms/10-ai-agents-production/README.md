# Ejen AI dalam Pengeluaran: Kebolehamatan & Penilaian

[![AI Agents in Production](../../../translated_images/ms/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Apabila ejen AI beralih dari prototaip percubaan kepada aplikasi dunia sebenar, kemampuan untuk memahami tingkah laku mereka, memantau prestasi mereka, dan menilai output mereka secara sistematik menjadi penting.

## Matlamat Pembelajaran

Selepas menyelesaikan pelajaran ini, anda akan mengetahui cara untuk/faham:
- Konsep asas kebolehamatan dan penilaian ejen
- Teknik untuk memperbaiki prestasi, kos, dan keberkesanan ejen
- Apa dan bagaimana untuk menilai ejen AI anda secara sistematik
- Cara mengawal kos apabila menyebarkan ejen AI ke dalam pengeluaran
- Cara untuk menginstrumentasikan ejen yang dibina dengan AutoGen

Matlamatnya adalah untuk membekalkan anda dengan pengetahuan untuk mengubah "kotak hitam" ejen anda menjadi sistem yang telus, boleh diurus dan boleh dipercayai.

_**Nota:** Penting untuk menyebarkan Ejen AI yang selamat dan boleh dipercayai. Lihat juga pelajaran [Membina Ejen AI Boleh Dipercayai](../06-building-trustworthy-agents/README.md)._

## Jejak dan Rentang

Alat kebolehamatan seperti [Langfuse](https://langfuse.com/) atau [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) biasanya mewakili larian ejen sebagai jejak dan rentang.

- **Jejak** mewakili tugasan lengkap ejen dari mula hingga selesai (seperti mengendalikan pertanyaan pengguna).
- **Rentang** adalah langkah individu dalam jejak (seperti memanggil model bahasa atau mendapatkan data).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)

Tanpa kebolehamatan, ejen AI boleh dirasakan seperti "kotak hitam" - keadaan dalaman dan penalarannya kabur, menyukarkan untuk mendiagnosis masalah atau mengoptimumkan prestasi. Dengan kebolehamatan, ejen menjadi "kotak kaca," menawarkan ketelusan yang penting untuk membina kepercayaan dan memastikan mereka beroperasi seperti yang diingini.

## Mengapa Kebolehamatan Penting dalam Persekitaran Pengeluaran

Peralihan ejen AI ke persekitaran pengeluaran memperkenalkan satu set cabaran dan keperluan baru. Kebolehamatan bukan lagi "baik untuk dimiliki" tetapi satu kemampuan kritikal:

*   **Penyahpepijatan dan Analisis Punca Akar:** Apabila ejen gagal atau menghasilkan output yang tidak dijangka, alat kebolehamatan menyediakan jejak yang diperlukan untuk mengenal pasti sumber ralat. Ini sangat penting dalam ejen kompleks yang mungkin melibatkan beberapa panggilan LLM, interaksi alat, dan logik bersyarat.
*   **Pengurusan Kelewatan dan Kos:** Ejen AI sering bergantung pada LLM dan API luaran lain yang dikenakan bayaran mengikut token atau panggilan. Kebolehamatan membolehkan penjejakan tepat panggilan ini, membantu mengenal pasti operasi yang terlalu perlahan atau mahal. Ini membolehkan pasukan mengoptimumkan prompt, memilih model yang lebih cekap, atau mereka semula aliran kerja untuk mengurus kos operasi dan memastikan pengalaman pengguna yang baik.
*   **Kepercayaan, Keselamatan, dan Pematuhan:** Dalam banyak aplikasi, penting untuk memastikan ejen berkelakuan selamat dan beretika. Kebolehamatan menyediakan jejak audit tindakan dan keputusan ejen. Ini boleh digunakan untuk mengesan dan mengurangkan isu seperti suntikan prompt, penjanaan kandungan berbahaya, atau pengendalian maklumat peribadi yang tidak betul (PII). Sebagai contoh, anda boleh meneliti jejak untuk memahami mengapa ejen memberikan respons tertentu atau menggunakan alat spesifik.
*   **Gelung Penambahbaikan Berterusan:** Data kebolehamatan adalah asas proses pembangunan iteratif. Dengan memantau prestasi ejen di dunia sebenar, pasukan dapat mengenal pasti bidang untuk penambahbaikan, mengumpul data untuk penyelarasan model, dan mengesahkan kesan perubahan. Ini mewujudkan gelung maklum balas di mana pandangan pengeluaran dari penilaian dalam talian memaklumkan eksperimen dan penambahbaikan luar talian, membawa kepada prestasi ejen yang semakin baik.

## Metrix Utama untuk Jejak

Untuk memantau dan memahami tingkah laku ejen, pelbagai metrik dan isyarat harus dijejak. Walaupun metrik tertentu mungkin berbeza bergantung kepada tujuan ejen, beberapa adalah penting secara umum.

Berikut adalah beberapa metrik paling biasa yang alat kebolehamatan jejak:

**Kelewatan:** Seberapa cepat ejen memberi respons? Masa menunggu yang lama memberi kesan negatif kepada pengalaman pengguna. Anda harus mengukur kelewatan untuk tugasan dan langkah individu dengan menjejaki larian ejen. Sebagai contoh, ejen yang mengambil masa 20 saat untuk semua panggilan model boleh dipercepatkan dengan menggunakan model yang lebih pantas atau menjalankan panggilan model secara selari.

**Kos:** Berapa perbelanjaan setiap larian ejen? Ejen AI bergantung pada panggilan LLM yang dikenakan bayaran per token atau API luaran. Penggunaan alat yang kerap atau pelbagai prompt boleh dengan cepat meningkatkan kos. Contohnya, jika ejen memanggil LLM lima kali untuk peningkatan kualiti marginal, anda mesti menilai sama ada kos itu wajar atau jika anda boleh mengurangkan bilangan panggilan atau menggunakan model yang lebih murah. Pemantauan masa sebenar juga boleh membantu mengenal pasti lonjakan tidak dijangka (contohnya, pepijat yang menyebabkan gelung API berlebihan).

**Ralat Permintaan:** Berapa banyak permintaan yang gagal oleh ejen? Ini boleh termasuk ralat API atau panggilan alat yang gagal. Untuk menjadikan ejen anda lebih tahan terhadap ini dalam pengeluaran, anda boleh menetapkan fallback atau cubaan semula. Contohnya jika pembekal LLM A gagal, anda bertukar kepada pembekal LLM B sebagai sandaran.

**Maklum Balas Pengguna:** Melaksanakan penilaian langsung pengguna memberikan pandangan berharga. Ini boleh termasuk penilaian eksplisit (👍thumbs-up/👎down, ⭐1-5 bintang) atau komen teks. Maklum balas negatif yang konsisten harus memberi amaran kerana ini tanda ejen tidak berfungsi seperti yang dijangka.

**Maklum Balas Implisit Pengguna:** Tingkah laku pengguna memberi maklum balas tidak langsung walaupun tanpa penilaian eksplisit. Ini boleh termasuk memetik soalan semula dengan cepat, pertanyaan berulang atau menekan butang cuba semula. Contohnya jika anda melihat pengguna berulang kali bertanya soalan yang sama, ini adalah tanda ejen tidak berfungsi seperti dijangka.

**Ketepatan:** Berapa kerapkah ejen menghasilkan output yang betul atau diingini? Definisi ketepatan berbeza (contohnya, ketepatan penyelesaian masalah, ketepatan pengambilan maklumat, kepuasan pengguna). Langkah pertama adalah untuk mentakrifkan apa kejayaan untuk ejen anda. Anda boleh menjejak ketepatan melalui pemeriksaan automatik, skor penilaian, atau label penyelesaian tugasan. Sebagai contoh, menanda jejak sebagai "berjaya" atau "gagal".

**Metrix Penilaian Automatik:** Anda juga boleh menyediakan penilaian automatik. Sebagai contoh, anda boleh menggunakan LLM untuk menilai output ejen sama ada ia membantu, tepat, atau tidak. Terdapat juga beberapa perpustakaan sumber terbuka yang membantu anda menilai aspek berbeza ejen. Contohnya, [RAGAS](https://docs.ragas.io/) untuk ejen RAG atau [LLM Guard](https://llm-guard.com/) untuk mengesan bahasa berbahaya atau suntikan prompt.

Dalam praktik, gabungan metrik ini memberikan liputan terbaik untuk kesihatan ejen AI. Dalam [notebook contoh](./code_samples/10_autogen_evaluation.ipynb) bab ini, kami akan menunjukkan bagaimana metrik ini kelihatan dalam contoh sebenar tetapi pertama, kami akan belajar bagaimana aliran kerja penilaian tipikal kelihatan.

## Instrumentasikan Ejen Anda

Untuk mengumpul data jejak, anda perlu menginstrumentasikan kod anda. Matlamatnya adalah untuk menginstrumentasikan kod ejen agar mengeluarkan jejak dan metrik yang boleh ditangkap, diproses, dan divisualisasikan oleh platform kebolehamatan.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) telah muncul sebagai standard industri untuk kebolehamatan LLM. Ia menyediakan set API, SDK, dan alat untuk menjana, mengumpul, dan mengeksport data telemetri.

Terdapat banyak perpustakaan instrumentasi yang membungkus rangka kerja ejen sedia ada dan memudahkan penghantaran rentang OpenTelemetry ke alat kebolehamatan. Berikut adalah contoh menginstrumentasikan ejen AutoGen dengan perpustakaan instrumentasi [OpenLit](https://github.com/openlit/openlit):

```python
import openlit

openlit.init(tracer = langfuse._otel_tracer, disable_batch = True)
```

[notebook contoh](./code_samples/10_autogen_evaluation.ipynb) dalam bab ini akan menunjukkan cara menginstrumentasikan ejen AutoGen anda.

**Penciptaan Rentang Manual:** Walaupun perpustakaan instrumentasi menyediakan asas yang baik, sering terdapat kes di mana maklumat lebih terperinci atau tersuai diperlukan. Anda boleh mencipta rentang secara manual untuk menambah logik aplikasi tersuai. Lebih penting, mereka boleh memperkayakan rentang yang dicipta secara automatik atau manual dengan atribut tersuai (juga dikenali sebagai tag atau metadata). Atribut ini boleh merangkumi data khusus perniagaan, pengiraan pertengahan, atau sebarang konteks yang mungkin berguna untuk penyahpepijatan atau analisis, seperti `user_id`, `session_id`, atau `model_version`.

Contoh mencipta jejak dan rentang secara manual dengan [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Penilaian Ejen

Kebolehamatan memberi kami metrik, tetapi penilaian adalah proses menganalisis data itu (dan melakukan ujian) untuk menentukan sejauh mana prestasi ejen AI dan bagaimana ia boleh diperbaiki. Dengan kata lain, setelah anda mempunyai jejak dan metrik itu, bagaimana anda menggunakannya untuk menilai ejen dan membuat keputusan?

Penilaian berkala penting kerana ejen AI sering tidak deterministik dan boleh berkembang (melalui kemas kini atau perubahan tingkah laku model) – tanpa penilaian, anda tidak akan tahu jika “ejen pintar” anda sebenarnya menjalankan tugas dengan baik atau jika ia merosot.

Terdapat dua kategori penilaian untuk ejen AI: **penilaian dalam talian** dan **penilaian luar talian**. Kedua-duanya bernilai dan saling melengkapi. Biasanya kita mulakan dengan penilaian luar talian, kerana ini adalah langkah minimum perlu sebelum menyebarkan mana-mana ejen.

### Penilaian Luar Talian

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Ini melibatkan menilai ejen dalam persekitaran terkawal, biasanya menggunakan set data ujian, bukan pertanyaan pengguna langsung. Anda menggunakan set data dikurasi di mana anda tahu output yang dijangka atau tingkah laku betul, dan kemudian menjalankan ejen anda ke atasnya.

Sebagai contoh, jika anda membina ejen masalah-matematik perkataan, anda mungkin mempunyai [set data ujian](https://huggingface.co/datasets/gsm8k) 100 soalan dengan jawapan yang diketahui. Penilaian luar talian sering dilakukan semasa pembangunan (dan boleh menjadi sebahagian daripada aliran CI/CD) untuk memeriksa penambahbaikan atau mengelakkan regresi. Kelebihannya ialah ia **boleh diulang dan anda boleh mendapatkan metrik ketepatan yang jelas kerana anda mempunyai asas benar**. Anda juga boleh mensimulasikan pertanyaan pengguna dan mengukur respons ejen terhadap jawapan ideal atau menggunakan metrik automatik seperti yang diterangkan di atas.

Cabaran utama dengan penilaian luar talian adalah memastikan set data ujian anda menyeluruh dan kekal relevan – ejen mungkin berprestasi baik pada set ujian tetap tetapi menghadapi pertanyaan yang sangat berbeza dalam pengeluaran. Oleh itu, anda harus sentiasa mengemas kini set ujian dengan kes tepi dan contoh baru yang mencerminkan senario dunia sebenar​. Gabungan kes "ujian asap" kecil dan set penilaian yang lebih besar adalah berguna: set kecil untuk pemeriksaan pantas dan set besar untuk metrik prestasi yang lebih luas​.

### Penilaian Dalam Talian

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Ini merujuk kepada menilai ejen dalam persekitaran hidup, dunia sebenar, iaitu semasa penggunaan sebenar dalam pengeluaran. Penilaian dalam talian melibatkan pemantauan prestasi ejen pada interaksi pengguna sebenar dan menganalisis hasil secara berterusan.

Sebagai contoh, anda mungkin menjejak kadar kejayaan, skor kepuasan pengguna, atau metrik lain pada trafik langsung. Kelebihan penilaian dalam talian adalah ia **menangkap perkara yang mungkin tidak anda jangka dalam persekitaran makmal** – anda boleh memerhati pergeseran model dari masa ke masa (jika keberkesanan ejen merosot apabila corak input berubah) dan menangkap pertanyaan atau situasi tidak dijangka yang tidak terdapat dalam data ujian anda​. Ia memberikan gambaran sebenar bagaimana ejen berkelakuan di dunia nyata.

Penilaian dalam talian sering melibatkan pengumpulan maklum balas implisit dan eksplisit pengguna, seperti yang dibincangkan, dan mungkin menjalankan ujian bayangan atau ujian A/B (di mana versi baru ejen berjalan secara selari untuk dibandingkan dengan yang lama). Cabarannya ialah agak sukar mendapatkan label atau skor yang boleh dipercayai untuk interaksi langsung – anda mungkin bergantung kepada maklum balas pengguna atau metrik hiliran (seperti sama ada pengguna mengklik hasil).

### Menggabungkan Kedua-duanya

Penilaian dalam talian dan luar talian tidak saling eksklusif; ia sangat melengkapi antara satu sama lain. Pandangan daripada pemantauan dalam talian (contohnya, jenis pertanyaan pengguna baru di mana ejen berprestasi buruk) boleh digunakan untuk menambah baik set data ujian luar talian. Sebaliknya, ejen yang berprestasi baik dalam ujian luar talian boleh disebarkan dengan lebih yakin dan dipantau dalam talian.

Malahan, banyak pasukan menggunakan gelung:

_menilai luar talian -> sebarkan -> pantau dalam talian -> kumpul kes kegagalan baru -> tambah ke set data luar talian -> haluskan ejen -> ulang_.

## Isu Biasa

Apabila anda menyebarkan ejen AI ke pengeluaran, anda mungkin menghadapi pelbagai cabaran. Berikut adalah beberapa isu biasa dan penyelesaian potensinya:

| **Isu**    | **Penyelesaian Potensial**   |
| ------------- | ------------------ |
| Ejen AI tidak menjalankan tugasan dengan konsisten | - Perhalusi prompt yang diberikan kepada Ejen AI; jelaskan objektif.<br>- Kenal pasti di mana membahagikan tugasan kepada subtugasan dan mengendalikannya oleh pelbagai ejen boleh membantu. |
| Ejen AI masuk ke dalam gelung berterusan  | - Pastikan anda ada terma dan syarat penamatan yang jelas supaya Ejen tahu bila untuk menghentikan proses.<br>- Untuk tugasan kompleks yang memerlukan penalaran dan perancangan, gunakan model yang lebih besar yang khusus untuk tugasan penalaran. |
| Panggilan alat Ejen AI tidak berprestasi baik   | - Uji dan sahkan output alat di luar sistem ejen.<br>- Perhalusi parameter, prompt, dan penamaan alat yang ditentukan.  |
| Sistem Multi-Ejen tidak berprestasi konsisten | - Perhalusi prompt yang diberikan kepada setiap ejen untuk memastikan ia spesifik dan berbeza antara satu sama lain.<br>- Bina sistem hierarki menggunakan ejen "penghalaan" atau pengawal untuk menentukan ejen yang betul. |

Banyak isu ini boleh dikenalpasti dengan lebih berkesan dengan kebolehamatan tersedia. Jejak dan metrik yang dibincangkan sebelum ini membantu mengenal pasti dengan tepat di mana dalam aliran kerja ejen masalah berlaku, menjadikan penyahpepijatan dan pengoptimuman lebih cekap.

## Menguruskan Kos
Berikut adalah beberapa strategi untuk menguruskan kos penyebaran agen AI ke dalam pengeluaran:

**Menggunakan Model Lebih Kecil:** Model Bahasa Kecil (SLM) boleh berprestasi baik pada beberapa kes penggunaan agen dan akan mengurangkan kos dengan ketara. Seperti yang disebutkan sebelum ini, membina sistem penilaian untuk menentukan dan membandingkan prestasi berbanding model yang lebih besar adalah cara terbaik untuk memahami berapa baik SLM akan berfungsi pada kes penggunaan anda. Pertimbangkan menggunakan SLM untuk tugas yang lebih mudah seperti klasifikasi niat atau pengekstrakan parameter, manakala menyimpan model yang lebih besar untuk pemikiran kompleks.

**Menggunakan Model Penentu Laluan:** Strategi yang serupa adalah menggunakan kepelbagaian model dan saiz. Anda boleh menggunakan LLM/SLM atau fungsi tanpa pelayan untuk menetapkan laluan permintaan berdasarkan kerumitan kepada model yang paling sesuai. Ini juga akan membantu mengurangkan kos sambil memastikan prestasi pada tugas yang betul. Contohnya, lalukan pertanyaan mudah kepada model yang lebih kecil dan lebih pantas, dan hanya gunakan model besar yang mahal untuk tugas pemikiran kompleks.

**Menyimpan Cache Tindak Balas:** Mengenal pasti permintaan dan tugas yang biasa serta menyediakan tindak balas sebelum ia masuk ke dalam sistem agen anda adalah cara yang baik untuk mengurangkan jumlah permintaan serupa. Anda juga boleh melaksanakan aliran untuk mengenal pasti seberapa serupa permintaan dengan permintaan yang telah disimpan dalam cache menggunakan model AI yang lebih asas. Strategi ini boleh mengurangkan kos dengan ketara untuk soalan yang kerap ditanya atau aliran kerja biasa.

## Mari kita lihat bagaimana ini berfungsi dalam praktik

Dalam [notebook contoh bahagian ini](./code_samples/10_autogen_evaluation.ipynb), kita akan melihat contoh bagaimana kita boleh menggunakan alat kebolehlihatan untuk memantau dan menilai agen kita.


### Ada Lebih Banyak Soalan tentang Agen AI dalam Pengeluaran?

Sertai [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) untuk berjumpa dengan pelajar lain, menghadiri waktu pejabat dan mendapatkan jawapan untuk soalan Agen AI anda.

## Pelajaran Sebelumnya

[Corak Reka Bentuk Metakognisi](../09-metacognition/README.md)

## Pelajaran Seterusnya

[Protokol Agenik](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidakakuratan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat yang kritikal, terjemahan profesional oleh manusia adalah disarankan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau tafsiran yang salah yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->