# Používanie protokolov pre agentov (MCP, A2A a NLWeb)

[![Agentické protokoly](../../../translated_images/sk/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Kliknite na obrázok vyššie pre zobrazenie videa tejto lekcie)_

So zvyšuje použitie AI agentov, rastie aj potreba protokolov, ktoré zabezpečujú štandardizáciu, bezpečnosť a podporujú otvorené inovácie. V tejto lekcii pokryjeme 3 protokoly, ktoré sa snažia tento dopyt naplniť - Model Context Protocol (MCP), Agent to Agent (A2A) a Natural Language Web (NLWeb).

## Úvod

V tejto lekcii preberieme:

• Ako **MCP** umožňuje AI agentom prístup k externým nástrojom a dátam na dokončenie úloh používateľa.

• Ako **A2A** umožňuje komunikáciu a spoluprácu medzi rôznymi AI agentmi.

• Ako **NLWeb** prináša rozhrania v prirodzenom jazyku na akúkoľvek webovú stránku, čím umožňuje AI agentom objavovať a interagovať s obsahom.

## Ciele učenia

• **Identifikovať** hlavný účel a výhody MCP, A2A a NLWeb v kontexte AI agentov.

• **Vysvetliť**, ako každý protokol uľahčuje komunikáciu a interakciu medzi LLM, nástrojmi a inými agentmi.

• **Rozpoznať** odlišné úlohy, ktoré každý protokol zohráva pri budovaní zložitých agentných systémov.

## Model Context Protocol

The **Model Context Protocol (MCP)** je otvorený štandard, ktorý poskytuje štandardizovaný spôsob, ako aplikácie môžu poskytovať kontext a nástroje pre LLM. To umožňuje „univerzálny adaptér“ k rôznym zdrojom dát a nástrojom, ku ktorým sa AI agenti môžu pripájať konzistentným spôsobom.

Pozrime sa na komponenty MCP, výhody oproti priamemu používaniu API a príklad, ako by AI agenti mohli používať MCP server.

### Základné komponenty MCP

MCP pracuje na architektúre **klient-server** a základné komponenty sú:

• **Hostitelia** sú aplikácie LLM (napríklad editor kódu ako VSCode), ktoré začínajú pripojenia k MCP serveru.

• **Klienti** sú komponenty v rámci hostiteľskej aplikácie, ktoré udržiavajú jeden-na-jeden spojenia so servermi.

• **Servery** sú ľahké programy, ktoré vystavujú špecifické schopnosti.

Súčasťou protokolu sú tri základné primitívy, ktoré sú schopnosťami MCP servera:

• **Nástroje**: Ide o diskrétne akcie alebo funkcie, ktoré si AI agent môže zavolať na vykonanie úlohy. Napríklad služba počasia môže vystaviť nástroj „získať počasie“, alebo e‑commerce server môže vystaviť nástroj „kúpiť produkt“. MCP servery v zozname svojich schopností inzerujú názov každého nástroja, popis a vstupno‑výstupné schémy.

• **Zdroje**: Sú to dátové položky alebo dokumenty iba na čítanie, ktoré môže MCP server poskytnúť a ktoré si klienti môžu vyžiadať na požiadanie. Príklady zahŕňajú obsah súborov, záznamy z databázy alebo log súbory. Zdroje môžu byť textové (ako kód alebo JSON) alebo binárne (ako obrázky alebo PDF).

• **Prompty**: Preddefinované šablóny, ktoré poskytujú navrhované výzvy a umožňujú komplexnejšie pracovné postupy.

### Výhody MCP

MCP ponúka významné výhody pre AI agentov:

• **Dynamické zistenie nástrojov**: Agenti môžu dynamicky získať zoznam dostupných nástrojov zo servera spolu s popismi toho, čo robia. To kontrastuje s tradičnými API, ktoré často vyžadujú statické kódovanie integrácií, čo znamená, že akákoľvek zmena API si vyžaduje aktualizácie kódu. MCP ponúka prístup „integrovať raz“, čo vedie k väčšej prispôsobivosti.

• **Interoperabilita medzi LLM**: MCP funguje naprieč rôznymi LLM, čo poskytuje flexibilitu pri prepínaní základných modelov za účelom dosiahnutia lepšieho výkonu.

• **Štandardizovaná bezpečnosť**: MCP obsahuje štandardnú autentifikačnú metódu, čo zlepšuje škálovateľnosť pri pridávaní prístupu k ďalším MCP serverom. To je jednoduchšie než spravovať rôzne kľúče a typy autentifikácie pre rôzne tradičné API.

### Príklad MCP

![Schéma MCP](../../../translated_images/sk/mcp-diagram.e4ca1cbd551444a1.webp)

Predstavte si, že používateľ chce rezervovať let pomocou AI asistenta poháňaného MCP.

1. **Pripojenie**: AI asistent (MCP klient) sa pripojí k MCP serveru poskytovanému leteckou spoločnosťou.

2. **Zistenie nástrojov**: Klient sa opýta MCP servera leteckej spoločnosti: „Aké nástroje máte k dispozícii?“ Server odpovie nástrojmi ako „vyhľadať lety“ a „rezervovať let“.

3. **Vyvolanie nástroja**: Potom požiadate AI asistenta: „Prosím, vyhľadaj let z Portlandu do Honolulu.“ AI asistent, používajúc svoj LLM, identifikuje, že potrebuje zavolať nástroj „vyhľadať lety“ a odovzdá relevantné parametre (odletové miesto, cieľ) MCP serveru.

4. **Vykonanie a odpoveď**: MCP server, pôsobiaci ako obal, vykoná skutočné volanie interného rezervačného API leteckej spoločnosti. Potom prijme informácie o letoch (napr. JSON dáta) a pošle ich späť AI asistentovi.

5. **Ďalšia interakcia**: AI asistent zobrazí možnosti letov. Keď vyberiete let, asistent môže zavolať nástroj „rezervovať let“ na tom istom MCP serveri a dokončiť rezerváciu.

## Protokol Agent‑to‑Agent (A2A)

Kým MCP sa zameriava na prepojenie LLM s nástrojmi, **protokol Agent‑to‑Agent (A2A)** posúva vec ďalej tým, že umožňuje komunikáciu a spoluprácu medzi rôznymi AI agentmi. A2A prepája AI agentov naprieč rôznymi organizáciami, prostrediami a technologickými zásobníkmi, aby dokončili spoločnú úlohu.

Preskúmame komponenty a výhody A2A, spolu s príkladom, ako by sa mohol použiť v našej cestovnej aplikácii.

### Základné komponenty A2A

A2A sa sústreďuje na umožnenie komunikácie medzi agentmi a na to, aby spolu pracovali na dokončení podúlohy používateľa. Každá súčasť protokolu k tomu prispieva:

#### Agentová karta

Podobne ako MCP server zdieľa zoznam nástrojov, Agentová karta obsahuje:
- Názov agenta .
- **popis všeobecných úloh**, ktoré dokončuje.
- **zoznam špecifických zručností** s popismi, ktoré pomáhajú ostatným agentom (alebo aj ľudským používateľom) pochopiť, kedy a prečo by mali daného agenta zavolať.
- **aktuálnu URL koncového bodu** agenta
- **verziu** a **schopnosti** agenta, ako sú streamovanie odpovedí a push notifikácie.

#### Spúšťač agenta

Spúšťač agenta je zodpovedný za **prenesenie kontextu používateľského chatu na vzdialeného agenta**, vzdialený agent to potrebuje, aby pochopil úlohu, ktorú treba splniť. V A2A serveri agent používa svoj vlastný veľký jazykový model (LLM) na parsovanie prichádzajúcich požiadaviek a vykonávanie úloh pomocou vlastných interných nástrojov.

#### Artefakt

Keď vzdialený agent dokončí požadovanú úlohu, jeho výsledok je vytvorený ako artefakt. Artefakt **obsahuje výsledok práce agenta**, **popis toho, čo bolo dokončené**, a **textový kontext**, ktorý je prenesený cez protokol. Po odoslaní artefaktu sa spojenie s vzdialeným agentom zatvorí, až kým nebude opäť potrebné.

#### Fronta udalostí

Táto súčasť sa používa na **spracovanie aktualizácií a prenášanie správ**. Je obzvlášť dôležitá v produkcii pre agentné systémy, aby sa zabránilo zatvoreniu spojenia medzi agentmi skôr, než je úloha dokončená, najmä keď dokončenie úloh môže trvať dlhší čas.

### Výhody A2A

• **Zlepšená spolupráca**: Umožňuje agentom od rôznych dodávateľov a platforiem vzájomne komunikovať, zdieľať kontext a spolupracovať, čo uľahčuje plynulú automatizáciu naprieč tradične odpojenými systémami.

• **Flexibilita výberu modelu**: Každý A2A agent si môže rozhodnúť, ktorý LLM použije na spracovanie svojich požiadaviek, čo umožňuje optimalizované alebo doladené modely pre každého agenta, na rozdiel od jediného LLM pripojenia v niektorých MCP scenároch.

• **Vstavaná autentifikácia**: Autentifikácia je integrovaná priamo do protokolu A2A, čo poskytuje robustný bezpečnostný rámec pre interakcie agentov.

### Príklad A2A

![Diagram A2A](../../../translated_images/sk/A2A-Diagram.8666928d648acc26.webp)

Rozšírme náš scenár rezervácie ciest, tentoraz pomocou A2A.

1. **Požiadavka používateľa na multi‑agenta**: Používateľ komunikuje s „Cestovným agentom“ A2A klientom/agenta, napríklad: „Prosím, rezervuj celý výlet do Honolulu na budúci týždeň, vrátane letov, hotela a požičovne áut“.

2. **Orchestrace Cestovným agentom**: Cestovný agent prijme túto komplexnú požiadavku. Použije svoj LLM na rozmyslenie úlohy a rozhodne, že potrebuje komunikovať s ďalšími špecializovanými agentmi.

3. **Medziagentová komunikácia**: Cestovný agent potom použije protokol A2A na pripojenie k downstream agentom, ako sú „Agent leteckej spoločnosti“, „Agent hotela“ a „Agent požičovne áut“, ktoré sú vytvorené rôznymi spoločnosťami.

4. **Delegované vykonanie úloh**: Cestovný agent pošle konkrétne úlohy týmto špecializovaným agentom (napr. „Nájdite lety do Honolulu“, „Rezervujte hotel“, „Požičajte auto“). Každý z týchto špecializovaných agentov, bežiacich s vlastnými LLM a využívajúcich svoje vlastné nástroje (ktoré môžu byť samy o sebe MCP servery), vykoná svoju časť rezervácie.

5. **Konsolidovaná odpoveď**: Keď všetci downstream agenti dokončia svoje úlohy, Cestovný agent skomplikuje výsledky (detaily letu, potvrdenie hotela, rezerváciu požičovne áut) a pošle komplexnú, chat‑štýlovú odpoveď späť používateľovi.

## Web v prirodzenom jazyku (NLWeb)

Webové stránky boli dlho hlavným spôsobom, ako používatelia pristupujú k informáciám a dátam na internete.

Pozrime sa na rôzne komponenty NLWeb, výhody NLWeb a príklad, ako náš NLWeb funguje na našej cestovnej aplikácii.

### Komponenty NLWeb

- **Aplikácia NLWeb (jadrový servisný kód)**: Systém, ktorý spracováva otázky v prirodzenom jazyku. Spája rôzne časti platformy, aby vytváral odpovede. Môžete si ho predstaviť ako **motor, ktorý poháňa funkcie v prirodzenom jazyku** webovej stránky.

- **Protokol NLWeb**: Toto je **základná sada pravidiel pre interakciu v prirodzenom jazyku** s webovou stránkou. Vráti odpovede v JSON formáte (často používajúc Schema.org). Jeho účelom je vytvoriť jednoduchý základ pre „AI Web“, podobne ako HTML umožnil zdieľanie dokumentov online.

- **MCP server (koncový bod Model Context Protocol)**: Každé NLWeb nastavenie tiež funguje ako **MCP server**. To znamená, že môže **zdieľať nástroje (napríklad metódu „ask“) a dáta** s inými AI systémami. V praxi to umožňuje, aby obsah a schopnosti webu boli použiteľné AI agentmi, čo umožní stránke stať sa súčasťou širšieho „ekosystému agentov“.

- **Modely embeddingov**: Tieto modely sa používajú na **prevod obsahu webovej stránky do číselných reprezentácií nazývaných vektory** (embeddings). Tieto vektory zachytávajú význam tak, aby ich počítače vedeli porovnávať a vyhľadávať. Ukladajú sa v špeciálnej databáze a používatelia si môžu vybrať, ktorý embedding model chcú použiť.

- **Vektorová databáza (mechanizmus vyhľadávania)**: Táto databáza **ukladá embeddingy obsahu webovej stránky**. Keď niekto položí otázku, NLWeb kontroluje vektorovú databázu, aby rýchlo našiel najrelevantnejšie informácie. Poskytne rýchly zoznam možných odpovedí, zoradených podľa podobnosti. NLWeb pracuje s rôznymi systémami ukladania vektorov, ako sú Qdrant, Snowflake, Milvus, Azure AI Search a Elasticsearch.

### NLWeb na príklade

![NLWeb](../../../translated_images/sk/nlweb-diagram.c1e2390b310e5fe4.webp)

Zoberme si opäť náš web na rezerváciu ciest, tentoraz poháňaný NLWeb.

1. **Získavanie dát**: Existujúce produktové katalógy cestovného webu (napr. zoznamy letov, popisy hotelov, balíky výletov) sú formátované pomocou Schema.org alebo nahrané cez RSS feedy. Nástroje NLWeb tieto štruktúrované dáta ingestujú, vytvoria embeddingy a uložia ich do lokálnej alebo vzdialenej vektorovej databázy.

2. **Otázka v prirodzenom jazyku (človek)**: Používateľ navštívi web a namiesto prehľadávania menu napíše do chatového rozhrania: "Nájdite mi rodinne priateľský hotel v Honolulu s bazénom na budúci týždeň".

3. **Spracovanie NLWeb**: Aplikácia NLWeb prijme tento dopyt. Posiela dopyt do LLM na pochopenie a zároveň prehľadne vyhľadáva vo svojej vektorovej databáze relevantné záznamy hotelov.

4. **Presné výsledky**: LLM pomáha interpretovať výsledky vyhľadávania z databázy, identifikovať najlepšie zhody na základe kritérií „rodinne priateľský“, „bazén“ a „Honolulu“, a potom formátovať odpoveď v prirodzenom jazyku. Kľúčové je, že odpoveď odkazuje na skutočné hotely z katalógu webu, čím sa predchádza vymysleným informáciám.

5. **Interakcia AI agenta**: Pretože NLWeb funguje ako MCP server, externý AI cestovný agent sa môže tiež pripojiť k inštancii NLWeb tejto webovej stránky. AI agent potom môže použiť metódu `ask` MCP na priame dotazovanie webu: `ask("Sú v oblasti Honolulu nejaké vegánske reštaurácie odporúčané hotelom?")`. Inštancia NLWeb to spracuje, využívajúc svoju databázu informácií o reštauráciách (ak sú nahraté), a vráti štruktúrovanú JSON odpoveď.

### Máte ďalšie otázky o MCP/A2A/NLWeb?

Pridajte sa na [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) a stretnite sa s ďalšími študentmi, zúčastnite sa konzultačných hodín a získajte odpovede na svoje otázky o AI agentech.

## Zdroje

- [MCP pre začiatočníkov](https://aka.ms/mcp-for-beginners)  
- [Dokumentácia MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framewrok)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o vylúčení zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa usilujeme o presnosť, berte prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu nenesieme zodpovednosť.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->