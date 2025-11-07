<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c268705e6fb2b30c7690d5b2a002e072",
  "translation_date": "2025-11-07T09:05:16+00:00",
  "source_file": "05-agentic-rag/code_samples/05-dotnet-agent-framework.md",
  "language_code": "nl"
}
-->
# 🔍 Enterprise RAG met Azure AI Foundry (.NET)

## 📋 Leerdoelen

Deze notebook laat zien hoe je enterprise-grade Retrieval-Augmented Generation (RAG)-systemen kunt bouwen met het Microsoft Agent Framework in .NET en Azure AI Foundry. Je leert productieklare agents te maken die door documenten kunnen zoeken en nauwkeurige, contextbewuste antwoorden kunnen geven met enterprise-beveiliging en schaalbaarheid.

**Enterprise RAG-mogelijkheden die je zult bouwen:**
- 📚 **Documentintelligentie**: Geavanceerde documentverwerking met Azure AI-services
- 🔍 **Semantisch zoeken**: Hoogwaardige vectorzoekfunctie met enterprise-functionaliteiten
- 🛡️ **Beveiligingsintegratie**: Rolgebaseerde toegang en patronen voor gegevensbescherming
- 🏢 **Schaalbare architectuur**: Productieklare RAG-systemen met monitoring

## 🎯 Enterprise RAG-architectuur

### Kerncomponenten voor ondernemingen
- **Azure AI Foundry**: Beheerd enterprise AI-platform met beveiliging en compliance
- **Persistente agents**: Stateful agents met gespreksgeschiedenis en contextbeheer
- **Vector Store Management**: Enterprise-grade documentindexering en -opvraging
- **Identiteitsintegratie**: Azure AD-authenticatie en rolgebaseerde toegangscontrole

### Voordelen van .NET voor ondernemingen
- **Typeveiligheid**: Validatie tijdens compilatie voor RAG-bewerkingen en datastructuren
- **Async-prestaties**: Niet-blokkerende documentverwerking en zoekbewerkingen
- **Geheugenbeheer**: Efficiënt gebruik van resources voor grote documentcollecties
- **Integratiepatronen**: Native integratie van Azure-services met dependency injection

## 🏗️ Technische architectuur

### Enterprise RAG-pijplijn
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Kerncomponenten van .NET
- **Azure.AI.Agents.Persistent**: Beheer van enterprise agents met statuspersistentie
- **Azure.Identity**: Geïntegreerde authenticatie voor veilige toegang tot Azure-services
- **Microsoft.Agents.AI.AzureAI**: Azure-geoptimaliseerde implementatie van het agentframework
- **System.Linq.Async**: Hoogwaardige asynchrone LINQ-bewerkingen

## 🔧 Enterprise-functies en voordelen

### Beveiliging en compliance
- **Azure AD-integratie**: Enterprise-identiteitsbeheer en authenticatie
- **Rolgebaseerde toegang**: Fijnmazige machtigingen voor documenttoegang en -bewerkingen
- **Gegevensbescherming**: Versleuteling in rust en tijdens transport voor gevoelige documenten
- **Auditlogging**: Uitgebreide activiteitstracking voor compliancevereisten

### Prestaties en schaalbaarheid
- **Connection pooling**: Efficiënt beheer van Azure-serviceverbindingen
- **Async-verwerking**: Niet-blokkerende bewerkingen voor scenario's met hoge doorvoer
- **Cachingstrategieën**: Slimme caching voor vaak geraadpleegde documenten
- **Load balancing**: Gedistribueerde verwerking voor grootschalige implementaties

### Beheer en monitoring
- **Gezondheidscontroles**: Ingebouwde monitoring voor RAG-systeemcomponenten
- **Prestatiestatistieken**: Gedetailleerde analyses van zoekkwaliteit en responstijden
- **Foutafhandeling**: Uitgebreid uitzonderingsbeheer met retry-beleid
- **Configuratiebeheer**: Omgevingsspecifieke instellingen met validatie

## ⚙️ Vereisten en installatie

**Ontwikkelomgeving:**
- .NET 9.0 SDK of hoger
- Visual Studio 2022 of VS Code met C#-extensie
- Azure-abonnement met toegang tot AI Foundry

**Vereiste NuGet-pakketten:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Azure-authenticatie instellen:**
```bash
# Install Azure CLI and authenticate
az login
az account set --subscription "your-subscription-id"
```

**Omgevingsconfiguratie:**
* Configuratie van Azure AI Foundry (automatisch afgehandeld via Azure CLI)
* Zorg ervoor dat je bent geauthenticeerd bij het juiste Azure-abonnement

## 📊 Enterprise RAG-patronen

### Documentbeheerpatronen
- **Bulk upload**: Efficiënte verwerking van grote documentcollecties
- **Incrementele updates**: Realtime toevoeging en wijziging van documenten
- **Versiebeheer**: Versiebeheer en wijzigingsregistratie van documenten
- **Metadatabeheer**: Rijke documentattributen en taxonomie

