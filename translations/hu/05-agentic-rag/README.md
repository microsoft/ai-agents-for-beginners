[![Agentic RAG](../../../translated_images/hu/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(A fenti képre kattintva tekintheti meg a lecke videóját)_

# Agentic RAG

Ez a lecke átfogó áttekintést nyújt az Agentic Retrieval-Augmented Generation (Agentic RAG) nevű új AI paradigmáról, amelyben a nagy nyelvi modellek (LLM-ek) önállóan tervezik meg a következő lépéseiket, miközben külső forrásokból húznak be információkat. A statikus lekérdezés-és-olvasás mintáktól eltérően az Agentic RAG iteratív hívásokat foglal magában az LLM-hez, amelyeket eszköz- vagy függvényhívások és strukturált kimenetek szakítanak meg. A rendszer kiértékeli az eredményeket, finomítja a lekérdezéseket, szükség esetén további eszközöket hív meg, és ezt a ciklust addig folytatja, amíg kielégítő megoldást nem ér el.

## Bevezetés

Ez a lecke a következőket tárgyalja:

- **Az Agentic RAG megértése:** Ismerje meg az AI-ben kibontakozó paradigmát, ahol a nagy nyelvi modellek (LLM-ek) önállóan tervezik meg a következő lépéseiket, miközben külső adatforrásokból szereznek információt.
- **Az iteratív készítő-ellenőr stílus elsajátítása:** Értse meg az iteratív hívásokból álló ciklust az LLM-hez, amelyet eszköz- vagy függvényhívások és strukturált kimenetek szakítanak meg, célja a helyesség javítása és a hibás lekérdezések kezelése.
- **Gyakorlati alkalmazások feltérképezése:** Azonosítsa azokat a helyzeteket, ahol az Agentic RAG különösen jól működik, például helyesség-központú környezetekben, komplex adatbázis-interakciókban és kiterjesztett munkafolyamatokban.

## Tanulási célok

A lecke elvégzése után képes lesz/meg fogja érteni:

- **Az Agentic RAG megértése:** Tudja meg az AI fejlődő paradigmáját, ahol a nagy nyelvi modellek önállóan tervezik következő lépéseiket, miközben külső adatforrásokból szereznek információt.
- **Az iteratív készítő-ellenőr stílus:** Értse meg az iteratív hívásokból álló ciklus fogalmát az LLM-hez, amely eszköz- vagy függvényhívásokkal és strukturált kimenetekkel szakítva javítja a helyességet és kezeli a hibás lekérdezéseket.
- **A következtetési folyamat saját kezelése:** Értse meg, hogyan birtokolja a rendszer a következtetési folyamatát, hoz döntéseket, hogy hogyan közelítsen meg problémákat előre definiált utak nélkül.
- **Munkafolyamat:** Értse meg, hogyan dönt önállóan az agent modell, például a piaci trendjelentések lekéréséről, versenytársi adatok azonosításáról, belső értékesítési mutatók összekapcsolásáról, eredmények szintetizálásáról és stratégiák értékeléséről.
- **Iteratív ciklusok, eszközintegráció és memória:** Tudjon meg többet az iteratív interakciós mintáról, amely fenntartja az állapotot és a memóriát a lépések között, hogy elkerülje az ismétlődő ciklusokat és megalapozott döntéseket hozzon.
- **Hibakezelés és önkorrekció:** Ismerje meg a rendszer robusztus önkorrekciós mechanizmusait, ideértve az iterálást, újra-lekérdezést, diagnosztikai eszközök használatát, és az emberi felügyelet igénybevételét.
- **Az ügynökség határai:** Értse meg az Agentic RAG korlátait, különös tekintettel a domain-specifikus autonómiára, az infrastruktúra-függőségre és a biztonsági keretek betartására.
- **Gyakorlati alkalmazási esetek és érték:** Azonosítsa azokat a helyzeteket, ahol az Agentic RAG kiemelkedik, például helyesség-központú környezetekben, komplex adatbázis-interakciókban és kiterjesztett munkafolyamatokban.
- **Irányítás, átláthatóság és bizalom:** Ismerje meg az irányítás és átláthatóság fontosságát, beleértve az értelmezhető következtetést, az elfogultság szabályozását és az emberi felügyeletet.

## Mi az az Agentic RAG?

Az Agentic Retrieval-Augmented Generation (Agentic RAG) egy fejlődő AI paradigma, amelyben a nagy nyelvi modellek (LLM-ek) önállóan tervezik meg következő lépéseiket, miközben külső forrásokból szereznek be információkat. A statikus keresés- és olvasás mintáktól eltérően az Agentic RAG iteratív hívásokat végez az LLM-hez, amelyeket eszköz- vagy függvényhívások és strukturált kimenetek szakítanak meg. A rendszer kiértékeli az eredményeket, finomítja a lekérdezéseket, szükség esetén újabb eszközöket hív be, és ezt a ciklust addig folytatja, amíg kielégítő megoldást nem ér el. Ez az iteratív „készítő-ellenőr” stílus javítja a helyességet, kezeli a hibás lekérdezéseket és magas színvonalú eredményeket biztosít.

A rendszer aktívan birtokolja következtetési folyamatát, átfogalmazza a sikertelen lekérdezéseket, különféle keresési módszereket választ, és több eszközt integrál — például vektorkeresést az Azure AI Search-ben, SQL adatbázisokat vagy egyedi API-kat — mielőtt végleges válaszát megadná. Egy agentic rendszer megkülönböztető tulajdonsága, hogy képes birtokolni következtetési folyamatát. A hagyományos RAG megoldások előre meghatározott utakra támaszkodnak, míg egy agentic rendszer önállóan határozza meg a lépések sorrendjét az általa talált információk minősége alapján.

## Agentic Retrieval-Augmented Generation (Agentic RAG) meghatározása

Az Agentic Retrieval-Augmented Generation (Agentic RAG) egy új AI fejlesztési paradigma, ahol az LLM-ek nemcsak külső adatforrásokból szereznek be információkat, hanem önállóan megtervezik a következő lépéseiket is. A statikus keresés- és olvasás mintáktól vagy gondosan megírt prompt sorozatoktól eltérően az Agentic RAG egy iteratív hívásciklust jelent az LLM-hez, amelyet eszköz- vagy függvényhívások és strukturált kimenetek szakítanak meg. Minden lépésnél a rendszer kiértékeli az általa kapott eredményeket, eldönti, hogy finomítani kell-e a lekérdezéseket, szükség esetén további eszközöket hív be, és folytatja ezt a ciklust, amíg kielégítő megoldást nem ér el.

Ez az iteratív „készítő-ellenőr” működésmód célja a helyesség javítása, hibás lekérdezések kezelése strukturált adatbázisokban (pl. NL2SQL) és kiegyensúlyozott, magas színvonalú eredmények biztosítása. A rendszer nem csupán gondosan megtervezett prompt láncokra támaszkodik, hanem aktívan birtokolja következtetési folyamatát. Átfogalmazhatja a sikertelen lekérdezéseket, választhat különböző keresési módszereket, és több eszközt is integrálhat — mint például vektorkeresés az Azure AI Search-ben, SQL adatbázisok vagy egyéni API-k — mielőtt végleges válaszát megadná. Ez eltávolítja a túlzottan bonyolult koordinációs rendszerek szükségességét. Ehelyett egy viszonylag egyszerű „LLM hívás → eszköz használat → LLM hívás → …” ciklus is kifinomult és megalapozott kimeneteket eredményezhet.

![Agentic RAG Core Loop](../../../translated_images/hu/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## A következtetési folyamat birtoklása

Az a megkülönböztető tulajdonság, amely „agentic”-ké teszi a rendszert, az a képessége, hogy birtokolja saját következtetési folyamatát. A hagyományos RAG megoldások gyakran emberek által előre meghatározott utakra támaszkodnak: egy gondolatmenet-láncra, amely előírja, hogy mit és mikor kérdezzen le.
Ám amikor egy rendszer valóban agentic, belsőleg dönt arról, hogy hogyan közelíti meg a problémát. Nem csak egy szkriptet hajt végre; önállóan határozza meg a lépések sorrendjét az általa talált információk minősége alapján.
Például, ha arra kérik, hogy hozzon létre egy termékbevezetési stratégiát, nem csupán egy olyan prompt alapján dolgozik, amely az egész kutatási és döntéshozatali munkafolyamatot kifejti. Ehelyett az agentic modell önállóan dönt arról, hogy:

1. Lekéri a jelenlegi piaci trendjelentéseket a Bing Web Grounding használatával
2. Azonosítja a releváns versenytársi adatokat az Azure AI Search segítségével.
3. Összekapcsolja a történeti belső értékesítési mutatókat az Azure SQL Adatbázis használatával.
4. Szisztezálja az eredményeket egy összefüggő stratégiává, amelyet az Azure OpenAI Service koordinál.
5. Értékeli a stratégiát hiányosságokra vagy inkonzisztenciákra, és ha szükséges, újabb lekérdezési kört indít.
Mindezeket a lépéseket - a lekérdezések finomítását, források választását, a válaszokkal való „elégedett” állapotig történő iterálást - a modell dönti el, nem egy ember előre megírt szkriptje.

## Iteratív ciklusok, eszközintegráció és memória

![Tool Integration Architecture](../../../translated_images/hu/tool-integration.0f569710b5c17c10.webp)

Egy agentic rendszer egy ciklikus interakciós mintára épít:

- **Kezdeti hívás:** A felhasználó célja (azaz a felhasználói prompt) bemutatásra kerül az LLM számára.
- **Eszköz hívása:** Ha a modell hiányzó információkat vagy bizonytalan utasításokat észlel, eszközt vagy lekérdezési módszert választ – például vektoralapú adatbázis-lekérdezést (pl. Azure AI Search Hybrid keresés privát adatokon) vagy strukturált SQL hívást – hogy több kontextust szerezzen.
- **Értékelés és finomítás:** A visszakapott adatok áttekintése után a modell eldönti, elégséges-e az információ. Ha nem, finomítja a lekérdezést, más eszközt próbál ki vagy módosítja az megközelítést.
- **Ismétlés amíg elégedett:** Ez a ciklus addig folytatódik, amíg a modell el nem döntötte, hogy elegendő világosság és bizonyíték áll rendelkezésére egy végső, jól megalapozott válasz megadásához.
- **Memória és állapot:** Mivel a rendszer fenntartja az állapotot és memóriát a lépések között, képes felidézni korábbi próbálkozásokat és azok eredményeit, elkerülve az ismétlődő ciklusokat, és megalapozottabb döntéseket hozva előrehaladás közben.

Idővel ez az evolúciós megértés érzését kelti, lehetővé téve a modell számára, hogy bonyolult, több lépéses feladatokat navigáljon emberi beavatkozás vagy prompt újraformálása nélkül.

## Hibák kezelése és önkorrekció

Az Agentic RAG autonómiája magában foglalja a robosztus önkorrekciós mechanizmusokat is. Amikor a rendszer zsákutcába jut – például irreleváns dokumentumokat talál vagy hibás lekérdezésekkel találkozik – a következőket teheti:

- **Iterálás és újra-lekérdezés:** Ahelyett, hogy alacsony értékű válaszokat adna, a modell új keresési stratégiákat próbál ki, újraírásokat végez az adatbázis lekérdezésein, vagy alternatív adatállományokat keres.
- **Diagnosztikai eszközök használata:** A rendszer további funkciókat hívhat meg, amelyek segítenek a következtetési lépések hibakeresésében vagy a lekért adatok helyességének megerősítésében. Az olyan eszközök, mint az Azure AI Tracing, nagyon fontosak a robosztus megfigyelhetőség és monitorozás biztosításához.
- **Emberi felügyelet igénybevétele:** Magas kockázatú vagy ismétlődően sikertelen helyzetekben a modell jelezheti a bizonytalanságot, és emberi iránymutatást kérhet. Amint az ember helyesbítő visszajelzést ad, a modell ezt a tanulságot felhasználhatja a jövőbeni működésében.

Ez az iteratív és dinamikus megközelítés lehetővé teszi a modell számára a folyamatos fejlődést, biztosítva, hogy ne legyen csupán egyszeri rendszer, hanem tanuljon hibáiból az adott munkamenet során.

![Önkorrekciós mechanizmus](../../../translated_images/hu/self-correction.da87f3783b7f174b.webp)

## Az ügynökség határai

Bár autonóm egy adott feladaton belül, az Agentic RAG nem azonos a mesterséges általános intelligenciával (AGI). Az „agentic” képességei korlátozottak az emberi fejlesztők által biztosított eszközökre, adatforrásokra és irányelvekre. Nem tud saját eszközöket feltalálni, vagy kilépni a megszabott domain-határok közül. Inkább az adott erőforrások dinamikus összehangolásában jeleskedik.
A fejlettebb AI formákhoz képest a fő különbségek:

1. **Domain-specifikus autonómia:** Az Agentic RAG rendszerek egy ismert domainen belül, felhasználó által meghatározott célok elérésére fókuszálnak, stratégiákat alkalmazva, mint például lekérdezés átírása vagy eszközválasztás az eredmények javítására.
2. **Infrastruktúra-függőség:** A rendszer képességei azon eszközöktől és adatoktól függenek, amelyeket a fejlesztők integráltak. Emberi beavatkozás nélkül nem lépheti túl ezeket a határokat.
3. **A biztonsági korlátok tisztelete:** Az etikai irányelvek, megfelelőségi szabályok és üzleti politikák továbbra is nagyon fontosak. Az agent szabadságát mindig biztonsági intézkedések és felügyeleti mechanizmusok korlátozzák (remélhetőleg).

## Gyakorlati alkalmazási esetek és érték

Az Agentic RAG olyan helyzetekben tűnik ki, ahol iteratív finomításra és pontosságra van szükség:

1. **Helyesség-központú környezetek:** Megfelelőségi ellenőrzésekben, szabályozási elemzésekben vagy jogi kutatásban az agentic modell többször ellenőrizheti a tényeket, több forrást megvizsgálhat, és újraírhat lekérdezéseket, amíg alaposan átvizsgált választ nem ad.
2. **Komplex adatbázis-interakciók:** Strukturált adat esetén, ahol a lekérdezések gyakran hibáznak vagy módosításra szorulnak, a rendszer önállóan finomíthatja lekérdezéseit Azure SQL vagy Microsoft Fabric OneLake használatával, biztosítva, hogy a végső lekérdezés megfeleljen a felhasználó szándékának.
3. **Kiterjesztett munkafolyamatok:** Hosszabb munkamenetek során új információk kerülhetnek elő, az Agentic RAG folyamatosan beépítheti az új adatokat, és stratégiákat módosíthat, miközben többet tanul a probléma területéről.

## Irányítás, átláthatóság és bizalom

Ahogy ezek a rendszerek egyre autonómabbak lesznek következtetési folyamataikban, az irányítás és az átláthatóság kulcsfontosságú:

- **Értelmezhető következtetés:** A modell audit nyomvonalat nyújthat a lekérdezésekről, amelyeket végrehajtott, a forrásokról, amelyeket megvizsgált, és a következtetési lépésekről, amelyeket tett konklúziója eléréséhez. Az olyan eszközök, mint az Azure AI Content Safety és az Azure AI Tracing / GenAIOps segíthetnek az átláthatóság fenntartásában és a kockázatok csökkentésében.
- **Elfogultság szabályozása és kiegyensúlyozott lekérdezés:** A fejlesztők hangolhatják a keresési stratégiákat annak érdekében, hogy kiegyensúlyozott, reprezentatív adatforrások kerüljenek figyelembe vételre, és rendszeresen auditolhatják a kimeneteket elfogultság vagy torzított mintázatok felismerése céljából, speciális modelleket használva fejlett adatelemző szervezetek számára az Azure Machine Learning révén.
- **Emberi felügyelet és megfelelőség:** Érzékeny feladatok esetén az emberi ellenőrzés továbbra is elengedhetetlen. Az Agentic RAG nem helyettesíti az emberi ítélőképességet magas kockázatú döntésekben – hanem kiegészíti azt, alaposabban ellenőrzött opciók biztosításával.

Alapvető fontosságú olyan eszközökkel rendelkezni, amelyek világos nyilvántartást biztosítanak a végrehajtott műveletekről. Ezek nélkül egy több lépéses folyamat hibakeresése nagyon nehéz lehet. Az alábbi példa a Literal AI-tól (a Chainlit mögött álló vállalat) egy Agent futtatásról:

![AgentRunExample](../../../translated_images/hu/AgentRunExample.471a94bc40cbdc0c.webp)

## Összegzés

Az Agentic RAG a mesterséges intelligencia rendszerek természetes fejlődését képviseli a komplex, adat-intenzív feladatok kezelésében. Azáltal, hogy egy ciklikus interakciós mintát alkalmaz, önállóan választ eszközöket és finomítja a lekérdezéseket, amíg magas színvonalú eredményt nem ér el, a rendszer túllép a statikus prompt követésen, és egy adaptívabb, kontextus-érzékeny döntéshozóvá válik. Bár továbbra is ember által meghatározott infrastruktúrákhoz és etikai irányelvekhez kötött, ezek az agentic képességek gazdagabb, dinamikusabb és végső soron hasznosabb AI interakciókat tesznek lehetővé mind vállalatok, mind végfelhasználók számára.

### Több kérdése van az Agentic RAG-ról?

Csatlakozzon a [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) szerveréhez, hogy találkozzon más tanulókkal, részt vehessen konzultációkon, és választ kapjon AI-ugynokokat érintő kérdéseire.

## További források

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">A Retrieval Augmented Generation (RAG) megvalósítása az Azure OpenAI Service segítségével: Ismerje meg, hogyan használhatja saját adatait az Azure OpenAI Service-zel. Ez a Microsoft Learn modul átfogó útmutatást biztosít a RAG megvalósításához</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">A generatív AI alkalmazások értékelése Microsoft Foundry-vel: Ez a cikk áttekinti a modellek értékelését és összehasonlítását nyilvánosan elérhető adatbázisokon, beleértve az Agentic AI alkalmazásokat és a RAG architektúrákat</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Mi az az Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Teljes útmutató az ügynökalapú Retrieval Augmented Generation-hez – hírek a generációs RAG-ról</a>

- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: turbózd fel RAG-ed lekérdezés újrafogalmazással és önlekérdezéssel! Hugging Face Nyílt Forráskódú AI Kézikönyv</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Agentikus rétegek hozzáadása a RAG-hez</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">A tudássegítők jövője: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Hogyan építsünk agentikus RAG rendszereket</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">A Microsoft Foundry Agent szolgáltatásának használata AI ügynökeid skálázásához</a>

### Tudományos cikkek

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Iteratív finomítás önvisszacsatolással</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Nyelvügynökök verbális megerősítéses tanulással</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: A nagynyelvű modellek önjavítása eszköz-interaktív kritika segítségével</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentikus lekérdezés-alapú generálás: Áttekintés az agentikus RAG-ről</a>

## Az ügynök gyors tesztelése (opcionális)

Miután megtanultad telepíteni az ügynököket a [16. leckében](../16-deploying-scalable-agents/README.md), gyorsan tesztelheted a jelen lecke `TravelRAGAgent` osztályát — ellenőrizve, hogy válaszai a tudásbázison alapulnak — a [`tests/lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) fájllal. Lásd a [`tests/README.md`](../tests/README.md) fájlt a futtatás módjáról.

## Előző lecke

[Eszközhasználati tervezési minta](../04-tool-use/README.md)

## Következő lecke

[Megbízható AI ügynökök építése](../06-building-trustworthy-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->