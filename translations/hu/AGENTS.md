# AGENTS.md

## Projekt áttekintése

Ez a repozitórium az "AI Agents for Beginners" című átfogó oktatási kurzust tartalmazza, amely mindent megtanít, ami szükséges AI ügynökök létrehozásához. A kurzus több mint 15 leckéből áll, amelyek az alapokat, tervezési mintákat, keretrendszereket és az AI ügynökök gyártási telepítését fedik le.

**Kulcstechnológiák:**
- Python 3.12+
- Jupyter Notebooks interaktív tanuláshoz
- AI keretrendszerek: Semantic Kernel, AutoGen, Microsoft Agent Framework (MAF)
- Azure AI szolgáltatások: Azure AI Foundry, Azure AI Agent Service
- GitHub Models Marketplace (ingyenes szint elérhető)

**Architektúra:**
- Leckék alapú struktúra (00-15+ könyvtárak)
- Minden lecke tartalmaz: README dokumentációt, kódmintákat (Jupyter notebookok) és képeket
- Többnyelvű támogatás automatikus fordítási rendszerrel
- Több keretrendszer opció minden leckéhez (Semantic Kernel, AutoGen, Azure AI Agent Service)

## Telepítési parancsok

### Előfeltételek
- Python 3.12 vagy újabb
- GitHub fiók (GitHub Models - ingyenes szinthez)
- Azure előfizetés (opcionális, Azure AI szolgáltatásokhoz)

### Kezdeti beállítás

1. **Repozitórium klónozása vagy forkolása:**
   ```bash
   gh repo fork microsoft/ai-agents-for-beginners --clone
   # OR
   git clone https://github.com/microsoft/ai-agents-for-beginners.git
   cd ai-agents-for-beginners
   ```

2. **Python virtuális környezet létrehozása és aktiválása:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Függőségek telepítése:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Környezeti változók beállítása:**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and endpoints
   ```

### Szükséges környezeti változók

**GitHub Models (ingyenes) esetén:**
- `GITHUB_TOKEN` - Személyes hozzáférési token a GitHub-tól

**Azure AI szolgáltatásokhoz** (opcionális):
- `PROJECT_ENDPOINT` - Azure AI Foundry projekt végpont
- `AZURE_OPENAI_API_KEY` - Azure OpenAI API kulcs
- `AZURE_OPENAI_ENDPOINT` - Azure OpenAI végpont URL
- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Chat modell telepítési neve
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Beágyazások telepítési neve
- További Azure konfiguráció a `.env.example` fájlban található

## Fejlesztési munkafolyamat

### Jupyter Notebookok futtatása

Minden lecke több Jupyter notebookot tartalmaz különböző keretrendszerekhez:

1. **Jupyter indítása:**
   ```bash
   jupyter notebook
   ```

2. **Navigálás egy lecke könyvtárba** (pl. `01-intro-to-ai-agents/code_samples/`)

3. **Notebookok megnyitása és futtatása:**
   - `*-semantic-kernel.ipynb` - Semantic Kernel keretrendszer használata
   - `*-autogen.ipynb` - AutoGen keretrendszer használata
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework (Python)
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework (.NET)
   - `*-azureaiagent.ipynb` - Azure AI Agent Service használata

### Különböző keretrendszerek használata

**Semantic Kernel + GitHub Models:**
- Ingyenes szint elérhető GitHub fiókkal
- Jó tanuláshoz és kísérletezéshez
- Fájlminta: `*-semantic-kernel*.ipynb`

**AutoGen + GitHub Models:**
- Ingyenes szint elérhető GitHub fiókkal
- Több ügynökös koordinációs képességek
- Fájlminta: `*-autogen.ipynb`

**Microsoft Agent Framework (MAF):**
- Microsoft legújabb keretrendszere
- Elérhető Pythonban és .NET-ben
- Fájlminta: `*-agent-framework.ipynb`

**Azure AI Agent Service:**
- Azure előfizetést igényel
- Gyártásra kész funkciók
- Fájlminta: `*-azureaiagent.ipynb`

## Tesztelési útmutató

Ez egy oktatási repozitórium példakódokkal, nem pedig gyártási kód automatikus tesztekkel. A beállítás és változtatások ellenőrzéséhez:

### Kézi tesztelés

1. **Python környezet tesztelése:**
   ```bash
   python --version  # Should be 3.12+
   pip list | grep -E "(autogen|semantic-kernel|azure-ai)"
   ```

2. **Notebook futtatás tesztelése:**
   ```bash
   # Convert notebook to script and run (tests imports)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Környezeti változók ellenőrzése:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ GITHUB_TOKEN' if os.getenv('GITHUB_TOKEN') else '✗ GITHUB_TOKEN missing')"
   ```

### Egyedi notebookok futtatása

Nyissa meg a notebookokat Jupyterben, és hajtsa végre a cellákat sorban. Minden notebook önálló, és tartalmazza:
- Importálási utasítások
- Konfiguráció betöltése
- Példa ügynök implementációk
- Várható kimenetek markdown cellákban

## Kódstílus

### Python konvenciók

- **Python verzió**: 3.12+
- **Kódstílus**: Kövesse a standard Python PEP 8 konvenciókat
- **Notebookok**: Használjon tiszta markdown cellákat a fogalmak magyarázatára
- **Importok**: Csoportosítás standard könyvtár, harmadik fél, helyi importok szerint

### Jupyter Notebook konvenciók

- Tartalmazzon leíró markdown cellákat a kódcellák előtt
- Adjon hozzá kimeneti példákat a notebookokhoz referenciaként
- Használjon tiszta változóneveket, amelyek megfelelnek a lecke fogalmainak
- Tartsa lineáris sorrendben a notebook végrehajtását (1. cella → 2 → 3...)

### Fájlok szervezése

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-semantic-kernel.ipynb
│   ├── <number>-autogen.ipynb
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-azureaiagent.ipynb
└── images/
    └── *.png
```

