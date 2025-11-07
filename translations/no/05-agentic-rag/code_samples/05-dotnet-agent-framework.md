<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c268705e6fb2b30c7690d5b2a002e072",
  "translation_date": "2025-11-07T09:04:32+00:00",
  "source_file": "05-agentic-rag/code_samples/05-dotnet-agent-framework.md",
  "language_code": "no"
}
-->
# 🔍 Enterprise RAG med Azure AI Foundry (.NET)

## 📋 Læringsmål

Denne notatboken viser hvordan man bygger bedriftsklare Retrieval-Augmented Generation (RAG)-systemer ved hjelp av Microsoft Agent Framework i .NET med Azure AI Foundry. Du vil lære å lage produksjonsklare agenter som kan søke gjennom dokumenter og gi nøyaktige, kontekstbevisste svar med bedriftsnivå sikkerhet og skalerbarhet.

**Enterprise RAG-funksjoner du vil bygge:**
- 📚 **Dokumentintelligens**: Avansert dokumentbehandling med Azure AI-tjenester
- 🔍 **Semantisk søk**: Høyytelses vektorsøk med bedriftsfunksjoner
- 🛡️ **Sikkerhetsintegrasjon**: Rollebasert tilgang og mønstre for databeskyttelse
- 🏢 **Skalerbar arkitektur**: Produksjonsklare RAG-systemer med overvåking

## 🎯 Enterprise RAG-arkitektur

### Kjernekomponenter for bedrifter
- **Azure AI Foundry**: Administrert AI-plattform for bedrifter med sikkerhet og samsvar
- **Vedvarende agenter**: Tilstandsfulle agenter med samtalehistorikk og kontekststyring
- **Vektorlagringsadministrasjon**: Bedriftsnivå dokumentindeksering og gjenfinning
- **Identitetsintegrasjon**: Azure AD-autentisering og rollebasert tilgangskontroll

### Fordeler med .NET for bedrifter
- **Type-sikkerhet**: Validering av RAG-operasjoner og datastrukturer ved kompilering
- **Asynkron ytelse**: Ikke-blokkerende dokumentbehandling og søkeoperasjoner
- **Minnehåndtering**: Effektiv ressursutnyttelse for store dokumentkolleksjoner
- **Integrasjonsmønstre**: Naturlig integrasjon med Azure-tjenester via avhengighetsinjeksjon

## 🏗️ Teknisk arkitektur

### Enterprise RAG-pipeline
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Kjernekomponenter i .NET
- **Azure.AI.Agents.Persistent**: Administrasjon av bedriftsagenter med tilstandslagring
- **Azure.Identity**: Integrert autentisering for sikker tilgang til Azure-tjenester
- **Microsoft.Agents.AI.AzureAI**: Azure-optimalisert implementering av agentrammeverket
- **System.Linq.Async**: Høyytelses asynkrone LINQ-operasjoner

## 🔧 Enterprise-funksjoner og fordeler

### Sikkerhet og samsvar
- **Azure AD-integrasjon**: Identitetsadministrasjon og autentisering for bedrifter
- **Rollebasert tilgang**: Finkornet tillatelse for dokumenttilgang og operasjoner
- **Databeskyttelse**: Kryptering i ro og under overføring for sensitive dokumenter
- **Revisjonslogging**: Omfattende aktivitetsregistrering for samsvarskrav

### Ytelse og skalerbarhet
- **Tilkoblingspooling**: Effektiv administrasjon av Azure-tjenestetilkoblinger
- **Asynkron behandling**: Ikke-blokkerende operasjoner for høy gjennomstrømning
- **Cache-strategier**: Intelligent caching for ofte brukte dokumenter
- **Lastbalansering**: Distribuert behandling for storskala distribusjoner

### Administrasjon og overvåking
- **Helsetester**: Innebygd overvåking av RAG-systemkomponenter
- **Ytelsesmetrikker**: Detaljert analyse av søkekvalitet og responstider
- **Feilhåndtering**: Omfattende unntakshåndtering med gjenforsøkspolicyer
- **Konfigurasjonsadministrasjon**: Miljøspesifikke innstillinger med validering

## ⚙️ Forutsetninger og oppsett

**Utviklingsmiljø:**
- .NET 9.0 SDK eller nyere
- Visual Studio 2022 eller VS Code med C#-utvidelse
- Azure-abonnement med tilgang til AI Foundry

**Påkrevde NuGet-pakker:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Azure-autentiseringsoppsett:**
```bash
# Install Azure CLI and authenticate
az login
az account set --subscription "your-subscription-id"
```

**Miljøkonfigurasjon:**
* Konfigurasjon av Azure AI Foundry (automatisk håndtert via Azure CLI)
* Sørg for at du er autentisert til riktig Azure-abonnement

## 📊 Enterprise RAG-mønstre

### Dokumentadministrasjonsmønstre
- **Bulkopplasting**: Effektiv behandling av store dokumentkolleksjoner
- **Inkrementelle oppdateringer**: Sanntids tillegg og modifikasjon av dokumenter
- **Versjonskontroll**: Dokumentversjonering og endringssporing
- **Metadataadministrasjon**: Rike dokumentattributter og taksonomi

