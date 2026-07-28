---
name: testing-course-samples
---
# Testování ukázek kurzu

Ověřte, že si sešitové lekce a ukázky kódu spustí proti živému 
Microsoft Foundry / Azure OpenAI prostředí. Repozitář obsahuje spouštěč v 
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1), který
spustí všechny Python notebooky bez hlavičky a vytiskne matici PASS/FAIL.

## Kdy použít
- "Ověřit všechny notebooky / ukázky proti mé Azure subskripci."
- "Rychle otestovat kurz po upgradu balíčků nebo změně modelů."
- "Které lekce stále procházejí / selhávají živě?"

**Nepoužívejte** toto pro AI Smoke Test GitHub Action (který ověřuje *nasazené* 
hostované agenty — viz [`tests/README.md`](../../../tests/README.md)). Tato dovednost 
spustí notebooky lokálně.

## Požadavky (nejprve zkontrolujte)
1. **Python 3.12+** s požadavky kurzu: `python -m pip install -r requirements.txt`
   plus exekutor: `python -m pip install nbconvert ipykernel`.
2. **`.env` v kořeni repozitáře** (zkopírovat z [`.env.example`](../../../../../.env.example)) s minimálně:
   - `AZURE_AI_PROJECT_ENDPOINT` — endpoint Foundry projektu
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — nepřestaný nasazený model (např. `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) a `AZURE_OPENAI_DEPLOYMENT`
     pro lekce volající Azure OpenAI přímo (Lekce 06, 02-azure-openai, 14 handoff/human-loop).
3. **dokončené `az login`** — ukázky autentizují přes `AzureCliCredential` (Entra ID, bez klíče).
4. Ověřit, že existuje modelové nasazení:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Spuštění ověření
```powershell
# Všechny Python notebooky (vynechává .NET, .venv, site-packages, překlady, skill assets)
pwsh scripts/validate-notebooks.ps1

# Jedna lekce, s delším timeoutem na buňku
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Pouze vypsat, co by se spustilo (bez spuštění)
pwsh scripts/validate-notebooks.ps1 -List

# Explicitní interpret (pokud `python` není v PATH, např. alias Windows Store)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
Skript zapisuje spouštěné kopie, logy ke každému notebooku a `results.json` do
`$env:TEMP\aiab-nbval` a končí s počtem neúspěchů.

Přechodné chyby (sdílené HTTP 429 limity rychlosti na subskripci, občasné
výpadky tokenu `AzureCliCredential`, nebo časový limit) se automaticky
opakují (`-Retries`, výchozí 2, s `-RetryDelaySeconds` pauzou, výchozí 20). Pokud je
modelové nasazení často 429-ováno, zkontrolujte limit GlobalStandard
TPM subskripce (`az cognitiveservices usage list -l <region>`) — zvýšení kapacity
jednoho nasazení nepomůže, pokud je *subskripční* limit vyčerpán.

## Interpretace výsledků
- `PASS` — notebook proběhl kompletně bez chyby v buňce.
- `FAIL` — zobrazuje se první řádek `*Error` / `*Exception`; otevřete odpovídající
  `log_*.txt` v adresáři výstupu pro celý traceback.
- Selhání jednoho notebooku je omezeno `-Timeout` (na buňku), takže zablokovaná
  buňka s člověkem v procesu se projeví jako `StdinNotImplementedError`, nevisí.

## Lekce vyžadující dodatečné zdroje (bez nich očekávaně selžou)
| Lekce | Dodatečná požadavka |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, klíč) — má zálohu v paměti |
| 11 MCP / GitHub | GitHub MCP server + PAT |
| 13 paměť (cognee) | `cognee` nakonfigurovaný s poskytovatelem modelu |
| 15 browser-use | Nainstalované prohlížeče Playwright (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 lokální agent | Foundry lokální runtime + stažený Qwen model (na zařízení, bez cloudu) |
| `*-dotnet-*` notebooky | .NET Interactive kernel (výchozí vyloučeno; použít `-IncludeDotnet`) |

## Zpětné hlášení
Shrňte do tabulky PASS/FAIL seskupené podle lekce. Oddělte opravdové regresy
(chyby v kódu/konfiguraci k opravě) od nedostatků prostředí (chybějící Search/Foundry Local/PAT), 
a uveďte padlé `log_*.txt` u každého reálného neúspěchu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->