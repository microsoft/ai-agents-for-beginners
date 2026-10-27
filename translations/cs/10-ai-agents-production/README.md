# AI Agent v Produkci: Sledovatelnost a Hodnocení

[![AI Agents in Production](../../../translated_images/cs/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

Jak se AI agenti posouvají od experimentálních prototypů k reálným aplikacím, stává se důležitou schopnost pochopit jejich chování, sledovat jejich výkon a systematicky hodnotit jejich výstupy.

## Cíle učení

Po dokončení této lekce budete vědět, jak/rozumět:
- Základní pojmy sledovatelnosti a hodnocení agentů
- Techniky pro zlepšení výkonu, nákladů a efektivity agentů
- Co a jak systematicky hodnotit své AI agenty
- Jak kontrolovat náklady při nasazení AI agentů do produkce
- Jak instrumentovat agenty vytvořené pomocí Microsoft Agent Frameworku

Cílem je vybavit vás znalostmi, které přemění vaše "černé skříňky" agentů na průhledné, spravovatelné a spolehlivé systémy.

_**Poznámka:** Je důležité nasadit AI agenty, kteří jsou bezpeční a důvěryhodní. Podívejte se také na lekci [Building Trustworthy AI Agents](../06-building-trustworthy-agents/README.md)._

## Sledy a rozmezí

Nástroje pro sledovatelnost, jako jsou [Langfuse](https://langfuse.com/) nebo [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry), obvykle zobrazují běhy agentů jako stopy a rozmezí.

- **Stopa (Trace)** představuje kompletní úkol agenta od začátku do konce (například zpracování uživatelského dotazu).
- **Rozmezí (Spans)** jsou jednotlivé kroky uvnitř stopy (například volání jazykového modelu nebo získávání dat).

![Trace tree in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Bez sledovatelnosti může AI agent působit jako "černá skříňka" – jeho vnitřní stav a uvažování jsou neprůhledné, což ztěžuje diagnostiku problémů nebo optimalizaci výkonu. Se sledovatelností se agenti stávají "skleněnými skříňkami", nabízející průhlednost, která je zásadní pro budování důvěry a zajištění, že fungují podle očekávání.

## Proč je sledovatelnost důležitá v produkčním prostředí

Přechod AI agentů do produkčního prostředí přináší novou sadu výzev a požadavků. Sledovatelnost už není pouhým „hezkým doplňkem“, ale kritickou schopností:

*   **Ladění a analýza příčin chyb:** Když agent selže nebo vygeneruje neočekávaný výstup, nástroje pro sledovatelnost poskytují stopy potřebné k lokalizaci zdroje chyby. To je zvláště důležité u komplexních agentů, kteří mohou zahrnovat více volání LLM, interakce s nástroji a podmíněnou logiku.
*   **Řízení latence a nákladů:** AI agenti často využívají LLM a další externí API, která jsou účtována za token nebo volání. Sledovatelnost umožňuje přesné sledování těchto volání, pomáhá identifikovat operace, které jsou příliš pomalé nebo drahé. To umožňuje týmům optimalizovat promptování, vybrat efektivnější modely nebo přepracovat pracovní postupy pro řízení provozních nákladů a zajištění dobré uživatelské zkušenosti.
*   **Důvěra, bezpečnost a shoda:** V mnoha aplikacích je důležité zajistit, aby agenti jednali bezpečně a eticky. Sledovatelnost poskytuje auditní záznam akcí a rozhodnutí agentů. To lze použít k detekci a zmírnění problémů, jako jsou prompt injection, generování škodlivého obsahu nebo nesprávné zacházení s osobními údaji (PII). Například můžete prohlédnout stopy, abyste pochopili, proč agent poskytl určitou odpověď nebo použil konkrétní nástroj.
*   **Smyčky nepřetržitého zlepšování:** Data o sledovatelnosti jsou základem iterativního vývojového procesu. Sledováním výkonu agentů v reálném světě mohou týmy identifikovat oblasti ke zlepšení, sbírat data pro doladění modelů a ověřovat dopad změn. To vytváří zpětnovazební smyčku, kde poznatky z produkce získané online hodnocením informují offline experimenty a dolaďování, což vede k postupnému zlepšování výkonu agentů.

## Klíčové metriky ke sledování

Pro sledování a pochopení chování agentů by měla být sledována řada metrik a signálů. Specifické metriky se mohou lišit podle účelu agenta, ale některé jsou univerzálně důležité.

Zde jsou některé z nejběžnějších metrik, které nástroje pro sledovatelnost monitorují:

**Latence:** Jak rychle agent odpovídá? Dlouhé čekací doby negativně ovlivňují uživatelskou zkušenost. Měli byste měřit latenci pro úkoly a jednotlivé kroky sledováním běhů agentů. Například agent, který potřebuje 20 sekund na všechna volání modelu, může být zrychlen použitím rychlejšího modelu nebo paralelním voláním modelů.

**Náklady:** Jaké jsou náklady na jeden běh agenta? AI agenti spoléhají na volání LLM účtovaná za token nebo externí API. Časté používání nástrojů nebo více promptů může náklady rychle zvýšit. Například pokud agent volá LLM pětkrát kvůli marginálnímu zlepšení kvality, musíte posoudit, zda jsou náklady opodstatněné, nebo zda lze snížit počet volání nebo použít levnější model. Sledování v reálném čase může také pomoci identifikovat neočekávané špičky (např. chyby způsobující nadměrné smyčky API).

**Chyby požadavků:** Kolik požadavků agent nezvládl? To může zahrnovat chyby API nebo selhání volání nástrojů. Aby byl váš agent robustnější v produkci, můžete nastavit záložní plány nebo opakování. Například, pokud je poskytovatel LLM A nedostupný, přepnete na poskytovatele LLM B jako zálohu.

**Uživatelská zpětná vazba:** Zavedení přímého hodnocení uživateli poskytuje cenné informace. Může jít o explicitní hodnocení (👍palec nahoru/👎dolů, ⭐1-5 hvězd) nebo textové komentáře. Konzistentní negativní zpětná vazba by vás měla varovat, protože je to znak, že agent nefunguje podle očekávání.

**Implicitní uživatelská zpětná vazba:** Chování uživatelů poskytuje nepřímou zpětnou vazbu i bez explicitního hodnocení. Může zahrnovat okamžité přeformulování otázky, opakované dotazy nebo klikání na tlačítko opakovat. Například pokud vidíte, že uživatelé opakovaně pokládají stejnou otázku, je to znak, že agent nefunguje podle očekávání.

**Přesnost:** Jak často agent produkuje správné nebo žádoucí výstupy? Definice přesnosti se liší (např. správnost řešení problémů, přesnost vyhledávání informací, spokojenost uživatelů). Prvním krokem je definovat, jaký úspěch pro vašeho agenta znamená. Přesnost můžete sledovat automatickými kontrolami, hodnoticími skóre nebo štítky dokončení úkolů. Například označovat stopy jako „úspěšné“ nebo „neúspěšné“.

**Automatizované hodnoticí metriky:** Můžete také nastavit automatické hodnocení. Například můžete použít LLM k hodnocení výstupu agenta, jestli je užitečný, přesný nebo ne. Existuje také několik open source knihoven, které pomáhají hodnotit různé aspekty agenta. Např. [RAGAS](https://docs.ragas.io/) pro RAG agenty nebo [LLM Guard](https://github.com/protectai/llm-guard) k detekci škodlivého jazyka nebo prompt injection.

V praxi je kombinace těchto metrik nejlepší pokrytí zdraví AI agenta. V [příkladovém sešitu](./code_samples/10-expense_claim-demo.ipynb) v této kapitole vám ukážeme, jak tyto metriky vypadají v reálných příkladech, ale nejprve se naučíme, jak vypadá typický proces hodnocení.

## Instrumentujte svého Agenta

Pro sběr dat o sledování budete muset instrumentovat svůj kód. Cílem je instrumentovat kód agenta tak, aby emitoval stopy a metriky, které mohou být zachyceny, zpracovány a vizualizovány platformou pro sledovatelnost.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) se etabloval jako průmyslový standard pro sledovatelnost LLM. Poskytuje sadu API, SDK a nástrojů pro generování, sběr a export telemetrických dat.

Existuje mnoho knihoven pro instrumentaci, které obalují existující frameworky agentů a usnadňují export OpenTelemetry spanů do nástroje pro sledovatelnost. Microsoft Agent Framework se nativně integruje s OpenTelemetry. Níže je příklad instrumentace MAF agenta:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Agent execution is traced automatically
    pass
```

[příkladový sešit](./code_samples/10-expense_claim-demo.ipynb) v této kapitole demonstruje, jak instrumentovat svého MAF agenta.

**Manuální vytváření spanů:** Zatímco knihovny pro instrumentaci poskytují dobrý základ, často jsou potřeba podrobnější nebo vlastní informace. Můžete manuálně vytvářet spany pro přidání vlastní aplikační logiky. Důležitější je, že mohou obohatit automaticky nebo manuálně vytvořené spany o vlastní atributy (také známé jako tagy nebo metadata). Tyto atributy mohou zahrnovat obchodně specifická data, mezilehlé výpočty nebo jakýkoliv kontext, který může být užitečný pro ladění nebo analýzu, jako například `user_id`, `session_id`, nebo `model_version`.

Příklad manuálního vytváření stop a spanů s [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Hodnocení Agenta

Sledovatelnost nám dává metriky, ale hodnocení je proces analýzy těchto dat (a provádění testů) k určení, jak dobře AI agent funguje a jak může být zlepšen. Jinými slovy, jakmile máte ty stopy a metriky, jak je použít k posouzení agenta a rozhodování?

Pravidelné hodnocení je důležité, protože AI agenti jsou často nedeterminističtí a mohou se vyvíjet (prostřednictvím aktualizací nebo driftu modelového chování) – bez hodnocení byste nevěděli, jestli váš „chytrý agent“ skutečně plní svou práci dobře nebo zda došlo ke zhoršení.

Existují dvě kategorie hodnocení AI agentů: **online hodnocení** a **offline hodnocení**. Obě jsou cenné a doplňují se navzájem. Obvykle začínáme offline hodnocením, protože to je minimální nezbytný krok před nasazením jakéhokoli agenta.

### Offline hodnocení

![Dataset items in Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

To zahrnuje hodnocení agenta v kontrolovaném prostředí, typicky použitím testovacích datasetů, nikoli živými uživatelskými dotazy. Používáte kurátorské datasetové sady, kde znáte očekávaný výstup nebo správné chování, a pak agentovi tyto datasety spustíte.

Například pokud jste vytvořili agenta na řešení slovních matematických úloh, možná máte [testovací dataset](https://huggingface.co/datasets/openai/gsm8k) se 100 problémy s známými odpověďmi. Offline hodnocení se často provádí během vývoje (a může být součástí CI/CD pipeline) pro kontrolu zlepšení nebo zabránění regresím. Výhoda je, že je **opakovatelný a můžete získat jasné metriky přesnosti, protože máte „ground truth“**. Můžete také simulovat uživatelské dotazy a měřit odpovědi agenta vůči ideálním odpovědím či využít automatizované metriky, jak bylo popsáno výše.

Klíčovou výzvou offline hodnocení je zajistit, že váš testovací dataset je komplexní a zůstává relevantní – agent může na fixované testovací sadě fungovat dobře, ale v produkci může narazit na velmi odlišné dotazy. Proto byste měli testovací sady aktualizovat s novými okrajovými případy a příklady odrážejícími reálné scénáře. Kombinace malých „smoke testů“ a větších evaluačních sad je užitečná: malé sady pro rychlé kontroly a větší pro širší metriky výkonu.

### Online hodnocení

![Observability metrics overview](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

To znamená hodnocení agenta v živém, reálném prostředí, tj. během skutečného používání v produkci. Online hodnocení zahrnuje sledování výkonu agenta na reálných uživatelských interakcích a kontinuální analýzu výsledků.

Například můžete sledovat úspěšnost, skóre spokojenosti uživatelů nebo jiné metriky na živém provozu. Výhodou online hodnocení je, že **zachytí věci, které byste v laboratorním prostředí nečekali** – můžete pozorovat modelový drift v čase (pokud se efektivita agenta zhoršuje, jak se mění vzory vstupů) a odhalit neočekávané dotazy nebo situace, které nebyly ve vašich testovacích datech. Poskytuje skutečný obraz toho, jak agent funguje v reálném provozu.

Online hodnocení často zahrnuje sběr implicitní a explicitní uživatelské zpětné vazby, jak bylo uvedeno, a případně provozování shadow testů nebo A/B testů (kde nová verze agenta běží paralelně, aby se mohla porovnat se starou). Výzvou může být získání spolehlivých štítků nebo skóre pro živé interakce – můžete se spoléhat na uživatelskou zpětnou vazbu nebo downstream metriky (např. jestli uživatel kliknul na výsledek).

### Kombinace obou

Online a offline hodnocení nejsou vzájemně si vylučující; naopak se velmi doplňují. Poznatky z online sledování (např. nové typy uživatelských dotazů, kde agent selhává) lze využít k obohacení a zlepšení offline testovacích datasetů. Naopak agenti, kteří si vedou dobře v offline testech, mohou být pak s větší jistotou nasazeni a sledováni online.

Ve skutečnosti mnoho týmů přijímá smyčku:

_offline hodnocení -> nasazení -> online monitoring -> sběr nových selhání -> doplnění offline datasetu -> vylepšení agenta -> opakování_.

## Běžné problémy

Při nasazování AI agentů do produkce se můžete setkat s různými výzvami. Zde jsou některé běžné problémy a potenciální řešení:

| **Problém**    | **Možné řešení**   |
| ------------- | ------------------ |
| AI agent neplní úkoly konzistentně | - Upřesněte prompt daný AI agentovi; buďte jasní v cílech.<br>- Identifikujte situace, kde rozdělení úkolů na dílčí úkoly a jejich řešení více agenty může pomoci. |
| AI agent se dostává do nekonečných smyček | - Zajistěte jasné ukončovací podmínky, aby agent věděl, kdy proces ukončit.<br>- Pro složité úkoly vyžadující uvažování a plánování použijte větší model specializovaný na tyto úlohy. |
| Volání nástrojů AI agentem nefungují dobře | - Testujte a ověřujte výstupy nástrojů mimo systém agenta.<br>- Upřesněte parametry, prompty a pojmenování nástrojů. |
| Multi-agentní systém nefunguje konzistentně | - Upřesněte prompty každému agentovi, aby byly specifické a odlišné.<br>- Postavte hierarchický systém s „routing“ nebo řídícím agentem, který rozhoduje, který agent je správný. |

Mnoho těchto problémů lze efektivněji identifikovat se sledovatelností. Stopy a metriky, které jsme diskutovali dříve, pomáhají přesně určit, kde ve workflow agenta se problémy vyskytují, což výrazně ulehčuje ladění a optimalizaci.

## Řízení nákladů

Zde jsou některé strategie pro řízení nákladů při nasazování AI agentů do produkce:

**Používání menších modelů:** Malé jazykové modely (SLM) mohou dobře fungovat u určitých agentních případů použití a výrazně sníží náklady. Jak již bylo zmíněno dříve, nejlepší způsob, jak pochopit, jak dobře SLM na vašem použití bude fungovat, je postavit hodnoticí systém, který určí a porovná výkon s většími modely. Zvažte použití SLM pro jednodušší úkoly, jako je klasifikace záměrů nebo extrakce parametrů, přičemž větší modely vyhraďte pro složité uvažování.

**Použití routerového modelu:** Podobnou strategií je využití rozmanitosti modelů a velikostí. Můžete použít LLM/SLM nebo bezserverovou funkci pro směrování požadavků na základě složitosti k nejvhodnějším modelům. To také pomůže snížit náklady a zároveň zajistit výkon pro správné úkoly. Například směrujte jednoduché dotazy na menší, rychlejší modely a drahé velké modely používejte pouze pro složité úlohy uvažování.

**Ukládání odpovědí do vyrovnávací paměti:** Identifikace běžných požadavků a úkolů a poskytování odpovědí ještě předtím, než projdou vaším agentním systémem, je dobrý způsob, jak snížit objem podobných požadavků. Můžete dokonce implementovat tok, který pomocí jednodušších AI modelů zjistí, jak moc je požadavek podobný již uloženým požadavkům. Tato strategie může výrazně snížit náklady u často kladených dotazů nebo běžných pracovních postupů.

## Podívejme se, jak to funguje v praxi

V [ukázkovém notebooku této sekce](./code_samples/10-expense_claim-demo.ipynb) uvidíme příklady, jak můžeme použít nástroje pro observabilitu k monitorování a hodnocení našeho agenta.


### Máte další otázky ohledně AI agentů v produkci?

Připojte se k [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), setkejte se s dalšími studenty, navštěvujte konzultace a získejte odpovědi na své otázky týkající se AI agentů.

## Předchozí lekce

[Metacognition Design Pattern](../09-metacognition/README.md)

## Další lekce

[Agentic Protocols](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->