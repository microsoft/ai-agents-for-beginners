---
name: testing-course-samples
---
# Kurso pavyzdžių testavimas

Patikrinkite, ar pamokų užrašų knygelės ir kodo pavyzdžiai veikia su tiesiogine
Microsoft Foundry / Azure OpenAI aplinka. Repozitorijoje yra vykdytojas
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1), kuris
be vartotojo sąsajos vykdo kiekvieną Python užrašų knygelę ir išveda PRABĖGĖ / NEPRABĖGĖ matricą.

## Kada naudoti
- "Patikrinti visas užrašų knygeles / pavyzdžius su mano Azure prenumerata."
- "Greitai patikrinti kursą po paketų atnaujinimo ar modelių pakeitimų."
- "Kurios pamokos vis dar veikia / neveikia tiesiogiai?"

**Nenaudokite** šio testavimo metodui AI Smoke Test GitHub Action (kuris tikrina *diegiamus*
talpinamus agentus — žr. [`tests/README.md`](../../../tests/README.md)). Šis įgūdis
vykdo užrašų knygeles lokaliai.

## Išankstiniai reikalavimai (pirmiausia patikrinkite)
1. **Python 3.12+** su kurso priklausomybėmis: `python -m pip install -r requirements.txt`
   ir vykdytojas: `python -m pip install nbconvert ipykernel`.
2. **`.env` failas repozitorijos šaknyje** (nukopijuokite iš [`.env.example`](../../../../../.env.example)) turint bent:
   - `AZURE_AI_PROJECT_ENDPOINT` — Foundry projekto endpoint'as
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — nebenaudojama diegimo versija (pvz., `gpt-4.1-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) ir `AZURE_OPENAI_DEPLOYMENT`
     pamokoms, kurios tiesiogiai kviečia Azure OpenAI (Pamoka 06, 02-azure-openai, 14 handoff/human-loop).
3. Įvykdyta **`az login`** — pavyzdžiai autentifikuojasi su `AzureCliCredential` (Entra ID, be rakto).
4. Patikrinkite, ar modelio diegimas yra:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Vykdyti patikrinimą
```powershell
# Visos Python užrašų knygelės (išskyrus .NET, .venv, site-packages, vertimus, įgūdžių turtą)
pwsh scripts/validate-notebooks.ps1

# Viena pamoka, su ilgesniu laiko limitu kiekvienai ląstelei
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Tik išvardinti, kas būtų vykdoma (be vykdymo)
pwsh scripts/validate-notebooks.ps1 -List

# Aiškus interpretatorius (jei `python` nėra PATH, pvz., Windows Store alias)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
Skriptas įrašo vykdomas kopijas, per užrašų knygelę žurnalus ir `results.json`
į `$env:TEMP\aiab-nbval` ir išeina su nepraėjusių skaičiumi.

## Rezultatų interpretavimas
- `PASS` — užrašų knygelė buvo įvykdyta nuosekliai be klaidų langeliuose.
- `FAIL` — rodoma pirmoji `*Error` / `*Exception` eilutė; pilną klaidos aprašymą žr.
  atitinkamame `log_*.txt` faile išvesties kataloge.
- Vienos užrašų knygelės nepavykimas ribojamas `-Timeout` (kiekvienam langeliui), todėl užstrigęs
  žmogaus įsikišimo langelis matomas kaip `StdinNotImplementedError`, o ne užstringa.

## Pamokos, kurioms reikalingi papildomi ištekliai (joms be jų testas turi nepavykti)
| Pamoka | Papildomas reikalavimas |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, raktas) — turi atminties pakaitos kelią |
| 11 MCP / GitHub | GitHub MCP serveris + PAT |
| 13 atmintis (cognee) | `cognee` sukonfigūruotas su modelių tiekėju |
| 15 naršyklės naudojimas | Įdiegti Playwright naršyklės (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 vietinis agentas | Foundry vietinis vykdymas + atsisiųstas Qwen modelis (vietoje, be debesies) |
| `*-dotnet-*` užrašų knygelės | .NET Interactive branduolys (pagal nutylėjimą neįtrauktas; naudokite `-IncludeDotnet`) |

## Atsiskaitymas
Apibendrinkite PASS/FAIL lentelę sugrupuotą pagal pamoką. Atskirai pažymėkite tikrus regresus
(kodo/konfigūracijos klaidas, kurias reikia ištaisyti) nuo aplinkos trūkumų (trūksta Search/Foundry Local/PAT),
ir nurodykite nepraėjusių atvejų `log_*.txt` failus.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->