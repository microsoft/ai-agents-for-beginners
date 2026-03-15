# AI agenti v produkci: Pozorovatelnost a hodnocení

[![AI agenti v produkci](../../../translated_images/cs/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Jak se AI agenti přesouvají z experimentálních prototypů do reálných aplikací, stává se schopnost porozumět jejich chování, sledovat jejich výkon a systematicky vyhodnocovat jejich výstupy důležitou.

## Cíle učení

Po dokončení této lekce budete vědět/rozumět:
- Základním pojmům pozorovatelnosti a hodnocení agentů
- Technice pro zlepšení výkonu, nákladů a efektivity agentů
- Co a jak systematicky hodnotit u svých AI agentů
- Jak kontrolovat náklady při nasazování AI agentů do produkce
- Jak instrumentovat agenty postavené s Microsoft Agent Framework

Cílem je vybavit vás znalostmi, jak přeměnit vaše „černé skříňky“ agentů na průhledné, snadno spravovatelné a spolehlivé systémy.

_**Poznámka:** Je důležité nasazovat AI agenty, kteří jsou bezpeční a důvěryhodní. Podívejte se také na lekci [Budování důvěryhodných AI agentů](./06-building-trustworthy-agents/README.md)._

## Traces and Spans

Observability nástroje jako [Langfuse](https://langfuse.com/) nebo [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) obvykle reprezentují běhy agentů jako traces a spans.

- **Trace** představuje kompletní úkol agenta od začátku do konce (např. zpracování dotazu uživatele).
- **Spans** jsou jednotlivé kroky uvnitř trace (např. volání modelu jazyka nebo načítání dat).

![Strom tras v Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Bez pozorovatelnosti může AI agent působit jako „černá skříňka“ – jeho interní stav a uvažování jsou neprůhledné, což ztěžuje diagnostiku problémů nebo optimalizaci výkonu. S pozorovatelností se agenti stávají „skleněnými krabičkami“, které nabízejí průhlednost nezbytnou pro budování důvěry a zajištění, že fungují podle očekávání.

## Proč je pozorovatelnost důležitá v produkčním prostředí

Přechod AI agentů do produkčních prostředí přináší novou sadu výzev a požadavků. Pozorovatelnost už není „hezké mít“, ale kritická schopnost:

*   **Ladění a analýza příčiny problému**: Když agent selže nebo vygeneruje neočekávaný výstup, nástroje pro pozorovatelnost poskytují trace potřebné k určení zdroje chyby. To je zvláště důležité u složitých agentů, které mohou zahrnovat více volání LLM, interakcí s nástroji a podmíněné logiky.
*   **Řízení latence a nákladů**: AI agenti často spoléhají na LLM a další externí API, která jsou účtována za token nebo za volání. Pozorovatelnost umožňuje přesné sledování těchto volání, což pomáhá identifikovat operace, které jsou nadměrně pomalé nebo drahé. To umožňuje týmům optimalizovat prompty, vybrat efektivnější modely nebo přepracovat pracovní toky, aby se snížily provozní náklady a zajistila dobrá uživatelská zkušenost.
*   **Důvěra, bezpečnost a shoda**: V mnoha aplikacích je důležité zajistit, aby agenti jednali bezpečně a eticky. Pozorovatelnost poskytuje auditní stopu akcí a rozhodnutí agenta. To lze využít k detekci a zmírnění problémů jako je prompt injection, generování škodlivého obsahu nebo nesprávné nakládání s osobně identifikovatelnými údaji (PII). Například můžete procházet traces, abyste pochopili, proč agent poskytl konkrétní odpověď nebo použil určitý nástroj.
*   **Cykly kontinuálního zlepšování**: Data z pozorovatelnosti jsou základem iterativního vývojového procesu. Sledováním toho, jak si agenti vedou v reálném světě, mohou týmy identifikovat oblasti pro zlepšení, získat data pro doladění modelů a ověřit dopad změn. To vytváří zpětnou vazbu, kde produkční poznatky z online hodnocení informují offline experimentování a doladění, což vede k postupnému zlepšování výkonu agenta.

## Klíčové metriky ke sledování

Pro monitorování a pochopení chování agentů by se měly sledovat různé metriky a signály. Konkrétní metriky se mohou lišit podle účelu agenta, ale některé jsou univerzálně důležité.

Zde jsou některé z nejběžnějších metrik, které nástroje pro pozorovatelnost sledují:

**Latence:** Jak rychle agent odpovídá? Dlouhé čekání negativně ovlivňuje uživatelskou zkušenost. Měli byste měřit latenci pro úkoly a jednotlivé kroky sledováním běhů agenta. Například agent, který potřebuje 20 sekund na všechna volání modelu, lze zrychlit použitím rychlejšího modelu nebo souběžným prováděním volání modelu.

**Náklady:** Jaké jsou náklady na jedno spuštění agenta? AI agenti spoléhají na volání LLM účtovaná za token nebo na externí API. Časté používání nástrojů nebo více promptů může náklady rychle zvýšit. Například pokud agent volá LLM pětkrát pro marginální zlepšení kvality, musíte posoudit, zda jsou náklady ospravedlněné, nebo zda byste mohli snížit počet volání či použít levnější model. Monitorování v reálném čase může také pomoci odhalit neočekávané špičky (např. chyby způsobující nadměrné API smyčky).

**Chyby požadavků:** Kolik požadavků agent selhal? To může zahrnovat chyby API nebo neúspěšná volání nástrojů. Aby byl váš agent v produkci odolnější vůči těmto problémům, můžete nastavit fallbacky nebo opakování. Např. pokud poskytovatel LLM A je nedostupný, přepnete na poskytovatele B jako zálohu.

**Zpětná vazba uživatelů:** Implementace přímého hodnocení uživateli poskytuje cenné poznatky. To může zahrnovat explicitní hodnocení (👍palec nahoru/👎dolů, ⭐1–5 hvězdiček) nebo textové komentáře. Konzistentně negativní zpětná vazba by vás měla varovat, protože to je známka, že agent nefunguje podle očekávání.

**Implicitní zpětná vazba uživatelů:** Chování uživatelů poskytuje nepřímou zpětnou vazbu i bez explicitního hodnocení. To může zahrnovat okamžité přeformulování otázky, opakované dotazy nebo kliknutí na tlačítko zkusit znovu. Např. pokud vidíte, že uživatelé opakovaně pokládají stejnou otázku, je to známka, že agent nefunguje podle očekávání.

**Přesnost:** Jak často agent produkuje správné nebo požadované výstupy? Definice přesnosti se liší (např. správnost řešení problémů, přesnost vyhledávání informací, spokojenost uživatele). Prvním krokem je definovat, jak úspěch pro vašeho agenta vypadá. Přesnost můžete sledovat pomocí automatických kontrol, evaluačních skóre nebo štítků dokončení úkolu. Například označování traces jako „succeeded“ nebo „failed“.

**Automatizované evaluační metriky:** Můžete také nastavit automatizované evaluace. Například můžete použít LLM k ohodnocení výstupu agenta, zda je nápomocný, přesný nebo nikoli. Existuje také několik open-source knihoven, které vám pomohou skórovat různé aspekty agenta. Např. [RAGAS](https://docs.ragas.io/) pro RAG agenty nebo [LLM Guard](https://llm-guard.com/) k detekci škodlivého jazyka nebo prompt injection.

V praxi dává kombinace těchto metrik nejlepší přehled o „zdraví“ AI agenta. V tomto kapitole [example notebook](./code_samples/10-expense_claim-demo.ipynb) vám ukážeme, jak tyto metriky vypadají na reálných příkladech, ale nejdříve si ukážeme, jak typický evaluační pracovní tok vypadá.

## Instrumentujte svého agenta

Pro shromažďování trace dat budete muset instrumentovat svůj kód. Cílem je instrumentovat kód agenta tak, aby emitoval traces a metriky, které mohou být zachyceny, zpracovány a vizualizovány platformou pro pozorovatelnost.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) se etablovalo jako průmyslový standard pro pozorovatelnost LLM. Poskytuje sadu API, SDK a nástrojů pro generování, sběr a export telemetry dat.

Existuje mnoho instrumentačních knihoven, které obalují existující agentní frameworky a usnadňují export OpenTelemetry spanů do nástroje pro pozorovatelnost. Microsoft Agent Framework se s OpenTelemetry integruje nativně. Níže je příklad instrumentace MAF agenta:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Vykonávání agenta je automaticky sledováno
    pass
```

The [example notebook](./code_samples/10-expense_claim-demo.ipynb) in this chapter will demonstrate how to instrument your MAF agent.

**Ruční vytváření spanů:** Zatímco instrumentační knihovny poskytují solidní základ, často jsou případy, kdy jsou potřeba podrobnější nebo vlastní informace. Můžete ručně vytvářet spany pro přidání vlastní aplikační logiky. Je důležitější, že mohou obohatit automaticky nebo ručně vytvořené spany o vlastní atributy (také známé jako tagy nebo metadata). Tyto atributy mohou zahrnovat obchodně-specifická data, mezivýpočty nebo jakýkoli kontext, který může být užitečný pro ladění nebo analýzu, například `user_id`, `session_id`, nebo `model_version`.

Example on creating traces and spans manually with the [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3): 

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Hodnocení agenta

Pozorovatelnost nám dává metriky, ale hodnocení je proces analýzy těchto dat (a provádění testů) za účelem určení, jak dobře si AI agent vede a jak jej lze zlepšit. Jinými slovy, jakmile máte traces a metriky, jak je použijete k ohodnocení agenta a rozhodování?

Pravidelné hodnocení je důležité, protože AI agenti jsou často nedeterminističtí a mohou se vyvíjet (prostřednictvím aktualizací nebo driftu chování modelu) – bez hodnocení byste nevěděli, zda váš „chytrý agent“ skutečně odvádí dobrou práci, nebo zda došlo ke zhoršení.

Existují dvě kategorie hodnocení AI agentů: **online hodnocení** a **offline hodnocení**. Obě jsou cenné a doplňují se. Obvykle začínáme offline hodnocením, protože je to minimální nezbytný krok před nasazením jakéhokoli agenta.

### Offline hodnocení

![Položky datové sady v Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

To zahrnuje hodnocení agenta v kontrolovaném prostředí, typicky pomocí testovacích datových sad, nikoli živých dotazů uživatelů. Používáte kurátorované datové sady, kde znáte očekávaný výstup nebo správné chování, a poté na nich spustíte agenta.

Například pokud jste vytvořili agenta pro slovní matematické úlohy, můžete mít [testovací datovou sadu](https://huggingface.co/datasets/gsm8k) 100 úloh se známými odpověďmi. Offline hodnocení se často provádí během vývoje (a může být součástí CI/CD pipeline) pro kontrolu zlepšení nebo ochranu proti regresím. Výhodou je, že je **opakovatelná a můžete získat jasné metriky přesnosti, protože máte ground truth**. Můžete také simulovat uživatelské dotazy a měřit odpovědi agenta vůči ideálním odpovědím nebo použít automatizované metriky, jak bylo popsáno výše.

Klíčovou výzvou offline eval je zajistit, aby vaše testovací datová sada byla komplexní a zůstávala relevantní – agent může na fixní testovací sadě fungovat dobře, ale v produkci narazit na velmi odlišné dotazy. Proto byste měli udržovat testovací sady aktualizované o nové hraniční případy a příklady, které odrážejí reálné scénáře​. Užitečná je směs malých „smoke testů“ a větších evaluačních sad: malé sady pro rychlé kontroly a větší pro širší metriky výkonu​.

### Online hodnocení 

![Přehled metrik pozorovatelnosti](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

To se týká hodnocení agenta v živém, reálném prostředí, tj. během skutečného používání v produkci. Online hodnocení zahrnuje monitorování výkonu agenta na reálných interakcích uživatelů a průběžnou analýzu výsledků.

Například můžete sledovat míru úspěšnosti, skóre spokojenosti uživatelů nebo jiné metriky na živém provozu. Výhodou online hodnocení je, že **zachytí věci, které v laboratorním prostředí nemusíte předvídat** – můžete pozorovat drift modelu v čase (pokud se efektivita agenta zhorší, jak se mění vzory vstupů) a zachytit neočekávané dotazy nebo situace, které ve vašich testovacích datech nebyly​. Poskytuje skutečný obraz toho, jak se agent chová v reálném světě.

Online hodnocení často zahrnuje sběr implicitní a explicitní zpětné vazby uživatelů, jak bylo diskutováno, a případně spouštění shadow testů nebo A/B testů (kde nová verze agenta běží paralelně pro porovnání se starou). Výzvou je, že může být složité získat spolehlivé štítky nebo skóre pro živé interakce – můžete se spolehnout na zpětnou vazbu uživatelů nebo downstream metriky (např. zda uživatel klikl na výsledek).

### Kombinace obou

Online a offline hodnocení nejsou navzájem se vylučující; vzájemně se doplňují. Poznatky z online monitorování (např. nové typy uživatelských dotazů, kde agent selhává) lze použít k rozšíření a vylepšení offline testovacích sad. Naopak agenti, kteří dobře uspějí v offline testech, mohou být s větší jistotou nasazeni a monitorováni online.

V praxi mnoho týmů přijímá smyčku:

_vyhodnotit offline -> nasadit -> monitorovat online -> sbírat nové chyby -> přidat do offline datasetu -> vylepšit agenta -> opakovat_.

## Běžné problémy

Při nasazování AI agentů do produkce se můžete setkat s různými výzvami. Zde jsou některé běžné problémy a jejich možná řešení:

| **Problém**    | **Možné řešení**   |
| ------------- | ------------------ |
| AI agent neplní úkoly konzistentně | - Upřesněte prompt zadaný AI agentovi; buďte jasní ohledně cílů.<br>- Identifikujte, zda rozdělení úkolů na podúkoly a jejich zpracování více agenty může pomoci. |
| AI agent uvízne v nekonečných smyčkách  | - Zajistěte jasné podmínky ukončení, aby agent věděl, kdy proces zastavit.<br>- Pro složité úkoly vyžadující uvažování a plánování použijte větší model specializovaný na úlohy z oblasti reasoning. |
| Volání nástrojů AI agenta nefungují dobře   | - Otestujte a ověřte výstup nástroje mimo systém agenta.<br>- Vyladěte definované parametry, prompty a pojmenování nástrojů.  |
| Systém s více agenty nefunguje konzistentně | - Upřesněte prompty každému agentovi, aby byly specifické a odlišné.<br>- Postavte hierarchický systém pomocí „routing“ nebo kontrolního agenta, který rozhodne, který agent je správný. |

Mnoho z těchto problémů lze efektivněji identifikovat s implementovanou pozorovatelností. Traces a metriky, o kterých jsme mluvili dříve, pomáhají přesně určit, kde v pracovním toku agenta k problémům dochází, což značně usnadňuje ladění a optimalizaci.

## Řízení nákladů
Zde je několik strategií, jak řídit náklady na nasazení AI agentů do produkce:

**Using Smaller Models:** Malé jazykové modely (SLMs) mohou dosahovat dobrých výsledků v určitých agentních použitích a výrazně snížit náklady. Jak bylo zmíněno dříve, vytvoření evaluačního systému pro určení a porovnání výkonu oproti větším modelům je nejlepší způsob, jak pochopit, jak dobře se SLM hodí pro váš konkrétní případ použití. Zvažte použití SLMs pro jednodušší úkoly, jako je klasifikace záměru nebo extrakce parametrů, a větší modely si ponechte pro složité úlohy vyžadující úvahu.

**Using a Router Model:** Podobná strategie je použít různorodost modelů a velikostí. Můžete použít LLM/SLM nebo serverless funkci k nasměrování požadavků podle složitosti na nejvhodnější modely. To také pomůže snížit náklady a zároveň zajistit výkon tam, kde je potřeba. Například nasměrujte jednoduché dotazy na menší, rychlejší modely a drahé velké modely používejte pouze pro složité úlohy vyžadující uvažování.

**Caching Responses:** Identifikace běžných požadavků a úkolů a poskytování odpovědí dříve, než projdou vaším agentním systémem, je dobrý způsob, jak snížit množství podobných požadavků. Dokonce můžete implementovat tok, který určí, jak moc je požadavek podobný těm v cache, pomocí jednodušších AI modelů. Tato strategie může výrazně snížit náklady na často kladené dotazy nebo běžné pracovní postupy.

## Podívejme se, jak to funguje v praxi

V [příkladovém notebooku této sekce](./code_samples/10-expense_claim-demo.ipynb) uvidíme příklady toho, jak můžeme použít nástroje pro observabilitu k monitorování a vyhodnocování našeho agenta.


### Máte další otázky ohledně AI agentů v produkci?

Připojte se k [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), setkejte se s ostatními studenty, účastněte se konzultačních hodin a získejte odpovědi na své otázky týkající se AI agentů.

## Předchozí lekce

[Vzor metakognice](../09-metacognition/README.md)

## Další lekce

[Agentní protokoly](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o vyloučení odpovědnosti**:
Tento dokument byl přeložen pomocí služby pro překlad založené na umělé inteligenci [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný. Pro kritické informace se doporučuje profesionální lidský překlad. Za žádná nedorozumění nebo chybné výklady vyplývající z použití tohoto překladu neneseme odpovědnost.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->