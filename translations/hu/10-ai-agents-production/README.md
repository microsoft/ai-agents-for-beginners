# AI ügynökök a gyakorlatban: megfigyelhetőség és értékelés

[![AI Agents in Production](../../../translated_images/hu/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Ahogy az AI ügynökök az kísérleti prototípusoktól a valós alkalmazások felé haladnak, egyre fontosabbá válik a viselkedésük megértése, teljesítményük figyelése és kimeneteik szisztematikus értékelése.

## Tanulási célok

A lecke elvégzése után tudni fogod / meg fogod érteni:
- Az ügynök megfigyelhetőségének és értékelésének alapfogalmait
- Az ügynökök teljesítményének, költségeinek és hatékonyságának javítási technikáit
- Mit és hogyan értékelj szisztematikusan az AI ügynökeiden
- Hogyan kontrolláld a költségeket AI ügynökök éles környezetbe történő telepítésekor
- Hogyan kell instrumentálni AutoGen-nel épített ügynököket

A cél, hogy olyan tudással ruházzunk fel téged, amely átláthatóvá, kezelhetővé és megbízhatóvá teszi a „fekete dobozos” ügynökeidet.

_**Megjegyzés:** Fontos, hogy biztonságos és megbízható AI ügynököket telepíts. Nézd meg a [Megbízható AI Ügynökök Építése](../06-building-trustworthy-agents/README.md) leckét is._

## Trace-ek és Span-ek

A megfigyelhetőségi eszközök, mint a [Langfuse](https://langfuse.com/) vagy a [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) általában trace-ek és span-ek formájában jelenítik meg az ügynök futásokat.

- **Trace:** egy teljes ügynök feladatot reprezentál a kezdetétől a végéig (például egy felhasználói kérés kezelése).
- **Span-ek:** trace-en belüli egyedi lépések (például egy nyelvi modell hívása vagy adatlekérés).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)

Megfigyelhetőség nélkül az AI ügynök olyan, mint egy „fekete doboz” – a belső állapota és érvelése átláthatatlan, megnehezítve a problémák diagnosztizálását vagy teljesítmény optimalizálását. A megfigyelhetőség által az ügynökök „üvegdobozokká” válnak, átláthatóságot nyújtva, ami elengedhetetlen a bizalomépítéshez és a szándéknak megfelelő működés biztosításához.

## Miért fontos a megfigyelhetőség az éles környezetekben

Az AI ügynökök éles környezetbe való átültetése új kihívásokat és követelményeket hoz magával. A megfigyelhetőség már nem „kényelmi kiegészítő”, hanem kritikus képesség:

*   **Hibakeresés és okfeltárás:** Ha az ügynök hibázik vagy váratlan kimenetet produkál, a megfigyelhetőségi eszközök trace-eket biztosítanak a hiba forrásának beazonosításához. Ez különösen fontos komplex ügynökök esetén, amelyek több LLM hívást, eszköz interakciót és feltételes logikát tartalmazhatnak.
*   **Késleltetés és költség menedzsment:** Az AI ügynökök gyakran LLM-ekre vagy más külső API-kra támaszkodnak, amelyek token vagy hívás alapú számlázásúak. A megfigyelhetőség pontos nyomon követést tesz lehetővé, segítve azonosítani a túl lassú vagy túl költséges műveleteket. Ezáltal optimalizálhatók a promptok, választhatók hatékonyabb modellek vagy újratervezhetők a munkafolyamatok az üzemeltetési költségek kezeléséhez és a jó felhasználói élmény biztosításához.
*   **Bizalom, biztonság és megfelelőség:** Sok alkalmazásban fontos biztosítani, hogy az ügynökök biztonságosan és etikusan viselkedjenek. A megfigyelhetőség auditírozási nyomvonalat ad az ügynök tevékenységeiről és döntéseiről. Ez felhasználható például prompt befecskendezés, káros tartalom generálása vagy személyes azonosítható információk (PII) nem megfelelő kezelése elleni védekezésre. Például trace-ek áttekintésével megértheted, miért adott egy adott válasz az ügynök vagy miért használt egy adott eszközt.
*   **Folyamatos fejlesztési ciklusok:** A megfigyelhetőségi adatok az iteratív fejlesztési folyamat alapját képezik. Az ügynökök valós környezetben nyújtott teljesítményének megfigyelésével azonosíthatók a fejlesztendő területek, gyűjthetők adatok a finomhangoláshoz, és validálhatók a változások hatásai. Ez egy visszacsatolási hurkot hoz létre, ahol az online értékelésből származó üzemeltetési ismeretek kiegészítik az offline kísérletezést és finomítást, ami egyre jobb ügynökteljesítményt eredményez.

## Fontos mérőszámok nyomon követése

Az ügynök viselkedésének megfigyeléséhez sokféle mérőszámot és jelet kell figyelni. Bár a konkrét mutatók az ügynök céljától függenek, néhány univerzálisan fontos.

Íme néhány általánosan megfigyelt mérőszám az eszközök által:

**Késleltetés:** Milyen gyorsan válaszol az ügynök? A hosszú várakozási idő rontja a felhasználói élményt. Mérd a késleltetést a feladatokra és az egyes lépésekre agent futások trace-elésével. Például egy olyan ügynök, amely 20 másodperc alatt végzi el az összes modellhívást, gyorsítható egy gyorsabb modell használatával vagy a párhuzamos modellhívásokkal.

**Költségek:** Mennyibe kerül egy ügynök futtatása? Az AI ügynökök LLM hívásokra (token alapon számlázva) vagy külső API-kra épülnek. Gyakori eszközhasználat vagy sok prompt gyorsan növelheti a költségeket. Például, ha egy ügynök ötször hív egy LLM-et egy marginális minőségjavításért, meg kell vizsgálni, hogy megéri-e a költség, vagy csökkenthető-e a hívások száma, illetve olcsóbb modell használata is lehetséges. A valós idejű monitorozás segíthet észrevenni váratlan kiugrásokat is (pl. hibák okozta túlzott API hurok).

**Kéréshibák:** Hány kérést nem sikerült kivitelezni? Ez magában foglalhat API hibákat vagy sikertelen eszközhívásokat. A megbízható ügynök érdekében beállíthatók tartalék megoldások vagy újrapróbálkozások. Pl. ha az LLM szolgáltató A leáll, akkor automatikusan váltasz a B szolgáltatóra tartaléknak.

**Felhasználói visszajelzés:** Közvetlen felhasználói értékelések implementálása értékes betekintést nyújt. Ez explicit értékeléseket (👍tetszik/👎nem tetszik, ⭐1-5 csillag) vagy szöveges kommenteket tartalmazhat. Az ismétlődően negatív visszajelzés jelzi, hogy az ügynök nem működik megfelelően.

**Implicit felhasználói visszajelzés:** A felhasználói viselkedés közvetett visszajelzést ad anélkül, hogy explicit értékelések lennének. Ez magában foglalja a kérdés azonnali átformálását, ismételt lekérdezéseket vagy az újrapróbálkozás gomb használatát. Pl. ha látod, hogy a felhasználók ismételten ugyanazt a kérdést teszik fel, az annak jele, hogy az ügynök nem működik elvárt módon.

**Pontosság:** Milyen gyakran ad az ügynök helyes vagy kívánatos kimenetet? A pontosság definíciója változó (pl. problémamegoldási helyesség, információkeresési pontosság, felhasználói elégedettség). Az első lépés annak meghatározása, hogy mi az ügynök sikeres működése. Követhető automatikus ellenőrzésekkel, értékelési pontszámokkal vagy feladat teljesítési címkékkel. Például trace-ek megjelölése sikeres vagy sikertelen állapotúként.

**Automatizált értékelési mérőszámok:** Automatizált értékeléseket is beállíthatsz. Például LLM-et használhatsz az ügynök kimenetének értékelésére, hogy mennyire segítőkész, pontos vagy sem. Több nyílt forráskódú könyvtár is létezik, amelyek segítenek értékelni az ügynök különböző aspektusait, pl. [RAGAS](https://docs.ragas.io/) RAG ügynökökhöz vagy [LLM Guard](https://llm-guard.com/) káros nyelvezet vagy prompt befecskendezés felismerésére.

A gyakorlatban ezek kombinációja adja az AI ügynök egészségi állapotának legjobb lefedését. Ebben a fejezetben a [példa jegyzetfüzetben](./code_samples/10_autogen_evaluation.ipynb) megmutatjuk, hogyan néznek ki ezek a mérőszámok valós példákon, de előbb megnézzük, hogy néz ki egy tipikus értékelési munkafolyamat.

## Instrumentáld az ügynöködet

Trace adatok gyűjtéséhez instrumentálni kell a kódot. A cél az, hogy az ügynök kódja trace-eket és mérőszámokat bocsásson ki, amelyeket megfigyelhetőségi platform képes fogadni, feldolgozni és vizualizálni.

**OpenTelemetry (OTel):** Az [OpenTelemetry](https://opentelemetry.io/) iparági szabvánnyá vált az LLM megfigyelhetőség területén. API-kat, SDK-kat és eszközöket kínál telemetry adatok generálására, gyűjtésére és exportálására.

Számos instrumentációs könyvtár létezik, amelyek létező ügynök keretrendszereket csomagolnak be, és megkönnyítik az OpenTelemetry span-ek exportját megfigyelhetőségi eszközökbe. Az alábbi példa egy AutoGen ügynök instrumentálása a [OpenLit instrumentációs könyvtár](https://github.com/openlit/openlit) használatával:

```python
import openlit

openlit.init(tracer = langfuse._otel_tracer, disable_batch = True)
```

A fejezet [példa jegyzetfüzete](./code_samples/10_autogen_evaluation.ipynb) bemutatja, hogyan lehet instrumentálni az AutoGen ügynöködet.

**Span-ek kézi létrehozása:** Az instrumentációs könyvtárak jó alapot adnak, de vannak esetek, amikor részletesebb vagy egyedi információ szükséges. Kézzel is létrehozhatsz span-eket egyedi alkalmazáslogika hozzáadására. Fontos, hogy gazdagítani is lehet automatikusan vagy manuálisan létrehozott span-eket egyedi attribútumokkal (ismert még tagek vagy metaadatok néven). Ezek az attribútumok üzlet-specifikus adatokat, köztes számításokat vagy bármilyen kontextust tartalmazhatnak, amely hasznos lehet hibakereséshez vagy elemzéshez, például `user_id`, `session_id` vagy `model_version`.

Példa trace-ek és span-ek kézi létrehozására a [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3) használatával:

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Ügynök értékelése

A megfigyelhetőség mérőszámokat ad, de az értékelés az az adat elemzése (és tesztek végzése), hogy megállapítsuk, az AI ügynök milyen jól teljesít, és hogyan lehet javítani. Más szóval, ha már vannak trace-ek és mérőszámok, hogyan használhatod őket az ügynök megítélésére és döntések meghozatalára?

A rendszeres értékelés fontos, mert az AI ügynökök gyakran nem determinisztikusak és fejlődhetnek (frissítések vagy modell viselkedés eltérés miatt) – értékelés nélkül nem tudnád, hogy az „okos ügynököd” tényleg jól végzi-e a munkáját vagy visszaesett.

Két fő értékelési kategória van AI ügynökök számára: **online értékelés** és **offline értékelés**. Mindkettő értékes és egymást kiegészítik. Általában offline értékeléssel kezdünk, mivel ez az alaplépés bármely ügynök telepítése előtt.

### Offline értékelés

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Ez a kontrollált körülmények között, általában tesztadatokon végzett értékelést jelenti, nem élő felhasználói lekéréseken. Olyan előre összeállított adatállományokat használsz, amelyeknél ismert a várt kimenet vagy helyes viselkedés, majd lefuttatod az ügynököt ezen.

Például, ha egy matematikai szöveges feladatmegoldó ügynököt építettél, lehet, hogy van egy [tesztadatokból álló készleted](https://huggingface.co/datasets/gsm8k) 100 ismert megoldású problémával. Az offline értékelést gyakran fejlesztés közben végezzük (és része lehet a CI/CD folyamatoknak) a javítások ellenőrzésére vagy visszaesések elkerülésére. Az előnye, hogy **ismételhető és világos pontossági mutatókat kaphatsz, mert van igazságérték**. Szimulálhatod a felhasználói lekérdezéseket és mérheted az ügynök válaszait az ideális válaszokkal szemben, vagy használhatsz automatizált mérőszámokat, amint azt fentebb bemutattuk.

A fő kihívás az offline értékelésnél, hogy a tesztadatok legyenek átfogóak és relevánsak – az ügynök jól teljesíthet a fix tesztadatokon, de élesben egészen más lekérdezésekkel találkozhat. Ezért frissíteni kell a tesztkészleteket új éls esetekkel és példákkal, amelyek a valós helyzeteket tükrözik. Hasznos a kis „füstteszt” esetsor vegyítése nagyobb értékelő halmazokkal: az előbbiek gyors ellenőrzést, az utóbbiak szélesebb körű teljesítménymutatókat biztosítanak.

### Online értékelés

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Ez az ügynök élő, valós környezetben történő értékelését jelenti, vagyis a tényleges éles használat során. Az online értékelés magában foglalja az ügynök valós felhasználói interakciókra vonatkozó teljesítményének folyamatos nyomon követését és az eredmények elemzését.

Például követheted a sikerességi arányokat, a felhasználói elégedettség pontszámokat vagy más mérőszámokat élő forgalomban. Az online értékelés előnye, hogy **olyan dolgokat is feltárhat, amelyekre a laboratóriumi körülmények között nem számítanál** – megfigyelheted a modell eltolódását idővel (ha az ügynök hatékonysága romlik az inputminták változása miatt) és észreveheted azokat a váratlan lekérdezéseket vagy helyzeteket, amelyek nem szerepeltek a tesztadatokban. Valódi képet ad arról, hogyan viselkedik az ügynök az éles környezetben.

Az online értékelés gyakran magában foglalja az implicit és explicit felhasználói visszajelzések gyűjtését, valamint árnyék teszteket vagy A/B teszteket is (amikor egy új ügynök verzió párhuzamosan fut, hogy összehasonlítható legyen a régivel). A kihívás az, hogy nehéz megbízható címkéket vagy pontszámokat kapni az élő interakciókhoz – ilyenkor esetleg a felhasználói visszajelzésre vagy a downstream mérőszámokra (például kattintott-e a felhasználó az eredményre) támaszkodhatsz.

### Kettő kombinálása

Az online és offline értékelések nem kizárólagosak, hanem nagymértékben kiegészítik egymást. Az online megfigyelésből származó észrevételek (például új felhasználói lekérdezési típusok, ahol az ügynök gyengén teljesít) használhatók az offline tesztadatok bővítésére és fejlesztésére. Ezzel szemben azok az ügynökök, amelyek jól teljesítenek az offline tesztekben, biztonságosabban telepíthetők és online figyelhetők.

Sok csapat egy hurkot alkalmaz:

_offline értékelés -> telepítés -> online monitorozás -> új hibás esetek gyűjtése -> hozzáadás az offline adatállományhoz -> ügynök finomítása -> ismétlés_.

## Gyakori problémák

Az AI ügynökök élesben történő telepítésekor különféle kihívásokba ütközhetsz. Íme néhány gyakori probléma és lehetséges megoldás:

| **Probléma**    | **Lehetséges megoldás**   |
| ------------- | ------------------ |
| AI ügynök nem végzi el következetesen a feladatokat | - Finomítsd az AI ügynöknek adott promptokat; legyenek világosak az elvárások.<br>- Azonosítsd, hol segíthet a feladatok alfeladatokra bontása és több ügynök párhuzamos kezelése. |
| AI ügynök folyamatos hurkokba kerül | - Biztosíts terminációs feltételeket, hogy az ügynök tudja, mikor kell leállítani a folyamatot.<br>- Összetett feladatokhoz, amelyek érvelést és tervezést igényelnek, használj nagyobb modellt, amely specializált ezen feladatokra. |
| AI ügynök eszköz hívások nem működnek jól | - Teszteld és validáld az eszköz kimenetét az ügynök rendszerén kívül.<br>- Finomítsd a paramétereket, promptokat és az eszközök elnevezését.  |
| Több ügynökös rendszer következetlenül teljesít | - Finomítsd az egyes ügynököknek adott promptokat, hogy specifikusak és egymástól elkülönültek legyenek.<br>- Építs hierarchikus rendszert „irányító” vagy vezérlő ügynökkel, amely meghatározza, melyik ügynök a megfelelő. |

Ezek a problémák sokkal hatékonyabban azonosíthatók megfigyelhetőség megléte esetén. Az előzőekben tárgyalt trace-ek és mérőszámok pontosan megmutatják, hol van az ügynök munkafolyamatában probléma, így a hibakeresés és optimalizálás sokkal eredményesebb.

## Költségek kezelése
Itt van néhány stratégia az AI ügynökök élesbe állítási költségeinek kezelésére:

**Kisebb modellek használata:** A kis nyelvi modellek (SLM-ek) bizonyos ügynöki esetekben jól teljesíthetnek, és jelentősen csökkentik a költségeket. Ahogy korábban említettük, egy értékelő rendszer felépítése, amely meghatározza és összehasonlítja a teljesítményt a nagyobb modellekkel szemben, a legjobb módszer annak megértésére, hogy egy SLM milyen jól fog teljesíteni az adott felhasználási esetben. Fontolja meg az SLM-ek használatát egyszerűbb feladatokra, például szándékosztályozásra vagy paraméterkinyerésre, miközben a nagyobb modelleket összetett következtetésekhez tartogatja.

**Router modell használata:** Egy hasonló stratégia a különböző modellek és méretek kombinálása. Használhat egy LLM/SLM-et vagy szerver nélküli funkciót, amely a komplexitás alapján irányítja a kéréseket a legmegfelelőbb modellekhez. Ez szintén segít csökkenteni a költségeket, miközben biztosítja a teljesítményt a megfelelő feladatokon. Például egyszerű lekérdezéseket kisebb, gyorsabb modellekhez irányítson, és csak költséges nagyobb modelleket használjon összetett következtetési feladatokhoz.

**Válaszok gyorsítótárazása:** Gyakori kérések és feladatok azonosítása, valamint ezek válaszainak előzetes biztosítása az ügynöki rendszerhez való eljutás előtt jó módja a hasonló kérések mennyiségének csökkentésére. Még egy folyamatot is megvalósíthat arra, hogy meghatározza, mennyire hasonló egy kérés a gyorsítótárazott kéréseihez, alapszintű AI modellek segítségével. Ez a stratégia jelentősen csökkentheti a költségeket gyakran feltett kérdések vagy tipikus munkafolyamatok esetén.

## Nézzük, hogyan működik ez a gyakorlatban

A [szakasz példánaplójában](./code_samples/10_autogen_evaluation.ipynb) példákat fogunk látni arra, hogyan használhatjuk az megfigyelhetőségi eszközöket az ügynökünk monitorozására és értékelésére.


### Több kérdésed van az AI ügynökökről az éles környezetben?

Csatlakozz a [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) közösséghez, hogy találkozz más tanulókkal, részt vegyél konzultációkon és megválaszoltasd AI Ügynökökkel kapcsolatos kérdéseidet.

## Előző leckék

[Metakogníciós tervezési minta](../09-metacognition/README.md)

## Következő lecke

[Ügynöki protokollok](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ezt a dokumentumot az AI fordító szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) használatával fordítottuk le. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén számít hivatalos forrásnak. Kritikus információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->