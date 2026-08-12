# Struktur Notebook

Jupyter notebooks adalah dokumen JSON dengan bentuk tingkat tinggi berikut:

- `nbformat` and `nbformat_minor`
- `metadata`
- `cells` (sebuah daftar sel markdown dan sel kode)

When editing `.ipynb` files programmatically:

- Preserve `nbformat` and `nbformat_minor` from the template.
- Keep `cells` as an ordered list; do not reorder unless intentional.
- For code cells, set `execution_count` to `null` when unknown.
- For code cells, set `outputs` to an empty list when scaffolding.
- For markdown cells, keep `cell_type="markdown"` and `metadata={}`.

Prefer scaffolding from the bundled templates or `new_notebook.py` (for example, `$CODEX_HOME/skills/jupyter-notebook/scripts/new_notebook.py`) instead of hand-authoring raw notebook JSON.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Penafian:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI Co-op Translator (https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diingat bahwa terjemahan otomatis dapat mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang bersifat krusial, disarankan menggunakan jasa penerjemah profesional. Kami tidak bertanggung jawab atas setiap kesalahpahaman atau penafsiran yang keliru yang timbul akibat penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->