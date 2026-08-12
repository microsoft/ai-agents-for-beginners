# Struktur Notebook

Notebook Jupyter adalah dokumen JSON dengan struktur peringkat tinggi berikut:

- `nbformat` dan `nbformat_minor`
- `metadata`
- `cells` (senarai sel markdown dan kod)

Apabila menyunting fail `.ipynb` secara programatik:

- Kekalkan `nbformat` dan `nbformat_minor` daripada templat.
- Kekalkan `cells` sebagai senarai berurutan; jangan menyusun semula kecuali disengajakan.
- Untuk sel kod, tetapkan `execution_count` kepada `null` apabila tidak diketahui.
- Untuk sel kod, tetapkan `outputs` kepada senarai kosong semasa menyediakan rangka.
- Untuk sel markdown, kekalkan `cell_type="markdown"` dan `metadata={}`.

Utamakan penggunaan rangka dari templat yang disertakan atau `new_notebook.py` (contohnya, `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`) daripada menulis JSON notebook mentah secara manual.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Penafian:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi ralat atau ketidaktepatan. Dokumen asal dalam bahasa asalnya hendaklah dianggap sebagai sumber rujukan yang sah. Untuk maklumat penting, disyorkan mendapatkan terjemahan profesional oleh penterjemah manusia. Kami tidak bertanggungjawab ke atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->