## Építés és telepítés

### Dokumentáció építése

Ez a repozitórium Markdown-t használ dokumentációhoz:
- README.md fájlok minden lecke mappájában
- Fő README.md a repozitórium gyökérkönyvtárában
- Automatikus fordítási rendszer GitHub Actions segítségével

### CI/CD Pipeline

A `.github/workflows/` könyvtárban található:

1. **co-op-translator.yml** - Automatikus fordítás 50+ nyelvre
2. **welcome-issue.yml** - Üdvözli az új probléma létrehozókat
3. **welcome-pr.yml** - Üdvözli az új pull request beküldőket

### Telepítés

Ez egy oktatási repozitórium - nincs telepítési folyamat. Felhasználók:
1. Forkolják vagy klónozzák a repozitóriumot
2. Futtassák a notebookokat helyben vagy GitHub Codespaces-ben
3. Tanuljanak példák módosításával és kísérletezésével

## Pull Request irányelvek

### Beküldés előtt

1. **Tesztelje a változtatásait:**
   - Teljesen futtassa az érintett notebookokat
   - Ellenőrizze, hogy minden cella hiba nélkül fut-e
   - Győződjön meg róla, hogy a kimenetek megfelelőek

2. **Dokumentáció frissítése:**
   - Frissítse a README.md fájlt, ha új fogalmakat ad hozzá
   - Adjon hozzá megjegyzéseket a notebookokban a bonyolult kódhoz
   - Győződjön meg róla, hogy a markdown cellák magyarázzák a célt

3. **Fájlmódosítások:**
   - Ne kötelezze el a `.env` fájlokat (használja a `.env.example`-t)
   - Ne kötelezze el a `venv/` vagy `__pycache__/` könyvtárakat
   - Tartsa meg a notebook kimeneteket, ha azok fogalmakat demonstrálnak
   - Távolítsa el az ideiglenes fájlokat és a backup notebookokat (`*-backup.ipynb`)

### PR cím formátuma

Használjon leíró címeket:
- `[Lesson-XX] Új példa hozzáadása <fogalom> számára`
- `[Fix] Helyesírási hiba javítása a lesson-XX README-ben`
- `[Update] Kódminta javítása a lesson-XX-ben`
- `[Docs] Telepítési utasítások frissítése`

### Szükséges ellenőrzések

- A notebookoknak hiba nélkül kell futniuk
- A README fájloknak világosnak és pontosnak kell lenniük
- Kövesse a repozitóriumban meglévő kódmintákat
- Tartsa meg a konzisztenciát a többi leckével

## További megjegyzések

### Gyakori problémák

1. **Python verzió eltérés:**
   - Győződjön meg róla, hogy Python 3.12+ van használatban
   - Néhány csomag nem működik régebbi verziókkal
   - Használja a `python3 -m venv` parancsot a Python verzió explicit megadásához

