---
name: microsoft-docs
description: Dapatkan dokumentasi rasmi Microsoft untuk mencari konsep, tutorial,
  dan contoh kod merentasi Azure, .NET, Agent Framework, Aspire, VS Code, GitHub,
  dan banyak lagi. Menggunakan Microsoft Learn MCP sebagai lalai, dengan Context7
  dan Aspire MCP untuk kandungan yang berada di luar learn.microsoft.com.
---
# Microsoft Docs

Kemahiran penyelidikan untuk ekosistem teknologi Microsoft. Merangkumi learn.microsoft.com dan dokumentasi yang berada di luar daripadanya (VS Code, GitHub, Aspire, repos Kerangka Agen).

---

## Lalai: Microsoft Learn MCP

Gunakan alat ini untuk **segala-galanya di learn.microsoft.com** — Azure, .NET, M365, Power Platform, Kerangka Agen, Semantic Kernel, Windows, dan banyak lagi. Ini adalah alat utama untuk kebanyakan pertanyaan dokumentasi Microsoft.

| Alat | Tujuan |
|------|---------|
| `microsoft_docs_search` | Cari learn.microsoft.com — konsep, panduan, tutorial, konfigurasi |
| `microsoft_code_sample_search` | Cari kod snippet yang berfungsi dari dokumen Learn. Berikan `language` (`python`, `csharp`, dan lain-lain) untuk hasil terbaik |
| `microsoft_docs_fetch` | Dapatkan kandungan halaman penuh dari URL tertentu (apabila petikan carian tidak mencukupi) |

Gunakan `microsoft_docs_fetch` selepas carian apabila anda memerlukan tutorial lengkap, semua pilihan konfigurasi, atau apabila petikan carian dipendekkan.

---

## Pengecualian: Bila Menggunakan Alat Lain

Kategori berikut berada **di luar** learn.microsoft.com. Gunakan alat yang ditetapkan sebaliknya.

### Aspire — Gunakan Aspire MCP Server (pilihan utama) atau Context7

Dokumen Aspire berada di **aspire.dev**, bukan Learn. Alat terbaik bergantung pada versi Aspire CLI anda:

**CLI 13.2+** (disyorkan) — Server Aspire MCP termasuk alat carian dokumen terbina dalam:

| Alat MCP | Penerangan |
|----------|-------------|
| `list_docs` | Senaraikan semua dokumentasi tersedia dari aspire.dev |
| `search_docs` | Carian leksikal berwajaran merentasi kandungan aspire.dev |
| `get_doc` | Mendapatkan dokumen tertentu berdasarkan slug |

Ini disertakan dalam Aspire CLI 13.2 ([PR #14028](https://github.com/microsoft/aspire/pull/14028)). Untuk mengemas kini: `aspire update --self --channel daily`.

**CLI 13.1** — Server MCP menyediakan carian integrasi (`list_integrations`, `get_integration_docs`) tetapi **tidak** carian dokumen. Gunakan Context7 sebagai gantian:

| ID Perpustakaan | Digunakan untuk |
|---|---|
| `/microsoft/aspire.dev` | Utama — panduan, integrasi, rujukan CLI, penyebaran |
| `/microsoft/aspire` | Sumber runtime — API dalaman, butiran pelaksanaan |
| `/communitytoolkit/aspire` | Integrasi komuniti — Go, Java, Node.js, Ollama |

### VS Code — Gunakan Context7

Dokumen VS Code berada di **code.visualstudio.com**, bukan Learn.

| ID Perpustakaan | Digunakan untuk |
|---|---|
| `/websites/code_visualstudio` | Dokumen pengguna — tetapan, ciri, debug, pembangunan jauh |
| `/websites/code_visualstudio_api` | API peluasan — webviews, TreeViews, arahan, titik sumbangan |

### GitHub — Gunakan Context7

Dokumen GitHub berada di **docs.github.com** dan **cli.github.com**.

| ID Perpustakaan | Digunakan untuk |
|---|---|
| `/websites/github_en` | Tindakan, API, repositori, keselamatan, pentadbiran, Copilot |
| `/websites/cli_github` | Arahan dan bendera GitHub CLI (`gh`) |

### Kerangka Agen — Gunakan Learn MCP + Context7

Tutorial Kerangka Agen berada di learn.microsoft.com (gunakan `microsoft_docs_search`), tetapi **repo GitHub** mempunyai butiran tahap API yang sering lebih terkini daripada dokumen yang diterbitkan — terutamanya rujukan REST API DevUI, pilihan CLI, dan integrasi .NET.

| ID Perpustakaan | Digunakan untuk |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Tutorial — panduan DevUI, penjejakan, penataan aliran kerja |
| `/microsoft/agent-framework` | Butiran API — titik akhir REST DevUI, bendera CLI, pengesahan, .NET `AddDevUI`/`MapDevUI` |

**Petua DevUI:** Tanyakan sumber laman Learn untuk panduan cara, kemudian sumber repo untuk spesifik tahap API (skema titik akhir, konfigurasi proxy, token pengesahan).

---

## Persediaan Context7

Untuk mana-mana pertanyaan Context7, selesaikan ID perpustakaan terlebih dahulu (sekali setiap sesi):

1. Panggil `mcp_context7_resolve-library-id` dengan nama teknologi
2. Panggil `mcp_context7_query-docs` dengan ID perpustakaan yang dikembalikan dan pertanyaan khusus

---

## Menulis Pertanyaan Berkesan

Jadilah spesifik — sertakan versi, niat, dan bahasa:

```
# ❌ Too broad
"Azure Functions"
"agent framework"

# ✅ Specific
"Azure Functions Python v2 programming model"
"Cosmos DB partition key design best practices"
"GitHub Actions workflow_dispatch inputs matrix strategy"
"Aspire AddUvicornApp Python FastAPI integration"
"DevUI serve agents tracing OpenTelemetry directory discovery"
"Agent Framework workflow conditional edges branching handoff"
```

Sertakan konteks:
- **Versi** apabila relevan (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Niat tugasan** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Bahasa** untuk dokumentasi poliglot (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan oleh manusia profesional adalah disyorkan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->