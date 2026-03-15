# Pamäť pre AI agentov 
[![Pamäť agenta](../../../translated_images/sk/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Keď sa diskutuje o jedinečných výhodách vytvárania AI agentov, zvyčajne sa spomínajú dve veci: schopnosť volať nástroje na dokončenie úloh a schopnosť zlepšovať sa v priebehu času. Pamäť je základom vytvárania samovylepšujúcich sa agentov, ktorí dokážu poskytovať lepšie zážitky pre našich používateľov.

V tejto lekcii sa pozrieme na to, čo je pamäť pre AI agentov a ako ju môžeme spravovať a využívať v prospech našich aplikácií.

## Úvod

Táto lekcia pokryje:

• **Pochopenie pamäte AI agentov**: Čo je pamäť a prečo je pre agentov nevyhnutná.

• **Implementácia a ukladanie pamäte**: Praktické metódy pridávania pamäťových schopností vašim AI agentom, so zameraním na krátkodobú a dlhodobú pamäť.

• **Ako dať AI agentom schopnosť samovylepšovania**: Ako pamäť umožňuje agentom učiť sa z minulých interakcií a zlepšovať sa v priebehu času.

## Dostupné implementácie

Táto lekcia obsahuje dva komplexné notebookové tutoriály:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementuje pamäť pomocou Mem0 a Azure AI Search s Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementuje štruktúrovanú pamäť pomocou Cognee, automaticky buduje znalostný graf podporený embeddingmi, vizualizuje graf a inteligentné získavanie informácií

## Ciele učenia

Po dokončení tejto lekcie budete vedieť:

• **Rozlíšiť medzi rôznymi typmi pamäte AI agenta**, vrátane pracovnej, krátkodobej a dlhodobej pamäte, ako aj špecializovaných foriem ako pamäť osobnosti (persona) a epizodická pamäť.

• **Implementovať a spravovať krátkodobú a dlhodobú pamäť pre AI agentov** pomocou Microsoft Agent Framework, využívajúc nástroje ako Mem0, Cognee, Whiteboard memory a integráciu s Azure AI Search.

• **Pochopiť princípy za samovylepšujúcimi sa AI agentmi** a ako robustné systémy správy pamäte prispievajú k priebežnému učeniu a adaptácii.

## Pochopenie pamäte AI agentov

V jadre, **pamäť pre AI agentov sa týka mechanizmov, ktoré im umožňujú uchovávať a vybavovať informácie**. Tieto informácie môžu byť konkrétne detaily o konverzácii, preferencie používateľa, minulé akcie alebo dokonca naučené vzory.

Bez pamäte sú AI aplikácie často bezstavové, čo znamená, že každá interakcia začína od nuly. To vedie k opakujúcemu sa a frustrujúcemu užívateľskému zážitku, kde agent „zabúda“ predchádzajúci kontext alebo preferencie.

### Prečo je pamäť dôležitá?

inteligencia agenta je hlboko spätá s jeho schopnosťou vybavovať si a využívať minulé informácie. Pamäť umožňuje agentom byť:

• **Reflektívni**: Učiť sa z minulých akcií a výsledkov.

• **Interaktívni**: Udržiavať kontext počas prebiehajúcej konverzácie.

• **Proaktívni a reaktívni**: Predvídať potreby alebo primerane reagovať na základe historických údajov.

• **Autonómni**: Fungovať samostatnejšie tým, že čerpajú z uložených znalostí.

Cieľom implementácie pamäte je urobiť agentov viac **spoľahlivými a schopnými**.

### Typy pamäte

#### Pracovná pamäť

Predstavte si to ako kúsok poznámkového papiera, ktorý agent používa počas jednej prebiehajúcej úlohy alebo mysleného procesu. Uchováva okamžité informácie potrebné na výpočet nasledujúceho kroku.

Pre AI agentov pracovná pamäť často zachytáva najrelevantnejšie informácie z konverzácie, aj keď je celá história chatu dlhá alebo orezaná. Zameriava sa na extrahovanie kľúčových prvkov ako požiadavky, návrhy, rozhodnutia a akcie.

**Príklad pracovnej pamäte**

V agentovi na rezerváciu ciest môže pracovná pamäť zachytiť aktuálnu požiadavku používateľa, napríklad „Chcem si rezervovať cestu do Paríža“. Táto konkrétna požiadavka je uložená v bezprostrednom kontexte agenta, aby usmerňovala aktuálnu interakciu.

#### Krátkodobá pamäť

Tento typ pamäte uchováva informácie počas trvania jednej konverzácie alebo relácie. Je to kontext aktuálneho chatu, ktorý agentovi umožňuje odkazovať späť na predchádzajúce kolá dialógu.

**Príklad krátkodobej pamäte**

Ak sa používateľ opýta: „Koľko by stál let do Paríža?“ a potom doplní „A čo ubytovanie tam?“, krátkodobá pamäť zabezpečí, že agent vie, že „tam“ sa vzťahuje na „Paríž“ v tej istej konverzácii.

#### Dlhodobá pamäť

To sú informácie, ktoré pretrvávajú naprieč viacerými konverzáciami alebo reláciami. Umožňuje agentom pamätať si používateľské preferencie, historické interakcie alebo všeobecné znalosti počas dlhšieho obdobia. Toto je dôležité pre personalizáciu.

**Príklad dlhodobej pamäte**

Dlhodobá pamäť môže uložiť, že „Ben má rád lyžovanie a aktivity vonku, má rád kávu s výhľadom na hory a chce sa vyhýbať náročným zjazdovkám kvôli starému zraneniu“. Tieto informácie, získané z predchádzajúcich interakcií, ovplyvnia odporúčania pri budúcom plánovaní ciest, čím budú silne personalizované.

#### Pamäť osobnosti (Persona Memory)

Tento špecializovaný typ pamäte pomáha agentovi rozvíjať konzistentnú „osobnosť“ alebo „rolu“. Umožňuje agentovi pamätať si detaily o sebe alebo o svojom zamýšľanom úlohe, čím sú interakcie plynulejšie a zameranejšie.

**Príklad pamäte osobnosti**
Ak je cestovný agent navrhnutý ako „expert na lyžovanie“, pamäť osobnosti môže posilniť túto rolu a ovplyvniť jeho odpovede tak, aby zodpovedali tónu a znalostiam experta.

#### Pamäť pracovného postupu / epizodická pamäť

Táto pamäť ukladá postupnosť krokov, ktoré agent vykonáva počas zložitej úlohy, vrátane úspechov a zlyhaní. Je to ako zapamätať si konkrétne „epizódy“ alebo minulosti skúsenosti, aby sa z nich dalo učiť.

**Príklad epizodickej pamäte**

Ak sa agent pokúsil rezervovať konkrétny let, ale zlyhalo to kvôli nedostupnosti, epizodická pamäť by mohla zaznamenať toto zlyhanie, čo umožní agentovi skúsiť alternatívne lety alebo informovať používateľa o probléme pri nasledujúcom pokuse.

#### Pamäť entít

To zahŕňa extrakciu a zapamätanie si konkrétnych entít (ako ľudia, miesta alebo veci) a udalostí z konverzácií. Umožňuje agentovi budovať štruktúrované chápanie kľúčových prvkov, o ktorých sa diskutovalo.

**Príklad pamäte entít**

Z konverzácie o minulej ceste môže agent extrahovať „Paríž“, „Eiffelova veža“ a „večera v reštaurácii Le Chat Noir“ ako entity. Pri budúcej interakcii by si agent mohol spomenúť na „Le Chat Noir“ a ponúknuť rezerváciu tam znova.

#### Štruktúrované RAG (Retrieval Augmented Generation)

Zatiaľ čo RAG je širšia technika, „Štruktúrované RAG“ je vyzdvihnuté ako výkonná pamäťová technológia. Extrahuje husté, štruktúrované informácie z rôznych zdrojov (konverzácie, e-maily, obrázky) a používa ich na zvýšenie presnosti, pripomenutia a rýchlosti odpovedí. Na rozdiel od klasického RAG, ktorý sa spolieha výhradne na sémantickú podobnosť, Štruktúrované RAG pracuje s vnútornou štruktúrou informácií.

**Príklad štruktúrovaného RAG**

Namiesto pouhého zhodovania kľúčových slov by Štruktúrované RAG mohlo parsovať údaje o lete (destiancia, dátum, čas, letecká spoločnosť) z e-mailu a uložiť ich štruktúrovaným spôsobom. To umožňuje presné dotazy ako „Akým letom som si rezervoval cestu do Paríža v utorok?“

## Implementácia a ukladanie pamäte

Implementácia pamäte pre AI agentov zahŕňa systematický proces **správy pamäte**, ktorý zahŕňa generovanie, ukladanie, získavanie, integráciu, aktualizáciu a dokonca aj „zabúdanie“ (alebo mazanie) informácií. Získavanie je obzvlášť kľúčový aspekt.

### Špecializované pamäťové nástroje

#### Mem0

Jeden zo spôsobov, ako ukladať a spravovať pamäť agenta, je použitie špecializovaných nástrojov ako Mem0. Mem0 funguje ako perzistentná pamäťová vrstva, ktorá agentom umožňuje pripomínať si relevantné interakcie, ukladať používateľské preferencie a faktický kontext a učiť sa z úspechov a neúspechov v priebehu času. Myšlienka je v tom, že bezstavové agenti sa stanú stavovými.

Funguje prostredníctvom **dvojfázového procesu pamäte: extrakcia a aktualizácia**. Najprv sú správy pridané do vlákna agenta odoslané do služby Mem0, ktorá používa Large Language Model (LLM) na zhrnutie histórie konverzácie a extrakciu nových spomienok. Následne LLM-riadená fáza aktualizácie rozhodne, či tieto spomienky pridať, upraviť alebo vymazať a uloží ich v hybridnom úložisku, ktoré môže zahŕňať vektorovú, grafovú a kľúč-hodnota databázy. Systém tiež podporuje rôzne typy pamäte a môže integrovať grafovú pamäť na správu vzťahov medzi entitami.

#### Cognee

Ďalším silným prístupom je použitie **Cognee**, open-source semantickej pamäte pre AI agentov, ktorá transformuje štruktúrované a neštruktúrované dáta do dotazovateľných znalostných grafov podporených embeddingmi. Cognee poskytuje **duálne úložisko** kombinujúce vyhľadávanie podľa vektorovej podobnosti s grafovými vzťahmi, čo umožňuje agentom chápať nielen to, čo je informáciou podobné, ale aj to, ako sú koncepty navzájom prepojené.

Vyniká v **hybridnom získavaní**, ktoré mieša vektorovú podobnosť, grafovú štruktúru a LLM uvažovanie - od priameho hľadania chunkov po grafovo-uvedomelé zodpovedanie otázok. Systém udržiava **živú pamäť**, ktorá sa vyvíja a rastie, pričom zostáva dotazovateľná ako jeden prepojený graf, podporujúc krátkodobý kontext relácie aj dlhodobú perzistentnú pamäť.

Notebookový tutoriál Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonštruje budovanie tejto zjednotenej pamäťovej vrstvy, s praktickými príkladmi ingestovania rôznych zdrojov dát, vizualizácie znalostného grafu a dotazovania s rôznymi vyhľadávacími stratégiami prispôsobenými konkrétnym potrebám agenta.

### Ukladanie pamäte s RAG

Nad rámec špecializovaných pamäťových nástrojov ako mem0 , môžete využiť robustné vyhľadávacie služby ako **Azure AI Search ako backend na ukladanie a získavanie spomienok**, najmä pre štruktúrované RAG.

To vám umožní ukotviť odpovede agenta vo vašich vlastných dátach, zabezpečujúc relevantnejšie a presnejšie odpovede. Azure AI Search môže byť použitý na ukladanie používateľských cestovných spomienok, katalógov produktov alebo akýchkoľvek iných doménovo špecifických znalostí.

Azure AI Search podporuje schopnosti ako **Štruktúrované RAG**, ktoré vynikajú v extrahovaní a získavaní hustých, štruktúrovaných informácií z veľkých datasetov, ako sú histórie konverzácií, e-maily alebo dokonca obrázky. To poskytuje „nadľudskú presnosť a pripomenutie“ v porovnaní s tradičnými prístupmi rozdelenia textu a embeddingov.

## Ako nechať AI agentov samovylepšovať sa

Bežným vzorom pre samovylepšujúcich sa agentov je zavedenie **„knowledge agenta“**. Tento samostatný agent pozoruje hlavnú konverzáciu medzi používateľom a primárnym agentom. Jeho úlohou je:

1. **Identifikovať cenné informácie**: Určiť, či je nejaká časť konverzácie hodná uloženia ako všeobecné vedomosti alebo konkrétna preferencia používateľa.

2. **Extrakcia a sumarizácia**: Destilovať podstatné učenie alebo preferenciu z konverzácie.

3. **Uložiť do znalostnej bázy**: Persistovať tieto extrahované informácie, často vo vektorovej databáze, aby mohli byť neskôr získané.

4. **Obohatiť budúce dotazy**: Keď používateľ iniciuje nový dotaz, knowledge agent získa relevantné uložené informácie a pripojí ich k promptu používateľa, poskytujúc kľúčový kontext primárnemu agentovi (podobne ako RAG).

### Optimalizácie pre pamäť

• **Riadenie latencie**: Aby sa predišlo spomaleniu užívateľských interakcií, môže sa najprv použiť lacnejší, rýchlejší model na rýchlu kontrolu, či sú informácie hodné uloženia alebo získania, a zložitejší extrakčný/získavací proces sa vyvolá len v prípade potreby.

• **Údržba znalostnej bázy**: Pre rastúcu znalostnú bázu sa menej často používané informácie môžu presunúť do „studeného úložiska“ na zníženie nákladov.

## Máte ďalšie otázky o pamäti agentov?

Pripojte sa k [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) a stretnite sa s ďalšími študentmi, zúčastnite sa office hours a získajte odpovede na svoje otázky o AI agentoch.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vylúčenie zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, majte, prosím, na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by sa mal považovať za záväzný (autoritívny) zdroj. Pre dôležité informácie sa odporúča profesionálny preklad vykonaný človekom. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne výklady vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->