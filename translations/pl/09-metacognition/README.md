[![Projekt Multi-Agent](../../../translated_images/pl/lesson-9-thumbnail.38059e8af1a5b71d.webp)](https://youtu.be/His9R6gw6Ec?si=3_RMb8VprNvdLRhX)

> _(Kliknij powyższy obraz, aby obejrzeć wideo z tej lekcji)_
# Metapoznanie w agentach AI

## Wprowadzenie

Witamy na lekcji o metapoznaniu w agentach AI! Ten rozdział jest przeznaczony dla początkujących, którzy są ciekawi, jak agenci AI mogą myśleć o własnych procesach myślowych. Po zakończeniu tej lekcji zrozumiesz kluczowe pojęcia i będziesz wyposażony w praktyczne przykłady stosowania metapoznania w projektowaniu agentów AI.

## Cele nauki

Po ukończeniu tej lekcji będziesz potrafił:

1. Zrozumieć implikacje pętli rozumowania w definicjach agentów.
2. Wykorzystać techniki planowania i ewaluacji do pomocy agentom samokorygującym się.
3. Tworzyć własnych agentów zdolnych do manipulowania kodem w celu realizacji zadań.

## Wprowadzenie do metapoznania

Metapoznanie odnosi się do wyższych procesów poznawczych, które obejmują myślenie o własnym myśleniu. Dla agentów AI oznacza to zdolność do oceny i dostosowywania swoich działań na podstawie samoświadomości i doświadczeń z przeszłości. Metapoznanie, czyli „myślenie o myśleniu”, jest ważnym pojęciem w rozwoju systemów AI o cechach agentowych. Polega na tym, że systemy AI są świadome własnych procesów wewnętrznych i potrafią monitorować, regulować oraz adaptować swoje zachowanie odpowiednio. Podobnie jak my, gdy czytamy sytuację lub rozpatrujemy problem. Ta samoświadomość może pomóc systemom AI podejmować lepsze decyzje, identyfikować błędy i z czasem poprawiać wydajność – co znowu odnosi się do testu Turinga i debaty o tym, czy AI przejmie kontrolę.

W kontekście systemów AI o cechach agentowych, metapoznanie może pomóc rozwiązać kilka wyzwań, takich jak:
- Przejrzystość: Zapewnienie, że systemy AI potrafią wyjaśnić swoje rozumowanie i decyzje.
- Rozumowanie: Zwiększenie zdolności systemów AI do syntezowania informacji i podejmowania właściwych decyzji.
- Adaptacja: Pozwolenie systemom AI na dostosowywanie się do nowych środowisk i zmieniających się warunków.
- Percepcja: Poprawa dokładności systemów AI w rozpoznawaniu i interpretacji danych ze środowiska.

### Czym jest metapoznanie?

Metapoznanie, czyli „myślenie o myśleniu”, to wyższy proces poznawczy, który obejmuje samoświadomość i samoregulację własnych procesów poznawczych. W dziedzinie AI metapoznanie umożliwia agentom ocenę i adaptację swoich strategii oraz działań, prowadząc do poprawy zdolności rozwiązywania problemów i podejmowania decyzji. Rozumiejąc metapoznanie, możesz projektować agentów AI, którzy będą nie tylko bardziej inteligentni, ale też bardziej elastyczni i efektywni. W prawdziwym metapoznaniu AI wprost rozważa własne rozumowanie.

Przykład: „Priorytetowałem tańsze loty, ponieważ… Mogę przegapiać loty bezpośrednie, więc sprawdzę to jeszcze raz.”.
Śledzi, jak i dlaczego wybrał określoną trasę.
- Zauważając, że popełnił błędy, ponieważ zbytnio polegał na preferencjach użytkownika z ostatniego razu, więc modyfikuje swoją strategię podejmowania decyzji, a nie tylko ostateczną rekomendację.
- Diagnozuje wzorce, takie jak: „Za każdym razem, gdy widzę, że użytkownik wspomina ‚za tłoczno’, nie tylko powinienem usuwać niektóre atrakcje, ale również przemyśleć, że moja metoda wyboru ‚top atrakcji’ jest wadliwa, jeśli zawsze oceniam je według popularności.”

### Znaczenie metapoznania w agentach AI

Metapoznanie odgrywa kluczową rolę w projektowaniu agentów AI z kilku powodów:

![Znaczenie metapoznania](../../../translated_images/pl/importance-of-metacognition.b381afe9aae352f7.webp)

- Samorefleksja: Agenci mogą oceniać swoje własne wyniki i wskazywać obszary do poprawy.
- Zdolność adaptacji: Agenci mogą modyfikować swoje strategie na podstawie wcześniejszych doświadczeń i zmieniających się środowisk.
- Korekta błędów: Agenci mogą autonomicznie wykrywać i poprawiać błędy, prowadząc do dokładniejszych wyników.
- Zarządzanie zasobami: Agenci mogą optymalizować wykorzystanie zasobów, takich jak czas i moc obliczeniowa, planując i oceniając swoje działania.

## Składniki agenta AI

Przed zagłębieniem się w procesy metapoznawcze, ważne jest zrozumienie podstawowych składników agenta AI. Agent AI zazwyczaj składa się z:

- Persony: Osobowości i cech agenta, które definiują, jak komunikuje się z użytkownikami.
- Narzędzi: Zdolności i funkcji, które agent potrafi wykonywać.
- Umiejętności: Wiedzy i eksperckiej wiedzy, które agent posiada.

Te składniki współpracują ze sobą, tworząc „jednostkę ekspertyzy”, która potrafi realizować określone zadania.

**Przykład**:
Weźmy pod uwagę agenta turystycznego, usługę agenta, która nie tylko planuje Twoje wakacje, ale również dostosowuje drogę na podstawie danych w czasie rzeczywistym i wcześniejszych doświadczeń klientów.

### Przykład: Metapoznanie w usłudze agenta turystycznego

Wyobraź sobie, że projektujesz usługę agenta turystycznego zasilanego AI. Ten agent, „Agent Turystyczny”, pomaga użytkownikom planować wakacje. Aby włączyć metapoznanie, Agent Turystyczny musi oceniać i dostosowywać swoje działania na podstawie samoświadomości i doświadczeń z przeszłości. Oto jak metapoznanie może odgrywać rolę:

#### Aktualne zadanie

Aktualnym zadaniem jest pomoc użytkownikowi w zaplanowaniu podróży do Paryża.

#### Kroki do wykonania zadania

1. **Zbierz preferencje użytkownika**: Zapytaj użytkownika o daty podróży, budżet, zainteresowania (np. muzea, kuchnia, zakupy) i ewentualne szczególne wymagania.
2. **Pozyskaj informacje**: Wyszukaj opcje lotów, zakwaterowania, atrakcji i restauracji odpowiadające preferencjom użytkownika.
3. **Wygeneruj rekomendacje**: Zapewnij spersonalizowany plan podróży z szczegółami lotów, rezerwacjami hotelów i proponowanymi aktywnościami.
4. **Dostosuj na podstawie opinii**: Zapytaj użytkownika o opinię na temat rekomendacji i wprowadź niezbędne poprawki.

#### Wymagane zasoby

- Dostęp do baz danych lotów i rezerwacji hoteli.
- Informacje o atrakcjach i restauracjach w Paryżu.
- Dane z opinii użytkowników z poprzednich interakcji.

#### Doświadczenie i samorefleksja

Agent Turystyczny używa metapoznania do oceny własnej wydajności i uczenia się na podstawie doświadczeń z przeszłości. Na przykład:

1. **Analiza opinii użytkowników**: Agent Turystyczny przegląda opinie użytkowników, aby określić, które rekomendacje zostały dobrze przyjęte, a które nie. Dostosowuje wtedy swoje przyszłe sugestie.
2. **Elastyczność**: Jeżeli użytkownik wcześniej wyraził niechęć do zatłoczonych miejsc, Agent Turystyczny w przyszłości nie będzie proponować popularnych miejsc turystycznych w godzinach szczytu.
3. **Korekta błędów**: Jeśli Agent Turystyczny popełnił błąd podczas wcześniejszej rezerwacji, np. zaproponował hotel, który był w pełni zarezerwowany, uczy się dokładniej sprawdzać dostępność przed rekomendacją.

#### Praktyczny przykład dla programisty

Oto uproszczony przykład kodu Travel Agent z wdrożonym metapoznaniem:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        # Wyszukaj loty, hotele i atrakcje na podstawie preferencji
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        # Analizuj opinie i dostosuj przyszłe rekomendacje
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Przykład użycia
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
```

#### Dlaczego metapoznanie ma znaczenie

- **Samorefleksja**: Agenci mogą analizować swoją wydajność i wskazywać obszary do poprawy.
- **Elastyczność**: Agenci mogą modyfikować strategie na podstawie opinii i zmieniających się warunków.
- **Korekta błędów**: Agenci mogą autonomicznie wykrywać i poprawiać błędy.
- **Zarządzanie zasobami**: Agenci mogą optymalizować wykorzystanie zasobów, takich jak czas i moc obliczeniowa.

Dzięki zastosowaniu metapoznania Agent Turystyczny może zapewniać bardziej spersonalizowane i dokładne rekomendacje podróżnicze, poprawiając ogólne doświadczenia użytkownika.

---

## 2. Planowanie w agentach

Planowanie jest kluczowym elementem zachowania agenta AI. Polega na określeniu kroków potrzebnych do osiągnięcia celu, uwzględniając aktualny stan, zasoby oraz możliwe przeszkody.

### Elementy planowania

- **Aktualne zadanie**: Jasno określ zadanie.
- **Kroki do wykonania zadania**: Podziel zadanie na zarządzalne kroki.
- **Wymagane zasoby**: Zidentyfikuj potrzebne zasoby.
- **Doświadczenie**: Wykorzystaj wcześniejsze doświadczenia do informowania planu.

**Przykład**:
Oto kroki, które Agent Turystyczny musi podjąć, aby skutecznie pomóc użytkownikowi w planowaniu podróży:

### Kroki dla Agenta Turystycznego

1. **Zbierz preferencje użytkownika**
   - Zapytaj użytkownika o szczegóły dotyczące dat podróży, budżetu, zainteresowań i ewentualnych szczególnych wymagań.
   - Przykłady: „Kiedy planujesz podróż?”, „Jaki jest Twój budżet?”, „Jakie aktywności lubisz na wakacjach?”

2. **Pozyskaj informacje**
   - Wyszukaj odpowiednie opcje podróży na podstawie preferencji użytkownika.
   - **Loty**: Znajdź dostępne loty mieszczące się w budżecie i preferowanych datach.
   - **Zakwaterowanie**: Znajdź hotele lub nieruchomości do wynajęcia zgodne z preferencjami użytkownika dotyczącymi lokalizacji, ceny i udogodnień.
   - **Atrakcje i restauracje**: Zidentyfikuj popularne atrakcje, aktywności i miejsca gastronomiczne odpowiadające zainteresowaniom użytkownika.

3. **Wygeneruj rekomendacje**
   - Skompiluj pozyskane informacje w spersonalizowany plan podróży.
   - Podaj szczegóły, takie jak opcje lotów, rezerwacje hoteli i proponowane aktywności, dopasowując rekomendacje do preferencji użytkownika.

4. **Przedstaw plan użytkownikowi**
   - Podziel się proponowanym planem podróży z użytkownikiem do oceny.
   - Przykład: „Oto proponowany plan Twojej podróży do Paryża. Zawiera szczegóły lotów, rezerwacje hoteli oraz listę rekomendowanych aktywności i restauracji. Daj znać, co o tym myślisz!”

5. **Zbierz feedback**
   - Zapytaj użytkownika o opinię na temat proponowanego planu.
   - Przykłady: „Czy podobają Ci się opcje lotów?”, „Czy hotel spełnia Twoje potrzeby?”, „Czy chcesz coś dodać lub usunąć z planu?”

6. **Dostosuj na podstawie opinii**
   - Zmodyfikuj plan na podstawie opinii użytkownika.
   - Dokonaj niezbędnych zmian w rekomendacjach dotyczących lotów, zakwaterowania i aktywności, aby lepiej odpowiadały preferencjom użytkownika.

7. **Ostateczne potwierdzenie**
   - Przedstaw zaktualizowany plan użytkownikowi do ostatecznego zatwierdzenia.
   - Przykład: „Wprowadziłem zmiany na podstawie Twojej opinii. Oto zaktualizowany plan. Wszystko się zgadza?”

8. **Rezerwuj i potwierdź**
   - Po zatwierdzeniu planu przez użytkownika dokonaj rezerwacji lotów, noclegów i zaplanowanych aktywności.
   - Wyślij użytkownikowi szczegóły potwierdzenia.

9. **Zapewnij ciągłe wsparcie**
   - Pozostań do dyspozycji, aby pomóc użytkownikowi przy zmianach lub dodatkowych potrzebach przed i w trakcie podróży.
   - Przykład: „Jeśli potrzebujesz dalszej pomocy podczas podróży, śmiało kontaktuj się ze mną w każdej chwili!”

### Przykładowa interakcja

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)

# Przykładowe użycie w ramach żądania rezerwacji
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
travel_agent.adjust_based_on_feedback(feedback)
```

## 3. Korekcyjny system RAG

Na początek zrozummy różnicę między narzędziem RAG a wcześniejszym ładowaniem kontekstu.

![RAG vs ładowanie kontekstu](../../../translated_images/pl/rag-vs-context.9eae588520c00921.webp)

### Generowanie wspomagane wyszukiwaniem (RAG)

RAG łączy system wyszukiwania z modelem generatywnym. Gdy następuje zapytanie, system wyszukiwania pobiera relewantne dokumenty lub dane z zewnętrznego źródła, a uzyskane informacje są używane do wzbogacenia wejścia modelu generatywnego. Pomaga to modelowi generować dokładniejsze i kontekstowo odpowiednie odpowiedzi.

W systemie RAG agent pobiera relewantne informacje z bazy wiedzy i wykorzystuje je do generowania odpowiednich odpowiedzi lub działań.

### Podejście korekcyjne RAG

Podejście korekcyjne RAG skupia się na wykorzystaniu technik RAG do korekty błędów i poprawy dokładności agentów AI. Obejmuje ono:

1. **Technikę promptowania**: Używanie konkretnych poleceń, aby kierować agentem w pobieraniu relewantnych informacji.
2. **Narzędzie**: Implementację algorytmów i mechanizmów umożliwiających agentowi ocenę relewantności pobranych informacji i generowanie dokładnych odpowiedzi.
3. **Ewaluację**: Ciągłą ocenę wydajności agenta i wprowadzanie korekt w celu poprawy dokładności i efektywności.

#### Przykład: Korekcyjne RAG w agencie wyszukiwania

Weźmy pod uwagę agenta wyszukiwania, który pobiera informacje z sieci, aby odpowiadać na pytania użytkownika. Podejście korekcyjne RAG może obejmować:

1. **Technikę promptowania**: Formułowanie zapytań wyszukiwawczych na podstawie wejścia użytkownika.
2. **Narzędzie**: Korzystanie z przetwarzania języka naturalnego i algorytmów uczenia maszynowego do rankingowania i filtrowania wyników wyszukiwania.
3. **Ewaluację**: Analizowanie opinii użytkowników w celu identyfikacji i korekty nieścisłości w pobranych informacjach.

### Korekcyjne RAG w Agencie Turystycznym

Korekcyjne RAG (Generowanie Wspomagane Wyszukiwaniem) zwiększa zdolność AI do pobierania i generowania informacji, jednocześnie korygując ewentualne nieścisłości. Zobaczmy, jak Agent Turystyczny może wykorzystać podejście korekcyjne RAG, aby zapewnić dokładniejsze i bardziej relewantne rekomendacje podróżnicze.

Obejmuje to:

- **Technikę promptowania:** Używanie konkretnych poleceń do kierowania agentem w pobieraniu relewantnych informacji.
- **Narzędzie:** Implementację algorytmów i mechanizmów pozwalających agentowi ocenić relewantność pobranych informacji i generować dokładne odpowiedzi.
- **Ewaluację:** Ciągłe ocenianie wydajności agenta i wprowadzanie korekt, by poprawić jego dokładność i efektywność.

#### Kroki wdrożenia korekcyjnego RAG w Agencie Turystycznym

1. **Początkowa interakcja z użytkownikiem**
   - Agent Turystyczny zbiera wstępne preferencje użytkownika, takie jak cel podróży, daty, budżet i zainteresowania.
   - Przykład:

     ```python
     preferences = {
         "destination": "Paris",
         "dates": "2025-04-01 to 2025-04-10",
         "budget": "moderate",
         "interests": ["museums", "cuisine"]
     }
     ```

2. **Pozyskiwanie informacji**
   - Agent Turystyczny pobiera informacje o lotach, zakwaterowaniu, atrakcjach i restauracjach zgodne z preferencjami użytkownika.
   - Przykład:

     ```python
     flights = search_flights(preferences)
     hotels = search_hotels(preferences)
     attractions = search_attractions(preferences)
     ```

3. **Generowanie wstępnych rekomendacji**
   - Agent Turystyczny wykorzystuje pobrane informacje do przygotowania spersonalizowanego planu podróży.
   - Przykład:

     ```python
     itinerary = create_itinerary(flights, hotels, attractions)
     print("Suggested Itinerary:", itinerary)
     ```

4. **Zbieranie opinii użytkownika**
   - Agent Turystyczny prosi użytkownika o opinię na temat wstępnych rekomendacji.
   - Przykład:

     ```python
     feedback = {
         "liked": ["Louvre Museum"],
         "disliked": ["Eiffel Tower (too crowded)"]
     }
     ```

5. **Proces korekcyjny RAG**
   - **Technika promptowania**: Agent Turystyczny formułuje nowe zapytania wyszukiwawcze na podstawie opinii użytkownika.
     - Przykład:

       ```python
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       ```

   - **Narzędzie**: Agent Turystyczny używa algorytmów do rankingowania i filtrowania nowych wyników wyszukiwania, podkreślając relewantność na podstawie opinii użytkownika.
     - Przykład:

       ```python
       new_attractions = search_attractions(preferences)
       new_itinerary = create_itinerary(flights, hotels, new_attractions)
       print("Updated Itinerary:", new_itinerary)
       ```

   - **Ewaluacja**: Agent Turystyczny ciągle ocenia relewantność i dokładność swoich rekomendacji, analizując opinie użytkownika i wprowadzając potrzebne poprawki.
     - Przykład:

       ```python
       def adjust_preferences(preferences, feedback):
           if "liked" in feedback:
               preferences["favorites"] = feedback["liked"]
           if "disliked" in feedback:
               preferences["avoid"] = feedback["disliked"]
           return preferences

       preferences = adjust_preferences(preferences, feedback)
       ```

#### Praktyczny przykład

Oto uproszczony przykład kodu w Pythonie zawierający podejście korekcyjne RAG w Agencie Turystycznym:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        itinerary = create_itinerary(flights, hotels, attractions)
        return itinerary

    def adjust_based_on_feedback(self, feedback):
        self.experience_data.append(feedback)
        self.user_preferences = adjust_preferences(self.user_preferences, feedback)
        new_itinerary = self.generate_recommendations()
        return new_itinerary

# Przykładowe użycie
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
new_itinerary = travel_agent.adjust_based_on_feedback(feedback)
print("Updated Itinerary:", new_itinerary)
```

### Wczesne ładowanie kontekstu


Wstępne ładowanie kontekstu polega na wczytywaniu istotnego kontekstu lub informacji tła do modelu przed przetworzeniem zapytania. Oznacza to, że model ma dostęp do tych informacji od samego początku, co może pomóc mu generować bardziej świadome odpowiedzi bez konieczności pobierania dodatkowych danych w trakcie procesu.

Oto uproszczony przykład, jak może wyglądać wstępne ładowanie kontekstu w aplikacji dla agenta podróży w Pythonie:

```python
class TravelAgent:
    def __init__(self):
        # Wczytaj wcześniej popularne destynacje i ich informacje
        self.context = {
            "Paris": {"country": "France", "currency": "Euro", "language": "French", "attractions": ["Eiffel Tower", "Louvre Museum"]},
            "Tokyo": {"country": "Japan", "currency": "Yen", "language": "Japanese", "attractions": ["Tokyo Tower", "Shibuya Crossing"]},
            "New York": {"country": "USA", "currency": "Dollar", "language": "English", "attractions": ["Statue of Liberty", "Times Square"]},
            "Sydney": {"country": "Australia", "currency": "Dollar", "language": "English", "attractions": ["Sydney Opera House", "Bondi Beach"]}
        }

    def get_destination_info(self, destination):
        # Pobierz informacje o destynacji z wcześniej załadowanego kontekstu
        info = self.context.get(destination)
        if info:
            return f"{destination}:\nCountry: {info['country']}\nCurrency: {info['currency']}\nLanguage: {info['language']}\nAttractions: {', '.join(info['attractions'])}"
        else:
            return f"Sorry, we don't have information on {destination}."

# Przykład użycia
travel_agent = TravelAgent()
print(travel_agent.get_destination_info("Paris"))
print(travel_agent.get_destination_info("Tokyo"))
```

#### Wyjaśnienie

1. **Inicjalizacja (metoda `__init__`)**: Klasa `TravelAgent` wstępnie ładuje słownik zawierający informacje o popularnych miejscach docelowych, takich jak Paryż, Tokio, Nowy Jork i Sydney. Słownik ten zawiera szczegóły takie jak kraj, waluta, język oraz główne atrakcje dla każdego miejsca.

2. **Pobieranie informacji (metoda `get_destination_info`)**: Gdy użytkownik pyta o konkretne miejsce docelowe, metoda `get_destination_info` pobiera odpowiednie informacje ze wstępnie załadowanego słownika kontekstu.

Dzięki wstępnemu ładowaniu kontekstu aplikacja agenta podróży może szybko odpowiadać na zapytania użytkowników bez konieczności pobierania tych informacji z zewnętrznego źródła w czasie rzeczywistym. Sprawia to, że aplikacja jest bardziej wydajna i responsywna.

### Bootstrapping planu z celem przed iteracją

Bootstrapping planu z celem polega na rozpoczęciu od jasnego celu lub oczekiwanego wyniku. Poprzez określenie tego celu z góry, model może używać go jako zasady przewodniej podczas całego procesu iteracyjnego. Pomaga to zapewnić, że każda iteracja przybliża do osiągnięcia pożądanego rezultatu, czyniąc proces bardziej efektywnym i skupionym.

Oto przykład, jak można bootstrappować plan podróży z celem przed iteracją dla agenta podróży w Pythonie:

### Scenariusz

Agent podróży chce zaplanować spersonalizowane wakacje dla klienta. Celem jest stworzenie planu podróży maksymalizującego satysfakcję klienta na podstawie jego preferencji i budżetu.

### Kroki

1. Określenie preferencji i budżetu klienta.
2. Bootstrapping początkowego planu na podstawie tych preferencji.
3. Iterowanie w celu ulepszenia planu, optymalizując go pod kątem satysfakcji klienta.

#### Kod w Pythonie

```python
class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def bootstrap_plan(self, preferences, budget):
        plan = []
        total_cost = 0

        for destination in self.destinations:
            if total_cost + destination['cost'] <= budget and self.match_preferences(destination, preferences):
                plan.append(destination)
                total_cost += destination['cost']

        return plan

    def match_preferences(self, destination, preferences):
        for key, value in preferences.items():
            if destination.get(key) != value:
                return False
        return True

    def iterate_plan(self, plan, preferences, budget):
        for i in range(len(plan)):
            for destination in self.destinations:
                if destination not in plan and self.match_preferences(destination, preferences) and self.calculate_cost(plan, destination) <= budget:
                    plan[i] = destination
                    break
        return plan

    def calculate_cost(self, plan, new_destination):
        return sum(destination['cost'] for destination in plan) + new_destination['cost']

# Przykładowe użycie
destinations = [
    {"name": "Paris", "cost": 1000, "activity": "sightseeing"},
    {"name": "Tokyo", "cost": 1200, "activity": "shopping"},
    {"name": "New York", "cost": 900, "activity": "sightseeing"},
    {"name": "Sydney", "cost": 1100, "activity": "beach"},
]

preferences = {"activity": "sightseeing"}
budget = 2000

travel_agent = TravelAgent(destinations)
initial_plan = travel_agent.bootstrap_plan(preferences, budget)
print("Initial Plan:", initial_plan)

refined_plan = travel_agent.iterate_plan(initial_plan, preferences, budget)
print("Refined Plan:", refined_plan)
```

#### Wyjaśnienie kodu

1. **Inicjalizacja (metoda `__init__`)**: Klasa `TravelAgent` jest inicjalizowana z listą potencjalnych miejsc docelowych, z których każde posiada atrybuty takie jak nazwa, koszt i typ aktywności.

2. **Bootstrapping planu (metoda `bootstrap_plan`)**: Ta metoda tworzy początkowy plan podróży na podstawie preferencji i budżetu klienta. Iteruje przez listę miejsc docelowych i dodaje je do planu, jeśli odpowiadają preferencjom klienta i mieszczą się w budżecie.

3. **Dopasowanie preferencji (metoda `match_preferences`)**: Ta metoda sprawdza, czy miejsce docelowe spełnia preferencje klienta.

4. **Iteracja planu (metoda `iterate_plan`)**: Ta metoda ulepsza początkowy plan, próbując zastąpić każde miejsce w planie lepszym dopasowaniem, uwzględniając preferencje klienta i ograniczenia budżetowe.

5. **Obliczanie kosztu (metoda `calculate_cost`)**: Ta metoda oblicza całkowity koszt obecnego planu, włączając potencjalne nowe miejsce docelowe.

#### Przykład użycia

- **Początkowy plan**: Agent tworzy początkowy plan na podstawie preferencji klienta dotyczących zwiedzania i budżetu wynoszącego 2000 dolarów.
- **Ulepszony plan**: Agent iteruje plan, optymalizując go pod kątem preferencji klienta i budżetu.

Dzięki bootstrappingowi planu z jasnym celem (np. maksymalizacja satysfakcji klienta) i iteracjom poprawiającym plan, agent podróży może stworzyć spersonalizowany i zoptymalizowany plan podróży dla klienta. Podejście to zapewnia, że plan jest zgodny z preferencjami i budżetem klienta od samego początku i ulepsza się z każdą iteracją.

### Wykorzystanie LLM do ponownego rankingu i oceniania

Duże modele językowe (LLM) mogą być wykorzystywane do ponownego rankingu i oceniania poprzez ocenę relewantności i jakości pobranych dokumentów lub wygenerowanych odpowiedzi. Oto jak to działa:

**Pobieranie:** Początkowy etap pobierania zwraca zestaw kandydatów dokumentów lub odpowiedzi na podstawie zapytania.

**Ponowny ranking:** LLM ocenia tych kandydatów i ponownie ustawia ich ranking na podstawie relewantności i jakości. Ten krok zapewnia, że najważniejsze i najwyższej jakości informacje są prezentowane jako pierwsze.

**Ocenianie:** LLM przypisuje oceny każdemu kandydatowi, odzwierciedlając ich relewantność i jakość. Pomaga to w wyborze najlepszej odpowiedzi lub dokumentu dla użytkownika.

Wykorzystując LLM do ponownego rankingu i oceniania, system może dostarczać dokładniejsze i kontekstowo odpowiednie informacje, poprawiając ogólne doświadczenie użytkownika.

Oto przykład, jak agent podróży może użyć dużego modelu językowego (LLM) do ponownego rankingu i oceniania miejsc docelowych podróży na podstawie preferencji użytkownika w Pythonie:

#### Scenariusz - Podróże na podstawie preferencji

Agent podróży chce polecić klientowi najlepsze miejsca podróży na podstawie jego preferencji. LLM pomoże ponownie uszeregować i ocenić miejsca, aby zapewnić najbardziej odpowiednie opcje.

#### Kroki:

1. Zbieranie preferencji użytkownika.
2. Pobranie listy potencjalnych miejsc podróży.
3. Użycie LLM do ponownego rankingu i oceniania miejsc na podstawie preferencji użytkownika.

Oto jak można zaktualizować poprzedni przykład, aby użyć usług Azure OpenAI:

#### Wymagania

1. Musisz mieć subskrypcję Azure.
2. Utwórz zasób Azure OpenAI i zdobądź swój klucz API.

#### Przykład kodu w Pythonie

```python
import requests
import json

class TravelAgent:
    def __init__(self, destinations):
        self.destinations = destinations

    def get_recommendations(self, preferences, api_key, endpoint):
        # Wygeneruj prompt dla Azure OpenAI
        prompt = self.generate_prompt(preferences)
        
        # Zdefiniuj nagłówki i treść żądania
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }
        payload = {
            "prompt": prompt,
            "max_tokens": 150,
            "temperature": 0.7
        }
        
        # Wywołaj API Azure OpenAI, aby otrzymać ponownie ocenione i ocenione miejsca docelowe
        response = requests.post(endpoint, headers=headers, json=payload)
        response_data = response.json()
        
        # Wyodrębnij i zwróć rekomendacje
        recommendations = response_data['choices'][0]['text'].strip().split('\n')
        return recommendations

    def generate_prompt(self, preferences):
        prompt = "Here are the travel destinations ranked and scored based on the following user preferences:\n"
        for key, value in preferences.items():
            prompt += f"{key}: {value}\n"
        prompt += "\nDestinations:\n"
        for destination in self.destinations:
            prompt += f"- {destination['name']}: {destination['description']}\n"
        return prompt

