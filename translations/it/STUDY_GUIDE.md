# Agenti AI per Principianti - Guida di Studio e Riassunto del Corso

Questa guida fornisce un riassunto del corso "Agenti AI per Principianti" e spiega i concetti chiave, i framework e i modelli di design per costruire Agenti AI.

## 1. Introduzione agli Agenti AI

**Cosa sono gli Agenti AI?**  
Gli Agenti AI sono sistemi che estendono le capacità dei Large Language Models (LLM) dando loro accesso a **strumenti**, **conoscenza** e **memoria**. Diversamente da un semplice chatbot LLM che genera testo basato solo sui dati di addestramento, un Agente AI può:  
- **Percepire** il proprio ambiente (tramite sensori o input).  
- **Ragionare** su come risolvere un problema.  
- **Agire** per modificare l’ambiente (tramite attuatori o esecuzione di strumenti).

**Componenti Chiave di un Agente:**  
- **Ambiente**: Lo spazio in cui l'agente opera (ad esempio, un sistema di prenotazioni).  
- **Sensori**: Meccanismi per raccogliere informazioni (ad esempio, leggere un'API).  
- **Attuatori**: Meccanismi per eseguire azioni (ad esempio, inviare un’email).  
- **Cervello (LLM)**: Il motore di ragionamento che pianifica e decide quali azioni intraprendere.

## 2. Framework Agenti

Il corso copre tre framework principali per costruire agenti:

| Framework | Focus | Migliore per |
|-----------|-------|-------------|
| **Semantic Kernel** | SDK pronto per la produzione per .NET/Python | Applicazioni aziendali, integrazione dell’AI con codice esistente. |
| **AutoGen** | Collaborazione multi-agente | Scenari complessi che richiedono più agenti specializzati che comunicano tra loro. |
| **Azure AI Agent Service** | Servizio cloud gestito | Deploy sicuro e scalabile con gestione dello stato integrata. |

## 3. Modelli di Design Agenti

I modelli di design aiutano a strutturare il funzionamento degli agenti per risolvere problemi in modo affidabile.

### **Modello di Uso degli Strumenti** (Lezione 4)  
Questo modello permette agli agenti di interagire con il mondo esterno.  
- **Concetto**: All’agente viene fornito uno "schema" (una lista di funzioni disponibili e relativi parametri). L’LLM decide *quale* strumento chiamare e con *quali* argomenti in base alla richiesta dell’utente.  
- **Flusso**: Richiesta Utente -> LLM -> **Selezione Strumento** -> **Esecuzione Strumento** -> LLM (con output dello strumento) -> Risposta Finale.  
- **Casi d’uso**: Recupero dati in tempo reale (meteo, prezzi azioni), esecuzione di calcoli, esecuzione di codice.

### **Modello di Pianificazione** (Lezione 7)  
Questo modello permette agli agenti di risolvere compiti complessi a più fasi.  
- **Concetto**: L’agente suddivide un obiettivo generale in una sequenza di sotto-compiti più piccoli.  
- **Approcci**:  
  - **Decomposizione del Compito**: Suddividere "Pianifica un viaggio" in "Prenota volo", "Prenota hotel", "Noleggia auto".  
  - **Pianificazione Iterativa**: Rivalutare il piano in base ai risultati dei passaggi precedenti (es. se il volo è pieno, scegliere un’altra data).  
- **Implementazione**: Spesso coinvolge un agente "Planner" che genera un piano strutturato (es. JSON) che viene quindi eseguito da altri agenti.

## 4. Principi di Design

Quando si progettano agenti, considerare tre dimensioni:  
- **Spazio**: Gli agenti dovrebbero connettere persone e conoscenze, essere accessibili ma discreti.  
- **Tempo**: Gli agenti dovrebbero imparare dal *Passato*, fornire suggerimenti rilevanti nel *Presente* e adattarsi per il *Futuro*.  
- **Nucleo**: Accettare l’incertezza ma stabilire fiducia tramite trasparenza e controllo dell’utente.

## 5. Riassunto delle Lezioni Chiave

- **Lezione 1**: Gli agenti sono sistemi, non solo modelli. Percepisco, ragionano e agiscono.  
- **Lezione 2**: Framework come Semantic Kernel e AutoGen astraggono la complessità della chiamata agli strumenti e gestione dello stato.  
- **Lezione 3**: Progettare pensando a trasparenza e controllo dell’utente.  
- **Lezione 4**: Gli strumenti sono le "mani" dell’agente. La definizione dello schema è cruciale per far capire all’LLM come usarli.  
- **Lezione 7**: La pianificazione è la "funzione esecutiva" dell’agente, che gli permette di affrontare flussi di lavoro complessi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avvertenza**:
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o inesattezze. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->