# Používanie agentových protokolov (MCP, A2A a NLWeb)

[![Agentové protokoly](../../../translated_images/sk/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Kliknite na obrázok vyššie pre zobrazenie videa tejto lekcie)_

Ako rastie používanie AI agentov, rastie aj potreba protokolov, ktoré zabezpečia štandardizáciu, bezpečnosť a podporu otvorenej inovácii. V tejto lekcii sa budeme venovať 3 protokolom, ktoré sa snažia túto potrebu naplniť – Model Context Protocol (MCP), Agent to Agent (A2A) a Natural Language Web (NLWeb).

## Úvod

V tejto lekcii budeme preberať:

• Ako **MCP** umožňuje AI agentom pristupovať k externým nástrojom a dátam na dokončenie používateľských úloh.

• Ako **A2A** umožňuje komunikáciu a spoluprácu medzi rôznymi AI agentmi.

• Ako **NLWeb** prináša rozhrania s prirodzeným jazykom na akúkoľvek webovú stránku, umožňujúc AI agentom objavovať a interagovať s obsahom.

## Ciele učenia

• **Identifikovať** hlavný účel a výhody MCP, A2A a NLWeb v kontexte AI agentov.

• **Vysvetliť**, ako každý protokol uľahčuje komunikáciu a interakciu medzi LLM, nástrojmi a inými agentmi.

• **Rozpoznať** odlišné úlohy, ktoré každý protokol zohráva pri budovaní komplexných agentových systémov.

## Model Context Protocol

**Model Context Protocol (MCP)** je otvorený štandard, ktorý poskytuje štandardizovaný spôsob, ako aplikácie môžu poskytovať kontext a nástroje pre LLM. Toto umožňuje „univerzálny adaptér“ k rôznym dátovým zdrojom a nástrojom, ku ktorým sa AI agenti môžu pripojiť konzistentným spôsobom.

Pozrime sa na komponenty MCP, výhody oproti priamemu používaniu API a príklad, ako by AI agenti mohli používať MCP server.

### Základné komponenty MCP

MCP funguje na **klient-server architektúre** a základné komponenty sú:

• **Hostitelia** sú LLM aplikácie (napríklad kódový editor ako VSCode), ktoré začínajú spojenia so serverom MCP.

• **Klienti** sú komponenty v hostiteľskej aplikácii, ktoré udržiavajú jedno-na-jedného spojenia so servermi.

• **Servery** sú ľahké programy, ktoré vystavujú špecifické schopnosti.

Súčasťou protokolu sú tri základné primitívy, ktoré sú schopnosťami MCP servera:

• **Nástroje**: Ide o samostatné akcie alebo funkcie, ktoré AI agent môže zavolať na vykonanie určitej akcie. Napríklad, služba počasia môže vystaviť nástroj „získaj počasie“, alebo e-commerce server môže vystaviť nástroj „kúp produkt“. MCP servery oznamujú názov nástroja, jeho popis a schému vstupov/výstupov vo svojom zozname schopností.

• **Zdroje**: Sú to dátové položky alebo dokumenty iba na čítanie, ktoré môže MCP server poskytnúť a klienti ich môžu podľa potreby načítať. Príklady zahŕňajú obsah súborov, databázové záznamy alebo log súbory. Zdroje môžu byť textové (ako kód alebo JSON) alebo binárne (ako obrázky alebo PDF).

• **Výzvy (Prompts)**: Sú to preddefinované šablóny, ktoré poskytujú navrhované výzvy, čo umožňuje zložitejšie pracovné postupy.

### Výhody MCP

MCP ponúka významné výhody pre AI agentov:

• **Dynamické objavovanie nástrojov**: Agentom sa dynamicky poskytuje zoznam dostupných nástrojov zo servera spolu s popismi, čo je oproti tradičným API, ktoré často vyžadujú statické kódovanie integrácií a akákoľvek zmena API znamená aktualizáciu kódu. MCP ponúka prístup „integruj raz“, čo vedie k väčšej flexibilite.

• **Interoperabilita naprieč LLM**: MCP funguje naprieč rôznymi LLM, čo poskytuje flexibilitu pri prepínaní základných modelov na lepší výkon.

• **Štandardizovaná bezpečnosť**: MCP obsahuje štandardný spôsob autentifikácie, čo zlepšuje škálovateľnosť pri pridávaní prístupu k ďalším MCP serverom. To je jednoduchšie ako spravovať rôzne kľúče a autentifikácie pre rôzne tradičné API.

### Príklad MCP

![MCP Diagram](../../../translated_images/sk/mcp-diagram.e4ca1cbd551444a1.webp)

Predstavte si, že používateľ chce rezervovať let pomocou AI asistenta poháňaného MCP.

1. **Pripojenie**: AI asistent (MCP klient) sa pripojí k MCP serveru poskytovanému leteckou spoločnosťou.

2. **Objavovanie nástrojov**: Klient sa spýta MCP serveru aerolinky: „Aké nástroje máte k dispozícii?“ Server odpovie nástrojmi ako „vyhľadávanie letov“ a „rezervácia letov“.

3. **Volanie nástroja**: Potom požiadate AI asistenta: „Prosím vyhľadaj let z Portlandu do Honolulu.“ AI asistent pomocou svojho LLM identifikuje, že musí zavolať nástroj „vyhľadávanie letov“ a odovzdá relevantné parametre (odletisko, cieľ) MCP serveru.

4. **Vykonanie a odpoveď**: MCP server, ktorý funguje ako obal, vykoná skutočné volanie vnútorného rezervačného API leteckej spoločnosti. Potom prijme informácie o lete (napr. dáta vo formáte JSON) a odošle ich späť AI asistentovi.

5. **Ďalšia interakcia**: AI asistent zobrazí možnosti letov. Ak vyberiete let, asistent môže zavolať nástroj „rezervovať let“ na tom istom MCP serveri a dokončiť rezerváciu.

## Protokol agent-agent (A2A)

Kým MCP sa zameriava na pripájanie LLM k nástrojom, **protokol Agent-to-Agent (A2A)** posúva vec ďalej tým, že umožňuje komunikáciu a spoluprácu medzi rôznymi AI agentmi. A2A prepája AI agentov naprieč rôznymi organizáciami, prostrediami a technologickými zásobníkmi na splnenie spoločnej úlohy.

Prezrieme si komponenty a výhody A2A spolu s príkladom, ako by sa dal aplikovať v našej cestovnej aplikácii.

### Základné komponenty A2A

A2A sa zameriava na umožnenie komunikácie medzi agentmi a ich spoluprácu na dokončení úlohy používateľa. Každá časť protokolu k tomu prispieva:

#### Agentová karta

Podobne ako MCP server zdieľa zoznam nástrojov, Agentová karta obsahuje:
- Názov agenta.
- **popis všeobecných úloh**, ktoré plní.
- **zoznam špecifických zručností** s popismi, ktoré pomáhajú ostatným agentom (alebo aj ľudským používateľom) pochopiť, kedy a prečo by mali volať daného agenta.
- **aktuálnu URL koncového bodu** agenta
- **verziu** a **schopnosti** agenta, napríklad streamovanie odpovedí a push notifikácie.

#### Agent Executor

Agent Executor je zodpovedný za **odovzdávanie kontextu používateľského chatu vzdialenému agentovi**, vzdialený agent to potrebuje na pochopenie úlohy, ktorú treba splniť. V A2A serveri agent používa vlastný veľký jazykový model (LLM) na spracovanie prichádzajúcich požiadaviek a vykonávanie úloh pomocou svojich interných nástrojov.

#### Artefakt

Akonáhle vzdialený agent dokončí požadovanú úlohu, jeho výsledok práce sa vytvorí ako artefakt. Artefakt **obsahuje výsledok práce agenta**, **popis toho, čo bolo dokončené**, a **textový kontext**, ktorý sa odosiela prostredníctvom protokolu. Po odoslaní artefaktu sa spojenie so vzdialeným agentom uzavrie, až kým nebude znova potrebné.

#### Fronta udalostí

Táto súčasť sa používa na **spracovanie aktualizácií a odovzdávanie správ**. Je obzvlášť dôležitá v produkcii pre agentové systémy, aby sa zabránilo ukončeniu spojenia medzi agentmi pred dokončením úlohy, najmä keď dokončenie úlohy môže trvať dlhší čas.

### Výhody A2A

• **Zlepšená spolupráca**: Umožňuje agentom z rôznych dodávateľov a platforiem vzájomne komunikovať, zdieľať kontext a pracovať spolu, čím umožňuje plynulú automatizáciu cez tradične oddelené systémy.

• **Flexibilita výberu modelu**: Každý A2A agent si môže zvoliť, ktorý LLM použije na obsluhu svojich požiadaviek, čo umožňuje optimalizované alebo jemne doladené modely pre každého agenta, na rozdiel od jediného LLM pripojenia v niektorých scenároch MCP.

• **Zabudovaná autentifikácia**: Autentifikácia je priamo integrovaná v protokole A2A, čo poskytuje robustný bezpečnostný rámec pre interakciu agentov.

### Príklad A2A

![A2A Diagram](../../../translated_images/sk/A2A-Diagram.8666928d648acc26.webp)

Rozšírme náš scenár rezervácie cestovania, tentoraz použitím A2A.

1. **Používateľská požiadavka na viacagentový systém**: Používateľ komunikuje s „Cestovným agentom“ A2A klientom/agenta, napríklad takto: „Prosím zarezervuj celú cestu do Honolulu na budúci týždeň, vrátane letov, hotela a prenájmu auta.“

2. **Orchestrace cestovného agenta**: Cestovný agent prijme túto zložitú požiadavku. Použije svoj LLM, aby zvážil úlohu a určil, že musí komunikovať s inými špecializovanými agentmi.

3. **Medziagentová komunikácia**: Potom Cestovný agent použije protokol A2A na pripojenie k dálnovým agentom, ako sú „Agent leteckej spoločnosti“, „Agent hotela“ a „Agent prenájmu auta“, ktoré vytvorili rôzne spoločnosti.

4. **Delegované vykonávanie úlohy**: Cestovný agent pošle konkrétne úlohy týmto špecializovaným agentom (napríklad „Nájdi lety do Honolulu“, „Zarezervuj hotel“, „Prenajmi auto“). Každý z týchto špecializovaných agentov, používajúci vlastné LLM a svoje nástroje (ktoré môžu byť aj MCP servery), vykoná svoju časť rezervácie.

5. **Konsolidovaná odpoveď**: Keď všetci downstream agenti dokončia svoje úlohy, Cestovný agent zloží výsledky (detaily letov, potvrdenie hotela, rezervácia auta) a odošle komplexnú odpoveď v štýle chatu späť používateľovi.

## Natural Language Web (NLWeb)

Webové stránky boli dlhodobo hlavným spôsobom, ako môžu používatelia získať informácie a dáta cez internet.

Pozrime sa na rôzne komponenty NLWeb, výhody NLWeb a príklad, ako náš NLWeb funguje na základe našej cestovnej aplikácie.

### Komponenty NLWeb

- **NLWeb aplikácia (jadrový kód služby)**: Systém, ktorý spracúva otázky v prirodzenom jazyku. Spája rôzne časti platformy na vytvorenie odpovedí. Môžete si to predstaviť ako **motor, ktorý poháňa funkcie prirodzeného jazyka** na webovej stránke.

- **NLWeb protokol**: Ide o **základnú sadu pravidiel pre interakciu v prirodzenom jazyku** s webovou stránkou. Posiela späť odpovede v JSON formáte (často so Schema.org). Jeho účelom je vytvoriť jednoduchý základ pre „AI Web“, podobne ako HTML umožnilo zdieľať dokumenty online.

- **MCP server (koncový bod Model Context Protocol)**: Každé nastavenie NLWeb tiež funguje ako **MCP server**. To znamená, že môže **zdieľať nástroje (napr. metódu „ask“) a dáta** s inými AI systémami. V praxi to umožňuje, aby obsah a schopnosti webu boli použiteľné AI agentmi a stránka sa stala súčasťou širšieho „agentového ekosystému“.

- **Embedovacie modely**: Tieto modely sa používajú na **prevod obsahu webovej stránky do číselných reprezentácií nazývaných vektory** (embeddingy). Tieto vektory zachytávajú význam tak, aby ich počítače mohli porovnávať a vyhľadávať. Ukladajú sa do špeciálnej databázy a používatelia si môžu vybrať, ktorý embedovací model chcú použiť.

- **Vektorová databáza (mechanizmus vyhľadávania)**: Táto databáza **ukladá embeddingy obsahu webovej stránky**. Keď niekto položí otázku, NLWeb kontroluje vektorovú databázu, aby rýchlo našla najrelevantnejšie informácie. Poskytne rýchly zoznam možných odpovedí, zoradených podľa podobnosti. NLWeb funguje s rôznymi systémami uchovávania vektorov ako Qdrant, Snowflake, Milvus, Azure AI Search a Elasticsearch.

### NLWeb na príklade

![NLWeb](../../../translated_images/sk/nlweb-diagram.c1e2390b310e5fe4.webp)

Znova zvážme našu webovú stránku na rezerváciu ciest, tentoraz však poháňanú NLWeb.

1. **Zber dát**: Existujúce katalógy produktov na cestovnej stránke (napríklad zoznamy letov, popisy hotelov, turistické balíčky) sú naformátované pomocou Schema.org alebo načítané cez RSS kanály. Nástroje NLWeb tieto štruktúrované dáta spracujú, vytvoria embeddingy a uložia ich do lokálnej alebo vzdialenej vektorovej databázy.

2. **Dotaz v prirodzenom jazyku (človek)**: Používateľ navštívi stránku a namiesto prechádzania menu napíše do chat rozhrania: „Nájdi mi rodinne priateľský hotel v Honolulu s bazénom na budúci týždeň“.

3. **Spracovanie NLWeb**: NLWeb aplikácia prijme tento dotaz. Pošle ho do LLM na porozumenie a zároveň vyhľadá v databáze vektorov relevantné ponuky hotelov.

4. **Presné výsledky**: LLM pomáha interpretovať výsledky vyhľadávania z databázy, identifikuje najlepšie zhody podľa kritérií „rodinne priateľský“, „bazén“ a „Honolulu“ a potom formátuje odpoveď v prirodzenom jazyku. Dôležité je, že odpoveď odkazuje na skutočné hotely z katalógu webu, vyhýbajúc sa vytváraniu nepravdivých informácií.

5. **Interakcia AI agenta**: Keďže NLWeb funguje ako MCP server, externý AI cestovný agent by sa tiež mohol pripojiť k tejto NLWeb inštancii webu. AI agent by potom mohol použiť MCP metódu `ask` na priamu otázku webu: `ask("Existujú nejaké vegánsky priateľské reštaurácie v oblasti Honolulu odporúčané hotelom?")`. Inštancia NLWeb by to spracovala, využívajúc svoju databázu informácií o reštauráciách (ak je načítaná), a vrátila by štruktúrovanú JSON odpoveď.

### Máte viac otázok o MCP/A2A/NLWeb?

Pridajte sa do [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), aby ste sa stretli s inými študentmi, zúčastnili sa konzultačných hodín a získali odpovede na svoje otázky o AI agentoch.

## Zdroje

- [MCP pre začiatočníkov](https://aka.ms/mcp-for-beginners)  
- [Dokumentácia MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python)

## Predchádzajúca lekcia

[AI agenti v produkcii](../10-ai-agents-production/README.md)

## Nasledujúca lekcia

[Kontextové inžinierstvo pre AI agentov](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->