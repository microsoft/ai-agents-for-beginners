<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "96eb7f95375daa3e91778ca0295a55d9",
  "translation_date": "2025-10-15T08:45:56+00:00",
  "source_file": "00-course-setup/README.md",
  "language_code": "hu"
}
-->
# A kurzus beállítása

## Bevezetés

Ebben a leckében megtanulhatod, hogyan futtasd a kurzus kódmintáit.

## Csatlakozz más tanulókhoz és kérj segítséget

Mielőtt elkezdenéd klónozni a repót, csatlakozz az [AI Agents For Beginners Discord csatornához](https://aka.ms/ai-agents/discord), hogy segítséget kapj a beállításhoz, választ kapj a kurzussal kapcsolatos kérdéseidre, vagy kapcsolatba lépj más tanulókkal.

## Klónozd vagy forkold a repót

Először klónozd vagy forkold a GitHub repót. Ezáltal létrehozod a kurzus anyagának saját verzióját, amelyet futtathatsz, tesztelhetsz és módosíthatsz!

Ezt úgy teheted meg, hogy rákattintasz a <a href="https://github.com/microsoft/ai-agents-for-beginners/fork" target="_blank">repo forkolása</a> linkre.

Most már rendelkezel a kurzus saját forkolt verziójával az alábbi linken:

![Forkolt Repo](../../../translated_images/forked-repo.33f27ca1901baa6a5e13ec3eb1f0ddd3a44d936d91cc8cfb19bfdb9688bd2c3d.hu.png)

### Sekély klónozás (ajánlott workshophoz / Codespaces-hez)

  >A teljes repó mérete nagy lehet (~3 GB), ha letöltöd az összes előzményt és fájlt. Ha csak a workshopon veszel részt, vagy csak néhány lecke mappára van szükséged, a sekély klónozás (vagy ritka klónozás) elkerüli a legtöbb letöltést az előzmények rövidítésével és/vagy a blobok kihagyásával.

#### Gyors sekély klónozás — minimális előzmény, minden fájl

Cseréld ki `<your-username>`-t az alábbi parancsokban a fork URL-re (vagy az upstream URL-re, ha azt preferálod).

Csak a legutóbbi commit előzmény klónozása (kis letöltés):

```bash|powershell
git clone --depth 1 https://github.com/<your-username>/ai-agents-for-beginners.git
```

Egy adott branch klónozása:

```bash|powershell
git clone --depth 1 --branch <branch-name> https://github.com/<your-username>/ai-agents-for-beginners.git
```

#### Részleges (ritka) klónozás — minimális blobok + csak kiválasztott mappák

Ez részleges klónozást és ritka-checkoutot használ (Git 2.25+ szükséges, modern Git ajánlott részleges klónozás támogatásával):

```bash|powershell
git clone --depth 1 --filter=blob:none --sparse https://github.com/<your-username>/ai-agents-for-beginners.git
```

Lépj be a repo mappájába:

Bash esetén:

```bash
cd ai-agents-for-beginners
```

Powershell esetén:

```powershell
Set-Location ai-agents-for-beginners
```

Ezután add meg, mely mappákra van szükséged (az alábbi példa két mappát mutat):

```bash|powershell
git sparse-checkout set 00-course-setup 01-intro-to-ai-agents
```

Miután klónoztad és ellenőrizted a fájlokat, ha csak fájlokra van szükséged és helyet szeretnél felszabadítani (nincs git előzmény), töröld a repó metaadatokat (💀visszafordíthatatlan — elveszíted az összes Git funkciót: nincs commit, pull, push vagy előzmény hozzáférés).

Linux/macOS esetén:

```bash
rm -rf .git
```

Windows esetén:

```powershell
Remove-Item -Recurse -Force .git
```

#### GitHub Codespaces használata (ajánlott a helyi nagy letöltések elkerülésére)

- Hozz létre egy új Codespace-t ehhez a repohoz a [GitHub UI](https://github.com/codespaces) segítségével.  

- Az újonnan létrehozott Codespace termináljában futtasd az egyik sekély/ritka klónozási parancsot, hogy csak a szükséges lecke mappákat hozd be a Codespace munkaterületére.
- Opcionális: a klónozás után a Codespaces-ben távolítsd el a .git-et, hogy extra helyet szabadíts fel (lásd a törlési parancsokat fent).
- Megjegyzés: Ha inkább közvetlenül a repo-t nyitnád meg Codespaces-ben (extra klónozás nélkül), vedd figyelembe, hogy a Codespaces létrehozza a devcontainer környezetet, és lehet, hogy többet biztosít, mint amire szükséged van. Egy sekély másolat klónozása egy friss Codespace-ben nagyobb kontrollt ad a lemezhasználat felett.

#### Tippek

- Mindig cseréld ki a klónozási URL-t a forkodra, ha szerkeszteni/commitálni szeretnél.
- Ha később több előzményre vagy fájlra van szükséged, letöltheted őket, vagy módosíthatod a ritka-checkoutot további mappák hozzáadásához.

## A kód futtatása

Ez a kurzus Jupyter Notebook-ok sorozatát kínálja, amelyeket futtathatsz, hogy gyakorlati tapasztalatot szerezz az AI Agentek építésében.

A kódminták az alábbiakat használják:

**GitHub fiók szükséges - Ingyenes**:

1) Semantic Kernel Agent Framework + GitHub Models Marketplace. Jelölve mint (semantic-kernel.ipynb)
2) AutoGen Framework + GitHub Models Marketplace. Jelölve mint (autogen.ipynb)

