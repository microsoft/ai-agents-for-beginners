<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c268705e6fb2b30c7690d5b2a002e072",
  "translation_date": "2025-11-07T09:03:56+00:00",
  "source_file": "05-agentic-rag/code_samples/05-dotnet-agent-framework.md",
  "language_code": "sv"
}
-->
# 🔍 Enterprise RAG med Azure AI Foundry (.NET)

## 📋 Lärandemål

Den här notebooken visar hur man bygger företagsklassade Retrieval-Augmented Generation (RAG)-system med Microsoft Agent Framework i .NET och Azure AI Foundry. Du kommer att lära dig att skapa produktionsklara agenter som kan söka igenom dokument och ge korrekta, kontextmedvetna svar med företagsmässig säkerhet och skalbarhet.

**Funktioner för Enterprise RAG du kommer att bygga:**
- 📚 **Dokumentintelligens**: Avancerad dokumentbearbetning med Azure AI-tjänster
- 🔍 **Semantisk sökning**: Högpresterande vektorsökning med företagsfunktioner
- 🛡️ **Säkerhetsintegration**: Rollbaserad åtkomst och dataskyddsmönster
- 🏢 **Skalbar arkitektur**: Produktionsklara RAG-system med övervakning

## 🎯 Enterprise RAG-arkitektur

### Centrala företagskomponenter
- **Azure AI Foundry**: Hanterad företagsplattform för AI med säkerhet och efterlevnad
- **Persistenta agenter**: Agenter med tillståndshantering och konversationshistorik
- **Hantering av vektorlagring**: Företagsklassad dokumentindexering och hämtning
- **Identitetsintegration**: Azure AD-autentisering och rollbaserad åtkomstkontroll

### Fördelar med .NET för företag
- **Typkontroll**: Validering vid kompilering för RAG-operationer och datastrukturer
- **Asynkron prestanda**: Icke-blockerande dokumentbearbetning och sökoperationer
- **Minneshantering**: Effektiv resursanvändning för stora dokumentkollektioner
- **Integrationsmönster**: Inbyggd integration med Azure-tjänster via dependency injection

## 🏗️ Teknisk arkitektur

### Enterprise RAG-pipeline
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Centrala .NET-komponenter
- **Azure.AI.Agents.Persistent**: Hantering av företagsagenter med tillståndsbevarande
- **Azure.Identity**: Integrerad autentisering för säker åtkomst till Azure-tjänster
- **Microsoft.Agents.AI.AzureAI**: Optimerad agentramverk för Azure
- **System.Linq.Async**: Högpresterande asynkrona LINQ-operationer

## 🔧 Företagsfunktioner och fördelar

### Säkerhet och efterlevnad
- **Azure AD-integration**: Företagsidentitetshantering och autentisering
- **Rollbaserad åtkomst**: Finkorniga behörigheter för dokumentåtkomst och operationer
- **Dataskydd**: Kryptering vid lagring och överföring för känsliga dokument
- **Revisionsloggning**: Omfattande aktivitetsövervakning för efterlevnadskrav

### Prestanda och skalbarhet
- **Anslutningspoolning**: Effektiv hantering av anslutningar till Azure-tjänster
- **Asynkron bearbetning**: Icke-blockerande operationer för hög genomströmning
- **Cache-strategier**: Intelligent caching för ofta åtkomna dokument
- **Lastbalansering**: Distribuerad bearbetning för storskaliga implementationer

### Hantering och övervakning
- **Hälsokontroller**: Inbyggd övervakning av RAG-systemkomponenter
- **Prestandamått**: Detaljerad analys av sökkvalitet och svarstider
- **Felhantering**: Omfattande undantagshantering med återförsökspolicyer
- **Konfigurationshantering**: Miljöspecifika inställningar med validering

## ⚙️ Förutsättningar och installation

**Utvecklingsmiljö:**
- .NET 9.0 SDK eller högre
- Visual Studio 2022 eller VS Code med C#-tillägg
- Azure-prenumeration med tillgång till AI Foundry

**Nödvändiga NuGet-paket:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Azure-autentiseringsinställning:**
```bash
# Install Azure CLI and authenticate
az login
az account set --subscription "your-subscription-id"
```

**Miljökonfiguration:**
* Konfiguration av Azure AI Foundry (hanteras automatiskt via Azure CLI)
* Se till att du är autentiserad till rätt Azure-prenumeration

## 📊 Mönster för Enterprise RAG

### Mönster för dokumenthantering
- **Massuppladdning**: Effektiv bearbetning av stora dokumentkollektioner
- **Inkrementella uppdateringar**: Realtidsaddition och modifiering av dokument
- **Versionskontroll**: Versionshantering och spårning av ändringar
- **Metadatahantering**: Rika dokumentattribut och taxonomi

