<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a008c204051cba8d0e253b75f261c41",
  "translation_date": "2025-08-29T18:03:20+00:00",
  "source_file": "08-multi-agent/README.md",
  "language_code": "id"
}
-->
[![Desain Multi-Agen](../../../translated_images/lesson-8-thumbnail.278a3e4a59137d625df92de3f885d2da2a92b1f7017abba25a99fb25edd83a55.id.png)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Klik gambar di atas untuk menonton video pelajaran ini)_

# Pola Desain Multi-Agen

Ketika Anda mulai mengerjakan proyek yang melibatkan beberapa agen, Anda perlu mempertimbangkan pola desain multi-agen. Namun, mungkin tidak langsung jelas kapan harus beralih ke multi-agen dan apa keuntungannya.

## Pendahuluan

Dalam pelajaran ini, kita akan mencoba menjawab pertanyaan-pertanyaan berikut:

- Dalam skenario apa saja multi-agen dapat diterapkan?
- Apa keuntungan menggunakan multi-agen dibandingkan hanya satu agen tunggal yang melakukan banyak tugas?
- Apa saja elemen dasar dalam menerapkan pola desain multi-agen?
- Bagaimana kita dapat memantau interaksi antara beberapa agen?

## Tujuan Pembelajaran

Setelah pelajaran ini, Anda diharapkan mampu:

- Mengidentifikasi skenario di mana multi-agen dapat diterapkan.
- Mengenali keuntungan menggunakan multi-agen dibandingkan agen tunggal.
- Memahami elemen dasar dalam menerapkan pola desain multi-agen.

Apa gambaran besarnya?

*Multi-agen adalah pola desain yang memungkinkan beberapa agen bekerja sama untuk mencapai tujuan bersama.*

Pola ini banyak digunakan di berbagai bidang, termasuk robotika, sistem otonom, dan komputasi terdistribusi.

## Skenario di Mana Multi-Agen Dapat Diterapkan

Jadi, dalam skenario apa saja penggunaan multi-agen menjadi pilihan yang baik? Jawabannya adalah ada banyak skenario di mana penggunaan beberapa agen sangat bermanfaat, terutama dalam kasus berikut:

- **Beban kerja besar**: Beban kerja besar dapat dibagi menjadi tugas-tugas kecil dan dialokasikan ke agen yang berbeda, memungkinkan pemrosesan paralel dan penyelesaian yang lebih cepat. Contohnya adalah dalam tugas pemrosesan data besar.
- **Tugas kompleks**: Tugas kompleks, seperti beban kerja besar, dapat dipecah menjadi sub-tugas kecil dan dialokasikan ke agen yang berbeda, masing-masing mengkhususkan diri pada aspek tertentu dari tugas tersebut. Contohnya adalah kendaraan otonom di mana agen yang berbeda mengelola navigasi, deteksi rintangan, dan komunikasi dengan kendaraan lain.
- **Keahlian beragam**: Agen yang berbeda dapat memiliki keahlian yang beragam, memungkinkan mereka menangani aspek-aspek tugas yang berbeda lebih efektif dibandingkan satu agen tunggal. Contohnya adalah dalam bidang kesehatan di mana agen dapat mengelola diagnosis, rencana perawatan, dan pemantauan pasien.

## Keuntungan Menggunakan Multi-Agen Dibandingkan Agen Tunggal

Sistem agen tunggal mungkin bekerja dengan baik untuk tugas sederhana, tetapi untuk tugas yang lebih kompleks, menggunakan beberapa agen dapat memberikan beberapa keuntungan:

- **Spesialisasi**: Setiap agen dapat mengkhususkan diri pada tugas tertentu. Kurangnya spesialisasi pada agen tunggal berarti agen tersebut dapat melakukan segalanya tetapi mungkin bingung ketika menghadapi tugas yang kompleks. Misalnya, agen tersebut mungkin melakukan tugas yang tidak sesuai dengan kemampuannya.
- **Skalabilitas**: Lebih mudah untuk meningkatkan sistem dengan menambahkan lebih banyak agen daripada membebani satu agen.
- **Toleransi Kesalahan**: Jika satu agen gagal, agen lain dapat terus berfungsi, memastikan keandalan sistem.

