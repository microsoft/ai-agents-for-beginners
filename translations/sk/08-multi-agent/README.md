[![Multi-agent dizajnové vzory](../../../translated_images/sk/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Kliknite na obrázok vyššie pre zobrazenie videa tejto lekcie)_

# Dizajnové vzory pre multi-agentné systémy

Akonáhle začnete pracovať na projekte, ktorý zahŕňa viacero agentov, budete musieť zvážiť použitie multi-agentného dizajnového vzoru. Nie je však vždy okamžite jasné, kedy prejsť na multi-agentný prístup a aké sú jeho výhody.

## Úvod

V tejto lekcii si odpovieme na nasledujúce otázky:

- Aké sú scenáre, kde je použitie multi-agentov vhodné?
- Aké sú výhody používania multi-agentov oproti jednému agentovi, ktorý vykonáva viacero úloh?
- Aké sú stavebné bloky implementácie multi-agentného dizajnového vzoru?
- Ako môžeme mať prehľad o tom, ako viacerí agenti navzájom interagujú?

## Ciele učenia

Po tejto lekcii by ste mali byť schopní:

- Identifikovať scenáre, kde je použitie multi-agentov vhodné
- Rozpoznať výhody používania multi-agentov oproti jednému agentovi
- Pochopiť stavebné bloky implementácie multi-agentného dizajnového vzoru

Aký je širší obraz?

*Multi-agenti sú dizajnovým vzorom, ktorý umožňuje viacerým agentom spolupracovať na dosiahnutí spoločného cieľa*.

Tento vzor sa používa v rôznych oblastiach, vrátane robotiky, autonómnych systémov a distribuovaných výpočtov.

## Scenáre, kde je použitie multi-agentov vhodné

Aké sú teda dobré scenáre na použitie multi-agentov? Odpoveď je, že existuje mnoho situácií, kde je výhodné použiť viacero agentov, najmä v týchto prípadoch:

- **Veľké pracovné zaťaženie**: Veľké úlohy môžu byť rozdelené na menšie časti a pridelené rôznym agentom, čo umožňuje paralelné spracovanie a rýchlejšie dokončenie. Príkladom môže byť veľký úloha spracovania údajov.
- **Zložité úlohy**: Zložité úlohy, podobne ako veľké pracovné zaťaženie, možno rozdeliť na menšie podúlohy a prideliť rôznym agentom, z ktorých každý sa špecializuje na určitý aspekt úlohy. Dobrým príkladom sú autonómne vozidlá, kde rôzni agenti riadia navigáciu, detekciu prekážok a komunikáciu s inými vozidlami.
- **Rôznorodá odbornosť**: Rôzni agenti môžu mať rôzne odbornosti, čo im umožňuje efektívnejšie zvládať rôzne aspekty úlohy než jeden jediný agent. Dobrým príkladom je zdravotná starostlivosť, kde agenti riadia diagnostiku, liečebné plány a monitorovanie pacientov.

## Výhody používania multi-agentov oproti jednému agentovi

Systém s jedným agentom môže dobre fungovať pri jednoduchých úlohách, no pri zložitejších úlohách viacerí agenti prinášajú niekoľko výhod:

- **Špecializácia**: Každý agent môže byť špecializovaný na konkrétnu úlohu. Nepretržitá všestrannosť jedného agenta môže viesť k zmätku pri riešení zložitej úlohy. Napríklad agent sa môže nakoniec venovať úlohe, na ktorú nie je najvhodnejší.
- **Škálovateľnosť**: Je jednoduchšie rozšíriť systém pridaním ďalších agentov než preťažením jedného agenta.
- **Odolnosť voči chybám**: Ak jeden agent zlyhá, ostatní môžu pokračovať v práci, čím sa zabezpečuje spoľahlivosť systému.

Napríklad, pri rezervácii cesty pre používateľa by systémy s jedným agentom museli zvládnuť všetky aspekty procesu, od hľadania letov až po rezerváciu hotelov a prenájom áut. Takýto agent by potreboval nástroje na celé spektrum úloh. To by mohlo viesť k zložitým a monolitickým systémom, ktoré sa ťažko udržiavajú a škálujú. Naopak, multi-agentný systém by mohol mať rôznych agentov špecializovaných na hľadanie letov, rezerváciu hotelov a prenájom áut. To by urobilo systém modulárnejším, ľahším na údržbu a škálovateľným.

Porovnajte to so cestovnou kanceláriou prevádzkovanou ako malý rodinný podnik oproti cestovnej kancelárii fungujúcej ako franšíza. Malý podnik by mal jedného agenta spravujúceho všetky aspekty rezervácie cesty, zatiaľ čo franšíza by mala rôznych agentov, ktorí riešia rôzne časti procesu.

## Stavebné bloky implementácie multi-agentného dizajnového vzoru

Pred implementáciou multi-agentného vzoru je potrebné pochopiť jeho stavebné bloky.

Urobme si to konkrétnejšie na príklade rezervácie cesty pre používateľa. V tomto prípade zahŕňajú stavebné bloky:

- **Komunikácia agentov**: Agenti pre vyhľadávanie letov, rezerváciu hotelov a prenájom áut musia komunikovať a zdieľať informácie o preferenciách a obmedzeniach používateľa. Musíte sa rozhodnúť, aké protokoly a metódy použijete na túto komunikáciu. To konkrétne znamená, že agent na vyhľadávanie letov musí komunikovať s agentom pre rezerváciu hotelov, aby sa zabezpečilo, že hotel bude rezervovaný na rovnaké dátumy ako let. Agenti teda musia zdieľať informácie o dátumoch cesty používateľa, a preto musíte rozhodnúť *ktorí agenti si informácie zdieľajú a ako*.
- **Koordinačné mechanizmy**: Agenti musia koordinovať svoje činnosti, aby boli splnené preferencie a obmedzenia používateľa. Používateľ môže preferovať hotel blízko letiska, zatiaľ čo obmedzenie môže byť, že požičovne áut sú dostupné len na letisku. To znamená, že agent rezervujúci hotely musí spolupracovať s agentom na prenájom áut, aby sa zabezpečilo splnenie preferencií a obmedzení používateľa. Musíte teda rozhodnúť *ako agenti koordinujú svoje činnosti*.
- **Architektúra agenta**: Agenti potrebujú vnútornú štruktúru na rozhodovanie a učenie sa z interakcií s používateľom. Napríklad agent na vyhľadávanie letov potrebuje mať vnútornú architektúru, ktorá mu umožní rozhodovať o tom, ktoré lety odporučiť používateľovi. Musíte rozhodnúť *ako agenti rozhodujú a učia sa z interakcií s používateľom*. Príkladom môže byť použitie modelu strojového učenia agentom na vyhľadávanie letov na odporúčanie letov na základe predchádzajúcich preferencií používateľa.
- **Prehľad o interakciách multi-agentov**: Potrebujete mať prehľad o tom, ako viacerí agenti medzi sebou interagujú. To znamená, že potrebujete nástroje a techniky na sledovanie aktivít a interakcií agentov. Môžu to byť nástroje na logovanie a monitorovanie, vizualizačné nástroje a výkonnostné metriky.
- **Multi-agentné vzory**: Existujú rôzne vzory implementácie multi-agentných systémov, ako sú centralizované, decentralizované a hybridné architektúry. Musíte sa rozhodnúť, ktorý vzor najlepšie vyhovuje vášmu prípad použitia.
- **Človek v slučke**: Vo väčšine prípadov je v procese človek a musíte určiť, kedy majú agenti požiadať o zásah človeka. Môže to byť napríklad vtedy, keď používateľ požaduje konkrétny hotel alebo let, ktoré agenti neodporučili, alebo keď je potrebné potvrdenie pred rezerváciou letu či hotela.

## Prehľad o interakciách multi-agentov

Je dôležité mať prehľad o tom, ako viacerí agenti medzi sebou interagujú. Tento prehľad je nevyhnutný pre ladenie, optimalizáciu a zabezpečenie celkovej efektívnosti systému. Na to potrebujete nástroje a techniky na sledovanie aktivít a interakcií agentov. Môžu to byť nástroje na logovanie a monitorovanie, vizualizačné nástroje a výkonnostné metriky.

Napríklad pri rezervácii cesty pre používateľa by ste mohli mať panel, ktorý zobrazuje stav každého agenta, preferencie a obmedzenia používateľa a interakcie medzi agentmi. Tento panel by mohol zobrazovať dátumy cesty používateľa, lety odporúčané agentom pre lety, hotely odporúčané agentom pre hotely a prenájom áut odporúčaný agentom na prenájom. To by vám poskytlo jasný obraz o tom, ako agenti interagujú a či sú splnené preferencie a obmedzenia používateľa.

Pozrime sa na tieto aspekty detailnejšie.

- **Nástroje na logovanie a monitorovanie**: Chcete mať zaznamenané všetky akcie, ktoré agent vykonáva. Záznam môže obsahovať informácie o agente, ktorý vykonal akciu, o samotnej akcii, čase vykonania a výsledku. Tieto informácie môžete následne použiť na ladenie, optimalizáciu a pod.
- **Vizualizačné nástroje**: Vizualizácia pomáha vidieť interakcie medzi agentmi intuitívnejším spôsobom. Mohli by ste mať napríklad graf zobrazujúci tok informácií medzi agentmi. Pomohlo by vám to identifikovať úzke miesta, neefektívnosti a ďalšie problémy v systéme.
- **Výkonnostné metriky**: Metriky vám pomôžu sledovať efektívnosť multi-agentného systému. Môžete merať čas potrebný na dokončenie úlohy, počet dokončených úloh za jednotku času a presnosť odporúčaní agentov. Tieto informácie vám pomôžu nájsť oblasti na zlepšenie a systém optimalizovať.

## Multi-agentné vzory

Poďme sa pozrieť na konkrétne vzory, ktoré môžeme použiť na tvorbu multi-agentných aplikácií. Tu sú niektoré zaujímavé vzory, ktoré stojí za to zvážiť:

### Skupinový chat

Tento vzor je vhodný, keď chcete vytvoriť aplikáciu na skupinový chat, kde viacerí agenti môžu medzi sebou komunikovať. Typické použitia zahŕňajú tímovú spoluprácu, zákaznícku podporu a sociálne siete.

V tomto vzore každý agent reprezentuje používateľa v skupinovom chate a správy sa medzi agentmi vymieňajú pomocou protokolu na odosielanie správ. Agenti môžu posielať správy do skupinového chatu, prijímať správy zo skupiny a odpovedať na správy od ostatných agentov.

Tento vzor sa dá implementovať buď pomocou centralizovanej architektúry, kde sú všetky správy smerované cez centrálny server, alebo decentralizovanej architektúry, kde si správy agenti vymieňajú priamo.

![Skupinový chat](../../../translated_images/sk/multi-agent-group-chat.ec10f4cde556babd.webp)

### Odovzdanie úloh (Hand-off)

Tento vzor je vhodný, keď chcete vytvoriť aplikáciu, kde môžu viacerí agenti odovzdávať úlohy medzi sebou.

Typické použitia zahŕňajú zákaznícku podporu, správu úloh a automatizáciu pracovných tokov.

V tomto vzore každý agent reprezentuje úlohu alebo krok v pracovnom toku a agenti môžu na základe preddefinovaných pravidiel odovzdávať úlohy iným agentom.

![Odovzdanie úloh](../../../translated_images/sk/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Kolaboratívne filtrovanie

Tento vzor sa hodí, keď chcete vytvoriť aplikáciu, kde viacerí agenti spolupracujú na poskytovaní odporúčaní používateľom.

Prečo používať viac agentov? Každý agent môže mať inú odbornosť a prispievať k procesu odporúčaní rôznymi spôsobmi.

Napríklad používateľ chce odporúčanie na najlepší akciový titul na kúpu na burze.

- **Odborník na odvetvie**: Jeden agent môže byť expertom na konkrétne odvetvie.
- **Technická analýza**: Iný agent môže byť odborníkom na technickú analýzu.
- **Fundamentálna analýza**: Ďalší agent môže byť expertom na fundamentálnu analýzu. Spoluprácou môžu agenti poskytnúť komplexnejšie odporúčania používateľovi.

![Odporúčanie](../../../translated_images/sk/multi-agent-filtering.d959cb129dc9f608.webp)

## Scenár: Proces vrátenia peňazí

Predstavte si scenár, kde zákazník sa snaží získať vrátenie peňazí za produkt. V tomto procese môže byť zapojených viac agentov, ale rozdelíme ich na agentov špecifických pre tento proces a všeobecných agentov, ktorí môžu byť použiteľní aj v iných procesoch.

**Agenti špecifickí pre proces vrátenia peňazí**:

Nasledujúci agenti môžu byť zapojení do procesu vrátenia peňazí:

- **Agent zákazníka**: Tento agent reprezentuje zákazníka a je zodpovedný za iniciovanie procesu vrátenia.
- **Agent predajcu**: Tento agent reprezentuje predajcu a je zodpovedný za spracovanie vrátenia.
- **Agent platieb**: Tento agent reprezentuje proces platby a zabezpečuje vrátenie peňazí zákazníkovi.
- **Agent riešenia**: Tento agent reprezentuje proces riešenia problémov vzniknutých počas vrátenia a zabezpečuje ich vyriešenie.
- **Agent súladu (compliance)**: Tento agent kontroluje, či je proces vrátenia v súlade s pravidlami a predpismi.

**Všeobecní agenti**:

Títo agenti môžu byť použiteľní aj v iných oblastiach vášho biznisu.

- **Agent dopravy**: Tento agent zastrešuje proces dopravy a zabezpečuje odoslanie produktu späť predajcovi. Môže byť použitý aj pri všeobecnej doprave pri nákupe.
- **Agent spätnej väzby**: Tento agent zodpovedá za zber spätnej väzby od zákazníka. Spätná väzba môže byť zbieraná kedykoľvek, nie len počas procesu vrátenia.
- **Agent eskalácie**: Tento agent slúži na eskaláciu problémov na vyššiu úroveň podpory. Tento typ agenta možno použiť v akomkoľvek procese, kde je potrebné eskalovať problém.
- **Agent notifikácií**: Tento agent zodpovedá za zasielanie upozornení zákazníkovi v rôznych fázach procesu vrátenia.
- **Agent analýz**: Tento agent spracováva dáta súvisiace s procesom vrátenia a vykonáva analýzy.
- **Agent auditu**: Tento agent kontroluje správnosť vykonávania procesu vrátenia.
- **Agent reportingu**: Tento agent generuje správy o procese vrátenia.
- **Agent znalostí**: Tento agent spravuje databázu znalostí o procese vrátenia a ďalších oblastiach vášho biznisu.
- **Agent bezpečnosti**: Tento agent zabezpečuje bezpečnosť počas celého procesu vrátenia.
- **Agent kvality**: Tento agent dohliada na kvalitu vykonávania procesu vrátenia.

Uvedených agentov je pomerne veľa, vrátane špecifických pre proces vrátenia, ale aj všeobecných, použiteľných v iných častiach vášho biznisu. Dúfame, že vám to poskytne predstavu, ako sa rozhodnúť, ktorých agentov použiť vo vašom multi-agentnom systéme.

## Zadanie úlohy

Navrhnite multi-agentný systém pre proces zákazníckej podpory. Identifikujte agentov zapojených v procese, ich úlohy a zodpovednosti a spôsob ich vzájomnej interakcie. Zvážte agentov špecifických pre proces zákazníckej podpory aj všeobecných agentov, ktorí môžu byť použiteľní aj v iných oblastiach vášho biznisu.
> Zamyslite sa, než si prečítate nasledujúce riešenie, možno budete potrebovať viac agentov, než si myslíte.

> TIP: Premýšľajte o rôznych fázach procesu zákazníckej podpory a zvážte aj agentov potrebných pre akýkoľvek systém.

## Riešenie

[Riešenie](./solution/solution.md)

## Kontroly vedomostí

Otázka: Kedy by ste mali zvážiť použitie viacerých agentov?

- [ ] A1: Keď máte malú záťaž a jednoduchú úlohu.
- [ ] A2: Keď máte veľkú záťaž
- [ ] A3: Keď máte jednoduchú úlohu.

[Kvíz riešenia](./solution/solution-quiz.md)

## Zhrnutie

V tejto lekcii sme preskúmali viacagentový návrhový vzor, vrátane scenárov, kde je použitie viacerých agentov vhodné, výhod používania viacagentov oproti jednému agentovi, stavebné kamene implementácie viacagentového návrhového vzoru a ako mať prehľad o interakcii viacerých agentov medzi sebou.

### Máte ďalšie otázky o viacagentovom návrhovom vzore?

Pridajte sa do [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), kde sa môžete stretnúť s ostatnými študentmi, zúčastniť sa konzultačných hodín a získať odpovede na vaše otázky o AI agentoch.

## Ďalšie zdroje

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Dokumentácia Microsoft Agent Framework</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Agentové návrhové vzory</a>


## Predchádzajúca lekcia

[Plánovanie dizajnu](../07-planning-design/README.md)

## Nasledujúca lekcia

[Metakognícia v AI agentoch](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Upozornenie**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, berte prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne výklady vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->