# 한국어 용어 기준서 (Korean Glossary)

이 문서는 [translations/ko](./README.md) 하위 문서에서 공통으로 사용하는 용어 기준입니다.

목표:
- 한국어 번역 문서의 용어 일관성 유지
- 리뷰 시 확인 가능한 단일 기준 제공
- Microsoft Learn 공식 표기와 프로젝트 현행 사용을 함께 반영

## 적용 범위

- 대상: `translations/ko/**/*.md`
- 제외: 원문(루트 영문 문서), 타 언어 번역 폴더

## 기준 원칙

1. 공식 용어는 Microsoft Learn 한국어 문서 표기를 우선합니다.
2. Learn이 복수 표현을 사용하는 경우, ko 폴더 현행 사용량이 높은 표현을 권장 표기로 채택합니다.
3. 고유 제품명은 번역하지 않습니다.
4. 동일 문서 내에서는 같은 개념을 하나의 표기로 유지합니다.
5. 본 기준서와 본문이 충돌하면, 기준서 업데이트 PR에서 근거(링크/검색 결과)를 먼저 제시합니다.

## Learn 공식 용어 근거

아래 문서에서 직접 확인한 표기를 기준으로 삼습니다.

1. Agent Framework 오케스트레이션: 다중 에이전트, Handoff(핸드오프), 휴먼 인 더 루프
- https://learn.microsoft.com/ko-kr/agent-framework/workflows/orchestrations/
2. Agent Framework HITL: HITL(휴먼 인 더 루프), 도구 승인, 승인 필수 도구
- https://learn.microsoft.com/ko-kr/agent-framework/workflows/human-in-the-loop
3. Foundry Observability: 관찰 가능성(문서 제목), 관찰성(개념 정의), 가시성(설명 문맥)
- https://learn.microsoft.com/ko-kr/azure/foundry/concepts/observability
4. Agent Framework 개요: 다중 에이전트, 워크플로
- https://learn.microsoft.com/ko-kr/agent-framework/overview/

## ko 폴더 현황 스냅샷 (2026-06-18)

`GLOSSARY_KO.md` 제외 집계:

- 다중 에이전트: 71
- 멀티 에이전트: 0
- 설계 패턴: 58
- 디자인 패턴: 0
- 관찰 가능성: 21
- 관찰성: 0
- 가시성: 5
- 휴먼 인 더 루프: 6
- HITL: 0

## 표준 용어

