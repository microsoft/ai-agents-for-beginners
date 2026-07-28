# 變更紀錄

所有 **初學者 AI 代理人** 課程的重要變更都記錄於此檔案中。

## [已釋出] — 2026-07-14

此版本將課程從兩個新棄用的模型移除，將剩餘的課程筆記本遷移至穩定的 Microsoft Agent Framework API，並針對即時 Microsoft Foundry 部署驗證 Python 筆記本。

### 變更

- **從棄用模型轉移 (`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`)。** `gpt-4.1` 和 `gpt-4.1-mini` 現已棄用（公布退休日期為 **2026 年 10 月 14 日**）。將課程中所有提及的地方（文件、`.env.example`、Python/.NET 筆記本和範例）替換為非棄用的 `gpt-5-mini`。第 16 課的模型路由範例保留小/大模型對比，使用 `gpt-5-nano`（小）與 `gpt-5-mini`（大）。第三方檔案（[15-browser-use/llms.txt](../../15-browser-use/llms.txt)）、歷史 GitHub Models 文字與 `azure-openai-to-responses` 技能的能力註記則刻意未更動。
- **第 14 課轉接筆記本遷移至穩定 API。** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) 現使用 `agent_framework.orchestrations.HandoffBuilder` 及 `.with_start_agent(...)`、`HandoffAgentUserRequest.create_response(...)`、基於 `event.type` 的串流，以及使用 `FoundryChatClient`（取代已被移除的 pre-1.0 `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent` 符號）。
- **第 14 課人類監督筆記本遷移至穩定 API。** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) 現使用 `ctx.request_info(...)` + `@response_handler` 來暫停（取代已移除的 `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse`），使用 `WorkflowBuilder(start_executor=..., output_executors=[...])` 建構流程，透過 `default_options={"response_format": ...}` 來驅動結構化輸出，並以腳本化回答方式執行，使筆記本能無人值守執行（無需阻塞 `input()`）。
- <strong>環境配置</strong>（[.env.example](../../.env.example)）：模型部署名稱切換為 `gpt-5-mini`，新增 `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL`（第 16 課路由使用）及先前缺少的 `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`（第 15 課瀏覽器使用）。
- <strong>依賴套件</strong>（[requirements.txt](../../requirements.txt)）：將 `agent-framework`、`agent-framework-foundry` 以及 `agent-framework-openai` 鎖定至 `~=1.10.0` 以確保自洽且經過驗證的套件組合（1.11.0 版啟用了對這些課程所使用介面具破壞性變更的實驗性更新）。

### 注意事項與已知限制

- **已針對即時 Microsoft Foundry 驗證。** Python 筆記本以無頭方式使用 `nbconvert` 執行，並連結使用 `gpt-5-mini`（及第 16 課路由的 `gpt-5-nano`）的 Microsoft Foundry 專案。請於您自己的專案中部署等效的非棄用模型；筆記本將從 `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT` 讀取部署名稱。
- **部分課程仍需額外資源。** 第 05 課需要 Azure AI Search；第 08 課的 Bing 整合工作流（`04.python-agent-framework-workflow-aifoundry-condition.ipynb`）需要 Bing 連接及 Microsoft Foundry Agent Service 的託管工具；第 13 課（Cognee）及第 17 課（Foundry Local）需要其專屬執行環境。

## [已釋出] — 2026-07-13

此版本新增兩個完成部署主軸的課程—將代理擴展至 Microsoft Foundry，再縮小至單一工作站—還包括冒煙測試流程、更新的課程導覽、新的學習者技能與更新的品牌形象。

### 新增

