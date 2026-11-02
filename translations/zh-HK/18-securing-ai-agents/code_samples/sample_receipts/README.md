# 範例收據夾具

三個預先生成的收據檔案，可供檢查而無需運行筆記本。

| 檔案 | 它是什麼 |
|---|---|
| `01_valid_receipt.json` | 一個有效簽署的 `lookup_flights` 工具呼叫收據。驗證結果為 True。 |
| `02_tampered_receipt.json` | 簽署後其中一個欄位被修改的相同收據。驗證結果為 False。 |
| `03_chain_three_receipts.json` | 三個有效收據（搜尋、保留、預訂）的鏈，使用 `previous_receipt_hash` 將每個收據與前一個連結起來。 |

這些夾具直接用 Ed25519 對有效負載的標準 JCS 位元組進行簽名。
SHA-256 仍用於內容摘要和收據鏈接，並非作為簽名前的
額外預雜湊。

## 驗證範例

筆記本透過四個部分來演示驗證。若想直接驗證這些夾具，
而無需瀏覽筆記本操作說明：

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

## 這些是如何生成的

這些測試資料使用與筆記本相同的程式路徑，並有一個固定的簽署金鑰
以及固定的時間戳記，以確保位元的可重現性。要重新生成：

```bash
python3 generate_fixtures.py
```

（腳本位於此目錄中的 `generate_fixtures.py`。）

## 從檢查原始 JSON 中學生學到的東西

閱讀原始收據格式能建立直覺，這是筆記本中的儲存格並不
總是提供的。略讀 JSON 的學生經常會注意到：

1. 簽名是一個不透明的 base64url 字串，但其他所有欄位都是可
   讀的純文字 JSON。簽名並未加密內容；而是對內容作出認證。
2. `public_key` 嵌入在收據中。審核者不需其他東西
   就能驗證（前提是信任該密鑰確實屬於聲稱的發行者；
   請參閱關於身份基礎架構的課程 README）。
3. 修改任何欄位的一個字元，然後重新跟 `02_tampered_receipt.json` 比較，
   使位元組級的機制具體化。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->