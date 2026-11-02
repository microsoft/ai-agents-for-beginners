---
name: testing-course-samples
description: "Use when asked to validate, test, smoke-test, or run the course's notebook and code samples against a live Microsoft Foundry / Azure OpenAI configuration. Covers environment setup (.env, az login, packages), the scripts/validate-notebooks.ps1 runner, interpreting PASS/FAIL results, and which lessons need extra resources (Azure AI Search, GitHub MCP, Foundry Local, Playwright)."
---
# Kurssinäytteiden testaaminen

Varmista, että oppituntien muistiinpanot ja koodinäytteet toimivat live-
Microsoft Foundry / Azure OpenAI -ympäristössä. Repossa on runner osoitteessa
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1), joka
suorittaa kaikki Python-muistiinpanot ilman käyttöliittymää ja tulostaa PASS/FAIL-matriisin.

## Milloin käyttää
- "Varmista, että kaikki muistiinpanot / näytteet toimivat Azure-tilauksessani."
- "Tee savutesti kurssille päivitysten tai mallien vaihdon jälkeen."
- "Mitkä oppitunnit läpäisevät / epäonnistuvat livenä?"

Älä käytä tätä AI Smoke Test -GitHub-toiminnossa (joka validoi *asennetut*
isännöidyt agentit — katso [`tests/README.md`](../../../tests/README.md)). Tämä taito
suorittaa muistiinpanot paikallisesti.

## Esivaatimukset (tarkista ensin)
1. **Python 3.12+** kurssin riippuvuuksilla: `python -m pip install -r requirements.txt`
   plus suoritin: `python -m pip install nbconvert ipykernel`.
2. **`.env` repossa juuressa** (kopioi [`.env.example`](../../../../../.env.example)) vähintään:
   - `AZURE_AI_PROJECT_ENDPOINT` — Foundry-projektin päätepiste
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — ei vanhentunut käyttöönotto (esim. `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) ja `AZURE_OPENAI_DEPLOYMENT`
     oppitunneille, jotka kutsuvat Azure OpenAI:ta suoraan (Oppitunti 06, 02-azure-openai, 14 handoff/human-loop).
3. **`az login`** suoritettu — näytteet todennetaan `AzureCliCredential` (Entra ID, avaineton).
4. Varmista, että mallin käyttöönotto on olemassa:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Vahvistuksen suorittaminen
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
Skripti kirjoittaa suoritetut kopiot, muistiinpanokohtaiset lokit ja `results.json` osoitteeseen
`$env:TEMP\aiab-nbval` ja sulkeutuu epäonnistumisten lukumäärällä.

Tilapäiset epäonnistumiset (jaetut-tilaus HTTP 429 -rajoitukset, satunnainen
`AzureCliCredential` tokenin ongelma tai aikakatkaisu) yritetään automaattisesti uudelleen
(`-Retries`, oletus 2, `-RetryDelaySeconds` takaisinkytkennällä, oletus 20). Jos
mallin käyttöönotto saa usein 429-virheitä, tarkista tilauksen GlobalStandard
TPM-quota (`az cognitiveservices usage list -l <region>`) — yhden
käyttöönoton kapasiteetin nostaminen ei auta, jos *tilauksen* quota on loppu.

## Tulosten tulkinta
- `PASS` — muistiinpano suoritettiin loppuun ilman solun virheitä.
- `FAIL` — ensimmäinen `*Error` / `*Exception` rivi näytetään; avaa vastaava
  `log_*.txt` tulostehakemistossa täydelliseen virhejäljitykseen.
- Yhden muistiinpanon epäonnistuminen rajataan `-Timeout` mukaan (solua kohti), joten jumissa oleva
  human-in-the-loop -solu näkyy `StdinNotImplementedError` eikä jää jumiin.

## Oppitunnit, jotka tarvitsevat lisäresursseja (epäonnistuvat ilman niitä)
| Oppitunti | Lisävaatimus |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, avain) — sisältää muistissa toimivan varareitin |
| 11 MCP / GitHub | GitHub MCP -palvelin + PAT |
| 13 muisti (cognee) | `cognee` asetettu mallin tarjoajalla |
| 15 selain-käyttö | Playwright-selaimet asennettuna (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 paikallinen agentti | Foundry Local runtime + ladattu Qwen-malli (laitteella, ei pilvessä) |
| `*-dotnet-*` muistiinpanot | .NET Interactive kernel (pois oletuksena; käytä `-IncludeDotnet`) |

## Raportointi
Tee yhteenveto PASS/FAIL-taulukkona oppitunnittain ryhmiteltynä. Erittele aidot takaiskset
(korjattavat koodi-/konfiguraatiovirheet) ympäristöpuutteista (puuttuvat Search/Foundry Local/PAT),
ja ilmoita epäonnistuneesta `log_*.txt` jokaisessa todellisessa epäonnistumisessa.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä on virallinen lähde. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->