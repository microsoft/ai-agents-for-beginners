# AGENTS.md

## Projekt áttekintése

Ez a tároló a "Kezdőknek szóló AI Ügynökök" nevű átfogó oktató tanfolyamot tartalmazza, amely mindent megtanít, ami az AI ügynökök létrehozásához szükséges. A tanfolyam 18 leckéből áll (számozva 00-18), amelyek az alapokat, a tervezési mintákat, a keretrendszereket, a termelési bevezetést, a helyi/készüléken futó ügynököket és az AI ügynökök biztonságát fedik le.

**Kulcs technológiák:**
- Python 3.12+
- Jupyter Notebook-ok az interaktív tanuláshoz
- AI keretrendszerek: Microsoft Agent Framework (MAF)
- Azure AI szolgáltatások: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Architektúra:**
- Leckékre bontott struktúra (00-18 könyvtárak)
- Minden lecke tartalmaz: README dokumentációt, kódpéldákat (Jupyter notebook-ok) és képeket
- Többnyelvű támogatás automatizált fordítási rendszerrel
- Egy Python notebook leckénként a Microsoft Agent Framework használatával

## Telepítési parancsok

### Előfeltételek
- Python 3.12 vagy újabb
- Azure előfizetés (Microsoft Foundry használatához)
- Azure CLI telepítve és hitelesítve (`az login`)

### Kezdeti beállítás

1. **Klónozza vagy fork-olja a tárolót:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Hozza létre és aktiválja a Python virtuális környezetet:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Telepítse a függőségeket:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Állítsa be a környezeti változókat:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### Szükséges környezeti változók

A **Microsoft Foundry** esetén (kötelező):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry projekt végpontja
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Modell telepítésének neve (pl. gpt-5-mini)

