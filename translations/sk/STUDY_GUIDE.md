# AI agenti pre začiatočníkov - študijný sprievodca

Použite tento sprievodca ako praktického spoločníka počas prechádzania kurzom. Nie je
určený na nahradenie lekcií. Pomáha vám rozhodnúť sa, kde začať, čo
hľadať v každej lekcii a ako spojiť myšlienky do malej funkčnej ukážky agenta.

Ak ste tu prvýkrát, začnite jednoducho:

1. Prečítajte si [Nastavenie kurzu](./00-course-setup/README.md).
2. Dokončite lekcie 01-06 v poradí.
3. Majte na pamäti jednu malú ukážku nápadu počas učenia.
4. Po každej lekcii sa opýtajte: „Čo môže môj agent teraz urobiť, čo predtým nevedel?“

## Jednoduchá ukážka na zapamätanie

Dobrým spôsobom, ako sa naučiť agentov, je sledovať jeden nápad ukážky cez celý kurz.

Príklad ukážky: **agent pomocník ku kurzu**.

Používateľ sa pýta:

> „Chcem sa naučiť, ako agenti používajú nástroje. Nájdite správne lekcie, zhrňte, čo
> by som mal najskôr prečítať, a dajte mi krátku praktickú úlohu.“

Bežný chatbot môže odpovedať na základe toho, čo už vie. Agent však môže viac:

1. **Čítať alebo vyhľadávať súbory kurzu** na nájdenie správnych lekcií.
2. **Používať nástroje** na získavanie odkazov na lekcie, príkladov alebo podporného materiálu.
3. **Plánovať** krátku cestu učenia namiesto dlhých odpovedí.
4. **Používať kontext** z aktuálneho rozhovoru, aby sa sústredil na cieľ študenta.
5. **Pamätať si užitočné preferencie**, ak aplikácia podporuje pamäť.
6. **Zobrazovať stopy, citácie alebo protokoly**, aby používateľ pochopil, čo sa stalo.
7. **Použiť ochranné opatrenia** pred nebezpečnými akciami alebo používaním citlivých dát.

Keď študujete každú lekciu, vráťte sa k tejto ukážke a opýtajte sa: akú novú schopnosť by táto lekcia pridala?

## K čomu smerujete

Na konci kurzu by ste mali vedieť vysvetliť a zostrojiť agentové systémy,
ktoré kombinujú tieto časti:

| Časť | Význam v bežnom jazyku | V demo ukážke |
|------|------------------------|---------------|
| Model | Odôvodňovací mechanizmus, ktorý interpretuje požiadavku používateľa | Chápe, že študent chce lekcie o používaní nástrojov |
| Nástroje | Funkcie, API, súbory, prehliadače alebo služby, ktoré agent môže používať | Vyhľadáva v repozitári alebo získava obsah lekcie |
| Vedomosti | Dokumenty alebo údaje používané na zakotvenie odpovede | Súbory README kurzu a materiál lekcií |
| Kontext | Informácie zahrnuté v ďalšom volaní modelu | Cieľ používateľa a výsledky nástrojov |
| Pamäť | Informácie uložené na neskoršie použitie | Študent preferuje praktické príklady v Pythone |
| Plánovanie | Rozdelenie väčšieho cieľa na menšie kroky | Nájsť lekcie, zhrnúť ich, navrhnúť úlohu na precvičenie |
| Orchestrace | Riadenie práce naprieč nástrojmi, krokmi alebo agentmi | Plánovač volá vyhľadávač, potom zhrňovač |
| Dôvera | Bezpečnosť, zabezpečenie, hodnotenie a pozorovateľnosť | Protokoly volaní nástrojov a opýtanie sa pred zásadnými akciami |

## Vyberte si svoju študijnú cestu

Môžete absolvovať celý kurz v poradí alebo prejsť k ceste podľa toho, čo chcete
vytvoriť.

| Ak je vaším cieľom... | Začnite s | Potom študujte |
|-----------------------|------------|----------------|
| Pochopiť, čo sú agenti | 01, 02, 03 | 04, 05, 06 |
| Vytvoriť agenta používajúceho nástroje | 04 | 05, 07, 14 |
| Postaviť agenta založeného na RAG | 05 | 04, 06, 12 |
| Navrhnúť viacstupňové pracovné postupy | 07 | 08, 09, 14 |
| Pochopiť viacagentové systémy | 08 | 07, 09, 11 |
| Pripraviť agentov do produkcie | 06, 10 | 12, 13, 18 |
| Preskúmať protokoly a automatizáciu prehliadača | 11, 15 | 10, 18 |

Tip: ak ste s agentmi noví, nevynechávajte lekcie 01-06. Poskytnú vám slovnú zásobu, ktorú budete potrebovať
pre zvyšok kurzu.

