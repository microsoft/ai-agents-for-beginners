# 建立電腦使用代理程式 (CUA)

電腦使用代理程式可以像人類一樣與網站互動：透過開啟瀏覽器、檢查頁面，並根據所見採取最佳後續動作。在本課程中，您將建立一個瀏覽器自動化代理，搜尋 Airbnb、擷取結構化的房源資料，並找出斯德哥爾摩最便宜的住宿。

本課程結合了用於 AI 驅動導航的 Browser-Use、控制瀏覽器的 Playwright 和 Chrome DevTools 協議 (CDP)、具有視覺推理能力的 Azure OpenAI 以及用於結構化擷取的 Pydantic。

## 簡介

本課程將涵蓋：

- 了解何時電腦使用代理程式比僅使用 API 的自動化更合適
- 結合 Browser-Use 與 Playwright 和 CDP 進行可靠的瀏覽器生命週期管理
- 使用 Azure OpenAI 視覺以及結構化 Pydantic 輸出，從動態網頁擷取房源資料
- 決定何時使用代理優先、執行者優先或混合瀏覽器自動化流程

## 學習目標

完成本課程後，您將會知道如何：

- 設定 Browser-Use 搭配 Azure OpenAI 和 Playwright
- 建立瀏覽器自動化流程，導航真實網站並處理動態 UI 元素
- 從可見頁面內容擷取類型化結果，並將其轉換為後續業務邏輯
- 根據瀏覽器任務的可預測性，選擇代理模式或執行者模式

## 代碼範例

本課程包含一個筆記本教學：

- [15-browser-user.ipynb](./15-browser-user.ipynb)：透過 CDP 啟動 Chrome 會話，在 Airbnb 搜尋斯德哥爾摩房源，使用 Browser-Use 視覺擷取價格，並以結構化資料返回最便宜的選項。

## 前置條件

- Python 3.12+
- 環境中已配置 Azure OpenAI 部署
- 本機安裝 Chrome 或 Chromium
- 安裝 Playwright 相依套件
- 基本的非同步 Python 熟悉度

## 設定

安裝筆記本中使用的套件：

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

