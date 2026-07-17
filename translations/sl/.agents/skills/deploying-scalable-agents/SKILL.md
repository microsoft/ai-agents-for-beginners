---
name: deploying-scalable-agents
license: MIT
---
# Izvajanje razširljivih agentov z Microsoft Foundry

> Spremljevalna veščina za [Lekcija 16 – Izvajanje razširljivih agentov](../../../16-deploying-scalable-agents/README.md).
> Uporabite jo, da pomagate učenčku premakniti agenta iz prototipa v razširljivo, opazno
> produkcijsko izvedbo. Vsak nasvet utemeljite na vsebini lekcije in
> zagonljivem zvezku; ne izmišljajte Foundry API-jev.

## Sprožilci

Aktivirajte to veščino, ko učenec želi:
- Izvesti agenta v Microsoft Foundry kot **gostujočega agenta** in ga narediti verzioniranega/opaznega.
- Izbirati med **odjemalsko-gostovan, gostujoči agent in agentni delovni tok** vzorci.
- Dodati **usmerjanje modela**, **predpomnjenje odgovorov** ali **omejeno sočasnost** za nadzor zakasnitve in stroškov.
- Dodati **ocenjevalno pregrado**, da slaba verzija agenta ne lahko pride v produkcijo.
- Dodati korak **človeške odobritve v zanki** za tvegane akcije.
- Instrumentirati agenta z **OpenTelemetry** sledenjem za produkcijsko opazovanje.
- Izvesti **smoke-test** nameščenega agenta kot hiter preizkus po namestitvi.

## Temeljni miselni model

Produkcijski agent je večinoma operativni okvir *okoli* modela (~80 %),
ne sam model. Vsak nasvet povežite z eno od teh skrbi:

| Skrb | Prototip → Produkcija |
|---------|------------------------|
| Gostovanje | zvezek → verzionirana gostujoča storitev |
| Identiteta | vaš `az login` → upravljana identiteta + omejen RBAC |
| Stanje | v spominu → zunanja shramba niti/spomina |
| Napaka | sled napake → poskusi znova, rezervni načrti, opozorila |
| Stroški | "nekaj centov" → spremljani, usmerjeni, predpomnjeni, proračun zabeležen |
| Kakovost | ocenjevanje z očmi → avtomatizirana ocenjevalna pregrada |
| Zaupanje | vaša odobritev → politika + človek v zanki |

## Vzorci izvajanja (izberite enega ali kombinirajte)

1. **Odjemalsko-gostovan** — razlogovanje poteka v vašem procesu. Največji nadzor; vi upravljate skaliranje/stanje.
2. **Gostujoči agent (Foundry Agent Service)** — Foundry gosti zanko, shranjuje niti, izvaja RBAC/varnost vsebine, prikazuje agenta v portalu. Manj nadzora, bistveno manj operativne površine.
3. **Agentni delovni tok** — več agentov/orodij sestavljenih v graf z razvejitvami, vozlišči za odobritev in trajnimi kontrolnimi točkami.

## Življenjski cikel (zanka, ki dostavi agenta)

`ustvari → verzioniraj → oceni (pregrada) → namesti gostujoče → opazuj na spletu → zbira napake → ponovi`.
**Offline ocenjevanje je pregrada, ne misel za nazaj** — verzije ne dostavimo,
če ne presežejo praga. Spletno opazovanje vrača resnične napake
v offline testni niz.

## Ročice skaliranja in stroškov (po prioriteti)

1. **Pravilno dimenzioniranje modela** — uporabite najmanjši model, ki prestane ocenjevalno pregrado.
2. **Usmerjanje po kompleksnosti** — majhen/hiter model za preproste zahteve, veliki model za resno sklepanje (lastni klasifikator ali Foundry Model Router).
3. **Predpomnjenje** — obravnavajte skoraj-multiple zahteve brez klica modela.
4. **Brezstatični dizajn + omejena sočasnost** — zunanja shranitev stanja; poskusi z nazajhodom.

## Ključni vzorci za ponovitev

Usmerite učenče v te iz zvezka
[`16-python-agent-framework.ipynb`](../../../16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb):

- **Obdelovalec zahtev**: predpomni → usmerjaj po kompleksnosti → sledilenje razpona → zaženi → predpomni.
- **Ocenjevalna pregrada**: oceni offline testni niz; vrni `pass_rate >= threshold` in namesti le, če je res.
- **Človeška odobritev**: `@tool(approval_mode="always_require")` za akcije, kot so veliki povračili.
- **Sledenje**: zavij vsako zahtevo v `tracer.start_as_current_span(...)` in nastavi atribute kot `routed.model`, `customer.id`.

## Smoke-test nameščenega agenta

Po namestitvi preverite, ali konec res odgovarja (zelena namestitev je lahko
tiha). Uporabite [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
akcijo prek [`.github/workflows/smoke-test.yml`](../../../../../.github/workflows/smoke-test.yml)
z katalogom v [`tests/`](../../../tests/README.md). Tekmovalec pošlje POST vsak
poziv na `POST {project_endpoint}/agents/{agent_name}/endpoint/protocols/openai/responses`
in preveri besedilo odgovora. Identiteta potrebuje vlogo **Azure AI User**
na obsegu projekta Foundry; občinstvo žetona mora biti `https://ai.azure.com/`.

Nakopičite pregrade: **smoke test** (dosegljiv/odziven, vsaka namestitev) → **offline
ocenjevanje** (dovolj dobro za pošiljanje, pred promocijo) → **spletno ocenjevanje** (kako
deluje v divjini, neprekinjeno).

## Podjetniška upravljanja

- **RBAC**: daj vsakemu gostujočemu agentu upravljano identiteto z najnižjimi privilegiji.
- **MCP v produkciji**: obravnavajte vsak MCP strežnik kot nezaupan mejnik — zaklenite verzijo, omejite njegovo identiteto, preverjajte izhode, omejujte stopnjo, nikoli ne izpostavljajte skrivnosti.

## Zaščitne ograje za asistenta

- Prednost dajte kanoničnemu vzorcu `FoundryChatClient(...)` + `provider.as_agent(...)`, ki se uporablja skozi celoten tečaj.
- Ne obljubljajte živih rezultatov Azure, ki jih niste preverili; priporočajte smoke-test delovni tok za potrditev namestitve.
- Ocenjevanje in nasvete o stroških obravnavajte skupaj: ocenjevanje določa kakovostno spodnjo mejo, usmerjanje/predpomnjenje pa držita stroške blizu te meje.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->