# Membangun Agen Penggunaan Komputer (CUA)

Agen penggunaan komputer dapat berinteraksi dengan situs web sama seperti orang: dengan membuka browser, memeriksa halaman, dan mengambil tindakan terbaik berikutnya dari apa yang mereka lihat. Dalam pelajaran ini, Anda akan membangun agen otomatisasi browser yang mencari Airbnb, mengekstrak data daftar terstruktur, dan mengidentifikasi penginapan termurah di Stockholm.

Pelajaran ini menggabungkan Browser-Use untuk navigasi yang digerakkan oleh AI, Playwright dan Chrome DevTools Protocol (CDP) untuk kontrol browser, Azure OpenAI untuk penalaran berbasis visi, dan Pydantic untuk ekstraksi terstruktur.

## Pendahuluan

Pelajaran ini akan membahas:

- Memahami kapan agen penggunaan komputer lebih cocok daripada otomatisasi berbasis API saja
- Menggabungkan Browser-Use dengan Playwright dan CDP untuk pengelolaan siklus hidup browser yang dapat diandalkan
- Menggunakan Azure OpenAI vision dan output Pydantic terstruktur untuk mengekstrak data daftar dari halaman web dinamis
- Memutuskan kapan menggunakan alur kerja otomatisasi browser agen-pertama, aktor-pertama, atau hibrida

## Tujuan Pembelajaran

Setelah menyelesaikan pelajaran ini, Anda akan tahu cara:

- Mengonfigurasi Browser-Use dengan Azure OpenAI dan Playwright
- Membangun alur kerja otomatisasi browser yang menavigasi situs nyata dan menangani elemen UI dinamis
- Mengekstraksi hasil yang bertipe dari konten halaman yang terlihat dan mengubahnya menjadi logika bisnis hilir
- Memilih antara pola agen dan aktor berdasarkan seberapa dapat diprediksi tugas browser

## Contoh Kode

Pelajaran ini mencakup satu tutorial notebook:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Meluncurkan sesi Chrome melalui CDP, mencari daftar Airbnb untuk Stockholm, mengekstrak harga dengan visi Browser-Use, dan mengembalikan opsi termurah sebagai data terstruktur.

## Prasyarat

- Python 3.12+
- Penyiapan deployment Azure OpenAI di lingkungan Anda
- Chrome atau Chromium terinstal secara lokal
- Ketergantungan Playwright terpasang
- Familiaritas dasar dengan Python async

## Pengaturan

