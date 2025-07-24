<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8164484c16b1ed3287ef9dae9fc437c1",
  "translation_date": "2025-07-24T08:58:26+00:00",
  "source_file": "10-ai-agents-production/README.md",
  "language_code": "cs"
}
-->
# AI agenti v produkci: Observabilita a hodnocení

Jakmile se AI agenti přesunou z experimentálních prototypů do reálných aplikací, stává se klíčovou schopnost porozumět jejich chování, monitorovat jejich výkon a systematicky hodnotit jejich výstupy.

## Cíle lekce

Po dokončení této lekce budete vědět, jak:
- Porozumět základním konceptům observability a hodnocení agentů
- Používat techniky ke zlepšení výkonu, nákladů a efektivity agentů
- Systematicky hodnotit vaše AI agenty – co a jak hodnotit
- Řídit náklady při nasazování AI agentů do produkce
- Instrumentovat agenty vytvořené pomocí AutoGen

Cílem je vybavit vás znalostmi, které promění vaše "černé skříňky" na transparentní, spravovatelné a spolehlivé systémy.

_**Poznámka:** Je důležité nasazovat AI agenty, kteří jsou bezpeční a důvěryhodní. Podívejte se na lekci [Budování důvěryhodných AI agentů](./06-building-trustworthy-agents/README.md)._

## Traces a spans

