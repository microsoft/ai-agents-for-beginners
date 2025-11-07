<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c268705e6fb2b30c7690d5b2a002e072",
  "translation_date": "2025-11-07T09:02:05+00:00",
  "source_file": "05-agentic-rag/code_samples/05-dotnet-agent-framework.md",
  "language_code": "it"
}
-->
# 🔍 Enterprise RAG con Azure AI Foundry (.NET)

## 📋 Obiettivi di Apprendimento

Questo notebook dimostra come costruire sistemi Retrieval-Augmented Generation (RAG) di livello enterprise utilizzando il Microsoft Agent Framework in .NET con Azure AI Foundry. Imparerai a creare agenti pronti per la produzione che possono cercare tra i documenti e fornire risposte accurate e contestualizzate con sicurezza e scalabilità aziendale.

**Funzionalità RAG Enterprise che costruirai:**
- 📚 **Intelligenza Documentale**: Elaborazione avanzata dei documenti con i servizi Azure AI
- 🔍 **Ricerca Semantica**: Ricerca vettoriale ad alte prestazioni con funzionalità aziendali
- 🛡️ **Integrazione della Sicurezza**: Accesso basato sui ruoli e modelli di protezione dei dati
- 🏢 **Architettura Scalabile**: Sistemi RAG pronti per la produzione con monitoraggio

## 🎯 Architettura RAG Enterprise

### Componenti Core Enterprise
- **Azure AI Foundry**: Piattaforma AI gestita per l'azienda con sicurezza e conformità
- **Agenti Persistenti**: Agenti con stato persistente e gestione della cronologia delle conversazioni
- **Gestione del Vector Store**: Indicizzazione e recupero di documenti di livello enterprise
- **Integrazione Identità**: Autenticazione Azure AD e controllo degli accessi basato sui ruoli

### Vantaggi di .NET per l'Enterprise
- **Sicurezza dei Tipi**: Validazione a tempo di compilazione per operazioni RAG e strutture dati
- **Prestazioni Asincrone**: Elaborazione e operazioni di ricerca non bloccanti
- **Gestione della Memoria**: Utilizzo efficiente delle risorse per collezioni di documenti di grandi dimensioni
- **Pattern di Integrazione**: Integrazione nativa dei servizi Azure con dependency injection

## 🏗️ Architettura Tecnica

### Pipeline RAG Enterprise
```
Document Upload → Security Validation → Vector Processing → Index Creation
                      ↓                    ↓                  ↓
User Query → Authentication → Semantic Search → Context Ranking → AI Response
```

### Componenti Core .NET
- **Azure.AI.Agents.Persistent**: Gestione degli agenti enterprise con persistenza dello stato
- **Azure.Identity**: Autenticazione integrata per accesso sicuro ai servizi Azure
- **Microsoft.Agents.AI.AzureAI**: Implementazione del framework per agenti ottimizzato per Azure
- **System.Linq.Async**: Operazioni LINQ asincrone ad alte prestazioni

## 🔧 Funzionalità e Vantaggi Enterprise

### Sicurezza e Conformità
- **Integrazione Azure AD**: Gestione dell'identità aziendale e autenticazione
- **Accesso Basato sui Ruoli**: Permessi granulari per accesso e operazioni sui documenti
- **Protezione dei Dati**: Crittografia a riposo e in transito per documenti sensibili
- **Registrazione delle Attività**: Tracciamento completo delle attività per requisiti di conformità

### Prestazioni e Scalabilità
- **Pooling delle Connessioni**: Gestione efficiente delle connessioni ai servizi Azure
- **Elaborazione Asincrona**: Operazioni non bloccanti per scenari ad alta capacità
- **Strategie di Caching**: Caching intelligente per documenti frequentemente accessibili
- **Bilanciamento del Carico**: Elaborazione distribuita per implementazioni su larga scala

### Gestione e Monitoraggio
- **Controlli di Salute**: Monitoraggio integrato per i componenti del sistema RAG
- **Metriche di Prestazione**: Analisi dettagliata sulla qualità della ricerca e sui tempi di risposta
- **Gestione degli Errori**: Gestione completa delle eccezioni con politiche di retry
- **Gestione della Configurazione**: Impostazioni specifiche per l'ambiente con validazione

## ⚙️ Prerequisiti e Configurazione

**Ambiente di Sviluppo:**
- SDK .NET 9.0 o superiore
- Visual Studio 2022 o VS Code con estensione C#
- Abbonamento Azure con accesso a AI Foundry

**Pacchetti NuGet Richiesti:**
```xml
<PackageReference Include="Microsoft.Extensions.AI" Version="9.9.0" />
<PackageReference Include="Azure.AI.Agents.Persistent" Version="1.2.0-beta.5" />
<PackageReference Include="Azure.Identity" Version="1.15.0" />
<PackageReference Include="System.Linq.Async" Version="6.0.3" />
<PackageReference Include="DotNetEnv" Version="3.1.1" />
```

**Configurazione Autenticazione Azure:**
```bash
# Install Azure CLI and authenticate
az login
az account set --subscription "your-subscription-id"
```

**Configurazione dell'Ambiente:**
* Configurazione di Azure AI Foundry (gestita automaticamente tramite Azure CLI)
* Assicurati di essere autenticato all'abbonamento Azure corretto

## 📊 Pattern RAG Enterprise

### Pattern di Gestione dei Documenti
- **Caricamento Massivo**: Elaborazione efficiente di collezioni di documenti di grandi dimensioni
- **Aggiornamenti Incrementali**: Aggiunta e modifica dei documenti in tempo reale
- **Controllo delle Versioni**: Versionamento dei documenti e tracciamento delle modifiche
- **Gestione dei Metadati**: Attributi ricchi dei documenti e tassonomia

