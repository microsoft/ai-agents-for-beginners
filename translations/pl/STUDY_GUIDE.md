# Agenci AI dla początkujących - Przewodnik i streszczenie kursu

Ten przewodnik przedstawia streszczenie kursu "AI Agents for Beginners" i wyjaśnia kluczowe koncepcje, ramy i wzorce projektowe do budowania agentów AI.

## 1. Wprowadzenie do agentów AI

**Czym są agenci AI?**
Agenci AI to systemy, które rozszerzają możliwości Dużych modeli językowych (LLMs) poprzez zapewnienie im dostępu do **narzędzi**, **wiedzy** i **pamięci**. W przeciwieństwie do standardowego chatbota opartego na LLM, który jedynie generuje tekst na podstawie danych treningowych, agent AI może:
- **Postrzegać** swoje otoczenie (za pomocą czujników lub danych wejściowych).
- **Rozumować** o tym, jak rozwiązać problem.
- **Działać**, aby zmienić środowisko (poprzez aktuatory lub wykonywanie narzędzi).

**Kluczowe komponenty agenta:**
- **Środowisko**: Przestrzeń, w której agent działa (np. system rezerwacji).
- **Czujniki**: Mechanizmy zbierania informacji (np. odczyt API).
- **Aktuatory**: Mechanizmy wykonywania akcji (np. wysyłanie e-maila).
- **Mózg (LLM)**: Silnik rozumowania, który planuje i decyduje, jakie działania podjąć.

## 2. Ramy dla agentów

Kurs używa **Microsoft Agent Framework (MAF)** wraz z **Azure AI Foundry Agent Service V2** do budowania agentów:

| Komponent | Zakres | Najlepsze dla |
|-----------|-------|----------|
| **Microsoft Agent Framework** | Zunifikowane SDK Python/C# dla agentów, narzędzi i przepływów pracy | Budowania agentów z narzędziami, przepływami wieloagentowymi i wzorcami produkcyjnymi. |
| **Azure AI Foundry Agent Service** | Zarządzalne środowisko uruchomieniowe w chmurze | Bezpieczne, skalowalne wdrożenie z wbudowanym zarządzaniem stanem, obserwowalnością i zaufaniem. |

## 3. Wzorce projektowe agentów

Wzorce projektowe pomagają uporządkować sposób działania agentów, aby rozwiązywały problemy w sposób niezawodny.

### **Wzorzec użycia narzędzi** (Lekcja 4)
Ten wzorzec umożliwia agentom interakcję ze światem zewnętrznym.
- **Koncepcja**: Agent otrzymuje "schemat" (listę dostępnych funkcji i ich parametrów). LLM decyduje, *które* narzędzie wywołać i z *jakimi* argumentami na podstawie żądania użytkownika.
- **Przepływ**: User Request -> LLM -> **Tool Selection** -> **Tool Execution** -> LLM (with tool output) -> Final Response.
- **Przypadki użycia**: Pobieranie danych w czasie rzeczywistym (pogoda, ceny akcji), wykonywanie obliczeń, uruchamianie kodu.

### **Wzorzec planowania** (Lekcja 7)
Ten wzorzec umożliwia agentom rozwiązywanie złożonych, wieloetapowych zadań.
- **Koncepcja**: Agent dzieli cel wysokiego poziomu na sekwencję mniejszych podzadań.
- **Podejścia**:
  - **Podział zadania**: Podzielenie "Plan a trip" na "Book flight", "Book hotel", "Rent car".
  - **Planowanie iteracyjne**: Ponowna ocena planu na podstawie wyników poprzednich kroków (np. jeśli lot jest pełny, wybierz inną datę).
- **Implementacja**: Często obejmuje agenta "Planner", który generuje ustrukturyzowany plan (np. JSON), który następnie jest wykonywany przez innych agentów.

## 4. Zasady projektowania

Projektując agentów, należy wziąć pod uwagę trzy wymiary:
- **Przestrzeń**: Agenci powinni łączyć ludzi i wiedzę, być dostępni, ale nienachalni.
- **Czas**: Agenci powinni uczyć się z *Przeszłość*, dostarczać istotnych wskazówek w *Teraz*, i przystosowywać się na *Przyszłość*.
- **Rdzeń**: Akceptuj niepewność, ale buduj zaufanie poprzez przejrzystość i kontrolę użytkownika.

## 5. Streszczenie kluczowych lekcji

- **Lekcja 1**: Agenci to systemy, nie tylko modele. Postrzegają, rozumują i działają.
- **Lekcja 2**: Microsoft Agent Framework abstrakcjonuje złożoność wywoływania narzędzi i zarządzania stanem.
- **Lekcja 3**: Projektuj mając na uwadze przejrzystość i kontrolę użytkownika.
- **Lekcja 4**: Narzędzia są "rękami" agenta. Definicja schematu jest kluczowa, aby LLM zrozumiało, jak ich używać.
- **Lekcja 7**: Planowanie jest "funkcją wykonawczą" agenta, umożliwiającą mu radzenie sobie ze złożonymi przepływami pracy.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Zastrzeżenie:
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia opartej na sztucznej inteligencji Co-op Translator (https://github.com/Azure/co-op-translator). Chociaż dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy uznać za wersję wiążącą. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za żadne nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->