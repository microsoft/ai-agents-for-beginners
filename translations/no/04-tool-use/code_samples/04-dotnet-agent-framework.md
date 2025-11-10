<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f82a3992438bcc028a2569c5fed828a9",
  "translation_date": "2025-11-07T09:25:43+00:00",
  "source_file": "04-tool-use/code_samples/04-dotnet-agent-framework.md",
  "language_code": "no"
}
-->
# 🛠️ Avansert Verktøybruk med GitHub-modeller (.NET)

## 📋 Læringsmål

Denne notatboken viser integrasjonsmønstre for verktøy på bedriftsnivå ved bruk av Microsoft Agent Framework i .NET med GitHub-modeller. Du vil lære å bygge sofistikerte agenter med flere spesialiserte verktøy, og dra nytte av C#'s sterke typisering og .NET's enterprise-funksjoner.

**Avanserte verktøyferdigheter du vil mestre:**
- 🔧 **Multi-verktøyarkitektur**: Bygge agenter med flere spesialiserte funksjoner
- 🎯 **Type-sikker verktøyutførelse**: Utnytte C#'s validering ved kompilering
- 📊 **Bedriftsverktøymønstre**: Produksjonsklare verktøydesign og feilhåndtering
- 🔗 **Verktøysammensetning**: Kombinere verktøy for komplekse forretningsprosesser

## 🎯 Fordeler med .NET-verktøyarkitektur

### Funksjoner for bedriftens verktøy
- **Validering ved kompilering**: Sterk typisering sikrer korrekthet i verktøyparametere
- **Dependency Injection**: IoC-containerintegrasjon for verktøyhåndtering
- **Async/Await-mønstre**: Ikke-blokkerende verktøyutførelse med riktig ressursstyring
- **Strukturert logging**: Innebygd logging for overvåking av verktøyutførelse

### Produksjonsklare mønstre
- **Unntakshåndtering**: Omfattende feilhåndtering med typede unntak
- **Ressursstyring**: Riktig avhendingsmønstre og minnehåndtering
- **Ytelsesovervåking**: Innebygde målinger og ytelsestellere
- **Konfigurasjonsstyring**: Type-sikker konfigurasjon med validering

## 🔧 Teknisk Arkitektur

### Kjernekomponenter i .NET-verktøy
- **Microsoft.Extensions.AI**: Enhetlig abstraksjonslag for verktøy
- **Microsoft.Agents.AI**: Verktøyorkestrering på bedriftsnivå
- **GitHub-modeller integrasjon**: Høyytelses API-klient med tilkoblingspooling

### Verktøyutførelsesrørledning
```
User Request → Agent Analysis → Tool Selection → Type Validation
                 ↓               ↓              ↓
         Parameter Binding → Tool Execution → Result Processing → Response
```

## 🛠️ Verktøykategorier og mønstre

### 1. **Databehandlingsverktøy**
- **Inputvalidering**: Sterk typisering med dataannotasjoner
- **Transformasjonsoperasjoner**: Type-sikker datakonvertering og formatering
- **Forretningslogikk**: Domene-spesifikke beregnings- og analyserverktøy
- **Outputformatering**: Strukturert responsgenerering

### 2. **Integrasjonsverktøy**
- **API-koblinger**: RESTful tjenesteintegrasjon med HttpClient
- **Databaseverktøy**: Entity Framework-integrasjon for dataadgang
- **Filoperasjoner**: Sikker filsystemoperasjon med validering
- **Eksterne tjenester**: Mønstre for integrasjon av tredjepartstjenester

### 3. **Hjelpeverktøy**
- **Tekstbehandling**: Strengmanipulasjon og formateringsverktøy
- **Dato/tid-operasjoner**: Kulturbevisste beregninger av dato/tid
- **Matematiske verktøy**: Presisjonsberegninger og statistiske operasjoner
- **Valideringsverktøy**: Validering av forretningsregler og dataverifikasjon

## ⚙️ Forutsetninger og Oppsett

**Utviklingsmiljø:**
- .NET 9.0 SDK eller nyere
- Visual Studio 2022 eller VS Code med C#-utvidelse
- Tilgang til GitHub Models API

**Nødvendige NuGet-pakker:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Miljøkonfigurasjon (.env-fil):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

Klar til å bygge bedriftsklare agenter med kraftige, type-sikre verktøyfunksjoner i .NET? La oss designe noen profesjonelle løsninger! 🏢⚡

## 💻 Kodeimplementering

Den komplette C#-implementeringen er tilgjengelig i den medfølgende filen `04-dotnet-agent-framework.cs`. Denne .NET Single File App demonstrerer:

- Laste inn miljøvariabler for GitHub Models-konfigurasjon
- Definere tilpassede verktøy ved bruk av C#-metoder med attributter
- Opprette en AI-agent med verktøyintegrasjon
- Administrere samtaletråder
- Utføre agentforespørsler med verktøyaktivering

For å kjøre eksempelet:

```bash
chmod +x 04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

Eller ved bruk av .NET CLI:

```bash
dotnet run 04-dotnet-agent-framework.cs
```

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.