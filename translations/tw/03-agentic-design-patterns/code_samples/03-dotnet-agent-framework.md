<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c8bc231a26e949f525d65b716538707f",
  "translation_date": "2025-11-07T09:44:19+00:00",
  "source_file": "03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.md",
  "language_code": "tw"
}
-->
# 🎨 使用 GitHub 模型的 Agentic 設計模式 (.NET)

## 📋 學習目標

此筆記本展示了使用 Microsoft Agent Framework 與 GitHub 模型整合在 .NET 中構建智能代理的企業級設計模式。您將學習使代理具備生產準備、可維護性和可擴展性的專業模式和架構方法。

**企業設計模式：**
- 🏭 **工廠模式**：使用依賴注入標準化代理創建
- 🔧 **建造者模式**：流暢的代理配置和設置
- 🧵 **線程安全模式**：並發對話管理
- 📋 **儲存庫模式**：有組織的工具和能力管理

## 🎯 .NET 特定架構優勢

### 企業功能
- **強類型**：編譯時驗證和 IntelliSense 支援
- **依賴注入**：內建 DI 容器整合
- **配置管理**：IConfiguration 和 Options 模式
- **Async/Await**：一流的非同步程式設計支援

### 生產準備模式
- **日誌整合**：ILogger 和結構化日誌支援
- **健康檢查**：內建監控和診斷
- **配置驗證**：使用資料註解的強類型
- **錯誤處理**：結構化的例外管理

## 🔧 技術架構

### 核心 .NET 元件
- **Microsoft.Extensions.AI**：統一的 AI 服務抽象
- **Microsoft.Agents.AI**：企業代理編排框架
- **GitHub 模型整合**：高效能 API 客戶端模式
- **配置系統**：appsettings.json 和環境整合

### 設計模式實現
```csharp
IServiceCollection → Agent Builder → Configuration → Tool Registry → AI Agent
```

## 🏗️ 展示的企業模式

### 1. **創建模式**
- **代理工廠**：集中化代理創建，具有一致的配置
- **建造者模式**：流暢的 API 用於複雜代理配置
- **單例模式**：共享資源和配置管理
- **依賴注入**：鬆耦合和可測試性

### 2. **行為模式**
- **策略模式**：可互換的工具執行策略
- **命令模式**：封裝的代理操作，具有撤銷/重做功能
- **觀察者模式**：事件驅動的代理生命週期管理
- **模板方法**：標準化的代理執行工作流程

### 3. **結構模式**
- **適配器模式**：GitHub 模型 API 整合層
- **裝飾者模式**：代理能力增強
- **外觀模式**：簡化的代理交互介面
- **代理模式**：延遲加載和快取以提升效能

## ⚙️ 先決條件與設置

**開發環境：**
- .NET 9.0 SDK 或更高版本
- Visual Studio 2022 或 VS Code，帶有 C# 擴展
- GitHub 模型 API 訪問權限

**NuGet 依賴項：**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**配置 (.env 文件)：**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 📚 .NET 設計原則

### SOLID 原則
- **單一職責**：每個元件有一個明確的目的
- **開放/封閉**：可擴展而不修改
- **里氏替換**：基於介面的工具實現
- **介面隔離**：專注且內聚的介面
- **依賴反轉**：依賴抽象而非具體實現

### 清晰架構
- **領域層**：核心代理和工具抽象
- **應用層**：代理編排和工作流程
- **基礎設施層**：GitHub 模型整合和外部服務
- **展示層**：用戶交互和響應格式化

## 🔒 企業考量

### 安全性
- **憑證管理**：使用 IConfiguration 安全處理 API 密鑰
- **輸入驗證**：強類型和資料註解驗證
- **輸出清理**：安全的響應處理和過濾
- **審計日誌**：全面的操作追蹤

### 效能
- **非同步模式**：非阻塞 I/O 操作
- **連接池**：高效的 HTTP 客戶端管理
- **快取**：響應快取以提升效能
- **資源管理**：正確的資源釋放和清理模式

### 可擴展性
- **線程安全**：支援並發代理執行
- **資源池化**：高效的資源利用
- **負載管理**：速率限制和反壓處理
- **監控**：效能指標和健康檢查

## 🚀 生產部署

- **配置管理**：特定環境的設置
- **日誌策略**：結構化日誌，帶有關聯 ID
- **錯誤處理**：全局例外處理，具有適當的恢復機制
- **監控**：應用洞察和效能計數器
- **測試**：單元測試、整合測試和負載測試模式

準備好使用 .NET 構建企業級智能代理了嗎？讓我們設計一些穩健的架構吧！ 🏢✨

## 程式碼範例

完整的工作範例請參見 [03-dotnet-agent-framework.cs](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs)。

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。