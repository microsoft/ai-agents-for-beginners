# Kontextusmérnökség AI ügynökök számára

[![Kontextusmérnökség](../../../translated_images/hu/lesson-12-thumbnail.ed19c94463e774d4.webp)](https://youtu.be/F5zqRV7gEag)

> _(Kattints a fenti képre a lecke videójának megtekintéséhez)_

Fontos megérteni az alkalmazás összetettségét, amelyhez AI ügynököt építesz, ha megbízható ügynököt szeretnél készíteni. Olyan AI ügynököket kell alkotnunk, amelyek hatékonyan kezelik az információkat, hogy összetettebb igényeket is kielégítsenek a prompt-mérnökségen túl.

Ebben a leckében megnézzük, mi az a kontextusmérnökség, és milyen szerepet tölt be az AI ügynökök építésében.

## Bevezetés

Ez a lecke az alábbiakat fogja lefedni:

• **Mi a kontextusmérnökség** és miben különbözik a prompt-mérnökségtől.

• **Stratégiák a hatékony kontextusmérnökséghez**, beleértve az információ írását, kiválasztását, tömörítését és elkülönítését.

• **Gyakori kontextushibák**, amelyek meghiúsíthatják az AI ügynököd működését, és hogyan lehet ezeket orvosolni.

## Tanulási célok

A lecke elvégzése után tudni fogod, hogyan:

• **Határozd meg a kontextusmérnökséget** és különböztesd meg a prompt-mérnökségtől.

• **Azonosítsd a kontextus kulcselemeit** a Nagy Nyelvi Modell (LLM) alkalmazásokban.

• **Alkalmazz stratégiákat a kontextus írására, kiválasztására, tömörítésére és elkülönítésére**, hogy javítsd az ügynök teljesítményét.

• **Ismerd fel a gyakori kontextushibákat**, mint például mérgezés, elterelés, zavarodottság és összeütközés, valamint alkalmazz enyhítő technikákat.

## Mi az a kontextusmérnökség?

AI ügynökök esetén a kontextus az, ami vezérli az AI Ügynök tervét egy adott cselekvés végrehajtására. A kontextusmérnökség az a gyakorlat, amikor biztosítjuk, hogy az AI ügynök rendelkezzen a megfelelő információval a feladat következő lépésének végrehajtásához. A kontextusablak mérete korlátozott, így ügynöképítőként olyan rendszereket és folyamatokat kell kialakítanunk, amelyek kezelik az információ hozzáadását, eltávolítását és tömörítését a kontextusablakban.

### Prompt-mérnökség vs Kontextusmérnökség

A prompt-mérnökség egyetlen statikus utasítássorozatra fókuszál, hogy hatékonyan vezérelje az AI ügynököket szabályok alkalmazásával. A kontextusmérnökség dinamikus információk halmazának kezelését jelenti, ideértve az eredeti promptot is, hogy az AI ügynök idővel rendelkezzen a szükséges információval. A kontextusmérnökség fő célja, hogy ez a folyamat ismételhető és megbízható legyen.

### Kontextustípusok

[![Kontextustípusok](../../../translated_images/hu/context-types.fc10b8927ee43f06.webp)](https://youtu.be/F5zqRV7gEag)

Fontos megjegyezni, hogy a kontextus nem csupán egyetlen dolog. Az AI ügynök által szükséges információ különböző forrásokból származhat, és rajtunk múlik, hogy biztosítsuk ezekhez a forrásokhoz való hozzáférést:

A kontextus, amelyet egy AI ügynöknek kezelnie kell, az alábbiakat foglalhatja magában:

• **Utasítások:** Ezek az ügynök „szabályai” – promptok, rendszerüzenetek, néhány példaként bemutatott eset (amikor megmutatják az AI-nak, hogyan kell valamit csinálni), valamint az általa használható eszközök leírása. Itt találkozik a prompt-mérnökség és a kontextusmérnökség fókusza.

• **Tudás:** Tények, adatbázisokból lekért információk vagy az ügynök által felhalmozott hosszú távú emlékek. Ide tartozik a Retrieval Augmented Generation (RAG) rendszer integrálása, ha ügynöknek különféle tudásbázisokhoz és adatbázisokhoz kell hozzáférnie.

• **Eszközök:** Külső függvények, API-k és MCP szerverek definíciói, amelyeket az ügynök hívhat, valamint az ezek használatából származó visszacsatolások (eredmények).

• **Beszélgetés Előzmények:** A felhasználóval folytatott folyamatban lévő párbeszéd. Az idő múlásával ezek egyre hosszabbak és összetettebbek lesznek, így egyre több helyet foglalnak el a kontextusablakban.

• **Felhasználói Preferenciák:** Az idővel megtanult információk a felhasználó kedveléseiről vagy nem kedveléseiről. Ezeket tárolni lehet, és előhívásuk segíthet fontos döntések meghozatalánál a felhasználó támogatására.

## Hatékony Kontextusmérnökség Stratégiái

### Tervezési Stratégiák

[![Kontextusmérnökség Legjobb Gyakorlatai](../../../translated_images/hu/best-practices.f4170873dc554f58.webp)](https://youtu.be/F5zqRV7gEag)

A jó kontextusmérnökség jó tervezéssel kezdődik. Íme egy olyan megközelítés, amely segít elkezdeni gondolkodni a kontextusmérnökség alkalmazásáról:

1. **Határozd meg az egyértelmű eredményeket** – Az AI ügynöknek kiosztott feladatok eredményeit pontosan definiálni kell. Válaszolj a kérdésre: „Hogy fog kinézni a világ, amikor az AI ügynök befejezte feladatát?” Más szóval, milyen változást, információt vagy választ kell kapnia a felhasználónak az AI ügynökkel való interakció után.
2. **Térképezd fel a kontextust** – Miután meghatároztad az AI ügynök eredményeit, meg kell válaszolnod a kérdést: „Milyen információra van szüksége az AI ügynöknek a feladat elvégzéséhez?” Így elkezdheted térképezni, hol található meg ez az információ.
3. **Hozz létre kontextus csatornákat** – Mivel most már tudod, hol van az információ, válaszold meg a kérdést: „Hogyan fogja az ügynök ezt az információt megszerezni?” Ezt többféleképpen lehet megtenni, beleértve a RAG használatát, MCP szerverek és más eszközök alkalmazását.

### Gyakorlati stratégiák

A tervezés fontos, de amikor az információ elkezd beáramlani az ügynök kontextusablakába, gyakorlati stratégiákra van szükség annak kezelésére:

#### Kontextus kezelése

Bár egyes információk automatikusan kerülnek be a kontextusablakba, a kontextusmérnökség aktívabb szerepvállalást jelent az információval kapcsolatban, amit néhány stratégia segítségével meg lehet valósítani:

 1. **Ügynök jegyzetfüzet**
 Ez lehetővé teszi, hogy egy AI ügynök jegyzeteket készítsen az aktuális feladatokról és a felhasználóval folytatott interakciókról egy munkamenet során. Ez a jegyzetfüzet a kontextusablakon kívül kell, hogy legyen, például egy fájlban vagy futásidejű objektumban, amelyet az ügynök később előhívhat, ha szükséges.

 2. **Emlékek**
 A jegyzetfüzetek jók az információk egy munkameneten túli kezelésére, a hosszabb távú emlékek pedig lehetővé teszik az ügynökök számára, hogy több munkameneten át releváns információkat tároljanak és előhívjanak. Ez magában foglalhat összefoglalókat, felhasználói preferenciákat és visszajelzéseket a jövőbeni fejlesztésekhez.

 3. **Kontextus tömörítése**
  Amint a kontextusablak nő és eléri a limitet, alkalmazhatók olyan technikák, mint az összefoglalás és a ritkítás. Ez jelentheti, hogy csak a legfontosabb információ marad meg, vagy a régebbi üzenetek eltávolítását.
  
 4. **Többügynökös rendszerek**
  Többügynökös rendszerek fejlesztése a kontextusmérnökség egyik formája, mivel minden ügynöknek megvan a saját kontextusablaka. Annak megtervezése, hogy hogyan történik a kontextus megosztása és átadása az egyes ügynökök között, további szempontot jelent ezeknek a rendszereknek az építésekor.
  
 5. **Sandbox környezetek**
  Ha egy ügynöknek kódot kell futtatnia vagy nagy mennyiségű információt kell feldolgoznia egy dokumentumban, ez sok token feldolgozását igényli. Ahelyett, hogy mindez a kontextusablakban tárolódna, az ügynök használhat egy sandbox környezetet, amely képes lefuttatni a kódot, és csak az eredményeket és a többi releváns információt olvassa be.
  
 6. **Futásidejű állapot objektumok**
   Ez úgy valósul meg, hogy információs tárolókat hozunk létre olyan helyzetek kezelésére, amikor az ügynöknek hozzáférést kell kapnia bizonyos információkhoz. Egy összetett feladat esetén ez lehetővé teszi az ügynök számára, hogy lépésről lépésre tárolja a részfeladatok eredményeit, így a kontextus csak az adott részfeladathoz kapcsolódik.

#### Kontextus vizsgálata

Miután alkalmaztad valamelyik stratégiát, érdemes ellenőrizni, milyen kontextust kapott valójában a következő modellhívás. Egy hasznos hibakeresési kérdés:

> Az ügynök túl sok kontextust töltött be, rossz kontextust, vagy hiányzott neki szükséges kontextus?

A kérdés megválaszolásához nem szükséges a nyers promptokat, eszköz kimeneteket vagy memória tartalmakat naplózni. A gyártásban előnyben részesítsd a kisebb kontextusvizsgálati rekordokat, amelyek számlálásokat, azonosítókat, hash-kódokat és szabályzati címkéket tartalmaznak:

- **Kiválasztás:** Kövesd nyomon, hány jelölt tömböt, eszközt vagy memóriát vizsgáltak meg, hányat választottak ki, és mely szabály vagy pontszám miatt szűrtek ki másokat.
- **Tömörítés:** Rögzítsd a forrás tartományt vagy a nyomkövetési azonosítót, az összefoglaló azonosítóját, becsült token számot tömörítés előtt és után, valamint azt, hogy a nyers tartalom kizárásra került-e a következő hívásból.
- **Elkülönítés:** Jegyezd fel, melyik részfeladat futott külön ügynökben, munkamenetben vagy sandboxban, milyen kötött összefoglaló tért vissza, és hogy a nagy eszközkimenet kívül maradt-e a fő ügynök kontextusán.
- **Memória és RAG:** Tárold a lekért dokumentumazonosítókat, memóriaazonosítókat, pontszámokat, kiválasztott azonosítókat és az átfogalmazási státuszt a teljes lekért szöveg helyett.
- **Biztonság és adatvédelem:** Előnyben részesítsd a hash-kódokat, azonosítókat, token-vödröket és szabályzati címkéket a kényes prompt szöveg, eszközargumentumok, eszközeredmények vagy felhasználói memória tartalmak helyett.

A cél nem több kontextus tárolása, hanem elegendő bizonyíték hagyása, hogy a fejlesztő meg tudja mondani, melyik kontextusstratégia futott le és hogy az a következő modellhívást a szándékolt módon változtatta meg.

### Kontextusmérnökség példa

Tegyük fel, hogy egy AI ügynököt szeretnénk arra kérni, hogy **"Foglaljon nekem egy utazást Párizsba."**

• Egy egyszerű ügynök, amely csak prompt-mérnökséget használ, lehet, hogy csak azt válaszolja: **"Rendben, mikor szeretnél Párizsba utazni?"** Csak az adott pillanatban feltett kérdést dolgozza fel.

• Egy ügynök, amely a kontextusmérnökségi stratégiákat alkalmazza, ennél sokkal többet tesz. Mielőtt válaszolna, a rendszere lehet, hogy:

  ◦ **Ellenőrzi a naptáradat**, hogy szabad időpontokat találjon (valós idejű adatok lekérése).

 ◦ **Felidézi a korábbi utazási preferenciáidat** (hosszú távú memóriából), mint például a kedvenc légitársaságod, költségvetésed vagy az, hogy közvetlen járatokat preferálsz-e.

 ◦ **Azonosítja az elérhető eszközöket** a repülőjegy- és szállásfoglaláshoz.

- Majd egy példa válasz lehet: "Szia [A te neved]! Látom, hogy az október első hetében szabad vagy. Keressek közvetlen járatokat Párizsba a [Kedvenc légitársaság]-nál a szokásos [Költségvetés] kereteden belül?" Ez a gazdagabb, kontextus-értő válasz jól szemlélteti a kontextusmérnökség erejét.

## Gyakori kontextushibák

### Kontextusmérgezés

**Mi ez:** Amikor egy hallucináció (hamis információ, amelyet az LLM generál) vagy hiba bekerül a kontextusba és ismételten hivatkoznak rá, az ügynök lehetetlen célokat tűz ki vagy értelmetlen stratégiákat dolgoz ki.

**Mit tegyél:** Vezess be **kontextus érvényesítést** és **karantént**. Érvényesítsd az információkat mielőtt azok bekerülnének a hosszú távú memóriába. Ha potenciális mérgezést észlelsz, indíts új kontextus-vonalakat, hogy megakadályozd a rossz információ terjedését.

**Utazásfoglalási példa:** Az ügynököd hallucinál egy **közvetlen járatot egy kis helyi repülőtérről egy távoli nemzetközi városba**, amely valójában nem kínál nemzetközi járatokat. Ez a nem létező járat részlete bekerül a kontextusba. Később, amikor az ügynökhöz fordulsz foglalásért, állandóan próbál jegyeket találni erre a lehetetlen járatra, ami ismételt hibákhoz vezet.

**Megoldás:** Vezess be egy lépést, amely **valós idejű API-val ellenőrzi a járat létezését és útvonalat** _mielőtt_ a járat részlet bekerül az ügynök működési kontextusába. Ha az ellenőrzés sikertelen, a hibás információ „karanténba” kerül, és nem használják tovább.

### Kontextuselterelés

**Mi ez:** Amikor a kontextus olyan nagy lesz, hogy a modell túlzottan az összegyűjtött előzményekre koncentrál ahelyett, hogy a tanulás során szerzett ismereteket használná, ismétlődő vagy haszontalan cselekvésekhez vezetve. A modellek még a kontextusablak telítődése előtt hibázni kezdenek.

**Mit tegyél:** Használj **kontextus összefoglalást**. Időszakosan tömörítsd az összegyűlt információkat rövidebb összefoglalókba, megtartva a fontos részleteket, miközben eltávolítod a felesleges előzményeket. Ez segít „újraindítani” a fókuszt.

**Utazásfoglalási példa:** Hosszú ideje beszélgetsz különböző álomutazási célokról, beleértve egy részletes beszámolót a két évvel ezelőtti hátizsákos utadról. Amikor végül arra kéred, hogy **„találj egy olcsó járatot a következő hónapra”**, az ügynök belebonyolódik a régi, relevánsatlan részletekbe, és folyton az utazófelszerelésed vagy korábbi útiterv részleteit kérdezi, figyelmen kívül hagyva a jelenlegi kérésedet.

**Megoldás:** Egy bizonyos mennyiségű forduló után vagy amikor a kontextus túl nagy lesz, az ügynöknek **összefoglalnia kell a beszélgetés legfrissebb és legfontosabb részeit** – a jelenlegi utazási dátumaidra és célpontodra koncentrálva –, és ezt a tömörített összefoglalót használnia a következő LLM híváshoz, miközben elveti a kevésbé releváns múltbeli beszélgetést.

### Kontextuszavar

**Mi ez:** Amikor felesleges kontextus, gyakran túl sok elérhető eszköz formájában, rossz válaszokat generál vagy nem releváns eszközöket hív meg a modell. A kisebb modellek különösen hajlamosak erre.

**Mit tegyél:** Vezess be **eszközök kiválasztásának kezelését** RAG technikák használatával. Tárold az eszközök leírását egy vektoriális adatbázisban, és válaszd ki _csak_ a legrelevánsabb eszközöket az adott feladathoz. Kutatások szerint 30 alatti eszközválasztás javasolt.

**Utazásfoglalási példa:** Az ügynököd számos eszközhöz fér hozzá: `book_flight`, `book_hotel`, `rent_car`, `find_tours`, `currency_converter`, `weather_forecast`, `restaurant_reservations`, stb. Megkérdezed: **„Mi a legjobb módja a közlekedésnek Párizsban?”** Az eszközök nagy száma miatt az ügynök zavarba jön, és megpróbálja hívni a `book_flight`-et _Párizson belül_, vagy a `rent_car`-t, holott te inkább tömegközlekedést preferálsz, mert az eszközleírások átfedik egymást, vagy nem tudja felismerni a legjobbat.

**Megoldás:** Használj **RAG-et az eszközleírások fölött**. Amikor a közlekedést kérdezed Párizsban, a rendszer dinamikusan lekéri _csak_ a legrelevánsabb eszközöket, mint a `rent_car` vagy `public_transport_info`, kérésed alapján, így egy fókuszált eszközkészletet mutat az LLM-nek.

### Kontextusütközés

**Mi ez:** Amikor ellentmondásos információk vannak a kontextusban, ami következetlen érveléshez vagy rossz végső válaszokhoz vezet. Ez gyakran akkor fordul elő, amikor az információk fokozatosan érkeznek, és a korai, helytelen feltételezések még mindig benne maradnak a kontextusban.

**Mit tegyél:** Használj **kontextus-ritkítást** és **átterhelést**. A ritkítás azt jelenti, hogy eltávolítod a régi vagy ellentmondásos információkat, amint új részletek érkeznek. Az átterhelés külön „jegyzetfüzetet” (scratchpad) ad a modellnek, hogy ott dolgozza fel az információkat a fő kontextus rendetlenítése nélkül.


**Utazási foglalás példája:** Először az ügynöködnek azt mondod, **„Gazdaságos osztályon szeretnék repülni.”** Később a beszélgetés során meggondolod magad, és azt mondod, **„Valójában ezen az úton üzleti osztályra váltsunk.”** Ha mindkét utasítás megmarad a kontextusban, az ügynök ellentmondásos keresési eredményeket kaphat, vagy összezavarodhat, hogy melyik preferenciát helyezze előtérbe.

**Megoldás:** Vezessük be a **kontextus lekicsinyítést**. Amikor egy új utasítás ellentmond a réginek, a régebbi utasítás eltávolításra kerül vagy kifejezetten felülírásra a kontextusban. Alternatívaként az ügynök használhat egy **vázlatfüzetet**, hogy egyeztesse az ellentmondó preferenciákat mielőtt döntést hoz, biztosítva, hogy csak a végleges, egységes utasítás irányítsa a cselekedeteit.

## További kérdéseid vannak a kontextus kialakításáról?

Csatlakozz a [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) közösséghez, hogy találkozz más tanulókkal, részt vegyél nyitott beszélgetéseken, és választ kapj az AI ügynökeiddel kapcsolatos kérdéseidre.
## Előző Lecke

[Agentikus protokollok](../11-agentic-protocols/README.md)

## Következő Lecke

[Memória az AI ügynökök számára](../13-agent-memory/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->