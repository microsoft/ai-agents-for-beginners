# 🤝 企業多代理工作流程系統 (.NET)

## 📋 學習目標

本筆記示範如何使用 .NET 中的 Microsoft Agent Framework 搭配 Azure OpenAI（Responses API）構建複雜的企業級多代理系統。您將學習如何透過結構化工作流程協同多個專門代理，利用 .NET 的企業功能打造生產就緒的解決方案。

**您將構建的企業多代理能力：**
- 👥 <strong>代理協作</strong>：具備編譯時驗證的型別安全代理協調
- 🔄 <strong>工作流程編排</strong>：使用 .NET 非同步模式的宣告式工作流程定義
- 🎭 <strong>角色專精</strong>：強型別代理人格與專業領域
- 🏢 <strong>企業整合</strong>：具監控與錯誤處理的生產就緒模式

## ⚙️ 前置需求與設定

**開發環境：**
- .NET 9.0 SDK 或更新版本
- Visual Studio 2022 或帶有 C# 擴充功能的 VS Code
- Azure 訂閱（用於持久代理）

**必要的 NuGet 套件：**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="10.*" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.10" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="10.*" />
<PackageReference Include="OpenTelemetry.Api" Version="1.*" />
<PackageReference Include="Microsoft.Agents.AI.Workflows" Version="1.*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
```

## 程式碼範例

本課程的完整工作程式碼可在附帶的 C# 檔案中取得：[`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

執行範例：

```bash
# 令檔案可執行（Linux/macOS）
chmod +x 08-dotnet-agent-framework.cs

# 執行範例
./08-dotnet-agent-framework.cs
```

或使用 .NET CLI：

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## 本範例示範內容

這個多代理工作流程系統建立了一個飯店旅遊推薦服務，包含兩個專門代理：

1. **FrontDesk Agent**：提供活動與地點推薦的旅遊代理
2. **Concierge Agent**：審核推薦內容，確保體驗真實且不觀光客導向

代理在以下工作流程中合作：
- FrontDesk 代理接收初始旅遊請求
- Concierge 代理審核並優化推薦內容
- 工作流程即時串流回應

## 重要概念

### 代理協調
範例示範使用 Microsoft Agent Framework 進行具編譯時驗證的型別安全代理協調。

### 工作流程編排
使用 .NET 非同步模式的宣告式工作流程定義，串連多個代理形成管線。

### 串流回應
實現使用非同步可列舉物與事件驅動架構的代理回應即時串流。

### 企業整合
展示生產就緒模式包括：
- 環境變數配置
- 安全憑證管理
- 錯誤處理
- 非同步事件處理

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->