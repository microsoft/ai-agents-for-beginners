# Membangun Ejen Penggunaan Komputer (CUA)

Ejen penggunaan komputer boleh berinteraksi dengan laman web sama seperti manusia: dengan membuka pelayar, memeriksa halaman, dan mengambil tindakan terbaik seterusnya daripada apa yang mereka lihat. Dalam pelajaran ini, anda akan membina ejen automasi pelayar yang mencari Airbnb, mengekstrak data listing berstruktur, dan mengenal pasti penginapan termurah di Stockholm.

Pelajaran ini menggabungkan Browser-Use untuk navigasi dipacu AI, Playwright dan Chrome DevTools Protocol (CDP) untuk kawalan pelayar, Azure OpenAI untuk penalaran berasaskan visi, dan Pydantic untuk ekstraksi berstruktur.

## Pengenalan

Pelajaran ini akan merangkumi:

- Memahami bila ejen penggunaan komputer lebih sesuai berbanding automasi hanya API
- Menggabungkan Browser-Use dengan Playwright dan CDP untuk pengurusan kitar hayat pelayar yang boleh dipercayai
- Menggunakan Azure OpenAI vision dan keluaran berstruktur Pydantic untuk mengekstrak data listing dari laman web dinamik
- Memutuskan bila untuk menggunakan aliran kerja automasi pelayar agent-first, actor-first, atau hibrid

## Matlamat Pembelajaran

Selepas menyelesaikan pelajaran ini, anda akan tahu bagaimana untuk:

- Konfigurasi Browser-Use dengan Azure OpenAI dan Playwright
- Membangun aliran kerja automasi pelayar yang melayari laman web sebenar dan mengendalikan elemen UI dinamik
- Mengekstrak keputusan berjenis dari kandungan halaman yang kelihatan dan menukarnya menjadi logik perniagaan hiliran
- Memilih antara corak ejen dan pelakon berdasarkan seberapa boleh diramalkan tugas pelayar

## Contoh Kod

Pelajaran ini termasuk satu tutorial buku nota:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Melancarkan sesi Chrome melalui CDP, mencari listing Stockholm di Airbnb, mengekstrak harga dengan visi Browser-Use, dan mengembalikan pilihan termurah sebagai data berstruktur.

## Prasyarat

- Python 3.12+
- Penggunaan Azure OpenAI sudah dikonfigurasi dalam persekitaran anda
- Chrome atau Chromium dipasang secara tempatan
- Kebergantungan Playwright dipasang
- Kefahaman asas mengenai Python async

## Persediaan

