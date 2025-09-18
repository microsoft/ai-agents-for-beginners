<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1923cf93aba522a5f4a493597112a893",
  "translation_date": "2025-09-18T16:20:32+00:00",
  "source_file": "13-agent-memory/README.md",
  "language_code": "cs"
}
-->
# Paměť pro AI agenty

Při diskusi o unikátních výhodách vytváření AI agentů se nejčastěji zmiňují dvě věci: schopnost využívat nástroje k plnění úkolů a schopnost se zlepšovat v průběhu času. Paměť je základem pro vytvoření samostatně se zlepšujícího agenta, který dokáže poskytovat lepší zážitky našim uživatelům.

V této lekci se podíváme na to, co je paměť pro AI agenty, jak ji můžeme spravovat a využívat ve prospěch našich aplikací.

## Úvod

Tato lekce pokryje:

• **Porozumění paměti AI agentů**: Co je paměť a proč je pro agenty nezbytná.

• **Implementace a ukládání paměti**: Praktické metody pro přidání paměťových schopností vašim AI agentům, se zaměřením na krátkodobou a dlouhodobou paměť.

• **Vytváření samostatně se zlepšujících AI agentů**: Jak paměť umožňuje agentům učit se z minulých interakcí a zlepšovat se v průběhu času.

## Cíle učení

Po dokončení této lekce budete vědět, jak:

• **Rozlišovat mezi různými typy paměti AI agentů**, včetně pracovní, krátkodobé a dlouhodobé paměti, stejně jako specializovaných forem, jako je paměť osobnosti a epizodická paměť.

• **Implementovat a spravovat krátkodobou a dlouhodobou paměť pro AI agenty** pomocí frameworku Semantic Kernel, využívat nástroje jako Mem0 a Whiteboard memory a integrovat je s Azure AI Search.

• **Porozumět principům samostatně se zlepšujících AI agentů** a tomu, jak robustní systémy správy paměti přispívají k neustálému učení a adaptaci.

## Porozumění paměti AI agentů

V jádru **paměť AI agentů odkazuje na mechanismy, které jim umožňují uchovávat a vybavovat si informace**. Tyto informace mohou zahrnovat konkrétní detaily o konverzaci, uživatelské preference, minulé akce nebo dokonce naučené vzory.

Bez paměti jsou AI aplikace často bezstavové, což znamená, že každá interakce začíná od nuly. To vede k opakovanému a frustrujícímu uživatelskému zážitku, kdy agent "zapomíná" předchozí kontext nebo preference.

### Proč je paměť důležitá?

Inteligence agenta je úzce spjata s jeho schopností vybavovat si a využívat minulé informace. Paměť umožňuje agentům být:

• **Reflexivní**: Učit se z minulých akcí a výsledků.

• **Interaktivní**: Udržovat kontext během probíhající konverzace.

• **Proaktivní a reaktivní**: Předvídat potřeby nebo reagovat vhodně na základě historických dat.

• **Autonomní**: Fungovat více nezávisle díky využívání uložených znalostí.

Cílem implementace paměti je učinit agenty více **spolehlivými a schopnými**.

### Typy paměti

#### Pracovní paměť

Představte si ji jako kus papíru, na který si agent zapisuje během jednoho úkolu nebo myšlenkového procesu. Uchovává okamžité informace potřebné k výpočtu dalšího kroku.

U AI agentů pracovní paměť často zachycuje nejrelevantnější informace z konverzace, i když je celá historie chatu dlouhá nebo zkrácená. Zaměřuje se na klíčové prvky, jako jsou požadavky, návrhy, rozhodnutí a akce.

**Příklad pracovní paměti**

U agenta pro rezervaci cest může pracovní paměť zachytit aktuální požadavek uživatele, například "Chci si rezervovat výlet do Paříže". Tento konkrétní požadavek je držen v bezprostředním kontextu agenta, aby vedl aktuální interakci.

#### Krátkodobá paměť