Mari kita ambil contoh, misalnya memesan perjalanan untuk seorang pengguna. Sistem agen tunggal harus menangani semua aspek proses pemesanan perjalanan, mulai dari mencari penerbangan hingga memesan hotel dan mobil sewaan. Untuk mencapai ini dengan satu agen, agen tersebut harus memiliki alat untuk menangani semua tugas ini. Hal ini dapat menyebabkan sistem yang kompleks dan monolitik yang sulit untuk dipelihara dan diskalakan. Sistem multi-agen, di sisi lain, dapat memiliki agen yang berbeda yang mengkhususkan diri dalam mencari penerbangan, memesan hotel, dan mobil sewaan. Ini akan membuat sistem lebih modular, lebih mudah dipelihara, dan lebih mudah diskalakan.

Bandingkan ini dengan biro perjalanan yang dijalankan sebagai toko kecil versus biro perjalanan yang dijalankan sebagai waralaba. Toko kecil akan memiliki satu agen yang menangani semua aspek proses pemesanan perjalanan, sedangkan waralaba akan memiliki agen yang berbeda yang menangani aspek-aspek berbeda dari proses pemesanan perjalanan.

## Elemen Dasar dalam Menerapkan Pola Desain Multi-Agen

Sebelum Anda dapat menerapkan pola desain multi-agen, Anda perlu memahami elemen dasar yang membentuk pola ini.

Mari kita buat ini lebih konkret dengan kembali melihat contoh memesan perjalanan untuk seorang pengguna. Dalam kasus ini, elemen dasarnya meliputi:

- **Komunikasi Agen**: Agen untuk mencari penerbangan, memesan hotel, dan mobil sewaan perlu berkomunikasi dan berbagi informasi tentang preferensi dan batasan pengguna. Anda perlu memutuskan protokol dan metode untuk komunikasi ini. Secara konkret, ini berarti agen untuk mencari penerbangan perlu berkomunikasi dengan agen untuk memesan hotel untuk memastikan bahwa hotel dipesan untuk tanggal yang sama dengan penerbangan. Ini berarti agen-agen tersebut perlu berbagi informasi tentang tanggal perjalanan pengguna, yang berarti Anda perlu memutuskan *agen mana yang berbagi informasi dan bagaimana mereka berbagi informasi*.
- **Mekanisme Koordinasi**: Agen perlu mengoordinasikan tindakan mereka untuk memastikan bahwa preferensi dan batasan pengguna terpenuhi. Preferensi pengguna bisa berupa keinginan untuk hotel yang dekat dengan bandara, sedangkan batasan bisa berupa mobil sewaan hanya tersedia di bandara. Ini berarti agen untuk memesan hotel perlu berkoordinasi dengan agen untuk memesan mobil sewaan untuk memastikan bahwa preferensi dan batasan pengguna terpenuhi. Ini berarti Anda perlu memutuskan *bagaimana agen-agen tersebut mengoordinasikan tindakan mereka*.
- **Arsitektur Agen**: Agen perlu memiliki struktur internal untuk membuat keputusan dan belajar dari interaksi mereka dengan pengguna. Ini berarti agen untuk mencari penerbangan perlu memiliki struktur internal untuk membuat keputusan tentang penerbangan mana yang direkomendasikan kepada pengguna. Ini berarti Anda perlu memutuskan *bagaimana agen-agen tersebut membuat keputusan dan belajar dari interaksi mereka dengan pengguna*. Contoh bagaimana agen belajar dan meningkatkan diri bisa berupa agen untuk mencari penerbangan menggunakan model pembelajaran mesin untuk merekomendasikan penerbangan kepada pengguna berdasarkan preferensi mereka di masa lalu.
- **Visibilitas ke Interaksi Multi-Agen**: Anda perlu memiliki visibilitas ke bagaimana beberapa agen berinteraksi satu sama lain. Ini berarti Anda perlu memiliki alat dan teknik untuk melacak aktivitas dan interaksi agen. Ini bisa berupa alat logging dan pemantauan, alat visualisasi, dan metrik kinerja.
- **Pola Multi-Agen**: Ada berbagai pola untuk menerapkan sistem multi-agen, seperti arsitektur terpusat, terdesentralisasi, dan hibrida. Anda perlu memutuskan pola yang paling sesuai dengan kasus penggunaan Anda.
- **Manusia dalam Lingkaran**: Dalam banyak kasus, Anda akan memiliki manusia dalam lingkaran dan Anda perlu menginstruksikan agen kapan harus meminta intervensi manusia. Ini bisa berupa pengguna yang meminta hotel atau penerbangan tertentu yang tidak direkomendasikan oleh agen atau meminta konfirmasi sebelum memesan penerbangan atau hotel.

