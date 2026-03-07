# Ejen AI untuk Pemula - Panduan Kajian & Ringkasan Kursus

This guide provides a summary of the "AI Agents for Beginners" course and explains key concepts, frameworks, and design patterns for building AI Agents.

## 1. Pengenalan kepada Ejen AI

**Apakah Ejen AI?**
Ejen AI adalah sistem yang memperluaskan keupayaan Large Language Models (LLMs) dengan memberi mereka akses kepada **alat**, **pengetahuan**, dan **memori**. Berbeza dengan chatbot LLM standard yang hanya menghasilkan teks berdasarkan data latihan, Ejen AI boleh:
- **Mengesan** persekitarannya (melalui sensor atau input).
- **Menalar** tentang bagaimana untuk menyelesaikan masalah.
- **Bertindak** untuk mengubah persekitaran (melalui aktuator atau pelaksanaan alat).

**Komponen Utama Ejen:**
- **Persekitaran**: Ruang di mana ejen beroperasi (contohnya, sistem tempahan).
- **Sensor**: Mekanisme untuk mengumpul maklumat (contohnya, membaca API).
- **Aktuator**: Mekanisme untuk melakukan tindakan (contohnya, menghantar e-mel).
- **Otak (LLM)**: Enjin penaakulan yang merancang dan memutuskan tindakan yang perlu diambil.

## 2. Rangka Kerja Ejen

Kursus ini menggunakan **Microsoft Agent Framework (MAF)** dengan **Azure AI Foundry Agent Service V2** untuk membina ejen:

| Component | Focus | Best For |
|-----------|-------|----------|
| **Microsoft Agent Framework** | Unified Python/C# SDK for agents, tools, and workflows | Building agents with tools, multi-agent workflows, and production patterns. |
| **Azure AI Foundry Agent Service** | Managed cloud runtime | Secure, scalable deployment with built-in state management, observability, and trust. |

## 3. Corak Reka Bentuk Ejen

Corak reka bentuk membantu menyusun bagaimana ejen beroperasi untuk menyelesaikan masalah secara boleh dipercayai.

### **Corak Penggunaan Alat** (Pelajaran 4)
Corak ini membolehkan ejen berinteraksi dengan dunia luar.
- **Konsep**: Ejen diberikan "skema" (senarai fungsi yang tersedia dan parameter mereka). LLM memutuskan *alat mana* untuk dipanggil dan dengan *argumen apa* berdasarkan permintaan pengguna.
- **Aliran**: Permintaan Pengguna -> LLM -> **Pemilihan Alat** -> **Pelaksanaan Alat** -> LLM (dengan keluaran alat) -> Respons Akhir.
- **Kes Penggunaan**: Mengambil data masa nyata (cuaca, harga saham), melakukan pengiraan, melaksanakan kod.

### **Corak Perancangan** (Pelajaran 7)
Corak ini membolehkan ejen menyelesaikan tugas kompleks berbilang langkah.
- **Konsep**: Ejen memecahkan matlamat tingkat tinggi kepada urutan subtugas yang lebih kecil.
- **Pendekatan**:
  - **Penguraian Tugas**: Membahagikan "Rancang perjalanan" kepada "Tempah penerbangan", "Tempah hotel", "Sewa kereta".
  - **Perancangan Iteratif**: Menilai semula rancangan berdasarkan keluaran langkah sebelumnya (contohnya, jika penerbangan penuh, pilih tarikh yang berbeza).
- **Pelaksanaan**: Selalunya melibatkan ejen "Perancang" yang menjana rancangan berstruktur (contohnya, JSON) yang kemudian dilaksanakan oleh ejen lain.

## 4. Prinsip Reka Bentuk

Apabila mereka bentuk ejen, pertimbangkan tiga dimensi:
- **Ruang**: Ejen harus menghubungkan orang dan pengetahuan, boleh diakses tetapi tidak mengganggu.
- **Masa**: Ejen harus belajar dari *Masa Lalu*, memberi dorongan yang relevan pada *Masa Kini*, dan menyesuaikan untuk *Masa Depan*.
- **Teras**: Terima ketidakpastian tetapi bina kepercayaan melalui ketelusan dan kawalan pengguna.

## 5. Ringkasan Pelajaran Utama

- **Pelajaran 1**: Ejen adalah sistem, bukan sekadar model. Mereka mengesan, menalar, dan bertindak.
- **Pelajaran 2**: Microsoft Agent Framework mengabstrakkan kerumitan pemanggilan alat dan pengurusan keadaan.
- **Pelajaran 3**: Reka bentuk dengan ketelusan dan kawalan pengguna dalam fikiran.
- **Pelajaran 4**: Alat adalah "tangan" ejen. Definisi skema amat penting supaya LLM memahami cara menggunakannya.
- **Pelajaran 7**: Perancangan adalah "fungsi eksekutif" ejen, membolehkannya menangani aliran kerja kompleks.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Penafian:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha mencapai ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi ralat atau ketidaktepatan. Dokumen asal dalam bahasa asalnya hendaklah dianggap sebagai sumber rujukan yang sahih. Untuk maklumat kritikal, disarankan mendapatkan terjemahan profesional oleh penterjemah manusia. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsiran yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->