### Mönster för sökning och hämtning
- **Hybrid sökning**: Kombinera semantisk och nyckelordssökning för optimala resultat
- **Facetterad sökning**: Multidimensionell filtrering och kategorisering
- **Relevansjustering**: Anpassade poängalgoritmer för domänspecifika behov
- **Resultatrangering**: Avancerad rangordning med affärslogik

### Säkerhetsmönster
- **Dokumentnivåsäkerhet**: Finkornig åtkomstkontroll per dokument
- **Dataklassificering**: Automatisk känslighetsmärkning och skydd
- **Revisionsspår**: Omfattande loggning av alla RAG-operationer
- **Integritetsskydd**: Identifiering och redigering av PII

## 🔒 Företagssäkerhetsfunktioner

### Autentisering och auktorisering
```csharp
// Azure AD integrated authentication
var credential = new AzureCliCredential();
var agentsClient = new PersistentAgentsClient(endpoint, credential);

// Role-based access validation
if (!await ValidateUserPermissions(user, documentId))
{
    throw new UnauthorizedAccessException("Insufficient permissions");
}
```

### Dataskydd
- **Kryptering**: Kryptering från början till slut för dokument och sökindex
- **Åtkomstkontroller**: Integration med Azure AD för användar- och gruppbehörigheter
- **Dataresidens**: Geografiska dataplatskontroller för efterlevnad
- **Backup och återställning**: Automatiserade backup- och katastrofåterställningsfunktioner

## 📈 Prestandaoptimering

### Mönster för asynkron bearbetning
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Minneshantering
- **Strömningsbearbetning**: Hantera stora dokument utan minnesproblem
- **Resurspoolning**: Effektiv återanvändning av dyra resurser
- **Skräpsamling**: Optimerade mönster för minnesallokering
- **Anslutningshantering**: Korrekt livscykel för anslutningar till Azure-tjänster

### Cache-strategier
- **Frågecache**: Cache för ofta utförda sökningar
- **Dokumentcache**: Cache i minnet för populära dokument
- **Indexcache**: Optimerad cache för vektorindex
- **Resultatcache**: Intelligent cache för genererade svar

## 📊 Företagsanvändningsområden

### Kunskapshantering
- **Företagswiki**: Intelligent sökning i företags kunskapsbaser
- **Policyer och procedurer**: Automatiserad vägledning för efterlevnad och procedurer
- **Utbildningsmaterial**: Intelligent stöd för lärande och utveckling
- **Forskningsdatabaser**: System för analys av akademiska och forskningsartiklar

### Kundsupport
- **Supportkunskapsbas**: Automatiserade kundtjänstsvar
- **Produktdokumentation**: Intelligent hämtning av produktinformation
- **Felsökningsguider**: Kontextuell problemlösningshjälp
- **FAQ-system**: Dynamisk FAQ-generering från dokumentkollektioner

### Regelverksefterlevnad
- **Analys av juridiska dokument**: Intelligens för avtal och juridiska dokument
- **Övervakning av efterlevnad**: Automatiserad kontroll av regelverksefterlevnad
- **Riskbedömning**: Riskanalys och rapportering baserad på dokument
- **Revisionsstöd**: Intelligent dokumentupptäckt för revisioner

## 🚀 Produktionsimplementering

### Övervakning och observabilitet
- **Application Insights**: Detaljerad telemetri och prestandaövervakning
- **Anpassade mått**: Företagsspecifik KPI-spårning och varningar
- **Distribuerad spårning**: Spårning av begäran från början till slut över tjänster
- **Hälsodashboards**: Realtidsvisualisering av systemhälsa och prestanda

### Skalbarhet och tillförlitlighet
- **Autoskalning**: Automatisk skalning baserat på belastning och prestandamått
- **Hög tillgänglighet**: Multi-region distribution med failover-funktioner
- **Lasttestning**: Prestandavalidering under företagsbelastning
- **Katastrofåterställning**: Automatiserade backup- och återställningsprocedurer

Redo att bygga företagsklassade RAG-system som kan hantera känsliga dokument i stor skala? Låt oss designa intelligenta kunskapssystem för företag! 🏢📖✨

## Kodimplementering

Det kompletta fungerande kodexemplet för denna lektion finns i `05-dotnet-agent-framework.cs`. 

För att köra exemplet:

```bash
# Make the script executable (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Run the .NET Single File App
./05-dotnet-agent-framework.cs
```

Eller använd `dotnet run` direkt:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Koden demonstrerar:

1. **Installation av paket**: Installera nödvändiga NuGet-paket för Azure AI Agents
2. **Miljökonfiguration**: Ladda inställningar för Azure AI Foundry endpoint och modell
3. **Dokumentuppladdning**: Ladda upp ett dokument för RAG-bearbetning
4. **Skapande av vektorlagring**: Skapa en vektorlagring för semantisk sökning
5. **Agentkonfiguration**: Ställa in en AI-agent med filsökningsfunktioner
6. **Utförande av frågor**: Köra frågor mot det uppladdade dokumentet

---

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.