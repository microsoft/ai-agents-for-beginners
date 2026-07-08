# Membina Ejen Penggunaan Komputer (CUA)

Ejen penggunaan komputer boleh berinteraksi dengan laman web sama seperti manusia: dengan membuka pelayar, memeriksa halaman, dan mengambil tindakan terbaik seterusnya berdasarkan apa yang mereka lihat. Dalam pelajaran ini, anda akan membina ejen automasi pelayar yang mencari Airbnb, mengekstrak data senarai berstruktur, dan mengenal pasti penginapan paling murah di Stockholm.

Pelajaran ini menggabungkan Browser-Use untuk navigasi dipacu AI, Playwright dan Protokol DevTools Chrome (CDP) untuk kawalan pelayar, Azure OpenAI untuk penalaran berasaskan visi, dan Pydantic untuk ekstraksi berstruktur.

## Pengenalan

Pelajaran ini akan merangkumi:

- Memahami bila ejen penggunaan komputer lebih sesuai daripada automasi berasaskan API sahaja
- Menggabungkan Browser-Use dengan Playwright dan CDP untuk pengurusan kitaran hayat pelayar yang boleh dipercayai
- Menggunakan Azure OpenAI visi dan output Pydantic berstruktur untuk mengekstrak data senarai dari halaman web dinamik
- Memutuskan bila untuk menggunakan aliran kerja automasi pelayar berasaskan ejen-utama, pelaku-utama, atau hibrid

## Matlamat Pembelajaran

Selepas melengkapkan pelajaran ini, anda akan tahu bagaimana untuk:

- Mengkonfigurasi Browser-Use dengan Azure OpenAI dan Playwright
- Membina aliran kerja automasi pelayar yang melayari laman web sebenar dan mengendalikan elemen UI dinamik
- Mengekstrak hasil yang ditaip dari kandungan halaman yang kelihatan dan mengubahnya menjadi logik perniagaan hiliran
- Memilih antara pola ejen dan pelaku berdasarkan betapa boleh jangka tugasan pelayar itu

## Contoh Kod

Pelajaran ini merangkumi satu tutorial buku nota:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Melancarkan sesi Chrome menggunakan CDP, mencari senarai Stockholm di Airbnb, mengekstrak harga dengan visi Browser-Use, dan memulangkan pilihan paling murah sebagai data berstruktur.

## Prasyarat

- Python 3.12+
- Penempatan Azure OpenAI disediakan dalam persekitaran anda
- Chrome atau Chromium dipasang secara tempatan
- Pergantungan Playwright dipasang
- Kefahaman asas tentang Python async

## Persediaan

