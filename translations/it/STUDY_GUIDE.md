# Agenti AI per Principianti - Guida di Studio e Riassunto del Corso

Questa guida fornisce un riassunto del corso "Agenti AI per Principianti" e spiega i concetti chiave, i framework e i modelli di progettazione per costruire Agenti AI.

## 1. Introduzione agli Agenti AI

**Cosa sono gli Agenti AI?**  
Gli Agenti AI sono sistemi che estendono le capacità dei Modelli di Linguaggio di Grandi Dimensioni (LLM) dando loro accesso a **strumenti**, **conoscenza** e **memoria**. Diversamente da un chatbot standard basato su LLM che genera solo testo in base ai dati di addestramento, un Agente AI può:  
- **Percepire** il proprio ambiente (tramite sensori o input).  
- **Ragionare** su come risolvere un problema.  
- **Agire** per modificare l’ambiente (tramite attuatori o esecuzione di strumenti).

**Componenti chiave di un Agente:**  
- **Ambiente**: Lo spazio in cui l'agente opera (es. un sistema di prenotazione).  
- **Sensori**: Meccanismi per raccogliere informazioni (es. leggere un’API).  
- **Attuatori**: Meccanismi per compiere azioni (es. inviare un’email).  
- **Cervello (LLM)**: Il motore di ragionamento che pianifica e decide quali azioni intraprendere.

## 2. Framework Agentici

Il corso utilizza **Microsoft Agent Framework (MAF)** con **Azure AI Foundry Agent Service V2** per costruire agenti:

| Componente | Focus | Ideale per |
|------------|-------|-----------|
| **Microsoft Agent Framework** | SDK unificato Python/C# per agenti, strumenti e flussi di lavoro | Costruire agenti con strumenti, flussi multi-agente e modelli di produzione. |
| **Azure AI Foundry Agent Service** | Runtime cloud gestito | Distribuzione sicura e scalabile con gestione dello stato integrata, osservabilità e affidabilità. |

## 3. Modelli di Progettazione Agentici

I modelli di progettazione aiutano a strutturare il modo in cui gli agenti operano per risolvere problemi in modo affidabile.

### **Modello di Uso degli Strumenti** (Lezione 4)  
Questo modello consente agli agenti di interagire con il mondo esterno.  
- **Concetto**: All’agente viene fornito uno "schema" (un elenco di funzioni disponibili e i loro parametri). Il LLM decide *quale* strumento chiamare e *con quali* argomenti basandosi sulla richiesta dell’utente.  
- **Flusso**: Richiesta Utente -> LLM -> **Selezione dello Strumento** -> **Esecuzione dello Strumento** -> LLM (con output dello strumento) -> Risposta Finale.  
- **Casi d’uso**: Recupero dati in tempo reale (tempo, prezzi azionari), esecuzione di calcoli, esecuzione di codice.

### **Modello di Pianificazione** (Lezione 7)  
Questo modello permette agli agenti di risolvere compiti complessi e articolati in più fasi.  
- **Concetto**: L’agente scompone un obiettivo di alto livello in una sequenza di sotto-compiti più piccoli.  
- **Approcci**:  
  - **Decomposizione del compito**: suddividere "Pianifica un viaggio" in "Prenota volo", "Prenota hotel", "Noleggia auto".  
  - **Pianificazione iterativa**: rivalutare il piano in base ai risultati delle fasi precedenti (es. se il volo è pieno, scegliere una data diversa).  
- **Implementazione**: Spesso coinvolge un agente "Pianificatore" che genera un piano strutturato (es. JSON) eseguito poi da altri agenti.

## 4. Principi di Progettazione

Quando si progettano agenti, considera tre dimensioni:  
- **Spazio**: Gli agenti dovrebbero collegare persone e conoscenza, essere accessibili ma non invasivi.  
- **Tempo**: Gli agenti dovrebbero apprendere dal *Passato*, fornire suggerimenti rilevanti nel *Presente* e adattarsi per il *Futuro*.  
- **Nucleo**: Accogliere l’incertezza ma stabilire fiducia attraverso trasparenza e controllo utente.

## 5. Riassunto delle Lezioni Chiave

- **Lezione 1**: Gli agenti sono sistemi, non solo modelli. Percepiscono, ragionano e agiscono.  
- **Lezione 2**: Microsoft Agent Framework astrae la complessità di chiamata degli strumenti e gestione dello stato.  
- **Lezione 3**: Progettare con trasparenza e controllo per l’utente in mente.  
- **Lezione 4**: Gli strumenti sono le "mani" dell’agente. La definizione dello schema è cruciale perché il LLM capisca come usarli.  
- **Lezione 7**: La pianificazione è la "funzione esecutiva" dell’agente, che gli consente di affrontare flussi di lavoro complessi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per l’accuratezza, si prega di considerare che le traduzioni automatiche possono contenere errori o inesattezze. Il documento originale nella sua lingua madre deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non ci assumiamo responsabilità per eventuali fraintendimenti o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->