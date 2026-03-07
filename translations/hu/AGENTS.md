# AGENTS.md

## Projekt áttekintés

Ez a tároló az "AI Agents for Beginners" kurzust tartalmazza - egy átfogó oktatási anyagot, amely megtanít mindent, ami az AI ügynökök felépítéséhez szükséges. A kurzus több mint 15 leckéből áll, amelyek lefedik az alapokat, tervezési mintákat, keretrendszereket és az AI ügynökök éles környezetbe történő telepítését.

**Fő technológiák:**
- Python 3.12+
- Jupyter Notebooks interaktív tanuláshoz
- AI keretrendszerek: Microsoft Agent Framework (MAF)
- Azure AI szolgáltatások: Microsoft Foundry, Azure AI Foundry Agent Service V2

**Architektúra:**
- Leckékre bontott struktúra (00-15+ könyvtárak)
- Minden lecke tartalmazza: README dokumentációt, kódmintákat (Jupyter notebooks) és képeket
- Többnyelvű támogatás automatizált fordítási rendszerrel
- Minden leckéhez egy Python jegyzetfüzet a Microsoft Agent Framework használatával

## Telepítési parancsok

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
   # Szerkessze a .env fájlt az API-kulcsok és a végpontok megadásához.
   ```

### Szükséges környezeti változók

Az **Azure AI Foundry** esetén (szükséges):
- `AZURE_AI_PROJECT_ENDPOINT` - Azure AI Foundry projektvégpont
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Modell telepítés neve (pl. gpt-4o)

Az **Azure AI Search** esetén (Lesson 05 - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search végpont
- `AZURE_SEARCH_API_KEY` - Azure AI Search API kulcs

Hitelesítés: Futtasd az `az login` parancsot a jegyzetfüzetek futtatása előtt (az `AzureCliCredential` használatával).

## Fejlesztési munkafolyamat

### Jupyter notebookok futtatása

Minden lecke több Jupyter notebookot tartalmaz különböző keretrendszerekhez:

1. **Jupyter indítása:**
   ```bash
   jupyter notebook
   ```

2. **Navigálj egy lecke könyvtárába** (pl. `01-intro-to-ai-agents/code_samples/`)

3. **Nyisd meg és futtasd a notebookokat:**
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework használata (Python)
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework használata (.NET)

### A Microsoft Agent Framework használata

**Microsoft Agent Framework + Azure AI Foundry:**
- Azure-előfizetést igényel
- Az Agent Service V2-hez az `AzureAIProjectAgentProvider`-t használja (az ügynökök láthatók a Foundry portálon)
- Éles környezetre alkalmas beépített megfigyelhetőséggel
- Fájlmintázat: `*-python-agent-framework.ipynb`

## Tesztelési utasítások

Ez egy oktatási tároló példa kóddal, nem pedig éles környezetre szánt automatizált tesztekkel rendelkező kód. A beállítás és a változtatások ellenőrzéséhez:

### Manuális tesztelés

1. **Teszteld a Python környezetet:**
   ```bash
   python --version  # 3.12 vagy újabb kell legyen.
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Teszteld a notebookok futtatását:**
   ```bash
   # A jegyzetfüzet átalakítása szkriptté és futtatása (a tesztek importálása)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Ellenőrizd a környezeti változókat:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Egyéni notebookok futtatása

Nyisd meg a notebookokat Jupyterben, és futtasd a cellákat sorban. Minden notebook önálló és tartalmazza:
- Import utasítások
- Konfiguráció betöltése
- Példa ügynök implementációk
- Várt kimenetek markdown cellákban

## Kódstílus

### Python konvenciók

- **Python verzió**: 3.12+
- **Kód stílus**: Kövesd a standard Python PEP 8 konvenciókat
- **Notebookok**: Használj világos markdown cellákat a fogalmak magyarázatához
- **Importok**: Csoportosítsd standard könyvtár, harmadik féltől származó és helyi importok szerint

### Jupyter notebook konvenciók

- Adj leíró markdown cellákat a kódcellák elé
- Adj kimeneti példákat a notebookokba referencia céljából
- Használj világos változóneveket, amelyek illeszkednek a lecke fogalmaihoz
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

## Építés és telepítés

### Dokumentáció építése

Ez a tároló Markdown-t használ dokumentációhoz:
- README.md fájlok minden lecke mappájában
- Fő README.md a tároló gyökerében
- Automatizált fordítási rendszer GitHub Actions segítségével

### CI/CD folyamat

A `.github/workflows/` könyvtárban található:

1. **co-op-translator.yml** - Automatikus fordítás 50+ nyelvre
2. **welcome-issue.yml** - Üdvözli az új issue létrehozókat
3. **welcome-pr.yml** - Üdvözli az új pull request hozzájárulókat

### Telepítés

Ez egy oktatási tároló - nincs telepítési folyamat. Felhasználók:
1. Forkold vagy klónozd a tárolót
2. Futtasd a notebookokat helyileg vagy GitHub Codespaces-ben
3. Tanulj a példák módosításával és kísérletezésével

## Pull request irányelvek

### Beküldés előtt

1. **Teszteld a változtatásaidat:**
   - Futtasd végig az érintett notebookokat
   - Ellenőrizd, hogy minden cella hibamentesen fut-e
   - Ellenőrizd, hogy a kimenetek megfelelőek-e

2. **Dokumentáció frissítései:**
   - Frissítsd a README.md-et, ha új fogalmakat adsz hozzá
   - Adj megjegyzéseket a notebookokban a bonyolult kódokhoz
   - Biztosítsd, hogy a markdown cellák elmagyarázzák a célját

3. **Fájlváltoztatások:**
   - Kerüld a `.env` fájlok committálását (`.env.example` használata javasolt)
   - Ne committáld a `venv/` vagy a `__pycache__/` könyvtárakat
   - Tartsd meg a notebook kimeneteket, ha bemutatják a fogalmakat
   - Távolítsd el az ideiglenes fájlokat és a biztonsági mentés notebookokat (`*-backup.ipynb`)

### PR cím formátuma

Használj leíró címeket:
- `[Lesson-XX] Új példa hozzáadása a <concept> számára`
- `[Fix] Javítsd a helyesírási hibát a lesson-XX README-ben`
- `[Update] Javítsd a kódpéldát a lesson-XX-ben`
- `[Docs] Frissítsd a telepítési utasításokat`

### Kötelező ellenőrzések

- A notebookoknak hibamentesen kell futniuk
- A README fájloknak világosnak és pontosnak kell lenniük
- Kövesd a meglévő kódmintákat a tárolóban
- Tartsd fenn az egységességet a többi leckével

## További megjegyzések

### Gyakori buktatók

1. **Python verzió eltérés:**
   - Gondoskodj róla, hogy Python 3.12+ legyen használatban
   - Néhány csomag nem működhet régebbi verziókkal
   - Használd a `python3 -m venv` parancsot a Python verzió egyértelmű megadásához

2. **Környezeti változók:**
   - Mindig hozd létre a `.env` fájlt a `.env.example` alapján
   - Ne commitáld a `.env` fájlt (a `.gitignore`-ban szerepel)
   - A GitHub tokennek megfelelő jogosultságokkal kell rendelkeznie

3. **Csomagütközések:**
   - Használj friss virtuális környezetet
   - Telepíts a `requirements.txt`-ből az egyes csomagok helyett
   - Néhány notebook további csomagokat igényelhet, amelyek a markdown cellákban vannak említve

4. **Azure szolgáltatások:**
   - Az Azure AI szolgáltatások aktív előfizetést igényelnek
   - Néhány funkció régióspecifikus
   - Ingyenes réteg korlátozásai érvényesek a GitHub Modellekre

### Tanulási útvonal

Ajánlott sorrend a leckéken át:
1. **00-course-setup** - Kezdd itt a környezet beállításához
2. **01-intro-to-ai-agents** - Ismerd meg az AI ügynökök alapjait
3. **02-explore-agentic-frameworks** - Ismerd meg a különböző keretrendszereket
4. **03-agentic-design-patterns** - Alapvető tervezési minták
5. Folytasd a számozott leckéken sorról sorra

### Keretrendszer kiválasztása

Válassz keretrendszert a céljaid alapján:
- **Minden lecke**: Microsoft Agent Framework (MAF) az `AzureAIProjectAgentProvider`-rel
- **Az ügynökök szerveroldalon regisztrálódnak** az Azure AI Foundry Agent Service V2-ben és láthatók a Foundry portálon

### Segítség kérése

- Csatlakozz a [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord)
- Nézd át a lecke README fájljait a speciális útmutatásért
- Ellenőrizd a fő [README.md](./README.md)-et a kurzus áttekintéséhez
- Hivatkozz a [Kurzus beállítása](./00-course-setup/README.md) a részletes telepítési utasításokért

### Hozzájárulás

Ez egy nyílt oktatási projekt. Hozzájárulásokat szívesen fogadunk:
- Javítsd a kód példákat
- Javíts hibákat vagy elgépeléseket
- Adj tisztázó megjegyzéseket
- Javasolj új lecke témákat
- Fordítsd le további nyelvekre

Tekintsd meg a [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) oldalt az aktuális igényekért.

## Projekt-specifikus kontextus

### Többnyelvű támogatás

Ez a tároló automatizált fordítási rendszert használ:
- Több mint 50 nyelv támogatott
- A fordítások a `/translations/<lang-code>/` könyvtárakban találhatók
- A GitHub Actions workflow kezeli a fordítások frissítését
- A forrásfájlok angol nyelven vannak a tároló gyökerében

### Lecke szerkezete

Minden lecke követ egy egységes mintát:
1. Videó bélyegkép linkkel
2. Írott lecke tartalom (README.md)
3. Kódpéldák több keretrendszerben
4. Tanulási célok és előfeltételek
5. Kapcsolt további tananyagok

### Kódminta elnevezése

Formátum: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - 1. lecke, MAF Python
- `14-sequential.ipynb` - 14. lecke, MAF haladó minták

### Speciális könyvtárak

- `translated_images/` - Lokalizált képek a fordítások számára
- `images/` - Eredeti képek az angol tartalomhoz
- `.devcontainer/` - VS Code fejlesztői konténer konfiguráció
- `.github/` - GitHub Actions workflowk és sablonok

### Függőségek

Kulcs csomagok a `requirements.txt`-ből:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent protokoll támogatás
- `azure-ai-inference`, `azure-ai-projects` - Azure AI szolgáltatások
- `azure-identity` - Azure hitelesítés (AzureCliCredential)
- `azure-search-documents` - Azure AI Search integráció
- `mcp[cli]` - Model Context Protocol támogatás

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Felelősségkizárás:
Ezt a dokumentumot az AI-alapú fordítószolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) használatával fordítottuk. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. A dokumentum eredeti, anyanyelvi változatát kell tekinteni az irányadónak. Kritikus információk esetén professzionális, emberi fordítás igénybevételét ajánljuk. Nem vállalunk felelősséget az ezen fordítás használatából eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->