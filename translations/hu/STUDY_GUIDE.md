# AI Ügynökök Kezdőknek - Tanulmányi Útmutató és Kurzus Összefoglaló

Ez az útmutató összefoglalja az "AI Ügynökök Kezdőknek" kurzust, és magyarázatot ad az AI ügynökök építéséhez szükséges kulcsfogalmakra, keretrendszerekre és tervezési mintákra.

## 1. Bevezetés az AI Ügynökökbe

**Mik azok az AI ügynökök?**
Az AI ügynökök olyan rendszerek, amelyek kibővítik a Nagy Nyelvi Modellek (LLM-ek) képességeit azáltal, hogy hozzáférést biztosítanak számukra **eszközökhöz**, **tudáshoz** és **memóriához**. Ellentétben egy szabványos LLM chatbot-tal, amely csak a képzési adatok alapján generál szöveget, egy AI ügynök képes:
- **Észlelni** környezetét (érzékelők vagy bemenetek segítségével).
- **Gondolkodni** arról, hogyan oldjon meg egy problémát.
- **Cselekedni**, hogy változtasson a környezeten (aktuátorok vagy eszközvégrehajtás által).

**Az ügynök kulcselemei:**
- **Környezet**: Az a tér, ahol az ügynök működik (pl. egy foglalási rendszer).
- **Érzékelők**: Információgyűjtés mechanizmusai (pl. API olvasása).
- **Aktuátorok**: Műveletek végrehajtására szolgáló mechanizmusok (pl. e-mail küldése).
- **Agy (LLM)**: Az a gondolkodó motor, amely megtervezi és eldönti, mely műveleteket kell végrehajtani.

## 2. Ügynöki Keretrendszerek

A kurzus három fő keretrendszert tárgyal az ügynökök építéséhez:

| Keretrendszer | Fókusz | Legjobb Felhasználás |
|---------------|--------|---------------------|
| **Semantic Kernel** | Termeléskész SDK .NET/Python számára | Vállalati alkalmazások, AI integrálása meglévő kódokkal. |
| **AutoGen** | Többügynökös együttműködés | Összetett helyzetek, ahol több specializált ügynök kommunikál egymással. |
| **Azure AI Agent Service** | Felügyelt felhőszolgáltatás | Biztonságos, skálázható telepítés beépített állapotkezeléssel. |

## 3. Ügynöki Tervezési Minták

A tervezési minták segítenek az ügynökök működésének megbízható struktúrájának kialakításában a problémamegoldás érdekében.

### **Eszköz Használati Minta** (4. lecke)
Ez a minta lehetővé teszi az ügynököknek, hogy interakcióba lépjenek a külvilággal.
- **Fogalom**: Az ügynök egy "sémát" kap (elérhető funkciók és paramétereik listáját). Az LLM eldönti, *melyik* eszközt hívja meg és *milyen* argumentumokkal a felhasználó kérésének alapján.
- **Folyamat**: Felhasználói kérés -> LLM -> **Eszköz kiválasztása** -> **Eszköz végrehajtása** -> LLM (eszköz kimenetével) -> Végső válasz.
- **Használati esetek**: Valós idejű adatok lekérése (időjárás, tőzsdeárfolyamok), számítások végzése, kód futtatása.

### **Tervezési Minta** (7. lecke)
Ez a minta lehetővé teszi az ügynökök számára összetett, több lépésből álló feladatok megoldását.
- **Fogalom**: Az ügynök lebontja a magas szintű célt kisebb, sorozatos részfeladatokra.
- **Megközelítések**:
  - **Feladatlebontás**: A "Tervezz egy utazást" feldarabolása "Repülőjegy foglalás", "Szállás foglalás", "Autóbérlés".
  - **Ismétlődő tervezés**: A terv újraértékelése az előző lépések kimenetére alapozva (pl. ha a járat tele van, másik dátumot választ).
- **Megvalósítás**: Gyakran "Tervező" ügynök készít egy strukturált tervet (pl. JSON formátumban), amit aztán más ügynökök hajtanak végre.

## 4. Tervezési Elvek

Az ügynökök tervezésekor három dimenziót érdemes figyelembe venni:
- **Tér**: Az ügynökök kapcsolják össze az embereket és a tudást, hozzáférhetőek legyenek, de ne tolakodóak.
- **Idő**: Az ügynökök tanuljanak a *múltból*, nyújtsanak releváns ösztönzést a *jelenben*, és alkalmazkodjanak a *jövőhöz*.
- **Mag**: Fogadják el a bizonytalanságot, de alakítsanak ki bizalmat átláthatósággal és felhasználói kontrollal.

## 5. A Főbb Leckék Összefoglalása

- **1. lecke**: Az ügynökök rendszerek, nem csak modellek. Észlelnek, gondolkodnak és cselekednek.
- **2. lecke**: A Semantic Kernel és az AutoGen keretrendszerek elvonják az eszközhívás és állapotkezelés összetettségét.
- **3. lecke**: Tervezéskor gondolni kell az átláthatóságra és a felhasználói irányításra.
- **4. lecke**: Az eszközök az ügynök "kezei". A séma definíciója kulcsfontosságú, hogy az LLM értse, hogyan használja őket.
- **7. lecke**: A tervezés az ügynök "végrehajtó funkciója", amely lehetővé teszi komplex munkafolyamatok kezelését.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordító szolgáltatás [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti, anyanyelvi dokumentum tekintendő a hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->