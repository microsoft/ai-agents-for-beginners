[![Intro to AI Agents](../../../translated_images/hu/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Kattints a fenti képre a leckéhez készült videó megtekintéséhez)_

# Bevezetés az AI Ügynökökbe és Ügynöki Használati Esetekbe

Üdvözlünk az **AI Ügynökök Kezdőknek** tanfolyamon! Ez a tanfolyam alapvető tudást — és működő kódot — ad ahhoz, hogy az AI ügynököket a semmiből elkezdd építeni.

Gyere, üdvözölj minket az <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord közösségben</a> — tele van tanulókkal és AI fejlesztőkkel, akik örömmel válaszolnak a kérdésekre.

Mielőtt belevágnánk az építésbe, győződjünk meg arról, hogy valóban értjük, mi az az AI Ügynök és mikor érdemes használni.

---

## Bevezető

Ez a lecke lefedi:

- Mik az AI Ügynökök, és milyen különböző típusok léteznek
- Milyen feladatokra alkalmasak leginkább az AI Ügynökök
- Az alap építőelemek, amelyeket használni fogsz egy ügynöki megoldás tervezésekor

## Tanulási célok

A lecke végére képesnek kell lenned:

- Elmagyarázni, mi az az AI Ügynök, és miben különbözik egy hagyományos AI megoldástól
- Tudni, mikor érdemes AI Ügynököt használni (és mikor nem)
- Vázolni egy alapvető ügynöki megoldástervezetet egy valós problémára

---

## AI Ügynökök meghatározása és AI Ügynök típusok

### Mik az AI Ügynökök?

Egy egyszerű mód arra, hogyan gondolkodjunk róla:

> **Az AI Ügynökök olyan rendszerek, amelyek lehetővé teszik, hogy a Nagy Nyelvi Modellek (LLM-ek) ténylegesen *cselekedjenek* — azáltal, hogy eszközöket és tudást kapnak a világon való tevékenységhez, nemcsak a kérdések megválaszolására.**

Fejtsük ki egy kicsit:

- **Rendszer** — Az AI Ügynök nem csupán egyetlen dolog. Egy részekből álló együttműködő rendszer. Minden ügynök alapvetően három részből áll:
  - **Környezet** — Az a tér, amelyben az ügynök működik. Egy utazási foglaló ügynök esetében ez maga a foglalási platform.
  - **Szenzorok** — Ahogyan az ügynök leolvassa a környezete aktuális állapotát. Az utazási ügynök például ellenőrizheti a szállodai elérhetőséget vagy a repülőjegy árakat.
  - **Aktuátorok** — Ahogyan az ügynök cselekszik. Az utazási ügynök foglalhat szobát, küldhet visszaigazolást vagy törölhet foglalást.

![What Are AI Agents?](../../../translated_images/hu/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Nagy Nyelvi Modellek** — Az ügynökök LLM-ek előtt is léteztek, de az LLM-ek teszik a modern ügynököket igazán erőssé. Értik a természetes nyelvet, tudnak kontextusban gondolkodni, és egy homályos kérésből konkrét cselekvési tervet készítenek.

- **Cselekvések Végrehajtása** — Ügynökrendszer nélkül egy LLM csak szöveget generál. Az ügynökrendszerben az LLM ténylegesen *végrehajtja* a lépéseket — adatbázist keres, API-t hív, üzenetet küld.

- **Eszközhozzáférés** — Az, hogy az ügynök milyen eszközökhöz fér hozzá, attól függ, (1) milyen környezetben fut és (2) mit adott neki a fejlesztő. Egy utazási ügynök keresheti a járatokat, de nem szerkesztheti az ügyfél adatokat — mindez attól függ, hogyan kötöd össze.

- **Memória + Tudás** — Az ügynökök rendelkezhetnek rövid távú memóriával (az aktuális beszélgetés), és hosszú távú memóriával (ügyfél adatbázis, korábbi interakciók). Az utazási ügynök „emlékezhet” arra, hogy ablak melletti ülőhelyet kedvelsz.

---

### Az AI Ügynökök különböző típusai

Nem minden ügynök épül ugyanúgy. Íme egy felosztás a fő típusokról, az utazási ügynök példáján keresztül:

| **Ügynök típus** | **Mit csinál** | **Utazási ügynök példa** |
|---|---|---|
| **Egyszerű reflex ügynökök** | Keménykódolt szabályokat követnek — nincs memória, nincs tervezés. | Lát egy panasz e-mailt → továbbítja az ügyfélszolgálatnak. Ennyi. |
| **Modell-alapú reflex ügynökök** | Belső világmodellt tartanak, és frissítik, ahogy változások történnek. | Követi a történelmi járatárakat, és figyelmeztet, ha hirtelen drágák a járatok. |
| **Cél-alapú ügynökök** | Van egy célja, és lépésről lépésre keresi az elérését. | Teljes utazást foglal (járatok, autó, szálloda), kiindulva a jelenlegi helyzetedből a célállomásig. |
| **Haszon-alapú ügynökök** | Nem csak egy megoldást talál, hanem a *legjobbat*, mérlegelve a kompromisszumokat. | Költségek és kényelem egyensúlyát mérve megtalálja a legjobb utazást a preferenciáid szerint. |
| **Tanuló ügynökök** | Idővel fejlődik, a visszajelzésekből tanulva. | A jövőbeli foglalási javaslatokat a trip után érkező visszajelzések alapján igazítja. |
| **Hierarchikus ügynökök** | Egy magas szintű ügynök munkát bont alfeladatokra, és delegál alacsonyabb szintű ügynököknek. | Egy „útlemondás” kérés három részre oszlik: járat törlése, szállodai foglalás törlése, autókölcsönzés törlése — mindegyiket egy-egy al-ügynök intézi. |
| **Több-ügynök rendszerek (MAS)** | Több független ügynök dolgozik együtt (vagy versenyez). | Együttműködés: külön ügynökök kezelik a szállodákat, járatokat és szórakozást. Versengés: több ügynök versenyez a legjobb áron történő szállodai szobák megtöltéséért. |

---

## Mikor érdemes AI Ügynököt használni

Az, hogy *lehet* AI Ügynököt használni, nem jelenti azt, hogy mindig *kell* is. Íme, azok a helyzetek, amikor az ügynökök igazán jól teljesítenek:

![When to use AI Agents?](../../../translated_images/hu/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Nyitott végű problémák** — amikor a probléma megoldásának lépései nem programozhatók előre. Szükség van arra, hogy az LLM dinamikusan találja meg az utat.
- **Többlépcsős folyamatok** — olyan feladatok, amelyek eszközhasználatot igényelnek több körben, nem csak egyetlen lekérdezés vagy generálás során.
- **Időbeli fejlődés** — amikor azt akarod, hogy a rendszer a felhasználói visszajelzések vagy környezeti jelek alapján egyre okosabb legyen.

A tanfolyam későbbi részében a **Megbízható AI Ügynökök építése** leckében mélyebben foglalkozunk azzal, mikor érdemes (és mikor nem) AI Ügynököt használni.

---

## Ügynöki megoldások alapjai

### Ügynök fejlesztés

Az első, amit egy ügynök építésekor teszel, az az, hogy definiálod, *mit tud csinálni* — az eszközeit, cselekvéseit és viselkedését.

Ebben a tanfolyamban az **Azure AI Agent Service** a fő platformunk. Támogatja:

- Modelljei olyan szolgáltatóktól, mint az OpenAI, Mistral és Meta (Llama)
- Licencelt adatok olyan szolgáltatóktól, mint a Tripadvisor
- Standardizált OpenAPI 3.0 eszközdefiníciók

### Ügynöki minták

Az LLM-ekkel promptokon keresztül kommunikálsz. Ügynököknél nem mindig lehet minden promptot kézzel megalkotni — az ügynöknek több lépésből kell végrehajtania tevékenységeket. Itt jönnek képbe az **ügynöki minták**. Ezek újrahasznosítható stratégiák az LLM-ek promptolására és irányítására egy skálázhatóbb, megbízhatóbb módon.

Ez a tanfolyam a leggyakoribb és leghasznosabb ügynöki mintákra épül.

### Ügynöki keretrendszerek

Az ügynöki keretrendszerek kész sablonokat, eszközöket és infrastruktúrát adnak a fejlesztők kezébe az ügynökök építéséhez. Egyszerűbbé teszik:

- Az eszközök és képességek bekötését
- Annak megfigyelését, mit csinál az ügynök (és hibakeresést, ha valami nem működik)
- Együttműködést több ügynök között

Ebben a tanfolyamban a **Microsoft Agent Framework (MAF)**-re fókuszálunk, hogy éles, gyártásba szánt ügynököket építsünk.

---

## Kódpéldák

Készen állsz, hogy működés közben lásd? Íme a lecke kódpéldái:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Kérdéseid vannak?

Csatlakozz a [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) közösséghez, hogy kapcsolatba lépj más tanulókkal, részt vegyél konzultációkon, és hogy a közösségtől választ kapj AI Ügynökös kérdéseidre.

---

## Előző lecke

[Tanfolyam beállítása](../00-course-setup/README.md)

## Következő lecke

[Az ügynöki keretrendszerek felfedezése](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->