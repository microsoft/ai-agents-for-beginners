# AI ügynökök éles környezetben: Megfigyelhetőség és értékelés

[![AI ügynökök éles környezetben](../../../translated_images/hu/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Ahogy az AI ügynökök az kísérleti prototípusoktól a valódi alkalmazások felé haladnak, egyre fontosabbá válik viselkedésük megértése, teljesítményük figyelése és kimeneteik szisztematikus értékelése.

## Tanulási célok

A leckét elvégezve tudni fogod/érteni fogod:
- Az ügynökök megfigyelhetőségének és értékelésének alapvető fogalmait
- Technikákat az ügynökök teljesítményének, költségeinek és hatékonyságának javítására
- Mit és hogyan érdemes szisztematikusan értékelni AI ügynökeiddel kapcsolatban
- Hogyan kontrolláld a költségeket az AI ügynökök éles környezetbe való telepítésekor
- Hogyan lehet műszerelni az Microsoft Agent Frameworkkel épített ügynököket

A cél, hogy olyan tudással vértezd fel magad, amely révén „fekete doboz” ügynökeidet átlátható, kezelhető és megbízható rendszerként alakíthatod át.

_**Megjegyzés:** Fontos, hogy biztonságos és megbízható AI ügynököket telepítsünk. Nézd meg a [Megbízható AI ügynökök építése](../06-building-trustworthy-agents/README.md) leckét is._

## Nyomok és szegmensek

A megfigyelhetőségi eszközök, mint például a [Langfuse](https://langfuse.com/) vagy a [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) jellemzően az ügynök futásokat nyomok és szegmensek formájában jelenítik meg.

- **Nyom** egy teljes ügynöki feladatot jelöl a kezdetétől a végéig (például egy felhasználói lekérdezés kezelése).
- **Szegmensek** a nyomon belüli egyes lépések (például egy nyelvi modell hívása vagy adatlekérés).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Megfigyelhetőség nélkül egy AI ügynök „fekete doboznak” tűnhet – belső állapota és érvelése átláthatatlan, ami megnehezíti a hibák felderítését vagy a teljesítmény optimalizálását. A megfigyelhetőséggel az ügynökök „üveg dobozzá” válnak, átláthatóságot nyújtva, ami létfontosságú a bizalom építéséhez és a kívánt működés biztosításához.

## Miért fontos a megfigyelhetőség az éles környezetekben

Az AI ügynökök éles környezetbe helyezése új kihívásokat és követelményeket hoz. A megfigyelhetőség már nem „jó, ha van”, hanem kritikus képesség:

*   **Hibakeresés és ok-okozati elemzés**: Ha egy ügynök hibázik vagy váratlan kimenetet produkál, a megfigyelhetőségi eszközök olyan nyomokat biztosítanak, amelyek segítségével pontosan meg lehet határozni a hiba forrását. Különösen fontos ez bonyolult ügynökök esetén, amelyek több LLM hívást, eszközhasználatot és feltételes logikát foglalhatnak magukban.
*   **Válaszidő és költségkezelés**: Az AI ügynökök gyakran LLM-ekre és más külső API-kra támaszkodnak, melyeket tokenenként vagy hívásonként számolnak el. A megfigyelhetőség lehetővé teszi ezen hívások pontos nyomon követését, segít azonosítani a túl lassú vagy drága műveleteket. Ezáltal a csapatok optimalizálhatják a promptokat, hatékonyabb modelleket választhatnak vagy áttervezhetik a munkafolyamatokat az üzemeltetési költségek csökkentése és a jó felhasználói élmény biztosítása érdekében.
*   **Bizalom, biztonság és megfelelőség**: Sok alkalmazásnál alapvető fontosságú, hogy az ügynökök biztonságosan és etikusan viselkedjenek. A megfigyelhetőség audit nyomot biztosít az ügynök műveleteiről és döntéseiről. Ez felhasználható például prompt injekció, káros tartalom generálása vagy személyes adatok helytelen kezelése (PII) észlelésére és enyhítésére. Például visszanézheted a nyomokat, hogy megértsd, egy adott válasz vagy eszközhasználat miért történt.
*   **Folyamatos fejlesztési ciklusok**: A megfigyelhetőségi adatok az iteratív fejlesztési folyamat alapját képezik. A valós környezetben nyújtott teljesítmény figyelése révén a csapatok javítási területeket azonosíthatnak, adatokat gyűjthetnek modellek finomhangolásához, valamint validálhatják a változtatások hatását. Ez olyan visszacsatolási hurkot hoz létre, amelyben az online értékelésből származó éles betekintések offline kísérletezést és finomítást táplálnak, egyre jobb ügynöki teljesítményt eredményezve.

## Nyomon követendő kulcsmutatók

Az ügynök viselkedésének figyeléséhez és megértéséhez számos mutatót és jelet érdemes követni. A konkrét mutatók változhatnak az ügynök céljától függően, de vannak általánosan fontosak is.

Íme néhány a leggyakoribb, megfigyelhetőségi eszközök által követett mutatók közül:

**Válaszidő:** Milyen gyorsan válaszol az ügynök? A hosszú várakozási idők negatívan befolyásolják a felhasználói élményt. A válaszidőt érdemes mérni feladatokra és egyéni lépésekre, az ügynök futásának nyomon követésével. Például egy olyan ügynök, amely az összes modellhívásra 20 másodpercet vesz igénybe, felgyorsítható gyorsabb modellel vagy párhuzamos hívások futtatásával.

**Költségek:** Mennyibe kerül egy ügynök futtatása? Az AI ügynökök LLM hívásokra támaszkodnak, amelyeket tokenenként vagy hívásonként számláznak, illetve külső API-kra. Gyakori eszközhasználat vagy sok prompt gyorsan növelheti a költségeket. Például, ha egy ügynök ötször hív egy LLM-et egy marginális minőségjavításért, mérlegelned kell, hogy megéri-e a költség, vagy csökkentheted a hívások számát vagy olcsóbb modellt használhatsz. Az élő monitorozás szintén segíthet váratlan költséghullámokat azonosítani (például hibák okozta túlzott API hívásokat).

**Kéréshibák:** Hány kérést nem tudott teljesíteni az ügynök? Ide tartozhatnak API hibák vagy sikertelen eszközhívások. A robosztusabb ügynök érdekében érdemes fallbacks vagy újrapróbálkozások beállítása, például ha LLM szolgáltató A leállt, akkor kapcsolj át LLM szolgáltató B-re tartalékba.

**Felhasználói visszajelzés:** Közvetlen felhasználói értékelések bevezetése értékes betekintést nyújt. Ide tartozhatnak explicit értékelések (👍jóváhagyás/👎elutasítás, ⭐1-5 csillag) vagy szöveges megjegyzések. Az ismétlődő negatív visszajelzés figyelmeztető jel, hogy az ügynök nem úgy működik, ahogy kellene.

**Implicit felhasználói visszajelzés:** A felhasználói viselkedések közvetett visszajelzést is adnak explicit értékelés nélkül. Ide tartoznak az azonnali kérdés átfogalmazások, ismételt lekérdezések vagy újrapróbálkozás gomb megnyomása. Például, ha azt látod, hogy a felhasználók ismételten ugyanazt a kérdést teszik fel, az azt jelzi, hogy az ügynök nem működik jól.

**Pontosság:** Milyen gyakran ad az ügynök helyes vagy kívánatos kimenetet? A pontosság definíciója változó (pl. probléma megoldás helyessége, információkeresés pontossága, felhasználói elégedettség). Az első lépés annak meghatározása, hogy mi a siker az ügynököd számára. Nyomon követheted a pontosságot automatikus ellenőrzéseken, értékelési pontszámokon vagy feladat teljesítési címkéken keresztül. Például a nyomok megjelölése „sikeres” vagy „sikertelen” státusszal.

**Automatikus értékelési mutatók:** Automatikus értékelések is beállíthatók. Például egy LLM-et használhatsz az ügynök kimenetének pontozására, például mennyire segítőkész vagy pontos. Számos nyílt forráskódú könyvtár is létezik, melyek segítenek az ügynök különböző aspektusainak pontozásában. Például a [RAGAS](https://docs.ragas.io/) RAG ügynökökhöz vagy az [LLM Guard](https://llm-guard.com/) a káros nyelvezet vagy prompt injekció detektálására.

Gyakorlatban ezeknek a mutatóknak a kombinációja adja az AI ügynök egészségügyi állapotának legjobb lefedettségét. Ebben a fejezetben a [példa jegyzetfüzetben](./code_samples/10-expense_claim-demo.ipynb) megmutatjuk, hogyan néznek ki ezek a mutatók valós példákban, de először megtanuljuk, hogy néz ki egy tipikus értékelési munkafolyamat.

## Műszereld az ügynököt

Annak érdekében, hogy nyomkövetési adatokat gyűjts, műszerelned kell a kódodat. A cél az, hogy az ügynök kódját olyan módon szereld fel, hogy nyomokat és mutatókat generáljon, melyeket egy megfigyelhetőségi platform be tud fogadni, feldolgozni és megjeleníteni.

**OpenTelemetry (OTel):** Az [OpenTelemetry](https://opentelemetry.io/) ipari szabvánnyá vált az LLM megfigyelhetőség terén. API-k, SDK-k és eszközök gyűjteményét nyújtja a telemetriai adatok generálásához, gyűjtéséhez és exportálásához.

Sok olyan műszerelési könyvtár létezik, amely a meglévő ügynök keretrendszereket burkolja, megkönnyítve az OpenTelemetry szegmensek exportálását megfigyelhetőségi eszközbe. A Microsoft Agent Framework natív módon integrálódik az OpenTelemetry-vel. Alább egy példa MAF ügynök műszerelésére:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Az ügynök végrehajtása automatikusan követve van
    pass
```

Ebben a fejezetben a [példa jegyzetfüzet](./code_samples/10-expense_claim-demo.ipynb) bemutatja, hogyan műszereld a MAF ügynöködet.

**Kézi szegmens létrehozás:** Bár a műszerelési könyvtárak jó alapot adnak, gyakran szükség van részletesebb vagy egyedi információkra. Kézzel is létrehozhatsz szegmenseket, hogy egyedi alkalmazáslogikát adj hozzá. Fontosabb, hogy a kézzel vagy automatikusan létrehozott szegmenseket egyedi attribútumokkal (más néven címkék vagy metaadatok) gazdagíthatod. Ezek az attribútumok tartalmazhatnak üzlet-specifikus adatokat, köztes számításokat vagy bármilyen kontextust, mely a hibakereséshez vagy elemzéshez hasznos lehet, például `user_id`, `session_id`, vagy `model_version`.

Példa az eljárásra a [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3) használatával:

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Ügynök értékelés

A megfigyelhetőség mutatókat ad, de az értékelés arra szolgál, hogy ezeket az adatokat elemezve (és teszteket végezve) meghatározzuk, az AI ügynök mennyire jól teljesít és hogyan lehet javítani rajta. Más szóval, miután megvan a nyom és a mutatók, hogyan használod ezeket az ügynök megítélésére és döntések meghozatalára?

A rendszeres értékelés fontos, mert az AI ügynökök gyakran nem determinisztikusak és fejlődhetnek (frissítések vagy model viselkedési elmozdulás révén) – értékelés nélkül nem tudnád, hogy az „okos ügynököd” valóban jól végzi-e a dolgát vagy visszaesett.

Az AI ügynökök értékelésének két kategóriája van: **online értékelés** és **offline értékelés**. Mindkettő értékes és kiegészítik egymást. Általában offline értékeléssel kezdjük, mivel ez a minimum lépés az ügynök telepítése előtt.

### Offline értékelés

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Ez az ügynök kontrollált környezetben való értékelését jelenti, általában tesztadatkészletek használatával, nem élő felhasználói lekérdezésekkel. Kurált adatbázisokat használsz, ahol tudod, mi az elvárt kimenet vagy helyes viselkedés, majd lefuttatod az ügynököt ezeken.

Például ha egy matematikai szöveges feladatokat megoldó ügynököt építettél, lehet, hogy van egy [tesztadatkészleted](https://huggingface.co/datasets/gsm8k) 100 jól ismert megoldású problémával. Az offline értékelés gyakran a fejlesztés során történik (és része lehet a CI/CD folyamatoknak) a javulás ellenőrzésére vagy a visszalépések megakadályozására. Ennek az az előnye, hogy **ismételhető és tiszta pontossági mutatókat kapsz, mert van igazságalap**. Szimulálhatod a felhasználói kérdéseket és mérheted az ügynök válaszait az ideális válaszokhoz képest, vagy használhatsz automatikus mutatókat, ahogy fentebb leírtuk.

Az offline értékelés fő kihívása annak biztosítása, hogy a tesztadatkészlet átfogó és releváns maradjon – az ügynök lehet, hogy jól teljesít egy fix tesztkészleten, de éles környezetben egészen más kérdésekkel találkozik. Ezért az adatkészletet folyamatosan frissíteni kell új szélső esetekkel és olyan példákkal, amelyek a valós helyzeteket tükrözik. Hasznos egy kis „gyors teszt” készlet és a nagyobb értékelő készletek kombinációja: a kis készletek gyors ellenőrzésekhez, a nagyobbak szélesebb körű teljesítménymutatókhoz.

### Online értékelés

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Ez az ügynök élő, valós környezetben történő értékelését jelenti, azaz az éles használat alatt. Az online értékelés folyamatosan figyeli az ügynök teljesítményét valós felhasználói interakciók alapján, és elemzi az eredményeket.

Például követheted a sikerarányokat, felhasználói elégedettségi pontszámokat vagy más mutatókat élő forgalomban. Az online értékelés előnye, hogy **megragadja azokat a dolgokat, amelyeket a laboratóriumi környezetben nem feltétlenül várnál** – megfigyelheted az idővel bekövetkező modell eltolódást (ha az ügynök hatékonysága romlik az input minták változása miatt) és észreveheted az váratlan lekérdezéseket vagy helyzeteket, amelyek nem voltak jelen a tesztadatban. Ez valós képet ad az ügynök viselkedéséről a terepen.

Az online értékelés gyakran magában foglalja a közvetett és közvetlen felhasználói visszajelzések gyűjtését, valamint árnyéktesztek vagy A/B tesztek futtatását (ahol az ügynök új verziója párhuzamosan fut a régi verzióval összehasonlítás céljából). Az kihívás az, hogy megbízható címkék vagy pontszámok beszerzése az élő interakciókhoz nehéz lehet – támaszkodhatsz a felhasználói visszajelzésekre vagy a további mutatókra (például hogy a felhasználó rákattintott-e az eredményre).

### A kettő kombinálása

Az online és offline értékelések nem zárják ki egymást; nagyon kiegészítik egymást. Az online monitorozásból származó betekintések (pl. új típusú felhasználói kérdések, ahol az ügynök rosszul teljesít) felhasználhatók az offline tesztadatok bővítésére és javítására. Ezzel szemben az offline teszteken jól teljesítő ügynököket bátrabban lehet élesíteni és online figyelni.

Valójában sok csapat egy ciklust alkalmaz:

_offline értékelés -> telepítés -> online monitorozás -> új hibás esetek gyűjtése -> hozzáadás az offline adatbázishoz -> ügynök finomítása -> ismétlés_.

## Gyakori problémák

AI ügynökök élesítésénél különféle kihívásokkal találkozhatsz. Íme néhány gyakori probléma és lehetséges megoldásuk:

| **Probléma**    | **Lehetséges megoldás**   |
| ------------- | ------------------ |
| Az AI ügynök nem végzi következetesen a feladatokat | - Finomítsd az AI ügynök számára adott promptot; legyél egyértelmű a célokkal.<br>- Azonosítsd, hol lehet a feladatokat alküldetésekre bontani és több ügynökre bízni. |
| Az AI ügynök ismétlődő hurkokba kerül | - Biztosíts egyértelmű leállítási feltételeket, hogy az ügynök tudja, mikor kell leállítani a folyamatot.<br>- Összetettebb, érvelést és tervezést igénylő feladatokhoz használj nagyobb, erre specializált modellt. |
| Az AI ügynök eszközhívásai nem működnek jól | - Teszteld és érvényesítsd az eszköz kimenetét az ügynök rendszerén kívül.<br>- Finomítsd az eszközök paramétereit, promptjait és elnevezéseit.  |
| Többügynökös rendszer nem működik következetesen | - Finomítsd azon ügynökök promptjait, hogy azok specifikusak és jól elkülönüljenek egymástól.<br>- Építs fel egy hierarchikus rendszert „irányító” vagy kontroller ügynökkel, amely meghatározza, melyik ügynök a megfelelő. |

Sok ilyen problémát hatékonyabban lehet azonosítani megfigyelhetőség alkalmazásával. A korábban említett nyomok és mutatók segítenek pontosan behatárolni, hogy az ügynök munkafolyamatában hol fordulnak elő gondok, így a hibakeresés és optimalizálás sokkal eredményesebb.

## Költségek kezelése


Íme néhány stratégia az AI ügynökök élesbe állítási költségeinek kezelésére:

**Kisebb modellek használata:** A kis nyelvi modellek (Small Language Models, SLM-k) bizonyos ügynöki alkalmazásokban jól teljesíthetnek, és jelentősen csökkentik a költségeket. Ahogy korábban említettük, a teljesítmény értékelésére és a nagyobb modellekkel való összehasonlításra szolgáló rendszer kiépítése a legjobb módja annak, hogy megértsük, egy SLM mennyire lesz hatékony az adott használati esetben. Érdemes SLM-eket használni egyszerűbb feladatokra, például szándék osztályozásra vagy paraméterkinyerésre, míg az összetettebb következtetésekhez tartalékolhatjuk a nagyobb modelleket.

**Útválasztó modell használata:** Egy hasonló stratégia, hogy különféle modelleket és méreteket alkalmazunk. Használhatunk LLM-et/SLM-et vagy szerver nélküli funkciót arra, hogy a bonyolultság alapján irányítsuk a kéréseket a legmegfelelőbb modellekhez. Ez szintén segít csökkenteni a költségeket, miközben biztosítja a teljesítményt a megfelelő feladatokhoz. Például az egyszerű lekérdezéseket irányítsuk kisebb, gyorsabb modellekhez, és csak a drága nagy modelleket használjuk összetett következtetésekhez.

**Válaszok gyorsítótárazása:** Gyakori kérések és feladatok azonosítása, valamint a válaszok előzetes biztosítása az ügynöki rendszer előtt jó módszer a hasonló kérések számának csökkentésére. Akár egy olyan folyamatot is kialakíthatunk, amely egy egyszerűbb AI modell segítségével megállapítja, mennyire hasonló egy kérés a gyorsítótárazott kérésekhez. Ez a stratégia jelentősen csökkentheti a költségeket gyakran feltett kérdések vagy gyakori munkafolyamatok esetén.

## Nézzük, hogyan működik ez a gyakorlatban

Ebben a [szakasz példafüzetében](./code_samples/10-expense_claim-demo.ipynb) példákat látunk arra, hogyan használhatunk megfigyelhetőségi eszközöket az ügynökünk monitorozására és értékelésére.


### További kérdéseid vannak az AI ügynökökről éles környezetben?

Csatlakozz a [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) közösséghez, hogy találkozz más tanulókkal, részt vegyél konzultációs órákon, és választ kapj az AI ügynökökkel kapcsolatos kérdéseidre.

## Előző lecké

[Metakogníciós tervezési minta](../09-metacognition/README.md)

## Következő lecké

[Ügynöki protokollok](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->