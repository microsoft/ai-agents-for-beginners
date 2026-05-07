[![Wprowadzenie do Agentów AI](../../../translated_images/pl/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Kliknij powyższy obrazek, aby obejrzeć wideo do tej lekcji)_

# Wprowadzenie do Agentów AI i zastosowań Agentów

Witamy w kursie **Agenci AI dla początkujących**! Ten kurs dostarcza podstawowej wiedzy — oraz działającego kodu — aby zacząć tworzyć Agentów AI od podstaw.

Przyjdź i przywitaj się w <a href="https://discord.gg/kzRShWzttr" target="_blank">Społeczności Azure AI na Discordzie</a> — jest pełna uczących się i twórców AI, którzy chętnie odpowiedzą na pytania.

Zanim przejdziemy do budowania, upewnijmy się, że naprawdę rozumiemy, czym jest Agent AI i kiedy warto go używać.

---

## Wprowadzenie

Ta lekcja obejmuje:

- Czym są Agenci AI oraz jakie istnieją ich typy
- Jakie zadania są najodpowiedniejsze dla Agentów AI
- Podstawowe elementy, których użyjesz projektując rozwiązanie oparte na Agentach

## Cele nauki

Pod koniec tej lekcji powinieneś potrafić:

- Wyjaśnić, czym jest Agent AI i czym różni się od zwykłego rozwiązania AI
- Wiedzieć, kiedy sięgnąć po Agenta AI (a kiedy nie)
- Szkicować podstawowy projekt rozwiązania agentowego dla realnego problemu

---

## Definicja Agentów AI i typy Agentów AI

### Czym są Agenci AI?

Oto proste wyjaśnienie:

> **Agenci AI to systemy, które pozwalają Dużym Modelom Językowym (LLM) faktycznie *działać* — dając im narzędzia i wiedzę do działania w świecie, a nie tylko odpowiadania na zapytania.**

Rozwińmy to trochę:

- **System** — Agent AI to nie tylko jedna rzecz. To zbiór współpracujących ze sobą części. W swojej istocie każdy agent ma trzy elementy:
  - **Środowisko** — przestrzeń, w której działa agent. Dla agenta rezerwacji podróży będzie to sama platforma rezerwacyjna.
  - **Czujniki** — sposób, w jaki agent odczytuje aktualny stan środowiska. Nasz agent podróży może sprawdzać dostępność hoteli lub ceny lotów.
  - **Aktuatory** — sposób, w jaki agent wykonuje działania. Agent podróży może zarezerwować pokój, wysłać potwierdzenie lub anulować rezerwację.

![Czym są Agenci AI?](../../../translated_images/pl/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Duże Modele Językowe** — Agenci istnieli przed LLM, ale to LLM sprawiają, że nowoczesni agenci są tak potężni. Potrafią rozumieć język naturalny, rozważać kontekst i przekształcić niejasne żądanie użytkownika w konkretny plan działania.

- **Wykonywanie Działań** — Bez systemu agenta, LLM tylko generuje tekst. W systemie agenta, LLM może faktycznie *wykonywać* kroki — wyszukiwać w bazie danych, wywoływać API, wysyłać wiadomości.

- **Dostęp do Narzędzi** — Narzędzia, których agent może używać, zależą od (1) środowiska, w którym działa, i (2) co twórca mu udostępnił. Agent podróży może wyszukiwać loty, ale nie edytować danych klientów — wszystko zależy od połączeń.

- **Pamięć + Wiedza** — Agenci mogą mieć pamięć krótkotrwałą (bieżąca rozmowa) i długotrwałą (baza klientów, wcześniejsze interakcje). Agent podróży może „pamiętać”, że wolisz miejsca przy oknie.

---

### Różne Typy Agentów AI

Nie wszyscy agenci są tworzeni tak samo. Oto podział głównych typów, używając agenta rezerwacji podróży jako przykładu:

| **Typ Agenta** | **Co robi** | **Przykład agenta podróży** |
|---|---|---|
| **Agenci prostego odruchu** | Kierują się sztywnymi regułami — brak pamięci, brak planowania. | Widzi mail z reklamacją → przekazuje do obsługi klienta. Tylko tyle. |
| **Agenci odruchowi oparte na modelu** | Utrzymuje wewnętrzny model świata i aktualizuje go, gdy się zmienia. | Śledzi historyczne ceny lotów i zaznacza trasy, które nagle staniały lub podrożały. |
| **Agenci oparte na celach** | Ma określony cel i krok po kroku planuje, jak go osiągnąć. | Rezerwuje pełną podróż (loty, auto, hotel) zaczynając z Twojej lokalizacji, aby dotrzeć do celu. |
| **Agenci oparte na użyteczności** | Nie tylko znajduje *jakieś* rozwiązanie — szuka *najlepszego* poprzez ważenie kompromisów. | Równoważy koszt i wygodę, by znaleźć podróż najlepiej dopasowaną do Twoich preferencji. |
| **Agenci uczący się** | Poprawia się z czasem ucząc się na podstawie informacji zwrotnych. | Dostosowuje przyszłe rekomendacje rezerwacji na podstawie ankiety po podróży. |
| **Agenci hierarchiczni** | Agent wysokiego poziomu dzieli zadania na podzadania, delegując je niższym agentom. | „Anuluj podróż” rozbija na: anuluj lot, anuluj hotel, anuluj wynajem auta — każdy obsługiwany przez pod-agenta. |
| **Systemy wieloagentowe (MAS)** | Wielu niezależnych agentów współpracuje (lub rywalizuje). | Współpraca: osobne agenty odpowiadają za hotele, loty i rozrywkę. Rywalizacja: wielu agentów konkuruje o rezerwacje hotelowe w najlepszej cenie. |

---

## Kiedy używać Agentów AI

Tylko dlatego, że możesz użyć Agenta AI, nie znaczy, że zawsze powinieneś. Oto sytuacje, w których agenci naprawdę się sprawdzają:

![Kiedy używać Agentów AI?](../../../translated_images/pl/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Problemy otwarte** — Gdy kroki rozwiązania problemu nie mogą być zaprogramowane na sztywno. LLM musi dynamicznie wyznaczyć ścieżkę działania.
- **Procesy wieloetapowe** — Zadania, które wymagają użycia narzędzi w wielu krokach, nie tylko jednorazowego wyszukiwania czy generowania.
- **Ulepszanie z czasem** — Gdy chcesz, aby system stawał się mądrzejszy na podstawie opinii użytkowników lub sygnałów środowiskowych.

Dogłębniej omówimy, kiedy (a kiedy *nie*) używać Agentów AI w lekcji **Budowanie zaufanych Agentów AI** później w kursie.

---

## Podstawy rozwiązań agentowych

### Tworzenie Agenta

Pierwszą rzeczą, którą robisz budując agenta, jest zdefiniowanie *co potrafi* — czyli jego narzędzi, działań i zachowań.

W tym kursie korzystamy głównie z **Azure AI Agent Service** jako platformy. Obsługuje ona:

- Otwarte modele, takie jak OpenAI, Mistral i Llama
- Licencjonowane dane od dostawców, np. Tripadvisor
- Standards Definicje narzędzi OpenAPI 3.0

### Wzorce agentowe

Komunikujesz się z LLM przez prompty. W przypadku agentów nie zawsze można ręcznie tworzyć każdy prompt — agent musi działać na wielu krokach. Tutaj z pomocą przychodzą **wzorce agentowe**. To wielokrotnego użytku strategie promptowania i orkiestracji LLM, które są bardziej skalowalne i niezawodne.

Ten kurs opiera się na najczęstszych i najbardziej użytecznych wzorcach agentowych.

### Frameworki agentowe

Frameworki agentowe dostarczają programistom gotowe szablony, narzędzia i infrastrukturę do tworzenia agentów. Ułatwiają one:

- Łączenie narzędzi i funkcji
- Obserwowanie działania agenta (i debugowanie błędów)
- Współpracę między wieloma agentami

W tym kursie skupiamy się na **Microsoft Agent Framework (MAF)** do tworzenia agentów gotowych do wdrożenia produkcyjnego.

---

## Przykłady kodu

Chcesz zobaczyć to w akcji? Oto przykładowe kody do tej lekcji:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Masz pytania?

Dołącz do [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), aby połączyć się z innymi uczącymi się, uczestniczyć w godzinach konsultacji i uzyskać odpowiedzi na pytania dotyczące Agentów AI od społeczności.

---

## Poprzednia lekcja

[Konfiguracja kursu](../00-course-setup/README.md)

## Następna lekcja

[Poznawanie frameworków agentowych](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Dokument ten został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dążymy do jak największej dokładności, prosimy pamiętać, że tłumaczenia automatyczne mogą zawierać błędy lub niedokładności. Oryginalny dokument w języku pierwotnym powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zaleca się korzystanie z profesjonalnego, ludzkiego tłumaczenia. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->