<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1a008c204051cba8d0e253b75f261c41",
  "translation_date": "2025-08-30T14:23:38+00:00",
  "source_file": "08-multi-agent/README.md",
  "language_code": "pl"
}
-->
[![Projektowanie wieloagentowe](../../../translated_images/lesson-8-thumbnail.278a3e4a59137d625df92de3f885d2da2a92b1f7017abba25a99fb25edd83a55.pl.png)](https://youtu.be/V6HpE9hZEx0?si=A7K44uMCqgvLQVCa)

> _(Kliknij obrazek powyżej, aby obejrzeć wideo z tej lekcji)_

# Wzorce projektowe dla systemów wieloagentowych

Gdy tylko zaczniesz pracować nad projektem obejmującym wielu agentów, będziesz musiał rozważyć zastosowanie wzorca projektowego dla systemów wieloagentowych. Jednak nie zawsze jest od razu jasne, kiedy należy przejść na system wieloagentowy i jakie są z tego korzyści.

## Wprowadzenie

W tej lekcji postaramy się odpowiedzieć na następujące pytania:

- W jakich scenariuszach można zastosować systemy wieloagentowe?
- Jakie są zalety korzystania z systemów wieloagentowych w porównaniu z jednym agentem wykonującym wiele zadań?
- Jakie są podstawowe elementy wdrażania wzorca projektowego dla systemów wieloagentowych?
- Jak uzyskać wgląd w interakcje między wieloma agentami?

## Cele nauki

Po tej lekcji powinieneś być w stanie:

- Zidentyfikować scenariusze, w których systemy wieloagentowe są odpowiednie.
- Rozpoznać zalety korzystania z systemów wieloagentowych w porównaniu z jednym agentem.
- Zrozumieć podstawowe elementy wdrażania wzorca projektowego dla systemów wieloagentowych.

Jaki jest szerszy kontekst?

*Systemy wieloagentowe to wzorzec projektowy, który pozwala wielu agentom współpracować w celu osiągnięcia wspólnego celu*.

Ten wzorzec jest szeroko stosowany w różnych dziedzinach, takich jak robotyka, systemy autonomiczne i obliczenia rozproszone.

## Scenariusze, w których systemy wieloagentowe są odpowiednie

W jakich sytuacjach warto zastosować systemy wieloagentowe? Odpowiedź brzmi: istnieje wiele scenariuszy, w których wykorzystanie wielu agentów jest korzystne, szczególnie w następujących przypadkach:

- **Duże obciążenia pracą**: Duże zadania można podzielić na mniejsze i przypisać różnym agentom, co pozwala na przetwarzanie równoległe i szybsze ukończenie. Przykładem może być przetwarzanie dużych zbiorów danych.
- **Złożone zadania**: Złożone zadania, podobnie jak duże obciążenia, można podzielić na mniejsze podzadania i przypisać różnym agentom, z których każdy specjalizuje się w określonym aspekcie zadania. Dobrym przykładem są pojazdy autonomiczne, gdzie różni agenci zarządzają nawigacją, wykrywaniem przeszkód i komunikacją z innymi pojazdami.
- **Różnorodne kompetencje**: Różni agenci mogą mieć różne kompetencje, co pozwala im skuteczniej radzić sobie z różnymi aspektami zadania niż jeden agent. Przykładem może być opieka zdrowotna, gdzie agenci zarządzają diagnostyką, planami leczenia i monitorowaniem pacjentów.

## Zalety korzystania z systemów wieloagentowych w porównaniu z jednym agentem

System z jednym agentem może dobrze działać w przypadku prostych zadań, ale w przypadku bardziej złożonych zadań zastosowanie wielu agentów może przynieść kilka korzyści:

- **Specjalizacja**: Każdy agent może być wyspecjalizowany w określonym zadaniu. Brak specjalizacji w przypadku jednego agenta oznacza, że agent może robić wszystko, ale może się pogubić, gdy stanie przed złożonym zadaniem. Może na przykład wykonać zadanie, do którego nie jest najlepiej przystosowany.
- **Skalowalność**: Łatwiej jest skalować systemy, dodając więcej agentów, niż przeciążać jednego agenta.
- **Odporność na błędy**: Jeśli jeden agent zawiedzie, inni mogą nadal działać, zapewniając niezawodność systemu.

Weźmy przykład rezerwacji podróży dla użytkownika. System z jednym agentem musiałby obsłużyć wszystkie aspekty procesu rezerwacji podróży, od wyszukiwania lotów po rezerwację hoteli i wynajem samochodów. Aby to osiągnąć, agent musiałby mieć narzędzia do obsługi wszystkich tych zadań. Mogłoby to prowadzić do powstania skomplikowanego i monolitycznego systemu, który trudno utrzymać i skalować. System wieloagentowy, z kolei, mógłby mieć różnych agentów wyspecjalizowanych w wyszukiwaniu lotów, rezerwacji hoteli i wynajmie samochodów. Dzięki temu system byłby bardziej modułowy, łatwiejszy w utrzymaniu i skalowalny.

Porównaj to do biura podróży prowadzonego jako mały rodzinny biznes w porównaniu z biurem podróży działającym jako franczyza. W małym rodzinnym biznesie jeden agent obsługuje wszystkie aspekty procesu rezerwacji podróży, podczas gdy w franczyzie różni agenci zajmują się różnymi aspektami procesu rezerwacji.

## Podstawowe elementy wdrażania wzorca projektowego dla systemów wieloagentowych

Zanim będziesz mógł wdrożyć wzorzec projektowy dla systemów wieloagentowych, musisz zrozumieć podstawowe elementy, które go tworzą.

Przyjrzyjmy się temu na przykładzie rezerwacji podróży dla użytkownika. W tym przypadku podstawowe elementy obejmują:

- **Komunikacja między agentami**: Agenci odpowiedzialni za wyszukiwanie lotów, rezerwację hoteli i wynajem samochodów muszą się komunikować i wymieniać informacje o preferencjach i ograniczeniach użytkownika. Musisz zdecydować o protokołach i metodach tej komunikacji. Oznacza to na przykład, że agent odpowiedzialny za wyszukiwanie lotów musi komunikować się z agentem odpowiedzialnym za rezerwację hoteli, aby upewnić się, że hotel jest zarezerwowany na te same daty co lot. Oznacza to, że agenci muszą wymieniać informacje o datach podróży użytkownika, co oznacza, że musisz zdecydować *którzy agenci wymieniają informacje i w jaki sposób*.
- **Mechanizmy koordynacji**: Agenci muszą koordynować swoje działania, aby zapewnić spełnienie preferencji i ograniczeń użytkownika. Preferencją użytkownika może być na przykład hotel blisko lotniska, podczas gdy ograniczeniem może być to, że samochody do wynajęcia są dostępne tylko na lotnisku. Oznacza to, że agent odpowiedzialny za rezerwację hoteli musi koordynować działania z agentem odpowiedzialnym za wynajem samochodów, aby zapewnić spełnienie preferencji i ograniczeń użytkownika. Oznacza to, że musisz zdecydować *jak agenci koordynują swoje działania*.
- **Architektura agentów**: Agenci muszą mieć wewnętrzną strukturę umożliwiającą podejmowanie decyzji i uczenie się na podstawie interakcji z użytkownikiem. Oznacza to, że agent odpowiedzialny za wyszukiwanie lotów musi mieć wewnętrzną strukturę umożliwiającą podejmowanie decyzji o tym, które loty polecić użytkownikowi. Oznacza to, że musisz zdecydować *jak agenci podejmują decyzje i uczą się na podstawie interakcji z użytkownikiem*. Przykładem tego, jak agent się uczy i doskonali, może być agent odpowiedzialny za wyszukiwanie lotów, który wykorzystuje model uczenia maszynowego do rekomendowania lotów użytkownikowi na podstawie jego wcześniejszych preferencji.
- **Widoczność interakcji między agentami**: Musisz mieć wgląd w to, jak agenci współdziałają ze sobą. Oznacza to, że musisz mieć narzędzia i techniki do śledzenia działań i interakcji agentów. Mogą to być narzędzia do logowania i monitorowania, narzędzia wizualizacyjne oraz metryki wydajności.
- **Wzorce wieloagentowe**: Istnieją różne wzorce wdrażania systemów wieloagentowych, takie jak architektury scentralizowane, zdecentralizowane i hybrydowe. Musisz zdecydować, który wzorzec najlepiej pasuje do Twojego przypadku użycia.
- **Człowiek w pętli**: W większości przypadków w procesie będzie uczestniczył człowiek i musisz poinstruować agentów, kiedy mają prosić o interwencję człowieka. Może to być na przykład sytuacja, w której użytkownik prosi o konkretny hotel lub lot, którego agenci nie zaproponowali, lub prosi o potwierdzenie przed dokonaniem rezerwacji.

## Widoczność interakcji między agentami

Ważne jest, aby mieć wgląd w to, jak agenci współdziałają ze sobą. Taka widoczność jest kluczowa dla debugowania, optymalizacji i zapewnienia skuteczności całego systemu. Aby to osiągnąć, musisz mieć narzędzia i techniki do śledzenia działań i interakcji agentów. Mogą to być narzędzia do logowania i monitorowania, narzędzia wizualizacyjne oraz metryki wydajności.

Na przykład w przypadku rezerwacji podróży dla użytkownika możesz mieć pulpit nawigacyjny, który pokazuje status każdego agenta, preferencje i ograniczenia użytkownika oraz interakcje między agentami. Taki pulpit może pokazywać daty podróży użytkownika, loty polecane przez agenta lotów, hotele polecane przez agenta hoteli i samochody polecane przez agenta wynajmu samochodów. Dzięki temu będziesz mieć jasny obraz tego, jak agenci współdziałają ze sobą i czy preferencje oraz ograniczenia użytkownika są spełniane.

Przyjrzyjmy się bliżej każdemu z tych aspektów.

- **Narzędzia do logowania i monitorowania**: Chcesz rejestrować każdą akcję podjętą przez agenta. Wpis w dzienniku może zawierać informacje o agencie, który podjął akcję, podjętej akcji, czasie jej podjęcia i wyniku. Te informacje mogą być następnie wykorzystane do debugowania, optymalizacji i innych celów.

- **Narzędzia wizualizacyjne**: Narzędzia wizualizacyjne mogą pomóc w intuicyjnym zobrazowaniu interakcji między agentami. Na przykład możesz mieć wykres pokazujący przepływ informacji między agentami. Może to pomóc w identyfikacji wąskich gardeł, nieefektywności i innych problemów w systemie.

- **Metryki wydajności**: Metryki wydajności mogą pomóc w śledzeniu skuteczności systemu wieloagentowego. Na przykład możesz śledzić czas potrzebny na wykonanie zadania, liczbę zadań wykonanych w jednostce czasu oraz dokładność rekomendacji agentów. Te informacje mogą pomóc w identyfikacji obszarów wymagających poprawy i optymalizacji systemu.

## Wzorce wieloagentowe

Przyjrzyjmy się konkretnym wzorcom, które można wykorzystać do tworzenia aplikacji wieloagentowych. Oto kilka interesujących wzorców wartych rozważenia:

### Czat grupowy

Ten wzorzec jest przydatny, gdy chcesz stworzyć aplikację czatu grupowego, w której wielu agentów może się ze sobą komunikować. Typowe przypadki użycia tego wzorca obejmują współpracę zespołową, obsługę klienta i sieci społecznościowe.

W tym wzorcu każdy agent reprezentuje użytkownika w czacie grupowym, a wiadomości są wymieniane między agentami za pomocą protokołu komunikacyjnego. Agenci mogą wysyłać wiadomości do czatu grupowego, odbierać wiadomości z czatu grupowego i odpowiadać na wiadomości od innych agentów.

Ten wzorzec można zaimplementować za pomocą architektury scentralizowanej, w której wszystkie wiadomości są przesyłane przez centralny serwer, lub architektury zdecentralizowanej, w której wiadomości są wymieniane bezpośrednio.

![Czat grupowy](../../../translated_images/multi-agent-group-chat.ec10f4cde556babd7b450fd01e1a0fac1f9788c27d3b9e54029377bb1bdd1db6.pl.png)

### Przekazywanie zadań

Ten wzorzec jest przydatny, gdy chcesz stworzyć aplikację, w której wielu agentów może przekazywać sobie zadania.

Typowe przypadki użycia tego wzorca obejmują obsługę klienta, zarządzanie zadaniami i automatyzację procesów.

W tym wzorcu każdy agent reprezentuje zadanie lub krok w procesie, a agenci mogą przekazywać zadania innym agentom na podstawie wcześniej zdefiniowanych reguł.

![Przekazywanie zadań](../../../translated_images/multi-agent-hand-off.4c5fb00ba6f8750a0754bf29d49fa19d578080c61da40416df84d866bcdd87a3.pl.png)

### Filtracja współdzielona

Ten wzorzec jest przydatny, gdy chcesz stworzyć aplikację, w której wielu agentów może współpracować, aby rekomendować użytkownikom różne opcje.

Dlaczego warto, aby wielu agentów współpracowało? Ponieważ każdy agent może mieć różne kompetencje i wnosić różne perspektywy do procesu rekomendacji.

Weźmy przykład, w którym użytkownik chce uzyskać rekomendację dotyczącą najlepszej akcji do zakupu na giełdzie.

- **Ekspert branżowy**: Jeden agent może być ekspertem w konkretnej branży.
- **Analiza techniczna**: Inny agent może być ekspertem w analizie technicznej.
- **Analiza fundamentalna**: Jeszcze inny agent może być ekspertem w analizie fundamentalnej. Dzięki współpracy ci agenci mogą dostarczyć użytkownikowi bardziej kompleksową rekomendację.

![Rekomendacja](../../../translated_images/multi-agent-filtering.d959cb129dc9f60826916f0f12fe7a8339b532f5f236860afb8f16b63ea10dc2.pl.png)

## Scenariusz: Proces zwrotu

Rozważmy scenariusz, w którym klient próbuje uzyskać zwrot za produkt. W procesie tym może być zaangażowanych wielu agentów, ale podzielmy ich na agentów specyficznych dla tego procesu oraz agentów ogólnych, którzy mogą być używani w innych procesach.

**Agenci specyficzni dla procesu zwrotu**:

Oto niektórzy agenci, którzy mogą być zaangażowani w proces zwrotu:

- **Agent klienta**: Reprezentuje klienta i jest odpowiedzialny za inicjowanie procesu zwrotu.
- **Agent sprzedawcy**: Reprezentuje sprzedawcę i jest odpowiedzialny za przetwarzanie zwrotu.
- **Agent płatności**: Reprezentuje proces płatności i jest odpowiedzialny za zwrot pieniędzy klientowi.
- **Agent rozwiązywania problemów**: Reprezentuje proces rozwiązywania problemów i jest odpowiedzialny za rozwiązywanie wszelkich problemów, które pojawią się podczas procesu zwrotu.
- **Agent zgodności**: Reprezentuje proces zgodności i jest odpowiedzialny za zapewnienie, że proces zwrotu jest zgodny z przepisami i politykami.

**Agenci ogólni**:

Ci agenci mogą być używani w innych częściach Twojego biznesu.

- **Agent wysyłki**: Reprezentuje proces wysyłki i jest odpowiedzialny za wysyłkę produktu z powrotem do sprzedawcy. Może być używany zarówno w procesie zwrotu, jak i w ogólnej wysyłce produktu, na przykład przy zakupie.
- **Agent opinii**: Reprezentuje proces zbierania opinii i jest odpowiedzialny za zbieranie opinii od klienta. Opinie mogą być zbierane w dowolnym momencie, nie tylko podczas procesu zwrotu.
- **Agent eskalacji**: Reprezentuje proces eskalacji i jest odpowiedzialny za eskalowanie problemów na wyższy poziom wsparcia. Tego typu agent może być używany w każdym procesie, w którym konieczne jest eskalowanie problemu.
- **Agent powiadomień**: Reprezentuje proces powiadomień i jest odpowiedzialny za wysyłanie powiadomień do klienta na różnych etapach procesu zwrotu.
- **Agent analityki**: Reprezentuje proces analityki i jest odpowiedzialny za analizowanie danych związanych z procesem zwrotu.
- **Agent audytu**: Reprezentuje proces audytu i jest odpowiedzialny za audyt procesu zwrotu, aby upewnić się, że jest on przeprowadzany poprawnie.
- **Agent raportowania**: Reprezentuje proces raportowania i jest odpowiedzialny za generowanie raportów dotyczących procesu zwrotu.
- **Agent wiedzy**: Reprezentuje proces zarządzania wiedzą i jest odpowiedzialny za utrzymywanie bazy wiedzy na temat procesu zwrotu. Ten agent może być kompetentny zarówno w zakresie zwrotów, jak i innych części Twojego biznesu.
- **Agent bezpieczeństwa**: Reprezentuje proces bezpieczeństwa i jest odpowiedzialny za zapewnienie bezpieczeństwa procesu zwrotu.
- **Agent jakości**: Reprezentuje proces zapewnienia jakości i jest odpowiedzialny za zapewnienie jakości procesu zwrotu.

Wymieniono tutaj wielu agentów, zarówno specyficznych dla procesu zwrotu, jak i ogólnych, którzy mogą być używani w innych częściach Twojego biznesu. Mamy nadzieję, że daje to wyobrażenie o tym, jak można zdecydować, których agentów użyć w swoim systemie
Zaprojektuj system wieloagentowy dla procesu obsługi klienta. Zidentyfikuj agentów zaangażowanych w proces, ich role i obowiązki oraz sposób, w jaki współdziałają ze sobą. Rozważ zarówno agentów specyficznych dla procesu obsługi klienta, jak i ogólnych agentów, którzy mogą być używani w innych częściach Twojego biznesu.

> Zastanów się, zanim przeczytasz poniższe rozwiązanie, możesz potrzebować więcej agentów, niż Ci się wydaje.

> TIP: Pomyśl o różnych etapach procesu obsługi klienta, a także rozważ agentów potrzebnych dla każdego systemu.

## Rozwiązanie

[Rozwiązanie](./solution/solution.md)

## Sprawdzenie wiedzy

Pytanie: Kiedy warto rozważyć użycie systemu wieloagentowego?

- [ ] A1: Gdy masz małe obciążenie pracą i proste zadanie.
- [ ] A2: Gdy masz duże obciążenie pracą.
- [ ] A3: Gdy masz proste zadanie.

[Rozwiązanie quizu](./solution/solution-quiz.md)

## Podsumowanie

W tej lekcji omówiliśmy wzorzec projektowy wieloagentowy, w tym scenariusze, w których wieloagenty są stosowne, zalety korzystania z wieloagentów w porównaniu z pojedynczym agentem, podstawowe elementy wdrażania wzorca projektowego wieloagentowego oraz sposób uzyskania wglądu w interakcje między wieloma agentami.

### Masz więcej pytań dotyczących wzorca projektowego wieloagentowego?

Dołącz do [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), aby spotkać się z innymi uczącymi się, uczestniczyć w godzinach konsultacji i uzyskać odpowiedzi na pytania dotyczące AI Agentów.

## Dodatkowe zasoby

- ## Poprzednia lekcja

[Projektowanie planowania](../07-planning-design/README.md)

## Następna lekcja

[Metapoznanie w agentach AI](../09-metacognition/README.md)

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.