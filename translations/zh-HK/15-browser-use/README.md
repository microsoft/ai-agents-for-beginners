# 建立電腦使用代理人（CUA）

電腦使用代理人可以像人一樣與網站互動：打開瀏覽器、檢查頁面，並根據所見採取下一步最佳行動。在本課程中，你將建立一個瀏覽器自動化代理人，它會搜尋 Airbnb，提取結構化的房源資料，並找出斯德哥爾摩最便宜的住宿。

本課程結合了使用 Browser-Use 進行 AI 驅動導航、Playwright 和 Chrome DevTools Protocol (CDP) 來控制瀏覽器、Azure OpenAI 來達成具視覺能力的推理，及 Pydantic 用於結構化資料提取。

## 介紹

本課程將涵蓋：

- 了解何時使用電腦使用代理人優於僅用 API 自動化
- 結合 Browser-Use、Playwright 和 CDP 以可靠管理瀏覽器生命週期
- 使用 Azure OpenAI 具視覺能力及結構化 Pydantic 輸出，從動態網頁提取房源資料
- 判斷何時採用代理人優先、行為者優先或混合瀏覽器自動化工作流程

## 學習目標

完成本課程後，你將了解如何：

- 配置 Browser-Use 並整合 Azure OpenAI 及 Playwright
- 建立一個瀏覽器自動化工作流程，導航真實網站並處理動態 UI 元素
- 從可見頁面內容提取類型化結果，並轉化為後續業務邏輯
- 根據瀏覽器任務的可預測性，選擇使用代理人還是行為者模式

## 程式碼範例

本課程包含一個筆記本教學：

- [15-browser-user.ipynb](./15-browser-user.ipynb)：利用 CDP 啟動 Chrome 瀏覽器，搜尋 Airbnb 斯德哥爾摩房源，使用 Browser-Use 視覺功能提取價格，並以結構化資料回傳最便宜選項。

## 先決條件

- Python 3.12+
- 在你的環境中配置好 Azure OpenAI 部署
- 本機安裝 Chrome 或 Chromium
- 安裝 Playwright 相關依賴
- 具備基本的非同步 Python 知識

## 安裝

安裝筆記本使用的套件：

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

