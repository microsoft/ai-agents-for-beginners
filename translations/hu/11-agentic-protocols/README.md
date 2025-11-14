<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aff92c6f019b4627ca9399c6e3882e17",
  "translation_date": "2025-09-18T15:27:02+00:00",
  "source_file": "11-agentic-protocols/README.md",
  "language_code": "hu"
}
-->
# Agentikus protokollok használata (MCP, A2A és NLWeb)

[![Agentikus protokollok](../../../translated_images/lesson-11-thumbnail.b6c742949cf1ce2aa0255968d287b31c99b51dfa9c9beaede7c3fbed90e8fcfb.hu.png)](https://youtu.be/X-Dh9R3Opn8)

> _(Kattints a fenti képre a leckéhez tartozó videó megtekintéséhez)_

Ahogy az AI ügynökök használata növekszik, úgy nő az igény olyan protokollokra, amelyek biztosítják a szabványosítást, a biztonságot és támogatják a nyílt innovációt. Ebben a leckében három protokollt vizsgálunk meg, amelyek ezt a célt szolgálják: Model Context Protocol (MCP), Agent to Agent (A2A) és Natural Language Web (NLWeb).

## Bevezetés

Ebben a leckében az alábbiakat tárgyaljuk:

• Hogyan teszi lehetővé az **MCP**, hogy az AI ügynökök külső eszközökhöz és adatokhoz férjenek hozzá a felhasználói feladatok elvégzéséhez.

• Hogyan biztosítja az **A2A** az AI ügynökök közötti kommunikációt és együttműködést.

• Hogyan hozza el az **NLWeb** a természetes nyelvi interfészeket bármely weboldalra, lehetővé téve az AI ügynökök számára, hogy felfedezzék és interakcióba lépjenek a tartalommal.

## Tanulási célok

• **Azonosítani** az MCP, A2A és NLWeb alapvető célját és előnyeit az AI ügynökök kontextusában.

• **Elmagyarázni**, hogyan segíti mindegyik protokoll az LLM-ek, eszközök és más ügynökök közötti kommunikációt és interakciót.

• **Felismerni**, hogy milyen külön szerepeket töltenek be ezek a protokollok az összetett ügynöki rendszerek építésében.

## Model Context Protocol

A **Model Context Protocol (MCP)** egy nyílt szabvány, amely szabványosított módot biztosít az alkalmazások számára, hogy kontextust és eszközöket biztosítsanak az LLM-ek számára. Ez lehetővé teszi egy "univerzális adaptert" különböző adatforrásokhoz és eszközökhöz, amelyhez az AI ügynökök konzisztens módon csatlakozhatnak.

Nézzük meg az MCP összetevőit, az API közvetlen használatához képest nyújtott előnyöket, és egy példát arra, hogyan használhatnak az AI ügynökök egy MCP szervert.

### MCP alapvető összetevői

Az MCP **kliens-szerver architektúrán** működik, és az alapvető összetevői a következők:

• **Hostok**: Olyan LLM alkalmazások (például egy kódszerkesztő, mint a VSCode), amelyek kapcsolatot kezdeményeznek egy MCP szerverrel.

• **Kliensek**: Az alkalmazáson belüli komponensek, amelyek egy-egy kapcsolatot tartanak fenn a szerverekkel.

• **Szerverek**: Könnyű programok, amelyek specifikus képességeket biztosítanak.

A protokoll három alapvető primitívet tartalmaz, amelyek az MCP szerver képességei:

• **Eszközök**: Ezek diszkrét műveletek vagy funkciók, amelyeket egy AI ügynök hívhat meg egy művelet végrehajtásához. Például egy időjárási szolgáltatás kínálhat egy "get weather" eszközt, vagy egy e-kereskedelmi szerver egy "purchase product" eszközt. Az MCP szerverek hirdetik az egyes eszközök nevét, leírását és bemeneti/kimeneti sémáját a képességek listájában.

• **Erőforrások**: Ezek csak olvasható adatokat vagy dokumentumokat jelentenek, amelyeket egy MCP szerver biztosíthat, és amelyeket a kliensek igény szerint lekérhetnek. Példák: fájltartalom, adatbázis-rekordok vagy naplófájlok. Az erőforrások lehetnek szövegesek (például kód vagy JSON) vagy binárisak (például képek vagy PDF-ek).

• **Promptok**: Ezek előre definiált sablonok, amelyek javasolt promptokat biztosítanak, lehetővé téve összetettebb munkafolyamatokat.

### MCP előnyei

Az MCP jelentős előnyöket kínál az AI ügynökök számára:

• **Dinamikus eszközfelfedezés**: Az ügynökök dinamikusan kaphatnak listát a szerver által elérhető eszközökről, valamint azok leírásáról. Ez szemben áll a hagyományos API-kkal, amelyek gyakran statikus kódolást igényelnek az integrációkhoz, ami azt jelenti, hogy bármilyen API-változás kódfrissítést igényel. Az MCP egy "egyszeri integráció" megközelítést kínál, ami nagyobb alkalmazkodóképességet eredményez.

• **Interoperabilitás az LLM-ek között**: Az MCP különböző LLM-ekkel működik, rugalmasságot biztosítva a fő modellek cseréjéhez a jobb teljesítmény érdekében.

• **Szabványosított biztonság**: Az MCP szabványos hitelesítési módszert tartalmaz, javítva a skálázhatóságot, amikor további MCP szerverekhez való hozzáférést adunk hozzá. Ez egyszerűbb, mint különböző kulcsok és hitelesítési típusok kezelése a hagyományos API-k esetében.

### MCP példa

![MCP Diagram](../../../translated_images/mcp-diagram.e4ca1cbd551444a12e1f0eb300191a036ab01124fce71c864fe9cb7f4ac2a15d.hu.png)

Képzeljük el, hogy egy felhasználó repülőjegyet szeretne foglalni egy MCP által működtetett AI asszisztens segítségével.

1. **Kapcsolat**: Az AI asszisztens (az MCP kliens) csatlakozik egy légitársaság által biztosított MCP szerverhez.

2. **Eszközfelfedezés**: A kliens megkérdezi a légitársaság MCP szerverét: "Milyen eszközök állnak rendelkezésre?" A szerver válaszol olyan eszközökkel, mint "search flights" és "book flights".

3. **Eszköz meghívása**: Ezután megkérdezed az AI asszisztenst: "Kérlek, keress egy repülőjáratot Portlandből Honoluluba." Az AI asszisztens, az LLM segítségével, azonosítja, hogy meg kell hívnia a "search flights" eszközt, és átadja a releváns paramétereket (kiindulási hely, célállomás) az MCP szervernek.

4. **Végrehajtás és válasz**: Az MCP szerver, mint egy wrapper, ténylegesen hívja a légitársaság belső foglalási API-ját. Ezután megkapja a járatinformációkat (például JSON adatokat), és visszaküldi az AI asszisztensnek.

5. **További interakció**: Az AI asszisztens bemutatja a járatopciókat. Miután kiválasztasz egy járatot, az asszisztens meghívhatja a "book flight" eszközt ugyanazon MCP szerveren, befejezve a foglalást.

## Agent-to-Agent Protocol (A2A)

Míg az MCP az LLM-ek és eszközök összekapcsolására összpontosít, az **Agent-to-Agent (A2A) protokoll** egy lépéssel tovább megy, lehetővé téve a különböző AI ügynökök közötti kommunikációt és együttműködést. Az A2A összekapcsolja az AI ügynököket különböző szervezetek, környezetek és technológiai stackek között, hogy közösen teljesítsenek egy feladatot.

Vizsgáljuk meg az A2A összetevőit és előnyeit, valamint egy példát arra, hogyan alkalmazható a mi utazási alkalmazásunkban.

### A2A alapvető összetevői

Az A2A az ügynökök közötti kommunikációt és együttműködést helyezi előtérbe, hogy egy felhasználói részfeladatot elvégezzenek. A protokoll minden összetevője hozzájárul ehhez:

#### Ügynökkártya

Hasonlóan ahhoz, ahogy egy MCP szerver megosztja az eszközök listáját, egy ügynökkártya tartalmazza:
- Az ügynök nevét.
- **Általános feladatok leírását**, amelyeket elvégez.
- **Specifikus készségek listáját** leírásokkal, hogy más ügynökök (vagy akár emberi felhasználók) megértsék, mikor és miért érdemes az ügynököt hívni.
- Az ügynök **aktuális végpont URL-jét**.
- Az ügynök **verzióját** és **képességeit**, például streaming válaszokat és push értesítéseket.

#### Ügynökvégrehajtó

Az ügynökvégrehajtó felelős azért, hogy **átadja a felhasználói chat kontextusát a távoli ügynöknek**, amelynek szüksége van erre, hogy megértse a végrehajtandó feladatot. Egy A2A szerverben az ügynök saját Nagy Nyelvi Modelljét (LLM) használja a bejövő kérések elemzésére és a feladatok végrehajtására saját belső eszközeivel.

#### Artefaktum

Miután egy távoli ügynök elvégezte a kért feladatot, munkájának eredménye artefaktumként jön létre. Az artefaktum **tartalmazza az ügynök munkájának eredményét**, egy **leírást arról, hogy mi készült el**, és a **szöveges kontextust**, amelyet a protokollon keresztül küldtek. Az artefaktum elküldése után a kapcsolat a távoli ügynökkel lezárul, amíg újra szükség nem lesz rá.

#### Eseménysor

Ez az összetevő **frissítések kezelésére és üzenetek továbbítására** szolgál. Különösen fontos a termelésben az ügynöki rendszerek számára, hogy megakadályozza az ügynökök közötti kapcsolat lezárását, mielőtt egy feladat befejeződik, különösen akkor, ha a feladat végrehajtási ideje hosszabb lehet.

### A2A előnyei

• **Fokozott együttműködés**: Lehetővé teszi különböző gyártók és platformok ügynökei számára, hogy interakcióba lépjenek, megosszák a kontextust és együtt dolgozzanak, megkönnyítve a zökkenőmentes automatizálást a hagyományosan elkülönült rendszerek között.

• **Modellválasztási rugalmasság**: Minden A2A ügynök eldöntheti, hogy melyik LLM-et használja a kérések kiszolgálására, lehetővé téve az optimalizált vagy finomhangolt modellek használatát ügynökönként, ellentétben az egyetlen LLM kapcsolattal néhány MCP esetben.

• **Beépített hitelesítés**: A hitelesítés közvetlenül az A2A protokollba van integrálva, robusztus biztonsági keretet biztosítva az ügynökök közötti interakciókhoz.

### A2A példa

![A2A Diagram](../../../translated_images/A2A-Diagram.8666928d648acc2687db4093d7b09ea2a595622f8fe18194a026ee55fc23af8e.hu.png)

Bővítsük ki az utazási foglalási forgatókönyvet, de ezúttal az A2A használatával.

1. **Felhasználói kérés több ügynökhöz**: Egy felhasználó interakcióba lép egy "Utazási Ügynök" A2A kliens/ügynökkel, például így: "Kérlek, foglalj egy teljes utazást Honoluluba jövő hétre, beleértve a repülőjegyeket, egy szállodát és egy bérautót."

2. **Orkesztráció az Utazási Ügynök által**: Az Utazási Ügynök megkapja ezt az összetett kérést. Az LLM segítségével elemzi a feladatot, és meghatározza, hogy más specializált ügynökökkel kell interakcióba lépnie.

3. **Ügynökök közötti kommunikáció**: Az Utazási Ügynök az A2A protokollt használja, hogy kapcsolatba lépjen alárendelt ügynökökkel, például egy "Légitársasági Ügynökkel", egy "Szállodai Ügynökkel" és egy "Autókölcsönző Ügynökkel", amelyeket különböző cégek hoztak létre.

4. **Feladatok delegálása**: Az Utazási Ügynök specifikus feladatokat küld ezeknek a specializált ügynököknek (például "Keress járatokat Honoluluba", "Foglalj szállodát", "Bérelj autót"). Mindegyik specializált ügynök, saját LLM-eket futtatva és saját eszközeit használva (amelyek maguk is MCP szerverek lehetnek), elvégzi a foglalás specifikus részét.

5. **Összesített válasz**: Miután az összes alárendelt ügynök elvégezte a feladatát, az Utazási Ügynök összeállítja az eredményeket (járatinformációk, szállodai visszaigazolás, autókölcsönzési foglalás), és egy átfogó, chat-stílusú választ küld vissza a felhasználónak.

## Natural Language Web (NLWeb)

A weboldalak régóta az elsődleges módjai annak, hogy a felhasználók információkhoz és adatokhoz férjenek hozzá az interneten.

Nézzük meg az NLWeb különböző összetevőit, az NLWeb előnyeit és egy példát arra, hogyan működik az NLWeb az utazási alkalmazásunkban.

### Az NLWeb összetevői

- **NLWeb alkalmazás (alapszolgáltatás kódja)**: Az a rendszer, amely feldolgozza a természetes nyelvi kérdéseket. Összekapcsolja a platform különböző részeit, hogy válaszokat hozzon létre. Gondolj rá úgy, mint a weboldal természetes nyelvi funkcióit működtető **motorra**.

- **NLWeb protokoll**: Ez egy **alapvető szabályrendszer a természetes nyelvi interakcióhoz** egy weboldallal. JSON formátumban küld vissza válaszokat (gyakran Schema.org használatával). Célja, hogy egyszerű alapot teremtsen az "AI Web"-hez, ugyanúgy, ahogy a HTML lehetővé tette az online dokumentumok megosztását.

- **MCP szerver (Model Context Protocol végpont)**: Minden NLWeb beállítás egyben **MCP szerverként** is működik. Ez azt jelenti, hogy **eszközöket (például egy "ask" metódust) és adatokat** oszthat meg más AI rendszerekkel. Gyakorlatban ez lehetővé teszi, hogy a weboldal tartalma és képességei az AI ügynökök számára is elérhetők legyenek, így a weboldal a szélesebb "ügynöki ökoszisztéma" részévé válik.

- **Beágyazási modellek**: Ezeket a modelleket arra használják, hogy **a weboldal tartalmát numerikus reprezentációkká, azaz vektorokká alakítsák** (beágyazások). Ezek a vektorok olyan jelentést hordoznak, amelyet a számítógépek össze tudnak hasonlítani és keresni. Egy speciális adatbázisban tárolják őket, és a felhasználók kiválaszthatják, hogy melyik beágyazási modellt szeretnék használni.

- **Vektoradatbázis (visszakeresési mechanizmus)**: Ez az adatbázis **a weboldal tartalmának beágyazásait tárolja**. Amikor valaki kérdést tesz fel, az NLWeb ellenőrzi a vektoradatbázist, hogy gyorsan megtalálja a legrelevánsabb információkat. Gyors listát ad a lehetséges válaszokról, hasonl

---

**Felelősség kizárása**:  
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével lett lefordítva. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális, emberi fordítást igénybe venni. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely a fordítás használatából eredhet.