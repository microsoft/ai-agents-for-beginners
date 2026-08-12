# Costruire Agenti per l'Uso del Computer (CUA)

Gli agenti per l'uso del computer possono interagire con i siti web allo stesso modo di una persona: aprendo un browser, ispezionando la pagina e prendendo la prossima migliore azione da ciò che vedono. In questa lezione, costruirai un agente di automazione del browser che cerca su Airbnb, estrae dati strutturati degli annunci e identifica il soggiorno più economico a Stoccolma.

La lezione combina Browser-Use per la navigazione guidata dall'IA, Playwright e Chrome DevTools Protocol (CDP) per il controllo del browser, Azure OpenAI per il ragionamento abilitato alla visione, e Pydantic per l'estrazione strutturata.

## Introduzione

Questa lezione tratterà:

- Capire quando gli agenti per l'uso del computer sono più adatti rispetto all'automazione solo API
- Combinare Browser-Use con Playwright e CDP per una gestione affidabile del ciclo di vita del browser
- Usare Azure OpenAI con visione e output strutturato Pydantic per estrarre dati da pagine web dinamiche
- Decidere quando utilizzare un flusso di lavoro di automazione browser agent-first, actor-first o ibrido

## Obiettivi di apprendimento

Dopo aver completato questa lezione, saprai:

- Configurare Browser-Use con Azure OpenAI e Playwright
- Costruire un flusso di lavoro di automazione browser che naviga un sito reale e gestisce elementi UI dinamici
- Estrarre risultati tipizzati dal contenuto visibile della pagina e convertirli in logica di business a valle
- Scegliere tra modelli agent e actor basandoti sulla prevedibilità del compito del browser

## Esempio di codice

Questa lezione include un tutorial in notebook:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Avvia una sessione Chrome tramite CDP, cerca annunci Airbnb per Stoccolma, estrae prezzi con la visione Browser-Use e restituisce l'opzione più economica come dati strutturati.

## Prerequisiti

- Python 3.12+
- Implementazione Azure OpenAI configurata nel tuo ambiente
- Chrome o Chromium installati localmente
- Dipendenze Playwright installate
- Familiarità base con Python asincrono

## Configurazione

