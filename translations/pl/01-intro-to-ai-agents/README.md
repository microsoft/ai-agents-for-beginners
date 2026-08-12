[![Wprowadzenie do Agentów AI](../../../translated_images/pl/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Kliknij powyższy obraz, aby obejrzeć wideo do tej lekcji)_

# Wprowadzenie do Agentów AI i Przypadków Użycia Agentów

Witamy na kursie **AI Agents for Beginners**! Ten kurs daje Ci podstawową wiedzę — oraz rzeczywisty działający kod — aby zacząć budować Agentów AI od podstaw.

Wpadnij się przywitać w <a href="https://discord.gg/kzRShWzttr" target="_blank">Azure AI Discord Community</a> — to społeczność pełna uczących się i budowniczych AI, którzy chętnie odpowiadają na pytania.

Zanim przejdziemy do budowy, upewnijmy się, że naprawdę rozumiemy, czym jest Agent AI i kiedy warto go użyć.

---

## Wprowadzenie

Ta lekcja obejmuje:

- Czym są Agenty AI oraz jakie istnieją ich różne typy
- Do jakich zadań najlepiej nadają się Agenty AI
- Główne elementy, których użyjesz projektując rozwiązanie oparte na agentach

## Cele Nauki

Pod koniec tej lekcji powinieneś być w stanie:

- Wyjaśnić, czym jest Agent AI i jak różni się od tradycyjnego rozwiązania AI
- Wiedzieć, kiedy sięgnąć po Agenta AI (a kiedy nie)
- Zarysować podstawowy projekt rozwiązania opartego na agentach dla realnego problemu

---

## Definicja Agentów AI i Typy Agentów AI

### Czym są Agenty AI?

Oto prosty sposób, aby to sobie wyobrazić:

> **Agenty AI to systemy, które pozwalają Modelom Językowym (LLM) rzeczywiście *coś robić* — poprzez dawanie im narzędzi i wiedzy do działania w świecie, a nie tylko odpowiadania na zapytania.**

Rozwińmy to trochę:

- **System** — Agent AI to nie pojedyncza rzecz. To zbiór części współpracujących ze sobą. W jego rdzeniu każdy agent ma trzy elementy:
  - **Środowisko** — Przestrzeń, w której agent działa. Dla agenta rezerwacji podróży będzie to platforma do rezerwacji.
  - **Sensory** — Jak agent odczytuje bieżący stan środowiska. Nasz agent podróży może sprawdzać dostępność hoteli lub ceny lotów.
  - **Aktuatory** — Jak agent wykonuje działania. Agent podróży może zarezerwować pokój, wysłać potwierdzenie lub anulować rezerwację.

![Czym są Agenty AI?](../../../translated_images/pl/what-are-ai-agents.1ec8c4d548af601a.webp)

- **Modele Językowe** — Agenty istniały przed LLM, ale to LLM sprawiają, że nowoczesne agenty są tak potężne. Potrafią rozumieć język naturalny, rozważać kontekst i przekształcać niejasne żądania użytkownika w konkretny plan działania.

- **Wykonywanie Działań** — Bez systemu agenta, LLM tylko generuje tekst. W systemie agenta, LLM może faktycznie *wykonać* kroki — przeszukać bazę danych, wywołać API, wysłać wiadomość.

- **Dostęp do Narzędzi** — Jakie narzędzia agent może używać zależy od (1) środowiska, w którym działa i (2) co deweloper zdecydował mu dać. Agent podróży może szukać lotów, ale nie edytować danych klientów — wszystko zależy od konfiguracji.

- **Pamięć + Wiedza** — Agenty mogą mieć pamięć krótkotrwałą (bieżąca konwersacja) i długotrwałą (baza klientów, przeszłe interakcje). Agent podróży może "pamiętać", że wolisz miejsca przy oknie.

---

### Różne Typy Agentów AI

Nie wszystkie agenty są zbudowane jednakowo. Oto podział głównych typów, na przykładzie agenta rezerwacji podróży:

| **Typ Agenta** | **Co robi** | **Przykład agenta podróży** |
|---|---|---|
| **Proste Agenty Refleksyjne** | Podążają za twardo zakodowanymi regułami — brak pamięci, brak planowania. | Widzi maila z reklamacją → przekazuje do obsługi klienta. Koniec. |
| **Agenty Refleksyjne oparte na Modelu** | Utrzymuje wewnętrzny model świata i aktualizuje go w miarę zmian. | Śledzi historyczne ceny lotów i sygnalizuje trasy, które nagle stają się drogie. |
| **Agenty Celowe** | Ma cel i krok po kroku ustala, jak go osiągnąć. | Rezerwuje cały wyjazd (loty, samochód, hotel) od Twojej lokalizacji do celu podróży. |
| **Agenty Utylitarne** | Nie tylko znajduje *jakieś* rozwiązanie, ale *najlepsze* poprzez ocenę kompromisów. | Równoważy koszt z wygodą, aby znaleźć wyjazd najlepiej dopasowany do Twoich preferencji. |
| **Agenty Uczące się** | Z czasem staje się lepszy ucząc się na podstawie opinii. | Dostosowuje przyszłe rekomendacje rezerwacji na podstawie ankiet po podróży. |
| **Agenty Hierarchiczne** | Agent na wysokim poziomie dzieli pracę na podzadania i deleguje agentom niższego poziomu. | Prośba o "anulowanie wyjazdu" jest rozdzielana na: anulowanie lotu, anulowanie hotelu, anulowanie wynajmu auta — każde realizowane przez pod-agenta. |
| **Systemy Multi-Agentowe (MAS)** | Wielu niezależnych agentów współpracuje (lub rywalizuje). | Kooperacja: odrębni agenci zajmują się hotelami, lotami i rozrywką. Rywalizacja: wielu agentów rywalizuje o wypełnienie pokoi hotelowych najlepszą ceną. |

---

## Kiedy używać Agentów AI

Tylko dlatego, że *możesz* użyć agenta AI, nie oznacza, że zawsze *powinieneś*. Oto sytuacje, w których agenty naprawdę się sprawdzają:

![Kiedy używać Agentów AI?](../../../translated_images/pl/when-to-use-ai-agents.54becb3bed74a479.webp)

- **Problemy otwarte** — Gdy kroki do rozwiązania problemu nie mogą być zaprogramowane wcześniej. Potrzebujesz, by LLM dynamicznie znalazł drogę.
- **Procesy wieloetapowe** — Zadania wymagające użycia narzędzi na wielu etapach, nie tylko pojedynczego sprawdzenia lub generacji.
- **Poprawa w Czasie** — Gdy chcesz, by system stawał się mądrzejszy na podstawie opinii użytkownika lub sygnałów z otoczenia.

W dalszej części kursu, w lekcji **Budowanie Godnych Zaufania Agentów AI**, zagłębimy się, kiedy (i kiedy *nie*) warto używać agentów AI.

---

## Podstawy Rozwiązań Agentowych

### Tworzenie Agenta

Pierwszą rzeczą, którą robisz budując agenta, jest zdefiniowanie *co potrafi robić* — jego narzędzi, działań i zachowań.

W tym kursie używamy **Microsoft Foundry Agent Service** jako głównej platformy. Obsługuje ona:

- Modele od dostawców, takich jak OpenAI, Mistral i Meta (Llama)
- Dane licencjonowane od dostawców takich jak Tripadvisor
- Ustandaryzowane definicje narzędzi OpenAPI 3.0

### Wzorce Agentowe

Komunikujesz się z LLM poprzez prompt-y. W przypadku agentów nie zawsze możesz ręcznie tworzyć każdy prompt — agent musi działać wieloetapowo. Tu z pomocą przychodzą **Wzorce Agentowe**. To wielokrotnego użytku strategie promptowania i organizowania pracy LLM w bardziej skalowalny, niezawodny sposób.

Kurs jest zorganizowany wokół najczęstszych i najbardziej użytecznych wzorców agentowych.

### Ramy Agentowe

Ramy agentowe dają deweloperom gotowe szablony, narzędzia i infrastrukturę do budowy agentów. Ułatwiają one:

- Podłączanie narzędzi i funkcji
- Obserwowanie, co agent robi (i debugowanie, gdy coś idzie źle)
- Współpracę między wieloma agentami

W tym kursie skupiamy się na **Microsoft Agent Framework (MAF)** do budowy agentów gotowych do produkcji.

---

## Przykłady kodu

Gotowy, by zobaczyć to w działaniu? Oto przykłady kodu do tej lekcji:

- 🐍 Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- 🔷 .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

---

## Masz pytania?

Dołącz do [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), aby połączyć się z innymi uczącymi się, uczestniczyć w godzinach konsultacji i uzyskać odpowiedzi na pytania dotyczące Agentów AI od społeczności.


---

## Testowanie tego Agenta (Opcjonalne)

Gdy nauczysz się wdrażać agentów w [Lekcji 16](../16-deploying-scalable-agents/README.md), możesz dodać szybki sprawdzian zdrowia po wdrożeniu dla tego agenta `TravelAgent` z gotowym katalogiem [`tests/lesson-01-smoke-tests.json`](../../../tests/lesson-01-smoke-tests.json). Zobacz [`tests/README.md`](../tests/README.md) jak go uruchomić.

---

## Poprzednia Lekcja

[Konfiguracja kursu](../00-course-setup/README.md)

## Następna Lekcja

[Odkrywanie Ram Agentowych](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->