Pasang pakej yang digunakan dalam buku nota:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Tetapkan pemboleh ubah persekitaran Azure OpenAI yang digunakan oleh buku nota:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Pilihan: menggunakan versi API terkini secara lalai apabila dihilangkan
AZURE_OPENAI_API_VERSION=...
```

## Gambaran Keseluruhan Seni Bina

Buku nota ini menunjukkan aliran kerja automasi pelayar hibrid:

1. Chrome dimulakan dengan CDP diaktifkan supaya Playwright dan Browser-Use boleh berkongsi sesi pelayar yang sama.
2. Ejen Browser-Use mengendalikan tugasan navigasi terbuka seperti membuka Airbnb, menutup pop-up, dan mencari Stockholm.
3. Halaman aktif diperiksa dengan skema Pydantic berstruktur untuk mengekstrak tajuk senarai, harga malam, penarafan, dan URL.
4. Logik Python membandingkan senarai yang diekstrak dan menonjolkan hasil paling murah.

Pendekatan ini mengekalkan penalaran berasaskan visi yang fleksibel yang Browser-Use mahir sambil tetap memberi anda kawalan pelayar deterministik apabila diperlukan.

## Perkara Penting dan Amalan Terbaik

### Bila Menggunakan Ejen vs Pelaku

| Senario | Gunakan Ejen | Gunakan Pelaku |
|----------|-----------|-----------|
| Susun atur dinamik | Ya, AI boleh menyesuaikan dengan perubahan halaman | Tidak, pemilih rapuh boleh rosak |
| Struktur diketahui | Tidak, ejen lebih perlahan daripada kawalan langsung | Ya, cepat dan tepat |
| Mencari elemen | Ya, bahasa semula jadi berfungsi dengan baik | Tidak, pemilih tepat diperlukan |
| Kawalan masa | Tidak, kurang boleh dijangka | Ya, kawalan penuh ke atas tunggu dan cuba semula |
| Aliran kerja kompleks | Ya, mengendalikan keadaan UI tidak dijangka | Tidak, memerlukan pencabangan jelas |

### Amalan Terbaik Browser-Use

1. Mulakan dengan ejen untuk penerokaan dan navigasi dinamik.
2. Tukar kepada kawalan halaman langsung apabila interaksi menjadi boleh diramal.
3. Gunakan model output berstruktur supaya data yang diekstrak disahkan dan selamat jenis.
4. Tambah kelewatan secara strategik selepas tindakan yang mencetuskan perubahan UI yang kelihatan.
5. Tangkap tangkapan skrin semasa iterasi supaya kegagalan lebih mudah dibaiki.
6. Jangka laman web berubah dan reka strategi sandaran untuk pop-up dan peralihan susun atur.
7. Padankan pola ejen dan pelaku untuk mendapatkan kedua-dua fleksibiliti dan ketepatan.

### Aplikasi Dunia Sebenar

- Tempahan perjalanan dan pemantauan harga
- Perbandingan harga e-dagang dan pemeriksaan ketersediaan
- Ekstraksi berstruktur dari laman web dinamik
- Ujian dan pengesahan UI berasaskan visi
- Pemantauan laman web dan pemberitahuan
- Pengisian borang pintar merentas aliran berbilang langkah

## Contoh Dunia Sebenar: Microsoft Project Opal

Ejen yang anda bina dalam pelajaran ini adalah versi kecil, tempatan bagi **ejen penggunaan komputer (CUA)** — program yang mengendalikan pelayar seperti seorang manusia. Microsoft membawa idea yang sama ini ke perniagaan dengan **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, satu keupayaan dalam Microsoft 365 Copilot.

Dengan Project Opal, anda menerangkan tugasan dan ejen bekerja bagi pihak anda menggunakan **penggunaan komputer pada Windows 365 Cloud PC yang selamat**, beroperasi merentas aplikasi pelayar, laman web, dan data organisasi anda. Ia berfungsi **secara tak segerak di latar belakang**, dan anda boleh membimbing kerja atau mengambil kawalan pada bila-bila masa. Contoh tugasan termasuk:

- Mengurus permintaan keanggotaan kumpulan keselamatan
- Mengumpul dan mengesahkan bukti audit untuk semakan pematuhan
- Menyelesaikan insiden IT (mengemas kini status tiket, menugaskan pemilik, menutup pendua)
- Menyusun data Excel ke dalam dek penutupan kewangan

Opal adalah rujukan berguna untuk bagaimana rupa ejen penggunaan komputer yang **berkualiti produksi dan boleh dipercayai** — dan ia menguatkan konsep dari pelajaran terdahulu:

| Konsep dalam kursus ini | Bagaimana Project Opal mengaplikasikannya |
|------------------------|-----------------------------|
| **Manusia dalam gelung** (Pelajaran 06) | Opal berhenti untuk bukti login, data sensitif, atau arahan yang samar, dan tidak pernah memasukkan kata laluan atau menghantar borang tanpa pengesahan jelas. Anda boleh *Mengambil Kawalan* dan *Mengembalikan Kawalan* di tengah tugasan. |
| **Ejen yang boleh dipercayai & selamat** (Pelajaran 06 & 18) | Berjalan dalam Windows 365 Cloud PC berasingan, hanya pelayar secara lalai (akses komputer lain disekat, dikuatkuasakan melalui Intune), menggunakan *identiti anda* jadi hanya mengakses apa yang anda dibenarkan, dan merekod setiap tindakan untuk audit. |
| **Perancangan & metakognisi** (Pelajaran 07 & 09) | Opal menghasilkan pelan untuk tugasan terlebih dahulu, kemudian menyelia penalarannya sendiri pada setiap langkah dan berhenti jika mengesan aktiviti mencurigakan. |
| **Keupayaan / alat boleh guna semula** (Pelajaran 04) | **Kemahiran** membolehkan anda menulis arahan untuk tugasan boleh ulang (diimport dari fail `.md` atau ditulis dengan Opal) dan menggunakannya semula dalam perbualan. |

> **Ketersediaan:** Project Opal kini tersedia untuk pengguna dalam [program akses awal Frontier](https://adoption.microsoft.com/copilot/frontier-program/) dengan langganan Microsoft 365 Copilot, dan pentadbir anda mesti melengkapkan persediaan. Kerana ia adalah ciri Frontier eksperimen, keupayaan mungkin berubah dari masa ke masa.

## Sumber Tambahan

- [Mulakan dengan Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Templat integrasi Playwright Browser-Use](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Parameter pelaku dan ekstraksi kandungan Browser-Use](https://docs.browser-use.com/customize/actor/all-parameters)
- [Persediaan Kursus](../00-course-setup/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->