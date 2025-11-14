<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f82a3992438bcc028a2569c5fed828a9",
  "translation_date": "2025-11-07T09:20:23+00:00",
  "source_file": "04-tool-use/code_samples/04-dotnet-agent-framework.md",
  "language_code": "en"
}
-->
# 🛠️ Advanced Tool Use with GitHub Models (.NET)

## 📋 Learning Objectives

This notebook showcases enterprise-level tool integration patterns using the Microsoft Agent Framework in .NET with GitHub Models. You'll learn how to create advanced agents equipped with multiple specialized tools, taking advantage of C#'s strong typing and .NET's robust enterprise features.

**Advanced Tool Capabilities You'll Master:**
- 🔧 **Multi-Tool Architecture**: Designing agents with diverse specialized functionalities
- 🎯 **Type-Safe Tool Execution**: Utilizing C#'s compile-time validation
- 📊 **Enterprise Tool Patterns**: Developing production-ready tools with effective error handling
- 🔗 **Tool Composition**: Integrating tools for complex business workflows

## 🎯 .NET Tool Architecture Benefits

### Enterprise Tool Features
- **Compile-Time Validation**: Strong typing ensures the correctness of tool parameters
- **Dependency Injection**: Integration with IoC containers for efficient tool management
- **Async/Await Patterns**: Non-blocking tool execution with optimized resource handling
- **Structured Logging**: Built-in logging support for monitoring tool execution

### Production-Ready Patterns
- **Exception Handling**: Robust error management with typed exceptions
- **Resource Management**: Proper disposal practices and memory optimization
- **Performance Monitoring**: Integrated metrics and performance tracking
- **Configuration Management**: Type-safe configuration with validation mechanisms

## 🔧 Technical Architecture

### Core .NET Tool Components
- **Microsoft.Extensions.AI**: Unified abstraction layer for tools
- **Microsoft.Agents.AI**: Enterprise-grade orchestration for tools
- **GitHub Models Integration**: High-performance API client with connection pooling

### Tool Execution Pipeline
```
User Request → Agent Analysis → Tool Selection → Type Validation
                 ↓               ↓              ↓
         Parameter Binding → Tool Execution → Result Processing → Response
```

## 🛠️ Tool Categories & Patterns

### 1. **Data Processing Tools**
- **Input Validation**: Strong typing with data annotations
- **Transform Operations**: Type-safe data conversion and formatting
- **Business Logic**: Tools for domain-specific calculations and analyses
- **Output Formatting**: Generating structured responses

### 2. **Integration Tools** 
- **API Connectors**: RESTful service integration using HttpClient
- **Database Tools**: Data access integration with Entity Framework
- **File Operations**: Secure file system operations with validation
- **External Services**: Patterns for integrating third-party services

### 3. **Utility Tools**
- **Text Processing**: Utilities for string manipulation and formatting
- **Date/Time Operations**: Culture-aware calculations for dates and times
- **Mathematical Tools**: Precision calculations and statistical utilities
- **Validation Tools**: Verification of business rules and data integrity

## ⚙️ Prerequisites & Setup

**Development Environment:**
- .NET 9.0 SDK or higher
- Visual Studio 2022 or VS Code with the C# extension
- GitHub Models API access

**Required NuGet Packages:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Environment Configuration (.env file):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

Ready to create enterprise-grade agents with powerful, type-safe tool capabilities in .NET? Let's design some professional solutions! 🏢⚡

## 💻 Code Implementation

The complete C# implementation is available in the companion file `04-dotnet-agent-framework.cs`. This .NET Single File App demonstrates:

- Loading environment variables for GitHub Models configuration
- Defining custom tools using C# methods with attributes
- Creating an AI agent with integrated tools
- Managing conversation threads
- Executing agent requests with tool invocation

To run the example:

```bash
chmod +x 04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

Or using the .NET CLI:

```bash
dotnet run 04-dotnet-agent-framework.cs
```

---

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we aim for accuracy, please note that automated translations may include errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is advised. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.