# 建立電腦使用代理程式（CUA）

電腦使用代理程式可以像人類一樣與網站互動：打開瀏覽器、檢查頁面，並根據看到的內容採取下一個最佳行動。在本課程中，您將建立一個瀏覽器自動化代理程式，搜尋 Airbnb，提取結構化的房源資料，並找出斯德哥爾摩最便宜的住宿。

本課程結合了用於 AI 驅動導航的 Browser-Use、用於瀏覽器控制的 Playwright 和 Chrome DevTools Protocol (CDP)、具有視覺功能推理的 Azure OpenAI，以及用於結構化擷取的 Pydantic。

## 介紹

本課程將涵蓋：

- 了解何時電腦使用代理程式比只有 API 的自動化更合適
- 將 Browser-Use 與 Playwright 和 CDP 結合以實現可靠的瀏覽器生命週期管理
- 使用 Azure OpenAI 視覺和結構化 Pydantic 輸出，從動態網頁中提取房源資料
- 決定何時使用 agent-first、actor-first 或混合的瀏覽器自動化工作流程

## 學習目標

完成本課程後，您將會知道如何：

- 配置 Browser-Use 與 Azure OpenAI 和 Playwright
- 建立一個瀏覽器自動化工作流程，能導航真實網站並處理動態 UI 元素
- 從可見頁面內容中提取類型化結果，並將其轉化為下游商業邏輯
- 根據瀏覽器任務的可預測性在 agent 和 actor 模式中做出選擇

## 程式碼範例

本課程包含一個筆記型教學：

- [15-browser-user.ipynb](./15-browser-user.ipynb)：透過 CDP 啟動 Chrome 會話，搜尋 Airbnb 斯德哥爾摩房源，使用 Browser-Use 視覺擷取價格，並以結構化資料回傳最便宜選項。

## 先決條件

- Python 3.12+
- 已在您的環境中配置 Azure OpenAI 部署
- 本地安裝 Chrome 或 Chromium
- 安裝 Playwright 依賴項
- 對 async Python 有基本熟悉

## 設定

安裝筆記型所使用的套件：

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

