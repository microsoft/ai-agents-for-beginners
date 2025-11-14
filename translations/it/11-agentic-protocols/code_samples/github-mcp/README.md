<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9bf0395cbc541ce8db2a9699c8678dfc",
  "translation_date": "2025-08-29T13:30:49+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/README.md",
  "language_code": "it"
}
-->
# Esempio di Server MCP Github

## Descrizione

Questa è una demo creata per l'Hackathon AI Agents organizzato dal Microsoft Reactor.

Lo strumento viene utilizzato per raccomandare progetti per l'hackathon basandosi sui repository Github di un utente. Questo viene fatto attraverso:

1. **Github Agent** - Utilizzando il Server MCP Github per recuperare i repository e le informazioni su di essi.
2. **Hackathon Agent** - Prende i dati dal Github Agent e propone idee creative per progetti di hackathon basandosi sui progetti, i linguaggi utilizzati dall'utente e i temi dell'hackathon AI Agents.
3. **Events Agent** - Sulla base delle proposte dell'Hackathon Agent, l'Events Agent raccomanderà eventi rilevanti della serie di hackathon AI Agents.

## Esecuzione del codice 

### Variabili d'ambiente

Questa demo utilizza Azure Open AI Service, Semantic Kernel, il Server MCP Github e Azure AI Search.

Assicurati di aver configurato correttamente le variabili d'ambiente per utilizzare questi strumenti:

```python
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=""
AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME=""
AZURE_OPENAI_ENDPOINT=""
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_API_VERSION=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Avvio del Server Chainlit

Per connettersi al server MCP, questa demo utilizza Chainlit come interfaccia chat.

Per avviare il server, usa il seguente comando nel tuo terminale:

```bash
chainlit run app.py -w
```

Questo dovrebbe avviare il server Chainlit su `localhost:8000` e popolare il tuo Azure AI Search Index con il contenuto di `event-descriptions.md`.

## Connessione al Server MCP

Per connettersi al Server MCP Github, seleziona l'icona a forma di "spina" sotto la casella di testo "Scrivi qui il tuo messaggio...":

![MCP Connect](../../../../../translated_images/mcp-chainlit-1.7ed66d648e3cfb28f1ea5f320b91e4404df4a24a0f236ce3de999666621f1cfc.it.png)

Da lì, puoi cliccare su "Connect an MCP" per aggiungere il comando per connetterti al Server MCP Github:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Sostituisci "[YOUR PERSONAL ACCESS TOKEN]" con il tuo effettivo Personal Access Token.

Dopo la connessione, dovresti vedere un (1) accanto all'icona della spina per confermare che la connessione è avvenuta. In caso contrario, prova a riavviare il server Chainlit con `chainlit run app.py -w`.

## Utilizzo della Demo 

Per avviare il flusso di lavoro dell'agente per raccomandare progetti di hackathon, puoi scrivere un messaggio come:

"Consiglia progetti per l'hackathon per l'utente Github koreyspace"

Il Router Agent analizzerà la tua richiesta e determinerà quale combinazione di agenti (GitHub, Hackathon ed Events) è più adatta per gestire la tua query. Gli agenti lavoreranno insieme per fornire raccomandazioni complete basate sull'analisi dei repository Github, l'ideazione di progetti e gli eventi tecnologici rilevanti.

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.