**Azure előfizetés szükséges**:
3) Azure AI Foundry + Azure AI Agent Service. Jelölve mint (azureaiagent.ipynb)

Javasoljuk, hogy próbáld ki mindhárom példát, hogy megtudd, melyik működik a legjobban számodra.

Az általad választott opció határozza meg, hogy melyik beállítási lépéseket kell követned az alábbiakban:

## Követelmények

- Python 3.12+
  - **MEGJEGYZÉS**: Ha nincs telepítve a Python 3.12, győződj meg róla, hogy telepíted. Ezután hozz létre egy venv-t python3.12 használatával, hogy biztosítsd a megfelelő verziók telepítését a requirements.txt fájlból.
  
    >Példa

    Python venv könyvtár létrehozása:

    ``` bash
    python3 -m venv venv
    ```

    Ezután aktiváld a venv környezetet:

    macOS és Linux esetén

    ```bash
    source venv/bin/activate
    ```
  
    Windows esetén

    ```bash
    venv\Scripts\activate
    ```

- GitHub fiók - A GitHub Models Marketplace eléréséhez
- Azure előfizetés - Az Azure AI Foundry eléréséhez
- Azure AI Foundry fiók - Az Azure AI Agent Service eléréséhez

A repó gyökérkönyvtárában található egy `requirements.txt` fájl, amely tartalmazza az összes szükséges Python csomagot a kódminták futtatásához.

Telepítheted őket az alábbi parancs futtatásával a terminálban, a repó gyökérkönyvtárában:

```bash
pip install -r requirements.txt
```
Javasoljuk, hogy hozz létre egy Python virtuális környezetet, hogy elkerüld az esetleges konfliktusokat és problémákat.

## VSCode beállítása
Győződj meg róla, hogy a megfelelő Python verziót használod a VSCode-ban.