2. **Környezeti változók:**
   - Mindig hozzon létre `.env` fájlt a `.env.example` alapján
   - Ne kötelezze el a `.env` fájlt (a `.gitignore`-ban van)
   - A GitHub tokennek megfelelő jogosultságokra van szüksége

3. **Csomagkonfliktusok:**
   - Használjon friss virtuális környezetet
   - Telepítse a `requirements.txt` fájlból, ne egyedi csomagokat
   - Néhány notebook további csomagokat igényel, amelyek markdown cellákban vannak megemlítve

4. **Azure szolgáltatások:**
   - Az Azure AI szolgáltatások aktív előfizetést igényelnek
   - Néhány funkció régióspecifikus
   - Az ingyenes szint korlátozásai vonatkoznak a GitHub Models-re

### Tanulási útvonal

Ajánlott haladási sorrend a leckék között:
1. **00-course-setup** - Kezdje itt a környezet beállításával
2. **01-intro-to-ai-agents** - Ismerje meg az AI ügynökök alapjait
3. **02-explore-agentic-frameworks** - Ismerje meg a különböző keretrendszereket
4. **03-agentic-design-patterns** - Alapvető tervezési minták
5. Folytassa a számozott leckéket sorrendben

### Keretrendszer kiválasztása

Válasszon keretrendszert céljai alapján:
- **Tanulás/Prototípus készítés**: Semantic Kernel + GitHub Models (ingyenes)
- **Több ügynökös rendszerek**: AutoGen
- **Legújabb funkciók**: Microsoft Agent Framework (MAF)
- **Gyártási telepítés**: Azure AI Agent Service

### Segítség kérése

- Csatlakozzon az [Azure AI Foundry Community Discord](https://aka.ms/ai-agents/discord) közösséghez
- Nézze át a lecke README fájlokat konkrét útmutatásért
- Ellenőrizze a fő [README.md](./README.md) fájlt a kurzus áttekintéséhez
- Tekintse meg a [Course Setup](./00-course-setup/README.md) fájlt részletes beállítási utasításokért

### Hozzájárulás

Ez egy nyílt oktatási projekt. Hozzájárulásokat szívesen fogadunk:
- Kódminták javítása
- Helyesírási hibák vagy hibák javítása
- Magyarázó megjegyzések hozzáadása
- Új lecke témák javaslata
- Fordítás további nyelvekre

Nézze meg a [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) oldalt az aktuális igényekért.

## Projekt-specifikus kontextus

### Többnyelvű támogatás

Ez a repozitórium automatikus fordítási rendszert használ:
- Több mint 50 nyelv támogatott
- Fordítások a `/translations/<lang-code>/` könyvtárakban találhatók
- GitHub Actions munkafolyamat kezeli a fordítási frissítéseket
- Forrásfájlok angolul a repozitórium gyökérkönyvtárában

### Lecke struktúra

Minden lecke követi a következő mintát:
1. Videó bélyegkép linkkel
2. Írott lecke tartalom (README.md)
3. Kódminták több keretrendszerben
4. Tanulási célok és előfeltételek
5. További tanulási források linkelve

### Kódminta elnevezés

Formátum: `<lesson-number>-<framework-name>.ipynb`
- `04-semantic-kernel.ipynb` - 4. lecke, Semantic Kernel
- `07-autogen.ipynb` - 7. lecke, AutoGen
- `14-python-agent-framework.ipynb` - 14. lecke, MAF Python
- `14-dotnet-agent-framework.ipynb` - 14. lecke, MAF .NET

### Speciális könyvtárak

- `translated_images/` - Lokalizált képek fordításokhoz
- `images/` - Eredeti képek angol tartalomhoz
- `.devcontainer/` - VS Code fejlesztési konténer konfiguráció
- `.github/` - GitHub Actions munkafolyamatok és sablonok

### Függőségek

Kulcsfontosságú csomagok a `requirements.txt` fájlból:
- `autogen-agentchat`, `autogen-core`, `autogen-ext` - AutoGen keretrendszer
- `semantic-kernel` - Semantic Kernel keretrendszer
- `agent-framework` - Microsoft Agent Framework
- `azure-ai-inference`, `azure-ai-projects` - Azure AI szolgáltatások
- `azure-search-documents` - Azure AI Search integráció
- `chromadb` - Vektoralapú adatbázis RAG példákhoz
- `chainlit` - Chat UI keretrendszer
- `browser_use` - Böngésző automatizálás ügynökök számára
- `mcp[cli]` - Model Context Protocol támogatás
- `mem0ai` - Memóriakezelés ügynökök számára

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Fontos információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.