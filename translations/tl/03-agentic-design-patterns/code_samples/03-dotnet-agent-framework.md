<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c8bc231a26e949f525d65b716538707f",
  "translation_date": "2025-11-07T09:50:05+00:00",
  "source_file": "03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.md",
  "language_code": "tl"
}
-->
# 🎨 Mga Pattern ng Disenyo ng Agentic gamit ang GitHub Models (.NET)

## 📋 Mga Layunin sa Pag-aaral

Ipinapakita ng notebook na ito ang mga disenyo ng pattern na pang-enterprise para sa paggawa ng mga intelligent agents gamit ang Microsoft Agent Framework sa .NET na may integrasyon ng GitHub Models. Matutunan mo ang mga propesyonal na pattern at mga diskarte sa arkitektura na ginagawang handa para sa produksyon, madaling mapanatili, at scalable ang mga agents.

**Mga Pattern ng Disenyo ng Pang-enterprise:**
- 🏭 **Factory Pattern**: Standardisadong paggawa ng agent gamit ang dependency injection
- 🔧 **Builder Pattern**: Fluent na pag-configure at pag-setup ng agent
- 🧵 **Thread-Safe Patterns**: Pamamahala ng sabay-sabay na pag-uusap
- 📋 **Repository Pattern**: Organisadong pamamahala ng tool at kakayahan

## 🎯 Mga Benepisyo ng Arkitektura ng .NET

### Mga Tampok ng Pang-enterprise
- **Strong Typing**: Pag-validate sa compile-time at suporta sa IntelliSense
- **Dependency Injection**: Built-in na integrasyon ng DI container
- **Pamamahala ng Configuration**: IConfiguration at Options patterns
- **Async/Await**: Suporta sa asynchronous programming bilang pangunahing tampok

### Mga Pattern na Handa para sa Produksyon
- **Logging Integration**: Suporta sa ILogger at structured logging
- **Health Checks**: Built-in na monitoring at diagnostics
- **Configuration Validation**: Strong typing gamit ang data annotations
- **Error Handling**: Structured na pamamahala ng exception

## 🔧 Arkitektura ng Teknikal

### Mga Pangunahing Komponent ng .NET
- **Microsoft.Extensions.AI**: Unified na abstraction ng AI service
- **Microsoft.Agents.AI**: Enterprise na framework para sa orchestration ng agent
- **GitHub Models Integration**: Mga pattern ng API client na mataas ang performance
- **Configuration System**: Integrasyon ng appsettings.json at environment

### Pagpapatupad ng Pattern ng Disenyo
```csharp
IServiceCollection → Agent Builder → Configuration → Tool Registry → AI Agent
```

## 🏗️ Mga Pattern ng Pang-enterprise na Ipinakita

### 1. **Creational Patterns**
- **Agent Factory**: Sentralisadong paggawa ng agent na may pare-parehong configuration
- **Builder Pattern**: Fluent na API para sa komplikadong configuration ng agent
- **Singleton Pattern**: Pamamahala ng shared resources at configuration
- **Dependency Injection**: Loose coupling at testability

### 2. **Behavioral Patterns**
- **Strategy Pattern**: Mga interchangeable na estratehiya sa pag-execute ng tool
- **Command Pattern**: Encapsulated na operasyon ng agent na may undo/redo
- **Observer Pattern**: Pamamahala ng lifecycle ng agent na batay sa event
- **Template Method**: Standardisadong workflows ng pag-execute ng agent

### 3. **Structural Patterns**
- **Adapter Pattern**: Layer ng integrasyon ng GitHub Models API
- **Decorator Pattern**: Pagpapahusay ng kakayahan ng agent
- **Facade Pattern**: Simpleng interface para sa interaksyon ng agent
- **Proxy Pattern**: Lazy loading at caching para sa performance

## ⚙️ Mga Kinakailangan at Setup

**Kapaligiran ng Pag-develop:**
- .NET 9.0 SDK o mas mataas
- Visual Studio 2022 o VS Code na may C# extension
- Access sa GitHub Models API

**Mga Dependency ng NuGet:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Configuration (.env file):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 📚 Mga Prinsipyo ng Disenyo ng .NET

### SOLID Principles
- **Single Responsibility**: Ang bawat component ay may isang malinaw na layunin
- **Open/Closed**: Maaaring palawakin nang hindi binabago
- **Liskov Substitution**: Mga implementasyon ng tool na batay sa interface
- **Interface Segregation**: Nakatuon at cohesive na mga interface
- **Dependency Inversion**: Umaasa sa mga abstraction, hindi sa mga konkretong bagay

### Clean Architecture
- **Domain Layer**: Mga pangunahing abstraction ng agent at tool
- **Application Layer**: Orchestration ng agent at workflows
- **Infrastructure Layer**: Integrasyon ng GitHub Models at mga external na serbisyo
- **Presentation Layer**: Interaksyon ng user at pag-format ng tugon

## 🔒 Mga Pagsasaalang-alang sa Pang-enterprise

### Seguridad
- **Pamamahala ng Kredensyal**: Secure na paghawak ng API key gamit ang IConfiguration
- **Pag-validate ng Input**: Strong typing at validation gamit ang data annotation
- **Pag-sanitize ng Output**: Secure na pagproseso at pag-filter ng tugon
- **Audit Logging**: Komprehensibong pagsubaybay sa operasyon

### Performance
- **Async Patterns**: Non-blocking na mga I/O operation
- **Connection Pooling**: Mahusay na pamamahala ng HTTP client
- **Caching**: Pag-cache ng tugon para sa mas mahusay na performance
- **Pamamahala ng Resource**: Tamang disposal at cleanup patterns

### Scalability
- **Thread Safety**: Suporta sa sabay-sabay na pag-execute ng agent
- **Resource Pooling**: Mahusay na paggamit ng resources
- **Load Management**: Rate limiting at pamamahala ng backpressure
- **Monitoring**: Mga performance metrics at health checks

## 🚀 Deployment sa Produksyon

- **Pamamahala ng Configuration**: Mga setting na partikular sa environment
- **Logging Strategy**: Structured logging na may correlation IDs
- **Error Handling**: Global na pamamahala ng exception na may tamang recovery
- **Monitoring**: Application insights at performance counters
- **Testing**: Mga unit test, integration test, at load testing patterns

Handa ka na bang gumawa ng mga intelligent agents na pang-enterprise gamit ang .NET? Mag-arkitekto tayo ng isang matibay na sistema! 🏢✨

## Halimbawa ng Code

Para sa kumpletong gumaganang halimbawa, tingnan ang [03-dotnet-agent-framework.cs](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs).

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na mapagkakatiwalaang pinagmulan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.