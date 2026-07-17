# Používanie agentových protokolov (MCP, A2A a NLWeb)

[![Agentic Protocols](../../../translated_images/sk/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Kliknite na obrázok vyššie pre zobrazenie videa tejto lekcie)_

Ako rastie používanie AI agentov, rastie aj potreba protokolov, ktoré zabezpečia štandardizáciu, bezpečnosť a podporia otvorenú inováciu. V tejto lekcii sa budeme venovať 3 protokolom, ktoré sa snažia túto potrebu naplniť – Model Context Protocol (MCP), Agent to Agent (A2A) a Natural Language Web (NLWeb).

## Úvod

V tejto lekcii pokryjeme:

• Ako **MCP** umožňuje AI agentom prístup k externým nástrojom a dátam na dokončenie úloh používateľa.

• Ako **A2A** umožňuje komunikáciu a spoluprácu medzi rôznymi AI agentmi.

• Ako **NLWeb** prináša prirodzené jazykové rozhrania na ľubovoľnú webovú stránku, čo umožňuje AI agentom objavovať a interagovať s jej obsahom.

## Ciele učenia

• **Identifikovať** základný účel a výhody MCP, A2A a NLWeb v kontexte AI agentov.

• **Vysvetliť**, ako každý protokol uľahčuje komunikáciu a interakciu medzi LLM, nástrojmi a inými agentmi.

• **Rozpoznať** rozdielne úlohy, ktoré každý protokol hrá pri budovaní komplexných agentových systémov.

## Model Context Protocol

**Model Context Protocol (MCP)** je otvorený štandard, ktorý poskytuje štandardizovaný spôsob pre aplikácie, ako poskytovať kontext a nástroje LLM. To umožňuje "univerzálny adaptér" ku rôznym dátovým zdrojom a nástrojom, ku ktorým sa AI agenti môžu pripojiť konzistentným spôsobom.

Pozrime sa na zložky MCP, výhody oproti priamemu používaniu API a príklad, ako by AI agenti mohli využiť MCP server.

### Základné komponenty MCP

MCP pracuje na **klient-server architektúre** a základné komponenty sú:

• **Hostia** sú LLM aplikácie (napríklad kódový editor ako VSCode), ktoré začínajú pripojenia k MCP serveru.

• **Klienti** sú komponenty v hostiteľskej aplikácii, ktoré udržiavajú jedno-na-jedno pripojenia so servermi.

• **Servery** sú ľahké programy, ktoré vystavujú špecifické schopnosti.

Súčasťou protokolu sú tri základné primitíva, ktoré predstavujú schopnosti MCP servera:

• **Nástroje**: To sú konkrétne akcie alebo funkcie, ktoré AI agent môže volať pre vykonanie úlohy. Napríklad služba počasia môže vystaviť nástroj „získaj počasie“ alebo server e-commerce môže vystaviť nástroj „kúp produkt“. MCP servery inzerujú názov nástroja, popis a vstupno/výstupný schéma vo svojom zozname schopností.

• **Zdroje**: Sú to dáta alebo dokumenty určené len na čítanie, ktoré MCP server môže poskytovať a klienti ich môžu na požiadanie načítať. Príklady zahŕňajú obsah súborov, záznamy v databáze alebo log súbory. Zdroje môžu byť textové (napr. kód alebo JSON) alebo binárne (napr. obrázky alebo PDF).

• **Výzvy (Prompts)**: Preddefinované šablóny, ktoré poskytujú odporúčané výzvy, umožňujúce zložitejšie pracovné postupy.

### Výhody MCP

MCP ponúka významné výhody pre AI agentov:

• **Dynamické objavovanie nástrojov**: Agenti môžu dynamicky získať zoznam dostupných nástrojov zo servera spolu s popismi ich funkcií. To je oproti tradičným API odlišné, ktoré často vyžadujú statické kódovanie integrácií, takže akákoľvek zmena API vyžaduje aktualizáciu kódu. MCP ponúka prístup „integrovať raz“, čo vedie k väčšej prispôsobivosti.

• **Interoperabilita naprieč LLM**: MCP funguje s rôznymi LLM, poskytuje flexibilitu pri prepínaní základných modelov za účelom lepšieho výkonu.

• **Štandardizovaná bezpečnosť**: MCP obsahuje štandardnú metódu autentifikácie, čo zlepšuje škálovateľnosť pri pridávaní prístupu k ďalším MCP serverom. Je to jednoduchšie ako spravovať rôzne kľúče a typy autentifikácie v tradičných API.

### Príklad MCP

![MCP Diagram](../../../translated_images/sk/mcp-diagram.e4ca1cbd551444a1.webp)

Predstavme si, že používateľ chce rezervovať let pomocou AI asistenta poháňaného MCP.

1. **Pripojenie**: AI asistent (MCP klient) sa pripája k MCP serveru poskytovanému leteckou spoločnosťou.

2. **Objavovanie nástrojov**: Klient sa pýta MCP servera leteckej spoločnosti: "Aké máte dostupné nástroje?" Server odpovedá nástrojmi ako „vyhľadávanie letov” a „rezervácia letu“.

3. **Volanie nástroja**: Používateľ potom požiada AI asistenta: „Prosím vyhľadaj let z Portlandu do Honolulu.“ AI asistent, využívajúc svoj LLM, identifikuje potrebu volať nástroj „vyhľadávanie letov“ a odovzdá príslušné parametre (odletové miesto, cieľ) MCP serveru.

4. **Vykonanie a odpoveď**: MCP server, pôsobiaci ako obálka, uskutoční skutočný hovor na interné API leteckej spoločnosti. Potom prijme informácie o lete (napr. JSON dáta) a odošle ich späť AI asistentovi.

5. **Ďalšia interakcia**: AI asistent predstaví možnosti letov. Keď používateľ vyberie let, asistent môže využiť nástroj „rezervácia letu“ na tom istom MCP serveri a dokončiť rezerváciu.

## Protokol Agent-to-Agent (A2A)

Kým MCP sa sústreďuje na pripájanie LLM k nástrojom, **protokol Agent-to-Agent (A2A)** ide krok ďalej tým, že umožňuje komunikáciu a spoluprácu medzi rôznymi AI agentmi. A2A spája AI agentov naprieč rôznymi organizáciami, prostrediami a technologickými zásobníky na dokončenie spoločnej úlohy.

Preskúmame komponenty a výhody A2A spolu s príkladom jej použitia v našej aplikácii na plánovanie ciest.

### Základné komponenty A2A

A2A sa zameriava na umožnenie komunikácie medzi agentmi a ich spoluprácu na dokončení podúlohy používateľa. Každá súčasť protokolu prispieva k tomu:

#### Agentová karta

Podobne ako MCP server zdieľa zoznam nástrojov, Agentová karta obsahuje:
- Názov agenta.
- **Popis všeobecných úloh**, ktoré agent vykonáva.
- **Zoznam špecifických zručností** s popismi, ktoré pomáhajú ostatným agentom (ale aj ľudským používateľom) pochopiť, kedy a prečo by mali daný agent volať.
- **Aktuálnu URL koncového bodu** agenta.
- **Verziu** a **schopnosti** agenta, napríklad streamovanie odpovedí a push notifikácie.

#### Agentový vykonávateľ

Agentový vykonávateľ je zodpovedný za **predávanie kontextu používateľského chatu vzdialenému agentovi**, ktorý ho potrebuje na pochopenie úlohy na splnenie. V A2A serveri agent používa svoj vlastný veľký jazykový model (LLM), aby spracoval prichádzajúce požiadavky a vykonal úlohy pomocou svojich interných nástrojov.

#### Artefakt

Akonáhle vzdialený agent dokončí požadovanú úlohu, jeho produkt práce sa vytvorí ako artefakt. Artefakt **obsahuje výsledok práce agenta**, **popis toho, čo bolo dokončené**, a **textový kontext** odoslaný cez protokol. Po odoslaní artefaktu sa spojenie s vzdialeným agentom uzavrie, kým nie je znovu potrebné.

#### Fronta udalostí

Táto súčasť sa používa na **spracovanie aktualizácií a odovzdávanie správ**. V produkcii je mimoriadne dôležitá pri agentových systémoch, aby sa zabránilo predčasnému zatvoreniu spojenia medzi agentmi pred dokončením úlohy, najmä keď dokončenie úloh môže trvať dlhší čas.

### Výhody A2A

• **Vylepšená spolupráca**: Umožňuje agentom z rôznych dodávateľov a platforiem vzájomne komunikovať, zdieľať kontext a spolupracovať, čím podporuje plynulú automatizáciu cez tradične oddelené systémy.

• **Flexibilita výberu modelu**: Každý A2A agent si môže vybrať LLM, ktorý používa na spracovanie svojich požiadaviek, čo umožňuje optimalizované alebo doladené modely pre jednotlivých agentov, na rozdiel od jedného LLM pripojenia v niektorých MCP scenároch.

• **Vstavaná autentifikácia**: Autentifikácia je integrovaná priamo do protokolu A2A, čo poskytuje robustné bezpečnostné rámce pre interakcie agentov.

### Príklad A2A

![A2A Diagram](../../../translated_images/sk/A2A-Diagram.8666928d648acc26.webp)

Rozšírme náš scenár rezervácie ciest, ale teraz s použitím A2A.

1. **Požiadavka používateľa na multi-agenta**: Používateľ komunikuje s A2A klientom/agentom "Cestovný agent", napríklad slovami "Prosím, zarezervuj celý výlet do Honolulu na budúci týždeň, vrátane letov, hotela a požičovne áut".

2. **Orchestrácia Cestovným agentom**: Cestovný agent prijíma túto komplexnú požiadavku. Používa svoj LLM na rozmyslenie úlohy a rozhodnutie, že musí komunikovať s inými špecializovanými agentmi.

3. **Komunikácia medzi agentmi**: Cestovný agent potom používa A2A protokol na pripojenie k podriadeným agentom, ako je "Agent leteckej spoločnosti", "Agent hotela" a "Agent požičovne áut", vytvoreným rôznymi spoločnosťami.

4. **Delegované vykonanie úloh**: Cestovný agent posiela jednotlivé úlohy týmto špecializovaným agentom (napr. "Nájdi lety do Honolulu," "Rezervuj hotel," "Požičaj auto"). Každý z týchto agentov, ktorý používa vlastné LLM a svoje nástroje (ktoré môžu byť samy MCP servery), vykoná svoju konkrétnu časť rezervácie.

5. **Konsolidovaná odpoveď**: Keď všetci podriadení agenti dokončia svoje úlohy, Cestovný agent zhrnie výsledky (detaily letov, potvrdenie hotela, rezerváciu požičovne áut) a odošle komplexnú chatovú odpoveď používateľovi.

## Natural Language Web (NLWeb)

Webové stránky dlho predstavovali hlavný spôsob, akým sa používatelia dostávajú k informáciám a dátam na internete.

Pozrime sa na rôzne súčasti NLWeb, výhody NLWeb a príklad, ako náš NLWeb funguje na príklade našej aplikácie cestovania.

### Komponenty NLWeb

- **NLWeb aplikácia (jadrový kód služby)**: Systém, ktorý spracováva otázky v prirodzenom jazyku. Spája rôzne časti platformy na tvorbu odpovedí. Môžete si ho predstaviť ako **motor, ktorý poháňa prirodzené jazykové funkcie** webovej stránky.

- **NLWeb protokol**: Toto je **základná sada pravidiel pre prirodzenú jazykovú interakciu** s webovou stránkou. Odpovede vracia vo formáte JSON (často využívajúcom Schema.org). Jeho cieľom je vytvoriť jednoduchý základ pre „AI Web“, podobne ako HTML umožnil zdieľať dokumenty online.

- **MCP server (Model Context Protocol koncový bod)**: Každá NLWeb inštalácia zároveň funguje ako **MCP server**, čo znamená, že môže **zdieľať nástroje (napríklad metódu „ask“) a dáta** s inými AI systémami. V praxi to robí obsah a schopnosti webu použiteľnými pre AI agentov, čím sa stránka stáva súčasťou širšieho „agentového ekosystému“.

- **Embedovacie modely**: Tieto modely sa používajú na **prekonvertovanie obsahu webu do číselných reprezentácií nazývaných vektory (embeddingy)**. Tieto vektory zachytávajú význam tak, aby ich počítače mohli porovnávať a vyhľadávať. Sú uložené v špeciálnej databáze a používatelia si môžu vybrať, ktorý embedovací model chcú použiť.

- **Vektorová databáza (retrieval mechanizmus)**: Táto databáza **ukladá embeddingy obsahu webu**. Keď niekto položí otázku, NLWeb skontroluje vektorovú databázu, aby rýchlo našiel najrelevantnejšie informácie. Poskytuje rýchly zoznam možných odpovedí, zoradených podľa podobnosti. NLWeb spolupracuje s rôznymi vektorovými úložiskami ako Qdrant, Snowflake, Milvus, Azure AI Search a Elasticsearch.

### NLWeb na príklade

![NLWeb](../../../translated_images/sk/nlweb-diagram.c1e2390b310e5fe4.webp)

Pozrime si opäť našu stránku na rezervácie ciest, tentoraz poháňanú NLWeb.

1. **Zavádzanie dát**: Existujúce katalógy produktov na stránke (napr. zoznamy letov, popisy hotelov, ponuky zájazdov) sú naformátované pomocou Schema.org alebo načítané cez RSS kanály. Nástroje NLWeb tieto štruktúrované dáta spracujú, vytvoria embeddingy a uložia ich do lokálnej alebo vzdialenej vektorovej databázy.

2. **Dotaz v prirodzenom jazyku (človek)**: Používateľ navštívi stránku a namiesto prehliadania menu zadá do chatového rozhrania: „Nájdi mi rodinne priateľský hotel v Honolulu s bazénom na budúci týždeň.“

3. **Spracovanie NLWeb**: NLWeb aplikácia prijme túto požiadavku, pošle ju LLM na pochopenie a súčasne prehľadáva svoju vektorovú databázu za relevantnými hotelovými ponukami.

4. **Presné výsledky**: LLM pomáha interpretovať výsledky vyhľadávania z databázy, vybrať najlepšie zhody na základe kritérií „rodinne priateľský“, „bazén“ a „Honolulu“ a potom formátovať odpoveď v prirodzenom jazyku. Kľúčové je, že odpoveď odkazuje na skutočné hotely z katalógu, čím sa vyhýba vymýšľaniu informácií.

5. **Interakcia AI agenta**: Pretože NLWeb slúži aj ako MCP server, externý AI cestovný agent sa môže pripojiť k tejto NLWeb inštancii. AI agent môže potom použiť MCP metódu `ask`, aby priamo položil otázku webu: `ask("Sú v okolí Honolulu reštaurácie vhodné pre vegánov, ktoré hotel odporúča?")`. NLWeb spracuje túto požiadavku, využije databázu informácií o reštauráciách (ak je načítaná) a vráti štruktúrovanú JSON odpoveď.

### Máte viac otázok o MCP/A2A/NLWeb?

Pridajte sa do [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kde sa stretnete s ďalšími študentmi, zúčastníte sa konzultačných hodín a získate odpovede na otázky o AI agentoch.

## Zdroje

- [MCP pre začiatočníkov](https://aka.ms/mcp-for-beginners)  
- [Dokumentácia MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb repozitár](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framework)

## Predchádzajúca lekcia

[AI agenti v produkcii](../10-ai-agents-production/README.md)

## Nasledujúca lekcia

[Inžinierstvo kontextu pre AI agentov](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->