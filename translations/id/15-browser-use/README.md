# Membangun Agen Penggunaan Komputer (CUA)

Agen penggunaan komputer dapat berinteraksi dengan situs web dengan cara yang sama seperti orang: dengan membuka browser, memeriksa halaman, dan mengambil tindakan terbaik berikutnya dari apa yang mereka lihat. Dalam pelajaran ini, Anda akan membangun agen otomasi browser yang mencari Airbnb, mengekstrak data listing terstruktur, dan mengidentifikasi penginapan termurah di Stockholm.

Pelajaran ini menggabungkan Browser-Use untuk navigasi yang didorong oleh AI, Playwright dan Chrome DevTools Protocol (CDP) untuk kontrol browser, Azure OpenAI untuk penalaran yang didukung penglihatan, dan Pydantic untuk ekstraksi terstruktur.

## Pengantar

Pelajaran ini akan membahas:

- Memahami kapan agen penggunaan komputer lebih cocok daripada otomasi hanya API
- Menggabungkan Browser-Use dengan Playwright dan CDP untuk manajemen siklus hidup browser yang andal
- Menggunakan visi Azure OpenAI dan output terstruktur Pydantic untuk mengekstrak data listing dari halaman web dinamis
- Memutuskan kapan menggunakan workflow otomasi browser berbasis agen, aktor, atau hibrida

## Tujuan Pembelajaran

Setelah menyelesaikan pelajaran ini, Anda akan tahu cara:

- Mengonfigurasi Browser-Use dengan Azure OpenAI dan Playwright
- Membangun workflow otomasi browser yang menavigasi situs web nyata dan menangani elemen UI dinamis
- Mengekstrak hasil bertipe dari konten halaman yang terlihat dan mengubahnya menjadi logika bisnis hilir
- Memilih antara pola agen dan aktor berdasarkan seberapa dapat diprediksinya tugas browser

## Contoh Kode

Pelajaran ini mencakup satu tutorial notebook:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Meluncurkan sesi Chrome melalui CDP, mencari listing Stockholm di Airbnb, mengekstrak harga dengan visi Browser-Use, dan mengembalikan opsi termurah sebagai data terstruktur.

## Prasyarat

- Python 3.12+
- Deployment Azure OpenAI dikonfigurasi di lingkungan Anda
- Chrome atau Chromium terpasang secara lokal
- Dependensi Playwright terpasang
- Familiaritas dasar dengan Python async

## Persiapan

