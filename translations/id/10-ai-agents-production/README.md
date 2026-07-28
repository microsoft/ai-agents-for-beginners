# Agen AI dalam Produksi: Observabilitas & Evaluasi

[![AI Agents in Production](../../../translated_images/id/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Saat agen AI beralih dari prototipe eksperimental ke aplikasi dunia nyata, kemampuan untuk memahami perilaku mereka, memantau kinerja mereka, dan secara sistematis mengevaluasi keluaran mereka menjadi penting.

## Tujuan Pembelajaran

Setelah menyelesaikan pelajaran ini, Anda akan mengetahui/memahami:
- Konsep inti observabilitas dan evaluasi agen
- Teknik untuk meningkatkan kinerja, biaya, dan efektivitas agen
- Apa dan bagaimana mengevaluasi agen AI Anda secara sistematis
- Cara mengontrol biaya saat menerapkan agen AI ke produksi
- Cara menginstrumentasikan agen yang dibangun dengan Microsoft Agent Framework

Tujuannya adalah membekali Anda dengan pengetahuan untuk mengubah agen "kotak hitam" Anda menjadi sistem yang transparan, dapat dikelola, dan dapat diandalkan.

_**Catatan:** Penting untuk menerapkan Agen AI yang aman dan dapat dipercaya. Lihat juga pelajaran [Membangun Agen AI yang Dapat Dipercaya](../06-building-trustworthy-agents/README.md)._

## Jejak dan Rentang

Alat observabilitas seperti [Langfuse](https://langfuse.com/) atau [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) biasanya merepresentasikan jalannya agen sebagai jejak dan rentang.

- **Jejak** mewakili sebuah tugas agen lengkap dari awal sampai selesai (seperti menangani query pengguna).
- **Rentang** adalah langkah individual dalam jejak tersebut (seperti memanggil model bahasa atau mengambil data).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Tanpa observabilitas, agen AI bisa terasa seperti "kotak hitam" – keadaan internal dan alasan dari agen tidak transparan, menyulitkan diagnosis masalah atau optimalisasi kinerja. Dengan observabilitas, agen menjadi "kotak kaca," menawarkan transparansi yang penting untuk membangun kepercayaan dan memastikan mereka beroperasi sesuai yang diharapkan.

## Mengapa Observabilitas Penting di Lingkungan Produksi

Memindahkan agen AI ke lingkungan produksi memperkenalkan tantangan dan kebutuhan baru. Observabilitas bukan lagi sekadar "baik untuk dimiliki" tetapi kemampuan yang sangat penting:

*   **Debugging dan Analisis Penyebab Utama**: Saat agen gagal atau menghasilkan keluaran yang tidak terduga, alat observabilitas menyediakan jejak yang diperlukan untuk menentukan sumber kesalahan. Ini sangat penting pada agen kompleks yang mungkin melibatkan beberapa panggilan LLM, interaksi alat, dan logika kondisional.
*   **Pengelolaan Latensi dan Biaya**: Agen AI sering bergantung pada LLM dan API eksternal lain yang ditagihkan per token atau per panggilan. Observabilitas memungkinkan pelacakan tepat panggilan tersebut, membantu mengidentifikasi operasi yang sangat lambat atau mahal. Ini memungkinkan tim untuk mengoptimalkan prompt, memilih model yang lebih efisien, atau merancang ulang alur kerja untuk mengelola biaya operasional dan memastikan pengalaman pengguna yang baik.
*   **Kepercayaan, Keamanan, dan Kepatuhan**: Dalam banyak aplikasi, penting untuk memastikan agen berperilaku dengan aman dan etis. Observabilitas menyediakan jejak audit dari tindakan dan keputusan agen. Ini dapat digunakan untuk mendeteksi dan mengurangi masalah seperti injeksi prompt, produksi konten berbahaya, atau penanganan data pribadi yang tidak semestinya (PII). Misalnya, Anda dapat meninjau jejak untuk memahami mengapa agen memberikan respons tertentu atau menggunakan alat spesifik.
*   **Siklus Peningkatan Berkelanjutan**: Data observabilitas adalah dasar dari proses pengembangan iteratif. Dengan memantau kinerja agen di dunia nyata, tim dapat mengidentifikasi area untuk ditingkatkan, mengumpulkan data untuk penyempurnaan model, dan memvalidasi dampak perubahan. Ini menciptakan siklus umpan balik di mana wawasan produksi dari evaluasi daring menginformasikan eksperimen dan penyempurnaan luring, menghasilkan kinerja agen yang semakin baik.

## Metrik Kunci untuk Dipantau

Untuk memantau dan memahami perilaku agen, berbagai metrik dan sinyal harus dilacak. Meskipun metrik spesifik dapat berbeda berdasarkan tujuan agen, beberapa sangat penting secara umum.

Berikut adalah beberapa metrik paling umum yang dipantau oleh alat observabilitas:

**Latensi:** Seberapa cepat agen merespon? Waktu tunggu yang lama berdampak negatif pada pengalaman pengguna. Anda harus mengukur latensi untuk tugas dan langkah individual dengan melacak jalannya agen. Misalnya, agen yang membutuhkan 20 detik untuk semua panggilan model bisa dipercepat dengan menggunakan model yang lebih cepat atau menjalankan panggilan model secara paralel.

**Biaya:** Berapa pengeluaran per jalannya agen? Agen AI bergantung pada panggilan LLM yang ditagihkan per token atau API eksternal. Penggunaan alat yang sering atau banyak prompt dapat cepat menaikkan biaya. Misalnya, jika agen memanggil LLM lima kali untuk peningkatan kualitas marginal, Anda harus menilai apakah biayanya sepadan atau jika Anda bisa mengurangi jumlah panggilan atau menggunakan model yang lebih murah. Pemantauan waktu nyata juga dapat membantu mengidentifikasi lonjakan tak terduga (misalnya bug yang menyebabkan loop API berlebihan).

**Kesalahan Permintaan:** Berapa banyak permintaan yang gagal oleh agen? Ini bisa termasuk kesalahan API atau panggilan alat yang gagal. Untuk membuat agen Anda lebih tangguh terhadap ini di produksi, Anda dapat mengatur fallback atau retry. Contoh: jika penyedia LLM A down, Anda beralih ke penyedia LLM B sebagai cadangan.

**Umpan Balik Pengguna:** Implementasi evaluasi langsung dari pengguna memberikan wawasan berharga. Ini dapat mencakup penilaian eksplisit (👍suka/👎tidak, ⭐1-5 bintang) atau komentar teks. Umpan balik negatif yang konsisten harus mengingatkan Anda sebagai tanda agen tidak bekerja sesuai harapan.

**Umpan Balik Pengguna Implisit:** Perilaku pengguna memberikan umpan balik tidak langsung meskipun tanpa penilaian eksplisit. Ini bisa berupa pengulangan pertanyaan segera, pertanyaan berulang, atau mengklik tombol coba ulang. Misalnya, jika Anda melihat pengguna bertanya kembali pertanyaan yang sama berulang kali, ini tanda agen tidak bekerja seperti seharusnya.

**Akurasi:** Seberapa sering agen menghasilkan keluaran yang benar atau diinginkan? Definisi akurasi bervariasi (misalnya, kebenaran penyelesaian masalah, ketepatan pengambilan informasi, kepuasan pengguna). Langkah pertama adalah mendefinisikan apa arti sukses bagi agen Anda. Anda dapat melacak akurasi melalui pengecekan otomatis, skor evaluasi, atau label penyelesaian tugas. Misalnya, menandai jejak sebagai "berhasil" atau "gagal".

**Metrik Evaluasi Otomatis:** Anda juga dapat mengatur evaluasi otomatis. Misalnya, Anda dapat menggunakan LLM untuk memberi skor keluaran agen apakah membantu, akurat, atau tidak. Ada juga beberapa perpustakaan sumber terbuka yang membantu Anda memberi skor berbagai aspek agen. Contoh: [RAGAS](https://docs.ragas.io/) untuk agen RAG atau [LLM Guard](https://llm-guard.com/) untuk mendeteksi bahasa berbahaya atau injeksi prompt.

Dalam praktiknya, kombinasi metrik ini memberikan cakupan terbaik terhadap kesehatan agen AI. Dalam [notebook contoh](./code_samples/10-expense_claim-demo.ipynb) bab ini, kami akan menunjukkan bagaimana metrik ini terlihat dalam contoh nyata tetapi pertama-tama, kita akan belajar bagaimana workflow evaluasi yang tipikal terlihat.

## Instrumentasikan Agen Anda

Untuk mengumpulkan data jejak, Anda perlu menginstrumentasikan kode Anda. Tujuannya adalah untuk menginstrumentasikan kode agen agar menghasilkan jejak dan metrik yang dapat ditangkap, diproses, dan divisualisasikan oleh platform observabilitas.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) telah menjadi standar industri untuk observabilitas LLM. Ini menyediakan set API, SDK, dan alat untuk menghasilkan, mengumpulkan, dan mengekspor data telemetri.

Ada banyak perpustakaan instrumentasi yang membungkus framework agen yang ada dan memudahkan ekspor rentang OpenTelemetry ke alat observabilitas. Microsoft Agent Framework terintegrasi secara native dengan OpenTelemetry. Berikut contoh cara menginstrumentasikan agen MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Eksekusi agen dilacak secara otomatis
    pass
```

[notebook contoh](./code_samples/10-expense_claim-demo.ipynb) di bab ini akan mendemonstrasikan cara menginstrumentasikan agen MAF Anda.

**Pembuatan Rentang Manual:** Meskipun perpustakaan instrumentasi menyediakan baseline yang baik, sering kali ada kasus di mana diperlukan informasi yang lebih rinci atau khusus. Anda dapat membuat rentang secara manual untuk menambahkan logika aplikasi khusus. Yang lebih penting, mereka dapat memperkaya rentang yang dibuat otomatis atau manual dengan atribut khusus (juga dikenal sebagai tag atau metadata). Atribut ini bisa meliputi data bisnis spesifik, perhitungan antara, atau konteks apa pun yang berguna untuk debugging atau analisis, seperti `user_id`, `session_id`, atau `model_version`.

Contoh membuat jejak dan rentang secara manual dengan [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Evaluasi Agen

Observabilitas memberi kita metrik, tetapi evaluasi adalah proses menganalisis data itu (dan melakukan pengujian) untuk menentukan seberapa baik agen AI berperforma dan bagaimana cara meningkatkannya. Dengan kata lain, setelah Anda memiliki jejak dan metrik tersebut, bagaimana Anda menggunakannya untuk menilai agen dan membuat keputusan?

Evaluasi rutin penting karena agen AI sering bersifat nondeterministik dan bisa berkembang (melalui pembaruan atau perubahan perilaku model) – tanpa evaluasi, Anda tidak akan tahu apakah “agen pintar” Anda benar-benar menjalankan tugasnya dengan baik atau sudah mengalami regresi.

Ada dua kategori evaluasi untuk agen AI: **evaluasi daring** dan **evaluasi luring**. Keduanya berharga, dan saling melengkapi. Biasanya kita mulai dengan evaluasi luring, karena ini merupakan langkah minimum yang diperlukan sebelum meluncurkan agen apa pun.

### Evaluasi Luring

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Ini melibatkan evaluasi agen dalam lingkungan yang terkendali, biasanya menggunakan dataset tes, bukan query pengguna langsung. Anda menggunakan dataset yang dikurasi di mana Anda mengetahui keluaran yang diharapkan atau perilaku yang benar, lalu menjalankan agen Anda pada dataset tersebut.

Misalnya, jika Anda membangun agen soal matematika, Anda mungkin memiliki [dataset tes](https://huggingface.co/datasets/gsm8k) berisi 100 soal dengan jawaban yang diketahui. Evaluasi luring sering dilakukan selama pengembangan (dan bisa menjadi bagian dari pipeline CI/CD) untuk memeriksa peningkatan atau mencegah regresi. Keuntungannya adalah ini **dapat diulang dan Anda bisa mendapatkan metrik akurasi yang jelas karena Anda memiliki kebenaran dasar**. Anda juga bisa mensimulasikan query pengguna dan mengukur respons agen terhadap jawaban ideal atau menggunakan metrik otomatis seperti dijelaskan di atas.

Tantangan utama dengan evaluasi luring adalah memastikan dataset uji Anda komprehensif dan tetap relevan – agen mungkin berkinerja baik pada set uji tetap, tetapi menemui query yang sangat berbeda di produksi. Oleh karena itu, Anda harus memperbarui set uji dengan kasus tepi dan contoh baru yang mencerminkan skenario dunia nyata. Campuran kasus “smoke test” kecil dan set evaluasi yang lebih besar berguna: set kecil untuk pemeriksaan cepat dan set besar untuk metrik kinerja yang lebih luas.

### Evaluasi Daring

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Ini merujuk pada evaluasi agen dalam lingkungan nyata secara langsung, yaitu selama penggunaan aktual di produksi. Evaluasi daring melibatkan pemantauan kinerja agen pada interaksi pengguna nyata dan analisis hasil secara terus-menerus.

Misalnya, Anda bisa melacak tingkat keberhasilan, skor kepuasan pengguna, atau metrik lain pada traffic langsung. Keuntungan evaluasi daring adalah bahwa ini **menangkap hal-hal yang mungkin tidak Anda duga di lingkungan laboratorium** – Anda dapat mengamati drift model dari waktu ke waktu (jika efektivitas agen menurun seiring perubahan pola input) dan menangkap query atau situasi tak terduga yang tidak ada dalam data uji Anda. Ini memberikan gambaran sebenarnya tentang bagaimana agen berperilaku di lapangan.

Evaluasi daring seringkali melibatkan pengumpulan umpan balik implisit dan eksplisit pengguna, seperti yang dibahas, dan mungkin menjalankan uji bayangan (shadow tests) atau uji A/B (di mana versi baru agen berjalan paralel untuk dibandingkan dengan versi lama). Tantangannya adalah sulit mendapatkan label atau skor yang andal untuk interaksi langsung – Anda mungkin mengandalkan umpan balik pengguna atau metrik hulu (seperti apakah pengguna mengklik hasil).

### Menggabungkan Keduanya

Evaluasi daring dan luring tidak saling eksklusif; keduanya saling melengkapi. Wawasan dari pemantauan daring (misalnya, tipe baru query pengguna yang kinerjanya buruk) dapat digunakan untuk menambah dan memperbaiki dataset uji luring. Sebaliknya, agen yang berkinerja baik dalam uji luring dapat lebih percaya diri untuk diterapkan dan dipantau secara daring.

Banyak tim menerapkan siklus:

_evaluasi luring -> deploy -> pantau daring -> kumpulkan kasus kegagalan baru -> tambahkan ke dataset luring -> perbaiki agen -> ulangi_.

## Masalah Umum

Saat Anda menerapkan agen AI ke produksi, Anda mungkin menghadapi berbagai tantangan. Berikut beberapa masalah umum dan solusi potensialnya:

| **Masalah**    | **Solusi Potensial**   |
| ------------- | ------------------ |
| Agen AI tidak menjalankan tugas secara konsisten | - Perbaiki prompt yang diberikan ke Agen AI; jelaskan tujuan dengan jelas.<br>- Identifikasi di mana membagi tugas menjadi subtugas dan menanganinya oleh beberapa agen dapat membantu. |
| Agen AI mengalami loop terus-menerus | - Pastikan Anda memiliki syarat dan ketentuan penghentian yang jelas sehingga Agen tahu kapan harus menghentikan proses.<br>- Untuk tugas kompleks yang membutuhkan penalaran dan perencanaan, gunakan model yang lebih besar dan khusus untuk tugas penalaran. |
| Panggilan alat Agen AI tidak bekerja dengan baik | - Uji dan validasi keluaran alat di luar sistem agen.<br>- Perjelas parameter yang ditentukan, prompt, dan penamaan alat. |
| Sistem Multi-Agen tidak berjalan konsisten | - Perbaiki prompt yang diberikan ke masing-masing agen agar spesifik dan berbeda satu sama lain.<br>- Bangun sistem hierarkis menggunakan agen "routing" atau pengendali untuk menentukan agen yang tepat. |

Banyak masalah ini bisa diidentifikasi lebih efektif dengan adanya observabilitas. Jejak dan metrik yang sudah kita bahas membantu menentukan dengan tepat di mana dalam alur kerja agen masalah terjadi, sehingga debugging dan optimalisasi menjadi jauh lebih efisien.

## Mengelola Biaya


Berikut adalah beberapa strategi untuk mengelola biaya penerapan agen AI ke produksi:

**Menggunakan Model yang Lebih Kecil:** Model Bahasa Kecil (SLM) dapat bekerja dengan baik pada beberapa kasus penggunaan agenis tertentu dan akan mengurangi biaya secara signifikan. Seperti yang disebutkan sebelumnya, membangun sistem evaluasi untuk menentukan dan membandingkan kinerja vs model yang lebih besar adalah cara terbaik untuk memahami seberapa baik SLM akan bekerja pada kasus penggunaan Anda. Pertimbangkan menggunakan SLM untuk tugas sederhana seperti klasifikasi niat atau ekstraksi parameter, sementara model yang lebih besar disediakan untuk penalaran kompleks.

**Menggunakan Model Router:** Strategi serupa adalah menggunakan berbagai model dan ukuran. Anda dapat menggunakan LLM/SLM atau fungsi tanpa server untuk mengarahkan permintaan berdasarkan kompleksitas ke model yang paling sesuai. Ini juga akan membantu mengurangi biaya sekaligus memastikan kinerja pada tugas yang tepat. Misalnya, arahkan pertanyaan sederhana ke model yang lebih kecil dan lebih cepat, dan hanya gunakan model besar yang mahal untuk tugas penalaran kompleks.

**Menyimpan Cache Respons:** Mengidentifikasi permintaan dan tugas umum serta memberikan respons sebelum melewati sistem agenis Anda adalah cara yang baik untuk mengurangi volume permintaan serupa. Anda bahkan dapat menerapkan alur untuk mengidentifikasi seberapa mirip sebuah permintaan dengan permintaan yang sudah di-cache menggunakan model AI yang lebih dasar. Strategi ini dapat secara signifikan mengurangi biaya untuk pertanyaan yang sering diajukan atau alur kerja umum.

## Mari kita lihat bagaimana ini bekerja dalam praktik

Dalam [notebook contoh bagian ini](./code_samples/10-expense_claim-demo.ipynb), kita akan melihat contoh bagaimana kita dapat menggunakan alat observabilitas untuk memantau dan mengevaluasi agen kami.


### Punya Pertanyaan Lebih Lanjut tentang Agen AI di Produksi?

Bergabunglah dengan [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) untuk bertemu dengan pembelajar lain, menghadiri jam kantor, dan mendapatkan jawaban atas pertanyaan Anda tentang Agen AI.

## Pelajaran Sebelumnya

[Polanya Metakognisi](../09-metacognition/README.md)

## Pelajaran Selanjutnya

[Protokol Agenik](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->