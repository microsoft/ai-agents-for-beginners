# Pamäť pre AI agentov 
[![Agent Memory](../../../translated_images/sk/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Pri diskutovaní o jedinečných výhodách tvorby AI agentov sa najmä hovorí o dvoch veciach: schopnosti volať nástroje na dokončenie úloh a schopnosti zlepšovať sa v priebehu času. Pamäť je základom vytvárania samo-zlepšujúcich sa agentov, ktorí môžu vytvárať lepšie zážitky pre našich používateľov.

V tejto lekcii sa pozrieme na to, čo je pamäť pre AI agentov a ako ju môžeme spravovať a využívať v prospech našich aplikácií.

## Úvod

Táto lekcia pokryje:

• **Pochopenie pamäte AI agenta**: Čo je pamäť a prečo je pre agentov nevyhnutná.

• **Implementácia a ukladanie pamäte**: Praktické metódy pridávania pamäťových schopností vašim AI agentom, so zameraním na krátkodobú a dlhodobú pamäť.

• **Zabezpečenie samo-zlepšovania AI agentov**: Ako pamäť umožňuje agentom učiť sa z minulých interakcií a zlepšovať sa v priebehu času.

## Dostupné implementácie

Táto lekcia obsahuje dva rozsiahle návodové zošity:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementuje pamäť pomocou Mem0 a Azure AI Search s Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementuje štruktúrovanú pamäť pomocou Cognee, automaticky buduje znalostný graf podporený embeddingmi, vizualizuje graf a inteligentné vyhľadávanie

## Ciele učenia

Po dokončení tejto lekcie budete vedieť:

• **Rozlíšiť rôzne typy pamäte AI agenta**, vrátane pracovnej, krátkodobej a dlhodobej pamäte, ako aj špecializovaných foriem ako persona a epizodická pamäť.

• **Implementovať a spravovať krátkodobú a dlhodobú pamäť pre AI agentov** pomocou Microsoft Agent Framework, využívajúc nástroje ako Mem0, Cognee, Whiteboard memory a integráciu s Azure AI Search.

• **Pochopiť princípy za samo-zlepšujúcimi sa AI agentmi** a ako robustné systémy správy pamäte prispievajú k nepretržitému učeniu sa a adaptácii.

## Pochopenie pamäte AI agenta

V jadre je **pamäť pre AI agentov mechanizmus, ktorý im umožňuje uchovávať a si vybavovať informácie**. Tieto informácie môžu byť konkrétne detaily o rozhovore, preferencie používateľa, minulé akcie alebo dokonca naučené vzory.

Bez pamäte sú AI aplikácie často bezstavové, čo znamená, že každá interakcia začína od nuly. To vedie k opakujúcemu sa a frustrujúcemu používateľskému zážitku, kde agent "zabúda" predchádzajúci kontext alebo preferencie.

### Prečo je pamäť dôležitá?

inteligencia agenta je hlboko spojená so schopnosťou si vybaviť a využiť minulé informácie. Pamäť umožňuje agentom byť:

• **Reflexívni**: Učiť sa z minulých činností a výsledkov.

• **Interaktívni**: Udržiavať kontext prebiehajúceho rozhovoru.

• **Proaktívni a reaktívni**: Predvídať potreby alebo primerane reagovať na základe historických dát.

• **Autonómni**: Fungovať viac nezávisle čerpaním z uložených znalostí.

Cieľom implementácie pamäte je spraviť agentov **spoľahlivejšími a schopnejšími**.

### Typy pamäte

#### Pracovná pamäť

Predstavte si ju ako kúsok papierovej plochy, ktorú agent používa počas jednej prebiehajúcej úlohy alebo procesu premýšľania. Uchováva okamžité informácie potrebné na výpočet ďalšieho kroku.

Pre AI agentov pracovná pamäť často zachytáva najrelevantnejšie informácie z rozhovoru, aj keď je celá história konverzácie dlhá alebo orezaná. Zameriava sa na vyťahovanie kľúčových prvkov ako požiadavky, návrhy, rozhodnutia a akcie.

**Príklad pracovnej pamäte**

V cestovnej kancelárii by pracovná pamäť mohla zachytiť aktuálnu požiadavku používateľa, napríklad "Chcem si rezervovať výlet do Paríža". Táto konkrétna požiadavka je uchovávaná v bezprostrednom kontexte agenta, aby usmernila aktuálnu interakciu.

#### Krátkodobá pamäť

Tento typ pamäte uchováva informácie počas jednej konverzácie alebo relácie. Je to kontext aktuálneho rozhovoru, ktorý agentovi umožňuje odkazovať na predchádzajúce kolá dialógu.

V príkladoch Python SDK pre [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) sa toto mapuje na `AgentSession`, vytvorenú pomocou `agent.create_session()`. Relácia je vstavaná krátkodobá pamäť rámca: udržiava kontext konverzácie dostupný, pokiaľ sa tá istá relácia používa, ale tento kontext sa neuchováva po ukončení relácie alebo reštarte aplikácie. Pre fakty a preferencie, ktoré musia prežiť medzi reláciami, používajte dlhodobú pamäť, zvyčajne cez databázu, vektorový index alebo iné perzistentné úložisko.

**Príklad krátkodobej pamäte**

Ak sa používateľ opýta: "Koľko by stál let do Paríža?" a následne doplní: "A čo ubytovanie tam?", krátkodobá pamäť zabezpečí, že agent rozumie, že "tam" sa vzťahuje na "Paríž" v rámci tej istej konverzácie.

#### Dlhodobá pamäť

Toto sú informácie, ktoré pretrvávajú naprieč viacerými konverzáciami alebo reláciami. Umožňuje agentom pamätať si preferencie používateľa, historické interakcie alebo všeobecné znalosti počas dlhého obdobia. To je dôležité pre personalizáciu.

**Príklad dlhodobej pamäte**

Dlhodobá pamäť by mohla uchovávať informáciu, že "Ben má rád lyžovanie a outdoorové aktivity, obľubuje kávu s výhľadom na hory a chce sa vyhnúť zložitým lyžiarskym svahom kvôli bývalému zraneniu". Tieto informácie, naučené z predchádzajúcich interakcií, ovplyvňujú odporúčania v budúcich cestovných plánoch, čím ich robia vysoko personalizovanými.

#### Pamäť persony

Tento špecializovaný typ pamäte pomáha agentovi vyvinúť konzistentnú "osobnosť" alebo "personu". Umožňuje agentovi pamätať si detaily o sebe alebo svojej zamýšľanej úlohe, čím sú interakcie plynulejšie a zamerané.

**Príklad pamäte persony**
Ak je cestovný agent navrhnutý ako "expert na plánovanie lyžovania", pamäť persony môže posilniť túto rolu a ovplyvniť jeho odpovede tak, aby boli v súlade s tónom a znalosťami odborníka.

#### Pamäť pracovného postupu / epizódová pamäť

Táto pamäť uchováva sekvenciu krokov, ktoré agent vykonáva počas zložitej úlohy, vrátane úspechov a neúspechov. Je to ako spomínanie na konkrétne "epizódy" alebo minulé skúsenosti, z ktorých sa môže učiť.

**Príklad epizódovej pamäte**

Ak sa agent pokúsil rezervovať konkrétny let, ale zlyhal kvôli nedostupnosti, epizódová pamäť by túto chybu zaznamenala, čo agentovi umožní skúsiť alternatívne lety alebo informovať používateľa o probléme pri ďalšom pokuse informovanejšie.

#### Pamäť entít

Táto pamäť zahŕňa extrahovanie a zapamätanie si konkrétnych entít (ako osoby, miesta alebo veci) a udalostí z rozhovorov. Umožňuje agentovi vytvoriť štruktúrované pochopenie kľúčových diskutovaných prvkov.

**Príklad pamäte entít**

Z rozhovoru o minulej ceste by agent mohol extrahovať "Paríž", "Eiffelova veža" a "večera v reštaurácii Le Chat Noir" ako entity. Pri ďalšej interakcii by agent mohol spomenúť "Le Chat Noir" a ponúknuť novú rezerváciu tam.

#### Štruktúrovaný RAG (Retrieval Augmented Generation)

Kým RAG je širšia technika, "Štruktúrovaný RAG" je vyzdvihovaný ako silná pamäťová technológia. Extrahuje husté, štruktúrované informácie z rôznych zdrojov (rozhovory, e-maily, obrázky) a využíva ich na zvýšenie presnosti, vybavovania a rýchlosti odpovedí. Na rozdiel od klasického RAG, ktoré sa spolieha len na sémantickú podobnosť, Štruktúrovaný RAG pracuje s inherentnou štruktúrou informácií.

**Príklad štruktúrovaného RAG**

Namiesto jednoduchého porovnávania kľúčových slov by Štruktúrovaný RAG mohol analyzovať údaje o lete (cieľ, dátum, čas, letecká spoločnosť) z e-mailu a ukladať ich štruktúrovane. To umožňuje presné dotazy ako "Ktorý let som si rezervoval do Paríža v utorok?"

## Implementácia a ukladanie pamäte

Implementácia pamäte pre AI agentov zahŕňa systematický proces **správy pamäte**, ktorý zahŕňa generovanie, ukladanie, získavanie, integráciu, aktualizáciu a dokonca aj "zabúdanie" (alebo mazanie) informácií. Získavanie je obzvlášť kľúčový aspekt.

### Špecializované pamäťové nástroje

#### Mem0

Jedným zo spôsobov, ako ukladať a spravovať pamäť agenta, je používanie špecializovaných nástrojov ako Mem0. Mem0 funguje ako perzistentná vrstva pamäte, ktorá agentom umožňuje vybaviť si relevantné interakcie, uchovávať používateľské preferencie a faktický kontext a učiť sa z úspechov a neúspechov v priebehu času. Myšlienka je, že bezstavoví agenti sa stanú stavovými.

Funguje cez **dvojfázový pamäťový proces: extrakcia a aktualizácia**. Najprv sú správy pridané do vlákna agenta zasielané službe Mem0, ktorá využíva veľký jazykový model (LLM) na zhrnutie histórie konverzácie a extrahovanie nových spomienok. Následne fáza aktualizácie riadená LLM rozhoduje, či tieto spomienky pridať, upraviť alebo vymazať, pričom ich ukladá do hybridného úložiska dát, ktoré môže obsahovať vektorové, grafové a kľúčovo-hodnotové databázy. Tento systém tiež podporuje rôzne typy pamäte a môže začleňovať grafovú pamäť na správu vzťahov medzi entitami.

#### Cognee

Ďalším silným prístupom je použitie **Cognee**, open-source sémantickej pamäte pre AI agentov, ktorá transformuje štruktúrované a neštruktúrované údaje do dotazovateľných znalostných grafov podporovaných embeddingmi. Cognee poskytuje **dvojité úložisko** kombinujúce vyhľadávanie podľa vektorovej podobnosti s grafovými vzťahmi, čo agentom umožňuje chápať nielen to, ktoré informácie sú si podobné, ale aj ako sa koncepty navzájom vzťahujú.

Vyniká vo **hybridnom získavaní**, ktoré spája vektorovú podobnosť, grafovú štruktúru a LLM uvažovanie – od vyhľadávania v surových útržkoch po otázky s grafovým povedomím. Systém udržiava **živú pamäť**, ktorá sa vyvíja a rastie a zároveň zostáva dotazovateľná ako jeden prepojený graf, podporujúci kontext krátkodobej relácie aj dlhodobú perzistentnú pamäť.

Návod v Cognee notebooku ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonštruje budovanie tejto jednotnej pamäťovej vrstvy, s praktickými príkladmi prijímania rôznych dátových zdrojov, vizualizácie znalostného grafu a dotazovania sa rôznymi stratégiami vyhľadávania prispôsobenými špecifickým potrebám agenta.

### Ukladanie pamäte s RAG

Okrem špecializovaných pamäťových nástrojov ako Mem0 môžete využiť robustné vyhľadávacie služby ako **Azure AI Search ako backend na ukladanie a získavanie pamätí**, najmä pre štruktúrovaný RAG.

Toto umožňuje zakotviť odpovede vášho agenta vo vlastných dátach, čím sa zabezpečia relevantnejšie a presnejšie odpovede. Azure AI Search sa môže použiť na ukladanie používateľsky špecifických cestovných pamätí, katalógov produktov alebo akýchkoľvek iných doménových znalostí.

Azure AI Search podporuje schopnosti ako **Štruktúrovaný RAG**, ktorý exceluje v extrakcii a získavaní hustých, štruktúrovaných informácií z veľkých datasetov ako histórie konverzácií, e-mailov, alebo dokonca obrázkov. Poskytuje to "nadľudskú presnosť a vybavenie" v porovnaní s tradičnými prístupmi delenia textu a embeddingov.

## Zabezpečenie samo-zlepšovania AI agentov

Bežný vzorec pre samo-zlepšujúcich sa agentov zahŕňa zavedenie **"agenta znalostí"**. Tento samostatný agent sleduje hlavnú konverzáciu medzi používateľom a primárnym agentom. Jeho úlohou je:

1. **Identifikovať cenné informácie**: Určiť, či časť rozhovoru stojí za uloženie ako všeobecné znalosti alebo špecifická preferencia používateľa.

2. **Extrahovať a zhrnúť**: Odísť podstatné učenie alebo preferenciu z rozhovoru.

3. **Uložiť do znalostnej bázy**: Persistovať tieto extrahované informácie, často vo vektorovej databáze, aby sa dali neskôr vyhľadať.

4. **Rozšíriť budúce dopyty**: Keď používateľ začne nový dopyt, agent znalostí vyhľadá relevantné uložené informácie a vloží ich do výzvy používateľa, poskytujúc kľúčový kontext primárnemu agentovi (podobne ako RAG).

### Optimalizácie pre pamäť

• **Riadenie latencie**: Aby sa predišlo spomaleniu interakcií používateľa, najskôr sa môže použiť lacnejší, rýchlejší model na rýchlu kontrolu, či je informácia hodná uloženia alebo vyhľadania, a komplikovanejší proces extrakcie/získavania sa použije len v prípade potreby.

• **Údržba znalostnej bázy**: Pre rastúcu znalostnú bázu môžu byť menej často používané informácie presunuté do "studeného úložiska" na zníženie nákladov.

## Máte viac otázok o pamäti agentov?

Pridajte sa na [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kde sa stretnete s ďalšími študentmi, zúčastníte sa konzultačných hodín a získate odpovede na vaše otázky o AI agentoch.
## Predchádzajúca lekcia

[Context Engineering for AI Agents](../12-context-engineering/README.md)

## Ďalšia lekcia

[Exploring Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->