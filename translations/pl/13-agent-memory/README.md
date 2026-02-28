# Pamięć dla Agentów AI  
[![Agent Memory](../../../translated_images/pl/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Podczas omawiania unikalnych korzyści płynących z tworzenia Agentów AI, głównie porusza się dwie kwestie: możliwość korzystania z narzędzi do wykonywania zadań oraz zdolność do doskonalenia się z czasem. Pamięć stanowi fundament tworzenia samo-udoskonalającego się agenta, który może oferować lepsze doświadczenia naszym użytkownikom.

W tej lekcji przyjrzymy się, czym jest pamięć dla Agentów AI oraz jak możemy nią zarządzać i wykorzystywać ją na korzyść naszych aplikacji.

## Wprowadzenie

Ta lekcja obejmie:

• **Zrozumienie pamięci Agenta AI**: Czym jest pamięć i dlaczego jest kluczowa dla agentów.

• **Implementacja i przechowywanie pamięci**: Praktyczne metody dodawania funkcji pamięci do twoich agentów AI, ze szczególnym uwzględnieniem pamięci krótkotrwałej i długotrwałej.

• **Sprawienie, by Agenci AI się doskonalili**: Jak pamięć umożliwia agentom uczenie się na podstawie wcześniejszych interakcji i poprawianie się z czasem.

## Dostępne implementacje

Ta lekcja zawiera dwa wszechstronne samouczki w notebookach:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementuje pamięć korzystając z Mem0 oraz Azure AI Search z Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementuje ustrukturyzowaną pamięć używając Cognee, automatycznie budując graf wiedzy oparty na embeddingach, wizualizując graf i inteligentne wyszukiwanie

## Cele nauki

Po ukończeniu tej lekcji będziesz umiał:

• **Rozróżniać różne typy pamięci agenta AI**, w tym pamięć roboczą, krótkotrwałą i długotrwałą, a także specjalistyczne formy jak persona i pamięć epizodyczna.

• **Implementować i zarządzać pamięcią krótkotrwałą i długotrwałą dla agentów AI** używając Microsoft Agent Framework, wykorzystując narzędzia takie jak Mem0, Cognee, pamięć na tablicy oraz integrując się z Azure AI Search.

• **Rozumieć zasady stojące za samo-udoskonalającymi się agentami AI** oraz jak solidne systemy zarządzania pamięcią przyczyniają się do ciągłego uczenia się i adaptacji.

## Zrozumienie pamięci Agenta AI

W istocie **pamięć dla agentów AI odnosi się do mechanizmów umożliwiających im przechowywanie i przywoływanie informacji**. Informacje te mogą obejmować konkretne szczegóły rozmowy, preferencje użytkownika, wcześniejsze działania lub nawet wyuczone wzorce.

Bez pamięci aplikacje AI często są bezstanowe, co oznacza, że każda interakcja zaczyna się od nowa. Prowadzi to do powtarzalnego i frustrującego doświadczenia użytkownika, gdzie agent „zapomina” wcześniejszy kontekst lub preferencje.

### Dlaczego pamięć jest ważna?

Inteligencja agenta jest ściśle powiązana z jego zdolnością do przypominania i wykorzystywania wcześniejszych informacji. Pamięć umożliwia agentom bycie:

• **Refleksyjnymi**: Uczenie się na podstawie wcześniejszych działań i wyników.

• **Interaktywnymi**: Utrzymywanie kontekstu w trakcie bieżącej rozmowy.

• **Proaktywnymi i reaktywnymi**: Przewidywanie potrzeb lub adekwatne reagowanie na podstawie danych historycznych.

• **Autonomicznymi**: Działanie bardziej niezależne przez sięganie po zgromadzoną wiedzę.

Celem implementacji pamięci jest uczynienie agentów bardziej **niezawodnymi i kompetentnymi**.

### Typy pamięci

#### Pamięć robocza

Myśl o niej jak o kartce do notatek, którą agent używa podczas jednego, bieżącego zadania lub procesu myślowego. Przechowuje ona natychmiastowe informacje potrzebne do wykonania kolejnego kroku.

Dla agentów AI pamięć robocza często przechwytuje najistotniejsze informacje z rozmowy, nawet jeśli pełna historia czatu jest długa lub ucięta. Koncentruje się na wyłapywaniu kluczowych elementów, takich jak wymagania, propozycje, decyzje i działania.

**Przykład pamięci roboczej**

W agencie rezerwacji podróży pamięć robocza może przechwycić aktualne żądanie użytkownika, takie jak „Chcę zarezerwować wyjazd do Paryża”. Ten konkretny wymóg jest trzymany w bezpośrednim kontekście agenta, by kierować bieżącą interakcją.

#### Pamięć krótkotrwała

Ten typ pamięci przechowuje informacje przez czas trwania pojedynczej rozmowy lub sesji. Jest to kontekst obecnego czatu, pozwalający agentowi odnosić się do wcześniejszych wypowiedzi w dialogu.

**Przykład pamięci krótkotrwałej**

Jeśli użytkownik pyta: „Ile kosztuje lot do Paryża?” a potem dodaje: „A co z zakwaterowaniem tam?”, pamięć krótkotrwała zapewnia, że agent rozumie, iż „tam” odnosi się do „Paryża” w tej samej rozmowie.

#### Pamięć długotrwała

To informacje przetrzymujące się przez wiele rozmów lub sesji. Pozwala agentom pamiętać preferencje użytkownika, wcześniejsze interakcje lub ogólną wiedzę przez dłuższy czas. To ważne dla personalizacji.

**Przykład pamięci długotrwałej**

Pamięć długotrwała może przechowywać informacje, że „Ben lubi narciarstwo i aktywności na świeżym powietrzu, pije kawę z widokiem na góry i chce unikać zaawansowanych stoków ze względu na wcześniejszą kontuzję”. Ta wiedza, nabyta podczas poprzednich interakcji, wpływa na rekomendacje w przyszłych sesjach planowania podróży, czyniąc je wysoce spersonalizowanymi.

#### Pamięć persony

Ten specjalistyczny rodzaj pamięci pomaga agentowi rozwijać spójną „osobowość” lub „personę”. Pozwala agentowi pamiętać szczegóły o sobie lub swojej roli, co sprawia, że interakcje są płynniejsze i bardziej ukierunkowane.

**Przykład pamięci persony**  
Jeśli agent podróży jest zaprojektowany jako „ekspert od planowania narciarskiego”, pamięć persony może wzmacniać tę rolę, wpływając na odpowiedzi, by były zgodne z tonem i wiedzą eksperta.

#### Pamięć Workflow/Epizodyczna

Ta pamięć przechowuje sekwencję kroków podejmowanych przez agenta podczas złożonego zadania, włączając sukcesy i niepowodzenia. To jak pamiętanie konkretnych „epizodów” lub doświadczeń z przeszłości, aby się na nich uczyć.

**Przykład pamięci epizodycznej**

Jeśli agent próbował zarezerwować konkretny lot, ale nie powiodło się to z powodu braku dostępności, pamięć epizodyczna może zarejestrować tę porażkę, pozwalając agentowi spróbować alternatywnych lotów lub poinformować użytkownika o problemie w bardziej świadomy sposób podczas kolejnej próby.

#### Pamięć encji

Jej istotą jest wyodrębnianie i zapamiętywanie konkretnych encji (np. osób, miejsc lub przedmiotów) oraz wydarzeń z rozmów. Pozwala agentowi budować ustrukturyzowane rozumienie kluczowych elementów omawianych tematów.

**Przykład pamięci encji**

Z rozmowy o wcześniejszej podróży agent może wyodrębnić „Paryż”, „Wieżę Eiffla” oraz „kolację w restauracji Le Chat Noir” jako encje. W przyszłej interakcji agent mógłby przywołać „Le Chat Noir” i zaproponować nową rezerwację w tym miejscu.

#### Ustrukturyzowany RAG (Retrieval Augmented Generation)

Choć RAG to szersza technika, „Ustrukturyzowany RAG” jest podkreślany jako potężna technologia pamięci. Pozyskuje gęste, ustrukturyzowane informacje z różnych źródeł (rozmowy, e-maile, obrazy) i wykorzystuje je do zwiększenia precyzji, trafności i szybkości odpowiedzi. W przeciwieństwie do klasycznego RAG opierającego się wyłącznie na semantycznym podobieństwie, Ustrukturyzowany RAG operuje na inherentnej strukturze danych.

**Przykład ustrukturyzowanego RAG**

Zamiast jedynie dopasowywać słowa kluczowe, Ustrukturyzowany RAG mógłby wyodrębnić szczegóły lotu (cel, data, godzina, linia lotnicza) z e-maila i przechować je w ustrukturyzowanej formie. Pozwala to na precyzyjne zapytania, jak „Jakim lotem do Paryża poleciałem we wtorek?”.

## Implementacja i przechowywanie pamięci

Implementacja pamięci dla agentów AI obejmuje systematyczny proces **zarządzania pamięcią**, który zawiera generowanie, przechowywanie, wyszukiwanie, integrowanie, aktualizowanie, a nawet „zapominanie” (usuwanie) informacji. Szczególnie istotny jest aspekt wyszukiwania.

### Specjalistyczne narzędzia pamięci

#### Mem0

Jednym ze sposobów przechowywania i zarządzania pamięcią agenta jest korzystanie ze specjalistycznych narzędzi, takich jak Mem0. Mem0 działa jako trwała warstwa pamięci, pozwalając agentom przywoływać istotne interakcje, przechowywać preferencje użytkownika i kontekst faktograficzny oraz uczyć się na podstawie sukcesów i porażek w czasie. Idea jest taka, że agenci bezstanowi stają się agentami stanowymi.

Działa to poprzez **dwufazowy pipeline pamięci: ekstrakcję i aktualizację**. Najpierw wiadomości dodawane do wątku agenta są przesyłane do usługi Mem0, która wykorzystuje Duży Model Językowy (LLM) do podsumowania historii rozmowy i wyodrębnienia nowych wspomnień. Następnie faza aktualizacji, napędzana przez LLM, decyduje, czy dodawać, modyfikować, czy usuwać te wspomnienia, przechowując je w hybrydowej bazie danych, która może zawierać bazy wektorowe, grafowe i klucz-wartość. System ten wspiera różne typy pamięci oraz może integrować pamięć grafową do zarządzania relacjami między encjami.

#### Cognee

Innym potężnym podejściem jest użycie **Cognee**, otwartoźródłowej semantycznej pamięci dla agentów AI, która transformuje dane ustrukturyzowane i nieustrukturyzowane w zapytalne grafy wiedzy oparte na embeddingach. Cognee zapewnia **architekturę dualstore** łączącą wyszukiwanie podobieństwa wektorowego z relacjami w grafie, umożliwiając agentom zrozumienie nie tylko tego, co jest podobne, ale także jak pojęcia są ze sobą powiązane.

Wyróżnia się w **hybrydowym wyszukiwaniu**, które łączy podobieństwo wektorowe, strukturę grafową oraz rozumowanie LLM — od surowego wyszukiwania fragmentów do zadawania pytań świadomych grafu. System utrzymuje **żywą pamięć**, która ewoluuje i rośnie, pozostając przy tym zapytalnym, jako jeden połączony graf, wspierając zarówno krótkoterminowy kontekst sesji, jak i długotrwałą pamięć trwałą.

Samouczek w notebooku Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstruje budowanie tej zunifikowanej warstwy pamięci, z praktycznymi przykładami wprowadzania zróżnicowanych źródeł danych, wizualizacji grafu wiedzy oraz zapytań z różnymi strategiami wyszukiwania dostosowanymi do potrzeb agenta.

### Przechowywanie pamięci z RAG

Poza specjalistycznymi narzędziami pamięci, jak mem0, możesz wykorzystać solidne usługi wyszukiwania, takie jak **Azure AI Search jako backend do przechowywania i wyszukiwania wspomnień**, szczególnie dla ustrukturyzowanego RAG.

Pozwala to ugruntować odpowiedzi agenta w twoich własnych danych, zapewniając bardziej relewantne i precyzyjne odpowiedzi. Azure AI Search można używać do przechowywania specyficznych dla użytkownika wspomnień podróżnych, katalogów produktów lub dowolnej innej wiedzy specyficznej dla domeny.

Azure AI Search wspiera funkcje takie jak **Ustrukturyzowany RAG**, który znakomicie wyodrębnia i wyszukuje gęste, ustrukturyzowane informacje z dużych zestawów danych, jak historie rozmów, e-maile lub nawet obrazy. Dzięki temu zapewnia „nadludzką precyzję i trafność” w porównaniu do tradycyjnych metod dzielenia tekstu i embedowania.

## Sprawienie, by Agenci AI się doskonalili

Powszechnym wzorcem dla samo-udoskonalających się agentów jest wprowadzenie **„agenta wiedzy”**. Ten oddzielny agent obserwuje główną rozmowę między użytkownikiem a podstawowym agentem. Jego rola to:

1. **Identyfikacja cennych informacji**: Określenie, czy jakaś część rozmowy jest warta zapisania jako wiedza ogólna lub specyficzna preferencja użytkownika.

2. **Ekstrakcja i podsumowanie**: Wyodrębnienie kluczowej nauki lub preferencji z rozmowy.

3. **Przechowywanie w bazie wiedzy**: Zachowanie tych informacji, często w bazie wektorowej, aby można je było później odzyskać.

4. **Wzbogacanie przyszłych zapytań**: Gdy użytkownik inicjuje nowe zapytanie, agent wiedzy pobiera odpowiednie przechowywane informacje i dołącza je do promptu użytkownika, dostarczając ważny kontekst dla agenta głównego (podobnie jak RAG).

### Optymalizacje pamięci

• **Zarządzanie latencją**: Aby uniknąć spowalniania interakcji użytkownika, początkowo można użyć tańszego, szybszego modelu do szybkiego sprawdzenia, czy informacja jest warta przechowania lub wyszukania, wywołując proces ekstrakcji/wyszukiwania tylko w razie potrzeby.

• **Utrzymanie bazy wiedzy**: W przypadku rosnącej bazy wiedzy, rzadziej używane informacje można przenieść do „zimnego magazynu”, aby zmniejszyć koszty.

## Masz więcej pytań o pamięć agenta?

Dołącz do [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), aby spotkać się z innymi uczącymi się, uczestniczyć w godzinach konsultacji i uzyskać odpowiedzi na pytania dotyczące Agentów AI.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zrzeczenie się odpowiedzialności**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczeń AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy wszelkich starań, aby tłumaczenie było jak najdokładniejsze, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->