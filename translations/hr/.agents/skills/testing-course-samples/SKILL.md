---
name: testing-course-samples
---
# Testiranje primjera tečaja

Provjerite rade li bilježnice lekcija i primjeri koda uz aktivno
Microsoft Foundry / Azure OpenAI okruženje. Repo dolazi s izvršiteljem na
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) koji
izvodi svaku Python bilježnicu bez sučelja i ispisuje PASS/FAIL matricu.

## Kada koristiti
- "Provjeriti sve bilježnice / primjere uz moju Azure pretplatu."
- "Brzi test tečaja nakon nadogradnje paketa ili promjene modela."
- "Koje lekcije i dalje prolaze / padaju uživo?"

**Ne** koristite ovo za AI Smoke Test GitHub akciju (koja provjerava *deployane* 
hostirane agente — vidi [`tests/README.md`](../../../tests/README.md)). Ova vještina
izvršava bilježnice lokalno.

## Preduvjeti (prvo provjerite)
1. **Python 3.12+** s ovisnostima tečaja: `python -m pip install -r requirements.txt`
   plus izvršitelj: `python -m pip install nbconvert ipykernel`.
2. **`.env` u korijenu repozitorija** (kopirati iz [`.env.example`](../../../../../.env.example)) s najmanje:
   - `AZURE_AI_PROJECT_ENDPOINT` — foundry projektna krajnja točka
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — aktivno postavljena verzija (npr. `gpt-4.1-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) i `AZURE_OPENAI_DEPLOYMENT`
     za lekcije koje koriste Azure OpenAI direktno (Lekcija 06, 02-azure-openai, 14 handoff/human-loop).
3. **`az login`** izvršen — primjeri se autentificiraju s `AzureCliCredential` (Entra ID, bez ključa).
4. Provjerite postoji li konfiguracija modela:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Izvršavanje provjere
```powershell
# Sve Python bilježnice (izostavlja .NET, .venv, site-packages, prijevode, vještine resurse)
pwsh scripts/validate-notebooks.ps1

# Jedna lekcija, s dužim timeout-om po ćeliji
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Samo navedi što bi se pokrenulo (bez izvršavanja)
pwsh scripts/validate-notebooks.ps1 -List

# Izričiti interpretator (ako `python` nije u PATH-u, npr. Windows Store alias)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
Skripta zapisuje izvršene kopije, zapisnike po bilježnicama i `results.json` u
`$env:TEMP\aiab-nbval` te se zaustavlja s brojem neuspjeha.

## Tumačenje rezultata
- `PASS` — bilježnica je izvršena u cijelosti bez pogreške u ćeliji.
- `FAIL` — prikazuje se prva `*Error` / `*Exception` linija; otvorite odgovarajući
  `log_*.txt` u izlaznom direktoriju za puni traceback.
- Neuspjeh jedne bilježnice ograničen je s `-Timeout` (po ćeliji), pa se zaglavljivanje
  human-in-the-loop ćelije prikazuje kao `StdinNotImplementedError` umjesto da se blokira.

## Lekcije koje zahtijevaju dodatne resurse (očekivano je da bez njih padnu)
| Lekcija | Dodatni zahtjev |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, ključ) — ima fallback put u memoriji |
| 11 MCP / GitHub | GitHub MCP server + PAT |
| 13 memorija (cognee) | `cognee` konfiguriran s pružateljem modela |
| 15 browser-use | Instalirani Playwright preglednici (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 lokalni agent | Foundry Local runtime + skinuti Qwen model (lokalno na uređaju, bez clouda) |
| `*-dotnet-*` bilježnice | .NET Interactive kernel (isključeno prema zadanim postavkama; koristi `-IncludeDotnet`) |

## Izvještavanje nazad
Sažmite kao PASS/FAIL tablicu grupiranu po lekciji. Razdvojite prave regresije
(bugove u kodu/konfiguraciji za popravak) od nedostataka u okruženju (nedostaje Search/Foundry Local/PAT),
i navedite neuspjele `log_*.txt` zapise za svaki stvarni neuspjeh.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->