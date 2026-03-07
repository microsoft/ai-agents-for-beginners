# AI ügynökök kezdőknek - Tanulási útmutató és tanfolyam összefoglaló

Ez az útmutató összefoglalja az "AI Agents for Beginners" tanfolyamot, és elmagyarázza az AI ügynökök építéséhez szükséges kulcsfogalmakat, keretrendszereket és tervezési mintákat.

## 1. Bevezetés az AI ügynökökhöz

**Mik az AI ügynökök?**
Az AI ügynökök olyan rendszerek, amelyek kiterjesztik a nagy nyelvi modellek (LLM-ek) képességeit azáltal, hogy hozzáférést adnak számukra **eszközökhöz**, **tudáshoz**, és **memóriához**. Ellentétben egy szabványos LLM chatbottal, amely csak a képzési adatok alapján generál szöveget, egy AI ügynök képes:
- **Észleli** a környezetét (szenzorokon vagy bemeneteken keresztül).
- **Gondolkodik** arról, hogyan oldjon meg egy problémát.
- **Cselekszik** a környezet megváltoztatása érdekében (aktuátorokon vagy eszközök futtatásán keresztül).

**Egy ügynök kulcsfontosságú összetevői:**
- **Környezet**: Az a tér, ahol az ügynök működik (pl. egy foglalási rendszer).
- **Szenzorok**: Mechanizmusok az információgyűjtésre (pl. egy API olvasása).
- **Aktuátorok**: Mechanizmusok cselekvésre (pl. e-mail küldése).
- **Agy (LLM)**: A következtető motor, amely tervezi és eldönti, mely intézkedéseket kell végrehajtani.

## 2. Agentic Frameworks

A tanfolyam a **Microsoft Agent Framework (MAF)** és az **Azure AI Foundry Agent Service V2** használatát ismerteti az ügynökök építéséhez:

| Component | Focus | Best For |
|-----------|-------|----------|
| **Microsoft Agent Framework** | Unified Python/C# SDK for agents, tools, and workflows | Building agents with tools, multi-agent workflows, and production patterns. |
| **Azure AI Foundry Agent Service** | Managed cloud runtime | Secure, scalable deployment with built-in state management, observability, and trust. |

## 3. Agentic Design Patterns

A tervezési minták segítenek strukturálni az ügynökök működését, hogy megbízhatóan oldjanak meg problémákat.

### **Eszközhasználati minta** (4. lecke)
Ez a minta lehetővé teszi az ügynökök számára, hogy kölcsönhatásba lépjenek a külvilággal.
- **Koncepció**: Az ügynök rendelkezésére bocsátanak egy "sémát" (a rendelkezésre álló függvények és paramétereik listája). Az LLM a felhasználó kérésének alapján dönt arról, *melyik* eszközt hívja meg és *milyen* argumentumokkal.
- **Flow**: Felhasználói kérés -> LLM -> **Eszköz kiválasztása** -> **Eszköz végrehajtása** -> LLM (eszköz kimenetével) -> Végső válasz.
- **Használati esetek**: Valós idejű adatok lekérése (időjárás, részvényárak), számítások elvégzése, kód futtatása.

### **Tervezési minta** (7. lecke)
Ez a minta lehetővé teszi az ügynökök számára, hogy összetett, többlépéses feladatokat oldjanak meg.
- **Koncepció**: Az ügynök egy magas szintű célt lebont kisebb részfeladatokra.
- **Megközelítések**:
  - **Feladatlebontás**: A "Utazás megtervezése" lebontása "Járat foglalása", "Szálloda foglalása", "Autóbérlés" részfeladatokra.
  - **Iteratív tervezés**: A terv újbóli értékelése az előző lépések kimenete alapján (pl. ha a járat tele van, válasszon másik dátumot).
- **Megvalósítás**: Gyakran egy "Tervező" ügynököt foglal magában, amely strukturált tervet (pl. JSON) generál, majd azt más ügynökök hajtják végre.

## 4. Design Principles

Az ügynökök tervezésekor három dimenziót vegyünk figyelembe:
- **Tér**: Az ügynököknek össze kell kapcsolniuk az embereket és a tudást, hozzáférhetőknek kell lenniük, de legyenek nem tolakodók.
- **Idő**: Az ügynököknek tanulniuk kell a *Múltból*, releváns ösztönzéseket kell adniuk a *Mostban*, és alkalmazkodniuk kell a *Jövőre*.
- **Alap**: Fogadjuk el a bizonytalanságot, de teremtsünk bizalmat átláthatóság és felhasználói kontroll révén.

## 5. Summary of Key Lessons

- **1. lecke**: Az ügynökök rendszerek, nem csak modellek. Észlelnek, gondolkodnak és cselekednek.
- **2. lecke**: A Microsoft Agent Framework elrejti az eszközmeghívás és az állapotkezelés összetettségét.
- **3. lecke**: Tervezzen átláthatóságot és felhasználói kontrollt szem előtt tartva.
- **4. lecke**: Az eszközök az ügynök "kezei". A séma meghatározása kulcsfontosságú ahhoz, hogy az LLM megértse, hogyan használja őket.
- **7. lecke**: A tervezés az ügynök "végrehajtó funkciója", amely lehetővé teszi számára, hogy összetett munkafolyamatokat kezeljen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Felelősségkizárás**:
Ezt a dokumentumot az AI fordítószolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével fordítottuk. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti, anyanyelvi dokumentum tekintendő a hiteles forrásnak. Kritikus jelentőségű információk esetén professzionális, emberi fordítást ajánlunk. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->