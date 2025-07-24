<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8164484c16b1ed3287ef9dae9fc437c1",
  "translation_date": "2025-07-24T08:47:35+00:00",
  "source_file": "10-ai-agents-production/README.md",
  "language_code": "ms"
}
-->
# Ejen AI dalam Pengeluaran: Pemerhatian & Penilaian

Apabila ejen AI beralih daripada prototaip eksperimen kepada aplikasi dunia sebenar, keupayaan untuk memahami tingkah laku mereka, memantau prestasi mereka, dan menilai output mereka secara sistematik menjadi penting.

## Matlamat Pembelajaran

Selepas menyelesaikan pelajaran ini, anda akan tahu bagaimana untuk/memahami:
- Konsep asas pemerhatian dan penilaian ejen
- Teknik untuk meningkatkan prestasi, kos, dan keberkesanan ejen
- Apa dan bagaimana untuk menilai ejen AI anda secara sistematik
- Cara mengawal kos semasa menggunakan ejen AI dalam pengeluaran
- Cara menginstrumentasikan ejen yang dibina dengan AutoGen

Matlamatnya adalah untuk melengkapkan anda dengan pengetahuan untuk mengubah ejen "kotak hitam" anda menjadi sistem yang telus, boleh diurus, dan boleh dipercayai.

_**Nota:** Adalah penting untuk menggunakan Ejen AI yang selamat dan boleh dipercayai. Lihat pelajaran [Membina Ejen AI yang Boleh Dipercayai](./06-building-trustworthy-agents/README.md) juga._

## Jejak dan Span

