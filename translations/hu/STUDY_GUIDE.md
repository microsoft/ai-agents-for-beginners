# AI ügynökök kezdőknek – Tanulmányi útmutató

Használd ezt az útmutatót gyakorlati kísérőként, miközben végighaladsz a tanfolyamon. Ez
nem a leckék helyettesítésére szolgál. Segít eldönteni, hol kezdj, mit
keress az egyes leckékben, és hogyan kapcsolhatod össze az ötleteket egy kis, működőképes
ügynök demóvá.

Ha itt jársz először, kezd egyszerűen:

1. Olvasd el a [Tanfolyam beállítása](./00-course-setup/README.md) részt.
2. Teljesítsd sorban az 01–06. leckéket.
3. Tarts szem előtt egy kis demóötletet, miközben tanulsz.
4. Minden lecke után tedd fel a kérdést: „Mit tud most az ügynököm, amit korábban
   nem tudott?”

## Egy egyszerű demó, amire gondolj

Jó tanulási mód, ha egy demóötletet követünk végig a tanfolyamon.

Példa demó: **egy tanfolyam segítő ügynök**.

A felhasználó ezt kérdezi:

> „Szeretném megtanulni, hogyan használnak az ügynökök eszközöket. Találd meg a megfelelő leckéket, foglald össze, mit
> kell először elolvasnom, és adj nekem egy rövid gyakorlati feladatot.”

Egy hagyományos chatbot az eddigi tudásából válaszol. Egy ügynök többre képes:

1. **Olvassa vagy keresi a tanfolyam fájljait**, hogy megtalálja a megfelelő leckéket.
2. **Eszközöket használ**, hogy lekérje a leckék linkjeit, példákat vagy kiegészítő anyagokat.
3. **Tervez** egy rövid tanulási útvonalat egy hosszú válasz helyett.
4. **Használja a kontextust** a jelenlegi beszélgetésből, hogy a tanuló céljára fókuszáljon.
5. **Emlékszik a hasznos beállításokra**, ha a alkalmazás támogatja a memóriát.
6. **Mutatja a nyomokat, hivatkozásokat vagy naplókat**, hogy a felhasználó megértse, mi történt.
7. **Alkalmaz védőkorlátokat**, mielőtt kockázatos lépéseket tenne vagy érzékeny adatokat használna.


adna hozzá ez a lecke?




amelyek ezeket az alkotóelemeket ötvözik:


|----------|-------------------------|-----------|
| Modell | Az a következtető motor, amely értelmezi a felhasználó kérését | Megérti, hogy a tanuló eszközhasználati leckéket akar |
| Eszközök | Funkciók, API-k, fájlok, böngészők vagy szolgáltatások, amelyeket az ügynök használhat | Keres a tárházban vagy lekéri a lecke tartalmát |
| Tudás | Dokumentumok vagy adatok, amelyek megalapozzák a választ | Tanfolyam README fájlok és lecke anyagok |
| Kontextus | Az információ, amelyet a következő modell hívásban használnak | A felhasználó célja és az eszközök eredményei |
| Memória | A későbbi használatra mentett információ | A tanuló a gyakorlati Python példákat részesíti előnyben |
| Tervezés | Egy nagyobb cél kisebb lépésekre bontása | Talál leckéket, foglalja össze őket, javasol gyakorlatot |
| Szervezés | Munka továbbítása eszközök, lépések vagy ügynökök között | Egy tervező meghív egy keresőeszközt, majd egy összefoglalót |
| Bizalom | Biztonság, védelem, értékelés és megfigyelhetőség | Naplózza az eszközhasználatot, és kérdez nagy hatású lépések előtt |




**Azure OpenAI Responses API**-ra céloznak — a jövőbeni ajánlott API, amely egyesíti a chat befejezéseket, eszközhívást, multimodális bemenetet és állapotú beszélgetéseket egyetlen API felületen. Csatlakozhatsz vagy a **Microsoft Foundry** projekten keresztül (`FoundryChatClient`), vagy közvetlenül az Azure OpenAI-hoz (`OpenAIChatClient`).

