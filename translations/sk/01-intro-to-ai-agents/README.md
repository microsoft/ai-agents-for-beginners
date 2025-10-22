<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1e40fe956ff79462a02a17080b125041",
  "translation_date": "2025-08-29T20:30:59+00:00",
  "source_file": "01-intro-to-ai-agents/README.md",
  "language_code": "sk"
}
-->
[![Úvod do AI agentov](../../../translated_images/lesson-1-thumbnail.d21b2c34b32d35bbc7f1b4a40a81b031970b6076b4e0c59fb006cf818cac5d4a.sk.png)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Kliknite na obrázok vyššie a pozrite si video k tejto lekcii)_

# Úvod do AI agentov a ich využitia

Vitajte v kurze "AI Agenti pre začiatočníkov"! Tento kurz poskytuje základné znalosti a praktické príklady na vytváranie AI agentov.

Pripojte sa k [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), aby ste sa stretli s ostatnými študentmi a tvorcami AI agentov a mohli klásť otázky týkajúce sa tohto kurzu.

Na začiatku kurzu sa zameriame na lepšie pochopenie toho, čo sú AI agenti a ako ich môžeme využiť v aplikáciách a pracovných postupoch, ktoré vytvárame.

## Úvod

Táto lekcia pokrýva:

- Čo sú AI agenti a aké sú ich rôzne typy?
- Aké prípady použitia sú najvhodnejšie pre AI agentov a ako nám môžu pomôcť?
- Aké sú základné stavebné bloky pri navrhovaní agentických riešení?

## Ciele učenia
Po dokončení tejto lekcie by ste mali byť schopní:

- Pochopiť koncepty AI agentov a ako sa líšia od iných AI riešení.
- Efektívne aplikovať AI agentov.
- Produktívne navrhovať agentické riešenia pre používateľov aj zákazníkov.

## Definovanie AI agentov a typy AI agentov

### Čo sú AI agenti?

AI agenti sú **systémy**, ktoré umožňujú **veľkým jazykovým modelom (LLMs)** **vykonávať akcie** tým, že rozširujú ich schopnosti a poskytujú im **prístup k nástrojom** a **vedomostiam**.

Rozdeľme túto definíciu na menšie časti:

- **Systém** - Je dôležité myslieť na agentov nie ako na jeden komponent, ale ako na systém mnohých komponentov. Základné komponenty AI agenta sú:
  - **Prostredie** - Definovaný priestor, v ktorom AI agent operuje. Napríklad, ak máme AI agenta na rezerváciu cestovania, prostredie môže byť rezervačný systém, ktorý agent používa na vykonávanie úloh.
  - **Senzory** - Prostredia poskytujú informácie a spätnú väzbu. AI agenti používajú senzory na zhromažďovanie a interpretáciu informácií o aktuálnom stave prostredia. V prípade cestovného agenta môže systém poskytovať informácie, ako je dostupnosť hotelov alebo ceny letov.
  - **Aktuátory** - Keď AI agent získa aktuálny stav prostredia, určí, akú akciu vykonať, aby zmenil prostredie. Pre cestovného agenta to môže byť rezervácia dostupnej izby pre používateľa.

![Čo sú AI agenti?](../../../translated_images/what-are-ai-agents.1ec8c4d548af601a3a78c6c02e5c355d19c06a4a74fe93e3609a1d08e8c15689.sk.png)

**Veľké jazykové modely** - Koncept agentov existoval už pred vznikom LLMs. Výhodou budovania AI agentov s LLMs je ich schopnosť interpretovať ľudský jazyk a dáta. Táto schopnosť umožňuje LLMs interpretovať informácie z prostredia a definovať plán na jeho zmenu.

**Vykonávanie akcií** - Mimo systémov AI agentov sú LLMs obmedzené na situácie, kde akcia spočíva v generovaní obsahu alebo informácií na základe používateľského podnetu. V rámci systémov AI agentov môžu LLMs plniť úlohy interpretáciou požiadaviek používateľa a využívaním nástrojov dostupných v ich prostredí.

**Prístup k nástrojom** - Aké nástroje má LLM k dispozícii, je definované 1) prostredím, v ktorom operuje, a 2) vývojárom AI agenta. V našom príklade cestovného agenta sú nástroje obmedzené operáciami dostupnými v rezervačnom systéme, prípadne vývojár môže obmedziť prístup agenta k nástrojom na lety.

**Pamäť + vedomosti** - Pamäť môže byť krátkodobá v kontexte konverzácie medzi používateľom a agentom. Dlhodobo, mimo informácií poskytovaných prostredím, môžu AI agenti získavať vedomosti z iných systémov, služieb, nástrojov a dokonca aj od iných agentov. V prípade cestovného agenta by tieto vedomosti mohli zahŕňať informácie o preferenciách používateľa uložené v zákazníckej databáze.

### Rôzne typy agentov

Teraz, keď máme všeobecnú definíciu AI agentov, pozrime sa na konkrétne typy agentov a ako by sa mohli aplikovať na cestovného agenta.

