---
name: azure-openai-to-responses
license: MIT
---
# Python alkalmazások migrálása az Azure OpenAI Chat Completions-ről a Responses API-re

> **HITELÉRHETŐ ÚTMUTATÁS — KÖVESD PONTOSAN**
>
> Ez a készség Python kódalapokat migrál az Azure OpenAI Chat Completions használatáról
> az egységes Responses API-re. Pontosan kövesd ezeket az utasításokat.
> Ne találj ki paraméter leképezéseket vagy API alakokat.

---

## Indítók

Aktiváld ezt a készséget, amikor a felhasználó azt szeretné, hogy:
- Python alkalmazást migráljon az Azure OpenAI Chat Completions-ről a Responses API-re
- Frissítse a Python OpenAI SDK használatát a legújabb API alakra Azure OpenAI ellen
- Felkészítse a Python kódot GPT-5 vagy újabb modellekhez, amelyek Responses API-t igényelnek az Azure-on
- Váltson az `AzureOpenAI`/`AsyncAzureOpenAI`-ról a szabványos `OpenAI`/`AsyncOpenAI` kliensre az v1 végponton
- Javítsa a `AzureOpenAI` konstruktorokhoz vagy `api_version`-hoz kapcsolódó elavulási figyelmeztetéseket

---

## ⚠️ Modell kompatibilitás — ELSŐLÉPÉS

> **Migrálás előtt ellenőrizd, hogy az Azure OpenAI telepítésed támogatja-e a Responses API-t.**

### 1. Gyors teszt a telepítéshez (leggyorsabb)

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
)

try:
    resp = client.responses.create(
        model=os.environ["AZURE_OPENAI_DEPLOYMENT"],
        input="ping",
        max_output_tokens=50,
        store=False,
    )
    print(f"✅ Deployment supports Responses API: {resp.output_text}")
except Exception as e:
    print(f"❌ Deployment does NOT support Responses API: {e}")