# Przykład użycia
destinations = [
    {"name": "Paris", "description": "City of lights, known for its art, fashion, and culture."},
    {"name": "Tokyo", "description": "Vibrant city, famous for its modernity and traditional temples."},
    {"name": "New York", "description": "The city that never sleeps, with iconic landmarks and diverse culture."},
    {"name": "Sydney", "description": "Beautiful harbour city, known for its opera house and stunning beaches."},
]

preferences = {"activity": "sightseeing", "culture": "diverse"}
api_key = 'your_azure_openai_api_key'
endpoint = 'https://your-endpoint.com/openai/deployments/your-deployment-name/completions?api-version=2022-12-01'

travel_agent = TravelAgent(destinations)
recommendations = travel_agent.get_recommendations(preferences, api_key, endpoint)
print("Recommended Destinations:")
for rec in recommendations:
    print(rec)
```

#### Wyjaśnienie kodu - Preference Booker

1. **Inicjalizacja**: Klasa `TravelAgent` jest inicjalizowana listą potencjalnych miejsc podróży, z których każde ma atrybuty takie jak nazwa i opis.

2. **Uzyskiwanie rekomendacji (metoda `get_recommendations`)**: Ta metoda generuje zapytanie do usługi Azure OpenAI na podstawie preferencji użytkownika i wykonuje żądanie HTTP POST do API Azure OpenAI, aby uzyskać ponownie uszeregowane i ocenione miejsca podróży.

3. **Generowanie zapytania (metoda `generate_prompt`)**: Metoda ta tworzy zapytanie dla Azure OpenAI, włączając preferencje użytkownika oraz listę miejsc. Zapytanie kieruje model, aby ponownie uszeregował i ocenił miejsca na podstawie dostarczonych preferencji.

4. **Wywołanie API**: Do wykonania żądania HTTP POST do punktu końcowego API Azure OpenAI używana jest biblioteka `requests`. Odpowiedź zawiera ponownie uszeregowane i ocenione miejsca.

5. **Przykład użycia**: Agent zbiera preferencje użytkownika (np. zainteresowanie zwiedzaniem i różnorodną kulturą) i korzysta z usługi Azure OpenAI, aby uzyskać ponownie uszeregowane i ocenione rekomendacje miejsc podróży.

Upewnij się, że zastąpiłeś `your_azure_openai_api_key` rzeczywistym kluczem API Azure OpenAI oraz `https://your-endpoint.com/...` rzeczywistym adresem URL punktu końcowego Twojego wdrożenia Azure OpenAI.

