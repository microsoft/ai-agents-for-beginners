# AI Ügynökök Kezdőknek - Tanulmányi Útmutató

Használd ezt az útmutatót gyakorlati segédeszközként a tanfolyam során. Ez
nem helyettesíti az órákat. Segít eldönteni, hogy hol kezdj, mire figyelj minden órában,
és hogyan kötheted össze a gondolatokat egy kis működő ügynök demóba.


Ha először jársz itt, kezdd egyszerűen:

1. Olvasd el a [Tanfolyam Beállítást](./00-course-setup/README.md).
2. Teljesítsd a 01-06. órákat sorrendben.
3. Tartson egy kis demó ötletet a fejedben tanulás közben.
4. Minden óra után tedd fel a kérdést: "Mit tud most az ügynököm, amit
   előtte nem tudott?"

## Egy Egyszerű Demó, Amit Érdemes Fejben Tartani

Jó módszer az ügynökök tanulására, ha végigkövetünk egy demó ötletet a tanfolyamon.

Példa demó: **egy tanfolyam segítő ügynök**.

A felhasználó azt kéri:

> "Meg akarom tanulni, hogyan használják az ügynökök az eszközöket. Találd meg a
> megfelelő órákat, foglald össze, mit kell először elolvasnom, és adj nekem egy




1. **Olvassa vagy keresse át a tanfolyam fájlokat**, hogy megtalálja a megfelelő órákat.
2. **Használ eszközöket** az óralinkek, példák vagy kiegészítő anyagok lekérésére.
3. **Tervez** egy rövid tanulási útvonalat ahelyett, hogy egy hosszú választ adna.
4. **Használja az aktuális beszélgetés kontextusát**, hogy a tanuló céljára összpontosítson.
5. **Emlékezik hasznos beállításokra**, ha az alkalmazás támogatja a memóriát.
6. **Mutat nyomokat, idézeteket vagy naplókat**, hogy a felhasználó megértse, mi történt.
7. **Alkalmaz védőintézkedéseket** mielőtt kockázatos műveletet hajtana végre vagy érzékeny adatokat használna.

Ahogy tanulsz minden órát, térj vissza ehhez a demóhoz és kérdezd meg: milyen új képességet
adna ez az óra?

## Mire Törekszel

A tanfolyam végére képes leszel elmagyarázni és felépíteni olyan ügynök rendszereket,
amelyek az alábbi részeket kombinálják:

| Rész | Egyszerű magyarázat | A demóban |
|------|---------------------|------------|
| Modell | Az érvelő motor, amely értelmezi a felhasználó kérését | Megérti, hogy a tanuló eszközhasználati órákat akar |
| Eszközök | Funkciók, API-k, fájlok, böngészők vagy szolgáltatások, amelyeket az ügynök használhat | Keres a repóban vagy lekéri az óra tartalmat |
| Tudás | Dokumentumok vagy adatok, amelyekre a válasz alapul | Tanfolyami README fájlok és órák anyagai |
| Kontextus | Az a információ, amely a következő modell hívásban szerepel | A felhasználó célja és az eszközök eredményei |
| Memória | Későbbi használatra elmentett információ | A tanuló a gyakorlati Python példákat részesíti előnyben |
| Tervezés | Egy nagyobb cél lépésekre bontása | Megtalálja az órákat, összefoglalja őket, gyakorlati feladatot javasol |
| Szervezés | Munka irányítása eszközök, lépések vagy ügynökök között | Egy tervező hív egy kereső eszközt, majd egy összefoglalót |
| Bizalom | Biztonság, védelem, értékelés és megfigyelhetőség | Naplózza az eszközhívásokat és megkérdezi a felhasználót fontos lépések előtt |

## Modellek és Szolgáltatók

A tanfolyam kód példái a **Microsoft Agent Framework-öt (MAF)** használják és az

egyesíti a csevegési választ, eszközhívást, multimodális bemenetet és állapotfüggő beszélgetéseket egyetlen API felületen. Csatlakozhatsz egy **Microsoft Foundry**


