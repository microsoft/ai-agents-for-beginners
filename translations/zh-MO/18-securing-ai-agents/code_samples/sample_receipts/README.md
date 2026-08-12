# Sample Receipt Fixtures

Three pre-generated receipt files for inspection without running the notebook.

| File | What it is |
|---|---|
| `01_valid_receipt.json` | 一個針對 `lookup_flights` 工具呼叫的有效簽署收據。驗證結果為 True。 |
| `02_tampered_receipt.json` | 同一收據，在簽署後修改了一個欄位。驗證結果為 False。 |
| `03_chain_three_receipts.json` | 三個有效收據的鏈條（搜尋、保留、預訂），以 `previous_receipt_hash` 將每個與之前的收據串連起來。 |

## Verifying the samples

The notebook walks through verification in four sections. To verify these fixtures
directly without running through the notebook narrative:

```python
import json
from pathlib import Path

# 假設你已完成導入和輔助函數
# 來自 18-signed-receipts.ipynb 的第 1 和第 2 部分。

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # 真

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # 假

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## How these were generated

The fixtures use the same code path as the notebook, with one fixed signing key
and fixed timestamps for byte-reproducibility. To regenerate:

```bash
python3 generate_fixtures.py
```

(Script is at `generate_fixtures.py` in this directory.)

## What students learn from inspecting raw JSON

Reading the raw receipt format builds intuition that the cells in the notebook
do not always provide. Students who skim the JSON often notice:

1. The signature is an opaque base64url string, but every other field is plain
   readable JSON. The signature does not encrypt the content; it attests to it.
2. The `public_key` is embedded in the receipt. An auditor needs nothing else
   to verify (subject to trusting that the key actually belongs to the claimed
   issuer; see the lesson README on identity infrastructure).
3. Modifying a single character of any field, then re-comparing this file with
   `02_tampered_receipt.json`, makes the byte-level mechanism concrete.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->