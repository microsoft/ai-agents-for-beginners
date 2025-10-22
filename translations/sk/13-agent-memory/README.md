<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d2c9703548140bafa2d6a77406552542",
  "translation_date": "2025-10-03T15:03:22+00:00",
  "source_file": "13-agent-memory/README.md",
  "language_code": "sk"
}
-->
# Pamäť pre AI agentov
[![Pamäť agenta](../../../translated_images/lesson-13-thumbnail.959e3bc52d210c64a614a3bece6b170a2c472138dc0a14c7fbde07306ef95ae7.sk.png)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Pri diskusii o jedinečných výhodách vytvárania AI agentov sa najčastejšie spomínajú dve veci: schopnosť využívať nástroje na dokončenie úloh a schopnosť zlepšovať sa v priebehu času. Pamäť je základom pre vytvorenie samostatne sa zlepšujúceho agenta, ktorý dokáže poskytovať lepšie zážitky pre našich používateľov.

V tejto lekcii sa pozrieme na to, čo je pamäť pre AI agentov, ako ju môžeme spravovať a využívať na zlepšenie našich aplikácií.

## Úvod

Táto lekcia pokryje:

• **Porozumenie pamäti AI agenta**: Čo je pamäť a prečo je pre agentov nevyhnutná.

• **Implementácia a ukladanie pamäte**: Praktické metódy na pridanie pamäťových schopností do vašich AI agentov, so zameraním na krátkodobú a dlhodobú pamäť.

• **Vytváranie samostatne sa zlepšujúcich AI agentov**: Ako pamäť umožňuje agentom učiť sa z minulých interakcií a zlepšovať sa v priebehu času.

## Ciele učenia

Po absolvovaní tejto lekcie budete vedieť:

• **Rozlíšiť rôzne typy pamäte AI agenta**, vrátane pracovnej, krátkodobej a dlhodobej pamäte, ako aj špecializovaných foriem, ako sú pamäť osobnosti a epizodická pamäť.

• **Implementovať a spravovať krátkodobú a dlhodobú pamäť pre AI agentov** pomocou rámca Semantic Kernel, využívať nástroje ako Mem0 a Whiteboard memory a integrovať ich s Azure AI Search.

• **Porozumieť princípom samostatne sa zlepšujúcich AI agentov** a tomu, ako robustné systémy správy pamäte prispievajú k neustálemu učeniu a adaptácii.

## Porozumenie pamäti AI agenta

V jadre **pamäť AI agenta odkazuje na mechanizmy, ktoré mu umožňujú uchovávať a vybavovať si informácie**. Tieto informácie môžu zahŕňať konkrétne detaily o konverzácii, preferencie používateľa, minulé akcie alebo dokonca naučené vzory.

Bez pamäte sú AI aplikácie často bezstavové, čo znamená, že každá interakcia začína od nuly. To vedie k opakovanému a frustrujúcemu používateľskému zážitku, kde agent "zabúda" predchádzajúci kontext alebo preferencie.

### Prečo je pamäť dôležitá?

Inteligencia agenta je úzko spojená s jeho schopnosťou vybaviť si a využívať minulé informácie. Pamäť umožňuje agentom byť:

• **Reflexívni**: Učiť sa z minulých akcií a výsledkov.

• **Interaktívni**: Udržiavať kontext počas prebiehajúcej konverzácie.

• **Proaktívni a reaktívni**: Predvídať potreby alebo reagovať vhodne na základe historických údajov.

• **Autonómni**: Fungovať nezávislejšie vďaka využívaniu uložených znalostí.

Cieľom implementácie pamäte je urobiť agentov **spoľahlivejšími a schopnejšími**.

### Typy pamäte

#### Pracovná pamäť

Predstavte si ju ako kúsok poznámkového papiera, ktorý agent používa počas jednej prebiehajúcej úlohy alebo myšlienkového procesu. Uchováva okamžité informácie potrebné na výpočet ďalšieho kroku.

Pre AI agentov pracovná pamäť často zachytáva najrelevantnejšie informácie z konverzácie, aj keď je celá história chatu dlhá alebo skrátená. Zameriava sa na extrahovanie kľúčových prvkov, ako sú požiadavky, návrhy, rozhodnutia a akcie.

**Príklad pracovnej pamäte**

V prípade agenta na rezerváciu cestovania môže pracovná pamäť zachytiť aktuálnu požiadavku používateľa, napríklad "Chcem si rezervovať výlet do Paríža". Táto konkrétna požiadavka je držaná v bezprostrednom kontexte agenta na vedenie aktuálnej interakcie.

#### Krátkodobá pamäť

Tento typ pamäte uchováva informácie počas jednej konverzácie alebo relácie. Je to kontext aktuálneho chatu, ktorý umožňuje agentovi odkazovať na predchádzajúce kroky v dialógu.

**Príklad krátkodobej pamäte**

Ak sa používateľ opýta: "Koľko by stál let do Paríža?" a potom pokračuje: "A čo ubytovanie tam?", krátkodobá pamäť zabezpečí, že agent vie, že "tam" odkazuje na "Paríž" v rámci tej istej konverzácie.

#### Dlhodobá pamäť

Toto sú informácie, ktoré pretrvávajú naprieč viacerými konverzáciami alebo reláciami. Umožňuje agentom pamätať si preferencie používateľa, historické interakcie alebo všeobecné znalosti počas dlhších období. To je dôležité pre personalizáciu.

**Príklad dlhodobej pamäte**

Dlhodobá pamäť môže uchovávať informácie ako "Ben má rád lyžovanie a outdoorové aktivity, obľubuje kávu s výhľadom na hory a chce sa vyhnúť pokročilým lyžiarskym svahom kvôli minulému zraneniu". Tieto informácie, naučené z predchádzajúcich interakcií, ovplyvňujú odporúčania v budúcich plánovacích reláciách, čím sú vysoko personalizované.

#### Pamäť osobnosti

Tento špecializovaný typ pamäte pomáha agentovi rozvíjať konzistentnú "osobnosť" alebo "personu". Umožňuje agentovi pamätať si detaily o sebe alebo svojej zamýšľanej úlohe, čím sú interakcie plynulejšie a zameranejšie.

**Príklad pamäte osobnosti**

Ak je cestovný agent navrhnutý ako "expert na plánovanie lyžovačiek", pamäť osobnosti môže posilniť túto úlohu, ovplyvňujúc jeho odpovede tak, aby zodpovedali tónu a znalostiam experta.

#### Pamäť pracovného toku/epizodická pamäť

Táto pamäť uchováva sekvenciu krokov, ktoré agent vykonáva počas komplexnej úlohy, vrátane úspechov a neúspechov. Je to ako pamätať si konkrétne "epizódy" alebo minulé skúsenosti na učenie sa z nich.

**Príklad epizodickej pamäte**

Ak sa agent pokúsil rezervovať konkrétny let, ale neúspešne kvôli nedostupnosti, epizodická pamäť môže zaznamenať tento neúspech, čo umožní agentovi skúsiť alternatívne lety alebo informovať používateľa o probléme informovanejším spôsobom pri ďalšom pokuse.

#### Pamäť entít

Táto pamäť zahŕňa extrahovanie a zapamätanie si konkrétnych entít (ako sú osoby, miesta alebo veci) a udalostí z konverzácií. Umožňuje agentovi vytvoriť štruktúrované pochopenie kľúčových prvkov, o ktorých sa diskutovalo.

**Príklad pamäte entít**

Z konverzácie o minulom výlete môže agent extrahovať "Paríž", "Eiffelova veža" a "večera v reštaurácii Le Chat Noir" ako entity. Pri budúcej interakcii by si agent mohol spomenúť na "Le Chat Noir" a ponúknuť rezerváciu tam.

#### Štruktúrovaný RAG (Retrieval Augmented Generation)

Aj keď je RAG širšou technikou, "Štruktúrovaný RAG" je zdôraznený ako výkonná pamäťová technológia. Extrahuje husté, štruktúrované informácie z rôznych zdrojov (konverzácie, e-maily, obrázky) a používa ich na zlepšenie presnosti, vybavenia a rýchlosti odpovedí. Na rozdiel od klasického RAG, ktorý sa spolieha výlučne na sémantickú podobnosť, Štruktúrovaný RAG pracuje so vnútornou štruktúrou informácií.

**Príklad štruktúrovaného RAG**

Namiesto jednoduchého porovnávania kľúčových slov by Štruktúrovaný RAG mohol analyzovať detaily letu (destinácia, dátum, čas, letecká spoločnosť) z e-mailu a uložiť ich štruktúrovaným spôsobom. To umožňuje presné dotazy, ako napríklad "Aký let som si rezervoval do Paríža na utorok?"

## Implementácia a ukladanie pamäte

Implementácia pamäte pre AI agentov zahŕňa systematický proces **správy pamäte**, ktorý zahŕňa generovanie, ukladanie, vyhľadávanie, integráciu, aktualizáciu a dokonca "zabúdanie" (alebo mazanie) informácií. Vyhľadávanie je obzvlášť dôležitý aspekt.

### Špecializované nástroje pamäte

Jedným zo spôsobov, ako ukladať a spravovať pamäť agenta, je použitie špecializovaných nástrojov, ako je Mem0. Mem0 funguje ako vrstva trvalej pamäte, ktorá umožňuje agentom vybaviť si relevantné interakcie, ukladať preferencie používateľa a faktický kontext a učiť sa z úspechov a neúspechov v priebehu času. Myšlienka je, že bezstavové agenti sa menia na stavové.

Funguje prostredníctvom **dvojfázového pamäťového procesu: extrakcia a aktualizácia**. Najprv sa správy pridané do vlákna agenta posielajú do služby Mem0, ktorá používa veľký jazykový model (LLM) na zhrnutie histórie konverzácie a extrakciu nových pamätí. Následne fáza aktualizácie riadená LLM určuje, či tieto pamäte pridať, upraviť alebo vymazať, pričom ich ukladá do hybridného dátového úložiska, ktoré môže zahŕňať vektorové, grafové a kľúčovo-hodnotové databázy. Tento systém tiež podporuje rôzne typy pamäte a môže zahŕňať grafovú pamäť na správu vzťahov medzi entitami.

### Ukladanie pamäte pomocou RAG

Okrem špecializovaných nástrojov pamäte, ako je Mem0, môžete využiť robustné vyhľadávacie služby, ako je **Azure AI Search ako backend na ukladanie a vyhľadávanie pamätí**, najmä pre štruktúrovaný RAG.

To umožňuje zakotviť odpovede agenta vo vašich vlastných údajoch, čím sa zabezpečia relevantnejšie a presnejšie odpovede. Azure AI Search môže byť použitý na ukladanie používateľských cestovných pamätí, katalógov produktov alebo akýchkoľvek iných znalostí špecifických pre danú oblasť.

Azure AI Search podporuje funkcie ako **Štruktúrovaný RAG**, ktorý vyniká pri extrakcii a vyhľadávaní hustých, štruktúrovaných informácií z veľkých datasetov, ako sú histórie konverzácií, e-maily alebo dokonca obrázky. To poskytuje "nadľudskú presnosť a vybavenie" v porovnaní s tradičnými prístupmi k textovému rozdeleniu a vkladaniu.

## Vytváranie samostatne sa zlepšujúcich AI agentov

Bežný vzor pre samostatne sa zlepšujúcich agentov zahŕňa zavedenie **"agenta znalostí"**. Tento samostatný agent pozoruje hlavnú konverzáciu medzi používateľom a primárnym agentom. Jeho úlohou je:

1. **Identifikovať hodnotné informácie**: Určiť, či je niektorá časť konverzácie hodná uloženia ako všeobecné znalosti alebo konkrétna preferencia používateľa.

2. **Extrahovať a zhrnúť**: Destilovať podstatné učenie alebo preferenciu z konverzácie.

3. **Uložiť do znalostnej databázy**: Uchovať tieto extrahované informácie, často vo vektorovej databáze, aby ich bolo možné neskôr vyhľadať.

4. **Rozšíriť budúce dotazy**: Keď používateľ iniciuje nový dotaz, agent znalostí vyhľadá relevantné uložené informácie a pridá ich do používateľského promptu, čím poskytne dôležitý kontext primárnemu agentovi (podobne ako RAG).

### Optimalizácie pre pamäť

• **Správa latencie**: Aby sa zabránilo spomaleniu interakcií používateľa, môže sa najskôr použiť lacnejší a rýchlejší model na rýchle overenie, či je informácia hodná uloženia alebo vyhľadania, pričom komplexnejší proces extrakcie/vyhľadávania sa spustí iba v prípade potreby.

• **Údržba znalostnej databázy**: Pre rastúcu znalostnú databázu môžu byť menej často používané informácie presunuté do "studeného úložiska" na správu nákladov.

## Máte ďalšie otázky o pamäti agenta?

Pripojte sa k [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), kde sa môžete stretnúť s ďalšími študentmi, zúčastniť sa konzultačných hodín a získať odpovede na vaše otázky o AI agentoch.

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.