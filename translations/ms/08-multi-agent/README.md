<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a008c204051cba8d0e253b75f261c41",
  "translation_date": "2025-08-29T18:15:57+00:00",
  "source_file": "08-multi-agent/README.md",
  "language_code": "ms"
}
-->
[![Reka Bentuk Multi-Ejen](../../../translated_images/lesson-8-thumbnail.278a3e4a59137d625df92de3f885d2da2a92b1f7017abba25a99fb25edd83a55.ms.png)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Klik imej di atas untuk menonton video pelajaran ini)_

# Corak Reka Bentuk Multi-Ejen

Apabila anda mula bekerja pada projek yang melibatkan pelbagai ejen, anda perlu mempertimbangkan corak reka bentuk multi-ejen. Walau bagaimanapun, mungkin tidak jelas bila untuk beralih kepada multi-ejen dan apakah kelebihannya.

## Pengenalan

Dalam pelajaran ini, kita akan cuba menjawab soalan berikut:

- Apakah senario di mana multi-ejen boleh digunakan?
- Apakah kelebihan menggunakan multi-ejen berbanding hanya satu ejen tunggal yang melakukan pelbagai tugas?
- Apakah komponen asas untuk melaksanakan corak reka bentuk multi-ejen?
- Bagaimana kita boleh mendapatkan gambaran tentang bagaimana pelbagai ejen berinteraksi antara satu sama lain?

## Matlamat Pembelajaran

Selepas pelajaran ini, anda seharusnya dapat:

- Mengenal pasti senario di mana multi-ejen boleh digunakan.
- Mengenali kelebihan menggunakan multi-ejen berbanding ejen tunggal.
- Memahami komponen asas untuk melaksanakan corak reka bentuk multi-ejen.

Apakah gambaran yang lebih besar?

*Multi-ejen adalah corak reka bentuk yang membolehkan pelbagai ejen bekerjasama untuk mencapai matlamat bersama.*

Corak ini digunakan secara meluas dalam pelbagai bidang, termasuk robotik, sistem autonomi, dan pengkomputeran teragih.

## Senario Di Mana Multi-Ejen Boleh Digunakan

Jadi, apakah senario yang sesuai untuk menggunakan multi-ejen? Jawapannya ialah terdapat banyak senario di mana penggunaan pelbagai ejen adalah bermanfaat, terutamanya dalam kes berikut:

- **Beban kerja besar**: Beban kerja besar boleh dibahagikan kepada tugas-tugas kecil dan diberikan kepada ejen yang berbeza, membolehkan pemprosesan selari dan penyelesaian yang lebih cepat. Contohnya ialah dalam tugas pemprosesan data yang besar.
- **Tugas kompleks**: Tugas kompleks, seperti beban kerja besar, boleh dipecahkan kepada sub-tugas kecil dan diberikan kepada ejen yang berbeza, masing-masing pakar dalam aspek tertentu tugas tersebut. Contoh yang baik ialah dalam kes kenderaan autonomi di mana ejen yang berbeza menguruskan navigasi, pengesanan halangan, dan komunikasi dengan kenderaan lain.
- **Kepakaran pelbagai**: Ejen yang berbeza boleh mempunyai kepakaran yang pelbagai, membolehkan mereka mengendalikan aspek tugas yang berbeza dengan lebih berkesan berbanding ejen tunggal. Contoh yang baik ialah dalam bidang penjagaan kesihatan di mana ejen boleh menguruskan diagnostik, pelan rawatan, dan pemantauan pesakit.

## Kelebihan Menggunakan Multi-Ejen Berbanding Ejen Tunggal

Sistem ejen tunggal mungkin berfungsi dengan baik untuk tugas mudah, tetapi untuk tugas yang lebih kompleks, menggunakan pelbagai ejen boleh memberikan beberapa kelebihan:

- **Pengkhususan**: Setiap ejen boleh dikhususkan untuk tugas tertentu. Kekurangan pengkhususan dalam ejen tunggal bermakna anda mempunyai ejen yang boleh melakukan segalanya tetapi mungkin keliru tentang apa yang perlu dilakukan apabila berhadapan dengan tugas yang kompleks. Ia mungkin, sebagai contoh, melakukan tugas yang tidak sesuai untuknya.
- **Kebolehskalaan**: Lebih mudah untuk menskalakan sistem dengan menambah lebih banyak ejen daripada membebankan ejen tunggal.
- **Toleransi Kesilapan**: Jika satu ejen gagal, ejen lain boleh terus berfungsi, memastikan kebolehpercayaan sistem.

