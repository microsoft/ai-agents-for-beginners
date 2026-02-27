# Agen AI untuk Pemula - Panduan Studi & Ringkasan Kursus

Panduan ini menyediakan ringkasan dari kursus "Agen AI untuk Pemula" dan menjelaskan konsep utama, kerangka kerja, dan pola desain untuk membangun Agen AI.

## 1. Pengantar Agen AI

**Apa itu Agen AI?**  
Agen AI adalah sistem yang memperluas kemampuan Large Language Models (LLM) dengan memberikan akses ke **alat**, **pengetahuan**, dan **memori**. Berbeda dengan chatbot LLM standar yang hanya menghasilkan teks berdasarkan data pelatihan, Agen AI dapat:  
- **Merasakan** lingkungannya (melalui sensor atau input).  
- **Memikirkan** cara untuk memecahkan masalah.  
- **Bertindak** untuk mengubah lingkungan (melalui aktuator atau eksekusi alat).

**Komponen Utama Agen:**  
- **Lingkungan**: Ruang tempat agen beroperasi (misalnya, sistem pemesanan).  
- **Sensor**: Mekanisme untuk mengumpulkan informasi (misalnya, membaca API).  
- **Aktuator**: Mekanisme untuk melakukan tindakan (misalnya, mengirim email).  
- **Otak (LLM)**: Mesin penalaran yang merencanakan dan memutuskan tindakan apa yang harus diambil.

## 2. Kerangka Agen

Kursus ini menggunakan **Microsoft Agent Framework (MAF)** dengan **Azure AI Foundry Agent Service V2** untuk membangun agen:

| Komponen | Fokus | Terbaik Untuk |
|-----------|-------|--------------|
| **Microsoft Agent Framework** | SDK Python/C# terpadu untuk agen, alat, dan alur kerja | Membangun agen dengan alat, alur kerja multi-agen, dan pola produksi. |
| **Azure AI Foundry Agent Service** | Runtime cloud terkelola | Penyebaran yang aman, skalabel dengan manajemen status, observabilitas, dan kepercayaan bawaan. |

## 3. Pola Desain Agen

Pola desain membantu menyusun cara agen beroperasi untuk memecahkan masalah secara andal.

### **Pola Penggunaan Alat** (Pelajaran 4)  
Pola ini memungkinkan agen berinteraksi dengan dunia luar.  
- **Konsep**: Agen diberikan "skema" (daftar fungsi yang tersedia dan parameter-parameternya). LLM memutuskan *alat* mana yang dipanggil dan dengan *argumen* apa berdasarkan permintaan pengguna.  
- **Alur**: Permintaan Pengguna -> LLM -> **Pemilihan Alat** -> **Eksekusi Alat** -> LLM (dengan keluaran alat) -> Respons Akhir.  
- **Kasus Penggunaan**: Mengambil data waktu nyata (cuaca, harga saham), melakukan perhitungan, menjalankan kode.

### **Pola Perencanaan** (Pelajaran 7)  
Pola ini memungkinkan agen memecahkan tugas kompleks dan berjenjang.  
- **Konsep**: Agen memecah tujuan tingkat tinggi menjadi rangkaian subtugas yang lebih kecil.  
- **Pendekatan**:  
  - **Dekonstruksi Tugas**: Memecah "Rencanakan perjalanan" menjadi "Pesan penerbangan", "Pesan hotel", "Sewa mobil".  
  - **Perencanaan Iteratif**: Mengevaluasi ulang rencana berdasarkan hasil langkah sebelumnya (misalnya, jika penerbangan penuh, pilih tanggal lain).  
- **Implementasi**: Sering melibatkan agen "Perencana" yang menghasilkan rencana terstruktur (misalnya JSON) yang kemudian dijalankan oleh agen lain.

## 4. Prinsip Desain

Saat mendesain agen, pertimbangkan tiga dimensi:  
- **Ruang**: Agen harus menghubungkan orang dan pengetahuan, mudah diakses tapi tidak mengganggu.  
- **Waktu**: Agen harus belajar dari *Masa Lalu*, memberikan dorongan relevan di *Saat Ini*, dan beradaptasi untuk *Masa Depan*.  
- **Inti**: Terima ketidakpastian tapi bangun kepercayaan melalui transparansi dan kontrol pengguna.

## 5. Ringkasan Pelajaran Kunci

- **Pelajaran 1**: Agen adalah sistem, bukan hanya model. Mereka merasakan, memikirkan, dan bertindak.  
- **Pelajaran 2**: Microsoft Agent Framework menyederhanakan kompleksitas pemanggilan alat dan manajemen status.  
- **Pelajaran 3**: Rancang dengan transparansi dan kontrol pengguna sebagai fokus utama.  
- **Pelajaran 4**: Alat adalah "tangan" agen. Definisi skema sangat penting agar LLM memahami cara menggunakannya.  
- **Pelajaran 7**: Perencanaan adalah "fungsi eksekutif" agen, memungkinkan menyelesaikan alur kerja kompleks.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah penafsiran yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->