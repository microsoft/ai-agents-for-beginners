# 🔍 使用 Microsoft Foundry (.NET) 建立企業級 RAG

## 📋 學習目標

本筆記本示範如何利用 Microsoft Foundry 中的 Microsoft Agent Framework (.NET) 建置企業級的 Retrieval-Augmented Generation (RAG) 系統。您將學會如何建立可投入生產的代理，能夠搜尋文件並提供精確且具情境感知的回應，同時具備企業級的安全性與可擴充性。

**您將建立的企業級 RAG 能力：**
- 📚 <strong>文件智能</strong>：利用 Azure AI 服務進行先進的文件處理
- 🔍 <strong>語意搜尋</strong>：具企業特性的高效能向量搜尋
- 🛡️ <strong>安全整合</strong>：角色基礎存取與資料保護模式
- 🏢 <strong>可擴充架構</strong>：具監控的生產準備 RAG 系統

## 🎯 企業級 RAG 架構

### 核心企業元件
- **Microsoft Foundry**：具安全與合規性的託管企業 AI 平台
- <strong>持久代理</strong>：具會話歷史與情境管理的有狀態代理
- <strong>向量庫管理</strong>：企業級文件索引與檢索
- <strong>身份整合</strong>：Azure AD 認證與角色基礎存取控制

### .NET 企業優勢
- <strong>類型安全</strong>：RAG 操作與資料結構的編譯時驗證
- <strong>非同步效能</strong>：非阻塞的文件處理與搜尋操作
- <strong>記憶體管理</strong>：大型文件集合的有效資源利用
- <strong>整合模式</strong>：依賴注入下原生 Azure 服務整合

## 🏗️ 技術架構

### 企業級 RAG 流程
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### 核心 .NET 元件
- **Azure.AI.Agents.Persistent**：具狀態持續的企業代理管理
- **Azure.Identity**：整合式認證以安全存取 Azure 服務
- **Microsoft.Agents.AI.AzureAI**：針對 Azure 優化的代理框架實作
- **System.Linq.Async**：高效能非同步 LINQ 操作

## 🔧 企業功能與優勢

### 安全性與合規性
- **Azure AD 整合**：企業身份管理與認證
- <strong>角色基礎存取</strong>：文件存取與操作的細緻權限
- <strong>資料保護</strong>：靜態及傳輸中敏感文件的加密
- <strong>稽核記錄</strong>：完整的活動追蹤以符合合規要求

### 效能與可擴充性
- <strong>連線池管理</strong>：有效的 Azure 服務連線管理
- <strong>非同步處理</strong>：高吞吐量場景的非阻塞操作
- <strong>快取策略</strong>：智慧快取熱門文件
- <strong>負載平衡</strong>：大型部署的分散式處理

### 管理與監控
- <strong>健康檢查</strong>：內建 RAG 系統元件監控
- <strong>效能指標</strong>：詳盡的搜尋品質與回應時間分析
- <strong>錯誤處理</strong>：完善的例外管理與重試策略
- <strong>設定管理</strong>：具驗證的環境特定設定

## ⚙️ 先決條件與設定

**開發環境：**
- .NET 9.0 SDK 或以上
- Visual Studio 2022 或具 C# 擴充套件的 VS Code
- 具 Microsoft Foundry 訂閱的 Azure 訂閱帳號

**必要的 NuGet 套件：**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Azure 認證設定：**
```bash
# 安裝 Azure CLI 並進行身份驗證
az login
az account set --subscription "your-subscription-id"
```

**環境設定：**
* Microsoft Foundry 設定（透過 Azure CLI 自動處理）
* 確認已認證至正確的 Azure 訂閱帳號

## 📊 企業級 RAG 模式

### 文件管理模式
- <strong>批次上傳</strong>：有效率地處理大型文件集合
- <strong>增量更新</strong>：即時新增與修改文件
- <strong>版本控制</strong>：文件版本管理與變更追蹤
- <strong>元資料管理</strong>：豐富的文件屬性與分類法

### 搜尋與檢索模式
- <strong>混合搜尋</strong>：結合語意與關鍵詞搜尋以達最佳效果
- <strong>層面搜尋</strong>：多維度篩選與分類
- <strong>相關性調校</strong>：為特定領域需求訂製分數演算法
- <strong>結果排序</strong>：結合商業邏輯的高階排序

