---
name: microsoft-docs
description: Kueri dokumentasi rasmi Microsoft untuk mencari konsep, tutorial, dan
  contoh kod merentas Azure, .NET, Agent Framework, Aspire, VS Code, GitHub, dan banyak
  lagi. Menggunakan Microsoft Learn MCP sebagai lalai, dengan Context7 dan Aspire
  MCP untuk kandungan yang berada di luar learn.microsoft.com.
---
# Microsoft Docs

Kemahiran penyelidikan untuk ekosistem teknologi Microsoft. Merangkumi learn.microsoft.com dan dokumentasi yang berada di luarnya (repo VS Code, GitHub, Aspire, Agent Framework).

---

## Default: Microsoft Learn MCP

Gunakan alat ini untuk **segala-galanya di learn.microsoft.com** — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows, dan lain-lain. Ini adalah alat utama untuk sebahagian besar pertanyaan dokumentasi Microsoft.

| Tool | Purpose |
|------|---------|
| `microsoft_docs_search` | Search learn.microsoft.com — concepts, guides, tutorials, configuration |
| `microsoft_code_sample_search` | Find working code snippets from Learn docs. Pass `language` (`python`, `csharp`, etc.) for best results |
| `microsoft_docs_fetch` | Get full page content from a specific URL (when search excerpts aren't enough) |

Gunakan `microsoft_docs_fetch` selepas carian apabila anda memerlukan tutorial lengkap, semua pilihan konfigurasi, atau apabila petikan carian dipendekkan.

---

## Exceptions: When to Use Other Tools

Kategori berikut berada di **luar** learn.microsoft.com. Gunakan alat yang ditentukan sebaliknya.

### .NET Aspire — Use Aspire MCP Server (preferred) or Context7

Dokumen Aspire berada di **aspire.dev**, bukan di Learn. Alat terbaik bergantung kepada versi Aspire CLI anda:

**CLI 13.2+** (disyorkan) — Pelayan Aspire MCP termasuk alat carian dokumen terbina dalam:

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | Menyenaraikan semua dokumentasi yang tersedia daripada aspire.dev |
| `search_docs` | Carian leksikal berbobot merentasi kandungan aspire.dev |
| `get_doc` | Mendapatkan dokumen tertentu berdasarkan slug |

These ship in Aspire CLI 13.2 ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). To update: `aspire update --self --channel daily`. Ruj: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — Pelayan MCP menyediakan carian integrasi (`list_integrations`, `get_integration_docs`) tetapi **bukan** carian dokumen. Gunakan Context7 sebagai ganti:

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | Utama — panduan, integrasi, rujukan CLI, penyebaran |
| `/dotnet/aspire` | Sumber runtime — dalaman API, butiran pelaksanaan |
| `/communitytoolkit/aspire` | Integrasi komuniti — Go, Java, Node.js, Ollama |

### VS Code — Use Context7

Dokumen VS Code berada di **code.visualstudio.com**, bukan di Learn.

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | Dokumen pengguna — tetapan, ciri, penyahpepijatan, pembangunan jauh |
| `/websites/code_visualstudio_api` | API sambungan — webviews, TreeViews, commands, contribution points |

### GitHub — Use Context7

Dokumen GitHub berada di **docs.github.com** dan **cli.github.com**.

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions, API, repositori, keselamatan, pentadbiran, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) arahan dan flag |

### Agent Framework — Use Learn MCP + Context7

Tutorial Agent Framework berada di learn.microsoft.com (gunakan `microsoft_docs_search`), tetapi **repo GitHub** mempunyai butiran peringkat API yang sering lebih terkini berbanding dokumen yang diterbitkan — terutamanya rujukan DevUI REST API, pilihan CLI, dan integrasi .NET.

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Tutorial — panduan DevUI, penjejakan, orkestrasi aliran kerja |
| `/microsoft/agent-framework` | Butiran API — endpoint DevUI REST, flag CLI, pengesahan, .NET `AddDevUI`/`MapDevUI` |

**Petua DevUI:** Pertanyakan sumber laman Learn untuk panduan cara, kemudian sumber repo untuk perincian peringkat API (skema endpoint, konfigurasi proksi, token pengesahan).

---

## Context7 Setup

Untuk sebarang pertanyaan Context7, selesaikan ID perpustakaan terlebih dahulu (sekali per sesi):

1. Panggil `mcp_context7_resolve-library-id` dengan nama teknologi
2. Panggil `mcp_context7_query-docs` dengan ID perpustakaan yang dikembalikan dan pertanyaan yang spesifik

---

## Writing Effective Queries

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
- **Niat tugas** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Bahasa** untuk dokumentasi pelbagai bahasa (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Penafian:
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI Co-op Translator (https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk memastikan ketepatan, sila ambil perhatian bahawa terjemahan automatik mungkin mengandungi ralat atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, disarankan agar terjemahan profesional oleh penterjemah manusia digunakan. Kami tidak bertanggungjawab terhadap sebarang salah faham atau salah tafsiran yang timbul daripada penggunaan terjemahan ini.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->