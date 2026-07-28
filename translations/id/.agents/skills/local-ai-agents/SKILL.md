---
name: local-ai-agents
license: MIT
---
# Membuat Agen AI Lokal dengan Foundry Local dan Qwen

> Keterampilan pendamping untuk [Lesson 17 – Membuat Agen AI Lokal](../../../17-creating-local-ai-agents/README.md).
> Gunakan ini untuk membantu pelajar membangun agen yang melakukan penalaran, memanggil alat, dan mencari
> dokumentasi sepenuhnya di mesin mereka sendiri — tanpa inferensi cloud. Dasarkan setiap
> rekomendasi pada konten pelajaran dan notebook yang dapat dijalankan.

## Pemicu

Aktifkan keterampilan ini ketika pelajar ingin:
- Menjalankan agen **sepenuhnya di perangkat** untuk alasan privasi, biaya, atau offline.
- Menyajikan model secara lokal dengan **Foundry Local** dan terhubung melalui endpoint kompatibel OpenAI.
- Menggunakan model **pemanggilan fungsi Qwen** untuk menjalankan panggilan alat lokal yang andal.
- Menambahkan **RAG lokal** (Chroma) atau **server MCP lokal**.
- Merancang strategi routing **hibrida** lokal/cloud.

## Model mental inti

Sebuah SLM menukar cakupan untuk privasi, biaya, dan operasi offline. Strategi
unggul: **biarkan SLM mengoordinasikan dan biarkan alat menangani pekerjaan berat.** Model
tidak perlu *mengetahui* basis kode — ia perlu tahu kapan memanggil
`read_file` dan `search_docs`. Ini memanfaatkan kekuatan SLM (keputusan terbatas
seperti pemilihan alat) dan menghindari kelemahannya (pengetahuan luas, penalaran multi-langkah panjang).


## Mengapa bagian-bagian ini dipilih

- **Foundry Local** menyediakan **endpoint HTTP kompatibel OpenAI**, sehingga kode agen cloud dapat dipindahkan hanya dengan mengubah `base_url` (dan menggunakan kunci API placeholder lokal). Ini juga secara otomatis memilih build terbaik (CPU/GPU/NPU) untuk mesin tersebut.
- Model **Qwen** dilatih untuk pemanggilan fungsi dan secara konsisten menghasilkan panggilan alat yang terstruktur dengan baik — inilah yang mengubah model *chat* lokal menjadi *agen* lokal.
- **Chroma** berjalan dalam proses dan menyimpan vektor di disk, sehingga seluruh pipeline RAG (embed → store → retrieve → reason) tetap lokal.
- **MCP** adalah transportasi, bukan layanan cloud: server MCP dapat dijalankan secara lokal melalui `stdio`.

## Persiapan penting

```bash
foundry model run qwen2.5-7b-instruct
foundry service status
```

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager("qwen2.5-7b-instruct")
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)  # placeholder lokal
```

~8 GB RAM adalah minimum yang realistis; GPU/NPU membantu tetapi tidak wajib.

## Pola kunci untuk direproduksi

Arahkan pelajar ke notebook
[`17-local-agent-foundry-local.ipynb`](../../../17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb):

- **Alat yang terisolasi**: setiap alat file menyelesaikan jalur dan menolak segala sesuatu di luar satu root proyek — bahkan secara lokal, sebuah alat berjalan dengan izin pengguna.
- **Loop pemanggilan alat**: daftarkan alat dengan skema alat OpenAI, jalankan alat yang diminta secara lokal, masukkan hasil kembali, ulangi sampai jawaban akhir.
- **RAG lokal**: masukkan dokumen ke koleksi Chroma; `search_docs` mengembalikan chunk teratas-k.
- **MCP lokal**: terhubung ke server lokal melalui `stdio`; batasi ke direktori proyek dan validasi outputnya.

## Routing hibrida (lokal sebagai salah satu model)

| Situasi | Tempat berjalan |
|-----------|---------------|
| Data sensitif / offline | SLM Lokal |
| Tugas sederhana, terbatas | SLM Lokal (murah, cepat) |
| Penalaran multi-langkah sulit pada data non-sensitif | Model Cloud |
| Gangguan cloud | SLM Lokal (penurunan kualitas yang mulus) |

Ini mencerminkan ide routing model dari Lesson 16, dengan workstation sebagai salah satu
rute. Pilih desain yang kembali ke lokal sehingga agen menurun
kualitasnya daripada gagal total.

## Pembatasan untuk asisten

- Batasi setiap operasi file/alat ke direktori proyek yang terisolasi.
- Jangan kirim kode atau data ke cloud ketika tujuan pelajar adalah privasi/offline — pertahankan seluruh pipeline lokal.
- Tetapkan harapan realistis untuk kualitas SLM; bergantung pada alat dan RAG daripada pengetahuan yang dihafal model.
- Perhatikan bahwa Lesson 17 **tidak** memiliki endpoint Foundry Responses, jadi tindakan uji coba cloud tidak berlaku — validasi dengan menjalankan notebook secara lokal.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->