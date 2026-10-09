# Používání agentních protokolů (MCP, A2A a NLWeb)

[![Agentní protokoly](../../../translated_images/cs/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Klikněte na obrázek výše pro zobrazení videa této lekce)_

S rostoucím využíváním AI agentů roste i potřeba protokolů, které zajišťují standardizaci, bezpečnost a podporu otevřené inovace. V této lekci si představíme 3 protokoly, které tuto potřebu naplňují – Model Context Protocol (MCP), Agent to Agent (A2A) a Natural Language Web (NLWeb).

## Úvod

V této lekci se zaměříme na:

• Jak **MCP** umožňuje AI agentům přístup k externím nástrojům a datům pro plnění úkolů uživatelů.

• Jak **A2A** umožňuje komunikaci a spolupráci mezi různými AI agenty.

• Jak **NLWeb** přináší přirozené jazykové rozhraní na jakoukoli webovou stránku, což umožňuje AI agentům objevovat a interagovat s jejím obsahem.

## Cíle učení

• **Identifikovat** hlavní účel a přínosy MCP, A2A a NLWeb v kontextu AI agentů.

• **Vysvětlit**, jak každý protokol usnadňuje komunikaci a interakci mezi LLM, nástroji a dalšími agenty.

• **Rozpoznat** odlišné role, které každý protokol hraje při tvorbě složitých agentních systémů.

## Model Context Protocol

**Model Context Protocol (MCP)** je otevřený standard, který poskytuje standardizovaný způsob, jak aplikace mohou poskytovat kontext a nástroje LLM. To umožňuje „univerzální adaptér“ pro různé zdroje dat a nástroje, ke kterým se AI agenti mohou připojit konzistentním způsobem.

Podívejme se na komponenty MCP, výhody oproti přímému používání API a příklad, jak mohou AI agenti používat MCP server.

### Hlavní komponenty MCP

MCP funguje na **klient-server architektuře** a hlavní komponenty jsou:

• **Hostitelé** jsou LLM aplikace (například kódovací editor jako VSCode), které zahajují připojení k MCP serveru.

• **Klienti** jsou komponenty uvnitř hostitelské aplikace, které udržují jedno-na-jedno připojení k serverům.

• **Servery** jsou lehké programy, které zpřístupňují specifické schopnosti.

Součástí protokolu jsou tři základní primitivy, což jsou schopnosti MCP serveru:

• **Nástroje**: Jsou to samostatné akce nebo funkce, které může AI agent zavolat k provedení úkolu. Například meteorologická služba může zpřístupnit nástroj „získat počasí“ nebo e-commerce server nástroj „koupit produkt“. MCP servery zveřejňují jméno, popis a vstupní/výstupní schéma každého nástroje ve svém seznamu schopností.

• **Zdroje**: Jsou to datové položky nebo dokumenty pouze pro čtení, které MCP server může poskytovat, a klienti je mohou na vyžádání získat. Příklady zahrnují obsah souborů, záznamy databází nebo log soubory. Zdroje mohou být textové (např. kód nebo JSON) nebo binární (např. obrázky nebo PDF).

• **Předvolby (Prompts)**: Jsou to předdefinované šablony, které poskytují navrhované výzvy, což umožňuje složitější pracovní toky.

### Výhody MCP

MCP nabízí významné výhody pro AI agenty:

• **Dynamické objevování nástrojů**: Agenti mohou dynamicky získat seznam dostupných nástrojů ze serveru spolu s popisy jejich funkcí. To kontrastuje s tradičními API, která často vyžadují statické programování pro integrace, což znamená, že jakákoli změna API vyžaduje úpravu kódu. MCP nabízí přístup „integrace jednou“, což vede k větší adaptabilitě.

• **Interoperabilita napříč LLM**: MCP funguje s různými LLM, poskytuje flexibilitu v přepínání modelů pro lepší výkon.

• **Standardizovaná bezpečnost**: MCP zahrnuje standardní autentizační metodu, která zlepšuje škálovatelnost při přidávání přístupu k dalším MCP serverům. To je jednodušší než správa různých klíčů a typů autentizace pro různá tradiční API.

### Příklad MCP

![MCP Diagram](../../../translated_images/cs/mcp-diagram.e4ca1cbd551444a1.webp)

Představte si, že uživatel chce rezervovat let pomocí AI asistenta založeného na MCP.

1. **Připojení**: AI asistent (MCP klient) se připojí k MCP serveru letecké společnosti.

2. **Objevování nástrojů**: Klient se zeptá MCP serveru letecké společnosti: „Jaké nástroje máte k dispozici?“ Server odpoví nástroji jako „vyhledat lety“ a „rezervovat lety“.

3. **Volání nástroje**: Poté požádáte AI asistenta: „Prosím, vyhledej let z Portlandu do Honolulu.“ AI asistent využívající svůj LLM zjistí, že musí zavolat nástroj „vyhledat lety“ a předá relevantní parametry (odlet, cíl) MCP serveru.

4. **Provedení a odpověď**: MCP server fungující jako obal provede skutečný hovor do interního rezervačního API letecké společnosti. Poté přijme informace o letu (např. ve formátu JSON) a odešle je zpět AI asistentovi.

5. **Další interakce**: AI asistent zobrazí možnosti letu. Po výběru letu může asistent zavolat nástroj „rezervovat let“ na stejném MCP serveru a dokončit rezervaci.

## Agent-to-Agent protokol (A2A)

Zatímco MCP se zaměřuje na připojení LLM k nástrojům, **Agent-to-Agent (A2A) protokol** jde o krok dále tím, že umožňuje komunikaci a spolupráci mezi různými AI agenty. A2A propojuje AI agenty napříč různými organizacemi, prostředími a technologiemi k dokončení společného úkolu.

Podíváme se na komponenty a přínosy A2A a uvedeme příklad, jak by mohl být použit v naší cestovní aplikaci.

### Hlavní komponenty A2A

A2A se soustředí na umožnění komunikace mezi agenty a jejich spolupráci při plnění dílčího úkolu uživatele. Každá komponenta protokolu k tomu přispívá:

#### Agent Card

Podobně jako MCP server sdílí seznam nástrojů, Agent Card obsahuje:
- Jméno agenta.
- **Popis obecných úkolů**, které plní.
- **Seznam specifických dovedností** s popisy, které pomáhají ostatním agentům (nebo i lidským uživatelům) pochopit, kdy a proč by měli volat daného agenta.
- **Aktuální URL koncového bodu** agenta.
- **Verzi** a **schopnosti** agenta, jako jsou streamování odpovědí a push notifikace.

#### Agent Executor

Agent Executor je zodpovědný za **předání kontextu uživatelského chatu vzdálenému agentovi**, který jej potřebuje k pochopení úkolu, který má být splněn. V A2A serveru používá agent svůj vlastní Large Language Model (LLM) k analýze příchozích požadavků a vykonání úkolů pomocí svých interních nástrojů.

#### Artifact

Jakmile vzdálený agent dokončí požadovaný úkol, vzniká jako výstup artifact. Artifact **obsahuje výsledek práce agenta**, **popis toho, co bylo dokončeno**, a **textový kontext**, který je přenášen protokolem. Po odeslání artifactu je spojení s vzdáleným agentem uzavřeno, dokud není znovu potřeba.

#### Event Queue

Tato komponenta slouží k **zpracování aktualizací a předávání zpráv**. Je obzvláště důležitá v produkci pro agentní systémy, aby se zabránilo ukončení spojení mezi agenty před dokončením úkolu, zejména když dokončení úkolů může trvat delší dobu.

### Výhody A2A

• **Vylepšená spolupráce**: Umožňuje agentům od různých dodavatelů a platforem vzájemně komunikovat, sdílet kontext a spolupracovat, což usnadňuje plynulou automatizaci napříč tradičně nespojenými systémy.

• **Flexibilita výběru modelu**: Každý A2A agent si může zvolit, který LLM používá k obsluze svých požadavků, což umožňuje optimalizované či doladěné modely pro jednotlivé agenty, na rozdíl od jednoho LLM připojení v některých MCP scénářích.

• **Integrovaná autentizace**: Autentizace je přímo integrována do A2A protokolu, což poskytuje robustní bezpečnostní rámec pro interakce agentů.

### Příklad A2A

![A2A Diagram](../../../translated_images/cs/A2A-Diagram.8666928d648acc26.webp)

Rozvineme náš scénář rezervace cestování, tentokrát však za použití A2A.

1. **Požadavek uživatele na multi-agenta**: Uživatel komunikuje s A2A klientem/agentem „Travel Agent“ například tím, že řekne: „Prosím, zarezervuj celý výlet do Honolulu na příští týden, včetně letů, hotelu a půjčení auta“.

2. **Orchestrace cestovním agentem**: Travel Agent obdrží tento složitý požadavek. Používá svůj LLM, aby zvážil úkol a určil, že musí komunikovat s dalšími specializovanými agenty.

3. **Komunikace mezi agenty**: Travel Agent pak použije A2A protokol k připojení k následným agentům, jako jsou „Airline Agent“, „Hotel Agent“ a „Car Rental Agent“, které vytvářejí různé společnosti.

4. **Delegované provádění úkolů**: Travel Agent pošle specifické úkoly těmto specializovaným agentům (např. „Najdi lety do Honolulu“, „Zarezervuj hotel“, „Půjč auto“). Každý z těchto agentů, provozující vlastní LLM a používající vlastní nástroje (které sami mohou být MCP servery), vykoná svou část rezervace.

5. **Konsolidovaná odpověď**: Po dokončení všech úkolů následnými agenty Travel Agent sestaví výsledky (detaily letu, potvrzení hotelu, rezervace auta) a zašle souhrnnou, chatovou odpověď zpět uživateli.

## Natural Language Web (NLWeb)

Webové stránky dlouhodobě představují hlavní způsob, jak uživatelé přistupují k informacím a datům na internetu.

Podívejme se na různé komponenty NLWeb, přínosy NLWeb a příklad, jak náš NLWeb funguje na naší cestovní aplikaci.

### Komponenty NLWeb

- **NLWeb aplikace (základní kód služby)**: Systém, který zpracovává přirozené jazykové dotazy. Spojuje různé části platformy pro tvorbu odpovědí. Můžete ji vnímat jako **motor, který pohání přirozené jazykové funkce** webu.

- **NLWeb protokol**: Toto je **základní sada pravidel pro přirozenou jazykovou interakci** s webem. Vrací odpovědi ve formátu JSON (často využívá Schema.org). Jeho účelem je vytvořit jednoduchý základ „AI webu“, obdobně jako HTML umožnilo sdílení dokumentů online.

- **MCP server (Model Context Protocol koncový bod)**: Každé nastavení NLWeb také funguje jako **MCP server**. To znamená, že může **sdílet nástroje (jako metodu „ask“) a data** s jinými AI systémy. V praxi to umožňuje, aby obsah a schopnosti webu byly použitelné AI agenty, což umožňuje webu stát se součástí širšího „agentního ekosystému“.

- **Embedding modely**: Tyto modely se používají k **převodu obsahu webu na číselné reprezentace nazývané vektory** (embeddingy). Tyto vektory zachycují význam způsobem, kterému mohou počítače porovnávat a vyhledávat. Ukládají se do speciální databáze a uživatelé si mohou zvolit, který embedding model chtějí využít.

- **Vektorová databáze (retrieval mechanismus)**: Tato databáze **ukládá embeddingy obsahu webových stránek**. Když někdo položí dotaz, NLWeb zkontroluje vektorovou databázi, aby rychle našel nejrelevantnější informace. Poskytne rychlý seznam možných odpovědí, seřazených podle podobnosti. NLWeb pracuje s různými systémy pro uložení vektorů, jako jsou Qdrant, Snowflake, Milvus, Azure AI Search a Elasticsearch.

### NLWeb na příkladu

![NLWeb](../../../translated_images/cs/nlweb-diagram.c1e2390b310e5fe4.webp)

Znovu si vezměme náš cestovní rezervační web, tentokrát poháněný NLWebem.

1. **Nahrání dat**: Stávající katalogy produktů na cestovním webu (např. seznamy letů, popisy hotelů, zájezdy) jsou formátovány pomocí Schema.org nebo načteny přes RSS feedy. NLWebovy nástroje zpracují tato strukturovaná data, vytvoří embeddingy a uloží je do lokální nebo vzdálené vektorové databáze.

2. **Dotaz v přirozeném jazyce (člověk)**: Uživatel navštíví web a místo procházení menu napíše do chatovacího rozhraní: „Najdi mi rodinný hotel v Honolulu s bazénem na příští týden“.

3. **Zpracování NLWebem**: NLWeb aplikace tento dotaz přijme. Odešle ho k pochopení do LLM a současně vyhledá v jeho vektorové databázi relevantní nabídky hotelů.

4. **Přesné výsledky**: LLM pomáhá interpretovat výsledky vyhledávání z databáze, identifikuje nejlepší odpovídající výsledky na základě kritérií „rodinný“, „bazén“ a „Honolulu“ a poté formátuje odpověď v přirozeném jazyce. Důležité je, že odpověď odkazuje na skutečné hotely z katalogu webu, ne na vymyšlené informace.

5. **Interakce AI agenta**: Protože NLWeb funguje jako MCP server, může se ke zdejšímu NLWebu připojit i externí AI cestovní agent. Ten může použít MCP metodu `ask` k přímému dotazu na web, například: `ask("Jsou v oblasti Honolulu veganské restaurace doporučené hotelem?")`. NLWeb tuto žádost zpracuje, využije svou databázi informací o restauracích (pokud je načtena) a vrátí strukturovanou JSON odpověď.

### Máte další otázky ohledně MCP/A2A/NLWeb?

Připojte se k [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kde potkáte další studenty, můžete navštěvovat konzultační hodiny a získat odpovědi na své otázky o AI agentech.

## Zdroje

- [MCP pro začátečníky](https://aka.ms/mcp-for-beginners)  
- [MCP dokumentace](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb repozitář](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python)

## Předchozí lekce

[AI agenti v produkci](../10-ai-agents-production/README.md)

## Následující lekce

[Context Engineering pro AI agenty](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->