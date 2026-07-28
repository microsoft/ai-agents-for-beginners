---
name: testing-course-samples
---
# Kursuse näidete testimine

Kontrolli, kas õppetunni märkmikud ja koodinäited töötavad otse
Microsoft Foundry / Azure OpenAI keskkonnas. Repos on kaasas käivitaja fail
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1), mis
käivitab kõik Python märkmikud ilma kasutajaliideseta ja kuvab Läbi/Ebaõnnestus tabeli.

## Millal kasutada
- "Kontrolli kõiki märkmikke / näiteid minu Azure tellimuse peal."
- "Tee kursuse suitsetest pärast pakettide uuendamist või mudelite muutmist."
- "Millised õppetunnid töötavad või ebaõnnestuvad otse?"

Ära kasuta seda AI suitsetesti GitHub Actioni jaoks (mis kontrollib *paigaldatud*
teenuseid — vaata [`tests/README.md`](../../../tests/README.md)). See oskus
käivitab märkmikud kohapeal.

## Eeldused (esiteks kontrolli)
1. **Python 3.12+** koos kursuse sõltuvustega: `python -m pip install -r requirements.txt`
   pluss käitaja: `python -m pip install nbconvert ipykernel`.
2. **`.env` fail repo juurikas** (kopeerida [`.env.example`](../../../../../.env.example)) vähemalt järgmistega:
   - `AZURE_AI_PROJECT_ENDPOINT` — Foundry projekti lõpp-punkt
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — mitte-vananenud juurutus (nt `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) ja `AZURE_OPENAI_DEPLOYMENT`
     õppetundide jaoks, mis kutsuvad Azure OpenAI otse (Lesson 06, 02-azure-openai, 14 handoff/human-loop).
3. **`az login`** tehtud — näited autentivad `AzureCliCredential` abil (Entra ID, ilma võtmeta).
4. Kontrolli, et mudeli juurutus eksisteerib:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Kinnituse jooksutamine
```powershell
# Kõik Pythoni märkmikud (välja arvates .NET, .venv, site-packages, tõlked, oskuste ressursid)
pwsh scripts/validate-notebooks.ps1

# Üksik õppetund, pikema rakuraku aikaviitega
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Loetle lihtsalt, mis tööle pandaks (ilma täitmiseta)
pwsh scripts/validate-notebooks.ps1 -List

# Selgesõnaline interpreter (kui `python` ei ole PATH-is, nt Windows Store-i aliase puhul)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
 Skript kirjutab täidetud koopiad, märkmiku-põhised logid ja `results.json` asukohta
`$env:TEMP\aiab-nbval` ning väljub ebaõnnestumiste arvuga.

Ajutised vead (jagunatud tellimuse HTTP 429 kiirusepiirangud, mõni
`AzureCliCredential` tokeni tõrge või aegumine) proovitakse automaatselt uuesti
(`-Retries`, vaikimisi 2, koos `-RetryDelaySeconds` tagasilangemisega, vaikimisi 20). Kui
mudeli juurutus annab pidevalt 429, kontrolli tellimuse GlobalStandard
TPM kvooti (`az cognitiveservices usage list -l <region>`) — ühe
juurutuse võimsuse tõstmine ei aita, kui *tellimuse* kvoot on ammendatud.

## Tulemuste tõlgendamine
- `PASS` — märkmik jooksis lõpuni ilma lahtrivigadeta.
- `FAIL` — kuvatakse esimene `*Error` / `*Exception` rida; ava sobiv
  `log_*.txt` väljundkaustas täispildi jaoks.
- Ühe märkmiku ebaõnnestumine on piiratud `-Timeout`-ga (lahtri kohta), nii et kinni jäänud
  inimese kaasamise lahter näitab `StdinNotImplementedError` asemel kinni püsimist.

## Õppetunnid, mis vajavad lisavahendeid (eeldatav ebaõnnestumine ilma nendeta)
| Õppetund | Lisaväli |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, võti) — sisaldab mälupõhist varuvõimalust |
| 11 MCP / GitHub | GitHub MCP server + PAT |
| 13 mälu (cognee) | `cognee` konfigureeritud mudelipakkujaga |
| 15 brauseri kasutus | Playwright brauserid paigaldatud (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 kohalik agent | Foundry Local runtime + alla laetud Qwen mudel (seadmel, mitte pilves) |
| `*-dotnet-*` märkmikud | .NET Interactive kernel (vaikimisi välja jäetud; kasuta `-IncludeDotnet`) |

## Tagasiside andmine
Võta kokku Läbi/Ebaõnnestus tabelina rühmitatuna õppetunni järgi. Eralda tegelikud regressioonid
(koodi/konfiguratsiooni vead, mida parandada) keskkonna puudujääkidest (puuduvad Search/Foundry Local/PAT),
ning tsiteeri iga reaalse ebaõnnestumise korral `log_*.txt` faili.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->