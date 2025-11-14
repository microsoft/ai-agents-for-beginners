<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c8bc231a26e949f525d65b716538707f",
  "translation_date": "2025-11-07T09:48:15+00:00",
  "source_file": "03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.md",
  "language_code": "da"
}
-->
# 🎨 Agentiske Designmønstre med GitHub-modeller (.NET)

## 📋 Læringsmål

Denne notebook demonstrerer designmønstre i virksomhedsklasse til opbygning af intelligente agenter ved hjælp af Microsoft Agent Framework i .NET med integration af GitHub-modeller. Du vil lære professionelle mønstre og arkitektoniske tilgange, der gør agenter klar til produktion, vedligeholdelsesvenlige og skalerbare.

**Designmønstre for virksomheder:**
- 🏭 **Factory Pattern**: Standardiseret agentoprettelse med dependency injection
- 🔧 **Builder Pattern**: Flydende agentkonfiguration og opsætning
- 🧵 **Thread-Safe Patterns**: Samtidig samtalestyring
- 📋 **Repository Pattern**: Organiseret værktøjs- og kapabilitetsstyring

## 🎯 .NET-specifikke arkitektoniske fordele

### Funktioner til virksomheder
- **Stærk typning**: Validering ved kompilering og IntelliSense-support
- **Dependency Injection**: Indbygget DI-containerintegration
- **Konfigurationsstyring**: IConfiguration og Options-mønstre
- **Async/Await**: Førsteklasses understøttelse af asynkron programmering

### Produktionsklare mønstre
- **Logningsintegration**: ILogger og struktureret logningssupport
- **Sundhedstjek**: Indbygget overvågning og diagnostik
- **Konfigurationsvalidering**: Stærk typning med dataannoteringer
- **Fejlhåndtering**: Struktureret undtagelseshåndtering

## 🔧 Teknisk arkitektur

### Centrale .NET-komponenter
- **Microsoft.Extensions.AI**: Enhedlige AI-serviceabstraktioner
- **Microsoft.Agents.AI**: Enterprise-agent orkestreringsframework
- **GitHub Models Integration**: Højtydende API-klientmønstre
- **Konfigurationssystem**: appsettings.json og miljøintegration

### Implementering af designmønstre
```csharp
IServiceCollection → Agent Builder → Configuration → Tool Registry → AI Agent
```

## 🏗️ Demonstrerede virksomhedsmønstre

### 1. **Creational Patterns**
- **Agent Factory**: Centraliseret agentoprettelse med ensartet konfiguration
- **Builder Pattern**: Flydende API til kompleks agentkonfiguration
- **Singleton Pattern**: Delte ressourcer og konfigurationsstyring
- **Dependency Injection**: Løs kobling og testbarhed

### 2. **Behavioral Patterns**
- **Strategy Pattern**: Udskiftelige værktøjsudførelsesstrategier
- **Command Pattern**: Indkapslede agentoperationer med fortryd/gendan
- **Observer Pattern**: Hændelsesdrevet agentlivscyklusstyring
- **Template Method**: Standardiserede agentudførelsesarbejdsgange

### 3. **Structural Patterns**
- **Adapter Pattern**: GitHub Models API-integrationslag
- **Decorator Pattern**: Forbedring af agentkapabiliteter
- **Facade Pattern**: Forenklede agentinteraktionsgrænseflader
- **Proxy Pattern**: Lazy loading og caching for ydeevne

## ⚙️ Forudsætninger og opsætning

**Udviklingsmiljø:**
- .NET 9.0 SDK eller nyere
- Visual Studio 2022 eller VS Code med C#-udvidelse
- Adgang til GitHub Models API

**NuGet-afhængigheder:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Konfiguration (.env-fil):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 📚 .NET Designprincipper

### SOLID-principper
- **Single Responsibility**: Hver komponent har ét klart formål
- **Open/Closed**: Udvidelig uden modifikation
- **Liskov Substitution**: Implementeringer baseret på grænseflader
- **Interface Segregation**: Fokuserede, sammenhængende grænseflader
- **Dependency Inversion**: Afhængighed af abstraktioner, ikke konkretiseringer

### Clean Architecture
- **Domain Layer**: Kerneagent- og værktøjsabstraktioner
- **Application Layer**: Agentorkestrering og arbejdsgange
- **Infrastructure Layer**: GitHub Models-integration og eksterne tjenester
- **Presentation Layer**: Brugerinteraktion og responsformatering

## 🔒 Overvejelser for virksomheder

### Sikkerhed
- **Credential Management**: Sikker håndtering af API-nøgler med IConfiguration
- **Input Validation**: Stærk typning og validering med dataannoteringer
- **Output Sanitization**: Sikker responsbehandling og filtrering
- **Audit Logging**: Omfattende sporingsoperationer

### Ydeevne
- **Async Patterns**: Ikke-blokerende I/O-operationer
- **Connection Pooling**: Effektiv HTTP-klientstyring
- **Caching**: Responscaching for forbedret ydeevne
- **Resource Management**: Korrekt bortskaffelse og oprydningsmønstre

### Skalerbarhed
- **Thread Safety**: Understøttelse af samtidig agentudførelse
- **Resource Pooling**: Effektiv ressourceudnyttelse
- **Load Management**: Hastighedsbegrænsning og håndtering af belastning
- **Monitoring**: Ydeevnemålinger og sundhedstjek

## 🚀 Produktionsudrulning

- **Konfigurationsstyring**: Miljøspecifikke indstillinger
- **Logningsstrategi**: Struktureret logning med korrelations-ID'er
- **Fejlhåndtering**: Global undtagelseshåndtering med korrekt genopretning
- **Overvågning**: Application Insights og ydeevnetællere
- **Testning**: Enhedstest, integrationstest og belastningstestmønstre

Klar til at bygge intelligente agenter i virksomhedsklasse med .NET? Lad os arkitektere noget robust! 🏢✨

## Eksempelkode

For et komplet fungerende eksempel, se [03-dotnet-agent-framework.cs](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs).

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.