---
name: testing-course-samples
---
# Test af kursusprøver

Bekræft, at lektions-notebooks og kodeeksempler kører mod en aktiv
Microsoft Foundry / Azure OpenAI opsætning. Repoet indeholder en runner i
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1), som
eksekverer hver Python-notebook headlessly og udskriver en PASS/FAIL matrix.

## Hvornår bruges den
- "Valider alle notebooks / prøver mod mit Azure abonnement."
- "Røgryst kurset efter opgradering af pakker eller ændring af modeller."
- "Hvilke lektioner går stadig igennem / fejler live?"

Brug **ikke** denne til AI Smoke Test GitHub Action (som validerer *udrullede*
hostede agenter — se [`tests/README.md`](../../../tests/README.md)). Denne skill
kører notebooks lokalt.

## Forudsætninger (kontrollér først)
1. **Python 3.12+** med kursusafhængigheder: `python -m pip install -r requirements.txt`
   plus eksekvereren: `python -m pip install nbconvert ipykernel`.
2. **`.env` i repoets rod** (kopiér fra [`.env.example`](../../../../../.env.example)) med mindst:
   - `AZURE_AI_PROJECT_ENDPOINT` — Foundry projekt-endpoint
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — en ikke-deprecieret udrulning (fx `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) og `AZURE_OPENAI_DEPLOYMENT`
     for lektioner, der kalder Azure OpenAI direkte (Lektion 06, 02-azure-openai, 14 handoff/human-loop).
3. **`az login`** gennemført — prøverne godkendes med `AzureCliCredential` (Entra ID, keyless).
4. Bekræft at modeludrulningen findes:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Kørsel af validering
```powershell
# Alle Python-notebooks (springer .NET, .venv, site-packages, oversættelser, færdighedsaktiver over)
pwsh scripts/validate-notebooks.ps1

# En enkelt lektion med en længere timeout pr. celle
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Bare list, hvad der ville køre (ingen udførelse)
pwsh scripts/validate-notebooks.ps1 -List

# Eksplicit fortolker (hvis `python` ikke er på PATH, f.eks. Windows Store alias)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
Skriptet skriver eksekverede kopier, per-notebook logs, og `results.json` til
`$env:TEMP\aiab-nbval` og afslutter med antallet af fejl.

Forbigående fejl (shared-subscription HTTP 429 rate limits, en lejlighedsvis
`AzureCliCredential` token-fejl eller timeout) prøves automatisk igen
(`-Retries`, standard 2, med `-RetryDelaySeconds` tilbagekobling, standard 20). Hvis en
modeludrulning jævnligt giver 429, tjek abonnementets GlobalStandard
TPM-kvote (`az cognitiveservices usage list -l <region>`) — at øge en enkelt
udrulnings kapacitet hjælper ikke når *abonnementets* kvote er opbrugt.

## Fortolkning af resultater
- `PASS` — notebooken kørte igennem fra start til slut uden cellefejl.
- `FAIL` — den første `*Error` / `*Exception` linje vises; åbn den tilsvarende
  `log_*.txt` i output-mappen for fuld traceback.
- En enkelt notebooks fejl begrænses af `-Timeout` (per celle), så en frossen
  human-in-the-loop celle fremstår som `StdinNotImplementedError` i stedet for at fryse.

## Lektioner der kræver ekstra ressourcer (forventes at fejle uden dem)
| Lektion | Ekstra krav |
|--------|------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, nøgle) — har en fallback vej i hukommelsen |
| 11 MCP / GitHub | GitHub MCP server + PAT |
| 13 memory (cognee) | `cognee` konfigureret med en modeludbyder |
| 15 browser-use | Playwright browsere installeret (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 lokal agent | Foundry Local runtime + en downloadet Qwen model (on-device, ikke i skyen) |
| `*-dotnet-*` notebooks | .NET Interactive kernel (udelukket som standard; brug `-IncludeDotnet`) |

## Rapportering tilbage
Opsummer som en PASS/FAIL tabel grupperet efter lektion. Skill ægte regressionsfejl
(kode-/konfigurationsfejl der skal rettes) fra miljømangler (manglende Search/Foundry Local/PAT),
og referer til den fejlede `log_*.txt` for hver reel fejl.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->