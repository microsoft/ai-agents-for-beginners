<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c8bc231a26e949f525d65b716538707f",
  "translation_date": "2025-11-07T09:46:45+00:00",
  "source_file": "03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.md",
  "language_code": "it"
}
-->
# 🎨 Modelli di Design Agentici con GitHub Models (.NET)

## 📋 Obiettivi di Apprendimento

Questo notebook illustra modelli di design di livello aziendale per la creazione di agenti intelligenti utilizzando il Microsoft Agent Framework in .NET con l'integrazione di GitHub Models. Imparerai modelli professionali e approcci architetturali che rendono gli agenti pronti per la produzione, manutenibili e scalabili.

**Modelli di Design Aziendali:**
- 🏭 **Factory Pattern**: Creazione standardizzata di agenti con dependency injection
- 🔧 **Builder Pattern**: Configurazione e impostazione fluente degli agenti
- 🧵 **Thread-Safe Patterns**: Gestione concorrente delle conversazioni
- 📋 **Repository Pattern**: Gestione organizzata degli strumenti e delle capacità

## 🎯 Benefici Architetturali Specifici di .NET

### Funzionalità Aziendali
- **Tipizzazione Forte**: Validazione durante la compilazione e supporto IntelliSense
- **Dependency Injection**: Integrazione con il contenitore DI integrato
- **Gestione della Configurazione**: Modelli IConfiguration e Options
- **Async/Await**: Supporto di prima classe per la programmazione asincrona

### Modelli Pronti per la Produzione
- **Integrazione del Logging**: Supporto ILogger e logging strutturato
- **Controlli di Salute**: Monitoraggio e diagnostica integrati
- **Validazione della Configurazione**: Tipizzazione forte con annotazioni dei dati
- **Gestione degli Errori**: Gestione strutturata delle eccezioni

## 🔧 Architettura Tecnica

### Componenti Core di .NET
- **Microsoft.Extensions.AI**: Astrazioni unificate per i servizi AI
- **Microsoft.Agents.AI**: Framework di orchestrazione degli agenti aziendali
- **Integrazione GitHub Models**: Modelli di client API ad alte prestazioni
- **Sistema di Configurazione**: Integrazione di appsettings.json e ambiente

### Implementazione dei Modelli di Design
```csharp
IServiceCollection → Agent Builder → Configuration → Tool Registry → AI Agent
```

## 🏗️ Modelli Aziendali Dimostrati

### 1. **Modelli Creazionali**
- **Agent Factory**: Creazione centralizzata di agenti con configurazione coerente
- **Builder Pattern**: API fluente per configurazioni complesse di agenti
- **Singleton Pattern**: Gestione delle risorse condivise e della configurazione
- **Dependency Injection**: Accoppiamento debole e testabilità

### 2. **Modelli Comportamentali**
- **Strategy Pattern**: Strategie intercambiabili per l'esecuzione degli strumenti
- **Command Pattern**: Operazioni degli agenti incapsulate con undo/redo
- **Observer Pattern**: Gestione del ciclo di vita degli agenti basata su eventi
- **Template Method**: Flussi di lavoro standardizzati per l'esecuzione degli agenti

### 3. **Modelli Strutturali**
- **Adapter Pattern**: Livello di integrazione API GitHub Models
- **Decorator Pattern**: Potenziamento delle capacità degli agenti
- **Facade Pattern**: Interfacce semplificate per l'interazione con gli agenti
- **Proxy Pattern**: Lazy loading e caching per migliorare le prestazioni

## ⚙️ Prerequisiti e Configurazione

**Ambiente di Sviluppo:**
- .NET 9.0 SDK o superiore
- Visual Studio 2022 o VS Code con estensione C#
- Accesso all'API GitHub Models

**Dipendenze NuGet:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Configurazione (file .env):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

## 📚 Principi di Design .NET

### Principi SOLID
- **Single Responsibility**: Ogni componente ha uno scopo chiaro
- **Open/Closed**: Estensibile senza modifiche
- **Sostituzione di Liskov**: Implementazioni degli strumenti basate su interfacce
- **Segregazione delle Interfacce**: Interfacce mirate e coese
- **Inversione delle Dipendenze**: Dipendenza da astrazioni, non da implementazioni concrete

### Architettura Pulita
- **Livello Dominio**: Astrazioni principali per agenti e strumenti
- **Livello Applicazione**: Orchestrazione degli agenti e flussi di lavoro
- **Livello Infrastruttura**: Integrazione GitHub Models e servizi esterni
- **Livello Presentazione**: Interazione con l'utente e formattazione delle risposte

## 🔒 Considerazioni Aziendali

### Sicurezza
- **Gestione delle Credenziali**: Gestione sicura delle chiavi API con IConfiguration
- **Validazione dell'Input**: Tipizzazione forte e validazione con annotazioni dei dati
- **Sanificazione dell'Output**: Elaborazione e filtraggio sicuro delle risposte
- **Audit Logging**: Tracciamento completo delle operazioni

### Prestazioni
- **Modelli Asincroni**: Operazioni I/O non bloccanti
- **Pooling delle Connessioni**: Gestione efficiente dei client HTTP
- **Caching**: Caching delle risposte per migliorare le prestazioni
- **Gestione delle Risorse**: Modelli di smaltimento e pulizia corretti

### Scalabilità
- **Sicurezza dei Thread**: Supporto per l'esecuzione concorrente degli agenti
- **Pooling delle Risorse**: Utilizzo efficiente delle risorse
- **Gestione del Carico**: Limitazione della velocità e gestione della pressione
- **Monitoraggio**: Metriche di prestazioni e controlli di salute

## 🚀 Distribuzione in Produzione

- **Gestione della Configurazione**: Impostazioni specifiche per l'ambiente
- **Strategia di Logging**: Logging strutturato con ID di correlazione
- **Gestione degli Errori**: Gestione globale delle eccezioni con recupero adeguato
- **Monitoraggio**: Application Insights e contatori di prestazioni
- **Testing**: Modelli di test unitari, di integrazione e di carico

Pronto a costruire agenti intelligenti di livello aziendale con .NET? Progettiamo qualcosa di robusto! 🏢✨

## Esempio di Codice

Per un esempio completo funzionante, vedi [03-dotnet-agent-framework.cs](../../../../03-agentic-design-patterns/code_samples/03-dotnet-agent-framework.cs).

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.