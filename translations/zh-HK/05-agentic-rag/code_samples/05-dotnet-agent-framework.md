# 🔍 使用 Microsoft Foundry (.NET) 建構企業級 RAG

## 📋 學習目標

本筆記本示範如何使用 Microsoft Foundry 中 .NET 的 Microsoft Agent Framework 建立企業級的檢索增強生成 (RAG) 系統。您將學會如何創建可用於生產的代理，能夠搜尋文件並提供準確且具上下文意識的回應，同時具備企業級的安全性與可擴展性。

**您將構建的企業級 RAG 功能：**
- 📚 <strong>文件智能</strong>：使用 Azure AI 服務進行先進的文件處理
- 🔍 <strong>語意搜尋</strong>：具備企業功能的高性能向量搜尋
- 🛡️ <strong>安全整合</strong>：基於角色的存取與資料保護模式
- 🏢 <strong>可擴展架構</strong>：具備監控的生產級 RAG 系統

## 🎯 企業級 RAG 架構

### 核心企業元件
- **Microsoft Foundry**：具備安全性和合規性的受控企業 AI 平台
- <strong>持續代理</strong>：具有狀態持續與會話記錄與上下文管理的代理
- <strong>向量庫管理</strong>：企業級文件索引與檢索
- <strong>身分整合</strong>：Azure AD 驗證以及基於角色的存取控制

### .NET 企業優勢
- <strong>型別安全</strong>：在編譯時驗證 RAG 操作與資料結構
- <strong>非同步效能</strong>：非阻塞文件處理與搜尋操作
- <strong>記憶體管理</strong>：大型文件集合的高效資源利用
- <strong>整合模式</strong>：透過依賴注入整合原生 Azure 服務

## 🏗️ 技術架構

### 企業級 RAG 流程
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### 核心 .NET 元件
- **Azure.AI.Agents.Persistent**：具備狀態持續性的企業代理管理
- **Azure.Identity**：整合驗證，確保安全存取 Azure 服務
- **Microsoft.Agents.AI.AzureAI**：Azure 最佳化代理框架實作
- **System.Linq.Async**：高效能非同步 LINQ 運算

## 🔧 企業特色與優勢

### 安全與合規
- **Azure AD 整合**：企業身分管理與驗證
- <strong>基於角色的存取</strong>：文件存取與操作的細緻權限管理
- <strong>資料保護</strong>：靜態及傳輸中敏感文件加密
- <strong>稽核日誌</strong>：全面行為追蹤以符合合規要求

### 效能與可擴展性
- <strong>連線池管理</strong>：高效 Azure 服務連線調度
- <strong>非同步處理</strong>：為高吞吐情境提供非阻塞運作
- <strong>快取策略</strong>：智慧快取頻繁存取文件
- <strong>負載平衡</strong>：大規模部署的分散式處理

### 管理與監控
- <strong>健康檢查</strong>：RAG 系統元件內建監控
- <strong>效能指標</strong>：搜尋品質與回應時間詳細分析
- <strong>錯誤處理</strong>：完整異常管理與重試策略
- <strong>設定管理</strong>：驗證環境特定設定

## ⚙️ 先決條件與設定

**開發環境：**
- .NET 9.0 SDK 或更新版本
- Visual Studio 2022 或具 C# 擴充功能的 VS Code
- 具 Microsoft Foundry 訪問權限的 Azure 訂閱

**必要 NuGet 套件：**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Azure 驗證設定：**
```bash
# 安裝 Azure CLI 並進行身份驗證
az login
az account set --subscription "your-subscription-id"
```

**環境設定：**
* Microsoft Foundry 設定（透過 Azure CLI 自動處理）
* 確認已驗證至正確的 Azure 訂閱

## 📊 企業級 RAG 模式

### 文件管理模式
- <strong>批量上傳</strong>：高效處理大量文件集合
- <strong>增量更新</strong>：即時文件新增與修改
- <strong>版本控制</strong>：文件版本與變更追蹤
- <strong>元資料管理</strong>：豐富文件屬性與分類法

### 搜尋與檢索模式
- <strong>混合搜尋</strong>：結合語意與關鍵字搜尋達最佳結果
- <strong>面向搜尋</strong>：多維篩選與分類
- <strong>關聯度調整</strong>：針對特定領域需求客製化評分演算法
- <strong>結果排序</strong>：結合業務邏輯的進階排名

