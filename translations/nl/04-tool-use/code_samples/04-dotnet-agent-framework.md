<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f82a3992438bcc028a2569c5fed828a9",
  "translation_date": "2025-11-07T09:26:06+00:00",
  "source_file": "04-tool-use/code_samples/04-dotnet-agent-framework.md",
  "language_code": "nl"
}
-->
# 🛠️ Geavanceerd gebruik van tools met GitHub-modellen (.NET)

## 📋 Leerdoelen

Dit notebook demonstreert integratiepatronen van tools op ondernemingsniveau met behulp van het Microsoft Agent Framework in .NET en GitHub-modellen. Je leert geavanceerde agents bouwen met meerdere gespecialiseerde tools, waarbij je profiteert van de sterke typificatie van C# en de enterprise-functies van .NET.

**Geavanceerde toolmogelijkheden die je zult beheersen:**
- 🔧 **Multi-Tool Architectuur**: Agents bouwen met meerdere gespecialiseerde mogelijkheden
- 🎯 **Type-Safe Tool Uitvoering**: Gebruik maken van C#'s compile-time validatie
- 📊 **Enterprise Tool Patronen**: Productieklaar toolontwerp en foutafhandeling
- 🔗 **Toolcompositie**: Tools combineren voor complexe bedrijfsworkflows

## 🎯 Voordelen van .NET Tool Architectuur

### Enterprise Tool Functies
- **Compile-Time Validatie**: Sterke typificatie zorgt voor correcte toolparameters
- **Dependency Injection**: IoC-containerintegratie voor toolbeheer
- **Async/Await Patronen**: Niet-blokkerende tooluitvoering met goed resourcebeheer
- **Gestructureerd Loggen**: Ingebouwde logintegratie voor monitoring van tooluitvoering

### Productieklare Patronen
- **Foutafhandeling**: Uitgebreid foutbeheer met getypeerde uitzonderingen
- **Resourcebeheer**: Correcte afvoermethoden en geheugenbeheer
- **Prestatiemonitoring**: Ingebouwde metrics en prestatiecounters
- **Configuratiebeheer**: Type-veilige configuratie met validatie

## 🔧 Technische Architectuur

### Kerncomponenten van .NET Tools
- **Microsoft.Extensions.AI**: Uniforme abstractielaag voor tools
- **Microsoft.Agents.AI**: Toolorkestratie op ondernemingsniveau
- **GitHub Models Integratie**: Hoogpresterende API-client met connection pooling

### Tooluitvoeringspijplijn
```
User Request → Agent Analysis → Tool Selection → Type Validation
                 ↓               ↓              ↓
         Parameter Binding → Tool Execution → Result Processing → Response
```

## 🛠️ Toolcategorieën & Patronen

### 1. **Dataverwerkingstools**
- **Inputvalidatie**: Sterke typificatie met data-annotaties
- **Transformatieoperaties**: Type-veilige dataconversie en -opmaak
- **Bedrijfslogica**: Domeinspecifieke berekening en analysetools
- **Outputopmaak**: Gestructureerde responsgeneratie

### 2. **Integratietools** 
- **API-Connectors**: RESTful service-integratie met HttpClient
- **Databasetools**: Entity Framework-integratie voor data-toegang
- **Bestandsbewerkingen**: Veilige bestandssysteemoperaties met validatie
- **Externe diensten**: Integratiepatronen voor diensten van derden

### 3. **Hulpprogramma's**
- **Tekstverwerking**: Hulpmiddelen voor stringmanipulatie en opmaak
- **Datum-/tijdoperaties**: Cultuurgevoelige berekeningen met datum/tijd
- **Wiskundige tools**: Nauwkeurige berekeningen en statistische operaties
- **Validatietools**: Validatie van bedrijfsregels en gegevensverificatie

## ⚙️ Vereisten & Setup

**Ontwikkelomgeving:**
- .NET 9.0 SDK of hoger
- Visual Studio 2022 of VS Code met C#-extensie
- Toegang tot GitHub Models API

**Vereiste NuGet-pakketten:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Omgevingsconfiguratie (.env-bestand):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

Klaar om agents op ondernemingsniveau te bouwen met krachtige, type-veilige toolmogelijkheden in .NET? Laten we professionele oplossingen ontwerpen! 🏢⚡

## 💻 Code-implementatie

De volledige C#-implementatie is beschikbaar in het bijbehorende bestand `04-dotnet-agent-framework.cs`. Deze .NET Single File App demonstreert:

- Het laden van omgevingsvariabelen voor GitHub Models-configuratie
- Het definiëren van aangepaste tools met behulp van C#-methoden en attributen
- Het creëren van een AI-agent met toolintegratie
- Het beheren van conversatiedraden
- Het uitvoeren van agentverzoeken met toolaanroepen

Om het voorbeeld uit te voeren:

```bash
chmod +x 04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

Of met behulp van de .NET CLI:

```bash
dotnet run 04-dotnet-agent-framework.cs
```

---

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.