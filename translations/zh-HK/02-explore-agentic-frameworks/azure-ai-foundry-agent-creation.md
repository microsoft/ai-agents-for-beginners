# Microsoft Foundry 代理服務開發

在本練習中，您將使用 [Microsoft Foundry 入口網站](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) 的 Microsoft Foundry 代理服務工具來建立一個航班預訂代理。該代理能與用戶互動並提供航班資訊。

## 前置條件

完成此練習，您需要以下條件：
1. 一個具有有效訂閱的 Azure 帳戶。[免費建立帳戶](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)。
2. 您需要具備建立 Microsoft Foundry 中樞的權限或由他人為您建立。
    - 如果您的角色為參與者或擁有者，您可以按照本教程中的步驟操作。

## 創建 Microsoft Foundry 中樞

> **注意:** Microsoft Foundry 之前稱為 Azure AI Studio。

1. 請遵循這篇 [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) 部落格文章中的指引來創建 Microsoft Foundry 中樞。
2. 建立專案後，關閉任何顯示的提示訊息，並查看 Microsoft Foundry 入口網站中的專案頁面，該頁面應與下圖類似：

    ![Microsoft Foundry Project](../../../translated_images/zh-HK/azure-ai-foundry.88d0c35298348c2f.webp)

## 部署模型

1. 在專案的左側面板中，於 <strong>我的資產</strong> 區段選擇 **模型 + 端點** 頁面。
2. 在 **模型 + 端點** 頁面中，於 <strong>模型部署</strong> 分頁，點擊 **+ 部署模型** 菜單，選擇 <strong>部署基礎模型</strong>。
3. 在清單中搜尋並選擇 `gpt-5-mini` 模型，然後確認部署。

    > <strong>注意</strong>：降低 TPM 可避免過度使用您所使用訂閱中可用的配額。

    ![Model Deployed](../../../translated_images/zh-HK/model-deployment.3749c53fb81e18fd.webp)

## 建立代理

現在您已部署模型，即可建立代理。代理是一種會話式 AI 模型，可用於與用戶互動。

1. 在專案的左側面板中，在 <strong>建立與自訂</strong> 區段選擇 <strong>代理</strong> 頁面。
2. 點擊 **+ 建立代理** 以建立新代理。在 <strong>代理設定</strong> 對話方塊中：
    - 輸入代理名稱，例如 `FlightAgent`。
    - 確定選擇先前建立的 `gpt-5-mini` 模型部署。
    - 設定 <strong>指示</strong> 內容，作為代理要遵循的提示。以下為範例：
    ```
    You are FlightAgent, a virtual assistant specialized in handling flight-related queries. Your role includes assisting users with searching for flights, retrieving flight details, checking seat availability, and providing real-time flight status. Follow the instructions below to ensure clarity and effectiveness in your responses:

    ### Task Instructions:
    1. **Recognizing Intent**:
       - Identify the user's intent based on their request, focusing on one of the following categories:
         - Searching for flights
         - Retrieving flight details using a flight ID
         - Checking seat availability for a specified flight
         - Providing real-time flight status using a flight number
       - If the intent is unclear, politely ask users to clarify or provide more details.
        
    2. **Processing Requests**:
        - Depending on the identified intent, perform the required task:
        - For flight searches: Request details such as origin, destination, departure date, and optionally return date.
        - For flight details: Request a valid flight ID.
        - For seat availability: Request the flight ID and date and validate inputs.
        - For flight status: Request a valid flight number.
        - Perform validations on provided data (e.g., formats of dates, flight numbers, or IDs). If the information is incomplete or invalid, return a friendly request for clarification.

    3. **Generating Responses**:
    - Use a tone that is friendly, concise, and supportive.
    - Provide clear and actionable suggestions based on the output of each task.
    - If no data is found or an error occurs, explain it to the user gently and offer alternative actions (e.g., refine search, try another query).
    
    ```
> [!NOTE]
> 有關詳細提示，您可以參考此[儲存庫](https://github.com/ShivamGoyal03/RoamMind)以獲得更多資訊。
    
> 此外，您也可以加入 <strong>知識庫</strong> 和 <strong>動作</strong>，增強代理提供更多資訊及根據用戶請求執行自動化任務的能力。本練習可跳過這些步驟。
    
![Agent Setup](../../../translated_images/zh-HK/agent-setup.9bbb8755bf5df672.webp)

3. 若要建立多 AI 代理，只需點擊 <strong>新代理</strong>。新建的代理將顯示在代理頁面上。


## 測試代理

在建立代理後，可以在 Microsoft Foundry 入口網站的遊樂場測試代理對用戶詢問的回應。

1. 在代理的 <strong>設定</strong> 面板頂部，選擇 <strong>在遊樂場試用</strong>。
2. 在 <strong>遊樂場</strong> 面板中，您可以在聊天視窗輸入查詢與代理互動。例如，您可以要求代理搜尋 28 日從西雅圖到紐約的航班。

    > <strong>注意</strong>：代理可能不會提供準確回應，因為本練習未使用即時資料。目的是測試代理基於指示理解並回應用戶查詢的能力。

    ![Agent Playground](../../../translated_images/zh-HK/agent-playground.dc146586de715010.webp)

3. 測試代理後，您可以透過新增意圖、訓練資料和動作進一步自訂，以提升功能。

## 清除資源

當您完成測試代理後，可以刪除代理以避免產生額外費用。
1. 開啟 [Azure 入口網站](https://portal.azure.com)，並檢視您用來部署本練習中樞資源的資源群組內容。
2. 在工具列選擇 <strong>刪除資源群組</strong>。
3. 輸入資源群組名稱並確認刪除。

## 資源

- [Microsoft Foundry 文件](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry 入口網站](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry 快速入門](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Azure 上 AI 代理基礎](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->