```

> **Megjegyzés**: Az `max_output_tokens` minimuma **16** az Azure OpenAI-n. A 16 alatti érték 400 hibát ad vissza. Smoke tesztekhez használj 50+ értéket.

Ha ez 404-et ad vissza, a telepítés modellje még nem támogatja a Responses API-t — nézd meg az alábbi hivatkozást vagy telepítsd újra támogatott modellel.

### 2. Ellenőrizd a régiódban elérhető modelleket (ajánlott)

Futtasd a beépített modell kompatibilitási eszközt, hogy lásd, milyen Responses API támogatással rendelkező modellek érhetők el az adott régióban:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Ez élő Azure ARM lekérdezést futtat, és megmutatja a kompatibilitási mátrixot — mely modellek támogatják a Response-t, strukturált kimenetet, eszközöket stb. Használd a `--filter gpt-5.1,gpt-5.2` a szűkítéshez vagy a `--json`-t szkriptekhez.

### 3. Teljes modell támogatási referencia

- **Élő lekérdezés**: `python migrate.py models` (lásd fent — régióspecifikus, mindig naprakész)
- **Böngéssz elérhetőséget**: [Modell összefoglaló táblázat és régió elérhetőség](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Gyors indítás & útmutató**: **https://aka.ms/openai/start**

### ⚠️ Régebbi modellek korlátozásai

> **FIGYELMEZTETÉS**: A régebbi modellek (`gpt-4.1` előtti) nem biztos, hogy teljes mértékben támogatják a Responses API összes funkcióját.
>
> Ismert korlátozások régebbi modelleknél:
> - **`reasoning` paraméter**: Sok nem-érvelő modell nem támogatja. Csak akkor migráld `reasoning`-gel, ha az eredeti kódban már jelen volt.
> - **`seed` paraméter**: A Responses API-ban egyáltalán nem támogatott — távolítsd el minden kérésből.
> - **Strukturált kimenet `text.format` révén**: Régebbi modellek nem biztos, hogy megbízhatóan érvényesítik a `strict: true` JSON sémákat.
> - **Eszköz koordináció**: A GPT-5+ modellek az eszköz meghívásokat belső érvelés részeként kezelik. Régebbi modellek Responses API-val működnek, de nem rendelkeznek ezzel a mély integrációval.
> - **Hőmérséklet korlátozások**: Amikor `gpt-5`-re migrálsz, a hőmérsékletet el kell hagyni vagy `1`-re állítani. Régebbi modelleknél ilyen korlátozás nincs.

### O-sorozatú érvelő modellek (o1, o3-mini, o3, o4-mini)

Az O-sorozat modelleknek egyedi paraméter korlátai vannak. O-sorozat modelleket célzó alkalmazások migrálásakor:

- **`temperature`**: Csak `1` lehet (vagy elhagyható). Az O-sorozat nem fogad el más értékeket.
- **`max_completion_tokens` → `max_output_tokens`**: Az Azure-specifikus `max_completion_tokens` használatát cseréld `max_output_tokens`-re. Magas értékre állítsd (4096+), mert az érvelési tokenek beleszámítanak a limitbe.
- **`reasoning_effort`**: Ha az alkalmazás használja a `reasoning_effort`-ot (alacsony/közepes/magas), tartsd meg — ezt a Responses API támogatja az O-sorozat modelleknél.
- **Streaming viselkedés**: Az O-sorozat modellek az érvelés befejezéséig pufferelik a kimenetet az események kibocsátása előtt. A streaming működik, de az első `response.output_text.delta` később érkezhet a GPT modellekhez képest.
- **`top_p`**: Nem támogatott az O-sorozatnál — távolítsd el, ha jelen van.
- **Eszközhasználat**: Az O-sorozat modellek támogatják az eszközöket a Responses API-n keresztül ugyanúgy, mint a GPT modellek, de az eszköhívás koordináció minősége modellfüggő.

**Intézkedés — előzetes modell tanácsadás**: A vizsgálati fázis alatt ellenőrizd, mely modellt célozza az alkalmazás (telepítés neve, környezeti változók, konfiguráció). Ha a modell a `gpt-4.1` előtti (nem gpt-4.1+), proaktívan tájékoztasd a felhasználót:
- Az alap szöveg, chat, streaming és eszközök támogatása működik az adott modellen.
- Az újabb modellek (`gpt-5.1`, `gpt-5.2`) jobb eszköz koordinációt, strukturált kimenet érvényesítést, érvelést és régiók közötti elérhetőséget kínálnak.
- Érdemes frissíteni a telepítést, ha készülnek rá — a migrálást nem blokkolja.

Ne blokkolj vagy utasíts el migrálást a modell verziója alapján. Ez csak információs tájékoztatás.

### A GitHub Models nem támogatja a Responses API-t

> **A GitHub Models (`models.github.ai`, `models.inference.ai.azure.com`) nem támogatja a Responses API-t.**

Ha a kódalap tartalmaz GitHub Models kódutat (keresd az `base_url`-t, ami `models.github.ai` vagy `models.inference.ai.azure.com`-ra mutat), **teljesen távolítsd el** a migrálás során. A Responses API Azure OpenAI, OpenAI vagy kompatibilis helyi végpontot (pl. Ollama Responses támogatással) igényel.

Intézkedés a vizsgálat során:
- Jelöld meg eltávolításra a GitHub Models kódutakat.

---

## Keretrendszer migráció

Sok alkalmazás magasabb szintű keretrendszereket használ az OpenAI felett. Ezek migrálásakor a keretrendszer saját API-ja változik — nem csak az alap OpenAI hívások.

### Microsoft Agent Framework (MAF)

**Először ellenőrizd a MAF verziódat** — a migráció attól függ, hogy MAF 1.0.0+ vagy egy pre-1.0.0 béta/rc verziót használsz-e.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

Az `OpenAIChatClient` **már a Responses API-t használja** — nincs szükség migrációra. Ha a kódarhívásban a régi `OpenAIChatCompletionClient` szerepel (ami a `chat.completions.create`-t használja), cseréld `OpenAIChatClient`-re.

| Előtte | Utána |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Verzió ellenőrzése: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pre-1.0.0 (béta/rc kiadások)

A pre-1.0.0 MAF-ban az `OpenAIChatClient` Chat Completions-t használt. Frissíts `agent-framework-openai>=1.0.0`-re, ahol alapból Responses API-t használ az `OpenAIChatClient`.

Nincs más szükséges változtatás — az `Agent` és eszköz API-k változatlanok maradnak.

### LangChain (`langchain-openai`)

Adj hozzá `use_responses_api=True`-t a `ChatOpenAI()` konstruktorhoz. Frissítsd a válasz elérését `.content` helyett `.text`-re.

| Előtte | Utána |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Teljes előtte/utána kódpéldákért lásd [cheat-sheet.md](./references/cheat-sheet.md).

---

## Frontend migrációs útmutató

> **A Responses API szerveroldali kérdés.** Migráld a Python backendet; a frontend HTTP szerződése változatlan marad, kivéve, ha a backend egy vékony pass-through — ebben az esetben fontold meg a Responses kérés alakját, hogy eltávolíts egy fordító réteget. Ha a frontend közvetlenül OpenAI-t hív kliensoldali kulccsal, ezeket a hívásokat először a backendre kell átvinni.

### `@microsoft/ai-chat-protocol` elavulás

A `@microsoft/ai-chat-protocol` npm csomag elavult, és ki kell cserélni [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream)-re. Ha frontendben találkozol vele:

1. Cseréld le a CDN script taget:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Távolítsd el az `AIChatProtocolClient` példányosítást (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Cseréld le `client.getStreamedCompletion(messages)`-t közvetlen `fetch()` hívásra a backend streaming végponton.
4. Cseréld le `for await (const response of result)`-et `for await (const chunk of readNDJSONStream(response.body))`-re.
5. Frissítsd a property hozzáférést `response.delta.content` / `response.error` helyett `chunk.delta.content` / `chunk.error` formára.

---

## Célok

- Sorold fel az összes Python hívási pontot, amelyek Chat Completions vagy régi Completions használatával az Azure OpenAI ellen futnak.
- Javasolj migrációs tervet és sorrendet a Python kódalap számára.
- Alkalmazz biztonságos, minimális módosításokat a Responses API-re váltáshoz.
- Frissítsd a hívókat, hogy a Responses kimeneti sémáját használják; ne hagyj hátra visszafelé kompatibilitási burkolókat.
- Futtass teszteket/lintelést; javítsd a migráció miatti apró hibákat.
- Készíts kis, átlátható változtatási csomagokat, majd adj végső összefoglalót különbségekkel (ne commitolj).

---

## Védelem

- Csak a git munkaterületen belüli fájlokat módosítsd. Soha ne írj kívül.
- Ne őrizz meg visszafelé kompatibilitási burkolókat; migráld a kódot az új API alakra.
- Ne hagyj átmeneti vagy biztonsági mentés megjegyzéseket, fájlokat.
- Ha korábban használtál streaminget, tartsd meg a streamelést; ha nem, használj nem-streamelt műveletet.
- Jóváhagyást kérj parancsok vagy hálózati hívások előtt, ha jóváhagyási módban vagy.
- Ne futtass `git add`/`git commit`/`git push` parancsokat; csak működőképes munkaterület módosításokat hozz létre.

---

## 0. lépés: Azure OpenAI kliens migráció (előfeltétel)

Ha a kódalap az `AzureOpenAI` vagy `AsyncAzureOpenAI` konstruktorokat használja, előbb migrálj a szabványos `OpenAI` / `AsyncOpenAI` konstruktorokra. Az Azure-specifikus konstruktorok elavultak az `openai>=1.108.1` verzióban.

### Miért az v1 API útvonal?

Az új `/openai/v1` végpont a szabványos `OpenAI()` klienst használja az `AzureOpenAI()` helyett, nem igényel `api_version` paramétert, és azonos módon működik OpenAI és Azure OpenAI esetén is. Ugyanazt a klienskódot használva jövőbiztos.

### Főbb változások

| Előtte | Utána |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Teljesen eltávolítandó |

### Takarítási ellenőrző lista

- Távolítsd el az `api_version` argumentumot a kliens konstruktorból.
- Távolítsd el az `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` környezeti változókat a `.env`, alkalmazás beállítások, és Bicep/infrastruktúra fájlokból.
- Nevezd át az `AZURE_OPENAI_CLIENT_ID`-t `AZURE_CLIENT_ID`-re `.env`, alkalmazás beállítások, Bicep/infrastruktúra és teszt fixture-okban (szabvány Azure Identity SDK konvenció).
- Biztosítsd, hogy `openai>=1.108.1` szerepeljen a `requirements.txt`-ben vagy `pyproject.toml`-ban.

### Környezeti változó migráció

| Régi env var | Intézkedés | Megjegyzés |
|-------------|--------|-------|
| `AZURE_OPENAI_VERSION` | **Eltávolítandó** | Az v1 végponthoz nincs szükség `api_version`-re |
| `AZURE_OPENAI_API_VERSION` | **Eltávolítandó** | Ugyanaz, mint fent |
| `AZURE_OPENAI_CLIENT_ID` | **Átnevezendő** → `AZURE_CLIENT_ID` | Szabvány Azure Identity SDK konvenció a `ManagedIdentityCredential(client_id=...)`-hez |
| `AZURE_OPENAI_ENDPOINT` | **Megőrizendő** | Kell a `base_url` összeállításához |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Megőrizendő** | Használatos mint `model` param a `responses.create`-ban |
| `AZURE_OPENAI_API_KEY` | **Megőrizendő** | Kulcs alapú hitelesítéshez az `api_key`-ként |

Kliens beállítási kód példákért (szinkron, aszinkron, EntraID, API kulcs, több bérlős) lásd [cheat-sheet.md](./references/cheat-sheet.md).

---

## 1. lépés: Régi hívási helyek észlelése

Futtasd a [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) szkriptet, hogy megtaláld az összes migrálandó hívási helyet:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Vagy végezd el kézzel az alábbi kereséseket — minden találat migrációs célpont:

```bash
# Régi API hívások (újra kell írni)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Elavult Azure kliens konstruktorok (ki kell cserélni)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Válasz alak hozzáférési minták (frissíteni kell)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Eszköz definíciók régi beágyazott formátumban (le kell lapítani)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Eszköz eredmények régi formátumban (át kell konvertálni function_call_output-ra)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Elavult paraméterek (el kell távolítani vagy át kell nevezni)
rg "response_format"
rg "max_tokens\b"        # átnevezni max_output_tokens-re
rg "['\"]seed['\"]"      # remove entirely

