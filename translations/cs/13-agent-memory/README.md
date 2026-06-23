# Paměť pro AI agenty  
[![Agent Memory](../../../translated_images/cs/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Při diskusi o unikátních výhodách vytváření AI agentů se většinou probírají dvě věci: schopnost volat nástroje k dokončení úkolů a schopnost se v průběhu času zlepšovat. Paměť je základem pro vytvoření samo-zlepšujícího se agenta, který dokáže vytvářet lepší zážitky pro naše uživatele.

V této lekci se podíváme na to, co je paměť pro AI agenty a jak ji můžeme spravovat a využívat ku prospěchu našich aplikací.

## Úvod

Tato lekce pokryje:

• **Porozumění paměti AI agentů**: Co je paměť a proč je pro agenty zásadní.

• **Implementace a ukládání paměti**: Praktické metody, jak přidat paměťové schopnosti vašim AI agentům, se zaměřením na krátkodobou a dlouhodobou paměť.

• **Způsob, jak umožnit AI agentům samo-zlepšování**: Jak paměť umožňuje agentům učit se z minulých interakcí a postupně se zlepšovat.

## Disponibilní implementace

Tato lekce obsahuje dva komplexní postupy v noteboocích:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementuje paměť pomocí Mem0 a Azure AI Search s Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementuje strukturovanou paměť pomocí Cognee, automaticky buduje znalostní graf podporovaný embeddingy, zobrazuje graf a inteligentní vyhledávání

## Cíle učení

Po dokončení této lekce budete umět:

• **Rozlišovat mezi různými typy paměti AI agentů**, včetně pracovní, krátkodobé a dlouhodobé paměti, stejně jako specializované formy jako osobnostní a epizodická paměť.

• **Implementovat a spravovat krátkodobou a dlouhodobou paměť pro AI agenty** pomocí Microsoft Agent Framework, využívajíc nástroje jako Mem0, Cognee, Whiteboard memory a integraci s Azure AI Search.

• **Porozumět principům za samo-zlepšujícími se AI agenty** a jak robustní systémy správy paměti přispívají k nepřetržitému učení a adaptaci.

## Porozumění paměti AI agentů

V jádru, **paměť pro AI agenty označuje mechanismy, které jim umožňují uchovávat a připomínat si informace**. Tyto informace mohou být konkrétní detaily o konverzaci, uživatelské preference, minulé činnosti nebo dokonce naučené vzory.

Bez paměti jsou AI aplikace často bezstavové, což znamená, že každá interakce začíná od začátku. To vede k opakujícímu se a frustrujícímu uživatelskému zážitku, kde agent „zapomíná“ předchozí kontext nebo preference.

### Proč je paměť důležitá?

Inteligence agenta je hluboce spojená s jeho schopností připomínat si a využívat minulé informace. Paměť umožňuje agentům být:

• **Reflexivní**: Učit se z minulých činností a výsledků.

• **Interaktivní**: Udržovat kontext během probíhající konverzace.

• **Proaktivní a reaktivní**: Předvídat potřeby nebo odpovídat adekvátně na základě historických dat.

• **Autonomní**: Fungovat samostatněji díky čerpání ze uložených znalostí.

Cílem implementace paměti je učinit agenty více **spolehlivými a schopnými**.

### Typy paměti

#### Pracovní paměť

Představte si to jako kousek papíru, který agent používá během jednoho pokračujícího úkolu nebo myšlenkového procesu. Drží okamžité informace potřebné k výpočtu dalšího kroku.

Pro AI agenty pracovní paměť často zachycuje nejrelevantnější informace z konverzace, i když je celé chatové historii dlouhé nebo zkrácené. Soustředí se na extrakci klíčových prvků jako požadavky, návrhy, rozhodnutí a činnosti.

**Příklad pracovní paměti**

U cestovního agenta by pracovní paměť mohla zaznamenat aktuální požadavek uživatele, například „Chci si zarezervovat cestu do Paříže“. Tento specifický požadavek je držen v bezprostředním kontextu agenta, aby vedl aktuální interakci.

#### Krátkodobá paměť

Tento typ paměti uchovává informace po dobu jedné konverzace nebo relace. Je to kontext aktuálního chatu, umožňující agentovi odkazovat na předchozí výměny v dialogu.

V ukázkách Python SDK [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) to odpovídá `AgentSession`, která je vytvořena pomocí `agent.create_session()`. Relace je vestavěnou krátkodobou pamětí rámce: uchovává kontext konverzace dostupný, dokud je taže relace znovu použita, ale tento kontext není uložen, když relace končí nebo se aplikace restartuje. Použijte dlouhodobou paměť pro fakta a preference, které musí přežít mezi relacemi, obvykle přes databázi, vektorový index nebo jiné trvalé úložiště.

**Příklad krátkodobé paměti**

Pokud uživatel zeptá „Kolik by stál let do Paříže?“ a poté pokračuje „A co ubytování tam?“, krátkodobá paměť zajistí, že agent ví, že „tam“ znamená „Paříž“ v rámci téže konverzace.

#### Dlouhodobá paměť

Toto jsou informace, které přetrvávají přes více konverzací nebo relací. Umožňuje agentům pamatovat si uživatelské preference, historické interakce nebo obecné znalosti po delší dobu. Je to důležité pro personalizaci.

**Příklad dlouhodobé paměti**

Dlouhodobá paměť může uchovávat třeba, že „Ben rád lyžuje a má rád venkovní aktivity, pije kávu s výhledem na hory a chce se vyhnout obtížným sjezdovkám kvůli předchozímu zranění“. Tyto informace získané z minulých interakcí ovlivňují doporučení v budoucích cestovních plánovacích sezeních, což je dělá velmi osobními.

#### Osobnostní paměť

Tento specializovaný typ paměti pomáhá agentovi vyvinout konzistentní „osobnost“ nebo „persona“. Umožňuje agentovi pamatovat si detaily o sobě nebo své zamýšlené roli, což činí interakce plynulejšími a zaměřenějšími.

**Příklad osobnostní paměti**  
Pokud je cestovní agent navržen jako „expert na plánování lyžování“, osobnostní paměť může posilovat tuto roli a ovlivňovat jeho odpovědi tak, aby odpovídaly tónu a znalostem experta.

#### Pracovní/Epizodická paměť

Tato paměť ukládá sekvenci kroků, které agent podnikne během složitého úkolu, včetně úspěchů a neúspěchů. Je to jako pamatovat si konkrétní „epizody“ nebo minulé zkušenosti, aby se z nich agent mohl poučit.

**Příklad epizodické paměti**

Pokud se agent pokusil zarezervovat konkrétní let, ale selhalo to kvůli nedostupnosti, epizodická paměť by tuto chybu zaznamenala, což umožní agentovi při následujícím pokusu nabídnout alternativní lety nebo informovat uživatele o problému informovanějším způsobem.

#### Paměť entit

Týká se extrakce a zapamatování konkrétních entit (jako lidé, místa nebo věci) a událostí z konverzací. Umožňuje agentovi vybudovat strukturované pochopení klíčových diskutovaných prvků.

**Příklad paměti entit**

Z konverzace o minulé cestě může agent extrahovat entity jako „Paříž“, „Eiffelova věž“ a „večeře v restauraci Le Chat Noir“. Při budoucí interakci si agent může vzpomenout na „Le Chat Noir“ a nabídnout novou rezervaci právě tam.

#### Strukturované RAG (Retrieval Augmented Generation)

Zatímco RAG je rozsáhlejší technika, „Strukturované RAG“ je zdůrazňováno jako mocná paměťová technologie. Extrahuje husté, strukturované informace z různých zdrojů (konverzace, e-maily, obrázky) a využívá je k vylepšení přesnosti, vyhledatelnosti a rychlosti odpovědí. Na rozdíl od klasického RAG, který spoléhá pouze na sémantickou podobnost, Strukturované RAG pracuje s inherentní strukturou informací.

**Příklad strukturovaného RAG**

Místo pouhého shody klíčových slov by Strukturované RAG mohlo analyzovat detaily letu (cílové místo, datum, čas, letecká společnost) z e-mailu a uložit je strukturovaně. To umožňuje přesné dotazy jako „Jaký let jsem si zarezervoval do Paříže v úterý?“

## Implementace a ukládání paměti

Implementace paměti pro AI agenty zahrnuje systematický proces **správy paměti**, který zahrnuje generování, ukládání, vybavování, integraci, aktualizaci a dokonce i „zapomínání“ (nebo mazání) informací. Vybavení (retrieval) je obzvlášť klíčový aspekt.

### Specializované paměťové nástroje

#### Mem0

Jedním ze způsobů, jak ukládat a spravovat paměť agenta, je použití specializovaných nástrojů jako Mem0. Mem0 funguje jako perzistentní paměťová vrstva, která agentům umožňuje vybavovat si relevantní interakce, ukládat uživatelské preference a faktický kontext a učit se z úspěchů i selhání v průběhu času. Myšlenka je, že bezstavoví agenti se stanou stavovými.

Funguje prostřednictvím **dvoufázového paměťového procesu: extrakce a aktualizace**. Nejprve se zprávy přidané do vlákna agenta posílají do služby Mem0, která využívá Velký jazykový model (LLM) k shrnutí historie konverzace a extrakci nových pamětí. Následně fáze řízená LLM určuje, zda přidat, upravit nebo smazat tyto paměti, které jsou uloženy v hybridním úložišti dat, zahrnujícím vektory, grafy a klíč-hodnotové databáze. Tento systém zároveň podporuje různé typy paměti a může začlenit grafovou paměť pro správu vztahů mezi entitami.

#### Cognee

Dalším silným přístupem je použití **Cognee**, open-source sémantické paměti pro AI agenty, která transformuje strukturovaná i nestrukturovaná data do dotazovatelných znalostních grafů podporovaných embeddingy. Cognee poskytuje **duální úložištní architekturu**, která kombinuje vyhledávání podle vektorové podobnosti s grafovými vztahy a umožňuje agentům chápat nejen jaké informace jsou si podobné, ale i jak jsou pojmy navzájem propojené.

Vyniká v **hybridním vybavování**, které kombinuje vektorovou podobnost, grafovou strukturu a LLM dedukci – od prostého vyhledávání částí až po odpovídání na otázky s vědomím grafu. Systém udržuje **živou paměť**, která se vyvíjí a roste při zachování možnosti dotazování jako jednoho propojeného grafu, podporující jak krátkodobý kontext relace, tak dlouhodobou perzistentní paměť.

Tutoriál v notebooku Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstruje vytváření této sjednocené paměťové vrstvy, s praktickými příklady importu různorodých zdrojů dat, vizualizace znalostního grafu a dotazování s různými vyhledávacími strategiemi přizpůsobenými specifickým potřebám agenta.

### Ukládání paměti pomocí RAG

Kromě specializovaných paměťových nástrojů jako Mem0 můžete využít robustní vyhledávací služby jako **Azure AI Search jako backend pro ukládání a vybavování pamětí**, zejména pro strukturované RAG.

To vám umožní zakotvit odpovědi agenta ve vlastních datech a zajistit tak relevantnější a přesnější odpovědi. Azure AI Search lze použít k ukládání uživatelsky specifických cestovních vzpomínek, katalogů produktů nebo jakýchkoli jiných doménově specifických znalostí.

Azure AI Search podporuje schopnosti jako **Strukturované RAG**, které vynikají v extrakci a vybavování hustých, strukturovaných informací z rozsáhlých souborů dat jako jsou historie konverzací, e-maily nebo dokonce obrázky. To poskytuje „nadlidskou přesnost a vybavitelnost“ v porovnání s tradičními přístupy založenými na dělení textu nebo vkládáních (embeddingu).

## Jak učinit AI agenty samo-zlepšujícími se

Běžný vzor pro samo-zlepšující se agenty zahrnuje zavedení **„znalostního agenta“**. Tento samostatný agent pozoruje hlavní konverzaci mezi uživatelem a primárním agentem. Jeho rolí je:

1. **Identifikovat cenné informace**: Určit, zda je část konverzace vhodná k uložení jako obecné znalosti nebo specifické uživatelské preference.

2. **Extrahovat a shrnout**: Destilovat podstatné znalosti nebo preference z konverzace.

3. **Uložit do znalostní báze**: Trvale uložit extrahované informace, často ve vektorové databázi, aby byly později dostupné.

4. **Rozšířit budoucí dotazy**: Když uživatel zahájí nový dotaz, znalostní agent vyhledá relevantní uložené informace a připojí je k uživatelskému podnětu, poskytujíc tak primárnímu agentovi klíčový kontext (podobně jako RAG).

### Optimalizace paměti

• **Řízení latence**: Aby nedošlo ke zpomalení uživatelských interakcí, může být použito levnější a rychlejší model pro rychlou kontrolu, zda je informace vhodná k uložení nebo vybavení, a složitější proces extrakce/vybavení se spustí jen podle potřeby.

• **Údržba znalostní báze**: Pro rostoucí znalostní bázi lze méně často používané informace přesunout do „studeného úložiště“ k řízení nákladů.

## Máte další otázky o paměti agentů?

Připojte se k [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), kde se setkáte s dalšími studenty, můžete navštěvovat otevřené hodiny a získat odpovědi na vaše otázky týkající se AI agentů.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->