<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f82a3992438bcc028a2569c5fed828a9",
  "translation_date": "2025-11-07T09:21:52+00:00",
  "source_file": "04-tool-use/code_samples/04-dotnet-agent-framework.md",
  "language_code": "mo"
}
-->
# 🛠️ 使用 GitHub 模型進行進階工具操作 (.NET)

## 📋 學習目標

此筆記本展示了使用 Microsoft Agent Framework 和 GitHub 模型在 .NET 中的企業級工具整合模式。您將學習如何使用 C# 的強型別和 .NET 的企業功能來構建具有多種專業工具的高級代理。

**您將掌握的進階工具功能：**
- 🔧 **多工具架構**：構建具有多種專業能力的代理
- 🎯 **型別安全的工具執行**：利用 C# 的編譯時驗證
- 📊 **企業工具模式**：生產級工具設計和錯誤處理
- 🔗 **工具組合**：結合工具以實現複雜的業務工作流程

## 🎯 .NET 工具架構的優勢

### 企業工具功能
- **編譯時驗證**：強型別確保工具參數的正確性
- **依賴注入**：IoC 容器整合以進行工具管理
- **非同步模式**：使用適當的資源管理進行非阻塞工具執行
- **結構化日誌**：內建日誌整合以監控工具執行

### 生產級模式
- **例外處理**：使用型別化例外進行全面的錯誤管理
- **資源管理**：正確的資源釋放模式和記憶體管理
- **效能監控**：內建指標和效能計數器
- **配置管理**：型別安全的配置和驗證

## 🔧 技術架構

### 核心 .NET 工具元件
- **Microsoft.Extensions.AI**：統一的工具抽象層
- **Microsoft.Agents.AI**：企業級工具編排
- **GitHub 模型整合**：高效能 API 客戶端，具備連線池功能

### 工具執行管道
```
User Request → Agent Analysis → Tool Selection → Type Validation
                 ↓               ↓              ↓
         Parameter Binding → Tool Execution → Result Processing → Response
```

## 🛠️ 工具類別與模式

### 1. **資料處理工具**
- **輸入驗證**：使用資料註解進行強型別驗證
- **轉換操作**：型別安全的資料轉換和格式化
- **業務邏輯**：特定領域的計算和分析工具
- **輸出格式化**：結構化的回應生成

### 2. **整合工具**
- **API 連接器**：使用 HttpClient 進行 RESTful 服務整合
- **資料庫工具**：使用 Entity Framework 進行資料存取
- **檔案操作**：具備驗證的安全檔案系統操作
- **外部服務**：第三方服務整合模式

### 3. **實用工具**
- **文字處理**：字串操作和格式化工具
- **日期/時間操作**：文化敏感的日期/時間計算
- **數學工具**：精確計算和統計操作
- **驗證工具**：業務規則驗證和資料檢查

## ⚙️ 先決條件與設置

**開發環境：**
- .NET 9.0 SDK 或更高版本
- Visual Studio 2022 或 VS Code，需安裝 C# 擴展
- GitHub 模型 API 存取權限

**所需 NuGet 套件：**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**環境配置 (.env 檔案)：**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

準備好使用 .NET 架構企業級代理，並具備強型別工具功能了嗎？讓我們一起設計專業級解決方案吧！ 🏢⚡

## 💻 程式碼實現

完整的 C# 實現可在附檔 `04-dotnet-agent-framework.cs` 中找到。此 .NET 單檔應用程式展示了：

- 加載 GitHub 模型配置的環境變數
- 使用 C# 方法和屬性定義自訂工具
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
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。