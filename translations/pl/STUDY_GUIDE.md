# Agent AI dla początkujących - Przewodnik i Podsumowanie Kursu

Ten przewodnik zawiera podsumowanie kursu "Agent AI dla początkujących" oraz wyjaśnia kluczowe pojęcia, frameworki i wzorce projektowe do budowy Agentów AI.

## 1. Wprowadzenie do Agentów AI

**Czym są Agenci AI?**
Agenci AI to systemy, które rozszerzają możliwości Dużych Modeli Językowych (LLM) poprzez udostępnienie im **narzędzi**, **wiedzy** i **pamięci**. W przeciwieństwie do standardowego czatu opartego na LLM, który tylko generuje tekst na podstawie danych treningowych, Agent AI potrafi:
- **Percepować** swoje otoczenie (za pomocą czujników lub wejść).
- **Rozumować** jak rozwiązać problem.
- **Działać**, aby zmienić otoczenie (za pomocą siłowników lub wykonania narzędzi).

**Kluczowe elementy Agenta:**
- **Środowisko**: Przestrzeń, w której działa agent (np. system rezerwacji).
- **Czujniki**: Mechanizmy do zbierania informacji (np. odczyt API).
- **Siłowniki**: Mechanizmy do wykonywania działań (np. wysyłanie maila).
- **Mózg (LLM)**: Silnik rozumowania, który planuje i decyduje, jakie działania podjąć.

## 2. Frameworki Agentów

Kurs obejmuje trzy główne frameworki do budowy agentów:

| Framework | Skupienie | Najlepsze zastosowanie |
|-----------|-----------|-----------------------|
| **Semantic Kernel** | Gotowy do produkcji SDK dla .NET/Python | Aplikacje korporacyjne, integracja AI z istniejącym kodem. |
| **AutoGen** | Współpraca wielu agentów | Złożone scenariusze wymagające wielu wyspecjalizowanych agentów komunikujących się ze sobą. |
| **Azure AI Agent Service** | Zarządzana usługa chmurowa | Bezpieczne, skalowalne wdrożenia z wbudowanym zarządzaniem stanem. |

## 3. Wzorce projektowe Agentów

Wzorce projektowe pomagają uporządkować działanie agentów, aby niezawodnie rozwiązywali problemy.

### **Wzorzec użycia narzędzi** (Lekcja 4)
Ten wzorzec umożliwia agentom interakcję ze światem zewnętrznym.
- **Koncepcja**: Agent otrzymuje „schemat” (listę dostępnych funkcji i ich parametrów). LLM decyduje, *które* narzędzie wywołać i z *jakimi* argumentami na podstawie żądania użytkownika.
- **Przebieg**: Żądanie użytkownika -> LLM -> **Wybór narzędzia** -> **Wykonanie narzędzia** -> LLM (ze zwrotem z narzędzia) -> Ostateczna odpowiedź.
- **Przypadki użycia**: Pobieranie danych w czasie rzeczywistym (pogoda, ceny akcji), wykonywanie obliczeń, uruchamianie kodu.

### **Wzorzec planowania** (Lekcja 7)
Ten wzorzec pozwala agentom rozwiązywać złożone zadania wieloetapowe.
- **Koncepcja**: Agent dzieli cel wysokiego poziomu na sekwencję mniejszych podzadań.
- **Podejścia**:
  - **Dekonstrukcja zadania**: Podział „Zaplanuj podróż” na „Zarezerwuj lot”, „Zarezerwuj hotel”, „Wypożycz auto”.
  - **Planowanie iteracyjne**: Ponowna ocena planu na podstawie wyników wcześniejszych kroków (np. jeśli lot jest pełny, wybierz inny termin).
- **Implementacja**: Często obejmuje agenta "Plannera", który generuje ustrukturyzowany plan (np. JSON), który jest następnie wykonywany przez innych agentów.

## 4. Zasady projektowe

Projektując agentów, rozważ trzy wymiary:
- **Przestrzeń**: Agenci powinni łączyć ludzi i wiedzę, być dostępni, ale nie narzucający się.
- **Czas**: Agenci powinni uczyć się z *przeszłości*, dostarczać odpowiednie wskazówki *teraz* i adaptować się na *przyszłość*.
- **Rdzeń**: Akceptuj niepewność, ale buduj zaufanie poprzez przejrzystość i kontrolę użytkownika.

## 5. Podsumowanie kluczowych lekcji

- **Lekcja 1**: Agenci to systemy, nie tylko modele. Percepować, rozumować i działać.
- **Lekcja 2**: Frameworki jak Semantic Kernel i AutoGen upraszczają wywoływanie narzędzi i zarządzanie stanem.
- **Lekcja 3**: Projektuj z myślą o przejrzystości i kontroli użytkownika.
- **Lekcja 4**: Narzędzia to „ręce” agenta. Definicja schematu jest kluczowa, aby LLM wiedział jak ich używać.
- **Lekcja 7**: Planowanie to „funkcja wykonawcza” agenta, pozwalająca mu realizować złożone procesy.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą automatycznej usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Pomimo naszych starań o dokładność, prosimy mieć na uwadze, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->