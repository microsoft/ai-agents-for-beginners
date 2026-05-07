[![Úvod do AI agentů](../../../translated_images/cs/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klikněte na obrázek výše pro přehrání videa k této lekci)_

# Úvod do AI agentů a případů použití agentů

Vítejte v kurzu **AI agenti pro začátečníky**! Tento kurz vám poskytne základní znalosti — a skutečný funkční kód — k tomu, abyste začali stavět AI agenty od nuly.

Přijďte pozdravit do <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord komunity</a> — je plná studentů a tvůrců AI, kteří rádi odpoví na vaše otázky.

Než se pustíme do stavění, ujistěme se, že skutečně chápeme, co AI agent *je* a kdy dává smysl ho použít.

---

## Úvod

Tato lekce pokrývá:

- Co jsou AI agenti a různé typy, které existují
- Pro jaké úkoly se AI agenti nejlépe hodí
- Základní stavební kameny, které použijete při navrhování agentního řešení

## Cíle učení

Na konci této lekce byste měli být schopni:

- Vysvětlit, co je AI agent a jak se liší od běžného AI řešení
- Vědět, kdy sáhnout po AI agentovi (a kdy ne)
- Náčrtnout základní design agentního řešení pro reálný problém

---

## Definování AI agentů a typy AI agentů

### Co jsou AI agenti?

Zde je jednoduchý způsob, jak si to představit:

> **AI agenti jsou systémy, které umožňují modelům velkého jazyka (LLM) skutečně *něco dělat* — tím, že jim dávají nástroje a znalosti k působení ve světě, ne jen reagovat na podněty.**

Pojďme si to trochu rozebrat:

- **Systém** — AI agent není jen jedna věc. Je to sbírka částí, které spolupracují. V jádru má každý agent tři části:
  - **Prostředí** — prostor, ve kterém agent pracuje. Pro cestovní agenturu by to byla samotná rezervační platforma.
  - **Senzory** — jak agent čte aktuální stav svého prostředí. Náš cestovní agent může kontrolovat dostupnost hotelů nebo ceny letenek.
  - **Aktuátory** — jak agent jedná. Cestovní agent může rezervovat pokoj, poslat potvrzení nebo zrušit rezervaci.

![Co jsou AI agenti?](../../../translated_images/cs/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Modely velkého jazyka** — agenti existovali už před LLM, ale LLM jsou tím, co moderní agenty dělá tak silnými. Rozumí přirozenému jazyku, dokážou uvažovat o kontextu a proměnit nejasné uživatelské požadavky v konkrétní plán akcí.

- **Provádění akcí** — bez systému agenta LLM jen generuje text. V rámci systému agenta může LLM skutečně *vykonávat* kroky — hledat v databázi, volat API, posílat zprávy.

- **Přístup k nástrojům** — jaké nástroje může agent používat závisí na (1) prostředí, ve kterém běží, a (2) co mu vývojář zvolí dát k dispozici. Cestovní agent může vyhledávat lety, ale nemůže upravovat záznamy zákazníků — záleží na tom, co je zapojeno.

- **Paměť + znalosti** — agenti mohou mít krátkodobou paměť (aktuální konverzaci) a dlouhodobou paměť (zákaznickou databázi, minulé interakce). Cestovní agent může "pamatovat" vaše preference například okna v letadle.

---

### Různé typy AI agentů

Ne všichni agenti jsou stavěni stejným způsobem. Tady je přehled hlavních typů, přičemž jako příklad použijeme cestovní agenturu:

| **Typ agenta** | **Co dělá** | **Příklad cestovního agenta** |
|---|---|---|
| **Agent reflexního typu** | Řídí se pevně danými pravidly — bez paměti, bez plánování. | Vidí stížnost v e-mailu → přepošle ji zákaznickému servisu. A tím to končí. |
| **Agent reflexního typu s modelem** | Uchovává vnitřní model světa a aktualizuje ho, jak se situace mění. | Sleduje historické ceny letenek a upozorní na trasy, které náhle zdražily. |
| **Agent s cílovým řízením** | Má cíl a krok po kroku hledá cestu, jak ho dosáhnout. | Zarezervuje celou cestu (letenky, auto, hotel) od vaší současné polohy až do cílové destinace. |
| **Agent založený na užitku** | Nejenže hledá *nějaké* řešení — váží možnosti a hledá *to nejlepší*. | Vyvažuje cenu a pohodlí, aby našel cestu, která nejvíc odpovídá vašim preferencím. |
| **Učící se agent** | Postupně se zlepšuje na základě zpětné vazby. | Upravuje budoucí doporučení rezervací na základě výsledků dotazníků po cestě. |
| **Hierarchický agent** | Vyšší úroveň agenta rozděluje práci na dílčí úkoly a přiděluje je nižším agentům. | Požadavek „zrušit cestu“ se rozdělí na: zrušení letu, zrušení hotelu, zrušení auta — každý úkol řeší podagent. |
| **Systémy více agentů (MAS)** | Více nezávislých agentů pracujících společně (nebo soupeřících). | Kooperativní: samostatní agenti spravují hotely, lety a zábavu. Soutěživí: několik agentů soupeří, kdo poskytne nejlepší cenu u hotelových pokojů. |

---

## Kdy používat AI agenty

To, že *můžete* použít AI agenta, ještě neznamená, že to vždy *musíte*. Tady jsou situace, kdy agenti skutečně vynikají:

![Kdy používat AI agenty?](../../../translated_images/cs/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Otevřené problémy** — Když nelze předem naprogramovat jednotlivé kroky řešení. LLM musí dynamicky najít cestu.
- **Vícekrokové procesy** — Úkoly vyžadující použití nástrojů přes několik kroků, ne jen jednorázové vyhledání nebo generování.
- **Zlepšování v čase** — Když chcete, aby se systém sám zlepšoval podle zpětné vazby uživatelů nebo signálů z prostředí.

Podrobněji si probereme, kdy (a kdy *ne*) používat AI agenty v lekci **Budování důvěryhodných AI agentů** později v kurzu.

---

## Základy agentních řešení

### Vývoj agentů

Prvním krokem při vytváření agenta je definovat *co zvládne* — jeho nástroje, akce a chování.

V tomto kurzu používáme jako hlavní platformu **Azure AI Agent Service**. Podporuje:

- Otevřené modely jako OpenAI, Mistral a Llama
- Licencovaná data od poskytovatelů jako Tripadvisor
- Standardizované definice nástrojů OpenAPI 3.0

### Agentní vzory

S LLM komunikujete pomocí promptů. S agenty nelze vždy ručně tvořit každý prompt — agent musí jednat přes mnoho kroků. Proto existují **agentní vzory**. Jsou to opakovaně použitelné strategie pro promptování a orchestraci LLM způsobem, který je škálovatelný a spolehlivý.

Tento kurz je organizován kolem nejběžnějších a nejužitečnějších agentních vzorů.

### Agentní frameworky

Agentní frameworky dávají vývojářům šablony, nástroje a infrastrukturu pro stavbu agentů. Usnadňují:

- Zapojení nástrojů a funkcí
- Sledování, co agent dělá (a ladění, když se něco pokazí)
- Spolupráci mezi více agenty

V tomto kurzu se zaměřujeme na **Microsoft Agent Framework (MAF)** pro vytváření produkčně připravených agentů.

---

## Ukázky kódu

Připravení vidět to v akci? Tady jsou ukázky kódu pro tuto lekci:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Máte otázky?

Připojte se do [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) a spojte se s dalšími studenty, navštivte konzultace a získejte odpovědi na své otázky o AI agentech od komunity.

---

## Předchozí lekce

[Nastavení kurzu](../00-course-setup/README.md)

## Další lekce

[Prozkoumání agentních frameworků](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace je doporučen profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo chybné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->