[![Wprowadzenie do Agentów AI](../../../translated_images/pl/lesson-1-thumbnail.d21b2c34b32d35bb.webp)](https://youtu.be/3zgm60bXmQk?si=QA4CW2-cmul5kk3D)

> _(Kliknij powyższy obraz, aby obejrzeć wideo tej lekcji)_


# Wprowadzenie do Agentów AI i Przypadków Ich Zastosowania

Witamy na kursie „Agenci AI dla początkujących”! Ten kurs dostarcza podstawową wiedzę i przykłady zastosowań do tworzenia Agentów AI.

Dołącz do <a href="https://discord.gg/kzRShWzttr" target="_blank">Społeczności Azure AI na Discordzie</a>, aby poznać innych uczących się i twórców agentów AI oraz zadać wszelkie pytania dotyczące tego kursu.

Aby rozpocząć ten kurs, zaczynamy od lepszego zrozumienia, czym są Agenci AI i jak możemy ich używać w aplikacjach i przepływach pracy, które tworzymy.

## Wprowadzenie

Ta lekcja obejmuje:

- Czym są Agenci AI i jakie są różne typy agentów?
- Jakie przypadki użycia są najlepsze dla Agentów AI i jak mogą nam pomóc?
- Jakie są podstawowe elementy budulcowe przy projektowaniu rozwiązań agentowych?

## Cele nauki
Po ukończeniu tej lekcji powinieneś być w stanie:

- Zrozumieć koncepcje Agentów AI i jak różnią się od innych rozwiązań AI.
- Efektywnie stosować Agentów AI.
- Produktywnie projektować rozwiązania agentowe zarówno dla użytkowników, jak i klientów.

## Definicja Agentów AI i Typy Agentów AI

### Czym są Agenci AI?

Agenci AI to **systemy**, które umożliwiają **Dużym Modelom Językowym (LLM)** **wykonywanie działań** poprzez rozszerzenie ich możliwości, dając LLM dostęp do **narzędzi** i **wiedzy**.

Podzielmy tę definicję na mniejsze części:

- **System** - Ważne jest, aby postrzegać agentów nie jako pojedynczy komponent, ale jako system wielu komponentów. Na podstawowym poziomie komponentami Agenta AI są:
  - **Środowisko** - Określona przestrzeń, w której działa Agent AI. Na przykład, gdybyśmy mieli agenta do rezerwacji podróży, środowiskiem mogłoby być system rezerwacji podróży, z którego Agent AI korzysta, aby wykonać zadania.
  - **Czujniki** - Środowiska posiadają informacje i zapewniają sprzężenie zwrotne. Agenci AI używają czujników do zbierania i interpretowania informacji o obecnym stanie środowiska. W przykładzie agenta do rezerwacji podróży system rezerwacji może dostarczać informacje takie jak dostępność hoteli czy ceny lotów.
  - **Wykonawcy (Aktuatory)** - Gdy Agent AI otrzyma aktualny stan środowiska, dla bieżącego zadania określa, jakie działanie należy wykonać, by zmienić środowisko. Dla agenta do rezerwacji podróży może to być zarezerwowanie dostępnego pokoju dla użytkownika.

![Czym są Agenci AI?](../../../translated_images/pl/what-are-ai-agents.1ec8c4d548af601a.webp)

**Duże Modele Językowe** - koncepcja agentów istniała przed stworzeniem LLM. Zaleta budowania Agentów AI z LLM to ich zdolność do interpretacji języka ludzkiego i danych. Ta zdolność pozwala LLM interpretować informacje środowiskowe i określić plan zmiany środowiska.

**Wykonywanie Działań** - Poza systemami Agentów AI, LLM są ograniczone do sytuacji, gdy działanie polega na generowaniu treści lub informacji na podstawie zapytania użytkownika. W systemach Agentów AI LLM mogą realizować zadania poprzez interpretację żądania użytkownika i korzystanie z dostępnych narzędzi w ich środowisku.

**Dostęp do Narzędzi** - Do jakich narzędzi LLM ma dostęp, definiuje się przez 1) środowisko, w którym działa, i 2) dewelopera Agenta AI. W naszym przykładzie agenta podróży narzędzia agenta są ograniczone przez operacje dostępne w systemie rezerwacji, a deweloper może ograniczyć dostęp agenta do narzędzi dotyczących tylko lotów.

**Pamięć + Wiedza** - Pamięć może być krótkoterminowa w kontekście rozmowy między użytkownikiem a agentem. Długoterminowo, poza informacjami dostarczanymi przez środowisko, Agenci AI mogą także pozyskiwać wiedzę z innych systemów, usług, narzędzi, a nawet innych agentów. W przykładzie agenta podróży, ta wiedza może być informacją o preferencjach podróżniczych użytkownika znajdującą się w bazie danych klientów.

### Różne typy agentów

Mając ogólną definicję Agentów AI, przyjrzyjmy się konkretnym typom agentów i jak mogą być zastosowane w agencie do rezerwacji podróży.

