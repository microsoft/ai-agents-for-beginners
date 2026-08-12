# Pamięć dla agentów AI 
[![Agent Memory](../../../translated_images/pl/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

W dyskusjach na temat unikalnych korzyści tworzenia agentów AI głównie porusza się dwie kwestie: możliwość korzystania z narzędzi do realizacji zadań oraz zdolność do samodoskonalenia się z czasem. Pamięć stanowi fundament tworzenia samodoskonalącego się agenta, który może kreować lepsze doświadczenia dla naszych użytkowników.

W tej lekcji przyjrzymy się, czym jest pamięć dla agentów AI oraz jak możemy nią zarządzać i wykorzystywać ją z korzyścią dla naszych aplikacji.

## Wprowadzenie

Ta lekcja obejmuje:

• **Zrozumienie pamięci agentów AI**: Czym jest pamięć i dlaczego jest niezbędna dla agentów.

• **Implementacja i przechowywanie pamięci**: Praktyczne metody dodawania funkcji pamięci do twoich agentów AI, ze szczególnym uwzględnieniem pamięci krótkotrwałej i długotrwałej.

• **Tworzenie samodoskonalących się agentów AI**: Jak pamięć umożliwia agentom uczenie się na podstawie wcześniejszych interakcji i poprawianie się z czasem.

## Dostępne implementacje

W tej lekcji znajdziesz dwa obszerne samouczki w notebookach:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementuje pamięć za pomocą Mem0 oraz Azure AI Search wraz z Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementuje pamięć strukturalną z użyciem Cognee, automatycznie budując graf wiedzy oparty na embeddingach, wizualizując graf oraz inteligentne wyszukiwanie

## Cele nauki

Po ukończeniu tej lekcji będziesz potrafił:

• **Rozróżniać różne typy pamięci agentów AI**, w tym pamięć roboczą, krótkoterminową i długoterminową, a także specjalistyczne formy, takie jak pamięć persony i epizodyczna.

• **Implementować i zarządzać pamięcią krótkotrwałą i długotrwałą dla agentów AI**, wykorzystując Microsoft Agent Framework, korzystając z narzędzi takich jak Mem0, Cognee, pamięć tablicowa oraz integrując je z Azure AI Search.

• **Zrozumieć zasady działania samodoskonalących się agentów AI** oraz jak solidne systemy zarządzania pamięcią przyczyniają się do ciągłego uczenia się i adaptacji.

## Zrozumienie pamięci agentów AI

W swej istocie **pamięć agentów AI odnosi się do mechanizmów pozwalających im przechowywać i przypominać sobie informacje**. Te informacje mogą obejmować szczegółowe dane o rozmowie, preferencje użytkownika, wcześniejsze działania czy nawet wyuczone wzorce.

Bez pamięci aplikacje AI często są bezstanowe, co oznacza, że każda interakcja zaczyna się od zera. Prowadzi to do powtarzalnych i frustrujących doświadczeń użytkownika, gdzie agent „zapomina” poprzedni kontekst lub preferencje.

### Dlaczego pamięć jest ważna?

inteligencja agenta jest ściśle związana z jego zdolnością do przypominania i wykorzystywania wcześniejszych informacji. Pamięć pozwala agentom być:

• **Refleksyjnymi**: Uczą się na podstawie wcześniejszych działań i wyników.

• **Interaktywnymi**: Utrzymują kontekst podczas trwającej rozmowy.

• **Proaktywnymi i reaktywnymi**: Przewidują potrzeby lub odpowiednio reagują na podstawie danych historycznych.

• **Autonomicznymi**: Działają bardziej niezależnie, korzystając z przechowywanej wiedzy.

Celem implementacji pamięci jest uczynienie agentów bardziej **niezawodnymi i zdolnymi**.

### Typy pamięci

#### Pamięć robocza

Można ją przyrównać do kawałka papieru roboczego, którego agent używa podczas pojedynczego, trwającego zadania lub procesu myślowego. Przechowuje natychmiastowe informacje potrzebne do wykonania następnego kroku.

Dla agentów AI pamięć robocza często przechwytuje najbardziej istotne informacje z rozmowy, nawet jeśli pełna historia czatu jest długa lub ucięta. Koncentruje się na wydobywaniu kluczowych elementów, takich jak wymagania, propozycje, decyzje i działania.

**Przykład pamięci roboczej**

W agencie rezerwacji podróży pamięć robocza może przechwycić aktualne żądanie użytkownika, takie jak „Chcę zarezerwować wycieczkę do Paryża”. Ten konkretny wymóg jest utrzymywany w natychmiastowym kontekście agenta, by kierować bieżącą interakcją.

#### Pamięć krótkotrwała

Ten typ pamięci przechowuje informacje przez czas trwania pojedynczej rozmowy lub sesji. To kontekst aktualnego czatu, pozwalający agentowi odwołać się do wcześniejszych wypowiedzi w dialogu.

W przykładach SDK Pythona [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) odpowiada to `AgentSession`, tworzonemu przez `agent.create_session()`. Sesja jest wbudowaną pamięcią krótkotrwałą frameworka: utrzymuje kontekst rozmowy dostępnym dopóki ta sama sesja jest używana, ale ten kontekst nie jest zachowywany po zakończeniu sesji lub restarcie aplikacji. Do przechowywania faktów i preferencji, które muszą przetrwać między sesjami, stosuje się pamięć długotrwałą, zwykle poprzez bazę danych, indeks wektorowy lub inny trwały magazyn.

**Przykład pamięci krótkotrwałej**

Jeśli użytkownik zapyta „Ile kosztuje lot do Paryża?”, a potem doda „A jak z zakwaterowaniem tam?”, pamięć krótkotrwała zapewnia, że agent wie, iż „tam” odnosi się do „Paryża” w tej samej rozmowie.

#### Pamięć długotrwała

To informacje, które zachowują się przez wiele rozmów lub sesji. Pozwala agentom pamiętać preferencje użytkownika, historyczne interakcje lub ogólną wiedzę przez dłuższy czas. Jest to ważne dla personalizacji.

**Przykład pamięci długotrwałej**

Pamięć długotrwała może przechowywać informacje, że „Ben lubi narciarstwo i aktywności na świeżym powietrzu, lubi kawę z widokiem na góry i chce unikać zaawansowanych stoków narciarskich z powodu wcześniejszej kontuzji”. Ta informacja, pozyskana z wcześniejszych interakcji, wpływa na rekomendacje podczas kolejnych sesji planowania podróży, czyniąc je bardzo spersonalizowanymi.

#### Pamięć persony

Ten specjalistyczny typ pamięci pomaga agentowi rozwijać spójną „osobowość” lub „personę”. Pozwala agentowi pamiętać szczegóły na swój temat lub dotyczące jego zamierzonej roli, co sprawia, że interakcje są bardziej płynne i ukierunkowane.

**Przykład pamięci persony**
Jeśli agent podróży jest zaprojektowany jako „ekspert od planowania narciarskiego”, pamięć persony może wzmocnić tę rolę, wpływając na odpowiedzi, by odpowiadały tonowi i wiedzy eksperta.

#### Pamięć przepływu pracy/epizodyczna

Ta pamięć przechowuje sekwencję kroków wykonywanych przez agenta podczas złożonego zadania, włączając sukcesy i porażki. To jak zapamiętywanie konkretnych „epizodów” lub poprzednich doświadczeń, aby się na nich uczyć.

**Przykład pamięci epizodycznej**

Jeśli agent próbował zarezerwować konkretny lot, ale nie udało się z powodu braku dostępności, pamięć epizodyczna może zanotować tę porażkę, pozwalając agentowi próbować alternatywnych lotów lub poinformować użytkownika o problemie w bardziej świadomy sposób przy kolejnej próbie.

#### Pamięć encji

Polega na wydobywaniu i zapamiętywaniu konkretnych encji (jak osoby, miejsca czy przedmioty) oraz zdarzeń z rozmów. Pozwala agentowi zbudować strukturalne rozumienie kluczowych elementów omawianych w dialogu.

**Przykład pamięci encji**

Z rozmowy o przeszłej podróży agent może wyodrębnić „Paryż”, „Wieża Eiffla” oraz „kolacja w restauracji Le Chat Noir” jako encje. W przyszłej interakcji agent mógłby przypomnieć „Le Chat Noir” i zaoferować dokonanie nowej rezerwacji tam.

#### Strukturalne RAG (Retrieval Augmented Generation)

Choć RAG to technika ogólna, „Strukturalne RAG” jest wyróżniane jako potężna technologia pamięci. Wydobywa gęste, strukturalne informacje z różnych źródeł (rozmów, maili, obrazów) i wykorzystuje je do zwiększenia precyzji, przypominania i szybkości odpowiedzi. W przeciwieństwie do klasycznego RAG, który bazuje wyłącznie na semantycznym podobieństwie, Strukturalne RAG pracuje z wrodzoną strukturą informacji.

**Przykład strukturalnego RAG**

Zamiast dopasowywać tylko słowa kluczowe, Strukturalne RAG może analizować szczegóły lotu (miejsce docelowe, data, godzina, linia lotnicza) z maila i przechowywać je w sposób strukturalny. Umożliwia to precyzyjne zapytania, takie jak „Jaki lot zarezerwowałem do Paryża na wtorek?”

## Implementacja i przechowywanie pamięci

Implementacja pamięci dla agentów AI obejmuje systematyczny proces **zarządzania pamięcią**, który zawiera generowanie, przechowywanie, pobieranie, integrowanie, aktualizowanie, a nawet „zapominanie” (lub usuwanie) informacji. Pobieranie jest szczególnie kluczowym elementem.

### Specjalistyczne narzędzia pamięci

#### Mem0

Jednym ze sposobów przechowywania i zarządzania pamięcią agenta jest użycie specjalistycznych narzędzi jak Mem0. Mem0 działa jako trwała warstwa pamięci, pozwalając agentom przypominać sobie istotne interakcje, przechowywać preferencje użytkownika oraz kontekst faktów, a także uczyć się na podstawie sukcesów i porażek z czasem. Ideą jest przemiana agentów bezstanowych w stanowych.

Działa przez **dwufazowy proces pamięci: ekstrakcję i aktualizację**. Najpierw wiadomości dodawane do wątku agenta są wysyłane do usługi Mem0, która używa Large Language Model (LLM) do podsumowania historii rozmowy i wydobycia nowych wspomnień. Następnie faza aktualizacji sterowana przez LLM decyduje, czy dodać, zmodyfikować lub usunąć te wspomnienia, przechowując je w hybrydowym magazynie danych, który może obejmować bazy danych wektorowych, grafowych i klucz-wartość. System ten wspiera różne typy pamięci oraz może integrować pamięć grafową do zarządzania relacjami między encjami.

#### Cognee

Innym potężnym podejściem jest użycie **Cognee**, otwartoźródłowej pamięci semantycznej dla agentów AI, która przekształca dane strukturalne i niestrukturalne w zapytalne grafy wiedzy oparte na embeddingach. Cognee zapewnia **architekturę podwójnego magazynu** łączącą wyszukiwanie według podobieństwa wektorowego z relacjami grafu, umożliwiając agentom zrozumienie nie tylko podobieństwa informacji, ale także powiązań między koncepcjami.

System doskonale radzi sobie z **hybrydowym pobieraniem**, które łączy podobieństwo wektorów, strukturę grafu i rozumowanie LLM - od prostego wyszukiwania fragmentów po odpowiadanie na pytania z uwzględnieniem grafu. System utrzymuje **żywą pamięć**, która ewoluuje i rośnie, pozostając jednocześnie zapytalnym, jako jeden połączony graf, wspierając zarówno kontekst sesji krótkoterminowej, jak i pamięć trwałą.

Samouczek w notebooku Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstruje budowę tej zunifikowanej warstwy pamięci, z praktycznymi przykładami przetwarzania różnych źródeł danych, wizualizacji grafu wiedzy i zapytań z różnymi strategiami wyszukiwania dostosowanymi do potrzeb agentów.

### Przechowywanie pamięci z RAG

Poza specjalistycznymi narzędziami pamięci jak Mem0, można wykorzystać solidne usługi wyszukiwania jak **Azure AI Search jako backend do przechowywania i pobierania wspomnień**, zwłaszcza dla strukturalnego RAG.

Pozwala to ufundować odpowiedzi agenta własnymi danymi, zapewniając bardziej trafne i dokładne odpowiedzi. Azure AI Search może być używany do przechowywania pamięci podróży użytkownika, katalogów produktów lub innej wiedzy specyficznej dla danej dziedziny.

Azure AI Search obsługuje takie możliwości jak **Strukturalne RAG**, które znacznie poprawia wydobywanie i pobieranie gęstych, strukturalnych informacji z dużych zbiorów danych, takich jak historie rozmów, maile czy nawet obrazy. Dostarcza to „nadzwyczajną precyzję i przypominanie” w porównaniu z tradycyjnym dzieleniem tekstu na fragmenty i embeddingami.

## Tworzenie samodoskonalących się agentów AI

Powszechny wzorzec samodoskonalących się agentów polega na wprowadzeniu **„agenta wiedzy”**. Ten oddzielny agent obserwuje główną rozmowę między użytkownikiem a agentem głównym. Jego rolą jest:

1. **Identyfikacja wartościowych informacji**: Określenie, czy jakaś część rozmowy jest warta zapisania jako ogólna wiedza lub konkretna preferencja użytkownika.

2. **Ekstrakcja i podsumowanie**: Wyodrębnienie istotnej nauki lub preferencji z rozmowy.

3. **Przechowywanie w bazie wiedzy**: Zachowanie wyodrębnionych informacji, często w bazie wektorowej, aby można je było później pobrać.

4. **Wzbogacanie przyszłych zapytań**: Kiedy użytkownik inicjuje nowe zapytanie, agent wiedzy pobiera odpowiednie przechowane informacje i dołącza je do polecenia użytkownika, zapewniając kluczowy kontekst agentowi głównemu (podobnie jak RAG).

### Optymalizacje dla pamięci

• **Zarządzanie opóźnieniami**: Aby uniknąć spowalniania interakcji użytkownika, można początkowo użyć tańszego, szybszego modelu do szybkiego sprawdzania, czy warto przechować lub pobrać daną informację, a wywołanie bardziej złożonego procesu ekstrakcji/pobierania następuje tylko w razie potrzeby.

• **Utrzymanie bazy wiedzy**: W przypadku rosnącej bazy wiedzy, rzadziej używane informacje można przenosić do „zimnego magazynu”, aby zarządzać kosztami.

## Masz więcej pytań na temat pamięci agenta?

Dołącz do [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), aby spotkać innych uczących się, uczestniczyć w godzinach konsultacji i uzyskać odpowiedzi na pytania dotyczące agentów AI.
## Poprzednia lekcja

[Inżynieria kontekstu dla agentów AI](../12-context-engineering/README.md)

## Następna lekcja

[Eksploracja Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->