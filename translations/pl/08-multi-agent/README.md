[![Projekt wieloagentowy](../../../translated_images/pl/lesson-8-thumbnail.278a3e4a59137d62.webp)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Kliknij obraz powyżej, aby obejrzeć wideo z tej lekcji)_

# Wzorce projektowe systemów wieloagentowych

Gdy zaczniesz pracować nad projektem obejmującym wielu agentów, będziesz musiał rozważyć wzorzec projektowy dla systemów wieloagentowych. Jednak może nie być od razu jasne, kiedy przejść na rozwiązanie wieloagentowe i jakie są korzyści.

## Wprowadzenie

W tej lekcji chcemy odpowiedzieć na następujące pytania:

- W jakich scenariuszach stosowanie systemów wieloagentowych ma zastosowanie?
- Jakie są zalety używania wielu agentów w porównaniu z jednym agentem wykonującym wiele zadań?
- Jakie są elementy składowe implementacji wzorca wieloagentowego?
- Jak uzyskać widoczność tego, jak agenty wchodzą ze sobą w interakcje?

## Cele nauki

Po tej lekcji powinieneś być w stanie:

- Zidentyfikować scenariusze, w których systemy wieloagentowe mają zastosowanie
- Rozpoznać zalety używania wielu agentów zamiast pojedynczego agenta
- Zrozumieć elementy składowe implementacji wzorca wieloagentowego

Jaki jest szerszy kontekst?

*Systemy wieloagentowe to wzorzec projektowy, który pozwala wielu agentom współpracować, aby osiągnąć wspólny cel*.

Ten wzorzec jest szeroko stosowany w różnych dziedzinach, w tym w robotyce, systemach autonomicznych i przetwarzaniu rozproszonym.

## Scenariusze, w których systemy wieloagentowe mają zastosowanie

Jakie scenariusze są dobrym przypadkiem użycia dla systemów wieloagentowych? Odpowiedź jest taka, że istnieje wiele scenariuszy, w których zatrudnienie wielu agentów jest korzystne, zwłaszcza w następujących przypadkach:

- **Duże obciążenia robocze**: Duże obciążenia robocze można podzielić na mniejsze zadania i przypisać różnym agentom, co pozwala na przetwarzanie równoległe i szybsze wykonanie. Przykładem może być duże zadanie związane z przetwarzaniem danych.
- **Złożone zadania**: Złożone zadania, podobnie jak duże obciążenia, można rozbić na mniejsze podzadania i przypisać różnym agentom, z których każdy specjalizuje się w określonym aspekcie zadania. Dobrym przykładem są pojazdy autonomiczne, gdzie różni agenci zarządzają nawigacją, wykrywaniem przeszkód i komunikacją z innymi pojazdami.
- **Różnorodne kompetencje**: Różni agenci mogą mieć różnorodne kompetencje, co pozwala im skuteczniej obsługiwać różne aspekty zadania niż pojedynczy agent. Dobrym przykładem jest służba zdrowia, gdzie agenci mogą zarządzać diagnostyką, planami leczenia i monitorowaniem pacjenta.

## Zalety używania wielu agentów zamiast pojedynczego agenta

System oparty na pojedynczym agencie może dobrze sprawdzić się w prostych zadaniach, ale w przypadku bardziej złożonych zadań użycie wielu agentów może przynieść kilka korzyści:

- **Specjalizacja**: Każdy agent może być wyspecjalizowany w konkretnym zadaniu. Brak specjalizacji w pojedynczym agencie oznacza, że masz agenta, który potrafi robić wszystko, ale może się pogubić, gdy napotka złożone zadanie. Może na przykład wykonywać zadanie, do którego nie jest najlepiej przystosowany.
- **Skalowalność**: Łatwiej jest skalować systemy poprzez dodawanie kolejnych agentów niż przeciążanie jednego agenta.
- **Tolerancja błędów**: Jeśli jeden agent zawiedzie, inni mogą nadal funkcjonować, co zapewnia niezawodność systemu.

