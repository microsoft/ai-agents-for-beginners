---
name: azure-openai-to-responses
license: MIT
---
# Python alkalmazások migrálása az Azure OpenAI Chat Completions-ről a Responses API-re

> **HITELÉRHETŐ IRÁNYELV — PONTOSAN KÖVESSE**
>
> Ez a skill az Azure OpenAI Chat Completions-t használó Python kódalapokat migrálja
> az egységes Responses API-re. Kövesse pontosan ezeket az utasításokat.
> Ne improvizáljon paramétermappingeket és ne találjon ki API-formákat.

---

## Indítók

Aktiválja ezt a skilleet, amikor a felhasználó szeretné:
- Python alkalmazást migrálni az Azure OpenAI Chat Completions-ről a Responses API-re
- Frissíteni a Python OpenAI SDK használatát a legújabb API-formára az Azure OpenAI ellen
- Előkészíteni a Python kódot GPT-5 vagy újabb modellekhez, amelyek a Responses API-t igénylik az Azure-on
- Átváltani az `AzureOpenAI`/`AsyncAzureOpenAI` használatról a standard `OpenAI`/`AsyncOpenAI` kliensre a v1 végponttal
- Elhárítani a `AzureOpenAI` konstruktorokkal vagy `api_version`-nal kapcsolatos elavulási figyelmeztetéseket

---

## ⚠️ Modell kompatibilitás — ELLENŐRIZZE ELŐSZÖR

> **Migrálás előtt ellenőrizze, hogy az Azure OpenAI telepítése támogatja-e a Responses API-t.**

### 1. Gyors tesztelés (leggyorsabb)

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

> **Megjegyzés**: `max_output_tokens` Azure OpenAI-nál **minimum 16**. 16 alatti érték 400-as hibát ad. Használjon 50+ értéket gyorsteszthez.

Ha 404-et ad vissza, a telepítés modellje még nem támogatja a Responses API-t — nézze meg az alábbi hivatkozást, vagy telepítsen új modellt, ami támogatja.

### 2. Ellenőrizze a régiójában elérhető modelleket (ajánlott)

Futtassa a beépített modellkompatibilitás ellenőrző eszközt, hogy lássa mi érhető el a Responses API támogatásával az adott régióban:

```bash
python migrate.py models --subscription YOUR_SUB_ID --location YOUR_REGION
```

Ez az Azure ARM-ot kérdezi le, és egy kompatibilitási mátrixot mutat — mely modellek támogatják a Responses-t, strukturált kimenetet, eszközöket, stb. Használja a `--filter gpt-5.1,gpt-5.2` szűkítéshez vagy `--json`-t szkriptekhez.

### 3. Teljes modell támogatási referencia

