# AI agenti pre začiatočníkov - študijný sprievodca

Použite tento sprievodca ako praktického spoločníka počas prechádzania kurzom. Nie je
určený na nahradenie lekcií. Pomáha vám rozhodnúť sa, kde začať, na čo
sa zamerať v každej lekcii a ako prepojiť myšlienky do malej fungujúcej agentovej
ukážky.

Ak ste tu prvýkrát, začnite jednoducho:

1. Prečítajte si [Nastavenie kurzu](./00-course-setup/README.md).
2. Postupne dokončite lekcie 01-06.
3. Majte na pamäti jednu malú ukážkovú myšlienku počas učenia.
4. Po každej lekcii sa opýtajte: "Čo môj agent teraz dokáže, čo predtým nedokázal?"


## Jednoduchá ukážka na zapamätanie

Dobrý spôsob učenia agentov je sledovať jednu ukážkovú myšlienku počas celého kurzu.

Príklad ukážky: **agent pomocník v kurze**.

Používateľ pýta:

> "Chcem sa naučiť, ako agenti používajú nástroje. Nájdite správne lekcie, zhrňte, čo
> by som mal najskôr prečítať, a dajte mi krátku úlohu na precvičenie."

Bežný chatbot odpovie z toho, čo už vie. Agent dokáže viac:

1. **Čítať alebo vyhľadávať v súboroch kurzu** na nájdenie správnych lekcií.
2. **Používať nástroje** na získanie odkazov na lekcie, príkladov alebo doplnkových materiálov.
3. **Plánovať** krátku učebnú cestu namiesto poskytovania jednej dlhej odpovede.
4. **Používať kontext** z aktuálneho rozhovoru, aby sa zameral na cieľ študenta.
5. **Pamätať si užitočné preferencie**, ak aplikácia podporuje pamäť.
6. **Zobraziť stopy, citácie alebo záznamy** aby používateľ rozumel, čo sa stalo.
7. **Použiť ochranné pravidlá** pred riskantnými akciami alebo použitím citlivých údajov.







ktoré kombinujú tieto časti:


|------|--------------|----------|
| Model | Racionálny motor, ktorý interpretuje požiadavku používateľa | Rozumie, že študent chce lekcie o používaní nástrojov |
| Nástroje | Funkcie, API, súbory, prehliadače alebo služby, ktoré agent môže použiť | Vyhľadáva v repozitári alebo získava obsah lekcií |
| Vedomosti | Dokumenty alebo údaje na podporu odpovede | README súbory kurzu a materiály k lekciám |
| Kontext | Informácie zahrnuté v ďalšom volaní modelu | Cieľ používateľa a výsledky z nástrojov |
| Pamäť | Informácie uložené na neskoršie použitie | Študent preferuje praktické príklady v Pythone |
| Plánovanie | Rozdelenie väčšieho cieľa na menšie kroky | Nájsť lekcie, zhrnúť ich, navrhnúť praktickú úlohu |
| Orchestrace | Rozdeľovanie práce medzi nástroje, kroky alebo agentov | Plánovač volá vyhľadávací nástroj, potom zhrávač |
| Dôvera | Bezpečnosť, ochrana, hodnotenie a pozorovateľnosť | Zaznamenáva volania nástrojov a pýta sa pred riskantnými krokmi |


## Modely a poskytovatelia

Ukážky kódov v kurze používajú **Microsoft Agent Framework (MAF)** a cielia na **Azure OpenAI Responses API** — odporúčanú API do budúcna, ktorá kombinuje chatovacie dokončenia, volanie nástrojov, multimodálne vstupy a stavové rozhovory v jednom rozhraní. Pripojíte sa buď cez **Microsoft Foundry** projekt (s `FoundryChatClient`) alebo priamo k Azure OpenAI (s `OpenAIChatClient`).

Počas prechádzania lekciami máte niekoľko možností poskytovateľov:

- **Microsoft Foundry / Azure OpenAI (Responses API)** — hlavná cesta používaná v lekciách. Prihláste sa pomocou `az login` pre autentifikáciu Entra ID bez kľúčov.
- **Foundry Local** — spúšťajte modely úplne lokálne cez API kompatibilné s OpenAI (bez cloudu, bez API kľúčov). Ideálne na offline alebo bezplatné experimentovanie. Pozrite [Nastavenie kurzu](./00-course-setup/README.md).
- **MiniMax** — poskytovateľ kompatibilný s OpenAI s modelmi na veľký kontext, použiteľný ako alternatíva "plug-and-play".

> **Poznámka:** GitHub Models je zastaraný (ukončenie v júli 2026) a nepodporuje Responses API. Ukážky boli aktualizované na použitie Azure OpenAI / Microsoft Foundry.

## Vyberte si svoju cestu učenia

Môžete absolvovať celý kurz postupne, alebo skočiť na cestu podľa toho, čo chcete
vybudovať.

| Ak je vaším cieľom... | Začnite s | Potom študujte |
|---------------------|------------|--------------|
| Porozumieť, čo sú agenti | 01, 02, 03 | 04, 05, 06 |
| Vybudovať agenta, ktorý používa nástroje | 04 | 05, 07, 14 |
| Vybudovať agenta založeného na RAG | 05 | 04, 06, 12 |
| Navrhnúť viacstupňové pracovné postupy | 07 | 08, 09, 14 |
| Porozumieť multi-agentným systémom | 08 | 07, 09, 11 |
| Pripraviť agentov na produkciu | 06, 10 | 12, 13, 16, 18 |
| Nasadiť a škálovať agentov na Foundry | 10, 16 | 06, 13, 18 |
| Vybudovať lokálne / offline-prvých agentov | 17 | 04, 05, 11 |
| Preskúmať protokoly a automatizáciu prehliadača | 11, 15 | 10, 18 |

Tip: ak ste nováčik v agentoch, nevynechávajte lekcie 01-06. Dajú vám slovnú zásobu,
ktorú budete potrebovať pre zvyšok kurzu.

## Sprievodca lekcia po lekcii

