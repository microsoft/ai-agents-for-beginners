# Korzystanie z protokołów agentowych (MCP, A2A i NLWeb)

[![Agentic Protocols](../../../translated_images/pl/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Kliknij obraz powyżej, aby obejrzeć wideo z tej lekcji)_

Wraz z rosnącym wykorzystaniem agentów AI zwiększa się również potrzeba protokołów zapewniających standaryzację, bezpieczeństwo i wspierających otwartą innowację. W tej lekcji omówimy 3 protokoły, które mają na celu sprostać tym potrzebom - Model Context Protocol (MCP), Agent to Agent (A2A) oraz Natural Language Web (NLWeb).

## Wprowadzenie

W tej lekcji omówimy:

• Jak **MCP** pozwala agentom AI na dostęp do zewnętrznych narzędzi i danych w celu realizacji zadań użytkownika.

• Jak **A2A** umożliwia komunikację i współpracę między różnymi agentami AI.

• Jak **NLWeb** wprowadza interfejsy w naturalnym języku do dowolnej strony internetowej, umożliwiając agentom AI odkrywanie i interakcję z jej treścią.

## Cele nauki

• **Zidentyfikować** podstawowy cel i korzyści MCP, A2A i NLWeb w kontekście agentów AI.

• **Wyjaśnić** jak każdy protokół ułatwia komunikację i interakcję między LLM, narzędziami i innymi agentami.

• **Rozpoznać** odrębne role, jakie pełni każdy protokół w budowaniu złożonych systemów agentowych.

## Model Context Protocol

**Model Context Protocol (MCP)** to otwarty standard, który zapewnia ustandaryzowany sposób na dostarczanie kontekstu i narzędzi do LLM przez aplikacje. Umożliwia to "uniwersalny adapter" do różnych źródeł danych i narzędzi, z którymi agenci AI mogą łączyć się w spójny sposób.

Przyjrzyjmy się komponentom MCP, korzyściom w porównaniu z bezpośrednim użyciem API oraz przykładowi, jak agenci AI mogą korzystać z serwera MCP.

### Podstawowe komponenty MCP

MCP działa na **architekturze klient-serwer**, a główne komponenty to:

• **Hosty** to aplikacje LLM (na przykład edytor kodu jak VSCode), które inicjują połączenia z serwerem MCP.

• **Klienci** to komponenty w aplikacji hosta, które utrzymują połączenia jeden do jednego z serwerami.

• **Serwery** to lekkie programy udostępniające określone możliwości.

W protokole są trzy podstawowe prymitywy, które stanowią możliwości serwera MCP:

• **Narzędzia**: są to dyskretne akcje lub funkcje, które agent AI może wywołać, aby wykonać działanie. Na przykład usługa pogodowa może udostępniać narzędzie "pobierz pogodę", a serwer e-commerce - narzędzie "zakup produkt". Serwery MCP reklamują nazwę narzędzia, opis oraz schemat danych wejściowych/wyjściowych w swojej liście możliwości.

• **Zasoby**: to dane lub dokumenty tylko do odczytu, które serwer MCP może udostępnić, a klienci mogą je pobierać na żądanie. Przykłady to zawartość plików, rekordy bazy danych lub pliki dziennika. Zasoby mogą być tekstowe (np. kod, JSON) lub binarne (np. obrazy, PDF).

• **Podpowiedzi** (Prompts): to zdefiniowane szablony, które dostarczają sugerowanych poleceń, umożliwiając bardziej złożone przepływy pracy.

### Korzyści z MCP

MCP oferuje znaczące zalety dla agentów AI:

• **Dynamiczne wykrywanie narzędzi**: Agenty mogą dynamicznie otrzymać listę dostępnych narzędzi z serwera wraz z opisami ich funkcji. W przeciwieństwie do tradycyjnych API, które często wymagają statycznego kodowania integracji i aktualizacji kodu przy każdej zmianie API, MCP daje podejście "zintegrować raz", co zapewnia większą elastyczność.

• **Interoperacyjność między LLM**: MCP działa na różnych LLM, oferując elastyczność w przełączaniu się między modelami bazowymi w celu uzyskania lepszej wydajności.

• **Ustandaryzowane zabezpieczenia**: MCP zawiera standardową metodę uwierzytelniania, co ułatwia skalowanie przy dodawaniu dostępu do kolejnych serwerów MCP. Jest to prostsze niż zarządzanie różnymi kluczami i typami uwierzytelniania w tradycyjnych API.

### Przykład MCP

![MCP Diagram](../../../translated_images/pl/mcp-diagram.e4ca1cbd551444a1.webp)

Wyobraź sobie, że użytkownik chce zarezerwować lot korzystając z asystenta AI opartego na MCP.

1. **Połączenie**: Asystent AI (klient MCP) łączy się z serwerem MCP udostępnionym przez linię lotniczą.

2. **Wykrywanie narzędzi**: Klient pyta serwer MCP linii lotniczej: „Jakie narzędzia masz dostępne?” Serwer odpowiada narzędziami takimi jak "wyszukaj loty" i "rezerwuj loty".

3. **Wywołanie narzędzia**: Następnie użytkownik prosi asystenta AI: „Proszę wyszukaj lot z Portland do Honolulu.” Asystent AI, korzystając ze swojego LLM, identyfikuje, że musi wywołać narzędzie "wyszukaj loty" i przekazuje odpowiednie parametry (miejsce wylotu, miejsce docelowe) do serwera MCP.

4. **Wykonanie i odpowiedź**: Serwer MCP, działając jako wrapper, wykonuje faktyczne wywołanie wewnętrznego API rezerwacji linii lotniczej. Otrzymuje informacje o lotach (np. dane JSON) i przesyła je z powrotem do asystenta AI.

5. **Dalsza interakcja**: Asystent AI przedstawia dostępne opcje lotów. Po wybraniu lotu asystent może wywołać narzędzie "rezerwuj lot" na tym samym serwerze MCP, kończąc rezerwację.

## Protokół Agent-to-Agent (A2A)

Podczas gdy MCP koncentruje się na łączeniu LLM z narzędziami, protokół **Agent-to-Agent (A2A)** idzie o krok dalej, umożliwiając komunikację i współpracę między różnymi agentami AI. A2A łączy agentów AI z różnych organizacji, środowisk i stosów technologicznych w celu realizacji wspólnego zadania.

Przyjrzymy się komponentom i korzyściom A2A oraz przykładzie zastosowania go w naszej aplikacji podróżniczej.

### Podstawowe komponenty A2A

A2A skupia się na umożliwieniu komunikacji między agentami i współpracy w realizacji podzadań użytkownika. Każdy komponent protokołu przyczynia się do tego:

#### Karta Agenta

Podobnie jak serwer MCP udostępnia listę narzędzi, Karta Agenta zawiera:  
- Nazwę Agenta.  
- **opis ogólnych zadań**, które wykonuje.  
- **listę konkretnych umiejętności** z opisami, które pomagają innym agentom (lub nawet użytkownikom) zrozumieć, kiedy i dlaczego warto wywołać tego agenta.  
- **aktualny URL końcówki** agenta  
- **wersję** i **możliwości** agenta, takie jak strumieniowe odpowiedzi i powiadomienia push.

#### Wykonawca Agenta

Wykonawca Agenta jest odpowiedzialny za **przekazywanie kontekstu rozmowy użytkownika do zdalnego agenta**; zdalny agent potrzebuje tego, aby zrozumieć zadanie do wykonania. W serwerze A2A agent używa własnego dużego modelu językowego (LLM) do analizowania przychodzących żądań i realizacji zadań za pomocą własnych wewnętrznych narzędzi.

#### Artefakt

Po zakończeniu zadania przez zdalnego agenta tworzony jest artefakt. Artefakt **zawiera wynik pracy agenta**, **opis wykonanej pracy** oraz **kontekst tekstowy** przesyłany przez protokół. Po przesłaniu artefaktu połączenie ze zdalnym agentem jest zamykane do następnej potrzeby.

#### Kolejka zdarzeń

Ten komponent służy do **obsługi aktualizacji i przesyłania wiadomości**. Jest szczególnie ważny w produkcji systemów agentowych, aby zapobiec zamknięciu połączenia między agentami przed ukończeniem zadania, szczególnie gdy realizacja zadań może trwać długo.

### Korzyści A2A

• **Rozszerzona współpraca**: Umożliwia agentom z różnych dostawców i platform współdziałanie, dzielenie się kontekstem i wspólną pracę, co ułatwia płynną automatyzację między tradycyjnie odizolowanymi systemami.

• **Elastyczność wyboru modelu**: Każdy agent A2A może zdecydować, którego LLM użyje do obsługi swoich żądań, co pozwala na optymalizację lub dostosowanie modeli per agent, w przeciwieństwie do pojedynczego połączenia LLM w niektórych scenariuszach MCP.

• **Wbudowane uwierzytelnianie**: Uwierzytelnianie jest zintegrowane bezpośrednio w protokole A2A, zapewniając solidne ramy bezpieczeństwa dla interakcji agentów.

### Przykład A2A

![A2A Diagram](../../../translated_images/pl/A2A-Diagram.8666928d648acc26.webp)

Rozbudujmy nasz scenariusz rezerwacji podróży, tym razem używając A2A.

1. **Żądanie użytkownika do multiagenta**: Użytkownik rozmawia z klientem/agenta A2A "Agent Podróży", na przykład mówiąc: „Zarezerwuj całą wycieczkę do Honolulu na przyszły tydzień, łącznie z lotami, hotelem i wynajmem samochodu”.

2. **Orkiestracja przez Agenta Podróży**: Agent Podróży otrzymuje to złożone żądanie. Używa swojego LLM, aby rozważyć zadanie i stwierdzić, że musi komunikować się z innymi wyspecjalizowanymi agentami.

3. **Komunikacja między agentami**: Agent Podróży używa protokołu A2A do połączenia się z agnetami podrzędnymi, takimi jak "Agent Linii Lotniczych", "Agent Hotelowy" i "Agent Wynajmu Samochodów", stworzonymi przez różne firmy.

4. **Delegowanie wykonania zadań**: Agent Podróży wysyła konkretne zadania tym wyspecjalizowanym agentom (np. "Znajdź loty do Honolulu", "Zarezerwuj hotel", "Wynajmij samochód"). Każdy z tych agentów, uruchamiający własne LLM i korzystający ze swoich narzędzi (które mogą być również serwerami MCP), wykonuje swoją część rezerwacji.

5. **Zjednoczona odpowiedź**: Gdy wszyscy agenci podrzędni zakończą swoje zadania, Agent Podróży kompiluje wyniki (szczegóły lotów, potwierdzenie hotelu, rezerwację samochodu) i wysyła kompleksową, stylizowaną na czat odpowiedź do użytkownika.

## Natural Language Web (NLWeb)

Strony internetowe od dawna są głównym sposobem dostępu użytkowników do informacji i danych w internecie.

Przyjrzyjmy się różnym komponentom NLWeb, korzyściom NLWeb oraz przykładowi działania NLWeb na przykładzie naszej aplikacji podróżniczej.

### Komponenty NLWeb

- **Aplikacja NLWeb (kod podstawowej usługi)**: System przetwarzający pytania w języku naturalnym. Łączy różne części platformy, aby tworzyć odpowiedzi. Możesz to uznać za **silnik napędzający funkcje naturalnego języka** na stronie internetowej.

- **Protokół NLWeb**: To **podstawowy zestaw zasad interakcji w języku naturalnym** ze stroną internetową. Zwraca odpowiedzi w formacie JSON (często używając Schema.org). Jego celem jest stworzenie prostej podstawy dla „AI Web”, podobnie jak HTML umożliwił udostępnianie dokumentów online.

- **Serwer MCP (Model Context Protocol Endpoint)**: Każda konfiguracja NLWeb działa również jako **serwer MCP**. Oznacza to, że może **udostępniać narzędzia (takie jak metoda „ask”) i dane** innym systemom AI. W praktyce sprawia to, że treść i funkcje strony mogą być używane przez agentów AI, pozwalając stronie stać się częścią szerszego „ekosystemu agentowego”.

- **Modele osadzania (Embedding Models)**: Modele te służą do **konwersji treści strony internetowej na reprezentacje numeryczne zwane wektorami (embeddingami)**. Wektory te uchwytują znaczenie w sposób umożliwiający komputerom porównywanie i wyszukiwanie. Są przechowywane w specjalnej bazie danych, a użytkownicy mogą wybrać, którego modelu embeddingów chcą użyć.

- **Baza danych wektorowych (mechanizm wyszukiwania)**: Ta baza danych **przechowuje embeddingi treści strony**. Kiedy ktoś zada pytanie, NLWeb sprawdza bazę danych wektorów, aby szybko znaleźć najbardziej odpowiednie informacje. Generuje szybką listę możliwych odpowiedzi, uporządkowaną według podobieństwa. NLWeb współpracuje z różnymi systemami przechowywania wektorów, takimi jak Qdrant, Snowflake, Milvus, Azure AI Search i Elasticsearch.

### NLWeb na przykładzie

![NLWeb](../../../translated_images/pl/nlweb-diagram.c1e2390b310e5fe4.webp)

Weźmy ponownie naszą stronę do rezerwacji podróży, tym razem napędzaną przez NLWeb.

1. **Ingestia danych**: Istniejące katalogi produktów na stronie podróży (np. wykazy lotów, opisy hoteli, pakiety wycieczek) są formatowane za pomocą Schema.org lub ładowane przez kanały RSS. Narzędzia NLWeb pobierają te dane strukturyzowane, tworzą embeddingi i przechowują je w lokalnej lub zdalnej bazie danych wektorów.

2. **Zapytanie w języku naturalnym (człowiek)**: Użytkownik odwiedza stronę i zamiast przeglądać menu, wpisuje w interfejs czatu: „Znajdź hotel przyjazny rodzinom w Honolulu z basenem na przyszły tydzień”.

3. **Przetwarzanie NLWeb**: Aplikacja NLWeb otrzymuje to zapytanie. Wysyła je do LLM, aby zrozumieć, i jednocześnie przeszukuje bazę danych wektorów w poszukiwaniu odpowiadających ofert hoteli.

4. **Dokładne wyniki**: LLM pomaga zinterpretować wyniki wyszukiwania, zidentyfikować najlepsze dopasowania według kryteriów „przyjazny rodzinom”, „basen” i „Honolulu”, a następnie formatuje odpowiedź w języku naturalnym. Co ważne, odpowiedź odnosi się do faktycznych hoteli z katalogu strony, unikając wymyślonych informacji.

5. **Interakcja agenta AI**: Ponieważ NLWeb działa jako serwer MCP, zewnętrzny agent podróży AI może również połączyć się z instancją NLWeb tej strony. Agent AI może wtedy użyć metody MCP `ask`, aby zapytać stronę bezpośrednio: `ask("Czy są jakieś restauracje przyjazne weganom w okolicy Honolulu polecane przez hotel?")`. Instancja NLWeb przetworzy to, korzystając z bazy danych informacji o restauracjach (jeśli są załadowane), i zwróci ustrukturyzowaną odpowiedź w formacie JSON.

### Masz więcej pytań o MCP/A2A/NLWeb?

Dołącz do [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), aby spotkać innych uczących się, uczestniczyć w godzinach konsultacji i uzyskać odpowiedzi na swoje pytania o agentach AI.

## Zasoby

- [MCP dla początkujących](https://aka.ms/mcp-for-beginners)  
- [Dokumentacja MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)  
- [Repozytorium NLWeb](https://github.com/nlweb-ai/NLWeb)  
- [Microsoft Agent Framework](https://aka.ms/ai-agents-beginners/agent-framewrok)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony przy użyciu automatycznej usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dążymy do dokładności, prosimy mieć na uwadze, że tłumaczenia automatyczne mogą zawierać błędy lub niedokładności. Oryginalny dokument w języku źródłowym należy traktować jako źródło wiążące. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za wszelkie nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->