Mari kita ambil contoh, mari kita tempah perjalanan untuk seorang pengguna. Sistem ejen tunggal perlu mengendalikan semua aspek proses tempahan perjalanan, daripada mencari penerbangan hingga menempah hotel dan kereta sewa. Untuk mencapai ini dengan ejen tunggal, ejen tersebut perlu mempunyai alat untuk mengendalikan semua tugas ini. Ini boleh membawa kepada sistem yang kompleks dan monolitik yang sukar untuk diselenggara dan diskalakan. Sistem multi-ejen, sebaliknya, boleh mempunyai ejen yang berbeza yang pakar dalam mencari penerbangan, menempah hotel, dan kereta sewa. Ini akan menjadikan sistem lebih modular, lebih mudah diselenggara, dan boleh diskalakan.

Bandingkan ini dengan biro perjalanan yang dijalankan sebagai kedai kecil berbanding biro perjalanan yang dijalankan sebagai francais. Kedai kecil akan mempunyai satu ejen yang mengendalikan semua aspek proses tempahan perjalanan, manakala francais akan mempunyai ejen yang berbeza yang mengendalikan aspek yang berbeza dalam proses tempahan perjalanan.

## Komponen Asas Melaksanakan Corak Reka Bentuk Multi-Ejen

Sebelum anda boleh melaksanakan corak reka bentuk multi-ejen, anda perlu memahami komponen asas yang membentuk corak ini.

Mari kita buat ini lebih konkrit dengan sekali lagi melihat contoh menempah perjalanan untuk seorang pengguna. Dalam kes ini, komponen asas akan merangkumi:

- **Komunikasi Ejen**: Ejen untuk mencari penerbangan, menempah hotel, dan kereta sewa perlu berkomunikasi dan berkongsi maklumat tentang keutamaan dan kekangan pengguna. Anda perlu memutuskan protokol dan kaedah untuk komunikasi ini. Apa yang dimaksudkan secara konkrit ialah ejen untuk mencari penerbangan perlu berkomunikasi dengan ejen untuk menempah hotel untuk memastikan bahawa hotel ditempah untuk tarikh yang sama dengan penerbangan. Ini bermakna ejen perlu berkongsi maklumat tentang tarikh perjalanan pengguna, bermakna anda perlu memutuskan *ejen mana yang berkongsi maklumat dan bagaimana mereka berkongsi maklumat*.
- **Mekanisme Penyelarasan**: Ejen perlu menyelaraskan tindakan mereka untuk memastikan keutamaan dan kekangan pengguna dipenuhi. Keutamaan pengguna boleh jadi mereka mahukan hotel yang dekat dengan lapangan terbang manakala kekangan boleh jadi kereta sewa hanya tersedia di lapangan terbang. Ini bermakna ejen untuk menempah hotel perlu menyelaraskan dengan ejen untuk menempah kereta sewa untuk memastikan keutamaan dan kekangan pengguna dipenuhi. Ini bermakna anda perlu memutuskan *bagaimana ejen menyelaraskan tindakan mereka*.
- **Seni Bina Ejen**: Ejen perlu mempunyai struktur dalaman untuk membuat keputusan dan belajar daripada interaksi mereka dengan pengguna. Ini bermakna ejen untuk mencari penerbangan perlu mempunyai struktur dalaman untuk membuat keputusan tentang penerbangan mana yang hendak disyorkan kepada pengguna. Ini bermakna anda perlu memutuskan *bagaimana ejen membuat keputusan dan belajar daripada interaksi mereka dengan pengguna*. Contoh bagaimana ejen belajar dan bertambah baik boleh jadi ejen untuk mencari penerbangan boleh menggunakan model pembelajaran mesin untuk mencadangkan penerbangan kepada pengguna berdasarkan keutamaan mereka yang lalu.
- **Keterlihatan dalam Interaksi Multi-Ejen**: Anda perlu mempunyai keterlihatan tentang bagaimana pelbagai ejen berinteraksi antara satu sama lain. Ini bermakna anda perlu mempunyai alat dan teknik untuk menjejaki aktiviti dan interaksi ejen. Ini boleh berupa alat log dan pemantauan, alat visualisasi, dan metrik prestasi.
- **Corak Multi-Ejen**: Terdapat corak yang berbeza untuk melaksanakan sistem multi-ejen, seperti seni bina berpusat, teragih, dan hibrid. Anda perlu memutuskan corak yang paling sesuai dengan kes penggunaan anda.
- **Manusia dalam Gelung**: Dalam kebanyakan kes, anda akan mempunyai manusia dalam gelung dan anda perlu mengarahkan ejen bila untuk meminta campur tangan manusia. Ini boleh berupa pengguna meminta hotel atau penerbangan tertentu yang tidak disyorkan oleh ejen atau meminta pengesahan sebelum menempah penerbangan atau hotel.

