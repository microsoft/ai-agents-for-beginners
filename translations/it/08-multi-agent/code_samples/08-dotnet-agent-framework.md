<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5f5a5f2902f32272257506d88d3c43a1",
  "translation_date": "2025-11-07T09:15:55+00:00",
  "source_file": "08-multi-agent/code_samples/08-dotnet-agent-framework.md",
  "language_code": "it"
}
-->
# 🤝 Sistemi di Workflow Multi-Agente per Imprese (.NET)

## 📋 Obiettivi di Apprendimento

Questo notebook dimostra come costruire sistemi multi-agente sofisticati di livello aziendale utilizzando il Microsoft Agent Framework in .NET con i modelli di GitHub. Imparerai a orchestrare più agenti specializzati che lavorano insieme attraverso workflow strutturati, sfruttando le funzionalità aziendali di .NET per soluzioni pronte per la produzione.

**Capacità Multi-Agente per Imprese che Imparerai a Costruire:**
- 👥 **Collaborazione tra Agenti**: Coordinazione tra agenti con validazione a tempo di compilazione
- 🔄 **Orchestrazione del Workflow**: Definizione dichiarativa del workflow con i pattern asincroni di .NET
- 🎭 **Specializzazione dei Ruoli**: Personalità degli agenti fortemente tipizzate e domini di competenza
- 🏢 **Integrazione Aziendale**: Pattern pronti per la produzione con monitoraggio e gestione degli errori

## ⚙️ Prerequisiti e Configurazione

**Ambiente di Sviluppo:**
- SDK .NET 9.0 o superiore
- Visual Studio 2022 o VS Code con estensione C#
- Abbonamento Azure (per agenti persistenti)

**Pacchetti NuGet Necessari:**
```xml
<PackageReference Include="Microsoft.Extensions.AI.Abstractions" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.4" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="Microsoft.Extensions.AI" Version="9.8.0" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
```

## Esempio di Codice

Il codice completo funzionante per questa lezione è disponibile nel file C# allegato: [`08-dotnet-agent-framework.cs`](../../../../08-multi-agent/code_samples/08-dotnet-agent-framework.cs)

Per eseguire l'esempio:

```bash
# Make the file executable (Linux/macOS)
chmod +x 08-dotnet-agent-framework.cs

# Run the sample
./08-dotnet-agent-framework.cs
```

Oppure utilizzando la CLI di .NET:

```bash
dotnet run 08-dotnet-agent-framework.cs
```

## Cosa Dimostra Questo Esempio

Questo sistema di workflow multi-agente crea un servizio di raccomandazione per viaggi in hotel con due agenti specializzati:

1. **Agente FrontDesk**: Un agente di viaggio che fornisce raccomandazioni su attività e luoghi
2. **Agente Concierge**: Rivede le raccomandazioni per garantire esperienze autentiche e non turistiche

Gli agenti lavorano insieme in un workflow dove:
- L'agente FrontDesk riceve la richiesta iniziale di viaggio
- L'agente Concierge rivede e perfeziona la raccomandazione
- Il workflow trasmette le risposte in tempo reale

## Concetti Chiave

### Coordinazione tra Agenti
L'esempio dimostra la coordinazione tra agenti con validazione a tempo di compilazione utilizzando il Microsoft Agent Framework.

### Orchestrazione del Workflow
Utilizza la definizione dichiarativa del workflow con i pattern asincroni di .NET per connettere più agenti in una pipeline.

### Risposte in Streaming
Implementa lo streaming in tempo reale delle risposte degli agenti utilizzando enumerabili asincroni e un'architettura basata su eventi.

### Integrazione Aziendale
Mostra pattern pronti per la produzione, tra cui:
- Configurazione tramite variabili d'ambiente
- Gestione sicura delle credenziali
- Gestione degli errori
- Elaborazione asincrona degli eventi

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche potrebbero contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.