| **Typ agenta**                | **Popis**                                                                                                                       | **Príklad**                                                                                                                                                                                                                   |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Jednoduchí reflexní agenti**      | Vykonávajú okamžité akcie na základe preddefinovaných pravidiel.                                                                 | Cestovný agent interpretuje kontext e-mailu a presmeruje sťažnosti na cestovanie na zákaznícky servis.                                                                                                                          |
| **Modelovo založení reflexní agenti** | Vykonávajú akcie na základe modelu sveta a zmien v tomto modeli.                                                               | Cestovný agent uprednostňuje trasy s výraznými zmenami cien na základe prístupu k historickým údajom o cenách.                                                                                                             |
| **Cieľovo orientovaní agenti**         | Vytvárajú plány na dosiahnutie konkrétnych cieľov interpretáciou cieľa a určením akcií na jeho dosiahnutie.                     | Cestovný agent rezervuje cestu určením potrebných cestovných opatrení (auto, verejná doprava, lety) z aktuálnej polohy do cieľovej destinácie.                                                                                |
| **Agenti založení na užitočnosti**      | Zohľadňujú preferencie a numericky vyvažujú kompromisy, aby určili, ako dosiahnuť ciele.                                       | Cestovný agent maximalizuje užitočnosť vyvažovaním pohodlia a nákladov pri rezervácii cestovania.                                                                                                                                          |
| **Učiaci sa agenti**           | Zlepšujú sa časom reagovaním na spätnú väzbu a prispôsobovaním akcií.                                                             | Cestovný agent sa zlepšuje na základe spätnej väzby od zákazníkov z dotazníkov po ceste, aby upravil budúce rezervácie.                                                                                                               |
| **Hierarchickí agenti**       | Obsahujú viacero agentov v hierarchickom systéme, kde agenti na vyššej úrovni rozdeľujú úlohy na podúlohy pre agentov na nižšej úrovni. | Cestovný agent ruší cestu rozdelením úlohy na podúlohy (napríklad zrušenie konkrétnych rezervácií) a agenti na nižšej úrovni ich vykonávajú, pričom podávajú správy agentovi na vyššej úrovni.                                     |
| **Systémy viacerých agentov (MAS)** | Agenti vykonávajú úlohy nezávisle, buď kooperatívne alebo konkurenčne.                                                          | Kooperatívne: Viacerí agenti rezervujú konkrétne cestovné služby, ako sú hotely, lety a zábava. Konkurenčne: Viacerí agenti spravujú a súťažia o zdieľaný kalendár rezervácií hotelov, aby rezervovali zákazníkov do hotela. |

## Kedy používať AI agentov

V predchádzajúcej časti sme použili prípad použitia cestovného agenta na vysvetlenie, ako sa rôzne typy agentov môžu použiť v rôznych scenároch rezervácie cestovania. Tento príklad budeme používať počas celého kurzu.

Pozrime sa na typy prípadov použitia, na ktoré sú AI agenti najvhodnejší:

![Kedy používať AI agentov?](../../../translated_images/when-to-use-ai-agents.54becb3bed74a479f5caca9c951132ce81d482a6704bcd22e5a600dbabc9434e.sk.png)

- **Otvorené problémy** - umožnenie LLM určiť potrebné kroky na dokončenie úlohy, pretože ich nie je vždy možné pevne zakódovať do pracovného postupu.
- **Viackrokové procesy** - úlohy, ktoré vyžadujú určitú úroveň zložitosti, pri ktorej AI agent potrebuje používať nástroje alebo informácie počas viacerých krokov namiesto jednorazového získania.
- **Zlepšovanie časom** - úlohy, pri ktorých sa agent môže zlepšovať časom na základe spätnej väzby od prostredia alebo používateľov, aby poskytoval lepšiu užitočnosť.

Viac úvah o používaní AI agentov pokrývame v lekcii Budovanie dôveryhodných AI agentov.

## Základy agentických riešení

### Vývoj agentov

Prvým krokom pri navrhovaní systému AI agenta je definovanie nástrojov, akcií a správania. V tomto kurze sa zameriavame na používanie **Azure AI Agent Service** na definovanie našich agentov. Ponúka funkcie ako:

- Výber otvorených modelov, ako sú OpenAI, Mistral a Llama
- Používanie licencovaných údajov prostredníctvom poskytovateľov, ako je Tripadvisor
- Používanie štandardizovaných nástrojov OpenAPI 3.0

### Agentické vzory

Komunikácia s LLMs prebieha prostredníctvom podnetov. Vzhľadom na poloautonómnu povahu AI agentov nie je vždy možné alebo potrebné manuálne opätovne podnietiť LLM po zmene prostredia. Používame **agentické vzory**, ktoré nám umožňujú podnietiť LLM počas viacerých krokov škálovateľnejším spôsobom.

Tento kurz je rozdelený na niektoré z aktuálne populárnych agentických vzorov.

### Agentické rámce

Agentické rámce umožňujú vývojárom implementovať agentické vzory prostredníctvom kódu. Tieto rámce ponúkajú šablóny, pluginy a nástroje na lepšiu spoluprácu AI agentov. Tieto výhody poskytujú schopnosti na lepšiu pozorovateľnosť a riešenie problémov systémov AI agentov.

V tomto kurze preskúmame výskumom podložený rámec AutoGen a produkčne pripravený rámec Agent od Semantic Kernel.

### Máte ďalšie otázky o AI agentoch?

Pripojte sa k [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), aby ste sa stretli s ostatnými študentmi, zúčastnili sa konzultačných hodín a získali odpovede na vaše otázky o AI agentoch.

## Predchádzajúca lekcia

[Nastavenie kurzu](../00-course-setup/README.md)

## Nasledujúca lekcia

[Preskúmanie agentických rámcov](../02-explore-agentic-frameworks/README.md)

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.