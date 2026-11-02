[![Agentic RAG](../../../translated_images/it/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Clicca sull'immagine sopra per vedere il video di questa lezione)_

# Agentic RAG

Questa lezione offre una panoramica completa di Agentic Retrieval-Augmented Generation (Agentic RAG), un paradigma emergente di IA in cui i modelli di linguaggio di grandi dimensioni (LLM) pianificano autonomamente i loro prossimi passi mentre estraggono informazioni da fonti esterne. A differenza dei modelli statici di recupero-then-read, Agentic RAG prevede chiamate iterative al LLM, intervallate da chiamate a strumenti o funzioni e output strutturati. Il sistema valuta i risultati, affina le query, attiva ulteriori strumenti se necessario e continua questo ciclo fino a ottenere una soluzione soddisfacente.

## Introduzione

Questa lezione tratterà

- **Comprendere Agentic RAG:** Impara il paradigma emergente nell'IA dove i modelli di linguaggio di grandi dimensioni (LLM) pianificano autonomamente i loro prossimi passi mentre estraggono informazioni da fonti dati esterne.
- **Comprendere lo Stile Iterativo Maker-Checker:** Comprendi il ciclo di chiamate iterative al LLM, intervallate da chiamate a strumenti o funzioni e output strutturati, progettato per migliorare la correttezza e gestire query malformate.
- **Esplorare Applicazioni Pratiche:** Identifica scenari in cui Agentic RAG eccelle, come ambienti incentrati sulla correttezza, interazioni complesse con database e flussi di lavoro estesi.

## Obiettivi di Apprendimento

Dopo aver completato questa lezione, saprai come/comprenderai:

- **Comprendere Agentic RAG:** Impara il paradigma emergente nell'IA dove i modelli di linguaggio di grandi dimensioni (LLM) pianificano autonomamente i loro prossimi passi attingendo a fonti dati esterne.
- **Stile Iterativo Maker-Checker:** Comprendi il concetto di un ciclo di chiamate iterative al LLM, intervallate da chiamate a strumenti o funzioni e output strutturati, progettato per migliorare la correttezza e gestire query malformate.
- **Gestire il Processo di Ragionamento:** Comprendi la capacità del sistema di gestire il proprio processo di ragionamento, prendendo decisioni su come affrontare i problemi senza affidarsi a percorsi predefiniti.
- **Flusso di Lavoro:** Comprendi come un modello agentico decida autonomamente di recuperare report sulle tendenze di mercato, identificare dati dei concorrenti, correlare metriche di vendita interne, sintetizzare i risultati e valutare la strategia.
- **Loop Iterativi, Integrazione degli Strumenti e Memoria:** Impara come il sistema si basi su un modello di interazione a ciclo, mantenendo stato e memoria tra i passaggi per evitare loop ripetitivi e prendere decisioni informate.
- **Gestione dei Fallimenti e Auto-Correzione:** Esplora i robusti meccanismi di auto-correzione del sistema, compreso iterazione e nuova interrogazione, uso di strumenti diagnostici e ricorso alla supervisione umana.
- **Limiti dell'Agenzia:** Comprendi le limitazioni di Agentic RAG, con particolare attenzione all'autonomia specifica del dominio, dipendenza dall'infrastruttura e rispetto delle misure di sicurezza.
- **Casi d'Uso Pratici e Valore:** Identifica scenari in cui Agentic RAG eccelle, come ambienti incentrati sulla correttezza, interazioni complesse con database e flussi di lavoro estesi.
- **Governance, Trasparenza e Fiducia:** Impara l'importanza della governance e della trasparenza, compreso il ragionamento spiegabile, il controllo dei bias e la supervisione umana.

## Cos'è Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) è un paradigma emergente di IA in cui i modelli di linguaggio di grandi dimensioni (LLM) pianificano autonomamente i loro prossimi passi attingendo a informazioni da fonti esterne. A differenza dei modelli statici di recupero-then-read, Agentic RAG prevede chiamate iterative al LLM, intervallate da chiamate a strumenti o funzioni e output strutturati. Il sistema valuta i risultati, affina le query, attiva ulteriori strumenti se necessario e continua questo ciclo fino a ottenere una soluzione soddisfacente. Questo stile iterativo “maker-checker” migliora la correttezza, gestisce query malformate e garantisce risultati di alta qualità.

Il sistema gestisce attivamente il proprio processo di ragionamento, riscrivendo query fallite, scegliendo metodi di recupero diversi e integrando più strumenti — come la ricerca vettoriale in Azure AI Search, database SQL o API personalizzate — prima di finalizzare la risposta. La qualità distintiva di un sistema agentico è la sua capacità di gestire autonomamente il proprio processo di ragionamento. Le implementazioni tradizionali di RAG si affidano a percorsi predefiniti, mentre un sistema agentico determina autonomamente la sequenza di passi basandosi sulla qualità dell'informazione trovata.

## Definizione di Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) è un paradigma emergente nello sviluppo di IA in cui i LLM non solo estraggono informazioni da fonti dati esterne, ma pianificano autonomamente i loro prossimi passi. A differenza dei modelli statici di recupero-then-read o delle sequenze di prompt accuratamente testate, Agentic RAG prevede un ciclo di chiamate iterative al LLM, intervallate da chiamate a strumenti o funzioni e output strutturati. Ad ogni passaggio, il sistema valuta i risultati ottenuti, decide se affinare le query, invoca ulteriori strumenti se necessario e continua questo ciclo fino al raggiungimento di una soluzione soddisfacente.

Questo stile iterativo “maker-checker” è progettato per migliorare la correttezza, gestire query malformate per database strutturati (es. NL2SQL) e garantire risultati bilanciati e di alta qualità. Piuttosto che affidarsi esclusivamente a catene di prompt ingegnerizzate, il sistema gestisce attivamente il proprio processo di ragionamento. Può riscrivere query fallite, scegliere metodi di recupero diversi e integrare più strumenti — come la ricerca vettoriale in Azure AI Search, database SQL o API personalizzate — prima di finalizzare la risposta. Ciò elimina la necessità di framework di orchestrazione eccessivamente complessi. Un ciclo relativamente semplice di “chiamata LLM → uso strumento → chiamata LLM → …” può produrre output sofisticati e ben fondati.

![Agentic RAG Core Loop](../../../translated_images/it/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## Gestione del Processo di Ragionamento

La qualità distintiva che rende un sistema “agentico” è la sua capacità di gestire il proprio processo di ragionamento. Le implementazioni tradizionali di RAG dipendono spesso da un percorso predefinito dagli umani: una catena di pensiero che indica cosa recuperare e quando.
Ma quando un sistema è veramente agentico, decide internamente come affrontare il problema. Non esegue semplicemente uno script; determina autonomamente la sequenza dei passi basandosi sulla qualità delle informazioni trovate.
Per esempio, se gli viene chiesto di creare una strategia di lancio prodotto, non si affida solo a un prompt che dettaglia l’intero flusso di ricerca e decisione. Invece, il modello agentico decide autonomamente di:

1. Recuperare report sulle tendenze di mercato attuali usando Bing Web Grounding
2. Identificare dati rilevanti dei concorrenti usando Azure AI Search.
3.	Correlare metriche di vendita interne storiche usando Azure SQL Database.
4. Sintetizzare i risultati in una strategia coerente orchestrata tramite Azure OpenAI Service.
5.	Valutare la strategia per individuare lacune o incongruenze, effettuando un altro ciclo di recupero se necessario.
Tutti questi passaggi — affinare query, scegliere fonti, iterare finché la risposta non è “soddisfacente” — sono decisi dal modello, non pre-scritti da un umano.

## Loop Iterativi, Integrazione degli Strumenti e Memoria

![Tool Integration Architecture](../../../translated_images/it/tool-integration.0f569710b5c17c10.webp)

Un sistema agentico si basa su un modello di interazione a ciclo:

- **Chiamata Iniziale:** L'obiettivo dell’utente (ossia il prompt dell’utente) viene presentato al LLM.
- **Invocazione dello Strumento:** Se il modello identifica informazioni mancanti o istruzioni ambigue, seleziona uno strumento o un metodo di recupero — come una query a un database vettoriale (es. Azure AI Search Hybrid su dati privati) o una chiamata SQL strutturata — per raccogliere più contesto.
- **Valutazione e Affinamento:** Dopo aver esaminato i dati restituiti, il modello decide se l'informazione è sufficiente. Se no, affina la query, prova uno strumento diverso o modifica il suo approccio.
- **Ripeti fino a soddisfazione:** Questo ciclo continua finché il modello determina di avere abbastanza chiarezza e evidenze per fornire una risposta finale ben ragionata.
- **Memoria e Stato:** Poiché il sistema mantiene stato e memoria tra i passaggi, può ricordare tentativi precedenti e risultati, evitando loop ripetitivi e prendendo decisioni più informate durante il processo.

Nel tempo, questo crea una sensazione di comprensione evolutiva, permettendo al modello di gestire compiti complessi e multi-step senza richiedere interventi umani continui o riformulazioni del prompt.

## Gestione dei Fallimenti e Auto-Correzione

L’autonomia di Agentic RAG include anche robusti meccanismi di auto-correzione. Quando il sistema incontra blocchi — come il recupero di documenti irrilevanti o query malformate — può:

- **Iterare e Riformulare le Query:** Invece di restituire risposte a basso valore, il modello tenta nuove strategie di ricerca, riscrive query al database o considera set di dati alternativi.
- **Utilizzare Strumenti Diagnostici:** Il sistema può invocare funzioni aggiuntive progettate per aiutarlo a debugare i passi del ragionamento o confermare la correttezza dei dati recuperati. Strumenti come Azure AI Tracing saranno importanti per abilitare una robusta osservabilità e monitoraggio.
- **Ricorrere alla Supervisione Umana:** Per scenari critici o errori ripetuti, il modello può segnalare incertezza e richiedere guida umana. Una volta ricevuto un feedback correttivo dall’umano, il modello può incorporarlo per le sessioni future.

Questo approccio iterativo e dinamico permette al modello di migliorare continuamente, garantendo che non sia solo un sistema one-shot ma uno che apprende dai propri errori durante una sessione.

![Self Correction Mechanism](../../../translated_images/it/self-correction.da87f3783b7f174b.webp)

## Limiti dell'Agenzia

Nonostante la sua autonomia nel compito, Agentic RAG non è equivalente all’Intelligenza Artificiale Generale. Le sue capacità “agentiche” sono confinate agli strumenti, fonti dati e politiche fornite dagli sviluppatori umani. Non può inventare propri strumenti o uscire dai confini di dominio stabiliti. Al contrario, eccelle nell’orchestrare dinamicamente le risorse disponibili.
Differenze chiave rispetto a forme di IA più avanzate includono:

1. **Autonomia Specifica del Dominio:** I sistemi Agentic RAG sono focalizzati sul raggiungimento di obiettivi definiti dall’utente in un dominio noto, impiegando strategie come la riscrittura delle query o la selezione degli strumenti per migliorare gli esiti.
2. **Dipendenza dall’Infrastruttura:** Le capacità del sistema dipendono dagli strumenti e dati integrati dagli sviluppatori. Non può superare questi limiti senza intervento umano.
3. **Rispetto delle Misure di Sicurezza:** Linee guida etiche, regole di conformità e politiche aziendali rimangono fondamentali. La libertà dell’agente è sempre vincolata da misure di sicurezza e meccanismi di supervisione (si spera!)

## Casi d'Uso Pratici e Valore

Agentic RAG eccelle in scenari che richiedono raffinamento iterativo e precisione:

1. **Ambienti Incentrati sulla Correttezza:** In verifiche di conformità, analisi regolatorie o ricerche legali, il modello agentico può verificare ripetutamente fatti, consultare più fonti e riscrivere query finché non produce una risposta accuratamente verificata.
2. **Interazioni Complesse con Database:** Quando si lavora con dati strutturati, dove le query possono spesso fallire o necessitare di aggiustamenti, il sistema può affinare autonomamente le query usando Azure SQL o Microsoft Fabric OneLake, assicurando che il recupero finale corrisponda all’intenzione dell’utente.
3. **Flussi di Lavoro Estesi:** Le sessioni di lunga durata possono evolvere man mano che emergono nuove informazioni. Agentic RAG può continuamente incorporare nuovi dati, modificando strategie man mano che apprende di più sul problema.

## Governance, Trasparenza e Fiducia

Man mano che questi sistemi diventano più autonomi nel loro ragionamento, governance e trasparenza sono cruciali:

- **Ragionamento Spiegabile:** Il modello può fornire una traccia di audit delle query effettuate, delle fonti consultate e dei passi di ragionamento seguiti per raggiungere la conclusione. Strumenti come Azure AI Content Safety e Azure AI Tracing / GenAIOps aiutano a mantenere la trasparenza e a mitigare i rischi.
- **Controllo dei Bias e Recupero Bilanciato:** Gli sviluppatori possono ottimizzare le strategie di recupero per garantire che siano considerate fonti dati bilanciate e rappresentative, e possono regolarmente verificare gli output per individuare bias o pattern distorti usando modelli personalizzati per organizzazioni avanzate di data science che utilizzano Azure Machine Learning.
- **Supervisione Umana e Conformità:** Per compiti sensibili, la revisione umana resta essenziale. Agentic RAG non sostituisce il giudizio umano in decisioni ad alto rischio — lo integra offrendo opzioni accuratamente verificate.

Avere strumenti che forniscano un chiaro registro delle azioni è essenziale. Senza di essi, il debug di un processo multi-step può essere molto difficile. Vedi il seguente esempio da Literal AI (azienda dietro Chainlit) per un run di un agente:

![AgentRunExample](../../../translated_images/it/AgentRunExample.471a94bc40cbdc0c.webp)

## Conclusione

Agentic RAG rappresenta un’evoluzione naturale nel modo in cui i sistemi IA gestiscono compiti complessi e intensivi di dati. Adottando un modello di interazione a ciclo, selezionando autonomamente strumenti e affinando query fino a ottenere un risultato di alta qualità, il sistema supera il semplice seguire prompt statici passando a un decisore più adattivo e contestuale. Pur essendo ancora vincolato da infrastrutture e linee guida etiche definite dall’uomo, queste capacità agentiche consentono interazioni IA più ricche, dinamiche e alla fine più utili sia per le imprese sia per gli utenti finali.

### Hai altre domande su Agentic RAG?

Unisciti al [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) per incontrare altri studenti, partecipare alle ore di ricevimento e ottenere risposte alle tue domande sugli AI Agents.

## Risorse Aggiuntive

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">Implementare Retrieval Augmented Generation (RAG) con Azure OpenAI Service: Impara come utilizzare i tuoi dati con Azure OpenAI Service. Questo modulo Microsoft Learn fornisce una guida completa all’implementazione di RAG</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Valutazione delle applicazioni di IA generativa con Microsoft Foundry: Questo articolo tratta la valutazione e il confronto di modelli su dataset pubblici, incluse applicazioni Agentic AI e architetture RAG</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Cos’è Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Una guida completa alla Retrieval Augmented Generation basata su agenti – News da generation RAG</a>

- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: potenzia il tuo RAG con la riformulazione delle query e l'auto-query! Ricettario AI open-source di Hugging Face</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Aggiungere livelli agentici a RAG</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Il futuro degli assistenti di conoscenza: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Come costruire sistemi Agentic RAG</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Utilizzo di Microsoft Foundry Agent Service per scalare i tuoi agenti AI</a>

### Articoli Accademici

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: raffinamento iterativo con auto-feedback</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: agenti linguistici con apprendimento per rinforzo verbale</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: grandi modelli linguistici possono autocorreggersi con critiche interattive agli strumenti</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation: una panoramica su Agentic RAG</a>

## Test di Funzionamento Rapido di Questo Agente (Opzionale)

Dopo aver imparato a distribuire agenti in [Lesson 16](../16-deploying-scalable-agents/README.md), puoi effettuare un test rapido dell'agente `TravelRAGAgent` di questa lezione — verificando che le sue risposte rimangano ancorate alla base di conoscenza — con [`tests/lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json). Vedi [`tests/README.md`](../tests/README.md) su come eseguirlo.

## Lezione Precedente

[Design Pattern per l'Uso degli Strumenti](../04-tool-use/README.md)

## Lezione Successiva

[Costruire Agenti AI Affidabili](../06-building-trustworthy-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->