<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "cdfd0acc8592c1af14f8637833450375",
  "translation_date": "2025-08-29T18:15:03+00:00",
  "source_file": "10-ai-agents-production/README.md",
  "language_code": "ms"
}
-->
# Ejen AI dalam Pengeluaran: Pemerhatian & Penilaian

[![Ejen AI dalam Pengeluaran](../../../translated_images/lesson-10-thumbnail.2b79a30773db093e0b4fb47aaa618069e0afb4745fad4836526cf51df87f9ac9.ms.png)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Apabila ejen AI beralih daripada prototaip eksperimen kepada aplikasi dunia sebenar, keupayaan untuk memahami tingkah laku mereka, memantau prestasi mereka, dan menilai output mereka secara sistematik menjadi penting.

## Matlamat Pembelajaran

Selepas menyelesaikan pelajaran ini, anda akan tahu cara/memahami:
- Konsep utama pemerhatian dan penilaian ejen
- Teknik untuk meningkatkan prestasi, kos, dan keberkesanan ejen
- Apa dan bagaimana untuk menilai ejen AI anda secara sistematik
- Cara mengawal kos apabila melancarkan ejen AI ke pengeluaran
- Cara melengkapkan ejen yang dibina dengan AutoGen

Matlamatnya adalah untuk melengkapkan anda dengan pengetahuan untuk mengubah ejen "kotak hitam" anda menjadi sistem yang telus, boleh diurus, dan boleh dipercayai.

_**Nota:** Adalah penting untuk melancarkan Ejen AI yang selamat dan boleh dipercayai. Lihat pelajaran [Membina Ejen AI yang Boleh Dipercayai](./06-building-trustworthy-agents/README.md) juga._

## Jejak dan Span

Alat pemerhatian seperti [Langfuse](https://langfuse.com/) atau [Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) biasanya mewakili larian ejen sebagai jejak dan span.

- **Jejak** mewakili tugas ejen lengkap dari awal hingga akhir (seperti menangani pertanyaan pengguna).
- **Span** adalah langkah individu dalam jejak (seperti memanggil model bahasa atau mendapatkan data).

![Pokok Jejak dalam Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)

Tanpa pemerhatian, ejen AI boleh terasa seperti "kotak hitam" - keadaan dalaman dan penalarannya tidak jelas, menjadikannya sukar untuk mendiagnosis masalah atau mengoptimumkan prestasi. Dengan pemerhatian, ejen menjadi "kotak kaca," menawarkan ketelusan yang penting untuk membina kepercayaan dan memastikan mereka beroperasi seperti yang diinginkan.

## Mengapa Pemerhatian Penting dalam Persekitaran Pengeluaran

Peralihan ejen AI ke persekitaran pengeluaran memperkenalkan satu set cabaran dan keperluan baharu. Pemerhatian bukan lagi sesuatu yang "baik untuk dimiliki" tetapi keupayaan yang kritikal:

*   **Penyahpepijatan dan Analisis Punca Masalah**: Apabila ejen gagal atau menghasilkan output yang tidak dijangka, alat pemerhatian menyediakan jejak yang diperlukan untuk mengenal pasti punca kesilapan. Ini amat penting dalam ejen yang kompleks yang mungkin melibatkan pelbagai panggilan LLM, interaksi alat, dan logik bersyarat.
*   **Pengurusan Kependaman dan Kos**: Ejen AI sering bergantung pada LLM dan API luaran lain yang dikenakan bayaran per token atau per panggilan. Pemerhatian membolehkan penjejakan tepat panggilan ini, membantu mengenal pasti operasi yang terlalu perlahan atau mahal. Ini membolehkan pasukan mengoptimumkan arahan, memilih model yang lebih cekap, atau mereka bentuk semula aliran kerja untuk mengurus kos operasi dan memastikan pengalaman pengguna yang baik.
*   **Kepercayaan, Keselamatan, dan Pematuhan**: Dalam banyak aplikasi, adalah penting untuk memastikan ejen berkelakuan dengan selamat dan beretika. Pemerhatian menyediakan jejak audit tindakan dan keputusan ejen. Ini boleh digunakan untuk mengesan dan mengurangkan isu seperti suntikan arahan, penjanaan kandungan berbahaya, atau pengendalian maklumat peribadi yang boleh dikenal pasti (PII) secara tidak betul. Sebagai contoh, anda boleh menyemak jejak untuk memahami mengapa ejen memberikan respons tertentu atau menggunakan alat tertentu.
*   **Gelung Penambahbaikan Berterusan**: Data pemerhatian adalah asas kepada proses pembangunan berulang. Dengan memantau bagaimana ejen berprestasi di dunia sebenar, pasukan boleh mengenal pasti kawasan untuk penambahbaikan, mengumpul data untuk penalaan model, dan mengesahkan kesan perubahan. Ini mencipta gelung maklum balas di mana pandangan pengeluaran daripada penilaian dalam talian memaklumkan eksperimen luar talian dan penapisan, membawa kepada prestasi ejen yang semakin baik.

## Metrik Utama untuk Dipantau

Untuk memantau dan memahami tingkah laku ejen, pelbagai metrik dan isyarat harus dipantau. Walaupun metrik tertentu mungkin berbeza berdasarkan tujuan ejen, beberapa adalah penting secara universal.

Berikut adalah beberapa metrik paling biasa yang dipantau oleh alat pemerhatian:

**Kependaman:** Seberapa cepat ejen memberikan respons? Masa menunggu yang lama memberi kesan negatif kepada pengalaman pengguna. Anda harus mengukur kependaman untuk tugas dan langkah individu dengan menjejaki larian ejen. Sebagai contoh, ejen yang mengambil masa 20 saat untuk semua panggilan model boleh dipercepatkan dengan menggunakan model yang lebih pantas atau dengan menjalankan panggilan model secara selari.

**Kos:** Berapakah kos setiap larian ejen? Ejen AI bergantung pada panggilan LLM yang dikenakan bayaran per token atau API luaran. Penggunaan alat yang kerap atau arahan berganda boleh meningkatkan kos dengan cepat. Sebagai contoh, jika ejen memanggil LLM lima kali untuk peningkatan kualiti yang marginal, anda mesti menilai sama ada kos itu wajar atau jika anda boleh mengurangkan bilangan panggilan atau menggunakan model yang lebih murah. Pemantauan masa nyata juga boleh membantu mengenal pasti lonjakan yang tidak dijangka (contohnya, pepijat yang menyebabkan gelung API berlebihan).

**Kesilapan Permintaan:** Berapa banyak permintaan yang gagal oleh ejen? Ini boleh termasuk kesilapan API atau panggilan alat yang gagal. Untuk menjadikan ejen anda lebih teguh terhadap ini dalam pengeluaran, anda boleh menyediakan sandaran atau percubaan semula. Contohnya, jika penyedia LLM A tidak berfungsi, anda beralih kepada penyedia LLM B sebagai sandaran.

**Maklum Balas Pengguna:** Melaksanakan penilaian langsung oleh pengguna memberikan pandangan yang berharga. Ini boleh termasuk penilaian eksplisit (👍thumbs-up/👎down, ⭐1-5 bintang) atau komen teks. Maklum balas negatif yang konsisten harus memberi amaran kepada anda kerana ini adalah tanda bahawa ejen tidak berfungsi seperti yang diharapkan.

**Maklum Balas Pengguna Tersirat:** Tingkah laku pengguna memberikan maklum balas tidak langsung walaupun tanpa penilaian eksplisit. Ini boleh termasuk penulisan semula soalan segera, pertanyaan berulang atau klik butang percubaan semula. Contohnya, jika anda melihat pengguna berulang kali bertanya soalan yang sama, ini adalah tanda bahawa ejen tidak berfungsi seperti yang diharapkan.

**Ketepatan:** Seberapa kerap ejen menghasilkan output yang betul atau diinginkan? Definisi ketepatan berbeza-beza (contohnya, ketepatan penyelesaian masalah, ketepatan pengambilan maklumat, kepuasan pengguna). Langkah pertama adalah untuk menentukan apa yang kelihatan seperti kejayaan untuk ejen anda. Anda boleh menjejaki ketepatan melalui pemeriksaan automatik, skor penilaian, atau label penyelesaian tugas. Sebagai contoh, menandakan jejak sebagai "berjaya" atau "gagal".

**Metrik Penilaian Automatik:** Anda juga boleh menyediakan penilaian automatik. Sebagai contoh, anda boleh menggunakan LLM untuk menilai output ejen contohnya sama ada ia berguna, tepat, atau tidak. Terdapat juga beberapa perpustakaan sumber terbuka yang membantu anda menilai aspek yang berbeza dari ejen. Contohnya, [RAGAS](https://docs.ragas.io/) untuk ejen RAG atau [LLM Guard](https://llm-guard.com/) untuk mengesan bahasa berbahaya atau suntikan arahan.

Dalam amalan, gabungan metrik ini memberikan liputan terbaik tentang kesihatan ejen AI. Dalam [notebook contoh](./code_samples/10_autogen_evaluation.ipynb) bab ini, kami akan menunjukkan kepada anda bagaimana metrik ini kelihatan dalam contoh sebenar tetapi pertama, kami akan belajar bagaimana aliran kerja penilaian biasa kelihatan.

## Lengkapkan Ejen Anda

Untuk mengumpulkan data jejak, anda perlu melengkapkan kod anda. Matlamatnya adalah untuk melengkapkan kod ejen untuk mengeluarkan jejak dan metrik yang boleh ditangkap, diproses, dan divisualisasikan oleh platform pemerhatian.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) telah muncul sebagai standard industri untuk pemerhatian LLM. Ia menyediakan satu set API, SDK, dan alat untuk menjana, mengumpulkan, dan mengeksport data telemetri.

Terdapat banyak perpustakaan instrumentasi yang membungkus rangka kerja ejen sedia ada dan memudahkan eksport span OpenTelemetry ke alat pemerhatian. Di bawah adalah contoh melengkapkan ejen AutoGen dengan perpustakaan instrumentasi [OpenLit](https://github.com/openlit/openlit):

```python
import openlit

openlit.init(tracer = langfuse._otel_tracer, disable_batch = True)
```

[Notebook contoh](./code_samples/10_autogen_evaluation.ipynb) dalam bab ini akan menunjukkan cara melengkapkan ejen AutoGen anda.

**Penciptaan Span Manual:** Walaupun perpustakaan instrumentasi menyediakan asas yang baik, terdapat kes di mana maklumat yang lebih terperinci atau tersuai diperlukan. Anda boleh mencipta span secara manual untuk menambah logik aplikasi tersuai. Lebih penting lagi, mereka boleh memperkayakan span yang dibuat secara automatik atau manual dengan atribut tersuai (juga dikenali sebagai tag atau metadata). Atribut ini boleh termasuk data khusus perniagaan, pengiraan perantaraan, atau sebarang konteks yang mungkin berguna untuk penyahpepijatan atau analisis, seperti `user_id`, `session_id`, atau `model_version`.

Contoh mencipta jejak dan span secara manual dengan [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Penilaian Ejen

Pemerhatian memberikan kita metrik, tetapi penilaian adalah proses menganalisis data tersebut (dan menjalankan ujian) untuk menentukan sejauh mana prestasi ejen AI dan bagaimana ia boleh diperbaiki. Dalam erti kata lain, setelah anda mempunyai jejak dan metrik tersebut, bagaimana anda menggunakannya untuk menilai ejen dan membuat keputusan?

Penilaian secara berkala adalah penting kerana ejen AI sering tidak deterministik dan boleh berkembang (melalui kemas kini atau perubahan tingkah laku model) – tanpa penilaian, anda tidak akan tahu sama ada "ejen pintar" anda benar-benar melakukan tugasnya dengan baik atau jika ia telah merosot.

Terdapat dua kategori penilaian untuk ejen AI: **penilaian luar talian** dan **penilaian dalam talian**. Kedua-duanya bernilai, dan mereka saling melengkapi. Kami biasanya bermula dengan penilaian luar talian, kerana ini adalah langkah minimum yang diperlukan sebelum melancarkan mana-mana ejen.

### Penilaian Luar Talian

![Item Dataset dalam Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Ini melibatkan penilaian ejen dalam persekitaran terkawal, biasanya menggunakan dataset ujian, bukan pertanyaan pengguna langsung. Anda menggunakan dataset yang dikurasi di mana anda tahu apa output yang diharapkan atau tingkah laku yang betul, dan kemudian menjalankan ejen anda pada dataset tersebut.

Sebagai contoh, jika anda membina ejen masalah perkataan matematik, anda mungkin mempunyai [dataset ujian](https://huggingface.co/datasets/gsm8k) sebanyak 100 masalah dengan jawapan yang diketahui. Penilaian luar talian sering dilakukan semasa pembangunan (dan boleh menjadi sebahagian daripada saluran CI/CD) untuk memeriksa penambahbaikan atau melindungi daripada kemerosotan. Kelebihannya ialah ia **boleh diulang dan anda boleh mendapatkan metrik ketepatan yang jelas kerana anda mempunyai kebenaran asas**. Anda juga mungkin mensimulasikan pertanyaan pengguna dan mengukur respons ejen terhadap jawapan ideal atau menggunakan metrik automatik seperti yang diterangkan di atas.

Cabaran utama dengan penilaian luar talian adalah memastikan dataset ujian anda komprehensif dan kekal relevan – ejen mungkin berprestasi baik pada set ujian tetap tetapi menghadapi pertanyaan yang sangat berbeza dalam pengeluaran. Oleh itu, anda harus memastikan set ujian dikemas kini dengan kes tepi baharu dan contoh yang mencerminkan senario dunia sebenar​. Campuran kes "ujian asap" kecil dan set penilaian yang lebih besar adalah berguna: set kecil untuk pemeriksaan pantas dan yang lebih besar untuk metrik prestasi yang lebih luas​.

### Penilaian Dalam Talian

![Gambaran Keseluruhan Metrik Pemerhatian](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Ini merujuk kepada penilaian ejen dalam persekitaran langsung, dunia sebenar, iaitu semasa penggunaan sebenar dalam pengeluaran. Penilaian dalam talian melibatkan pemantauan prestasi ejen pada interaksi pengguna sebenar dan menganalisis hasil secara berterusan.

Sebagai contoh, anda mungkin menjejaki kadar kejayaan, skor kepuasan pengguna, atau metrik lain pada trafik langsung. Kelebihan penilaian dalam talian ialah ia **menangkap perkara yang mungkin tidak anda jangkakan dalam persekitaran makmal** – anda boleh memerhatikan perubahan model dari masa ke masa (jika keberkesanan ejen merosot apabila corak input berubah) dan menangkap pertanyaan atau situasi yang tidak dijangka yang tidak terdapat dalam data ujian anda​. Ia memberikan gambaran sebenar tentang bagaimana ejen berkelakuan di dunia sebenar.

Penilaian dalam talian sering melibatkan pengumpulan maklum balas pengguna tersirat dan eksplisit, seperti yang dibincangkan, dan mungkin menjalankan ujian bayangan atau ujian A/B (di mana versi baharu ejen berjalan selari untuk dibandingkan dengan yang lama). Cabarannya ialah ia boleh menjadi sukar untuk mendapatkan label atau skor yang boleh dipercayai untuk interaksi langsung – anda mungkin bergantung pada maklum balas pengguna atau metrik hiliran (seperti adakah pengguna mengklik hasilnya).

### Menggabungkan Kedua-duanya

Penilaian dalam talian dan luar talian tidak saling eksklusif; mereka sangat saling melengkapi. Pandangan daripada pemantauan dalam talian (contohnya, jenis pertanyaan pengguna baharu di mana ejen berprestasi buruk) boleh digunakan untuk menambah dan meningkatkan dataset ujian luar talian. Sebaliknya, ejen yang berprestasi baik dalam ujian luar talian boleh dilancarkan dengan lebih yakin dan dipantau dalam talian.

Malah, banyak pasukan mengamalkan gelung:

_penilaian luar talian -> pelancaran -> pemantauan dalam talian -> pengumpulan kes kegagalan baharu -> tambah pada dataset luar talian -> penapisan ejen -> ulang_.

## Isu Biasa

Apabila anda melancarkan ejen AI ke pengeluaran, anda mungkin menghadapi pelbagai cabaran. Berikut adalah beberapa isu biasa dan penyelesaian berpotensi mereka:

| **Isu**    | **Penyelesaian Berpotensi**   |
| ------------- | ------------------ |
| Ejen AI tidak melaksanakan tugas secara konsisten | - Perbaiki arahan yang diberikan kepada Ejen AI; jelaskan objektif.<br>- Kenal pasti di mana membahagikan tugas kepada subtugas dan mengendalikannya oleh pelbagai ejen boleh membantu. |
| Ejen AI terperangkap dalam gelung berterusan  | - Pastikan anda mempunyai syarat dan terma penamatan yang jelas supaya Ejen tahu bila untuk menghentikan proses. |

## Memahami Masalah Biasa

Berikut adalah beberapa masalah biasa yang mungkin anda hadapi semasa menggunakan AI agents, bersama dengan cadangan penyelesaian:

| **Masalah**                                | **Cadangan Penyelesaian**                                                                                                                                                                                                                     |
|--------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Model AI tidak memberikan jawapan yang betul | - Semak semula data latihan untuk memastikan ia relevan dan berkualiti tinggi.<br>- Perbaiki prompt untuk memberikan arahan yang lebih jelas kepada model.<br>- Gunakan model yang lebih besar untuk tugas yang memerlukan penalaran kompleks. |
| Panggilan alat AI Agent tidak berfungsi dengan baik | - Uji dan sahkan output alat di luar sistem agent.<br>- Perbaiki parameter yang ditetapkan, prompt, dan penamaan alat.                                                                                                                         |
| Sistem Multi-Agent tidak konsisten          | - Perbaiki prompt yang diberikan kepada setiap agent untuk memastikan ia spesifik dan berbeza antara satu sama lain.<br>- Bina sistem hierarki menggunakan agent "routing" atau pengawal untuk menentukan agent yang sesuai.                     |

Banyak masalah ini boleh dikenal pasti dengan lebih berkesan jika terdapat kebolehlihatan (observability). Jejak dan metrik yang kita bincangkan sebelum ini membantu mengenal pasti dengan tepat di mana masalah berlaku dalam aliran kerja agent, menjadikan proses debugging dan pengoptimuman lebih efisien.

## Mengurus Kos

Berikut adalah beberapa strategi untuk mengurus kos semasa menggunakan AI agents dalam pengeluaran:

**Menggunakan Model yang Lebih Kecil:** Small Language Models (SLMs) boleh berfungsi dengan baik untuk beberapa kes penggunaan agentik dan dapat mengurangkan kos dengan ketara. Seperti yang disebutkan sebelum ini, membina sistem penilaian untuk menentukan dan membandingkan prestasi berbanding model yang lebih besar adalah cara terbaik untuk memahami sejauh mana SLM dapat berfungsi untuk kes penggunaan anda. Pertimbangkan untuk menggunakan SLM untuk tugas yang lebih mudah seperti klasifikasi niat atau pengekstrakan parameter, dan simpan model yang lebih besar untuk penalaran kompleks.

**Menggunakan Model Router:** Strategi serupa adalah dengan menggunakan pelbagai model dan saiz. Anda boleh menggunakan LLM/SLM atau fungsi tanpa pelayan untuk mengarahkan permintaan berdasarkan tahap kerumitan kepada model yang paling sesuai. Ini juga akan membantu mengurangkan kos sambil memastikan prestasi untuk tugas yang betul. Sebagai contoh, arahkan pertanyaan mudah kepada model yang lebih kecil dan pantas, dan hanya gunakan model besar yang mahal untuk tugas penalaran kompleks.

**Caching Respons:** Mengenal pasti permintaan dan tugas yang biasa serta menyediakan respons sebelum ia melalui sistem agentik anda adalah cara yang baik untuk mengurangkan jumlah permintaan serupa. Anda juga boleh melaksanakan aliran untuk mengenal pasti sejauh mana permintaan serupa dengan permintaan yang telah dicache menggunakan model AI yang lebih asas. Strategi ini dapat mengurangkan kos dengan ketara untuk soalan yang sering ditanya atau aliran kerja biasa.

## Mari Lihat Bagaimana Ini Berfungsi dalam Praktik

Dalam [notebook contoh bahagian ini](./code_samples/10_autogen_evaluation.ipynb), kita akan melihat contoh bagaimana kita boleh menggunakan alat observability untuk memantau dan menilai agent kita.

### Ada Lagi Soalan tentang AI Agents dalam Pengeluaran?

Sertai [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) untuk berhubung dengan pelajar lain, menghadiri sesi soal jawab, dan mendapatkan jawapan kepada soalan anda tentang AI Agents.

## Pelajaran Sebelumnya

[Corak Reka Bentuk Metakognisi](../09-metacognition/README.md)

## Pelajaran Seterusnya

[Protokol Agentik](../11-agentic-protocols/README.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.