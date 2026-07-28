[![Hogyan tervezzünk jó AI ügynököket](../../../translated_images/hu/lesson-3-thumbnail.1092dd7a8f1074a5.webp)](https://youtu.be/m9lM8qqoOEA?si=4KimounNKvArQQ0K)

> _(Kattints a fenti képre a lecke videójának megtekintéséhez)_
# AI Ügynök Tervezési Elvek

## Bevezetés

Számos módja van az AI ügynöki rendszerek építésének megközelítésére. Tekintettel arra, hogy a generatív AI tervezésben a bizonytalanság jellemző, nem hiba, néha nehéz a mérnökök számára eldönteni, hol kezdjék. Kifejlesztettünk egy emberközpontú UX tervezési elvcsomagot, amely lehetővé teszi a fejlesztők számára, hogy ügyfélközpontú ügynöki rendszereket építsenek üzleti igényeik megoldására. Ezek a tervezési elvek nem előíró architektúrák, hanem inkább kiindulópontok azoknak a csapatoknak, akik definiálják és építik az ügynöki élményeket.

Általánosságban az ügynököknek a következőket kell tennie:

- Bővíteni és skálázni az emberi képességeket (ötletelés, problémamegoldás, automatizálás, stb.)
- Kitölteni a tudáshiányokat (frissíteni az ismereteim a tudományterületeken, fordítás, stb.)
- Támogatni és elősegíteni az együttműködést olyan módokon, ahogyan mi egyénenként szívesen dolgozunk másokkal
- Jobbá tenni minket (pl. életvezetési tanácsadó/feladatmester, segíteni az érzelmi szabályozás és tudatosság fejlesztésében, reziliencia építésében, stb.)

## Mit fog tartalmazni ez a lecke

- Mik azok az ügynöki tervezési elvek
- Mik a követendő irányelvek ezen tervezési elvek megvalósítása közben
- Néhány példa a tervezési elvek használatára

## Tanulási célok

A lecke elvégzése után képes leszel:

1. Elmagyarázni, mik az ügynöki tervezési elvek
2. Elmagyarázni az ügynöki tervezési elvek használatára vonatkozó irányelveket
3. Megérteni, hogyan építhető ügynök az ügynöki tervezési elvek alapján

## Az Ügynöki Tervezési Elvek

![Ügynöki Tervezési Elvek](../../../translated_images/hu/agentic-design-principles.1cfdf8b6d3cc73c2.webp)

### Ügynök (Tér)

Ez az a környezet, amelyben az ügynök működik. Ezek az elvek irányítják, hogyan tervezzünk ügynököket a fizikai és digitális világokkal való kapcsolódáshoz.

- **Kapcsolódás, nem összeomlás** – segítsük az emberek kapcsolatát más emberekkel, eseményekkel és hasznos tudással az együttműködés és kapcsolódás érdekében.
- Az ügynökök segítenek összekapcsolni eseményeket, tudást és embereket.
- Az ügynökök közelebb hozzák az embereket egymáshoz. Nem arra tervezték őket, hogy helyettesítsék vagy lekicsinyeljék az embereket.
- **Könnyen elérhető, de időnként láthatatlan** – az ügynök nagyrészt háttérben működik, és csak akkor serkent bennünket, ha releváns és megfelelő.
  - Az ügynök könnyen felfedezhető és elérhető a jogosult felhasználók számára bármilyen eszközön vagy platformon.
  - Az ügynök multimodális bemeneteket és kimeneteket támogat (hang, beszéd, szöveg, stb.).
  - Az ügynök zökkenőmentesen vált a háttér és előtér között; a proaktív és reaktív működés között is, a felhasználói igények érzékelésének függvényében.
  - Az ügynök láthatatlan formában is működhet, azonban működési folyamata és más ügynökökkel való együttműködése átlátható és a felhasználó számára irányítható.

### Ügynök (Idő)

Ez azt mutatja, hogyan működik az ügynök időben. Ezek az elvek irányítják, hogyan tervezzünk ügynököket, amelyek a múlt, jelen és jövő között lépnek kapcsolatba.

- **Múlt**: Elmélkedés a történelemről, amely magában foglalja az állapotot és a kontextust.
  - Az ügynök relevánsabb eredményeket nyújt az eseményen, embereken vagy állapotokon túlmutató gazdag történelmi adatok elemzése alapján.
  - Az ügynök kapcsolatokat teremt a múltbeli eseményekből és aktívan reflektál az emlékekre, hogy hatékonyan lépjen jelenlegi helyzetekkel kapcsolatba.
- **Most**: Serkentés többet, mint értesítés.
  - Az ügynök átfogó megközelítést testesít meg az emberekkel való interakcióban. Amikor esemény történik, az ügynök túllép a statikus értesítés vagy más formális kereten. Az ügynök egyszerűsítheti a folyamatokat vagy dinamikusan generálhat jelzéseket, hogy a felhasználó figyelmét a megfelelő pillanatban irányítsa.
  - Az ügynök információt nyújt a kontextuális környezet, társadalmi és kulturális változások alapján, és személyre szabott a felhasználói szándékokhoz.
  - Az ügynökkel való interakció fokozatos lehet, fejlődő/növekvő komplexitással, hogy hosszú távon megerősítse a felhasználókat.
- **Jövő**: Alkalmazkodás és fejlődés.
  - Az ügynök alkalmazkodik különféle eszközökhöz, platformokhoz és módokhoz.
  - Az ügynök alkalmazkodik a felhasználói viselkedéshez, akadálymentességi igényekhez és szabadon testreszabható.
  - Az ügynök alakítja és fejlődik a folyamatos felhasználói interakciók során.

### Ügynök (Mag)

Ezek az ügynök tervezésének kulcselemei.

- **Vállaljuk a bizonytalanságot, de építsünk bizalmat**.
  - Egy bizonyos szintű ügynöki bizonytalanság elvárt. A bizonytalanság az ügynök tervezésének alapvető eleme.
  - A bizalom és átláthatóság az ügynök tervezésének alapvető rétegei.
  - Az emberek irányítják, mikor van az ügynök be-/kikapcsolva, és az ügynök státusza mindig egyértelműen látható.

## Az elvek megvalósításának irányelvei

Amikor a fent említett tervezési elveket használod, kövesd az alábbi irányelveket:

1. **Átláthatóság**: Tájékoztasd a felhasználót, hogy AI működik a háttérben, hogyan működik (beleértve a múltbeli tevékenységeket), és hogyan adhat visszajelzést vagy módosíthatja a rendszert.
2. **Irányítás**: Engedd, hogy a felhasználó testreszabhassa, megadhassa preferenciáit és személyre szabhassa a rendszert, valamint rendelkezzen az irányítás a rendszer és jellemzői felett (beleértve a felejtés képességét).
3. **Következetesség**: Törekedj következetes, multimodális élményre eszközök és végpontok között. Használj ismert UI/UX elemeket, ahol lehetséges (pl. mikrofon ikon a hangfelismeréshez), és csökkentsd az ügyfél kognitív terhelését a lehető legjobban (pl. tömör válaszok, vizuális segédletek, „Tudj meg többet” tartalom).

## Hogyan tervezzünk utazási ügynököt ezen elvek és irányelvek alapján

Képzeld el, hogy egy utazási ügynököt tervezel, így gondolkodhatsz az elvek és irányelvek használatáról:

1. **Átláthatóság** – Tájékoztasd a felhasználót, hogy az utazási ügynök AI alapú. Adj alapvető útmutatást a kezdéshez (pl. „Helló” üzenet, mintapéldák). Egyértelműen dokumentáld ezt a termékoldalon. Mutasd meg a felhasználó által korábban feltett kérések listáját. Tegyük világossá a visszajelzésadás módját (fel és le hüvelykujj, Visszajelzés küldése gomb, stb.). Egyértelműen közöld, ha az ügynök használati vagy témakorlátozásokkal rendelkezik.
2. **Irányítás** – Gondoskodj arról, hogy a felhasználó könnyen módosíthassa az ügynököt a létrehozás után olyan eszközökkel, mint a Rendszer Parancs. Engedd, hogy a felhasználó válassza meg, mennyire részletes legyen az ügynök, az írásstílusa, és bármilyen korlátozás, hogy miről ne beszéljen az ügynök. Engedd meg, hogy a felhasználó megtekinthesse és törölhesse a kapcsolódó fájlokat, adatokat, kéréseket és korábbi beszélgetéseket.
3. **Következetesség** – Gondoskodj arról, hogy a Megosztás kérelem, fájl vagy fénykép hozzáadása és címkézés ikonok szabványosak és felismerhetők legyenek. Használd a gemkapocs ikont a fájl feltöltés/megosztás jelzésére az ügynökkel, és a kép ikont a grafikus anyag feltöltésére.

## Példa kódok

- Python: [Agent Framework](./code_samples/03-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/03-dotnet-agent-framework.md)


## További kérdésed van az AI Ügynöki Tervezési Mintákról?

Csatlakozz a [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) közösséghez, hogy találkozz más tanulókkal, részt vegyél fogadóórákon és válaszokat kapj AI ügynökeiddel kapcsolatos kérdéseidre.

## További források

- <a href="https://openai.com" target="_blank">Gyakorlatok az Ügynöki AI Rendszerek Irányítására | OpenAI</a>
- <a href="https://microsoft.com" target="_blank">A HAX Toolkit Projekt - Microsoft Research</a>
- <a href="https://responsibleaitoolbox.ai" target="_blank">Felelős AI Eszköztár</a>

## Előző lecke

[Ügynöki Keretrendszerek Felfedezése](../02-explore-agentic-frameworks/README.md)

## Következő lecke

[Eszközhasználati Tervezési Minta](../04-tool-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->