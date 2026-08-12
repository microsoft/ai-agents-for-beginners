# 🔍 使用 Microsoft Foundry (.NET) 的企業級 RAG

## 📋 學習目標

本筆記本示範如何使用 Microsoft Foundry 在 .NET 中利用 Microsoft Agent Framework 建構企業級檢索增強生成 (RAG) 系統。你將學會如何建立可投入生產的代理，能夠搜尋文件並提供準確且具上下文感知的回應，同時具備企業安全性和可擴充性。

**你將打造的企業級 RAG 能力：**
- 📚 <strong>文件智慧</strong>：利用 Azure AI 服務進行先進的文件處理
- 🔍 <strong>語義搜尋</strong>：具企業功能的高性能向量搜尋
- 🛡️ <strong>安全整合</strong>：基於角色的存取及資料保護模式
- 🏢 <strong>可擴充架構</strong>：具監控的生產級 RAG 系統

## 🎯 企業級 RAG 架構

### 核心企業元件
- **Microsoft Foundry**：具安全與合規性的管理型企業 AI 平台
- <strong>持久代理</strong>：具對話記錄和上下文管理的狀態代理
- <strong>向量存儲管理</strong>：企業級文件索引與檢索
- <strong>身份整合</strong>：Azure AD 驗證與基於角色的存取控制

### .NET 企業優勢
- <strong>型別安全</strong>：RAG 操作和資料結構的編譯時驗證
- <strong>非同步效能</strong>：非阻塞的文件處理與搜尋作業
- <strong>記憶體管理</strong>：大型文件集合的高效資源利用
- <strong>整合模式</strong>：原生 Azure 服務整合與依賴注入

## 🏗️ 技術架構

### 企業 RAG 流程
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### 核心 .NET 元件
- **Azure.AI.Agents.Persistent**：具狀態持續性的企業代理管理
- **Azure.Identity**：整合的驗證以安全存取 Azure 服務
- **Microsoft.Agents.AI.AzureAI**：經 Azure 優化的代理框架實作
- **System.Linq.Async**：高性能非同步 LINQ 操作

## 🔧 企業功能與優勢

### 安全與合規
- **Azure AD 整合**：企業身份管理與驗證
- <strong>基於角色的存取</strong>：文件存取與操作的細緻權限控管
- <strong>資料保護</strong>：敏感文件靜態與傳輸加密
- <strong>稽核記錄</strong>：全面的活動追蹤以符合合規要求

### 效能與擴充性
- <strong>連線池管理</strong>：高效的 Azure 服務連線管理
- <strong>非同步處理</strong>：高吞吐場景的非阻塞作業
- <strong>快取策略</strong>：常用文件的智能快取
- <strong>負載平衡</strong>：大規模部署的分散式處理

### 管理與監控
- <strong>健康檢查</strong>：內建的 RAG 系統組件監控
- <strong>效能指標</strong>：詳細的搜尋品質與回應時間分析
- <strong>錯誤處理</strong>：全面的例外管理與重試策略
- <strong>配置管理</strong>：環境特定設定與驗證

## ⚙️ 前置條件與設定

**開發環境：**
- .NET 9.0 SDK 或更高版本
- Visual Studio 2022 或帶有 C# 擴充的 VS Code
- 具有 Microsoft Foundry 存取權的 Azure 訂閱

**所需 NuGet 套件：**
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

**環境配置：**
* Microsoft Foundry 配置（透過 Azure CLI 自動處理）
* 確認您已對正確的 Azure 訂閱完成驗證

## 📊 企業 RAG 模式

### 文件管理模式
- <strong>批次上傳</strong>：高效處理大型文件集合
- <strong>增量更新</strong>：實時文件新增與修改
- <strong>版本控制</strong>：文件版本管理與變更追蹤
- <strong>元資料管理</strong>：豐富文件屬性與分類法

### 搜尋與檢索模式
- <strong>混合搜尋</strong>：結合語義與關鍵字搜尋以達最佳效果
- <strong>多面向搜尋</strong>：多維度過濾與分類
- <strong>相關度調整</strong>：符合領域需求的客製化評分演算法
- <strong>結果排序</strong>：結合商業邏輯的進階排序

