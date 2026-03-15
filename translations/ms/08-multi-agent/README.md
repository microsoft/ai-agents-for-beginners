[![Reka Bentuk Multi-Ejen](../../../translated_images/ms/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Klik imej di atas untuk menonton video pelajaran ini)_

# Corak reka bentuk multi-ejen

Sebaik sahaja anda mula bekerja pada projek yang melibatkan berbilang ejen, anda perlu mempertimbangkan corak reka bentuk multi-ejen. Walau bagaimanapun, mungkin tidak jelas bila perlu beralih kepada berbilang ejen dan apakah kelebihannya.

## Pengenalan

Dalam pelajaran ini, kita ingin menjawab soalan-soalan berikut:

- Apakah senario di mana berbilang ejen sesuai digunakan?
- Apakah kelebihan menggunakan berbilang ejen berbanding hanya satu ejen yang melakukan pelbagai tugas?
- Apakah blok pembinaan untuk melaksanakan corak reka bentuk multi-ejen?
- Bagaimana kita mendapat keterlihatan terhadap bagaimana berbilang ejen berinteraksi antara satu sama lain?

## Matlamat Pembelajaran

Selepas pelajaran ini, anda sepatutnya dapat:

- Mengenal pasti senario di mana berbilang ejen sesuai digunakan
- Mengiktiraf kelebihan menggunakan berbilang ejen berbanding satu ejen.
- Memahami blok pembinaan untuk melaksanakan corak reka bentuk multi-ejen.

Apa gambaran besar?

*Berbilang ejen adalah corak reka bentuk yang membolehkan beberapa ejen bekerjasama untuk mencapai matlamat bersama*.

Corak ini digunakan secara meluas dalam pelbagai bidang, termasuk robotik, sistem autonomi, dan pengkomputeran teragih.

## Senario di Mana Berbilang Ejen Sesuai Digunakan

Jadi, apakah senario yang merupakan kes penggunaan yang baik untuk menggunakan berbilang ejen? Jawapannya ialah terdapat banyak senario di mana menggunakan berbilang ejen memberi manfaat terutamanya dalam kes-kes berikut:

- **Beban kerja besar**: Beban kerja besar boleh dibahagikan kepada tugas-tugas kecil dan ditugaskan kepada ejen yang berbeza, membolehkan pemprosesan selari dan penyelesaian yang lebih pantas. Contohnya ialah dalam kes tugas pemprosesan data yang besar.
- **Tugas kompleks**: Tugas kompleks, seperti beban kerja besar, boleh dipecahkan kepada subtugas yang lebih kecil dan ditugaskan kepada ejen yang berlainan, setiap satu mengkhusus dalam aspek tertentu tugas itu. Contoh yang baik ialah dalam kes kenderaan autonomi di mana ejen yang berbeza mengurus navigasi, pengesanan halangan, dan komunikasi dengan kenderaan lain.
- **Kepakaran pelbagai**: Ejen yang berbeza boleh mempunyai kepakaran yang pelbagai, membolehkan mereka mengendalikan aspek yang berbeza bagi sesuatu tugas dengan lebih berkesan daripada satu ejen sahaja. Untuk kes ini, contoh yang baik ialah dalam bidang penjagaan kesihatan di mana ejen boleh mengurus diagnostik, pelan rawatan, dan pemantauan pesakit.

## Kelebihan Menggunakan Berbilang Ejen Berbanding Satu Ejen

Sistem ejen tunggal mungkin berfungsi dengan baik untuk tugas mudah, tetapi untuk tugas yang lebih kompleks, menggunakan berbilang ejen boleh memberikan beberapa kelebihan:

- **Pengkhususan**: Setiap ejen boleh mengkhusus untuk tugas tertentu. Kekurangan pengkhususan dalam satu ejen bermakna anda mempunyai ejen yang boleh melakukan segala-galanya tetapi mungkin keliru mengenai apa yang perlu dilakukan apabila berhadapan dengan tugas yang kompleks. Sebagai contoh, ia mungkin akhirnya melakukan tugas yang bukan kepakarannya.
- **Kebolehskalaan**: Adalah lebih mudah untuk menskala sistem dengan menambah lebih banyak ejen daripada membebankan satu ejen sahaja.
- **Toleransi Ralat**: Jika satu ejen gagal, ejen lain boleh terus berfungsi, memastikan kebolehpercayaan sistem.

Mari kita ambil contoh, mari tempah perjalanan untuk seorang pengguna. Sistem ejen tunggal perlu mengendalikan semua aspek proses tempahan perjalanan, daripada mencari penerbangan hingga menempah hotel dan kereta sewa. Untuk mencapai ini dengan satu ejen, ejen tersebut perlu mempunyai alat untuk mengendalikan semua tugas ini. Ini boleh membawa kepada sistem yang kompleks dan monolitik yang sukar diselenggara dan diskalakan. Sebaliknya, sistem berbilang ejen boleh mempunyai ejen yang berbeza yang mengkhusus dalam mencari penerbangan, menempah hotel, dan kereta sewa. Ini akan menjadikan sistem lebih modular, lebih mudah diselenggara, dan boleh diskalakan.

Bandingkan ini dengan sebuah biro pelancongan yang dijalankan sebagai kedai ibu dan bapa berbanding biro pelancongan yang dijalankan sebagai francais. Kedai ibu dan bapa akan mempunyai satu ejen yang mengendalikan semua aspek proses tempahan perjalanan, manakala francais akan mempunyai ejen yang berbeza mengendalikan aspek berbeza proses tempahan perjalanan.

## Blok Pembinaan untuk Melaksanakan Corak Reka Bentuk Multi-Ejen

Sebelum anda boleh melaksanakan corak reka bentuk multi-ejen, anda perlu memahami blok pembinaan yang membentuk corak itu.

Mari kita jadikan ini lebih konkrit dengan sekali lagi melihat contoh menempah perjalanan untuk seorang pengguna. Dalam kes ini, blok pembinaannya termasuk:

- **Komunikasi Ejen**: Ejen untuk mencari penerbangan, menempah hotel, dan kereta sewa perlu berkomunikasi dan berkongsi maklumat tentang keutamaan dan kekangan pengguna. Anda perlu membuat keputusan mengenai protokol dan kaedah untuk komunikasi ini. Secara konkrit, ini bermakna ejen mencari penerbangan perlu berkomunikasi dengan ejen menempah hotel untuk memastikan hotel ditempah untuk tarikh yang sama dengan penerbangan. Ini bermakna ejen-ejen perlu berkongsi maklumat tentang tarikh perjalanan pengguna, bermakna anda perlu memutuskan *ejen mana yang berkongsi maklumat dan bagaimana mereka berkongsi maklumat*.
- **Mekanisme Penyelarasan**: Ejen perlu menyelaraskan tindakan mereka untuk memastikan keutamaan dan kekangan pengguna dipenuhi. Satu keutamaan pengguna mungkin mereka mahu hotel yang dekat dengan lapangan terbang manakala satu kekangan mungkin kereta sewa hanya tersedia di lapangan terbang. Ini bermakna ejen menempah hotel perlu menyelaraskan dengan ejen menempah kereta sewa untuk memastikan keutamaan dan kekangan pengguna dipenuhi. Ini bermakna anda perlu memutuskan *bagaimana ejen-ejen menyelaraskan tindakan mereka*.
- **Senibina Ejen**: Ejen perlu mempunyai struktur dalaman untuk membuat keputusan dan belajar daripada interaksi mereka dengan pengguna. Ini bermakna ejen mencari penerbangan perlu mempunyai struktur dalaman untuk membuat keputusan tentang penerbangan mana yang hendak dicadangkan kepada pengguna. Ini bermakna anda perlu memutuskan *bagaimana ejen-ejen membuat keputusan dan belajar daripada interaksi mereka dengan pengguna*. Contoh bagaimana ejen belajar dan memperbaiki boleh jadi ejen mencari penerbangan menggunakan model pembelajaran mesin untuk mencadangkan penerbangan kepada pengguna berdasarkan keutamaan lalu mereka.
- **Keterlihatan terhadap Interaksi Berbilang Ejen**: Anda perlu mempunyai keterlihatan terhadap bagaimana berbilang ejen berinteraksi antara satu sama lain. Ini bermakna anda perlu mempunyai alat dan teknik untuk menjejak aktiviti dan interaksi ejen. Ini boleh dalam bentuk alat logging dan pemantauan, alat visualisasi, dan metrik prestasi.
- **Corak Multi-Ejen**: Terdapat corak yang berbeza untuk melaksanakan sistem multi-ejen, seperti senibina berpusat, terdesentralisasi, dan hibrid. Anda perlu memutuskan corak yang paling sesuai dengan kes penggunaan anda.
- **Manusia dalam gelung**: Dalam kebanyakan kes, anda akan mempunyai manusia dalam gelung dan anda perlu mengarahkan ejen bila untuk meminta campur tangan manusia. Ini boleh dalam bentuk pengguna meminta hotel atau penerbangan tertentu yang ejen tidak cadangkan atau meminta pengesahan sebelum menempah penerbangan atau hotel.

## Keterlihatan terhadap Interaksi Berbilang Ejen

Adalah penting bahawa anda mempunyai keterlihatan terhadap bagaimana berbilang ejen berinteraksi antara satu sama lain. Keterlihatan ini penting untuk debugging, mengoptimumkan, dan memastikan keberkesanan keseluruhan sistem. Untuk mencapai ini, anda perlu mempunyai alat dan teknik untuk menjejak aktiviti dan interaksi ejen. Ini boleh dalam bentuk alat logging dan pemantauan, alat visualisasi, dan metrik prestasi.

Sebagai contoh, dalam kes menempah perjalanan untuk seorang pengguna, anda boleh mempunyai papan pemuka yang menunjukkan status setiap ejen, keutamaan dan kekangan pengguna, dan interaksi antara ejen. Papan pemuka ini boleh menunjukkan tarikh perjalanan pengguna, penerbangan yang dicadangkan oleh ejen penerbangan, hotel yang dicadangkan oleh ejen hotel, dan kereta sewa yang dicadangkan oleh ejen kereta sewa. Ini akan memberikan anda gambaran yang jelas tentang bagaimana ejen-ejen berinteraksi antara satu sama lain dan sama ada keutamaan dan kekangan pengguna dipenuhi.

Mari kita lihat setiap aspek ini dengan lebih terperinci.

- **Alat Log dan Pemantauan**: Anda mahu melakukan logging untuk setiap tindakan yang diambil oleh ejen. Satu entri log boleh menyimpan maklumat mengenai ejen yang mengambil tindakan, tindakan yang diambil, masa tindakan diambil, dan hasil tindakan. Maklumat ini kemudian boleh digunakan untuk debugging, pengoptimuman dan lebih banyak lagi.

- **Alat Visualisasi**: Alat visualisasi boleh membantu anda melihat interaksi antara ejen dengan cara yang lebih intuitif. Contohnya, anda boleh mempunyai graf yang menunjukkan aliran maklumat antara ejen. Ini boleh membantu anda mengenal pasti kesesakan, ketidakcekapan, dan isu lain dalam sistem.

- **Metrik Prestasi**: Metrik prestasi boleh membantu anda menjejak keberkesanan sistem multi-ejen. Contohnya, anda boleh menjejak masa yang diambil untuk menyiapkan sesuatu tugas, bilangan tugas yang diselesaikan per unit masa, dan ketepatan cadangan yang dibuat oleh ejen. Maklumat ini boleh membantu anda mengenal pasti bidang untuk penambahbaikan dan mengoptimumkan sistem.

## Corak Multi-Ejen

Mari kita selami beberapa corak konkrit yang boleh kita gunakan untuk mencipta aplikasi multi-ejen. Berikut adalah beberapa corak menarik yang patut dipertimbangkan:

### Sembang berkumpulan

Corak ini berguna apabila anda mahu mencipta aplikasi sembang berkumpulan di mana berbilang ejen boleh berkomunikasi antara satu sama lain. Kes penggunaan biasa untuk corak ini termasuk kerjasama pasukan, sokongan pelanggan, dan rangkaian sosial.

Dalam corak ini, setiap ejen mewakili seorang pengguna dalam sembang berkumpulan, dan mesej ditukar antara ejen menggunakan protokol pemesejan. Ejen boleh menghantar mesej ke sembang berkumpulan, menerima mesej dari sembang berkumpulan, dan membalas mesej daripada ejen lain.

Corak ini boleh dilaksanakan menggunakan senibina berpusat di mana semua mesej dirutekan melalui pelayan pusat, atau senibina terdesentralisasi di mana mesej ditukar secara terus.

![Sembang berkumpulan](../../../translated_images/ms/multi-agent-group-chat.ec10f4cde556babd.webp)

### Penyerahan

Corak ini berguna apabila anda mahu mencipta aplikasi di mana berbilang ejen boleh menyerahkan tugas antara satu sama lain.

Kes penggunaan biasa untuk corak ini termasuk sokongan pelanggan, pengurusan tugas, dan automasi aliran kerja.

Dalam corak ini, setiap ejen mewakili tugas atau langkah dalam aliran kerja, dan ejen boleh menyerahkan tugas kepada ejen lain berdasarkan peraturan yang telah ditetapkan.

![Penyerahan](../../../translated_images/ms/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Penapisan kolaboratif

Corak ini berguna apabila anda mahu mencipta aplikasi di mana berbilang ejen boleh bekerjasama untuk membuat cadangan kepada pengguna.

Mengapa anda mahu berbilang ejen bekerjasama ialah kerana setiap ejen boleh mempunyai kepakaran yang berbeza dan boleh menyumbang kepada proses cadangan dengan cara yang berbeza.

Mari kita ambil contoh di mana seorang pengguna mahukan cadangan tentang saham terbaik untuk dibeli di pasaran saham.

- **Pakar industri**: Satu ejen boleh menjadi pakar dalam industri tertentu.
- **Analisis teknikal**: Satu lagi ejen boleh menjadi pakar dalam analisis teknikal.
- **Analisis fundamental**: Dan satu lagi ejen boleh menjadi pakar dalam analisis fundamental. Dengan bekerjasama, ejen-ejen ini boleh memberikan cadangan yang lebih menyeluruh kepada pengguna.

![Cadangan](../../../translated_images/ms/multi-agent-filtering.d959cb129dc9f608.webp)

## Senario: Proses bayaran balik

Pertimbangkan senario di mana seorang pelanggan cuba mendapatkan bayaran balik untuk produk, boleh terdapat beberapa ejen yang terlibat dalam proses ini tetapi mari kita bahagikan antara ejen yang khusus untuk proses ini dan ejen umum yang boleh digunakan dalam proses lain.

**Ejen khusus untuk proses bayaran balik**:

Berikut adalah beberapa ejen yang boleh terlibat dalam proses bayaran balik:

- **Ejen pelanggan**: Ejen ini mewakili pelanggan dan bertanggungjawab untuk memulakan proses bayaran balik.
- **Ejen penjual**: Ejen ini mewakili penjual dan bertanggungjawab untuk memproses bayaran balik.
- **Ejen pembayaran**: Ejen ini mewakili proses pembayaran dan bertanggungjawab untuk mengembalikan pembayaran kepada pelanggan.
- **Ejen resolusi**: Ejen ini mewakili proses penyelesaian dan bertanggungjawab untuk menyelesaikan sebarang isu yang timbul semasa proses bayaran balik.
- **Ejen pematuhan**: Ejen ini mewakili proses pematuhan dan bertanggungjawab untuk memastikan proses bayaran balik mematuhi peraturan dan dasar.

**Ejen umum**:

Ejen-ejen ini boleh digunakan oleh bahagian lain dalam perniagaan anda.

- **Ejen penghantaran**: Ejen ini mewakili proses penghantaran dan bertanggungjawab untuk menghantar produk kembali kepada penjual. Ejen ini boleh digunakan untuk proses bayaran balik dan untuk penghantaran produk am melalui pembelian, contohnya.
- **Ejen maklum balas**: Ejen ini mewakili proses maklum balas dan bertanggungjawab untuk mengumpul maklum balas daripada pelanggan. Maklum balas boleh diambil pada bila-bila masa dan bukan hanya semasa proses bayaran balik.
- **Ejen pengeskalan**: Ejen ini mewakili proses pengeskalan dan bertanggungjawab untuk meningkatkan isu kepada tahap sokongan yang lebih tinggi. Anda boleh menggunakan jenis ejen ini untuk mana-mana proses di mana anda perlu meningkatkan isu.
- **Ejen notifikasi**: Ejen ini mewakili proses notifikasi dan bertanggungjawab untuk menghantar notifikasi kepada pelanggan pada pelbagai peringkat proses bayaran balik.
- **Ejen analitik**: Ejen ini mewakili proses analitik dan bertanggungjawab untuk menganalisis data berkaitan proses bayaran balik.
- **Ejen audit**: Ejen ini mewakili proses audit dan bertanggungjawab untuk mengaudit proses bayaran balik untuk memastikan ia dijalankan dengan betul.
- **Ejen laporan**: Ejen ini mewakili proses pelaporan dan bertanggungjawab untuk menghasilkan laporan mengenai proses bayaran balik.
- **Ejen pengetahuan**: Ejen ini mewakili proses pengetahuan dan bertanggungjawab untuk menyelenggara pangkalan pengetahuan mengenai maklumat berkaitan proses bayaran balik. Ejen ini boleh berpengetahuan tentang bayaran balik dan bahagian lain dalam perniagaan anda.
- **Ejen keselamatan**: Ejen ini mewakili proses keselamatan dan bertanggungjawab untuk memastikan keselamatan proses bayaran balik.
- **Ejen kualiti**: Ejen ini mewakili proses kualiti dan bertanggungjawab untuk memastikan kualiti proses bayaran balik.

Terdapat banyak ejen disenaraikan sebelum ini sama ada untuk proses bayaran balik khusus tetapi juga untuk ejen umum yang boleh digunakan dalam bahagian lain perniagaan anda. Diharapkan ini memberi anda idea mengenai bagaimana anda boleh membuat keputusan mengenai ejen mana yang akan digunakan dalam sistem multi-ejen anda.

## Tugasan

Reka sebuah sistem multi-ejen untuk proses sokongan pelanggan. Kenal pasti ejen-ejen yang terlibat dalam proses, peranan dan tanggungjawab mereka, dan bagaimana mereka berinteraksi antara satu sama lain. Pertimbangkan kedua-dua ejen yang khusus untuk proses sokongan pelanggan dan ejen umum yang boleh digunakan dalam bahagian lain perniagaan anda.
> Fikirkan dahulu sebelum anda membaca penyelesaian berikut, anda mungkin memerlukan lebih banyak ejen daripada yang anda fikirkan.
>
> PETUA: Fikirkan tentang peringkat berbeza dalam proses sokongan pelanggan dan juga pertimbangkan ejen yang diperlukan untuk mana-mana sistem.

## Penyelesaian

[Pen​yelesaian](./solution/solution.md)

## Pemeriksaan Pengetahuan

Question: When should you consider using multi-agents?

- [ ] A1: Apabila anda mempunyai beban kerja yang kecil dan tugasan yang mudah.
- [ ] A2: Apabila anda mempunyai beban kerja yang besar
- [ ] A3: Apabila anda mempunyai tugasan yang mudah.

[Kuiz penyelesaian](./solution/solution-quiz.md)

## Ringkasan

Dalam pelajaran ini, kita telah melihat corak reka bentuk berbilang ejen, termasuk senario di mana berbilang ejen boleh digunakan, kelebihan menggunakan berbilang ejen berbanding ejen tunggal, blok pembinaan untuk melaksanakan corak reka bentuk berbilang ejen, dan bagaimana untuk mendapatkan keterlihatan tentang bagaimana pelbagai ejen berinteraksi antara satu sama lain.

### Ada Lagi Soalan mengenai Corak Reka Bentuk Berbilang Ejen?

Join the [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) to meet with other learners, attend office hours and get your AI Agents questions answered.

## Sumber tambahan

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Dokumentasi Rangka Kerja Ejen Microsoft</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Corak reka bentuk agentik</a>


## Pelajaran Sebelumnya

[Perancangan Reka Bentuk](../07-planning-design/README.md)

## Pelajaran Seterusnya

[Metakognisi dalam Ejen AI](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya hendaklah dianggap sebagai sumber rujukan yang muktamad. Untuk maklumat yang kritikal, disyorkan mendapatkan terjemahan profesional oleh penterjemah manusia. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->