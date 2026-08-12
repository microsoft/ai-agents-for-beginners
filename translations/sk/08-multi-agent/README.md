[![Návrhové vzory preViacagentný systém](../../../translated_images/sk/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Kliknite na obrázok vyššie pre zobrazenie videa tejto lekcie)_

# Návrhové vzory pre viacagentné systémy

Hneď ako začnete pracovať na projekte, ktorý zahŕňa viac agentov, budete musieť zvážiť návrhový vzor viacagentného systému. Nemusí však byť hneď jasné, kedy prejsť na viac agentov a aké výhody to prináša.

## Úvod

V tejto lekcii sa pokúsime odpovedať na nasledujúce otázky:

- V ktorých scenároch sú viacagentné systémy použiteľné?
- Aké sú výhody používania viacerých agentov oproti jednému agentovi, ktorý vykonáva viac úloh?
- Aké sú stavebné bloky implementácie návrhového vzoru viacagentného systému?
- Ako získať prehľad o tom, ako viacerí agenti navzájom interagujú?

## Ciele učenia sa

Po tejto lekcii by ste mali byť schopní:

- Identifikovať scenáre, v ktorých sú viacagentné systémy vhodné
- Rozpoznať výhody používania viacerých agentov oproti jednému agentovi.
- Pochopiť stavebné bloky implementácie viacagentného návrhového vzoru.

Aký je širší obraz?

*Viacagentné systémy sú návrhový vzor, ktorý umožňuje viacerým agentom spolupracovať na dosiahnutí spoločného cieľa*.

Tento vzor sa široko používa v rôznych oblastiach, vrátane robotiky, autonómnych systémov a distribuovaného výpočtu.

## Scenáre, kde sa viacagentné systémy využívajú

Ktoré scenáre sú teda dobrým prípadom použitia viacagentných systémov? Odpoveďou je, že existuje mnoho prípadov, kde je výhodné použiť viac agentov, najmä v týchto prípadoch:

- **Veľké pracovné zaťaženie**: Veľké pracovné zaťaženie je možné rozdeliť na menšie úlohy a priradiť rôznym agentom, čo umožňuje paralelné spracovanie a rýchlejšie dokončenie. Príkladom je spracovanie veľkých dátových úloh.
- **Zložité úlohy**: Zložité úlohy, podobne ako veľké pracovné zaťaženie, je možné rozložiť na menšie podúlohy a priradiť rôznym agentom, ktorí sa špecializujú na konkrétny aspekt úlohy. Dobrým príkladom sú autonómne vozidlá, kde rôzni agenti riadia navigáciu, detekciu prekážok a komunikáciu s ostatnými vozidlami.
- **Rôznorodé znalosti**: Rôzni agenti môžu mať rôzne znalosti, čo im umožňuje efektívnejšie riešiť rôzne aspekty úlohy než jeden agent. Príkladom je zdravotná starostlivosť, kde agenti spravujú diagnostiku, liečebné plány a monitorovanie pacienta.

## Výhody používania viacerých agentov oproti jednému agentovi

Jednoagentový systém môže dobre fungovať pri jednoduchých úlohách, no pri zložitejších úlohách používanie viacerých agentov prináša niekoľko výhod:

- **Špecializácia**: Každý agent sa môže špecializovať na konkrétnu úlohu. Neschopnosť špecializácie v jednom agentovi znamená, že agent, ktorý robí všetko, môže byť zmätený, čo má robiť pri zložitých úlohách. Môže napríklad skončiť pri vykonávaní úlohy, na ktorú nie je najvhodnejší.
- **Škálovateľnosť**: Je jednoduchšie škálovať systémy pridaním ďalších agentov ako preťažovaním jediného agenta.
- **Odolnosť voči chybám**: Ak jeden agent zlyhá, ostatní môžu pokračovať v činnosti, čím sa zabezpečuje spoľahlivosť systému.

Uveďme príklad, rezervujme používateľovi výlet. Jednoagentový systém by musel zvládnuť všetky aspekty rezervácie výletu, od vyhľadania letov cez rezerváciu hotelov až po prenájom áut. Aby to zvládol, agent by potreboval nástroje na všetky tieto úlohy. To by mohlo viesť k zložitému a monolitickému systému, ktorý je ťažko udržiavateľný a škálovateľný. Naopak, viacagentový systém by mohol mať rôznych agentov špecializovaných na vyhľadávanie letov, rezerváciu hotelov a prenájom áut. To by systém spravilo modulárnejším, ľahšie udržiavateľným a škálovateľným.

Porovnajte to s cestovnou kanceláriou prevádzkovanou ako malý rodinný obchod oproti cestovnej kancelárii prevádzkovanej ako franšíza. Rodinný obchod by mal jedného agenta spravujúceho všetky aspekty rezervácie výletu, zatiaľ čo franšíza by mala rôznych agentov riešiacich rôzne časti procesu.

## Stavebné bloky implementácie viacagentného návrhového vzoru

Pred implementáciou viacagentného návrhového vzoru musíte pochopiť jeho stavebné bloky.

Pre lepšiu predstavu sa znovu pozrime na príklad rezervácie výletu pre používateľa. V tomto prípade stavebné bloky zahŕňajú:

- **Komunikácia agentov**: Agenti zodpovední za vyhľadávanie letov, rezerváciu hotelov a prenájom áut musia komunikovať a zdieľať informácie o preferenciách a obmedzeniach používateľa. Konkrétne, agent pre vyhľadávanie letov musí komunikovať s agentom pre rezerváciu hotelov, aby sa zabezpečilo, že hotel je rezervovaný na rovnaké dátumy ako let. To znamená, že agenti musia zdieľať informácie o dátumoch cesty používateľa, takže musíte rozhodnúť *ktorí agenti zdieľajú aké informácie a ako*.
- **Koordinačné mechanizmy**: Agenti musia koordinovať svoje činnosti, aby splnili preferencie a obmedzenia používateľa. Napríklad používateľ preferuje hotel blízko letiska, no obmedzením je, že prenájom áut je možný len na letisku. To znamená, že agent pre rezerváciu hotelov musí koordinovať s agentom pre prenájom áut, aby sa zabezpečilo splnenie preferencií a obmedzení. Musíte teda rozhodnúť *ako agenti koordinujú svoje akcie*.
- **Architektúra agenta**: Agenti musia mať vnútornú štruktúru na rozhodovanie a učenie sa z interakcií s používateľom. Agent pre vyhľadávanie letov musí mať štruktúru na rozhodovanie o tom, ktoré lety odporučiť používateľovi. Musíte teda rozhodnúť *ako agenti robia rozhodnutia a učia sa z interakcií s používateľom*. Príkladom môže byť, že agent pre vyhľadávanie letov použije model strojového učenia na odporúčanie letov na základe minulých preferencií používateľa.
- **Prehľad o interakciách viac agentov**: Musíte mať prehľad o tom, ako viacerí agenti medzi sebou interagujú. To znamená mať nástroje a techniky na sledovanie aktivít a interakcií agentov, ako sú nástroje na logovanie a monitorovanie, vizualizácie a výkonnostné metriky.
- **Vzory viacagentných systémov**: Existujú rôzne vzory implementácie viacagentných systémov, ako sú centralizované, decentralizované a hybridné architektúry. Musíte si vybrať vzor, ktorý najlepšie vyhovuje vášmu prípadu použitia.
- **Človek v slučke**: Vo väčšine prípadov bude človek v slučke a musíte agentov poučiť, kedy žiadať o zásah človeka. Môže to byť v podobe používateľa žiadajúceho o konkrétny hotel alebo let, ktorý agenti neodporučili, alebo požiadavka na potvrdenie pred rezerváciou letu či hotela.

## Prehľad o interakciách viac agentov

Je dôležité mať prehľad o tom, ako viacerí agenti medzi sebou interagujú. Tento prehľad je nevyhnutný na ladenie, optimalizáciu a zaistenie efektívnosti celého systému. Na to potrebujete nástroje a techniky na sledovanie aktivít a interakcií agentov, ako sú nástroje na logovanie a monitorovanie, vizualizácie a výkonnostné metriky.

Napríklad pri rezervácii výletu pre používateľa by ste mohli mať dashboard, ktorý ukazuje stav jednotlivých agentov, preferencie a obmedzenia používateľa a interakcie medzi agentmi. Tento dashboard by mohol zobraziť dátumy cesty používateľa, lety odporúčané agentom pre lety, hotely odporúčané hotelovým agentom a prenájom áut odporúčaný agentom pre prenájom áut. To by vám poskytlo jasný prehľad o tom, ako agenti medzi sebou interagujú a či sa dodržiavajú preferencie a obmedzenia používateľa.

Pozrime sa na jednotlivé aspekty podrobnejšie.

- **Nástroje na logovanie a monitorovanie**: Chcete logovať každú akciu agenta. Záznam môže obsahovať informácie o agentovi, ktorý akciu vykonal, akciu samotnú, čas vykonania a výsledok akcie. Tieto údaje je možné použiť na ladenie, optimalizáciu a iné účely.

- **Nástroje na vizualizáciu**: Vizualizácie vám pomôžu vidieť interakcie medzi agentmi intuitívnejším spôsobom. Napríklad graf, ktorý ukazuje tok informácií medzi agentmi, môže pomôcť identifikovať úzke miesta, neefektívnosť a iné problémy v systéme.

- **Metriky výkonnosti**: Metriky výkonnosti pomáhajú sledovať efektívnosť viacagentného systému. Napríklad môžete sledovať čas potrebný na dokončenie úlohy, počet dokončených úloh za jednotku času a presnosť odporúčaní agentov. Tieto informácie vám pomôžu nájsť oblasti na zlepšenie a optimalizovať systém.

## Vzory viacagentných systémov

Poďme sa pozrieť na niektoré konkrétne vzory, ktoré môžeme použiť na vytvorenie viacagentných aplikácií. Tu sú niektoré zaujímavé vzory, ktoré stojí za zváženie:

### Skupinový chat

Tento vzor je užitočný, keď chcete vytvoriť aplikáciu skupinového chatu, kde si viacerí agenti môžu vymieňať správy. Typické použitia sú tímová spolupráca, zákaznícka podpora a sociálne siete.

V tomto vzore každý agent predstavuje používateľa v skupinovom chate a správy sa vymieňajú medzi agentmi pomocou protokolu správy. Agenti môžu odosielať správy do chatu, prijímať správy zo skupiny a reagovať na správy od ostatných agentov.

Tento vzor môže byť implementovaný centralizovanou architektúrou, kde všetky správy prechádzajú cez centrálny server, alebo decentralizovanou architektúrou, kde si agenti správy vymieňajú priamo.

![Skupinový chat](../../../translated_images/sk/multi-agent-group-chat.ec10f4cde556babd.webp)

### Predávanie úloh

Tento vzor je užitočný, keď chcete vytvoriť aplikáciu, kde si viac agentov môže vzájomne predávať úlohy.

Typické prípady použitia tohto vzoru sú zákaznícka podpora, riadenie úloh a automatizácia pracovných tokov.

V tomto vzore každý agent predstavuje úlohu alebo krok vo workflow a agenti si môžu podľa preddefinovaných pravidiel úlohy predávať.

![Predávanie úloh](../../../translated_images/sk/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Spolupráca na filtrovaní odporúčaní

Tento vzor je užitočný, keď chcete vytvoriť aplikáciu, kde viacerí agenti spolupracujú na tvorbe odporúčaní pre používateľov.

Dôvod, prečo by ste chceli, aby viacerí agenti spolupracovali, je ten, že každý agent má inú odbornosť a môže prispieť k odporúčaniam rôznymi spôsobmi.

Pozrime sa na príklad, kde používateľ chce odporúčanie najlepšej akcie na nákup na burze.

- **Odborník v odvetví**: Jeden agent môže byť expertom na konkrétne odvetvie.
- **Technická analýza**: Iný agent môže byť expertom na technickú analýzu.
- **Fundamentálna analýza**: Ďalší agent môže byť odborníkom na fundamentálnu analýzu. Spoluprácou tieto agenti môžu používateľovi poskytnúť komplexnejšie odporúčania.

![Odporúčanie](../../../translated_images/sk/multi-agent-filtering.d959cb129dc9f608.webp)

## Scenár: Proces vrátenia peňazí

Predstavme si situáciu, kde zákazník žiada vrátenie peňazí za produkt. Do tohto procesu môže byť zapojených niekoľko agentov, rozdelme ich však na agentov špecifických pre tento proces a všeobecných agentov, ktorí sa dajú využiť aj inde.

**Agenti špecifickí pre proces vrátenia peňazí**:

Nižšie sú uvedení niektorí agenti, ktorí by mohli byť zapojení do procesu vrátenia peňazí:

- **Agent zákazníka**: Tento agent zastupuje zákazníka a je zodpovedný za iniciovanie procesu vrátenia peňazí.
- **Agent predajcu**: Tento agent zastupuje predajcu a spracováva vrátenie peňazí.
- **Agent platby**: Tento agent spracúva platby a je zodpovedný za vrátenie platby zákazníkovi.
- **Agent riešenia**: Tento agent rieši akékoľvek problémy, ktoré vzniknú počas procesu vrátenia peňazí.
- **Agent dodržiavania pravidiel**: Tento agent zabezpečuje, že proces vrátenia peňazí je v súlade s predpismi a politikami.

**Všeobecní agenti**:

Títo agenti môžu byť používaní aj v iných oblastiach vášho podnikania.

- **Agent dopravy**: Tento agent spravuje prepravu a je zodpovedný za zaslanie produktu späť predajcovi. Môže byť používaný ako pre proces vrátenia peňazí, tak aj všeobecne na prepravu produktov v rámci predaja.
- **Agent spätnej väzby**: Tento agent zhromažďuje spätnú väzbu od zákazníka. Spätnú väzbu možno zbierať kedykoľvek, nielen počas procesu vrátenia peňazí.
- **Agent eskalácie**: Tento agent eskaluje problémy na vyššiu úroveň podpory. Tento typ agenta môžete použiť v akomkoľvek procese, kde je potrebné eskalovať problém.
- **Agent notifikácií**: Tento agent zodpovedá za odosielanie notifikácií zákazníkovi v rôznych fázach procesu vrátenia peňazí.
- **Agent analytiky**: Tento agent analyzuje dáta súvisiace s procesom vrátenia peňazí.
- **Agent auditu**: Tento agent kontroluje proces vrátenia peňazí, aby zabezpečil, že prebieha správne.
- **Agent reportovania**: Tento agent generuje správy o procese vrátenia peňazí.
- **Agent znalostí**: Tento agent spravuje databázu vedomostí týkajúcich sa procesu vrátenia peňazí. Môže byť znalý nielen vrátení peňazí, ale aj iných častí vášho podnikania.
- **Agent bezpečnosti**: Tento agent zabezpečuje bezpečnosť procesu vrátenia peňazí.
- **Agent kvality**: Tento agent zabezpečuje kvalitu procesu vrátenia peňazí.

Predošlý zoznam agentov obsahuje rôznych agentov pre špecifický proces vrátenia peňazí i všeobecných agentov použiteľných v iných oblastiach vášho podnikania. Dúfame, že vám to poskytuje predstavu, ako si vybrať agentov pre váš viacagentný systém.

## Zadanie

Navrhnite viacagentný systém pre proces zákazníckej podpory. Identifikujte agentov zapojených do procesu, ich úlohy a zodpovednosti a spôsob, akým navzájom komunikujú. Zvážte agentov špecifických pre zákaznícku podporu aj všeobecných agentov použiteľných v iných oblastiach vášho podnikania.


> Počkajte a porozmýšľajte, než si prečítate nasledujúce riešenie, možno budete potrebovať viac agentov, než si myslíte.

> TIP: Premyslite si rôzne etapy procesu zákazníckej podpory a zvážte aj agentov potrebných pre akýkoľvek systém.

## Riešenie

[Riešenie](./solution/solution.md)

## Overovanie znalostí

### Otázka 1

Ktorý scenár najviac vyhovuje multi-agentnému systému?

- [ ] A1: Podporný bot odpovedá na bežné otázky pomocou jednej databázy znalostí a malej sady nástrojov.
- [ ] A2: Refundácia vyžaduje samostatné roly pre podvody, platby a dodržiavanie predpisov, každú s vlastnými nástrojmi, pričom ich výsledky musia byť koordinované.
- [ ] A3: Tá istá jednoduchá klasifikačná požiadavka prichádza tisícky krát za hodinu.

### Otázka 2

Kedy je zvyčajne lepšou voľbou jeden agent?

- [ ] A1: Úlohu je možné zvládnuť jednou sadou inštrukcií a nástrojov, bez špecializovaných odovzdaní.
- [ ] A2: Agent má prístup k viac ako jednému nástroju.
- [ ] A3: Pracovný postup vyžaduje samostatné roly s rôznymi oprávneniami a nezávislé audítorské záznamy.

[Riešenie kvízu](./solution/solution-quiz.md)

## Zhrnutie

V tejto lekcii sme sa pozreli na multi-agentný dizajnový vzor, vrátane scenárov, kde je použitie multi-agentov vhodné, výhod využívania multi-agentov oproti jednému agentovi, základné stavebné prvky implementácie multi-agentného dizajnového vzoru a ako mať prehľad o tom, ako viacerí agenti navzájom interagujú.

### Máte ďalšie otázky o multi-agentnom dizajnovom vzore?

Pripojte sa k [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kde môžete stretnúť ďalších študentov, zúčastniť sa konzultačných hodín a získať odpovede na otázky o AI agentoch.

## Dodatočné zdroje

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Dokumentácia Microsoft Agent Framework</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Agentné dizajnové vzory</a>


## Predchádzajúca lekcia

[Plánovanie dizajnu](../07-planning-design/README.md)

## Nasledujúca lekcia

[Metakognícia v AI agentoch](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->