---
name: microsoft-docs
description: Azure, .NET, Agent Framework, Aspire, VS Code, GitHub ve daha fazlası
  gibi Microsoft resmi belgelerinde kavramlar, eğitimler ve kod örnekleri arayın.
  Varsayılan olarak Microsoft Learn MCP'yi kullanır, learn.microsoft.com dışındaki
  içerikler için Context7 ve Aspire MCP'yi kullanır.
---
# Microsoft Docs

Microsoft teknoloji ekosistemi için araştırma becerisi. learn.microsoft.com ve bunun dışında bulunan dökümantasyonları kapsar (VS Code, GitHub, Aspire, Agent Framework depoları).

---

## Varsayılan: Microsoft Learn MCP

**learn.microsoft.com üzerindeki her şey** için bu araçları kullanın — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows ve daha fazlası. Bu araç, Microsoft dökümantasyon sorgularının büyük çoğunluğu için birincil araçtır.

| Araç | Amaç |
|------|---------|
| `microsoft_docs_search` | learn.microsoft.com içinde ara — kavramlar, rehberler, öğreticiler, yapılandırma |
| `microsoft_code_sample_search` | Learn dökümanlarından çalışan kod parçacıkları bul. En iyi sonuçlar için `language` (`python`, `csharp`, vb.) kullan. |
| `microsoft_docs_fetch` | Belirli bir URL'den tam sayfa içeriği al (arama alıntıları yeterli olmadığında) |

Arama sonrası, eksiksiz öğreticilere, tüm yapılandırma seçeneklerine ihtiyacınız olduğunda veya arama alıntıları kısaltıldığında `microsoft_docs_fetch` kullanın.

---

## İstisnalar: Diğer Araçlar Ne Zaman Kullanılır

Aşağıdaki kategoriler **learn.microsoft.com dışındadır**. Bunun yerine belirtilen aracı kullanın.

### Aspire — Aspire MCP Sunucusu (tercih edilen) veya Context7 kullanın

Aspire dokümanları **aspire.dev** sitesinde bulunur, Learn'de değil. En iyi araç Aspire CLI sürümünüze bağlıdır:

**CLI 13.2+** (önerilen) — Aspire MCP sunucusu dahili doküman arama araçlarını içerir:

| MCP Aracı | Açıklama |
|----------|-------------|
| `list_docs` | aspire.dev sitesindeki tüm mevcut dokümanları listeler |
| `search_docs` | aspire.dev içeriğinde ağırlıklı sözcüksel arama yapar |
| `get_doc` | Belirli bir belgeyi slug ile getirir |

Bunlar Aspire CLI 13.2 ile gelir ([PR #14028](https://github.com/microsoft/aspire/pull/14028)). Güncellemek için: `aspire update --self --channel daily`.

**CLI 13.1** — MCP sunucusu entegrasyon araması sağlar (`list_integrations`, `get_integration_docs`) ama **doküman araması sağlamaz**. Bu durumda Context7 kullanın:

| Kütüphane ID | Kullanım Alanı |
|---|---|
| `/microsoft/aspire.dev` | Birincil — rehberler, entegrasyonlar, CLI referansı, dağıtım |
| `/microsoft/aspire` | Çalışma zamanı kaynakları — API iç detayları, uygulama ayrıntıları |
| `/communitytoolkit/aspire` | Topluluk entegrasyonları — Go, Java, Node.js, Ollama |

### VS Code — Context7 kullanın

VS Code dokümanları **code.visualstudio.com** sitesinde bulunur, Learn'de değil.

| Kütüphane ID | Kullanım Alanı |
|---|---|
| `/websites/code_visualstudio` | Kullanıcı dokümanları — ayarlar, özellikler, hata ayıklama, uzak geliştirme |
| `/websites/code_visualstudio_api` | Uzantı API — webview'ler, TreeView'lar, komutlar, katkı noktaları |

### GitHub — Context7 kullanın

GitHub dokümanları **docs.github.com** ve **cli.github.com** adreslerinde bulunur.

| Kütüphane ID | Kullanım Alanı |
|---|---|
| `/websites/github_en` | Actions, API, depolar, güvenlik, yönetim, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) komutları ve bayrakları |

### Agent Framework — Learn MCP + Context7 kullanın

Agent Framework öğreticileri learn.microsoft.com üzerindedir (`microsoft_docs_search` kullanın), ancak **GitHub deposu** genellikle yayımlanan dokümanlardan daha güncel olan API düzeyinde detaylar içerir — özellikle DevUI REST API referansı, CLI seçenekleri ve .NET entegrasyonu.

| Kütüphane ID | Kullanım Alanı |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | Öğreticiler — DevUI rehberleri, izleme, iş akışı düzenleme |
| `/microsoft/agent-framework` | API detayları — DevUI REST uç noktaları, CLI bayrakları, kimlik doğrulama, .NET `AddDevUI`/`MapDevUI` |

**DevUI ipucu:** Öğretici rehberleri için Learn web sitesi kaynağını, ardından uç nokta şemaları, proxy konfigürasyonu, kimlik doğrulama jetonları gibi API düzeyinde detaylar için depo kaynağını sorgulayın.

---

## Context7 Kurulumu

Herhangi bir Context7 sorgusu için öncelikle kütüphane ID'sini çözümleyin (oturum başına bir kez):

1. Teknoloji adıyla `mcp_context7_resolve-library-id` çağırın
2. Dönen kütüphane ID'si ve belirli bir sorguyla `mcp_context7_query-docs` çağırın

---

## Etkili Sorgular Yazma

Spesifik olun — sürüm, niyet ve dili dahil edin:

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
- İlgili olduğunda **Sürüm** (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **Görev niyeti** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- Poliglot belgeler için **Dil** (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Feragatname**:
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba sarf etsek de, otomatik çevirilerin hata veya yanlışlık içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu ortaya çıkabilecek yanlış anlamalardan veya yanlış yorumlamalardan sorumlu değiliz.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->