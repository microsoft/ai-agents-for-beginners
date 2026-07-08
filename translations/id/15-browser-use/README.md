# Membangun Agen Penggunaan Komputer (CUA)

Agen penggunaan komputer dapat berinteraksi dengan situs web sama seperti manusia: dengan membuka browser, memeriksa halaman, dan mengambil tindakan terbaik berikutnya dari apa yang mereka lihat. Dalam pelajaran ini, Anda akan membangun agen otomasi browser yang mencari Airbnb, mengekstrak data listing terstruktur, dan mengidentifikasi tempat menginap termurah di Stockholm.

Pelajaran menggabungkan Browser-Use untuk navigasi yang didorong AI, Playwright dan Chrome DevTools Protocol (CDP) untuk kontrol browser, Azure OpenAI untuk penalaran yang dilengkapi visi, dan Pydantic untuk ekstraksi terstruktur.

## Pendahuluan

Pelajaran ini akan membahas:

- Memahami kapan agen penggunaan komputer lebih cocok dibandingkan otomasi hanya API
- Menggabungkan Browser-Use dengan Playwright dan CDP untuk manajemen siklus hidup browser yang andal
- Menggunakan visi Azure OpenAI dan output Pydantic terstruktur untuk mengekstrak data listing dari halaman web dinamis
- Memutuskan kapan menggunakan alur kerja otomasi browser berbasis agen terlebih dahulu, aktor terlebih dahulu, atau hibrida

## Tujuan Pembelajaran

Setelah menyelesaikan pelajaran ini, Anda akan tahu cara:

- Mengonfigurasi Browser-Use dengan Azure OpenAI dan Playwright
- Membangun alur kerja otomasi browser yang menavigasi situs nyata dan menangani elemen UI dinamis
- Mengekstrak hasil bertipe dari konten halaman yang terlihat dan mengubahnya menjadi logika bisnis lanjutan
- Memilih antara pola agen dan aktor berdasarkan seberapa dapat diprediksinya tugas browser

## Contoh Kode

Pelajaran ini termasuk satu tutorial notebook:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Meluncurkan sesi Chrome melalui CDP, mencari listing Stockholm di Airbnb, mengekstrak harga dengan visi Browser-Use, dan mengembalikan opsi termurah sebagai data terstruktur.

## Prasyarat

- Python 3.12+
- Deployment Azure OpenAI dikonfigurasi di lingkungan Anda
- Chrome atau Chromium terpasang secara lokal
- Dependency Playwright terpasang
- Pemahaman dasar tentang Python async

