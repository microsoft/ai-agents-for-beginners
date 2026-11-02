---
name: local-ai-agents
license: MIT
---
# 使用 Foundry Local 和 Qwen 建立本地 AI 代理

> 伴隨 [Lesson 17 – Creating Local AI Agents](../../../17-creating-local-ai-agents/README.md) 的輔助技能。
> 用於協助學習者打造一個能獨立在自己機器上推理、調用工具及搜尋文件的代理 — 完全無雲端推理。所有建議都基於課程內容與可執行筆記本。
> 
> 

## 觸發條件

當學習者希望：
- 完全在設備端執行代理，為了隱私、成本或離線需求。
- 使用 **Foundry Local** 本地部署模型，並透過 OpenAI 兼容端點連接。
- 使用 **Qwen 函數呼叫** 模型來驅動可靠的本地工具調用。
- 新增 **本地 RAG**（Chroma）或 **本地 MCP 伺服器**。
- 設計一個 <strong>混合</strong> 本地/雲端路由策略。

## 核心心智模型

SLM 以隱私、成本與離線操作換取廣度。致勝策略是：**讓 SLM 負責協調，讓工具執行繁重任務。** 模型不需要<em>了解</em>整個程式碼庫，只需知道何時呼叫 `read_file` 和 `search_docs`。這符合 SLM 的強項（例如界定決策如工具選擇），避開其弱項（廣泛知識、長距多跳推理）。






## 為何選擇這些元件

- **Foundry Local** 提供 **OpenAI 兼容 HTTP 端點**，切換到本地代理只需改變 `base_url`（並用本地占位 API 金鑰）。它也會自動選擇最佳建構版本（CPU/GPU/NPU）。
- **Qwen** 模型經過函數呼叫訓練，穩定輸出格式良好的工具呼叫，使本地<em>聊天</em>模型變成本地<em>代理</em>。
- **Chroma** 內嵌運行並將向量存放磁碟，整個 RAG 流程（嵌入 → 存儲 → 檢索 → 推理）均保持本地。
- **MCP** 是傳輸協定，不是雲端服務：MCP 伺服器可在 `stdio` 上本地運行。

## 安裝必備

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

8GB 記憶體為實際最低需求；GPU/NPU 有助於性能但非必需。

## 需重複的主要模式

指引學習者閱讀筆記本
[`17-local-agent-foundry-local.ipynb`](../../../17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb)：

- <strong>沙盒工具</strong>：每個檔案工具均解析路徑並拒絕超出單一專案根目錄的路徑 — 即使本地，工具也只以使用者權限運行。
- <strong>工具呼叫迴圈</strong>：使用 OpenAI 工具架構註冊工具，於本地執行請求工具，將結果回饋，重複直到產出最終答案。
- **本地 RAG**：將文件添加到 Chroma 集合；`search_docs` 回傳前 k 筆區塊。
- **本地 MCP**：透過 `stdio` 連接本地伺服器；限定作用域到專案目錄並驗證其輸出。

## 混合路由（本地作為其中一個模型）

| 狀態 | 模型運行位置 |
|-----------|---------------|
| 敏感資料 / 離線 | 本地 SLM |
| 簡單、界定明確的任務 | 本地 SLM（經濟快速） |
| 複雜多跳推理且非敏感資料 | 雲端模型 |
| 雲端故障 | 本地 SLM（漸進退化） |

這呼應了 Lesson 16 的模型路由概念，將工作站列為其中一條路徑。優先設計可回退至本地的方案，讓代理效能降低而非直接失效。



## 助理控制規則

- 將所有檔案/工具操作限制在沙盒化專案目錄。
- 當學習者明確要求隱私/離線目標時，不將程式碼或資料送往雲端 — 保持整個流程本地化。
- 對 SLM 的品質設定現實預期；依賴工具與 RAG 多於模型本身的記憶知識。
- 注意 Lesson 17 無 Foundry 回應端點，因此雲端煙霧測試不適用 — 請透過本地執行筆記本驗證。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->