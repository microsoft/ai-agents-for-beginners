# 🎯 使用 Azure OpenAI (Responses API) (.NET) 的規劃與設計模式

## 📋 學習目標

本筆記本展示使用 Microsoft Agent Framework 及 Azure OpenAI (Responses API) 在 .NET 中建構企業級智能代理的規劃與設計模式。您將學會創建能分解複雜問題、規劃多步驟解決方案並利用 .NET 企業功能執行複雜工作流程的代理。

## ⚙️ 前置條件與設定

**開發環境：**
- .NET 9.0 SDK 或更高版本
- Visual Studio 2022 或具備 C# 擴充功能的 VS Code
- 具備 Azure OpenAI 資源與模型部署的 Azure 訂閱
- Azure CLI — 使用 `az login` 登入

**必要依賴：**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**環境配置 (.env 檔案)：**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## 執行程式碼

本課程包含一個 .NET 單一檔案應用程式實作。執行方式如下：

```bash
# 令檔案可執行（Linux/macOS）
chmod +x 07-dotnet-agent-framework.cs

# 運行應用程式
./07-dotnet-agent-framework.cs
```

或使用 dotnet run 指令：

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## 程式碼實作

完整實作見 `07-dotnet-agent-framework.cs`，內容示範：

- 使用 DotNetEnv 載入環境配置
- 設定 Azure OpenAI 用戶端並利用 `GetChatClient().AsAIAgent()` 建立 AI 代理
- 定義帶 JSON 序列化的結構化資料模型（Plan 和 TravelPlan）
- 使用 JSON schema 創建具結構化輸出的 AI 代理
- 以類型安全的回應執行規劃請求

## 主要概念

### 使用類型安全模型的結構化規劃

代理使用 C# 類別定義規劃輸出的結構：

```csharp
public class Plan
{
    [JsonPropertyName("assigned_agent")]
    public string? Assigned_agent { get; set; }

    [JsonPropertyName("task_details")]
    public string? Task_details { get; set; }
}

public class TravelPlan
{
    [JsonPropertyName("main_task")]
    public string? Main_task { get; set; }

    [JsonPropertyName("subtasks")]
    public IList<Plan> Subtasks { get; set; }
}
```

### 結構化輸出的 JSON Schema

代理配置為回傳符合 TravelPlan schema 的回應：

```csharp
ChatClientAgentOptions agentOptions = new()
{
    Name = AGENT_NAME,
    Description = AGENT_INSTRUCTIONS,
    ChatOptions = new()
    {
        ResponseFormat = ChatResponseFormatJson.ForJsonSchema(
            schema: AIJsonUtilities.CreateJsonSchema(typeof(TravelPlan)),
            schemaName: "TravelPlan",
            schemaDescription: "Travel Plan with main_task and subtasks")
    }
};
```

### 規劃代理指令

代理作為協調者，將任務委派給專門子代理：

- FlightBooking：負責訂機票與提供航班資訊
- HotelBooking：負責訂飯店與提供飯店資訊
- CarRental：負責訂車並提供租車資訊
- ActivitiesBooking：負責訂活動並提供活動資訊
- DestinationInfo：提供目的地資訊
- DefaultAgent：處理一般請求

## 預期輸出

當您使用旅行規劃請求執行代理時，代理會分析請求並產生一個結構化計畫，適當分配任務給專門代理，輸出格式為符合 TravelPlan schema 的 JSON。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->