設定筆記本使用的 Azure OpenAI 環境變數：

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# 選擇性：省略時預設為最新的 API 版本
AZURE_OPENAI_API_VERSION=...
```

## 架構概述

筆記本展示混合瀏覽器自動化流程：

1. Chrome 啟用 CDP，讓 Playwright 和 Browser-Use 可共用相同的瀏覽器會話。
2. Browser-Use 代理處理開放式導覽任務，如開啟 Airbnb、關閉跳出視窗並搜尋斯德哥爾摩。
3. 使用結構化 Pydantic 架構檢查目前頁面，擷取房源標題、每晚價格、評分和 URL。
4. Python 邏輯比較擷取的房源，標示出最便宜的結果。

此方法保留了 Browser-Use 擅長的靈活視覺推理，同時在需要時提供決定性的瀏覽器控制。

## 重要重點與最佳實踐

### 何時使用代理與執行者

| 情境 | 使用代理 | 使用執行者 |
|----------|-----------|-----------|
| 動態版面 | 是，AI 可適應頁面變動 | 否，易被破壞的選擇器 |
| 已知結構 | 否，代理較慢 | 是，快速且精確 |
| 查找元素 | 是，自然語言效果佳 | 否，需要精確選擇器 |
| 定時控制 | 否，較不可預測 | 是，可完全控制等待與重試 |
| 複雜流程 | 是，可處理意外 UI 狀態 | 否，需明確分支邏輯 |

### Browser-Use 最佳實踐

1. 初期探索與動態導覽使用代理。
2. 當互動可預測時，切換為直接頁面控制。
3. 使用結構化輸出模型，確保擷取資料已驗證並類型安全。
4. 在觸發可見 UI 變化的動作後，策略性加入延遲。
5. 迭代時截取螢幕截圖，有助於除錯故障。
6. 預期網站會變動，為跳出視窗與版面變動設計後備策略。
7. 融合代理與執行者模式，兼顧靈活度與精準度。

### 瀏覽器代理的安全防護措施

瀏覽器代理在實時網站上操作，因此需要比僅呼叫已知 API 的腳本更嚴格的界限。在從筆記本示範轉為真實流程之前，需定義代理可瀏覽、點擊和提交的範圍。

1. **範圍限定瀏覽環境。** 在專用瀏覽器設定檔或沙盒中運行代理，並將其限制在任務所需的網域內。
2. **觀察與行動分離。** 先讓代理搜尋、閱讀與擷取資料；提交表單、發送訊息、預訂行程、完成購買、刪除紀錄、變更帳戶設定前，需取得明確批准步驟。
3. **避免將機密資訊置入提示與追蹤。** 不將密碼、付款資料、會話 cookie 或原始個資放入模型上下文。讓使用者接手認證並從日誌中遮蔽敏感欄位。
4. **將頁面內容視為不受信任的輸入。** 網站可能含有針對代理的指令，代理應忽略要求更改目標、顯示資料、關閉防護或前往無關網站的頁面文字。
5. **在風險步驟加入決定性檢查。** 用程式碼驗證目前 URL、頁面標題、選中項目、價格、收件人及動作摘要，並在最後步驟前請使用者批准。
6. **設定預算與停止條件。** 限制代理使用的動作數、重試次數、標籤數和分鐘數。當頁面狀態模糊時停止，而非持續點擊。
7. **記錄有用證據，不是全部東西。** 保留動作摘要、時間戳、URL、選中元素描述和截圖參考，方便檢查故障，避免存儲不必要的敏感頁面內容。

在 Airbnb 範例中，安全預設是搜尋房源並擷取價格。登入、聯繫房東或完成預訂應是使用者明確授權的單獨動作。

### 真實世界應用

- 旅遊訂票與價格監控
- 電子商務價格比對與庫存檢查
- 從動態網站結構化擷取資料
- 具視覺感知的 UI 測試與驗證
- 網站監控與警示
- 遍及多步驟流程的智慧表單填寫

## 真實案例：Microsoft Project Opal

您在本課建構的代理是一個小型本地版的 **電腦使用代理程式 (CUA)** — 一種以人類方式操作瀏覽器的程式。Microsoft 正將此理念帶入企業領域，推出 Microsoft 365 Copilot 的能力 **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**。

使用 Project Opal，您描述任務後，代理會利用 **受安全控管的 Windows 365 雲端 PC 上的電腦使用**，跨您組織的瀏覽器應用程式、網站和資料代表您執行。它 <strong>會在背景非同步運作</strong>，您可隨時導引工作或接管控制。範例任務包括：

- 管理安全群組成員請求
- 收集與驗證稽核證據以供合規審查
- IT 事件分流（更新工單狀態、指派負責人、關閉重複工單）
- 編輯 Excel 資料彙整財務結算簡報

Opal 是具 <strong>生產級且可信任</strong> 電腦使用代理的良好範例，並強化本課和前面課程的概念：

| 本課概念 | Project Opal 的應用 |
|------------------------|-----------------------------|
| <strong>人類介入流程</strong>（第 06 課） | Opal 會暫停要求登入憑證、敏感資料或模稜兩可的指示，且不會在未明確確認下輸入密碼或提交表單。您可在任務途中 <em>接管控制</em> 和 <em>歸還控制</em>。 |
| <strong>可信且安全的代理</strong>（第 06 與 18 課） | 運行於隔離的 Windows 365 雲端 PC，預設僅限瀏覽器存取（受 Intune 強制，阻絕其他電腦存取），使用 <em>您的</em> 身份，只存取您有權限的資源，記錄每個動作以供審計。 |
| <strong>計畫與後設認知</strong>（第 07 與 09 課） | Opal 先產生任務計畫，並在每步監督自身推理，若偵測異常會暫停。 |
| **可重複使用的能力／工具**（第 04 課） | <strong>技能</strong> 讓您編寫可重複任務指令（從 `.md` 檔案匯入或用 Opal 編寫），並可跨對話重複使用。 |

> **可用性：** Project Opal 目前在 [Frontier 早期體驗計畫](https://adoption.microsoft.com/copilot/frontier-program/)中，搭配 Microsoft 365 Copilot 訂閱對用戶開放，且必須由管理員完成設定。由於是實驗性 Frontier 功能，功能可能隨時間調整。

## 知識檢測

在進入下一課程前檢測您的理解。

**1. 何時瀏覽器為基礎的電腦使用代理比僅 API 工作流程更合適？**

<details>
<summary>答案</summary>

當任務依賴網頁 UI 可見內容、網站未提供所需 API，或頁面頻繁變動導致固定 API 或選擇器邏輯易破裂時，適合使用瀏覽器代理。如有穩定的 API，同任務則優先使用 API，因為速度較快、測試較易、安全性較高。
</details>

**2. 在混合流程中，代理與直接 Playwright 程式碼分別該處理哪些部分？**

<details>
<summary>答案</summary>

讓代理處理開放式導覽與動態 UI 狀態，如尋找合適頁面或關閉意外彈窗。當頁面結構已知，需精準控制動作、重試、等待或決定性驗證時，切換為直接 Playwright 控制。
</details>

**3. Airbnb 範例找到使用者可能想預訂的房源。流程在登入、聯絡房東或完成預訂前應做什麼？**

<details>
<summary>答案</summary>

流程應暫停並請求明確的使用者批准。請求前，應顯示選中房源、當前 URL、價格、日期及預定動作的明確摘要。搜尋與擷取價格可自主進行；帳戶存取、通訊、購買與預訂須使用者批准。
</details>

**4. 若網頁指示代理忽略原始指令，前往其他網站並揭露保存的憑證，代理應如何處理該文字？**

<details>
<summary>答案</summary>

將其視為不受信任的頁面內容，而非開發者或使用者指令。代理應保持在允許的網域與任務範圍內，拒絕揭露機密資訊，避免遵從更改目標、關閉防護機制或導向無關網站的頁面文字。
</details>

**5. 當瀏覽器代理執行時，哪些證據有用應保存？該避免保存什麼？**

<details>
<summary>答案</summary>

保存動作摘要、時間戳、URL、選中元素描述、驗證結果及截圖參考，以便回顧執行歷程。避免保存密碼、付款資訊、會話 cookie、原始個資或完整頁面內容，除非有明確的保留與隱私理由。
</details>

## 其他資源

- [開始使用 Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright 整合範本](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use 執行者參數及內容擷取](https://docs.browser-use.com/customize/actor/all-parameters)
- [課程設定](../00-course-setup/README.md)

## 前一課程

[探索 Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

## 下一課程

[部署可擴展代理](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->