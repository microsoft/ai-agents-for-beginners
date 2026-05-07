[![Úvod do AI agentov](../../../translated_images/sk/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Kliknite na obrázok vyššie pre sledovanie videa k tejto lekcii)_

# Úvod do AI agentov a príklady použitia agentov

Vitajte v kurze **AI agenti pre začiatočníkov**! Tento kurz vám poskytne základné vedomosti — a skutočný funkčný kód — aby ste mohli začať stavať AI agentov od základov.

Príďte sa pozdraviť do <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord komunity</a> — je plná študentov a tvorcov AI, ktorí radi zodpovedajú otázky.

Predtým než začneme stavať, poďme si ujasniť, čo AI agent *vlastne je* a kedy má zmysel ho použiť.

---

## Úvod

Táto lekcia pokrýva:

- Čo sú AI agenti a rôzne typy, ktoré existujú
- Na aké úlohy sú AI agenti najvhodnejší
- Základné stavebné bloky, ktoré použijete pri navrhovaní Agentickej riešenia

## Učebné ciele

Na konci tejto lekcie by ste mali vedieť:

- Vysvetliť, čo je AI agent a ako sa líši od bežného AI riešenia
- Vedieť, kedy použiť AI agenta (a kedy nie)
- Načrtnúť základný návrh Agentického riešenia pre reálny problém

---

## Definovanie AI agentov a typy AI agentov

### Čo sú AI agenti?

Tu je jednoduchý spôsob, ako o tom premýšľať:

> **AI agenti sú systémy, ktoré umožňujú veľkým jazykovým modelom (LLM) skutočne *robiť veci* — tým, že im dávajú nástroje a poznatky na pôsobenie vo svete, nie len reagovať na požiadavky.**

Trochu to rozoberme:

- **Systém** — AI agent nie je len jedna vec. Je to súbor častí, ktoré spolupracujú. V jadre má každý agent tri časti:
  - **Prostredie** — Priestor, v ktorom agent pracuje. Pre cestovného agenta by to bola samotná rezervačná platforma.
  - **Senzory** — Ako agent číta aktuálny stav svojho prostredia. Náš cestovný agent môže napríklad kontrolovať dostupnosť hotelov alebo ceny letov.
  - **Aktuátory** — Ako agent koná. Cestovný agent môže rezervovať izbu, poslať potvrdenie alebo zrušiť rezerváciu.

![Čo sú AI agenti?](../../../translated_images/sk/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Veľké jazykové modely** — Agenti existovali pred LLM, ale práve LLM robia moderných agentov tak silnými. Dokážu rozumieť prirodzenému jazyku, uvažovať o kontexte a premeniť nejasnú požiadavku používateľa na konkrétny plán.

- **Vykonávanie akcií** — Bez systému agenta LLM len generuje text. V rámci agenta môže LLM naozaj *vykonávať* kroky — vyhľadávať v databáze, volať API, posielať správu.

- **Prístup k nástrojom** — Aké nástroje agent môže používať závisí (1) od prostredia, v ktorom beží, a (2) od toho, čo mu vývojár dovolil. Cestovný agent môže napríklad vyhľadávať lety, ale nemusí upravovať zákaznícke záznamy — všetko záleží na zapojení.

- **Pamäť + poznatky** — Agenti môžu mať krátkodobú pamäť (aktuálny rozhovor) a dlhodobú pamäť (databázu zákazníkov, minulé interakcie). Cestovný agent si môže „pamätať“, že preferujete sedadlá pri okne.

---

### Rôzne typy AI agentov

Nie všetci agenti sú postavení rovnako. Tu je prehľad hlavných typov, použijúc cestovného agenta ako príklad:

| **Typ agenta** | **Čo robí** | **Príklad cestovného agenta** |
|---|---|---|
| **Jednoduché reflexné agenti** | Dodržiavajú pevne stanovené pravidlá — bez pamäti, bez plánovania. | Vidí sťažnosť v e-maile → preposiela ju zákazníckej podpore. To je všetko. |
| **Reflexní agenti s modelom** | Udržujú interný model sveta a aktualizujú ho, keď sa situácia mení. | Sleduje historické ceny letov a upozorní na trasy, ktoré majú náhle vysoké ceny. |
| **Agent založený na cieľoch** | Má cieľ a zisťuje, ako ho dosiahnuť krok za krokom. | Rezervuje celú cestu (lety, auto, hotel) od vášho miesta k cieľu. |
| **Agent založený na užitočnosti** | Nielen nájde *nejaké* riešenie — hľadá *najlepšie* riešenie zvažovaním kompromisov. | Vyvažuje cenu a pohodlie, aby našiel cestu najviac vyhovujúcu vašim preferenciám. |
| **Učiaci sa agenti** | Zlepšujú sa v priebehu času učením sa z spätnej väzby. | Prispôsobuje budúce odporúčania na základe výsledkov prieskumu po ceste. |
| **Hierarchickí agenti** | Vysokopozičný agent rozdeľuje prácu na podúlohy a prideľuje ich nižším agentom. | Požiadavka „zrušiť cestu“ sa rozdelí na: zrušiť let, hotel, požičovňu auta — každý spracuje podagent. |
| **Systémy viacerých agentov (MAS)** | Niekoľko nezávislých agentov spolupracuje (alebo súťaží). | Kooperatívne: samostatní agenti zvládajú hotely, lety a zábavu. Súťažne: viac agentov bojuje o obsadenie hotelových izieb za najlepšiu cenu. |

---

## Kedy použiť AI agentov

Len preto, že *môžete* použiť AI agenta, neznamená, že by ste vždy *mali*. Tu sú situácie, kde agenti naozaj vynikajú:

![Kedy použiť AI agentov?](../../../translated_images/sk/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Otvorené problémy** — Keď nie je možné vopred naprogramovať kroky riešenia problému. LLM musí dynamicky nájsť cestu.
- **Viacstupňové procesy** — Úlohy, ktoré vyžadujú použitie nástrojov cez niekoľko krokov, nie len jedno vyhľadanie alebo generovanie.
- **Zlepšovanie v čase** — Keď chcete, aby sa systém zlepšoval na základe spätnej väzby používateľa alebo signálov z prostredia.

Podrobnejšie sa pozrieme na to, kedy (a kedy *nie*) používať AI agentov v lekcii **Stavba dôveryhodných AI agentov** neskôr v kurze.

---

## Základy Agentických riešení

### Vývoj agenta

Prvým krokom pri stavbe agenta je definovať *čo môže robiť* — jeho nástroje, akcie a správanie.

V tomto kurze používame **Azure AI Agent Service** ako hlavnú platformu. Podporuje:

- Otvorené modely ako OpenAI, Mistral a Llama
- Licencované dáta od poskytovateľov ako Tripadvisor
- Štandardizované definície nástrojov OpenAPI 3.0

### Agentické vzory

S LLM komunikujete pomocou promptov. Pri agentoch však nemôžete vždy manuálne vytvárať každý prompt — agent musí konať naprieč mnohými krokmi. Tu prichádzajú na rad **agentické vzory**. Sú to znovupoužiteľné stratégie pre promptovanie a riadenie LLM, ktoré sú škálovateľnejšie a spoľahlivejšie.

Tento kurz je postavený okolo najbežnejších a najpoužívanejších agentických vzorov.

### Agentické frameworky

Agentické frameworky dávajú vývojárom pripravené šablóny, nástroje a infraštruktúru na stavbu agentov. Uľahčujú:

- Pripojenie nástrojov a schopností
- Monitorovanie toho, čo agent robí (a ladeniu chýb)
- Spoluprácu medzi viacerými agentmi

V tomto kurze sa zameriavame na **Microsoft Agent Framework (MAF)** pre tvorbu agentov pripravených do produkcie.

---

## Ukážky kódu

Pripravení vidieť to v akcii? Tu sú ukážky kódu k tejto lekcii:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Máte otázky?

Pridajte sa na [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), aby ste sa spojili s ďalšími študentmi, zúčastnili sa konzultačných hodín a získali odpovede na otázky o AI agentoch od komunity.

---

## Predchádzajúca lekcia

[Príprava kurzu](../00-course-setup/README.md)

## Ďalšia lekcia

[Preskúmanie agentických frameworkov](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Upozornenie**:
Tento dokument bol preložený pomocou AI prekladačskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, majte prosím na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku sa považuje za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->