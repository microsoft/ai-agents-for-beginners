# 샘플 영수증 예제

노트북을 실행하지 않고도 검사할 수 있는 세 개의 미리 생성된 영수증 파일입니다.

| 파일 | 설명 |
|---|---|
| `01_valid_receipt.json` | `lookup_flights` 도구 호출을 위한 유효한 서명된 영수증입니다. 검증 결과는 True를 반환합니다. |
| `02_tampered_receipt.json` | 서명 후 하나의 필드가 수정된 동일한 영수증입니다. 검증 결과는 False를 반환합니다. |
| `03_chain_three_receipts.json` | `previous_receipt_hash`로 이전 영수증과 연결된 세 개의 유효한 영수증(검색, 예약 보류, 예약)의 체인입니다. |

이 예제들은 Ed25519로 페이로드의 정규화된 JCS 바이트를 직접 서명합니다.
SHA-256은 콘텐츠 다이제스트와 영수증 체인 링크에 계속 사용되며, 서명 전에 추가적인
사전 해시 용도로는 사용되지 않습니다.

## 샘플 검증

`18-signed-receipts.ipynb`에서 먼저 Setup과 섹션 1부터 3까지 실행하세요.
섹션 3은 `verify_chain`을 정의합니다; 섹션 1과 2만으로는 충분하지 않습니다.
그런 다음 새 셀에서 다음 블록을 실행하되, 노트북의 작업 디렉터리가
`18-securing-ai-agents/code_samples`로 설정되어 있도록 하세요. 아래의 fixture 경로들은
그 디렉터리를 기준으로 합니다.

```python
import json
from pathlib import Path

fixture_dir = Path("sample_receipts")

# This fixture key is pinned by the verifier, outside the receipt under test.
FIXTURE_ISSUER_PUBLIC_KEY = "11qYAYKxCrfVS_7TyWQHOg7hcvPapiMlrwIaaPcHURo"
fixture_trusted_public_keys = {FIXTURE_ISSUER_PUBLIC_KEY}

valid = json.loads((fixture_dir / "01_valid_receipt.json").read_text())
print(
    f"Valid receipt: {verify_receipt(valid, fixture_trusted_public_keys)}"
)  # True

tampered = json.loads((fixture_dir / "02_tampered_receipt.json").read_text())
print(
    f"Tampered receipt: {verify_receipt(tampered, fixture_trusted_public_keys)}"
)  # False

chain = json.loads((fixture_dir / "03_chain_three_receipts.json").read_text())
for r in verify_chain(chain, fixture_trusted_public_keys):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

### Jupyter 없이 예제 확인

저장소 루트에서 레슨 종속성을 설치하고 다음을 실행하세요:

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

이 테스트들은 노트북의 Python 예제들과 정확히 일치하는 README 블록을 실행합니다
또한 변조 및 고정되지 않은 키가 검증자들에 의해 거부되는지도 확인합니다.
이 테스트들은 노트북의 `%pip` setup 셀을 건너뛰는데, 이는 종속성이
별도로 설치되기 때문입니다. 테스트는 노트북이나 fixtures를 변경하지 않습니다.

## 생성 방법

이 예제들은 노트북과 동일한 코드 경로를 사용하며, 고정된 서명 키와
바이트 재현 가능성을 위한 고정된 타임스탬프가 사용됩니다. 재생성 방법은:

```bash
python3 generate_fixtures.py
```

(스크립트는 이 디렉토리의 `generate_fixtures.py`에 있습니다.)

## 원시 JSON 검사를 통해 학생들이 배우는 것

원시 영수증 포맷을 읽으면 노트북의 셀에서 항상 제공하지 않는 직관을 쌓을 수 있습니다.
JSON을 대충 훑어보는 학생들은 종종 다음을 알아차립니다:

1. 서명은 불투명한 base64url 문자열이지만, 다른 모든 필드는 읽기 쉬운 평범한 JSON입니다.
   서명은 내용을 암호화하지 않고, 내용을 증명합니다.
2. `public_key`는 영수증에 내장되어 있습니다. 감사자는 별도의 것 없이
   검증할 수 있습니다 (키가 실제로 주장된 발행자에 속한다는 것을 신뢰하는 경우; 신원 인프라에 관한
   레슨 README를 참조하십시오).
3. 어떤 필드의 단일 문자를 수정한 다음 `02_tampered_receipt.json`과 비교하면,
   바이트 수준의 메커니즘이 구체적으로 이해됩니다.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**면책 조항**:
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 기하기 위해 노력하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 유의하시기 바랍니다. 원본 문서의 원어본이 권위 있는 자료로 간주되어야 합니다. 중요한 정보의 경우, 전문가의 인간 번역을 권장합니다. 이 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
