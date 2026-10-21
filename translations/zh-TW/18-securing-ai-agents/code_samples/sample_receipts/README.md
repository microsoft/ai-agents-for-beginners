# 範例收據範本

三個預先產生的收據檔供檢視，無須執行筆記本。

| 檔案 | 說明 |
|---|---|
| `01_valid_receipt.json` | 一個有效且已簽署的 `lookup_flights` 工具呼叫收據。驗證結果為 True。 |
| `02_tampered_receipt.json` | 在簽署後修改一個欄位的相同收據。驗證結果為 False。 |
| `03_chain_three_receipts.json` | 三個有效收據（搜尋、保留、預訂）串接的鏈條，以 `previous_receipt_hash` 連結每個前一筆。 |

這些範本直接以 Ed25519 簽署有效負載的正規 JCS 位元組。
SHA-256 仍用於內容摘要及收據鏈結，不是作為簽署前的額外預散列。


## 驗證這些範例

筆記本分成四個部份說明驗證流程。若要直接驗證這些範本，
可不必執行筆記本說明：

```python
import json
from pathlib import Path

# Assumes you have completed the imports and helper functions
# from sections 1 and 2 of 18-signed-receipts.ipynb.

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # True

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # False

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## 這些範本的生成方式

這些範本使用與筆記本相同的程式碼路徑，以固定簽署金鑰
和固定時間戳，確保位元組可重現。重新生成步驟如下：

```bash
python3 generate_fixtures.py
```

（此腳本位於本目錄的 `generate_fixtures.py`。）

## 從檢視原始 JSON 學到的知識

閱讀原始收據格式有助培養直覺，這是筆記本中
單元不一定會提供的。略讀 JSON 的學生常發現：

1. 簽章是一串不透明的 base64url 字串，其它欄位都是純
   可讀 JSON。簽章不會加密內容；它是對內容的驗證。
2. `public_key` 嵌入於收據中。稽核者不需其他東西就能驗證，
   （條件是信任該金鑰確實屬於聲稱的
   發行者；詳見課程說明中的身份基礎架構）。
3. 修改任何欄位的單一字元，然後與
   `02_tampered_receipt.json` 再次比對，可具體理解位元級的運作機制。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->