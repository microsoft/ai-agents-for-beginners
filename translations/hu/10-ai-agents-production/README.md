# AI Ügynökök éles környezetben: Megfigyelhetőség és értékelés

[![AI Ügynökök éles környezetben](../../../translated_images/hu/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Ahogy az AI ügynökök a kísérleti prototípusoktól a valós alkalmazásokig fejlődnek, egyre fontosabbá válik viselkedésük megértése, teljesítményük nyomon követése és kimeneteik szisztematikus értékelése.

## Tanulási célok

A lecke elvégzése után tudni fogja/hogy értse meg:
- Az ügynök megfigyelhetőség és értékelés alapvető fogalmait
- Technikákat az ügynökök teljesítményének, költségeinek és hatékonyságának javítására
- Mit és hogyan értékeljen szisztematikusan az AI ügynökeinél
- Hogyan kontrollálja a költségeket az AI ügynökök éles üzembe helyezésekor
- Hogyan kell instrumentálni a Microsoft Agent Framework-kel épített ügynököket

A cél az, hogy az Ön kezébe olyan tudást adjunk, amellyel "fekete doboz" ügynökeiből átlátható, kezelhető és megbízható rendszereket alakíthat ki.

_**Megjegyzés:** Fontos, hogy biztonságos és megbízható AI ügynököket telepítsünk. Nézze meg a [Bizalomépítő AI Ügynökök építése](./06-building-trustworthy-agents/README.md) leckét is._

## Trace-ek és Span-ek

A megfigyelhetőségi eszközök, mint a [Langfuse](https://langfuse.com/) vagy a [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) általában trace-ek és span-ek formájában ábrázolják az ügynök futásokat.

- **Trace** egy teljes ügynök feladatot reprezentál a kezdetétől a végéig (például egy felhasználói lekérdezés kezelése).
- **Span-ek** a trace egyedi lépései (például egy nyelvi modell meghívása vagy adat lekérése).

![Trace fa a Langfuse-ban](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Megfigyelhetőség nélkül egy AI ügynök olyan, mint egy "fekete doboz" – belső állapota és érvelése átláthatatlan, nehéz hibát diagnosztizálni vagy a teljesítményt optimalizálni. Megfigyelhetőséggel az ügynökök "üvegdobozokká" válnak, transzparenciát nyújtva, ami létfontosságú a bizalom kiépítéséhez és annak biztosításához, hogy úgy működjenek, ahogy azt elvárjuk.

## Miért fontos a megfigyelhetőség az éles környezetekben?

Az AI ügynökök éles környezetekbe való átültetése új kihívásokat és követelményeket hoz magával. A megfigyelhetőség már nem „jó, ha van”, hanem kritikus képességgé válik:

*   **Hibakeresés és gyökérok-elemzés**: Ha egy ügynök hibázik vagy váratlan kimenetet produkál, a megfigyelhetőségi eszközök trace-jei segítenek a hiba forrásának feltárásában. Ez különösen fontos összetett ügynökök esetén, amelyek több LLM hívást, eszközinterakciót és feltételes logikát tartalmazhatnak.
*   **Késleltetés és költségkezelés**: Az AI ügynökök gyakran LLM-ekre és más külső API-kra támaszkodnak, amelyeket token vagy hívás alapon számláznak. A megfigyelhetőség lehetővé teszi ezen hívások pontos nyomon követését, segítve azonosítani a túl lassú vagy költséges műveleteket. Ez lehetővé teszi csapatok számára promptok optimalizálását, hatékonyabb modellek kiválasztását vagy munkafolyamatok áttervezését a működési költségek kezelésére és a jó felhasználói élmény biztosítására.
*   **Bizalom, biztonság és megfelelőség**: Sok alkalmazásnál fontos, hogy az ügynökök biztonságosan és etikusan működjenek. A megfigyelhetőség auditálási nyomot biztosít az ügynök műveleteiről és döntéseiről. Ezzel észlelhető és mérsékelhető a prompt-injektálás, káros tartalom generálása vagy személyes azonosító információk (PII) helytelen kezelése. Például megtekintheti a trace-eket, hogy megértse, miért adott az ügynök egy bizonyos választ vagy használt egy adott eszközt.
*   **Folyamatos fejlesztési ciklusok**: A megfigyelhetőség adatai az iteratív fejlesztési folyamat alapját képezik. Az ügynökök valós környezetben történő teljesítményének monitorozásával a csapatok azonosíthatják a fejlesztendő területeket, adatokat gyűjthetnek a modellek finomhangolásához, illetve validálhatják a változtatások hatását. Ez egy visszacsatolási kört hoz létre, ahol az éles online értékelésből származó betekintések az offline kísérletezést és finomítást segítik elő, vezetve a fokozatosan jobb ügynök teljesítményhez.

## Követendő kulcs metrikák

Az ügynök viselkedésének nyomon követéséhez és megértéséhez számos metrikát és jelet kell mérni. Bár a konkrét metrikák az ügynök céljától függően változhatnak, néhány univerzálisan fontos.

Íme a megfigyelhetőségi eszközök által leggyakrabban követett metrikák:

**Késleltetés:** Milyen gyorsan válaszol az ügynök? A hosszú várakozási idők negatívan befolyásolják a felhasználói élményt. Mérje a késleltetést feladatokra és egyes lépésekre agent futtatások trace-elésével. Például, ha egy ügynök 20 másodpercet tölt az összes modell hívással, gyorsítható egy gyorsabb modell használatával vagy párhuzamos hívásokkal.

**Költségek:** Mennyibe kerül egy ügynök futás? Az AI ügynökök LLM hívásokra vagy külső API-kra támaszkodnak, melyeket token vagy hívás alapján számláznak. Gyakori eszközhasználat vagy sok prompt gyorsan növeli a költségeket. Például, ha egy ügynök ötször hívja meg az LLM-et apró minőségi javulás érdekében, mérlegelnie kell, hogy a költség indokolt-e, vagy csökkentheti a hívások számát, esetleg olcsóbb modellt használhat. Azonnali monitorozás segíthet váratlan költségcsúcsok azonosításában (pl. hibák miatt túl sok API hívás).

**Kéréshibák:** Hány kérést nem tudott teljesíteni az ügynök? Ez magában foglalhat API hibákat vagy sikertelen eszközhívásokat. Az ügynök robosztusabbá tétele érdekében állítson be visszaesési stratégiákat vagy újrapróbálkozásokat. Pl. ha az LLM szolgáltató A leáll, válthat a B szolgáltatóra.

**Felhasználói visszajelzés:** Közvetlen felhasználói értékelések értékes betekintést adnak. Ide tartozhatnak explicit értékelések (👍/👎, ⭐1-5 csillag) vagy szöveges kommentek. Az ismétlődően negatív visszajelzés figyelmeztetés, hogy az ügynök nem működik az elvárások szerint.

**Implicit felhasználói visszajelzés:** A felhasználói viselkedés közvetett visszajelzést ad explicit értékelések nélkül is. Ilyen lehet a kérdés azonnali átformálása, ismételt lekérdezések vagy az újrapróbálkozás gomb használata. Pl. ha a felhasználók többször ismétlik ugyanazt a kérdést, az arra utal, hogy az ügynök nem megfelelő.

**Pontosság:** Milyen gyakran ad helyes vagy kívánatos kimenetet az ügynök? A pontosság definíciója változó (pl. probléma megoldás helyessége, információkinyerés pontossága, felhasználói elégedettség). Az első lépés meghatározni, hogy mi az Ön ügynöke számára a siker. Követheti a pontosságot automatizált ellenőrzésekkel, értékelési pontszámokkal vagy feladat befejezési címkékkel (pl. trace-ek „sikeres” vagy „sikertelen” megjelölése).

**Automatizált értékelési metrikák:** Beállíthat automatizált értékeléseket is. Például használhat LLM-et az ügynök kimenetének pontozására (pl. hasznosság, pontosság alapján). Több nyílt forráskódú könyvtár is létezik különböző aspektusok értékelésére, pl. [RAGAS](https://docs.ragas.io/) RAG ügynökökhöz vagy [LLM Guard](https://llm-guard.com/) káros nyelvezet vagy prompt injektálás észlelésére.

A gyakorlatban ezeknek a metrikáknak a kombinációja adja az AI ügynök állapotának legjobb lefedettségét. Ebben a fejezetben található [példa jegyzetkönyv](./code_samples/10-expense_claim-demo.ipynb) valós példákon mutatja be ezeket a metrikákat, de előbb nézzük meg, hogyan néz ki egy tipikus értékelési munkafolyamat.

## Instrumentálja az ügynökét

A trace adatok gyűjtéséhez instrumentálnia kell a kódot. A cél az, hogy az ügynök kódot úgy instrumentálja, hogy trace-eket és metrikákat bocsásson ki, amelyeket egy megfigyelhetőségi platform el tud fogadni, feldolgozni és vizualizálni.

**OpenTelemetry (OTel):** Az [OpenTelemetry](https://opentelemetry.io/) ipari szabványként jelent meg az LLM megfigyelhetőségében. API-kat, SDK-kat és eszközöket biztosít a telemetriai adatok generálására, gyűjtésére és exportálására.

Számos instrumentációs könyvtár létezik, amely meglévő agent keretrendszereket csomagol be, és megkönnyíti az OpenTelemetry span-ek exportálását megfigyelhetőségi eszközökbe. A Microsoft Agent Framework natívan integrálja az OpenTelemetry-t. Lentebb egy példa MAF ügynök instrumentálására:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Az ügynök végrehajtása automatikusan követve van
    pass
```

A fejezet [példa jegyzetkönyve](./code_samples/10-expense_claim-demo.ipynb) bemutatja, hogyan instrumentálhatja MAF ügynökét.

**Manuális Span létrehozás:** Az instrumentációs könyvtárak jó kiindulási alapot nyújtanak, de vannak esetek, amikor részletesebb vagy egyedi információkra van szükség. Manuálisan is létrehozhat span-eket az egyedi alkalmazáslogika hozzáadásához. Még fontosabb, hogy gazdagíthatja az automatikusan vagy manuálisan létrehozott span-eket egyedi attribútumokkal (más néven címkék vagy metaadatok). Ezek az attribútumok tartalmazhatnak üzleti szempontból releváns adatokat, köztes számításokat vagy bármilyen kontextust, ami hasznos lehet hibakereséshez vagy elemzéshez, mint például `user_id`, `session_id` vagy `model_version`.

Példa trace-ek és span-ek kézi létrehozására a [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3) segítségével:

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Ügynök értékelése

A megfigyelhetőség metrikákat ad, de az értékelés az az eljárás, amikor azokat az adatokat (és teszteket) elemezzük, hogy megállapítsuk, hogyan teljesít az AI ügynök és hogyan lehetne javítani. Más szóval, ha már rendelkezik trace-ekkel és metrikákkal, hogyan használja ezeket az ügynök megítéléséhez és döntések meghozatalához?

A rendszeres értékelés fontos, mert az AI ügynökök gyakran nem determinisztikusak és fejlődhetnek (frissítések vagy modell viselkedés elcsúszása révén) – értékelés nélkül nem tudná meg, hogy az „okos ügynök” ténylegesen jól végzi-e a munkáját vagy visszaesett.

Két értékelési kategória létezik AI ügynökök számára: **online értékelés** és **offline értékelés**. Mindkettő értékes és kiegészíti egymást. Általában offline értékeléssel kezdünk, mivel ez a minimális szükséges lépés bármely ügynök élesbe helyezése előtt.

### Offline értékelés

![Adathalmaz elemek a Langfuse-ban](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Ez az ügynök ellenőrzött környezetben való értékelését jelenti, tipikusan teszt adathalmazok felhasználásával, nem élő felhasználói lekérdezéseken. Kurált adathalmazokat használ, ahol tudja, mi a várható kimenet vagy helyes viselkedés, és ezeken futtatja az ügynököt.

Például, ha egy matematikai szöveges feladatokat megoldó ügynököt épített, lehet, hogy van egy [teszt adathalmaza](https://huggingface.co/datasets/gsm8k) 100 ismert megoldású problémával. Az offline értékelést gyakran fejlesztés közben végzik (például CI/CD pipeline részeként), hogy ellenőrizzék a fejlesztéseket vagy megakadályozzák a regressziókat. Az előnye, hogy **ismételhető, és egyértelmű pontossági metrikákat kaphat, hiszen rendelkezik valós igazsággal**. Szimulálhat felhasználói lekérdezéseket és mérheti az ügynök válaszait ideális válaszokkal vagy automatikus metrikiákkal, amint azt fentebb ismertettük.

Az offline értékelés kulcsfontosságú kihívása, hogy biztosítani kell az adathalmaz teljességét és relevanciáját – az ügynök jól szerepelhet egy fix tesztkészleten, de az éles környezetben nagyon eltérő lekérdezésekkel találkozhat. Ezért frissen kell tartania a teszt készleteket új szélsőséges esetekkel és példákkal, amelyek a valós szituációkat tükrözik. Hasznos egy kis „füstteszt” és nagyobb értékelő készlet keveréke: a kis készletek gyors ellenőrzésekhez, a nagyobbak szélesebb körű teljesítmény méréshez.

### Online értékelés

![Megfigyelhetőségi metrikák áttekintése](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Ez az ügynök élő, valós környezetben történő értékelését jelenti, azaz az éles használat közben. Az online értékelés magában foglalja az ügynök teljesítményének nyomon követését valós felhasználói interakciókon, és az eredmények folyamatos elemzését.

Például nyomon követheti a sikerességi arányokat, felhasználói elégedettségi pontszámokat vagy más metrikákat élő forgalomban. Az online értékelés előnye, hogy **észleli azokat a dolgokat, amiket laboratóriumi környezetben nem lehet előre látni** – figyelheti a modell elcsúszását idővel (ha az ügynök hatékonysága romlik, ahogy az input minták változnak), illetve felfedezhet váratlan lekérdezéseket vagy helyzeteket, amelyek nem szerepeltek korábbi tesztadatokban. Ez valós képet ad az ügynök viselkedéséről a valóságban.

Az online értékelés gyakran magába foglalja a felhasználói visszajelzések implicit és explicit gyűjtését, valamint árnyék tesztek vagy A/B tesztek futtatását (amikor az ügynök új verziója párhuzamosan fut, hogy összehasonlítsa a régivel). A kihívás, hogy nehéz megbízható címkéket vagy pontszámokat kapni valódi interakciókra – gyakran a felhasználói visszajelzésekre vagy az utólagos metrikákra (pl., kattintott-e a felhasználó az eredményre) kell támaszkodni.

### Kombinálva

Az online és offline értékelések nem kizárják egymást; nagyon jól kiegészítik egymást. Az online monitorozásból származó felismerések (pl. új típusú felhasználói lekérdezések, amelyekben az ügynök gyengén teljesít) felhasználhatók az offline teszt adathalmazok bővítésére és javítására. Fordítva, az offline teszteken jól teljesítő ügynököket magabiztosabban telepítheti és monitorozhatja online.

Sok csapat gyakorlatában ez egy ciklussá válik:

_offline értékelés -> telepítés -> online monitorozás -> új hibás esetek gyűjtése -> offline adatokhoz adás -> ügynök finomítása -> ismétlés_.

## Gyakori problémák

AI ügynökök élesbe állítása során számos kihívással találkozhat. Íme néhány gyakori probléma és lehetséges megoldásuk:

| **Probléma**    | **Lehetséges megoldás**   |
| ------------- | ------------------ |
| Az AI ügynök nem hajtja végre következetesen a feladatokat | - Finomítsa az AI ügynöknek adott promptot; legyen világos a cél.<br>- Határozza meg, hol lehet a feladatokat alfeladatokra bontani és több ügynökkel megoldani. |
| Az AI ügynök folyamatos hurkokba kerül  | - Biztosítson világos leállási feltételeket, hogy az ügynök tudja, mikor kell befejezni a folyamatot.<br>- Összetett, érvelést és tervezést igénylő feladatokhoz használjon nagyobb modellt, amely specializált az érvelő feladatokra. |
| Az AI ügynök eszközhívásai nem működnek jól   | - Tesztelje és validálja az eszköz kimenetét az ügynök rendszeren kívül.<br>- Finomítsa az eszköz paramétereit, promptokat és elnevezéseit.  |
| Több ügynökös rendszer nem teljesít következetesen | - Finomítsa az adott promptokat minden ügynök számára, hogy azok specifikusak és eltérőek legyenek egymástól.<br>- Építsen fel egy hierarchikus rendszert egy „irányító” vagy vezérlő ügynökkel, amely eldönti, melyik ügynök a megfelelő. |

Sok ilyen problémát hatékonyabban lehet azonosítani megfelelő megfigyelhetőséggel. A fent tárgyalt trace-ek és metrikák pontosan megmutatják, hol jelentkeznek problémák az ügynök munkafolyamataiban, így a hibakeresés és az optimalizáció sokkal hatékonyabb.

## Költségek kezelése
Íme néhány stratégia az AI ügynökök éles bevezetésének költségeinek kezelésére:

**Kisebb modellek használata:** A Kis Nyelvi Modellek (SLM-ek) bizonyos ügynöki esetekben jól teljesíthetnek, és jelentősen csökkentik a költségeket. Ahogy korábban említettük, egy értékelő rendszer kiépítése, amely meghatározza és összehasonlítja a teljesítményt a nagyobb modellekkel szemben, a legjobb módja annak, hogy megértsük, mennyire jól teljesít egy SLM a saját használati esetünkben. Érdemes SLM-eket alkalmazni egyszerűbb feladatokra, mint például szándék osztályozás vagy paraméterkivonás, míg a komplexebb érveléshez nagyobb modelleket fenntartani.

**Router modell használata:** Egy hasonló stratégia a modellek és méretek sokféleségének alkalmazása. Használhatunk LLM-et/SLM-et vagy szerver nélküli függvényt, hogy a bonyolultság alapján a legmegfelelőbb modellekhez irányítsuk a kéréseket. Ez szintén csökkenti a költségeket, miközben biztosítja a teljesítményt a megfelelő feladatoknál. Például irányítsuk az egyszerűbb lekérdezéseket kisebb, gyorsabb modellekhez, és csak a drágább nagy modelleket használjuk a komplex érvelési feladatokhoz.

**Válaszok gyorsítótárazása:** Az azonosított gyakori kérések és feladatok válaszainak előzetes biztosítása az ügynöki rendszer általi feldolgozás előtt jó módja a hasonló kérések számának csökkentésére. Akár egy folyamatot is bevezethetünk, amely az alapvetőbb AI modellek segítségével megállapítja, mennyire hasonló egy kérés a gyorsítótárazott kérésekhez. Ez a stratégia jelentősen csökkentheti a költségeket a gyakran feltett kérdésekre vagy gyakori munkafolyamatokra.

## Nézzük meg, hogyan működik ez a gyakorlatban

A [szakasz példafüzetében](./code_samples/10-expense_claim-demo.ipynb) olyan példákat fogunk látni, amelyek segítségével megfigyelhetjük és értékelhetjük az ügynökünket megfigyelhetőségi eszközök segítségével.


### További kérdéseid vannak az AI ügynökök éles alkalmazásáról?

Csatlakozz a [Microsoft Foundry Discordhoz](https://aka.ms/ai-agents/discord), hogy találkozz más tanulókkal, részt vehess konzultációkon, és választ kapj AI ügynökeiddel kapcsolatos kérdéseidre.

## Előző lecke

[Metakogníció tervezési minta](../09-metacognition/README.md)

## Következő lecke

[Ügynöki protokollok](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Felelősség kizárása**:
Ezt a dokumentumot az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum a saját nyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->