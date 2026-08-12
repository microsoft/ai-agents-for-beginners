---
name: microsoft-docs
description: Resmi Microsoft belgelerini sorgulayarak Azure, .NET, Agent Framework,
  Aspire, VS Code, GitHub ve daha fazlası genelinde kavramlar, öğreticiler ve kod
  örnekleri bulabilirsiniz. Varsayılan olarak Microsoft Learn MCP kullanılır; learn.microsoft.com
  dışında yer alan içerikler için Context7 ve Aspire MCP kullanılır.
---
# Microsoft Docs

Microsoft teknoloji ekosistemi için araştırma becerisi. learn.microsoft.com ve bunun dışında bulunan belgeleri kapsar (VS Code, GitHub, Aspire, Agent Framework depoları).

---

## Default: Microsoft Learn MCP

Bu araçları **learn.microsoft.com üzerindeki her şey için** kullanın — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows ve daha fazlası. Bu, Microsoft belgeleriyle ilgili soruların büyük çoğunluğu için birincil araçtır.

| Tool | Purpose |
|------|---------|
| `microsoft_docs_search` | learn.microsoft.com içinde arama — kavramlar, kılavuzlar, öğreticiler, yapılandırma |
| `microsoft_code_sample_search` | Learn belgelerinden çalışan kod parçacıklarını bulun. En iyi sonuçlar için `language` (`python`, `csharp`, vb.) parametresini geçin |
| `microsoft_docs_fetch` | Belirli bir URL'den tam sayfa içeriğini alın (arama alıntıları yeterli olmadığında) |

Arama sonrası tam öğreticilere, tüm yapılandırma seçeneklerine veya arama alıntıları kesildiğinde `microsoft_docs_fetch` kullanın.

---

## Exceptions: When to Use Other Tools

Aşağıdaki kategoriler **learn.microsoft.com dışında** yer alır. Bunun yerine belirtilen aracı kullanın.

### .NET Aspire — Use Aspire MCP Server (preferred) or Context7

Aspire belgeleri **aspire.dev** üzerinde bulunur, Learn üzerinde değil. En iyi araç Aspire CLI sürümünüze bağlıdır:

**CLI 13.2+** (önerilir) — Aspire MCP sunucusu yerleşik belge arama araçları içerir:

| MCP Tool | Description |
|----------|-------------|
| `list_docs` | aspire.dev içindeki tüm kullanılabilir belgeleri listeler |
| `search_docs` | aspire.dev içeriği üzerinde ağırlıklı leksikal arama yapar |
| `get_doc` | Belirli bir slug ile bir belge getirir |

Bunlar Aspire CLI 13.2 ile gelir ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). Güncellemek için: `aspire update --self --channel daily`. Ref: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — MCP sunucusu entegrasyon araması (`list_integrations`, `get_integration_docs`) sağlar ancak belge araması sağlamaz. Context7'e geri dönün:

| Library ID | Use for |
|---|---|
| `/microsoft/aspire.dev` | Birincil — kılavuzlar, entegrasyonlar, CLI referansı, dağıtım |
| `/dotnet/aspire` | Çalışma zamanı kaynağı — API iç detayları, uygulama ayrıntıları |
| `/communitytoolkit/aspire` | Topluluk entegrasyonları — Go, Java, Node.js, Ollama |

### VS Code — Use Context7

VS Code belgeleri **code.visualstudio.com** üzerinde bulunur, Learn üzerinde değil.

| Library ID | Use for |
|---|---|
| `/websites/code_visualstudio` | Kullanıcı belgeleri — ayarlar, özellikler, hata ayıklama, uzak geliştirme |
| `/websites/code_visualstudio_api` | Uzantı API'si — web görünümleri, TreeView'lar, komutlar, katkı noktaları |

### GitHub — Use Context7

GitHub belgeleri **docs.github.com** ve **cli.github.com** üzerinde bulunur.

| Library ID | Use for |
|---|---|
| `/websites/github_en` | Actions, API, depolar, güvenlik, yönetim, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) komutları ve bayrakları |

### Agent Framework — Use Learn MCP + Context7

Agent Framework öğreticileri learn.microsoft.com üzerinde (kullan `microsoft_docs_search`), ancak **GitHub deposu** genellikle yayımlanmış belgelerden daha ileri düzeyde API ayrıntısına sahiptir — özellikle DevUI REST API referansı, CLI seçenekleri ve .NET entegrasyonu.

| Library ID | Use for |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Öğreticiler — DevUI kılavuzları, izleme, iş akışı orkestrasyonu |
| `/microsoft/agent-framework` | API ayrıntısı — DevUI REST uç noktaları, CLI bayrakları, kimlik doğrulama, .NET `AddDevUI`/`MapDevUI` |

**DevUI ipucu:** Nasıl yapılır kılavuzları için Learn web sitesi kaynağını sorgulayın, ardından uç nokta şemaları, proxy yapılandırması, kimlik doğrulama belirteçleri gibi API düzeyindeki ayrıntılar için depo kaynağına bakın.

---

## Context7 Setup

Herhangi bir Context7 sorgusu için önce kütüphane ID'sini çözün (oturum başına bir kerelik):

1. Teknoloji adı ile `mcp_context7_resolve-library-id` çağırın
2. Döndürülen kütüphane ID'si ve belirli bir sorgu ile `mcp_context7_query-docs` çağırın

---

## Writing Effective Queries

Spesifik olun — sürümü, amacı ve dili dahil edin:

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

Bağlam ekleyin:
- **Version** gerektiğinde (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Task intent** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **Language** çok dilli belgeler için (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, [Co-op Translator](https://github.com/Azure/co-op-translator) adlı yapay zeka çeviri hizmeti kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal diliyle hazırlanmış versiyonu yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucunda ortaya çıkabilecek herhangi bir yanlış anlama veya yanlış yorumdan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->