# AI Agenti pre Začiatočníkov - Študijný Sprievodca

Použite tento sprievodca ako praktického pomocníka počas vášho prechodu kurzom. Nie je
určený na nahradenie lekcií. Pomáha vám rozhodnúť sa, kde začať, na čo sa
zamerať v každej lekcii a ako spojiť myšlienky do malej funkčnej demonštrácie
agenta.

Ak ste tu prvýkrát, začnite jednoducho:

1. Prečítajte si [Nastavenie Kurzu](./00-course-setup/README.md).
2. Dokončite lekcie 01-06 v poradí.
3. Majte jednu malú demo myšlienku na mysli počas učenia.
4. Po každej lekcii sa opýtajte: "Čo teraz môj agent dokáže, čo predtým nedokázal?"


## Jednoduchá Demo Myšlienka na Pamäti

Dobrý spôsob, ako sa učiť o agentoch, je sledovať jednu demo myšlienku počas kurzu.

Príklad demo: **agent pomocník ku kurzu**.

Používateľ pýta:

> "Chcem sa naučiť, ako agenti používajú nástroje. Nájdite správne lekcie, zhrňte, čo
> by som mal najskôr prečítať, a dajte mi krátku praktickú úlohu."

Bežný chatbot môže odpovedať na základe toho, čo už vie. Agent však dokáže viac:

1. **Čítať alebo vyhľadávať v súboroch kurzu** na nájdenie správnych lekcií.
2. **Používať nástroje** na získanie odkazov na lekcie, príkladov alebo podporných materiálov.
3. **Plánovať** krátku učebnú cestu namiesto poskytovania jednej dlhšej odpovede.
4. **Používať kontext** z aktuálneho rozhovoru na udržanie zamerania na cieľ študenta.
5. **Pamätať si užitočné preferencie**, ak aplikácia podporuje pamäť.
6. **Ukazovať stopy, citácie alebo protokoly**, aby používateľ rozumel, čo sa stalo.
7. **Použiť ochranné opatrenia** pred vykonaním rizikových krokov alebo použitím citlivých údajov.


by táto lekcia pridala?


## K Čomu Smerujete

Na konci kurzu by ste mali byť schopní vysvetliť a postaviť agentné systémy,
ktoré kombinujú tieto časti:

| Časť | Význam v jednoduchej reči | V demo |
|------|------------------------|-------------|
| Model | Motor uvažovania, ktorý interpretuje požiadavku používateľa | Rozumie, že študent chce lekcie o používaní nástrojov |
| Nástroje | Funkcie, API, súbory, prehliadače alebo služby, ktoré agent môže používať | Vyhľadáva v úložisku alebo získava obsah lekcie |
| Vedomosti | Dokumenty alebo údaje použité na podloženie odpovede | README súbory kurzu a materiál lekcie |
| Kontext | Informácie zahrnuté v ďalšom volaní modelu | Cieľ používateľa a výsledky nástroja |
| Pamäť | Informácie uložené na neskoršie použitie | Študent preferuje praktické príklady v Pythone |
| Plánovanie | Rozdelenie väčšieho cieľa na menšie kroky | Nájsť lekcie, zhrnúť ich, navrhnúť prax |
| Orchestrace | Riadenie práce medzi nástrojmi, krokmi alebo agentmi | Plánovač volá vyhľadávací nástroj, potom zhrňovač |
| Dôvera | Bezpečnosť, ochrana, hodnotenie a sledovateľnosť | Protokoluje volania nástrojov a pýta sa pred akciami s veľkým dopadom |

## Modely a Poskytovatelia

Ukážkové kódy ku kurzu používajú **Microsoft Agent Framework (MAF)** a cielia na **Azure OpenAI Responses API** — odporúčanú API do budúcna, ktorá kombinuje chatové dokončenia, volanie nástrojov, multimodálny vstup a stavové rozhovory v jednom API. Pripájate sa buď cez projekt **Microsoft Foundry** (s `FoundryChatClient`) alebo priamo do Azure OpenAI (s `OpenAIChatClient`).

Počas prechádzania lekciami máte niekoľko možností poskytovateľov:

- **Microsoft Foundry / Azure OpenAI (Responses API)** — hlavná cesta používaná naprieč lekciami. Prihláste sa pomocou `az login` na bezkľúčovú autentifikáciu Entra ID.
- **Foundry Local** — spustite modely úplne na zariadení cez OpenAI-kompatibilné API (bez cloudu, bez API kľúčov). Ideálne na offline alebo bezplatné experimentovanie. Pozrite [Nastavenie Kurzu](./00-course-setup/README.md).
- **MiniMax** — OpenAI-kompatibilný poskytovateľ s modelmi veľkého kontextu, použiteľný ako priamá náhrada.