Alat pemerhatian seperti [Langfuse](https://langfuse.com/) atau [Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) biasanya mewakili operasi ejen sebagai jejak dan span.

- **Jejak** mewakili tugas ejen lengkap dari awal hingga akhir (seperti menangani pertanyaan pengguna).
- **Span** adalah langkah individu dalam jejak (seperti memanggil model bahasa atau mendapatkan data).

![Pokok Jejak dalam Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)

Tanpa pemerhatian, ejen AI boleh terasa seperti "kotak hitam" - keadaan dalaman dan penaakulan mereka tidak jelas, menjadikannya sukar untuk mendiagnosis masalah atau mengoptimumkan prestasi. Dengan pemerhatian, ejen menjadi "kotak kaca," menawarkan ketelusan yang penting untuk membina kepercayaan dan memastikan mereka beroperasi seperti yang diinginkan.

## Mengapa Pemerhatian Penting dalam Persekitaran Pengeluaran

Peralihan ejen AI ke persekitaran pengeluaran memperkenalkan set cabaran dan keperluan baru. Pemerhatian bukan lagi sekadar "bagus untuk ada" tetapi keupayaan yang kritikal:

*   **Penyahpepijatan dan Analisis Punca Masalah**: Apabila ejen gagal atau menghasilkan output yang tidak dijangka, alat pemerhatian menyediakan jejak yang diperlukan untuk mengenal pasti punca masalah. Ini sangat penting dalam ejen kompleks yang mungkin melibatkan banyak panggilan LLM, interaksi alat, dan logik bersyarat.
*   **Pengurusan Kelewatan dan Kos**: Ejen AI sering bergantung pada LLM dan API luaran lain yang dikenakan bayaran per token atau per panggilan. Pemerhatian membolehkan penjejakan tepat terhadap panggilan ini, membantu mengenal pasti operasi yang terlalu lambat atau mahal. Ini membolehkan pasukan mengoptimumkan arahan, memilih model yang lebih cekap, atau mereka bentuk semula aliran kerja untuk mengurus kos operasi dan memastikan pengalaman pengguna yang baik.
*   **Kepercayaan, Keselamatan, dan Pematuhan**: Dalam banyak aplikasi, adalah penting untuk memastikan ejen berkelakuan dengan selamat dan beretika. Pemerhatian menyediakan jejak audit tindakan dan keputusan ejen. Ini boleh digunakan untuk mengesan dan mengurangkan isu seperti suntikan arahan, penghasilan kandungan berbahaya, atau pengendalian maklumat peribadi yang salah (PII). Sebagai contoh, anda boleh menyemak jejak untuk memahami mengapa ejen memberikan respons tertentu atau menggunakan alat tertentu.
*   **Gelung Penambahbaikan Berterusan**: Data pemerhatian adalah asas kepada proses pembangunan iteratif. Dengan memantau bagaimana ejen berprestasi di dunia sebenar, pasukan boleh mengenal pasti kawasan untuk penambahbaikan, mengumpul data untuk penalaan model, dan mengesahkan kesan perubahan. Ini mencipta gelung maklum balas di mana pandangan pengeluaran daripada penilaian dalam talian memaklumkan eksperimen luar talian dan penambahbaikan, membawa kepada prestasi ejen yang semakin baik.

## Metrik Utama untuk Dipantau

Untuk memantau dan memahami tingkah laku ejen, pelbagai metrik dan isyarat perlu dipantau. Walaupun metrik tertentu mungkin berbeza berdasarkan tujuan ejen, beberapa metrik adalah penting secara universal.

Berikut adalah beberapa metrik paling biasa yang dipantau oleh alat pemerhatian:

**Kelewatan:** Seberapa cepat ejen memberikan respons? Masa menunggu yang lama memberi kesan negatif kepada pengalaman pengguna. Anda harus mengukur kelewatan untuk tugas dan langkah individu dengan menjejaki operasi ejen. Sebagai contoh, ejen yang mengambil masa 20 saat untuk semua panggilan model boleh dipercepatkan dengan menggunakan model yang lebih pantas atau menjalankan panggilan model secara selari.

**Kos:** Berapakah kos per operasi ejen? Ejen AI bergantung pada panggilan LLM yang dikenakan bayaran per token atau API luaran. Penggunaan alat yang kerap atau arahan berganda boleh meningkatkan kos dengan cepat. Sebagai contoh, jika ejen memanggil LLM lima kali untuk peningkatan kualiti yang marginal, anda perlu menilai sama ada kos itu berbaloi atau jika anda boleh mengurangkan bilangan panggilan atau menggunakan model yang lebih murah. Pemantauan masa nyata juga boleh membantu mengenal pasti lonjakan yang tidak dijangka (contohnya, pepijat yang menyebabkan gelung API berlebihan).

**Ralat Permintaan:** Berapa banyak permintaan yang gagal dilakukan oleh ejen? Ini boleh termasuk ralat API atau kegagalan panggilan alat. Untuk menjadikan ejen anda lebih tahan terhadap masalah ini dalam pengeluaran, anda boleh menyediakan mekanisme sandaran atau percubaan semula. Contohnya, jika penyedia LLM A tidak berfungsi, anda beralih kepada penyedia LLM B sebagai sandaran.

**Maklum Balas Pengguna:** Melaksanakan penilaian langsung daripada pengguna memberikan pandangan yang berharga. Ini boleh termasuk penilaian eksplisit (👍thumbs-up/👎down, ⭐1-5 bintang) atau komen teks. Maklum balas negatif yang konsisten harus memberi amaran kepada anda kerana ini adalah tanda bahawa ejen tidak berfungsi seperti yang diharapkan.

**Maklum Balas Pengguna Tidak Langsung:** Tingkah laku pengguna memberikan maklum balas tidak langsung walaupun tanpa penilaian eksplisit. Ini boleh termasuk pengulangan soalan segera, pertanyaan berulang, atau menekan butang cuba semula. Contohnya, jika anda melihat pengguna berulang kali bertanya soalan yang sama, ini adalah tanda bahawa ejen tidak berfungsi seperti yang diharapkan.

**Ketepatan:** Seberapa kerap ejen menghasilkan output yang betul atau diingini? Definisi ketepatan berbeza-beza (contohnya, ketepatan penyelesaian masalah, ketepatan pengambilan maklumat, kepuasan pengguna). Langkah pertama adalah untuk menentukan apa yang kelihatan seperti kejayaan untuk ejen anda. Anda boleh menjejaki ketepatan melalui pemeriksaan automatik, skor penilaian, atau label penyelesaian tugas. Sebagai contoh, menandakan jejak sebagai "berjaya" atau "gagal".

**Metrik Penilaian Automatik:** Anda juga boleh menyediakan penilaian automatik. Sebagai contoh, anda boleh menggunakan LLM untuk menilai output ejen, contohnya sama ada ia berguna, tepat, atau tidak. Terdapat juga beberapa perpustakaan sumber terbuka yang membantu anda menilai aspek berbeza ejen. Contohnya, [RAGAS](https://docs.ragas.io/) untuk ejen RAG atau [LLM Guard](https://llm-guard.com/) untuk mengesan bahasa berbahaya atau suntikan arahan.

Dalam praktiknya, gabungan metrik ini memberikan liputan terbaik terhadap kesihatan ejen AI. Dalam [notebook contoh](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb) bab ini, kami akan menunjukkan bagaimana metrik ini kelihatan dalam contoh sebenar tetapi pertama, kami akan belajar bagaimana aliran kerja penilaian tipikal kelihatan.

## Instrumentasikan Ejen Anda

Untuk mengumpul data jejak, anda perlu menginstrumentasikan kod anda. Matlamatnya adalah untuk menginstrumentasikan kod ejen supaya menghasilkan jejak dan metrik yang boleh ditangkap, diproses, dan divisualisasikan oleh platform pemerhatian.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) telah muncul sebagai standard industri untuk pemerhatian LLM. Ia menyediakan satu set API, SDK, dan alat untuk menjana, mengumpul, dan mengeksport data telemetri.

Terdapat banyak perpustakaan instrumentasi yang membungkus rangka kerja ejen sedia ada dan memudahkan eksport span OpenTelemetry ke alat pemerhatian. Berikut adalah contoh instrumentasi ejen AutoGen dengan perpustakaan instrumentasi [OpenLit](https://github.com/openlit/openlit):

```python
import openlit

openlit.init(tracer = langfuse._otel_tracer, disable_batch = True)
```

[Notebook contoh](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb) dalam bab ini akan menunjukkan cara untuk menginstrumentasikan ejen AutoGen anda.

**Penciptaan Span Manual:** Walaupun perpustakaan instrumentasi menyediakan asas yang baik, sering terdapat kes di mana maklumat yang lebih terperinci atau tersuai diperlukan. Anda boleh mencipta span secara manual untuk menambah logik aplikasi tersuai. Lebih penting lagi, anda boleh memperkayakan span yang dicipta secara automatik atau manual dengan atribut tersuai (juga dikenali sebagai tag atau metadata). Atribut ini boleh merangkumi data khusus perniagaan, pengiraan perantaraan, atau sebarang konteks yang mungkin berguna untuk penyahpepijatan atau analisis, seperti `user_id`, `session_id`, atau `model_version`.

Contoh penciptaan jejak dan span secara manual dengan [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Penilaian Ejen

Pemerhatian memberikan kita metrik, tetapi penilaian adalah proses menganalisis data tersebut (dan menjalankan ujian) untuk menentukan sejauh mana prestasi ejen AI dan bagaimana ia boleh diperbaiki. Dalam erti kata lain, setelah anda mempunyai jejak dan metrik tersebut, bagaimana anda menggunakannya untuk menilai ejen dan membuat keputusan?

Penilaian berkala adalah penting kerana ejen AI sering tidak deterministik dan boleh berkembang (melalui kemas kini atau perubahan tingkah laku model) – tanpa penilaian, anda tidak akan tahu sama ada "ejen pintar" anda benar-benar melakukan tugasnya dengan baik atau jika ia telah merosot.

Terdapat dua kategori penilaian untuk ejen AI: **penilaian luar talian** dan **penilaian dalam talian**. Kedua-duanya bernilai dan saling melengkapi. Biasanya, kita bermula dengan penilaian luar talian, kerana ini adalah langkah minimum yang diperlukan sebelum menggunakan mana-mana ejen.

### Penilaian Luar Talian

![Item Dataset dalam Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Ini melibatkan penilaian ejen dalam persekitaran terkawal, biasanya menggunakan set data ujian, bukan pertanyaan pengguna langsung. Anda menggunakan set data yang dikurasi di mana anda tahu apa output yang diharapkan atau tingkah laku yang betul, dan kemudian menjalankan ejen anda pada set data tersebut.

Sebagai contoh, jika anda membina ejen masalah perkataan matematik, anda mungkin mempunyai [set data ujian](https://huggingface.co/datasets/gsm8k) sebanyak 100 masalah dengan jawapan yang diketahui. Penilaian luar talian sering dilakukan semasa pembangunan (dan boleh menjadi sebahagian daripada saluran CI/CD) untuk memeriksa penambahbaikan atau melindungi daripada kemerosotan. Kelebihannya ialah ia **boleh diulang dan anda boleh mendapatkan metrik ketepatan yang jelas kerana anda mempunyai kebenaran asas**. Anda juga mungkin mensimulasikan pertanyaan pengguna dan mengukur respons ejen terhadap jawapan ideal atau menggunakan metrik automatik seperti yang diterangkan di atas.

Cabaran utama dengan penilaian luar talian adalah memastikan set data ujian anda komprehensif dan kekal relevan – ejen mungkin berprestasi baik pada set ujian tetap tetapi menghadapi pertanyaan yang sangat berbeza dalam pengeluaran. Oleh itu, anda harus memastikan set ujian dikemas kini dengan kes tepi baru dan contoh yang mencerminkan senario dunia sebenar. Gabungan kes "ujian asap" kecil dan set penilaian yang lebih besar adalah berguna: set kecil untuk pemeriksaan pantas dan set yang lebih besar untuk metrik prestasi yang lebih luas.

### Penilaian Dalam Talian

![Gambaran Keseluruhan Metrik Pemerhatian](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Ini merujuk kepada penilaian ejen dalam persekitaran langsung, dunia sebenar, iaitu semasa penggunaan sebenar dalam pengeluaran. Penilaian dalam talian melibatkan pemantauan prestasi ejen pada interaksi pengguna sebenar dan menganalisis hasil secara berterusan.

Sebagai contoh, anda mungkin menjejaki kadar kejayaan, skor kepuasan pengguna, atau metrik lain pada trafik langsung. Kelebihan penilaian dalam talian ialah ia **menangkap perkara yang mungkin tidak anda jangkakan dalam persekitaran makmal** – anda boleh memerhatikan perubahan model dari masa ke masa (jika keberkesanan ejen merosot apabila corak input berubah) dan menangkap pertanyaan atau situasi yang tidak dijangka yang tidak terdapat dalam data ujian anda. Ia memberikan gambaran sebenar tentang bagaimana ejen berkelakuan di dunia sebenar.

Penilaian dalam talian sering melibatkan pengumpulan maklum balas pengguna tidak langsung dan langsung, seperti yang dibincangkan, dan mungkin menjalankan ujian bayangan atau ujian A/B (di mana versi baru ejen dijalankan selari untuk dibandingkan dengan yang lama). Cabarannya ialah sukar untuk mendapatkan label atau skor yang boleh dipercayai untuk interaksi langsung – anda mungkin bergantung pada maklum balas pengguna atau metrik hiliran (seperti sama ada pengguna mengklik hasilnya).

### Menggabungkan Kedua-duanya

Penilaian dalam talian dan luar talian tidak saling eksklusif; mereka sangat saling melengkapi. Pandangan daripada pemantauan dalam talian (contohnya, jenis pertanyaan pengguna baru di mana ejen berprestasi buruk) boleh digunakan untuk menambah dan memperbaiki set data ujian luar talian. Sebaliknya, ejen yang berprestasi baik dalam ujian luar talian boleh digunakan dengan lebih yakin dan dipantau dalam talian.

Malah, banyak pasukan mengamalkan gelung:

_penilaian luar talian -> penggunaan -> pemantauan dalam talian -> pengumpulan kes kegagalan baru -> tambah ke set data luar talian -> perbaiki ejen -> ulang_.

## Isu Biasa

Apabila anda menggunakan ejen AI ke dalam pengeluaran, anda mungkin menghadapi pelbagai cabaran. Berikut adalah beberapa isu biasa dan penyelesaian yang berpotensi:

| **Isu**    | **Penyelesaian Berpotensi**   |
| ------------- | ------------------ |
| Ejen AI tidak melaksanakan tugas secara konsisten | - Perhalusi arahan yang diberikan kepada Ejen AI; jelaskan objektif.<br>- Kenal pasti di mana membahagikan tugas kepada subtugas dan mengendalikannya oleh beberapa ejen boleh membantu. |
| Ejen AI terperangkap dalam gelung berterusan  | - Pastikan anda mempunyai syarat dan terma penamatan yang jelas supaya Ejen tahu bila untuk menghentikan proses.<br>- Untuk tugas kompleks yang memerlukan penaakulan dan perancangan, gunakan model yang lebih besar yang khusus untuk tugas penaakulan. |
| Panggilan alat ejen AI tidak berfungsi dengan baik   | - Uji dan sahkan output alat di luar sistem ejen. |

- Perhalusi parameter yang ditetapkan, arahan, dan penamaan alat.  
| Sistem Multi-Ejen tidak berfungsi secara konsisten | - Perhalusi arahan yang diberikan kepada setiap ejen untuk memastikan ia spesifik dan berbeza antara satu sama lain.<br>- Bina sistem hierarki menggunakan ejen "routing" atau pengawal untuk menentukan ejen yang sesuai. |

Banyak isu ini boleh dikenal pasti dengan lebih berkesan jika terdapat kebolehlihatan. Jejak dan metrik yang kita bincangkan sebelum ini membantu mengenal pasti dengan tepat di mana masalah berlaku dalam aliran kerja ejen, menjadikan proses penyahpepijatan dan pengoptimuman lebih cekap.

## Mengurus Kos

Berikut adalah beberapa strategi untuk mengurus kos dalam melaksanakan ejen AI ke dalam pengeluaran:

**Menggunakan Model Lebih Kecil:** Model Bahasa Kecil (SLM) boleh berfungsi dengan baik untuk beberapa kes penggunaan ejen dan akan mengurangkan kos dengan ketara. Seperti yang disebutkan sebelum ini, membina sistem penilaian untuk menentukan dan membandingkan prestasi berbanding model yang lebih besar adalah cara terbaik untuk memahami sejauh mana SLM akan berfungsi untuk kes penggunaan anda. Pertimbangkan untuk menggunakan SLM untuk tugas yang lebih mudah seperti klasifikasi niat atau pengekstrakan parameter, sementara model yang lebih besar dikhaskan untuk penaakulan yang lebih kompleks.

**Menggunakan Model Router:** Strategi serupa adalah dengan menggunakan kepelbagaian model dan saiz. Anda boleh menggunakan LLM/SLM atau fungsi tanpa pelayan untuk mengarahkan permintaan berdasarkan tahap kerumitan kepada model yang paling sesuai. Ini juga akan membantu mengurangkan kos sambil memastikan prestasi pada tugas yang betul. Sebagai contoh, arahkan pertanyaan mudah kepada model yang lebih kecil dan lebih pantas, dan hanya gunakan model besar yang mahal untuk tugas penaakulan yang kompleks.

**Caching Respons:** Mengenal pasti permintaan dan tugas yang biasa serta menyediakan respons sebelum ia melalui sistem ejen anda adalah cara yang baik untuk mengurangkan jumlah permintaan yang serupa. Anda juga boleh melaksanakan aliran untuk mengenal pasti sejauh mana kesamaan permintaan dengan permintaan yang telah dicache menggunakan model AI yang lebih asas. Strategi ini boleh mengurangkan kos dengan ketara untuk soalan yang sering ditanya atau aliran kerja yang biasa.

## Mari kita lihat bagaimana ini berfungsi dalam amalan

Dalam [notebook contoh bahagian ini](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb), kita akan melihat contoh bagaimana kita boleh menggunakan alat kebolehlihatan untuk memantau dan menilai ejen kita.

## Pelajaran Sebelumnya

[Pola Reka Bentuk Metakognisi](../09-metacognition/README.md)

## Pelajaran Seterusnya

[MCP](../11-mcp/README.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat penting, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.