Weźmy przykład: zarezerwujmy podróż dla użytkownika. System z jednym agentem musiałby obsłużyć wszystkie aspekty procesu rezerwacji podróży, od wyszukiwania lotów po rezerwację hoteli i samochodów. Aby osiągnąć to jednym agentem, agent musiałby mieć narzędzia do obsługi wszystkich tych zadań. Mogłoby to prowadzić do powstania skomplikowanego i monolitycznego systemu, który jest trudny w utrzymaniu i skalowaniu. System wieloagentowy mógłby natomiast mieć różnych agentów wyspecjalizowanych w wyszukiwaniu lotów, rezerwowaniu hoteli i wynajmowaniu samochodów. Sprawiłoby to, że system byłby bardziej modułowy, łatwiejszy w utrzymaniu i skalowalny.

Porównaj to z biurem podróży prowadzonym jako małe, rodzinne biuro (mom-and-pop) w kontraście do biura podróży działającego jako franczyza. W tym pierwszym przypadku jeden agent obsługiwałby wszystkie aspekty procesu rezerwacji podróży, podczas gdy franczyza miałaby różnych agentów zajmujących się różnymi aspektami procesu rezerwacji.

## Elementy składowe implementacji wzorca wieloagentowego

Zanim będziesz mógł zaimplementować wzorzec wieloagentowy, musisz zrozumieć elementy składowe, które tworzą ten wzorzec.

Uprośćmy to, ponownie patrząc na przykład rezerwacji podróży dla użytkownika. W tym przypadku elementy składowe obejmowałyby:

- **Komunikacja między agentami**: Agenty wyszukujące loty, rezerwujące hotele i samochody muszą się komunikować i udostępniać informacje o preferencjach i ograniczeniach użytkownika. Musisz zdecydować o protokołach i metodach tej komunikacji. Konkretnie oznacza to, że agent wyszukujący loty musi komunikować się z agentem rezerwującym hotele, aby upewnić się, że hotel jest zarezerwowany na te same daty co lot. Oznacza to, że agenty muszą udostępniać informacje o datach podróży użytkownika, co znaczy, że musisz zdecydować *które agenty udostępniają informacje i jak je udostępniają*.
- **Mechanizmy koordynacji**: Agenty muszą koordynować swoje działania, aby zapewnić spełnienie preferencji i ograniczeń użytkownika. Preferencją użytkownika może być na przykład hotel blisko lotniska, podczas gdy ograniczeniem może być dostępność samochodów tylko na lotnisku. Oznacza to, że agent rezerwujący hotele musi koordynować się z agentem rezerwującym samochody, aby zapewnić zgodność preferencji i ograniczeń użytkownika. Musisz zdecydować *jak agenty koordynują swoje działania*.
- **Architektura agenta**: Agenty muszą mieć wewnętrzną strukturę do podejmowania decyzji i uczenia się na podstawie interakcji z użytkownikiem. Oznacza to, że agent wyszukujący loty musi mieć strukturę pozwalającą podejmować decyzje o tym, które loty polecić użytkownikowi. Musisz zdecydować *jak agenty podejmują decyzje i uczą się na podstawie interakcji z użytkownikiem*. Przykłady uczenia i poprawy działania agenta mogą obejmować wykorzystanie modelu uczenia maszynowego przez agenta wyszukującego loty do polecania lotów użytkownikowi na podstawie jego wcześniejszych preferencji.
- **Widoczność interakcji między agentami**: Musisz mieć widoczność tego, jak wieloagentowe interakcje przebiegają między agentami. Oznacza to, że potrzebujesz narzędzi i technik do śledzenia aktywności i interakcji agentów. Może to mieć formę narzędzi do logowania i monitorowania, narzędzi wizualizacyjnych oraz metryk wydajności.
- **Wzorce wieloagentowe**: Istnieją różne wzorce implementacji systemów wieloagentowych, takie jak architektury scentralizowane, zdecentralizowane i hybrydowe. Musisz zdecydować, który wzorzec najlepiej pasuje do twojego przypadku użycia.
- **Człowiek w pętli**: W większości przypadków masz człowieka w pętli i musisz zaprojektować, kiedy agenty mają prosić o interwencję człowieka. Może to mieć formę użytkownika proszącego o konkretny hotel lub lot, którego agenty nie poleciły, lub proszenia o potwierdzenie przed dokonaniem rezerwacji lotu czy hotelu.

