<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c268705e6fb2b30c7690d5b2a002e072",
  "translation_date": "2025-11-07T09:06:59+00:00",
  "source_file": "05-agentic-rag/code_samples/05-dotnet-agent-framework.md",
  "language_code": "tl"
}
-->
# 🔍 Enterprise RAG gamit ang Azure AI Foundry (.NET)

## 📋 Mga Layunin sa Pag-aaral

Ipinapakita ng notebook na ito kung paano bumuo ng mga enterprise-grade na Retrieval-Augmented Generation (RAG) systems gamit ang Microsoft Agent Framework sa .NET kasama ang Azure AI Foundry. Matutunan mong lumikha ng mga production-ready na agent na kayang maghanap sa mga dokumento at magbigay ng tumpak, may kontekstong sagot na may enterprise security at scalability.

**Mga Kakayahan ng Enterprise RAG na Iyong Bubuuin:**
- 📚 **Intelligence sa Dokumento**: Advanced na pagproseso ng dokumento gamit ang Azure AI services
- 🔍 **Semantic Search**: Mataas na performance na vector search na may enterprise features
- 🛡️ **Integrasyon ng Seguridad**: Role-based access at mga pattern ng proteksyon ng data
- 🏢 **Scalable Architecture**: Production-ready na RAG systems na may monitoring

## 🎯 Arkitektura ng Enterprise RAG

### Mga Pangunahing Komponent ng Enterprise
- **Azure AI Foundry**: Managed enterprise AI platform na may seguridad at pagsunod
- **Persistent Agents**: Mga agent na may stateful na conversation history at context management
- **Vector Store Management**: Enterprise-grade na pag-index at retrieval ng dokumento
- **Identity Integration**: Azure AD authentication at role-based access control

### Mga Benepisyo ng .NET Enterprise
- **Type Safety**: Compile-time validation para sa mga RAG operations at data structures
- **Async Performance**: Non-blocking na pagproseso ng dokumento at mga search operations
- **Memory Management**: Epektibong paggamit ng resources para sa malalaking koleksyon ng dokumento
- **Integration Patterns**: Native na integrasyon ng Azure service gamit ang dependency injection

## 🏗️ Teknikal na Arkitektura

### Enterprise RAG Pipeline
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Mga Pangunahing Komponent ng .NET
- **Azure.AI.Agents.Persistent**: Pamamahala ng enterprise agent na may state persistence
- **Azure.Identity**: Integrated authentication para sa secure na access sa Azure services
- **Microsoft.Agents.AI.AzureAI**: Azure-optimized na implementasyon ng agent framework
- **System.Linq.Async**: Mataas na performance na asynchronous LINQ operations

## 🔧 Mga Tampok at Benepisyo ng Enterprise

### Seguridad at Pagsunod
- **Azure AD Integration**: Pamamahala ng enterprise identity at authentication
- **Role-Based Access**: Fine-grained na mga pahintulot para sa access sa dokumento at mga operasyon
- **Proteksyon ng Data**: Encryption sa pahinga at sa transit para sa sensitibong mga dokumento
- **Audit Logging**: Komprehensibong pagsubaybay sa aktibidad para sa mga pangangailangan sa pagsunod

### Performance at Scalability
- **Connection Pooling**: Epektibong pamamahala ng koneksyon sa Azure services
- **Async Processing**: Non-blocking na mga operasyon para sa high-throughput na mga scenario
- **Caching Strategies**: Matalinong caching para sa madalas na ina-access na mga dokumento
- **Load Balancing**: Distributed na pagproseso para sa malakihang deployment

### Pamamahala at Monitoring
- **Health Checks**: Built-in na monitoring para sa mga komponent ng RAG system
- **Performance Metrics**: Detalyadong analytics sa kalidad ng search at response times
- **Error Handling**: Komprehensibong pamamahala ng exception na may retry policies
- **Configuration Management**: Mga setting na specific sa environment na may validation

## ⚙️ Mga Kinakailangan at Setup

**Development Environment:**
- .NET 9.0 SDK o mas mataas
- Visual Studio 2022 o VS Code na may C# extension
- Azure subscription na may access sa AI Foundry

**Mga Kinakailangang NuGet Packages:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Setup ng Azure Authentication:**
```bash
# Install Azure CLI and authenticate
az login
az account set --subscription "your-subscription-id"
```

**Configuration ng Environment:**
* Configuration ng Azure AI Foundry (awtomatikong pinamamahalaan gamit ang Azure CLI)
* Siguraduhing authenticated ka sa tamang Azure subscription

## 📊 Mga Pattern ng Enterprise RAG

### Mga Pattern sa Pamamahala ng Dokumento
- **Bulk Upload**: Epektibong pagproseso ng malalaking koleksyon ng dokumento
- **Incremental Updates**: Real-time na pagdagdag at pagbabago ng dokumento
- **Version Control**: Pag-track ng bersyon ng dokumento at mga pagbabago
- **Metadata Management**: Mayamang attributes ng dokumento at taxonomy

