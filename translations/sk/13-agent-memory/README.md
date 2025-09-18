<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1923cf93aba522a5f4a493597112a893",
  "translation_date": "2025-09-18T16:21:09+00:00",
  "source_file": "13-agent-memory/README.md",
  "language_code": "sk"
}
-->
# Pamäť pre AI agentov

Pri diskusii o jedinečných výhodách vytvárania AI agentov sa najčastejšie spomínajú dve veci: schopnosť používať nástroje na dokončenie úloh a schopnosť zlepšovať sa v priebehu času. Pamäť je základom pre vytvorenie samostatne sa zlepšujúceho agenta, ktorý dokáže poskytovať lepšie zážitky pre našich používateľov.

V tejto lekcii sa pozrieme na to, čo je pamäť pre AI agentov, ako ju môžeme spravovať a využívať na prospech našich aplikácií.

## Úvod

Táto lekcia pokrýva:

• **Porozumenie pamäti AI agenta**: Čo je pamäť a prečo je pre agentov nevyhnutná.

• **Implementácia a ukladanie pamäte**: Praktické metódy na pridanie pamäťových schopností do vašich AI agentov, so zameraním na krátkodobú a dlhodobú pamäť.

• **Vytváranie samostatne sa zlepšujúcich AI agentov**: Ako pamäť umožňuje agentom učiť sa z minulých interakcií a zlepšovať sa v priebehu času.

## Ciele učenia

Po dokončení tejto lekcie budete vedieť:

• **Rozlíšiť rôzne typy pamäte AI agenta**, vrátane pracovnej, krátkodobej a dlhodobej pamäte, ako aj špecializovaných foriem, ako sú pamäť osobnosti a epizodická pamäť.

• **Implementovať a spravovať krátkodobú a dlhodobú pamäť pre AI agentov** pomocou rámca Semantic Kernel, využívať nástroje ako Mem0 a Whiteboard memory a integrovať ich s Azure AI Search.

• **Porozumieť princípom samostatne sa zlepšujúcich AI agentov** a tomu, ako robustné systémy správy pamäte prispievajú k neustálemu učeniu a adaptácii.

## Porozumenie pamäti AI agenta

V jadre **pamäť AI agenta odkazuje na mechanizmy, ktoré mu umožňujú uchovávať a vybavovať informácie**. Tieto informácie môžu zahŕňať konkrétne detaily o konverzácii, preferencie používateľa, minulé akcie alebo dokonca naučené vzory.

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

Predstavte si ju ako kúsok poznámkového papiera, ktorý agent používa počas jednej úlohy alebo myšlienkového procesu. Uchováva okamžité informácie potrebné na výpočet ďalšieho kroku.

Pre AI agentov pracovná pamäť často zachytáva najrelevantnejšie informácie z konverzácie, aj keď je celá história chatu dlhá alebo skrátená. Zameriava sa na extrakciu kľúčových prvkov, ako sú požiadavky, návrhy, rozhodnutia a akcie.

**Príklad pracovnej pamäte**

V prípade agenta na rezerváciu cestovania môže pracovná pamäť zachytiť aktuálnu požiadavku používateľa, napríklad "Chcem si rezervovať výlet do Paríža". Táto konkrétna požiadavka je držaná v okamžitom kontexte agenta na usmernenie aktuálnej interakcie.

#### Krátkodobá pamäť

Tento typ pamäte uchováva informácie počas jednej konverzácie alebo relácie. Je to kontext aktuálneho chatu, ktorý umožňuje agentovi odkazovať na predchádzajúce kroky v dialógu.

**Príklad krátkodobej pamäte**

Ak sa používateľ opýta: "Koľko by stál let do Paríža?" a potom pokračuje: "A čo ubytovanie tam?", krátkodobá pamäť zabezpečí, že agent vie, že "tam" odkazuje na "Paríž" v rámci tej istej konverzácie.

#### Dlhodobá pamäť