Ahogy haladsz a leckékkel, néhány szolgáltató közül választhatsz:

- **Microsoft Foundry / Azure OpenAI (Responses API)** — a tanfolyamok fő útvonala. Jelentkezz be `az login`-nal kulcs nélküli Entra ID hitelesítéshez.
- **Foundry Local** — futtass modelleket teljesen helyileg OpenAI-kompatibilis API-n keresztül (nem felhő, nincs API-kulcs). Ideális offline vagy költségmentes kísérletezéshez. Lásd a [Tanfolyam beállítását](./00-course-setup/README.md).
- **MiniMax** — OpenAI-kompatibilis szolgáltató nagy kontextusú modellekkel, drop-in alternatívaként használható.

> **Megjegyzés:** A GitHub modellek elavultak (2026 júliusában megszűnnek) és nem támogatják a Responses API-t. A kódminták Azure OpenAI / Microsoft Foundry használatára frissültek.

## Válaszd ki a tanulási utadat

A teljes tanfolyamot végigcsinálhatod sorrendben, vagy ugorhatsz az érdeklődésed szerinti útra,
amit építeni szeretnél.

| Ha a célod... | Kezdd ezzel | Aztán tanulmányozd ezt |
|--------------|--------------|---------------------|
| Megérteni, mik azok az ügynökök | 01, 02, 03 | 04, 05, 06 |
| Készíteni egy eszközhasználó ügynököt | 04 | 05, 07, 14 |
| Készíteni egy RAG alapú ügynököt | 05 | 04, 06, 12 |
| Többlépcsős munkafolyamatokat tervezni | 07 | 08, 09, 14 |
| Megérteni a többügynökös rendszereket | 08 | 07, 09, 11 |
| Ügynököket előkészíteni éles üzemre | 06, 10 | 12, 13, 18 |
| Protokollokat és böngésző automatizálást felfedezni | 11, 15 | 10, 18 |

Tipp: ha új vagy az ügynökök világában, ne hagyd ki az 01–06. leckéket. Ezek adják
azt a szókincset, amire a tanfolyam többi részéhez szükséged lesz.

## Leckénkénti útmutató

| Lecke | Amit tanulsz | Próbáld ki a lecke után |
|-------|--------------|---------------------|
| [01 - Bevezetés az AI ügynökökbe](./01-intro-to-ai-agents/README.md) | Mi különbözteti meg az ügynököt az alap chatbottól. | Magyarázd el a demóötleted ügynökként, ne csak chat appként. |
| [02 - Ügynöki keretrendszerek](./02-explore-agentic-frameworks/README.md) | Hogyan segítik a keretrendszerek a modelleket, eszközöket, állapotot és munkafolyamatokat. | Azonosítsd be, mit kezelne a keretrendszer a demódban. |
| [03 - Ügynöki tervezési minták](./03-agentic-design-patterns/README.md) | Gyakori minták az ügynök viselkedésének tervezéséhez. | Vázold fel a felhasználói utat a kódírás előtt. |
| [04 - Eszközhasználat](./04-tool-use/README.md) | Hogyan hívják az ügynökök az eszközöket adatok lekérésére vagy lépések megtételére. | Határozz meg egy eszközt, amire a demó ügynöködnek szüksége lenne. |
| [05 - Ügynöki RAG](./05-agentic-rag/README.md) | Hogyan alapozzák meg a lekérdezések az ügynök válaszait dokumentumok vagy adatok alapján. | Döntsd el, mit kell keresnie a demód tudásforrásai között. |
| [06 - Megbízható ügynökök](./06-building-trustworthy-agents/README.md) | Hogyan adj védőkorlátokat, felügyeletet és biztonságosabb viselkedést. | Adj hozzá egy szabályt, hogy mikor kérdezze meg először a felhasználót. |
| [07 - Tervezési minta](./07-planning-design/README.md) | Hogyan bontják az ügynökök a nagyobb célokat kisebb lépésekre. | Írj egy háromlépéses tervet a demó kérésedhez. |

