<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f5a5f2902f32272257506d88d3c43a1",
  "translation_date": "2025-11-07T09:17:57+00:00",
  "source_file": "08-multi-agent/code_samples/08-dotnet-agent-framework.md",
  "language_code": "tl"
}
-->
# 🤝 Enterprise Multi-Agent Workflow Systems (.NET)

## 📋 Mga Layunin sa Pag-aaral

Ang notebook na ito ay nagpapakita kung paano bumuo ng mga sopistikadong enterprise-grade multi-agent systems gamit ang Microsoft Agent Framework sa .NET na may GitHub Models. Matutunan mong mag-orchestrate ng maraming specialized agents na nagtutulungan sa pamamagitan ng mga structured workflows, gamit ang mga enterprise features ng .NET para sa mga production-ready na solusyon.

**Mga Kakayahan ng Enterprise Multi-Agent na Iyong Mabubuo:**
- 👥 **Pakikipagtulungan ng Agent**: Type-safe na koordinasyon ng agent na may compile-time validation
- 🔄 **Workflow Orchestration**: Deklaratibong pagdedepina ng workflow gamit ang async patterns ng .NET
- 🎭 **Role Specialization**: Malakas na uri ng personalidad ng agent at mga domain ng expertise
- 🏢 **Enterprise Integration**: Mga production-ready na pattern na may monitoring at error handling

## ⚙️ Mga Kinakailangan at Setup

**Kapaligiran ng Pag-develop:**
- .NET 9.0 SDK o mas mataas
- Visual Studio 2022 o VS Code na may C# extension
- Azure subscription (para sa mga persistent agents)

**Mga Kinakailangang NuGet Packages:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.4" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="9.8.0" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
```

## Halimbawa ng Code

Ang kumpletong gumaganang code para sa araling ito ay makikita sa kasamang C# file: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Para patakbuhin ang halimbawa:

```bash
# Make the file executable (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Run the sample
./08-dotnet-agent-framework.cs
```

O gamit ang .NET CLI:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Ano ang Ipinapakita ng Halimbawang Ito

Ang multi-agent workflow system na ito ay lumilikha ng hotel travel recommendation service na may dalawang specialized agents:

1. **FrontDesk Agent**: Isang travel agent na nagbibigay ng mga rekomendasyon sa aktibidad at lokasyon
2. **Concierge Agent**: Sinusuri ang mga rekomendasyon upang matiyak na authentic at hindi pangkaraniwang karanasan

Ang mga agents ay nagtutulungan sa isang workflow kung saan:
- Tumatanggap ang FrontDesk agent ng paunang travel request
- Sinusuri at pinapaganda ng Concierge agent ang rekomendasyon
- Ang workflow ay nag-stream ng mga tugon nang real-time

## Mga Pangunahing Konsepto

### Koordinasyon ng Agent
Ipinapakita ng halimbawa ang type-safe na koordinasyon ng agent gamit ang Microsoft Agent Framework na may compile-time validation.

### Workflow Orchestration
Gumagamit ng deklaratibong pagdedepina ng workflow gamit ang async patterns ng .NET upang ikonekta ang maraming agents sa isang pipeline.

### Streaming Responses
Nagpapatupad ng real-time na pag-stream ng mga tugon ng agent gamit ang async enumerables at event-driven architecture.

### Enterprise Integration
Ipinapakita ang mga production-ready na pattern kabilang ang:
- Configuration ng environment variable
- Secure na pamamahala ng credentials
- Error handling
- Asynchronous na pagproseso ng event

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.