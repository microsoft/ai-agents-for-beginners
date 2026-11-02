# Costruire Agenti di Utilizzo del Computer (CUA)

Gli agenti di utilizzo del computer possono interagire con i siti web allo stesso modo in cui farebbe una persona: aprendo un browser, ispezionando la pagina e prendendo la migliore azione successiva basata su ciò che vedono. In questa lezione, costruirai un agente di automazione del browser che cerca su Airbnb, estrae dati strutturati delle inserzioni e identifica il soggiorno più economico a Stoccolma.

La lezione combina Browser-Use per la navigazione guidata dall'IA, Playwright e Chrome DevTools Protocol (CDP) per il controllo del browser, Azure OpenAI per il ragionamento abilitato alla visione e Pydantic per l'estrazione strutturata.

## Introduzione

Questa lezione coprirà:

- Comprendere quando gli agenti di utilizzo del computer sono più adatti rispetto all'automazione solo via API
- Combinare Browser-Use con Playwright e CDP per una gestione affidabile del ciclo di vita del browser
- Utilizzare Azure OpenAI vision e output strutturato Pydantic per estrarre dati di inserzioni da pagine web dinamiche
- Decidere quando usare un flusso di lavoro di automazione browser agent-first, actor-first, o ibrido

## Obiettivi di Apprendimento

Dopo aver completato questa lezione, saprai come:

- Configurare Browser-Use con Azure OpenAI e Playwright
- Costruire un flusso di lavoro di automazione browser che naviga un sito reale e gestisce elementi UI dinamici
- Estrarre risultati tipizzati dal contenuto visibile della pagina e trasformarli in logica aziendale a valle
- Scegliere tra pattern agent e actor in base a quanto è prevedibile il compito browser

## Esempio di Codice

Questa lezione include un tutorial in un notebook:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Avvia una sessione Chrome tramite CDP, cerca inserzioni Airbnb per Stoccolma, estrae prezzi con la visione di Browser-Use e restituisce l'opzione più economica come dati strutturati.

## Prerequisiti

- Python 3.12+
- Deploy di Azure OpenAI configurato nel tuo ambiente
- Chrome o Chromium installato localmente
- Dipendenze di Playwright installate
- Familiarità di base con Python async

