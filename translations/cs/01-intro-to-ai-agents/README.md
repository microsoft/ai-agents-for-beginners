[![Úvod do AI agentů](../../../translated_images/cs/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Klikněte na obrázek výše a sledujte video k této lekci)_

# Úvod do AI agentů a případů použití agentů

Vítejte v kurzu **AI Agentů pro začátečníky**! Tento kurz vám poskytne základní znalosti — a funkční pracovní kód — abyste mohli začít s tvorbou AI agentů od základu.

Přijďte se přivítat do <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord komunity</a> — je plná studentů a tvůrců AI, kteří rádi zodpoví vaše dotazy.

Než se pustíme do tvorby, ujistěme se, že opravdu rozumíme tomu, co AI agent *je* a kdy dává smysl ho použít.

---

## Úvod

Tato lekce zahrnuje:

- Co jsou AI agenti a jaké existují různé typy
- Jaké úkoly jsou pro AI agenty nejvhodnější
- Základní stavební bloky, které budete používat při navrhování agentního řešení

## Cíle učení

Na konci této lekce byste měli být schopni:

- Vysvětlit, co je AI agent a jak se liší od běžného AI řešení
- Vědět, kdy sáhnout po AI agentovi (a kdy ne)
- Nakreslit základní návrh agentního řešení pro reálný problém

---

## Definice AI agentů a typy AI agentů

### Co jsou AI agenti?

Zde je jednoduchý způsob, jak o nich přemýšlet:

> **AI agenti jsou systémy, které umožňují Modelům Velkého Jazyka (LLM) skutečně *něco dělat* — tím, že jim dávají nástroje a znalosti k akci ve světě, ne jen odpovídat na podněty.**

Pojďme si to trochu rozebrat:

- **Systém** — AI agent není jen jedna věc. Je to soubor částí pracujících společně. V jádru má každý agent tři části:
  - **Prostředí** — Prostředí, ve kterém agent pracuje. Pro cestovní agenturu by to byla samotná rezervační platforma.
  - **Senzory** — Jak agent čte aktuální stav svého prostředí. Náš cestovní agent může kontrolovat dostupnost hotelů nebo ceny letů.
  - **Aktuátory** — Jak agent provádí akci. Cestovní agent může rezervovat pokoj, poslat potvrzení nebo zrušit rezervaci.

![Co jsou AI agenti?](../../../translated_images/cs/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Modely Velkého Jazyka** — Agent existovali před LLM, ale LLM jsou to, co dělá moderní agenty tak silnými. Rozumí přirozenému jazyku, uvažují o kontextu a proměňují vágní uživatelský požadavek na konkrétní plán akce.

- **Provádění akcí** — Bez agentského systému by LLM jen generoval text. V agentském systému může LLM skutečně *provádět* kroky — prohledávat databázi, volat API, posílat zprávu.

- **Přístup k nástrojům** — Jaké nástroje agent může použít závisí na (1) prostředí, ve kterém běží a (2) co mu vývojář povolil. Cestovní agent může hledat lety, ale nemusí upravovat záznamy zákazníků — vše závisí na napojení.

- **Paměť + znalosti** — Agenti mohou mít krátkodobou paměť (aktuální konverzaci) a dlouhodobou paměť (databázi zákazníků, minulé interakce). Cestovní agent si může "pamatovat", že preferujete sedadla u okna.

---

### Různé typy AI agentů

Ne všichni agenti jsou postaveni stejně. Zde je přehled hlavních typů s použitím cestovního agenta jako příkladu:

| **Typ agenta** | **Co dělá** | **Příklad cestovního agenta** |
|---|---|---|
| **Jednoduchý reflexní agent** | Sleduje pevně daná pravidla — bez paměti, bez plánování. | Vidí stížnost v emailu → přepošle ji na zákaznický servis. To je vše. |
| **Model založený na reflexním agentovi** | Udržuje vnitřní model světa a aktualizuje ho, jak se věci mění. | Sleduje historické ceny letenek a signalizuje náhle drahé trasy. |
| **Agent založený na cílech** | Má cíl a krok za krokem hledá, jak ho dosáhnout. | Rezervuje celou cestu (lety, auto, hotel) z vašeho současného místa do cíle. |
| **Agent založený na užitku** | Nejenže najde řešení, ale najde *to nejlepší* tím, že vyvažuje kompromisy. | Vyvažuje cenu a pohodlí, aby našel cestu, která nejlépe vyhovuje vašim preferencím. |
| **Učící se agent** | Časem se zlepšuje učení se z feedbacku. | Upravené budoucí doporučení na základě výsledků po cestě z dotazníku. |
| **Hierarchický agent** | Vyšší agent rozdělí práci na podúkoly a deleguje na nižší agenty. | Požadavek "zrušit cestu" se rozdělí na: zrušit let, zrušit hotel, zrušit auto — každý řeší podagent. |
| **Systémy více agentů (MAS)** | Více nezávislých agentů spolupracuje (nebo soupeří). | Kooperativní: jednotliví agenti řeší hotely, lety a zábavu. Soutěživý: více agentů soupeří o obsazení hotelových pokojů za nejlepší cenu. |

---

## Kdy používat AI agenty

Jen proto, že *můžete* použít AI agenta, neznamená, že byste ho měli vždy *použít*. Zde jsou případy, kdy agenty opravdu vynikají:

![Kdy používat AI agenty?](../../../translated_images/cs/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Otevřené problémy** — Když nelze předem naprogramovat kroky k vyřešení problému. Potřebujete, aby LLM zjistil cestu dynamicky.
- **Vícekrokové procesy** — Úkoly, které vyžadují použití nástrojů přes několik kroků, ne jen jednu kontrolu nebo generování.
- **Zlepšení v čase** — Když chcete, aby se systém inteligentně zlepšoval na základě uživatelské zpětné vazby nebo signálů z prostředí.

V lekci **Budování důvěryhodných AI agentů** se později v kurzu podíváme podrobněji, kdy (a kdy *ne*) AI agenty používat.

---

## Základy agentních řešení

### Vývoj agenta

První věc, kterou uděláte při tvorbě agenta, je definovat *co může dělat* — jeho nástroje, akce a chování.

V tomto kurzu používáme **Microsoft Foundry Agent Service** jako hlavní platformu. Podporuje:

- Modely od poskytovatelů jako OpenAI, Mistral a Meta (Llama)
- Licencovaná data od poskytovatelů jako Tripadvisor
- Standardizované definice nástrojů OpenAPI 3.0

### Agentní vzory

Komunikujete s LLM pomocí podnětů (promptů). U agentů nelze vždy všechno dělávat ručně — agent musí provádět akce přes mnoho kroků. Proto existují **agentní vzory**. Jsou to znovupoužitelné strategie pro vyvolávání a orchestraci LLM škálovatelně a spolehlivě.

Tento kurz se strukturuje kolem nejběžnějších a nejužitečnějších agentních vzorů.

### Agentní rámce

Agentní rámce dávají vývojářům předpřipravené šablony, nástroje a infrastrukturu pro tvorbu agentů. Ulehčují:

- Napojení nástrojů a schopností
- Sledování, co agent dělá (a ladění, když něco nefunguje)
- Spolupráci mezi více agenty

V tomto kurzu se zaměřujeme na **Microsoft Agent Framework (MAF)** pro tvorbu produkčně připravených agentů.

---

## Příklady kódu

Připravení vidět to v akci? Zde jsou ukázky kódu pro tuto lekci:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Máte otázky?

Připojte se k [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), spojte se s ostatními studenty, navštěvujte konzultační hodiny a získejte odpovědi na své otázky týkající se AI agentů od komunity.


---

## Testování agenta (volitelné)

Jakmile se naučíte nasazovat agenty v [Lekci 16](../16-deploying-scalable-agents/README.md), můžete přidat rychlou kontrolu po nasazení pro tento lekční `TravelAgent` pomocí připraveného katalogu [`tests/lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json). Viz [`tests/README.md`](../tests/README.md) jak jej spustit.

---

## Předchozí lekce

[Nastavení kurzu](../00-course-setup/README.md)

## Další lekce

[Prozkoumání agentních rámců](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->