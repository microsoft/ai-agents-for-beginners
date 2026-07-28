# Membangun Ejen Penggunaan Komputer (CUA)

Ejen penggunaan komputer boleh berinteraksi dengan laman web dengan cara yang sama seperti manusia: dengan membuka pelayar, memeriksa halaman, dan mengambil tindakan terbaik seterusnya berdasarkan apa yang mereka lihat. Dalam pelajaran ini, anda akan membina ejen automasi pelayar yang mencari Airbnb, mengekstrak data senarai berstruktur, dan mengenal pasti penginapan termurah di Stockholm.

Pelajaran ini menggabungkan Penggunaan Pelayar untuk navigasi yang dipacu AI, Playwright dan Protokol DevTools Chrome (CDP) untuk kawalan pelayar, Azure OpenAI untuk penalaran berasaskan visi, dan Pydantic untuk ekstraksi berstruktur.

## Pengenalan

Pelajaran ini merangkumi:

- Memahami bila ejen penggunaan komputer lebih sesuai daripada automasi hanya API
- Menggabungkan Penggunaan Pelayar dengan Playwright dan CDP untuk pengurusan kitaran hayat pelayar yang boleh dipercayai
- Menggunakan visi Azure OpenAI dan output berstruktur Pydantic untuk mengekstrak data senarai daripada halaman web dinamik
- Memutuskan bila menggunakan aliran kerja automasi pelayar berasaskan ejen, pelakon, atau gabungan

## Matlamat Pembelajaran

Selepas menamatkan pelajaran ini, anda akan tahu bagaimana untuk:

- Mengkonfigurasikan Penggunaan Pelayar dengan Azure OpenAI dan Playwright
- Membangun aliran kerja automasi pelayar yang menavigasi laman web sebenar dan mengendalikan elemen UI dinamik
- Mengekstrak hasil yang ditaip daripada kandungan halaman yang kelihatan dan mengubahnya menjadi logik perniagaan seterusnya
- Memilih antara corak ejen dan pelakon berdasarkan seberapa boleh diramal tugas pelayar

## Contoh Kod

Pelajaran ini merangkumi satu tutorial notebook:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Melancarkan sesi Chrome melalui CDP, mencari senarai Airbnb untuk Stockholm, mengekstrak harga dengan visi Penggunaan Pelayar, dan mengembalikan pilihan termurah sebagai data berstruktur.

## Prasyarat

- Python 3.12+
- Penempatan Azure OpenAI dikonfigurasikan dalam persekitaran anda
- Chrome atau Chromium dipasang secara tempatan
- Pergantungan Playwright dipasang
- Kefahaman asas tentang Python async

## Persediaan

