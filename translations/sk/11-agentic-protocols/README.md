# Používanie agentných protokolov (MCP, A2A a NLWeb)

[![Agentné protokoly](../../../translated_images/sk/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Kliknite na obrázok vyššie pre zobrazenie videa k tejto lekcii)_

S rastúcim používaním AI agentov rastie aj potreba protokolov, ktoré zabezpečia štandardizáciu, bezpečnosť a podporia otvorenú inováciu. V tejto lekcii sa budeme venovať 3 protokolom, ktoré sa snažia túto potrebu naplniť - Model Context Protocol (MCP), Agent to Agent (A2A) a Natural Language Web (NLWeb).

## Úvod

V tejto lekcii sa dozvieme:

• Ako **MCP** umožňuje AI agentom pristupovať k externým nástrojom a dátam na dokončenie úloh používateľa.

• Ako **A2A** umožňuje komunikáciu a spoluprácu medzi rôznymi AI agentmi.

• Ako **NLWeb** prináša rozhrania v prirodzenom jazyku na akúkoľvek webovú stránku, ktoré umožňujú AI agentom objavovať a interagovať s obsahom.

## Ciele učenia sa

• **Identifikovať** základný účel a výhody MCP, A2A a NLWeb v kontexte AI agentov.

• **Vysvetliť** ako každý protokol uľahčuje komunikáciu a interakciu medzi LLM, nástrojmi a inými agentmi.

• **Rozpoznať** odlišné úlohy, ktoré každý protokol zohráva pri budovaní komplexných agentných systémov.

## Model Context Protocol

**Model Context Protocol (MCP)** je otvorený štandard, ktorý poskytuje štandardizovaný spôsob, ako aplikácie môžu poskytovať kontext a nástroje LLM. To umožňuje „univerzálny adaptér“ k rôznym zdrojom dát a nástrojom, na ktoré sa AI agenti môžu pripájať konzistentným spôsobom.

Pozrime sa na komponenty MCP, výhody oproti priamemu používaniu API a príklad, ako by AI agenti mohli používať MCP server.

### Kľúčové komponenty MCP

MCP funguje na **klient-server architektúre** a kľúčové komponenty sú:

• **Hostitelia** sú LLM aplikácie (napríklad editor kódu ako VSCode), ktoré začínajú spojenia so serverom MCP.

• **Klienti** sú komponenty v hostiteľskej aplikácii, ktoré udržiavajú jednotkové spojenia so servermi.

• **Servery** sú nenáročné programy, ktoré vystavujú konkrétne schopnosti.

Súčasťou protokolu sú tri základné primitívy, ktoré predstavujú schopnosti MCP servera:

• **Nástroje**: Diskrétne akcie alebo funkcie, ktoré môže AI agent zavolať na vykonanie činnosti. Napríklad služba počasia môže vystaviť nástroj „zistiť počasie“ alebo server e-commerce môže vystaviť nástroj „kúpiť produkt“. MCP servery inzerujú názov, popis a vstupno-výstupné schémy každého nástroja v zozname schopností.

• **Zdroje**: Sú to dátové položky alebo dokumenty na čítanie, ktoré MCP server môže poskytnúť, a klienti si ich môžu vyžiadať podľa potreby. Príklady zahŕňajú obsah súborov, databázové záznamy alebo log súbory. Zdroje môžu byť textové (ako kód alebo JSON) alebo binárne (ako obrázky alebo PDF).

• **Podnety**: Preddefinované šablóny, ktoré poskytujú navrhované dotazy a umožňujú komplexnejšie pracovné toky.

### Výhody MCP

MCP ponúka významné výhody pre AI agentov:

• **Dynamické objavovanie nástrojov**: Agenti môžu dynamicky získať zoznam dostupných nástrojov od servera spolu s popismi ich funkcií. To kontrastuje s tradičnými API, ktoré často vyžadujú statické kódovanie integrácií, takže akákoľvek zmena API znamená aktualizácie kódu. MCP ponúka prístup „integruj raz“, čo vedie k väčšej prispôsobivosti.

• **Interoperabilita medzi LLM**: MCP funguje cez rôzne LLM, poskytujúc flexibilitu pri prepínaní jadrových modelov pre lepší výkon.

• **Štandardizovaná bezpečnosť**: MCP zahŕňa štandardnú metódu autentifikácie, čo zlepšuje škálovateľnosť pri pridávaní prístupu k ďalším MCP serverom. Je to jednoduchšie ako spravovať rôzne kľúče a typy autentifikácie pre rôzne tradičné API.

### Príklad MCP

![MCP Diagram](../../../translated_images/sk/mcp-diagram.e4ca1cbd551444a1.webp)

Predstavte si, že používateľ chce zaistiť let pomocou AI asistenta, ktorý používa MCP.

1. **Pripojenie**: AI asistent (MCP klient) sa pripojí k MCP serveru poskytovanému leteckou spoločnosťou.

2. **Objavovanie nástrojov**: Klient sa opýta MCP servera leteckej spoločnosti: „Aké nástroje máte dostupné?“ Server odpovie nástrojmi ako „vyhľadávať lety“ a „rezervovať lety“.

3. **Volanie nástroja**: Používateľ potom povie AI asistentovi: „Prosím, vyhľadaj let z Portlandu do Honolulu.“ AI asistent, pomocou svojho LLM, identifikuje potrebu zavolať nástroj „vyhľadávať lety“ a odovzdá relevantné parametre (odlet, cieľ) MCP serveru.

4. **Vykonanie a odpoveď**: MCP server, pôsobiaci ako obal, vykoná skutočné volanie na vnútorné API rezervácie leteckej spoločnosti. Následne prijme informácie o lete (napríklad JSON dáta) a odošle ich späť AI asistentovi.

5. **Ďalšia interakcia**: AI asistent predloží možnosti letov. Akonáhle používateľ vyberie let, asistent môže zavolať nástroj „rezervovať let“ na tom istom MCP serveri a dokončiť rezerváciu.

## Protokol Agent-to-Agent (A2A)

Zatiaľ čo MCP sa zameriava na pripájanie LLM k nástrojom, **Agent-to-Agent (A2A) protokol** ide ďalej tým, že umožňuje komunikáciu a spoluprácu medzi rôznymi AI agentmi. A2A spája AI agentov naprieč rôznymi organizáciami, prostrediami a technologickými platformami na splnenie spoločnej úlohy.

Preskúmame komponenty a výhody A2A spolu s príkladom, ako by sa mohol použiť v našej aplikácii na cestovanie.

### Kľúčové komponenty A2A

A2A kladie dôraz na umožnenie komunikácie medzi agentmi a ich spoluprácu na dokončení podúlohy používateľa. Každá súčasť protokolu k tomu prispieva:

#### Agentná karta

Podobne ako MCP server zdieľa zoznam nástrojov, Agentná karta obsahuje:
- Meno agenta.
- **popis všeobecných úloh**, ktoré agent vykonáva.
- **zoznam špecifických zručností** s popismi, ktoré pomáhajú ostatným agentom (alebo aj ľudským používateľom) pochopiť, kedy a prečo by mali daného agenta využiť.
- **aktuálnu adresu URL endpointu** agenta.
- **verziu** a **schopnosti** agenta, ako napríklad streamovanie odpovedí a push notifikácie.

#### Agentný vykonávateľ

Agentný vykonávateľ je zodpovedný za **odosielanie kontextu používateľského chatu vzdialenému agentovi**, ktorý tento kontext potrebuje na pochopenie úlohy, ktorú má splniť. V A2A serveri agent používa svoj vlastný veľký jazykový model (LLM), aby analyzoval prichádzajúce požiadavky a vykonával úlohy pomocou svojich interných nástrojov.

#### Artefakt

Keď vzdialený agent splní požadovanú úlohu, jeho výsledok je vytvorený ako artefakt. Artefakt **obsahuje výsledok agentovej práce**, **popis toho, čo bolo dokončené**, a **textový kontext**, ktorý je zaslaný prostredníctvom protokolu. Po odoslaní artefaktu sa spojenie s vzdialeným agentom uzavrie, kým nebude znovu potrebné.

#### Fronta udalostí

Tento komponent sa používa na **spracovanie aktualizácií a odosielanie správ**. Je obzvlášť dôležitý v produkcii agentných systémov, aby sa zabránilo uzavretiu spojenia medzi agentmi pred dokončením úlohy, najmä keď dokončenie úlohy môže trvať dlhší čas.

### Výhody A2A

• **Vylepšená spolupráca**: Umožňuje agentom z rôznych dodávateľov a platforiem vzájomne komunikovať, zdieľať kontext a spolupracovať, čím sa uľahčuje plynulá automatizácia cez tradične izolované systémy.

• **Flexibilita výberu modelu**: Každý A2A agent si môže vybrať, ktorý LLM použije na obsluhu svojich požiadaviek, čo umožňuje optimalizované alebo doladené modely pre každého agenta, na rozdiel od jedného LLM spojenia v niektorých prípadoch MCP.

• **Vstavaná autentifikácia**: Autentifikácia je priamo integrovaná do A2A protokolu, poskytujúc robustný bezpečnostný rámec pre interakcie agentov.

### Príklad A2A

![A2A Diagram](../../../translated_images/sk/A2A-Diagram.8666928d648acc26.webp)

Rozšírme našu scénu rezervácie cestovania, tentoraz používajúc A2A.

1. **Používateľská požiadavka na multiagentný systém**: Používateľ komunikuje s „Cestovným agentom“ ako A2A klientom/agentom, povedzme slovami: „Prosím, rezervuj celý výlet do Honolulu na budúci týždeň, vrátane letov, hotela a prenájmu auta“.

2. **Orchestrácia cestovným agentom**: Cestovný agent prijme túto zložitú požiadavku. Pomocou svojho LLM prehodnotí úlohu a určí, že je potrebné komunikovať s inými špecializovanými agentmi.

3. **Komunikácia medzi agentmi**: Cestovný agent potom použije A2A protokol na pripojenie k podriadeným agentom, ako sú „agent leteckej spoločnosti“, „hotelový agent“ a „agent prenájmu áut“, ktoré vytvorili rozdielne spoločnosti.

4. **Zadané vykonanie úloh**: Cestovný agent posiela špecifické úlohy týmto špecializovaným agentom (napríklad „Nájdi lety do Honolulu“, „Rezervuj hotel“, „Prenajmi auto“). Každý z týchto špecializovaných agentov, bežiacich na vlastných LLM a využívajúcich svoje vlastné nástroje (čo môžu byť sami MCP servery), vykonáva svoju časť rezervácie.

5. **Konsolidovaná odpoveď**: Keď všetci podriadení agenti dokončia svoje úlohy, Cestovný agent zostaví výsledky (detaily letov, potvrdenie hotela, rezerváciu auta) a pošle komplexnú, chatovú odpoveď späť používateľovi.

## Natural Language Web (NLWeb)

Webové stránky sú už dlhú dobu hlavným spôsobom, ako používatelia pristupujú k informáciám a dátam na internete.

Pozrime sa na rôzne komponenty NLWeb, výhody NLWeb a príklad, ako náš NLWeb funguje, pozrime sa na našu aplikáciu na cestovanie.

### Komponenty NLWeb

- **NLWeb aplikácia (hlavný servisný kód)**: Systém, ktorý spracováva otázky v prirodzenom jazyku. Spája rôzne časti platformy na vytváranie odpovedí. Môžete to vnímať ako **motor, ktorý poháňa funkcie v prirodzenom jazyku** na webovej stránke.

- **NLWeb protokol**: Je to **základná súprava pravidiel pre interakciu v prirodzenom jazyku** s webovou stránkou. Odosiela odpovede vo formáte JSON (často používajúci Schema.org). Jeho cieľom je vytvoriť jednoduchý základ pre „AI web“, tak ako HTML umožnilo zdieľať dokumenty online.

- **MCP server (endpoint Model Context Protocolu)**: Každá konfigurácia NLWeb tiež funguje ako **MCP server**. To znamená, že môže **zdieľať nástroje (ako metódu „ask“) a dáta** s inými AI systémami. V praxi to umožňuje, aby obsah webovej stránky a jej schopnosti boli použiteľné pre AI agentov, čím sa stránka stáva súčasťou širšieho „agentného ekosystému“.

- **Embedding modely**: Tieto modely sa používajú na **prevod obsahu webovej stránky do číselných reprezentácií nazývaných vektory (embeddingy)**. Tieto vektory zachytávajú význam spôsobom, ktorý môžu počítače porovnávať a vyhľadávať. Sú uložené v špeciálnej databáze a používatelia si môžu vybrať, ktorý embedding model chcú použiť.

- **Vektorová databáza (retrieval mechanizmus)**: Táto databáza **uchováva embeddingy obsahu webovej stránky**. Keď niekto položí otázku, NLWeb kontroluje vektorovú databázu, aby rýchlo našiel relevantné informácie. Poskytuje rýchly zoznam možných odpovedí, zoradených podľa podobnosti. NLWeb pracuje s rôznymi systémami ukladania vektorov ako Qdrant, Snowflake, Milvus, Azure AI Search a Elasticsearch.

### NLWeb na príklade

![NLWeb](../../../translated_images/sk/nlweb-diagram.c1e2390b310e5fe4.webp)

Zoberme si opäť našu webovú stránku na rezerváciu cestovania, tentoraz poháňanú NLWeb.

1. **Zber dát**: Existujúce produktové katalógy cestovnej stránky (napr. zoznamy letov, popisy hotelov, turistické balíčky) sú naformátované pomocou Schema.org alebo načítané cez RSS feedy. Nástroje NLWeb tieto štruktúrované dáta nasávajú, vytvárajú embeddingy a ukladajú ich do lokálnej alebo vzdialenej vektorovej databázy.

2. **Dotaz v prirodzenom jazyku (človek)**: Používateľ navštívi web a namiesto prehľadávania menu zadá do chatovacieho rozhrania: „Nájdi mi rodinne priateľský hotel v Honolulu s bazénom na budúci týždeň“.

3. **Spracovanie NLWeb**: NLWeb aplikácia prijme tento dotaz. Odosiela dotaz na LLM na pochopenie a zároveň vyhľadáva vo svojej vektorovej databáze relevantné ponuky hotelov.

4. **Presné výsledky**: LLM pomáha interpretovať výsledky vyhľadávania z databázy, vyhľadáva najlepšie zhody podľa kritérií „rodinne priateľský“, „bazén“ a „Honolulu“ a následne formátuje odpoveď v prirodzenom jazyku. Dôležité je, že odpoveď odkazuje na skutočné hotely z katalógu webovej stránky, čím sa vyhýba vymysleným informáciám.

5. **Interakcia s AI agentom**: Pretože NLWeb slúži ako MCP server, externý AI cestovný agent sa môže tiež pripojiť k inštancii NLWeb tejto webovej stránky. AI agent môže potom použiť metódu `ask` MCP na priame dotazovanie stránky: `ask("Sú v oblasti Honolulu nejaké vegánske reštaurácie odporúčané hotelom?")`. Inštancia NLWeb toto spracuje, využívajúc svoju databázu informácií o reštauráciách (ak bola načítaná), a vráti štruktúrovanú JSON odpoveď.

### Máte viac otázok o MCP/A2A/NLWeb?

Pridajte sa k [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) a stretnite sa s ostatnými študentmi, navštevujte konzultačné hodiny a získajte odpovede na vaše otázky ohľadom AI agentov.

## Zdroje

- [MCP pre začiatočníkov](https://aka.ms/mcp-for-beginners)  
- [Dokumentácia MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python)

## Predchádzajúca lekcia

[AI agenti v produkcii](../10-ai-agents-production/README.md)

## Nasledujúca lekcia

[Inžinierstvo kontextu pre AI agentov](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->