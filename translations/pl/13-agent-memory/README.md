# Pamięć dla Agentów AI  
[![Agent Memory](../../../translated_images/pl/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Gdy rozmawiamy o unikalnych korzyściach tworzenia Agentów AI, głównie omawiane są dwie kwestie: możliwość wywoływania narzędzi do realizacji zadań oraz zdolność do ulepszania się w czasie. Pamięć stanowi podstawę tworzenia samo-ulepszających się agentów, którzy mogą tworzyć lepsze doświadczenia dla naszych użytkowników.

W tej lekcji przyjrzymy się, czym jest pamięć dla Agentów AI oraz jak nią zarządzać i wykorzystywać ją na korzyść naszych aplikacji.

## Wprowadzenie

Ta lekcja obejmie:

• **Zrozumienie pamięci agentów AI**: Czym jest pamięć i dlaczego jest niezbędna dla agentów.

• **Implementacja i przechowywanie pamięci**: Praktyczne metody dodawania funkcji pamięci do agentów AI, ze szczególnym naciskiem na pamięć krótkotrwałą i długotrwałą.

• **Czynienie agentów AI samo-ulepszającymi się**: Jak pamięć umożliwia agentom uczenie się na podstawie wcześniejszych interakcji i poprawianie się w czasie.

## Dostępne implementacje

Ta lekcja zawiera dwa kompleksowe samouczki w notatnikach:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementuje pamięć za pomocą Mem0 i Azure AI Search z Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementuje strukturalną pamięć za pomocą Cognee, automatycznie budując graf wiedzy oparty na embeddingach, wizualizując graf i inteligentne wyszukiwanie

## Cele nauki

Po ukończeniu tej lekcji będziesz potrafił:

• **Różnicować różne typy pamięci agenta AI**, w tym pamięć roboczą, krótkoterminową i długoterminową, a także specjalistyczne formy, takie jak pamięć osobowościowa i epizodyczna.

• **Implementować i zarządzać pamięcią krótkoterminową i długoterminową dla agentów AI** za pomocą Microsoft Agent Framework, wykorzystując narzędzia takie jak Mem0, Cognee, pamięć Whiteboard oraz integrując z Azure AI Search.

• **Zrozumieć zasady działania samo-ulepszających się agentów AI** i jak solidne systemy zarządzania pamięcią przyczyniają się do ciągłego uczenia się i adaptacji.

## Zrozumienie pamięci agenta AI

W swojej istocie **pamięć dla agentów AI odnosi się do mechanizmów pozwalających im przechowywać i przypominać informacje**. Mogą to być konkretne szczegóły dotyczące rozmowy, preferencje użytkownika, wcześniejsze działania lub nawet wyuczone wzorce.

Bez pamięci aplikacje AI często są bezstanowe, co oznacza, że każda interakcja zaczyna się od zera. Prowadzi to do powtarzalnego i frustrującego doświadczenia użytkownika, gdzie agent „zapomina” poprzedni kontekst lub preferencje.

### Dlaczego pamięć jest ważna?

Inteligencja agenta jest głęboko powiązana z jego zdolnością do przypominania i wykorzystywania wcześniejszych informacji. Pamięć pozwala agentom być:

• **Refleksyjnymi**: Uczyć się na podstawie wcześniejszych działań i wyników.

• **Interaktywnymi**: Utrzymywać kontekst podczas trwającej rozmowy.

• **Proaktywnymi i reaktywnymi**: Przewidywać potrzeby lub odpowiednio reagować na podstawie danych historycznych.

• **Autonomicznymi**: Działać bardziej niezależnie, odwołując się do zapisanej wiedzy.

Celem implementacji pamięci jest uczynienie agentów bardziej **wiarygodnymi i zdolnymi**.

### Typy pamięci

#### Pamięć robocza

Traktuj ją jak kartkę do notatek, którą agent używa podczas pojedynczego, trwającego zadania lub procesu myślowego. Przechowuje bezpośrednie informacje potrzebne do obliczenia następnego kroku.

Dla agentów AI pamięć robocza często przechwytuje najistotniejsze informacje z rozmowy, nawet jeśli pełna historia czatu jest długa lub skrócona. Skupia się na wyodrębnianiu kluczowych elementów, takich jak wymagania, propozycje, decyzje i działania.

**Przykład pamięci roboczej**

W agencie do rezerwacji podróży pamięć robocza może przechwytywać aktualne żądanie użytkownika, np. "Chcę zarezerwować podróż do Paryża". Ten konkretny wymóg jest przechowywany w bieżącym kontekście agenta, aby kierować obecną interakcją.

#### Pamięć krótkoterminowa

Ten typ pamięci przechowuje informacje przez czas trwania jednej rozmowy lub sesji. To kontekst bieżącego czatu, pozwalający agentowi odwoływać się do wcześniejszych wymian w dialogu.

W przykładach Python SDK [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) odpowiada to `AgentSession`, tworzonemu przez `agent.create_session()`. Sesja stanowi wbudowaną pamięć krótkoterminową frameworka: utrzymuje kontekst rozmowy dostępnym podczas korzystania z tej samej sesji, ale ten kontekst nie jest zachowywany, gdy sesja kończy się lub aplikacja restartuje. Używaj pamięci długoterminowej do faktów i preferencji, które muszą przetrwać między sesjami, zwykle przez bazę danych, indeks wektorowy lub inne trwałe repozytorium.

**Przykład pamięci krótkoterminowej**

Jeśli użytkownik pyta „Ile kosztuje lot do Paryża?” a potem dodaje „A co z zakwaterowaniem tam?”, pamięć krótkoterminowa zapewnia, że agent wie, iż „tam” odnosi się do „Paryża” w trakcie tej samej rozmowy.

#### Pamięć długoterminowa

To informacje przechowywane przez wiele rozmów lub sesji. Pozwala agentom zapamiętywać preferencje użytkownika, historyczne interakcje lub ogólną wiedzę przez długi czas. Ma to znaczenie w personalizacji.

**Przykład pamięci długoterminowej**

Pamięć długoterminowa mogłaby przechowywać, że „Ben lubi narciarstwo i aktywności na świeżym powietrzu, pije kawę z widokiem na góry i unika zaawansowanych tras narciarskich ze względu na wcześniejszą kontuzję”. Informacje te, wyuczone z poprzednich interakcji, wpływają na rekomendacje w przyszłych sesjach planowania podróży, czyniąc je bardzo spersonalizowanymi.

#### Pamięć osobowościowa

Ten specjalistyczny typ pamięci pomaga agentowi rozwijać spójną „osobowość” lub „personę”. Pozwala agentowi pamiętać szczegóły o sobie lub swojej przypisanej roli, czyniąc interakcje bardziej płynnymi i ukierunkowanymi.

**Przykład pamięci osobowościowej**  
Jeśli agent podróżniczy ma być „ekspertem od planowania nart”, pamięć osobowościowa może utrwalać tę rolę, wpływając na jego odpowiedzi tak, by odpowiadały tonowi i wiedzy eksperta.

#### Pamięć workflow/epizodyczna

Ta pamięć przechowuje sekwencję kroków podejmowanych przez agenta podczas złożonego zadania, włącznie z sukcesami i porażkami. To jak zapamiętywanie konkretnych „epizodów” lub doświadczeń, by się na nich uczyć.

**Przykład pamięci epizodycznej**

Jeśli agent próbuje zarezerwować konkretny lot, ale mu się to nie udaje z powodu braku dostępności, pamięć epizodyczna może zarejestrować tę porażkę, dzięki czemu agent może spróbować alternatywnych lotów lub poinformować użytkownika o problemie w bardziej świadomy sposób przy kolejnej próbie.

#### Pamięć encji

Polega na wyodrębnianiu i zapamiętywaniu konkretnych encji (takich jak osoby, miejsca czy przedmioty) oraz wydarzeń z rozmów. Pozwala agentowi zbudować ustrukturyzowane rozumienie kluczowych elementów omawianych tematów.

**Przykład pamięci encji**

Z rozmowy o przeszłej podróży agent może wyciągnąć „Paryż”, „Wieża Eiffla” oraz „kolacja w restauracji Le Chat Noir” jako encje. W przyszłej interakcji agent może przypomnieć „Le Chat Noir” i zaproponować dokonanie nowej rezerwacji tam.

#### Strukturalny RAG (Retrieval Augmented Generation)

Chociaż RAG to szersza technika, „Strukturalny RAG” jest wyróżniany jako potężna technologia pamięci. Wydobywa gęste, strukturalne informacje z różnych źródeł (rozmowy, e-maile, obrazy) i wykorzystuje je do zwiększenia precyzji, trafności i szybkości odpowiedzi. W przeciwieństwie do klasycznego RAG, który polega wyłącznie na semantycznym podobieństwie, Strukturalny RAG działa z wrodzoną strukturą informacji.

**Przykład Strukturalnego RAG**

Zamiast tylko dopasowywać słowa kluczowe, Strukturalny RAG może wyodrębnić szczegóły lotu (cel, data, godzina, linia lotnicza) z e-maila i przechowywać je w ustrukturyzowany sposób. Pozwala to na precyzyjne zapytania, takie jak „Jaki lot zarezerwowałem do Paryża na wtorek?”

## Implementacja i przechowywanie pamięci

Implementacja pamięci dla agentów AI wymaga systematycznego procesu **zarządzania pamięcią**, który obejmuje generowanie, przechowywanie, wyszukiwanie, integrowanie, aktualizowanie, a nawet „zapominanie” (lub usuwanie) informacji. Wyszukiwanie jest tu szczególnie kluczowym aspektem.

### Specjalistyczne narzędzia pamięci

#### Mem0

Jednym ze sposobów przechowywania i zarządzania pamięcią agenta jest użycie specjalistycznych narzędzi takich jak Mem0. Mem0 działa jako trwała warstwa pamięci, pozwalając agentom przypominać sobie istotne interakcje, przechowywać preferencje użytkownika i faktyczny kontekst oraz uczyć się na sukcesach i porażkach z czasem. Ideą jest, że agenci bezstanowi stają się stanowi.

Funkcjonuje poprzez **dwufazowy proces pamięci: ekstrakcję i aktualizację**. Najpierw wiadomości dodawane do wątku agenta są wysyłane do usługi Mem0, która używa dużego modelu językowego (LLM), by podsumować historię rozmowy i wydobyć nowe wspomnienia. Następnie faza aktualizacji napędzana LLM decyduje, czy te wspomnienia dodać, zmodyfikować lub usunąć, przechowując je w hybrydowym magazynie danych, który może zawierać bazy wektorowe, grafowe i klucz-wartość. System ten wspiera też różne typy pamięci i może integrować pamięć grafową do zarządzania relacjami między encjami.

#### Cognee

Innym potężnym podejściem jest użycie **Cognee**, otwartoźródłowej semantycznej pamięci dla agentów AI, która zamienia dane strukturalne i niestrukturalne w zapytania grafowe wiedzy oparte na embeddingach. Cognee zapewnia **architekturę dual-store**, łączącą wyszukiwanie podobieństwa wektorowego z zależnościami grafu, umożliwiając agentom rozumienie nie tylko podobieństwa informacji, ale też relacji między pojęciami.

Sprawdza się doskonale w **hybrydowym wyszukiwaniu**, które łączy podobieństwo wektorowe, strukturę grafu i rozumowanie LLM – od zwykłego wyszukiwania fragmentów po świadome grafowo odpowiadanie na pytania. System utrzymuje **żywą pamięć** rozwijającą się i rosnącą, pozostając dostępną jako jeden powiązany graf, wspierający zarówno kontekst krótkoterminowy sesji, jak i trwałą pamięć długoterminową.

Notatnik Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstruje budowanie tej zunifikowanej warstwy pamięci, z praktycznymi przykładami pobierania różnych źródeł danych, wizualizacji grafu wiedzy oraz zapytań z zastosowaniem różnych strategii dopasowanych do potrzeb agentów.

### Przechowywanie pamięci za pomocą RAG

Poza specjalistycznymi narzędziami pamięci jak mem0 , możesz wykorzystać solidne usługi wyszukiwania, takie jak **Azure AI Search jako backend do przechowywania i wyszukiwania wspomnień**, szczególnie w kontekście strukturalnego RAG.

Pozwala to ugruntować odpowiedzi agenta na własnych danych, zapewniając bardziej trafne i dokładne odpowiedzi. Azure AI Search może być używany do przechowywania pamięci podróży specyficznych dla użytkownika, katalogów produktów lub jakiejkolwiek innej domenowej wiedzy.

Azure AI Search wspiera funkcje takie jak **Strukturalny RAG**, który doskonale wydobywa i przywołuje gęste, strukturalne informacje z dużych zbiorów danych takich jak historia rozmów, e-maile czy nawet obrazy. Zapewnia to „ponadludzką precyzję i trafność” w porównaniu do tradycyjnych podejść opartych na dzieleniu tekstu na fragmenty i embeddingach.

## Umożliwienie agentom AI samo-ulepszania się

Powszechny wzorzec dla samo-ulepszających się agentów obejmuje wprowadzenie **„agenta wiedzy”**. Ten odrębny agent obserwuje główną rozmowę między użytkownikiem a podstawowym agentem. Jego rolą jest:

1. **Identyfikacja cennych informacji**: Określenie, czy jakaś część rozmowy jest warta zapisania jako ogólna wiedza lub konkretna preferencja użytkownika.

2. **Wydobycie i podsumowanie**: Wyekstrahowanie istotnej nauki lub preferencji z rozmowy.

3. **Przechowanie w bazie wiedzy**: Zachowanie tych informacji, często w bazie wektorowej, aby można je było później przywołać.

4. **Rozszerzanie przyszłych zapytań**: Gdy użytkownik inicjuje nowe zapytanie, agent wiedzy przywołuje odpowiednie zapisane informacje i dołącza je do promptu użytkownika, dostarczając kluczowego kontekstu głównemu agentowi (podobnie jak w RAG).

### Optymalizacje pamięci

• **Zarządzanie opóźnieniami**: Aby nie spowalniać interakcji użytkownika, początkowo można użyć tańszego i szybszego modelu, który szybko sprawdzi, czy informacja jest warta zapisania lub przywołania, odwołując się do bardziej złożonych procesów ekstrakcji/wyszukiwania tylko wtedy, gdy to konieczne.

• **Utrzymanie bazy wiedzy**: Dla rosnącej bazy wiedzy informacje używane rzadziej mogą być przenoszone do „zimnego przechowywania” w celu obniżenia kosztów.

## Masz więcej pytań o pamięć agentów?

Dołącz do [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), aby spotkać innych uczących się, uczestniczyć w godzinach konsultacji i uzyskać odpowiedzi na pytania dotyczące agentów AI.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->