## Widoczność interakcji między agentami

Ważne jest, abyś miał widoczność tego, jak agenty wchodzą ze sobą w interakcje. Ta widoczność jest niezbędna do debugowania, optymalizacji i zapewnienia ogólnej skuteczności systemu. Aby to osiągnąć, potrzebujesz narzędzi i technik do śledzenia aktywności i interakcji agentów. Może to mieć formę narzędzi do logowania i monitorowania, narzędzi do wizualizacji oraz metryk wydajności.

Na przykład w przypadku rezerwacji podróży dla użytkownika możesz mieć pulpit nawigacyjny pokazujący status każdego agenta, preferencje i ograniczenia użytkownika oraz interakcje między agentami. Ten pulpit mógłby pokazywać daty podróży użytkownika, loty rekomendowane przez agenta lotów, hotele rekomendowane przez agenta hotelowego oraz samochody rekomendowane przez agenta ds. wynajmu. Dałoby to jasny obraz tego, jak agenty wchodzą ze sobą w interakcje i czy preferencje oraz ograniczenia użytkownika są spełniane.

Przyjrzyjmy się każdemu z tych aspektów bardziej szczegółowo.

- **Narzędzia do logowania i monitorowania**: Chcesz mieć logi każdej akcji wykonanej przez agenta. Wpis w logu może przechowywać informacje o agencie, który wykonał akcję, o wykonanej akcji, czasie jej wykonania oraz wyniku. Te informacje można następnie wykorzystać do debugowania, optymalizacji i innych celów.
- **Narzędzia do wizualizacji**: Narzędzia wizualizacyjne mogą pomóc zobaczyć interakcje między agentami w bardziej intuicyjny sposób. Na przykład możesz mieć grafikę pokazującą przepływ informacji między agentami. To może pomóc zidentyfikować wąskie gardła, nieefektywności i inne problemy w systemie.
- **Metryki wydajności**: Metryki wydajności mogą pomóc śledzić skuteczność systemu wieloagentowego. Na przykład możesz śledzić czas potrzebny na wykonanie zadania, liczbę zadań wykonanych na jednostkę czasu oraz dokładność rekomendacji udzielanych przez agentów. Te informacje mogą pomóc wskazać obszary do poprawy i zoptymalizować system.

## Wzorce wieloagentowe

Zanurzmy się w kilka konkretnych wzorców, które możemy wykorzystać do tworzenia aplikacji wieloagentowych. Oto kilka interesujących wzorców wartych rozważenia:

### Czat grupowy

Ten wzorzec jest przydatny, gdy chcesz stworzyć aplikację czatu grupowego, w której wielu agentów może się komunikować ze sobą. Typowe przypadki użycia tego wzorca to współpraca zespołowa, obsługa klienta i sieci społecznościowe.

W tym wzorcu każdy agent reprezentuje użytkownika w czacie grupowym, a wiadomości są wymieniane między agentami przy użyciu protokołu komunikatów. Agenty mogą wysyłać wiadomości na czat grupowy, otrzymywać wiadomości z czatu i odpowiadać na wiadomości od innych agentów.

Wzorzec ten można zaimplementować przy użyciu architektury scentralizowanej, w której wszystkie wiadomości są trasowane przez serwer centralny, lub architektury zdecentralizowanej, w której wiadomości są wymieniane bezpośrednio.

![Czat grupowy](../../../translated_images/pl/multi-agent-group-chat.ec10f4cde556babd.webp)

### Przekazanie zadań

