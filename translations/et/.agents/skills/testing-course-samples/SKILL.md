---
name: testing-course-samples
---
# Kursuse näidiste testimine

Kontrolli, et õppetunni märkmikud ja koodinäited töötaksid elava
Microsoft Foundry / Azure OpenAI seadistuse vastu. Repo sisaldab käivitajat
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1), mis
käivitab iga Python märkmiku pealetükkimata ja kuvab ÕNNESTUS/EBAPÄRITUSED maatriksi.

## Millal kasutada
- "Kontrolli kõiki märkmikke / näiteid minu Azure tellimuse vastu."
- "Tee kursuse suitsutest pärast pakettide uuendamist või mudelite muutmist."
- "Millised õppetunnid veel lähevad läbi / ebaõnnestuvad reaalajas?"

Ära kasuta seda AI suitsutesti GitHub Actioni jaoks (mis kontrollib *paigaldatud*
hostitud agente — vaata [`tests/README.md`](../../../tests/README.md)). See oskus
käivitab märkmikud kohapeal.

## Eeltingimused (kontrolli esmalt)
1. **Python 3.12+** koos kursuse sõltuvustega: `python -m pip install -r requirements.txt`
   pluss täitja: `python -m pip install nbconvert ipykernel`.
2. **`.env` repo juures** (kopeeri [`.env.example`](../../../../../.env.example)) vähemalt:
   - `AZURE_AI_PROJECT_ENDPOINT` — Foundry projekti otsapunkt
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — mitte-aegunud paigaldus (nt `gpt-4.1-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) ja `AZURE_OPENAI_DEPLOYMENT`
     õppetundidele, mis kutsuvad Azure OpenAI otse (Õppetund 06, 02-azure-openai, 14 handoff/human-loop).
3. **`az login`** lõpetatud — näited tõendavad `AzureCliCredential` abil (Entra ID, ilma võtmeta).
4. Kinnita, et mudeli paigaldus on olemas:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Valideerimise käivitamine
```powershell
# Kõik Pythoni märkmikud (väldib .NET, .venv, site-packages, tõlked, oskuste varad)
pwsh scripts/validate-notebooks.ps1

# Üksik õppetund, pikema ajapiiranguga per-rakk
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Loetle lihtsalt, mis käivitatakse (ilma täitmiseta)
pwsh scripts/validate-notebooks.ps1 -List

# Selgesõnaline tõlgendi määramine (kui `python` ei ole PATH-is, nt Windows Store'i alias)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
Skript kirjutab täidetud koopiad, märkmiku kohta logid ja `results.json` aadressile
`$env:TEMP\aiab-nbval` ning väljub nurjumiste arvuga.

## Tulemuste tõlgendamine
- `PASS` — märkmik töötas lõpuni ilma rakkude vigadeta.
- `FAIL` — kuvatakse esimene `*Error` / `*Exception` rida; täieliku jäljeraja saamiseks ava sobiv
  `log_*.txt` väljundkaustas.
- Üksiku märkmiku nurjumist piirab `-Timeout` (per rakk), nii et ummikusse jäänud
  inim-tsükkel ilmneb `StdinNotImplementedError`-na, mitte ei külmuta skripti.

## Õppetunnid, millel on lisavajadused (ilma nendeta eeldatav nurjumine)
| Õppetund | Lisanõue |
|--------|----------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, võti) — on mäluühendusega tagavararada |
| 11 MCP / GitHub | GitHub MCP server + PAT |
| 13 mälu (cognee) | `cognee` konfigureeritud mudelite pakkujaga |
| 15 brauserikasutus | Playwrighti brauserid installitud (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 kohalik agent | Foundry Local käitusaeg + alla laetud Qwen mudel (seadmes, ilma pilveta) |
| `*-dotnet-*` märkmikud | .NET Interactive kernel (vaikimisi välja jäetud; kasuta `-IncludeDotnet`) |

## Tagasiside andmine
Võta kokku ÕNNESTUS/EBAPÄRITUSED tabelina, rühmitatuna õppetunni kaupa. Eristada ehtsaid regressioone
(parandamist vajavaid koodi/konfiguratsiooni vigu) keskkonnatühikutest (puuduvad Search/Foundry Local/PAT),
ning viidata iga tegeliku nurjumise korral vastavale `log_*.txt` failile.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->