Pasang paket-paket yang digunakan dalam notebook:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Tetapkan variabel lingkungan Azure OpenAI yang digunakan oleh notebook:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Opsional: menggunakan versi API terbaru jika tidak disertakan
AZURE_OPENAI_API_VERSION=...
```

## Ikhtisar Arsitektur

Notebook ini menunjukkan alur kerja otomatisasi browser hibrida:

1. Chrome dimulai dengan CDP diaktifkan sehingga Playwright dan Browser-Use dapat berbagi sesi browser yang sama.
2. Agen Browser-Use menangani tugas navigasi yang terbuka seperti membuka Airbnb, menutup pop-up, dan mencari Stockholm.
3. Halaman aktif diperiksa dengan skema Pydantic terstruktur untuk mengekstrak judul daftar, harga per malam, peringkat, dan URL.
4. Logika Python membandingkan daftar yang diekstrak dan menyoroti hasil termurah.

Pendekatan ini mempertahankan penalaran berbasis visi yang fleksibel yang dimiliki Browser-Use sambil tetap memberikan kontrol browser yang deterministik saat Anda membutuhkannya.

## Pelajaran Penting dan Praktik Terbaik

### Kapan Menggunakan Agen vs Aktor

| Skenario | Gunakan Agen | Gunakan Aktor |
|----------|--------------|------------|
| Tata letak dinamis | Ya, AI dapat beradaptasi dengan perubahan halaman | Tidak, selector rapuh bisa rusak |
| Struktur yang diketahui | Tidak, agen lebih lambat daripada kontrol langsung | Ya, cepat dan tepat |
| Mencari elemen | Ya, bahasa alami bekerja dengan baik | Tidak, selector tepat diperlukan |
| Kontrol waktu | Tidak, kurang dapat diprediksi | Ya, kontrol penuh atas waktu tunggu dan percobaan ulang |
| Alur kerja kompleks | Ya, menangani status UI yang tidak terduga | Tidak, membutuhkan percabangan eksplisit |

### Praktik Terbaik Browser-Use

1. Mulailah dengan agen untuk eksplorasi dan navigasi dinamis.
2. Beralih ke kontrol halaman langsung saat interaksi menjadi dapat diprediksi.
3. Gunakan model output terstruktur agar data yang diekstrak tervalidasi dan aman tipe.
4. Tambahkan penundaan secara strategis setelah tindakan yang memicu perubahan UI yang terlihat.
5. Ambil tangkapan layar saat iterasi sehingga kegagalan lebih mudah untuk debug.
6. Harapkan situs web berubah dan rancang strategi fallback untuk pop-up dan pergeseran tata letak.
7. Gabungkan pola agen dan aktor untuk mendapatkan fleksibilitas dan presisi.

### Pengaman Keamanan untuk Agen Browser

Agen browser beroperasi di situs web langsung, jadi mereka membutuhkan batasan yang lebih ketat dibandingkan skrip yang hanya memanggil API yang diketahui. Sebelum beralih dari demo notebook ke alur kerja nyata, definisikan kontrol tentang apa yang dapat dilihat, diklik, dan dikirim oleh agen.

1. **Batas lingkungan penjelajahan.** Jalankan agen dalam profil browser atau sandbox yang terpisah, dan batasi hanya pada domain yang diperlukan untuk tugas.
2. **Pisahkan pengamatan dari tindakan.** Biarkan agen mencari, membaca, dan mengekstrak data terlebih dahulu; memerlukan langkah persetujuan eksplisit sebelum mengirimkan formulir, mengirim pesan, memesan perjalanan, melakukan pembelian, menghapus catatan, atau mengubah pengaturan akun.
3. **Jaga rahasia dari prompt dan jejak.** Jangan letakkan kata sandi, rincian pembayaran, cookie sesi, atau data pribadi mentah dalam konteks model. Biarkan pengguna mengambil alih untuk autentikasi dan menyunting bidang sensitif dari log.
4. **Perlakukan konten halaman sebagai input yang tidak dipercaya.** Situs web dapat berisi instruksi yang ditujukan untuk agen, bukan pengguna. Agen harus mengabaikan teks halaman yang memintanya mengubah tujuan, mengungkap data, menonaktifkan pengaman, atau mengunjungi situs yang tidak terkait.
5. **Gunakan pemeriksaan deterministik pada langkah berisiko.** Verifikasi URL saat ini, judul halaman, item yang dipilih, harga, penerima, dan ringkasan tindakan dengan kode sebelum meminta pengguna menyetujui langkah akhir.
6. **Tetapkan anggaran dan kondisi berhenti.** Batasi jumlah tindakan, percobaan ulang, tab, dan menit yang bisa digunakan agen. Hentikan saat status halaman ambigu daripada melanjutkan klik.
7. **Rekam bukti yang berguna, bukan semuanya.** Simpan ringkasan tindakan, cap waktu, URL, deskripsi elemen terpilih, dan referensi tangkapan layar sehingga kegagalan dapat ditinjau tanpa menyimpan konten halaman sensitif yang tidak perlu.

Dalam contoh Airbnb, default aman adalah mencari daftar dan mengekstrak harga. Masuk, menghubungi host, atau menyelesaikan pemesanan harus menjadi tindakan yang disetujui pengguna secara terpisah.

### Aplikasi Dunia Nyata

- Pemesanan perjalanan dan pemantauan harga
- Perbandingan harga e-commerce dan pengecekan ketersediaan
- Ekstraksi terstruktur dari situs web dinamis
- Pengujian dan verifikasi UI berbasis visi
- Pemantauan dan pemberitahuan situs web
- Pengisian formulir cerdas di alur multi-langkah

## Contoh Dunia Nyata: Microsoft Project Opal

Agen yang Anda bangun dalam pelajaran ini adalah versi kecil dan lokal dari **agen penggunaan komputer (CUA)** — program yang menggerakkan browser seperti halnya manusia. Microsoft menghadirkan ide yang sama ini ke perusahaan melalui **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, kemampuan dalam Microsoft 365 Copilot.

Dengan Project Opal, Anda mendeskripsikan tugas dan agen bekerja atas nama Anda menggunakan **penggunaan komputer pada Windows 365 Cloud PC yang aman**, beroperasi di aplikasi, situs, dan data berbasis browser organisasi Anda. Ia bekerja **secara asinkron di latar belakang**, dan Anda dapat mengarahkan pekerjaan atau mengambil alih kontrol kapan saja. Contoh pekerjaan meliputi:

- Mengelola permintaan keanggotaan grup keamanan
- Mengumpulkan dan memvalidasi bukti audit untuk tinjauan kepatuhan
- Melakukan triase insiden TI (memperbarui status tiket, menetapkan pemilik, menutup duplikat)
- Mengompilasi data Excel menjadi laporan penutupan keuangan

Opal adalah referensi yang berguna untuk seperti apa agen penggunaan komputer **bertingkat produksi dan dapat dipercaya** — dan memperkuat konsep dari pelajaran sebelumnya:

| Konsep dalam kursus ini | Cara Project Opal menerapkannya |
|-------------------------|--------------------------------|
| **Human-in-the-loop** (Pelajaran 06) | Opal berhenti untuk kredensial login, data sensitif, atau instruksi ambigu, dan tidak pernah memasukkan kata sandi atau mengirim formulir tanpa konfirmasi eksplisit. Anda dapat *Mengambil Kontrol* dan *Mengembalikan Kontrol* saat tugas berlangsung. |
| **Agen yang dapat dipercaya & aman** (Pelajaran 06 & 18) | Berjalan dalam Windows 365 Cloud PC yang terisolasi, default hanya browser (akses komputer lain diblokir, ditegakkan melalui Intune), menggunakan *identitas Anda* sehingga hanya mengakses apa yang Anda berwenang, dan mencatat setiap tindakan untuk audit. |
| **Perencanaan & metakognisi** (Pelajaran 07 & 09) | Opal membuat rencana untuk tugas terlebih dahulu, kemudian mengawasi penalarannya sendiri di setiap langkah dan berhenti jika mendeteksi aktivitas mencurigakan. |
| **Kemampuan / alat yang dapat digunakan ulang** (Pelajaran 04) | **Keahlian** membiarkan Anda menulis instruksi untuk pekerjaan yang dapat diulang (diimpor dari file `.md` atau dibuat dengan Opal) dan menggunakannya kembali di berbagai percakapan. |

> **Ketersediaan:** Project Opal saat ini tersedia bagi pengguna dalam [program akses awal Frontier](https://adoption.microsoft.com/copilot/frontier-program/) dengan langganan Microsoft 365 Copilot, dan administrator Anda harus menyelesaikan penyiapan. Karena merupakan fitur Frontier eksperimental, kemampuan dapat berubah seiring waktu.

## Pemeriksaan Pengetahuan

Uji pemahaman Anda sebelum melanjutkan ke pelajaran berikutnya.

**1. Kapan agen penggunaan komputer berbasis browser lebih cocok daripada alur kerja berbasis API saja?**

<details>
<summary>Jawaban</summary>

Gunakan agen browser ketika tugas bergantung pada apa yang terlihat dalam UI web, situs tidak menyediakan API yang dibutuhkan, atau halaman sering berubah sehingga logika API atau selector tetap menjadi rapuh. Jika ada API stabil untuk tugas yang sama, lebih baik gunakan API karena biasanya lebih cepat, mudah diuji, dan lebih mudah diamankan.
</details>

**2. Dalam alur kerja hibrida, bagian mana yang sebaiknya ditangani agen dan bagian mana yang sebaiknya ditangani kode Playwright langsung?**

<details>
<summary>Jawaban</summary>

Biarkan agen menangani navigasi terbuka dan status UI dinamis, seperti menemukan halaman yang tepat atau menutup pop-up tak terduga. Beralih ke kontrol Playwright langsung saat struktur halaman diketahui dan tindakan membutuhkan presisi, percobaan ulang, waktu tunggu, atau validasi deterministik.
</details>

**3. Contoh Airbnb menemukan daftar yang mungkin ingin dipesan pengguna. Apa yang seharusnya terjadi sebelum alur kerja masuk, menghubungi host, atau menyelesaikan pemesanan?**

<details>
<summary>Jawaban</summary>

Alur kerja harus berhenti dan meminta persetujuan eksplisit pengguna. Sebelum meminta, harus menunjukkan ringkasan jelas dari daftar yang dipilih, URL saat ini, harga, tanggal, dan tindakan yang dimaksudkan. Pencarian dan ekstraksi harga bisa dilakukan secara otonom; akses akun, pesan, pembelian, dan pemesanan harus disetujui pengguna.
</details>

**4. Sebuah halaman web memberi tahu agen untuk mengabaikan instruksi aslinya, mengunjungi situs lain, dan mengungkap kredensial yang tersimpan. Bagaimana agen harus memperlakukan teks tersebut?**

<details>
<summary>Jawaban</summary>

Perlakukan sebagai konten halaman yang tidak dipercaya, bukan sebagai instruksi pengembang atau pengguna. Agen harus tetap dalam domain dan lingkup tugas yang diizinkan, menolak mengungkap rahasia, dan menghindari mengikuti teks halaman yang mengubah tujuan, menonaktifkan pengaman, atau mengirim ke situs tidak terkait.
</details>

**5. Bukti apa yang berguna disimpan saat agen browser berjalan, dan apa yang harus dihindari?**

<details>
<summary>Jawaban</summary>

Simpan ringkasan tindakan, cap waktu, URL, deskripsi elemen terpilih, hasil validasi, dan referensi tangkapan layar agar jalannya dapat ditinjau. Hindari menyimpan kata sandi, rincian pembayaran, cookie sesi, data pribadi mentah, atau isi halaman penuh kecuali ada alasan retensi dan privasi yang spesifik.
</details>

## Sumber Daya Tambahan

- [Memulai dengan Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Template integrasi Playwright Browser-Use](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Parameter aktor Browser-Use dan ekstraksi konten](https://docs.browser-use.com/customize/actor/all-parameters)
- [Pengaturan Kursus](../00-course-setup/README.md)

## Pelajaran Sebelumnya

[Menjelajahi Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

## Pelajaran Selanjutnya

[Menerapkan Agen yang Dapat Diskalakan](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->