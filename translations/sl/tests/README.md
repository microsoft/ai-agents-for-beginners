# Agentni Smoke testi

Ta mapa vsebuje **kataloge za smoke testiranje** agentov, ki jih zgradite v okviru tečaja.
Smoke test je poceni, hiter pregled, ali je **razporejeni Microsoft Foundry gostovani
agent** dosegljiv, odgovarja in sledi svojim najosnovnejšim pričakovanjem o pozivu.
Je prvi preizkus — ne nadomestilo za celoten evalvacijski
potek, ki se ga naučite v [Lekciji 10](../10-ai-agents-production/README.md) in
[Lekciji 16](../16-deploying-scalable-agents/README.md).

Katalozi se uporabljajo v [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
GitHub akciji preko [`.github/workflows/smoke-test.yml`](../../../.github/workflows/smoke-test.yml)
delovnega toka.

## Kako izvajati

1. **Razporedite agent lekcije** v Microsoft Foundry kot gostovanega agenta (oglejte si
   Lekcijo 16 za potek razporejanja). Zabeležite **ime agenta** in vaš
   **Foundry projektni konec**.
2. Dodajte te skrivnosti repozitorija (Nastavitve → Skrivnosti in spremenljivke → Akcije):
   `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`. Federativna
   identiteta mora imeti vlogo **Azure AI User** znotraj **Foundry projektnega dosega**.
3. V zavihku **Akcije**, zaženite **Smoke-test hosted agents** in izberite
   `tests_file` za lekcijo, nato vnesite ustrezno `agent_name` in
   `project_endpoint`.

## Katalog → lekcija → ime agenta

| Katalog | Lekcija | Razporedi agenta kot |
|---------|---------|----------------------|
| [`lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) | [01 – Uvod v AI agente](../01-intro-to-ai-agents/README.md) | `TravelAgent` |
| [`lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) | [04 – Uporaba orodij](../04-tool-use/README.md) | `TravelToolAgent` |
| [`lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) | [05 – Agentni RAG](../05-agentic-rag/README.md) | `TravelRAGAgent` |
| [`lesson-16-smoke-tests.json`](../../../tests/lesson-16-smoke-tests.json) | [16 – Razporejanje razširljivih agentov](../16-deploying-scalable-agents/README.md) | `ContosoSupportAgent` |

## Kateri lekciji imata smoke teste?

Smoke testi veljajo za lekcije, kjer **razporedite agenta**, katerih besedilni odgovori se
lahko preverijo glede na znano vsebino. Lekcije, ki so konceptualne, tečejo le lokalno,
ali ustvarjajo nedoločljiv ustvarjalni izhod so namerno izključene:

- **Lekcija 17 (Ustvarjanje lokalnih AI agentov)** teče izključno na vaši delovni postaji z
  Foundry Local in **ne** izpostavlja končne točke Foundry Response, zato to
  dejanje ne velja. Preverite jo z zagonom zvezka lokalno.
- Lekcije o vzorcih in teoriji (02, 03, 06, 07, 09, 12) ne vključujejo niti enega
  razpoložljivega agenta za smoke testiranje.

## Shema kataloga (hitri pregled)

Vsak katalog je JSON dokument z zgornjim nivojem tabele `tests`. Vsak vnos POST-a
pošlje en poziv in preveri odgovor:

| Polje | Pomen |
|-------|---------|
| `id` | Unikatni identifikator koraka, zapisan v dnevnik. |
| `description` | Človeku berljiv namen. |
| `prompt` | Sporočilo poslano agentu. |
| `assertions.status` | Pričakovani HTTP status (privzeto 200). |
| `assertions.contains_any` | Sprejme, če odgovor vsebuje kateri koli od teh podnizov. |
| `assertions.contains_all` | Sprejme, če odgovor vsebuje vsak podniz. |
| `assertions.contains_none` | Sprejme, če odgovor ne vsebuje nobenega od teh podnizov. |
| `save_response_id_as` | Shrani id odgovora za kasnejši večkrožni korak. |
| `use_previous_response_id` | Pošlje ta krog kot povezan z shranjenim id-jem odgovora. |

Preverjanja so nepristranski pregledi podnizov. Oglejte si
[dokumentacijo akcije](https://github.com/marketplace/actions/ai-smoke-test) za
celotno shemo, vključno z viri pogovorov, ki jih upravlja Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Omejitev odgovornosti**:
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za kritične informacije je priporočljiv strokovni človeški prevod. Ne odgovarjamo za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->