- **第 16 課 — 使用 Microsoft Foundry 部署可擴展代理。** 新課程 [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) 及可執行筆記本 [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb)，構建生產環境客戶支援代理（工具、RAG、記憶、模型路由、回應快取、人類審核、評估門檻與 OpenTelemetry 追蹤），包含開發/部署/運行時的 Mermaid 圖、知識檢核、作業及挑戰。
- **第 17 課 — 使用 Foundry Local 與 Qwen 建立本地 AI 代理。** 新課程 [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) 及筆記本 [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb)，打造完全本地裝置的工程助理（透過 Foundry Local 呼叫 Qwen 函數、沙盒化檔案工具、本地 RAG 使用 Chroma、可選本地 MCP），附帶本地專用 / 本地 RAG / 工具呼叫圖示、知識檢核、作業及挑戰。
- **冒煙測試流程。** 新增 [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) 工作流程 [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml) 及每課的目錄於 [tests/](./tests/README.md)，涵蓋第 01、04、05 和 16 課的可部署代理，並附有索引 README，將各目錄映射至其課程及託管代理名稱。第 16 課新增「使用冒煙測試驗證部署代理」章節；第 01/04/05 課新增可選冒煙測試指標。
- **學習者技能。** 新增代理技能於 `.agents/skills/`：包含 [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md)、[local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md)（整合第 16 和 17 課指導）與 [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md)（如何針對即時 Microsoft Foundry / Azure OpenAI 環境驗證筆記本範例）。
- **筆記本驗證執行程式。** 新增 [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1)，可無頭執行所有 Python 筆記本並以 `nbconvert` 執行，輸出 PASS/FAIL 狀態矩陣（及 `results.json`）。自動偵測倉庫根目錄與 Python，預設排除非課程筆記本（`.venv`、`site-packages`、翻譯、技能模板資產）及 `.NET` 筆記本，支援 `-Filter`、`-Timeout`、`-List`、`-IncludeDotnet` 和 `-Python`。
- **課程導覽。** 為第 11 至 15 課補充了上一節/下一節連結（先前缺失），使整個課程在 00 至 18 課間雙向串連。
- **新縮圖。** 第 16 和 17 課新增課程縮圖，並更新檔案庫社群圖片 [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png)（現在宣傳兩個新課程及 `aka.ms/ai-agents-beginners` 連結）。
- <strong>依賴套件</strong>（[requirements.txt](../../requirements.txt)）：新增第 17 課所需的 `foundry-local-sdk` 和 `chromadb`。

### 變更

- **主體 [README.md](./README.md) 課程表：** 第 16 和 17 課現在連結到其內容（先前為「即將推出」）；倉庫圖片更新為 `repo-thumbnailv3.png`。
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)：** 新增第 16 和 17 課到逐課指導及學習路徑，並新增「使用冒煙測試驗證部署代理」章節。
- **[AGENTS.md](./AGENTS.md)：** 更新課程數量/說明（00–18 課）、新增冒煙測試驗證章節及第 16/17 課樣本命名示例。
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)：** 「上一課」現在指向第 17 課（先前為第 15 課），完成串連。
- **標準化非棄用模型參考。** 全課程將所有 `gpt-4o` / `gpt-4o-mini` 參考（包含文件、`.env.example`、Python/.NET 筆記本及範例）替換為 `gpt-4.1-mini`。`gpt-4o`（所有版本）將於 2026 年退役。第 16 課的模型路由範例維持小/大模型對比，使用 `gpt-4.1-mini`（小）及 `gpt-4.1`（大）。Python 筆記本現在從環境變數（`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`）讀取模型，而非硬編碼模型名稱。

### 注意事項與已知限制

- **未於即時 Azure 執行。** 新課程筆記本為教學範例；請在您的 Microsoft Foundry / Foundry Local 環境中執行並驗證。冒煙測試工作流程要求部署課程代理並設定具備 **Azure AI 使用者** 角色的 Foundry 專案範圍 Azure OIDC 機密（`AZURE_CLIENT_ID`、`AZURE_TENANT_ID`、`AZURE_SUBSCRIPTION_ID`）。
- **第 17 課僅限本地。** 無 Foundry Responses 端點，冒煙測試動作不適用；請透過工作站執行筆記本進行驗證。

