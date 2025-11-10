<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c8bc231a26e949f525d65b716538707f",
  "translation_date": "2025-11-07T09:47:58+00:00",
  "source_file": "03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.md",
  "language_code": "sv"
}
-->
# 🎨 Agentiska designmönster med GitHub-modeller (.NET)

## 📋 Inlärningsmål

Den här notebooken demonstrerar designmönster i företagsklass för att bygga intelligenta agenter med Microsoft Agent Framework i .NET och integration med GitHub-modeller. Du kommer att lära dig professionella mönster och arkitektoniska tillvägagångssätt som gör agenter produktionsklara, underhållbara och skalbara.

**Designmönster för företag:**
- 🏭 **Fabriksmönster**: Standardiserad agentskapande med dependency injection
- 🔧 **Byggarmönster**: Flytande konfiguration och inställning av agenter
- 🧵 **Trådsäkra mönster**: Hantering av samtidiga konversationer
- 📋 **Repository-mönster**: Organiserad hantering av verktyg och kapaciteter

## 🎯 .NET-specifika arkitektoniska fördelar

### Funktioner för företag
- **Stark typning**: Validering vid kompilering och stöd för IntelliSense
- **Dependency Injection**: Inbyggd DI-containerintegration
- **Konfigurationshantering**: IConfiguration och Options-mönster
- **Async/Await**: Förstklassigt stöd för asynkron programmering

### Produktionsklara mönster
- **Loggningsintegration**: ILogger och stöd för strukturerad loggning
- **Hälsokontroller**: Inbyggd övervakning och diagnostik
- **Konfigurationsvalidering**: Stark typning med dataannoteringar
- **Felkorrigering**: Strukturerad hantering av undantag

## 🔧 Teknisk arkitektur

### Kärnkomponenter i .NET
- **Microsoft.Extensions.AI**: Enhetliga AI-tjänsteabstraktioner
- **Microsoft.Agents.AI**: Ramverk för företagsagentorkestrering
- **GitHub Models Integration**: Högpresterande API-klientmönster
- **Konfigurationssystem**: appsettings.json och miljöintegration

### Implementering av designmönster
```csharp
IServiceCollection → Agent Builder → Configuration → Tool Registry → AI Agent
```

## 🏗️ Demonstrerade företagsmönster

### 1. **Skapandemönster**
- **Agentfabrik**: Centraliserad agentskapande med konsekvent konfiguration
- **Byggarmönster**: Flytande API för komplex agentkonfiguration
- **Singleton-mönster**: Delade resurser och konfigurationshantering
- **Dependency Injection**: Lös koppling och testbarhet

### 2. **Beteendemönster**
- **Strategimönster**: Utbytbara verktygsutförandestrategier
- **Kommandomönster**: Inkapslade agentoperationer med ångra/göra om
- **Observatörsmönster**: Händelsedriven hantering av agentens livscykel
- **Mallmetod**: Standardiserade arbetsflöden för agentutförande

### 3. **Strukturella mönster**
- **Adaptermönster**: Integrationslager för GitHub Models API
- **Dekoratormönster**: Förbättring av agentens kapacitet
- **Fasadmönster**: Förenklade gränssnitt för agentinteraktion
- **Proxymönster**: Lata laddningar och caching för prestanda

## ⚙️ Förutsättningar och installation

**Utvecklingsmiljö:**
- .NET 9.0 SDK eller högre
- Visual Studio 2022 eller VS Code med C#-tillägg
- Åtkomst till GitHub Models API

**NuGet-beroenden:**
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

## 📚 .NET-designprinciper

### SOLID-principer
- **Enkel ansvarighet**: Varje komponent har ett tydligt syfte
- **Öppen/sluten**: Utbyggbar utan modifiering
- **Liskovs substitutionsprincip**: Implementeringar baserade på gränssnitt
- **Gränssnittsegregering**: Fokuserade, sammanhängande gränssnitt
- **Inversion av beroenden**: Beroende av abstraktioner, inte konkretioner

### Ren arkitektur
- **Domänlager**: Kärnabstraktioner för agenter och verktyg
- **Applikationslager**: Orkestrering och arbetsflöden för agenter
- **Infrastrukturlager**: Integration med GitHub Models och externa tjänster
- **Presentationslager**: Användarinteraktion och formatering av svar

## 🔒 Företagsöverväganden

### Säkerhet
- **Hantering av autentiseringsuppgifter**: Säker hantering av API-nycklar med IConfiguration
- **Validering av indata**: Stark typning och validering med dataannoteringar
- **Sanering av utdata**: Säker bearbetning och filtrering av svar
- **Revisionsloggning**: Omfattande spårning av operationer

### Prestanda
- **Asynkrona mönster**: Icke-blockerande I/O-operationer
- **Anslutningspoolning**: Effektiv hantering av HTTP-klienter
- **Caching**: Caching av svar för förbättrad prestanda
- **Resurshantering**: Korrekt borttagning och städrutiner

### Skalbarhet
- **Trådsäkerhet**: Stöd för samtidiga agentutföranden
- **Resurspoolning**: Effektiv användning av resurser
- **Belastningshantering**: Hastighetsbegränsning och hantering av mottryck
- **Övervakning**: Prestandamått och hälsokontroller

## 🚀 Produktionsdistribution

- **Konfigurationshantering**: Miljöspecifika inställningar
- **Loggningsstrategi**: Strukturerad loggning med korrelations-ID
- **Felkorrigering**: Global hantering av undantag med korrekt återhämtning
- **Övervakning**: Application Insights och prestandaräknare
- **Testning**: Enhetstester, integrationstester och belastningstestmönster

Redo att bygga intelligenta agenter i företagsklass med .NET? Låt oss skapa något robust! 🏢✨

## Kodexempel

För ett komplett fungerande exempel, se [03-dotnet-agent-framework.cs](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs).

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiska översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.