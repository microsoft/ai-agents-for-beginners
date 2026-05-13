# 範例收據測試資料

三個預先產生的收據檔案，可供檢查而無需執行筆記本。

| 檔案 | 內容說明 |
|---|---|
| `01_valid_receipt.json` | 一個有效的簽名收據，用於 `lookup_flights` 工具調用。驗證結果為 True。 |
| `02_tampered_receipt.json` | 簽署後修改過一個欄位的相同收據。驗證結果為 False。 |
| `03_chain_three_receipts.json` | 三個有效收據（搜尋、保留、訂票）串聯的鏈條，使用 `previous_receipt_hash` 互相連結。 |

## 驗證範例檔案

筆記本中有四個章節演示驗證流程。如要直接驗證這些測試資料而不需閱讀筆記本說明：

```python
import json
from pathlib import Path

# 假設你已完成第 1 和第 2 部分的導入和輔助函數
# 位於 18-signed-receipts.ipynb。

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # 是

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # 否

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## 這些檔案如何產生

這些測試資料使用與筆記本相同的程式碼路徑，且使用固定的簽名金鑰和固定的時間戳，
以確保位元組可重現。重新產生方法如下：

```bash
python3 generate_fixtures.py
```

（產生腳本位於此目錄下的 `generate_fixtures.py`。）

## 從檢查原始 JSON 學到什麼

閱讀原始收據格式能建立比筆記本中程式碼單元更直觀的理解。快速瀏覽 JSON 的學生通常會注意到：

1. 簽名是一個不透明的 base64url 字串，但其他欄位均為可讀的 JSON。簽名不對內容加密；而是為內容做鑑證。
2. `public_key` 內嵌於收據中。審核者不需其他資料即可驗證（當然前提是相信該金鑰真的屬於所聲稱的簽發者；詳見身分基礎設施的課程說明）。
3. 修改任何欄位的一個字元，再對比此檔案與 `02_tampered_receipt.json`，即可具體了解位元組層級的驗證機制。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->