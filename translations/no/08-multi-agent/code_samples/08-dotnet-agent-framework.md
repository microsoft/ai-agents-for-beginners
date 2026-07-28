# 🤝 Foretaks Multi-Agent Arbeidsflytsystemer (.NET)

## 📋 Læringsmål

Denne notatboken demonstrerer hvordan man bygger sofistikerte fleragent-systemer i bedriftsklasse ved hjelp av Microsoft Agent Framework i .NET med Azure OpenAI (Responses API). Du vil lære å orkestrere flere spesialiserte agenter som jobber sammen gjennom strukturerte arbeidsflyter, og utnytte .NETs bedriftsfunksjoner for produksjonsklare løsninger.

**Multi-agent kapasiteter for bedriftsbruk du vil bygge:**
- 👥 **Agent-samarbeid**: Typesikker agentkoordinering med kompileringstid-validering
- 🔄 **Arbeidsflyt-orkestrering**: Deklarativ arbeidsflytdefinisjon med .NETs asynkrone mønstre
- 🎭 **Rolle-spesialisering**: Sterkt typede agent-personligheter og ekspertisedomener
- 🏢 **Foretaksintegrasjon**: Produksjonsklare mønstre med overvåking og feilhåndtering

## ⚙️ Forutsetninger og oppsett

**Utviklingsmiljø:**
- .NET 9.0 SDK eller nyere
- Visual Studio 2022 eller VS Code med C#-utvidelse
- Azure-abonnement (for vedvarende agenter)

**Nødvendige NuGet-pakker:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="10.*" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.10" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="10.*" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="10.*" />
<PackageReference Include="OpenTelemetry.Api" Version="1.*" />
<PackageReference Include="Microsoft.Agents.AI.Workflows" Version="1.*" />
<PackageReference Include="Microsoft.Agents.AI.OpenAI" Version="1.*-*" />
```

## Eksempelkode

Den komplette fungerende koden for denne leksjonen er tilgjengelig i den medfølgende C#-filen: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

For å kjøre eksemplet:

```bash
# Gjør filen kjørbar (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Kjør eksempelet
./08-dotnet-agent-framework.cs
```

Eller bruke .NET CLI:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Hva dette eksemplet demonstrerer

Dette fleragentarbeidsflytsystemet lager en hotellreiseanbefalingstjeneste med to spesialiserte agenter:

1. **FrontDesk Agent**: En reiseagent som gir anbefalinger om aktiviteter og steder
2. **Concierge Agent**: Gjennomgår anbefalingene for å sikre autentiske, ikke-turistifiserte opplevelser

Agentene jobber sammen i en arbeidsflyt der:
- FrontDesk-agenten mottar den innledende reiseforespørselen
- Concierge-agenten gjennomgår og finjusterer anbefalingen
- Arbeidsflyten streamer svarene i sanntid

## Nøkkelkonsepter

### Agentkoordinering
Eksemplet demonstrerer typesikker agentkoordinering ved bruk av Microsoft Agent Framework med kompileringstid-validering.

### Arbeidsflytorkestrering
Bruker deklarativ arbeidsflytdefinisjon med .NETs asynkrone mønstre for å koble flere agenter i en pipe.

### Streaming av svar
Implementerer sanntidsstreaming av agentsvar ved bruk av asynkrone enumerabler og hendelsesdrevet arkitektur.

### Foretaksintegrasjon
Viser produksjonsklare mønstre inkludert:
- Konfigurasjon via miljøvariabler
- Sikker administrasjon av legitimasjon
- Feilhåndtering
- Asynkron hendelsesbehandling

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->