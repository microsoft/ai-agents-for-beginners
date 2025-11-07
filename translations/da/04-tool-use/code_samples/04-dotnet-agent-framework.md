<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f82a3992438bcc028a2569c5fed828a9",
  "translation_date": "2025-11-07T09:25:31+00:00",
  "source_file": "04-tool-use/code_samples/04-dotnet-agent-framework.md",
  "language_code": "da"
}
-->
# 🛠️ Avanceret Værktøjsbrug med GitHub-modeller (.NET)

## 📋 Læringsmål

Denne notebook demonstrerer mønstre for integration af værktøjer på virksomhedsniveau ved hjælp af Microsoft Agent Framework i .NET med GitHub-modeller. Du vil lære at bygge sofistikerede agenter med flere specialiserede værktøjer, der udnytter C#'s stærke typning og .NET's virksomhedsfunktioner.

**Avancerede værktøjsfunktioner, du vil mestre:**
- 🔧 **Multi-værktøjsarkitektur**: Bygge agenter med flere specialiserede funktioner
- 🎯 **Type-sikker værktøjsudførelse**: Udnytte C#'s compile-time validering
- 📊 **Virksomhedsværktøjsmønstre**: Produktionsklare værktøjsdesign og fejlhåndtering
- 🔗 **Værktøjssammensætning**: Kombinere værktøjer til komplekse forretningsarbejdsgange

## 🎯 Fordele ved .NET-værktøjsarkitektur

### Funktioner på virksomhedsniveau
- **Compile-Time Validering**: Stærk typning sikrer korrekthed af værktøjsparametre
- **Dependency Injection**: IoC-containerintegration til værktøjsstyring
- **Async/Await Mønstre**: Ikke-blokerende værktøjsudførelse med korrekt ressourcehåndtering
- **Struktureret Logning**: Indbygget logningsintegration til overvågning af værktøjsudførelse

### Produktionsklare mønstre
- **Fejlhåndtering**: Omfattende fejlhåndtering med typede undtagelser
- **Ressourcehåndtering**: Korrekte dispose-mønstre og hukommelseshåndtering
- **Ydelsesovervågning**: Indbyggede metrikker og ydelsestællere
- **Konfigurationsstyring**: Type-sikker konfiguration med validering

## 🔧 Teknisk Arkitektur

### Centrale .NET-værktøjskomponenter
- **Microsoft.Extensions.AI**: Enhedligt værktøjsabstraktionslag
- **Microsoft.Agents.AI**: Værktøjsorkestrering på virksomhedsniveau
- **GitHub Models Integration**: Højtydende API-klient med forbindelsespulje

### Værktøjsudførelsespipeline
```
User Request → Agent Analysis → Tool Selection → Type Validation
                 ↓               ↓              ↓
         Parameter Binding → Tool Execution → Result Processing → Response
```

## 🛠️ Værktøjskategorier & Mønstre

### 1. **Databehandlingsværktøjer**
- **Inputvalidering**: Stærk typning med dataannoteringer
- **Transformationsoperationer**: Type-sikker datakonvertering og formatering
- **Forretningslogik**: Domænespecifikke beregnings- og analysemuligheder
- **Outputformatering**: Generering af strukturerede svar

### 2. **Integrationsværktøjer** 
- **API-forbindelser**: RESTful serviceintegration med HttpClient
- **Databaseværktøjer**: Entity Framework-integration til dataadgang
- **Filoperationer**: Sikker filsystemhåndtering med validering
- **Eksterne tjenester**: Mønstre for integration af tredjepartstjenester

### 3. **Hjælpeværktøjer**
- **Tekstbehandling**: Strengmanipulation og formateringsværktøjer
- **Dato-/tidsoperationer**: Kulturbevidste dato-/tidsberegninger
- **Matematiske værktøjer**: Præcisionsberegninger og statistiske operationer
- **Valideringsværktøjer**: Forretningsregelvalidering og dataverifikation

## ⚙️ Forudsætninger & Opsætning

**Udviklingsmiljø:**
- .NET 9.0 SDK eller nyere
- Visual Studio 2022 eller VS Code med C#-udvidelse
- Adgang til GitHub Models API

**Påkrævede NuGet-pakker:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Miljøkonfiguration (.env-fil):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

Klar til at bygge virksomhedsklare agenter med kraftfulde, type-sikre værktøjsfunktioner i .NET? Lad os designe nogle professionelle løsninger! 🏢⚡

## 💻 Implementering af kode

Den komplette C#-implementering er tilgængelig i den tilhørende fil `04-dotnet-agent-framework.cs`. Denne .NET Single File App demonstrerer:

- Indlæsning af miljøvariabler til GitHub Models-konfiguration
- Definition af brugerdefinerede værktøjer ved hjælp af C#-metoder med attributter
- Oprettelse af en AI-agent med værktøjsintegration
- Håndtering af samtaletråde
- Udførelse af agentforespørgsler med værktøjsaktivering

For at køre eksemplet:

```bash
chmod +x 04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

Eller ved hjælp af .NET CLI:

```bash
dotnet run 04-dotnet-agent-framework.cs
```

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.