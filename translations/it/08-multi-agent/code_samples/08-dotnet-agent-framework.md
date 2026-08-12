# 🤝 Sistemi Enterprise Multi-Agente per Flussi di Lavoro (.NET)

## 📋 Obiettivi di Apprendimento

Questo notebook dimostra come costruire sistemi multi-agente sofisticati di livello enterprise utilizzando il Microsoft Agent Framework in .NET con Azure OpenAI (Responses API). Imparerai a orchestrare più agenti specializzati che lavorano insieme attraverso flussi di lavoro strutturati, sfruttando le funzionalità enterprise di .NET per soluzioni pronte per la produzione.

**Capacità Multi-Agente Enterprise che Costruirai:**
- 👥 **Collaborazione tra Agenti**: Coordinazione di agenti con tipizzazione sicura e validazione a compile-time
- 🔄 **Orchestrazione del Flusso di Lavoro**: Definizione dichiarativa di flussi di lavoro con i pattern async di .NET
- 🎭 **Specializzazione del Ruolo**: Personalità di agenti fortemente tipizzate e domini di competenza
- 🏢 **Integrazione Enterprise**: Pattern pronti per la produzione con monitoraggio e gestione degli errori

## ⚙️ Prerequisiti e Configurazione

**Ambiente di Sviluppo:**
- .NET 9.0 SDK o superiore
- Visual Studio 2022 o VS Code con estensione C#
- Sottoscrizione Azure (per agenti persistenti)

**Pacchetti NuGet Richiesti:**
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

## Esempio di Codice

Il codice completo funzionante per questa lezione è disponibile nel file C# allegato: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Per eseguire l’esempio:

```bash
# Rendi il file eseguibile (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Esegui l'esempio
./08-dotnet-agent-framework.cs
```

Oppure usando la CLI di .NET:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Cosa Dimostra Questo Esempio

Questo sistema multi-agente per flussi di lavoro crea un servizio di raccomandazioni per viaggi in hotel con due agenti specializzati:

1. **Agente FrontDesk**: Un agente di viaggio che fornisce raccomandazioni su attività e luoghi
2. **Agente Concierge**: Rivede le raccomandazioni per garantire esperienze autentiche e non turistiche

Gli agenti collaborano in un flusso di lavoro dove:
- L’agente FrontDesk riceve la richiesta di viaggio iniziale
- L’agente Concierge revisiona e affina la raccomandazione
- Il flusso di lavoro trasmette le risposte in tempo reale

## Concetti Chiave

### Coordinamento degli Agenti
L’esempio dimostra il coordinamento di agenti con tipizzazione sicura utilizzando il Microsoft Agent Framework con validazione a compile-time.

### Orchestrazione del Flusso di Lavoro
Utilizza una definizione dichiarativa del flusso di lavoro con i pattern async di .NET per collegare più agenti in una pipeline.

### Risposte in Streaming
Implementa lo streaming in tempo reale delle risposte degli agenti utilizzando enumerabili async e architettura event-driven.

### Integrazione Enterprise
Mostra pattern pronti per la produzione inclusi:
- Configurazione tramite variabili d’ambiente
- Gestione sicura delle credenziali
- Gestione degli errori
- Elaborazione asincrona degli eventi

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->