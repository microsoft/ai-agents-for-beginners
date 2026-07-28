# Tes Smoke Agen

Folder ini menyimpan **katalog tes smoke** untuk agen yang Anda buat dalam kursus.
Tes smoke adalah pemeriksaan murah dan cepat bahwa **agen yang dihosting Microsoft Foundry yang 
sudah diterapkan** dapat dijangkau, merespons, dan mengikuti harapan prompt dasarnya.
Ini adalah gerbang pertama — bukan pengganti untuk pipeline evaluasi penuh 
yang Anda pelajari di [Lesson 10](../10-ai-agents-production/README.md) dan
[Lesson 16](../16-deploying-scalable-agents/README.md).

Katalog digunakan oleh [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
GitHub Action melalui workflow [`.github/workflows/smoke-test.yml`](../../../.github/workflows/smoke-test.yml).


## Cara menjalankan

1. **Terapkan agen pelajaran** ke Microsoft Foundry sebagai agen yang dihosting (lihat
   Lesson 16 untuk alur kerja penerapan). Catat **nama agen** dan
   **titik akhir proyek Foundry** Anda.
2. Tambahkan rahasia repositori ini (Settings → Secrets and variables → Actions):
   `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`. Identitas federasi
   membutuhkan peran **Azure AI User** di **lingkup proyek Foundry**.
3. Dari tab **Actions**, jalankan **Smoke-test hosted agents** dan pilih
   `tests_file` untuk pelajaran tersebut, lalu masukkan `agent_name` dan
   `project_endpoint` yang sesuai.

## Katalog → pelajaran → nama agen

| Katalog | Pelajaran | Terapkan agen sebagai |
|--------|-----------|----------------------|
| [`lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) | [01 – Intro to AI Agents](../01-intro-to-ai-agents/README.md) | `TravelAgent` |
| [`lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) | [04 – Tool Use](../04-tool-use/README.md) | `TravelToolAgent` |
| [`lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) | [05 – Agentic RAG](../05-agentic-rag/README.md) | `TravelRAGAgent` |
| [`lesson-16-smoke-tests.json`](../../../tests/lesson-16-smoke-tests.json) | [16 – Deploying Scalable Agents](../16-deploying-scalable-agents/README.md) | `ContosoSupportAgent` |

## Pelajaran mana yang memiliki tes smoke?

Tes smoke berlaku untuk pelajaran di mana Anda **menerapkan agen** yang balasan teksnya dapat
dipastikan terhadap konten yang diketahui. Pelajaran yang bersifat konseptual, berjalan hanya secara lokal,
atau menghasilkan output kreatif yang tidak deterministik sengaja dikecualikan:

- **Pelajaran 17 (Membuat Agen AI Lokal)** berjalan sepenuhnya di workstation Anda dengan
  Foundry Local dan **tidak** mengekspos titik akhir Foundry Responses, jadi
  aksi ini tidak berlaku. Validasi dengan menjalankan notebook secara lokal.
- Pelajaran pola desain dan teori (02, 03, 06, 07, 09, 12) tidak mengirimkan agen yang dapat diterapkan
  untuk tes smoke.

## Skema katalog (referensi cepat)

Setiap katalog adalah dokumen JSON dengan array `tests` tingkat atas. Setiap entri mengirim POST
satu prompt dan memeriksa balasannya:

| Kolom | Makna |
|-------|---------|
| `id` | Identifier langkah unik yang dicetak di log. |
| `description` | Tujuan yang dapat dibaca manusia. |
| `prompt` | Pesan yang dikirimkan ke agen. |
| `assertions.status` | Status HTTP yang diharapkan (default 200). |
| `assertions.contains_any` | Lulus jika balasan mengandung salah satu substring ini. |
| `assertions.contains_all` | Lulus jika balasan mengandung semua substring. |
| `assertions.contains_none` | Lulus jika balasan tidak mengandung satupun substring ini. |
| `save_response_id_as` | Simpan id balasan untuk langkah multi-gilir berikutnya. |
| `use_previous_response_id` | Kirim giliran ini terikat dengan id balasan yang disimpan. |

Pemeriksaan adalah cek substring tanpa memperhatikan huruf besar kecil. Lihat
[dokumentasi action](https://github.com/marketplace/actions/ai-smoke-test) untuk
skema lengkap, termasuk sumber daya percakapan yang dikelola Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->