Dzięki wykorzystaniu LLM do ponownego rankingu i oceniania agent podróży może dostarczać bardziej spersonalizowane i odpowiednie rekomendacje podróży, poprawiając ogólne doświadczenie klientów.

### RAG: Technika promptowania vs narzędzie

Retrieval-Augmented Generation (RAG) może być zarówno techniką promptowania, jak i narzędziem w rozwoju agentów AI. Zrozumienie rozróżnienia między tymi dwoma może pomóc w efektywniejszym wykorzystaniu RAG w Twoich projektach.

#### RAG jako technika promptowania

**Co to jest?**

- Jako technika promptowania, RAG polega na formułowaniu konkretnych zapytań lub promptów, które kierują wyszukiwaniem odpowiednich informacji z dużego korpusu lub bazy danych. Te informacje są następnie używane do generowania odpowiedzi lub działań.

**Jak to działa:**

1. **Formułowanie promptów**: Tworzenie dobrze ustrukturyzowanych promptów lub zapytań na podstawie zadania lub danych wejściowych użytkownika.
2. **Pobieranie informacji**: Wykorzystanie promptów do wyszukiwania odpowiednich danych z istniejącej bazy wiedzy lub zbioru danych.
3. **Generowanie odpowiedzi**: Połączenie pobranych informacji z modelami generatywnymi AI w celu wytworzenia kompleksowej i spójnej odpowiedzi.

