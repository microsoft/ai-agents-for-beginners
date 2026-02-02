# Agen AI untuk Pemula - Panduan Studi & Ringkasan Kursus

Panduan ini memberikan ringkasan dari kursus "Agen AI untuk Pemula" dan menjelaskan konsep kunci, kerangka kerja, serta pola desain untuk membangun Agen AI.

## 1. Pengenalan Agen AI

**Apa itu Agen AI?**  
Agen AI adalah sistem yang memperluas kemampuan Large Language Models (LLMs) dengan memberikan mereka akses ke **alat**, **pengetahuan**, dan **memori**. Berbeda dengan chatbot LLM standar yang hanya membuat teks berdasarkan data pelatihan, Agen AI dapat:  
- **Mengamati** lingkungannya (melalui sensor atau input).  
- **Menalar** tentang bagaimana memecahkan masalah.  
- **Bertindak** untuk mengubah lingkungan (melalui aktuator atau eksekusi alat).

**Komponen Utama Agen:**  
- **Lingkungan**: Ruang tempat agen beroperasi (misalnya, sistem pemesanan).  
- **Sensor**: Mekanisme untuk mengumpulkan informasi (misalnya, membaca API).  
- **Aktuator**: Mekanisme untuk melakukan tindakan (misalnya, mengirim email).  
- **Otak (LLM)**: Mesin penalaran yang merencanakan dan memutuskan tindakan yang akan diambil.

## 2. Kerangka Kerja Agentic

Kursus mencakup tiga kerangka kerja utama untuk membangun agen:

| Kerangka Kerja | Fokus | Terbaik Untuk |
|-----------|-------|----------|
| **Semantic Kernel** | SDK siap produksi untuk .NET/Python | Aplikasi perusahaan, mengintegrasikan AI dengan kode yang sudah ada. |
| **AutoGen** | Kolaborasi multi-agen | Skenario kompleks yang memerlukan beberapa agen khusus saling berkomunikasi. |
| **Azure AI Agent Service** | Layanan cloud terkelola | Penyebaran aman dan skalabel dengan manajemen status bawaan. |

## 3. Pola Desain Agentic

Pola desain membantu menyusun cara agen beroperasi untuk memecahkan masalah secara andal.

### **Pola Penggunaan Alat** (Pelajaran 4)  
Pola ini memungkinkan agen berinteraksi dengan dunia luar.  
- **Konsep**: Agen diberikan "skema" (daftar fungsi yang tersedia dan parameternya). LLM memutuskan *alat* mana yang akan dipanggil dan *argument* apa yang diberikan berdasarkan permintaan pengguna.  
- **Alur**: Permintaan Pengguna -> LLM -> **Pemilihan Alat** -> **Eksekusi Alat** -> LLM (dengan output alat) -> Respon Akhir.  
- **Kasus Penggunaan**: Mengambil data waktu nyata (cuaca, harga saham), melakukan perhitungan, mengeksekusi kode.

### **Pola Perencanaan** (Pelajaran 7)  
Pola ini memungkinkan agen menyelesaikan tugas kompleks dan bertahap.  
- **Konsep**: Agen memecah tujuan tingkat tinggi menjadi rangkaian subtugas yang lebih kecil.  
- **Pendekatan**:  
  - **Dekompisi Tugas**: Membagi "Rencanakan perjalanan" menjadi "Pesan penerbangan", "Pesan hotel", "Sewa mobil".  
  - **Perencanaan Iteratif**: Mengevaluasi ulang rencana berdasarkan hasil langkah sebelumnya (misalnya, jika penerbangan penuh, pilih tanggal lain).  
- **Implementasi**: Sering melibatkan agen "Perencana" yang menghasilkan rencana terstruktur (misalnya JSON) yang kemudian dieksekusi oleh agen lain.

## 4. Prinsip Desain

Saat merancang agen, pertimbangkan tiga dimensi:  
- **Ruang**: Agen harus menghubungkan orang dan pengetahuan, dapat diakses tapi tidak mengganggu.  
- **Waktu**: Agen harus belajar dari *Masa Lalu*, memberikan dorongan relevan di *Saat Ini*, dan beradaptasi untuk *Masa Depan*.  
- **Inti**: Terima ketidakpastian namun bangun kepercayaan melalui transparansi dan kontrol pengguna.

## 5. Ringkasan Pelajaran Kunci

- **Pelajaran 1**: Agen adalah sistem, bukan hanya model. Mereka mengamati, menalar, dan bertindak.  
- **Pelajaran 2**: Kerangka seperti Semantic Kernel dan AutoGen menyederhanakan kompleksitas pemanggilan alat dan manajemen status.  
- **Pelajaran 3**: Rancang dengan transparansi dan kontrol pengguna dalam pikiran.  
- **Pelajaran 4**: Alat adalah "tangan" agen. Definisi skema sangat penting agar LLM mengerti cara menggunakannya.  
- **Pelajaran 7**: Perencanaan adalah "fungsi eksekutif" agen, memungkinkan agen menangani alur kerja kompleks.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk keakuratan, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi yang penting, disarankan menggunakan jasa terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->