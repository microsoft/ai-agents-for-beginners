# Agentów AI w produkcji: Obserwowalność i ocena

[![Agentów AI w produkcji](../../../translated_images/pl/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

W miarę jak agenci AI przechodzą od prototypów eksperymentalnych do zastosowań w świecie rzeczywistym, zdolność do rozumienia ich zachowania, monitorowania wydajności oraz systematycznej oceny wyników staje się istotna.

## Cele nauki

Po ukończeniu tej lekcji będziesz potrafił/zrozumiesz:
- Podstawowe koncepcje obserwowalności i oceny agentów
- Techniki poprawy wydajności, kosztów i skuteczności agentów
- Co i jak systematycznie oceniać w swoich agentach AI
- Jak kontrolować koszty podczas wdrażania agentów AI do produkcji
- Jak instrumentować agentów zbudowanych za pomocą AutoGen

Celem jest wyposażenie Cię w wiedzę pozwalającą przekształcić Twoich agentów „czarna skrzynka” w systemy przejrzyste, zarządzalne i niezawodne.

_**Uwaga:** Ważne jest wdrażanie agentów AI, które są bezpieczne i godne zaufania. Sprawdź także lekcję [Budowanie godnych zaufania agentów AI](../06-building-trustworthy-agents/README.md)._

## Ślady i zakresy

Narzędzia do obserwowalności takie jak [Langfuse](https://langfuse.com/) czy [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) zwykle przedstawiają uruchomienia agentów jako ślady i zakresy.

- **Ślad** reprezentuje kompletne zadanie agenta od początku do końca (np. obsługę zapytania użytkownika).
- **Zakresy** to poszczególne kroki w śladzie (np. wywołanie modelu językowego lub pobranie danych).

![Drzewo śladów w Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)

Bez obserwowalności agent AI może wydawać się „czarną skrzynką” - jego stan wewnętrzny i proces rozumowania są nieprzejrzyste, co utrudnia diagnozowanie problemów lub optymalizację wydajności. Dzięki obserwowalności agenci stają się „szklanymi skrzynkami”, oferując przejrzystość, która jest kluczowa do budowania zaufania i zapewnienia ich prawidłowego działania.

## Dlaczego obserwowalność jest ważna w środowiskach produkcyjnych

Przeniesienie agentów AI do środowisk produkcyjnych wprowadza nowy zestaw wyzwań i wymagań. Obserwowalność przestaje być „miłym dodatkiem” i staje się krytyczną funkcjonalnością:

*   **Debugowanie i analiza przyczyn źródłowych**: Gdy agent zawodzi lub generuje nieoczekiwany wynik, narzędzia do obserwowalności dostarczają ślady potrzebne do zlokalizowania źródła błędu. Jest to szczególnie ważne w przypadku skomplikowanych agentów, które mogą wykorzystywać wiele wywołań LLM, interakcji z narzędziami i logikę warunkową.
*   **Zarządzanie opóźnieniami i kosztami**: Agenci AI często opierają się na LLM i zewnętrznych API rozliczanych za token lub wywołanie. Obserwowalność pozwala na precyzyjne śledzenie tych wywołań, pomagając zidentyfikować operacje nadmiernie wolne lub kosztowne. To umożliwia zespołom optymalizację promptów, wybór bardziej efektywnych modeli lub przeprojektowanie przepływów pracy w celu zarządzania kosztami operacyjnymi i zapewnienia dobrej jakości obsługi użytkownika.
*   **Zaufanie, bezpieczeństwo i zgodność**: W wielu zastosowaniach ważne jest, aby agenci zachowywali się bezpiecznie i etycznie. Obserwowalność zapewnia ścieżkę audytu działań i decyzji agenta. Może być użyta do wykrywania i łagodzenia problemów takich jak wstrzyknięcia promptów, generowanie szkodliwych treści lub niewłaściwe przetwarzanie danych osobowych (PII). Na przykład możesz przeglądać ślady, aby zrozumieć, dlaczego agent udzielił określonej odpowiedzi lub użył konkretnego narzędzia.
*   **Pętle ciągłego doskonalenia**: Dane z obserwowalności stanowią podstawę iteracyjnego procesu rozwoju. Monitorując, jak agenci działają w rzeczywistym świecie, zespoły mogą identyfikować obszary do poprawy, zbierać dane do dopracowywania modeli i weryfikować wpływ wprowadzanych zmian. Tworzy to sprzężenie zwrotne, w którym produkcyjne insighty z oceny online wpływają na eksperymenty offline i udoskonalenia, prowadząc do stopniowo lepszej wydajności agenta.

## Kluczowe metryki do śledzenia

Aby monitorować i rozumieć zachowanie agenta, należy śledzić szereg metryk i sygnałów. Choć konkretne metryki mogą się różnić w zależności od celu agenta, niektóre są uniwersalnie ważne.

Oto kilka najczęściej monitorowanych metryk przez narzędzia do obserwowalności:

**Opóźnienie:** Jak szybko agent odpowiada? Długie czasy oczekiwania negatywnie wpływają na doświadczenie użytkownika. Powinieneś mierzyć opóźnienie dla zadań i poszczególnych kroków, śledząc przebiegi agenta. Na przykład agent, który na wszystkie wywołania modelu potrzebuje 20 sekund, mógłby zostać przyspieszony przez zastosowanie szybszego modelu lub wywoływanie modeli równolegle.

**Koszty:** Jaki jest koszt pojedynczego uruchomienia agenta? Agenci AI opierają się na wywołaniach LLM rozliczanych za token lub zewnętrznych API. Częste użycie narzędzi lub wiele promptów może szybko zwiększyć koszty. Na przykład jeśli agent wywołuje LLM pięć razy, by osiągnąć niewielką poprawę jakości, musisz ocenić, czy koszt jest uzasadniony, czy można ograniczyć liczbę wywołań lub użyć tańszego modelu. Monitorowanie w czasie rzeczywistym pomaga także wykryć nieoczekiwane skoki (np. błędy powodujące nadmierne pętle API).

**Błędy żądań:** Ile żądań nie powiodło się? Może to obejmować błędy API lub nieudane wywołania narzędzi. Aby uczynić agenta bardziej odpornym w produkcji, możesz wtedy wprowadzić mechanizmy zapasowe lub ponowne próby. Np. jeśli dostawca LLM A jest niedostępny, przełączasz się zapasowo na dostawcę B.

**Opinie użytkowników:** Wdrożenie bezpośredniej ewaluacji użytkowników zapewnia cenne informacje. Może to obejmować jawne oceny (👍lajk/👎dislajk, ⭐1-5 gwiazdek) lub komentarze tekstowe. Konsekwentnie negatywne opinie powinny Cię zaalarmować – to znak, że agent nie działa zgodnie z oczekiwaniami.

**Niejawne opinie użytkowników:** Zachowania użytkowników dostarczają pośredniego feedbacku nawet bez jawnych ocen. Może to obejmować natychmiastowe przeformułowanie pytania, wielokrotne zapytania lub klikanie przycisku ponów. Np. jeśli widzisz, że użytkownicy wielokrotnie zadają to samo pytanie, to znak, że agent nie działa zgodnie z oczekiwaniami.

**Dokładność:** Jak często agent generuje poprawne lub pożądane wyniki? Definicje dokładności mogą się różnić (np. poprawność rozwiązywania problemów, dokładność wyszukiwania informacji, satysfakcja użytkownika). Pierwszym krokiem jest określenie, jak wygląda sukces dla Twojego agenta. Możesz mierzyć dokładność poprzez automatyczne sprawdzenia, oceny ewaluacyjne lub oznaczenia ukończenia zadania. Na przykład oznaczając ślady jako „powodzenie” lub „niepowodzenie”.

**Automatyczne metryki oceny:** Można również ustawić automatyczne ewaluacje. Na przykład, możesz użyć LLM do oceniania outputu agenta, np. czy jest pomocny, dokładny, czy nie. Istnieje wiele otwartych bibliotek, które pomagają oceniać różne aspekty agenta. Np. [RAGAS](https://docs.ragas.io/) dla agentów RAG lub [LLM Guard](https://llm-guard.com/) do wykrywania szkodliwego języka lub wstrzyknięć promptów.

W praktyce kombinacja tych metryk zapewnia najlepszy obraz kondycji agenta AI. W [przykładowym notatniku](./code_samples/10_autogen_evaluation.ipynb) tego rozdziału pokażemy, jak te metryki wyglądają na przykładach, ale najpierw nauczymy się, jak wygląda typowy proces ewaluacji.

## Instrumentuj swojego agenta

Aby zbierać dane śledzenia, musisz instrumentować swój kod. Celem jest instrumentacja kodu agenta, aby emitował ślady i metryki, które mogą być przechwytywane, przetwarzane i wizualizowane przez platformę obserwowalności.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) stało się standardem branżowym dla obserwowalności LLM. Zapewnia zestaw API, SDK i narzędzi do generowania, zbierania i eksportowania danych telemetrycznych.

Istnieje wiele bibliotek instrumentacyjnych, które opakowują istniejące frameworki agentów i ułatwiają eksportowanie zakresów OpenTelemetry do narzędzia obserwowalności. Poniżej przykład instrumentacji agenta AutoGen z wykorzystaniem biblioteki instrumentacji [OpenLit](https://github.com/openlit/openlit):

```python
import openlit

openlit.init(tracer = langfuse._otel_tracer, disable_batch = True)
```

[Przykładowy notatnik](./code_samples/10_autogen_evaluation.ipynb) w tym rozdziale pokaże, jak instrumentować swojego agenta AutoGen.

**Ręczne tworzenie zakresów:** Chociaż biblioteki instrumentacyjne zapewniają dobrą bazę, często potrzebne są bardziej szczegółowe lub niestandardowe informacje. Możesz ręcznie tworzyć zakresy, aby dodać własną logikę aplikacji. Co ważniejsze, można wzbogacić automatycznie lub ręcznie tworzone zakresy o niestandardowe atrybuty (zwane także tagami lub metadanymi). Atrybuty te mogą zawierać dane specyficzne dla biznesu, obliczenia pośrednie lub kontekst przydatny do debugowania lub analizy, takie jak `user_id`, `session_id` lub `model_version`.

Przykład ręcznego tworzenia śladów i zakresów z użyciem [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Ewaluacja agenta

Obserwowalność dostarcza metryk, ale ocena to proces analizy tych danych (i wykonywania testów), by określić, jak dobrze agent AI działa i jak można go poprawić. Innymi słowy, gdy masz już ślady i metryki, jak ich użyć do oceny agenta i podejmowania decyzji?

Regularna ocena jest ważna, ponieważ agenci AI często są niedeterministyczni i mogą ewoluować (przez aktualizacje lub dryft zachowania modelu) – bez oceny nie wiedziałbyś, czy Twój „inteligentny agent” faktycznie dobrze wykonuje swoje zadanie, czy nastąpił regres.

Istnieją dwie kategorie ocen dla agentów AI: **ocena online** i **ocena offline**. Obie są wartościowe i się uzupełniają. Zazwyczaj zaczynamy od oceny offline, ponieważ jest to minimalny niezbędny krok przed wdrożeniem jakiegokolwiek agenta.

### Ocena offline

![Elementy zbioru danych w Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Polega na ocenie agenta w kontrolowanym środowisku, zazwyczaj przy użyciu zbiorów testowych, a nie zapytań użytkowników na żywo. Używasz kuratorowanych zbiorów danych, w których znasz oczekiwany wynik lub poprawne zachowanie, a następnie uruchamiasz na nich agenta.

Na przykład, jeśli zbudowałeś agenta do rozwiązywania zadań tekstowych z matematyki, możesz mieć [zbiór testowy](https://huggingface.co/datasets/gsm8k) 100 problemów z znanymi odpowiedziami. Ocena offline jest często przeprowadzana podczas rozwoju (i może być częścią pipeline'ów CI/CD), by sprawdzać poprawki lub chronić przed regresją. Zaleta jest taka, że jest **powtarzalna i możesz uzyskać wyraźne metryki dokładności, bo masz prawdziwe odpowiedzi**. Możesz także symulować zapytania użytkownika i mierzyć odpowiedzi agenta względem idealnych odpowiedzi lub używać automatycznych metryk opisanych wyżej.

Kluczowe wyzwanie oceny offline to zapewnienie, że Twój zbiór testowy jest kompleksowy i pozostaje aktualny – agent może dobrze działać na stałym zbiorze testowym, ale napotkać zupełnie inne zapytania w produkcji. Dlatego należy aktualizować zestawy testowe o nowe przypadki graniczne i przykłady odzwierciedlające scenariusze z prawdziwego świata. Przydatne jest połączenie małych „testów dymnych” i większych zestawów ewaluacyjnych: małe zestawy do szybkich kontroli i większe do szerszych metryk wydajności.

### Ocena online

![Przegląd metryk obserwowalności](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Odnosi się do oceny agenta w środowisku na żywo, rzeczywistym, tj. podczas faktycznego użytkowania w produkcji. Ocena online polega na monitorowaniu wydajności agenta na prawdziwych interakcjach użytkowników i ciągłej analizie wyników.

Na przykład możesz śledzić wskaźniki sukcesu, oceny satysfakcji użytkownika lub inne metryki na ruchu na żywo. Zaleta oceny online jest taka, że **uchwytuje rzeczy, których możesz nie przewidzieć w laboratorium** – możesz obserwować dryft modelu w czasie (jeśli wydajność agenta pogarsza się wraz ze zmianą wzorców wejścia) i wyłapywać nieoczekiwane zapytania lub sytuacje, które nie występowały w danych testowych. Dostarcza prawdziwy obraz zachowania agenta na wolności.

Ocena online często obejmuje zbieranie jawnych i niejawnych opinii użytkowników, jak opisano wyżej, a także potencjalnie przeprowadzanie testów w tle lub testów A/B (gdzie nowa wersja agenta działa równolegle, by porównać ją ze starą). Wyzwanie polega na tym, że może być trudno uzyskać wiarygodne oznaczenia lub oceny dla interakcji na żywo – możesz polegać na feedbacku użytkowników lub metrykach pochodnych (np. czy użytkownik kliknął wynik).

### Łączenie obu

Oceny online i offline nie wykluczają się wzajemnie; są bardzo uzupełniające. Wnioski z monitoringu online (np. nowe typy zapytań użytkowników, na które agent słabo reaguje) mogą służyć do wzbogacenia i ulepszenia offline zestawów testowych. Natomiast agenci dobrze wypadający w testach offline mogą być z większą pewnością wdrażani i monitorowani online.

W rzeczywistości wiele zespołów stosuje pętlę:

_ocena offline -> wdrożenie -> monitoring online -> zbieranie nowych przypadków błędów -> dodanie do zbioru offline -> udoskonalenie agenta -> powtórz_.

## Typowe problemy

Podczas wdrażania agentów AI do produkcji możesz napotkać różne wyzwania. Oto niektóre typowe problemy i ich potencjalne rozwiązania:

| **Problem**    | **Potencjalne rozwiązanie**   |
| ------------- | ------------------ |
| Agent AI nie wykonuje zadań konsekwentnie | - Doprecyzuj prompt przekazywany agentowi AI; bądź jasny co do celów.<br>- Zidentyfikuj, gdzie podział zadań na podzadania obsługiwane przez wielu agentów może pomóc. |
| Agent AI wpada w ciągłe pętle  | - Upewnij się, że masz klarowne warunki zakończenia, aby agent wiedział, kiedy zatrzymać proces.<br>- Dla zadań wymagających rozumowania i planowania użyj większego modelu specjalizującego się w rozumowaniu. |
| Wywołania narzędzi agenta AI nie działają poprawnie   | - Testuj i weryfikuj wyniki narzędzia poza systemem agenta.<br>- Doprecyzuj parametry, prompty i nazwy narzędzi.  |
| System wieloagentowy działa niespójnie | - Doprecyzuj prompt dla każdego agenta, aby były specyficzne i odróżniały się od siebie.<br>- Zbuduj system hierarchiczny, wykorzystując agenta „routingu” lub kontrolera do określenia, który agent jest odpowiedni. |

Wiele z tych problemów można skuteczniej zidentyfikować dzięki obserwowalności. Omówione wcześniej ślady i metryki pomagają precyzyjnie wskazać, w którym miejscu w przepływie agenta występują problemy, co znacznie ułatwia debugowanie i optymalizację.

## Zarządzanie kosztami
Oto kilka strategii zarządzania kosztami wdrażania agentów AI do produkcji:

**Używanie mniejszych modeli:** Małe modele językowe (SLM) mogą dobrze sprawdzać się w niektórych przypadkach użycia agentów i znacznie obniżą koszty. Jak wspomniano wcześniej, stworzenie systemu oceny, który określi i porówna wydajność względem większych modeli, jest najlepszym sposobem, aby zrozumieć, jak dobrze SLM poradzi sobie w Twoim przypadku użycia. Rozważ użycie SLM do prostszych zadań, takich jak klasyfikacja intencji czy ekstrakcja parametrów, rezerwując większe modele do skomplikowanego rozumowania.

**Używanie modelu routera:** Podobną strategią jest użycie różnorodnych modeli i rozmiarów. Możesz użyć LLM/SLM albo funkcji bezserwerowej, aby kierować zapytania na podstawie ich złożoności do najlepiej dopasowanych modeli. To również pomoże obniżyć koszty, jednocześnie zapewniając wydajność przy odpowiednich zadaniach. Na przykład, kieruj proste zapytania do mniejszych, szybszych modeli, a kosztowne duże modele wykorzystuj tylko do zadań związanych ze złożonym rozumowaniem.

**Buforowanie odpowiedzi:** Identyfikowanie częstych zapytań i zadań oraz zapewnianie odpowiedzi zanim przejdą one przez Twój system agentowy to dobry sposób na zmniejszenie liczby podobnych zapytań. Możesz nawet zaimplementować mechanizm, który określi, jak bardzo zapytanie jest podobne do już zbuforowanych, wykorzystując bardziej podstawowe modele AI. Ta strategia może znacząco obniżyć koszty przy często zadawanych pytaniach lub popularnych przepływach pracy.

## Zobaczmy, jak to działa w praktyce

W [przykładowym notatniku z tej sekcji](./code_samples/10_autogen_evaluation.ipynb) zobaczymy przykłady, jak można wykorzystać narzędzia do obserwowalności, aby monitorować i oceniać naszego agenta.


### Masz więcej pytań dotyczących agentów AI w produkcji?

Dołącz do [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), aby spotkać się z innymi uczącymi się, uczestniczyć w godzinach konsultacji i uzyskać odpowiedzi na swoje pytania dotyczące agentów AI.

## Poprzednia lekcja

[Metacognition Design Pattern](../09-metacognition/README.md)

## Następna lekcja

[Agentic Protocols](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Ten dokument został przetłumaczony przy użyciu usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że staramy się zapewnić dokładność, prosimy pamiętać, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło obowiązujące. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->