### 安全模式
- <strong>文件級安全</strong>：針對每個文件的細緻存取控制
- <strong>資料分類</strong>：自動敏感度標示與保護
- <strong>稽核追蹤</strong>：所有 RAG 操作的完整記錄
- <strong>隱私保護</strong>：個人識別資訊偵測與遮罩功能

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
- <strong>加密</strong>：文件與搜尋索引的端到端加密
- <strong>存取控制</strong>：與 Azure AD 整合的使用者與群組權限
- <strong>資料所在地</strong>：合規所需的地理資料位置控管
- <strong>備份與復原</strong>：自動化備份與災難復原能力

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
- <strong>串流處理</strong>：處理大型文件無記憶體問題
- <strong>資源池化</strong>：高效重複利用昂貴資源
- <strong>垃圾回收</strong>：優化的記憶體分配模式
- <strong>連線管理</strong>：正確的 Azure 服務連線生命週期

### 快取策略
- <strong>查詢快取</strong>：快取常執行搜尋
- <strong>文件快取</strong>：熱點文件的記憶體內快取
- <strong>索引快取</strong>：優化的向量索引快取
- <strong>結果快取</strong>：智能快取生成的回應

## 📊 企業使用案例

### 知識管理
- **企業 Wiki**：跨公司知識庫的智慧搜尋
- <strong>政策與程序</strong>：自動化合規與程序指導
- <strong>培訓教材</strong>：智慧學習與發展輔助
- <strong>研究資料庫</strong>：學術及研究論文分析系統

### 客戶支援
- <strong>支援知識庫</strong>：自動化客服回應
- <strong>產品文件</strong>：智慧產品資訊檢索
- <strong>疑難排解指南</strong>：有上下文的問題解決輔助
- <strong>問答系統</strong>：從文件集合動態生成 FAQ

### 規範合規
- <strong>法律文件分析</strong>：合約及法律文件智慧分析
- <strong>合規監控</strong>：自動化法規合規檢查
- <strong>風險評估</strong>：基於文件的風險分析與報告
- <strong>稽核支援</strong>：智慧文件發現以利稽核

## 🚀 生產部署

### 監控與可觀測性
- **Application Insights**：詳細遙測與效能監控
- <strong>自訂指標</strong>：業務特定的 KPI 追蹤與警示
- <strong>分散式追蹤</strong>：跨服務的端到端請求追蹤
- <strong>健康儀表板</strong>：即時系統健康與效能視覺化

### 可擴充性與可靠性
- <strong>自動擴充</strong>：依負載與效能指標自動調整規模
- <strong>高可用性</strong>：多區域部署與故障轉移能力
- <strong>負載測試</strong>：企業負載條件下的效能驗證
- <strong>災難復原</strong>：自動備份與復原程序

準備好打造能大規模處理敏感文件的企業級 RAG 系統了嗎？讓我們一起架構智慧知識系統給企業使用！🏢📖✨

## 程式碼實作

本課程的完整範例程式碼可在 `05-dotnet-agent-framework.cs` 取得。 

執行範例如下：

```bash
# 令腳本可執行（Linux/macOS）
chmod +x 05-dotnet-agent-framework.cs

# 執行 .NET 單檔應用程式
./05-dotnet-agent-framework.cs
```

或直接使用 `dotnet run`：

```bash
dotnet run 05-dotnet-agent-framework.cs
```

程式碼示範：

1. <strong>套件安裝</strong>：安裝 Azure AI 代理所需的 NuGet 套件
2. <strong>環境配置</strong>：載入 Microsoft Foundry 端點和模型設定
3. <strong>文件上傳</strong>：上傳文件以作 RAG 處理
4. <strong>向量存儲建立</strong>：建立用於語義搜尋的向量存儲
5. <strong>代理設定</strong>：設定具檔案搜尋能力的 AI 代理
6. <strong>查詢執行</strong>：對上傳文件執行查詢

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
本文件使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議尋求專業人工翻譯。我們不對因使用本翻譯而引起的任何誤解或曲解承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->