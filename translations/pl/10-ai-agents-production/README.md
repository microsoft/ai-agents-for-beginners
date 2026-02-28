# Agenci AI w produkcji: Obserwowalność i ewaluacja

[![Agenci AI w produkcji](../../../translated_images/pl/lesson-10-thumbnail.2b79a30773db093e.webp)](https://youtu.be/l4TP6IyJxmQ?si=reGOyeqjxFevyDq9)

W miarę jak agenci AI przechodzą od prototypów eksperymentalnych do praktycznych zastosowań, zdolność do rozumienia ich zachowania, monitorowania wydajności i systematycznej oceny wyników staje się istotna.

## Cele nauki

Po ukończeniu tej lekcji będziesz potrafił/rozumiał:
- Podstawowe pojęcia obserwowalności i ewaluacji agentów
- Techniki poprawy wydajności, kosztów i efektywności agentów
- Co i jak systematycznie oceniać w swoich agentach AI
- Jak kontrolować koszty podczas wdrażania agentów AI do produkcji
- Jak instrumentować agentów zbudowanych za pomocą Microsoft Agent Framework

Celem jest wyposażenie Cię w wiedzę, która pozwoli przemienić Twoich „czarnych skrzynek” agentów w transparentne, zarządzalne i wiarygodne systemy.

_**Uwaga:** Ważne jest wdrażanie agentów AI, które są bezpieczne i godne zaufania. Sprawdź również lekcję [Budowanie godnych zaufania agentów AI](./06-building-trustworthy-agents/README.md)._

## Ślady i zakresy (traces and spans)

Narzędzia do obserwowalności, takie jak [Langfuse](https://langfuse.com/) lub [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry), zwykle przedstawiają uruchomienia agentów jako ślady (traces) i zakresy (spans).

- **Ślad (Trace)** reprezentuje całe zadanie agenta od początku do końca (np. obsługa zapytania użytkownika).
- **Zakresy (Spans)** to pojedyncze kroki w śladzie (np. wywołanie modelu językowego lub pobieranie danych).

![Drzewo śladów w Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)
<!-- Image URL retained for illustration purposes -->

Bez obserwowalności agent AI może wydawać się „czarną skrzynką” – jego wewnętrzny stan i procesy są nieprzejrzyste, co utrudnia diagnozowanie problemów lub optymalizację wydajności. Dzięki obserwowalności agenci stają się „szklanymi skrzynkami”, oferując przezroczystość niezbędną do budowania zaufania i zapewnienia działania zgodnie z zamierzeniami.

## Dlaczego obserwowalność ma znaczenie w środowiskach produkcyjnych

Przeniesienie agentów AI do produkcji wiąże się z nowymi wyzwaniami i wymaganiami. Obserwowalność przestaje być „miłym dodatkiem”, a staje się kluczową funkcją:

*   **Debugowanie i analiza przyczyn źródłowych**: Gdy agent zawodzi lub daje nieoczekiwany wynik, narzędzia do obserwowalności dostarczają ślady pozwalające zlokalizować źródło błędu. Jest to szczególnie ważne w złożonych agentach, które mogą wykorzystywać wiele wywołań LLM, interakcje z narzędziami i logikę warunkową.
*   **Zarządzanie latencją i kosztami**: Agenci AI często korzystają z LLM i innych zewnętrznych API rozliczanych za token lub wywołanie. Obserwowalność pozwala dokładnie śledzić te wywołania, pomagając zidentyfikować operacje zbyt wolne lub kosztowne. Dzięki temu zespoły mogą optymalizować prompty, wybierać efektywniejsze modele lub przebudowywać przepływy pracy, by kontrolować koszty operacyjne i zapewnić dobre doświadczenia użytkownika.
*   **Zaufanie, bezpieczeństwo i zgodność**: W wielu zastosowaniach ważne jest, aby agenci zachowywali się bezpiecznie i etycznie. Obserwowalność zapewnia ścieżkę audytu działań i decyzji agenta. Może to służyć do wykrywania i łagodzenia problemów takich jak wstrzyknięcia promptów, generowanie szkodliwych treści czy złe przetwarzanie danych osobowych (PII). Na przykład można przejrzeć ślady, by zrozumieć, dlaczego agent udzielił konkretnej odpowiedzi lub użył określonego narzędzia.
*   **Cykle ciągłego doskonalenia**: Dane z obserwowalności stanowią podstawę iteracyjnego procesu rozwoju. Monitorując działanie agentów w rzeczywistych warunkach, zespoły mogą identyfikować obszary do poprawy, zbierać dane do strojenia modeli i weryfikować skutki zmian. Tworzy to pętlę zwrotną, w której informacje z produkcji z online evaluation wspierają eksperymenty offline, prowadząc do stopniowej poprawy działania agentów.

## Kluczowe metryki do śledzenia

Aby monitorować i rozumieć zachowanie agenta, należy śledzić różnorodne metryki i sygnały. Konkretne metryki mogą się różnić w zależności od celu agenta, ale niektóre są uniwersalne.

Oto niektóre z najczęściej monitorowanych metryk w narzędziach obserwowalności:

**Latencja:** Jak szybko agent odpowiada? Długie czasy oczekiwania negatywnie wpływają na doświadczenie użytkownika. Powinieneś mierzyć latencję zadań i poszczególnych kroków, śledząc przebiegi agenta. Na przykład agent, który zajmuje 20 sekund na wszystkie wywołania modelu, może przyspieszyć, używając szybszego modelu lub wywołując modele równolegle.

**Koszty:** Jaki jest koszt jednego uruchomienia agenta? Agenci AI opierają się na wywołaniach LLM rozliczanych per token lub zewnętrznych API. Częste użycie narzędzi lub wielokrotne prompty szybko zwiększają koszty. Na przykład, jeśli agent wywołuje LLM pięć razy dla minimalnej poprawy jakości, trzeba ocenić, czy koszt jest uzasadniony, czy da się zmniejszyć liczbę wywołań lub użyć tańszego modelu. Monitorowanie w czasie rzeczywistym pomaga też wykrywać niespodziewane skoki (np. błędy powodujące nadmierne pętle API).

**Błędy zapytań:** Ile zapytań agentowi nie powiodło się? Mogą to być błędy API lub nieudane wywołania narzędzi. Aby zwiększyć odporność agenta w produkcji, można ustawić mechanizmy awaryjne lub powtórzenia. Np. jeśli dostawca LLM A jest niedostępny, przełącz się na dostawcę B jako zapasowy.

**Opinie użytkowników:** Bezpośrednie oceny użytkowników dostarczają cennych informacji. Mogą to być oceny wyrażone jawnie (👍kciuk do góry/👎do dołu, ⭐ocena 1-5 gwiazdek) lub komentarze tekstowe. Konsekwentnie negatywne opinie powinny Cię ostrzegać, bo to znak, że agent nie działa zgodnie z oczekiwaniami.

**Umyślne opinie użytkowników:** Zachowania użytkowników dostarczają pośrednich sygnałów, nawet bez jawnych ocen. Może to obejmować natychmiastowe przeformułowanie pytania, powtarzanie zapytań lub klikanie przycisku ponowienia. Np. jeśli widzisz, że użytkownicy wielokrotnie zadają to samo pytanie, to znak, że agent nie spełnia oczekiwań.

**Dokładność:** Jak często agent generuje poprawne lub pożądane wyniki? Definicja dokładności zależy od kontekstu (np. poprawność rozwiązywania problemów, precyzja wyszukiwania informacji, satysfakcja użytkownika). Pierwszym krokiem jest zdefiniowanie, co oznacza sukces dla Twojego agenta. Możesz śledzić dokładność przez automatyczne kontrole, oceny ewaluacyjne lub etykiety ukończenia zadań. Na przykład oznaczając ślady jako „udaną” lub „nieudaną”.

**Automatyczne metryki ewaluacji:** Możesz również ustawić automatyczne ewaluacje. Na przykład wykorzystać LLM do oceniania wyjścia agenta pod kątem użyteczności, dokładności itd. Istnieje kilka bibliotek open source pomagających ocenić różne aspekty agenta, np. [RAGAS](https://docs.ragas.io/) dla agentów RAG lub [LLM Guard](https://llm-guard.com/) do wykrywania szkodliwego języka i wstrzyknięć promptów.

W praktyce połączenie tych metryk daje najlepszy obraz stanu zdrowia agenta AI. W [przykładowym notatniku](./code_samples/10-expense_claim-demo.ipynb) z tego rozdziału pokażemy jak te metryki wyglądają na realnych przykładach, ale najpierw nauczymy się, jak wygląda typowy workflow ewaluacji.

## Instrumentowanie agenta

Aby zbierać dane śledzenia, musisz zainstrumentować swój kod. Celem jest instrumentowanie kodu agenta, aby generował ślady i metryki, które mogą być przechwycone, przetworzone i wizualizowane przez platformę do obserwowalności.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) stało się standardem branżowym w zakresie obserwowalności LLM. Dostarcza zestaw API, SDK i narzędzi do generowania, zbierania i eksportowania danych telemetrycznych.

Istnieje wiele bibliotek do instrumentacji, które opakowują istniejące frameworki agentów i ułatwiają eksportowanie spanów OpenTelemetry do narzędzi obserwowalności. Microsoft Agent Framework integruje się natywnie z OpenTelemetry. Poniżej znajduje się przykład instrumentowania agenta MAF:

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()

with tracer.start_as_current_span("agent_run"):
    # Wykonanie agenta jest śledzone automatycznie
    pass
```

[Przykładowy notatnik](./code_samples/10-expense_claim-demo.ipynb) w tym rozdziale pokazuje, jak instrumentować Twojego agenta MAF.

**Ręczne tworzenie zakresów:** Choć biblioteki instrumentacyjne zapewniają solidną bazę, często potrzebne są bardziej szczegółowe lub niestandardowe informacje. Możesz ręcznie tworzyć zakresy, aby dodać własną logikę aplikacji. Co ważniejsze, możesz wzbogacać automatycznie lub ręcznie tworzone zakresy o niestandardowe atrybuty (zwane też tagami lub metadanymi). Mogą one obejmować dane specyficzne dla biznesu, obliczenia pośrednie lub dowolny kontekst pomocny do debugowania lub analizy, np. `user_id`, `session_id` czy `model_version`.

Przykład ręcznego tworzenia śladów i zakresów za pomocą [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Ewaluacja agenta

Obserwowalność dostarcza nam metryki, ale ewaluacja to proces analizy tych danych (i wykonywania testów), by określić, jak dobrze agent AI działa i jak można go ulepszyć. Innymi słowy, mając ślady i metryki, jak ich użyć do oceny agenta i podejmowania decyzji?

Regularna ewaluacja jest ważna, ponieważ agenci AI często są niedeterministyczni i mogą ewoluować (poprzez aktualizacje lub dryft zachowania modelu) – bez ewaluacji nie wiadomo, czy „inteligentny agent” faktycznie dobrze wykonuje swoje zadanie, czy uległ regresji.

Są dwie kategorie ewaluacji agentów AI: **ewaluacja online** i **ewaluacja offline**. Obie są wartościowe i się uzupełniają. Zazwyczaj zaczynamy od ewaluacji offline, ponieważ jest to minimalny niezbędny krok przed wdrożeniem agenta.

### Ewaluacja offline

![Elementy zbioru danych w Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Polega na ocenie agenta w kontrolowanym środowisku, zwykle z użyciem zestawów testowych, a nie zapytań od użytkowników na żywo. Używasz wyselekcjonowanych zbiorów danych, dla których znasz oczekiwane wyniki lub poprawne zachowanie, a następnie uruchamiasz na nich agenta.

Na przykład jeśli stworzyłeś agenta do rozwiązywania zadań tekstowych z matematyki, możesz mieć [zbiór testowy](https://huggingface.co/datasets/gsm8k) składający się ze 100 zadań z znanymi odpowiedziami. Ewaluacja offline jest często wykonywana podczas rozwoju (i może być elementem pipelines CI/CD) do sprawdzania ulepszeń lub zabezpieczania się przed regresjami. Zaletą jest to, że jest **powtarzalna i daje jasne metryki dokładności, ponieważ masz prawdę bazową**. Możesz również symulować zapytania użytkowników i oceniać odpowiedzi agenta względem idealnych rozwiązań lub używać automatycznych metryk, jak opisano wcześniej.

Wyzwanie ewaluacji offline to zapewnienie, że zbiór testowy jest kompleksowy i aktualny – agent może dobrze radzić sobie na stałym zbiorze testowym, lecz w produkcji napotkać zupełnie inne zapytania. Dlatego warto regularnie aktualizować zbiory testowe o nowe przypadki brzegowe i przykłady odpowiadające rzeczywistym scenariuszom. Przydatne jest połączenie małych „testów dymnych” i większych zestawów ewaluacyjnych: małe do szybkich kontroli, większe dla ogólnych metryk wydajności.

### Ewaluacja online

![Przegląd metryk obserwowalności](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Odnosi się do oceny agenta w środowisku na żywo, czyli podczas rzeczywistego użytkowania w produkcji. Ewaluacja online polega na monitorowaniu wydajności agenta w czasie rzeczywistym i ciągłej analizie wyników.

Na przykład możesz śledzić wskaźniki sukcesu, oceny satysfakcji użytkowników lub inne metryki na ruchu na żywo. Zaletą ewaluacji online jest to, że pozwala **dostrzec rzeczy, które mogą Cię zaskoczyć w laboratorium** – możesz obserwować dryft modelu w czasie (jeśli skuteczność agenta spada wraz ze zmianą wzorców wejściowych) oraz wychwycić nieoczekiwane zapytania lub sytuacje, które nie były uwzględnione w zbiorach testowych. Daje to prawdziwy obraz działania agenta w środowisku produkcyjnym.

Ewaluacja online często obejmuje zbieranie jawnych i umyślnych opinii użytkowników oraz przeprowadzanie testów cieniowych lub testów A/B (gdzie nowa wersja agenta działa równolegle do starej, by porównać wyniki). Wyzwanie polega na trudnościach z uzyskaniem wiarygodnych etykiet lub ocen dla interakcji na żywo – często trzeba polegać na feedbacku użytkowników lub wskaźnikach zadań pośrednich (np. czy użytkownik kliknął wynik).

### Łączenie obu podejść

Ewaluacje online i offline nie wykluczają się, lecz uzupełniają. Wnioski z monitoringu online (np. nowe typy zapytań, w których agent radzi sobie słabo) można wykorzystać do wzbogacenia i poprawy zbiorów testowych offline. Natomiast agenci, którzy dobrze działają w testach offline, mogą być pewniej wdrażani i monitorowani online.

W praktyce wiele zespołów stosuje pętlę:

_ewaluacja offline -> wdrożenie -> monitoring online -> zbieranie nowych przypadków błędów -> dodanie do zbioru offline -> usprawnienie agenta -> powtórka_.

## Typowe problemy

Podczas wdrażania agentów AI do produkcji możesz napotkać różne wyzwania. Oto kilka typowych problemów i ich możliwe rozwiązania:

| **Problem**    | **Potencjalne rozwiązanie**   |
| ------------- | ------------------ |
| Agent AI nie wykonuje zadań spójnie | - Udoskonal prompt wysyłany do agenta; jasno określ cele.<br>- Zastanów się, czy podział zadań na podzadania wykonywane przez wielu agentów nie pomoże. |
| Agent AI wpada w nieskończone pętle  | - Zapewnij jasne warunki zakończenia procesu, aby agent wiedział, kiedy przestać.<br>- W przypadku zadań złożonych wymagających rozumowania i planowania użyj większego modelu specjalizowanego w takich zadaniach. |
| Wywołania narzędzi przez agenta działają nieprawidłowo   | - Przetestuj i zweryfikuj wyniki narzędzi poza systemem agenta.<br>- Udoskonal parametry, prompty i nazewnictwo narzędzi.  |
| System wieloagentowy działa niestabilnie | - Popraw prompt wysyłany do poszczególnych agentów, by był specyficzny i odróżniał się od innych.<br>- Zbuduj hierarchię z agentem sterującym (routingiem), który wybierze odpowiedniego agenta. |

Wiele z tych problemów można skuteczniej wykryć mając włączoną obserwowalność. Ślady i metryki omówione wcześniej pomagają precyzyjnie zlokalizować, gdzie w przepływie pracy agenta pojawiają się kłopoty, co znacznie ułatwia debugowanie i optymalizację.

## Zarządzanie kosztami
Oto kilka strategii zarządzania kosztami wdrażania agentów AI do produkcji:

**Używanie mniejszych modeli:** Małe modele językowe (SLM) mogą dobrze radzić sobie w niektórych zastosowaniach agentowych i znacznie obniżą koszty. Jak wspomniano wcześniej, zbudowanie systemu oceny w celu określenia i porównania wydajności względem większych modeli jest najlepszym sposobem na zrozumienie, jak dobrze SLM sprawdzi się w Twoim przypadku użycia. Rozważ użycie SLM do prostszych zadań, takich jak klasyfikacja intencji lub ekstrakcja parametrów, rezerwując większe modele do skomplikowanych rozumowań.

**Używanie modelu routera:** Podobną strategią jest użycie różnorodności modeli i rozmiarów. Możesz użyć LLM/SLM lub funkcji bezserwerowej do kierowania zapytań na podstawie ich złożoności do najlepiej dopasowanych modeli. Pomoże to również zmniejszyć koszty, jednocześnie zapewniając odpowiednią wydajność przy odpowiednich zadaniach. Na przykład kieruj proste zapytania do mniejszych, szybszych modeli i używaj droższych, dużych modeli tylko do złożonych zadań rozumowania.

**Buforowanie odpowiedzi:** Identyfikowanie wspólnych zapytań i zadań oraz udzielanie odpowiedzi zanim przejdą one przez Twój system agentowy to dobry sposób na zmniejszenie liczby podobnych zapytań. Możesz nawet zaimplementować proces identyfikujący, jak bardzo zapytanie jest podobne do tych w buforze, używając prostszych modeli AI. Ta strategia może znacząco obniżyć koszty w przypadku często zadawanych pytań lub typowych procesów.

## Zobaczmy, jak to działa w praktyce

W [przykładowym notatniku tego rozdziału](./code_samples/10-expense_claim-demo.ipynb) zobaczymy przykłady wykorzystania narzędzi do obserwowalności w celu monitorowania i oceny naszego agenta.

### Masz więcej pytań dotyczących agentów AI w produkcji?

Dołącz do [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), aby spotkać się z innymi uczącymi się, uczestniczyć w godzinach konsultacyjnych i uzyskać odpowiedzi na swoje pytania dotyczące agentów AI.

## Poprzednia lekcja

[Wzorzec projektowy metapoznania](../09-metacognition/README.md)

## Następna lekcja

[Protokoły agentowe](../11-agentic-protocols/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zalecamy skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->