Tento typ paměti uchovává informace po dobu jedné konverzace nebo relace. Je to kontext aktuálního chatu, který umožňuje agentovi odkazovat na předchozí kroky v dialogu.

**Příklad krátkodobé paměti**

Pokud se uživatel zeptá: "Kolik by stál let do Paříže?" a poté pokračuje: "A co ubytování tam?", krátkodobá paměť zajistí, že agent ví, že "tam" odkazuje na "Paříž" v rámci stejné konverzace.

#### Dlouhodobá paměť

Toto jsou informace, které přetrvávají napříč více konverzacemi nebo relacemi. Umožňuje agentům pamatovat si uživatelské preference, historické interakce nebo obecné znalosti po delší dobu. To je důležité pro personalizaci.

**Příklad dlouhodobé paměti**

Dlouhodobá paměť může uchovávat, že "Ben má rád lyžování a outdoorové aktivity, má rád kávu s výhledem na hory a chce se vyhnout pokročilým lyžařským svahům kvůli minulému zranění". Tyto informace, naučené z předchozích interakcí, ovlivňují doporučení v budoucích plánovacích relacích, což je činí vysoce personalizovanými.

#### Paměť osobnosti

Tento specializovaný typ paměti pomáhá agentovi rozvíjet konzistentní "osobnost" nebo "roli". Umožňuje agentovi pamatovat si detaily o sobě nebo své zamýšlené roli, což činí interakce plynulejšími a zaměřenějšími.

**Příklad paměti osobnosti**

Pokud je cestovní agent navržen jako "expert na plánování lyžařských výletů", paměť osobnosti může posilovat tuto roli, ovlivňovat jeho odpovědi tak, aby odpovídaly tónu a znalostem experta.

#### Workflow/Epizodická paměť

Tato paměť uchovává sekvenci kroků, které agent podniká během složitého úkolu, včetně úspěchů a neúspěchů. Je to jako pamatovat si konkrétní "epizody" nebo minulé zkušenosti, aby se z nich mohl učit.

**Příklad epizodické paměti**

Pokud se agent pokusil rezervovat konkrétní let, ale neuspěl kvůli nedostupnosti, epizodická paměť by mohla zaznamenat tento neúspěch, což by agentovi umožnilo zkusit alternativní lety nebo informovat uživatele o problému při následném pokusu.

#### Paměť entit

Tato paměť zahrnuje extrakci a zapamatování konkrétních entit (jako jsou lidé, místa nebo věci) a událostí z konverzací. Umožňuje agentovi vytvořit strukturované porozumění klíčovým prvkům, o kterých se diskutuje.

**Příklad paměti entit**

Z konverzace o minulém výletu by agent mohl extrahovat "Paříž", "Eiffelova věž" a "večeře v restauraci Le Chat Noir" jako entity. V budoucí interakci by si agent mohl vzpomenout na "Le Chat Noir" a nabídnout rezervaci tam.

#### Strukturovaný RAG (Retrieval Augmented Generation)

Zatímco RAG je širší technika, "Strukturovaný RAG" je zdůrazněn jako výkonná paměťová technologie. Extrahuje husté, strukturované informace z různých zdrojů (konverzací, e-mailů, obrázků) a využívá je ke zvýšení přesnosti, vybavení a rychlosti odpovědí. Na rozdíl od klasického RAG, který se spoléhá pouze na sémantickou podobnost, Strukturovaný RAG pracuje s inherentní strukturou informací.

**Příklad strukturovaného RAG**

Místo pouhého shody klíčových slov by Strukturovaný RAG mohl analyzovat detaily letu (destinace, datum, čas, letecká společnost) z e-mailu a uložit je strukturovaným způsobem. To umožňuje přesné dotazy, jako například "Jaký let jsem si rezervoval do Paříže na úterý?"

## Implementace a ukládání paměti

