<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "aff92c6f019b4627ca9399c6e3882e17",
  "translation_date": "2025-09-18T14:50:37+00:00",
  "source_file": "11-agentic-protocols/README.md",
  "language_code": "pl"
}
-->
# Korzystanie z protokołów agentowych (MCP, A2A i NLWeb)

[![Protokoły agentowe](../../../translated_images/lesson-11-thumbnail.b6c742949cf1ce2aa0255968d287b31c99b51dfa9c9beaede7c3fbed90e8fcfb.pl.png)](https://youtu.be/X-Dh9R3Opn8)

> _(Kliknij obrazek powyżej, aby obejrzeć wideo z tej lekcji)_

Wraz ze wzrostem wykorzystania agentów AI rośnie potrzeba protokołów zapewniających standaryzację, bezpieczeństwo i wspierających otwartą innowację. W tej lekcji omówimy trzy protokoły, które mają na celu spełnienie tych potrzeb: Model Context Protocol (MCP), Agent to Agent (A2A) oraz Natural Language Web (NLWeb).

## Wprowadzenie

W tej lekcji omówimy:

• Jak **MCP** umożliwia agentom AI dostęp do zewnętrznych narzędzi i danych w celu realizacji zadań użytkownika.

• Jak **A2A** pozwala na komunikację i współpracę między różnymi agentami AI.

• Jak **NLWeb** wprowadza interfejsy w języku naturalnym na każdą stronę internetową, umożliwiając agentom AI odkrywanie i interakcję z treścią.

## Cele nauki

• **Zidentyfikować** główny cel i korzyści MCP, A2A i NLWeb w kontekście agentów AI.

• **Wyjaśnić**, jak każdy z protokołów ułatwia komunikację i interakcję między LLM, narzędziami i innymi agentami.

• **Rozpoznać** różne role, jakie każdy protokół odgrywa w budowaniu złożonych systemów agentowych.

## Model Context Protocol

**Model Context Protocol (MCP)** to otwarty standard, który zapewnia ustandaryzowany sposób, w jaki aplikacje dostarczają kontekst i narzędzia do LLM. Umożliwia to "uniwersalny adapter" do różnych źródeł danych i narzędzi, z którymi agenci AI mogą się łączyć w spójny sposób.

Przyjrzyjmy się komponentom MCP, korzyściom w porównaniu z bezpośrednim użyciem API oraz przykładowi, jak agenci AI mogą korzystać z serwera MCP.

### Główne komponenty MCP

MCP działa w oparciu o **architekturę klient-serwer**, a jego główne komponenty to:

• **Hosty** to aplikacje LLM (na przykład edytor kodu, taki jak VSCode), które inicjują połączenia z serwerem MCP.

• **Klienci** to komponenty w aplikacji hosta, które utrzymują połączenia jeden-do-jednego z serwerami.

• **Serwery** to lekkie programy, które udostępniają określone funkcje.

Protokół zawiera trzy podstawowe prymitywy, które definiują możliwości serwera MCP:

• **Narzędzia**: Są to konkretne akcje lub funkcje, które agent AI może wywołać, aby wykonać zadanie. Na przykład serwis pogodowy może udostępniać narzędzie "get weather", a serwer e-commerce narzędzie "purchase product". Serwery MCP reklamują nazwę, opis i schemat wejścia/wyjścia każdego narzędzia w swojej liście możliwości.

• **Zasoby**: Są to elementy danych lub dokumenty tylko do odczytu, które serwer MCP może dostarczyć, a klienci mogą je pobierać na żądanie. Przykłady obejmują zawartość plików, rekordy baz danych lub pliki logów. Zasoby mogą być tekstowe (np. kod lub JSON) lub binarne (np. obrazy lub PDF).

• **Podpowiedzi**: Są to wstępnie zdefiniowane szablony, które dostarczają sugerowane podpowiedzi, umożliwiając bardziej złożone przepływy pracy.

### Korzyści MCP

MCP oferuje znaczące korzyści dla agentów AI:

• **Dynamiczne odkrywanie narzędzi**: Agenci mogą dynamicznie otrzymywać listę dostępnych narzędzi z serwera wraz z opisami ich funkcji. W przeciwieństwie do tradycyjnych API, które często wymagają statycznego kodowania integracji, MCP oferuje podejście "zintegrować raz", co prowadzi do większej elastyczności.

• **Interoperacyjność między LLM**: MCP działa z różnymi LLM, zapewniając elastyczność w przełączaniu modeli podstawowych w celu oceny lepszej wydajności.

• **Standaryzowane bezpieczeństwo**: MCP zawiera standardową metodę uwierzytelniania, co ułatwia skalowanie przy dodawaniu dostępu do kolejnych serwerów MCP. Jest to prostsze niż zarządzanie różnymi kluczami i typami uwierzytelniania dla różnych tradycyjnych API.

### Przykład MCP

![Diagram MCP](../../../translated_images/mcp-diagram.e4ca1cbd551444a12e1f0eb300191a036ab01124fce71c864fe9cb7f4ac2a15d.pl.png)

Wyobraź sobie, że użytkownik chce zarezerwować lot za pomocą asystenta AI obsługiwanego przez MCP.

1. **Połączenie**: Asystent AI (klient MCP) łączy się z serwerem MCP udostępnionym przez linię lotniczą.

2. **Odkrywanie narzędzi**: Klient pyta serwer MCP linii lotniczej: "Jakie narzędzia są dostępne?" Serwer odpowiada narzędziami, takimi jak "search flights" i "book flights".

3. **Wywołanie narzędzia**: Następnie prosisz asystenta AI: "Proszę wyszukaj lot z Portland do Honolulu." Asystent AI, korzystając ze swojego LLM, identyfikuje, że musi wywołać narzędzie "search flights" i przekazuje odpowiednie parametry (miejsce wylotu, miejsce docelowe) do serwera MCP.

4. **Wykonanie i odpowiedź**: Serwer MCP, działając jako wrapper, wykonuje rzeczywiste wywołanie wewnętrznego API rezerwacji linii lotniczej. Następnie otrzymuje informacje o locie (np. dane JSON) i przesyła je z powrotem do asystenta AI.

5. **Dalsza interakcja**: Asystent AI przedstawia opcje lotów. Po wybraniu lotu asystent może wywołać narzędzie "book flight" na tym samym serwerze MCP, finalizując rezerwację.

## Protokół Agent-to-Agent (A2A)

Podczas gdy MCP koncentruje się na łączeniu LLM z narzędziami, **Agent-to-Agent (A2A)** idzie o krok dalej, umożliwiając komunikację i współpracę między różnymi agentami AI. A2A łączy agentów AI z różnych organizacji, środowisk i stosów technologicznych, aby wspólnie realizować zadanie.

Przyjrzymy się komponentom i korzyściom A2A oraz przykładowi jego zastosowania w naszej aplikacji podróżniczej.

### Główne komponenty A2A

A2A koncentruje się na umożliwieniu komunikacji między agentami i ich współpracy w realizacji podzadania użytkownika. Każdy komponent protokołu przyczynia się do tego:

#### Karta agenta

Podobnie jak serwer MCP udostępnia listę narzędzi, karta agenta zawiera:
- Nazwę agenta.
- **Opis ogólnych zadań**, które wykonuje.
- **Listę konkretnych umiejętności** z opisami, które pomagają innym agentom (lub nawet użytkownikom) zrozumieć, kiedy i dlaczego warto wywołać tego agenta.
- **Aktualny URL punktu końcowego** agenta.
- **Wersję** i **możliwości** agenta, takie jak odpowiedzi strumieniowe i powiadomienia push.

#### Wykonawca agenta

Wykonawca agenta odpowiada za **przekazywanie kontekstu rozmowy użytkownika do zdalnego agenta**, który potrzebuje tego, aby zrozumieć zadanie do wykonania. W serwerze A2A agent korzysta z własnego modelu LLM, aby analizować przychodzące żądania i wykonywać zadania za pomocą własnych wewnętrznych narzędzi.

#### Artefakt

Po zakończeniu zadania przez zdalnego agenta jego produkt pracy jest tworzony jako artefakt. Artefakt **zawiera wynik pracy agenta**, **opis tego, co zostało wykonane**, oraz **tekstowy kontekst**, który jest przesyłany przez protokół. Po przesłaniu artefaktu połączenie ze zdalnym agentem zostaje zamknięte, dopóki nie będzie ponownie potrzebne.

#### Kolejka zdarzeń

Ten komponent służy do **obsługi aktualizacji i przekazywania wiadomości**. Jest szczególnie ważny w produkcji dla systemów agentowych, aby zapobiec zamknięciu połączenia między agentami przed zakończeniem zadania, zwłaszcza gdy czas realizacji zadania może być dłuższy.

### Korzyści A2A

• **Zwiększona współpraca**: Umożliwia agentom z różnych dostawców i platform interakcję, dzielenie się kontekstem i współpracę, ułatwiając płynną automatyzację w tradycyjnie odłączonych systemach.

• **Elastyczność wyboru modelu**: Każdy agent A2A może zdecydować, który LLM wykorzysta do obsługi swoich żądań, pozwalając na optymalizację lub dostosowanie modeli dla każdego agenta, w przeciwieństwie do pojedynczego połączenia LLM w niektórych scenariuszach MCP.

• **Wbudowane uwierzytelnianie**: Uwierzytelnianie jest zintegrowane bezpośrednio z protokołem A2A, zapewniając solidne ramy bezpieczeństwa dla interakcji agentów.

### Przykład A2A

![Diagram A2A](../../../translated_images/A2A-Diagram.8666928d648acc2687db4093d7b09ea2a595622f8fe18194a026ee55fc23af8e.pl.png)

Rozwińmy nasz scenariusz rezerwacji podróży, ale tym razem używając A2A.

1. **Żądanie użytkownika do multi-agenta**: Użytkownik wchodzi w interakcję z "Agentem podróży" (klientem/agentem A2A), mówiąc na przykład: "Proszę zarezerwuj całą podróż do Honolulu na przyszły tydzień, w tym loty, hotel i samochód."

2. **Orkiestracja przez agenta podróży**: Agent podróży otrzymuje to złożone żądanie. Korzysta ze swojego LLM, aby rozważyć zadanie i określić, że musi współpracować z innymi wyspecjalizowanymi agentami.

3. **Komunikacja między agentami**: Agent podróży korzysta z protokołu A2A, aby połączyć się z agentami podrzędnymi, takimi jak "Agent linii lotniczych", "Agent hotelowy" i "Agent wynajmu samochodów", które są tworzone przez różne firmy.

4. **Delegowane wykonanie zadania**: Agent podróży wysyła konkretne zadania do tych wyspecjalizowanych agentów (np. "Znajdź loty do Honolulu", "Zarezerwuj hotel", "Wynajmij samochód"). Każdy z tych wyspecjalizowanych agentów, korzystając z własnych LLM i narzędzi (które mogą być serwerami MCP), wykonuje swoją część rezerwacji.

5. **Skompilowana odpowiedź**: Po zakończeniu zadań przez wszystkich agentów podrzędnych, agent podróży kompiluje wyniki (szczegóły lotu, potwierdzenie hotelu, rezerwacja samochodu) i przesyła kompleksową odpowiedź w stylu rozmowy z powrotem do użytkownika.

## Natural Language Web (NLWeb)

Strony internetowe od dawna są głównym sposobem dostępu użytkowników do informacji i danych w internecie.

Przyjrzyjmy się różnym komponentom NLWeb, korzyściom NLWeb oraz przykładowi działania NLWeb na podstawie naszej aplikacji podróżniczej.

### Komponenty NLWeb

- **Aplikacja NLWeb (Kod usługi podstawowej)**: System, który przetwarza pytania w języku naturalnym. Łączy różne części platformy, aby tworzyć odpowiedzi. Można go traktować jako **silnik napędzający funkcje języka naturalnego** strony internetowej.

- **Protokół NLWeb**: To **podstawowy zestaw reguł dla interakcji w języku naturalnym** ze stroną internetową. Zwraca odpowiedzi w formacie JSON (często używając Schema.org). Jego celem jest stworzenie prostego fundamentu dla "AI Web", podobnie jak HTML umożliwił udostępnianie dokumentów online.

- **Serwer MCP (Punkt końcowy Model Context Protocol)**: Każda konfiguracja NLWeb działa również jako **serwer MCP**. Oznacza to, że może **udostępniać narzędzia (np. metodę "ask") i dane** innym systemom AI. W praktyce pozwala to na wykorzystanie treści i możliwości strony internetowej przez agentów AI, czyniąc stronę częścią szerszego "ekosystemu agentów".

- **Modele osadzania**: Modele te są używane do **konwersji treści strony internetowej na reprezentacje numeryczne zwane wektorami** (osadzenia). Wektory te uchwytują znaczenie w sposób, który komputery mogą porównywać i wyszukiwać. Są przechowywane w specjalnej bazie danych, a użytkownicy mogą wybrać, który model osadzania chcą używać.

- **Baza danych wektorów (Mechanizm wyszukiwania)**: Ta baza danych **przechowuje osadzenia treści strony internetowej**. Gdy ktoś zada pytanie, NLWeb sprawdza bazę danych wektorów, aby szybko znaleźć najbardziej odpowiednie informacje. Dostarcza szybką listę możliwych odpowiedzi, uporządkowaną według podobieństwa. NLWeb współpracuje z różnymi systemami przechowywania wektorów, takimi jak Qdrant, Snowflake, Milvus, Azure AI Search i Elasticsearch.

### NLWeb na przykładzie

![NLWeb](../../../translated_images/nlweb-diagram.c1e2390b310e5fe4b245b86690ac6c49c26e355da5ab124128c8675d58cc9b07.pl.png)

Rozważmy naszą stronę internetową do rezerwacji podróży, ale tym razem zasilaną przez NLWeb.

1. **Pobieranie danych**: Istniejące katalogi produktów strony podróżniczej (np. listy lotów, opisy hoteli, pakiety wycieczek) są formatowane za pomocą Schema.org lub ładowane przez kanały RSS. Narzędzia NLWeb pobierają te dane strukturalne, tworzą osadzenia i przechowują je w lokalnej lub zdalnej bazie danych wektorów.

2. **Zapytanie w języku naturalnym (człowiek)**: Użytkownik odwiedza stronę internetową i zamiast nawigować po menu, wpisuje w interfejsie czatu: "Znajdź mi hotel przyjazny rodzinom w Honolulu z basenem na przyszły tydzień".

3. **Przetwarzanie NLWeb**: Aplikacja NLWeb otrzymuje to zapytanie. Wysyła je do LLM w celu zrozumienia i jednocześnie przeszukuje swoją bazę danych wektorów w poszukiwaniu odpowiednich ofert hotelowych.

4. **Dokładne wyniki**: LLM pomaga zinterpretować wyniki wyszukiwania z bazy danych, zidentyfikować najlepsze dopasowania na podstawie kryteriów "przyjazny rodzinom", "basen" i "Honolulu", a następnie formatuje odpowiedź w języku naturalnym. Co ważne, odpowiedź odnosi się do rzeczywistych hoteli z katalogu strony, unikając wymyślonych informacji.

5. **Interakcja z agentem AI**: Ponieważ NLWeb działa jako serwer MCP, zewnętrzny agent podróżniczy AI mógłby również połączyć się z instancją NLWeb tej strony. Agent AI mógłby wtedy użyć metody `ask` MCP, aby bezpośrednio zapytać stronę: `ask("Czy są jakieś restauracje przyjazne weganom w okolicy Honolulu polecane przez hotel?")`. Instancja NLWeb przetworzyłaby to, wykorzystując swoją bazę danych informacji o restauracjach (jeśli załadowana), i zwróciłaby odpowiedź w formacie JSON.

### Masz więcej pytań dotyczących MCP/A2A/NLWeb?

Dołącz do [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), aby spotkać się z innymi uczącymi się, uczestniczyć w godzinach konsultacji i uzyskać odpowiedzi na pytania dotyczące agentów AI.

## Zasoby

- [MCP dla początkujących](https://aka.ms/mcp-for-beginners)  
- [Dokumentacja MCP](https://github.com/microsoft/semantic-kernel/tree/main/python/semantic-kernel/semantic_kernel/connectors/mcp)
- [Repozytorium NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Przewodniki Semantic Kernel](https://learn.microsoft.com/semantic-kernel/)

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.