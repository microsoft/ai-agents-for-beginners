---
name: deploying-scalable-agents
license: MIT
---
# Wdrażanie skalowalnych agentów z Microsoft Foundry

> Umiejętność towarzysząca do [Lekcji 16 – Wdrażanie skalowalnych agentów](../../../16-deploying-scalable-agents/README.md).
> Użyj jej, aby pomóc uczącemu się przenieść agenta z prototypu do skalowalnego, obserwowalnego
> wdrożenia produkcyjnego. Oparte każdą rekomendację na treści lekcji i
> działającej notatce; nie wymyślaj API Foundry.

## Wyzwalacze

Aktywuj tę umiejętność, gdy uczący się chce:
- Wdrożyć agenta w Microsoft Foundry jako **hostowanego agenta** i uczynić go wersjonowanym/obserwowalnym.
- Wybrać między wzorcami wdrożenia **hostowane przez klienta, hostowanego agenta oraz agent-workflow**.
- Dodać **rutowanie modelu**, **buforowanie odpowiedzi** lub **ograniczoną współbieżność**, aby kontrolować opóźnienia i koszty.
- Dodać **bramkę oceny**, aby zła wersja agenta nie została wysłana.
- Dodać krok **zatwierdzenia z udziałem człowieka** dla działań wysokiego ryzyka.
- Instrumentować agenta śledzeniem **OpenTelemetry** dla obserwowalności produkcyjnej.
- **Test dymny** wdrożonego agenta jako szybka bramka po wdrożeniu.

## Główny model mentalny

Agent produkcyjny to w dużej mierze operacyjny szkielet *wokół* modelu (~80%),
a nie sam model. Odnieś każdą rekomendację do jednego z tych aspektów:

| Aspekt | Prototyp → Produkcja |
|---------|------------------------|
| Hosting | notatnik → wersjonowana usługa hostowana |
| Tożsamość | twoje `az login` → zarządzana tożsamość + ograniczony RBAC |
| Stan | w pamięci → zewnętrzny magazyn wątków/pamięci |
| Błąd | traceback → ponowne próby, zapasowe działania, alerty |
| Koszt | "kilka centów" → monitorowany, kierowany, buforowany, budżetowany |
| Jakość | ocenianie wzrokowe → zautomatyzowana bramka oceny |
| Zaufanie | twoja akceptacja → polityka + człowiek w pętli |

## Wzorce wdrożenia (wybierz jeden lub połącz)

1. **Hostowane przez klienta** — pętla rozumowania działa w twoim procesie. Maksymalna kontrola; ty zarządzasz skalowaniem/stanem.
2. **Hostowany agent (Foundry Agent Service)** — Foundry hostuje pętlę, przechowuje wątki, wymusza RBAC/bezpieczeństwo treści, pokazuje agenta w portalu. Mniej kontroli, znacznie mniejsza powierzchnia operacyjna.
3. **Agent workflow** — wielu agentów/narzędzi połączonych w graf z rozgałęzieniami, węzłami zatwierdzającymi i trwałymi punktami kontrolnymi.

## Cykl życia (pętla wysyłająca agenta)

`create → wersjonuj → oceniaj (bramka) → wdrażaj jako hostowanego → obserwuj online → zbieraj błędy → powtórz`.
**Ocena offline to bramka, nie dodatek** — wersja nie zostanie wysłana
, jeśli nie przejdzie progu. Obserwowalność online przekazuje rzeczywiste błędy
do zestawu testów offline.

## Dźwignie skalowania i kosztów (w kolejności priorytetu)

1. **Dopasuj rozmiar modelu** — użyj najmniejszego modelu, który przejdzie bramkę oceny.
2. **Routowanie według złożoności** — mały/szybki model do prostych zapytań, duży model do prawdziwego rozumowania (własny klasyfikator lub Foundry Model Router).
3. **Buforowanie** — obsługuj niemal identyczne zapytania bez wywołania modelu.
4. **Projekt bezstanowy + ograniczona współbieżność** — zewnętrzny stan; ponawiaj próby z opóźnieniem.

## Kluczowe wzorce do odwzorowania

Wskaż uczącemu się te fragmenty w notatniku
[`16-python-agent-framework.ipynb`](../../../16-deploying-scalable-agents/code_samples/16-python-agent-framework.ipynb):

- **Obsługa żądań**: cache → routowanie według złożoności → śledzenie span → wykonanie → cache.
- **Bramka oceny**: oceniaj zestaw testowy offline; zwracaj `pass_rate >= threshold` i wdrażaj tylko jeśli prawda.
- **Zatwierdzenie człowieka**: `@tool(approval_mode="always_require")` dla działań takich jak duże zwroty.
- **Śledzenie**: owijaj każde żądanie w `tracer.start_as_current_span(...)` i ustawiaj atrybuty takie jak `routed.model`, `customer.id`.

## Test dymny wdrożonego agenta

Po wdrożeniu sprawdź, czy punkt końcowy faktycznie odpowiada (zielone wdrożenie może być
ciche). Użyj akcji [AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test)
przez [`.github/workflows/smoke-test.yml`](../../../../../.github/workflows/smoke-test.yml)
z katalogiem w [`tests/`](../../../tests/README.md). Runner wysyła POST każdego
promptu do `POST {project_endpoint}/agents/{agent_name}/endpoint/protocols/openai/responses`
i sprawdza tekst odpowiedzi. Tożsamość potrzebuje roli **Azure AI User**
w zakresie projektu Foundry; audiencja tokena musi być `https://ai.azure.com/`.

Nakładaj bramki: **test dymny** (osiągalność/odpowiedź, każde wdrożenie) → **ocena offline**
(wystarczająco dobra do wysłania, przed promocją) → **ocena online** (jak sobie radzi w praktyce, ciągła).


## Kontrole przedsiębiorstwa

- **RBAC**: daj każdemu hostowanemu agentowi zarządzaną tożsamość z minimalnymi uprawnieniami.
- **MCP w produkcji**: traktuj każdy serwer MCP jako nieufną granicę — przypnij wersję, ogranicz tożsamość, weryfikuj wyniki, ograniczaj tempo, nigdy nie ujawniaj sekretów.

## Bariery ochronne dla asystenta

- Preferuj kanoniczny wzorzec `FoundryChatClient(...)` + `provider.as_agent(...)` używany w całym kursie.
- Nie obiecuj wyników live-Azure, których nie zweryfikowałeś; zalecaj workflow testu dymnego, aby potwierdzić wdrożenie.
- Trzymaj ocenę i porady kosztowe powiązane: ocena ustala minimalną jakość, routowanie/buforowanie utrzymują koszt blisko tego poziomu.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->