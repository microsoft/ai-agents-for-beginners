# 샘플 영수증 고정값

노트북을 실행하지 않고 검사할 수 있는 네 개의 미리 생성된 영수증 파일입니다.

| 파일 | 설명 |
|---|---|
| `01_valid_receipt.json` | `lookup_flights` 도구 호출에 대한 유효한 서명된 영수증입니다. 검증 결과는 True입니다. |
| `02_tampered_receipt.json` | 서명 후 한 필드가 수정된 동일한 영수증입니다. 검증 결과는 False입니다. |
| `03_chain_three_receipts.json` | 세 개의 유효한 영수증(검색, 보류, 예약)이 체인을 이루며 `previous_receipt_hash`가 각각 이전 영수증과 연결되어 있습니다. |
| `04_resigned_receipt.json` | 공격자가 변조한 뒤 다시 서명한 동일한 영수증이며, 공격자의 공개 키가 내장되어 있습니다. 내장된 키에 대해 검증은 성공하지만 발행자의 키에 대해서는 실패합니다. |

이 픽스처들은 페이로드의 표준 JCS 바이트를 Ed25519로 직접 서명합니다.
SHA-256은 콘텐츠 다이제스트와 영수증 체인 링크에 계속 사용되며,
서명 전에 추가적인 사전 해시로는 사용되지 않습니다.

## 샘플 검증하기

`18-signed-receipts.ipynb`에서 먼저 Setup과 섹션 1부터 3까지 실행하세요.
섹션 3에서 `verify_chain`를 정의하므로, 섹션 1과 2만으로는 충분하지 않습니다.
그런 다음 새 셀에서 다음 블록을 실행하며, 노트북의 작업 디렉터리를
`18-securing-ai-agents/code_samples`로 설정하세요. 아래 픽스처 경로는 해당 디렉터리를 기준으로 한 상대 경로입니다.


```python
import json
from pathlib import Path

fixture_dir = Path("sample_receipts")

# The issuer's key, pinned here rather than read from any receipt. In a real
# deployment it comes from the issuer's JWK Set or a pinned config value.
# This is the public half of the fixed signing key in generate_fixtures.py.
ISSUER_KEY = "11qYAYKxCrfVS_7TyWQHOg7hcvPapiMlrwIaaPcHURo"

valid = json.loads((fixture_dir / "01_valid_receipt.json").read_text(encoding="utf-8"))
print(f"Valid receipt: {verify_receipt(valid, ISSUER_KEY)}")        # True

tampered = json.loads((fixture_dir / "02_tampered_receipt.json").read_text(encoding="utf-8"))
print(f"Tampered receipt: {verify_receipt(tampered, ISSUER_KEY)}")  # False

chain = json.loads((fixture_dir / "03_chain_three_receipts.json").read_text(encoding="utf-8"))
for r in verify_chain(chain, ISSUER_KEY):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")

# The forgery. Verified against the key it carries, it passes. Against the
# issuer's key, it fails. Only the second question is worth asking.
forged = json.loads((fixture_dir / "04_resigned_receipt.json").read_text(encoding="utf-8"))
print(f"Forged, checked against its own key: "
      f"{verify_receipt(forged, forged['signature']['public_key'])}")  # True
print(f"Forged, checked against issuer key:  "
      f"{verify_receipt(forged, ISSUER_KEY)}")                        # False
```

### Jupyter 없이 예제 확인하기

저장소 루트에서, 수업 종속성을 설치하고 다음을 실행하세요:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

이 테스트들은 노트북의 파이썬 예제들과 위의 정확한 README 블록을 실행합니다.
또한 변조되거나 고정되지 않은 키가 검증 도구에 의해 거부되는지도 검사합니다.
테스트는 노트북의 `%pip` 설정 셀을 건너뛰는데, 종속성이
별도로 설치되기 때문입니다. 이들은 노트북이나 픽스처를 변경하지 않습니다.

## 이들 생성 방법

픽스처들은 노트북과 동일한 코드 경로를 사용하며, 하나의 고정된 서명 키와
바이트 재현성을 위한 고정된 타임스탬프를 사용합니다. 다시 생성하려면:

```bash
python3 generate_fixtures.py
```

(스크립트는 이 디렉터리의 `generate_fixtures.py`에 있습니다.)

`../test_signed_receipts.py`는 이 모든 것을 자동으로 확인합니다: 실행합니다
노트북의 코드는 이 네 가지 픽스처를 노트북의
`verify_receipt`와 `verify_chain`으로 검증하며, 픽스처를 다시 생성해도
동일한 바이트가 나오는 것을 확인합니다. `code_samples`에서:

```bash
python -m unittest test_signed_receipts
```

## 학생들이 원시 JSON을 검사하면서 배우는 것

원시 영수증 형식을 읽으면 노트북 셀이 항상 제공하지 않는 직관을 쌓을 수 있습니다.
JSON을 대충 훑어보는 학생들이 종종 알아차리는 점은:

1. 서명은 불투명한 base64url 문자열이지만, 나머지 모든 필드는 평범한 읽을 수 있는 JSON입니다.
   서명은 내용을 암호화하지 않고, 내용에 대해 증명하는 역할을 합니다.
2. `public_key` 는 영수증에 내장되어 있어 파일을 
   독립적으로 만들지만 감사자가 확인하는 대상은 아닙니다. 
   `02_tampered_receipt.json` 와 `04_resigned_receipt.json` 를 비교해 보세요: 둘 다 
   서명 후에 변경되었지만, 두 번째는 공격자의 
   키로 재서명되어 자신이 가진 키로 검증됩니다. 
   내장된 키는 파일이 내부적으로 일관됨을 알려줍니다. 
   발급자를 알려면 다른 곳에서 얻은 키만이 필요합니다.
3. `signature` 외부의 어떤 필드의 단일 문자를 수정한 후, 
   이 파일을 `02_tampered_receipt.json` 와 다시 비교하면, 
   바이트 수준의 메커니즘이 구체화됩니다.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->