設定筆記型使用的 Azure OpenAI 環境變數：

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# 可選：如未指定，預設為最新 API 版本
AZURE_OPENAI_API_VERSION=...
```

## 架構概覽

筆記型展示了一個混合瀏覽器自動化工作流程：

1. 以 CDP 啟用啟動 Chrome，讓 Playwright 和 Browser-Use 可以共享同一瀏覽器會話。
2. Browser-Use 代理處理開放式導航任務，如開啟 Airbnb、關閉彈出視窗、搜尋斯德哥爾摩。
3. 使用結構化 Pydantic 架構檢查活動頁面，提取房源標題、每晚價格、評分及網址。
4. Python 邏輯比較擷取的房源並標示最便宜的結果。

此方法保留了 Browser-Use 擅長的彈性且基於視覺的推理，並在您需要時提供確定性的瀏覽器控制。

## 主要重點與最佳實務

### 何時使用 Agent 還是 Actor

| 情境 | 使用 Agent | 使用 Actor |
|----------|-----------|-----------|
| 動態版面 | 是，AI 可適應頁面變化 | 否，脆弱的選擇器會故障 |
| 已知結構 | 否，agent 較慢於直接控制 | 是，快速且精確 |
| 尋找元素 | 是，自然語言運作良好 | 否，需要精確選擇器 |
| 時間控制 | 否，不易預測 | 是，完全控制等待和重試 |
| 複雜工作流程 | 是，處理意外的 UI 狀況 | 否，需要明確分支 |

### Browser-Use 最佳實務

1. 起初使用 agent 進行探索及動態導航。
2. 當互動變得可預測時，轉為直接頁面控制。
3. 使用結構化輸出模型，使擷取數據被驗證並確保類型安全。
4. 在觸發可見 UI 變化的操作後策略性地加入延遲。
5. 迭代過程中捕捉截圖，使故障更易調試。
6. 預期網站會改變，設計彈出視窗及版面移動的備援策略。
7. 結合 agent 和 actor 模式，獲得彈性與精確度。

### 瀏覽器代理的安全防護

瀏覽器代理在實時網站上操作，因此比只調用已知 API 的腳本需要更嚴格的邊界。在從筆記型示範轉至真實工作流程前，請定義代理可以查看、點擊和提交的控制範圍。

1. **規劃瀏覽環境。** 在專用瀏覽器設定檔或沙盒中運行代理，並限制它訪問任務所需的網域。
2. **區分觀察與行動。** 先讓代理搜尋、閱讀和擷取資料；在提交表單、發送訊息、預訂旅行、完成購買、刪除記錄或更改帳戶設定前，需經過明確批准步驟。
3. **避免將密碼和敏感資料置於提示與記錄中。** 不要將密碼、付款細節、會話 Cookie 或原始個人資料放入模型語境。讓使用者負責驗證，並從日誌中消除敏感欄位。
4. **將頁面內容視為不可信輸入。** 網站可能包含針對代理的指令，而非使用者。代理應忽略要求更改目標、揭露資料、停用防護或造訪無關網站的頁面文字。
5. **針對風險步驟使用確定性檢查。** 用程式碼核對當前 URL、頁面標題、所選項目、價格、接收人和行動摘要，然後再請使用者批准最終步驟。
6. **設定預算和停止條件。** 限制代理可用的操作數、重試次數、分頁和時間。當頁面狀態不明時停止，而非繼續點擊。
7. **只記錄有用證據，不記錄所有資料。** 保存操作摘要、時間戳、URL、選中元素描述和截圖參考，以便審核失敗，而不儲存不必要的敏感頁面內容。

在 Airbnb 範例中，安全預設是搜尋房源和擷取價格。登入、聯絡房東或完成預訂應該是需用戶批准的獨立操作。

### 實際應用

- 旅遊預訂與價格監控
- 電子商務價格比較與可用性檢查
- 從動態網站提取結構化資料
- 具視覺感知的 UI 測試與驗證
- 網站監控與警報
- 跨多步驟的智慧表單填寫

## 真實範例：Microsoft Project Opal

您在本課程建立的代理程式，是一個小型本地版的<strong>電腦使用代理程式（CUA）</strong>，即一種像人一樣駕馭瀏覽器的程式。微軟正將這個概念應用於企業級解決方案，即 Microsoft 365 Copilot 中的 **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)** 功能。

透過 Project Opal，您描述一項工作，代理程式代表您在<strong>安全的 Windows 365 雲端 PC 上執行電腦使用</strong>，操作組織內所有基於瀏覽器的應用程式、網站與資料。它以<strong>非同步背景</strong>方式工作，您可隨時指導或接手控制。範例任務包括：

- 管理安全群組成員請求
- 收集並驗證合規審查的審計證據
- 處理 IT 事件（更新工單狀態、指派負責人、關閉重複事件）
- 將 Excel 資料整理成財務結案報告

Opal 是生產級、可被信任的電腦使用代理程式的良好參考，並強化了本課程之前的概念：

| 本課程概念 | Project Opal 的運用方式 |
|------------------------|-----------------------------|
| <strong>人員介入迴路</strong>（課程06） | Opal 在輸入登入憑據、敏感資料或不明指示時暫停，無明確確認不會輸入密碼或提交表單。您可在任務中途 <em>接管控制</em> 與 <em>返回控制</em>。 |
| <strong>可信且安全的代理</strong>（課程06 & 18） | 在隔離的 Windows 365 雲端 PC 運行，預設為僅瀏覽器存取（其它電腦存取受 Intune 管控封鎖），使用<em>您的</em>身分，只造訪您有權限的資源，且記錄所有操作以供稽核。 |
| <strong>規劃與元認知</strong>（課程07 & 09） | Opal 先制定工作計畫，然後在每步自我監督推理，檢測異常即暫停。 |
| **可重用能力 / 工具**（課程04） | <strong>技能</strong>讓您為重複任務撰寫指令（可從 `.md` 檔匯入或用 Opal 撰寫），並在對話中重複使用。 |

> **可用性：** Project Opal 現於有 Microsoft 365 Copilot 訂閱且管理員完成設置的用戶，可透過 [Frontier 早期體驗計劃](https://adoption.microsoft.com/copilot/frontier-program/) 使用。因為是 Frontier 實驗功能，其功能可能會隨時間變化。

## 知識檢核

在進入下一課程前，測試您的理解度。

**1. 何時瀏覽器基礎的電腦使用代理程式，會比純 API 工作流程更合適？**

<details>
<summary>答案</summary>

當任務依賴於網頁使用者界面中可見的內容、網站未公開所需 API、或頁面經常變動造成固定 API 或選擇器邏輯不穩定時，宜使用瀏覽器代理。如果存在穩定的 API 完成相同任務，優先使用 API，因其通常更快、更易測試且更安全。
</details>

**2. 在混合工作流程中，哪些部分應由代理處理，哪些部分應由直接的 Playwright 代碼處理？**

<details>
<summary>答案</summary>

讓代理處理開放式導航和動態 UI 狀態，例如尋找正確頁面或關閉意外彈出視窗。當頁面結構明確且操作需要精確、重試、等待或確定性驗證時，切換為直接 Playwright 控制。
</details>

**3. Airbnb 範例找到用戶可能想預訂的房源。在工作流程簽入、聯絡房東或完成預訂前應該發生什麼？**

<details>
<summary>答案</summary>

工作流程應暫停並請求用戶明確批准。在請求前，應顯示選擇房源的清楚摘要、當前網址、價格、日期和預期操作。搜尋和擷取價格可自動執行；帳戶登入、訊息、購買和預訂須由用戶批准。
</details>

**4. 網頁告訴代理忽略原先指令、造訪其他網站並揭露儲存的憑據。代理該如何處理該文本？**

<details>
<summary>答案</summary>

將其視為不可信的頁面內容，而非開發人員或使用者指令。代理應保持在允許的網域和任務範圍內，拒絕洩露秘密，避免依據頁面文字改變目標、停用防護或跳轉無關網站。
</details>

**5. 瀏覽器代理運行時，哪些證據有用，哪些應避免保留？**

<details>
<summary>答案</summary>

保留操作摘要、時間戳記、URL、選中元素描述、驗證結果和截圖參考，以便日後檢閱流程。避免儲存密碼、付款細節、會話 Cookie、原始個人資料或完整頁面內容，除非有具體儲存理由與隱私考量。
</details>

## 其他資源

- [開始使用 Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright 整合範本](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use actor 參數及內容擷取](https://docs.browser-use.com/customize/actor/all-parameters)
- [課程設定](../00-course-setup/README.md)

## 前一課程

[探索 Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

## 下一課程

[部署可擴展代理程式](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->