<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c4be907703b836d1a1c360db20da4de9",
  "translation_date": "2025-08-29T13:36:51+00:00",
  "source_file": "11-agentic-protocols/code_samples/github-mcp/MCP_SETUP.md",
  "language_code": "it"
}
-->
# Guida all'integrazione del server MCP

## Prerequisiti
- Node.js installato (versione 14 o superiore)
- Gestore di pacchetti npm
- Ambiente Python con dipendenze necessarie

## Passaggi di configurazione

1. **Installa il pacchetto MCP Server**
   ```bash
   npm install -g @modelcontextprotocol/server-github
   ```

2. **Avvia il server MCP**
   ```bash
   npx @modelcontextprotocol/server-github
   ```  
   Il server dovrebbe avviarsi e mostrare un URL di connessione.

3. **Verifica la connessione**
   - Cerca l'icona della spina (🔌) nell'interfaccia Chainlit
   - Un numero (1) dovrebbe apparire accanto all'icona della spina, indicando una connessione riuscita
   - La console dovrebbe mostrare: "Configurazione del plugin GitHub completata con successo" (insieme a ulteriori linee di stato)

## Risoluzione dei problemi

### Problemi comuni

1. **Conflitto di porta**
   ```bash
   Error: listen EADDRINUSE: address already in use
   ```  
   Soluzione: Cambia la porta utilizzando:  
   ```bash
   npx @modelcontextprotocol/server-github --port 3001
   ```

2. **Problemi di autenticazione**
   - Assicurati che le credenziali GitHub siano configurate correttamente
   - Controlla che il file .env contenga i token richiesti
   - Verifica l'accesso all'API di GitHub

3. **Connessione fallita**
   - Conferma che il server sia in esecuzione sulla porta prevista
   - Controlla le impostazioni del firewall
   - Verifica che l'ambiente Python abbia i pacchetti necessari

## Verifica della connessione

Il tuo server MCP è correttamente connesso quando:
1. La console mostra "Configurazione del plugin GitHub completata con successo"
2. I log di connessione mostrano "✓ Stato connessione MCP: Attivo"
3. I comandi GitHub funzionano nell'interfaccia chat

## Variabili d'ambiente

Necessarie nel file .env:  
```
GITHUB_TOKEN=your_github_token
MCP_SERVER_PORT=3000  # Optional, default is 3000
```

## Test della connessione

Invia questo messaggio di test nella chat:  
```
Show me the repositories for username: [GitHub Username]
```  
Una risposta positiva mostrerà le informazioni del repository.

---

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche potrebbero contenere errori o imprecisioni. Il documento originale nella sua lingua nativa dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si consiglia una traduzione professionale eseguita da un traduttore umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.