### Søke- og gjenfinningsmønstre
- **Hybrid søk**: Kombinering av semantisk og nøkkelordssøk for optimale resultater
- **Fasettert søk**: Multidimensjonal filtrering og kategorisering
- **Relevansjustering**: Tilpassede rangeringsalgoritmer for spesifikke domener
- **Resultatrangering**: Avansert rangering med integrasjon av forretningslogikk

### Sikkerhetsmønstre
- **Dokumentnivå sikkerhet**: Finkornet tilgangskontroll per dokument
- **Dataklassifisering**: Automatisk sensitivitetsetikettering og beskyttelse
- **Revisjonsspor**: Omfattende logging av alle RAG-operasjoner
- **Personvern**: PII-deteksjon og redigeringsfunksjoner

## 🔒 Enterprise sikkerhetsfunksjoner

### Autentisering og autorisasjon
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
- **Kryptering**: Ende-til-ende kryptering for dokumenter og søkeindekser
- **Tilgangskontroller**: Integrasjon med Azure AD for bruker- og gruppeautorisasjon
- **Dataresidens**: Geografisk datalokasjonskontroll for samsvar
- **Backup og gjenoppretting**: Automatiserte backup- og katastrofegjenopprettingsfunksjoner

## 📈 Ytelsesoptimalisering

### Asynkrone behandlingsmønstre
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Minnehåndtering
- **Streaming-behandling**: Håndtering av store dokumenter uten minneproblemer
- **Ressurspooling**: Effektiv gjenbruk av kostbare ressurser
- **Søppelsamling**: Optimaliserte mønstre for minneallokering
- **Tilkoblingsadministrasjon**: Riktig livssyklus for Azure-tjenestetilkoblinger

### Cache-strategier
- **Spørringscache**: Cache ofte utførte søk
- **Dokumentcache**: Minnebasert caching for populære dokumenter
- **Indekscache**: Optimalisert vektorindekscaching
- **Resultatcache**: Intelligent caching av genererte svar

## 📊 Enterprise brukstilfeller

### Kunnskapsadministrasjon
- **Bedriftswiki**: Intelligent søk i bedriftens kunnskapsbaser
- **Policyer og prosedyrer**: Automatisert samsvar og veiledning for prosedyrer
- **Opplæringsmateriale**: Intelligent lærings- og utviklingsassistanse
- **Forskningsdatabaser**: Analyse av akademiske og forskningsartikler

### Kundestøtte
- **Støttekunnskapsbase**: Automatiserte kundeserviceresponser
- **Produktdokumentasjon**: Intelligent gjenfinning av produktinformasjon
- **Feilsøkingsveiledninger**: Kontekstuell problemløsningsassistanse
- **FAQ-systemer**: Dynamisk FAQ-generering fra dokumentkolleksjoner

### Regulatorisk samsvar
- **Analyse av juridiske dokumenter**: Intelligens for kontrakter og juridiske dokumenter
- **Samsvarsovervåking**: Automatisert kontroll av regulatorisk samsvar
- **Risikovurdering**: Dokumentbasert risikoanalyse og rapportering
- **Revisjonsstøtte**: Intelligent dokumentgjenfinning for revisjoner

## 🚀 Produksjonsdistribusjon

### Overvåking og observasjon
- **Application Insights**: Detaljert telemetri og ytelsesovervåking
- **Egendefinerte metrikker**: Spesifikke KPI-sporing og varsling
- **Distribuert sporing**: Ende-til-ende forespørselssporing på tvers av tjenester
- **Helsetavler**: Sanntids visualisering av systemhelse og ytelse

### Skalerbarhet og pålitelighet
- **Auto-skalering**: Automatisk skalering basert på belastning og ytelsesmetrikker
- **Høy tilgjengelighet**: Distribusjon på tvers av regioner med failover-funksjoner
- **Lasttesting**: Ytelsesvalidering under bedriftsbelastning
- **Katastrofegjenoppretting**: Automatiserte backup- og gjenopprettingsprosedyrer

Klar til å bygge bedriftsklare RAG-systemer som kan håndtere sensitive dokumenter i stor skala? La oss arkitektere intelligente kunnskapssystemer for bedrifter! 🏢📖✨

## Kodeimplementering

Den komplette fungerende kodeeksempelet for denne leksjonen er tilgjengelig i `05-dotnet-agent-framework.cs`. 

For å kjøre eksempelet:

```bash
# Make the script executable (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Run the .NET Single File App
./05-dotnet-agent-framework.cs
```

Eller bruk `dotnet run` direkte:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Koden demonstrerer:

1. **Pakkeinstallasjon**: Installering av nødvendige NuGet-pakker for Azure AI-agenter
2. **Miljøkonfigurasjon**: Laste inn Azure AI Foundry-endepunkt og modellinnstillinger
3. **Dokumentopplasting**: Opplasting av et dokument for RAG-behandling
4. **Vektorlageroppretting**: Oppretting av et vektorlager for semantisk søk
5. **Agentkonfigurasjon**: Oppsett av en AI-agent med filsøkemuligheter
6. **Spørringsutførelse**: Kjøre spørringer mot det opplastede dokumentet

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.