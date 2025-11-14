<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a008c204051cba8d0e253b75f261c41",
  "translation_date": "2025-08-29T20:37:05+00:00",
  "source_file": "08-multi-agent/README.md",
  "language_code": "sk"
}
-->
[![Multi-Agent Design](../../../translated_images/lesson-8-thumbnail.278a3e4a59137d625df92de3f885d2da2a92b1f7017abba25a99fb25edd83a55.sk.png)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Kliknite na obrázok vyššie, aby ste si pozreli video k tejto lekcii)_

# Dizajnové vzory pre multi-agentové systémy

Akonáhle začnete pracovať na projekte, ktorý zahŕňa viacerých agentov, budete musieť zvážiť dizajnový vzor pre multi-agentové systémy. Avšak nemusí byť hneď jasné, kedy prejsť na multi-agentové systémy a aké sú ich výhody.

## Úvod

V tejto lekcii sa snažíme odpovedať na nasledujúce otázky:

- Aké sú scenáre, kde sú multi-agentové systémy použiteľné?
- Aké sú výhody používania multi-agentových systémov oproti jednému agentovi vykonávajúcemu viacero úloh?
- Aké sú stavebné bloky implementácie dizajnového vzoru pre multi-agentové systémy?
- Ako môžeme získať prehľad o tom, ako viacerí agenti medzi sebou interagujú?

## Ciele učenia

Po tejto lekcii by ste mali byť schopní:

- Identifikovať scenáre, kde sú multi-agentové systémy použiteľné.
- Rozpoznať výhody používania multi-agentových systémov oproti jednému agentovi.
- Pochopiť stavebné bloky implementácie dizajnového vzoru pre multi-agentové systémy.

Aký je širší kontext?

*Multi-agentové systémy sú dizajnový vzor, ktorý umožňuje viacerým agentom spolupracovať na dosiahnutí spoločného cieľa.*

Tento vzor sa široko používa v rôznych oblastiach, vrátane robotiky, autonómnych systémov a distribuovaného výpočtu.

## Scenáre, kde sú multi-agentové systémy použiteľné

Aké scenáre sú vhodné na použitie multi-agentových systémov? Odpoveďou je, že existuje mnoho scenárov, kde je zamestnanie viacerých agentov prospešné, najmä v nasledujúcich prípadoch:

- **Veľké pracovné zaťaženie**: Veľké pracovné zaťaženie môže byť rozdelené na menšie úlohy a pridelené rôznym agentom, čo umožňuje paralelné spracovanie a rýchlejšie dokončenie. Príkladom je spracovanie veľkého množstva dát.
- **Komplexné úlohy**: Komplexné úlohy, podobne ako veľké pracovné zaťaženie, môžu byť rozdelené na menšie podúlohy a pridelené rôznym agentom, pričom každý sa špecializuje na konkrétny aspekt úlohy. Dobrým príkladom sú autonómne vozidlá, kde rôzni agenti spravujú navigáciu, detekciu prekážok a komunikáciu s inými vozidlami.
- **Rôznorodá odbornosť**: Rôzni agenti môžu mať rôznorodú odbornosť, čo im umožňuje efektívnejšie riešiť rôzne aspekty úlohy než jeden agent. Príkladom je zdravotníctvo, kde agenti môžu spravovať diagnostiku, liečebné plány a monitorovanie pacientov.

## Výhody používania multi-agentových systémov oproti jednému agentovi

Systém s jedným agentom môže dobre fungovať pri jednoduchých úlohách, ale pri zložitejších úlohách môže používanie viacerých agentov priniesť niekoľko výhod:

- **Špecializácia**: Každý agent sa môže špecializovať na konkrétnu úlohu. Nedostatok špecializácie u jedného agenta znamená, že agent dokáže robiť všetko, ale môže sa zmiasť pri riešení zložitej úlohy. Môže napríklad vykonávať úlohu, na ktorú nie je najlepšie vybavený.
- **Škálovateľnosť**: Je jednoduchšie škálovať systémy pridaním ďalších agentov než preťažovaním jedného agenta.
- **Odolnosť voči chybám**: Ak jeden agent zlyhá, ostatní môžu pokračovať vo fungovaní, čím sa zabezpečí spoľahlivosť systému.

Pozrime sa na príklad: rezervácia výletu pre používateľa. Systém s jedným agentom by musel spravovať všetky aspekty procesu rezervácie výletu, od hľadania letov po rezerváciu hotelov a prenájom áut. Na dosiahnutie tohto cieľa by jeden agent musel mať nástroje na spracovanie všetkých týchto úloh. To by mohlo viesť k zložitému a monolitickému systému, ktorý je ťažké udržiavať a škálovať. Multi-agentový systém by na druhej strane mohol mať rôznych agentov špecializovaných na hľadanie letov, rezerváciu hotelov a prenájom áut. To by systém urobilo modulárnejším, ľahšie udržiavateľným a škálovateľným.

