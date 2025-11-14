<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f5a5f2902f32272257506d88d3c43a1",
  "translation_date": "2025-11-07T09:18:44+00:00",
  "source_file": "08-multi-agent/code_samples/08-dotnet-agent-framework.md",
  "language_code": "ro"
}
-->
# 🤝 Sisteme de flux de lucru multi-agent pentru întreprinderi (.NET)

## 📋 Obiective de învățare

Acest notebook demonstrează cum să construiești sisteme multi-agent sofisticate, de nivel enterprise, utilizând Microsoft Agent Framework în .NET cu modele GitHub. Vei învăța să orchestrezi mai mulți agenți specializați care lucrează împreună prin fluxuri de lucru structurate, valorificând caracteristicile enterprise ale .NET pentru soluții pregătite pentru producție.

**Capabilități multi-agent pentru întreprinderi pe care le vei construi:**
- 👥 **Colaborarea agenților**: Coordonare între agenți cu validare la compilare
- 🔄 **Orchestrarea fluxului de lucru**: Definirea declarativă a fluxului de lucru cu modele asincrone din .NET
- 🎭 **Specializarea rolurilor**: Personalități de agenți puternic tipizate și domenii de expertiză
- 🏢 **Integrare în întreprindere**: Modele pregătite pentru producție cu monitorizare și gestionarea erorilor

## ⚙️ Cerințe preliminare și configurare

**Mediu de dezvoltare:**
- .NET 9.0 SDK sau mai recent
- Visual Studio 2022 sau VS Code cu extensia C#
- Abonament Azure (pentru agenți persistenți)

**Pachete NuGet necesare:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.4" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="9.8.0" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
```

## Exemplu de cod

Codul complet funcțional pentru această lecție este disponibil în fișierul C# asociat: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Pentru a rula exemplul:

```bash
# Make the file executable (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Run the sample
./08-dotnet-agent-framework.cs
```

Sau folosind CLI-ul .NET:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Ce demonstrează acest exemplu

Acest sistem de flux de lucru multi-agent creează un serviciu de recomandări pentru călătorii la hotel, cu doi agenți specializați:

1. **Agentul FrontDesk**: Un agent de călătorii care oferă recomandări de activități și locații
2. **Agentul Concierge**: Revizuiește recomandările pentru a asigura experiențe autentice, non-turistice

Agenții lucrează împreună într-un flux de lucru în care:
- Agentul FrontDesk primește cererea inițială de călătorie
- Agentul Concierge revizuiește și rafinează recomandarea
- Fluxul de lucru transmite răspunsurile în timp real

## Concepte cheie

### Coordonarea agenților
Exemplul demonstrează coordonarea între agenți, sigură din punct de vedere al tipurilor, utilizând Microsoft Agent Framework cu validare la compilare.

### Orchestrarea fluxului de lucru
Folosește definirea declarativă a fluxului de lucru cu modele asincrone din .NET pentru a conecta mai mulți agenți într-un pipeline.

### Răspunsuri în timp real
Implementează transmiterea în timp real a răspunsurilor agenților utilizând enumerabile asincrone și arhitectură bazată pe evenimente.

### Integrare în întreprindere
Prezintă modele pregătite pentru producție, inclusiv:
- Configurarea variabilelor de mediu
- Gestionarea securizată a acreditărilor
- Gestionarea erorilor
- Procesarea asincronă a evenimentelor

---

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim să asigurăm acuratețea, vă rugăm să fiți conștienți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de oameni. Nu ne asumăm responsabilitatea pentru neînțelegerile sau interpretările greșite care pot apărea din utilizarea acestei traduceri.