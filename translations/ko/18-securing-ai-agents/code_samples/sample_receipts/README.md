# 샘플 영수증 고정값

노트북을 실행하지 않고 확인할 수 있는 세 가지 사전 생성된 영수증 파일입니다.

| 파일 | 설명 |
|---|---|
| `01_valid_receipt.json` | `lookup_flights` 도구 호출에 대한 유효한 서명된 영수증입니다. 검증 결과는 True를 반환합니다. |
| `02_tampered_receipt.json` | 서명 후 하나의 필드가 수정된 동일한 영수증입니다. 검증 결과는 False를 반환합니다. |
| `03_chain_three_receipts.json` | `previous_receipt_hash`로 앞의 영수증과 연결된 세 개의 유효한 영수증(검색, 보류, 예약) 체인입니다. |

## 샘플 검증하기

노트북은 네 개의 섹션에서 검증 과정을 안내합니다. 노트북 내러티브를 실행하지 않고
이 고정값을 직접 검증하려면:

```python
import json
from pathlib import Path

# 1단계와 2단계의 18-signed-receipts.ipynb에서 가져오기 및 도우미 함수를 완료했다고 가정합니다.
# 18-signed-receipts.ipynb의 섹션 1과 2에서.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # 참

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # 거짓

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## 생성 방법

고정값은 노트북과 같은 코드 경로를 사용하며, 하나의 고정된 서명 키와
바이트 재현성을 위한 고정 타임스탬프를 사용합니다. 재생성 방법은:

```bash
python3 generate_fixtures.py
```

(스크립트는 이 디렉터리 내 `generate_fixtures.py`에 있습니다.)

## 학생들이 원시 JSON을 확인하며 배우는 점

원시 영수증 포맷을 읽으면 노트북 셀에서 항상 제공하지 않는 직관을 쌓을 수 있습니다.
JSON을 훑어보는 학생들은 종종 다음을 알아차립니다:

1. 서명은 불투명한 base64url 문자열이지만, 모든 다른 필드는 읽기 쉬운 JSON입니다.
   서명이 내용을 암호화하지 않고 내용을 입증합니다.
2. `public_key`가 영수증에 내장되어 있습니다. 감사자는 (키가 실제로 주장한 발행자에
   속한다는 신뢰를 전제로) 검증에 대해 다른 것이 필요 없습니다.
3. 어떤 필드의 한 글자를 변경한 후 이 파일과 `02_tampered_receipt.json`을 다시 비교하면
   바이트 수준의 메커니즘이 구체적으로 드러납니다.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->