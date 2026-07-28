# 建立電腦使用代理程式 (CUA)

電腦使用代理程式可以像人類一樣與網站互動：開啟瀏覽器、檢查頁面，並根據所見採取最佳下一步行動。在本課程中，您將建立一個瀏覽器自動化代理程式，搜尋 Airbnb，提取結構化的房源資料，並找出斯德哥爾摩最便宜的住宿。

本課程結合了 AI 導航的 Browser-Use、用於瀏覽器控制的 Playwright 和 Chrome DevTools Protocol (CDP)、支持視覺推理的 Azure OpenAI，以及用於結構化提取的 Pydantic。

## 介紹

本課程涵蓋：

- 了解什麼時候電腦使用代理程式比純 API 自動化更合適
- 結合 Browser-Use、Playwright 和 CDP 以實現可靠的瀏覽器生命週期管理
- 使用 Azure OpenAI 的視覺能力和結構化 Pydantic 輸出從動態網頁中提取房源資料
- 決定何時使用代理優先、執行者優先或混合瀏覽器自動化工作流程

## 學習目標

完成本課程後，您將能：

- 配置 Azure OpenAI 和 Playwright 的 Browser-Use
- 建立能夠導航實際網站並處理動態用戶界面元素的瀏覽器自動化工作流程
- 從可見頁面內容中提取類型化結果並將其轉換為下游業務邏輯
- 根據瀏覽器任務的可預測性在代理和執行者模式中做出選擇

## 範例程式碼

本課程包含一個筆記本教學：

- [15-browser-user.ipynb](./15-browser-user.ipynb)：透過 CDP 啟動 Chrome 工作階段，在 Airbnb 搜尋斯德哥爾摩的房源，使用 Browser-Use 視覺提取價格，並以結構化資料返回最便宜的選項。

## 先決條件

- Python 3.12+
- Azure OpenAI 部署已在您的環境中配置
- 本地已安裝 Chrome 或 Chromium
- 已安裝 Playwright 依賴
- 對 async Python 有基本認識

## 安裝設定

安裝筆記本中使用的套件：

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

