# 建立電腦使用代理（CUA）

電腦使用代理可以像人類一樣與網站互動：開啟瀏覽器、檢查頁面，並根據所見採取最佳下一步行動。在本課程中，您將構建一個瀏覽器自動化代理，搜尋 Airbnb，提取結構化的房源數據，並找出斯德哥爾摩最便宜的住宿。

本課程結合了 Browser-Use 用於 AI 驅動的導航、Playwright 與 Chrome DevTools 協議（CDP）用於瀏覽器控制、Azure OpenAI 用於視覺輔助推理，以及 Pydantic 用於結構化提取。

## 介紹

本課程將涵蓋：

- 了解何時電腦使用代理比純 API 自動化更合適
- 結合 Browser-Use、Playwright 與 CDP 以實現可靠的瀏覽器生命週期管理
- 使用 Azure OpenAI 視覺功能與結構化 Pydantic 輸出從動態網頁提取房源數據
- 判斷何時使用代理優先、演員優先或混合型瀏覽器自動化工作流程

## 學習目標

完成本課程後，您將能：

- 配置 Browser-Use，整合 Azure OpenAI 與 Playwright
- 建立瀏覽器自動化工作流程，導航真實網站並處理動態 UI 元素
- 從可見的頁面內容提取類型化結果並將其轉化為後續的業務邏輯
- 根據瀏覽器任務的可預測性選擇代理或演員模式

## 程式碼範例

本課程包含一個筆記本教學：

- [15-browser-user.ipynb](./15-browser-user.ipynb)：透過 CDP 啟動 Chrome，搜尋斯德哥爾摩的 Airbnb 房源，利用 Browser-Use 視覺功能提取價格，並將最便宜選項以結構化資料回傳。

## 先決條件

