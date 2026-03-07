[![Úvod do AI agentů](../../../translated_images/cs/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klikněte na obrázek výše pro zobrazení videa této lekce)_


# Úvod do AI agentů a případů použití agentů

Vítejte v kurzu "AI Agents for Beginners"! Tento kurz poskytuje základní znalosti a praktické ukázky pro vytváření AI agentů.

Připojte se ke <a href="https://discord.gg/kzRShWzttr" target="_blank">Komunitě Azure AI na Discordu</a>, kde se můžete setkat s dalšími studenty a tvůrci AI agentů a zeptat se na jakékoli otázky týkající se tohoto kurzu.

Pro zahájení tohoto kurzu začneme tím, že lépe pochopíme, co jsou AI agenti a jak je můžeme využít v aplikacích a pracovních postupech, které vytváříme.

## Úvod

Tato lekce zahrnuje:

- Co jsou AI agenti a jaké jsou různé typy agentů?
- Pro které případy použití jsou AI agenti nejvhodnější a jak nám mohou pomoci?
- Jaké jsou některé základní stavební bloky při navrhování agentických řešení?

## Cíle učení
Po dokončení této lekce byste měli být schopni:

- Pochopit koncepty AI agentů a jak se liší od jiných AI řešení.
- Efektivně využívat AI agenty.
- Produktivně navrhovat agentická řešení pro uživatele i zákazníky.

## Definování AI agentů a typy AI agentů

### Co jsou AI agenti?

AI agenti jsou **systémy**, které umožňují **Velké jazykové modely(LLMs)** **provádět akce** tím, že rozšiřují jejich schopnosti poskytnutím **přístupu k nástrojům** a **znalostem**.

Rozdělme tuto definici na menší části:

- **Systém** - Je důležité uvažovat o agentech nikoli jen jako o jedné součásti, ale jako o systému mnoha komponent. Na základní úrovni jsou komponenty AI agenta:
  - **Prostředí** - Definovaný prostor, ve kterém AI agent operuje. Například u AI agenta pro rezervaci cest by prostředím mohl být rezervační systém, který agent používá k dokončení úkolů.
  - **Senzory** - Prostředí má informace a poskytuje zpětnou vazbu. AI agenti používají senzory ke sběru a interpretaci těchto informací o aktuálním stavu prostředí. V příkladu cestovního agenta může rezervační systém poskytovat informace jako dostupnost hotelů nebo ceny letů.
  - **Aktuátory** - Jakmile AI agent obdrží aktuální stav prostředí, pro aktuální úkol určí, kterou akci provést, aby změnil prostředí. U cestovního agenta to může být rezervace dostupného pokoje pro uživatele.

![Co jsou AI agenti?](../../../translated_images/cs/what-are-ai-agents.1ec8c4d548af601a.webp)

**Velké jazykové modely** - Koncept agentů existoval už před vytvořením LLM. Výhodou budování AI agentů s LLM je jejich schopnost interpretovat lidský jazyk a data. Tato schopnost umožňuje LLM interpretovat informace z prostředí a definovat plán, jak změnit prostředí.

**Provádět akce** - Mimo systémy AI agentů jsou LLM omezené na situace, kde je akcí generování obsahu nebo informací na základě uživatelova dotazu. V systémech AI agentů mohou LLM úkoly dokončit tím, že interpretují uživatelovu žádost a používají nástroje dostupné v jejich prostředí.

**Přístup k nástrojům** - Jaké nástroje má LLM k dispozici, je definováno 1) prostředím, ve kterém operuje, a 2) vývojářem AI agenta. V našem příkladu cestovního agenta jsou agentovy nástroje omezeny operacemi dostupnými v rezervačním systému a/nebo může vývojář omezit přístup agenta pouze na lety.

**Paměť+Znalosti** - Paměť může být krátkodobá v kontextu konverzace mezi uživatelem a agentem. Dlouhodobě, mimo informace poskytnuté prostředím, mohou AI agenti také získávat znalosti z jiných systémů, služeb, nástrojů a dokonce jiných agentů. V příkladu cestovního agenta by tyto znalosti mohly být informace o uživatelových cestovních preferencích uložené v databázi zákazníků.

### Různé typy agentů

Nyní, když máme obecnou definici AI agentů, podívejme se na některé konkrétní typy agentů a jak by byly uplatněny na AI agenta pro rezervaci cest.

