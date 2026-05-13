[Watch the lesson video: Securing AI Agents with Cryptographic Receipts](https://youtu.be/PLACEHOLDER_VIDEO_ID)

> _(Lesson video and thumbnail to be added by the Microsoft content team post-merge, matching the lesson 14 / 15 pattern.)_

# Securing AI Agents with Cryptographic Receipts

## 소개

이 강의에서는 다음 내용을 다룹니다:

- AI 에이전트의 감사 추적(audit trail)이 컴플라이언스, 디버깅, 신뢰에 왜 중요한지
- 암호학적 영수증이란 무엇이며 서명되지 않은 로그 라인과 어떻게 다른지
- 평이한 Python으로 에이전트의 도구 호출에 대한 서명된 영수증을 생성하는 방법
- 영수증을 오프라인으로 검증하고 변조를 감지하는 방법
- 영수증을 체인으로 연결하여 하나를 제거하거나 순서를 변경하면 체인이 깨지는 방법
- 영수증이 증명하는 것과 명시적으로 증명하지 않는 것

## 학습 목표

이 강의를 완료하면 다음을 알게 됩니다:

- 에이전트 동작에 대한 암호학적 출처 증명이 필요한 실패 모드를 식별하는 방법
- 표준화된 JSON 페이로드에 대해 Ed25519로 서명된 영수증을 생성하는 방법
- 서명자의 공개 키만 사용하여 독립적으로 영수증을 검증하는 방법
- 수정된 영수증에 대해 검증을 다시 수행하여 변조를 감지하는 방법
- 해시 체인된 영수증 시퀀스를 구축하고 체인이 왜 중요한지 설명하는 방법
- 영수증이 증명하는 것(귀속, 무결성, 순서)과 증명하지 않는 것(동작의 정당성, 정책의 타당성) 사이의 경계 인식

## 문제: 에이전트의 감사 추적

Contoso Travel 용 AI 에이전트를 배포했다고 가정해 보십시오. 이 에이전트는 고객 요청을 읽고, 항공편 API를 호출하여 옵션을 조회한 후 고객을 대신해 좌석을 예약합니다. 지난 분기에 이 에이전트는 50,000건의 예약을 처리했습니다.

오늘 감사자가 도착합니다. 간단한 질문을 합니다: "에이전트가 무엇을 했는지 보여주세요."

로그 파일을 건네줍니다. 감사자는 더 까다로운 질문을 합니다: "이 로그가 편집되지 않았다는 것을 어떻게 알 수 있나요?"

이것이 감사 추적 문제입니다. 오늘날 대부분 에이전트 배포는 다음에 의존합니다:

- **응용 프로그램 로그**: 에이전트 자체가 작성하며 파일 시스템 접근 권한이 있는 누구나 편집 가능
- **클라우드 로깅 서비스**: 플랫폼 수준에서 변조 감지 가능하지만 감사자가 플랫폼 운영자를 신뢰할 경우에만 유효
- **데이터베이스 트랜잭션 로그**: 데이터베이스 변경에는 적합하지만 임의 도구 호출에는 부적절

이들 중 그 어떤 것도 감사자가 누군가(당신, 클라우드 공급자, 데이터베이스 공급자)를 신뢰하지 않고 감사자의 질문에 답할 수 없습니다. 내부 용도라면 신뢰가 수락될 수 있지만, 규제 대상 작업(금융, 의료, EU AI 법 적용 대상 등)에는 그렇지 않습니다.

암호학적 영수증은 각 에이전트 동작을 독립적으로 검증 가능하게 만들어 이 문제를 해결합니다. 감사자는 당신을 신뢰할 필요 없이 공개 키와 영수증만 있으면 됩니다.

## 암호학적 영수증이란?

영수증은 에이전트가 수행한 작업을 기록한 JSON 객체로, 디지털 서명되어 있습니다.

```mermaid
flowchart LR
    A[에이전트가 도구를 호출함] --> B[영수증 페이로드 생성]
    B --> C[JSON RFC 8785 표준화]
    C --> D[SHA-256 해시]
    D --> E[Ed25519 서명]
    E --> F[서명된 영수증]
    F --> G[감사자가 오프라인으로 검증]
    G --> H{서명 유효한가?}
    H -- yes --> I[변조 방지 증거]
    H -- no --> J[영수증 거부됨]
```

최소 영수증 예시는 다음과 같습니다:

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

세 가지 속성이 작업을 수행합니다:

1. <strong>서명</strong>. 영수증은 에이전트의 게이트웨이에서 Ed25519 비공개 키로 서명합니다. 대응하는 공개 키를 가진 누구나 서명을 오프라인으로 검증할 수 있습니다. 어떤 필드든 변조 시 서명은 무효가 됩니다.

2. **표준 인코딩**. 서명 전에 JSON Canonicalization Scheme(JCS, RFC 8785)을 사용해 영수증을 직렬화합니다. 이를 통해 두 구현체가 동일한 논리적 영수증을 만들어 바이트까지 동일한 출력을 제공합니다. 표준화가 없으면 서로 다른 JSON 직렬화기가 같은 내용에 대해 다른 서명을 생성할 수 있습니다.

3. **해시 체인**. `previous_receipt_hash` 필드는 각 영수증을 이전 영수증과 연결합니다. 하나의 영수증을 제거하거나 순서를 변경하면 그 이후 영수증 모두가 깨집니다. 개별 서명을 우회하더라도 체인 수준에서 변조가 감지됩니다.

이 속성들은 세 가지 보증을 제공합니다:

- <strong>귀속</strong>: 이 키가 이 콘텐츠에 서명했다.
- <strong>무결성</strong>: 서명 이후 내용이 변경되지 않았다.
- <strong>순서</strong>: 이 영수증이 체인에서 저 영수증 이후에 생성되었다.

## Python에서 영수증 생성하기

영수증을 생성하려고 특별한 라이브러리가 필요하지 않습니다. 암호학 기본 요소는 널리 사용 가능하며, 로직도 수십 줄의 Python 코드입니다.

`code_samples/18-signed-receipts.ipynb`의 핸즈온 연습에서는 전체 과정을 단계별로 안내합니다. 요약 버전:

```python
import json
import hashlib
import base64
from nacl import signing
from jcs import canonicalize  # RFC 8785 정규 JSON

def b64url_nopad(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode("ascii").rstrip("=")

def sha256_canonical(obj) -> str:
    """SHA-256 of a Python object's JCS-canonical JSON form."""
    return f"sha256:{hashlib.sha256(canonicalize(obj)).hexdigest()}"

# 서명 키 생성 또는 로드(운영 환경에서는 키 금고에 저장)
signing_key = signing.SigningKey.generate()
verify_key = signing_key.verify_key

# 영수증 페이로드 작성(아직 서명 없음)
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

이것이 전체 서명 파이프라인입니다. 노트북의 연습에서 각 단계를 자세히 다룹니다.

## 영수증 검증과 변조 감지

검증은 역과정입니다:

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

이 함수는 영수증을 받아 서명이 유효하면 `True`, 그렇지 않으면 `False`를 반환합니다. 네트워크 호출, 서비스 의존성, 제3자 신뢰가 전혀 필요 없습니다.

변조 감지 데모는 노트북에서 다음을 다룹니다:

1. 유효한 영수증을 생성하고 검증되는지 확인하기
2. `tool_args_hash` 필드의 한 바이트를 수정하기
3. 다시 검증하여 실패하는지 확인하기

이것이 영수증이 변조 감지 기능을 가진 실질적 증거입니다: 아주 작은 변경이라도 서명을 깨뜨립니다.

## 다단계 에이전트를 위한 영수증 체인

단일 서명 영수증은 하나의 동작을 보호합니다. 영수증 체인은 시퀀스를 보호합니다.

```mermaid
flowchart LR
    R0[영수증 0<br/>제네시스] --> R1[영수증 1]
    R1 --> R2[영수증 2]
    R2 --> R3[영수증 3]
    R1 -. previous_receipt_hash .-> R0
    R2 -. previous_receipt_hash .-> R1
    R3 -. previous_receipt_hash .-> R2
```

각 영수증은 앞선 영수증의 해시를 기록합니다. 악의자가 2번째 영수증을 조용히 제거하려면 다음 둘 중 하나가 필요합니다:

- 3번째 영수증의 `previous_receipt_hash` 필드를 수정(3번째 서명 깨짐)하거나,
- 수정된 3번째 영수증에 대해 새로운 서명을 위조(에이전트 비공개 키 필요).

비공개 키가 하드웨어 키 보관소에 있고 공개 키를 각 영수증과 함께 공개하면 두 공격 모두 탐지 없이 실행 불가능합니다.

노트북은 다음을 다룹니다:

1. 세 개 영수증 체인 만들기
2. 각 영수증의 `previous_receipt_hash`가 이전 영수증의 실제 해시와 일치하는지 검증하기
3. 중간 영수증을 변조하고 해당 지점에서 체인이 끊어지는지 확인하기

이렇게 외부 감사자가 신뢰 없이 검증 가능한 감사 추적을 만듭니다.

## 영수증이 증명하는 것(그리고 증명하지 않는 것)

이 강의에서 가장 중요한 부분입니다. 영수증은 강력하지만 그 힘은 한계가 있습니다.

**영수증이 증명하는 세 가지:**

1. <strong>귀속</strong>: 특정 키가 특정 페이로드에 서명했다.
2. <strong>무결성</strong>: 서명 이후 페이로드가 변경되지 않았다.
3. <strong>순서</strong>: 이 영수증이 체인에서 저 영수증 뒤에 왔다.

**영수증이 증명하지 않는 것:**

1. <strong>정확성</strong>: 에이전트 동작이 옳은 행동이었다는 것. 틀린 답안도 영수증으로 똑같이 서명될 수 있다.
2. **정책 준수**: `policy_id`에 나타난 정책이 실제 평가되었거나, 평가될 경우 이 동작이 허용되었는지. 영수증은 주장한 바를 기록할 뿐 실행 여부를 증명하지 않는다.
3. **키 이상의 신원 보장**: 영수증은 "이 키가 이 콘텐츠에 서명했다"고 하지만 "이 사람이 이 행동을 승인했다"고 하지 않는다. 키와 인물을 연결하는 것은 별도의 신원 인프라가 필요하다(디렉터리, 공개 키 레지스트리 등).
4. **입력의 진실성**: 에이전트가 조작된 프롬프트를 받아 동작했더라도 영수증은 그 동작을 충실히 기록한다. 영수증은 입력 검증의 하류이며 대체물이 아니다.

이 경계가 중요한 이유는 두 가지입니다:

- 영수증이 어떤 용도로 유용한지를 알려줌: 에이전트 행동을 감사 가능하고 변조 감지 가능하게 만들기, 조직 경계까지 포함.
- 추가로 필요한 계층을 알림: 입력 검증(6강), 정책 적용(아래에서 약간 다룸), 신원 인프라(본 강의 범위 외).

흔한 착각은 "우리에겐 영수증이 있으니 규제받는다"는 생각입니다. 그렇지 않습니다. 영수증은 기초입니다. 규제는 그 위에 구축하는 시스템입니다.

## 실제 참고자료

이 강의의 Python 코드는 작고 명확하여 각 줄을 이해할 수 있게 설계되었습니다. 실제 운영에서는 두 가지 선택지가 있습니다:

1. **암호학 기본 요소를 직접 사용**. 위에 나온 약 50줄 코드는 많은 용도에 충분합니다. PyNaCl(Ed25519)과 `jcs` 패키지(표준 JSON)는 잘 유지보수되고 감사된 라이브러리입니다.

2. **상용 영수증 라이브러리 사용**. 여러 오픈소스 프로젝트가 동일한 패턴을 추가 기능(키 교체, 배치 검증, JWK 세트 배포, 정책 엔진 통합)과 함께 구현합니다:
   - 이 강의에서 쓰인 영수증 포맷은 현재 표준 절차 중인 IETF 인터넷 초안(`draft-farley-acta-signed-receipts`)을 따릅니다.
   - Microsoft Agent Governance Toolkit은 Cedar 기반 정책 결정과 영수증을 결합합니다; 해당 저장소의 튜토리얼 33에서 전체 예제를 확인하세요.
   - `protect-mcp`(npm) 및 `@veritasacta/verify`(npm) 패키지는 tamper-evident 감사 추적으로 MCP 서버를 래핑하기 위한 노드 기반 영수증 서명 및 오프라인 검증 구현체입니다.

직접 구현할지 라이브러리를 사용할지는 JWT 라이브러리 선택과 유사합니다: 둘 다 합리적; 라이브러리가 시간 절약 및 감사 표면 감소; 직접 구현은 모든 기본 요소를 이해하게 됨. 이 강의는 직접 구현 방식을 가르쳐 어느 쪽 선택에도 기초를 제공합니다.

## 이해 점검

실습 전에 이해도를 테스트하세요.

**1. 영수증은 에이전트의 Ed25519 비공개 키로 서명됩니다. 감사자는 공개 키만 갖고 있습니다. 감사자가 오프라인으로 영수증을 검증할 수 있나요?**

<details>
<summary>답변</summary>

네. Ed25519 검증에 필요한 것은 공개 키와 서명된 바이트뿐입니다. 네트워크 호출, 서비스 의존성 없이 가능하며, 이것이 영수증이 격리된 환경, 다중 조직, 또는 낮은 신뢰 감사 상황에서 유용한 이유입니다.
</details>

**2. 공격자가 영수증의 `policy_id` 필드를 더 관대한 정책을 적용한 것처럼 수정했습니다. 서명은 원본 페이로드에 대해 됐습니다. 검증 과정에서 무슨 일이 발생하나요?**

<details>
<summary>답변</summary>

검증 실패합니다. 서명은 원본 페이로드의 표준화된 바이트에서 계산됐습니다; 어떤 필드를 수정하면 표준화된 바이트가 바뀌어 SHA-256 해시가 바뀌고, 결국 서명이 유효하지 않게 됩니다. 공격자는 새 서명을 생성하려면 비공개 키가 필요한데, 이 키는 없으므로 실패합니다.
</details>

**3. 왜 영수증은 원시 인수나 결과 대신 `tool_args_hash`와 `result_hash`를 포함하나요?**

<details>
<summary>답변</summary>

두 가지 이유입니다. 첫째, 영수증은 보관되거나 전송될 때 원시 내용(PII, 비즈니스 데이터) 누출이 문제가 되는 환경을 가질 수 있습니다. 해시를 사용하면 영수증 크기는 작게 유지되고 내용은 비공개로 유지됩니다; 감사자는 별도로 보관된 실제 내용과 해시 일치를 확인합니다. 둘째, 해시는 크기가 고정되어 입력과 출력이 아무리 커도 영수증 크기는 제한됩니다.
</details>

**4. `previous_receipt_hash` 필드는 각 영수증을 이전 영수증과 연결합니다. 공격자가 체인 중간에서 한 영수증을 조용히 삭제하면 무엇이 무효가 되나요?**

<details>
<summary>답변</summary>

삭제된 영수증 이후 모든 영수증의 `previous_receipt_hash` 필드가 실제 체인과 일치하지 않게 되어 무효가 됩니다(참조한 영수증이 없거나 체인이 다른 선행을 가리킴). 삭제를 숨기려면 이후 모든 영수증을 재서명해야 하는데, 이는 비공개 키가 있어야 가능합니다.
</details>

**5. 영수증이 정상 검증됐습니다. 이로써 에이전트 동작의 정확성, 건전성 또는 정책 준수가 증명되나요?**

<details>
<summary>답변</summary>

아닙니다. 유효한 영수증은 세 가지를 증명합니다: 귀속(이 키가 이 콘텐츠에 서명했다), 무결성(내용이 변경되지 않았다), 순서(이 영수증이 저 영수증 뒤에 왔다). 동작이 올바르다거나 `policy_id`에 명시된 정책이 실제 평가되었거나 모든 규칙을 따랐다는 뜻은 아닙니다. 영수증은 에이전트 행동을 감사 가능하게 만들 뿐, 반드시 정확하지는 않습니다. 이것이 이 강의에서 가장 중요한 경계입니다.
</details>

## 실습 연습

`code_samples/18-signed-receipts.ipynb`를 열어 네 섹션을 모두 완료하세요:

1. **섹션 1**: 첫 영수증에 서명하고 검증하기.
2. **섹션 2**: 영수증을 변조하고 검증 실패 관찰하기.
3. **섹션 3**: 세 개 영수증 체인 만들고 체인 무결성 검증하기.
4. **섹션 4**: Microsoft Agent Framework로 구축된 에이전트에 패턴을 적용: 도구 호출에 영수증 서명 래핑, 영수증 독립 검증.

**도전 과제 1:** 영수증 스키마에 임의의 추가 필드(예: 추적용 요청 ID)를 넣고 표준 서명 로직을 갱신 후, 영수증이 검증 과정에서 정상적으로 왕복하는지 확인하세요. 그 후 서명 후 필드를 수정해 검증 실패를 확인하세요. 이것은 표준 인코딩의 모든 바이트가 서명에 어떻게 기여하는지 이해하게 합니다.
**도전 과제 2:** 두 개의 영수증을 SHA-256으로 해시합니다(결정론적 순서로 정규화된 바이트를 연결). 그리고 그 결과 다이제스트를 세 번째 영수증의 새로운 필드로 삽입한 뒤 서명하세요. 세 개의 영수증 모두가 여전히 올바르게 왕복 검증되는지 확인합니다. 이렇게 하면 단일 단계 포함 증명을 구축한 것입니다: 세 번째 영수증을 가진 누구나 그 서명 시점에 첫 두 영수증이 존재했다는 것을, 내용 공개 없이 증명할 수 있습니다. 이것은 선택적 공개 영수증이 대규모로 사용하는 패턴입니다(머클 커밋먼트, RFC 6962).

## 결론

암호화 영수증은 AI 에이전트에게 다음과 같은 감사 추적을 제공합니다:

- **독립적으로 검증 가능**: 공개키를 가진 어느 쪽이든 검증할 수 있으며, 서비스 의존성이 없습니다.
- **변조 감지 가능**: 어떤 수정이라도 서명을 무효화합니다.
- **휴대 가능**: 영수증은 작은 JSON 파일로서, 보관, 전송, 어디서나 검증할 수 있습니다.
- **표준 준수**: Ed25519 (RFC 8032), JCS (RFC 8785), SHA-256 등의 널리 배포된 원시 알고리즘 위에 구축되었습니다.

영수증은 입력 검증, 정책 실행, 또는 신원 인프라를 대체하지 않습니다. 그것들은 그런 계층들을 위한 기반입니다. 규제된 작업, 다기관 워크플로우, 또는 미래의 감사자가 신뢰할 수 없는 상황에 에이전트를 배포할 때, 영수증은 감사 추적을 정직하게 만드는 방법입니다.

가장 중요한 핵심은: 영수증은 누가 언제 무엇을 말했는지를 증명합니다. 영수증은 말한 내용이 진실이거나 옳았음을 증명하지 않습니다. 이 차이를 확실히 인식하세요. 정직한 출처 시스템과 오해를 불러일으키는 시스템의 차이입니다.

## 생산 준비 체크리스트

이 교육과정을 졸업하고 실제 환경에 영수증 서명 에이전트를 배포할 준비가 되면:

- [ ] **서명 키를 개발자 노트북에서 이동하세요.** Azure Key Vault, AWS KMS, 또는 하드웨어 보안 모듈을 사용하세요. 영수증 서명에 사용하는 비공개 키는 절대 소스 컨트롤이나 평문으로 애플리케이션 머신에 존재해서는 안 됩니다.
- [ ] **검증용 공개 키를 공개하세요.** 감사자가 오프라인으로 검증할 수 있어야 합니다. 표준 패턴은 알려진 URL에 JWK 세트 (RFC 7517) 게시, 예: `https://your-org.example.com/.well-known/agent-keys.json`.
- [ ] **체인을 외부에 앵커링 하세요.** 정기적으로 최신 체인 헤드 해시를 투명성 로그(Sigstore Rekor, RFC 3161 타임스탬프 권한, 또는 두 번째 내부 시스템)에 기록하여 외부 당사자가 “이 체인이 이 시점에 존재했다”를 확인할 수 있게 합니다.
- [ ] **영수증을 변경 불가능하게 저장하세요.** 추가만 가능한 Blob 저장소(Azure Storage 불변 정책, AWS S3 Object Lock)가 내부자가 저장 계층에서 기록을 다시 쓰는 것을 방지합니다.
- [ ] **보존 기간을 결정하세요.** 많은 규정 준수 체계가 다년 보존을 요구합니다. 영수증 증가량을 계획하세요(영수증 하나당 약 500바이트, 에이전트가 하루에 10,000건 호출 시 연간 약 1.8GB 생성).
- [ ] **영수증이 다루지 않는 내용을 문서화하세요.** 영수증은 귀속, 무결성, 순서를 증명합니다. 귀하의 운영 매뉴얼에는 입력 검증, 정책 집행, 속도 제한, 신원 인프라와 같은 추가 제어가 영수증과 함께 거버넌스 태세에 어떻게 위치하는지 명확히 적어야 합니다.

### AI 에이전트 보안에 관한 추가 질문이 있나요?

다른 학습자들과 만나고, 오피스 아워에 참석하며 AI 에이전트 관련 질문에 답변을 받으려면 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord)에 참여하세요.

