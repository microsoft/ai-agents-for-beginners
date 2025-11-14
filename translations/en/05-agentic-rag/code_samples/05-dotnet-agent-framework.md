<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c268705e6fb2b30c7690d5b2a002e072",
  "translation_date": "2025-11-07T08:55:27+00:00",
  "source_file": "05-agentic-rag/code_samples/05-dotnet-agent-framework.md",
  "language_code": "en"
}
-->
# 🔍 Enterprise RAG with Azure AI Foundry (.NET)

## 📋 Learning Objectives

This notebook explains how to create enterprise-level Retrieval-Augmented Generation (RAG) systems using the Microsoft Agent Framework in .NET with Azure AI Foundry. You'll learn to develop production-ready agents capable of searching through documents and delivering precise, context-aware responses while ensuring enterprise security and scalability.

**Enterprise RAG Capabilities You'll Build:**
- 📚 **Document Intelligence**: Advanced document processing using Azure AI services
- 🔍 **Semantic Search**: High-performance vector search with enterprise-grade features
- 🛡️ **Security Integration**: Role-based access control and data protection strategies
- 🏢 **Scalable Architecture**: Production-ready RAG systems with monitoring capabilities

## 🎯 Enterprise RAG Architecture

### Core Enterprise Components
- **Azure AI Foundry**: A managed enterprise AI platform with built-in security and compliance
- **Persistent Agents**: Stateful agents that maintain conversation history and context
- **Vector Store Management**: Enterprise-grade indexing and retrieval for documents
- **Identity Integration**: Azure AD authentication and role-based access control

### .NET Enterprise Benefits
- **Type Safety**: Compile-time validation for RAG operations and data structures
- **Async Performance**: Non-blocking operations for document processing and search
- **Memory Management**: Efficient resource handling for large document collections
- **Integration Patterns**: Seamless integration with Azure services using dependency injection

## 🏗️ Technical Architecture

### Enterprise RAG Pipeline
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Core .NET Components
- **Azure.AI.Agents.Persistent**: Enterprise agent management with state persistence
- **Azure.Identity**: Integrated authentication for secure access to Azure services
- **Microsoft.Agents.AI.AzureAI**: Azure-optimized implementation of the agent framework
- **System.Linq.Async**: High-performance asynchronous LINQ operations

## 🔧 Enterprise Features & Benefits

### Security & Compliance
- **Azure AD Integration**: Enterprise-grade identity management and authentication
- **Role-Based Access**: Granular permissions for document access and operations
- **Data Protection**: Encryption for sensitive documents both at rest and in transit
- **Audit Logging**: Comprehensive activity tracking for compliance purposes

### Performance & Scalability
- **Connection Pooling**: Efficient management of Azure service connections
- **Async Processing**: Non-blocking operations for high-throughput scenarios
- **Caching Strategies**: Smart caching for frequently accessed documents
- **Load Balancing**: Distributed processing for large-scale deployments

### Management & Monitoring
- **Health Checks**: Built-in monitoring for RAG system components
- **Performance Metrics**: Detailed analytics on search quality and response times
- **Error Handling**: Robust exception management with retry policies
- **Configuration Management**: Environment-specific settings with validation

## ⚙️ Prerequisites & Setup

**Development Environment:**
- .NET 9.0 SDK or higher
- Visual Studio 2022 or VS Code with the C# extension
- Azure subscription with access to AI Foundry

**Required NuGet Packages:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Azure Authentication Setup:**
```bash
# Install Azure CLI and authenticate
az login
az account set --subscription "your-subscription-id"
```

**Environment Configuration:**
* Azure AI Foundry configuration (automatically handled via Azure CLI)
* Ensure authentication to the correct Azure subscription

## 📊 Enterprise RAG Patterns

### Document Management Patterns
- **Bulk Upload**: Efficient handling of large document collections
- **Incremental Updates**: Real-time addition and modification of documents
- **Version Control**: Tracking changes and versions of documents
- **Metadata Management**: Rich attributes and taxonomy for documents

