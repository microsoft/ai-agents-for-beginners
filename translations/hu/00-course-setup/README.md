# Kurzus beállítása

## Bevezetés

Ebben a leckében arról lesz szó, hogyan futtathatja a kurzus kódpéldáit.

## Csatlakozz más tanulókhoz és kérj segítséget

Mielőtt elkezdenéd klónozni a repo-t, csatlakozz az [AI Agents For Beginners Discord csatornához](https://aka.ms/ai-agents/discord), hogy segítséget kapj a beállításokhoz, kérdéseidet megválaszoljuk, vagy hogy kapcsolatba lépj más tanulókkal.

## Klónozd vagy forkold ezt a repót

Kezdésként kérjük, klónozd vagy forkold a GitHub Repository-t. Így meglesz a saját verziód a tananyagból, hogy futtathasd, tesztelhesd és módosíthasd a kódot!

Ezt megteheted, ha rákattintasz a <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">repo forkolása</a> linkre.

Most már meg kell, hogy legyen a saját forkolt verziód a kurzusról a következő linken:

![Forked Repo](../../../translated_images/hu/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (ajánlott workshop / Codespaceshez)

  >A teljes repository nagy (~3 GB) lehet, ha a teljes történetet és az összes fájlt letöltöd. Ha csak a workshopra mész, vagy csak néhány lecke mappát használsz, egy shallow clone (vagy sparse clone) elkerüli a nagyrészt letöltését azzal, hogy levágja a történetet és/vagy kihagyja a blobokat.

#### Gyors shallow clone — minimális előzmény, az összes fájl

Cseréld le az alábbi parancsokban a `<your-username>`-t a fork URL-edre (vagy ha inkább az upstream URL-t szeretnéd használni).

Csak az utolsó commit előzményét klónozáshoz (kis letöltés):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Specifikus ág klónozáshoz:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Részleges (sparse) klón — minimális blob + csak kiválasztott mappák

Ez részleges klónozást és sparse-checkout-ot használ (Git 2.25+ szükséges és ajánlott modern Git részleges klónozás támogatással):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Lépj be a repo mappába:

```bash|powershell
cd ai-agents-for-beginners
```

Majd határozd meg, mely mappákat szeretnéd (a példa két mappát mutat):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

A klónozás és a fájlok ellenőrzése után, ha csak a fájlokat akarod és helyet akarsz felszabadítani (git előzmény nélkül), kérlek töröld a tároló metaadatait (💀visszafordíthatatlan — elveszíted az összes Git funkciót: nem lesz commit, pull, push vagy előzmény hozzáférés).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces használata (ajánlott a helyi nagy letöltések elkerülésére)

- Hozz létre egy új Codespace-et ehhez a repóhoz a [GitHub UI](https://github.com/codespaces) segítségével.

- A frissen létrehozott codespace termináljában futtasd a fenti shallow/sparse clone parancsok valamelyikét, hogy csak a szükséges lecke mappákat hozd be a Codespace munkaterületére.
- Opcionális: a klónozás után Codespace-ben töröld a .git mappát a plusz hely felszabadításához (lásd a fenti törlési parancsokat).
- Megjegyzés: ha inkább közvetlenül nyitod meg a repót Codespace-ben (klónozás nélkül), vedd figyelembe, hogy Codespaces létrehozza a devcontainer környezetet, és lehet, hogy több mindent telepít, mint amire szükséged van. Egy friss Codespace-ben klónozni egy shallow példányt több kontrollt ad a lemezhasználat felett.

#### Tippek

- Mindig cseréld ki a klón URL-t a forkodra, ha szerkeszteni/commitálni szeretnél.
- Ha később több előzményre vagy fájlokra van szükséged, lehívhatod vagy módosíthatod a sparse-checkout-ot, hogy további mappákat vegyen fel.

## A kód futtatása

Ez a kurzus egy sor Jupyter Notebookot kínál, amelyeket futtathatsz, hogy gyakorlatot szerezz AI ügynökök építésében.

A kódpéldák a **Microsoft Agent Framework (MAF)** rendszert használják az `AzureAIProjectAgentProvider`-rel, amely kapcsolódik az **Azure AI Agent Service V2**-höz (Responses API) a **Microsoft Foundry** rendszeren keresztül.

Az összes Python notebook neve `*-python-agent-framework.ipynb` végződésű.

## Követelmények

- Python 3.12+
  - **MEGJEGYZÉS**: Ha még nincs Python3.12 telepítve, telepítsd azt. Ezután hozd létre a virtuális környezeted python3.12-vel, hogy biztosan a megfelelő verziók települjenek a requirements.txt fájlból.
  
    >Példa

    Hozd létre a Python venv könyvtárat:

    ```bash|powershell
    python -m venv venv
    ```

    Ezután aktiváld a venv környezetet ehhez:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: A mintakódok futtatásához a .NET verziót telepíteni kell. Telepítsd a [.NET 10 SDK-t](https://dotnet.microsoft.com/download/dotnet/10.0) vagy újabbat. Ezután ellenőrizd a telepített .NET SDK verziót:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Hitelesítéshez szükséges. Telepítsd innen: [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure előfizetés** — A Microsoft Foundry és Azure AI Agent Service eléréséhez.
- **Microsoft Foundry Projekt** — Egy projekt, amely telepített modellel rendelkezik (pl. `gpt-4o`). Lásd az [1. lépést](../../../00-course-setup) lent.

Ez a repó tartalmaz egy `requirements.txt` fájlt a gyökérkönyvtárban, amely az összes szükséges Python csomagot tartalmazza a kódpéldák futtatásához.

Telepítheted őket, ha futtatod a következő parancsot a terminálodban, a repó gyökérkönyvtárában:

```bash|powershell
pip install -r requirements.txt
```

Ajánljuk, hogy hozz létre egy Python virtuális környezetet az esetleges konfliktusok és problémák elkerülésére.

## VSCode beállítása

Győződj meg róla, hogy a VSCode-ban a megfelelő Python verziót használod.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry és Azure AI Agent Service beállítása

### 1. lépés: Microsoft Foundry projekt létrehozása

Szükséged lesz egy Azure AI Foundry **hub**-ra és egy **projektre**, amelyhez van telepített modell, hogy futtasd a jegyzetfüzeteket.

1. Lépj a [ai.azure.com](https://ai.azure.com) oldalra, és jelentkezz be az Azure fiókoddal.
2. Hozz létre egy **hubot** (vagy használj egy meglévőt). Lásd: [Hub erőforrások áttekintése](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. A hubon belül hozz létre egy **projektet**.
4. Telepíts egy modellt (pl. `gpt-4o`) a **Models + Endpoints** → **Deploy model** alatt.

### 2. lépés: A projekt végpontjának és a modell telepítési nevének lekérése

A Microsoft Foundry portálon a projektednél:

- **Projekt végpont** — Lépj a **Overview** oldalra és másold ki a végpont URL-t.

![Project Connection String](../../../translated_images/hu/project-endpoint.8cf04c9975bbfbf1.webp)

- **Modell telepítés neve** — Menj a **Models + Endpoints** pontra, válaszd a telepített modelljed és jegyezd fel a **Deployment name**-et (pl. `gpt-4o`).

### 3. lépés: Jelentkezz be az Azure-ba `az login`-nal

Az összes jegyzetfüzet a **`AzureCliCredential`**-t használja hitelesítéshez — semmilyen API kulcsot nem kell kezelni. Ez megköveteli, hogy jelentkezz be az Azure CLI-n keresztül.

1. **Telepítsd az Azure CLI-t**, ha még nincs meg: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Jelentkezz be** futtatva:

    ```bash|powershell
    az login
    ```

    Vagy ha távoli/Codespace környezetben vagy böngésző nélkül:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Válaszd ki az előfizetésed**, ha kéri — azt, amelyik tartalmazza a Foundry projekted.

4. **Ellenőrizd**, hogy be vagy-e jelentkezve:

    ```bash|powershell
    az account show
    ```

> **Miért `az login`?** A jegyzetfüzetek az `azure-identity` csomag **`AzureCliCredential`**-jét használják hitelesítéshez. Ez azt jelenti, hogy az Azure CLI munkameneted adja a hitelesítő adatokat — nincs API kulcs vagy titok a `.env` fájlban. Ez egy [biztonsági legjobb gyakorlat](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### 4. lépés: Hozd létre a `.env` fájlodat

Másold az mintafájlt:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Nyisd meg a `.env`-t és töltsd ki az alábbi két értéket:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Változó | Hol találod |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portál → a projekted → **Overview** oldal |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portál → **Models + Endpoints** → a telepített modell neve |

Ennyi az alapokhoz! A jegyzetfüzetek automatikusan hitelesítenek az `az login` munkameneteden keresztül.

### 5. lépés: Python függőségek telepítése

```bash|powershell
pip install -r requirements.txt
```

Ajánlott ezt a virtuális környezetben futtatni, amit korábban létrehoztál.

## Kiegészítő beállítás az 5. leckéhez (Agentic RAG)

Az 5. lecke **Azure AI Search**-t használ a retrieval-augmented generáláshoz. Ha futtatni szeretnéd ezt a leckét, add hozzá az alábbi változókat a `.env` fájlodhoz:

| Változó | Hol találod |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portál → az **Azure AI Search** erőforrásod → **Overview** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portál → az **Azure AI Search** erőforrásod → **Settings** → **Keys** → elsődleges admin kulcs |

## Kiegészítő beállítás a 6. és 8. leckéhez (GitHub Modellek)

A 6. és 8. leckék néhány jegyzetfüzete **GitHub Modelleket** használ az Azure AI Foundry helyett. Ha ezeket a példákat fogod futtatni, add hozzá az alábbi változókat a `.env` fájlodhoz:

| Változó | Hol találod |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Settings** → **Developer settings** → **Personal access tokens** |
| `GITHUB_ENDPOINT` | Használd a `https://models.inference.ai.azure.com`-t (alapértelmezett érték) |
| `GITHUB_MODEL_ID` | Használandó modell neve (pl. `gpt-4o-mini`) |

## Kiegészítő beállítás a 8. leckéhez (Bing Grounding Workflow)

A 8. leckében a feltételes munkafolyamat jegyzetfüzet a **Bing grounding**-et használja az Azure AI Foundry révén. Ha futtatni szeretnéd ezt a példát, add hozzá ezt a változót a `.env` fájlodhoz:

| Változó | Hol találod |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry portál → a projekted → **Management** → **Connected resources** → a Bing kapcsolódásod → másold ki a kapcsolat ID-t |

## Hibakeresés

### SSL tanúsítvány ellenőrzési hibák macOS-en

Ha macOS-t használsz és a következő hibát kapod:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Ez egy ismert probléma Python-on macOS alatt, amikor a rendszer SSL tanúsítványai nincsenek automatikusan megbízhatónak jelölve. Próbáld ki az alábbi megoldásokat sorrendben:

**1. megoldás: Fuss Python Install Certificates szkriptje (ajánlott)**

```bash
# Cseréld ki a 3.XX-et a telepített Python verziódra (pl. 3.12 vagy 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**2. megoldás: Használd a `connection_verify=False` opciót a jegyzetfüzetben (csak GitHub Modellekhez készült notebookokhoz)**

A 6. leckében lévő jegyzetfüzetben (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) már van kommentelt megoldás erre. Szedd ki a kommentet `connection_verify=False` létrehozásánál:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Kapcsolja ki az SSL ellenőrzést, ha tanúsítványhibákat tapasztal
)
```

> **⚠️ Figyelem:** Az SSL ellenőrzés kikapcsolása (`connection_verify=False`) biztonsági kockázatot jelent, mert kihagyja a tanúsítvány ellenőrzést. Csak ideiglenes fejlesztési célokra használd, soha ne éles környezetben.

**3. megoldás: Telepítsd és használd a `truststore`-t**

```bash
pip install truststore
```

Majd add hozzá a következőt a jegyzetfüzet vagy szkript elejére, még mielőtt hálózati hívást kezdeményeznél:

```python
import truststore
truststore.inject_into_ssl()
```

## Elakadtál valahol?

Ha bármi gondod akad ezzel a beállítással, csatlakozz az <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> csatornához, vagy <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">hozz létre egy hibajegyet</a>.

## Következő lecke

Most már készen állsz, hogy futtasd a kódot ehhez a kurzushoz. Jó tanulást az AI ügynökök világában!

[Bevezetés az AI ügynökökbe és azok felhasználási eseteihez](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár igyekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások tartalmazhatnak hibákat vagy pontatlanságokat. Az eredeti dokumentum a hivatalos és hiteles forrás az eredeti nyelven. Kritikus információk esetén professzionális, emberi fordítást javaslunk. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->