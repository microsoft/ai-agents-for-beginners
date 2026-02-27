# AGENTS.md

## Projekt áttekintés

Ez a tároló tartalmazza az "AI Agents for Beginners" kurzust - egy átfogó oktatási tananyagot, amely megtanít mindent, ami az AI ügynökök felépítéséhez szükséges. A kurzus több mint 15 leckéből áll, amelyek lefedik az alapokat, tervezési mintákat, keretrendszereket és az AI ügynökök éles környezetbe történő telepítését.

**Főbb technológiák:**
- Python 3.12+
- Jupyter Notebookok az interaktív tanuláshoz
- AI keretrendszerek: Microsoft Agent Framework (MAF)
- Azure AI szolgáltatások: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Architektúra:**
- Leckealapú felépítés (00-15+ mappák)
- Minden lecke tartalmaz: README dokumentációt, kódpéldákat (Jupyter notebookok) és képeket
- Többnyelvű támogatás automatizált fordítási rendszerrel
- Minden leckéhez egy Python notebook a Microsoft Agent Framework használatával

## Beállítási parancsok

### Előfeltételek
- Python 3.12 vagy újabb
- Azure-előfizetés (az Azure AI Foundry-hoz)
- Azure CLI telepítve és hitelesítve (`az login`)

### Kezdeti beállítás

