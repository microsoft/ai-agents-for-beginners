# 範例收據範本

四個預先產生的收據檔案，可供檢查而無需執行筆記本。

| 檔案 | 內容說明 |
|---|---|
| `01_valid_receipt.json` | 已簽署的有效收據，針對 `lookup_flights` 工具呼叫。驗證結果為 True。 |
| `02_tampered_receipt.json` | 相同收據，在簽署後其中一欄位被修改。驗證結果為 False。 |
| `03_chain_three_receipts.json` | 三個有效收據 (搜尋、保留、訂位) 的鏈條，`previous_receipt_hash` 將每個收據連結到前一個。 |
| `04_resigned_receipt.json` | 同一份收據被攻擊者篡改後重新簽署，並嵌入了攻擊者自己的公鑰。根據內部的鑰匙進行驗證通過。根據發行者的鑰匙驗證失敗。 |

固定裝置直接使用 Ed25519 對有效負載的標準 JCS 位元組進行簽名。
SHA-256 仍用於內容摘要和收據鏈接，而非簽名前的額外預雜湊。


## 驗證範例

在 `18-signed-receipts.ipynb` 中，先執行 Setup 與第 1 至第 3 節。
第 3 節定義了 `verify_chain`；僅第 1 與第 2 節是不足夠的。
然後在一個新儲存格中執行以下區塊，筆記本的工作目錄
設為 `18-securing-ai-agents/code_samples`。以下的 fixture 路徑是相對於該目錄。


```python
import json
from pathlib import Path

fixture_dir = Path("sample_receipts")

# The issuer's key, pinned here rather than read from any receipt. In a real
# deployment it comes from the issuer's JWK Set or a pinned config value.
# This is the public half of the fixed signing key in generate_fixtures.py.
ISSUER_KEY = "11qYAYKxCrfVS_7TyWQHOg7hcvPapiMlrwIaaPcHURo"

valid = json.loads((fixture_dir / "01_valid_receipt.json").read_text(encoding="utf-8"))
print(f"Valid receipt: {verify_receipt(valid, ISSUER_KEY)}")        # True

tampered = json.loads((fixture_dir / "02_tampered_receipt.json").read_text(encoding="utf-8"))
print(f"Tampered receipt: {verify_receipt(tampered, ISSUER_KEY)}")  # False

chain = json.loads((fixture_dir / "03_chain_three_receipts.json").read_text(encoding="utf-8"))
for r in verify_chain(chain, ISSUER_KEY):
    print(f"  Receipt {r['index']} ({r['tool']}): {'VALID' if r['overall_valid'] else 'INVALID'}")

# The forgery. Verified against the key it carries, it passes. Against the
# issuer's key, it fails. Only the second question is worth asking.
forged = json.loads((fixture_dir / "04_resigned_receipt.json").read_text(encoding="utf-8"))
print(f"Forged, checked against its own key: "
      f"{verify_receipt(forged, forged['signature']['public_key'])}")  # True
print(f"Forged, checked against issuer key:  "
      f"{verify_receipt(forged, ISSUER_KEY)}")                        # False
```

### 在沒有 Jupyter 的情況下檢查範例

從儲存庫根目錄安裝課程依賴並執行：

```bash
python -m pip install -r 18-securing-ai-agents/code_samples/requirements.txt
python -m unittest discover -s 18-securing-ai-agents/code_samples -p test_signed_receipts.py -v
```

這些測試執行筆記本的 Python 範例及上方 README 的相同區段。
同時也檢查驗證程式是否拒絕竄改和未鎖定的金鑰。
測試會略過筆記本的 `%pip` 設定儲存格，因為依賴是另外安裝的。
它們不會更動筆記本或測試用例。

## 這些如何產生

測試用例使用和筆記本相同的程式碼路徑，且使用固定的簽章金鑰
及固定的時間戳記以確保位元可重現性。重新生成的方法為：

```bash
python3 generate_fixtures.py
```

(腳本位於此目錄中的 `generate_fixtures.py`。)

`../test_signed_receipts.py` 會自動檢查所有這些：它會執行
筆記本的程式碼，使用筆記本的四個固定裝置進行驗證
`verify_receipt` 和 `verify_chain`，並確認重新生成
固定裝置會產生相同的位元組。來自 `code_samples`：

```bash
python -m unittest test_signed_receipts
```

## 從檢查原始 JSON 中學生學到的東西

閱讀原始收據格式能建立直覺，而筆記本中的儲存格並不總是能提供這種直覺。  
略讀 JSON 的學生通常會注意到：

1. 簽名是一個不透明的 base64url 字串，但其他欄位都是純文字可讀的 JSON。
   簽名不會加密內容；它是對內容的證明。
2. `public_key` 嵌入在收據中，使檔案
   是自包含的，但這不是審核員驗證的對象。比較
   `02_tampered_receipt.json` 與 `04_resigned_receipt.json`：兩者都是
   在簽章後被修改，但第二個是使用攻擊者自己的金鑰重新簽章，
   所以它可以用隨帶的金鑰來驗證。嵌入的金鑰
   告訴你檔案在內部是一致的。只有從其他地方取得的金鑰
   告訴你是誰發行它。
3. 修改 `signature` 之外任一欄位的單一字元，然後
   再將此檔案與 `02_tampered_receipt.json` 重新比較，使
   位元層級機制變得具體。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->