## [已釋出] — 2026-07-06

此版本將課程遷移至 **Azure OpenAI Responses API**，統一產品命名為 **Microsoft Foundry** 和 **Microsoft Agent Framework (MAF)**，棄用 GitHub Models，升級 SDK 版本，並新增在本地模型及 Foundry 上託管其他框架的內容。

### 新增

- <strong>遷移技能</strong> — 安裝 [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) 代理技能（摘自 [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)），位於 `.agents/skills/`，包括其引用及掃描腳本。
- **Foundry Local（本地裝置執行模型）** — [00-course-setup/README.md](./00-course-setup/README.md) 新增「替代提供者：Foundry Local」章節，涵蓋安裝（`winget` / `brew`）、`foundry model run` 指令、`foundry-local-sdk`，以及透過 `OpenAIChatClient` 將 `FoundryLocalManager` 與 Microsoft Agent Framework 串接。
- **在 Microsoft Foundry 上託管 LangChain / LangGraph 代理人** — [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) 新增章節，以及可執行範例 [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py)，採用 `langchain-azure-ai[hosting]` 和 `ResponsesHostServer`（`/responses` 協定），基於 [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents) 教學。
- **Microsoft Project Opal** — [15-browser-use/README.md](./15-browser-use/README.md) 新增「實務範例：Microsoft Project Opal」章節，將 Opal 定義為企業電腦使用代理，並對應課程概念（人類監督、信任／安全、規劃、技能）。
- **第二個第 02 課 Python 範例** — 新增 [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb)（見「變更」— 自先前的 Semantic Kernel 筆記本遷移），並於課程 README 中加入連結。
- **新增 Models and Providers 章節** 於 [STUDY_GUIDE.md](./STUDY_GUIDE.md)。

### 變更

- **聊天室完成 → Responses API（Python）**。直接呼叫模型的範例改用 Responses API（`client.responses.create(input=..., store=False)`，`resp.output_text`），使用 `OpenAI` 客戶端連接至穩定版 Azure OpenAI `/openai/v1/` 端點（無 `api_version`）。受影響範例如下：
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04/tool-use/README.md) — 完整函數呼叫流程說明（將工具結構扁平化為 Responses 格式，工具結果以 `function_call_output`、`max_output_tokens` 等格式返回）。

- **GitHub 模型 → Azure OpenAI。** GitHub 模型已不建議使用（將於 **2026 年 7 月退役**），且不支援 Responses API。所有 GitHub 模型相關程式碼路徑已在 Python 及 .NET 範例中轉換為 Azure OpenAI / Microsoft Foundry：
  - Python：Lesson 08 工作流程筆記本（`01`–`03`）、Lesson 14（`14-handoff`、`14-human-loop`、`hotel_booking_workflow_sample.py`）。
  - .NET：`01`–`04`、`07`、`08` `*-dotnet-agent-framework.cs` 及相伴的 `.md` 文件，以及 Lesson 08 dotNET 工作流程筆記本/`.md`（`01`–`03`）現改用 `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` 結合 `AzureCliCredential`。
- **Semantic Kernel → Microsoft Agent Framework。** 先前的 `02-semantic-kernel.ipynb` 已重寫為使用帶有 Azure OpenAI（Responses API）的 Microsoft Agent Framework，並重新命名為 `02-python-agent-framework-azure-openai.ipynb`。
- **標準化使用 `FoundryChatClient` + `as_agent`。** README 及筆記本中引用 `AzureAIProjectAgentProvider` 的代碼已統一為 Lesson 01 和框架自有範例使用的標準化模式：`FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` 配合 `provider.as_agent(...)`。這些更新遍及 Lesson 02–14 的 README 和筆記本（例如 Lesson 13 記憶、所有 Lesson 14 筆記本、`11-agentic-protocols/code_samples/github-mcp/app.py`）。
- **產品命名。** 在英文內容中統一更名：
  - “Azure AI Foundry” / “Azure AI Studio” → **Microsoft Foundry**
  - “Azure AI Agent Service” → **Microsoft Foundry Agent Service**
  -（保持不變：“Azure OpenAI”、“Azure AI Search”、“Azure AI Inference” 以及環境變數名稱。）
