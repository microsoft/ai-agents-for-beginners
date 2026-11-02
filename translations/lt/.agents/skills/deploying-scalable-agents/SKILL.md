---
name: deploying-scalable-agents
license: MIT
---
# Skalaujamų agentų diegimas su Microsoft Foundry

> Palydovinė įguda pamokai [16 pamoka – Skalaujamų agentų diegimas](../../../16-deploying-scalable-agents/README.md).
> Naudokite ją, kad padėtumėte mokiniui perkelti agentą nuo prototipo prie skaluojamo, stebimo
> gamybinio diegimo. Kiekvieną rekomendaciją pagrįskite pamokos turiniu ir
> vykdomuoju nešiojamuoju užrašu; nekurkite naujų Foundry API.

## Sukelėjai

Aktyvinkite šią įgudį, kai mokinys nori:
- Diegti agentą į Microsoft Foundry kaip **hostintą agentą** ir jį versijuoti/stebėti.
- Pasirinkti tarp **kliento hostinimo, hostinto agente ir agentų darbo eigos** diegimo modelių.
- Pridėti **modelio maršrutizavimą**, **atsakymo kešavimą** arba **ribotą lygiagrečią apdorojimą** vėlinimo ir išlaidų valdymui.
- Pridėti **vertinimo vartus**, kad prasta agento versija negalėtų patekti į gamybą.
- Pridėti **žmogiško patvirtinimo** etapą rizikingiems veiksmams.
- Instrumentuoti agentą su **OpenTelemetry** sekimu gamybinio stebėjimo tikslu.
- Atlikti **pradūmimo testą** diegtam agentui kaip greitą po diegimo kontrolę.

## Pagrindinė mąstymo schema

Gamybinis agentas daugiausia yra operacinis karkasas *aplink* modelį (~80%),
o ne pats modelis. Kiekvieną rekomendaciją susiekite su šiais aspektais:

| Sritis | Prototipas → Gamyba |
|---------|---------------------|
| Hostinimas | užrašas → versijuota hostinta paslauga |
| Tapatybė | jūsų `az login` → valdomoji tapatybė + apribotas RBAC |
| Būsena | atmintyje → išorinė siūlų/atminties saugykla |
| Gedimai | klaidų sekimas → pakartojimai, atsarginiai variantai, aliarmas |
| Kaina | „kelios centai“ → sekama, maršrutizuojama, kešuojama, biudžetuojama |
| Kokybė | apžvalga → automatizuotas vertinimo vartai |
| Pasitikėjimas | jūs patvirtinate → politika + žmogus procese |

## Diegimo modeliai (rinkitės vieną arba derinkite)

1. **Kliento hostinimas** — sprendimų ciklas vyksta jūsų procesoriuje. Maksimalus valdymas; jūs kontroliuojate skalavimą/būseną.
2. **Hostintas agentas (Foundry Agent Service)** — Foundry talpina ciklą, saugo siūlus, vykdo RBAC/turinio saugumą, rodo agentą portale. Mažiau kontrolės, gerokai mažiau eksploatacinio paviršiaus.
3. **Agentų darbo eiga** — keli agentai/įrankiai sudaryti į grafiką su šakomis, patvirtinimo mazgais ir patvariais patikros taškais.

## Gyvavimo ciklas (ciklas, kuris išleidžia agentą)

`create → version → evaluate (gate) → deploy hosted → observe online → collect failures → repeat`.
**Ofline vertinimas yra vartai, o ne papildoma mintis** — versija neišleidžiama
, jei ji neperžengia ribos. Online stebėjimas sugrąžina tikrus gedimus
atgal į offline testų rinkinį.

## Skalavimo ir kainos svertai (pagal prioritetą)

1. **Tinkami modelio matmenys** — naudokite mažiausią modelį, kuris peržengia vertinimo vartus.
2. **Maršrutuokite pagal sudėtingumą** — mažas/greitas modelis paprastiems užklausim, didelis modelis tikram sprendimų priėmimui (DIY klasifikatorius arba Foundry Model Router).
3. **Kešuokite** — aptarnauti beveik identiškas užklausas be modelio kvietimo.
4. **Be būseno dizainas + ribota lygiagretis apdorojimas** — išorinė būsena; pakartoti su atsitraukimu.

## Svarbūs modeliai, kuriuos reikia atkartoti

Nukreipkite mokinį į šiuos nešiojamajame užraše
[`16-python-agent-framework.ipynb`](../../../16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb):

- **Užklausos apdorojėjas**: kešas → maršrutas pagal sudėtingumą → sekančio trasa → vykdymas → kešavimas.
- **Vertinimo vartai**: įvertinkite offline testų rinkinį; grąžinkite `pass_rate >= threshold` ir diegkite tik jei true.
- **Žmogiškas patvirtinimas**: `@tool(approval_mode="always_require")` tokiems veiksmams kaip didelės grąžos.
- **Sekimas**: įvilkite kiekvieną užklausą į `tracer.start_as_current_span(...)` ir nustatykite atributus kaip `routed.model`, `customer.id`.

## Pradūmimo testas diegtam agentui

Po diegimo patikrinkite, ar galinis taškas tikrai atsako (žalias diegimas vis dar gali būti
tylus). Naudokite [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
veiksmą per [`.github/workflows/smoke-test.yml`](../../../../../.github/workflows/smoke-test.yml)
su katalogu [`tests/`](../../../tests/README.md). Vykdytojas siunčia POST kiekvienam
užklausimui į `POST {project_endpoint}/agents/{agent_name}/endpoint/protocols/openai/responses`
ir patikrina atsakymo tekstą. Tapatybė turi turėti **Azure AI User** rolę prie
Foundry projekto aprėpties; žymens auditorija turi būti `https://ai.azure.com/`.

Sudėliokite vartus: **pradūmimo testas** (pasiekiamas/atsako, kiekvienas diegimas) → **offline vertinimas** (pakankamai geras išleidimui, prieš pervedimą) → **online vertinimas** (kaip veikia realybėje, nuolatinis).



## Įmonių kontrolės

- **RBAC**: suteikite kiekvienam hostintam agentui valdomą tapatybę su mažiausiais leidimais.
- **MCP gamyboje**: traktinkite kiekvieną MCP serverį kaip nepatikimą ribą – fiksuokite versiją, ribokite jo tapatybę, tikrinkite rezultatus, ribokite dažnį, niekada neatskleiskite paslapčių.

## Pagalbinio įrankio saugos priemonės

- Pirmenybę teikite kanoniniam `FoundryChatClient(...)` + `provider.as_agent(...)` modeliui, naudotam per visą kursą.
- Nežadėkite tiesioginių Azure rezultatų, kurių nesate patvirtinę; rekomenduokite pradūmimo testų darbų eigą diegimo patvirtinimui.
- Laikykite vertinimo ir kainos rekomendacijas kartu: vertinimas nustato kokybės ribą, maršrutizavimas/kešavimas palaiko kainą arti šios ribos.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->