Pasang pakej yang digunakan dalam notebook:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Tetapkan pembolehubah persekitaran Azure OpenAI yang digunakan oleh notebook:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Pilihan: lalai kepada versi API terkini apabila diabaikan
AZURE_OPENAI_API_VERSION=...
```

## Gambaran Keseluruhan Senibina

Notebook ini menunjukkan aliran kerja automasi pelayar hibrid:

1. Chrome bermula dengan CDP diaktifkan supaya Playwright dan Penggunaan Pelayar boleh berkongsi sesi pelayar yang sama.
2. Ejen Penggunaan Pelayar mengendalikan tugas navigasi terbuka seperti membuka Airbnb, menolak pop-up, dan mencari Stockholm.
3. Halaman aktif diperiksa dengan skema Pydantic berstruktur untuk mengekstrak tajuk senarai, harga malam, penilaian, dan URL.
4. Logik Python membandingkan senarai yang diekstrak dan menyerlahkan hasil termurah.

Pendekatan ini mengekalkan penalaran berasaskan visi yang fleksibel yang Penggunaan Pelayar mahir sambil masih memberi anda kawalan pelayar deterministik apabila anda memerlukannya.

## Perkara Penting dan Amalan Terbaik

### Bila Menggunakan Ejen vs Pelakon

| Senario | Gunakan Ejen | Gunakan Pelakon |
|----------|-----------|-----------|
| Susun atur dinamik | Ya, AI boleh menyesuaikan dengan perubahan halaman | Tidak, pemilih rapuh boleh rosak |
| Struktur diketahui | Tidak, ejen lebih perlahan daripada kawalan langsung | Ya, pantas dan tepat |
| Mencari elemen | Ya, bahasa semula jadi berfungsi dengan baik | Tidak, pemilih tepat diperlukan |
| Kawalan masa | Tidak, kurang boleh diramal | Ya, kawalan penuh ke atas masa menunggu dan percubaan semula |
| Aliran kerja kompleks | Ya, mengendalikan keadaan UI yang tidak dijangka | Tidak, memerlukan percabangan eksplisit |

### Amalan Terbaik Penggunaan Pelayar

1. Mulakan dengan ejen untuk penerokaan dan navigasi dinamik.
2. Beralih ke kawalan halaman langsung apabila interaksi menjadi boleh diramal.
3. Gunakan model output berstruktur supaya data yang diekstrak disahkan dan selamat jenis.
4. Tambah kelewatan secara strategik selepas tindakan yang mencetuskan perubahan UI yang kelihatan.
5. Tangkap tangkapan layar semasa iterasi supaya kegagalan lebih mudah untuk dibaiki.
6. Jangka laman web berubah dan reka strategi sandaran untuk pop-up dan pergeseran susun atur.
7. Gabungkan corak ejen dan pelakon untuk mendapatkan fleksibiliti dan ketepatan.

### Panduan Keselamatan untuk Ejen Pelayar

Ejen pelayar beroperasi di laman web langsung, jadi mereka memerlukan batasan lebih ketat berbanding skrip yang hanya memanggil API yang diketahui. Sebelum beralih dari demo notebook ke aliran kerja sebenar, tetapkan kawalan mengenai apa yang ejen boleh lihat, klik, dan hantar.

1. **Hadkan persekitaran pelayaran.** Jalankan ejen dalam profil pelayar khusus atau sandbox, dan hadkan kepada domain yang diperlukan untuk tugas tersebut.
2. **Pisahkan pemerhatian daripada tindakan.** Biarkan ejen mencari, membaca, dan mengekstrak data terlebih dahulu; perlukan langkah kelulusan eksplisit sebelum ia menghantar borang, menghantar mesej, menempah perjalanan, membuat pembelian, memadam rekod, atau mengubah tetapan akaun.
3. **Jangan letak rahsia dalam arahan dan jejak.** Jangan letakkan kata laluan, maklumat pembayaran, kuki sesi, atau data peribadi mentah dalam konteks model. Biarkan pengguna mengambil alih untuk pengesahan dan menyembunyikan medan sensitif dari log.
4. **Anggap kandungan halaman sebagai input yang tidak dipercayai.** Laman web boleh mengandungi arahan yang ditujukan kepada ejen, bukan pengguna. Ejen harus mengabaikan teks halaman yang mengarahkannya mengubah matlamat, mendedahkan data, melumpuhkan keselamatan, atau melawat laman yang tidak berkaitan.
5. **Gunakan pemeriksaan deterministik sekitar langkah berisiko.** Sahkan URL semasa, tajuk halaman, item yang dipilih, harga, penerima, dan ringkasan tindakan dengan kod sebelum meminta kelulusan pengguna untuk langkah akhir.
6. **Tetapkan bajet dan syarat hentian.** Hadkan bilangan tindakan, percubaan semula, tab, dan minit yang ejen boleh gunakan. Henti apabila keadaan halaman samar daripada meneruskan klik.
7. **Rekod bukti berguna, bukan semuanya.** Simpan ringkasan tindakan, cap waktu, URL, keterangan elemen yang dipilih, dan rujukan tangkapan layar supaya kegagalan boleh dikaji tanpa menyimpan kandungan halaman sensitif yang tidak perlu.

Dalam contoh Airbnb, lalai selamat adalah mencari senarai dan mengekstrak harga. Log masuk, menghubungi hos, atau menamatkan tempahan harus menjadi tindakan berasingan yang diluluskan pengguna.

### Aplikasi Dunia Nyata

- Tempahan perjalanan dan pemantauan harga
- Perbandingan harga e-dagang dan pemeriksaan ketersediaan
- Ekstraksi berstruktur dari laman web dinamik
- Ujian UI berasaskan visi dan pengesahan
- Pemantauan laman web dan amaran
- Pengisian borang pintar merentasi aliran multi-langkah

## Contoh Dunia Nyata: Projek Microsoft Opal

Ejen yang anda bina dalam pelajaran ini adalah versi kecil, tempatan dari **ejen penggunaan komputer (CUA)** — program yang menggerakkan pelayar seperti manusia. Microsoft membawa idea yang sama ini ke perusahaan dengan **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, satu keupayaan dalam Microsoft 365 Copilot.

Dengan Project Opal, anda menerangkan tugas dan ejen bekerja bagi pihak anda menggunakan **penggunaan komputer pada Windows 365 Cloud PC yang selamat**, beroperasi di seluruh aplikasi, tapak web, dan data berasaskan pelayar organisasi anda. Ia berfungsi **secara tak segerak di latar belakang**, dan anda boleh mengarahkan kerja atau mengambil kawalan bila-bila masa. Contoh tugasan termasuk:

- Mengurus permintaan keahlian kumpulan keselamatan
- Mengumpul dan mengesahkan bukti audit untuk tinjauan pematuhan
- Menvaluasi insiden IT (mengemas kini status tiket, menetapkan pemilik, menutup pendua)
- Menyusun data Excel ke dalam dek penutupan kewangan

Opal adalah rujukan berguna untuk rupa agen penggunaan komputer **kelas produksi dan boleh dipercayai** — dan ia mengukuhkan konsep dari pelajaran terdahulu:

| Konsep dalam kursus ini | Bagaimana Project Opal mengaplikasikannya |
|------------------------|-----------------------------|
| **Manusia dalam gelung** (Pelajaran 06) | Opal berhenti untuk keterangan log masuk, data sensitif, atau arahan samar, dan tidak pernah memasukkan kata laluan atau menghantar borang tanpa pengesahan eksplisit. Anda boleh *Mengambil Kawalan* dan *Mengembalikan Kawalan* ketika tugas. |
| **Ejen boleh dipercayai & selamat** (Pelajaran 06 & 18) | Berjalan dalam Windows 365 Cloud PC yang terasing, hanya pelayar secara default (akses komputer lain disekat, dikuatkuasakan melalui Intune), menggunakan *identiti anda* supaya hanya mengakses apa yang anda dibenarkan, dan merekod setiap tindakan untuk diaudit. |
| **Perancangan & metakognisi** (Pelajaran 07 & 09) | Opal menjana pelan untuk tugasan terlebih dahulu, kemudian menyelia penalarannya sendiri pada setiap langkah dan berhenti jika mengesan aktiviti mencurigakan. |
| **Kemahiran / alat boleh guna semula** (Pelajaran 04) | **Kemahiran** membolehkan anda menulis arahan untuk tugasan yang boleh diulang (diimport dari fail `.md` atau ditulis dengan Opal) dan menggunakannya semula merentasi perbualan. |

> **Ketersediaan:** Project Opal kini tersedia kepada pengguna dalam [program akses awal Frontier](https://adoption.microsoft.com/copilot/frontier-program/) dengan langganan Microsoft 365 Copilot, dan pentadbir anda mesti melengkapkan persediaan. Kerana ia ciri eksperimen Frontier, keupayaan mungkin berubah dari masa ke masa.

## Sumber Tambahan

- [Memulakan dengan Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Templat integrasi Browser-Use Playwright](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Parameter pelakon Browser-Use dan ekstraksi kandungan](https://docs.browser-use.com/customize/actor/all-parameters)
- [Persediaan Kursus](../00-course-setup/README.md)

## Pelajaran Sebelumnya

[Meneroka Rangka Kerja Ejen Microsoft](../14-microsoft-agent-framework/README.md)

## Pelajaran Seterusnya

[Menyebarkan Ejen Skala Besar](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->