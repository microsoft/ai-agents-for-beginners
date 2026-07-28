# Agentikus protokollok használata (MCP, A2A és NLWeb)

[![Agentikus protokollok](../../../translated_images/hu/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Kattintson a fenti képre, hogy megtekinthesse az óra videóját)_

Ahogy a mesterséges intelligencia ügynökök használata növekszik, úgy nő az igény a szabványosítást, biztonságot és nyílt innovációt támogató protokollokra. Ebben az órában három ilyen protokollt tekintünk át - a Model Context Protocol-t (MCP), az Agent to Agent-et (A2A) és a Natural Language Web-et (NLWeb).

## Bevezetés

Ebben az órában az alábbiakról lesz szó:

• Hogyan teszi lehetővé az **MCP**, hogy az AI ügynökök külső eszközökhöz és adatokhoz férjenek hozzá a felhasználói feladatok elvégzéséhez.

• Hogyan teszi lehetővé az **A2A** különböző AI ügynökök közötti kommunikációt és együttműködést.

• Hogyan hozza el az **NLWeb** a természetes nyelvi felületeket bármely weboldalra, lehetővé téve az AI ügynökök számára a tartalom felfedezését és interakcióját.

## Tanulási célok

• **Azonosítani** az MCP, az A2A és az NLWeb központi célját és előnyeit az AI ügynökök kontextusában.

• **Megmagyarázni**, hogy ezek a protokollok miként teszik lehetővé a kommunikációt és az interakciót a nagy nyelvi modellek, eszközök és más ügynökök között.

• **Fel kell ismerni** a protokollok eltérő szerepét a komplex agentikus rendszerek építésében.

## Model Context Protocol

A **Model Context Protocol (MCP)** egy nyílt szabvány, amely egységes módot biztosít az alkalmazások számára, hogy kontextust és eszközöket biztosítsanak a nagy nyelvi modelleknek (LLM). Ez lehetővé teszi egy "univerzális adapter" létrejöttét különböző adatforrások és eszközök számára, amelyhez az AI ügynökök következetes módon kapcsolódhatnak.

Nézzük meg az MCP komponenseit, az előnyöket a közvetlen API-használattal szemben és egy példát, hogyan használhatják az AI ügynökök az MCP szervert.

### Az MCP alapvető komponensei

Az MCP egy **kliens-szerver architektúrán** működik, és az alapvető elemek a következők:

• A **Hosts** LLM alkalmazások (például egy VSCode kód szerkesztő), amelyek elindítják a kapcsolatokat az MCP szerverhez.

• A **Clients** a host alkalmazás azon komponensei, amelyek egy-egy kapcsolattartás a szerverekkel.

• A **Servers** könnyű programok, melyek meghatározott képességeket tesznek elérhetővé.

A protokoll három alapvető primitívet tartalmaz, amelyek egy MCP szerver képességei:

• **Eszközök**: Ezek diszkrét műveletek vagy funkciók, amelyeket az AI ügynök meghívhat egy művelet végrehajtására. Például egy időjárás szolgáltatás kinyithat egy „időjárás lekérése” eszközt, vagy egy e-kereskedelmi szerver egy „termék vásárlása” eszközt. Az MCP szerverek hirdetik az egyes eszközök nevét, leírását és input/output sémáját a képességek listájában.

• **Erőforrások**: Ezek olvasható adatelemek vagy dokumentumok, amelyeket egy MCP szerver biztosít, és az ügyfelek igény szerint lekérhetik azokat. Példák: fájl tartalmak, adatbázis rekordok vagy naplófájlok. Az erőforrások lehetnek szövegesek (pl. kód vagy JSON) vagy binárisak (pl. képek vagy PDF-ek).

• **Promptok**: Ezek előre definiált sablonok, amelyek javasolt promptokat tartalmaznak, lehetővé téve összetettebb munkafolyamatokat.

### Az MCP előnyei

Az MCP jelentős előnyöket kínál az AI ügynökök számára:

• **Dinamikus Eszköz Felfedezés**: Az ügynökök dinamikusan fogadhatnak elérhető eszközök listáját egy szervertől, azok leírásával együtt. Ez eltér a hagyományos API-któl, amelyek gyakran statikus kódolást igényelnek az integrációkhoz, így az API módosítások kódfrissítést követelnek. Az MCP egy "egyszer integráld" megközelítést kínál, ami nagyobb alkalmazkodóképességet eredményez.

• **Interoperabilitás több LLM között**: Az MCP különféle LLM-ek között működik, lehetőséget adva a magmodellek váltására a jobb teljesítményért.

• **Szabványosított biztonság**: Az MCP tartalmaz egy szabványos hitelesítési módszert, javítva a skálázhatóságot az újabb MCP szerverek hozzáadásakor. Ez egyszerűbb, mint különféle kulcsok és hitelesítési típusok kezelése a hagyományos API-knál.

### MCP példa

![MCP diagram](../../../translated_images/hu/mcp-diagram.e4ca1cbd551444a1.webp)

Tegyük fel, hogy egy felhasználó repülőjegyet akar foglalni egy MCP-vel működő AI asszisztenssel.

1. **Kapcsolódás**: Az AI asszisztens (az MCP kliens) kapcsolódik egy MCP szerverhez, amelyet egy légitársaság biztosít.

2. **Eszköz felfedezés**: Az ügyfél megkérdezi a légitársaság MCP szerverétől: "Milyen eszközök állnak rendelkezésre?" A szerver olyan eszközökkel válaszol, mint a "járatok keresése" és a "járat foglalása".

3. **Eszköz meghívása**: Ezután a felhasználó megkéri az AI asszisztenst: "Kérlek, keress járatot Portland és Honolulu között." Az AI asszisztens, az LLM használatával, felderíti, hogy meg kell hívnia a "járatok keresése" eszközt és átadja a releváns paramétereket (indulási hely, célállomás) az MCP szervernek.

4. **Végrehajtás és válasz**: Az MCP szerver, mint egy burkoló (wrapper), ténylegesen meghívja a légitársaság belső foglalási API-ját. Ezután megkapja a járat információkat (például JSON adatokat) és visszaküldi az AI asszisztensnek.

5. **További interakció**: Az AI asszisztens bemutatja a járat opciókat. Amikor a felhasználó kiválaszt egy járatot, az asszisztens esetleg meghívja ugyanazon MCP szerveren a "járat foglalása" eszközt, ezzel befejezve a foglalást.

## Agent-to-Agent protokoll (A2A)

Míg az MCP az LLM-ek és eszközök összekapcsolására fókuszál, az **Agent-to-Agent (A2A) protokoll** egy lépéssel tovább megy, lehetővé téve a kommunikációt és együttműködést különböző AI ügynökök között. Az A2A összeköti az AI ügynököket különböző szervezetek, környezetek és technológiai rendszerek között, hogy közös feladatot hajtsanak végre.

Megvizsgáljuk az A2A komponenseit és előnyeit, valamint egy példát, hogyan alkalmazható az utazási alkalmazásunkban.

### Az A2A alapvető komponensei

Az A2A a kommunikáció elősegítésére fókuszál az ügynökök között, valamint arra, hogy együtt dolgozzanak egy felhasználói alfeladat elvégzésén. A protokoll minden komponense ehhez járul hozzá:

#### Agent kártya

Hasonlóan ahhoz, ahogy egy MCP szerver megosztja az eszközök listáját, egy Agent kártya a következőket tartalmazza:
- Az ügynök nevét.
- Az általa általánosan végzett feladatok **leírását**.
- Egy **konkrét képességek listáját** leírásokkal, hogy más ügynökök (vagy akár emberek) megértsék, mikor és miért akarnának az adott ügynökhöz fordulni.
- Az ügynök aktuális **végpont URL-jét**.
- Az ügynök **verzióját** és **képességeit**, mint például streaming válaszok vagy push értesítések.

#### Agent végrehajtó (Executor)

Az Agent Executor felelős azért, hogy a felhasználói beszélgetés kontextusát továbbítsa a távoli ügynöknek, amelynek szüksége van erre a megértéshez. Egy A2A szerveren az ügynök a saját nagy nyelvi modelljét (LLM) használja a bejövő kérések feldolgozásához és a belső eszközei használatával végzi el a feladatokat.

#### Artefaktum

Amint a távoli ügynök befejezte a kért feladatot, a munkája egy artefaktumként jön létre. Egy artefaktum **tartalmazza az ügynök munkájának eredményét**, a **megvalósított feladat leírását**, és a protokollon keresztül továbbított **szöveges kontextust**. Miután az artefaktum elküldésre került, a kapcsolat a távoli ügynökkel lezárul, amíg újra szükség nem lesz rá.

#### Esemény sor (Event Queue)

Ezt a komponenst a **frissítések kezelésére és üzenetek továbbítására** használják. Különösen fontos a termelésben az agentikus rendszerekben, hogy megakadályozza a kapcsolat megszakadását az ügynökök között a feladat befejezése előtt, főként akkor, ha a feladatteljesítés hosszabb ideig tart.

### Az A2A előnyei

• **Fokozott együttműködés**: Lehetővé teszi, hogy különböző szolgáltatók és platformok ügynökei kommunikáljanak, megosszák a kontextust és együtt dolgozzanak, megkönnyítve a zökkenőmentes automatizálást hagyományosan elszigetelt rendszerek között.

• **Modell választás rugalmassága**: Minden A2A ügynök dönthet arról, melyik LLM-et használja a kérelmek kiszolgálásához, lehetővé téve optimalizált vagy finomhangolt modellek alkalmazását ügynökönként, ellentétben az egy LLM kapcsolatú MCP esetekkel.

• **Beépített hitelesítés**: A hitelesítés közvetlenül az A2A protokollba integrált, erős biztonsági keretrendszert biztosítva az ügynöki interakciókhoz.

### A2A példa

![A2A diagram](../../../translated_images/hu/A2A-Diagram.8666928d648acc26.webp)

Tekintsük bővebben az utazási foglalási forgatókönyvet, ezúttal A2A használatával.

1. **Felhasználói kérés a többagenthez**: Egy felhasználó egy "Utazási Ügynök" A2A klienssel/ügynökkel kommunikál, például így: "Kérlek foglalj le egy teljes utazást Honoluluba a jövő héten, repülőjeggyel, szállodával és bérelt autóval."

2. **Az Utazási Ügynök irányítása**: Az Utazási Ügynök megkapja ezt az összetett kérést. Az LLM-jét használva megérti a feladatot, és eldönti, hogy más specializált ügynökökkel kell együttműködnie.

3. **Ügynökök közötti kommunikáció**: Az Utazási Ügynök az A2A protokollt használva csatlakozik további ügynökökhöz, például egy „Légitársaság ügynökhöz”, egy „Szálloda ügynökhöz” és egy „Autókölcsönző ügynökhöz”, amelyeket különböző cégek hoztak létre.

4. **Feladat delegálás**: Az Utazási Ügynök konkrét feladatokat küld ezeknek a specializált ügynököknek (pl. "Keress járatokat Honolulu-ba", "Foglalj szállodát", "Bérelj autót"). Ezek az ügynökök saját LLM-jeiket és eszközeiket használva (amik lehetnek MCP szerverek) végzik el a foglalás egyes részeit.

5. **Összesített válasz**: Miután az összes downstream ügynök befejezte feladatait, az Utazási Ügynök összesíti az eredményeket (járat adatok, szállodai visszaigazolás, autóbérlés) és egy átfogó, chat-stílusú választ küld vissza a felhasználónak.

## Természetes Nyelvű Web (NLWeb)

A weboldalak régóta az elsődleges módjai a felhasználók számára, hogy információhoz és adatokhoz jussanak az interneten.

Tekintsük át az NLWeb különböző komponenseit, előnyeit, és nézzük meg példán keresztül az utazási alkalmazásunk működését.

### Az NLWeb komponensei

- **NLWeb alkalmazás (alapszolgáltatás kódja)**: Az a rendszer, amely feldolgozza a természetes nyelvű kérdéseket. Összekapcsolja a platform különböző részeit, hogy válaszokat hozzon létre. Ezt lehet tekinteni úgy, mint a **motor, amely támogatja a weboldal természetes nyelvi funkcióit**.

- **NLWeb protokoll**: Ez egy **alapvető szabályrendszer** a természetes nyelvi interakcióhoz weboldalakkal. Válaszokat küld JSON formátumban (gyakran Schema.org használatával). Célja, hogy egyszerű alapot teremtsen az „AI Web” számára, ugyanúgy, ahogy a HTML tette lehetővé az online dokumentum megosztást.

- **MCP szerver (Model Context Protocol végpont)**: Minden NLWeb telepítés MCP szerverként is működik. Ez azt jelenti, hogy **eszközöket (például egy „ask” metódust) és adatokat** is megoszthat más AI rendszerekkel. Gyakorlatban ez lehetővé teszi, hogy a weboldal tartalma és képességei AI ügynökök számára is elérhetők legyenek, így a webhely része lesz a szélesebb „ügynök ökoszisztémának”.

- **Beágyazó modellek**: Ezek a modellek a weboldal tartalmát numerikus reprezentációkká, ún. vektorokká (embedding) alakítják át. Ezek a vektorok a jelentést úgy ragadják meg, hogy a számítógépek képesek legyenek összehasonlítani és keresni bennük. Egy speciális adatbázisban tárolódnak, és a felhasználók választhatják, melyik embedding modellt kívánják használni.

- **Vektor adatbázis (keresési mechanizmus)**: Ez az adatbázis tárolja a weboldal tartalmának beágyazásait. Amikor valaki kérdést tesz fel, az NLWeb a vektor adatbázisban gyorsan megtalálja a legrelevánsabb információkat. Egy gyors, hasonlóság szerint rangsorolt válaszulistát ad. Az NLWeb különféle vektor tároló rendszerekkel működik együtt, például Qdrant, Snowflake, Milvus, Azure AI Search és Elasticsearch.

### Példa az NLWeb használatára

![NLWeb](../../../translated_images/hu/nlweb-diagram.c1e2390b310e5fe4.webp)

Vegyük ismét az utazási foglaló weboldalunkat, amely ezúttal az NLWeb motorjával működik.

1. **Adatbeolvasás**: Az utazási weboldal meglévő termékkatalógusai (pl. járatlista, szállodai leírások, túracsomagok) Schema.org segítségével vannak formázva, vagy RSS feedeken keresztül töltődnek be. Az NLWeb eszközök feldolgozzák ezt a strukturált adatot, beágyazásokat hoznak létre, és eltárolják helyi vagy távoli vektor adatbázisban.

2. **Természetes nyelvű kérdés (emberi)**: A felhasználó meglátogatja az oldalt és a menük helyett a chat felületre írja: "Találj nekem a jövő hétre családbarát, medencés szállodát Honoluluban."

3. **NLWeb feldolgozás**: Az NLWeb alkalmazás megkapja a kérdést. Elküldi azt egy LLM-nek az értelmezéshez, miközben egy időben átnézi a vektor adatbázist releváns szállodák keresésére.

4. **Pontos eredmények**: Az LLM segít értelmezni az adatbázisból kapott találatokat, azonosítani a legjobb találatokat a „családbarát”, „medence” és „Honolulu” kritériumok alapján, majd természetes nyelvű választ formáz. Fontos, hogy a válasz a weboldal tényleges szállodai katalógusára hivatkozik, elkerülve a kitalált információkat.

5. **AI ügynök interakció**: Mivel az NLWeb MCP szerverként is működik, egy külső AI utazási ügynök is csatlakozhat az adott weboldal NLWeb példányához. Az AI ügynök ezt követően az `ask` MCP metódussal közvetlen kérdést tehet fel az oldalnak: `ask("Vannak a hoteltől ajánlott vegánbarát éttermek Honoluluban?")`. Az NLWeb feldolgozza ezt, kihasználva az éttermi információkat tartalmazó adatbázist (ha betöltve), és strukturált JSON választ ad.

### Több kérdése lenne az MCP/A2A/NLWeb témában?

Csatlakozzon a [Microsoft Foundry Discord-hoz](https://discord.com/invite/ATgtXmAS5D) találkozni más tanulókkal, részt venni az irodai órákon, és válaszokat kapni AI ügynökök kérdéseire.

## Források

- [MCP kezdőknek](https://aka.ms/mcp-for-beginners)  
- [MCP dokumentáció](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb forráskód](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framework)

## Előző óra

[AI ügynökök a gyakorlatban](../10-ai-agents-production/README.md)

## Következő óra

[Kontextus tervezés AI ügynököknek](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->