[![Multi-Agent Design](../../../translated_images/id/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Klik gambar di atas untuk melihat video pelajaran ini)_

# Pola desain multi-agen

Begitu Anda mulai mengerjakan proyek yang melibatkan beberapa agen, Anda perlu mempertimbangkan pola desain multi-agen. Namun, mungkin tidak langsung jelas kapan harus beralih ke multi-agen dan apa keuntungannya.

## Pendahuluan

Dalam pelajaran ini, kita akan mencoba menjawab pertanyaan-pertanyaan berikut:

- Apa saja skenario di mana multi-agen dapat diterapkan?
- Apa keuntungan menggunakan multi-agen dibandingkan hanya satu agen tunggal yang melakukan banyak tugas?
- Apa blok bangunan dari penerapan pola desain multi-agen?
- Bagaimana kita memiliki visibilitas tentang bagaimana beberapa agen saling berinteraksi?

## Tujuan Pembelajaran

Setelah pelajaran ini, Anda harus dapat:

- Mengidentifikasi skenario di mana multi-agen dapat diterapkan
- Mengenali keuntungan menggunakan multi-agen dibandingkan agen tunggal.
- Memahami blok bangunan dalam penerapan pola desain multi-agen.

Apa gambaran besarnya?

*Multi-agen adalah pola desain yang memungkinkan beberapa agen bekerja sama untuk mencapai tujuan bersama*.

Pola ini banyak digunakan di berbagai bidang, termasuk robotika, sistem otonom, dan komputasi terdistribusi.

## Skenario Di Mana Multi-Agen Dapat Diterapkan

Jadi, skenario apa yang merupakan kasus penggunaan yang baik untuk memakai multi-agen? Jawabannya adalah ada banyak skenario di mana penggunaan beberapa agen menguntungkan, terutama dalam kasus berikut:

- **Beban kerja besar**: Beban kerja besar dapat dibagi menjadi tugas-tugas kecil dan dialokasikan ke agen yang berbeda, memungkinkan pemrosesan paralel dan penyelesaian lebih cepat. Contohnya dalam kasus tugas pengolahan data besar.
- **Tugas kompleks**: Tugas kompleks, seperti beban kerja besar, dapat dipecah menjadi subtugas yang lebih kecil dan dialokasikan ke agen yang berbeda, masing-masing mengkhususkan diri pada aspek tertentu dari tugas tersebut. Contoh yang baik adalah pada kendaraan otonom di mana agen berbeda mengelola navigasi, deteksi rintangan, dan komunikasi dengan kendaraan lain.
- **Keahlian beragam**: Berbeda agen dapat memiliki keahlian yang beragam, memungkinkan mereka menangani aspek tugas yang berbeda dengan lebih efektif daripada satu agen tunggal. Untuk kasus ini, contoh yang baik adalah di bidang layanan kesehatan di mana agen dapat mengelola diagnostik, rencana perawatan, dan pemantauan pasien.

## Keuntungan Menggunakan Multi-Agen Dibandingkan Agen Tunggal

Sistem agen tunggal bisa bekerja dengan baik untuk tugas sederhana, tetapi untuk tugas lebih kompleks, menggunakan beberapa agen dapat memberikan beberapa keuntungan:

- **Spesialisasi**: Setiap agen dapat mengkhususkan diri pada tugas tertentu. Kurangnya spesialisasi pada agen tunggal berarti Anda memiliki agen yang bisa melakukan segalanya tetapi mungkin bingung tentang apa yang harus dilakukan saat menghadapi tugas yang kompleks. Misalnya, agen tersebut bisa saja akhirnya mengerjakan tugas yang tidak sesuai dengan keahliannya.
- **Skalabilitas**: Lebih mudah meningkatkan sistem dengan menambahkan lebih banyak agen daripada membebani satu agen tunggal.
- **Toleransi Kesalahan**: Jika satu agen gagal, agen lain dapat terus berfungsi, memastikan keandalan sistem.

Mari kita ambil contoh, mari kita pesan perjalanan untuk seorang pengguna. Sistem agen tunggal harus menangani semua aspek proses pemesanan perjalanan, dari mencari penerbangan sampai memesan hotel dan mobil sewaan. Untuk mencapai ini dengan satu agen, agen harus memiliki alat untuk menangani semua tugas tersebut. Hal ini dapat menghasilkan sistem yang kompleks dan monolitik yang sulit untuk dipelihara dan diskalakan. Sistem multi-agen, di sisi lain, dapat memiliki agen berbeda yang mengkhususkan diri dalam mencari penerbangan, memesan hotel, dan mobil sewaan. Ini membuat sistem lebih modular, lebih mudah dipelihara, dan dapat diskalakan.

Bandingkan ini dengan biro perjalanan yang dijalankan sebagai toko kecil versus biro perjalanan yang dijalankan sebagai waralaba. Toko kecil akan memiliki satu agen yang menangani semua aspek proses pemesanan perjalanan, sementara waralaba memiliki agen berbeda yang menangani berbagai aspek proses pemesanan perjalanan.

## Blok Bangunan dalam Penerapan Pola Desain Multi-Agen

Sebelum Anda dapat menerapkan pola desain multi-agen, Anda perlu memahami blok bangunan yang membentuk pola tersebut.

Mari kita buat ini lebih konkret dengan kembali melihat contoh pemesanan perjalanan untuk seorang pengguna. Dalam hal ini, blok bangunannya meliputi:

- **Komunikasi Agen**: Agen untuk mencari penerbangan, memesan hotel, dan mobil sewaan perlu berkomunikasi dan berbagi informasi tentang preferensi dan kendala pengguna. Anda perlu memutuskan protokol dan metode untuk komunikasi ini. Secara konkret ini berarti agen pencari penerbangan perlu berkomunikasi dengan agen pemesan hotel untuk memastikan hotel dipesan pada tanggal yang sama dengan penerbangan. Artinya agen-agen harus saling berbagi informasi tentang tanggal perjalanan pengguna, sehingga Anda perlu memutuskan *agen mana yang berbagi informasi dan bagaimana mereka berbagi informasi*.
- **Mekanisme Koordinasi**: Agen perlu mengoordinasikan tindakan mereka untuk memastikan preferensi dan kendala pengguna terpenuhi. Preferensi pengguna misalnya ingin hotel dekat bandara sedangkan kendalanya adalah mobil sewaan hanya tersedia di bandara. Ini berarti agen pemesan hotel perlu berkoordinasi dengan agen pemesan mobil sewaan untuk memastikan preferensi dan kendala pengguna terpenuhi. Jadi Anda perlu memutuskan *bagaimana agen-agen mengoordinasikan tindakan mereka*.
- **Arsitektur Agen**: Agen perlu memiliki struktur internal untuk membuat keputusan dan belajar dari interaksi mereka dengan pengguna. Ini berarti agen pencari penerbangan perlu memiliki struktur internal untuk membuat keputusan tentang penerbangan mana yang akan direkomendasikan kepada pengguna. Ini berarti Anda perlu memutuskan *bagaimana agen membuat keputusan dan belajar dari interaksi mereka dengan pengguna*. Contoh bagaimana agen belajar dan meningkatkan bisa berupa agen pencari penerbangan menggunakan model pembelajaran mesin untuk merekomendasikan penerbangan kepada pengguna berdasarkan preferensi sebelumnya.
- **Visibilitas terhadap Interaksi Multi-Agen**: Anda perlu memiliki visibilitas tentang bagaimana beberapa agen berinteraksi satu sama lain. Ini berarti Anda memerlukan alat dan teknik untuk melacak aktivitas dan interaksi agen. Ini bisa berupa alat pencatatan dan pemantauan, alat visualisasi, dan metrik kinerja.
- **Pola Multi-Agen**: Ada beberapa pola untuk menerapkan sistem multi-agen, seperti arsitektur terpusat, terdesentralisasi, dan hibrid. Anda perlu memilih pola yang paling sesuai dengan kasus penggunaan Anda.
- **Manusia dalam Loop**: Dalam sebagian besar kasus, Anda akan memiliki manusia dalam loop dan perlu menginstruksikan agen kapan harus meminta intervensi manusia. Ini bisa berupa pengguna yang meminta hotel atau penerbangan spesifik yang tidak direkomendasikan agen atau meminta konfirmasi sebelum memesan penerbangan atau hotel.

## Visibilitas terhadap Interaksi Multi-Agen

Penting bagi Anda untuk memiliki visibilitas bagaimana beberapa agen berinteraksi satu sama lain. Visibilitas ini penting untuk debugging, optimalisasi, dan memastikan efektivitas keseluruhan sistem. Untuk mencapainya, Anda perlu memiliki alat dan teknik untuk melacak aktivitas dan interaksi agen. Ini bisa berupa alat pencatatan dan pemantauan, alat visualisasi, dan metrik kinerja.

Misalnya, dalam kasus memesan perjalanan untuk seorang pengguna, Anda bisa memiliki dashboard yang menunjukkan status masing-masing agen, preferensi dan kendala pengguna, serta interaksi antar agen. Dashboard ini bisa menunjukkan tanggal perjalanan pengguna, penerbangan yang direkomendasikan oleh agen penerbangan, hotel yang direkomendasikan oleh agen hotel, dan mobil sewaan yang direkomendasikan oleh agen mobil sewaan. Ini memberikan gambaran jelas bagaimana agen berinteraksi dan apakah preferensi dan kendala pengguna terpenuhi.

Mari kita lihat masing-masing aspek ini lebih rinci.

- **Alat Pencatatan dan Pemantauan**: Anda ingin pencatatan dilakukan untuk setiap tindakan yang dilakukan oleh agen. Entri log bisa menyimpan informasi tentang agen yang melakukan tindakan, tindakan yang diambil, waktu tindakan diambil, dan hasil tindakan. Informasi ini kemudian dapat digunakan untuk debugging, optimalisasi, dan lain-lain.

- **Alat Visualisasi**: Alat visualisasi dapat membantu Anda melihat interaksi antar agen secara lebih intuitif. Misalnya, Anda bisa memiliki grafik yang menunjukkan aliran informasi antar agen. Ini bisa membantu mengidentifikasi hambatan, ketidakefisienan, dan masalah lain dalam sistem.

- **Metrik Kinerja**: Metrik kinerja dapat membantu Anda melacak efektivitas sistem multi-agen. Misalnya, Anda bisa melacak waktu yang dibutuhkan untuk menyelesaikan sebuah tugas, jumlah tugas yang diselesaikan per satuan waktu, dan akurasi rekomendasi yang dibuat oleh agen. Informasi ini dapat membantu Anda mengidentifikasi area yang perlu diperbaiki dan mengoptimalkan sistem.

## Pola Multi-Agen

Mari kita dalami beberapa pola konkret yang dapat kita gunakan untuk membuat aplikasi multi-agen. Berikut beberapa pola menarik yang patut dipertimbangkan:

### Obrolan grup

Pola ini berguna ketika Anda ingin membuat aplikasi obrolan grup di mana beberapa agen dapat berkomunikasi satu sama lain. Kasus penggunaan khas untuk pola ini termasuk kolaborasi tim, dukungan pelanggan, dan jejaring sosial.

Dalam pola ini, setiap agen mewakili pengguna dalam obrolan grup, dan pesan dipertukarkan antar agen menggunakan protokol pengiriman pesan. Agen dapat mengirim pesan ke obrolan grup, menerima pesan dari obrolan grup, dan merespons pesan dari agen lain.

Pola ini dapat diterapkan menggunakan arsitektur terpusat di mana semua pesan diarahkan melalui server pusat atau arsitektur terdesentralisasi di mana pesan dipertukarkan secara langsung.

![Group chat](../../../translated_images/id/multi-agent-group-chat.ec10f4cde556babd.webp)

### Penyerahan tugas

Pola ini berguna ketika Anda ingin membuat aplikasi di mana beberapa agen dapat menyerahkan tugas kepada satu sama lain.

Kasus penggunaan khas untuk pola ini termasuk dukungan pelanggan, manajemen tugas, dan otomasi alur kerja.

Dalam pola ini, setiap agen mewakili tugas atau langkah dalam alur kerja, dan agen dapat menyerahkan tugas kepada agen lain berdasarkan aturan yang telah ditentukan.

![Hand off](../../../translated_images/id/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Penyaringan kolaboratif

Pola ini berguna ketika Anda ingin membuat aplikasi di mana beberapa agen dapat berkolaborasi untuk memberikan rekomendasi kepada pengguna.

Alasan Anda ingin beberapa agen berkolaborasi adalah karena setiap agen dapat memiliki keahlian berbeda dan dapat memberikan kontribusi dalam proses rekomendasi dengan cara yang berbeda.

Mari kita ambil contoh seorang pengguna ingin rekomendasi saham terbaik untuk dibeli di pasar saham.

- **Ahli industri**: Satu agen bisa menjadi ahli dalam industri tertentu.
- **Analisis teknikal**: Agen lain bisa ahli dalam analisis teknikal.
- **Analisis fundamental**: dan agen lain bisa ahli dalam analisis fundamental. Dengan berkolaborasi, agen-agen ini dapat memberikan rekomendasi yang lebih komprehensif kepada pengguna.

![Recommendation](../../../translated_images/id/multi-agent-filtering.d959cb129dc9f608.webp)

## Skenario: Proses pengembalian uang

Pertimbangkan skenario di mana pelanggan mencoba mendapatkan pengembalian uang untuk suatu produk, ada cukup banyak agen yang terlibat dalam proses ini tetapi mari kita bagi antara agen khusus untuk proses ini dan agen umum yang dapat digunakan di proses lain.

**Agen khusus untuk proses pengembalian uang**:

Berikut beberapa agen yang bisa terlibat dalam proses pengembalian uang:

- **Agen pelanggan**: Agen ini mewakili pelanggan dan bertanggung jawab memulai proses pengembalian uang.
- **Agen penjual**: Agen ini mewakili penjual dan bertanggung jawab memproses pengembalian uang.
- **Agen pembayaran**: Agen ini mewakili proses pembayaran dan bertanggung jawab mengembalikan pembayaran pelanggan.
- **Agen penyelesaian**: Agen ini mewakili proses penyelesaian dan bertanggung jawab menyelesaikan masalah yang muncul selama proses pengembalian uang.
- **Agen kepatuhan**: Agen ini mewakili proses kepatuhan dan bertanggung jawab memastikan proses pengembalian uang sesuai dengan regulasi dan kebijakan.

**Agen umum**:

Agen-agen ini dapat digunakan oleh bagian lain dari bisnis Anda.

- **Agen pengiriman**: Agen ini mewakili proses pengiriman dan bertanggung jawab mengirimkan produk kembali ke penjual. Agen ini dapat digunakan baik untuk proses pengembalian uang maupun pengiriman produk umum melalui pembelian misalnya.
- **Agen umpan balik**: Agen ini mewakili proses umpan balik dan bertanggung jawab mengumpulkan umpan balik dari pelanggan. Umpan balik dapat dilakukan kapan saja, tidak hanya selama proses pengembalian uang.
- **Agen eskalasi**: Agen ini mewakili proses eskalasi dan bertanggung jawab mengeskalasi masalah ke tingkat dukungan yang lebih tinggi. Anda dapat menggunakan jenis agen ini untuk proses apa pun yang membutuhkan eskalasi masalah.
- **Agen notifikasi**: Agen ini mewakili proses notifikasi dan bertanggung jawab mengirim notifikasi kepada pelanggan pada berbagai tahap proses pengembalian uang.
- **Agen analitik**: Agen ini mewakili proses analitik dan bertanggung jawab menganalisis data terkait proses pengembalian uang.
- **Agen audit**: Agen ini mewakili proses audit dan bertanggung jawab mengaudit proses pengembalian uang untuk memastikan proses berjalan dengan benar.
- **Agen pelaporan**: Agen ini mewakili proses pelaporan dan bertanggung jawab membuat laporan tentang proses pengembalian uang.
- **Agen pengetahuan**: Agen ini mewakili proses pengetahuan dan bertanggung jawab memelihara basis pengetahuan informasi terkait proses pengembalian uang. Agen ini bisa memiliki pengetahuan tentang pengembalian uang dan bagian lain dari bisnis Anda.
- **Agen keamanan**: Agen ini mewakili proses keamanan dan bertanggung jawab memastikan keamanan proses pengembalian uang.
- **Agen kualitas**: Agen ini mewakili proses kualitas dan bertanggung jawab memastikan kualitas proses pengembalian uang.

Ada cukup banyak agen yang disebutkan sebelumnya, baik untuk proses pengembalian uang spesifik maupun untuk agen umum yang dapat digunakan di bagian lain bisnis Anda. Semoga ini memberi Anda gambaran tentang bagaimana Anda bisa memutuskan agen mana yang digunakan dalam sistem multi-agen Anda.

## Tugas

Rancang sistem multi-agen untuk proses dukungan pelanggan. Identifikasi agen yang terlibat dalam proses, peran dan tanggung jawab mereka, serta bagaimana mereka berinteraksi satu sama lain. Pertimbangkan baik agen yang spesifik untuk proses dukungan pelanggan maupun agen umum yang dapat digunakan di bagian lain bisnis Anda.
> Pikirkan sebentar sebelum Anda membaca solusi berikut, Anda mungkin memerlukan lebih banyak agen daripada yang Anda kira.

> TIP: Pikirkan tentang berbagai tahapan proses dukungan pelanggan dan juga pertimbangkan agen yang dibutuhkan untuk sistem apa pun.

## Solution

[Solution](./solution/solution.md)

## Knowledge checks

Question: Kapan Anda harus mempertimbangkan menggunakan multi-agen?

- [ ] A1: Ketika Anda memiliki beban kerja kecil dan tugas sederhana.
- [ ] A2: Ketika Anda memiliki beban kerja besar
- [ ] A3: Ketika Anda memiliki tugas sederhana.

[Solution quiz](./solution/solution-quiz.md)

## Summary

Dalam pelajaran ini, kita telah melihat pola desain multi-agen, termasuk skenario di mana multi-agen dapat diterapkan, keuntungan menggunakan multi-agen dibandingkan agen tunggal, blok bangunan dalam mengimplementasikan pola desain multi-agen, dan bagaimana memiliki visibilitas tentang bagaimana beberapa agen berinteraksi satu sama lain.

### Punya Lebih Banyak Pertanyaan tentang Pola Desain Multi-Agen?

Bergabunglah dengan [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) untuk bertemu dengan pelajar lain, menghadiri jam kantor, dan mendapatkan jawaban atas pertanyaan AI Agents Anda.

## Additional resources

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Dokumentasi Microsoft Agent Framework</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Pola desain agentic</a>


## Previous Lesson

[Planning Design](../07-planning-design/README.md)

## Next Lesson

[Metacognition in AI Agents](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan terjemahan yang akurat, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang salah yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->