# Agent Røyktester

Denne mappen inneholder **røyktestkataloger** for agentene du bygger i kurset.
En røyktest er en billig, rask sjekk for at en **utplassert Microsoft Foundry-hostet
agent** er tilgjengelig, responderer og følger sine mest grunnleggende prompt
forventninger. Det er en første port — ikke en erstatning for hele evaluerings-
prosessen du lærer i [Leksjon 10](../10-ai-agents-production/README.md) og
[Leksjon 16](../16-deploying-scalable-agents/README.md).

Katalogene brukes av [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
GitHub Action via [`.github/workflows/smoke-test.yml`](../../../.github/workflows/smoke-test.yml)
arbeidsflyten.

## Hvordan kjøre

1. **Distribuer leksjonens agent** til Microsoft Foundry som en hostet agent (se
   Leksjon 16 for distribusjonsarbeidsflyt). Merk deg **agentnavnet** og ditt
   **Foundry-prosjektendepunkt**.
2. Legg til disse repositoryhemmelighetene (Innstillinger → Hemmeligheter og variabler → Actions):
   `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`. Den fødererte
   identiteten trenger rollen **Azure AI User** i **Foundry prosjektomfang**.
3. Fra **Actions**-fanen, kjør **Smoke-test hosted agents** og velg
   `tests_file` for leksjonen, og legg inn det matchende `agent_name` og
   `project_endpoint`.

## Katalog → leksjon → agentnavn

| Katalog | Leksjon | Distribuer agent som |
|---------|--------|---------------------|
| [`lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) | [01 – Intro til AI-agenter](../01-intro-to-ai-agents/README.md) | `TravelAgent` |
| [`lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) | [04 – Bruk av verktøy](../04-tool-use/README.md) | `TravelToolAgent` |
| [`lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) | [05 – Agentic RAG](../05-agentic-rag/README.md) | `TravelRAGAgent` |
| [`lesson-16-smoke-tests.json`](../../../tests/lesson-16-smoke-tests.json) | [16 – Distribuere skalerbare agenter](../16-deploying-scalable-agents/README.md) | `ContosoSupportAgent` |

## Hvilke leksjoner har røyktester?

Røyktester gjelder for leksjoner hvor du **distribuerer en agent** hvor tekstsvar
kan påberopes mot kjent innhold. Leksjoner som er konseptuelle, kun kjører lokalt,
eller produserer ikke-deterministisk kreativt innhold er bevisst ekskludert:

- **Leksjon 17 (Opprette lokale AI-agenter)** kjører helt på din arbeidsstasjon med
  Foundry Local og eksponerer **ikke** et Foundry Responses-endepunkt, så denne
  handlingen gjelder ikke. Valider den ved å kjøre notebooken lokalt.
- Designmønster- og teorileksjoner (02, 03, 06, 07, 09, 12) leverer ikke en eneste
  distribuerbar agent for røyktesting.

## Katalogskjema (rask referanse)

Hver katalog er et JSON-dokument med et øverste nivå `tests` array. Hver oppføring POSTer
ett prompt og påberoper svaret:

| Felt | Betydning |
|-------|----------|
| `id` | Unik stegidentifikator skrevet i loggen. |
| `description` | Menneskelesbar hensikt. |
| `prompt` | Meldingen sendt til agenten. |
| `assertions.status` | Forventet HTTP-status (standard 200). |
| `assertions.contains_any` | Passer hvis svaret inneholder noen av disse delstrengene. |
| `assertions.contains_all` | Passer hvis svaret inneholder alle delstrenger. |
| `assertions.contains_none` | Passer hvis svaret ikke inneholder noen av disse delstrengene. |
| `save_response_id_as` | Lagre svar-id for et senere flertrinns-trinn. |
| `use_previous_response_id` | Send denne turen lenket til en lagret svar-id. |

Påberopelser er ikke-sakssensitive delstrengsjekker. Se
[handlingsdokumentasjonen](https://github.com/marketplace/actions/ai-smoke-test) for
fullt skjema, inkludert Foundry-administrerte samtaleressurser.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Ansvarsfraskrivelse**:
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->