# Elavult környezeti változók (takarítani)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # AZURE_CLIENT_ID kell legyen

# GitHub Modellek végpontok (el kell távolítani — Responses API nem támogatott)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Keretrendszer-szintű régi minták (frissíteni kell)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: cseréljük OpenAIChatClient-re
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: use_responses_api=True szükséges

# Teszt infrastruktúra (frissíteni kell)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Tartalomszűrő hiba törzs hozzáférés (frissíteni kell — szerkezet megváltozott)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # régi egyes számú forma — most content_filter_results (többes szám) a content_filters tömbön belül

# Nyers HTTP hívások Chat Completions végponthoz (frissíteni kell az URL-t)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Heuristikák (észlel és átír)

- **Chat Completions kliens**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Azure kliens konstruktőrök**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Eszközök**: konvertáld a függvényhívó eszköz definíciókat egymásba ágyazott formátumból (`{"type": "function", "function": {"name": ...}}`) lapos Responses formátumba (`{"type": "function", "name": ...}`); használd a `tool_choice`-ot; az eszköz eredményeket add vissza `{"type": "function_call_output", "call_id": ..., "output": ...}` elemeként (ne `{"role": "tool", ...}`).
- **Eszköz köröket visszaadó műveletek**: amikor a modell függvényhívásokat ad vissza, illeszd a `response.output` elemeket a beszélgetéshez (ne kézzel `{"role": "assistant", "tool_calls": [...]}` szótárat), majd minden eredményhez illeszd a `function_call_output` elemeket.
- **Few-shot eszköz példák**: ha a beszélgetés fixen kódolt eszközhívás példákat tartalmaz, alakítsd őket át `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` elemekre. Az azonosítók `fc_`-vel kell kezdődjenek.
- **`pydantic_function_tool()`**: ez a segédfüggvény még az régi egymásba ágyazott formátumot generálja és **nem kompatibilis** a `responses.create()`-val. Helyettesítsd kézi eszközdefiníciókkal vagy egy laposítót csomagolóval.
- **Többszörös kör**: tárold a beszélgetés előzményeit az alkalmazásban; add át a korábbi köröket `input` elemekként.
- **Formázás**: cseréld a Chat `response_format` tetejű mezőjét Responses `text.format`-ra. Kanonikus alak: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Tartalmi elemek**: cseréld a Chat `content[].type: "text"`-jét Responses `content[].type: "input_text"`-re felhasználói/rendszer köröknél.
- **Kép tartalmi elemek**: cseréld a Chat `content[].type: "image_url"`-t Responses `content[].type: "input_image"`-re. Az `image_url` mező egy lapos stringgé változik, nem több beágyazott objektum (`{"url": "..."}`). Lásd a csalólapot a részletekért.
- **Érvelési erőfeszítés**: **csak akkor migráld a `reasoning`-et, ha az már létezik az eredeti kódban**.
- **Tartalomszűrő hiba kezelés**: a hiba törzs felépítése változott. A Chat Completions az `error.body["innererror"]["content_filter_result"]` (egyesszám) helyett a Responses API az `error.body["content_filters"][0]["content_filter_results"]` (többesszám, tömbön belül) struktúrát használja. Az `innererror` elérése `KeyError`-t dob. Írd át, hogy az új útvonalat használd.
- **Nyers HTTP hívások**: ha az alkalmazás közvetlenül hívja az Azure OpenAI REST API-t (pl. `requests`, `httpx`), az útvonal `/openai/deployments/{name}/chat/completions?api-version=...` helyett legyen `/openai/v1/responses`. A kérés törzse változik: `messages` → `input`, adj hozzá `max_output_tokens` és `store: false` mezőket, vedd ki az `api-version` query paramétert. A válasz törzse változik: `choices[0].message.content` → `output[0].content[0].text` (megjegyzés: az `output_text` egy SDK kényelmi tulajdonság, nincs meg a nyers REST JSON-ban).

