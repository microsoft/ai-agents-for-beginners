# Agent AI dla początkujących - przewodnik do nauki

Używaj tego przewodnika jako praktycznego towarzysza podczas przechodzenia przez kurs. Nie jest on
przeznaczony do zastąpienia lekcji. Pomaga zdecydować, od czego zacząć, na co zwrócić
uwagę w każdej lekcji oraz jak połączyć pomysły w mały działający demo agenta.


Jeśli jesteś tu po raz pierwszy, zacznij prosto:

1. Przeczytaj [Course Setup](./00-course-setup/README.md).
2. Ukończ lekcje 01-06 w kolejności.
3. Miej na uwadze jeden mały pomysł na demo podczas nauki.
4. Po każdej lekcji zapytaj: „Co mój agent potrafi teraz, czego wcześniej nie potrafił?”


## Proste demo do zapamiętania

Dobrym sposobem nauki agentów jest śledzenie jednego pomysłu na demo przez cały kurs.

Przykładowe demo: **agent pomocnik kursu**.

Użytkownik pyta:

> „Chcę się nauczyć, jak agenci wykorzystują narzędzia. Znajdź właściwe lekcje, podsumuj co
> powinienem przeczytać najpierw i daj mi krótkie zadanie do praktyki.”

Zwykły chatbot odpowiada na podstawie tego, co już wie. Agent potrafi więcej:

1. **Czyta lub wyszukuje pliki kursu**, aby znaleźć odpowiednie lekcje.
2. **Używa narzędzi** do pobierania linków do lekcji, przykładów lub materiałów pomocniczych.
3. **Planuje** krótki plan nauki zamiast dawać jedną długą odpowiedź.
4. **Wykorzystuje kontekst** z bieżącej rozmowy, aby skupić się na celu ucznia.
5. **Pamięta przydatne preferencje**, jeśli aplikacja obsługuje pamięć.
6. **Pokazuje ślady, cytaty lub logi**, aby użytkownik mógł zrozumieć, co się wydarzyło.
7. **Stosuje zabezpieczenia** przed podejmowaniem ryzykownych działań lub używaniem danych wrażliwych.


dodałaby ta lekcja?


## Do czego zmierzasz

Pod koniec kursu powinieneś być w stanie wyjaśnić i zbudować systemy agentów,
które łączą te części:

| Część | Znaczenie w prostych słowach | W demo |
|------|-----------------------------|---------|
| Model | Silnik rozumowania, który interpretuje zapytanie użytkownika | Rozumie, że uczeń chce lekcje o użyciu narzędzi |
| Narzędzia | Funkcje, API, pliki, przeglądarki lub usługi, których agent może używać | Przeszukuje repozytorium lub pobiera treść lekcji |
| Wiedza | Dokumenty lub dane używane do ugruntowania odpowiedzi | Pliki README kursu i materiały lekcyjne |
| Kontekst | Informacje przekazane w kolejnym wywołaniu modelu | Cel użytkownika i wyniki narzędzi |
| Pamięć | Informacje zapamiętane do późniejszego użycia | Uczeń preferuje praktyczne przykłady Pythona |
| Planowanie | Podział większego celu na mniejsze kroki | Znajduje lekcje, podsumowuje, sugeruje zadanie praktyczne |
| Orkiestracja | Kierowanie pracą między narzędziami, krokami lub agentami | Planista wywołuje narzędzie wyszukiwania, potem podsumowującego |
| Zaufanie | Bezpieczeństwo, ocena i obserwowalność | Loguje wywołania narzędzi i pyta przed działaniami wysokiego ryzyka |

## Modele i dostawcy

Przykłady kodu z kursu używają **Microsoft Agent Framework (MAF)** i celują w **Azure OpenAI Responses API** — zalecane API na przyszłość, które łączy czaty, wywoływanie narzędzi, multimodalne wejścia i rozmowy ze stanem w jednym interfejsie. Możesz połączyć się przez projekt **Microsoft Foundry** (z `FoundryChatClient`) lub bezpośrednio do Azure OpenAI (z `OpenAIChatClient`).

Podczas pracy z lekcjami masz kilka opcji dostawców:

- **Microsoft Foundry / Azure OpenAI (Responses API)** — główna ścieżka używana w lekcjach. Zaloguj się przez `az login` dla uwierzytelniania Entra ID bez klucza.
- **Foundry Local** — uruchom modele całkowicie na urządzeniu przez zgodne API OpenAI (bez chmury, bez kluczy API). Idealne do eksperymentów offline lub bezkosztowych. Zobacz [Course Setup](./00-course-setup/README.md).
- **MiniMax** — kompatybilny dostawca OpenAI z modelami dużego kontekstu, możliwy jako zamiennik "plug-and-play".

> **Nota:** GitHub Models jest przestarzały (przestanie działać w lipcu 2026) i nie obsługuje Responses API. Przykłady zostały zaktualizowane, aby używać Azure OpenAI / Microsoft Foundry.

## Wybierz swoją ścieżkę nauki

Możesz przejść cały kurs w kolejności lub wybrać ścieżkę na podstawie tego, co chcesz zbudować.


| Jeśli Twoim celem jest... | Zacznij od | Następnie ucz się |
|-------------------------|------------|--------------|
| Zrozumieć, czym są agenci | 01, 02, 03 | 04, 05, 06 |
| Zbudować agenta używającego narzędzi | 04 | 05, 07, 14 |
| Zbudować agenta RAG | 05 | 04, 06, 12 |
| Projektować wieloetapowe przepływy pracy | 07 | 08, 09, 14 |
| Zrozumieć systemy multi-agentowe | 08 | 07, 09, 11 |
| Przygotować agentów do produkcji | 06, 10 | 12, 13, 16, 18 |
| Wdrożyć i skalować agentów na Foundry | 10, 16 | 06, 13, 18 |
| Zbudować agentów lokalnych / offline-first | 17 | 04, 05, 11 |
| Poznać protokoły i automatyzację w przeglądarce | 11, 15 | 10, 18 |

Wskazówka: jeśli jesteś nowy w agentach, nie pomijaj lekcji 01-06. Dostarczają
słownictwa potrzebnego na resztę kursu.

## Przewodnik lekcja po lekcji

