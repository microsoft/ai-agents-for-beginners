# Agen AI di Produksi: Observabilitas & Evaluasi

[![Agen AI di Produksi](../../../translated_images/id/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Saat agen AI bergerak dari prototipe eksperimental ke aplikasi dunia nyata, kemampuan untuk memahami perilaku mereka, memantau kinerja mereka, dan secara sistematis mengevaluasi output mereka menjadi penting.

## Tujuan Pembelajaran

Setelah menyelesaikan pelajaran ini, Anda akan mengetahui/memahami:
- Konsep inti observabilitas dan evaluasi agen
- Teknik untuk meningkatkan kinerja, biaya, dan efektivitas agen
- Apa dan bagaimana mengevaluasi agen AI Anda secara sistematis
- Cara mengendalikan biaya saat menerapkan agen AI ke produksi
- Cara menginstrumen agen yang dibangun dengan Microsoft Agent Framework

Tujuannya adalah membekali Anda dengan pengetahuan untuk mengubah agen "kotak hitam" menjadi sistem yang transparan, dapat dikelola, dan dapat diandalkan.

_**Catatan:** Penting untuk menerapkan Agen AI yang aman dan dapat dipercaya. Lihat juga pelajaran [Membangun Agen AI yang Dapat Dipercaya](./06-building-trustworthy-agents/README.md)._

## Jejak dan Spans

Alat observabilitas seperti [Langfuse](https://langfuse.com/) atau [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) biasanya merepresentasikan jalannya agen sebagai jejak dan spans.

- **Trace** mewakili tugas agen lengkap dari awal hingga selesai (seperti menangani kueri pengguna).
- **Spans** adalah langkah-langkah individual dalam jejak (seperti memanggil model bahasa atau mengambil data).

![Pohon Trace di Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Tanpa observabilitas, agen AI bisa terasa seperti "kotak hitam" - kondisi internal dan penalarannya tidak terlihat, membuatnya sulit untuk mendiagnosis masalah atau mengoptimalkan kinerja. Dengan observabilitas, agen menjadi "kotak kaca," menawarkan transparansi yang penting untuk membangun kepercayaan dan memastikan mereka beroperasi sebagaimana mestinya. 

## Mengapa Observabilitas Penting di Lingkungan Produksi

Transisi agen AI ke lingkungan produksi memperkenalkan serangkaian tantangan dan persyaratan baru. Observabilitas tidak lagi menjadi "berguna untuk dimiliki" tetapi kemampuan yang kritis:

*   **Debugging dan Analisis Akar Masalah:** Ketika agen gagal atau menghasilkan output yang tidak terduga, alat observabilitas menyediakan jejak yang dibutuhkan untuk menentukan sumber kesalahan. Ini sangat penting pada agen kompleks yang mungkin melibatkan banyak pemanggilan LLM, interaksi alat, dan logika kondisional.
*   **Manajemen Latensi dan Biaya:** Agen AI sering bergantung pada LLM dan API eksternal lainnya yang ditagih per token atau per panggilan. Observabilitas memungkinkan pelacakan tepat dari panggilan-panggilan ini, membantu mengidentifikasi operasi yang sangat lambat atau mahal. Ini memungkinkan tim untuk mengoptimalkan prompt, memilih model yang lebih efisien, atau merancang ulang alur kerja untuk mengelola biaya operasional dan memastikan pengalaman pengguna yang baik.
*   **Kepercayaan, Keamanan, dan Kepatuhan:** Dalam banyak aplikasi, penting untuk memastikan bahwa agen berperilaku aman dan etis. Observabilitas menyediakan jejak audit dari tindakan dan keputusan agen. Ini dapat digunakan untuk mendeteksi dan mengurangi masalah seperti injeksi prompt, generasi konten berbahaya, atau penanganan data pribadi yang tidak semestinya (PII). Misalnya, Anda dapat meninjau jejak untuk memahami mengapa agen memberikan respons tertentu atau menggunakan alat spesifik.
*   **Siklus Peningkatan Berkelanjutan:** Data observabilitas adalah dasar dari proses pengembangan iteratif. Dengan memantau bagaimana agen berkinerja di dunia nyata, tim dapat mengidentifikasi area yang perlu ditingkatkan, mengumpulkan data untuk penyetelan model, dan memvalidasi dampak perubahan. Ini menciptakan loop umpan balik di mana wawasan produksi dari evaluasi online menginformasikan eksperimen offline dan penyempurnaan, yang mengarah pada peningkatan kinerja agen secara bertahap.

## Metrik Utama yang Perlu Dipantau

Untuk memantau dan memahami perilaku agen, berbagai metrik dan sinyal harus dilacak. Meskipun metrik spesifik mungkin bervariasi berdasarkan tujuan agen, beberapa metrik bersifat universal penting.

Berikut beberapa metrik yang paling umum dipantau oleh alat observabilitas:

**Latency:** Seberapa cepat agen merespons? Waktu tunggu yang lama berdampak negatif pada pengalaman pengguna. Anda harus mengukur latensi untuk tugas dan langkah individual dengan menelusuri jalannya agen. Misalnya, agen yang membutuhkan 20 detik untuk semua panggilan model dapat dipercepat dengan menggunakan model yang lebih cepat atau menjalankan panggilan model secara paralel.

**Costs:** Berapa biaya per eksekusi agen? Agen AI bergantung pada panggilan LLM yang ditagih per token atau API eksternal. Penggunaan alat yang sering atau beberapa prompt dapat dengan cepat meningkatkan biaya. Misalnya, jika agen memanggil LLM lima kali untuk peningkatan kualitas marginal, Anda harus menilai apakah biayanya sepadan atau apakah Anda bisa mengurangi jumlah panggilan atau menggunakan model yang lebih murah. Pemantauan waktu nyata juga dapat membantu mengidentifikasi lonjakan tak terduga (mis. bug yang menyebabkan loop API berlebihan).

**Request Errors:** Berapa banyak permintaan yang gagal oleh agen? Ini dapat mencakup kesalahan API atau kegagalan pemanggilan alat. Untuk membuat agen Anda lebih tangguh terhadap hal ini di produksi, Anda kemudian dapat menyiapkan fallback atau retry. Mis. jika penyedia LLM A down, Anda beralih ke penyedia LLM B sebagai cadangan.

**User Feedback:** Menerapkan evaluasi langsung dari pengguna memberikan wawasan berharga. Ini dapat mencakup penilaian eksplisit (👍thumbs-up/👎down, ⭐1-5 bintang) atau komentar tekstual. Umpan balik negatif yang konsisten harus memperingatkan Anda karena ini tanda bahwa agen tidak bekerja sebagaimana mestinya. 

**Implicit User Feedback:** Perilaku pengguna memberikan umpan balik tidak langsung meskipun tanpa penilaian eksplisit. Ini dapat mencakup pengulangan pertanyaan segera, pengulangan kueri, atau mengklik tombol coba lagi. Mis. jika Anda melihat pengguna berulang kali menanyakan pertanyaan yang sama, ini tanda bahwa agen tidak bekerja sebagaimana mestinya.

**Accuracy:** Seberapa sering agen menghasilkan output yang benar atau diinginkan? Definisi akurasi bervariasi (mis. kebenaran pemecahan masalah, akurasi pengambilan informasi, kepuasan pengguna). Langkah pertama adalah mendefinisikan seperti apa keberhasilan untuk agen Anda. Anda dapat melacak akurasi melalui pemeriksaan otomatis, skor evaluasi, atau label penyelesaian tugas. Misalnya, menandai jejak sebagai "succeeded" atau "failed". 

**Automated Evaluation Metrics:** Anda juga dapat menyiapkan evaluasi otomatis. Misalnya, Anda dapat menggunakan LLM untuk memberi skor output agen, mis. apakah berguna, akurat, atau tidak. Ada juga beberapa pustaka sumber terbuka yang membantu Anda memberi skor berbagai aspek agen. Mis. [RAGAS](https://docs.ragas.io/) untuk agen RAG atau [LLM Guard](https://llm-guard.com/) untuk mendeteksi bahasa berbahaya atau injeksi prompt. 

Dalam praktiknya, kombinasi metrik-metrik ini memberikan cakupan terbaik untuk kesehatan agen AI. Dalam [notebook contoh](./code_samples/10-expense_claim-demo.ipynb) pada bab ini, kami akan menunjukkan bagaimana metrik-metrik ini terlihat dalam contoh nyata tetapi pertama-tama, kita akan mempelajari bagaimana alur kerja evaluasi tipikal terlihat.

## Instrumen Agen Anda

Untuk mengumpulkan data penelusuran, Anda perlu menginstrumen kode Anda. Tujuannya adalah menginstrumen kode agen untuk memancarkan jejak dan metrik yang dapat ditangkap, diproses, dan divisualisasikan oleh platform observabilitas.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) telah muncul sebagai standar industri untuk observabilitas LLM. Ini menyediakan seperangkat API, SDK, dan alat untuk menghasilkan, mengumpulkan, dan mengekspor data telemetri. 

Ada banyak pustaka instrumentasi yang membungkus kerangka agen yang ada dan memudahkan ekspor span OpenTelemetry ke alat observabilitas. Microsoft Agent Framework terintegrasi dengan OpenTelemetry secara native. Di bawah ini adalah contoh tentang menginstrumentasikan agen MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Eksekusi agen dilacak secara otomatis
    pass
```

The [example notebook](./code_samples/10-expense_claim-demo.ipynb) in this chapter will demonstrate how to instrument your MAF agent.

**Pembuatan Span Manual:** Sementara pustaka instrumentasi menyediakan dasar yang baik, seringkali ada kasus di mana informasi yang lebih rinci atau kustom diperlukan. Anda dapat membuat span secara manual untuk menambahkan logika aplikasi kustom. Yang lebih penting, mereka dapat memperkaya span yang dibuat secara otomatis atau manual dengan atribut kustom (juga dikenal sebagai tag atau metadata). Atribut ini dapat mencakup data spesifik bisnis, perhitungan antara, atau konteks apa pun yang mungkin berguna untuk debugging atau analisis, seperti `user_id`, `session_id`, atau `model_version`.

Contoh membuat jejak dan span secara manual dengan [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3): 

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Evaluasi Agen

Observabilitas memberi kita metrik, tetapi evaluasi adalah proses menganalisis data tersebut (dan melakukan pengujian) untuk menentukan seberapa baik agen AI berkinerja dan bagaimana ia dapat ditingkatkan. Dengan kata lain, setelah Anda memiliki jejak dan metrik tersebut, bagaimana Anda menggunakannya untuk menilai agen dan membuat keputusan? 

Evaluasi rutin penting karena agen AI seringkali nondeterministik dan dapat berkembang (melalui pembaruan atau pergeseran perilaku model) – tanpa evaluasi, Anda tidak akan tahu apakah "agen pintar" Anda benar-benar melakukan tugasnya dengan baik atau mengalami regresi.

Ada dua kategori evaluasi untuk agen AI: **evaluasi online** dan **evaluasi offline**. Keduanya berharga, dan saling melengkapi. Kami biasanya mulai dengan evaluasi offline, karena ini adalah langkah minimum yang diperlukan sebelum menerapkan agen apa pun.

### Evaluasi Offline

![Item dataset di Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Ini melibatkan mengevaluasi agen dalam pengaturan terkontrol, biasanya menggunakan dataset uji, bukan kueri pengguna langsung. Anda menggunakan dataset yang dikurasi di mana Anda tahu apa output yang diharapkan atau perilaku yang benar, lalu menjalankan agen Anda pada dataset tersebut. 

Misalnya, jika Anda membangun agen pemecah soal matematika, Anda mungkin memiliki [dataset uji](https://huggingface.co/datasets/gsm8k) berisi 100 soal dengan jawaban yang diketahui. Evaluasi offline sering dilakukan selama pengembangan (dan dapat menjadi bagian dari pipeline CI/CD) untuk memeriksa peningkatan atau mencegah regresi. Keuntungannya adalah bahwa ini **dapat diulang dan Anda dapat memperoleh metrik akurasi yang jelas karena Anda memiliki ground truth**. Anda juga dapat mensimulasikan kueri pengguna dan mengukur respons agen terhadap jawaban ideal atau menggunakan metrik otomatis seperti yang dijelaskan di atas. 

Tantangan utama dengan evaluasi offline adalah memastikan dataset uji Anda komprehensif dan tetap relevan – agen mungkin berkinerja baik pada set uji tetap tetapi menemui kueri yang sangat berbeda di produksi. Oleh karena itu, Anda harus terus memperbarui set uji dengan kasus tepi dan contoh baru yang mencerminkan skenario dunia nyata​. Campuran "smoke test" kecil dan set evaluasi yang lebih besar berguna: set kecil untuk pemeriksaan cepat dan set yang lebih besar untuk metrik kinerja yang lebih luas​.

### Evaluasi Online 

![Ikhtisar metrik observabilitas](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Ini merujuk pada mengevaluasi agen di lingkungan langsung dan dunia nyata, yaitu selama penggunaan aktual di produksi. Evaluasi online melibatkan memantau kinerja agen pada interaksi pengguna nyata dan menganalisis hasil secara berkelanjutan. 

Misalnya, Anda dapat melacak tingkat keberhasilan, skor kepuasan pengguna, atau metrik lain pada lalu lintas langsung. Keuntungan evaluasi online adalah bahwa ini **menangkap hal-hal yang mungkin tidak Anda antisipasi dalam pengaturan laboratorium** – Anda dapat mengamati drift model dari waktu ke waktu (jika efektivitas agen menurun saat pola input bergeser) dan menangkap kueri atau situasi tak terduga yang tidak ada dalam data uji Anda​. Ini memberikan gambaran nyata tentang bagaimana agen berperilaku di lapangan. 

Evaluasi online sering melibatkan pengumpulan umpan balik implisit dan eksplisit dari pengguna, seperti yang dibahas, dan mungkin menjalankan shadow tests atau uji A/B (di mana versi baru agen berjalan paralel untuk dibandingkan dengan versi lama). Tantangannya adalah bahwa bisa sulit mendapatkan label atau skor yang andal untuk interaksi langsung – Anda mungkin bergantung pada umpan balik pengguna atau metrik hilir (seperti apakah pengguna mengklik hasil).

### Menggabungkan Keduanya

Evaluasi online dan offline tidak saling eksklusif; mereka sangat saling melengkapi. Wawasan dari pemantauan online (mis. jenis kueri pengguna baru di mana agen berkinerja buruk) dapat digunakan untuk menambah dan memperbaiki dataset uji offline. Sebaliknya, agen yang berkinerja baik dalam pengujian offline dapat lebih percaya diri untuk dideploy dan dipantau secara online. 

Faktanya, banyak tim mengadopsi sebuah loop: 

_evaluasi offline -> terapkan -> pantau online -> kumpulkan kasus kegagalan baru -> tambahkan ke dataset offline -> perbaiki agen -> ulangi_.

## Masalah Umum

Saat Anda menerapkan agen AI ke produksi, Anda mungkin menghadapi berbagai tantangan. Berikut beberapa masalah umum dan solusi potensialnya:

| **Masalah**    | **Solusi Potensial**   |
| ------------- | ------------------ |
| Agen AI tidak menjalankan tugas secara konsisten | - Perbaiki prompt yang diberikan ke Agen AI; jelaskan tujuannya.<br>- Identifikasi apakah membagi tugas menjadi subtugas dan menanganinya oleh beberapa agen dapat membantu. |
| Agen AI mengalami loop berkelanjutan  | - Pastikan Anda memiliki istilah dan kondisi terminasi yang jelas sehingga Agen tahu kapan harus menghentikan proses.<br>- Untuk tugas kompleks yang memerlukan penalaran dan perencanaan, gunakan model yang lebih besar yang khusus untuk tugas penalaran. |
| Pemanggilan alat oleh Agen AI tidak berjalan baik   | - Uji dan validasi output alat di luar sistem agen.<br>- Perbaiki parameter yang didefinisikan, prompt, dan penamaan alat.  |
| Sistem Multi-Agen tidak bekerja secara konsisten | - Perbaiki prompt yang diberikan ke setiap agen untuk memastikan mereka spesifik dan berbeda satu sama lain.<br>- Bangun sistem hierarkis menggunakan agen "routing" atau controller untuk menentukan agen mana yang tepat. |

Banyak dari masalah ini dapat diidentifikasi lebih efektif dengan observabilitas yang terpasang. Jejak dan metrik yang dibahas sebelumnya membantu menentukan dengan tepat di mana dalam alur kerja agen masalah terjadi, membuat debugging dan optimisasi jauh lebih efisien.

## Mengelola Biaya
Berikut beberapa strategi untuk mengelola biaya penerapan agen AI ke produksi:

**Using Smaller Models:** Small Language Models (SLMs) dapat berkinerja baik pada beberapa kasus penggunaan agenik tertentu dan akan mengurangi biaya secara signifikan. Seperti disebutkan sebelumnya, membangun sistem evaluasi untuk menentukan dan membandingkan kinerja dibandingkan model yang lebih besar adalah cara terbaik untuk memahami seberapa baik SLM akan berkinerja pada kasus penggunaan Anda. Pertimbangkan menggunakan SLMs untuk tugas yang lebih sederhana seperti klasifikasi intent atau ekstraksi parameter, sementara menyimpan model yang lebih besar untuk penalaran yang kompleks.

**Using a Router Model:** Strategi serupa adalah menggunakan beragam model dan ukuran. Anda dapat menggunakan LLM/SLM atau fungsi serverless untuk merutekan permintaan berdasarkan kompleksitas ke model yang paling sesuai. Ini juga akan membantu mengurangi biaya sekaligus memastikan kinerja pada tugas yang tepat. Misalnya, rute kueri sederhana ke model yang lebih kecil dan lebih cepat, dan hanya gunakan model besar yang mahal untuk tugas penalaran yang kompleks.

**Caching Responses:** Mengidentifikasi permintaan dan tugas yang umum dan menyediakan respons sebelum melewati sistem agentik Anda adalah cara yang bagus untuk mengurangi volume permintaan serupa. Anda bahkan dapat mengimplementasikan alur untuk mengidentifikasi seberapa mirip suatu permintaan dengan permintaan yang telah di-cache menggunakan model AI yang lebih dasar. Strategi ini dapat secara signifikan mengurangi biaya untuk pertanyaan yang sering diajukan atau alur kerja umum.

## Mari kita lihat bagaimana ini bekerja dalam praktik

Dalam [notebook contoh dari bagian ini](./code_samples/10-expense_claim-demo.ipynb), kita akan melihat contoh bagaimana kita dapat menggunakan alat observabilitas untuk memantau dan mengevaluasi agen kita.


### Punya Pertanyaan Lain tentang Agen AI dalam Produksi?

Bergabung dengan [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) untuk bertemu dengan pembelajar lain, menghadiri jam kantor dan mendapatkan jawaban atas pertanyaan Anda tentang Agen AI.

## Pelajaran Sebelumnya

[Pola Desain Metakognisi](../09-metacognition/README.md)

## Pelajaran Berikutnya

[Protokol Agentik](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Penafian:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya mencapai ketepatan, harap diperhatikan bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidaktepatan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber otoritatif. Untuk informasi yang bersifat krusial, disarankan menggunakan terjemahan profesional oleh penerjemah manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->