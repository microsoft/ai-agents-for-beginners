[![Multi-Agent Design](../../../translated_images/hu/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Kattintson a fenti képre a lecke videójának megtekintéséhez)_

# Többügynökös tervezési minták

Amint elkezdi egy olyan projekten való munkát, amely több ügynököt is magában foglal, figyelembe kell vennie a többügynökös tervezési mintát. Ugyanakkor nem feltétlenül egyértelmű, hogy mikor kell áttérni több ügynökre, és mik az előnyei.

## Bevezetés

Ebben a leckében az alábbi kérdésekre keressük a választ:

- Milyen helyzetekben alkalmazhatók többügynökös rendszerek?
- Mik az előnyei annak, ha több ügynöket használunk egyetlen, több feladatot végző ügynök helyett?
- Mik a többügynökös tervezési minta megvalósításának építőkövei?
- Hogyan láthatjuk, hogy a több ügynök miként lép kölcsönhatásba egymással?

## Tanulási célok

A lecke végére képesnek kell lennie arra, hogy:

- Azonosítsa azokat a helyzeteket, ahol többügynökös rendszereket érdemes alkalmazni
- Felismerje a többügynökös rendszerek előnyeit az egyetlen ügynökhöz képest.
- Megértse a többügynökös tervezési minta megvalósításának építőköveit.

Mi a nagyobb kép?

*A többügynökös rendszerek egy olyan tervezési minta, amely lehetővé teszi, hogy több ügynök együttműködjön egy közös cél eléréséért*.

Ezt a mintát számos területen használják, többek között robotikában, autonóm rendszerekben és elosztott számítástechnikában.

## Helyzetek, ahol többügynökös rendszerek alkalmazhatók

Milyen helyzetek alkalmasak a többügynökös rendszerek használatára? A válasz az, hogy sok esetben előnyös több ügynök alkalmazása, különösen az alábbi esetekben:

- **Nagy terhelések**: A nagy terhelések kisebb feladatokra bonthatók és különböző ügynökökre oszthatók, így párhuzamos feldolgozás és gyorsabb befejezés érhető el. Ennek példája egy nagy adatfeldolgozó feladat.
- **Összetett feladatok**: Az összetett feladatok, akárcsak a nagy terhelések, kisebb alfeladatokra bonthatók, amelyeket különböző ügynökök végeznek, mindegyikük egy adott aspektusra specializálódva. Jó példa erre az autonóm járművek esete, ahol különböző ügynökök kezelik a navigációt, akadályfelismerést és a kommunikációt más járművekkel.
- **Sokféle szaktudás**: Különböző ügynökök eltérő szakértelemmel rendelkezhetnek, amelyek lehetővé teszik számukra, hogy egy adott feladat különböző aspektusait hatékonyabban kezeljék, mint egyetlen ügynök. Erre jó példa az egészségügy, ahol az ügynökök diagnosztikát, kezelési terveket és betegmegfigyelést vezérelhetnek.

## Többügynökös rendszer előnyei egyetlen ügynökhöz képest

Egy egyszerű feladat esetén egyetlen ügynök is jól működhet, de összetettebb feladatok esetén több ügynök használata több előnnyel járhat:

- **Specializáció**: Minden ügynök specializálódhat egy adott feladatra. Az egyetlen ügynök hiányzó specializációja miatt előfordulhat, hogy egy komplex feladat esetén tanácstalan lesz, vagy nem a legmegfelelőbb feladatot végzi el.
- **Skálázhatóság**: Könnyebb rendszereket skálázni több ügynök hozzáadásával, mint egyetlen ügynök túlterhelésével.
- **Hibatűrés**: Ha egy ügynök meghibásodik, a többi tovább működhet, biztosítva a rendszer megbízhatóságát.

Vegyünk egy példát: foglaljunk egy utazást egy felhasználónak. Egyetlen ügynöknek kellene kezelnie az összes utazásfoglalási folyamatot, a repülőjáratok keresésétől a szállodák és bérautók foglalásáig. Egyetlen ügynök esetén mindez bonyolult és monolitikus rendszert eredményezne, amely nehezen karbantartható és skálázható. Egy többügynökös rendszer viszont eltérő ügynököket alkalmazna a repülőjáratok, szállodák és bérautók foglalására, így a rendszer modulárisabb, könnyebben karbantartható és jobban skálázható lenne.

Hasonlítsuk össze ezt egy kis utazási irodával és egy franchise-szal működő utazási irodával. Az előző esetében egy ügynök kezelné az összes foglalási folyamatot, míg az utóbbinál különböző ügynökök különböző feladatokat látnának el.

## Többügynökös tervezési minta megvalósításának építőkövei

Mielőtt megvalósítaná a többügynökös tervezési mintát, meg kell értenie az ennek az elemző rendszernek építőköveit.

Tegyük ezt konkrétabbá azzal, hogy ismét megnézzük az utazásfoglalás példáját. Ebben az esetben az építőkövek a következők lennének:

- **Ügynökök közötti kommunikáció**: Az ügynökök, amelyek repülőjáratokat keresnek, szállodákat és bérautókat foglalnak, kommunikálniuk kell és meg kell osztaniuk az információkat a felhasználó preferenciáiról és korlátairól. El kell dönteni a kommunikáció protokolljait és módszereit. Konkrétan ez azt jelenti, hogy a repülőjáratot kereső ügynöknek kommunikálnia kell a szállodafoglalást végző ügynökkel, hogy a szálló ugyanarra az időszakra legyen lefoglalva, mint a repülőjegy. Vagyis az ügynököknek meg kell osztaniuk a felhasználó utazási időpontjait, vagyis el kell dönteni *mely ügynökök osztanak meg információt és hogyan*.
- **Koordinációs mechanizmusok**: Az ügynököknek össze kell hangolniuk tevékenységüket, hogy megfeleljenek a felhasználó preferenciáinak és korlátainak. Például a felhasználó azt szeretné, hogy a szálloda közel legyen a repülőtérhez, ugyanakkor az autókölcsönző csak a repülőtéren érhető el. Ez azt jelenti, hogy a szállodafoglaló ügynöknek koordinálnia kell a bérautós ügynökkel, hogy a felhasználó igényei teljesüljenek. Vagyis el kell dönteni *hogyan hangolják össze az ügynökök tevékenységüket*.
- **Ügynök architektúra**: Az ügynököknek belső struktúrával kell rendelkezniük, amely lehetővé teszi döntéshozást és a felhasználóval való interakciókból való tanulást. Például a repülőjáratokat kereső ügynöknek rendelkeznie kell a döntéshozatali struktúrával, hogy azt eldöntse, mely repülőjáratokat ajánlja. Vagyis el kell dönteni *hogyan hoznak döntéseket és tanulnak az ügynökök a felhasználóval való interakciókból*. Az egyik tanulási példa lehet, hogy a repülőjáratokat kereső ügynök gépi tanulási modellt használ az ajánlásokhoz a felhasználó múltbeli preferenciái alapján.
- **Áttekinthetőség a többügynökös interakciókban**: Látni kell, hogyan lépnek egymással kölcsönhatásba az ügynökök. Ehhez eszközöket és technikákat kell használni az ügynökök tevékenységének és kölcsönhatásainak követésére. Ez történhet naplózó- és monitorozó eszközök, vizualizációs eszközök és teljesítménymutatók formájában.
- **Többügynökös minták**: Különböző minták léteznek a többügynökös rendszerek megvalósításához, például központosított, decentralizált és hibrid architektúrák. El kell dönteni, melyik minta illik leginkább az adott feladathoz.
- **Ember a rendszerben**: A legtöbb esetben az ember is részt vesz a folyamatban, és meg kell határozni, hogy az ügynökök mikor kérjenek emberi beavatkozást. Ez történhet például úgy, hogy a felhasználó kéri egy adott szálloda vagy járat foglalását, amit az ügynökök nem ajánlottak, vagy megerősítést kérnek a foglalás előtt.

## Áttekinthetőség a többügynökös interakciókban

Fontos, hogy legyen áttekintése arról, miként lépnek egymásba a több ügynökök. Ez az áttekinthetőség elengedhetetlen hibakereséshez, optimalizáláshoz és a rendszer hatékonyságának biztosításához. Ehhez eszközökre és technikákra van szükség az ügynökök tevékenységének és interakcióinak követésére. Ez megvalósítható naplózó és monitorozó eszközökkel, vizualizációs eszközökkel és teljesítménymutatókkal.

Például egy utazásfoglalás esetén lehet egy irányítópult, amely mutatja az egyes ügynökök állapotát, a felhasználó preferenciáit és korlátait, valamint az ügynökök közötti interakciókat. Ez az irányítópult megmutathatja a felhasználó utazási időpontjait, a repülőjárat ajánlásokat, a szállodaszakértő javaslatait és a bérautó ügynök ajánlásait. Ez tiszta képet ad az ügynökök kölcsönhatásairól és arról, hogy a felhasználó igényei teljesülnek-e.

Nézzük meg ezeket az aspektusokat részletesebben.

- **Naplózó és monitorozó eszközök**: Fontos, hogy minden ügynöki tevékenységet naplózzanak. Egy naplóbejegyzés tartalmazhat információt az adott ügynökről, az elvégzett feladatról, a végrehajtás idejéről és eredményéről. Ezeket az adatokat hibakereséshez és optimalizáláshoz lehet felhasználni.

- **Vizualizációs eszközök**: Segítenek az ügynökök közötti interakciók intuitív megjelenítésében. Például lehet egy gráf, amely megmutatja az információáramlást az ügynökök között. Ez segíthet azonosítani szűk keresztmetszeteket, hatékonysági problémákat és egyéb gondokat.

- **Teljesítménymutatók**: Ezekkel mérhető a többügynökös rendszer hatékonysága. Például mérhető a feladatvégrehajtás ideje, a feladatok számának egységnyi időben történő teljesítése, és az ügynökök által adott ajánlások pontossága. Ezek az adatok segítenek azonosítani fejlesztési területeket és optimalizálni a rendszert.

## Többügynökös minták

Nézzünk néhány konkrét mintát, amelyek hasznosak lehetnek többügynökös alkalmazások létrehozásához. Íme néhány érdekes minta, amelyeket érdemes megfontolni:

### Csoportos csevegés

Ez a minta akkor hasznos, ha egy csoportos csevegőalkalmazást akar létrehozni, ahol több ügynök kommunikál egymással. Tipikus felhasználási területek a csapatmunka, ügyfélszolgálat és közösségi hálózatok.

Ebben a mintában minden ügynök egy felhasználót képvisel a csoportos csevegésben, és üzeneteket váltanak a protokoll segítségével. Az ügynökök küldhetnek üzeneteket a csoportnak, fogadhatnak azoktól, és válaszolhatnak más ügynökök üzeneteire.

A minta megvalósítható központosított architektúrával, ahol minden üzenet egy központi szerveren keresztül áramlik, vagy decentralizált architektúrával, ahol az üzenetek közvetlenül cserélődnek.

![Group chat](../../../translated_images/hu/multi-agent-group-chat.ec10f4cde556babd.webp)

### Feladatátadás

Ez a minta akkor hasznos, ha olyan alkalmazást szeretne létrehozni, ahol az ügynökök egymás között átadhatják a feladatokat.

Tipikus felhasználási területek az ügyfélszolgálat, feladatkezelés és munkafolyamat-automatizálás.

Ebben a mintában minden ügynök egy feladatot vagy munkafolyamat lépést képvisel, és az ügynökök előre meghatározott szabályok alapján adhatják át a feladatokat más ügynököknek.

![Hand off](../../../translated_images/hu/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Együttműködő szűrés

Ez a minta akkor hasznos, ha olyan alkalmazást szeretne létrehozni, ahol több ügynök együttműködik, hogy ajánlásokat tegyen a felhasználóknak.

Több ügynök együttműködésének oka, hogy mindegyik ügynök más-más szaktudással rendelkezik, így különféle módon járulhatnak hozzá az ajánlási folyamathoz.

Vegyünk egy példát, ahol egy felhasználó a legjobb részvényt szeretné ajánlásként kapni a tőzsdén.

- **Iparági szakértő**: Egy ügynök iparági szakértő lehet.
- **Technikai elemzés**: Egy másik ügynök technikai elemzésben lehet jártas.
- **Fundamentális elemzés**: Egy harmadik ügynök fundamentális elemzés szakértője lehet. Együttműködésük révén átfogóbb ajánlást nyújtanak a felhasználónak.

![Recommendation](../../../translated_images/hu/multi-agent-filtering.d959cb129dc9f608.webp)

## Forgatókönyv: Visszatérítési folyamat

Tegyük fel, hogy egy vásárló visszatérítést szeretne igényelni egy termékre. Ebben a folyamatban sok ügynök is részt vehet, de osszuk fel őket speciális ügynökökre a visszatérítési folyamathoz és általános ügynökökre, amelyeket más folyamatokban is lehet használni.

**A visszatérítési folyamathoz kapcsolódó ügynökök**:

Íme néhány ügynök, amely részt vehet a visszatérítési folyamatban:

- **Ügyfél ügynök**: Ez az ügynök az ügyfelet képviseli, és a visszatérítés kezdeményezéséért felelős.
- **Eladó ügynök**: Ez az ügynök az eladót képviseli, és a visszatérítési folyamat lebonyolításáért felelős.
- **Fizetési ügynök**: Ez az ügynök a fizetési folyamatot képviseli, és az ügyfél visszatérítésének lebonyolításáért felelős.
- **Megoldási ügynök**: Ez az ügynök a problémamegoldási folyamatot képviseli, és a visszatérítési folyamat során felmerülő problémák megoldásáért felelős.
- **Megfelelőségi ügynök**: Ez az ügynök a megfelelőségi folyamatot képviseli, és a szabályoknak és előírásoknak való megfelelés biztosításáért felelős.

**Általános ügynökök**:

Ezeket az ügynököket az üzlet más részein is használhatja.

- **Szállítási ügynök**: Ez az ügynök a szállítási folyamatért felelős, és a termék visszaküldéséért az eladóhoz. Ezt az ügynököt lehet használni a visszatérítési folyamatban és általános szállítási folyamatokhoz, például vásárlások esetén.
- **Visszajelzési ügynök**: Ez az ügynök a visszajelzések gyűjtéséért felelős az ügyféltől. Visszajelzést bármikor lehet kérni, nem csak a visszatérítési folyamat alatt.
- **Eszkalációs ügynök**: Ez az ügynök az eszkalációs folyamatért felelős, és a problémákat magasabb szintű támogatáshoz továbbítja. Ezt az ügynököt bármilyen folyamatnál lehet használni, ahol probléma eszkaláció szükséges.
- **Értesítési ügynök**: Ez az ügynök felel az értesítések küldéséért az ügyfél számára a visszatérítési folyamat különböző szakaszaiban.
- **Elemzési ügynök**: Ez az ügynök az elemzési folyamatért felel, és a visszatérítési folyamathoz kapcsolódó adatok elemzését végzi.
- **Audit ügynök**: Ez az ügynök az audit folyamatot képviseli, és biztosítja, hogy a visszatérítési folyamat megfelelően történjen.
- **Jelentési ügynök**: Ez az ügynök a jelentési folyamatért felel, és jelentéseket készít a visszatérítési folyamatról.
- **Tudás ügynök**: Ez az ügynök a tudásmenedzsmentért felel, fenntartva a visszatérítési folyamathoz kapcsolódó, valamint az üzlet más részeire vonatkozó információs bázist.
- **Biztonsági ügynök**: Ez az ügynök a visszatérítési folyamat biztonságáért felelős.
- **Minőségügyi ügynök**: Ez az ügynök a visszatérítési folyamat minőségének biztosításáért felelős.

Előzőleg meglehetősen sok ügynök került felsorolásra, mind a speciális visszatérítési folyamathoz, mind az általános, üzleten belüli használatra. Remélhetőleg ez segít eldönteni, hogy milyen ügynököket érdemes bevonni a többügynökös rendszerbe.

## Feladat

Tervezzen meg egy többügynökös rendszert egy ügyfélszolgálati folyamathoz. Azonosítsa a folyamatban részt vevő ügynököket, azok szerepeit és felelősségeit, valamint azok kölcsönhatását egymással. Vegye figyelembe mind az ügyfélszolgálat specifikus ügynökeit, mind az általános ügynököket, amelyeket az üzlet más területein is lehet alkalmazni.


> Gondolkodj el rajta, mielőtt elolvasnád a következő megoldást, lehet, hogy több ügynökre lesz szükséged, mint gondolnád.

> TIPP: Gondolj át az ügyféltámogatási folyamat különböző szakaszait, és vedd figyelembe a rendszerhez szükséges ügynököket is.

## Megoldás

[Megoldás](./solution/solution.md)

## Tudásellenőrzés

### 1. kérdés

Melyik szcenárió a leginkább alkalmas egy többügynökös rendszerhez?

- [ ] A1: Egy támogatási bot egy tudásbázissal és egy kis eszközkészlettel válaszol a gyakori kérdésekre.
- [ ] A2: Egy visszatérítés folyamathoz külön csalás, fizetés és megfelelőség szerepkörök kellenek, mindegyik saját eszközökkel, és az eredményeket össze kell hangolni.
- [ ] A3: Ugyanaz az egyszerű osztályozási kérés ezerszer érkezik be óránként.

### 2. kérdés

Mikor jobb választás általában egyetlen ügynök?

- [ ] A1: A feladat egyetlen utasítás- és eszközkészlettel kezelhető, szakértői átadás nélkül.
- [ ] A2: Az ügynök több eszközhöz is hozzáfér.
- [ ] A3: A munkafolyamat külön szerepköröket igényel eltérő jogosultságokkal és független auditálási naplókkal.

[Megoldás kvíz](./solution/solution-quiz.md)

## Összefoglaló

Ebben a leckében megismertük a többügynökös tervezési mintát, beleértve azokat a helyzeteket, ahol többügynökök alkalmazhatók, a többügynök használatának előnyeit az egyetlen ügynökkel szemben, a többügynökös tervezési minta megvalósításának építőköveit, és azt, hogyan lehet átlátni azt, hogy a több ügynök hogyan lép kölcsönhatásba egymással.

### Van még kérdésed a többügynökös tervezési mintáról?

Csatlakozz a [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) közösséghez, találkozz más tanulókkal, vegyél részt konzultációkon, és kapj választ az AI ügynökeiddel kapcsolatos kérdéseidre.

## További források

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework dokumentáció</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Agentikus tervezési minták</a>


## Előző lecke

[Tervezési terv](../07-planning-design/README.md)

## Következő lecke

[Metakogníció AI ügynököknél](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->