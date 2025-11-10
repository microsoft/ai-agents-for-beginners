<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c268705e6fb2b30c7690d5b2a002e072",
  "translation_date": "2025-11-07T08:58:40+00:00",
  "source_file": "05-agentic-rag/code_samples/05-dotnet-agent-framework.md",
  "language_code": "tw"
}
-->
# 🔍 使用 Azure AI Foundry (.NET) 建立企業級 RAG 系統

## 📋 學習目標

此筆記本展示如何使用 Microsoft Agent Framework 和 Azure AI Foundry 在 .NET 中建立企業級的檢索增強生成 (RAG) 系統。您將學習如何建立可投入生產的代理，能夠搜索文件並提供準確且具上下文的回應，同時具備企業級的安全性和可擴展性。

**您將建立的企業級 RAG 功能：**
- 📚 **文件智能**：利用 Azure AI 服務進行高級文件處理
- 🔍 **語義搜索**：具備企業功能的高效能向量搜索
- 🛡️ **安全整合**：基於角色的存取控制和資料保護模式
- 🏢 **可擴展架構**：具備監控功能的生產級 RAG 系統

## 🎯 企業級 RAG 架構

### 核心企業元件
- **Azure AI Foundry**：具備安全性和合規性的企業 AI 平台
- **持久代理**：具備對話歷史和上下文管理的有狀態代理
- **向量存儲管理**：企業級文件索引和檢索
- **身份整合**：Azure AD 身份驗證和基於角色的存取控制

### .NET 企業優勢
- **類型安全**：針對 RAG 操作和資料結構的編譯時驗證
- **非同步效能**：非阻塞的文件處理和搜索操作
- **記憶體管理**：針對大型文件集合的高效資源利用
- **整合模式**：與 Azure 服務的原生整合及依賴注入

## 🏗️ 技術架構

### 企業級 RAG 管道
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### 核心 .NET 元件
- **Azure.AI.Agents.Persistent**：具備狀態持久性的企業代理管理
- **Azure.Identity**：安全的 Azure 服務存取整合身份驗證
- **Microsoft.Agents.AI.AzureAI**：Azure 優化的代理框架實現
- **System.Linq.Async**：高效能的非同步 LINQ 操作

## 🔧 企業功能與優勢

### 安全性與合規性
- **Azure AD 整合**：企業身份管理和驗證
- **基於角色的存取**：針對文件存取和操作的細粒度權限
- **資料保護**：針對敏感文件的靜態和傳輸加密
- **審計日誌**：全面的活動追蹤以滿足合規要求

### 效能與可擴展性
- **連接池管理**：高效的 Azure 服務連接管理
- **非同步處理**：針對高吞吐量場景的非阻塞操作
- **快取策略**：針對頻繁存取文件的智能快取
- **負載平衡**：針對大規模部署的分布式處理

### 管理與監控
- **健康檢查**：內建的 RAG 系統元件監控
- **效能指標**：搜索質量和回應時間的詳細分析
- **錯誤處理**：全面的異常管理和重試策略
- **配置管理**：具備驗證功能的環境特定設置

## ⚙️ 先決條件與設置

**開發環境：**
- .NET 9.0 SDK 或更高版本
- Visual Studio 2022 或 VS Code（需安裝 C# 擴展）
- 擁有 Azure AI Foundry 存取權的 Azure 訂閱

**所需 NuGet 套件：**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Azure 身份驗證設置：**
```bash
# Install Azure CLI and authenticate
az login
az account set --subscription "your-subscription-id"
```

**環境配置：**
* Azure AI Foundry 配置（通過 Azure CLI 自動處理）
* 確保已驗證到正確的 Azure 訂閱

## 📊 企業級 RAG 模式

### 文件管理模式
- **批量上傳**：高效處理大型文件集合
- **增量更新**：實時文件新增和修改
- **版本控制**：文件版本管理和變更追蹤
- **元數據管理**：豐富的文件屬性和分類法

