# 🔍 Enterprise RAG med Microsoft Foundry (.NET)

## 📋 Læringsmål

Denne notesbog demonstrerer, hvordan man bygger enterprise-grade Retrieval-Augmented Generation (RAG) systemer ved brug af Microsoft Agent Framework i .NET med Microsoft Foundry. Du lærer at oprette produktionsklare agenter, der kan søge igennem dokumenter og give præcise, kontekstbevidste svar med enterprise-sikkerhed og skalerbarhed.

**Enterprise RAG Funktioner, du vil opbygge:**
- 📚 **Dokumentintelligens**: Avanceret dokumentbehandling med Azure AI-tjenester
- 🔍 **Semantisk Søgning**: Højtydende vektorsøgning med enterprise-funktioner
- 🛡️ **Sikkerhedsintegration**: Rollebaseret adgang og databeskyttelsesmønstre
- 🏢 **Skalerbar Arkitektur**: Produktionsklare RAG-systemer med overvågning

## 🎯 Enterprise RAG Arkitektur

### Kernekomponenter for Enterprise
- **Microsoft Foundry**: Administreret enterprise AI-platform med sikkerhed og overholdelse
- **Vedvarende Agenter**: Stateful agenter med samtalehistorik og kontekststyring
- **Vektorbutikadministration**: Enterprise-grade dokumentindeksering og hentning
- **Identitetsintegration**: Azure AD-autentificering og rollebaseret adgangskontrol

### Fordele ved .NET til Enterprise
- **Typesikkerhed**: Kompilerings-tidsvalidering for RAG-operationer og datastrukturer
- **Asynkron Ydeevne**: Ikke-blokerende dokumentbehandling og søgeoperationer
- **Hukommelsesstyring**: Effektiv ressourceudnyttelse til store dokumentsamlinger
- **Integrationsmønstre**: Indbygget Azure-tjenesteintegration med dependency injection

## 🏗️ Teknisk Arkitektur

### Enterprise RAG Pipeline
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Kerne .NET-komponenter
- **Azure.AI.Agents.Persistent**: Enterprise agentstyring med tilstandsbevarelse
- **Azure.Identity**: Integreret autentifikation til sikker Azure-tjenesteadgang
- **Microsoft.Agents.AI.AzureAI**: Azure-optimeret agentframework-implementering
- **System.Linq.Async**: Højtydende asynkrone LINQ-operationer

## 🔧 Enterprise Funktioner & Fordele

### Sikkerhed & Overholdelse
- **Azure AD Integration**: Enterprise identitetsstyring og autentifikation
- **Rollebaseret Adgang**: Fine-grained tilladelser til dokumentadgang og operationer
- **Databeskyttelse**: Kryptering i hvile og under transit for følsomme dokumenter
- **Audit Logging**: Omfattende aktivitetsregistrering til overholdelseskrav

### Ydeevne & Skalerbarhed
- **Forbindelsespuljer**: Effektiv Azure-tjenesteforbindelsesstyring
- **Asynkron Behandling**: Ikke-blokerende operationer til høj-throughput scenarier
- **Caching-strategier**: Intelligent caching af ofte tilgåede dokumenter
- **Load Balancing**: Distribueret behandling til store implementeringer

### Administration & Overvågning
- **Health Checks**: Indbygget overvågning af RAG-systemkomponenter
- **Ydelsesmålinger**: Detaljeret analyse af søgekvalitet og svartider
- **Fejlhåndtering**: Omfattende undtagelseshåndtering med retry-politikker
- **Konfigurationsstyring**: Miljøspecifikke indstillinger med validering

## ⚙️ Forudsætninger & Opsætning

**Udviklingsmiljø:**
- .NET 9.0 SDK eller nyere
- Visual Studio 2022 eller VS Code med C#-udvidelse
- Azure-abonnement med adgang til Microsoft Foundry

**Påkrævede NuGet-pakker:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Azure Autentificeringsopsætning:**
```bash
# Installer Azure CLI og godkend
az login
az account set --subscription "your-subscription-id"
```

**Miljøkonfiguration:**
* Microsoft Foundry-konfiguration (automatisk håndteret via Azure CLI)
* Sørg for, at du er autentificeret til det rigtige Azure-abonnement

## 📊 Enterprise RAG Mønstre

### Dokumentadministrationsmønstre
- **Bulk Upload**: Effektiv behandling af store dokumentsamlinger
- **Inkrementelle Opdateringer**: Real-time dokumenttilføjelse og ændringer
- **Versionskontrol**: Dokumentversionering og ændringssporing
- **Metadataadministration**: Rige dokumentattributter og taksonomi

### Søge- & Hentningsmønstre
- **Hybrid Søgning**: Kombinere semantisk og søgeordssøgning for optimale resultater
- **Facetteret Søgning**: Multidimensionel filtrering og kategorisering
- **Relevanstilpasning**: Tilpassede scorealgoritmer til domænespecifikke behov
- **Resultatrangering**: Avanceret rangering med forretningslogikintegration

