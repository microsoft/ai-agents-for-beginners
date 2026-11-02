# Memória az AI ügynökök számára
[![Agent Memory](../../../translated_images/hu/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Az AI ügynökök létrehozásának egyedi előnyeiről beszélve főként két dolgot említünk: az eszközök hívásának képességét feladatok elvégzésére, illetve a folyamatos fejlődés képességét. A memória az alapja annak, hogy egy önfejlesztő ügynök jobban tudjon élményeket teremteni a felhasználók számára.

Ebben a leckében megnézzük, mit jelent a memória az AI ügynökök esetében, hogyan tudjuk kezelni és alkalmazni azt alkalmazásaink javára.

## Bevezetés

Ez a lecke a következőket fogja lefedni:

• **Az AI ügynök memória megértése**: Mi a memória és miért elengedhetetlen az ügynökök számára.

• **Memória megvalósítása és tárolása**: Gyakorlati módszerek az AI ügynökök memóriaképességeinek bővítésére, kiemelve a rövid- és hosszú távú memóriát.

• **Az AI ügynökök önfejlesztése**: Hogyan teszi lehetővé a memória az ügynökök számára, hogy tanuljanak a múltbeli interakciókból és idővel fejlődjenek.

## Elérhető megvalósítások

Ez a lecke két átfogó jegyzetfüzet-gyakorlatot tartalmaz:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Mem0 és Azure AI Search használatával valósítja meg a memóriát a Microsoft Agent Framework-kel

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Strukturált memóriát valósít meg Cognee segítségével, automatikusan épít tudásgráfot beágyazás-alapú támogatással, megjeleníti a gráfot és intelligens lekérdezést tesz lehetővé

## Tanulási célok

A lecke elvégzése után tudni fogod, hogyan:

• **Megkülönböztesd az AI ügynök memória különböző típusait**, beleértve a munkamemóriát, rövid- és hosszú távú memóriát, valamint speciális formákat, mint a persona és epizodikus memória.

• **Megvalósítsd és kezeld a rövid- és hosszú távú memóriát** AI ügynökök számára a Microsoft Agent Framework-kel, olyan eszközöket használva, mint Mem0, Cognee, Whiteboard memória, és integrációval az Azure AI Search-szal.

• **Megértsd az önfejlesztő AI ügynökök mögött álló elveket**, és hogyan járulnak hozzá a fejlett memóriakezelő rendszerek a folyamatos tanuláshoz és alkalmazkodáshoz.

## Az AI ügynök memória megértése

Lényegében az **AI ügynökök memóriája azok a mechanizmusok, amelyek lehetővé teszik az információk megtartását és előhívását**. Ezek lehetnek specifikus részletek egy beszélgetésről, felhasználói preferenciák, múltbeli cselekvések vagy akár tanult minták.

Memória nélkül az AI alkalmazások gyakran állapot nélküli (stateless) jellegűek, vagyis minden interakció újrakezdődik. Ez ismétlődő és frusztráló felhasználói élményt eredményez, ahol az ügynök "elfelejti" az előző kontextust vagy preferenciákat.

### Miért fontos a memória?

Egy ügynök intelligenciája mélyen kapcsolódik ahhoz a képességéhez, hogy előhívjon és használjon múltbeli információkat. A memória lehetővé teszi az ügynökök számára, hogy:

• **Reflektívak legyenek**: Tanuljanak múltbeli cselekvésekből és eredményekből.

• **Interaktívak legyenek**: Fenntartsák a kontextust egy folyamatos beszélgetés során.

• **Proaktívak és reaktívak legyenek**: Megjósolják az igényeket vagy megfelelően reagálnak a történelmi adatok alapján.

• **Autonómok legyenek**: Önállóbban működjenek a tárolt tudásra alapozva.

A memória megvalósításának célja, hogy az ügynökök megbízhatóbbak és képzettebbek legyenek.

### Memória típusai

#### Munkamemória

Gondolj erre úgy, mint egy jegyzettömbre, amit az ügynök használ egyetlen, folyamatban lévő feladat vagy gondolatmenet során. Azonnali információkat tartalmaz, amelyek a következő lépés kiszámításához szükségesek.

Az AI ügynökök esetében a munkamemória gyakran rögzíti a legrelevánsabb információkat egy beszélgetésből, még akkor is, ha a teljes chat előzmény hosszú vagy lerövidített. Kiemeli a fő elemeket, mint például követelmények, javaslatok, döntések és cselekvések.

**Munkamemória példa**

Egy utazási foglaló ügynöknél a munkamemória rögzítheti a felhasználó aktuális kérését, például "Szeretnék egy utat lefoglalni Párizsba". Ez a konkrét kérés az ügynök azonnali kontextusában van, hogy vezérelje az aktuális interakciót.

#### Rövid távú memória

Ez a memória egyetlen beszélgetés vagy munkamenet időtartamára tárol információkat. Ez a jelenlegi chat kontextusát jelenti, lehetővé téve, hogy az ügynök visszautaljon a beszélgetés korábbi fordulóira.

A [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) Python SDK mintákban ez megfelel az `AgentSession`-nek, amelyet a `agent.create_session()` hoz létre. A munkamenet a keretrendszer beépített rövid távú memóriája: megtartja a beszélgetés kontextusát, amíg ugyanaz a munkamenet újra használatban van, de ez a kontextus nem marad meg a munkamenet végeztével vagy az alkalmazás újraindulásakor. A tények és preferenciák hosszútávú tárolásához, amelyeknek túl kell élniük a munkameneteket, általában adatbázist, vektorindexet vagy más tartós tárolót használj.

**Rövid távú memória példa**

Ha egy felhasználó megkérdezi, "Mennyibe kerül egy repülőjegy Párizsba?" majd utána azt, "Mi a helyzet a szállással ott?", a rövid távú memória biztosítja, hogy az ügynök tudja, miszerint az "ott" Párizsra vonatkozik ugyanabban a beszélgetésben.

#### Hosszú távú memória

Ez az információ több beszélgetés vagy munkamenet során megmarad. Lehetővé teszi az ügynökök számára, hogy megjegyezzék a felhasználói preferenciákat, korábbi interakciókat vagy általános tudást hosszabb időn keresztül. Ez fontos a személyre szabáshoz.

**Hosszú távú memória példa**

A hosszú távú memória eltárolhatja, hogy "Ben szeret síelni és a szabadban lenni, szereti a kávét hegyi kilátással, és el akarja kerülni a nehéz sípályákat egy korábbi sérülése miatt". Ez az információ a korábbi interakciókból származik, és hatással van a jövőbeni utazási tervek személyre szabott ajánlásaira.

#### Persona memória

Ez a speciális memória segít az ügynöknek egy következetes "személyiség" vagy "persona" kialakításában. Lehetővé teszi, hogy az ügynök megjegyezzen magáról vagy a szándékolt szerepéről részleteket, így az interakciók gördülékenyebbek és fókuszáltabbak legyenek.

**Persona memória példa**
Ha az utazási ügynök "szakértő síelési tervezőként" van kialakítva, a persona memória erősítheti ezt a szerepet, befolyásolva a válaszait, hogy azok szakértői hangvételűek és tudásalapúak legyenek.

#### Munkafolyamat/Epizodikus memória

Ez a memória tárolja azt a lépéssorozatot, amelyet az ügynök egy összetett feladat során tesz, beleértve a sikereket és kudarcokat is. Olyan, mint ha "epizódokat" vagy korábbi tapasztalatokat őrizne meg, hogy tanuljon belőlük.

**Epizodikus memória példa**

Ha az ügynök megpróbált lefoglalni egy adott járatot, de az sikertelen volt a rendelkezésre állás hiánya miatt, az epizodikus memória ezt a kudarcot rögzítheti, lehetővé téve, hogy az ügynök alternatív járatokat próbáljon ki vagy tájékoztassa a felhasználót tudatosabban egy későbbi próbálkozás során.

#### Entitás memória

Ez magában foglalja a beszélgetésekből származó specifikus entitások (emberek, helyek vagy tárgyak) és események kinyerését és megjegyzését. Lehetővé teszi az ügynök számára, hogy strukturáltan értelmezze a tárgyalt főbb elemeket.

**Entitás memória példa**

Egy korábbi utazásról szóló beszélgetésből az ügynök kinyerheti például a "Párizs", "Eiffel-torony", és "vacsora a Le Chat Noir étteremben" entitásokat. Egy későbbi interakciónál az ügynök emlékezhet a "Le Chat Noir"-ra, és felajánlhatja egy új foglalás létrehozását ott.

#### Strukturált RAG (Retrieval Augmented Generation)

Bár a RAG egy tágabb technika, a "Strukturált RAG" kiemelkedően erős memória technológiaként jelenik meg. Különféle forrásokból (beszélgetések, emailek, képek) sűrű, strukturált információt nyer ki, és használ erre a válaszok pontosságának, előhívásának és gyorsaságának növelésére. Ellentétben a klasszikus RAG-gal, amely kizárólag a szemantikai hasonlóságra támaszkodik, a Strukturált RAG az információ belső struktúráját használja.

**Strukturált RAG példa**

Ahelyett, hogy csak kulcsszavakat illesztene össze, a Strukturált RAG képes értelmezni egy emailből a repülőjárat részleteit (célállomás, dátum, idő, légitársaság) és strukturált módon tárolni azokat. Ez lehetővé teszi az olyan pontos lekérdezéseket, mint "Milyen járatot foglaltam Párizsba kedden?"

## Memória megvalósítása és tárolása

Az AI ügynökök memóriájának megvalósítása egy rendszeres memóriakezelési folyamatot jelent, amely magában foglalja az információk generálását, tárolását, előhívását, integrációját, frissítését, sőt a felejtést (vagy törlést) is. Különösen fontos az előhívás.

### Specializált memória eszközök

#### Mem0

Egy módja az ügynöki memória tárolásának és kezelésének a specializált eszközök, mint például a Mem0 használata. A Mem0 állandó memória rétegként működik, lehetővé téve az ügynökök számára, hogy előhívják a releváns interakciókat, tárolják a felhasználói preferenciákat és tényleges kontextust, valamint tanuljanak a sikerekből és kudarcokból az idő múlásával. Az elképzelés az, hogy az állapot nélküli ügynökök állapottartókká váljanak.

Ez egy **kétfázisú memóriacsővezetéken** keresztül működik: kivonatolás és frissítés. Először az ügynök szálához hozzáadott üzeneteket elküldik a Mem0 szolgáltatásnak, amely egy Nagy Nyelvi Modell használatával összefoglalja a beszélgetés történetét és kinyeri az új memóriákat. Ezt követően egy LLM-vezérelt frissítési fázis dönt arról, hogy ezeket a memóriákat hozzáadja, módosítja vagy törli-e, és ezeket kevert adattárban tárolják, amely magában foglalhat vektor-, gráf- és kulcs-érték adatbázisokat. Ez a rendszer támogatja a különféle memória típusokat és képes gráf memóriát is alkalmazni az entitások közötti kapcsolatok kezelésére.

#### Cognee

Egy másik erőteljes megközelítés a **Cognee**, egy nyílt forráskódú szemantikus memória AI ügynökök számára, amely átalakítja a strukturált és strukturálatlan adatokat lekérdezhető tudásgráfokká, amelyeket beágyazások támasztanak alá. A Cognee egy **kettős tároló architektúrát** biztosít, amely ötvözi a vektor-alapú hasonlóságkeresést a gráf kapcsolatokkal, lehetővé téve az ügynökök számára, hogy ne csak azt értsék meg, mi hasonló, hanem hogy a fogalmak hogyan kapcsolódnak egymáshoz.

Kiemelkedik a **hiper hibrid előhívásban**, amely ötvözi a vektor-hasonlóságot, a gráf struktúrát és az LLM-alapú érvelést - a nyers darabok keresésétől a gráf tudatos kérdésmegoldásig. A rendszer **élő memóriát** tart fenn, amely fejlődik és növekszik, miközben egy összefüggő gráfként lekérdezhető, támogatva a rövid távú munkamenet kontextust és a hosszú távú tartós memóriát is.

A Cognee jegyzetfüzet-gyakorlat ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) bemutatja ennek az egységes memória rétegnek az építését, gyakorlati példákkal változatos adatforrások bevitelére, a tudásgráf megjelenítésére és különféle keresési stratégiák szerinti lekérdezésre, az ügynökök egyedi igényeinek megfelelően.

### Memória tárolása RAG segítségével

A Mem0hoz hasonló specializált memória eszközökön túl használhatsz robusztus keresési szolgáltatásokat, például az **Azure AI Search-t** memória tárolására és előhívására, különösen strukturált RAG kiegészítéshez.

Ez lehetővé teszi, hogy az ügynök válaszait saját adataiddal támaszd alá, pontosabb és relevánsabb válaszokat biztosítva. Az Azure AI Search tárolhat felhasználóspecifikus utazási memóriákat, termékkatalógusokat vagy bármilyen egyéb területspecifikus tudást.

Az Azure AI Search támogatja a **Strukturált RAG** képességeit, amely kiváló a sűrű, strukturált információk kinyerésére és előhívására nagy adatállományokból, például beszélgetési előzményekből, emailekből vagy akár képekből. Ez "emberfeletti pontosságot és előhívást" biztosít a hagyományos szövegtöredékekkel és beágyazásokkal szemben.

## Az AI ügynökök önfejlesztése

Egy gyakori minta az önfejlesztő ügynököknél egy **„tudásügynök”** bevezetése. Ez a különálló ügynök figyeli a fő beszélgetést a felhasználó és a elsődleges ügynök között. Feladata:

1. **Értékes információk azonosítása**: Meghatározza, hogy a beszélgetés mely részei érdemesek általános tudásként vagy specifikus felhasználói preferenciaként megőrizni.

2. **Kinyerés és összefoglalás**: Kivonja a beszélgetés lényeges tanulságát vagy preferenciáját.

3. **Tudásbázisban tárolás**: Ezt a kinyert információt gyakran egy vektor adatbázisban tartósítja, hogy később előhívható legyen.

4. **Jövőbeli lekérdezések kiegészítése**: Amikor a felhasználó új lekérdezést indít, a tudásügynök visszakeresi a tárolt releváns információkat és hozzáfűzi azokat a felhasználói prompthoz, ezzel kulcsfontosságú kontextust adva az elsődleges ügynöknek (hasonlóan a RAG-hoz).

### Optimalizációk a memóriához

• **Késleltetés kezelése**: A felhasználói interakciók lassulásának elkerülése érdekében kezdetben egy olcsóbb, gyorsabb modell használható, hogy gyorsan ellenőrizze, érdemes-e az információt eltárolni vagy előhívni, és csak szükség esetén hívja meg a bonyolultabb kivonatolási/előhívási folyamatot.

• **Tudásbázis karbantartása**: A növekvő tudásbázis esetén a ritkábban használt információk "hideg tárolásba" helyezhetők a költségek kezelése érdekében.

## Több kérdésed van az ügynöki memóriáról?

Csatlakozz a [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D)-hoz, hogy találkozz más tanulókkal, részt vegyél nyitott órákon és válaszokat kapj AI ügynökökkel kapcsolatos kérdéseidre.
## Előző lecke

[Context Engineering for AI Agents](../12-context-engineering/README.md)

## Következő lecke

[Exploring Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->