Installa i pacchetti usati nel notebook:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Imposta le variabili d'ambiente Azure OpenAI usate dal notebook:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Facoltativo: per default utilizza l'ultima versione dell'API quando omesso
AZURE_OPENAI_API_VERSION=...
```

## Panoramica dell'Architettura

Il notebook mostra un flusso di lavoro di automazione browser ibrido:

1. Chrome si avvia con CDP abilitato così che Playwright e Browser-Use possano condividere la stessa sessione del browser.
2. Un agente Browser-Use gestisce i compiti di navigazione aperti come l'apertura di Airbnb, la chiusura di pop-up e la ricerca di Stoccolma.
3. La pagina attiva viene ispezionata con uno schema Pydantic strutturato per estrarre titoli degli annunci, prezzi per notte, valutazioni e URL.
4. La logica Python confronta gli annunci estratti e evidenzia il risultato più economico.

Questo approccio conserva il ragionamento basato sulla visione flessibile che Browser-Use gestisce bene, pur fornendo un controllo deterministico del browser quando necessario.

## Punti Chiave e Best Practice

### Quando Usare Agente vs Attore

| Scenario | Usa Agente | Usa Attore |
|----------|------------|-----------|
| Layout dinamici | Sì, l'IA si adatta ai cambiamenti della pagina | No, selettori fragili possono rompersi |
| Struttura nota | No, un agente è più lento del controllo diretto | Sì, veloce e preciso |
| Trovare elementi | Sì, il linguaggio naturale funziona bene | No, servono selettori esatti |
| Controllo temporale | No, meno prevedibile | Sì, pieno controllo su attese e tentativi |
| Flussi di lavoro complessi | Sì, gestisce stati UI imprevisti | No, richiede ramificazioni esplicite |

### Best Practice per Browser-Use

1. Inizia con un agente per esplorazione e navigazione dinamica.
2. Passa al controllo diretto della pagina quando l'interazione diventa prevedibile.
3. Usa modelli di output strutturati in modo che i dati estratti siano validati e tipizzati in sicurezza.
4. Inserisci ritardi strategici dopo azioni che causano cambiamenti visibili nell'UI.
5. Cattura screenshot durante l'iterazione così gli errori sono più facili da debuggare.
6. Aspettati che i siti web cambino e progetta strategie di fallback per pop-up e modifiche al layout.
7. Combina pattern agent e actor per ottenere sia flessibilità che precisione.

### Barriere di Sicurezza per Agenti Browser

Gli agenti browser operano su siti web live, quindi hanno bisogno di limiti più stretti rispetto a uno script che usa solo API note. Prima di passare da un demo notebook a un flusso reale, definisci controlli su cosa l'agente può vedere, cliccare e inviare.

1. **Definisci l'ambiente di navigazione.** Esegui l'agente in un profilo browser dedicato o sandbox e limitane l'uso ai domini necessari per il compito.
2. **Separa osservazione da azione.** Lascia che l'agente cerchi, legga ed estragga dati prima; richiedi un passo di approvazione esplicita prima che invii form, mandi messaggi, prenoti viaggi, faccia acquisti, cancelli record o modifichi impostazioni account.
3. **Tieni segreti fuori da prompt e tracce.** Non inserire password, dettagli di pagamento, cookie di sessione o dati personali grezzi nel contesto del modello. Lascia all'utente il controllo per l'autenticazione e censura i campi sensibili nei log.
4. **Tratta il contenuto della pagina come input non affidabile.** Un sito web può contenere istruzioni destinate all'agente, non all'utente. L'agente dovrebbe ignorare testi che gli chiedono di cambiare obiettivo, rivelare dati, disabilitare protezioni o visitare siti non correlati.
5. **Usa controlli deterministici per passaggi rischiosi.** Verifica URL corrente, titolo pagina, elemento selezionato, prezzo, destinatario e sintesi azione con codice prima di chiedere all'utente di approvare il passo finale.
6. **Imposta budget e condizioni di stop.** Limita numero di azioni, tentativi, schede e minuti utilizzabili dall'agente. Arresta il processo se lo stato della pagina è ambiguo invece di continuare a cliccare.
7. **Registra prove utili, non tutto.** Conserva sintesi azioni, timestamp, URL, descrizioni degli elementi selezionati e riferimenti a screenshot così i fallimenti possono essere revisionati senza memorizzare contenuti sensibili inutili.

Nell'esempio Airbnb, il comportamento sicuro di default è cercare annunci ed estrarre prezzi. Effettuare l'accesso, contattare un host o completare una prenotazione deve essere un'azione approvata separatamente dall'utente.

### Applicazioni nel Mondo Reale

- Prenotazioni di viaggi e monitoraggio prezzi
- Comparazione prezzi e verifica disponibilità e-commerce
- Estrazione strutturata da siti web dinamici
- Test e verifica UI consapevoli della visione
- Monitoraggio e allertamento siti web
- Compilazione intelligente di form in flussi multi-step

## Esempio Reale: Microsoft Project Opal

L'agente che costruisci in questa lezione è una versione piccola e locale di un **agente per l’uso del computer (CUA)** — un programma che guida un browser come farebbe una persona. Microsoft porta questa stessa idea in azienda con **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, una funzionalità in Microsoft 365 Copilot.

Con Project Opal, descrivi un compito e l'agente agisce per tuo conto usando **uso del computer su un Windows 365 Cloud PC sicuro**, operando su applicazioni, siti e dati browser-based della tua organizzazione. Funziona **asincronamente in background**, e puoi guidare il lavoro o prendere il controllo in qualsiasi momento. Esempi di lavori includono:

- Gestire richieste di appartenenza a gruppi di sicurezza
- Raccogliere e validare prove di audit per revisioni di conformità
- Gestire incidenti IT (aggiornare stato ticket, assegnare responsabili, chiudere duplicati)
- Compilare dati Excel in un report di chiusura finanziaria

Opal è un riferimento utile per come appare un agente per l’uso del computer **di livello produttivo e affidabile** — e rinforza concetti delle lezioni precedenti:

| Concetto in questo corso | Come Project Opal lo applica |
|------------------------|-----------------------------|
| **Human-in-the-loop** (Lezione 06) | Opal si ferma per credenziali di login, dati sensibili o istruzioni ambigue, e mai inserisce password o invia form senza conferma esplicita. Puoi *Prendere il Controllo* e *Restituirlo* a metà compito. |
| **Agenti affidabili e sicuri** (Lezioni 06 & 18) | Gira in un Windows 365 Cloud PC isolato, è solo browser di default (altre accessi computer bloccati, applicato via Intune), usa *la tua* identità così accede solo a ciò che sei autorizzato e registra ogni azione per auditabilità. |
| **Pianificazione & metacognizione** (Lezioni 07 & 09) | Opal crea prima un piano per il lavoro, poi supervisiona il proprio ragionamento a ogni passo e si ferma se rileva attività sospette. |
| **Capacità / strumenti riutilizzabili** (Lezione 04) | Le **Skills** ti permettono di scrivere istruzioni per lavori ripetibili (importati da un file `.md` o scritti con Opal) e riutilizzarle nelle conversazioni. |

> **Disponibilità:** Project Opal è attualmente disponibile agli utenti nel [programma di early access Frontier](https://adoption.microsoft.com/copilot/frontier-program/) con abbonamento Microsoft 365 Copilot, e l’amministratore deve completare la configurazione. Essendo una funzionalità sperimentale Frontier, le capacità potrebbero cambiare nel tempo.

## Risorse Aggiuntive

- [Inizia con Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Template di integrazione Browser-Use Playwright](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Parametri actor Browser-Use ed estrazione contenuti](https://docs.browser-use.com/customize/actor/all-parameters)
- [Configurazione del Corso](../00-course-setup/README.md)

## Lezione Precedente

[Esplorare Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

## Prossima Lezione

[Deployment di Agenti Scalabili](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->