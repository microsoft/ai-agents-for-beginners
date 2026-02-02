# Ejen AI untuk Pemula - Panduan Kajian & Ringkasan Kursus

Panduan ini menyediakan ringkasan kursus "Ejen AI untuk Pemula" dan menerangkan konsep utama, rangka kerja, dan corak reka bentuk untuk membina Ejen AI.

## 1. Pengenalan kepada Ejen AI

**Apakah Ejen AI?**  
Ejen AI adalah sistem yang memanjangkan keupayaan Large Language Models (LLMs) dengan memberikan mereka akses kepada **alat**, **pengetahuan**, dan **ingatan**. Berbeza dengan chatbot LLM standard yang hanya menjana teks berdasarkan data latihan, Ejen AI dapat:  
- **Menerima deria** persekitarannya (melalui penderia atau input).  
- **Berfikir** tentang cara menyelesaikan masalah.  
- **Bertindak** untuk mengubah persekitaran (melalui penggerak atau pelaksanaan alat).

**Komponen Utama Ejen:**  
- **Persekitaran**: Ruang tempat ejen beroperasi (contoh: sistem tempahan).  
- **Penderia**: Mekanisme untuk mengumpul maklumat (contoh: membaca API).  
- **Penggerak**: Mekanisme untuk melaksanakan tindakan (contoh: menghantar e-mel).  
- **Otak (LLM)**: Enjin pemikiran yang merancang dan membuat keputusan tindakan yang akan diambil.

## 2. Rangka Kerja Ejen

Kursus ini merangkumi tiga rangka kerja utama untuk membina ejen:

| Rangka Kerja | Fokus | Sesuai Untuk |
|--------------|-------|--------------|
| **Semantic Kernel** | SDK sedia untuk pengeluaran untuk .NET/Python | Aplikasi perusahaan, mengintegrasikan AI dengan kod sedia ada. |
| **AutoGen** | Kolaborasi multi-ejen | Senario kompleks yang memerlukan banyak ejen khusus berkomunikasi antara satu sama lain. |
| **Azure AI Agent Service** | Perkhidmatan awan terurus | Pelaksanaan yang selamat dan skala dengan pengurusan keadaan terbina dalam. |

## 3. Corak Reka Bentuk Ejen

Corak reka bentuk membantu menyusun bagaimana ejen beroperasi untuk menyelesaikan masalah secara boleh dipercayai.

### **Corak Penggunaan Alat** (Pelajaran 4)  
Corak ini membolehkan ejen berinteraksi dengan dunia luar.  
- **Konsep**: Ejen diberikan "skim" (senarai fungsi tersedia dan parameternya). LLM memutuskan *alat* mana yang akan dipanggil dan dengan *argumen* apa berdasarkan permintaan pengguna.  
- **Aliran**: Permintaan Pengguna -> LLM -> **Pemilihan Alat** -> **Pelaksanaan Alat** -> LLM (dengan output alat) -> Respons Akhir.  
- **Kes Penggunaan**: Mendapatkan data masa nyata (cuaca, harga saham), melakukan pengiraan, melaksanakan kod.

### **Corak Perancangan** (Pelajaran 7)  
Corak ini membolehkan ejen menyelesaikan tugas kompleks berbilang langkah.  
- **Konsep**: Ejen membahagikan matlamat tinggi ke dalam urutan subtugas yang lebih kecil.  
- **Pendekatan**:  
  - **Pecahan Tugasan**: Memecahkan "Rancang perjalanan" kepada "Tempah penerbangan", "Tempah hotel", "Sewa kereta".  
  - **Perancangan Iteratif**: Menilai semula pelan berdasarkan output langkah sebelumnya (contohnya, jika penerbangan penuh, pilih tarikh lain).  
- **Pelaksanaan**: Selalunya melibatkan ejen "Perancang" yang menjana pelan berstruktur (contoh: JSON) yang kemudiannya dilaksanakan oleh ejen lain.

## 4. Prinsip Reka Bentuk

Apabila mereka bentuk ejen, pertimbangkan tiga dimensi:  
- **Ruang**: Ejen harus menghubungkan manusia dan pengetahuan, boleh diakses tetapi tidak mengganggu.  
- **Masa**: Ejen harus belajar dari *Masa Lalu*, memberikan dorongan relevan pada *Masa Kini*, dan menyesuaikan untuk *Masa Depan*.  
- **Teras**: Terima ketidakpastian tetapi bina kepercayaan melalui ketelusan dan kawalan pengguna.

## 5. Ringkasan Pelajaran Utama

- **Pelajaran 1**: Ejen adalah sistem, bukan sekadar model. Mereka menerima deria, berfikir, dan bertindak.  
- **Pelajaran 2**: Rangka kerja seperti Semantic Kernel dan AutoGen memudahkan kerumitan pemanggilan alat dan pengurusan keadaan.  
- **Pelajaran 3**: Mereka bentuk dengan ketelusan dan kawalan pengguna dalam fikiran.  
- **Pelajaran 4**: Alat adalah "tangan" ejen. Definisi skim penting untuk LLM memahami cara menggunakannya.  
- **Pelajaran 7**: Perancangan adalah "fungsi eksekutif" ejen, membolehkan ia mengendalikan aliran kerja yang kompleks.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->