# 範例收據範本

三個預先產生的收據檔供檢視，無須執行筆記本。

| 檔案 | 說明 |
|---|---|
| `01_valid_receipt.json` | 一個有效且已簽署的 `lookup_flights` 工具呼叫收據。驗證結果為 True。 |
| `02_tampered_receipt.json` | 在簽署後修改一個欄位的相同收據。驗證結果為 False。 |
| `03_chain_three_receipts.json` | 三個有效收據（搜尋、保留、預訂）串接的鏈條，以 `previous_receipt_hash` 連結每個前一筆。 |

這些範本直接以 Ed25519 簽署有效負載的正規 JCS 位元組。
SHA-256 仍用於內容摘要及收據鏈結，不是作為簽署前的額外預散列。


## 驗證範例

在 `18-signed-receipts.ipynb`, 先執行 Setup 和第 1 到第 3 節.
第 3 節定義了 `verify_chain`; 只有第 1 和第 2 節是不夠的.
然後在一個新的儲存格中執行下列區塊，並將 notebook 的工作目錄
設定為 `18-securing-ai-agents/code_samples`. 下方的 fixture 路徑是相對
該目錄.

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

### 在不使用 Jupyter 的情況下檢查範例

從儲存庫根目錄，安裝課程的相依套件並執行：

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

這些測試會執行筆記本中的 Python 範例以及 README 中完全相同的區塊
上述。它們也會檢查篡改和未固定的金鑰是否會被
驗證器拒絕。這些測試會跳過筆記本的 `%pip` 設定儲存格，因為相依項目
是分開安裝的。它們不會變更筆記本或測試夾具。

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
