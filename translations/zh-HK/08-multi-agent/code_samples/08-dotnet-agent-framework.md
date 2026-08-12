# 🤝 企業多代理工作流程系統 (.NET)

## 📋 學習目標

本筆記本展示如何使用 .NET 中的 Microsoft Agent Framework 並結合 Azure OpenAI (Responses API) 建立複雜的企業級多代理系統。你將學習如何通過結構化工作流程協調多個專業代理協同工作，並利用 .NET 的企業功能打造可投入生產的解決方案。

**你將打造的企業多代理能力：**
- 👥 <strong>代理協作</strong>：具備編譯時驗證的類型安全代理協調
- 🔄 <strong>工作流程編排</strong>：使用 .NET 非同步模式的宣告式工作流程定義
- 🎭 <strong>角色專精</strong>：強類型代理人格與專業領域
- 🏢 <strong>企業整合</strong>：監控與錯誤處理的生產級範式

## ⚙️ 前置條件與設置

**開發環境：**
- .NET 9.0 SDK 或更高版本
- Visual Studio 2022 或具備 C# 擴充的 VS Code
- Azure 訂閱（用於持久代理）

**所需 NuGet 套件：**
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

本課程的完整可執行程式碼可在附帶的 C# 檔案中取得：[`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

執行範例步驟：

```bash
# 令檔案可執行（Linux/macOS）
chmod +x 08-dotnet-agent-framework.cs

# 運行範例
./08-dotnet-agent-framework.cs
```

或使用 .NET CLI：

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## 本範例展示內容

此多代理工作流程系統創建了一個飯店旅遊推薦服務，包含兩個專業代理：

1. **FrontDesk 代理**：提供活動及地點推薦的旅遊代理
2. **Concierge 代理**：檢視推薦以確保體驗真實且非觀光客化

這些代理在一個工作流程中協作：
- FrontDesk 代理接收初始旅遊請求
- Concierge 代理審核並精煉推薦內容
- 工作流程實時串流回應

## 主要概念

### 代理協調
範例展示如何使用 Microsoft Agent Framework 實現具編譯時驗證的類型安全代理協調。

### 工作流程編排
使用 .NET 的非同步模式，以宣告式工作流程定義串聯多個代理。

### 串流回應
實作代理回應的實時串流，採用非同步列舉和事件驅動架構。

### 企業整合
展示生產級範式包括：
- 環境變數設定
- 安全憑證管理
- 錯誤處理
- 非同步事件處理

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->