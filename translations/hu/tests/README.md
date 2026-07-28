# Agent Smoke Tesztek

Ez a mappa tartalmazza az **smoke-teszt katalógusokat** az órán épített agentekhez.
A smoke teszt egy olcsó, gyors ellenőrzés, hogy egy **telepített Microsoft Foundry által hosztolt
agent** elérhető-e, válaszol-e és követi-e a legalapvetőbb prompt
elvárásokat. Ez egy első kapu – nem helyettesíti a teljes értékelési
folyamatot, amit a [10. leckében](../10-ai-agents-production/README.md) és
a [16. leckében](../16-deploying-scalable-agents/README.md) tanulsz.

A katalógusokat a [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
GitHub Action fogyasztja a [`.github/workflows/smoke-test.yml`](../../../.github/workflows/smoke-test.yml)
munkafolyamaton keresztül.

## Futatás módja

1. **Telepítsd az adott lecke agentjét** Microsoft Foundry-ba mint hosztolt agentet (lásd
   a 16. leckét a telepítési munkafolyamathoz). Jegyezd fel az **agent nevét** és a
   **Foundry projekt végpontját**.
2. Add meg ezeket a repository titkokat (Beállítások → Titkok és változók → Műveletek):
   `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`. A szövetséges
   identitásnak szüksége van az **Azure AI User** szerepkörre a **Foundry projekt szintjén**.
3. Az **Actions** fülön futtasd a **Smoke-test hosted agents** műveletet, és válaszd ki az
   adott lecke `tests_file` fájlját, majd add meg a megfelelő `agent_name` és
   `project_endpoint` értékeket.

## Katalógus → lecke → agent név

| Katalógus | Lecke | Telepített agent neve |
|---------|--------|-----------------|
| [`lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) | [01 – Bevezetés az AI agentekhez](../01-intro-to-ai-agents/README.md) | `TravelAgent` |
| [`lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) | [04 – Eszközhasználat](../04-tool-use/README.md) | `TravelToolAgent` |
| [`lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) | [05 – Agentic RAG](../05-agentic-rag/README.md) | `TravelRAGAgent` |
| [`lesson-16-smoke-tests.json`](../../../tests/lesson-16-smoke-tests.json) | [16 – Skálázható agentek telepítése](../16-deploying-scalable-agents/README.md) | `ContosoSupportAgent` |

## Mely leckékhez vannak smoke tesztek?

A smoke tesztek olyan leckékre vonatkoznak, ahol **telepítesz egy agentet**, amelynek
szöveges válaszai ismert tartalomhoz viszonyíthatók. Az olyan leckék, amelyek
elméletiek, csak helyileg futnak, vagy nem-determinisztikus kreatív kimenetet adnak,


- **17. lecke (Helyi AI agentek létrehozása)** teljes egészében a saját munkaállomásodon fut
  Foundry Local segítségével, és **nem** biztosít Foundry Válasz végpontot, így ez a
  művelet nem alkalmazható. Helyileg a notebook futtatásával validáld.
- Tervezési minta és elméleti leckék (02, 03, 06, 07, 09, 12) nem szállítanak egyetlen




Minden katalógus egy JSON dokumentum, amelynek tetején egy `tests` tömb található. Minden bejegyzés egy POST promptot küld el az agentnek és ellenőrzi a választ:

| Mező | Jelentés |
|-------|---------|
| `id` | Egyedi lépésazonosító, amely a naplóban jelenik meg. |
| `description` | Ember számára olvasható cél. |
| `prompt` | Az agentnek küldött üzenet. |
| `assertions.status` | Várt HTTP státusz (alapértelmezett 200). |
| `assertions.contains_any` | Teljesül, ha a válasz bármelyik megadott részszöveget tartalmazza. |
| `assertions.contains_all` | Teljesül, ha a válasz minden megadott részszöveget tartalmazza. |
| `assertions.contains_none` | Teljesül, ha a válasz egyik megadott részszöveget sem tartalmazza. |
| `save_response_id_as` | Elmenti a válasz azonosítót későbbi többlépcsős lépéshez. |
| `use_previous_response_id` | Ezt a kört egy elmentett válaszazonosítóhoz láncolva küldi el. |

Az állítások kis- és nagybetűtől független részszöveg-ellenőrzések. Lásd a
[action dokumentációját](https://github.com/marketplace/actions/ai-smoke-test) a
teljes séma, beleértve a Foundry által kezelt beszélgetési erőforrásokat is.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Jogi nyilatkozat**:
Ez a dokumentum az AI fordítási szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár az pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén professzionális emberi fordítást javasolunk. Nem vállalunk felelősséget semmilyen félreértésért vagy téves értelmezésért, amely ebből a fordításból ered.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->