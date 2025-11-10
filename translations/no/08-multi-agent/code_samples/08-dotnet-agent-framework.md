<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f5a5f2902f32272257506d88d3c43a1",
  "translation_date": "2025-11-07T09:16:58+00:00",
  "source_file": "08-multi-agent/code_samples/08-dotnet-agent-framework.md",
  "language_code": "no"
}
-->
# 🤝 Enterprise Multi-Agent Workflow Systems (.NET)

## 📋 Læringsmål

Denne notatboken viser hvordan man bygger sofistikerte, bedriftsklare multi-agent systemer ved hjelp av Microsoft Agent Framework i .NET med GitHub-modeller. Du vil lære å orkestrere flere spesialiserte agenter som samarbeider gjennom strukturerte arbeidsflyter, og utnytte .NETs funksjoner for produksjonsklare løsninger.

**Bedriftsfunksjoner for multi-agent systemer du vil bygge:**
- 👥 **Agent-samarbeid**: Type-sikker koordinering av agenter med validering ved kompilering
- 🔄 **Arbeidsflytorkestrering**: Deklarativ definisjon av arbeidsflyt med .NETs asynkrone mønstre
- 🎭 **Rolle-spesialisering**: Sterkt typede agentpersonligheter og ekspertiseområder
- 🏢 **Bedriftsintegrasjon**: Produksjonsklare mønstre med overvåking og feilhåndtering

## ⚙️ Forutsetninger og oppsett

**Utviklingsmiljø:**
- .NET 9.0 SDK eller nyere
- Visual Studio 2022 eller VS Code med C#-utvidelse
- Azure-abonnement (for vedvarende agenter)

**Nødvendige NuGet-pakker:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.4" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="9.8.0" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
```

## Eksempelkode

Den komplette fungerende koden for denne leksjonen er tilgjengelig i den medfølgende C#-filen: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

For å kjøre eksempelet:

```bash
# Make the file executable (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Run the sample
./08-dotnet-agent-framework.cs
```

Eller ved bruk av .NET CLI:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Hva dette eksempelet demonstrerer

Dette multi-agent arbeidsflytsystemet skaper en hotellreiseanbefalingstjeneste med to spesialiserte agenter:

1. **FrontDesk Agent**: En reiseagent som gir anbefalinger for aktiviteter og steder
2. **Concierge Agent**: Gjennomgår anbefalingene for å sikre autentiske, ikke-turistiske opplevelser

Agentene samarbeider i en arbeidsflyt hvor:
- FrontDesk-agenten mottar den innledende reiseforespørselen
- Concierge-agenten gjennomgår og forbedrer anbefalingen
- Arbeidsflyten strømmer svar i sanntid

## Nøkkelkonsepter

### Agent-samarbeid
Eksempelet demonstrerer type-sikker koordinering av agenter ved bruk av Microsoft Agent Framework med validering ved kompilering.

### Arbeidsflytorkestrering
Bruker deklarativ definisjon av arbeidsflyt med .NETs asynkrone mønstre for å koble flere agenter i en pipeline.

### Strømming av svar
Implementerer sanntidsstrømming av agenters svar ved bruk av asynkrone enumerables og hendelsesdrevet arkitektur.

### Bedriftsintegrasjon
Viser produksjonsklare mønstre inkludert:
- Konfigurasjon av miljøvariabler
- Sikker håndtering av legitimasjon
- Feilhåndtering
- Asynkron hendelsesbehandling

---

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.