# Tanfolyam beállítása

## Bevezetés

Ebben az órában megtanuljuk, hogyan futtathatod az ezen tanfolyam kódmintáit.

## Csatlakozz más tanulókhoz és kérj segítséget

Mielőtt elkezdenéd klónozni a repódat, csatlakozz az [AI Agents For Beginners Discord csatornához](https://aka.ms/ai-agents/discord), hogy segítséget kapj a beállításhoz, kérdéseidre választ találj a tanfolyammal kapcsolatban, vagy hogy kapcsolatba léphess más tanulókkal.

## Klónozd vagy forkold ezt a repót

Első lépésként kérlek klónozd vagy forkold a GitHub-tárhelyet. Ezáltal saját verziója lesz a tananyagnak, amelyen futtathatod, tesztelheted és módosíthatod a kódot!

Ezt elvégezheted a <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">repó fork-olása</a> linkre kattintva.

Most már meg kell, hogy legyen a saját fork-olt verziód erről a tanfolyamról a következő linken:

![Forkolt repó](../../../translated_images/hu/forked-repo.33f27ca1901baa6a.webp)

### Felületes klónozás (ajánlott workshophoz / Codespaces használathoz)

  >A teljes repó letöltése, amely tartalmazza az egész előzményt és minden fájlt, nagy lehet (~3 GB). Ha csak a workshopon veszel részt, vagy csak néhány leckefejlécet kell letöltened, egy felületes klónozás (vagy ritkított klónozás) elkerüli a legtöbb adatletöltést azáltal, hogy megszakítja az előzményeket és/vagy kihagyja a blobokat.

#### Gyors felületes klónozás — minimális előzmény, minden fájl

A lenti parancsokban cseréld ki a `<your-username>` helyet a fork URL-edre (vagy az upstream URL-re, ha azt használod).

Csak a legfrissebb commit előzményeket klónozásához (kicsi letöltés):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Egy adott ág klónozásához:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Részleges (ritkított) klónozás — minimális blob + csak kiválasztott mappák

Ez részleges klónozást és sparse-checkout-ot használ (szükséges Git 2.25+ és ajánlott modern Git részleges klónozási támogatással):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Lépj be a repó könyvtárba:

```bash|powershell
cd ai-agents-for-beginners
```

Ezután add meg, melyik könyvtárakat szeretnéd (a példa két mappát mutat):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

A klónozás és a fájlok ellenőrzése után, ha csak a fájlokra van szükséged és helyet akarsz felszabadítani (nem kell git előzmény), töröld a repó metaadatait (💀visszafordíthatatlan — elveszíted az összes Git funkciót: nincs commit, pull, push vagy előzmény elérés).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces használata (ajánlott a nagy helyi letöltések elkerülésére)

- Hozz létre egy új Codespace-et ehhez a repóhoz a [GitHub UI](https://github.com/codespaces) segítségével.

- A nemrég létrehozott codespace termináljában futtass egyet a fenti felületes/ritkított klónozó parancsok közül, hogy csak a szükséges leckefájlokat hozd be a Codespace munkaterületére.
- Opcionális: a Codespaces-en belüli klónozás után töröld a .git-et, hogy helyet szabadíts fel (lásd a fentebb adott törlési parancsokat).
- Megjegyzés: Ha inkább közvetlenül nyitnád meg a repót Codespaces-ben (klónozás nélkül), vedd figyelembe, hogy Codespaces felállítja a devcontainer környezetet, és talán több dolgot is telepít, mint amire szükséged van. Egy friss Codespace-en belüli felületes klónozás nagyobb irányítást ad a lemezhasználat felett.

#### Tippek

- Mindig cseréld le a klónozási URL-t a saját forkodra, ha szerkeszteni vagy commitolni szeretnél.
- Ha később több előzményre vagy fájlokra van szükséged, letöltheted azokat, vagy beállíthatod a sparse-checkout-ot további mappák bevonására.

## A kód futtatása

Ez a tanfolyam egy sor Jupyter notebookot kínál, amelyeket futtatva gyakorlati tapasztalatot szerezhetsz AI ügynökök építésében.

A kódminták a **Microsoft Agent Framework (MAF)**-et használják a `FoundryChatClient`-tel, amely kapcsolódik a **Microsoft Foundry Agent Service V2**-höz (az Responses API-hoz) a **Microsoft Foundry** segítségével.

Minden Python notebook címkéje `*-python-agent-framework.ipynb`.

## Követelmények

- Python 3.12+
  - **MEGJEGYZÉS**: Ha nincs telepítve a Python 3.12, győződj meg róla, hogy telepíted. Ezután hozd létre a virtuális környezeted python3.12-vel, hogy a requirements.txt fájlból a megfelelő verziók települjenek.
  
    >Példa

    Python venv könyvtár létrehozása:

    ```bash|powershell
    python -m venv venv
    ```

    Ezután aktiváld a virtuális környezetet:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: A .NET-et használó mintakódokhoz győződj meg arról, hogy telepítve van a [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) vagy újabb. Ellenőrizd az installált .NET SDK verziót:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Szükséges az azonosításhoz. Telepítsd a [aka.ms/installazurecli](https://aka.ms/installazurecli) weboldalról.
- **Azure előfizetés** — Hozzáféréshez a Microsoft Foundry és Microsoft Foundry Agent Service használatához.
- **Microsoft Foundry projekt** — Egy modell-leképzéssel rendelkező projekt (pl. `gpt-5-mini`). Lásd [1. lépést](#1-lépés-microsoft-foundry-projekt-létrehozása) lent.

A repó gyökerében található egy `requirements.txt` fájl, amely tartalmaz minden Python csomagot a kódminták futtatásához.

A telepítéshez futtasd a következő parancsot a repó gyökerében a terminálban:

```bash|powershell
pip install -r requirements.txt
```

Ajánljuk egy Python virtuális környezet létrehozását az esetleges konfliktusok és problémák elkerülésére.

## VSCode beállítása

Győződj meg arról, hogy a megfelelő Python verziót használod a VSCode-ban.

![kép](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry és Microsoft Foundry Agent Service beállítása

### 1. lépés: Microsoft Foundry projekt létrehozása

Szükséged van egy Microsoft Foundry **hub**-ra és **projektre** telepített modellel a notebookok futtatásához.

1. Lépj a [ai.azure.com](https://ai.azure.com) oldalra és jelentkezz be Azure fiókoddal.
2. Hozz létre egy **hub-ot** (vagy használj létezőt). Lásd: [Hub erőforrások áttekintése](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. A hub-ban hozz létre egy **projektet**.
4. Telepíts egy modellt (pl. `gpt-5-mini`) a **Models + Endpoints** → **Deploy model** menüpontból.

### 2. lépés: Szerezd meg a projekt végpontját és a modell telepítésének nevét

A Microsoft Foundry portálon a projektedből:

- **Projekt végpont** — Nyisd meg az **Áttekintés** oldalt és másold ki a végpont URL-jét.

![Projekt Kapcsolati karakterlánc](../../../translated_images/hu/project-endpoint.8cf04c9975bbfbf1.webp)

- **Modell telepítés neve** — Menj a **Models + Endpoints** részhez, válaszd ki a telepített modelled, és jegyezd fel a **Deployment name**-et (pl. `gpt-5-mini`).

### 3. lépés: Jelentkezz be az Azure-ba az `az login` segítségével

Minden notebook az **`AzureCliCredential`**-et használja az azonosításhoz — nincs API kulcs kezelés. Ehhez be kell jelentkezned az Azure CLI segítségével.

1. **Telepítsd az Azure CLI-t**, ha még nincs fent: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Jelentkezz be** a következő parancs futtatásával:

    ```bash|powershell
    az login
    ```

    Vagy ha távoli/Codespace környezetben vagy böngésző nélkül:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Válaszd ki az előfizetésedet**, ha erre kérdés érkezik — válaszd azt, amelyik tartalmazza a Foundry projekted.

4. **Ellenőrizd**, hogy be vagy-e jelentkezve:

    ```bash|powershell
    az account show
    ```

> **Miért `az login`?** A notebookok az `azure-identity` csomagból származó `AzureCliCredential`-t használják az azonosításhoz. Ez azt jelenti, hogy az Azure CLI munkameneted szolgáltatja a hitelesítő adatokat — nincs API kulcs vagy titok a `.env` fájlban. Ez egy [biztonsági legjobb gyakorlat](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### 4. lépés: Készítsd el a `.env` fájlodat

Másold ki a példafájlt:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Nyisd meg a `.env` fájlt és töltsd ki a következő két értéket:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Változó | Hol találod meg |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portál → a projekted → **Áttekintés** oldal |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portál → **Models + Endpoints** → a telepített modell neve |

Ennyi az egész a legtöbb leckéhez! A notebookok automatikusan autentikálnak az `az login` munkameneteden keresztül.

### 5. lépés: Telepítsd a Python függőségeket

```bash|powershell
pip install -r requirements.txt
```

Ajánlott ezt a már létrehozott virtuális környezeten belül futtatni.

## További beállítás az 5. leckéhez (Agentic RAG)

Az 5. lecke az **Azure AI Search**-t használja a lekérdezésekkel kiegészített generáláshoz. Ha ezt a leckét futtatni szeretnéd, add hozzá ezeket a változókat a `.env` fájlhoz:

| Változó | Hol találod meg |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portál → az **Azure AI Search** erőforrásod → **Áttekintés** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portál → az **Azure AI Search** erőforrásod → **Beállítások** → **Kulcsok** → elsődleges admin kulcs |

## További beállítás a Azure OpenAI-t közvetlenül hívó leckékhez (6. és 8. lecke)

A 6. és 8. lecke néhány notebookja közvetlenül az **Azure OpenAI**-t hívja (a **Responses API**-n keresztül) ahelyett, hogy Microsoft Foundry projekten keresztül menne. Ezek a minták korábban GitHub Modelleket használtak, ami elavult (2026 júliusában kivezetés alatt áll) és nem támogatja a Responses API-t. Ha ezeket a mintákat futtatod, add hozzá ezeket a változókat a `.env` fájlhoz:

| Változó | Hol találod meg |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portál → az **Azure OpenAI** erőforrásod → **Kulcsok és végpont** → Végpont (pl. `https://<az-erőforrásod>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | A telepített modell neve (pl. `gpt-5-mini`), amely támogatja a Responses API-t |
| `AZURE_OPENAI_API_KEY` | Opcionális — csak ha kulcsalapú hitelesítést használsz `az login` / Entra ID helyett |

> A Responses API a stabil `/openai/v1/` végpontot használja, így nem kell `api-version` megadni. Jelentkezz be az `az login` segítségével, hogy kulcs nélküli Entra ID azonosítást használhass.

## Alternatív szolgáltató: MiniMax (OpenAI-kompatibilis)

A [MiniMax](https://platform.minimaxi.com/) nagy kontextusú modelleket kínál (akár 204K token) OpenAI-kompatibilis API-n keresztül. Mivel a Microsoft Agent Framework `OpenAIChatClient`-je bármely OpenAI-kompatibilis végponttal működik, a MiniMax használható helyettesítőként az Azure OpenAI vagy OpenAI helyett.

Add hozzá ezeket a változókat a `.env` fájlhoz:

| Változó | Hol találod meg |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API kulcsok |
| `MINIMAX_BASE_URL` | Használd a `https://api.minimax.io/v1` (alapértelmezett) értéket |
| `MINIMAX_MODEL_ID` | A használandó modell neve (pl. `MiniMax-M3`) |

**Példamodellek**: `MiniMax-M3` (ajánlott), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (gyorsabb válaszidő). A modellnevek és elérhetőség idővel változhatnak, és egy adott modellhez való hozzáférés fióktól vagy régiótól függ — a jelenlegi listáért nézd meg a [MiniMax Platformot](https://platform.minimaxi.com/). Ha a `MiniMax-M3` nem elérhető a fiókod számára, állítsd be a `MINIMAX_MODEL_ID` változót olyan modellre, amelyhez hozzáférsz (pl. `MiniMax-M2.7`).

A `OpenAIChatClient`-et használó minták (pl. 14. lecke, szállodafoglalás munkafolyamat) automatikusan érzékelik és használják majd MiniMax konfigurációd, ha be van állítva a `MINIMAX_API_KEY`.

## Alternatív szolgáltató: Foundry Local (Futtatás eszközön)

A [Foundry Local](https://foundrylocal.ai) egy könnyűsúlyú futtatókörnyezet, amely nyelvi modelleket tölt le, kezel és szolgáltat teljes egészében saját gépeden OpenAI-kompatibilis API-n keresztül — nincs felhő, nincs Azure előfizetés, és nem kell API kulcsokat használnod. Kiváló offline fejlesztéshez, kísérletezéshez felhőköltségek nélkül, vagy adatokat helyben tartva.

Mivel a Microsoft Agent Framework `OpenAIChatClient`-je bármilyen OpenAI-kompatibilis végponttal működik, a Foundry Local helyi alternatívaként szolgálhat az Azure OpenAI helyett.

**1. Telepítsd a Foundry Local-t**

```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install foundrylocal
```

**2. Tölts le és futtass egy modellt** (ez elindítja a helyi szolgáltatást is):

```bash
foundry model list          # elérhető modellek megtekintése
foundry model run phi-4-mini
```

**3. Telepítsd a Python SDK-t**, amellyel felfedezheted a helyi végpontot:

```bash
pip install foundry-local-sdk
```

**4. Állítsd be a Microsoft Agent Framework-öt a helyi modelledre:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Letölti (ha szükséges) és helyben szolgálja ki a modellt, majd felfedezi a végpontot/portot.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # pl. http://localhost:<port>/v1
    api_key=manager.api_key,        # mindig "nem szükséges" a Foundry Local esetén
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Megjegyzés:** A Foundry Local egy OpenAI-kompatibilis **Chat Completions** végpontot szolgáltat. Használd helyi fejlesztéshez és offline forgatókönyvekhez. A teljes **Responses API** szolgáltatáskészlethez (állapotkövető beszélgetések, mély eszköz-orchestration, és ügynök-stílusú fejlesztés) használd az **Azure OpenAI**-t vagy egy **Microsoft Foundry** projektet, ahogy a leckékben látható. Lásd a [Foundry Local dokumentációját](https://foundrylocal.ai) a jelenlegi modellkatalógusért és platform támogatásért.

## További beállítás a 8. leckéhez (Bing Grounding munkafolyamat)


A 8. lecke feltételes munkafolyamat jegyzete a Microsoft Foundry által biztosított **Bing alaperőre** támaszkodik. Ha futtatni szeretnéd ezt a példát, add hozzá ezt a változót a `.env` fájlodhoz:

| Változó | Hol találod meg |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry portál → a projekted → **Management** → ** kapcsolódó erőforrások** → a Bing kapcsolatod → másold ki a kapcsolat azonosítóját |

## Hibakeresés

### SSL tanúsítvány ellenőrzési hibák macOS rendszeren

Ha macOS rendszeren ilyen hibába ütközöl:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Ez egy ismert probléma a Python macOS verziójánál, ahol a rendszer SSL tanúsítványai nincsenek automatikusan megbízhatónak jelölve. Próbáld ki a következő megoldásokat sorban:

**1. lehetőség: Futtasd Python Install Certificates szkriptjét (ajánlott)**

```bash
# Cseréld ki a 3.XX-et a telepített Python verziódra (pl. 3.12 vagy 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**2. lehetőség: Használd a `connection_verify=False` beállítást a jegyzetedben (csak GitHub Models jegyzetekhez)**

A 6. lecke jegyzetében (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) már benne van egy kikommentezett megoldás. Kommenteld ki a `connection_verify=False` sort a kliens létrehozásakor:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Tiltsa le az SSL ellenőrzést, ha tanúsítványhibákat tapasztal
)
```

> **⚠️ Figyelem:** Az SSL ellenőrzés kikapcsolása (`connection_verify=False`) a tanúsítvány validálás kihagyásával csökkenti a biztonságot. Csak fejlesztői környezetben, ideiglenes megoldásként használd, soha ne éles környezetben.

**3. lehetőség: Telepítsd és használd a `truststore`-t**

```bash
pip install truststore
```

Ezután add hozzá a következőt a jegyzet vagy szkript elejére, mielőtt hálózati hívásokat indítanál:

```python
import truststore
truststore.inject_into_ssl()
```

## Elakadtál valahol?

Ha problémád adódik a beállítással, gyere el az <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord csatornára</a> vagy <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">jelents hibát</a>.

## Következő lecke

Most már készen állsz a kurzus kódjának futtatására. Jó tanulást az AI ügynökök világához!

[Bevezetés az AI ügynökökbe és használati esetekbe](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->