# Ügynöki protokollok használata (MCP, A2A és NLWeb)

[![Agentic Protocols](../../../translated_images/hu/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Kattintson a fenti képre a lecke videójának megtekintéséhez)_

Ahogy az AI ügynökök használata növekszik, úgy nő az igény a szabványosítást, biztonságot és a nyílt innováció támogatását biztosító protokollokra is. Ebben a leckében 3 olyan protokollt mutatunk be, amelyek ezt az igényt hivatottak kielégíteni – a Model Context Protocol (MCP), az Agent to Agent (A2A) és a Natural Language Web (NLWeb).

## Bevezetés

Ebben a leckében az alábbiakról lesz szó:

• Hogyan teszi lehetővé az **MCP**, hogy az AI ügynökök külső eszközökhöz és adatokhoz férjenek hozzá a felhasználói feladatok elvégzéséhez.

• Hogyan teszi lehetővé az **A2A** a különböző AI ügynökök közötti kommunikációt és együttműködést.

• Hogyan hozza el az **NLWeb** a természetes nyelvű felületeket bármely weboldalra, lehetővé téve az AI ügynökök számára a tartalom felfedezését és interakcióját.

## Tanulási célok

• **Azonosítsa** az MCP, A2A és NLWeb protokollok fő célját és előnyeit az AI ügynökök szemszögéből.

• **Magyarázza el**, hogyan segíti elő mindegyik protokoll a LLM-ek, eszközök és egyéb ügynökök közötti kommunikációt és interakciót.

• **Ismerje fel** mindhárom protokoll eltérő szerepét az összetett ügynöki rendszerek építésében.

## Model Context Protocol

A **Model Context Protocol (MCP)** egy nyílt szabvány, amely egységes módot biztosít az alkalmazásoknak arra, hogy kontextust és eszközöket szolgáltassanak a LLM-eknek. Ez lehetővé teszi egy "univerzális adapter" létrejöttét különböző adatforrásokhoz és eszközökhöz, amelyeket az AI ügynökök következetesen csatlakoztathatnak.

Nézzük meg az MCP összetevőit, az előnyöket a közvetlen API használathoz képest, valamint egy példát arra, hogyan használhatják az AI ügynökök az MCP szervert.

### MCP alapvető összetevői

Az MCP **ügyfél-szerver architektúrán** alapul, és az alapvető összetevők a következők:

• **Hostok**: ezek LLM alkalmazások (például egy kódszerkesztő, mint a VSCode), amelyek megkezdik a kapcsolatot egy MCP szerverrel.

• **Kliens**: a host alkalmazáson belüli összetevők, amelyek egy-egy kapcsolatot tartanak fenn a szerverrel.

• **Szerverek**: könnyű programok, amelyek bizonyos képességeket tesznek elérhetővé.

A protokoll tartalmaz három alapvető elemet, amelyek egy MCP szerver képességei:

• **Eszközök**: olyan különálló műveletek vagy funkciók, amelyeket az AI ügynök hívhat meg egy tevékenység végrehajtásához. Például egy időjárás-szolgáltatás kitesz egy "időjárás lekérése" eszközt, vagy egy e-kereskedelmi szerver egy "termék vásárlása" eszközt. Az MCP szerverek egyenként hirdetik az eszközök nevét, leírását és bemenet/kimenet sémáját a képességek listájában.

• **Erőforrások**: ezek csak olvasható adat elemek vagy dokumentumok, amelyeket az MCP szerver biztosíthat, és a kliensek igény szerint lekérhetik őket. Példák a fájlok tartalma, adatbázis rekordok vagy naplófájlok. Az erőforrás lehet szöveg (például kód vagy JSON) vagy bináris állomány (például képek vagy PDF-ek).

• **Ösztönzők (Prompts)**: ezek előre definiált sablonok, amelyek javasolt kérdéseket biztosítanak, lehetővé téve összetettebb munkafolyamatok kialakítását.

### Az MCP előnyei

Az MCP jelentős előnyöket kínál az AI ügynökök számára:

• **Dinamikus eszközfelismerés**: Az ügynökök dinamikusan kapnak listát az elérhető eszközökről a szervertől, azok leírásával együtt. Ez eltér a hagyományos API-któl, amelyek gyakran statikus kódolást igényelnek az integrációkhoz, így bármilyen API változás kódfrissítést kíván. Az MCP egyszeri integrációt tesz lehetővé, ami nagyobb alkalmazkodóképességet eredményez.

• **Interoperabilitás különböző LLM-ek között**: Az MCP különböző LLM-ek között működik, rugalmasságot biztosítva a fő modellek cseréjéhez a jobb teljesítmény érdekében.

• **Szabványosított biztonság**: Az MCP tartalmaz egy szabványos hitelesítési módszert, amely javítja a skálázhatóságot az MCP szerverekhez való hozzáférés bővítésekor. Ez egyszerűbb, mint különböző kulcsok és hitelesítési típusok kezelése hagyományos API-knál.

### MCP példa

![MCP Diagram](../../../translated_images/hu/mcp-diagram.e4ca1cbd551444a1.webp)

Képzeljük el, hogy egy felhasználó repülőjegyet szeretne foglalni egy MCP által támogatott AI asszisztenssel.

1. **Kapcsolódás**: Az AI asszisztens (MCP kliens) csatlakozik egy MCP szerverhez, amelyet egy légitársaság működtet.

2. **Eszközfelismerés**: A kliens megkérdezi a légitársaság MCP szerverét: "Milyen eszközök érhetők el?" A szerver válaszként a "járatkeresés" és "járatfoglalás" eszközöket listázza.

3. **Eszköz meghívása**: Ezután a felhasználó megkéri az AI asszisztenst: "Kérem, keressen járatot Portlandból Honolulu-ba." Az AI asszisztens a LLM-je segítségével felismeri, hogy a "járatkeresés" eszközt kell meghívnia, és átadja a releváns paramétereket (indulási hely, célállomás) az MCP szervernek.

4. **Végrehajtás és válasz**: Az MCP szerver, mint egy csomagoló réteg, ténylegesen meghívja a légitársaság belső foglalási API-ját. Ezután megkapja a járatinformációt (például JSON adatokat), és visszaküldi az AI asszisztensnek.

5. **További interakció**: Az AI asszisztens bemutatja a járatopciókat. Amikor a felhasználó kiválaszt egy járatot, az asszisztens meghívhatja ugyanazon MCP szerveren a "járatfoglalás" eszközt, ezzel befejezve a foglalást.

## Ügynök-ügynök protokoll (A2A)

Míg az MCP az LLM-ek és eszközök összekapcsolására fókuszál, az **Agent-to-Agent (A2A) protokoll** tovább lép azzal, hogy lehetővé teszi különböző AI ügynökök közötti kommunikációt és együttműködést. Az A2A összeköti az AI ügynököket különböző szervezetek, környezetek és technológiai stakkok között a közös feladat végrehajtásához.

Megvizsgáljuk az A2A összetevőit és előnyeit, valamint egy példán keresztül bemutatjuk, hogyan alkalmazható egy utazási alkalmazásban.

### Az A2A alapvető összetevői

Az A2A a kommunikációt és az együttműködést helyezi előtérbe az ügynökök között, hogy feladatokat együtt oldjanak meg. A protokoll minden összetevője hozzájárul ehhez:

#### Ügynök kártya

Hasonlóan ahhoz, hogy egy MCP szerver eszközlistát oszt meg, az Ügynök kártya tartalmazza:
- Az ügynök nevét.
- A **feladatok általános leírását**, amelyeket elvégez.
- Egy **specifikus készségeket felsoroló listát** leírásokkal, hogy más ügynökök (vagy akár emberek) megértsék, mikor és miért hívnák meg az adott ügynököt.
- Az ügynök **aktuális végpont URL-címét**.
- Az ügynök **verzióját** és **képességeit**, mint például a streamelt válaszok és push értesítések.

#### Ügynök futtató

Az Ügynök futtató felelős azért, hogy **átadja a felhasználói chat kontextusát a távoli ügynöknek**, amelynek ez szükséges a feladat megértéséhez. Egy A2A szervernél az ügynök a saját LLM-jét használja a bejövő kérések elemzésére és a feladatok végrehajtására a saját belső eszközeivel.

#### Műtárgy

Amikor egy távoli ügynök végrehajtja a kért feladatot, a munkájának eredménye műtárgyként jön létre. Egy műtárgy **tartalmazza az ügynök munkájának eredményét**, a **végrehajtott tevékenység leírását**, és a protokollon keresztül továbbított **szöveges kontextust**. Miután a műtárgy elküldésre került, a kapcsolat a távoli ügynökkel bezárul, amíg újra szükség nem lesz rá.

#### Esemény sor

Ez az összetevő az **frissítések kezelésére és üzenetátadásra** szolgál. Különösen fontos a termelési ügynöki rendszerekben, hogy megakadályozza az ügynökök közötti kapcsolat lezárását a feladat befejezése előtt, különösen, ha a feladat végrehajtása hosszabb időt vehet igénybe.

### Az A2A előnyei

• **Fokozott együttműködés**: Lehetővé teszi, hogy különböző eladók és platformok ügynökei interakcióba lépjenek, kontextust osszanak meg és együtt dolgozzanak, elősegítve a zökkenőmentes automatizálást a hagyományosan elkülönült rendszerek között.

• **Rugalmasság a modellválasztásban**: Minden A2A ügynök eldöntheti, melyik LLM-et használja a kérések kiszolgálására, lehetővé téve az optimalizált vagy finomhangolt modellek alkalmazását ügynökönként, ellentétben az MCP bizonyos eseteiben használt egyetlen LLM kapcsolattal.

• **Beépített hitelesítés**: A hitelesítés közvetlenül az A2A protokollba van integrálva, biztosítva a robosztus biztonsági keretrendszert az ügynöki interakciókhoz.

### A2A példa

![A2A Diagram](../../../translated_images/hu/A2A-Diagram.8666928d648acc26.webp)

Bővítsük ki az utazási foglalási példánkat, de ezúttal az A2A segítségével.

1. **Felhasználói kérés multi-ügynöknek**: Egy felhasználó egy "Utazási Ügynök" A2A klienssel/ügynökkel lép kapcsolatba, talán így mondva: „Kérlek, foglalj egy teljes utazást Honolulu-ba a jövő hétre, beleértve a repülőjegyeket, szállodát és autókölcsönzést.”

2. **Az Utazási Ügynök irányítása**: Az Utazási Ügynök megkapja ezt az összetett kérést. LLM-et használ, hogy értelmezze a feladatot, és meghatározza, hogy más, speciális ügynökökkel kell kapcsolatot teremtenie.

3. **Ügynökök közötti kommunikáció**: Az Utazási Ügynök az A2A protokollt használja, hogy kapcsolódjon alárendelt ügynökökhöz, mint például a „Légitársaság Ügynök”, „Szálloda Ügynök” és „Autókölcsönző Ügynök”, amelyeket különböző cégek hoztak létre.

4. **Feladatdelegálás végrehajtása**: Az Utazási Ügynök részfeladatokat küld ezeknek a speciális ügynököknek (pl. "Keress járatokat Honolulu-ba", "Foglalj szállodát", "Kölcsönözz autót"). Mindegyik ügynök a saját LLM-jével és eszközeivel (amelyek lehetnek maguk is MCP szerverek) hajtja végre az adott részfeladatot.

5. **Összevont válasz**: Miután minden alárendelt ügynök befejezte a feladatát, az Utazási Ügynök összeállítja az eredményeket (járat részletek, szállodai visszaigazolás, autóbérlési foglalás), és egy átfogó, cset-szerű választ küld vissza a felhasználónak.

## Természetes Nyelvű Web (NLWeb)

A weboldalak régóta az elsődleges módját jelentik az információhoz és adatokhoz való internetes hozzáférésnek a felhasználók számára.

Nézzük meg az NLWeb különböző összetevőit, az NLWeb előnyeit, és egy példát arra, hogyan működik NLWeb az utazási alkalmazásunk esetén.

### Az NLWeb összetevői

- **NLWeb alkalmazás (alapszolgáltatás kódja)**: Ez a rendszer dolgozza fel a természetes nyelvű kérdéseket. Összeköti a platform különböző részeit a válaszok létrehozásához. Gondolhatunk rá úgy, mint a **weboldal természetes nyelvű funkcióinak motorjára**.

- **NLWeb protokoll**: Ez egy **alapvető szabálykészlet a természetes nyelvű interakcióhoz egy weboldallal**. Válaszokat JSON formátumban küld vissza (gyakran a Schema.org használatával). Célja, hogy egyszerű alapot teremtsen az "AI Web"-hez, ugyanúgy, ahogy az HTML lehetővé tette az online dokumentummegosztást.

- **MCP szerver (Model Context Protocol végpont)**: Minden NLWeb beállítás MCP szerverként is működik. Ez azt jelenti, hogy képes **megosztani eszközöket (például egy „ask” metódust) és adatokat** más AI rendszerekkel. Gyakorlatban ez lehetővé teszi, hogy a weboldal tartalma és képességei elérhetővé váljanak AI ügynökök számára, így a weboldal a tágabb „ügynöki ökoszisztéma” része lesz.

- **Beágyazó modellek**: Ezek a modellek arra szolgálnak, hogy a weboldal tartalmát numerikus reprezentációkká, úgynevezett vektorokká (beágyazásokká) alakítsák át. Ezek a vektorok olyan jelentést ragadnak meg, amelyeket a számítógépek összehasonlíthatnak és kereshetnek köztük. Egy speciális adatbázisban tárolódnak, és a felhasználók választhatják ki, melyik beágyazó modellt szeretnék használni.

- **Vektoradatbázis (keresési mechanizmus)**: Ez az adatbázis tárolja a weboldal tartalmának beágyazásait. Amikor valaki kérdést tesz fel, az NLWeb megnézi a vektoradatbázist, hogy gyorsan megtalálja a legrelevánsabb információt. Gyors listát ad lehetséges válaszokról, hasonlóság alapján rangsorolva. NLWeb különböző vektor tároló rendszerekkel működik együtt, mint a Qdrant, Snowflake, Milvus, Azure AI Search és Elasticsearch.

### NLWeb példa

![NLWeb](../../../translated_images/hu/nlweb-diagram.c1e2390b310e5fe4.webp)

Vegyük újra az utazási foglaló weboldalunkat, de ezúttal NLWeb által vezérelve.

1. **Adatbevitel**: Az utazási weboldal meglévő termékkatalógusai (pl. járatlisták, szállodaleírások, túracsomagok) Schema.org szabvány szerint formázottak vagy RSS feedeken keresztül töltődnek be. Az NLWeb eszközei feldolgozzák ezt a strukturált adatot, létrehozzák a beágyazásokat, és egy helyi vagy távoli vektor adatbázisba mentik őket.

2. **Természetes nyelvű lekérdezés (ember)**: Egy felhasználó meglátogatja a weboldalt, és a menük böngészése helyett egy csevegőfelületen írja be: „Keress számomra családbarát szállodát Honolulu-ban medencével a jövő hétre.”

3. **NLWeb feldolgozás**: Az NLWeb alkalmazás megkapja ezt a lekérdezést. Elküldi az LLM-nek megértésre, miközben saját vektoradatbázisában releváns szállodai ajánlatokat keres.

4. **Pontosságos találatok**: Az LLM segít értelmezni az adatbázisból származó találatokat, kiválasztja a legjobb egyezéseket a „családbarát”, „medence” és „Honolulu” szempontok alapján, majd természetes nyelvű választ formáz. Kiemelten fontos, hogy a válasz tényleges szállodákra hivatkozik a weboldal katalógusából, nem kitalált információkra.

5. **AI ügynök interakció**: Mivel az NLWeb MCP szerverként is működik, egy külső AI utazási ügynök is csatlakozhat ehhez a weboldal NLWeb példányához. Az AI ügynök az `ask` MCP metódust használhatja arra, hogy közvetlenül kérdezze a weboldalt: `ask("Van-e a szálloda által ajánlott vegánbarát étterem a Honolulu környékén?")`. Az NLWeb feldolgozza ezt, kihasználva az étteremadatbázist (ha betöltötték), és strukturált JSON választ ad.

### További kérdései vannak az MCP/A2A/NLWeb kapcsán?

Csatlakozzon a [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) csoporthoz, hogy találkozzon más tanulókkal, részt vehessen ügyfélfogadási órákon és megkaphassa az AI ügynökeivel kapcsolatos kérdéseinek válaszát.

## Források

- [MCP kezdőknek](https://aka.ms/mcp-for-beginners)  
- [MCP dokumentáció](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb tároló](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python)

## Előző lecke

[AI ügynökök a termelésben](../10-ai-agents-production/README.md)

## Következő lecke

[Kontextus mérnökség AI ügynökök számára](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->