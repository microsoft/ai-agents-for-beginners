---
name: testing-course-samples
---
# Test dei Campioni del Corso

Verifica che i notebook delle lezioni e i campioni di codice funzionino con una configurazione live
Microsoft Foundry / Azure OpenAI. Il repo include un runner in
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) che
esegue ogni notebook Python senza interfaccia grafica e stampa una matrice PASS/FAIL.

## Quando usare
- "Verificare tutti i notebook / campioni contro il mio abbonamento Azure."
- "Testare rapidamente il corso dopo l'aggiornamento dei pacchetti o la modifica dei modelli."
- "Quali lezioni passano/fallisco ancora live?"

Non usare **questo** per l'Azione GitHub AI Smoke Test (che verifica gli agenti *distribuiti* —
vedi [`tests/README.md`](../../../tests/README.md)). Questa skill
esegue i notebook localmente.

## Prerequisiti (controllare prima)
1. **Python 3.12+** con dipendenze del corso: `python -m pip install -r requirements.txt`
   più l'esecutore: `python -m pip install nbconvert ipykernel`.
2. **`.env` nella root del repo** (copia da [`.env.example`](../../../../../.env.example)) con almeno:
   - `AZURE_AI_PROJECT_ENDPOINT` — endpoint progetto Foundry
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — un deployment non deprecato (es. `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) e `AZURE_OPENAI_DEPLOYMENT`
     per lezioni che chiamano direttamente Azure OpenAI (Lezione 06, 02-azure-openai, 14 handoff/human-loop).
3. **`az login`** completato — i campioni si autenticano con `AzureCliCredential` (Entra ID, senza chiavi).
4. Verificare che il deployment del modello esista:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Come eseguire la validazione
```powershell
# Tutti i notebook Python (esclude .NET, .venv, site-packages, traduzioni, risorse delle skill)
pwsh scripts/validate-notebooks.ps1

# Una singola lezione, con un timeout per cella più lungo
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Elenca solamente ciò che verrebbe eseguito (nessuna esecuzione)
pwsh scripts/validate-notebooks.ps1 -List

# Interprete esplicito (se `python` non è nel PATH, es. alias del Windows Store)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
Lo script scrive copie eseguite, log per notebook e `results.json` in
`$env:TEMP\aiab-nbval` e termina con il numero di fallimenti.

Fallimenti transitori (limiti di velocità HTTP 429 su abbonamenti condivisi, un’occasionale
problema di token `AzureCliCredential` o timeout) vengono riprovati automaticamente
(`-Retries`, default 2, con backoff `-RetryDelaySeconds`, default 20). Se un
deployment del modello riceve regolarmente 429, controllare la quota TPM GlobalStandard
dell’abbonamento (`az cognitiveservices usage list -l <regione>`) — aumentare la capacità di un singolo
deployment non aiuta quando la quota *dell’abbonamento* è esaurita.

## Interpretazione dei risultati
- `PASS` — il notebook è stato eseguito dall’inizio alla fine senza errori nelle celle.
- `FAIL` — viene mostrata la prima riga `*Error` / `*Exception`; aprire il corrispondente
  `log_*.txt` nella cartella output per il traceback completo.
- Il fallimento di un singolo notebook è limitato da `-Timeout` (per cella), così una cella
  human-in-the-loop bloccata appare come `StdinNotImplementedError` invece di bloccarsi.

## Lezioni che necessitano di risorse aggiuntive (ci si aspetta un fallimento senza di esse)
| Lezione | Requisito extra |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, chiave) — ha una modalità fallback in memoria |
| 11 MCP / GitHub | Server GitHub MCP + PAT |
| 13 memory (cognee) | `cognee` configurato con un provider di modelli |
| 15 browser-use | Browser Playwright installati (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Runtime Foundry Local + un modello Qwen scaricato (on-device, senza cloud) |
| notebook `*-dotnet-*` | Kernel .NET Interactive (escluso di default; usare `-IncludeDotnet`) |

## Segnalazione
Riassumere come tabella PASS/FAIL raggruppata per lezione. Separare regressioni reali
(bug di codice/configurazione da correggere) da lacune ambientali (mancanza di Search/Foundry Local/PAT),
e citare i `log_*.txt` che falliscono per ogni errore reale.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Questo documento è stato tradotto utilizzando il servizio di traduzione AI [Co-op Translator](https://github.com/Azure/co-op-translator). Sebbene ci impegniamo per garantire la precisione, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un essere umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall’uso di questa traduzione.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->