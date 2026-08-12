# Inżynieria kontekstu dla agentów AI

[![Inżynieria kontekstu](../../../translated_images/pl/lesson-12-thumbnail.ed19c94463e774d4.webp)](https://youtu.be/F5zqRV7gEag)

> _(Kliknij powyższy obraz, aby obejrzeć wideo z tej lekcji)_

Zrozumienie złożoności aplikacji, dla której budujesz agenta AI, jest ważne dla stworzenia niezawodnego agenta. Musimy tworzyć agentów AI, którzy skutecznie zarządzają informacjami, aby sprostać złożonym potrzebom wykraczającym poza inżynierię promptów.

W tej lekcji przyjrzymy się, czym jest inżynieria kontekstu i jaką pełni rolę w budowaniu agentów AI.

## Wprowadzenie

Ta lekcja obejmuje:

• **Czym jest inżynieria kontekstu** i dlaczego różni się od inżynierii promptów.

• **Strategie skutecznej inżynierii kontekstu**, w tym jak pisać, wybierać, kompresować i izolować informacje.

• **Typowe błędy kontekstu**, które mogą zakończyć działanie twojego agenta AI i jak je naprawić.

## Cele nauki

Po ukończeniu tej lekcji będziesz rozumieć, jak:

• **Zdefiniować inżynierię kontekstu** i odróżnić ją od inżynierii promptów.

• **Zidentyfikować kluczowe składniki kontekstu** w aplikacjach z wykorzystaniem dużych modeli językowych (LLM).

• **Stosować strategie pisania, wybierania, kompresji i izolowania kontekstu**, aby poprawić wydajność agenta.

• **Rozpoznawać typowe błędy kontekstu**, takie jak zatruwanie, rozpraszanie, zamieszanie i konflikt, oraz stosować techniki łagodzenia ich skutków.

## Czym jest inżynieria kontekstu?

Dla agentów AI kontekst to element, który napędza planowanie agenta do podejmowania określonych działań. Inżynieria kontekstu to praktyka zapewniania, że agent AI ma właściwe informacje do wykonania kolejnego kroku zadania. Okno kontekstowe jest ograniczone rozmiarem, dlatego jako twórcy agentów musimy budować systemy i procesy zarządzające dodawaniem, usuwaniem i kondensowaniem informacji w oknie kontekstu.

### Inżynieria promptów a inżynieria kontekstu

Inżynieria promptów koncentruje się na jednym zestawie statycznych instrukcji, które skutecznie kierują agentami AI za pomocą zasad. Inżynieria kontekstu to zarządzanie dynamicznym zestawem informacji, w tym początkowym promptem, aby zapewnić agentowi to, czego potrzebuje w czasie. Główną ideą inżynierii kontekstu jest uczynienie tego procesu powtarzalnym i niezawodnym.

### Rodzaje kontekstu

[![Rodzaje kontekstu](../../../translated_images/pl/context-types.fc10b8927ee43f06.webp)](https://youtu.be/F5zqRV7gEag)

Ważne jest, aby pamiętać, że kontekst to nie tylko jedna rzecz. Informacje, których agent AI potrzebuje, mogą pochodzić z różnych źródeł i od nas zależy, aby agent miał do nich dostęp:

Rodzaje kontekstu, które agent AI może potrzebować zarządzać, obejmują:

• **Instrukcje:** To jak „zasady” agenta – promptów, komunikatów systemowych, przykładów few-shot (pokazujących AI jak coś robić) i opisów dostępnych narzędzi. To tutaj łączy się inżynieria promptów z inżynierią kontekstu.

• **Wiedza:** Obejmuje fakty, informacje pobrane z baz danych lub pamięć długoterminową agenta. To również integracja systemu Retrieval Augmented Generation (RAG), jeśli agent potrzebuje dostępu do różnych zasobów wiedzy i baz danych.

• **Narzędzia:** To definicje zewnętrznych funkcji, API i serwerów MCP, które agent może wywoływać, wraz z informacją zwrotną (wynikami) z ich użycia.

• **Historia konwersacji:** Trwający dialog z użytkownikiem. Z upływem czasu rozmowy stają się dłuższe i bardziej złożone, co zajmuje miejsce w oknie kontekstu.

• **Preferencje użytkownika:** Informacje zdobyte o upodobaniach lub niechęciach użytkownika z czasem. Mogą być przechowywane i używane przy podejmowaniu kluczowych decyzji, aby wspierać użytkownika.

## Strategie skutecznej inżynierii kontekstu

### Strategie planowania

[![Najlepsze praktyki inżynierii kontekstu](../../../translated_images/pl/best-practices.f4170873dc554f58.webp)](https://youtu.be/F5zqRV7gEag)

Dobra inżynieria kontekstu zaczyna się od dobrego planowania. Oto podejście, które pomoże ci zacząć myśleć o stosowaniu koncepcji inżynierii kontekstu:

1. **Zdefiniuj jasne rezultaty** – wyniki zadań przydzielonych agentom AI powinny być jasno określone. Odpowiedz na pytanie – „Jak będzie wyglądał świat, gdy agent AI zakończy swoje zadanie?” Innymi słowy, jaka zmiana, informacja lub odpowiedź powinna być dostępna dla użytkownika po interakcji z agentem AI.
2. **Zmapuj kontekst** – po zdefiniowaniu rezultatów agenta AI musisz odpowiedzieć na pytanie „Jakich informacji agent potrzebuje, aby wykonać to zadanie?”. W ten sposób możesz zacząć mapować, gdzie te informacje można znaleźć.
3. **Utwórz pipeline'y kontekstu** – teraz, gdy wiesz gdzie są informacje, musisz odpowiedzieć na pytanie „Jak agent zdobędzie te informacje?”. Można to zrobić na różne sposoby, w tym za pomocą RAG, użycia serwerów MCP i innych narzędzi.

### Strategie praktyczne

Planowanie jest ważne, ale gdy informacje zaczynają napływać do okna kontekstu agenta, potrzebujemy praktycznych strategii do ich zarządzania:

#### Zarządzanie kontekstem

Choć część informacji będzie dodawana do okna kontekstu automatycznie, inżynieria kontekstu polega na bardziej aktywnym zarządzaniu tymi danymi, co można osiągnąć kilkoma strategiami:

 1. **Notatnik agenta (Agent Scratchpad)**
 Umożliwia agentowi AI notowanie istotnych informacji o bieżących zadaniach i interakcjach z użytkownikiem podczas jednej sesji. Powinien istnieć poza oknem kontekstu w pliku lub obiekcie w czasie działania, który agent może później przywołać podczas sesji, jeśli zajdzie taka potrzeba.

 2. **Wspomnienia (Memories)**
 Notatniki są dobre do zarządzania informacjami poza oknem kontekstu w pojedynczej sesji. Wspomnienia pozwalają agentom przechowywać i odzyskiwać istotne informacje w wielu sesjach. Mogą to być podsumowania, preferencje użytkownika i opinie na przyszłość.

 3. **Kompresja kontekstu**
  Gdy okno kontekstu rośnie i zbliża się do limitu, można stosować techniki takie jak streszczanie i przycinanie. Obejmuje to albo pozostawienie tylko najbardziej istotnych informacji, albo usuwanie starszych wiadomości.
  
 4. **Systemy wieloagentowe (Multi-Agent Systems)**
  Tworzenie systemu wieloagentowego to forma inżynierii kontekstu, ponieważ każdy agent ma własne okno kontekstu. To, jak ten kontekst jest udostępniany i przekazywany różnym agentom, to kolejny element do zaplanowania podczas budowy takich systemów.
  
 5. **Środowiska piaskownicy (Sandbox Environments)**
  Jeśli agent musi wykonać jakiś kod lub przetworzyć dużą ilość informacji w dokumencie, może to wymagać dużej liczby tokenów, aby przetworzyć wyniki. Zamiast przechowywać to wszystko w oknie kontekstu, agent może użyć środowiska piaskownicy, które jest w stanie wykonać ten kod i odczytać tylko wyniki oraz inne istotne informacje.
  
 6. **Obiekty stanu w czasie działania (Runtime State Objects)**
   Polega to na tworzeniu pojemników informacji do zarządzania sytuacjami, gdy agent potrzebuje dostępu do określonych informacji. Dla złożonego zadania umożliwi to agentowi przechowywanie wyników każdego podzadania krok po kroku, pozwalając kontekstowi pozostać powiązanym wyłącznie z tym konkretnym podzadaniem.

#### Inspekcja kontekstu

Po zastosowaniu jednej z tych strategii warto sprawdzić, co rzeczywiście otrzymało następne wywołanie modelu. Przydatnym pytaniem debugującym jest:

> Czy agent załadował za dużo kontekstu, niewłaściwy kontekst, czy brakowało mu potrzebnego kontekstu?

Nie musisz logować surowych promptów, wyników narzędzi czy zawartości pamięci, aby odpowiedzieć na to pytanie. W produkcji preferuj małe zapisy inspekcji kontekstu, które zawierają liczby, identyfikatory, hashe i oznaczenia polityk:

- **Wybór:** Śledź, ile kandydatów na fragmenty, narzędzi lub pamięci rozważano, ile wybrano oraz jaka reguła lub ocena spowodowała odfiltrowanie pozostałych.
- **Kompresja:** Zanotuj zakres źródłowy lub identyfikator śledzenia, identyfikator podsumowania, szacunkową liczbę tokenów przed i po kompresji oraz czy surowa zawartość została wykluczona z następnego wywołania.
- **Izolacja:** Zanotuj, które podzadanie było wykonywane w oddzielnym agencie, sesji lub piaskownicy, jakie było zwrócone ograniczone podsumowanie i czy duże wyniki narzędzi pozostały poza kontekstem agenta nadrzędnego.
- **Pamięć i RAG:** Przechowuj identyfikatory dokumentów wyszukiwania, identyfikatory pamięci, oceny, wybrane identyfikatory i status redakcji zamiast pełnego pobranego tekstu.
- **Bezpieczeństwo i prywatność:** Preferuj hashe, identyfikatory, pojemniki tokenów i oznaczenia polityk zamiast wrażliwych tekstów promptu, argumentów narzędzi, wyników narzędzi lub ciał pamięci użytkownika.

Celem nie jest przechowywanie więcej kontekstu. Chodzi o pozostawienie wystarczających dowodów, aby deweloper mógł powiedzieć, która strategia kontekstowa działała i czy zmieniła następne wywołanie modelu w zamierzony sposób.

### Przykład inżynierii kontekstu

Załóżmy, że chcemy, aby agent AI **„Zarezerwował mi podróż do Paryża.”**

• Prosty agent używający tylko inżynierii promptów może po prostu odpowiedzieć: **„Dobrze, kiedy chciałbyś jechać do Paryża?”**. Przetworzył tylko bezpośrednie pytanie użytkownika w momencie jego zadania.

• Agent stosujący strategie inżynierii kontekstu omówione powyżej zrobiłby znacznie więcej. Zanim w ogóle odpowie, jego system mógłby:

  ◦ **Sprawdzić twój kalendarz** pod kątem dostępnych terminów (pobierając dane w czasie rzeczywistym).

 ◦ **Przypomnieć sobie wcześniejsze preferencje podróży** (z pamięci długoterminowej) takie jak preferowane linie lotnicze, budżet lub czy wolisz loty bezpośrednie.

 ◦ **Zidentyfikować dostępne narzędzia** do rezerwacji lotów i hoteli.

- Następnie przykładowa odpowiedź mogłaby brzmieć: „Cześć [Twoje Imię]! Widzę, że jesteś wolny w pierwszym tygodniu października. Czy mam szukać lotów bezpośrednich do Paryża na [Preferowanych Liniach Lotniczych] w twoim zwykłym budżecie [Budżet]?” Ta bogatsza, świadoma kontekstu odpowiedź pokazuje moc inżynierii kontekstu.

## Typowe błędy kontekstu

### Zatruwanie kontekstu

**Co to jest:** Gdy halucynacja (fałszywa informacja wygenerowana przez LLM) lub błąd pojawia się w kontekście i jest powtarzalnie wykorzystywana, powodując, że agent dąży do niemożliwych celów lub tworzy nonsensowne strategie.

**Co zrobić:** Wdrożyć **walidację kontekstu** i **kwarantannę**. Weryfikuj informacje zanim zostaną dodane do pamięci długoterminowej. Jeśli wykryje się potencjalne zatruwanie, rozpocznij nowe wątki kontekstowe, aby zapobiec rozprzestrzenianiu się złych informacji.

**Przykład rezerwacji podróży:** Twój agent halucynuje **lot bezpośredni z małego lokalnego lotniska do odległego miasta międzynarodowego**, które faktycznie nie obsługuje lotów międzynarodowych. Ten nieistniejący szczegół lotu zostaje zapisany w kontekście. Później, gdy prosisz agenta o rezerwację, cały czas próbuje znaleźć bilety na tę niemożliwą trasę, prowadząc do powtarzalnych błędów.

**Rozwiązanie:** Wprowadź krok, który **weryfikuje istnienie lotu i trasy za pomocą API w czasie rzeczywistym** _przed_ dodaniem szczegółów lotu do aktywnego kontekstu agenta. Jeśli walidacja zawiedzie, błędna informacja jest „kwarantannowana” i nie jest dalej używana.

### Rozpraszanie kontekstu

**Co to jest:** Gdy kontekst staje się tak duży, że model skupia się zbytnio na zgromadzonej historii zamiast wykorzystać to, czego nauczył się podczas treningu, prowadząc do powtarzających się lub nieprzydatnych działań. Modele mogą zaczynać popełniać błędy nawet zanim okno kontekstu się zapełni.

**Co zrobić:** Użyj **streszczania kontekstu**. Okresowo kompresuj zgromadzone informacje do krótszych podsumowań, zachowując ważne szczegóły, usuwając jednocześnie zbędną historię. Pomaga to „zresetować” skupienie.

**Przykład rezerwacji podróży:** Rozmawiałeś długo o różnych wymarzonych miejscach podróży, w tym szczegółowo opisywałeś swoją wyprawę z plecakiem sprzed dwóch lat. Gdy w końcu prosisz o **„znajdź tani lot na następny miesiąc”**, agent utknął na starych, nieistotnych szczegółach i ciągle pyta o twój ekwipunek czy dawne plany podróży, ignorując obecne zapytanie.

**Rozwiązanie:** Po określonej liczbie wymian lub gdy kontekst staje się zbyt duży, agent powinien **zestawić podsumowanie najnowszych i najbardziej istotnych części rozmowy** – koncentrując się na obecnych datach podróży i celu – i użyć tego skróconego podsumowania do następnego wywołania LLM, odrzucając mniej istotną historyczną rozmowę.

### Zamieszanie kontekstu

**Co to jest:** Gdy niepotrzebny kontekst, często w postaci zbyt wielu dostępnych narzędzi, powoduje, że model generuje złe odpowiedzi lub wywołuje nieodpowiednie narzędzia. Mniejsze modele są na to szczególnie podatne.

**Co zrobić:** Wprowadź **zarządzanie zestawem narzędzi** za pomocą technik RAG. Przechowuj opisy narzędzi w bazie wektorowej i wybieraj _tylko_ najbardziej odpowiednie narzędzia dla konkretnego zadania. Badania pokazują, że ograniczenie wyboru do mniej niż 30 jest efektywne.

**Przykład rezerwacji podróży:** Twój agent ma dostęp do dziesiątek narzędzi: `book_flight`, `book_hotel`, `rent_car`, `find_tours`, `currency_converter`, `weather_forecast`, `restaurant_reservations` itd. Pytasz: **„Jaki jest najlepszy sposób poruszania się po Paryżu?”** Z powodu ogromnej liczby narzędzi agent się myli i próbuje wywołać `book_flight` _w Paryżu_ albo `rent_car`, mimo, że wolisz transport publiczny, ponieważ opisy narzędzi mogą się nakładać lub po prostu nie potrafi wybrać najlepszego.

**Rozwiązanie:** Użyj **RAG na opisach narzędzi**. Gdy pytasz o poruszanie się po Paryżu, system dynamicznie dobiera _tylko_ najbardziej odpowiednie narzędzia, takie jak `rent_car` czy `public_transport_info` na podstawie zapytania, prezentując LLM skoncentrowany „zestaw narzędzi”.

### Konflikt kontekstu

**Co to jest:** Gdy w kontekście istnieją sprzeczne informacje, co prowadzi do niespójnego rozumowania lub złych ostatecznych odpowiedzi. Często dzieje się tak, gdy informacje przychodzą etapami, a wczesne, błędne założenia pozostają w kontekście.

**Co zrobić:** Stosuj **przycinanie kontekstu** i **odciążanie**. Przycinanie oznacza usuwanie przestarzałych lub sprzecznych informacji, gdy napływają nowe dane. Odciążanie daje modelowi osobne miejsce robocze („notatnik”), gdzie może przetwarzać informacje bez zaśmiecania głównego kontekstu.


**Przykład rezerwacji podróży:** Początkowo mówisz swojemu agentowi: **„Chcę lecieć klasą ekonomiczną.”** Później w rozmowie zmieniasz zdanie i mówisz: **„Właściwie na tę podróż wybierzmy klasę biznesową.”** Jeśli obie instrukcje pozostaną w kontekście, agent może otrzymać sprzeczne wyniki wyszukiwania lub mieć problem z ustaleniem, którą preferencję należy priorytetowo traktować.

**Rozwiązanie:** Wprowadź **przycinanie kontekstu**. Kiedy nowa instrukcja jest sprzeczna ze starą, starsza instrukcja jest usuwana lub wyraźnie nadpisywana w kontekście. Alternatywnie agent może użyć **notatnika roboczego**, by pogodzić sprzeczne preferencje przed podjęciem decyzji, zapewniając, że tylko ostateczna, spójna instrukcja kieruje jego działaniami.

## Masz więcej pytań dotyczących inżynierii kontekstu?

Dołącz do [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), aby spotkać się z innymi uczącymi się, uczestniczyć w godzinach konsultacji i uzyskać odpowiedzi na pytania dotyczące AI Agentów.
## Poprzednia lekcja

[Protokoły agentowe](../11-agentic-protocols/README.md)

## Następna lekcja

[Pamięć dla AI Agentów](../13-agent-memory/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->