- **Élő lekérdezés**: `python migrate.py models` (lásd fent — régióspecifikus, mindig friss)
- **Elérhetőség böngészése**: [Modell összefoglaló tábla és régió elérhetőség](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/models-sold-directly-by-azure?tabs=global-standard-aoai%2Cglobal-standard&pivots=azure-openai#model-summary-table-and-region-availability)
- **Gyorsindítás és útmutató**: **https://aka.ms/openai/start**

### ⚠️ Régebbi modellek korlátozásai

> **FIGYELMEZTETÉS**: A régebbi modellek (pl. `gpt-4o`, `gpt-4`) nem feltétlenül támogatnak minden Responses API funkciót teljesen.
>
> Ismert korlátozások régi modellekkel:
> - **`reasoning` paraméter**: Nem támogatott `gpt-4o-mini`, `gpt-4o` és sok nem-érvelő modell esetén. Csak akkor migrálja a `reasoning`-et, ha az eredeti kódban már jelen volt.
> - **`seed` paraméter**: Egyáltalán nem támogatott a Responses API-ban — távolítsa el minden kérésből.
> - **Strukturált kimenet `text.format` használatával**: A régebbi modellek nem feltétlenül érvényesítik pártatlanul a `strict: true` JSON sémákat.
> - **Eszköz-orchestration**: A GPT-5+ modellek az eszközhívásokat belső érvelés részének tekintik. A régebbi modellek Responses alatt is működnek, de nem rendelkeznek ilyen mély integrációval.
> - **Hőmérséklet korlátok**: Migráláskor `gpt-5`-re a temperature-t el kell hagyni vagy `1`-re állítani. A régebbi modellekre ez a korlát nem vonatkozik.

### O-sorozatú érvelő modellek (o1, o3-mini, o3, o4-mini)

Az O-sorozatú modellek egyedi paraméterkorlátokkal rendelkeznek. O-sorozatú modellekre célozó alkalmazások migrálásakor:

- **`temperature`**: Kizárólag `1` lehet (vagy elhagyható). Az O-sorozat más értéket nem fogad el.
- **`max_completion_tokens` → `max_output_tokens`**: Az Azure-specifikus `max_completion_tokens` használatát váltsa `max_output_tokens`-ra. Állítson magas értéket (4096+), mert az érvelő tokenek beleszámítanak a limitbe.
- **`reasoning_effort`**: Ha az alkalmazás használja a `reasoning_effort`-ot (low/medium/high), tartsa meg — a Responses API támogatja ezt az O-sorozatú modelleknél.
- **Streaming viselkedés**: Az O-sorozatú modellek az outputot az érvelés befejezéséig pufferezhetik mielőtt emitálnák a szöveg delta eseményeket. Streaming működik, de az első `response.output_text.delta` később érkezhet meg, mint GPT modelleknél.
- **`top_p`**: Nem támogatott az O-sorozatúaknál — távolítsa el, ha van.
- **Eszközhasználat**: Az O-sorozatú modellek az eszközöket a Responses API-n keresztül támogatják ugyanúgy, mint a GPT-k, de az eszközhívás orchestration minősége modelltől függ.

**Teendő — proaktív model ajánlás**: A vizsgálati fázisban nézze meg, melyik modellt célozza az alkalmazás (deployment nevek, környezeti változók, konfiguráció). Ha a modell `gpt-4o` vagy régebbi (nem gpt-4.1+), proaktívan tájékoztassa a felhasználót:
- A migráció működni fog alapvető szövegre, chatre, streamelésre és eszközökre a jelenlegi modellen.
- Az újabb modellek (`gpt-5.1`, `gpt-5.2`) jobb eszköz orchestrationt, strukturált kimenet érvényesítést, érvelést és régiók közötti elérhetőséget kínálnak.
- Fontolják meg a telepítésük frissítését, amikor készen állnak — ez nem gátolja a migrációt.

Ne akadályozza vagy tagadja meg a migrációt modell verzió alapján. Az ajánlás tájékoztató jellegű.

### A GitHub modellek NEM támogatják a Responses API-t

> **A GitHub modellek (`models.github.ai`, `models.inference.ai.azure.com`) nem támogatják a Responses API-t.**

Ha a kódbázisban van GitHub Models kódútvonal (keresse a `base_url`-t ami `models.github.ai` vagy `models.inference.ai.azure.com`-ra mutat), **távolítsa el teljesen** a migráció során. A Responses API Azure OpenAI-t, OpenAI-t vagy kompatibilis helyi végpontot igényel (pl. Ollama Responses támogatással).

A vizsgálati fázisban:
- Jelöljön meg minden GitHub Models kódútvonalat eltávolításra.

---

## Framework migráció

Sok alkalmazás magasabb szintű framework-öket használ az OpenAI fölött. Ezek migrálásakor a framework saját API változik — nem csak az alap OpenAI hívások.

### Microsoft Agent Framework (MAF)

**Ellenőrizze először a MAF verzióját** — a migráció függ attól, hogy MAF 1.0.0+ vagy pre-1.0.0 béta/rc.

#### MAF 1.0.0+ (agent-framework-openai >= 1.0.0)

Az `OpenAIChatClient` **már a Responses API-t használja** — nincs szükség migrációra. Ha a kódbázis a régi `OpenAIChatCompletionClient`-et használja (`chat.completions.create`-t), cserélje le `OpenAIChatClient`-re.

| Előtte | Utána |
|--------|-------|
| `from agent_framework.openai import OpenAIChatCompletionClient` | `from agent_framework.openai import OpenAIChatClient` |
| `OpenAIChatCompletionClient(...)` | `OpenAIChatClient(...)` |

Verzió ellenőrzéséhez: `python -c "import agent_framework_openai; print(agent_framework_openai.__version__)"`

#### MAF pre-1.0.0 (béta/rc kiadások)

A pre-1.0.0 MAF `OpenAIChatClient` Chat Completions-t használt. Frissítsen `agent-framework-openai>=1.0.0`-ra, ahol az `OpenAIChatClient` alapból a Responses API-t használja.

Egyéb változtatás nem szükséges — az `Agent` és az eszköz API-k változatlanok maradnak.

### LangChain (`langchain-openai`)

Adja hozzá a `use_responses_api=True` opciót a `ChatOpenAI()`-hoz. A válasz elérését is frissítse `.content`-ről `.text`-re.

| Előtte | Utána |
|--------|-------|
| `ChatOpenAI(model=..., base_url=..., api_key=...)` | `ChatOpenAI(model=..., base_url=..., api_key=..., use_responses_api=True)` |
| `result['messages'][-1].content` | `result['messages'][-1].text` |

Teljes előtte/utána kódpéldákért lásd [cheat-sheet.md](./references/cheat-sheet.md).

---

## Frontend migrációs útmutató

> **A Responses API szerveroldali kérdés.** Migrálja a Python backendjét; a frontend HTTP szerződésének nem szabad változnia, kivéve ha a backend csak vékony passthrough — ilyen esetben fontolja meg a Responses kérésforma használatát, hogy megszüntesse az átkódoló réteget. Ha a frontend közvetlenül OpenAI-t hív ügyfél-oldali kulccsal, helyezze át ezeket a hívásokat elsőként a backendbe.

### `@microsoft/ai-chat-protocol` elavulás

Az `@microsoft/ai-chat-protocol` npm csomag elavult, és helyette az [`ndjson-readablestream`](https://www.npmjs.com/package/ndjson-readablestream) használata javasolt. Ha frontendben találkozik vele:

1. Cserélje le a CDN script taget:
   ```html
   <!-- Before -->
   <script src="https://cdn.jsdelivr.net/npm/@microsoft/ai-chat-protocol@.../dist/iife/index.js"></script>
   <!-- After -->
   <script src="https://cdn.jsdelivr.net/npm/ndjson-readablestream@1.0.7/dist/ndjson-readablestream.umd.js"></script>
   ```
2. Távolítsa el az `AIChatProtocolClient` példányosítást (`new ChatProtocol.AIChatProtocolClient("/chat")`).
3. Cserélje le a `client.getStreamedCompletion(messages)` hívást közvetlen `fetch()` hívásra a backend streaming végpontra.
4. Cserélje a `for await (const response of result)` ciklust `for await (const chunk of readNDJSONStream(response.body))`-re.
5. Frissítse az property elérést `response.delta.content` / `response.error`-ről `chunk.delta.content` / `chunk.error`-re.

---

## Célok

- Azonosítsa az összes Python hívási helyet, amely Chat Completions-t vagy régi Completions-t használ az Azure OpenAI ellen.
- Javasoljon migrációs tervet és sorrendet a Python kódalapra.
- Alkalmazzon biztonságos, minimális módosításokat a Responses API-re váltáshoz.
- Frissítse a hívókat, hogy a Responses kimeneti sémáját használják; ne használjon visszafelé kompatibilitási borítókat.
- Futtasson teszteket/ellenőrzéseket; javítsa a migráció által okozott apró hibákat.
- Készítsen kis, áttekinthető változáscsomagokat és adja meg a végső összegzést diffekkel (ne commitálja).

---

## Védelem

- Csak a git munkaterületen belüli fájlokat módosítsa. Sohase írjon kívül.
- Ne tartson fent visszafelé kompatibilitási shim-eket; migráljon az új API-formára.
- Ne hagyjon átmeneti vagy archivált kommenteket, vagy biztonsági mentési fájlokat.
- Ha korábban használt streaminget, tartsa meg azt; különben használjon nem-streaming módot.
- Járuljon hozzá futtatás előtt a parancsokhoz vagy hálózati hívásokhoz, ha engedélyezett.
- Ne használja a `git add`/`git commit`/`git push` parancsokat; csak dolgozófa állapotra vonatkozó módosításokat készítsen.

---

## 0. lépés: Azure OpenAI kliens migráció (előfeltétel)

Ha a kódbázis `AzureOpenAI` vagy `AsyncAzureOpenAI` konstruktorokat használ, migrálja először a standard `OpenAI` / `AsyncOpenAI` konstruktorokra. Az Azure-specifikus konstruktorok elavultak az `openai>=1.108.1` verzióban.

### Miért a v1 API elérési út?

Az új `/openai/v1` végpont a standard `OpenAI()` klienst használja az `AzureOpenAI()` helyett, nem igényel `api_version` paramétert, és OpenAI-n és Azure OpenAI-n egyaránt ugyanúgy működik. Ugyanaz a klienskód jövőbiztos — nem szükséges verziókezelés.

### Fontos változások

| Előtte | Utána |
|--------|-------|
| `AzureOpenAI` | `OpenAI` |
| `AsyncAzureOpenAI` | `AsyncOpenAI` |
| `azure_endpoint` | `base_url` |
| `azure_ad_token_provider` | `api_key` |
| `api_version=...` | Teljes eltávolítás |

### Takarítási ellenőrzőlista

- Távolítsa el az `api_version` argumentumot a kliens létrehozásakor.
- Távolítsa el a `AZURE_OPENAI_VERSION` / `AZURE_OPENAI_API_VERSION` környezeti változókat a `.env`, alkalmazásbeállítások és Bicep/infrastruktúra fájlokból.
- Nevezze át a `AZURE_OPENAI_CLIENT_ID`-t `AZURE_CLIENT_ID`-re `.env`, app beállítások, Bicep/infrastruktúra és teszt fixture-ökben (szabványos Azure Identity SDK konvenció).
- Biztosítsa az `openai>=1.108.1` jelenlétét a `requirements.txt` vagy `pyproject.toml` fájlokban.

### Környezeti változó migráció

| Régi env var | Teendő | Megjegyzések |
|-------------|--------|-------------|
| `AZURE_OPENAI_VERSION` | **Eltávolítás** | A v1 végpont nem igényel `api_version`-t |
| `AZURE_OPENAI_API_VERSION` | **Eltávolítás** | Ugyanaz, mint fent |
| `AZURE_OPENAI_CLIENT_ID` | **Átnevezés** → `AZURE_CLIENT_ID` | Szabványos Azure Identity SDK konvenció a `ManagedIdentityCredential(client_id=...)`-hez |
| `AZURE_OPENAI_ENDPOINT` | **Megőrzés** | Szükséges továbbra is a `base_url` felépítéséhez |
| `AZURE_OPENAI_CHAT_DEPLOYMENT` | **Megőrzés** | `model` paraméterként használatos a `responses.create` hívásban |
| `AZURE_OPENAI_API_KEY` | **Megőrzés** | API kulcs alapú hitelesítéshez használt `api_key` |

Kliens beállítás kód példákért (szinkron, aszinkron, EntraID, API kulcs, multi-tenant) lásd [cheat-sheet.md](./references/cheat-sheet.md).

---

## 1. lépés: Régi hívási helyek érzékelése

Futtassa a [detect_legacy.py](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py) szkriptet, hogy megtalálja az összes migrálandó hívási helyet:

```bash
python skills/azure-openai-to-responses/scripts/detect_legacy.py .
```

Vagy manuálisan keresse meg ezeket — minden találat migrációs célpont:

```bash
# Legacy API hívások (újra kell írni)
rg "chat\.completions\.create"
rg "ChatCompletion\.create"
rg "Completion\.create"

# Elavult Azure kliens konstruktőrök (ki kell cserélni)
rg "AzureOpenAI\("
rg "AsyncAzureOpenAI\("

# Válasz forma elérési minták (frissíteni kell)
rg "choices\[0\]\.message\.content"
rg "choices\[0\]\.delta\.content"
rg "choices\[0\]\.message\.function_call"
rg "choices\[0\]\.message\.tool_calls"

# Eszköz definíciók régi, beágyazott formátumban (kiegyenesíteni kell)
rg '"function":\s*{\s*"name"'
rg "pydantic_function_tool"

# Eszköz eredmények régi formátumban (át kell konvertálni function_call_output-ra)
rg '"role":\s*"tool"'
rg '"tool_call_id"'

# Elavult paraméterek (el kell távolítani vagy át kell nevezni)
rg "response_format"
rg "max_tokens\b"        # átnevezni max_output_tokens-re
rg "['\"]seed['\"]"      # remove entirely

# Elavult környezeti változók (tisztítani kell)
rg "AZURE_OPENAI_API_VERSION|AZURE_OPENAI_VERSION"
rg "AZURE_OPENAI_CLIENT_ID"  # ennek AZURE_CLIENT_ID-nek kell lennie

# GitHub Modellek végpontok (el kell távolítani — Responses API nem támogatott)
rg "models\.github\.ai|models\.inference\.ai\.azure"

# Keretrendszer szintű régi minták (frissíteni kell)
rg "OpenAIChatCompletionClient"  # MAF 1.0.0+: cserélje le OpenAIChatClient-re
rg "ChatOpenAI\(" | grep -v "use_responses_api"  # LangChain: szükséges use_responses_api=True

# Teszt infrastruktúra (frissíteni kell)
rg "ChatCompletionChunk|AsyncCompletions\.create" tests/
rg "_azure_ad_token_provider" tests/
rg "prompt_filter_results|content_filter_results" tests/
rg "choices\[0\]" tests/

# Tartalomszűrő hibatest hozzáférés (frissíteni kell — szerkezet megváltozott)
rg 'innererror.*content_filter_result|error\.body\["innererror"\]'
rg "content_filter_result\[" # régi egyes szám — most content_filter_results (többes szám) a content_filters tömbön belül

# Nyers HTTP hívások a Chat Completions végponthoz (frissíteni kell az URL-t)
rg "/openai/deployments/.*/chat/completions"
rg "api-version="
```

### Heurisztikák (észlelés és átírás)

- **Chat Completions kliens**: `client.chat.completions.create` → `client.responses.create(...)`.

- **Azure kliens konstruktorok**: `AzureOpenAI(...)` → `OpenAI(base_url=..., api_key=...)`.
- **Eszközök**: a függvényhívó eszközdefiníciókat konvertáld át beágyazott formátumból (`{"type": "function", "function": {"name": ...}}`) lapos Responses formátumba (`{"type": "function", "name": ...}`); használd a `tool_choice`-ot; az eszközök eredményeit `{"type": "function_call_output", "call_id": ..., "output": ...}` elemekként add vissza (nem `{"role": "tool", ...}` formában).
- **Eszköz körök**: amikor a modell függvényhívásokat ad vissza, fűzd hozzá a `response.output` elemeket a beszélgetéshez (nem manuális `{"role": "assistant", "tool_calls": [...]}` szótárként), majd hozzáadod a `function_call_output` elemeket az egyes eredményekhez.
- **Néhány lövés eszközpéldák**: ha a beszélgetés tartalmaz kódba ágyazott eszközhívási példákat, alakítsd át őket `{"type": "function_call", "id": "fc_...", "call_id": "fc_...", ...}` + `{"type": "function_call_output", ...}` elemekre. Az azonosítóknak `fc_`-val kell kezdődniük.
- **`pydantic_function_tool()`**: ez a segédfüggvény még mindig a régi beágyazott formátumot generálja, és **nem kompatibilis** a `responses.create()`-vel. Helyettesítsd manuális eszközdefiníciókkal vagy laposító csomagolóval.
- **Több körös**: tartsd meg a beszélgetés előzményeit az alkalmazásban; add át az előző köröket `input` elemek formájában.
- **Formázás**: cseréld le a Chat felső szintű `response_format` mezőjét `text.format`-ra a Responses-ban. Kanonikus alak: `text={"format": {"type": "json_schema", "name": "Output", "strict": True, "schema": {...}}}`.
- **Tartalmi elemek**: cseréld a Chat `content[].type: "text"` értékeit Responses `content[].type: "input_text"` értékre felhasználó/rendszer körök esetén.
- **Kép tartalmi elemek**: cseréld a Chat `content[].type: "image_url"` értékeit Responses `content[].type: "input_image"` értékre. Az `image_url` mező a beágyazott objektumból `{"url": "..."}` egy lapos stringgé válik. Lásd a cheat sheet-et a előtte/utána példákért.
- **Indoklási erőfeszítés**: **csak akkor migráld a `reasoning` mezőt, ha az már az eredeti kódban létezik**.
- **Tartalomszűrő hibakezelés**: a hiba test szerkezete megváltozott. Chat Completion-nél `error.body["innererror"]["content_filter_result"]` (egyes szám) volt; Responses API használja a `error.body["content_filters"][0]["content_filter_results"]` (többes szám, tömbben). A `innererror`-hoz való hozzáférés `KeyError`-t okoz. Írd át az új elérési útra.
- **Nyers HTTP hívások**: ha az alkalmazás közvetlenül az Azure OpenAI REST API-t hívja (`requests`, `httpx`, stb.) `/openai/deployments/{name}/chat/completions?api-version=...` végponton, írd át `/openai/v1/responses` végpontra. A kérés törzs változik: `messages` → `input`, hozzáad `max_output_tokens` és `store: false`, törli az `api-version` lekérdezési paramétert. A válasz törzs változik: `choices[0].message.content` → `output[0].content[0].text` (megjegyzés: `output_text` egy SDK kényelem tulajdonság, ami nem szerepel a nyers REST JSON-ban).

---

## 2. lépés: Migráció alkalmazása

### Migrációs megjegyzések (Chat Completions → Responses)

- **Miért migráljunk**: A Responses az egységes API szöveghez, eszközökhöz és streaminghez; a Chat Completions örökség. GPT-5-tel a legjobb teljesítményhez a Responses használata kötelező.
- **HTTP**: az Azure végpont vált `/openai/deployments/{name}/chat/completions`-ről `/openai/v1/responses`-re.
- **Mezők**: `messages` → `input`, `max_tokens` → `max_output_tokens`. `temperature` változatlan.
- **Formázás**: `response_format` → `text.format` megfelelő objektummal.
- **Tartalmi elemek**: cseréld a Chat `content[].type: "text"` értékeket Responses `content[].type: "input_text"` értékekre rendszer/felhasználói köröknél.
- **Kép tartalmi elemek**: cseréld a Chat `content[].type: "image_url"` értékeket Responses `content[].type: "input_image"` értékekre. Lapítsd ki az `image_url` mezőt `{"image_url": {"url": "..."}}` → `{"image_url": "..."}` (egyszerű string — HTTPS URL vagy `data:image/...;base64,...` adat URI).

### Paraméter leképezési referencia

| Chat Completions | Responses API |
|-----------------|---------------|
| `prompt` | `input` |
| `messages` | `input` (elemek tömbje) |
| `max_tokens` | `max_output_tokens` |
| `response_format` | `text.format` (objektum) |
| `temperature` | `temperature` (változatlan) |
| `stop` | `stop` (változatlan) |
| `frequency_penalty` | `frequency_penalty` (változatlan) |
| `presence_penalty` | `presence_penalty` (változatlan) |
| `tools` / függvényhívás | `tools` (változatlan) |
| `seed` | **Eltávolítandó** (nem támogatott) |
| `store` | `store` (`false`-ra állítva) |
| `content[].type: "text"` | `content[].type: "input_text"` |
| `content[].type: "image_url"` | `content[].type: "input_image"` |
| `"image_url": {"url": "..."}` | `"image_url": "..."` (lapos string) |

Teljes, előtte/utána kódpéldákért lásd a [cheat-sheet.md](./references/cheat-sheet.md) fájlt.

A teszt infrastruktúra migrációjához (mock-ok, snapshotok, állítások) lásd a [test-migration.md](./references/test-migration.md) fájlt.

Hibák és buktatók megoldásához lásd a [troubleshooting.md](./references/troubleshooting.md) dokumentumot.

---

## Adatmegőrzés és állapot

- Állíts be `store: false` értéket az összes Responses kérésen.
- Ne támaszkodj korábbi üzenet-azonosítókra vagy szerveroldali kontextusra; tartsd az állapotot kliens által kezeltnek és minimalizáld a metaadatokat.

---

## Elfogadási kritériumok

### Kódszintű átjárók (mindnek át kell menni)

- [ ] Nulla találat `rg "chat\.completions\.create|ChatCompletion\.create|Completion\.create"` kifejezésre a migrált fájlokban.
- [ ] Nulla találat `rg "AzureOpenAI\(|AsyncAzureOpenAI\("` kifejezésre — minden konstruktor `OpenAI`/`AsyncOpenAI`-t használ az v1 végponttal.
- [ ] Nulla találat `rg "models\.github\.ai|models\.inference\.ai\.azure"` — eltávolított GitHub Models kódútvonalak.
- [ ] Nulla találat `rg "OpenAIChatCompletionClient"` — MAF 1.0.0+ kódban `OpenAIChatClient` használata (ami a Responses API-t használja). Pre-1.0.0 esetén frissíts `agent-framework-openai>=1.0.0`-ra.
- [ ] Minden `ChatOpenAI(...)` hívás tartalmazza a `use_responses_api=True` paramétert.
- [ ] Nulla találat `rg "choices\[0\]"` — az összes válasz elérés `resp.output_text` vagy a Responses kimeneti séma szerint történik.
- [ ] Nincs `response_format` felső szinten; minden strukturált kimenet `text={"format": {...}}` formátumot használ.
- [ ] `openai>=1.108.1` és `azure-identity` benne van a `requirements.txt`-ben vagy `pyproject.toml`-ben; függőségek újratelepítve.
- [ ] `store=False` beállítva minden `responses.create` hívásnál.
- [ ] Nincs `api_version` a kliens konstrukcióban; az `AZURE_OPENAI_API_VERSION` törölve az env fájlokból és infrastruktúrából.

### Teszt infrastruktúra átjárók (mindnek át kell menni)

- [ ] Nulla találat `rg "ChatCompletionChunk|AsyncCompletions\.create|chat\.completions" tests/` könyvtárban.
- [ ] Nulla találat `rg "_azure_ad_token_provider" tests/` — állításokat frissítették, hogy `isinstance(client, AsyncOpenAI)` vagy `base_url` szerint ellenőrizzenek.
- [ ] Nulla találat `rg "prompt_filter_results|content_filter_results" tests/` — Azure-specifikus filter mock-ok eltávolítva.
- [ ] Mock fixture-k `kwargs.get("input")`-et használnak `kwargs.get("messages")` helyett.
- [ ] Snapshot / golden fájlok frissítve Responses streaming formára (nincs `choices[0]`, `function_call`, `logprobs`, stb.).
- [ ] `pytest` nulla hibával lefut minden teszt frissítés után.

### Viselkedési átjárók (kézi ellenőrzés vagy tesztházzal)

- [ ] **Alapvető kiegészítés**: nem streaming `responses.create` visszaad nem üres `output_text`-et.
- [ ] **Streaming paritás**: ha az eredeti kód streaminget használt, a migrált kód streameli és adja a `response.output_text.delta` eseményeket nem üres deltalokkal.
- [ ] **Strukturált kimenet**: ha `text.format` és `json_schema` van használatban, `json.loads(resp.output_text)` sikeres és megegyezik a sémával.
- [ ] **Eszközhívó ciklus**: ha eszközöket használnak, a modell eszközhívásokat indít, az app végrehajtja azokat, és a következő kérés visszaad egy végleges `output_text`-et (végtelen ciklus nélkül).
- [ ] **Async paritás**: ha `AsyncAzureOpenAI` volt használatban, az ekvivalens `AsyncOpenAI` működik `await`-tel.
- [ ] **Hibaarány**: nincs új 400/401/404 hiba az előtti migrációs állapothoz képest.

### Szállítandók

- Összefoglaló tartalmazza a módosított fájlokat, a régi hívási helyek előtti/utáni számait és a következő lépéseket.
- A változtatások csak working-tree szerkesztések (nincsenek commitok).

---

## SDK verzió követelmények

| Csomag | Minimális verzió |
|---------|----------------|
| `openai` | `>=1.108.1` |
| `azure-identity` | Legújabb (EntraID hitelesítéshez) |

---

## Hivatkozások

- [Cheat Sheet — az összes kódpélda](./references/cheat-sheet.md)
- [Teszt Migráció — mock-ok, snapshotok, állítások](./references/test-migration.md)
- [Hibaelhárítás — hibák, kockázati táblázat, buktatók](./references/troubleshooting.md)
- [detect_legacy.py — automatizált szkenner](../../../../../.agents/skills/azure-openai-to-responses/scripts/detect_legacy.py)
- [Azure OpenAI Starter Kit](https://aka.ms/openai/start)
- [Azure OpenAI Responses API dokumentáció](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/responses)
- [Azure OpenAI API verzió életciklus](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/api-version-lifecycle?view=foundry-classic&tabs=python#api-evolution)
- [OpenAI Responses API referencia](https://platform.openai.com/docs/api-reference/responses)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->