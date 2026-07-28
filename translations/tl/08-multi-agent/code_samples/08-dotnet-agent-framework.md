# 🤝 Enterprise Multi-Agent Workflow Systems (.NET)

## 📋 Mga Layunin sa Pagkatuto

Ipinapakita ng notebook na ito kung paano bumuo ng sopistikadong enterprise-grade na multi-agent systems gamit ang Microsoft Agent Framework sa .NET kasama ang Azure OpenAI (Responses API). Matututuhan mong isaayos ang maraming espesyal na ahente na nagtutulungan sa pamamagitan ng mga istrukturadong workflow, gamit ang mga enterprise features ng .NET para sa mga solusyong handa na sa produksyon.

**Mga Kakayahan ng Enterprise Multi-Agent na Iyong Bubuuin:**
- 👥 **Agent Collaboration**: Type-safe na koordinasyon ng ahente na may compile-time validation
- 🔄 **Workflow Orchestration**: Declarative workflow definition gamit ang async patterns ng .NET
- 🎭 **Role Specialization**: Malakas ang tipong personalidad at larangan ng expertise ng ahente
- 🏢 **Enterprise Integration**: Mga pattern na handa na sa produksyon kasama ang monitoring at error handling

## ⚙️ Mga Kinakailangan at Setup

**Development Environment:**
- .NET 9.0 SDK o mas mataas pa
- Visual Studio 2022 o VS Code na may C# extension
- Azure subscription (para sa persistent agents)

**Mga Kinakailangang NuGet Packages:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="10.*" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.10" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="10.*" />
<PackageReference Include="OpenTelemetry.Api" Version="1.*" />
<PackageReference Include="Microsoft.Agents.AI.Workflows" Version="1.*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
```

## Halimbawa ng Code

Ang kumpletong gumaganang code para sa araling ito ay makikita sa kalakip na C# file: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Para patakbuhin ang halimbawa:

```bash
# Gawing executable ang file (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Patakbuhin ang halimbawa
./08-dotnet-agent-framework.cs
```

O gamit ang .NET CLI:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Ano ang Ipinapakita ng Halimbawang Ito

Gumagawa ang multi-agent workflow system na ito ng hotel travel recommendation service na may dalawang espesyalisadong ahente:

1. **FrontDesk Agent**: Isang travel agent na nagbibigay ng mga rekomendasyon para sa mga aktibidad at lokasyon
2. **Concierge Agent**: Sinusuri ang mga rekomendasyon upang matiyak na tunay at hindi turistang karanasan

Nagtutulungan ang mga ahente sa isang workflow kung saan:
- Tumatanggap ang FrontDesk agent ng unang kahilingan sa paglalakbay
- Sinusuri at pinapino ng Concierge agent ang rekomendasyon
- Ang workflow ay nagpapadala ng mga tugon nang real-time

## Pangunahing Mga Konsepto

### Koordinasyon ng Ahente
Ipinapakita ng halimbawa ang type-safe na koordinasyon ng ahente gamit ang Microsoft Agent Framework na may compile-time validation.

### Workflow Orchestration
Gumagamit ng declarative workflow definition gamit ang async patterns ng .NET para ikonekta ang maraming ahente sa isang pipeline.

### Streaming Responses
Nagpapatupad ng real-time na streaming ng mga tugon ng ahente gamit ang async enumerables at event-driven architecture.

### Enterprise Integration
Ipinapakita ang mga pattern na handa na sa produksyon kabilang ang:
- Pag-configure ng environment variables
- Secure na pamamahala ng credentials
- Pag-handle ng error
- Asynchronous na pagproseso ng event

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->