## Keterlihatan dalam Interaksi Multi-Ejen

Adalah penting untuk anda mempunyai keterlihatan tentang bagaimana pelbagai ejen berinteraksi antara satu sama lain. Keterlihatan ini penting untuk penyahpepijatan, pengoptimuman, dan memastikan keberkesanan keseluruhan sistem. Untuk mencapai ini, anda perlu mempunyai alat dan teknik untuk menjejaki aktiviti dan interaksi ejen. Ini boleh berupa alat log dan pemantauan, alat visualisasi, dan metrik prestasi.

Sebagai contoh, dalam kes menempah perjalanan untuk seorang pengguna, anda boleh mempunyai papan pemuka yang menunjukkan status setiap ejen, keutamaan dan kekangan pengguna, dan interaksi antara ejen. Papan pemuka ini boleh menunjukkan tarikh perjalanan pengguna, penerbangan yang disyorkan oleh ejen penerbangan, hotel yang disyorkan oleh ejen hotel, dan kereta sewa yang disyorkan oleh ejen kereta sewa. Ini akan memberikan anda gambaran yang jelas tentang bagaimana ejen berinteraksi antara satu sama lain dan sama ada keutamaan dan kekangan pengguna dipenuhi.

Mari kita lihat setiap aspek ini dengan lebih terperinci.

- **Alat Log dan Pemantauan**: Anda mahu log dilakukan untuk setiap tindakan yang diambil oleh ejen. Entri log boleh menyimpan maklumat tentang ejen yang mengambil tindakan, tindakan yang diambil, masa tindakan diambil, dan hasil tindakan. Maklumat ini kemudian boleh digunakan untuk penyahpepijatan, pengoptimuman, dan banyak lagi.

- **Alat Visualisasi**: Alat visualisasi boleh membantu anda melihat interaksi antara ejen dengan cara yang lebih intuitif. Sebagai contoh, anda boleh mempunyai graf yang menunjukkan aliran maklumat antara ejen. Ini boleh membantu anda mengenal pasti halangan, ketidakcekapan, dan isu lain dalam sistem.

- **Metrik Prestasi**: Metrik prestasi boleh membantu anda menjejaki keberkesanan sistem multi-ejen. Sebagai contoh, anda boleh menjejaki masa yang diambil untuk menyelesaikan tugas, bilangan tugas yang diselesaikan setiap unit masa, dan ketepatan cadangan yang dibuat oleh ejen. Maklumat ini boleh membantu anda mengenal pasti kawasan untuk penambahbaikan dan mengoptimumkan sistem.

## Corak Multi-Ejen

Mari kita selami beberapa corak konkrit yang boleh kita gunakan untuk mencipta aplikasi multi-ejen. Berikut adalah beberapa corak menarik yang patut dipertimbangkan:

### Sembang Kumpulan

Corak ini berguna apabila anda ingin mencipta aplikasi sembang kumpulan di mana pelbagai ejen boleh berkomunikasi antara satu sama lain. Kes penggunaan tipikal untuk corak ini termasuk kerjasama pasukan, sokongan pelanggan, dan rangkaian sosial.

Dalam corak ini, setiap ejen mewakili pengguna dalam sembang kumpulan, dan mesej ditukar antara ejen menggunakan protokol pemesejan. Ejen boleh menghantar mesej ke sembang kumpulan, menerima mesej dari sembang kumpulan, dan bertindak balas kepada mesej dari ejen lain.

