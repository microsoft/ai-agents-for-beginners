---
name: testing-course-samples
description: Použite, keď sa vyžaduje overenie, testovanie, rýchle testovanie alebo
  spustenie poznámkového bloku kurzu a ukážok kódu proti živej konfigurácii Microsoft
  Foundry / Azure OpenAI. Pokrýva nastavenie prostredia (.env, az login, balíky),
  skript runner scripts/validate-notebooks.ps1, interpretáciu výsledkov PASS/FAIL
  a ktoré lekcie potrebujú ďalšie zdroje (Azure AI Search, GitHub MCP, Foundry Local,
  Playwright).
---
# Testovanie ukážok kurzu

Overte, či sa poznámkové bloky lekcií a príklady kódu spúšťajú proti live
nastaveniu Microsoft Foundry / Azure OpenAI. Repo obsahuje spúšťač v
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1), ktorý
spustí každý Python notebook bez zobrazenia GUI a vytlačí maticu PASS/FAIL.

## Kedy použiť
- "Overiť všetky poznámkové bloky / ukážky proti mojej Azure predplatnému."
- "Rýchlotest kurzu po aktualizácii balíkov alebo zmene modelov."
- "Ktoré lekcie stále prechádzajú / zlyhávajú v live režime?"

**Nepoužívajte** to pre AI Smoke Test GitHub Action (ktorý overuje *nasadených*
hostovaných agentov — pozri [`tests/README.md`](../../../tests/README.md)). Tento skript
spúšťa notebooky lokálne.

## Predpoklady (skontrolujte najskôr)
1. **Python 3.12+** s dependencies kurzu: `python -m pip install -r requirements.txt`
   plus spúšťač: `python -m pip install nbconvert ipykernel`.
2. **`.env` v koreňovom adresári repozitára** (skopírovať z [`.env.example`](../../../../../.env.example)) minimálne s:
   - `AZURE_AI_PROJECT_ENDPOINT` — endpoint projektu Foundry
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — neodporúčaný deployment (napr. `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) a `AZURE_OPENAI_DEPLOYMENT`
     pre lekcie, ktoré volajú priamo Azure OpenAI (Lekcia 06, 02-azure-openai, 14 handoff/human-loop).
3. Dokončený príkaz **`az login`** — príklady sa autentifikujú pomocou `AzureCliCredential` (Entra ID, bez kľúča).
4. Overiť, že deployment modelu existuje:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Spustenie validácie
```powershell
# Všetky Python notebooky (vynecháva .NET, .venv, site-packages, preklady, skill assets)
pwsh scripts/validate-notebooks.ps1

# Jedna lekcia, s dlhším časovým limitom na bunku
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Len zoznam, čo by sa spustilo (bez vykonania)
pwsh scripts/validate-notebooks.ps1 -List

# Explicitný interpret (ak `python` nie je v PATH, napr. alias Windows Store)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
Skript zapisuje spustené kópie, logy ku každému notebooku a `results.json` do
`$env:TEMP\aiab-nbval` a končí s počtom zlyhaní.

Prechodné chyby (HTTP 429 obmedzenia zdieľanej predplatenej služby, občasný
problém s tokenom `AzureCliCredential` alebo timeout) sa automaticky opakujú
(`-Retries`, predvolené 2, s `-RetryDelaySeconds` oneskorením, predvolené 20). Ak je
deployment modelu pravidelne blokovaný 429 odpoveďami, skontrolujte globálnu kvótu
TPM pre predplatné GlobalStandard (`az cognitiveservices usage list -l <region>`) — zvýšenie kapacity
jedného deploymentu nepomôže, ak je *kvóta* predplatného vyčerpaná.

## Interpretácia výsledkov
- `PASS` — notebook prebehol celý bez chyby bunky.
- `FAIL` — ukáže sa prvá línia `*Error` / `*Exception`; otvorte zodpovedajúci
  súbor `log_*.txt` v výstupnom adresári pre celý traceback.
- Zlyhanie jednotlivého notebooku sa obmedzuje parametrom `-Timeout` (pre bunku), takže zaseknutá
  bunka s požiadavkou na človeka je nahlásená ako `StdinNotImplementedError` namiesto zaseknutia.

## Lekcie vyžadujúce extra zdroje (očakáva sa zlyhanie bez nich)
| Lekcia | Dodatočná požiadavka |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, kľúč) — má záložnú cestu v pamäti |
| 11 MCP / GitHub | GitHub MCP server + PAT |
| 13 memory (cognee) | `cognee` nakonfigurovaný s poskytovateľom modelu |
| 15 browser-use | Nainštalované prehliadače Playwright (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 local agent | Foundry Local runtime + stiahnutý model Qwen (na zariadení, bez cloudu) |
| `*-dotnet-*` notebooky | Kernely .NET Interactive (štandardne vylúčené; použite `-IncludeDotnet`) |

## Správa späť
Zhrňte do tabuľky PASS/FAIL zoskupenej podľa lekcie. Oddeľte skutočné regresie
(chyby/konfigurácie na opravu) od nedostatkov prostredia (chýbajúci Search/Foundry Local/PAT),
a pre každé skutočné zlyhanie uveďte zodpovedajúci súbor `log_*.txt`.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->