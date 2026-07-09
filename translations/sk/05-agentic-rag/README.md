[![Agentic RAG](../../../translated_images/sk/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Kliknite na obrázok vyššie pre zobrazenie videa tejto lekcie)_

# Agentic RAG

Táto lekcia poskytuje komplexný prehľad o Agentic Retrieval-Augmented Generation (Agentic RAG), novom paradigme AI, kde veľké jazykové modely (LLM) samostatne plánujú svoje ďalšie kroky, zatiaľ čo získavajú informácie z externých zdrojov. Na rozdiel od statických vzorov „retrieve-then-read“ Agentic RAG zahŕňa iteratívne volania na LLM, ktoré sú prerušované volaniami nástrojov alebo funkcií a štruktúrovanými výstupmi. Systém vyhodnocuje výsledky, zdokonaľuje dopyty, v prípade potreby aktivuje ďalšie nástroje a pokračuje v tomto cykle, kým nie je dosiahnuté uspokojivé riešenie.

## Úvod

Táto lekcia bude zahŕňať

- **Pochopenie Agentic RAG:** Naučte sa o vyvíjajúcej sa paradigme v AI, kde veľké jazykové modely (LLM) samostatne plánujú svoje ďalšie kroky, pričom získavajú informácie z externých zdrojov dát.
- **Pochopenie iteratívneho maker-checker štýlu:** Pochopte cyklus iteratívnych volaní LLM, prerušovaných volaniami nástrojov alebo funkcií a štruktúrovanými výstupmi, navrhnutý na zlepšenie správnosti a zvládanie poškodených dopytov.
- **Preskúmanie praktických použití:** Identifikujte scenáre, kde Agentic RAG vyniká, ako sú prostredia orientované na správnosť, zložité interakcie s databázami a rozšírené pracovné toky.

## Ciele učenia

Po dokončení tejto lekcie budete vedieť/pochopíte:

- **Pochopenie Agentic RAG:** Naučíte sa o vyvíjajúcej sa paradigme v AI, kde veľké jazykové modely (LLM) samostatne plánujú svoje ďalšie kroky, pričom získavajú informácie z externých zdrojov dát.
- **Iteratívny maker-checker štýl:** Pochopíte koncept cyklu iteratívnych volaní LLM, prerušovaných volaniami nástrojov alebo funkcií a štruktúrovanými výstupmi, navrhnutý na zlepšenie správnosti a zvládanie poškodených dopytov.
- **Ovládanie procesu uvažovania:** Pochopíte schopnosť systému vlastniť svoj proces uvažovania, robiť rozhodnutia, ako pristupovať k problémom bez spoliehania sa na preddefinované cesty.
- **Pracovný tok:** Pochopíte, ako agentný model samostatne rozhoduje o získavaní správ o trendoch trhu, identifikácii údajov konkurentov, korelácii interných predajných ukazovateľov, syntetizovaní zistení a vyhodnocovaní stratégie.
- **Iteratívne cykly, integrácia nástrojov a pamäť:** Naučíte sa o spoliehaní systému na cyklický interakčný vzor, ktorý udržuje stav a pamäť naprieč krokmi, aby sa zabránilo opakujúcim sa slučkám a umožnilo robiť informované rozhodnutia.
- **Zvládanie chybových režimov a sebaopravovanie:** Preskúmate robustné mechanizmy sebaopravovania systému, vrátane iterácií a opätovného dopytovania, používania diagnostických nástrojov a zálohovania na ľudský dohľad.
- **Hranice autonómie:** Pochopíte obmedzenia Agentic RAG, sústredené na autonómiu špecifickú pre doménu, závislosť na infraštruktúre a rešpektovanie bezpečnostných obmedzení.
- **Praktické prípady použitia a hodnota:** Identifikujete scenáre, kde Agentic RAG vyniká, ako sú prostredia orientované na správnosť, zložité interakcie s databázami a rozšírené pracovné toky.
- **Riadenie, transparentnosť a dôvera:** Naučíte sa o význame riadenia a transparentnosti, vrátane vysvetliteľného uvažovania, kontroly zaujatosti a ľudského dohľadu.

## Čo je Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) je vyvíjajúca sa paradigma AI, kde veľké jazykové modely (LLM) samostatne plánujú svoje ďalšie kroky, pričom ťažia informácie z externých zdrojov. Na rozdiel od statických vzorov „retrieve-then-read“ Agentic RAG zahŕňa opakované volania na LLM, prerušované volaniami nástrojov alebo funkcií a štruktúrovanými výstupmi. Systém vyhodnocuje výsledky, zdokonaľuje dopyty, podľa potreby aktivuje ďalšie nástroje a pokračuje v tomto cykle, kým nedosiahne uspokojivé riešenie. Tento iteratívny „maker-checker“ štýl zlepšuje správnosť, zvládanie poškodených dopytov a zabezpečuje vysokokvalitné výsledky.

Systém aktívne vlastní svoj proces uvažovania, prepíše zlyhané dopyty, vyberie rôzne metódy získavania informácií a integruje viac nástrojov — ako vyhľadávanie vektorov v Azure AI Search, SQL databázy alebo vlastné API — pred finalizáciou odpovede. Rozlišujúcou vlastnosťou agentného systému je jeho schopnosť vlastniť proces uvažovania. Tradičné implementácie RAG sa spoliehajú na preddefinované cesty, ale agentný systém autonómne určuje sekvenciu krokov na základe kvality nájdených informácií.

## Definovanie Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) je vyvíjajúca sa paradigma v rozvoji AI, kde LLM nielen získavajú informácie z externých dátových zdrojov, ale aj samostatne plánujú svoje ďalšie kroky. Na rozdiel od statických vzorov „retrieve-then-read“ alebo starostlivo napísaných sekvencií výziev, Agentic RAG zahŕňa slučku iteratívnych volaní na LLM, prerušovaných volaniami nástrojov alebo funkcií a štruktúrovanými výstupmi. Pri každom kroku systém vyhodnocuje dosiahnuté výsledky, rozhoduje, či dopyty vylepšiť, aktivuje ďalšie nástroje podľa potreby a pokračuje v tomto cykle, kým nedosiahne uspokojivý výsledok.

Tento iteratívny „maker-checker“ štýl prevádzky je navrhnutý na zlepšenie správnosti, zvládanie poškodených dopytov do štruktúrovaných databáz (napr. NL2SQL) a zabezpečenie vyvážených, kvalitných výsledkov. Namiesto spoliehania sa výhradne na starostlivo navrhnuté reťazce výziev systém aktívne vlastní svoj proces uvažovania. Môže prepísať neúspešné dopyty, zvoliť rôzne metódy získavania informácií a integrovať viacero nástrojov — ako vyhľadávanie vektorov v Azure AI Search, SQL databázy alebo vlastné API — skôr než finalizuje svoju odpoveď. Tým sa odstraňuje potreba príliš komplexných rámcov orchestrácie. Namiesto toho môže relatívne jednoduchý cyklus „volanie LLM → použitie nástroja → volanie LLM → …“ priniesť sofistikované a dobre podložené výstupy.

![Agentic RAG Core Loop](../../../translated_images/sk/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## Ovládanie procesu uvažovania

Rozlišujúcou vlastnosťou, ktorá robí systém „agentným“, je jeho schopnosť vlastniť proces uvažovania. Tradičné implementácie RAG často závisia na ľuďoch, ktorí pre model preddefinujú cestu: reťazec myšlienok, ktorý naznačuje, čo a kedy vyhľadávať.
Ale keď je systém skutočne agentný, rozhoduje interne, ako k problému pristúpiť. Nevykonáva len skript; autonómne určuje sekvenciu krokov na základe kvality nájdených informácií.
Napríklad, ak je požiadaný vytvoriť stratégiu uvádzania produktu na trh, nespolieha sa výhradne na výzvu, ktorá vypisuje celý výskumný a rozhodovací proces. Namiesto toho agentný model samostatne rozhodne:

1. Získať aktuálne správy o trendoch trhu pomocou Bing Web Grounding
2. Identifikovať relevantné údaje konkurentov pomocou Azure AI Search.
3. Korelovať historické interné predajné metriky pomocou Azure SQL Database.
4. Syntetizovať zistenia do súdržnej stratégie orchestranej cez Azure OpenAI Service.
5. Vyhodnotiť stratégiu na medzery alebo nezrovnalosti a v prípade potreby vyvolať ďalšie kolo získavania informácií.
Všetky tieto kroky – zdokonaľovanie dopytov, výber zdrojov, iterovanie kým nie je odpoveď „uspokojivá“ – rozhoduje model, nie človek, ktorý vopred napísal scenár.

## Iteratívne slučky, integrácia nástrojov a pamäť

![Tool Integration Architecture](../../../translated_images/sk/tool-integration.0f569710b5c17c10.webp)

Agentný systém sa spolieha na cyklický interakčný vzor:

- **Počiatočné volanie:** Cieľ používateľa (t.j. používateľská požiadavka) je predložený LLM.
- **Volanie nástroja:** Ak model identifikuje chýbajúce informácie alebo nejasné inštrukcie, vyberie nástroj alebo metódu získavania – napr. dotaz do vektorovej databázy (napr. hybridné vyhľadávanie Azure AI Search nad súkromnými dátami) alebo štruktúrovaný SQL dotaz – na získanie ďalšieho kontextu.
- **Hodnotenie a zdokonaľovanie:** Po preskúmaní vrátených údajov model rozhodne, či sú informácie postačujúce. Ak nie, zdokonalí dopyt, vyskúša iný nástroj alebo upraví svoj prístup.
- **Opakovanie, kým spokojný:** Tento cyklus pokračuje, kým model nerozhodne, že má dostatok jasno- stí a dôkazov na dodanie konečnej dobre prepracovanej odpovede.
- **Pamäť a stav:** Pretože systém udržiava stav a pamäť naprieč krokmi, môže si pamätať predchádzajúce pokusy a ich výsledky, vyhýbať sa opakujúcim sa slučkám a robiť informovanejšie rozhodnutia počas postupu.

Postupom času to vytvára pocit vyvíjajúceho sa porozumenia, umožňujúci modelu orientovať sa v zložitých, viackrokových úlohách bez potreby neustáleho ľudského zásahu alebo prepracovania výzvy.

## Zvládanie chybových režimov a sebaopravovanie

Autonómia Agentic RAG tiež zahŕňa robustné mechanizmy sebaopravovania. Keď systém narazí na slepé uličky – ako získanie nerelevantných dokumentov alebo stretávanie sa s poškodenými dopytmi – môže:

- **Iterovať a opätovne dopytovať:** Namiesto vracania málo hodnotných odpovedí model skúša nové stratégie vyhľadávania, prepíše databázové dopyty alebo prezerá alternatívne dátové sady.
- **Použiť diagnostické nástroje:** Systém môže vyvolať ďalšie funkcie určené na pomoc pri ladení krokov uvažovania alebo na potvrdenie správnosti získaných údajov. Nástroje ako Azure AI Tracing budú dôležité pre umožnenie robustnej pozorovateľnosti a monitorovania.
- **Záloha na ľudský dohľad:** Pri vysoko rizikových alebo opakovane zlyhávajúcich scénároch môže model označiť neistotu a požiadať o ľudské vedenie. Akonáhle človek poskytne korektívnu spätnú väzbu, model môže túto lekciu zapracovať do budúcnosti.

Tento iteratívny a dynamický prístup umožňuje modelu neustále sa zlepšovať, zabezpečujúc, že nejde o jednorazový systém, ale o systém, ktorý sa učí zo svojich omylov počas danej relácie.

![Self Correction Mechanism](../../../translated_images/sk/self-correction.da87f3783b7f174b.webp)

## Hranice autonómie

Napriek svojej autonómii v rámci úlohy nie je Agentic RAG analogický s umelou všeobecnou inteligenciou. Jeho „agentné“ schopnosti sú obmedzené na nástroje, zdroje dát a pravidlá poskytnuté ľudskými vývojármi. Nemôže si vymýšľať vlastné nástroje ani vystúpiť mimo hraníc domény, ktoré boli stanovené. Skôr vyniká v dynamickej orchestrácii dostupných zdrojov.
Kľúčové rozdiely oproti pokročilejším formám AI zahŕňajú:

1. **Doménovo špecifická autonómia:** Agentné systémy RAG sa zameriavajú na dosiahnutie používateľom definovaných cieľov v známej doméne, používajúc stratégie ako prepísanie dopytov alebo výber nástrojov na zlepšenie výsledkov.
2. **Závislosť na infraštruktúre:** Schopnosti systému závisia na nástrojoch a dátach integrovaných vývojármi. Bez ľudského zásahu nemôže tieto hranice prekročiť.
3. **Rešpektovanie bezpečnostných opatrení:** Etické smernice, pravidlá súladu a obchodné politiky zostávajú veľmi dôležité. Sloboda agenta je vždy obmedzená bezpečnostnými opatreniami a mechanizmami dohľadu (dúfajme?).

## Praktické prípady použitia a hodnota

Agentic RAG vyniká v scenároch vyžadujúcich iteratívne zdokonaľovanie a presnosť:

1. **Prostredia orientované na správnosť:** V kontrolách súladu, regulačnej analýze alebo právnom výskume môže agentný model opakovane overovať fakty, konzultovať viacero zdrojov a prepísať dopyty, kým nevyprodukuje dôkladne overenú odpoveď.
2. **Zložité interakcie s databázami:** Pri práci so štruktúrovanými dátami, kde dopyty často zlyhávajú alebo je potrebné ich upraviť, môže systém autonómne zdokonaľovať svoje dopyty pomocou Azure SQL alebo Microsoft Fabric OneLake, zabezpečujúc, že konečné získavanie údajov je v súlade s úmyslom používateľa.
3. **Rozšírené pracovné toky:** Dlhšie prebiehajúce relácie sa môžu vyvíjať, keď sa objavujú nové informácie. Agentic RAG môže neustále začleňovať nové dáta a meniť stratégie, ako sa dozvedá viac o problematike.

## Riadenie, transparentnosť a dôvera

Ako sa tieto systémy stávajú autonómnejšími vo svojom uvažovaní, riadenie a transparentnosť sú rozhodujúce:

- **Vysvetliteľné uvažovanie:** Model môže poskytnúť auditný záznam dopytov, ktoré vykonal, zdrojov, ktoré konzultoval, a krokov uvažovania, ktoré podnikol na dosiahnutie záveru. Nástroje ako Azure AI Content Safety a Azure AI Tracing / GenAIOps môžu pomôcť udržiavať transparentnosť a zmierňovať riziká.
- **Kontrola zaujatosti a vyvážené získavanie:** Vývojári môžu ladíť stratégie získavania, aby zaistili, že sa berú do úvahy vyvážené, reprezentatívne zdroje dát, a pravidelne auditovať výstupy na odhalenie zaujatosti alebo skreslených vzorov pomocou vlastných modelov pre pokročilé dátové vedecké organizácie využívajúce Azure Machine Learning.
- **Ľudský dohľad a súlad:** Pri citlivých úlohách zostáva ľudský prehliadnutie nevyhnutné. Agentic RAG nenahrádza ľudské rozhodovanie v rozhodnutiach s vysokým rizikom — rozširuje ho tým, že poskytuje dôkladnejšie overené možnosti.

Mať nástroje, ktoré poskytujú jasný záznam o akciách, je nevyhnutné. Bez nich môže byť ladenie viackrokového procesu veľmi náročné. Pozrite si nasledujúci príklad od Literal AI (spoločnosť za Chainlit) pre spustenie Agenta:

![AgentRunExample](../../../translated_images/sk/AgentRunExample.471a94bc40cbdc0c.webp)

## Záver

Agentic RAG predstavuje prirodzenú evolúciu v tom, ako AI systémy zvládajú zložité, dátami náročné úlohy. Adopciou cyklického interakčného vzoru, autonómnym výberom nástrojov a zdokonaľovaním dopytov až k dosiahnutiu výsledku vysokej kvality sa systém posúva za hranice statického sledovania promptov k adaptívnejšiemu, kontextovo vedomému rozhodovateľovi. Aj keď je stále viazaný infraštruktúrami a etickými smernicami definovanými ľuďmi, tieto agentné schopnosti umožňujú bohatšie, dynamickejšie a nakoniec užitočnejšie AI interakcie pre firmy aj koncových používateľov.

### Máte ďalšie otázky o Agentic RAG?

Pridajte sa k [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), aby ste sa stretli s ostatnými študentmi, zúčastnili sa kancelárskych hodín a získali odpovede na svoje otázky o AI Agentoch.

## Ďalšie zdroje

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">Implementácia Retrieval Augmented Generation (RAG) s Azure OpenAI Service: Naučte sa, ako používať vlastné dáta s Azure OpenAI Service. Tento Microsoft Learn modul poskytuje komplexného sprievodcu implementáciou RAG</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Hodnotenie generatívnych AI aplikácií s Microsoft Foundry: Tento článok sa zaoberá hodnotením a porovnaním modelov na verejne dostupných datasetoch, vrátane Agentic AI aplikácií a RAG architektúr</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Čo je Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Kompletný sprievodca agentovo založenou Retrieval Augmented Generation – Novinky z generácie RAG</a>

- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: zrýchlite svoj RAG pomocou reformulácie dopytu a samodopytovania! Hugging Face Open-Source AI Cookbook</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Pridanie agentických vrstiev k RAG</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Budúcnosť znalostných asistentov: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Ako vybudovať agentické RAG systémy</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Použitie Microsoft Foundry Agent Service na škálovanie vašich AI agentov</a>

### Akademické články

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Iteratívne zdokonaľovanie s vlastnou spätnou väzbou</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Jazykové agenti s verbálnym posilňovacím učením</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Veľké jazykové modely sa môžu samy opravovať pomocou nástrojovej interaktívnej kritiky</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation: Prehľad o agentickom RAG</a>

## Predchádzajúca lekcia

[Návrhový vzor použitia nástroja](../04-tool-use/README.md)

## Nasledujúca lekcia

[Budovanie dôveryhodných AI agentov](../06-building-trustworthy-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->