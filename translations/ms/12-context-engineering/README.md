# Kejuruteraan Konteks untuk Ejen AI

[![Kejuruteraan Konteks](../../../translated_images/ms/lesson-12-thumbnail.ed19c94463e774d4.webp)](https://youtu.be/F5zqRV7gEag)

> _(Klik gambar di atas untuk menonton video pelajaran ini)_

Memahami kerumitan aplikasi yang anda bina ejen AI untuknya adalah penting bagi menghasilkan ejen yang boleh dipercayai. Kita perlu membina Ejen AI yang menguruskan maklumat dengan berkesan untuk menangani keperluan kompleks di luar kejuruteraan prompt.

Dalam pelajaran ini, kita akan melihat apa itu kejuruteraan konteks dan peranannya dalam membina ejen AI.

## Pengenalan

Pelajaran ini akan merangkumi:

• **Apa itu Kejuruteraan Konteks** dan mengapa ia berbeza daripada kejuruteraan prompt.

• **Strategi untuk Kejuruteraan Konteks yang berkesan**, termasuk cara menulis, memilih, memampatkan, dan mengasingkan maklumat.

• **Kegagalan Konteks Biasa** yang boleh menggagalkan ejen AI anda dan cara memperbaikinya.

## Matlamat Pembelajaran

Selepas menamatkan pelajaran ini, anda akan memahami cara untuk:

• **Mendefinisikan kejuruteraan konteks** dan membezakannya daripada kejuruteraan prompt.

• **Mengenal pasti komponen utama konteks** dalam aplikasi Model Bahasa Besar (LLM).

• **Mengaplikasi strategi untuk menulis, memilih, memampatkan, dan mengasingkan konteks** untuk meningkatkan prestasi ejen.

• **Mengenal pasti kegagalan konteks biasa** seperti pencemaran, gangguan, kekeliruan, dan pertentangan, serta melaksanakan teknik mitigasi.

## Apa itu Kejuruteraan Konteks?

Untuk Ejen AI, konteks adalah apa yang menggerakkan perancangan Ejen AI untuk mengambil tindakan tertentu. Kejuruteraan Konteks adalah amalan memastikan Ejen AI mempunyai maklumat yang betul untuk melengkapkan langkah seterusnya dalam tugasan. Tingkap konteks adalah terhad saiznya, jadi sebagai pembina ejen kita perlu membina sistem dan proses untuk mengurus penambahan, penghapusan, dan pemadatan maklumat dalam tingkap konteks.

### Kejuruteraan Prompt vs Kejuruteraan Konteks

Kejuruteraan prompt memfokuskan pada satu set arahan statik untuk membimbing Ejen AI dengan satu set peraturan. Kejuruteraan konteks adalah cara mengurus set maklumat dinamik, termasuk prompt awal, untuk memastikan Ejen AI mempunyai apa yang diperlukan dari masa ke masa. Idea utama dalam kejuruteraan konteks adalah menjadikan proses ini boleh diulang dan boleh dipercayai.

### Jenis-jenis Konteks

[![Jenis-jenis Konteks](../../../translated_images/ms/context-types.fc10b8927ee43f06.webp)](https://youtu.be/F5zqRV7gEag)

Penting untuk diingat bahawa konteks bukan hanya satu perkara. Maklumat yang diperlukan oleh Ejen AI boleh datang dari pelbagai sumber yang berbeza dan terpulang kepada kita untuk memastikan ejen mempunyai akses kepada sumber-sumber ini:

Jenis konteks yang mungkin perlu diurus oleh ejen AI termasuk:

• **Arahan:** Ini seperti "peraturan" ejen – prompt, mesej sistem, contoh beberapa tembakan (menunjukkan cara melakukan sesuatu kepada AI), dan deskripsi alat yang boleh digunakan. Di sinilah fokus kejuruteraan prompt bergabung dengan kejuruteraan konteks.

• **Pengetahuan:** Ini merangkumi fakta, maklumat yang diperoleh dari pangkalan data, atau memori jangka panjang yang telah dikumpulkan ejen. Ini termasuk integrasi sistem Generasi Diperkuatkan Pengambilan (RAG) jika ejen memerlukan akses ke pelbagai stor pengetahuan dan pangkalan data.

• **Alat:** Ini adalah definisi fungsi luaran, API dan Server MCP yang boleh dipanggil oleh ejen, bersama dengan maklum balas (hasil) yang diperolehi dari penggunaannya.

• **Sejarah Perbualan:** Dialog berterusan dengan pengguna. Apabila masa berlalu, perbualan ini menjadi lebih panjang dan kompleks yang bermakna mengambil ruang dalam tingkap konteks.

• **Keutamaan Pengguna:** Maklumat yang dipelajari mengenai suka atau tidak suka pengguna dari masa ke masa. Ini boleh disimpan dan digunakan semasa membuat keputusan penting untuk membantu pengguna.

## Strategi untuk Kejuruteraan Konteks yang Berkesan

### Strategi Perancangan

[![Amalan Terbaik Kejuruteraan Konteks](../../../translated_images/ms/best-practices.f4170873dc554f58.webp)](https://youtu.be/F5zqRV7gEag)

Kejuruteraan konteks yang baik bermula dengan perancangan yang baik. Berikut adalah pendekatan yang akan membantu anda mula memikirkan cara menerapkan konsep kejuruteraan konteks:

1. **Tentukan Keputusan yang Jelas** - Keputusan tugasan yang akan diberikan kepada Ejen AI harus ditakrif dengan jelas. Jawab soalan – "Bagaimana dunia akan kelihatan apabila Ejen AI selesai dengan tugasnya?" Dengan kata lain, apa perubahan, maklumat, atau respons yang harus diperoleh pengguna selepas berinteraksi dengan Ejen AI.
2. **Peta Konteks** - Setelah anda menentukan keputusan Ejen AI, anda perlu menjawab soalan "Maklumat apa yang Ejen AI perlukan untuk melengkapkan tugas ini?". Dengan cara ini anda boleh mula memetakan konteks di mana maklumat itu boleh ditemui.
3. **Cipta Saluran Konteks** - Sekarang anda tahu di mana maklumat itu berada, anda perlu menjawab soalan "Bagaimana Ejen akan dapatkan maklumat ini?". Ini boleh dilakukan dengan pelbagai cara termasuk RAG, penggunaan pelayan MCP dan alat-alat lain.

### Strategi Praktikal

Perancangan adalah penting tetapi apabila maklumat mula mengalir ke dalam tingkap konteks ejen kita, kita perlu mempunyai strategi praktikal untuk menguruskannya:

#### Mengurus Konteks

Walaupun sesetengah maklumat akan ditambah ke tingkap konteks secara automatik, kejuruteraan konteks adalah tentang mengambil peranan lebih aktif terhadap maklumat ini yang boleh dilakukan dengan beberapa strategi:

 1. **Kertas Nota Ejen**
 Ini membenarkan Ejen AI membuat nota maklumat relevan tentang tugasan semasa dan interaksi pengguna sepanjang sesi tunggal. Ini harus wujud di luar tingkap konteks dalam fail atau objek masa jalan yang boleh diambil semula oleh ejen pada sesi ini jika diperlukan.

 2. **Memori**
 Kertas nota baik untuk mengurus maklumat di luar tingkap konteks sesi tunggal. Memori membolehkan ejen menyimpan dan mengambil semula maklumat relevan merentasi pelbagai sesi. Ini boleh termasuk ringkasan, keutamaan pengguna dan maklum balas untuk penambahbaikan masa depan.

 3. **Memampatkan Konteks**
  Setelah tingkap konteks membesar dan hampir mencapai hadnya, teknik seperti membuat ringkasan dan pemotongan boleh digunakan. Ini termasuk sama ada menyimpan hanya maklumat yang paling relevan atau mengeluarkan mesej lama.
  
 4. **Sistem Multi-Ejen**
  Membangunkan sistem multi-ejen adalah satu bentuk kejuruteraan konteks kerana setiap ejen mempunyai tingkap konteksnya sendiri. Bagaimana konteks itu dikongsi dan disalurkan ke ejen yang berbeza adalah satu aspek yang perlu dirancang ketika membina sistem ini.
  
 5. **Persekitaran Pembersihan (Sandbox)**
  Jika ejen perlu menjalankan beberapa kod atau memproses sejumlah besar maklumat dalam dokumen, ini boleh mengambil banyak token untuk memproses hasil. Daripada menyimpan semua ini dalam tingkap konteks, ejen boleh menggunakan persekitaran pembersihan yang boleh menjalankan kod ini dan hanya membaca hasil dan maklumat relevan lain.
  
 6. **Objek Keadaan Runtime**
   Ini dilakukan dengan mencipta bekas maklumat untuk mengurus situasi apabila Ejen perlu mempunyai akses kepada maklumat tertentu. Untuk tugasan kompleks, ini membolehkan Ejen menyimpan hasil setiap sub-tugasan secara langkah demi langkah, membolehkan konteks kekal terhubung hanya pada sub-tugasan spesifik itu.

#### Memeriksa Konteks

Setelah anda menggunakan salah satu strategi ini, adalah berbaloi untuk memeriksa apa yang sebenarnya diterima panggilan model seterusnya. Soalan debugging yang berguna ialah:

> Adakah ejen memuatkan terlalu banyak konteks, konteks yang salah, atau terlepas konteks yang diperlukan?

Anda tidak perlu merekodkan prompt mentah, output alat, atau kandungan memori untuk menjawab soalan itu. Dalam pengeluaran, pilih rekod pemeriksaan konteks kecil yang merangkumi kiraan, id, hash, dan label polisi:

- **Pemilihan:** Jejak berapa banyak segmen calon, alat, atau memori dipertimbangkan, berapa banyak dipilih, dan peraturan atau skor mana yang menyebabkan yang lain ditapis keluar.
- **Pemampatan:** Rekod julat sumber atau id jejak, id ringkasan, anggaran kiraan token sebelum dan selepas pemampatan, dan sama ada kandungan mentah dikecualikan dari panggilan seterusnya.
- **Pengasingan:** Catatkan sub-tugasan yang dijalankan dalam ejen, sesi, atau sandbox berasingan, ringkasan terhad yang dikembalikan, dan sama ada output alat besar kekal di luar konteks ejen induk.
- **Memori dan RAG:** Simpan id dokumen pengambilan, id memori, skor, id terpilih, dan status penyuntingan menggantikan teks penuh yang diambil.
- **Keselamatan dan privasi:** Pilih hash, id, baldi token, dan label polisi daripada teks prompt sensitif, hujah alat, hasil alat, atau badan memori pengguna.

Matlamatnya bukan untuk menyimpan lebih banyak konteks. Ia adalah untuk meninggalkan bukti yang cukup supaya pembangun dapat memberitahu strategi konteks mana yang dijalankan dan sama ada ia mengubah panggilan model seterusnya dengan cara yang dimaksudkan.

### Contoh Kejuruteraan Konteks

Katakan kita mahu ejen AI **"Tempahkan saya perjalanan ke Paris."**

• Ejen mudah yang menggunakan hanya kejuruteraan prompt mungkin hanya memberi respons: **"Baik, bila anda ingin pergi ke Paris?**". Ia hanya memproses soalan langsung anda pada waktu pengguna bertanya.

• Ejen yang menggunakan strategi kejuruteraan konteks yang dibincangkan akan melakukan lebih daripada itu. Sebelum menjawab pun, sistemnya mungkin:

  ◦ **Periksa kalendar anda** untuk tarikh yang tersedia (mengambil data masa nyata).

 ◦ **Kenang keutamaan perjalanan lalu** (daripada memori jangka panjang) seperti syarikat penerbangan pilihan anda, bajet, atau sama ada anda lebih suka penerbangan terus.

 ◦ **Kenalpasti alat yang tersedia** untuk tempahan penerbangan dan hotel.

- Kemudian, contoh respons boleh jadi: "Hai [Nama Anda]! Saya nampak anda bebas minggu pertama Oktober. Haruskah saya cari penerbangan terus ke Paris dengan [Syarikat Penerbangan Pilihan] dalam bajet biasa anda [Bajet]?". Respons yang lebih kaya dan sedar konteks ini menunjukkan kuasa kejuruteraan konteks.

## Kegagalan Konteks Biasa

### Pencemaran Konteks

**Apa itu:** Apabila halusinasi (maklumat palsu yang dijana oleh LLM) atau ralat masuk ke dalam konteks dan dirujuk berulang kali, menyebabkan ejen mengejar matlamat yang mustahil atau membangunkan strategi tidak masuk akal.

**Apa yang perlu dilakukan:** Laksanakan **pengesahan konteks** dan **kuarantin**. Sahkan maklumat sebelum ditambah ke memori jangka panjang. Jika pencemaran berpotensi dikesan, mulakan semula thread konteks untuk mengelakkan maklumat buruk itu merebak.

**Contoh Tempahan Perjalanan:** Ejen anda mengalami halusinasi tentang **penerbangan terus dari lapangan terbang tempatan kecil ke bandar antarabangsa jauh** yang sebenarnya tidak menawarkan penerbangan antarabangsa. Butiran penerbangan yang tidak wujud ini disimpan dalam konteks. Kemudian, apabila anda minta ejen tempah, ia terus cuba mencari tiket untuk laluan mustahil ini, menyebabkan kesilapan berulang.

**Penyelesaian:** Laksanakan langkah yang **mengesahkan kewujudan penerbangan dan laluan dengan API masa nyata** _sebelum_ menambah butiran penerbangan dalam konteks kerja ejen. Jika pengesahan gagal, maklumat salah itu "dikurung" dan tidak digunakan lagi.

### Gangguan Konteks

**Apa itu:** Apabila konteks menjadi sangat besar sehingga model terlalu fokus pada sejarah terkumpul daripada menggunakan apa yang dipelajari semasa latihan, menyebabkan tindakan berulang atau tidak membantu. Model mungkin mula berbuat kesilapan walaupun sebelum tingkap konteks penuh.

**Apa yang perlu dilakukan:** Gunakan **ringkasan konteks**. Secara berkala mampatkan maklumat terkumpul menjadi ringkasan lebih pendek, mengekalkan butiran penting sambil menghapus sejarah yang berulang. Ini membantu "set semula" fokus.

**Contoh Tempahan Perjalanan:** Anda telah membincangkan pelbagai destinasi impian untuk masa yang lama, termasuk penceritaan terperinci tentang perjalanan backpacking dua tahun lalu. Apabila anda akhirnya minta **"carikan saya penerbangan murah untuk bulan depan,"** ejen terperangkap dengan butiran lama yang tidak relevan dan terus bertanya tentang peralatan backpacking atau jadual lama, mengabaikan permintaan semasa anda.

**Penyelesaian:** Selepas sejumlah pusingan atau apabila konteks terlalu besar, ejen perlu **meringkaskan bahagian terkini dan relevan perbualan** – menumpukan pada tarikh perjalanan dan destinasi anda sekarang – dan gunakan ringkasan padat itu untuk panggilan LLM seterusnya, membuang sembang sejarah kurang relevan.

### Kekeliruan Konteks

**Apa itu:** Apabila konteks tidak diperlukan, selalunya dalam bentuk terlalu banyak alat tersedia, menyebabkan model menghasilkan respons buruk atau memanggil alat yang tidak relevan. Model lebih kecil amat terdedah kepada ini.

**Apa yang perlu dilakukan:** Laksanakan **pengurusan muatan alat** menggunakan teknik RAG. Simpan deskripsi alat dalam pangkalan data vektor dan pilih _hanya_ alat yang paling relevan untuk setiap tugasan spesifik. Kajian menunjukkan hadkan pemilihan alat kurang daripada 30.

**Contoh Tempahan Perjalanan:** Ejen anda mempunyai akses kepada puluhan alat: `tempah_penerbangan`, `tempah_hotel`, `sewa_mobil`, `cari_tur`, `penukar_matawang`, `ramalan_cuaca`, `tempahan_restoran`, dan lain-lain. Anda bertanya, **"Apa cara terbaik untuk bergerak di Paris?"** Disebabkan bilangan alat yang banyak, ejen keliru dan cuba memanggil `tempah_penerbangan` _di dalam_ Paris, atau `sewa_mobil` walaupun anda lebih suka pengangkutan awam, kerana deskripsi alat mungkin bertindih atau ia tidak dapat membezakan yang terbaik.

**Penyelesaian:** Gunakan **RAG ke atas deskripsi alat**. Apabila anda bertanya tentang cara bergerak di Paris, sistem secara dinamik mendapatkan _hanya_ alat yang paling relevan seperti `sewa_mobil` atau `maklumat_pengangkutan_awam` berdasarkan pertanyaan anda, mempersembahkan "muatan" alat yang fokus kepada LLM.

### Pertentangan Konteks

**Apa itu:** Apabila maklumat bertentangan wujud dalam konteks, menyebabkan penalaran tidak konsisten atau respons akhir yang buruk. Ini sering berlaku apabila maklumat tiba secara berperingkat, dan andaian awal yang salah kekal dalam konteks.

**Apa yang perlu dilakukan:** Gunakan **pemangkasan konteks** dan **pemindahan keluar**. Pemangkasan bermaksud mengeluarkan maklumat lapuk atau bertentangan apabila maklumat baru tiba. Pemindahan keluar memberi model ruang kerja "kertas nota" berasingan untuk memproses maklumat tanpa mengacau konteks utama.


**Contoh Tempahan Perjalanan:** Pada mulanya anda memberitahu ejen anda, **"Saya mahu terbang dalam kelas ekonomi."** Kemudian dalam perbualan, anda berubah fikiran dan berkata, **"Sebenarnya, untuk perjalanan ini, mari kita guna kelas perniagaan."** Jika kedua-dua arahan itu kekal dalam konteks, ejen mungkin menerima keputusan carian yang bertentangan atau keliru tentang keutamaan mana yang perlu diberi perhatian.

**Penyelesaian:** Laksanakan **pemangkasan konteks**. Apabila arahan baru bercanggah dengan yang lama, arahan lama akan dikeluarkan atau secara jelas ditindih dalam konteks. Sebaliknya, ejen boleh menggunakan **buku nota** untuk menyelasikan keutamaan yang bertentangan sebelum membuat keputusan, memastikan hanya arahan akhir yang konsisten yang membimbing tindakannya.

## Ada Lebih Banyak Soalan Tentang Kejuruteraan Konteks?

Sertai [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) untuk berjumpa dengan pelajar lain, hadiri waktu pejabat dan dapatkan jawapan untuk soalan Ejen AI anda.
## Pelajaran Sebelumnya

[Agentic Protocols](../11-agentic-protocols/README.md)

## Pelajaran Seterusnya

[Memory for AI Agents](../13-agent-memory/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->