### Mga Pattern sa Search at Retrieval
- **Hybrid Search**: Pagsasama ng semantic at keyword search para sa optimal na resulta
- **Faceted Search**: Multi-dimensional na pag-filter at pag-categorize
- **Relevance Tuning**: Custom na scoring algorithms para sa domain-specific na pangangailangan
- **Result Ranking**: Advanced na ranking na may integrasyon ng business logic

### Mga Pattern sa Seguridad
- **Document-Level Security**: Fine-grained na access control kada dokumento
- **Data Classification**: Awtomatikong sensitivity labeling at proteksyon
- **Audit Trails**: Komprehensibong pag-log ng lahat ng RAG operations
- **Privacy Protection**: Pagtuklas at pag-redact ng PII

## 🔒 Mga Tampok ng Enterprise Security

### Authentication at Authorization
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

### Proteksyon ng Data
- **Encryption**: End-to-end na encryption para sa mga dokumento at search indices
- **Access Controls**: Integrasyon sa Azure AD para sa user at group permissions
- **Data Residency**: Geographic na kontrol sa lokasyon ng data para sa pagsunod
- **Backup & Recovery**: Awtomatikong backup at mga kakayahan sa disaster recovery

## 📈 Pag-optimize ng Performance

### Mga Pattern sa Async Processing
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Pamamahala ng Memory
- **Streaming Processing**: Pagproseso ng malalaking dokumento nang walang isyu sa memory
- **Resource Pooling**: Epektibong paggamit muli ng mga mahal na resources
- **Garbage Collection**: Na-optimize na mga pattern sa memory allocation
- **Connection Management**: Tamang lifecycle ng koneksyon sa Azure services

### Mga Caching Strategies
- **Query Caching**: Cache para sa madalas na isinasagawang mga search
- **Document Caching**: In-memory caching para sa mga hot documents
- **Index Caching**: Na-optimize na vector index caching
- **Result Caching**: Matalinong caching ng mga generated na sagot

## 📊 Mga Gamit ng Enterprise

### Pamamahala ng Kaalaman
- **Corporate Wiki**: Matalinong search sa mga knowledge base ng kumpanya
- **Policy & Procedures**: Awtomatikong compliance at gabay sa mga procedure
- **Training Materials**: Matalinong tulong sa pag-aaral at pag-develop
- **Research Databases**: Sistema ng pagsusuri ng academic at research papers

### Customer Support
- **Support Knowledge Base**: Awtomatikong sagot sa customer service
- **Product Documentation**: Matalinong retrieval ng impormasyon ng produkto
- **Troubleshooting Guides**: Kontekstwal na tulong sa pagresolba ng problema
- **FAQ Systems**: Dynamic na pagbuo ng FAQ mula sa mga koleksyon ng dokumento

### Regulatory Compliance
- **Legal Document Analysis**: Intelligence sa kontrata at legal na dokumento
- **Compliance Monitoring**: Awtomatikong pag-check ng regulatory compliance
- **Risk Assessment**: Pagsusuri ng panganib batay sa dokumento
- **Audit Support**: Matalinong paghanap ng dokumento para sa mga audit

## 🚀 Production Deployment

### Monitoring at Observability
- **Application Insights**: Detalyadong telemetry at monitoring ng performance
- **Custom Metrics**: Pagsubaybay at alerting ng business-specific na KPI
- **Distributed Tracing**: End-to-end na pagsubaybay ng request sa mga serbisyo
- **Health Dashboards**: Visualization ng real-time na kalusugan at performance ng sistema

### Scalability at Reliability
- **Auto-Scaling**: Awtomatikong pag-scale batay sa load at performance metrics
- **High Availability**: Multi-region na deployment na may failover capabilities
- **Load Testing**: Pag-validate ng performance sa ilalim ng enterprise load conditions
- **Disaster Recovery**: Awtomatikong backup at mga procedure sa recovery

Handa ka na bang bumuo ng enterprise-grade na RAG systems na kayang magproseso ng sensitibong mga dokumento sa malakihang scale? Mag-architect tayo ng matatalinong knowledge systems para sa enterprise! 🏢📖✨

## Implementasyon ng Code

Ang kumpletong working code sample para sa araling ito ay makikita sa `05-dotnet-agent-framework.cs`. 

Para patakbuhin ang halimbawa:

```bash
# Make the script executable (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Run the .NET Single File App
./05-dotnet-agent-framework.cs
```

O gamitin ang `dotnet run` nang direkta:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Ipinapakita ng code ang:

1. **Pag-install ng Package**: Pag-install ng kinakailangang NuGet packages para sa Azure AI Agents
2. **Configuration ng Environment**: Pag-load ng Azure AI Foundry endpoint at model settings
3. **Pag-upload ng Dokumento**: Pag-upload ng dokumento para sa RAG processing
4. **Paglikha ng Vector Store**: Paglikha ng vector store para sa semantic search
5. **Configuration ng Agent**: Pag-setup ng AI agent na may kakayahan sa file search
6. **Pagpapatakbo ng Query**: Pagpapatakbo ng mga query laban sa na-upload na dokumento

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na awtoritatibong pinagmulan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.