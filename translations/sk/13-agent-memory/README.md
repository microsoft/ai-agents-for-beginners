# Pamäť pre AI Agentov 
[![Agent Memory](../../../translated_images/sk/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Pri diskusii o jedinečných výhodách vytvárania AI agentov sa hlavne hovorí o dvoch veciach: schopnosti volať nástroje na dokončenie úloh a schopnosti zlepšovať sa v priebehu času. Pamäť je základom vytvorenia samo-sa zlepšujúceho sa agenta, ktorý môže vytvárať lepšie skúsenosti pre našich používateľov.

V tejto lekcii sa pozrieme na to, čo je pamäť pre AI agentov a ako ju môžeme spravovať a používať v prospech našich aplikácií.

## Úvod

Táto lekcia pokrýva:

• **Pochopenie pamäte AI agenta**: Čo je pamäť a prečo je pre agentov nevyhnutná.

• **Implementácia a ukladanie pamäte**: Praktické metódy pridávania pamäťových schopností vašim AI agentom, so zameraním na krátkodobú a dlhodobú pamäť.

• **Urobiť AI agentov samo-zlepšujúcimi sa**: Ako pamäť umožňuje agentom učiť sa z minulých interakcií a zlepšovať sa v priebehu času.

## Dostupné implementácie

Táto lekcia obsahuje dva komplexné notebookové tutoriály:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementuje pamäť pomocou Mem0 a Azure AI Search s Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementuje štruktúrovanú pamäť pomocou Cognee, automaticky vytvára znalostný graf podporovaný embeddingmi, vizualizuje graf a inteligentné vyhľadávanie

## Ciele učenia

Po dokončení tejto lekcie budete vedieť:

• **Rozlíšiť rôzne typy pamäte AI agenta**, vrátane pracovnej, krátkodobej a dlhodobej pamäte, ako aj špecializovaných typov ako persona a epizodická pamäť.

• **Implementovať a spravovať krátkodobú a dlhodobú pamäť pre AI agentov** pomocou Microsoft Agent Framework, využívajúc nástroje ako Mem0, Cognee, Whiteboard pamäť a integráciu s Azure AI Search.

• **Pochopiť princípy za samo-zlepšujúcimi sa AI agentmi** a ako robustné systémy správy pamäte prispievajú k neustálemu učeniu a adaptácii.

## Pochopenie pamäte AI agenta

V jadre, **pamäť pre AI agentov znamená mechanizmy, ktoré im umožňujú uchovávať a vybavovať si informácie**. Tieto informácie môžu byť špecifické detaily o konverzácii, preferencie používateľa, minulé akcie alebo dokonca naučené vzory.

Bez pamäte sú AI aplikácie často bezstavové, čo znamená, že každá interakcia začína od znova. To vedie k opakujúcemu sa a frustrujúcemu používateľskému zážitku, kde agent "zabúda" predchádzajúci kontext alebo preferencie.

### Prečo je pamäť dôležitá?

Inteligencia agenta je hlboko viazaná na jeho schopnosť vybaviť si a využiť minulé informácie. Pamäť umožňuje agentom byť:

• **Reflexívni**: Učiť sa z minulých akcií a výsledkov.

• **Interaktívni**: Udržiavať kontext počas prebiehajúcej konverzácie.

• **Proaktívni a Reaktívni**: Predvídať potreby alebo primerane reagovať na základe historických dát.

• **Autonómni**: Pôsobia samostatnejšie tým, že čerpajú zo zaznamenaných znalostí.

Cieľom implementácie pamäte je urobiť agentov **spoľahlivejšími a schopnejšími**.

### Typy pamäti

#### Pracovná pamäť

Predstavte si to ako kus škrabacieho papiera, ktorý agent používa počas jednej prebiehajúcej úlohy alebo procesu myslenia. Uchováva okamžité informácie potrebné na vypočítanie ďalšieho kroku.

Pre AI agentov pracovná pamäť často zachytáva najrelevantnejšie informácie z konverzácie, aj keď je celý chat dlhý alebo skrátený. Zameriava sa na extrakciu kľúčových prvkov ako požiadavky, návrhy, rozhodnutia a akcie.

**Príklad pracovnej pamäte**

V agentovi na rezerváciu ciest môže pracovná pamäť zachytiť aktuálnu požiadavku používateľa, napríklad "Chcem si rezervovať výlet do Paríža". Táto konkrétna požiadavka je držaná v bezprostrednom kontexte agenta, aby riadila aktuálnu interakciu.

#### Krátkodobá pamäť

Tento typ pamäte uchováva informácie počas jednej konverzácie alebo relácie. Je to kontext aktuálneho chatu, ktorý agentovi umožňuje odkazovať späť na predchádzajúce kolá dialógu.

V ukážkach Python SDK [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) sa to mapuje na `AgentSession`, vytvorenú pomocou `agent.create_session()`. Session je vstavaná krátkodobá pamäť rámca: udržiava kontext konverzácie dostupný, kým sa táto istá session znova používa, ale kontext sa neuchováva, keď session skončí alebo sa aplikácia reštartuje. Na fakty a preferencie, ktoré musia prežiť cez viaceré session, používajte dlhodobú pamäť, obvykle cez databázu, vektorový index alebo iný trvalý úložný priestor.

**Príklad krátkodobej pamäte**

Ak používateľ spýta "Koľko by stál let do Paríža?" a neskôr "A čo ubytovanie tam?", krátkodobá pamäť zabezpečí, že agent vie, že "tam" odkazuje na "Paríž" v tej istej konverzácii.

#### Dlhodobá pamäť

Ide o informácie, ktoré pretrvávajú cez viacero konverzácií alebo relácií. Umožňuje agentom pamätať si používateľské preferencie, historické interakcie alebo všeobecné znalosti počas dlhšieho obdobia. To je dôležité pre personalizáciu.

**Príklad dlhodobej pamäte**

Dlhodobá pamäť môže uložiť, že "Ben má rád lyžovanie a vonkajšie aktivity, obľubuje kávu s výhľadom na hory a chce sa vyhnúť pokročilým lyžiarskym zjazdovkám kvôli minulému zraneniu". Tieto informácie, naučené z predchádzajúcich interakcií, ovplyvňujú odporúčania v budúcich plánovacích cestovateľských reláciách a robia ich veľmi personalizované.

#### Persona pamäť

Tento špecializovaný typ pamäte pomáha agentovi vyvinúť konzistentnú "osobnosť" alebo "personu". Umožňuje agentovi pamätať si detaily o sebe alebo o svojej zamýšľanej úlohe, čím robí interakcie plynulejšími a zameranými.

**Príklad persona pamäte**  
Ak je cestovný agent navrhnutý ako "expert na plánovanie lyžovačky", persona pamäť môže tento rolový aspekt posilniť, ovplyvňujúc jeho odpovede tak, aby zodpovedali tónu a znalostiam experta.

#### Workflow/Epizodická pamäť

Táto pamäť uchováva sekvenciu krokov, ktoré agent vykonáva počas zložitej úlohy, vrátane úspechov a neúspechov. Je to ako pamätať si konkrétne "epizódy" alebo minulé skúsenosti, aby sa z nich agent mohol učiť.

**Príklad epizodickej pamäte**

Ak sa agent pokúsil rezervovať konkrétny let, ale neúspešne kvôli nedostupnosti, epizodická pamäť môže zaznamenať tento neúspech, čo umožní agentovi skúsiť alternatívne lety alebo informovať používateľa o probléme pri ďalšom pokuse informovanejším spôsobom.

#### Entity pamäť

Zahŕňa extrakciu a zapamätanie si konkrétnych entít (ako ľudia, miesta alebo veci) a udalostí z konverzácií. Umožňuje agentovi vybudovať štruktúrované pochopenie kľúčových prvkov, ktoré sa diskutovali.

**Príklad entity pamäte**

Z konverzácie o minulom výlete môže agent extrahovať entity ako "Paríž," "Eiffelova veža" a "večera v reštaurácii Le Chat Noir". Pri budúcej interakcii si agent pamätá "Le Chat Noir" a môže ponúknuť, že tam urobí novú rezerváciu.

#### Štruktúrovaný RAG (Retrieval Augmented Generation)

Kým RAG je širšia technika, "Štruktúrovaný RAG" je zdôraznený ako silná pamäťová technológia. Extrahuje husté, štruktúrované informácie z rôznych zdrojov (konverzácie, e-maily, obrázky) a využíva ich na zvýšenie presnosti, vybavenia a rýchlosti odpovedí. Na rozdiel od klasického RAG, ktorý sa spolieha len na sémantickú podobnosť, štruktúrovaný RAG pracuje s inherentnou štruktúrou informácií.

**Príklad štruktúrovaného RAG**

Namiesto iba zhodovania kľúčových slov by štruktúrovaný RAG mohol rozparsovať detaily letu (cieľ, dátum, čas, letecká spoločnosť) z e-mailu a uložiť ich štruktúrovane. To umožňuje presné otázky ako "Aký let som si rezervoval do Paríža na utorok?"

## Implementácia a ukladanie pamäte

Implementácia pamäte pre AI agentov zahŕňa systematický proces **správy pamäte**, ktorý zahŕňa generovanie, ukladanie, vyhľadávanie, integráciu, aktualizáciu a dokonca aj "zabúdanie" (alebo mazanie) informácií. Vyhľadávanie je obzvlášť kľúčovým aspektom.

### Špecializované pamäťové nástroje

#### Mem0

Jedným zo spôsobov, ako ukladať a spravovať agentovú pamäť, je použitie špecializovaných nástrojov ako Mem0. Mem0 funguje ako perzistentná pamäťová vrstva, ktorá agentom umožňuje vybavovať relevantné interakcie, ukladať používateľské preferencie a faktický kontext a učiť sa zo svojich úspechov i neúspechov v priebehu času. Myšlienka je, že bezstavoví agenti sa menia na stavových.

Funguje pomocou **dvojfázového pamäťového procesu: extrakcia a aktualizácia**. Najskôr správy pridané do agentovho vlákna sú odoslané do služby Mem0, ktorá používa veľký jazykový model (LLM) na zhrnutie histórie konverzácie a extrakciu nových spomienok. Následne fáza aktualizácie riadená LLM rozhoduje, či tieto spomienky pridať, modifikovať alebo vymazať, a ukladá ich do hybridného dátového úložiska, ktoré môže zahŕňať vektorové, grafové a kľúčovo-hodnotové databázy. Tento systém podporuje rôzne typy pamäte a môže začleniť aj grafovú pamäť na správu vzťahov medzi entitami.

#### Cognee

Ďalším silným prístupom je použitie **Cognee**, open-source sémantickej pamäte pre AI agentov, ktorá mení štruktúrované a neštruktúrované dáta na dotazovateľné znalostné grafy podporované embeddingmi. Cognee poskytuje **dvojité úložisko** kombinujúce vyhľadávanie podľa vektorovej podobnosti s grafovými vzťahmi, čo agentom umožňuje chápať nielen to, aké informácie sú podobné, ale aj ako sú koncepty navzájom prepojené.

Vyniká v **hybridnom vyhľadávaní**, ktoré kombinuje vektorovú podobnosť, štruktúru grafu a LLM dedukciu - od jednoduchého vyhľadávania v kúskach dát až po otázky zohľadňujúce graf. Systém udržiava **živú pamäť**, ktorá sa vyvíja a rastie, pričom zostáva dotazovateľná ako jeden prepojený graf, podporujúc krátkodobý kontext session aj dlhodobú perzistentnú pamäť.

Notebookový tutoriál Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) ukazuje budovanie tejto jednotnej pamäťovej vrstvy s praktickými príkladmi ingestovania rôznych dátových zdrojov, vizualizácie znalostného grafu a dotazovania s rôznymi vyhľadávacími stratégiami prispôsobenými potrebám konkrétneho agenta.

### Ukladanie pamäte pomocou RAG

Okrem špecializovaných pamäťových nástrojov ako Mem0, môžete využiť robustné vyhľadávacie služby ako **Azure AI Search ako backend na ukladanie a získavanie spomienok**, najmä pre štruktúrovaný RAG.

To vám umožní zakotviť odpovede agenta vo vašich vlastných dátach, čím sa zabezpečia relevantnejšie a presnejšie odpovede. Azure AI Search môže byť použitý na ukladanie špecifických cestovateľských spomienok používateľa, katalógov produktov alebo iných doménovo špecifických znalostí.

Azure AI Search podporuje schopnosti ako **Štruktúrovaný RAG**, ktorý exceluje vo vyťahovaní a vyhľadávaní hustých, štruktúrovaných informácií z rozsiahlych datasetov ako histórie konverzácií, e-mailov alebo dokonca obrázkov. To poskytuje "nadzemskú presnosť a vybavenie" v porovnaní s tradičnými prístupmi založenými na rozdelení textov a embeddingoch.

## Urobiť AI agentov samo-zlepšujúcimi sa

Bežný vzorec pre samo-zlepšujúcich sa agentov zahŕňa zavedenie **"vedomostného agenta"**. Tento samostatný agent sleduje hlavnú konverzáciu medzi používateľom a primárnym agentom. Jeho úlohou je:

1. **Identifikovať cenné informácie**: Určiť, či je časť konverzácie hodná uloženia ako všeobecné poznanie alebo špecifická používateľská preferencia.

2. **Extrahovať a zhrnúť**: Destilovať podstatné učenie alebo preferenciu z konverzácie.

3. **Uložiť do znalostnej databázy**: Trvalo uložiť tieto extrahované informácie, často do vektorovej databázy, aby boli neskôr prístupné.

4. **Doplniť budúce dopyty**: Keď používateľ iniciuje nový dopyt, vedomostný agent načíta relevantné uložené informácie a pripojí ich k používateľskému dopytu, poskytujúc kľúčový kontext primárnemu agentovi (podobne ako RAG).

### Optimalizácie pre pamäť

• **Riadenie latencie**: Aby sa predišlo spomaleniu interakcií s používateľom, môže sa najskôr použiť lacnejší a rýchlejší model na rýchlu kontrolu, či je informácia hodná uloženia alebo načítania, a zložitejší proces extrakcie/vyhľadávania sa spustí len v prípade potreby.

• **Údržba znalostnej bázy**: Pre rastúcu znalostnú bázu možno menej často využívané informácie presunúť do "studeného úložiska" na kontrolu nákladov.

## Máte ďalšie otázky o pamäti agenta?

Pridajte sa do [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), aby ste sa stretli s ďalšími študentmi, zúčastnili sa konzultačných hodín a získali odpovede na svoje otázky o AI agentoch.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->