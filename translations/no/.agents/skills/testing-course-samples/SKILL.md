---
name: testing-course-samples
description: Brukes når du blir bedt om å validere, teste, røykteste eller kjøre kursets
  notatbok og kodeeksempler mot en aktiv Microsoft Foundry / Azure OpenAI-konfigurasjon.
  Dekker miljøoppsett (.env, az login, pakker), skriptet/validate-notebooks.ps1-kjøreren,
  tolkning av PASS/FAIL-resultater, og hvilke leksjoner som trenger ekstra ressurser
  (Azure AI Search, GitHub MCP, Foundry Local, Playwright).
---
# Testing av Eksempelkurs

Valider at leksjons-notatbøker og kodeeksempler kjører mot en levende
Microsoft Foundry / Azure OpenAI-oppsett. Repositoriet leverer en kjører på
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) som
kjører hver Python-notatbok hodeløst og skriver ut en PASS/FAIL-matrise.

## Når man skal bruke den
- "Valider alle notatbøker / eksempler mot min Azure-abonnement."
- "Rasktest kurset etter oppgradering av pakker eller modellendringer."
- "Hvilke leksjoner består fortsatt / feiler live?"

Bruk **ikke** denne for AI Smoke Test GitHub Action (som validerer *utrullerte*
hostede agenter — se [`tests/README.md`](../../../tests/README.md)). Denne skillen
kjører notatbøkene lokalt.

## Forutsetninger (sjekk først)
1. **Python 3.12+** med kursavhengigheter: `python -m pip install -r requirements.txt`
   pluss kjøremiljø: `python -m pip install nbconvert ipykernel`.
2. **`.env` i repos rot** (kopier fra [`.env.example`](../../../../../.env.example)) med minst:
   - `AZURE_AI_PROJECT_ENDPOINT` — Foundry prosjektendepunkt
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — en ikke-utdatert utrulling (f.eks. `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) og `AZURE_OPENAI_DEPLOYMENT`
     for leksjoner som kontakter Azure OpenAI direkte (Leksjon 06, 02-azure-openai, 14 handoff/human-loop).
3. **`az login`** fullført — eksemplene autentiserer med `AzureCliCredential` (Entra ID, uten nøkkel).
4. Verifiser at modellutrullingen finnes:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Kjør valideringen
```powershell
# Alle Python-notatbøker (hopper .NET, .venv, site-packages, oversettelser, ferdighetsressurser)
pwsh scripts/validate-notebooks.ps1

# En enkelt leksjon, med lengre tidsavbrudd per celle
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Bare list opp hva som ville kjøres (ingen kjøring)
pwsh scripts/validate-notebooks.ps1 -List

# Eksplisitt tolker (hvis `python` ikke er i PATH, f.eks. Windows Store-alias)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
Skriptet skriver ut kjørte kopier, per-notatbok logger, og `results.json` til
`$env:TEMP\aiab-nbval` og avslutter med antall feil.

Midlertidige feil (felles-abonnement HTTP 429 rate limits, en tilfeldig
`AzureCliCredential` token-hickup, eller timeout) blir forsøkt på nytt automatisk
(`-Retries`, standard 2, med `-RetryDelaySeconds` backoff, standard 20). Hvis en
modellutrulling jevnlig får 429, sjekk abonnementets GlobalStandard
TPM-kvote (`az cognitiveservices usage list -l <region>`) — det hjelper ikke å øke
kapasiteten til én enkelt utrulling når *abonnementets* kvote er brukt opp.

## Tolkning av resultater
- `PASS` — notatboken kjørte fra start til slutt uten cellfeil.
- `FAIL` — den første `*Error` / `*Exception` linjen vises; åpne matchende
  `log_*.txt` i utdata-mappen for full traceback.
- En enkelt notatboks feil er begrenset av `-Timeout` (per celle), så en hengende
  human-in-the-loop-celle fremstår som `StdinNotImplementedError` i stedet for å henge.

## Leksjoner som krever ekstra ressurser (forventet å feile uten)
| Leksjon | Ekstra krav |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, nøkkel) — har en minnebasert fallback |
| 11 MCP / GitHub | GitHub MCP-server + PAT |
| 13 minne (cognee) | `cognee` konfigurert med modell-leverandør |
| 15 nettleser-bruk | Playwright nettlesere installert (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 lokal agent | Foundry Local runtime + en nedlastet Qwen-modell (på enheten, ikke sky) |
| `*-dotnet-*` notatbøker | .NET Interactive-kjerne (utelatt som standard; bruk `-IncludeDotnet`) |

## Rapportering
Oppsummer som en PASS/FAIL-tabell gruppert etter leksjon. Skill ut ekte regresjoner
(kode-/konfigurasjonsfeil som må fikses) fra miljømangler (manglende Search/Foundry Local/PAT),
og vis den feilede `log_*.txt` for hver reell feil.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->