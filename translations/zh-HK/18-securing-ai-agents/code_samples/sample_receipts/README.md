# 範例收據固定資料

三個預先產生的收據檔案，可供檢查，無需執行筆記本。

| 檔案 | 內容說明 |
|---|---|
| `01_valid_receipt.json` | 一個有效的已簽署收據，用於 `lookup_flights` 工具呼叫。驗證結果為 True。 |
| `02_tampered_receipt.json` | 同一份收據，但其中一個欄位在簽署後被修改。驗證結果為 False。 |
| `03_chain_three_receipts.json` | 三個有效收據的鏈條（search、hold、book），透過 `previous_receipt_hash` 將每個收據連結到前一個。 |

## 驗證範例

筆記本以四個章節說明驗證步驟。若要直接驗證這些固定資料而不透過筆記本說明：

```python
import json
from pathlib import Path

# 假設你已經完成了導入和輔助函數的編寫
# 來自 18-signed-receipts.ipynb 的第 1 及第 2 部分。

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # 是

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # 否

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## 產生方式說明

這些固定資料使用與筆記本相同的程式碼路徑，並使用固定的簽署金鑰
和固定時間戳，以確保位元組可重現。欲重新產生：

```bash
python3 generate_fixtures.py
```

（腳本位置在此目錄中的 `generate_fixtures.py`。）

## 學生從檢視原始 JSON 中學到什麼

閱讀原始收據格式可以建立直覺，這是筆記本中程式格子不一定提供的。快速瀏覽 JSON 的學生常注意到：

1. 簽名是不可讀的 base64url 字串，但其他欄位皆為可讀的純 JSON。簽名不是加密內容，而是對其內容的證明。
2. `public_key` 嵌入在收據中。稽核者不需要其他東西即可驗證（前提是相信該金鑰確實隸屬於聲稱的發行者；請參閱課程 README 的身份基礎設施說明）。
3. 修改任何欄位的一個字元，接著與 `02_tampered_receipt.json` 重新比較，可以使位元層級的運作機制更加具體。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->