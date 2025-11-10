<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f5a5f2902f32272257506d88d3c43a1",
  "translation_date": "2025-11-07T09:14:13+00:00",
  "source_file": "08-multi-agent/code_samples/08-dotnet-agent-framework.md",
  "language_code": "hk"
}
-->
# 🤝 企業級多代理工作流程系統 (.NET)

## 📋 學習目標

此筆記本展示如何使用 Microsoft Agent Framework 和 GitHub 模型在 .NET 中構建高級企業級多代理系統。您將學習如何通過結構化的工作流程協調多個專業代理，利用 .NET 的企業功能來打造適合生產環境的解決方案。

**您將構建的企業級多代理功能：**
- 👥 **代理協作**：類型安全的代理協調，具備編譯時驗證
- 🔄 **工作流程編排**：使用 .NET 的異步模式進行聲明式工作流程定義
- 🎭 **角色專業化**：強類型的代理角色和專業領域
- 🏢 **企業整合**：具備監控和錯誤處理的生產級模式

## ⚙️ 先決條件與設置

**開發環境：**
- .NET 9.0 SDK 或更高版本
- Visual Studio 2022 或安裝了 C# 擴展的 VS Code
- Azure 訂閱（用於持久化代理）

**所需的 NuGet 套件：**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.4" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="9.8.0" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
```

## 程式碼範例

本課程的完整工作程式碼可在附帶的 C# 文件中找到：[`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

執行範例：

```bash
# Make the file executable (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Run the sample
./08-dotnet-agent-framework.cs
```

或者使用 .NET CLI：

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## 本範例展示的內容

此多代理工作流程系統創建了一個酒店旅行推薦服務，包含兩個專業代理：

1. **前台代理**：提供活動和地點推薦的旅行代理
2. **禮賓代理**：審核推薦以確保提供真實且非旅遊化的體驗

代理通過以下工作流程協作：
- 前台代理接收初始旅行請求
- 禮賓代理審核並改進推薦
- 工作流程以實時流方式傳遞回應

## 核心概念

### 代理協作
範例展示了使用 Microsoft Agent Framework 進行類型安全的代理協作，並具備編譯時驗證。

### 工作流程編排
使用 .NET 的異步模式進行聲明式工作流程定義，將多個代理連接到管道中。

### 實時回應流
使用異步可枚舉和事件驅動架構實現代理回應的實時流。

### 企業整合
展示了生產級模式，包括：
- 環境變數配置
- 安全憑證管理
- 錯誤處理
- 異步事件處理

---

**免責聲明**：  
此文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。