- Python 3.12 以上版本
- 已在環境中配置 Azure OpenAI 部署
- 本機已安裝 Chrome 或 Chromium
- 已安裝 Playwright 相依套件
- 對 async Python 有基本認識

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
# 選填：省略時預設為最新的 API 版本
AZURE_OPENAI_API_VERSION=...
```

## 架構概覽

筆記本展示了一種混合瀏覽器自動化工作流程：

1. Chrome 啟動時啟用 CDP，以便 Playwright 和 Browser-Use 共用同一瀏覽器會話。
2. Browser-Use 代理處理開放式導航任務，例如開啟 Airbnb、關閉彈跳視窗並搜尋斯德哥爾摩。
3. 使用結構化 Pydantic 架構檢查當前頁面，提取房源標題、每晚價格、評分和網址。
4. Python 邏輯比較提取的房源，並突顯最便宜的結果。

這種方法保留了 Browser-Use 擅長的靈活視覺推理，同時在需要時提供確定性的瀏覽器控制。

## 主要要點與最佳實踐

### 何時使用代理 vs 演員

| 情境 | 使用代理 | 使用演員 |
|----------|-----------|-----------|
| 動態布局 | 是，AI 可適應頁面變化 | 否，脆弱的選擇器可能失效 |
| 已知結構 | 否，代理比直接控制慢 | 是，快速且精確 |
| 尋找元素 | 是，自然語言效果好 | 否，需要精準選擇器 |
| 時間控制 | 否，不太可預測 | 是，完全掌握等待及重試 |
| 複雜工作流程 | 是，能處理意外 UI 狀態 | 否，需要明確分支 |

### Browser-Use 最佳實踐

1. 探索和動態導航時先用代理。
2. 互動可預測時切換到直接頁面控制。
3. 使用結構化輸出模型，確保提取資料經過驗證且類型安全。
4. 在觸發可見 UI 變化的操作後策略性添加延遲。
5. 迭代過程中拍攝截圖，便於除錯失敗。
6. 預期網站會變動，並設計彈跳視窗及版面變動的備援策略。
7. 混用代理與演員模式，兼得彈性與精確。

### 瀏覽器代理的安全護欄

瀏覽器代理在即時網站上運作，因此需要比僅呼叫已知 API 的腳本更嚴格的界限。在從筆記本示範轉向實際工作流程之前，務必定義代理可觀察、可點擊及可提交的範圍。

1. **限定瀏覽環境。** 在專用瀏覽器設定檔或沙盒中運行代理，並限制其訪問任務所需的域名。
2. **分離觀察與行動。** 先讓代理搜尋、閱讀與提取資料；提交表單、傳訊息、訂房、購買、刪除記錄或更改帳戶設置前必須取得明確批准。
3. **避免在提示與追蹤中暴露秘密。** 不要在模型上下文中放置密碼、付款細節、會話 Cookies 或個人敏感資料。讓使用者接手進行身份驗證，並從日誌中遮蔽敏感欄位。
4. **將頁面內容視為不可信輸入。** 網站可能包含針對代理的指令而非使用者。代理應忽略任何要求改變目標、透露資料、關閉安全措施或訪問無關網站的頁面文字。
5. **對風險步驟使用確定性檢查。** 確認目前網址、頁面標題、所選項目、價格、收件人及操作摘要後，再請使用者批准最終步驟。
6. **設定預算與停止條件。** 限制代理可執行的操作數、重試次數、分頁及時間（分鐘）。頁面狀態模糊時停止操作，不再盲目點擊。
7. **紀錄有用證據，而非全部紀錄。** 保留操作摘要、時間戳記、網址、所選元素描述及截圖參考，便於審核失敗原因，避免存儲不必要的敏感頁面內容。

在 Airbnb 範例中，安全的預設是搜尋房源並提取價格。登入、聯繫房東或完成訂房應為使用者另行批准的操作。

### 真實世界應用

- 旅遊訂房與價格監控
- 電商價格比較與庫存查詢
- 從動態網站提取結構化資料
- 具視覺感知的 UI 測試與驗證
- 網站監控與警報
- 多步驟流程中的智慧表單填寫

## 真實世界範例：Microsoft Project Opal

您在本課程建立的代理是“小型、在地”的 **電腦使用代理（CUA）** —— 一種像人一樣操作瀏覽器的程式。微軟將此概念應用於企業，打造了 **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**，為 Microsoft 365 Copilot 的功能之一。

有了 Project Opal，您描述任務後，代理會代表您在<strong>安全的 Windows 365 雲端 PC 上使用電腦操作</strong>，跨越組織內的基於瀏覽器的應用、網站和資料。它會<strong>非同步在背景執行</strong>，且您隨時可以引導或接管工作。範例工作包括：

- 管理安全群組成員請求
- 收集與驗證合規審核的稽核證據
- 分流 IT 事件（更新工單狀態、分配負責人、關閉重複）
- 彙整 Excel 資料成財務結案簡報

Opal 是一個有價值的參考範例，展示了什麼是<strong>生產級、值得信賴</strong>的電腦使用代理——並強化先前課程中的概念：

| 本課程概念 | Project Opal 的應用方式 |
|------------------------|-----------------------------|
| <strong>人機協同</strong>（第 06 課） | Opal 在需要登入憑證、敏感資料或指令模糊時暫停，且不在未獲得明確確認時輸入密碼或提交表單。您可以在任務中途<em>接管控制</em>並<em>交還控制</em>。 |
| <strong>可信任與安全代理</strong>（第 06、18 課） | 運行於隔離的 Windows 365 雲端 PC，預設僅允許瀏覽器操作（透過 Intune 強制其他電腦存取封鎖），使用<em>您的</em>身份僅取用授權範圍資源，並紀錄所有操作供審計。 |
| <strong>規劃與後設認知</strong>（第 07、09 課） | Opal 首先針對工作生成計劃，再在每步推理過程中監督自我，並在偵測異常時暫停。 |
| **可重用能力／工具**（第 04 課） | <strong>技能</strong>讓您以`.md`檔匯入或由 Opal 撰寫可重複使用的工作指令，並跨對話重用。 |

> **可用性：** Project Opal 目前向參與[Frontier 早期體驗計劃](https://adoption.microsoft.com/copilot/frontier-program/)並擁有 Microsoft 365 Copilot 訂閱的使用者開放，且需由管理者完成設定。由於這是 Frontier 的實驗性功能，功能隨時間可能調整。

## 額外資源

- [開始使用 Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Browser-Use Playwright 整合範本](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Browser-Use 演員參數與內容提取](https://docs.browser-use.com/customize/actor/all-parameters)
- [課程設定](../00-course-setup/README.md)

## 上一課

[探索 Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

## 下一課

[部署可擴展代理](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->