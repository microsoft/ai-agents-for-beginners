# 變更日誌

本檔案記錄了 **AI Agents for Beginners** 課程所有重大的更新變更。

## [已發布] — 2026-07-14

本次發佈將課程從兩個已停用模型移除，將剩餘章節的筆記本遷移至穩定的 Microsoft Agent Framework API，並對 Python 筆記本在實時 Microsoft Foundry 部署環境中進行驗證。

### 變更項目

- **移除已停用模型（`gpt-4.1` / `gpt-4.1-mini` → `gpt-5-mini`）。** `gpt-4.1` 和 `gpt-4.1-mini` 均已停用（發佈退役日期為 **2026 年 10 月 14 日**）。課程中所有引用（文檔、`.env.example`、Python/.NET 筆記本與範例）均替換為未停用的 `gpt-5-mini`。第 16 課的模型路由範例維持使用 `gpt-5-nano`（小型）和 `gpt-5-mini`（大型）作對比。第三方供應文件（[15-browser-use/llms.txt](../../15-browser-use/llms.txt)），歷史 GitHub Models 文本，以及 `azure-openai-to-responses` 技能的能力說明保持不變。
- **第 14 課交接筆記本遷移至穩定 API。** [14-handoff.ipynb](./14-microsoft-agent-framework/code-samples/14-handoff.ipynb) 現在使用 `agent_framework.orchestrations.HandoffBuilder` 搭配 `.with_start_agent(...)`、`HandoffAgentUserRequest.create_response(...)`，基於 `event.type` 的串流，以及 `FoundryChatClient`（取代移除的 pre-1.0 `HandoffBuilder`/`ChatMessage`/`RequestInfoEvent` 符號）。
- **第 14 課人類在回路筆記本遷移至穩定 API。** [14-human-loop.ipynb](./14-microsoft-agent-framework/code-samples/14-human-loop.ipynb) 現在透過 `ctx.request_info(...)` + `@response_handler` 暫停（取代移除的 `RequestInfoExecutor` / `RequestInfoMessage` / `RequestResponse`），利用 `WorkflowBuilder(start_executor=..., output_executors=[...])` 建構，透過 `default_options={"response_format": ...}` 驅動結構化輸出，並使用腳本式回答使筆記本無需互動（無阻塞的 `input()`）。
- <strong>環境配置</strong> ([.env.example](../../.env.example))：將模型部署名稱切換為 `gpt-5-mini`；新增 `AZURE_AI_SMALL_MODEL` / `AZURE_AI_LARGE_MODEL`（第 16 課路由）和先前遺漏的 `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME`（第 15 課瀏覽器使用）。
- <strong>依賴項</strong> ([requirements.txt](../../requirements.txt))：將 `agent-framework`、`agent-framework-foundry` 和 `agent-framework-openai` 固定為 `~=1.10.0` 版本，以維持一致且驗證過的組合（1.11.0 含有本課程所用介面的實驗性破壞性更新）。

### 注意事項與已知限制

- **已在 Microsoft Foundry 實際環境中驗證。** Python 筆記本使用 `nbconvert` 無頭執行，並於 Microsoft Foundry 項目中使用 `gpt-5-mini`（第 16 課路由採用 `gpt-5-nano`）進行驗證。請在您自己的項目中部署等效非停用模型；筆記本從 `AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT` 讀取部署名稱。
- **部分章節仍需額外資源。** 第 05 課需 Azure AI Search；第 08 課 Bing 基礎流程（`04.python-agent-framework-workflow-aifoundry-condition.ipynb`）需 Bing 連線和 Microsoft Foundry Agent Service 托管工具；第 13 課（Cognee）及第 17 課（Foundry Local）需要各自的運行環境。

## [已發布] — 2026-07-13

本次發佈新增兩個章節，完善部署範圍——將代理擴展至 Microsoft Foundry 及縮減至單一工作站；另新增煙霧測試流程，更新課程導覽，新學習者技能，以及更新品牌形象。

### 新增

