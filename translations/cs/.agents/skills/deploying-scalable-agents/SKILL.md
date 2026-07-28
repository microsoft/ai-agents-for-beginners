---
name: deploying-scalable-agents
license: MIT
---
# Nasazení škálovatelných agentů s Microsoft Foundry

> Doplňková dovednost k [Lekci 16 – Nasazení škálovatelných agentů](../../../16-deploying-scalable-agents/README.md).
> Použijte ji k pomoci studentovi přesunout agenta z prototypu do škálovatelného, 
> pozorovatelného produkčního nasazení. Každé doporučení zakládejte na obsahu lekce a
> spustitelném notebooku; nevymýšlejte API Foundry.

## Spouštěče

Aktivujte tuto dovednost, když chce student:
- Nasadit agenta do Microsoft Foundry jako **hostovaného agenta** a zajistit jeho verzování/pozorovatelnost.
- Vybrat mezi nasazovacími vzory **client-hosted, hosted-agent a agent-workflow**.
- Přidat **směrování modelů**, **cache odpovědí** nebo **omezenou paralelnost** pro kontrolu latence a nákladů.
- Přidat **evaluační bránu**, aby se špatná verze agenta nemohla nasadit.
- Přidat krok **schválení člověkem v procesu** pro akce s vysokým rizikem.
- Instrumentovat agenta **OpenTelemetry** trasováním pro produkční pozorovatelnost.
- Provést **smoke test** nasazeného agenta jako rychlou kontrolu po nasazení.

## Základní mentální model

Produkční agent je z velké části provozní kostra *kolem* modelu (~80%),
nikoli samotný model. Každé doporučení namapujte na jeden z těchto aspektů:

| Aspekt | Prototyp → Produkce |
|---------|---------------------|
| Hosting | notebook → verzovaná hostovaná služba |
| Identita | váš `az login` → spravovaná identita + omezena RBAC |
| Stav | v paměti → externí úložiště vláken/paměti |
| Selhání | traceback → opakování, záložní mechanismy, upozornění |
| Náklady | "několik centů" → sledované, směrované, cachované, rozpočtované |
| Kvalita | odhadování okem → automatizovaná evaluační brána |
| Důvěra | vy schvalujete → politika + člověk v procesu |

## Nasazovací vzory (vyberte jeden, nebo kombinujte)

1. **Client-hosted** — smyčka rozumování běží ve vašem procesu. Maximální kontrola; vlastníte škálování/stav.
2. **Hosted agent (Foundry Agent Service)** — Foundry hostuje smyčku, ukládá vlákna, vynucuje RBAC/bezpečnost obsahu, zobrazuje agenta v portálu. Méně kontroly, mnohem menší provozní povrch.
3. **Agent workflow** — více agentů/nástrojů složených do grafu s větvením, schvalovacími uzly a trvalými kontrolními body.

## Životní cyklus (smyčka, která agentovi umožňuje nasazení)

`create → version → evaluate (gate) → deploy hosted → observe online → collect failures → repeat`.
**Offline hodnocení je brána, nikoli dodatečná myšlenka** — verze se nenasazuje,
pokud neprojde nastaveným prahem. Online pozorovatelnost vrací skutečná selhání
zpět do offline testovací sady.

## Škálování a páky nákladů (v pořadí priority)

1. **Správná velikost modelu** — použijte nejmenší model, který projde evaluační bránou.
2. **Směrování podle složitosti** — malý/rychlý model pro jednoduché požadavky, velký model pro skutečné rozumování (vlastní klasifikátor nebo Foundry Model Router).
3. **Cache** — obsluhujte téměř duplicitní požadavky bez volání modelu.
4. **Bezustavový design + omezená paralelnost** — externě uložte stav; opakujte se zpožděním.

## Klíčové vzory k reprodukci

Nasměrujte studenta k těmto z notebooku
[`16-python-agent-framework.ipynb`](../../../16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb):

- **Obslužná funkce požadavků**: cache → směrování podle složitosti → trasovací span → spuštění → cache.
- **Evaluační brána**: vyhodnotit offline testovací sadu; vrátit `pass_rate >= threshold` a nasadit pouze, pokud je pravda.
- **Lidské schválení**: `@tool(approval_mode="always_require")` pro akce jako velké refundace.
- **Trasování**: zabalte každý požadavek do `tracer.start_as_current_span(...)` a nastavte atributy jako `routed.model`, `customer.id`.

## Smoke test nasazeného agenta

Po nasazení ověřte, že endpoint opravdu odpovídá (zelené nasazení může být stále
tiché). Použijte [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
akci přes [`.github/workflows/smoke-test.yml`](../../../../../.github/workflows/smoke-test.yml)
s katalogem v [`tests/`](../../../tests/README.md). Běhoun odesílá POST každého
promptu na `POST {project_endpoint}/agents/{agent_name}/endpoint/protocols/openai/responses`
a kontroluje odpověď textu. Identita potřebuje roli **Azure AI User** v rámci
rozsahu Foundry projektu; token audience musí být `https://ai.azure.com/`.

Naskládejte brány: **smoke test** (dosažitelnost/reakce, každý deploy) → **offline
hodnocení** (dostatečně dobré k nasazení, před propagací) → **online hodnocení** (jak si vede v provozu, kontinuálně).


## Podnikové kontroly

- **RBAC**: přiřaďte každému hostovanému agentovi spravovanou identitu s nejmenšími právy.
- **MCP v produkci**: považujte každý MCP server za nedůvěryhodnou hranici — připněte verzi, omezte jeho identitu, ověřujte výstupy, omezujte rychlost, nikdy nezveřejňujte tajné údaje.

## Bezpečnostní opatření pro asistenta

- Preferujte kanonický vzor `FoundryChatClient(...)` + `provider.as_agent(...)` používaný napříč kurzem.
- Neslibujte výsledky živého Azure, které jste neověřili; doporučte workflow smoke-testu k potvrzení nasazení.
- Držte hodnocení a rady ohledně nákladů propojené: hodnocení určuje kvalitativní standard, směrování/cachování drží náklady poblíž této úrovně.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->