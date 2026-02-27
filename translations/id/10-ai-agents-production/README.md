# Agen AI dalam Produksi: Observabilitas & Evaluasi

[![Agen AI dalam Produksi](../../../translated_images/id/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Seiring agen AI bergerak dari prototipe eksperimental ke aplikasi dunia nyata, kemampuan untuk memahami perilaku mereka, memantau kinerja mereka, dan mengevaluasi keluaran mereka secara sistematis menjadi penting.

## Tujuan Pembelajaran

Setelah menyelesaikan pelajaran ini, Anda akan mengetahui/memahami:
- Konsep inti observabilitas dan evaluasi agen
- Teknik untuk meningkatkan kinerja, biaya, dan efektivitas agen
- Apa dan bagaimana mengevaluasi agen AI Anda secara sistematis
- Cara mengendalikan biaya saat menerapkan agen AI ke produksi
- Cara menginstrumentasikan agen yang dibangun dengan Microsoft Agent Framework

Tujuannya adalah membekali Anda dengan pengetahuan untuk mengubah agen "kotak hitam" menjadi sistem yang transparan, dapat dikelola, dan dapat diandalkan.

_**Catatan:** Penting untuk men-deploy Agen AI yang aman dan dapat dipercaya. Periksa juga pelajaran [Membangun Agen AI yang Dapat Dipercaya](./06-building-trustworthy-agents/README.md)._

## Traces and Spans

Alat observabilitas seperti [Langfuse](https://langfuse.com/) atau [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) biasanya merepresentasikan run agen sebagai traces dan spans.

- **Trace** merepresentasikan tugas agen lengkap dari awal sampai selesai (seperti menangani query pengguna).
- **Spans** adalah langkah individual di dalam trace (seperti memanggil model bahasa atau mengambil data).

![Pohon jejak di Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Tanpa observabilitas, agen AI bisa terasa seperti "kotak hitam" - status internal dan alasan operasinya tidak terlihat, sehingga sulit untuk mendiagnosa masalah atau mengoptimalkan kinerja. Dengan observabilitas, agen menjadi "kotak kaca," menawarkan transparansi yang penting untuk membangun kepercayaan dan memastikan mereka beroperasi sebagaimana mestinya. 

## Mengapa Observabilitas Penting di Lingkungan Produksi

Transisi agen AI ke lingkungan produksi memperkenalkan serangkaian tantangan dan persyaratan baru. Observabilitas bukan lagi sekadar "bagus untuk dimiliki" tetapi kemampuan yang kritis:

*   **Debugging dan Analisis Akar Masalah**: Ketika agen gagal atau menghasilkan keluaran yang tidak terduga, alat observabilitas menyediakan trace yang diperlukan untuk menunjukkan sumber kesalahan. Ini sangat penting pada agen kompleks yang mungkin melibatkan banyak panggilan LLM, interaksi alat, dan logika kondisional.
*   **Manajemen Latensi dan Biaya**: Agen AI sering bergantung pada LLM dan API eksternal lainnya yang ditagih per token atau per panggilan. Observabilitas memungkinkan pelacakan tepat dari panggilan-panggilan ini, membantu mengidentifikasi operasi yang sangat lambat atau mahal. Ini memungkinkan tim mengoptimalkan prompt, memilih model yang lebih efisien, atau merancang ulang alur kerja untuk mengelola biaya operasional dan memastikan pengalaman pengguna yang baik.
*   **Kepercayaan, Keamanan, dan Kepatuhan**: Dalam banyak aplikasi, penting untuk memastikan bahwa agen berperilaku aman dan etis. Observabilitas menyediakan jejak audit dari tindakan dan keputusan agen. Ini dapat digunakan untuk mendeteksi dan mengurangi masalah seperti prompt injection, pembuatan konten berbahaya, atau penanganan data pribadi yang tidak semestinya (PII). Misalnya, Anda dapat meninjau trace untuk memahami mengapa agen memberikan respons tertentu atau menggunakan alat tertentu.
*   **Loop Perbaikan Berkelanjutan**: Data observabilitas adalah dasar dari proses pengembangan iteratif. Dengan memantau bagaimana agen berkinerja di dunia nyata, tim dapat mengidentifikasi area untuk perbaikan, mengumpulkan data untuk fine-tuning model, dan memvalidasi dampak perubahan. Ini menciptakan loop umpan balik di mana wawasan produksi dari evaluasi online menginformasikan eksperimen offline dan penyempurnaan, yang mengarah pada peningkatan kinerja agen secara bertahap.

## Metrik Kunci untuk Dipantau

Untuk memantau dan memahami perilaku agen, berbagai metrik dan sinyal harus dilacak. Meskipun metrik spesifik mungkin bervariasi berdasarkan tujuan agen, beberapa metrik bersifat universal penting.

Berikut beberapa metrik yang paling umum dipantau oleh alat observabilitas:

**Latency:** Seberapa cepat agen merespons? Waktu tunggu yang lama berdampak negatif pada pengalaman pengguna. Anda harus mengukur latensi untuk tugas dan langkah individual dengan menelusuri run agen. Misalnya, agen yang membutuhkan 20 detik untuk semua panggilan model dapat dipercepat dengan menggunakan model yang lebih cepat atau dengan menjalankan panggilan model secara paralel.

**Costs:** Berapa biaya per run agen? Agen AI bergantung pada panggilan LLM yang ditagih per token atau API eksternal. Penggunaan alat yang sering atau prompt berkali-kali dapat dengan cepat meningkatkan biaya. Misalnya, jika agen memanggil LLM lima kali untuk peningkatan kualitas yang marginal, Anda harus menilai apakah biayanya sepadan atau apakah Anda bisa mengurangi jumlah panggilan atau menggunakan model yang lebih murah. Pemantauan waktu-nyata juga dapat membantu mengidentifikasi lonjakan tak terduga (mis. bug yang menyebabkan loop API berlebihan).

**Request Errors:** Berapa banyak permintaan yang gagal dilakukan agen? Ini dapat mencakup error API atau panggilan alat yang gagal. Untuk membuat agen Anda lebih tangguh terhadap ini di produksi, Anda kemudian dapat menyiapkan fallback atau retry. Mis. jika penyedia LLM A down, Anda beralih ke penyedia LLM B sebagai cadangan.

**User Feedback:** Menerapkan evaluasi langsung dari pengguna memberikan wawasan berharga. Ini dapat mencakup penilaian eksplisit (👍thumbs-up/👎down, ⭐1-5 bintang) atau komentar tekstual. Umpan balik negatif yang konsisten harus memberi peringatan karena ini adalah tanda bahwa agen tidak bekerja sebagaimana mestinya. 

**Implicit User Feedback:** Perilaku pengguna memberikan umpan balik tidak langsung meskipun tanpa penilaian eksplisit. Ini dapat mencakup pengulangan penyusunan pertanyaan langsung, pertanyaan berulang atau mengeklik tombol coba lagi. Mis. jika Anda melihat pengguna berulang kali menanyakan pertanyaan yang sama, ini adalah tanda bahwa agen tidak bekerja sebagaimana mestinya.

**Accuracy:** Seberapa sering agen menghasilkan keluaran yang benar atau diinginkan? Definisi akurasi bervariasi (mis. ketepatan pemecahan masalah, akurasi pengambilan informasi, kepuasan pengguna). Langkah pertama adalah mendefinisikan seperti apa keberhasilan untuk agen Anda. Anda dapat melacak akurasi melalui pemeriksaan otomatis, skor evaluasi, atau label penyelesaian tugas. Misalnya, menandai trace sebagai "succeeded" atau "failed". 

**Automated Evaluation Metrics:** Anda juga dapat menyiapkan evaluasi otomatis. Misalnya, Anda dapat menggunakan LLM untuk memberi skor keluaran agen mis. apakah itu membantu, akurat, atau tidak. Ada juga beberapa pustaka open source yang membantu Anda memberi skor aspek berbeda dari agen. Mis. [RAGAS](https://docs.ragas.io/) untuk agen RAG atau [LLM Guard](https://llm-guard.com/) untuk mendeteksi bahasa berbahaya atau prompt injection. 

Dalam praktiknya, kombinasi metrik-metrik ini memberikan cakupan terbaik terhadap kesehatan agen AI. Dalam [notebook contoh](./code_samples/10-expense_claim-demo.ipynb) bab ini, kami akan menunjukkan bagaimana metrik-metrik ini terlihat dalam contoh nyata tetapi pertama-tama, kita akan mempelajari bagaimana alur kerja evaluasi tipikal terlihat.

## Instrumentasikan Agen Anda

Untuk mengumpulkan data tracing, Anda perlu menginstrumentasikan kode Anda. Tujuannya adalah menginstrumentasikan kode agen untuk menghasilkan trace dan metrik yang dapat ditangkap, diproses, dan divisualisasikan oleh platform observabilitas.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) telah muncul sebagai standar industri untuk observabilitas LLM. Ini menyediakan serangkaian API, SDK, dan alat untuk menghasilkan, mengumpulkan, dan mengekspor data telemetri. 

Ada banyak pustaka instrumentasi yang membungkus framework agen yang ada dan memudahkan mengekspor span OpenTelemetry ke alat observabilitas. Microsoft Agent Framework terintegrasi dengan OpenTelemetry secara native. Di bawah ini adalah contoh menginstrumentasikan agen MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Eksekusi agen dilacak secara otomatis
    pass
```

The [example notebook](./code_samples/10-expense_claim-demo.ipynb) in this chapter will demonstrate how to instrument your MAF agent.

**Pembuatan Span Manual:** Meski pustaka instrumentasi menyediakan baseline yang baik, sering kali ada kasus di mana informasi yang lebih rinci atau kustom dibutuhkan. Anda dapat membuat span secara manual untuk menambahkan logika aplikasi kustom. Lebih penting lagi, mereka dapat memperkaya span yang dibuat otomatis atau manual dengan atribut kustom (juga dikenal sebagai tag atau metadata). Atribut ini dapat mencakup data spesifik bisnis, perhitungan antara, atau konteks apa pun yang mungkin berguna untuk debugging atau analisis, seperti `user_id`, `session_id`, atau `model_version`.

Contoh membuat trace dan span secara manual dengan [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3): 

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Evaluasi Agen

Observabilitas memberi kita metrik, tetapi evaluasi adalah proses menganalisis data tersebut (dan melakukan pengujian) untuk menentukan seberapa baik agen AI berkinerja dan bagaimana ia dapat diperbaiki. Dengan kata lain, setelah Anda memiliki trace dan metrik tersebut, bagaimana Anda menggunakannya untuk menilai agen dan membuat keputusan? 

Evaluasi rutin penting karena agen AI sering nondeterministik dan dapat berkembang (melalui pembaruan atau perilaku model yang drift) – tanpa evaluasi, Anda tidak akan tahu apakah “agen pintar” Anda benar-benar melakukan tugasnya dengan baik atau mengalami regresi.

Ada dua kategori evaluasi untuk agen AI: **evaluasi online** dan **evaluasi offline**. Keduanya berharga, dan saling melengkapi. Kami biasanya memulai dengan evaluasi offline, karena ini adalah langkah minimum yang diperlukan sebelum menerapkan agen apa pun.

### Evaluasi Offline

![Item dataset di Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Ini melibatkan mengevaluasi agen dalam pengaturan terkontrol, biasanya menggunakan dataset pengujian, bukan query pengguna langsung. Anda menggunakan dataset kurasi di mana Anda tahu keluaran yang diharapkan atau perilaku yang benar, lalu menjalankan agen Anda pada dataset tersebut. 

Misalnya, jika Anda membangun agen soal kata matematika, Anda mungkin memiliki [dataset pengujian](https://huggingface.co/datasets/gsm8k) berisi 100 masalah dengan jawaban yang diketahui. Evaluasi offline sering dilakukan selama pengembangan (dan dapat menjadi bagian dari pipeline CI/CD) untuk memeriksa peningkatan atau mencegah regresi. Manfaatnya adalah bahwa ini **dapat diulang dan Anda dapat memperoleh metrik akurasi yang jelas karena Anda memiliki ground truth**. Anda juga dapat mensimulasikan query pengguna dan mengukur respons agen terhadap jawaban ideal atau menggunakan metrik otomatis seperti yang dijelaskan di atas. 

Tantangan utama dengan evaluasi offline adalah memastikan dataset pengujian Anda komprehensif dan tetap relevan – agen mungkin berkinerja baik pada set pengujian tetap tetapi menghadapi query yang sangat berbeda di produksi. Oleh karena itu, Anda harus terus memperbarui set pengujian dengan kasus tepi dan contoh baru yang mencerminkan skenario dunia nyata. Kombinasi set kecil "smoke test" dan set evaluasi yang lebih besar berguna: set kecil untuk pemeriksaan cepat dan set lebih besar untuk metrik kinerja yang lebih luas.

### Evaluasi Online 

![Ikhtisar metrik observabilitas](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Ini merujuk pada evaluasi agen di lingkungan langsung, dunia nyata, yaitu selama penggunaan aktual di produksi. Evaluasi online melibatkan pemantauan kinerja agen pada interaksi pengguna nyata dan analisis hasil secara berkelanjutan. 

Misalnya, Anda mungkin melacak tingkat keberhasilan, skor kepuasan pengguna, atau metrik lain pada lalu lintas langsung. Keuntungan evaluasi online adalah bahwa ini **menangkap hal-hal yang mungkin tidak Anda antisipasi di lingkungan lab** – Anda dapat mengamati drift model seiring waktu (jika efektivitas agen menurun saat pola input bergeser) dan menangkap query atau situasi tak terduga yang tidak ada dalam data uji Anda. Ini memberikan gambaran nyata tentang bagaimana agen berperilaku di lapangan. 

Evaluasi online sering melibatkan pengumpulan umpan balik implisit dan eksplisit dari pengguna, seperti yang dibahas, dan mungkin menjalankan shadow tests atau A/B tests (di mana versi baru agen berjalan paralel untuk dibandingkan dengan yang lama). Tantangannya adalah mendapatkan label atau skor yang andal untuk interaksi langsung bisa rumit – Anda mungkin mengandalkan umpan balik pengguna atau metrik hilir (mis. apakah pengguna mengklik hasil).

### Menggabungkan Keduanya

Evaluasi online dan offline tidak saling eksklusif; keduanya sangat saling melengkapi. Wawasan dari pemantauan online (mis. jenis query pengguna baru di mana agen berkinerja buruk) dapat digunakan untuk menambah dan memperbaiki dataset pengujian offline. Sebaliknya, agen yang berkinerja baik dalam uji offline dapat kemudian lebih percaya diri di-deploy dan dipantau secara online. 

Banyak tim mengadopsi sebuah loop: 

_evaluasi offline -> deploy -> pantau online -> kumpulkan kasus kegagalan baru -> tambahkan ke dataset offline -> perbaiki agen -> ulangi_.

## Masalah Umum

Saat Anda menerapkan agen AI ke produksi, Anda mungkin menghadapi berbagai tantangan. Berikut beberapa masalah umum dan solusi potensialnya:

| **Masalah**    | **Solusi Potensial**   |
| ------------- | ------------------ |
| Agen AI tidak menjalankan tugas secara konsisten | - Perbaiki prompt yang diberikan ke Agen AI; jelaskan tujuan dengan jelas.<br>- Identifikasi di mana membagi tugas menjadi subtugas dan menanganinya oleh beberapa agen dapat membantu. |
| Agen AI mengalami loop terus-menerus  | - Pastikan Anda memiliki ketentuan penghentian yang jelas sehingga Agen tahu kapan menghentikan proses.<br>- Untuk tugas kompleks yang memerlukan penalaran dan perencanaan, gunakan model yang lebih besar yang khusus untuk tugas penalaran. |
| Panggilan alat Agen AI tidak berkinerja baik   | - Uji dan validasi keluaran alat di luar sistem agen.<br>- Perbaiki parameter yang ditetapkan, prompt, dan penamaan alat.  |
| Sistem Multi-Agen tidak berkinerja konsisten | - Perbaiki prompt yang diberikan ke masing-masing agen untuk memastikan mereka spesifik dan berbeda satu sama lain.<br>- Bangun sistem hierarkis menggunakan agen "routing" atau pengontrol untuk menentukan agen mana yang tepat. |

Banyak dari masalah ini dapat diidentifikasi lebih efektif dengan observabilitas yang diterapkan. Trace dan metrik yang kita bahas sebelumnya membantu menunjukkan tepat di mana dalam alur kerja agen masalah terjadi, membuat debugging dan optimisasi jauh lebih efisien.

## Mengelola Biaya
Berikut beberapa strategi untuk mengelola biaya penerapan agen AI ke produksi:

**Menggunakan Model Lebih Kecil:** Model Bahasa Kecil (SLMs) dapat berkinerja baik pada beberapa kasus penggunaan agen dan secara signifikan akan mengurangi biaya. Seperti disebutkan sebelumnya, membangun sistem evaluasi untuk menentukan dan membandingkan kinerja vs model yang lebih besar adalah cara terbaik untuk memahami seberapa baik SLM akan berkinerja pada kasus penggunaan Anda. Pertimbangkan menggunakan SLM untuk tugas yang lebih sederhana seperti klasifikasi niat atau ekstraksi parameter, sementara menyimpan model yang lebih besar untuk penalaran yang kompleks.

**Menggunakan Model Router:** Strategi serupa adalah menggunakan keberagaman model dan ukuran. Anda dapat menggunakan LLM/SLM atau fungsi tanpa server untuk mengarahkan permintaan berdasarkan kompleksitas ke model yang paling sesuai. Ini juga akan membantu mengurangi biaya sekaligus memastikan kinerja pada tugas yang tepat. Misalnya, arahkan kueri sederhana ke model yang lebih kecil dan lebih cepat, dan hanya gunakan model besar yang mahal untuk tugas penalaran yang kompleks.

**Menyimpan Respons dalam Cache:** Mengidentifikasi permintaan dan tugas yang umum serta memberikan respons sebelum mereka melalui sistem agen Anda adalah cara yang baik untuk mengurangi volume permintaan serupa. Anda bahkan dapat menerapkan alur untuk mengidentifikasi seberapa mirip suatu permintaan dengan permintaan yang disimpan dalam cache menggunakan model AI yang lebih dasar. Strategi ini dapat secara signifikan mengurangi biaya untuk pertanyaan yang sering diajukan atau alur kerja umum.

## Mari kita lihat bagaimana ini bekerja dalam praktik

In the [example notebook of this section](./code_samples/10-expense_claim-demo.ipynb), kita akan melihat contoh tentang bagaimana kita dapat menggunakan alat observabilitas untuk memantau dan mengevaluasi agen kita.


### Punya Pertanyaan Lebih Lanjut tentang Agen AI di Produksi?

Bergabunglah dengan [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) untuk bertemu dengan pelajar lain, menghadiri jam kantor, dan mendapatkan jawaban atas pertanyaan Anda tentang Agen AI.

## Pelajaran Sebelumnya

[Pola Desain Metakognisi](../09-metacognition/README.md)

## Pelajaran Berikutnya

[Protokol Agen](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya mencapai akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat penting atau krusial, disarankan menggunakan terjemahan profesional oleh penerjemah manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul akibat penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->