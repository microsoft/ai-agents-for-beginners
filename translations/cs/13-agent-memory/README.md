# Paměť pro AI agenty 
[![Agent Memory](../../../translated_images/cs/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Když se mluví o jedinečných výhodách vytváření AI agentů, hlavně se zmiňují dvě věci: schopnost využívat nástroje k plnění úkolů a schopnost zlepšovat se v průběhu času. Paměť je základem pro vytvoření sebezdokonalujícího se agenta, který může vytvářet lepší zážitky pro naše uživatele.

V této lekci se podíváme, co je paměť pro AI agenty a jak ji můžeme spravovat a využívat ve prospěch našich aplikací.

## Úvod

Tato lekce pokryje:

• **Pochopení paměti AI agentů**: Co je paměť a proč je pro agenty důležitá.

• **Implementace a ukládání paměti**: Praktické metody, jak přidat paměťové schopnosti vašim AI agentům, se zaměřením na krátkodobou a dlouhodobou paměť.

• **Jak učinit AI agenty sebezdokonalujícími se**: Jak paměť umožňuje agentům učit se z minulých interakcí a zlepšovat se v průběhu času.

## Dostupné implementace

Tato lekce obsahuje dva komplexní tutoriály v noteboocích:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementuje paměť pomocí Mem0 a Azure AI Search s Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementuje strukturovanou paměť pomocí Cognee, automaticky buduje znalostní graf podporovaný embeddingy, vizualizuje graf a inteligentní vyhledávání

## Výukové cíle

Po dokončení této lekce budete umět:

• **Rozlišovat mezi různými typy paměti AI agentů**, včetně pracovní, krátkodobé a dlouhodobé paměti, stejně jako specializovaných forem jako je persona a epizodická paměť.

• **Implementovat a spravovat krátkodobou a dlouhodobou paměť AI agentů** pomocí Microsoft Agent Framework, využívajíc nástroje jako Mem0, Cognee, Whiteboard memory a integrující se s Azure AI Search.

• **Pochopit principy za sebezdokonalujícími se AI agenty** a jak robustní systémy správy paměti přispívají k nepřetržitému učení a adaptaci.

## Pochopení paměti AI agentů

V jádru **paměť AI agentů znamená mechanismy, které jim umožňují uchovávat a vybavovat informace**. Tyto informace mohou být konkrétní detaily o konverzaci, uživatelské preference, minulé akce nebo dokonce naučené vzory.

Bez paměti jsou AI aplikace často bezstavové, což znamená, že každá interakce začíná od začátku. To vede k opakujícím se a frustrujícím uživatelským zážitkům, kde agent "zapomíná" předchozí kontext nebo preference.

### Proč je paměť důležitá?

inteligence agenta je hluboce spjata s jeho schopností vybavovat a využívat minulé informace. Paměť umožňuje agentům být:

• **Reflexivní**: Učit se z minulých akcí a výsledků.

• **Interaktivní**: Udržovat kontext během probíhající konverzace.

• **Proaktivní a Reaktivní**: Předvídat potřeby nebo adekvátně reagovat na základě historických dat.

• **Autonomní**: Fungovat samostatněji čerpáním ze uložených znalostí.

Cílem implementace paměti je učinit agenty **spolehlivějšími a schopnějšími**.

### Typy paměti

#### Pracovní paměť

Představte si to jako kus papíru, který agent používá během jednoho probíhajícího úkolu nebo myšlenkového procesu. Uchovává okamžité informace potřebné k výpočtu dalšího kroku.

Pro AI agenty často pracovní paměť zachycuje nejrelevantnější informace z konverzace, i když je celá historie chatu dlouhá nebo zkrácená. Soustředí se na získání klíčových prvků jako požadavky, návrhy, rozhodnutí a akce.

**Příklad pracovní paměti**

U rezervačního agenta pro cestování by pracovní paměť mohla zachytit aktuální požadavek uživatele, například "Chci zarezervovat výlet do Paříže". Tento konkrétní požadavek je držen v bezprostředním kontextu agenta, aby usměrňoval aktuální interakci.

#### Krátkodobá paměť

Tento typ paměti uchovává informace po dobu trvání jedné konverzace nebo sezení. Je to kontext aktuálního rozhovoru, který agentovi umožňuje odkazovat zpět na předchozí kroky dialogu.

Ve vzorcích Python SDK [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) odpovídá tomu `AgentSession`, který je vytvořen příkazem `agent.create_session()`. Sezení je v rámci frameworku zabudovaná krátkodobá paměť: udržuje dostupný kontext konverzace, dokud je stejné sezení znovu použito, ale tento kontext není uchováván při ukončení sezení nebo restartu aplikace. Pro fakta a preference, které mají přetrvávat mezi sezeními, použijte dlouhodobou paměť, obvykle pomocí databáze, vektorového indexu nebo jiného perzistentního úložiště.

**Příklad krátkodobé paměti**

Pokud uživatel položí otázku "Kolik stojí let do Paříže?" a následně "A co ubytování tam?", krátkodobá paměť zajišťuje, že agent ví, že "tam" se ve stejné konverzaci vztahuje na "Paříž".

#### Dlouhodobá paměť

Jsou to informace, které přetrvávají přes více konverzací či sezení. Umožňuje agentům pamatovat si uživatelské preference, historické interakce nebo obecné znalosti po delší období. To je důležité pro personalizaci.

**Příklad dlouhodobé paměti**

Dlouhodobá paměť by mohla uložit, že "Ben má rád lyžování a venkovní aktivity, preferuje kávu s výhledem na hory a chce se vyhnout pokročilým lyžařským tratím kvůli starému zranění". Tyto informace, naučené z předchozích interakcí, ovlivňují doporučení při budoucím plánování cest, díky čemuž jsou velmi personalizovaná.

#### Persona paměť

Tento specializovaný typ paměti pomáhá agentovi vyvinout konzistentní "osobnost" nebo "personu". Umožňuje agentovi pamatovat si detaily o sobě nebo o své zamýšlené roli, což činí interakce plynulejšími a cílenějšími.

**Příklad persona paměti**
Pokud je cestovní agent navržen jako "expert na plánování lyžování", persona paměť může posílit tuto roli a ovlivnit jeho odpovědi tak, aby odpovídaly tónu a znalostem experta.

#### Workflow/Epizodická paměť

Tato paměť ukládá posloupnost kroků, které agent podnikne během složitého úkolu, včetně úspěchů a neúspěchů. Je to jako vzpomínání na specifické "epizody" nebo minulé zkušenosti, ze kterých se agent může poučit.

**Příklad epizodické paměti**

Pokud se agent pokusil zarezervovat konkrétní let, ale neuspěl kvůli nedostupnosti, epizodická paměť může tuto neúspěšnost zaznamenat, což agentovi umožní zkusit alternativní lety nebo informovat uživatele o problému při další snaze.

#### Entitní paměť

Zahrnuje extrahování a zapamatování specifických entit (jako lidé, místa nebo věci) a událostí z konverzací. Umožňuje agentovi vybudovat strukturované pochopení klíčových prvků diskutovaných témat.

**Příklad entitní paměti**

Z konverzace o minulé cestě může agent extrahovat "Paříž", "Eiffelova věž" a "večeře v restauraci Le Chat Noir" jako entity. Při budoucí interakci by agent mohl vzpomenout na "Le Chat Noir" a nabídnout novou rezervaci.

#### Strukturovaný RAG (Retrieval Augmented Generation)

Zatímco RAG je širší technika, "Strukturovaný RAG" je vyzdvihován jako výkonná paměťová technologie. Extrahuje husté, strukturované informace z různých zdrojů (konverzace, emaily, obrázky) a používá je k vylepšení přesnosti, vyhledávání a rychlosti odpovědí. Na rozdíl od klasického RAG, který spoléhá výhradně na sémantickou podobnost, Strukturovaný RAG pracuje s inherentní strukturou informací.

**Příklad Strukturovaného RAG**

Místo úzkého vyhledávání klíčových slov by Strukturovaný RAG mohl rozeznat detaily letu (cíl, datum, čas, leteckou společnost) z emailu a uložit je strukturovaně. To umožňuje přesné dotazy jako "Který let jsem rezervoval do Paříže v úterý?"

## Implementace a ukládání paměti

Implementace paměti pro AI agenty spočívá v systematickém procesu **správy paměti**, která zahrnuje generování, ukládání, vyhledávání, integraci, aktualizaci a dokonce i "zapomínání" (nebo mazání) informací. Vyhledávání je zvlášť klíčovým aspektem.

### Specializované paměťové nástroje

#### Mem0

Jedním ze způsobů, jak ukládat a spravovat paměť agenta, je použití specializovaných nástrojů jako Mem0. Mem0 funguje jako perzistentní paměťová vrstva, která agentům umožňuje vybavovat si relevantní interakce, ukládat uživatelské preference a faktický kontext a učit se z úspěchů a neúspěchů v průběhu času. Cílem je, aby stateless agenti získali stavovost.

Funguje přes **dvoufázový paměťový pipeline: extrakce a aktualizace**. Nejprve jsou zprávy přidané do vlákna agenta zaslány službě Mem0, která používá Large Language Model (LLM) k shrnutí historie konverzace a extrahování nových vzpomínek. Následná fáze řízená LLM rozhoduje, zda tyto vzpomínky přidat, změnit nebo smazat, přičemž je ukládá do hybridního datového úložiště, které může zahrnovat vektorové, grafové a klíč-hodnota databáze. Tento systém také podporuje různé typy paměti a může začlenit grafovou paměť pro správu vztahů mezi entitami.

#### Cognee

Další silný přístup je použití **Cognee**, open source sémantické paměti pro AI agenty, která převádí strukturovaná i nestrukturovaná data na dotazovatelné znalostní grafy podporované embeddingy. Cognee poskytuje **architekturu s dvojím uložištěm**, která kombinuje vyhledávání podle vektorové podobnosti s grafovými vztahy, což agentům umožňuje chápat nejen co je podobné, ale jak jsou pojmy vzájemně propojeny.

Vyniká v **hybridním vyhledávání**, které kombinuje vektorovou podobnost, strukturu grafu a reasoning pomocí LLM – od jednoduchého hledání kusů dat až po dotazy s vědomím grafu. Systém udržuje **živou paměť**, která se vyvíjí a roste, přičemž zůstává dotazovatelná jako jeden propojený graf, podporující jak krátkodobý kontext sezení, tak dlouhodobou perzistentní paměť.

Tutoriál v notebooku Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstruje budování této sjednocené paměťové vrstvy, s praktickými příklady ingestování rozmanitých datových zdrojů, vizualizace znalostního grafu a dotazování s různými strategiemi vyhledávání přizpůsobenými specifickým potřebám agentů.

### Ukládání paměti s RAG

Kromě specializovaných paměťových nástrojů jako Mem0 můžete využít robustní vyhledávací služby jako **Azure AI Search jako backend pro ukládání a vyhledávání vzpomínek**, zejména pro strukturovaný RAG.

To umožňuje, aby reakce vašeho agenta byly podpořeny vlastními daty, což zajišťuje relevantnější a přesnější odpovědi. Azure AI Search může být použit pro ukládání uživatelských cestovatelských vzpomínek, katalogů produktů nebo jakýchkoli jiných oborově specifických znalostí.

Azure AI Search podporuje vlastnosti jako **Strukturovaný RAG**, který vyniká v extrahování a vyhledávání hustých, strukturovaných informací z rozsáhlých datasetů, jako jsou historie konverzací, emaily nebo dokonce obrázky. Poskytuje tak "nadlidskou přesnost a vyhledávání" ve srovnání s tradičními přístupy rozdělení textu a embeddingů.

## Jak učinit AI agenty sebezdokonalujícími se

Běžný vzor pro sebezdokonalující se agenty zahrnuje zavedení **"vědomostního agenta"**. Tento samostatný agent sleduje hlavní konverzaci mezi uživatelem a primárním agentem. Jeho úlohou je:

1. **Identifikovat cenné informace**: Rozpoznat, zda je nějaká část konverzace hodná uložení jako obecná znalost nebo specifická uživatelská preference.

2. **Extrahovat a shrnout**: Destilovat klíčovou naučenou věc nebo preferenci z konverzace.

3. **Uložit do znalostní báze**: Trvale uložit tuto extrahovanou informaci, často do vektorové databáze, aby mohla být později vyhledána.

4. **Doplňovat budoucí dotazy**: Když uživatel zahájí nový dotaz, vědomostní agent vyhledá relevantní uložené informace a připojí je k uživatelskému promptu, poskytující tak rozhodující kontext primárnímu agentovi (podobně jako RAG).

### Optimalizace paměti

• **Správa latence**: Aby se zabránilo zpomalení uživatelských interakcí, může být na začátku použit levnější, rychlejší model k rychlé kontrole, zda je informace hodná uložení nebo vyhledávání, a složitější proces extrakce/vyhledávání se spustí jen, když je to nutné.

• **Údržba znalostní báze**: Pro rostoucí znalostní bázi mohou být méně často používané informace přesunuty do "studeného úložiště" ke snížení nákladů.

## Máte více otázek ohledně paměti agentů?

Připojte se na [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kde můžete potkat ostatní studenty, účastnit se konzultačních hodin a získat odpovědi na své otázky o AI agentech.
## Předchozí lekce

[Context Engineering for AI Agents](../12-context-engineering/README.md)

## Následující lekce

[Exploring Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->