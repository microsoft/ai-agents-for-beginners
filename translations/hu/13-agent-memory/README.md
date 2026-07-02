# Memória az AI ügynökök számára 
[![Agent Memory](../../../translated_images/hu/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Az AI ügynökök egyedi előnyeiről beszélve főként két dolog kerül szóba: a feladatok elvégzéséhez szükséges eszközök hívásának képessége és a folyamatos fejlődés képessége. A memória az önfejlesztő ügynökök létrehozásának alapja, amely jobb élményeket tud nyújtani a felhasználóink számára.

Ebben a leckében megnézzük, hogy mi a memória az AI ügynökök számára, és hogyan tudjuk kezelni és felhasználni azt alkalmazásaink előnyére.

## Bevezetés

Ez a lecke a következőket fedi le:

• **Az AI ügynök memória megértése**: Mi a memória és miért létfontosságú az ügynökök számára.

• **Memória megvalósítása és tárolása**: Gyakorlati módszerek a memória képességek hozzáadására AI ügynökeidhez, a rövid- és hosszú távú memóriára fókuszálva.

• **AI ügynökök önfejlesztése**: Hogyan teszi lehetővé a memória az ügynökök számára, hogy korábbi interakciókból tanuljanak és idővel fejlődjenek.

## Elérhető megvalósítások

Ez a lecke két átfogó jegyzetfüzetes bemutatót tartalmaz:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Mem0 és Azure AI Search használatával valósít meg memóriát a Microsoft Agent Framework segítségével

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Strukturált memóriát valósít meg Cognee segítségével, automatikusan építve beágyazásokkal alátámasztott tudásgráfot, megjelenítve a gráfot és intelligens visszakeresést biztosítva

## Tanulási célok

A lecke elvégzése után tudni fogod, hogyan:

• **Megkülönböztesd az AI ügynök memória különböző típusait**, beleértve a munkamemóriát, rövid távú és hosszú távú memóriát, valamint a speciális formákat, mint a személyiség- és epizodikus memória.

• **Megvalósítsd és kezeld a rövid- és hosszú távú memóriát AI ügynököknek** a Microsoft Agent Framework használatával, kihasználva olyan eszközöket, mint a Mem0, Cognee, Whiteboard memória, és integrálva az Azure AI Search-t.

• **Megértsd az önfejlesztő AI ügynökök alapelveit**, és azt, hogyan járulnak hozzá a robosztus memória-kezelési rendszerek a folyamatos tanuláshoz és alkalmazkodáshoz.

## Az AI ügynök memória megértése

Alapvetően az **AI ügynökök memóriája azok a mechanizmusok, amelyek lehetővé teszik számukra az információ megtartását és előhívását**. Ezek az információk lehetnek specifikus részletek egy beszélgetésről, felhasználói preferenciák, korábbi műveletek vagy akár tanult minták.

Memória nélkül az AI alkalmazások gyakran állapot nélkülinek tekintendők, ami azt jelenti, hogy minden interakció újrakezdődik. Ez ismétlődő és frusztráló felhasználói élményhez vezet, ahol az ügynök "elfelejti" az előző kontextust vagy preferenciákat.

### Miért fontos a memória?

Egy ügynök intelligenciája mélyen összefügg azzal a képességgel, hogy előhívja és felhasználja a múltbéli információkat. A memória lehetővé teszi az ügynökök számára, hogy:

• **Reflektív legyen**: Tanuljon a múltbeli cselekvésekből és eredményekből.

• **Interaktív legyen**: Fenntartsa a kontextust egy folyamatban lévő beszélgetés alatt.

• **Proaktív és reaktív legyen**: Megjósolja a szükségleteket vagy megfelelően reagál a történelmi adatok alapján.

• **Autonóm legyen**: Függetlenebben működjön a tárolt tudás felhasználásával.

A memória megvalósításának célja, hogy az ügynökök megbízhatóbbak és képzettebbek legyenek.

### A memória típusai

#### Munkamemória

Ezt gondold egy jegyzettömbnek, amelyet az ügynök egyetlen, folyamatban lévő feladat vagy gondolatmenet közben használ. Tartalmazza a következő lépéshez szükséges azonnali információkat.

Az AI ügynököknél a munkamemória gyakran a beszélgetés legrelevánsabb részleteit ragadja meg, akkor is, ha a teljes csetelőzési előzmény hosszú vagy levágott. A fő elemek kivonására koncentrál, mint például követelmények, javaslatok, döntések és műveletek.

**Példa munkamemóriára**

Egy utazásszervező ügynöknél a munkamemória rögzítheti a felhasználó aktuális kérését, például: "Szeretnék foglalni egy utat Párizsba". Ez a konkrét igény az ügynök közvetlen kontextusában van, irányítva a jelenlegi interakciót.

#### Rövid távú memória

Ez a memória típusa megőrzi az információkat egyetlen beszélgetés vagy munkamenet idejére. Ez az aktuális cset kontextusa, amely lehetővé teszi az ügynök számára, hogy visszautaljon a párbeszéd korábbi fordulóira.

A [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) Python SDK mintákban ez `AgentSession`-nek felel meg, amelyet `agent.create_session()`-nel hoznak létre. A munkamenet a framework beépített rövid távú memóriája: megőrzi a beszélgetés kontextusát, amíg ugyanaz a munkamenet újrahasznosul, de az adott kontextus nem marad meg, ha a munkamenet véget ér vagy az alkalmazás újraindul. Hosszú távú memóriát használj azon tények és preferenciák tárolására, amelyeknek túl kell élniük a munkameneteket, jellemzően adatbázison, vektor indexen vagy más perzisztens tárolón keresztül.

**Példa rövid távú memóriára**

Ha egy felhasználó megkérdezi, "Mennyibe kerül egy repülőjegy Párizsba?" majd folytatja "Mi a helyzet a szállással ott?", a rövid távú memória biztosítja, hogy az ügynök tudja, hogy a „ott” Párizsra utal az ugyanazon beszélgetésen belül.

#### Hosszú távú memória

Ezek olyan információk, amelyek több beszélgetésen vagy munkameneten át fennmaradnak. Lehetővé teszi az ügynökök számára, hogy megjegyezzék a felhasználói preferenciákat, történelmi interakciókat vagy általános tudást hosszabb időszakon keresztül. Ez fontos a személyre szabás szempontjából.

**Példa hosszú távú memóriára**

Egy hosszú távú memória tárolhatja, hogy „Ben szeret síelni és a szabadidős tevékenységeket, szereti a kávét hegyi kilátással, és el akarja kerülni a haladó sípályákat egy korábbi sérülés miatt”. Ez az információ, amely korábbi interakciókból származik, befolyásolja a jövőbeli utazástervezési ajánlásokat, így személyre szabottabbá téve azokat.

#### Személyiség memória

Ez a specializált memória típus segíti az ügynököt abban, hogy következetes „személyiséget” vagy „perszónát” alakítson ki. Lehetővé teszi az ügynök számára, hogy megjegyezze önmagával vagy célzott szerepével kapcsolatos részleteket, így az interakciók gördülékenyebbek és fókuszáltabbak lesznek.

**Példa személyiség memóriára**

Ha az utazási ügynök „szakértő sítervezőként” van megtervezve, a személyiség memória erősítheti ezt a szerepet, befolyásolva a válaszait, hogy azok egy szakértő hangvételéhez és tudásához igazodjanak.

#### Munkafolyamat / Epizodikus memória

Ez a memória tárolja az ügynök által egy összetett feladat során tett lépések sorrendjét, beleértve a sikereket és kudarcokat is. Olyan, mint az egyes „epizódok” vagy korábbi tapasztalatok megőrzése, hogy azokból tanuljon.

**Példa epizodikus memóriára**

Ha az ügynök megpróbált lefoglalni egy adott járatot, de az nem volt elérhető, az epizodikus memória rögzítheti ezt a sikertelenséget, lehetővé téve, hogy alternatív járatokat próbáljon vagy tájékoztassa a felhasználót az ügyről tájékozottabb módon egy későbbi próbálkozás során.

#### Entitás memória

Ez magában foglalja az adott beszélgetésekből konkrét entitások (például személyek, helyek vagy tárgyak) és események kinyerését és megjegyzését. Segít az ügynöknek strukturáltan megérteni a kulcselemeket, amelyeket tárgyaltak.

**Példa entitás memóriára**

Egy korábbi utazásról szóló beszélgetésből az ügynök kivonhatja a „Párizs”, „Eiffel-torony” és „vacsora a Le Chat Noir étteremben” entitásokat. Egy későbbi interakcióban az ügynök emlékezhet a „Le Chat Noir”-ra, és felajánlhatja, hogy új foglalást készít ott.

#### Strukturált RAG (Retrieval Augmented Generation)

Míg a RAG egy tágabb technika, a "Strukturált RAG" kiemelten hatékony memória technológiaként jelenik meg. Ez különféle forrásokból (beszélgetések, e-mailek, képek) sűrű, strukturált információkat von ki, és használja azok pontosságának, előhívásának és sebességének javítására a válaszok során. Klasszikus RAG-vel ellentétben, amely kizárólag szemantikus hasonlóságra támaszkodik, a Strukturált RAG az információk belső szerkezetét használja.

**Strukturált RAG példa**

Ahelyett, hogy csupán kulcsszavakra illesztene, a Strukturált RAG képes egy e-mailből kinyerni a járat részleteit (célállomás, dátum, idő, légitársaság) és struktúrált módon tárolni azokat. Ez lehetővé teszi pontos lekérdezéseket, például: „Milyen járatot foglaltam Párizsba kedden?”

## Memória megvalósítása és tárolása

Az AI ügynökök memóriájának megvalósítása egy rendszeres folyamatot jelent, azaz a **memóriakezelést**, amely magában foglalja az információ generálását, tárolását, visszakeresését, integrálását, frissítését és akár az„elfelejtést” (vagy törlést). A visszakeresés különösen fontos elem.

### Specializált memóriaeszközök

#### Mem0

Az ügynök memória tárolásának és kezelésének egyik módja specializált eszközök, mint a Mem0 használata. A Mem0 állandó memória rétegként működik, lehetővé téve az ügynökök számára a releváns interakciók előhívását, a felhasználói preferenciák és tényalapú kontextus tárolását, valamint az idővel elért sikerekből és kudarcokból való tanulást. Az elképzelés az, hogy az állapot nélküli ügynökök állapotfüggővé válnak.

Ez egy **kétfázisú memória folyamaton: kivonáson és frissítésen** keresztül működik. Először az ügynök szálához adott üzeneteket elküldi a Mem0 szolgáltatásnak, amely egy Nagy Nyelvi Modell (LLM) segítségével összefoglalja a beszélgetés előzményeit és új memóriákat nyer ki. Ezt követően egy LLM-vezérelt frissítési szakasz dönti el, hogy hozzáadja-e, módosítja-e vagy törli-e ezeket a memóriákat, melyek hibrid adatbázisban tárolódnak, amely tartalmazhat vektor-, gráf- és kulcs-érték adatbázisokat. A rendszer különféle memória típusokat is támogat, és képes grafikus memóriát is beépíteni az entitások közti kapcsolatok kezelésére.

#### Cognee

Egy másik hatékony megközelítés a **Cognee** használata, amely egy nyílt forráskódú szemantikus memória AI ügynököknek, és strukturált és strukturálatlan adatokat alakít át lekérdezhető tudásgráfokká, beágyazásokkal alátámasztva. A Cognee egy **kettős tárolós architektúrát** nyújt, amely kombinálja a vektor alapú hasonlóságkeresést a gráfkapcsolatokkal, lehetővé téve az ügynökök számára, hogy ne csak azt értsék meg, milyen információk hasonlóak, hanem a fogalmak közti kapcsolódást is.

Kiváló a **hibrid visszakeresésben**, amely ötvözi a vektoros hasonlóságot, a gráfszerkezetet és az LLM logikai következtetést – a nyers részletkereséstől a gráférzékeny kérdés-válaszolásig. A rendszer egy **élő memóriát** tart fenn, amely fejlődik és növekszik, miközben egy összekapcsolt gráfként lekérdezhető marad, támogatva mind a rövid távú munkameneti kontextust, mind a hosszú távú perzisztens memóriát.

A Cognee jegyzetfüzetes oktatóanyag ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) bemutatja ennek az egységes memória réteg megépítését, gyakorlati példákkal, amelyek eltérő adatforrások feldolgozását, a tudásgráf vizualizálását és különféle keresési stratégiák szerinti lekérdezést szemléltetnek az adott ügynök igényeihez igazítva.

### Memória tárolása RAG segítségével

A specializált memóriaeszközökön túl, mint a Mem0, használhatsz robosztus keresési szolgáltatásokat, például az **Azure AI Search-t háttérként a memóriák tárolására és előhívására**, különösen strukturált RAG esetén.

Ez lehetővé teszi, hogy az ügynök válaszait a saját adataiddal egészítsd ki, biztosítva relevánsabb és pontosabb válaszokat. Az Azure AI Search tárolhat felhasználóspecifikus utazási memóriákat, termékkatalógusokat vagy bármilyen más, adott területhez kapcsolódó tudást.

Az Azure AI Search támogat olyan képességeket, mint a **Strukturált RAG**, amely kiváló a sűrű, strukturált információk kinyerésében és előhívásában nagy adathalmazokból, például beszélgetési előzményekből, e-mailekből vagy akár képekből. Ez „szuperemberi pontosságot és előhívó képességet” biztosít a hagyományos szövegtöredékes és beágyazás-alapú megközelítésekkel szemben.

## AI ügynökök önfejlesztése

Az önfejlesztő ügynökök gyakori mintája egy **„tudásügynök”** bevezetése. Ez a külön ügynök figyeli a fő beszélgetést a felhasználó és a primér ügynök között. Feladata:

1. **Értékes információ azonosítása**: Meghatározni, hogy a beszélgetés valamely része érdemes-e megőrzésre általános tudásként vagy specifikus felhasználói preferenciaként.

2. **Kinyerés és összefoglalás**: Kivonatolni a lényeges tanulságot vagy preferenciát a beszélgetésből.

3. **Tárolás egy tudásbázisban**: Ezt a kinyert információt jellemzően egy vektoralapú adatbázisban megőrizni, hogy később előhívható legyen.

4. **Jövőbeli lekérdezések kiegészítése**: Amikor a felhasználó új lekérdezést indít, a tudásügynök előhívja a releváns korábban tárolt információkat, és hozzáfűzi a felhasználói prompthoz, kritikus kontextust adva a primér ügynöknek (hasonlóan a RAG-hez).

### Memória optimalizálása

• **Késleltetés kezelése**: A felhasználói interakciók lassítása elkerülése érdekében először egy olcsóbb, gyorsabb modellt lehet használni annak gyors megítélésére, hogy az információ tárolásra vagy előhívásra érdemes-e, és csak szükség esetén aktiválni a bonyolultabb kivonási/visszakeresési folyamatot.

• **Tudásbázis karbantartása**: Egy növekvő tudásbázis esetén a ritkábban használt információkat „hidegtárolóra” lehet áthelyezni a költségek kezelése érdekében.

## További kérdéseid vannak az ügynök memória kapcsán?

Csatlakozz a [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) közösséghez, találkozz más tanulókkal, vegyél részt konzultációs órákon, és kapj válaszokat AI ügynökökkel kapcsolatos kérdéseidre.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->