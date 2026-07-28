---
name: local-ai-agents
license: MIT
---
# Foundry Local과 Qwen으로 로컬 AI 에이전트 만들기

> [Lesson 17 – 로컬 AI 에이전트 만들기](../../../17-creating-local-ai-agents/README.md)의 동반 스킬입니다.
> 학습자가 자신의 머신에서 독립적으로 추론하고, 도구를 호출하며, 문서를 검색하는 에이전트를 구축하는 데 사용하세요 — 클라우드 추론 없이. 모든 권장 사항은 수업 내용과 실행 가능한 노트북을 기반으로 합니다.
> 
> 

## 트리거

학습자가 다음을 원할 때 이 스킬을 활성화하세요:
- 완전히 **기기 내에서** 에이전트를 실행하여 개인 정보 보호, 비용 절감 또는 오프라인 목적을 달성.
- <strong>Foundry Local</strong>을 사용하여 로컬에서 모델 서비스를 제공하고 OpenAI 호환 엔드포인트로 연결.
- 신뢰할 수 있는 로컬 도구 호출을 위해 **Qwen 함수 호출** 모델 사용.
- **로컬 RAG** (Chroma) 또는 **로컬 MCP 서버** 추가.
- <strong>하이브리드</strong> 로컬/클라우드 라우팅 전략 설계.

## 핵심 사고 모델

SLM은 개인 정보 보호, 비용, 오프라인 운영을 위해 범위를 줄입니다. 성공 전략은: **SLM이 오케스트레이션하고 도구가 무거운 작업을 맡도록 하는 것.** 모델이 코드베이스를 <em>알 필요</em>는 없으며 — 대신 `read_file`과 `search_docs`를 언제 호출할지 알아야 합니다. 이는 도구 선택과 같은 제한된 결정에는 SLM이 강하지만, 광범위한 지식이나 긴 다중 단계 추론에는 약한 점을 이용하는 것입니다.






## 왜 이 특정 구성 요소들인가

- <strong>Foundry Local</strong>은 <strong>OpenAI 호환 HTTP 엔드포인트</strong>를 노출하므로 클라우드 에이전트 코드를 `base_url`만 바꾸고 로컬 플레이스홀더 API 키를 사용해도 이전할 수 있습니다. 또한 머신에 최적화된 빌드(CPU/GPU/NPU)를 자동 선택합니다.
- **Qwen** 모델은 함수 호출을 위해 훈련되었으며 일관되게 형식에 맞는 도구 호출을 생성합니다 — 로컬 <em>챗</em> 모델을 로컬 <em>에이전트</em>로 만드는 핵심입니다.
- <strong>Chroma</strong>는 프로세스 내에서 실행되며 벡터를 디스크에 저장하므로 전체 RAG 파이프라인(임베드 → 저장 → 검색 → 추론)이 로컬에 머무릅니다.
- <strong>MCP</strong>는 클라우드 서비스가 아니라 전송 계층입니다: MCP 서버는 `stdio`를 통해 로컬에서 실행할 수 있습니다.

## 설치 필수 요소

```bash
foundry model run qwen2.5-7b-instruct
foundry service status
```

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager("qwen2.5-7b-instruct")
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)  # 로컬 자리 표시자
```

약 8GB RAM이 현실적인 최소 사양이며 GPU/NPU가 있으면 도움이 되나 필수는 아닙니다.

## 재현할 주요 패턴

학습자에게 다음 노트북을 안내하세요
[`17-local-agent-foundry-local.ipynb`](../../../17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb):

- **샌드박스화된 도구**: 모든 파일 도구는 경로를 해석하고 단일 프로젝트 루트 외부는 거부 — 로컬이어도 도구 실행 시 사용자의 권한만 사용합니다.
- **도구 호출 루프**: OpenAI 도구 스키마에 도구 등록, 요청된 도구 로컬 실행, 결과 반환, 최종 답변까지 반복.
- **로컬 RAG**: 문서를 Chroma 컬렉션에 업서트; `search_docs`는 상위 k개 청크를 반환.
- **로컬 MCP**: `stdio`로 로컬 서버에 연결; 프로젝트 디렉토리에 범위를 설정하고 출력 유효성 검사.

## 하이브리드 라우팅 (모델 중 하나로서 로컬)

| 상황 | 실행 위치 |
|-----------|---------------|
| 민감한 데이터 / 오프라인 | 로컬 SLM |
| 단순하고 제한된 작업 | 로컬 SLM (저렴하고 빠름) |
| 비민감 데이터에 대한 복잡한 다중 단계 추론 | 클라우드 모델 |
| 클라우드 장애 | 로컬 SLM (점진적 성능 저하) |

이는 Lesson 16의 모델 라우팅 아이디어를 반영하며 워크스테이션을 하나의 경로로 활용합니다. 에이전트가 완전히 실패하지 않고 품질이 저하되는 방향으로 로컬 fallback을 선호하세요.



## 어시스턴트를 위한 가드레일

- 모든 파일/도구 작업을 샌드박스화된 프로젝트 디렉토리 내로 제한하세요.
- 학습자의 명시적 목표가 개인 정보 보호/오프라인일 때는 코드나 데이터를 클라우드로 전송하지 마세요 — 전체 파이프라인을 로컬에 유지하세요.
- SLM 품질에 대해 현실적인 기대를 설정하고, 모델의 암기 지식보다는 도구와 RAG에 의존하세요.
- Lesson 17에는 **Foundry Responses 엔드포인트가 없으므로**, 클라우드 스모크 테스트 액션은 적용되지 않습니다 — 노트북을 로컬에서 실행해 검증하세요.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->