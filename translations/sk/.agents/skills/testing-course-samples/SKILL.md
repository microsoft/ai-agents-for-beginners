---
name: testing-course-samples
---
# Testovanie ukážok kurzu

Overte, či sa lekčné notebooky a ukážky kódu spúšťajú proti živej
inštalácii Microsoft Foundry / Azure OpenAI. Repo obsahuje skript runner na
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1), ktorý
bezhlavo vykoná každý Python notebook a vypíše maticu PASS/FAIL.

## Kedy použiť
- "Overiť všetky notebooky / ukážky proti mojej Azure predplatnému."
- "Rýchly test kurzu po aktualizácii balíkov alebo zmene modelov."
- "Ktoré lekcie stále prechádzajú / zlyhávajú v reálnom čase?"

Nepoužívajte tento nástroj pre AI Smoke Test GitHub Action (ktorý overuje *nasadených*
hostovaných agentov — pozri [`tests/README.md`](../../../tests/README.md)). Tento nástroj
spúšťa notebooky lokálne.

## Predpoklady (najprv skontrolujte)
1. **Python 3.12+** s dependencies kurzu: `python -m pip install -r requirements.txt`
   plus vykonávateľ: `python -m pip install nbconvert ipykernel`.
2. **`.env` v koreňovom adresári repozitára** (skopírovať z [`.env.example`](../../../../../.env.example)) s minimálne:
   - `AZURE_AI_PROJECT_ENDPOINT` — endpoint projektu Foundry
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — neodporúčaný deployment (napr. `gpt-4.1-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) a `AZURE_OPENAI_DEPLOYMENT`
     pre lekcie, ktoré volajú Azure OpenAI priamo (Lekcia 06, 02-azure-openai, 14 handoff/human-loop).
3. **`az login`** ukončené — ukážky autentifikujú cez `AzureCliCredential` (Entra ID, bez kľúča).
4. Overte, že deployment modelu existuje:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Spustenie validácie
```powershell
# Všetky Pythonové poznámkové bloky (vynechá .NET, .venv, site-packages, preklady, skill assets)
pwsh scripts/validate-notebooks.ps1

# Jedna lekcia s dlhším časovým limitom na bunku
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Iba vypísať, čo by sa spustilo (žiadna exekúcia)
pwsh scripts/validate-notebooks.ps1 -List

# Explicitný interpret (ak `python` nie je v PATH, napr. alias Windows Store)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
Skript zapisuje vykonané kópie, záznamy ku každému notebooku a `results.json` do
`$env:TEMP\aiab-nbval` a ukončí sa s počtom neúspechov.

## Interpretácia výsledkov
- `PASS` — notebook bol spustený od začiatku do konca bez chyby bunky.
- `FAIL` — zobrazuje sa prvý riadok s chybou `*Error` / `*Exception`; otvorte príslušný
  súbor `log_*.txt` v adresári výstupu pre celý traceback.
- Neúspech jedného notebooku je obmedzený timeoutom na bunku (`-Timeout`), takže zaseknutá
  bunka s interakciou človeka sa zobrazí ako `StdinNotImplementedError` namiesto zaseknutia.

## Lekcie, ktoré vyžadujú extra zdroje (očakávané zlyhanie bez nich)
| Lekcia | Extra požiadavky |
|--------|------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, kľúč) — má náhradnú cestu v pamäti |
| 11 MCP / GitHub | GitHub MCP server + PAT |
| 13 memory (cognee) | `cognee` nakonfigurovaný s poskytovateľom modelu |
| 15 browser-use | Nainštalované prehliadače Playwright (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry Local runtime + stiahnutý model Qwen (na zariadení, bez cloudu) |
| `*-dotnet-*` notebooky | .NET Interactive kernel (štandardne vylúčené; použiť `-IncludeDotnet`) |

## Reportovanie späť
Zhrňte ako tabuľku PASS/FAIL zoskupenú podľa lekcie. Oddelte reálne regresie
(chyby v kóde/konfigurácii na opravu) od nedostatkov v prostredí (chýba Search/Foundry Local/PAT),
a uveďte zlyhávajúce `log_*.txt` pre každý reálny neúspech.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->