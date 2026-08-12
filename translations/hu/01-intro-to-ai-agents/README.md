[![Bevezetés az AI ügynökökbe](../../../translated_images/hu/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(A fenti képre kattintva nézheted meg a leckéhez tartozó videót)_

# Bevezetés az AI ügynökökbe és az ügynökök használati eseteibe

Üdvözlünk az **AI ügynökök kezdőknek** tanfolyamon! Ez a tanfolyam alapvető ismereteket és működő példakódot ad számodra, hogy nulláról kezdve építs AI ügynököket.

Gyere és köszönj be a <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord közösségbe</a> – tele van tanulókkal és AI fejlesztőkkel, akik örömmel válaszolnak a kérdésekre.

Mielőtt belevágnánk az építésbe, győződjünk meg róla, hogy valóban értjük, mi az AI ügynök és mikor érdemes használni.

---

## Bevezetés

Ebben a leckében a következőkről lesz szó:

- Mi az AI ügynök, és milyen típusai léteznek
- Milyen feladatokra a legalkalmasabbak az AI ügynökök
- Az alapvető építőelemek, amelyeket ügynöki megoldás tervezésekor használsz

## Tanulási célok

A lecke végére képes leszel:

- Megmagyarázni, mi az AI ügynök, és miben különbözik a hagyományos AI megoldástól
- Tudni, mikor érdemes AI ügynököt használni (és mikor nem)
- Felvázolni egy alap ügynöki megoldástervezést egy valós problémára

---

## AI ügynökök definíciója és típusai

### Mik azok az AI ügynökök?

Íme egy egyszerű mód, hogy gondolkodj róluk:

> **Az AI ügynökök olyan rendszerek, amelyek lehetővé teszik a Nagy Nyelvi Modellek (LLM-ek) számára, hogy ténylegesen *cselekedjenek* — azáltal, hogy eszközökkel és tudással látják el őket a világban való tevékenységhez, nem csak válaszolni a kérdésekre.**

Fejtsük ki egy kicsit:

- **Rendszer** — Egy AI ügynök nem csak egyetlen dolog. Ez egy több részből álló rendszer, amely együtt dolgozik. Minden ügynök alapja három rész:
  - **Környezet** — Az a tér, ahol az ügynök működik. Egy utazási foglalási ügynök esetén ez maga a foglalási platform.
  - **Érzékelők** — Ahogyan az ügynök olvassa környezete aktuális állapotát. Utazási ügynökünk például ellenőrizheti a szállodák elérhetőségét vagy a repülőjegy árakat.
  - **Hatórendszerek** — Hogyan hajt végre műveleteket az ügynök. Az utazási ügynök például foglalhat szobát, küldhet visszaigazolást, vagy törölhet foglalást.

![Mik azok az AI ügynökök?](../../../translated_images/hu/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Nagy Nyelvi Modellek** — Ügynökök már LLM-ek előtt is léteztek, de az LLM-ek teszik a modern ügynököket ilyen hatékonnyá. Megértik a természetes nyelvet, képesek kontextusról érvelni, és a homályos felhasználói kérést konkrét cselekvési tervvé alakítják.

- **Cselekvés végrehajtása** — Ügynökrendszer nélkül egy LLM csak szöveget generál. Ügynökrendszeren belül az LLM ténylegesen végrehajthat lépéseket — adatbázis keresése, API hívása, üzenetküldés.

- **Eszközhozzáférés** — Az, hogy milyen eszközöket használhat az ügynök, attól függ (1) a környezettől, ahol fut, és (2) attól, hogy a fejlesztő milyen eszközöket adott számára. Egy utazási ügynök például kereshet járatokat, de nem szerkesztheti az ügyféladatokat — az egész attól függ, mit kötöttél össze.

- **Memória + Tudás** — Az ügynökök lehetnek rövid távú memóriával (az aktuális beszélgetés) és hosszú távú memóriával (ügyféladatbázis, múltbeli interakciók). Az utazási ügynök például „megjegyezheti”, hogy szereted az ablak melletti helyeket.

---

### Az AI ügynökök különböző típusai

Nem minden ügynök épül ugyanúgy. Itt van a fő típusok bontása, egy utazási foglalási ügynök példáján keresztül:

| **Ügynök típusa** | **Mire képes** | **Utazási ügynök példa** |
|---|---|---|
| **Egyszerű reflex ügynökök** | Szigorúan előre kódolt szabályokat követ — nincs memória, nincs tervezés. | Ha panasz e-mailt lát → továbbítja az ügyfélszolgálathoz. Ennyi. |
| **Modell-alapú reflex ügynökök** | Belső modellt tart fenn a világról, és frissíti azt változások esetén. | Figyeli a történelmi repülőjegy árakat, és jelzi a hirtelen dráguló útvonalakat. |
| **Cél-alapú ügynökök** | Van egy céljuk, és lépésről lépésre kitalálják, hogyan érjék el. | Egész utazást foglal (repülő, autó, szálloda) a jelenlegi helyzetből a célállomásra. |
| **Hasznosság-alapú ügynökök** | Nem csak *egy* megoldást keresnek — a *legjobb* megoldást találják meg, a kompromisszumokat mérlegelve. | Költség és kényelem között egyensúlyozva találja meg a legjobban preferenciáidnak megfelelő utazást. |
| **Tanuló ügynökök** | Idővel fejlődik visszajelzések alapján. | A jövőbeni foglalási ajánlásokat a túra utáni felmérések alapján szabja. |
| **Hierarchikus ügynökök** | Egy magas szintű ügynök bontja kisebb feladatokra a munkát, és delegál alacsonyabb szintű ügynököknek. | Egy "út lefújása" kérés felosztódik: repülő törlés, szálloda törlés, autóbérlés törlés — mindegyiket alügynök kezeli. |
| **Több ügynökös rendszer (MAS)** | Több önálló ügynök együttműködik (vagy verseng). | Együttműködés: külön ügynök foglalkozik szállásokkal, repülőjegyekkel, szórakozással. Versengés: több ügynök verseng a szállodai szobák legjobb árú kitöltéséért. |

---

## Mikor érdemes AI ügynököket használni?

Csak azért, mert *lehet* AI ügynököt használni, nem jelenti azt, hogy mindig *kell*. Itt vannak azok a helyzetek, amikor az ügynökök igazán hasznosak:

![Mikor használjuk az AI ügynököket?](../../../translated_images/hu/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Nyitott végű problémák** — Amikor a probléma megoldásának lépéseit nem lehet előre programozni. Az LLM-nek dinamikusan kell kitalálnia az útvonalat.
- **Többlépéses folyamatok** — Olyan feladatok, amelyek több lépésen át kell eszközöket használni, nem csak egy lekérdezés vagy generálás.
- **Idővel javulás** — Ha azt szeretnéd, hogy a rendszer okosabb legyen a felhasználói visszajelzések vagy környezeti jelek alapján.

Később a tanfolyamban az **Megbízható AI ügynökök építése** leckében mélyebben is foglalkozunk azzal, mikor érdemes (és mikor *nem* érdemes) AI ügynököket használni.

---

## Az ügynöki megoldások alapjai

### Ügynök fejlesztés

Az első dolog ügynök építésekor, hogy definiáld, *mit tud csinálni* — az eszközeit, műveleteit és viselkedését.

Ebben a tanfolyamban a **Microsoft Foundry Agent Service**-t használjuk fő platformként. Ez támogatja:

- Olyan modelleket, mint az OpenAI, Mistral és Meta (Llama)
- Licencelt adatokat, például a Tripadvisor-tól
- Szabványosított OpenAPI 3.0 eszközdefiníciókat

### Ügynöki minták

Az LLM-ekkel promptokon keresztül kommunikálsz. Ügynököknél nem lehet minden promptot kézzel készíteni — az ügynöknek több lépésen át kell cselekednie. Itt jönnek képbe az **ügynöki minták**. Ezek újrahasznosítható stratégiák az LLM-ek promptolására és irányítására skálázhatóbb, megbízhatóbb módon.

Ez a tanfolyam a leggyakoribb és leghasznosabb ügynöki minták köré épül.

### Ügynöki keretrendszerek

Az ügynöki keretrendszerek kész sablonokat, eszközöket és infrastruktúrát adnak a fejlesztőknek az ügynökök építéséhez. Ezek megkönnyítik:

- Eszközök és képességek összekapcsolását
- Figyelni, mit csinál az ügynök (és hibakeresni, ha valami rosszul működik)
- Több ügynök közötti együttműködést

Ebben a kurzusban a **Microsoft Agent Framework (MAF)**-re összpontosítunk, amely ipari szintű, éles használatra kész ügynökök építéséhez alkalmas.

---

## Kódminták

Készen állsz, hogy működés közben is lásd? Íme a lecke kódmintái:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Kérdésed van?

Csatlakozz a [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) közösséghez, hogy más tanulókkal találkozz, vegyél részt irodai időben, és az AI ügynökökkel kapcsolatos kérdéseidre választ kapj a közösségtől.


---

## Gyors tesztelés ennek az ügynöknek (opcionális)

Amint megtanulod ügynökök telepítését a [16. leckében](../16-deploying-scalable-agents/README.md), adhatsz gyors post-deploy egészségellenőrzést ennek a lecke `TravelAgent` ügynökének az előre elkészített katalógussal: [`tests/lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json). Lásd a [`tests/README.md`](../tests/README.md) fájlt a futtatási utasításokért.

---

## Előző lecke

[Kurzus beállítása](../00-course-setup/README.md)

## Következő lecke

[Ügynöki keretrendszerek felfedezése](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->