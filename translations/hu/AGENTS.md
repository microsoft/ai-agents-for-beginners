# AGENTS.md

## Projekt áttekintése

Ez a tároló az "AI ügynökök kezdőknek" teljes oktatási tanfolyamot tartalmazza, amely megtanít mindent az AI ügynökök felépítéséhez. A tanfolyam 18 leckéből áll, melyek lefedik az alapokat, a tervezési mintákat, keretrendszereket és az AI ügynökök éles üzembe helyezését.

**Főbb technológiák:**
- Python 3.12+
- Jupyter jegyzetfüzetek az interaktív tanuláshoz
- AI keretrendszerek: Microsoft Agent Framework (MAF)
- Azure AI szolgáltatások: Microsoft Foundry, Microsoft Foundry Agent Service V2

**Architektúra:**
- Lecke-alapú struktúra (00-15+ könyvtárak)
- Minden lecke tartalmaz: README dokumentációt, kódmintákat (Jupyter jegyzetfüzetek), és képeket
- Többnyelvű támogatás automatikus fordító rendszerrel
- Egy Python jegyzetfüzet leckénként, Microsoft Agent Framework használatával

## Telepítési parancsok

### Előfeltételek
- Python 3.12 vagy újabb
- Azure előfizetés (Microsoft Foundryhoz)
- Telepített és hitelesített Azure CLI (`az login`)

### Kezdeti beállítás

1. **Klónozd vagy forkkold a tárolót:**
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
   # Szerkessze a .env fájlt az API kulcsaival és végpontjaival
   ```

### Szükséges környezeti változók

**Microsoft Foundryhoz** (kötelező):
- `AZURE_AI_PROJECT_ENDPOINT` - Microsoft Foundry projekt végpont
- `AZURE_AI_MODEL_DEPLOYMENT_NAME` - Modell üzembe helyezési név (pl. gpt-4o)

**Azure AI Searchhez** (05-ös lecke – RAG):
- `AZURE_SEARCH_SERVICE_ENDPOINT` - Azure AI Search végpont
- `AZURE_SEARCH_API_KEY` - Azure AI Search API kulcs

Hitelesítés: Futtasd az `az login` parancsot a jegyzetfüzetek futtatása előtt (`AzureCliCredential` használatával).

## Fejlesztési munkafolyamat

### Jupyter jegyzetfüzetek futtatása

Minden lecke több Jupyter jegyzetfüzetet tartalmaz különböző keretrendszerekhez:

1. **Indítsd el a Jupytert:**
   ```bash
   jupyter notebook
   ```

2. **Navigálj egy lecke könyvtárába** (pl. `01-intro-to-ai-agents/code_samples/`)

3. **Nyisd meg és futtasd a jegyzetfüzeteket:**
   - `*-python-agent-framework.ipynb` - Microsoft Agent Framework használata (Python)
   - `*-dotnet-agent-framework.ipynb` - Microsoft Agent Framework használata (.NET)

### Microsoft Agent Framework használata

**Microsoft Agent Framework + Microsoft Foundry:**
- Szükséges Azure előfizetés
- `FoundryChatClient` használata az Agent Service V2-hez (ügynökök láthatóak a Foundry portálon)
- Éles környezetre kész beépített megfigyelhetőséggel
- Fájlminta: `*-python-agent-framework.ipynb`

## Tesztelési útmutató

Ez egy oktatási tároló példakódokkal, nem éles kód automatizált tesztekkel. A beállítás és módosítások ellenőrzéséhez:

### Manuális tesztelés

1. **Teszteld a Python környezetet:**
   ```bash
   python --version  # Legalább 3.12 legyen+
   pip list | grep -E "(agent-framework|azure-ai|azure-identity)"
   ```

2. **Teszteld a jegyzetfüzet futtatását:**
   ```bash
   # Átalakítja a jegyzetfüzetet szkriptté és futtatja (teszteli az importokat)
   jupyter nbconvert --to script <lesson-folder>/code_samples/<notebook>.ipynb --stdout | python
   ```

3. **Ellenőrizd a környezeti változókat:**
   ```bash
   python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('✓ AZURE_AI_PROJECT_ENDPOINT' if os.getenv('AZURE_AI_PROJECT_ENDPOINT') else '✗ AZURE_AI_PROJECT_ENDPOINT missing')"
   ```

### Egyedi jegyzetfüzetek futtatása

Nyisd meg a jegyzetfüzeteket Jupyterben és futtasd a cellákat sorban. Minden jegyzetfüzet önálló és tartalmazza:
- Importálási utasításokat
- Konfiguráció betöltését
- Példaügynök-implementációkat
- Várt kimeneteket markdown cellákban

## Kódstílus

### Python konvenciók

- **Python verzió**: 3.12+
- **Kódstílus**: Kövesd a standard Python PEP 8 konvenciókat
- **Jegyzetfüzetek**: Használj világos markdown cellákat a fogalmak magyarázatához
- **Importok**: Csoportosítsd azokat standard könyvtári, harmadik fél, helyi importokra

### Jupyter jegyzetfüzet konvenciók

- Tartalmazzon leíró markdown cellákat a kód cellák előtt
- Adj hozzá kimeneti példákat a jegyzetfüzetekben hivatkozásként
- Használj világos változóneveket, amelyek megfelelnek a lecke fogalmainak
- Tartsd a jegyzetfüzet futtatási sorrendjét lineárisan (1. cella → 2. cella → 3. cella...)

### Fájl szervezés

```
<lesson-number>-<lesson-name>/
├── README.md                     # Lesson documentation
├── code_samples/
│   ├── <number>-python-agent-framework.ipynb
│   └── <number>-dotnet-agent-framework.ipynb  (optional)
└── images/
    └── *.png
