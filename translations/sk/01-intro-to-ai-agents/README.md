[![Úvod do AI agentov](../../../translated_images/sk/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Kliknite na obrázok vyššie pre zobrazenie videa tejto lekcie)_


# Úvod do AI agentov a prípadov použitia

Vitajte v kurze "AI Agents for Beginners"! Tento kurz poskytuje základné znalosti a praktické ukážky pre tvorbu AI agentov.

Pridajte sa do <a href="https://discord.gg/kzRShWzttr" target="_blank">komunity Azure AI na Discorde</a>, aby ste sa stretli s ďalšími študentmi a tvorcami AI agentov a položili všetky otázky týkajúce sa tohto kurzu.

Na začiatku tohto kurzu si najprv lepšie objasníme, čo sú AI agenti a ako ich môžeme využiť v aplikáciách a pracovných postupoch, ktoré vytvárame.

## Úvod

Táto lekcia zahŕňa:

- Čo sú AI agenti a aké sú rôzne typy agentov?
- Pre aké prípady použitia sú AI agenti najvhodnejší a ako nám môžu pomôcť?
- Aké sú niektoré základné stavebné prvky pri navrhovaní agentických riešení?

## Ciele učenia
Po dokončení tejto lekcie by ste mali byť schopní:

- Pochopiť koncepty AI agentov a ako sa líšia od iných AI riešení.
- Efektívne aplikovať AI agentov.
- Produktívne navrhovať agentické riešenia pre používateľov a zákazníkov.

## Definovanie AI agentov a typy AI agentov

### Čo sú to AI agenti?

AI agenti sú **systémy**, ktoré umožňujú **veľkým jazykovým modelom (LLMs)** **vykonávať akcie** tým, že rozširujú ich schopnosti a poskytujú LLM prístup k **nástrojom** a **vedomostiam**.

Rozoberme túto definíciu na menšie časti:

- **Systém** - Je dôležité vnímať agentov nie len ako jeden komponent, ale ako systém mnohých komponentov. Na základnej úrovni sú zložky AI agenta:
  - **Prostredie** - Definovaný priestor, v ktorom AI agent operuje. Napríklad, ak by sme mali AI agenta na rezerváciu ciest, prostredím by mohol byť rezervačný systém, ktorý AI agent využíva na dokončenie úloh.
  - **Senzory** - Prostredia obsahujú informácie a poskytujú spätnú väzbu. AI agenti používajú senzory na zhromažďovanie a interpretáciu týchto informácií o aktuálnom stave prostredia. V príklade cestovného agenta môže rezervačný systém poskytovať informácie, ako je dostupnosť hotelov alebo ceny letov.
  - **Aktuátory** - Keď AI agent získa aktuálny stav prostredia, pre danú úlohu určí, akú akciu vykonať na zmenu prostredia. Pre cestovného agenta to môže byť rezervácia dostupnej izby pre používateľa.

![Čo sú AI agenti?](../../../translated_images/sk/what-are-ai-agents.1ec8c4d548af601a.webp)

**Veľké jazykové modely (LLMs)** - Koncept agentov existoval ešte pred vznikom LLM. Výhodou stavby AI agentov s LLM je ich schopnosť interpretovať ľudský jazyk a údaje. Táto schopnosť umožňuje LLM interpretovať informácie z prostredia a definovať plán na zmenu prostredia.

**Vykonávanie akcií** - Mimo systémov AI agentov sú LLM obmedzené na situácie, kde je akciou generovanie obsahu alebo informácií na základe výzvy používateľa. V systémoch AI agentov môžu LLM plniť úlohy interpretáciou požiadavky používateľa a použitím nástrojov dostupných v ich prostredí.

**Prístup k nástrojom** - To, ku ktorým nástrojom má LLM prístup, určuje 1) prostredie, v ktorom operuje, a 2) vývojár AI agenta. V našom príklade cestovného agenta sú nástroje agenta obmedzené operáciami dostupnými v rezervačnom systéme, a/alebo vývojár môže obmedziť prístup agenta len na lety.

**Pamäť + Vedomosti** - Pamäť môže byť krátkodobá v kontexte rozhovoru medzi používateľom a agentom. Dlhodobo, mimo informácií poskytovaných prostredím, AI agenti môžu tiež získavať vedomosti z iných systémov, služieb, nástrojov a dokonca aj od iných agentov. V príklade cestovného agenta by tieto vedomosti mohli byť informácie o preferenciách cestovania používateľa uložené v databáze zákazníka.

### Rôzne typy agentov

Teraz, keď máme všeobecnú definíciu AI agentov, pozrime sa na niektoré konkrétne typy agentov a ako by sa ich dalo aplikovať na cestovného agenta.

