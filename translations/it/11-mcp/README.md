<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "e255edb8423b34b4bba20263ef38f208",
  "translation_date": "2025-07-24T08:17:22+00:00",
  "source_file": "11-mcp/README.md",
  "language_code": "it"
}
-->
# Lezione 11: Integrazione del Protocollo di Contesto Modello (MCP)

## Introduzione al Protocollo di Contesto Modello (MCP)

Il Protocollo di Contesto Modello (MCP) è un framework all'avanguardia progettato per standardizzare le interazioni tra modelli di intelligenza artificiale e applicazioni client. MCP funge da ponte tra i modelli di IA e le applicazioni che li utilizzano, fornendo un'interfaccia coerente indipendentemente dall'implementazione del modello sottostante.

Aspetti chiave di MCP:

- **Comunicazione Standardizzata**: MCP stabilisce un linguaggio comune per le applicazioni per comunicare con i modelli di IA
- **Gestione Avanzata del Contesto**: Consente un passaggio efficiente delle informazioni contestuali ai modelli di IA
- **Compatibilità Cross-platform**: Funziona con diversi linguaggi di programmazione, tra cui C#, Java, JavaScript, Python e TypeScript
- **Integrazione Semplice**: Permette agli sviluppatori di integrare facilmente diversi modelli di IA nelle loro applicazioni

MCP è particolarmente utile nello sviluppo di agenti di IA, poiché consente agli agenti di interagire con vari sistemi e fonti di dati attraverso un protocollo unificato, rendendo gli agenti più flessibili e potenti.

## Obiettivi di Apprendimento
- Comprendere cos'è MCP e il suo ruolo nello sviluppo di agenti di IA
- Configurare e impostare un server MCP per l'integrazione con GitHub
- Creare un sistema multi-agente utilizzando gli strumenti MCP
- Implementare RAG (Retrieval Augmented Generation) con Azure Cognitive Search

## Prerequisiti
- Python 3.8+
- Node.js 14+
- Abbonamento Azure
- Account GitHub
- Conoscenza di base di Semantic Kernel

## Istruzioni per la Configurazione

1. **Configurazione dell'Ambiente**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configurare i Servizi Azure**
   - Creare una risorsa Azure Cognitive Search
   - Configurare il servizio Azure OpenAI
   - Impostare le variabili d'ambiente in `.env`

3. **Configurazione del Server MCP**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

## Struttura del Progetto

```
11-mcp/
├── code_samples/
│   ├── github-mcp/
│   │   ├── app.py              # Main application
│   │   ├── event-descriptions.md  # Event data
│   │   └── MCP_SETUP.md        # Setup guide
│   └── mcp-agents/             # Agent-to-agent communication
│       ├── client/             # MCP client implementation
│       ├── server/             # MCP server with agents
│       └── README.md           # Advanced agent examples
├── README.md
└── requirements.txt
```

## Componenti Principali

### 1. Sistema Multi-Agente
- Agente GitHub: Analisi dei repository
- Agente Hackathon: Raccomandazioni sui progetti
- Agente Eventi: Suggerimenti per eventi tecnologici

### 2. Integrazione con Azure
- Cognitive Search per l'indicizzazione degli eventi
- Azure OpenAI per l'intelligenza degli agenti
- Implementazione del pattern RAG

### 3. Strumenti MCP
- Analisi dei repository GitHub
- Ispezione del codice
- Estrazione dei metadati

## Analisi del Codice

L'esempio dimostra:
1. Integrazione del server MCP
2. Orchestrazione multi-agente
3. Integrazione con Azure Cognitive Search
4. Implementazione del pattern RAG

Caratteristiche principali:
- Analisi in tempo reale dei repository GitHub
- Raccomandazioni intelligenti sui progetti
- Abbinamento di eventi utilizzando Azure Search
- Risposte in streaming con Chainlit

## Esecuzione dell'Esempio

Per istruzioni dettagliate sulla configurazione e ulteriori informazioni, fare riferimento al [README dell'Esempio del Server MCP su GitHub](./code_samples/github-mcp/README.md).

1. Avviare il server MCP:
   ```bash
   npx @modelcontextprotocol/server-github
   ```

2. Lanciare l'applicazione:
   ```bash
   chainlit run app.py -w
   ```

3. Testare l'integrazione:
   ```
   Example query: "Analyze repositories for username: <github_username>"
   ```

## Risoluzione dei Problemi

Problemi comuni e soluzioni:
1. Problemi di Connessione MCP
   - Verificare che il server sia in esecuzione
   - Controllare la disponibilità della porta
   - Confermare i token GitHub

2. Problemi con Azure Search
   - Validare le stringhe di connessione
   - Controllare l'esistenza dell'indice
   - Verificare il caricamento dei documenti

## Prossimi Passi
- Esplorare ulteriori strumenti MCP
- Implementare agenti personalizzati
- Migliorare le capacità RAG
- Aggiungere più fonti di eventi
- **Avanzato**: Consultare [mcp-agents/](../../../11-mcp/code_samples/mcp-agents) per esempi di comunicazione agente-agente

## Risorse
- [MCP per Principianti](https://aka.ms/mcp-for-beginners)  
- [Documentazione MCP](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Documentazione Azure Cognitive Search](https://learn.microsoft.com/azure/search/)
- [Guide di Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un esperto umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.