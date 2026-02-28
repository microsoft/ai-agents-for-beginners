# Agenti AI per Principianti - Guida di Studio e Riepilogo del Corso

Questa guida fornisce un riepilogo del corso "Agenti AI per Principianti" e spiega i concetti chiave, i framework e i modelli di progettazione per costruire Agenti AI.

## 1. Introduzione agli Agenti AI

**Cosa sono gli Agenti AI?**
Gli Agenti AI sono sistemi che estendono le capacità dei Modelli di Linguaggio Estesi (LLM) fornendo loro accesso a **strumenti**, **conoscenza** e **memoria**. Diversamente da un chatbot LLM standard che genera solo testo basato sui dati di addestramento, un Agente AI può:
- **Percepire** il proprio ambiente (tramite sensori o input).
- **Ragionare** su come risolvere un problema.
- **Agire** per modificare l’ambiente (tramite attuatori o esecuzione di strumenti).

**Componenti Chiave di un Agente:**
- **Ambiente**: Lo spazio in cui opera l’agente (es. un sistema di prenotazioni).
- **Sensori**: Meccanismi per raccogliere informazioni (es. lettura di un’API).
- **Attuatori**: Meccanismi per eseguire azioni (es. invio di un’email).
- **Cervello (LLM)**: Il motore di ragionamento che pianifica e decide quali azioni intraprendere.

## 2. Framework Agentici

Il corso utilizza **Microsoft Agent Framework (MAF)** con **Azure AI Foundry Agent Service V2** per costruire agenti:

| Componente | Focus | Ideale Per |
|------------|-------|------------|
| **Microsoft Agent Framework** | SDK unificato Python/C# per agenti, strumenti e workflow | Costruire agenti con strumenti, workflow multi-agente e modelli di produzione. |
| **Azure AI Foundry Agent Service** | Runtime cloud gestito | Distribuzione sicura, scalabile con gestione dello stato, osservabilità e affidabilità integrate. |

## 3. Modelli di Progettazione Agentici

I modelli di progettazione aiutano a strutturare il modo in cui gli agenti operano per risolvere problemi in modo affidabile.

### **Modello di Utilizzo degli Strumenti** (Lezione 4)
Questo modello consente agli agenti di interagire con il mondo esterno.
- **Concetto**: All’agente viene fornito uno "schema" (una lista di funzioni disponibili e dei loro parametri). L’LLM decide *quale* strumento chiamare e con *quali* argomenti in base alla richiesta dell’utente.
- **Flusso**: Richiesta Utente -> LLM -> **Selezione Strumento** -> **Esecuzione Strumento** -> LLM (con output dello strumento) -> Risposta Finale.
- **Casi d’Uso**: Recupero dati in tempo reale (meteo, prezzi azioni), eseguire calcoli, eseguire codice.

### **Modello di Pianificazione** (Lezione 7)
Questo modello permette agli agenti di risolvere compiti complessi a più passi.
- **Concetto**: L’agente scompone un obiettivo di alto livello in una sequenza di sotto-attività più piccole.
- **Approcci**:
  - **Decomposizione del Compito**: Dividere "Pianificare un viaggio" in "Prenotare volo", "Prenotare hotel", "Noleggiare auto".
  - **Pianificazione Iterativa**: Rivalutare il piano in base all’output dei passi precedenti (es. se il volo è pieno, scegliere una data diversa).
- **Implementazione**: Spesso coinvolge un agente "Planner" che genera un piano strutturato (es. JSON) poi eseguito da altri agenti.

## 4. Principi di Progettazione

Quando si progettano agenti, considera tre dimensioni:
- **Spazio**: Gli agenti dovrebbero connettere persone e conoscenza, essere accessibili ma discreti.
- **Tempo**: Gli agenti devono imparare dal *Passato*, fornire suggerimenti rilevanti nel *Presente* e adattarsi per il *Futuro*.
- **Nucleo**: Accettare l’incertezza ma stabilire fiducia tramite trasparenza e controllo dell’utente.

## 5. Riepilogo delle Lezioni Chiave

- **Lezione 1**: Gli agenti sono sistemi, non solo modelli. Percepiscono, ragionano e agiscono.
- **Lezione 2**: Microsoft Agent Framework astrarre la complessità di chiamata degli strumenti e gestione dello stato.
- **Lezione 3**: Progettare con trasparenza e controllo utente in mente.
- **Lezione 4**: Gli strumenti sono le "mani" dell’agente. La definizione dello schema è cruciale per far comprendere all’LLM come usarli.
- **Lezione 7**: La pianificazione è la "funzione esecutiva" dell’agente, che gli permette di affrontare workflow complessi.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Avvertenza**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per la precisione, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua originale deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->