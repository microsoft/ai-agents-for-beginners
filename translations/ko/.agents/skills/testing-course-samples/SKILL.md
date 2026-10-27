---
name: testing-course-samples
description: "Use when asked to validate, test, smoke-test, or run the course's notebook and code samples against a live Microsoft Foundry / Azure OpenAI configuration. Covers environment setup (.env, az login, packages), the scripts/validate-notebooks.ps1 runner, interpreting PASS/FAIL results, and which lessons need extra resources (Azure AI Search, GitHub MCP, Foundry Local, Playwright)."
---
# 강의 샘플 테스트

수업 노트북과 코드 샘플이 라이브 Microsoft Foundry / Azure OpenAI 설정에서 실행되는지 검증합니다.
이 저장소에는 모든 Python 노트북을 헤드리스로 실행하고 PASS/FAIL 결과를 출력하는 러너가
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1)에 제공됩니다.


## 사용할 때
- "내 Azure 구독을 기준으로 모든 노트북/샘플을 검증할 때."
- "패키지를 업그레이드하거나 모델을 변경한 후 코스를 스모크 테스트할 때."
- "어떤 강의가 아직 통과/실패하는지 실시간으로 확인할 때."

AI Smoke Test GitHub 작업(배포된 *를 검증하는 작업)에는 **사용하지 마세요**
호스팅된 에이전트 — [`tests/README.md`](../../../tests/README.md) 참조). 이 기능은
노트북을 로컬에서 실행합니다.

## 사전 요구 사항 (먼저 확인)
1. **Python 3.12+** 와 과정 의존성: `python -m pip install -r requirements.txt`
   그리고 실행기: `python -m pip install nbconvert ipykernel`.
2. **저장소 루트의 `.env`** ([`.env.example`](../../../../../.env.example)에서 복사) 다음 항목 최소 포함:
   - `AZURE_AI_PROJECT_ENDPOINT` — Foundry 프로젝트 엔드포인트
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — 사용 중단되지 않은 배포 (예: `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) 및 `AZURE_OPENAI_DEPLOYMENT`
     Azure OpenAI를 직접 호출하는 강의용 (Lesson 06, 02-azure-openai, 14 handoff/human-loop).
3. **`az login`** 완료 — 샘플이 `AzureCliCredential` (Entra ID, 키리스)로 인증됨.
4. 모델 배포가 존재하는지 확인:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## 검증 실행
```powershell
# All Python notebooks (skips .NET, .venv, site-packages, translations, skill assets)
pwsh scripts/validate-notebooks.ps1

# A single lesson, with a longer per-cell timeout
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Just list what would run (no execution)
pwsh scripts/validate-notebooks.ps1 -List

# Explicit interpreter (if `python` is not on PATH, e.g. Windows Store alias)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
스크립트는 실행된 복사본, 노트북별 로그, 그리고 `results.json`를
`$env:TEMP\aiab-nbval` 에 기록하고 실패 횟수와 함께 종료합니다.

일시적 실패(공유 구독 HTTP 429 속도 제한, 가끔 있는
`AzureCliCredential` 토큰 문제 또는 타임아웃)는 자동으로 재시도됩니다.
(`-Retries`, 기본값 2, `-RetryDelaySeconds` 백오프로 기본값 20). 만약
모델 배포가 정기적으로 429 응답을 보낸다면, 구독의 GlobalStandard
TPM 할당량(`az cognitiveservices usage list -l <region>`)을 확인하세요 — 단일
배포 용량을 높이는 것은 <em>구독</em> 할당량이 소진된 경우 도움이 되지 않습니다.

## 결과 해석
- `PASS` — 노트북이 셀 오류 없이 처음부터 끝까지 실행되었습니다.
- `FAIL` — 첫 번째 `*Error` / `*Exception` 줄이 표시됩니다; 전체 추적을 보려면
  출력 디렉터리의 해당하는 `log_*.txt` 를 여세요.
- 단일 노트북 실패는 `-Timeout`(셀당)으로 제한되므로, 중단된
  인간-인터랙티브 셀은 중단되지 않고 `StdinNotImplementedError`로 나타납니다.

## 추가 리소스가 필요한 강의 (리소스 없이는 실패할 것으로 예상)
| 강의 | 추가 요구 사항 |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, 키) — 메모리 내 백업 경로 포함 |
| 11 MCP / GitHub | GitHub MCP 서버 + PAT |
| 13 메모리 (cognee) | 모델 공급자와 구성된 `cognee` |
| 15 브라우저 사용 | Playwright 브라우저 설치됨 (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 로컬 에이전트 | Foundry 로컬 런타임 + 다운로드된 Qwen 모델 (장치 내, 클라우드 없음) |
| `*-dotnet-*` 노트북 | .NET Interactive 커널 (기본 제외; `-IncludeDotnet` 사용) |

## 보고
수업별로 그룹화된 PASS/FAIL 표로 요약합니다. 진짜 퇴보된 사항
(수정해야 할 코드/구성 버그)과 환경 문제 (누락된 Search/Foundry Local/PAT)를 구분하고,
각 실제 실패에 대해 실패한 `log_*.txt`를 인용합니다.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->