Pasang paket yang digunakan dalam notebook:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Atur variabel lingkungan Azure OpenAI yang digunakan oleh notebook:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Opsional: menggunakan versi API terbaru secara default jika dihilangkan
AZURE_OPENAI_API_VERSION=...
```

## Gambaran Arsitektur

Notebook ini menunjukan workflow otomasi browser hibrida:

1. Chrome dimulai dengan CDP diaktifkan sehingga Playwright dan Browser-Use dapat berbagi sesi browser yang sama.
2. Agen Browser-Use menangani tugas navigasi terbuka seperti membuka Airbnb, menutup pop-up, dan mencari Stockholm.
3. Halaman aktif diperiksa dengan skema Pydantic terstruktur untuk mengekstrak judul listing, harga per malam, rating, dan URL.
4. Logika Python membandingkan listing yang diekstrak dan menyoroti hasil termurah.

Pendekatan ini mempertahankan penalaran berbasis penglihatan yang fleksibel yang dikuasai oleh Browser-Use sambil tetap memberi Anda kontrol browser deterministik saat Anda membutuhkannya.

## Poin Penting dan Praktik Terbaik

### Kapan Menggunakan Agen vs Aktor

| Skenario | Gunakan Agen | Gunakan Aktor |
|----------|--------------|--------------|
| Tata letak dinamis | Ya, AI dapat menyesuaikan dengan perubahan halaman | Tidak, pemilih rapuh bisa rusak |
| Struktur dikenal | Tidak, agen lebih lambat dibanding kontrol langsung | Ya, cepat dan tepat |
| Menemukan elemen | Ya, bahasa alami bekerja baik | Tidak, diperlukan pemilih tepat |
| Kontrol waktu | Tidak, kurang dapat diprediksi | Ya, kontrol penuh atas waktu tunggu dan percobaan ulang |
| Workflow kompleks | Ya, menangani keadaan UI tak terduga | Tidak, butuh percabangan eksplisit |

### Praktik Terbaik Browser-Use

1. Mulai dengan agen untuk eksplorasi dan navigasi dinamis.
2. Beralih ke kontrol halaman langsung saat interaksi menjadi dapat diprediksi.
3. Gunakan model output terstruktur agar data yang diekstrak tervalidasi dan aman tipe.
4. Tambahkan penundaan secara strategis setelah tindakan yang memicu perubahan UI yang terlihat.
5. Ambil tangkapan layar saat iterasi agar kegagalan lebih mudah di-debug.
6. Harapkan situs web berubah dan desain strategi cadangan untuk pop-up dan pergeseran tata letak.
7. Gabungkan pola agen dan aktor untuk mendapatkan fleksibilitas dan presisi.

### Pembatas Keamanan untuk Agen Browser

Agen browser beroperasi pada situs web langsung, jadi mereka membutuhkan batasan lebih ketat dibanding skrip yang hanya memanggil API yang diketahui. Sebelum beralih dari demo notebook ke workflow nyata, definisikan kontrol tentang apa yang bisa dilihat, diklik, dan dikirim oleh agen.

1. **Batas lingkungan penjelajahan.** Jalankan agen dalam profil browser atau sandbox khusus, dan batasi hanya pada domain yang diperlukan untuk tugas.
2. **Pisahkan pengamatan dari aksi.** Biarkan agen mencari, membaca, dan mengekstrak data terlebih dahulu; butuhkan langkah persetujuan eksplisit sebelum mengirim formulir, mengirim pesan, memesan perjalanan, melakukan pembelian, menghapus data, atau mengubah pengaturan akun.
3. **Jaga rahasia tetap di luar prompt dan jejak.** Jangan meletakkan password, detail pembayaran, cookie sesi, atau data pribadi mentah di konteks model. Biarkan pengguna yang menangani autentikasi dan menghapus data sensitif dari log.
4. **Perlakukan konten halaman sebagai input tidak terpercaya.** Sebuah situs web dapat berisi instruksi yang ditujukan untuk agen, bukan pengguna. Agen harus mengabaikan teks halaman yang memintanya mengubah tujuan, mengungkap data, menonaktifkan pengaman, atau mengunjungi situs yang tidak terkait.
5. **Gunakan pemeriksaan deterministik di langkah berisiko.** Verifikasi URL saat ini, judul halaman, item yang dipilih, harga, penerima, dan ringkasan aksi dengan kode sebelum meminta persetujuan pengguna untuk langkah akhir.
6. **Tetapkan anggaran dan kondisi berhenti.** Batasi jumlah aksi, percobaan ulang, tab, dan menit yang bisa dipakai agen. Berhenti saat status halaman ambigu daripada terus mengklik.
7. **Rekam bukti yang berguna, bukan semuanya.** Simpan ringkasan aksi, waktu, URL, deskripsi elemen yang dipilih, dan referensi tangkapan layar agar kegagalan dapat ditinjau tanpa menyimpan konten halaman sensitif yang tidak perlu.

Dalam contoh Airbnb, default aman adalah mencari listing dan mengekstrak harga. Masuk, menghubungi host, atau menyelesaikan pemesanan harus menjadi aksi terpisah yang disetujui pengguna.

### Aplikasi Dunia Nyata

- Pemesanan perjalanan dan pemantauan harga
- Perbandingan harga e-commerce dan pengecekan ketersediaan
- Ekstraksi terstruktur dari situs web dinamis
- Pengujian dan verifikasi UI berbasis visi
- Pemantauan dan pemberitahuan situs web
- Pengisian formulir cerdas pada alur multi-langkah

## Contoh Dunia Nyata: Microsoft Project Opal

Agen yang Anda bangun dalam pelajaran ini adalah versi lokal kecil dari **agen penggunaan komputer (CUA)** — program yang menjalankan browser seperti manusia. Microsoft membawa ide yang sama ke perusahaan dengan **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, sebuah kemampuan di Microsoft 365 Copilot.

Dengan Project Opal, Anda mendeskripsikan tugas dan agen bekerja atas nama Anda menggunakan **penggunaan komputer pada Windows 365 Cloud PC yang aman**, beroperasi di seluruh aplikasi, situs, dan data berbasis browser organisasi Anda. Agen bekerja **secara asinkron di latar belakang**, dan Anda dapat memandu kerjaannya atau mengambil kendali kapan saja. Contoh pekerjaan meliputi:

- Mengelola permintaan keanggotaan grup keamanan
- Mengumpulkan dan memvalidasi bukti audit untuk tinjauan kepatuhan
- Menangani insiden TI (memperbarui status tiket, menetapkan pemilik, menutup duplikat)
- Mengompilasi data Excel ke dalam deck penutupan keuangan

Opal adalah referensi berguna untuk seperti apa agen penggunaan komputer yang **berkualitas produksi dan terpercaya** — dan memperkuat konsep dari pelajaran sebelumnya:

| Konsep dalam kursus ini | Bagaimana Project Opal menerapkannya |
|------------------------|------------------------------|
| **Human-in-the-loop** (Pelajaran 06) | Opal berhenti untuk kredensial login, data sensitif, atau instruksi ambigu, dan tidak pernah memasukkan password atau mengirim formulir tanpa konfirmasi eksplisit. Anda dapat *Mengambil Kendali* dan *Mengembalikan Kendali* di tengah tugas. |
| **Agen terpercaya & aman** (Pelajaran 06 & 18) | Berjalan di Windows 365 Cloud PC terisolasi, hanya browser secara default (akses komputer lain diblokir via Intune), menggunakan identitas *Anda* sehingga hanya mengakses yang Anda otorisasi, dan mencatat setiap aksi untuk auditabilitas. |
| **Perencanaan & metakognisi** (Pelajaran 07 & 09) | Opal membuat rencana pekerjaan terlebih dahulu, lalu mengawasi penalarannya sendiri di setiap langkah dan berhenti jika mendeteksi aktivitas mencurigakan. |
| **Kemampuan / alat yang dapat digunakan ulang** (Pelajaran 04) | **Skills** memungkinkan Anda menulis instruksi untuk pekerjaan berulang (diimpor dari file `.md` atau dibuat dengan Opal) dan menggunakannya kembali antar percakapan. |

> **Ketersediaan:** Project Opal saat ini tersedia untuk pengguna dalam [program akses awal Frontier](https://adoption.microsoft.com/copilot/frontier-program/) dengan langganan Microsoft 365 Copilot, dan administrator Anda harus menyelesaikan pengaturan. Karena ini adalah fitur experimental Frontier, kemampuan dapat berubah seiring waktu.

## Sumber Daya Tambahan

- [Mulai dengan Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Template integrasi Browser-Use Playwright](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Parameter aktor Browser-Use dan ekstraksi konten](https://docs.browser-use.com/customize/actor/all-parameters)
- [Setup Kursus](../00-course-setup/README.md)

## Pelajaran Sebelumnya

[Menjelajahi Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

## Pelajaran Berikutnya

[Menerapkan Agen yang Dapat Diskalakan](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->