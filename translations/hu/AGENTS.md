# AGENTS.md

## Projekt áttekintése

Ez a tároló az "AI ügynökök kezdőknek" nevű átfogó oktatási tanfolyamot tartalmazza, amely mindent megtanít az AI ügynökök építéséhez. A tanfolyam 18 leckéből áll (számozva 00-18), amelyek lefedik az alapokat, a tervezési mintákat, a keretrendszereket, a gyártási telepítést, a helyi/eszközön futó ügynököket és az AI ügynökök biztonságát.

**Fő technológiák:**
- Python 3.12+
- Jupyter Notebookok az interaktív tanuláshoz
- AI keretrendszerek: Microsoft Agent Framework (MAF)
- Azure AI szolgáltatások: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Architektúra:**
- Leckénkénti felépítés (00-15+ könyvtárak)
- Minden lecke tartalmaz: README dokumentációt, kódmintákat (Jupyter notebookok), és képeket
- Többnyelvű támogatás automatizált fordítási rendszerrel
- Egy Python notebook leckénként, a Microsoft Agent Framework használatával

## Telepítési parancsok

### Előfeltételek
- Python 3.12 vagy újabb
- Azure előfizetés (Microsoft Foundry használatához)
- Telepített és hitelesített Azure CLI (`az login`)

### Kezdeti telepítés

