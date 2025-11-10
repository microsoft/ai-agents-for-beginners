<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c8bc231a26e949f525d65b716538707f",
  "translation_date": "2025-11-07T09:48:58+00:00",
  "source_file": "03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.md",
  "language_code": "nl"
}
-->
# 🎨 Agentische Ontwerp Patronen met GitHub Modellen (.NET)

## 📋 Leerdoelen

Deze notebook demonstreert ontwerp patronen van ondernemingsniveau voor het bouwen van intelligente agents met behulp van het Microsoft Agent Framework in .NET, geïntegreerd met GitHub Modellen. Je leert professionele patronen en architecturale benaderingen die agents productie-klaar, onderhoudbaar en schaalbaar maken.

**Ontwerp Patronen voor Ondernemingen:**
- 🏭 **Factory Pattern**: Gestandaardiseerde agentcreatie met dependency injection
- 🔧 **Builder Pattern**: Vloeiende configuratie en opzet van agents
- 🧵 **Thread-Safe Patterns**: Beheer van gelijktijdige gesprekken
- 📋 **Repository Pattern**: Georganiseerd beheer van tools en mogelijkheden

## 🎯 .NET-Specifieke Architecturale Voordelen

### Ondernemingskenmerken
- **Sterke Typing**: Validatie tijdens compilatie en ondersteuning voor IntelliSense
- **Dependency Injection**: Ingebouwde DI-containerintegratie
- **Configuratiebeheer**: IConfiguration en Options patronen
- **Async/Await**: Ondersteuning voor asynchrone programmering van topniveau

### Productie-Klare Patronen
- **Logging Integratie**: ILogger en ondersteuning voor gestructureerde logging
- **Gezondheidscontroles**: Ingebouwde monitoring en diagnostiek
- **Configuratievalidatie**: Sterke typing met data-annotaties
- **Foutafhandeling**: Gestructureerd beheer van uitzonderingen

## 🔧 Technische Architectuur

### Kerncomponenten van .NET
- **Microsoft.Extensions.AI**: Geünificeerde AI-service abstracties
- **Microsoft.Agents.AI**: Framework voor ondernemingsagenten orkestratie
- **GitHub Modellen Integratie**: API-client patronen met hoge prestaties
- **Configuratiesysteem**: appsettings.json en omgevingsintegratie

### Implementatie van Ontwerp Patronen
```csharp
IServiceCollection → Agent Builder → Configuration → Tool Registry → AI Agent
```

## 🏗️ Gedemonstreerde Ondernemingspatronen

### 1. **Creational Patterns**
- **Agent Factory**: Gecentraliseerde agentcreatie met consistente configuratie
- **Builder Pattern**: Vloeiende API voor complexe agentconfiguratie
- **Singleton Pattern**: Beheer van gedeelde bronnen en configuratie
- **Dependency Injection**: Losse koppeling en testbaarheid

### 2. **Behavioral Patterns**
- **Strategy Pattern**: Verwisselbare uitvoeringsstrategieën voor tools
- **Command Pattern**: Geïntegreerde agentoperaties met undo/redo
- **Observer Pattern**: Event-gedreven beheer van de levenscyclus van agents
- **Template Method**: Gestandaardiseerde workflows voor agentuitvoering

### 3. **Structural Patterns**
- **Adapter Pattern**: Integratielaag voor GitHub Modellen API
- **Decorator Pattern**: Verbetering van agentmogelijkheden
- **Facade Pattern**: Vereenvoudigde interfaces voor agentinteractie
- **Proxy Pattern**: Lazy loading en caching voor prestaties

## ⚙️ Vereisten & Setup

**Ontwikkelomgeving:**
- .NET 9.0 SDK of hoger
- Visual Studio 2022 of VS Code met C# extensie
- Toegang tot GitHub Modellen API

**NuGet Afhankelijkheden:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Configuratie (.env bestand):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 📚 .NET Ontwerp Principes

### SOLID Principes
- **Single Responsibility**: Elk component heeft één duidelijke doelstelling
- **Open/Closed**: Uitbreidbaar zonder modificatie
- **Liskov Substitution**: Implementaties van tools op basis van interfaces
- **Interface Segregation**: Gerichte, samenhangende interfaces
- **Dependency Inversion**: Afhankelijkheid van abstracties, niet van concreties

### Clean Architecture
- **Domeinlaag**: Kernabstracties voor agents en tools
- **Applicatielaag**: Orkestratie en workflows van agents
- **Infrastructuurlaag**: GitHub Modellen integratie en externe services
- **Presentatielaag**: Gebruikersinteractie en responsformattering

## 🔒 Overwegingen voor Ondernemingen

### Beveiliging
- **Beheer van Referenties**: Veilige API-sleutelverwerking met IConfiguration
- **Inputvalidatie**: Sterke typing en validatie met data-annotaties
- **Outputsanitatie**: Veilige verwerking en filtering van responsen
- **Audit Logging**: Uitgebreide tracking van operaties

### Prestaties
- **Async Patronen**: Niet-blokkerende I/O-operaties
- **Connection Pooling**: Efficiënt beheer van HTTP-clients
- **Caching**: Responscaching voor verbeterde prestaties
- **Bronbeheer**: Correcte verwijdering en opruimingspatronen

### Schaalbaarheid
- **Thread Safety**: Ondersteuning voor gelijktijdige agentuitvoering
- **Resource Pooling**: Efficiënt gebruik van bronnen
- **Load Management**: Rate limiting en backpressure handling
- **Monitoring**: Prestatiemetrics en gezondheidscontroles

## 🚀 Productie Implementatie

- **Configuratiebeheer**: Omgevingsspecifieke instellingen
- **Logging Strategie**: Gestructureerde logging met correlatie-ID's
- **Foutafhandeling**: Globale uitzonderingsafhandeling met correcte herstelmethoden
- **Monitoring**: Application Insights en prestatiecounters
- **Testen**: Unit tests, integratietests en load testing patronen

Klaar om intelligente agents van ondernemingsniveau te bouwen met .NET? Laten we iets robuusts ontwerpen! 🏢✨

## Code Voorbeeld

Voor een volledig werkend voorbeeld, zie [03-dotnet-agent-framework.cs](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs).

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.