- **第 16 課 — 使用 Microsoft Foundry 部署可擴展代理。** 新章節 [16-deploying-scalable-agents/README.md](./16-deploying-scalable-agents/README.md) 與可運行筆記本 [16-python-agent-framework.ipynb](./16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb)，構建生產級客戶支援代理（工具、RAG、記憶、模型路由、回應快取、人類批准、評估門檻及 OpenTelemetry 追蹤），含開發／部署／運行期 Mermaid 圖，知識檢核，作業及挑戰。
- **第 17 課 — 使用 Foundry Local 與 Qwen 建立本地 AI 代理。** 新章節 [17-creating-local-ai-agents/README.md](./17-creating-local-ai-agents/README.md) 與筆記本 [17-local-agent-foundry-local.ipynb](./17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb)，建造全設備端工程助手（Qwen 函數調用透過 Foundry Local，沙箱文件工具，使用 Chroma 的本地 RAG，可選本地 MCP），含本地專用、本地 RAG、工具調用流程圖，知識檢核，作業及挑戰。
- **煙霧測試流程。** 新增 [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) 工作流程 [.github/workflows/smoke-test.yml](../../.github/workflows/smoke-test.yml)，並於 [tests/](./tests/README.md) 下增設各章節清單，涵蓋第 01、04、05 和 16 課可部署代理，提供索引 README 映射各清單至其章節與代理名稱。第 16 課新增「以煙霧測試驗證已部署代理」章節；第 01/04/05 課新增可選煙霧測試指引。
- **學習技能。** 新增代理技能於 `.agents/skills/`： [deploying-scalable-agents](./.agents/skills/deploying-scalable-agents/SKILL.md)、[local-ai-agents](./.agents/skills/local-ai-agents/SKILL.md)（涵蓋第 16 與 17 課內容），及 [testing-course-samples](./.agents/skills/testing-course-samples/SKILL.md)（如何針對實時 Microsoft Foundry / Azure OpenAI 平台驗證筆記本範例）。
- **筆記本驗證執行器。** 新增 [scripts/validate-notebooks.ps1](../../scripts/validate-notebooks.ps1)，可使用 `nbconvert` 無頭模式執行所有 Python 筆記本並輸出通過/失敗矩陣（及 `results.json`），自動偵測倉庫根目錄與 Python，預設排除非課程筆記本（`.venv`、`site-packages`、`translations`、技能模板資產）與 `.NET` 筆記本，支援 `-Filter`、`-Timeout`、`-List`、`-IncludeDotnet` 及 `-Python` 參數。
- **課程導覽。** 為第 11–15 課增加前後節連結（先前缺失），使整個課程連結由 00 延續至 18，雙向皆可。
- **新縮圖。** 第 16 與 17 課課程縮圖，以及更新後的倉庫社交圖像 [images/repo-thumbnailv3.png](./images/repo-thumbnailv3.png)（現強調兩個新章節及 `aka.ms/ai-agents-beginners` URL）。
- <strong>依賴項</strong> ([requirements.txt](../../requirements.txt))：為第 17 課新增了 `foundry-local-sdk` 及 `chromadb`。

### 變更項目

- **主檔 [README.md](./README.md) 課程表更新：** 第 16 與 17 課現已連結至其內容（先前顯示「即將推出」）；倉庫圖片更新為 `repo-thumbnailv3.png`。
- **[STUDY_GUIDE.md](./STUDY_GUIDE.md)**：新增第 16 及 17 課於逐課導覽及學習路徑，並加入「以煙霧測試驗證已部署代理」章節。
- **[AGENTS.md](./AGENTS.md)**：更新章節數量與說明（00–18），新增煙霧測試驗證章節，並加入第 16/17 課範例命名範例。
- **[18-securing-ai-agents/README.md](./18-securing-ai-agents/README.md)**：將「上一課」連結從第 15 課更正為指向第 17 課，完成課程連結閉環。
- **非停用模型的統一命名。** 將全課程中所有 `gpt-4o` / `gpt-4o-mini` 參考（文檔、`.env.example`、Python/.NET 筆記本及範例）替換為 `gpt-4.1-mini`——因 `gpt-4o`（所有版本）將於 2026 年退役。第 16 課模型路由範例維持使用 `gpt-4.1-mini`（小型）與 `gpt-4.1`（大型）作對比。Python 筆記本改為從環境變量（`AZURE_AI_MODEL_DEPLOYMENT_NAME` / `AZURE_OPENAI_DEPLOYMENT`）選擇模型，避免硬編碼模型名稱。

### 注意事項與已知限制

- **未在實際 Azure 環境執行。** 新章節筆記本為教學示例；請自行於 Microsoft Foundry / Foundry Local 環境中執行並驗證。煙霧測試流程需您部署該章節代理，並在 Foundry 項目範疇設定 Azure OIDC 機密 (`AZURE_CLIENT_ID`、`AZURE_TENANT_ID`、`AZURE_SUBSCRIPTION_ID`)，需具備 **Azure AI User** 角色。
- **第 17 課僅限本地使用。** 無 Foundry 回應端點，故煙霧測試動作不適用；請在工作站上執行筆記本驗證。

