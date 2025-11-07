<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f82a3992438bcc028a2569c5fed828a9",
  "translation_date": "2025-11-07T09:27:01+00:00",
  "source_file": "04-tool-use/code_samples/04-dotnet-agent-framework.md",
  "language_code": "tl"
}
-->
# 🛠️ Advanced Tool Use with GitHub Models (.NET)

## 📋 Mga Layunin sa Pag-aaral

Ipinapakita ng notebook na ito ang mga pattern ng enterprise-grade tool integration gamit ang Microsoft Agent Framework sa .NET kasama ang GitHub Models. Matutunan mong bumuo ng mga sopistikadong agent na may maraming espesyal na tools, gamit ang malakas na typing ng C# at mga enterprise features ng .NET.

**Mga Advanced na Kakayahan ng Tool na Iyong Matututunan:**
- 🔧 **Multi-Tool Architecture**: Pagbuo ng mga agent na may maraming espesyal na kakayahan
- 🎯 **Type-Safe Tool Execution**: Paggamit ng compile-time validation ng C#
- 📊 **Enterprise Tool Patterns**: Disenyo ng tool na handa para sa produksyon at error handling
- 🔗 **Tool Composition**: Pagsasama-sama ng mga tool para sa masalimuot na mga workflow ng negosyo

## 🎯 Mga Benepisyo ng .NET Tool Architecture

### Mga Tampok ng Enterprise Tool
- **Compile-Time Validation**: Tinitiyak ng malakas na typing ang tamang parameter ng tool
- **Dependency Injection**: IoC container integration para sa pamamahala ng tool
- **Async/Await Patterns**: Non-blocking na pagpapatupad ng tool na may tamang pamamahala ng resources
- **Structured Logging**: Built-in logging integration para sa pagsubaybay sa pagpapatupad ng tool

### Mga Pattern na Handa para sa Produksyon
- **Exception Handling**: Komprehensibong pamamahala ng error gamit ang typed exceptions
- **Resource Management**: Tamang disposal patterns at pamamahala ng memorya
- **Performance Monitoring**: Built-in metrics at performance counters
- **Configuration Management**: Type-safe na configuration na may validation

## 🔧 Teknikal na Arkitektura

### Mga Core na Komponent ng .NET Tool
- **Microsoft.Extensions.AI**: Unified tool abstraction layer
- **Microsoft.Agents.AI**: Enterprise-grade na tool orchestration
- **GitHub Models Integration**: High-performance API client na may connection pooling

### Tool Execution Pipeline
```
User Request → Agent Analysis → Tool Selection → Type Validation
                 ↓               ↓              ↓
         Parameter Binding → Tool Execution → Result Processing → Response
```

## 🛠️ Mga Kategorya ng Tool at Mga Pattern

### 1. **Mga Tool sa Pagproseso ng Data**
- **Input Validation**: Malakas na typing gamit ang data annotations
- **Transform Operations**: Type-safe na conversion at formatting ng data
- **Business Logic**: Mga domain-specific na kalkulasyon at analysis tools
- **Output Formatting**: Structured na pagbuo ng tugon

### 2. **Mga Integration Tools** 
- **API Connectors**: RESTful service integration gamit ang HttpClient
- **Database Tools**: Entity Framework integration para sa pag-access ng data
- **File Operations**: Secure na operasyon sa file system na may validation
- **External Services**: Mga pattern ng integration sa third-party na serbisyo

### 3. **Mga Utility Tools**
- **Text Processing**: String manipulation at formatting utilities
- **Date/Time Operations**: Culture-aware na kalkulasyon ng petsa/oras
- **Mathematical Tools**: Precision calculations at statistical operations
- **Validation Tools**: Business rule validation at data verification

## ⚙️ Mga Kinakailangan at Setup

**Development Environment:**
- .NET 9.0 SDK o mas mataas
- Visual Studio 2022 o VS Code na may C# extension
- Access sa GitHub Models API

**Mga Kinakailangang NuGet Packages:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Configuration ng Environment (.env file):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

Handa ka na bang bumuo ng mga agent na pang-enterprise na may makapangyarihan at type-safe na kakayahan ng tool sa .NET? Simulan na natin ang pag-arkitekto ng mga solusyon na pang-propesyonal! 🏢⚡

## 💻 Implementasyon ng Code

Ang kumpletong implementasyon ng C# ay makikita sa kasamang file na `04-dotnet-agent-framework.cs`. Ipinapakita ng .NET Single File App na ito ang:

- Pag-load ng mga environment variable para sa configuration ng GitHub Models
- Pagde-define ng mga custom na tool gamit ang mga C# method na may attributes
- Paglikha ng AI agent na may tool integration
- Pamamahala ng mga conversation thread
- Pagpapatupad ng mga request ng agent gamit ang tool invocation

Para patakbuhin ang halimbawa:

```bash
chmod +x 04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

O gamit ang .NET CLI:

```bash
dotnet run 04-dotnet-agent-framework.cs
```

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na mapagkakatiwalaang pinagmulan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.