| **Agent Type**                | **Description**                                                                                                                       | **Example**                                                                                                                                                                                                                   |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Simple Reflex Agents**      | Provedou okamžité akce na základě předdefinovaných pravidel.                                                                            | Cestovní agent interpretuje kontext e-mailu a přeposílá stížnosti na cestování zákaznickému servisu.                                                                                                                          |
| **Model-Based Reflex Agents** | Provedou akce na základě modelu světa a změn v tomto modelu.                                                                            | Cestovní agent upřednostní trasy s významnými změnami cen na základě přístupu k historickým cenovým údajům.                                                                                                                  |
| **Goal-Based Agents**         | Vytvářejí plány k dosažení konkrétních cílů interpretací cíle a určením kroků k jeho dosažení.                                         | Cestovní agent zarezervuje cestu tím, že určí potřebná cestovní uspořádání (auto, veřejná doprava, lety) z aktuální polohy do cíle.                                                                                                     |
| **Utility-Based Agents**      | Zohledňují preference a numericky vyvažují kompromisy pro rozhodnutí, jak dosáhnout cílů.                                               | Cestovní agent maximalizuje užitek vážením pohodlí versus ceny při rezervaci cesty.                                                                                                                                          |
| **Learning Agents**           | Zlepšují se v čase reakcí na zpětnou vazbu a přizpůsobováním akcí.                                                                     | Cestovní agent se zlepšuje pomocí zpětné vazby od zákazníků z dotazníků po cestě a provádí úpravy u budoucích rezervací.                                                                                                       |
| **Hierarchical Agents**       | Obsahují více agentů ve vícestupňovém systému, přičemž vyšší úrovně rozdělují úkoly na podúkoly pro nižší úrovně.                         | Cestovní agent zruší cestu rozdělením úkolu na podúkoly (například zrušení konkrétních rezervací) a nižší úrovně agentů je dokončí a ohlásí zpět vyššímu agentovi.                                                                     |
| **Multi-Agent Systems (MAS)** | Agenti dokončují úkoly nezávisle, buď kooperativně, nebo soutěživě.                                                                    | Kooperativní: Více agentů zarezervuje specifické cestovní služby, jako jsou hotely, lety a zábava. Soutěživé: Více agentů spravuje a soupeří o sdílený kalendář rezervací hotelu, aby zákazníky umístili do hotelu. |

## Kdy použít AI agenty

V předchozí části jsme použili případ použití cestovního agenta, abychom vysvětlili, jak lze různé typy agentů využít v různých scénářích rezervací cest. Tento příklad budeme používat i v průběhu kurzu.

Podívejme se na typy případů použití, pro které jsou AI agenti nejvhodnější:

![Kdy použít AI agenty?](../../../translated_images/cs/when-to-use-ai-agents.54becb3bed74a479.webp)


- **Problémy s otevřeným koncem** - umožnění LLM určit potřebné kroky k dokončení úkolu, protože to nelze vždy pevně zakódovat do pracovního postupu.
- **Vícekrokové procesy** - úkoly, které vyžadují úroveň složitosti, při níž agent potřebuje používat nástroje nebo informace přes více kol místo jednorázového získání.  
- **Zlepšení v čase** - úkoly, kde se agent může zlepšovat v průběhu času přijímáním zpětné vazby buď ze svého prostředí, nebo od uživatelů, aby poskytl lepší užitek.

Další úvahy o používání AI agentů probíráme v lekci Budování důvěryhodných AI agentů.

## Základy agentických řešení

### Vývoj agentů

Prvním krokem při navrhování systému AI agentů je definovat nástroje, akce a chování. V tomto kurzu se zaměřujeme na použití služby **Azure AI Agent Service** k definování našich agentů. Nabízí funkce jako:

- Výběr otevřených modelů, například OpenAI, Mistral a Llama
- Použití licencovaných dat prostřednictvím poskytovatelů jako Tripadvisor
- Použití standardizovaných nástrojů OpenAPI 3.0

### Agentické vzory

Komunikace s LLM probíhá pomocí promptů. Vzhledem k poloautonomní povaze AI agentů není vždy možné nebo nutné ručně opětovně promptovat LLM po změně v prostředí. Používáme **agentické vzory**, které nám umožňují promptovat LLM přes více kroků škálovatelnějším způsobem.

Tento kurz je rozdělen do některých současných populárních agentických vzorů.

### Agentické rámce

Agentické rámce umožňují vývojářům implementovat agentické vzory pomocí kódu. Tyto rámce nabízejí šablony, zásuvné moduly a nástroje pro lepší spolupráci agentů. Tyto výhody zvyšují možnost lepší pozorovatelnosti a odstraňování problémů systémů AI agentů.

V tomto kurzu prozkoumáme Microsoft Agent Framework (MAF) pro vytváření agentů připravených do produkce.

## Ukázkové kódy

- Python: [Rámec agentů](./code_samples/01-python-agent-framework.ipynb)
- .NET: [Rámec agentů](./code_samples/01-dotnet-agent-framework.md)

## Máte další otázky o AI agentech?

Připojte se na [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), kde se můžete setkat s dalšími studenty, účastnit se konzultačních hodin a získat odpovědi na své otázky ohledně AI agentů.

## Předchozí lekce

[Nastavení kurzu](../00-course-setup/README.md)

## Další lekce

[Prozkoumání agentických rámců](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Upozornění:
Tento dokument byl přeložen pomocí služby překladu založené na umělé inteligenci Co-op Translator (https://github.com/Azure/co-op-translator). Ačkoliv usilujeme o přesnost, vezměte prosím na vědomí, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Za jakákoli nedorozumění nebo mylné výklady vyplývající z použití tohoto překladu neneseme odpovědnost.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->