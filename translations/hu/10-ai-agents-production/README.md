# AI Agentek a termelésben: Megfigyelhetőség és értékelés

[![AI Agents in Production](../../../translated_images/hu/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Ahogy az AI agentek az experimentális prototípusoktól a valós világban használt alkalmazások felé haladnak, egyre fontosabbá válik a viselkedésük megértése, a teljesítményük figyelése és az eredményeik szisztematikus értékelése.

## Tanulási Célok

A leckének a végére tudni fogod/meg fogod érteni:
- Az agent megfigyelhetőség és értékelés alapfogalmait
- Technikákat az agentek teljesítményének, költségeinek és hatékonyságának javításához
- Mit és hogyan értékelj szisztematikusan az AI agentjeidnél
- Hogyan kontrolláld a költségeket AI agentek termelési bevezetésekor
- Hogyan instrumentáld azokat az agenteket, amiket a Microsoft Agent Frameworkkel építesz

A cél az, hogy olyan tudást adjunk át, amivel "fekete dobozos" agentjeidet átlátható, kezelhető és megbízható rendszerekké alakíthatod.

_**Megjegyzés:** Fontos, hogy biztonságos és megbízható AI Agenteket vezessünk be. Nézd meg a [Meghitt AI Agentek építése](../06-building-trustworthy-agents/README.md) leckét is._

## Traces és Spans

A megfigyelhetőségi eszközök, mint a [Langfuse](https://langfuse.com/) vagy a [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry), általában az agent futásokat traces és spans formájában jelenítik meg.

- **Trace** egy teljes agent feladatot reprezentál a kezdetétől a végéig (például egy felhasználói lekérdezés kezelése).
- **Spans** a trace egyes lépései (például egy nyelvi modell hívása vagy adatlekérés).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Megfigyelhetőség nélkül egy AI agent „fekete doboznak” tűnhet – belső állapota és logikája átlátszatlan, nehéz hibát diagnosztizálni vagy a teljesítményt optimalizálni. Megfigyelhetőséggel az agentek „üveg dobozzá” válnak, átláthatóságot kínálva, amely létfontosságú a bizalom kiépítéséhez és annak biztosításához, hogy rendeltetésszerűen működjenek.

## Miért fontos a megfigyelhetőség a termelési környezetben?

AI agentek termelési környezetbe való áthelyezése új kihívásokat és követelményeket hoz. A megfigyelhetőség már nem „jó, ha van”, hanem kritikus képesség:

*   **Hibakeresés és Okfeltáró Elemzés:** Amikor egy agent hibázik vagy váratlan eredményt produkál, a megfigyelhetőségi eszközök rendelkezésre bocsátják a szükséges trace-eket a hiba forrásának beazonosításához. Ez különösen fontos komplex agenteknél, amelyek több LLM hívást, eszközinterakciót és feltételes logikát tartalmazhatnak.
*   **Késleltetés és Költségkezelés:** Az AI agentek gyakran LLM-ekre és külső API-kra támaszkodnak, melyeket token vagy hívás alapján számláznak. A megfigyelhetőség lehetővé teszi ezen hívások pontos nyomon követését, segítve az olyan műveletek azonosítását, amelyek túl lassúak vagy költségesek. Ezáltal a csapatok optimalizálhatják a promptokat, hatékonyabb modelleket választhatnak, vagy újratervezhetik a munkafolyamatokat, hogy kezeljék az üzemeltetési költségeket és jó felhasználói élményt biztosítsanak.
*   **Bizalom, Biztonság és Megfelelés:** Sok alkalmazásban fontos biztosítani, hogy az agentek biztonságosan és etikusan viselkedjenek. A megfigyelhetőség audit nyomvonalat biztosít az agent műveleteiről és döntéseiről. Ez használható olyan problémák detektálására és kezelése, mint a prompt injekció, káros tartalom létrehozása vagy személyes azonosító információk (PII) nem megfelelő kezelése. Például áttekintheted a trace-eket, hogy megértsd, miért adott az agent adott választ vagy miért használt egy konkrét eszközt.
*   **Folyamatos Fejlesztési Ciklusok:** A megfigyelhetőségi adatok egy iteratív fejlesztési folyamat alapjai. A valódi világban nyújtott teljesítmény figyelésével a csapatok azonosíthatják a fejlesztendő területeket, adatokat gyűjthetnek a modellek finomhangolásához, és validálhatják a változtatások hatását. Ez visszacsatolási hurkot hoz létre, ahol a termelési betekintések az online értékelésből visszahatnak az offline kísérletezésre és finomításra, ami egyre jobb ügynök teljesítményt eredményez.

## Követendő Fő Mutatók

Az agent viselkedésének figyelemmel kíséréséhez és megértéséhez számos mutatót és jelet kell figyelni. A specifikus mutatók változhatnak az agent céljától függően, de néhány általánosan fontos.

Íme néhány a leggyakoribb mutatók közül, amelyeket a megfigyelhetőségi eszközök monitoroznak:

**Késleltetés:** Milyen gyorsan válaszol az agent? A hosszú várakozási idők negatívan befolyásolják a felhasználói élményt. Kell mérned a késleltetést a feladatokra és az egyes lépésekre is, trace-ek segítségével. Például, ha egy agent a teljes modellhívásokra 20 másodpercet igényel, gyorsabb modellel vagy párhuzamos hívásokkal felgyorsítható.

**Költségek:** Mennyi a költség egy agent futtatásra? Az AI agentek LLM hívásokat használnak tokenalapú számlázással vagy külső API-kat. Gyakori eszközhasználat vagy többszörös promptok gyorsan növelhetik a költségeket. Például, ha egy agent ötször hív egy LLM-et egész kismértékű minőségjavulásért, fontold meg, hogy megéri-e a költséget, vagy csökkenteni kell a hívások számát vagy egy olcsóbb modellt használni. Az élő monitorozás segíthet váratlan kiugrások azonosításában (pl. hibák miatt túlzott API ciklusok).

**Kérés Hibák:** Hány kérés sikertelen az agentnél? Ez magában foglalhat API hibákat vagy sikertelen eszközhívásokat. Ahhoz, hogy az agent robosztusabb legyen éles környezetben, beállíthatsz visszaeséseket vagy újrapróbálkozásokat. Pl. ha az LLM szolgáltató A nem elérhető, váltasz a B szolgáltatóra tartalékként.

**Felhasználói Visszajelzés:** A közvetlen felhasználói értékelések értékes betekintéseket adnak. Ez lehet egyértelmű értékelés (👍fel, 👎le, ⭐1-5 csillag) vagy szöveges kommentek. A következetesen negatív visszajelzések figyelmeztetnek, hogy az agent nem a vártak szerint működik.

**Implicit Felhasználói Visszajelzés:** A felhasználók viselkedése közvetett visszajelzést ad még explict értékelések nélkül is. Ez magában foglalhat azonnali kérdésátfogalmazást, ismételt lekérdezéseket vagy ismétlés gomb megnyomását. Pl. ha látod, hogy a felhasználók ismételten ugyanazt a kérdést teszik fel, az a jele annak, hogy az agent nem működik megfelelően.

**Pontosság:** Milyen gyakran produkál az agent helyes vagy kívánatos kimenetet? A pontosság definíciói változnak (pl. problémamegoldás helyessége, információ visszakeresési pontosság, felhasználói elégedettség). Az első lépés meghatározni, mi a siker az agent számára. Követheted az pontosságot automata ellenőrzések, értékelési pontszámok vagy feladat teljesítési címkék alapján. Például trace-ek megjelölése „sikeres” vagy „sikertelen” státusszal.

**Automatizált Értékelési Mutatók:** Beállíthatsz automatikus értékeléseket is. Például használhatsz LLM-et az agent kimenetének értékelésére, vajon segítőkész, pontos-e vagy sem. Számos nyílt forráskódú könyvtár segít különböző aspektusok pontozásában, pl. [RAGAS](https://docs.ragas.io/) RAG agentekhez vagy [LLM Guard](https://github.com/protectai/llm-guard) káros nyelv vagy prompt injekció detektálására.

Gyakorlatban ezen mutatók kombinációja adja a legjobb lefedettséget egy AI agent egészségére vonatkozóan. Ebben a fejezetben a [példa jegyzetfüzetben](./code_samples/10-expense_claim-demo.ipynb) megmutatjuk, hogyan néznek ki ezek a mutatók valós példákban, de előbb tanuljuk meg, hogyan néz ki egy tipikus értékelési munkafolyamat.

## Instrumentáld az Agentet

A trace adatok gyűjtéséhez instrumentálnod kell a kódodat. A cél, hogy az agent kódja olyan trace-eket és metrikákat adjon le, amelyeket egy megfigyelhetőségi platform elfogadhat, feldolgozhat és vizualizálhat.

**OpenTelemetry (OTel):** Az [OpenTelemetry](https://opentelemetry.io/) iparági szabványként jelent meg az LLM megfigyelhetőséghez. API-kat, SDK-kat és eszközöket nyújt a telemetriai adatok generálásához, gyűjtéséhez és exportálásához.

Számos instrumentációs könyvtár létezik, amelyek beburkolják a meglévő agent keretrendszereket, és megkönnyítik az OpenTelemetry span-ek exportálását megfigyelhetőségi eszközökbe. A Microsoft Agent Framework natívan integrálódik az OpenTelemetry-vel. Az alábbi példa egy MAF agent instrumentálására:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agent execution is traced automatically
    pass
```

Ebben a fejezetben a [példa jegyzetfüzet](./code_samples/10-expense_claim-demo.ipynb) megmutatja, hogyan instrumentáld a MAF agented.

**Manuális Span Létrehozás:** Bár az instrumentációs könyvtárak jó alapot adnak, sok esetben részletesebb vagy egyedi információkra van szükség. Manuálisan is létrehozhatsz span-eket egyedi alkalmazási logikákkal. Ami még fontosabb, bővítheted az automatikusan vagy manuálisan létrehozott span-eket egyedi attribútumokkal (más néven címkék vagy metaadatok). Ezek az attribútumok tartalmazhatnak üzleti specifikus adatokat, köztes számításokat vagy bármilyen kontextust, ami hasznos lehet hibakereséshez vagy elemzéshez, mint például `user_id`, `session_id` vagy `model_version`.

Példa trace-ek és span-ek manuális létrehozására a [Langfuse Python SDK-val](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agent Értékelés

A megfigyelhetőség mutatókat szolgáltat, de az értékelés az az adat elemzési folyamat (és tesztek végzése), amivel meghatározzuk, mennyire teljesít jól az AI agent, és hogyan javítható. Másképp fogalmazva, amikor megvannak a trace-ek és metrikák, hogyan használod őket az agent megítéléséhez és döntésekhez?

Rendszeres értékelés fontos, mert az AI agentek gyakran nem determinisztikusak és fejlődhetnek (frissítéseken vagy modell viselkedés eltolódáson keresztül) – értékelés nélkül nem tudnád, hogy az „okos agented” tényleg jól végzi-e a munkáját, vagy visszaesett.

Két kategória van AI agentek értékelésében: **online értékelés** és **offline értékelés**. Mindkettő értékes, és kiegészítik egymást. Általában offline értékeléssel kezdünk, mert ez a minimálisan szükséges lépés ügynök bevezetése előtt.

### Offline Értékelés

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Ez az agent kontrollált környezetben történő értékelését jelenti, tipikusan teszt adathalmazokkal, nem élő felhasználói lekérdezésekkel. Kurált adatokat használsz, ahol tudod, mi a várt kimenet vagy helyes viselkedés, és azokon futtatod az agentet.

Például, ha egy matek szöveges feladatokat megoldó agentet építettél, lehet egy [teszt adatkészleted](https://huggingface.co/datasets/openai/gsm8k) 100 ismert megoldású problémával. Az offline értékelést gyakran fejlesztés alatt végzik (és része lehet CI/CD folyamatoknak), hogy ellenőrizzék a javulást vagy akadályozzák a visszaesést. Előnye, hogy **ismételhető és tiszta pontossági mérőszámokat ad, mert megvan az igazság**. Szimulálhatod a felhasználói lekérdezéseket és mérheted az agent válaszait az ideális megoldásokhoz képest, vagy használhatod az automatizált metrikákat, ahogy fentebb leírtuk.

Az offline értékelés kulcskihívása az, hogy az adatkészlet átfogó és releváns maradjon – az agent jól teljesíthet egy fix tesztkészleten, de a termelésben nagyon eltérő kérdésekkel találkozhat. Ezért naprakészen kell tartanod a tesztkészleteket új szélsőséges esetekkel és a valós élet szcenáriókat tükröző példákkal. Hasznos egy keverék: kis „füstteszt” esetek gyors ellenőrzésre és nagyobb értékelő készletek szélesebb körű teljesítmény mérésre.

### Online Értékelés

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Ez azt jelenti, hogy az agentet élő, valós környezetben értékeljük, vagyis a termelésben való tényleges használat során. Az online értékelés belefoglalja az agent teljesítményének figyelését valós felhasználói interakciókon és az eredmények folyamatos elemzését.

Például követheted a sikerességi arányokat, felhasználói elégedettségi pontszámokat vagy más metrikákat élő forgalomnál. Az online értékelés előnye, hogy **megragad olyan dolgokat, amit labor körülmények között nem feltétlenül várnál** – megfigyelheted a modell eltolódását az idő múlásával (ha az agent hatékonysága romlik az input mintázatok változásával) és elcsíphetsz váratlan lekérdezéseket vagy helyzeteket, amik nem voltak a tesztadatokban. Valódi képet ad az agent természetszerű viselkedéséről.

Az online értékelés gyakran gyűjt implicit és explicit felhasználói visszajelzést, ahogy korábban tárgyaltuk, és előfordulhat árnyék tesztek vagy A/B tesztek futtatása is (ahol az agent új verziója párhuzamosan fut a régivel az összehasonlításhoz). Kihívás, hogy nehéz megbízható címkéket vagy pontszámokat szerezni élő interakciókhoz – gyakran a felhasználói visszajelzésekre vagy lenyomati mutatókra (pl. az eredményre kattintott-e a felhasználó) támaszkodhatsz.

### A kettő kombinálása

Az online és offline értékelés nem kizárólagos; erősen kiegészítik egymást. Az online monitorozásból származó észrevételeket (pl. új típusú felhasználói kérdések, ahol az agent gyengén teljesít) felhasználhatod az offline tesztadatkészletek bővítésére és javítására. Fordítva, az offline teszteken jól teljesítő agenteket magabiztosabban telepítheted és figyelheted online.

Tény, hogy sok csapat egy ciklust követ:

_offline értékel -> telepít -> online monitoroz -> új hibás eseteket gyűjt -> hozzáad az offline adatokhoz -> finomhangolja az agentet -> ismét_

## Gyakori problémák

AI agentek termelési környezetbe való bevezetése során különféle kihívásokkal találkozhatsz. Íme néhány gyakori probléma és lehetséges megoldásaik:

| **Probléma**    | **Lehetséges megoldás**   |
| ------------- | ------------------ |
| Az AI agent nem végzi a feladatokat következetesen | - Finomítsd az agentnek adott promptokat; legyél világos a célokkal.<br>- Azonosítsd, hol segíthet a feladatokat alfeladatokra bontani és több agentet használni. |
| Az AI agent folyamatos ciklusokba fut  | - Biztosíts világos befejezési feltételeket, hogy tudja, mikor álljon le.<br>- Összetett, érvelést és tervezést igénylő feladatokhoz használd a nagyobb, érvelési feladatokra szakosodott modellt. |
| AI agent eszköz hívások nem jól működnek   | - Teszteld és validáld az eszköz kimenetét az agent rendszeren kívül.<br>- Finomítsd a definiált paramétereket, promptokat és az eszközök elnevezését.  |
| Többagent rendszer nem működik következetesen | - Finomítsd az egyes agenteknek adott promptokat, hogy specifikusak és megkülönböztethetőek legyenek.<br>- Építs hierarchikus rendszert, egy „irányító” vagy vezérlő agenttel, amely meghatározza, hogy melyik agent a megfelelő. |

Sok problémát hatékonyabban azonosítanak megfigyelhetőség segítségével. Az előzőekben tárgyalt trace-ek és metrikák pontosan megmutatják, hogy az agent munkafolyamat mely pontján jelentkeznek problémák, így a hibakeresés és optimalizálás jóval hatékonyabbá válik.

## Költségek kezelése

Íme néhány stratégia AI agentek termelési bevezetésének költségeinek kezelésére:

**Kisebb modellek használata:** A kis nyelvi modellek (SLM-ek) bizonyos agentikus felhasználási esetekben jól teljesíthetnek, és jelentősen csökkentik a költségeket. Ahogy korábban említettük, a legjobb módja annak, hogy megértsük, mennyire jól teljesít egy SLM az Ön használati esetében, ha kiépítünk egy értékelő rendszert a teljesítményük meghatározására és összehasonlítására a nagyobb modellekkel. Fontolja meg SLM-ek használatát egyszerűbb feladatokra, például szándék osztályozásra vagy paraméterkinyerésre, miközben a nagyobb modelleket összetett következtetésekhez tartogatja.

**Router modell használata:** Egy hasonló stratégia, ha különféle modelleket és méreteket használunk. Használhat egy LLM/SLM-et vagy szerver nélküli függvényt arra, hogy a kéréseket a komplexitás szerint a legmegfelelőbb modellekhez irányítsa. Ez segít csökkenteni a költségeket, miközben a teljesítményt a megfelelő feladatoknál biztosítja. Például az egyszerű lekérdezéseket kisebb, gyorsabb modellekhez irányítsa, és csak az összetett következtetési feladatokhoz használja a drága nagy modelleket.

**Válaszok gyorsítótárazása:** Gyakori kérések és feladatok azonosítása, illetve a válaszok megadása még mielőtt átmennének az agentikus rendszerén, jó módja a hasonló kérések mennyiségének csökkentésére. Még egy olyan folyamatot is megvalósíthat, amely azonosítja, mennyire hasonló egy kérés a gyorsítótárazott kéréseihez alapvetőbb AI modellek segítségével. Ez a stratégia jelentősen csökkentheti a gyakran feltett kérdésekre vagy gyakori munkafolyamatokra jutó költségeket.

## Nézzük meg, hogyan működik ez a gyakorlatban

A [szakasz példafüzete](./code_samples/10-expense_claim-demo.ipynb) példákat mutat arra, hogyan használhatunk megfigyelési eszközöket az agentünk figyelésére és értékelésére.


### További kérdései vannak az AI ügynökökről a termelésben?

Csatlakozzon a [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) csoporthoz, hogy találkozzon más tanulókkal, részt vegyen irodai órákon, és kérdéseit megválaszolják az AI ügynökökről.

## Előző lecke

[Metakogníció tervezési minta](../09-metacognition/README.md)

## Következő lecke

[Agentikus protokollok](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->