## Pengaturan

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
# Opsional: default ke versi API terbaru jika dilewatkan
AZURE_OPENAI_API_VERSION=...
```

## Gambaran Arsitektur

Notebook ini mendemonstrasikan alur kerja otomasi browser hibrida:

1. Chrome dimulai dengan CDP diaktifkan agar Playwright dan Browser-Use dapat berbagi sesi browser yang sama.
2. Agen Browser-Use menangani tugas navigasi terbuka seperti membuka Airbnb, menutup pop-up, dan mencari Stockholm.
3. Halaman aktif diperiksa dengan skema Pydantic terstruktur untuk mengekstrak judul listing, harga per malam, peringkat, dan URL.
4. Logika Python membandingkan listing yang diekstrak dan menyoroti hasil termurah.

Pendekatan ini mempertahankan penalaran berbasis visi yang fleksibel yang Browser-Use kuasai sekaligus memberi Anda kontrol browser yang deterministik saat diperlukan.

## Poin Penting dan Praktik Terbaik

### Kapan Menggunakan Agen vs Aktor

| Skenario | Gunakan Agen | Gunakan Aktor |
|----------|--------------|------------|
| Tata letak dinamis | Ya, AI dapat beradaptasi dengan perubahan halaman | Tidak, selector yang rapuh bisa rusak |
| Struktur diketahui | Tidak, agen lebih lambat dibanding kontrol langsung | Ya, cepat dan tepat |
| Menemukan elemen | Ya, bahasa alami bekerja dengan baik | Tidak, dibutuhkan selector tepat |
| Kontrol waktu | Tidak, kurang dapat diprediksi | Ya, kontrol penuh atas waktu tunggu dan pengulangan |
| Alur kerja kompleks | Ya, menangani keadaan UI tak terduga | Tidak, memerlukan percabangan eksplisit |

### Praktik Terbaik Browser-Use

1. Mulailah dengan agen untuk eksplorasi dan navigasi dinamis.
2. Beralihlah ke kontrol halaman langsung bila interaksi menjadi dapat diprediksi.
3. Gunakan model output terstruktur agar data yang diekstrak divalidasi dan bertipe aman.
4. Tambahkan jeda secara strategis setelah aksi yang memicu perubahan UI terlihat.
5. Ambil tangkapan layar saat iterasi agar kegagalan lebih mudah di-debug.
6. Antisipasi perubahan situs web dan desain strategi cadangan untuk pop-up dan pergeseran tata letak.
7. Gabungkan pola agen dan aktor untuk mendapatkan fleksibilitas dan presisi.

### Aplikasi Dunia Nyata

- Pemesanan perjalanan dan pemantauan harga
- Perbandingan harga e-commerce dan pengecekan ketersediaan
- Ekstraksi terstruktur dari situs web dinamis
- Pengujian dan verifikasi UI berbasis visi
- Pemantauan dan pemberitahuan situs web
- Pengisian formulir cerdas di alur bertahap

## Contoh Dunia Nyata: Microsoft Project Opal

Agen yang Anda bangun dalam pelajaran ini adalah versi kecil dan lokal dari **computer use agent (CUA)** — sebuah program yang mengendalikan browser seperti layaknya manusia. Microsoft menghadirkan gagasan ini ke dunia perusahaan dengan **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, sebuah kemampuan dalam Microsoft 365 Copilot.

Dengan Project Opal, Anda mendeskripsikan tugas dan agen bekerja atas nama Anda menggunakan **penggunaan komputer pada Windows 365 Cloud PC yang aman**, beroperasi di seluruh aplikasi, situs, dan data berbasis browser organisasi Anda. Agen bekerja **secara asinkron di latar belakang**, dan Anda bisa memandu pekerjaan atau mengambil kontrol kapan saja. Contoh pekerjaan meliputi:

- Mengelola permintaan keanggotaan grup keamanan
- Mengumpulkan dan memvalidasi bukti audit untuk tinjauan kepatuhan
- Menangani insiden TI (memperbarui status tiket, menetapkan pemilik, menutup duplikat)
- Mengompilasi data Excel ke dalam bahan penutupan keuangan

Opal adalah referensi berguna untuk seperti apa agen penggunaan komputer yang **kelas produksi dan dapat dipercaya** — dan menguatkan konsep dari pelajaran sebelumnya:

| Konsep dalam kursus ini | Bagaimana Project Opal menerapkannya |
|----------------------|--------------------------------|
| **Manusia dalam loop** (Pelajaran 06) | Opal berhenti untuk kredensial login, data sensitif, atau instruksi yang ambigu, dan tidak pernah memasukkan kata sandi atau mengirim formulir tanpa konfirmasi eksplisit. Anda dapat *Mengambil Kontrol* dan *Mengembalikan Kontrol* saat tugas berjalan. |
| **Agen yang dapat dipercaya & aman** (Pelajaran 06 & 18) | Berjalan dalam Windows 365 Cloud PC yang terisolasi, hanya browser secara default (akses komputer lain diblokir, ditegakkan dengan Intune), menggunakan identitas *Anda* sehingga hanya mengakses yang Anda otorisasi, dan mencatat setiap tindakan untuk audit. |
| **Perencanaan & metakognisi** (Pelajaran 07 & 09) | Opal menghasilkan rencana terlebih dahulu, lalu mengawasi penalarannya di tiap langkah dan berhenti jika mendeteksi aktivitas mencurigakan. |
| **Kemampuan / alat yang dapat digunakan ulang** (Pelajaran 04) | **Keterampilan** memungkinkan Anda menulis instruksi untuk tugas berulang (diimpor dari file `.md` atau dibuat dengan Opal) dan menggunakannya kembali dalam percakapan. |

> **Ketersediaan:** Project Opal saat ini tersedia untuk pengguna dalam [program akses awal Frontier](https://adoption.microsoft.com/copilot/frontier-program/) dengan langganan Microsoft 365 Copilot, dan administrator Anda harus menyelesaikan pengaturan. Karena ini fitur eksperimental Frontier, kemampuan dapat berubah seiring waktu.

## Sumber Tambahan

- [Mulai dengan Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Template integrasi Browser-Use Playwright](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Parameter aktor dan ekstraksi konten Browser-Use](https://docs.browser-use.com/customize/actor/all-parameters)
- [Pengaturan Kursus](../00-course-setup/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->