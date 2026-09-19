# 範例收據固定裝置

三個預先產生的收據檔案，方便檢查而不用執行筆記本。

| 檔案 | 它是什麼 |
|---|---|
| `01_valid_receipt.json` | 對 `lookup_flights` 工具呼叫的有效簽署收據。驗證結果為 True。 |
| `02_tampered_receipt.json` | 同一收據，在簽署後修改了一個欄位。驗證結果為 False。 |
| `03_chain_three_receipts.json` | 三個有效收據（搜尋、保留、預訂）鏈結而成的鏈條，每個皆用 `previous_receipt_hash` 鏈結至前一張。 |

這些固定裝置是直接用 Ed25519 對載荷的標準化 JCS 位元組簽名。
SHA-256 持續用於內容摘要和收據鏈結，不作為
簽名前的額外預先哈希。

## 驗證範例

筆記本分四部分詳細說明驗證。要直接驗證這些固定裝置
而不經筆記本講解：

```python
import json
from pathlib import Path

# 假設您已完成導入和輔助函數
# 來自18-signed-receipts.ipynb的第1和第2部分。

valid = json.loads(Path("01_valid_receipt.json").read_text())
print(f"Valid receipt: {verify_receipt(valid)}")        # 真

tampered = json.loads(Path("02_tampered_receipt.json").read_text())
print(f"Tampered receipt: {verify_receipt(tampered)}")  # 假

chain = json.loads(Path("03_chain_three_receipts.json").read_text())
for r in verify_chain(chain):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")
```

## 生成方式

這些固定裝置使用與筆記本相同的程式碼路徑，採用固定簽名金鑰
和固定時間戳，確保持位元組可重現。要重新生成：

```bash
python3 generate_fixtures.py
```

(腳本位於本目錄的 `generate_fixtures.py`。)

## 學生從檢查原始 JSON 中學到什麼

閱讀原始收據格式有助培養直覺，這是筆記本中儲存格
不一定會提供的。掃描 JSON 的學生常發現：

1. 簽名是一個不透明的 base64url 字串，但其他欄位都是純粹
   可讀的 JSON。簽名不是加密內容；而是一種證明。
2. `public_key` 嵌入在收據中。稽核者不需要其他東西
   即可驗證（前提是相信該金鑰確實屬於聲稱的
   發行者；可參考課程說明檔關於身份識別基礎設施的部分）。
3. 修改任何欄位的一個字元，然後與
   `02_tampered_receipt.json` 重新比較，能具體感受位元組層級的機制。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->