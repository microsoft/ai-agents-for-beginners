---
name: local-ai-agents
license: MIT
---
# Membina Ejen AI Tempatan dengan Foundry Local dan Qwen

> Kemahiran pendamping untuk [Pelajaran 17 – Membina Ejen AI Tempatan](../../../17-creating-local-ai-agents/README.md).
> Gunakannya untuk membantu pelajar membina ejen yang membuat penalaran, memanggil alat, dan mencari
> dokumentasi sepenuhnya di mesin mereka sendiri — tiada inferens awan. Berdasarkan setiap
> cadangan kepada kandungan pelajaran dan buku nota yang boleh dijalankan.

## Pencetus

Aktifkan kemahiran ini apabila pelajar mahu:
- Menjalankan ejen **sepenuhnya di peranti** untuk privasi, kos, atau sebab luar talian.
- Menyediakan model secara tempatan dengan **Foundry Local** dan sambungkan melalui titik akhir sepadan OpenAI.
- Menggunakan model **Qwen pemanggil fungsi** untuk menggerakkan panggilan alat tempatan yang boleh dipercayai.
- Menambah **RAG tempatan** (Chroma) atau **pelayan MCP tempatan**.
- Mereka bentuk strategi penghalaan **hibrid** tempatan/awan.

## Model mental teras

SLM menukar liputan luas untuk privasi, kos, dan operasi luar talian. Strategi kemenangan:
**biarkan SLM mengatur dan biarkan alat melakukan kerja berat.** Model
tidak perlu *tahu* kod sumber — ia perlu tahu bila untuk memanggil
`read_file` dan `search_docs`. Ini memanfaatkan kekuatan SLM (keputusan terhad
seperti pemilihan alat) dan menjauhkannya dari kelemahan (pengetahuan luas, penalaran berbilang lonjak panjang).


## Kenapa bahagian khusus ini

- **Foundry Local** menyediakan **titik akhir HTTP sepadan OpenAI**, jadi kod ejen awan boleh dipindahkan hanya dengan menukar `base_url` (dan menggunakan kunci API tempatan palsu). Ia juga memilih binaan terbaik (CPU/GPU/NPU) untuk mesin itu secara automatik.
- Model **Qwen** dilatih untuk pemanggilan fungsi dan menghasilkan panggilan alat yang teratur secara konsisten — inilah yang menjadikan model *chat* tempatan menjadi *agen* tempatan.
- **Chroma** berjalan dalam proses dan menyimpan vektor di cakera, jadi keseluruhan saluran RAG (embed → simpan → ambil → beri alasan) kekal tempatan.
- **MCP** adalah pengangkut, bukan perkhidmatan awan: pelayan MCP boleh dijalankan secara tempatan melalui `stdio`.

## Keperluan pemasangan

```bash
foundry model run qwen2.5-7b-instruct
foundry service status
```

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager("qwen2.5-7b-instruct")
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)  # pemegang tempat setempat
```

~8 GB RAM adalah minimum yang realistik; GPU/NPU membantu tetapi tidak diwajibkan.

## Corak utama untuk ditiru

Tunjukkan pelajar kepada buku nota
[`17-local-agent-foundry-local.ipynb`](../../../17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb):

- **Alat dalam sandbox**: setiap alat fail menyelesaikan laluan dan menolak apa-apa di luar akar projek tunggal — walaupun secara tempatan, alat dijalankan dengan kebenaran pengguna.
- **Gelung pemanggilan alat**: daftarkan alat dengan skema alat OpenAI, jalankan alat yang diminta secara tempatan, beri maklum balas hasil, ulang sehingga jawapan akhir.
- **RAG tempatan**: kemas kini dokumen ke dalam koleksi Chroma; `search_docs` mengembalikan pecahan utama-k.
- **MCP tempatan**: sambungkan ke pelayan tempatan melalui `stdio`; tetapkan skop ke direktori projek dan sahkan outputnya.

## Penghalaan hibrid (tempatan sebagai salah satu model)

| Situasi | Di mana ia dijalankan |
|-----------|---------------|
| Data sensitif / luar talian | SLM Tempatan |
| Tugasan mudah dan terhad | SLM Tempatan (murah, cepat) |
| Penalaran banyak lonjak yang sukar pada data tidak sensitif | Model awan |
| Gangguan awan | SLM Tempatan (penurunan kualiti secara terkawal) |

Ini mencerminkan idea penghalaan model dari Pelajaran 16, dengan stesen kerja sebagai salah
satu laluan. Pilih reka bentuk yang kembali ke tempatan supaya ejen menurun kualiti
daripada gagal sepenuhnya.

## Panduan untuk pembantu

- Kekalkan setiap operasi fail/alat yang dihadkan kepada direktori projek berpasir.
- Jangan hantar kod atau data ke awan apabila tujuan dinyatakan pelajar adalah privasi/luar talian — pastikan seluruh saluran kekal tempatan.
- Tetapkan jangkaan realistik untuk kualiti SLM; bergantung pada alat dan RAG daripada pengetahuan model yang diingati.
- Perhatikan bahawa Pelajaran 17 **tiada** titik akhir Respons Foundry, jadi tindakan ujian asap awan tidak terpakai — sahkan dengan menjalankan buku nota secara tempatan.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->