```

## Készítés és telepítés

### Dokumentáció építése

Ez a tároló Markdownt használ dokumentációhoz:
- README.md fájlok minden lecke mappában
- Fő README.md a tároló gyökérkönyvtárában
- Automata fordító rendszer GitHub Actions segítségével

### CI/CD folyamat

A `.github/workflows/` könyvtárban található:

1. **co-op-translator.yml** - Automatikus fordítás 50+ nyelvre
2. **welcome-issue.yml** - Üdvözli az új hibabejelentőket
3. **welcome-pr.yml** - Üdvözli az új pull request hozzájárulókat

### Telepítés

Ez egy oktatási tároló – nincs telepítési folyamat. A felhasználók:
1. Forkkolják vagy klónozzák a tárolót
2. Helyben vagy GitHub Codespaces-ben futtatják a jegyzetfüzeteket
3. Tanulnak a példák módosításával és kísérletezésével

## Pull Request irányelvek

### Beküldés előtt

1. **Teszteld a változtatásokat:**
   - Teljesen futtasd az érintett jegyzetfüzeteket
   - Ellenőrizd, hogy minden cella hiba nélkül fut
   - Győződj meg arról, hogy a kimenetek megfelelőek

2. **Dokumentáció frissítések:**
   - Frissítsd a README.md-t, ha új fogalmakat adsz hozzá
   - Adj kommentárokat a jegyzetfüzetekhez a bonyolult kódhoz
   - Biztosítsd, hogy a markdown cellák magyarázzák a célt

3. **Fájl módosítások:**
   - Kerüld a `.env` fájlok beküldését (használj `.env.example`-et)
   - Ne küldj be `venv/` vagy `__pycache__/` könyvtárakat
   - Tartsd meg a jegyzetfüzet kimeneteket, ha azok fogalmakat szemléltetnek
   - Távolítsd el az ideiglenes fájlokat és biztonsági mentett jegyzetfüzeteket (`*-backup.ipynb`)

### PR cím formátuma

Használj leíró címeket:
- `[Lesson-XX] Új példa hozzáadása <fogalomhoz>`
- `[Fix] Hiba javítása a lesson-XX README-ben`
- `[Update] Kódminta javítása a lesson-XX-ben`
- `[Docs] Telepítési útmutatók frissítése`

### Kötelező ellenőrzések

- A jegyzetfüzeteknek hiba nélkül kell futniuk
- A README fájlok legyenek világosak és pontosak
- Kövesd a tároló meglévő kódmintáit
- Tartsd fenn az egységességet a többi leckével

## Egyéb megjegyzések

### Gyakori buktatók

1. **Python verzió nem megfelelő:**
   - Győződj meg róla, hogy Python 3.12+ van használatban
   - Néhány csomag nem működik régebbi verziókkal
   - Használd a `python3 -m venv` parancsot a Python verzió explicit megadására

2. **Környezeti változók:**
   - Mindig készíts `.env`-et a `.env.example`-ből
   - Ne add be a `.env` fájlt (be van írva a `.gitignore`-ba)
   - Azonosítás az `az login` segítségével billentyű nélküli Entra ID-hez

3. **Csomagütközések:**
   - Használj friss virtuális környezetet
   - Telepíts csomagokat a `requirements.txt`-ből egyenként helyett
   - Néhány jegyzetfüzet további csomagokat igényel, melyeket a markdown cellákban jelölnek

4. **Azure szolgáltatások:**
   - Az Azure AI szolgáltatások aktív előfizetést igényelnek
   - Néhány funkció régióspecifikus
   - Győződj meg arról, hogy az Azure OpenAI modell üzembehelyezés támogatja a Responses API-t

### Tanulási útvonal

Ajánlott haladás a leckéken:
1. **00-course-setup** - Kezdés a környezet beállításával
2. **01-intro-to-ai-agents** - AI ügynökök alapjainak megértése
3. **02-explore-agentic-frameworks** - Különböző keretrendszerek megismerése
4. **03-agentic-design-patterns** - Alapvető tervezési minták
5. Folytasd a számozott leckék sorrendjében

### Keretrendszer választás

Válassz keretrendszert céljaid szerint:
- **Minden leckéhez**: Microsoft Agent Framework (MAF) a `FoundryChatClient`-tel
- **Az ügynökök szerveroldalon regisztrálnak** a Microsoft Foundry Agent Service V2-ben és láthatóak a Foundry portálon

### Segítség kérése

- Csatlakozz a [Microsoft Foundry Community Discordhoz](https://aka.ms/ai-agents/discord)
- Nézd át a lecke README fájlokat speciális útmutatásokért
- Nézd meg a fő [README.md](./README.md) fájlt a tanfolyam áttekintéséhez
- Hivatkozz a [Course Setup](./00-course-setup/README.md) részletes telepítési útmutatóra

### Hozzájárulás

Ez egy nyílt oktatási projekt. Várjuk a hozzájárulásokat:
- Kód példák fejlesztése
- Elgépelések vagy hibák javítása
- Tisztázó kommentárok hozzáadása
- Új lecke témák javaslata
- Fordítás más nyelvekre

Nézd meg a [GitHub Issues](https://github.com/microsoft/ai-agents-for-beginners/issues) aktuális igényeit.

## Projektre jellemző háttér

### Többnyelvű támogatás

Ez a tároló automatikus fordító rendszert használ:
- Több mint 50 nyelvet támogat
- Fordítások a `/translations/<lang-code>/` könyvtárakban
- A GitHub Actions munkafolyamata kezeli a fordítás frissítéseket
- A forrásfájlok angolul vannak a tároló gyökérkönyvtárában

### Lecke szerkezet

Minden lecke követ egy egységes mintát:
1. Videó indexkép linkkel
2. Írott lecke tartalom (README.md)
3. Kód példák több keretrendszerben
4. Tanulási célok és előfeltételek
5. Extra tanulási források linkelve

### Kódminta elnevezés

Formátum: `<lesson-number>-python-agent-framework.ipynb`
- `01-python-agent-framework.ipynb` - 1. lecke, MAF Python
- `14-sequential.ipynb` - 14. lecke, MAF haladó minták

### Speciális könyvtárak

- `translated_images/` - Lokalizált képek a fordításokhoz
- `images/` - Eredeti angol képek
- `.devcontainer/` - VS Code fejlesztői konténer konfiguráció
- `.github/` - GitHub Actions munkafolyamatok és sablonok

### Függőségek

Fontos csomagok a `requirements.txt`-ből:
- `agent-framework` - Microsoft Agent Framework
- `a2a-sdk` - Agent-to-Agent protokoll támogatás
- `azure-ai-inference`, `azure-ai-projects` - Azure AI szolgáltatások
- `azure-identity` - Azure azonosítás (AzureCliCredential)
- `azure-search-documents` - Azure AI Search integráció
- `mcp[cli]` - Model Context Protocol támogatás

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->