## Installazione

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
# Facoltativo: usa per default l'ultima versione dell'API quando omesso
AZURE_OPENAI_API_VERSION=...
```

## Panoramica dell'Architettura

Il notebook dimostra un flusso di lavoro di automazione browser ibrido:

1. Chrome si avvia con CDP abilitato così Playwright e Browser-Use possono condividere la stessa sessione browser.
2. Un agente Browser-Use gestisce compiti di navigazione aperta come aprire Airbnb, chiudere popup e cercare Stoccolma.
3. La pagina attiva è ispezionata con uno schema Pydantic strutturato per estrarre titoli delle inserzioni, prezzi per notte, valutazioni e URL.
4. La logica Python confronta le inserzioni estratte e evidenzia il risultato più economico.

Questo approccio mantiene il ragionamento flessibile basato sulla visione in cui Browser-Use eccelle, pur offrendo un controllo deterministico del browser quando è necessario.

## Punti Chiave e Best Practice

### Quando Usare Agent vs Actor

| Scenario | Usa Agent | Usa Actor |
|----------|-----------|-----------|
| Layout dinamici | Sì, l'IA può adattarsi ai cambiamenti della pagina | No, selettori fragili possono rompersi |
| Struttura nota | No, un agente è più lento del controllo diretto | Sì, veloce e preciso |
| Trovare elementi | Sì, il linguaggio naturale funziona bene | No, servono selettori esatti |
| Controllo dei tempi | No, meno prevedibile | Sì, pieno controllo su attese e ritenti |
| Flussi di lavoro complessi | Sì, gestisce stati UI inaspettati | No, richiede ramificazioni esplicite |

### Best Practice di Browser-Use

1. Inizia con un agente per esplorazione e navigazione dinamica.
2. Passa al controllo diretto della pagina quando l'interazione diventa prevedibile.
3. Usa modelli di output strutturati in modo che i dati estratti siano validati e tipizzati in modo sicuro.
4. Aggiungi ritardi strategici dopo azioni che attivano cambiamenti visibili dell'interfaccia.
5. Cattura screenshot durante l'iterazione per facilitare il debug in caso di errori.
6. Aspettati che i siti web cambino e progetta strategie di fallback per popup e spostamenti di layout.
7. Combina pattern agent e actor per ottenere flessibilità e precisione.

### Linee Guida di Sicurezza per Agenti Browser

Gli agenti browser operano su siti live, quindi necessitano di confini più rigidi rispetto a uno script che chiama solo API note. Prima di passare da una demo notebook a un flusso reale, definisci i controlli su cosa l'agente può vedere, cliccare e inviare.

1. **Definisci l'ambiente di navigazione.** Esegui l'agente in un profilo browser dedicato o sandbox e limitane gli ambiti ai domini necessari per il compito.
2. **Separa osservazione e azione.** Permetti all'agente di cercare, leggere e estrarre dati prima; richiedi un'azione esplicita di approvazione prima di inviare moduli, mandare messaggi, prenotare viaggi, effettuare acquisti, cancellare record o modificare impostazioni account.
3. **Non inserire segreti in prompt e tracce.** Non mettere password, dettagli di pagamento, cookie di sessione o dati personali grezzi nel contesto del modello. Lascia che l’utente gestisca l’autenticazione e filtri campi sensibili dai log.
4. **Tratta il contenuto della pagina come input non affidabile.** Un sito può contenere istruzioni destinate all’agente, non all’utente. L’agente dovrebbe ignorare testo pagina che chiede di cambiare obiettivo, rivelare dati, disabilitare salvaguardie o visitare siti non correlati.
5. **Usa controlli deterministici attorno a passaggi a rischio.** Verifica URL corrente, titolo pagina, elemento selezionato, prezzo, destinatario e riepilogo azione con codice prima di chiedere all’utente di approvare il passaggio finale.
6. **Imposta budget e condizioni di arresto.** Limita numero di azioni, ritenti, schede e minuti che l’agente può usare. Ferma l’esecuzione se lo stato della pagina è ambiguo invece di continuare a cliccare.
7. **Registra evidenze utili, non tutto.** Conserva riepiloghi azioni, timestamp, URL, descrizioni degli elementi selezionati e riferimenti agli screenshot così gli errori possono essere revisionati senza memorizzare contenuto sensibile superfluo.

Nell’esempio Airbnb, il comportamento sicuro predefinito è cercare inserzioni ed estrarre prezzi. Effettuare il login, contattare un host o completare una prenotazione dovrebbe essere un’azione separata approvata dall’utente.

### Applicazioni Reali

- Prenotazione viaggi e monitoraggio prezzi
- Confronto prezzi e controlli di disponibilità per e-commerce
- Estrazione strutturata da siti web dinamici
- Testing e verifica UI con visione intelligente
- Monitoraggio e allerta siti web
- Compilazione intelligente di moduli in flussi multi-step

## Esempio Reale: Microsoft Project Opal

L'agente che costruisci in questa lezione è una piccola versione locale di un **agente di utilizzo del computer (CUA)** — un programma che controlla un browser come farebbe una persona. Microsoft sta portando questa stessa idea alle aziende con **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, una funzionalità in Microsoft 365 Copilot.

Con Project Opal, descrivi un compito e l’agente agisce per conto tuo utilizzando **l’utilizzo del computer su un Windows 365 Cloud PC sicuro**, operando attraverso le applicazioni, i siti e i dati basati su browser della tua organizzazione. Funziona **in modo asincrono in background**, e puoi guidare o prendere il controllo in ogni momento. Esempi di lavori includono:

- Gestione delle richieste di appartenenza a gruppi di sicurezza
- Raccolta e validazione di prove di audit per revisioni di conformità
- Gestione incidenti IT (aggiornamento stato ticket, assegnazione responsabili, chiusura duplicati)
- Compilare dati Excel in una presentazione per la chiusura finanziaria

Opal è un riferimento utile per come appare un agente di utilizzo del computer **di livello produzione, affidabile** — e rafforza concetti dalle lezioni precedenti:

| Concetto in questo corso | Come Project Opal lo applica |
|------------------------|-----------------------------|
| **Human-in-the-loop** (Lezione 06) | Opal si ferma per credenziali di accesso, dati sensibili o istruzioni ambigue, e non inserisce mai password o invia moduli senza conferma esplicita. Puoi *Prendere il Controllo* e *Restituire il Controllo* a metà compito. |
| **Agenti affidabili e sicuri** (Lezioni 06 e 18) | Operano in un Windows 365 Cloud PC isolato, usano solo browser (accesso ad altri computer bloccato e imposto via Intune), utilizzano *la tua* identità quindi accedono solo a ciò per cui sei autorizzato, e registrano ogni azione per auditabilità. |
| **Pianificazione & metacognizione** (Lezioni 07 e 09) | Opal genera prima un piano per il lavoro, poi supervisiona il proprio ragionamento ad ogni passo e si ferma se rileva attività sospette. |
| **Capacità/strumenti riutilizzabili** (Lezione 04) | Le **Skills** ti permettono di scrivere istruzioni per compiti ripetibili (importati da file `.md` o scritti con Opal) e riutilizzarle tra conversazioni. |

> **Disponibilità:** Project Opal è attualmente disponibile agli utenti nel [programma di accesso anticipato Frontier](https://adoption.microsoft.com/copilot/frontier-program/) con abbonamento Microsoft 365 Copilot, e il tuo amministratore deve completare la configurazione. Poiché è una funzionalità sperimentale Frontier, le capacità possono cambiare nel tempo.

## Verifica delle Conoscenze

Mettiti alla prova prima di passare alla lezione successiva.

**1. Quando un agente di utilizzo del computer basato su browser è più adatto di un flusso solo API?**

<details>
<summary>Risposta</summary>

Usa un agente browser quando il compito dipende da ciò che è visibile in un’interfaccia web, il sito non espone l’API necessaria, o la pagina cambia abbastanza spesso da rendere fragile la logica basata su API o selettori fissi. Se esiste un’API stabile per lo stesso compito, preferisci l’API perché è solitamente più veloce, più facile da testare e più sicura.
</details>

**2. In un flusso ibrido, quali parti dovrebbe gestire l’agente e quali il codice diretto Playwright?**

<details>
<summary>Risposta</summary>

Lascia all’agente compiti di navigazione aperta e stati dinamici dell’interfaccia, come trovare la pagina giusta o chiudere popup inaspettati. Passa al controllo diretto Playwright quando la struttura della pagina è nota e l’azione richiede precisione, ritenti, attese o validazione deterministica.
</details>

**3. L’esempio Airbnb trova un’inserzione che l’utente potrebbe voler prenotare. Cosa dovrebbe accadere prima che il flusso effettui il login, contatti un host o completi una prenotazione?**

<details>
<summary>Risposta</summary>

Il flusso dovrebbe fermarsi e chiedere approvazione esplicita all’utente. Prima di richiedere l’approvazione, dovrebbe mostrare un chiaro riepilogo dell’inserzione selezionata, URL corrente, prezzo, date e azione prevista. Cercare ed estrarre prezzi può essere autonomo; accesso account, messaggi, acquisti e prenotazioni dovrebbero essere approvati dall’utente.
</details>

**4. Una pagina web dice all’agente di ignorare le istruzioni originali, visitare un altro sito e rivelare credenziali salvate. Come dovrebbe trattare quel testo l’agente?**

<details>
<summary>Risposta</summary>

Trattalo come contenuto pagina non affidabile, non come istruzione da sviluppatore o utente. L’agente dovrebbe rimanere nel dominio e scopo consentiti, rifiutare di rivelare segreti e evitare di seguire testo pagina che cambia l’obiettivo, disabilita salvaguardie o lo manda a siti non correlati.
</details>

**5. Quali prove è utile conservare quando gira un agente browser, e cosa dovrebbe essere evitato?**

<details>
<summary>Risposta</summary>

Conserva riepiloghi azioni, timestamp, URL, descrizioni elementi selezionati, risultati di validazione e riferimenti a screenshot così l’esecuzione può essere rivista. Evita di memorizzare password, dettagli pagamento, cookie sessione, dati personali grezzi o contenuti pagina completi a meno che non ci sia uno specifico motivo di conservazione e privacy.
</details>

## Risorse Aggiuntive

- [Iniziare con Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Template integrazione Browser-Use Playwright](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Parametri actor Browser-Use e estrazione contenuti](https://docs.browser-use.com/customize/actor/all-parameters)
- [Configurazione del Corso](../00-course-setup/README.md)

## Lezione Precedente

[Esplorare Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

## Lezione Successiva

[Distribuzione di Agenti Scalabili](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->