### Pattern di Ricerca e Recupero
- **Ricerca Ibrida**: Combinazione di ricerca semantica e per parole chiave per risultati ottimali
- **Ricerca Facetata**: Filtraggio e categorizzazione multidimensionale
- **Ottimizzazione della Rilevanza**: Algoritmi di scoring personalizzati per esigenze specifiche del dominio
- **Classifica dei Risultati**: Classificazione avanzata con integrazione della logica aziendale

### Pattern di Sicurezza
- **Sicurezza a Livello di Documento**: Controllo degli accessi granulare per documento
- **Classificazione dei Dati**: Etichettatura automatica della sensibilità e protezione
- **Tracciabilità delle Operazioni**: Registrazione completa di tutte le operazioni RAG
- **Protezione della Privacy**: Rilevamento e redazione di PII

## 🔒 Funzionalità di Sicurezza Enterprise

### Autenticazione e Autorizzazione
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

### Protezione dei Dati
- **Crittografia**: Crittografia end-to-end per documenti e indici di ricerca
- **Controlli di Accesso**: Integrazione con Azure AD per permessi utente e di gruppo
- **Residenza dei Dati**: Controlli sulla posizione geografica dei dati per conformità
- **Backup e Ripristino**: Backup automatico e capacità di recupero in caso di disastro

## 📈 Ottimizzazione delle Prestazioni

### Pattern di Elaborazione Asincrona
```csharp
// Efficient async document processing
await foreach (var document in documentStream.AsAsyncEnumerable())
{
    await ProcessDocumentAsync(document, cancellationToken);
}
```

### Gestione della Memoria
- **Elaborazione in Streaming**: Gestione di documenti di grandi dimensioni senza problemi di memoria
- **Pooling delle Risorse**: Riutilizzo efficiente delle risorse costose
- **Garbage Collection**: Pattern ottimizzati di allocazione della memoria
- **Gestione delle Connessioni**: Ciclo di vita corretto delle connessioni ai servizi Azure

### Strategie di Caching
- **Caching delle Query**: Cache per ricerche eseguite frequentemente
- **Caching dei Documenti**: Cache in memoria per documenti "caldi"
- **Caching degli Indici**: Ottimizzazione del caching degli indici vettoriali
- **Caching dei Risultati**: Cache intelligente delle risposte generate

## 📊 Casi d'Uso Enterprise

### Gestione della Conoscenza
- **Wiki Aziendale**: Ricerca intelligente tra le basi di conoscenza aziendali
- **Politiche e Procedure**: Guida automatizzata per conformità e procedure
- **Materiali di Formazione**: Assistenza intelligente per apprendimento e sviluppo
- **Database di Ricerca**: Sistemi di analisi di articoli accademici e di ricerca

### Supporto Clienti
- **Base di Conoscenza per il Supporto**: Risposte automatizzate per il servizio clienti
- **Documentazione di Prodotto**: Recupero intelligente di informazioni sui prodotti
- **Guide di Risoluzione Problemi**: Assistenza contestuale per la risoluzione dei problemi
- **Sistemi FAQ**: Generazione dinamica di FAQ da collezioni di documenti

### Conformità Normativa
- **Analisi dei Documenti Legali**: Intelligenza per contratti e documenti legali
- **Monitoraggio della Conformità**: Verifica automatizzata della conformità normativa
- **Valutazione del Rischio**: Analisi e reportistica dei rischi basati sui documenti
- **Supporto per Audit**: Scoperta intelligente di documenti per audit

## 🚀 Distribuzione in Produzione

### Monitoraggio e Osservabilità
- **Application Insights**: Telemetria dettagliata e monitoraggio delle prestazioni
- **Metriche Personalizzate**: Tracciamento e avvisi KPI specifici per il business
- **Tracciamento Distribuito**: Tracciamento end-to-end delle richieste tra i servizi
- **Dashboard di Salute**: Visualizzazione in tempo reale della salute e delle prestazioni del sistema

### Scalabilità e Affidabilità
- **Auto-Scaling**: Scalabilità automatica basata su carico e metriche di prestazione
- **Alta Disponibilità**: Distribuzione multi-regione con capacità di failover
- **Test di Carico**: Validazione delle prestazioni sotto carico aziendale
- **Recupero da Disastri**: Procedure automatizzate di backup e recupero

Pronto a costruire sistemi RAG di livello enterprise in grado di gestire documenti sensibili su larga scala? Progettiamo sistemi di conoscenza intelligenti per l'azienda! 🏢📖✨

## Implementazione del Codice

Il codice completo funzionante per questa lezione è disponibile in `05-dotnet-agent-framework.cs`. 

Per eseguire l'esempio:

```bash
# Make the script executable (Linux/macOS)
chmod +x 05-dotnet-agent-framework.cs

# Run the .NET Single File App
./05-dotnet-agent-framework.cs
```

Oppure usa direttamente `dotnet run`:

```bash
dotnet run 05-dotnet-agent-framework.cs
```

Il codice dimostra:

1. **Installazione dei Pacchetti**: Installazione dei pacchetti NuGet richiesti per Azure AI Agents
2. **Configurazione dell'Ambiente**: Caricamento delle impostazioni dell'endpoint e del modello di Azure AI Foundry
3. **Caricamento dei Documenti**: Caricamento di un documento per l'elaborazione RAG
4. **Creazione del Vector Store**: Creazione di un vector store per la ricerca semantica
5. **Configurazione dell'Agente**: Configurazione di un agente AI con capacità di ricerca nei file
6. **Esecuzione delle Query**: Esecuzione di query sui documenti caricati

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche potrebbero contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.