---
name: testing-course-samples
description: "Use when asked to validate, test, smoke-test, or run the course's notebook and code samples against a live Microsoft Foundry / Azure OpenAI configuration. Covers environment setup (.env, az login, packages), the scripts/validate-notebooks.ps1 runner, interpreting PASS/FAIL results, and which lessons need extra resources (Azure AI Search, GitHub MCP, Foundry Local, Playwright)."
---
# Testarea Exemplelor din Curs

Verificați dacă caietele de lecție și exemplele de cod funcționează cu o configurare live
Microsoft Foundry / Azure OpenAI. Repozitoriul include un executabil la
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) care
rulează fiecare caiet Python fără interfață și afișează o matrice PASS/FAIL.

## Când să utilizați
- "Validarea tuturor caietelor / exemplelor în raport cu abonamentul meu Azure."
- "Testare rapidă a cursului după actualizarea pachetelor sau schimbarea modelelor."
- "Care lecții mai trec / eșuează live?"

Nu utilizați **pentru** GitHub Action AI Smoke Test (care validează agenții *deployed*
găzduiți — vezi [`tests/README.md`](../../../tests/README.md)). Această abilitate
rulează caietele local.

## Condiții preliminare (verificați întâi)
1. **Python 3.12+** cu dependențele cursului: `python -m pip install -r requirements.txt`
   plus executorul: `python -m pip install nbconvert ipykernel`.
2. **`.env` la rădăcina repo-ului** (copiat din [`.env.example`](../../../../../.env.example)) cu cel puțin:
   - `AZURE_AI_PROJECT_ENDPOINT` — punctul final al proiectului Foundry
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — un deployment neînvechit (de exemplu `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) și `AZURE_OPENAI_DEPLOYMENT`
     pentru lecțiile care apelează direct Azure OpenAI (Lecția 06, 02-azure-openai, 14 handoff/human-loop).
3. **`az login`** finalizat — exemplele se autentifică cu `AzureCliCredential` (Entra ID, fără cheie).
4. Verificați existența deployment-ului modelului:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Rularea validării
```powershell
# All Python notebooks (skips .NET, .venv, site-packages, translations, skill assets)
pwsh scripts/validate-notebooks.ps1

# A single lesson, with a longer per-cell timeout
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Just list what would run (no execution)
pwsh scripts/validate-notebooks.ps1 -List

# Explicit interpreter (if `python` is not on PATH, e.g. Windows Store alias)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
Scriptul scrie copii executate, jurnale pe caiet și `results.json` în
`$env:TEMP\aiab-nbval` și iese cu numărul erorilor.

Eșecurile tranzitorii (limitele de rată HTTP 429 pe abonamente partajate, o
ezitare ocazională a token-ului `AzureCliCredential`, sau un timeout) sunt reîncercate automat
(`-Retries`, implicit 2, cu retragere `-RetryDelaySeconds`, implicit 20). Dacă un
deployment de model produce frecvent eroarea 429, verificați cota GlobalStandard
TPM a abonamentului (`az cognitiveservices usage list -l <region>`) — creșterea capacității unui
singur deployment nu ajută dacă *cota* abonamentului este epuizată.

## Interpretarea rezultatelor
- `PASS` — caietul a rulat complet fără eroare într-o celulă.
- `FAIL` — este afișat primul rând `*Error` / `*Exception`; deschideți fișierul
  `log_*.txt` corespunzător din directorul de ieșire pentru urmărirea completă a erorii.
- O singură eroare a unui caiet este limitată la `-Timeout` (pe celulă), astfel încât o celulă
  uman-in-the-loop blocată apare ca `StdinNotImplementedError` și nu rămâne blocată.

## Lecții care necesită resurse suplimentare (se așteaptă să eșueze fără ele)
| Lecția | Cerință suplimentară |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, cheie) — are o rută fallback în memorie |
| 11 MCP / GitHub | Server GitHub MCP + PAT |
| 13 memorare (cognee) | `cognee` configurat cu un furnizor de model |
| 15 folosire browser | Browsere Playwright instalate (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 agent local | Runtime Foundry Local + model Qwen descărcat (pe dispozitiv, fără cloud) |
| Caiete `*-dotnet-*` | Kernel .NET Interactive (exclus implicit; folosiți `-IncludeDotnet`) |

## Raportare înapoi
Rezumați într-un tabel PASS/FAIL grupat pe lecție. Separați regresiile reale
(bug-uri de cod/configurație de reparat) de lipsurile din mediu (Search/Foundry Local/PAT lipsă),
și citați `log_*.txt` care eșuează pentru fiecare eșec real.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Declinare a responsabilității**:
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). În timp ce ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un om. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care decurg din utilizarea acestei traduceri.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->