| Lekcja | Czego się uczysz | Spróbuj po lekcji |
|--------|-----------------|------------------|
| [01 - Wprowadzenie do agentów AI](./01-intro-to-ai-agents/README.md) | Co odróżnia agenta od podstawowego chatbota. | Wyjaśnij pomysł swojego demo jako agenta, nie tylko aplikacji czatu. |
| [02 - Agentic Frameworks](./02-explore-agentic-frameworks/README.md) | Jak frameworki pomagają z modelami, narzędziami, stanem i przepływami pracy. | Zidentyfikuj, które części twojego demo zarządzałby framework. |
| [03 - Agentic Design Patterns](./03-agentic-design-patterns/README.md) | Typowe wzorce projektowe dla zachowania agentów. | Nakreśl podróż użytkownika przed napisaniem kodu. |
| [04 - Wykorzystanie narzędzi](./04-tool-use/README.md) | Jak agenci wywołują narzędzia, by uzyskać dane lub podjąć działanie. | Zdefiniuj jedno narzędzie, którego potrzebowałby twój agent demo. |
| [05 - Agentic RAG](./05-agentic-rag/README.md) | Jak wyszukiwanie opiera odpowiedzi agenta na dokumentach lub danych. | Zdecyduj, jakie źródło wiedzy twoje demo powinno przeszukiwać. |
| [06 - Zaufani agenci](./06-building-trustworthy-agents/README.md) | Jak dodać zabezpieczenia, nadzór i bezpieczne zachowanie. | Dodaj jedną regułę, gdy agent powinien najpierw zapytać użytkownika. |
| [07 - Projektowanie planowania](./07-planning-design/README.md) | Jak agenci dzielą większe cele na mniejsze kroki. | Napisz trzyetapowy plan dla swojego zapytania demo. |
| [08 - Projektowanie multi-agentowe](./08-multi-agent/README.md) | Kiedy rozdzielić pracę między specjalistycznych agentów. | Zdecyduj, czy twoje demo potrzebuje jednego agenta czy kilku. |
| [09 - Metapoznanie](./09-metacognition/README.md) | Jak agenci mogą przeglądać i poprawiać własne wyniki. | Dodaj ostateczną kontrolę przed odpowiedzią agenta. |
| [10 - Agenci AI w produkcji](./10-ai-agents-production/README.md) | Co się zmienia, gdy agent przechodzi z demo do produkcji. | Wymień, co byś monitorował: jakość, koszt, opóźnienia, błędy. |
| [11 - Protokoły agentowe](./11-agentic-protocols/README.md) | Jak protokoły łączą agentów z narzędziami i innymi agentami. | Zidentyfikuj, gdzie standardowy protokół mógłby uprościć integrację. |
| [12 - Inżynieria kontekstu](./12-context-engineering/README.md) | Jak wybierać, przycinać, izolować i zarządzać kontekstem. | Zdecyduj, co należy uwzględnić w prompt, a co wykluczyć. |
| [13 - Pamięć agenta](./13-agent-memory/README.md) | Jak agenci mogą zapisywać przydatne informacje między interakcjami. | Wybierz jedną bezpieczną preferencję, którą twoje demo mogłoby zapamiętać. |
| [14 - Microsoft Agent Framework](./14-microsoft-agent-framework/README.md) | Elementy frameworka do budowania agentów i przepływów, oraz hostowanie agentów LangChain/LangGraph na Microsoft Foundry. | Przyporządkuj kroki swojego demo do koncepcji frameworka. |
| [15 - Agenci używający komputera](./15-browser-use/README.md) | Jak agenci mogą wchodzić w interakcję z przeglądarką lub UI, na przykład Microsoft Project Opal. | Wybierz jedno zadanie przeglądarki, które wciąż powinno wymagać potwierdzenia użytkownika. |
| [16 - Wdrażanie skalowalnych agentów](./16-deploying-scalable-agents/README.md) | Jak przenieść agenta z prototypu do skalowalnego, obserwowalnego wdrożenia produkcyjnego na Microsoft Foundry (hostowanie agentów, routing modeli, cache, bramki oceny, testy dymne). | Wymień kwestie produkcyjne, które twoje demo wciąż potrzebuje: hostowanie, routing, koszt, ocena. |
| [17 - Tworzenie lokalnych agentów AI](./17-creating-local-ai-agents/README.md) | Jak budować agentów lokalnych, którzy działają całkowicie na twoim komputerze z Foundry Local i Qwen (lokalne narzędzia, lokalny RAG, lokalny MCP). | Zdecyduj, które części twojego demo powinny pozostać prywatne i działać lokalnie. |
| [18 - Zabezpieczanie agentów AI](./18-securing-ai-agents/README.md) | Jak uczynić działania agenta bardziej audytowalne i odporne na manipulacje. | Zdecyduj, które działania w twoim demo powinny być logowane lub potwierdzane. |

## Weryfikacja wdrożonych agentów testami dymnymi