### 搜索與檢索模式
- **混合搜索**：結合語義和關鍵字搜索以獲得最佳結果
- **分面搜索**：多維度篩選和分類
- **相關性調整**：針對特定領域需求的自定義評分算法
- **結果排序**：結合業務邏輯的高級排序

### 安全模式
- **文件級安全性**：針對每個文件的細粒度存取控制
- **資料分類**：自動敏感性標籤和保護
- **審計追蹤**：全面記錄所有 RAG 操作
- **隱私保護**：PII 檢測和遮蔽功能

## 🔒 企業安全功能

### 身份驗證與授權
```csharp
// Azure AD integrated authentication
var credential = new AzureCliCredential();
var agentsClient = new PersistentAgentsClient(endpoint, credential);

// Role-based access validation
if (!await ValidateUserPermissions(user, documentId))
{
    throw new UnauthorizedAccessException("Insufficient permissions");
}
```

### 資料保護
- **加密**：針對文件和搜索索引的端到端加密
- **存取控制**：與 Azure AD 整合的用戶和群組權限
- **資料駐留**：針對合規性的地理資料位置控制
- **備份與恢復**：自動備份和災難恢復功能

## 📈 效能優化

### 非同步處理模式
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### 記憶體管理
- **流式處理**：處理大型文件而不會出現記憶體問題
- **資源池化**：高效重用昂貴資源
- **垃圾回收**：優化的記憶體分配模式
- **連接管理**：正確的 Azure 服務連接生命周期

### 快取策略
- **查詢快取**：快取頻繁執行的搜索
- **文件快取**：針對熱門文件的內存快取
- **索引快取**：優化的向量索引快取
- **結果快取**：智能快取生成的回應

## 📊 企業應用場景

### 知識管理
- **企業 Wiki**：智能搜索公司知識庫
- **政策與程序**：自動合規和程序指導
- **培訓材料**：智能學習和發展輔助
- **研究數據庫**：學術和研究論文分析系統

### 客戶支持
- **支持知識庫**：自動化客戶服務回應
- **產品文檔**：智能產品信息檢索
- **故障排除指南**：上下文問題解決輔助
- **常見問題系統**：從文件集合動態生成常見問題

### 法規合規
- **法律文件分析**：合同和法律文件智能
- **合規監控**：自動化法規合規檢查
- **風險評估**：基於文件的風險分析和報告
- **審計支持**：智能文件發現以支持審計

## 🚀 生產部署

### 監控與可觀察性
- **Application Insights**：詳細的遙測和效能監控
- **自定義指標**：業務特定 KPI 追蹤和警報
- **分布式追蹤**：跨服務的端到端請求追蹤
- **健康儀表板**：實時系統健康和效能可視化

### 可擴展性與可靠性
- **自動擴展**：基於負載和效能指標的自動擴展
- **高可用性**：具備故障轉移功能的多區域部署
- **負載測試**：在企業負載條件下進行效能驗證
- **災難恢復**：自動化備份和恢復程序

準備好建立能夠處理敏感文件且具備可擴展性的企業級 RAG 系統了嗎？讓我們為企業架構智能知識系統吧！ 🏢📖✨

## 程式碼實現

此課程的完整工作範例程式碼可在 `05-dotnet-agent-framework.cs` 中找到。

執行範例：

```bash
# Make the script executable (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Run the .NET Single File App
./05-dotnet-agent-framework.cs
```

或直接使用 `dotnet run`：

```bash
dotnet run 05-dotnet-agent-framework.cs
```

程式碼展示了：

1. **套件安裝**：安裝 Azure AI Agents 所需的 NuGet 套件
2. **環境配置**：載入 Azure AI Foundry 端點和模型設置
3. **文件上傳**：上傳文件以進行 RAG 處理
4. **向量存儲建立**：建立語義搜索的向量存儲
5. **代理配置**：設置具備文件搜索功能的 AI 代理
6. **查詢執行**：對上傳的文件執行查詢

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。