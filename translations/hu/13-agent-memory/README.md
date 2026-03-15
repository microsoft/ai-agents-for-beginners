# Memória az MI Ügynökök számára 
[![Agent Memory](../../../translated_images/hu/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Az MI ügynökök készítésének egyedi előnyeiről beszélve elsősorban két dolgot szoktak megvitatni: az eszközök meghívásának képességét a feladatok elvégzéséhez, valamint az idővel történő fejlődés képességét. A memória alapja az önfejlesztő ügynök létrehozásának, amely jobb élményeket tud teremteni a felhasználóink számára.

Ebben a leckében megvizsgáljuk, hogy mi a memória az MI ügynökök számára, és hogyan kezelhetjük és használhatjuk azt alkalmazásaink előnyére.

## Bevezetés

Ez a lecke a következőket tartalmazza:

• **Az MI ügynök memória megértése**: Mi a memória, és miért fontos az ügynökök számára.

• **A memória megvalósítása és tárolása**: Gyakorlati módszerek az MI ügynökeid memóriaképességeinek bővítésére, a rövid és hosszú távú memória fókuszálásával.

• **Az MI ügynökök önfejlesztővé tétele**: Hogyan teszi lehetővé a memória, hogy az ügynökök tanuljanak a korábbi interakciókból és idővel fejlődjenek.

## Elérhető megvalósítások

Ez a lecke két átfogó jegyzetfüzet-tananyagot tartalmaz:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Mem0 és Azure AI Search használatával valósítja meg a memóriát a Microsoft Agent Framework segítségével

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Strukturált memóriát valósít meg Cognee segítségével, automatikusan építve egy beágyazások által támogatott tudásgráfot, megjelenítve a gráfot és intelligens visszakeresést biztosítva

## Tanulási célok

A lecke elvégzése után tudni fogod, hogyan kell:

• **Megkülönböztetni az MI ügynök különböző típusú memóriáit**, beleértve a munkamemóriát, a rövid távú és hosszú távú memóriát, valamint a speciális formákat, mint a személyiség- és epizodikus memória.

• **Megvalósítani és kezelni a rövid és hosszú távú memóriát az MI ügynökök számára** a Microsoft Agent Framework használatával, kihasználva olyan eszközöket, mint a Mem0, Cognee, Whiteboard memória, és integrálva az Azure AI Search szolgáltatást.

• **Megérteni az önfejlesztő MI ügynökök mögötti elveket** és azt, hogy a stabil memória kezelési rendszerek hogyan járulnak hozzá a folyamatos tanuláshoz és alkalmazkodáshoz.

## Az MI ügynök memória megértése

Lényegében az **MI ügynökök memóriája az a mechanizmus, amely lehetővé teszi számukra az információk megőrzését és előhívását**. Ez az információ lehet beszélgetésről szóló részletek, felhasználói preferenciák, múltbeli cselekvések vagy akár megtanult mintázatok.

Memória nélkül az MI alkalmazások gyakran állapot nélküli alkalmazások, vagyis minden interakció nulláról kezdődik. Ez ismétlődő és frusztráló felhasználói élményt eredményez, ahol az ügynök "elfelejti" a korábbi kontextust vagy preferenciákat.

### Miért fontos a memória?

Az ügynök intelligenciája mélyen kapcsolódik a korábbi információk előhívásának és felhasználásának képességéhez. A memória lehetővé teszi az ügynökök számára, hogy:

• **Reflektívak legyenek**: Tanuljanak a múltbeli cselekvésekből és eredményekből.

• **Interaktívak legyenek**: Fenntartsák a kontextust a folyamatban lévő beszélgetés során.

• **Proaktívak és reaktívak legyenek**: Előre jelezzék a szükségleteket vagy megfelelően reagáljanak a történelmi adatok alapján.

• **Autonómok legyenek**: Függetlenebben működjenek, miközben a tárolt tudásra támaszkodnak.

A memória megvalósításának célja, hogy az ügynökök megbízhatóbbak és képzettebbek legyenek.

### A memória típusai

#### Munkamemória

Gondoljunk erre úgy, mint egy egyszerű jegyzetpapírra, amelyet az ügynök egyetlen, folyamatban lévő feladat vagy gondolatmenet során használ. Ez tartalmazza a következő lépéshez szükséges közvetlen információkat.

Az MI ügynökök számára a munkamemória gyakran megragadja a beszélgetés legrelevánsabb információit, még ha a teljes csevegéstörténet hosszú vagy lerövidített is. Ez kulcselemekre koncentrál, mint a követelmények, javaslatok, döntések és cselekvések.

**Munkamemória példa**

Egy utazási foglaló ügynöknél a munkamemória megőrizheti a felhasználó aktuális kérését, például: „Parizsba szeretnék utazást foglalni”. Ez a konkrét igény az ügynök azonnali kontextusában van ahhoz, hogy irányítsa az aktuális interakciót.

#### Rövid távú memória

Ez a memóriatípus megőrzi az információt egyetlen beszélgetés vagy munkamenet idejére. Ez a jelenlegi csevegés kontextusa, amely lehetővé teszi az ügynöknek, hogy visszautaljon a párbeszéd korábbi köreiben elhangzottakra.

**Rövid távú memória példa**

Ha a felhasználó megkérdezi: „Mennyibe kerül egy repülőjegy Párizsba?”, majd azt követően: „Mi a helyzet a szállással ott?”, a rövid távú memória biztosítja, hogy az ügynök tudja, hogy az „ott” kifejezés a „Párizs”-ra vonatkozik ugyanabban a beszélgetésben.

#### Hosszú távú memória

Ez az információ több beszélgetés vagy munkamenet során fennmarad. Lehetővé teszi az ügynökök számára, hogy emlékezzenek a felhasználó preferenciáira, korábbi interakcióira vagy általános tudásra hosszabb időn keresztül. Ez fontos a személyre szabás szempontjából.

**Hosszú távú memória példa**

Egy hosszú távú memória tárolhatja, hogy „Ben szeret síelni és szabadban tevékenykedni, kedveli a kávét hegyi kilátással, és el akarja kerülni a nehéz sípályákat egy korábbi sérülés miatt”. Ez az információ, amelyet korábbi interakciókból tanult, befolyásolja a jövőbeni utazási tervezési ajánlásokat, így azok nagyon személyre szabottak lesznek.

#### Személyiség memória

Ez a speciális memória típus segíti az ügynököt, hogy kialakítson egy következetes „személyiséget” vagy „persona”-t. Lehetővé teszi az ügynök számára, hogy emlékezzen önmagára vagy szándékolt szerepére, ezáltal folyékonyabb és fókuszáltabb interakciókat teremtve.

**Személyiség memória példa**

Ha az utazási ügynököt „szakértő sítervezőként” tervezték, a személyiség memória erősítheti ezt a szerepet, befolyásolva válaszait, hogy azok megfeleljenek egy szakértő hangvételének és tudásának.

#### Munkafolyamat / Epizódikus memória

Ez a memória tárolja az ügynök által végrehajtott lépések sorozatát egy összetett feladat során, beleértve a sikereket és kudarcokat is. Olyan, mintha „epizódokat” vagy korábbi tapasztalatokat őrizne meg, hogy tanuljon belőlük.

**Epizódikus memória példa**

Ha az ügynök megpróbált egy adott járatot lefoglalni, de az nem sikerült elérhetőség hiánya miatt, az epizódikus memória rögzítheti ezt a sikertelenséget. Ez lehetővé teszi, hogy az ügynök alternatív járatokat próbáljon vagy tájékoztassa a felhasználót az ügyről tájékozottabban egy következő próbálkozás során.

#### Entitás memória

Ez magában foglalja a beszélgetésekből kinyert és megjegyzett konkrét entitásokat (például embereket, helyeket vagy tárgyakat) és eseményeket. Lehetővé teszi az ügynök számára, hogy strukturáltan értelmezze a megbeszélt kulcselemeket.

**Entitás memória példa**

Egy múltbeli utazásról szóló beszélgetésből az ügynök kinyerheti a „Párizs”, az „Eiffel-torony” és a „vacsora a Le Chat Noir étteremben” kifejezéseket mint entitásokat. A jövőbeni interakció során az ügynök emlékezhet a „Le Chat Noir”-ra, és felajánlhatja, hogy új foglalást készít oda.

#### Strukturált RAG (Retrieval Augmented Generation)

Bár a RAG egy tágabb technika, a „Strukturált RAG” kiemelt mint erőteljes memória technológia. Kivonja a tömör, strukturált információkat különböző forrásokból (beszélgetésekből, emailekből, képekből), és ezt használja válaszok pontosságának, előhívásának és sebességének javítására. Ellentétben a klasszikus RAG-gal, amely kizárólag szemantikai hasonlóságra támaszkodik, a Strukturált RAG az információk veleszületett szerkezetét használja.

**Strukturált RAG példa**

Kulcsszavak egyezése helyett a Strukturált RAG képes lehet kinyerni repülőjegy-adatokat (célállomás, dátum, idő, légitársaság) egy e-mailből, és strukturáltan tárolni azokat. Ez lehetővé teszi az olyan pontos lekérdezéseket, mint „Milyen járatot foglaltam Párizsba kedden?”

## A memória megvalósítása és tárolása

Az MI ügynökök memóriájának megvalósítása egy rendszerezett folyamatot jelent, azaz a **memóriakezelést**, amely magában foglalja az információ generálását, tárolását, előhívását, integrálását, frissítését, sőt akár az „elfelejtést” (törlést) is. Az előhívás különösen kulcsfontosságú.

### Speciális memória eszközök

#### Mem0

Az ügynök memória tárolására és kezelésére egyik eszköz a Mem0. A Mem0 egy állandó memória rétegként működik, amely lehetővé teszi az ügynököknek, hogy előhívják a releváns interakciókat, tárolják a felhasználói preferenciákat és a tényalapú kontextust, és idővel tanuljanak a sikerekből és kudarcokból. Az ötlet az, hogy az állapot nélküli ügynökök állapottartóvá váljanak.

Ez egy **kétfázisú memória-folyamatból áll: kivonás és frissítés**. Először az adott ügynök szálához hozzáadott üzenetek a Mem0 szolgáltatásba kerülnek, amely egy Large Language Model (LLM) segítségével összefoglalja a beszélgetéstörténetet és kinyeri az új emlékeket. Ezt követően egy LLM által vezérelt frissítési szakasz dönt arról, hogy az emlékeket hozzáadja, módosítja vagy törli, majd ezeket egy hibrid adattárolóban tárolja, amely vektor-, gráf- és kulcs-érték adatbázisokat is tartalmazhat. Ez a rendszer különféle memória típusokat támogat, és képes gráf memóriát is beépíteni az entitások közötti kapcsolatok kezeléséhez.

#### Cognee

Egy másik hatékony megközelítés a **Cognee** használata, amely egy nyílt forráskódú szemantikus memória az MI ügynökök számára, amely strukturált és strukturálatlan adatokat alakít lekérdezhető tudásgráfokká, amelyeket beágyazások támogatnak. A Cognee egy **kettős tárolós architektúrát** alkalmaz, amely ötvözi a vektor alapú hasonlóságkeresést és a gráf kapcsolatrendszereket, így az ügynökök nemcsak azt értik meg, hogy milyen információk hasonlóak, hanem azt is, hogy a fogalmak hogyan kapcsolódnak egymáshoz.

Kiválóan alkalmas a **hibrid visszakeresésre**, amely egyesíti a vektor hasonlóságot, a gráf szerkezetet és a LLM-alapú érvelést – a nyers darabok keresésétől a gráf-tudatos kérdés-megadásokig. A rendszer fenntartja az **élő memóriát**, amely fejlődik és növekszik, miközben egy összekapcsolt gráfként lekérdezhető marad, támogatva a rövid távú munkameneti kontextust és a hosszú távú állandó memóriát.

A Cognee jegyzetfüzet-tananyag ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) bemutatja ennek az egységes memória rétegnek az építését, gyakorlati példákkal különféle adatforrások befogadására, a tudásgráf vizualizálására és különböző keresési stratégiák használatára, amelyek az adott ügynök igényeihez igazodnak.

### A memória tárolása RAG-gal

A mem0-hoz hasonló speciális memória eszközökön túl használhatók megbízható keresési szolgáltatások, mint az **Azure AI Search**, amely memóriák tárolására és visszakeresésére szolgálhat, különösen a strukturált RAG esetén.

Ez lehetővé teszi, hogy az ügynök válaszai saját adataiddal legyenek alátámasztva, biztosítva a relevánsabb és pontosabb válaszokat. Az Azure AI Search használható felhasználó-specifikus utazási emlékek, termékkatalógusok vagy bármilyen más domain-specifikus tudás tárolására.

Az Azure AI Search támogat olyan képességeket, mint a **Strukturált RAG**, amely kiválóan alkalmas tömör, strukturált információk kinyerésére és előhívására nagy adatállományokból, mint a beszélgetések története, e-mailek vagy akár képek. Ez „emberfeletti pontosságot és előhívást” nyújt a hagyományos szövegdarabolásos és beágyazásos megközelítésekkel szemben.

## Az MI ügynökök önfejlesztővé tétele

Az önfejlesztő ügynököknél gyakori mintázat egy **„tudás ügynök”** bevezetése. Ez a különálló ügynök megfigyeli a fő beszélgetést a felhasználó és a fő ügynök között. Feladata:

1. **Értékes információk azonosítása**: Meghatározni, hogy a beszélgetés bármely része érdemes-e általános tudásként vagy specifikus felhasználói preferenciaként elmentésre.

2. **Kinyerés és összefoglalás**: Kivonatolni az alapvető tanulságokat vagy preferenciákat a beszélgetésből.

3. **Tárolás egy tudásbázisban**: Elmenteni ezt a kinyert információt, gyakran vektoralapú adatbázisba, hogy később előhívható legyen.

4. **Jövőbeli lekérdezések kiegészítése**: Amikor a felhasználó új lekérdezést indít, a tudás ügynök előhívja a releváns tárolt adatokat, és hozzáfűzi a felhasználói kérésekhez, így kritikus kontextust biztosítva a fő ügynök számára (hasonlóan a RAG-hoz).

### Memória optimalizálások

• **Késleltetés kezelése**: Annak érdekében, hogy ne lassítsa le a felhasználói interakciókat, kezdetben olcsóbb, gyorsabb modell alkalmazható arra, hogy gyorsan ellenőrizze, érdemes-e tárolni vagy előhívni az információt, és csak szükség esetén hívja meg a komplexebb kivonási/visszakeresési folyamatot.

• **Tudásbázis karbantartása**: Egy növekvő tudásbázis esetén a kevésbé gyakran használt információk „hideg tárhelyre” mozgathatók a költségek kezelése érdekében.

## Több kérdésed van az ügynök memória kapcsán?

Csatlakozz a [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) csatornához, hogy találkozz más tanulókkal, részt vehess konzultációkon, és választ kapj az MI ügynökökkel kapcsolatos kérdéseidre.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az igyekszünk pontosságra törekedni, kérjük, vegye figyelembe, hogy az automatikus fordítások tartalmazhatnak hibákat vagy pontatlanságokat. Az eredeti, anyanyelven írt dokumentum tekintendő hiteles forrásnak. Kritikus információk esetén professzionális, emberi fordítást javaslunk. Nem vállalunk felelősséget az ebből eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->