1. **Klónozd vagy forkold a tárolót:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # VAGY
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Hozz létre és aktiválj egy Python virtuális környezetet:**
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
   # Szerkessze a .env fájlt az API kulcsaival és végpontjaival
   ```

### Szükséges környezeti változók

A **Microsoft Foundry-hoz** (kötelező):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry projekt végpontja
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Modell telepítés neve (pl. gpt-5-mini)

Az **Azure AI Search-hoz** (05-ös lecke - RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search végpont
- `AZURE_SEARCH_API_KEY` - Azure AI Search API kulcs

Hitelesítés: Futtasd az `az login` parancsot a notebookok indítása előtt (az `AzureCliCredential` használatával).

## Fejlesztési munkafolyamat

### Jupyter notebookok futtatása

Minden lecke több Jupyter notebookot tartalmaz különböző keretrendszerekhez:

1. **Indítsd el a Jupitert:**
   ```bash
   jupyter notebook
   ```

2. **Navigálj a lecke könyvtárához** (pl. `01-intro-to-ai-agents/code_samples/`)

3. **Nyisd meg és futtasd a notebookokat:**
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework használata (Python)
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework használata (.NET)

### Munkavégzés a Microsoft Agent Frameworkkel

**Microsoft Agent Framework + Microsoft Foundry:**
- Szükséges Azure előfizetés
- Használja a `FoundryChatClient`-et az Agent Service V2-höz (az ügynökök láthatók a Foundry portálon)
- Gyártásra kész beépített megfigyelhetőséggel
- Fájlnév minta: `*-python-agent-framework.ipynb`

## Tesztelési útmutató

Ez egy oktatási tároló példakódokkal, nem pedig gyártási kód automatizált tesztekkel. A beállítás és változtatások ellenőrzéséhez:

### Manuális tesztelés

1. **Teszteld a Python környezetet:**
   ```bash
   python --version  # Legalább 3.12-es verziónak kell lennie
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Teszteld a notebook végrehajtást:**
   ```bash
   # Jegyzetfüzet átalakítása szkriptté és futtatása (tesztek importálása)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Ellenőrizd a környezeti változókat:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Egyedi notebookok futtatása

Nyisd meg a notebookokat Jupyterben és futtasd a cellákat egymás után. Minden notebook önálló és tartalmazza:
- Importálásokat
- Konfiguráció betöltést
- Példa ügynök megvalósításokat
- Várt kimeneteket markdown cellákban

### Gyorsellenőrzés a telepített ügynököknél

Azokban a leckékben, ahol az ügynökök Microsoft Foundry hosztolt ügynökként vannak telepítve (01, 04, 05, 16), a repo tartalmaz gyors teszt katalógusokat a `tests/` könyvtár alatt, amelyeket a `.github/workflows/smoke-test.yml` munkafolyamat futtat a [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) akció segítségével. Ezek egy könnyű poszttelepítési átmeneti kapuként szolgálnak (elérhető-e az ügynök és követi-e az alap prompt elvárásokat?), kiegészítve a kiértékelő folyamatot a 10. és 16. leckékben. Lásd a [tests/README.md](./tests/README.md) fájlt a katalógus-lecke-ügynök megfeleltetésért. A 17. lecke helyileg fut Foundry Local segítségével, nincs hosztolt végpontja, ezért közvetlenül a notebook futtatásával validálható.

## Kódstílus

### Python konvenciók

- **Python verzió**: 3.12+
- **Kódstílus**: Kövesd a standard Python PEP 8 konvenciókat
- **Notebookok**: Használj világos markdown cellákat a fogalmak magyarázatára
- **Importok**: Csoportosítsd őket standard könyvtár, harmadik fél, helyi importokra

### Jupyter Notebook konvenciók

- Tartalmazzon leíró markdown cellákat a kódcellák előtt
- Adj példakimeneteket a notebookokban hivatkozásként
- Használj egyértelmű változóneveket, amelyek illeszkednek a lecke fogalmaihoz
- Tartsd meg a notebook futtatási sorrendjét lineárisan (1 → 2 → 3. cella...)

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

Ez a tároló Markdown formátumot használ a dokumentációhoz:
- README.md fájlok minden lecke mappájában
- Fő README.md a tároló gyökérkönyvtárában
- Automatizált fordítási rendszer GitHub Actions segítségével

### CI/CD Folyamat

A `.github/workflows/` könyvtárban található:

1. **co-op-translator.yml** - Automatikus fordítás 50+ nyelvre
2. **welcome-issue.yml** - Üdvözli az új issue létrehozókat
3. **welcome-pr.yml** - Üdvözli az új pull request hozzájárulókat

### Telepítés

Ez egy oktatási tároló - nincs telepítési folyamat. A felhasználók:
1. Forkolják vagy klónozzák a tárolót
2. Futtassák a notebookokat helyileg vagy GitHub Codespaces-ben
3. Tanuljanak módosítással és kísérletezéssel a példákkal

## Pull Request irányelvek

### Küldés előtt

1. **Teszteld a változtatásaidat:**
   - Futtasd végig az érintett notebookokat teljesen
   - Ellenőrizd, hogy minden cella hiba nélkül fut
   - Nézd meg, hogy a kimenetek megfelelőek-e

2. **Dokumentáció frissítése:**
   - Frissítsd a README.md-et, ha új fogalmat adsz hozzá
   - Adj kommenteket a notebookokba a bonyolult kódhoz
   - Gondoskodj arról, hogy a markdown cellák magyarázzák a célt

3. **Fájlváltozások:**
   - Kerüld a `.env` fájlok commitálását (`.env.example` használata javasolt)
   - Ne commitáld a `venv/` vagy `__pycache__/` könyvtárakat
   - Tartsd meg a notebook kimeneteket, ha azok bemutatják a fogalmakat
   - Távolítsd el az ideiglenes fájlokat és biztonsági mentés notebookokat (`*-backup.ipynb`)

### PR cím formátuma

Használj leíró címeket:
- `[Lesson-XX] Új példa hozzáadása <fogalomhoz>`
- `[Fix] Elírás javítása a lesson-XX README-ben`
- `[Update] Kódminta javítása a lesson-XX-ben`
- `[Docs] Telepítési utasítások frissítése`

### Követelmény ellenőrzések

- A notebookoknak hiba nélkül kell futniuk
- A README fájloknak világosnak és pontosnak kell lenniük
- Kövesd a meglévő kódmintákat a tárolóban
- Tartsd a konzisztenciát a többi leckével

## További megjegyzések

### Gyakori buktatók

1. **Python verzió eltérés:**
   - Győződj meg arról, hogy Python 3.12+ verziót használsz
   - Néhány csomag nem működhet régebbi verzióval
   - Használd a `python3 -m venv` parancsot a Python verzió explicite megadásához

2. **Környezeti változók:**
   - Mindig hozz létre `.env` fájlt a `.env.example` alapján
   - Ne commitáld a `.env` fájlt (ez `.gitignore`-ban van)
   - Jelentkezz be `az login`-nal kulcs nélküli Entra ID hitelesítésért

3. **Csomag ütközések:**
   - Használj friss virtuális környezetet
   - Telepítsd a csomagokat a `requirements.txt`-ből egyenkénti helyett
   - Néhány notebook plusz csomagokat igényelhet, amik a markdown cellákban szerepelnek

4. **Azure szolgáltatások:**
   - Az Azure AI szolgáltatások aktív előfizetést igényelnek
   - Néhány funkció régió-specifikus
   - Győződj meg arról, hogy az Azure OpenAI modell telepítésed támogatja a Responses API-t

### Tanulási útvonal

Ajánlott haladás a leckéken keresztül:
1. **00-course-setup** - Itt kezd a környezet beállításával
2. **01-intro-to-ai-agents** - Értsd meg az AI ügynökök alapjait
3. **02-explore-agentic-frameworks** - Ismerd meg a különböző keretrendszereket
4. **03-agentic-design-patterns** - Alapvető tervezési minták
5. Haladj sorban a számozott leckéken át

### Keretrendszer választás

Válaszd a keretrendszert a céljaid alapján:
- **Minden lecke**: Microsoft Agent Framework (MAF) a `FoundryChatClient`-tel
- **Az ügynökök szerver oldalon regisztrálnak** a Microsoft Foundry Agent Service V2-ben és láthatók a Foundry portálon

### Segítség kérése

- Csatlakozz a [Microsoft Foundry Community Discord](https://aka.ms/ai-agents/discord) közösséghez
- Nézd át az egyes leckék README fájljait specifikus útmutatókért
- Tekintsd meg a fő [README.md](./README.md) fájlt a tanfolyam áttekintéséhez
- Hivatkozz a [Course Setup](./00-course-setup/README.md) oldalra részletes telepítési utasításokért

### Hozzájárulás

Ez egy nyílt oktatási projekt. Várjuk a hozzájárulásokat:
- Kódpéldák fejlesztése
- Elírások vagy hibák javítása
- Tisztázó kommentek hozzáadása
- Új lecke témák javaslata
- Fordítások további nyelvekre

Nézd meg a [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) feladatlistát a jelenlegi igényekért.

## Projekt-specifikus kontextus

### Többnyelvű támogatás

Ez a tároló egy automatizált fordítási rendszert használ:
- Több mint 50 nyelvet támogat
- Fordítások a `/translations/<lang-code>/` könyvtárakban
- GitHub Actions folyamat kezeli a fordítási frissítéseket
- Forrásfájlok angol nyelven a tároló gyökerében

### Lecke felépítése

Minden lecke következetes mintát követ:
1. Videó előnézeti képe linkkel
2. Írott lecke tartalom (README.md)
3. Kódminták több keretrendszerben
4. Tanulási célok és előfeltételek
5. Extra tanulási források hivatkozásai

### Kódminta fájlnevek

Formátum: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - 1. lecke, MAF Python
- `14-sequential.ipynb` - 14. lecke, MAF haladó minták
- `16-python-agent-framework.ipynb` - 16. lecke, gyártásra kész ügyfélszolgálati ügynök
- `17-local-agent-foundry-local.ipynb` - 17. lecke, helyi ügynök Foundry Local + Qwen használattal

### Speciális könyvtárak

- `translated_images/` - Fordításokhoz lokalizált képek
- `images/` - Eredeti képek az angol tartalomhoz
- `.devcontainer/` - VS Code fejlesztői konténer konfiguráció
- `.github/` - GitHub Actions munkafolyamatok és sablonok

### Függőségek

Fő csomagok a `requirements.txt`-ben:
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