## 이 과정을 넘어

이 수업에서는 단일 영수증 서명과 해시로 체인된 시퀀스를 다루었습니다. 동일한 원시 알고리즘이 성숙한 거버넌스 태세에서 마주칠 수 있는 여러 고급 패턴으로 구성됩니다:

- **선택적 공개.** 영수증 필드를 독립적으로 커밋할 때(RFC 6962 스타일 머클 트리), 특정 필드를 특정 감사자에게 공개하고 나머지는 변경되지 않았음을 노출 없이 증명할 수 있습니다. 동일한 영수증이 포괄적 감사를 만족시키면서도 GDPR같은 데이터 최소화 규정을 준수해야 할 때 유용합니다.
- **영수증 폐기.** 서명 키가 유출되면, 그 키로 서명된 모든 영수증을 신뢰할 수 없게 표시할 방법이 필요합니다. 표준 패턴은 단기 서명 키 및 공개 폐기 목록, 혹은 폐기 항목이 포함된 투명성 로그입니다.
- **양자 서명/분할 서명 영수증.** 일부 구현은 서명한 페이로드를 실행 전(`authorization_*`)과 실행 후(`result_*`)의 두 절반으로 나누어 독립 서명하며, 권한 부여 결정과 관찰된 결과가 다른 행위자나 다른 시점에 생산될 때 유용합니다. 이는 본 수업에서 다룬 영수증 포맷 위에 추가적으로 구성됩니다.
- **페이로드 구성.** 영수증은 `result_hash`에 넣는 어떤 바이트든 봉인합니다. 실제 페이로드는 단일 도구 호출 결과보다 풍부하며: 결정 전 추론(모델 예측, 고려 옵션, 증거 및 완전성, 위험 태도, 책임 체인, 게이트 결과)이 단일 영수증으로 봉인될 수 있습니다. 이는 영수증 포맷은 최소한으로 유지하면서 페이로드 스키마는 영역별로 진화할 수 있게 합니다.
- **교차 구현 적합성.** 동일한 영수증 포맷의 독립적 구현체 (Python, TypeScript, Rust, Go)가 공유 테스트 벡터 대비 상호 검증합니다. 자체 구현 시 공개된 벡터와 검증하면 통신 호환성을 확인할 수 있습니다.
- **후양자 이행.** Ed25519는 현재 널리 배포되어 있으나 양자 저항성은 없습니다. 영수증 포맷은 알고리즘 변경 가능하며: `signature.alg` 필드에 필요 시 `ML-DSA-65` (NIST 후양자 서명 표준)를 담을 수 있습니다. 영수증이 이중 서명되는 전환 기간을 계획하세요.