## Visibilitas ke Interaksi Multi-Agen

Penting untuk memiliki visibilitas ke bagaimana beberapa agen berinteraksi satu sama lain. Visibilitas ini penting untuk debugging, pengoptimalan, dan memastikan efektivitas keseluruhan sistem. Untuk mencapainya, Anda perlu memiliki alat dan teknik untuk melacak aktivitas dan interaksi agen. Ini bisa berupa alat logging dan pemantauan, alat visualisasi, dan metrik kinerja.

Sebagai contoh, dalam kasus memesan perjalanan untuk seorang pengguna, Anda bisa memiliki dasbor yang menunjukkan status masing-masing agen, preferensi dan batasan pengguna, serta interaksi antara agen. Dasbor ini bisa menunjukkan tanggal perjalanan pengguna, penerbangan yang direkomendasikan oleh agen penerbangan, hotel yang direkomendasikan oleh agen hotel, dan mobil sewaan yang direkomendasikan oleh agen mobil sewaan. Ini akan memberikan Anda gambaran yang jelas tentang bagaimana agen-agen tersebut berinteraksi satu sama lain dan apakah preferensi dan batasan pengguna terpenuhi.

Mari kita lihat masing-masing aspek ini lebih detail.

- **Alat Logging dan Pemantauan**: Anda ingin melakukan logging untuk setiap tindakan yang diambil oleh agen. Entri log dapat menyimpan informasi tentang agen yang mengambil tindakan, tindakan yang diambil, waktu tindakan diambil, dan hasil dari tindakan tersebut. Informasi ini kemudian dapat digunakan untuk debugging, pengoptimalan, dan lainnya.

- **Alat Visualisasi**: Alat visualisasi dapat membantu Anda melihat interaksi antara agen dengan cara yang lebih intuitif. Misalnya, Anda bisa memiliki grafik yang menunjukkan aliran informasi antara agen. Ini dapat membantu Anda mengidentifikasi hambatan, ketidakefisienan, dan masalah lainnya dalam sistem.

- **Metrik Kinerja**: Metrik kinerja dapat membantu Anda melacak efektivitas sistem multi-agen. Misalnya, Anda bisa melacak waktu yang dibutuhkan untuk menyelesaikan tugas, jumlah tugas yang diselesaikan per unit waktu, dan akurasi rekomendasi yang dibuat oleh agen. Informasi ini dapat membantu Anda mengidentifikasi area untuk perbaikan dan mengoptimalkan sistem.

## Pola Multi-Agen

Mari kita bahas beberapa pola konkret yang dapat digunakan untuk membuat aplikasi multi-agen. Berikut adalah beberapa pola menarik yang patut dipertimbangkan:

### Obrolan Grup

Pola ini berguna ketika Anda ingin membuat aplikasi obrolan grup di mana beberapa agen dapat saling berkomunikasi. Kasus penggunaan khas untuk pola ini termasuk kolaborasi tim, dukungan pelanggan, dan jejaring sosial.

Dalam pola ini, setiap agen mewakili pengguna dalam obrolan grup, dan pesan dipertukarkan antara agen menggunakan protokol pesan. Agen dapat mengirim pesan ke obrolan grup, menerima pesan dari obrolan grup, dan merespons pesan dari agen lain.

Pola ini dapat diterapkan menggunakan arsitektur terpusat di mana semua pesan dirutekan melalui server pusat, atau arsitektur terdesentralisasi di mana pesan dipertukarkan secara langsung.