**Przykład zastosowania w agencie podróży**:

- Dane użytkownika: "Chcę odwiedzić muzea w Paryżu."
- Prompt: "Znajdź najlepsze muzea w Paryżu."
- Pobranie informacji: Szczegóły o Luwrze, Musée d'Orsay itp.
- Wygenerowana odpowiedź: "Oto najlepsze muzea w Paryżu: Luwr, Musée d'Orsay oraz Centre Pompidou."

#### RAG jako narzędzie

**Co to jest?**

- Jako narzędzie, RAG to zintegrowany system, który automatyzuje proces pobierania i generowania, ułatwiając deweloperom implementację złożonych funkcjonalności AI bez ręcznego tworzenia promptów dla każdego zapytania.

**Jak to działa:**

1. **Integracja**: Osadzenie RAG w architekturze agenta AI, pozwalając mu automatycznie obsługiwać zadania pobierania i generowania.
2. **Automatyzacja**: Narzędzie zarządza całym procesem, od otrzymania danych wejściowych od użytkownika do wygenerowania ostatecznej odpowiedzi, bez konieczności jawnych promptów dla każdego kroku.
3. **Efektywność**: Poprawia wydajność agenta, usprawniając proces pobierania i generowania, umożliwiając szybsze i dokładniejsze odpowiedzi.

