# Tanfolyam beállítása

## Bevezetés

Ez a lecke arról szól, hogyan futtathatod a tanfolyam kódmintáit.

## Csatlakozz más tanulókhoz és kérj segítséget

Mielőtt elkezdenéd klónozni a repo-dat, csatlakozz az [AI Agents For Beginners Discord csatornához](https://aka.ms/ai-agents/discord), hogy segítséget kapj a beállításhoz, kérdéseket tehess fel a tanfolyammal kapcsolatban, vagy kapcsolatba léphess más tanulókkal.

## Klónozd vagy Forkold ezt a repót

Kezdésként kérjük, klónozd vagy forkold a GitHub-tárházat. Így saját verziódat kapod meg a tanfolyami anyagból, hogy futtathasd, tesztelhesd és módosíthasd a kódot!

Ezt megteheted úgy, hogy rákattintasz az <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">repo fork-olása</a> linkre.

Most már saját fork-olt verzióddal kell rendelkezned a tanfolyamról az alábbi linken:

![Forkolt Repo](../../../translated_images/hu/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (ajánlott workshophoz / Codespaces-hez)

  >A teljes repó nagy (~3 GB) lehet, ha a teljes történetet és összes fájlt letöltöd. Ha csak a workshopon veszel részt, vagy csak néhány leckefüzetre van szükséged, egy shallow clone (vagy sparse clone) elkerüli a legtöbb letöltést azzal, hogy levágja a történetet és/vagy átugorja a blobokat.

#### Gyors shallow clone – minimális történet, az összes fájl

Cseréld ki `<your-username>` a lentiekben a fork URL-edre (vagy az upstream URL-re, ha inkább azt használod).

Az utolsó commit történetének klónozásához (kis letöltés):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Egy adott ág klónozásához:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Részleges (sparse) klón – minimális blobok + csak kiválasztott mappák

Ez részleges klónozást és sparse-checkout-ot használ (Git 2.25+ szükséges, ajánlott modern Git, ami támogatja a részleges klónozást):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Lépj be a repo mappájába:

```bash|powershell
cd ai-agents-for-beginners
```

Majd határozd meg, mely mappákat szeretnéd (a példa két mappát mutat):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

A klónozás és a fájlok ellenőrzése után, ha csak a fájlokra van szükséged és helyet akarsz felszabadítani (nincs git történelem), töröld a repó metaadatait (💀visszafordíthatatlan – elveszted az összes Git funkciót: nincs commit, pull, push, vagy történelem elérés).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces használata (ajánlott a helyi nagy letöltések elkerülésére)

- Hozz létre új Codespace-t ehhez a repóhoz a [GitHub UI-n keresztül](https://github.com/codespaces).  

- A most létrejött codespace termináljában futtass az előzőekben említett shallow/sparse klón parancsok közül egyet, hogy csak a szükséges leckefüzeteket hozd be a Codespace munkaterületére.
- Opcionális: a klónozás után Codespaces-ben töröld a .git-et, hogy extra helyet szabadíts fel (lásd a fent látható törlési parancsokat).
- Megjegyzés: Ha inkább a repót közvetlenül nyitod meg Codespaces-ben (klónozás nélkül), vedd figyelembe, hogy a Codespaces elkészíti a devcontainer környezetet, és lehet, hogy többet telepít, mint amennyire szükséged van. Egy könnyített klón friss Codespace-en belüli készítése nagyobb kontrollt ad a lemezhasználat felett.

#### Tippek

- Mindig cseréld le a klón URL-t a saját forkodra, ha szerkeszteni/commitálni szeretnél.
- Ha később több történetre vagy fájlra van szükséged, lekérheted őket vagy módosíthatod a sparse-checkout-ot további mappák bevonásához.

## A kód futtatása

Ez a tanfolyam egy sor Jupyter Notebook-ot kínál, amelyek futtatásával gyakorlati tapasztalatot szerezhetsz AI ügynökök építésében.

A kódminták a **Microsoft Agent Framework (MAF)**-ot használják az `AzureAIProjectAgentProvider`-rel, amely kapcsolatot létesít az **Azure AI Agent Service V2**-vel (a Responses API) a **Microsoft Foundry**-n keresztül.

Minden Python notebook `*-python-agent-framework.ipynb` névvel van megjelölve.

## Követelmények

- Python 3.12+
  - **MEGJEGYZÉS**: Ha nincs telepítve Python3.12, győződj meg róla, hogy telepíted. Majd a venv-et python3.12-vel hozd létre, hogy a requirements.txt-ből a megfelelő verziók települjenek.
  
    >Példa

    Hozd létre a Python venv könyvtárat:

    ```bash|powershell
    python -m venv venv
    ```

    Majd aktiváld a venv környezetet ehhez:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: A .NET mintakódokhoz telepítsd a [.NET 10 SDK-t](https://dotnet.microsoft.com/download/dotnet/10.0) vagy újabbat. Ellenőrizd az installált .NET SDK verzióját:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — szükséges az azonosításhoz. Telepítsd innen: [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure-előfizetés** — a Microsoft Foundry és Azure AI Agent Service eléréséhez.
- **Microsoft Foundry projekt** — projekt telepített modellel (pl. `gpt-4o`). Lásd az alábbi [1. lépést](../../../00-course-setup).

A repó gyökérkönyvtárában található egy `requirements.txt` fájl, amely tartalmazza a szükséges Python csomagokat a kódminták futtatásához.

Telepítheted őket az alábbi paranccsal a repó gyökérkönyvtárában:

```bash|powershell
pip install -r requirements.txt
```

Ajánlott Python virtuális környezet létrehozása az összeférhetetlenségek és problémák elkerülése érdekében.

## VSCode beállítása

Győződj meg róla, hogy a megfelelő Python verziót használod a VSCode-ban.

![kép](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry és Azure AI Agent Service beállítása

### 1. lépés: Microsoft Foundry projekt létrehozása

Szükséged van egy Azure AI Foundry **hubra** és **projektre** telepített modellel a notebookok futtatásához.

1. Lépj be a [ai.azure.com](https://ai.azure.com) oldalra az Azure fiókoddal.
2. Hozz létre egy **hubot** (vagy használj egy meglévőt). Lásd: [Hub erőforrások áttekintése](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. A hubon belül hozz létre egy **projektet**.
4. Telepíts egy modellt (például `gpt-4o`) a **Models + Endpoints** → **Deploy model** menüpontból.

### 2. lépés: Szerezz be a projekt végpontját és a modell telepítésének nevét

A Microsoft Foundry portálon a projektednél:

- **Projekt végpont** — Lépj az **Áttekintés** oldalra és másold ki a végpont URL-t.

![Projekt kapcsolat string](../../../translated_images/hu/project-endpoint.8cf04c9975bbfbf1.webp)

- **Modell telepítés neve** — Lépj a **Models + Endpoints** menübe, válaszd ki a telepített modellt, és jegyezd meg a **Deployment name**-et (pl. `gpt-4o`).

### 3. lépés: Jelentkezz be az Azure-ba az `az login` paranccsal

Minden notebook az **`AzureCliCredential`**-t használja hitelesítéshez – nincs szükség API kulcsok kezelésére. Ehhez az Azure CLI-n keresztüli bejelentkezés szükséges.

1. **Telepítsd az Azure CLI-t**, ha még nincs: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Jelentkezz be** az alábbi paranccsal:

    ```bash|powershell
    az login
    ```

    Vagy ha távoli/Codespace környezetben vagy böngésző nélkül:

    ```bash|powershell
    az login --use-device-code
    ```

3. Válaszd ki az előfizetésedet, ha megkérdezi – azt, amelyik tartalmazza a Foundry projektedet.

4. Ellenőrizd, hogy be vagy jelentkezve:

    ```bash|powershell
    az account show
    ```

> **Miért `az login`?** A notebookok az `AzureCliCredential`-t használják az `azure-identity` csomagból a hitelesítéshez. Ez azt jelenti, hogy az Azure CLI munkameneted biztosítja a hitelesítő adatokat – nincs szükség API kulcsokra vagy titkokra `.env` fájlban. Ez egy [biztonsági bevált gyakorlat](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### 4. lépés: Hozd létre a `.env` fájlodat

Másold le a példa fájlt:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Nyisd meg a `.env` fájlt és írd be ezeket az értékeket:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Változó | Hol találod meg |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portál → a projekted → **Áttekintő** oldal |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portál → **Models + Endpoints** → a telepített modell neve |

Ennyi az egész a legtöbb leckéhez! A notebookok automatikusan hitelesítenek az `az login` munkameneted alapján.

### 5. lépés: Telepítsd a Python függőségeket

```bash|powershell
pip install -r requirements.txt
```

Ajánlott ezt a már létrehozott virtuális környezeten belül futtatni.

## További beállítás az 5. leckéhez (Agentic RAG)

Az 5. lecke az **Azure AI Search**-t használja a retrieval-augmented generationhöz. Ha ezt a leckét szeretnéd futtatni, add hozzá ezeket a változókat a `.env` fájlodhoz:

| Változó | Hol találod meg |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portál → az **Azure AI Search** erőforrásod → **Áttekintő** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portál → az **Azure AI Search** erőforrásod → **Beállítások** → **Kulcsok** → elsődleges admin kulcs |

## További beállítás a 6. és 8. leckékhez (GitHub modellek)

A 6. és 8. leckében néhány notebook **GitHub modelleket** használ Azure AI Foundry helyett. Ha ezeket a mintákat futtatni szeretnéd, add hozzá ezeket a változókat a `.env` fájlodhoz:

| Változó | Hol találod meg |
|----------|-----------------|
| `GITHUB_TOKEN` | GitHub → **Beállítások** → **Fejlesztői beállítások** → **Személyes hozzáférési tokenek** |
| `GITHUB_ENDPOINT` | Használd a `https://models.inference.ai.azure.com` URL-t (alapértelmezett érték) |
| `GITHUB_MODEL_ID` | A használandó modell neve (pl. `gpt-4o-mini`) |

## További beállítás a 8. leckéhez (Bing Grounding munkafolyamat)

A 8. leckében a feltételes munkafolyamat notebookja a **Bing grounding**-et használja az Azure AI Foundry-n keresztül. Ha ezt a mintát szeretnéd futtatni, add hozzá ezt a változót a `.env` fájlodhoz:

| Változó | Hol találod meg |
|----------|-----------------|
| `BING_CONNECTION_ID` | Azure AI Foundry portál → a projekted → **Kezelés** → **Csatlakoztatott erőforrások** → a Bing kapcsolatod → másold ki a kapcsolódási azonosítót |

## Hibakeresés

### SSL tanúsítványellenőrzési hibák macOS-en

Ha macOS-en vagy, és ilyen hibát kapsz:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Ez egy ismert probléma Python alatt macOS-en, ahol a rendszer SSL tanúsítványokat nem bízzák automatikusan meg. Próbáld ki az alábbi megoldásokat sorban:

**1. lehetőség: Fuss le a Python Install Certificates scriptet (ajánlott)**

```bash
# Cseréld ki a 3.XX-et a telepített Python verziódra (pl. 3.12 vagy 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**2. lehetőség: Használd a `connection_verify=False` opciót a notebook-ban (csak GitHub Modellekhez)**

A 6. lecke notebook-jában (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) már van egy kikommentelt megoldás erre. Vedd ki a kommentet `connection_verify=False`-nál a kliens létrehozásakor:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Kapcsolja ki az SSL ellenőrzést, ha tanúsítványhibákba ütközik
)
```

> **⚠️ Figyelem:** Az SSL ellenőrzés letiltása (`connection_verify=False`) csökkenti a biztonságot a tanúsítvány ellenőrzésének kihagyásával. Csak fejlesztési környezetben, átmeneti megoldásként használd, soha ne éles környezetben.

**3. lehetőség: Telepítsd és használd a `truststore`-t**

```bash
pip install truststore
```

Majd ezt add hozzá a notebook vagy szkript tetejéhez, mielőtt hálózati hívásokat kezdeményeznél:

```python
import truststore
truststore.inject_into_ssl()
```

## Elakadtál valahol?

Ha probléma merül fel a beállításkor, lépj be az <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> szerverére vagy <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">nyiss hibajegyet</a>.

## Következő lecke

Most már készen állsz a tanfolyam kódjának futtatására. Sok sikert az AI ügynökök világának megismeréséhez!

[Bevezetés az AI ügynökökbe és az ügynökök használati esetei](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár igyekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások tartalmazhatnak hibákat vagy pontatlanságokat. Az eredeti dokumentum anyanyelvén tekintendő hivatalos forrásnak. Kritikus információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget az ebből eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->