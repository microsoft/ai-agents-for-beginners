[![Návrh viacagentných systémov](../../../translated_images/sk/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Kliknite na obrázok vyššie pre zobrazenie videa k tejto lekcii)_

# Vzory návrhu viacagentných systémov

Hneď ako začnete pracovať na projekte, ktorý zahŕňa viac agentov, budete musieť zvážiť viacagentný návrhový vzor. Nie je však vždy hneď jasné, kedy prejsť na viac agentov a aké výhody to prináša.

## Úvod

V tejto lekcii sa pokúsime odpovedať na nasledovné otázky:

- V ktorých situáciách sú viacagentné systémy použiteľné?
- Aké sú výhody použitia viac agentov v porovnaní s jedným agentom vykonávajúcim viacero úloh?
- Aké sú základné stavebné kamene implementácie viacagentného návrhového vzoru?
- Ako mať prehľad o interakciách medzi viacerými agentmi?

## Ciele učenia

Po tejto lekcii by ste mali byť schopní:

- Identifikovať situácie, kde sú viacagentné systémy použiteľné
- Rozpoznať výhody použitia viac agentov oproti jednému agentovi.
- Pochopiť základné stavebné kamene implementácie viacagentného návrhového vzoru.

Aký je širší obraz?

*Viac agentov je návrhový vzor, ktorý umožňuje viacerým agentom spolupracovať na dosiahnutí spoločného cieľa*.

Tento vzor sa bežne využíva v rôznych oblastiach, vrátane robotiky, autonómnych systémov a distribuovaných výpočtov.

## Situácie, kde sú viacagentné systémy použiteľné

Aké situácie sú teda vhodné na použitie viac agentov? Odpoveď je, že existuje mnoho situácií, kde je výhodné použiť viacerých agentov, najmä v nasledujúcich prípadoch:

- **Veľké pracovné zaťaženie**: Veľké pracovné zaťaženie môže byť rozdelené na menšie úlohy priradené rôznym agentom, čo umožňuje paralelné spracovanie a rýchlejšie dokončenie. Príkladom je spracovanie veľkého množstva dát.
- **Komplexné úlohy**: Komplexné úlohy, podobne ako veľké zaťaženie, môžu byť rozdelené na menšie podúlohy, ktorým sú priradení agenti špecializujúci sa na konkrétne aspekty úlohy. Dobrou ukážkou sú autonómne vozidlá, kde rôzni agenti riadia navigáciu, detekciu prekážok a komunikáciu s inými vozidlami.
- **Rôznorodé znalosti**: Rôzni agenti môžu mať rozličné odbornosti, čo im umožňuje efektívnejšie zvládnuť rôzne oblasti úlohy než jediný agent. Dobrou ukážkou je zdravotná starostlivosť, kde agenti riadia diagnostiku, plány liečby a sledovanie pacienta.

## Výhody použitia viac agentov oproti jednému agentovi

Jednoagentný systém môže fungovať dobre pre jednoduché úlohy, ale pri zložitejších úlohách môže viac agentov priniesť niekoľko výhod:

- **Špecializácia**: Každý agent môže byť špecializovaný pre konkrétnu úlohu. Nepresná špecializácia pri jednom agentovi znamená, že agent robí všetko, ale môže byť zmätený, čo má robiť pri zložitej úlohe. Napríklad môže skončiť vykonávaním úlohy, na ktorú nie je najvhodnejší.
- **Škálovateľnosť**: Je jednoduchšie rozšíriť systém pridaním ďalších agentov namiesto preťaženia jediného agenta.
- **Odolnosť voči chybám**: Ak jeden agent zlyhá, ostatní môžu pokračovať v činnosti, čím sa zvyšuje spoľahlivosť systému.

Uveďme príklad — zarezervujme používateľovi cestu. Jednoagentný systém by musel zvládnuť všetky aspekty rezervácie, od hľadania letov, cez rezerváciu hotelov až po prenájom áut. Aby to zvládol, agent by potreboval nástroje pre všetky tieto úlohy, čo by mohlo viesť k zložitému a monolitickému systému, ktorý je ťažké udržiavať a škálovať. Viacagentný systém by mohol mať rôznych agentov špecializovaných na hľadanie letov, rezerváciu hotelov a prenájom áut. To by systém spravilo modulárnejším, ľahším na údržbu a škálovateľným.

Porovnajte to s cestovnou kanceláriou prevádzkovanou rodinným obchodom verzus cestovnou kanceláriou vo forme franšízy. Rodinný obchod by mal jedného agenta riešiaceho všetky aspekty rezervácie, zatiaľ čo franšíza by mala rôznych agentov riešiacich rôzne aspekty procesu.

## Základné stavebné kamene implementácie viacagentného návrhového vzoru

Pred implementáciou viacagentného vzoru musíte poznať základné stavebné kamene tohto vzoru.

Urobme to konkrétnejším, opäť sa pozrime na príklad rezervácie cesty pre používateľa. Stavebné kamene by zahŕňali:

- **Komunikácia agentov**: Agenti pre hľadanie letov, rezerváciu hotelov a prenájom áut musia komunikovať a zdieľať informácie o preferenciách a obmedzeniach používateľa. Musíte rozhodnúť o protokoloch a metódach tejto komunikácie. Konkrétne to znamená, že agent pre hľadanie letov musí komunikovať s agentom pre rezerváciu hotelov, aby sa zabezpečilo, že hotel je rezervovaný na rovnaké dátumy ako let. To znamená, že agenti musia zdieľať informácie o dátumoch cesty používateľa, čiže musíte rozhodnúť *ktorí agenti zdieľajú informácie a ako ich zdieľajú*.
- **Koordinačné mechanizmy**: Agenti musia koordinovať svoje činnosti, aby sa zabezpečilo dodržanie preferencií a obmedzení používateľa. Užívateľskou preferenciou môže byť hotel blízko letiska, zatiaľ čo obmedzenie môže byť, že prenájom áut je k dispozícii len na letisku. To znamená, že agent pre rezerváciu hotelov musí koordinovať s agentom pre prenájom áut, aby boli splnené preferencie a obmedzenia používateľa. Musíte rozhodnúť *ako agenti koordinujú svoje činnosti*.
- **Architektúra agentov**: Agenti musia mať vnútornú štruktúru na rozhodovanie a učenie sa z interakcií s používateľom. To znamená, že agent pre hľadanie letov musí mať vnútornú štruktúru na rozhodovanie o tom, ktoré lety odporučiť používateľovi. Musíte rozhodnúť *ako agenti rozhodujú a učia sa z interakcií s používateľom*. Príklady, ako agent učí a zlepšuje sa môžu byť napríklad použitie modelu strojového učenia na odporúčanie letov na základe minulých preferencií používateľa.
- **Viditeľnosť interakcií viac agentov**: Potrebujete mať prehľad o tom, ako viacerí agenti medzi sebou interagujú. To znamená, že potrebujete nástroje a techniky na sledovanie aktivít a interakcií agentov. Môžu to byť nástroje na logovanie a monitorovanie, vizualizačné nástroje a metriky výkonnosti.
- **Vzory viacagentných systémov**: Existujú rôzne vzory na implementáciu viacagentných systémov, ako sú centralizované, decentralizované a hybridné architektúry. Musíte rozhodnúť, ktorý vzor najlepšie vyhovuje vašemu prípadu použitia.
- **Človek v slučke**: Vo väčšine prípadov bude vo vnútri procesu človek a musíte určiť agentom, kedy majú žiadať jeho zásah. Môže to byť v podobe požiadavky používateľa na konkrétny hotel alebo let, ktorý agenti neodporučili, alebo žiadosť o potvrdenie pred rezerváciou letu či hotela.

## Viditeľnosť interakcií viac agentov

Je dôležité mať prehľad o tom, ako viacerí agenti spolu komunikujú. Táto viditeľnosť je nevyhnutná na ladenie, optimalizáciu a zabezpečenie celkovej efektívnosti systému. Na to potrebujete mať nástroje a techniky na sledovanie aktivít a interakcií agentov. Môžu to byť nástroje na zaznamenávanie a monitorovanie, vizualizačné nástroje a metriky výkonu.

Napríklad pri rezervácii cesty pre používateľa by ste mohli mať dashboard, ktorý zobrazuje stav každého agenta, preferencie a obmedzenia používateľa a interakcie medzi agentmi. Tento dashboard by mohol ukazovať dátumy cesty používateľa, lety odporúčané agentom pre lety, hotely odporúčané agentom pre hotely a prenájom áut odporúčaný agentom pre prenájom áut. Poskytoval by jasný pohľad na to, ako agenti spolu komunikujú a či sú preferencie a obmedzenia používateľa splnené.

Pozrime sa na jednotlivé aspekty podrobnejšie.

- **Nástroje na zaznamenávanie a monitorovanie**: Chcete mať zaznamenané každé konanie agenta. Záznam môže obsahovať informácie o agente, ktorý vykonal akciu, o akcii, čase vykonania a výsledku akcie. Tieto informácie sa potom dajú použiť na ladenie, optimalizáciu a ďalšie účely.

- **Vizualizačné nástroje**: Vizualizačné nástroje vám pomôžu vidieť interakcie medzi agentmi intuitívnejším spôsobom. Napríklad graf, ktorý zobrazí tok informácií medzi agentmi. To vám môže pomôcť identifikovať úzke miesta, neefektívnosť a iné problémy v systéme.

- **Metriky výkonu**: Metriky výkonu vám pomôžu sledovať efektívnosť viacagentného systému. Môžete napríklad sledovať čas na dokončenie úlohy, počet dokončených úloh za jednotku času a presnosť odporúčaní agentov. Tieto informácie vám umožnia identifikovať oblasti na zlepšenie a optimalizovať systém.

## Vzory viacagentných systémov

Pozrime sa na konkrétne vzory, ktoré môžeme použiť na tvorbu viacagentných aplikácií. Tu je niekoľko zaujímavých vzorov, ktoré stojí za zváženie:

### Skupinový chat

Tento vzor je užitočný, ak chcete vytvoriť aplikáciu skupinového chatu, kde viacerí agenti môžu komunikovať medzi sebou. Typické použitia zahŕňajú tímovú spoluprácu, zákaznícku podporu a sociálne siete.

V tomto vzore každý agent predstavuje používateľa v skupinovom chate a správy sa vymieňajú medzi agentmi pomocou protokolu pre zasielanie správ. Agenti môžu posielať správy do skupiny, prijímať správy zo skupiny a odpovedať na správy od iných agentov.

Tento vzor možno implementovať pomocou centralizovanej architektúry, kde všetky správy prechádzajú centrálnym serverom, alebo decentralizovanej architektúry, kde si správy agenti vymieňajú priamo.

![Skupinový chat](../../../translated_images/sk/multi-agent-group-chat.ec10f4cde556babd.webp)

### Odovzdávanie úloh

Tento vzor je užitočný, ak chcete vytvoriť aplikáciu, kde viacerí agenti môžu odovzdávať úlohy medzi sebou.

Typické použitia zahŕňajú zákaznícku podporu, riadenie úloh a automatizáciu pracovných tokov.

V tomto vzore každý agent predstavuje úlohu alebo krok v pracovnom toku a agenti môžu odovzdávať úlohy iným agentom na základe preddefinovaných pravidiel.

![Odovzdávanie úloh](../../../translated_images/sk/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Spolupracujúca filtrácia

Tento vzor je užitočný, ak chcete vytvoriť aplikáciu, kde viacerí agenti môžu spolupracovať na tvorbe odporúčaní pre používateľov.

Dôvod, prečo chcete, aby viacerí agenti spolupracovali, je ten, že každý agent môže mať inú odbornú znalosť a prispievať k odporúčaciemu procesu rôznymi spôsobmi.

Uveďme príklad, keď chce používateľ odporúčanie na najlepší akciový titul na nákup na burze.

- **Odborník na odvetvie**: Jeden agent môže byť odborníkom na konkrétne odvetvie.
- **Technická analýza**: Ďalší agent môže byť odborníkom na technickú analýzu.
- **Fundamentálna analýza**: A ďalší agent môže byť odborníkom na fundamentálnu analýzu. Spoluprácou môžu títo agenti poskytnúť komplexnejšie odporúčanie používateľovi.

![Odporúčanie](../../../translated_images/sk/multi-agent-filtering.d959cb129dc9f608.webp)

## Scenár: Proces reklamácie

Zvážme scenár, kde zákazník sa snaží získať vrátenie peňazí za produkt, v tomto procese môže byť zapojených niekoľko agentov, ale rozdelme ich na agentov špecifických pre tento proces a všeobecných agentov, ktorí môžu byť používaní v iných procesoch.

**Agenti špecifickí pre proces reklamácie**:

Nasledujú agenti, ktorí by mohli byť zapojení do procesu reklamácie:

- **Agent zákazníka**: Tento agent reprezentuje zákazníka a zodpovedá za začatie procesu reklamácie.
- **Agent predajcu**: Tento agent reprezentuje predajcu a zodpovedá za spracovanie reklamácie.
- **Agent platieb**: Tento agent reprezentuje platobný proces a zodpovedá za vrátenie peňazí zákazníkovi.
- **Agent riešení**: Tento agent reprezentuje proces riešenia a zodpovedá za vyriešenie problémov, ktoré sa vyskytnú počas procesu reklamácie.
- **Agent zhody**: Tento agent reprezentuje proces dodržiavania predpisov a zodpovedá za zabezpečenie, že proces reklamácie je v súlade s pravidlami a politikami.

**Všeobecní agenti**:

Títo agenti môžu byť použiteľní aj v iných častiach vášho podniku.

- **Agent dopravy**: Tento agent reprezentuje proces dopravy a zodpovedá za odoslanie produktu späť predajcovi. Tento agent môže byť použitý tak v procese reklamácie, ako aj pri všeobecnej doprave produktu napríklad pri nákupe.
- **Agent spätnej väzby**: Tento agent reprezentuje proces zberu spätnej väzby od zákazníka. Spätná väzba môže byť získaná kedykoľvek, nielen počas procesu reklamácie.
- **Agent eskalácie**: Tento agent reprezentuje proces eskalácie a zodpovedá za presunutie problémov na vyššiu úroveň podpory. Tento typ agenta môžete použiť v akomkoľvek procese, kde je potrebné eskalovať problém.
- **Agent notifikácií**: Tento agent reprezentuje proces zasielania notifikácií zákazníkovi v rôznych fázach procesu reklamácie.
- **Agent analytiky**: Tento agent reprezentuje proces analýzy dát súvisiacich s procesom reklamácie.
- **Agent auditu**: Tento agent reprezentuje proces auditu a zodpovedá za kontrolu, že proces reklamácie prebieha správne.
- **Agent reportovania**: Tento agent reprezentuje proces tvorby správ o procese reklamácie.
- **Agent znalostí**: Tento agent reprezentuje správu znalostnej databázy informácií súvisiacich s procesom reklamácie. Tento agent môže mať znalosti nielen o reklamáciách, ale aj o iných častiach vášho podniku.
- **Agent bezpečnosti**: Tento agent reprezentuje proces bezpečnosti a zodpovedá za zabezpečenie bezpečnosti procesu reklamácie.
- **Agent kvality**: Tento agent reprezentuje proces zabezpečovania kvality a zodpovedá za zabezpečenie kvality procesu reklamácie.

Vyššie sme uviedli pomerne veľa agentov, a to pre špecifický proces reklamácie aj pre všeobecných agentov použiteľných aj inde vo vašom podniku. Dúfam, že to poskytuje predstavu o tom, ako môžete rozhodnúť, ktorých agentov použiť vo vašom viacagentnom systéme.

## Zadanie

Navrhnite viacagentný systém pre proces zákazníckej podpory. Identifikujte agentov zapojených do procesu, ich úlohy a zodpovednosti a ich vzájomné interakcie. Zvážte agentov špecifických pre zákaznícku podporu aj všeobecných agentov použiteľných v iných častiach vášho podniku.


> Zamyslite sa, než si prečítate nasledujúce riešenie, možno budete potrebovať viac agentov, než si myslíte.

> TIP: Premýšľajte o rôznych fázach procesu zákazníckej podpory a tiež zvažujte agentov potrebných pre akýkoľvek systém.

## Riešenie

[Riešenie](./solution/solution.md)

## Kontroly vedomostí

### Otázka 1

Ktorý scenár najlepšie vyhovuje systému s viacerými agentmi?

- [ ] A1: Podporný bot odpovedá na bežné otázky pomocou jednej znalostnej databázy a malej sady nástrojov.
- [ ] A2: Pracovný postup pre vrátenie peňazí vyžaduje samostatné roly pre podvod, platby a súlad, každú s vlastnými nástrojmi, pričom výsledky musia byť koordinované.
- [ ] A3: Rovnaká jednoduchá žiadosť o klasifikáciu prichádza tisíckrát za hodinu.

### Otázka 2

Kedy je zvyčajne lepšou voľbou jeden agent?

- [ ] A1: Úloha sa dá riešiť jedným súborom inštrukcií a nástrojov, bez potreby špecializovaných odovzdaní.
- [ ] A2: Agent má prístup k viacerým nástrojom.
- [ ] A3: Pracovný postup vyžaduje samostatné roly s rôznymi oprávneniami a nezávislé audítorské záznamy.

[Riešenie kvízu](./solution/solution-quiz.md)

## Zhrnutie

V tejto lekcii sme sa pozreli na návrhový vzor s viacerými agentmi, vrátane situácií, kde sú viacagentové systémy použiteľné, výhody používania viacerých agentov oproti jednému agentovi, stavebné kamene implementácie návrhového vzoru viacagentového systému a ako získať prehľad o tom, ako si jednotliví agenti navzájom interagujú.

### Máte viac otázok o viacagentovom návrhovom vzore?

Pridajte sa k [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), aby ste sa stretli s ostatnými študentmi, zúčastnili sa konzultácií a získali odpovede na svoje otázky o AI agentoch.

## Dodatočné zdroje

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Dokumentácia Microsoft Agent Framework</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Agentické návrhové vzory</a>


## Predchádzajúca lekcia

[Návrh plánovania](../07-planning-design/README.md)

## Nasledujúca lekcia

[Metakognícia v AI agentoch](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->