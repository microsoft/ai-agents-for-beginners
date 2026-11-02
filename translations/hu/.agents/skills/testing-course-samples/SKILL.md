---
name: testing-course-samples
---
# A tanfolyam mintáinak tesztelése

Ellenőrizze, hogy a leckék jegyzetei és kódmintái működnek-e egy élő
Microsoft Foundry / Azure OpenAI környezettel. A repo tartalmaz egy futtatót a
[`scripts/validate-notebooks.ps1`](../../../../../scripts/validate-notebooks.ps1) útvonalon, amely
fej nélküli futtatással végrehajt minden Python jegyzetfüzetet, és PASS/FAIL mátrixot nyomtat.

## Mikor használjuk
- "Ellenőrizze az összes jegyzetfüzetet / mintát az Azure előfizetésemhez."
- "Futtasson gyors ellenőrzést a tanfolyamon csomagfrissítés vagy modellváltoztatás után."
- "Mely leckék futnak még át / kerülnek hibára élő környezetben?"

Ne használja ezt az AI Smoke Test GitHub Actionhoz (amely a *telepített*
hosztolt ügynököket validálja — lásd [`tests/README.md`](../../../tests/README.md)). Ez a skill
a jegyzetfüzeteket helyben futtatja.

## Előfeltételek (ellenőrizze először)
1. **Python 3.12+** a tanfolyami függőségekkel: `python -m pip install -r requirements.txt`
   továbbá a futtató: `python -m pip install nbconvert ipykernel`.
2. **`.env` a repo gyökérkönyvtárában** (másolja a [`.env.example`](../../../../../.env.example) fájlból) legalább:
   - `AZURE_AI_PROJECT_ENDPOINT` — Foundry projekt végpontja
     (`https://<account>.services.ai.azure.com/api/projects/<project>`)
   - `AZURE_AI_MODEL_DEPLOYMENT_NAME` — egy nem elavult telepítés (pl. `gpt-5-mini`)
   - `AZURE_OPENAI_ENDPOINT` (`https://<account>.openai.azure.com`) és `AZURE_OPENAI_DEPLOYMENT`
     azokhoz a leckékhez, melyek Azure OpenAI-t közvetlenül hívnak (06. lecke, 02-azure-openai, 14 handoff/human-loop).
3. **`az login`** elvégezve — a minták az `AzureCliCredential`-lel hitelesítenek (Entra ID, kulcs nélküli).
4. Ellenőrizze, hogy létezik a modell telepítés:
   `az cognitiveservices account deployment list -g <rg> -n <account> -o table`.

## Az ellenőrzés futtatása
```powershell
# Minden Python jegyzetfüzet (kihagyva: .NET, .venv, site-packages, fordítások, készség erőforrások)
pwsh scripts/validate-notebooks.ps1

# Egyetlen lecke, hosszabb cellánkénti időkorláttal
pwsh scripts/validate-notebooks.ps1 -Filter '08-*' -Timeout 600

# Csak felsorolja, hogy mi futna (nem hajt végre)
pwsh scripts/validate-notebooks.ps1 -List

# Explicit értelmező (ha a `python` nincs a PATH-on, pl. Windows Store alias)
pwsh scripts/validate-notebooks.ps1 -Python "C:/path/to/python.exe"
```
A szkript végrehajtott másolatokat, jegyzetfüzetenkénti naplókat és `results.json` fájlt ír a
`$env:TEMP\aiab-nbval` könyvtárba és a sikertelenek számával lép ki.

Átmeneti hibákat (közös előfizetésből eredő HTTP 429 korlátozások, alkalmi
`AzureCliCredential` token-probléma vagy időtúllépés) automatikusan újrapróbálja
(`-Retries`, alapértelmezett 2, `-RetryDelaySeconds` várakozással, alapértelmezett 20). Ha egy
modell telepítés gyakran 429-et ad vissza, ellenőrizze az előfizetés GlobalStandard
TPM kvótáját (`az cognitiveservices usage list -l <region>`) — egyetlen
telepítés kapacitásának növelése nem segít, ha az *előfizetés* kvóta kimerült.

## Eredmények értelmezése
- `PASS` — a jegyzetfüzet hiba nélkül lefutott végig.
- `FAIL` — az első `*Error` / `*Exception` sor megjelenik; a teljes tracebackhez nyissa meg a
  megfelelő `log_*.txt` fájlt a kimeneti könyvtárban.
- Egyetlen jegyzetfüzet hibája a `-Timeout` idővel korlátozott (cellánként), így egy lefagyott
  human-in-the-loop cella `StdinNotImplementedError` hibát ad vissza a lefagyás helyett.

## Olyan leckék, amelyek extra erőforrásokat igényelnek (ezek hiányában hibára futnak)
| Lecke | Extra követelmény |
|--------|-------------------|
| 05 Agentic RAG | Azure AI Search (`AZURE_SEARCH_SERVICE_ENDPOINT`, kulcs) — van memóriabeli tartalék útvonal |
| 11 MCP / GitHub | GitHub MCP szerver + PAT |
| 13 memória (cognee) | `cognee` konfigurálva modell szolgáltatóval |
| 15 browser-használat | Playwright böngészők telepítve (`playwright install`) + `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` |
| 17 helyi ügynök | Foundry Local futtatókörnyezet + letöltött Qwen modell (helyi eszközön, nem felhőben) |
| `*-dotnet-*` jegyzetfüzetek | .NET Interactive kernel (alapértelmezésben kizárva; használja a `-IncludeDotnet` opciót) |

## Visszajelzés
Összegezze PASS/FAIL táblázatként leckénként csoportosítva. Válassza szét az valódi regressziókat
(javítandó kód/beállítás hibák) a környezeti hiányosságoktól (hiányzó Search/Foundry Local/PAT),
és hivatkozzon a hibás `log_*.txt` fájlokra minden valódi hiba esetén.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->