# Agento dūmų testai

Šiame kataloge laikomi **dūmų testų katalogai** agentams, kuriuos kuriate kurso metu.
Dūmų testas yra pigus, greitas patikrinimas, ar **diegiami Microsoft Foundry talpinami
agentai** yra pasiekiami, reaguoja ir atitinka pagrindinius užklausos
lūkesčius. Tai pirmasis barjeras – ne pilno vertinimo proceso, kurį išmoksite
[10 pamokoje](../10-ai-agents-production/README.md) ir
[16 pamokoje](../16-deploying-scalable-agents/README.md), pakaitalas.

Katalogus naudoja [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
GitHub veiksmas per [`.github/workflows/smoke-test.yml`](../../../.github/workflows/smoke-test.yml)
darbo eigą.

## Kaip paleisti

1. **Įdiekite pamokos agentą** Microsoft Foundry kaip talpinamą agentą (žr.
   16 pamoką dėl diegimo darbo eigos). Užsirašykite **agento pavadinimą** ir savo
   **Foundry projekto galinį tašką**.
2. Pridėkite šias saugyklos paslaptis (Settings → Secrets and variables → Actions):
   `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`. Federuota
   tapatybė turi turėti **Azure AI User** rolę **Foundry projekto aprėptyje**.
3. Skiltyje **Actions** paleiskite **Smoke-test hosted agents** ir pasirinkite
   pamokos `tests_file`, tada nurodykite atitinkamus `agent_name` ir
   `project_endpoint`.

## Katalogas → pamoka → agento pavadinimas

| Katalogas | Pamoka | Diegti agentą kaip |
|---------|--------|-----------------|
| [`lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) | [01 – Įžanga į AI agentus](../01-intro-to-ai-agents/README.md) | `TravelAgent` |
| [`lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) | [04 – Įrankių naudojimas](../04-tool-use/README.md) | `TravelToolAgent` |
| [`lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) | [05 – Agentinė RAG](../05-agentic-rag/README.md) | `TravelRAGAgent` |
| [`lesson-16-smoke-tests.json`](../../../tests/lesson-16-smoke-tests.json) | [16 – Masto agentų diegimas](../16-deploying-scalable-agents/README.md) | `ContosoSupportAgent` |

## Kurios pamokos turi dūmų testus?

Dūmų testai taikomi toms pamokoms, kuriose **diegiama agentas**, kurio teksto atsakymai gali
būti patvirtinti pagal žinomą turinį. Pamokos, kurios yra konceptualios, veikia tik lokaliai
arba generuoja nedeterminuotą kūrybinį turinį, sąmoningai neįtraukiamos:

- **17 pamoka (Vietinių AI agentų kūrimas)** visiškai veikia jūsų darbalaukyje su
  Foundry Local ir **neišskleidžia** Foundry atsakymų galinio taško, todėl šis
  veiksmas netinka. Patikrinkite ją paleisdami užrašų knygelę lokaliai.
- Dizaino šablonų ir teorijos pamokos (02, 03, 06, 07, 09, 12) neišleidžia nė vieno
  diegiamo agento dūmų testams.

## Katalogo schema (greita nuoroda)

Kiekvienas katalogas yra JSON dokumentas su viršutinio lygio `tests` masyvu. Kiekvienas įrašas POST duoda
vieną užklausą ir patikrina atsakymą:

| Laukas | Reikšmė |
|-------|---------|
| `id` | Unikalus žingsnio identifikatorius, spausdinamas žurnale. |
| `description` | Žmogiškai skaitomas tikslas. |
| `prompt` | Pranešimas agentui. |
| `assertions.status` | Laukiamas HTTP statusas (numatytasis 200). |
| `assertions.contains_any` | Testas praeina, jei atsakyme yra bent viena iš šių potekstžių. |
| `assertions.contains_all` | Testas praeina, jei atsakyme yra kiekviena potekstė. |
| `assertions.contains_none` | Testas praeina, jei atsakyme nėra nė vienos iš šių potekstžių. |
| `save_response_id_as` | Išsaugoti atsakymo ID vėlesniam daugiažingsniam veiksmui. |
| `use_previous_response_id` | Siųsti šį žingsnį susietą su išsaugotu atsakymo ID. |

Tvirtinimai yra neskaidraus didžiųjų ir mažųjų raidžių potekstžių tikrinimai. Peržiūrėkite
[veiksmo dokumentaciją](https://github.com/marketplace/actions/ai-smoke-test) dėl
pilnos schemos, įskaitant Foundry valdomus pokalbių išteklius.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Atsakomybės apribojimas**:
Šis dokumentas buvo išverstas naudojant dirbtinio intelekto vertimo paslaugą [Co-op Translator](https://github.com/Azure/co-op-translator). Nors siekiame tikslumo, prašome atkreipti dėmesį, kad automatiniai vertimai gali turėti klaidų ar netikslumų. Originalus dokumentas jo gimtąja kalba laikomas autoritetingu šaltiniu. Svarbiai informacijai rekomenduojama naudoti profesionalų žmogiškąjį vertimą. Mes neatsakome už jokius nesusipratimus ar neteisingą interpretaciją, kilusią naudojantis šiuo vertimu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->