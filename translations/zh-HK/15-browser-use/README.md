# 建立電腦使用代理程式 (CUA)

電腦使用代理程式能夠以與人類相同的方式與網站互動：開啟瀏覽器、檢查網頁，並根據所見採取最佳後續行動。在本課程中，你將建立一個瀏覽器自動化代理，搜尋 Airbnb、擷取結構化房源資料，並找出斯德哥爾摩最便宜的住宿。

本課程結合了用於 AI 驅動導航的 Browser-Use、Playwright 及 Chrome DevTools 協議 (CDP) 以控制瀏覽器、啟用視覺推理的 Azure OpenAI，與用於結構化擷取的 Pydantic。

## 介紹

本課程將涵蓋：

- 了解何時電腦使用代理比純 API 自動化更合適
- 結合 Browser-Use 與 Playwright 和 CDP 以實現可靠的瀏覽器生命週期管理
- 使用 Azure OpenAI 視覺和結構化 Pydantic 輸出從動態網頁擷取房源資料
- 判斷何時採用以代理優先、執行者優先或混合的瀏覽器自動化工作流程

## 學習目標

完成本課程後，你將學會如何：

- 配置 Browser-Use 結合 Azure OpenAI 和 Playwright
- 建立一個實際網站導覽的瀏覽器自動化工作流程並處理動態 UI 元素
- 從可見頁面內容提取類型化結果並轉換成下游業務邏輯
- 根據瀏覽任務的可預測性選擇代理或執行者模式

## 程式碼範例

本課程包含一個筆記本教學：

- [15-browser-user.ipynb](./15-browser-user.ipynb)：通過 CDP 啟動 Chrome 會話，搜尋 Airbnb 斯德哥爾摩房源，使用 Browser-Use 視覺擷取價格，並以結構化資料回傳最便宜的選項。

## 先決條件

- Python 3.12+
- 已在你的環境中配置 Azure OpenAI 部署
- 本地已安裝 Chrome 或 Chromium
- 已安裝 Playwright 相關依賴
- 基本非同步 Python 熟悉度

## 安裝設定

安裝筆記本中使用的套件：

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