Ten wzorzec jest przydatny, gdy chcesz stworzyć aplikację, w której wielu agentów może przekazywać sobie zadania.

Typowe przypadki użycia tego wzorca obejmują obsługę klienta, zarządzanie zadaniami i automatyzację przepływów pracy.

W tym wzorcu każdy agent reprezentuje zadanie lub krok w przepływie pracy, a agenty mogą przekazywać zadania innym agentom na podstawie z góry określonych reguł.

![Przekazanie zadań](../../../translated_images/pl/multi-agent-hand-off.4c5fb00ba6f8750a.webp)

### Filtrowanie kolaboracyjne

Ten wzorzec jest przydatny, gdy chcesz stworzyć aplikację, w której wielu agentów może współpracować, aby tworzyć rekomendacje dla użytkowników.

Powód, dla którego warto, aby wielu agentów współpracowało, polega na tym, że każdy agent może mieć inną ekspertyzę i może przyczyniać się do procesu rekomendacji na różne sposoby.

Weźmy przykład, w którym użytkownik chce rekomendacji dotyczącej najlepszej akcji do kupienia na giełdzie.

- **Ekspert branżowy**:. Jeden agent może być ekspertem w konkretnej branży.
- **Analiza techniczna**: Inny agent może być ekspertem w analizie technicznej.
- **Analiza fundamentalna**: A jeszcze inny agent może być ekspertem w analizie fundamentalnej. Współpracując, ci agenci mogą dostarczyć użytkownikowi bardziej kompleksową rekomendację.

![Rekomendacja](../../../translated_images/pl/multi-agent-filtering.d959cb129dc9f608.webp)

## Scenariusz: proces zwrotu

Rozważ scenariusz, w którym klient stara się uzyskać zwrot za produkt — w tym procesie może uczestniczyć dość wiele agentów, ale podzielmy je na agentów specyficznych dla tego procesu oraz ogólnych agentów, których można używać w innych procesach.

**Agenty specyficzne dla procesu zwrotu**:

Poniżej znajdują się niektóre agenty, które mogłyby być zaangażowane w proces zwrotu:

- **Agent klienta**: Ten agent reprezentuje klienta i jest odpowiedzialny za zainicjowanie procesu zwrotu.
- **Agent sprzedawcy**: Ten agent reprezentuje sprzedawcę i jest odpowiedzialny za przetworzenie zwrotu.
- **Agent płatności**: Ten agent reprezentuje proces płatności i jest odpowiedzialny za zwrócenie środków klientowi.
- **Agent rozstrzygania**: Ten agent reprezentuje proces rozstrzygania i jest odpowiedzialny za rozwiązywanie wszelkich problemów, które pojawią się w trakcie procesu zwrotu.
- **Agent zgodności**: Ten agent reprezentuje proces zgodności i jest odpowiedzialny za zapewnienie, że proces zwrotu jest zgodny z przepisami i politykami.

**Agenty ogólne**:

Te agenty mogą być wykorzystywane przez inne części twojego biznesu.

