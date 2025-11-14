<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c268705e6fb2b30c7690d5b2a002e072",
  "translation_date": "2025-11-07T09:04:13+00:00",
  "source_file": "05-agentic-rag/code_samples/05-dotnet-agent-framework.md",
  "language_code": "da"
}
-->
# 🔍 Enterprise RAG med Azure AI Foundry (.NET)

## 📋 Læringsmål

Denne notebook demonstrerer, hvordan man bygger virksomhedsklare Retrieval-Augmented Generation (RAG) systemer ved hjælp af Microsoft Agent Framework i .NET med Azure AI Foundry. Du vil lære at skabe produktionsklare agenter, der kan søge i dokumenter og levere præcise, kontekstbevidste svar med virksomhedssikkerhed og skalerbarhed.

**Enterprise RAG-funktioner, du vil bygge:**
- 📚 **Dokumentintelligens**: Avanceret dokumentbehandling med Azure AI-tjenester
- 🔍 **Semantisk søgning**: Højtydende vektorsøgning med virksomhedsfunktioner
- 🛡️ **Sikkerhedsintegration**: Rollebaseret adgang og databeskyttelsesmønstre
- 🏢 **Skalerbar arkitektur**: Produktionsklare RAG-systemer med overvågning

## 🎯 Enterprise RAG Arkitektur

### Centrale virksomhedskomponenter
- **Azure AI Foundry**: Administreret virksomhedens AI-platform med sikkerhed og overholdelse
- **Vedvarende agenter**: Agenter med tilstandshistorik og kontekststyring
- **Vector Store Management**: Virksomhedsklar dokumentindeksering og -hentning
- **Identitetsintegration**: Azure AD-autentificering og rollebaseret adgangskontrol

### Fordele ved .NET i virksomheder
- **Type Safety**: Validering af RAG-operationer og datastrukturer ved kompilering
- **Async Performance**: Ikke-blokerende dokumentbehandling og søgeoperationer
- **Memory Management**: Effektiv ressourceudnyttelse for store dokumentkollektioner
- **Integrationsmønstre**: Naturlig integration med Azure-tjenester via dependency injection

## 🏗️ Teknisk Arkitektur

### Enterprise RAG Pipeline
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Centrale .NET-komponenter
- **Azure.AI.Agents.Persistent**: Virksomhedens agentstyring med tilstandspersistens
- **Azure.Identity**: Integreret autentificering for sikker adgang til Azure-tjenester
- **Microsoft.Agents.AI.AzureAI**: Azure-optimeret agentframework-implementering
- **System.Linq.Async**: Højtydende asynkrone LINQ-operationer

## 🔧 Enterprise Funktioner & Fordele

### Sikkerhed & Overholdelse
- **Azure AD Integration**: Virksomhedens identitetsstyring og autentificering
- **Rollebaseret adgang**: Finkornede tilladelser til dokumentadgang og operationer
- **Databeskyttelse**: Kryptering i hvile og under transport for følsomme dokumenter
- **Audit Logging**: Omfattende aktivitetsregistrering for overholdelseskrav

### Ydeevne & Skalerbarhed
- **Connection Pooling**: Effektiv styring af Azure-tjenesteforbindelser
- **Async Processing**: Ikke-blokerende operationer for scenarier med høj gennemstrømning
- **Caching Strategies**: Intelligent caching for ofte tilgåede dokumenter
- **Load Balancing**: Distribueret behandling for store implementeringer

### Styring & Overvågning
- **Health Checks**: Indbygget overvågning af RAG-systemkomponenter
- **Performance Metrics**: Detaljeret analyse af søgekvalitet og svartider
- **Error Handling**: Omfattende undtagelseshåndtering med genforsøgspolitikker
- **Configuration Management**: Miljøspecifikke indstillinger med validering

## ⚙️ Forudsætninger & Opsætning

