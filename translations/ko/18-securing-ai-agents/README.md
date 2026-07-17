[수업 영상 보기: 암호화된 영수증으로 AI 에이전트 보안 강화하기](https://youtu.be/PLACEHOLDER_VIDEO_ID)

> _(수업 영상 및 썸네일은 병합 후 Microsoft 콘텐츠 팀에서 추가할 예정이며, 14/15강 패턴에 맞추어집니다.)_

# 암호화된 영수증으로 AI 에이전트 보안 강화하기

## 소개

이 수업에서 다룰 내용:

- AI 에이전트의 감사 추적이 컴플라이언스, 디버깅 및 신뢰에 왜 중요한지.
- 암호화 영수증이 무엇이며 서명되지 않은 로그 라인과 어떻게 다른지.
- 순수 Python으로 에이전트의 툴 호출에 서명된 영수증을 생성하는 방법.
- 오프라인에서 영수증을 검증하고 변조를 감지하는 방법.
- 영수증을 체인으로 연결하여 하나를 제거하거나 재정렬하면 체인이 깨지는 방식.
- 영수증이 증명하는 것과 명확히 증명하지 않는 것.

## 학습 목표

이 수업을 완료하면 다음을 알 수 있습니다:

- 에이전트 동작에 대한 암호학적 출처 증명을 요구하는 실패 모드를 식별하기.
- 표준 JSON 페이로드에 대해 Ed25519 서명 영수증을 생성하기.
- 서명자의 공개 키만으로 독립적으로 영수증을 검증하기.
- 수정된 영수증에 대해 재검증을 실행하여 변조를 감지하기.
- 해시 체인된 영수증 시퀀스를 구축하고 체인이 중요한 이유를 설명하기.
- 영수증이 증명하는 것(귀속, 무결성, 순서)과 증명하지 않는 것(행동의 올바름, 정책 타당성) 사이 경계를 인식하기.

## 문제: 당신 에이전트의 감사 추적

Contoso Travel용 AI 에이전트를 배포했다고 상상해 보세요. 이 에이전트는 고객 요청을 읽고, 항공편 API를 호출하여 옵션을 조회하고, 고객을 대신해 좌석을 예약합니다. 지난 분기에 에이전트는 50,000건의 예약을 처리했습니다.

오늘, 감사인이 찾아옵니다. 그들은 간단한 질문을 합니다: "당신의 에이전트가 한 일을 보여 주세요."

당신은 로그 파일을 건네줍니다. 감사인은 로그를 보고 더 어려운 질문을 합니다: "이 로그가 편집되지 않았다는 걸 어떻게 알죠?"

이것이 감사 추적 문제입니다. 오늘날 대부분의 에이전트 배포는 다음에 의존합니다:

- **애플리케이션 로그**: 에이전트가 직접 작성하며, 파일 시스템 접근 권한이 있는 누구나 수정 가능.
- **클라우드 로깅 서비스**: 플랫폼 수준에서 변조 감지 가능하지만 감사인이 플랫폼 운영자를 신뢰해야 함.
- **데이터베이스 트랜잭션 로그**: 데이터베이스 변경에는 적합하지만 임의 도구 호출 기록으로는 부적합.

이들은 모두 감사인이 누군가(당신, 클라우드 제공자, 데이터베이스 공급자)를 신뢰하지 않고는 질문에 답할 수 없습니다. 내부 용도로는 흔히 신뢰가 가능하지만, 규제 대상 작업(금융, 의료, EU AI 법령 적용 대상 등)에는 적합하지 않습니다.

암호화된 영수증은 각 에이전트 동작을 독립적으로 검증 가능하도록 하여 이 문제를 해결합니다. 감사인은 당신을 신뢰할 필요 없이 공개 키와 영수증만 있으면 됩니다.

## 암호화된 영수증이란?

영수증은 에이전트가 수행한 작업을 기록한 JSON 객체로, 디지털 서명으로 서명되어 있습니다.

```mermaid
flowchart LR
    A[에이전트가 도구를 호출함] --> B[영수증 페이로드 생성]
    B --> C[JSON RFC 8785 정규화]
    C --> D[SHA-256 해시]
    D --> E[Ed25519 서명]
    E --> F[서명된 영수증]
    F --> G[감사자가 오프라인 검증]
    G --> H{서명 유효한가?}
    H -- yes --> I[변조 방지 증거]
    H -- no --> J[영수증 거부됨]
```
  
간단한 영수증은 다음과 같습니다:

```json
{
  "type": "agent.tool_call.v1",
  "agent_id": "contoso-travel-bot",
  "tool_name": "lookup_flights",
  "tool_args_hash": "sha256:a3f9c1...",
  "result_hash": "sha256:7b2e1d...",
  "policy_id": "contoso-travel-policy-v3",
  "timestamp": "2026-04-25T14:30:00Z",
  "sequence": 47,
  "previous_receipt_hash": "sha256:9d4e6a...",
  "signature": {
    "alg": "EdDSA",
    "sig": "c5af83...",
    "public_key": "8f3b2c..."
  }
}
```
  
세 가지 속성이 핵심 역할을 합니다:

1. <strong>서명</strong>: 영수증은 에이전트 게이트웨이가 Ed25519 비밀 키로 서명합니다. 대응하는 공개 키를 가진 누구나 오프라인에서 서명을 검증할 수 있습니다. 어떤 필드라도 변조하면 서명이 무효가 됩니다.

2. **정규 인코딩**: 서명 전에 영수증은 JSON Canonicalization Scheme (JCS, RFC 8785)으로 직렬화됩니다. 이는 두 구현체가 동일한 논리적 영수증을 생성하면 바이트가 완전히 동일하도록 보장합니다. 정규화 없이는 서로 다른 JSON 직렬화기가 같은 내용에 대해 서로 다른 서명을 만듭니다.

3. **해시 체이닝**: `previous_receipt_hash` 필드는 각 영수증을 이전 영수증에 연결합니다. 하나의 영수증을 제거하거나 순서를 바꾸면 이후 모든 영수증이 손상됩니다. 서명이 우회되어도 체인 수준에서 변조가 보입니다.

이 세 속성은 다음 세 가지 보장을 제공합니다:

- <strong>귀속</strong>: 이 키가 이 내용을 서명했다.
- <strong>무결성</strong>: 서명 이후 내용이 바뀌지 않았다.
- <strong>순서</strong>: 이 영수증은 체인에서 저 영수증 다음에 있다.

## Python에서 영수증 생성하기

영수증 생성에 특수 라이브러리는 필요 없습니다. 암호학적 원시 기능은 널리 제공되며, 로직도 수십 줄의 Python 코드입니다.

`code_samples/18-signed-receipts.ipynb` 노트북의 실습에서는 전체 과정을 단계별로 안내합니다. 요약 버전:

```python
import json
import hashlib
import base64
from nacl import signing
from jcs import canonicalize  # RFC 8785 표준 JSON

def b64url_nopad(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode("ascii").rstrip("=")

def sha256_canonical(obj) -> str:
    """SHA-256 of a Python object's JCS-canonical JSON form."""
    return f"sha256:{hashlib.sha256(canonicalize(obj)).hexdigest()}"

# 서명 키 생성 또는 로드 (운영 환경에서는 키 볼트에 저장)
signing_key = signing.SigningKey.generate()
verify_key = signing_key.verify_key

# 영수증 페이로드 구성 (아직 서명 없음)
tool_args = {"origin": "SYD", "destination": "LAX"}
tool_result = [{"flight": "QF11", "price": 1850, "stops": 0}]

payload = {
    "type": "agent.tool_call.v1",
    "agent_id": "contoso-travel-bot",
    "tool_name": "lookup_flights",
    "tool_args_hash": sha256_canonical(tool_args),
    "result_hash": sha256_canonical(tool_result),
    "policy_id": "contoso-travel-policy-v3",
    "timestamp": "2026-04-25T14:30:00Z",
    "sequence": 0,
    "previous_receipt_hash": None,
}

# 정규화, 해시, 서명.
canonical_bytes = canonicalize(payload)
message_hash = hashlib.sha256(canonical_bytes).digest()
signature_bytes = signing_key.sign(message_hash).signature

# 구조화된 서명 객체 첨부.
receipt = {
    **payload,
    "signature": {
        "alg": "EdDSA",
        "sig": b64url_nopad(signature_bytes),
        "public_key": b64url_nopad(bytes(verify_key)),
    },
}
```
  
이것이 서명 파이프라인의 전부입니다. 노트북 실습이 각 단계를 상세히 다룹니다.

## 영수증 검증과 변조 감지

검증은 반대 과정입니다:

```python
import base64
import hashlib
from nacl import signing
from nacl.exceptions import BadSignatureError
from jcs import canonicalize

def b64url_decode(s: str) -> bytes:
    padding = "=" * ((4 - len(s) % 4) % 4)
    return base64.urlsafe_b64decode(s + padding)

def verify_receipt(receipt: dict) -> bool:
    # 서명은 구조화된 객체입니다: {"alg", "sig", "public_key"}.
    sig_obj = receipt.get("signature")
    if not sig_obj or sig_obj.get("alg") != "EdDSA":
        return False

    # 실제로 서명된 페이로드를 재구성합니다 (서명을 제외한 모든 것).
    payload = {k: v for k, v in receipt.items() if k != "signature"}

    canonical_bytes = canonicalize(payload)
    message_hash = hashlib.sha256(canonical_bytes).digest()

    try:
        verify_key = signing.VerifyKey(b64url_decode(sig_obj["public_key"]))
        verify_key.verify(message_hash, b64url_decode(sig_obj["sig"]))
        return True
    except BadSignatureError:
        return False
```
  
이 함수는 영수증을 받아 서명이 유효하면 `True`, 아니면 `False`를 반환합니다. 네트워크 호출, 서비스 의존, 제3자 신뢰가 전혀 필요 없습니다.

변조 감지 시연은 노트북에서 다음을 다룹니다:

1. 유효한 영수증 생성 및 성공적으로 검증 확인.
2. `tool_args_hash` 필드의 1바이트를 수정.
3. 다시 검증 실행 후 실패 확인.

이것은 영수증이 변조 감지 기능을 갖췄음을 보여주는 실용적 시연입니다: 아주 작은 수정도 서명을 망가뜨립니다.

## 다단계 에이전트를 위한 영수증 체인 만들기

단일 서명 영수증은 한 동작을 보호합니다. 영수증 체인은 시퀀스를 보호합니다.

```mermaid
flowchart LR
    R0[영수증 0<br/>제네시스] --> R1[영수증 1]
    R1 --> R2[영수증 2]
    R2 --> R3[영수증 3]
    R1 -. previous_receipt_hash .-> R0
    R2 -. previous_receipt_hash .-> R1
    R3 -. previous_receipt_hash .-> R2
```
  
각 영수증은 이전 영수증의 해시를 기록합니다. 체인 중간의 영수증 2를 조용히 제거하려면 공격자는:

- 영수증 3의 `previous_receipt_hash` 필드를 수정(영수증 3의 서명 무효), 또는
- 수정된 영수증 3에 새 서명을 위조(에이전트 비밀 키 필요)

하드웨어 키 보관소에 비밀 키가 있고 각 영수증에 공개 키를 발행하면 어느 쪽 공격도 탐지 없이 불가능합니다.

노트북은 다음을 안내합니다:

1. 3개 영수증 체인 구축.
2. 각 영수증의 `previous_receipt_hash`가 실제 이전 영수증 해시와 일치하는지 검증.
3. 중간 영수증 변조 후 체인이 정확히 그 지점에서 끊김을 확인.

이것이 외부 감사인이 당신을 신뢰하지 않고도 검증 가능한 감사 추적을 만드는 방법입니다.

## 영수증이 증명하는 것(그리고 증명하지 않는 것)

이 섹션은 이 수업의 가장 중요한 부분입니다. 영수증은 강력하지만 그 한계가 분명합니다.

**영수증이 증명하는 세 가지:**

1. <strong>귀속</strong>: 특정 키가 특정 페이로드를 서명했다.
2. <strong>무결성</strong>: 서명 이후 페이로드가 변하지 않았다.
3. <strong>순서</strong>: 이 영수증이 체인에서 저 영수증 다음이다.

**영수증이 증명하지 않는 것:**

1. <strong>정확성</strong>: 에이전트 동작이 올바른 행동이었다는 것. 잘못된 답안도 똑같이 서명 가능.
2. **정책 준수**: `policy_id`에 참조된 정책이 실제로 평가되었거나, 평가 시 이 동작을 허용했을지 여부. 영수증은 주장된 내용을 기록할 뿐, 시행된 내용은 아님.
3. **키 이상의 신원**: 영수증은 "이 키가 이 내용을 서명했다"고 말할 뿐 "이 사람이 승인했다"고 말하지 않음. 키와 사람/조직 연결은 별도의 신원 인프라 필요(디렉터리, 공개 키 등록소 등).
4. **입력의 진실성**: 에이전트가 조작된 프롬프트를 받아 행동해도, 영수증은 행동을 충실히 기록. 영수증은 입력 검증의 대체물이 아님.

이 경계가 중요한 두 가지 이유:

- 영수증이 유용한 용도: 조직 경계를 넘어 에이전트 행동의 감사 가능성 및 변조 감지를 제공.
- 추가적으로 필요한 층: 입력 검증(6강), 정책 시행(아래 간단히 소개), 신원 인프라(이 수업은 범위 밖).

흔한 실수는 "영수증이 있으니 통제되고 있다"고 착각하는 것. 그렇지 않습니다. 영수증은 기반일 뿐, 통제 시스템은 그 위에 구축하는 것입니다.

## 운영 참조

이 수업의 Python 코드는 의도적으로 최소한으로 작성되어 정확히 무슨 일이 일어나는지 읽고 이해하기 쉽습니다. 운영 환경에서는 두 가지 옵션이 있습니다:

1. **암호학 원시 기능을 직접 사용**: 위의 50줄 코드는 많은 사용 사례에 충분합니다. PyNaCl (Ed25519)과 `jcs` 패키지(정규 JSON)는 잘 유지·감사된 라이브러리입니다.

2. **운영용 영수증 라이브러리 사용**: 몇몇 오픈소스 프로젝트는 추가 기능(키 교체, 배치 검증, JWK 세트 배포, 정책 엔진 통합)을 갖춘 동일 패턴 구현:
   - 본 수업의 영수증 포맷은 표준화 과정 중인 IETF 인터넷 초안(`draft-farley-acta-signed-receipts`)에 따름.
   - Microsoft Agent Governance Toolkit은 Cedar 기반 정책 결정과 영수증을 결합; 해당 저장소의 튜토리얼 33에서 end-to-end 예제 참조.
   - `protect-mcp`(npm) 및 `@veritasacta/verify`(npm) 패키지는 영수증 서명과 오프라인 검증을 위한 Node 기반 구현 제공, 임의 MCP 서버를 변조 감지 감사 추적으로 포장 가능.
   - **[nobulex](https://github.com/arian-gogani/nobulex)** Python SDK(`pip install nobulex`)는 LangChain 및 CrewAI 통합, 교차 검증 테스트 벡터와 [OWASP PR #2210](https://github.com/OWASP/CheatSheetSeries/pull/2210)을 통한 규정 준수 매핑 포함 Ed25519 + JCS 서명 패턴 구현.

자체 구현과 라이브러리 사용 결정은 직접 JWT 라이브러리 작성과 검증된 라이브러리 사용 결정과 유사: 두 가지 모두 합리적, 라이브러리는 시간 절약 및 감사지면 축소, 직접 구현은 모든 원시 기능 이해 강제. 이 수업은 직접 구현 방식을 가르쳐 두 가지 선택 모두에 기초를 마련합니다.

## 지식 점검

실습 전에 이해도를 테스트하세요.

**1. 영수증은 에이전트 개인 Ed25519 키로 서명됩니다. 감사인은 공개 키만 가집니다. 감사인은 오프라인에서 영수증을 검증할 수 있나요?**

<details>
<summary>답변</summary>

네. Ed25519 검증은 공개 키와 서명된 바이트만 필요합니다. 네트워크 호출, 서비스 의존 없음. 이 특성 덕분에 영수증은 네트워크 연결이 없는 환경, 다기관, 낮은 신뢰감시 감사 환경에서 유용합니다.
</details>

**2. 공격자가 영수증의 `policy_id` 필드를 더 관대한 정책으로 수정했습니다. 서명은 원본 페이로드에 대한 것이었습니다. 검증 시 어떻게 되나요?**

<details>
<summary>답변</summary>

검증 실패합니다. 서명은 원본 페이로드의 정규화된 바이트에 대해 계산되었으며, 어떤 필드라도 변경하면 정규화된 바이트가 바뀌고 SHA-256 해시가 바뀌며 서명이 무효가 됩니다. 공격자는 새 유효 서명을 만들기 위해 비밀 키가 필요하지만, 그들이 갖고 있지 않습니다.
</details>

**3. 왜 영수증에 원본 인자와 결과 대신 `tool_args_hash` 및 `result_hash`가 포함되나요?**

<details>
<summary>답변</summary>

두 가지 이유입니다. 첫째, 영수증은 개인정보나 업무 데이터 등 원본 내용을 노출하면 안 되는 환경에서 보관 또는 전송될 수 있습니다. 해시를 사용하면 영수증 크기가 작고 내용이 비공개로 유지되며, 감사인은 해시가 실제 별도 저장된 내용과 일치하는지 검증합니다. 둘째, 해시는 고정 크기이며, 해시 사용으로 입력·출력 크기와 관계없이 영수증 크기를 제한할 수 있습니다.
</details>

**4. `previous_receipt_hash` 필드는 각 영수증을 바로 이전 영수증에 연결합니다. 공격자가 체인 중간에서 영수증 하나를 몰래 삭제하면 무엇이 무효가 되나요?**

<details>
<summary>답변</summary>

삭제된 영수증 뒤에 오는 모든 영수증이 무효가 됩니다. 그들의 `previous_receipt_hash` 필드가 실제 체인과 일치하지 않습니다(참조 대상 영수증이 없거나 체인이 다른 선행 영수증을 가리키므로). 삭제를 숨기려면 공격자가 이후 모든 영수증을 다시 서명해야 하는데, 비밀 키가 필요합니다.
</details>

**5. 영수증이 정상적으로 검증됩니다. 이것이 에이전트 동작이 올바르고 정책에 부합했다는 것을 증명할까요?**

<details>
<summary>답변</summary>

아니요. 유효한 영수증은 세 가지를 증명합니다: 귀속(이 키가 이 내용을 서명), 무결성(내용이 변경되지 않음), 순서(이 영수증이 저 영수증 다음). 에이전트 행동이 정확하거나 `policy_id`에 명시된 정책이 실제 평가되었거나 에이전트가 규칙을 모두 따랐다는 증명은 아닙니다. 영수증은 에이전트 행동 감사 가능성을 제공할 뿐, 올바름을 보장하지 않습니다. 이 점이 이 수업에서 가장 중요한 경계입니다.
</details>

## 실습 과제

`code_samples/18-signed-receipts.ipynb`를 열고 네 섹션을 모두 완료하세요:

1. **섹션 1**: 첫 영수증에 서명하고 검증하기.
2. **섹션 2**: 영수증을 변조하고 검증 실패 관찰하기.
3. **섹션 3**: 세 개 영수증 체인 구축 및 체인 무결성 검증하기.
4. **섹션 4**: Microsoft Agent Framework로 구축한 에이전트에 패턴 적용: 툴 호출을 영수증 서명으로 래핑하고 영수증을 독립적으로 검증하기.
**확장 과제 1:** 영수증 스키마에 직접 선택한 추가 필드(예: 추적용 요청 ID)를 확장하고, 해당 필드를 포함하도록 정식 서명 로직을 업데이트한 뒤, 영수증이 검증을 거쳐도 정상적으로 순환하는지 확인하세요. 그런 다음 서명 후 필드를 수정하고 검증이 실패하는지 확인하세요. 이를 통해 정식 인코딩의 각 바이트가 서명에 어떻게 기여하는지 이해하게 됩니다.

**확장 과제 2:** 두 개의 영수증을 SHA-256으로 해시(정식 바이트를 결정적인 순서로 연결)한 다음, 결과 요약을 서명 전에 세 번째 영수증의 새 필드에 삽입하세요. 세 개의 영수증 모두 정상적으로 순환하는지 검증하세요. 이렇게 하면 세 번째 영수증을 가진 누구나 첫 번째 두 영수증이 서명 시점에 존재했음을 내용 공개 없이 증명할 수 있는 한 단계 포함 증명을 구축한 셈입니다. 이것이 대규모 선택적 공개 영수증에서 사용하는 패턴입니다(머클 커밋먼트, RFC 6962).

## 결론

암호화 영수증은 AI 에이전트에 다음과 같은 감사 추적을 제공합니다:

- **독립적 검증 가능:** 공개 키를 가진 누구나 검증할 수 있으며 서비스 의존도가 없습니다.
- **변조 감지:** 어떤 수정이라도 서명을 무효화합니다.
- **이식성:** 영수증은 작은 JSON 파일로 어디서든 보관, 전송, 검증할 수 있습니다.
- **표준 준수:** Ed25519(RFC 8032), JCS(RFC 8785), SHA-256 등 널리 배포된 기본 원칙에 기반합니다.

입력 검증, 정책 집행, 신원 인프라를 대체하지는 않습니다. 이들은 해당 레이어를 위한 기초입니다. 규제된 작업, 다중 조직 워크플로우, 미래의 감사자가 신뢰할 수 없을 상황에 에이전트를 배포할 때, 영수증이 감사 추적을 정직하게 만드는 방법입니다.

가장 중요한 요점: 영수증은 누가 언제 무엇을 말했는지를 증명합니다. 말한 내용이 진실이거나 옳다는 것을 증명하지는 않습니다. 이 차이를 명확히 유지하세요. 이는 정직한 출처 시스템과 오도하는 시스템의 차이입니다.

## 운영 시 체크리스트

이 수업을 마치고 실제 환경에 영수증 서명 에이전트를 배포할 준비가 되면:

- [ ] **서명 키를 개발자 노트북에서 분리하세요.** Azure Key Vault, AWS KMS, 또는 하드웨어 보안 모듈을 사용하세요. 영수증 서명에 사용하는 비공개 키는 절대 소스 코드 저장소나 일반 텍스트로 된 애플리케이션 머신에 있어서는 안 됩니다.
- [ ] **검증용 공개 키를 공개하세요.** 감사자는 오프라인에서 검증에 필요합니다. 표준 패턴은 잘 알려진 URL(RFC 7517)의 JWK 세트입니다. 예: `https://your-org.example.com/.well-known/agent-keys.json`.
- [ ] **체인을 외부에 앵커하세요.** 최신 체인 헤드 해시를 정기적으로 투명성 로그(Sigstore Rekor, RFC 3161 타임스탬프 기관, 또는 내부 시스템에 기록)하여 제3자가 "이 체인이 해당 시점에 존재했다"는 것을 확인할 수 있게 하세요.
- [ ] **영수증을 불변으로 저장하세요.** 추가 전용 블롭 스토리지(Azure Storage 불변 정책, AWS S3 객체 잠금 등)를 사용하면 내부자가 스토리지 단계에서 기록을 다시 쓰는 것을 방지할 수 있습니다.
- [ ] **보관 기간을 결정하세요.** 다수의 컴플라이언스 정책이 여러 해 보관을 요구합니다. 영수증 증가를 계획하세요(영수증 하나에 약 500바이트, 에이전트가 하루 10,000번 호출하면 연간 약 1.8 GB 발생).
- [ ] **영수증이 다루지 않는 항목을 문서화하세요.** 영수증은 귀속, 무결성, 순서를 증명합니다. 운영 매뉴얼에는 추가적인 제어(입력 검증, 정책 집행, 속도 제한, 신원 인프라)가 거버넌스 체계에서 영수증과 함께 어떻게 작동하는지 명시해야 합니다.

### AI 에이전트 보안에 관해 더 궁금한 점이 있나요?

[Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)에 참여해 다른 학습자와 만나고, 오피스 아워에 참석하고, AI 에이전트 질문에 답변을 받아보세요.

## 이 수업을 넘어서

이 수업은 단일 영수증 서명과 해시 체인 시퀀스를 다룹니다. 동일한 기본 원칙으로 더 고급 패턴을 구성할 수 있으며, 거버넌스 체계가 성숙해질수록 접하게 될 것입니다:

- **선택적 공개.** 영수증 필드가 독립적으로 커밋(RFC 6962 스타일 머클 트리)되면 특정 감사자에게 특정 필드만 공개하고 나머지는 변경되지 않았음을 증명할 수 있습니다. 전체 감사(완전성을 원하는)와 GDPR과 같은 데이터 최소화 규정을 동시에 충족해야 할 때 유용합니다.
- **영수증 폐기.** 서명 키가 유출되면 해당 키로 서명된 모든 영수증을 특정 시점 이후부터 신뢰할 수 없다고 표시해야 합니다. 표준 패턴: 단기 서명 키와 공개 폐기 목록, 또는 폐기 항목 포함 투명성 로그.
- **양자/분할 서명 영수증.** 일부 구현체는 서명된 페이로드를 실행 전(`authorization_*`)과 실행 후(`result_*`) 절반으로 나누어 독립 서명을 수행합니다. 승인 결정과 관찰된 결과가 다른 주체 또는 시간에 발생할 때 유용합니다. 이 패턴은 본 수업에서 배운 영수증 포맷 위에 추가로 적용됩니다.
- **페이로드 구성.** 영수증은 `result_hash`에 넣은 바이트를 봉인합니다. 실제 페이로드는 도구 호출 결과 하나보다 더 풍부할 수 있습니다: 사전 결정 추론(모델 예측, 고려 옵션, 증거 및 그 완전성, 위험 태세, 책임 사슬, 게이트 결과) 등도 페이로드에 포함되어 단일 영수증으로 봉인할 수 있습니다. 이렇게 하면 영수증 포맷은 최소화하면서 도메인별 페이로드 스키마를 진화시킬 수 있습니다.
- **다중 구현체 간 호환성.** 동일한 영수증 포맷을 여러 독립 구현체(Python, TypeScript, Rust, Go)가 공유 테스트 벡터로 교차 검증합니다. 자체 구현체를 만들면 공개된 벡터 검증으로 호환성을 확신할 수 있습니다.
- **포스트 양자 전환.** Ed25519는 현재 널리 배포되어 있지만 양자 저항성이 없습니다. 영수증 포맷은 알고리즘 유연성을 갖추고 있어서 `signature.alg` 필드에 필요 시 `ML-DSA-65`(NIST 포스트 양자 서명 표준)를 넣을 수 있습니다. 전환 기간 동안 영수증이 이중 서명되는 것을 계획하세요.

## 추가 자료

- <a href="https://datatracker.ietf.org/doc/draft-farley-acta-signed-receipts/" target="_blank">IETF 인터넷 드래프트: 기계 간 접근 제어를 위한 서명된 결정 영수증</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">책임 있는 AI 개요 (Azure AI)</a>
- <a href="https://datatracker.ietf.org/doc/html/rfc8032" target="_blank">RFC 8032: 에드워즈 곡선 디지털 서명 알고리즘(EdDSA)</a>
- <a href="https://datatracker.ietf.org/doc/html/rfc8785" target="_blank">RFC 8785: JSON 정식화 스킴(JCS)</a>
- <a href="https://datatracker.ietf.org/doc/html/rfc6962" target="_blank">RFC 6962: 인증서 투명성</a> (선택적 공개 영수증에서 사용하는 머클 트리 구축)
- <a href="https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/tutorials/33-offline-verifiable-receipts.md" target="_blank">Microsoft Agent Governance Toolkit, 튜토리얼 33: 오프라인 검증 가능 결정 영수증</a>
- <a href="https://github.com/ScopeBlind/agent-governance-testvectors" target="_blank">본 수업에서 사용한 영수증 포맷의 다중 구현 일치 테스트 벡터</a> (Apache-2.0)
- <a href="https://pynacl.readthedocs.io/" target="_blank">PyNaCl 문서</a> (Python 용 Ed25519)

## 이전 수업

[컴퓨터 사용 에이전트 빌드 (CUA)](../15-browser-use/README.md)

## 다음 수업

_(커리큘럼 관리자가 결정 예정)_

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->