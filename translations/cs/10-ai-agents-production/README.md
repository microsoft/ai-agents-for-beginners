# AI Agentů v produkci: Pozorovatelnost a hodnocení

[![AI Agentů v produkci](../../../translated_images/cs/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Jak se AI agenti posouvají od experimentálních prototypů k aplikacím v reálném světě, stává se důležitou schopnost porozumět jejich chování, sledovat jejich výkon a systematicky hodnotit jejich výstupy.

## Výukové cíle

Po dokončení této lekce budete vědět/jak pochopit:
- Základní koncepty pozorovatelnosti a hodnocení agentů
- Techniky pro zlepšení výkonu, nákladů a efektivity agentů
- Co a jak systematicky hodnotit své AI agenty
- Jak kontrolovat náklady při nasazení AI agentů do produkce
- Jak instrumentovat agenty postavené pomocí Microsoft Agent Framework

Cílem je vybavit vás znalostmi, které promění vaše „černé skříňky“ na transparentní, říditelné a spolehlivé systémy.

_**Poznámka:** Je důležité nasazovat AI agenty, kteří jsou bezpeční a důvěryhodní. Podívejte se také na lekci [Budování důvěryhodných AI agentů](../06-building-trustworthy-agents/README.md)._

## Trasování a span-y

Nástroje pro pozorovatelnost, jako jsou [Langfuse](https://langfuse.com/) nebo [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry), obvykle reprezentují běhy agentů jako trasy a span-y.

- **Trace (trasa)** představuje kompletní úkol agenta od začátku do konce (například zpracování uživatelského dotazu).
- **Spans (span-y)** jsou jednotlivé kroky v trase (například volání jazykového modelu nebo získání dat).

![Strom tras v Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Bez pozorovatelnosti může AI agent působit jako „černá skříňka“ – jeho vnitřní stav a uvažování jsou neprůhledné, což ztěžuje diagnostiku problémů nebo optimalizaci výkonu. S pozorovatelností se agenti stávají „skleněnými skříňkami“, které nabízejí transparentnost zásadní pro budování důvěry a zajištění správné funkce.

## Proč je pozorovatelnost důležitá v produkčním prostředí

Přechod AI agentů do produkčního prostředí přináší novou řadu výzev a požadavků. Pozorovatelnost už není „pěkný doplněk“ ale kritická schopnost:

*   **Ladění a analýza příčiny problémů:** Když agent selže nebo vygeneruje neočekávaný výstup, nástroje pozorovatelnosti poskytují stopy potřebné k lokalizaci zdroje chyby. To je zvláště důležité u složitých agentů, kteří mohou zahrnovat vícenásobná volání LLM, interakce s nástroji a podmíněnou logiku.
*   **Řízení latence a nákladů:** AI agenti často využívají LLM a další externí API, která jsou účtována za token nebo za volání. Pozorovatelnost umožňuje přesné sledování těchto volání, což pomáhá identifikovat operace, které jsou příliš pomalé nebo drahé. To umožňuje týmům optimalizovat podněty, vybrat efektivnější modely nebo přepracovat pracovní postupy pro řízení provozních nákladů a zajištění dobré uživatelské zkušenosti.
*   **Důvěra, bezpečnost a soulad:** V mnoha aplikacích je důležité zajistit, aby agenti jednali bezpečně a eticky. Pozorovatelnost poskytuje auditní stopu akcí a rozhodnutí agenta. To lze využít k detekci a zmírnění problémů, jako je injektáž podnětů (prompt injection), generování škodlivého obsahu nebo nesprávné zacházení s osobními identifikačními údaji (PII). Například si můžete prohlédnout trasy a pochopit, proč agent poskytl určitou odpověď nebo použil konkrétní nástroj.
*   **Smyčky kontinuálního zlepšování:** Data z pozorovatelnosti jsou základem iterativního vývojového procesu. Sledováním výkonu agentů v reálném světě mohou týmy identifikovat oblasti pro zlepšení, shromažďovat data pro dolaďování modelů a ověřovat dopad změn. Tím vzniká zpětná vazba, kde produkční poznatky z online hodnocení informují offline experimenty a zdokonalování, což vede k postupnému zlepšování výkonu agentů.

## Klíčové metriky ke sledování

Pro sledování a pochopení chování agentů by měly být sledovány různé metriky a signály. I když se konkrétní metriky mohou lišit podle účelu agenta, některé jsou univerzálně důležité.

Zde jsou některé z nejběžnějších metrik, které nástroje pozorovatelnosti monitorují:

**Latence:** Jak rychle agent reaguje? Dlouhé čekací doby negativně ovlivňují uživatelský zážitek. Měli byste měřit latenci pro úkoly a jednotlivé kroky sledováním běhů agentů. Například agent, kterému trvá 20 sekund na všechna volání modelu, může být zrychlen použitím rychlejšího modelu nebo paralelním spouštěním volání modelu.

**Náklady:** Jaké jsou náklady na jednu relaci běhu agenta? AI agenti spoléhají na volání LLM účtovaná za tokeny nebo externí API. Časté používání nástrojů nebo více podnětů může rychle zvýšit náklady. Například pokud agent volá LLM pětkrát pro marginální zlepšení kvality, měli byste posoudit, zda je náklad ospravedlnitelný, nebo zda by bylo lepší snížit počet volání či použít levnější model. Monitorování v reálném čase také pomáhá identifikovat neočekávané nárůsty (např. chyby způsobující nadměrné API smyčky).

**Chyby požadavků:** Kolik požadavků agent nezvládl? To může zahrnovat chyby API nebo neúspěšná volání nástrojů. Pro zvýšení robustnosti agenta v produkci můžete nastavit záložní mechanismy nebo opakování (fallbacks, retries). Například pokud je poskytovatel LLM A nedostupný, přepnete na poskytovatele LLM B jako zálohu.

**Uživatelská zpětná vazba:** Implementace přímých uživatelských hodnocení poskytuje cenné poznatky. To může zahrnovat explicitní hodnocení (👍palec nahoru/👎dolů, ⭐1-5 hvězdiček) nebo textové komentáře. Konzistentní negativní zpětná vazba by vás měla varovat, protože je to znak, že agent nefunguje podle očekávání.

**Implicitní uživatelská zpětná vazba:** Uživatelské chování poskytuje nepřímou zpětnou vazbu i bez explicitních hodnocení. Může to zahrnovat okamžité přeformulování otázky, opakované dotazy nebo klikání na tlačítko opakovat. Například pokud vidíte, že uživatelé opakovaně kladou stejnou otázku, je to známka, že agent nefunguje podle očekávání.

**Přesnost:** Jak často agent generuje správné nebo žádoucí výstupy? Definice přesnosti se liší (např. správnost řešení problému, přesnost vyhledávání informací, spokojenost uživatele). Prvním krokem je definovat, jak úspěch pro vašeho agenta vypadá. Přesnost můžete sledovat pomocí automatických kontrol, hodnotících skóre nebo označení dokončení úkolu. Například označení tras jako „úspěšné“ nebo „neúspěšné“.

**Automatizované hodnotící metriky:** Můžete také nastavit automatické hodnocení. Například můžete použít LLM k ohodnocení výstupu agenta, zda je užitečný, přesný nebo ne. Existuje také několik open source knihoven, které pomáhají hodnotit různé aspekty agenta. Např. [RAGAS](https://docs.ragas.io/) pro RAG agenty nebo [LLM Guard](https://llm-guard.com/) k detekci škodlivého jazyka či injektáže podnětů.

V praxi nejlepší pokrytí zdraví AI agenta poskytuje kombinace těchto metrik. V tomto kapitole [příklad notebooku](./code_samples/10-expense_claim-demo.ipynb) vám ukážeme, jak tyto metriky vypadají na reálných příkladech, ale nejprve se naučíme, jak vypadá typický hodnotící pracovní postup.

## Instrumentujte svého agenta

Pro sběr dat o trasování budete muset instrumentovat svůj kód. Cílem je instrumentovat kód agenta tak, aby emitoval trasy a metriky, které mohou být zachyceny, zpracovány a vizualizovány platformou pro pozorovatelnost.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) se stalo průmyslovým standardem pro pozorovatelnost LLM. Poskytuje sadu API, SDK a nástrojů pro generování, sběr a export telemetrických dat.

Existuje mnoho knihoven pro instrumentaci, které obalují existující rámce agentů a usnadňují export OpenTelemetry spanů do nástroje pro pozorovatelnost. Microsoft Agent Framework se nativně integruje s OpenTelemetry. Níže je příklad instrumentace agenta MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Spouštění agenta je sledováno automaticky
    pass
```

Příklad notebooku v této kapitole (./code_samples/10-expense_claim-demo.ipynb) ukáže, jak instrumentovat vašeho MAF agenta.

**Manuální vytváření spanů:** I když knihovny pro instrumentaci poskytují dobrý základ, často jsou potřeba podrobnější nebo vlastní informace. Můžete ručně vytvářet spany pro přidání vlastní aplikační logiky. Důležitější je, že můžete obohatit automaticky nebo ručně vytvořené spany o vlastní atributy (také známé jako tagy nebo metadata). Tyto atributy mohou obsahovat obchodně specifická data, mezivýpočty nebo jakýkoliv kontext užitečný pro ladění či analýzu, jako je `user_id`, `session_id` nebo `model_version`.

Příklad ručního vytváření tras a spanů s použitím [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Hodnocení agenta

Pozorovatelnost nám poskytuje metriky, ale hodnocení je proces analýzy těchto dat (a provádění testů) k určení, jak dobře AI agent funguje a jak může být vylepšen. Jinými slovy, jakmile máte tyto trasy a metriky, jak je použít k posouzení agenta a učinění rozhodnutí?

Pravidelné hodnocení je důležité, protože AI agenti jsou často nedeterminističtí a mohou se vyvíjet (prostřednictvím aktualizací nebo driftu chování modelu) – bez hodnocení byste nevěděli, zda váš „chytrý agent“ skutečně plní svou práci dobře, nebo zda došlo k regresi.

Existují dvě kategorie hodnocení AI agentů: **online hodnocení** a **offline hodnocení**. Oba jsou cenné a doplňují se. Obvykle začínáme offline hodnocením, protože je to minimální nezbytný krok před nasazením jakéhokoliv agenta.

### Offline hodnocení

![Položky datasetu v Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

To zahrnuje hodnocení agenta v kontrolovaném prostředí, typicky za použití testovacích datasetů, nikoli živých uživatelských dotazů. Používáte kurátorské datasety, kde znáte očekávaný výstup nebo správné chování, a poté na nich spouštíte svého agenta.

Například pokud jste vytvořili agenta pro slovní matematické úlohy, můžete mít [testovací dataset](https://huggingface.co/datasets/gsm8k) se 100 problémy s známými odpověďmi. Offline hodnocení se často provádí během vývoje (a může být součástí CI/CD pipeline) pro kontrolu zlepšení nebo zabránění regresím. Výhodou je, že je **opakovatelný a můžete získat jasné metriky přesnosti, protože máte pravdu o stavu věcí (ground truth)**. Můžete také simulovat uživatelské dotazy a měřit odpovědi agenta vůči ideálním odpovědím nebo používat automatické metriky, jak je popsáno výše.

Klíčovou výzvou offline hodnocení je zajistit, aby váš testovací dataset byl komplexní a zůstal relevantní – agent může na pevně daném testovacím setu fungovat dobře, ale v produkci narazit na velmi odlišné dotazy. Proto byste měli udržovat testovací sety aktualizované o nové okrajové případy a příklady, které odrážejí reálné scénáře. Užitečná je kombinace malých „smoke testů“ pro rychlé kontroly a větších hodnotících sad pro širší metriky výkonu.

### Online hodnocení

![Přehled metrik pozorovatelnosti](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

To odkazuje na hodnocení agenta v živém, reálném prostředí, tj. během skutečného používání v produkci. Online hodnocení zahrnuje sledování výkonu agenta při skutečných uživatelských interakcích a průběžnou analýzu výsledků.

Například můžete sledovat míru úspěšnosti, skóre spokojenosti uživatelů nebo jiné metriky na živém provozu. Výhodou online hodnocení je, že **zachytí věci, které byste v laboratorních podmínkách nemuseli očekávat** – můžete pozorovat drift modelu v čase (pokud efektivita agenta klesá, jak se mění vzory vstupů) a zachytit neočekávané dotazy nebo situace, které nebyly v testovacích datech. Poskytuje pravdivý obrázek o chování agenta v reálném světě.

Online hodnocení často zahrnuje sběr implicitní i explicitní zpětné vazby uživatelů, jak bylo popsáno, a možná i spuštění shadow testů nebo A/B testů (kde nová verze agenta běží paralelně k porovnání se starou). Výzvou je, že může být obtížné získat spolehlivé štítky nebo skóre pro živé interakce – můžete spoléhat na zpětnou vazbu uživatelů nebo na následné metriky (například zda uživatel klikl na výsledek).

### Kombinace obou

Online a offline hodnocení nejsou vzájemně vylučující; jsou velmi doplňkové. Poznatky z online monitoringu (např. nové typy uživatelských dotazů, kde agent selhává) lze využít pro rozšíření a zlepšení offline testovacích datasetů. Naopak agenti, kteří dobře fungují v offline testech, mohou být s větším confidence nasazeni a sledováni online.

Vlastně mnoho týmů přijímá smyčku:

_offline hodnocení -> nasazení -> online monitorování -> sběr nových případů selhání -> přidání do offline datasetu -> zdokonalení agenta -> opakování_.

## Běžné problémy

Při nasazování AI agentů do produkce můžete narazit na různé výzvy. Zde jsou některé běžné problémy a jejich možné řešení:

| **Problém**    | **Možné řešení**   |
| ------------- | ------------------ |
| AI agent neplní úkoly konzistentně | - Upřesněte podnět (prompt) předávaný AI agentovi; buďte jasní v cílech.<br>- Identifikujte, kde může pomoci rozdělení úkolů na dílčí úkoly a jejich zpracování více agenty. |
| AI agent padá do nekonečných smyček | - Zajistěte jasné podmínky ukončení, aby agent věděl, kdy proces zastavit.<br>- Pro složité úkoly vyžadující uvažování a plánování použijte větší model specializovaný na uvažovací úkoly. |
| Volání nástrojů AI agenta nefungují dobře | - Testujte a validujte výstupy nástrojů mimo systém agenta.<br>- Upřesněte definované parametry, podněty a názvy nástrojů. |
| Multi-agentní systém neplní úkoly konzistentně | - Vylepšete podněty předávané každému agentovi tak, aby byly specifické a odlišné.<br>- Vytvořte hierarchický systém s "routingem" nebo řídicím agentem, který rozhodne, který agent je správný. |

Mnoho těchto problémů lze efektivněji identifikovat při zapnuté pozorovatelnosti. Trasy a metriky, které jsme probírali dříve, pomáhají přesně lokalizovat, kde v pracovním postupu agenta problémy nastávají, což činí ladění a optimalizaci mnohem efektivnějšími.

## Řízení nákladů


Zde je několik strategií, jak zvládat náklady na nasazení AI agentů do produkce:

**Použití menších modelů:** Malé jazykové modely (SLM) mohou dobře fungovat u určitých agentních případů použití a výrazně snížit náklady. Jak již bylo zmíněno, vytvoření hodnotícího systému pro určení a porovnání výkonu vůči větším modelům je nejlepší způsob, jak pochopit, jak dobře se SLM osvědčí ve vašem případě použití. Zvažte použití SLM pro jednodušší úkoly, jako je klasifikace záměru nebo extrakce parametrů, zatímco větší modely vyhraďte pro složité rozumování.

**Použití routerového modelu:** Podobnou strategií je využití rozmanitosti modelů a velikostí. Můžete použít LLM/SLM nebo serverless funkci k směrování požadavků na základě složitosti do nejvhodnějších modelů. To také pomůže snížit náklady a zároveň zajistit výkon u správných úkolů. Například nasměrujte jednoduché dotazy na menší, rychlejší modely a drahé velké modely použijte jen pro složité úkoly rozumování.

**Ukládání odpovědí do cache:** Identifikace běžných požadavků a úkolů a poskytování odpovědí dříve, než projdou vaším agentním systémem, je dobrý způsob, jak snížit objem podobných požadavků. Můžete dokonce implementovat tok, který identifikuje, jak moc je požadavek podobný vašim uloženým požadavkům pomocí jednodušších AI modelů. Tato strategie může výrazně snížit náklady u často kladených otázek nebo běžných pracovních postupů.

## Podívejme se, jak to funguje v praxi

V [ukázkovém notebooku této sekce](./code_samples/10-expense_claim-demo.ipynb) uvidíme příklady, jak můžeme použít nástroje pro sledování a vyhodnocování našeho agenta.


### Máte další otázky ohledně AI agentů v produkci?

Přidejte se na [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), kde se můžete setkat s dalšími studenty, účastnit se konzultačních hodin a nechat si zodpovědět své otázky o AI agentech.

## Předchozí lekce

[Metacognition Design Pattern](../09-metacognition/README.md)

## Další lekce

[Agentic Protocols](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->