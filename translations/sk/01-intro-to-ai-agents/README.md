[![Úvod do AI agentov](../../../translated_images/sk/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Kliknite na obrázok vyššie a pozrite si video k tejto lekcii)_

# Úvod do AI agentov a prípadov použitia agentov

Vitajte v kurze **AI agenti pre začiatočníkov**! Tento kurz vám poskytne základné znalosti — a skutočný fungujúci kód — na začatie tvorby AI agentov od základu.

Príďte sa pozdraviť do <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord komunity</a> — je plná študentov a tvorcov AI, ktorí radi odpovedia na vaše otázky.

Predtým, ako sa pustíme do tvorby, poďme si najprv ujasniť, čo vlastne AI agent *je* a kedy má zmysel ho použiť.

---

## Úvod

Táto lekcia pokrýva:

- Čo sú AI agenti a rôzne typy, ktoré existujú
- Aký druh úloh AI agenti najlepšie zvládajú
- Základné stavebné prvky, ktoré použijete pri navrhovaní agentického riešenia

## Ciele učenia

Na konci tejto lekcie by ste mali byť schopní:

- Vysvetliť, čo je AI agent a ako sa líši od bežného AI riešenia
- Vedieť, kedy použiť AI agenta (a kedy nie)
- Nakresliť základný návrh agentického riešenia pre reálny problém

---

## Definovanie AI agentov a typy AI agentov

### Čo sú AI agenti?

Tu je jednoduchý spôsob, ako to pochopiť:

> **AI agenti sú systémy, ktoré umožňujú veľkým jazykovým modelom (LLMs) skutočne *robíť veci* — tým, že im dávajú nástroje a znalosti na ovplyvňovanie sveta, nielen reagovanie na požiadavky.**

Poďme si to trochu rozobrať:

- **Systém** — AI agent nie je len jedna vec. Je to súbor častí pracujúcich spolu. Každý agent má základne tri súčasti:
  - **Prostredie** — Priestor, v ktorom agent pracuje. Pre cestovného agenta by to bola samotná rezervačná platforma.
  - **Senzory** — Ako agent číta aktuálny stav svojho prostredia. Náš cestovný agent môže kontrolovať dostupnosť hotelov alebo ceny leteniek.
  - **Akčné prvky (aktuátory)** — Ako agent vykonáva akciu. Cestovný agent môže rezervovať izbu, poslať potvrdenie alebo zrušiť rezerváciu.

![Čo sú AI agenti?](../../../translated_images/sk/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Veľké jazykové modely** — Agenti existovali aj pred LLM, no práve LLM robia moderných agentov takými silnými. Dokážu rozumieť prirodzenému jazyku, uvažovať o kontexte a premeniť nejasnú požiadavku používateľa na konkrétny plán.

- **Vykonávanie akcií** — Bez systému agenta LLM iba generuje text. V agentickom systéme však môže LLM *vykonávať* kroky — vyhľadávanie v databáze, volanie API, zasielanie správ.

- **Prístup k nástrojom** — Aké nástroje agent môže použiť závisí od (1) prostredia, v ktorom beží, a (2) čo mu vývojár poskytol. Cestovný agent môže vyhľadávať lety, ale nemusí upravovať zákaznícke záznamy — je to o tom, čo prepojíte.

- **Pamäť + Znalosti** — Agenti môžu mať krátkodobú pamäť (aktuálny rozhovor) a dlhodobú pamäť (zákaznícka databáza, minulé interakcie). Cestovný agent si môže "pamätať", že preferujete sedadlá pri okne.

---

### Rôzne typy AI agentov

Nie všetci agenti sú postavení rovnako. Tu je prehľad hlavných typov na príklade cestovného agenta:

| **Typ agenta** | **Čo robí** | **Príklad cestovného agenta** |
|---|---|---|
| **Jednoduchí reflexní agenti** | Nasleduje pevné pravidlá — bez pamäti, bez plánovania. | Vidí sťažnosť v emaili → preposiela ju zákazníckej podpore. To je všetko. |
| **Modelovo založení reflexní agenti** | Uchováva vnútorný model sveta a aktualizuje ho, keď sa veci menia. | Sleduje historické ceny leteniek a upozorňuje na trasy, ktoré sa náhle zdraželi. |
| **Agentí založení na cieľoch** | Má určený cieľ a krok po kroku hľadá cestu k nemu. | Rezervuje celú cestu (letenky, auto, hotel) od vašej aktuálnej polohy, aby ste sa dostali do cieľa. |
| **Agentí založení na užitočnosti** | Namiesto *nejakého* riešenia hľadá *najlepšie* riešenie vážením kompromisov. | Vyvažuje cenu a pohodlie, aby našiel cestu, ktorá najviac vyhovuje vašim preferenciám. |
| **Učiace sa agentí** | Zlepšuje sa v priebehu času učením sa na základe spätnej väzby. | Prispôsobuje budúce odporúčania na rezervácie podľa výsledkov poanketového prieskumu. |
| **Hierarchickí agentí** | Vyššia úroveň agenta rozdelí prácu na podúlohy a deleguje ich na podriadených agentov. | Požiadavka "zrušiť cestu" sa rozdelí na: zrušiť let, zrušiť hotel, zrušiť prenájom auta — každý rieši podagent. |
| **Systémy viacerých agentov (MAS)** | Viacerí nezávislí agenti spolupracujú (alebo súperia). | Kooperatívne: samostatní agenti riešia hotely, lety a zábavu. Konkurenčné: viacerí agenti súperia o obsadenie hotelových izieb za najlepšiu cenu. |

---

## Kedy použiť AI agentov

Len preto, že *môžete* použiť AI agenta, neznamená to, že by ste ho mali vždy použiť. Tu sú situácie, keď agenti naozaj vynikajú:

![Kedy používať AI agentov?](../../../translated_images/sk/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Otvárané problémy** — Keď kroky na vyriešenie problému nemožno dopredu naprogramovať. LLM musí dynamicky nájsť cestu.
- **Viackrokové procesy** — Úlohy, ktoré vyžadujú používanie nástrojov cez viacero krokov, nie len jednorazové vyhľadávanie alebo generovanie.
- **Zlepšovanie v čase** — Keď chcete, aby sa systém zdokonaľoval na základe spätnej väzby používateľov alebo signálov z prostredia.

Podrobnejšie sa budeme zaoberať kedy (a kedy *nie*) použiť AI agentov v lekcii **Budovanie dôveryhodných AI agentov** neskôr v kurze.

---

## Základy agentických riešení

### Vývoj agenta

Prvou vecou pri tvorbe agenta je definovať *čo môže robiť* — jeho nástroje, akcie a správanie.

V tomto kurze používame ako hlavnú platformu **Microsoft Foundry Agent Service**. Podporuje:

- Modely od poskytovateľov ako OpenAI, Mistral a Meta (Llama)
- Licencované dáta od poskytovateľov ako Tripadvisor
- Štandardizované definície nástrojov OpenAPI 3.0

### Agentické vzory

Komunikujete s LLM cez promptové požiadavky. Pri agentoch však nie je vždy možné ručne vytvoriť každý prompt — agent musí vykonať akciu cez viacero krokov. Tu prichádzajú na scénu **agentické vzory**. Sú to znovupoužiteľné stratégie pre promptovanie a orchestráciu LLM spôsobom, ktorý je škálovateľnejší a spoľahlivejší.

Tento kurz je postavený na najčastejších a najužitočnejších agentických vzoroch.

### Agentické rámce

Agentické rámce poskytujú vývojárom pripravené šablóny, nástroje a infraštruktúru na stavbu agentov. Uľahčujú:

- Prepojenie nástrojov a funkcií
- Sledovanie, čo agent robí (a ladenie chýb)
- Spoluprácu medzi viacerými agentmi

V tomto kurze sa zameriavame na **Microsoft Agent Framework (MAF)** pre tvorbu agentov pripravených na produkciu.

---

## Ukážky kódu

Pripravení vidieť to v akcii? Tu sú ukážky kódu k tejto lekcii:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Máte otázky?

Pripojte sa k [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), aby ste sa spojili s inými študentmi, zúčastnili sa konzultačných hodín a odpovedali na otázky o AI agentoch od komunity.


---

## Rýchle testovanie tohto agenta (voliteľné)

Keď sa naučíte nasadzovať agentov v [Lekcii 16](../16-deploying-scalable-agents/README.md), môžete pridať rýchlu zdravotnú kontrolu po nasadení pre `TravelAgent` tejto lekcie pomocou hotového katalógu [`tests/lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json). Pozrite si [`tests/README.md`](../tests/README.md) pre informácie, ako ho spustiť.

---

## Predchádzajúca lekcia

[Nastavenie kurzu](../00-course-setup/README.md)

## Nasledujúca lekcia

[Preskúmanie agentických rámcov](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->