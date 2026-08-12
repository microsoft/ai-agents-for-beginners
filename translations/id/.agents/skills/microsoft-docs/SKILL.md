---
name: microsoft-docs
description: Menelusuri dokumentasi resmi Microsoft untuk menemukan konsep, tutorial,
  dan contoh kode di seluruh Azure, .NET, Agent Framework, Aspire, VS Code, GitHub,
  dan lainnya. Menggunakan Microsoft Learn MCP sebagai default, dengan Context7 dan
  Aspire MCP untuk konten yang berada di luar learn.microsoft.com.
---
# Microsoft Docs

Keterampilan riset untuk ekosistem teknologi Microsoft. Mencakup learn.microsoft.com dan dokumentasi yang berada di luar situs tersebut (repo VS Code, GitHub, Aspire, Agent Framework).

---

## Default: Microsoft Learn MCP

Gunakan alat-alat ini untuk **semua hal di learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows, dan lainnya. Ini adalah alat utama untuk sebagian besar kueri dokumentasi Microsoft.

| Alat | Tujuan |
|------|---------|
| `microsoft_docs_search` | Cari learn.microsoft.com — konsep, panduan, tutorial, konfigurasi |
| `microsoft_code_sample_search` | Temukan potongan kode yang berfungsi dari dokumen Learn. Berikan `language` (`python`, `csharp`, dll.) untuk hasil terbaik |
| `microsoft_docs_fetch` | Dapatkan konten halaman penuh dari URL tertentu (ketika kutipan hasil pencarian tidak cukup) |

Gunakan `microsoft_docs_fetch` setelah pencarian ketika Anda membutuhkan tutorial lengkap, semua opsi konfigurasi, atau ketika kutipan hasil pencarian dipotong.

---

## Exceptions: When to Use Other Tools

Kategori berikut berada **di luar** learn.microsoft.com. Gunakan alat yang ditentukan sebagai gantinya.

### .NET Aspire — Gunakan Aspire MCP Server (direkomendasikan) atau Context7

Dokumentasi Aspire berada di **aspire.dev**, bukan Learn. Alat terbaik bergantung pada versi Aspire CLI Anda:

**CLI 13.2+** (disarankan) — Server Aspire MCP menyertakan alat pencarian dokumen bawaan:

| MCP Tool | Deskripsi |
|----------|-------------|
| `list_docs` | Mencantumkan semua dokumentasi yang tersedia dari aspire.dev |
| `search_docs` | Pencarian leksikal berbobot di seluruh konten aspire.dev |
| `get_doc` | Mengambil dokumen tertentu berdasarkan slug |

Fitur ini dikirimkan pada Aspire CLI 13.2 ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). Untuk memperbarui: `aspire update --self --channel daily`. Ref: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — Server MCP menyediakan pencarian integrasi (`list_integrations`, `get_integration_docs`) tetapi **tidak** pencarian dokumen. Kembalikan ke Context7:

| Library ID | Gunakan untuk |
|---|---|
| `/microsoft/aspire.dev` | Utama — panduan, integrasi, referensi CLI, deployment |
| `/dotnet/aspire` | Sumber runtime — internal API, detail implementasi |
| `/communitytoolkit/aspire` | Integrasi komunitas — Go, Java, Node.js, Ollama |

### VS Code — Gunakan Context7

Dokumentasi VS Code berada di **code.visualstudio.com**, bukan Learn.

| Library ID | Gunakan untuk |
|---|---|
| `/websites/code_visualstudio` | Dokumen pengguna — pengaturan, fitur, debugging, pengembangan jarak jauh |
| `/websites/code_visualstudio_api` | API ekstensi — webviews, TreeViews, perintah, titik kontribusi |

### GitHub — Gunakan Context7

Dokumentasi GitHub berada di **docs.github.com** dan **cli.github.com**.

| Library ID | Gunakan untuk |
|---|---|
| `/websites/github_en` | Actions, API, repositori, keamanan, admin, Copilot |
| `/websites/cli_github` | Perintah dan flag GitHub CLI (`gh`) |

### Agent Framework — Gunakan Learn MCP + Context7

Tutorial Agent Framework ada di learn.microsoft.com (gunakan `microsoft_docs_search`), tetapi **repo GitHub** memiliki detail tingkat API yang seringkali lebih maju daripada dokumen yang dipublikasikan — khususnya referensi REST API DevUI, opsi CLI, dan integrasi .NET.

| Library ID | Gunakan untuk |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Tutorial — panduan DevUI, tracing, orkestrasi alur kerja |
| `/microsoft/agent-framework` | Detail API — endpoint REST DevUI, flag CLI, autentikasi, .NET `AddDevUI`/`MapDevUI` |

**Tip DevUI:** Kuari sumber situs Learn untuk panduan how-to, lalu sumber repo untuk spesifik tingkat API (skema endpoint, konfigurasi proxy, token autentikasi).

---

## Context7 Setup

Untuk setiap kueri Context7, tentukan library ID terlebih dahulu (sekali per sesi):

1. Panggil `mcp_context7_resolve-library-id` dengan nama teknologi
2. Panggil `mcp_context7_query-docs` dengan library ID yang dikembalikan dan kueri spesifik

---

## Writing Effective Queries

Jadilah spesifik — sertakan versi, tujuan, dan bahasa:

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
- **Versi** bila relevan (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Tujuan tugas** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Bahasa** untuk dokumentasi poliglot (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Penafian:
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya mencapai akurasi, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan menggunakan terjemahan profesional oleh penerjemah manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->