Toto sú informácie, ktoré pretrvávajú naprieč viacerými konverzáciami alebo reláciami. Umožňuje agentom pamätať si preferencie používateľa, historické interakcie alebo všeobecné znalosti počas dlhších období. To je dôležité pre personalizáciu.

**Príklad dlhodobej pamäte**

Dlhodobá pamäť môže uchovávať informácie ako "Ben má rád lyžovanie a outdoorové aktivity, obľubuje kávu s výhľadom na hory a chce sa vyhnúť pokročilým lyžiarskym svahom kvôli minulému zraneniu". Tieto informácie, naučené z predchádzajúcich interakcií, ovplyvňujú odporúčania v budúcich plánovacích reláciách, čím sú vysoko personalizované.

#### Pamäť osobnosti

Tento špecializovaný typ pamäte pomáha agentovi vyvinúť konzistentnú "osobnosť" alebo "personu". Umožňuje agentovi pamätať si detaily o sebe alebo svojej zamýšľanej úlohe, čím sú interakcie plynulejšie a zameranejšie.

**Príklad pamäte osobnosti**

Ak je cestovný agent navrhnutý ako "expert na plánovanie lyžiarskych výletov", pamäť osobnosti môže posilniť túto úlohu, čím ovplyvňuje jeho odpovede tak, aby zodpovedali tónu a znalostiam experta.

#### Epizodická pamäť

Táto pamäť uchováva sekvenciu krokov, ktoré agent vykonáva počas komplexnej úlohy, vrátane úspechov a zlyhaní. Je to ako pamätať si konkrétne "epizódy" alebo minulé skúsenosti, aby sa z nich poučil.

**Príklad epizodickej pamäte**

Ak sa agent pokúsil rezervovať konkrétny let, ale zlyhal kvôli nedostupnosti, epizodická pamäť môže zaznamenať toto zlyhanie, čo umožní agentovi skúsiť alternatívne lety alebo informovať používateľa o probléme informovanejším spôsobom pri ďalšom pokuse.

#### Pamäť entít

Táto pamäť zahŕňa extrakciu a zapamätanie si konkrétnych entít (ako sú osoby, miesta alebo veci) a udalostí z konverzácií. Umožňuje agentovi vytvoriť štruktúrované pochopenie kľúčových prvkov, o ktorých sa diskutovalo.

**Príklad pamäte entít**

Z konverzácie o minulom výlete môže agent extrahovať "Paríž", "Eiffelova veža" a "večera v reštaurácii Le Chat Noir" ako entity. Pri budúcej interakcii si agent môže vybaviť "Le Chat Noir" a ponúknuť rezerváciu tam.

#### Štruktúrovaný RAG (Retrieval Augmented Generation)

Aj keď je RAG širšou technikou, "Štruktúrovaný RAG" je zdôraznený ako výkonná pamäťová technológia. Extrahuje husté, štruktúrované informácie z rôznych zdrojov (konverzácie, e-maily, obrázky) a používa ich na zlepšenie presnosti, vybavenia a rýchlosti odpovedí. Na rozdiel od klasického RAG, ktorý sa spolieha výlučne na sémantickú podobnosť, Štruktúrovaný RAG pracuje so vnútornou štruktúrou informácií.

**Príklad štruktúrovaného RAG**

Namiesto jednoduchého porovnávania kľúčových slov by Štruktúrovaný RAG mohol analyzovať detaily letu (destinácia, dátum, čas, letecká spoločnosť) z e-mailu a uložiť ich štruktúrovaným spôsobom. To umožňuje presné dotazy, ako napríklad "Aký let som si rezervoval do Paríža na utorok?"

## Implementácia a ukladanie pamäte

Implementácia pamäte pre AI agentov zahŕňa systematický proces **správy pamäte**, ktorý zahŕňa generovanie, ukladanie, vybavovanie, integráciu, aktualizáciu a dokonca "zabúdanie" (alebo mazanie) informácií. Vybavovanie je obzvlášť dôležitý aspekt.

### Špecializované nástroje pamäte