| **Typ agenta**                | **Popis**                                                                                                                       | **Príklad**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Jednoduché reflexné agenty**      | Vykonávajú okamžité akcie na základe preddefinovaných pravidiel.                                                                                  | Cestovný agent interpretuje kontext e-mailu a presmeruje sťažnosti týkajúce sa ciest na zákaznícky servis.                                                                                                                          |
| **Reflexné agenti založené na modeli** | Vykonávajú akcie založené na modeli sveta a zmenách tohto modelu.                                                              | Cestovný agent uprednostňuje trasy so značnými zmenami cien na základe prístupu k historickým údajom o cenách.                                                                                                             |
| **Agenti orientovaní na ciele**         | Vytvárajú plány na dosiahnutie konkrétnych cieľov interpretáciou cieľa a určením krokov na jeho dosiahnutie.                                  | Cestovný agent rezervuje cestu tým, že určí potrebné cestovné usporiadania (auto, verejná doprava, lety) z aktuálnej lokality do cieľa.                                                                                |
| **Agenti založení na užitočnosti**      | Zohľadňujú preferencie a numericky vážia kompromisy, aby rozhodli, ako dosiahnuť ciele.                                               | Cestovný agent maximalizuje užitočnosť vážením pohodlia oproti nákladom pri rezervácii cesty.                                                                                                                                          |
| **Učiace sa agenti**           | Zlepšujú sa v priebehu času reagovaním na spätnú väzbu a úpravou svojich akcií.                                                        | Cestovný agent sa zlepšuje využívaním spätnej väzby od zákazníkov z prieskumov po ceste a upravuje budúce rezervácie.                                                                                                               |
| **Hierarchické agenti**       | Obsahujú viacerých agentov v vrstvenom systéme, pričom vyššie úrovne rozdeľujú úlohy na podúlohy pre nižšie úrovne. | Cestovný agent zruší výlet tak, že rozdelí úlohu na podúlohy (napríklad zrušenie konkrétnych rezervácií) a nechá nižšie úrovne agentov ich vykonať a nahlásiť späť vyššiemu agentovi.                                     |
| **Viacagentové systémy (MAS)** | Agenti dokončujú úlohy nezávisle, buď kooperatívne alebo konkurenčne.                                                           | Kooperatívne: Viac agentov rezervuje konkrétne cestovné služby, ako sú hotely, lety a zábava. Konkurenčné: Viac agentov spravuje a súťaží o spoločný rezervačný kalendár hotela, aby rezervovali zákazníkov do hotela. |

## Kedy použiť AI agentov

V predchádzajúcej časti sme použili prípad použitia cestovného agenta na vysvetlenie, ako sa rôzne typy agentov môžu použiť v rôznych scenároch rezervácie ciest. Tento príklad budeme naďalej používať v celom kurze.

Pozrime sa na typy prípadov použitia, pri ktorých sú AI agenti najvhodnejší:

![Kedy použiť AI agentov?](../../../translated_images/sk/when-to-use-ai-agents.54becb3bed74a479.webp)


- **Otvorené problémy** - umožniť LLM určiť potrebné kroky na dokončenie úlohy, pretože to nemožno vždy napevno zakódovať do pracovného postupu.
- **Viacstupňové procesy** - úlohy, ktoré vyžadujú určitú úroveň zložitosti, pri ktorej agent musí používať nástroje alebo informácie počas viacerých krokov namiesto jednorazového získania.  
- **Zlepšovanie v priebehu času** - úlohy, pri ktorých sa agent môže v priebehu času zlepšovať prijímaním spätnej väzby z prostredia alebo od používateľov, aby poskytoval lepšiu užitočnosť.

Viac úvah o používaní AI agentov pokrývame v lekcii Budovanie dôveryhodných AI agentov.

## Základy agentických riešení

### Vývoj agentov

Prvým krokom pri navrhovaní systému AI agenta je definovať nástroje, akcie a správanie. V tomto kurze sa zameriavame na použitie **Azure AI Agent Service** na definovanie našich agentov. Ponúka funkcie ako:

- Výber otvorených modelov, ako sú OpenAI, Mistral a Llama
- Použitie licencovaných údajov cez poskytovateľov, ako napríklad Tripadvisor
- Použitie štandardizovaných nástrojov OpenAPI 3.0

### Agentické vzory

Komunikácia s LLM prebieha prostredníctvom promptov. Vzhľadom na semiautomatickú povahu AI agentov nie je vždy možné alebo potrebné manuálne znovu spúšťať prompt LLM po zmene v prostredí. Používame **agentické vzory**, ktoré nám umožňujú promptovať LLM cez viacero krokov škálovateľnejším spôsobom.

Tento kurz je rozdelený podľa niektorých z aktuálne populárnych agentických vzorov.

### Agentické rámce

Agentické rámce umožňujú vývojárom implementovať agentické vzory prostredníctvom kódu. Tieto rámce ponúkajú šablóny, pluginy a nástroje pre lepšiu spoluprácu AI agentov. Tieto výhody poskytujú možnosti pre lepšiu pozorovateľnosť a riešenie problémov v systémoch AI agentov.

V tomto kurze preskúmame Microsoft Agent Framework (MAF) pre tvorbu produkčne pripravených AI agentov.

## Ukážkové kódy

- Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

## Máte ďalšie otázky o AI agentoch?

Pridajte sa k [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), aby ste sa stretli s ďalšími študentmi, zúčastnili sa konzultačných hodín a získali odpovede na svoje otázky o AI agentech.

## Predchádzajúca lekcia

[Course Setup](../00-course-setup/README.md)

## Nasledujúca lekcia

[Preskúmanie agentických rámcov](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vylúčenie zodpovednosti**:
Tento dokument bol preložený pomocou služby prekladu založenej na umelej inteligencii [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa usilujeme o presnosť, berte prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by sa mal považovať za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne výklady, ktoré môžu vzniknúť v dôsledku použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->