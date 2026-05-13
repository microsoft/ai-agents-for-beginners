[![Wprowadzenie do AI Agents](../../../translated_images/pl/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Kliknij powyższy obraz, aby obejrzeć wideo do tej lekcji)_

# Wprowadzenie do AI Agents i przypadków użycia Agentów

Witamy na kursie **AI Agents dla początkujących**! Ten kurs daje Ci podstawową wiedzę — oraz działający kod — aby zacząć tworzyć AI Agents od podstaw.

Wpadnij przywitać się na <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord Community</a> — pełne jest uczniów i twórców AI, którzy chętnie odpowiedzą na pytania.

Zanim przejdziemy do budowania, upewnijmy się, że faktycznie rozumiemy, czym jest AI Agent i kiedy ma sens go używać.

---

## Wprowadzenie

W tej lekcji omówimy:

- Czym są AI Agents i jakie istnieją ich rodzaje
- Jakie zadania najlepiej nadają się dla AI Agents
- Podstawowe elementy, których użyjesz przy projektowaniu rozwiązania agentowego

## Cele nauki

Pod koniec tej lekcji powinieneś być w stanie:

- Wyjaśnić, czym jest AI Agent i czym różni się od zwykłego rozwiązania AI
- Wiedzieć, kiedy warto sięgnąć po AI Agent (a kiedy nie warto)
- Nakreślić podstawowy projekt rozwiązania agentowego dla rzeczywistego problemu

---

## Definicja AI Agents i rodzaje AI Agents

### Czym są AI Agents?

Oto proste podejście do tematu:

> **AI Agents to systemy, które pozwalają dużym modelom językowym (LLM) faktycznie *coś robić* — przez udostępnienie im narzędzi i wiedzy do działania na świecie, nie tylko odpowiadania na zapytania.**

Rozwińmy to trochę:

- **System** — AI Agent to nie jest pojedynczy element. To zbiór części współpracujących ze sobą. W swojej istocie każdy agent składa się z trzech elementów:
  - **Środowisko** — przestrzeń, w której agent działa. Dla agenta rezerwacji podróży, to będzie sama platforma rezerwacyjna.
  - **Czujniki** — jak agent odczytuje aktualny stan środowiska. Nasz agent podróży może sprawdzać dostępność hoteli lub ceny lotów.
  - **Aktuatory** — jak agent podejmuje działania. Agent podróży może rezerwować pokój, wysyłać potwierdzenie lub anulować rezerwację.

![Czym są AI Agents?](../../../translated_images/pl/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Duże modele językowe** — Agenci istnieli przed LLM, ale to właśnie LLM czynią nowoczesnych agentów tak potężnymi. Potrafią rozumieć język naturalny, analizować kontekst i zamieniać niejasne zapytania użytkownika w konkretne plany działania.

- **Wykonywanie działań** — Bez systemu agenta, LLM tylko generuje tekst. W systemie agenta LLM może faktycznie *wykonywać* kroki — przeszukiwać bazę danych, wywoływać API, wysyłać wiadomości.

- **Dostęp do narzędzi** — To, jakich narzędzi agent może użyć, zależy (1) od środowiska, w którym działa i (2) od wyboru programisty. Agent podróży może mieć możliwość wyszukiwania lotów, ale nie edytować rekordów klientów — wszystko zależy od tego, co jest połączone.

- **Pamięć + Wiedza** — Agenci mogą mieć pamięć krótkoterminową (bieżąca rozmowa) i długoterminową (baza klientów, wcześniejsze interakcje). Agent podróży może „zapamiętać”, że wolisz miejsca przy oknie.

---

### Różne rodzaje AI Agents

Nie wszyscy agenci są zbudowani tak samo. Oto podział na główne typy, z przykładem agenta rezerwacji podróży:

| **Typ agenta** | **Co robi** | **Przykład agenta podróży** |
|---|---|---|
| **Proste agenty refleksyjne** | Podążają za zakodowanymi regułami — brak pamięci, brak planowania. | Widzi mail z reklamacją → przekazuje do obsługi klienta. Tyle. |
| **Agenty refleksyjne oparte na modelu** | Trzymają wewnętrzny model świata i aktualizują go gdy coś się zmienia. | Śledzi historyczne ceny lotów i zaznacza trasy, które nagle stały się drogie. |
| **Agenty oparte na celach** | Mają cel i krok po kroku planują, jak go osiągnąć. | Rezerwuje pełną wycieczkę (loty, samochód, hotel) zaczynając z twojej obecnej lokalizacji, aby dotrzeć do celu. |
| **Agenty oparte na użyteczności** | Nie znajdują tylko *rozwiązania* — szukają *najlepszego* rozwiązania przez analizę kompromisów. | Równoważy koszt i wygodę, aby znaleźć wycieczkę, która najlepiej pasuje do twoich preferencji. |
| **Agenty uczące się** | Polepszają się z czasem ucząc się na podstawie informacji zwrotnej. | Dostosowuje przyszłe rekomendacje rezerwacji na podstawie wyników ankiety po wycieczce. |
| **Agenty hierarchiczne** | Agent wysokiego poziomu dzieli zadanie na podzadania i deleguje je agentom niższego poziomu. | Prośba o "anulowanie wycieczki" zostaje podzielona na: anuluj lot, anuluj hotel, anuluj wynajem samochodu — każde z nich obsługiwane przez pod-agenta. |
| **Systemy multi-agentowe (MAS)** | Wiele niezależnych agentów współpracujących (lub konkurujących). | Kooperacyjne: oddzielne agenty obsługujące hotele, loty i rozrywkę. Konkurencyjne: wielu agentów konkuruje, aby zapełnić pokoje hotelowe najlepszą ceną. |

---

## Kiedy korzystać z AI Agents

Nie każda możliwość użycia AI Agenta oznacza, że zawsze trzeba tego używać. Oto sytuacje, w których agenci naprawdę błyszczą:

![Kiedy używać AI Agents?](../../../translated_images/pl/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Problemy o otwartym zakończeniu** — Gdy kroki rozwiązania problemu nie mogą być wstępnie zaprogramowane. LLM musi dynamicznie znaleźć ścieżkę.
- **Procesy wieloetapowe** — Zadania wymagające użycia narzędzi na wielu etapach, a nie tylko jednorazowego wyszukiwania lub generowania.
- **Poprawa w czasie** — Gdy chcesz, aby system stawał się mądrzejszy na podstawie informacji zwrotnej od użytkownika lub sygnałów środowiskowych.

Dogłębniej omówimy, kiedy (i kiedy *nie*) należy używać AI Agents na lekcji **Budowanie godnych zaufania AI Agents** później w kursie.

---

## Podstawy rozwiązań agentowych

### Rozwój agenta

Pierwszą rzeczą, którą robisz przy budowie agenta, jest zdefiniowanie *co może robić* — jego narzędzi, działań i zachowań.

Na tym kursie używamy **Azure AI Agent Service** jako głównej platformy. Obsługuje ona:

- Modele od dostawców takich jak OpenAI, Mistral i Meta (Llama)
- Licencjonowane dane od dostawców takich jak Tripadvisor
- Standardowe definicje narzędzi OpenAPI 3.0

### Wzorce agentowe

Komunikujesz się z LLM przez prompt-y. W przypadku agentów nie da się ręcznie tworzyć każdego promptu — agent musi działać na wielu krokach. Właśnie dlatego powstały **wzorce agentowe**. To powtarzalne strategie promptowania i orkiestracji LLM w sposób bardziej skalowalny i niezawodny.

Ten kurs jest zorganizowany wokół najczęstszych i najbardziej przydatnych wzorców agentowych.

### Frameworki agentowe

Frameworki agentowe dają programistom gotowe szablony, narzędzia i infrastrukturę do tworzenia agentów. Ułatwiają one:

- Podłączenie narzędzi i funkcjonalności
- Obserwowanie, co agent robi (oraz debugowanie błędów)
- Współpracę między wieloma agentami

W tym kursie skupiamy się na **Microsoft Agent Framework (MAF)** do budowy agentów gotowych do produkcji.

---

## Przykłady kodu

Gotowy zobaczyć to w akcji? Oto przykłady kodu do tej lekcji:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Masz pytania?

Dołącz do [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), aby połączyć się z innymi uczniami, uczestniczyć w godzinach konsultacji i uzyskać odpowiedzi na pytania dotyczące AI Agents od społeczności.

---

## Poprzednia lekcja

[Konfiguracja kursu](../00-course-setup/README.md)

## Następna lekcja

[Poznawanie frameworków agentowych](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->