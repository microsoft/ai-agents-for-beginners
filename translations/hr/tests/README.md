# Agent Smoke Testovi

Ova mapa sadrži **smoke-test kataloške** za agente koje gradite tijekom tečaja.
Smoke test je jeftina, brza provjera da je **postavljeni Microsoft Foundry hostani
agent** dostupan, odgovara i slijedi svoje najosnovnije zahtjeve
upita. To je prva prepreka — nije zamjena za cjelokupni evaluacijski
tijek rada kojeg učite u [Lekcija 10](../10-ai-agents-production/README.md) i
[Lekcija 16](../16-deploying-scalable-agents/README.md).

Katalozi se koriste putem [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
GitHub akcije preko [`.github/workflows/smoke-test.yml`](../../../.github/workflows/smoke-test.yml)
tijeka rada.

## Kako pokrenuti

1. **Postavite agenta iz lekcije** na Microsoft Foundry kao hostanog agenta (pogledajte
   Lekciju 16 za tijek rada implementacije). Zabilježite **ime agenta** i svoj
   **Foundry projekt endpoint**.
2. Dodajte ove tajne repozitorija (Settings → Secrets and variables → Actions):
   `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`. Federirana
   identifikacija treba imati ulogu **Azure AI User** na **Foundry projekt opsegu**.
3. Iz kartice **Actions**, pokrenite **Smoke-test hosted agents** i odaberite
   `tests_file` za lekciju, zatim unesite odgovarajući `agent_name` i
   `project_endpoint`.

## Katalog → lekcija → ime agenta

| Katalog | Lekcija | Postavi agenta kao |
|---------|---------|---------------------|
| [`lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) | [01 – Uvod u AI agente](../01-intro-to-ai-agents/README.md) | `TravelAgent` |
| [`lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) | [04 – Korištenje alata](../04-tool-use/README.md) | `TravelToolAgent` |
| [`lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) | [05 – Agentic RAG](../05-agentic-rag/README.md) | `TravelRAGAgent` |
| [`lesson-16-smoke-tests.json`](../../../tests/lesson-16-smoke-tests.json) | [16 – Postavljanje skalabilnih agenata](../16-deploying-scalable-agents/README.md) | `ContosoSupportAgent` |

## Koje lekcije imaju smoke testove?

Smoke testovi se primjenjuju na lekcije gdje **postavljate agenta** čiji se tekstualni odgovori mogu
potvrditi prema poznatom sadržaju. Lekcije koje su konceptualne, rade samo lokalno,
ili proizvode nedeterministički kreativni izlaz su namjerno isključene:

- **Lekcija 17 (Kreiranje lokalnih AI agenata)** radi u potpunosti na vašem radnom računalu s
  Foundry Local i **ne** izlaže Foundry Responses endpoint, pa se ova
  akcija ne primjenjuje. Validirajte ju pokretanjem bilježnice lokalno.
- Lekcije o dizajn obrazcima i teoriji (02, 03, 06, 07, 09, 12) ne distribuiraju ni jednog
  implementabilnog agenta za smoke-test.

## Shema kataloga (brzi pregled)

Svaki katalog je JSON dokument s gornjom razinom `tests` nizom. Svaki unos šalje
jedan upit i provjerava odgovor:

| Polje | Značenje |
|-------|----------|
| `id` | Jedinstveni identifikator koraka ispisan u zapisniku. |
| `description` | Svrha čitljiva ljudima. |
| `prompt` | Poruka poslata agentu. |
| `assertions.status` | Očekivani HTTP status (zadano 200). |
| `assertions.contains_any` | Prođe ako odgovor sadrži bilo koji od ovih podnizova. |
| `assertions.contains_all` | Prođe ako odgovor sadrži svaki podniz. |
| `assertions.contains_none` | Prođe ako odgovor ne sadrži nijedan od ovih podnizova. |
| `save_response_id_as` | Spremi id odgovora za kasniji višekorak. |
| `use_previous_response_id` | Pošalji ovaj korak u lancu s prethodno spremljenim id-om odgovora. |

Provjere su neosjetljive na velika/mala slova i provjeravaju podnizove. Pogledajte
[dokumentaciju akcije](https://github.com/marketplace/actions/ai-smoke-test) za
potpunu shemu, uključujući Foundry-jem upravljane resurse razgovora.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Napomena**:
Ovaj dokument je preveden korištenjem AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati greške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporuča se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazumevanja ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->