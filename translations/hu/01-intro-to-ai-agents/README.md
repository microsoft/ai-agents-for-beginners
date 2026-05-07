[![Bevezetés az AI ágensekhez](../../../translated_images/hu/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Kattints a fenti képre, hogy megnézd a videót ehhez a leckéhez)_

# Bevezetés az AI ágensekhez és az ágenses felhasználási esetekhez

Üdvözlünk az **AI ágensek kezdőknek** tanfolyamon! Ez a tanfolyam alapképzést ad — és valódi működő kódot — hogy nulláról kezdhess AI ágenseket építeni.

Gyere és köszönj be az <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord közösségbe</a> — tele van tanulókkal és AI fejlesztőkkel, akik szívesen válaszolnak a kérdésekre.

Mielőtt belevágnánk az építésbe, győződjünk meg róla, hogy valóban értjük, mi az az AI ügynök, és mikor érdemes használni.

---

## Bevezető

Ebben a leckében a következő témákat érintjük:

- Mik azok az AI ágensek, és milyen különböző típusok léteznek
- Milyen feladatokra a legalkalmasabbak az AI ágensek
- Az alapvető építőelemek, amelyeket egy ágenses megoldás tervezésekor használsz

## Tanulási célok

A lecke végére képes leszel:

- Elmagyarázni, mi az AI ügynök, és miben különbözik egy hagyományos AI megoldástól
- Tudni, mikor érdemes AI ügynököt használni (és mikor nem)
- Vázlatosan megtervezni egy alapvető ágenses megoldást egy valós problémára

---

## Az AI ágensek meghatározása és típusai

### Mik azok az AI ágensek?

Íme egy egyszerű megközelítés:

> **Az AI ágensek olyan rendszerek, amelyek lehetővé teszik a Nagy Nyelvi Modellek (LLM-ek) számára, hogy ténylegesen *cselekedjenek* — eszközöket és tudást kapnak, hogy a világra hatással legyenek, nem csak válaszoljanak utasításokra.**

Fejtsük ezt ki egy kicsit:

- **Rendszer** — Az AI ügynök nem csupán egyetlen dolog. Egy együttműködő részekből álló rendszer. Minden ügynök alapjaiban három részből áll:
  - **Környezet** — Az a tér, ahol az ügynök dolgozik. Egy utazási ügynök esetén ez maga a foglalási platform.
  - **Szenzorok** — Ahogyan az ügynök érzékeli a környezet aktuális állapotát. Utazási ügynökünk például ellenőrizheti a szállodai foglaltságot vagy a repülőjegy árakat.
  - **Aktuátorok** — Ahogyan az ügynök cselekszik. Az utazási ügynök foglalhat szobát, küldhet visszaigazolást vagy törölhet foglalást.

![Mik azok az AI ágensek?](../../../translated_images/hu/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Nagy Nyelvi Modellek** — Ágensek már LLM-ek előtt is léteztek, de az LLM-ek tették a modern ágenseket igazán erőssé. Képesek megérteni a természetes nyelvet, kontextusról gondolkodni, és egy homályos felhasználói kérést konkrét cselekvési tervvé alakítani.

- **Cselekvés végrehajtása** — Ágensek rendszere nélkül egy LLM csak szöveget generál. Az ágensek rendszerében az LLM ténylegesen végrehajthat lépéseket — kereshet az adatbázisban, hívhat API-t, üzenetet küldhet.

- **Eszközök elérése** — Az, hogy milyen eszközöket használhat az ügynök, attól függ (1) milyen környezetben fut, és (2) milyen eszközöket adott neki a fejlesztő. Egy utazási ügynök kereshet járatokat, de nem módosíthat ügyféladatokat — ez mind attól függ, mit kötöttél össze.

- **Memória + Tudás** — Az ágensek rendelkezhetnek rövid távú memóriával (aktuális beszélgetés) és hosszú távú memóriával (ügyféladatbázis, korábbi interakciók). Az utazási ügynök "emlékezhet" például, hogy az ablak melletti ülést részesíted előnyben.

---

### Az AI ágensek különböző típusai

Nem minden ágense ugyanúgy épül fel. Íme a fő típusok bontása, az utazási ügynök példáján:

| **Ágents típus** | **Mit csinál** | **Utazási ügynök példa** |
|---|---|---|
| **Egyszerű reflexügynökök** | Kemény kódolt szabályokat követ — nincs memória, nincs tervezés. | Ha panaszos e-mailt lát → továbbítja az ügyfélszolgálatnak. Ennyi. |
| **Modellező reflexügynökök** | Belső modellt tart fenn a világról, és frissíti a változások szerint. | Követi a korábbi repülőjegy árakat, és jelzi azokat az útvonalakat, amelyek hirtelen drágák lettek. |
| **Cél alapú ágensek** | Egy cél érdekében fokozatosan lépésenként dolgozik. | Teljes utazást foglal (repülő, autó, szálloda) a jelenlegi helyedről a célállomásodra. |
| **Haszon alapú ágensek** | Nem csak *egy* megoldást keres — a *legjobbat* találja, mérlegelve a kompromisszumokat. | Költség és kényelem egyensúlyát keresve megtalálja a neked legjobb utazást. |
| **Tanuló ágensek** | Idővel egyre jobb lesz, a visszajelzésekből tanulva. | Az utazás utáni felmérés alapján módosítja a jövőbeli foglalási ajánlásokat. |
| **Hierarchikus ágensek** | Egy felső szintű ügynök részmunkákra bontja az ügyet, és al-ügynökökre bízza. | Egy "utazás törlése" kérés felbontódik: repülő, szálloda, autóbérlés törlése — mindegyik külön al-ügynökre hárul. |
| **Többágenses rendszerek (MAS)** | Több független ügynök együttműködik (vagy verseng). | Együttműködés: külön ágensek kezelik a szállodákat, repülőket és szórakozást. Versengés: több ügynök verseng a szállodai szobák legjobb áron való betöltéséért. |

---

## Mikor érdemes AI ágenseket használni?

Az, hogy *lehet*, nem jelenti azt, hogy mindig is *kell* AI ügynököt használni. Ezek a helyzetek valóban jól működnek ágensekkel:

![Mikor érdemes AI ágenseket használni?](../../../translated_images/hu/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Nyitott végű problémák** — Amikor a probléma megoldásának lépései nem programozhatók előre. Az LLM-nek dinamikusan kell megtalálnia az utat.
- **Többlépéses folyamatok** — Olyan feladatok, amelyek több lépésen át eszközök használatát igénylik, nem csak egyszeri lekérdezést vagy generálást.
- **Időbeli fejlődés** — Ha azt akarod, hogy a rendszer egyre okosabb legyen a felhasználói visszajelzések vagy környezeti jelek alapján.

Ezután mélyebben is foglalkozunk majd azzal, mikor érdemes (és mikor *nem*) AI ágenseket használni a tanfolyam során a **Megbízható AI ágensek építése** leckében.

---

## Az ágenses megoldások alapjai

### Ügynök fejlesztés

Az első lépés egy ügynök építésénél annak meghatározása, *mit tud csinálni* — milyen eszközök, cselekvések és viselkedések tartoznak hozzá.

Ebben a tanfolyamban az **Azure AI Agent Service** platformot használjuk. Támogatja:

- Nyílt modelleket, mint az OpenAI, Mistral, és Llama
- Licencelt adatokat olyan szolgáltatóktól, mint a Tripadvisor
- Standardizált OpenAPI 3.0 eszközdefiníciókat

### Ágenses minták

Az LLM-ekkel utasítások (promptok) segítségével kommunikálsz. Ügynököknél nem lehet minden promptot kézzel készíteni — az ügynöknek kell cselekednie többlépésesen. Ebben segítenek az **ágenses minták**. Ezek újrahasznosítható stratégiák az LLM-ek promptolására és irányítására skálázhatóbb és megbízhatóbb módon.

Ez a tanfolyam a leggyakoribb és leghasznosabb ágenses mintákra épül.

### Ágenses keretrendszerek

Az ágenses keretrendszerek kész sablonokat, eszközöket és infrastruktúrát kínálnak a fejlesztőknek az ágensek építéséhez. Megkönnyítik:

- Az eszközök és képességek összekötését
- Az ügynök tevékenységének megfigyelését (és hibakeresést, ha valami nem működik)
- Több ügynök közötti együttműködést

Ebben a tanfolyamban az **Microsoft Agent Framework (MAF)** keretrendszerre fókuszálunk, amely gyártásra kész ágensek létrehozását segíti.

---

## Kódminták

Készen állsz, hogy lásd működés közben? Íme a lecke kódpéldái:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Kérdésed van?

Csatlakozz a [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) közösséghez, hogy kapcsolatba léphess más tanulókkal, részt vehess office hour-okon, és megkapd az AI ügynökökkel kapcsolatos kérdéseidre adott válaszokat közösségi segítséggel.

---

## Előző lecke

[Kurzus beállítása](../00-course-setup/README.md)

## Következő lecke

[Ágenses keretrendszerek felfedezése](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum, az eredeti nyelven tekintendő hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget az e fordítás használatából eredő félreértésekért vagy téves értelmezésekért.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->