Implementace paměti pro AI agenty zahrnuje systematický proces **správy paměti**, který zahrnuje generování, ukládání, vybavování, integraci, aktualizaci a dokonce "zapomínání" (nebo mazání) informací. Vybavování je obzvláště klíčovým aspektem.

### Specializované nástroje pro paměť

Jedním ze způsobů, jak ukládat a spravovat paměť agenta, je použití specializovaných nástrojů, jako je Mem0. Mem0 funguje jako vrstva trvalé paměti, která umožňuje agentům vybavovat si relevantní interakce, ukládat uživatelské preference a faktický kontext a učit se z úspěchů a neúspěchů v průběhu času. Myšlenkou je, že bezstavoví agenti se mění na stavové.

Funguje prostřednictvím **dvoufázového paměťového procesu: extrakce a aktualizace**. Nejprve jsou zprávy přidané do vlákna agenta odeslány do služby Mem0, která používá velký jazykový model (LLM) k sumarizaci historie konverzace a extrakci nových pamětí. Následně fáze aktualizace řízená LLM určuje, zda tyto paměti přidat, upravit nebo smazat, a ukládá je do hybridního datového úložiště, které může zahrnovat vektorové, grafové a klíč-hodnota databáze. Tento systém také podporuje různé typy paměti a může zahrnovat grafovou paměť pro správu vztahů mezi entitami.

### Ukládání paměti pomocí RAG

Kromě specializovaných nástrojů pro paměť, jako je Mem0, můžete využít robustní vyhledávací služby, jako je **Azure AI Search jako backend pro ukládání a vybavování pamětí**, zejména pro strukturovaný RAG.

To umožňuje zakotvit odpovědi agenta ve vašich vlastních datech, což zajišťuje relevantnější a přesnější odpovědi. Azure AI Search lze použít k ukládání uživatelských cestovních pamětí, katalogů produktů nebo jakýchkoli jiných znalostí specifických pro danou oblast.

Azure AI Search podporuje funkce jako **Strukturovaný RAG**, který vyniká při extrakci a vybavování hustých, strukturovaných informací z velkých datových sad, jako jsou historie konverzací, e-maily nebo dokonce obrázky. To poskytuje "nadlidskou přesnost a vybavení" ve srovnání s tradičními přístupy k textovému rozdělování a vkládání.

## Vytváření samostatně se zlepšujících AI agentů

Běžný vzor pro samostatně se zlepšující agenty zahrnuje zavedení **"agenta znalostí"**. Tento samostatný agent sleduje hlavní konverzaci mezi uživatelem a primárním agentem. Jeho role je:

1. **Identifikovat hodnotné informace**: Určit, zda je část konverzace vhodná k uložení jako obecná znalost nebo specifická uživatelská preference.

2. **Extrahovat a sumarizovat**: Destilovat podstatné učení nebo preference z konverzace.

3. **Uložit do znalostní databáze**: Uchovat tyto extrahované informace, často ve vektorové databázi, aby mohly být později vybaveny.

4. **Rozšířit budoucí dotazy**: Když uživatel zahájí nový dotaz, agent znalostí vybaví relevantní uložené informace a připojí je k uživatelskému promptu, čímž poskytne klíčový kontext primárnímu agentovi (podobně jako RAG).

### Optimalizace pro paměť

• **Správa latence**: Aby se zabránilo zpomalení uživatelských interakcí, může být zpočátku použit levnější a rychlejší model, který rychle zkontroluje, zda je informace hodnotná k uložení nebo vybavení, a složitější proces extrakce/vybavení se spustí pouze v případě potřeby.

• **Údržba znalostní databáze**: Pro rostoucí znalostní databázi mohou být méně často používané informace přesunuty do "studeného úložiště" pro správu nákladů.

## Máte další otázky ohledně inženýrství kontextu?

Připojte se na [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), kde se můžete setkat s dalšími studenty, zúčastnit se konzultačních hodin a získat odpovědi na vaše otázky ohledně AI agentů.

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.