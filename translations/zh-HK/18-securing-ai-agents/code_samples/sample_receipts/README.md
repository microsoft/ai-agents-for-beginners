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

在 `18-signed-receipts.ipynb` 中，先執行 設定 以及第 1 至第 3 節。
第 3 節定義了 `verify_chain`；僅第 1 和第 2 節並不足夠。
然後在一個新儲存格執行以下區塊，並將 notebook 的工作目錄
設為 `18-securing-ai-agents/code_samples`。下面的測試夾具路徑是相對
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

從儲存庫根目錄，安裝課程的相依套件並執行：

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

這些測試會執行 notebook 的 Python 範例以及 README 中完全相同的區塊
上述。他們也會檢查遭到竄改和未鎖定的金鑰是否會被
驗證器拒絕。測試會跳過 notebook 的 `%pip` 設定儲存格，因為相依項
是另行安裝的。它們不會更改 notebook 或測試夾具。

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