Pasang pakej yang digunakan dalam buku nota:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Tetapkan pembolehubah persekitaran Azure OpenAI yang digunakan oleh buku nota:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Pilihan: secara lalai menggunakan versi API terkini apabila tidak disertakan
AZURE_OPENAI_API_VERSION=...
```

## Gambaran Keseluruhan Seni Bina

Buku nota ini menunjukkan aliran kerja automasi pelayar hibrid:

1. Chrome bermula dengan CDP diaktifkan supaya Playwright dan Browser-Use boleh berkongsi sesi pelayar yang sama.
2. Ejen Browser-Use mengendalikan tugas navigasi terbuka seperti membuka Airbnb, menolak pop-up, dan mencari Stockholm.
3. Halaman aktif diperiksa dengan skema Pydantic berstruktur untuk mengekstrak tajuk listing, harga malam, penilaian, dan URL.
4. Logik Python membandingkan listing yang diekstrak dan menyerlahkan hasil termurah.

Pendekatan ini mengekalkan penalaran berasaskan visi yang fleksibel yang Browser-Use mahir sambil masih memberi anda kawalan pelayar deterministik apabila anda memerlukannya.

## Intipati dan Amalan Terbaik

### Bila untuk Menggunakan Ejen vs Pelakon

| Senario | Gunakan Ejen | Gunakan Pelakon |
|----------|-----------|-----------|
| Susun atur dinamik | Ya, AI boleh menyesuaikan kepada perubahan halaman | Tidak, penentu rapuh boleh rosak |
| Struktur diketahui | Tidak, ejen lebih lambat dari kawalan terus | Ya, pantas dan tepat |
| Mencari elemen | Ya, bahasa semula jadi berkesan | Tidak, diperlukan penentu tepat |
| Kawalan masa | Tidak, kurang boleh diramalkan | Ya, kawalan penuh ke atas tunggu dan cuba semula |
| Aliran kerja kompleks | Ya, mengendalikan keadaan UI yang tidak dijangka | Tidak, memerlukan penguncupan eksplisit |

### Amalan Terbaik Browser-Use

1. Mulakan dengan ejen untuk penerokaan dan navigasi dinamik.
2. Beralih ke kawalan halaman langsung bila interaksi menjadi boleh diramalkan.
3. Gunakan model keluaran berstruktur supaya data yang diekstrak disahkan dan jenisnya selamat.
4. Tambah kelewatan secara strategik selepas tindakan yang mencetus perubahan UI yang kelihatan.
5. Tangkap tangkapan skrin semasa iterasi supaya kegagalan lebih mudah dibaiki.
6. Jangka laman web berubah dan reka strategi sandaran untuk pop-up dan peralihan susun atur.
7. Campur corak ejen dan pelakon untuk mendapatkan fleksibiliti dan ketepatan.

### Perlindungan Keselamatan untuk Ejen Pelayar

Ejen pelayar beroperasi di laman web langsung, jadi mereka perlukan batasan yang lebih ketat berbanding skrip yang hanya memanggil API yang diketahui. Sebelum beralih daripada demo buku nota ke aliran kerja sebenar, tentukan kawalan tentang apa yang ejen boleh lihat, klik, dan hantar.

1. **Hadkan persekitaran pelayaran.** Jalankan ejen dalam profil pelayar khusus atau sandbox, dan hadkan kepada domain yang diperlukan untuk tugas.
2. **Pisahkan pemerhatian daripada tindakan.** Benarkan ejen mencari, membaca, dan mengekstrak data dahulu; perlukan langkah kelulusan eksplisit sebelum menghantar borang, menghantar mesej, menempah perjalanan, membuat pembelian, memadam rekod, atau mengubah tetapan akaun.
3. **Jangan letakkan rahsia dalam arahan dan jejak.** Jangan letakkan kata laluan, butiran pembayaran, kuki sesi, atau data peribadi mentah dalam konteks model. Benarkan pengguna mengambil alih untuk pengesahan dan merahsiakan medan sensitif dari log.
4. **Anggap kandungan halaman sebagai input tidak dipercayai.** Sesuatu laman web boleh mengandungi arahan untuk ejen, bukan pengguna. Ejen harus mengabaikan teks halaman yang meminta ia mengubah matlamat, mendedahkan data, mematikan perlindungan, atau melawat laman tidak berkaitan.
5. **Gunakan semakan deterministik untuk langkah berisiko.** Sahkan URL semasa, tajuk halaman, item terpilih, harga, penerima, dan ringkasan tindakan dengan kod sebelum meminta pengguna meluluskan langkah akhir.
6. **Tetapkan bajet dan syarat hentian.** Hadkan bilangan tindakan, cubaan semula, tab, dan minit yang ejen boleh gunakan. Berhenti apabila keadaan halaman samar daripada terus klik.
7. **Rekod bukti berguna, bukan semuanya.** Simpan ringkasan tindakan, cap masa, URL, deskripsi elemen terpilih, dan rujukan tangkapan skrin supaya kegagalan dapat disemak tanpa menyimpan kandungan halaman sensitif yang tidak perlu.

Dalam contoh Airbnb, lalai selamat adalah untuk mencari listing dan mengekstrak harga. Log masuk, menghubungi hos, atau melengkapkan tempahan harus menjadi tindakan berasingan yang disahkan pengguna.

### Aplikasi Dunia Sebenar

- Tempahan perjalanan dan pemantauan harga
- Perbandingan harga e-dagang dan semakan ketersediaan
- Ekstraksi berstruktur dari laman web dinamik
- Ujian dan verifikasi UI berasaskan visi
- Pemantauan dan pemberitahuan laman web
- Pengisian borang pintar merentasi aliran multi-langkah

## Contoh Dunia Sebenar: Microsoft Project Opal

Ejen yang anda bina dalam pelajaran ini adalah versi kecil, tempatan bagi **ejen penggunaan komputer (CUA)** — program yang menggerakkan pelayar seperti manusia. Microsoft membawa idea yang sama ke perusahaan dengan **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, satu kemampuan dalam Microsoft 365 Copilot.

Dengan Project Opal, anda menggambarkan tugas dan ejen bekerja bagi pihak anda menggunakan **penggunaan komputer pada PC Awan Windows 365 yang selamat**, beroperasi merentasi aplikasi berasaskan pelayar, laman, dan data organisasi anda. Ia berfungsi **secara asinkron di latar belakang**, dan anda boleh mengarahkan kerja atau mengambil kawalan pada bila-bila masa. Contoh kerja termasuk:

- Mengurus permintaan keanggotaan kumpulan keselamatan
- Mengumpul dan mengesahkan bukti audit untuk semakan pematuhan
- Menilai insiden IT (mengemas kini status tiket, menetapkan pemilik, menutup duplikat)
- Mengumpulkan data Excel ke dalam dek penutupan kewangan

Opal adalah rujukan berguna untuk bagaimana **ejen penggunaan komputer yang boleh dipercayai dan berperingkat pengeluaran** kelihatan — dan ia mengukuhkan konsep dari pelajaran terdahulu:

| Konsep dalam kursus ini | Bagaimana Project Opal menerapkannya |
|------------------------|-----------------------------|
| **Manusia dalam gelung** (Pelajaran 06) | Opal berhenti untuk maklumat log masuk, data sensitif, atau arahan samar, dan tidak pernah memasukkan kata laluan atau menghantar borang tanpa pengesahan jelas. Anda boleh *Mengambil Kawalan* dan *Mengembalikan Kawalan* di tengah tugas. |
| **Ejen boleh dipercayai & selamat** (Pelajaran 06 & 18) | Berjalan dalam PC Awan Windows 365 terasing, secara lalai hanya pelayar dibenarkan (akses komputer lain disekat, dikuatkuasakan melalui Intune), menggunakan identiti *anda* jadi hanya mengakses apa yang dibenarkan, dan merekod setiap tindakan untuk audit. |
| **Perancangan & metakognisi** (Pelajaran 07 & 09) | Opal menjana rancangan untuk kerja terlebih dahulu, kemudian memantau penalarannya sendiri di setiap langkah dan berhenti jika mengesan aktiviti mencurigakan. |
| **Keupayaan / alat boleh guna semula** (Pelajaran 04) | **Kemahiran** membolehkan anda menulis arahan untuk kerja berulang (diimport dari fail `.md` atau ditulis dengan Opal) dan menggunakannya semula dalam perbualan. |

> **Ketersediaan:** Project Opal kini tersedia kepada pengguna dalam [program akses awal Frontier](https://adoption.microsoft.com/copilot/frontier-program/) dengan langganan Microsoft 365 Copilot, dan pentadbir anda mesti melengkapkan persediaan. Oleh kerana ia ciri eksperimental Frontier, keupayaan mungkin berubah dari semasa ke semasa.

## Semakan Pengetahuan

Uji pemahaman anda sebelum beralih ke pelajaran seterusnya.

**1. Bila ejen penggunaan komputer berasaskan pelayar lebih sesuai berbanding aliran kerja hanya API?**

<details>
<summary>Jawapan</summary>

Gunakan ejen pelayar apabila tugas bergantung pada apa yang kelihatan dalam UI web, laman tidak mendedahkan API yang diperlukan, atau halaman sering berubah sehingga logik API atau penentu yang tetap akan rapuh. Jika API stabil wujud bagi tugas sama, pilih API kerana biasanya lebih cepat, mudah diuji, dan mudah diamankan.
</details>

**2. Dalam aliran kerja hibrid, bahagian mana yang harus dikendalikan oleh ejen dan bahagian mana yang harus dikendalikan oleh kod Playwright langsung?**

<details>
<summary>Jawapan</summary>

Biarkan ejen mengendalikan navigasi terbuka dan keadaan UI dinamik, seperti mencari halaman yang betul atau menolak pop-up yang tidak dijangka. Beralih ke kawalan Playwright langsung apabila struktur halaman diketahui dan tindakan memerlukan ketepatan, cubaan semula, tunggu, atau pengesahan deterministik.
</details>

**3. Contoh Airbnb menemui listing yang pengguna mungkin mahu tempah. Apa yang harus berlaku sebelum aliran kerja log masuk, menghubungi hos, atau melengkapkan tempahan?**

<details>
<summary>Jawapan</summary>

Aliran kerja harus berhenti dan meminta kelulusan pengguna secara eksplisit. Sebelum meminta, ia harus menunjukkan ringkasan jelas listing terpilih, URL semasa, harga, tarikh, dan tindakan yang dimaksudkan. Pencarian dan ekstraksi harga boleh autonomi; akses akaun, mesej, pembelian, dan tempahan harus mendapat persetujuan pengguna.
</details>

**4. Sebuah halaman web memberitahu ejen untuk mengabaikan arahan asalnya, melawat laman lain, dan mendedahkan kelayakan tersimpan. Bagaimana ejen harus melayan teks itu?**

<details>
<summary>Jawapan</summary>

Anggap ia sebagai kandungan halaman yang tidak dipercayai, bukan arahan pembangun atau pengguna. Ejen harus kekal dalam domain dan skop tugas yang dibenarkan, enggan mendedahkan rahsia, dan elakkan mengikuti teks halaman yang mengubah matlamat, mematikan perlindungan, atau menghantarnya ke laman tidak berkaitan.
</details>

**5. Bukti apa yang berguna untuk disimpan apabila ejen pelayar berjalan, dan apa yang harus dielakkan?**

<details>
<summary>Jawapan</summary>

Simpan ringkasan tindakan, cap masa, URL, deskripsi elemen terpilih, keputusan pengesahan, dan rujukan tangkapan skrin supaya larian boleh disemak. Elakkan menyimpan kata laluan, butiran pembayaran, kuki sesi, data peribadi mentah, atau kandungan penuh halaman kecuali ada sebab penyimpanan dan privasi khusus.
</details>

## Sumber Tambahan

- [Mulakan dengan Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Templat integrasi Browser-Use Playwright](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Parameter pelakon Browser-Use dan ekstraksi kandungan](https://docs.browser-use.com/customize/actor/all-parameters)
- [Persediaan Kursus](../00-course-setup/README.md)

## Pelajaran Sebelumnya

[Meneroka Kerangka Ejen Microsoft](../14-microsoft-agent-framework/README.md)

## Pelajaran Seterusnya

[Menyebarkan Ejen Skala Besar](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->