Amint haladsz az órákon, több szolgáltató közül választhatsz:


- **Foundry Local** — a modelleket teljes egészében a készüléken futtató OpenAI-kompatibilis API (nincs felhő, nincs API kulcs). Ideális offline vagy költségmentes kísérletezéshez. Lásd a [Tanfolyam Beállítást](./00-course-setup/README.md).




## Válaszd ki a Tanulási Utadat

Teljes egészében végigcsinálhatod a kurzust sorrendben, vagy kiválaszthatod az érdeklődési körödnek megfelelő utat.

| Ha a célod az, hogy... | Kezdd ezzel | Aztán tanulj |
|-----------------------|------------|------------|
| Megértsd, mik azok az ügynökök | 01, 02, 03 | 04, 05, 06 |
| Készíts olyan ügynököt, amely eszközöket használ | 04 | 05, 07, 14 |
| Építs egy RAG alapú ügynököt | 05 | 04, 06, 12 |
| Tervezd meg az összetett munkafolyamatokat | 07 | 08, 09, 14 |
| Értsd meg a többügynökös rendszereket | 08 | 07, 09, 11 |
| Készülj fel az ügynökök éles bevetésére | 06, 10 | 12, 13, 16, 18 |
| Telepítsd és skálázd az ügynököket Foundry-n | 10, 16 | 06, 13, 18 |

| Fedezd fel a protokollokat és böngésző automatizálást | 11, 15 | 10, 18 |


szükséges szókincset a kurzus többi részéhez.

## Óránkénti Útmutató

| Óra | Amit megtanulsz | Próbáld ki az óra után |
|--------|----------------|---------------------------|
| [01 - Bevezetés az AI Ügynökökbe](./01-intro-to-ai-agents/README.md) | Mi különbözteti meg az ügynököt egy egyszerű chatbot-tól. | Magyarázd el a demó ötletedet ügynökként, ne csak chat alkalmazásként. |
| [02 - Ügynök Frameworkök](./02-explore-agentic-frameworks/README.md) | Hogyan segítenek a frameworkök a modellekben, eszközökben, állapotban és munkafolyamatokban. | Azonosítsd, a demód mely részeit kezelné egy framework. |
| [03 - Ügynök Tervezési Minták](./03-agentic-design-patterns/README.md) | Gyakori minták az ügynök viselkedés tervezéséhez. | Vázold fel a felhasználói utat kódírás előtt. |
| [04 - Eszközhasználat](./04-tool-use/README.md) | Hogyan hívnak eszközöket az ügynökök adatlekérésre vagy cselekvésre. | Határozz meg egy eszközt, amire a demódnak szüksége lenne. |
| [05 - Ügynök RAG](./05-agentic-rag/README.md) | Hogyan alapozzák az ügynök válaszokat dokumentumokra vagy adatokra. | Döntsd el, milyen tudásforrást keressen a demód. |
| [06 - Megbízható Ügynökök](./06-building-trustworthy-agents/README.md) | Hogyan adjunk hozzá védőintézkedéseket, felügyeletet és biztonságosabb viselkedést. | Adj hozzá egy szabályt, amikor az ügynöknek először a felhasználót kell megkérdeznie. |
| [07 - Tervezés](./07-planning-design/README.md) | Hogyan bontanak nagyobb célokat kisebb lépésekre az ügynökök. | Írj egy háromlépéses tervet a demó kérésedhez. |
| [08 - Többügynökös Tervezés](./08-multi-agent/README.md) | Mikor osszuk meg a munkát specializált ügynökök között. | Döntsd el, kell-e demódnak egy vagy több ügynök. |
| [09 - Metakogníció](./09-metacognition/README.md) | Hogyan értékelhetik és javíthatják ki az ügynökök saját eredményüket. | Adj hozzá egy végső önellenőrzést az ügynök válasza előtt. |
| [10 - AI Ügynökök Éles Használatban](./10-ai-agents-production/README.md) | Mi változik, amikor az ügynök demóból éles használatba lép. | Sorold fel, mit figyelnél: minőség, költség, válaszidő, hibák. |
| [11 - Ügynök Protokollok](./11-agentic-protocols/README.md) | Hogyan kapcsolódnak az ügynökök eszközökhöz és más ügynökökhöz protokollokon keresztül. | Azonosítsd, hol könnyíthet meg egy szabványos protokoll az integrációt. |
| [12 - Kontextus Tervezés](./12-context-engineering/README.md) | Hogyan válasszuk ki, vágjuk, izoláljuk és kezeljük a kontextust. | Döntsd el, mi kerüljön a promptba és mi maradjon ki. |
| [13 - Ügynök Memória](./13-agent-memory/README.md) | Hogyan menthetnek az ügynökök hasznos információkat interakciók között. | Válassz ki egy biztonságos beállítást, amit a demó megjegyezhet. |
| [14 - Microsoft Agent Framework](./14-microsoft-agent-framework/README.md) | Framework-specifikus építőelemek ügynökökhöz és munkafolyamatokhoz, valamint LangChain/LangGraph ügynökök hosztolása Microsoft Foundry-n. | Térképezd fel a demód lépéseit a framework fogalmakra. |
| [15 - Számítógép Használó Ügynökök](./15-browser-use/README.md) | Hogyan lépnek interakcióba az ügynökök böngésző vagy UI felületekkel, valós példákkal, mint a Microsoft Project Opal. | Válassz egy böngészési feladatot, amihez még mindig szükség van felhasználói jóváhagyásra. |
| [16 - Skálázható Ügynökök Telepítése](./16-deploying-scalable-agents/README.md) | Hogyan viszünk egy ügynököt prototípusról skálázható, megfigyelhető éles telepítésbe Microsoft Foundry-n (hosztolt ügynökök, modell irányítás, gyorsítótárazás, értékelő kapuk, füst tesztek). | Sorold fel azokat az éles üzemmel kapcsolatos kérdéseket, amikre demódnak még szüksége van: hosztolás, irányítás, költség, értékelés. |

