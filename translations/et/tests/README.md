# Agendi suitsutestid

See kaust sisaldab **suitsutesti katalooge** agentide jaoks, mida te kursuse jooksul ehitate.
Suitsutest on odav ja kiire kontroll, kas **Microsoft Foundry majutatud agent**, mis on välja pandud,
on ligipääsetav, reageerib ja järgib oma kõige põhilisemaid prompti
ootusi. See on esimene värav — mitte täieliku hindamis-
protsessi asendaja, mida õpite [Õppetükk 10-s](../10-ai-agents-production/README.md) ja
[Õppetükk 16-s](../16-deploying-scalable-agents/README.md).

Katalooge kasutab [AI suitsutest](https://github.com/marketplace/actions/ai-smoke-test)
GitHub Action kaudu [`.github/workflows/smoke-test.yml`](../../../.github/workflows/smoke-test.yml)
töövoog.

## Kuidas käivitada

1. **Deploy agent õppetükist** Microsoft Foundrys majutatud agendina (vt
   Õppetükk 16 deploy töövoogu). Pane tähele **agendi nime** ja oma
   **Foundry projekti lõpp-punkti**.
2. Lisa need repositooriumi saladused (Settings → Secrets and variables → Actions):
   `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`. Föderaalne
   identiteet vajab **Azure AI User** rolli **Foundry projekti ulatuses**.
3. Vali vaheleht **Actions**, käivita **Smoke-test hosted agents** ja vali õppetüki
   `tests_file`, seejärel anna sobiv `agent_name` ja
   `project_endpoint`.

## Kataloog → õppetükk → agendi nimi

| Kataloog | Õppetükk | Deploy agentina |
|---------|----------|-----------------|
| [`lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) | [01 – Intro AI Agentidesse](../01-intro-to-ai-agents/README.md) | `TravelAgent` |
| [`lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) | [04 – Tööriistade kasutamine](../04-tool-use/README.md) | `TravelToolAgent` |
| [`lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) | [05 – Agentic RAG](../05-agentic-rag/README.md) | `TravelRAGAgent` |
| [`lesson-16-smoke-tests.json`](../../../tests/lesson-16-smoke-tests.json) | [16 – Skalaarsete agentide deployimine](../16-deploying-scalable-agents/README.md) | `ContosoSupportAgent` |

## Millistel õppetundidel on suitsutestid?

Suitsutestid kehtivad õppetundidele, kus sa **deployid agenti**, kelle tekstivastuseid saab
teadaoleva sisuga kontrollida. Õppetunnid, mis on kontseptuaalsed, töötavad vaid lokaalselt
või annavad mitte-determineeritavaid loomingulisi tulemusi, on tahtlikult välistatud:

- **Õppetükk 17 (Kohalike AI agentide loomine)** töötab täielikult sinu tööjaamas koos
  Foundry Localiga ja ei avalda Foundry Responses lõpp-punkti, seega see
  tegevus ei kehti. Kontrolli seda lokaalselt sülearvuti abil.
- Disainimustrite ja teooria õppetunnid (02, 03, 06, 07, 09, 12) ei paku deploy agenti,
  mida võiks suitsutesti jaoks kasutada.

## Kataloogi skeem (kiire viide)

Iga kataloog on JSON dokument, mille tipp-tasemel on `tests` massiiv. Iga kirje POSTib
ühe prompti ja kontrollib vastust:

| Väli | Tähendus |
|-------|---------|
| `id` | Unikaalne sammu identifikaator, mis trükitakse logisse. |
| `description` | Inimloetav eesmärk. |
| `prompt` | Agentile saadetud sõnum. |
| `assertions.status` | Oodatud HTTP staatus (vaikimisi 200). |
| `assertions.contains_any` | Läbib, kui vastus sisaldab mõnda neist alamstringidest. |
| `assertions.contains_all` | Läbib, kui vastus sisaldab kõiki alamstringe. |
| `assertions.contains_none` | Läbib, kui vastus ei sisalda ühtegi neist alamstringidest. |
| `save_response_id_as` | Salvestab vastuse ID hilisemaks mitme pöörde sammuks. |
| `use_previous_response_id` | Saadab selle pöörde seotuna salvestatud vastuse ID-ga. |

Kontrollid on tõstutundlikkust ignoreerivad alamstringi otsingud. Vaata
[tegevuse dokumentatsiooni](https://github.com/marketplace/actions/ai-smoke-test) täielikku skeemi,
sealhulgas Foundry hallatavaid vestlusressursse.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Lahtiütlus**:
See dokument on tõlgitud kasutades AI tõlketeenust [Co-op Translator](https://github.com/Azure/co-op-translator). Kuigi me püüdleme täpsuse poole, palun pange tähele, et automatiseeritud tõlgetes võib esineda vigu või ebatäpsusi. Originaaldokument selle emakeeles tuleks pidada autoriteetseks allikaks. Olulise teabe puhul soovitatakse kasutada professionaalset inimtõlget. Me ei vastuta selle tõlkega seotud eksimustest või valesti mõistmistest.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->