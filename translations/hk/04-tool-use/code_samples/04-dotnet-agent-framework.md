<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f82a3992438bcc028a2569c5fed828a9",
  "translation_date": "2025-11-07T09:22:02+00:00",
  "source_file": "04-tool-use/code_samples/04-dotnet-agent-framework.md",
  "language_code": "hk"
}
-->
# 🛠️ 使用 GitHub 模型進行進階工具操作 (.NET)

## 📋 學習目標

此筆記本展示了使用 Microsoft Agent Framework 與 GitHub 模型在 .NET 中的企業級工具整合模式。您將學習如何使用多個專門工具構建高級代理，並充分利用 C# 的強類型和 .NET 的企業功能。

**您將掌握的進階工具能力：**
- 🔧 **多工具架構**：構建具有多種專門功能的代理
- 🎯 **類型安全的工具執行**：利用 C# 的編譯時驗證
- 📊 **企業工具模式**：生產級工具設計與錯誤處理
- 🔗 **工具組合**：結合工具以實現複雜的業務工作流程

## 🎯 .NET 工具架構的優勢

### 企業工具功能
- **編譯時驗證**：強類型確保工具參數的正確性
- **依賴注入**：IoC 容器整合以管理工具
- **Async/Await 模式**：非阻塞工具執行並妥善管理資源
- **結構化日誌**：內建日誌整合以監控工具執行

### 生產級模式
- **例外處理**：全面的錯誤管理與類型化例外
- **資源管理**：妥善的資源釋放模式與記憶體管理
- **效能監控**：內建指標與效能計數器
- **配置管理**：類型安全的配置與驗證

## 🔧 技術架構

### 核心 .NET 工具元件
- **Microsoft.Extensions.AI**：統一的工具抽象層
- **Microsoft.Agents.AI**：企業級工具編排
- **GitHub 模型整合**：高效能 API 客戶端與連接池

### 工具執行管道
```
User Request → Agent Analysis → Tool Selection → Type Validation
                 ↓               ↓              ↓
         Parameter Binding → Tool Execution → Result Processing → Response
```

## 🛠️ 工具類別與模式

### 1. **數據處理工具**
- **輸入驗證**：使用數據註解進行強類型驗證
- **轉換操作**：類型安全的數據轉換與格式化
- **業務邏輯**：特定領域的計算與分析工具
- **輸出格式化**：結構化的響應生成

### 2. **整合工具**
- **API 連接器**：使用 HttpClient 進行 RESTful 服務整合
- **數據庫工具**：使用 Entity Framework 進行數據訪問
- **文件操作**：安全的文件系統操作與驗證
- **外部服務**：第三方服務整合模式

### 3. **實用工具**
- **文本處理**：字串操作與格式化工具
- **日期/時間操作**：文化敏感的日期/時間計算
- **數學工具**：精確計算與統計操作
- **驗證工具**：業務規則驗證與數據檢查

## ⚙️ 先決條件與設置

**開發環境：**
- .NET 9.0 SDK 或更高版本
- Visual Studio 2022 或 VS Code（需安裝 C# 擴展）
- GitHub 模型 API 訪問權限

**所需 NuGet 套件：**
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

準備好在 .NET 中構建具有強大類型安全工具功能的企業級代理了嗎？讓我們一起設計專業級解決方案吧！ 🏢⚡

## 💻 程式碼實現

完整的 C# 實現可在配套文件 `04-dotnet-agent-framework.cs` 中找到。此 .NET 單文件應用展示了：

- 加載 GitHub 模型配置的環境變數
- 使用 C# 方法與屬性定義自訂工具
- 創建具有工具整合的 AI 代理
- 管理對話線程
- 執行代理請求並調用工具

執行範例：

```bash
chmod +x 04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

或使用 .NET CLI：

```bash
dotnet run 04-dotnet-agent-framework.cs
```

---

**免責聲明**：  
此文件已使用人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。