Porovnajte to s cestovnou kanceláriou vedenou ako rodinný podnik oproti cestovnej kancelárii vedenou ako franšíza. Rodinný podnik by mal jedného agenta, ktorý spravuje všetky aspekty procesu rezervácie výletu, zatiaľ čo franšíza by mala rôznych agentov, ktorí spravujú rôzne aspekty procesu rezervácie výletu.

## Stavebné bloky implementácie dizajnového vzoru pre multi-agentové systémy

Predtým, než budete môcť implementovať dizajnový vzor pre multi-agentové systémy, musíte pochopiť stavebné bloky, ktoré tvoria tento vzor.

Urobme to konkrétnejším opäť na príklade rezervácie výletu pre používateľa. V tomto prípade by stavebné bloky zahŕňali:

- **Komunikácia medzi agentmi**: Agenti na hľadanie letov, rezerváciu hotelov a prenájom áut musia komunikovať a zdieľať informácie o preferenciách a obmedzeniach používateľa. Musíte rozhodnúť o protokoloch a metódach tejto komunikácie. Konkrétne to znamená, že agent na hľadanie letov musí komunikovať s agentom na rezerváciu hotelov, aby zabezpečil, že hotel je rezervovaný na rovnaké dátumy ako let. To znamená, že agenti musia zdieľať informácie o dátumoch cestovania používateľa, čo znamená, že musíte rozhodnúť *ktorí agenti zdieľajú informácie a ako ich zdieľajú*.
- **Koordinačné mechanizmy**: Agenti musia koordinovať svoje akcie, aby zabezpečili, že preferencie a obmedzenia používateľa sú splnené. Preferencia používateľa môže byť, že chce hotel blízko letiska, zatiaľ čo obmedzenie môže byť, že prenájom áut je dostupný iba na letisku. To znamená, že agent na rezerváciu hotelov musí koordinovať s agentom na prenájom áut, aby zabezpečil, že preferencie a obmedzenia používateľa sú splnené. To znamená, že musíte rozhodnúť *ako agenti koordinujú svoje akcie*.
- **Architektúra agenta**: Agenti musia mať vnútornú štruktúru na rozhodovanie a učenie sa z interakcií s používateľom. To znamená, že agent na hľadanie letov musí mať vnútornú štruktúru na rozhodovanie o tom, ktoré lety odporučiť používateľovi. To znamená, že musíte rozhodnúť *ako agenti robia rozhodnutia a učia sa z interakcií s používateľom*. Príklady toho, ako sa agent učí a zlepšuje, môžu byť, že agent na hľadanie letov môže používať model strojového učenia na odporúčanie letov používateľovi na základe jeho minulých preferencií.
- **Prehľad o interakciách medzi agentmi**: Musíte mať prehľad o tom, ako viacerí agenti medzi sebou interagujú. To znamená, že musíte mať nástroje a techniky na sledovanie aktivít a interakcií agentov. To môže byť vo forme nástrojov na logovanie a monitorovanie, vizualizačných nástrojov a výkonnostných metrík.
- **Vzory pre multi-agentové systémy**: Existujú rôzne vzory na implementáciu multi-agentových systémov, ako sú centralizované, decentralizované a hybridné architektúry. Musíte rozhodnúť o vzore, ktorý najlepšie vyhovuje vášmu prípadu použitia.
- **Človek v procese**: Vo väčšine prípadov budete mať človeka v procese a musíte inštruovať agentov, kedy požiadať o zásah človeka. To môže byť vo forme používateľa, ktorý žiada o konkrétny hotel alebo let, ktorý agenti neodporučili, alebo žiada o potvrdenie pred rezerváciou letu alebo hotela.

## Prehľad o interakciách medzi agentmi

Je dôležité, aby ste mali prehľad o tom, ako viacerí agenti medzi sebou interagujú. Tento prehľad je nevyhnutný na ladenie, optimalizáciu a zabezpečenie efektívnosti celého systému. Na dosiahnutie tohto cieľa musíte mať nástroje a techniky na sledovanie aktivít a interakcií agentov. To môže byť vo forme nástrojov na logovanie a monitorovanie, vizualizačných nástrojov a výkonnostných metrík.

