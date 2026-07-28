# 🤝 企業多代理工作流程系統 (.NET)

## 📋 學習目標

本筆記本示範如何使用 .NET 中的 Microsoft Agent Framework 並結合 Azure OpenAI（Responses API）來建立複雜的企業級多代理系統。你將學會如何透過結構化工作流程協調多個專業代理協同工作，並利用 .NET 的企業功能打造可用於生產的解決方案。

**你將建立的企業多代理功能：**
- 👥 <strong>代理協作</strong>：具有編譯時驗證的類型安全代理協調
- 🔄 <strong>工作流程編排</strong>：使用 .NET 非同步模式的宣告式工作流程定義
- 🎭 <strong>角色專精化</strong>：強類型代理人格與專業領域
- 🏢 <strong>企業整合</strong>：包含監控與錯誤處理的生產就緒模式

## ⚙️ 前置條件與設定

**開發環境：**
- .NET 9.0 SDK 或更高版本
- Visual Studio 2022 或附有 C# 擴充功能的 VS Code
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

本課程完整可運行的程式碼在附帶的 C# 檔案中：[ `08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

執行範例：

```bash
# 使檔案可執行（Linux/macOS）
chmod +x 08-dotnet-agent-framework.cs

# 執行範例
./08-dotnet-agent-framework.cs
```

或使用 .NET CLI：

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## 本範例展示內容

此多代理工作流程系統創建了一個酒店旅遊推薦服務，包含兩個專業代理：

1. **FrontDesk Agent**：一個負責提供活動與地點推薦的旅遊代理
2. **Concierge Agent**：審核推薦內容，確保體驗真實且非觀光客常去的地方

這些代理協同工作，流程如下：
- FrontDesk 代理接收初始旅遊需求
- Concierge 代理審查並優化推薦內容
- 工作流程即時串流回應

## 主要概念

### 代理協調
此範例展示如何使用 Microsoft Agent Framework 進行具有編譯時驗證的類型安全代理協調。

### 工作流程編排
使用 .NET 的非同步模式宣告性定義工作流程，串接多個代理於管線中。

### 串流回應
透過非同步可列舉物件與事件驅動架構實現即時串流代理回應。

### 企業整合
展示生產就緒的模式，包括：
- 環境變數設定
- 安全憑證管理
- 錯誤處理
- 非同步事件處理

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->