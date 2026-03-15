# Agen AI untuk Pemula - Panduan Studi & Ringkasan Kursus

Panduan ini memberikan ringkasan kursus "Agen AI untuk Pemula" dan menjelaskan konsep kunci, kerangka kerja, dan pola desain untuk membangun Agen AI.

## 1. Pengenalan Agen AI

**Apa itu Agen AI?**  
Agen AI adalah sistem yang memperluas kemampuan Large Language Models (LLMs) dengan memberikan mereka akses ke **alat**, **pengetahuan**, dan **memori**. Berbeda dengan chatbot LLM standar yang hanya menghasilkan teks berdasarkan data pelatihan, Agen AI dapat:  
- **Menyadari** lingkungannya (melalui sensor atau input).  
- **Menyusun alasan** tentang cara memecahkan masalah.  
- **Bertindak** untuk mengubah lingkungan (melalui aktuator atau eksekusi alat).

**Komponen Utama Agen:**  
- **Lingkungan**: Ruang tempat agen beroperasi (misalnya sistem pemesanan).  
- **Sensor**: Mekanisme untuk mengumpulkan informasi (misalnya membaca API).  
- **Aktuator**: Mekanisme untuk melakukan tindakan (misalnya mengirim email).  
- **Otak (LLM)**: Mesin penalaran yang merencanakan dan memutuskan tindakan apa yang akan diambil.

## 2. Kerangka Kerja Agen

Kursus ini menggunakan **Microsoft Agent Framework (MAF)** dengan **Azure AI Foundry Agent Service V2** untuk membangun agen:

| Komponen | Fokus | Terbaik Untuk |
|-----------|-------|--------------|
| **Microsoft Agent Framework** | SDK Python/C# terpadu untuk agen, alat, dan alur kerja | Membangun agen dengan alat, alur kerja multi-agen, dan pola produksi. |
| **Azure AI Foundry Agent Service** | Runtime cloud terkelola | Penyebaran yang aman dan skala besar dengan manajemen status, observabilitas, dan kepercayaan bawaan. |

## 3. Pola Desain Agen

Pola desain membantu menyusun cara agen bekerja untuk memecahkan masalah dengan andal.

### **Pola Penggunaan Alat** (Pelajaran 4)  
Pola ini memungkinkan agen berinteraksi dengan dunia luar.  
- **Konsep**: Agen diberikan "skema" (daftar fungsi yang tersedia dan parameternya). LLM memutuskan *alat* mana yang akan dipanggil dan dengan *argumen apa* berdasarkan permintaan pengguna.  
- **Alur**: Permintaan Pengguna -> LLM -> **Pemilihan Alat** -> **Eksekusi Alat** -> LLM (dengan output alat) -> Respon Akhir.  
- **Kasus Penggunaan**: Mengambil data waktu nyata (cuaca, harga saham), melakukan perhitungan, menjalankan kode.

### **Pola Perencanaan** (Pelajaran 7)  
Pola ini memungkinkan agen menyelesaikan tugas kompleks yang terdiri dari banyak langkah.  
- **Konsep**: Agen memecah tujuan tingkat tinggi menjadi rangkaian subtugas yang lebih kecil.  
- **Pendekatan**:  
  - **Decomposisi Tugas**: Memecah "Rencanakan perjalanan" menjadi "Pesan penerbangan", "Pesan hotel", "Sewa mobil".  
  - **Perencanaan Iteratif**: Menilai kembali rencana berdasarkan output langkah sebelumnya (misalnya, jika penerbangan penuh, pilih tanggal lain).  
- **Implementasi**: Sering melibatkan agen "Perencana" yang menghasilkan rencana terstruktur (misalnya JSON) yang kemudian dijalankan oleh agen lain.

## 4. Prinsip Desain

Saat mendesain agen, pertimbangkan tiga dimensi:  
- **Ruang**: Agen harus menghubungkan orang dan pengetahuan, mudah diakses tapi tidak mengganggu.  
- **Waktu**: Agen harus belajar dari *Masa Lalu*, memberikan dorongan relevan di *Sekarang*, dan beradaptasi untuk *Masa Depan*.  
- **Inti**: Terima ketidakpastian namun bangun kepercayaan melalui transparansi dan kontrol pengguna.

## 5. Ringkasan Pelajaran Utama

- **Pelajaran 1**: Agen adalah sistem, bukan hanya model. Mereka menyadari, beralasan, dan bertindak.  
- **Pelajaran 2**: Microsoft Agent Framework menyederhanakan kompleksitas pemanggilan alat dan manajemen status.  
- **Pelajaran 3**: Rancang dengan transparansi dan kontrol pengguna sebagai prioritas.  
- **Pelajaran 4**: Alat adalah "tangan" agen. Definisi skema sangat penting agar LLM mengerti cara menggunakannya.  
- **Pelajaran 7**: Perencanaan adalah "fungsi eksekutif" agen, memungkinkan menyelesaikan alur kerja kompleks.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diingat bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidaktepatan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas segala kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->