Nástroje pro observabilitu, jako [Langfuse](https://langfuse.com/) nebo [Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry), obvykle reprezentují běhy agentů jako traces a spans.

- **Trace** představuje kompletní úkol agenta od začátku do konce (například zpracování dotazu uživatele).
- **Spans** jsou jednotlivé kroky uvnitř trace (například volání jazykového modelu nebo získávání dat).

![Strom trace v Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)

Bez observability může AI agent působit jako "černá skříňka" – jeho vnitřní stav a uvažování jsou neprůhledné, což ztěžuje diagnostiku problémů nebo optimalizaci výkonu. S observabilitou se agenti stávají "skleněnými skříňkami", které nabízejí transparentnost nezbytnou pro budování důvěry a zajištění správného fungování.

## Proč je observabilita důležitá v produkčním prostředí

Přechod AI agentů do produkčního prostředí přináší nové výzvy a požadavky. Observabilita již není jen "pěkný doplněk", ale klíčová schopnost:

*   **Ladění a analýza příčin problémů**: Když agent selže nebo poskytne neočekávaný výstup, nástroje pro observabilitu poskytují traces potřebné k identifikaci zdroje chyby. To je obzvláště důležité u komplexních agentů, kteří mohou zahrnovat více volání LLM, interakce s nástroji a podmíněnou logiku.
*   **Řízení latence a nákladů**: AI agenti často spoléhají na LLM a další externí API, která jsou účtována za token nebo za volání. Observabilita umožňuje přesné sledování těchto volání, což pomáhá identifikovat operace, které jsou příliš pomalé nebo drahé. To umožňuje týmům optimalizovat prompty, vybrat efektivnější modely nebo přepracovat pracovní postupy, aby řídily provozní náklady a zajistily dobrý uživatelský zážitek.
*   **Důvěra, bezpečnost a shoda**: V mnoha aplikacích je důležité zajistit, aby agenti jednali bezpečně a eticky. Observabilita poskytuje auditní stopu akcí a rozhodnutí agenta. To lze použít k detekci a zmírnění problémů, jako je injekce promptů, generování škodlivého obsahu nebo nesprávné nakládání s osobními údaji (PII). Například můžete přezkoumat traces, abyste pochopili, proč agent poskytl určitou odpověď nebo použil konkrétní nástroj.
*   **Smyčky kontinuálního zlepšování**: Data z observability jsou základem iterativního vývojového procesu. Sledováním výkonu agentů v reálném světě mohou týmy identifikovat oblasti pro zlepšení, shromažďovat data pro doladění modelů a ověřovat dopad změn. To vytváří zpětnou vazbu, kde produkční poznatky z online hodnocení informují offline experimenty a zdokonalování, což vede k postupně lepšímu výkonu agentů.

## Klíčové metriky ke sledování

Pro monitorování a pochopení chování agentů by měly být sledovány různé metriky a signály. Ačkoli konkrétní metriky se mohou lišit podle účelu agenta, některé jsou univerzálně důležité.

Zde jsou některé z nejběžnějších metrik, které nástroje pro observabilitu sledují:

**Latence:** Jak rychle agent reaguje? Dlouhé čekací doby negativně ovlivňují uživatelský zážitek. Latenci byste měli měřit jak pro úkoly, tak pro jednotlivé kroky sledováním běhů agenta. Například agent, který potřebuje 20 sekund na všechna volání modelu, by mohl být zrychlen použitím rychlejšího modelu nebo paralelním spuštěním volání modelu.

**Náklady:** Jaké jsou náklady na jeden běh agenta? AI agenti spoléhají na volání LLM účtovaná za token nebo externí API. Časté používání nástrojů nebo více promptů může rychle zvýšit náklady. Například pokud agent volá LLM pětkrát pro marginální zlepšení kvality, musíte posoudit, zda jsou náklady oprávněné, nebo zda můžete snížit počet volání či použít levnější model. Monitorování v reálném čase může také pomoci identifikovat neočekávané špičky (např. chyby způsobující nadměrné smyčky API).

**Chyby požadavků:** Kolik požadavků agent selhal? To může zahrnovat chyby API nebo neúspěšná volání nástrojů. Aby byl váš agent v produkci odolnější vůči těmto chybám, můžete nastavit záložní mechanismy nebo opakování. Např. pokud je poskytovatel LLM A nedostupný, přepnete na poskytovatele LLM B jako zálohu.

**Zpětná vazba uživatelů:** Implementace přímého hodnocení od uživatelů poskytuje cenné poznatky. To může zahrnovat explicitní hodnocení (👍palec nahoru/👎dolů, ⭐1-5 hvězdiček) nebo textové komentáře. Konzistentní negativní zpětná vazba by vás měla upozornit, protože to je známka toho, že agent nefunguje podle očekávání.

**Implicitní zpětná vazba uživatelů:** Chování uživatelů poskytuje nepřímou zpětnou vazbu i bez explicitního hodnocení. To může zahrnovat okamžité přeformulování otázky, opakované dotazy nebo kliknutí na tlačítko opakování. Např. pokud vidíte, že uživatelé opakovaně kladou stejnou otázku, je to známka toho, že agent nefunguje podle očekávání.

**Přesnost:** Jak často agent produkuje správné nebo žádoucí výstupy? Definice přesnosti se liší (např. správnost řešení problémů, přesnost získávání informací, spokojenost uživatelů). Prvním krokem je definovat, jak vypadá úspěch pro vašeho agenta. Přesnost můžete sledovat pomocí automatických kontrol, hodnotících skóre nebo štítků dokončení úkolů. Například označování traces jako "úspěšné" nebo "neúspěšné".

**Automatizované hodnotící metriky:** Můžete také nastavit automatizované hodnocení. Například můžete použít LLM k ohodnocení výstupu agenta, např. zda je užitečný, přesný nebo ne. Existuje také několik open source knihoven, které vám pomohou ohodnotit různé aspekty agenta. Např. [RAGAS](https://docs.ragas.io/) pro RAG agenty nebo [LLM Guard](https://llm-guard.com/) k detekci škodlivého jazyka nebo injekce promptů.

V praxi kombinace těchto metrik poskytuje nejlepší pokrytí zdraví AI agenta. V [ukázkovém notebooku](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb) této kapitoly vám ukážeme, jak tyto metriky vypadají na reálných příkladech, ale nejprve se naučíme, jak vypadá typický hodnotící pracovní postup.

## Instrumentace vašeho agenta

Pro sběr dat o trace budete muset instrumentovat váš kód. Cílem je instrumentovat kód agenta tak, aby emitoval traces a metriky, které mohou být zachyceny, zpracovány a vizualizovány platformou pro observabilitu.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) se stalo průmyslovým standardem pro observabilitu LLM. Poskytuje sadu API, SDK a nástrojů pro generování, sběr a export telemetrických dat.

Existuje mnoho knihoven pro instrumentaci, které obalují existující rámce agentů a usnadňují export OpenTelemetry spans do nástroje pro observabilitu. Níže je příklad instrumentace agenta AutoGen pomocí knihovny [OpenLit](https://github.com/openlit/openlit):

```python
import openlit

openlit.init(tracer = langfuse._otel_tracer, disable_batch = True)
```

[Ukázkový notebook](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb) v této kapitole ukáže, jak instrumentovat vašeho agenta AutoGen.

**Ruční vytváření spans:** Zatímco knihovny pro instrumentaci poskytují dobrý základ, často existují případy, kdy je potřeba podrobnější nebo vlastní informace. Můžete ručně vytvářet spans pro přidání vlastní aplikační logiky. Důležitější je, že mohou obohatit automaticky nebo ručně vytvořené spans o vlastní atributy (také známé jako tagy nebo metadata). Tyto atributy mohou zahrnovat obchodně specifická data, mezivýpočty nebo jakýkoli kontext, který může být užitečný pro ladění nebo analýzu, jako `user_id`, `session_id` nebo `model_version`.

Příklad ručního vytváření traces a spans pomocí [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Hodnocení agenta

Observabilita nám poskytuje metriky, ale hodnocení je proces analýzy těchto dat (a provádění testů) za účelem určení, jak dobře AI agent funguje a jak jej lze zlepšit. Jinými slovy, jakmile máte traces a metriky, jak je použít k posouzení agenta a rozhodování?

Pravidelné hodnocení je důležité, protože AI agenti jsou často nedeterminističtí a mohou se vyvíjet (prostřednictvím aktualizací nebo změn chování modelu) – bez hodnocení byste nevěděli, zda váš "chytrý agent" skutečně plní svou práci dobře nebo zda došlo k regresi.

Existují dvě kategorie hodnocení AI agentů: **online hodnocení** a **offline hodnocení**. Obě jsou cenná a vzájemně se doplňují. Obvykle začínáme s offline hodnocením, protože to je minimální nezbytný krok před nasazením jakéhokoli agenta.

### Offline hodnocení

![Položky datasetu v Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

To zahrnuje hodnocení agenta v kontrolovaném prostředí, obvykle pomocí testovacích datasetů, nikoli živých dotazů uživatelů. Používáte kurátorské datasety, kde víte, jaký je očekávaný výstup nebo správné chování, a poté na nich spustíte svého agenta.

Například pokud jste vytvořili agenta pro slovní úlohy z matematiky, můžete mít [testovací dataset](https://huggingface.co/datasets/gsm8k) se 100 problémy s známými odpověďmi. Offline hodnocení se často provádí během vývoje (a může být součástí CI/CD pipeline) k ověření zlepšení nebo ochraně proti regresím. Výhodou je, že je **opakovatelný a můžete získat jasné metriky přesnosti, protože máte referenční hodnoty**. Můžete také simulovat dotazy uživatelů a měřit odpovědi agenta vůči ideálním odpovědím nebo použít automatizované metriky, jak bylo popsáno výše.

Klíčovou výzvou u offline hodnocení je zajistit, aby váš testovací dataset byl komplexní a zůstal relevantní – agent může dobře fungovat na fixním testovacím setu, ale narazit na velmi odlišné dotazy v produkci. Proto byste měli testovací sety aktualizovat o nové hraniční případy a příklady, které odrážejí reálné scénáře​. Kombinace malých "smoke testů" a větších evaluačních setů je užitečná: malé sety pro rychlé kontroly a větší pro širší metriky výkonu​.

### Online hodnocení

![Přehled metrik observability](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

To se týká hodnocení agenta v živém, reálném prostředí, tj. během skutečného používání v produkci. Online hodnocení zahrnuje monitorování výkonu agenta na reálných interakcích uživatelů a průběžnou analýzu výsledků.

Například můžete sledovat míru úspěšnosti, skóre spokojenosti uživatelů nebo jiné metriky na živém provozu. Výhodou online hodnocení je, že **zachycuje věci, které byste v laboratorním prostředí nemuseli předvídat** – můžete pozorovat drift modelu v průběhu času (pokud se účinnost agenta zhoršuje, jak se mění vzory vstupů) a zachytit neočekávané dotazy nebo situace, které nebyly v testovacích datech​. Poskytuje skutečný obraz o tom, jak se agent chová v reálném světě.

Online hodnocení často zahrnuje sběr implicitní a explicitní zpětné vazby od uživatelů, jak bylo diskutováno, a případně provádění shadow testů nebo A/B testů (kde nová verze agenta běží paralelně pro porovnání se starou). Výzvou je, že může být obtížné získat spolehlivé štítky nebo skóre pro živé interakce – můžete se spoléhat na zpětnou vazbu uživatelů nebo na následné metriky (např. zda uživatel klikl na výsledek).

### Kombinace obou

Online a offline hodnocení nejsou vzájemně výlučné; jsou vysoce komplementární. Poznatky z online monitorování (např. nové typy dotazů uživatelů, kde agent funguje špatně) mohou být použity k rozšíření a zlepšení offline testovacích datasetů. Naopak agenti, kteří dobře fungují v offline testech, mohou být poté s větší jistotou nasazeni a monitorováni online.

Ve skutečnosti mnoho týmů přijímá smyčku:

_hodnotit offline -> nasadit -> monitorovat online -> sbírat nové případy selhání -> přidat do offline datasetu -> zdokonalit agenta -> opakovat_.

## Běžné problémy

Při nasazování AI agentů do produkce se můžete setkat s různými výzvami. Zde jsou některé běžné problémy a jejich možné řešení:

| **Problém**    | **Možné řešení**   |
| ------------- | ------------------ |
| AI agent neprovádí úkoly konzistentně | - Zjemněte prompt, který je agentovi zadán; buďte jasní ohledně cílů.<br>- Identifikujte, kde by rozdělení úkolů na dílčí úkoly a jejich zpracování více agenty mohlo pomoci. |
| AI agent se dostává do nekonečných smyček  | - Zajistěte, aby měl jasné podmínky ukončení, aby agent věděl, kdy proces zastavit.<br>- Pro složité úkoly vyžadující uvažování a plánování použijte větší model specializovaný na úkoly vyžadující uvažování. |
| Volání nástrojů AI agenta nefungují dobře   | - Otestujte a ověřte výstup nástroje mimo systém agenta. |

- Upřesněte definované parametry, výzvy a pojmenování nástrojů.  |
| Multi-agentní systém nefunguje konzistentně | - Upřesněte výzvy pro každého agenta, aby byly specifické a odlišné od sebe navzájem.<br>- Vytvořte hierarchický systém pomocí "směrovacího" nebo řídicího agenta, který určí, který agent je ten správný. |

Mnoho z těchto problémů lze efektivněji identifikovat, pokud je zavedena pozorovatelnost. Stopy a metriky, o kterých jsme mluvili dříve, pomáhají přesně určit, kde v pracovním postupu agenta dochází k problémům, což činí ladění a optimalizaci mnohem efektivnější.

## Řízení nákladů

Zde je několik strategií, jak řídit náklady na nasazení AI agentů do produkce:

**Používání menších modelů:** Malé jazykové modely (SLM) mohou dobře fungovat u některých agentních případů použití a výrazně sníží náklady. Jak bylo zmíněno dříve, vytvoření hodnoticího systému pro určení a porovnání výkonu oproti větším modelům je nejlepší způsob, jak pochopit, jak dobře bude SLM fungovat ve vašem případě použití. Zvažte použití SLM pro jednodušší úkoly, jako je klasifikace záměrů nebo extrakce parametrů, a větší modely si ponechte pro složitější úvahy.

**Používání směrovacího modelu:** Podobnou strategií je použití různorodých modelů a velikostí. Můžete použít LLM/SLM nebo serverless funkci k směrování požadavků na základě složitosti k nejvhodnějším modelům. To také pomůže snížit náklady a zároveň zajistit výkon u správných úkolů. Například směrujte jednoduché dotazy na menší, rychlejší modely a používejte drahé velké modely pouze pro složité úkoly vyžadující hlubší úvahy.

**Kešování odpovědí:** Identifikace běžných požadavků a úkolů a poskytování odpovědí předtím, než projdou vaším agentním systémem, je dobrý způsob, jak snížit objem podobných požadavků. Můžete dokonce implementovat proces, který identifikuje, jak podobný je požadavek vašim kešovaným požadavkům, pomocí základnějších AI modelů. Tato strategie může výrazně snížit náklady na často kladené otázky nebo běžné pracovní postupy.

## Podívejme se, jak to funguje v praxi

V [ukázkovém notebooku této sekce](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb) uvidíme příklady, jak můžeme použít nástroje pro pozorovatelnost k monitorování a hodnocení našeho agenta.

## Předchozí lekce

[Metakognitivní návrhový vzor](../09-metacognition/README.md)

## Další lekce

[MCP](../11-mcp/README.md)

**Prohlášení**:  
Tento dokument byl přeložen pomocí služby pro automatický překlad [Co-op Translator](https://github.com/Azure/co-op-translator). I když se snažíme o co největší přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Za autoritativní zdroj by měl být považován původní dokument v jeho původním jazyce. Pro důležité informace doporučujeme profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.