**Przykład zastosowania w agencie podróży**:

- Dane użytkownika: "Chcę odwiedzić muzea w Paryżu."
- Narzędzie RAG: Automatycznie pobiera informacje o muzeach i generuje odpowiedź.
- Wygenerowana odpowiedź: "Oto najlepsze muzea w Paryżu: Luwr, Musée d'Orsay oraz Centre Pompidou."

### Porównanie

| Aspekt                 | Technika promptowania                                  | Narzędzie                                         |
|------------------------|--------------------------------------------------------|--------------------------------------------------|
| **Ręczne vs Automatyczne** | Ręczne formułowanie promptów dla każdego zapytania.   | Zautomatyzowany proces pobierania i generowania. |
| **Kontrola**            | Daje większą kontrolę nad procesem pobierania.         | Usprawnia i automatyzuje pobieranie i generowanie.|
| **Elastyczność**        | Pozwala na dostosowane prompty wg specyficznych potrzeb.| Bardziej efektywne dla dużych implementacji.     |
| **Złożoność**           | Wymaga tworzenia i dostosowywania promptów.             | Łatwiejsze do integracji w architekturze agenta AI.|

### Praktyczne przykłady

**Przykład techniki promptowania:**

```python
def search_museums_in_paris():
    prompt = "Find top museums in Paris"
    search_results = search_web(prompt)
    return search_results

museums = search_museums_in_paris()
print("Top Museums in Paris:", museums)
```

**Przykład narzędzia:**

```python
class Travel_Agent:
    def __init__(self):
        self.rag_tool = RAGTool()

    def get_museums_in_paris(self):
        user_input = "I want to visit museums in Paris."
        response = self.rag_tool.retrieve_and_generate(user_input)
        return response

travel_agent = Travel_Agent()
museums = travel_agent.get_museums_in_paris()
print("Top Museums in Paris:", museums)
```

### Ocena relewantności

Ocena relewantności to kluczowy aspekt wydajności agenta AI. Zapewnia, że informacje pobrane i wygenerowane przez agenta są odpowiednie, dokładne i użyteczne dla użytkownika. Przyjrzyjmy się, jak oceniać relewantność w agentach AI, z praktycznymi przykładami i technikami.

#### Kluczowe pojęcia w ocenie relewantności

1. **Świadomość kontekstu**:
   - Agent musi rozumieć kontekst zapytania użytkownika, aby pobrać i wygenerować odpowiednie informacje.
   - Przykład: Jeśli użytkownik pyta o "najlepsze restauracje w Paryżu", agent powinien uwzględnić preferencje takie jak rodzaj kuchni i budżet.

2. **Dokładność**:
   - Informacje dostarczane przez agenta powinny być faktograficznie poprawne i aktualne.
   - Przykład: Polecanie obecnie otwartych restauracji z dobrymi opiniami zamiast nieaktualnych lub zamkniętych opcji.

3. **Intencja użytkownika**:
   - Agent powinien rozumieć intencję stojącą za zapytaniem, aby dostarczyć najbardziej relewantne informacje.
   - Przykład: Jeśli użytkownik pyta o "hotele budżetowe", agent powinien priorytetowo traktować przystępne cenowo opcje.

4. **Pętla informacji zwrotnej**:
   - Ciągłe zbieranie i analizowanie opinii użytkowników pomaga agentowi ulepszać proces oceny relewantności.
   - Przykład: Włączenie ocen i opinii użytkowników dotyczących wcześniejszych rekomendacji w celu poprawy przyszłych odpowiedzi.

#### Praktyczne techniki oceny relewantności

1. **Ocena relewantności punktowa**:
   - Przypisanie każdemu pobranemu elementowi oceny relewantności na podstawie dopasowania do zapytania i preferencji użytkownika.
   - Przykład:

     ```python
     def relevance_score(item, query):
         score = 0
         if item['category'] in query['interests']:
             score += 1
         if item['price'] <= query['budget']:
             score += 1
         if item['location'] == query['destination']:
             score += 1
         return score
     ```

2. **Filtrowanie i ranking**:
   - Odfiltrowanie nieistotnych elementów i uszeregowanie pozostałych wg ocen relewantności.
   - Przykład:

     ```python
     def filter_and_rank(items, query):
         ranked_items = sorted(items, key=lambda item: relevance_score(item, query), reverse=True)
         return ranked_items[:10]  # Zwróć 10 najważniejszych elementów
     ```

3. **Przetwarzanie języka naturalnego (NLP)**:
   - Wykorzystanie technik NLP do zrozumienia zapytania użytkownika i pobrania relewantnych informacji.
   - Przykład:

     ```python
     def process_query(query):
         # Użyj NLP, aby wydobyć kluczowe informacje z zapytania użytkownika
         processed_query = nlp(query)
         return processed_query
     ```

4. **Integracja opinii użytkowników**:
   - Zbieranie opinii użytkowników na temat rekomendacji i używanie ich do korygowania przyszłych ocen relewantności.
   - Przykład:

     ```python
     def adjust_based_on_feedback(feedback, items):
         for item in items:
             if item['name'] in feedback['liked']:
                 item['relevance'] += 1
             if item['name'] in feedback['disliked']:
                 item['relevance'] -= 1
         return items
     ```

#### Przykład: Ocena relewantności w agencie podróży

Oto praktyczny przykład, jak agent podróży może ocenić relewantność rekomendacji podróży:

```python
class Travel_Agent:
    def __init__(self):
        self.user_preferences = {}
        self.experience_data = []

    def gather_preferences(self, preferences):
        self.user_preferences = preferences

    def retrieve_information(self):
        flights = search_flights(self.user_preferences)
        hotels = search_hotels(self.user_preferences)
        attractions = search_attractions(self.user_preferences)
        return flights, hotels, attractions

    def generate_recommendations(self):
        flights, hotels, attractions = self.retrieve_information()
        ranked_hotels = self.filter_and_rank(hotels, self.user_preferences)
        itinerary = create_itinerary(flights, ranked_hotels, attractions)
        return itinerary

    def filter_and_rank(self, items, query):
        ranked_items = sorted(items, key=lambda item: self.relevance_score(item, query), reverse=True)
        return ranked_items[:10]  # Zwróć 10 najbardziej istotnych elementów

    def relevance_score(self, item, query):
        score = 0
        if item['category'] in query['interests']:
            score += 1
        if item['price'] <= query['budget']:
            score += 1
        if item['location'] == query['destination']:
            score += 1
        return score

    def adjust_based_on_feedback(self, feedback, items):
        for item in items:
            if item['name'] in feedback['liked']:
                item['relevance'] += 1
            if item['name'] in feedback['disliked']:
                item['relevance'] -= 1
        return items

# Przykład użycia
travel_agent = Travel_Agent()
preferences = {
    "destination": "Paris",
    "dates": "2025-04-01 to 2025-04-10",
    "budget": "moderate",
    "interests": ["museums", "cuisine"]
}
travel_agent.gather_preferences(preferences)
itinerary = travel_agent.generate_recommendations()
print("Suggested Itinerary:", itinerary)
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_items = travel_agent.adjust_based_on_feedback(feedback, itinerary['hotels'])
print("Updated Itinerary with Feedback:", updated_items)
```