---

## 2. lépés: Alkalmazd a migrációt

### Migrációs jegyzetek (Chat Completions → Responses)

- **Miért migráljunk**: a Responses az egységes API szöveg, eszközök és streaming kezelésére; a Chat Completions régi. GPT-5-tel a Responses elengedhetetlen a legjobb teljesítményhez.
- **HTTP**: az Azure végpont átvált az `/openai/deployments/{name}/chat/completions`-ról az `/openai/v1/responses`-ra.
- **Mezők**: `messages` → `input`, `max_tokens` → `max_output_tokens`. A `temperature` változatlan.
- **Formázás**: `response_format` → `text.format` egy megfelelő objektummal.
- **Tartalmi elemek**: cseréld a Chat `content[].type: "text"`-et Responses `content[].type: "input_text"`-re rendszer/felhasználói köröknél.
- **Kép tartalmi elemek**: cseréld a Chat `content[].type: "image_url"`-t Responses `content[].type: "input_image"`-re. Lapítsd le az `image_url` mezőt a `{"image_url": {"url": "..."}}`-ből `{"image_url": "..."}`-re (egyszerű string — lehet HTTPS URL vagy `data:image/...;base64,...` adat URI).

### Paraméter leképezési referencia

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (tömb elemei) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (objektum) |
| `temperature` | `temperature` (változatlan) |
| `stop` | `stop` (változatlan) |
| `frequency_penalty` | `frequency_penalty` (változatlan) |
| `presence_penalty` | `presence_penalty` (változatlan) |
| `tools` / függvényhívás | `tools` (változatlan) |
| `seed` | **Eltávolítandó** (nem támogatott) |
| `store` | `store` (állítva `false`-ra) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (lapos string) |

