# Používání agentních protokolů (MCP, A2A a NLWeb)

[![Agentní protokoly](../../../translated_images/cs/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Klikněte na obrázek výše pro zobrazení videa této lekce)_

Jak roste používání AI agentů, roste i potřeba protokolů, které zajistí standardizaci, bezpečnost a podporu otevřené inovace. V této lekci se budeme věnovat 3 protokolům, které se snaží tuto potřebu naplnit – Model Context Protocol (MCP), Agent to Agent (A2A) a Natural Language Web (NLWeb).

## Úvod

V této lekci pokryjeme:

• Jak **MCP** umožňuje AI agentům přístup k externím nástrojům a datům pro dokončení uživatelských úkolů.

• Jak **A2A** umožňuje komunikaci a spolupráci mezi různými AI agenty.

• Jak **NLWeb** přináší přirozené jazykové rozhraní na jakoukoli webovou stránku, což umožňuje AI agentům objevovat a interagovat s obsahem.

## Cíle učení

• **Identifikovat** hlavní účel a přínosy MCP, A2A a NLWeb v kontextu AI agentů.

• **Vysvětlit**, jak každý protokol usnadňuje komunikaci a interakci mezi LLM, nástroji a dalšími agenty.

• **Rozpoznat** odlišné role, které každý protokol hraje při budování složitých agentních systémů.

## Model Context Protocol

**Model Context Protocol (MCP)** je otevřený standard, který poskytuje standardizovaný způsob, jak aplikace mohou poskytovat kontext a nástroje LLM. To umožňuje „univerzální adaptér“ k různým zdrojům dat a nástrojům, ke kterým se AI agenti mohou připojit konzistentním způsobem.

Pojďme se podívat na součásti MCP, výhody oproti přímému použití API a příklad toho, jak by AI agenti mohli používat MCP server.

### Základní komponenty MCP

MCP funguje na **klient-serverové architektuře** a základní komponenty jsou:

• **Hostitelé** jsou aplikace LLM (například editor kódu jako VSCode), které zahajují připojení k MCP serveru.

• **Klienti** jsou komponenty v rámci hostitelské aplikace, které udržují jedinečná spojení se servery.

• **Servery** jsou lehké programy, které vystavují specifické schopnosti.

Protokol zahrnuje tři základní primitiva, což jsou schopnosti MCP serveru:

• **Nástroje**: Jsou to samostatné akce nebo funkce, které může AI agent volat k provedení určité akce. Například služba počasí může vystavit nástroj „získat počasí“ nebo e-commerce server může vystavit nástroj „zakoupit produkt“. MCP servery zveřejňují jména nástrojů, popisy a vstupní/výstupní schémata ve svém seznamu schopností.

• **Zdroje**: Jsou to datové položky nebo dokumenty pouze pro čtení, které může MCP server poskytovat a klienti je mohou získat na vyžádání. Příklady zahrnují obsah souborů, záznamy v databázi nebo logovací soubory. Zdroje mohou být textové (například kód nebo JSON) nebo binární (například obrázky nebo PDF).

• **Výzvy**: Jsou to předdefinované šablony, které poskytují doporučené výzvy, umožňující složitější pracovní postupy.

### Výhody MCP

MCP nabízí významné výhody pro AI agenty:

• **Dynamické objevování nástrojů**: Agenti mohou dynamicky získat seznam dostupných nástrojů od serveru spolu s popisy jejich funkcí. To je oproti tradičním API, která často vyžadují statické kódování integrací, protože jakákoli změna API vyžaduje aktualizaci kódu. MCP nabízí přístup „integrovat jednou“, což vede k lepší přizpůsobivosti.

• **Kompatibilita napříč LLM**: MCP funguje napříč různými LLM, což poskytuje flexibilitu při přepínání základních modelů pro lepší výkon.

• **Standardizovaná bezpečnost**: MCP obsahuje standardní metodu autentizace, která zlepšuje škálovatelnost při přidávání přístupu k dalším MCP serverům. Je to jednodušší než správa různých klíčů a typů autentizace u tradičních API.

### Příklad MCP

![MCP Diagram](../../../translated_images/cs/mcp-diagram.e4ca1cbd551444a1.webp)

Představme si uživatele, který chce rezervovat let pomocí AI asistenta poháněného MCP.

1. **Připojení**: AI asistent (MCP klient) se připojí k MCP serveru poskytovanému leteckou společností.

2. **Objevování nástrojů**: Klient se zeptá MCP serveru letecké společnosti: „Jaké nástroje máte k dispozici?“ Server odpoví nástroji jako „vyhledat lety“ a „rezervovat lety“.

3. **Volání nástroje**: Poté požádáte AI asistenta: „Prosím, vyhledej let z Portlandu do Honolulu.“ AI asistent, využívající svůj LLM, určí, že musí zavolat nástroj „vyhledat lety“ a předá relevantní parametry (odlet, cílové místo) MCP serveru.

4. **Provedení a odpověď**: MCP server, fungující jako obal, provede skutečné volání interního rezervačního API letecké společnosti. Obdrží informace o letu (například v JSON formátu) a odešle je zpět AI asistentovi.

5. **Další interakce**: AI asistent zobrazí možnosti letu. Jakmile si vyberete let, asistent může zavolat nástroj „rezervovat let“ na stejném MCP serveru a dokončit rezervaci.

## Protokol Agent-to-Agent (A2A)

Zatímco MCP se zaměřuje na propojení LLM s nástroji, **protokol Agent-to-Agent (A2A)** jde o krok dál a umožňuje komunikaci a spolupráci mezi různými AI agenty. A2A propojuje AI agenty napříč organizacemi, prostředími a technologickými zásobníky, aby mohli společně plnit úkol.

Podíváme se na komponenty a výhody A2A spolu s příkladem, jak by mohl být použit v naší cestovní aplikaci.

### Základní komponenty A2A

A2A se zaměřuje na umožnění komunikace mezi agenty a jejich spolupráci při plnění dílčího uživatelského úkolu. Každá komponenta protokolu k tomu přispívá:

#### Agentní karta

Podobně jako MCP server sdílí seznam nástrojů, Agentní karta obsahuje:
- Jméno agenta.
- **Popis obecných úkolů**, které plní.
- **Seznam specifických dovedností** s popisy, které pomáhají ostatním agentům (nebo dokonce lidským uživatelům) pochopit, kdy a proč by daného agenta volali.
- **Aktuální URL koncového bodu** agenta.
- **Verzi** a **schopnosti** agenta, například streamování odpovědí a push notifikace.

#### Agentní vykonavatel

Agentní vykonavatel je zodpovědný za **předání kontextu uživatelského rozhovoru vzdálenému agentovi**, který tento kontext potřebuje, aby pochopil úkol, který má být splněn. V A2A serveru agent používá svůj vlastní LLM k analýze přicházejících požadavků a vykonává úkoly pomocí svých interních nástrojů.

#### Artefakt

Poté, co vzdálený agent dokončí požadovaný úkol, vytvoří svůj výstup jako artefakt. Artefakt **obsahuje výsledek práce agenta**, **popis toho, co bylo dokončeno**, a **textový kontext**, který je přenášen protokolem. Po odeslání artefaktu je spojení s vzdáleným agentem uzavřeno, dokud není opět potřeba.

#### Fronta událostí

Tato komponenta je používána pro **zpracování aktualizací a předávání zpráv**. V produkčních agentních systémech je obzvlášť důležitá, aby zajistila, že spojení mezi agenty nebude uzavřeno před dokončením úkolu, zvláště když dokončení úkolu může trvat delší dobu.

### Výhody A2A

• **Vylepšená spolupráce**: Umožňuje agentům z různých dodavatelů a platforem vzájemně komunikovat, sdílet kontext a spolupracovat, což usnadňuje bezproblémovou automatizaci mezi jinak oddělenými systémy.

• **Flexibilita výběru modelu**: Každý A2A agent si může zvolit, který LLM použije k obsluze svých požadavků, což umožňuje optimalizované nebo jemně laděné modely pro jednotlivé agenty, na rozdíl od jediného LLM připojení v některých scénářích MCP.

• **Vestavěná autentizace**: Autentizace je integrována přímo do A2A protokolu, čímž poskytuje robustní bezpečnostní rámec pro interakce mezi agenty.

### Příklad A2A

![A2A Diagram](../../../translated_images/cs/A2A-Diagram.8666928d648acc26.webp)

Rozšíříme náš scénář s rezervací cestování, tentokrát však s využitím A2A.

1. **Uživatelský požadavek na multi-agenta**: Uživatel komunikuje s A2A klientem/agenta nazvaným „Travel Agent“ například slovy: „Prosím, rezervuj celý výlet do Honolulu na příští týden, včetně letů, hotelu a půjčení auta.“

2. **Orchestrace cestovním agentem**: Travel Agent přijme tento složitý požadavek. Používá svůj LLM k rozmyšlení úkolu a určí, že musí komunikovat s dalšími specializovanými agenty.

3. **Mezi-agentní komunikace**: Travel Agent poté použije A2A protokol k navázání spojení s následujícími agenty, jako je „Airline Agent“, „Hotel Agent“ a „Car Rental Agent“, které jsou vytvořeny různými firmami.

4. **Delegované vykonání úkolu**: Travel Agent pošle specifické úkoly těmto specializovaným agentům (například „Najdi lety do Honolulu“, „Rezervuj hotel“, „Půjč auto“). Každý z těchto agentů, používajících vlastní LLM a své vlastní nástroje (které mohou být sami MCP servery), vykonává svou část rezervace.

5. **Konsolidovaná odpověď**: Jakmile všichni následující agenti dokončí své úkoly, Travel Agent sestaví výsledky (detaily letu, potvrzení hotelu, rezervaci auta) a pošle komplexní odpověď ve stylu chatu zpět uživateli.

## Natural Language Web (NLWeb)

Webové stránky byly dlouho hlavním způsobem, jak uživatelé přistupují k informacím a datům na internetu.

Pojďme se podívat na různé komponenty NLWeb, výhody NLWeb a příklad, jak NLWeb funguje na naší cestovní aplikaci.

### Komponenty NLWeb

- **NLWeb aplikace (základní kód služby)**: Systém, který zpracovává otázky v přirozeném jazyce. Spojuje různé části platformy pro vytváření odpovědí. Můžete ji vnímat jako **motor, který pohání funkce přirozeného jazyka** na webu.

- **NLWeb protokol**: Jedná se o **základní sadu pravidel pro interakci v přirozeném jazyce** s webovou stránkou. Odpovědi odesílá ve formátu JSON (často s použitím Schema.org). Jeho účelem je vytvořit jednoduchý základ pro „AI web“, podobně jako HTML umožnilo sdílení dokumentů online.

- **MCP server (koncový bod Model Context Protocolu)**: Každé nastavení NLWeb také funguje jako **MCP server**. To znamená, že může **sdílet nástroje (například metodu „ask“) a data** s jinými AI systémy. V praxi to umožňuje využít obsah a schopnosti webu AI agenty, čímž se web stává součástí širší „agentní ekosystému“.

- **Embeddingové modely**: Tyto modely se používají k **převodu obsahu webu na číselné reprezentace nazývané vektory** (embeddingy). Tyto vektory zachycují význam tak, že je počítače mohou porovnávat a vyhledávat. Jsou ukládány ve speciální databázi a uživatelé si mohou vybrat, který embedding model chtějí použít.

- **Vektorová databáze (mechanismus vyhledávání)**: Tato databáze **ukládá embeddingy obsahu webu**. Když někdo položí otázku, NLWeb prohledá vektorovou databázi a rychle najde nejrelevantnější informace. Poskytuje rychlý seznam možných odpovědí seřazených podle podobnosti. NLWeb spolupracuje s různými systémy pro ukládání vektorů, jako jsou Qdrant, Snowflake, Milvus, Azure AI Search a Elasticsearch.

### NLWeb na příkladu

![NLWeb](../../../translated_images/cs/nlweb-diagram.c1e2390b310e5fe4.webp)

Znovu vezměme naši cestovní rezervaci na webové stránce, tentokrát však s podporou NLWeb.

1. **Zpracování dat**: Existující produktové katalogy cestovní stránky (například seznamy letů, popisy hotelů, balíčky výletů) jsou formátovány pomocí Schema.org nebo načítány přes RSS kanály. Nástroje NLWeb tyto strukturované údaje přijímají, vytvářejí embeddingy a ukládají je do lokální nebo vzdálené vektorové databáze.

2. **Dotaz v přirozeném jazyce (člověk)**: Uživatel navštíví webovou stránku a místo procházení menu napíše do chatovacího rozhraní: „Najdi mi hotel vhodný pro rodiny v Honolulu s bazénem na příští týden.“

3. **Zpracování NLWeb**: Aplikace NLWeb obdrží tento dotaz. Odešle ho LLM k pochopení a současně prohledá svou vektorovou databázi pro relevantní nabídky hotelů.

4. **Přesné výsledky**: LLM pomáhá interpretovat výsledky vyhledávání z databáze, identifikuje nejlepší shody založené na kritériích „vhodný pro rodiny“, „bazén“ a „Honolulu“ a poté formátuje odpověď v přirozeném jazyce. Klíčové je, že odpověď odkazuje na skutečné hotely z katalogu webu a vyhýbá se vymyšleným informacím.

5. **Interakce AI agenta**: Protože NLWeb funguje jako MCP server, externí AI cestovní agent se může také připojit k této instanci NLWeb. AI agent pak může použít MCP metodu `ask` k přímému dotazu webu: `ask("Jsou v oblasti Honolulu nějaké veganské restaurace doporučené hotelem?")`. NLWeb tento dotaz zpracuje, využije svou databázi informací o restauracích (pokud je načtena) a vrátí strukturovanou JSON odpověď.

### Máte další otázky o MCP/A2A/NLWeb?

Připojte se na [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kde se setkáte s dalšími studenty, můžete navštěvovat konzultační hodiny a získat odpovědi na své otázky o AI agentech.

## Zdroje

- [MCP pro začátečníky](https://aka.ms/mcp-for-beginners)  
- [Dokumentace MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [NLWeb repozitář](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framework)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->