![image](https://github.com/user-attachments/assets/a85e776c-2edb-4331-ae5b-6bfdfb98ee0e)

## Beállítás GitHub Modellek használatához 

### 1. lépés: GitHub személyes hozzáférési token (PAT) lekérése

Ez a kurzus a GitHub Models Marketplace-t használja, amely ingyenes hozzáférést biztosít Nagy Nyelvi Modellekhez (LLM-ekhez), amelyeket az AI Agentek építéséhez fogsz használni.

A GitHub Modellek használatához létre kell hoznod egy [GitHub személyes hozzáférési tokent](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

Ezt úgy teheted meg, hogy a GitHub fiókod <a href="https://github.com/settings/personal-access-tokens" target="_blank">Személyes hozzáférési tokenek beállításai</a> oldalára mész.

Kérjük, kövesd a [Legkisebb jogosultság elvét](https://docs.github.com/en/get-started/learning-to-code/storing-your-secrets-safely) a token létrehozásakor. Ez azt jelenti, hogy csak azokat a jogosultságokat add meg a tokennek, amelyek szükségesek a kurzus kódmintáinak futtatásához.

1. Válaszd ki a `Fine-grained tokens` opciót a képernyő bal oldalán, a **Fejlesztői beállítások** menüpontban.
   ![](../../../translated_images/profile_developer_settings.410a859fe749c755c859d414294c5908e307222b2c61819c3203bbeed4470e25.hu.png)

    Ezután válaszd a `Generate new token` opciót.

    ![Token létrehozása](../../../translated_images/fga_new_token.1c1a234afe202ab37483944a291ee80c1868e1e78082fd6bd4180fea5d5a15b4.hu.png)

2. Adj meg egy leíró nevet a tokennek, amely tükrözi annak célját, így később könnyen azonosítható.

    🔐 Token időtartam ajánlás

    Ajánlott időtartam: 30 nap
    A biztonságosabb megközelítés érdekében választhatsz rövidebb időszakot is, például 7 napot 🛡️
    Ez egy remek módja annak, hogy személyes célt állíts be, és befejezd a kurzust, miközben a tanulási lendületed magas 🚀.

    ![Token név és lejárati dátum](../../../translated_images/token-name-expiry-date.a095fb0de63868640a4c82d6b1bbc92b482930a663917a5983a3c7cd1ef86b77.hu.png)

3. Korlátozd a token hatókörét a repód forkjára.

    ![Hatókör korlátozása fork repóra](../../../translated_images/token_repository_limit.924ade5e11d9d8bb6cd21293987e4579dea860e2ba66d607fb46e49524d53644.hu.png)

4. Korlátozd a token jogosultságait: A **Jogosultságok** alatt kattints az **Account** fülre, majd az "+ Add permissions" gombra. Egy legördülő menü jelenik meg. Keresd meg a **Models** opciót, és jelöld be a négyzetet.
    ![Modellek jogosultság hozzáadása](../../../translated_images/add_models_permissions.c0c44ed8b40fc143dc87792da9097d715b7de938354e8f771d65416ecc7816b8.hu.png)

5. Ellenőrizd a szükséges jogosultságokat a token létrehozása előtt. ![Jogosultságok ellenőrzése](../../../translated_images/verify_permissions.06bd9e43987a8b219f171bbcf519e45ababae35b844f5e9757e10afcb619b936.hu.png)

6. A token létrehozása előtt győződj meg róla, hogy készen állsz a token biztonságos helyen történő tárolására, például egy jelszókezelőben, mivel a token nem lesz újra látható a létrehozás után. ![Token biztonságos tárolása](../../../translated_images/store_token_securely.08ee2274c6ad6caf3482f1cd1bad7ca3fdca1ce737bc485bfa6499c84297c789.hu.png)

Másold ki az újonnan létrehozott tokent. Most hozzáadod ezt a `.env` fájlhoz, amelyet a kurzus tartalmaz.


### 2. lépés: `.env` fájl létrehozása

A `.env` fájl létrehozásához futtasd az alábbi parancsot a terminálban.

```bash
cp .env.example .env
```

Ez lemásolja a példafájlt, és létrehoz egy `.env` fájlt a könyvtáradban, ahol kitöltheted a környezeti változók értékeit.

A token másolása után nyisd meg a `.env` fájlt a kedvenc szövegszerkesztődben, és illeszd be a tokent a `GITHUB_TOKEN` mezőbe.
![GitHub Token mező](../../../translated_images/github_token_field.20491ed3224b5f4ab24d10ced7a68c4aba2948fe8999cfc8675edaa16f5e5681.hu.png)


Most már képesnek kell lenned futtatni a kurzus kódmintáit.

## Beállítás Azure AI Foundry és Azure AI Agent Service mintákhoz

### 1. lépés: Azure projekt végpontjának lekérése

Kövesd az Azure AI Foundry hub és projekt létrehozásának lépéseit itt: [Hub erőforrások áttekintése](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/ai-resources)

Miután létrehoztad a projektedet, le kell kérned a projekt kapcsolatának karakterláncát.

Ezt a projekt **Áttekintés** oldalán találod az Azure AI Foundry portálon.

![Projekt kapcsolat karakterlánc](../../../translated_images/project-endpoint.8cf04c9975bbfbf18f6447a599550edb052e52264fb7124d04a12e6175e330a5.hu.png)

### 2. lépés: `.env` fájl létrehozása

A `.env` fájl létrehozásához futtasd az alábbi parancsot a terminálban.

```bash
cp .env.example .env
```

Ez lemásolja a példafájlt, és létrehoz egy `.env` fájlt a könyvtáradban, ahol kitöltheted a környezeti változók értékeit.

A token másolása után nyisd meg a `.env` fájlt a kedvenc szövegszerkesztődben, és illeszd be a tokent a `PROJECT_ENDPOINT` mezőbe.

### 3. lépés: Bejelentkezés az Azure-ba

Biztonsági legjobb gyakorlatként [kulcs nélküli hitelesítést](https://learn.microsoft.com/azure/developer/ai/keyless-connections?tabs=csharp%2Cazure-cli?WT.mc_id=academic-105485-koreyst) fogunk használni az Azure OpenAI hitelesítéséhez Microsoft Entra ID-val. 

Ezután nyiss meg egy terminált, és futtasd az `az login --use-device-code` parancsot, hogy bejelentkezz az Azure fiókodba.

Miután bejelentkeztél, válaszd ki az előfizetésedet a terminálban.


## További környezeti változók - Azure Search és Azure OpenAI 

Az Agentic RAG lecke - 5. lecke - mintái az Azure Search és Azure OpenAI használatát igénylik.

Ha futtatni szeretnéd ezeket a mintákat, hozzá kell adnod az alábbi környezeti változókat a `.env` fájlodhoz:

### Áttekintés oldal (Projekt)

- `AZURE_SUBSCRIPTION_ID` - Ellenőrizd a **Projekt részletek**-et a projekt **Áttekintés** oldalán.

- `AZURE_AI_PROJECT_NAME` - Nézd meg a projekt **Áttekintés** oldalának tetejét.

- `AZURE_OPENAI_SERVICE` - Keresd meg az **Azure OpenAI Service**-t az **Included capabilities** fülön az **Áttekintés** oldalon.

### Menedzsment központ

- `AZURE_OPENAI_RESOURCE_GROUP` - Menj a **Projekt tulajdonságok**-hoz az **Áttekintés** oldalon a **Menedzsment központban**.

- `GLOBAL_LLM_SERVICE` - Az **Kapcsolt erőforrások** alatt keresd meg az **Azure AI Services** kapcsolat nevét. Ha nem szerepel, ellenőrizd az **Azure portálon** az erőforráscsoportodban az AI Services erőforrás nevét.

### Modellek + Végpontok oldal

- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME` - Válaszd ki az embedding modelledet (pl. `text-embedding-ada-002`), és jegyezd fel a **Deployment name**-et a modell részleteiből.

- `AZURE_OPENAI_CHAT_DEPLOYMENT_NAME` - Válaszd ki a chat modelledet (pl. `gpt-4o-mini`), és jegyezd fel a **Deployment name**-et a modell részleteiből.

### Azure portál

- `AZURE_OPENAI_ENDPOINT` - Keresd meg az **Azure AI services**-t, kattints rá, majd menj a **Resource Management**, **Keys and Endpoint**-hez, görgess le az "Azure OpenAI endpoints"-hoz, és másold ki azt, amelyik "Language APIs"-t mond.

- `AZURE_OPENAI_API_KEY` - Ugyanazon az oldalon másold ki az 1. vagy 2. kulcsot.

- `AZURE_SEARCH_SERVICE_ENDPOINT` - Keresd meg az **Azure AI Search** erőforrásodat, kattints rá, és nézd meg az **Áttekintés**-t.

- `AZURE_SEARCH_API_KEY` - Ezután menj a **Beállítások**-hoz, majd **Kulcsok**-hoz, hogy lemásold az elsődleges vagy másodlagos admin kulcsot.

### Külső weboldal

- `AZURE_OPENAI_API_VERSION` - Látogasd meg az [API verzió életciklus](https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation#latest-ga-api-release) oldalt a **Latest GA API release** alatt.

### Kulcs nélküli hitelesítés beállítása

A hitelesítő adatok kódolása helyett kulcs nélküli kapcsolatot fogunk használni az Azure OpenAI-val. Ehhez importáljuk a `DefaultAzureCredential`-t, majd később meghívjuk a `DefaultAzureCredential` függvényt a hitelesítő adat megszerzéséhez.

```python
from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
```

## Elakadtál valahol?
Ha bármilyen problémád adódik a beállítás futtatása során, csatlakozz az <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Community Discord</a> közösséghez, vagy <a href="https://github.com/microsoft/ai-agents-for-beginners/issues?WT.mc_id=academic-105485-koreyst" target="_blank">hozz létre egy hibajelentést</a>.

## Következő lecke

Most már készen állsz arra, hogy futtasd a kurzushoz tartozó kódot. Jó tanulást az AI ügynökök világáról! 

[Bevezetés az AI ügynökökbe és azok felhasználási eseteibe](../01-intro-to-ai-agents/README.md)

---

**Felelősség kizárása**:  
Ez a dokumentum az [Co-op Translator](https://github.com/Azure/co-op-translator) AI fordítási szolgáltatás segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.