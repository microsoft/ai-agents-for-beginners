# Agentröktester

Denna mapp innehåller **röktestskataloger** för de agenter du bygger under kursen.
Ett röktest är en billig, snabb kontroll för att en **distribuerad Microsoft Foundry-hostad
agent** är nåbar, svarar och följer sina mest grundläggande prompt
förväntningar. Det är en första grind — inte en ersättning för den fullständiga utvärderings-
process som du lär dig i [Lektion 10](../10-ai-agents-production/README.md) och
[Lektion 16](../16-deploying-scalable-agents/README.md).

Katalogerna konsumeras av [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
GitHub Action via [`.github/workflows/smoke-test.yml`](../../../.github/workflows/smoke-test.yml)
arbetsflödet.

## Hur man kör

1. **Distribuera lektionens agent** till Microsoft Foundry som en hostad agent (se
   Lektion 16 för distributionsarbetsflödet). Notera **agentens namn** och din
   **Foundry projektendpoint**.
2. Lägg till dessa repository-hemligheter (Inställningar → Hemligheter och variabler → Actions):
   `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`. Den federerade
   identiteten behöver rollen **Azure AI User** på **Foundry projektomfång**.
3. Från fliken **Actions**, kör **Smoke-test hosted agents** och välj
   `tests_file` för lektionen, och ange sedan motsvarande `agent_name` och
   `project_endpoint`.

## Katalog → lektion → agentnamn

| Katalog | Lektion | Distribuera agent som |
|---------|--------|-----------------|
| [`lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) | [01 – Intro till AI Agent](../01-intro-to-ai-agents/README.md) | `TravelAgent` |
| [`lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) | [04 – Användning av verktyg](../04-tool-use/README.md) | `TravelToolAgent` |
| [`lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) | [05 – Agentic RAG](../05-agentic-rag/README.md) | `TravelRAGAgent` |
| [`lesson-16-smoke-tests.json`](../../../tests/lesson-16-smoke-tests.json) | [16 – Distribuera skalbara agenter](../16-deploying-scalable-agents/README.md) | `ContosoSupportAgent` |

## Vilka lektioner har röktester?

Röktester gäller lektioner där du **distribuerar en agent** vars text-svar kan
verifieras mot känt innehåll. Lektioner som är konceptuella, endast körs lokalt,
eller producerar icke-deterministiskt kreativt innehåll är medvetet uteslutna:

- **Lektion 17 (Skapa Lokala AI-Agenter)** körs helt på din arbetsstation med
  Foundry Local och exponerar **inte** någon Foundry Responses-endpoint, så denna
  åtgärd gäller inte. Validera den genom att köra anteckningsboken lokalt.
- Designmönster- och teorilektioner (02, 03, 06, 07, 09, 12) levererar inte en enda
  distribuerbar agent för röktest.

## Katalogschema (snabbreferens)

Varje katalog är ett JSON-dokument med en överordnad `tests` array. Varje post POST:ar
en prompt och verifierar svaret:

| Fält | Betydelse |
|-------|---------|
| `id` | Unikt steg-ID som skrivs ut i loggen. |
| `description` | Människoläsbar syfte. |
| `prompt` | Meddelandet skickat till agenten. |
| `assertions.status` | Förväntad HTTP-status (standard 200). |
| `assertions.contains_any` | Godkänd om svaret innehåller någon av dessa delsträngar. |
| `assertions.contains_all` | Godkänd om svaret innehåller alla delsträngar. |
| `assertions.contains_none` | Godkänd om svaret inte innehåller någon av dessa delsträngar. |
| `save_response_id_as` | Spara svarsid för ett senare stegs flersvängskommunikation. |
| `use_previous_response_id` | Skicka denna sväng kopplad till ett sparat svarsid. |

Påståenden är skiftlägesokänsliga kontroll av delsträngar. Se
[åtgärdsdokumentationen](https://github.com/marketplace/actions/ai-smoke-test) för
fullständigt schema, inklusive Foundry-hanterade konversationsresurser.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfriskrivning**:
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->