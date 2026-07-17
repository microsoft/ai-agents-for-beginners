---
name: deploying-scalable-agents
license: MIT
---
# Postavljanje skalabilnih agenata s Microsoft Foundryjem

> Prateća vještina za [Lekcija 16 – Postavljanje skalabilnih agenata](../../../16-deploying-scalable-agents/README.md).
> Koristite je da pomognete učeniku da premjesti agenta iz prototipa u skalabilnu, promatrivu
> produkcijsku implementaciju. Svaku preporuku utemeljite na sadržaju lekcije i
> izvršivoj bilježnici; ne izmišljajte Foundry API-je.

## Okidači

Aktivirajte ovu vještinu kada učenik želi:
- Implementirati agenta u Microsoft Foundry kao **hostanog agenta** i učiniti ga verzioniranim/promatrivim.
- Izabrati između obrazaca implementacije **client-hosted, hosted-agent i agent-workflow**.
- Dodati **usmjeravanje modela**, **keširanje odgovora** ili **ograničenu konkurentnost** za kontrolu latencije i troškova.
- Dodati **vratilo za evaluaciju** tako da se loša verzija agenta ne može isporučiti.
- Dodati korak **odobrenja čovjeka u petlji** za radnje visokog rizika.
- Instrumentirati agenta s **OpenTelemetry** praćenjem za produkcijsku promatrivost.
- **Smoke-testirati** implementiranog agenta kao brzu provjeru nakon implementacije.

## Osnovni mentalni model

Produkcijski agent je uglavnom operativni okvir *oko* modela (~80%),
ne sam model. Svaku preporuku povezujte s jednom od ovih briga:

| Briga | Prototip → Produkcija |
|---------|------------------------|
| Hosting | bilježnica → verzionirana hostana usluga |
| Identitet | vaš `az login` → upravljani identitet + ograničeni RBAC |
| Stanje | u memoriji → eksternalizirano spremište dretvi/memorije |
| Pogreške | praćenje staza → ponovni pokušaji, povratne opcije, upozorenja |
| Trošak | "nekoliko centi" → praćeno, usmjereno, keširano, planirano |
| Kvaliteta | procjena golim okom → automatizirani evaluacijski prag |
| Povjerenje | vaše odobrenje → politika + čovjek u petlji |

## Obrasci implementacije (izaberite jedan ili kombinirajte)

1. **Client-hosted** — petlja rezoniranja radi u vašem procesu. Maksimalna kontrola; vi upravljate skaliranjem/stanjem.
2. **Hosted agent (Foundry Agent Service)** — Foundry hosta petlju, pohranjuje dretve, provodi RBAC/sigurnost sadržaja, prikazuje agenta u portalu. Manje kontrole, znatno manja operativna složenost.
3. **Agent workflow** — više agenata/alata sastavljeno u graf s razgranatostima, odobrenjima i trajnim kontrolnim točkama.

## Životni ciklus (petlja koja isporučuje agenta)

`create → version → evaluate (vratilo) → deploy hosted → observe online → collect failures → repeat`.
**Offline evaluacija je vratilo, nije naknadna misao** — verzija se ne isporučuje
osim ako ne prođe prag. Online promatrivost vraća stvarne pogreške
natrag u offline testni skup.

## Poluge skaliranja i troškova (po prioritetu)

1. **Prilagodite veličinu modela** — koristite najmanji model koji prolazi evaluacijski prag.
2. **Usmjeravanje prema složenosti** — mali/brzi modeli za jednostavne zahtjeve, veliki modeli za stvarno rezoniranje (DIY klasifikator ili Foundry Model Router).
3. **Keširanje** — uslužite gotovo-identične zahtjeve bez poziva modelu.
4. **Bezustvni dizajn + ograničena konkurentnost** — eksternalizirajte stanje; pokušajte ponovo s odgodom.

## Ključni obrasci za reprodukciju

Uputite učenika na sljedeće iz bilježnice
[`16-python-agent-framework.ipynb`](../../../16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb):

- **Obrada zahtjeva**: keš → usmjeri prema složenosti → pratite opseg → izvrši → keš.
- **Evaluacijsko vratilo**: ocijenite offline testni skup; vratite `pass_rate >= threshold` i implementirajte samo ako je točno.
- **Ljudsko odobrenje**: `@tool(approval_mode="always_require")` za radnje poput velikih povrata.
- **Praćenje**: obavijte svaki zahtjev s `tracer.start_as_current_span(...)` i postavite atribute poput `routed.model`, `customer.id`.

## Smoke-testiranje implementiranog agenta

Nakon implementacije provjerite da endpoint zaista odgovara (zelena implementacija može biti
tiha). Koristite [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
akciju putem [`.github/workflows/smoke-test.yml`](../../../../../.github/workflows/smoke-test.yml)
s katalogom u [`tests/`](../../../tests/README.md). Izvršitelj šalje svaki
prompt na `POST {project_endpoint}/agents/{agent_name}/endpoint/protocols/openai/responses`
i provjerava tekst odgovora. Identitet treba ulogu **Azure AI User** u
Foundry obuhvatu projekta; token publika mora biti `https://ai.azure.com/`.

Slojite vratila: **smoke test** (dostupno/odgovara, svaka implementacija) → **offline
evaluacija** (dovoljno dobra za isporuku, prije promocije) → **online evaluacija** (kako
se ponaša u divljini, kontinuirana).

## Enterprise kontrole

- **RBAC**: dodijelite svakom hostanom agentu upravljani identitet s minimalnim privilegijama.
- **MCP u produkciji**: tretirajte svaki MCP poslužitelj kao nepouzdanu granicu — zaključajte verziju, ograničite identitet, provjerite izlaze, ograničite brzinu, nikada ne izlažite tajne.

## Zaštitne mjere za asistenta

- Preferirajte kanonski obrazac `FoundryChatClient(...)` + `provider.as_agent(...)` korišten kroz cijeli tečaj.
- Nemojte obećavati rezultate uživo iz Azurea koje niste provjerili; preporučite smoke-test workflow za potvrdu implementacije.
- Držite savjete o evaluaciji i troškovima povezanim: evaluacija postavlja kvalitetni prag, usmjeravanje/keširanje drži trošak blizu tog praga.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->