---
name: jupyter-notebook
description: Gunakan saat pengguna meminta untuk membuat, membangun kerangka, atau
  mengedit notebook Jupyter (`.ipynb`) untuk eksperimen, eksplorasi, atau tutorial;
  utamakan templat bawaan dan jalankan skrip pembantu `new_notebook.py` untuk menghasilkan
  notebook awal yang bersih.
---
# Keterampilan Jupyter Notebook

Buat notebook Jupyter yang bersih dan dapat direproduksi untuk dua mode utama:

- Eksperimen dan analisis eksploratori
- Tutorial dan panduan berorientasi pengajaran

Utamakan template bawaan dan skrip pembantu untuk struktur yang konsisten dan lebih sedikit kesalahan JSON.

## Kapan digunakan
- Buat notebook `.ipynb` baru dari awal.
- Konversi catatan kasar atau skrip menjadi notebook yang terstruktur.
- Refaktor notebook yang ada agar lebih dapat direproduksi dan mudah dibaca.
- Bangun eksperimen atau tutorial yang akan dibaca atau dijalankan ulang oleh orang lain.

## Pohon keputusan
- Jika permintaan bersifat eksploratori, analitis, atau berorientasi hipotesis, pilih `experiment`.
- Jika permintaan bersifat instruksional, langkah-demi-langkah, atau spesifik audiens, pilih `tutorial`.
- Jika mengedit notebook yang sudah ada, perlakukan sebagai refaktor: pertahankan maksud dan perbaiki struktur.

## Jalur keterampilan (atur sekali)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

User-scoped skills install under `$CODEX_HOME/skills` (default: `~/.codex/skills`).

## Alur kerja
1. Kunci tujuan.
Identifikasi jenis notebook: `experiment` atau `tutorial`.
Catat tujuan, audiens, dan seperti apa "selesai".

2. Buat kerangka dari template.
Gunakan skrip pembantu untuk menghindari menulis JSON notebook mentah secara manual.

```bash
uv run --python 3.12 python "$JUPYTER_NOTEBOOK_CLI" \
  --kind experiment \
  --title "Compare prompt variants" \
  --out output/jupyter-notebook/compare-prompt-variants.ipynb
```

```bash
uv run --python 3.12 python "$JUPYTER_NOTEBOOK_CLI" \
  --kind tutorial \
  --title "Intro to embeddings" \
  --out output/jupyter-notebook/intro-to-embeddings.ipynb
```

3. Isi notebook dengan langkah-langkah kecil yang dapat dijalankan.
Pastikan setiap sel kode fokus pada satu langkah.
Tambahkan sel markdown singkat yang menjelaskan tujuan dan hasil yang diharapkan.
Hindari keluaran besar yang berisik ketika ringkasan singkat sudah memadai.

4. Terapkan pola yang tepat.
Untuk eksperimen, ikuti `references/experiment-patterns.md`.
Untuk tutorial, ikuti `references/tutorial-patterns.md`.

5. Edit dengan aman saat bekerja pada notebook yang ada.
Pertahankan struktur notebook; hindari mengubah urutan sel kecuali itu memperbaiki alur dari atas ke bawah.
Utamakan suntingan terarah daripada penulisan ulang penuh.
Jika harus mengedit JSON mentah, tinjau `references/notebook-structure.md` terlebih dahulu.

6. Validasi hasil.
Jalankan notebook dari atas ke bawah bila lingkungan memungkinkan.
Jika eksekusi tidak memungkinkan, nyatakan secara eksplisit dan jelaskan cara memvalidasinya secara lokal.
Gunakan daftar periksa akhir di `references/quality-checklist.md`.

## Template dan skrip pembantu
- Template berada di `assets/experiment-template.ipynb` dan `assets/tutorial-template.ipynb`.
- Skrip pembantu memuat template, memperbarui sel judul, dan menulis notebook.

Script path:
- `$JUPYTER_NOTEBOOK_CLI` (default terinstal: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## Konvensi sementara dan keluaran
- Gunakan `tmp/jupyter-notebook/` untuk file sementara; hapus saat selesai.
- Tulis artefak akhir di `output/jupyter-notebook/` saat bekerja di repo ini.
- Gunakan nama file yang stabil dan deskriptif (misalnya, `ablation-temperature.ipynb`).

## Dependensi (pasang hanya bila diperlukan)
Utamakan `uv` untuk manajemen dependensi.

Optional Python packages for local notebook execution:

```bash
uv pip install jupyterlab ipykernel
```

The bundled scaffold script uses only the Python standard library and does not require extra dependencies.

## Lingkungan
Tidak ada variabel lingkungan yang diperlukan.

## Peta referensi
- `references/experiment-patterns.md`: struktur eksperimen dan heuristik.
- `references/tutorial-patterns.md`: struktur tutorial dan alur pengajaran.
- `references/notebook-structure.md`: bentuk JSON notebook dan aturan pengeditan aman.
- `references/quality-checklist.md`: daftar periksa validasi akhir.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya memastikan keakuratan, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat kritis, disarankan menggunakan jasa penerjemah profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->