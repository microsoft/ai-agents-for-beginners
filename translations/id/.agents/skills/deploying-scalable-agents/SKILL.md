---
name: deploying-scalable-agents
license: MIT
---
# Mendeploy Agen Skala Besar dengan Microsoft Foundry

> Keterampilan pendamping untuk [Lesson 16 – Mendeploy Agen Skala Besar](../../../16-deploying-scalable-agents/README.md).
> Gunakan ini untuk membantu pembelajar memindahkan agen dari prototipe ke deploy produksi yang skalabel dan dapat diamati.
> Dasarkan setiap rekomendasi pada konten pelajaran dan
> notebook yang dapat dijalankan; jangan buat API Foundry.

## Pemicu

Aktifkan keterampilan ini ketika pembelajar ingin:
- Mendeploy agen ke Microsoft Foundry sebagai **agen yang dihosting** dan membuatnya versi/terobservasi.
- Memilih antara pola deploy **client-hosted, hosted-agent, dan agent-workflow**.
- Menambahkan **routing model**, **penyimpanan respons (response caching)**, atau **konkurensi terbatas** untuk mengontrol latensi dan biaya.
- Menambahkan **gerbang evaluasi** supaya versi agen yang buruk tidak dikirim.
- Menambahkan langkah **persetujuan manusia dalam proses (human-in-the-loop)** untuk tindakan berisiko tinggi.
- Menginstrumentasi agen dengan **OpenTelemetry** untuk pelacakan observabilitas produksi.
- **Smoke-test** agen yang dideploy sebagai gerbang cepat pasca deploy.

## Model mental inti

Agen produksi sebagian besar adalah kerangka operasional *di sekitar* model (~80%),
bukan model itu sendiri. Peta setiap rekomendasi ke salah satu perhatian ini:

| Perhatian | Prototipe → Produksi |
|---------|------------------------|
| Hosting | notebook → layanan hosted versi |
| Identitas | `az login` Anda → managed identity + RBAC terperinci |
| Status | di memori → penyimpanan thread/memori eksternal |
| Kegagalan | jejak kesalahan → pengulangan, fallback, peringatan |
| Biaya | "beberapa sen" → dilacak, diarahkan, disimpan, dianggarkan |
| Kualitas | penilaian manual → gerbang evaluasi otomatis |
| Kepercayaan | Anda setuju → kebijakan + manusia dalam proses |

## Pola deploy (pilih satu, atau gabungkan)

1. **Client-hosted** — loop penalaran berjalan di proses Anda. Kontrol maksimal; Anda mengelola skala/status.
2. **Hosted agent (Foundry Agent Service)** — Foundry menghosting loop, menyimpan thread, menerapkan RBAC/keamanan konten, menampilkan agen di portal. Kontrol lebih sedikit, permukaan operasional jauh lebih kecil.
3. **Agent workflow** — beberapa agen/alat disusun dalam graf dengan cabang, node persetujuan, dan checkpoint tahan lama.

## Siklus hidup (loop yang mengirim agen)

`create → version → evaluate (gate) → deploy hosted → observe online → collect failures → repeat`.
**Evaluasi offline adalah gerbang, bukan pikiran terakhir** — versi tidak dikirim
kecuali melewati ambang batas. Observasi online mengembalikan kegagalan nyata
ke set pengujian offline.

## Tuas skala dan biaya (urutan prioritas)

1. **Sesuaikan ukuran model** — gunakan model terkecil yang lolos gerbang evaluasi.
2. **Routing berdasarkan kompleksitas** — model kecil/cepat untuk permintaan sederhana, model besar untuk penalaran nyata (klasifikasi DIY atau Foundry Model Router).
3. **Cache** — layani permintaan hampir duplikat tanpa panggilan model.
4. **Desain tanpa status + konkurensi terbatas** — eksternalisasi status; ulangi dengan penundaan kembali.

## Pola kunci untuk direproduksi

Arahkan pembelajar ke ini dari notebook
[`16-python-agent-framework.ipynb`](../../../16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb):

- **Penangan permintaan**: cache → route berdasarkan kompleksitas → span jejak → jalankan → cache.
- **Gerbang evaluasi**: beri skor set pengujian offline; kembalikan `pass_rate >= threshold` dan hanya deploy jika benar.
- **Persetujuan manusia**: `@tool(approval_mode="always_require")` untuk tindakan seperti pengembalian dana besar.
- **Pelacakan**: bungkus setiap permintaan dalam `tracer.start_as_current_span(...)` dan atur atribut seperti `routed.model`, `customer.id`.

## Smoke-test agen yang sudah dideploy

Setelah deploy, verifikasi endpoint benar-benar menjawab (deploy hijau masih bisa
diam). Gunakan aksi [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
melalui [`.github/workflows/smoke-test.yml`](../../../../../.github/workflows/smoke-test.yml)
dengan katalog di [`tests/`](../../../tests/README.md). Runner meng-POST setiap
prompt ke `POST {project_endpoint}/agents/{agent_name}/endpoint/protocols/openai/responses`
dan memeriksa teks balasan. Identitas membutuhkan peran **Azure AI User** di
lingkup proyek Foundry; audiens token harus `https://ai.azure.com/`.

Lapisi gerbang: **smoke test** (terjangkau/merespon, setiap deploy) → **evaluasi offline**
(cukup baik untuk dikirim, sebelum promosi) → **evaluasi online** (bagaimana
performanya di dunia nyata, berkelanjutan).

## Kontrol perusahaan

- **RBAC**: berikan setiap agen hosted sebuah managed identity dengan hak minimum.
- **MCP di produksi**: perlakukan setiap server MCP sebagai batas yang tidak dipercaya — pin versinya, batasi identitasnya, validasi keluaran, batasi tingkat, jangan pernah ekspose rahasia.

## Pedoman untuk asisten

- Prefer pola kanonik `FoundryChatClient(...)` + `provider.as_agent(...)` yang digunakan di seluruh kursus.
- Jangan menjanjikan hasil live-Azure yang belum Anda verifikasi; rekomendasikan alur kerja smoke-test untuk mengonfirmasi deploy.
- Jaga evaluasi dan saran biaya agar tetap terkait: evaluasi menetapkan batas kualitas, routing/caching menjaga biaya dekat batas tersebut.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->