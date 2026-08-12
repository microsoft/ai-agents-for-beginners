[![Agentic RAG](../../../translated_images/sk/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Kliknite na obrázok vyššie pre zobrazenie videa k tejto lekcii)_

# Agentic RAG

Táto lekcia poskytuje komplexný prehľad o Agentic Retrieval-Augmented Generation (Agentic RAG), novom paradigme AI, kde veľké jazykové modely (LLM) samostatne plánujú svoje ďalšie kroky, pričom získavajú informácie z externých zdrojov. Na rozdiel od statických vzorov načítavania a následného čítania, Agentic RAG zahŕňa iteratívne volania LLM, striedané s volaniami nástrojov alebo funkcií a so štruktúrovanými výstupmi. Systém hodnotí výsledky, vylepšuje dotazy, v prípade potreby vyvoláva ďalšie nástroje a pokračuje v tomto cykle, kým nedosiahne uspokojivé riešenie.

## Úvod

Táto lekcia pokrýva

- **Porozumenie Agentic RAG:** Naučte sa o novom paradigme v AI, kde veľké jazykové modely (LLM) samostatne plánujú svoje ďalšie kroky pri získavaní informácií z externých dátových zdrojov.
- **Pochopenie štýlu iteratívneho tvorcu-kontrolóra:** Pochopte cyklus iteratívnych volaní LLM, striedaných s volaniami nástrojov alebo funkcií a so štruktúrovanými výstupmi, navrhnutý na zvýšenie správnosti a zvládanie nesprávne vytvorených dotazov.
- **Preskúmanie praktických aplikácií:** Identifikujte scenáre, kde Agentic RAG vyniká, napríklad v prostrediach nárokovaných na správnosť, pri zložitých interakciách s databázami a pri rozšírených pracovných tokoch.

## Výučbové ciele

Po dokončení tejto lekcie budete vedieť/pochopíte:

- **Porozumenie Agentic RAG:** Naučte sa o novom paradigme v AI, kde veľké jazykové modely (LLM) samostatne plánujú svoje ďalšie kroky pri získavaní informácií z externých dátových zdrojov.
- **Iteratívny štýl tvorcu-kontrolóra:** Pochopte koncept cyklu iteratívnych volaní LLM, striedaných s volaniami nástrojov alebo funkcií a so štruktúrovanými výstupmi, navrhnutý na zvýšenie správnosti a zvládanie nesprávne vytvorených dotazov.
- **Ovplyvnenie procesu uvažovania:** Pochopte schopnosť systému prevziať kontrolu nad svojím procesom uvažovania, robiť rozhodnutia o prístupe k problémom bez spolahladania sa na vopred definované cesty.
- **Pracovný tok:** Pochopte, ako agentný model nezávisle rozhoduje o vyhľadávaní správ o trendoch na trhu, identifikovaní údajov konkurencie, korelácie vnútorných predajných metrik, syntéze zistení a hodnotení stratégie.
- **Iteratívne slučky, integrácia nástrojov a pamäť:** Naučte sa o závislosti systému na vzorci slučkovej interakcie, udržiavaní stavu a pamäte cez kroky, aby sa predišlo opakujúcim sa slučkám a podporilo sa informované rozhodovanie.
- **Riešenie chýb a samokorekcia:** Preskúmajte robustné mechanizmy samokorekcie systému, vrátane iterácií a opätovných dotazov, využívania diagnostických nástrojov a spoliehania sa na ľudský dohľad.
- **Hranice agentnosti:** Pochopte obmedzenia Agentic RAG, zamerané na autonómiu špecifickú pre doménu, závislosť od infraštruktúry a rešpektovanie bezpečnostných opatrení.
- **Praktické prípady použitia a hodnota:** Identifikujte scenáre, kde Agentic RAG vyniká, napríklad v prostrediach kladúcich dôraz na správnosť, zložitých interakciách s databázami a rozšírených pracovných tokoch.
- **Riadenie, transparentnosť a dôvera:** Naučte sa o dôležitosti riadenia a transparentnosti vrátane vysvetliteľného uvažovania, kontroly zaujatosti a ľudského dohledu.

## Čo je Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) je nová paradigma AI, kde veľké jazykové modely (LLM) samostatne plánujú svoje ďalšie kroky pri získavaní informácií z externých zdrojov. Na rozdiel od statických vzorov načítavania a následného čítania, Agentic RAG zahŕňa iteratívne volania LLM, striedané s volaniami nástrojov alebo funkcií a so štruktúrovanými výstupmi. Systém hodnotí výsledky, vylepšuje dotazy, v prípade potreby vyvoláva ďalšie nástroje a pokračuje v tomto cykle, kým nedosiahne uspokojivé riešenie. Tento iteratívny „tvorca-kontrolór“ štýl zlepšuje správnosť, zvláda nesprávne dotazy a zabezpečuje vysokú kvalitu výsledkov.

Systém aktívne prevziať kontrolu nad svojím procesom uvažovania, prepíše zlyhané dotazy, vyberie rôzne metódy vyhľadávania a integruje viacero nástrojov – ako napríklad vyhľadávanie vektorov v Azure AI Search, SQL databázy alebo vlastné API – pred konečným zodpovedaním otázky. Výraznou vlastnosťou agentného systému je jeho schopnosť riadiť vlastný proces uvažovania. Tradičné implementácie RAG sa spoliehajú na vopred definované cesty, no agentný systém autonómne určuje poradie krokov na základe kvality nájdených informácií.

## Definovanie Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) je nová paradigma v AI vývoji, kde LLM nielen získavajú informácie z externých dátových zdrojov, ale tiež autonómne plánujú svoje ďalšie kroky. Na rozdiel od statických vzorov načítavania a následného čítania alebo starostlivo napisanych sekvencií promptov, Agentic RAG zahŕňa slučku iteratívnych volaní LLM, striedaných s volaniami nástrojov alebo funkcií a so štruktúrovanými výstupmi. V každom kroku systém hodnotí získané výsledky, rozhoduje, či dotazy vylepšiť, vyvoláva ďalšie nástroje podľa potreby a pokračuje, kým nedosiahne uspokojivé riešenie.

Tento iteratívny „tvorca-kontrolór“ štýl je navrhnutý tak, aby zlepšil správnosť, zvládal nesprávne dotazy k štruktúrovaným databázam (napr. NL2SQL) a zabezpečil vyvážené, vysokokvalitné výsledky. Namiesto spoliehania sa výlučne na starostlivo navrhnuté reťazce promptov, systém aktívne kontroluje svoj proces uvažovania. Vie prepísať nezdařilé dotazy, vybrať odlišné metódy vyhľadávania a integrovať viacero nástrojov – ako napríklad vyhľadávanie vektorov v Azure AI Search, SQL databázy alebo vlastné API – pred konečným zodpovedaním otázky. Odpadá potreba komplexných rámcov orchestrácie. Relatívne jednoduchá slučka „volanie LLM → použitie nástroja → volanie LLM → …“ môže vytvoriť sofistikované a dobre podložené výstupy.

![Agentic RAG Core Loop](../../../translated_images/sk/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## Prevzatie kontroly nad procesom uvažovania

Rozlišujúcou kvalitou, ktorá robí systém „agentným“, je jeho schopnosť prevziať kontrolu nad procesom uvažovania. Tradičné implementácie RAG často závisia od ľudí, ktorí vopred definujú dráhu modelu: reťazec myšlienok, ktorý stanovuje, čo a kedy načítať.
Ak je však systém skutočne agentný, rozhoduje vnútorne, ako pristúpiť k problému. Nielen, že vykonáva skript, ale autonómne určuje sekvenciu krokov založených na kvalite nájdených informácií.
Napríklad, ak je požiadaný vytvoriť stratégiu uvedenia produktu na trh, nespolieha sa iba na prompt, ktorý popisuje celý výskumný a rozhodovací pracovný tok. Namiesto toho agentný model nezávisle rozhoduje:

1. Získať aktuálne správy o trendoch na trhu pomocou Bing Web Grounding
2. Identifikovať relevantné údaje konkurencie pomocou Azure AI Search.
3. Korelovať historické interné predajné metriky pomocou Azure SQL Database.
4. Syntetizovať zistenia do ucelenej stratégie orchestrácie prostredníctvom Azure OpenAI Service.
5. Vyhodnotiť stratégiu, či neobsahuje medzery alebo nezrovnalosti, a v prípade potreby vyvolať ďalšie vyhľadávanie.
Všetky tieto kroky – vylepšovanie dotazov, výber zdrojov, iterovanie, kým nie je odpoveď „uspokojivá“ – sú rozhodované modelom, nie vopred napísané človekom.

## Iteratívne slučky, integrácia nástrojov a pamäť

![Tool Integration Architecture](../../../translated_images/sk/tool-integration.0f569710b5c17c10.webp)

Agentný systém sa spolieha na vzorec slučkovitej interakcie:

- **Počiatočné volanie:** Cieľ používateľa (teda užívateľský prompt) sa predloží LLM.
- **Volanie nástroja:** Ak model identifikuje chýbajúce informácie alebo nejasné inštrukcie, vyberie nástroj alebo metódu vyhľadávania – napríklad dotaz do vektorovej databázy (napr. Azure AI Search Hybrid search nad súkromnými údajmi) alebo štruktúrovaný SQL dotaz – na získanie ďalšieho kontextu.
- **Hodnotenie a vylepšovanie:** Po preskúmaní vrátených údajov model rozhodne, či sú informácie dostatočné. Ak nie, vylepší dotaz, vyskúša iný nástroj alebo upraví prístup.
- **Opakovať, kým je spokojný:** Tento cyklus pokračuje, kým model nerozhodne, že má dostatočnú jasnosť a dôkazy na doručenie konečnej, dobre premyslenej odpovede.
- **Pamäť a stav:** Keďže systém udržiava stav a pamäť naprieč krokmi, dokáže si pamätať predchádzajúce pokusy a ich výsledky, vyhýba sa opakovaným slučkám a robí informovanejšie rozhodnutia počas procesu.

Postupom času to vytvára pocit vyvíjajúceho sa porozumenia, ktorý umožňuje modelu pohybovať sa v zložitých úlohách pozostávajúcich z viacerých krokov bez potreby neustáleho zásahu človeka alebo preformulovania promptu.

## Riešenie chýb a samokorekcia

Autonómia Agentic RAG zahŕňa tiež robustné mechanizmy samokorekcie. Keď systém narazí na mŕtve konce – napríklad získava nerelevantné dokumenty alebo narazí na nesprávne dotazy – môže:

- **Iterovať a opakovane dotazovať:** Namiesto vrátenia málo hodnotných odpovedí model skúša nové stratégie vyhľadávania, prepíše databázové dotazy alebo sa pozrie na alternatívne dátové súbory.
- **Použiť diagnostické nástroje:** Systém môže vyvolať ďalšie funkcie, ktoré mu pomôžu debugovať kroky uvažovania alebo potvrdiť správnosť získaných údajov. Nástroje ako Azure AI Tracing budú dôležité pre zabezpečenie robustnej pozorovateľnosti a monitorovania.
- **Spoliehanie sa na ľudský dohľad:** Pri vysoko rizikových alebo opakovane zlyhávajúcich scénároch môže model signalizovať neistotu a žiadať o pomoc človeka. Po poskytnutí korektívnej spätnej väzby model túto lekciu zapracuje do budúcna.

Tento iteratívny a dynamický prístup umožňuje modelu neustále sa zlepšovať, čo zabezpečuje, že nie je jednorazový systém, ale taký, ktorý sa počas danej relácie učí zo svojich omylov.

![Self Correction Mechanism](../../../translated_images/sk/self-correction.da87f3783b7f174b.webp)

## Hranice agentnosti

Napriek jeho autonómii v rámci úlohy Agentic RAG nie je analógiou k Všeobecnej umelej inteligencii. Jeho „agentné“ schopnosti sú obmedzené na nástroje, dátové zdroje a zásady poskytované ľudskými vývojármi. Nemôže vynájsť vlastné nástroje alebo prekročiť hranice domény, ktoré boli stanovené. Skôr exceluje v dynamickej orchestrácii dostupných zdrojov.
Kľúčové rozdiely od pokročilejších foriem AI zahŕňajú:

1. **Autonómia špecifická pre doménu:** Agentic RAG systémy sa zameriavajú na dosiahnutie užívateľmi definovaných cieľov v známej doméne, využívajúc stratégie ako prepísanie dotazu alebo výber nástroja na zlepšenie výsledkov.
2. **Závislosť od infraštruktúry:** Schopnosti systému závisia od nástrojov a dát integrovaných vývojármi. Nemôže prekročiť tieto hranice bez ľudského zásahu.
3. **Rešpektovanie bezpečnostných opatrení:** Etické usmernenia, pravidlá dodržiavania predpisov a podnikové politiky zostávajú veľmi dôležité. Sloboda agenta je vždy obmedzená bezpečnostnými opatreniami a dohľadovými mechanizmami (dúfajme).

## Praktické prípady použitia a hodnota

Agentic RAG vyniká v scenároch vyžadujúcich iteratívne vylepšovanie a presnosť:

1. **Prostredia kladúce dôraz na správnosť:** Pri kontrolách súladu, regulačných analýzach alebo právnom výskume môže agentný model opakovane overovať fakty, konzultovať viacero zdrojov a prepísať dotazy, kým nevytvorí dôkladne overenú odpoveď.
2. **Zložité interakcie s databázami:** Pri práci s štruktúrovanými údajmi, kde dotazy často zlyhávajú alebo sa vyžaduje ich úprava, systém môže autonómne vylepšovať dotazy pomocou Azure SQL alebo Microsoft Fabric OneLake, zabezpečujúc, že konečné vyhľadanie zodpovedá zámeru používateľa.
3. **Rozšírené pracovné toky:** Dlhšie relácie môžu pokračovať, keď sa objavia nové informácie. Agentic RAG môže neustále začleňovať nové dáta a meniť stratégie podľa toho, ako sa dozvedá viac o probléme.

## Riadenie, transparentnosť a dôvera

Ako sa tieto systémy stávajú autonómnejšími vo svojom uvažovaní, riadenie a transparentnosť sú kľúčové:

- **Vysvetliteľné uvažovanie:** Model môže poskytnúť auditný záznam dotazov, ktoré urobil, zdrojov, ktoré konzultoval, a krokov uvažovania, ktoré podnikol na dosiahnutie záveru. Nástroje ako Azure AI Content Safety a Azure AI Tracing / GenAIOps môžu pomôcť udržať transparentnosť a zmierniť riziká.
- **Kontrola zaujatosti a vyvážené vyhľadávanie:** Vývojári môžu doladiť vyhľadávacie stratégie, aby sa zabezpečilo, že sa zvažujú vyvážené, reprezentatívne zdroje údajov, a pravidelne kontrolovať výstupy na zistenie zaujatostí alebo skreslených vzorcov pomocou vlastných modelov pre pokročilé organizácie dátovej vedy využívajúce Azure Machine Learning.
- **Ľudský dohľad a súlad:** Pri citlivých úlohách zostáva ľudský prehľad nevyhnutný. Agentic RAG nenahrádza ľudský úsudok v rozhodnutiach s vysokým rizikom – dopĺňa ho tým, že poskytuje dôkladnejšie overené možnosti.

Mať nástroje, ktoré poskytujú jasný záznam akcií, je zásadné. Bez nich je ladenie viacstupňového procesu veľmi ťažké. Pozrite si nasledujúci príklad od Literal AI (spoločnosť za Chainlit) pre beh agenta:

![AgentRunExample](../../../translated_images/sk/AgentRunExample.471a94bc40cbdc0c.webp)

## Záver

Agentic RAG predstavuje prirodzený vývoj v tom, ako AI systémy zvládajú zložité, dátovo náročné úlohy. Prijatím vzorca slučkovitej interakcie, autonómnym výberom nástrojov a vylepšovaním dotazov až do dosiahnutia vysoko kvalitného výsledku systém prekračuje statické sledovanie promptov smerom k adaptívnemu, kontextovo uvedomelému rozhodovaciemu systému. Hoci je stále obmedzený infraštruktúrami a etickými zásadami definovanými ľuďmi, tieto agentné schopnosti umožňujú bohatšie, dynamickejšie a nakoniec užitočnejšie interakcie AI pre firmy aj koncových používateľov.

### Máte ďalšie otázky o Agentic RAG?

Pridajte sa k [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D) a stretnite sa s ďalšími študentmi, zúčastnite sa konzultačných hodín a získajte odpovede na svoje otázky o AI agentoch.

## Doplnkové zdroje

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">Implementácia Retrieval Augmented Generation (RAG) s Azure OpenAI Service: Naučte sa, ako používať vlastné dáta so službou Azure OpenAI Service. Tento modul Microsoft Learn poskytuje komplexný návod na implementáciu RAG</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Hodnotenie generatívnych AI aplikácií s Microsoft Foundry: Tento článok pokrýva hodnotenie a porovnanie modelov na verejne dostupných dátových sadách, vrátane Agentic AI aplikácií a RAG architektúr</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Čo je Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Kompletný sprievodca agentovo založenou retrieval augmented generation – novinky z generácie RAG</a>

- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: zrýchlite svoj RAG pomocou reformulácie dopytov a samodopytovania! Open-Source AI Cookbook od Hugging Face</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Pridanie agentickej vrstvy do RAG</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Budúcnosť asistentov znalostí: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Ako vytvoriť agentické RAG systémy</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Použitie služby Microsoft Foundry Agent na škálovanie AI agentov</a>

### Akademické články

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Iteratívne zlepšovanie s vlastnou spätnou väzbou</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Jazykoví agenti s verbálnym posilňovaným učením</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Veľké jazykové modely sa môžu samokorigovať pomocou interaktívnej kritiky nástrojmi</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation: Prehľad agentického RAG</a>

## Rýchly test tohto agenta (voliteľné)

Po naučení sa nasadzovať agentov v [Lekcii 16](../16-deploying-scalable-agents/README.md) môžete rýchlo otestovať `TravelRAGAgent` z tejto lekcie — overiť, že jeho odpovede zostávajú zakotvené v databáze znalostí — pomocou [`tests/lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json). Pre informácie, ako test spustiť, si pozrite [`tests/README.md`](../tests/README.md).

## Predchádzajúca lekcia

[Vzor použitia nástroja](../04-tool-use/README.md)

## Nasledujúca lekcia

[Budovanie dôveryhodných AI agentov](../06-building-trustworthy-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->