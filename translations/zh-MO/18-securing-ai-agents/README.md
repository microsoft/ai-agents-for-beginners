[觀看課程影片：使用加密收據保護 AI 代理](https://youtu.be/PLACEHOLDER_VIDEO_ID)

> _(課程影片與縮圖將由 Microsoft 內容團隊在合併後新增，符合第14/15課的模式。)_

# 使用加密收據保護 AI 代理

## 簡介

本課將涵蓋：

- 為什麼 AI 代理的審計軌跡對合規、除錯及信任很重要。
- 什麼是加密收據，以及它和未簽署的日誌行有何不同。
- 如何用純 Python 為代理的工具呼叫產生簽署收據。
- 如何離線驗證收據並偵測篡改。
- 如何串接收據鏈條，使刪除或重排任一收據會破壞整條鏈。
- 收據能證明什麼，以及它明確不證明什麼。

## 學習目標

完成本課後，你將能：

- 識別驅動加密溯源代理行為的失敗模式。
- 產生帶有 Ed25519 簽名的收據，內容為標準化 JSON 載荷。
- 使用僅有簽署者公鑰來獨立驗證收據。
- 透過重新驗證被修改收據發現篡改。
- 建立串接的收據雜湊鏈及說明鏈條重要性。
- 識別收據能證明的範圍（歸屬、完整性、排序）與不能證明的範圍（行為正確性、政策正當性）。

## 問題：你的代理的審計軌跡

想像你部署了一個為 Contoso Travel 服務的 AI 代理。代理讀取客戶請求，呼叫航班 API 尋找選項，並代表客戶訂座。上季度，該代理處理了 50,000 筆訂單。

今日一位稽核人員來訪。他們問一個簡單問題：「請給我看你的代理做了什麼。」

你交出日誌檔案。稽核人員再提更難問題：「我怎麼知道這些日誌沒有被編輯過？」

這就是審計軌跡問題。如今多數代理部署依賴：

- <strong>應用程式日誌</strong>：由代理自身寫入，任何有檔案系統存取權的人都可編輯。
- <strong>雲端記錄服務</strong>：平台層級防篡改，但只有在稽核人員信任平台操作商才有效。
- <strong>資料庫交易日誌</strong>：適合記錄資料庫變更，但不適用於任意工具呼叫。

這些方法都無法在不要求稽核方信任某人（你、雲端供應商或資料庫廠商）的情況下回答問題。內部使用時此種信任往往可接受，但對於受規管的工作負載（金融、醫療保健、任何受歐盟 AI 法規約束的）則不然。

密碼學收據透過使簽署的聲明能夠獨立地
可驗證。稽核者仍然需要一個帶外的理由來信任簽署金鑰及
產生該聲明的組件。內嵌的金鑰證明自我一致性，
而非發行者身份或執行位置。

## 什麼是加密收據？

收據是一個 JSON 物件，記錄代理做了什麼，並附有數位簽名。

```mermaid
flowchart LR
    A[Agent invokes a tool] --> B[Build receipt payload]
    B --> C[Canonicalize JSON RFC 8785]
    C --> E[Ed25519 sign canonical bytes]
    E --> F[Receipt with signature]
    F --> G[Auditor verifies offline]
    G --> H{Signature valid?}
    H -- yes --> I[Signed statement is intact]
    H -- no --> J[Receipt rejected]
```

一份最簡收據長這樣：

```json
{
  "type": "agent.tool_call.v1",
  "agent_id": "contoso-travel-bot",
  "tool_name": "lookup_flights",
  "tool_args_hash": "sha256:a3f9c1...",
  "result_hash": "sha256:7b2e1d...",
  "policy_id": "contoso-travel-policy-v3",
  "timestamp": "2026-04-25T14:30:00Z",
  "sequence": 47,
  "previous_receipt_hash": "sha256:9d4e6a...",
  "signature": {
    "alg": "EdDSA",
    "sig": "c5af83...",
    "public_key": "8f3b2c..."
  }
}
```

有三個屬性能發揮作用：

1. <strong>簽名</strong>. 收據由代理的閘道使用 Ed25519 私鑰簽署。 任何持有對應公鑰的人都可以離線驗證該簽名。 依賴方必須固定該金鑰或從收據外的受信任註冊庫解析它。 篡改任何已簽署欄位會使簽名失效。

2. <strong>標準化編碼</strong>。簽署前，收據會使用 JSON 標準化方案（JCS，RFC 8785）序列化。這確保兩套實作只要輸出相同邏輯收據，就會產生完全相同的位元組序列。若無標準化編碼，不同 JSON 序列化器會為相同內容產生不同簽名。

3. <strong>雜湊鏈</strong>。該 `previous_receipt_hash` 欄位將每個收據連結到前一個收據。移除或重新排序收據會破壞所呈現的序列。偵測截斷或由簽署者控制的重寫也需要一個已釘選的當前鏈頭、獨立見證的檢查點，或經過驗證的封閉族群承諾。

這些屬性共同帶來三項保證：

- <strong>歸因於密鑰</strong>: 此密鑰簽署了此內容。組織或個人身份需要受信任的密鑰綁定。
- <strong>完整性</strong>：此內容自簽署後未曾更動。
- <strong>在已驗證序列中的排序</strong>: 此收據連結至該前一項目。

## 使用 Python 產生收據

你不需要特殊函式庫即可產生收據。加密基元廣泛可用，邏輯只有幾十行 Python 程式碼。

位於 `code_samples/18-signed-receipts.ipynb` 的實作練習會逐步示範整個流程。受版本控制的 `code_samples/18-signed-receipts.execution-receipt.json` 會記錄最新一次乾淨執行的精確筆記本雜湊、Python 環境、儲存格數量和檢查，而不會更改課程已儲存的輸出。摘要版本:

```python
import json
import hashlib
import base64
from nacl import signing
from jcs import canonicalize  # RFC 8785 canonical JSON

def b64url_nopad(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).decode("ascii").rstrip("=")

def sha256_canonical(obj) -> str:
    """SHA-256 of a Python object's JCS-canonical JSON form."""
    return f"sha256:{hashlib.sha256(canonicalize(obj)).hexdigest()}"

# Generate or load a signing key (in production, store in a key vault)
signing_key = signing.SigningKey.generate()
verify_key = signing_key.verify_key
TRUSTED_PUBLIC_KEYS = {b64url_nopad(bytes(verify_key))}  # pinned out of band by the verifier

# Build the receipt payload (no signature yet)
tool_args = {"origin": "SYD", "destination": "LAX"}
tool_result = [{"flight": "QF11", "price": 1850, "stops": 0}]

payload = {
    "type": "agent.tool_call.v1",
    "agent_id": "contoso-travel-bot",
    "tool_name": "lookup_flights",
    "tool_args_hash": sha256_canonical(tool_args),
    "result_hash": sha256_canonical(tool_result),
    "policy_id": "contoso-travel-policy-v3",
    "timestamp": "2026-04-25T14:30:00Z",
    "sequence": 0,
    "previous_receipt_hash": None,
}

# Canonicalize and sign the JCS bytes directly. PureEdDSA hashes internally.
canonical_bytes = canonicalize(payload)
signature_bytes = signing_key.sign(canonical_bytes).signature

# Attach a structured signature object.
receipt = {
    **payload,
    "signature": {
        "alg": "EdDSA",
        "sig": b64url_nopad(signature_bytes),
        "public_key": b64url_nopad(bytes(verify_key)),
    },
}
```

這就是整個簽署流程。筆記本中步驟會逐一引導。

## 驗證收據與檢測篡改

驗證是相反操作：

```python
import base64
import hashlib
from nacl import signing
from nacl.exceptions import CryptoError
from jcs import canonicalize

def b64url_decode(s: str) -> bytes:
    padding = "=" * ((4 - len(s) % 4) % 4)
    return base64.b64decode(s + padding, altchars=b"-_", validate=True)

def verify_receipt(receipt: dict, trusted_public_keys: set[str]) -> bool:
    # The signature is a structured object: {"alg", "sig", "public_key"}.
    if not isinstance(receipt, dict):
        return False
    sig_obj = receipt.get("signature")
    if not isinstance(sig_obj, dict) or sig_obj.get("alg") != "EdDSA":
        return False
    try:
        # An inline key proves only self-consistency. Trust is configured out of band.
        public_key = sig_obj.get("public_key")
        signature = sig_obj.get("sig")
        if not isinstance(public_key, str) or not isinstance(signature, str):
            return False
        if public_key not in trusted_public_keys:
            return False
        payload = {k: v for k, v in receipt.items() if k != "signature"}
        canonical_bytes = canonicalize(payload)
        verify_key = signing.VerifyKey(b64url_decode(public_key))
        verify_key.verify(canonical_bytes, b64url_decode(signature))
        return True
    except (CryptoError, TypeError, ValueError, KeyError, OverflowError):
        return False
```

此函式接收一張收據以及信賴方已釘選的金鑰集合，並回傳
`True` 僅當簽名在被接受的金鑰下有效時。驗證不需要
網絡呼叫，但金鑰的信任仍然是外部配置的決定。

要觀察篡改偵測如何運作，筆記本示範：

1. 產生有效收據並確認通過驗證。
2. 修改 `tool_args_hash` 欄位的一個位元組。
3. 重新執行驗證並發現失敗。

這是收據防篡改性質的實務示範：任何改動，無論多小，都會破壞簽名。

## 串接多步代理的收據鏈條

單一簽署收據保護一個行為。串接收據鏈保護序列行為。

```mermaid
flowchart LR
    R0[Receipt 0<br/>genesis] --> R1[Receipt 1]
    R1 --> R2[Receipt 2]
    R2 --> R3[Receipt 3]
    R1 -. previous_receipt_hash .-> R0
    R2 -. previous_receipt_hash .-> R1
    R3 -. previous_receipt_hash .-> R2
```

每份收據記錄前一份收據的雜湊。要隱密刪除第2份收據，攻擊者必須：

- 修改第3份收據的 `previous_receipt_hash` 欄位（會破壞第3份收據簽名），或者
- 偽造第3份被修改收據的新簽名（需掌握代理私鑰）。

如果私鑰受到保護，且驗證者釘選一個經獨立見證的鏈
頭，這些攻擊是可被偵測的。將金鑰刊登在每個收據內並不足夠
充足：簽署者或攻擊者可以提出不同的金鑰、重寫一個後綴，或
截斷鏈，除非依賴方擁有外部信任和完整性錨點。

筆記本示範：

1. 建立三份收據的鏈條。
2. 驗證每份收據的 `previous_receipt_hash` 與前一收據的真實雜湊相符。
3. 中間某筆收據遭篡改並演示鏈條正於該點斷裂。

這就是你如何產生一條審計追蹤，讓外部稽核員能在其
自己固定的簽發者金鑰與鏈檢查點下驗證，而無須信任你那個可變的日誌儲存庫。

## 收據能證明什麼（及不能證明什麼）

這是本課最重要部分。收據很強大，但其能力有限。

**收據證明三件事：**

1. <strong>歸屬</strong>：特定金鑰簽署了特定載荷。
2. <strong>完整性</strong>：載荷自簽署後未被改變。
3. <strong>在已呈現且已驗證的序列中的排序</strong>: 此收據連結到該前一項。

**收據不證明：**

1. <strong>正確性</strong>：代理的行為是否正確。錯誤答案同樣可被簽署收據支持。
2. <strong>政策合規</strong>：`policy_id` 所指政策是否實際被評估，或若評估會否允許此行為。收據紀錄的是宣稱，而非實際執行。
3. <strong>超越金鑰的身份</strong>：收據只說「此金鑰簽署此內容。」不代表「真人授權。」要將金鑰連結到人或組織，需另行身份基礎架構（如目錄、公鑰註冊等）。
4. <strong>輸入的真實性</strong>：若代理接收被操控的提示並據其行動，收據忠實記錄行為。收據處理的是輸入驗證之後，不是替代品。
5. <strong>執行或真實世界影響</strong>：呼叫後的收據記錄其發行者聲稱發生的事情。要證明承認或調和外部效應，需來自實際執行者或提供者邊界的證據。
6. <strong>完整性</strong>：缺失的收據可以表示被阻擋、遺漏、遺失，或未被記錄。只有在經過驗證的封閉族群內，缺席才會成為證據。
7. <strong>可信時間</strong>：簽名的時間戳證明簽署者攜帶了該值，而非該值是正確的。可信時間需要一個獨立的時間權威或有見證的檢查點。

這個界線重要有兩原因：

- 告訴你收據的用途：讓代理行為可被審計及防篡改，即使跨組織邊界。
- 告訴你還需要哪些額外層次：輸入驗證（第6課）、政策執行（下文簡述）、身份基礎架構（本課題外）。

常見誤解是認為「我們有收據」就代表「我們被治理」。事實不是。收據是基石。治理是你建立於基石之上的系統。

## 將核准者的簽名綁定到確切的操作

上述第 3 項值得成為獨立一節：一個操作憑證會寫「此金鑰簽署了此內容」，而不會寫「某個人授權了此事」。對於高風險操作（退款、刪除、電匯），由另一位核准者的簽名可以約束該具體操作。將該金鑰連結到一個人以及檢查該人是否在場仍然是獨立的職責。

後續的筆記本 `code_samples/human-authorization-receipts.ipynb` 新增了第二種收據類型，`human.approval.v1`，其封裝形狀與本課程的收據相同 (由 Ed25519 對其規範化的 JCS 位元組簽署的類型化載荷，且 `signature` 物件位於已簽署位元組之外). 批准者金鑰會簽署 <strong>完整的規範化動作及其摘要</strong>；代理者金鑰會簽署一份聲明，載有 <strong>相同的動作摘要</strong> 和 `parent_approval_ref`，批准的 `receipt_hash`，與你在上面建立的鏈中 `previous_receipt_hash` 的慣例相同。 一個 `verify_chain` 會在 <strong>分開釘選的金鑰註冊表</strong> (核准者金鑰與代理人金鑰), 因此程式碼路徑是共用的但授權實體永遠不會共用。

這項帶來的性質，謹慎陳述：*已鎖定的核准者金鑰簽署了這個精確的
動作，且代理金鑰後來簽署了一份載有相同動作摘要的聲明。*
這是有用的證據，但單憑它並不能證明該動作已被執行。為了
控制執行，該確切的批准也必須在
實際執行者邊界；未知的提供者結果必須保持未知，而不是
被盲目重試。筆記本的拒絕夾具測試收據鏈層：

- 篡改、混淆代理、任一方偽造的金鑰、以及格式錯誤的輸入;
- <strong>過時的授權</strong>: 一個仍然可驗證的簽名，但仍被拒絕，因為政策版本已變更、批准者的金鑰已從釘選的註冊表中輪換出來，或批准在提供的驗證時間之前已過期;
- <strong>摘要置換</strong>：有效簽署的行為收據指向<em>不同</em>標準化行動的<em>真實</em>核准。

每一項拒絕都有不同的理由，因此審核者在讀到拒絕時可以判斷是授權已失效還是所聲稱的操作改變了。驗證是唯讀且可重複的：它不會消耗批准或呼叫提供者。獨立的執行器需要具備持久且原子化的重放保護，並明確區分成功、失敗與不確定的結果。人類批准收據是本課程定義的一種教學性組合，而不是 `draft-farley-acta-signed-receipts` 定義的收據類型。

## 生產參考

本課 Python 程式碼刻意簡潔，你可以逐行理解運作。在生產環境，你有兩種選擇：

1. **直接建構在加密基元上。** 上述約 50 行程式碼已足夠多數用例。PyNaCl（Ed25519）和 `jcs`（標準化 JSON）皆為維護良好且經過審核的函式庫。

2. **使用生產級收據函式庫。** 多個開源專案實作相同模式並增添功能（金鑰輪替、批次驗證、JWK Set 分發、政策引擎整合）：
   - 簽署流程使用了獨立 IETF 草案（[`draft-farley-acta-signed-receipts`](https://datatracker.ietf.org/doc/draft-farley-acta-signed-receipts/)，第02版）定義的 JCS 和簽名範圍慣例。本課的扁平教育收據與草案中的 `{payload, signature}` 信封格式不同，且不宣稱為標準相容實作。該草案發佈了共通相容性測試集（[agent-governance-testvectors](https://github.com/ScopeBlind/agent-governance-testvectors)），用於目標其網路格式的實作。
   - Microsoft Agent Governance Toolkit 結合 Cedar 政策決策與收據；見該資源庫第33個教學範例，展示端到端實例。
   - `protect-mcp`（npm）與 `@veritasacta/verify`（npm）封裝 Node 環境的收據簽署與離線驗證功能，目標為封裝任一 MCP 伺服器以產生防篡改審計軌跡，包括持有共簽流程，其中暫停動作會產生綁定動作摘要的核准收據（桌面流程使用 WebAuthn 支援），與上文真人核准筆記本相同模式。
   - **[nobulex](https://github.com/arian-gogani/nobulex)** Python SDK (`pip install nobulex`) 提供相同 Ed25519 + JCS 簽署模式，含 LangChain 與 CrewAI 整合，且公布交叉驗證測試向量以及通過 [OWASP PR #2210](https://github.com/OWASP/CheatSheetSeries/pull/2210) 出版合規映射。
- **[EMILIA Protocol](https://github.com/emiliaprotocol/emilia-protocol)** 提供一個互補的精確行為強制層：可離線驗證的核准收據、綁定的 WebAuthn 或法定人數授權、在執行者邊界的一次性消耗，以及一條明確的不確定結果路徑。其框架適配器將收據視為必要的證據，而非外部效果已發生的證明。

自行開發與使用函式庫的抉擇，類似於開發自己 JWT 函式庫與使用經過測試的函式庫的決定：兩者合理；函式庫節省時間並降低審核範圍；自己開發則逼你徹底理解每個基元。本課教授自己開發路徑，提供任一選擇的基礎。

## 知識檢核

在開始實作練習前測試你的理解。

**1. 收據是以代理的私鑰 Ed25519 簽署。稽核人只有公鑰。稽核人能離線驗證收據嗎？**

<details>
<summary>答案</summary>

是的，密碼學驗證只需要公鑰和已簽名的位元組。該
審計者仍然必須在收據之外獨立取得並釘選（pin）被接受的公鑰。
在建立該信任配置後，不需要進行任何網絡呼叫。
</details>

**2. 攻擊者修改收據的 `policy_id` 欄位，聲稱其受更寬鬆政策管轄。簽名是對原始載荷。驗證時會發生什麼？**

<details>
<summary>答案</summary>


驗證失敗。簽名是基於原始有效載荷的正規化字節計算的；修改任何欄位都會改變這些字節，導致簽名無效。攻擊者需要私鑰來生成一個新的有效簽名，但他們沒有。
</details>

**3. 為何收據包括 `tool_args_hash` 和 `result_hash`，而不是原始參數和結果？**

<details>
<summary>回答</summary>

有兩個原因。首先，收據可能需要在會洩漏原始內容（個人身份資訊、商業數據）成為問題的環境中存檔或傳輸。雜湊能保持收據體積小且內容私密；審核者驗證雜湊是否與分開儲存的實際內容副本相符。其次，雜湊具有固定大小；無論輸入輸出多大，收據帶有雜湊後大小都是有界的。
</details>

**4. `previous_receipt_hash` 欄位將每張收據連接到前一張。如果攻擊者靜默刪除鏈中某張收據，什麼會變得無效？**

<details>
<summary>回答</summary>

下一個所呈交的收據不再連結到其預期的前一項，因此驗證
該呈交序列自該缺口起會失敗。如果簽署者掌握私鑰，
它可以改寫或截斷一段後綴。偵測到這點需要已固定的當前 head,
外部檢查點，或經過驗證的整體承諾。
</details>

**5. 一張收據驗證成功。這證明代理的行動是正確、合理，或符合法規嗎？**

<details>
<summary>回答</summary>

不是。在已釘選的金鑰與鏈式上下文下，有效的收據證明簽名歸屬，
內容完整性，以及與所呈示的前置項的連結。它並不證明該
操作是正確或已執行、政策已被評估、時間戳是
可信的，或記錄集合是完整的。這是本課程中最重要的界限。
</details>

## 練習作業

打開 `code_samples/18-signed-receipts.ipynb` 並完成以下四個部分：

1. <strong>第一部分</strong>：簽署你的第一份收據並驗證它。
2. <strong>第二部分</strong>：篡改收據並觀察驗證失敗。
3. <strong>第三部分</strong>：建立三張收據鏈並驗證鏈條的完整性。
4. <strong>第四部分</strong>：將此模式應用於使用 Microsoft Agent Framework 構建的代理：包裝工具調用以簽署收據，然後獨立驗證收據。

**延伸挑戰 1：** 擴展收據結構，添加你自己選擇的欄位（例如用於追蹤的請求 ID），更新正規化簽名邏輯以包含它，並確認收據仍可成功往返驗證。然後簽名後修改該欄位，確認驗證失敗。這強迫你理解正規化編碼的每一字節如何影響簽名。

**延伸挑戰 2：** 將兩張收據的正規化字節按確定性順序串接，進行 SHA-256 雜湊，並將產生的摘要作為第三張收據的一個新欄位嵌入，再簽名它。驗證三張收據仍可往返驗證。你剛建構了一種一步包含證明：持有第三張收據的任何人都能證明在簽名時前兩張收據存在，而無需公開它們內容。這是大規模可選擇披露收據（Merkle 承諾，RFC 6962）所使用的模式。

## 結論

密碼學收據為 AI 代理提供了審計軌跡，特點包括：

- <strong>在已釘選信任下可獨立驗證</strong>: 持有已接受的公鑰和已簽名的位元組的一方可以在不依賴任何服務的情況下進行驗證。
- <strong>防篡改</strong>：任何修改都使簽名無效。
- <strong>可攜帶</strong>：收據是一個小型 JSON 文件；可存檔、傳輸並在任處驗證。
- <strong>標準對齊</strong>：基於 Ed25519（RFC 8032）、JCS（RFC 8785）與 SHA-256，均為廣泛部署的原語。

它們不能取代輸入驗證、政策執行、執行者準入、結果證據、完整性控制或身份基礎設施。
它們是這些層的基礎。
在受規管或多組織的工作流程中，收據使特定的發行者聲明
可在稽核者自身的信任配置下獨立核查。

最重要的要點：收據證明某個特定的金鑰簽署了特定的
內容。隨附的時間戳記除非另有時間見證，否則是簽署者的主張。 一個
收據並不證明其內容為真、某個動作已被執行，或是
記錄集是完整的。務必嚴格區分這些差異。

## 生產檢查清單

當你準備從本課進階到實際環境部署簽署收據的代理時：

- [ ] **將簽名密鑰移出開發者筆記本。** 使用 Azure Key Vault、AWS KMS 或硬體安全模組。用以簽署收據的私鑰絕不可存在原始碼控制或應用機器上的純文字中。
- [ ] **建立驗證者金鑰信任。** 透過 JWK Set 或註冊表發佈金鑰，然後讓依賴方在個別收據之外釘選已接受的發行者身份、金鑰集和輪換政策。單憑內嵌金鑰並非信任根。
- [ ] **在外部錨定鏈條。** 定期將最新鏈頭哈希寫入公開記錄（日誌如 Sigstore Rekor、RFC 3161 時間戳機構，或第二內部系統），讓外部方能確認「此鏈條當時已存在」。
- [ ] **收據不可變存儲。** 使用僅增追加型 blob 儲存（如 Azure Storage 不可變策略、AWS S3 物件鎖定）防止內部人員在儲存層重寫歷史。
- [ ] **決定保存期限。** 許多合規要求多年保存。規劃收據成長（每張收據約 500 字節；一個每天呼叫 10K 次的代理一年產出約 1.8 GB）。
- [ ] **文件化收據不涵蓋的部分。** 收據證明歸屬、完整性與排序。你的運行手冊應明確列出哪些額外控管（輸入驗證、政策執行、速率限制、身份基礎設施）與收據一同構成治理態勢。

### 想進一步瞭解如何保護 AI 代理？

加入 [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) 與其他學習者交流，參加辦公時間，獲得你的 AI 代理疑問解答。

## 超越本課程

本課涵蓋單張收據簽署與雜湊鏈式序列。這些原語可組成你治理態勢成熟後可能遇到的多種進階模式：

- **選擇性披露。** 當收據欄位彼此獨立承諾（RFC 6962 風格 Merkle 樹），你可以向特定審核者揭露特定欄位，並證明其他欄位未變更，但不透露它們。當同一收據需同時滿足全面審計（要求完整性）與如 GDPR 這樣的數據最小化規範（要求審核者只能看到最少資訊）時非常有用。
- **收據撤銷。** 若簽名密鑰被洩露，你需要方法標記從某時間點開始該密鑰簽署的所有收據不再可信。標準模式是短期簽名密鑰加上公布的撤銷列表，或帶有撤銷條目的公開日誌。
- **雙邊／分割簽名收據。** 有些實作將簽署的有效載荷分為執行前（`authorization_*`）和執行後（`result_*`）兩部分，並各自獨立簽名，適合授權決策與觀察結果由不同行為者或不同時點產生。這可在本課程教的收據格式上加法組合。
- **有效載荷組合。** 收據封裝你放入 `result_hash` 的任何字節。現實中載荷常比單一工具調用結果更豐富：決策前推理（模型預測、考慮的選項、證據及其完整性、風險姿態、問責鏈、門檻結果）都可包含在載荷內，並由單張收據封裝。這保持收據格式簡潔，同時載荷架構可按領域演變。
- **跨實作一致性。** 多個獨立實作（Python、TypeScript、Rust、Go）針對共享測試向量互相驗證。若自行實作，對照公布向量可確保協定兼容性。
- **後量子遷移。** Ed25519 目前被廣泛部署，但並非抗量子攻擊。單靠 `alg` 標籤並不足以達成遷移：設定檔必須定義 ML-DSA 金鑰編碼、規範化已簽名位元組、驗證、依賴方政策、抗降級能力，以及遷移語義。在提出相容性主張之前，應針對共享向量規劃並測試雙重簽名遷移。

## 附加資源

- <a href="https://datatracker.ietf.org/doc/draft-farley-acta-signed-receipts/" target="_blank">IETF 網際網路草案：用於機器對機器存取控制的簽署決策收據</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/responsible-use-of-ai-overview" target="_blank">負責任 AI 概述 （Azure AI）</a>
- <a href="https://datatracker.ietf.org/doc/html/rfc8032" target="_blank">RFC 8032：愛德華曲線數位簽章演算法（EdDSA）</a>
- <a href="https://datatracker.ietf.org/doc/html/rfc8785" target="_blank">RFC 8785：JSON 規範化方案（JCS）</a>
- <a href="https://datatracker.ietf.org/doc/html/rfc6962" target="_blank">RFC 6962：憑證透明度</a>（選擇性披露收據用的 Merkle 樹結構）
- <a href="https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/tutorials/33-offline-verifiable-receipts.md" target="_blank">Microsoft Agent Governance Toolkit，教程 33：離線驗證決策收據</a>
- <a href="https://github.com/ScopeBlind/agent-governance-testvectors" target="_blank">本課程收據格式之跨實作一致性測試向量</a>（Apache-2.0）
- <a href="https://pynacl.readthedocs.io/" target="_blank">PyNaCl 文件</a>（Python 中的 Ed25519 實作）

## 前一課程

[建立本地 AI 代理](../17-creating-local-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->
