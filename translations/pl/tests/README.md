# Testy dymne agenta

Ten folder zawiera **katalogi testów dymnych** dla agentów, których budujesz podczas kursu.
Test dymny to tani, szybki test sprawdzający, czy **wdrożony agent Microsoft Foundry jako hostowany
jest osiągalny, odpowiada i spełnia swoje najbardziej podstawowe oczekiwania względem promptu**.
To pierwsza brama — nie zastępuje pełnego procesu ewaluacji,
którego uczysz się w [Lekcji 10](../10-ai-agents-production/README.md) oraz
[Lekcji 16](../16-deploying-scalable-agents/README.md).

Katalogi są wykorzystywane przez [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
akcję GitHub poprzez [workflow `.github/workflows/smoke-test.yml`](../../../.github/workflows/smoke-test.yml).


## Jak uruchomić

1. **Wdróż agenta z lekcji** do Microsoft Foundry jako hostowanego agenta (zobacz
   Lekcję 16 i proces wdrożenia). Zapamiętaj **nazwę agenta** oraz swój
   **endpoint projektu Foundry**.
2. Dodaj sekrety do repozytorium (Ustawienia → Sekrety i zmienne → Akcje):
   `AZURE_CLIENT_ID`, `AZURE_TENANT_ID`, `AZURE_SUBSCRIPTION_ID`. Tożsamość federowana
   musi mieć przypisaną rolę **Azure AI User** na poziomie **zakresu projektu Foundry**.
3. Z zakładki **Akcje** uruchom **Smoke-test hosted agents** i wybierz
   `tests_file` dla lekcji, następnie podaj odpowiadające `agent_name` i
   `project_endpoint`.

## Katalog → lekcja → nazwa agenta

| Katalog | Lekcja | Wdróż agenta jako |
|---------|--------|-------------------|
| [`lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json) | [01 – Wprowadzenie do agentów AI](../01-intro-to-ai-agents/README.md) | `TravelAgent` |
| [`lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json) | [04 – Użycie narzędzi](../04-tool-use/README.md) | `TravelToolAgent` |
| [`lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json) | [05 – Agentic RAG](../05-agentic-rag/README.md) | `TravelRAGAgent` |
| [`lesson-16-smoke-tests.json`](../../../tests/lesson-16-smoke-tests.json) | [16 – Wdrażanie skalowalnych agentów](../16-deploying-scalable-agents/README.md) | `ContosoSupportAgent` |

## Dla których lekcji są testy dymne?

Testy dymne dotyczą lekcji, w których **wdrażasz agenta**, którego tekstowe odpowiedzi można
porównać z oczekiwaną treścią. Lekcje o charakterze koncepcyjnym, działające tylko lokalnie
lub generujące niedeterministyczne kreatywne wyniki są świadomie wyłączone:

- **Lekcja 17 (Tworzenie lokalnych agentów AI)** działa całkowicie na twoim komputerze lokalnym w
  Foundry Local i **nie** udostępnia endpointu Foundry Responses, więc ta
  akcja nie ma zastosowania. Zweryfikuj ją uruchamiając notatnik lokalnie.
- Lekcje dotyczące wzorców projektowych i teorii (02, 03, 06, 07, 09, 12) nie zawierają
  żadnego wdrażalnego agenta do testów dymnych.

## Schemat katalogu (szybka referencja)

Każdy katalog to dokument JSON z główną tablicą `tests`. Każdy wpis wysyła 
jeden prompt i sprawdza odpowiedź:

| Pole | Znaczenie |
|-------|----------|
| `id` | Unikalny identyfikator kroku, wyświetlany w logu. |
| `description` | Cel zrozumiały dla ludzi. |
| `prompt` | Wiadomość wysłana do agenta. |
| `assertions.status` | Oczekiwany status HTTP (domyślnie 200). |
| `assertions.contains_any` | Test przejdzie, jeśli odpowiedź zawiera dowolny z tych podłańcuchów. |
| `assertions.contains_all` | Test przejdzie, jeśli odpowiedź zawiera każdy z podłańcuchów. |
| `assertions.contains_none` | Test przejdzie, jeśli odpowiedź nie zawiera żadnego z podłańcuchów. |
| `save_response_id_as` | Zapisz id odpowiedzi do użycia w późniejszym wieloturnowym kroku. |
| `use_previous_response_id` | Wyślij ten turnus powiązany z zapisanym id odpowiedzi. |

Assercje to ignorujące wielkość liter sprawdzenia obecności podłańcuchów. Zobacz
[dokumentację akcji](https://github.com/marketplace/actions/ai-smoke-test) dla
pełnego schematu, włączając zasoby konwersacji zarządzane przez Foundry.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->