# Korzystanie z protokołów agentowych (MCP, A2A i NLWeb)

[![Protokóły agentowe](../../../translated_images/pl/lesson-11-thumbnail.b6c742949cf1ce2a.webp)](https://youtu.be/X-Dh9R3Opn8)

> _(Kliknij powyższy obraz, aby obejrzeć wideo z tej lekcji)_

Wraz ze wzrostem użycia agentów AI rośnie potrzeba protokołów zapewniających standaryzację, bezpieczeństwo i wspierających otwartą innowację. W tej lekcji omówimy 3 protokoły, które mają sprostać temu zapotrzebowaniu - Model Context Protocol (MCP), Agent to Agent (A2A) oraz Natural Language Web (NLWeb).

## Wprowadzenie

W tej lekcji omówimy:

• Jak **MCP** pozwala agentom AI na dostęp do zewnętrznych narzędzi i danych w celu realizacji zadań użytkownika.

• Jak **A2A** umożliwia komunikację i współpracę między różnymi agentami AI.

• Jak **NLWeb** wprowadza interfejsy w naturalnym języku na dowolnej stronie internetowej, umożliwiając agentom AI odkrywanie i interakcję z jej treścią.

## Cele nauki

• **Zidentyfikować** główny cel i korzyści MCP, A2A i NLWeb w kontekście agentów AI.

• **Wyjaśnić**, jak każdy protokół ułatwia komunikację i interakcje między LLM, narzędziami i innymi agentami.

• **Rozpoznać** odrębne role, jakie każdy protokół pełni w budowaniu złożonych systemów agentowych.

## Model Context Protocol

**Model Context Protocol (MCP)** to otwarty standard, który zapewnia ustandaryzowany sposób, aby aplikacje mogły dostarczać kontekst i narzędzia do LLM. Pozwala to na stworzenie „uniwersalnego adaptera” do różnych źródeł danych i narzędzi, do których agenci AI mogą się w sposób spójny podłączać.

Przyjrzyjmy się komponentom MCP, korzyściom w porównaniu do bezpośredniego użycia API oraz przykładowi, jak agenci AI mogą korzystać z serwera MCP.

### Główne komponenty MCP

MCP działa na **architekturze klient-serwer**, a kluczowymi komponentami są:

• **Hosty** to aplikacje LLM (na przykład edytor kodu jak VSCode), które inicjują połączenia z serwerem MCP.

• **Klienci** to komponenty wewnątrz aplikacji hosta, które utrzymują połączenia jeden do jednego z serwerami.

• **Serwery** to lekkie programy udostępniające określone funkcje.

Protokół zawiera trzy podstawowe prymitywy, które określają możliwości serwera MCP:

• **Narzędzia**: Są to oddzielne akcje lub funkcje, które agent AI może wywołać, by wykonać zadanie. Na przykład serwis pogodowy może udostępniać narzędzie "pobierz pogodę", a serwer e-commerce - narzędzie "kup produkt". Serwery MCP reklamują nazwę, opis oraz schemat wejścia/wyjścia każdego narzędzia w swoim wykazie możliwości.

• **Zasoby**: To dane lub dokumenty tylko do odczytu, które serwer MCP może udostępniać, a klienci mogą pobierać na żądanie. Przykłady to zawartość plików, rekordy baz danych czy pliki logów. Zasoby mogą być tekstowe (np. kod lub JSON) lub binarne (np. obrazy czy PDF).

• **Podpowiedzi (Prompts)**: To zdefiniowane szablony zawierające sugerowane podpowiedzi, pozwalające na bardziej złożone przepływy pracy.

### Korzyści MCP

MCP oferuje znaczące zalety dla agentów AI:

• **Dynamiczne odkrywanie narzędzi**: Agenci mogą dynamicznie otrzymać listę dostępnych narzędzi z serwera wraz z opisami ich funkcji. W przeciwieństwie do tradycyjnych API, które często wymagają statycznego kodowania integracji, co oznacza, że każda zmiana API wymaga aktualizacji kodu, MCP pozwala "zintegrować raz", co zapewnia większą adaptacyjność.

• **Interoperacyjność między LLM**: MCP działa w różnych LLM, dając elastyczność zmiany podstawowych modeli w celu lepszego działania.

• **Standaryzowane bezpieczeństwo**: MCP zawiera standardową metodę uwierzytelniania, poprawiającą skalowalność przy dodawaniu dostępu do kolejnych serwerów MCP. Jest to prostsze niż zarządzanie różnymi kluczami i metodami uwierzytelniania dla różnych tradycyjnych API.

### Przykład MCP

![MCP Diagram](../../../translated_images/pl/mcp-diagram.e4ca1cbd551444a1.webp)

Wyobraźmy sobie, że użytkownik chce zarezerwować lot za pomocą asystenta AI opartego na MCP.

1. **Połączenie**: Asystent AI (klient MCP) łączy się z serwerem MCP dostarczonym przez linię lotniczą.

2. **Odkrywanie narzędzi**: Klient pyta serwera MCP linii lotniczej: „Jakie narzędzia są dostępne?” Serwer odpowiada narzędziami takimi jak "wyszukaj loty" i "zarezerwuj lot".

3. **Wywołanie narzędzia**: Następnie użytkownik mówi do asystenta AI: „Proszę, wyszukaj lot z Portland do Honolulu.” Asystent AI, korzystając ze swojego LLM, rozpoznaje, że musi wywołać narzędzie "wyszukaj loty" i przekazuje odpowiednie parametry (miejsce startu, miejsce docelowe) do serwera MCP.

4. **Wykonanie i odpowiedź**: Serwer MCP, działając jako pośrednik, wykonuje rzeczywiste wywołanie do wewnętrznego API rezerwacji linii lotniczej. Następnie otrzymuje informacje o locie (np. dane JSON) i przesyła je z powrotem do asystenta AI.

5. **Dalsza interakcja**: Asystent AI prezentuje opcje lotu. Po wybraniu lotu asystent może wywołać narzędzie "zarezerwuj lot" na tym samym serwerze MCP, kończąc rezerwację.

## Protokół Agent-to-Agent (A2A)

Podczas gdy MCP koncentruje się na łączeniu LLM z narzędziami, protokół **Agent-to-Agent (A2A)** idzie o krok dalej, umożliwiając komunikację i współpracę między różnymi agentami AI. A2A łączy agentów AI z różnych organizacji, środowisk i stosów technologicznych w celu wspólnego wykonania zadania.

Omówimy komponenty i korzyści A2A oraz przykład jego zastosowania w naszej aplikacji podróżniczej.

### Główne komponenty A2A

A2A skupia się na umożliwieniu komunikacji między agentami i na współpracy przy realizacji podzadań użytkownika. Każdy komponent protokołu przyczynia się do tego:

#### Karta Agenta

Podobnie jak serwer MCP udostępnia listę narzędzi, Karta Agenta zawiera:
- Nazwę Agenta.
- **Opis ogólnych zadań**, które realizuje.
- **Listę konkretnych umiejętności** z opisami, które pomagają innym agentom (lub nawet użytkownikom) zrozumieć, kiedy i dlaczego warto wywołać tego agenta.
- **Aktualny URL końcówki** agenta
- **Wersję** i **możliwości** agenta, takie jak streamowanie odpowiedzi i powiadomienia push.

#### Wykonawca Agenta

Wykonawca Agenta odpowiada za **przekazywanie kontekstu rozmowy użytkownika do zdalnego agenta**; zdalny agent potrzebuje tego, aby zrozumieć zadanie do wykonania. W serwerze A2A agent używa własnego modelu językowego (LLM) do parsowania nadchodzących żądań i wykonywania zadań przy użyciu własnych narzędzi wewnętrznych.

#### Artefakt

Po wykonaniu przez zdalnego agenta żądanego zadania powstaje produkt pracy w postaci artefaktu. Artefakt **zawiera rezultat pracy agenta**, **opis wykonanej czynności** oraz **kontekst tekstowy** przekazywany przez protokół. Po wysłaniu artefaktu połączenie ze zdalnym agentem zostaje zamknięte do następnego użycia.

#### Kolejka zdarzeń

Ten komponent służy do **obsługi aktualizacji i przesyłania wiadomości**. Jest szczególnie ważny w środowisku produkcyjnym systemów agentowych, aby zapobiec zamknięciu połączenia między agentami przed ukończeniem zadania, szczególnie gdy czas realizacji zadań bywa dłuższy.

### Korzyści A2A

• **Ulepszona współpraca**: Umożliwia agentom z różnych dostawców i platform interakcję, dzielenie się kontekstem i współpracę, co pozwala na płynną automatyzację w tradycyjnie rozłączonych systemach.

• **Elastyczność wyboru modelu**: Każdy agent A2A może wybrać, którego LLM używa do obsługi swoich żądań, pozwalając na optymalizację lub dostosowanie modeli dla każdego agenta, w przeciwieństwie do pojedynczego połączenia LLM w niektórych scenariuszach MCP.

• **Wbudowane uwierzytelnianie**: Uwierzytelnianie jest zintegrowane bezpośrednio z protokołem A2A, zapewniając solidne ramy bezpieczeństwa dla interakcji agentów.

### Przykład A2A

![A2A Diagram](../../../translated_images/pl/A2A-Diagram.8666928d648acc26.webp)

Rozbudujmy nasz scenariusz rezerwacji podróży, tym razem korzystając z A2A.

1. **Żądanie użytkownika do multi-agenta**: Użytkownik rozmawia z "Agentem Podróży" - klientem/agenta A2A, mówiąc na przykład: "Proszę, zarezerwuj całą wycieczkę do Honolulu na przyszły tydzień, w tym loty, hotel i wynajem samochodu".

2. **Orkiestracja przez Agenta Podróży**: Agent Podróży odbiera to złożone żądanie. Korzysta ze swojego LLM, by rozważyć zadanie i ustalić, że musi interagować z innymi wyspecjalizowanymi agentami.

3. **Komunikacja między agentami**: Agent Podróży wykorzystuje protokół A2A, aby połączyć się z agentami docelowymi, takimi jak "Agent Linii Lotniczej", "Agent Hotelowy" i "Agent Wynajmu Samochodów", którzy pochodzą z różnych firm.

4. **Delegowanie wykonania zadań**: Agent Podróży przesyła konkretne zadania wspomnianym agentom (np. "Znajdź loty do Honolulu", "Zarezerwuj hotel", "Wynajmij samochód"). Każdy z tych wyspecjalizowanych agentów, korzystając z własnych LLM i narzędzi (które mogą być serwerami MCP), wykonuje odpowiednią część rezerwacji.

5. **Skonsolidowana odpowiedź**: Gdy wszyscy agenci zakończą swoje zadania, Agent Podróży kompiluje wyniki (szczegóły lotu, potwierdzenie hotelu, rezerwacja samochodu) i przesyła kompleksową odpowiedź w stylu czatu do użytkownika.

## Natural Language Web (NLWeb)

Strony internetowe od dawna są podstawowym sposobem dostępu użytkowników do informacji i danych w Internecie.

Przyjrzyjmy się różnym komponentom NLWeb, jego zaletom oraz przykładowi działania, analizując naszą aplikację podróżniczą.

### Komponenty NLWeb

- **Aplikacja NLWeb (Kod kluczowej usługi)**: System przetwarzający pytania w naturalnym języku. Łączy różne części platformy, by tworzyć odpowiedzi. Można go uznać za **silnik obsługujący funkcje naturalnego języka** na stronie www.

- **Protokół NLWeb**: To **podstawowy zestaw reguł do interakcji w naturalnym języku** ze stroną internetową. Zwraca odpowiedzi w formacie JSON (często używając Schema.org). Jego celem jest stworzenie prostych podstaw dla „Webu AI”, podobnie jak HTML umożliwił udostępnianie dokumentów online.

- **Serwer MCP (punkt końcowy Model Context Protocol)**: Każda konfiguracja NLWeb działa również jako **serwer MCP**. Oznacza to, że może **udostępniać narzędzia (np. metodę „ask”) i dane** innym systemom AI. W praktyce pozwala to, aby zawartość i funkcje strony były dostępne dla agentów AI, umożliwiając stronie bycie częścią szerokiego „ekosystemu agentów”.

- **Modele osadzające (Embedding Models)**: Modele te służą do **zamiany treści strony w reprezentacje numeryczne zwane wektorami** (embeddingami). Wektory te oddają znaczenie w sposób, który komputery mogą porównywać i wyszukiwać. Przechowywane są w specjalnej bazie danych, a użytkownicy mogą wybrać, którego modelu embedding chcą używać.

- **Baza wektorowa (mechanizm wyszukiwania)**: Ta baza **przechowuje embeddingi zawartości strony**. Gdy ktoś zada pytanie, NLWeb przeszukuje bazę wektorową, by szybko odnaleźć najbardziej istotne informacje. Dostarcza szybką listę możliwych odpowiedzi, uszeregowanych wg podobieństwa. NLWeb działa z różnymi systemami przechowywania wektorów takimi jak Qdrant, Snowflake, Milvus, Azure AI Search i Elasticsearch.

### Przykład NLWeb

![NLWeb](../../../translated_images/pl/nlweb-diagram.c1e2390b310e5fe4.webp)

Rozważmy naszą stronę rezerwacji podróży, tym razem zasilaną przez NLWeb.

1. **Ingestia danych**: Istniejące katalogi produktów na stronie podróżniczej (np. listy lotów, opisy hoteli, pakiety wycieczek) są formatowane zgodnie ze Schema.org lub ładowane przez kanały RSS. Narzędzia NLWeb przetwarzają te dane strukturalne, tworzą embeddingi i przechowują je w lokalnej lub zdalnej bazie wektorowej.

2. **Zapytanie w naturalnym języku (człowiek)**: Użytkownik odwiedza stronę i zamiast nawigować po menu, wpisuje w interfejsie czatu: „Znajdź przyjazny rodzinom hotel w Honolulu z basenem na przyszły tydzień”.

3. **Przetwarzanie przez NLWeb**: Aplikacja NLWeb odbiera to zapytanie. Wysyła je do LLM w celu zrozumienia oraz jednocześnie przeszukuje swoją bazę wektorową, aby znaleźć odpowiednie oferty hotelowe.

4. **Dokładne wyniki**: LLM pomaga zinterpretować wyniki z bazy, identyfikuje najlepsze dopasowania według kryteriów "przyjazny rodzinom", "basen" oraz "Honolulu", a następnie formatuje odpowiedź w naturalnym języku. Co ważne, odpowiedź odnosi się do faktycznych hoteli z katalogu strony, unikając informacji fikcyjnych.

5. **Interakcja agenta AI**: Ponieważ NLWeb działa jako serwer MCP, zewnętrzny agent AI podróży może połączyć się z tym egzemplarzem NLWeb strony. Agent AI może wtedy użyć metody `ask` MCP, aby bezpośrednio zapytać stronę: `ask("Czy są polecane hotele z wegańską restauracją w okolicy Honolulu?")`. Instancja NLWeb przetwarza to, korzystając z bazy danych informacji o restauracjach (jeśli została załadowana) i zwraca ustrukturyzowaną odpowiedź JSON.

### Masz więcej pytań o MCP/A2A/NLWeb?

Dołącz do [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), aby spotkać innych uczących się, uczestniczyć w godzinach konsultacji i uzyskać odpowiedzi na pytania dotyczące agentów AI.

## Zasoby

- [MCP dla początkujących](https://aka.ms/mcp-for-beginners)  
- [Dokumentacja MCP](https://learn.microsoft.com/python/api/overview/azure/ai-projects-readme)
- [Repozytorium NLWeb](https://github.com/nlweb-ai/NLWeb)
- [Microsoft Agent Framework](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python)

## Poprzednia lekcja

[AI Agents w produkcji](../10-ai-agents-production/README.md)

## Następna lekcja

[Inżynieria kontekstu dla agentów AI](../12-context-engineering/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->