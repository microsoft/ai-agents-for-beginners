[![Úvod do AI agentů](../../../translated_images/cs/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klikněte na obrázek výše pro zhlédnutí videa k této lekci)_

# Úvod do AI agentů a případů použití agentů

Vítejte v kurzu **AI Agentů pro začátečníky**! Tento kurz vám poskytne základní znalosti — i funkční kód — abyste mohli začít vytvářet AI agenty od nuly.

Přijďte se pozdravit na <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord komunitu</a> — je plná studentů a tvůrců AI, kteří rádi odpoví na vaše otázky.

Než se pustíme do tvorby, ujistěme se, že skutečně chápeme, co AI agent *je* a kdy dává smysl ho použít.

---

## Úvod

Tato lekce pokrývá:

- Co jsou AI agenti a různé typy, které existují
- Pro jaké úkoly jsou AI agenti nejvhodnější
- Základní stavební kameny, které použijete při navrhování agentního řešení

## Cíle učení

Na konci této lekce byste měli být schopni:

- Vysvětlit, co je AI agent a jak se liší od běžného AI řešení
- Vědět, kdy sáhnout po AI agentovi (a kdy naopak ne)
- Nákreslit základní návrh agentního řešení pro reálný problém

---

## Definice AI agentů a typy AI agentů

### Co jsou AI agenti?

Tady je jednoduchý způsob, jak o tom přemýšlet:

> **AI agenti jsou systémy, které umožňují velkým jazykovým modelům (LLMs) skutečně *něco dělat* — tím, že jim dávají nástroje a znalosti, aby mohli působit ve světě, nejen odpovídat na příkazy.**

Pojďme si to rozebrat:

- **Systém** — AI agent není jen jedna věc. Je to kolekce částí, které spolupracují. V jádru má každý agent tři části:
  - **Prostředí** — prostor, ve kterém agent pracuje. Pro cestovního agenta je to samotná rezervační platforma.
  - **Senzory** — jak agent čte aktuální stav svého prostředí. Náš cestovní agent může kontrolovat dostupnost hotelů nebo ceny letenek.
  - **Aktuátory** — jak agent jedná. Cestovní agent může zarezervovat pokoj, poslat potvrzení nebo zrušit rezervaci.

![Co jsou AI agenti?](../../../translated_images/cs/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Velké jazykové modely** — agenti existovali i před LLM, ale LLM je to, co dělá moderní agenty tak silnými. Dokážou rozumět přirozenému jazyku, uvažovat o kontextu a proměnit vágní uživatelský požadavek v konkrétní plán akce.

- **Provádění akcí** — bez agenta LLM jen generuje text. V rámci agentního systému může LLM skutečně *vykonávat* kroky — hledat v databázi, volat API, posílat zprávu.

- **Přístup k nástrojům** — jaké nástroje agent může použít, závisí na (1) prostředí, ve kterém běží, a (2) co mu vývojář zvolí. Cestovní agent může například hledat lety, ale nebude upravovat zákaznické záznamy — to záleží na připojení.

- **Paměť + znalosti** — agenti mohou mít krátkodobou paměť (aktuální konverzace) a dlouhodobou paměť (zákaznická databáze, minulé interakce). Cestovní agent si může „pamatovat“, že preferujete sedadlo u okna.

---

### Různé typy AI agentů

Ne všichni agenti jsou postaveni stejně. Tady je přehled hlavních typů, s příkladem cestovního agenta:

| **Typ agenta** | **Co dělá** | **Příklad cestovního agenta** |
|---|---|---|
| **Jednoduchý reflexní agent** | Řídí se tvrdě zakódovanými pravidly — nemá paměť, neplánuje. | Vidí stížnost v e-mailu → přepošle jí zákaznické podpoře. Tím to končí. |
| **Modelový reflexní agent** | Uchovává interní model světa a aktualizuje ho, jak se situace mění. | Sleduje historické ceny letenek a upozorní na náhle zvýšené trasy. |
| **Agent založený na cíli** | Má cíl a krok za krokem vymýšlí, jak ho dosáhnout. | Zarezervuje celou cestu (letenky, auto, hotel) od vaší aktuální polohy k cíli. |
| **Agent založený na užitku** | Nehledá jen *nějaké* řešení, ale *nejlepší* vážením kompromisů. | Balancuje náklady a pohodlí, aby našel cestu, která nejlépe odpovídá vašim preferencím. |
| **Učící agent** | Zlepšuje se časem učením z reakcí. | Přizpůsobuje budoucí návrhy rezervací podle výsledků dotazníků po cestě. |
| **Hierarchický agent** | Vyšší agent rozděluje práci na podúkoly a deleguje je nižším agentům. | Požadavek „zrušit cestu“ se rozdělí na: zrušit let, zrušit hotel, zrušit půjčení auta — každý řeší jiný agent. |
| **Systémy více agentů (MAS)** | Více nezávislých agentů spolupracuje (nebo soupeří). | Kooperace: jednotliví agenti se starají o hotely, lety a zábavu. Soutěž: více agentů soutěží o rezervaci hotelů za nejlepší cenu. |

---

## Kdy používat AI agenty

Jen proto, že *můžete* použít AI agenta, neznamená to, že byste vždy měli. Zde jsou situace, kdy agenti skutečně vynikají:

![Kdy používat AI agenty?](../../../translated_images/cs/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Otevřené problémy** — když nejsou kroky k řešení problému předem naprogramovatelné. LLM musí dynamicky vymyslet cestu.
- **Vícekrokové procesy** — úkoly vyžadující používání nástrojů přes několik kol, ne jen jedno vyhledání nebo generování.
- **Zlepšování v čase** — když chcete, aby systém získával inteligenci na základě zpětné vazby uživatelů nebo signálů z prostředí.

V lekci **Budování důvěryhodných AI agentů** později v kurzu se ponoříme hlouběji do toho, kdy (a kdy *ne*) používat AI agenty.

---

## Základy agentních řešení

### Vývoj agentů

První, co při stavbě agenta uděláte, je definovat *co může dělat* — jaké má nástroje, akce a chování.

V tomto kurzu používáme jako hlavní platformu **Azure AI Agent Service**. Podporuje:

- Modely od poskytovatelů jako OpenAI, Mistral a Meta (Llama)
- Licencovaná data od poskytovatelů jako Tripadvisor
- Standardizované definice nástrojů podle OpenAPI 3.0

### Agentní vzory

Komunikujete s LLM pomocí promptů. U agentů nelze vždy ručně vytvářet každý prompt — agent musí podniknout akce přes mnoho kroků. Proto přicházejí **agentní vzory**. Jsou to znovupoužitelné strategie pro promptování a orchestraci LLM způsobem, který je škálovatelnější a spolehlivější.

Tento kurz je postaven kolem nejběžnějších a nejužitečnějších agentních vzorů.

### Agentní frameworky

Agentní frameworky dávají vývojářům předpřipravené šablony, nástroje a infrastrukturu pro tvorbu agentů. Usnadňují:

- Propojení nástrojů a schopností
- Sledování, co agent dělá (a ladění, když se něco pokazí)
- Spolupráci napříč více agenty

V tomto kurzu se zaměřujeme na **Microsoft Agent Framework (MAF)** pro tvorbu agentů připravených do produkce.

---

## Ukázky kódu

Chcete to vidět v praxi? Tady jsou ukázky kódu pro tuto lekci:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Máte otázky?

Připojte se na [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), kde se spojíte s ostatními studenty, zúčastníte se konzultací a získáte odpovědi na své otázky ohledně AI agentů od komunity.

---

## Předchozí lekce

[Nastavení kurzu](../00-course-setup/README.md)

## Další lekce

[Prozkoumání agentních frameworků](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->