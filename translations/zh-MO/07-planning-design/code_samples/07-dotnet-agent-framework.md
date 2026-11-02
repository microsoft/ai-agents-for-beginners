# 🎯 使用 Azure OpenAI（Responses API）與 .NET 的規劃與設計模式

## 📋 學習目標

本筆記本示範了使用 .NET 中的 Microsoft Agent Framework 與 Azure OpenAI（Responses API）構建智能代理的企業級規劃與設計模式。您將學會創建能分解複雜問題、規劃多步解決方案並利用 .NET 的企業功能執行複雜工作流程的代理。

## ⚙️ 前置條件與環境設置

**開發環境：**
- .NET 9.0 SDK 或更高版本
- Visual Studio 2022 或帶有 C# 擴充功能的 VS Code
- 擁有 Azure 訂閱與 Azure OpenAI 資源及模型部署
- Azure CLI — 使用 `az login` 登入

**必要依賴項：**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="Microsoft.Agents.AI" Version="1.*-*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
<PackageReference Include="Azure.AI.OpenAI" Version="2.1.0" />
<PackageReference Include="Azure.Identity" Version="1.13.1" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**環境配置（.env 檔案）：**
```env
AZURE_OPENAI_ENDPOINT=https://<your-resource>.openai.azure.com
AZURE_OPENAI_DEPLOYMENT=gpt-5-mini
```

## 執行程式碼

本課程包含一個 .NET 單文件應用程式的實作。執行方法如下：

```bash
# 令檔案可執行（Linux/macOS）
chmod +x 07-dotnet-agent-framework.cs

# 執行應用程式
./07-dotnet-agent-framework.cs
```

或使用 dotnet run 命令：

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## 程式碼實作說明

完整實作位於 `07-dotnet-agent-framework.cs`，示範了：

- 使用 DotNetEnv 載入環境配置
- 配置 Azure OpenAI 用戶端並透過 `GetChatClient().AsAIAgent()` 創建 AI 代理
- 使用 JSON 序列化定義結構化資料模型（Plan 與 TravelPlan）
- 使用 JSON schema 創建具結構化輸出的 AI 代理
- 以型別安全的回應執行規劃請求

## 主要概念

### 利用型別安全模型進行結構化規劃

代理採用 C# 類別定義規劃輸出的結構：

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

### 用於結構化輸出的 JSON Schema

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

- FlightBooking：負責訂機票及提供航班資訊
- HotelBooking：負責訂旅館及提供旅館資訊
- CarRental：負責訂租車及提供租車資訊
- ActivitiesBooking：負責訂活動及提供活動資訊
- DestinationInfo：負責提供旅遊目的地資訊
- DefaultAgent：負責處理一般請求

## 預期輸出

當您執行代理處理旅遊規劃請求時，代理會分析請求並產生一份結構化計劃，將任務適當指派至專門代理，並以符合 TravelPlan schema 的 JSON 格式回傳。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->