### Sikkerhedsmønstre
- **Dokumentnivåsikkerhed**: Finmasket adgangskontrol pr. dokument
- **Dataklassifikation**: Automatisk mærkning af følsomhed og beskyttelse
- **Auditspor**: Omfattende logging af alle RAG-operationer
- **Privatlivsbeskyttelse**: PII-detektion og udtoningsfunktioner

## 🔒 Enterprise Sikkerhedsfunktioner

### Autentifikation & Autorisation
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

### Databeskyttelse
- **Kryptering**: End-to-end-kryptering for dokumenter og søgeindekser
- **Adgangskontroller**: Integration med Azure AD for bruger- og gruppetilladelser
- **Dataopholdssted**: Geografiske datalokaliseringskontroller for overholdelse
- **Backup & Recovery**: Automatiserede backup- og katastrofegendannelsesmuligheder

## 📈 Ydeevneoptimering

### Asynkrone Behandlingsmønstre
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Hukommelsesstyring
- **Streaming Behandling**: Håndter store dokumenter uden hukommelsesproblemer
- **Ressourcepuljning**: Effektiv genbrug af dyre ressourcer
- **Garbage Collection**: Optimerede hukommelsesallokeringsmønstre
- **Forbindelsesstyring**: Korrekt Azure-tjenesteforbindelses livscyklus

### Caching-strategier
- **Forespørgselscaching**: Cache af ofte udførte søgninger
- **Dokumentcaching**: Hukommelses-caching til hotte dokumenter
- **Indekscaching**: Optimeret caching af vektorindeks
- **Resultatcaching**: Intelligent caching af genererede svar

## 📊 Enterprise Use Cases

### Vidensstyring
- **Firma Wiki**: Intelligent søgning på tværs af virksomhedens vidensbaser
- **Politikker & Procedurer**: Automatiseret overholdelse og procedurevejledning
- **Træningsmaterialer**: Intelligent lærings- og udviklingsassistance
- **Forskningsdatabaser**: Akademiske og forskningspapirsanalyssystemer

### Kundesupport
- **Support Vidensbase**: Automatiserede kundeservicerespons
- **Produktdokumentation**: Intelligent informationshentning om produkter
- **Fejlfindingvejledninger**: Kontekstuel problemløsningsassistance
- **FAQ-systemer**: Dynamisk FAQ-generering fra dokumentsamlinger

### Regulatorisk Overholdelse
- **Juridisk Dokumentanalyse**: Kontrakt- og juridisk dokumentintelligens
- **Overvågning af Overholdelse**: Automatiseret kontrol af regulativ overholdelse
- **Risikoevaluering**: Dokumentbaseret risikoanalyse og rapportering
- **Revision Support**: Intelligent dokumentopdagelse til revisioner

## 🚀 Produktionsudrulning

### Overvågning & Observabilitet
- **Application Insights**: Detaljeret telemetri og ydelsesovervågning
- **Brugertilpassede Metrics**: Forretningsspecifik KPI-overvågning og alarmering
- **Distribueret Tracing**: End-to-end sporbarhed af forespørgsler på tværs af tjenester
- **Health Dashboards**: Realtidsvisualisering af systemets helbred og ydeevne

### Skalerbarhed & Pålidelighed
- **Auto-Scaling**: Automatisk skalering baseret på belastnings- og ydelsesmålinger
- **Høj Tilgængelighed**: Multi-region udrulning med failover-muligheder
- **Load Testing**: Ydelsesvalidering under enterprise belastningsforhold
- **Katastrofegendannelse**: Automatiserede backup- og gendannelsesprocedurer

Klar til at bygge enterprise-grade RAG-systemer, der kan håndtere følsomme dokumenter i stor skala? Lad os arkitektere intelligente videnssystemer til enterprise! 🏢📖✨

## Kodeimplementering

Det komplette fungerende kodeeksempel til denne lektion findes i `05-dotnet-agent-framework.cs`. 

For at køre eksemplet:

```bash
# Gør scriptet eksekverbart (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Kør .NET Single File App
./05-dotnet-agent-framework.cs
```

Eller brug `dotnet run` direkte:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Koden demonstrerer:

1. **Pakkebetaling**: Installation af nødvendige NuGet-pakker til Azure AI-agenter
2. **Miljøkonfiguration**: Indlæsning af Microsoft Foundry endpoint- og modelindstillinger
3. **Dokumentupload**: Upload af et dokument til RAG-behandling
4. **Vektorbutik Oprettelse**: Oprettelse af en vektorbutik til semantisk søgning
5. **Agentkonfiguration**: Opsætning af en AI-agent med fil-søgefunktionalitet
6. **Forespørgsels-eksekvering**: Kørsel af forespørgsler mod det uploadede dokument

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->