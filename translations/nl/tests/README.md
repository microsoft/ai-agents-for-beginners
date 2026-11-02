# Agent Smoke Tests

Deze map bevat **smoke-test catalogi** voor de agents die je bouwt in de cursus.
Een smoke test is een goedkope, snelle controle of een **gedeployde Microsoft Foundry gehoste
agent** bereikbaar is, reageert en zich aan de meest basale prompt
verwachtingen houdt. Het is een eerste poort — geen vervanging voor de volledige evaluatie
pijplijn die je leert in [Les 10](../10-ai-agents-production/README.md) en
[Les 16](../16-deploying-scalable-agents/README.md).

De catalogi worden gebruikt door de [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
GitHub Action via de [`.github/workflows/smoke-test.yml`](../../../.github/workflows/smoke-test.yml)
workflow.

## Hoe te runnen

1. **Deploy de agent uit de les** naar Microsoft Foundry als een gehoste agent (zie
   Les 16 voor de deployment workflow). Noteer de **agentnaam** en je
   **Foundry project endpoint**.
2. Voeg deze repository secrets toe (Instellingen → Secrets en variabelen → Acties):
   `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`. De gefedereerde
   identiteit heeft de **Azure AI User** rol nodig binnen de **Foundry project scope**.
3. Ga naar de **Acties** tab, run **Smoke-test hosted agents** en kies het
   `tests_file` voor de les, vul dan de bijpassende `agent_name` en
   `project_endpoint` in.

## Catalogus → les → agentnaam

| Catalogus | Les | Agent deployen als |
|---------|--------|-----------------|
| [`lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) | [01 – Intro tot AI Agents](../01-intro-to-ai-agents/README.md) | `TravelAgent` |
| [`lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) | [04 – Tool gebruik](../04-tool-use/README.md) | `TravelToolAgent` |
| [`lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) | [05 – Agentic RAG](../05-agentic-rag/README.md) | `TravelRAGAgent` |
| [`lesson-16-smoke-tests.json`](../../../tests/lesson-16-smoke-tests.json) | [16 – Deployen van schaalbare agents](../16-deploying-scalable-agents/README.md) | `ContosoSupportAgent` |

## Welke lessen hebben smoke tests?

Smoke tests gelden voor lessen waarbij je **een agent deployt** wiens tekstuele antwoorden
kunnen worden geverifieerd tegen bekende inhoud. Lessen die conceptueel zijn, alleen lokaal draaien,
of niet-deterministische creatieve output opleveren worden opzettelijk uitgesloten:

- **Les 17 (Lokale AI Agents maken)** draait volledig op je werkstation met
  Foundry Local en biedt **geen** Foundry Responses endpoint, dus deze
  actie is niet van toepassing. Valideer deze les door het notebook lokaal te draaien.
- Design-patroon en theorie lessen (02, 03, 06, 07, 09, 12) leveren niet één
  deploybare agent op om te smoke-testen.

## Catalogus schema (korte referentie)

Elke catalogus is een JSON-document met een bovenliggende `tests` array. Elke invoer doet een POST van
één prompt en controleert het antwoord:

| Veld | Betekenis |
|-------|---------|
| `id` | Uniek stapidentificatie getoond in het log. |
| `description` | Mens leesbaar doel. |
| `prompt` | Het bericht verstuurd naar de agent. |
| `assertions.status` | Verwachte HTTP-status (standaard 200). |
| `assertions.contains_any` | Slaag als het antwoord een van deze deelstrings bevat. |
| `assertions.contains_all` | Slaag als het antwoord elke deelstring bevat. |
| `assertions.contains_none` | Slaag als het antwoord geen van deze deelstrings bevat. |
| `save_response_id_as` | Bewaar het antwoord-ID voor een latere multi-turn stap. |
| `use_previous_response_id` | Verstuur deze beurt gekoppeld aan een opgeslagen antwoord-ID. |

Asserties zijn case-insensitieve substring controles. Zie de
[actie documentatie](https://github.com/marketplace/actions/ai-smoke-test) voor
het volledige schema, inclusief Foundry-beheerde conversatiebronnen.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:
Dit document is vertaald met behulp van de AI vertaaldienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->