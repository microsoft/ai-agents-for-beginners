[![Úvod do AI agentov](../../../translated_images/sk/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Kliknite na obrázok vyššie a pozrite si video k tejto lekcii)_

# Úvod do AI agentov a príklady použitia agentov

Vitajte v kurze **AI agenti pre začiatočníkov**! Tento kurz vám poskytne základné vedomosti — a skutočný funkčný kód — aby ste mohli začať budovať AI agentov od základov.

Príďte sa pozdraviť do <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord komunity</a> — je plná študentov a tvorcov AI, ktorí radi zodpovedia vaše otázky.

Predtým, než sa pustíme do budovania, uistime sa, že naozaj rozumieme tomu, čo AI agent *je* a kedy dáva zmysel ho použiť.

---

## Úvod

Táto lekcia pokrýva:

- Čo sú AI agenti a aké rôzne typy existujú
- Pre aké typy úloh sú AI agenti najlepšie vhodní
- Základné stavebné bloky, ktoré použijete pri navrhovaní agentického riešenia

## Ciele učenia

Na konci tejto lekcie by ste mali byť schopní:

- Vysvetliť, čo je AI agent a ako sa líši od bežného AI riešenia
- Vedieť, kedy siahnuť po AI agentovi (a kedy nie)
- Nakresliť základný návrh agentického riešenia pre reálny problém

---

## Definovanie AI agentov a typy AI agentov

### Čo sú AI agenti?

Tu je jednoduchý spôsob, ako si to predstaviť:

> **AI agenti sú systémy, ktoré umožňujú veľkým jazykovým modelom (LLM) skutočne *vykonávať činnosti* — tým, že im dávajú nástroje a vedomosti na pôsobenie vo svete, nielen odpovedanie na podnety.**

Poďme si to trochu rozobrať:

- **Systém** — AI agent nie je iba jedna vec. Je to zbierka častí pracujúcich spolu. V jadre má každý agent tri časti:
  - **Prostredie** — Priestor, v ktorom agent pracuje. Pre cestovného agenta je to samotná rezervačná platforma.
  - **Senzory** — Ako agent číta aktuálny stav svojho prostredia. Náš cestovný agent môže kontrolovať dostupnosť hotelov alebo ceny leteniek.
  - **Aktuátory** — Ako agent koná. Cestovný agent môže zarezervovať izbu, poslať potvrdenie alebo zrušiť rezerváciu.

![Čo sú AI agenti?](../../../translated_images/sk/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Veľké jazykové modely** — Agenti existovali ešte pred LLM, ale LLM práve robia moderných agentov takými silnými. Dokážu porozumieť prirodzenému jazyku, uvažovať o kontexte a premeniť nejasný požiadavok používateľa na konkrétny plán akcie.

- **Vykonávanie činností** — Bez systému agenta LLM iba generuje text. V rámci systému agenta môže LLM skutočne *vykonávať* kroky — vyhľadávať v databáze, volať API, posielať správu.

- **Prístup k nástrojom** — Aké nástroje agent môže používať závisí od (1) prostredia, v ktorom beží, a (2) čo mu vývojár poskytne. Cestovný agent môže vyhľadávať lety, ale nemusí upravovať zákaznícke záznamy — všetko závisí od toho, čo je prepojené.

- **Pamäť + vedomosti** — Agenti môžu mať krátkodobú pamäť (aktuálny rozhovor) a dlhodobú pamäť (zákaznícka databáza, minulé interakcie). Cestovný agent si môže "pamätať", že preferujete miesta pri okne.

---

### Rôzne typy AI agentov

Nie všetci agenti sú postavení rovnako. Tu je rozdelenie hlavných typov na príklade cestovného agenta:

| **Typ agenta** | **Čo robí** | **Príklad cestovného agenta** |
|---|---|---|
| **Jednoduchí reflexní agenti** | Nasledujú pevne dané pravidlá — bez pamäti, bez plánovania. | Vidí sťažnosť v emaili → presmeruje ju na zákaznícku podporu. To je všetko. |
| **Reflexní agenti založení na modeli** | Udržiavajú interný model sveta a aktualizujú ho, keď sa situácia mení. | Sleduje historické ceny leteniek a označuje trasy, ktoré sa náhle zdraželi. |
| **Agentí s cieľmi** | Má cieľ a zisťuje, ako ho krok za krokom dosiahnuť. | Rezervuje kompletnú cestu (lety, auto, hotel) od vašej aktuálnej polohy k cieľu. |
| **Agentí založení na užitočnosti** | Nielenže nájde *riešenie*, ale hľadá *najlepšie* riešenie vážením kompromisov. | Vyvažuje náklady a pohodlie, aby našiel cestu, ktorá najviac vyhovuje vašim preferenciám. |
| **Učiaci sa agenti** | Zlepšujú sa v čase učením sa z spätnej väzby. | Prispôsobuje budúce odporúčania na základe výsledkov dotazníka po ceste. |
| **Hierarchickí agenti** | Vyšší agent rozdeľuje prácu na podúlohy a deleguje nižším agentom. | Požiadavka "zrušiť cestu" sa rozdelí na: zrušiť let, zrušiť hotel, zrušiť prenájom auta — každú rieši pod-agent. |
| **Systémy multi-agentov (MAS)** | Viac nezávislých agentov spolupracuje (alebo súperí). | Kooperatívne: samostatní agenti riešia hotely, lety a zábavu. Súťaživo: viacerí agenti súperia o rezervácie hotelových izieb za najlepšiu cenu. |

---

## Kedy použiť AI agentov

Len preto, že *môžete* použiť AI agenta, neznamená, že by ste ho vždy *mali* používať. Tu sú situácie, kde agenti naozaj vyniknú:

![Kedy použiť AI agentov?](../../../translated_images/sk/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Otvorené problémy** — Keď kroky na vyriešenie problému nemožno dopredu naprogramovať. LLM musí dynamicky nájsť cestu.
- **Viacstupňové procesy** — Úlohy, ktoré vyžadujú použitie nástrojov cez niekoľko kôl, nie len jednorazové vyhľadávanie alebo generovanie.
- **Zlepšovanie v čase** — Keď chcete, aby systém bol múdrejší na základe spätnej väzby od používateľa alebo signálov z prostredia.

O väčšej hĺbke kedy (a kedy *nie*) používať AI agentov sa dozviete v lekcii **Budovanie dôveryhodných AI agentov** neskôr v kurze.

---

## Základy agentických riešení

### Vývoj agenta

Prvou vecou pri budovaní agenta je definovať *čo môže robiť* — jeho nástroje, akcie a správanie.

V tomto kurze používame **Azure AI Agent Service** ako našu hlavnú platformu. Podporuje:

- Modely od poskytovateľov ako OpenAI, Mistral a Meta (Llama)
- Licencované dáta od poskytovateľov ako Tripadvisor
- Štandardizované definície nástrojov OpenAPI 3.0

### Agentické vzory

S LLM komunikujete cez podnety (prompty). Pri agentoch nie je vždy možné všetky prompti ručne vytvárať — agent potrebuje konať cez viacero krokov. Tu prichádzajú na rad **Agentické vzory**. Sú to opakovane použiteľné stratégie na vytváranie a riadenie LLM v škálovateľnejšom a spoľahlivejšom štýle.

Tento kurz je postavený okolo najbežnejších a najužitočnejších agentických vzorov.

### Agentické rámce

Agentické rámce poskytujú vývojárom hotové šablóny, nástroje a infraštruktúru na budovanie agentov. Uľahčujú:

- Prepojenie nástrojov a schopností
- Sledovanie, čo agent robí (a ladenie, keď sa niečo pokazí)
- Spoluprácu medzi viacerými agentmi

V tomto kurze sa zameriavame na **Microsoft Agent Framework (MAF)** na tvorbu agentov pripravených do produkcie.

---

## Ukážky kódu

Chcete to vidieť v akcii? Tu sú ukážky kódu pre túto lekciu:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Máte otázky?

Pridajte sa do [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), spojte sa s ďalšími študentmi, zúčastnite sa konzultačných hodín a získajte odpovede na svoje otázky o AI agentoch od komunity.

---

## Predchádzajúca lekcia

[Príprava kurzu](../00-course-setup/README.md)

## Nasledujúca lekcia

[Preskúmanie agentických rámcov](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->