**Udviklingsmiljø:**
- .NET 9.0 SDK eller nyere
- Visual Studio 2022 eller VS Code med C#-udvidelse
- Azure-abonnement med AI Foundry-adgang

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
# Install Azure CLI and authenticate
az login
az account set --subscription "your-subscription-id"
```

**Miljøkonfiguration:**
* Azure AI Foundry-konfiguration (automatisk håndteret via Azure CLI)
* Sørg for, at du er autentificeret til det korrekte Azure-abonnement

## 📊 Enterprise RAG Mønstre

### Dokumentstyringsmønstre
- **Bulk Upload**: Effektiv behandling af store dokumentkollektioner
- **Incremental Updates**: Realtids tilføjelse og ændring af dokumenter
- **Version Control**: Dokumentversionering og ændringssporing
- **Metadata Management**: Rige dokumentattributter og taksonomi

### Søge- & Hentemønstre
- **Hybrid Search**: Kombination af semantisk og nøgleordssøgning for optimale resultater
- **Faceted Search**: Multidimensionel filtrering og kategorisering
- **Relevance Tuning**: Tilpassede scoringsalgoritmer til domænespecifikke behov
- **Result Ranking**: Avanceret rangering med forretningslogik-integration

### Sikkerhedsmønstre
- **Document-Level Security**: Finkornet adgangskontrol pr. dokument
- **Data Classification**: Automatisk følsomhedsmærkning og beskyttelse
- **Audit Trails**: Omfattende logning af alle RAG-operationer
- **Privacy Protection**: PII-detektion og redigeringsfunktioner

## 🔒 Enterprise Sikkerhedsfunktioner

### Autentificering & Autorisation
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
- **Kryptering**: End-to-end kryptering for dokumenter og søgeindekser
- **Adgangskontrol**: Integration med Azure AD for bruger- og gruppeadgang
- **Data Residency**: Geografisk dataplacering for overholdelse
- **Backup & Recovery**: Automatiserede backup- og katastrofehåndteringsfunktioner

## 📈 Ydeevneoptimering

### Async Processing Mønstre
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Memory Management
- **Streaming Processing**: Håndtering af store dokumenter uden hukommelsesproblemer
- **Resource Pooling**: Effektiv genbrug af dyre ressourcer
- **Garbage Collection**: Optimerede hukommelsesallokeringsmønstre
- **Connection Management**: Korrekt livscyklus for Azure-tjenesteforbindelser

### Caching Strategies
- **Query Caching**: Cache ofte udførte søgninger
- **Document Caching**: In-memory caching for populære dokumenter
- **Index Caching**: Optimeret vektorindekscaching
- **Result Caching**: Intelligent caching af genererede svar

## 📊 Enterprise Anvendelsesområder

### Vidensstyring
- **Corporate Wiki**: Intelligent søgning på tværs af virksomhedens vidensbaser
- **Policy & Procedures**: Automatiseret overholdelse og procedurevejledning
- **Training Materials**: Intelligent lærings- og udviklingsassistance
- **Research Databases**: Analyse af akademiske og forskningsartikler

### Kundesupport
- **Support Knowledge Base**: Automatiserede kundeservice-svar
- **Produktdokumentation**: Intelligent produktinformationshentning
- **Fejlfindingsguider**: Kontekstuel problemløsningsassistance
- **FAQ Systems**: Dynamisk FAQ-generering fra dokumentkollektioner

### Overholdelse af regler
- **Juridisk dokumentanalyse**: Intelligens for kontrakter og juridiske dokumenter
- **Compliance Monitoring**: Automatiseret kontrol af regeloverholdelse
- **Risk Assessment**: Dokumentbaseret risikovurdering og rapportering
- **Audit Support**: Intelligent dokumentopdagelse til revisioner

## 🚀 Produktionsimplementering

### Overvågning & Synlighed
- **Application Insights**: Detaljeret telemetri og ydeevneovervågning
- **Custom Metrics**: Virksomhedsspecifik KPI-sporing og alarmering
- **Distributed Tracing**: End-to-end anmodningssporing på tværs af tjenester
- **Health Dashboards**: Realtids visualisering af systemets sundhed og ydeevne

### Skalerbarhed & Pålidelighed
- **Auto-Scaling**: Automatisk skalering baseret på belastning og ydeevnemålinger
- **High Availability**: Multi-region implementering med failover-funktioner
- **Load Testing**: Ydeevnevalidering under virksomhedens belastningsforhold
- **Disaster Recovery**: Automatiserede backup- og genoprettelsesprocedurer

Klar til at bygge virksomhedsklare RAG-systemer, der kan håndtere følsomme dokumenter i stor skala? Lad os designe intelligente videnssystemer til virksomheder! 🏢📖✨

## Kodeimplementering

Den komplette arbejdskode for denne lektion er tilgængelig i `05-dotnet-agent-framework.cs`. 

For at køre eksemplet:

```bash
# Make the script executable (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Run the .NET Single File App
./05-dotnet-agent-framework.cs
```

Eller brug `dotnet run` direkte:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Koden demonstrerer:

1. **Pakkeinstallation**: Installation af nødvendige NuGet-pakker til Azure AI Agents
2. **Miljøkonfiguration**: Indlæsning af Azure AI Foundry-endpoint og modelindstillinger
3. **Dokumentupload**: Upload af et dokument til RAG-behandling
4. **Vector Store Creation**: Oprettelse af en vektorbutik til semantisk søgning
5. **Agentkonfiguration**: Opsætning af en AI-agent med filsøgningsfunktioner
6. **Query Execution**: Udførelse af forespørgsler mod det uploadede dokument

---

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi er ikke ansvarlige for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.