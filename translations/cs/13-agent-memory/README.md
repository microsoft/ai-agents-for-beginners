# Paměť pro AI agenty 
[![Paměť agenta](../../../translated_images/cs/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Když se diskutuje o jedinečných výhodách vytváření AI agentů, mluví se hlavně o dvou věcech: schopnosti volat nástroje k dokončení úkolů a schopnosti se v průběhu času zlepšovat. Paměť je základem vytváření samoučících se agentů, kteří mohou vytvářet lepší zážitky pro naše uživatele.

V této lekci se podíváme na to, co je paměť pro AI agenty a jak ji můžeme spravovat a využívat ve prospěch našich aplikací.

## Introduction

Tato lekce pokryje:

• **Porozumění paměti AI agentů**: Co je paměť a proč je pro agenty zásadní.

• **Implementace a ukládání paměti**: Praktické metody přidání schopností paměti vašim AI agentům, se zaměřením na krátkodobou a dlouhodobou paměť.

• **Jak udělat AI agenty samovylepšujícími se**: Jak paměť umožňuje agentům učit se z minulých interakcí a zlepšovat se v průběhu času.

## Available Implementations

Tato lekce obsahuje dva komplexní notebook tutoriály:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementuje paměť pomocí Mem0 a Azure AI Search s Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementuje strukturovanou paměť pomocí Cognee, automaticky buduje znalostní graf založený na embedincích, vizualizuje graf a inteligentní vyhledávání

## Learning Goals

Po dokončení této lekce budete umět:

• **Rozlišit různé typy paměti AI agentů**, včetně pracovní, krátkodobé a dlouhodobé paměti, stejně jako specializované formy jako persona a epizodická paměť.

• **Implementovat a spravovat krátkodobou a dlouhodobou paměť pro AI agenty** pomocí Microsoft Agent Framework, využívajíc nástroje jako Mem0, Cognee, Whiteboard memory a integraci s Azure AI Search.

• **Pochopit principy stojící za samovylepšujícími se AI agenty** a jak robustní systémy správy paměti přispívají k průběžnému učení a adaptaci.

## Understanding AI Agent Memory

V jádru **paměť pro AI agenty odkazuje na mechanismy, které jim umožňují uchovávat a vybavovat si informace**. Tyto informace mohou být konkrétní detaily o konverzaci, uživatelské preference, minulá jednání nebo dokonce naučené vzory.

Bez paměti jsou AI aplikace často bezstavové, což znamená, že každá interakce začíná od začátku. To vede k opakujícímu se a frustrujícímu uživatelskému zážitku, kde agent „zapomíná“ předchozí kontext nebo preference.

### Why is Memory Important?

chytrý výkon agenta je hluboce spojen s jeho schopností si vybavovat a využívat minulé informace. Paměť umožňuje agentům být:

• **Reflexivní**: Učit se z minulých akcí a výsledků.

• **Interaktivní**: Udržovat kontext během probíhající konverzace.

• **Proaktivní a reaktivní**: Předvídat potřeby nebo odpovídat vhodně na základě historických dat.

• **Autonomní**: Fungovat více nezávisle čerpáním ze uložených znalostí.

Cílem implementace paměti je učinit agenty více **spolehlivými a schopnými**.

### Types of Memory

#### Working Memory

Představte si to jako papír na poznámky, který agent používá během jediného, probíhajícího úkolu nebo myšlenkového procesu. Obsahuje okamžité informace potřebné k výpočtu dalšího kroku.

U AI agentů pracovní paměť často zachycuje nejrelevantnější informace z konverzace, i když je celé chatové zázemí dlouhé nebo zkrácené. Soustředí se na extrakci klíčových prvků jako požadavky, návrhy, rozhodnutí a akce.

**Working Memory Example**

U agenta pro rezervaci cest by pracovní paměť mohla zachytit aktuální požadavek uživatele, například „chci si zarezervovat cestu do Paříže“. Tento konkrétní požadavek je držen v bezprostředním kontextu agenta, aby řídit aktuální interakci.

#### Short Term Memory

Tento typ paměti uchovává informace po dobu jedné konverzace nebo relace. Je to kontext aktuálního chatu, který umožňuje agentovi odkazovat na předchozí výměny v dialogu.

**Short Term Memory Example**

Pokud se uživatel zeptá: „Kolik by stál let do Paříže?“ a poté naváže: „A co ubytování tam?“, krátkodobá paměť zajistí, že agent ví, že „tam“ odkazuje na „Paříž“ v rámci téže konverzace.

#### Long Term Memory

To jsou informace, které přetrvávají přes více konverzací nebo relací. Umožňují agentům pamatovat si uživatelské preference, historické interakce nebo obecné znalosti po delší dobu. To je důležité pro personalizaci.

**Long Term Memory Example**

Dlouhodobá paměť by mohla uložit, že „Ben rád jezdí na lyžích a má rád venkovní aktivity, má rád kávu s výhledem na hory a chce se vyhnout pokročilým sjezdovkám kvůli minulému zranění“. Tyto informace, získané z předchozích interakcí, ovlivní doporučení při budoucím plánování cestování a udělají je vysoce personalizovanými.

#### Persona Memory

Tento specializovaný typ paměti pomáhá agentovi vyvinout konzistentní „osobnost“ nebo „personu“. Umožňuje agentovi pamatovat si detaily o sobě nebo o zamýšlené roli, čímž jsou interakce plynulejší a cílenější.

**Persona Memory Example**
Pokud je cestovní agent navržen tak, aby byl „expert na plánování lyžařských zájezdů“, persona paměť by mohla posílit tuto roli a ovlivnit jeho odpovědi tak, aby ladily s tónem a znalostmi experta.

#### Workflow/Episodic Memory

Tato paměť ukládá sekvenci kroků, které agent provádí během složitého úkolu, včetně úspěchů a neúspěchů. Je to jako zapamatování si konkrétních „epizod“ nebo minulých zkušeností, aby se z nich mohl agent poučit.

**Episodic Memory Example**

Pokud se agent pokusil rezervovat konkrétní let, ale selhalo to kvůli nedostupnosti, epizodická paměť by mohla zaznamenat tento neúspěch, což agentovi umožní vyzkoušet alternativní lety nebo informovat uživatele o problému informovaněji při dalším pokusu.

#### Entity Memory

To zahrnuje extrakci a zapamatování konkrétních entit (jako lidé, místa nebo věci) a událostí z konverzací. Umožňuje agentovi vybudovat strukturované porozumění klíčovým prvkům, o kterých se diskutovalo.

**Entity Memory Example**

Z konverzace o minulé cestě může agent extrahovat „Paříž“, „Eiffelovu věž“ a „večeře v restauraci Le Chat Noir“ jako entity. Při budoucí interakci by si agent mohl vybavit „Le Chat Noir“ a nabídnout nové zarezervování tam.

#### Structured RAG (Retrieval Augmented Generation)

I když je RAG širší technikou, „Strukturované RAG“ je vyzdviženo jako silná paměťová technologie. Extrahuje husté, strukturované informace z různých zdrojů (konverzace, e-maily, obrázky) a používá je ke zvýšení přesnosti, vyhledatelnosti a rychlosti odpovědí. Na rozdíl od klasického RAG, který spoléhá výhradně na sémantickou podobnost, Structured RAG pracuje s inherentní strukturou informací.

**Structured RAG Example**

Místo prostého párování klíčových slov může Structured RAG analyzovat detaily letu (destinace, datum, čas, letecká společnost) z e-mailu a uložit je strukturovaným způsobem. To umožňuje přesné dotazy jako „Jakým letem jsem letěl do Paříže v úterý?“

## Implementing and Storing Memory

Implementace paměti pro AI agenty zahrnuje systematický proces **správy paměti**, který zahrnuje generování, ukládání, vyhledávání, integraci, aktualizaci a dokonce „zapomínání“ (nebo mazání) informací. Vyhledávání je obzvláště klíčový aspekt.

### Specialized Memory Tools

#### Mem0

Jeden způsob, jak ukládat a spravovat paměť agentů, je použití specializovaných nástrojů jako Mem0. Mem0 funguje jako perzistentní vrstva paměti, která umožňuje agentům vybavit si relevantní interakce, ukládat uživatelské preference a faktický kontext a učit se z úspěchů a neúspěchů v průběhu času. Myšlenka je taková, že bezstavní agenti se proměňují v stavové.

Funguje prostřednictvím **dvoufázového pipeline paměti: extrakce a aktualizace**. Nejprve jsou zprávy přidané do vlákna agenta odeslány do služby Mem0, která používá velký jazykový model (LLM) k shrnutí historie konverzace a extrakci nových vzpomínek. Následně fáze aktualizace řízená LLM určí, zda přidat, upravit nebo smazat tyto vzpomínky a uloží je do hybridního úložiště, které může zahrnovat vektorové, grafové a key-value databáze. Tento systém také podporuje různé typy paměti a může začlenit grafovou paměť pro správu vztahů mezi entitami.

#### Cognee

Dalším silným přístupem je použití **Cognee**, open-source sémantické paměti pro AI agenty, která transformuje strukturovaná i nestrukturovaná data do dotazovatelného znalostního grafu podloženého embedincemi. Cognee poskytuje **architekturu s dvojím úložištěm**, kombinující vyhledávání podle vektorové podobnosti s grafovými vztahy, což umožňuje agentům rozumět nejen tomu, jaké informace jsou podobné, ale jak spolu pojmy souvisejí.

Vyniká ve **hybridním vyhledávání**, které mísí vektorovou podobnost, grafovou strukturu a LLM uvažování - od surového vyhledávání chunků až po dotazování s ohledem na graf. Systém udržuje **živou paměť**, která se vyvíjí a roste, přičemž zůstává dotazovatelná jako jeden propojený graf, podporující jak krátkodobý kontext relace, tak dlouhodobou perzistentní paměť.

Tutoriál v notebooku Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstruje budování této sjednocené vrstvy paměti s praktickými příklady importu různorodých datových zdrojů, vizualizace znalostního grafu a dotazování s různými vyhledávacími strategiemi přizpůsobenými potřebám konkrétních agentů.

### Storing Memory with RAG

Kromě specializovaných nástrojů paměti jako mem0 , můžete využít robustní vyhledávací služby jako **Azure AI Search jako backend pro ukládání a získávání vzpomínek**, zejména pro strukturované RAG.

To vám umožní zakotvit odpovědi agenta ve vašich datech, zajišťující relevantnější a přesnější odpovědi. Azure AI Search může být použita k ukládání uživatelsky specifických cestovních vzpomínek, katalogů produktů nebo jakýchkoli jiných doménově specifických znalostí.

Azure AI Search podporuje schopnosti jako **Structured RAG**, která vyniká v extrakci a získávání hustých, strukturovaných informací z velkých datových sad, jako jsou historie konverzací, e-maily nebo dokonce obrázky. To poskytuje „nadlidskou přesnost a vyhledatelnost“ ve srovnání s tradičními přístupy založenými na dělení textu na části a embeddingech.

## Making AI Agents Self-Improve

Běžný vzor pro samovylepšující se agenty zahrnuje zavedení **„znalostního agenta“**. Tento samostatný agent pozoruje hlavní konverzaci mezi uživatelem a primárním agentem. Jeho role je:

1. **Identifikovat cenné informace**: Určit, zda je část konverzace hodna uložení jako obecná znalost nebo konkrétní uživatelská preference.

2. **Extrahovat a shrnout**: Destilovat podstatné učení nebo preferenci z konverzace.

3. **Uložit do znalostní báze**: Perzistovat tyto extrahované informace, často ve vektorové databázi, aby je bylo možné později vyhledat.

4. **Obohatit budoucí dotazy**: Když uživatel zahájí nový dotaz, znalostní agent vyhledá relevantní uložené informace a připojí je k uživatelovu promptu, poskytujíc zásadní kontext primárnímu agentovi (podobně jako RAG).

### Optimizations for Memory

• **Řízení latence**: Aby se předešlo zpomalení uživatelských interakcí, může být zpočátku použit levnější, rychlejší model ke krátké kontrole, zda je informace vhodná k uložení nebo vyhledání, a složitější extrakční/vyhledávací proces se spustí jen pokud je to nutné.

• **Údržba znalostní báze**: Pro rostoucí znalostní bázi lze méně často používané informace přesunout do „studeného úložiště“ za účelem správy nákladů.

## Got More Questions About Agent Memory?

Join the [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) to meet with other learners, attend office hours and get your AI Agents questions answered.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Prohlášení o vyloučení odpovědnosti:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v originálním znění by měl být považován za závazný. Pro kritické informace doporučujeme využít profesionální lidský překlad. Za jakékoli nedorozumění nebo chybné interpretace vzniklé v důsledku použití tohoto překladu neneseme odpovědnost.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->