---
name: local-ai-agents
license: MIT
---
# Creare Agenti AI Locali con Foundry Local e Qwen

> Competenze complementari per [Lezione 17 – Creare Agenti AI Locali](../../../17-creating-local-ai-agents/README.md).
> Usalo per aiutare un apprendente a costruire un agente che ragiona, chiama strumenti e cerca
> documentazione interamente sulla propria macchina — nessuna inferenza cloud. Basa ogni
> raccomandazione sul contenuto della lezione e sul notebook eseguibile.

## Attivatori

Attiva questa competenza quando un apprendente vuole:
- Eseguire un agente **completamente sul dispositivo** per motivi di privacy, costo o offline.
- Servire un modello localmente con **Foundry Local** e connettersi tramite l'endpoint compatibile OpenAI.
- Usare un modello **Qwen per chiamata di funzioni** per guidare chiamate affidabili a strumenti locali.
- Aggiungere **RAG locale** (Chroma) o un **server MCP locale**.
- Progettare una strategia di instradamento **ibrida** locale/cloud.

## Modello mentale di base

Un SLM sacrifica ampiezza per privacy, costo e funzionamento offline. La strategia vincente:
**lascia che l'SLM orchestrii e che gli strumenti facciano il lavoro pesante.** Il
modello non ha bisogno di *conoscere* il codice — deve sapere quando chiamare
`read_file` e `search_docs`. Questo sfrutta un punto di forza dell'SLM (decisioni limitate
come la selezione degli strumenti) e evita il suo punto debole (conoscenza ampia, ragionamenti multi-hop lunghi).


## Perché questi elementi specifici

- **Foundry Local** espone un **endpoint HTTP compatibile OpenAI**, quindi il codice agente cloud si trasferisce cambiando solo `base_url` (e usando una chiave API locale segnaposto). Seleziona automaticamente anche la build migliore (CPU/GPU/NPU) per la macchina.
- I modelli **Qwen** sono addestrati per la chiamata di funzioni ed emettono chiamate strumento ben formate in modo coerente — questo è ciò che trasforma un modello *chat* locale in un *agente* locale.
- **Chroma** gira in-process e memorizza vettori su disco, così tutta la pipeline RAG (embedding → memorizzazione → recupero → ragionamento) rimane locale.
- **MCP** è un trasporto, non un servizio cloud: un server MCP può girare localmente via `stdio`.

## Essenziali per l'installazione

```bash
foundry model run qwen2.5-7b-instruct
foundry service status
```

```python
from foundry_local import FoundryLocalManager
from openai import OpenAI

manager = FoundryLocalManager("qwen2.5-7b-instruct")
client = OpenAI(base_url=manager.endpoint, api_key=manager.api_key)  # segnaposto locale
```

Un minimo realistico è ~8 GB di RAM; una GPU/NPU aiuta ma non è obbligatoria.

## Pattern chiave da riprodurre

Indirizza l'apprendente al notebook
[`17-local-agent-foundry-local.ipynb`](../../../17-creating-local-ai-agents/code_samples/17-local-agent-foundry-local.ipynb):

- **Strumenti sandboxed**: ogni strumento file risolve i percorsi e rifiuta tutto ciò che sta fuori da una singola radice di progetto — anche localmente, uno strumento gira con i permessi dell'utente.
- **Loop di chiamata strumenti**: registra gli strumenti con lo schema OpenAI tools, esegui localmente gli strumenti richiesti, reinserisci i risultati, ripeti fino alla risposta finale.
- **RAG locale**: inserisci i documenti in una collezione Chroma; `search_docs` restituisce i primi k chunk.
- **MCP locale**: connetti a un server locale via `stdio`; limita a una directory di progetto e valida gli output.

## Instradamento ibrido (locale come uno dei modelli)

| Situazione | Dove gira |
|-----------|---------------|
| Dati sensibili / offline | SLM locale |
| Compito semplice, limitato | SLM locale (economico, veloce) |
| Ragionamento multi-hop complesso su dati non sensibili | Modello cloud |
| Interruzione cloud | SLM locale (degradazione controllata) |

Questo rispecchia l'idea di instradamento modello della Lezione 16, con la workstation come una
delle rotte. Preferisci design che facciano fallback al locale così l'agente degrada in
qualità piuttosto che fallire completamente.

## Guardrail per l'assistente

- Mantieni ogni operazione file/strumento limitata a una directory progetto sandboxed.
- Non inviare codice o dati al cloud quando l'obiettivo dichiarato dell'apprendente è privacy/offline — mantieni tutta la pipeline locale.
- Imposta aspettative realistiche per la qualità SLM; usa strumenti e RAG piuttosto che la conoscenza memorizzata del modello.
- Nota che la Lezione 17 **non** ha un endpoint Foundry Responses, quindi l'azione di smoke-test cloud non si applica — convalida eseguendo il notebook localmente.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->