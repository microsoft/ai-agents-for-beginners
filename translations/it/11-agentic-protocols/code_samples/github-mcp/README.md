# Esempio del server Github MCP

## Descrizione

Questa è stata una demo creata per l'AI Agents Hackathon organizzato attraverso il Microsoft Reactor.

Questo strumento viene utilizzato per raccomandare progetti per hackathon basati sui repository Github di un utente.
Questo viene fatto tramite:

1. **Github Agent** - Usa il Github MCP Server per recuperare i repo e le informazioni su quei repo.
2. **Hackathon Agent** - Prende i dati dal Github Agent e genera idee creative per progetti da hackathon basate sui progetti, sui linguaggi usati dall'utente e sulle track di progetto per l'AI Agents hackathon.
3. **Events Agent** - In base ai suggerimenti del Hackathon Agent, l'Events Agent raccomanderà eventi rilevanti dalla serie AI Agent Hackathon.
## Esecuzione del codice 

### Variabili d'ambiente

Questa demo usa Microsoft Agent Framework, Azure OpenAI Service, il Github MCP Server e Azure AI Search.

Assicurati di aver impostato le variabili d'ambiente necessarie per usare questi strumenti:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Avvio del server Chainlit

Per connettersi al server MCP, questa demo utilizza Chainlit come interfaccia di chat. 

Per avviare il server, usa il seguente comando nel tuo terminale:

```bash
chainlit run app.py -w
```

Questo dovrebbe avviare il tuo server Chainlit su `localhost:8000` e popolare il tuo Azure AI Search Index con il contenuto di `event-descriptions.md`. 

## Connessione al server MCP

Per connetterti al Github MCP Server, seleziona l'icona "plug" sotto la casella di chat "Type your message here..":

![Connessione MCP](../../../../../translated_images/it/mcp-chainlit-1.7ed66d648e3cfb28.webp)

Da lì puoi cliccare su "Connect an MCP" per aggiungere il comando per connetterti al Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Sostituisci "[YOUR PERSONAL ACCESS TOKEN]" con il tuo Personal Access Token reale. 

Dopo la connessione, dovresti vedere un (1) accanto all'icona "plug" per confermare che è connesso. In caso contrario, prova a riavviare il server chainlit con `chainlit run app.py -w`.

## Utilizzo della demo 

Per avviare il flusso di lavoro degli agenti per raccomandare progetti per l'hackathon, puoi digitare un messaggio come: 

"Raccomanda progetti per l'hackathon per l'utente Github koreyspace"

The Router Agent will analyze your request and determine which combination of agents (GitHub, Hackathon, and Events) is best suited to handle your query. The agents work together to provide comprehensive recommendations based on GitHub repository analysis, project ideation, and relevant tech events.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Dichiarazione di non responsabilità:
Questo documento è stato tradotto mediante il servizio di traduzione basato su IA Co-op Translator (https://github.com/Azure/co-op-translator). Sebbene ci impegniamo a garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o inesattezze. Il documento originale nella sua lingua dovrebbe essere considerato la fonte autorevole. Per informazioni critiche si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->