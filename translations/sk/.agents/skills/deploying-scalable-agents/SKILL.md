---
name: deploying-scalable-agents
license: MIT
---
# Nasadzovanie škálovateľných agentov s Microsoft Foundry

> Sprievodná zručnosť pre [Lekcia 16 – Nasadzovanie škálovateľných agentov](../../../16-deploying-scalable-agents/README.md).
> Použite ju na pomoc študentovi pri presune agenta z prototypu do škálovateľného, pozorovateľného
> produkčného nasadenia. Každé odporúčanie zakladajte na obsahu lekcie a
> spustiteľnom notebooku; nevymýšľajte API Foundry.

## Spúšťače

Aktivujte túto zručnosť, keď chce študent:
- Nasadiť agenta do Microsoft Foundry ako **hostovaného agenta** a spravovať ho verziami/pozorovateľnosťou.
- Vybrať medzi vzormi nasadenia **klient-hosted, hosted-agent a agent-workflow**.
- Pridať **smerovanie modelu**, **kešovanie odpovedí** alebo **obmedzenú paralelizáciu** na kontrolu latencie a nákladov.
- Pridať **evaluačnú bránu**, aby sa zlá verzia agenta nedostala do produkcie.
- Pridať krok **schválenia človekom v slučke** pre rizikové akcie.
- Instrumentovať agenta pomocou **OpenTelemetry** trasovania pre produkčnú pozorovateľnosť.
- **Rýchlo otestovať (smoke-test)** nasadeného agenta ako rýchlu bránu po nasadení.

## Základný mentálny model

Produkčný agent je prevažne operačný skelet *okolo* modelu (~80 %),
nie samotný model. Každé odporúčanie priraďte k jednému z týchto aspektov:

| Aspekt | Prototyp → Produkcia |
|--------|--------------------|
| Hosting | notebook → verziovaná hostovaná služba |
| Identita | váš `az login` → spravovaná identita + obmedzený RBAC |
| Stav | v pamäti → externé ukladanie vlákien/pamäte |
| Chyba | traceback → opakovania, záložné možnosti, upozornenia |
| Cena | "niekoľko centov" → sledovaná, smerovaná, kešovaná, rozpočtovaná |
| Kvalita | odhadovanie okom → automatizovaná evaluačná brána |
| Dôvera | vy schvaľujete → politika + človek v slučke |

## Vzory nasadenia (vyberte jeden alebo kombinujte)

1. **Klient-hosted** — slučka uvažovania beží vo vašom procese. Maximálna kontrola; vlastníte škálovanie/stav.
2. **Hostovaný agent (Foundry Agent Service)** — Foundry hostí slučku, ukladá vlákna, vynucuje RBAC/bezpečnosť obsahu, zobrazí agenta v portáli. Menej kontroly, oveľa menšia prevádzková plocha.
3. **Agent workflow** — viac agentov/nástrojov zložených do grafu s vetvením, schvaľovacími uzlami a trvalými kontrolnými bodmi.

## životný cyklus (slučka, ktorá dodáva agenta)

`create → version → evaluate (gate) → deploy hosted → observe online → collect failures → repeat`.
**Offline hodnotenie je brána, nie dodatočná myšlienka** — verzia sa nedodá
, pokiaľ neprejde prahom. Online pozorovateľnosť vracia skutočné chyby späť
do offline testovacej sady.

## Páky škálovania a nákladov (v poradí priority)

1. **Zvoliť vhodnú veľkosť modelu** — použiť najmenší model, ktorý prejde evaluačnou bránou.
2. **Smerovať podľa zložitosti** — malý/rýchly model pre jednoduché požiadavky, veľký model pre reálne uvažovanie (DIY klasifikátor alebo Foundry Model Router).
3. **Kešovať** — obslúžiť takmer duplicitné požiadavky bez volania modelu.
4. **Bezstavový dizajn + obmedzená paralelizácia** — externalizovať stav; opakovať s odkladom.

## Kľúčové vzory na reprodukciu

Ukážte študentovi tieto z notebooku
[`16-python-agent-framework.ipynb`](../../../16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb):

- **Spracovanie požiadaviek**: kešovať → smerovať podľa zložitosti → trasovací úsek → spustiť → kešovať.
- **Evaluačná brána**: ohodnotiť offline testovaciu sadu; vrátiť `pass_rate >= threshold` a nasadiť len ak je pravda.
- **Ľudské schválenie**: `@tool(approval_mode="always_require")` pre akcie ako veľké vrátenia.
- **Trasovanie**: obaliť každú požiadavku do `tracer.start_as_current_span(...)` a nastaviť atribúty ako `routed.model`, `customer.id`.

## Rýchlotestovanie (smoke-testing) nasadeného agenta

Po nasadení overte, že endpoint skutočne odpovedá (zelené nasadenie môže byť
tiché). Použite akciu [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
cez [`.github/workflows/smoke-test.yml`](../../../../../.github/workflows/smoke-test.yml)
s katalógom v [`tests/`](../../../tests/README.md). Spúšťač pošle POST pre každý
prompt na `POST {project_endpoint}/agents/{agent_name}/endpoint/protocols/openai/responses`
a preverí text odpovede. Identita potrebuje rolu **Azure AI User** v Foundry projekte; divák tokenu musí byť `https://ai.azure.com/`.


hodnotenie** (dostatočne dobrý na dodanie, pred propagáciou) → **online hodnotenie** (ako sa mu darí v reálnom prostredí, kontinuálne).



## Podnikové kontroly

- **RBAC**: každému hostovanému agentovi priraďte spravovanú identitu s minimálnymi oprávneniami.
- **MCP v produkcii**: každý MCP server považujte za neoverenú hranicu — pripnite verziu, ohraničte identitu, overujte výstupy, limitujte rýchlosť, nikdy neodhaľujte tajomstvá.

## Ochranné opatrenia pre asistenta

- Uprednostnite kanonický vzor `FoundryChatClient(...)` + `provider.as_agent(...)` používaný v celom kurze.
- Nesľubujte výsledky live-Azure, ktoré ste neoverili; odporučte workflow smoke-testu na overenie nasadenia.
- Držte rady ohľadom hodnotenia a nákladov spolu: hodnotenie nastavuje kvalitativny základ, smerovanie/kešovanie drží náklady blízko tohto základu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->