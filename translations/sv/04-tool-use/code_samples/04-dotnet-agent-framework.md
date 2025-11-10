<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f82a3992438bcc028a2569c5fed828a9",
  "translation_date": "2025-11-07T09:25:21+00:00",
  "source_file": "04-tool-use/code_samples/04-dotnet-agent-framework.md",
  "language_code": "sv"
}
-->
# 🛠️ Avancerad Verktygsanvändning med GitHub-modeller (.NET)

## 📋 Inlärningsmål

Den här notebooken visar integrationsmönster för verktyg på företagsnivå med hjälp av Microsoft Agent Framework i .NET tillsammans med GitHub-modeller. Du kommer att lära dig att bygga sofistikerade agenter med flera specialiserade verktyg, och dra nytta av C#'s starka typning och .NET's företagsfunktioner.

**Avancerade verktygskapaciteter du kommer att bemästra:**
- 🔧 **Multi-verktygsarkitektur**: Bygga agenter med flera specialiserade funktioner
- 🎯 **Typ-säker verktygsanvändning**: Utnyttja C#'s validering vid kompilering
- 📊 **Företagsverktygsmönster**: Produktionsklara verktygsdesign och felhantering
- 🔗 **Verktygskomposition**: Kombinera verktyg för komplexa affärsarbetsflöden

## 🎯 Fördelar med .NET-verktygsarkitektur

### Funktioner för företagsverktyg
- **Validering vid kompilering**: Stark typning säkerställer korrekthet i verktygsparametrar
- **Dependency Injection**: IoC-containerintegration för verktygshantering
- **Async/Await-mönster**: Icke-blockerande verktygsanvändning med korrekt resursförvaltning
- **Strukturerad loggning**: Inbyggd loggningsintegration för övervakning av verktygsanvändning

### Produktionsklara mönster
- **Felhantering**: Omfattande felhantering med typade undantag
- **Resurshantering**: Korrekt hantering av resurser och minnesförvaltning
- **Prestandaövervakning**: Inbyggda mätvärden och prestandaräknare
- **Konfigurationshantering**: Typ-säker konfiguration med validering

## 🔧 Teknisk arkitektur

### Kärnkomponenter i .NET-verktyg
- **Microsoft.Extensions.AI**: Enhetligt abstraktionslager för verktyg
- **Microsoft.Agents.AI**: Verktygsorkestrering på företagsnivå
- **GitHub-modeller integration**: Högpresterande API-klient med anslutningspoolning

### Verktygsanvändningspipeline
```
User Request → Agent Analysis → Tool Selection → Type Validation
                 ↓               ↓              ↓
         Parameter Binding → Tool Execution → Result Processing → Response
```

## 🛠️ Verktygskategorier och mönster

### 1. **Databehandlingsverktyg**
- **Inmatningsvalidering**: Stark typning med dataannoteringar
- **Transformationsoperationer**: Typ-säker datakonvertering och formatering
- **Affärslogik**: Domänspecifika beräkningar och analysverktyg
- **Utdataformatering**: Generering av strukturerade svar

### 2. **Integrationsverktyg** 
- **API-kopplingar**: RESTful-tjänsteintegration med HttpClient
- **Databasverktyg**: Entity Framework-integration för dataåtkomst
- **Filoperationer**: Säker filsystemhantering med validering
- **Externa tjänster**: Mönster för integration av tredjepartstjänster

### 3. **Hjälpverktyg**
- **Textbehandling**: Strängmanipulation och formateringsverktyg
- **Datum/tid-operationer**: Kulturmedvetna beräkningar av datum och tid
- **Matematiska verktyg**: Precisionsberäkningar och statistiska operationer
- **Valideringsverktyg**: Validering av affärsregler och datakontroll

## ⚙️ Förutsättningar och installation

**Utvecklingsmiljö:**
- .NET 9.0 SDK eller högre
- Visual Studio 2022 eller VS Code med C#-tillägg
- GitHub Models API-åtkomst

**Nödvändiga NuGet-paket:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Miljökonfiguration (.env-fil):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

Redo att bygga företagsklassade agenter med kraftfulla, typ-säkra verktygskapaciteter i .NET? Låt oss skapa professionella lösningar! 🏢⚡

## 💻 Kodimplementering

Den kompletta C#-implementeringen finns i den medföljande filen `04-dotnet-agent-framework.cs`. Denna .NET Single File App demonstrerar:

- Laddning av miljövariabler för GitHub Models-konfiguration
- Definiera anpassade verktyg med C#-metoder och attribut
- Skapa en AI-agent med verktygsintegration
- Hantera konversationstrådar
- Utföra agentförfrågningar med verktygsanrop

För att köra exemplet:

```bash
chmod +x 04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

Eller med .NET CLI:

```bash
dotnet run 04-dotnet-agent-framework.cs
```

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.