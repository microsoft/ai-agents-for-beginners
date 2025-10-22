<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1e40fe956ff79462a02a17080b125041",
  "translation_date": "2025-08-29T20:16:14+00:00",
  "source_file": "01-intro-to-ai-agents/README.md",
  "language_code": "cs"
}
-->
[![Úvod do AI agentů](../../../translated_images/lesson-1-thumbnail.d21b2c34b32d35bbc7f1b4a40a81b031970b6076b4e0c59fb006cf818cac5d4a.cs.png)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klikněte na obrázek výše pro zhlédnutí videa této lekce)_

# Úvod do AI agentů a jejich využití

Vítejte v kurzu "AI agenti pro začátečníky"! Tento kurz poskytuje základní znalosti a praktické příklady pro tvorbu AI agentů.

Připojte se k [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), kde se můžete setkat s dalšími studenty a tvůrci AI agentů a klást jakékoli otázky týkající se tohoto kurzu.

Na začátku kurzu se zaměříme na lepší pochopení toho, co jsou AI agenti a jak je můžeme využít v aplikacích a pracovních postupech, které vytváříme.

## Úvod

Tato lekce zahrnuje:

- Co jsou AI agenti a jaké jsou jejich různé typy?
- Jaké případy použití jsou pro AI agenty nejvhodnější a jak nám mohou pomoci?
- Jaké jsou základní stavební kameny při navrhování agentních řešení?

## Cíle učení
Po dokončení této lekce byste měli být schopni:

- Pochopit koncepty AI agentů a jak se liší od jiných AI řešení.
- Efektivně aplikovat AI agenty.
- Produktivně navrhovat agentní řešení pro uživatele i zákazníky.

## Definice AI agentů a jejich typy

### Co jsou AI agenti?

AI agenti jsou **systémy**, které umožňují **velkým jazykovým modelům (LLMs)** **provádět akce** tím, že rozšiřují jejich schopnosti a poskytují jim **přístup k nástrojům** a **znalostem**.

Rozložme si tuto definici na menší části:

- **Systém** – Je důležité vnímat agenty ne jako jeden samostatný prvek, ale jako systém složený z mnoha komponent. Základní komponenty AI agenta jsou:
  - **Prostředí** – Definovaný prostor, ve kterém AI agent operuje. Například u AI agenta pro rezervaci cest by prostředím mohl být rezervační systém, který agent používá k plnění úkolů.
  - **Senzory** – Prostředí poskytuje informace a zpětnou vazbu. AI agenti používají senzory k získávání a interpretaci těchto informací o aktuálním stavu prostředí. V příkladu s rezervačním agentem by senzory mohly poskytovat informace, jako je dostupnost hotelů nebo ceny letů.
  - **Aktuátory** – Jakmile AI agent obdrží aktuální stav prostředí, určí, jakou akci provést, aby prostředí změnil. U rezervačního agenta by to mohlo být například rezervování dostupného pokoje pro uživatele.

![Co jsou AI agenti?](../../../translated_images/what-are-ai-agents.1ec8c4d548af601a3a78c6c02e5c355d19c06a4a74fe93e3609a1d08e8c15689.cs.png)

**Velké jazykové modely** – Koncept agentů existoval již před vznikem LLM. Výhodou budování AI agentů s LLM je jejich schopnost interpretovat lidský jazyk a data. Tato schopnost umožňuje LLM interpretovat informace z prostředí a definovat plán pro změnu prostředí.

**Provádění akcí** – Mimo systémy AI agentů jsou LLM omezeny na situace, kdy akce spočívá v generování obsahu nebo informací na základě uživatelského zadání. V systémech AI agentů mohou LLM plnit úkoly interpretací uživatelských požadavků a využíváním nástrojů dostupných v jejich prostředí.

**Přístup k nástrojům** – Jaké nástroje má LLM k dispozici, je definováno 1) prostředím, ve kterém operuje, a 2) vývojářem AI agenta. V našem příkladu s rezervačním agentem jsou nástroje omezeny operacemi dostupnými v rezervačním systému, případně může vývojář omezit přístup agenta pouze na určité funkce, například na lety.

**Paměť + znalosti** – Paměť může být krátkodobá v kontextu konverzace mezi uživatelem a agentem. Dlouhodobě, mimo informace poskytované prostředím, mohou AI agenti získávat znalosti z jiných systémů, služeb, nástrojů a dokonce i od jiných agentů. V příkladu s rezervačním agentem by těmito znalostmi mohly být informace o uživatelských preferencích uložené v zákaznické databázi.

### Různé typy agentů

Nyní, když máme obecnou definici AI agentů, podívejme se na konkrétní typy agentů a jak by mohly být aplikovány na rezervačního AI agenta.

