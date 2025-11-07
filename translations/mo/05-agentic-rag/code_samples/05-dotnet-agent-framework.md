<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c268705e6fb2b30c7690d5b2a002e072",
  "translation_date": "2025-11-07T08:58:02+00:00",
  "source_file": "05-agentic-rag/code_samples/05-dotnet-agent-framework.md",
  "language_code": "mo"
}
-->
# 🔍 使用 Azure AI Foundry (.NET) 建立企業級 RAG 系統

## 📋 學習目標

本筆記本展示如何使用 Microsoft Agent Framework 在 .NET 與 Azure AI Foundry 中建立企業級檢索增強生成 (RAG) 系統。您將學習如何建立可投入生產的代理，能夠搜尋文件並提供準確且具上下文的回應，同時具備企業級的安全性與可擴展性。

**您將學到的企業級 RAG 功能：**
- 📚 **文件智能**：利用 Azure AI 服務進行高級文件處理
- 🔍 **語義搜尋**：具備企業功能的高效能向量搜尋
- 🛡️ **安全整合**：基於角色的存取控制與資料保護模式
- 🏢 **可擴展架構**：具備監控功能的生產級 RAG 系統

## 🎯 企業級 RAG 架構

### 核心企業組件
- **Azure AI Foundry**：具備安全性與合規性的管理型企業 AI 平台
- **持久代理**：具有對話歷史與上下文管理的有狀態代理
- **向量存儲管理**：企業級文件索引與檢索
- **身份整合**：Azure AD 驗證與基於角色的存取控制

### .NET 企業優勢
- **類型安全**：針對 RAG 操作與數據結構的編譯時驗證
- **非同步效能**：非阻塞的文件處理與搜尋操作
- **記憶體管理**：針對大型文件集合的高效資源利用
- **整合模式**：與 Azure 服務的原生整合與依賴注入

## 🏗️ 技術架構

### 企業級 RAG 流程
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### 核心 .NET 組件
- **Azure.AI.Agents.Persistent**：具備狀態持久性的企業代理管理
- **Azure.Identity**：整合驗證以安全存取 Azure 服務
- **Microsoft.Agents.AI.AzureAI**：針對 Azure 優化的代理框架實現
- **System.Linq.Async**：高效能的非同步 LINQ 操作

## 🔧 企業功能與優勢

### 安全性與合規性
- **Azure AD 整合**：企業身份管理與驗證
- **基於角色的存取**：針對文件存取與操作的細粒度權限
- **資料保護**：針對敏感文件的靜態與傳輸加密
- **審計日誌**：滿足合規需求的全面活動追蹤

### 效能與可擴展性
- **連線池化**：高效的 Azure 服務連線管理
- **非同步處理**：適用於高吞吐量場景的非阻塞操作
- **快取策略**：針對常用文件的智能快取
- **負載平衡**：適用於大規模部署的分散式處理

### 管理與監控
- **健康檢查**：內建的 RAG 系統組件監控
- **效能指標**：搜尋質量與回應時間的詳細分析
- **錯誤處理**：具備重試策略的全面異常管理
- **配置管理**：具有驗證功能的環境特定設置

## ⚙️ 先決條件與設置

**開發環境：**
- .NET 9.0 SDK 或更高版本
- Visual Studio 2022 或帶有 C# 擴展的 VS Code
- 具有 AI Foundry 訪問權限的 Azure 訂閱

**所需 NuGet 套件：**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Azure 驗證設置：**
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
- **增量更新**：實時文件新增與修改
- **版本控制**：文件版本管理與變更追蹤
- **元數據管理**：豐富的文件屬性與分類法

### 搜尋與檢索模式
- **混合搜尋**：結合語義與關鍵字搜尋以獲得最佳結果
- **分面搜尋**：多維度篩選與分類
- **相關性調整**：針對特定領域需求的自定義評分算法
- **結果排序**：結合業務邏輯的高級排序

### 安全模式
- **文件級安全性**：針對每個文件的細粒度存取控制
- **數據分類**：自動敏感性標籤與保護
- **審計追蹤**：所有 RAG 操作的全面日誌記錄
- **隱私保護**：PII 檢測與遮蔽功能

## 🔒 企業安全功能

### 驗證與授權
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
- **加密**：針對文件與搜尋索引的端到端加密
- **存取控制**：與 Azure AD 整合的用戶與群組權限
- **數據駐留**：符合合規要求的地理數據位置控制
- **備份與恢復**：自動化備份與災難恢復功能

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
- **連線管理**：正確的 Azure 服務連線生命週期

### 快取策略
- **查詢快取**：快取經常執行的搜尋
- **文件快取**：針對熱門文件的內存快取
- **索引快取**：優化的向量索引快取
- **結果快取**：智能快取生成的回應

## 📊 企業應用場景

### 知識管理
- **企業維基**：智能搜尋公司知識庫
- **政策與程序**：自動化合規與程序指導
- **培訓材料**：智能學習與發展輔助
- **研究數據庫**：學術與研究論文分析系統

### 客戶支持
- **支持知識庫**：自動化客戶服務回應
- **產品文檔**：智能產品信息檢索
- **故障排除指南**：上下文問題解決輔助
- **常見問題系統**：從文件集合動態生成常見問題

### 法規合規
- **法律文件分析**：合同與法律文件智能
- **合規監控**：自動化法規合規檢查
- **風險評估**：基於文件的風險分析與報告
- **審計支持**：審計所需的智能文件檢索

## 🚀 生產部署

### 監控與可觀察性
- **Application Insights**：詳細的遙測與效能監控
- **自定義指標**：業務特定 KPI 追蹤與警報
- **分佈式追蹤**：跨服務的端到端請求追蹤
- **健康儀表板**：實時系統健康與效能可視化

### 可擴展性與可靠性
- **自動擴展**：基於負載與效能指標的自動擴展
- **高可用性**：具備故障轉移功能的多區域部署
- **負載測試**：在企業負載條件下進行效能驗證
- **災難恢復**：自動化備份與恢復程序

準備好建立能夠處理敏感文件的企業級 RAG 系統了嗎？讓我們為企業設計智能知識系統吧！🏢📖✨

## 程式實現

本課程的完整工作代碼範例可在 `05-dotnet-agent-framework.cs` 中找到。

執行範例：

```bash
# Make the script executable (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Run the .NET Single File App
./05-dotnet-agent-framework.cs
```

或者直接使用 `dotnet run`：

```bash
dotnet run 05-dotnet-agent-framework.cs
```

該代碼展示了：

1. **套件安裝**：安裝 Azure AI Agents 所需的 NuGet 套件
2. **環境配置**：加載 Azure AI Foundry 端點與模型設置
3. **文件上傳**：上傳文件以進行 RAG 處理
4. **向量存儲創建**：創建用於語義搜尋的向量存儲
5. **代理配置**：設置具備文件搜尋功能的 AI 代理
6. **查詢執行**：針對上傳的文件執行查詢

---

**免責聲明**：  
本文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或誤釋不承擔責任。