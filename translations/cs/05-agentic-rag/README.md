<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d2f04b783b9e1253100329afd698f8ff",
  "translation_date": "2025-08-29T20:25:43+00:00",
  "source_file": "05-agentic-rag/README.md",
  "language_code": "cs"
}
-->
[![Agentic RAG](../../../translated_images/lesson-5-thumbnail.20ba9d0c0ae64fae06637eb2023395d437b0152c0463c2227ff456afe5f14644.cs.png)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Klikněte na obrázek výše pro zhlédnutí videa této lekce)_

# Agentic RAG

Tato lekce poskytuje komplexní přehled o Agentic Retrieval-Augmented Generation (Agentic RAG), nově vznikajícím AI paradigmatu, kde velké jazykové modely (LLMs) autonomně plánují své další kroky a zároveň čerpají informace z externích zdrojů. Na rozdíl od statických vzorců „vyhledat a přečíst“ Agentic RAG zahrnuje iterativní volání LLM, prokládané voláním nástrojů nebo funkcí a strukturovanými výstupy. Systém vyhodnocuje výsledky, zpřesňuje dotazy, v případě potřeby volá další nástroje a pokračuje v tomto cyklu, dokud nedosáhne uspokojivého řešení.

## Úvod

Tato lekce pokryje:

- **Pochopení Agentic RAG:** Seznamte se s nově vznikajícím paradigmatem v AI, kde velké jazykové modely (LLMs) autonomně plánují své další kroky a zároveň čerpají informace z externích datových zdrojů.
- **Iterativní styl Maker-Checker:** Pochopte smyčku iterativních volání LLM, prokládaných voláním nástrojů nebo funkcí a strukturovanými výstupy, navrženou ke zlepšení přesnosti a zvládání chybných dotazů.
- **Praktické aplikace:** Identifikujte scénáře, kde Agentic RAG vyniká, jako jsou prostředí zaměřená na přesnost, složité interakce s databázemi a rozšířené pracovní postupy.

## Cíle učení

Po dokončení této lekce budete vědět, jak/rozumět:

- **Pochopení Agentic RAG:** Seznamte se s nově vznikajícím paradigmatem v AI, kde velké jazykové modely (LLMs) autonomně plánují své další kroky a zároveň čerpají informace z externích datových zdrojů.
- **Iterativní styl Maker-Checker:** Pochopte koncept smyčky iterativních volání LLM, prokládaných voláním nástrojů nebo funkcí a strukturovanými výstupy, navržený ke zlepšení přesnosti a zvládání chybných dotazů.
- **Vlastnictví procesu uvažování:** Pochopte schopnost systému vlastnit svůj proces uvažování, rozhodovat o tom, jak přistupovat k problémům, aniž by se spoléhal na předem definované cesty.
- **Pracovní postup:** Pochopte, jak agentický model nezávisle rozhoduje o získávání zpráv o trendech na trhu, identifikaci dat o konkurenci, korelaci interních prodejních metrik, syntéze zjištění a hodnocení strategie.
- **Iterativní smyčky, integrace nástrojů a paměť:** Naučte se, jak systém spoléhá na vzor interakce ve smyčce, udržuje stav a paměť napříč kroky, aby se vyhnul opakovaným smyčkám a činil informovaná rozhodnutí.
- **Zvládání selhání a sebekorekce:** Prozkoumejte robustní mechanismy sebekorekce systému, včetně iterace a opětovného dotazování, používání diagnostických nástrojů a spoléhání na lidský dohled.
- **Hranice agentury:** Pochopte omezení Agentic RAG, zaměřte se na autonomii specifickou pro danou doménu, závislost na infrastruktuře a respektování ochranných opatření.
- **Praktické případy použití a hodnota:** Identifikujte scénáře, kde Agentic RAG vyniká, jako jsou prostředí zaměřená na přesnost, složité interakce s databázemi a rozšířené pracovní postupy.
- **Řízení, transparentnost a důvěra:** Naučte se o důležitosti řízení a transparentnosti, včetně vysvětlitelného uvažování, kontroly zaujatosti a lidského dohledu.