Gdy wdrażasz agenta (lekcja 16), **test dymny** to najtańsze pierwsze
sprawdzenie, czy wdrożenie faktycznie odpowiada. To repozytorium zawiera gotowe do uruchomienia
katalogi w [tests/](./tests/README.md) dla wdrażanych agentów z lekcji 01, 04, 05 i 16, podłączone do
[AI Smoke Test](https://github.com/marketplace/actions/ai-smoke-test) GitHub
Action. Uruchom je z zakładki **Actions** po wdrożeniu agenta lekcji.
Testy dymne to pierwsza brama — oceny offline i online (lekcje 10 i 16)
mówią, jak *dobry* jest agent.






ma jasną nazwę, wąskie zadanie, typowane wejścia, przewidywalny wynik i bezpieczny sposób
na obsługę błędów.


Dla demo pomocnika kursu narzędzia mogą być:

- `search_lessons(query)`
- `read_lesson(path)`
- `create_practice_task(topic)`

### RAG i wiedza

RAG pomaga agentowi odpowiadać na podstawie źródłowych materiałów zamiast zgadywać. W
tym kursie źródłem mogą być pliki README lekcji, przykłady kodu lub zewnętrzne
zasoby powiązane z lekcjami.

Używaj RAG, gdy odpowiedź powinna opierać się na dokumentach, danych lub aktualnych
plikach projektu.

### Planowanie

Planowanie jest przydatne, gdy zapytanie ma kilka kroków. Plany trzymaj krótkie i
wystarczająco przejrzyste, by programista lub użytkownik mogli je sprawdzić.

Dla demo plan może wyglądać tak:

1. Znajdź lekcje związane z używaniem narzędzi.
2. Podsumuj najbardziej istotne lekcje.
3. Zaproponuj jedno zadanie praktyczne.

### Kontekst

Kontekst to, co model widzi teraz. Za mało kontekstu może spowodować, że agent
przegapi ważne detale. Za dużo kontekstu może sprawić, że agent będzie wolniejszy, droższy,
lub łatwiej się pomyli.

Dobra inżynieria kontekstu oznacza wybór odpowiednich informacji do kolejnego wywołania modelu.




tylko wtedy, gdy są użyteczne, bezpieczne i łatwe do aktualizacji lub usunięcia.


Na przykład, zapamiętanie, że „uczeń woli przykłady Pythona” może się przydać.
Zapamiętywanie wrażliwych danych osobowych zazwyczaj nie jest wskazane.

### Ocena i obserwowalność

Ocena pyta: czy agent zrobił to, co powinien?

Obserwowalność pyta: czy możemy zobaczyć, jak to się stało?

Dla agentów produkcyjnych monitoruj wywołania modeli, narzędzi, pobrany kontekst,
opóźnienia, koszty, błędy oraz opinie użytkowników.

### Zaufanie i bezpieczeństwo

Godni zaufania agenci potrzebują więcej niż pomocnego promptu. Korzystaj z narzędzi o
minimalnych uprawnieniach, zatwierdzania przez człowieka dla działań o dużym wpływie, redakcji danych, gdy trzeba, oraz logów lub
potwierdzeń dla działań podlegających audytowi.

## 15-minutowa rutyna przeglądu

Używaj tej rutyny po każdej lekcji:

1. **Podsumuj lekcję jednym zdaniem.**
2. **Nazwij nową zdolność agenta.** Na przykład: użycie narzędzi, retrieval,
   planowanie, pamięć, obserwowalność lub bezpieczeństwo.
3. **Dodaj ją do demo pomocnika kursu.** Co się zmienia w demo teraz?
4. **Znajdź ryzyko.** Co mogłoby pójść nie tak, gdyby zdolność była nadużywana?
5. **Napisz jedno pytanie testowe.** Jak byś sprawdził, czy agent zachowuje się dobrze?

## Szybki auto-test

Zanim przejdziesz dalej, spróbuj odpowiedzieć na te pytania:

1. Co agent potrafi zrobić, czego zwykły chatbot sam nie potrafi?
2. Jakiego narzędzia twój agent potrzebowałby najpierw i dlaczego?
3. Jakie źródło wiedzy powinno stanowić podstawę odpowiedzi agenta?
4. Jaki kontekst należy zawrzeć w kolejnym wywołaniu modelu?
5. Co agent powinien zapamiętać, a czego unikać przechowywania?
6. Kiedy agent powinien prosić o zatwierdzenie przez człowieka?
7. Jakie logi, ślady lub potwierdzenia pozwoliłyby ci później debugować lub audytować agenta?


## Proponowane zadanie finałowe

Na koniec kursu stwórz małego agenta, który pomoże uczącemu się nawigować po tym
repozytorium.

Wersja podstawowa:

- Przyjmij temat od użytkownika.
- Znajdź najbardziej odpowiednie lekcje.
- Podsumuj, co należy przeczytać najpierw.
- Zaproponuj jedno praktyczne zadanie.
- Pokaż, które pliki lekcji lub linki zostały użyte.

Wersja rozszerzona:

- Zapamiętaj preferowany język programowania uczącego się.
- Użyj prostego planu przed odpowiedzią.
- Dodaj krok samosprawdzenia przed ostateczną odpowiedzią.
- Rejestruj wywołania narzędzi i pobrane źródła.
- Poproś o potwierdzenie przed otwarciem przeglądarki lub uruchomieniem automatyzacji UI.

To daje mały, ale realistyczny sposób na ćwiczenie narzędzi, RAG, planowania,
kontekstu, pamięci, obserwowalności i zaufania w jednym projekcie.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->