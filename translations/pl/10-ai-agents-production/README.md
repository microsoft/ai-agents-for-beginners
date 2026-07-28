# Agenci AI w Produkcji: Obserwowalność i Ocena

[![Agenci AI w Produkcji](../../../translated_images/pl/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

W miarę jak agenci AI przechodzą od prototypów eksperymentalnych do zastosowań w rzeczywistym świecie, zdolność do rozumienia ich zachowania, monitorowania wydajności i systematycznej oceny wyników staje się istotna.

## Cele nauki

Po ukończeniu tej lekcji będziesz znać/jak zrozumieć:
- Kluczowe pojęcia obserwowalności i oceny agentów
- Techniki poprawy wydajności, kosztów i efektywności agentów
- Co i jak systematycznie oceniać swoich agentów AI
- Jak kontrolować koszty przy wdrażaniu agentów AI do produkcji
- Jak instrumentować agentów zbudowanych za pomocą Microsoft Agent Framework

Celem jest wyposażenie Cię w wiedzę potrzebną do przekształcenia Twoich agentów z „czarnej skrzynki” w systemy przejrzyste, łatwe do zarządzania i niezawodne.

_**Uwaga:** Ważne jest wdrażanie agentów AI, które są bezpieczne i godne zaufania. Sprawdź także lekcję [Budowanie godnych zaufania agentów AI](../06-building-trustworthy-agents/README.md)._

## Ślady i zakresy

Narzędzia do obserwowalności takie jak [Langfuse](https://langfuse.com/) lub [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry) zazwyczaj przedstawiają działanie agenta jako ślady i zakresy.

- **Ślad** reprezentuje kompletne zadanie agenta od początku do końca (np. obsługa zapytania użytkownika).
- **Zakresy** to poszczególne kroki w obrębie śladu (np. wywołanie modelu językowego lub pobranie danych).

![Drzewo śladu w Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Bez obserwowalności agent AI może wydawać się „czarną skrzynką” – jego stan wewnętrzny i rozumowanie są nieprzejrzyste, co utrudnia diagnozę problemów lub optymalizację wydajności. Z obserwowalnością agenci stają się „szklanymi skrzynkami”, oferując przejrzystość niezbędną do budowania zaufania i zapewnienia ich działania zgodnie z zamierzeniami.

## Dlaczego obserwowalność ma znaczenie w środowiskach produkcyjnych

Przeniesienie agentów AI do środowisk produkcyjnych wiąże się z nowym zestawem wyzwań i wymagań. Obserwowalność przestaje być „miłym dodatkiem”, stając się krytyczną funkcjonalnością:

*   **Debugowanie i analiza przyczyny źródłowej**: Gdy agent zawiedzie lub wygeneruje nieoczekiwany wynik, narzędzia obserwowalności dostarczają ślady potrzebne do zlokalizowania źródła błędu. Jest to szczególnie ważne w złożonych agentach, które mogą obsługiwać wiele wywołań LLM, interakcje z narzędziami i logikę warunkową.
*   **Zarządzanie opóźnieniami i kosztami**: Agenci AI często korzystają z LLM i innych zewnętrznych API, które są rozliczane za token lub za wywołanie. Obserwowalność pozwala precyzyjnie śledzić te wywołania, pomagając zidentyfikować operacje zbyt wolne lub kosztowne. Umożliwia to zespołom optymalizację zapytań, wybór wydajniejszych modeli lub przeprojektowanie procesów w celu kontrolowania kosztów operacyjnych i zapewnienia dobrej jakości doświadczenia użytkownika.
*   **Zaufanie, bezpieczeństwo i zgodność**: W wielu zastosowaniach ważne jest zapewnienie, że agenci zachowują się bezpiecznie i etycznie. Obserwowalność zapewnia ślad audytu działań i decyzji agenta. Można go użyć do wykrywania i łagodzenia problemów, takich jak wstrzyknięcia zapytań, generowanie szkodliwych treści lub niewłaściwe przetwarzanie danych osobowych (PII). Na przykład, możesz przeglądać ślady, aby zrozumieć, dlaczego agent udzielił konkretnej odpowiedzi lub użył konkretnego narzędzia.
*   **Ciągłe pętle doskonalenia**: Dane obserwowalności są fundamentem iteracyjnego procesu rozwoju. Monitorując, jak agenci działają w rzeczywistości, zespoły mogą identyfikować obszary do poprawy, zbierać dane do dopasowywania modeli i weryfikować wpływ zmian. Tworzy to pętlę zwrotną, gdzie spostrzeżenia z produkcji uzyskane z oceny online informują eksperymenty i udoskonalenia offline, prowadząc do stopniowo lepszej wydajności agenta.

## Kluczowe metryki do śledzenia

Aby monitorować i rozumieć zachowanie agenta, należy śledzić szereg metryk i sygnałów. Chociaż konkretne metryki mogą się różnić w zależności od celu agenta, niektóre mają uniwersalne znaczenie.

Oto niektóre z najczęściej monitorowanych metryk przez narzędzia obserwowalności:

**Opóźnienie:** Jak szybko agent odpowiada? Długie czasy oczekiwania negatywnie wpływają na doświadczenie użytkownika. Powinieneś mierzyć opóźnienia dla zadań i poszczególnych kroków, śledząc przebieg działania agenta. Na przykład agent, który potrzebuje 20 sekund na wszystkie wywołania modelu, może przyspieszyć, używając szybszego modelu lub wykonując wywołania równolegle.

**Koszty:** Jaki jest koszt za jedno wykonanie agenta? Agenci AI opierają się na wywołaniach LLM rozliczanych za token lub zewnętrznych API. Częste korzystanie z narzędzi lub wielokrotne zapytania mogą szybko zwiększyć koszty. Na przykład, jeśli agent wywołuje LLM pięć razy dla niewielkiej poprawy jakości, musisz ocenić, czy koszt jest uzasadniony lub czy można zmniejszyć liczbę wywołań albo użyć tańszego modelu. Monitorowanie w czasie rzeczywistym może też pomóc wykryć niespodziewane skoki (np. błędy powodujące nadmierne pętle API).

**Błędy zapytań:** Ile zapytań nie powiodło się? Może to obejmować błędy API lub nieudane wywołania narzędzi. Aby uczynić agenta bardziej odpornym na takie sytuacje w produkcji, możesz ustawić zapasowe mechanizmy lub próby ponownego wywołania. Np. jeśli dostawca LLM A jest niedostępny, przełączasz się na dostawcę B jako zapas.

**Opinie użytkowników:** Implementacja bezpośrednich ocen użytkowników dostarcza cennych informacji. Może to obejmować wyraźne oceny (👍kciuk w górę/👎w dół, ⭐1-5 gwiazdek) lub komentarze tekstowe. Stała negatywna opinia powinna Cię zaalarmować, ponieważ jest znakiem, że agent nie działa zgodnie z oczekiwaniami.

**Pośrednia opinia użytkowników:** Zachowania użytkowników dostarczają pośredniego feedbacku nawet bez wyraźnych ocen. Może to obejmować natychmiastowe przeformułowanie pytania, powtarzane zapytania lub kliknięcie przycisku ponów. Np. jeśli widzisz, że użytkownicy wielokrotnie zadają to samo pytanie, jest to sygnał, że agent nie działa zgodnie z oczekiwaniami.

**Dokładność:** Jak często agent generuje poprawne lub pożądane wyniki? Definicje dokładności różnią się (np. poprawność rozwiązywania problemów, dokładność wyszukiwania informacji, satysfakcja użytkownika). Pierwszym krokiem jest zdefiniowanie, czym jest sukces dla Twojego agenta. Możesz śledzić dokładność za pomocą automatycznych testów, ocen ewaluacyjnych lub oznaczeń ukończenia zadań. Na przykład oznaczając ślady jako „powodzenie” lub „niepowodzenie”.

**Automatyczne metryki ewaluacyjne:** Możesz także skonfigurować automatyczne testy. Na przykład możesz użyć LLM do oceniania wyników agenta, na przykład czy są pomocne, dokładne, czy nie. Istnieje również kilka bibliotek open source, które pomagają oceniać różne aspekty agenta. Np. [RAGAS](https://docs.ragas.io/) dla agentów RAG lub [LLM Guard](https://llm-guard.com/) do wykrywania szkodliwego języka lub wstrzyknięć zapytań.

W praktyce połączenie tych metryk daje najlepszy obraz zdrowia agenta AI. W [przykładowym notatniku](./code_samples/10-expense_claim-demo.ipynb) w tym rozdziale pokażemy, jak te metryki wyglądają na konkretnych przykładach, ale najpierw nauczymy się, jak wygląda typowy przepływ pracy oceny.

## Instrumentuj swojego agenta

Aby zbierać dane śledzenia, musisz zaimplementować instrumentację swojego kodu. Celem jest instrumentowanie kodu agenta, aby emitował ślady i metryki, które mogą być przechwycone, przetworzone i wizualizowane przez platformę obserwowalności.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) stał się standardem branżowym dla obserwowalności LLM. Dostarcza zestaw API, SDK i narzędzi do generowania, zbierania i eksportowania danych telemetrycznych.

Istnieje wiele bibliotek instrumentacyjnych, które opakowują istniejące frameworki agentów i ułatwiają eksportowanie zakresów OpenTelemetry do narzędzia obserwowalności. Microsoft Agent Framework natywnie integruje się z OpenTelemetry. Poniżej przykład instrumentacji agenta MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Wykonanie agenta jest śledzone automatycznie
    pass
```

[Przykładowy notatnik](./code_samples/10-expense_claim-demo.ipynb) w tym rozdziale pokaże, jak instrumentować swojego agenta MAF.

**Ręczne tworzenie zakresów:** Choć biblioteki instrumentacyjne zapewniają dobrą podstawę, często potrzebne są bardziej szczegółowe lub niestandardowe informacje. Możesz ręcznie tworzyć zakresy, aby dodać niestandardową logikę aplikacji. Co ważniejsze, mogą one wzbogacać automatycznie lub ręcznie tworzone zakresy o niestandardowe atrybuty (zwane też tagami lub metadanymi). Atrybuty te mogą zawierać dane specyficzne dla biznesu, obliczenia pośrednie lub dowolny kontekst użyteczny do debugowania lub analizy, taki jak `user_id`, `session_id` czy `model_version`.

Przykład ręcznego tworzenia śladów i zakresów za pomocą [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Ocena agenta

Obserwowalność dostarcza nam metryk, ale ocena to proces analizowania tych danych (i przeprowadzania testów), aby określić, jak dobrze agent AI działa i jak można go poprawić. Innymi słowy, gdy masz te ślady i metryki, jak ich użyć do oceny agenta i podejmowania decyzji?

Regularna ocena jest ważna, ponieważ agenci AI często są niedeterministyczni i mogą się zmieniać (przez aktualizacje lub dryftowanie zachowania modelu) – bez oceny nie wiedziałbyś, czy Twój „inteligentny agent” rzeczywiście dobrze wykonuje swoją pracę, czy też jego działanie się pogorszyło.

Istnieją dwie kategorie ocen dla agentów AI: **ocena online** i **ocena offline**. Obie są wartościowe i się uzupełniają. Zazwyczaj zaczynamy od oceny offline, ponieważ jest to minimalny krok konieczny przed wdrożeniem dowolnego agenta.

### Ocena offline

![Elementy zbioru danych w Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Obejmuje ocenę agenta w kontrolowanym środowisku, zwykle za pomocą zestawów testowych, a nie zapytań na żywo od użytkowników. Używasz wyselekcjonowanych zestawów danych, gdzie znasz oczekiwany wynik lub prawidłowe zachowanie, a następnie testujesz na nich agenta.

Na przykład, jeśli zbudowałeś agenta do rozwiązywania zadań tekstowych z matematyki, możesz mieć [zestaw testowy](https://huggingface.co/datasets/gsm8k) zawierający 100 problemów z znanymi odpowiedziami. Ocena offline jest często przeprowadzana podczas rozwoju (i może być częścią pipeline’ów CI/CD) w celu weryfikacji ulepszeń lub ochrony przed regresją. Zaleta jest taka, że jest **powtarzalna i pozwala uzyskać jasne metryki dokładności, ponieważ masz prawdziwe odpowiedzi**. Możesz też symulować zapytania użytkowników i mierzyć odpowiedzi agenta wobec idealnych odpowiedzi lub używać automatycznych metryk opisanych wyżej.

Głównym wyzwaniem oceny offline jest zapewnienie, że zestaw testowy jest wszechstronny i pozostaje aktualny – agent może dobrze radzić sobie na stałym zestawie, ale napotkać zupełnie inne zapytania w produkcji. Dlatego warto aktualizować zestawy testowe o nowe skrajne przypadki i przykłady odzwierciedlające rzeczywiste scenariusze. Przydatne jest łączenie małych „testów dymnych” z większymi zestawami ewaluacyjnymi: małe zestawy do szybkich kontroli, większe do szerszych metryk wydajności.

### Ocena online

![Przegląd metryk obserwowalności](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Odnosi się do oceny agenta w czasie rzeczywistym, w środowisku produkcyjnym, tzn. podczas faktycznego użycia. Ocena online polega na monitorowaniu wydajności agenta podczas rzeczywistych interakcji użytkowników i ciągłej analizie wyników.

Przykładowo możesz śledzić wskaźniki sukcesu, oceny satysfakcji użytkowników lub inne metryki na ruchu na żywo. Zaletą oceny online jest to, że **uchwytuje rzeczy, których możesz nie przewidzieć w środowisku laboratoryjnym** – możesz zaobserwować dryft modelu w czasie (jeśli efektywność agenta pogarsza się wraz ze zmianą wzorców danych wejściowych) oraz wykryć nieoczekiwane zapytania lub sytuacje, które nie były w danych testowych. Dostarcza prawdziwego obrazu zachowania agenta na żywo.

Ocena online często obejmuje zbieranie pośrednich i wyraźnych opinii użytkowników, jak omówiono, oraz ewentualne przeprowadzanie testów cienia lub testów A/B (gdzie nowa wersja agenta działa równolegle, aby porównać ją ze starą). Wyzwanie polega na tym, że trudno jest uzyskać wiarygodne oznaczenia lub wyniki dla interakcji na żywo – możesz polegać na opiniach użytkowników lub metrykach niższego poziomu (np. czy użytkownik kliknął wynik).

### Łączenie obu

Oceny online i offline nie wykluczają się; są bardzo komplementarne. Wnioski z monitoringu na żywo (np. nowe typy zapytań użytkowników, na które agent reaguje słabo) można wykorzystać do rozszerzenia i poprawy zestawów testowych offline. Z kolei agenci, którzy sprawdzają się w testach offline, mogą być z większą pewnością wdrożeni i monitorowani online.

W rzeczywistości wiele zespołów stosuje cykl:

_ocena offline -> wdrożenie -> monitoring online -> zbieranie nowych błędów -> dodawanie do zbioru offline -> doskonalenie agenta -> powtórka_.

## Typowe problemy

W miarę wdrażania agentów AI do produkcji możesz napotkać różne wyzwania. Oto kilka powszechnych problemów i ich potencjalne rozwiązania:

| **Problem**    | **Potencjalne rozwiązanie**   |
| ------------- | ------------------ |
| Agent AI nie wykonuje zadań konsekwentnie | - Doprecyzuj zapytanie (prompt) przekazywane agentowi AI; bądź jasny co do celów.<br>- Zidentyfikuj, gdzie podział zadań na subtasks i obsługa ich przez wielu agentów może pomóc. |
| Agent AI wpada w ciągłe pętle  | - Upewnij się, że masz jasne warunki zakończenia, aby agent wiedział, kiedy zakończyć proces.<br>- Do złożonych zadań wymagających rozumowania i planowania użyj większego modelu specjalizowanego do takich zadań. |
| Wywołania narzędzi agenta AI nie działają dobrze   | - Testuj i weryfikuj output narzędzia poza systemem agenta.<br>- Doprecyzuj parametry, zapytania i nazewnictwo narzędzi.  |
| System Multi-Agent działa niespójnie | - Doprecyzuj zapytania dla każdego agenta, aby były specyficzne i odrębne.<br>- Zbuduj system hierarchiczny z agentem „routingowym” lub kontrolerem, który określa, który agent jest właściwy. |

Wiele z tych problemów można skuteczniej zidentyfikować mając obserwowalność. Ślady i metryki, o których wcześniej mówiliśmy, pomagają dokładnie ustalić, gdzie w przepływie działania agenta występują problemy, co znacznie ułatwia debugowanie i optymalizację.

## Zarządzanie kosztami


Oto kilka strategii zarządzania kosztami wdrażania agentów AI do produkcji:

**Używanie mniejszych modeli:** Małe modele językowe (SLM) mogą dobrze sprawdzać się w niektórych zastosowaniach agentowych i znacznie obniżyć koszty. Jak wspomniano wcześniej, budowanie systemu oceny do określania i porównywania wydajności w stosunku do większych modeli jest najlepszym sposobem, aby zrozumieć, jak dobrze SLM sprawdzi się w Twoim przypadku użycia. Rozważ użycie SLM do prostszych zadań, takich jak klasyfikacja intencji lub ekstrakcja parametrów, pozostawiając większe modele do złożonych rozumowań.

**Używanie modelu routera:** Podobną strategią jest korzystanie z różnorodności modeli i rozmiarów. Możesz użyć LLM/SLM lub funkcji serverless do kierowania zapytań na podstawie ich złożoności do najlepiej dopasowanych modeli. To również pomoże obniżyć koszty, jednocześnie zapewniając wydajność w odpowiednich zadaniach. Na przykład, kieruj proste zapytania do mniejszych, szybszych modeli, a do złożonych zadań rozumowania używaj tylko drogich, dużych modeli.

**Buforowanie odpowiedzi:** Identyfikowanie typowych zapytań i zadań oraz dostarczanie odpowiedzi przed tym, jak trafią do Twojego systemu agentowego, to dobry sposób na zmniejszenie liczby podobnych zapytań. Możesz nawet zaimplementować mechanizm do oceny, jak podobne jest zapytanie do tych już zbuforowanych, używając prostszych modeli AI. Ta strategia może znacznie zmniejszyć koszty dla często zadawanych pytań lub typowych procesów.

## Zobaczmy, jak to działa w praktyce

W [przykładowym zeszycie tego rozdziału](./code_samples/10-expense_claim-demo.ipynb) zobaczymy przykłady, jak możemy używać narzędzi do obserwowalności, by monitorować i oceniać naszego agenta.


### Masz więcej pytań dotyczących agentów AI w produkcji?

Dołącz do [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), aby spotkać innych uczących się, uczestniczyć w godzinach konsultacji i uzyskać odpowiedzi na pytania dotyczące agentów AI.

## Poprzednia lekcja

[Wzorzec projektowy metapoznania](../09-metacognition/README.md)

## Następna lekcja

[Protokoły agentowe](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->