> **Poznámka:** GitHub Models je zastaraný (bude ukončený v júli 2026) a nepodporuje Responses API. Ukážky boli aktualizované na použitie Azure OpenAI / Microsoft Foundry.

## Vyberte si Svoj Učebný Plán

Môžete absolvovať celý kurz v poradí alebo skočiť na cestu podľa toho, čo chcete
vytvoriť.

| Ak je vaším cieľom... | Začnite s | Potom študujte |
|-----------------------|------------|------------|
| Pochopiť, čo agenti sú | 01, 02, 03 | 04, 05, 06 |
| Vytvoriť agenta, ktorý používa nástroje | 04 | 05, 07, 14 |
| Vytvoriť agenta založeného na RAG | 05 | 04, 06, 12 |
| Navrhovať viacstupňové pracovné postupy | 07 | 08, 09, 14 |
| Pochopiť multi-agentné systémy | 08 | 07, 09, 11 |
| Pripraviť agentov na produkciu | 06, 10 | 12, 13, 18 |
| Preskúmať protokoly a automatizáciu prehliadača | 11, 15 | 10, 18 |

Tip: ak ste v agentoch noví, nevynechávajte lekcie 01-06. Tie vám dajú slovník,
ktorý budete potrebovať pre zvyšok kurzu.

## Sprievodca Lekcia-po-Lekcii

| Lekcia | Čo sa naučíte | Vyskúšajte po lekcii |
|--------|----------------|---------------------------|
| [01 - Úvod do AI Agentov](./01-intro-to-ai-agents/README.md) | Čím sa agent líši od základného chatbota. | Vysvetlite svoju demo myšlienku ako agenta, nielen chatovú aplikáciu. |
| [02 - Agentné Frameworky](./02-explore-agentic-frameworks/README.md) | Ako frameworky pomáhajú s modelmi, nástrojmi, stavom a pracovnými postupmi. | Identifikujte, ktoré časti vášho demoa by spravoval framework. |
| [03 - Agentné Dizajnové Vzory](./03-agentic-design-patterns/README.md) | Bežné vzory na navrhovanie správania agentov. | Náčrt používateľskej cesty pred písaním kódu. |
| [04 - Používanie Nástrojov](./04-tool-use/README.md) | Ako agenti volajú nástroje na získavanie údajov alebo vykonávanie akcií. | Definujte jeden nástroj, ktorý by váš demo agent potreboval. |
| [05 - Agentný RAG](./05-agentic-rag/README.md) | Ako retrieval umožňuje agentovi základ na dokumentoch alebo dátach. | Rozhodnite, aký zdroj vedomostí by mal váš demo agent vyhľadávať. |
| [06 - Dôveryhodní Agenti](./06-building-trustworthy-agents/README.md) | Ako pridať ochranné opatrenia, dohľad a bezpečnejšie správanie. | Pridajte pravidlo, kedy by sa mal agent najskôr opýtať používateľa. |
| [07 - Dizajn Plánovania](./07-planning-design/README.md) | Ako agenti rozkladajú väčšie ciele na menšie kroky. | Napíšte trojkrokový plán pre vašu demo požiadavku. |
| [08 - Multi-Agentný Dizajn](./08-multi-agent/README.md) | Kedy rozdeliť prácu medzi špecializovaných agentov. | Rozhodnite, či váš demo potrebuje jedného alebo viacerých agentov. |
| [09 - Metakognícia](./09-metacognition/README.md) | Ako agenti môžu prehodnotiť a zlepšiť vlastný výstup. | Pridajte finálnu kontrolu pred odpoveďou agenta. |
| [10 - AI Agenti v Produkcii](./10-ai-agents-production/README.md) | Čo sa mení, keď agent prechádza z demo do produkcie. | Vypíšte, čo by ste monitorovali: kvalitu, náklady, latenciu, chyby. |
| [11 - Agentné Protokoly](./11-agentic-protocols/README.md) | Ako protokoly spájajú agentov s nástrojmi a inými agentmi. | Identifikujte, kde by štandardný protokol mohol zjednodušiť integráciu. |
| [12 - Kontextový Inžiniering](./12-context-engineering/README.md) | Ako vybrať, orezať, izolovať a spravovať kontext. | Rozhodnite, čo patrí do promptu a čo má zostať vonku. |
| [13 - Agentná Pamäť](./13-agent-memory/README.md) | Ako agenti môžu ukladať užitočné informácie medzi interakciami. | Vyberte jednu bezpečnú preferenciu, ktorú by váš demo mohol pamätať. |
| [14 - Microsoft Agent Framework](./14-microsoft-agent-framework/README.md) | Frameworkové stavebné bloky pre agentov a pracovné postupy, plus hostovanie LangChain/LangGraph agentov na Microsoft Foundry. | Priraďte kroky vášho demoa ku konceptom frameworku. |
| [15 - Agenti pre Použitie Počítača](./15-browser-use/README.md) | Ako agenti môžu komunikovať s prehliadačom alebo UI, vrátane príkladov z praxe ako Microsoft Project Opal. | Vyberte jednu prehliadačovú úlohu, ktorá by mala stále vyžadovať potvrdenie používateľa. |
| [18 - Zabezpečenie AI Agentov](./18-securing-ai-agents/README.md) | Ako urobiť akcie agenta viac auditovateľnými a odolnými voči manipulácii. | Rozhodnite, ktoré akcie v demo by mali byť zaznamenané alebo zdokumentované. |

