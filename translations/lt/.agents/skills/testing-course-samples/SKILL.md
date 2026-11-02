---
name: testing-course-samples
---
# Kurso pavyzdžių testavimas

Patikrinkite, ar pamokų užrašų knygelės ir kodo pavyzdžiai veikia su veikia
Microsoft Foundry / Azure OpenAI konfigūracija. Repozitorijoje pateiktas vykdytojas
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1), kuris
vykdo kiekvieną Python užrašų knygelę be sąveikos ir išspausdina PASIŽIŪRĖTI/NEPASIŽIŪRĖTI matricą.

## Kada naudoti
- "Patikrinti visas užrašų knygeles / pavyzdžius pagal mano Azure prenumeratą."
- "Greitas kurso testavimas po paketų atnaujinimo ar modelių keitimo."
- "Kurios pamokos dar veikia / neveikia tiesiogiai?"

**Nenaudokite** to AI Smoke Test GitHub Action (kuris tikrina *diegtus* 
talpinamus agentus — žr. [`tests/README.md`](../../../tests/README.md)). Ši priemonė
paleidžia užrašų knygeles vietoje.

## Išankstiniai reikalavimai (patikrinkite pirmiausia)
1. **Python 3.12+** su kurso priklausomybėmis: `python -m pip install -r requirements.txt`
   + vykdytojui: `python -m pip install nbconvert ipykernel`.
2. **`.env` faile repo šaknyje** (kopijuokite iš [`.env.example`](../../../../../.env.example)) turi būti bent:
   - `AZURE_AI_PROJECT_ENDPOINT` — Foundry projekto galinis taškas
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — nepasenęs diegimas (pvz., `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) ir `AZURE_OPENAI_DEPLOYMENT`
     pamokoms, kurios tiesiogiai naudoja Azure OpenAI (06 pamoka, 02-azure-openai, 14 perdavimas/žmogaus ciklas).
3. Atliktas **`az login`** — pavyzdžiai autentifikuojasi su `AzureCliCredential` (Entra ID, be rakto).
4. Patikrinkite, ar modelio diegimas egzistuoja:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Tikrinimo vykdymas
```powershell
# Visi Python užrašų knygelės (neįtraukia .NET, .venv, site-packages, vertimų, įgūdžių išteklių)
pwsh scripts/validate-notebooks.ps1

# Viena pamoka su ilgesniu laiko limitu kiekvienai ląstelei
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Tik surašyti, kas būtų vykdoma (vykdymas nevykdomas)
pwsh scripts/validate-notebooks.ps1 -List

# Aiškus interpretatorius (jei `python` nėra PATH, pvz., Windows Store alias)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
Skriptas įrašo vykdomas kopijas, kiekvienos užrašų knygelės žurnalus ir `results.json` į
`$env:TEMP\aiab-nbval` ir išeina su nepavykusių skaičiumi.

Laikini nesėkmingi bandymai (bendros prenumeratos HTTP 429 ribos, kartais
`AzureCliCredential` tokeno klaidos ar timeout) automatiškai bandomi iš naujo
(`-Retries`, numatyta 2, su `-RetryDelaySeconds` pauze, numatyta 20). Jei
modelio diegimas nuolat sukelia 429 klaidą, patikrinkite prenumeratos GlobalStandard
TPM kvotą (`az cognitiveservices usage list -l <region>`) — atskirai didinant vieno
diegimo pajėgumą nepadeda, kai išeikvota *prenumeratos* kvota.

## Rezultatų interpretacija
- `PASS` — užrašų knygelė prabėgo nuo pradžios iki galo be klaidų.
- `FAIL` — rodoma pirmoji `*Error` / `*Exception` eilutė; atidarykite atitinkamą
  `log_*.txt` išvesties kataloge, kad matytumėte pilną klaidos seką.
- Vienos užrašų knygelės nesėkmė ribojama `-Timeout` (vienam langeliui), todėl
  pakibusį žmogaus ciklo langelį pakeičia `StdinNotImplementedError`, o ne pakimba.

## Pamokos, kurioms reikalingi papildomi ištekliai (tikėtina, kad nepavyks be jų)
| Pamoka | Papildomi reikalavimai |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, raktas) — turi atminties atsarginį kelią |
| 11 MCP / GitHub | GitHub MCP serveris + PAT |
| 13 atmintis (cognee) | `cognee` sukonfigūruotas su modelio tiekėju |
| 15 naršyklės naudojimas | Įdiegti Playwright naršyklės (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 vietinis agentas | Foundry Local vykdymo aplinka + atsisiųstas Qwen modelis (vietoje, be debesies) |
| `*-dotnet-*` užrašų knygelės | .NET Interactive branduolys (pagal nutylėjimą išimtas; naudokite `-IncludeDotnet`) |

## Ataskaitos grąžinimas
Apibendrinkite PASIŽIŪRĖTI/NEPASIŽIŪRĖTI lentelę suskirstytą pagal pamokas. Atskirai nurodykite tikras regresijas
(kodo / konfigūracijos klaidas) nuo aplinkos trūkumų (neprieinamos Search/Foundry Local/PAT),
ir paminėkite raspiančius `log_*.txt` failus kiekvienam tikram nesklandumui.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->