## Sprievodca lekcia po lekcii

| Lekcia | Čo sa naučíte | Vyskúšajte po lekcii |
|--------|----------------|----------------------|
| [01 - Úvod do AI agentov](./01-intro-to-ai-agents/README.md) | Čo robí agenta odlišným od základného chatbota. | Vysvetlite svoju ukážku ako agenta, nie len chatovaciu aplikáciu. |
| [02 - Agentové rámce](./02-explore-agentic-frameworks/README.md) | Ako rámce pomáhajú s modelmi, nástrojmi, stavom a pracovnými postupmi. | Identifikujte, ktoré časti demo by rámec spravoval. |
| [03 - Agentové dizajnové vzory](./03-agentic-design-patterns/README.md) | Bežné vzory na navrhovanie správania agenta. | Nakreslite cestu používateľa pred písaním kódu. |
| [04 - Používanie nástrojov](./04-tool-use/README.md) | Ako agenti volajú nástroje na získavanie dát alebo vykonanie akcie. | Definujte jeden nástroj, ktorý by váš demo agent potreboval. |
| [05 - Agentic RAG](./05-agentic-rag/README.md) | Ako vyhľadávanie zakotvuje odpovede agenta v dokumentoch alebo dátach. | Rozhodnite, ktorý zdroj vedomostí by mal vaša demo prehľadávať. |
| [06 - Dôveryhodní agenti](./06-building-trustworthy-agents/README.md) | Ako pridať ochranné opatrenia, dohľad a bezpečnejšie správanie. | Pridajte jedno pravidlo, kedy by sa mal agent najskôr opýtať používateľa. |
| [07 - Dizajn plánovania](./07-planning-design/README.md) | Ako agenti rozdeľujú väčšie ciele na menšie kroky. | Napíšte trojkrokový plán pre vašu demo požiadavku. |
| [08 - Dizajn viacagentových systémov](./08-multi-agent/README.md) | Kedy rozdeliť prácu medzi špecializovaných agentov. | Rozhodnite, či vaša demo potrebuje jedného alebo viac agentov. |
| [09 - Metakognícia](./09-metacognition/README.md) | Ako agenti môžu hodnotiť a zlepšovať vlastný výstup. | Pridajte záverečnú samo-kontrolu pred odpoveďou agenta. |
| [10 - AI agenti v produkcii](./10-ai-agents-production/README.md) | Čo sa mení, keď agent prechádza z ukážky do produkcie. | Vypíšte, čo by ste monitorovali: kvalitu, náklady, latenciu, chyby. |
| [11 - Agentové protokoly](./11-agentic-protocols/README.md) | Ako protokoly spájajú agentov s nástrojmi a inými agentmi. | Identifikujte, kde by štandardný protokol mohol zjednodušiť integráciu. |
| [12 - Kontextové inžinierstvo](./12-context-engineering/README.md) | Ako vyberať, orezať, izolovať a spravovať kontext. | Rozhodnite, čo patrí do výzvy (prompt) a čo má zostať vonku. |
| [13 - Pamäť agenta](./13-agent-memory/README.md) | Ako agenti môžu ukladať užitočné informácie medzi interakciami. | Vyberte jednu bezpečnú preferenciu, ktorú by si vaša demo mohla pamätať. |
| [14 - Microsoft Agent Framework](./14-microsoft-agent-framework/README.md) | Špecifické stavebné bloky rámca pre agentov a pracovné postupy. | Namapujte kroky svojho demo na koncepty rámca. |
| [15 - Agenti na používanie počítača](./15-browser-use/README.md) | Ako agenti môžu interagovať s prehliadačom alebo UI rozhraním. | Vyberte jednu úlohu v prehliadači, ktorá by mala stále vyžadovať potvrdenie používateľa. |
| [18 - Zabezpečenie AI agentov](./18-securing-ai-agents/README.md) | Ako spraviť akcie agenta auditovateľné a odolné voči manipulácii. | Rozhodnite, ktoré akcie v demo by mali byť zaznamenávané alebo potvrdené. |

Lekcie 16 a 17 sú v hlavnom README označené ako čoskoro k dispozícii. Pridajte ich do svojho
študijného plánu, keď bude obsah lekcií k dispozícii.

## Kľúčové myšlienky v priateľskom jazyku pre začiatočníkov

### Nástroje

Nástroj je niečo, čo agent môže zavolať na vykonanie práce mimo modelu. Dobrý nástroj
má jasný názov, úzku úlohu, typované vstupy, predvídateľný výstup a bezpečný spôsob
zlyhania.

Pre demo pomocníka ku kurzu môže byť nástroj:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG a vedomosti

