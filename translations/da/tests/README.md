# Agent Smoke Tests

Denne mappe indeholder **smoke-test kataloger** for de agenter, du bygger i kurset.
En smoke test er en billig, hurtig kontrol for, at en **udrullet Microsoft Foundry hosted
agent** er tilgængelig, svarer, og følger sine mest basale prompt
forventninger. Det er en første port — ikke en erstatning for den fulde evaluering
pipeline, du lærer i [Lesson 10](../10-ai-agents-production/README.md) og
[Lesson 16](../16-deploying-scalable-agents/README.md).

Katalogerne bruges af [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
GitHub Action via [`.github/workflows/smoke-test.yml`](../../../.github/workflows/smoke-test.yml)
workflowen.

## Hvordan man kører

1. **Deploy agenten fra lektionen** til Microsoft Foundry som en hosted agent (se
   Lektion 16 for implementeringsworkflowen). Bemærk **agentnavnet** og dit
   **Foundry projektendepunkt**.
2. Tilføj disse repository secrets (Indstillinger → Secrets og variabler → Actions):
   `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`. Den fødererede
   identitet skal have **Azure AI User** rollen på **Foundry projektomfang**.
3. Fra **Actions** fanen, kør **Smoke-test hosted agents** og vælg
   `tests_file` for lektionen, og angiv derefter det tilsvarende `agent_name` og
   `project_endpoint`.

## Katalog → lektion → agentnavn

| Katalog | Lektion | Deploy agent som |
|---------|---------|-----------------|
| [`lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) | [01 – Intro til AI Agenter](../01-intro-to-ai-agents/README.md) | `TravelAgent` |
| [`lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) | [04 – Brug af Værktøj](../04-tool-use/README.md) | `TravelToolAgent` |
| [`lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) | [05 – Agentic RAG](../05-agentic-rag/README.md) | `TravelRAGAgent` |
| [`lesson-16-smoke-tests.json`](../../../tests/lesson-16-smoke-tests.json) | [16 – Deploying Skalerbare Agenter](../16-deploying-scalable-agents/README.md) | `ContosoSupportAgent` |

## Hvilke lektioner har smoke tests?

Smoke tests gælder lektioner, hvor du **deployerer en agent**, hvis tekstsvar kan
kontrolleres mod kendt indhold. Lektioner som er konceptuelle, kører kun lokalt,
eller producerer ikke-deterministisk kreativ output er bevidst udelukket:

- **Lektion 17 (Oprettelse af Lokale AI Agenter)** kører udelukkende på din arbejdsstation med
  Foundry Local og eksponerer **ikke** et Foundry Responses endpoint, så denne
  handling gælder ikke. Valider den ved at køre notebook’en lokalt.
- Designmønster- og teori-lektioner (02, 03, 06, 07, 09, 12) leverer ikke en eneste
  deployerbar agent til smoke-test.

## Katalogskema (hurtig reference)

Hvert katalog er et JSON dokument med et top-niveau `tests` array. Hvert element POSTer
en prompt og foretager påstande om svaret:

| Felt | Betydning |
|-------|---------|
| `id` | Unikt trin-id, der skrives i loggen. |
| `description` | Menneskelæsbar beskrivelse. |
| `prompt` | Beskeden sendt til agenten. |
| `assertions.status` | Forventet HTTP status (standard 200). |
| `assertions.contains_any` | Godkend hvis svaret indeholder en af disse understreng. |
| `assertions.contains_all` | Godkend hvis svaret indeholder alle understrengene. |
| `assertions.contains_none` | Godkend hvis svaret ikke indeholder nogen af disse understreng. |
| `save_response_id_as` | Gem svar-id’et til et senere multi-turn trin. |
| `use_previous_response_id` | Send denne runde kædet til et gemt svar-id. |

Påstande er case-insensitive understrengkontroller. Se
[action-dokumentationen](https://github.com/marketplace/actions/ai-smoke-test) for
det fulde skema, inklusive Foundry-styrede samtaleressourcer.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->