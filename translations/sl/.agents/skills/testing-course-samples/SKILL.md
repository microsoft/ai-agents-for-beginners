---
name: testing-course-samples
---
# Testiranje vzorcev tečaja

Preverite, ali se zvezki lekcij in vzorčni kodi izvajajo v živo
okolju Microsoft Foundry / Azure OpenAI. V skladišču je zaganjalnik
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1), ki
izvaja vse Python zvezke brez glave in izpiše PASS/FAIL matriko.

## Kdaj uporabljati
- "Preverite vse zvezke / vzorce z mojim naročniškim računom Azure."
- "Osnovno testiranje tečaja po nadgradnji paketov ali spremembah modelov."
- "Katere lekcije še vedno uspešno / neuspešno delujejo v živo?"

Ne uporabljajte tega za GitHub akcijo AI Smoke Test (ki preverja *delo* 
gostujočih agentov — glej [`tests/README.md`](../../../tests/README.md)). Ta funkcija
zažene zvezke lokalno.

## Predpogoji (najprej preverite)
1. **Python 3.12+** s potrebnimi elementi tečaja: `python -m pip install -r requirements.txt`
   ter izvajalnik: `python -m pip install nbconvert ipykernel`.
2. **`.env` v korenu skladišča** (kopirajte iz [`.env.example`](../../../../../.env.example)) vsaj z:
   - `AZURE_AI_PROJECT_ENDPOINT` — končna točka projekta Foundry
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — ne-odslužena postavitev (npr. `gpt-4.1-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) in `AZURE_OPENAI_DEPLOYMENT`
     za lekcije, ki kličejo Azure OpenAI neposredno (Lekcija 06, 02-azure-openai, 14 handoff/human-loop).
3. Opravljen **`az login`** — vzorci se avtenticirajo z `AzureCliCredential` (Entra ID, brez ključa).
4. Preverite obstoj postavitve modela:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Zagon preverjanja
```powershell
# Vse Python zvezke (preskoči .NET, .venv, site-packages, prevode, viri veščin)
pwsh scripts/validate-notebooks.ps1

# Ena lekcija, z daljšim časom poteka na posamezno celico
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Samo izpiši, kaj bi se izvajalo (brez izvedbe)
pwsh scripts/validate-notebooks.ps1 -List

# Izrecen tolmač (če `python` ni v PATH, npr. Windows Store alias)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
 Skripta zapisuje izvršene kopije, dnevnike po zvezkih in `results.json` v
`$env:TEMP\aiab-nbval` ter izstopi s številom napak.

## Interpretacija rezultatov
- `PASS` — zvezek se je zagnal od začetka do konca brez napake v celici.
- `FAIL` — prikazana je prva vrstica z `*Error` / `*Exception`; za celotno sledenje napaki
  odprite ustrezno datoteko `log_*.txt` v izhodni mapi.
- Neuspeh posameznega zvezka je omejen z `-Timeout` (na celico), zato zasedena
  celica, kjer je potreben človek v zanki, prikaže `StdinNotImplementedError` namesto zastoja.

## Lekcije, ki zahtevajo dodatne vire (pričakovane napake brez njih)
| Lekcija | Dodatna zahteva |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, ključ) — ima pot za izhod v primeru pomanjkanja pomnilnika |
| 11 MCP / GitHub | GitHub MCP strežnik + PAT |
| 13 pomnilnik (cognee) | `cognee` konfiguriran z dobaviteljem modela |
| 15 brskalnik uporaba | Nameščeni brskalniki Playwright (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 lokalni agent | Foundry Local runtime + prenesen model Qwen (na napravi, brez oblaka) |
| `*-dotnet-*` zvezki | Jedro .NET Interactive (privzeto izključeno; uporabite `-IncludeDotnet`) |

## Poročanje nazaj
Povzemite v tabeli PASS/FAIL združeni po lekcijah. Ločite prave regresije
(napake kode/konfiguracije za popravilo) od pomanjkanja okolja (manjkajoči Search/Foundry Local/PAT),
in navajajte neuspešne `log_*.txt` za vsako resnično napako.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->