![Obrolan Grup](../../../translated_images/multi-agent-group-chat.ec10f4cde556babd7b450fd01e1a0fac1f9788c27d3b9e54029377bb1bdd1db6.id.png)

### Serah Terima

Pola ini berguna ketika Anda ingin membuat aplikasi di mana beberapa agen dapat menyerahkan tugas satu sama lain.

Kasus penggunaan khas untuk pola ini termasuk dukungan pelanggan, manajemen tugas, dan otomatisasi alur kerja.

Dalam pola ini, setiap agen mewakili tugas atau langkah dalam alur kerja, dan agen dapat menyerahkan tugas kepada agen lain berdasarkan aturan yang telah ditentukan.

![Serah Terima](../../../translated_images/multi-agent-hand-off.4c5fb00ba6f8750a0754bf29d49fa19d578080c61da40416df84d866bcdd87a3.id.png)

### Penyaringan Kolaboratif

Pola ini berguna ketika Anda ingin membuat aplikasi di mana beberapa agen dapat berkolaborasi untuk memberikan rekomendasi kepada pengguna.

Mengapa Anda ingin beberapa agen berkolaborasi? Karena setiap agen dapat memiliki keahlian yang berbeda dan dapat berkontribusi pada proses rekomendasi dengan cara yang berbeda.

Mari kita ambil contoh di mana seorang pengguna ingin mendapatkan rekomendasi tentang saham terbaik untuk dibeli di pasar saham.

- **Ahli industri**: Satu agen bisa menjadi ahli dalam industri tertentu.
- **Analisis teknis**: Agen lain bisa menjadi ahli dalam analisis teknis.
- **Analisis fundamental**: Dan agen lainnya bisa menjadi ahli dalam analisis fundamental. Dengan berkolaborasi, agen-agen ini dapat memberikan rekomendasi yang lebih komprehensif kepada pengguna.

![Rekomendasi](../../../translated_images/multi-agent-filtering.d959cb129dc9f60826916f0f12fe7a8339b532f5f236860afb8f16b63ea10dc2.id.png)

## Skenario: Proses Pengembalian Dana

Pertimbangkan skenario di mana seorang pelanggan mencoba mendapatkan pengembalian dana untuk suatu produk, ada beberapa agen yang terlibat dalam proses ini, tetapi mari kita bagi antara agen yang spesifik untuk proses ini dan agen umum yang dapat digunakan dalam proses lainnya.

**Agen yang spesifik untuk proses pengembalian dana**:

Berikut adalah beberapa agen yang dapat terlibat dalam proses pengembalian dana:

- **Agen pelanggan**: Agen ini mewakili pelanggan dan bertanggung jawab untuk memulai proses pengembalian dana.
- **Agen penjual**: Agen ini mewakili penjual dan bertanggung jawab untuk memproses pengembalian dana.
- **Agen pembayaran**: Agen ini mewakili proses pembayaran dan bertanggung jawab untuk mengembalikan pembayaran pelanggan.
- **Agen resolusi**: Agen ini mewakili proses resolusi dan bertanggung jawab untuk menyelesaikan masalah yang muncul selama proses pengembalian dana.
- **Agen kepatuhan**: Agen ini mewakili proses kepatuhan dan bertanggung jawab untuk memastikan bahwa proses pengembalian dana mematuhi peraturan dan kebijakan.

**Agen umum**:

Agen-agen ini dapat digunakan oleh bagian lain dari bisnis Anda.