| Lekcia | Čo sa naučíte | Vyskúšajte po lekcii |
|--------|---------------|----------------------|
| [01 - Úvod do AI agentov](./01-intro-to-ai-agents/README.md) | Čo robí agenta odlišným od bežného chatbota. | Vysvetlite svoju myšlienku agentovej ukážky, nie len chatovacej aplikácie. |
| [02 - Agentic Frameworks](./02-explore-agentic-frameworks/README.md) | Ako frameworky pomáhajú s modelmi, nástrojmi, stavom a pracovnými tokmi. | Identifikujte, ktoré časti vašej ukážky by framework spravoval. |
| [03 - Agentic Design Patterns](./03-agentic-design-patterns/README.md) | Bežné vzory na navrhovanie správania agenta. | Nakreslite cestu používateľa pred písaním kódu. |
| [04 - Používanie nástrojov](./04-tool-use/README.md) | Ako agenti volajú nástroje na získanie dát alebo vykonanie akcie. | Definujte jeden nástroj, ktorý by váš ukážkový agent potreboval. |
| [05 - Agentic RAG](./05-agentic-rag/README.md) | Ako retrieval zakladá odpovede agenta na dokumentoch alebo dátach. | Rozhodnite, ktorý zdroj vedomostí by mal vaša ukážka vyhľadávať. |
| [06 - Dôveryhodní agenti](./06-building-trustworthy-agents/README.md) | Ako pridať ochranné pravidlá, dohľad a bezpečnejšie správanie. | Pridajte jedno pravidlo, kedy by sa mal agent najskôr opýtať používateľa. |
| [07 - Návrh plánovania](./07-planning-design/README.md) | Ako agenti rozkladajú väčšie ciele na menšie kroky. | Napíšte trojkrokový plán pre vašu ukážkovú požiadavku. |
| [08 - Multi-agentný dizajn](./08-multi-agent/README.md) | Kedy rozdeliť prácu medzi špecializovaných agentov. | Rozhodnite, či vaša ukážka potrebuje jedného agenta alebo niekoľko. |
| [09 - Metakognícia](./09-metacognition/README.md) | Ako si agenti môžu prehliadať a zlepšovať vlastný výstup. | Pridajte záverečnú vlastnú kontrolu pred odpoveďou agenta. |
| [10 - AI agenti v produkcii](./10-ai-agents-production/README.md) | Čo sa mení, keď agent prechádza z ukážky do produkcie. | Vypíšte, čo by ste monitorovali: kvalitu, náklady, latenciu, zlyhania. |
| [11 - Agentné protokoly](./11-agentic-protocols/README.md) | Ako protokoly prepájajú agentov s nástrojmi a inými agentmi. | Identifikujte, kde by štandardný protokol zjednodušil integráciu. |
| [12 - Kontextový inžiniering](./12-context-engineering/README.md) | Ako vybrať, skrátiť, izolovať a spravovať kontext. | Rozhodnite, čo patrí do promptu a čo by malo zostať mimo. |
| [13 - Pamäť agenta](./13-agent-memory/README.md) | Ako si agenti môžu ukladať užitočné informácie medzi interakciami. | Vyberte jednu bezpečnú preferenciu, ktorú by vaša ukážka mohla pamätať. |
| [14 - Microsoft Agent Framework](./14-microsoft-agent-framework/README.md) | Špecifické stavebné bloky pre agentov a pracovné toky plus hosťovanie LangChain/LangGraph agentov na Microsoft Foundry. | Mapujte kroky vašej ukážky na framework koncepty. |
| [15 - Agentné používanie počítača](./15-browser-use/README.md) | Ako môžu agenti interagovať s prehliadačom alebo UI povrchmi, vrátane reálnych príkladov ako Microsoft Project Opal. | Vyberte jednu úlohu v prehliadači, ktorá by stále mala vyžadovať potvrdenie používateľa. |
| [16 - Nasadzovanie škálovateľných agentov](./16-deploying-scalable-agents/README.md) | Ako vziať agenta od prototypu k škálovateľnému, pozorovateľnému produkčnému nasadeniu na Microsoft Foundry (hosťované agenti, smerovanie modelov, caching, evaluačné brány, smoke testy). | Vypíšte produkčné potreby, ktoré vaša ukážka ešte vyžaduje: hosťovanie, smerovanie, náklady, hodnotenie. |
| [17 - Vytváranie lokálnych AI agentov](./17-creating-local-ai-agents/README.md) | Ako vybudovať lokaálne-prvých agentov, ktorí bežia úplne na vašom zariadení s Foundry Local a Qwen (lokálne nástroje, lokálny RAG, lokálne MCP). | Rozhodnite, ktoré časti vašej ukážky by mali zostať súkromné a bežať lokálne. |
| [18 - Zabezpečenie AI agentov](./18-securing-ai-agents/README.md) | Ako spraviť akcie agenta auditovateľnejšie a odolné voči manipulácii. | Rozhodnite, ktoré akcie v ukážke by mali byť zaznamenané alebo potvrdené. |

## Validácia nasadených agentov pomocou smoke testov

Keď nasadíte agenta (Lekcia 16), **smoke test** je najlacnejšia prvá kontrola,
ktorá overí, či nasadenie naozaj odpovedá. Tento repozitár obsahuje pripravené
katalógy v [tests/](./tests/README.md) pre nasaditeľných agentov v lekciách
01, 04, 05 a 16, pripojených k
[AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) GitHub
akcii. Spustite ich v záložke **Actions** po nasadení agenta z lekcie.
Smoke testy sú prvá brána — offline a online hodnotenie (lekcie 10 a 16)
vám povedia, aký *dobrý* agent je.

## Kľúčové myšlienky v zrozumiteľnej forme

### Nástroje

Nástroj je niečo, čo agent môže zavolať, aby vykonal prácu mimo modelu. Dobrý nástroj
má jasný názov, úzku úlohu, typované vstupy, predvídateľný výstup a bezpečný spôsob,
ako zlyhať.

Pre agentov pomocníka v kurze by nástroj mohol byť:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG a vedomosti

RAG pomáha agentovi odpovedať zo zdrojového materiálu namiesto hádania. V tomto
kurze môže byť zdrojovým materiálom README lekcií, ukážky kódu alebo externé
zdroje spojené s lekciami.

Použite RAG, keď odpoveď má byť zakotvená v dokumentoch, dátach alebo aktuálnych
súboroch projektu.

### Plánovanie

