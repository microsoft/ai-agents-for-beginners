[![Úvod do AI agentov](../../../translated_images/sk/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Kliknite na obrázok vyššie pre sledovanie videa k tejto lekcii)_

# Úvod do AI agentov a prípadov použitia agentov

Vitajte v kurze **AI agenti pre začiatočníkov**! Tento kurz vám poskytne základné vedomosti — a skutočný funkčný kód — aby ste mohli začať vytvárať AI agentov od základu.

Príďte sa pozdraviť do <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord komunity</a> — je plná študentov a tvorcov AI, ktorí radi odpovedia na vaše otázky.

Skôr než sa pustíme do tvorby, uistime sa, že naozaj rozumieme, čo AI agent *je* a kedy má zmysel ho použiť.

---

## Úvod

Táto lekcia pokrýva:

- Čo sú AI agenti a rôzne typy, ktoré existujú
- Aké úlohy sú pre AI agentov najvhodnejšie
- Základné stavebné bloky, ktoré použijete pri navrhovaní agentického riešenia

## Ciele učenia

Na konci tejto lekcie by ste mali byť schopní:

- Vysvetliť, čo je AI agent a ako sa líši od bežného AI riešenia
- Vedieť, kedy použiť AI agenta (a kedy nie)
- Náčrt základného dizajnu agentického riešenia pre reálny problém

---

## Definovanie AI agentov a typy AI agentov

### Čo sú AI agenti?

Tu je jednoduchý spôsob, ako o nich uvažovať:

> **AI agenti sú systémy, ktoré umožňujú veľkým jazykovým modelom (LLM) skutočne *vykonávať činnosti* — tým, že im dávajú nástroje a vedomosti, aby mohli pôsobiť vo svete, nie len odpovedať na podnety.**

Rozoberme si to trochu podrobnejšie:

- **Systém** — AI agent nie je len jedna vec. Je to súbor častí pracujúcich spoločne. Základom každého agenta sú tri diely:
  - **Prostredie** — Priestor, v ktorom agent pracuje. Pre cestovného agenta by to bola samotná rezervačná platforma.
  - **Senzory** — Spôsob, akým agent číta aktuálny stav prostredia. Náš cestovný agent by mohol kontrolovať dostupnosť hotelov alebo ceny leteniek.
  - **Aktuátory** — Spôsob, akým agent vykonáva akciu. Cestovný agent môže rezervovať izbu, poslať potvrdenie alebo zrušiť rezerváciu.

![Čo sú AI agenti?](../../../translated_images/sk/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Veľké jazykové modely** — Agent existovali aj pred LLM, ale to práve LLM robia moderných agentov takých silných. Dokážu rozumieť prirodzenému jazyku, uvažovať o kontexte a premeniť nejasnú požiadavku používateľa na konkrétny akčný plán.

- **Vykonávanie akcií** — Bez agentného systému LLM len generuje text. V agentnom systéme môže LLM skutočne *vykonať* kroky — prehľadávať databázu, volať API, posielať správu.

- **Prístup k nástrojom** — Aké nástroje môže agent používať závisí od (1) prostredia, v ktorom beží, a (2) čo mu vývojár poskytol. Cestovný agent môže vyhľadávať lety, ale nemôže meniť údaje o zákazníkovi — všetko závisí od prepojení.

- **Pamäť + vedomosti** — Agent môže mať krátkodobú pamäť (aktuálny rozhovor) a dlhodobú pamäť (databázu zákazníkov, minulé interakcie). Cestovný agent si môže "pamätať", že uprednostňujete sedadlá pri okne.

---

### Rôzne typy AI agentov

Nie všetci agenti sú postavení rovnako. Tu je rozdelenie hlavných typov na príklade cestovného agenta:

| **Typ agenta** | **Čo robí** | **Príklad cestovného agenta** |
|---|---|---|
| **Jednoduchí reflexní agenti** | Dodržiavajú pevne naprogramované pravidlá — bez pamäte, bez plánovania. | Vidí sťažnosť v emaile → posiela ju zákazníckemu servisu. To je všetko. |
| **Modelovo založení reflexní agenti** | Udržiavajú interný model sveta a aktualizujú ho podľa zmien. | Sleduje historické ceny leteniek a označuje trasy, ktoré sú náhle drahé. |
| **Cieľovo založení agenti** | Majú cieľ a krok za krokom zisťujú, ako ho dosiahnuť. | Rezervuje celý výlet (lety, auto, hotel) od vašej aktuálnej polohy k cieľu. |
| **Agentí založení na užitočnosti** | Nájdu nielen *nejaké* riešenie, ale *najlepšie* riešenie vyvažovaním kompromisov. | Vyvažuje cenu a pohodlie, aby našiel výlet, ktorý najviac vyhovuje vašim preferenciám. |
| **Učiaci sa agenti** | Zlepšujú sa postupne učením sa z reakcií. | Upravuje budúce odporúčania rezervácií podľa výsledkov dotazníkov po výlete. |
| **Hierarchickí agenti** | Vysokopostavený agent rozdelí prácu na podúlohy a deleguje nižším agentom. | Žiadosť "zrušiť výlet" sa rozdelí na: zrušiť let, zrušiť hotel, zrušiť prenájom auta — každý rieši pod-agent. |
| **Systémy viacerých agentov (MAS)** | Viac nezávislých agentov pracujúcich spoločne (alebo súťažiacich). | Kooperatívne: rôzni agenti spravujú hotely, lety a zábavu. Súťaživé: viacerí agenti súťažia o najlepšie ceny hotelových izieb. |

---

## Kedy používať AI agentov

Len preto, že *môžete* použiť AI agenta, neznamená, že by ste mali vždy. Tu sú situácie, kde agenti naozaj vynikajú:

![Kedy používať AI agentov?](../../../translated_images/sk/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Otvorené problémy** — Keď sa kroky na vyriešenie problému nedajú pevne naprogramovať. Potrebujete, aby LLM dynamicky zistil cestu.
- **Viackrokové procesy** — Úlohy vyžadujúce používanie nástrojov počas viacerých krokov, nie len jedno vyhľadanie alebo generovanie.
- **Zlepšenie v priebehu času** — Keď chcete, aby systém bol múdrejší na základe spätnej väzby od používateľa alebo signálov z prostredia.

Podrobnejšie preskúmame, kedy (a kedy *nie*) použiť AI agentov v lekcii **Budovanie dôveryhodných AI agentov** neskôr v kurze.

---

## Základy agentických riešení

### Vývoj agenta

Prvou vecou pri budovaní agenta je definovať, *čo dokáže* — jeho nástroje, akcie a správanie.

V tomto kurze používame ako hlavnú platformu **Azure AI Agent Service**. Podporuje:

- Modely od poskytovateľov ako OpenAI, Mistral, a Meta (Llama)
- Licencované údaje od poskytovateľov ako Tripadvisor
- Štandardizované definície nástrojov OpenAPI 3.0

### Agentické vzory

S LLM komunikujete pomocou výziev (promptov). Pri agentoch nemôžete vždy ručne skladať každý prompt — agent musí konať cez viacero krokov. Tu prichádzajú na scénu **agentické vzory**. Sú to opakovane použiteľné stratégie na promptovanie a koordináciu LLM spôsobom, ktorý je škálovateľnejší a spoľahlivejší.

Tento kurz je postavený na najbežnejších a najpoužívanejších agentických vzoroch.

### Agentické rámce

Agentické rámce dávajú vývojárom hotové šablóny, nástroje a infraštruktúru na tvorbu agentov. Uľahčujú:

- Prepojenie nástrojov a schopností
- Monitorovanie činností agenta (a ladenie problémov)
- Spoluprácu viacerých agentov

V tomto kurze sa zameriavame na **Microsoft Agent Framework (MAF)** pre tvorbu produkčne pripravených agentov.

---

## Ukážky kódu

Pripravení vidieť to v praxi? Tu sú ukážky kódu pre túto lekciu:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Máte otázky?

Pridajte sa do [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) a spojte sa s ostatnými študentmi, zúčastnite sa konzultačných hodín a získajte odpovede na otázky o AI agentoch od komunity.

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