### Zoek- en opvraagpatronen
- **Hybride zoeken**: Combinatie van semantisch en trefwoord zoeken voor optimale resultaten
- **Gefacetteerd zoeken**: Multidimensionale filtering en categorisatie
- **Relevantieafstemming**: Aangepaste scoringsalgoritmen voor domeinspecifieke behoeften
- **Resultaatrangschikking**: Geavanceerde rangschikking met integratie van bedrijfslogica

### Beveiligingspatronen
- **Documentniveau beveiliging**: Fijnmazige toegangscontrole per document
- **Gegevensclassificatie**: Automatische gevoeligheidslabeling en bescherming
- **Audit trails**: Uitgebreide logging van alle RAG-bewerkingen
- **Privacybescherming**: Detectie en redactie van PII (persoonlijk identificeerbare informatie)

## 🔒 Enterprise beveiligingsfuncties

### Authenticatie en autorisatie
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

### Gegevensbescherming
- **Versleuteling**: End-to-end versleuteling voor documenten en zoekindexen
- **Toegangscontrole**: Integratie met Azure AD voor gebruikers- en groepsmachtigingen
- **Gegevenslocatie**: Geografische gegevenslocatiecontrole voor compliance
- **Back-up en herstel**: Geautomatiseerde back-up en herstelmogelijkheden

## 📈 Prestatieoptimalisatie

### Async-verwerkingspatronen
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Geheugenbeheer
- **Streamingverwerking**: Grote documenten verwerken zonder geheugenproblemen
- **Resource pooling**: Efficiënt hergebruik van dure resources
- **Garbage collection**: Geoptimaliseerde patronen voor geheugentoewijzing
- **Verbindingsbeheer**: Correcte levenscyclus van Azure-serviceverbindingen

### Cachingstrategieën
- **Query caching**: Cache vaak uitgevoerde zoekopdrachten
- **Document caching**: In-memory caching voor veelgebruikte documenten
- **Index caching**: Geoptimaliseerde vectorindex caching
- **Resultaat caching**: Intelligente caching van gegenereerde antwoorden

## 📊 Enterprise-toepassingen

### Kennisbeheer
- **Bedrijfswiki**: Slim zoeken in bedrijfskennisbanken
- **Beleid en procedures**: Geautomatiseerde compliance- en procedurebegeleiding
- **Trainingsmateriaal**: Intelligente ondersteuning bij leren en ontwikkelen
- **Onderzoeksdatabases**: Analyse van academische en onderzoeksdocumenten

### Klantenservice
- **Support kennisbank**: Geautomatiseerde klantenservice-antwoorden
- **Productdocumentatie**: Slimme informatieopvraging over producten
- **Probleemoplossingsgidsen**: Contextuele hulp bij probleemoplossing
- **FAQ-systemen**: Dynamische FAQ-generatie uit documentcollecties

### Regelgevingscompliance
- **Analyse van juridische documenten**: Intelligentie voor contracten en juridische documenten
- **Compliance monitoring**: Geautomatiseerde controle op naleving van regelgeving
- **Risicobeoordeling**: Documentgebaseerde risicoanalyse en rapportage
- **Auditondersteuning**: Slimme documentontdekking voor audits

## 🚀 Productie-implementatie

### Monitoring en observatie
- **Application Insights**: Gedetailleerde telemetrie en prestatiemonitoring
- **Aangepaste statistieken**: KPI-tracking en waarschuwingen specifiek voor het bedrijf
- **Gedistribueerde tracing**: End-to-end tracking van verzoeken over services
- **Gezondheidsdashboards**: Realtime visualisatie van systeemgezondheid en prestaties

### Schaalbaarheid en betrouwbaarheid
- **Auto-scaling**: Automatische schaalvergroting op basis van belasting en prestatiedata
- **Hoge beschikbaarheid**: Multi-regio implementatie met failovermogelijkheden
- **Load testing**: Prestatievalidatie onder enterprise-belastingcondities
- **Disaster recovery**: Geautomatiseerde back-up en herstelprocedures

Klaar om enterprise-grade RAG-systemen te bouwen die gevoelige documenten op schaal kunnen verwerken? Laten we intelligente kennissystemen voor ondernemingen ontwerpen! 🏢📖✨

## Code-implementatie

De volledige werkende codevoorbeeld voor deze les is beschikbaar in `05-dotnet-agent-framework.cs`. 

Om het voorbeeld uit te voeren:

```bash
# Make the script executable (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Run the .NET Single File App
./05-dotnet-agent-framework.cs
```

Of gebruik `dotnet run` direct:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

De code demonstreert:

1. **Pakketinstallatie**: Installeren van vereiste NuGet-pakketten voor Azure AI Agents
2. **Omgevingsconfiguratie**: Laden van Azure AI Foundry-eindpunt en modelinstellingen
3. **Documentupload**: Uploaden van een document voor RAG-verwerking
4. **Vector Store-creatie**: Creëren van een vector store voor semantisch zoeken
5. **Agentconfiguratie**: Instellen van een AI-agent met zoekmogelijkheden in bestanden
6. **Query-uitvoering**: Uitvoeren van zoekopdrachten op het geüploade document

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.