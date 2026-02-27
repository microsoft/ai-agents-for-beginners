# AI Agents in Production: Observability & Evaluation

[![AI Agents in Production](../../../translated_images/cs/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Jak se AI agenti přesouvají z experimentálních prototypů do reálných aplikací, stává se důležitou schopnost porozumět jejich chování, sledovat jejich výkon a systematicky hodnotit jejich výstupy.

## Learning Goals

Po dokončení této lekce budete vědět/jak porozumět:
- Základní koncepty observability a vyhodnocování agentů
- Techniky pro zlepšení výkonu, nákladů a efektivity agentů
- Co a jak systematicky vyhodnocovat vaše AI agenty
- Jak kontrolovat náklady při nasazování AI agentů do produkce
- Jak instrumentovat agenty postavené s Microsoft Agent Framework

Cílem je vybavit vás znalostmi, které promění vaše „černé skříňky“ agentů v průhledné, snadno spravovatelné a spolehlivé systémy.

_**Poznámka:** Je důležité nasazovat AI agenty, kteří jsou bezpeční a důvěryhodní. Podívejte se také na lekci [Budování důvěryhodných AI agentů](./06-building-trustworthy-agents/README.md)._

## Traces and Spans

Nástroje pro observabilitu jako [Langfuse](https://langfuse.com/) nebo [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) obvykle reprezentují běhy agentů jako trace a spany.

- **Trace** reprezentuje celý úkol agenta od začátku do konce (např. zpracování uživatelského dotazu).
- **Spans** jsou jednotlivé kroky v trace (např. volání language modelu nebo získávání dat).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Bez observability může agent působit jako „černá skříňka“ – jeho vnitřní stav a uvažování jsou neprůhledné, což ztěžuje diagnostiku problémů nebo optimalizaci výkonu. S observabilitou se agenti stávají „skleněnými krabičkami“, které poskytují průhlednost nezbytnou pro budování důvěry a zajištění, že fungují podle očekávání. 

## Why Observability Matters in Production Environments

Přesun AI agentů do produkčního prostředí přináší novou sadu výzev a požadavků. Observabilita už není „příjemným doplňkem“, ale kritickou schopností:

*   **Ladění a analýza příčiny problému:** Když agent selže nebo vygeneruje neočekávaný výstup, nástroje pro observabilitu poskytují trace potřebné k určení zdroje chyby. To je obzvlášť důležité u složitých agentů, které mohou zahrnovat více volání LLM, interakce s nástroji a podmíněnou logiku.
*   **Správa latence a nákladů:** AI agenti často spoléhají na LLM a jiné externí API, která se účtují za tokeny nebo za volání. Observabilita umožňuje přesné sledování těchto volání a pomáhá identifikovat operace, které jsou nadměrně pomalé nebo drahé. To umožňuje týmům optimalizovat prompty, vybrat efektivnější modely nebo přepracovat pracovní postupy tak, aby zvládly provozní náklady a zajistily dobrý uživatelský zážitek.
*   **Důvěra, bezpečnost a shoda:** V mnoha aplikacích je důležité zajistit, aby se agenti chovali bezpečně a eticky. Observabilita poskytuje auditní stopu akcí a rozhodnutí agenta. To lze využít k detekci a zmírnění problémů, jako je prompt injection, generování škodlivého obsahu nebo špatné nakládání s osobně identifikovatelnými informacemi (PII). Například můžete zkontrolovat trace, abyste pochopili, proč agent poskytl určitá odpověď nebo použil konkrétní nástroj.
*   **Cykly nepřetržitého zlepšování:** Data z observability jsou základem iterativního vývojového procesu. Monitorováním výkonu agentů v reálném světě mohou týmy identifikovat oblasti pro zlepšení, shromažďovat data pro doladění modelů a ověřovat dopad změn. To vytváří zpětnou vazbu, kde produkční poznatky z online vyhodnocování informují offline experimentování a vylepšování, což vede k postupnému zlepšování výkonu agentů.

## Key Metrics to Track

Pro sledování a porozumění chování agenta by měl být sledován řada metrik a signálů. Konkrétní metriky se mohou lišit podle účelu agenta, ale některé jsou univerzálně důležité.

Zde jsou některé z nejběžnějších metrik, které nástroje pro observabilitu monitorují:

**Latency:** Jak rychle agent odpovídá? Dlouhé čekání negativně ovlivňuje uživatelský zážitek. Měli byste měřit latenci pro úkoly a jednotlivé kroky sledováním běhů agenta. Například agent, který potřebuje 20 sekund na všechna volání modelu, lze zrychlit použitím rychlejšího modelu nebo paralelním spouštěním volání modelu.

**Costs:** Kolik stojí jedno spuštění agenta? AI agenti se spoléhají na volání LLM účtovaná za tokeny nebo na externí API. Časté používání nástrojů nebo více promptů může rychle zvýšit náklady. Například pokud agent volá LLM pětkrát pro marginální zlepšení kvality, musíte posoudit, zda jsou náklady ospravedlněné, nebo jestli by bylo možné snížit počet volání nebo použít levnější model. Monitorování v reálném čase také pomůže identifikovat neočekávané výkyvy (např. chyby způsobující nadměrné smyčky API).

**Request Errors:** Kolik požadavků agent nezpracoval? To může zahrnovat chyby API nebo neúspěšná volání nástrojů. Aby byl agent v produkci odolnější vůči těmto chybám, můžete nastavit fallbacky nebo retry mechanismy. Např. pokud poskytovatel LLM A selže, přepnete na poskytovatele LLM B jako zálohu.

**User Feedback:** Implementace přímého hodnocení uživatelů poskytuje cenné informace. To může zahrnovat explicitní hodnocení (👍thumbs-up/👎down, ⭐1-5 hvězdiček) nebo textové komentáře. Konzistentně negativní zpětná vazba by vás měla varovat, protože to je signál, že agent nefunguje podle očekávání. 

**Implicit User Feedback:** Chování uživatelů poskytuje nepřímou zpětnou vazbu i bez explicitních hodnocení. To může zahrnovat okamžité přeformulování otázky, opakované dotazy nebo kliknutí na tlačítko opakovat. Např. pokud vidíte, že uživatelé opakovaně pokládají stejnou otázku, je to znamení, že agent nefunguje podle očekávání.

**Accuracy:** Jak často agent produkuje správné nebo žádoucí výstupy? Definice přesnosti se liší (např. správnost řešení problému, přesnost vyhledávání informací, spokojenost uživatele). Prvním krokem je definovat, jak vypadá úspěch pro vašeho agenta. Přesnost můžete sledovat prostřednictvím automatizovaných kontrol, evaluačních skóre nebo štítků dokončení úkolu. Například označováním trace jako „succeeded“ nebo „failed“.

**Automated Evaluation Metrics:** Můžete také nastavit automatizované evaluace. Například můžete použít LLM k ohodnocení výstupu agenta, zda je užitečný, přesný nebo ne. Existuje také několik open source knihoven, které vám pomohou skórovat různé aspekty agenta. Např. [RAGAS](https://docs.ragas.io/) pro RAG agenty nebo [LLM Guard](https://llm-guard.com/) k detekci škodlivého jazyka nebo prompt injection. 

V praxi dává kombinace těchto metrik nejlepší pokrytí stavu AI agenta. V tomto kapitole [example notebook](./code_samples/10-expense_claim-demo.ipynb) vám ukážeme, jak tyto metriky vypadají na reálných příkladech, ale nejdříve se naučíme, jak obvykle vypadá typický evaluační workflow.

## Instrument your Agent

K získávání tracing dat budete muset instrumentovat svůj kód. Cílem je instrumentovat kód agenta tak, aby emitoval trace a metriky, které může zachytit, zpracovat a vizualizovat platforma pro observabilitu.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) se stal průmyslovým standardem pro observabilitu LLM. Poskytuje sadu API, SDK a nástrojů pro generování, sběr a export telemetrických dat. 

Existuje mnoho instrumentačních knihoven, které obalí stávající agentní frameworky a usnadní export OpenTelemetry spanů do nástroje pro observabilitu. Microsoft Agent Framework se s OpenTelemetry integruje nativně. Níže je příklad instrumentace agenta MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Vykonávání agenta je automaticky sledováno.
    pass
```

The [example notebook](./code_samples/10-expense_claim-demo.ipynb) in this chapter will demonstrate how to instrument your MAF agent.

**Manual Span Creation:** Zatímco instrumentační knihovny poskytují dobrý základ, často jsou případy, kdy jsou potřeba podrobnější nebo vlastní informace. Můžete ručně vytvářet span-y za účelem přidání vlastního aplikačního logického obsahu. Důležitější je, že mohou obohacovat automaticky nebo ručně vytvořené spany o vlastní atributy (také známé jako tagy nebo metadata). Tyto atributy mohou zahrnovat obchodně specifická data, mezivýpočty nebo jakýkoli kontext, který může být užitečný pro ladění nebo analýzu, jako jsou `user_id`, `session_id` nebo `model_version`.

Příklad ručního vytváření trace a spanů s [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3): 

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Agent Evaluation

Observabilita nám dává metriky, ale evaluace je proces analýzy těchto dat (a provádění testů) za účelem zjištění, jak dobře AI agent funguje a jak ho lze zlepšit. Jinými slovy, jakmile máte trace a metriky, jak je použít k posouzení agenta a rozhodování? 

Pravidelné vyhodnocování je důležité, protože AI agenti jsou často nedeterminističtí a mohou se vyvíjet (prostřednictvím aktualizací nebo driftu chování modelu) – bez vyhodnocování byste nevěděli, zda váš „chytrý agent“ skutečně odvádí svou práci dobře, nebo zda došlo ke zhoršení.

Existují dvě kategorie vyhodnocení AI agentů: **online evaluation** a **offline evaluation**. Oba jsou cenné a vzájemně se doplňují. Obvykle začínáme s offline evaluací, protože je to minimální nezbytný krok před nasazením agenta.

### Offline Evaluation

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

To zahrnuje hodnocení agenta v kontrolovaném prostředí, typicky za použití testovacích datasetů, nikoli živých uživatelských dotazů. Používáte kurátované datové sady, kde znáte očekávaný výstup nebo správné chování, a poté na nich spustíte agenta. 

Například pokud jste vytvořili agenta pro slovní matematické úlohy, můžete mít [testovací dataset](https://huggingface.co/datasets/gsm8k) 100 úloh se známými odpověďmi. Offline evaluace se často provádí během vývoje (a může být součástí CI/CD pipeline) za účelem kontroly zlepšení nebo ochrany proti regresím. Výhodou je, že je to **opakovatelná metodika a můžete získat jasné metriky přesnosti, protože máte ground truth**. Můžete také simulovat uživatelské dotazy a měřit odpovědi agenta proti ideálním odpovědím nebo použít automatizované metriky, jak bylo popsáno výše. 

Hlavní výzvou offline evaluace je zajistit, aby byl testovací dataset komplexní a zůstal relevantní – agent může dobře fungovat na fixním testovacím setu, ale v produkci narazit na velmi odlišné dotazy. Proto byste měli udržovat testovací sady aktualizované o nové okrajové případy a příklady, které odrážejí reálné scénáře. Směs malých „smoke testů“ a větších evaluačních sad je užitečná: malé sady pro rychlé kontroly a větší pro širší metriky výkonu.

### Online Evaluation 

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

To se týká hodnocení agenta v živém, reálném prostředí, tedy během skutečného používání v produkci. Online evaluace zahrnuje monitorování výkonu agenta na reálných uživatelských interakcích a průběžnou analýzu výsledků. 

Například můžete sledovat míru úspěšnosti, skóre spokojenosti uživatelů nebo jiné metriky na živém provozu. Výhodou online evaluace je, že **zachytí věci, které nemusíte předvídat v laboratorním prostředí** – můžete pozorovat drift modelu v čase (pokud se efektivita agenta zhoršuje s posunem vzorů vstupů) a zachytit neočekávané dotazy nebo situace, které nebyly ve vašich testovacích datech. Poskytuje skutečný obraz toho, jak se agent chová „v divočině“. 

Online evaluace často zahrnuje shromažďování implicitní a explicitní zpětné vazby uživatelů, jak bylo diskutováno, a možné spouštění shadow testů nebo A/B testů (kde nová verze agenta běží paralelně k porovnání se starou). Výzvou je, že může být obtížné získat spolehlivé štítky nebo skóre pro živé interakce – můžete se spoléhat na zpětnou vazbu uživatelů nebo downstream metriky (např. zda uživatel klikl na výsledek).

### Combining the two

Online a offline evaluace si nejsou vzájemně vyhrazené; jsou vysoce komplementární. Poznatky z online monitorování (např. nové typy uživatelských dotazů, kde agent selhává) lze použít k doplnění a zlepšení offline testovacích datasetů. Naopak agenti, kteří dobře fungují v offline testech, mohou být následně s větší důvěrou nasazeni a monitorováni online. 

Ve skutečnosti mnoho týmů přijímá smyčku: 

_evaluate offline -> deploy -> monitor online -> collect new failure cases -> add to offline dataset -> refine agent -> repeat_.

## Common Issues

Při nasazování AI agentů do produkce můžete narazit na různé výzvy. Zde jsou některé běžné problémy a jejich možná řešení:

| **Issue**    | **Potential Solution**   |
| ------------- | ------------------ |
| AI Agent not performing tasks consistently | - Refine the prompt given to the AI Agent; be clear on objectives.<br>- Identify where dividing the tasks into subtasks and handling them by multiple agents can help. |
| AI Agent running into continuous loops  | - Ensure you have clear termination terms and conditions so the Agent knows when to stop the process.<br>- For complex tasks that require reasoning and planning, use a larger model that is specialized for reasoning tasks. |
| AI Agent tool calls are not performing well   | - Test and validate the tool's output outside of the agent system.<br>- Refine the defined parameters, prompts, and naming of tools.  |
| Multi-Agent system not performing consistently | - Refine prompts given to each agent to ensure they are specific and distinct from one another.<br>- Build a hierarchical system using a "routing" or controller agent to determine which agent is the correct one. |

Mnoho z těchto problémů lze identifikovat efektivněji s observabilitou na místě. Trace a metriky, o kterých jsme mluvili výše, pomáhají přesně určit, kde v pracovním postupu agenta problémy nastávají, což činí ladění a optimalizaci mnohem efektivnějšími.

## Managing Costs
Zde jsou některé strategie ke zvládání nákladů na nasazení AI agentů do produkce:

**Použití menších modelů:** Malé jazykové modely (SLMs) mohou v určitých agentních případech použití podávat dobrý výkon a výrazně sníží náklady. Jak bylo uvedeno dříve, vybudování evaluačního systému pro určení a porovnání výkonu oproti větším modelům je nejlepší způsob, jak pochopit, jak dobře se SLM osvědčí ve vašem případě použití. Zvažte použití SLM pro jednodušší úkoly jako klasifikace záměru nebo extrakce parametrů, zatímco větší modely vyhraďte pro složité uvažování.

**Použití směrovacího modelu:** Podobnou strategií je používat různorodost modelů a jejich velikostí. Můžete použít LLM/SLM nebo serverless funkci ke směrování požadavků podle jejich složitosti na nejvhodnější modely. To také pomůže snížit náklady a zároveň zajistit výkon tam, kde je potřeba. Například směrujte jednoduché dotazy na menší, rychlejší modely a drahé velké modely používejte pouze pro složité úlohy vyžadující uvažování.

**Kešování odpovědí:** Identifikace běžných požadavků a úkolů a poskytování odpovědí dříve, než projdou vaším agentním systémem, je dobrý způsob, jak snížit objem podobných požadavků. Můžete dokonce implementovat tok, který pomocí jednodušších AI modelů určí, jak moc se požadavek podobá vašim uloženým (kešovaným) požadavkům. Tato strategie může výrazně snížit náklady u často kladených dotazů nebo běžných pracovních postupů.

## Podívejme se, jak to funguje v praxi

V [ukázkovém notebooku této sekce](./code_samples/10-expense_claim-demo.ipynb) uvidíme příklady, jak můžeme použít nástroje pro observabilitu k monitorování a hodnocení našeho agenta.


### Máte další otázky ohledně AI agentů v produkci?

Připojte se k [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), abyste se setkali s ostatními studenty, zúčastnili se konzultačních hodin a získali odpovědi na své otázky týkající se AI agentů.

## Předchozí lekce

[Návrhový vzor metakognice](../09-metacognition/README.md)

## Další lekce

[Agentní protokoly](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, berte prosím na vědomí, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazné znění. Pro důležité informace se doporučuje využít profesionální lidský překlad. Nejsme odpovědní za jakákoli nedorozumění nebo chybné výklady vyplývající z použití tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->