| **Typ Agenta**                | **Opis**                                                                                                                           | **Przykład**                                                                                                                                                                                                                  |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Agenci refleksyjni prości**  | Wykonują natychmiastowe działania na podstawie wcześniej zdefiniowanych reguł.                                                    | Agent podróży interpretuje kontekst e-maila i przesyła skargi dotyczące podróży do obsługi klienta.                                                                                                                           |
| **Agenci refleksyjni oparte na modelu** | Wykonują działania na podstawie modelu świata i zmian w tym modelu.                                                                   | Agent podróży priorytetyzuje trasy z znaczącymi zmianami cen na podstawie dostępu do historycznych danych cenowych.                                                                                                         |
| **Agenci celowi**             | Tworzą plany, by osiągnąć konkretne cele, interpretując cel i określając działania do jego osiągnięcia.                           | Agent podróży rezerwuje podróż, określając niezbędne ustalenia (samochód, komunikacja publiczna, loty) z aktualnego miejsca do celu podróży.                                                                               |
| **Agenci opierający się na użyteczności** | Uwzględniają preferencje i ważone kompromisy liczbowo, by określić, jak osiągnąć cele.                                              | Agent podróży maksymalizuje użyteczność, ważąc wygodę kontra koszt przy rezerwacji podróży.                                                                                                                                    |
| **Agenci uczący się**          | Ulepszają się z czasem, reagując na sprzężenie zwrotne i dostosowując działania.                                                    | Agent podróży poprawia się, korzystając z opinii klientów z ankiet po podróży, aby wprowadzać zmiany do przyszłych rezerwacji.                                                                                                |
| **Agenci hierarchiczni**       | Posiadają wielu agentów w systemie warstwowym, gdzie wyższej rangi agenci dzielą zadania na podzadania dla niższej rangi agentów. | Agent podróży anuluje podróż, dzieląc zadanie na podzadania (np. anulowanie konkretnych rezerwacji) i przekazuje je agentom niższej rangi do wykonania, raportując z powrotem do agenta wyższego poziomu.                        |
| **Systemy wieloagentowe (MAS)** | Agenci wykonują zadania niezależnie, współpracując lub konkurując.                                                                 | Współpraca: Wiele agentów rezerwuje konkretne usługi podróżne, takie jak hotele, loty i rozrywka. Konkurencja: Wiele agentów zarządza i konkuruje o wspólny kalendarz rezerwacji hotelowych, aby zakwaterować klientów w hotelu. |

## Kiedy stosować Agentów AI

W poprzedniej sekcji używaliśmy przypadku agenta podróży, aby wyjaśnić, jak różne typy agentów mogą być używane w różnych scenariuszach rezerwacji podróży. Będziemy kontynuować używanie tej aplikacji przez cały kurs.

Spójrzmy na typy przypadków użycia, do których Agenci AI są najlepiej dopasowani:

![Kiedy stosować Agentów AI?](../../../translated_images/pl/when-to-use-ai-agents.54becb3bed74a479.webp)


- **Problemy o charakterze otwartym** - pozwalając LLM określić potrzebne kroki do wykonania zadania, ponieważ nie zawsze można je z góry zaprogramować w przepływie pracy.
- **Procesy wieloetapowe** - zadania wymagające stopnia złożoności, w których Agent AI musi korzystać z narzędzi lub informacji przez wiele etapów, a nie jednorazowe pobranie danych.  
- **Poprawa z czasem** - zadania, w których agent może się ulepszać z czasem, otrzymując informacje zwrotne zarówno od środowiska, jak i od użytkowników, aby zapewnić lepszą użyteczność.

Więcej rozważań dotyczących używania Agentów AI omawiamy w lekcji Budowanie Godnych Zaufania Agentów AI.

## Podstawy rozwiązań agentowych

### Tworzenie agenta

Pierwszym krokiem w projektowaniu systemu Agenta AI jest zdefiniowanie narzędzi, działań i zachowań. W tym kursie skupiamy się na używaniu **Azure AI Agent Service** do definiowania naszych Agentów. Oferuje on funkcje takie jak:

- Wybór otwartych modeli takich jak OpenAI, Mistral i Llama
- Korzystanie z licencjonowanych danych od dostawców takich jak Tripadvisor
- Stosowanie standaryzowanych narzędzi OpenAPI 3.0

### Wzorce agentowe

Komunikacja z LLM odbywa się poprzez zapytania (prompty). Ze względu na półautonomiczną naturę Agentów AI, nie zawsze jest możliwe lub konieczne ręczne ponowne zapytanie LLM po zmianie w środowisku. Używamy **wzorców agentowych**, które pozwalają na wieloetapowe zadawanie zapytań LLM w bardziej skalowalny sposób.

Ten kurs jest podzielony na niektóre z obecnie popularnych wzorców agentowych.

### Frameworki agentowe

Frameworki agentowe pozwalają programistom implementować wzorce agentowe przez kod. Frameworki te oferują szablony, wtyczki i narzędzia dla lepszej współpracy Agentów AI. Te korzyści umożliwiają lepszą obserwowalność i diagnostykę systemów Agentów AI.

W tym kursie zbadamy Microsoft Agent Framework (MAF) do tworzenia agentów AI gotowych do produkcji.

## Przykładowe kody

- Python: [Agent Framework](./code_samples/01-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/01-dotnet-agent-framework.md)

## Masz więcej pytań o Agentach AI?

Dołącz do [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), aby spotkać innych uczących się, uczestniczyć w godzinach konsultacji i uzyskać odpowiedzi na pytania dotyczące Agentów AI.

## Poprzednia lekcja

[Konfiguracja kursu](../00-course-setup/README.md)

## Następna lekcja

[Eksploracja Frameworków Agentowych](../02-explore-agentic-frameworks/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że staramy się zapewnić dokładność, prosimy pamiętać, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o istotnym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->