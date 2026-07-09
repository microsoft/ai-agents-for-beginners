# Kurzusbeállítás

## Bevezetés

Ez a lecke bemutatja, hogyan futtathatók a kurzus kódpéldái.

## Csatlakozz más tanulókhoz és kérj segítséget

Mielőtt elkezdenéd klónozni a repód, csatlakozz az [AI Agents For Beginners Discord csatornához](https://aka.ms/ai-agents/discord), hogy segítséget kapj a beállításhoz, kérdéseket tegyél fel a kurzussal kapcsolatban, vagy kapcsolatba lépj más tanulókkal.

## Klónozd vagy forkold ezt a repót

Kezdésként kérlek, klónozd vagy forkold a GitHub tárhelyet. Ez által létrejön a saját verziód a kurzus anyagából, hogy futtathasd, tesztelhesd és módosíthasd a kódot!

Ezt megteheted az <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">repo fork-olása</a> linkre kattintva

Most már megvan a saját, fork-olt verziód erről a kurzusról az alábbi linken:

![Forked Repo](../../../translated_images/hu/forked-repo.33f27ca1901baa6a.webp)

### Shallow Clone (ajánlott műhelyhez / Codespaceshez)

  >A teljes tárhely nagy lehet (~3 GB), ha letöltöd az összes előzményt és fájlt. Ha csak a műhelyre jársz vagy csak néhány leckefüzetre van szükséged, egy shallow clone (vagy sparse clone) elkerüli a legtöbb letöltést az előzmények rövidítésével és/vagy blobok kihagyásával.

#### Gyors shallow clone — minimális előzmény, minden fájl

Cseréld ki a `<your-username>` részt az alábbi parancsokban a fork URL-edre (vagy upstream URL-re, ha azt preferálod).

Csak a legfrissebb commit előzmény klónozásához (kis letöltés):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Egy adott ág klónozásához:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Részleges (sparse) klón — minimális blobok + csak kiválasztott mappák

Ez részleges klónt és sparse-checkoutot használ (Git 2.25+ szükséges és ajánlott modern Git részleges klón támogatással):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Lépj be a repó mappába:

```bash|powershell
cd ai-agents-for-beginners
```

Ezután határozd meg, mely mappákat szeretnéd (példa két mappát mutat):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

A klónozás és a fájlok ellenőrzése után, ha csak fájlokra van szükséged és helyet akarsz felszabadítani (nincs git előzmény), kérlek töröld a repository metaadatokat (💀visszafordíthatatlan — elveszíted a Git funkciókat: nem lesznek commitok, pullok, pushok vagy előzmény hozzáférés).

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces használata (ajánlott a helyi nagy letöltések elkerülésére)

- Hozz létre új Codespace-t ehhez a repóhoz a [GitHub UI](https://github.com/codespaces) segítségével.  

- A frissen létrehozott codespace termináljában futtasd az egyik shallow/sparse clone parancsot fent, hogy csak a szükséges leckefüzetek kerüljenek a Codespace munkaterületébe.
- Opcionális: a klónozás után Codespaces-ben töröld a .git-et a hely felszabadításához (lásd fent a törlési parancsokat).
- Megjegyzés: Ha inkább közvetlenül a repót nyitod meg Codespaces-ben (klónozás nélkül), tudd, hogy a Codespaces létrehozza a devcontainer környezetet, és nagyobb erőforrásokat is előkészíthet, mint amire szükséged van. Egy friss Codespaces-ben történő shallow klónozás nagyobb kontrollt ad a lemezhasználat felett.

#### Tippek

- Mindig cseréld ki a klón URL-t a forkodra, ha szerkeszteni/commitolni akarsz.
- Ha később több előzményre vagy fájlra van szükséged, lekérdezheted azokat vagy módosíthatod a sparse-checkoutot további mappák bevonására.

## A kód futtatása

Ez a kurzus számos Jupyter Notebookot kínál, amelyeket futtatva gyakorlati tapasztalatot szerezhetsz AI Agentek építésében.

A kódpéldák a **Microsoft Agent Framework (MAF)**-et használják a `FoundryChatClient`-tel, amely a **Microsoft Foundry Agent Service V2**-hez (a Responses API-hoz) csatlakozik a **Microsoft Foundry**-n keresztül.

Minden Python notebook `*-python-agent-framework.ipynb` jelöléssel rendelkezik.

## Követelmények

- Python 3.12+
  - **MEGJEGYZÉS**: Ha még nincs telepítve a Python3.12, telepítsd azt. Ezután hozd létre a virtual environment-ed python3.12-vel, hogy biztosítsd a requirements.txt-ben megadott helyes verziók telepítését.
  
    >Példa

    Python venv könyvtár létrehozása:

    ```bash|powershell
    python -m venv venv
    ```

    Ezután aktiváld a venv környezetet:

    ```bash
    # zsh/bash
    source venv/bin/activate
    ```
  
    ```dos
    # Command Prompt for Windows
    venv\Scripts\activate
    ```

- .NET 10+: A .NET példák futtatásához telepítsd a [.NET 10 SDK-t](https://dotnet.microsoft.com/download/dotnet/10.0) vagy újabbat. Ezután ellenőrizd az SDK verziódat:

    ```bash|powershell
    dotnet --list-sdks
    ```

- **Azure CLI** — Szükséges az azonosításhoz. Telepítsd innen: [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure előfizetés** — A Microsoft Foundry és Foundry Agent Service eléréséhez.
- **Microsoft Foundry projekt** — Olyan projekt, amelybe telepítve van egy modell (pl. `gpt-4o`). Lásd [1. lépés](#1-lépés-microsoft-foundry-projekt-létrehozása) alább.

Tartalmazunk egy `requirements.txt` fájlt a repó gyökerében, amely az összes szükséges Python csomagot felsorolja a kódpéldák futtatásához.

Telepítheted őket a terminálban, a repó gyökerében a következő paranccsal:

```bash|powershell
pip install -r requirements.txt
```

Javasoljuk egy Python virtuális környezet létrehozását a konfliktusok és problémák elkerülésére.

## VSCode beállítása

Győződj meg róla, hogy a megfelelő Python verziót használod a VSCode-ban.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry és Foundry Agent Service beállítása

### 1. lépés: Microsoft Foundry projekt létrehozása

Egy Microsoft Foundry **hub**-ra és **projektre** van szükséged, amelyben telepítve van egy modell a jegyzetfüzetek futtatásához.

1. Látogass el az [ai.azure.com](https://ai.azure.com) oldalra, és jelentkezz be Azure fiókoddal.
2. Hozz létre egy **hubot** (vagy használj egy meglévőt). Lásd: [Hub erőforrások áttekintése](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. A hubon belül hozz létre egy **projektet**.
4. Telepíts egy modellt (pl. `gpt-4o`) a **Models + Endpoints** → **Deploy model** menüpontból.

### 2. lépés: Projekt végpont és modell telepítési név lekérése

A Microsoft Foundry portálon a projektedből:

- **Projekt végpont** — Menj az **Áttekintés** oldalra, és másold ki a végpont URL-t.

![Project Connection String](../../../translated_images/hu/project-endpoint.8cf04c9975bbfbf1.webp)

- **Modell telepítési név** — Menj a **Models + Endpoints** részhez, válaszd ki a telepített modelljeidet, és jegyezd fel a **Deployment name**-et (pl. `gpt-4o`).

### 3. lépés: Jelentkezz be az Azure CLI-vel `az login`-nel

Minden jegyzetfüzet a **`AzureCliCredential`** azonosítást használja — nincs szükség API kulcsok kezelgetésére. Ez megköveteli, hogy be legyél jelentkezve az Azure CLI-n keresztül.

1. **Telepítsd az Azure CLI-t**, ha még nincs: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Jelentkezz be** a következő paranccsal:

    ```bash|powershell
    az login
    ```

    Vagy, ha távoli/Codespace környezetben vagy böngésző nélkül:

    ```bash|powershell
    az login --use-device-code
    ```

3. **Válaszd ki az előfizetésed**, ha kéri — azt válaszd, amelyik tartalmazza a Foundry projekted.

4. **Ellenőrizd**, hogy be vagy jelentkezve:

    ```bash|powershell
    az account show
    ```

> **Miért `az login`?** A jegyzetfüzetek az `azure-identity` csomagban lévő `AzureCliCredential`-t használják az azonosításhoz. Ez azt jelenti, hogy az Azure CLI munkameneted biztosítja a hitelesítést — nincs szükség API kulcsokra vagy titkokra a `.env` fájlban. Ez egy [biztonsági ajánlás](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

### 4. lépés: Hozd létre a `.env` fájlodat

Másold az példafájlt:

```bash
# zsh/bash
cp .env.example .env
```

```powershell
# PowerShell
Copy-Item .env.example .env
```

Nyisd meg a `.env` fájlt, és töltsd ki ezeket az értékeket:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-4o
```

| Változó | Hol találod meg |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portál → projekted → **Áttekintés** oldal |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portál → **Models + Endpoints** → telepített modell neve |

Ennyi a legtöbb leckéhez! A jegyzetfüzetek automatikusan hitelesítenek az `az login` munkameneteden keresztül.

### 5. lépés: Telepítsd a Python függőségeket

```bash|powershell
pip install -r requirements.txt
```

Ajánlott, hogy ezt abban a virtuális környezetben futtasd, amit korábban létrehoztál.

## További beállítás az 5. leckéhez (Agentic RAG)

Az 5. lecke az **Azure AI Search**-t használja a visszakeresés központú generáláshoz. Ha ezt a leckét futtatni szeretnéd, add hozzá ezeket a változókat a `.env` fájlodhoz:

| Változó | Hol találod meg |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portál → **Azure AI Search** erőforrásod → **Áttekintés** → URL |
| `AZURE_SEARCH_API_KEY` | Azure portál → **Azure AI Search** erőforrásod → **Beállítások** → **Kulcsok** → elsődleges admin kulcs |

## További beállítás a közvetlen Azure OpenAI hívásos leckékhez (6. és 8. lecke)

Néhány 6. és 8. leckében lévő jegyzetfüzet közvetlenül az **Azure OpenAI**-t használja (a **Responses API**-n keresztül), ahelyett, hogy Microsoft Foundry projektet használnának. Ezek a példák korábban a GitHub Models-t használták, amely elavult (2026 júliusában megszűnik) és nem támogatja a Responses API-t. Ha ezeket a példákat futtatni szeretnéd, add hozzá ezeket a változókat a `.env` fájlodhoz:

| Változó | Hol találod meg |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portál → **Azure OpenAI** erőforrásod → **Kulcsok és végpont** → Végpont (pl. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | Telepített modell neve (pl. `gpt-4o-mini`), amely támogatja a Responses API-t |
| `AZURE_OPENAI_API_KEY` | Opcionális — csak ha kulcs alapú hitelesítést használsz az `az login` / Entra ID helyett |

> A Responses API a stabil `/openai/v1/` végpontot használja, így nincs szükség `api-version` megadásra. Jelentkezz be `az login`-nel a kulcs nélküli Entra ID hitelesítéshez.

## Alternatív szolgáltató: MiniMax (OpenAI-kompatibilis)

A [MiniMax](https://platform.minimaxi.com/) nagy kontextusú modelleket (akár 204K tokenig) biztosít OpenAI-kompatibilis API-n keresztül. Mivel a Microsoft Agent Framework `OpenAIChatClient`-je bármely OpenAI-kompatibilis végponttal működik, a MiniMax használható helyettesítőként Azure OpenAI vagy OpenAI helyett.

Add hozzá ezeket a változókat a `.env` fájlodhoz:

| Változó | Hol találod meg |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API kulcsok |
| `MINIMAX_BASE_URL` | Használd a `https://api.minimax.io/v1` (alapértelmezett érték) |
| `MINIMAX_MODEL_ID` | Használt modell neve (pl. `MiniMax-M3`) |

**Példa modellek**: `MiniMax-M3` (ajánlott), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (gyorsabb válaszok). A modellnevek és elérhetőség változhat idővel, és egyes modellekhez való hozzáférés az adott fióktól vagy régiótól függ — nézd meg a [MiniMax Platformot](https://platform.minimaxi.com/) a jelenlegi listáért. Ha a `MiniMax-M3` nem elérhető a fiókodhoz, állítsd be a `MINIMAX_MODEL_ID`-t olyan modellre, amihez hozzáférsz (pl. `MiniMax-M2.7`).

Azok a kódpéldák, amelyek az `OpenAIChatClient`-et használják (pl. a 14. leckében a hotelfoglalási munkafolyamat), automatikusan észlelik és használják a MiniMax konfigurációdat, ha be van állítva a `MINIMAX_API_KEY`.

## Alternatív szolgáltató: Foundry Local (Modellek futtatása saját gépen)

A [Foundry Local](https://foundrylocal.ai) egy könnyű futtatókörnyezet, amely letölti, kezeli, és helyben szolgáltatja a nyelvi modelleket **teljes egészében a saját gépeden** OpenAI-kompatibilis API-n keresztül — nincs felhő, nincs Azure előfizetés, nincs API kulcs. Ez remek választás offline fejlesztéshez, kísérletezéshez felhő költségek nélkül, vagy az adatok helyben tartásához.

Mivel a Microsoft Agent Framework `OpenAIChatClient`-je bármely OpenAI-kompatibilis végponttal működik, a Foundry Local egy helyi alternatíva az Azure OpenAI-hez.

**1. Telepítsd a Foundry Localt**

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

**3. Telepítsd a Python SDK-t**, amivel megtalálod a helyi végpontot:

```bash
pip install foundry-local-sdk
```

**4. Irányítsd a Microsoft Agent Framework-öt a helyi modellre:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Letölti (ha szükséges) és helyben szolgáltatja a modellt, majd felderíti a végpontot/portot.
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

> **Megjegyzés:** A Foundry Local egy OpenAI-kompatibilis **Chat Completions** végpontot kínál. Használd helyi fejlesztéshez és offline forgatókönyvekhez. A teljes **Responses API** funkciókészletért (állapot tartó beszélgetések, mély eszköz koordináció, ügynök-stílusú fejlesztés) célzottan az **Azure OpenAI** vagy egy **Microsoft Foundry** projekteket használj, ahogy a leckék mutatják. Lásd a [Foundry Local dokumentációt](https://foundrylocal.ai) a jelenlegi modell katalógusért és platform támogatásért.

## További beállítás a 8. leckéhez (Bing grounding munkafolyamat)


A 8. leckében található feltételes munkafolyamat jegyzetfüzet **Bing alapozást** használ a Microsoft Foundry-n keresztül. Ha futtatni szeretnéd ezt a példát, add hozzá ezt a változót a `.env` fájlodhoz:

| Változó | Hol található |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry portál → a projekted → **Kezelés** → **Csatlakoztatott erőforrások** → a Bing kapcsolatod → másold ki a kapcsolat azonosítóját |

## Hibakeresés

### SSL tanúsítvány ellenőrzési hibák macOS rendszeren

Ha macOS-t használsz és a következő hibát észleled:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Ez egy ismert probléma a Python macOS verziójánál, ahol a rendszer SSL tanúsítványai nem kerülnek automatikusan megbízhatóként kezelésre. Próbáld ki a következő megoldásokat sorrendben:

**1. lehetőség: Futtasd a Python Install Certificates szkriptjét (ajánlott)**

```bash
# Cseréld le a 3.XX-et a telepített Python verziódra (pl. 3.12 vagy 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**2. lehetőség: Használd a `connection_verify=False` opciót a jegyzetfüzetedben (csak GitHub Modellek jegyzetfüzetekhez)**

A 6. leckében található jegyzetfüzetben (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) már szerepel egy kikommentelt megoldás. Vedd ki a kommentet a `connection_verify=False` sorból, amikor létrehozod az ügyfelet:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # Tiltsa le az SSL ellenőrzést, ha tanúsítványhibákba ütközik
)
```

> **⚠️ Figyelem:** Az SSL ellenőrzés kikapcsolása (`connection_verify=False`) csökkenti a biztonságot, mert kihagyja a tanúsítvány érvényesítését. Ezt csak fejlesztési környezetekben, ideiglenes megoldásként használd, soha ne éles környezetben.

**3. lehetőség: Telepítsd és használd a `truststore`-t**

```bash
pip install truststore
```

Ezután add hozzá a következőt a jegyzetfüzet vagy szkript tetejére, mielőtt bármilyen hálózati hívást indítasz:

```python
import truststore
truststore.inject_into_ssl()
```

## Elakadtál valahol?

Ha problémád van a beállítás futtatásával, csatlakozz a <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> szerverhez, vagy <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">jelents hibát</a>.

## Következő lecke

Most már készen állsz a kurzus kódjának futtatására. Jó tanulást az AI ügynökök világában! 

[Bevezetés az AI ügynökökbe és ügynök felhasználási esetek](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->