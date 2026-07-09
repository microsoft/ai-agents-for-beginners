# AI agenti v produkci: Pozorovatelnost a hodnocení

[![AI Agents in Production](../../../translated_images/cs/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Jak AI agenti postupují od experimentálních prototypů k reálným aplikacím, stává se důležitou schopnost porozumět jejich chování, monitorovat jejich výkon a systematicky hodnotit jejich výstupy.

## Cíle učení

Po dokončení této lekce budete znát/rozumět:
- Základním konceptům pozorovatelnosti a hodnocení agentů
- Techniky pro zlepšení výkonu, nákladů a efektivity agentů
- Co a jak systematicky hodnotit u vašich AI agentů
- Jak kontrolovat náklady při nasazení AI agentů do produkce
- Jak instrumentovat agenty postavené na Microsoft Agent Framework

Cílem je vybavit vás znalostmi, jak proměnit své "černé skříňky" agentů na průhledné, spravovatelné a spolehlivé systémy.

_**Poznámka:** Je důležité nasazovat AI agenty, kteří jsou bezpeční a důvěryhodní. Podívejte se také na lekci [Budování důvěryhodných AI agentů](../06-building-trustworthy-agents/README.md)._

## Trace a Spans

Nástroje pro pozorovatelnost, jako [Langfuse](https://langfuse.com/) nebo [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry), obvykle představují běhy agentů jako sledy (traces) a intervaly (spans).

- **Trace** představuje kompletní úkol agenta od začátku do konce (například zpracování uživatelského dotazu).
- **Spans** jsou jednotlivé kroky uvnitř trace (např. volání jazykového modelu nebo získávání dat).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Bez pozorovatelnosti může AI agent působit jako "černá skříňka" – jeho vnitřní stav a odůvodnění jsou neprůhledné, což ztěžuje diagnostiku problémů nebo optimalizaci výkonu. S pozorovatelností se agenti stávají "skleněnými skříňkami," které nabízejí průhlednost nezbytnou pro budování důvěry a zajištění správného fungování.

## Proč je pozorovatelnost důležitá v produkčním prostředí

Přechod AI agentů do produkčních prostředí přináší novou řadu výzev a požadavků. Pozorovatelnost již není jen "příjemným doplňkem", ale kritickou schopností:

*   **Ladění a analýza příčiny problému**: Když agent selže nebo vytvoří neočekávaný výstup, nástroje pozorovatelnosti poskytují sledy potřebné k určení zdroje chyby. To je zejména důležité u složitých agentů, kteří mohou volat více LLM, interagovat s nástroji a používat podmíněnou logiku.
*   **Správa latence a nákladů**: AI agenti často využívají LLM a další externí API, která jsou účtována za token nebo za volání. Pozorovatelnost umožňuje přesně sledovat tyto volání a pomáhá identifikovat operace, které jsou příliš pomalé nebo drahé. To umožňuje týmům optimalizovat prompty, vybrat efektivnější modely nebo přetvořit pracovní postupy za účelem snížení provozních nákladů a zajištění dobrého uživatelského zážitku.
*   **Důvěra, bezpečnost a soulad s předpisy**: V mnoha aplikacích je důležité zajistit, že agenti se chovají bezpečně a eticky. Pozorovatelnost poskytuje auditní stopu akcí a rozhodnutí agenta. Tuto stopu lze využít k detekci a zmírnění problémů, jako je vkládání škodlivých příkazů, generování škodlivého obsahu nebo nesprávné nakládání s osobními údaji (PII). Například můžete přezkoumat trace, abyste pochopili, proč agent poskytl určitou odpověď nebo použil konkrétní nástroj.
*   **Kontinuální smyčky zlepšování**: Data z pozorovatelnosti jsou základem iterativního vývojového procesu. Sledováním výkonu agentů v reálném světě mohou týmy identifikovat oblasti pro zlepšení, shromažďovat data pro doladění modelů a ověřovat dopad změn. To vytváří zpětnou vazbu, kde produkční poznatky z online hodnocení informují offline experimenty a úpravy, což vede k postupně lepšímu výkonu agentů.

## Klíčové metriky ke sledování

Pro sledování a pochopení chování agenta by mělo být sledováno množství metrik a signálů. Specifické metriky se mohou lišit podle účelu agenta, ale některé jsou univerzálně důležité.

Zde jsou některé z nejběžnějších metrik, které nástroje pozorovatelnosti sledují:

**Latence:** Jak rychle agent odpovídá? Dlouhé čekací doby negativně ovlivňují uživatelský zážitek. Měli byste měřit latenci pro úkoly a jednotlivé kroky sledováním běhů agenta. Například agent, který volá všechny modely 20 sekund, může být zrychlen použitím rychlejšího modelu nebo paralelním voláním modelů.

**Náklady:** Jaké jsou náklady na jeden běh agenta? AI agenti spoléhají na volání LLM, která jsou účtována za token, nebo na externí API. Časté používání nástrojů nebo více promptů může náklady rychle zvýšit. Například když agent provede pět volání LLM pro marginální zlepšení kvality, musíte posoudit, zda je náklad ospravedlněný, nebo zda byste mohli snížit počet volání či použít levnější model. Monitorování v reálném čase také pomáhá identifikovat nečekané špičky (např. chyby způsobující nadměrné API smyčky).

**Chyby požadavků:** Kolik požadavků agent nezvládl? Může to zahrnovat chyby API nebo neúspěšné volání nástrojů. Aby byl váš agent v produkci robustnější vůči těmto chybám, můžete nastavit záložní plány nebo opakování. Např. pokud je poskytovatel LLM A nedostupný, přepnete na poskytovatele LLM B jako zálohu.

**Uživatelská zpětná vazba:** Implementace přímých uživatelských hodnocení poskytuje cenné informace. To může zahrnovat explicitní hodnocení (👍palec nahoru/👎dolů, ⭐1-5 hvězdiček) nebo textové komentáře. Konzistentní negativní zpětná vazba vás má upozornit, protože je to znak toho, že agent nefunguje podle očekávání. 

**Implicitní uživatelská zpětná vazba:** Uživatelské chování poskytuje nepřímou zpětnou vazbu i bez explicitních hodnocení. Může zahrnovat okamžité přeformulování dotazu, opakované dotazy nebo kliknutí na tlačítko retry. Např. pokud vidíte, že uživatelé opakovaně kladou stejnou otázku, je to známka, že agent nepracuje podle očekávání.

**Přesnost:** Jak často agent produkuje správné nebo žádoucí výstupy? Definice přesnosti se liší (např. správnost řešení problému, přesnost vyhledávání informací, spokojenost uživatelů). Prvním krokem je definovat, jak vypadá úspěch pro vašeho agenta. Přesnost můžete sledovat pomocí automatických kontrol, hodnotících skóre nebo označení dokončení úkolů. Například označení trace jako "úspěšný" nebo "nepodařený".

**Automatizované evaluační metriky:** Můžete také nastavit automatizované hodnocení. Například můžete použít LLM ke skórování výstupu agenta, zda je užitečný, přesný nebo ne. K dispozici je také několik open-source knihoven, které vám pomohou skórovat různé aspekty agenta. Např. [RAGAS](https://docs.ragas.io/) pro RAG agenty nebo [LLM Guard](https://llm-guard.com/) k detekci škodlivého jazyka nebo vkládání škodlivých příkazů (prompt injection).

V praxi kombinace těchto metrik poskytuje nejlepší pokrytí zdraví AI agenta. V tomto kapitole [příkladovém notebooku](./code_samples/10-expense_claim-demo.ipynb) vám ukážeme, jak tyto metriky vypadají na reálných příkladech, ale nejdříve se naučíme, jak vypadá typický evaluační workflow.

## Instrumentujte svého agenta

Abyste získali data o trasování, musíte svůj kód instrumentovat. Cílem je instrumentovat kód agenta tak, aby vysílal trace a metriky, které lze zachytit, zpracovat a vizualizovat na platformě pro pozorovatelnost.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) se stal průmyslovým standardem pro pozorovatelnost LLM. Poskytuje sadu API, SDK a nástrojů pro generování, sběr a export telemetrických dat.

Existuje mnoho instrumentačních knihoven, které obalují stávající rámce agentů a usnadňují export OpenTelemetry spanů do nástroje pozorovatelnosti. Microsoft Agent Framework se s OpenTelemetry natívně integruje. Níže je příklad instrumentace agenta MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Provedení agenta je automaticky sledováno
    pass
```

[Příkladový notebook](./code_samples/10-expense_claim-demo.ipynb) v tomto kapitole ukáže, jak instrumentovat vašeho MAF agenta.

**Ruční tvorba spanů:** I když instrumentační knihovny poskytují dobrou základnu, často jsou potřeba podrobnější nebo vlastní informace. Span lze ručně vytvořit pro přidání vlastní aplikační logiky. Důležitější je, že mohou obohatit automaticky nebo ručně vytvořené spany o vlastní atributy (také známé jako tagy nebo metadata). Tyto atributy mohou zahrnovat specifická obchodní data, mezivýpočty nebo jakýkoliv kontext užitečný pro debuggování či analýzu, například `user_id`, `session_id` nebo `model_version`.

Příklad ručního vytváření trace a spanů s [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Hodnocení agenta

Pozorovatelnost nám dává metriky, ale hodnocení je proces analýzy těchto dat (a provádění testů), který určuje, jak dobře AI agent funguje a jak ho lze zlepšit. Jinými slovy, když máte tyto trace a metriky, jak je použijete k posouzení agenta a k rozhodování?

Pravidelné hodnocení je důležité, protože AI agenti jsou často nedeterminističtí a mohou se vyvíjet (skrze aktualizace nebo postupné změny chování modelu) – bez hodnocení byste nevěděli, zda váš „chytrý agent“ skutečně plní úkol dobře, nebo zda došlo k regresi.

Existují dvě kategorie hodnocení AI agentů: **online hodnocení** a **offline hodnocení**. Obě jsou cenné a doplňují se. Obvykle začínáme offline hodnocením, protože to je minimální nutný krok před nasazením jakéhokoliv agenta.

### Offline hodnocení

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

To znamená hodnocení agenta v kontrolovaném prostředí, typicky s testovacími datovými sadami, nikoliv se živými uživatelskými dotazy. Používáte připravené datové sady, kde znáte očekávaný výstup nebo správné chování, a pak na nich spustíte svého agenta.

Například pokud jste vytvořili agenta pro slovní matematické úlohy, můžete mít [testovací datovou sadu](https://huggingface.co/datasets/gsm8k) se 100 problémy se známými odpověďmi. Offline hodnocení se často provádí během vývoje (a může být součástí CI/CD pipeline) pro ověření vylepšení nebo ochranu proti regresím. Výhodou je, že je **opakovatelný a získáte jasné metriky přesnosti, protože máte pravdu (ground truth)**. Také můžete simulovat uživatelské dotazy a měřit odpovědi agenta vůči ideálním odpovědím nebo použít automatizované metriky, jak bylo popsáno výše.

Klíčovou výzvou offline hodnocení je zajistit, že vaše testovací data jsou komplexní a zůstávají relevantní – agent může fungovat dobře na pevné testovací sadě, ale v produkci narazit na velmi odlišné dotazy. Proto byste měli testovací sady aktualizovat o nové hraniční případy a příklady, které odrážejí reálné scénáře. Je užitečné mít kombinaci malých „smoke testů“ a větších evaluačních sad: malé sady pro rychlé kontroly a větší pro širší metriky výkonu.

### Online hodnocení 

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

To se týká hodnocení agenta v živém, reálném prostředí, tedy během skutečného používání v produkci. Online hodnocení zahrnuje sledování výkonu agenta při reálné uživatelské interakci a průběžnou analýzu výsledků.

Například můžete sledovat úspěšnost, skóre spokojenosti uživatelů nebo jiné metriky na živém provozu. Výhodou online hodnocení je, že **zachytí věci, které byste v laboratorním prostředí nemuseli očekávat** – můžete pozorovat drift modelu v čase (pokud efektivita agenta klesá s posunem vzorů vstupů) a odhalit neočekávané dotazy nebo situace, které nebyly v testovacích datech. Poskytuje skutečný obraz chování agenta ve skutečném světě.

Online hodnocení často zahrnuje sběr implicitní i explicitní uživatelské zpětné vazby, jak bylo zmíněno, a možná běh shadow testů nebo A/B testů (kde nová verze agenta běží paralelně pro srovnání se starou). Výzvou je, že může být obtížné získat spolehlivé štítky nebo skóre pro živé interakce – možná se musíte spolehnout na uživatelskou zpětnou vazbu nebo metriky napříč hodnocením (např. zda uživatel klikl na výsledek).

### Kombinování obou

Online a offline hodnocení se nevylučují, jsou velmi doplňující. Poznatky z online monitoringu (např. nové typy uživatelských dotazů, kde agent funguje špatně) lze použít k rozšíření a zlepšení offline testovacích datových sad. Naopak agenti, kteří dobře fungují v offline testech, mohou být s větší jistotou nasazeni a sledováni online.

Mnoho týmů v praxi používá smyčku:

_offline hodnocení -> nasazení -> online monitoring -> sběr nových selhání -> přidání do offline datové sady -> zdokonalení agenta -> opakovat_.

## Časté problémy

Při nasazování AI agentů do produkce můžete narazit na různé výzvy. Zde jsou některé běžné problémy a jejich možná řešení:

| **Problém**    | **Možné řešení**   |
| ------------- | ------------------ |
| AI agent nekonzistentně plní úkoly | - Upřesněte prompt, který agentovi dáváte; buďte jasní v cílech.<br>- Identifikujte situace, kdy je výhodné rozdělit úkoly na dílčí a ty řešit více agenty. |
| AI agent se dostává do nekonečných smyček | - Zajistěte jasné podmínky ukončení, aby agent věděl, kdy přestat.<br>- U složitých úloh s vyžadovaným uvažováním a plánováním použijte větší model specializovaný na tyto úkoly. |
| Volání nástrojů AI agentem nefungují dobře  | - Testujte a ověřte výstupy nástroje mimo systém agenta.<br>- Upřesněte parametry, prompty a pojmenování nástrojů.  |
| Multi-agentní systém nekonzistentně funguje | - Upřesněte prompt pro každého agenta, aby byly specifické a odlišné.<br>- Vytvořte hierarchický systém s "směrovacím" nebo řídícím agentem, který rozhoduje, který agent je ten správný. |

Mnoho těchto problémů lze efektivněji odhalit pomocí pozorovatelnosti. Trace a metriky, které jsme popsali výše, pomáhají přesně určit, kde v pracovním postupu agenta problémy vznikají, což výrazně usnadňuje ladění a optimalizaci.

## Řízení nákladů


Zde je několik strategií, jak zvládat náklady na nasazení AI agentů do produkce:

**Používání menších modelů:** Malé jazykové modely (SLM) mohou dobře fungovat u některých agentických případů použití a výrazně sníží náklady. Jak již bylo zmíněno dříve, vytvoření hodnoticího systému pro určení a porovnání výkonu oproti větším modelům je nejlepší způsob, jak pochopit, jak dobře SLM bude fungovat ve vašem případě použití. Zvažte použití SLM pro jednodušší úkoly, jako je klasifikace záměrů nebo extrakce parametrů, zatímco větší modely ponechejte pro složité uvažování.

**Používání routerového modelu:** Podobná strategie je využívat různorodost modelů a velikostí. Můžete použít LLM/SLM nebo bezserverovou funkci k nasměrování požadavků na základě složitosti na nejvhodnější modely. To také pomůže snížit náklady a zároveň zajistit výkon na správných úkolech. Například směrujte jednoduché dotazy na menší, rychlejší modely a drahé velké modely používejte pouze pro složité úkoly uvažování.

**Cacheování odpovědí:** Identifikace běžných požadavků a úkolů a poskytování odpovědí ještě před tím, než projdou vaším agentickým systémem, je dobrý způsob, jak snížit objem podobných požadavků. Můžete dokonce implementovat tok, který identifikuje, jak podobný je požadavek těm, které máte uložené v cache, pomocí jednodušších AI modelů. Tato strategie může výrazně snížit náklady u často kladených otázek nebo běžných pracovních postupů.

## Podívejme se, jak to funguje v praxi

V [příkladovém notebooku této sekce](./code_samples/10-expense_claim-demo.ipynb) uvidíme příklady, jak můžeme použít nástroje pro observabilitu k monitorování a hodnocení našeho agenta.


### Máte další otázky ohledně AI agentů v produkci?

Připojte se k [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kde se setkáte s dalšími studenty, můžete navštívit konzultační hodiny a získat odpovědi na své otázky ohledně AI agentů.

## Předchozí lekce

[Design Pattern Metakognice](../09-metacognition/README.md)

## Následující lekce

[Agentické protokoly](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->