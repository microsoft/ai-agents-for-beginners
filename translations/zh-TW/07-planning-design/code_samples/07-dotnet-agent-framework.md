# 🎯 使用 Azure OpenAI（Responses API）與 .NET 進行規劃與設計模式

## 📋 學習目標

本筆記本展示了使用 Microsoft Agent Framework 在 .NET 中搭配 Azure OpenAI（Responses API）建構智慧代理的企業級規劃與設計模式。您將學會如何創建能分解複雜問題、規劃多步驟解決方案以及運用 .NET 企業功能執行複雜工作流程的代理。

## ⚙️ 先決條件與設定

**開發環境：**
- .NET 9.0 SDK 或更高版本
- Visual Studio 2022 或具有 C# 擴充功能的 VS Code
- 擁有 Azure 訂閱、Azure OpenAI 資源與模型部署
- 已登入的 Azure CLI — 使用 `az login`

**必要的相依套件：**
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

本課程包含 .NET 單一檔案應用程式實作。執行方式如下：

```bash
# 使檔案具有執行權限（Linux/macOS）
chmod +x 07-dotnet-agent-framework.cs

# 執行應用程式
./07-dotnet-agent-framework.cs
```

或使用 dotnet run 指令：

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## 程式碼實作

完整實作位於 `07-dotnet-agent-framework.cs`，示範了：

- 使用 DotNetEnv 載入環境配置
- 設定 Azure OpenAI 用戶端並使用 `GetChatClient().AsAIAgent()` 建立 AI 代理
- 使用 JSON 序列化定義結構化資料模型（Plan 與 TravelPlan）
- 使用 JSON schema 建立結構化輸出 AI 代理
- 以型別安全回應執行規劃請求

## 主要概念

### 使用型別安全模型的結構化規劃

代理使用 C# 類別來定義規劃輸出的結構：

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

代理扮演協調者角色，將任務委派給專門的子代理：

- FlightBooking：負責訂票與航班資訊
- HotelBooking：負責訂房與飯店資訊
- CarRental：負責租車與租車資訊
- ActivitiesBooking：負責預訂活動與活動資訊
- DestinationInfo：提供目的地資訊
- DefaultAgent：處理一般請求

## 預期輸出

當您運行代理並提供旅遊規劃請求時，代理會分析該請求並產生結構化計畫，將任務適當分配給專門代理，並以符合 TravelPlan schema 的 JSON 格式輸出。

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->