Napríklad v prípade rezervácie výletu pre používateľa môžete mať dashboard, ktorý zobrazuje stav každého agenta, preferencie a obmedzenia používateľa a interakcie medzi agentmi. Tento dashboard môže zobrazovať dátumy cestovania používateľa, lety odporúčané agentom na hľadanie letov, hotely odporúčané agentom na rezerváciu hotelov a prenájmy áut odporúčané agentom na prenájom áut. To by vám poskytlo jasný prehľad o tom, ako agenti medzi sebou interagujú a či sú preferencie a obmedzenia používateľa splnené.

Pozrime sa na každý z týchto aspektov podrobnejšie.

- **Nástroje na logovanie a monitorovanie**: Chcete mať logovanie pre každú akciu vykonanú agentom. Záznam môže obsahovať informácie o agentovi, ktorý vykonal akciu, vykonanej akcii, čase vykonania akcie a výsledku akcie. Tieto informácie môžu byť použité na ladenie, optimalizáciu a ďalšie.
- **Vizualizačné nástroje**: Vizualizačné nástroje vám môžu pomôcť vidieť interakcie medzi agentmi intuitívnejším spôsobom. Napríklad môžete mať graf, ktorý zobrazuje tok informácií medzi agentmi. To vám môže pomôcť identifikovať úzke miesta, neefektívnosti a ďalšie problémy v systéme.
- **Výkonnostné metriky**: Výkonnostné metriky vám môžu pomôcť sledovať efektívnosť multi-agentového systému. Napríklad môžete sledovať čas potrebný na dokončenie úlohy, počet úloh dokončených za jednotku času a presnosť odporúčaní vytvorených agentmi. Tieto informácie vám môžu pomôcť identifikovať oblasti na zlepšenie a optimalizovať systém.

## Vzory pre multi-agentové systémy

Pozrime sa na niektoré konkrétne vzory, ktoré môžeme použiť na vytvorenie aplikácií s multi-agentovými systémami. Tu sú niektoré zaujímavé vzory, ktoré stojí za zváženie:

### Skupinový chat

Tento vzor je užitočný, keď chcete vytvoriť aplikáciu skupinového chatu, kde viacerí agenti môžu medzi sebou komunikovať. Typické prípady použitia tohto vzoru zahŕňajú tímovú spoluprácu, zákaznícku podporu a sociálne siete.

V tomto vzore každý agent predstavuje používateľa v skupinovom chate a správy sa vymieňajú medzi agentmi pomocou protokolu na odosielanie správ. Agenti môžu posielať správy do skupinového chatu, prijímať správy zo skupinového chatu a odpovedať na správy od iných agentov.

Tento vzor môže byť implementovaný pomocou centralizovanej architektúry, kde všetky správy prechádzajú cez centrálny server, alebo decentralizovanej architektúry, kde sa správy vymieňajú priamo.

![Skupinový chat](../../../translated_images/multi-agent-group-chat.ec10f4cde556babd7b450fd01e1a0fac1f9788c27d3b9e54029377bb1bdd1db6.sk.png)

### Odovzdanie úlohy

Tento vzor je užitočný, keď chcete vytvoriť aplikáciu, kde viacerí agenti môžu odovzdávať úlohy jeden druhému.

Typické prípady použitia tohto vzoru zahŕňajú zákaznícku podporu, správu úloh a automatizáciu pracovných procesov.

V tomto vzore každý agent predstavuje úlohu alebo krok v pracovnom procese a agenti môžu odovzdávať úlohy iným agentom na základe preddefinovaných pravidiel.

![Odovzdanie úlohy](../../../translated_images/multi-agent-hand-off.4c5fb00ba6f8750a0754bf29d49fa19d578080c61da40416df84d866bcdd87a3.sk.png)

### Kolaboratívne filtrovanie

Tento vzor je užitočný, keď chcete vytvoriť aplikáciu, kde viacerí agenti môžu spolupracovať na vytváraní odporúčaní pre používateľov.

Prečo by ste chceli, aby viacerí agenti spolupracovali? Pretože každý agent môže mať rôznu odbornosť a môže prispieť k procesu odporúčania rôznymi spôsobmi.

Pozrime sa na príklad, kde používateľ chce odporúčanie na najlepšiu akciu na kúpu na akciovom trhu.

- **Odborník na odvetvie**: Jeden agent môže byť odborníkom na konkrétne odvetvie.
- **Technická analýza**: Ďalší agent môže byť odborníkom na technickú analýzu.
- **Fundamentálna analýza**: A ďalší agent môže byť odborníkom na fundamentálnu analýzu. Spoluprácou môžu títo agenti poskytnúť používateľovi komplexnejšie odporúčanie.

![Odporúčanie](../../../translated_images/multi-agent-filtering.d959cb129dc9f60826916f0f12fe7a8339b532f5f236860afb8f16b63ea10dc2.sk.png)

