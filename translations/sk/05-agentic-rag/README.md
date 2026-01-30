[![Agentic RAG](../../../translated_images/sk/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Kliknite na obrázok vyššie a pozrite si video k tejto lekcii)_

# Agentic RAG

Táto lekcia poskytuje komplexný prehľad o Agentic Retrieval-Augmented Generation (Agentic RAG), novom AI paradigme, kde veľké jazykové modely (LLMs) autonómne plánujú svoje ďalšie kroky a zároveň získavajú informácie z externých zdrojov. Na rozdiel od statických vzorcov „získaj a čítaj“ Agentic RAG zahŕňa iteratívne volania LLM, ktoré sa striedajú s volaniami nástrojov alebo funkcií a štruktúrovanými výstupmi. Systém vyhodnocuje výsledky, upravuje dotazy, v prípade potreby používa ďalšie nástroje a pokračuje v tomto cykle, kým nedosiahne uspokojivé riešenie.

## Úvod

Táto lekcia pokryje:

- **Porozumenie Agentic RAG:** Zoznámte sa s novým AI paradigmom, kde veľké jazykové modely (LLMs) autonómne plánujú svoje ďalšie kroky a získavajú informácie z externých dátových zdrojov.
- **Iteratívny štýl Maker-Checker:** Pochopte cyklus iteratívnych volaní LLM, ktoré sa striedajú s volaniami nástrojov alebo funkcií a štruktúrovanými výstupmi, navrhnutý na zlepšenie správnosti a riešenie chybných dotazov.
- **Preskúmanie praktických aplikácií:** Identifikujte scenáre, kde Agentic RAG exceluje, ako napríklad prostredia orientované na správnosť, komplexné interakcie s databázami a rozšírené pracovné postupy.

## Ciele učenia

Po absolvovaní tejto lekcie budete vedieť/rozumieť:

- **Porozumenie Agentic RAG:** Zoznámte sa s novým AI paradigmom, kde veľké jazykové modely (LLMs) autonómne plánujú svoje ďalšie kroky a získavajú informácie z externých dátových zdrojov.
- **Iteratívny štýl Maker-Checker:** Pochopte koncept cyklu iteratívnych volaní LLM, ktoré sa striedajú s volaniami nástrojov alebo funkcií a štruktúrovanými výstupmi, navrhnutý na zlepšenie správnosti a riešenie chybných dotazov.
- **Vlastníctvo procesu uvažovania:** Pochopte schopnosť systému vlastniť proces uvažovania, robiť rozhodnutia o tom, ako pristupovať k problémom bez spoliehania sa na preddefinované cesty.
- **Pracovný postup:** Pochopte, ako agentický model nezávisle rozhoduje o získavaní správ o trendoch na trhu, identifikácii údajov o konkurencii, korelácii interných predajných metrík, syntéze zistení a hodnotení stratégie.
- **Iteratívne cykly, integrácia nástrojov a pamäť:** Zoznámte sa so závislosťou systému na vzorci interakcie v cykloch, udržiavaní stavu a pamäte medzi krokmi, aby sa predišlo opakovaniu cyklov a robili informované rozhodnutia.
- **Riešenie zlyhaní a samokorekcia:** Preskúmajte robustné mechanizmy samokorekcie systému, vrátane iterácie a opätovného dotazovania, používania diagnostických nástrojov a spoliehania sa na ľudský dohľad.
- **Hranice autonómie:** Pochopte obmedzenia Agentic RAG, zamerané na autonómiu špecifickú pre danú oblasť, závislosť od infraštruktúry a rešpektovanie bezpečnostných opatrení.
- **Praktické prípady použitia a hodnota:** Identifikujte scenáre, kde Agentic RAG exceluje, ako napríklad prostredia orientované na správnosť, komplexné interakcie s databázami a rozšírené pracovné postupy.
- **Riadenie, transparentnosť a dôvera:** Zoznámte sa s dôležitosťou riadenia a transparentnosti, vrátane vysvetliteľného uvažovania, kontroly zaujatosti a ľudského dohľadu.

## Čo je Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) je nový AI paradigma, kde veľké jazykové modely (LLMs) autonómne plánujú svoje ďalšie kroky a získavajú informácie z externých zdrojov. Na rozdiel od statických vzorcov „získaj a čítaj“ Agentic RAG zahŕňa iteratívne volania LLM, ktoré sa striedajú s volaniami nástrojov alebo funkcií a štruktúrovanými výstupmi. Systém vyhodnocuje výsledky, upravuje dotazy, v prípade potreby používa ďalšie nástroje a pokračuje v tomto cykle, kým nedosiahne uspokojivé riešenie. Tento iteratívny štýl „maker-checker“ zlepšuje správnosť, rieši chybné dotazy a zabezpečuje vysokokvalitné výsledky.

Systém aktívne vlastní svoj proces uvažovania, prepisuje neúspešné dotazy, volí rôzne metódy získavania informácií a integruje viaceré nástroje—ako napríklad vektorové vyhľadávanie v Azure AI Search, SQL databázy alebo vlastné API—predtým, než dokončí svoju odpoveď. Rozlišujúcou kvalitou agentického systému je jeho schopnosť vlastniť proces uvažovania. Tradičné implementácie RAG sa spoliehajú na preddefinované cesty, ale agentický systém autonómne určuje sekvenciu krokov na základe kvality informácií, ktoré nájde.

## Definícia Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) je nový AI paradigma, kde LLMs nielen získavajú informácie z externých dátových zdrojov, ale aj autonómne plánujú svoje ďalšie kroky. Na rozdiel od statických vzorcov „získaj a čítaj“ alebo starostlivo skriptovaných sekvencií promptov Agentic RAG zahŕňa cyklus iteratívnych volaní LLM, ktoré sa striedajú s volaniami nástrojov alebo funkcií a štruktúrovanými výstupmi. Na každom kroku systém vyhodnocuje získané výsledky, rozhoduje, či upraví dotazy, používa ďalšie nástroje, ak je to potrebné, a pokračuje v tomto cykle, kým nedosiahne uspokojivé riešenie.

Tento iteratívny štýl „maker-checker“ je navrhnutý na zlepšenie správnosti, riešenie chybných dotazov do štruktúrovaných databáz (napr. NL2SQL) a zabezpečenie vyvážených, vysokokvalitných výsledkov. Namiesto spoliehania sa výlučne na starostlivo navrhnuté reťazce promptov systém aktívne vlastní svoj proces uvažovania. Môže prepisovať neúspešné dotazy, voliť rôzne metódy získavania informácií a integrovať viaceré nástroje—ako napríklad vektorové vyhľadávanie v Azure AI Search, SQL databázy alebo vlastné API—predtým, než dokončí svoju odpoveď. To eliminuje potrebu príliš komplexných orchestrálnych rámcov. Namiesto toho relatívne jednoduchý cyklus „volanie LLM → použitie nástroja → volanie LLM → …“ môže priniesť sofistikované a dobre podložené výstupy.

![Agentic RAG Core Loop](../../../translated_images/sk/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## Vlastníctvo procesu uvažovania

Rozlišujúcou kvalitou, ktorá robí systém „agentickým“, je jeho schopnosť vlastniť proces uvažovania. Tradičné implementácie RAG často závisia od toho, že ľudia preddefinujú cestu pre model: reťazec myšlienok, ktorý určuje, čo získať a kedy.  
Ale keď je systém skutočne agentický, rozhoduje interne, ako pristupovať k problému. Nevykonáva len skript; autonómne určuje sekvenciu krokov na základe kvality informácií, ktoré nájde.  
Napríklad, ak je požiadaný o vytvorenie stratégie uvedenia produktu na trh, nespolieha sa výlučne na prompt, ktorý podrobne opisuje celý výskum a rozhodovací pracovný postup. Namiesto toho agentický model nezávisle rozhodne:

1. Získať aktuálne správy o trendoch na trhu pomocou Bing Web Grounding.
2. Identifikovať relevantné údaje o konkurencii pomocou Azure AI Search.
3. Korelovať historické interné predajné metriky pomocou Azure SQL Database.
4. Syntetizovať zistenia do ucelenej stratégie orchestrovanej cez Azure OpenAI Service.
5. Vyhodnotiť stratégiu z hľadiska medzier alebo nekonzistencií, čo môže vyvolať ďalšie kolo získavania informácií.

Všetky tieto kroky—upravovanie dotazov, výber zdrojov, iterácia až do „spokojnosti“ s odpoveďou—sú rozhodnuté modelom, nie predskriptované človekom.

## Iteratívne cykly, integrácia nástrojov a pamäť

![Tool Integration Architecture](../../../translated_images/sk/tool-integration.0f569710b5c17c10.webp)

Agentický systém sa spolieha na vzorec interakcie v cykloch:

- **Počiatočné volanie:** Cieľ používateľa (t.j. používateľský prompt) je prezentovaný LLM.
- **Použitie nástroja:** Ak model identifikuje chýbajúce informácie alebo nejasné pokyny, vyberie nástroj alebo metódu získavania informácií—ako napríklad dotaz na vektorovú databázu (napr. Azure AI Search Hybrid search nad súkromnými dátami) alebo štruktúrované volanie SQL—na získanie ďalšieho kontextu.
- **Hodnotenie a úprava:** Po preskúmaní vrátených údajov model rozhodne, či informácie postačujú. Ak nie, upraví dotaz, vyskúša iný nástroj alebo prispôsobí svoj prístup.
- **Opakovanie až do spokojnosti:** Tento cyklus pokračuje, kým model neurčí, že má dostatok jasnosti a dôkazov na poskytnutie konečnej, dobre premyslenej odpovede.
- **Pamäť a stav:** Pretože systém udržiava stav a pamäť medzi krokmi, môže si spomenúť na predchádzajúce pokusy a ich výsledky, čím sa vyhne opakovaniu cyklov a robí informovanejšie rozhodnutia, ako postupuje.

Postupom času to vytvára pocit vyvíjajúceho sa porozumenia, čo umožňuje modelu navigovať komplexné, viacstupňové úlohy bez potreby neustáleho zásahu človeka alebo preformulovania promptu.

## Riešenie zlyhaní a samokorekcia

Autonómia Agentic RAG zahŕňa aj robustné mechanizmy samokorekcie. Keď systém narazí na slepé uličky—ako napríklad získanie irelevantných dokumentov alebo narazenie na chybné dotazy—môže:

- **Iterovať a opätovne dotazovať:** Namiesto poskytovania nízko hodnotných odpovedí model skúša nové stratégie vyhľadávania, prepisuje dotazy do databázy alebo skúma alternatívne dátové sady.
- **Použiť diagnostické nástroje:** Systém môže použiť ďalšie funkcie navrhnuté na pomoc pri ladení krokov uvažovania alebo potvrdení správnosti získaných údajov. Nástroje ako Azure AI Tracing budú dôležité na umožnenie robustnej pozorovateľnosti a monitorovania.
- **Spoliehať sa na ľudský dohľad:** Pri scenároch s vysokými stávkami alebo opakovanými zlyhaniami môže model označiť neistotu a požiadať o ľudské vedenie. Keď človek poskytne korektívnu spätnú väzbu, model môže túto lekciu začleniť do budúcnosti.

Tento iteratívny a dynamický prístup umožňuje modelu neustále sa zlepšovať, čím zabezpečuje, že nie je len jednorazovým systémom, ale takým, ktorý sa učí zo svojich chýb počas danej relácie.

![Self Correction Mechanism](../../../translated_images/sk/self-correction.da87f3783b7f174b.webp)

## Hranice autonómie

Napriek svojej autonómii v rámci úlohy Agentic RAG nie je ekvivalentom všeobecnej umelej inteligencie. Jeho „agentické“ schopnosti sú obmedzené na nástroje, dátové zdroje a politiky poskytované ľudskými vývojármi. Nemôže si vymýšľať vlastné nástroje ani prekračovať hranice domény, ktoré boli nastavené. Skôr exceluje v dynamickom orchestrálnom využívaní dostupných zdrojov.  
Kľúčové rozdiely oproti pokročilejším formám AI zahŕňajú:

1. **Autonómia špecifická pre doménu:** Systémy Agentic RAG sú zamerané na dosiahnutie cieľov definovaných používateľom v známej doméne, pričom používajú stratégie ako prepisovanie dotazov alebo výber nástrojov na zlepšenie výsledkov.
2. **Závislosť od infraštruktúry:** Schopnosti systému závisia od nástrojov a dát integrovaných vývojármi. Nemôže prekročiť tieto hranice bez zásahu človeka.
3. **Rešpektovanie bezpečnostných opatrení:** Etické smernice, pravidlá súladu a obchodné politiky zostávajú veľmi dôležité. Sloboda agenta je vždy obmedzená bezpečnostnými opatreniami a mechanizmami dohľadu (dúfajme).

## Praktické prípady použitia a hodnota

Agentic RAG exceluje v scenároch vyžadujúcich iteratívne zdokonaľovanie a presnosť:

1. **Prostredia orientované na správnosť:** Pri kontrolách súladu, regulačnej analýze alebo právnom výskume môže agentický model opakovane overovať fakty, konzultovať viaceré zdroje a prepisovať dotazy, kým neprodukuje dôkladne overenú odpoveď.
2. **Komplexné interakcie s databázami:** Pri práci so štruktúrovanými údajmi, kde dotazy často zlyhávajú alebo potrebujú úpravu, systém môže autonómne upravovať svoje dotazy pomocou Azure SQL alebo Microsoft Fabric OneLake, čím zabezpečí, že konečné získanie údajov zodpovedá zámeru používateľa.
3. **Rozšírené pracovné postupy:** Dlhšie relácie sa môžu vyvíjať, keď sa objavia nové informácie. Agentic RAG môže neustále začleňovať nové údaje, meniť stratégie, keď sa dozvie viac o problematike.

## Riadenie, transparentnosť a dôvera

Ako sa tieto systémy stávajú autonómnejšími vo svojom uvažovaní, riadenie a transparentnosť sú kľúčové:

- **Vysvetliteľné uvažovanie:** Model môže poskytnúť záznam o dotazoch, ktoré vykonal, zdrojoch, ktoré konzultoval, a krokoch uvažovania, ktoré podnikol na dosiahnutie svojho záveru. Nástroje ako Azure AI Content Safety a Azure AI Tracing / GenAIOps môžu pomôcť udržiavať transparentnosť a zmierňovať riziká.
- **Kontrola zaujatosti a vyvážené získavanie:** Vývojári môžu doladiť stratégie získavania informácií, aby zabezpečili, že sa zohľadnia vyvážené, reprezentatívne dátové zdroje, a pravidelne auditovať výstupy na detekciu zaujatosti alebo skreslených vzorcov pomocou vlastných modelov pre pokročilé dátové organizácie využívajúce Azure Machine Learning.
- **Ľudský dohľad a súlad:** Pri citlivých úlohách zostáva ľudská kontrola nevyhnutná. Agentic RAG nenahrádza ľudský úsudok pri rozhodnutiach s vysokými stávkami—dopĺňa ho tým, že poskytuje dôkladnejšie overené možnosti.

Mať nástroje, ktoré poskytujú jasný záznam o akciách, je nevyhnutné. Bez nich môže byť ladenie viacstupňového procesu veľmi náročné. Pozrite si nasledujúci príklad
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Kompletný sprievodca agentovo založeným vyhľadávaním a rozšírenou generáciou – Novinky z generácie RAG</a>
- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: zrýchlite svoj RAG pomocou reformulácie dotazov a samostatného dotazovania! Hugging Face Open-Source AI Cookbook</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Pridávanie agentových vrstiev do RAG</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Budúcnosť asistentov znalostí: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Ako vytvoriť systémy Agentic RAG</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Používanie služby Azure AI Foundry Agent na škálovanie vašich AI agentov</a>

### Akademické články

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Iteratívne zdokonaľovanie so spätnou väzbou od seba</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Jazykoví agenti s verbálnym posilňovacím učením</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Veľké jazykové modely sa môžu samy korigovať pomocou interaktívneho kritizovania nástrojov</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation: Prehľad o Agentic RAG</a>

## Predchádzajúca lekcia

[Šablóna dizajnu pre používanie nástrojov](../04-tool-use/README.md)

## Nasledujúca lekcia

[Budovanie dôveryhodných AI agentov](../06-building-trustworthy-agents/README.md)

---

**Upozornenie**:  
Tento dokument bol preložený pomocou služby AI prekladu [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, berte na vedomie, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.