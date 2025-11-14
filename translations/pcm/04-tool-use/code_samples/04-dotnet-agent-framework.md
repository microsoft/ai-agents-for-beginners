<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f82a3992438bcc028a2569c5fed828a9",
  "translation_date": "2025-11-11T14:14:06+00:00",
  "source_file": "04-tool-use/code_samples/04-dotnet-agent-framework.md",
  "language_code": "pcm"
}
-->
# 🛠️ Advanced Tool Use wit GitHub Models (.NET)

## 📋 Wetin You Go Learn

Dis notebook dey show how enterprise-level tool integration dey work wit Microsoft Agent Framework for .NET wit GitHub Models. You go sabi how to build agents wey get plenty special tools, dey use C# strong typing and .NET enterprise features.

**Advanced Tool Skills Weh You Go Master:**
- 🔧 **Multi-Tool Architecture**: How to build agents wey get plenty special skills
- 🎯 **Type-Safe Tool Execution**: How to use C# compile-time validation
- 📊 **Enterprise Tool Patterns**: How to design tools wey fit production and handle errors well
- 🔗 **Tool Composition**: How to join tools together for complex business work

## 🎯 Benefits of .NET Tool Architecture

### Enterprise Tool Features
- **Compile-Time Validation**: Strong typing dey make sure say tool parameters dey correct
- **Dependency Injection**: IoC container dey help manage tools
- **Async/Await Patterns**: Non-blocking tool execution wey manage resources well
- **Structured Logging**: Built-in logging dey monitor tool execution

### Patterns Weh Fit Production
- **Exception Handling**: Better error management wit typed exceptions
- **Resource Management**: Correct disposal patterns and memory management
- **Performance Monitoring**: Built-in metrics and performance counters
- **Configuration Management**: Type-safe configuration wey dey validate

## 🔧 Technical Architecture

### Main .NET Tool Components
- **Microsoft.Extensions.AI**: Unified tool abstraction layer
- **Microsoft.Agents.AI**: Enterprise-level tool orchestration
- **GitHub Models Integration**: High-performance API client wey get connection pooling

### Tool Execution Pipeline
```
User Request → Agent Analysis → Tool Selection → Type Validation
                 ↓               ↓              ↓
         Parameter Binding → Tool Execution → Result Processing → Response
```

## 🛠️ Tool Categories & Patterns

### 1. **Data Processing Tools**
- **Input Validation**: Strong typing wit data annotations
- **Transform Operations**: Type-safe data conversion and formatting
- **Business Logic**: Domain-specific calculation and analysis tools
- **Output Formatting**: Structured response generation

### 2. **Integration Tools** 
- **API Connectors**: RESTful service integration wit HttpClient
- **Database Tools**: Entity Framework dey help access data
- **File Operations**: Secure file system operations wit validation
- **External Services**: Patterns for third-party service integration

### 3. **Utility Tools**
- **Text Processing**: String manipulation and formatting utilities
- **Date/Time Operations**: Culture-aware date/time calculations
- **Mathematical Tools**: Precision calculations and statistical operations
- **Validation Tools**: Business rule validation and data verification

## ⚙️ Wetin You Need & Setup

**Development Environment:**
- .NET 9.0 SDK or higher
- Visual Studio 2022 or VS Code wit C# extension
- GitHub Models API access

**NuGet Packages Weh You Need:**
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

Ready to build enterprise-level agents wey get strong, type-safe tool skills for .NET? Make we start dey architect professional-grade solutions! 🏢⚡

## 💻 Code Implementation

The full C# implementation dey for the companion file `04-dotnet-agent-framework.cs`. Dis .NET Single File App dey show:

- How to load environment variables for GitHub Models configuration
- How to define custom tools wit C# methods wey get attributes
- How to create AI agent wey dey integrate tools
- How to manage conversation threads
- How to execute agent requests wit tool invocation

To run the example:

```bash
chmod +x 04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

Or use the .NET CLI:

```bash
dotnet run 04-dotnet-agent-framework.cs
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator) do di translation. Even though we dey try make am accurate, abeg make you sabi say automated translations fit get mistake or no dey correct well. Di original dokyument for im native language na di one wey you go take as di correct source. For important information, e better make professional human translation dey use. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->