1. **Klónozd vagy forkold a tárolót:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # VAGY
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Hozd létre és aktiváld a Python virtuális környezetet:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows rendszeren: venv\Scripts\activate
   ```

3. **Telepítsd a függőségeket:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Állítsd be a környezeti változókat:**
   ```bash
   cp .env.example .env
   # Szerkeszd a .env fájlt az API-kulcsaid és végpontjaid megadásához
   ```

### Szükséges környezeti változók

Az **Azure AI Foundry** számára (kötelező):
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry project endpoint
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Model deployment name (e.g., gpt-4o)

Az **Azure AI Search** számára (05. lecke - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search endpoint
- `AZURE_SEARCH_API_KEY` - Azure AI Search API key

Hitelesítés: Futtasd az `az login` parancsot a notebookok futtatása előtt (az `AzureCliCredential`-t használja).

## Fejlesztési munkafolyamat

### Jupyter notebookok futtatása

Minden lecke több Jupyter notebookot tartalmaz különböző keretrendszerekhez:

1. **Indítsd el a Jupytert:**
   ```bash
   jupyter notebook
   ```

2. **Navigálj a lecke könyvtárába** (pl. `01-intro-to-ai-agents/code_samples/`)

3. **Nyisd meg és futtasd a notebookokat:**
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework használata (Python)
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework használata (.NET)

### A Microsoft Agent Framework használata

**Microsoft Agent Framework + Azure AI Foundry:**
- Szükséges Azure-előfizetés
- Az Agent Service V2-hez az `AzureAIProjectAgentProvider`-t használja (az ügynökök láthatók a Foundry portálon)
- Éles környezetre kész beépített megfigyelhetőséggel
- Fájlnév-minta: `*-python-agent-framework.ipynb`

## Tesztelési utasítások

Ez egy oktató célú tároló példakódokkal, nem pedig automatikus tesztekkel ellátott éles kóddal. A beállítás és a módosítások ellenőrzéséhez:

### Kézi tesztelés

1. **Teszteld a Python környezetet:**
   ```bash
   python --version  # 3.12 vagy újabb legyen.
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Teszteld a notebookok futtatását:**
   ```bash
   # Konvertáld a jegyzetfüzetet szkriptté és futtasd (a tesztek importjai)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Ellenőrizd a környezeti változókat:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Egyedi notebookok futtatása

Nyisd meg a notebookokat Jupyterben és futtasd a cellákat sorban. Minden notebook önálló és a következőket tartalmazza:
- Import utasítások
- Konfiguráció betöltése
- Példa ügynökmegvalósítások
- Várt kimenetek markdown cellákban

## Kódstílus

### Python konvenciók

- **Python verzió**: 3.12+
- **Kódstílus**: Kövesd a Python PEP 8 szabványt
- **Notebookok**: Használj világos markdown cellákat a fogalmak magyarázatához
- **Importok**: Csoportosítsd standard könyvtár, harmadik féltől származó és helyi importok szerint

### Jupyter notebook konvenciók

- Tegyél leíró markdown cellákat a kódcellák elé
- Adj kimenetpéldákat a notebookokba referencia céljából
- Használj egyértelmű változóneveket, amelyek megfelelnek a lecke fogalmainak
- Tartsd a notebook végrehajtási sorrendjét lineárisan (cell 1 → 2 → 3...)

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

## Build és telepítés

### Dokumentáció készítése

Ez a tároló Markdown-t használ a dokumentációhoz:
- README.md fájlok minden lecke mappájában
- Fő README.md a tároló gyökerében
- Automatizált fordítási rendszer GitHub Actions segítségével

### CI/CD folyamat

A `.github/workflows/` könyvtárban található:

1. **co-op-translator.yml** - Automatikus fordítás 50+ nyelvre
2. **welcome-issue.yml** - Üdvözli az új issue létrehozókat
3. **welcome-pr.yml** - Üdvözli az új pull request hozzájárulókat

### Telepítés

Ez egy oktató tároló - nincs telepítési folyamat. A felhasználók:
1. Forkold vagy klónozd a tárolót
2. Futtasd a notebookokat helyileg vagy GitHub Codespaces-ben
3. Tanulj a példák módosításával és kísérletezésével

## Pull Request irányelvek

### Beküldés előtt

1. **Teszteld a változtatásaidat:**
   - Futtasd végig az érintett notebookokat
   - Ellenőrizd, hogy minden cella hiba nélkül fut
   - Ellenőrizd, hogy a kimenetek megfelelőek

2. **Dokumentáció frissítései:**
   - Frissítsd a README.md-et, ha új fogalmakat adsz hozzá
   - Adj megjegyzéseket a notebookokban a bonyolult kódhoz
   - Biztosítsd, hogy a markdown cellák elmagyarázzák a célt

3. **Fájlváltoztatások:**
   - Kerüld a `.env` fájlok feltöltését (használd a `.env.example`-t)
   - Ne töltsd fel a `venv/` vagy `__pycache__/` könyvtárakat
   - Tartsd meg a notebook kimeneteit, ha bemutatnak fogalmakat
   - Távolítsd el az ideiglenes fájlokat és a mentési notebookokat (`*-backup.ipynb`)

### PR cím formátuma

Használj leíró címet:
- [Lesson-XX] Új példa a <concept> számára
- [Fix] Gépelési hiba javítása a lesson-XX README-ben
- [Update] A kódpélda javítása a lesson-XX-ben
- [Docs] A beállítási utasítások frissítése

### Kötelező ellenőrzések

- A notebookoknak hibamentesen kell futniuk
- A README fájlok legyenek világosak és pontosak
- Kövesd a tároló meglévő kódmintáit
- Őrizd meg az egységességet a többi leckével

## További megjegyzések

### Gyakori buktatók

1. **Python verzió eltérés:**
   - Győződj meg róla, hogy Python 3.12+ van használatban
   - Néhány csomag nem működhet régebbi verziókkal
   - Használd a `python3 -m venv`-t a Python verzió egyértelmű megadásához

2. **Környezeti változók:**
   - Mindig hozd létre a `.env` fájlt a `.env.example` alapján
   - Ne töltsd fel a `.env` fájlt (a `.gitignore`-ban szerepel)
   - A GitHub tokennek megfelelő engedélyekre van szüksége

3. **Csomagütközések:**
   - Használj friss virtuális környezetet
   - Telepíts a `requirements.txt` alapján, ne egyes csomagokat külön
   - Néhány notebook további csomagokat igényelhet, amelyek a markdown cellákban vannak feltüntetve

4. **Azure szolgáltatások:**
   - Az Azure AI szolgáltatások aktív előfizetést igényelnek
   - Néhány funkció régióspecifikus
   - Ingyenes csomag korlátozások érvényesek a GitHub Models-re

### Tanulási útvonal

Ajánlott haladás a leckéken keresztül:
1. **00-course-setup** - Kezdj itt a környezet beállításához
2. **01-intro-to-ai-agents** - Ismerkedj meg az AI ügynökök alapjaival
3. **02-explore-agentic-frameworks** - Ismerd meg a különböző keretrendszereket
4. **03-agentic-design-patterns** - Alapvető tervezési minták
5. Folytasd a számozott leckéket egymás után

### Keretrendszer kiválasztása

Válassz keretrendszert a céljaid alapján:
- **Minden lecke**: Microsoft Agent Framework (MAF) az `AzureAIProjectAgentProvider`-rel
- **Ügynökök szerveroldalon regisztrálódnak** az Azure AI Foundry Agent Service V2-ben és láthatók a Foundry portálon

### Segítség kérése

- Csatlakozz a [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Nézd át a lecke README fájlokat a részletes útmutatásért
- Nézd meg a fő [README.md](./README.md)-et a kurzus áttekintéséhez
- Hivatkozz a [Course Setup](./00-course-setup/README.md)-re a részletes beállítási utasításokért

### Hozzájárulás

Ez egy nyílt oktatási projekt. Várjuk a hozzájárulásokat:
- Fejleszd a kódpéldákat
- Javítsd az elírásokat vagy hibákat
- Adj hozzá tisztázó megjegyzéseket
- Javasolj új lecke témákat
- Fordítsd le további nyelvekre

Nézd meg a [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues)-t a jelenlegi igényekhez.

## Projekt-specifikus kontextus

### Többnyelvű támogatás

Ez a tároló egy automatizált fordítási rendszert használ:
- 50+ nyelv támogatott
- Fordítások a `/translations/<lang-code>/` könyvtárakban
- A GitHub Actions workflow kezeli a fordítási frissítéseket
- A forrásfájlok angolul találhatók a tároló gyökerében

### Lecke felépítése

Minden lecke követ egy egységes mintát:
1. Videó bélyegkép linkkel
2. Írott lecke tartalom (README.md)
3. Kódpéldák több keretrendszerben
4. Tanulási célok és előfeltételek
5. További tanulási források linkelve

### Kódminta elnevezése

Formátum: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - 1. lecke, MAF Python
- `14-sequential.ipynb` - 14. lecke, MAF haladó minták

### Speciális könyvtárak

- `translated_images/` - Lokalizált képek a fordításokhoz
- `images/` - Eredeti képek az angol tartalomhoz
- `.devcontainer/` - VS Code fejlesztői konténer konfiguráció
- `.github/` - GitHub Actions workflowok és sablonok

### Függőségek

Fő csomagok a `requirements.txt`-ből:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent protokoll támogatás
- `azure-ai-inference`, `azure-ai-projects` - Azure AI szolgáltatások
- `azure-identity` - Azure hitelesítés (AzureCliCredential)
- `azure-search-documents` - Azure AI Search integráció
- `mcp[cli]` - Model Context Protocol támogatás

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Felelősségkizárás:
Ez a dokumentum az AI-alapú fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelven tekintendő hiteles forrásnak. Kritikus információk esetén emberi, hivatásos fordítást javaslunk. Nem vállalunk felelősséget a jelen fordítás használatából eredő félreértésekért vagy téves értelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->