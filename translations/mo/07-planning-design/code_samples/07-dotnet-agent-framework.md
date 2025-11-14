<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "2d13c1e3518a0257a00fea949e2d0350",
  "translation_date": "2025-11-07T09:55:07+00:00",
  "source_file": "07-planning-design/code_samples/07-dotnet-agent-framework.md",
  "language_code": "mo"
}
-->
# 🎯 規劃與設計模式：使用 GitHub 模型 (.NET)

## 📋 學習目標

本筆記本展示了使用 Microsoft Agent Framework 和 GitHub 模型在 .NET 中構建智能代理的企業級規劃與設計模式。您將學習如何創建能分解複雜問題、規劃多步解決方案並執行複雜工作流程的代理，結合 .NET 的企業功能。

## ⚙️ 先決條件與設置

**開發環境：**
- .NET 9.0 SDK 或更高版本
- Visual Studio 2022 或安裝 C# 擴展的 VS Code
- GitHub Models API 訪問權限

**所需依賴項：**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**環境配置 (.env 文件)：**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 執行代碼

本課程包含一個 .NET 單文件應用程式的實現。執行方式如下：

```bash
# Make the file executable (Linux/macOS)
chmod +x 07-dotnet-agent-framework.cs

# Run the application
./07-dotnet-agent-framework.cs
```

或者使用 dotnet run 命令：

```bash
dotnet run 07-dotnet-agent-framework.cs
```

## 代碼實現

完整的實現可在 `07-dotnet-agent-framework.cs` 中找到，展示了以下內容：

- 使用 DotNetEnv 加載環境配置
- 配置 OpenAI 客戶端以使用 GitHub 模型
- 使用 JSON 序列化定義結構化數據模型（Plan 和 TravelPlan）
- 使用 JSON schema 創建具有結構化輸出的 AI 代理
- 執行規劃請求並生成類型安全的響應

## 核心概念

### 使用類型安全模型進行結構化規劃

代理使用 C# 類來定義規劃輸出的結構：

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

代理被配置為返回符合 TravelPlan schema 的響應：

```csharp
ChatClientAgentOptions agentOptions = new(name: AGENT_NAME, instructions: AGENT_INSTRUCTIONS)
{
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

代理充當協調者，將任務分配給專門的子代理：

- FlightBooking：負責預訂航班並提供航班信息
- HotelBooking：負責預訂酒店並提供酒店信息
- CarRental：負責租車並提供租車信息
- ActivitiesBooking：負責預訂活動並提供活動信息
- DestinationInfo：負責提供目的地信息
- DefaultAgent：負責處理一般請求

## 預期輸出

當您使用旅行規劃請求運行代理時，它將分析請求並生成結構化的計劃，將適當的任務分配給專門的代理，並以符合 TravelPlan schema 的 JSON 格式輸出。

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。