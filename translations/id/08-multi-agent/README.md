[![Desain Multi-Agen](../../../translated_images/id/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Klik gambar di atas untuk menonton video pelajaran ini)_

# Pola desain multi-agen

Begitu Anda mulai mengerjakan proyek yang melibatkan beberapa agen, Anda perlu mempertimbangkan pola desain multi-agen. Namun, mungkin tidak langsung jelas kapan harus beralih ke multi-agen dan apa keuntungannya.

## Pendahuluan

Dalam pelajaran ini, kita ingin menjawab pertanyaan-pertanyaan berikut:

- Apa saja skenario di mana multi-agen dapat diterapkan?
- Apa keuntungan menggunakan multi-agen dibandingkan hanya satu agen tunggal yang melakukan banyak tugas?
- Apa saja blok bangunan dalam mengimplementasikan pola desain multi-agen?
- Bagaimana kita dapat melihat bagaimana beberapa agen berinteraksi satu sama lain?

## Tujuan Pembelajaran

Setelah pelajaran ini, Anda seharusnya dapat:

- Mengidentifikasi skenario di mana multi-agen dapat diterapkan
- Mengenali keuntungan menggunakan multi-agen dibandingkan agen tunggal.
- Memahami blok bangunan dalam mengimplementasikan pola desain multi-agen.

Apa gambaran besarnya?

*Multi agen adalah pola desain yang memungkinkan beberapa agen bekerja sama untuk mencapai tujuan bersama*.

Pola ini banyak digunakan di berbagai bidang, termasuk robotika, sistem otonom, dan komputasi terdistribusi.

## Skenario di mana Multi-Agen Dapat Diterapkan

Jadi, skenario apa saja yang merupakan kasus penggunaan yang baik untuk menggunakan multi-agen? Jawabannya adalah ada banyak skenario di mana penggunaan beberapa agen menguntungkan terutama dalam kasus berikut:

- **Beban kerja besar**: Beban kerja besar dapat dibagi menjadi tugas-tugas kecil dan dialokasikan ke agen berbeda, memungkinkan pemrosesan paralel dan penyelesaian lebih cepat. Contohnya adalah pada tugas pemrosesan data besar.
- **Tugas kompleks**: Tugas kompleks, seperti beban kerja besar, dapat dipecah menjadi subtugas yang lebih kecil dan dialokasikan ke agen berbeda, masing-masing mengkhususkan diri pada aspek tertentu dari tugas tersebut. Contoh yang baik adalah pada kendaraan otonom di mana agen berbeda mengelola navigasi, deteksi rintangan, dan komunikasi dengan kendaraan lain.
- **Keahlian beragam**: Agen berbeda dapat memiliki keahlian beragam, memungkinkan mereka menangani aspek tugas yang berbeda lebih efektif daripada satu agen tunggal. Contoh untuk kasus ini adalah di bidang kesehatan di mana agen dapat mengelola diagnosis, rencana perawatan, dan pemantauan pasien.

## Keuntungan Menggunakan Multi-Agen Dibanding Agen Tunggal

Sistem agen tunggal bisa bekerja dengan baik untuk tugas sederhana, tetapi untuk tugas yang lebih kompleks, menggunakan beberapa agen dapat memberikan beberapa keuntungan:

- **Spesialisasi**: Setiap agen dapat berspesialisasi untuk tugas tertentu. Kurangnya spesialisasi pada agen tunggal berarti Anda memiliki agen yang bisa melakukan segala hal tetapi bisa bingung saat menghadapi tugas kompleks. Misalnya, bisa saja ia akhirnya melakukan tugas yang tidak paling cocok untuknya.
- **Skalabilitas**: Lebih mudah untuk menskalakan sistem dengan menambahkan lebih banyak agen daripada membebani satu agen saja.
- **Toleransi Kesalahan**: Jika satu agen gagal, agen lain bisa terus berfungsi, memastikan keandalan sistem.

Mari kita ambil contoh, kita memesan perjalanan untuk seorang pengguna. Sistem agen tunggal harus menangani semua aspek proses pemesanan perjalanan, mulai dari mencari penerbangan hingga memesan hotel dan mobil sewaan. Untuk mencapai ini dengan satu agen tunggal, agen tersebut perlu memiliki alat untuk menangani semua tugas ini. Ini bisa menghasilkan sistem yang kompleks dan monolitik yang sulit dipelihara dan diskalakan. Sistem multi-agen, sebaliknya, bisa memiliki agen berbeda yang berspesialisasi dalam mencari penerbangan, memesan hotel, dan mobil sewaan. Ini membuat sistem lebih modular, lebih mudah dipelihara, dan skalabel.

Bandingkan ini dengan biro perjalanan yang dijalankan sebagai toko kecil keluarga versus biro perjalanan yang dijalankan sebagai waralaba. Toko kecil keluarga akan memiliki satu agen yang menangani semua aspek proses pemesanan perjalanan, sementara waralaba memiliki agen berbeda yang menangani aspek-aspek berbeda dari proses pemesanan perjalanan.

## Blok Bangunan Mengimplementasikan Pola Desain Multi-Agen

Sebelum Anda dapat mengimplementasikan pola desain multi-agen, Anda perlu memahami blok bangunan yang membentuk pola tersebut.

Mari kita buat ini lebih konkret dengan kembali melihat contoh pemesanan perjalanan untuk pengguna. Dalam kasus ini, blok bangunan akan mencakup:

- **Komunikasi Agen**: Agen untuk mencari penerbangan, memesan hotel, dan mobil sewaan perlu berkomunikasi dan berbagi informasi tentang preferensi dan batasan pengguna. Anda perlu memutuskan protokol dan metode untuk komunikasi ini. Artinya secara konkret adalah agen untuk mencari penerbangan perlu berkomunikasi dengan agen pemesan hotel untuk memastikan hotel dipesan pada tanggal yang sama dengan penerbangan. Itu berarti agen harus saling berbagi informasi tentang tanggal perjalanan pengguna, artinya Anda perlu memutuskan *agen mana yang berbagi info dan bagaimana mereka berbagi info*.
- **Mekanisme Koordinasi**: Agen perlu mengoordinasikan tindakannya untuk memastikan preferensi dan batasan pengguna terpenuhi. Preferensi pengguna bisa jadi ingin hotel dekat bandara sedangkan batasan bisa jadi mobil sewaan hanya tersedia di bandara. Ini berarti agen pemesan hotel perlu berkoordinasi dengan agen pemesan mobil sewaan untuk memastikan preferensi dan batasan pengguna terpenuhi. Ini berarti Anda perlu memutuskan *bagaimana agen mengoordinasikan tindakan mereka*.
- **Arsitektur Agen**: Agen perlu memiliki struktur internal untuk membuat keputusan dan belajar dari interaksi mereka dengan pengguna. Ini berarti agen pencari penerbangan perlu memiliki struktur internal untuk membuat keputusan tentang penerbangan mana yang direkomendasikan kepada pengguna. Ini berarti Anda perlu memutuskan *bagaimana agen membuat keputusan dan belajar dari interaksi dengan pengguna*. Contohnya bagaimana agen belajar dan meningkat bisa jadi agen pencari penerbangan menggunakan model pembelajaran mesin untuk merekomendasikan penerbangan kepada pengguna berdasarkan preferensi sebelumnya.
- **Visibilitas Interaksi Multi-Agen**: Anda perlu memiliki visibilitas bagaimana beberapa agen berinteraksi satu sama lain. Ini berarti Anda harus memiliki alat dan teknik untuk melacak aktivitas dan interaksi agen. Ini bisa berupa alat pencatatan dan pemantauan, alat visualisasi, dan metrik kinerja.
- **Pola Multi-Agen**: Ada pola berbeda untuk mengimplementasikan sistem multi-agen, seperti arsitektur terpusat, terdesentralisasi, dan hibrid. Anda perlu memutuskan pola yang paling cocok untuk kasus penggunaan Anda.
- **Manusia dalam loop**: Dalam kebanyakan kasus, Anda akan memiliki manusia dalam loop dan Anda perlu menginstruksikan agen kapan harus meminta intervensi manusia. Ini bisa berupa pengguna yang meminta hotel atau penerbangan tertentu yang agen belum rekomendasikan atau meminta konfirmasi sebelum memesan penerbangan atau hotel.

## Visibilitas Interaksi Multi-Agen

Penting bahwa Anda memiliki visibilitas bagaimana beberapa agen berinteraksi satu sama lain. Visibilitas ini penting untuk debugging, pengoptimalan, dan memastikan efektivitas keseluruhan sistem. Untuk mencapai ini, Anda perlu memiliki alat dan teknik untuk melacak aktivitas dan interaksi agen. Ini bisa berupa alat pencatatan dan pemantauan, alat visualisasi, dan metrik kinerja.

Misalnya, dalam kasus pemesanan perjalanan untuk pengguna, Anda bisa memiliki dasbor yang menunjukkan status setiap agen, preferensi dan batasan pengguna, serta interaksi antar agen. Dasbor ini bisa menunjukkan tanggal perjalanan pengguna, penerbangan yang direkomendasikan oleh agen penerbangan, hotel yang direkomendasikan oleh agen hotel, dan mobil sewaan yang direkomendasikan oleh agen mobil sewaan. Ini akan memberi Anda pandangan jelas bagaimana agen berinteraksi satu sama lain dan apakah preferensi serta batasan pengguna terpenuhi.

Mari kita lihat setiap aspek ini lebih rinci.

- **Alat Pencatatan dan Pemantauan**: Anda ingin melakukan pencatatan untuk setiap tindakan yang diambil agen. Entri log bisa menyimpan informasi tentang agen yang mengambil tindakan, tindakan yang diambil, waktu tindakan dilakukan, dan hasil dari tindakan tersebut. Informasi ini kemudian bisa digunakan untuk debugging, pengoptimalan, dan lainnya.

- **Alat Visualisasi**: Alat visualisasi dapat membantu Anda melihat interaksi antar agen dengan cara yang lebih intuitif. Misalnya, Anda bisa memiliki grafik yang menunjukkan aliran informasi antar agen. Ini bisa membantu Anda mengidentifikasi hambatan, ketidakefisienan, dan masalah lain dalam sistem.

- **Metrik Kinerja**: Metrik kinerja dapat membantu Anda melacak efektivitas sistem multi-agen. Misalnya, Anda bisa melacak waktu yang dibutuhkan untuk menyelesaikan tugas, jumlah tugas yang selesai per satuan waktu, dan akurasi rekomendasi yang dibuat agen. Informasi ini membantu Anda mengidentifikasi area untuk perbaikan dan mengoptimalkan sistem.

## Pola Multi-Agen

Mari kita bahas beberapa pola konkret yang bisa kita gunakan untuk membuat aplikasi multi-agen. Berikut beberapa pola menarik yang layak dipertimbangkan:

### Obrolan grup

Pola ini berguna ketika Anda ingin membuat aplikasi obrolan grup di mana beberapa agen dapat saling berkomunikasi. Kasus penggunaan tipikal untuk pola ini termasuk kolaborasi tim, dukungan pelanggan, dan jejaring sosial.

Dalam pola ini, setiap agen mewakili pengguna dalam obrolan grup, dan pesan dipertukarkan antar agen menggunakan protokol pengiriman pesan. Agen dapat mengirim pesan ke obrolan grup, menerima pesan dari obrolan grup, dan merespons pesan dari agen lain.

Pola ini bisa diimplementasikan menggunakan arsitektur terpusat di mana semua pesan diarahkan melalui server pusat, atau arsitektur terdesentralisasi di mana pesan dipertukarkan langsung.

![Obrolan grup](../../../translated_images/id/multi-agent-group-chat.ec10f4cde556babd.webp)

### Penyerahan tugas (Hand-off)

Pola ini berguna ketika Anda ingin membuat aplikasi di mana beberapa agen bisa menyerahkan tugas ke agen lain.

Kasus penggunaan tipikal pola ini termasuk dukungan pelanggan, manajemen tugas, dan otomatisasi alur kerja.

Dalam pola ini, setiap agen mewakili tugas atau langkah dalam alur kerja, dan agen dapat menyerahkan tugas ke agen lain berdasarkan aturan yang telah ditetapkan.

![Penyerahan tugas](../../../translated_images/id/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Penyaringan kolaboratif

Pola ini berguna ketika Anda ingin membuat aplikasi di mana beberapa agen dapat bekerja sama untuk memberikan rekomendasi kepada pengguna.

Alasan Anda ingin beberapa agen berkolaborasi adalah karena setiap agen dapat memiliki keahlian berbeda dan dapat berkontribusi dalam proses rekomendasi dengan cara berbeda.

Mari ambil contoh di mana seorang pengguna ingin rekomendasi saham terbaik untuk dibeli di pasar saham.

- **Ahli industri**: Satu agen bisa menjadi ahli di industri tertentu.
- **Analisis teknis**: Agen lain bisa ahli dalam analisis teknis.
- **Analisis fundamental**: dan agen lain bisa ahli dalam analisis fundamental. Dengan berkolaborasi, agen-agen ini bisa memberikan rekomendasi yang lebih komprehensif kepada pengguna.

![Rekomendasi](../../../translated_images/id/multi-agent-filtering.d959cb129dc9f608.webp)

## Skenario: Proses pengembalian dana

Pertimbangkan skenario di mana pelanggan mencoba mendapatkan pengembalian dana untuk sebuah produk, ada cukup banyak agen yang terlibat dalam proses ini tapi mari kita bagi antara agen spesifik untuk proses ini dan agen umum yang bisa digunakan di proses lain.

**Agen spesifik untuk proses pengembalian dana**:

Berikut ini beberapa agen yang bisa terlibat dalam proses pengembalian dana:

- **Agen pelanggan**: Agen ini mewakili pelanggan dan bertanggung jawab memulai proses pengembalian dana.
- **Agen penjual**: Agen ini mewakili penjual dan bertanggung jawab memproses pengembalian dana.
- **Agen pembayaran**: Agen ini mewakili proses pembayaran dan bertanggung jawab mengembalikan pembayaran kepada pelanggan.
- **Agen penyelesaian**: Agen ini mewakili proses penyelesaian dan bertanggung jawab menyelesaikan masalah yang muncul selama proses pengembalian dana.
- **Agen kepatuhan**: Agen ini mewakili proses kepatuhan dan bertanggung jawab memastikan proses pengembalian dana sesuai dengan peraturan dan kebijakan.

**Agen umum**:

Agen-agen ini dapat digunakan oleh bagian lain dari bisnis Anda.

- **Agen pengiriman**: Agen ini mewakili proses pengiriman dan bertanggung jawab mengirim produk kembali ke penjual. Agen ini bisa digunakan baik untuk proses pengembalian dana maupun pengiriman produk secara umum melalui pembelian misalnya.
- **Agen umpan balik**: Agen ini mewakili proses pengumpulan umpan balik dari pelanggan. Umpan balik bisa diberikan kapan saja, tidak hanya saat proses pengembalian dana.
- **Agen eskalasi**: Agen ini mewakili proses eskalasi dan bertanggung jawab menaikkan isu ke tingkat dukungan yang lebih tinggi. Anda dapat menggunakan jenis agen ini untuk proses apapun yang perlu eskalasi masalah.
- **Agen notifikasi**: Agen ini mewakili proses pemberitahuan dan bertanggung jawab mengirimkan notifikasi ke pelanggan di berbagai tahap proses pengembalian dana.
- **Agen analitik**: Agen ini mewakili proses analitik dan bertanggung jawab menganalisis data terkait proses pengembalian dana.
- **Agen audit**: Agen ini mewakili proses audit dan bertanggung jawab mengaudit proses pengembalian dana untuk memastikan pelaksanaannya benar.
- **Agen pelaporan**: Agen ini mewakili proses pelaporan dan bertanggung jawab membuat laporan tentang proses pengembalian dana.
- **Agen pengetahuan**: Agen ini mewakili proses pengetahuan dan bertanggung jawab memelihara basis pengetahuan informasi terkait proses pengembalian dana. Agen ini mungkin berpengetahuan baik tentang pengembalian dana maupun bagian lain dari bisnis Anda.
- **Agen keamanan**: Agen ini mewakili proses keamanan dan bertanggung jawab menjamin keamanan proses pengembalian dana.
- **Agen kualitas**: Agen ini mewakili proses kualitas dan bertanggung jawab memastikan kualitas proses pengembalian dana.

Ada cukup banyak agen yang telah disebutkan sebelumnya baik untuk proses pengembalian dana spesifik maupun agen umum yang dapat digunakan di bagian lain bisnis Anda. Harapannya ini memberi Anda gambaran bagaimana Anda dapat memutuskan agen mana yang digunakan dalam sistem multi-agen Anda.

## Tugas

Rancang sistem multi-agen untuk proses dukungan pelanggan. Identifikasi agen yang terlibat dalam proses, peran dan tanggung jawab mereka, serta bagaimana mereka berinteraksi satu sama lain. Pertimbangkan baik agen yang spesifik untuk proses dukungan pelanggan dan agen umum yang dapat digunakan di bagian lain bisnis Anda.


> Pikirkan dulu sebelum Anda membaca solusi berikut, Anda mungkin membutuhkan lebih banyak agen daripada yang Anda kira.

> TIP: Pikirkan tentang tahapan berbeda dari proses dukungan pelanggan dan juga pertimbangkan agen yang dibutuhkan untuk setiap sistem.

## Solusi

[Solusi](./solution/solution.md)

## Pemeriksaan Pengetahuan

### Pertanyaan 1

Skenario mana yang paling cocok untuk sistem multi-agen?

- [ ] A1: Bot dukungan menjawab pertanyaan umum menggunakan satu basis pengetahuan dan satu set alat kecil.
- [ ] A2: Alur kerja pengembalian memerlukan peran terpisah untuk penipuan, pembayaran, dan kepatuhan, masing-masing dengan alatnya sendiri, dan hasilnya harus dikoordinasikan.
- [ ] A3: Permintaan klasifikasi sederhana yang sama datang ribuan kali per jam.

### Pertanyaan 2

Kapan agen tunggal biasanya pilihan yang lebih baik?

- [ ] A1: Tugas dapat ditangani dengan satu set instruksi dan alat, tanpa alih tangan spesialis.
- [ ] A2: Agen memiliki akses ke lebih dari satu alat.
- [ ] A3: Alur kerja memerlukan peran terpisah dengan izin berbeda dan jejak audit independen.

[Kuis solusi](./solution/solution-quiz.md)

## Ringkasan

Dalam pelajaran ini, kita telah melihat pola desain multi-agen, termasuk skenario di mana multi-agen berlaku, keuntungan menggunakan multi-agen dibanding agen tunggal, blok bangunan untuk mengimplementasikan pola desain multi-agen, dan bagaimana memiliki visibilitas ke dalam cara banyak agen saling berinteraksi.

### Punya Pertanyaan Lebih Banyak tentang Pola Desain Multi-Agen?

Bergabunglah dengan [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) untuk bertemu dengan pelajar lain, menghadiri jam kantor, dan dapatkan pertanyaan tentang Agen AI Anda dijawab.

## Sumber Tambahan

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Dokumentasi Microsoft Agent Framework</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Pola desain agentik</a>


## Pelajaran Sebelumnya

[Perencanaan Desain](../07-planning-design/README.md)

## Pelajaran Berikutnya

[Metakognisi dalam Agen AI](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->