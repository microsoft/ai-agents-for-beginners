# Mesterséges intelligencia ügynökök a termelésben: Megfigyelhetőség és értékelés

[![Mesterséges intelligencia ügynökök a termelésben](../../../translated_images/hu/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Ahogy a mesterséges intelligencia ügynökök az kísérleti prototípusoktól a valós alkalmazásokig terjednek, egyre fontosabbá válik a viselkedésük megértése, a teljesítményük nyomon követése és a kimeneteik rendszerszerű értékelése.

## Tanulási célok

A lecke elvégzése után tudni fogja, hogyan kell / meg fogja érteni:
- Az ügynökök megfigyelhetőségének és értékelésének alapvető fogalmai
- Technikák az ügynökök teljesítményének, költségeinek és hatékonyságának javítására
- Mit és hogyan értékeljen rendszerszerűen a mesterséges intelligencia ügynökök esetében
- Hogyan kontrollálja a költségeket az AI ügynökök éles környezetbe történő bevezetésekor
- Hogyan instrumentáljon Microsoft Agent Framework-kel készült ügynököket

A cél, hogy olyan tudással vértezzük fel, amely a „fekete doboz” ügynököket átlátható, kezelhető és megbízható rendszerekké alakítja.

_**Megjegyzés:** Fontos biztonságos és megbízható AI ügynököket telepíteni. Tekintse meg a [Bizalmi AI ügynökök építése](../06-building-trustworthy-agents/README.md) leckét is._

## Nyomkövetések és szegmensek

A megfigyelhetőségi eszközök, mint például a [Langfuse](https://langfuse.com/) vagy a [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry), általában az ügynökök futását nyomkövetések és szegmensek formájában ábrázolják.

- **Nyomkövetés** az ügynök teljes feladatát jelenti a kezdetétől a végéig (például egy felhasználói lekérdezés kezelése).
- **Szegmensek** a nyomkövetés egyes lépései (például egy nyelvi modell hívása vagy adatlekérés).

![Nyomkövetési fa a Langfuse-ban](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Kép URL megtartva illusztráció céljából -->

Megfigyelhetőség nélkül egy AI ügynök olyan lehet, mint egy „fekete doboz” – a belső állapota és logikája átláthatatlan, ami megnehezíti a problémák diagnosztizálását vagy a teljesítmény optimalizálását. A megfigyelhetőséggel az ügynökök „üvegdobozokká” válnak, átláthatóságot nyújtva, amely elengedhetetlen a bizalom kiépítéséhez és annak biztosításához, hogy a tervek szerint működjenek.

## Miért fontos a megfigyelhetőség az éles környezetben

Az AI ügynökök éles környezetbe való áttelepítése új kihívásokat és elvárásokat hoz. A megfigyelhetőség már nem csak egy „jó lenne” funkció, hanem kritikus képességgé válik:

*   **Hibakeresés és okfeltáró elemzés:** Ha egy ügynök hibát jelez vagy váratlan kimenetet produkál, a megfigyelhetőségi eszközök nyomkövetései segítenek a hiba forrásának pontos meghatározásában. Ez különösen fontos összetett ügynökök esetén, amelyek több LLM hívást, eszköz-interakciókat és feltételes logikát is tartalmazhatnak.
*   **Késleltetés és költség menedzsment:** Az AI ügynökök gyakran olyan LLM-ekre és külső API-kra támaszkodnak, amelyek token vagy hívás alapú elszámolásúak. A megfigyelhetőség pontos nyomon követést tesz lehetővé ezekre a hívásokra, elősegítve a túl lassú vagy költséges műveletek felismerését. Ez lehetővé teszi a csapatok számára, hogy optimalizálják a promptokat, hatékonyabb modelleket válasszanak vagy áttervezzék a munkafolyamatokat az üzemeltetési költségek kordában tartására és a jó felhasználói élmény biztosítására.
*   **Bizalom, biztonság és megfelelőség:** Sok alkalmazás esetén fontos az ügynökök biztonságos és etikus viselkedésének garantálása. A megfigyelhetőség audit nyomvonalat biztosít az ügynökök tevékenységeiről és döntéseiről. Ezt felhasználhatja például prompt injekció, káros tartalom generálása vagy személyes adatok (PII) kezelésének hibáinak felismerésére és enyhítésére. Például megvizsgálhatja a nyomkövetéseket, hogy megértse, miért adott egy adott válasz a modell vagy miért használt egy bizonyos eszközt.
*   **Folyamatos fejlesztési ciklusok:** A megfigyelhetőségi adatok egy iteratív fejlesztési folyamat alapját képezik. Az ügynökök valós világban történő teljesítményének nyomon követésével a csapatok azonosíthatják a fejlesztendő területeket, adatokat gyűjthetnek modellek finomhangolásához és validálhatják a változtatások hatását. Ez egy visszacsatolási ciklust hoz létre, ahol az éles értékelésből származó eredmények offline kísérletekhez és finomításokhoz vezetnek, fokozatosan javítva az ügynök teljesítményét.

## Fontos mérőszámok nyomon követése

Az ügynök viselkedésének megfigyeléséhez számos mutatót és jelet célszerű követni. Bár az egyes mérőszámok változhatnak az ügynök céljától függően, néhány univerzálisan fontos.

Íme néhány a leggyakoribb mérőszámok közül, amelyeket a megfigyelhetőségi eszközök monitoroznak:

**Késleltetés:** Milyen gyorsan válaszol az ügynök? A hosszú várakozási idők negatívan befolyásolják a felhasználói élményt. Mérje a késleltetést a feladatok és az egyes lépések esetében az ügynök futásainak nyomkövetésével. Például, ha egy ügynök 20 másodpercig futtat összes modellhívást, akkor ezt gyorsabb modellel vagy párhuzamosított hívásokkal lehet felgyorsítani.

**Költségek:** Mennyibe kerül egy ügynök futtatása? Az AI ügynökök LLM hívásokra és külső API-kra támaszkodnak, amelyek token vagy hívás alapú elszámolásúak. Gyakori eszközhasználat vagy több prompt gyorsan növeli a költségeket. Például, ha egy ügynök öt alkalommal hívja meg az LLM-et a marginalis minőségjavulásért, meg kell fontolni, hogy a költség indokolt-e, vagy csökkenteni lehet-e a hívások számát, vagy olcsóbb modellt használni. A valós idejű monitorozás segíthet az váratlan kiugrások (például hibák, amelyek túlzott API-hívásokat okoznak) felismerésében is.

**Kérelmi hibák:** Hány kérelmet nem tudott teljesíteni az ügynök? Ez magában foglalhat API hibákat vagy sikertelen eszközhívásokat. Az ügynök robusztusságának növelése érdekében az éles környezetben fallback mechanizmusokat vagy ismétlődéseket állíthat be. Pl. ha az LLM szolgáltató A nem elérhető, akkor szolgáltató B-hez vált tartalékként.

**Felhasználói visszajelzés:** Közvetlen felhasználói értékelések bevezetése értékes betekintést nyújt. Ez magában foglalhat explicit értékeléseket (👍fel, 👎le, ⭐1-5 csillag) vagy szöveges megjegyzéseket. Az ismétlődő negatív visszajelzés figyelmeztető jelzés, hogy az ügynök nem a várakozások szerint működik.

**Implicit felhasználói visszajelzés:** A felhasználói viselkedések közvetett visszajelzést adnak még akkor is, ha nincs kifejezett értékelés. Ez tartalmazhat azonnali kérdésátfogalmazásokat, ismételt lekérdezéseket vagy újrapróbálkozás gomb megnyomását. Pl. ha azt tapasztalja, hogy a felhasználók ismételten ugyanazt a kérdést teszik fel, az az ügynök hibás működését jelzi.

**Pontosság:** Milyen gyakran ad az ügynök helyes vagy kívánatos kimenetet? A pontosság definíciója változó (pl. probléma-megoldás helyessége, információ-visszakeresési pontosság, felhasználói elégedettség). Az első lépés meghatározni, mit jelent az Ön ügynöke számára a siker. A pontosságot automatizált ellenőrzések, értékelési pontszámok és feladat-kész eredmények alapján nyomon követheti. Pl. nyomkövetések „sikeres” vagy „sikertelen” címkézése.

**Automatizált értékelési metrikák:** Automatizált értékeléseket is beállíthat. Például egy LLM-mel pontozhatja az ügynök kimenetét, hogy mennyire segítőkész, pontos vagy nem. Számos nyílt forráskódú könyvtár segíti különböző aspektusok pontozását. Pl. [RAGAS](https://docs.ragas.io/) RAG ügynökökhöz vagy [LLM Guard](https://llm-guard.com/) káros nyelvezet vagy prompt injekció érzékelésére.

A gyakorlatban ezen mérőszámok kombinációja adja a legjobb átfogó képet egy AI ügynök állapotáról. A fejezet [példánynaplójában](./code_samples/10-expense_claim-demo.ipynb) bemutatjuk, hogyan néznek ki ezek a mérőszámok valós példákban, de előtte elsajátítjuk egy tipikus értékelési munkafolyamatot.

## Instrumentálja az ügynököt

Nyomkövetési adatok gyűjtéséhez instrumentálni kell a kódot. A cél az, hogy az ügynök kódja olyan nyomkövetéseket és metrikákat állítson elő, amelyeket egy megfigyelhetőségi platform képes elfogadni, feldolgozni és vizualizálni.

**OpenTelemetry (OTel):** Az [OpenTelemetry](https://opentelemetry.io/) iparági szabvánnyá vált az LLM megfigyelhetőségben. API-k, SDK-k és eszközök gyűjteményét nyújtja telemetriai adatok generálásához, gyűjtéséhez és exportálásához.

Számos instrumentációs könyvtár létezik, amelyek meglévő ügynökkereteket burkolnak, megkönnyítve az OpenTelemetry szegmensek exportálását megfigyelhetőségi eszközökbe. A Microsoft Agent Framework natívan integrálja az OpenTelemetry-t. Alább egy példa MAF ügynök instrumentálására:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Az ügynök végrehajtása automatikusan követve van
    pass
```

E fejezet [példánynaplója](./code_samples/10-expense_claim-demo.ipynb) bemutatja, hogyan instrumentálhatja MAF ügynökét.

**Manuális szegmens létrehozás:** Az instrumentációs könyvtárak jó alapot nyújtanak, de gyakran előfordul, hogy részletesebb vagy egyedi információra van szükség. Manuálisan hozhat létre szegmenseket egyedi alkalmazáslogika hozzáadásához. Fontosabb, hogy manuálisan vagy automatikusan létrehozott szegmenseket egyedi attribútumokkal (más néven címkék vagy metaadatok) gazdagíthat. Ezek az attribútumok üzleti-specifikus adatokat, köztes számításokat vagy bármilyen olyan kontextust tartalmazhatnak, amely hasznos a hibakereséshez vagy elemzéshez, mint például `user_id`, `session_id` vagy `model_version`.

Példa nyomkövetések és szegmensek manuális létrehozására a [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3) segítségével:

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Ügynök értékelés

A megfigyelhetőség mérőszámokat ad, de az értékelés az a folyamat, amely elemezi ezeket az adatokat (és teszteket végez), hogy megállapítsa, mennyire teljesít jól egy AI ügynök és hogyan lehet javítani. Másképp fogalmazva, miután megvannak a nyomkövetések és mérőszámok, hogyan használja fel őket az ügynök megítélésére és döntések meghozatalára?

A rendszeres értékelés fontos, mert az AI ügynökök gyakran nem determinisztikusak és fejlődhetnek (frissítések vagy a modell viselkedésének eltolódása révén) – értékelés nélkül nem tudná, hogy az „okos ügynök” valóban jól végzi-e a munkáját, vagy visszaesett-e.

Két értékelési kategória létezik AI ügynökökhöz: **online értékelés** és **offline értékelés**. Mindkettő értékes és kiegészíti egymást. Általában offline értékeléssel kezdünk, mivel ez a minimálisan szükséges lépés egy ügynök telepítése előtt.

### Offline értékelés

![Adatkészlet elemei a Langfuse-ban](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Ez az ügynök ellenőrzött környezetben történő értékelését jelenti, jellemzően tesztadatkészletek felhasználásával, nem éles felhasználói lekérdezésekkel. Kurátori adatbázisokat használ, ahol ismert a várt kimenet vagy a helyes viselkedés, majd ezeken futtatja le az ügynököt.

Például ha egy matematikai szöveges feladatokat megoldó ügynököt épített, lehet, hogy rendelkezik egy [tesztadatkészlettel](https://huggingface.co/datasets/gsm8k), amely 100 feladatot tartalmaz ismert megoldásokkal. Az offline értékelés gyakran a fejlesztés során történik (és része lehet a CI/CD pipeline-oknak), hogy ellenőrizze a javulásokat vagy megakadályozza a regressziót. Az előnye az, hogy **ismételhető és tiszta pontossági mérőszámokat kaphat, mert van valódi alapérték**. Szimulálhat felhasználói lekérdezéseket és számíthatja az ügynök válaszait az ideális válaszokhoz viszonyítva, vagy használhat automatizált metrikákat, amint azt fentebb ismertettük.

Az offline értékelés kulcskihívása, hogy biztosítsa, hogy a tesztadatkészlete átfogó és releváns maradjon – az ügynök jól teljesíthet egy fix tesztkészleten, de az élesben nagyon eltérő kérdésekkel találkozhat. Ezért frissíteni kell a tesztkészleteket új szélsőséges esetekkel és valós helyzeteket tükröző példákkal. Hasznos egy keverék kis „füstteszt” esetekből és nagyobb értékelési készletekből: a kis készletek gyors ellenőrzésre, a nagyobbak átfogóbb teljesítménymutatókra.

### Online értékelés

![Megfigyelhetőségi mutatók áttekintése](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Ez az ügynök élő, valós környezetben történő értékelését jelenti, vagyis a tényleges használat során az éles rendszerben. Az online értékelés az ügynök valós felhasználói interakciókon való teljesítményének nyomon követését és folyamatos elemzését foglalja magában.

Például nyomon követheti a sikerességi arányokat, a felhasználói elégedettségi pontszámokat vagy más mutatókat az élő forgalomban. Az online értékelés előnye, hogy **megfogja azokat a tényezőket, amelyeket laboratóriumi körülmények között nem tudna előre látni** – megfigyelheti a modell eltolódását idővel (ha az ügynök hatékonysága csökken, ahogy a bemeneti minták változnak), és észlelhet váratlan lekérdezéseket vagy helyzeteket, amelyek nem szerepeltek a tesztadatokban. Igaz képet nyújt arról, hogyan viselkedik az ügynök a való világban.

Az online értékelés gyakran magában foglalja az implicit és explicit felhasználói visszajelzések gyűjtését, valamint esetleg árnyékteszteket vagy A/B teszteket (amikor az új ügynök verzió párhuzamosan fut az előzővel összehasonlítás céljából). Hátránya, hogy nehéz megbízható címkéket vagy pontszámokat kapni az élő interakciókhoz – gyakran a felhasználói visszajelzésekre vagy utólagos mutatókra (például rákattintott-e a felhasználó az eredményre) kell támaszkodni.

### A kettő kombinálása

Az online és offline értékelés nem zárja ki egymást; nagyon jól kiegészítik egymást. Az online megfigyelési betekintések (pl. új típusú felhasználói lekérdezések, ahol az ügynök gyengén teljesít) felhasználhatók az offline tesztadatok kiegészítésére és javítására. Ezzel szemben, az offline teszteken jól teljesítő ügynököket következetesebben lehet élesben bevezetni és monitorozni.

Sok csapat egy ciklust alkalmaz:

_offline értékelés -> telepítés -> online monitorozás -> új hibás esetek gyűjtése -> hozzáadás az offline adathalmazhoz -> ügynök finomítása -> ismétlés_.

## Gyakori problémák

Az AI ügynökök éles környezetbe történő bevezetése során többféle kihívással találkozhat. Íme néhány gyakori probléma és lehetséges megoldásuk:

| **Probléma**    | **Lehetséges megoldás**   |
| ------------- | ------------------ |
| AI ügynök nem teljesít következetesen | - Finomítsa az AI ügynöknek adott promptokat; legyen világos a célokkal.<br>- Azonosítsa, hol segíthet az alfeladatokra bontás és több ügynök használata. |
| AI ügynök folytonos hurkokba kerül  | - Biztosítsa egyértelmű befejezési feltételeket, hogy az ügynök tudja, mikor fejezze be a folyamatot.<br>- Összetett, gondolkodást és tervezést igénylő feladatokhoz használjon nagyobb, speciálisabb modellt. |
| AI ügynök eszközhívások nem megfelelőek   | - Tesztelje és validálja az eszköz kimenetét az ügynök rendszeren kívül.<br>- Finomítsa az eszköz paramétereit, promptjait és elnevezését.  |
| Többügynökös rendszer nem működik következetesen | - Finomítsa az egyes ügynököknek adott promptokat, hogy specifikusak és megkülönböztethetőek legyenek.<br>- Építsen hierarchikus rendszert, ahol egy „irányító” ügynök dönti el, melyik ügynök a megfelelő. |

Sok problémát hatékonyabban lehet felismerni megfigyelhetőség bevezetésével. A fent tárgyalt nyomkövetések és mérőszámok pontosan megmutatják, hogy az ügynök munkafolyamatában hol jelentkeznek problémák, megkönnyítve ezzel a hibakeresést és az optimalizációt.

## Költségek kezelése


Íme néhány stratégia az AI ügynökök élesbe állításának költségeinek kezelésére:

**Kisebb modellek használata:** A Kis Nyelvi Modellek (SLM-ek) bizonyos ügynöki feladatokban jól teljesíthetnek, és jelentősen csökkentik a költségeket. Ahogy korábban említettük, a teljesítmény meghatározására és a nagyobb modellekkel való összehasonlításra szolgáló értékelőrendszer kiépítése a legjobb módja annak, hogy megértsük, egy SLM milyen jól teljesít az adott használati esetben. Érdemes SLM-eket alkalmazni egyszerűbb feladatokra, például szándék osztályozásra vagy paraméterkinyerésre, míg az összetettebb érveléshez tartani a nagyobb modelleket.

**Router modell használata:** Hasonló stratégia a különféle modellek és méretek használata. Egy LLM/SLM vagy szerver nélküli függvény segítségével az összetettség alapján irányíthatók a kérések a legmegfelelőbb modellekhez. Ez segít csökkenteni a költségeket, miközben biztosítja a teljesítményt a megfelelő feladatoknál. Például egyszerű lekérdezéseket kisebb, gyorsabb modellekhez irányítunk, míg a drága nagy modelleket csak összetett érvelési feladatokra használjuk.

**Válaszok gyorsítótárazása:** A gyakori kérések és feladatok azonosítása, valamint válaszok előzetes biztosítása az ügynöki rendszer elé jó módja a hasonló kérések számának csökkentésére. Akár egy folyamatot is bevezethetünk, amely AI alapú egyszerűbb modellekkel megállapítja, mennyire hasonlít egy kérés a gyorsítótárazott kérésekre. Ez a stratégia jelentősen csökkentheti a költségeket gyakran ismételt kérdések vagy tipikus munkafolyamatok esetén.

## Nézzük meg, hogyan működik ez a gyakorlatban

Ebben a [szakasz példa jegyzetfüzetében](./code_samples/10-expense_claim-demo.ipynb) megmutatjuk, hogyan használhatjuk megfigyelő eszközöket az ügynökünk figyelésére és értékelésére.


### Van még kérdésed az AI ügynökökkel kapcsolatban az éles környezetben?

Csatlakozz a [Microsoft Foundry Discord szerveréhez](https://discord.com/invite/ATgtXmAS5D), hogy találkozz más tanulókkal, részt vegyél az irodai órákon, és megkapd AI ügynökeiddel kapcsolatos kérdéseidre a választ.

## Előző lecke

[Metakogníció tervezési minta](../09-metacognition/README.md)

## Következő lecke

[Ügynöki protokollok](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->