設定筆記本中使用的 Azure OpenAI 環境變數：

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# 可選：省略時預設為最新的 API 版本
AZURE_OPENAI_API_VERSION=...
```

## 架構概述

筆記本示範混合瀏覽器自動化工作流程：

1. Chrome 以啟用 CDP 的方式啟動，使 Playwright 與 Browser-Use 能共用同一瀏覽器會話。
2. Browser-Use 代理處理開放式導航任務，如開啟 Airbnb、關閉彈出視窗及搜尋斯德哥爾摩。
3. 使用結構化 Pydantic 架構檢查當前頁面，擷取房源標題、每晚價格、評分與 URL。
4. Python 邏輯比較擷取到的房源並標示最便宜的結果。

這種方式兼具 Browser-Use 擅長的靈活視覺推理，同時在需要時提供確定性的瀏覽器控制。

## 主要重點與最佳實踐

### 何時使用代理 vs 執行者

| 情境 | 使用代理 | 使用執行者 |
|----------|-----------|-----------|
| 動態版面 | 是，AI 能適應頁面變動 | 否，脆弱選擇器可能會出錯 |
| 已知結構 | 否，代理較慢不及直接控制 | 是，快速且精準 |
| 定位元素 | 是，自然語言表達良好 | 否，需要精確選擇器 |
| 時序控制 | 否，較不具可預測性 | 是，完全控制等待與重試 |
| 複雜工作流程 | 是，能處理意外 UI 狀態 | 否，需要明確分支 |

### Browser-Use 最佳實踐

1. 以代理開始探索和動態導航。
2. 互動趨於可預測後改用直接頁面控制。
3. 使用結構化輸出模型，使擷取資料具驗證與類型安全。
4. 在觸發可見 UI 變化的動作後策略性加入延遲。
5. 迭代時擷取螢幕截圖，便於故障調試。
6. 預期網站會變，設計備用策略應對彈窗與版面變動。
7. 混合代理與執行者模式，以兼顧靈活與精準。

### 瀏覽器代理安全防護

瀏覽器代理運作在實時網站，需比純呼叫已知 API 的腳本更嚴格的邊界限制。從筆記本示範升級為實際工作流程前，先定義代理可檢視、點擊和提交的控制範圍。

1. **界定瀏覽環境範圍。** 在專用瀏覽器設定檔或沙箱中執行代理，限制於任務所需網域。
2. **區分觀察與操作。** 先讓代理搜尋、閱讀與擷取資料；提交表單、發訊息、訂旅遊、購買、刪除記錄或更改帳戶設定需額外明確批准。
3. **避免機密出現在提示與記錄中。** 不要將密碼、付款細節、會話 Cookie 或原始個人資料放入模型上下文。讓使用者進行身分驗證並從日誌中刪除敏感欄位。
4. **視頁面內容為不受信的輸入。** 網站可能包含針對代理的指令而非使用者指令。代理應忽略要求改變目標、揭露資料、停用防護或訪問無關網站的頁面文字。
5. **在風險步驟周圍採用確定性檢查。** 在請求使用者批准最終步驟前，用程式碼驗證當前 URL、頁面標題、選取項目、價格、收件人與行動摘要。
6. **設定使用預算與停止條件。** 限制代理可用的動作數、重試次數、分頁數與時間，頁面狀態不明確時停止而非持續點擊。
7. **保留有用證據，不是所有內容。** 儲存動作摘要、時間戳記、URL、所選元素描述與截圖參考，便於回顧錯誤，避免儲存不必要的敏感頁面內容。

在 Airbnb 範例中，安全的預設是搜尋房源並擷取價格。登入、聯絡房東或完成訂房應為獨立經使用者批准的動作。

### 真實世界應用

- 旅遊訂房與價格監控
- 電商價格比較與存貨檢查
- 從動態網站擷取結構化資料
- 視覺感知的 UI 測試與驗證
- 網站監控與警報
- 跨多步驟流程的智慧表單填寫

## 真實案例：微軟 Project Opal

你在本課程中建置的代理是 **電腦使用代理 (CUA)** 的小型本地版本──一種以人類方式驅動瀏覽器的程式。微軟以同樣理念推動企業場景，推出 Microsoft 365 Copilot 中的 **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)** 功能。

使用 Project Opal，你描述任務，代理即在安全的 Windows 365 雲端 PC 上以 <strong>電腦使用</strong> 模式代你於組織的瀏覽器應用、網站與資料中操作。它在後台 <strong>非同步運行</strong>，且你可以隨時引導或接管工作。範例任務包括：

- 管理安全群組成員請求
- 收集並驗證合規審查的稽核證據
- IT 事件分流（更新工單狀態、指派負責人、關閉重複）
- 編製 Excel 資料成財務結案簡報

Opal 是用於展現 **生產級、值得信賴** 電腦使用代理的有力參考，也鞏固本課程早期的概念：

| 本課程概念 | Project Opal 應用方式 |
|------------------------|-----------------------------|
| <strong>人機互動迴圈</strong> (課程 06) | Opal 會在登入憑證、敏感資料或不明指令時暫停，且絕不未經明確確認即輸入密碼或提交表單。你可在任務中途 <em>接管</em> 與 <em>歸還控制權</em>。 |
| <strong>可信與安全代理</strong> (課程 06 & 18) | 運行於隔離的 Windows 365 雲端 PC，預設僅能使用瀏覽器（其他電腦存取被 Intune 強制阻止），使用 <em>你的</em> 身分，只能存取你的授權範圍，並對每個動作皆有詳細操作紀錄以利稽核。 |
| <strong>規劃與元認知</strong> (課程 07 & 09) | Opal 先產生任務計劃，然後在每步驟監督自身推理並於發現可疑行為時暫停。 |
| **可重用能力／工具** (課程 04) | <strong>技能</strong> 讓你撰寫可重複使用的工作指令（從 `.md` 檔匯入或使用 Opal 撰寫），並在多個對話中重複使用。 |

> **可用性：** Project Opal 目前提供給訂閱 Microsoft 365 Copilot 的用戶，並且必須由管理員完成設定，屬 Frontier 早期存取計劃成員。由於是實驗性 Frontier 功能，功能可能會隨時間調整。

## 知識檢測

在進入下一課程前，測試你的理解度。

**1. 何時瀏覽器為基礎的電腦使用代理比純 API 工作流程更合適？**

<details>
<summary>答案</summary>

當任務依賴可見的網頁 UI、網站未公開必要 API，或頁面變動頻繁導致固定 API 或選擇器邏輯脆弱時，使用瀏覽器代理。如果有穩定 API 可用，通常偏好 API，因其速度更快、測試與安全性較佳。
</details>

**2. 混合工作流程中，哪些部分應由代理處理？哪些部分應由 Playwright 直接控制？**

<details>
<summary>答案</summary>

讓代理處理開放式導航與動態 UI 狀態，如尋找正確頁面或關閉意外彈窗；當頁面結構已知且操作需精準、重試、等待或確定性驗證時，切換為直接 Playwright 控制。
</details>

**3. Airbnb 範例中找到用戶可能想訂的房源。工作流程在登入、聯絡房東或完成訂房前應做什麼？**

<details>
<summary>答案</summary>

工作流程應暫停並徵求明確使用者批准，顯示選中房源、當前 URL、價格、日期及預期動作的明確摘要。搜尋與擷取價格可自主執行，帳戶存取、訊息、購買與訂房則須使用者批准。
</details>

**4. 頁面內容指示代理忽略原始指令、造訪其他網站並揭露儲存資訊。代理應如何處理該文字？**

<details>
<summary>答案</summary>

視為不受信的頁面內容而非開發者或使用者指令。代理應留在允許的網域與任務範圍內，拒絕透露機密，避免遵循改變目標、關閉防護或導向無關網站的頁面文字。
</details>

**5. 執行瀏覽器代理時，哪些證據適合保存，哪些應避免？**

<details>
<summary>答案</summary>

保留動作摘要、時間戳記、URL、所選元素描述、驗證結果與截圖參考，便於審查執行狀態。避免儲存密碼、付款細節、會話 Cookie、原始個人資料或完整頁面內容，除非有特定保存與隱私需求。
</details>

## 其他資源

- [開始使用 Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright 整合範本](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use 執行者參數與內容擷取](https://docs.browser-use.com/customize/actor/all-parameters)
- [課程設定](../00-course-setup/README.md)

## 前一課程

[探索 Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

## 下一課程

[部署可擴展代理](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->