- **Agen pengiriman**: Agen ini mewakili proses pengiriman dan bertanggung jawab untuk mengirimkan produk kembali ke penjual. Agen ini dapat digunakan baik untuk proses pengembalian dana maupun untuk pengiriman produk secara umum, misalnya melalui pembelian.
- **Agen umpan balik**: Agen ini mewakili proses umpan balik dan bertanggung jawab untuk mengumpulkan umpan balik dari pelanggan. Umpan balik dapat dikumpulkan kapan saja dan tidak hanya selama proses pengembalian dana.
- **Agen eskalasi**: Agen ini mewakili proses eskalasi dan bertanggung jawab untuk mengeskalasi masalah ke tingkat dukungan yang lebih tinggi. Anda dapat menggunakan jenis agen ini untuk proses apa pun di mana Anda perlu mengeskalasi masalah.
- **Agen notifikasi**: Agen ini mewakili proses notifikasi dan bertanggung jawab untuk mengirimkan notifikasi kepada pelanggan pada berbagai tahap proses pengembalian dana.
- **Agen analitik**: Agen ini mewakili proses analitik dan bertanggung jawab untuk menganalisis data terkait proses pengembalian dana.
- **Agen audit**: Agen ini mewakili proses audit dan bertanggung jawab untuk mengaudit proses pengembalian dana untuk memastikan bahwa proses tersebut dilakukan dengan benar.
- **Agen pelaporan**: Agen ini mewakili proses pelaporan dan bertanggung jawab untuk menghasilkan laporan tentang proses pengembalian dana.
- **Agen pengetahuan**: Agen ini mewakili proses pengetahuan dan bertanggung jawab untuk memelihara basis pengetahuan informasi terkait proses pengembalian dana. Agen ini dapat memiliki pengetahuan baik tentang pengembalian dana maupun bagian lain dari bisnis Anda.
- **Agen keamanan**: Agen ini mewakili proses keamanan dan bertanggung jawab untuk memastikan keamanan proses pengembalian dana.
- **Agen kualitas**: Agen ini mewakili proses kualitas dan bertanggung jawab untuk memastikan kualitas proses pengembalian dana.

Ada cukup banyak agen yang disebutkan sebelumnya, baik untuk proses pengembalian dana yang spesifik maupun untuk agen umum yang dapat digunakan di bagian lain dari bisnis Anda. Semoga ini memberi Anda gambaran tentang bagaimana Anda dapat memutuskan agen mana yang akan digunakan dalam sistem multi-agen Anda.

## Tugas
Desain sistem multi-agen untuk proses dukungan pelanggan. Identifikasi agen-agen yang terlibat dalam proses tersebut, peran dan tanggung jawab mereka, serta bagaimana mereka saling berinteraksi. Pertimbangkan baik agen yang spesifik untuk proses dukungan pelanggan maupun agen umum yang dapat digunakan di bagian lain bisnis Anda.

> Pikirkan baik-baik sebelum membaca solusi berikut, Anda mungkin membutuhkan lebih banyak agen daripada yang Anda pikirkan.

> TIP: Pikirkan tentang berbagai tahap dalam proses dukungan pelanggan dan juga pertimbangkan agen yang dibutuhkan untuk sistem apa pun.

## Solusi

[Solusi](./solution/solution.md)

## Pemeriksaan Pengetahuan

Pertanyaan: Kapan Anda harus mempertimbangkan menggunakan multi-agen?

- [ ] A1: Ketika Anda memiliki beban kerja kecil dan tugas yang sederhana.
- [ ] A2: Ketika Anda memiliki beban kerja besar.
- [ ] A3: Ketika Anda memiliki tugas yang sederhana.

[Kuis Solusi](./solution/solution-quiz.md)

## Ringkasan

Dalam pelajaran ini, kita telah membahas pola desain multi-agen, termasuk skenario di mana multi-agen dapat diterapkan, keuntungan menggunakan multi-agen dibandingkan agen tunggal, elemen-elemen dasar dalam menerapkan pola desain multi-agen, dan bagaimana memiliki visibilitas terhadap interaksi antar agen.

### Punya Pertanyaan Lebih Lanjut tentang Pola Desain Multi-Agen?

Bergabunglah dengan [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) untuk bertemu dengan pelajar lainnya, menghadiri jam kantor, dan mendapatkan jawaban atas pertanyaan Anda tentang AI Agents.

## Sumber Daya Tambahan

- 

## Pelajaran Sebelumnya

[Desain Perencanaan](../07-planning-design/README.md)

## Pelajaran Selanjutnya

[Metakognisi dalam AI Agents](../09-metacognition/README.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan penerjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk memberikan hasil yang akurat, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.