## [已發布] — 2026-07-06

本次發佈將課程遷移至 **Azure OpenAI Responses API**，統一產品命名為 **Microsoft Foundry** 與 **Microsoft Agent Framework (MAF)**，淘汰 GitHub Models，更新 SDK 版本，並新增本地模型與其他框架在 Foundry 上託管內容。

### 新增

- <strong>遷移技能</strong> — 安裝了 [`azure-openai-to-responses`](./.agents/skills/azure-openai-to-responses/SKILL.md) 代理技能（來源於 [Azure-Samples/azure-openai-to-responses](https://github.com/Azure-Samples/azure-openai-to-responses)），置於 `.agents/skills/` 下，含引用與掃描腳本。
- **Foundry Local（裝置端運行模型）** — [00-course-setup/README.md](./00-course-setup/README.md) 新增「替代提供者：Foundry Local」章節，涵蓋安裝（`winget` / `brew`）、`foundry model run`、`foundry-local-sdk`，以及透過 `OpenAIChatClient` 銜接 Microsoft Agent Framework 的 `FoundryLocalManager`。
- **Microsoft Foundry 上託管 LangChain / LangGraph 代理** — [14-microsoft-agent-framework/README.md](./14-microsoft-agent-framework/README.md) 新增該章節，以及可運行範例 [14-langchain-hosted-agent.py](../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py)，使用 `langchain-azure-ai[hosting]` 和 `ResponsesHostServer`（/responses 協議），基於 [Microsoft Learn](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents)。
- **Microsoft Project Opal** — [15-browser-use/README.md](./15-browser-use/README.md) 新增「真實案例：Microsoft Project Opal」章節，將 Opal 定位為企業電腦使用代理，並對應課程概念（人類在回路、信任/安全、規劃、技能）。
- **第二個第 02 課 Python 範例** — 新增 [02-python-agent-framework-azure-openai.ipynb](./02-explore-agentic-frameworks/code_samples/02-python-agent-framework-azure-openai.ipynb)（詳見「變更項目」中——自前 Semantic Kernel 筆記本遷移而來），且於課程 README 中新增連結。
- **於 [STUDY_GUIDE.md](./STUDY_GUIDE.md) 新增「模型與提供者」章節。**

### 變更項目

- **聊天完成 → Responses API（Python）。** 呼叫模型的範例從聊天完成切換至 Responses API（`client.responses.create(input=..., store=False)`，`resp.output_text`），使用 `OpenAI` 用戶端對穩定 Azure OpenAI `/openai/v1/` 端點（無需 `api_version`）。影響範例包括：
  - [06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb](./06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb)
  - [06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb](./06-building-trustworthy-agents/code_samples/06-human-in-the-loop.ipynb)
  - [04-tool-use/README.md](./04/tool-use/README.md) — 完整函數調用流程（工具結構展平成 Responses 格式，工具結果以 `function_call_output`、`max_output_tokens` 等返回）。

- **GitHub 模型 → Azure OpenAI。** GitHub 模型已被淘汰（將於 **2026 年 7 月退休**），且不支援 Responses API。所有 GitHub 模型的程式碼路徑已在 Python 和 .NET 範例中轉換為 Azure OpenAI / Microsoft Foundry：
  - Python：第 08 課工作流程筆記本（`01`–`03`）、第 14 課（`14-handoff`、`14-human-loop`、`hotel_booking_workflow_sample.py`）。
  - .NET：`01`–`04`、`07`、`08` `*-dotnet-agent-framework.cs` 及附屬 `.md` 文件，以及第 08 課 dotNET 工作流程筆記本/`.md`（`01`–`03`）現使用 `AzureOpenAIClient(...).GetOpenAIResponseClient(deployment).CreateAIAgent(...)` 加上 `AzureCliCredential`。
- **Semantic Kernel → Microsoft Agent Framework。** 先前的 `02-semantic-kernel.ipynb` 已重寫為使用 Microsoft Agent Framework 搭配 Azure OpenAI（Responses API），並重新命名為 `02-python-agent-framework-azure-openai.ipynb`。
- **統一標準為 `FoundryChatClient` + `as_agent`。** README 和筆記本程式碼中引用 `AzureAIProjectAgentProvider` 的部分，已統一為第 01 課及框架自有範例採用的標準模式：`FoundryChatClient(project_endpoint=..., model=..., credential=AzureCliCredential())` 配合 `provider.as_agent(...)`。更新範圍涵蓋第 02–14 課的 README 和筆記本（例如第 13 課記憶體、所有第 14 課筆記本、`11-agentic-protocols/code_samples/github-mcp/app.py`）。
- **產品命名。** 全文英語內容中重新命名：
  - 「Azure AI Foundry」/「Azure AI Studio」→ **Microsoft Foundry**
  - 「Azure AI Agent Service」→ **Microsoft Foundry Agent Service**
  - （未變更：「Azure OpenAI」、「Azure AI Search」、「Azure AI Inference」與環境變數名稱。）
- <strong>依賴</strong> ([requirements.txt](../../requirements.txt))：
  - 鎖定 `agent-framework>=1.10.0`、`agent-framework-foundry>=1.10.0`、`agent-framework-openai>=1.10.0`。
  - 鎖定 `openai>=1.108.1`（Responses API 的最低要求版本）。
  - 移除 `azure-ai-inference`（僅用於已遷移的 GitHub 模型範例）。
- <strong>環境配置</strong> ([.env.example](../../.env.example))：移除 GitHub 模型變數 (`GITHUB_TOKEN`、`GITHUB_ENDPOINT`、`GITHUB_MODEL_ID`)；新增 `AZURE_OPENAI_ENDPOINT`、`AZURE_OPENAI_DEPLOYMENT` 和可選的 `AZURE_OPENAI_API_KEY`；更新命名為 Microsoft Foundry。
- <strong>文件</strong> — 更新 [00-course-setup/README.md](./00-course-setup/README.md)、[AGENTS.md](./AGENTS.md)、[README.md](./README.md) 及 [STUDY_GUIDE.md](./STUDY_GUIDE.md) 以反映上述變更（環境變數設置、驗證程式碼段、提供者指引、命名方式）。

### 已移除

- 移除 GitHub 模型的入門步驟及環境變數，已由 Azure OpenAI / Microsoft Foundry 取代的設定文件中。

### 安全性 / 隱私（公開分享清理）

- 清除洩漏真實 **Azure 訂閱 ID**、資源群組 / 資源名稱，以及 Bing 連線 ID，還有開發者的 <strong>本地檔案路徑和使用者名稱</strong> 的 Jupyter 筆記本執行輸出；檔案包括：
  - `08-multi-agent/code_samples/workflows-agent-framework/dotNET/04.dotnet-agent-framework-workflow-aifoundry-condition.ipynb`
  - `08-multi-agent/code_samples/workflows-agent-framework/python/04.python-agent-framework-workflow-aifoundry-condition.ipynb`
  - `15-browser-use/15-browser-user.ipynb`
- 確認追蹤的英語內容中不再含有 API 密鑰、權杖、訂閱 ID 或個人路徑（剩餘 `GITHUB_TOKEN` 引用皆為工作流程中的 GitHub Actions Token 及第 11 課設置中 GitHub MCP 伺服器 PAT，兩者皆為合法且與 GitHub 模型無關）。

### 備註與已知限制

- **未執行/編譯。** 這些是為 API/命名正確性更新的教學範例；未曾在實際 Azure 資源上運行，且 .NET 範例未在此環境編譯。請自行在 Microsoft Foundry / Azure OpenAI 部署環境中驗證。
- **模型部署必須支援 Responses API。** 建議使用如 `gpt-4.1-mini`、`gpt-4.1` 或 `gpt-5.x` 的部署版本。較舊模型支援核心 Responses 功能，但非所有特性。
- **agent-framework 版本。** 範例以最新 MAF（`>=1.10.0`）為目標。創建 agent 的標準呼叫為 `client.as_agent(...)`；API 已根據框架公佈文件及已安裝版本驗證。若鎖定不同版本，請確認方法名稱（`as_agent` 與 `create_agent`）。
- **第 08 課工作流程筆記本 04** 特意保留 `AzureAIAgentClient`（來自 `agent-framework-azure-ai`），因其使用 Microsoft Foundry Agent Service 托管工具（Bing grounding、程式碼解析器）；該客戶端已基於 Responses 架構。
- **.NET 預設部署。** 兩個第 08 課 dotNET 工作流程範例先前硬編碼特定模型；現默認為 `AZURE_OPENAI_DEPLOYMENT`（`gpt-4.1-mini`）。若範例需要多模態/視覺輸入，請將 `AZURE_OPENAI_DEPLOYMENT` 設定為合適的模型。
- **Foundry Local** 提供 OpenAI 相容的 <strong>聊天補全</strong> 端點，旨在本地開發使用；完整的 Responses API 功能請使用 Azure OpenAI / Microsoft Foundry。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->