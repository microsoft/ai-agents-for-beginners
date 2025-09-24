<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d2f04b783b9e1253100329afd698f8ff",
  "translation_date": "2025-08-29T13:02:04+00:00",
  "source_file": "05-agentic-rag/README.md",
  "language_code": "it"
}
-->
[![Agentic RAG](../../../translated_images/lesson-5-thumbnail.20ba9d0c0ae64fae06637eb2023395d437b0152c0463c2227ff456afe5f14644.it.png)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Clicca sull'immagine sopra per guardare il video di questa lezione)_

# Agentic RAG

Questa lezione offre una panoramica completa sull'Agentic Retrieval-Augmented Generation (Agentic RAG), un paradigma emergente dell'IA in cui i modelli linguistici di grandi dimensioni (LLM) pianificano autonomamente i loro prossimi passi mentre estraggono informazioni da fonti esterne. A differenza dei modelli statici di recupero e lettura, l'Agentic RAG prevede chiamate iterative all'LLM, intervallate da richieste a strumenti o funzioni e output strutturati. Il sistema valuta i risultati, affina le query, invoca strumenti aggiuntivi se necessario e continua questo ciclo fino a raggiungere una soluzione soddisfacente.

## Introduzione

Questa lezione coprirà:

- **Comprendere l'Agentic RAG:** Scopri il paradigma emergente dell'IA in cui i modelli linguistici di grandi dimensioni (LLM) pianificano autonomamente i loro prossimi passi mentre estraggono informazioni da fonti di dati esterne.
- **Stile Iterativo Maker-Checker:** Comprendi il ciclo di chiamate iterative all'LLM, intervallate da richieste a strumenti o funzioni e output strutturati, progettato per migliorare la correttezza e gestire query malformate.
- **Esplorare Applicazioni Pratiche:** Identifica scenari in cui l'Agentic RAG eccelle, come ambienti in cui la correttezza è prioritaria, interazioni complesse con database e flussi di lavoro estesi.

## Obiettivi di Apprendimento

Dopo aver completato questa lezione, saprai come/comprenderai:

- **Comprendere l'Agentic RAG:** Scopri il paradigma emergente dell'IA in cui i modelli linguistici di grandi dimensioni (LLM) pianificano autonomamente i loro prossimi passi mentre estraggono informazioni da fonti di dati esterne.
- **Stile Iterativo Maker-Checker:** Comprendi il concetto di un ciclo di chiamate iterative all'LLM, intervallate da richieste a strumenti o funzioni e output strutturati, progettato per migliorare la correttezza e gestire query malformate.
- **Possedere il Processo di Ragionamento:** Comprendi la capacità del sistema di gestire autonomamente il proprio processo di ragionamento, prendendo decisioni su come affrontare i problemi senza affidarsi a percorsi predefiniti.
- **Flusso di Lavoro:** Comprendi come un modello agentico decida autonomamente di recuperare rapporti sulle tendenze di mercato, identificare dati sui concorrenti, correlare metriche di vendita interne, sintetizzare i risultati e valutare la strategia.
- **Cicli Iterativi, Integrazione di Strumenti e Memoria:** Scopri la dipendenza del sistema da un modello di interazione ciclico, mantenendo stato e memoria tra i passaggi per evitare cicli ripetitivi e prendere decisioni informate.
- **Gestione dei Fallimenti e Auto-Correzione:** Esplora i meccanismi di auto-correzione robusti del sistema, inclusi iterazione e ri-query, utilizzo di strumenti diagnostici e ricorso alla supervisione umana.
- **Limiti dell'Agenzia:** Comprendi i limiti dell'Agentic RAG, concentrandoti sull'autonomia specifica del dominio, la dipendenza dall'infrastruttura e il rispetto delle linee guida.
- **Casi d'Uso Pratici e Valore:** Identifica scenari in cui l'Agentic RAG eccelle, come ambienti in cui la correttezza è prioritaria, interazioni complesse con database e flussi di lavoro estesi.
- **Governance, Trasparenza e Fiducia:** Scopri l'importanza della governance e della trasparenza, inclusi ragionamenti spiegabili, controllo dei bias e supervisione umana.

## Cos'è l'Agentic RAG?

L'Agentic Retrieval-Augmented Generation (Agentic RAG) è un paradigma emergente dell'IA in cui i modelli linguistici di grandi dimensioni (LLM) pianificano autonomamente i loro prossimi passi mentre estraggono informazioni da fonti esterne. A differenza dei modelli statici di recupero e lettura, l'Agentic RAG prevede chiamate iterative all'LLM, intervallate da richieste a strumenti o funzioni e output strutturati. Il sistema valuta i risultati, affina le query, invoca strumenti aggiuntivi se necessario e continua questo ciclo fino a raggiungere una soluzione soddisfacente. Questo stile iterativo “maker-checker” migliora la correttezza, gestisce query malformate e garantisce risultati di alta qualità.

Il sistema gestisce attivamente il proprio processo di ragionamento, riscrivendo query fallite, scegliendo metodi di recupero diversi e integrando più strumenti—come la ricerca vettoriale in Azure AI Search, database SQL o API personalizzate—prima di finalizzare la risposta. La qualità distintiva di un sistema agentico è la sua capacità di gestire autonomamente il proprio processo di ragionamento. Le implementazioni tradizionali di RAG si affidano a percorsi predefiniti, ma un sistema agentico determina autonomamente la sequenza di passaggi in base alla qualità delle informazioni trovate.

## Definizione di Agentic Retrieval-Augmented Generation (Agentic RAG)

L'Agentic Retrieval-Augmented Generation (Agentic RAG) è un paradigma emergente nello sviluppo dell'IA in cui gli LLM non solo estraggono informazioni da fonti di dati esterne, ma pianificano anche autonomamente i loro prossimi passi. A differenza dei modelli statici di recupero e lettura o delle sequenze di prompt attentamente scriptate, l'Agentic RAG prevede un ciclo di chiamate iterative all'LLM, intervallate da richieste a strumenti o funzioni e output strutturati. A ogni passaggio, il sistema valuta i risultati ottenuti, decide se affinare le query, invoca strumenti aggiuntivi se necessario e continua questo ciclo fino a raggiungere una soluzione soddisfacente.

Questo stile iterativo “maker-checker” è progettato per migliorare la correttezza, gestire query malformate verso database strutturati (es. NL2SQL) e garantire risultati bilanciati e di alta qualità. Piuttosto che affidarsi esclusivamente a catene di prompt attentamente ingegnerizzate, il sistema gestisce attivamente il proprio processo di ragionamento. Può riscrivere query fallite, scegliere metodi di recupero diversi e integrare più strumenti—come la ricerca vettoriale in Azure AI Search, database SQL o API personalizzate—prima di finalizzare la risposta. Questo elimina la necessità di framework di orchestrazione eccessivamente complessi. Invece, un ciclo relativamente semplice di “chiamata LLM → utilizzo strumento → chiamata LLM → …” può produrre output sofisticati e ben fondati.

![Agentic RAG Core Loop](../../../translated_images/agentic-rag-core-loop.c8f4b85c26920f71ed181ebb14001ac7aae47c0b0af237edcf71898645a62db3.it.png)

## Gestire il Processo di Ragionamento

La qualità distintiva che rende un sistema “agentico” è la sua capacità di gestire autonomamente il proprio processo di ragionamento. Le implementazioni tradizionali di RAG spesso dipendono da percorsi predefiniti stabiliti dagli esseri umani: una catena di pensieri che delinea cosa recuperare e quando.  
Ma quando un sistema è veramente agentico, decide internamente come affrontare il problema. Non sta semplicemente eseguendo uno script; sta determinando autonomamente la sequenza di passaggi in base alla qualità delle informazioni trovate.  
Ad esempio, se gli viene chiesto di creare una strategia di lancio di un prodotto, non si affida esclusivamente a un prompt che descrive l'intero flusso di lavoro di ricerca e decisione. Invece, il modello agentico decide autonomamente di:

1. Recuperare rapporti sulle tendenze di mercato attuali utilizzando Bing Web Grounding.
2. Identificare dati rilevanti sui concorrenti utilizzando Azure AI Search.
3. Correlare metriche di vendita interne storiche utilizzando Azure SQL Database.
4. Sintetizzare i risultati in una strategia coesa orchestrata tramite Azure OpenAI Service.
5. Valutare la strategia per individuare lacune o incoerenze, avviando un altro ciclo di recupero se necessario.  

Tutti questi passaggi—affinare le query, scegliere le fonti, iterare fino a essere “soddisfatti” della risposta—sono decisi dal modello, non pre-scriptati da un essere umano.

## Cicli Iterativi, Integrazione di Strumenti e Memoria

![Tool Integration Architecture](../../../translated_images/tool-integration.0f569710b5c17c106757adba082f6c4be025ca0721bff7d1ee4b929a3617a600.it.png)

Un sistema agentico si basa su un modello di interazione ciclico:

- **Chiamata Iniziale:** L'obiettivo dell'utente (ovvero il prompt dell'utente) viene presentato all'LLM.
- **Invocazione di Strumenti:** Se il modello identifica informazioni mancanti o istruzioni ambigue, seleziona uno strumento o un metodo di recupero—come una query su un database vettoriale (es. Azure AI Search Hybrid search su dati privati) o una chiamata SQL strutturata—per raccogliere più contesto.
- **Valutazione e Affinamento:** Dopo aver esaminato i dati restituiti, il modello decide se le informazioni sono sufficienti. In caso contrario, affina la query, prova uno strumento diverso o adatta il suo approccio.
- **Ripetere Fino a Soddisfazione:** Questo ciclo continua finché il modello non determina di avere abbastanza chiarezza ed evidenze per fornire una risposta finale ben ragionata.
- **Memoria e Stato:** Poiché il sistema mantiene stato e memoria tra i passaggi, può ricordare tentativi precedenti e i loro risultati, evitando cicli ripetitivi e prendendo decisioni più informate man mano che procede.

Nel tempo, questo crea una sorta di comprensione evolutiva, consentendo al modello di affrontare compiti complessi e multi-step senza richiedere un intervento umano costante o una riformulazione del prompt.

## Gestione dei Fallimenti e Auto-Correzione

L'autonomia dell'Agentic RAG include anche meccanismi robusti di auto-correzione. Quando il sistema incontra vicoli ciechi—come il recupero di documenti irrilevanti o query malformate—può:

- **Iterare e Ri-Query:** Invece di restituire risposte di basso valore, il modello tenta nuove strategie di ricerca, riscrive query di database o esamina set di dati alternativi.
- **Utilizzare Strumenti Diagnostici:** Il sistema può invocare funzioni aggiuntive progettate per aiutarlo a eseguire il debug dei suoi passaggi di ragionamento o confermare la correttezza dei dati recuperati. Strumenti come Azure AI Tracing saranno importanti per abilitare un'osservabilità e un monitoraggio robusti.
- **Ricorrere alla Supervisione Umana:** Per scenari ad alto rischio o che falliscono ripetutamente, il modello potrebbe segnalare incertezza e richiedere una guida umana. Una volta che l'essere umano fornisce un feedback correttivo, il modello può incorporare quella lezione per il futuro.

Questo approccio iterativo e dinamico consente al modello di migliorare continuamente, garantendo che non sia solo un sistema “one-shot” ma uno che apprende dai suoi errori durante una sessione specifica.

![Self Correction Mechanism](../../../translated_images/self-correction.da87f3783b7f174bdc592c754b352884dd283814758bfeb7a68f5fd910272f3b.it.png)

## Limiti dell'Agenzia

Nonostante la sua autonomia all'interno di un compito, l'Agentic RAG non è paragonabile a un'Intelligenza Artificiale Generale. Le sue capacità “agentiche” sono confinate agli strumenti, alle fonti di dati e alle politiche fornite dagli sviluppatori umani. Non può inventare i propri strumenti o uscire dai confini del dominio che gli sono stati assegnati. Piuttosto, eccelle nell'orchestrare dinamicamente le risorse a disposizione.  
Le principali differenze rispetto a forme di IA più avanzate includono:

1. **Autonomia Specifica del Dominio:** I sistemi Agentic RAG si concentrano sul raggiungimento di obiettivi definiti dall'utente all'interno di un dominio noto, utilizzando strategie come la riscrittura delle query o la selezione degli strumenti per migliorare i risultati.
2. **Dipendenza dall'Infrastruttura:** Le capacità del sistema dipendono dagli strumenti e dai dati integrati dagli sviluppatori. Non può superare questi limiti senza intervento umano.
3. **Rispetto delle Linee Guida:** Linee guida etiche, regole di conformità e politiche aziendali rimangono molto importanti. La libertà dell'agente è sempre vincolata da misure di sicurezza e meccanismi di supervisione (si spera?).

## Casi d'Uso Pratici e Valore

L'Agentic RAG eccelle in scenari che richiedono raffinamento iterativo e precisione:

1. **Ambienti in cui la Correttezza è Prioritaria:** In controlli di conformità, analisi normative o ricerche legali, il modello agentico può verificare ripetutamente i fatti, consultare più fonti e riscrivere query fino a produrre una risposta accuratamente verificata.
2. **Interazioni Complesse con Database:** Quando si lavora con dati strutturati in cui le query possono spesso fallire o richiedere aggiustamenti, il sistema può affinare autonomamente le sue query utilizzando Azure SQL o Microsoft Fabric OneLake, garantendo che il recupero finale sia allineato con l'intento dell'utente.
3. **Flussi di Lavoro Estesi:** Sessioni più lunghe potrebbero evolversi man mano che emergono nuove informazioni. L'Agentic RAG può incorporare continuamente nuovi dati, modificando le strategie mentre apprende di più sul problema.

## Governance, Trasparenza e Fiducia

Man mano che questi sistemi diventano più autonomi nel loro ragionamento, governance e trasparenza sono cruciali:

- **Ragionamento Spiegabile:** Il modello può fornire una traccia di audit delle query effettuate, delle fonti consultate e dei passaggi di ragionamento seguiti per arrivare alla sua conclusione. Strumenti come Azure AI Content Safety e Azure AI Tracing / GenAIOps possono aiutare a mantenere la trasparenza e mitigare i rischi.
- **Controllo dei Bias e Recupero Bilanciato:** Gli sviluppatori possono ottimizzare le strategie di recupero per garantire che vengano considerate fonti di dati bilanciate e rappresentative, e auditare regolarmente gli output per rilevare bias o schemi distorti utilizzando modelli personalizzati per organizzazioni avanzate di data science con Azure Machine Learning.
- **Supervisione Umana e Conformità:** Per compiti sensibili, la revisione umana rimane essenziale. L'Agentic RAG non sostituisce il giudizio umano in decisioni ad alto rischio—lo integra fornendo opzioni più accuratamente verificate.

Avere strumenti che forniscono un chiaro registro delle azioni è essenziale. Senza di essi, il debug di un processo multi-step può essere molto difficile. Vedi il seguente esempio da Literal AI (azienda dietro Chainlit) per un'esecuzione di un agente:

![AgentRunExample](../../../translated_images/AgentRunExample.471a94bc40cbdc0cd04c1f43c8d8c9b751f10d97918c900e29cb3ba0d6aa4c00.it.png)

## Conclusione

L'Agentic RAG rappresenta un'evoluzione naturale nel modo in cui i sistemi di IA gestiscono compiti complessi e intensivi di dati. Adottando un modello di interazione ciclico, selezionando autonomamente strumenti e affinando le query fino a ottenere un risultato di alta qualità, il sistema va oltre il semplice seguire i prompt statici, diventando un decisore più adattivo e consapevole del contesto. Sebbene ancora vincolato da infrastrutture e linee guida etiche definite dagli esseri umani, queste capacità agentiche consentono interazioni con l'IA più ricche, dinamiche e, in definitiva, più utili per le imprese e gli utenti finali.

### Hai altre domande sull'Agentic RAG?

Unisciti al [Discord di Azure AI Foundry](https://aka.ms/ai-agents/discord) per incontrare altri studenti, partecipare agli orari di ricevimento e ottenere risposte alle tue domande sugli AI Agents.

## Risorse Aggiuntive

-
<a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">
Implementazione di Retrieval Augmented Generation (RAG) con Azure OpenAI Service: Scopri come utilizzare i tuoi dati con Azure OpenAI Service. Questo modulo di Microsoft Learn fornisce una guida completa all'implementazione di RAG</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Valutazione delle applicazioni di intelligenza artificiale generativa con Azure AI Foundry: Questo articolo tratta la valutazione e il confronto dei modelli su dataset pubblicamente disponibili, incluse applicazioni di Agentic AI e architetture RAG</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Che cos'è Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Una guida completa alla generazione aumentata da retrieval basata su agenti – Notizie da generation RAG</a>
- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: potenzia il tuo RAG con la riformulazione delle query e l'auto-query! Hugging Face Open-Source AI Cookbook</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Aggiungere livelli agentici a RAG</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Il futuro degli assistenti di conoscenza: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Come costruire sistemi Agentic RAG</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Utilizzare Azure AI Foundry Agent Service per scalare i tuoi agenti AI</a>

### Articoli Accademici

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Iterative Refinement with Self-Feedback</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Language Agents with Verbal Reinforcement Learning</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG</a>

## Lezione Precedente

[Tool Use Design Pattern](../04-tool-use/README.md)

## Prossima Lezione

[Building Trustworthy AI Agents](../06-building-trustworthy-agents/README.md)

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si consiglia una traduzione professionale eseguita da un traduttore umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.