A teljes előtte/utána kód példákért lásd [cheat-sheet.md](./references/cheat-sheet.md).

Teszt infrastruktúra migrációhoz (mockok, snapshotok, állítások) lásd [test-migration.md](./references/test-migration.md).

Hibakereséshez, problémákhoz lásd [troubleshooting.md](./references/troubleshooting.md).

---

## Adatmegőrzés és állapot

- Állítsd a `store: false`-t minden Responses kérésen.
- Ne támaszkodj előző üzenetazonosítókra vagy szerveroldali tárolt kontextusra; az állapot legyen kliens által kezelt és minimalizáld a metaadatokat.

---

## Elfogadási kritériumok

### Kód szintű feltételek (mindnek teljesülnie kell)

- [ ] Nincs találat a `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` kifejezésre a migrált fájlokban.
- [ ] Nincs találat a `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` kifejezésre — minden konstruktőr az `OpenAI`/`AsyncOpenAI` v1 végpontot használja.
- [ ] Nincs találat a `rg "models\.github\.ai|models\.inference\.ai\.azure"` kifejezésre — GitHub Modellek kódútvonalak törölve.
- [ ] Nincs találat a `rg "OpenAIChatCompletionClient"`-re — MAF 1.0.0+ kód az `OpenAIChatClient`-et használja (ami a Responses API-t használja). Pre-1.0.0 esetén frissíts `agent-framework-openai>=1.0.0`-ra.
- [ ] Minden `ChatOpenAI(...)` hívás tartalmazza a `use_responses_api=True` paramétert.
- [ ] Nincs találat a `rg "choices\[0\]"` kifejezésre — minden válasz elérés `resp.output_text` vagy a Responses kimeneti sémájának megfelelő.
- [ ] Nincs `response_format` a felső szinten; minden strukturált kimenet `text={"format": {...}}` formátumot használ.
- [ ] `openai>=1.108.1` és `azure-identity` megtalálható `requirements.txt`-ben vagy `pyproject.toml`-ben; függőségek újratelepítve.
- [ ] `store=False` beállítva minden `responses.create` hívásnál.
- [ ] Nincs `api_version` az ügyfél létrehozásakor; `AZURE_OPENAI_API_VERSION` eltávolítva környezeti fájlokból és infrastruktúrából.

