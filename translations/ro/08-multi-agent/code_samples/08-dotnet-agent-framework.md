# 🤝 Sisteme Enterprise de Workflow Multi-Agent (.NET)

## 📋 Obiective de învățare

Acest caiet demonstrează cum să construiești sisteme sofisticate multi-agent de nivel enterprise folosind Microsoft Agent Framework în .NET cu Azure OpenAI (Responses API). Vei învăța să orchestrezi mai mulți agenți specializați care lucrează împreună prin fluxuri de lucru structurate, valorificând funcționalitățile Enterprise ale .NET pentru soluții pregătite pentru producție.

**Capabilități Enterprise Multi-Agent pe care le vei construi:**
- 👥 **Colaborare între agenți**: Coordonare tip-safe a agenților cu validare la compilare
- 🔄 **Orchestrarea fluxurilor de lucru**: Definirea declarativă a workflow-urilor cu pattern-uri async în .NET
- 🎭 **Specializarea rolurilor**: Personalități de agenți puternic tipizate și domenii de expertiză
- 🏢 **Integrare Enterprise**: Pattern-uri pregătite pentru producție cu monitorizare și gestionare a erorilor

## ⚙️ Precondiții & Configurare

**Mediu de Dezvoltare:**
- .NET 9.0 SDK sau versiune superioară
- Visual Studio 2022 sau VS Code cu extensia C#
- Abonament Azure (pentru agenți persistenți)

**Pachete NuGet necesare:**
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

## Exemplu de cod

Codul complet funcțional pentru această lecție este disponibil în fișierul C#: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Pentru a rula exemplul:

```bash
# Fă fișierul executabil (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Rulează exemplul
./08-dotnet-agent-framework.cs
```

Sau folosind .NET CLI:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Ce demonstrează acest exemplu

Acest sistem de workflow multi-agent creează un serviciu de recomandări turistice pentru hoteluri cu doi agenți specializați:

1. **Agentul FrontDesk**: Un agent de călătorie care oferă recomandări de activități și locații
2. **Agentul Concierge**: Revizuiește recomandările pentru a asigura experiențe autentice, non-turistice

Agenții lucrează împreună într-un workflow unde:
- Agentul FrontDesk primește cererea inițială de călătorie
- Agentul Concierge revizuiește și rafinează recomandarea
- Workflow-ul transmite răspunsuri în timp real

## Concepe cheie

### Coordonarea agenților
Exemplul demonstrează coordonarea tip-safe a agenților folosind Microsoft Agent Framework cu validare la compilare.

### Orchestrarea workflow-ului
Utilizează definirea declarativă a workflow-urilor cu pattern-uri async în .NET pentru a conecta mai mulți agenți într-un pipeline.

### Transmiterea răspunsurilor în flux
Implementează transmiterea în timp real a răspunsurilor agenților folosind enumerabile asincrone și arhitectură bazată pe evenimente.

### Integrare Enterprise
Arată pattern-uri pregătite pentru producție incluzând:
- Configurarea prin variabile de mediu
- Gestionare securizată a credentialelor
- Gestionarea erorilor
- Procesarea asincronă a evenimentelor

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->