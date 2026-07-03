# Inžinierstvo kontextu pre AI agentov

[![Inžinierstvo kontextu](../../../translated_images/sk/lesson-12-thumbnail.ed19c94463e774d4.webp)](https://youtu.be/F5zqRV7gEag)

> _(Kliknite na obrázok vyššie pre prehranie videa tejto lekcie)_

Pochopenie zložitosti aplikácie, pre ktorú tvoríte AI agenta, je dôležité pre vytvorenie spoľahlivého agenta. Potrebujeme vyvíjať AI agentov, ktorí efektívne spravujú informácie, aby dokázali riešiť komplexné potreby, ktoré presahujú prompt engineering.

V tejto lekcii sa pozrieme na to, čo je inžinierstvo kontextu a akú úlohu zohráva pri vytváraní AI agentov.

## Úvod

Táto lekcia pokryje:

• **Čo je inžinierstvo kontextu** a prečo sa líši od prompt engineeringu.

• **Stratégie efektívneho inžinierstva kontextu**, vrátane spôsobov, ako písať, vyberať, komprimovať a izolovať informácie.

• **Bežné zlyhania kontextu**, ktoré môžu sabotovať váš AI agent a ako ich odstrániť.

## Ciele učenia

Po absolvovaní tejto lekcie budete vedieť:

• **Definovať inžinierstvo kontextu** a odlíšiť ho od prompt engineeringu.

• **Identifikovať kľúčové komponenty kontextu** v aplikáciách s veľkými jazykovými modelmi (LLM).

• **Použiť stratégie pre písanie, výber, kompresiu a izolovanie kontextu** na zlepšenie výkonu agenta.

• **Rozpoznať bežné zlyhania kontextu** ako otrava, rozptýlenie, zmätok či konflikt a uplatniť techniky ich zmiernenia.

## Čo je inžinierstvo kontextu?

Pre AI agentov je kontext tým, čo riadi plánovanie AI agenta k vykonaniu určitých akcií. Inžinierstvo kontextu je prax, vďaka ktorej AI agent disponuje správnymi informáciami na dokončenie ďalšieho kroku úlohy. Kontextové okno má obmedzenú veľkosť, preto ako tvorcovia agentov musíme vytvárať systémy a procesy na správu pridávania, odstraňovania a zjednocovania informácií v kontextovom okne.

### Prompt engineering vs inžinierstvo kontextu

Prompt engineering sa sústreďuje na jednu sadu statických inštrukcií na efektívne usmernenie AI agentov s pravidlami. Inžinierstvo kontextu sa zaoberá riadením dynamickej sady informácií, vrátane počiatočného promptu, aby mal AI agent v čase k dispozícii, čo potrebuje. Hlavnou myšlienkou inžinierstva kontextu je urobiť tento proces opakovateľným a spoľahlivým.

### Typy kontextu

[![Typy kontextu](../../../translated_images/sk/context-types.fc10b8927ee43f06.webp)](https://youtu.be/F5zqRV7gEag)

Je dôležité si pamätať, že kontext nie je len jedna vec. Informácie, ktoré AI agent potrebuje, môžu pochádzať z rôznych zdrojov a na nás je zabezpečiť, aby agent mal k týmto zdrojom prístup:

Typy kontextu, ktoré môže AI agent potrebovať spravovať, zahŕňajú:

• **Inštrukcie:** Sú ako "pravidlá" agenta – promptové správy, systémové správy, príklady few-shot (ukazujúce AI, ako niečo robiť) a popisy nástrojov, ktoré môže používať. Toto je oblasť, kde sa stretáva prompt engineering s inžinierstvom kontextu.

• **Znalosti:** Zahŕňajú fakty, informácie získané z databáz alebo dlhodobé spomienky, ktoré si agent uložil. To zahŕňa integráciu systému Retrieval Augmented Generation (RAG), ak agent potrebuje prístup k rôznym zdrojom znalostí a databázam.

• **Nástroje:** Definície externých funkcií, API a MCP serverov, ktoré môže agent volať, vrátane spätnej väzby (výsledky) z ich používania.

• **História konverzácie:** Prebiehajúci dialóg s používateľom. Ako čas plynie, tieto rozhovory sa predlžujú a stávajú sa zložitejšími, čo zaberá miesto v kontextovom okne.

• **Preferencie používateľa:** Informácie o obľube a neobľube používateľa, získané v priebehu času. Mohli by byť uložené a využité pri kľúčových rozhodnutiach na pomoc používateľovi.

## Stratégie efektívneho inžinierstva kontextu

### Plánovacie stratégie

[![Najlepšie praktiky inžinierstva kontextu](../../../translated_images/sk/best-practices.f4170873dc554f58.webp)](https://youtu.be/F5zqRV7gEag)

Dobrý základ inžinierstva kontextu je dobré plánovanie. Tu je prístup, ktorý vám pomôže začať uvažovať o tom, ako aplikovať koncept inžinierstva kontextu:

1. **Definujte jasné výsledky** – výsledky úloh, ktoré budú AI agentom pridelené, by mali byť jasne definované. Odpovedzte na otázku: „Ako bude svet vyzerať, keď AI agent dokončí svoju úlohu?“ Inými slovami, akú zmenu, informáciu alebo odpoveď by mal používateľ mať po interakcii s AI agentom.
2. **Zmapujte kontext** – keď máte definované výsledky AI agenta, musíte zodpovedať otázku: „Aké informácie potrebuje AI agent na dokončenie tejto úlohy?“ Takto môžete začať lokalizovať kontext, kde sa dané informácie nachádzajú.
3. **Vytvorte kontextové pipeline-y** – teraz, keď viete, kde sa informácie nachádzajú, musíte odpovedať na otázku: „Ako agent získa tieto informácie?“ To sa môže robiť rôznymi spôsobmi, vrátane RAG, použitia MCP serverov a ďalších nástrojov.

### Praktické stratégie

Plánovanie je dôležité, ale akonáhle začnú prichádzať informácie do kontextového okna nášho agenta, potrebujeme aj praktické stratégie na ich riadenie:

#### Správa kontextu

Kým niektoré informácie sa do kontextového okna pridávajú automaticky, inžinierstvo kontextu znamená aktívnejšie riadiť tieto informácie, čo možno dosiahnuť niekoľkými stratégiami:

 1. **Agent Scratchpad**
 Tento umožňuje AI agentovi robiť si poznámky o relevantných informáciách o aktuálnych úlohách a interakciách s používateľom počas jednej relácie. Tento má existovať mimo kontextového okna vo forme súboru alebo runtime objektu, ktorý môže agent počas tejto relácie neskôr načítať podľa potreby.

 2. **Spomienky**
 Scratchpady sú dobré pre správu informácií mimo kontextového okna jednej relácie. Spomienky umožňujú agentom ukladať a získavať relevantné informácie naprieč viacerými reláciami. Môžu to byť napríklad zhrnutia, preferencie používateľa a spätná väzba pre budúce zlepšenia.

 3. **Kompresia kontextu**
  Keď kontextové okno rastie a blíži sa k svojmu limitu, možno použiť techniky ako zhrnutie a orezávanie. To zahŕňa ponechanie len najrelevantnejších informácií alebo odstránenie starších správ.

 4. **Viac-agentové systémy**
  Vývoj viac-agentových systémov je forma inžinierstva kontextu, pretože každý agent má svoje vlastné kontextové okno. Ako sa tento kontext zdieľa a prenáša medzi rôznymi agentmi je ďalšia vec, ktorú treba naplánovať pri budovaní týchto systémov.

 5. **Sandboxové prostredia**
  Ak agent potrebuje spustiť nejaký kód alebo spracovať veľké množstvo informácií v dokumente, môže to vyžadovať veľký počet tokenov na spracovanie výsledkov. Namiesto toho, aby sa to všetko ukladalo v kontextovom okne, agent môže používať sandboxové prostredie, ktoré dokáže spustiť kód a načítať len výsledky a ďalšie relevantné informácie.

 6. **Runtime State Objects**
   To sa realizuje vytváraním kontajnerov informácií na správu situácií, keď agent potrebuje mať prístup k určitým informáciám. Pri komplexnej úlohe to agentovi umožní ukladať výsledky jednotlivých podúloh krok za krokom, čo umožňuje, aby kontext zostal pripojený len k danej konkrétnej podúlohe.

#### Kontrola kontextu

Po aplikovaní jednej z týchto stratégií stojí za to skontrolovať, čo presne model získal pri nasledujúcom volaní. Užitočná otázka na ladenie je:

> Načítal agent príliš veľa kontextu, nesprávny kontext alebo mu chýbal kontext, ktorý potreboval?

Nemusíte logovať surové promptové vstupy, výstupy nástrojov alebo obsah pamäte na zodpovedanie tejto otázky. V produkcii uprednostnite malé záznamy kontroly kontextu, ktoré zachytávajú počty, ID, hashy a označenia pravidiel:

- **Výber:** Sledovať, koľko kandidátskych blokov, nástrojov alebo spomienok bolo zvážených, koľko bolo vybraných a ktoré pravidlo alebo skóre spôsobili filtrovanie ostatných.

- **Kompresia:** Zaznamenať rozsah zdroja alebo trace ID, ID zhrnutia, odhadovaný počet tokenov pred a po kompresii, a či bol surový obsah z ďalšieho volania vylúčený.

- **Izolácia:** Poznamenať, ktorá podúloha bežala v samostatnom agentovi, relácii alebo sandboxe, aké ohraničené zhrnutie bolo vrátené a či veľké výstupy nástrojov zostali mimo kontext hlavného agenta.

- **Pamäť a RAG:** Ukladať ID dokumentov na získanie, ID pamäte, skóre, vybrané ID a stav redakcie namiesto celého načítaného textu.

- **Bezpečnosť a súkromie:** Uprednostniť hashe, ID, token bucket-y a označenia pravidiel namiesto citlivého textu promptu, argumentov nástrojov, výsledkov nástrojov alebo tela používateľskej pamäte.

Cieľom nie je uchovávať viac kontextu, ale ponechať dostatok dôkazov, aby vývojár vedel, ktorá stratégia kontextu bola použitá a či zmenila ďalšie volanie modelu zamýšľaným spôsobom.

### Príklad inžinierstva kontextu

Povedzme, že chceme, aby AI agent **„Zarezervoval mi výlet do Paríža.“**

• Jednoduchý agent využívajúci len prompt engineering by mohol len reagovať: **„Dobre, kedy by ste chceli ísť do Paríža?“**. Spracoval iba vašu priamu otázku v čase, keď ste ju položili.

• Agent používajúci stratégie inžinierstva kontextu popísané vyššie by urobil oveľa viac. Ešte pred odpoveďou by jeho systém mohol:

  ◦ **Skontrolovať váš kalendár** pre dostupné termíny (získanie dát v reálnom čase).

 ◦ **Pripomenúť si minulé cestovateľské preferencie** (z dlhodobej pamäte) ako vaša preferovaná letecká spoločnosť, rozpočet alebo či uprednostňujete priame lety.

 ◦ **Identifikovať dostupné nástroje** na rezerváciu letu a hotela.

- Príklad odpovede potom môže byť:  „Ahoj [Vaše meno]! Vidím, že máte voľno v prvom týždni októbra. Mám hľadať priame lety do Paríža s [preferovaná letecká spoločnosť] v rámci vášho bežného rozpočtu [rozpočet]?“. Táto bohatšia, kontextovo uvedomelá odpoveď demonštruje silu inžinierstva kontextu.

## Bežné zlyhania kontextu

### Otrava kontextu

**Čo to je:** Keď halucinácia (falošná informácia generovaná LLM) alebo chyba prenikne do kontextu a je opakovane odkazovaná, čo vedie agenta k nasledovaniu nemožných cieľov alebo vytváraniu nezmyselných stratégií.

**Čo robiť:** Implementovať **validáciu kontextu** a **karanténu**. Validujte informácie pred ich pridaním do dlhodobej pamäte. Ak sa zistí potenciálna otrava, začnite nové vlákna kontextu, aby ste zabránili šíreniu zlých informácií.

**Príklad rezervácie cesty:** Váš agent halucinoval **priamy let z malého miestneho letiska do vzdialeného medzinárodného mesta**, ktoré v skutočnosti neponúka medzinárodné lety. Tento neexistujúci detail letu sa uloží do kontextu. Neskôr, keď agenta požiadate o rezerváciu, stále sa snaží nájsť lístky na túto nemožnú trasu, čo vedie k opakovaným chybám.

**Riešenie:** Implementujte krok, ktorý **overí existenciu letu a trasy pomocou API v reálnom čase** _pred_ pridaním detailu letu do pracovného kontextu agenta. Ak validácia zlyhá, chybná informácia sa „karanténne“ izoluje a ďalej nepoužíva.

### Rozptýlenie kontextu

**Čo to je:** Keď sa kontext zväčší natoľko, že model sa príliš zameriava na nahromadenú históriu namiesto toho, aby využíval to, čo sa naučil počas tréningu, čo vedie k opakovaniu alebo neefektívnym akciám. Modely môžu robiť chyby ešte pred zaplnením kontextového okna.

**Čo robiť:** Použite **zhrnutie kontextu**. Pravidelne komprimujte nahromadené informácie do kratších zhrnutí, pričom zachovávejte dôležité detaily a odstraňujte redundantnú históriu. To pomáha „resetovať“ fokus.

**Príklad rezervácie cesty:** Už dlhý čas diskutujete o rôznych vysnívaných destináciách vrátane detailného rozprávania o vašom batohu pred dvoma rokmi. Keď nakoniec požiadate o **„nájdenie lacného letu na budúci mesiac“**, agent sa zamotá v starých, nerelevantných detailoch a stále sa pýta na batoh alebo predchádzajúce itineráre, ignorujúc vašu aktuálnu požiadavku.

**Riešenie:** Po dosiahnutí určitého počtu ťahov alebo keď kontext príliš narastie, by mal agent **zhrnúť najnovšie a najrelevantnejšie časti konverzácie** – zamerané na aktuálne dátumy cesty a cieľ – a toto zhrnutie použiť pre ďalšie volanie LLM, pričom menej relevantné historické chaty vynechá.

### Zmätenie kontextu

**Čo to je:** Keď zbytočný kontext, často vo forme príliš mnohých dostupných nástrojov, prinúti model generovať zlé odpovede alebo volať nerelevantné nástroje. Menšie modely sú na to zvlášť náchylné.

**Čo robiť:** Implementujte **správu nástrojov** pomocou techník RAG. Ukladajte popisy nástrojov do vektorovej databázy a vyberajte _len_ tie najrelevantnejšie nástroje pre každú konkrétnu úlohu. Výskumy ukazujú, že by mal byť počet vybraných nástrojov menší ako 30.

**Príklad rezervácie cesty:** Váš agent má prístup k desiatkam nástrojov: `book_flight`, `book_hotel`, `rent_car`, `find_tours`, `currency_converter`, `weather_forecast`, `restaurant_reservations` a ďalšie. Položíte otázku: **„Aký je najlepší spôsob, ako sa pohybovať po Paríži?“** Kvôli obrovskému množstvu nástrojov sa agent zamotá a pokúsi sa volať `book_flight` _v rámci_ Paríža alebo `rent_car` aj keď uprednostňujete verejnú dopravu, pretože popisy nástrojov sa môžu prekrývať alebo jednoducho nevie rozlíšiť ten najlepší.

**Riešenie:** Použite **RAG na popisy nástrojov**. Keď sa pýtate na pohyb po Paríži, systém dynamicky načíta _len_ najrelevantnejšie nástroje ako `rent_car` alebo `public_transport_info` na základe vášho dotazu, čím poskytne zameraný „loadout“ nástrojov pre LLM.

### Konflikt kontextu

**Čo to je:** Keď v kontexte existujú protichodné informácie, vedie to k nekonzistentnému uvažovaniu alebo zlým konečným odpovediam. Často sa to stáva, keď sa informácie doručujú po etapách a skoré, nesprávne predpoklady zostávajú v kontexte.

**Čo robiť:** Použite **orezávanie kontextu** a **odkládanie**. Orezávanie znamená odstraňovanie zastaraných alebo konfliktových informácií s príchodom nových dát. Odkládanie poskytuje modelu samostatný pracovný „scratchpad“ na spracovanie informácií bez zahltenia hlavného kontextu.
**Príklad rezervácie cestovania:** Najprv poviete svojmu agentovi, **„Chcem letieť ekonomickou triedou.“** Neskôr v rozhovore si to rozmyslíte a poviete, **„Vlastne, na túto cestu by sme mali ísť business triedou.“** Ak obe inštrukcie zostanú v kontexte, agent môže dostať protichodné výsledky vyhľadávania alebo sa môže zmiasť, ktorú preferenciu uprednostniť.

**Riešenie:** Implementujte **prerezávanie kontextu**. Keď nová inštrukcia odporuje starej, staršia inštrukcia sa z kontextu odstráni alebo explicitne prepíše. Alternatívne môže agent použiť **scratchpad** na zosúladenie protichodných preferencií pred finálnym rozhodnutím, čím zabezpečí, že iba konečná, konzistentná inštrukcia bude riadiť jeho činnosti.

## Máte ďalšie otázky ohľadom spracovania kontextu?

Pridajte sa na [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kde sa stretnete s ďalšími študentmi, zúčastníte sa konzultačných hodín a získate odpovede na svoje otázky o AI agentoch.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->