| [08 - Többügynökös tervezés](./08-multi-agent/README.md) | Mikor osszuk fel a munkát specializált ügynökök között. | Döntsd el, hogy a demódhoz egy vagy több ügynökre van-e szükség. |
| [09 - Metakogníció](./09-metacognition/README.md) | Hogyan vizsgálhatják felül és javíthatják saját teljesítményüket az ügynökök. | Adj hozzá egy végső önellenőrzést, mielőtt az ügynök válaszol. |
| [10 - MI ügynökök éles környezetben](./10-ai-agents-production/README.md) | Mi változik, amikor egy ügynök a demóból éles környezetbe kerül. | Sorold fel, mit figyelnél: minőség, költség, késleltetés, hibák. |
| [11 - Ügynöki protokollok](./11-agentic-protocols/README.md) | Hogyan kapcsolják a protokollok az ügynököket eszközökhöz és más ügynökökhöz. | Azonosítsd, hol egyszerűsíthetné egy szabványos protokoll az integrációt. |
| [12 - Kontextus mérnökség](./12-context-engineering/README.md) | Hogyan válasszuk ki, vágjuk le, izoláljuk és kezeljük a kontextust. | Döntsd el, mi tartozik az utasításba, és mi maradjon ki. |
| [13 - Ügynök memória](./13-agent-memory/README.md) | Hogyan menthetnek az ügynökök hasznos információkat az interakciók között. | Válassz ki egy biztonságos preferenciát, amit a demód megjegyezhet. |
| [14 - Microsoft Agent Framework](./14-microsoft-agent-framework/README.md) | Keret specifikus építőelemek ügynökökhöz és munkafolyamatokhoz, plusz LangChain/LangGraph ügynökök hosztolása a Microsoft Foundry-n. | Térképezd fel a demó lépéseit a keret koncepcióira. |
| [15 - Számítógép Használati Ügynökök](./15-browser-use/README.md) | Hogyan léphetnek kapcsolatba az ügynökök böngésző vagy UI felületekkel, beleértve valós példákat, mint a Microsoft Project Opal. | Válassz ki egy böngésző feladatot, amihez még mindig szükség van felhasználói megerősítésre. |
| [18 - MI Ügynökök Biztonsága](./18-securing-ai-agents/README.md) | Hogyan tehető az ügynöki műveletek átláthatóbbá és manipulációval szemben ellenállóbbá. | Döntsd el, mely műveleteket kell naplózni vagy visszaigazolni a demóban. |

A 16. és 17. leckék a fő README-ben hamarosan érkeznekként szerepelnek. Add hozzá őket a
tanulási tervedhez, amikor elérhetővé válnak a leckék tartalmai.

## Lényeges Fogalmak Kezdőbarát Megfogalmazásban

### Eszközök

Az eszköz valami, amit az ügynök hívhat, hogy a modellen kívül végezzen munkát. Egy jó eszköz
világos nevű, szűk feladatkörű, típusos bemenettel, kiszámítható kimenettel és biztonságos
hibakezeléssel rendelkezik.

A kurzus segítő demójában például egy eszköz lehet:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG és Tudás

A RAG segíti az ügynököt, hogy forrásanyagból válaszoljon a találgatás helyett. Ebben a
kurzusban a forrásanyag lehet lecke README-k, kódminták vagy a leckékhez kapcsolódó külső
erőforrások.

Használd a RAG-et, amikor a válasznak dokumentumokon, adatokon vagy aktuális
projektfájlokon kell alapulnia.

### Tervezés

A tervezés akkor hasznos, ha a kérés több lépésből áll. Tartsd a terveket röviden és
elég átláthatóan a fejlesztő vagy felhasználó számára.

A demóban egy terv lehet például:

1. Keress eszközhasználathoz kapcsolódó leckéket.
2. Foglald össze a legfontosabb leckéket.
3. Javasolj egy gyakorlati feladatot.

### Kontextus

