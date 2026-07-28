# Použití agentních protokolů (MCP, A2A a NLWeb)

[![Agentní protokoly](../../../translated_images/cs/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Klikněte na obrázek výše pro zobrazení videa této lekce)_

Jak roste využívání AI agentů, roste i potřeba protokolů, které zajistí standardizaci, bezpečnost a podpoří otevřenou inovaci. V této lekci pokryjeme 3 protokoly, které mají tento požadavek uspokojit – Model Context Protocol (MCP), Agent to Agent (A2A) a Natural Language Web (NLWeb).

## Úvod

V této lekci se zaměříme na:

• Jak **MCP** umožňuje AI Agentům přístup k externím nástrojům a datům pro dokončení uživatelských úkolů.

• Jak **A2A** umožňuje komunikaci a spolupráci mezi různými AI agenty.

• Jak **NLWeb** přináší přirozené jazykové rozhraní na jakoukoli webovou stránku, což umožňuje AI Agentům objevovat a interagovat s obsahem.

## Cíle učení

• **Identifikovat** hlavní účel a výhody MCP, A2A a NLWeb v kontextu AI agentů.

• **Vysvětlit**, jak každý protokol usnadňuje komunikaci a interakci mezi LLM, nástroji a dalšími agenty.

• **Rozpoznat** odlišné role každého protokolu při budování složitých agentních systémů.

## Model Context Protocol

**Model Context Protocol (MCP)** je otevřený standard, který poskytuje standardizovaný způsob, jak aplikace mohou poskytovat kontext a nástroje LLM. Umožňuje tak "univerzální adaptér" na různé zdroje dat a nástroje, ke kterým se AI Agent může připojit konzistentním způsobem.

Pojďme se podívat na složky MCP, výhody oproti přímému použití API a příklad, jak by AI agenti mohli používat MCP server.

### Hlavní složky MCP

MCP funguje na **klient-server architektuře** a hlavní složky jsou:

• **Hostitelé** jsou LLM aplikace (například editor kódu jako VSCode), které zahajují spojení s MCP serverem.

• **Klienti** jsou komponenty v rámci hostitelské aplikace, které udržují spojení jeden na jednoho se servery.

• **Servery** jsou lehké programy, které vystavují specifické schopnosti.

Protokol obsahuje tři základní primitivy, které představují schopnosti MCP serveru:

• **Nástroje**: Jde o jednotlivé akce nebo funkce, které může AI agent vyvolat k provedení úkolu. Například počasí může vystavit nástroj "získat počasí", nebo e-commerce server nástroj "zakoupit produkt". MCP servery inzerují název, popis a schéma vstupu/výstupu každého nástroje ve svém seznamu schopností.

• **Zdroje**: Jsou to data nebo dokumenty pouze pro čtení, které MCP server může poskytovat a klienti si je mohou načíst na požádání. Příklady zahrnují obsah souborů, databázové záznamy nebo soubory protokolů. Zdroje mohou být textové (jako kód nebo JSON) nebo binární (jako obrázky nebo PDF).

• **Výzvy (Prompts)**: Jsou to předdefinované šablony, které poskytují navrhované výzvy, umožňující složitější pracovní postupy.

### Výhody MCP

MCP nabízí významné výhody pro AI agenty:

• **Dynamické objevování nástrojů**: Agenti mohou dynamicky obdržet seznam dostupných nástrojů od serveru spolu s popisy jejich funkcí. Na rozdíl od tradičních API, která často vyžadují statické kódování integrací, což znamená, že jakákoli změna API vyžaduje aktualizaci kódu. MCP nabízí přístup "integruj jednou", což vede k větší přizpůsobivosti.

• **Interoperabilita napříč LLM**: MCP funguje napříč různými LLM, poskytuje flexibilitu přepínat hlavní modely za účelem lepšího výkonu.

• **Standardizovaná bezpečnost**: MCP obsahuje standardní metodu autentifikace, což zlepšuje škálovatelnost při přidávání přístupu k dalším MCP serverům. To je jednodušší než spravovat různé klíče a typy autentifikace pro různá tradiční API.

### Příklad MCP

![Diagram MCP](../../../translated_images/cs/mcp-diagram.e4ca1cbd551444a1.webp)

Představme si uživatele, který chce rezervovat let pomocí AI asistenta postaveného na MCP.

1. **Připojení**: AI asistent (MCP klient) se připojí k MCP serveru poskytovanému leteckou společností.

2. **Objevování nástrojů**: Klient se zeptá MCP serveru aerolinek: „Jaké nástroje máte k dispozici?“ Server odpoví nástroji jako „vyhledat lety“ a „rezervovat lety“.

3. **Volání nástroje**: Poté požádáte AI asistenta: „Vyhledej prosím let z Portlandu do Honolulu.“ AI asistent s využitím LLM identifikuje, že musí zavolat nástroj „vyhledat lety“ a předá relevantní parametry (odlet, cílové místo) MCP serveru.

4. **Vykonání a odpověď**: MCP server, fungující jako obal, provede skutečné volání interního rezervačního API aerolinek. Poté obdrží informace o letu (např. JSON data) a pošle je zpět AI asistentovi.

5. **Další interakce**: AI asistent představí možnosti letu. Jakmile vyberete let, asistent může vyvolat nástroj „rezervovat let“ na stejném MCP serveru a dokončit rezervaci.

## Agent-to-Agent protokol (A2A)

Zatímco MCP se soustředí na propojení LLM s nástroji, **Agent-to-Agent (A2A) protokol** jde o krok dál tím, že umožňuje komunikaci a spolupráci mezi různými AI agenty. A2A propojuje AI agenty napříč různými organizacemi, prostředími a technologiemi za účelem dokončení sdíleného úkolu.

Podíváme se na složky a výhody A2A a také na příklad, jak by mohl být použit v naší cestovní aplikaci.

### Hlavní složky A2A

A2A se zaměřuje na umožnění komunikace mezi agenty a jejich spolupráci na dokončení části uživatelova úkolu. Každá složka protokolu k tomu přispívá:

#### Agentní karta

Podobně jako MCP server sdílí seznam nástrojů, agentní karta obsahuje:
- Jméno agenta.
- **popis obecných úkolů**, které plní.
- **seznam specifických dovedností** s popisy, které pomáhají ostatním agentům (nebo i lidským uživatelům) pochopit, kdy a proč by měli daného agenta volat.
- **aktuální URL koncového bodu** agenta.
- **verzi** a **schopnosti** agenta, například streamované odpovědi a push notifikace.

#### Prováděč agenta (Agent Executor)

Prováděč agenta je odpovědný za **předání kontextu uživatelského chatu vzdálenému agentovi**, vzdálený agent to potřebuje, aby pochopil úkol, který má dokončit. V A2A serveru agent používá svůj vlastní velký jazykový model (LLM) k analýze příchozích požadavků a vykonání úkolů za pomoci svých interních nástrojů.

#### Artefakt

Jakmile vzdálený agent dokončí požadovaný úkol, jeho pracovní výsledek je vytvořen jako artefakt. Artefakt **obsahuje výsledek agentovy práce**, **popis toho, co bylo dokončeno**, a **textový kontext**, který je předán protokolem. Po odeslání artefaktu je spojení s vzdáleným agentem ukončeno, dokud není znovu potřeba.

#### Fronta událostí (Event Queue)

Tato složka se používá k **zpracování aktualizací a předávání zpráv**. Je zvláště důležitá ve výrobním prostředí pro agentní systémy, aby se zabránilo předčasnému ukončení spojení mezi agenty před dokončením úkolu, zvláště když může dokončení úkolu trvat déle.

### Výhody A2A

• **Vylepšená spolupráce**: Umožňuje agentům od různých dodavatelů a platforem komunikovat, sdílet kontext a spolupracovat, čímž zajišťuje plynulou automatizaci napříč tradičně oddělenými systémy.

• **Flexibilita výběru modelu**: Každý A2A agent si může zvolit, který LLM používá k obsluze svých požadavků, což umožňuje optimalizaci či ladění modelů na agenta, na rozdíl od jednoho LLM připojení v některých scénářích MCP.

• **Vestavěná autentifikace**: Autentifikace je integrována přímo do A2A protokolu, což poskytuje robustní bezpečnostní rámec pro interakce agentů.

### Příklad A2A

![Diagram A2A](../../../translated_images/cs/A2A-Diagram.8666928d648acc26.webp)

Rozšíříme náš scénář rezervace cestování, tentokrát však s použitím A2A.

1. **Uživatelský požadavek na multi-agenta**: Uživatel komunikuje s „Cestovním agentem“, A2A klientem/agentem, například řekne: „Prosím, rezervuj celou cestu do Honolulu na příští týden, včetně letů, hotelu a půjčení auta.“

2. **Orchestrace Cestovního agenta**: Cestovní agent přijme tento složitý požadavek. Použije svůj LLM k rozmyšlení úkolu a určí, že musí komunikovat s dalšími specializovanými agenty.

3. **Meziagentní komunikace**: Cestovní agent pak využije A2A protokol k připojení k podřízeným agentům, jako je „Agent aerolinek“, „Hotelový agent“ a „Agent půjčovny aut“, které jsou vytvořeny různými společnosti.

4. **Delegované vykonání úkolů**: Cestovní agent posílá specifické úkoly těmto specializovaným agentům (např. „Najdi lety do Honolulu“, „Rezervuj hotel“, „Půjč auto“). Každý z těchto specializovaných agentů, který provozuje svůj vlastní LLM a využívá své nástroje (které mohou být samotné MCP servery), vykoná svoji část rezervace.

5. **Konsolidovaná odpověď**: Jakmile všichni podřízení agenti dokončí úkoly, Cestovní agent sestaví výsledky (detaily letu, potvrzení hotelu, rezervaci auta) a pošle komplexní odpověď ve stylu chatu zpět uživateli.

## Natural Language Web (NLWeb)

Webové stránky byly dlouho primárním způsobem, jak uživatelé přistupují k informacím a datům na internetu.

Podívejme se na různé složky NLWeb, výhody NLWeb a příklad, jak náš NLWeb funguje na příkladu naší cestovní aplikace.

### Složky NLWeb

- **NLWeb aplikace (základní kód služby)**: Systém, který zpracovává otázky v přirozeném jazyce. Spojuje různé části platformy pro vytváření odpovědí. Můžete to vnímat jako **motor, který pohání funkce přirozeného jazyka** na webu.

- **NLWeb protokol**: Toto je **základní soubor pravidel pro interakci v přirozeném jazyce** s webovou stránkou. Vrací odpovědi ve formátu JSON (často s použitím Schema.org). Jeho účelem je vytvořit jednoduchý základ pro „AI Web“, podobně jako HTML umožnilo sdílení dokumentů online.

- **MCP server (Model Context Protocol Endpoint)**: Každé nastavení NLWeb funguje také jako **MCP server**. To znamená, že může **sdílet nástroje (například metodu „ask“) a data** s jinými AI systémy. V praxi to umožňuje, aby obsah a schopnosti webu byly použitelné AI agenty, čímž se stránka stává součástí širší „agentní ekosystému“.

- **Vkládací modely (Embedding Models)**: Tyto modely se používají k **převodu obsahu webu na číselné reprezentace zvané vektory** (embeddingy). Tyto vektory zachycují význam způsobem, který počítače mohou porovnávat a vyhledávat. Jsou uloženy ve speciální databázi a uživatelé si mohou vybrat, který embedding model chtějí použít.

- **Vektorová databáze (Retrieval Mechanism)**: Tato databáze **ukládá embeddingy obsahu webu**. Když někdo položí otázku, NLWeb prohledá vektorovou databázi, aby rychle našel nejrelevantnější informace. Poskytuje rychlý seznam možných odpovědí řazených podle podobnosti. NLWeb pracuje s různými systémy pro ukládání vektorů, jako jsou Qdrant, Snowflake, Milvus, Azure AI Search a Elasticsearch.

### NLWeb na příkladu

![NLWeb](../../../translated_images/cs/nlweb-diagram.c1e2390b310e5fe4.webp)

Připomeňme si naši cestovní rezervační webovou stránku, tentokrát však poháněnou NLWeb.

1. **Vstup dat**: Existující katalogy produktů na webu (např. seznamy letů, popisy hotelů, balíčky zájezdů) jsou formátovány pomocí Schema.org nebo načítány přes RSS kanály. Nástroje NLWeb tyto strukturované data zpracují, vytvoří embeddingy a uloží je do lokální či vzdálené vektorové databáze.

2. **Dotaz v přirozeném jazyce (člověk)**: Uživatel navštíví web a místo procházení menu napíše do chatu: „Najdi mi rodinný hotel v Honolulu s bazénem na příští týden.“

3. **Zpracování NLWeb**: Aplikace NLWeb přijme tento dotaz. Pošle dotaz LLM k pochopení a zároveň prohledává svou vektorovou databázi pro relevantní nabídky hotelů.

4. **Přesné výsledky**: LLM pomůže interpretovat výsledky hledání z databáze, identifikovat nejlepší shody podle kritérií „rodinný“, „bazén“ a „Honolulu“ a poté vytvoří odpověď v přirozeném jazyce. Zásadní je, že odpověď odkazuje na skutečné hotely z katalogu webu, čímž se vyhne vymyšleným informacím.

5. **Interakce AI agenta**: Protože NLWeb funguje jako MCP server, může se externí AI cestovní agent také připojit k NLWeb instanci tohoto webu. AI agent pak může použít metodu `ask` MCP k přímému dotazování webu: `ask("Jsou v oblasti Honolulu nějaké vegansky přátelské restaurace doporučené hotelem?")`. NLWeb zpracuje tento dotaz, využije svou databázi informací o restauracích (pokud jsou načteny) a vrátí strukturovanou JSON odpověď.

### Máte další otázky ohledně MCP/A2A/NLWeb?

Připojte se na [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kde se můžete setkat s ostatními studenty, zúčastnit úředních hodin a získat odpovědi na své otázky ohledně AI agentů.

## Zdroje

- [MCP pro začátečníky](https://aka.ms/mcp-for-beginners)  
- [Dokumentace MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Repositář NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framework)

## Předchozí lekce

[AI agenti ve výrobě](../10-ai-agents-production/README.md)

## Další lekce

[Inženýrství kontextu pro AI agenty](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->