設定筆記本使用的 Azure OpenAI 環境變數：

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# 可選：省略時預設為最新的 API 版本
AZURE_OPENAI_API_VERSION=...
```

## 架構概述

筆記本範例示範一個混合式瀏覽器自動化工作流程：

1. Chrome 以啟用 CDP 的方式啟動，讓 Playwright 和 Browser-Use 共享同一個瀏覽器工作階段。
2. Browser-Use 代理人處理開放式導航任務，如開啟 Airbnb、關閉彈窗和搜尋斯德哥爾摩。
3. 使用結構化 Pydantic 架構檢視活躍頁面，提取房源標題、每晚價格、評分和網址。
4. Python 邏輯比較抽取的房源並凸顯出最便宜的結果。

此方法保留了 Browser-Use 擅長的具視覺靈活推理，同時在需要時提供確定性瀏覽器控制。

## 主要重點和最佳實踐

### 何時使用代理人 vs 行為者

| 情境 | 使用代理人 | 使用行為者 |
|----------|-----------|-----------|
| 動態版面 | 是，AI 能適應頁面變化 | 否，脆弱的選擇器易失效 |
| 已知結構 | 否，代理人速度較慢不直控 | 是，快速且精確 |
| 尋找元素 | 是，自然語言效果好 | 否，需精確選擇器 |
| 時間控制 | 否，較少可預測性 | 是，對等待與重試完全控制 |
| 複雜工作流程 | 是，可處理意外 UI 狀態 | 否，需明確分支邏輯 |

### Browser-Use 最佳實踐

1. 一開始用代理人進行探索和動態導航。
2. 當互動可預測時，切換到直接頁面控制。
3. 使用結構化輸出模型，確保提取資料被驗證且類型安全。
4. 在觸發可見 UI 變更的操作後，有策略地加入延遲。
5. 迭代時捕捉截圖，方便除錯失敗狀況。
6. 預期網站會變動，並設計彈窗及版面漂移的備用策略。
7. 混用代理人與行為者模式，兼具靈活性與精準度。

### 瀏覽器代理人的安全護欄

瀏覽器代理人在即時網站上執行，需要比僅呼叫已知 API 的腳本更嚴格的界限。從筆記本示範移轉到真實工作流程前，請定義代理人可見、點擊和提交的範圍。

1. **限定瀏覽環境範圍。** 在專用瀏覽器配置檔或沙盒中執行代理人，限制其只限於任務所需的網域。
2. **將觀察與行動分開。** 先讓代理人搜尋、閱讀及提取資料；在提交表單、發送訊息、預訂旅程、完成購買、刪除記錄或更改帳戶設定前，必須有明確批准步驟。
3. **勿將機密放入提示與記錄。** 不要將密碼、支付資訊、會話 Cookie 或未經處理的個人資料置入模型上下文。讓使用者負責認證，並從日誌中刪除敏感欄位。
4. **視頁面內容為不可信輸入。** 網站可能包含針對代理人的指令，而非使用者。代理人應忽略任何要它改變目標、揭露資料、關閉防護措施或造訪無關網站的頁面文字。
5. **在高風險步驟設置確定性檢查。** 在請使用者批准最終步驟前，先用程式碼核實目前 URL、頁面標題、選中項目、價格、接收者與動作摘要。
6. **設定預算與停止條件。** 限制代理人操作次數、重試次數、分頁數和可用分鐘數。頁面狀態不明時應停止操作，而非繼續點擊。
7. **記錄有用證據，不用記錄全部。** 保留動作摘要、時間戳記、URL、選中元素描述與截圖參考，方便復盤失敗原因，不儲存不必要且敏感的頁面內容。

在 Airbnb 範例中，安全預設是搜尋房源並提取價格。登入、聯絡房東或完成訂房應是另行使用者核准的動作。

### 實際應用場景

- 旅遊預訂與價格監控
- 電子商務價格比較與存貨檢查
- 從動態網站結構化提取資料
- 具視覺能力的 UI 測試與驗證
- 網站監控與警示
- 跨多步驟流程的智能表單填寫

## 實際範例：Microsoft Project Opal

本課程中建立的代理人，是一個小型本地版本的<strong>電腦使用代理人（CUA）</strong>——一個如人般驅動瀏覽器的程式。微軟正將這個概念帶進企業端，以 **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**，這是 Microsoft 365 Copilot 的一項功能。

使用 Project Opal，你只要描述一個任務，代理人便能在你的安全 Windows 365 雲端 PC 上使用<strong>電腦使用</strong>技術，代理你操作組織內的瀏覽器應用程式、網站和資料。它<strong>在背景非同步運行</strong>，你可以隨時引導或接管工作。示例任務包括：

- 管理安全群組成員請求
- 收集並驗證合規審查用的稽核證據
- 分流 IT 事件（更新工單狀態、指派負責人、關閉重複）
- 編譯 Excel 數據製作財務結算簡報

Opal 是一個有用參考，展示何謂<strong>生產級且可信任</strong>的電腦使用代理人 —— 同時鞏固本課程先前的概念：

| 本課程中的概念 | Project Opal 的實踐方式 |
|------------------------|-----------------------------|
| <strong>人員介入迴圈</strong>（第06課） | Opal 在需要登入憑證、敏感資料或模糊指令時會暫停，絕不會在未經明確確認下輸入密碼或提交表單。你可於任務中途「接管控制」並「歸還控制」。 |
| <strong>可信且安全的代理人</strong>（第06與18課） | 於獨立的 Windows 365 雲端 PC 運行，預設只操作瀏覽器（其它電腦存取被封鎖，並以 Intune 強制執行），使用<em>你的</em>身分，只存取你被授權的資源，並記錄所有操作以利稽核。 |
| <strong>規劃與後設認知</strong>（第07與09課） | Opal 首先生成任務計劃，然後監督各步驟的內部推理，如發現可疑行為則暫停。 |
| **可重用能力 / 工具**（第04課） | <strong>技能</strong>讓你撰寫可重複任務的指令（可從 `.md` 檔匯入或使用 Opal 編輯），並在多次對話中重用。 |

> **可用性：** Project Opal 目前於[Frontier 早期體驗計畫](https://adoption.microsoft.com/copilot/frontier-program/)中提供給 Microsoft 365 Copilot 訂閱用戶，且需由管理員完成設定。因為它屬於 Frontier 實驗性功能，未來能力可能會變動。

## 額外資源

- [開始使用 Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright 整合範本](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use 行為者參數與內容提取](https://docs.browser-use.com/customize/actor/all-parameters)
- [課程安裝](../00-course-setup/README.md)

## 上一課

[探索 Microsoft 代理人框架](../14-microsoft-agent-framework/README.md)

## 下一課

[部署可擴充代理人](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->