### Teszt infrastruktúra feltételek (mindnek teljesülnie kell)

- [ ] Nincs találat a `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/` kifejezésre.
- [ ] Nincs találat a `rg "_azure_ad_token_provider" tests/` kifejezésre — az állítások frissítve az `isinstance(client, AsyncOpenAI)` vagy `base_url` ellenőrzésére.
- [ ] Nincs találat a `rg "prompt_filter_results|content_filter_results" tests/` kifejezésre — Azure-specifikus szűrő mockok eltávolítva.
- [ ] Mock fixturek használják a `kwargs.get("input")`-et, nem a `kwargs.get("messages")`-t.
- [ ] Snapshot / golden fájlok frissítve a Responses streaming alakra (nincs `choices[0]`, `function_call`, `logprobs` stb.).
- [ ] `pytest` hibamentesen lefut minden teszt frissítés után.

### Viselkedési feltételek (kézi vagy teszteszközzel ellenőrizendő)

- [ ] **Alap befejezés**: nem streaming `responses.create` nem üres `output_text`-et ad vissza.
- [ ] **Stream paritás**: ha az eredeti kód streaminget használt, a migrált kód streamel és `response.output_text.delta` eseményeket ad nem üres delta értékekkel.
- [ ] **Strukturált kimenet**: ha `text.format` és `json_schema` használatban van, akkor a `json.loads(resp.output_text)` sikeres és megegyezik a sémával.
- [ ] **Eszközhívó ciklus**: ha eszközök használatban, a modell eszközhívásokat ad, az alkalmazás lefuttatja őket, és az utókövető kérés végső `output_text`-et ad (nincs végtelen ciklus).
- [ ] **Async paritás**: ha `AsyncAzureOpenAI` volt használatban, az `AsyncOpenAI` ekvivalens await használattal működik.
- [ ] **Hiba arány**: nincs új 400/401/404 hiba az elő-migrációs alapvonalhoz képest.

### Szállítandók

- Összefoglaló tartalmazza a szerkesztett fájlokat, régi hívások előtti/utáni számát és a következő lépéseket.
- A módosítások csak working-tree szerkesztések (nincsenek commitok).

---

## SDK verzió követelmények

| Csomag | Minimum verzió |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Legfrissebb (EntraID hitelesítéshez) |

---

## Hivatkozások

- [Csalólap — minden kódpélda](./references/cheat-sheet.md)
- [Teszt migráció — mockok, snapshotok, állítások](./references/test-migration.md)
- [Hibakeresés — hibák, kockázati tábla, buktatók](./references/troubleshooting.md)
- [detect_legacy.py — automatikus szkenner](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI kezdő készlet](https://aka.ms/openai/start)
- [Azure OpenAI Responses API dokumentáció](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Azure OpenAI API verzió életciklus](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API referencia](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->