- <strong>相依套件</strong> ([requirements.txt](../../requirements.txt))：
  - 鎖定 `agent-framework>=1.10.0`、`agent-framework-foundry>=1.10.0`、`agent-framework-openai>=1.10.0`。
  - 鎖定 `openai>=1.108.1`（Responses API 的最低版本）。
  - 移除 `azure-ai-inference`（只在已轉換的 GitHub 模型範例中使用）。
- <strong>環境配置</strong> ([.env.example](../../.env.example))：移除 GitHub 模型變數（`GITHUB_TOKEN`、`GITHUB_ENDPOINT`、`GITHUB_MODEL_ID`）；新增 `AZURE_OPENAI_ENDPOINT`、`AZURE_OPENAI_DEPLOYMENT` 與可選的 `AZURE_OPENAI_API_KEY`；命名更新為 Microsoft Foundry。
- <strong>文件</strong> — 更新了 [00-course-setup/README.md](./00-course-setup/README.md)、[AGENTS.md](./AGENTS.md)、[README.md](./README.md) 及 [STUDY_GUIDE.md](./STUDY_GUIDE.md) 以反映上述變更（設定環境變數、驗證片段、提供者指引、命名）。

### 已移除

- 移除 GitHub 模型入門步驟及相關環境變數設定文件（已被 Azure OpenAI / Microsoft Foundry 取代）。

### 安全性 / 隱私（公開分享清理）

- 清除在 Jupyter 筆記本執行輸出中洩漏的實際 **Azure 訂閱 ID**、資源群組與資源名稱以及 Bing 連線 ID，並移除開發者 <strong>本機檔案路徑與使用者名稱</strong>，包括：
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- 確認追蹤的英文內容中不再含有 API 金鑰、權杖、訂閱 ID 或個人路徑（保留的 `GITHUB_TOKEN` 參照是 GitHub Actions 工作流程的權杖以及 Lesson 11 設定中的 GitHub MCP 伺服器 PAT，兩者均為合法且與 GitHub 模型無關）。

### 備註與已知限制

- **未執行/編譯。** 這些為依 API/命名正確性更新的教學範例；並未針對現場 Azure 資源執行，且 .NET 範例未於此環境編譯。請根據您自己的 Microsoft Foundry / Azure OpenAI 部署環境驗證。
- **模型部署必須支援 Responses API。** 使用例如 `gpt-4.1-mini`、`gpt-4.1` 或 `gpt-5.x` 系列的部署。舊模型支援核心 Responses 功能，但不包含所有特性。
- **Agent-framework 版本。** 範例目標為最新 MAF（`>=1.10.0`）。標準的 agent 建立呼叫為 `client.as_agent(...)`；API 依框架的官方文件及已安裝版本驗證。如您鎖定不同版本，請確認方法是否存在（`as_agent` 或 `create_agent`）。
- **Lesson 08 工作流程筆記本 04** 故意保留 `AzureAIAgentClient`（來自 `agent-framework-azure-ai`），因其使用 Microsoft Foundry Agent Service 托管工具（Bing 查證、程式碼解譯器）；該方式已基於 Responses。
- **.NET 預設部署。** 兩個 Lesson 08 dotNET 工作流程範例過去硬編碼特定模型，現在預設為 `AZURE_OPENAI_DEPLOYMENT`（`gpt-4.1-mini`）。若範例依賴多模態／視覺輸入，請將 `AZURE_OPENAI_DEPLOYMENT` 設為適當模型。
- **Foundry Local** 提供相容 OpenAI 的 **Chat Completions** 端點，適用於本機開發；若需完整 Responses API 功能集，請使用 Azure OpenAI / Microsoft Foundry。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->