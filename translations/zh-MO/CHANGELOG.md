# 變更日誌

所有對 **初學者的 AI 代理** 課程的重要變更都記錄在此檔案中。

## [已發佈] — 2026-07-14

此版本將課程從兩個新棄用的模型轉移，將剩餘課程手冊遷移到穩定的 Microsoft Agent Framework API，並針對實時 Microsoft Foundry 部署驗證 Python 筆記本。

### 變更

- **移除棄用模型 (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`)。** `gpt-4.1` 和 `gpt-4.1-mini` 現已棄用（正式退役日期為 **2026 年 10 月 14 日**）。已將所有課程參考（文件、`.env.example`、Python/.NET 筆記本和範例）替換為非棄用的 `gpt-5-mini`。第16課的模型路由範例透過 `gpt-5-nano`（小型）和 `gpt-5-mini`（大型）保持小型/大型對比。供應的第三方檔案（[15-browser-use/llms.txt](../../15-browser-use/llms.txt)）、舊有 GitHub Models 文字及 `azure-openai-to-responses` 技能的能力說明故意未做更動。
- **第14課交接筆記本遷移至穩定 API。** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) 現使用 `agent_framework.orchestrations.HandoffBuilder` 搭配 `.with_start_agent(...)`、`HandoffAgentUserRequest.create_response(...)`、基於 `event.type` 的串流及 `FoundryChatClient`（取代已移除的 pre-1.0 `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent` 符號）。
- **第14課人機互動筆記本遷移至穩定 API。** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) 現透過 `ctx.request_info(...)` 加 `@response_handler` 暫停（取代已移除的 `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse`），使用 `WorkflowBuilder(start_executor=..., output_executors=[...])` 建置，透過 `default_options={"response_format": ...}` 推動結構化輸出，且使用腳本化回答以便筆記本可無人值守運行（不阻塞 `input()`）。
- <strong>環境配置</strong> ([.env.example](../../.env.example))：模型部署名稱變更為 `gpt-5-mini`；新增 `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL`（第16課路由使用）及先前缺少的 `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`（第15課瀏覽器使用）。
- <strong>相依套件</strong> ([requirements.txt](../../requirements.txt))：將 `agent-framework`、`agent-framework-foundry` 和 `agent-framework-openai` 固定為 `~=1.10.0` 版本，確保一組自洽且驗證過的依賴（1.11.0 將引入這些課程所用介面的實驗性破壞性變更）。

### 備註與已知限制

- **已針對實時 Microsoft Foundry 驗證。** Python 筆記本在無頭模式下以 `nbconvert` 執行，對 Microsoft Foundry 專案使用 `gpt-5-mini` （第16課路由用 `gpt-5-nano`）。請在您自己的專案中部署等效非棄用模型；筆記本從 `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT` 讀取部署名稱。
- **某些課程仍需額外資源。** 第05課需 Azure AI Search；第08課 Bing 定向工作流程（`04.python-agent-framework-workflow-aifoundry-condition.ipynb`）需連接 Bing 與 Microsoft Foundry Agent Service 的託管工具；第13課（Cognee）及第17課（Foundry Local）需自有運行環境。

## [已發佈] — 2026-07-13

此版本新增兩個完成部署軌跡的新課程 — 將代理擴展到 Microsoft Foundry 及縮減至單一工作站 — 以及煙霧測試流程、更新過的課程導航、新學習者技能和更新的品牌。

### 新增

- **第16課 — 使用 Microsoft Foundry 部署可擴展代理。** 新課程 [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) 與可執行筆記本 [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb)，建立生產用客服代理（工具、RAG、記憶、模型路由、回應快取、人為審核、評估閘門與 OpenTelemetry 追蹤），包含開發／部署／運行 Mermaid 圖、知識檢核、作業及挑戰。
- **第17課 — 使用 Foundry Local 與 Qwen 建立本地 AI 代理。** 新課程 [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) 與筆記本 [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb)，打造完全裝置內工程助理（透過 Foundry Local 執行 Qwen 函數呼叫、沙盒化的檔案工具、本地 RAG 與 Chroma、可選本地 MCP），包含純本地／本地 RAG／工具呼叫圖、知識檢核、作業及挑戰。
- **煙霧測試流程。** 新的 [AI 煙霧測試](https://github.com/marketplace/actions/ai-smoke-test) 工作流程 [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml)，以及各課程的目錄於 [tests/](./tests/README.md)，涵蓋第01、04、05及16課的可部署代理，並有對應每個目錄至課程及託管代理名稱的索引 README。第16課新增「使用煙霧測試驗證部署代理」章節；第01/04/05課新增可選煙霧測試指引。
- **學習者技能。** 新增代理技能於 `.agents/skills/`： [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md)、[local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md)（封裝第16和17課指導）、及 [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md)（如何針對實時 Microsoft Foundry / Azure OpenAI 環境驗證筆記本範例）。
- **筆記本驗證執行器。** 新增 [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1)，能以 `nbconvert` 無頭執行所有 Python 筆記本並列印通過/失敗矩陣（及 `results.json`）。自動偵測倉庫根目錄及 Python，預設排除非課程筆記本（`.venv`、`site-packages`、`translations`、技能範本資產）及 `.NET` 筆記本，支援 `-Filter`、`-Timeout`、`-List`、`-IncludeDotnet` 和 `-Python`。
- **課程導航。** 為第11至15課新增上下課連結（之前缺少），使整個課程在 00 → 18 方向雙向鏈接。
- **新縮略圖。** 為第16和17課新增縮略圖，並更新倉庫社交圖片 [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png)（現宣傳兩個新課程及 `aka.ms/ai-agents-beginners` URL）。
- <strong>相依套件</strong> ([requirements.txt](../../requirements.txt))：為第17課新增 `foundry-local-sdk` 和 `chromadb`。

### 變更

- **主 [README.md](./README.md)** 課程表：第16和17課現連結至其內容（之前為「即將推出」）；倉庫圖片更新為 `repo-thumbnailv3.png`。
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**：將第16和17課加入逐課指南與學習路徑，並新增「使用煙霧測試驗證部署代理」章節。
- **[AGENTS.md](./AGENTS.md)**：更新課程數量及描述（00–18）、增加煙霧測試驗證章節，以及新增第16/17課範例命名示例。
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**：「上一課」現指向第17課（之前為第15課），完成鏈結。
- **非棄用模型的模型參考標準化。** 將課程所有 `gpt-4o` / `gpt-4o-mini` 參考（文件、`.env.example`、Python/.NET 筆記本和範例）全部更換為 `gpt-4.1-mini` — `gpt-4o`（所有版本）將於2026年退役。第16課模型路由範例透過 `gpt-4.1-mini`（小型）和 `gpt-4.1`（大型）保持小型/大型對比。Python 筆記本改從環境變數（`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`）選擇模型，而非硬編碼名稱。

### 備註與已知限制

- **未對實時 Azure 執行。** 新課筆記本為教育樣本；請在您自己的 Microsoft Foundry / Foundry Local 環境運行並驗證。煙霧測試工作流程要求您部署課程代理，並於 Foundry 專案範圍設定 Azure OIDC 秘密（`AZURE_CLIENT_ID`、`AZURE_TENANT_ID`、`AZURE_SUBSCRIPTION_ID`）並賦予 **Azure AI User** 角色。
- **第17課僅限本地。** 無 Foundry Responses 端點，故煙霧測試動作不適用；請在工作站執行筆記本進行驗證。

## [已發佈] — 2026-07-06

此版本將課程遷移至 **Azure OpenAI Responses API**，統一產品命名為 **Microsoft Foundry** 與 **Microsoft Agent Framework (MAF)**，退役 GitHub Models、更新 SDK 版本，並新增本地模型及在 Foundry 託管其他框架的內容。

### 新增

- <strong>遷移技能</strong> — 安裝 [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) 代理技能（來自 [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)）置於 `.agents/skills/`，包括參考及掃描腳本。
- **Foundry Local（裝置上運行模型）** — 在 [00-course-setup/README.md](./00-course-setup/README.md) 中新增「替代供應商：Foundry Local」章節，涵蓋安裝（`winget` / `brew`）、`foundry model run`、`foundry-local-sdk`，及透過 `OpenAIChatClient` 將 `FoundryLocalManager` 導入 Microsoft Agent Framework。
- **在 Microsoft Foundry 上託管 LangChain / LangGraph 代理** — 在 [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) 新增章節及可執行範例 [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py)，利用 `langchain-azure-ai[hosting]` 與 `ResponsesHostServer`（即 `/responses` 協議），基於 [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents)。
- **Microsoft Project Opal** — 在 [15-browser-use/README.md](./15-browser-use/README.md) 新增「實務範例：Microsoft Project Opal」章節，將 Opal 置於企業電腦使用助手定位，並對應課程概念（人機互動、信任/安全、規劃、技能）。
- **第二個第02課 Python 範例** — 新增 [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb)（見「變更」— 從前 Semantic Kernel 筆記本遷移），並於課程 README 中連結。
- <strong>新增模型與供應商</strong> 章節於 [STUDY_GUIDE.md](./STUDY_GUIDE.md)。

### 變更

- **聊天完成 → Responses API（Python）。** 直接呼叫模型的範例，從聊天完成遷移至 Responses API（`client.responses.create(input=..., store=False)`、`resp.output_text`），使用針對穩定 Azure OpenAI `/openai/v1/` 端點的 `OpenAI` 用戶端（無 `api_version`）。受影響範例包括：
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04/tool-use/README.md) — 完整函數呼叫操作流程（工具結構扁平化為 Responses 格式，工具結果以 `function_call_output`、`max_output_tokens` 等回傳）。

- **GitHub Models → Azure OpenAI。** GitHub Models 已被棄用（將於 **2026 年 7 月** 退役），並且不支援 Responses API。所有 GitHub Models 的程式碼路徑已轉換為 Azure OpenAI / Microsoft Foundry，覆蓋 Python 和 .NET 範例：
  - Python：第 08 課程工作流程筆記本（`01`–`03`）、第 14 課程（`14-handoff`、`14-human-loop`、`hotel_booking_workflow_sample.py`）。
  - .NET：`01`–`04`、`07`、`08` `*-dotnet-agent-framework.cs` 與配套 `.md` 文件，以及第 08 課程的 dotNET 工作流程筆記本/`.md`（`01`–`03`）現使用 `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` 搭配 `AzureCliCredential`。
- **Semantic Kernel → Microsoft Agent Framework。** 先前的 `02-semantic-kernel.ipynb` 已重寫為使用 Microsoft Agent Framework 與 Azure OpenAI（Responses API），並重新命名為 `02-python-agent-framework-azure-openai.ipynb`。
- **標準化為 `FoundryChatClient` + `as_agent`。** README 和筆記本程式碼中曾引用 `AzureAIProjectAgentProvider` 的部分，已統一為第一課與框架自身範例所用的標準範式：`FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` 配合 `provider.as_agent(...)`。已於第 02–14 課程 README 和筆記本更新（例如第 13 課記憶體、所有第 14 課筆記本、`11-agentic-protocols/code_samples/github-mcp/app.py`）。
- **產品命名。** 英文內容中全盤重新命名：
  - 「Azure AI Foundry」 / 「Azure AI Studio」→ **Microsoft Foundry**
  - 「Azure AI Agent Service」→ **Microsoft Foundry Agent Service**
  - （未變更：「Azure OpenAI」、「Azure AI Search」、「Azure AI Inference」，以及環境變數名稱。）
- <strong>相依性</strong> ([requirements.txt](../../requirements.txt))：
  - 鎖定版本為 `agent-framework>=1.10.0`、`agent-framework-foundry>=1.10.0`、`agent-framework-openai>=1.10.0`。
  - 鎖定版本為 `openai>=1.108.1`（為 Responses API 的最低要求）。
  - 移除 `azure-ai-inference`（僅用於已遷移的 GitHub Models 範例）。
- <strong>環境設定</strong> ([.env.example](../../.env.example))：移除 GitHub Models 變數（`GITHUB_TOKEN`、`GITHUB_ENDPOINT`、`GITHUB_MODEL_ID`）；新增 `AZURE_OPENAI_ENDPOINT`、`AZURE_OPENAI_DEPLOYMENT`，以及選用的 `AZURE_OPENAI_API_KEY`；更新命名為 Microsoft Foundry。
- <strong>文件</strong> — 更新 [00-course-setup/README.md](./00-course-setup/README.md)、[AGENTS.md](./AGENTS.md)、[README.md](./README.md)、[STUDY_GUIDE.md](./STUDY_GUIDE.md) 以符合以上更改（環境變數設定、驗證程式碼片段、提供者指引、命名）。

### 已移除

- 設定說明文件中 GitHub Models 的入門步驟和環境變數（已被 Azure OpenAI / Microsoft Foundry 取代）。

### 安全性／隱私（公開共享清理）

- 清除 Jupyter 筆記本執行輸出中洩漏的真實 **Azure 訂閱 ID**、資源群組 / 資源名稱及 Bing 連線 ID，以及開發者的 <strong>本機檔案路徑和用戶名</strong>，位置包括：
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- 確認追蹤的英文內容中不再有 API 金鑰、權杖、訂閱 ID 或個人路徑（剩餘的 `GITHUB_TOKEN` 參考是合法且與 GitHub Models 無關的，如工作流程中的 GitHub Actions 權杖與第 11 課設定中的 GitHub MCP 伺服器 PAT）。

### 備註與已知限制

- **未執行／未編譯。** 這些為教學範例，經過 API 與命名正確性更新；未在實際 Azure 資源上執行，且 .NET 範例未於此環境中編譯。請於您自己的 Microsoft Foundry / Azure OpenAI 部署環境中驗證。
- **模型部署必須支援 Responses API。** 使用諸如 `gpt-4.1-mini`、`gpt-4.1` 或 `gpt-5.x` 的部署。舊模型支援基本 Responses 功能，但非所有特色。
- **Agent-framework 版本。** 範例目標為最新的 MAF（`>=1.10.0`）。標準代理建立呼叫為 `client.as_agent(...)`；API 已根據框架公開文件和安裝的版本驗證。若鎖定不同版本，請確認方法是否存在（`as_agent` vs `create_agent`）。
- **第 08 課工作流程筆記本 04** 有意保留 `AzureAIAgentClient`（來自 `agent-framework-azure-ai`），因其使用 Microsoft Foundry Agent Service 托管工具（Bing 根據、程式碼解釋器）；本身已基於 Responses。
- **.NET 預設部署。** 之前第 08 課的兩個 dotNET 工作流程範例硬編碼特定模型，現皆采用 `AZURE_OPENAI_DEPLOYMENT`（預設為 `gpt-4.1-mini`）。若範例依賴多模態／視覺輸入，請將 `AZURE_OPENAI_DEPLOYMENT` 設為適當模型。
- **Foundry Local** 暴露 OpenAI 相容的 **Chat Completions** 端點，適用於本機開發；完整的 Responses API 功能則建議使用 Azure OpenAI / Microsoft Foundry。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->