RAG pomáha agentovi odpovedať zo zdrojového materiálu namiesto hádania. V tomto
kurze môže byť zdrojový materiál README súbory lekcií, ukážky kódu alebo externé
zdroje prepojené z lekcií.

Používajte RAG, keď má byť odpoveď zakotvená v dokumentoch, dátach alebo aktuálnych
súboroch projektu.

### Plánovanie

Plánovanie je užitočné, keď požiadavka má viac ako jeden krok. Plány držte krátke a
dostatočne viditeľné, aby ich mohol skontrolovať vývojár alebo používateľ.

Pre demo môže byť plán:

1. Nájsť lekcie súvisiace s používaním nástrojov.
2. Zhrnúť najrelevantnejšie lekcie.
3. Odporučiť jednu praktickú úlohu.

### Kontext

Kontext je to, čo model práve vidí. Príliš málo kontextu môže spôsobiť, že agent prehliadne dôležité detaily. Príliš veľa kontextu môže spomaliť agenta, zvýšiť náklady alebo ho zbytočne zmiasť.

Dobré kontextové inžinierstvo znamená vybrať správne informácie pre ďalšie volanie modelu.

### Pamäť

Pamäť sú informácie uložené na neskoršie použitie. Neukladajte všetko. Ukladajte informácie len keď sú užitočné, bezpečné a ľahko sa dajú aktualizovať alebo vymazať.

Napríklad zapamätať si, že „študent preferuje príklady v Pythone“ môže byť užitočné. Ukladanie citlivých osobných údajov zvyčajne nie je vhodné.

### Hodnotenie a pozorovateľnosť

Hodnotenie sa pýta: správne agent urobil svoju prácu?

Pozorovateľnosť sa pýta: môžeme vidieť, ako sa to stalo?

Pre produkčné agentov sledujte volania modelu, volania nástrojov, získaný kontext,
latenciu, náklady, chyby a spätnú väzbu od používateľov.

### Dôvera a bezpečnosť

Dôveryhodní agenti potrebujú viac než len užitočnú výzvu (prompt). Používajte nástroje s najmenšími oprávneniami,
ľudské schválenie pre zásadné akcie, redakciu dát tam, kde je to potrebné, a protokoly alebo potvrdenia pre
akcie, ktoré musia byť auditované.

## Rutina pre 15-minútovú rekapituláciu

Použite túto rutinu po každej lekcii:

1. **Zhrňte lekciu jednou vetou.**
2. **Pomenujte novú schopnosť agenta.** Napríklad: používanie nástrojov, vyhľadávanie,
   plánovanie, pamäť, pozorovateľnosť alebo bezpečnosť.
3. **Pridajte ju do demo pomocníka ku kurzu.** Čo sa v demo teraz zmenilo?
4. **Nájdite riziko.** Čo by mohlo pokaziť, ak sa táto schopnosť zneužije?
5. **Napíšte jednu testovaciu otázku.** Ako by ste skontrolovali, že agent sa správa správne?

## Rýchla samo-kontrola

Pred pokračovaním skúste odpovedať na tieto otázky:

1. Čo môže agent urobiť, čo bežný chatbot sám nedokáže?
2. Aký nástroj by váš agent potreboval najskôr a prečo?
3. Aký zdroj vedomostí by mal zakladať odpoveď agenta?
4. Aký kontext by mal byť zahrnutý v ďalšom volaní modelu?
5. Čo by si mal agent pamätať a čo by sa mal vyhnúť ukladať?
6. Kedy by sa mal agent opýtať na ľudské schválenie?
7. Aké protokoly, stopy alebo potvrdenia by vám pomohli neskôr agent auditovať alebo ladiť?

## Navrhovaná záverečná úloha

Na konci kurzu vytvorte malého agenta, ktorý pomáha študentovi navigovať v tomto repozitári.

Minimálna verzia:

- Prijať tému od používateľa.
- Nájsť najrelevantnejšie lekcie.
- Zhrnúť, čo čítať najskôr.
- Navrhnúť jednu praktickú úlohu.
- Ukázať, ktoré súbory lekcie alebo odkazy boli použité.

Rozšírená verzia:

- Pamätať si preferovaný programovací jazyk študenta.
- Použiť jednoduchý plán pred odpoveďou.
- Pridať krok samo-kontroly pred konečnou odpoveďou.
- Protokolovať volania nástrojov a získané zdroje.
- Vyžiadať potvrdenie pred otvorením prehliadača alebo úlohy automatizácie UI.

Tým získate malý, ale realistický spôsob, ako precvičiť nástroje, RAG, plánovanie,
kontext, pamäť, pozorovateľnosť a dôveru v jednom projekte.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->