### Wyszukiwanie z intencją

Wyszukiwanie z intencją polega na rozumieniu i interpretacji podstawowego celu lub zamierzenia stojącego za zapytaniem użytkownika, aby pobrać i wygenerować najbardziej relewantne i użyteczne informacje. Podejście to wykracza poza prostą analizę słów kluczowych i skupia się na zrozumieniu faktycznych potrzeb i kontekstu użytkownika.

#### Kluczowe pojęcia w wyszukiwaniu z intencją

1. **Rozumienie intencji użytkownika**:
   - Intencję użytkownika można sklasyfikować na trzy główne typy: informacyjną, nawigacyjną i transakcyjną.
     - **Intencja informacyjna**: Użytkownik szuka informacji na dany temat (np. "Jakie są najlepsze muzea w Paryżu?").
     - **Intencja nawigacyjna**: Użytkownik chce przejść na konkretną stronę lub witrynę (np. "Oficjalna strona Muzeum Luwru").
     - **Intencja transakcyjna**: Użytkownik chce wykonać transakcję, np. zarezerwować lot lub dokonać zakupu (np. "Zarezerwuj lot do Paryża").

2. **Świadomość kontekstu**:
   - Analiza kontekstu zapytania użytkownika pomaga dokładnie określić jego intencję. Obejmuje to uwzględnienie wcześniejszych interakcji, preferencji użytkownika oraz szczegółów bieżącego zapytania.

3. **Przetwarzanie języka naturalnego (NLP)**:
   - Techniki NLP są wykorzystywane do rozumienia i interpretacji naturalnego języka zapytań użytkowników. Obejmuje to zadania takie jak rozpoznawanie jednostek, analiza sentimentu i parsowanie zapytań.

4. **Personalizacja**:
   - Personalizacja wyników wyszukiwania na podstawie historii, preferencji i opinii użytkownika zwiększa relewantność pozyskanych informacji.

#### Praktyczny przykład: Wyszukiwanie z intencją w agencie podróży

Przeanalizujmy agenta podróży jako przykład implementacji wyszukiwania z intencją.

1. **Zbieranie preferencji użytkownika**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Rozumienie intencji użytkownika**

   ```python
   def identify_intent(query):
       if "book" in query or "purchase" in query:
           return "transactional"
       elif "website" in query or "official" in query:
           return "navigational"
       else:
           return "informational"
   ```

3. **Świadomość kontekstu**


   ```python
   def analyze_context(query, user_history):
       # Połącz bieżące zapytanie z historią użytkownika, aby zrozumieć kontekst
       context = {
           "current_query": query,
           "user_history": user_history
       }
       return context
   ```

4. **Wyszukiwanie i personalizacja wyników**

   ```python
   def search_with_intent(query, preferences, user_history):
       intent = identify_intent(query)
       context = analyze_context(query, user_history)
       if intent == "informational":
           search_results = search_information(query, preferences)
       elif intent == "navigational":
           search_results = search_navigation(query)
       elif intent == "transactional":
           search_results = search_transaction(query, preferences)
       personalized_results = personalize_results(search_results, user_history)
       return personalized_results

   def search_information(query, preferences):
       # Przykładowa logika wyszukiwania dla intencji informacyjnej
       results = search_web(f"best {preferences['interests']} in {preferences['destination']}")
       return results

   def search_navigation(query):
       # Przykładowa logika wyszukiwania dla intencji nawigacyjnej
       results = search_web(query)
       return results

   def search_transaction(query, preferences):
       # Przykładowa logika wyszukiwania dla intencji transakcyjnej
       results = search_web(f"book {query} to {preferences['destination']}")
       return results

   def personalize_results(results, user_history):
       # Przykładowa logika personalizacji
       personalized = [result for result in results if result not in user_history]
       return personalized[:10]  # Zwróć 10 najlepszych spersonalizowanych wyników
   ```

5. **Przykładowe zastosowanie**

   ```python
   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   user_history = ["Louvre Museum website", "Book flight to Paris"]
   query = "best museums in Paris"
   results = search_with_intent(query, preferences, user_history)
   print("Search Results:", results)
   ```

---

## 4. Generowanie kodu jako narzędzie

Agenci generujący kod wykorzystują modele AI do pisania i wykonywania kodu, rozwiązując złożone problemy i automatyzując zadania.

### Agenci generujący kod

Agenci generujący kod wykorzystują generatywne modele AI do pisania i wykonywania kodu. Ci agenci mogą rozwiązywać złożone problemy, automatyzować zadania oraz dostarczać cenne informacje poprzez generowanie i uruchamianie kodu w różnych językach programowania.

#### Zastosowania praktyczne

1. **Automatyczne generowanie kodu**: Generowanie fragmentów kodu do konkretnych zadań, takich jak analiza danych, zbieranie danych z sieci lub uczenie maszynowe.
2. **SQL jako RAG**: Używanie zapytań SQL do pobierania i manipulowania danymi z baz danych.
3. **Rozwiązywanie problemów**: Tworzenie i wykonywanie kodu w celu rozwiązania konkretnych problemów, takich jak optymalizacja algorytmów lub analiza danych.

#### Przykład: Agent generujący kod do analizy danych

Załóżmy, że projektujesz agenta generującego kod. Oto jak mógłby działać:

1. **Zadanie**: Analiza zestawu danych w celu identyfikacji trendów i wzorców.
2. **Kroki**:
   - Załaduj zestaw danych do narzędzia analizy danych.
   - Wygeneruj zapytania SQL do filtrowania i agregowania danych.
   - Wykonaj zapytania i pobierz wyniki.
   - Wykorzystaj wyniki do generowania wizualizacji i wniosków.
3. **Wymagane zasoby**: Dostęp do zestawu danych, narzędzi analizy danych i możliwości SQL.
4. **Doświadczenie**: Wykorzystaj wyniki poprzednich analiz do poprawy dokładności i trafności przyszłych analiz.

### Przykład: Agent generujący kod dla agenta podróży

W tym przykładzie zaprojektujemy agenta generującego kod, Agenta Podróży, aby pomóc użytkownikom w planowaniu podróży poprzez generowanie i wykonywanie kodu. Agent może obsługiwać zadania takie jak pobieranie opcji podróży, filtrowanie wyników i tworzenie harmonogramu za pomocą generatywnej AI.

#### Przegląd agenta generującego kod

1. **Zbieranie preferencji użytkownika**: Zbiera dane wejściowe użytkownika, takie jak cel podróży, daty podróży, budżet i zainteresowania.
2. **Generowanie kodu do pobierania danych**: Generuje fragmenty kodu do pobierania danych o lotach, hotelach i atrakcjach.
3. **Wykonywanie wygenerowanego kodu**: Uruchamia wygenerowany kod, aby pobrać informacje w czasie rzeczywistym.
4. **Generowanie harmonogramu**: Kompiluje pobrane dane w spersonalizowany plan podróży.
5. **Dostosowywanie na podstawie opinii**: Otrzymuje opinie użytkownika i w razie potrzeby regeneruje kod, aby udoskonalić wyniki.

#### Implementacja krok po kroku

1. **Zbieranie preferencji użytkownika**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Generowanie kodu do pobierania danych**

   ```python
   def generate_code_to_fetch_data(preferences):
       # Przykład: Wygeneruj kod do wyszukiwania lotów na podstawie preferencji użytkownika
       code = f"""
       def search_flights():
           import requests
           response = requests.get('https://api.example.com/flights', params={preferences})
           return response.json()
       """
       return code

   def generate_code_to_fetch_hotels(preferences):
       # Przykład: Wygeneruj kod do wyszukiwania hoteli
       code = f"""
       def search_hotels():
           import requests
           response = requests.get('https://api.example.com/hotels', params={preferences})
           return response.json()
       """
       return code
   ```

