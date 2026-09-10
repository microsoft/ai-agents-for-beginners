---
name: microsoft-docs
description: 공식 Microsoft 문서를 조회하여 Azure, .NET, Agent Framework, Aspire, VS Code,
  GitHub 등 다양한 분야의 개념, 튜토리얼 및 코드 예제를 찾습니다. 기본적으로 Microsoft Learn MCP를 사용하며, learn.microsoft.com
  외부에 있는 콘텐츠에 대해서는 Context7 및 Aspire MCP를 사용합니다.
---
# Microsoft Docs

Microsoft 기술 생태계에 대한 리서치 스킬입니다. learn.microsoft.com 및 그 밖의 문서(예: VS Code, GitHub, Aspire, Agent Framework 리포지토리)를 다룹니다.

---

## 기본값: Microsoft Learn MCP

다음 도구들을 **learn.microsoft.com의 모든 콘텐츠**에 사용하세요 — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows 등. 대부분의 Microsoft 문서 관련 질문에 대한 주요 도구입니다.

| Tool | 용도 |
|------|---------|
| `microsoft_docs_search` | learn.microsoft.com 검색 — 개념, 가이드, 튜토리얼, 구성 |
| `microsoft_code_sample_search` | Learn 문서에서 작동하는 코드 스니펫을 찾습니다. 최상의 결과를 위해 `language` (`python`, `csharp`, 등)를 전달하세요 |
| `microsoft_docs_fetch` | 특정 URL에서 전체 페이지 콘텐츠를 가져옵니다(검색 발췌가 충분하지 않을 때) |

검색 후 전체 튜토리얼, 모든 구성 옵션 또는 검색 발췌가 잘려있을 때 `microsoft_docs_fetch`를 사용하세요.

---

## 예외: 다른 도구를 사용해야 할 때

다음 카테고리는 **learn.microsoft.com 외부**에 있습니다. 대신 지정된 도구를 사용하세요.

### .NET Aspire — Aspire MCP Server(권장) 또는 Context7 사용

Aspire 문서는 **aspire.dev**에 있으며 Learn에 있지 않습니다. 최적의 도구는 Aspire CLI 버전에 따라 다릅니다:

**CLI 13.2+** (권장) — Aspire MCP 서버에는 내장 문서 검색 도구가 포함되어 있습니다:

| MCP Tool | 설명 |
|----------|-------------|
| `list_docs` | aspire.dev의 사용 가능한 모든 문서를 나열합니다 |
| `search_docs` | aspire.dev 콘텐츠에 대한 가중치 기반 어휘 검색 |
| `get_doc` | 슬러그로 특정 문서를 검색합니다 |

이 기능들은 Aspire CLI 13.2에 포함되어 있습니다 ([PR #14028](https://github.com/dotnet/aspire/pull/14028)). 업데이트하려면: `aspire update --self --channel daily`. 참조: https://davidpine.dev/posts/aspire-docs-mcp-tools/

**CLI 13.1** — MCP 서버는 통합 조회(`list_integrations`, `get_integration_docs`)를 제공하지만 문서 검색은 제공하지 않습니다. 이 경우 Context7을 사용하세요:

| Library ID | 사용 용도 |
|---|---|
| `/microsoft/aspire.dev` | 주요 — 가이드, 통합, CLI 참조, 배포 |
| `/dotnet/aspire` | 런타임 소스 — API 내부, 구현 세부사항 |
| `/communitytoolkit/aspire` | 커뮤니티 통합 — Go, Java, Node.js, Ollama |

### VS Code — Context7 사용

VS Code 문서는 **code.visualstudio.com**에 있으며 Learn에 없습니다.

| Library ID | 사용 용도 |
|---|---|
| `/websites/code_visualstudio` | 사용자 문서 — 설정, 기능, 디버깅, 원격 개발 |
| `/websites/code_visualstudio_api` | 확장 API — webviews, TreeViews, 명령, 기여 포인트 |

### GitHub — Context7 사용

GitHub 문서는 **docs.github.com** 및 **cli.github.com**에 있습니다.

| Library ID | 사용 용도 |
|---|---|
| `/websites/github_en` | Actions, API, 저장소, 보안, 관리자, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) 명령 및 플래그 |

### Agent Framework — Learn MCP + Context7 사용

Agent Framework 튜토리얼은 learn.microsoft.com에 있습니다 (`microsoft_docs_search` 사용), 그러나 **GitHub 리포지토리**에는 종종 공개된 문서보다 앞선 API 수준의 세부사항이 포함되어 있습니다 — 특히 DevUI REST API 레퍼런스, CLI 옵션, .NET 통합 관련.

| Library ID | 사용 용도 |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | 튜토리얼 — DevUI 가이드, 추적, 워크플로 오케스트레이션 |
| `/microsoft/agent-framework` | API 세부사항 — DevUI REST 엔드포인트, CLI 플래그, 인증, .NET `AddDevUI`/`MapDevUI` |

**DevUI 팁:** how-to 가이드는 Learn 웹사이트 소스에서 조회하고, API 수준의 세부사항(엔드포인트 스키마, 프록시 구성, 인증 토큰)은 리포지토리 소스에서 조회하세요.

---

## Context7 설정

Context7 쿼리에서는 세션당 한 번 라이브러리 ID를 먼저 확인하세요:

1. 기술 이름으로 `mcp_context7_resolve-library-id`를 호출합니다
2. 반환된 라이브러리 ID와 구체적인 쿼리로 `mcp_context7_query-docs`를 호출합니다

---

## 효과적인 쿼리 작성

구체적으로 작성하세요 — 버전, 목적, 언어를 포함합니다:

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

Include context:
- **버전** 관련 있는 경우 (`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **작업 의도** (`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- **언어** 다중언어 문서를 위해 (`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나 자동 번역에는 오류나 부정확성이 포함될 수 있음을 유의하시기 바랍니다. 원문(원어로 된 문서)을 권위 있는 출처로 간주하시기 바랍니다. 중요한 정보의 경우에는 전문적인 인간 번역을 권장합니다. 본 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->