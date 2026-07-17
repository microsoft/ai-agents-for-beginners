# Agentné Smoke testy

Tento priečinok obsahuje **smoke-test katalógy** pre agentov, ktorých vytvárate v kurze.
Smoke test je lacná, rýchla kontrola, či je **nasadený agent hosťovaný Microsoft Foundry**
dostupný, odpovedá a dodržiava svoje najzákladnejšie očakávania v promptoch.
Je to prvá brána — nie náhrada za úplný evaluačný
proces, ktorý sa naučíte v [Lekcii 10](../10-ai-agents-production/README.md) a
[Lekcii 16](../16-deploying-scalable-agents/README.md).

Katalógy sú využívané GitHub Action [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
cez workflow [`.github/workflows/smoke-test.yml`](../../../.github/workflows/smoke-test.yml).


## Ako spustiť

1. **Nasadiť agenta lekcie** do Microsoft Foundry ako hosťovaného agenta (pozri Lekciu 16 pre nasadzovací workflow). Poznačte si **meno agenta** a váš
   **Foundry projektový endpoint**.
2. Pridajte tieto tajomstvá (Settings → Secrets and variables → Actions):
   `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`. Federovaná
   identita potrebuje rolu **Azure AI User** v **Foundry project scope**.
3. Zo záložky **Actions** spustite **Smoke-test hosted agents** a vyberte
   `tests_file` pre lekciu, potom zadajte zodpovedajúce `agent_name` a
   `project_endpoint`.


## Katalóg → lekcia → meno agenta

| Katalóg | Lekcia | Nasadiť agenta ako |
|---------|--------|-----------------|
| [`lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) | [01 – Úvod do AI agentov](../01-intro-to-ai-agents/README.md) | `TravelAgent` |
| [`lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) | [04 – Použitie nástrojov](../04-tool-use/README.md) | `TravelToolAgent` |
| [`lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) | [05 – Agentický RAG](../05-agentic-rag/README.md) | `TravelRAGAgent` |
| [`lesson-16-smoke-tests.json`](../../../tests/lesson-16-smoke-tests.json) | [16 – Nasadzovanie škálovateľných agentov](../16-deploying-scalable-agents/README.md) | `ContosoSupportAgent` |

## Ktoré lekcie majú smoke testy?

Smoke testy platia pre lekcie, kde **nasadzujete agenta**, ktorého textové odpovede je možné
overiť podľa známeho obsahu. Lekcie, ktoré sú koncepčné, bežia iba lokálne,
alebo produkujú nedeterministický kreatívny výstup, sú zámerne vynechané:

- **Lekcia 17 (Vytváranie lokálnych AI agentov)** beží úplne na vašom počítači s
  Foundry Local a **neposkytuje Foundry Responses endpoint**, takže táto
  akcia sa na ňu nevzťahuje. Validujte ju spustením notebooku lokálne.
- Lekcie o dizajnových vzoroch a teórii (02, 03, 06, 07, 09, 12) neobsahujú žiadne
  nasaditeľné agentné pre smoke-test.

## Schéma katalógu (rýchla referencia)

Každý katalóg je JSON dokument s poľom `tests` na najvyššej úrovni. Každý záznam
POSTne jeden prompt a overuje odpoveď:

| Pole | Význam |
|-------|---------|
| `id` | Jedinečný identifikátor kroku vypísaný v logu. |
| `description` | Čitateľný účel. |
| `prompt` | Správa odoslaná agentovi. |
| `assertions.status` | Očakávaný HTTP status (predvolené 200). |
| `assertions.contains_any` | Prejde, ak odpoveď obsahuje niektorý z týchto podreťazcov. |
| `assertions.contains_all` | Prejde, ak odpoveď obsahuje všetky podreťazce. |
| `assertions.contains_none` | Prejde, ak odpoveď neobsahuje žiadny z týchto podreťazcov. |
| `save_response_id_as` | Uložiť id odpovede pre neskorší multi-turn krok. |
| `use_previous_response_id` | Odoslať tento krok naviazaný na uložené id odpovede. |

Overenia sú kontrolou podreťazcov nezávisle na veľkosti písmen. Viď
[dokumentáciu akcie](https://github.com/marketplace/actions/ai-smoke-test) pre
úplnú schému vrátane konverzačných zdrojov spravovaných Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vyhlásenie o zodpovednosti**:
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, vezmite prosím na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho natívnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->