# Agenci AI w produkcji: Obserwowalność i ewaluacja

[![Agenci AI w produkcji](../../../translated_images/pl/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

W miarę jak agenci AI przechodzą od prototypów eksperymentalnych do zastosowań w rzeczywistym świecie, zdolność do rozumienia ich zachowania, monitorowania wydajności oraz systematycznej ewaluacji ich wyników staje się ważna.

## Cele nauki

Po ukończeniu tej lekcji będziesz wiedzieć jak/rozumieć:
- Podstawowe pojęcia obserwowalności i ewaluacji agentów
- Techniki poprawiające wydajność, koszty i skuteczność agentów
- Co i jak systematycznie oceniać u swoich agentów AI
- Jak kontrolować koszty podczas wdrażania agentów AI do produkcji
- Jak instrumentować agentów zbudowanych przy użyciu Microsoft Agent Framework

Celem jest wyposażenie Cię w wiedzę, która pozwoli przekształcić Twoich agentów „czarna skrzynka” w przejrzyste, zarządzalne i niezawodne systemy.

_**Uwaga:** Ważne jest, aby wdrażać agentów AI, którzy są bezpieczni i godni zaufania. Sprawdź także lekcję [Budowanie godnych zaufania agentów AI](./06-building-trustworthy-agents/README.md)._

## Ślady i rozpiętości

Narzędzia do obserwowalności, takie jak [Langfuse](https://langfuse.com/) lub [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry), zazwyczaj przedstawiają przebiegi agentów jako ślady i rozpiętości.

- **Ślad** reprezentuje kompletną zadanie agenta od początku do końca (np. obsługa zapytania użytkownika).
- **Rozpiętości** to poszczególne kroki w ramach śladu (np. wywołanie modelu językowego lub pobranie danych).

![Drzewo śladu w Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Bez obserwowalności agent AI może przypominać „czarną skrzynkę” – jego stan wewnętrzny i rozumowanie są nieprzejrzyste, co utrudnia diagnozowanie problemów lub optymalizację wydajności. Z obserwowalnością agenci stają się „szklanymi skrzynkami”, oferując przejrzystość niezbędną do budowania zaufania i zapewnienia, że działają zgodnie z zamierzeniem.

## Dlaczego obserwowalność ma znaczenie w środowiskach produkcyjnych

Przeniesienie agentów AI do środowisk produkcyjnych wprowadza nowy zestaw wyzwań i wymagań. Obserwowalność przestaje być „miłym dodatkiem”, stając się krytyczną możliwością:

*   **Debugowanie i analiza przyczyn źródłowych:** Gdy agent zawiedzie lub wygeneruje nieoczekiwany wynik, narzędzia obserwowalności dostarczają ślady potrzebne do zlokalizowania źródła błędu. Jest to szczególnie ważne w złożonych agentach, które mogą wykorzystywać wiele wywołań LLM, interakcji z narzędziami i logikę warunkową.
*   **Zarządzanie opóźnieniami i kosztami:** Agenci AI często korzystają z LLM i innych zewnętrznych API rozliczanych za token lub wywołanie. Obserwowalność pozwala na precyzyjne śledzenie tych wywołań, pomagając zidentyfikować operacje nadmiernie wolne lub kosztowne. Umożliwia to zespołom optymalizację promptów, wybór wydajniejszych modeli lub przebudowę procesów w celu kontroli kosztów operacyjnych i zapewnienia dobrej jakości użytkowania.
*   **Zaufanie, bezpieczeństwo i zgodność:** W wielu zastosowaniach ważne jest, aby agenci zachowywali się bezpiecznie i etycznie. Obserwowalność zapewnia ścieżkę audytu działań i decyzji agenta. Może być wykorzystana do wykrywania i łagodzenia problemów, takich jak wstrzyknięcie promptu, generowanie szkodliwych treści czy niewłaściwe obchodzenie się z danymi osobowymi (PII). Na przykład możesz przejrzeć ślady, aby zrozumieć, dlaczego agent udzielił określonej odpowiedzi lub użył konkretnego narzędzia.
*   **Pętle ciągłego usprawniania:** Dane z obserwowalności stanowią fundament iteracyjnego procesu rozwoju. Monitorując, jak agenci działają w rzeczywistości, zespoły mogą zidentyfikować obszary do poprawy, zebrać dane do dostrajania modeli oraz zweryfikować skutki zmian. Tworzy to pętlę sprzężenia zwrotnego, gdzie wglądy produkcyjne z ewaluacji online informują eksperymenty offline i refinament, prowadząc do coraz lepszej wydajności.

## Kluczowe metryki do śledzenia

Aby monitorować i rozumieć zachowanie agentów, należy śledzić szereg metryk i sygnałów. Konkretne metryki mogą się różnić w zależności od celu agenta, ale niektóre są uniwersalnie ważne.

Oto niektóre z najczęściej monitorowanych metryk przez narzędzia obserwowalności:

**Opóźnienie:** Jak szybko agent odpowiada? Długie czasy oczekiwania negatywnie wpływają na doświadczenie użytkownika. Powinieneś mierzyć opóźnienie dla zadań i pojedynczych kroków poprzez śledzenie przebiegów agenta. Na przykład agent wymagający 20 sekund na wszystkie wywołania modelu może zostać przyspieszony przez użycie szybszego modelu lub równoległe uruchomienie wywołań modeli.

**Koszty:** Jaki jest koszt za jedno uruchomienie agenta? Agenci AI polegają na wywołaniach LLM rozliczanych za token lub na zewnętrznych API. Częste korzystanie z narzędzi lub wielokrotne promptowanie może szybko podnieść koszty. Na przykład jeśli agent wywołuje LLM pięć razy dla marginalnej poprawy jakości, musisz ocenić, czy koszt jest uzasadniony, czy można zmniejszyć liczbę wywołań lub użyć tańszego modelu. Monitorowanie w czasie rzeczywistym pomaga wykrywać nieoczekiwane skoki (np. błędy powodujące nadmierne pętle API).

**Błędy żądań:** Ile żądań agentowi się nie powiodło? Może to obejmować błędy API lub nieudane wywołania narzędzi. Aby zwiększyć odporność agenta w produkcji, możesz wprowadzić alternatywy lub ponawianie prób. Np. jeśli dostawca LLM A jest niedostępny, przełącz się na dostawcę B jako zapas.

**Opinie użytkowników:** Wdrażanie bezpośrednich ocen użytkowników dostarcza cennych informacji. Może to obejmować wyraźne oceny (👍lubię/👎nie lub gwiazdki 1-5) lub komentarze tekstowe. Stała negatywna informacja zwrotna powinna wzbudzić alarm, ponieważ świadczy o tym, że agent nie działa zgodnie z oczekiwaniami.

**Ukryta opinia użytkowników:** Zachowania użytkowników dostarczają pośrednich informacji zwrotnych nawet bez wyraźnych ocen. Może to obejmować natychmiastowe przeformułowanie pytania, powtarzanie zapytań lub kliknięcie przycisku ponów. Np. powtarzające się pytania wskazują, że agent nie spełnia oczekiwań.

**Dokładność:** Jak często agent generuje prawidłowe lub pożądane wyniki? Definicje dokładności się różnią (np. poprawność rozwiązań, dokładność odzyskiwania informacji, satysfakcja użytkownika). Pierwszym krokiem jest zdefiniowanie, czym jest sukces dla Twojego agenta. Możesz śledzić dokładność przez automatyczne kontrole, oceny ewaluacyjne lub etykiety ukończenia zadania. Na przykład oznaczając ślady jako „powodzenie” lub „niepowodzenie”.

**Automatyczne metryki ewaluacyjne:** Możesz również skonfigurować automatyczne oceny. Na przykład możesz użyć LLM do oceniania wyników agenta, czy są pomocne, dokładne, czy nie. Istnieje także kilka bibliotek open source, które pomagają ocenić różne aspekty agenta. Np. [RAGAS](https://docs.ragas.io/) dla agentów RAG lub [LLM Guard](https://llm-guard.com/) do wykrywania szkodliwego języka czy wstrzyknięć promptów.

W praktyce połączenie tych metryk daje najlepszy obraz zdrowia agenta AI. W tym rozdziale w [przykładowym notatniku](./code_samples/10-expense_claim-demo.ipynb) pokażemy, jak te metryki wyglądają na przykładach, ale najpierw nauczymy się, jak wygląda typowy przepływ pracy ewaluacji.

## Instrumentuj swojego agenta

Aby zbierać dane śledzenia, musisz zainstrumentować swój kod. Celem jest instrumentacja kodu agenta w sposób umożliwiający emitowanie śladów i metryk, które można przechwycić, przetworzyć i zwizualizować na platformie do obserwowalności.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) stało się standardem branżowym w obserwowalności LLM. Dostarcza zestaw API, SDK i narzędzi do generowania, zbierania i eksportowania danych telemetrycznych.

Istnieje wiele bibliotek instrumentacyjnych, które opakowują istniejące frameworki agentów i ułatwiają eksport rozpiętości OpenTelemetry do narzędzi obserwowalności. Microsoft Agent Framework integruje się z OpenTelemetry natywnie. Poniżej przykład instrumentacji agenta MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Wykonanie agenta jest śledzone automatycznie
    pass
```

[Przykładowy notatnik](./code_samples/10-expense_claim-demo.ipynb) w tym rozdziale pokaże, jak instrumentować Twojego agenta MAF.

**Ręczne tworzenie rozpiętości:** Chociaż biblioteki instrumentacyjne dostarczają dobry punkt wyjścia, często potrzebne są bardziej szczegółowe lub niestandardowe informacje. Możesz ręcznie tworzyć rozpiętości, aby dodać niestandardową logikę aplikacji. Co ważniejsze, mogą one wzbogacić automatycznie lub ręcznie tworzone rozpiętości o niestandardowe atrybuty (zwane też tagami lub metadanymi). Te atrybuty mogą obejmować dane specyficzne dla biznesu, pośrednie obliczenia lub kontekst przydatny przy debugowaniu lub analizie, takie jak `user_id`, `session_id` czy `model_version`.

Przykład ręcznego tworzenia śladów i rozpiętości z [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Ewaluacja Agenta

Obserwowalność daje metryki, ale ewaluacja to proces analizy tych danych (i wykonywania testów), aby określić, jak dobrze agent AI działa i jak go można ulepszyć. Innymi słowy, mając te ślady i metryki, jak ich użyć do oceny agenta i podejmowania decyzji?

Regularna ewaluacja jest ważna, ponieważ agenci AI często są niedeterministyczni i mogą ewoluować (poprzez aktualizacje lub dryft zachowania modelu) – bez ewaluacji nie wiedziałbyś, czy Twój „inteligentny agent” faktycznie wykonuje dobrze swoją pracę lub czy nastąpił regres.

Są dwie kategorie ewaluacji agentów AI: **ewaluacja online** i **offline**. Obie są wartościowe i się uzupełniają. Zazwyczaj zaczynamy od ewaluacji offline, ponieważ jest to minimalny niezbędny krok przed wdrożeniem agenta.

### Ewaluacja offline

![Elementy zestawu danych w Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Polega na ocenie agenta w kontrolowanym środowisku, zwykle używając zestawów testowych, a nie żywych zapytań użytkowników. Używasz dobranych zestawów danych, gdzie znasz oczekiwane wyjście lub poprawne zachowanie, a następnie uruchamiasz na nich agenta.

Na przykład, jeśli zbudowałeś agenta rozwiązującego zadania matematyczne słowem, możesz mieć [zestaw testowy](https://huggingface.co/datasets/gsm8k) 100 zadań o znanych odpowiedziach. Ewaluacja offline jest często wykonywana podczas rozwoju (i może być częścią pipeline CI/CD), aby sprawdzić poprawki lub zapobiec regresjom. Zaletą jest to, że jest **powtarzalna i pozwala uzyskać wyraźne metryki dokładności, ponieważ masz prawdziwą wartość odniesienia**. Możesz też symulować zapytania użytkowników i mierzyć odpowiedzi agenta względem idealnych odpowiedzi lub używać automatycznych metryk, jak wyżej.

Głównym wyzwaniem ewaluacji offline jest zapewnienie, że Twój zestaw testowy jest obszerny i pozostaje aktualny – agent może dobrze performować na ustalonym zestawie testowym, ale napotkać bardzo różne zapytania w produkcji. Dlatego należy aktualizować zestawy testowe o nowe przypadki graniczne i przykłady odzwierciedlające realne scenariusze. Przydatna jest mieszanka małych testów „smoke” i większych zestawów ewaluacyjnych: małe zestawy do szybkich kontroli i większe do szerszych metryk wydajności.

### Ewaluacja online

![Przegląd metryk obserwowalności](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Odnosi się do oceny agenta w środowisku na żywo, rzeczywistym, tj. podczas faktycznego użytkowania w produkcji. Ewaluacja online polega na monitorowaniu wydajności agenta na prawdziwych interakcjach użytkowników i ciągłej analizie wyników.

Na przykład możesz śledzić wskaźniki sukcesu, oceny satysfakcji użytkowników lub inne metryki na ruchu na żywo. Zaleta ewaluacji online to to, że **uchwytuje rzeczy, których możesz nie przewidzieć w warunkach laboratoryjnych** – możesz obserwować dryft modelu w czasie (jeśli skuteczność agenta spada wraz ze zmianą wzorców danych wejściowych) i wykrywać nieoczekiwane zapytania lub sytuacje, które nie były w danych testowych. Daje to rzeczywisty obraz zachowania agenta „w naturze”.

Ewaluacja online często obejmuje zbieranie jawnej i ukrytej informacji zwrotnej od użytkowników, jak omówiono wcześniej, oraz ewentualne uruchamianie testów shadow lub A/B (gdzie nowa wersja agenta działa równolegle do starej w celu porównania). Wyzwanie polega na tym, że trudno jest uzyskać wiarygodne etykiety lub oceny dla interakcji na żywo – możesz polegać na opiniach użytkowników lub metrykach pochodnych (np. czy użytkownik kliknął wynik).

### Połączenie obu

Ewaluacje online i offline nie wykluczają się – są bardzo uzupełniające. Wnioski z monitoringu online (np. nowe typy zapytań, na które agent słabo reaguje) mogą być użyte do wzbogacenia i poprawy zestawów testowych offline. Natomiast agenci, którzy dobrze wypadają w testach offline, mogą zostać pewniej wdrożeni i monitorowani online.

Wiele zespołów stosuje pętlę:

_ewaluacja offline -> wdrożenie -> monitoring online -> zbieranie nowych przypadków błędów -> dodanie do zbioru offline -> udoskonalenie agenta -> powtarzanie_.

## Typowe problemy

Podczas wdrażania agentów AI do produkcji możesz napotkać różne wyzwania. Oto niektóre typowe problemy i możliwe rozwiązania:

| **Problem**    | **Potencjalne rozwiązanie**   |
| ------------- | ------------------ |
| Agent AI nie realizuje zadań konsekwentnie | - Doprecyzuj prompt przekazywany agentowi; bądź jasny co do celów.<br>- Zidentyfikuj, gdzie podział zadań na podzadania obsługiwane przez wielu agentów może pomóc. |
| Agent AI wpada w ciągłe pętle | - Upewnij się, że masz jasne warunki zakończenia, by agent wiedział, kiedy zatrzymać proces.<br>- Dla złożonych zadań wymagających rozumowania i planowania użyj większego modelu specjalizowanego w zadaniach rozumowania. |
| Wywołania narzędzi przez agenta AI działają słabo | - Testuj i weryfikuj wyjścia narzędzia poza systemem agenta.<br>- Doprecyzuj parametry, promptowanie i nazewnictwo narzędzi. |
| System wieloagentowy nie działa konsekwentnie | - Doprecyzuj prompty dla każdego agenta, by były specyficzne i odrębne.<br>- Zbuduj hierarchiczny system z agentem „routingowym” lub kontrolerem, który decyduje, który agent jest właściwy. |

Wiele z tych problemów można skuteczniej zidentyfikować mając wdrożoną obserwowalność. Ślady i metryki omówione wcześniej pomagają dokładnie wskazać miejsca w przepływie agenta, w których występują problemy, co znacznie ułatwia debugowanie i optymalizację.

## Zarządzanie kosztami
Oto kilka strategii zarządzania kosztami wdrażania agentów AI do produkcji:

**Używanie mniejszych modeli:** Małe modele językowe (SLM) mogą dobrze sprawdzać się w niektórych przypadkach użycia agentów i znacznie obniżyć koszty. Jak wspomniano wcześniej, zbudowanie systemu oceny do określenia i porównania wydajności w stosunku do większych modeli jest najlepszym sposobem na zrozumienie, jak dobrze SLM poradzi sobie w Twoim przypadku użycia. Rozważ użycie SLM do prostszych zadań, takich jak klasyfikacja intencji czy ekstrakcja parametrów, rezerwując większe modele do bardziej złożonych rozumowań.

**Używanie modelu routera:** Podobną strategią jest użycie różnorodności modeli i rozmiarów. Można wykorzystać LLM/SLM lub funkcję bezserwerową do kierowania zapytań w zależności od złożoności do najbardziej odpowiednich modeli. To również pomoże zmniejszyć koszty, zapewniając jednocześnie wydajność w odpowiednich zadaniach. Na przykład, kieruj proste zapytania do mniejszych, szybszych modeli, a drogie duże modele wykorzystuj tylko do złożonych zadań rozumowania.

**Buforowanie odpowiedzi:** Identyfikowanie częstych zapytań i zadań oraz dostarczanie odpowiedzi zanim trafią do Twojego systemu agentowego to dobry sposób na zmniejszenie liczby podobnych zapytań. Możesz nawet zaimplementować proces identyfikujący, jak bardzo zapytanie jest podobne do tych już zbuforowanych, wykorzystując bardziej podstawowe modele AI. Ta strategia może znacznie obniżyć koszty w przypadku często zadawanych pytań lub typowych przepływów pracy.

## Zobaczmy, jak to działa w praktyce

W [przykładowym notatniku z tej sekcji](./code_samples/10-expense_claim-demo.ipynb) zobaczymy przykłady wykorzystania narzędzi do obserwacji, aby monitorować i oceniać naszego agenta.


### Masz więcej pytań dotyczących agentów AI w produkcji?

Dołącz do [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), aby spotkać się z innymi uczniami, uczestniczyć w godzinach konsultacji i uzyskać odpowiedzi na pytania dotyczące agentów AI.

## Poprzednia lekcja

[Metacognition Design Pattern](../09-metacognition/README.md)

## Następna lekcja

[Agentic Protocols](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczeń AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->