### Search & Retrieval Patterns
- **Hybrid Search**: Combining semantic and keyword search for optimal results
- **Faceted Search**: Multi-dimensional filtering and categorization
- **Relevance Tuning**: Custom scoring algorithms tailored to specific domains
- **Result Ranking**: Advanced ranking with integrated business logic

### Security Patterns
- **Document-Level Security**: Granular access control for individual documents
- **Data Classification**: Automatic sensitivity labeling and protection
- **Audit Trails**: Comprehensive logging of all RAG operations
- **Privacy Protection**: Detection and redaction of personally identifiable information (PII)

## 🔒 Enterprise Security Features

### Authentication & Authorization
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

### Data Protection
- **Encryption**: End-to-end encryption for documents and search indices
- **Access Controls**: Integration with Azure AD for user and group permissions
- **Data Residency**: Geographic controls for data location compliance
- **Backup & Recovery**: Automated backup and disaster recovery capabilities

## 📈 Performance Optimization

### Async Processing Patterns
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Memory Management
- **Streaming Processing**: Efficient handling of large documents without memory overload
- **Resource Pooling**: Reuse of expensive resources for better efficiency
- **Garbage Collection**: Optimized memory allocation and cleanup
- **Connection Management**: Proper lifecycle management of Azure service connections

### Caching Strategies
- **Query Caching**: Cache frequently executed searches
- **Document Caching**: In-memory caching for frequently accessed documents
- **Index Caching**: Optimized caching for vector indices
- **Result Caching**: Smart caching of generated responses

## 📊 Enterprise Use Cases

### Knowledge Management
- **Corporate Wiki**: Intelligent search across company knowledge bases
- **Policy & Procedures**: Automated guidance for compliance and procedures
- **Training Materials**: Intelligent assistance for learning and development
- **Research Databases**: Analysis systems for academic and research papers

### Customer Support
- **Support Knowledge Base**: Automated responses for customer service
- **Product Documentation**: Intelligent retrieval of product information
- **Troubleshooting Guides**: Contextual assistance for problem-solving
- **FAQ Systems**: Dynamic generation of FAQs from document collections

### Regulatory Compliance
- **Legal Document Analysis**: Intelligence for contracts and legal documents
- **Compliance Monitoring**: Automated checks for regulatory compliance
- **Risk Assessment**: Document-based risk analysis and reporting
- **Audit Support**: Intelligent discovery of documents for audits

## 🚀 Production Deployment

### Monitoring & Observability
- **Application Insights**: Detailed telemetry and performance monitoring
- **Custom Metrics**: Tracking and alerting for business-specific KPIs
- **Distributed Tracing**: End-to-end tracking of requests across services
- **Health Dashboards**: Real-time visualization of system health and performance

### Scalability & Reliability
- **Auto-Scaling**: Automatic scaling based on load and performance metrics
- **High Availability**: Multi-region deployment with failover capabilities
- **Load Testing**: Validation of performance under enterprise-level loads
- **Disaster Recovery**: Automated backup and recovery procedures

Ready to create enterprise-grade RAG systems capable of handling sensitive documents at scale? Let's design intelligent knowledge systems for the enterprise! 🏢📖✨

## Code Implementation

The complete working code sample for this lesson is available in `05-dotnet-agent-framework.cs`. 

To run the example:

```bash
# Make the script executable (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Run the .NET Single File App
./05-dotnet-agent-framework.cs
```

Or use `dotnet run` directly:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

The code demonstrates:

1. **Package Installation**: Installing required NuGet packages for Azure AI Agents
2. **Environment Configuration**: Loading Azure AI Foundry endpoint and model settings
3. **Document Upload**: Uploading a document for RAG processing
4. **Vector Store Creation**: Creating a vector store for semantic search
5. **Agent Configuration**: Setting up an AI agent with file search capabilities
6. **Query Execution**: Running queries against the uploaded document

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.