# Inžinierstvo kontextu pre AI agentov

[![Inžinierstvo kontextu](../../../translated_images/sk/lesson-12-thumbnail.ed19c94463e774d4.webp)](https://youtu.be/F5zqRV7gEag)

> _(Kliknite na obrázok vyššie pre zobrazenie videa z tejto lekcie)_

Pochopenie komplexnosti aplikácie, pre ktorú vytvárate AI agenta, je dôležité pre vytvorenie spoľahlivého agenta. Musíme vytvárať AI agentov, ktorí efektívne spravujú informácie, aby zvládli zložité požiadavky presahujúce samotné prompt engineering.

V tejto lekcii si pozrieme, čo je to inžinierstvo kontextu a jeho úlohu pri vytváraní AI agentov.

## Úvod

Táto lekcia pokryje:

• **Čo je inžinierstvo kontextu** a prečo sa líši od prompt engineering.

• **Stratégie efektívneho inžinierstva kontextu**, vrátane spôsobov, ako písať, vyberať, komprimovať a izolovať informácie.

• **Bežné zlyhania kontextu**, ktoré môžu prekazit váš AI agent a ako ich opraviť.

## Ciele učenia

Po dokončení tejto lekcie budete vedieť, ako:

• **Definovať inžinierstvo kontextu** a odlíšiť ho od prompt engineering.

• **Identifikovať kľúčové komponenty kontextu** v aplikáciách založených na veľkých jazykových modeloch (LLM).

• **Použiť stratégie písania, výberu, komprimácie a izolácie kontextu** na zlepšenie výkonu agenta.

• **Rozpoznať bežné zlyhania kontextu** ako otrava, rozptýlenie, zmätok a konflikt, a implementovať techniky ich zmiernenia.

## Čo je inžinierstvo kontextu?

Pre AI agentov je kontext tým, čo riadi plánovanie agenta vykonať určité akcie. Inžinierstvo kontextu je prax zabezpečiť, aby AI agent mal správne informácie na dokončenie ďalšieho kroku úlohy. Kontextové okno je obmedzené veľkosťou, takže ako tvorcovia agentov musíme budovať systémy a procesy na správu pridávania, odstraňovania a zhutňovania informácií v kontextovom okne.

### Prompt engineering vs Inžinierstvo kontextu

Prompt engineering sa zameriava na jeden statický súbor inštrukcií na efektívne usmernenie AI agentov pomocou súboru pravidiel. Inžinierstvo kontextu je o správe dynamického súboru informácií, vrátane počiatočného promptu, aby agent mal to, čo potrebuje v priebehu času. Hlavnou myšlienkou inžinierstva kontextu je spraviť tento proces opakovateľným a spoľahlivým.

### Typy kontextu

[![Typy kontextu](../../../translated_images/sk/context-types.fc10b8927ee43f06.webp)](https://youtu.be/F5zqRV7gEag)

Je dôležité si zapamätať, že kontext nie je len jedna vec. Informácie, ktoré AI agent potrebuje, môžu pochádzať z rôznych zdrojov a našou úlohou je zabezpečiť, aby agent mal prístup k týmto zdrojom:

Typy kontextu, ktoré môže AI agent potrebovať spravovať, zahŕňajú:

• **Inštrukcie:** Sú to akési "pravidlá" agenta – prompty, systémové správy, príklady few-shot (ukazujúce AI, ako niečo robiť) a popisy nástrojov, ktoré môže používať. Tu sa stretáva prompt engineering s inžinierstvom kontextu.

• **Znalosti:** Zahŕňa fakty, informácie získané z databáz alebo dlhodobé spomienky, ktoré agent nahromadil. To zahŕňa aj integráciu systému Retrieval Augmented Generation (RAG), ak agent potrebuje prístup k rôznym úložiskám znalostí a databázam.

• **Nástroje:** Sú to definície externých funkcií, API a MCP serverov, ktoré agent môže volať, spolu so spätnou väzbou (výsledkami) z ich použitia.

• **História konverzácie:** Prebiehajúci dialóg s používateľom. Ako čas plynie, tieto rozhovory sa predlžujú a komplikujú, čo znamená, že zaberajú miesto v kontextovom okne.

• **Preferencie používateľa:** Informácie o tom, čo má používateľ rád alebo nemá rád, získané v priebehu času. Tieto môžu byť uložené a volané pri dôležitých rozhodnutiach na pomoc používateľovi.

## Stratégie efektívneho inžinierstva kontextu

### Plánovacie stratégie

[![Najlepšie praktiky inžinierstva kontextu](../../../translated_images/sk/best-practices.f4170873dc554f58.webp)](https://youtu.be/F5zqRV7gEag)

Dobrý základ inžinierstva kontextu začína dobrým plánovaním. Toto je prístup, ktorý vám pomôže začať premýšľať o tom, ako aplikovať koncept inžinierstva kontextu:

1. **Definujte jasné výsledky** – výsledky úloh, ktoré budú AI agentom pridelené, by mali byť jasne definované. Odpovedzte na otázku – „Ako bude vyzerať svet, keď AI agent skončí svoju úlohu?“ Inými slovami, aká zmena, informácia alebo odpoveď by mala byť pre používateľa po interakcii s AI agentom.
2. **Mapujte kontext** – Keď máte definované výsledky AI agenta, musíte odpovedať na otázku „Aké informácie agent potrebuje na dokončenie tejto úlohy?“ Toto umožní začať mapovať kontext a kde by sa tieto informácie mohli nachádzať.
3. **Vytvorte kontextové pipeline-y** – Keď viete, kde sú informácie, musíte odpovedať na otázku „Ako agent získa tieto informácie?“ Toto sa dá riešiť rôznymi spôsobmi, vrátane RAG, využitia MCP serverov a iných nástrojov.

### Praktické stratégie

Plánovanie je dôležité, ale keď sa informácie začnú hromadiť v kontextovom okne nášho agenta, potrebujeme praktické stratégie, ako ich spravovať:

#### Správa kontextu

Kým niektoré informácie sa pridávajú do kontextového okna automaticky, inžinierstvo kontextu znamená aktívnejšie riadiť tieto informácie, čo sa dá urobiť niekoľkými stratégiami:

 1. **Poznámkový blok agenta (Agent Scratchpad)**
 Tento umožňuje AI agentovi robiť si poznámky o relevantných informáciách o aktuálnych úlohách a interakciách s používateľom počas jednej relácie. Mal by existovať mimo kontextového okna, napríklad v súbore alebo runtime objekte, ktorý si agent môže neskôr vyhľadať počas tejto relácie, ak je to potrebné.

 2. **Spomienky (Memories)**
 Poznámkové bloky sú vhodné na správu informácií mimo kontextového okna jednej relácie. Spomienky umožňujú agentom ukladať a vyhľadávať relevantné informácie naprieč viacerými reláciami. Môžu zahŕňať zhrnutia, preferencie používateľa a spätnú väzbu pre budúce vylepšenia.

 3. **Komprimácia kontextu**
  Keď kontextové okno rastie a blíži sa k limitu, môžu sa použiť techniky ako zhrnutie a orezanie. Zahŕňa to buď ponechanie iba najrelevantnejších informácií alebo odstránenie starších správ.
  
 4. **Systémy viacerých agentov**
  Vývoj viacagentových systémov je formou inžinierstva kontextu, pretože každý agent má svoje vlastné kontextové okno. Ako sa tento kontext zdieľa a prenáša medzi rôznymi agentmi, je ďalšou vecou, ktorú treba naplánovať pri vytváraní týchto systémov.
  
 5. **Sandboxové prostredia**
  Ak agent potrebuje spustiť nejaký kód alebo spracovať veľké množstvo informácií v dokumente, môže to vyžadovať veľa tokenov na spracovanie výsledkov. Namiesto toho, aby boli všetky uložené v kontextovom okne, agent môže použiť sandboxové prostredie, ktoré dokáže kód spustiť a načítať iba výsledky a ďalšie relevantné informácie.
  
 6. **Objekty stavu runtime (Runtime State Objects)**
   Toto sa robí vytvorením kontajnerov informácií na riadenie situácií, keď agent potrebuje mať prístup k určitým informáciám. Pri zložitej úlohe to umožní agentovi ukladať výsledky každej podúlohy krok za krokom, čo umožní, aby kontext zostal pripojený iba k tej konkrétnej podúlohe.

#### Kontrola kontextu

Po aplikovaní jednej z týchto stratégií stojí za to skontrolovať, čo ďalší modelový dotaz vlastne obdržal. Užitečnou otázkou na ladenie je:

> Nahrala agent príliš veľa kontextu, zlý kontext alebo mu chýbal kontext, ktorý potreboval?

Na odpoveď na túto otázku nie je potrebné zaznamenávať surové prompty, výstupy nástrojov alebo obsah pamäti. V produkcii uprednostňujte malé záznamy kontroly kontextu, ktoré zachytávajú počty, ID, hašy a štítky politiky:

- **Výber:** Sledujte, koľko kandidátskych kúskov, nástrojov alebo pamätí bolo zvážených, koľko bolo vybraných a ktoré pravidlo alebo skóre spôsobilo filtrovanie ostatných.
- **Kompresia:** Zaznamenajte rozsah zdroja alebo ID stopy, ID zhrnutia, odhadovaný počet tokenov pred a po kompresii a či bol surový obsah vynechaný z ďalšieho volania.
- **Izolácia:** Poznačte, ktorá podúloha bežala v samostatnom agentovi, relácii alebo sandboxe, aké ohraničené zhrnutie bolo vrátené a či veľké výstupy nástroja zostali mimo rodičovský kontext agenta.
- **Pamäť a RAG:** Ukladajte ID dokumentov vyhľadávania, ID pamäte, skóre, vybrané ID a stav cenzúry namiesto plného vyhľadaného textu.
- **Bezpečnosť a súkromie:** Uprednostňujte haše, ID, tokenové vedrá a štítky politiky namiesto citlivého textu promptu, argumentov nástroja, výsledkov nástroja alebo obsahu používateľskej pamäte.

Cieľom nie je uchovávať viac kontextu. Cieľom je zanechať dostatok dôkazov, aby vývojár mohol povedať, ktorá stratégia kontextu bola použitá a či zmenila ďalší modelový dotaz zamýšľaným spôsobom.

### Príklad inžinierstva kontextu

Povedzme, že chceme, aby AI agent **„Zarezervoval mi výlet do Paríža.“**

• Jednoduchý agent používajúci iba prompt engineering by mohol len odpovedať: **„Dobre, kedy by ste chceli ísť do Paríža?“**. Spracoval len vašu priamu otázku v čase, keď ste sa opýtali.

• Agent používajúci stratégie inžinierstva kontextu by urobil oveľa viac. Skôr, než odpovie, jeho systém by mohol:

  ◦ **Skontrolovať váš kalendár** pre dostupné dátumy (získanie údajov v reálnom čase).

 ◦ **Pripomenúť si predchádzajúce preferencie cestovania** (z dlhodobej pamäte), ako vaša obľúbená letecká spoločnosť, rozpočet alebo či uprednostňujete priame lety.

 ◦ **Identifikovať dostupné nástroje** na rezerváciu leteniek a hotelov.

- Potom môže byť odpoveďou napríklad: „Ahoj [Vaše meno]! Vidím, že máte voľno v prvom týždni októbra. Mám vyhľadávať priame lety do Paríža s [preferovanou leteckou spoločnosťou] v rámci vášho obvyklého rozpočtu [rozpočet]?“. Táto bohatšia, na kontexte založená odpoveď demonštruje silu inžinierstva kontextu.

## Bežné zlyhania kontextu

### Otrava kontextu

**Čo to je:** Keď halucinácia (nepravdivá informácia generovaná LLM) alebo chyba vstúpi do kontextu a je opakovane spomínaná, čo spôsobuje, že agent sleduje nemožné ciele alebo vyvíja nezmyselné stratégie.

**Čo robiť:** Implementujte **validáciu kontextu** a **karanténu**. Overte informácie pred ich pridaním do dlhodobej pamäte. Ak sa detekuje možná otrava, začnite nové vlákna kontextu, aby sa zabránilo šíreniu zlých informácií.

**Príklad rezervácie cestovania:** Váš agent halucinuje **priamy let z malého miestneho letiska do vzdialeného medzinárodného mesta**, ktoré v skutočnosti medzinárodné lety neponúka. Tento neexistujúci detail letu sa uloží do kontextu. Neskôr, keď požiadajte agenta o rezerváciu, pokračuje v snahe nájsť letenky na tejto nemožnej trase, čo vedie k opakovaným chybám.

**Riešenie:** Zaveďte krok, ktorý **overí existenciu letu a trasy pomocou API v reálnom čase** _predtým_, než sa detail letu pridá do pracovného kontextu agenta. Ak overenie zlyhá, chybná informácia je „karanténovaná“ a ďalej nepoužívaná.

### Rozptýlenie kontextu

**Čo to je:** Keď kontext rastie tak veľký, že model sa príliš zameriava na nahromadenú históriu namiesto toho, čo sa naučil počas tréningu, čo vedie k opakujúcim sa alebo nepomocným akciám. Modely môžu začať robiť chyby ešte predtým, než je kontextové okno plné.

**Čo robiť:** Používajte **zhrnutie kontextu**. Pravidelne komprimujte nahromadené informácie do kratších zhrnutí, ktoré zachovávajú dôležité detaily a odstraňujú redundantnú históriu. Pomáha to „resetovať“ zameranie.

**Príklad rezervácie cestovania:** Dlho ste diskutovali o rôznych vysnívaných cestovateľských cieľoch vrátane podrobného rozprávania o vašej batohovej ceste spred dvoch rokov. Keď nakoniec požiadate **„nájdi mi lacný let na budúci mesiac“**, agent sa zamotá do starých, nerelevantných detailov a stále sa pýta na výbavu na batohovanie alebo minulé itineráre, zanedbávajúc vašu aktuálnu požiadavku.

**Riešenie:** Po určitej počte odoziev alebo keď kontext rastie príliš veľký by mal agent **zhrnúť najnovšie a najrelevantnejšie časti konverzácie** – zameriavajúc sa na aktuálne dátumy cesty a cieľ – a použiť toto skondenzované zhrnutie pre ďalšie volanie LLM, pričom menej relevantné historické časti rozhovoru zahodí.

### Zmätok kontextu

**Čo to je:** Keď zbytočný kontext, často vo forme príliš veľa dostupných nástrojov, spôsobuje, že model generuje zlé odpovede alebo volá nerelevantné nástroje. Najmä menšie modely sú na to náchylné.

**Čo robiť:** Zaviesť **správu výberu nástrojov** pomocou RAG techník. Ukladajte popisy nástrojov do vektorovej databázy a vyberajte _len_ najrelevantnejšie nástroje pre každú špecifickú úlohu. Výskumy ukazujú, že je vhodné obmedziť výber nástrojov na menej ako 30.

**Príklad rezervácie cestovania:** Váš agent má prístup k desiatkam nástrojov: `book_flight`, `book_hotel`, `rent_car`, `find_tours`, `currency_converter`, `weather_forecast`, `restaurant_reservations`, atď. Pýtate sa, **„Aký je najlepší spôsob, ako sa pohybovať po Paríži?“** Kvôli množstvu nástrojov sa agent zamotá a pokúša sa volať `book_flight` _v rámci_ Paríža alebo `rent_car`, hoci uprednostňujete verejnú dopravu, pretože popisy nástrojov sa môžu prekrývať alebo jednoducho nedokáže správne vybrať ten najlepší.

**Riešenie:** Použite **RAG na popisy nástrojov**. Keď sa pýtate na pohyb po Paríži, systém dynamicky vyhľadá _len_ najrelevantnejšie nástroje ako `rent_car` alebo `public_transport_info` na základe vášho dotazu a predstaví LLM sústredený „výber“ nástrojov.

### Konflikt kontextu

**Čo to je:** Keď v kontexte existujú protichodné informácie, ktoré vedú k nekonzistentnému uvažovaniu alebo zlým konečným odpovediam. Často sa to stáva, keď informácie prichádzajú etapovite a skoré nesprávne predpoklady zostávajú v kontexte.

**Čo robiť:** Používajte **prerezávanie kontextu** a **presun mimo hlavný kontext**. Prerezávanie znamená odstránenie zastaraných alebo protichodných informácií, keď prichádzajú nové detaily. Presun mimo hlavný kontext poskytuje modelu samostatný pracovný priestor („scratchpad“) na spracovanie informácií bez zahlcovania hlavného kontextu.


**Príklad rezervácie cestovania:** Najskôr poviete svojmu agentovi, **„Chcem lietať v ekonomickej triede.“** Neskôr v rozhovore zmeníte názor a poviete, **„Vlastne na túto cestu poďme business triedu.“** Ak obe pokyny zostanú v kontexte, agent môže dostať protichodné výsledky vyhľadávania alebo môže byť zmätený, ktorú preferenciu uprednostniť.

**Riešenie:** Implementujte **ořezávanie kontextu**. Keď nová inštrukcia protirečí starej, staršia inštrukcia sa odstráni alebo v kontexte výslovne prekoná. Alternatívne agent môže použiť **poznámkový blok** na zladenie protichodných preferencií pred rozhodnutím, čím sa zabezpečí, že jeho činnosťami bude riadiť len konečný, konzistentný pokyn.

## Máte viac otázok o inžinierstve kontextu?

Pripojte sa k [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), aby ste sa stretli s ďalšími študentmi, zúčastnili sa konzultácií a dostali odpovede na svoje otázky o AI agentoch.
## Predchádzajúca lekcia

[Agentic Protocols](../11-agentic-protocols/README.md)

## Nasledujúca lekcia

[Pamäť pre AI agentov](../13-agent-memory/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->