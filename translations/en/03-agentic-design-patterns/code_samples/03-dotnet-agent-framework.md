<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c8bc231a26e949f525d65b716538707f",
  "translation_date": "2025-11-07T09:42:05+00:00",
  "source_file": "03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.md",
  "language_code": "en"
}
-->
# 🎨 Agentic Design Patterns with GitHub Models (.NET)

## 📋 Learning Objectives

This notebook showcases enterprise-level design patterns for creating intelligent agents using the Microsoft Agent Framework in .NET, integrated with GitHub Models. You'll explore professional patterns and architectural strategies that ensure agents are production-ready, maintainable, and scalable.

**Enterprise Design Patterns:**
- 🏭 **Factory Pattern**: Standardized agent creation with dependency injection
- 🔧 **Builder Pattern**: Fluent agent configuration and setup
- 🧵 **Thread-Safe Patterns**: Managing concurrent conversations
- 📋 **Repository Pattern**: Organized management of tools and capabilities

## 🎯 .NET-Specific Architectural Benefits

### Enterprise Features
- **Strong Typing**: Compile-time validation and IntelliSense support
- **Dependency Injection**: Integrated DI container support
- **Configuration Management**: IConfiguration and Options patterns
- **Async/Await**: Native support for asynchronous programming

### Production-Ready Patterns
- **Logging Integration**: ILogger and structured logging support
- **Health Checks**: Built-in monitoring and diagnostics
- **Configuration Validation**: Strong typing with data annotations
- **Error Handling**: Structured exception management

## 🔧 Technical Architecture

### Core .NET Components
- **Microsoft.Extensions.AI**: Unified AI service abstractions
- **Microsoft.Agents.AI**: Enterprise agent orchestration framework
- **GitHub Models Integration**: High-performance API client patterns
- **Configuration System**: appsettings.json and environment integration

### Design Pattern Implementation
```csharp
IServiceCollection → Agent Builder → Configuration → Tool Registry → AI Agent
```

## 🏗️ Enterprise Patterns Demonstrated

### 1. **Creational Patterns**
- **Agent Factory**: Centralized agent creation with consistent configuration
- **Builder Pattern**: Fluent API for complex agent configuration
- **Singleton Pattern**: Shared resources and configuration management
- **Dependency Injection**: Loose coupling and testability

### 2. **Behavioral Patterns**
- **Strategy Pattern**: Interchangeable tool execution strategies
- **Command Pattern**: Encapsulated agent operations with undo/redo
- **Observer Pattern**: Event-driven agent lifecycle management
- **Template Method**: Standardized agent execution workflows

### 3. **Structural Patterns**
- **Adapter Pattern**: GitHub Models API integration layer
- **Decorator Pattern**: Agent capability enhancement
- **Facade Pattern**: Simplified agent interaction interfaces
- **Proxy Pattern**: Lazy loading and caching for performance

## ⚙️ Prerequisites & Setup

**Development Environment:**
- .NET 9.0 SDK or higher
- Visual Studio 2022 or VS Code with C# extension
- GitHub Models API access

**NuGet Dependencies:**
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

## 📚 .NET Design Principles

### SOLID Principles
- **Single Responsibility**: Each component has one clear purpose
- **Open/Closed**: Extensible without modification
- **Liskov Substitution**: Interface-based tool implementations
- **Interface Segregation**: Focused, cohesive interfaces
- **Dependency Inversion**: Depend on abstractions, not concretions

### Clean Architecture
- **Domain Layer**: Core agent and tool abstractions
- **Application Layer**: Agent orchestration and workflows
- **Infrastructure Layer**: GitHub Models integration and external services
- **Presentation Layer**: User interaction and response formatting

## 🔒 Enterprise Considerations

### Security
- **Credential Management**: Secure API key handling with IConfiguration
- **Input Validation**: Strong typing and data annotation validation
- **Output Sanitization**: Secure response processing and filtering
- **Audit Logging**: Comprehensive operation tracking

### Performance
- **Async Patterns**: Non-blocking I/O operations
- **Connection Pooling**: Efficient HTTP client management
- **Caching**: Response caching for improved performance
- **Resource Management**: Proper disposal and cleanup patterns

### Scalability
- **Thread Safety**: Concurrent agent execution support
- **Resource Pooling**: Efficient resource utilization
- **Load Management**: Rate limiting and backpressure handling
- **Monitoring**: Performance metrics and health checks

## 🚀 Production Deployment

- **Configuration Management**: Environment-specific settings
- **Logging Strategy**: Structured logging with correlation IDs
- **Error Handling**: Global exception handling with proper recovery
- **Monitoring**: Application insights and performance counters
- **Testing**: Unit tests, integration tests, and load testing patterns

Ready to build enterprise-grade intelligent agents with .NET? Let's architect something robust! 🏢✨

## Code Sample

For a complete working example, see [03-dotnet-agent-framework.cs](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs).

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.