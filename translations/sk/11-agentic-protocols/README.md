# Používanie agentných protokolov (MCP, A2A a NLWeb)

[![Agentné protokoly](../../../translated_images/sk/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Kliknite na obrázok vyššie pre zobrazenie videa tejto lekcie)_

Ako rastie používanie AI agentov, rastie aj potreba protokolov, ktoré zabezpečujú štandardizáciu, bezpečnosť a podporujú otvorenú inováciu. V tejto lekcii si prejdeme 3 protokoly, ktoré sa snažia túto potrebu splniť - Model Context Protocol (MCP), Agent to Agent (A2A) a Natural Language Web (NLWeb).

## Úvod

V tejto lekcii si prejdeme:

• Ako **MCP** umožňuje AI agentom pristupovať k externým nástrojom a dátam, aby splnili úlohy používateľa.

• Ako **A2A** umožňuje komunikáciu a spoluprácu medzi rôznymi AI agentmi.

• Ako **NLWeb** prináša rozhrania v prirodzenom jazyku na akúkoľvek webovú stránku, umožňujúce AI agentom objavovať a interagovať s obsahom.

## Ciele učenia

• **Identifikovať** základný účel a výhody MCP, A2A a NLWeb v kontexte AI agentov.

• **Vysvetliť**, ako každý protokol umožňuje komunikáciu a interakciu medzi LLM, nástrojmi a inými agentmi.

• **Rozoznať** odlišné úlohy, ktoré každý protokol hrá pri budovaní komplexných agentných systémov.

## Model Context Protocol

**Model Context Protocol (MCP)** je otvorený štandard, ktorý poskytuje štandardizovaný spôsob, ako aplikácie poskytujú kontext a nástroje LLM. To umožňuje „univerzálny adaptér“ k rôznym zdrojom dát a nástrojom, ku ktorým sa AI agenti môžu pripojiť konzistentným spôsobom.

Pozrime sa na komponenty MCP, výhody oproti priamemu použitiu API a príklad, ako by AI agenti mohli používať MCP server.

### Základné komponenty MCP

MCP funguje na **klient-server architektúre** a jeho základné komponenty sú:

• **Hostitelia** sú LLM aplikácie (napríklad editory kódu ako VSCode), ktoré začínajú pripojenia k MCP serveru.

• **Klienti** sú komponenty v rámci hostiteľskej aplikácie, ktoré udržiavajú jednovrstvové pripojenie so servermi.

• **Servery** sú ľahké programy, ktoré vystavujú špecifické schopnosti.

V protokole sú zahrnuté tri základné primitívy, ktoré predstavujú schopnosti MCP servera:

• **Nástroje**: Sú to konkrétne akcie alebo funkcie, ktoré môže AI agent vyvolať na vykonanie určitej akcie. Napríklad, meteorologická služba môže vystaviť nástroj „získať počasie“, alebo e-commerce server môže vystaviť nástroj „zakúpiť produkt“. MCP servery oznamujú každý nástroj s menom, popisom a schémou vstupov/výstupov vo svojom zozname schopností.

• **Zdroje**: Sú to údaje alebo dokumenty len na čítanie, ktoré MCP server môže poskytnúť a klienti si ich môžu vyžiadať podľa potreby. Príklady zahŕňajú obsah súborov, databázové záznamy alebo log súbory. Zdroje môžu byť textové (ako kód alebo JSON) alebo binárne (ako obrázky alebo PDF).

• **Výzvy (Prompts)**: Sú to preddefinované šablóny, ktoré poskytujú navrhované výzvy, umožňujúce komplexnejšie pracovné postupy.

### Výhody MCP

MCP ponúka významné výhody pre AI agentov:

• **Dynamické objavovanie nástrojov**: Agenti môžu dynamicky prijímať zoznam dostupných nástrojov zo servera spolu s popismi ich funkcií. To je odlišné od tradičných API, ktoré často vyžadujú statické kódovanie integrácií, pričom každá zmena API si vyžaduje aktualizácie kódu. MCP ponúka prístup „integrovať raz“, ktorý vedie k väčšej prispôsobivosti.

• **Interoperabilita medzi LLM**: MCP funguje naprieč rôznymi LLM, čo umožňuje flexibilitu pri zmene základných modelov za účelom lepšieho výkonu.

• **Štandardizovaná bezpečnosť**: MCP obsahuje štandardnú metódu overovania, ktorá zlepšuje škálovateľnosť pri pridávaní prístupu k ďalším MCP serverom. Je to jednoduchšie než spravovať rôzne kľúče a typy overovania pre tradičné API.

### Príklad MCP

![MCP Diagram](../../../translated_images/sk/mcp-diagram.e4ca1cbd551444a1.webp)

Predstavte si, že používateľ chce rezervovať let pomocou AI asistenta poháňaného MCP.

1. **Pripojenie**: AI asistent (klient MCP) sa pripája k MCP serveru poskytnutému leteckou spoločnosťou.

2. **Objavovanie nástrojov**: Klient sa pýta MCP serveru leteckej spoločnosti: „Aké nástroje máte k dispozícii?“ Server odpovie nástrojmi ako „vyhľadávanie letov“ a „rezervácia letov“.

3. **Volanie nástroja**: Používateľ potom požiada AI asistenta: „Prosím, vyhľadaj let z Portlandu do Honolulu.“ AI asistent pomocou LLM identifikuje, že potrebuje zavolať nástroj „vyhľadávanie letov“ a odovzdá príslušné parametre (odletové miesto, cieľ) MCP serveru.

4. **Vykonanie a odpoveď**: MCP server, ktorý funguje ako obal, uskutoční skutočné volanie na interné rezervačné API leteckej spoločnosti. Získané informácie o lete (napr. JSON dáta) potom odošle späť AI asistentovi.

5. **Ďalšia interakcia**: AI asistent zobrazí možnosti letov. Keď si používateľ vyberie let, asistent môže zavolať nástroj „rezervácia letu“ na rovnakom MCP serveri a dokončiť rezerváciu.

## Protokol agent-agent (A2A)

Kým MCP sa zameriava na prepojenie LLM s nástrojmi, **protokol Agent-to-Agent (A2A)** posúva to o krok ďalej tým, že umožňuje komunikáciu a spoluprácu medzi rôznymi AI agentmi. A2A spája AI agentov naprieč rôznymi organizáciami, prostrediami a technológiami, aby vykonali spoločnú úlohu.

Preskúmame komponenty a výhody A2A spolu s príkladom, ako by sa dalo použiť v našej cestovnej aplikácii.

### Základné komponenty A2A

A2A sa zameriava na umožnenie komunikácie medzi agentmi a ich spolupráce na dokončení podúlohy používateľa. Každá časť protokolu prispieva k tejto funkcii:

#### Agentná karta

Podobne ako MCP server zdieľa zoznam nástrojov, Agentná karta obsahuje:

- Meno agenta.

- **Popis všeobecných úloh**, ktoré agent plní.

- **Zoznam konkrétnych zručností** s popismi, ktoré pomáhajú ostatným agentom (alebo aj ľudským používateľom) pochopiť, kedy a prečo by mali daného agenta zavolať.

- **Aktuálnu URL koncového bodu** agenta.

- **Verziu** a **schopnosti** agenta, ako napríklad streamovanie odpovedí a push notifikácie.

#### Agentný vykonávateľ

Agentný vykonávateľ je zodpovedný za **odovzdanie kontextu chatovej konverzácie používateľa vzdialenému agentovi**. Vzdialený agent to potrebuje na pochopenie úlohy, ktorú má vykonať. V A2A serveri agent používa svoj vlastný Large Language Model (LLM) na spracovanie prichádzajúcich požiadaviek a vykonávanie úloh pomocou svojich vnútorných nástrojov.

#### Artefakt

Keď vzdialený agent dokončí požadovanú úlohu, jeho výstup sa vytvorí ako artefakt. Artefakt **obsahuje výsledok práce agenta**, **popis toho, čo bolo dokončené** a **textový kontext** odoslaný prostredníctvom protokolu. Po odoslaní artefaktu sa spojenie so vzdialeným agentom zatvorí, kým nebude opäť potrebné.

#### Fronta udalostí

Táto zložka sa používa na **spracovanie aktualizácií a prenos správ**. Je obzvlášť dôležitá v produkcii agentných systémov, aby sa zabránilo predčasnému uzavretiu spojenia medzi agentami pred dokončením úlohy, najmä ak dokončenie úlohy môže trvať dlhšie.

### Výhody A2A

• **Zlepšená spolupráca**: Umožňuje agentom od rôznych dodávateľov a platforiem vzájomne komunikovať, zdieľať kontext a spolupracovať, čím sa zabezpečuje plynulá automatizácia naprieč tradične oddelenými systémami.

• **Flexibilita výberu modelov**: Každý A2A agent si môže vybrať, ktorý LLM používa na obsluhu svojich požiadaviek, čo umožňuje optimalizované alebo špecificky doladené modely pre každého agenta, na rozdiel od jedného LLM spojenia v niektorých MCP scenároch.

• **Vstavané overovanie**: Overovanie je integrované priamo do protokolu A2A, čo poskytuje robustný bezpečnostný rámec pre interakcie agentov.

### Príklad A2A

![A2A Diagram](../../../translated_images/sk/A2A-Diagram.8666928d648acc26.webp)

Rozšírme náš scenár rezervácie cesty, ale tentokrát použime A2A.

1. **Požiadavka používateľa na multi-agenta**: Používateľ interaguje s A2A klientom/agenta „Cestovný agent“, napríklad hovorením: „Prosím, rezervuj celú cestu do Honolulu na budúci týždeň, vrátane letov, hotela a požičovne áut“.

2. **Orchestrácia cestovným agentom**: Cestovný agent prijme tento komplexný požiadavok. Použije svoj LLM na rozmyslenie úlohy a určí, že potrebuje komunikovať s inými špecializovanými agentmi.

3. **Medziagentná komunikácia**: Cestovný agent potom použije A2A protokol na pripojenie k ďalším agentom, ako sú „agent leteckej spoločnosti“, „hotelový agent“ a „agent požičovne áut“, ktoré vytvorili rôzne spoločnosti.

4. **Delegované vykonanie úloh**: Cestovný agent odosiela špecifické úlohy týmto špecializovaným agentom (napr. „nájdi lety do Honolulu“, „rezervuj hotel“, „požičiavaj auto“). Každý z týchto agendov, bežiacich na vlastných LLM a využívajúcich vlastné nástroje (ktoré môžu byť MCP servermi), vykonáva svoju špecifickú časť rezervácie.

5. **Konsolidovaná odpoveď**: Keď všetci agenti dokončia svoje úlohy, cestovný agent zkompiluje výsledky (detaily letu, potvrdenie hotela, rezerváciu auta) a pošle komplexnú, chatového štýlu odpoveď používateľovi.

## Natural Language Web (NLWeb)

Webové stránky sú už dlhodobo hlavným spôsobom, ako používatelia získavajú informácie a dáta cez internet.

Pozrime sa na rôzne komponenty NLWeb, výhody NLWeb a príklad, ako náš NLWeb funguje pri našej cestovnej aplikácii.

### Komponenty NLWeb

- **NLWeb aplikácia (jadrový servisný kód)**: Systém, ktorý spracováva otázky v prirodzenom jazyku. Spája rôzne časti platformy na tvorbu odpovedí. Môžeme si ju predstaviť ako **motor, ktorý poháňa funkcie prirodzeného jazyka** na webovej stránke.

- **NLWeb protokol**: Je to **základný súbor pravidiel pre interakciu v prirodzenom jazyku** s webovou stránkou. Odosiela odpovede v JSON formáte (často pomocou Schema.org). Jeho účelom je vytvoriť jednoduchý základ pre „AI web“, podobne ako HTML umožnilo zdieľanie dokumentov online.

- **MCP server (Model Context Protocol Endpoint)**: Každé NLWeb nastavenie funguje aj ako **MCP server**. To znamená, že môže **zdieľať nástroje (ako metódu „ask“) a dáta** s inými AI systémami. V praxi to umožňuje, aby obsah a schopnosti webu boli použiteľné AI agentmi a stránka sa stala súčasťou širšieho „agentného ekosystému“.

- **Embedding modely**: Tieto modely sa používajú na **prevedenie obsahu webu do číselných reprezentácií nazývaných vektory (embeddingy)**. Tieto vektory zachytávajú význam spôsobom, ktorý môžu počítače porovnávať a vyhľadávať. Ukladajú sa do špeciálnej databázy a používatelia môžu vybrať, ktorý embedding model chcú používať.

- **Vektorová databáza (retrieval mechanizmus)**: Táto databáza **ukladá embeddingy obsahu webu**. Keď niekto položí otázku, NLWeb skontroluje vektorovú databázu, aby rýchlo našiel najrelevantnejšie informácie. Poskytuje rýchly zoznam možných odpovedí zoradených podľa podobnosti. NLWeb spolupracuje s rôznymi systémami ukladania vektorov ako Qdrant, Snowflake, Milvus, Azure AI Search a Elasticsearch.

### NLWeb na príklade

![NLWeb](../../../translated_images/sk/nlweb-diagram.c1e2390b310e5fe4.webp)

Zvážte znova našu cestovnú rezervačnú stránku, ale tentokrát poháňanú NLWeb.

1. **Ingestovanie dát**: Existujúce katalógy produktov cestovnej stránky (napr. zoznamy letov, popisy hotelov, turistické balíčky) sú formátované pomocou Schema.org alebo načítané cez RSS kanály. Nástroje NLWeb tieto štruktúrované dáta spracujú, vytvoria embeddingy a uložia ich do lokálnej alebo vzdialenej vektorovej databázy.

2. **Otázka v prirodzenom jazyku (človek)**: Používateľ navštívi stránku a namiesto prechádzania menu napíše do chatového rozhrania: „Nájdite mi rodinne priateľský hotel v Honolulu s bazénom na budúci týždeň“.

3. **Spracovanie NLWeb**: NLWeb aplikácia prijme túto otázku. Pošle dopyt do LLM na porozumenie a zároveň prehľadá svoju vektorovú databázu pre relevantné hotelové ponuky.

4. **Presné výsledky**: LLM pomáha interpretovať výsledky vyhľadávania z databázy, identifikuje najlepšie zhody podľa kritérií „rodinne priateľský“, „bazén“ a „Honolulu“ a potom formátuje odpoveď v prirodzenom jazyku. Dôležité je, že odpoveď sa odvoláva na skutočné hotely z katalógu stránky a neobsahuje vymyslené informácie.

5. **Interakcia AI agenta**: Pretože NLWeb funguje ako MCP server, externý AI cestovný agent by sa mohol pripojiť k tejto NLWeb inštancii webu. AI agent by mohol použiť metódu `ask` MCP na priame položenie otázky stránke: `ask("Existujú v oblasti Honolulu reštaurácie priateľské k vegánom, ktoré odporúča hotel?")`. NLWeb by to spracoval, využívajúc svoju databázu informácií o reštauráciách (ak je načítaná), a vrátil štruktúrovanú JSON odpoveď.

### Máte viac otázok o MCP/A2A/NLWeb?

Pridajte sa na [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kde sa môžete stretnúť s ďalšími študentmi, zúčastniť sa kancelárskych hodín a získať odpovede na otázky týkajúce sa AI agentov.

## Zdroje

- [MCP pre začiatočníkov](https://aka.ms/mcp-for-beginners)  
- [Dokumentácia MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framework)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->