設置筆記本使用的 Azure OpenAI 環境變量：

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# 可選：省略時預設為最新的 API 版本
AZURE_OPENAI_API_VERSION=...
```

## 架構概覽

筆記本展示了一種混合瀏覽器自動化工作流程：

1. Chrome 開啟並啟用 CDP，讓 Playwright 與 Browser-Use 共用相同瀏覽器工作階段。
2. Browser-Use 代理處理開放式導航任務，例如開啟 Airbnb、關閉彈出視窗和搜尋斯德哥爾摩。
3. 使用結構化的 Pydantic 綱要檢查當前頁面，以提取房源標題、每晚價格、評分與 URL。
4. Python 邏輯比較提取的房源並標示最便宜的結果。

此方法保留了 Browser-Use 擅長的具靈活性的基於視覺的推理，同時在需要時提供確定性的瀏覽器控制。

## 主要重點與最佳實踐

### 何時使用代理 vs 執行者

| 情境 | 使用代理 | 使用執行者 |
|----------|-----------|-----------|
| 動態佈局 | 是，AI 可適應頁面變化 | 否，易斷裂的選擇器會失效 |
| 已知結構 | 否，代理比直接控制慢 | 是，快速且精確 |
| 尋找元素 | 是，自然語言表現良好 | 否，需要精確的選擇器 |
| 時序控制 | 否，較不易預測 | 是，完全控制等待和重試 |
| 複雜工作流程 | 是，處理意外的 UI 狀態 | 否，需要明確分支 |

### Browser-Use 最佳實踐

1. 以代理開始進行探索和動態導航。
2. 當互動變得可預測時切換到直接控制頁面。
3. 使用結構化輸出模型，確保提取的資料經過驗證且具類型安全。
4. 在觸發明顯 UI 變化的操作後有策略地加入延遲。
5. 迭代過程中拍攝截圖，使錯誤更易調試。
6. 預期網站會變化，設計彈出視窗和佈局變動的備援策略。
7. 結合代理與執行者模式，兼得靈活與精確。

### 瀏覽器代理的安全防護

瀏覽器代理在實時網站上操作，因此比只調用已知 API 的腳本需要更嚴格的界限。在從筆記本示範過渡到實際工作流程前，需定義代理可瀏覽、點擊和提交內容的控制範圍。

1. **定義瀏覽範圍。** 在專用瀏覽器配置文件或沙盒中執行代理，並限制其訪問任務所需的網域。
2. **分離觀察與操作。** 先讓代理進行搜尋、閱讀和資料提取；提交表單、發送訊息、預訂、購買、刪除記錄或更改帳戶設置前需明確批准步驟。
3. **不要將機密放入提示和追蹤中。** 不要將密碼、付款資訊、會話 Cookie 或原始個人資料置於模型上下文。由使用者負責認證並從記錄中刪除敏感欄位。
4. **將頁面內容視為不可信輸入。** 網站上可能含有針對代理的指令，而非用戶。代理應忽略要求改變目標、揭露資料、停用防護措施或造訪無關網站的頁面文字。
5. **在風險步驟使用確定性檢查。** 以程式碼核實當前 URL、頁面標題、選中項目、價格、收件人與操作摘要，然後請用戶批准最終步驟。
6. **設定預算與停止條件。** 限制代理可使用的操作次數、重試次數、分頁及時間。當頁面狀態模糊不清時停止操作，不要繼續點擊。
7. **記錄有用證據，而非全部內容。** 保留操作摘要、時間戳、URL、選中元素描述和截圖參考，以便檢視失敗情況，避免儲存不必要的敏感頁面內容。

在 Airbnb 範例中，安全默認是搜尋房源並提取價格。登入、聯絡房東或完成預訂應是使用者另行同意的操作。

### 現實世界應用

- 旅遊預訂和價格監控
- 電子商務價格比較和存貨檢查
- 從動態網站提取結構化資料
- 視覺感知的 UI 測試和驗證
- 網站監控和警報
- 跨步驟流程的智慧表單填寫

## 現實示例：Microsoft Project Opal

您在本課程中建立的代理是<strong>電腦使用代理程式 (CUA)</strong> 的小型本地版本 —— 一種以人類方式驅動瀏覽器的程式。Microsoft 正在將這個想法引入企業，推出 Microsoft 365 Copilot 的<strong>[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)</strong> 功能。

透過 Project Opal，您描述任務，代理便使用<strong>在安全的 Windows 365 雲端 PC 上的電腦使用</strong>代表您操作，跨瀏覽器應用、網站和資料。它<strong>在背景中非同步運行</strong>，您隨時可以引導工作或接管控制。示例工作包括：

- 管理安全群組成員請求
- 收集和驗證合規性審核的審計證據
- IT 事件分類（更新工單狀態、指派負責人、關閉重複工單）
- 編制 Excel 資料至財務報告簡報

Opal 是參考建立<strong>生產級、值得信賴</strong>電腦使用代理程式的有力資源 —— 也強化了前面課程的概念：

| 本課程概念 | Project Opal 的應用 |
|------------------------|-----------------------------|
| **人機協作 (Lesson 06)** | Opal 在需登入認證、敏感資料或模糊指令時暫停，且絕不會在未明確同意下輸入密碼或提交表單。您可在任務中途<em>接管控制</em>與<em>歸還控制</em>。 |
| **值得信賴與安全代理 (Lesson 06 & 18)** | 運行於獨立的 Windows 365 雲端 PC，預設只限瀏覽器存取（其餘電腦資源受 Intune 強制管控），使用<em>您的</em>身份授權且記錄所有操作供審計。 |
| **規劃與元認知 (Lesson 07 & 09)** | Opal 先生成任務計劃，接著監督每步的推理，若發現疑似異常即暫停。 |
| **可重用能力 / 工具 (Lesson 04)** | <strong>技能</strong> 讓您為可重複任務撰寫指令（可從 `.md` 檔導入或用 Opal 撰寫），並在對話中重複使用。 |

> **可用性：** Project Opal 目前對參與 [Frontier 早期體驗計畫](https://adoption.microsoft.com/copilot/frontier-program/) 且擁有 Microsoft 365 Copilot 訂閱的用戶開放，系統管理員需完成設置。由於它是實驗性 Frontier 功能，功能可能隨時間改變。

## 其他資源

- [開始使用 Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use 與 Playwright 整合範本](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use 執行者參數與內容提取](https://docs.browser-use.com/customize/actor/all-parameters)
- [課程設定](../00-course-setup/README.md)

## 前一課

[探索 Microsoft 代理框架](../14-microsoft-agent-framework/README.md)

## 下一課

[部署可擴展代理](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->