### 安全模式
- <strong>文件層級安全</strong>：針對每份文件的細緻存取控制
- <strong>資料分類</strong>：自動敏感度標籤與保護
- <strong>稽核追蹤</strong>：完整記錄所有 RAG 操作
- <strong>隱私保護</strong>：個人資料識別(PII)偵測與遮蔽功能

## 🔒 企業安全特性

### 認證與授權
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
- <strong>加密</strong>：文件與搜尋索引的端對端加密
- <strong>存取控制</strong>：結合 Azure AD 管理使用者與群組權限
- <strong>資料駐留</strong>：符合合規的地理資料位置控制
- <strong>備份與復原</strong>：自動化備份及災難復原能力

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
- <strong>串流處理</strong>：處理大型文件而不造成記憶體問題
- <strong>資源池化</strong>：有效重用高成本資源
- <strong>垃圾回收</strong>：優化記憶體配置模式
- <strong>連線管理</strong>：正確管理 Azure 服務連線週期

### 快取策略
- <strong>查詢快取</strong>：快取頻繁執行的搜尋
- <strong>文件快取</strong>：熱點文件的記憶體快取
- <strong>索引快取</strong>：優化向量索引快取
- <strong>結果快取</strong>：智慧快取生成的回應

## 📊 企業使用案例

### 知識管理
- <strong>企業維基</strong>：跨公司知識庫的智慧搜尋
- <strong>政策與程序</strong>：自動合規與程序指引
- <strong>培訓教材</strong>：智慧學習與發展助手
- <strong>研究資料庫</strong>：學術及研究論文分析系統

### 客戶支援
- <strong>支援知識庫</strong>：自動客服回應
- <strong>產品文件</strong>：智慧產品資訊檢索
- <strong>故障排除指南</strong>：具上下文的問題解決協助
- <strong>常見問題系統</strong>：從文件集合動態產生 FAQ

### 合規監管
- <strong>法律文件分析</strong>：合約與法律文件智慧解讀
- <strong>合規監控</strong>：自動化法規合規檢查
- <strong>風險評估</strong>：基於文件的風險分析與報告
- <strong>稽核支援</strong>：智慧文件發掘輔助稽核

## 🚀 生產部署

### 監控與可觀察性
- **Application Insights**：詳細遙測與效能監控
- <strong>自訂指標</strong>：業務專屬 KPI 追蹤與警報
- <strong>分散式追蹤</strong>：跨服務的端到端請求追蹤
- <strong>健康儀表板</strong>：即時系統健康與效能視覺化

### 可擴展性與可靠性
- <strong>自動擴展</strong>：基於負載與效能指標的自動縮放
- <strong>高可用性</strong>：多區域部署及故障轉移能力
- <strong>負載測試</strong>：企業負載情境下的效能驗證
- <strong>災難復原</strong>：自動化備份與復原程序

準備好建立能處理敏感文件並具規模的企業級 RAG 系統了嗎？讓我們架構智能企業知識系統！🏢📖✨

## 程式碼實作

本課程的完整範例程式碼可於 `05-dotnet-agent-framework.cs` 找到。 

執行範例：

```bash
# 令腳本可執行（Linux/macOS）
chmod +x 05-dotnet-agent-framework.cs

# 執行 .NET 單文件應用程式
./05-dotnet-agent-framework.cs
```

或直接使用 `dotnet run`：

```bash
dotnet run 05-dotnet-agent-framework.cs
```

程式碼示範：

1. <strong>套件安裝</strong>：安裝 Azure AI Agents 所需的 NuGet 套件
2. <strong>環境設定</strong>：載入 Microsoft Foundry 端點及模型設定
3. <strong>文件上傳</strong>：上傳文件以供 RAG 處理
4. <strong>向量庫建立</strong>：為語意搜尋建立向量庫
5. <strong>代理配置</strong>：設置具備文件搜尋功能的 AI 代理
6. <strong>查詢執行</strong>：對已上傳文件執行查詢

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意，機器自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議進行專業人工翻譯。我們不對因使用本翻譯而產生的任何誤解或誤釋承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->