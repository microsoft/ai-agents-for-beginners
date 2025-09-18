<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aff92c6f019b4627ca9399c6e3882e17",
  "translation_date": "2025-09-18T15:29:58+00:00",
  "source_file": "11-agentic-protocols/README.md",
  "language_code": "cs"
}
-->
# Používání agentních protokolů (MCP, A2A a NLWeb)

[![Agentní protokoly](../../../translated_images/lesson-11-thumbnail.b6c742949cf1ce2aa0255968d287b31c99b51dfa9c9beaede7c3fbed90e8fcfb.cs.png)](https://youtu.be/X-Dh9R3Opn8)

> _(Klikněte na obrázek výše pro zhlédnutí videa k této lekci)_

S rostoucím využíváním AI agentů roste i potřeba protokolů, které zajistí standardizaci, bezpečnost a podporu otevřené inovace. V této lekci se zaměříme na 3 protokoly, které se snaží tyto potřeby naplnit – Model Context Protocol (MCP), Agent to Agent (A2A) a Natural Language Web (NLWeb).

## Úvod

V této lekci se naučíte:

• Jak **MCP** umožňuje AI agentům přístup k externím nástrojům a datům pro splnění úkolů uživatele.

• Jak **A2A** umožňuje komunikaci a spolupráci mezi různými AI agenty.

• Jak **NLWeb** přináší rozhraní v přirozeném jazyce na jakýkoli web, což umožňuje AI agentům objevovat a interagovat s obsahem.

## Cíle učení

• **Identifikovat** hlavní účel a přínosy MCP, A2A a NLWeb v kontextu AI agentů.

• **Vysvětlit**, jak každý protokol usnadňuje komunikaci a interakci mezi LLM, nástroji a dalšími agenty.

• **Rozpoznat** odlišné role, které každý protokol hraje při budování komplexních agentních systémů.

## Model Context Protocol

**Model Context Protocol (MCP)** je otevřený standard, který poskytuje standardizovaný způsob, jak aplikace poskytují kontext a nástroje LLM. To umožňuje "univerzální adaptér" pro různé datové zdroje a nástroje, ke kterým se AI agenti mohou připojit konzistentním způsobem.

Podívejme se na komponenty MCP, výhody oproti přímému používání API a příklad, jak by AI agenti mohli využívat MCP server.

### Základní komponenty MCP

MCP funguje na **architektuře klient-server** a jeho základní komponenty jsou:

• **Hostitelé** jsou aplikace LLM (například editor kódu jako VSCode), které zahajují připojení k MCP serveru.

• **Klienti** jsou komponenty v hostitelské aplikaci, které udržují jednosměrná připojení k serverům.

• **Servery** jsou lehké programy, které poskytují specifické schopnosti.

Protokol zahrnuje tři základní primitivy, které představují schopnosti MCP serveru:

• **Nástroje**: Jsou to samostatné akce nebo funkce, které může AI agent vyvolat pro provedení úkolu. Například služba počasí může poskytovat nástroj "získat počasí" nebo e-commerce server může poskytovat nástroj "zakoupit produkt". MCP servery inzerují název, popis a schéma vstupů/výstupů každého nástroje ve svém seznamu schopností.

• **Zdroje**: Jsou to položky dat nebo dokumenty pouze pro čtení, které může MCP server poskytovat a klienti je mohou na vyžádání získat. Příklady zahrnují obsah souborů, záznamy databáze nebo logy. Zdroje mohou být textové (například kód nebo JSON) nebo binární (například obrázky nebo PDF).

• **Prompty**: Jsou to předdefinované šablony, které poskytují navrhované prompty, umožňující složitější pracovní postupy.

### Výhody MCP

MCP nabízí významné výhody pro AI agenty:

• **Dynamické objevování nástrojů**: Agenti mohou dynamicky získat seznam dostupných nástrojů ze serveru spolu s popisy jejich funkcí. To je v kontrastu s tradičními API, které často vyžadují statické kódování pro integrace, což znamená, že jakákoli změna API vyžaduje aktualizaci kódu. MCP nabízí přístup "integrovat jednou", což vede k větší přizpůsobivosti.

• **Interoperabilita mezi LLM**: MCP funguje napříč různými LLM, což poskytuje flexibilitu při přepínání základních modelů pro lepší výkon.

• **Standardizovaná bezpečnost**: MCP zahrnuje standardní metodu autentizace, což zlepšuje škálovatelnost při přidávání přístupu k dalším MCP serverům. To je jednodušší než správa různých klíčů a typů autentizace pro různé tradiční API.

### Příklad MCP

![MCP Diagram](../../../translated_images/mcp-diagram.e4ca1cbd551444a12e1f0eb300191a036ab01124fce71c864fe9cb7f4ac2a15d.cs.png)

Představte si, že uživatel chce rezervovat let pomocí AI asistenta poháněného MCP.

1. **Připojení**: AI asistent (MCP klient) se připojí k MCP serveru poskytovanému leteckou společností.

2. **Objevování nástrojů**: Klient se zeptá MCP serveru letecké společnosti: "Jaké nástroje máte k dispozici?" Server odpoví nástroji jako "vyhledat lety" a "rezervovat lety".

3. **Vyvolání nástroje**: Poté požádáte AI asistenta: "Prosím, vyhledej let z Portlandu do Honolulu." AI asistent pomocí svého LLM identifikuje, že potřebuje vyvolat nástroj "vyhledat lety" a předá relevantní parametry (původ, destinace) MCP serveru.

4. **Provedení a odpověď**: MCP server, fungující jako obal, provede skutečné volání na interní API letecké společnosti. Poté obdrží informace o letu (například JSON data) a pošle je zpět AI asistentovi.

5. **Další interakce**: AI asistent představí možnosti letu. Jakmile vyberete let, asistent může vyvolat nástroj "rezervovat let" na stejném MCP serveru a dokončit rezervaci.

## Protokol Agent-to-Agent (A2A)

Zatímco MCP se zaměřuje na připojení LLM k nástrojům, **Agent-to-Agent (A2A) protokol** jde o krok dále tím, že umožňuje komunikaci a spolupráci mezi různými AI agenty. A2A propojuje AI agenty napříč různými organizacemi, prostředími a technologickými stacky, aby splnily společný úkol.

Prozkoumáme komponenty a výhody A2A spolu s příkladem, jak by mohl být aplikován v naší cestovní aplikaci.

### Základní komponenty A2A

A2A se zaměřuje na umožnění komunikace mezi agenty a jejich spolupráci na splnění dílčího úkolu uživatele. Každá komponenta protokolu k tomu přispívá:

#### Agentní karta

Podobně jako MCP server sdílí seznam nástrojů, agentní karta obsahuje:
- Název agenta.
- **Popis obecných úkolů**, které agent plní.
- **Seznam specifických dovedností** s popisy, které pomáhají ostatním agentům (nebo dokonce lidským uživatelům) pochopit, kdy a proč by chtěli zavolat tohoto agenta.
- **Aktuální URL koncového bodu** agenta.
- **Verzi** a **schopnosti** agenta, jako jsou streamované odpovědi a push notifikace.

#### Agentní vykonavatel

Agentní vykonavatel je zodpovědný za **předání kontextu uživatelského chatu vzdálenému agentovi**, který tento kontext potřebuje k pochopení úkolu, který má být splněn. Na A2A serveru agent používá svůj vlastní LLM k analýze příchozích požadavků a provádění úkolů pomocí svých vlastních interních nástrojů.

#### Artefakt

Jakmile vzdálený agent dokončí požadovaný úkol, jeho výsledek je vytvořen jako artefakt. Artefakt **obsahuje výsledek práce agenta**, **popis toho, co bylo dokončeno**, a **textový kontext**, který je poslán přes protokol. Po odeslání artefaktu je připojení s vzdáleným agentem uzavřeno, dokud není znovu potřeba.

#### Fronta událostí

Tato komponenta se používá pro **zpracování aktualizací a předávání zpráv**. Je obzvláště důležitá v produkci pro agentní systémy, aby se zabránilo uzavření připojení mezi agenty před dokončením úkolu, zejména když doba dokončení úkolu může být delší.

### Výhody A2A

• **Zlepšená spolupráce**: Umožňuje agentům od různých dodavatelů a platforem interagovat, sdílet kontext a spolupracovat, což usnadňuje automatizaci napříč tradičně odpojenými systémy.

• **Flexibilita výběru modelu**: Každý A2A agent může rozhodnout, který LLM použije k obsluze svých požadavků, což umožňuje optimalizované nebo jemně doladěné modely pro každého agenta, na rozdíl od jediného LLM připojení v některých scénářích MCP.

• **Integrovaná autentizace**: Autentizace je přímo integrovaná do A2A protokolu, což poskytuje robustní bezpečnostní rámec pro interakce agentů.

### Příklad A2A

![A2A Diagram](../../../translated_images/A2A-Diagram.8666928d648acc2687db4093d7b09ea2a595622f8fe18194a026ee55fc23af8e.cs.png)

Rozšiřme náš scénář rezervace cestování, tentokrát pomocí A2A.

1. **Požadavek uživatele na multi-agentní systém**: Uživatel interaguje s "Cestovním agentem" A2A klientem/agentem, například tím, že řekne: "Prosím, rezervujte celý výlet do Honolulu na příští týden, včetně letů, hotelu a pronájmu auta."

2. **Orchestrace cestovním agentem**: Cestovní agent obdrží tento komplexní požadavek. Používá svůj LLM k rozpoznání úkolu a určení, že musí interagovat s dalšími specializovanými agenty.

3. **Komunikace mezi agenty**: Cestovní agent poté použije A2A protokol k připojení k downstream agentům, jako je "Agent letecké společnosti", "Agent hotelu" a "Agent pronájmu auta", které jsou vytvořeny různými společnostmi.

4. **Delegované provedení úkolu**: Cestovní agent pošle specifické úkoly těmto specializovaným agentům (například "Najdi lety do Honolulu", "Rezervuj hotel", "Pronajmi auto"). Každý z těchto specializovaných agentů, provozující své vlastní LLM a využívající své vlastní nástroje (které mohou být samy MCP servery), provede svou specifickou část rezervace.

5. **Konsolidovaná odpověď**: Jakmile všichni downstream agenti dokončí své úkoly, cestovní agent sestaví výsledky (detaily letu, potvrzení hotelu, rezervace auta) a pošle komplexní odpověď ve stylu chatu zpět uživateli.

## Natural Language Web (NLWeb)

Webové stránky dlouho sloužily jako primární způsob, jak uživatelé přistupují k informacím a datům na internetu.

Podívejme se na různé komponenty NLWeb, výhody NLWeb a příklad, jak NLWeb funguje v naší cestovní aplikaci.

### Komponenty NLWeb

- **NLWeb aplikace (základní kód služby)**: Systém, který zpracovává otázky v přirozeném jazyce. Spojuje různé části platformy, aby vytvořil odpovědi. Můžete si ho představit jako **motor, který pohání funkce přirozeného jazyka** na webu.

- **NLWeb protokol**: Jedná se o **základní sadu pravidel pro interakci v přirozeném jazyce** s webem. Odpovědi posílá ve formátu JSON (často pomocí Schema.org). Jeho účelem je vytvořit jednoduchý základ pro „AI web“, podobně jako HTML umožnil sdílení dokumentů online.

- **MCP server (Model Context Protocol Endpoint)**: Každé nastavení NLWeb také funguje jako **MCP server**. To znamená, že může **sdílet nástroje (například metodu „ask“) a data** s jinými AI systémy. V praxi to umožňuje, aby obsah a schopnosti webu byly použitelné AI agenty, což umožňuje webu stát se součástí širšího „ekosystému agentů“.

- **Modely vkládání**: Tyto modely se používají k **převodu obsahu webu na číselné reprezentace zvané vektory** (vkládání). Tyto vektory zachycují význam způsobem, který počítače mohou porovnávat a vyhledávat. Jsou uloženy ve speciální databázi a uživatelé si mohou vybrat, který model vkládání chtějí použít.

- **Vektorová databáze (mechanismus vyhledávání)**: Tato databáze **ukládá vkládání obsahu webu**. Když někdo položí otázku, NLWeb zkontroluje vektorovou databázi, aby rychle našel nejrelevantnější informace. Poskytuje rychlý seznam možných odpovědí, seřazených podle podobnosti. NLWeb pracuje s různými systémy pro ukládání vektorů, jako jsou Qdrant, Snowflake, Milvus, Azure AI Search a Elasticsearch.

### Příklad NLWeb

![NLWeb](../../../translated_images/nlweb-diagram.c1e2390b310e5fe4b245b86690ac6c49c26e355da5ab124128c8675d58cc9b07.cs.png)

Zvažme náš cestovní web, tentokrát poháněný NLWeb.

1. **Příjem dat**: Stávající katalogy produktů cestovního webu (například seznamy letů, popisy hotelů, balíčky zájezdů) jsou formátovány pomocí Schema.org nebo načteny prostřednictvím RSS feedů. Nástroje NLWeb tyto strukturované údaje načtou, vytvoří vkládání a uloží je do lokální nebo vzdálené vektorové databáze.

2. **Dotaz v přirozeném jazyce (člověk)**: Uživatel navštíví web a místo navigace v menu zadá do rozhraní chatu: "Najdi mi rodinný hotel v Honolulu s bazénem na příští týden".

3. **Zpracování NLWeb**: NLWeb aplikace obdrží tento dotaz. Pošle dotaz LLM pro porozumění a současně prohledá svou vektorovou databázi pro relevantní seznamy hotelů.

4. **Přesné výsledky**: LLM pomáhá interpretovat výsledky vyhledávání z databáze, identifikovat nejlepší shody na základě kritérií "rodinný", "bazén" a "Honolulu" a poté formátuje odpověď v přirozeném jazyce. Klíčové je, že odpověď odkazuje na skutečné hotely z katalogu webu, čímž se vyhýbá vymyšleným informacím.

5. **Interakce AI agenta**: Protože NLWeb slouží jako MCP server, externí AI cestovní agent by se mohl také připojit k NLWeb instanci tohoto webu. AI agent by mohl použít metodu `ask` MCP k přímému dotazování webu: `ask("Jsou v oblasti Honolulu nějaké veganské restaurace doporučené hotelem?")`. NLWeb instance by to zpracovala, využila svou databázi informací o restauracích (pokud je načtena) a vrátila strukturovanou JSON odpověď.

### Máte další otázky ohledně MCP/A2A/NLWeb?

Připojte se k [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), kde se můžete setkat s dalšími studenty, zúčastnit se konzultačních hodin a získat odpovědi na své otázky ohledně AI agentů.

## Zdroje

- [MCP pro začátečníky](https://aka.ms/mcp-for-beginners)  
- [MCP dokumentace](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [NLWeb Repo](https://github.com/nlweb-ai/NLWeb)
- [Semantic Kernel Guides](https://learn.microsoft.com/semantic-kernel/)

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby AI pro překlady [Co-op Translator](https://github.com/Azure/co-op-translator). Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.