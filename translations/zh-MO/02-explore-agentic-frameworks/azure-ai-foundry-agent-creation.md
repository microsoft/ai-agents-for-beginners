# Microsoft Foundry 代理服務開發

在這個練習中，您將使用 [Microsoft Foundry 門戶](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst) 的 Microsoft Foundry 代理服務工具來建立一個航班預訂代理。該代理將能夠與用戶互動並提供有關航班的信息。

## 預備條件

完成此練習，您需要以下條件：
1. 一個具有有效訂閱的 Azure 帳戶。[免費創建帳戶](https://azure.microsoft.com/free/?WT.mc_id=academic-105485-koreyst)。
2. 您需要有建立 Microsoft Foundry 集線器的權限或已有他人為您建立。
    - 如果您的角色是貢獻者或擁有者，您可以按照本教程中的步驟操作。

## 建立 Microsoft Foundry 集線器

> **注意：** Microsoft Foundry 以前稱為 Azure AI Studio。

1. 請參考 [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst) 博客文章中的指引來建立 Microsoft Foundry 集線器。
2. 當您的專案建立完成後，關閉任何顯示的提示，並查看 Microsoft Foundry 門戶中的專案頁，畫面應該類似下圖：

    ![Microsoft Foundry Project](../../../translated_images/zh-MO/azure-ai-foundry.88d0c35298348c2f.webp)

## 部署模型

1. 在您專案左側窗格中的 <strong>我的資產</strong> 區域，選擇 **模型 + 端點** 頁面。
2. 在 **模型 + 端點** 頁中的 <strong>模型部署</strong> 標籤下，從 **+ 部署模型** 菜單選擇 <strong>部署基礎模型</strong>。
3. 在列表中搜尋 `gpt-5-mini` 模型，選擇後予以確認。

    > <strong>注意</strong>：降低 TPM 可避免過度使用您訂閱中的配額。

    ![Model Deployed](../../../translated_images/zh-MO/model-deployment.3749c53fb81e18fd.webp)

## 建立代理

現在您已經部署了模型，可以開始建立代理。代理是一個對話式 AI 模型，可以用來與用戶互動。

1. 在您專案左側窗格中的 <strong>建構與自訂</strong> 區域，選擇 <strong>代理</strong> 頁面。
2. 點擊 **+ 建立代理** 來建立新代理。在 <strong>代理設定</strong> 對話框中：
    - 輸入代理的名稱，例如 `FlightAgent`。
    - 確認之前建立的 `gpt-5-mini` 模型部署被選中。
    - 根據您希望代理遵循的提示設定 <strong>指示</strong>。範例如下：
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
> 詳細的提示，您可以查看 [此存儲庫](https://github.com/ShivamGoyal03/RoamMind) 以獲取更多資訊。
    
> 此外，您可以加入 <strong>知識庫</strong> 及 <strong>動作</strong>，提升代理提供更多資訊及基於用戶請求執行自動化任務的能力。在此練習中，您可以跳過這些步驟。
    
![Agent Setup](../../../translated_images/zh-MO/agent-setup.9bbb8755bf5df672.webp)

3. 若要建立新的多 AI 代理，只需點選 <strong>新代理</strong>。新建立的代理會顯示在代理頁面上。


## 測試代理

建立代理後，您可以在 Microsoft Foundry 門戶的遊樂場中測試它如何回應使用者查詢。

1. 在代理的 <strong>設定</strong> 窗格頂部，選擇 <strong>在遊樂場嘗試</strong>。
2. 在 <strong>遊樂場</strong> 窗格中，您可以通過聊天視窗輸入查詢與代理互動。例如，您可以要求代理搜尋 28 日從西雅圖飛往紐約的航班。

    > <strong>注意</strong>：代理可能無法提供精確回答，因為本練習未使用即時數據。目的是檢驗代理根據提供的指示理解並回應用戶查詢的能力。

    ![Agent Playground](../../../translated_images/zh-MO/agent-playground.dc146586de715010.webp)

3. 測試代理後，您可以進一步自訂，添加更多意圖、訓練數據及動作，以提升其功能。

## 清理資源

測試完成後，您可以刪除代理以避免額外費用。
1. 開啟 [Azure 入口網站](https://portal.azure.com)，並檢視您用於部署集線器資源所在的資源群組內容。
2. 在工具列上選擇 <strong>刪除資源群組</strong>。
3. 輸入資源群組名稱並確認刪除。

## 資源

- [Microsoft Foundry 文件](https://learn.microsoft.com/en-us/azure/ai-studio/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry 門戶](https://ai.azure.com/?WT.mc_id=academic-105485-koreyst)
- [Microsoft Foundry 入門指南](https://techcommunity.microsoft.com/blog/educatordeveloperblog/getting-started-with-azure-ai-studio/4095602?WT.mc_id=academic-105485-koreyst)
- [Azure 上 AI 代理基礎知識](https://learn.microsoft.com/en-us/training/modules/ai-agent-fundamentals/?WT.mc_id=academic-105485-koreyst)
- [Azure AI Discord](https://aka.ms/AzureAI/Discord)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->