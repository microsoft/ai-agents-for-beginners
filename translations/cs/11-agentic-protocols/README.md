# Používání agentních protokolů (MCP, A2A a NLWeb)

[![Agentní protokoly](../../../translated_images/cs/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Klikněte na obrázek výše pro zhlédnutí videa této lekce)_

S rostoucím využíváním AI agentů roste i potřeba protokolů, které zajišťují standardizaci, bezpečnost a podporují otevřené inovace. V této lekci pokryjeme 3 protokoly, které usilují o naplnění této potřeby - Model Context Protocol (MCP), Agent to Agent (A2A) a Natural Language Web (NLWeb).

## Úvod

V této lekci se zaměříme na:

• Jak **MCP** umožňuje AI agentům přistupovat k externím nástrojům a datům, aby dokončili úkoly uživatele.

•  Jak **A2A** umožňuje komunikaci a spolupráci mezi různými AI agenty.

• Jak **NLWeb** přináší rozhraní v přirozeném jazyce na jakoukoli webovou stránku, což umožňuje AI agentům objevovat a interagovat s obsahem.

## Vzdělávací cíle

• **Identifikovat** hlavní účel a přínosy MCP, A2A a NLWeb v kontextu AI agentů.

• **Vysvětlit**, jak každý protokol usnadňuje komunikaci a interakci mezi LLM, nástroji a dalšími agenty.

• **Rozpoznat** odlišné role, které každý protokol hraje při budování složitých agentních systémů.

## Protokol kontextu modelu

Protokol kontextu modelu (**Model Context Protocol (MCP)**) je otevřený standard, který poskytuje standardizovaný způsob, jak aplikace poskytují kontext a nástroje LLM. To umožňuje „univerzální adaptér“ k různým datovým zdrojům a nástrojům, ke kterým se AI agenti mohou připojovat konzistentním způsobem.

Pojďme se podívat na komponenty MCP, výhody ve srovnání s přímým používáním API a příklad toho, jak by AI agenti mohli používat MCP server.

### Základní komponenty MCP

MCP funguje na **klient-server architektuře** a základní komponenty jsou:

• **Hostitelé** jsou aplikace využívající LLM (například editor kódu jako VSCode), které zahajují připojení k MCP serveru.

• **Klienti** jsou komponenty v rámci hostitelské aplikace, které udržují jedno-na-jedno spojení se servery.

• **Servery** jsou lehké programy, které vystavují specifické schopnosti.

Součástí protokolu jsou tři základní primitivy, což jsou schopnosti MCP serveru:

• **Nástroje**: Jedná se o jednotlivé akce nebo funkce, které může AI agent vyvolat k provedení úkolu. Například služba počasí může vystavit nástroj „získat počasí“, nebo e‑commerce server může vystavit nástroj „koupit produkt“. MCP servery inzerují název každého nástroje, popis a vstupní/výstupní schéma ve výpisu svých schopností.

• **Zdroje**: Jedná se o datové položky nebo dokumenty pouze pro čtení, které MCP server může poskytnout, a které si klienti mohou vyžádat na vyžádání. Příklady zahrnují obsah souborů, záznamy v databázi nebo log soubory. Zdroje mohou být textové (např. kód nebo JSON) nebo binární (např. obrázky nebo PDF).

• **Prompty**: Jsou to předdefinované šablony, které poskytují navrhované výzvy, umožňující složitější pracovní postupy.

### Výhody MCP

MCP nabízí významné výhody pro AI agenty:

• **Dynamické objevování nástrojů**: Agenti mohou dynamicky obdržet seznam dostupných nástrojů ze serveru spolu s popisy toho, co dělají. To kontrastuje s tradičními API, která často vyžadují statické kódování integrací, což znamená, že jakákoli změna API vyžaduje aktualizace kódu. MCP nabízí přístup „integrovat jednou“, což vede k větší přizpůsobivosti.

• **Interoperabilita napříč LLM**: MCP funguje napříč různými LLM, poskytuje flexibilitu přepínat základní modely za účelem lepšího výkonu.

• **Standardizovaná bezpečnost**: MCP zahrnuje standardní metodu autentizace, což zlepšuje škálovatelnost při přidávání přístupu k dalším MCP serverům. To je jednodušší než správa různých klíčů a typů autentizace pro různá tradiční API.

### Příklad MCP

![Diagram MCP](../../../translated_images/cs/mcp-diagram.e4ca1cbd551444a1.webp)

Představte si, že uživatel chce rezervovat let pomocí AI asistenta poháněného MCP.

1. **Připojení**: AI asistent (MCP klient) se připojí k MCP serveru poskytovanému leteckou společností.

2. **Objevování nástrojů**: Klient se zeptá MCP serveru letecké společnosti: „Jaké nástroje máte k dispozici?“ Server odpoví nástroji jako „vyhledat lety“ a „rezervovat lety“.

3. **Volání nástroje**: Pak požádáte AI asistenta: „Prosím, najdi let z Portlandu do Honolulu.“ AI asistent, používající svůj LLM, identifikuje, že potřebuje zavolat nástroj „vyhledat lety“ a předá relevantní parametry (odletové místo, cíl) MCP serveru.

4. **Provedení a odpověď**: MCP server, fungující jako obal, provede skutečné volání na interní rezervační API letecké společnosti. Poté obdrží informace o letech (např. JSON data) a pošle je zpět AI asistentovi.

5. **Další interakce**: AI asistent zobrazí možnosti letů. Jakmile vyberete let, asistent může zavolat nástroj „rezervovat let“ na tomtéž MCP serveru a dokončit rezervaci.

## Protokol agent‑k agentovi (A2A)

Zatímco MCP se zaměřuje na propojení LLM s nástroji, protokol **Agent-to-Agent (A2A)** jde o krok dál tím, že umožňuje komunikaci a spolupráci mezi různými AI agenty. A2A spojuje AI agenty napříč různými organizacemi, prostředími a technologickými zásobníky, aby společně dokončili sdílený úkol.

Prozkoumáme komponenty a výhody A2A spolu s příkladem, jak by mohl být uplatněn v naší cestovní aplikaci.

### Základní komponenty A2A

A2A se soustředí na umožnění komunikace mezi agenti a jejich spolupráci na dokončení dílčího úkolu uživatele. Každá komponenta protokolu k tomu přispívá:

#### Karta agenta

Podobně jako MCP server sdílí seznam nástrojů, Karta agenta obsahuje:
- Název agenta.
- **popis obecných úkolů**, které plní.
- **seznam specifických dovedností** s popisy, které pomohou dalším agentům (nebo i lidským uživatelům) pochopit, kdy a proč by měli tohoto agenta volat.
- **aktuální Endpoint URL** agenta
- **verzi** a **schopnosti** agenta, jako jsou streamované odpovědi a push notifikace.

#### Executor agenta

Executor agenta je zodpovědný za **předání kontextu uživatelského chatu vzdálenému agentovi**, vzdálený agent to potřebuje, aby pochopil úkol, který je třeba dokončit. V A2A serveru agent používá svůj vlastní Large Language Model (LLM) k parsování příchozích požadavků a vykonávání úkolů pomocí svých interních nástrojů.

#### Artefakt

Jakmile vzdálený agent dokončí požadovaný úkol, jeho výstup je vytvořen jako artefakt. Artefakt **obsahuje výsledek práce agenta**, **popis toho, co bylo dokončeno**, a **textový kontext**, který je protokolem posílán. Po odeslání artefaktu je spojení se vzdáleným agentem uzavřeno až do další potřeby.

#### Fronta událostí

Tato komponenta se používá pro **zpracování aktualizací a předávání zpráv**. Je zvláště důležitá v produkci pro agentní systémy, aby se zabránilo uzavření spojení mezi agenty dříve, než je úkol dokončen, obzvláště když dokončení úkolu může trvat delší dobu.

### Výhody A2A

• **Vylepšená spolupráce**: Umožňuje agentům od různých poskytovatelů a platforem interagovat, sdílet kontext a spolupracovat, což usnadňuje bezproblémovou automatizaci napříč tradičně oddělenými systémy.

• **Flexibilita výběru modelu**: Každý A2A agent si může zvolit, který LLM používá k obsluze svých požadavků, což umožňuje optimalizované nebo doladěné modely pro jednotlivé agenty, na rozdíl od jediného LLM připojení v některých MCP scénářích.

• **Vestavěná autentizace**: Autentizace je integrována přímo v A2A protokolu, poskytující robustní bezpečnostní rámec pro interakce agentů.

### Příklad A2A

![Diagram A2A](../../../translated_images/cs/A2A-Diagram.8666928d648acc26.webp)

Rozeberme náš scénář rezervace cestování, tentokrát s využitím A2A.

1. **Uživatelský požadavek na multi-agenta**: Uživatel komunikuje s „Cestovním agentem“ A2A klientem/agente, například: „Prosím, rezervuj celou cestu do Honolulu na příští týden, včetně letů, hotelu a půjčovny auta.“

2. **Orchestrace Cestovním agentem**: Cestovní agent obdrží tento složitý požadavek. Použije svůj LLM k rozmyšlení úkolu a určí, že potřebuje komunikovat s jinými specializovanými agenty.

3. **Meziagentní komunikace**: Cestovní agent poté použije A2A protokol k připojení k downstream agentům, jako jsou „Agent letecké společnosti“, „Agent hotelu“ a „Agent půjčoven aut“, které vytvořily různé společnosti.

4. **Delegované vykonání úkolu**: Cestovní agent pošle specifické úkoly těmto specializovaným agentům (např. „Najděte lety do Honolulu,“ „Rezervujte hotel,“ „Půjčte auto“). Každý z těchto specializovaných agentů, provozující své vlastní LLM a využívající své nástroje (které sami mohou být MCP servery), provede svou část rezervace.

5. **Konsolidovaná odpověď**: Jakmile všichni downstream agenti dokončí své úkoly, Cestovní agent sestaví výsledky (detaily letu, potvrzení hotelu, rezervaci auta) a pošle uživateli komplexní odpověď ve formě chatu.

## Web v přirozeném jazyce (NLWeb)

Webové stránky dlouho byly hlavním způsobem, jak uživatelé přistupují k informacím a datům na internetu.

Podívejme se na různé komponenty NLWeb, výhody NLWeb a příklad, jak náš NLWeb funguje na příkladu naší cestovní aplikace.

### Komponenty NLWeb

- **Aplikace NLWeb (jádro služby)**: Systém, který zpracovává otázky v přirozeném jazyce. Spojuje různé části platformy pro tvorbu odpovědí. Můžete si ji představit jako **motor, který pohání funkce v přirozeném jazyce** na webu.

- **Protokol NLWeb**: Jedná se o **základní sadu pravidel pro interakci v přirozeném jazyce** s webovou stránkou. Vrací odpovědi v JSON formátu (často s využitím Schema.org). Jeho cílem je vytvořit jednoduchý základ pro „AI web“, podobně jako HTML umožnilo sdílení dokumentů online.

- **MCP server (konečný bod Model Context Protocol)**: Každé nastavení NLWeb také funguje jako **MCP server**. To znamená, že může **sdílet nástroje (jako metodu „ask“) a data** s jinými AI systémy. V praxi to umožňuje, aby obsah a schopnosti webu byly použitelné AI agenty, což umožňuje webu stát se součástí širší „ekosystému agentů“.

- **Modely pro embeddingy**: Tyto modely se používají k **převodu obsahu webu na číselné reprezentace zvané vektory** (embeddingy). Tyto vektory zachycují význam způsobem, který mohou počítače porovnávat a prohledávat. Jsou uloženy ve speciální databázi a uživatelé si mohou vybrat, který embedding model chtějí použít.

- **Vektorová databáze (mechanismus pro vyhledávání)**: Tato databáze **ukládá embeddingy obsahu webu**. Když někdo položí otázku, NLWeb zkontroluje vektorovou databázi, aby rychle nalezl nejrelevantnější informace. Poskytne rychlý seznam možných odpovědí, řazených podle podobnosti. NLWeb pracuje s různými systémy pro ukládání vektorů jako Qdrant, Snowflake, Milvus, Azure AI Search a Elasticsearch.

### NLWeb na příkladu

![NLWeb](../../../translated_images/cs/nlweb-diagram.c1e2390b310e5fe4.webp)

Zvažme znovu náš web pro rezervaci cestování, tentokrát poháněný NLWeb.

1. **Ingestace dat**: Existující produktové katalogy cestovního webu (např. seznamy letů, popisy hotelů, nabídky zájezdů) jsou formátovány pomocí Schema.org nebo načteny přes RSS feedy. Nástroje NLWeb tyto strukturované údaje ingestují, vytvářejí embeddingy a ukládají je do lokální nebo vzdálené vektorové databáze.

2. **Dotaz v přirozeném jazyce (člověk)**: Uživatel navštíví web a místo procházení menu napíše do chatovacího rozhraní: "Najděte mi rodinně přátelský hotel v Honolulu s bazénem na příští týden".

3. **Zpracování NLWeb**: Aplikace NLWeb obdrží tento dotaz. Pošle dotaz do LLM pro porozumění a současně prohledá svou vektorovou databázi pro relevantní záznamy o hotelech.

4. **Přesné výsledky**: LLM pomáhá interpretovat výsledky hledání z databáze, identifikovat nejlepší shody na základě kritérií „rodinně přátelský“, „bazén“ a „Honolulu“, a poté formátuje odpověď v přirozeném jazyce. Důležité je, že odpověď odkazuje na skutečné hotely z katalogu webu, čímž se vyhýbá vymyšleným informacím.

5. **Interakce AI agenta**: Protože NLWeb slouží jako MCP server, externí AI cestovní agent se může také připojit k instanci NLWeb tohoto webu. AI agent pak může použít `ask` MCP metodu k dotazu na web přímo: `ask("Are there any vegan-friendly restaurants in the Honolulu area recommended by the hotel?")`. Instance NLWeb to zpracuje, využije svou databázi informací o restauracích (pokud jsou načteny) a vrátí strukturovanou JSON odpověď.

### Máte další otázky ohledně MCP/A2A/NLWeb?

Připojte se k [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) a setkejte se s ostatními studenty, navštěvujte konzultační hodiny a nechte si zodpovědět své dotazy ohledně AI agentů.

## Zdroje

- [MCP pro začátečníky](https://aka.ms/mcp-for-beginners)  
- [Dokumentace MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Repozitář NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framewrok)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Prohlášení o vyloučení odpovědnosti:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, vezměte prosím na vědomí, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za rozhodující zdroj. Pro zásadní informace doporučujeme využít profesionální lidský překlad. Nepřebíráme odpovědnost za jakákoli nedorozumění nebo chybné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->