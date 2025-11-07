<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c8bc231a26e949f525d65b716538707f",
  "translation_date": "2025-11-07T09:48:28+00:00",
  "source_file": "03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.md",
  "language_code": "no"
}
-->
# 🎨 Agentiske designmønstre med GitHub-modeller (.NET)

## 📋 Læringsmål

Denne notatboken demonstrerer designmønstre på bedriftsnivå for å bygge intelligente agenter ved bruk av Microsoft Agent Framework i .NET med integrasjon av GitHub-modeller. Du vil lære profesjonelle mønstre og arkitektoniske tilnærminger som gjør agenter klare for produksjon, vedlikeholdbare og skalerbare.

**Designmønstre for bedrifter:**
- 🏭 **Fabrikkmønster**: Standardisert agentopprettelse med avhengighetsinjeksjon
- 🔧 **Byggemønster**: Flytende konfigurasjon og oppsett av agenter
- 🧵 **Trådsikre mønstre**: Samtidig samtalehåndtering
- 📋 **Repository-mønster**: Organisert verktøy- og kapabilitetshåndtering

## 🎯 Arkitektoniske fordeler med .NET

### Funksjoner for bedrifter
- **Sterk typisering**: Validering ved kompilering og IntelliSense-støtte
- **Avhengighetsinjeksjon**: Integrert DI-container
- **Konfigurasjonsstyring**: IConfiguration og Options-mønstre
- **Async/Await**: Førsteklasses støtte for asynkron programmering

### Mønstre klare for produksjon
- **Loggintegrasjon**: ILogger og støtte for strukturert logging
- **Helsesjekker**: Innebygd overvåking og diagnostikk
- **Konfigurasjonsvalidering**: Sterk typisering med dataannotasjoner
- **Feilhåndtering**: Strukturert unntakshåndtering

## 🔧 Teknisk arkitektur

### Kjernekomponenter i .NET
- **Microsoft.Extensions.AI**: Enhetlige AI-tjenesteabstraksjoner
- **Microsoft.Agents.AI**: Rammeverk for agentorkestrering på bedriftsnivå
- **GitHub Models Integration**: API-klientmønstre med høy ytelse
- **Konfigurasjonssystem**: appsettings.json og miljøintegrasjon

### Implementering av designmønstre
```csharp
IServiceCollection → Agent Builder → Configuration → Tool Registry → AI Agent
```

## 🏗️ Demonstrerte mønstre for bedrifter

### 1. **Opprettelsesmønstre**
- **Agentfabrikk**: Sentralisert opprettelse av agenter med konsistent konfigurasjon
- **Byggemønster**: Flytende API for kompleks agentkonfigurasjon
- **Singleton-mønster**: Delte ressurser og konfigurasjonshåndtering
- **Avhengighetsinjeksjon**: Løs kobling og testbarhet

### 2. **Atferdsmønstre**
- **Strategimønster**: Utskiftbare strategier for verktøyutførelse
- **Kommandomønster**: Innkapslede agentoperasjoner med angre/gjenta
- **Observatørmønster**: Hendelsesdrevet livssyklushåndtering for agenter
- **Malmetode**: Standardiserte arbeidsflyter for agentutførelse

### 3. **Strukturelle mønstre**
- **Adaptermønster**: Integrasjonslag for GitHub Models API
- **Dekoratørmønster**: Forbedring av agentkapabiliteter
- **Fasademønster**: Forenklede grensesnitt for agentinteraksjon
- **Proxymønster**: Lazy loading og caching for ytelse

## ⚙️ Forutsetninger og oppsett

**Utviklingsmiljø:**
- .NET 9.0 SDK eller nyere
- Visual Studio 2022 eller VS Code med C#-utvidelse
- Tilgang til GitHub Models API

**NuGet-avhengigheter:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Konfigurasjon (.env-fil):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 📚 Designprinsipper i .NET

### SOLID-prinsipper
- **Enkelt ansvar**: Hver komponent har ett klart formål
- **Åpen/lukket**: Utvidbar uten modifikasjon
- **Liskovs substitusjonsprinsipp**: Implementasjoner basert på grensesnitt
- **Grensesnittsegregering**: Fokusert, sammenhengende grensesnitt
- **Avhengighetsinversjon**: Avhengighet av abstraksjoner, ikke konkrete implementasjoner

### Ren arkitektur
- **Domenelag**: Kjerneabstraksjoner for agenter og verktøy
- **Applikasjonslag**: Orkestrering og arbeidsflyter for agenter
- **Infrastrukturlag**: Integrasjon med GitHub Models og eksterne tjenester
- **Presentasjonslag**: Brukerinteraksjon og responsformatering

## 🔒 Betraktninger for bedrifter

### Sikkerhet
- **Håndtering av legitimasjon**: Sikker håndtering av API-nøkler med IConfiguration
- **Validering av input**: Sterk typisering og validering med dataannotasjoner
- **Sanitering av output**: Sikker behandling og filtrering av responser
- **Revisjonslogging**: Omfattende sporing av operasjoner

### Ytelse
- **Asynkrone mønstre**: Ikke-blokkerende I/O-operasjoner
- **Tilkoblingspooling**: Effektiv håndtering av HTTP-klienter
- **Caching**: Responscaching for forbedret ytelse
- **Ressurshåndtering**: Riktig opprydding og avhending

### Skalerbarhet
- **Trådsikkerhet**: Støtte for samtidig utførelse av agenter
- **Ressurspooling**: Effektiv utnyttelse av ressurser
- **Laststyring**: Ratebegrensning og håndtering av mottrykk
- **Overvåking**: Ytelsesmetrikker og helsesjekker

## 🚀 Produksjonsutplassering

- **Konfigurasjonsstyring**: Miljøspesifikke innstillinger
- **Loggstrategi**: Strukturert logging med korrelasjons-ID-er
- **Feilhåndtering**: Global unntakshåndtering med riktig gjenoppretting
- **Overvåking**: Application Insights og ytelsestellere
- **Testing**: Enhetstester, integrasjonstester og lasttestmønstre

Klar til å bygge intelligente agenter på bedriftsnivå med .NET? La oss arkitektere noe robust! 🏢✨

## Eksempelkode

For et komplett fungerende eksempel, se [03-dotnet-agent-framework.cs](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs).

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.