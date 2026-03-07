# Agentikus protokollok használata (MCP, A2A és NLWeb)

[![Agentikus protokollok](../../../translated_images/hu/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Kattintson a fenti képre a lecke videójának megtekintéséhez)_

Ahogy az AI ügynökök használata növekszik, úgy nő az igény az olyan protokollokra, amelyek biztosítják a szabványosítást, a biztonságot és támogatják a nyílt innovációt. Ebben a leckében 3 protokollt fogunk áttekinteni, amelyek ezt az igényt kívánják kielégíteni – Model Context Protocol (MCP), Agent to Agent (A2A) és Natural Language Web (NLWeb).

## Bevezetés

Ebben a leckében áttekintjük:

• Hogyan teszi lehetővé az **MCP**, hogy az AI ügynökök külső eszközökhöz és adatokhoz férjenek hozzá a felhasználói feladatok elvégzéséhez.

• Hogyan teszi lehetővé az **A2A** az eltérő AI ügynökök közötti kommunikációt és együttműködést.

• Hogyan hozza el az **NLWeb** a természetes nyelvű felületeket bármely weboldalra, lehetővé téve az AI ügynökök számára a tartalom felfedezését és interakcióját.

## Tanulási célok

• **Azonosítani** az MCP, A2A és NLWeb alapvető célját és előnyeit az AI ügynökök kontextusában.

• **Megmagyarázni**, hogyan segíti elő mindegyik protokoll a kommunikációt és az interakciót LLM-ek, eszközök és más ügynökök között.

• **Felül ismerni** az egyes protokollok különböző szerepét összetett ügynökrendszerek építésében.

## Model Context Protocol

A **Model Context Protocol (MCP)** egy nyílt szabvány, amely szabványosított módot biztosít az alkalmazások számára, hogy kontextust és eszközöket szolgáltassanak LLM-eknek. Ez lehetővé tesz egy "univerzális adaptert" különböző adattípusokhoz és eszközökhöz, amelyhez az AI ügynökök konzisztensen tudnak csatlakozni.

Nézzük meg az MCP összetevőit, az előnyöket a közvetlen API használathoz képest, és egy példát arra, hogyan használhatják az AI ügynökök az MCP szervert.

### MCP alapkomponensek

Az MCP **kliens-szerver architektúrán** alapul, és az alapkomponensei:

• **Hostok** azok az LLM alkalmazások (például egy kódszerkesztő, mint a VSCode), amelyek elindítják a kapcsolatokat egy MCP szerverhez.

• **Klienseik** a host alkalmazáson belüli komponensek, amelyek egy-egy kapcsolatot tartanak fenn a szerverekkel.

• **Szerverek** könnyű programok, amelyek konkrét képességeket tesznek elérhetővé.

A protokoll tartalmaz három alapvető primitívet, amelyek egy MCP szerver képességei:

• **Eszközök (Tools)**: Ezek önálló műveletek vagy függvények, amelyeket egy AI ügynök hívhat meg egy művelet végrehajtására. Például egy időjárás-szolgáltatás kínálhat „időjárás lekérése” eszközt, vagy egy e-kereskedelmi szerver "termék vásárlása" eszközt. Az MCP szerverek minden eszköz nevét, leírását és bemeneti/kimeneti sémáját hirdetik a képességlistában.

• **Erőforrások (Resources)**: Ezek olvasható adat elemek vagy dokumentumok, amelyeket egy MCP szerver szolgáltathat, és az ügyfelek igény szerint kérhetik le őket. Példák: fájl tartalom, adatbázis rekordok vagy naplófájlok. Az erőforrások lehetnek szövegesek (például kód vagy JSON) vagy binárisak (például képek vagy PDF-ek).

• **Kezdőlapok (Prompts)**: Előre definiált sablonok, amelyek javasolt promptokat adnak, lehetővé téve komplexebb munkafolyamatokat.

### Az MCP előnyei

Az MCP jelentős előnyöket nyújt az AI ügynökök számára:

• **Dinamikus Eszközfelismerés**: Az ügynökök dinamikusan megkaphatják egy szerver elérhető eszközeinek listáját azok leírásaival együtt. Ez ellentétben áll a hagyományos API-kkal, amelyek tipikusan statikus kódolást igényelnek az integrációkhoz, így bármilyen API változás kódmódosítást követel meg. Az MCP egy "egyszer integráld" megközelítést kínál, ami nagyobb alkalmazkodóképességet eredményez.

• **Interoperabilitás Különböző LLM-ek Között**: Az MCP különböző LLM-eket támogat, lehetővé téve a modellek könnyű cseréjét jobb teljesítmény elérése érdekében.

• **Szabványosított Biztonság**: Az MCP tartalmaz egy szabványos hitelesítési módszert, ami megkönnyíti az új MCP szerverekhez való hozzáférések skálázását. Ez egyszerűbb, mint különböző kulcsok és hitelesítési típusok kezelése a hagyományos API-k esetén.

### MCP példa

![MCP Diagram](../../../translated_images/hu/mcp-diagram.e4ca1cbd551444a1.webp)

Képzeljük el, hogy egy felhasználó szeretne repülőjegyet foglalni egy MCP által támogatott AI asszisztens segítségével.

1. **Kapcsolat**: Az AI asszisztens (az MCP kliens) kapcsolódik egy MCP szerverhez, amelyet egy légitársaság biztosít.

2. **Eszközfelismerés**: A kliens megkérdezi a légitársaság MCP szerverét: "Milyen eszközök érhetőek el nálatok?" A szerver válaszul eszközöket küld, mint például „járatok keresése” és „járat foglalása”.

3. **Eszköz meghívás**: Ezután a felhasználó megkéri az AI asszisztenst: „Kérlek, keresd meg a Portland–Honolulu járatokat.” Az AI asszisztens LLM-jével felismerteti, hogy meg kell hívja a „járatok keresése” eszközt, és átadja a megfelelő paramétereket (indulási hely, célállomás) az MCP szervernek.

4. **Végrehajtás és válasz**: Az MCP szerver, csomagolóként működve, ténylegesen meghívja a légitársaság belső foglalási API-ját. Ezután megkapja a járatok információit (pl. JSON adatot) és visszaküldi az AI asszisztensnek.

5. **További interakció**: Az AI asszisztens bemutatja a járatlehetőségeket. Amikor a felhasználó kiválaszt egy járatot, az asszisztens a „járat foglalása” eszközt is meghívhatja ugyanazon MCP szerveren, ezzel befejezve a foglalást.

## Agent-to-Agent Protokoll (A2A)

Míg az MCP az LLM-eket köti össze eszközökkel, addig az **Agent-to-Agent (A2A) protokoll** továbblép azzal, hogy lehetővé teszi a különböző AI ügynökök közötti kommunikációt és együttműködést. Az A2A összekapcsolja az AI ügynököket különböző szervezetek, környezetek és technológiai platformok között egy közös feladat elvégzéséhez.

Áttekintjük az A2A komponenseit és előnyeit, valamint egy példát arra, hogyan alkalmazható ez az utazási alkalmazásunkban.

### A2A alapkomponensek

Az A2A az ügynökök közti kommunikációt és a feladatmegosztásban való együttműködést támogatja. A protokoll minden komponense ebben segít:

#### Ügynök kártya (Agent Card)

Hasonlóan ahhoz, hogy egy MCP szerver megosztja az elérhető eszközök listáját, az Ügynök Kártya tartalmazza:
- Az ügynök nevét.
- A **végzett általános feladatok** leírását.
- Egy **specifikus képességek listáját** leírásokkal, amelyek segítenek más ügynököknek (vagy akár emberi felhasználóknak) megérteni, mikor és miért érdemes az adott ügynökhöz fordulni.
- Az ügynök **aktuális végpont URL-jét**.
- Az **ügynök verzióját** és **képességeit**, például streaming válaszokat és push értesítéseket.

#### Ügynök Végrehajtó (Agent Executor)

Az Ügynök Végrehajtó felelős az **aktuális felhasználói chat kontextus átadásáért a távoli ügynöknek**, amely ehhez szükséges a kiosztott feladat megértéshez. Egy A2A szerveren egy ügynök a saját Nagy Nyelvi Modelljét (LLM-jét) használja a bejövő kérések értelmezésére és a feladatok végrehajtására saját belső eszközeivel.

#### Műtárgy (Artifact)

Miután a távoli ügynök végrehajtotta a kért feladatot, az eredményt egy műtárgy formájában hozza létre. A műtárgy **tartalmazza az ügynök munkájának eredményét**, a **végrehajtott tevékenység leírását**, valamint a **szöveges kontextust**, amely átadásra kerül a protokollon keresztül. A műtárgy elküldése után a kapcsolat a távoli ügynökkel lezárul, amíg újra szükség nem lesz rá.

#### Esemény sor (Event Queue)

Ez a komponens az **frissítések kezelésére és üzenetek továbbítására** szolgál. Kiemelten fontos a termelésben használatos ügynökrendszerek számára, hogy megakadályozza a kapcsolatok idő előtti záródását a feladat befejezése előtt, különösen amikor a feladatok végrehajtása hosszabb időt vehet igénybe.

### Az A2A előnyei

• **Fokozott együttműködés**: Lehetővé teszi, hogy különböző szállítók és platformok ügynökei interakcióba lépjenek, megosszák a kontextust és együtt dolgozzanak, zökkenőmentes automatizálást érve el hagyományosan elszigetelt rendszerek között.

• **Modellválasztási rugalmasság**: Minden A2A ügynök maga döntheti el, melyik LLM-et használja a kérés kiszolgálására, lehetővé téve egyedi vagy finomhangolt modellek alkalmazását ügynökönként, ellentétben az egyetlen LLM kapcsolatú MCP esetekkel.

• **Beépített hitelesítés**: A hitelesítés közvetlenül az A2A protokoll része, erős biztonsági keretet nyújtva az ügynökök közötti interakciókhoz.

### A2A példa

![A2A Diagram](../../../translated_images/hu/A2A-Diagram.8666928d648acc26.webp)

Fejlesszük tovább utazási foglalási példánkat, de most A2A használatával.

1. **Felhasználói kérés több ügynöknek**: Egy felhasználó egy "Utazási Ügynök" nevű A2A klienssel/ügynökkel kommunikál, például így: „Foglalj nekem egy egész utat Honolulu-ba a jövő hétre, beleértve járatokat, szállást és bérautót.”

2. **Az Utazási Ügynök koordinálása**: Az Utazási Ügynök megkapja ezt az összetett kérést. LLM-jét használva végiggondolja a feladatot, és megállapítja, hogy más specializált ügynökökkel kell kommunikálnia.

3. **Ügynökök közti kommunikáció**: Az Utazási Ügynök az A2A protokollt alkalmazva csatlakozik downstream ügynökökhöz, mint például egy „Légitársaság Ügynök”, „Szálloda Ügynök” és „Autókölcsönző Ügynök”, amelyek különböző cégekhez tartoznak.

4. **Feladat delegálása**: Az Utazási Ügynök konkrét feladatokat (pl. „Keress járatokat Honolulu-ba”, „Foglalj szállást”, „Kölcsönözz autót”) küld ezeknek a specializált ügynököknek, akik saját LLM-eket és eszközöket használnak (akár maguk is MCP szerverek lehetnek) a foglalás egyes részeinek elvégzésére.

5. **Konszolidált válasz**: Miután az összes downstream ügynök befejezte a feladatait, az Utazási Ügynök összegyűjti az eredményeket (járatszámítás, szállodai visszaigazolás, autókölcsönzés), és részletes, csevegés-szerű választ küld vissza a felhasználónak.

## Természetes Nyelvű Web (NLWeb)

A weboldalak régóta a fő módját jelentik az interneten elérhető információk és adatok használatának.

Nézzük meg az NLWeb különböző komponenseit, az NLWeb előnyeit és egy példát arra, hogyan működik az NLWeb az utazási alkalmazásunkban.

### Az NLWeb összetevői

- **NLWeb alkalmazás (Core Service Code)**: A rendszer, amely feldolgozza a természetes nyelvű kérdéseket. Kapcsolja a platform különböző részeit a válaszok elkészítéséhez. Úgy tekinthetünk rá, mint a **weboldal természetes nyelvű funkcióinak motorjára**.

- **NLWeb protokoll**: Ez egy **egyszerű szabályrendszer a természetes nyelvű interakcióhoz** egy weboldallal. JSON formátumban (gyakran Schema.org használatával) küldi vissza a válaszokat. Célja, hogy egyszerű alapot teremtsen az „AI Web” számára, ugyanúgy, ahogy a HTML tette lehetővé a dokumentumok online megosztását.

- **MCP szerver (Model Context Protocol végpont)**: Minden NLWeb beállítás egyben egy **MCP szerverként** is működik. Ez azt jelenti, hogy **eszközöket (például `ask` metódust) és adatokat** oszthat meg más AI rendszerekkel. Gyakorlatban ez azt jelenti, hogy a weboldal tartalma és képességei elérhetővé válnak AI ügynökök számára, így a webhely része lesz a „ügynök ökoszisztémának”.

- **Beágyazási modellek (Embedding Models)**: Ezeket a modelleket arra használják, hogy a weboldal tartalmát olyan numerikus ábrázolásokká (vektorokká, embeddings) alakítsák, amelyek számítógéppel összehasonlíthatók és kereshetők. Ezeket egy speciális adatbázisban tárolják, és a felhasználók választhatnak, melyik beágyazási modellt szeretnék használni.

- **Vektor adatbázis (kereső mechanizmus)**: Ez az adatbázis tárolja a weboldal tartalmának beágyazásait. Amikor valaki kérdez, az NLWeb ezt a vektor adatbázist használja, hogy gyorsan megtalálja a legrelevánsabb információkat. Gyors válaszlehetőségeket ad, amelyeket hasonlóság alapján rangsorol. Az NLWeb különféle vektortároló rendszerekkel működik, például Qdrant, Snowflake, Milvus, Azure AI Search és Elasticsearch.

### NLWeb példa

![NLWeb](../../../translated_images/hu/nlweb-diagram.c1e2390b310e5fe4.webp)

Vegyük újra az utazási foglaló weboldalunkat, de most NLWeb által támogatva.

1. **Adatfeltöltés**: Az utazási weboldal meglévő termékkatalógusai (pl. járatlisták, szállodai leírások, túra csomagok) Schema.org szerint vannak formázva vagy RSS feedeken keresztül betöltve. Az NLWeb eszközei feldolgozzák ezt a strukturált adatot, létrehozzák a beágyazásokat, és eltárolják ezeket helyi vagy távoli vektor adatbázisban.

2. **Természetes nyelvű lekérdezés (ember)**: Egy felhasználó meglátogatja a weboldalt, és a menük böngészése helyett a csevegőfelületen beírja: „Találj számomra családbarát szállodát Honolulu-ban medencével a jövő hétre.”

3. **NLWeb feldolgozás**: Az NLWeb alkalmazás megkapja a lekérdezést. Elküldi az LLM-nek megértésre, egyidejűleg lekérdezve a vektor adatbázist a releváns szállodákért.

4. **Pontosságos találatok**: Az LLM segít értelmezni az adatbázisból jövő keresési eredményeket, azonosítja a legjobb találatokat olyan kritériumok alapján, mint „családbarát”, „medence” és „Honolulu”, majd természetes nyelvű választ formáz. Fontos, hogy a válasz valódi szállodákra hivatkozik, nem kitalált információra.

5. **AI ügynök interakció**: Mivel az NLWeb MCP szerverként is működik, egy külső AI utazási ügynök is csatlakozhat ehhez a weboldal NLWeb példányához. Az AI ügynök használhatja az `ask` MCP metódust, hogy közvetlenül kérdezzen: `ask("Ajánlottak a szálloda környékén vegánbarát éttermeket?")`. Az NLWeb feldolgozza ezt a lekérdezést, kihasználva az éttermek adatbázisát (amennyiben az betöltött), és struktúrált JSON választ küld.

### További kérdése van MCP/A2A/NLWeb-ről?

Csatlakozzon a [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) közösséghez, ahol találkozhat más tanulókkal, részt vehet irodai órákon és választ kaphat AI ügynökökkel kapcsolatos kérdéseire.

## Források

- [MCP kezdőknek](https://aka.ms/mcp-for-beginners)  
- [MCP dokumentáció](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb tárház](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framewrok)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Felelősség kizárása**:
Ezt a dokumentumot az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti, anyanyelvi dokumentum tekinthető a hiteles forrásnak. Kritikus információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy félreértelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->