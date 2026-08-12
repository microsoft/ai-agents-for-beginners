---
name: jupyter-notebook
description: Gunakan apabila pengguna meminta untuk membuat, membina kerangka, atau
  mengedit notebook Jupyter (`.ipynb`) untuk eksperimen, penerokaan, atau tutorial;
  utamakan templat yang disertakan dan jalankan skrip pembantu `new_notebook.py` untuk
  menjana notebook permulaan yang bersih.
---
# Kemahiran Jupyter Notebook

Cipta notebook Jupyter yang kemas dan boleh diulang untuk dua mod utama:

- Eksperimen dan analisis eksploratori
- Tutorial dan panduan berorientasikan pengajaran

Utamakan templat terbundel dan skrip pembantu untuk struktur yang konsisten dan lebih sedikit kesilapan JSON.

## Bila untuk digunakan
- Cipta notebook `.ipynb` baru dari awal.
- Tukarkan nota kasar atau skrip kepada notebook yang berstruktur.
- Refaktor notebook sedia ada supaya lebih boleh diulang dan mudah diimbas.
- Bina eksperimen atau tutorial yang akan dibaca atau dijalankan semula oleh orang lain.

## Pokok keputusan
- Jika permintaan bersifat eksploratori, analitik, atau berasaskan hipotesis, pilih `experiment`.
- Jika permintaan bersifat pengajaran, langkah-demi-langkah, atau khusus kepada audiens, pilih `tutorial`.
- Jika menyunting notebook sedia ada, anggap ia sebagai refaktor: kekalkan niat dan perbaiki struktur.

## Laluan kemahiran (tetapkan sekali)

```bash
export CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
export JUPYTER_NOTEBOOK_CLI="$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py"
```

User-scoped skills install under `$CODEX_HOME/skills` (default: `~/.codex/skills`).

## Aliran kerja
1. Kunci niat.
Kenal pasti jenis notebook: `experiment` atau `tutorial`.
Tangkap objektif, audiens, dan bagaimana rupa "siap".

2. Rangka daripada templat.
Gunakan skrip pembantu untuk mengelakkan penghasilan JSON notebook mentah secara manual.

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

3. Isi notebook dengan langkah kecil yang boleh dijalankan.
Pastikan setiap sel kod fokus pada satu langkah.
Tambah sel markdown ringkas yang menerangkan tujuan dan hasil yang dijangka.
Elakkan output besar dan bising apabila ringkasan pendek memadai.

4. Terapkan corak yang betul.
Untuk eksperimen, ikut `references/experiment-patterns.md`.
Untuk tutorial, ikut `references/tutorial-patterns.md`.

5. Sunting dengan selamat apabila bekerja dengan notebook sedia ada.
Kekalkan struktur notebook; elakkan menyusun semula sel melainkan ia memperbaiki aliran dari atas ke bawah.
Utamakan suntingan bertarget berbanding penulisan semula sepenuhnya.
Jika anda mesti menyunting JSON mentah, semak `references/notebook-structure.md` dahulu.

6. Sahkan hasilnya.
Jalankan notebook dari atas ke bawah apabila persekitaran membenarkan.
Jika pelaksanaan tidak mungkin, nyatakan dengan jelas dan terangkan cara untuk mengesahkan secara tempatan.
Gunakan semakan akhir dalam `references/quality-checklist.md`.

## Templat dan skrip pembantu
- Templat terletak di `assets/experiment-template.ipynb` dan `assets/tutorial-template.ipynb`.
- Skrip pembantu memuatkan templat, mengemas kini sel tajuk, dan menulis sebuah notebook.

Script path:
- `$JUPYTER_NOTEBOOK_CLI` (installed default: `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`)

## Konvensyen sementara dan output
- Gunakan `tmp/jupyter-notebook/` untuk fail sementara; padam apabila selesai.
- Tulis artifak akhir di bawah `output/jupyter-notebook/` apabila bekerja dalam repo ini.
- Gunakan nama fail yang stabil dan deskriptif (contohnya, `ablation-temperature.ipynb`).

## Pergantungan (pasang hanya bila diperlukan)
Utamakan `uv` untuk pengurusan pergantungan.

Pakej Python pilihan untuk pelaksanaan notebook tempatan:

```bash
uv pip install jupyterlab ipykernel
```

Skrip rangka terbundel hanya menggunakan perpustakaan standard Python dan tidak memerlukan pergantungan tambahan.

## Persekitaran
Tiada pembolehubah persekitaran yang diperlukan.

## Peta rujukan
- `references/experiment-patterns.md`: struktur eksperimen dan heuristik.
- `references/tutorial-patterns.md`: struktur tutorial dan aliran pengajaran.
- `references/notebook-structure.md`: bentuk JSON notebook dan peraturan penyuntingan selamat.
- `references/quality-checklist.md`: senarai semak pengesahan akhir.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Penafian:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha mencapai ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi ralat atau ketidaktepatan. Dokumen asal dalam bahasa asalnya hendaklah dianggap sebagai sumber yang muktamad. Untuk maklumat penting, disyorkan mendapatkan terjemahan profesional oleh penterjemah manusia. Kami tidak bertanggungjawab terhadap sebarang salah faham atau tafsiran yang salah yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->