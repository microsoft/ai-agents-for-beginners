# Agenci AI dla początkujących - Przewodnik i podsumowanie kursu

Ten przewodnik zawiera streszczenie kursu "AI Agents for Beginners" i wyjaśnia kluczowe koncepcje, ramy i wzorce projektowe do budowania agentów AI.

## 1. Wprowadzenie do agentów AI

**Czym są agenci AI?**
Agenci AI to systemy, które rozszerzają możliwości Large Language Models (LLM) poprzez udostępnienie im **narzędzi**, **wiedzy** i **pamięci**. W przeciwieństwie do standardowego chatbota LLM, który generuje tekst tylko na podstawie danych treningowych, agent AI może:
- **Percepować** swoje środowisko (za pomocą sensorów lub wejść).
- **Rozumować** o tym, jak rozwiązać problem.
- **Działać**, aby zmienić środowisko (za pomocą aktuatorów lub wykonywania narzędzi).

**Kluczowe komponenty agenta:**
- **Środowisko**: Przestrzeń, w której agent działa (np. system rezerwacji).
- **Sensory**: Mechanizmy do zbierania informacji (np. odczyt API).
- **Aktuatory**: Mechanizmy do wykonywania działań (np. wysyłanie e-maila).
- **Mózg (LLM)**: Silnik rozumujący, który planuje i decyduje, jakie działania podjąć.

## 2. Ramy agentowe

Kurs używa **Microsoft Agent Framework (MAF)** wraz z **Azure AI Foundry Agent Service V2** do budowy agentów:

| Component | Focus | Best For |
|-----------|-------|----------|
| **Microsoft Agent Framework** | Zunifikowane SDK Python/C# dla agentów, narzędzi i przepływów pracy | Budowanie agentów z narzędziami, przepływów wieloagentowych i wzorców produkcyjnych. |
| **Azure AI Foundry Agent Service** | Zarządzalne środowisko uruchomieniowe w chmurze | Bezpieczne, skalowalne wdrożenie z wbudowanym zarządzaniem stanem, obserwowalnością i zaufaniem. |

## 3. Wzorce projektowe agentów

Wzorce projektowe pomagają ustrukturyzować sposób działania agentów, aby rozwiązywały problemy niezawodnie.

### **Wzorzec użycia narzędzi** (Lekcja 4)
Ten wzorzec umożliwia agentom interakcję ze światem zewnętrznym.
- **Koncepcja**: Agent otrzymuje "schemat" (listę dostępnych funkcji i ich parametrów). LLM decyduje *które* narzędzie wywołać i z *jakimi* argumentami na podstawie żądania użytkownika.
- **Przepływ**: Żądanie użytkownika -> LLM -> **Wybór narzędzia** -> **Wykonanie narzędzia** -> LLM (z wynikiem narzędzia) -> Ostateczna odpowiedź.
- **Przypadki użycia**: Pobieranie danych w czasie rzeczywistym (pogoda, ceny akcji), wykonywanie obliczeń, uruchamianie kodu.

### **Wzorzec planowania** (Lekcja 7)
Ten wzorzec umożliwia agentom rozwiązywanie złożonych, wieloetapowych zadań.
- **Koncepcja**: Agent rozbija cel wysokiego poziomu na sekwencję mniejszych podzadań.
- **Podejścia**:
  - **Decompozycja zadań**: Podział "Zaplanuj podróż" na "Zarezerwuj lot", "Zarezerwuj hotel", "Wypożycz samochód".
  - **Planowanie iteracyjne**: Ponowne ocenianie planu na podstawie wyników poprzednich kroków (np. jeśli lot jest pełny, wybierz inną datę).
- **Wdrożenie**: Często obejmuje agenta "Planner", który generuje ustrukturyzowany plan (np. JSON), który następnie jest wykonywany przez innych agentów.

## 4. Zasady projektowania

Projektując agentów, rozważ trzy wymiary:
- **Przestrzeń**: Agenci powinni łączyć ludzi i wiedzę, być dostępni, ale nienachalni.
- **Czas**: Agenci powinni uczyć się z *Przeszłości*, dostarczać trafne sugestie w *Teraz*, i dostosowywać się na *Przyszłość*.
- **Rdzeń**: Akceptuj niepewność, ale buduj zaufanie poprzez przejrzystość i kontrolę użytkownika.

## 5. Podsumowanie kluczowych lekcji

- **Lekcja 1**: Agenci to systemy, nie tylko modele. Postrzegają, rozumują i działają.
- **Lekcja 2**: Microsoft Agent Framework upraszcza złożoność wywoływania narzędzi i zarządzania stanem.
- **Lekcja 3**: Projektuj mając na uwadze przejrzystość i kontrolę użytkownika.
- **Lekcja 4**: Narzędzia są „rękami” agenta. Definicja schematu jest kluczowa, aby LLM zrozumiał, jak ich używać.
- **Lekcja 7**: Planowanie to „funkcja wykonawcza” agenta, umożliwiająca mu radzenie sobie ze złożonymi przepływami pracy.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Zastrzeżenie:
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczeń AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dążymy do jak największej dokładności, prosimy pamiętać, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy uznać za źródło wiążące. W przypadku informacji o krytycznym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->