| [18 - AI Ügynökök Biztonsága](./18-securing-ai-agents/README.md) | Hogyan tegyük az ügynök tevékenységeket auditálhatóvá és hamisításbiztossá. | Döntsd el, mely műveletek legyenek naplózva vagy bizonylatoltak a demódban. |

## Az Éles Ügynökök Validálása Füst Tesztekkel

Amikor telepítesz egy ügynököt (10. óra), egy **füst teszt** a legolcsóbb első
ellenőrzés, hogy a telepítés valóban válaszol-e. Ez a repó készen álló katalógusokat tartalmaz
a [tests/](./tests/README.md) alatt a 01, 04, 05 és 16. óra telepíthető ügynökeihez,
összekötve az [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) GitHub
Action-nel. Futtasd őket az **Actions** fülről az ügynök telepítése után.
A füst tesztek az első kapu — offline és online értékelés (10. és 16. óra)






Egy eszköz olyan dolog, amelyet az ügynök hívhat, hogy a modellen kívüli munkát végezzen. Egy jó eszköznek
tiszta neve, szűk feladata, típusos bemenetei, kiszámítható kimenete és biztonságos hibakezelése van.

A tanfolyam segítő demóban egy eszköz lehet:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG és Tudás

A RAG segít az ügynöknek a forrásanyagból válaszolni a találgatás helyett. Ebben a
tanfolyamban a forrásanyag lehet az órai README-k, kód példák vagy az órákból hivatkozott külső
erőforrások.

Használj RAG-ot, ha a válasznak dokumentumokban, adatokban vagy aktuális
projekt fájlokban kell megalapozottnak lennie.

### Tervezés

A tervezés hasznos, ha a kérés több lépésből áll. Tartsd a terveket rövidnek és
elég láthatónak ahhoz, hogy egy fejlesztő vagy felhasználó megvizsgálhassa.

A demóban egy terv lehet:

1. Keress eszközhasználathoz kapcsolódó órákat.
2. Foglald össze a legfontosabb órákat.
3. Javasolj egy gyakorló feladatot.

### Kontextus

A kontextus az, amit a modell éppen lát. Túl kevés kontextus hiányossá teszi az ügynököt
fontos részletekben. Túl sok kontextus lassabbá, költségesebbé,
vagy könnyebben összezavarhatóvá teheti az ügynököt.

A jó kontextus-tervezés azt jelenti, hogy a következő modell híváshoz a megfelelő információt választod ki.




mentsd el, amelyek hasznosak, biztonságosak, és könnyen frissíthetők vagy törölhetők.


Például hasznos lehet megjegyezni, hogy "a tanuló a Python példákat részesíti előnyben".
Általában nem célszerű érzékeny személyes adatokat megőrizni.

### Értékelés és Megfigyelhetőség

Az értékelés arra kérdez rá: az ügynök a helyes dolgot tette-e?

A megfigyelhetőség pedig arra: láthatjuk-e, hogyan történt?

Éles ügynökök esetén kövesd nyomon a modell hívásokat, eszköz hívásokat, előhívott kontextust,
válaszidőt, költséget, hibákat és a felhasználói visszajelzéseket.

### Bizalom és Biztonság

A megbízható ügynökök több kell, mint egy segítőkész prompt. Használj a lehető legkisebb jogosultságú eszközöket,
emberi jóváhagyást a nagy hatású műveletek előtt, adatredakciót ahol szükséges, és naplókat vagy
bizonylatokat az auditálandó műveletekhez.

## 15 perces Áttekintési Rutin

Használd ezt a rutint minden óra után:

1. **Foglald össze az órát egyetlen mondatban.**
2. **Nevezd meg az új ügynök képességet.** Például: eszközhasználat, előhívás,
   tervezés, memória, megfigyelhetőség, vagy biztonság.
3. **Add hozzá a tanfolyam segítő demóhoz.** Mi változik most a demóban?
4. **Találd meg a kockázatot.** Mi mehet félre, ha ezt a képességet rosszul használják?
5. **Írj egy tesztkérdést.** Hogyan ellenőriznéd, hogy az ügynök jól viselkedik-e?

## Gyors Önellenőrzés

Mielőtt tovább mennél, próbáld megválaszolni ezeket a kérdéseket:

1. Mit tud egy ügynök, amit egy sima chatbot maga nem tud?
2. Melyik eszközre lenne először szüksége az ügynöködnek, és miért?
3. Milyen tudásforrásra kell alapoznia az ügynök válaszának?
4. Milyen kontextusnak kell szerepelnie a következő modell hívásban?
5. Mit kell az ügynöknek megjegyeznie, és mit kell elkerülnie a tárolásban?
6. Mikor kell az ügynöknek emberi jóváhagyást kérnie?
7. Milyen naplók, nyomok vagy bizonylatok segítenének később az ügynök hibakeresésében vagy auditálásában?


## Javasolt záró feladat

A tanfolyam végén építs egy kis ügynököt, amely segít a tanulónak eligazodni ebben a
tárolóban.

Minimális verzió:

- Fogadjon témát a felhasználótól.
- Keresse meg a legrelevánsabb leckéket.
- Összefoglalja, mit kell először elolvasni.
- Javasoljon egy gyakorlati feladatot.
- Mutassa meg, mely leckefájlokat vagy hivatkozásokat használták.

Fejlettebb verzió:

- Emlékezzen a tanuló preferált programozási nyelvére.
- Használjon egyszerű tervet a válaszadás előtt.
- Adjon hozzá önellenőrző lépést a végső válasz előtt.
- Naplózza az eszközhívásokat és a lekért forrásokat.
- Kérje megerősítést, mielőtt megnyitja a böngészőt vagy UI automatizálási feladatokat indít.

Ez egy kis, de valósághű módot ad eszközök, RAG, tervezés,
kontextus, memória, megfigyelhetőség és bizalom gyakorlására egyetlen projektben.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->