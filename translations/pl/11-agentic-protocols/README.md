# Korzystanie z protokołów agentów (MCP, A2A oraz NLWeb)

[![Protokoły agentów](../../../translated_images/pl/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Kliknij powyższy obraz, aby obejrzeć wideo z tej lekcji)_

Wraz ze wzrostem wykorzystania agentów AI rośnie potrzeba wprowadzenia protokołów zapewniających standaryzację, bezpieczeństwo oraz wspierających otwartą innowację. W tej lekcji omówimy 3 protokoły odpowiadające tym potrzebom – Model Context Protocol (MCP), Agent to Agent (A2A) oraz Natural Language Web (NLWeb).

## Wprowadzenie

W tej lekcji omówimy:

• Jak **MCP** umożliwia agentom AI dostęp do zewnętrznych narzędzi i danych w celu realizacji zadań użytkownika.

• Jak **A2A** umożliwia komunikację i współpracę między różnymi agentami AI.

• Jak **NLWeb** wprowadza interfejsy języka naturalnego do dowolnej strony internetowej, umożliwiając agentom AI odkrywanie i interakcję z jej zawartością.

## Cele nauki

• **Identyfikować** podstawowy cel i korzyści MCP, A2A i NLWeb w kontekście agentów AI.

• **Wyjaśnić**, w jaki sposób każdy protokół ułatwia komunikację i interakcję między LLM, narzędziami i innymi agentami.

• **Rozpoznać** różne role, jakie pełnią poszczególne protokoły w tworzeniu złożonych systemów agentowych.

## Model Context Protocol

**Model Context Protocol (MCP)** to otwarty standard zapewniający ustandaryzowany sposób, w jaki aplikacje dostarczają kontekst i narzędzia do LLM. Umożliwia to „uniwersalny adapter” do różnych źródeł danych i narzędzi, do których agenci AI mogą się podłączać w spójny sposób.

Przyjrzyjmy się komponentom MCP, korzyściom w porównaniu z bezpośrednim użyciem API oraz przykładowi, jak agenci AI mogą korzystać z serwera MCP.

### Główne komponenty MCP

MCP działa w oparciu o **architekturę klient-serwer**, a główne komponenty to:

• **Hosty** to aplikacje LLM (np. edytor kodu taki jak VSCode), które inicjują połączenia z serwerem MCP.

• **Klienci** to komponenty w aplikacji hosta, które utrzymują połączenia jeden na jeden z serwerami.

• **Serwery** to lekkie programy udostępniające określone funkcjonalności.

Protokół zawiera trzy podstawowe prymitywy, które są możliwościami serwera MCP:

• **Narzędzia**: To oddzielne akcje lub funkcje, które agent AI może wywołać, by wykonać określone działanie. Na przykład serwis pogodowy może udostępniać narzędzie „pobierz pogodę”, a serwer e-commerce — narzędzie „zakup produkt”. Serwery MCP reklamują nazwę, opis oraz schemat wejścia/wyjścia każdego narzędzia w liście swoich możliwości.

• **Zasoby**: To dane tylko do odczytu lub dokumenty, które serwer MCP może udostępnić, a klienci mogą je pobierać na żądanie. Przykłady to zawartość plików, rekordy baz danych lub pliki dziennika. Zasoby mogą być tekstowe (np. kod lub JSON) lub binarne (np. obrazy lub pliki PDF).

• **Podpowiedzi**: To predefiniowane szablony zawierające sugerowane zapytania, umożliwiające tworzenie bardziej złożonych przepływów pracy.

### Korzyści MCP

MCP oferuje znaczące zalety dla agentów AI:

• **Dynamiczne wykrywanie narzędzi**: Agenci mogą dynamicznie otrzymywać listę dostępnych narzędzi od serwera wraz z opisami ich funkcji. W przeciwieństwie do tradycyjnych API, które często wymagają statycznego kodowania integracji, gdzie każda zmiana API wymaga aktualizacji kodu, MCP proponuje podejście „wdróż raz”, co zapewnia większą elastyczność.

• **Interoperacyjność między LLM**: MCP działa z różnymi LLM, oferując elastyczność zmiany podstawowych modeli dla lepszej wydajności.

• **Ustandaryzowane bezpieczeństwo**: MCP zawiera standardową metodę uwierzytelniania, ułatwiając skalowanie przy dodawaniu dostępu do kolejnych serwerów MCP. Jest to prostsze niż zarządzanie różnymi kluczami i typami uwierzytelniania dla tradycyjnych API.

### Przykład MCP

![Diagram MCP](../../../translated_images/pl/mcp-diagram.e4ca1cbd551444a1.webp)

Wyobraź sobie użytkownika chcącego zarezerwować lot za pomocą asystenta AI działającego na MCP.

1. **Połączenie**: Asystent AI (klient MCP) łączy się z serwerem MCP udostępnionym przez linię lotniczą.

2. **Wykrywanie narzędzi**: Klient pyta serwer MCP linii lotniczej: „Jakie narzędzia są dostępne?” Serwer odpowiada narzędziami takimi jak „wyszukaj loty” i „zarezerwuj lot”.

3. **Wywołanie narzędzia**: Następnie prosisz asystenta AI: „Proszę, wyszukaj lot z Portland do Honolulu.” Asystent AI, używając swojego LLM, rozpoznaje, że musi wywołać narzędzie „wyszukaj loty” i przekazuje serwerowi MCP odpowiednie parametry (miejsce wylotu, miejsce docelowe).

4. **Wykonanie i odpowiedź**: Serwer MCP, pełniący funkcję opakowania, wykonuje rzeczywiste wywołanie do wewnętrznego API rezerwacji linii lotniczej. Następnie odbiera informacje o lotach (np. dane JSON) i przesyła je z powrotem do asystenta AI.

5. **Dalsza interakcja**: Asystent AI przedstawia opcje lotów. Po wybraniu lotu asystent może wywołać narzędzie „zarezerwuj lot” na tym samym serwerze MCP, finalizując rezerwację.

## Protokół agent-agent (A2A)

Podczas gdy MCP koncentruje się na łączeniu LLM z narzędziami, **protokół Agent-to-Agent (A2A)** idzie o krok dalej, umożliwiając komunikację i współpracę między różnymi agentami AI. A2A łączy agentów AI w różnych organizacjach, środowiskach i stosach technologicznych, by realizować wspólne zadania.

Przyjrzymy się komponentom i korzyściom A2A oraz przykładzie zastosowania w naszej aplikacji do podróży.

### Główne komponenty A2A

A2A skupia się na umożliwieniu komunikacji między agentami i ich współpracy przy realizacji podzadań użytkownika. Każdy komponent protokołu wspiera to:

#### Karta Agenta

Podobnie jak serwer MCP udostępnia listę narzędzi, Karta Agenta zawiera:
- Nazwę Agenta.
- **opis ogólnych zadań**, które realizuje.
- **listę konkretnych umiejętności** wraz z opisami pomagającymi innym agentom (lub nawet użytkownikom) zrozumieć, kiedy i dlaczego warto wywołać danego agenta.
- **obecny URL endpointu** agenta.
- **wersję** i **możliwości** agenta, takie jak odpowiedzi strumieniowe i powiadomienia push.

#### Wykonawca Agenta

Wykonawca Agenta odpowiada za **przekazywanie kontekstu rozmowy użytkownika do zdalnego agenta**, który potrzebuje tego, by zrozumieć zadanie do wykonania. Na serwerze A2A agent używa własnego modelu językowego (LLM) do analizowania przychodzących żądań i wykonywania zadań z wykorzystaniem swoich narzędzi wewnętrznych.

#### Artefakt

Po wykonaniu zadania przez zdalnego agenta powstaje artefakt. Artefakt **zawiera wynik pracy agenta**, **opis wykonanej pracy** oraz **kontekst tekstowy** przesyłany przez protokół. Po wysłaniu artefaktu połączenie ze zdalnym agentem jest zamykane aż do ponownego wykorzystania.

#### Kolejka zdarzeń

Komponent ten służy do **obsługi aktualizacji i przekazywania wiadomości**. Jest szczególnie ważny w środowiskach produkcyjnych, aby zapobiec zamknięciu połączenia między agentami przed ukończeniem zadania, zwłaszcza gdy czas realizacji może być dłuższy.

### Korzyści A2A

• **Zwiększona współpraca**: Umożliwia agentom od różnych dostawców i na różnych platformach wzajemną interakcję, wymianę kontekstu oraz wspólną pracę, umożliwiając bezproblemową automatyzację między dotychczas oddzielonymi systemami.

• **Elastyczność wyboru modelu**: Każdy agent A2A może sam decydować, który LLM wykorzystuje do obsługi swoich żądań, pozwalając na optymalizację lub dostosowanie modeli indywidualnych dla agenta, w przeciwieństwie do pojedynczego połączenia LLM w niektórych scenariuszach MCP.

• **Wbudowane uwierzytelnianie**: Uwierzytelnianie jest zintegrowane bezpośrednio z protokołem A2A, zapewniając solidne ramy bezpieczeństwa dla interakcji agentów.

### Przykład A2A

![Diagram A2A](../../../translated_images/pl/A2A-Diagram.8666928d648acc26.webp)

Rozbudujmy nasz scenariusz rezerwacji podróży, tym razem korzystając z A2A.

1. **Żądanie użytkownika do multi-agenta**: Użytkownik wchodzi w interakcję z klientem/agenta A2A o nazwie „Agent Podróży”, na przykład mówiąc: „Proszę zarezerwuj cały wyjazd do Honolulu na przyszły tydzień, obejmujący loty, hotel i wynajem samochodu”.

2. **Orkiestracja przez Agenta Podróży**: Agent Podróży odbiera to złożone żądanie. Wykorzystuje swój LLM, by przeanalizować zadanie i ustalić, że musi współpracować z innymi wyspecjalizowanymi agentami.

3. **Komunikacja między agentami**: Agent Podróży łączy się za pomocą protokołu A2A z agentami podrzędnymi, takimi jak „Agent Linii Lotniczej”, „Agent Hotelu” i „Agent Wynajmu Samochodu”, tworzonymi przez różne firmy.

4. **Delegowanie wykonania zadań**: Agent Podróży przesyła konkretne zadania do tych specjalistycznych agentów (np. „Znajdź loty do Honolulu”, „Zarezerwuj hotel”, „Wynajmij samochód”). Każdy z tych wyspecjalizowanych agentów, korzystając z własnego LLM i własnych narzędzi (które mogą być samodzielnymi serwerami MCP), wykonuje swoją część rezerwacji.

5. **Zintegrowana odpowiedź**: Gdy wszyscy agenci podrzędni ukończą zadania, Agent Podróży kompiluje wyniki (szczegóły lotu, potwierdzenie hotelu, rezerwację samochodu) i wysyła kompleksową odpowiedź w stylu czatu do użytkownika.

## Natural Language Web (NLWeb)

Strony internetowe od dawna stanowią główny sposób dostępu użytkowników do informacji i danych w internecie.

Przyjrzyjmy się różnym komponentom NLWeb, korzyściom korzystania z NLWeb oraz przykładzie działania NLWeb na naszym przykładzie aplikacji do podróży.

### Komponenty NLWeb

- **Aplikacja NLWeb (główny kod usługi)**: System przetwarzający pytania w języku naturalnym. Łączy różne części platformy, tworząc odpowiedzi. Można go uważać za **silnik napędzający funkcje języka naturalnego** na stronie internetowej.

- **Protokół NLWeb**: To **podstawowy zestaw reguł do interakcji w języku naturalnym** ze stroną internetową. Wysyła odpowiedzi w formacie JSON (często korzystając ze Schema.org). Jego celem jest stworzenie prostych podstaw dla „AI Web”, podobnie jak HTML umożliwił udostępnianie dokumentów online.

- **Serwer MCP (endpoint Model Context Protocol)**: Każda konfiguracja NLWeb działa także jako **serwer MCP**. Oznacza to, że może **udostępniać narzędzia (np. metodę „ask”) oraz dane** innym systemom AI. W praktyce umożliwia to wykorzystanie zawartości i funkcji strony przez agentów AI, czyniąc ją częścią szerszego „ekosystemu agentów”.

- **Modele osadzania (embedding models)**: Modele te służą do **konwertowania zawartości strony na reprezentacje numeryczne zwane wektorami (embeddingami)**. Wektory te uchwytują znaczenie w sposób zrozumiały dla komputerów, umożliwiając porównywanie i wyszukiwanie. Są przechowywane w specjalnej bazie danych, a użytkownicy mogą wybierać, którego modelu osadzenia użyć.

- **Baza wektorowa (mechanizm wyszukiwania)**: Ta baza **przechowuje embeddingi zawartości strony**. Gdy ktoś zada pytanie, NLWeb przeszukuje bazę, aby szybko znaleźć najbardziej odpowiednie informacje. Zwraca listę możliwych odpowiedzi, uporządkowaną według podobieństwa. NLWeb współpracuje z różnymi systemami przechowywania wektorów, takimi jak Qdrant, Snowflake, Milvus, Azure AI Search oraz Elasticsearch.

### NLWeb na przykładzie

![NLWeb](../../../translated_images/pl/nlweb-diagram.c1e2390b310e5fe4.webp)

Rozważmy ponownie naszą stronę do rezerwacji podróży, tym razem z zasilaniem NLWeb.

1. **Przetwarzanie danych**: Istniejące katalogi produktów na stronie podróżniczej (np. listy lotów, opisy hoteli, pakiety wycieczek) są formatowane za pomocą Schema.org lub ładowane przez kanały RSS. Narzędzia NLWeb przetwarzają te ustrukturyzowane dane, tworzą embeddingi i przechowują je w lokalnej lub zdalnej bazie wektorowej.

2. **Zapytanie w języku naturalnym (użytkownik)**: Użytkownik odwiedza stronę i zamiast nawigować po menu, wpisuje w interfejsie czatu: „Znajdź mi hotel przyjazny rodzinom w Honolulu z basenem na przyszły tydzień”.

3. **Przetwarzanie przez NLWeb**: Aplikacja NLWeb odbiera to zapytanie. Wysyła je do LLM w celu zrozumienia oraz jednocześnie przeszukuje bazę wektorową w poszukiwaniu odpowiednich ofert hotelowych.

4. **Dokładne wyniki**: LLM pomaga zinterpretować wyniki z bazy danych, wskazać najlepsze dopasowania na podstawie kryteriów „przyjazny rodzinom”, „basen” i „Honolulu”, a następnie formatuje odpowiedź w języku naturalnym. Co ważne, odpowiedź odwołuje się do faktycznych hoteli z katalogu strony, unikając wymyślonych informacji.

5. **Interakcja agenta AI**: Ponieważ NLWeb działa jako serwer MCP, zewnętrzny agent AI do podróży mógłby połączyć się z tą instancją NLWeb strony. Agent AI mógłby wtedy użyć metody `ask` MCP, by bezpośrednio zapytać stronę: `ask("Czy są jakieś wegańskie restauracje w okolicy Honolulu rekomendowane przez hotel?")`. Instancja NLWeb przetworzyłaby to, wykorzystując swoją bazę informacji o restauracjach (jeśli została załadowana), i zwróciła ustrukturyzowaną odpowiedź JSON.

### Masz więcej pytań dotyczących MCP/A2A/NLWeb?

Dołącz do [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), aby spotkać innych uczących się, uczestniczyć w godzinach konsultacji i uzyskać odpowiedzi na pytania dotyczące agentów AI.

## Zasoby

- [MCP dla początkujących](https://aka.ms/mcp-for-beginners)  
- [Dokumentacja MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Repozytorium NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framework)

## Poprzednia lekcja

[Agenci AI w produkcji](../10-ai-agents-production/README.md)

## Następna lekcja

[Inżynieria kontekstu dla agentów AI](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->