| 개념 | 권장 표기 | 허용 표기 | 지양 표기 | 근거 |
|---|---|---|---|---|
| Multi-agent | 다중 에이전트 | - | 멀티 에이전트 | Learn 오케스트레이션/개요 + ko 현행 |
| Multi-agent system | 다중 에이전트 시스템 | MAS(병기) | 멀티 에이전트 시스템 | Learn 다중 에이전트 맥락 |
| Design pattern | 설계 패턴 | - | 디자인 패턴 | ko 현행 일관화 |
| Observability | 관찰 가능성 | 관찰성(Learn 원문 인용 시) | 가시성 단독 고정 | Learn 관찰 가능성/관찰성 병행 |
| Visibility | 가시성 | - | 관찰 가능성과 무분별 혼용 | Learn 설명 문맥 |
| Human-in-the-loop | 휴먼 인 더 루프 | HITL(휴먼 인 더 루프) | 인간 개입 단독 고정 | Learn HITL 문서 |
| Handoff | 핸드오프 | Handoff(핸드오프) | 인계 | Learn 오케스트레이션 |
| Group chat pattern | 그룹 채팅 | Group Chat(그룹 채팅) | 단체 채팅 | Learn 오케스트레이션 |
| Coordination | 조정 | 조율 | 협업으로 고정 대체 | 문맥 의존 |
| Workflow | 워크플로 | 워크플로우 | 작업 흐름(기술 용어 대체) | Learn 개요/오케스트레이션 |
| Agent Framework | Agent Framework | 에이전트 프레임워크(설명 문맥) | 약어만 단독 표기 | 제품명 원문 유지 |
| Tool approval | 도구 승인 | 승인 필수 도구 | 툴 승인 혼용 | Learn HITL 문서 |
| Orchestration | 오케스트레이션 | 조정(설명 문맥) | 오케스트레이터와 혼용 | Learn 오케스트레이션 문서 |
| Sequential | 순차 | 순차 실행 | 직렬(혼용) | Learn 오케스트레이션 패턴 |
| Concurrent | 동시 | 동시 실행 | 병렬(개념 혼용) | Learn 오케스트레이션 패턴 |
| Parallel | 병렬 | 병렬 실행 | 동시와 무분별 치환 | 문맥 구분(실행 방식) |
| Routing | 라우팅 | 경로 지정(설명 문맥) | 라우트(동사/명사 혼용) | ko 현행 사용 |
| Session | 세션 | 대화 세션 | 회차 | Learn/ko 공통 |
| Middleware | 미들웨어 | - | 중간 소프트웨어 | Learn/ko 공통 |
| Tracing | 추적 | 트레이싱 | 추척(오탈자) | Learn Observability |
| Monitoring | 모니터링 | 감시(일반 문맥) | 관제(기술 문맥 대체) | Learn Observability |
| Evaluation | 평가 | - | 성능 측정(개념 축소) | Learn Observability |
| Checkpoint | 검사점 | 체크포인트 | 포인트 저장 | Learn HITL/Workflows |
| RAG | RAG(검색 증강 생성) | 검색 증강 생성(RAG) | RAG만 반복(최초 정의 없음) | Learn/프로젝트 관행 |
| MCP server | MCP 서버 | 모델 컨텍스트 프로토콜 서버 | MCP 툴(개념 혼용) | Learn/프로젝트 공통 |
| A2A protocol | A2A 프로토콜 | Agent-to-Agent(A2A) 프로토콜 | A2A만 단독 고정 | Learn/프로젝트 공통 |
| Agent service | 에이전트 서비스 | Microsoft Foundry 에이전트 서비스 | 에이전트 런타임(개념 혼용) | Learn Foundry |
| Knowledge base | 지식 베이스 | 지식 기반(설명 문맥) | 지식창고 | ko 현행 사용 |

## 문서 작성 예시

- 권장: `다중 에이전트 오케스트레이션에서는 관찰 가능성이 중요합니다.`
- 권장: `휴먼 인 더 루프(HITL) 시나리오에서 도구 승인을 사용합니다.`
- 허용: `관찰 가능성(관찰성)`
- 지양: `멀티/다중 에이전트`, `디자인/설계 패턴` 혼용

## 리뷰 체크리스트

PR 리뷰 시 아래를 확인합니다.

- `다중 에이전트`와 `멀티 에이전트`가 혼용되지 않았는가?
- `설계 패턴`과 `디자인 패턴`이 혼용되지 않았는가?
- `관찰 가능성`/`관찰성`/`가시성`이 문맥에 맞게 사용되었는가?
- `휴먼 인 더 루프`는 필요 시 `HITL` 병기 규칙을 따르는가?
- `워크플로`/`워크플로우`, `순차`/`동시`/`병렬` 용어를 문맥에 맞게 구분했는가?
- `오케스트레이션`, `라우팅`, `세션`, `미들웨어` 핵심 용어 표기를 유지했는가?
- 제품명(예: Agent Framework, Microsoft Foundry)은 임의 번역하지 않았는가?

## 빠른 점검 쿼리

VS Code 검색(정규식) 예시:

- `(멀티 에이전트|다중 에이전트)`
- `(디자인 패턴|설계 패턴)`
- `(관찰 가능성|관찰성|가시성)`
- `(휴먼 인 더 루프|HITL|인간 개입)`
- `(워크플로우|워크플로)`
- `(체크포인트|검사점)`
- `(순차|동시|병렬)`

## 변경 절차

1. 이 문서 수정 PR 생성
2. Learn 링크 또는 ko 검색 결과를 근거로 첨부
3. 변경 이유와 영향 문서 명시
4. 합의 후 관련 문서 반영
5. 필요 시 [translations/ko/README.md](./README.md)에 공지 갱신

## 버전

- v1.2 (2026-06-18): 표준 용어 항목 확장(오케스트레이션, 순차/동시/병렬, 세션, 미들웨어, 추적/모니터링/평가, 검사점, RAG, MCP, A2A 등)
- v1.1 (2026-06-18): ko 전체 점검 결과와 Learn 공식 용어 근거 반영
- v1.0 (2026-06-18): 최초 기준서 작성