## Co je Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) je nově vznikající AI paradigma, kde velké jazykové modely (LLMs) autonomně plánují své další kroky a zároveň čerpají informace z externích zdrojů. Na rozdíl od statických vzorců „vyhledat a přečíst“ Agentic RAG zahrnuje iterativní volání LLM, prokládané voláním nástrojů nebo funkcí a strukturovanými výstupy. Systém vyhodnocuje výsledky, zpřesňuje dotazy, v případě potřeby volá další nástroje a pokračuje v tomto cyklu, dokud nedosáhne uspokojivého řešení. Tento iterativní styl „maker-checker“ zlepšuje přesnost, zvládá chybné dotazy a zajišťuje vysoce kvalitní výsledky.

Systém aktivně vlastní svůj proces uvažování, přepisuje neúspěšné dotazy, volí různé metody vyhledávání a integruje více nástrojů—jako je vektorové vyhledávání v Azure AI Search, SQL databáze nebo vlastní API—před dokončením své odpovědi. Rozlišující kvalitou agentického systému je jeho schopnost vlastnit svůj proces uvažování. Tradiční implementace RAG spoléhají na předem definované cesty, ale agentický systém autonomně určuje sekvenci kroků na základě kvality nalezených informací.

## Definice Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) je nově vznikající paradigma ve vývoji AI, kde LLM nejen čerpají informace z externích datových zdrojů, ale také autonomně plánují své další kroky. Na rozdíl od statických vzorců „vyhledat a přečíst“ nebo pečlivě skriptovaných sekvencí promptů Agentic RAG zahrnuje smyčku iterativních volání LLM, prokládaných voláním nástrojů nebo funkcí a strukturovanými výstupy. V každém kroku systém vyhodnocuje získané výsledky, rozhoduje, zda zpřesnit dotazy, volá další nástroje, pokud je to potřeba, a pokračuje v tomto cyklu, dokud nedosáhne uspokojivého řešení.

Tento iterativní styl „maker-checker“ je navržen ke zlepšení přesnosti, zvládání chybných dotazů na strukturované databáze (např. NL2SQL) a zajištění vyvážených, vysoce kvalitních výsledků. Namísto spoléhání se pouze na pečlivě navržené řetězce promptů systém aktivně vlastní svůj proces uvažování. Může přepisovat neúspěšné dotazy, volit různé metody vyhledávání a integrovat více nástrojů—jako je vektorové vyhledávání v Azure AI Search, SQL databáze nebo vlastní API—před dokončením své odpovědi. To eliminuje potřebu příliš složitých orchestrálních rámců. Místo toho relativně jednoduchá smyčka „volání LLM → použití nástroje → volání LLM → …“ může přinést sofistikované a dobře podložené výstupy.

![Agentic RAG Core Loop](../../../translated_images/agentic-rag-core-loop.c8f4b85c26920f71ed181ebb14001ac7aae47c0b0af237edcf71898645a62db3.cs.png)

## Vlastnictví procesu uvažování

Rozlišující kvalitou, která činí systém „agentickým“, je jeho schopnost vlastnit svůj proces uvažování. Tradiční implementace RAG často závisí na tom, že lidé předem definují cestu pro model: řetězec myšlenek, který určuje, co a kdy vyhledat.  
Ale když je systém skutečně agentický, rozhoduje interně, jak k problému přistoupit. Neprovádí jen skript; autonomně určuje sekvenci kroků na základě kvality nalezených informací.  
Například pokud je požádán o vytvoření strategie uvedení produktu na trh, nespoléhá se pouze na prompt, který podrobně popisuje celý výzkumný a rozhodovací pracovní postup. Místo toho agentický model nezávisle rozhodne:

1. Získat aktuální zprávy o trendech na trhu pomocí Bing Web Grounding.
2. Identifikovat relevantní data o konkurenci pomocí Azure AI Search.
3. Korelovat historické interní prodejní metriky pomocí Azure SQL Database.
4. Syntetizovat zjištění do ucelené strategie zpracované prostřednictvím Azure OpenAI Service.
5. Vyhodnotit strategii z hlediska mezer nebo nesrovnalostí a případně vyvolat další kolo vyhledávání.  
Všechny tyto kroky—zpřesňování dotazů, volba zdrojů, iterace, dokud není „spokojen“ s odpovědí—jsou rozhodnuty modelem, nikoli předem skriptovány člověkem.

## Iterativní smyčky, integrace nástrojů a paměť

![Tool Integration Architecture](../../../translated_images/tool-integration.0f569710b5c17c106757adba082f6c4be025ca0721bff7d1ee4b929a3617a600.cs.png)