## 추가 자료

- <a href="https://datatracker.ietf.org/doc/draft-farley-acta-signed-receipts/" target="_blank">IETF 인터넷 초안: 기계 간 접근 제어를 위한 서명된 결정 영수증</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">책임 있는 AI 개요 (Azure AI)</a>
- <a href="https://datatracker.ietf.org/doc/html/rfc8032" target="_blank">RFC 8032: Edwards-곡선 디지털 서명 알고리즘 (EdDSA)</a>
- <a href="https://datatracker.ietf.org/doc/html/rfc8785" target="_blank">RFC 8785: JSON 정규화 스킴 (JCS)</a>
- <a href="https://datatracker.ietf.org/doc/html/rfc6962" target="_blank">RFC 6962: 인증서 투명성</a> (선택적 공개 영수증에서 사용하는 머클 트리 구조)
- <a href="https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/tutorials/33-offline-verifiable-receipts.md" target="_blank">Microsoft Agent Governance Toolkit, 튜토리얼 33: 오프라인 검증 가능한 결정 영수증</a>
- <a href="https://github.com/ScopeBlind/agent-governance-testvectors" target="_blank">이 수업에서 사용한 영수증 포맷에 대한 교차 구현 적합성 테스트 벡터</a> (Apache-2.0)
- <a href="https://pynacl.readthedocs.io/" target="_blank">PyNaCl 문서</a> (Python에서 Ed25519)

## 이전 강의

[컴퓨터 사용 에이전트 구축 (CUA)](../15-browser-use/README.md)

## 다음 강의

_(커리큘럼 유지관리자가 결정 예정)_

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->