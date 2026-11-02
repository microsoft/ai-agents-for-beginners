---
name: microsoft-docs
description: Query dokumentasi resmi Microsoft untuk menemukan konsep, tutorial, dan
  contoh kode di seluruh Azure, .NET, Agent Framework, Aspire, VS Code, GitHub, dan
  lainnya. Menggunakan Microsoft Learn MCP sebagai default, dengan Context7 dan Aspire
  MCP untuk konten yang berada di luar learn.microsoft.com.
---
# Microsoft Docs

Keterampilan riset untuk ekosistem teknologi Microsoft. Mencakup learn.microsoft.com dan dokumentasi yang berada di luar situs tersebut (VS Code, GitHub, Aspire, repositori Agent Framework).

---

## Default: Microsoft Learn MCP

Gunakan alat ini untuk **semua hal di learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows, dan lainnya. Ini adalah alat utama untuk sebagian besar pencarian dokumentasi Microsoft.

| Tool | Tujuan |
|------|---------|
| `microsoft_docs_search` | Cari learn.microsoft.com — konsep, panduan, tutorial, konfigurasi |
| `microsoft_code_sample_search` | Temukan potongan kode yang bekerja dari dokumen Learn. Gunakan `language` (`python`, `csharp`, dll.) untuk hasil terbaik |
| `microsoft_docs_fetch` | Dapatkan konten halaman lengkap dari URL spesifik (ketika kutipan pencarian tidak cukup) |

Gunakan `microsoft_docs_fetch` setelah pencarian saat Anda membutuhkan tutorial lengkap, semua opsi konfigurasi, atau ketika kutipan pencarian terpotong.

---

## Pengecualian: Kapan Menggunakan Alat Lain

Kategori berikut berada **di luar** learn.microsoft.com. Gunakan alat yang ditentukan sebagai gantinya.

### Aspire — Gunakan Aspire MCP Server (disarankan) atau Context7

Dokumen Aspire berada di **aspire.dev**, bukan Learn. Alat terbaik tergantung pada versi Aspire CLI Anda:

**CLI 13.2+** (direkomendasikan) — Server Aspire MCP menyertakan alat pencarian dokumen bawaan:

| Alat MCP | Deskripsi |
|----------|-------------|
| `list_docs` | Daftar semua dokumentasi yang tersedia dari aspire.dev |
| `search_docs` | Pencarian leksikal berbobot di seluruh konten aspire.dev |
| `get_doc` | Mengambil dokumen spesifik berdasarkan slug |

Fitur ini tersedia di Aspire CLI 13.2 ([PR #14028](https://github.com/microsoft/aspire/pull/14028)). Untuk memperbarui: `aspire update --self --channel daily`.

**CLI 13.1** — Server MCP menyediakan pencarian integrasi (`list_integrations`, `get_integration_docs`) tetapi **tidak** pencarian dokumen. Gunakan Context7 sebagai alternatif:

| ID Perpustakaan | Digunakan untuk |
|---|---|
| `/microsoft/aspire.dev` | Utama — panduan, integrasi, referensi CLI, deployment |
| `/microsoft/aspire` | Sumber runtime — API internal, detail implementasi |
| `/communitytoolkit/aspire` | Integrasi komunitas — Go, Java, Node.js, Ollama |

### VS Code — Gunakan Context7

Dokumentasi VS Code berada di **code.visualstudio.com**, bukan Learn.

| ID Perpustakaan | Digunakan untuk |
|---|---|
| `/websites/code_visualstudio` | Dokumentasi pengguna — pengaturan, fitur, debugging, pengembangan jarak jauh |
| `/websites/code_visualstudio_api` | Ekstensi API — webviews, TreeViews, perintah, titik kontribusi |

### GitHub — Gunakan Context7

Dokumentasi GitHub berada di **docs.github.com** dan **cli.github.com**.

| ID Perpustakaan | Digunakan untuk |
|---|---|
| `/websites/github_en` | Actions, API, repositori, keamanan, admin, Copilot |
| `/websites/cli_github` | Perintah dan flag GitHub CLI (`gh`) |

### Agent Framework — Gunakan Learn MCP + Context7

Tutorial Agent Framework ada di learn.microsoft.com (gunakan `microsoft_docs_search`), tetapi **repositori GitHub** memiliki detail level API yang sering lebih mutakhir daripada dokumen yang diterbitkan — terutama referensi DevUI REST API, opsi CLI, dan integrasi .NET.

| ID Perpustakaan | Digunakan untuk |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Tutorial — panduan DevUI, pelacakan, orkestrasi workflow |
| `/microsoft/agent-framework` | Detail API — endpoint REST DevUI, flag CLI, otentikasi, .NET `AddDevUI`/`MapDevUI` |

**Tips DevUI:** Cari sumber situs Learn untuk panduan cara, lalu lihat sumber repositori untuk spesifik tingkat API (skema endpoint, konfigurasi proxy, token otentikasi).

---

## Pengaturan Context7

Untuk setiap kueri Context7, tentukan ID perpustakaan terlebih dahulu (sekali per sesi):

1. Panggil `mcp_context7_resolve-library-id` dengan nama teknologi
2. Panggil `mcp_context7_query-docs` dengan ID perpustakaan yang dikembalikan dan kueri spesifik

---

## Menulis Kueri yang Efektif

Jadilah spesifik — sertakan versi, maksud, dan bahasa:

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
- **Versi** saat relevan (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Maksud tugas** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Bahasa** untuk dokumentasi poliglot (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Penafian**:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sah. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang keliru yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->