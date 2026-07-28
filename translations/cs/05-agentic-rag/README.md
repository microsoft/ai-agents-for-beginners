[![Agentic RAG](../../../translated_images/cs/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Klikněte na obrázek výše pro zobrazení videa této lekce)_

# Agentic RAG

Tato lekce nabízí komplexní přehled o Agentic Retrieval-Augmented Generation (Agentic RAG), novém paradigmatickém přístupu v AI, kde velké jazykové modely (LLM) autonomně plánují své další kroky při získávání informací z externích zdrojů. Na rozdíl od statických vzorců „nejprve vyhledat a potom číst“ zahrnuje Agentic RAG iterativní volání LLM, prokládané voláními nástrojů nebo funkcí a strukturovanými výstupy. Systém vyhodnocuje výsledky, zpřesňuje dotazy, v případě potřeby vyvolává další nástroje a tento cyklus opakuje, dokud není dosaženo uspokojivého řešení.

## Úvod

Tato lekce pokrývá

- **Pochopení Agentic RAG:** Naučte se o novém paradigmatickém přístupu v AI, kde velké jazykové modely (LLM) autonomně plánují své další kroky při načítání informací z externích datových zdrojů.
- **Pochopení iterativního stylu Maker-Checker:** Porozumět smyčce iterativních volání LLM, prokládaných voláními nástrojů či funkcí a strukturovanými výstupy, navržené pro zlepšení správnosti a zvládání chybně formovaných dotazů.
- **Prozkoumání praktických aplikací:** Identifikovat scénáře, kde Agentic RAG exceluje, například prostředí s důrazem na správnost, složité databázové interakce a rozšířené pracovní postupy.

## Výukové cíle

Po dokončení této lekce budete schopni/porušíte:

- **Porozumění Agentic RAG:** Naučte se o novém paradigmatickém přístupu v AI, kde velké jazykové modely (LLM) autonomně plánují své další kroky při načítání informací z externích datových zdrojů.
- **Iterativní styl Maker-Checker:** Pochopte koncept smyčky iterativních volání LLM, prokládaných využitím nástrojů nebo funkcí a strukturovanými výstupy, navrženými ke zlepšení správnosti a zvládání chybně formovaných dotazů.
- **Vlastnictví procesu uvažování:** Pochopte schopnost systému disponovat vlastním procesem uvažování, rozhodovat o tom, jak přistupovat k problémům bez spoléhání se na předem dané cesty.
- **Pracovní postup:** Pochopte, jak agentní model nezávisle rozhoduje o získání reportů o tržních trendech, identifikaci konkurenčních dat, korelaci interních prodejních metrik, syntéze zjištění a vyhodnocení strategie.
- **Iterativní smyčky, integrace nástrojů a paměť:** Pochopte systém založený na vzoru interakce ve smyčce, udržující stav a paměť přes různé kroky, aby se předešlo opakování smyček a umožnilo přijímání informovaných rozhodnutí.
- **Zvládání režimů selhání a samoopravování:** Prozkoumejte robustní mechanismy samoopravování systému, včetně iterací a opětovného dotazování, používání diagnostických nástrojů a případného přechodu na lidský dohled.
- **Meze agentnosti:** Pochopte omezení Agentic RAG, se zaměřením na doménově specifickou autonomii, závislost na infrastruktuře a respektování bezpečnostních opatření.
- **Praktické případy použití a hodnota:** Identifikovat scénáře, ve kterých Agentic RAG vyniká, jako jsou prostředí kladoucí důraz na správnost, složité interakce s databázemi a rozšířené pracovní postupy.
- **Řízení, transparentnost a důvěra:** Naučte se o významu řízení a transparentnosti, včetně vysvětlitelného uvažování, kontroly zkreslení a lidského dohledu.

## Co je Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) je nově vznikající paradigmatický přístup v AI, kde velké jazykové modely (LLM) autonomně plánují své další kroky při získávání informací z externích zdrojů. Na rozdíl od statických vzorců „nejprve vyhledat a potom číst“ zahrnuje Agentic RAG iterativní volání LLM, prolínané voláními nástrojů či funkcí a strukturovanými výstupy. Systém vyhodnocuje výsledky, zpřesňuje dotazy, v případě potřeby vyvolává další nástroje a tento cyklus opakuje, dokud není dosaženo uspokojivého řešení. Tento iterativní styl „maker-checker“ zlepšuje správnost, zvládá chybné dotazy a zajišťuje vysoce kvalitní výsledky.

Systém aktivně ovládá svůj proces uvažování, přepisuje neúspěšné dotazy, vybírá jiné metody vyhledávání a integruje různé nástroje – například vektorové vyhledávání v Azure AI Search, SQL databáze či vlastní API – než dospěje ke konečné odpovědi. Rozlišující vlastností agentního systému je jeho schopnost vlastnit svůj proces uvažování. Tradiční implementace RAG spoléhají na předem definované cesty, zatímco agentní systém autonomně určuje posloupnost kroků na základě kvality nalezených informací.

## Definice Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) je nově vznikající paradigmatický přístup v oblasti vývoje AI, kde LLM nejen získávají informace z externích datových zdrojů, ale také autonomně plánují své další kroky. Na rozdíl od statických vzorců „nejprve vyhledat a poté číst“ nebo pečlivě skriptovaných sekvencí promptů zahrnuje Agentic RAG smyčku iterativních volání LLM, prokládaných voláními nástrojů či funkcí a strukturovanými výstupy. Systém vždy vyhodnocuje získané výsledky, rozhoduje se, zda dotazy zpřesnit, v případě potřeby vyvolává další nástroje a tento cyklus pokračuje, dokud není dosaženo uspokojivého řešení.

Tento iterativní styl „maker-checker“ je navržen ke zvýšení správnosti, zvládání chybně formovaných dotazů do strukturovaných databází (např. NL2SQL) a zajištění vyvážených, vysoce kvalitních výsledků. Místo spoléhání se výhradně na pečlivě navržené řetězce promptů systém aktivně vlastní svůj proces uvažování. Může přepisovat neúspěšné dotazy, volit jiné metody vyhledávání a integrovat více nástrojů – například vektorové vyhledávání v Azure AI Search, SQL databáze nebo vlastní API – než dospěje ke konečné odpovědi. Odpadá potřeba příliš složitých orchestracích frameworků. Místo toho relativně jednoduchá smyčka „volání LLM → použití nástroje → volání LLM → …“ může přinést sofistikované a solidní výstupy.

![Agentic RAG Core Loop](../../../translated_images/cs/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## Vlastnictví procesu uvažování

Rozlišující vlastností, která dělá systém „agentní“, je jeho schopnost vlastnit svůj proces uvažování. Tradiční implementace RAG často závisí na tom, že lidé předem definují modelu cestu: řetězec myšlenek, který stanovuje, co se má kdy vyhledávat.
Ale když je systém skutečně agentní, rozhoduje interně, jak přistoupit k problému. Nejenže vykonává skript, ale autonomně určuje posloupnost kroků na základě kvality nalezených informací.
Například pokud má vytvořit strategii uvedení produktu na trh, nespoléhá se pouze na prompt, který přesně popisuje celý výzkumný a rozhodovací proces. Agentní model místo toho nezávisle rozhoduje, že:

1. Získá aktuální zprávy o trendech na trhu pomocí Bing Web Grounding
2. Identifikuje relevantní data o konkurentech pomocí Azure AI Search.
3. Koreluje historické interní prodejní metriky pomocí Azure SQL Database.
4. Syntetizuje zjištění do soudržné strategie, kterou orchestruje přes Azure OpenAI Service.
5. Vyhodnotí strategii na mezery nebo rozporuplnosti a v případě potřeby vyvolá další kolo vyhledávání.
Všechny tyto kroky – zpřesnění dotazů, volba zdrojů, iterace dokud není „spokojený“ s odpovědí – jsou rozhodovány modelem, nikoli předem skriptovány člověkem.

## Iterativní smyčky, integrace nástrojů a paměť

![Tool Integration Architecture](../../../translated_images/cs/tool-integration.0f569710b5c17c10.webp)

Agentní systém spoléhá na vzor interakce ve smyčce:

- **Inicialní volání:** Cíl uživatele (tj. vstupní prompt) je předán LLM.
- **Vyvolání nástroje:** Pokud model zjistí chybějící informace nebo nejasné instrukce, vybere nástroj nebo metodu vyhledávání – například dotaz do vektorové databáze (např. Azure AI Search Hybrid vyhledávání nad soukromými daty) nebo strukturovaný SQL dotaz – aby získal další kontext.
- **Hodnocení a zpřesnění:** Po přezkoumání získaných dat model rozhodne, zda informace stačí. Pokud ne, zpřesní dotaz, zkusí jiný nástroj nebo upraví svůj přístup.
- **Opakovat dokud není spokojen:** Tento cyklus pokračuje, dokud model nerozhodne, že má dostatečnou jasnost a důkazy pro dodání konečné a dobře zdůvodněné odpovědi.
- **Paměť a stav:** Protože systém udržuje stav a paměť přes jednotlivé kroky, může si pamatovat předchozí pokusy a jejich výsledky, vyhnout se opakování smyček a přijímat informovanější rozhodnutí v průběhu.

Postupem času to vytváří dojem vyvíjejícího se porozumění, což modelu umožňuje zvládat složité úkoly zahrnující více kroků bez nutnosti soustavného zásahu člověka nebo přepisování promptu.

## Zvládání režimů selhání a samoopravování

Autonomie Agentic RAG zahrnuje také robustní mechanismy samoopravování. Když systém narazí na slepé uličky – například nalezení nerelevantních dokumentů nebo setkání s chybnými dotazy – může:

- **Iterovat a znovu klást dotazy:** Místo vracení málo hodnotných odpovědí model zkouší nové vyhledávací strategie, přepisuje databázové dotazy nebo zkoumá alternativní datové sady.
- **Použití diagnostických nástrojů:** Systém může vyvolat další funkce určené k diagnostice kroků uvažování nebo ověření správnosti získaných dat. Nástroje jako Azure AI Tracing budou důležité pro umožnění robustní sledovatelnosti a monitorování.
- **Přechod na lidský dohled:** Pro scénáře s vysokou zátěží nebo opakujícím se selháváním může model označit nejistotu a požádat o lidskou pomoc. Poté, co člověk poskytne nápravnou zpětnou vazbu, může model toto poučení začlenit do budoucna.

Tento iterativní a dynamický přístup umožňuje modelu se neustále zlepšovat a zajistit, že nejde o systém jednorázový, ale o systém, který se učí ze svých chyb během dané relace.

![Self Correction Mechanism](../../../translated_images/cs/self-correction.da87f3783b7f174b.webp)

## Meze agentnosti

Přestože má autonomii v rámci úkolu, Agentic RAG není ekvivalentem Umělé obecné inteligence. Jeho „agentní“ schopnosti jsou omezeny na nástroje, datové zdroje a politiky poskytované lidskými vývojáři. Nemůže si vymýšlet vlastní nástroje ani opustit hranice domény, které byly nastaveny. Místo toho vyniká v dynamické orchestraci dostupných zdrojů.
Klíčové rozdíly od pokročilejších forem AI zahrnují:

1. **Doménově specifická autonomie:** Agentic RAG systémy se zaměřují na dosahování uživatelem definovaných cílů v rámci známé domény, využívající strategie jako přepisování dotazů nebo výběr nástrojů ke zlepšení výsledků.
2. **Závislost na infrastruktuře:** Schopnosti systému závisí na nástrojích a datech integrováných vývojáři. Nemůže tyto hranice překročit bez lidského zásahu.
3. **Respektování bezpečnostních opatření:** Etické směrnice, pravidla souladu a obchodní politiky zůstávají velmi důležité. Svoboda agenta je vždy omezena bezpečnostními opatřeními a dozorovými mechanismy (doufejme?).

## Praktické případy použití a hodnota

Agentic RAG vyniká v scénářích vyžadujících iterativní zpřesňování a přesnost:

1. **Prostředí kladoucí důraz na správnost:** Při kontrolách souladu, regulačních analýzách nebo právním výzkumu může agentní model opakovaně ověřovat fakta, konzultovat více zdrojů a přepisovat dotazy, dokud nevytvoří důkladně ověřenou odpověď.
2. **Složité databázové interakce:** Při práci se strukturovanými daty, kde se dotazy často nedaří nebo je potřeba je upravovat, může systém autonomně zpřesňovat dotazy pomocí Azure SQL nebo Microsoft Fabric OneLake, aby zajistil, že výsledné získání odpovídá záměru uživatele.
3. **Rozšířené pracovní postupy:** Dlouhotrvající relace se mohou vyvíjet s tím, jak se objevují nové informace. Agentic RAG může kontinuálně začleňovat nová data, měnit strategie podle toho, jak se učí více o problematickém prostoru.

## Řízení, transparentnost a důvěra

Jak tyto systémy získávají více autonomie ve svém uvažování, je řízení a transparentnost klíčové:

- **Vysvětlitelné uvažování:** Model může poskytovat auditní stopu dotazů, které položil, zdrojů, které konzultoval, a kroků uvažování, kterými prošel, aby dospěl ke svému závěru. Nástroje jako Azure AI Content Safety a Azure AI Tracing / GenAIOps pomáhají udržovat transparentnost a zmírňovat rizika.
- **Kontrola zkreslení a vyvážené vyhledávání:** Vývojáři mohou ladit strategie vyhledávání, aby zajistili, že jsou zohledňovány vyvážené a reprezentativní datové zdroje, a pravidelně auditovat výstupy, aby odhalili zkreslení nebo nesprávné vzory pomocí vlastních modelů pro pokročilé datově vědecké organizace využívající Azure Machine Learning.
- **Lidský dohled a shoda:** Pro citlivé úkoly zůstává lidský přezkum nezbytný. Agentic RAG nenahrazuje lidský úsudek ve vysoce rizikových rozhodnutích – rozšiřuje ho tím, že dodává důkladně prověřené možnosti.

Mít nástroje, které poskytují jasný záznam akcí, je nezbytné. Bez nich může být ladění vícekrokového procesu velmi náročné. Viz následující příklad od Literal AI (společnosti za Chainlit) pro běh agenta:

![AgentRunExample](../../../translated_images/cs/AgentRunExample.471a94bc40cbdc0c.webp)

## Závěr

Agentic RAG představuje přirozený vývoj v tom, jak AI systémy zvládají složité, datově náročné úkoly. Přijetím smyčkového vzoru interakce, autonomním výběrem nástrojů a zpřesňováním dotazů dokud nedosáhne vysoce kvalitního výsledku, systém přechází od statického následování promptů k adaptivnějšímu, kontextově uvědomělému rozhodovacímu procesu. Přestože je stále omezen lidsky definovanou infrastrukturou a etickými zásadami, tyto agentní schopnosti umožňují bohatší, dynamičtější a konečně užitečnější AI interakce jak pro podniky, tak koncové uživatele.

### Máte další otázky ohledně Agentic RAG?

Připojte se k [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kde se setkáte s dalšími studenty, zúčastníte se konzultací a získáte odpovědi na své otázky týkající se AI agentů.

## Další zdroje

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">Implementace Retrieval Augmented Generation (RAG) s Azure OpenAI Service: Naučte se používat svá data s Azure OpenAI Service. Tento modul Microsoft Learn poskytuje komplexního průvodce implementací RAG</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Hodnocení generativních AI aplikací s Microsoft Foundry: Tento článek pokrývá hodnocení a porovnání modelů na veřejně dostupných datech, včetně agentních AI aplikací a RAG architektur</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Co je Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Kompletní průvodce agentní Retrieval Augmented Generation – Novinky z generation RAG</a>

- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: zrychlete svůj RAG pomocí přeformulování dotazů a samo-dotazování! Hugging Face Open-Source AI Cookbook</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Přidání agentních vrstev do RAG</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Budoucnost znalostních asistentů: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Jak vybudovat agentní RAG systémy</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Použití Microsoft Foundry Agent Service pro škálování vašich AI agentů</a>

### Akademické články

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Iterativní vylepšování se zpětnou vazbou od sebe sama</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Jazykoví agenti s verbálním posilovacím učením</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Velké jazykové modely se mohou samy korigovat pomocí nástrojově interaktivních hodnocení</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentické retrieval-augmentované generování: Přehled o agentním RAG</a>

## Smoke-testování tohoto agenta (volitelné)

Poté, co se naučíte nasazovat agenty v [Lekci 16](../16-deploying-scalable-agents/README.md), můžete smoke-testovat `TravelRAGAgent` z této lekce — kontrolovat, že jeho odpovědi zůstávají založeny na znalostní bázi — pomocí [`tests/lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json). Viz [`tests/README.md`](../tests/README.md) pro instrukce, jak test spustit.

## Předchozí lekce

[Designový vzor používání nástrojů](../04-tool-use/README.md)

## Následující lekce

[Budování důvěryhodných AI agentů](../06-building-trustworthy-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->