- **Agent wysyłki**: Ten agent reprezentuje proces wysyłki i jest odpowiedzialny za odesłanie produktu do sprzedawcy. Ten agent może być używany zarówno w procesie zwrotu, jak i przy ogólnej wysyłce produktu w ramach zakupu.
- **Agent opinii**: Ten agent reprezentuje proces zbierania opinii i jest odpowiedzialny za zbieranie informacji zwrotnych od klienta. Opinie mogą być zbierane w dowolnym momencie, nie tylko podczas procesu zwrotu.
- **Agent eskalacji**: Ten agent reprezentuje proces eskalacji i jest odpowiedzialny za przekazywanie problemów na wyższy poziom wsparcia. Możesz używać tego typu agenta w każdym procesie, gdzie trzeba eskalować problem.
- **Agent powiadomień**: Ten agent reprezentuje proces powiadamiania i jest odpowiedzialny za wysyłanie powiadomień do klienta na różnych etapach procesu zwrotu.
- **Agent analityczny**: Ten agent reprezentuje proces analizy i jest odpowiedzialny za analizowanie danych związanych z procesem zwrotu.
- **Agent audytu**: Ten agent reprezentuje proces audytu i jest odpowiedzialny za kontrolę procesu zwrotu, aby upewnić się, że przebiega poprawnie.
- **Agent raportowania**: Ten agent reprezentuje proces raportowania i jest odpowiedzialny za generowanie raportów dotyczących procesu zwrotu.
- **Agent wiedzy**: Ten agent reprezentuje proces zarządzania wiedzą i jest odpowiedzialny za utrzymywanie bazy wiedzy związanej z procesem zwrotu. Ten agent może posiadać wiedzę zarówno o zwrotach, jak i o innych obszarach twojego biznesu.
- **Agent bezpieczeństwa**: Ten agent reprezentuje proces bezpieczeństwa i jest odpowiedzialny za zapewnienie bezpieczeństwa procesu zwrotu.
- **Agent jakości**: Ten agent reprezentuje proces kontroli jakości i jest odpowiedzialny za zapewnienie jakości procesu zwrotu.

Wcześniej wymieniono całkiem sporo agentów, zarówno specyficznych dla procesu zwrotu, jak i ogólnych agentów, które można wykorzystać w innych częściach twojego biznesu. Miejmy nadzieję, że daje to wyobrażenie o tym, jak możesz zdecydować, które agenty użyć w swoim systemie wieloagentowym.

## Zadanie

Zaprojektuj system wieloagentowy dla procesu obsługi klienta. Zidentyfikuj agenty zaangażowane w proces, ich role i obowiązki oraz sposób, w jaki wchodzą ze sobą w interakcje. Weź pod uwagę zarówno agenty specyficzne dla procesu obsługi klienta, jak i agenty ogólne, które można wykorzystać w innych częściach twojego biznesu.
> Pomyśl zanim przeczytasz następujące rozwiązanie, możesz potrzebować więcej agentów, niż myślisz.
> 
> Wskazówka: Pomyśl o różnych etapach procesu obsługi klienta oraz rozważ agentów potrzebnych dla każdego systemu.

## Rozwiązanie

[Rozwiązanie](./solution/solution.md)

## Sprawdzenie wiedzy

Pytanie: Kiedy należy rozważyć użycie wielu agentów?

- [ ] A1: Gdy masz niewielkie obciążenie i proste zadanie.
- [ ] A2: Kiedy masz duże obciążenie
- [ ] A3: Kiedy masz proste zadanie.

[Quiz rozwiązania](./solution/solution-quiz.md)

## Podsumowanie

W tej lekcji omówiliśmy wzorzec projektowy wielu agentów, w tym scenariusze, w których wielu agentów jest zastosowalnych, zalety stosowania wielu agentów zamiast pojedynczego agenta, elementy składowe implementacji wzorca projektowego wielu agentów oraz sposoby uzyskania wglądu w to, jak poszczególni agenci wchodzą ze sobą w interakcje.

### Masz więcej pytań dotyczących wzorca projektowego wielu agentów?

Dołącz do [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), aby spotkać innych uczących się, uczestniczyć w godzinach konsultacji i uzyskać odpowiedzi na pytania dotyczące agentów AI.

## Dodatkowe zasoby

- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Dokumentacja Microsoft Agent Framework</a>
- <a href="https://www.analyticsvidhya.com/blog/2024/10/agentic-design-patterns/" target="_blank">Agentowe wzorce projektowe</a>


## Poprzednia lekcja

[Planowanie projektu](../07-planning-design/README.md)

## Następna lekcja

[Metapoznanie w agentach AI](../09-metacognition/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Zastrzeżenie:
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI Co-op Translator (https://github.com/Azure/co-op-translator). Dokładamy starań, aby tłumaczenie było jak najbardziej dokładne, jednak prosimy pamiętać, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy uznać za źródło wiążące. Dla informacji istotnych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->