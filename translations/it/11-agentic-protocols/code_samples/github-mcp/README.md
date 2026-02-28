# Esempio del server MCP di Github

## Descrizione

Questa è stata una demo creata per l'AI Agents Hackathon ospitato tramite il Microsoft Reactor.

Lo strumento viene utilizzato per raccomandare progetti per hackathon basati sui repository Github di un utente.
Questo viene fatto tramite:

1. **Github Agent** - Utilizza il Github MCP Server per recuperare i repository e le informazioni su quei repository.
2. **Hackathon Agent** - Prende i dati dal Github Agent e propone idee creative per progetti da hackathon basate sui progetti, sui linguaggi utilizzati dall'utente e sulle tracce dei progetti per l'AI Agents hackathon.
3. **Events Agent** - In base ai suggerimenti dell'Hackathon Agent, l'Events Agent raccomanderà eventi rilevanti della serie AI Agent Hackathon.
## Esecuzione del codice 

### Variabili d'ambiente

Questa demo utilizza Microsoft Agent Framework, Azure OpenAI Service, il Github MCP Server e Azure AI Search.

Assicurati di avere impostato le opportune variabili d'ambiente per utilizzare questi strumenti:

```python
AZURE_AI_PROJECT_ENDPOINT=""
AZURE_AI_MODEL_DEPLOYMENT_NAME=""
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_API_KEY=""
``` 

## Avvio del server Chainlit

Per connettersi al server MCP, questa demo usa Chainlit come interfaccia chat. 

Per avviare il server, usa il seguente comando nel terminale:

```bash
chainlit run app.py -w
```

Questo dovrebbe avviare il tuo server Chainlit su `localhost:8000` e popolare il tuo indice Azure AI Search con il contenuto di `event-descriptions.md`. 

## Connessione al server MCP

Per connetterti al Github MCP Server, seleziona l'icona "plug" sotto la casella di chat "Type your message here..":

![Connessione MCP](../../../../../translated_images/it/mcp-chainlit-1.7ed66d648e3cfb28.webp)

Da lì puoi cliccare su "Connect an MCP" per aggiungere il comando per connetterti al Github MCP Server:

```bash
npx -y @modelcontextprotocol/server-github --env GITHUB_PERSONAL_ACCESS_TOKEN=[YOUR PERSONAL ACCESS TOKEN]
```

Sostituisci "[YOUR PERSONAL ACCESS TOKEN]" con il tuo effettivo Personal Access Token. 

Dopo la connessione, dovresti vedere un (1) accanto all'icona a forma di plug per confermare che è connesso. In caso contrario, prova a riavviare il server chainlit con `chainlit run app.py -w`.

## Utilizzo della demo 

Per avviare il flusso di lavoro degli agenti per raccomandare progetti per hackathon, puoi digitare un messaggio come: 

"Recommend hackathon projects for the Github user koreyspace"

Il Router Agent analizzerà la tua richiesta e determinerà quale combinazione di agenti (GitHub, Hackathon e Events) è più adatta a gestire la tua query. Gli agenti lavorano insieme per fornire raccomandazioni complete basate sull'analisi dei repository GitHub, sull'ideazione dei progetti e sugli eventi tecnici pertinenti.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Dichiarazione di non responsabilità:
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica basato su IA Co-op Translator (https://github.com/Azure/co-op-translator). Pur impegnandoci a garantire l'accuratezza, si prega di tenere presente che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua madre dovrebbe essere considerato la fonte autorevole. Per informazioni critiche si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->