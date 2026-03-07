[![Többügynökös tervezés](../../../translated_images/hu/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Kattints a fenti képre, hogy megtekinthesd a lecke videóját)_

# Többügynökös tervezési minták

Amint elkezdesz dolgozni egy többrésztvevős (több ügynököt érintő) projekten, meg kell fontolnod a többügynökös tervezési mintát. Azonban nem mindig egyértelmű, mikor érdemes áttérni több ügynökre, és mik az előnyei.

## Bevezetés

Ebben a leckében a következő kérdésekre keressük a választ:

- Milyen helyzetekben alkalmazható a többügynökös megközelítés?
- Milyen előnyei vannak annak, ha több ügynök dolgozik együtt egyetlen ügynökhöz képest, amely több feladatot végez?
- Mik a többügynökös tervezési minta megvalósításának építőkövei?
- Hogyan nyerhetünk betekintést abba, hogy a több ügynök hogyan lép kölcsönhatásba egymással?

## Tanulási célok

A lecke elvégzése után képes leszel:

- Felismerni azokat a helyzeteket, ahol a többügynökös megoldás alkalmazható
- Felismerni a többügynökös megközelítés előnyeit az egyetlen ügynökhöz képest
- Megérteni a többügynökös tervezési minta megvalósításának építőköveit

Mi a nagyobb kép?

*A többügynökös megoldás egy tervezési minta, amely lehetővé teszi, hogy több ügynök együttműködjön egy közös cél eléréséért*.

Ezt a mintát sok területen alkalmazzák, többek között robotikában, autonóm rendszerekben és elosztott számítástechnikában.

## Olyan helyzetek, ahol a többügynökös megoldás alkalmazható

Milyen helyzetekben érdemes több ügynököt alkalmazni? A válasz az, hogy számos olyan helyzet van, ahol több ügynök használata előnyös, különösen az alábbi esetekben:

- **Nagy munkaterhelés**: A nagy munkaterheléseket kisebb feladatokra bonthatjuk, és különböző ügynököknek oszthatjuk ki, lehetővé téve a párhuzamos feldolgozást és a gyorsabb befejezést. Erre példa egy nagyméretű adatfeldolgozási feladat.
- **Komplex feladatok**: A komplex feladatokat, hasonlóan a nagy munkaterhelésekhez, kisebb alfeladatokra lehet bontani, és különböző ügynököknek lehet kiosztani, amelyek mindegyike a feladat egy adott aspektusára szakosodott. Erre jó példa az autonóm járművek esete, ahol külön ügynökök kezelik a navigációt, az akadályfelismerést és a kommunikációt más járművekkel.
- **Sokféle szakértelem**: Különböző ügynökök különböző szakértelemmel rendelkezhetnek, így hatékonyabban kezelhetik a feladat különböző aspektusait, mint egyetlen ügynök. Erre jó példa az egészségügy, ahol az ügynökök kezelhetik a diagnosztikát, a kezelési terveket és a betegmegfigyelést.

## Előnyök egyetlen ügynökhöz képest

Egyetlen ügynökös rendszer jól működhet egyszerű feladatoknál, de összetettebb feladatok esetén a több ügynök használata több előnnyel járhat:

- **Specializáció**: Minden ügynök egy adott feladatra specializálódhat. Egyetlen ügynök specializáció hiányában mindent megpróbálhat elvégezni, de összetett feladatok esetén bizonytalan lehet, mit tegyen. Előfordulhat, hogy végül olyan feladatot végez el, amelyhez nem a legalkalmasabb.
- **Skálázhatóság**: Könnyebb a rendszert skálázni több ügynök hozzáadásával, mint egyetlen ügynök túlterhelésével.
- **Hibatűrés**: Ha egy ügynök meghibásodik, a többiek tovább működhetnek, biztosítva a rendszer megbízhatóságát.

Vegyünk egy példát: foglaljunk egy utazást egy felhasználónak. Egyetlen ügynöknek kellene kezelnie az utazásfoglalás minden aspektusát, a járatok megtalálásától a szállodák és bérautók lefoglalásáig. Ha ezt egyetlen ügynökkel szeretnénk megoldani, az ügynöknek eszközökkel kellene rendelkeznie az összes ilyen feladat kezelésére. Ez egy összetett és monolitikus rendszert eredményezhet, amelyet nehéz karbantartani és skálázni. Ezzel szemben egy többügynökös rendszerben különböző ügynökök specializálódhatnak a járatok keresésére, a szállodafoglalásra és a bérautók kezelésére. Ez a rendszer modulárisabbá, könnyebben karbantarthatóvá és skálázhatóbbá teszi a megoldást.

Hasonlítsuk össze ezt egy családi utazási irodával és egy franchise-szal működő utazási irodával. A családi iroda egyetlen ügynököt alkalmazna az utazásfoglalás minden aspektusának kezelésére, míg a franchise esetén különböző ügynökök különböző feladatokat látnának el.

## A többügynökös tervezési minta megvalósításának építőkövei

Mielőtt megvalósíthatnád a többügynökös tervezési mintát, meg kell értened azokat az építőköveket, amelyek a mintát alkotják.

Tegyük ezt konkrétabbá azzal, hogy ismét megnézzük az utazásfoglalás példáját. Ebben az esetben az építőkövek a következők lennének:

- **Ügynökök közötti kommunikáció**: A járatokat kereső, a szállodát foglaló és a bérautót kezelő ügynököknek kommunikálniuk és megosztaniuk kell az információkat a felhasználó preferenciáiról és korlátairól. El kell döntened a kommunikáció protokolljait és módszereit. Konkrétan ez azt jelenti, hogy a járatkereső ügynöknek kommunikálnia kell a szállodafoglaló ügynökkel, hogy a szálloda ugyanazokra a dátumokra legyen lefoglalva, mint a járat. Ez azt jelenti, hogy az ügynököknek meg kell osztaniuk az utazási dátumokra vonatkozó információkat, tehát el kell döntened, *mely ügynökök osztanak meg információt és hogyan osztják meg azt*.
- **Koordinációs mechanizmusok**: Az ügynököknek koordinálniuk kell tevékenységüket, hogy a felhasználó preferenciái és korlátai teljesüljenek. Egy felhasználói preferencia lehet például, hogy a szálloda legyen közel a repülőtérhez, míg egy korlát lehet, hogy a bérautók csak a repülőtéren érhetők el. Ez azt jelenti, hogy a szállodafoglaló ügynöknek össze kell hangolnia a működését a bérautó-foglaló ügynökkel, hogy a felhasználó igényei teljesüljenek. Tehát el kell döntened, *hogyan koordinálják egymást az ügynökök*.
- **Ügynök-architektúra**: Az ügynököknek olyan belső felépítéssel kell rendelkezniük, amely lehetővé teszi a döntéshozatalt és a felhasználóval való interakciókból való tanulást. Ez azt jelenti, hogy a járatkereső ügynök belső felépítése alkalmas legyen annak eldöntésére, mely járatokat ajánlja a felhasználónak. Tehát el kell döntened, *hogyan hoznak döntéseket az ügynökök és hogyan tanulnak a felhasználóval való interakciókból*. Egy példa arra, hogyan tanulhat és javulhat egy ügynök: a járatkereső ügynök használhat egy gépi tanulási modellt, hogy a felhasználó korábbi preferenciái alapján járatokat ajánljon.
- **Átláthatóság a többügynökös interakciókban**: Láthatósággal kell rendelkezned arra vonatkozóan, hogyan lépnek kölcsönhatásba egymással az ügynökök. Ez azt jelenti, hogy eszközökre és technikákra van szükséged az ügynöktevékenységek és -interakciók nyomon követéséhez. Ez megvalósulhat naplózó és megfigyelő eszközök, vizualizációs eszközök és teljesítménymutatók formájában.
- **Többügynökös minták**: Különböző minták léteznek a többügynökös rendszerek megvalósítására, például központosított, decentralizált és hibrid architektúrák. El kell döntened, melyik minta illeszkedik legjobban az esethez.
- **Ember a folyamatban**: Többnyire ember is részt vesz a folyamatban, és meg kell határoznod, mikor kérjenek az ügynökök emberi beavatkozást. Ez lehet például, ha a felhasználó kíván egy konkrét szállodát vagy járatot, amelyet az ügynökök nem ajánlottak, vagy ha megerősítést kérnek a foglalás előtt.

## Átláthatóság a többügynökös interakciókban

Fontos, hogy lásd, hogyan lépnek kölcsönhatásba egymással a különböző ügynökök. Ez az átláthatóság elengedhetetlen a hibakereséshez, optimalizáláshoz és a teljes rendszer hatékonyságának biztosításához. Ennek eléréséhez eszközökre és technikákra van szükség az ügynöktevékenységek és -interakciók nyomon követéséhez. Ez megvalósulhat naplózó és megfigyelő eszközök, vizualizációs eszközök és teljesítménymutatók formájában.

Például egy utazásfoglalás esetén lehet egy irányítópultod, amely megmutatja az egyes ügynökök státuszát, a felhasználó preferenciáit és korlátait, valamint az ügynökök közötti interakciókat. Ez az irányítópult megjelenítheti a felhasználó utazási dátumait, a járatügynök által ajánlott járatokat, a szállodaugynök által ajánlott szállodákat és a bérautó-ügynök által ajánlott autókat. Ez tiszta képet ad arról, hogyan lépnek kapcsolatba az ügynökök, és hogy a felhasználó igényei teljesülnek-e.

Nézzük részletesebben ezeket a szempontokat.

- **Naplózó és megfigyelő eszközök**: Szeretnéd, ha minden egyes ügynök által végrehajtott művelet naplózásra kerülne. Egy naplóbejegyzés tartalmazhat információt az ügynökről, aki a műveletet végrehajtotta, a végrehajtott műveletről, annak időpontjáról és a művelet eredményéről. Ezek az információk hibakeresésre, optimalizálásra és más célokra használhatók.
- **Vizualizációs eszközök**: A vizualizációs eszközök segíthetnek az ügynökök közötti interakciók intuitív megjelenítésében. Például lehet egy gráf, amely megmutatja az információ áramlását az ügynökök között. Ez segíthet azonosítani a szűk keresztmetszeteket, hatékonysági problémákat és egyéb rendszerbeli gondokat.
- **Teljesítménymutatók**: A teljesítménymutatók segítenek nyomon követni a többügynökös rendszer hatékonyságát. Például mérheted egy feladat elvégzéséhez szükséges időt, az egységnyi idő alatt elvégzett feladatok számát és az ügynökök által adott ajánlások pontosságát. Ezek az adatok segíthetnek a fejlesztési lehetőségek azonosításában és a rendszer optimalizálásában.

## Többügynökös minták

Merüljünk el néhány konkrét mintában, amelyeket használhatunk többügynökös alkalmazások létrehozásához. Íme néhány érdekes minta, amelyet érdemes megfontolni:

### Csoportos csevegés

Ez a minta hasznos, ha csoportos csevegőalkalmazást szeretnél létrehozni, ahol több ügynök is kommunikálhat egymással. Tipikus felhasználási esetek: csapatmunka, ügyfélszolgálat és közösségi hálózatok.

Ebben a mintában minden ügynök egy felhasználót képvisel a csoportos csevegésben, és az üzeneteket üzenetküldési protokollon keresztül cserélik. Az ügynökök üzeneteket küldhetnek a csoportnak, fogadhatnak üzeneteket, és válaszolhatnak más ügynökök üzeneteire.

Ezt a mintát megvalósíthatod egy központosított architektúrával, ahol az összes üzenetet egy központi szerver irányítja, vagy egy decentralizált architektúrával, ahol az üzenetek közvetlenül cserélődnek.

![Csoportos csevegés](../../../translated_images/hu/multi-agent-group-chat.ec10f4cde556babd.webp)

### Feladatátadás

Ez a minta akkor hasznos, ha olyan alkalmazást szeretnél létrehozni, ahol több ügynök adhat át feladatokat egymásnak.

Tipikus felhasználási esetek: ügyfélszolgálat, feladatkezelés és munkafolyamat-automatizálás.

Ebben a mintában minden ügynök egy feladatot vagy egy lépést képvisel egy munkafolyamatban, és az ügynökök előre definiált szabályok alapján adhatják át a feladatokat más ügynököknek.

![Feladatátadás](../../../translated_images/hu/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Kollaboratív szűrés

Ez a minta akkor hasznos, ha olyan alkalmazást szeretnél létrehozni, ahol több ügynök együttműködve ad ajánlásokat a felhasználóknak.

Azért érdemes több ügynököt bevonni, mert mindegyik ügynök más-más szakértelemmel rendelkezhet, és különböző módon járulhat hozzá az ajánlási folyamathoz.

Vegyünk egy példát: egy felhasználó ajánlást szeretne kapni arról, melyik részvényt érdemes megvásárolni a tőzsdén.

- **Iparági szakértő**: Egy ügynök lehet iparági szakértő.
- **Technikai elemző**: Egy másik ügynök technikai elemzésekben lehet jártas.
- **Fundamentális elemző**: Egy harmadik ügynök a fundamentális elemzésben lehet szakértő. Az együttműködés révén ezek az ügynökök átfogóbb ajánlást adhatnak a felhasználónak.

![Ajánlás](../../../translated_images/hu/multi-agent-filtering.d959cb129dc9f608.webp)

## Forgatókönyv: Visszatérítési folyamat

Gondoljunk egy olyan esetre, amikor egy vásárló visszatérítést szeretne kapni egy termékért; ebben a folyamatban több ügynök is részt vehet, de osszuk fel őket a visszatérítési folyamathoz specifikus ügynökökre és az olyan általános ügynökökre, amelyeket más folyamatokban is lehet használni.

**A visszatérítési folyamathoz kapcsolódó ügynökök**:

Az alábbiakban néhány, a visszatérítési folyamatban érintett ügynököt sorolunk fel:

- **Vásárlói ügynök**: Ez az ügynök a vásárlót képviseli, és felelős a visszatérítési folyamat elindításáért.
- **Eladói ügynök**: Ez az ügynök az eladót képviseli, és felelős a visszatérítés feldolgozásáért.
- **Fizetési ügynök**: Ez az ügynök a fizetési folyamatot képviseli, és felelős a vásárló pénzének visszatérítéséért.
- **Megoldási ügynök**: Ez az ügynök a problémamegoldást képviseli, és felelős bármilyen, a visszatérítési folyamat során felmerülő probléma rendezéséért.
- **Megfelelőségi ügynök**: Ez az ügynök a megfelelőséget képviseli, és biztosítja, hogy a visszatérítési folyamat megfeleljen a szabályozásoknak és belső irányelveknek.

**Általános ügynökök**:

Ezeket az ügynököket más üzleti folyamatokban is felhasználhatod.

- **Szállítmányozási ügynök**: Ez az ügynök a szállítási folyamatot képviseli, és felelős a termék eladóhoz történő visszajuttatásáért. Ezt az ügynököt használhatod mind a visszatérítési folyamatban, mind általános termékszállításnál, például vásárlás esetén.
- **Visszajelzési ügynök**: Ez az ügynök a visszajelzések gyűjtéséért felelős, és a vásárlótól gyűjthetsz visszajelzést bármikor, nem csak a visszatérítési folyamat során.
- **Eszkalációs ügynök**: Ez az ügynök a probléma eszkalálásáért felelős, és magasabb szintű támogatás felé továbbítja az ügyeket. Ezt az ügynököt bármely olyan folyamatban használhatod, ahol szükség van probléma továbbítására.
- **Értesítési ügynök**: Ez az ügynök az értesítési folyamatot képviseli, és felelős az értesítések küldéséért a vásárlónak a visszatérítési folyamat különböző szakaszaiban.
- **Analitikai ügynök**: Ez az ügynök az analitika folyamatát képviseli, és felelős a visszatérítési folyamathoz kapcsolódó adatok elemzéséért.
- **Audit ügynök**: Ez az ügynök az audit folyamatáért felel, és felügyeli a visszatérítési folyamatot, hogy biztosítsa annak helyes végrehajtását.
- **Jelentéskészítő ügynök**: Ez az ügynök a jelentések készítéséért felelős, és jelentéseket generál a visszatérítési folyamatról.
- **Tudásügynök**: Ez az ügynök a tudáskezelést képviseli, és felelős a visszatérítési folyamathoz kapcsolódó tudásbázis karbantartásáért. Ez az ügynök ismeretekkel rendelkezhet a visszatérítésekről és vállalkozásod más területeiről is.
- **Biztonsági ügynök**: Ez az ügynök a biztonsági folyamatokat képviseli, és biztosítja a visszatérítési folyamat biztonságosságát.
- **Minőségügyi ügynök**: Ez az ügynök a minőségbiztosítást képviseli, és felelős a visszatérítési folyamat minőségének biztosításáért.

Előzőleg elég sok ügynököt felsoroltunk, mind a visszatérítési folyamathoz specifikusakat, mind azokat az általános ügynököket, amelyeket vállalkozásod más területein is használhatsz. Remélhetőleg ez ötletet ad arra, hogyan dönthetsz arról, mely ügynököket érdemes alkalmazni a többügynökös rendszeredben.

## Feladat

Tervezd meg egy többügynökös rendszert egy ügyfélszolgálati folyamathoz. Azonosítsd a folyamatban részt vevő ügynököket, azok szerepét és felelősségi köreit, valamint azt, hogyan lépnek kölcsönhatásba egymással. Vedd figyelembe mind az ügyfélszolgálati folyamathoz specifikus ügynököket, mind azokat az általános ügynököket, amelyeket vállalkozásod más részein is felhasználhatsz.
> Gondolkodj el rajta, mielőtt elolvasod a következő megoldást, lehet, hogy több ügynökre lesz szükséged, mint gondolod.
> TIPP: Gondolj a vevőszolgálati folyamat különböző szakaszaira, és vedd figyelembe az adott rendszerhez szükséges ügynököket is.

## Megoldás

[Megoldás](./solution/solution.md)

## Tudásellenőrzések

Question: Mikor érdemes többügynökös megoldást alkalmazni?

- [ ] A1: Amikor kis munkaterhelésed és egyszerű feladatod van.
- [ ] A2: Amikor nagy munkaterhelésed van.
- [ ] A3: Amikor egyszerű feladatod van.

[Megoldás kvíz](./solution/solution-quiz.md)

## Összefoglalás

Ebben a leckében megvizsgáltuk a többügynökös tervezési mintát, beleértve azokat a helyzeteket, amikor többügynökös megközelítést érdemes alkalmazni, a többügynökös rendszer egyetlen ügynökhöz képesti előnyeit, a többügynökös tervezési minta megvalósításának építőköveit, valamint azt, hogyan nyerhetünk betekintést abba, hogy a több ügynök hogyan lép kölcsönhatásba egymással.

### További kérdéseid vannak a többügynökös tervezési mintával kapcsolatban?

Csatlakozz a [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) közösséghez, hogy találkozz más tanulókkal, részt vehess konzultációs órákon és választ kapj AI-ügynökökkel kapcsolatos kérdéseidre.

## További erőforrások

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework dokumentáció</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Agentikus tervezési minták</a>


## Previous Lesson

[Planning Design](../07-planning-design/README.md)

## Next Lesson

[Metacognition in AI Agents](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Felelősségkizárás:
Ezt a dokumentumot a mesterséges intelligencia alapú fordítószolgáltatás, a Co-op Translator (https://github.com/Azure/co-op-translator) segítségével fordítottuk le. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum anyanyelven írt változata tekintendő hiteles forrásnak. Kritikus információk esetén emberi, szakmai fordítást javaslunk. Nem vállalunk felelősséget az ezen fordítás használatából eredő bármilyen félreértésért vagy téves értelmezésért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->