A kontextus az, amit a modell éppen lát. Ha túl kevés a kontextus, az ügynök lényeges
részleteket hiányolhat. Ha túl sok, az lassabbá, költségesebbé vagy könnyebben összezavarhatóvá
teszi az ügynököt.

A jó kontextusmérnökség azt jelenti, hogy a következő modell híváshoz a megfelelő
információkat választjuk ki.

### Memória

A memória későbbre mentett információ. Ne ments el mindent. Csak azokat az infókat
tárold, amelyek hasznosak, biztonságosak, és könnyen frissíthetők vagy törölhetők.

Például hasznos lehet megjegyezni, hogy "a tanuló előnyben részesíti a Python példákat".
Személyes, érzékeny adatokat általában nem érdemes megjegyezni.

### Értékelés és Megfigyelhetőség

Az értékelés azt kérdezi: helyesen cselekedett-e az ügynök?

A megfigyelhetőség azt, hogy látható-e, hogyan történt mindez?

Éles környezetben kövesd nyomon a modellhívásokat, eszközhasználatot, visszakeresett kontextust,
késleltetést, költséget, hibákat és a felhasználói visszajelzéseket.

### Bizalom és Biztonság

A megbízható ügynökök több kell, mint egy hasznos utasítás. Használj minimális jogosultságú eszközöket,
emberi jóváhagyást nagy kockázatú műveletekhez, adatredakciót szükség esetén, és
naplókat vagy visszaigazolásokat az ellenőrizendő műveletekhez.

## Egy 15 Perces Áttekintő Rutin

Használd ezt a rutint minden lecke után:

1. **Foglald össze a leckét egy mondatban.**
2. **Nevezd meg az új ügynöki képességet.** Például: eszközhasználat, visszakeresés,
   tervezés, memória, megfigyelhetőség vagy biztonság.
3. **Add hozzá a kurzus segítő demóhoz.** Mi változik most a demóban?
4. **Találd meg a kockázatot.** Mi mehet rosszul, ha ezt a képességet rosszul használják?
5. **Írj egy tesztkérdést.** Hogyan ellenőriznéd, hogy az ügynök jól viselkedik-e?

## Gyors Önellenőrzés

Mielőtt továbbmennél, próbáld megválaszolni ezeket a kérdéseket:

1. Mit tud egy ügynök, amit egy átlagos chatbot nem tud önmagától?
2. Milyen eszközre lenne először szüksége az ügynöködnek, és miért?
3. Milyen tudásforrásnak kell megalapoznia az ügynök válaszát?
4. Milyen kontextust kell belefoglalni a következő modell hívásba?
5. Mit kell az ügynöknek megjegyeznie, és mit kell elkerülnie a tárolás során?
6. Mikor kell az ügynöknek emberi jóváhagyást kérnie?
7. Milyen naplók, nyomok vagy visszaigazolások segítenék a későbbi hibakeresést vagy ellenőrzést?

## Javasolt Zárógyakorlat

A kurzus végén építs egy kis ügynököt, amely segíti a tanulót ebben a
tárházban való eligazodásban.

Minimális verzió:

- Fogadjon egy témát a felhasználótól.
- Keresse meg a legrelevánsabb leckéket.
- Foglalja össze, mit kell először elolvasni.
- Javasoljon egy gyakorlati feladatot.
- Mutassa meg, mely lecke fájlokat vagy linkeket használta.

Kiterjesztett verzió:

- Jegyezze meg a tanuló előnyben részesített programozási nyelvét.
- Használjon egyszerű tervet a válaszadás előtt.
- Adjon hozzá egy önellenőrző lépést a végső válasz előtt.
- Naplózza az eszközhívásokat és a visszakeresett forrásokat.
- Kérjen megerősítést, mielőtt böngésző vagy UI automatizációs feladatokat indít.

Ez egy kicsi, de valósághű módot ad a gyakorlásra eszközök, RAG, tervezés,
kontextus, memória, megfigyelhetőség és bizalom témákban egyetlen projektben.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->