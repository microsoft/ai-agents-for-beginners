# Smoke testy agentů

Tato složka obsahuje **katalogy smoke testů** pro agenty, které v kurzu vytváříte.
Smoke test je levná, rychlá kontrola, zda je **nasazený agent hostovaný v Microsoft Foundry**
dostupný, reaguje a dodržuje své nejzákladnější očekávání od promptu.
Je to první brána — nikoli náhrada za celý evaluační
proces, který se naučíte v [Lekci 10](../10-ai-agents-production/README.md) a
[Lekci 16](../16-deploying-scalable-agents/README.md).

Katalogy využívá [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
GitHub Action přes workflow [`.github/workflows/smoke-test.yml`](../../../.github/workflows/smoke-test.yml).


## Jak spustit

1. **Nasadit agenta z lekce** do Microsoft Foundry jako hostovaného agenta (viz
   Lekce 16 pro postup nasazení). Poznamenejte si **název agenta** a svůj
   **Foundry projektový endpoint**.
2. Přidejte tyto repozitářové tajné klíče (Nastavení → Tajné klíče a proměnné → Akce):
   `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`. Federovaná
   identita potřebuje roli **Azure AI User** na **úrovni projektu Foundry**.
3. Ze záložky **Akce** spusťte **Smoke-test hosted agents** a vyberte
   `tests_file` pro lekci, poté zadejte odpovídající `agent_name` a
   `project_endpoint`.

## Katalog → lekce → jméno agenta

| Katalog | Lekce | Nasadit agenta jako |
|---------|--------|-----------------|
| [`lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) | [01 – Úvod do AI agentů](../01-intro-to-ai-agents/README.md) | `TravelAgent` |
| [`lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) | [04 – Použití nástrojů](../04-tool-use/README.md) | `TravelToolAgent` |
| [`lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) | [05 – Agentic RAG](../05-agentic-rag/README.md) | `TravelRAGAgent` |
| [`lesson-16-smoke-tests.json`](../../../tests/lesson-16-smoke-tests.json) | [16 – Nasazování škálovatelných agentů](../16-deploying-scalable-agents/README.md) | `ContosoSupportAgent` |

## Které lekce mají smoke testy?

Smoke testy se vztahují na lekce, kde **nasazujete agenta**, jehož textové odpovědi lze
ověřit vůči známému obsahu. Lekce, které jsou koncepční, běží pouze lokálně,
nebo produkují nedeterministický kreativní výstup, jsou záměrně vynechány:

- **Lekce 17 (Vytváření lokálních AI agentů)** běží kompletně na vašem počítači s
  Foundry Local a neexponuje endpoint Foundry Responses, takže na
  tuto akci neplatí. Validujte ji spuštěním notebooku lokálně.
- Lekce týkající se návrhových vzorů a teorie (02, 03, 06, 07, 09, 12) neposílají
  jediného nasaditelného agenta pro smoke test.

## Schéma katalogu (rychlá reference)

Každý katalog je JSON dokument s polem `tests` na nejvyšší úrovni. Každý záznam pošle
jeden prompt a ověří odpověď:

| Pole | Význam |
|-------|---------|
| `id` | Jedinečný identifikátor kroku vypsaný v logu. |
| `description` | Čitelný popis účelu. |
| `prompt` | Zpráva odeslaná agentovi. |
| `assertions.status` | Očekávaný HTTP status (výchozí 200). |
| `assertions.contains_any` | Projde, pokud odpověď obsahuje některý z těchto podřetězců. |
| `assertions.contains_all` | Projde, pokud odpověď obsahuje každý podřetězec. |
| `assertions.contains_none` | Projde, pokud odpověď neobsahuje žádný z těchto podřetězců. |
| `save_response_id_as` | Uloží ID odpovědi pro následující vícetahový krok. |
| `use_previous_response_id` | Odešle tento tah vázaný na uložené ID odpovědi. |

Ověření jsou bez ohledu na velikost písmen a kontrolují podřetězce. Viz
[dokumentace akce](https://github.com/marketplace/actions/ai-smoke-test) pro
celé schéma včetně zdrojů pro správu konverzací ve Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Prohlášení o omezení odpovědnosti**:
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o co největší přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoli nedorozumění nebo nesprávné interpretace vzniklé použitím tohoto překladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->