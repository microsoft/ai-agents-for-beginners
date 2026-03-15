# AI ügynökök élesben: Megfigyelhetőség és értékelés

[![AI ügynökök élesben](../../../translated_images/hu/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Ahogy az AI ügynökök az kísérleti prototípusoktól az éles felhasználások felé haladnak, fontossá válik viselkedésük megértése, teljesítményük monitorozása és kimeneteik rendszeres értékelése.

## Tanulási célok

A lecke elvégzése után tudni fogod/megérted:
- Az ügynökök megfigyelhetőségének és értékelésének alapvető fogalmait
- Módszereket az ügynökök teljesítményének, költségeinek és hatékonyságának javítására
- Mit és hogyan értékelj rendszeresen AI ügynökeiddel kapcsolatban
- Hogyan kontrolld a költségeket AI ügynökök éles üzembe helyezésekor
- Hogyan instrumentáld a Microsoft Agent Framework-kel épített ügynököket

A cél, hogy olyan tudással ruházzunk fel, amivel „fekete doboz” ügynökeidet átlátható, kezelhető és megbízható rendszerré alakíthatod.

_**Megjegyzés:** Fontos, hogy biztonságos és megbízható AI ügynököket helyezzünk üzembe. Nézd meg a [Megbízható AI ügynökök építése](./06-building-trustworthy-agents/README.md) leckét is._

## Tracerek és spanok

A [Langfuse](https://langfuse.com/) vagy a [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) megfigyelési eszközök általában az ügynök futásokat tracerként és spanokként ábrázolják.

- **Trace (tracer):** egy teljes ügynök-feladatot reprezentál a kezdetétől a végéig (például egy felhasználói lekérdezés kezelése).
- **Spanok:** a tracerben lévő egyedi lépések (például egy nyelvi modell hívása vagy adatlekérés).

![Tracer fa a Langfuse-ban](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Kép URL megtartva bemutatási céllal -->

Megfigyelhetőség nélkül egy AI ügynök olyan lehet, mint egy „fekete doboz” – belső állapota és következtetései áttetszőek, így nehéz hibákat diagnosztizálni vagy optimalizálni a teljesítményt. Megfigyelhetőséggel az ügynökök „üveg dobozokká” válnak, és átláthatóságot nyújtanak, ami elengedhetetlen a bizalom kiépítéséhez és hogy a kívánt módon működjenek.

## Miért fontos a megfigyelhetőség éles környezetben?

Az AI ügynökök éles környezetbe helyezése új kihívásokat és követelményeket hoz. A megfigyelhetőség már nem „csak jó lenne”, hanem kritikus képesség:

*   **Hibakeresés és okfeltárás:** Ha az ügynök hibázik vagy váratlan eredményt produkál, a megfigyelési eszközökből származó tracer segít a hiba forrásának pontos meghatározásában. Különösen fontos ez bonyolult ügynökök esetén, amelyek több LLM hívást, eszközhasználatot és feltételes logikát foglalnak magukban.
*   **Várakozási idő és költségmenedzsment:** Az AI ügynökök gyakran LLM-ekre és egyéb külső API-kra támaszkodnak, amelyeket token vagy hívás alapján számláznak. A megfigyelhetőség lehetővé teszi ezek pontos nyomon követését, így azonosíthatók a túl lassú vagy költséges műveletek. Ez segíti a csapatokat abban, hogy optimálják a promptokat, hatékonyabb modelleket válasszanak, vagy áttervezzék a munkafolyamatokat a működési költségek és a felhasználói élmény javítása érdekében.
*   **Bizalom, biztonság és megfelelés:** Sok alkalmazásban fontos, hogy az ügynökök biztonságosan és etikusan viselkedjenek. A megfigyelhetőség auditálási nyomvonalat biztosít az ügynök akcióiról és döntéseiről. Ez használható prompt injekció, káros tartalom generálása vagy személyes azonosító információk (PII) helytelen kezelése észlelésére és enyhítésére. Például felülvizsgálhatod a tracer adatokat, hogy megértsd, miért adott az ügynök egy adott választ vagy miért használt egy adott eszközt.
*   **Folyamatos fejlesztési ciklusok:** A megfigyelési adatok az iteratív fejlesztési folyamat alapjai. Az ügynökök valós idejű teljesítményének monitorozásával a csapatok javítási lehetőségeket azonosíthatnak, adatokat gyűjthetnek modellek finomhangolásához, és validálhatják a változtatások hatását. Ez egy visszacsatolási ciklust hoz létre, ahol az éles környezetből származó online értékelési adatok kiegészítik az offline kísérletezést és finomítást, ezáltal fokozatosan jobb teljesítmény érhető el.

## Követendő kulcsmutatók

Az ügynök viselkedésének megértése és nyomon követése érdekében többféle metrikát és jelzést kell követni. Bár a konkrét mutatók az ügynök céljától függően eltérhetnek, néhány univerzális fontosságú.

Íme a leggyakoribb metrikák, amelyeket a megfigyelési eszközök monitoroznak:

**Válaszidő:** Milyen gyorsan reagál az ügynök? A hosszú várakozások rossz hatással vannak a felhasználói élményre. Mérned kell a feladatokra és egyes lépésekre vonatkozó késleltetést az ügynök futások tracerjei alapján. Például, ha egy ügynök 20 másodperc alatt végzi el az összes modellhívást, érdemes gyorsabb modellt használni vagy párhuzamos hívásokat végezni.

**Költségek:** Mennyibe kerül egy ügynök futás? Az AI ügynökök LLM hívásokra támaszkodnak, amelyeket token vagy hívás alapján számolnak fel, illetve külső API-kra. Gyakori eszközhasználat vagy többszöri prompt gyorsan megdobhatja a költségeket. Például, ha egy ügynök öt alkalommal hív egy LLM-et csak minimális minőségjavulás érdekében, mérlegelni kell, megéri-e a költség vagy csökkenteni lehet a hívások számát, vagy olcsóbb modellt használni. A valós idejű monitorozás segít felismerni a váratlan költségnövekedéseket (például hibák miatti túlzott API hívások).

**Hibás kérések:** Hányszor nem sikerült az ügynök kérése? Ide tartozhatnak API hibák vagy sikertelen eszközhívások. Az ilyen hibák ellen az ügynök robosztusabbá tétele érdekében felállíthatók visszaesések vagy újrapróbálkozások. Pl. ha az LLM szolgáltató A elérhetetlenné válik, zárolhatsz egy tartalék LLM szolgáltató B-t.

**Felhasználói visszajelzés:** Közvetlen felhasználói értékelések értékes információkat adnak. Ez magában foglalhat kifejezett értékeléseket (👍fel, 👎le, ⭐1-5 csillag) vagy szöveges megjegyzéseket. Állandóan negatív visszajelzés azt jelzi, hogy az ügynök nem működik megfelelően.

**Implicit felhasználói visszajelzés:** A felhasználók viselkedése közvetett visszacsatolást nyújt anélkül, hogy explicit értékelést adna. Ilyen lehet a kérdés azonnali átfogalmazása, ismételt lekérdezések vagy a próbálkozás újragomb lenyomása. Például, ha azt látod, hogy a felhasználók ismételten ugyanazt a kérdést teszik fel, az arra utal, hogy az ügynök nem működik az elvárások szerint.

**Pontosság:** Milyen gyakran ad helyes vagy kívánatos válaszokat az ügynök? A pontosság definíciója eltérő lehet (pl. problémamegoldás helyessége, információkeresési pontosság, felhasználói elégedettség). Az első lépés meghatározni, mit jelent a siker az adott ügynök esetén. A pontosság követhető automatizált ellenőrzésekkel, értékelési pontszámokkal vagy feladatbefejezési címkékkel. Például a tracer-ek jelölése „sikeres” vagy „sikertelen” státusszal.

**Automatizált értékelési metrikák:** Automatizált értékeléseket is beállíthatsz. Például használhatsz LLM-et az ügynök kimenetének értékelésére, hogy mennyire hasznos vagy pontos. Számos nyílt forrású könyvtár is létezik, melyek segítségével különböző aspektusokat értékelhetsz az ügynök működésében, pl. [RAGAS](https://docs.ragas.io/) RAG ügynökökhöz vagy [LLM Guard](https://llm-guard.com/) káros nyelvezet vagy prompt injekció észlelésére.

A gyakorlatban ezeknek a mutatóknak a kombinációja adja a legteljesebb képet egy AI ügynök állapotáról. Ebben a fejezetben a [példafüzetben](./code_samples/10-expense_claim-demo.ipynb) megmutatjuk, hogyan néznek ki ezek a mutatók valós példákon, de előbb tanuljuk meg, milyen egy tipikus értékelési munkafolyamat.

## Instrumentáld az ügynököd

A tracer adatok gyűjtéséhez instrumentálni kell a kódot. A cél az, hogy az ügynök kódját úgy instrumentáld, hogy tracer adatokat és metrikákat adjon ki, amelyeket megfigyelési platform képes rögzíteni, feldolgozni és vizualizálni.

**OpenTelemetry (OTel):** Az [OpenTelemetry](https://opentelemetry.io/) iparági szabványként alakult ki az LLM megfigyelhetőséghez. API-k, SDK-k és eszközök összességét kínálja a telemetriai adatok generálásához, gyűjtéséhez és exportálásához.

Számos instrumentációs könyvtár létezik, amelyek becsomagolják a meglévő ügynök keretrendszereket és megkönnyítik az OpenTelemetry spanok exportját megfigyelési eszközbe. A Microsoft Agent Framework natívan integrálva van az OpenTelemetry-vel. Az alábbi példa egy MAF ügynök instrumentálását mutatja be:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Az ügynök végrehajtása automatikusan nyomon követett
    pass
```

Ebben a fejezetben az [példafüzetben](./code_samples/10-expense_claim-demo.ipynb) bemutatjuk, hogyan instrumentálható egy MAF ügynök.

**Span-ok kézi létrehozása:** Bár az instrumentációs könyvtárak jó alapot szolgáltatnak, gyakran szükség van részletesebb vagy testreszabott információkra. Lehetőség van span-ok kézi létrehozására, hogy egyedi alkalmazáslogikát adj hozzá. Fontosabb, hogy ezek gazdagíthatják az automatikusan vagy kézzel létrehozott spanokat egyedi attribútumokkal (más néven címkék vagy metaadatok). Ezek az attribútumok tartalmazhatnak üzleti adatokat, köztes számításokat vagy bármilyen, hibakereséshez vagy elemzéshez hasznos kontextust, például `user_id`, `session_id` vagy `model_version`.

Példa tracer és span kézi létrehozására a [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3) használatával:

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Ügynök értékelés

A megfigyelhetőség metrikákat nyújt, de az értékelés az az eljárás, amikor az adatokat elemzed (és teszteket végzel) annak megállapítására, hogy az AI ügynök mennyire teljesít jól és hogyan lehet javítani rajta. Más szóval, miután megvannak a trace-ek és metrikák, hogyan használod azokat az ügynök megítélésére és döntések meghozatalára?

A rendszeres értékelés fontos, mert az AI ügynökök gyakran nem determinisztikusak és fejlődhetnek (frissítések vagy a modell viselkedésének elcsúszása miatt) – értékelés nélkül nem tudnád, hogy az „okos ügynököd” valóban jól végzi-e a feladatát vagy romlott.

Két értékelési kategória létezik AI ügynökök esetén: **online értékelés** és **offline értékelés**. Mindkettő értékes és kiegészítik egymást. Általában offline értékeléssel kezdünk, mert ez az alapvető lépés bármely ügynök élesítés előtt.

### Offline értékelés

![Adatkészlet elemek a Langfuse-ban](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Ez az értékelési módszer kontrollált környezetben zajlik, jellemzően tesztadatkészletek használatával, nem élő felhasználói lekérdezésekkel. Olyan válogatott adatkészleteket használsz, ahol ismert a várt kimenet vagy helyes viselkedés, majd ezeken futtatod le az ügynököt.

Például ha egy matematikai szöveges feladat megoldó ügynököt építettél, lehet egy [teszt adatkészleted](https://huggingface.co/datasets/gsm8k) 100 problémával ismert válaszokkal. Az offline értékelést fejlesztés alatt végezheted (és CI/CD folyamat része lehet), hogy javításokat ellenőrizz vagy regressziót kizárj. Az előnye, hogy **ismételhető és tiszta pontossági mutatókat kapsz, mert ismert az igazság**. Szimulálhatod a felhasználói lekérdezéseket, és mérheted az ügynök válaszait az ideális válaszok ellen, vagy használhatsz a fent említett automatizált metrikákat.

Az offline értékelés kulcskihívása, hogy az adatkészlet átfogó és releváns maradjon – az ügynök jól teljesíthet egy rögzített adatkészleten, de élesben nagyon eltérő lekérdezésekkel találkozhat. Ezért fontos folyamatosan frissíteni a tesztkészleteket új, szélsőséges esetekkel és valós szcenáriókat tükröző példákkal. Hasznos keverni a kis „füstteszt” eseteket gyors ellenőrzéshez és nagyobb értékelési készleteket átfogó teljesítmény mérésére.

### Online értékelés

![Megfigyelési metrikák áttekintése](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Az ügynök élő, valós környezetben történő értékelése, vagyis az éles használat során. Online értékeléskor folyamatosan monitorozod az ügynök teljesítményét valós felhasználói interakciókon, és elemzed az eredményeket.

Például nyomon követheted a sikerességi arányt, ügyfél-elégedettségi pontszámokat vagy egyéb metrikákat az élő forgalomban. Az online értékelés előnye, hogy **azokat a problémákat is feltárja, amikre a laborban nem számítanál** – megfigyelhető a modell elcsúszása idővel (ha az ügynök hatékonysága csökken az input minták változásával) és felfedezhetők váratlan lekérdezések vagy helyzetek, melyek nem szerepeltek a tesztadatban. Valódi képet ad arról, hogyan viselkedik az ügynök a való világban.

Az online értékelésbe beletartozik a felhasználói visszajelzések begyűjtése, implicit és explicit módon, illetve árnyéktesztek vagy A/B tesztek futtatása (amikor az ügynök új verziója párhuzamosan fut a régivel összehasonlítás céljából). A kihívás, hogy élő interakciókhoz nehéz megbízható címkéket vagy pontszámokat szerezni – ilyenkor felhasználói visszajelzésre vagy downstream metrikákra támaszkodhatsz (például, hogy a felhasználó rákattintott-e az eredményre).

### Az értékelések kombinálása

Az online és offline értékelések nem zárják ki egymást; nagyon jól kiegészítik egymást. Az online monitorozásból származó észrevételek (például új típusú gyengén teljesítő lekérdezések) felhasználhatók az offline tesztadatkészletek bővítésére és javítására. Fordítva, az offline teszteken jól teljesítő ügynökök magabiztosabban helyezhetők élesbe és monitorozhatók online.

Sok csapat egy ciklust követ:

_offline értékelés -> élesítés -> online monitorozás -> új hibás esetek gyűjtése -> offline adatbázis bővítése -> ügynök finomhangolása -> ismétlés_.

## Gyakori problémák

AI ügynökök élesbe helyezésekor különféle kihívásokkal szembesülhetsz. Íme néhány gyakori probléma és a lehetséges megoldások:

| **Probléma**    | **Lehetséges megoldás**   |
| ------------- | ------------------ |
| AI ügynök nem végzi következetesen a feladatokat | - Finomítsd az AI ügynöknek adott promptokat; légy világos a célokban.<br>- Azonosítsd, hol lehet szétosztani a feladatokat részfeladatokra, amiket külön ügynökök kezelnek. |
| AI ügynök végtelen ciklusokba kerül | - Győződj meg róla, hogy világos leállítási feltételek vannak, hogy az ügynök tudja, mikor hagyja abba a folyamatot.<br>- Összetett feladatok esetén, melyek következtetést és tervezést igényelnek, használj nagyobb, erre a feladatra specializált modellt. |
| AI ügynök eszközhívások nem működnek jól | - Teszteld és validáld az eszköz kimenetét az ügynök rendszeren kívül.<br>- Finomítsd az eszköz paramétereit, promptjait és elnevezéseit.  |
| Több ügynökös rendszer nem működik következetesen | - Finomítsd az ügynököknek adott promptokat, hogy specifikusak és elkülönültek legyenek egymástól.<br>- Építs fel egy hierarchikus rendszert "irányító" vagy vezérlő ügynökkel, amely meghatározza, melyik ügynök a megfelelő. |

Sok ilyen probléma hatékonyabban felismerhető megfigyelhetőség segítségével. Az előzőekben tárgyalt trace-ek és metrikák pontosan megmutatják, az ügynök munkafolyamatának mely pontján jelentkezik a gond, így a hibakeresés és optimalizálás sokkal gyorsabbá válik.

## Költségek kezelése
Íme néhány stratégia az AI-ügynökök éles környezetbe való telepítésének költségeinek kezelésére:

**Kisebb modellek használata:** A kis nyelvi modellek (SLM-ek) bizonyos ügynöki felhasználási esetekben jól teljesíthetnek, és jelentősen csökkentik a költségeket. Ahogy korábban említettük, a teljesítmény nagyméretű modellekkel való összehasonlítására és meghatározására szolgáló értékelő rendszer kiépítése a legjobb módja annak, hogy megértsük, egy SLM mennyire lesz alkalmas az adott feladatra. Fontolja meg az SLM-ek alkalmazását egyszerűbb feladatokra, például szándékos osztályozásra vagy paraméterkivonásra, míg a nagyobb modelleket bonyolultabb következtetésekhez tartsa fenn.

**Router modell használata:** Egy hasonló stratégia a modellek és méretek diverzitásának alkalmazása. Használhat LLM/SLM-et vagy szerver nélküli funkciót a kérések összetettség szerinti irányítására a legmegfelelőbb modellekhez. Ez szintén segít csökkenteni a költségeket, miközben biztosítja a teljesítményt a megfelelő feladatoknál. Például egyszerű kérdéseket irányítson kisebb, gyorsabb modellekhez, és csak a drága nagy modelleket használja összetett érvelési feladatokra.

**Válaszok gyorsítótárazása:** Gyakori kérések és feladatok azonosítása, majd az azokhoz tartozó válaszok szolgáltatása még az ügynök rendszerébe jutás előtt jó módszer a hasonló kérések mennyiségének csökkentésére. Akár egy olyan folyamatot is kialakíthat, amely alapvetőbb AI modelleket használva felismeri, hogy egy kérés mennyire hasonlít a gyorsítótárazott kérésekhez. Ez a stratégia jelentősen csökkentheti a költségeket gyakran feltett kérdések vagy gyakori munkafolyamatok esetén.

## Nézzük meg, hogyan működik ez a gyakorlatban

A [szakasz példafüzetében](./code_samples/10-expense_claim-demo.ipynb) példákat látunk arra, hogyan használhatjuk megfigyelhetőségi eszközöket ügynökünk monitorozására és értékelésére.


### További kérdései vannak az AI-ügynökök éles használatával kapcsolatban?

Csatlakozzon a [Microsoft Foundry Discordhoz](https://aka.ms/ai-agents/discord), hogy találkozhasson más tanulókkal, részt vehessen tanácsadói órákon, és választ kaphasson AI-ügynökökkel kapcsolatos kérdéseire.

## Előző lecke

[Metakogníció tervezési minta](../09-metacognition/README.md)

## Következő lecke

[Ügynöki protokollok](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Nyilatkozat**:
Ezt a dokumentumot az AI fordító szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti, anyanyelvi dokumentum tekintendő hiteles forrásnak. Kritikus információk esetén szakember által végzett emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->