## Scenár: Proces refundácie

Zvážte scenár, kde sa zákazník snaží získať refundáciu za produkt. Môže byť zapojených pomerne veľa agentov, ale rozdelíme ich na agentov špecifických pre tento proces a všeobecných agentov, ktorí môžu byť použiteľní v iných procesoch.

**Agenti špecifickí pre proces refundácie**:

Nasledujú niektorí agenti, ktorí by mohli byť zapojení do procesu refundácie:

- **Agent zákazníka**: Tento agent predstavuje zákazníka a je zodpovedný za iniciovanie procesu refundácie.
- **Agent predajcu**: Tento agent predstavuje predajcu a je zodpovedný za spracovanie refundácie.
- **Agent platby**: Tento agent predstavuje proces platby a je zodpovedný za refundáciu platby zákazníka.
- **Agent riešenia problémov**: Tento agent predstavuje proces riešenia problémov a je zodpovedný za riešenie akýchkoľvek problémov, ktoré vzniknú počas procesu refundácie.
- **Agent súladu**: Tento agent predstavuje proces súladu a je zodpovedný za zabezpečenie, že proces refundácie je v súlade s predpismi a politikami.

**Všeobecní agenti**:

Títo agenti môžu byť použiteľní v iných častiach vášho podnikania.

- **Agent dopravy**: Tento agent predstavuje proces dopravy a je zodpovedný za dopravu produktu späť predajcovi. Tento agent môže byť použitý ako v procese refundácie, tak aj pri všeobecnej doprave produktu napríklad pri nákupe.
- **Agent spätnej väzby**: Tento agent predstavuje proces spätnej väzby a je zodpovedný za zber spätnej väzby od zákazníka. Spätná väzba môže byť získaná kedykoľvek, nielen počas procesu refundácie.
- **Agent eskalácie**: Tento agent predstavuje proces eskalácie a je zodpovedný za eskaláciu problémov na vyššiu úroveň podpory. Tento typ agenta môžete použiť v akomkoľvek procese, kde je potrebné eskalovať problém.
- **Agent notifikácií**: Tento agent predstavuje proces notifikácií a je zodpovedný za odosielanie notifikácií zákazníkovi v rôznych fázach procesu refundácie.
- **Agent analytiky**: Tento agent predstavuje proces analytiky a je zodpovedný za analýzu dát súvisiacich s procesom refundácie.
- **Agent auditu**: Tento agent predstavuje proces auditu a je zodpovedný za audit procesu refundácie, aby sa zabezpečilo, že je vykonávaný správne.
- **Agent reportovania**: Tento agent predstavuje proces reportovania a
Navrhnite multi-agentový systém pre proces zákazníckej podpory. Identifikujte agentov zapojených do procesu, ich úlohy a zodpovednosti a spôsob, akým spolu komunikujú. Zohľadnite agentov špecifických pre proces zákazníckej podpory, ako aj všeobecných agentov, ktorí môžu byť využití v iných častiach vášho podnikania.

> Zamyslite sa predtým, než si prečítate nasledujúce riešenie, možno budete potrebovať viac agentov, než si myslíte.

> TIP: Premýšľajte o rôznych fázach procesu zákazníckej podpory a zvážte aj agentov potrebných pre akýkoľvek systém.

## Riešenie

[Riešenie](./solution/solution.md)

## Kontrola vedomostí

Otázka: Kedy by ste mali zvážiť použitie multi-agentov?

- [ ] A1: Keď máte malú pracovnú záťaž a jednoduchú úlohu.
- [ ] A2: Keď máte veľkú pracovnú záťaž.
- [ ] A3: Keď máte jednoduchú úlohu.

[Riešenie kvízu](./solution/solution-quiz.md)

## Zhrnutie

V tejto lekcii sme sa zaoberali návrhovým vzorom multi-agentov, vrátane scenárov, kde sú multi-agenti použiteľní, výhodami použitia multi-agentov oproti jednému agentovi, stavebnými blokmi implementácie návrhového vzoru multi-agentov a spôsobom, ako mať prehľad o tom, ako spolu viacerí agenti komunikujú.

### Máte ďalšie otázky o návrhovom vzore Multi-Agent?

Pripojte sa na [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), kde sa môžete stretnúť s ďalšími študentmi, zúčastniť sa konzultačných hodín a získať odpovede na vaše otázky o AI agentoch.

## Ďalšie zdroje

- 

## Predchádzajúca lekcia

[Návrh plánovania](../07-planning-design/README.md)

## Nasledujúca lekcia

[Metakognícia v AI agentoch](../09-metacognition/README.md)

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.