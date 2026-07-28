[![Reka Bentuk Multi-Ejen](../../../translated_images/ms/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Klik imej di atas untuk menonton video pelajaran ini)_

# Corak reka bentuk multi-ejen

Sebaik sahaja anda mula bekerja pada projek yang melibatkan pelbagai ejen, anda perlu mempertimbangkan corak reka bentuk multi-ejen. Walau bagaimanapun, mungkin tidak serta-merta jelas bila hendak beralih kepada multi-ejen dan apakah kelebihannya.

## Pengenalan

Dalam pelajaran ini, kita ingin menjawab soalan-soalan berikut:

- Apakah senario di mana multi-ejen boleh digunakan?
- Apakah kelebihan menggunakan multi-ejen berbanding hanya satu ejen tunggal yang melakukan pelbagai tugas?
- Apakah blok binaan untuk melaksanakan corak reka bentuk multi-ejen?
- Bagaimana kita dapat melihat bagaimana pelbagai ejen berinteraksi antara satu sama lain?

## Matlamat Pembelajaran

Selepas pelajaran ini, anda sepatutnya dapat:

- Mengenal pasti senario di mana multi-ejen boleh digunakan
- Mengiktiraf kelebihan menggunakan multi-ejen berbanding ejen tunggal.
- Memahami blok binaan pelaksanaan corak reka bentuk multi-ejen.

Apakah gambaran besar?

*Multi-ejen adalah corak reka bentuk yang membolehkan pelbagai ejen bekerja bersama untuk mencapai matlamat bersama*.

Corak ini banyak digunakan dalam pelbagai bidang, termasuk robotik, sistem autonomi, dan pengkomputeran teragih.

## Senario Di Mana Multi-Ejen Boleh Digunakan

Jadi, apakah senario yang sesuai untuk penggunaan multi-ejen? Jawapannya ialah terdapat banyak senario di mana menggunakan pelbagai ejen adalah bermanfaat terutamanya dalam kes berikut:

- **Beban kerja besar**: Beban kerja besar boleh dibahagikan kepada tugas-tugas kecil dan ditugaskan kepada ejen yang berbeza, membolehkan pemprosesan selari dan penyelesaian lebih cepat. Contohnya ialah dalam kes tugas pemprosesan data besar.
- **Tugas kompleks**: Tugas kompleks, seperti beban kerja besar, boleh dipecahkan kepada sub-tugas lebih kecil dan ditugaskan kepada ejen yang berbeza, masing-masing mengkhusus dalam aspek tertentu tugas tersebut. Contoh yang baik ialah dalam kes kenderaan autonomi di mana ejen berbeza menguruskan navigasi, pengesanan halangan, dan komunikasi dengan kenderaan lain.
- **Kepakaran pelbagai**: Ejen yang berbeza boleh mempunyai kepakaran berbeza, membolehkan mereka mengendalikan aspek tugas yang berbeza dengan lebih efektif berbanding satu ejen sahaja. Dalam kes penjagaan kesihatan, ejen boleh menguruskan diagnostik, pelan rawatan, dan pemantauan pesakit.

## Kelebihan Menggunakan Multi-Ejen Berbanding Ejen Tunggal

Sistem ejen tunggal boleh berfungsi dengan baik untuk tugas mudah, tetapi untuk tugas yang lebih kompleks, menggunakan pelbagai ejen dapat memberikan beberapa kelebihan:

- **Pengkhususan**: Setiap ejen boleh mengkhusus untuk tugas tertentu. Kekurangan pengkhususan dalam satu ejen bermakna anda mempunyai ejen yang boleh melakukan semuanya tetapi mungkin keliru apa yang perlu dilakukan apabila berhadapan dengan tugas kompleks. Contohnya, ia mungkin akhirnya melakukan tugas yang tidak sesuai dengannya.
- **Skalabiliti**: Lebih mudah untuk menskalakan sistem dengan menambah lebih banyak ejen berbanding membebankan satu ejen.
- **Ketahanan Kesalahan**: Jika satu ejen gagal, ejen lain boleh terus berfungsi, memastikan kebolehpercayaan sistem.

Mari kita ambil contoh, mari tempah perjalanan untuk pengguna. Sistem ejen tunggal perlu mengendalikan semua aspek proses tempahan perjalanan, daripada mencari penerbangan hingga menempah hotel dan kereta sewa. Untuk mencapai ini dengan ejen tunggal, ejen tersebut perlu mempunyai alat untuk mengendalikan semua tugas ini. Ini boleh membawa kepada sistem yang kompleks dan monolitik yang sukar untuk diselenggara dan diskala. Sebaliknya, sistem multi-ejen boleh mempunyai ejen yang berbeza khusus untuk mencari penerbangan, menempah hotel, dan kereta sewa. Ini menjadikan sistem lebih modular, mudah diselenggara, dan boleh diskala.

Bandingkan dengan biro perjalanan yang diuruskan sebagai kedai kecil keluarga berbanding biro perjalanan yang dijalankan sebagai francais. Kedai kecil keluarga mempunyai satu ejen yang mengendalikan semua aspek proses tempahan perjalanan, manakala francais mempunyai ejen berbeza yang mengendalikan aspek yang berbeza proses tempahan perjalanan.

## Blok Binaan Pelaksanaan Corak Reka Bentuk Multi-Ejen

Sebelum anda boleh melaksanakan corak reka bentuk multi-ejen, anda perlu memahami blok binaan yang membentuk corak tersebut.

Mari kita jadikan ini lebih nyata dengan sekali lagi melihat contoh menempah perjalanan untuk pengguna. Dalam kes ini, blok binaan termasuk:

- **Komunikasi Ejen**: Ejen untuk mencari penerbangan, menempah hotel, dan kereta sewa perlu berkomunikasi dan berkongsi maklumat tentang keutamaan dan kekangan pengguna. Anda perlu memutuskan protokol dan kaedah komunikasi ini. Secara konkrit, ejen untuk mencari penerbangan perlu berkomunikasi dengan ejen untuk menempah hotel untuk memastikan hotel ditempah untuk tarikh yang sama dengan penerbangan. Ini bermakna ejen perlu berkongsi maklumat tentang tarikh perjalanan pengguna, yang bermakna anda perlu memutuskan *ejen mana berkongsi maklumat dan bagaimana mereka berkongsi maklumat*.
- **Mekanisme Penyelarasan**: Ejen perlu menyelaraskan tindakan mereka untuk memastikan keutamaan dan kekangan pengguna dipenuhi. Keutamaan pengguna boleh jadi mereka mahu hotel yang dekat dengan lapangan terbang manakala kekangan boleh jadi kereta sewa hanya tersedia di lapangan terbang. Ini bermakna ejen untuk menempah hotel perlu menyelaraskan dengan ejen menempah kereta sewa untuk memastikan keutamaan dan kekangan pengguna dipenuhi. Ini bermakna anda perlu memutuskan *bagaimana ejen menyelaraskan tindakan mereka*.
- **Senibina Ejen**: Ejen perlu mempunyai struktur dalaman untuk membuat keputusan dan belajar daripada interaksi mereka dengan pengguna. Ini bermakna ejen untuk mencari penerbangan perlu mempunyai struktur dalaman untuk membuat keputusan tentang penerbangan mana yang hendak disyorkan kepada pengguna. Ini bermakna anda perlu memutuskan *bagaimana ejen membuat keputusan dan belajar daripada interaksi mereka dengan pengguna*. Contoh bagaimana ejen belajar dan memperbaiki mungkin ejen mencari penerbangan menggunakan model pembelajaran mesin untuk menyarankan penerbangan berdasarkan keutamaan lalu pengguna.
- **Keterlihatan dalam Interaksi Multi-Ejen**: Anda perlu mempunyai keterlihatan tentang bagaimana pelbagai ejen berinteraksi antara satu sama lain. Ini bermakna anda perlu mempunyai alat dan teknik untuk menjejak aktiviti dan interaksi ejen. Ini boleh berbentuk alat log dan pemantauan, alat visualisasi, dan metrik prestasi.
- **Corak Multi-Ejen**: Terdapat pelbagai corak untuk melaksanakan sistem multi-ejen, seperti senibina berpusat, tidak berpusat, dan hibrid. Anda perlu memilih corak yang paling sesuai dengan kes penggunaan anda.
- **Manusia dalam gelung**: Dalam kebanyakan kes, anda akan mempunyai manusia dalam gelung dan perlu memberi arahan kepada ejen bila hendak minta campur tangan manusia. Ini boleh berbentuk pengguna meminta hotel atau penerbangan spesifik yang ejen belum syorkan atau meminta pengesahan sebelum menempah penerbangan atau hotel.

## Keterlihatan dalam Interaksi Multi-Ejen

Penting untuk anda mempunyai keterlihatan tentang bagaimana pelbagai ejen berinteraksi antara satu sama lain. Keterlihatan ini penting untuk pengesanan ralat, pengoptimuman, dan memastikan keberkesanan keseluruhan sistem. Untuk mencapainya, anda perlu mempunyai alat dan teknik untuk menjejak aktiviti dan interaksi ejen. Ini boleh berbentuk alat log dan pemantauan, alat visualisasi, dan metrik prestasi.

Contohnya, dalam kes menempah perjalanan untuk pengguna, anda boleh mempunyai papan pemuka yang menunjukkan status setiap ejen, keutamaan dan kekangan pengguna, dan interaksi antara ejen. Papan pemuka ini boleh menunjukkan tarikh perjalanan pengguna, penerbangan yang disyorkan oleh ejen penerbangan, hotel yang disyorkan oleh ejen hotel, dan kereta sewa yang disyorkan oleh ejen kereta sewa. Ini memberikan anda gambaran jelas bagaimana ejen berinteraksi antara satu sama lain dan sama ada keutamaan serta kekangan pengguna dipenuhi.

Mari kita lihat setiap aspek ini dengan lebih terperinci.

- **Alat Log dan Pemantauan**: Anda mahu log dibuat untuk setiap tindakan yang diambil oleh ejen. Entri log boleh menyimpan maklumat tentang ejen yang mengambil tindakan, tindakan yang diambil, masa tindakan diambil, dan hasil tindakan. Maklumat ini boleh digunakan untuk pengesanan ralat, pengoptimuman, dan lain-lain.

- **Alat Visualisasi**: Alat visualisasi boleh membantu anda melihat interaksi antara ejen dengan cara yang lebih intuitif. Contohnya, anda boleh mempunyai graf yang menunjukkan aliran maklumat antara ejen. Ini boleh membantu mengenal pasti kesesakan, ketidakcekapan, dan isu lain dalam sistem.

- **Metrik Prestasi**: Metrik prestasi boleh membantu anda menjejak keberkesanan sistem multi-ejen. Contohnya, anda boleh menjejak masa yang diambil untuk menyelesaikan tugas, jumlah tugas diselesaikan setiap unit masa, dan ketepatan cadangan yang dibuat oleh ejen. Maklumat ini boleh membantu mengenal pasti kawasan untuk penambahbaikan dan mengoptimumkan sistem.

## Corak Multi-Ejen

Mari menyelami beberapa corak konkrit yang boleh digunakan untuk mencipta aplikasi multi-ejen. Berikut adalah beberapa corak menarik yang patut dipertimbangkan:

### Sembang kumpulan

Corak ini berguna apabila anda ingin membuat aplikasi sembang kumpulan di mana banyak ejen boleh berkomunikasi antara satu sama lain. Kegunaan tipikal corak ini termasuk kolaborasi pasukan, sokongan pelanggan, dan rangkaian sosial.

Dalam corak ini, setiap ejen mewakili pengguna dalam sembang kumpulan, dan mesej dihantar antara ejen menggunakan protokol pesanan. Ejen boleh menghantar mesej ke sembang kumpulan, menerima mesej dari sembang kumpulan, dan membalas mesej dari ejen lain.

Corak ini boleh dilaksanakan menggunakan senibina berpusat di mana semua mesej disalurkan melalui pelayan pusat, atau senibina tidak berpusat di mana mesej ditukar secara terus.

![Sembang kumpulan](../../../translated_images/ms/multi-agent-group-chat.ec10f4cde556babd.webp)

### Serah tugas

Corak ini berguna apabila anda ingin membuat aplikasi di mana pelbagai ejen boleh menyerahkan tugas antara satu sama lain.

Kegunaan tipikal corak ini termasuk sokongan pelanggan, pengurusan tugas, dan automasi aliran kerja.

Dalam corak ini, setiap ejen mewakili tugas atau langkah dalam aliran kerja, dan ejen boleh menyerahkan tugas kepada ejen lain berdasarkan peraturan yang telah ditetapkan.

![Serah tugas](../../../translated_images/ms/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Penapisan kolaboratif

Corak ini berguna apabila anda ingin membuat aplikasi di mana pelbagai ejen boleh bekerjasama untuk memberi cadangan kepada pengguna.

Kenapa anda mahu pelbagai ejen bekerjasama adalah kerana setiap ejen boleh mempunyai kepakaran berbeza dan boleh menyumbang kepada proses cadangan dengan cara yang berbeza.

Mari ambil contoh di mana pengguna mahu cadangan tentang saham terbaik untuk dibeli di pasaran saham.

- **Pakar industri**: Satu ejen boleh menjadi pakar dalam industri tertentu.
- **Analisis teknikal**: Ejen lain boleh menjadi pakar dalam analisis teknikal.
- **Analisis fundamental**: dan ejen lain boleh menjadi pakar dalam analisis fundamental. Dengan bekerjasama, ejen-ejen ini boleh memberikan cadangan yang lebih menyeluruh kepada pengguna.

![Cadangan](../../../translated_images/ms/multi-agent-filtering.d959cb129dc9f608.webp)

## Senario: Proses bayaran balik

Pertimbangkan senario di mana pelanggan cuba mendapatkan bayaran balik untuk produk, boleh jadi ada banyak ejen yang terlibat dalam proses ini tetapi mari kita bahagikan antara ejen khusus untuk proses ini dan ejen umum yang boleh digunakan dalam proses lain.

**Ejen khusus untuk proses bayaran balik**:

Berikut adalah beberapa ejen yang boleh terlibat dalam proses bayaran balik:

- **Ejen pelanggan**: Ejen ini mewakili pelanggan dan bertanggungjawab untuk memulakan proses bayaran balik.
- **Ejen penjual**: Ejen ini mewakili penjual dan bertanggungjawab memproses bayaran balik.
- **Ejen pembayaran**: Ejen ini mewakili proses pembayaran dan bertanggungjawab mengembalikan pembayaran pelanggan.
- **Ejen penyelesaian**: Ejen ini mewakili proses penyelesaian dan bertanggungjawab menyelesaikan sebarang isu yang timbul semasa proses bayaran balik.
- **Ejen pematuhan**: Ejen ini mewakili proses pematuhan dan bertanggungjawab memastikan proses bayaran balik mematuhi peraturan dan polisi.

**Ejen umum**:

Ejen ini boleh digunakan oleh bahagian lain perniagaan anda.

- **Ejen penghantaran**: Ejen ini mewakili proses penghantaran dan bertanggungjawab menghantar produk kembali kepada penjual. Ejen ini boleh digunakan untuk proses bayaran balik dan juga penghantaran am produk melalui pembelian contohnya.
- **Ejen maklum balas**: Ejen ini mewakili proses maklum balas dan bertanggungjawab mengumpul maklum balas daripada pelanggan. Maklum balas boleh diambil pada bila-bila masa dan bukan semasa proses bayaran balik sahaja.
- **Ejen eskalasi**: Ejen ini mewakili proses eskalasi dan bertanggungjawab mengeskalasikan isu ke tahap sokongan yang lebih tinggi. Anda boleh menggunakan jenis ejen ini untuk sebarang proses di mana anda perlu eskalasikan isu.
- **Ejen notifikasi**: Ejen ini mewakili proses notifikasi dan bertanggungjawab menghantar notifikasi kepada pelanggan pada pelbagai peringkat dalam proses bayaran balik.
- **Ejen analitik**: Ejen ini mewakili proses analitik dan bertanggungjawab menganalisis data berkaitan proses bayaran balik.
- **Ejen audit**: Ejen ini mewakili proses audit dan bertanggungjawab mengaudit proses bayaran balik untuk memastikan ia dilakukan dengan betul.
- **Ejen pelaporan**: Ejen ini mewakili proses pelaporan dan bertanggungjawab menghasilkan laporan tentang proses bayaran balik.
- **Ejen pengetahuan**: Ejen ini mewakili proses pengetahuan dan bertanggungjawab mengekalkan pangkalan pengetahuan maklumat berkaitan proses bayaran balik. Ejen ini boleh mempunyai pengetahuan tentang bayaran balik dan bahagian lain perniagaan anda.
- **Ejen keselamatan**: Ejen ini mewakili proses keselamatan dan bertanggungjawab memastikan keselamatan proses bayaran balik.
- **Ejen kualiti**: Ejen ini mewakili proses kualiti dan bertanggungjawab memastikan kualiti proses bayaran balik.

Terdapat banyak ejen yang disenaraikan sebelum ini baik untuk proses bayaran balik khusus tetapi juga ejen umum yang boleh digunakan dalam bahagian lain perniagaan anda. Diharapkan ini memberikan anda idea bagaimana anda boleh memutuskan ejen mana yang digunakan dalam sistem multi-ejen anda.

## Tugasan

Reka sistem multi-ejen untuk proses sokongan pelanggan. Kenal pasti ejen yang terlibat dalam proses, peranan dan tanggungjawab mereka, dan bagaimana mereka berinteraksi antara satu sama lain. Pertimbangkan ejen khusus untuk proses sokongan pelanggan dan ejen umum yang boleh digunakan dalam bahagian lain perniagaan anda.


> Fikir dahulu sebelum anda membaca penyelesaian berikut, anda mungkin memerlukan lebih banyak ejen daripada yang anda sangka.

> TIP: Fikirkan tentang peringkat berbeza dalam proses sokongan pelanggan dan juga pertimbangkan ejen yang diperlukan untuk mana-mana sistem.

## Penyelesaian

[Penyelesaian](./solution/solution.md)

## Semakan Pengetahuan

### Soalan 1

Senario manakah yang paling sesuai untuk sistem berbilang ejen?

- [ ] A1: Bot sokongan menjawab soalan biasa menggunakan satu pangkalan pengetahuan dan set alat kecil.
- [ ] A2: Aliran kerja pemulangan memerlukan peranan penipuan, pembayaran, dan pematuhan yang berasingan, masing-masing dengan alatnya sendiri, dan keputusan mereka mesti diselaraskan.
- [ ] A3: Permintaan pengelasan mudah yang sama tiba beribu kali sejam.

### Soalan 2

Bila pilihan satu ejen biasanya lebih baik?

- [ ] A1: Tugasan boleh diuruskan dengan satu set arahan dan alat, tanpa peralihan pakar.
- [ ] A2: Ejen mempunyai akses kepada lebih daripada satu alat.
- [ ] A3: Aliran kerja memerlukan peranan berasingan dengan kebenaran berbeza dan jejak audit bebas.

[Penyelesaian kuiz](./solution/solution-quiz.md)

## Rumusan

Dalam pelajaran ini, kita telah melihat corak reka bentuk berbilang ejen, termasuk senario di mana berbilang ejen sesuai digunakan, kelebihan menggunakan berbilang ejen berbanding ejen tunggal, blok pembinaan melaksanakan corak reka bentuk berbilang ejen, dan cara mendapatkan keterlihatan tentang bagaimana beberapa ejen berinteraksi antara satu sama lain.

### Ada Soalan Lagi tentang Corak Reka Bentuk Berbilang Ejen?

Sertai [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) untuk bertemu dengan pelajar lain, menghadiri waktu pejabat dan mendapatkan soalan mengenai Ejen AI anda terjawab.

## Sumber tambahan

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Dokumentasi Rangka Kerja Ejen Microsoft</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Corak reka bentuk agentik</a>


## Pelajaran Sebelumnya

[Reka Bentuk Perancangan](../07-planning-design/README.md)

## Pelajaran Seterusnya

[Metakognisi dalam Ejen AI](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->