Lekcie 16 a 17 sú uvedené v hlavnom README ako čoskoro dostupné. Pridajte ich do svojho
študijného plánu, keď budú materiály k dispozícii.

## Kľúčové Myšlienky v Prístupných Termínoch

### Nástroje

Nástroj je niečo, čo môže agent volať, aby vykonal prácu mimo modelu. Dobrý nástroj
má jasný názov, úzky rozsah práce, typované vstupy, predvídateľný výstup a bezpečný spôsob
zlyhania.

Pre demo pomocníka ku kurzu by mohol byť nástroj:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG a Vedomosti

RAG pomáha agentovi odpovedať zo zdrojového materiálu namiesto hádania. V tomto
kurze môže byť zdrojový materiál README súbory lekcií, ukážkové kódy alebo externé
zdroje prepojené z lekcií.

Používajte RAG, keď by odpoveď mala byť podložená dokumentmi, dátami alebo aktuálnymi
súbormi projektu.

### Plánovanie

Plánovanie je užitočné, keď požiadavka má viac ako jeden krok. Plány udržiavajte krátke a
dostatočne viditeľné, aby ich mohol skontrolovať vývojár alebo používateľ.

Pre demo by mohol byť plán:

1. Nájsť lekcie súvisiace s používaním nástrojov.
2. Zhrnúť najrelevantnejšie lekcie.
3. Odporučiť jednu praktickú úlohu.

### Kontext

Kontext je to, čo model práve vidí. Príliš málo kontextu môže spôsobiť, že agent
prehliadne dôležité detaily. Príliš veľa kontextu môže agentovi spomaliť, predražiť ho
alebo zjednodušiť zmätenie.

Dobrá kontextová práca znamená vybrať správne informácie pre ďalšie volanie modelu.




iba keď sú užitočné, bezpečné a ľahko aktualizovateľné alebo vymazateľné.


Zapamätanie si citlivých osobných údajov zvyčajne nie je.








latenciu, náklady, zlyhania a spätnú väzbu od používateľov.




schválenie človekom pre akcie s vysokým dopadom, redakciu údajov kde treba, a záznamy alebo
potvrdenky pre akcie, ktoré musí byť možné auditovať.






2. **Pomenujte novú schopnosť agenta.** Napríklad: používanie nástrojov, retrieval,
   plánovanie, pamäť, sledovateľnosť alebo bezpečnosť.
3. **Pridajte ju do demo pomocníka ku kurzu.** Čo sa v démach teraz zmení?
4. **Nájdite riziko.** Čo by mohlo zlyhať, ak sa táto schopnosť zneužije?
5. **Napíšte jednu testovaciu otázku.** Ako by ste skontrolovali, že sa agent správne správa?






2. Aký nástroj by váš agent potreboval ako prvý a prečo?
3. Aký zdroj vedomostí by mal podkladať odpoveď agenta?
4. Aký kontext by mal byť zahrnutý v ďalšom volaní modelu?
5. Čo by si mal agent pamätať a čo by mal vynechať z ukladania?
6. Kedy by sa mal agent opýtať na schválenie človeka?
7. Aké záznamy, stopy alebo potvrdenky by vám pomohli neskôr ladeniu alebo auditu agenta?


## Navrhovaná Záverečná Úloha

Na konci kurzu vytvorte malého agenta, ktorý pomôže študentovi navigovať v tomto
úložisku.

Minimálna verzia:

- Prijať tému od používateľa.
- Nájsť najrelevantnejšie lekcie.
- Zhrnúť, čo prečítať najskôr.
- Navrhnúť jednu praktickú úlohu.
- Ukázať, ktoré súbory alebo odkazy boli použité.

Rozšírená verzia:

- Pamätať si preferovaný programovací jazyk študenta.
- Použiť jednoduchý plán pred odpoveďou.
- Pridať krok samokontroly pred finálnou odpoveďou.
- Protokolovať volania nástrojov a získané zdroje.
- Pýtať sa na potvrdenie pred otvorením úloh prehliadača alebo UI automatizácie.

Toto vám poskytne malý, ale realistický spôsob, ako praktizovať nástroje, RAG, plánovanie,
kontext, pamäť, sledovateľnosť a dôveru v jednom projekte.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->