| **Typ agenta**                | **Popis**                                                                                                                       | **Příklad**                                                                                                                                                                                                                   |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Jednoduchý reflexní agent** | Provádí okamžité akce na základě předem definovaných pravidel.                                                                   | Rezervační agent interpretuje kontext e-mailu a přeposílá stížnosti na cestování zákaznickému servisu.                                                                                                                          |
| **Modelově založený reflexní agent** | Provádí akce na základě modelu světa a změn v tomto modelu.                                                              | Rezervační agent upřednostňuje trasy s významnými změnami cen na základě přístupu k historickým údajům o cenách.                                                                                                             |
| **Agent založený na cílech**  | Vytváří plány k dosažení konkrétních cílů interpretací cíle a určením akcí k jeho dosažení.                                      | Rezervační agent rezervuje cestu určením potřebných cestovních opatření (auto, veřejná doprava, lety) z aktuálního místa do cílové destinace.                                                                                |
| **Agent založený na užitku**  | Zvažuje preference a numericky vyhodnocuje kompromisy, aby určil, jak dosáhnout cílů.                                           | Rezervační agent maximalizuje užitek tím, že váží pohodlí oproti nákladům při rezervaci cesty.                                                                                                                               |
| **Učící se agent**            | Zlepšuje se v průběhu času na základě zpětné vazby a přizpůsobuje své akce.                                                     | Rezervační agent se zlepšuje na základě zpětné vazby od zákazníků z dotazníků po cestě, aby provedl úpravy při budoucích rezervacích.                                                                                         |
| **Hierarchický agent**        | Obsahuje více agentů v hierarchickém systému, kde agenti na vyšší úrovni rozdělují úkoly na podúkoly, které plní agenti na nižší úrovni. | Rezervační agent ruší cestu rozdělením úkolu na podúkoly (například zrušení konkrétních rezervací) a nechává je dokončit agenty na nižší úrovni, kteří podávají zprávu agentovi na vyšší úrovni.                                     |
| **Systémy více agentů (MAS)** | Agenti plní úkoly nezávisle, buď kooperativně, nebo konkurenčně.                                                                | Kooperativní: Více agentů rezervuje konkrétní cestovní služby, jako jsou hotely, lety a zábava. Konkurenční: Více agentů spravuje a soutěží o sdílený rezervační kalendář hotelu, aby zákazníky ubytovali. |

## Kdy používat AI agenty

V předchozí části jsme použili příklad rezervačního agenta k vysvětlení, jak lze různé typy agentů použít v různých scénářích rezervace cest. Tento příklad budeme používat i v průběhu kurzu.

Podívejme se na typy případů použití, pro které jsou AI agenti nejvhodnější:

![Kdy používat AI agenty?](../../../translated_images/when-to-use-ai-agents.54becb3bed74a479f5caca9c951132ce81d482a6704bcd22e5a600dbabc9434e.cs.png)

- **Otevřené problémy** – umožnění LLM určit potřebné kroky k dokončení úkolu, protože je nelze vždy pevně zakódovat do pracovního postupu.
- **Vícekrokové procesy** – úkoly, které vyžadují určitou úroveň složitosti, kdy AI agent potřebuje používat nástroje nebo informace během více kroků, nikoli jednorázově.
- **Zlepšování v průběhu času** – úkoly, kde se agent může zlepšovat na základě zpětné vazby od prostředí nebo uživatelů, aby poskytoval lepší užitek.

Další úvahy o používání AI agentů pokryjeme v lekci o budování důvěryhodných AI agentů.

## Základy agentních řešení

### Vývoj agentů

Prvním krokem při navrhování systému AI agenta je definování nástrojů, akcí a chování. V tomto kurzu se zaměřujeme na použití **Azure AI Agent Service** k definování našich agentů. Nabízí funkce jako:

- Výběr otevřených modelů, jako jsou OpenAI, Mistral a Llama
- Použití licencovaných dat prostřednictvím poskytovatelů, jako je Tripadvisor
- Použití standardizovaných nástrojů OpenAPI 3.0

### Agentní vzory

Komunikace s LLM probíhá prostřednictvím promptů. Vzhledem k poloautonomní povaze AI agentů není vždy možné nebo nutné ručně znovu promptovat LLM po změně prostředí. Používáme **agentní vzory**, které nám umožňují promptovat LLM během více kroků škálovatelnějším způsobem.

Tento kurz je rozdělen do některých aktuálně populárních agentních vzorů.

### Agentní rámce

Agentní rámce umožňují vývojářům implementovat agentní vzory prostřednictvím kódu. Tyto rámce nabízejí šablony, pluginy a nástroje pro lepší spolupráci AI agentů. Tyto výhody poskytují schopnosti pro lepší pozorovatelnost a odstraňování problémů v systémech AI agentů.

V tomto kurzu prozkoumáme výzkumně orientovaný rámec AutoGen a produkčně připravený rámec Agent od Semantic Kernel.

### Máte další otázky o AI agentech?

Připojte se k [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), kde se můžete setkat s dalšími studenty, zúčastnit se konzultačních hodin a získat odpovědi na své otázky ohledně AI agentů.

## Předchozí lekce

[Nastavení kurzu](../00-course-setup/README.md)

## Další lekce

[Prozkoumání agentních rámců](../02-explore-agentic-frameworks/README.md)

---

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nenese odpovědnost za žádné nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.