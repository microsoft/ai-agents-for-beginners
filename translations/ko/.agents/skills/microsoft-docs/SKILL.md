---
name: microsoft-docs
---
# Microsoft Docs

Microsoft 기술 생태계에 대한 연구 기술. learn.microsoft.com과 그 밖의 문서(VS Code, GitHub, Aspire, Agent Framework 리포지토리)를 다룸.

---

## 기본: Microsoft Learn MCP

<strong>learn.microsoft.com</strong>에서 모두 사용할 수 있는 도구 — Azure, .NET, M365, Power Platform, Agent Framework, Semantic Kernel, Windows 등. 대부분의 Microsoft 문서 검색에 주로 사용되는 도구입니다.

| 도구 | 용도 |
|------|---------|
| `microsoft_docs_search` | learn.microsoft.com 검색 — 개념, 가이드, 튜토리얼, 구성 |
| `microsoft_code_sample_search` | Learn 문서 내 작동하는 코드 조각 찾기. 최상의 결과를 위해 `language` (`python`, `csharp` 등) 전달 |
| `microsoft_docs_fetch` | 특정 URL에서 전체 페이지 콘텐츠 가져오기 (검색 발췌가 충분하지 않을 때) |

검색 후 `microsoft_docs_fetch`를 사용하면 완전한 튜토리얼, 모든 구성 옵션 또는 잘린 검색 발췌가 필요할 때 유용합니다.

---

## 예외: 다른 도구를 사용해야 할 때

다음 카테고리는 <strong>learn.microsoft.com 외부</strong>에 있습니다. 지정된 도구를 대신 사용하세요.

### Aspire — Aspire MCP Server (권장) 또는 Context7 사용

Aspire 문서는 <strong>aspire.dev</strong>에 있으며 Learn에 없습니다. 가장 좋은 도구는 Aspire CLI 버전에 따라 달라집니다:

**CLI 13.2 이상** (권장) — Aspire MCP 서버는 내장된 문서 검색 도구를 포함합니다:

| MCP 도구 | 설명 |
|----------|-------------|
| `list_docs` | aspire.dev의 모든 사용 가능한 문서 나열 |
| `search_docs` | aspire.dev 콘텐츠 전반에 가중치가 부여된 어휘 검색 |
| `get_doc` | 슬러그로 특정 문서 검색 |

이 도구들은 Aspire CLI 13.2 ([PR #14028](https://github.com/microsoft/aspire/pull/14028))에 포함되어 있습니다. 업데이트 방법: `aspire update --self --channel daily`.

**CLI 13.1** — MCP 서버는 통합 조회(`list_integrations`, `get_integration_docs`)는 제공하지만 문서 검색은 제공하지 않습니다. 이 경우 Context7으로 대체하세요:

| 라이브러리 ID | 용도 |
|---|---|
| `/microsoft/aspire.dev` | 주요 문서 — 가이드, 통합, CLI 참조, 배포 |
| `/microsoft/aspire` | 런타임 소스 — API 내부, 구현 세부 사항 |
| `/communitytoolkit/aspire` | 커뮤니티 통합 — Go, Java, Node.js, Ollama |

### VS Code — Context7 사용

VS Code 문서는 <strong>code.visualstudio.com</strong>에 있으며 Learn에 없습니다.

| 라이브러리 ID | 용도 |
|---|---|
| `/websites/code_visualstudio` | 사용자 문서 — 설정, 기능, 디버깅, 원격 개발 |
| `/websites/code_visualstudio_api` | 확장 API — 웹뷰, TreeViews, 명령, 기여 포인트 |

### GitHub — Context7 사용

GitHub 문서는 **docs.github.com** 및 <strong>cli.github.com</strong>에 있습니다.

| 라이브러리 ID | 용도 |
|---|---|
| `/websites/github_en` | 액션, API, 저장소, 보안, 관리자, Copilot |
| `/websites/cli_github` | GitHub CLI (`gh`) 명령어 및 플래그 |

### Agent Framework — Learn MCP + Context7 사용

Agent Framework 튜토리얼은 learn.microsoft.com에 있으며(`microsoft_docs_search` 사용), <strong>GitHub 리포지토리</strong>에는 공개 문서보다 앞선 API 수준 세부 정보가 자주 있습니다 — 특히 DevUI REST API 참조, CLI 옵션, .NET 통합.

| 라이브러리 ID | 용도 |
|---|---|
| `/websites/learn_microsoft_en-us_agent-framework` | 튜토리얼 — DevUI 가이드, 추적, 워크플로우 오케스트레이션 |
| `/microsoft/agent-framework` | API 세부 사항 — DevUI REST 엔드포인트, CLI 플래그, 인증, .NET `AddDevUI`/`MapDevUI` |

**DevUI 팁:** Learn 웹사이트 소스에서 작업 가이드를 조회한 후, 리포지토리 소스에서 API 수준 구체 정보(엔드포인트 스키마, 프록시 구성, 인증 토큰) 조회.

---

## Context7 설정

모든 Context7 쿼리에 대해 먼저 라이브러리 ID를 확인하세요(세션당 한 번만):

1. 기술 이름으로 `mcp_context7_resolve-library-id` 호출
2. 반환된 라이브러리 ID와 특정 쿼리로 `mcp_context7_query-docs` 호출

---

## 효과적인 쿼리 작성

구체적으로 작성 — 버전, 의도, 언어 포함:

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

문맥 포함:
- 관련 시 <strong>버전</strong>(`.NET 8`, `Aspire 13`, `VS Code 1.96`)
- **작업 의도**(`quickstart`, `tutorial`, `overview`, `limits`, `API reference`)
- 폴리글롯 문서를 위한 <strong>언어</strong>(`Python`, `TypeScript`, `C#`)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->