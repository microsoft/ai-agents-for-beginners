# AI ügynökök kezdőknek - Tanulmányi útmutató és kurzus összefoglaló

Ez az útmutató összefoglalót nyújt az "AI ügynökök kezdőknek" kurzusról és elmagyarázza a főbb fogalmakat, keretrendszereket és tervezési mintákat az AI ügynökök építéséhez.

## 1. Bevezetés az AI ügynökökhöz

**Mik azok az AI ügynökök?**
Az AI ügynökök olyan rendszerek, amelyek kiterjesztik a Nagy nyelvi modellek (LLM-ek) képességeit azzal, hogy hozzáférést biztosítanak számukra **eszközökhöz**, **tudáshoz** és **memóriához**. Ellentétben egy szabványos LLM chatbot-tal, amely csak a tanító adatok alapján generál szöveget, egy AI ügynök képes:
- **Észlelni** a környezetét (szenzorok vagy bemenetek révén).
- **Értelmezni**, hogyan oldjon meg egy problémát.
- **Cselekedni** a környezet megváltoztatása érdekében (aktuátorok vagy eszközvégrehajtás révén).

**Az ügynök kulcsfontosságú összetevői:**
- **Környezet**: Az a tér, ahol az ügynök működik (pl. egy foglalási rendszer).
- **Szenzorok**: Mechanizmusok az információgyűjtésre (pl. egy API olvasása).
- **Aktuátorok**: Mechanizmusok a műveletek végrehajtására (pl. e-mail küldése).
- **Agy (LLM)**: A tervezésért és döntéshozatalért felelős motor, amely megtervezi és eldönti, mely műveleteket hajtsa végre.

## 2. Ügynöki keretrendszerek

A kurzus a **Microsoft Agent Framework (MAF)**-ot használja az ügynökök építéséhez együtt az **Azure AI Foundry Agent Service V2**-vel:

| Component | Focus | Best For |
|-----------|-------|----------|
| **Microsoft Agent Framework** | Egységes Python/C# SDK ügynökökhöz, eszközökhöz és munkafolyamatokhoz | Ügynökök építése eszközökkel, többügynöki munkafolyamatokkal és éles üzemmintákkal. |
| **Azure AI Foundry Agent Service** | Felügyelt felhő futtatókörnyezet | Biztonságos, skálázható telepítés beépített állapotkezeléssel, megfigyelhetőséggel és megbízhatósággal. |

## 3. Ügynöki tervezési minták

A tervezési minták segítenek struktúrálni, hogyan működnek az ügynökök, hogy megbízhatóan oldjanak meg problémákat.

### **Eszközhasználati minta** (Lesson 4)
Ez a minta lehetővé teszi az ügynökök számára, hogy kölcsönhatásba lépjenek a külvilággal.
- **Concept**: Az ügynöknek megadnak egy "sémát" (a rendelkezésre álló függvények és azok paramétereinek listáját). Az LLM eldönti, *melyik* eszközt hívja meg és *milyen* argumentumokkal a felhasználó kérésének alapján.
- **Flow**: Felhasználói kérés -> LLM -> **Tool Selection** -> **Tool Execution** -> LLM (eszköz kimenetével) -> Végső válasz.
- **Use Cases**: Valós idejű adatok lekérése (időjárás, részvényárak), számítások végrehajtása, kód futtatása.

### **Tervezési minta** (Lesson 7)
Ez a minta lehetővé teszi az ügynökök számára, hogy összetett, többlépéses feladatokat oldjanak meg.
- **Concept**: Az ügynök lebont egy magas szintű célt egy sor kisebb részfeladatra.
- **Approaches**:
  - **Task Decomposition**: A "Utazás megtervezése" feladatot bontja "Repülőjegy foglalása", "Szállás foglalása", "Autóbérlés" részfeladatokra.
  - **Iterative Planning**: A terv újraértékelése az előző lépések kimenete alapján (pl. ha a járat tele van, másik dátumot választani).
- **Implementation**: Gyakran egy "Tervező" ügynököt foglal magában, amely strukturált tervet (pl. JSON) generál, amelyet aztán más ügynökök hajtanak végre.

## 4. Tervezési alapelvek

Az ügynökök tervezésekor három dimenziót vegyünk figyelembe:
- **Space**: Az ügynökök kössék össze az embereket és a tudást, legyenek hozzáférhetők, de ne tolakodóak.
- **Time**: Az ügynökök tanuljanak a *múltból*, adjanak releváns ösztönzéseket a *jelenben*, és alkalmazkodjanak a *jövőhöz*.
- **Core**: Fogadjuk el a bizonytalanságot, de teremtsünk bizalmat átláthatósággal és felhasználói irányítással.

## 5. A kulcsfontosságú leckék összefoglalása

- **Lesson 1**: Az ügynökök rendszerek, nem csupán modellek. Észlelnek, gondolkodnak és cselekednek.
- **Lesson 2**: A Microsoft Agent Framework elrejti az eszközhívások és az állapotkezelés összetettségét.
- **Lesson 3**: Tervezéskor helyezzük előtérbe az átláthatóságot és a felhasználói irányítást.
- **Lesson 4**: Az eszközök az ügynök "kezei". A séma meghatározása kulcsfontosságú ahhoz, hogy az LLM megértse, hogyan használja azokat.
- **Lesson 7**: A tervezés az ügynök "végrehajtó funkciója", amely lehetővé teszi számára, hogy bonyolult munkafolyamatokat kezeljen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Felelősségkizárás:
Ezt a dokumentumot a Co-op Translator (https://github.com/Azure/co-op-translator) nevű mesterséges intelligencia alapú fordító szolgáltatással fordítottuk. Bár igyekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelven tekintendő hiteles forrásnak. Fontos információk esetén professzionális, emberi fordítást javaslunk. Nem vállalunk felelősséget a jelen fordítás használatából eredő félreértésekért vagy téves értelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->