3. **Wykonywanie wygenerowanego kodu**

   ```python
   def execute_code(code):
       # Wykonaj wygenerowany kod za pomocą exec
       exec(code)
       result = locals()
       return result

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   
   flight_code = generate_code_to_fetch_data(preferences)
   hotel_code = generate_code_to_fetch_hotels(preferences)
   
   flights = execute_code(flight_code)
   hotels = execute_code(hotel_code)

   print("Flight Options:", flights)
   print("Hotel Options:", hotels)
   ```

4. **Generowanie harmonogramu**

   ```python
   def generate_itinerary(flights, hotels, attractions):
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   attractions = search_attractions(preferences)
   itinerary = generate_itinerary(flights, hotels, attractions)
   print("Suggested Itinerary:", itinerary)
   ```

5. **Dostosowywanie na podstawie opinii**

   ```python
   def adjust_based_on_feedback(feedback, preferences):
       # Dostosuj preferencje na podstawie opinii użytkownika
       if "liked" in feedback:
           preferences["favorites"] = feedback["liked"]
       if "disliked" in feedback:
           preferences["avoid"] = feedback["disliked"]
       return preferences

   feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
   updated_preferences = adjust_based_on_feedback(feedback, preferences)
   
   # Odtwórz i wykonaj kod z zaktualizowanymi preferencjami
   updated_flight_code = generate_code_to_fetch_data(updated_preferences)
   updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)
   
   updated_flights = execute_code(updated_flight_code)
   updated_hotels = execute_code(updated_hotel_code)
   
   updated_itinerary = generate_itinerary(updated_flights, updated_hotels, attractions)
   print("Updated Itinerary:", updated_itinerary)
   ```

### Wykorzystanie świadomości środowiskowej i rozumowania

Bazowanie na schemacie tabeli może rzeczywiście usprawnić proces generowania zapytań poprzez wykorzystanie świadomości środowiskowej i rozumowania.

Oto przykład, jak można to zrobić:

1. **Zrozumienie schematu**: System zrozumie schemat tabeli i wykorzysta te informacje do ugruntowania generowania zapytań.
2. **Dostosowywanie na podstawie opinii**: System dostosuje preferencje użytkownika na podstawie opinii i oceni, które pola w schemacie trzeba zaktualizować.
3. **Generowanie i wykonywanie zapytań**: System wygeneruje i wykona zapytania pobierające zaktualizowane dane o lotach i hotelach na podstawie nowych preferencji.

Oto zaktualizowany przykład kodu w Pythonie, który uwzględnia te koncepcje:

```python
def adjust_based_on_feedback(feedback, preferences, schema):
    # Dostosuj preferencje na podstawie opinii użytkownika
    if "liked" in feedback:
        preferences["favorites"] = feedback["liked"]
    if "disliked" in feedback:
        preferences["avoid"] = feedback["disliked"]
    # Wnioskowanie na podstawie schematu w celu dostosowania innych powiązanych preferencji
    for field in schema:
        if field in preferences:
            preferences[field] = adjust_based_on_environment(feedback, field, schema)
    return preferences

def adjust_based_on_environment(feedback, field, schema):
    # Niestandardowa logika dostosowywania preferencji na podstawie schematu i opinii
    if field in feedback["liked"]:
        return schema[field]["positive_adjustment"]
    elif field in feedback["disliked"]:
        return schema[field]["negative_adjustment"]
    return schema[field]["default"]

def generate_code_to_fetch_data(preferences):
    # Wygeneruj kod do pobierania danych o lotach na podstawie zaktualizowanych preferencji
    return f"fetch_flights(preferences={preferences})"

def generate_code_to_fetch_hotels(preferences):
    # Wygeneruj kod do pobierania danych o hotelach na podstawie zaktualizowanych preferencji
    return f"fetch_hotels(preferences={preferences})"

def execute_code(code):
    # Symuluj wykonanie kodu i zwróć dane przykładowe
    return {"data": f"Executed: {code}"}

def generate_itinerary(flights, hotels, attractions):
    # Wygeneruj plan podróży na podstawie lotów, hoteli i atrakcji
    return {"flights": flights, "hotels": hotels, "attractions": attractions}

# Przykładowy schemat
schema = {
    "favorites": {"positive_adjustment": "increase", "negative_adjustment": "decrease", "default": "neutral"},
    "avoid": {"positive_adjustment": "decrease", "negative_adjustment": "increase", "default": "neutral"}
}

# Przykładowe użycie
preferences = {"favorites": "sightseeing", "avoid": "crowded places"}
feedback = {"liked": ["Louvre Museum"], "disliked": ["Eiffel Tower (too crowded)"]}
updated_preferences = adjust_based_on_feedback(feedback, preferences, schema)

# Ponownie wygeneruj i wykonaj kod z zaktualizowanymi preferencjami
updated_flight_code = generate_code_to_fetch_data(updated_preferences)
updated_hotel_code = generate_code_to_fetch_hotels(updated_preferences)

updated_flights = execute_code(updated_flight_code)
updated_hotels = execute_code(updated_hotel_code)

updated_itinerary = generate_itinerary(updated_flights, updated_hotels, feedback["liked"])
print("Updated Itinerary:", updated_itinerary)
```

#### Wyjaśnienie - Rezerwacja na podstawie opinii

1. **Świadomość schematu**: Słownik `schema` definiuje, jak preferencje powinny być dostosowywane na podstawie opinii. Zawiera pola takie jak `favorites` i `avoid` z odpowiadającymi im zmianami.
2. **Dostosowywanie preferencji (metoda `adjust_based_on_feedback`)**: Ta metoda dostosowuje preferencje na podstawie opinii użytkownika i schematu.
3. **Dostosowania oparte na środowisku (metoda `adjust_based_on_environment`)**: Ta metoda dostosowuje zmiany w oparciu o schemat i opinie.
4. **Generowanie i wykonywanie zapytań**: System generuje kod do pobierania zaktualizowanych danych o lotach i hotelach na podstawie dostosowanych preferencji i symuluje wykonanie tych zapytań.
5. **Generowanie harmonogramu**: System tworzy zaktualizowany plan podróży oparty na nowych danych o lotach, hotelach i atrakcjach.

Dzięki świadomości środowiskowej systemu i rozumowaniu na podstawie schematu, może generować dokładniejsze i bardziej trafne zapytania, co prowadzi do lepszych rekomendacji podróży i bardziej spersonalizowanego doświadczenia użytkownika.

### Wykorzystanie SQL jako techniki Retrieval-Augmented Generation (RAG)

SQL (Structured Query Language) to potężne narzędzie do interakcji z bazami danych. Wykorzystując je jako element podejścia Retrieval-Augmented Generation (RAG), SQL może pobierać odpowiednie dane z baz, by informować i generować odpowiedzi czy działania w agentach AI. Zobaczmy, jak SQL może być stosowany jako technika RAG w kontekście Agenta Podróży.

#### Kluczowe koncepcje

1. **Interakcja z bazą danych**:
   - SQL służy do zapytań do baz danych, pobierania odpowiednich informacji i manipulowania danymi.
   - Przykład: Pobieranie szczegółów lotów, informacji o hotelach i atrakcjach z bazy danych podróży.

2. **Integracja z RAG**:
   - Zapytania SQL są generowane na podstawie danych wejściowych i preferencji użytkownika.
   - Pobierane dane są następnie wykorzystywane do generowania spersonalizowanych rekomendacji lub działań.

3. **Dynamiczne generowanie zapytań**:
   - Agent AI generuje dynamiczne zapytania SQL w zależności od kontekstu i potrzeb użytkownika.
   - Przykład: Dostosowywanie zapytań SQL do filtrowania wyników według budżetu, dat i zainteresowań.

#### Zastosowania

- **Automatyczne generowanie kodu**: Generowanie fragmentów kodu do konkretnych zadań.
- **SQL jako RAG**: Używanie zapytań SQL do manipulacji danymi.
- **Rozwiązywanie problemów**: Tworzenie i wykonywanie kodu do rozwiązywania problemów.

**Przykład**:
Agent analizujący dane:

1. **Zadanie**: Analiza zestawu danych w celu znalezienia trendów.
2. **Kroki**:
   - Załaduj zestaw danych.
   - Wygeneruj zapytania SQL do filtrowania danych.
   - Wykonaj zapytania i pobierz wyniki.
   - Wygeneruj wizualizacje i wnioski.