### 安全模式
- <strong>文件層級安全</strong>：細緻的文件存取控制
- <strong>資料分類</strong>：自動敏感度標籤與保護
- <strong>稽核軌跡</strong>：完整記錄所有 RAG 操作
- <strong>隱私保護</strong>：個資偵測與遮罩功能

## 🔒 企業安全功能

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
- <strong>加密</strong>：文件及搜尋索引的端對端加密
- <strong>存取控制</strong>：與 Azure AD 整合的使用者及群組權限
- <strong>資料駐留</strong>：符合合規性的地理資料位置控管
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
- <strong>串流處理</strong>：處理大型文件避免記憶體溢位
- <strong>資源池化</strong>：有效重複利用昂貴資源
- <strong>垃圾回收</strong>：優化的記憶體分配模式
- <strong>連線管理</strong>：妥善管理 Azure 服務連線生命週期

### 快取策略
- <strong>查詢快取</strong>：快取常用搜尋結果
- <strong>文件快取</strong>：熱門文件記憶體快取
- <strong>索引快取</strong>：優化向量索引快取
- <strong>結果快取</strong>：智慧快取生成的回應

## 📊 企業應用案例

### 知識管理
- <strong>企業維基</strong>：跨公司知識庫的智慧搜尋
- <strong>政策與程序</strong>：自動化合規與程序指導
- <strong>訓練教材</strong>：智慧學習與發展輔助
- <strong>研究資料庫</strong>：學術與研究論文分析系統

### 客戶支援
- <strong>支援知識庫</strong>：自動化客戶服務回應
- <strong>產品文件</strong>：智慧產品資訊檢索
- <strong>故障排除指南</strong>：情境問題解決協助
- <strong>常見問題系統</strong>：從文件集合動態生成 FAQ

### 法規合規
- <strong>法律文件分析</strong>：合約及法律文件智能分析
- <strong>合規監控</strong>：自動化法規合規檢查
- <strong>風險評估</strong>：基於文件的風險分析與報告
- <strong>稽核支援</strong>：智慧文件發現協助稽核

## 🚀 產線部署

### 監控與可觀察性
- **Application Insights**：詳細遙測與效能監控
- <strong>自訂指標</strong>：商業特定 KPI 追蹤與警示
- <strong>分散式追蹤</strong>：跨服務的端到端請求追蹤
- <strong>健康儀表板</strong>：即時系統健康與效能視覺化

### 可擴充性與可靠性
- <strong>自動調整大小</strong>：依負載與效能指標自動擴縮
- <strong>高可用性</strong>：多區域部署與故障轉移能力
- <strong>負載測試</strong>：企業負載條件下的效能驗證
- <strong>災難復原</strong>：自動化備份與復原程序

準備好建立可處理大量敏感文件的企業級 RAG 系統了嗎？讓我們為企業打造智慧知識系統！🏢📖✨

## 程式碼實作

本課程的完整可用程式碼範例在 `05-dotnet-agent-framework.cs`。

執行範例：

```bash
# 使腳本可執行（Linux/macOS）
chmod +x 05-dotnet-agent-framework.cs

# 執行 .NET 單一檔案應用程式
./05-dotnet-agent-framework.cs
```

或直接使用 `dotnet run`：

```bash
dotnet run 05-dotnet-agent-framework.cs
```

程式碼示範：

1. <strong>套件安裝</strong>：安裝 Azure AI Agents 所需的 NuGet 套件
2. <strong>環境設定</strong>：載入 Microsoft Foundry 端點與模型設定
3. <strong>文件上傳</strong>：上傳文件進行 RAG 處理
4. <strong>向量庫建立</strong>：建立用於語意搜尋的向量庫
5. <strong>代理設定</strong>：設定具檔案搜尋能力的 AI 代理
6. <strong>查詢執行</strong>：針對上傳文件執行查詢

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**免責聲明**：
此文件已使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們努力追求準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於關鍵資訊，建議採用專業人工翻譯。我們不對因使用此翻譯所產生的任何誤解或誤譯承擔責任。
<!-- CO-OP TRANSLATOR DISCLAIMER END -->