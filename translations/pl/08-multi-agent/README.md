[![Multi-Agent Design](../../../translated_images/pl/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Kliknij obraz powyżej, aby obejrzeć film z tej lekcji)_

# Wzorce projektowe wieloagentowe

Gdy tylko zaczniesz pracować nad projektem, który obejmuje wielu agentów, będziesz musiał rozważyć wzorzec projektowy wieloagentowy. Jednak może nie być od razu jasne, kiedy przejść do wieloagentowości i jakie są jej zalety.

## Wprowadzenie

W tej lekcji spróbujemy odpowiedzieć na następujące pytania:

- Do jakich scenariuszy nadają się systemy wieloagentowe?
- Jakie są zalety używania wielu agentów zamiast pojedynczego wykonującego wiele zadań?
- Jakie są elementy składowe implementacji wzorca projektowego wieloagentowego?
- Jak mieć wgląd w to, jak agenci współdziałają ze sobą?

## Cele nauki

Po tej lekcji powinieneś być w stanie:

- Zidentyfikować scenariusze, gdzie pasują systemy wieloagentowe
- Dostrzec zalety stosowania wielu agentów zamiast pojedynczego.
- Zrozumieć elementy składowe implementacji wzorca projektowego wieloagentowego.

Jaki jest szerszy obraz?

*Systemy wieloagentowe to wzorzec projektowy, który pozwala wielu agentom współpracować, aby osiągnąć wspólny cel*.

Wzorzec ten jest szeroko stosowany w różnych dziedzinach, w tym w robotyce, systemach autonomicznych i przetwarzaniu rozproszonym.

## Scenariusze, w których systemy wieloagentowe mają zastosowanie

Jakie więc scenariusze są dobrym przypadkiem użycia systemów wieloagentowych? Odpowiedź brzmi, że istnieje wiele scenariuszy, w których zastosowanie wielu agentów jest korzystne, zwłaszcza w następujących przypadkach:

- **Duże obciążenia**: Duże obciążenia można podzielić na mniejsze zadania i przydzielić różnym agentom, co pozwala na przetwarzanie równoległe i szybsze ukończenie. Przykładem jest przetwarzanie dużych zbiorów danych.
- **Złożone zadania**: Złożone zadania, podobnie jak duże obciążenia, można rozbić na mniejsze podzadania i przydzielić różnym agentom, z których każdy specjalizuje się w określonym aspekcie zadania. Dobrym przykładem są pojazdy autonomiczne, gdzie różni agenci zarządzają nawigacją, wykrywaniem przeszkód i komunikacją z innymi pojazdami.
- **Różnorodne kompetencje**: Różni agenci mogą mieć różne kompetencje, co pozwala im efektywniej zarządzać różnymi aspektami zadania niż pojedynczy agent. Przykładem jest opieka zdrowotna, gdzie agenci mogą obsługiwać diagnostykę, plany leczenia i monitorowanie pacjenta.

## Zalety używania systemów wieloagentowych w porównaniu do pojedynczego agenta

System z jednym agentem może sprawdzić się przy prostych zadaniach, ale przy bardziej złożonych zadaniach użycie wielu agentów daje kilka korzyści:

- **Specjalizacja**: Każdy agent może być wyspecjalizowany do konkretnego zadania. Brak specjalizacji w pojedynczym agencie oznacza, że agent potrafi wszystko, ale może być zdezorientowany przy złożonym zadaniu. Może np. wykonywać zadanie, do którego nie jest najlepiej przystosowany.
- **Skalowalność**: Łatwiej jest skalować system, dodając kolejnych agentów niż przeciążając pojedynczego.
- **Tolerancja na błędy**: Jeśli jeden agent zawiedzie, pozostałe mogą dalej działać, co zapewnia niezawodność systemu.

Weźmy przykład: zarezerwujmy wycieczkę dla użytkownika. System z jednym agentem musiałby obsłużyć wszystkie aspekty procesu rezerwacji, od wyszukiwania lotów po rezerwację hoteli i samochodów. Aby to osiągnąć za pomocą jednego agenta, musiałby on mieć narzędzia do realizacji wszystkich tych zadań. Mogłoby to prowadzić do skomplikowanego i monolitycznego systemu, trudnego w utrzymaniu i skalowaniu. System wieloagentowy mógłby z kolei mieć różnych agentów wyspecjalizowanych w wyszukiwaniu lotów, rezerwacji hoteli i samochodów. Dzięki temu system byłby bardziej modułowy, łatwiejszy w utrzymaniu i skalowalny.

Porównaj to do biura podróży prowadzonym przez mały rodzinny biznes w porównaniu do biura działającego jako franczyza. Mały biznes miałby pojedynczego agenta obsługującego wszystkie aspekty rezerwacji, podczas gdy franczyza miałaby różnych agentów odpowiedzialnych za różne aspekty procesu rezerwacji.

## Elementy składowe implementacji wzorca projektowego wieloagentowego

Zanim zaimplementujesz wzorzec wieloagentowy, musisz poznać elementy, które go tworzą.

Uczyńmy to bardziej konkretnym, ponownie patrząc na przykład rezerwacji wycieczki dla użytkownika. W tym przypadku elementy składowe obejmują:

- **Komunikacja agentów**: Agenci zajmujący się wyszukiwaniem lotów, rezerwacją hoteli i samochodów muszą się komunikować i wymieniać informacjami o preferencjach i ograniczeniach użytkownika. Musisz zdecydować o protokołach i metodach tej komunikacji. Konkretnie oznacza to, że agent wyszukujący loty musi komunikować się z agentem rezerwującym hotele, by zapewnić, że hotel jest rezerwowany na te same daty co lot. Oznacza to, że agenci muszą dzielić się informacjami o datach podróży użytkownika, co wymaga zdecydowania *którzy agenci dzielą się informacjami i jak to robią*.
- **Mechanizmy koordynacji**: Agenci muszą koordynować swoje działania, aby spełnić preferencje i ograniczenia użytkownika. Preferencja użytkownika może być taka, że chce hotel blisko lotniska, podczas gdy ograniczeniem jest, że auta z wypożyczalni są dostępne tylko na lotnisku. Oznacza to, że agent rezerwujący hotel musi się koordynować z agentem rezerwującym samochody, aby spełnić wymagania użytkownika. Musisz zdecydować *jak agenci koordynują swoje działania*.
- **Architektura agentów**: Agenci muszą mieć wewnętrzną strukturę pozwalającą na podejmowanie decyzji i uczenie się z interakcji z użytkownikiem. Oznacza to, że agent wyszukujący loty musi mieć strukturę do podejmowania decyzji, które loty rekomendować użytkownikowi. Musisz zdecydować *jak agenci podejmują decyzje i uczą się z interakcji z użytkownikiem*. Przykładem nauki i poprawy działania agenta może być użycie modelu uczenia maszynowego do rekomendowania lotów na podstawie wcześniejszych preferencji użytkownika.
- **Widoczność interakcji wieloagentowych**: Musisz mieć wgląd w to, jak agenci współdziałają. Potrzebujesz narzędzi i technik do śledzenia działań i interakcji agentów. Może to być w formie narzędzi do logowania i monitoringu, narzędzi wizualizacyjnych oraz mierników wydajności.
- **Wzorce wieloagentowe**: Istnieją różne wzorce implementacji systemów wieloagentowych, takie jak architektury scentralizowane, zdecentralizowane i hybrydowe. Musisz wybrać wzorzec najlepiej pasujący do twojego przypadku użycia.
- **Człowiek w pętli**: W większości przypadków w systemie znajduje się człowiek i musisz poinstruować agentów, kiedy mają prosić o interwencję człowieka. Może to mieć formę użytkownika żądającego konkretnego hotelu lub lotu, którego agenci nie zaproponowali, albo prośby o potwierdzenie przed dokonaniem rezerwacji.

## Widoczność interakcji wieloagentowych

Ważne jest, aby mieć wgląd w to, jak agenci ze sobą współpracują. Ta widoczność jest niezbędna do debugowania, optymalizacji i zapewnienia efektywności całego systemu. Aby to osiągnąć, potrzebujesz narzędzi i technik do śledzenia działań i interakcji agentów. Mogą to być narzędzia do logowania i monitoringu, narzędzia wizualizacyjne oraz mierniki wydajności.

Na przykład przy rezerwacji wycieczki dla użytkownika, możesz mieć panel pokazujący status każdego agenta, preferencje i ograniczenia użytkownika oraz interakcje między agentami. Panel może pokazywać daty podróży, loty rekomendowane przez agenta lotów, hotele rekomendowane przez agenta hotelowego oraz samochody przez agenta wypożyczalni. Pozwala to jasno zobaczyć, jak agenci współpracują i czy spełniane są preferencje i ograniczenia użytkownika.

Przyjrzyjmy się każdemu z tych aspektów bardziej szczegółowo.

- **Narzędzia do logowania i monitoringu**: Chcesz rejestrować każde działanie agenta. Wpis w logu może zawierać informacje o agencie podejmującym działanie, rodzaju działania, czasie wykonania oraz wyniku działania. Te informacje można potem wykorzystać do debugowania, optymalizacji i innych celów.

- **Narzędzia wizualizacyjne**: Narzędzia wizualizacyjne pomagają zobaczyć interakcje między agentami w sposób bardziej intuicyjny. Na przykład możesz mieć wykres pokazujący przepływ informacji między agentami. Pomaga to zidentyfikować wąskie gardła, nieefektywności i inne problemy w systemie.

- **Mierniki wydajności**: Mierniki wydajności pomagają śledzić efektywność systemu wieloagentowego. Możesz np. monitorować czas potrzebny na ukończenie zadania, liczbę zadań wykonanych na jednostkę czasu oraz dokładność rekomendacji agentów. Te informacje pomagają w identyfikacji obszarów do poprawy i optymalizacji systemu.

## Wzorce dla systemów wieloagentowych

Przeanalizujmy kilka konkretnych wzorców, które można zastosować do tworzenia aplikacji wieloagentowych. Oto kilka interesujących wzorców wartych rozważenia:

### Czat grupowy

Ten wzorzec jest przydatny, gdy chcesz stworzyć aplikację czatu grupowego, gdzie wielu agentów może się komunikować między sobą. Typowe zastosowania to współpraca zespołowa, wsparcie klienta i sieci społecznościowe.

W tym wzorcu każdy agent reprezentuje użytkownika w czacie grupowym, a wiadomości są wymieniane między agentami z użyciem protokołu komunikacyjnego. Agenci mogą wysyłać wiadomości do grupy, odbierać je i odpowiadać na wiadomości innych agentów.

Wzorzec można zaimplementować przy użyciu architektury scentralizowanej, gdzie wszystkie wiadomości są przekazywane przez serwer centralny, lub zdecentralizowanej, gdzie wiadomości wymieniane są bezpośrednio.

![Group chat](../../../translated_images/pl/multi-agent-group-chat.ec10f4cde556babd.webp)

### Przekazywanie zadania

Ten wzorzec jest użyteczny, gdy chcesz stworzyć aplikację, w której wielu agentów może przekazywać sobie nawzajem zadania.

Typowe przypadki to wsparcie klienta, zarządzanie zadaniami i automatyzacja przepływu pracy.

W tym wzorcu każdy agent reprezentuje zadanie lub etap w przepływie pracy, a agenci mogą przekazywać zadania innym agentom na podstawie wcześniej ustalonych reguł.

![Hand off](../../../translated_images/pl/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Filtracja współpracująca

Ten wzorzec jest użyteczny, gdy chcesz stworzyć aplikację, w której wielu agentów współpracuje, by tworzyć rekomendacje dla użytkowników.

Powodem, dla którego pożądana jest współpraca wielu agentów, jest to, że każdy agent ma inną specjalizację i może wnosić różne wkłady do procesu rekomendacji.

Weźmy przykład, gdzie użytkownik chce rekomendacji najlepszego akcji do kupienia na giełdzie.

- **Ekspert branżowy**: Jeden agent może być ekspertem w konkretnej branży.
- **Analiza techniczna**: Inny agent może być ekspertem od analizy technicznej.
- **Analiza fundamentalna**: A kolejny agent może być ekspertem od analizy fundamentalnej. Współpracując, agenci mogą dostarczyć użytkownikowi pełniejszą rekomendację.

![Recommendation](../../../translated_images/pl/multi-agent-filtering.d959cb129dc9f608.webp)

## Scenariusz: Proces zwrotu pieniędzy

Weźmy scenariusz, gdzie klient stara się o zwrot pieniędzy za produkt – w tym procesie może być zaangażowanych wiele agentów, ale podzielmy ich na agentów specyficznych dla tego procesu oraz agentów ogólnych, używanych w innych procesach.

**Agenci specyficzni dla procesu zwrotu:**

Poniżej kilka agentów, którzy mogą być zaangażowani w proces zwrotu:

- **Agent klienta**: Reprezentuje klienta i odpowiada za inicjację procesu zwrotu.
- **Agent sprzedawcy**: Reprezentuje sprzedawcę i odpowiada za przetwarzanie zwrotu.
- **Agent płatności**: Reprezentuje proces płatności i odpowiada za zwrot pieniędzy klientowi.
- **Agent rozstrzygający**: Odpowiada za rozwiązywanie problemów pojawiających się podczas procesu zwrotu.
- **Agent zgodności**: Odpowiada za zapewnienie zgodności procesu zwrotu z regulacjami i politykami.

**Agenci ogólni**:

Ci agenci mogą być używani przez inne części twojej działalności.

- **Agent wysyłki**: Reprezentuje proces wysyłki i odpowiada za odesłanie produktu do sprzedawcy. Ten agent może być używany zarówno w procesie zwrotu, jak i do ogólnej wysyłki produktów przy zakupach.
- **Agent opinii**: Odpowiada za zbieranie opinii od klienta. Opinie mogą być zbierane w dowolnym czasie, nie tylko w trakcie procesu zwrotu.
- **Agent eskalacji**: Odpowiada za eskalację problemów do wyższego poziomu wsparcia. Można go używać w dowolnym procesie wymagającym eskalacji.
- **Agent powiadomień**: Odpowiada za wysyłanie powiadomień do klienta na różnych etapach procesu zwrotu.
- **Agent analityczny**: Odpowiada za analizę danych związanych z procesem zwrotu.
- **Agent audytu**: Odpowiada za audyt procesu zwrotu, by upewnić się, że przebiega prawidłowo.
- **Agent raportów**: Odpowiada za tworzenie raportów dotyczących procesu zwrotu.
- **Agent wiedzy**: Odpowiada za utrzymanie bazy wiedzy dotyczącej procesu zwrotu. Ten agent może posiadać wiedzę zarówno o zwrotach, jak i innych częściach działalności.
- **Agent bezpieczeństwa**: Odpowiada za zapewnienie bezpieczeństwa procesu zwrotu.
- **Agent jakości**: Odpowiada za zapewnienie jakości procesu zwrotu.

Wymieniono całkiem sporo agentów, zarówno specyficznych dla procesu zwrotu, jak i ogólnych używanych w innych częściach twojej działalności. Mam nadzieję, że daje to ci obraz, jak możesz zdecydować, których agentów użyć w swoim systemie wieloagentowym.

## Zadanie

Zaprojektuj system wieloagentowy dla procesu wsparcia klienta. Zidentyfikuj agentów zaangażowanych w proces, ich role i obowiązki oraz sposób, w jaki ze sobą współpracują. Weź pod uwagę zarówno agentów specyficznych dla procesu wsparcia klienta, jak i agentów ogólnych, którzy mogą być używani w innych częściach twojej działalności.


> Zastanów się zanim przeczytasz poniższe rozwiązanie, może być potrzebnych więcej agentów, niż myślisz.

> WSKAZÓWKA: Pomyśl o różnych etapach procesu obsługi klienta oraz rozważ agentów potrzebnych dla każdego systemu.

## Rozwiązanie

[Rozwiązanie](./solution/solution.md)

## Sprawdzian wiedzy

### Pytanie 1

Który scenariusz najlepiej pasuje do systemu wieloagentowego?

- [ ] A1: Bot wsparcia odpowiada na często zadawane pytania korzystając z jednej bazy wiedzy i zestawu narzędzi.
- [ ] A2: Proces zwrotów wymaga oddzielnych ról ds. oszustw, płatności i zgodności, każda z własnymi narzędziami, a ich wyniki muszą być skoordynowane.
- [ ] A3: To samo proste zapytanie o klasyfikację pojawia się tysiące razy na godzinę.

### Pytanie 2

Kiedy pojedynczy agent jest zazwyczaj lepszym wyborem?

- [ ] A1: Zadanie można obsłużyć przy pomocy jednego zestawu instrukcji i narzędzi, bez konieczności przekazywania specjalistom.
- [ ] A2: Agent ma dostęp do więcej niż jednego narzędzia.
- [ ] A3: Proces wymaga oddzielnych ról z różnymi uprawnieniami i niezależnymi ścieżkami audytu.

[Rozwiązanie quizu](./solution/solution-quiz.md)

## Podsumowanie

W tej lekcji omówiliśmy wzorzec projektowy wieloagentowy, w tym scenariusze, w których wieloagentowość jest stosowana, zalety używania wielu agentów zamiast pojedynczego, podstawowe elementy implementacji wzorca wieloagentowego oraz jak mieć wgląd w to, jak agenci wzajemnie się komunikują.

### Masz więcej pytań dotyczących wzorca wieloagentowego?

Dołącz do [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), aby spotkać się z innymi uczącymi się, uczestniczyć w godzinach konsultacji i uzyskać odpowiedzi na pytania dotyczące agentów AI.

## Dodatkowe zasoby

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Dokumentacja Microsoft Agent Framework</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Wzorce projektowe agentowe</a>


## Poprzednia lekcja

[Planowanie projektu](../07-planning-design/README.md)

## Następna lekcja

[Metapoznanie w agentach AI](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->