Corak ini boleh dilaksanakan menggunakan seni bina berpusat di mana semua mesej dihantar melalui pelayan pusat, atau seni bina teragih di mana mesej ditukar secara langsung.

![Sembang Kumpulan](../../../translated_images/multi-agent-group-chat.ec10f4cde556babd7b450fd01e1a0fac1f9788c27d3b9e54029377bb1bdd1db6.ms.png)

### Penyerahan Tugas

Corak ini berguna apabila anda ingin mencipta aplikasi di mana pelbagai ejen boleh menyerahkan tugas antara satu sama lain.

Kes penggunaan tipikal untuk corak ini termasuk sokongan pelanggan, pengurusan tugas, dan automasi aliran kerja.

Dalam corak ini, setiap ejen mewakili tugas atau langkah dalam aliran kerja, dan ejen boleh menyerahkan tugas kepada ejen lain berdasarkan peraturan yang telah ditetapkan.

![Penyerahan Tugas](../../../translated_images/multi-agent-hand-off.4c5fb00ba6f8750a0754bf29d49fa19d578080c61da40416df84d866bcdd87a3.ms.png)

### Penapisan Kolaboratif

Corak ini berguna apabila anda ingin mencipta aplikasi di mana pelbagai ejen boleh bekerjasama untuk membuat cadangan kepada pengguna.

Mengapa anda ingin pelbagai ejen bekerjasama adalah kerana setiap ejen boleh mempunyai kepakaran yang berbeza dan boleh menyumbang kepada proses cadangan dengan cara yang berbeza.

Mari kita ambil contoh di mana seorang pengguna ingin mendapatkan cadangan tentang saham terbaik untuk dibeli di pasaran saham.

- **Pakar Industri**: Satu ejen boleh menjadi pakar dalam industri tertentu.
- **Analisis Teknikal**: Ejen lain boleh menjadi pakar dalam analisis teknikal.
- **Analisis Fundamental**: Dan ejen lain boleh menjadi pakar dalam analisis fundamental. Dengan bekerjasama, ejen-ejen ini boleh memberikan cadangan yang lebih komprehensif kepada pengguna.

![Cadangan](../../../translated_images/multi-agent-filtering.d959cb129dc9f60826916f0f12fe7a8339b532f5f236860afb8f16b63ea10dc2.ms.png)

## Senario: Proses Pemulangan Wang

Pertimbangkan senario di mana seorang pelanggan cuba mendapatkan pemulangan wang untuk produk, terdapat beberapa ejen yang boleh terlibat dalam proses ini tetapi mari kita bahagikan antara ejen khusus untuk proses ini dan ejen umum yang boleh digunakan dalam proses lain.

**Ejen khusus untuk proses pemulangan wang**:

Berikut adalah beberapa ejen yang boleh terlibat dalam proses pemulangan wang:

- **Ejen Pelanggan**: Ejen ini mewakili pelanggan dan bertanggungjawab untuk memulakan proses pemulangan wang.
- **Ejen Penjual**: Ejen ini mewakili penjual dan bertanggungjawab untuk memproses pemulangan wang.
- **Ejen Pembayaran**: Ejen ini mewakili proses pembayaran dan bertanggungjawab untuk memulangkan pembayaran pelanggan.
- **Ejen Resolusi**: Ejen ini mewakili proses resolusi dan bertanggungjawab untuk menyelesaikan sebarang isu yang timbul semasa proses pemulangan wang.
- **Ejen Pematuhan**: Ejen ini mewakili proses pematuhan dan bertanggungjawab untuk memastikan bahawa proses pemulangan wang mematuhi peraturan dan dasar.

**Ejen umum**:

Ejen-ejen ini boleh digunakan oleh bahagian lain dalam perniagaan anda.