3. **Zasoby**: Dostęp do zestawu danych, możliwości SQL.
4. **Doświadczenie**: Wykorzystaj wyniki wcześniejszych analiz, aby udoskonalić przyszłe analizy.

#### Praktyczny przykład: Wykorzystanie SQL w Agencie Podróży

1. **Zbieranie preferencji użytkownika**

   ```python
   class Travel_Agent:
       def __init__(self):
           self.user_preferences = {}

       def gather_preferences(self, preferences):
           self.user_preferences = preferences
   ```

2. **Generowanie zapytań SQL**

   ```python
   def generate_sql_query(table, preferences):
       query = f"SELECT * FROM {table} WHERE "
       conditions = []
       for key, value in preferences.items():
           conditions.append(f"{key}='{value}'")
       query += " AND ".join(conditions)
       return query
   ```

3. **Wykonywanie zapytań SQL**

   ```python
   import sqlite3

   def execute_sql_query(query, database="travel.db"):
       connection = sqlite3.connect(database)
       cursor = connection.cursor()
       cursor.execute(query)
       results = cursor.fetchall()
       connection.close()
       return results
   ```

4. **Generowanie rekomendacji**

   ```python
   def generate_recommendations(preferences):
       flight_query = generate_sql_query("flights", preferences)
       hotel_query = generate_sql_query("hotels", preferences)
       attraction_query = generate_sql_query("attractions", preferences)
       
       flights = execute_sql_query(flight_query)
       hotels = execute_sql_query(hotel_query)
       attractions = execute_sql_query(attraction_query)
       
       itinerary = {
           "flights": flights,
           "hotels": hotels,
           "attractions": attractions
       }
       return itinerary

   travel_agent = Travel_Agent()
   preferences = {
       "destination": "Paris",
       "dates": "2025-04-01 to 2025-04-10",
       "budget": "moderate",
       "interests": ["museums", "cuisine"]
   }
   travel_agent.gather_preferences(preferences)
   itinerary = generate_recommendations(preferences)
   print("Suggested Itinerary:", itinerary)
   ```

#### Przykładowe zapytania SQL

1. **Zapytanie o loty**

   ```sql
   SELECT * FROM flights WHERE destination='Paris' AND dates='2025-04-01 to 2025-04-10' AND budget='moderate';
   ```

2. **Zapytanie o hotel**

   ```sql
   SELECT * FROM hotels WHERE destination='Paris' AND budget='moderate';
   ```

3. **Zapytanie o atrakcje**

   ```sql
   SELECT * FROM attractions WHERE destination='Paris' AND interests='museums, cuisine';
   ```

Wykorzystując SQL jako część techniki Retrieval-Augmented Generation (RAG), agenci AI tacy jak Agent Podróży mogą dynamicznie pobierać i wykorzystywać odpowiednie dane, by dostarczać dokładne i spersonalizowane rekomendacje.

### Przykład metapoznania

Aby zilustrować implementację metapoznania, stwórzmy prostego agenta, który *reflektuje nad swoim procesem podejmowania decyzji* podczas rozwiązywania problemu. W tym przykładzie zbudujemy system, w którym agent próbuje zoptymalizować wybór hotelu, ale następnie ocenia własne rozumowanie i dostosowuje strategię, gdy popełnia błędy lub dokonuje suboptymalnych wyborów.

Zasymulujemy to, używając prostego przykładu, gdzie agent wybiera hotele na podstawie kombinacji ceny i jakości, ale „reflektuje” nad swoimi decyzjami i dostosowuje się odpowiednio.

#### Jak to ilustruje metapoznanie:

1. **Początkowa decyzja**: Agent wybierze najtańszy hotel, nie rozumiejąc wpływu jakości.
2. **Refleksja i ocena**: Po początkowym wyborze agent sprawdzi, czy hotel był „złym” wyborem, korzystając z opinii użytkownika. Jeśli oceni, że jakość hotelu była zbyt niska, zastanowi się nad swoim rozumowaniem.
3. **Dostosowanie strategii**: Agent dostosuje swoją strategię na podstawie refleksji, zmieniając podejście z „najtańszy” na „najwyższa jakość”, poprawiając tym samym proces podejmowania decyzji w kolejnych iteracjach.

Oto przykład:

```python
class HotelRecommendationAgent:
    def __init__(self):
        self.previous_choices = []  # Przechowuje wcześniej wybrane hotele
        self.corrected_choices = []  # Przechowuje poprawione wybory
        self.recommendation_strategies = ['cheapest', 'highest_quality']  # Dostępne strategie

    def recommend_hotel(self, hotels, strategy):
        """
        Recommend a hotel based on the chosen strategy.
        The strategy can either be 'cheapest' or 'highest_quality'.
        """
        if strategy == 'cheapest':
            recommended = min(hotels, key=lambda x: x['price'])
        elif strategy == 'highest_quality':
            recommended = max(hotels, key=lambda x: x['quality'])
        else:
            recommended = None
        self.previous_choices.append((strategy, recommended))
        return recommended

    def reflect_on_choice(self):
        """
        Reflect on the last choice made and decide if the agent should adjust its strategy.
        The agent considers if the previous choice led to a poor outcome.
        """
        if not self.previous_choices:
            return "No choices made yet."

        last_choice_strategy, last_choice = self.previous_choices[-1]
        # Załóżmy, że mamy opinię użytkownika, która informuje nas, czy ostatni wybór był dobry czy nie
        user_feedback = self.get_user_feedback(last_choice)

        if user_feedback == "bad":
            # Dostosuj strategię, jeśli poprzedni wybór był niezadowalający
            new_strategy = 'highest_quality' if last_choice_strategy == 'cheapest' else 'cheapest'
            self.corrected_choices.append((new_strategy, last_choice))
            return f"Reflecting on choice. Adjusting strategy to {new_strategy}."
        else:
            return "The choice was good. No need to adjust."

    def get_user_feedback(self, hotel):
        """
        Simulate user feedback based on hotel attributes.
        For simplicity, assume if the hotel is too cheap, the feedback is "bad".
        If the hotel has quality less than 7, feedback is "bad".
        """
        if hotel['price'] < 100 or hotel['quality'] < 7:
            return "bad"
        return "good"

# Symuluj listę hoteli (cena i jakość)
hotels = [
    {'name': 'Budget Inn', 'price': 80, 'quality': 6},
    {'name': 'Comfort Suites', 'price': 120, 'quality': 8},
    {'name': 'Luxury Stay', 'price': 200, 'quality': 9}
]

# Utwórz agenta
agent = HotelRecommendationAgent()

# Krok 1: Agent poleca hotel, używając strategii „najtańszy”
recommended_hotel = agent.recommend_hotel(hotels, 'cheapest')
print(f"Recommended hotel (cheapest): {recommended_hotel['name']}")

# Krok 2: Agent zastanawia się nad wyborem i w razie potrzeby dostosowuje strategię
reflection_result = agent.reflect_on_choice()
print(reflection_result)

# Krok 3: Agent ponownie poleca hotel, tym razem używając dostosowanej strategii
adjusted_recommendation = agent.recommend_hotel(hotels, 'highest_quality')
print(f"Adjusted hotel recommendation (highest_quality): {adjusted_recommendation['name']}")
```

#### Zdolności metapoznawcze agentów

Kluczowe jest tutaj zdolność agenta do:
- Oceniania swoich poprzednich wyborów i procesu podejmowania decyzji.
- Dostosowywania swojej strategii na podstawie tej refleksji, czyli metapoznanie w działaniu.

To prosty przykład metapoznania, gdzie system potrafi dostosowywać swój proces rozumowania na podstawie wewnętrznej informacji zwrotnej.

### Podsumowanie

Metapoznanie jest potężnym narzędziem, które może znacząco zwiększyć możliwości agentów AI. Wdrażając procesy metapoznawcze, możesz zaprojektować agentów bardziej inteligentnych, elastycznych i efektywnych. Skorzystaj z dodatkowych zasobów, aby dalej zgłębiać fascynujący świat metapoznania w agentach AI.

### Masz więcej pytań dotyczących wzorca projektowego metapoznania?

Dołącz do [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), aby spotkać innych uczących się, uczestniczyć w godzinach konsultacji i uzyskać odpowiedzi na pytania dotyczące agentów AI.

## Poprzednia lekcja

[Wzorzec projektowy wieloagentowy](../08-multi-agent/README.md)

## Następna lekcja

[Agenci AI w produkcji](../10-ai-agents-production/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->