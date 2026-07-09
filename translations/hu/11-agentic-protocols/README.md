# Ágens Protokollok használata (MCP, A2A és NLWeb)

[![Ágens Protokollok](../../../translated_images/hu/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Kattintson a fenti képre a leckéhez tartozó videó megtekintéséhez)_

Ahogy az MI ágens használata növekszik, úgy nő az igény az olyan protokollokra, amelyek biztosítják a szabványosítást, a biztonságot és támogatják a nyílt innovációt. Ebben a leckében három ilyen protokollt tárgyalunk, amelyek ezt az igényt kívánják kielégíteni – Model Context Protocol (MCP), Agent to Agent (A2A) és Natural Language Web (NLWeb).

## Bevezetés

Ebben a leckében áttekintjük:

• Hogyan teszi lehetővé az **MCP**, hogy az MI ágensek külső eszközökhöz és adatokhoz férjenek hozzá a felhasználói feladatok elvégzéséhez.

• Hogyan teszi lehetővé az **A2A** a különböző MI ágensek közötti kommunikációt és együttműködést.

• Hogyan hoz az **NLWeb** természetes nyelvi felületeket bármely weboldalra, lehetővé téve az MI ágensek számára a tartalom felfedezését és interakcióját.

## Tanulási célok

• **Azonosítsa** az MCP, A2A és NLWeb fő célját és előnyeit az MI ágensek kontextusában.

• **Magyarázza el**, hogyan segíti elő mindegyik protokoll az LLM-ek, eszközök és más ágensek közti kommunikációt és interakciót.

• **Ismerje fel** az egyes protokollok egyedi szerepét a komplex ágens rendszerek kiépítésében.

## Model Context Protocol

A **Model Context Protocol (MCP)** egy nyílt szabvány, amely egységes módot kínál alkalmazásoknak az LLM-eknek kontextus és eszközök biztosítására. Ez lehetővé teszi egy "univerzális adapter" létrejöttét különböző adatforrásokhoz és eszközökhöz, amelyekhez az MI ágensek következetesen csatlakozhatnak.

Nézzük meg az MCP összetevőit, az előnyeit a közvetlen API használathoz képest, és egy példát arra, hogyan használhatnak MI ágensek egy MCP szervert.

### Az MCP alapvető elemei

Az MCP **kliens-szerver architektúrán** alapul, és az alapvető elemei:

• **Hosztok** olyan LLM alkalmazások (például egy kódszerkesztő, mint a VSCode), amelyek megkezdik a kapcsolatot az MCP szerverrel.

• **Kliens komponensek** a hoszt alkalmazásban, amelyek egy-egy kapcsolatot tartanak fenn a szerverekkel.

• **Szerverek** könnyűsúlyú programok, amelyek konkrét funkciókat kínálnak.

A protokoll tartalmaz három alapvető primívet, melyek az MCP szerver képességei:

• **Eszközök**: Ezek elkülönült műveletek vagy funkciók, amelyeket egy MI ügynök meghívhat egy feladat elvégzéséhez. Például egy időjárás-szolgáltatás kínálhat egy „időjárás lekérdezés” eszközt, vagy egy e-kereskedelmi szerver egy „termék vásárlása” eszközt. Az MCP szerverek hirdetik az egyes eszközök nevét, leírását és input/output sémáját a képességeik között.

• **Erőforrások**: Ezek olvasható, csak-olvasás adat elemek vagy dokumentumok, amelyeket az MCP szerver biztosít, és amelyeket a kliensek igény szerint lekérhetnek. Példák: fájl tartalma, adatbázis rekordok vagy naplófájlok. Az erőforrások lehetnek szövegesek (például kód vagy JSON) vagy binárisak (például képek vagy PDF-ek).

• **Promptok**: Ezek előre definiált sablonok, amelyek javasolt utasításokat adnak, lehetővé téve összetettebb munkafolyamatokat.

### Az MCP előnyei

Az MCP jelentős előnyöket kínál az MI ágensek számára:

• **Dinamikus eszköz-felfedezés**: Az ágensek dinamikusan megkapják a rendelkezésre álló eszközök listáját a szervertől, azok leírásával együtt. Ez eltér a hagyományos API-któl, amelyek gyakran statikus kódolást igényelnek az integrációkhoz, így egy API változás kódfrissítést követel meg. Az MCP az "egyszer integrálj" megközelítést kínálja, nagyobb rugalmasságot biztosítva.

• **Interoperabilitás különböző LLM-ek között**: Az MCP többféle LLM-mel működik, rugalmasságot adva a központi modell váltásához a jobb teljesítmény érdekében.

• **Szabványos biztonság**: Az MCP tartalmaz egy szabványos hitelesítési módszert, amely javítja a skálázhatóságot, ha további MCP szerverekhez adnak hozzáférést. Ez egyszerűbb, mint különböző kulcsokat és hitelesítési típusokat kezelni különböző hagyományos API-knál.

### MCP példa

![MCP Diagram](../../../translated_images/hu/mcp-diagram.e4ca1cbd551444a1.webp)

Képzeljük el, hogy egy felhasználó szeretne repülőjegyet foglalni egy MCP által működtetett MI asszisztens segítségével.

1. **Kapcsolódás**: Az MI asszisztens (az MCP kliens) csatlakozik egy MCP szerverhez, amelyet egy légitársaság biztosít.

2. **Eszköz-felfedezés**: A kliens megkérdezi a légitársaság MCP szerverét: „Milyen eszközök érhetők el?” A szerver válaszként eszközöket mutat, például „járatkeresés” és „járatfoglalás”.

3. **Eszközök meghívása**: Ezután megkérjük az MI asszisztenst: „Kérlek, keress egy járatot Portlandből Honolulu-ba.” Az MI asszisztens LLM-jét használva felismeri, hogy meg kell hívnia a „járatkeresés” eszközt, és továbbítja a releváns paramétereket (indulási hely, cél).

4. **Végrehajtás és válasz**: Az MCP szerver, mint egy burkoló, végrehajtja a légitársaság belső foglalási API hívását. Ezután megkapja a járat adatait (például JSON formátumban) és visszaküldi az MI asszisztensnek.

5. **További interakció**: Az MI asszisztens bemutatja a járat opciókat. Miután kiválasztott egy járatot, az asszisztens meghívhatja a „járatfoglalás” eszközt ugyanazon az MCP szerveren, így befejezve a foglalást.

## Ágens-ágens protokoll (A2A)

Míg az MCP az LLM-ek és eszközök összekapcsolására fókuszál, az **Agent-to-Agent (A2A) protokoll** tovább lép, lehetővé téve a kommunikációt és együttműködést különböző MI ágensek között. Az A2A összeköti az MI ágenseket különböző szervezetek, környezetek és technológiai rendszerek között egy közös feladat elvégzése érdekében.

Megvizsgáljuk az A2A összetevőit és előnyeit, valamint egy példát, hogyan alkalmazható a mi utazási alkalmazásunkban.

### Az A2A alapvető elemei

Az A2A a kommunikáció lehetővé tételére összpontosít az ágensek között, és arra, hogy együtt dolgozzanak a felhasználó munkafolyamatának részfeladatán. A protokoll összetevői ezért mind ezt segítik elő:

#### Agent Card

Hasonlóan ahhoz, ahogy egy MCP szerver megosztja az eszközök listáját, egy Agent Card tartalmazza:
- Az ágens nevét.
- Általános feladatok **leírását**, amelyeket elvégez.
- Egy **speciális készségek listáját** leírásokkal, hogy más ágensek (vagy akár emberi felhasználók) értsék, mikor és miért hívnák meg az adott ágenst.
- Az ágens jelenlegi **végpont URL-jét**.
- Az ágens **verzióját** és **képességeit**, mint például a válaszok streamelése és push értesítések.

#### Agent Executor

Az Agent Executor felelős azért, hogy **átadja a felhasználói beszélgetés kontextusát a távoli ágensnek**, amelyre szükség van a feladat megértéséhez. Egy A2A szervernél az ágens a saját Nagy Nyelvi Modelljét (LLM) használja a bejövő kérelmek feldolgozására és a feladatok végrehajtására a saját belső eszközeivel.

#### Artifact

Amint a távoli ágens befejezte a kért feladatot, a munkája eredménye egy artifact formájában készül el. Egy artifact **tartalmazza az ágens munkájának eredményét**, a **végrehajtott feladat leírását** és az aztól származó **szöveges kontextust**, amelyet a protokoll továbbít. Az artifact elküldése után a kapcsolat a távoli ágennsel lezárul, amíg újra szükség nem lesz rá.

#### Event Queue

Ez az összetevő a **frissítések kezelésére és üzenetek továbbítására** szolgál. Különösen fontos produkciós rendszerben az ágens rendszerek összekapcsoltságának fenntartására, hogy a kapcsolat ne záródjon le idő előtt, amikor a feladat végrehajtása hosszabb időt vehet igénybe.

### Az A2A előnyei

• **Fokozott együttműködés**: Lehetővé teszi, hogy különböző gyártók és platformok ágensei kommunikáljanak, megosszák a kontextust és együtt dolgozzanak, elősegítve a zökkenőmentes automatizálást korábban elszigetelt rendszerek között.

• **Modellválasztás rugalmassága**: Minden A2A ágens eldöntheti, melyik LLM-et használja kérelmei kiszolgálására, lehetővé téve a külön ágensre szabott vagy finomhangolt modelleket, ellentétben az egyetlen LLM kapcsolatú MCP esetekkel.

• **Beépített hitelesítés**: A hitelesítés közvetlenül be van ágyazva az A2A protokollba, erős biztonsági keretet biztosítva az ágens interakciók számára.

### A2A példa

![A2A Diagram](../../../translated_images/hu/A2A-Diagram.8666928d648acc26.webp)

Bővítsük tovább az utazási foglalási forgatókönyvünket, de most A2A-t használva.

1. **Felhasználói kérés a multi-ágenstől**: Egy felhasználó egy „Utazási Ügynök” A2A kliens/ágenssel lép kapcsolatba, például így szól: „Kérlek, foglalj le egy teljes utazást Honolulu-ba a jövő hétre, beleértve a repülőjegyeket, szállodát és bérautót.”

2. **Utazási Ügynök koordinációja**: Az Utazási Ügynök megkapja ezt a komplex kérést. Az LLM-jét használva mérlegeli a feladatot és megállapítja, hogy együtt kell működnie más specializált ágensekkel.

3. **Ágens közötti kommunikáció**: Az Utazási Ügynök az A2A protokollt használva csatlakozik további ágensekhez, mint például egy „Légitársaság Ágens”, egy „Szálloda Ágens” és egy „Bérautó Ágens”, amelyeket különböző cégek hoztak létre.

4. **Delegált feladatvégrehajtás**: Az Utazási Ügynök konkrét feladatokat küld ezeknek a specializált ágenseknek (pl. „Keress járatokat Honolulu-ba”, „Foglalj szállodát”, „Bérelj autót”). Mindegyik specializált ágens a saját LLM-jét és eszközeit (amelyek maguk is lehetnek MCP szerverek) használva végrehajtja a hozzá tartozó foglalási részt.

5. **Összevont válasz**: Miután az összes alágens befejezte feladatait, az Utazási Ügynök összegyűjti az eredményeket (járat adatok, szállodai visszaigazolás, autóbérlés) és egy átfogó, csevegési stílusú választ küld vissza a felhasználónak.

## Natural Language Web (NLWeb)

A weboldalak régóta az elsődleges módot jelentik a felhasználóknak az információk és adatok elérésére az interneten.

Tekintsük át az NLWeb különböző összetevőit, az NLWeb előnyeit és egy példán keresztül, hogyan működik az NLWeb a mi utazási alkalmazásunkban.

### Az NLWeb összetevői

- **NLWeb alkalmazás (alapszolgáltatás kódja)**: Az a rendszer, amely feldolgozza a természetes nyelvű kérdéseket. Kapcsolja a platform különböző részeit, hogy választ hozzon létre. Gondolhatunk rá, mint a **természetes nyelvi funkciók meghajtó motorjára** egy weboldalon.

- **NLWeb protokoll**: Ez egy **alapszabályrendszer a természetes nyelvi interakcióhoz** egy weboldallal. Válaszokat JSON formátumban küld vissza (gyakran Schema.org használatával). Célja, hogy egyszerű alapot teremtsen az „AI Web” számára, ugyanúgy, ahogy a HTML tette lehetővé a dokumentumok online megosztását.

- **MCP szerver (Model Context Protocol végpont)**: Minden NLWeb beállítás MCP szerverként is működik. Ez azt jelenti, hogy **megoszthat eszközöket (például az „ask” metódust) és adatokat** más MI rendszerekkel. Gyakorlatban ez lehetővé teszi, hogy a weboldal tartalma és képességei használhatóvá váljanak MI ágensek számára, így az oldal az „ágens ökoszisztéma” részévé válik.

- **Beágyazási modellek**: Ezek a modellek szolgálnak arra, hogy a weboldal tartalmát **numerikus reprezentációvá, úgynevezett vektorokká (embeddingek)** alakítsák át. Ezek a vektorok jelentést ragadnak meg számítógépek számára összehasonlításra és keresésre. Egy speciális adatbázisban tárolják őket, és a felhasználók kiválaszthatják, melyik embedding modellt szeretnék használni.

- **Vektor adatbázis (visszakereső mechanizmus)**: Ez az adatbázis tárolja a weboldal tartalmának embeddingjeit. Amikor valaki kérdést tesz fel, az NLWeb az adatbázisban gyorsan megkeresi a legrelevánsabb információkat. Gyors listát ad a lehetséges válaszokról, mérlegelve a hasonlóságot. Az NLWeb különböző vektor tároló rendszerekkel működik együtt, például Qdrant, Snowflake, Milvus, Azure AI Search és Elasticsearch.

### NLWeb példa

![NLWeb](../../../translated_images/hu/nlweb-diagram.c1e2390b310e5fe4.webp)

Vegyük ismét az utazási foglaló weboldalunkat, de most NLWeb hajtja azt.

1. **Adatbeviteli folyamat**: Az utazási weboldal meglévő termékkatalógusai (például járatlisták, szállodai leírások, túra csomagok) Schema.org formátumban vannak, vagy RSS feedeken keresztül töltődnek be. Az NLWeb eszközei feldolgozzák ezt a strukturált adatot, létrehozzák az embeddingeket, és tárolják azokat egy helyi vagy távoli vektor adatbázisban.

2. **Természetes nyelvű lekérdezés (ember)**: Egy felhasználó meglátogatja az oldalt, és a menük böngészése helyett beír egy csevegő felületen: „Kérlek, találj nekem egy családbarát szállodát Honolulu-ban medencével a jövő hétre.”

3. **NLWeb feldolgozás**: Az NLWeb alkalmazás megkapja ezt a kérdést. Elküldi azt egy LLM-nek a megértéshez, miközben párhuzamosan a vektor adatbázisában keres a releváns szállodai listák között.

4. **Pontosság az eredményekben**: Az LLM segít értelmezni az adatbázisból kapott találatokat, azonosítja a legjobb egyezéseket a „családbarát”, „medence” és „Honolulu” kritériumok alapján, majd természetes nyelvű választ formáz. Lényeges, hogy a válasz valós szállodákra hivatkozik az oldal katalógusából, kerülve a kitalált információt.

5. **MI ágens interakció**: Mivel az NLWeb MCP szerverként működik, egy külső MI utazási ágens is csatlakozhat az oldal NLWeb példányához. Az MI ágens a `ask` MCP metódust használva közvetlenül lekérdezheti az oldalt: `ask("Vannak-e a szálloda által ajánlott vegánbarát éttermek a honolului környéken?")`. Az NLWeb feldolgozza ezt, az éttermi adatbázist (ha betöltve) használva, és strukturált JSON választ ad vissza.

### Több kérdése van az MCP/A2A/NLWeb-ről?

Csatlakozzon a [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) közösséghez, hogy találkozzon más tanulókkal, részt vegyen nyitvatartási órákon, és választ kapjon az MI Ágens kérdéseire.

## Források

- [MCP kezdőknek](https://aka.ms/mcp-for-beginners)  
- [MCP dokumentáció](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb kód](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Ágens Keretrendszer](https://aka.ms/ai-agents-beginners/agent-framework)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->