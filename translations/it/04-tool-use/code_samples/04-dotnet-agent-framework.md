<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f82a3992438bcc028a2569c5fed828a9",
  "translation_date": "2025-11-07T09:24:18+00:00",
  "source_file": "04-tool-use/code_samples/04-dotnet-agent-framework.md",
  "language_code": "it"
}
-->
# 🛠️ Utilizzo Avanzato degli Strumenti con i Modelli GitHub (.NET)

## 📋 Obiettivi di Apprendimento

Questo notebook dimostra modelli di integrazione di strumenti di livello aziendale utilizzando il Microsoft Agent Framework in .NET con i Modelli GitHub. Imparerai a costruire agenti sofisticati con strumenti specializzati multipli, sfruttando il forte typing di C# e le funzionalità aziendali di .NET.

**Capacità Avanzate degli Strumenti che Apprenderai:**
- 🔧 **Architettura Multi-Strumento**: Creazione di agenti con capacità specializzate multiple
- 🎯 **Esecuzione di Strumenti Type-Safe**: Sfruttare la validazione a tempo di compilazione di C#
- 📊 **Modelli di Strumenti Aziendali**: Progettazione di strumenti pronti per la produzione e gestione degli errori
- 🔗 **Composizione degli Strumenti**: Combinare strumenti per flussi di lavoro aziendali complessi

## 🎯 Vantaggi dell'Architettura degli Strumenti .NET

### Caratteristiche degli Strumenti Aziendali
- **Validazione a Tempo di Compilazione**: Il forte typing garantisce la correttezza dei parametri degli strumenti
- **Iniezione delle Dipendenze**: Integrazione del contenitore IoC per la gestione degli strumenti
- **Pattern Async/Await**: Esecuzione non bloccante degli strumenti con gestione adeguata delle risorse
- **Logging Strutturato**: Integrazione del logging per il monitoraggio dell'esecuzione degli strumenti

### Modelli Pronti per la Produzione
- **Gestione delle Eccezioni**: Gestione completa degli errori con eccezioni tipizzate
- **Gestione delle Risorse**: Pattern di smaltimento adeguato e gestione della memoria
- **Monitoraggio delle Prestazioni**: Metriche integrate e contatori di prestazioni
- **Gestione della Configurazione**: Configurazione type-safe con validazione

## 🔧 Architettura Tecnica

### Componenti Principali degli Strumenti .NET
- **Microsoft.Extensions.AI**: Livello di astrazione unificato per gli strumenti
- **Microsoft.Agents.AI**: Orchestrazione di strumenti di livello aziendale
- **Integrazione Modelli GitHub**: Client API ad alte prestazioni con pooling delle connessioni

### Pipeline di Esecuzione degli Strumenti
```
User Request → Agent Analysis → Tool Selection → Type Validation
                 ↓               ↓              ↓
         Parameter Binding → Tool Execution → Result Processing → Response
```

## 🛠️ Categorie e Modelli di Strumenti

### 1. **Strumenti di Elaborazione Dati**
- **Validazione Input**: Forte typing con annotazioni dei dati
- **Operazioni di Trasformazione**: Conversione e formattazione dei dati type-safe
- **Logica Aziendale**: Strumenti di calcolo e analisi specifici del dominio
- **Formattazione Output**: Generazione di risposte strutturate

### 2. **Strumenti di Integrazione**
- **Connettori API**: Integrazione di servizi RESTful con HttpClient
- **Strumenti Database**: Integrazione di Entity Framework per l'accesso ai dati
- **Operazioni su File**: Operazioni sicure sul file system con validazione
- **Servizi Esterni**: Modelli di integrazione di servizi di terze parti

### 3. **Strumenti Utilitari**
- **Elaborazione Testo**: Utilità di manipolazione e formattazione delle stringhe
- **Operazioni Data/Ora**: Calcoli data/ora sensibili alla cultura
- **Strumenti Matematici**: Calcoli di precisione e operazioni statistiche
- **Strumenti di Validazione**: Validazione delle regole aziendali e verifica dei dati

## ⚙️ Prerequisiti e Configurazione

**Ambiente di Sviluppo:**
- SDK .NET 9.0 o superiore
- Visual Studio 2022 o VS Code con estensione C#
- Accesso all'API Modelli GitHub

**Pacchetti NuGet Richiesti:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Microsoft.Extensions.AI.OpenAI" Version="9.9.0-preview.1.25458.4" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Configurazione Ambiente (.env file):**
```env
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_ENDPOINT=https://models.inference.ai.azure.com
GITHUB_MODEL_ID=gpt-4o-mini
```

Pronto a costruire agenti di livello aziendale con potenti capacità di strumenti type-safe in .NET? Progettiamo soluzioni professionali! 🏢⚡

## 💻 Implementazione del Codice

L'implementazione completa in C# è disponibile nel file di accompagnamento `04-dotnet-agent-framework.cs`. Questa App Singola .NET dimostra:

- Caricamento delle variabili di ambiente per la configurazione dei Modelli GitHub
- Definizione di strumenti personalizzati utilizzando metodi C# con attributi
- Creazione di un agente AI con integrazione degli strumenti
- Gestione dei thread di conversazione
- Esecuzione delle richieste dell'agente con invocazione degli strumenti

Per eseguire l'esempio:

```bash
chmod +x 04-dotnet-agent-framework.cs
./04-dotnet-agent-framework.cs
```

Oppure utilizzando la CLI .NET:

```bash
dotnet run 04-dotnet-agent-framework.cs
```

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.