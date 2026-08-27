# 샘플 영수증 고정 데이터

노트북을 실행하지 않고도 검사할 수 있는 세 개의 사전 생성된 영수증 파일입니다.

| 파일 | 설명 |
|---|---|
| `01_valid_receipt.json` | `lookup_flights` 도구 호출에 대한 유효한 서명된 영수증입니다. 검증 시 True를 반환합니다. |
| `02_tampered_receipt.json` | 서명 후 한 필드가 변경된 동일 영수증입니다. 검증 시 False를 반환합니다. |
| `03_chain_three_receipts.json` | 세 개의 유효 영수증(검색, 보류, 예약)이 `previous_receipt_hash`로 이전 영수증과 연결된 체인입니다. |

이 고정 데이터들은 Ed25519로 페이로드의 표준 JCS 바이트를 직접 서명합니다.
SHA-256은 콘텐츠 다이제스트와 영수증 체인 링크에 계속 사용되며,
서명 전에 추가적인 프리해시로 쓰이지 않습니다.

## 샘플 검증하기

노트북은 검증을 네 섹션으로 나누어 설명합니다. 이 고정 데이터를 노트북 내러티브 없이
직접 검증하려면 다음을 참고하세요:

```python
import json
from pathlib import Path

# 임포트 및 헬퍼 함수들을 완료했다고 가정합니다
# 18-signed-receipts.ipynb의 1섹션과 2섹션에서.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # 참

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # 거짓

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## 생성 방법

고정 데이터는 노트북과 동일한 코드 경로를 사용하며, 고정된 서명 키와
바이트 재현성을 위한 고정 타임스탬프를 사용합니다. 재생성하려면:

```bash
python3 generate_fixtures.py
```

(스크립트는 이 디렉터리의 `generate_fixtures.py`에 있습니다.)

## 학생들이 원시 JSON을 통해 배우는 내용

원시 영수증 형식을 읽으며, 노트북 셀에서 항상 제공하지 않는 직관을 쌓게 됩니다.
JSON을 대충 훑어보는 학생들은 종종 다음을 알아차립니다:

1. 서명은 불투명한 base64url 문자열이지만, 나머지 필드는 모두 일반 읽기 가능한 JSON입니다.
   서명이 콘텐츠를 암호화하는 것이 아니라 그것을 증명합니다.
2. `public_key`가 영수증에 내장되어 있습니다. 감사자는 키가 실제로
   주장된 발행자에게 속한다는 신뢰만 있으면 다른 정보 없이 검증할 수 있습니다.
   (신원 인프라에 대해서는 수업 README를 참조하세요.)
3. 필드 중 한 문자를 수정한 다음 `02_tampered_receipt.json`과 비교하면
   바이트 단위 메커니즘이 구체적으로 이해됩니다.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->