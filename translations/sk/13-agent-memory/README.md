# Pamäť pre AI agentov 
[![Agent Memory](../../../translated_images/sk/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Pri diskusii o jedinečných výhodách vytvárania AI agentov sa väčšinou hovorí o dvoch veciach: schopnosti volať nástroje na dokončenie úloh a schopnosti zlepšovať sa v priebehu času. Pamäť je základom pre vytvorenie sebazlepšujúceho sa agenta, ktorý dokáže vytvárať lepšie zážitky pre našich používateľov.

V tejto lekcii sa pozrieme na to, čo je pamäť pre AI agentov a ako ju môžeme spravovať a využívať v prospech našich aplikácií.

## Úvod

Táto lekcia pokrýva:

• **Pochopenie pamäte AI agentov**: Čo je pamäť a prečo je pre agentov nevyhnutná.

• **Implementácia a ukladanie pamäte**: Praktické metódy pridávania pamäťových schopností do vašich AI agentov so zameraním na krátkodobú a dlhodobú pamäť.

• **Vytváranie sebazlepšujúcich sa AI agentov**: Ako pamäť umožňuje agentom učiť sa z minulých interakcií a zlepšovať sa v priebehu času.

## Dostupné implementácie

Táto lekcia obsahuje dva komplexné notebooky s tutoriálmi:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementuje pamäť pomocou Mem0 a Azure AI Search s Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementuje štruktúrovanú pamäť pomocou Cognee, ktorá automaticky vytvára znalostný graf podporený embeddingmi, vizualizuje graf a inteligentné vyhľadávanie

## Ciele učenia

Po absolvovaní tejto lekcie budete vedieť:

• **Rozlíšiť medzi rôznymi typmi pamäte AI agentov**, vrátane pracovnej, krátkodobej a dlhodobej pamäte, ako aj špecializovaných foriem ako persona a epizodická pamäť.

• **Implementovať a spravovať krátkodobú a dlhodobú pamäť pre AI agentov** pomocou Microsoft Agent Framework, využívajúc nástroje ako Mem0, Cognee, Whiteboard memory a integráciu so službou Azure AI Search.

• **Pochopiť zásady za sebazlepšujúcimi sa AI agentmi** a ako robustné systémy správy pamäte prispievajú k neustálemu učeniu sa a adaptácii.

## Pochopenie pamäte AI agentov

V jadre, **pamäť pre AI agentov odkazuje na mechanizmy, ktoré im umožňujú uchovávať a vybavovať si informácie**. Tieto informácie môžu byť konkrétne detaily o konverzácii, preferencie používateľa, minulé akcie alebo dokonca naučené vzory.

Bez pamäte sú AI aplikácie často bezstavové, čo znamená, že každá interakcia začína odznova. To vedie k opakujúcemu sa a frustrujúcemu používateľskému zážitku, kde agent "zabúda" predchádzajúci kontext alebo preferencie.

### Prečo je pamäť dôležitá?

inteligencia agenta je hlboko viazaná na jeho schopnosť pripomínať si a využívať minulé informácie. Pamäť umožňuje agentom byť:

• **Reflexívni**: Učiť sa z minulých akcií a výsledkov.

• **Interaktívni**: Udržiavať kontext počas prebiehajúcej konverzácie.

• **Proaktívni a reaktívni**: Predvídať potreby alebo primerane reagovať na základe historických dát.

• **Autonómni**: Fungovať viac nezávisle čerpaním zo uložených poznatkov.

Cieľom implementácie pamäte je urobiť agentov **spoľahlivejšími a schopnejšími**.

### Typy pamäte

#### Pracovná pamäť

Predstavte si to ako kus papiera, ktorý agent používa počas jednej prebiehajúcej úlohy alebo myšlienkového procesu. Obsahuje okamžité informácie potrebné na výpočet ďalšieho kroku.

Pre AI agentov pracovná pamäť často zachytáva najdôležitejšie informácie z konverzácie, aj keď je celá história rozhovoru dlhá alebo skrátená. Zameriava sa na vyťahovanie kľúčových prvkov ako požiadavky, návrhy, rozhodnutia a akcie.

**Príklad pracovnej pamäte**

V agenta na rezerváciu ciest by pracovná pamäť mohla zachytiť aktuálnu požiadavku používateľa, napríklad "Chcem rezervovať cestu do Paríža". Táto konkrétna požiadavka je uložená v bezprostrednom kontexte agenta na usmernenie aktuálnej interakcie.

#### Krátkodobá pamäť

Tento typ pamäte uchováva informácie počas jednej konverzácie alebo relácie. Je to kontext aktuálneho rozhovoru, čo umožňuje agentovi odkazovať späť na predchádzajúce kolá dialógu.

V ukážkach Python SDK [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) sa to mapuje na `AgentSession`, vytvorenú pomocou `agent.create_session()`. Relácia je vstavaná krátkodobá pamäť rámca: udržiava dostupný kontext konverzácie, kým je tá istá relácia používaná, ale tento kontext nie je uchovávaný po ukončení relácie alebo reštarte aplikácie. Pre fakty a preferencie, ktoré majú pretrvávať medzi reláciami, použite dlhodobú pamäť, zvyčajne cez databázu, vektorový index alebo iný trvalý úložisko.

**Príklad krátkodobej pamäte**

Ak používateľ položí otázku "Koľko by stál let do Paríža?" a následne sa opýta "A čo ubytovanie tam?", krátkodobá pamäť zabezpečí, že agent vie, že "tam" odkazuje na "Paríž" v rámci toho istého rozhovoru.

#### Dlhodobá pamäť

Ide o informácie, ktoré pretrvávajú počas viacerých rozhovorov alebo relácií. Umožňuje agentom pamätať si preferencie používateľa, historické interakcie alebo všeobecné znalosti počas dlhších období. Je to dôležité pre personalizáciu.

**Príklad dlhodobej pamäte**

Dlhodobá pamäť môže uložiť, že "Ben má rád lyžovanie a aktivity v prírode, rád pije kávu s výhľadom na hory a chce sa vyhnúť pokročilým zjazdovkám kvôli minulému zraneniu". Tieto informácie, získané z predchádzajúcich interakcií, ovplyvňujú odporúčania v budúcich plánovacích reláciách ciest, čím ich robia vysoko personalizované.

#### Persona pamäť

Tento špecializovaný typ pamäte pomáha agentovi vyvinúť konzistentnú "osobnosť" alebo "personu". Umožňuje agentovi pamätať si detaily o sebe alebo svojej zamýšľanej úlohe, čím zlepšuje plynulosť a zameranie interakcií.

**Príklad persona pamäte**
Ak je agent na cestovanie navrhnutý ako "expert na plánovanie lyžovania", persona pamäť môže túto rolu zosilniť a ovplyvniť odpovede tak, aby zodpovedali tónu a znalostiam experta.

#### Pracovný postup / Epizodická pamäť

Táto pamäť ukladá postupnosť krokov, ktoré agent vykonáva počas zložitej úlohy, vrátane úspechov a zlyhaní. Je to ako spomínanie na konkrétne "epizódy" alebo minulé skúsenosti s cieľom poučiť sa z nich.

**Príklad epizodickej pamäte**

Ak sa agent pokúsil rezervovať konkrétny let, ale zlyhal kvôli nedostupnosti, epizodická pamäť by túto nevydarenú akciu zaznamenala, čo umožní agentovi skúsiť alternatívne lety alebo informovať používateľa o probléme lepšie informovaným spôsobom pri následnom pokuse.

#### Entitná pamäť

Táto pamäť zahŕňa vyťahovanie a zapamätanie si konkrétnych entít (ako ľudia, miesta alebo objekty) a udalostí z konverzácií. Umožňuje agentovi vytvoriť štruktúrované pochopenie kľúčových prvkov diskutovaných tém.

**Príklad entitnej pamäte**

Z konverzácie o minulom výlete môže agent vyťažiť entity ako "Paríž", "Eiffelova veža" a "večera v reštaurácii Le Chat Noir". V budúcej interakcii by si agent mohol spomenúť na "Le Chat Noir" a ponúknuť novú rezerváciu tam.

#### Štruktúrovaný RAG (Retrieval Augmented Generation)

Kým RAG je širšia technika, "Štruktúrovaný RAG" je zdôraznený ako silná pamäťová technológia. Vyťahuje husté, štruktúrované informácie z rôznych zdrojov (rozhovory, e-maily, obrázky) a využíva ich na zvýšenie presnosti, vyhľadávania a rýchlosti odpovedí. Na rozdiel od klasického RAG, ktorý sa spolieha len na sémantickú podobnosť, Štruktúrovaný RAG pracuje s inherentnou štruktúrou informácií.

**Príklad štruktúrovaného RAG**

Namiesto iba zhodovania kľúčových slov by Štruktúrovaný RAG mohol rozparsovať detaily letu (cieľ, dátum, čas, letecká spoločnosť) z e-mailu a uložiť ich štruktúrovane. To umožňuje presné dotazy ako "Aký let som si rezervoval do Paríža v utorok?"

## Implementácia a ukladanie pamäte

Implementácia pamäte pre AI agentov zahŕňa systematický proces **správy pamäte**, ktorý zahŕňa generovanie, ukladanie, vyhľadávanie, integráciu, aktualizáciu a dokonca "zabúdanie" (alebo mazanie) informácií. Vyhľadávanie je obzvlášť kľúčovým aspektom.

### Špecializované pamäťové nástroje

#### Mem0

Jedným zo spôsobov, ako ukladať a spravovať pamäť agentov, je použitie špecializovaných nástrojov ako Mem0. Mem0 funguje ako trvalá pamäťová vrstva, ktorá umožňuje agentom vybavovať si relevantné interakcie, ukladať používateľské preferencie a faktický kontext a učiť sa z úspechov a neúspechov v priebehu času. Myšlienka je, že bezstavoví agenti sa menia na stavových.

Funguje cez **dvojfázový pamäťový proces: extrakcia a aktualizácia**. Najprv správy pridané do vlákna agenta sú odoslané do služby Mem0, ktorá využíva veľký jazykový model (LLM) na sumarizáciu histórie konverzácie a extrakciu nových spomienok. Následne fáza aktualizácie riadená LLM rozhodne, či sa tieto spomienky pridajú, upravia alebo vymažú, pričom sú uložené v hybridnom dátovom úložisku, ktoré môže obsahovať vektorové, grafové a kľúč-hodnota databázy. Tento systém podporuje rôzne typy pamäte a môže začleňovať aj grafovú pamäť na správu vzťahov medzi entitami.

#### Cognee

Ďalším silným prístupom je použitie **Cognee**, open-source sémantickej pamäte pre AI agentov, ktorá transformuje štruktúrované a neštruktúrované údaje na dopytovateľné znalostné grafy podporené embeddingmi. Cognee poskytuje **dvojúrovňovú architektúru** kombinujúcu vyhľadávanie na základe vektorovej podobnosti s grafovými vzťahmi, čo agentom umožňuje chápať nielen podobnosť informácií, ale aj ich vzájomné prepojenie.

Vyniká v **hybridnom vyhľadávaní**, ktoré kombinuje vektorovú podobnosť, grafovú štruktúru a uvažovanie pomocou LLM - od vyhľadávania neštruktúrovaných častí po odpovedanie s ohľadom na graf. Systém udržiava **živú pamäť**, ktorá sa vyvíja a rastie, pričom zostáva dotazovateľná ako jeden prepojený graf a podporuje tak krátkodobý kontext relácie aj dlhodobú perzistentnú pamäť.

Notebookový tutoriál Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonštruje vytvorenie tejto jednotnej pamäťovej vrstvy s praktickými príkladmi ingestie rozmanitých dátových zdrojov, vizualizácie znalostného grafu a dopytovania s rôznymi vyhľadávacími stratégiami prispôsobenými konkrétnym potrebám agenta.

### Ukladanie pamäte pomocou RAG

Okrem špecializovaných pamäťových nástrojov ako Mem0 môžete využiť robustné vyhľadávacie služby ako **Azure AI Search ako backend na ukladanie a vyhľadávanie spomienok**, najmä pre štruktúrovaný RAG.

To vám umožní podložiť odpovede agenta vašimi vlastnými dátami, čím zabezpečíte relevantnejšie a presnejšie odpovede. Azure AI Search možno používať na ukladanie používateľských cestovných spomienok, produktových katalógov alebo iných doménovo špecifických znalostí.

Azure AI Search podporuje funkcie ako **Štruktúrovaný RAG**, ktorý exceluje vo vyťahovaní a vyhľadávaní hustých, štruktúrovaných informácií z veľkých datasetov ako histórie rozhovorov, e-mailov alebo dokonca obrázkov. To poskytuje "nadľudskú presnosť a vyhľadávanie" v porovnaní s tradičnými prístupmi členených textov a embeddingov.

## Ako urobiť AI agentov sebazlepšujúcimi

Bežný vzor pre sebazlepšujúcich sa agentov zahŕňa zavedenie **"poznatkovo" agenta**. Tento samostatný agent sleduje hlavný rozhovor medzi používateľom a primárnym agentom. Jeho úlohou je:

1. **Identifikovať cenné informácie**: Zistiť, či časť konverzácie stojí za uloženie ako všeobecné poznatky alebo špecifická používateľská preferencia.

2. **Extrahovať a zhrnúť**: Destilovať podstatné učenie alebo preferenciu z konverzácie.

3. **Uložiť do znalostnej databázy**: Trvalo uložiť tieto vyťažené informácie, často do vektorovej databázy, aby mohli byť neskôr vyhľadané.

4. **Rozšíriť budúce dopyty**: Keď používateľ začne nový dopyt, poznatkovo agent vyhľadá relevantné uložené informácie a pridá ich k zadaniu používateľa, poskytujúc tak dôležitý kontext primárnemu agentovi (podobne ako RAG).

### Optimalizácie pre pamäť

• **Manažment latencie**: Aby sa zabránilo spomaleniu používateľských interakcií, môže sa najskôr použiť lacnejší a rýchlejší model na rýchlu kontrolu, či sú informácie vhodné na uloženie alebo vyhľadanie, pričom komplexnejší proces extrakcie/vyhľadávania sa zavolá iba v prípade potreby.

• **Údržba znalostnej databázy**: Pre rastúcu znalostnú databázu sa menej často používané informácie môžu presunúť do "studeného úložiska" na kontrolu nákladov.

## Máte ďalšie otázky o pamäti agentov?

Pridajte sa do [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kde sa stretnete s ostatnými študentmi, môžete navštevovať úradné hodiny a dostať odpovede na vaše otázky o AI agentoch.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->