- **Ejen Penghantaran**: Ejen ini mewakili proses penghantaran dan bertanggungjawab untuk menghantar produk kembali kepada penjual. Ejen ini boleh digunakan untuk proses pemulangan wang dan juga untuk penghantaran produk secara umum, contohnya melalui pembelian.
- **Ejen Maklum Balas**: Ejen ini mewakili proses maklum balas dan bertanggungjawab untuk mengumpul maklum balas daripada pelanggan. Maklum balas boleh diperoleh pada bila-bila masa dan bukan hanya semasa proses pemulangan wang.
- **Ejen Eskalasi**: Ejen ini mewakili proses eskalasi dan bertanggungjawab untuk meningkatkan isu ke tahap sokongan yang lebih tinggi. Anda boleh menggunakan jenis ejen ini untuk sebarang proses di mana anda perlu meningkatkan isu.
- **Ejen Pemberitahuan**: Ejen ini mewakili proses pemberitahuan dan bertanggungjawab untuk menghantar pemberitahuan kepada pelanggan pada pelbagai peringkat proses pemulangan wang.
- **Ejen Analitik**: Ejen ini mewakili proses analitik dan bertanggungjawab untuk menganalisis data yang berkaitan dengan proses pemulangan wang.
- **Ejen Audit**: Ejen ini mewakili proses audit dan bertanggungjawab untuk mengaudit proses pemulangan wang bagi memastikan ia dijalankan dengan betul.
- **Ejen Pelaporan**: Ejen ini mewakili proses pelaporan dan bertanggungjawab untuk menghasilkan laporan mengenai proses pemulangan wang.
- **Ejen Pengetahuan**: Ejen ini mewakili proses pengetahuan dan bertanggungjawab untuk mengekalkan pangkalan pengetahuan maklumat yang berkaitan dengan proses pemulangan wang. Ejen ini boleh berpengetahuan tentang pemulangan wang dan juga bahagian lain dalam perniagaan anda.
- **Ejen Keselamatan**: Ejen ini mewakili proses keselamatan dan bertanggungjawab untuk memastikan keselamatan proses pemulangan wang.
- **Ejen Kualiti**: Ejen ini mewakili proses kualiti dan bertanggungjawab untuk memastikan kualiti proses pemulangan wang.

Terdapat banyak ejen yang disenaraikan sebelum ini, baik untuk proses pemulangan wang khusus mahupun untuk ejen umum yang boleh digunakan dalam bahagian lain perniagaan anda. Diharapkan ini memberikan anda idea tentang bagaimana anda boleh memutuskan ejen mana yang hendak digunakan dalam sistem multi-ejen anda.

## Tugasan
Reka bentuk sistem berbilang ejen untuk proses sokongan pelanggan. Kenal pasti ejen yang terlibat dalam proses ini, peranan dan tanggungjawab mereka, serta bagaimana mereka berinteraksi antara satu sama lain. Pertimbangkan kedua-dua ejen khusus untuk proses sokongan pelanggan dan ejen umum yang boleh digunakan dalam bahagian lain perniagaan anda.

> Fikirkan dahulu sebelum membaca penyelesaian berikut, anda mungkin memerlukan lebih banyak ejen daripada yang anda sangka.

> TIP: Fikirkan tentang peringkat berbeza dalam proses sokongan pelanggan dan juga pertimbangkan ejen yang diperlukan untuk mana-mana sistem.

## Penyelesaian

[Penyelesaian](./solution/solution.md)

## Pemeriksaan Pengetahuan

Soalan: Bilakah anda perlu mempertimbangkan untuk menggunakan berbilang ejen?

- [ ] A1: Apabila anda mempunyai beban kerja kecil dan tugas yang mudah.
- [ ] A2: Apabila anda mempunyai beban kerja yang besar.
- [ ] A3: Apabila anda mempunyai tugas yang mudah.

[Kuiz Penyelesaian](./solution/solution-quiz.md)

## Ringkasan

Dalam pelajaran ini, kita telah melihat corak reka bentuk berbilang ejen, termasuk senario di mana berbilang ejen boleh digunakan, kelebihan menggunakan berbilang ejen berbanding ejen tunggal, blok binaan untuk melaksanakan corak reka bentuk berbilang ejen, dan cara untuk mendapatkan gambaran tentang bagaimana berbilang ejen berinteraksi antara satu sama lain.

### Ada Lagi Soalan tentang Corak Reka Bentuk Berbilang Ejen?

Sertai [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord) untuk bertemu dengan pelajar lain, menghadiri waktu pejabat, dan mendapatkan jawapan kepada soalan anda tentang Ejen AI.

## Sumber Tambahan

- 

## Pelajaran Sebelumnya

[Reka Bentuk Perancangan](../07-planning-design/README.md)

## Pelajaran Seterusnya

[Metakognisi dalam Ejen AI](../09-metacognition/README.md)

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat yang kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.