Agentický systém spoléhá na vzor interakce ve smyčce:

- **Počáteční volání:** Cíl uživatele (tj. uživatelský prompt) je představen LLM.
- **Volání nástroje:** Pokud model identifikuje chybějící informace nebo nejasné pokyny, vybere nástroj nebo metodu vyhledávání—například dotaz na vektorovou databázi (např. Azure AI Search Hybrid search nad soukromými daty) nebo strukturované volání SQL—k získání více kontextu.
- **Hodnocení a zpřesnění:** Po přezkoumání vrácených dat model rozhodne, zda informace postačují. Pokud ne, zpřesní dotaz, vyzkouší jiný nástroj nebo upraví svůj přístup.
- **Opakování, dokud není spokojen:** Tento cyklus pokračuje, dokud model neurčí, že má dostatek jasnosti a důkazů k poskytnutí konečné, dobře odůvodněné odpovědi.
- **Paměť a stav:** Protože systém udržuje stav a paměť napříč kroky, může si pamatovat předchozí pokusy a jejich výsledky, vyhnout se opakovaným smyčkám a činit informovanější rozhodnutí, jak postupuje.

Tímto způsobem se postupem času vytváří pocit vyvíjejícího se porozumění, což umožňuje modelu zvládat složité, vícestupňové úkoly bez nutnosti neustálého zásahu člověka nebo přeformulování promptu.

## Zvládání selhání a sebekorekce

Autonomie Agentic RAG zahrnuje také robustní mechanismy sebekorekce. Když systém narazí na slepé uličky—například získávání nerelevantních dokumentů nebo setkání s chybnými dotazy—může:

- **Iterovat a opětovně se dotazovat:** Namísto vrácení odpovědí s nízkou hodnotou model zkouší nové strategie vyhledávání, přepisuje dotazy na databáze nebo zkoumá alternativní datové sady.
- **Používat diagnostické nástroje:** Systém může volat další funkce navržené k tomu, aby mu pomohly ladit jeho kroky uvažování nebo potvrdit správnost získaných dat. Nástroje jako Azure AI Tracing budou důležité pro umožnění robustní pozorovatelnosti a monitorování.
- **Spoléhat na lidský dohled:** U scénářů s vysokými sázkami nebo opakovanými selháními může model označit nejistotu a požádat o lidské vedení. Jakmile člověk poskytne korektivní zpětnou vazbu, model může tuto lekci začlenit do budoucna.

Tento iterativní a dynamický přístup umožňuje modelu neustále se zlepšovat, což zajišťuje, že není jen jednorázovým systémem, ale systémem, který se během dané relace učí ze svých chyb.

![Self Correction Mechanism](../../../translated_images/self-correction.da87f3783b7f174bdc592c754b352884dd283814758bfeb7a68f5fd910272f3b.cs.png)

## Hranice agentury

Navzdory své autonomii v rámci úkolu Agentic RAG není analogický s umělou obecnou inteligencí. Jeho „agentické“ schopnosti jsou omezeny na nástroje, datové zdroje a politiky poskytované lidskými vývojáři. Nemůže si vymýšlet vlastní nástroje nebo překračovat hranice domény, které byly nastaveny. Spíše vyniká v dynamickém orchestraci dostupných zdrojů.  
Klíčové rozdíly oproti pokročilejším formám AI zahrnují:

1. **Autonomie specifická pro doménu:** Systémy Agentic RAG se zaměřují na dosažení uživatelem definovaných cílů v rámci známé domény, přičemž využívají strategie jako přepisování dotazů nebo výběr nástrojů ke zlepšení výsledků.
2. **Závislost na infrastruktuře:** Schopnosti systému závisí na nástrojích a datech integrovaných vývojáři. Nemůže překročit tyto hranice bez lidského zásahu.
3. **Respektování ochranných opatření:** Etické pokyny, pravidla dodržování předpisů a obchodní politiky zůstávají velmi důležité. Svoboda agenta je vždy omezena bezpečnostními opatřeními a mechanismy dohledu (snad?).

## Praktické případy použití a hodnota

Agentic RAG vyniká ve scénářích vyžadujících iterativní zpřesňování a přesnost:

1. **Prostředí zaměřená na přesnost:** Při kontrolách souladu, regulační analýze nebo právním výzkumu může agentický model opakovaně ověřovat fakta, konzultovat více zdrojů a přepisovat dotazy, dokud neposkytne důkladně ověřenou odpověď.
2. **Složité interakce s databázemi:** Při práci se strukturovanými daty, kde dotazy často selhávají nebo potřebují úpravy, může systém autonomně zpřesňovat své dotazy pomocí Azure SQL nebo Microsoft Fabric OneLake, čímž zajistí, že konečné vyhledávání odpovídá záměru uživatele.
3. **Rozšířené pracovní postupy:** Dlouhodobější relace se mohou vyvíjet, jak se objevují nové informace. Agentic RAG může neustále začleňovat nová data a měnit strategie, jak se dozvídá více o problematice.

## Řízení, transparentnost a důvěra

Jak se tyto systémy stávají autonomnějšími ve svém uvažování, řízení a transparentnost jsou klíčové:

- **Vysvětlitelné uvažování:** Model může poskytnout auditní stopu dotazů, které vytvořil, zdrojů, které konzultoval, a kroků uvažování, které podnikl k dosažení svého závěru. Nástroje jako Azure AI Content Safety a Azure AI Tracing / GenAIOps mohou pomoci udržet transparentnost a zmírnit rizika.
- **Kontrola zaujatosti a vyvážené vyhledávání:** Vývojáři mohou ladit strategie vyhledávání, aby zajistili, že budou zvažovány vyvážené, reprezentativní datové zdroje, a pravidelně auditovat výstupy, aby odhalili zaujatost nebo zkreslené vzorce pomocí vlastních modelů pro pokročilé datové vědecké organizace využívající Azure Machine Learning.
- **Lidský dohled a dodržování předpisů:** U citlivých úkolů zůstává lidská kontrola nezbytná. Agentic RAG nenahrazuje lidský úsudek při rozhodování s vysokými sázkami—spíše jej doplňuje tím, že poskytuje důkladněji ověřené možnosti.

Mít nástroje, které poskytují jasný záznam akcí, je zásadní. Bez nich může být ladění vícestupňového procesu velmi obtížné. Podívejte se na následující příklad od Literal AI (společnost za Chainlit) pro běh agenta:

![AgentRunExample](../../../translated_images/AgentRunExample.471a94bc40cbdc0cd04c1f43c8d8c9b751f10d97918c900e29cb3ba0d6aa4c00.cs.png)

## Závěr

Agentic RAG představuje přirozený vývoj v tom, jak AI systémy zvládají složité, datově náročné úkoly. Přijetím vzoru interakce ve smyčce, autonomním výběrem nástrojů a zpřesňováním dotazů, dokud nedosáhne vysoce kvalitního výsledku, systém překračuje statické sledování promptů a stává se adaptivnějším, kontextově uvědomělejším rozhodovacím nástrojem. Přestože je stále omezen lidsky definovanými
<a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">
Implementace Retrieval Augmented Generation (RAG) s Azure OpenAI Service: Naučte se, jak používat vlastní data s Azure OpenAI Service. Tento modul Microsoft Learn poskytuje komplexní průvodce implementací RAG</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Hodnocení aplikací generativní AI s Azure AI Foundry: Tento článek se zabývá hodnocením a porovnáváním modelů na veřejně dostupných datových sadách, včetně aplikací Agentic AI a architektur RAG</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Co je Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Kompletní průvodce agentově založeným Retrieval Augmented Generation – Novinky z generace RAG</a>
- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: zrychlete svůj RAG pomocí reformulace dotazů a self-query! Hugging Face Open-Source AI Cookbook</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Přidání agentických vrstev do RAG</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Budoucnost asistentů znalostí: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Jak vytvořit systémy Agentic RAG</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Použití služby Azure AI Foundry Agent k rozšíření vašich AI agentů</a>

### Akademické články

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Iterativní zdokonalování pomocí zpětné vazby</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Jazykoví agenti s verbálním posilovacím učením</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Velké jazykové modely se mohou samy opravovat pomocí interaktivního kritického nástroje</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation: Přehled o Agentic RAG</a>

## Předchozí lekce

[Design Pattern pro použití nástrojů](../04-tool-use/README.md)

## Další lekce

[Budování důvěryhodných AI agentů](../06-building-trustworthy-agents/README.md)

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádné nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.