Jedným zo spôsobov, ako ukladať a spravovať pamäť agenta, je použitie špecializovaných nástrojov, ako je Mem0. Mem0 funguje ako vrstva trvalej pamäte, ktorá umožňuje agentom vybaviť si relevantné interakcie, ukladať preferencie používateľa a faktický kontext a učiť sa z úspechov a zlyhaní v priebehu času. Myšlienka je, že bezstavové agenti sa menia na stavové.

Funguje prostredníctvom **dvojfázového pamäťového procesu: extrakcia a aktualizácia**. Najprv sa správy pridané do vlákna agenta posielajú do služby Mem0, ktorá používa veľký jazykový model (LLM) na sumarizáciu histórie konverzácie a extrakciu nových pamätí. Následne fáza aktualizácie riadená LLM určuje, či tieto pamäte pridať, upraviť alebo vymazať, pričom ich ukladá do hybridného dátového úložiska, ktoré môže zahŕňať vektorové, grafové a kľúčovo-hodnotové databázy. Tento systém tiež podporuje rôzne typy pamäte a môže integrovať grafovú pamäť na správu vzťahov medzi entitami.

### Ukladanie pamäte pomocou RAG

Okrem špecializovaných nástrojov pamäte, ako je Mem0, môžete využiť robustné vyhľadávacie služby, ako je **Azure AI Search ako backend na ukladanie a vybavovanie pamätí**, najmä pre štruktúrovaný RAG.

To umožňuje zakotviť odpovede agenta vo vašich vlastných údajoch, čím sa zabezpečia relevantnejšie a presnejšie odpovede. Azure AI Search môže byť použitý na ukladanie používateľských cestovných pamätí, katalógov produktov alebo akýchkoľvek iných znalostí špecifických pre danú oblasť.

Azure AI Search podporuje schopnosti ako **Štruktúrovaný RAG**, ktorý vyniká pri extrakcii a vybavovaní hustých, štruktúrovaných informácií z veľkých datasetov, ako sú histórie konverzácií, e-maily alebo dokonca obrázky. To poskytuje "nadľudskú presnosť a vybavenie" v porovnaní s tradičnými prístupmi k textovému rozdeľovaniu a vkladaniu.

## Vytváranie samostatne sa zlepšujúcich AI agentov

Bežný vzor pre samostatne sa zlepšujúcich agentov zahŕňa zavedenie **"agenta znalostí"**. Tento samostatný agent pozoruje hlavnú konverzáciu medzi používateľom a primárnym agentom. Jeho úlohou je:

1. **Identifikovať hodnotné informácie**: Určiť, či je niektorá časť konverzácie hodná uloženia ako všeobecná znalosť alebo konkrétna preferencia používateľa.

2. **Extrahovať a sumarizovať**: Destilovať podstatné učenie alebo preferenciu z konverzácie.

3. **Uložiť do znalostnej databázy**: Uchovať tieto extrahované informácie, často vo vektorovej databáze, aby ich bolo možné neskôr vybaviť.

4. **Rozšíriť budúce dotazy**: Keď používateľ iniciuje nový dotaz, agent znalostí vybaví relevantné uložené informácie a pridá ich do používateľského promptu, čím poskytne dôležitý kontext primárnemu agentovi (podobne ako RAG).

### Optimalizácie pre pamäť

• **Správa latencie**: Aby sa zabránilo spomaleniu interakcií používateľa, môže sa najskôr použiť lacnejší, rýchlejší model na rýchle overenie, či je informácia hodná uloženia alebo vybavenia, pričom zložitejší proces extrakcie/vybavenia sa spustí iba v prípade potreby.

• **Údržba znalostnej databázy**: Pre rastúcu znalostnú databázu môžu byť menej často používané informácie presunuté do "studeného úložiska" na správu nákladov.

## Máte ďalšie otázky o inžinierstve kontextu?

Pripojte sa k [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), kde sa môžete stretnúť s ďalšími študentmi, zúčastniť sa konzultačných hodín a získať odpovede na vaše otázky o AI agentoch.

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.