Plánovanie je užitočné, keď požiadavka obsahuje viac ako jeden krok. Plány nechajte krátke a
dostatočne viditeľné, aby ich mohol skontrolovať vývojár alebo používateľ.

Pre ukážku by plán mohol byť:

1. Nájsť lekcie súvisiace s používaním nástrojov.
2. Zhrnúť najrelevantnejšie lekcie.
3. Odporučiť jednu praktickú úlohu.

### Kontext

Kontext je to, čo model práve vidí. Príliš málo kontextu môže spôsobiť, že agent
prehliadne dôležité detaily. Príliš veľa kontextu môže agent spomaliť, zvýšiť náklady,
alebo urobiť agentovi ľahšie sa pomýliť.

Dobré kontextové inžinierstvo znamená vybrať správne informácie pre ďalšie volanie modelu.




iba keď sú užitočné, bezpečné a ľahko aktualizovateľné alebo vymazateľné.


Napríklad zapamätať si "študent preferuje príklady v Pythone" môže byť užitočné.
Zapamätať si citlivé osobné údaje zvyčajne nie je vhodné.

### Hodnotenie a pozorovateľnosť

Hodnotenie sa pýta: urobil agent správnu vec?

Pozorovateľnosť sa pýta: vidíme, ako sa to stalo?

Pre produkčných agentov sledujte volania modelu, volania nástrojov, získaný kontext,
latenciu, náklady, zlyhania a spätnú väzbu používateľa.

### Dôvera a bezpečnosť

Dôveryhodní agenti potrebujú viac než len užitočný prompt. Používajte nástroje s najnižšími
oprávneniami, ľudské schválenie pre akcie s vysokým dopadom, redakciu údajov podľa potreby a
záznamy alebo potvrdenky pre akcie, ktoré musia byť auditované.

## 15-minútová kontrolná rutina

Používajte túto rutinu po každej lekcii:

1. **Zhrňte lekciu v jednej vete.**
2. **Pomenovajte novú schopnosť agenta.** Napríklad: používanie nástrojov, retrieval,
   plánovanie, pamäť, pozorovateľnosť alebo bezpečnosť.
3. **Pridajte ju do ukážky pomocníka v kurze.** Čo sa v ukážke teraz zmení?
4. **Nájdite riziko.** Čo by sa mohlo pokaziť, ak by sa táto schopnosť zneužila?
5. **Napíšte jedno testovacie otázku.** Ako by ste otestovali, že agent sa správa správne?

## Rýchla samokontrola

Pred pokračovaním skúste odpovedať na tieto otázky:

1. Čo agent dokáže, čo bežný chatbot sám o sebe nedokáže?
2. Ktorý nástroj by váš agent potreboval najskôr a prečo?
3. Ktorý zdroj vedomostí by mal zakladať agentovu odpoveď?
4. Aký kontext by mal byť zahrnutý v ďalšom volaní modelu?
5. Čo by si agent mal pamätať a čo by sa mal vyhnúť ukladať?
6. Kedy by mal agent požiadať o ľudské schválenie?
7. Aké záznamy, stopy alebo potvrdenky by vám pomohli neskôr debugovať alebo auditovať agenta?


## Navrhované záverečné cvičenie

Na konci kurzu vytvorte malého agenta, ktorý pomôže študentovi orientovať sa v tomto
repozitári.

Minimálna verzia:

- Prijať tému od používateľa.
- Nájsť najrelevantnejšie lekcie.
- Zhrnúť, čo čítať ako prvé.
- Navrhnúť jeden praktický úlohu.
- Ukázať, ktoré súbory lekcií alebo odkazy boli použité.

Rozšírená verzia:

- Zapamätať si preferovaný programovací jazyk študenta.
- Použiť jednoduchý plán pred odpoveďou.
- Pridať krok seba-kontroly pred finálnou odpoveďou.
- Zaznamenávať volania nástrojov a získané zdroje.
- Požiadať o potvrdenie pred otvorením prehliadača alebo automatizáciou UI úloh.

Toto vám poskytuje malý, ale realistický spôsob, ako si precvičiť nástroje, RAG, plánovanie,
kontext, pamäť, observabilitu a dôveru v jednom projekte.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->