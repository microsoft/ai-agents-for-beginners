# Kurzus beállítása

## Bevezetés

Ez a lecke bemutatja, hogyan futtathatod a kurzus kódmintáit.

## Csatlakozz más tanulókhoz és kérj segítséget

Mielőtt elkezdenéd a repo klónozását, csatlakozz az [AI Agents For Beginners Discord csatornához](https://aka.ms/ai-agents/discord), hogy segítséget kapj a beállításhoz, kérdéseid legyenek a kurzusról, vagy más tanulókkal kapcsolatba léphess.

## Klónozd vagy Forkold ezt a repót

Kezdéshez kérjük, klónozd vagy forkold a GitHub repozitóriumot. Ez létrehozza a saját verziódat a kurzus anyagából, hogy futtathasd, tesztelhesd és módosíthasd a kódot!

Ezt megteheted a <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">repo fork-olása</a> linkre kattintva

Most már meg kell, hogy legyen a saját fork-olt verziód ebből a kurzusból a következő linken:

![Forked Repo](../../../translated_images/hu/forked-repo.33f27ca1901baa6a.webp)

### Shallow clone (ajánlott workshophoz / Codespaces-hez)

  >A teljes repozitórium nagy lehet (~3 GB), ha letöltöd az összes korábbi verziót és fájlt. Ha csak a workshopon veszel részt vagy csak néhány lecke mappára van szükséged, egy shallow clone (vagy sparse clone) sokkal kevesebbet tölt le.

#### Gyors shallow clone — minimális előzmények, minden fájl

Cseréld le az `<your-username>` részt az alábbi parancsokban a saját fork URL-edre (vagy az upstream URL-re, ha azt szereted).

Csak a legutóbbi commit előzményét klónozáshoz (kicsi letöltés):

```bash
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Egy adott ág klónozásához:

```bash
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Részleges (sparse) clone — minimális blobok + csak a kiválasztott mappák

Ez a partial clone-t és sparse-checkout-ot használ (Git 2.25+ szükséges és ajánlott modern Git a partial clone támogatásával):

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Lépj be a repo mappába:

```bash
cd ai-agents-for-beginners
```

Majd add meg, mely mappákat szeretnéd (a lenti példa két mappát mutat):

```bash
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

A klónozás és a fájlok ellenőrzése után, ha csak a fájlokra van szükséged és felszabadítanál helyet (git előzmények nélkül), kérjük töröld a repozitórium metaadatait (💀visszafordíthatatlan — elveszted az összes Git funkciót):

```bash
# zsh/bash
rm -rf .git
```

```powershell
# PowerShell
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces használata (ajánlott, hogy elkerüld a nagy helyi letöltéseket)

- Hozz létre egy új Codespace-t ehhez a repóhoz a [GitHub UI](https://github.com/codespaces) segítségével.  

- Az újonnan létrehozott codespace termináljában futtasd az előbbi shallow/sparse clone parancsok valamelyikét, hogy csak azokat a leckemappákat töltsd be a Codespace munkaterületére, amikre szükséged van.
- Opcionális: a klónozás után Codespaces-ben töröld a .git mappát, hogy plusz helyet nyerj (lásd fentebb a törlési parancsokat).
- Megjegyzés: Ha inkább közvetlenül nyitod meg a repót Codespaces-ben (klónozás nélkül), vedd figyelembe, hogy a Codespaces létrehozza a devcontainer környezetet, és előfordulhat, hogy több dolgot tölt be, mint amire szükséged van.

#### Tippek

- Mindig cseréld le a klónozási URL-t a saját forkodra, ha szerkeszteni/commitolni szeretnél.
- Ha később több előzményre vagy fájlra van szükséged, lekérdezheted vagy módosíthatod a sparse-checkout beállítást további mappák bevonásához.

## A kód futtatása

Ez a kurzus egy sor Jupyter jegyzetfüzetet kínál, amiket futtathatsz, hogy gyakorlati tapasztalatot szerezz az AI Ügynökök építésében.

A kódminták a **Microsoft Agent Framework (MAF)**-et használják a `FoundryChatClient`-tel, amely kapcsolódik a **Microsoft Foundry Agent Service V2**-höz (a Responses API-hoz) a **Microsoft Foundry**-n keresztül.

Minden Python jegyzetfüzet `*-python-agent-framework.ipynb` címkével van ellátva.

## Követelmények

- Python 3.12+
  - **MEGJEGYZÉS**: Ha nincs telepítve a Python3.12, győződj meg róla, hogy azt telepíted. Ezután hozd létre a venv-t python3.12-vel, hogy a requirements.txt fájlból a megfelelő verziók kerüljenek telepítésre.
  
    >Példa

    Python venv könyvtár létrehozása:

    ```bash
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

- .NET 10+: A .NET-et használó példa kódokhoz telepítsd a [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0) vagy újabb verziót. Ezután ellenőrizd a telepített .NET SDK verziót:

    ```bash
    dotnet --list-sdks
    ```

- **Azure CLI** — Szükséges az azonosításhoz. Telepítsd innen: [aka.ms/installazurecli](https://aka.ms/installazurecli).
- **Azure előfizetés** — Hozzáférés a Microsoft Foundry-hoz és a Microsoft Foundry Agent Service-hez.
- **Microsoft Foundry Projekt** — Egy projekt telepített modellel (pl. `gpt-5-mini`). Lásd [1. lépés](#1-lépés-hozz-létre-egy-microsoft-foundry-projektet) lent.

A repozitórium gyökerében található egy `requirements.txt` fájl, amely tartalmazza az összes szükséges Python csomagot a kódminták futtatásához.

Telepítheted őket, ha a következő parancsot futtatod a termináledben a repó gyökeréből:

```bash
pip install -r requirements.txt
```

Javasoljuk, hogy hozz létre egy Python virtuális környezetet a konfliktusok és problémák elkerülése érdekében.

## VSCode beállítása

Győződj meg róla, hogy a VSCode-ban a megfelelő Python verziót használod.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Microsoft Foundry és Microsoft Foundry Agent Service beállítása

### 1. lépés: Hozz létre egy Microsoft Foundry projektet

Szükséged van egy Microsoft Foundry **hubra** és **projektre** telepített modellel a jegyzetfüzetek futtatásához.

1. Lépj be a [ai.azure.com](https://ai.azure.com)-ra az Azure fiókoddal.
2. Hozz létre egy **hubot** (vagy használj meglévőt). Lásd: [Hub erőforrások áttekintése](https://learn.microsoft.com/azure/ai-foundry/concepts/ai-resources).
3. A hubon belül hozz létre egy **projektet**.
4. Telepíts egy modellt (pl. `gpt-5-mini`) a **Models + Endpoints** → **Deploy model** menüpontból.

### 2. lépés: Szerezd meg a projekt végpontját és a modell telepítésének nevét

A Microsoft Foundry portálon a projektednél:

- **Projekt végpont** — Kattints az **Áttekintés** oldalra és másold ki a végpont URL-jét.

![Project Connection String](../../../translated_images/hu/project-endpoint.8cf04c9975bbfbf1.webp)

- **Modell telepítésének neve** — Menj a **Models + Endpoints**-hez, válaszd ki a telepített modellt, és jegyezd fel a **Deployment name**-et (pl.: `gpt-5-mini`).

### 3. lépés: Jelentkezz be az Azure-ba az `az login` paranccsal

A legtöbb jegyzetfüzet az **Azure CLI bejelentkezéssel** hitelesít — `AzureCliCredential` vagy `DefaultAzureCredential` segítségével (mindkettő felhasználja az `az login` munkamenetedet) az `azure-identity` csomagból — így nincs szükség API kulcsokra. Néhány lecke és opcionális integrációk API kulcsokat használnak; ellenőrizd az adott lecke előfeltételeit a további környezeti változókért. Ehhez szükséges, hogy be legyél jelentkezve az Azure CLI segítségével.

1. **Telepítsd az Azure CLI-t**, ha még nincs: [aka.ms/installazurecli](https://aka.ms/installazurecli)

2. **Jelentkezz be** ezzel:

    ```bash
    az login
    ```

    Vagy ha távoli/Codespace környezetben vagy böngésző nélkül:

    ```bash
    az login --use-device-code
    ```

3. **Válaszd ki az előfizetésedet**, ha kéri — azt válaszd, amely a Foundry projektedet tartalmazza.

4. **Ellenőrizd**, hogy be vagy jelentkezve:

    ```bash
    az account show
    ```

> **Miért az `az login`?** A jegyzetfüzetek `AzureCliCredential` (vagy `DefaultAzureCredential`, ami szintén használja az Azure CLI belépést) az `azure-identity` csomagból hitelesítik. Ez azt jelenti, hogy az Azure CLI munkameneted adja az azonosítási adatokat — nincs szükség API kulcsokra vagy titkokra a `.env` fájlban. Ez egy [biztonsági bevált gyakorlat](https://learn.microsoft.com/azure/developer/ai/keyless-connections).

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

Nyisd meg a `.env` fájlt és töltsd ki az alábbi két értékkel:

```env
AZURE_AI_PROJECT_ENDPOINT=https://<your-project>.services.ai.azure.com/api/projects/<your-project-id>
AZURE_AI_MODEL_DEPLOYMENT_NAME=gpt-5-mini
```

| Változó | Hol található |
|----------|-----------------|
| `AZURE_AI_PROJECT_ENDPOINT` | Foundry portál → a projekted → **Áttekintés** oldal |
| `AZURE_AI_MODEL_DEPLOYMENT_NAME` | Foundry portál → **Models + Endpoints** → a telepített modell neve |

Ennyi az egész a legtöbb leckéhez! A jegyzetfüzetek automatikusan hitelesítenek az `az login` munkameneteden keresztül.

### 5. lépés: Telepítsd a Python függőségeket

```bash
pip install -r requirements.txt
```

Ajánljuk, hogy ezt a korábban létrehozott virtuális környezetben futtasd.

## Opcionális beállítás: Azure AI Search (5. és 16. lecke)

Az 5. lecke (Agentic RAG) és a 16. lecke jegyzetfüzetei azonnal futnak az **memóriában tárolt tudásbázissal** — nincs szükség további Azure erőforrásokra. Ha valódi **Azure AI Search** indexet szeretnél használni, vedd figyelembe, hogy a **16. lecke jegyzetfüzete jelenleg kulcs-alapú hitelesítést használ**: csak akkor vált az in-memory keresésről Azure AI Search-re, ha **mindkettő** `AZURE_SEARCH_SERVICE_ENDPOINT` **és** `AZURE_SEARCH_API_KEY` be van állítva, különben az in-memory keresés marad — tehát a valódi index használatához az admin kulcsot is meg kell adnod. A Microsoft Entra ID-s (RBAC) kulcs nélküli hitelesítés a javasolt megoldás a saját éles kódodhoz, összhangban az `az login` folyamattal, amit a kurzusban mindenhol alkalmazunk.

Az alábbi RBAC lépések a beállítási útmutató mintákra és a saját kódodra is vonatkoznak. Ezek nem teszik lehetővé a kulcs nélküli hitelesítést a 16. lecke jegyzetfüzetében; a 16. lecke továbbra is megköveteli a végpontot és az admin kulcsot az Azure AI Search használatához.

1. **Engedélyezd a szerepalapú hozzáférés-vezérlést** a keresési szolgáltatásodon:

    ```bash
    az search service update --name <service-name> --resource-group <resource-group> --auth-options aadOrApiKey
    ```

2. **Add magadnak a szükséges szerepköröket** (indexek létrehozása/betöltése és lekérdezése):

    ```bash
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Service Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    az role assignment create --assignee <your-user-or-principal-id> --role "Search Index Data Contributor" --scope $(az search service show -g <resource-group> -n <service-name> --query id -o tsv)
    ```

3. **Add hozzá a végpontot** a `.env` fájlodhoz:

| Változó | Hol található |
|----------|-----------------|
| `AZURE_SEARCH_SERVICE_ENDPOINT` | Azure portál → a **Azure AI Search** erőforrásod → **Áttekintés** → URL |
| `AZURE_SEARCH_API_KEY` | Kötelező (a végponttal együtt) az Azure AI Search engedélyezéséhez a 16. lecke jegyzetfüzetében, ami kulcs-alapú hitelesítést használ. Azure portál → **Beállítások** → **Kulcsok** → elsődleges admin kulcs |

> **Miért kulcs nélküli?** Az admin kulcs teljes írási jogosultságot ad a keresési szolgáltatáshoz, és kiszivároghat `.env` fájlokból. RBAC esetén az `az login` identitásodat használod — ugyanaz a kulcs nélküli Entra ID mintaminta, amit a kurzus jegyzetfüzetei is használnak (`AzureCliCredential` / `DefaultAzureCredential`). Lásd [Azure AI Search szerepkörök segítségével](https://learn.microsoft.com/azure/search/search-security-rbac).

Lásd a [Azure AI Search beállítási útmutatót](./AzureSearch.md) a teljes index létrehozási példákért Pythonban és .NET-ben.

## További beállítások azokhoz a leckékhez, amik közvetlenül az Azure OpenAI-t hívják meg (6. és 8. lecke)

Néhány jegyzetfüzet a 6. és 8. leckében közvetlenül az **Azure OpenAI**-t használja (**Responses API**-n keresztül) a Microsoft Foundry projektek helyett. Ezek a minták korábban GitHub Modelleket használtak, amelyek elavultak és nem támogatják a Responses API-t. Add hozzá ezeket a változókat a `.env` fájlodhoz:

| Változó | Hol található |
|----------|-----------------|
| `AZURE_OPENAI_ENDPOINT` | Azure portál → a **Azure OpenAI** erőforrásod → **Kulcsok és végpont** → Végpont (pl. `https://<your-resource>.openai.azure.com`) |
| `AZURE_OPENAI_DEPLOYMENT` | A telepített modell neve (pl. `gpt-5-mini`), amely támogatja a Responses API-t |
| `AZURE_OPENAI_API_KEY` | Opcionális — csak akkor, ha kulcs-alapú hitelesítést használsz az `az login` / Entra ID helyett |

> A Responses API a stabil `/openai/v1/` végpontot használja, ezért nincs szükség `api-version` megadására. Jelentkezz be `az login`-nal a kulcs nélküli Entra ID hitelesítéshez.

## Alternatív szolgáltató: MiniMax (OpenAI-kompatibilis)

A [MiniMax](https://platform.minimaxi.com/) nagy kontextusú modelleket (akár 204K token) biztosít OpenAI-kompatibilis API-n keresztül. Mivel a Microsoft Agent Framework `OpenAIChatClient`-je bármilyen OpenAI-kompatibilis végponttal működik, használhatod a MiniMax-ot is alternatív megoldásként azokban a leckékben, amelyek `OpenAIChatClient`-et használnak.

Add hozzá ezeket a változókat a `.env` fájlodhoz:

| Változó | Hol található |
|----------|-----------------|
| `MINIMAX_API_KEY` | [MiniMax Platform](https://platform.minimaxi.com/) → API kulcsok |
| `MINIMAX_BASE_URL` | Használd a `https://api.minimax.io/v1` (alapértelmezett érték) |
| `MINIMAX_MODEL_ID` | Használandó modell neve (pl. `MiniMax-M3`) |

**Példa modellek**: `MiniMax-M3` (ajánlott), `MiniMax-M2.7`, `MiniMax-M2.7-highspeed` (gyorsabb válaszok). A modell nevek és elérhetőség változhat idővel, és a hozzáférés függ a fiókodatól.

Az `OpenAIChatClient`-et használó kódminták (pl. a 14. lecke szállodafoglalási folyamat) automatikusan felismerik és használják a MiniMax konfigurációdat, ha be van állítva a `MINIMAX_API_KEY`.


## Alternatív Szolgáltató: Novita AI (OpenAI-kompatibilis)

[Novita AI](https://novita.ai/llm-api) OpenAI-kompatibilis API-t biztosít nyílt forráskódú és élvonalbeli LLM-ekhez (DeepSeek, Llama, Qwen és még sok más). Mivel a Microsoft Agent Framework `OpenAIChatClient`-je bármely OpenAI-kompatibilis végponttal működik, a Novita AI-t az Azure OpenAI vagy OpenAI helyettesítőjeként használhatod.

Add hozzá ezeket a változókat a `.env` fájlodhoz:

| Változó | Hol található |
|----------|-----------------|
| `NOVITA_API_KEY` | [Novita AI Vezérlőpult](https://novita.ai/settings/key-management) → API Kulcsok |
| `NOVITA_BASE_URL` | Használd a `https://api.novita.ai/openai/v1` (alapértelmezett érték) |
| `NOVITA_MODEL_ID` | Használandó modell neve (pl. `moonshotai/kimi-k3`) |

**Példa modellek**: `moonshotai/kimi-k3`, `zai-org/glm-5.2`, `deepseek/deepseek-v4-flash-0731`. A Novita AI számos más nyílt forráskódú modellcsaládot is kínál (Llama, Qwen, GLM és még sok más) — ellenőrizd a [Novita AI modellkönyvtárat](https://novita.ai/llm-api) a jelenleg elérhető modellek és modellazonosítók listájáért.

A jelenlegi minták nem használják automatikusan a `NOVITA_*` változókat. A Novita AI használatához add meg ezeket az értékeket kifejezetten, amikor az `OpenAIChatClient`-et létrehozod a futtatandó mintában.

## Alternatív Szolgáltató: Foundry Local (Modellek futtatása eszközön)

A [Foundry Local](https://foundrylocal.ai) egy könnyű futtatókörnyezet, amely teljes egészében a saját gépeden tölti le, kezeli és szolgálja ki a nyelvi modelleket OpenAI-kompatibilis API-n keresztül — felhő nélkül.

Mivel a Microsoft Agent Framework `OpenAIChatClient`-je bármely OpenAI-kompatibilis végponttal működik, a Foundry Local egy helyi, azonnal használható alternatíva az Azure OpenAI-hoz.

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

**3. Telepítsd a Python SDK-t** a helyi végpont felfedezéséhez:

```bash
pip install foundry-local-sdk
```

**4. Állítsd be a Microsoft Agent Framework-öt a helyi modelledhez:**

```python
from foundry_local import FoundryLocalManager
from agent_framework.openai import OpenAIChatClient

# Letölti (ha szükséges) és helyben kiszolgálja a modellt, majd felfedezi a végpontot/portot.
manager = FoundryLocalManager("phi-4-mini")

chat_client = OpenAIChatClient(
    base_url=manager.endpoint,      # pl. http://localhost:<port>/v1
    api_key=manager.api_key,        # mindig "not-required" a Foundry Local esetében
    model_id=manager.get_model_info("phi-4-mini").id,
)

agent = chat_client.as_agent(
    name="LocalAgent",
    instructions="You are a helpful assistant running fully on-device.",
)
```

> **Megjegyzés:** A Foundry Local egy OpenAI-kompatibilis **Chat Completions** végpontot tesz elérhetővé. Használd helyi fejlesztéshez és offline helyzetekben. A teljes **Responses API** funkciókészlethez (állapotmegőrző beszélgetések, stb.) használd az Azure OpenAI-t vagy a Microsoft Foundry projektet.

## További Beállítás a 8. Lecke (Bing Grounding Munkafolyamat)

A 8. leckében a feltételes munkafolyamat a Microsoft Foundry-n keresztüli **Bing grounding**-et használ. Ha ezt a mintát futtatni szeretnéd, add hozzá ezt a változót a `.env` fájlodhoz:

| Változó | Hol található |
|----------|-----------------|
| `BING_CONNECTION_ID` | Microsoft Foundry portál → a projekted → **Management** → **Connected resources** → a Bing kapcsolat → másold ki a kapcsolat azonosítóját |

## Hibakeresés

### SSL Tanúsítvány Ellenőrzési Hibák macOS-en

Ha macOS-en ezt az hibát tapasztalod:

```plaintext
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain
```

Ez egy ismert probléma Python esetén macOS-en, ahol a rendszer SSL tanúsítványokat nem bízzák automatikusan meg. Próbáld ki a következő megoldásokat ebben a sorrendben:

**1. Opció: Futtasd a Python Telepítő Tanúsítvány szkriptjét (ajánlott)**

```bash
# Cseréld ki a 3.XX-et a telepített Python verzióddal (pl. 3.12 vagy 3.13):
/Applications/Python\ 3.XX/Install\ Certificates.command
```

**2. Opció: Használd a `connection_verify=False` opciót a jegyzetfüzetedben (csak GitHub Models jegyzetfüzetekhez)**

A 6. leckében (`06-building-trustworthy-agents/code_samples/06-system-message-framework.ipynb`) egy kikommentezett megoldás már benne van. Kapcsold be a `connection_verify=False`-t, ha tanúsítványhibába ütközöl:

```python
client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
    connection_verify=False,  # SSL ellenőrzés letiltása, ha tanúsítványhibákkal találkozol
)
```

> **⚠️ Figyelmeztetés:** Az SSL ellenőrzés kikapcsolása (`connection_verify=False`) csökkenti a biztonságot, mert kihagyja a tanúsítvány ellenőrzést. Csak fejlesztési környezetben, ideiglenes megoldásként használd. Éles környezetben soha ne alkalmazd.

**3. Opció: Telepítsd és használd a `truststore`-t**

```bash
pip install truststore
```

Ezután add hozzá a következőt a jegyzetfüzeted vagy scripted tetejére a hálózati hívások előtt:

```python
import truststore
truststore.inject_into_ssl()
```

## Elakadtál Valahol?

Ha bármilyen problémád van a beállítás futtatásával, csatlakozz a <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discordhoz</a> vagy <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">jelents hibát</a>.

## Következő Lecke

Most már készen állsz a kurzus kódjának futtatására. Jó tanulást az AI Ügynökök világában! 

[Bevezetés az AI Ügynökökbe és Ügynök Használati Esetek](../01-intro-to-ai-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->