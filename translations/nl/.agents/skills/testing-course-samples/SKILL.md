---
name: testing-course-samples
---
# Testen van de Cursusvoorbeelden

Controleer of de lesnotebooks en codevoorbeelden werken met een live
Microsoft Foundry / Azure OpenAI setup. De repo bevat een runner bij
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) die
elke Python-notebook hoofdzakelijk headless uitvoert en een PASS/FAIL matrix afdrukt.

## Wanneer te gebruiken
- "Valideer alle notebooks / voorbeelden tegen mijn Azure-abonnement."
- "Smoke-test de cursus na het upgraden van pakketten of wijzigen van modellen."
- "Welke lessen slagen nog steeds / falen live?"

Gebruik dit **niet** voor de AI Smoke Test GitHub Actie (die *geïmplementeerde*
gehoste agents valideert — zie [`tests/README.md`](../../../tests/README.md)). Deze vaardigheid
voert de notebooks lokaal uit.

## Vereisten (controleer eerst)
1. **Python 3.12+** met cursusafhankelijkheden: `python -m pip install -r requirements.txt`
   plus de executor: `python -m pip install nbconvert ipykernel`.
2. **`.env` in de root van de repo** (kopieer van [`.env.example`](../../../../../.env.example)) met tenminste:
   - `AZURE_AI_PROJECT_ENDPOINT` — Foundry project endpoint
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — een niet-verouderde deployment (bijv. `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) en `AZURE_OPENAI_DEPLOYMENT`
     voor lessen die direct Azure OpenAI aanroepen (Les 06, 02-azure-openai, 14 handoff/human-loop).
3. **`az login`** voltooid — voorbeelden authenticeren met `AzureCliCredential` (Entra ID, keyless).
4. Controleer of de model deployment bestaat:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## De validatie uitvoeren
```powershell
# Alle Python-notebooks (slaat .NET, .venv, site-packages, vertalingen, skill-middelen over)
pwsh scripts/validate-notebooks.ps1

# Een enkele les, met een langere timeout per cel
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Alleen lijst wat zou worden uitgevoerd (geen uitvoering)
pwsh scripts/validate-notebooks.ps1 -List

# Expliciete interpreter (als `python` niet op PATH staat, bv. Windows Store-alias)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
Het script schrijft uitgevoerde kopieën, per-notebook logs, en `results.json` naar
`$env:TEMP\aiab-nbval` en sluit af met het aantal fouten.

Tijdelijke fouten (gedeelde-subscriptie HTTP 429 rate limits, een incidentele
`AzureCliCredential` token hapering, of een timeout) worden automatisch herhaald
(`-Retries`, standaard 2, met `-RetryDelaySeconds` backoff, standaard 20). Als een
model deployment regelmatig 429 geeft, controleer dan de GlobalStandard
TPM quotum van de abonnement (`az cognitiveservices usage list -l <region>`) — het verhogen van de capaciteit van een
enkele deployment helpt niet als het *abonnement*quotum is uitgeput.

## Resultaten interpreteren
- `PASS` — de notebook liep volledig door zonder fouten in cellen.
- `FAIL` — de eerste `*Error` / `*Exception` regel wordt getoond; open de bijbehorende
  `log_*.txt` in de uitvoermap voor de volledige traceback.
- Een enkele notebook fout wordt begrensd door `-Timeout` (per cel), dus een vastgelopen
  human-in-the-loop cel verschijnt als `StdinNotImplementedError` in plaats van te hangen.

## Lessen die extra bronnen nodig hebben (verwacht te falen zonder deze)
| Les | Extra vereiste |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, sleutel) — heeft een fallback-pad in het geheugen |
| 11 MCP / GitHub | GitHub MCP server + PAT |
| 13 geheugen (cognee) | `cognee` geconfigureerd met een modelprovider |
| 15 browser-gebruik | Playwright browsers geïnstalleerd (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 lokale agent | Foundry Local runtime + een gedownload Qwen-model (op apparaat, geen cloud) |
| `*-dotnet-*` notebooks | .NET Interactive kernel (standaard uitgesloten; gebruik `-IncludeDotnet`) |

## Terugrapporteren
Vat samen als een PASS/FAIL tabel gegroepeerd per les. Scheid echte regressies
(code/config bugs om te repareren) van omgevingsgebreken (ontbrekende Search/Foundry Local/PAT),
en citeer de falende `log_*.txt` voor elke echte fout.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->