Az **Azure AI Search** esetén (05-ös lecke - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search végpont
- `AZURE_SEARCH_API_KEY` - Azure AI Search API kulcs

Hitelesítés: Futtassa a `az login` parancsot a notebook-ok futtatása előtt (a `AzureCliCredential`-t használja).

## Fejlesztési munkafolyamat

### Jupyter Notebook-ok futtatása

Minden lecke több Jupyter notebook-ot tartalmaz különböző keretrendszerekhez:

1. **Indítsa el a Jupyter-t:**
   ```bash
   jupyter notebook
   ```

2. **Navigáljon a lecke könyvtárába** (pl. `01-intro-to-ai-agents/code_samples/`)

3. **Nyissa meg és futtassa a notebook-okat:**
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework használata (Python)
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework használata (.NET)

### Munka a Microsoft Agent Framework-kel

**Microsoft Agent Framework + Microsoft Foundry:**
- Azure előfizetés szükséges
- `FoundryChatClient` használata az Agent Service V2-hez (az ügynökök láthatók a Foundry portálon)
- Termelésre kész beépített megfigyelhetőséggel
- Fájlnév minta: `*-python-agent-framework.ipynb`

## Tesztelési utasítások

Ez egy oktatási adattár példakódokkal, nem termelési kód automata tesztekkel. A beállítás és a változtatások ellenőrzéséhez:

### Manuális tesztelés

1. **Python környezet tesztelése:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Jupyter notebook futtatás tesztelése:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Környezeti változók ellenőrzése:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Egyéni notebookok futtatása

Nyisd meg a notebookokat Jupyter-ben és futtass sorrendben cellákat. Minden notebook önálló és tartalmaz:
- Import utasításokat
- Konfiguráció betöltést
- Példa agent implementációkat
- Várható kimenetek markdown cellákban

### Ügynökök telepítés utáni alapvető tesztelése (“smoke-testing”)

Azokon a leckéken, ahol az agent Microsoft Foundry által üzemeltetett agentként van telepítve (01, 04, 05, 16), az adattár smoke-test katalógusokat tartalmaz az `tests/` alatt, amelyeket az `.github/workflows/smoke-test.yml` workflow futtat a [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) akción keresztül. Ezek egy könnyű, telepítés utáni ellenőrző kapuk (elérhető-e az ügynök és követi-e az alap prompteket?), kiegészítve a 10. és 16. leckék értékelő csatornáját. Lásd a [tests/README.md](./tests/README.md) a katalógus-lecke-agent hozzárendeléshez. A 17. lecke helyileg fut Foundry Local-lal és nincs távoli végpontja, így annak notebookját közvetlenül futtatva ellenőrzik.

## Kódstílus

### Python konvenciók

- **Python verzió**: 3.12+
- **Kódstílus**: Kövesd a standard Python PEP 8 szokásokat
- **Notebookok**: Használj tiszta markdown cellákat a koncepciók magyarázatához
- **Importok**: Csoportosítsd standard könyvtárak, harmadik féltől és helyi importokra

### Jupyter Notebook konvenciók

- Tartalmazz leíró markdown cellákat a kód cellák előtt
- Adj példákat kimenetekre a notebookokban hivatkozásként
- Használj egyértelmű változóneveket, amelyek megfelelnek a lecke fogalmainak
- Tartsd a notebook futtatási sorrendet lineárisan (cellák 1 → 2 → 3...)

### Fájlok szervezése

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Fordítás és Telepítés

### Dokumentáció készítése

Az adattár Markdown-t használ dokumentációhoz:
- README.md fájlok minden lecke mappában
- Fő README.md az adattár gyökerében
- Automatikus fordítási rendszer GitHub Actions használatával

### CI/CD folyamat

A helye: `.github/workflows/`

1. **co-op-translator.yml** - Automatikus fordítás 50+ nyelvre
2. **welcome-issue.yml** - Üdvözli az új issue szerzőket
3. **welcome-pr.yml** - Üdvözli az új pull request hozzájárulókat

### Telepítés

Ez oktatási adattár - nincs telepítési folyamat. Felhasználók:
1. Forkolják vagy klónozzák az adattárat
2. Futtatják a notebookokat helyileg vagy GitHub Codespaces-ben
3. Tanulnak példák módosításával és kísérletezéssel

## Pull Request irányelvek

### Beküldés előtt

1. **Teszteld a változtatásokat:**
   - Futtasd végig az érintett notebookokat teljesen
   - Ellenőrizd, hogy minden cella hiba nélkül fut
   - Nézd meg, hogy a kimenetek megfelelőek

2. **Dokumentáció frissítése:**
   - Frissítsd a README.md fájlokat, ha új fogalmakat adsz hozzá
   - Írj kommenteket a notebookokban a bonyolult kódhoz
   - Gondoskodj arról, hogy a markdown cellák magyarázzák a célt

3. **Fájl változtatások:**
   - Kerüld az `.env` fájlok commitálását (használj `.env.example`)
   - Ne commitálj `venv/` vagy `__pycache__/` könyvtárakat
   - Tartsd meg a notebook kimeneteket, ha azok koncepciókat demonstrálnak
   - Távolítsd el az ideiglenes fájlokat és biztonsági mentési notebookokat (`*-backup.ipynb`)

### PR cím formátum

Használj leíró címeket:
- `[Lesson-XX] Add new example for <concept>`
- `[Fix] Correct typo in lesson-XX README`
- `[Update] Improve code sample in lesson-XX`
- `[Docs] Update setup instructions`

### Kötelező ellenőrzések

- A notebookoknak hiba nélkül kell futniuk
- A README fájloknak tisztának és pontosnak kell lenniük
- Kövesd az adattár meglévő kód mintáit
- Tartsd meg a konzisztenciát a többi leckével

## További megjegyzések

### Gyakori hibák

1. **Python verzió eltérés:**
   - Biztosítsd, hogy Python 3.12+ van használatban
   - Egyes csomagok nem működnek régebbi verziókon
   - Használd `python3 -m venv` a Python verzió explicit megadásához

2. **Környezeti változók:**
   - Mindig hozz létre `.env` `.env.example`-ből
   - Ne commitáld az `.env` fájlt (az `.gitignore` alatt van)
   - Jelentkezz be `az login`-vel kulcs nélküli Entra ID hitelesítéshez

3. **Csomag ütközések:**
   - Használj új virtuális környezetet
   - Telepíts a `requirements.txt` segítségével, ne egyes csomagokat külön
   - Egyes notebookok további csomagokat igényelhetnek, melyek a markdown cellákban vannak megemlítve

4. **Azure szolgáltatások:**
   - Az Azure AI szolgáltatások aktív előfizetést igényelnek
   - Egyes funkciók régióspecifikusak
   - Biztosítsd, hogy az Azure OpenAI modell telepítés támogatja a Responses API-t

### Tanulási út

Ajánlott sorrend a leckék között:
1. **00-course-setup** - Itt kezd a környezet beállításával
2. **01-intro-to-ai-agents** - Értsd meg az AI agentek alapjait
3. **02-explore-agentic-frameworks** - Ismerd meg a különböző framework-öket
4. **03-agentic-design-patterns** - Alapvető tervezési minták
5. Folytasd a számozott leckéket sorban

### Keretrendszer kiválasztás

Válassz framework-öt a céljaid alapján:
- **Minden leckéhez**: Microsoft Agent Framework (MAF) `FoundryChatClient`-vel
- **Az ügynökök szerveroldalon regisztrálnak** a Microsoft Foundry Agent Service V2-ben és láthatók a Foundry portálon

### Segítségkérés

- Csatlakozz a [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Nézd át a lecke README fájlokat specifikus iránymutatásért
- Tekintsd át a fő [README.md](./README.md) fájlt a kurzus áttekintéséhez
- Hivatkozz a [Course Setup](./00-course-setup/README.md) fájlra a részletes beállításért

### Hozzájárulás

Ez egy nyílt oktatási projekt. A hozzájárulások szívesen látottak:
- Javítsd a kódpéldákat
- Javíts elírásokat vagy hibákat
- Adj hozzá tisztázó kommentárokat
- Javasolj új lecketémákat
- Fordítsd le további nyelvekre

Lásd a [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) a jelenlegi igényekért.

## Projekt-specifikus kontextus

### Többnyelvű támogatás

Ez az adattár automatikus fordítási rendszert használ:
- 50+ nyelvet támogat
- A fordítások `/translations/<lang-code>/` könyvtárakban vannak
- A GitHub Actions workflow kezeli a fordítási frissítéseket
- A forrásfájlok angol nyelvűek az adattár gyökerében

### Lecke struktúra

Minden lecke követ egy egységes sémát:
1. Videó előnézeti kép linkkel
2. Írott lecke tartalom (README.md)
3. Kódpéldák több keretrendszerben
4. Tanulási célok és előfeltételek
5. További tanulási források hivatkozással

### Kódminta nevezék

Formátum: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - 1. lecke, MAF Python
- `14-sequential.ipynb` - 14. lecke, MAF haladó minták
- `16-python-agent-framework.ipynb` - 16. lecke, termelési ügyféltámogató ügynök
- `17-local-agent-foundry-local.ipynb` - 17. lecke, helyi ügynök Foundry Local + Qwen-nel

### Speciális könyvtárak

- `translated_images/` - Fordítási képek lokalizált változatai
- `images/` - Eredeti képek az angol tartalomhoz
- `.devcontainer/` - VS Code fejlesztői konténer konfiguráció
- `.github/` - GitHub Actions workflow-k és sablonok

### Függőségek

Kulcs csomagok a `requirements.txt`-ból:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent protokoll támogatás
- `azure-ai-inference`, `azure-ai-projects` - Azure AI szolgáltatások
- `azure-identity` - Azure hitelesítés (AzureCliCredential)
- `azure-search-documents` - Azure AI Search integráció
- `mcp[cli]` - Model Context Protocol támogatás

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->