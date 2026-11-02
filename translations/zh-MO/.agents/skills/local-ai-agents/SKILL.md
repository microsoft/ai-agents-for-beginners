---
name: local-ai-agents
license: MIT
---
# 使用 Foundry Local 和 Qwen 創建本地 AI 代理

> 與 [第17課 – 創建本地 AI 代理](../../../17-creating-local-ai-agents/README.md) 配套的技能。
> 用於幫助學習者構建一個能夠推理、調用工具並在他們自己的機器上完全獨立搜尋文檔的代理 — 無需雲端推論。所有建議均基於課程內容和可運行的筆記本。

> 

## 觸發條件

學習者希望在以下情況下啟動此技能：
- 完全<strong>在設備上運行</strong>代理，考慮到隱私、成本或離線需求。
- 使用 **Foundry Local** 於本地提供模型，並通過 OpenAI 相容端點連接。
- 使用 <strong>Qwen 函數調用</strong>模型驅動可靠的本地工具調用。
- 添加 **本地 RAG**（Chroma）或 **本地 MCP 服務器**。
- 設計 <strong>混合</strong> 本地/雲端路由策略。

## 核心心理模型

SLM 在範圍上做出取捨，換取隱私、成本和離線操作。取勝的策略是：**讓 SLM 進行編排，工具來做重工作。** 模型不需要<em>了解</em>代碼庫 — 它只需知道何時調用 `read_file` 和 `search_docs`。這發揮了 SLM 的優勢（有限決策如工具選擇），避開了它的弱點（廣泛知識，長距多跳推理）。






## 為何選擇這些具體部分

- **Foundry Local** 暴露 **OpenAI 相容的 HTTP 端點**，所以雲端代理程式碼只需更改 `base_url`（並使用本地占位 API 鍵）。它還會自動選擇機器上最佳的構建（CPU/GPU/NPU）。
- **Qwen** 模型針對函數調用訓練，並穩定發出格式良好的工具調用 — 這使本地<em>聊天</em>模型變成本地<em>代理</em>。
- **Chroma** 進程內運行並將向量存儲在磁碟上，因此整個 RAG 流程（嵌入 → 存儲 → 檢索 → 推理）均保持本地。
- **MCP** 是一種傳輸方法，而非雲端服務：MCP 服務器可通過 `stdio` 本地運行。

## 基本設置

```bash
foundry model run qwen2.5-7b-instruct
foundry service status
```

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager("qwen2.5-7b-instruct")
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)  # 本地佔位符
```

~8 GB RAM 是現實可行的最低要求；GPU/NPU 有助於性能，但非必需。

## 可複製的關鍵模式

引導學習者參考筆記本
[`17-local-agent-foundry-local.ipynb`](../../../17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb)：

- <strong>沙盒工具</strong>：每個文件工具解析路徑並拒絕位於單個專案根目錄之外的任何路徑 — 即使在本地，工具也在用戶權限下運行。
- <strong>工具調用循環</strong>：根據 OpenAI 工具架構註冊工具，本地執行請求的工具，將結果反饋，重複直到得到最終答案。
- **本地 RAG**：將文檔上傳至 Chroma 集合；`search_docs` 回傳 top-k 區塊。
- **本地 MCP**：通過 `stdio` 連接本地服務器；限定專案目錄範圍並驗證其輸出。

## 混合路由（本地作為模型之一）

| 情況 | 運行位置 |
|-----------|---------------|
| 敏感資料／離線 | 本地 SLM |
| 簡單、有限任務 | 本地 SLM（便宜、快速） |
| 非敏感資料的複雜多跳推理 | 雲端模型 |
| 雲端故障 | 本地 SLM（優雅降級） |

這與第16課中的模型路由思路相呼應，工作站作為其中一條路由。設計優先考慮回退到本地，讓代理表現下降而非徹底失效。



## 助理的防護措施

- 將每次文件／工具操作限定於沙盒專案目錄內。
- 在學習者明確追求隱私／離線目標時，不向雲端發送代碼或數據 — 保持整個流程本地。
- 對 SLM 質量設定合理期待；倚重工具和 RAG 而非模型的記憶知識。
- 注意第17課 <strong>沒有</strong> Foundry Responses 端點，因此雲端煙霧測試動作不適用 — 通過本地運行筆記本驗證。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->