---
name: testing-course-samples
description: Koristite kada se zatraži validacija, testiranje, smoke-test ili pokretanje
  bilježnica i primjera koda tečaja protiv aktivne Microsoft Foundry / Azure OpenAI
  konfiguracije. Obuhvaća postavljanje okruženja (.env, az login, pakete), pokretač
  scripts/validate-notebooks.ps1, tumačenje PASS/FAIL rezultata i koje lekcije zahtijevaju
  dodatne resurse (Azure AI Search, GitHub MCP, Foundry Local, Playwright).
---
# Testiranje Primjera Tečaja

Provjerite rade li bilježnice lekcija i primjeri koda u stvarnoj
Microsoft Foundry / Azure OpenAI postavci. Repozitorij sadrži pokretač u
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) koji
izvršava svaku Python bilježnicu bez glave i ispisuje PASS/FAIL matricu.

## Kada koristiti
- "Provjerite sve bilježnice / primjere u odnosu na moju Azure pretplatu."
- "Provedite osnovni test tečaja nakon nadogradnje paketa ili promjene modela."
- "Koje lekcije još uvijek prolaze / ne uspijevaju uživo?"

**Nemojte** koristiti ovo za AI Smoke Test GitHub Akciju (koja provjerava *postavljene*
hostirane agente — pogledajte [`tests/README.md`](../../../tests/README.md)). Ova vještina
izvršava bilježnice lokalno.

## Preduvjeti (provjerite prvo)
1. **Python 3.12+** s ovisnostima tečaja: `python -m pip install -r requirements.txt`
   plus izvršiteljem: `python -m pip install nbconvert ipykernel`.
2. **`.env` u korijenu repozitorija** (kopirajte iz [`.env.example`](../../../../../.env.example)) s barem:
   - `AZURE_AI_PROJECT_ENDPOINT` — Foundry endpoint projekta
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — ne-deprecirana implementacija (npr. `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) i `AZURE_OPENAI_DEPLOYMENT`
     za lekcije koje izravno pozivaju Azure OpenAI (Lekcija 06, 02-azure-openai, 14 handoff/human-loop).
3. **`az login`** dovršen — primjeri autentificiraju se s `AzureCliCredential` (Entra ID, bez ključa).
4. Provjerite postoji li implementacija modela:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Pokretanje validacije
```powershell
# Sve Python bilježnice (preskače .NET, .venv, site-packages, prijevode, vještine)
pwsh scripts/validate-notebooks.ps1

# Jedna lekcija, s duljim vremenom čekanja po ćeliji
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Samo navedi što bi se izvršilo (bez izvođenja)
pwsh scripts/validate-notebooks.ps1 -List

# Izričiti interpreter (ako `python` nije u PATH-u, npr. Windows Store alias)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
Skripta zapisuje izvršene kopije, dnevnike po bilježnici, i `results.json` u
`$env:TEMP\aiab-nbval` i izlazi s brojem neuspjeha.

Privremene greške (ograničenja HTTP 429 na zajedničkoj pretplati, povremeni
problem s `AzureCliCredential` tokenom ili timeout) automatski se ponavljaju
(`-Retries`, zadano 2, s `-RetryDelaySeconds` odgodom, zadano 20). Ako
implementacija modela redovito daje 429, provjerite GlobalStandard
TPM kvotu pretplate (`az cognitiveservices usage list -l <region>`) — povećanje kapaciteta
pojedinačne implementacije ne pomaže ako je *pretplatnička* kvota iscrpljena.

## Tumačenje rezultata
- `PASS` — bilježnica je izvršena od početka do kraja bez pogreške ćelije.
- `FAIL` — prikazana je prva linija `*Error` / `*Exception`; otvorite odgovarajući
  `log_*.txt` u izlaznom direktoriju za puni trag pogreške.
- Neuspjeh pojedine bilježnice ograničen je s `-Timeout` (po ćeliji), pa se ćelija
  koja čeka na angažman čovjeka prikazuje kao `StdinNotImplementedError` umjesto da visi.

## Lekcije koje trebaju dodatne resurse (očekivano neuspješne bez njih)
| Lekcija | Dodatni zahtjev |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, ključ) — ima alternativni put u memoriji |
| 11 MCP / GitHub | GitHub MCP poslužitelj + PAT |
| 13 memory (cognee) | `cognee` konfiguriran s pružateljem modela |
| 15 browser-use | Instalirani Playwright preglednici (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 lokalni agent | Foundry Local runtime + preuzeti Qwen model (na uređaju, bez oblaka) |
| `*-dotnet-*` bilježnice | .NET Interactive kernel (isključeno prema zadanim postavkama; koristi `-IncludeDotnet`) |

## Izvještavanje nazad
Sažmite kao PASS/FAIL tablicu grupiranu po lekciji. Odvojite stvarne regresije
(programske/konfiguracijske greške za popravak) od nedostataka u okruženju (nedostaje Search/Foundry Local/PAT),
i navedite neuspješne `log_*.txt` za svaki stvarni neuspjeh.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->