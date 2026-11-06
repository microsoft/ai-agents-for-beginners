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

在 `18-signed-receipts.ipynb` 中，先執行 Setup 以及第 1 至第 3 節。
第 3 節 定義了 `verify_chain`；只有第 1 和第 2 節 不足夠。
然後在一個新儲存格中執行以下區塊，並將 notebook 的工作目錄
設定為 `18-securing-ai-agents/code_samples`。下面的 fixture 路徑是相對於
該目錄。

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

### 在沒有 Jupyter 的情況下檢查範例

從儲存庫根目錄，安裝課程所需的相依項目並執行：

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

這些測試會執行筆記本的 Python 範例以及上方 README 中的完全相同區塊
它們也會檢查竄改與未固定金鑰是否會被
驗證器拒絕。測試會跳過筆記本的 `%pip` 設定儲存格，因為相依
項目是分別安裝的。它們不會更改筆記本或 fixtures。

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
