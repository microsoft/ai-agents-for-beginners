---
name: testing-course-samples
---
# Testa kursproverna

Validera att lektionernas anteckningsböcker och kodexempel körs mot en live
Microsoft Foundry / Azure OpenAI-miljö. Repositoriet levererar en körbar fil på
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) som
exekverar varje Python-anteckningsbok headlessly och skriver ut en PASS/FAIL-matris.

## När man ska använda
- "Validera alla anteckningsböcker / exempel mot mitt Azure-abonnemang."
- "Snabbtesta kursen efter uppgradering av paket eller modelländringar."
- "Vilka lektioner klarar sig fortfarande / misslyckas live?"

Använd **inte** detta för AI Smoke Test GitHub Action (som validerar *utplacerade*
hostade agenter — se [`tests/README.md`](../../../tests/README.md)). Denna förmåga
kör anteckningsböckerna lokalt.

## Förutsättningar (kontrollera först)
1. **Python 3.12+** med kursberoenden: `python -m pip install -r requirements.txt`
   plus exekveraren: `python -m pip install nbconvert ipykernel`.
2. **`.env` i repo-roten** (kopiera från [`.env.example`](../../../../../.env.example)) med minst:
   - `AZURE_AI_PROJECT_ENDPOINT` — Foundry-projektendpoint
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — en icke-deprecierad distribution (t.ex. `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) och `AZURE_OPENAI_DEPLOYMENT`
     för lektioner som anropar Azure OpenAI direkt (Lektion 06, 02-azure-openai, 14 handoff/human-loop).
3. **`az login`** genomfört — prover autentiserar med `AzureCliCredential` (Entra ID, nyckellöst).
4. Verifiera att modelldistributionen finns:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Köra valideringen
```powershell
# Alla Python-notebookar (hoppar över .NET, .venv, site-packages, översättningar, kompetensresurser)
pwsh scripts/validate-notebooks.ps1

# En enskild lektion, med längre tidsgräns per cell
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Lista bara vad som skulle köras (ingen exekvering)
pwsh scripts/validate-notebooks.ps1 -List

# Explicit tolk (om `python` inte finns i PATH, t.ex. Windows Store-alias)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
Skriptet skriver körda kopior, per-anteckningsboksloggar och `results.json` till
`$env:TEMP\aiab-nbval` och avslutar med antalet fel.

Övergående fel (delade-prenumerations HTTP 429 hastighetsbegränsningar, ett tillfälligt
`AzureCliCredential` tokenhaveri eller en timeout) försöks automatiskt igen
(`-Retries`, standard 2, med `-RetryDelaySeconds` paus, standard 20). Om en
modelldistribution regelbundet ger 429, kontrollera prenumerationens GlobalStandard
TPM-kvot (`az cognitiveservices usage list -l <region>`) — att öka kapaciteten hos en enda
distribution hjälper inte när *prenumerations*kvooten är uttömd.

## Tolka resultaten
- `PASS` — anteckningsboken kördes från början till slut utan cellfel.
- `FAIL` — den första `*Error` / `*Exception`-raden visas; öppna motsvarande
  `log_*.txt` i utdatamappen för fullständigt felsökningsspår.
- Ett enskilt anteckningsboksfel är begränsat av `-Timeout` (per cell), så en fastnad
  human-in-the-loop cell visas som `StdinNotImplementedError` istället för att frysa.

## Lektioner som kräver extra resurser (förväntas misslyckas utan dem)
| Lektion | Extra krav |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, nyckel) — har en fallback-väg i minnet |
| 11 MCP / GitHub | GitHub MCP-server + PAT |
| 13 minne (cognee) | `cognee` konfigurerad med en modellleverantör |
| 15 browser-use | Playwright-browser installerade (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 lokal agent | Foundry Local-runtime + en nedladdad Qwen-modell (på enheten, ingen moln) |
| `*-dotnet-*` anteckningsböcker | .NET Interactive-kärna (utesluten som standard; använd `-IncludeDotnet`) |

## Rapportera tillbaka
Sammanfatta som en PASS/FAIL-tabell grupperad efter lektion. Separera verkliga regressioner
(kod-/konfigurationsbuggar att åtgärda) från miljöbrister (saknad Search/Foundry Local/PAT),
och ange den felande `log_*.txt` för varje verkligt fel.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->