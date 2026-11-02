---
name: local-ai-agents
license: MIT
---
# 使用 Foundry Local 和 Qwen 建立本地 AI 代理

> 與[課程 17 – 建立本地 AI 代理](../../../17-creating-local-ai-agents/README.md) 的輔助技能。
> 幫助學習者在他們自己的機器上構建一個能推理、調用工具並搜尋
> 文件的代理 — 完全不依賴雲端推理。每一項建議都基於課程內容和可運行的筆記本。




- 為了隱私、成本或離線原因，<strong>完全在設備上</strong>運行代理。
- 使用 **Foundry Local** 於本地部署模型，並透過 OpenAI 相容端點連接。
- 使用 **Qwen 函數調用** 模型來驅動可靠的本地工具調用。
- 添加 **本地 RAG**（Chroma）或者 **本地 MCP 服務器**。
- 設計 <strong>混合式</strong> 本地/雲端路由策略。




**讓 SLM 負責協調，並讓工具承擔繁重工作。** 模型不需要 <em>知道</em> 程式碼庫 — 它只需要知道什麼時候調用
策略：**讓 SLM 來協調，並讓工具負責繁重工作。** 模型不需要<em>知道</em>代碼庫——它只需知道何時呼叫
model does not need to *know* the codebase — it needs to know when to call
`read_file` 和 `search_docs`。這符合 SLM 的優勢（有界決策
如工具選擇）並避開其弱點（廣泛知識、長多跳推理）。


## 為什麼是這些特定部分

- **Foundry Local** 暴露了一個 **與 OpenAI 相容的 HTTP 端點**，因此雲端代理代碼只需更改 `base_url`（並使用本地的佔位符 API 金鑰）即可轉移。它還會自動為該設備選擇最佳的構建（CPU/GPU/NPU）。
- **Qwen** 模型訓練用於函數呼叫，並穩定傳出格式良好的工具呼叫 —— 這就是將本地聊天模型轉變為本地代理的關鍵。
- **Chroma** 在同一進程中運行並將向量存儲於磁盤，因此整個 RAG 流程（嵌入 → 存儲 → 檢索 → 推理）保持本地化。
- **MCP** 是一種傳輸工具，而非雲服務：MCP 伺服器可以透過 `stdio` 在本地運行。

## 基本設置要點

```bash
foundry model run qwen2.5-7b-instruct
foundry service status
```

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager("qwen2.5-7b-instruct")
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)  # local placeholder
```

約需 8 GB RAM 是現實的最低需求；GPU/NPU 有助益但非必須。

## 關鍵模式重現

指向學習者筆記本
[`17-local-agent-foundry-local.ipynb`](../../../17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb):

- <strong>受沙盒限制的工具</strong>：每個文件工具解析路徑，並拒絕任何單一專案根目錄外的請求 —— 即使在本地，工具也在使用者權限下運行。
- <strong>工具呼叫迴圈</strong>：使用 OpenAI 工具架構註冊工具，在本地執行請求的工具，反饋結果，重複直到得出最終答案。
- **本地 RAG**：將文件上傳至 Chroma 集合；`search_docs` 返回 top-k 片段。
- **本地 MCP**：通過 `stdio` 連接到本地伺服器；將其範圍限定於項目目錄並驗證其輸出。

## 混合路由（本地作為其中一個模型）

| 情境 | 運行地點 |
|-----------|---------------|
| 敏感數據／離線 | 本地 SLM |
| 簡單、範圍有限的任務 | 本地 SLM（廉價且快速） |
| 複雜的多步推理且非敏感數據 | 雲端模型 |
| 雲端故障 | 本地 SLM（漸進式降級） |

此方法反映第 16 課的模型路由概念，將工作站作為其中一條路由。優先考慮可回退到本地的設計，讓代理程式在品質上漸進下降，而非完全失效。



## 助理的防護措施

- 保持所有檔案／工具操作限定於沙盒化的項目目錄內。
- 當學習者的明確目標是隱私或離線時，切勿將代碼或數據發送到雲端 —— 保持整個流程在本地完成。
- 設置對 SLM 品質的合理預期；依賴工具和 RAG，而非模型的記憶知識。
- 注意第 17 課 <strong>沒有</strong> Foundry Responses 端點，因此雲端煙霧測試操作不適用 —— 請通過在本地運行筆記本進行驗證。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->