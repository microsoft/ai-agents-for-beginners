# Pamięć dla Agentów AI  
[![Agent Memory](../../../translated_images/pl/lesson-13-thumbnail.959e3bc52d210c64.webp)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Podczas omawiania unikalnych zalet tworzenia Agentów AI, najczęściej poruszane są dwie kwestie: zdolność do korzystania z narzędzi do realizacji zadań oraz zdolność do doskonalenia się z czasem. Pamięć stanowi podstawę tworzenia agenta zdolnego do samodzielnej poprawy, który może tworzyć lepsze doświadczenia dla naszych użytkowników.

W tej lekcji przyjrzymy się, czym jest pamięć dla Agentów AI oraz jak możemy nią zarządzać i wykorzystywać ją na korzyść naszych aplikacji.

## Wprowadzenie

Ta lekcja obejmie:

• **Zrozumienie pamięci agenta AI**: Czym jest pamięć i dlaczego jest niezbędna dla agentów.

• **Implementacja i przechowywanie pamięci**: Praktyczne metody dodawania możliwości pamięci do twoich agentów AI, skoncentrowane na pamięci krótkoterminowej i długoterminowej.

• **Tworzenie agentów AI zdolnych do samodoskonalenia**: Jak pamięć umożliwia agentom uczenie się na podstawie wcześniejszych interakcji i doskonalenie z czasem.

## Dostępne Implementacje

Ta lekcja zawiera dwa obszerne samouczki w notebookach:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementuje pamięć przy użyciu Mem0 i Azure AI Search z Microsoft Agent Framework

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementuje strukturalną pamięć używając Cognee, automatycznie budując graf wiedzy oparty na embeddingach, wizualizując graf i inteligentne wyszukiwanie

## Cele Nauki

Po ukończeniu tej lekcji będziesz umiał:

• **Rozróżniać różne typy pamięci agentów AI**, w tym pamięć roboczą, krótkoterminową i długoterminową, a także specjalizowane formy, takie jak pamięć persony i epizodyczna.

• **Implementować i zarządzać pamięcią krótkoterminową i długoterminową dla agentów AI** z użyciem Microsoft Agent Framework, korzystając z narzędzi takich jak Mem0, Cognee, pamięć Whiteboard oraz integrując z Azure AI Search.

• **Zrozumieć zasady stojące za samo-uczącymi się agentami AI** oraz jak solidne systemy zarządzania pamięcią przyczyniają się do ciągłego uczenia się i adaptacji.

## Zrozumienie pamięci agenta AI

W swojej istocie, **pamięć dla agentów AI odnosi się do mechanizmów pozwalających im zatrzymywać i przypominać informacje**. Mogą to być szczegółowe dane dotyczące rozmowy, preferencje użytkownika, wcześniejsze działania lub nawet wyuczone wzorce.

Bez pamięci aplikacje AI często są bezstanowe, co oznacza, że każda interakcja zaczyna się od nowa. Prowadzi to do powtarzalnych i frustrujących doświadczeń użytkownika, gdzie agent "zapomina" poprzedni kontekst lub preferencje.

### Dlaczego pamięć jest ważna?

Inteligencja agenta jest ściśle związana z jego zdolnością do przypominania i wykorzystywania wcześniejszych informacji. Pamięć pozwala agentom być:

• **Refleksyjnymi**: Uczyć się na podstawie wcześniejszych działań i wyników.

• **Interaktywnymi**: Utrzymywać kontekst w trakcie trwającej rozmowy.

• **Proaktywnymi i reaktywnymi**: Przewidywać potrzeby lub odpowiednio reagować na podstawie danych historycznych.

• **Autonomicznymi**: Działać bardziej niezależnie, bazując na zgromadzonej wiedzy.

Celem implementacji pamięci jest uczynienie agentów bardziej **niezawodnymi i zdolnymi**.

### Typy pamięci

#### Pamięć robocza

Można ją porównać do kartki do notowania, którą agent używa podczas pojedynczego, bieżącego zadania lub procesu myślowego. Zawiera ona natychmiastowe informacje potrzebne do wyliczenia następnego kroku.

Dla agentów AI pamięć robocza często przechwytuje najbardziej istotne informacje z rozmowy, nawet jeśli pełna historia czatu jest długa lub ucięta. Skupia się na wyodrębnianiu kluczowych elementów, takich jak wymagania, propozycje, decyzje i działania.

**Przykład pamięci roboczej**

W agencie rezerwacji podróży, pamięć robocza może przechwytywać bieżące zapytanie użytkownika, na przykład „Chcę zarezerwować wycieczkę do Paryża”. Ten konkretny wymóg jest utrzymywany w bezpośrednim kontekście agenta, by pokierować obecną interakcją.

#### Pamięć krótkoterminowa

Ten typ pamięci przechowuje informacje przez czas trwania pojedynczej rozmowy lub sesji. To kontekst aktualnej rozmowy, pozwalający agentowi odnosić się do poprzednich wypowiedzi.

**Przykład pamięci krótkoterminowej**

Jeśli użytkownik zapyta „Ile kosztuje lot do Paryża?”, a następnie doda „A co z zakwaterowaniem tam?”, pamięć krótkoterminowa zapewnia, że agent rozumie, iż „tam” odnosi się do „Paryża” w ramach tej samej rozmowy.

#### Pamięć długoterminowa

To informacje, które utrzymują się przez wiele rozmów lub sesji. Pozwala agentom zapamiętywać preferencje użytkownika, historyczne interakcje lub ogólną wiedzę przez dłuższy czas. Jest to istotne dla personalizacji.

**Przykład pamięci długoterminowej**

Pamięć długoterminowa może przechowywać informacje takie jak „Ben lubi narciarstwo i aktywności na świeżym powietrzu, pije kawę z widokiem na góry i chce unikać zaawansowanych stoków narciarskich z powodu przeszłej kontuzji”. Ta wiedza, pozyskana z wcześniejszych interakcji, wpływa na rekomendacje podczas przyszłych sesji planowania podróży, co sprawia, że są one bardzo spersonalizowane.

#### Pamięć persony

Ten specjalizowany typ pamięci pomaga agentowi rozwijać spójną „osobowość” lub „personę”. Pozwala agentowi zapamiętywać szczegóły dotyczące samego siebie lub swojej roli, sprawiając, że interakcje stają się płynniejsze i bardziej ukierunkowane.

**Przykład pamięci persony**

Jeśli agent podróży jest zaprojektowany jako „ekspert od planowania narciarskiego”, pamięć persony może wzmacniać tę rolę, wpływając na odpowiedzi, aby były zgodne z tonem i wiedzą eksperta.

#### Pamięć workflow/epizodyczna

Ta pamięć przechowuje sekwencję kroków podejmowanych przez agenta podczas skomplikowanego zadania, włącznie z sukcesami i porażkami. To jak pamiętanie konkretnych „epizodów” lub doświadczeń, by się na nich uczyć.

**Przykład pamięci epizodycznej**

Jeśli agent próbował zarezerwować konkretny lot, ale nie powiodło się z powodu braku dostępności, pamięć epizodyczna może zarejestrować tę porażkę, umożliwiając agentowi próbowanie alternatywnych przelotów lub informowanie użytkownika o problemie w bardziej świadomy sposób podczas kolejnej próby.

#### Pamięć encji

Dotyczy ona wydobywania i zapamiętywania konkretnych encji (takich jak osoby, miejsca lub rzeczy) oraz wydarzeń z rozmów. Pozwala agentowi zbudować strukturalne zrozumienie kluczowych elementów dyskutowanych w rozmowie.

**Przykład pamięci encji**

Z rozmowy o przeszłej podróży agent może wyłowić „Paryż”, „Wieża Eiffla” oraz „kolacja w restauracji Le Chat Noir” jako encje. W przyszłej interakcji agent może przypomnieć „Le Chat Noir” i zaproponować dokonanie nowej rezerwacji.

#### Strukturalny RAG (Retrieval Augmented Generation)

Chociaż RAG jest szeroką techniką, „Strukturalny RAG” jest wyróżniany jako potężna technologia pamięci. Wydobywa gęste, ustrukturyzowane informacje z różnych źródeł (rozmów, e-maili, obrazów) i wykorzystuje je do poprawy precyzji, trafności i szybkości odpowiedzi. W przeciwieństwie do klasycznego RAG, który opiera się wyłącznie na podobieństwie semantycznym, Strukturalny RAG korzysta z wrodzonej struktury informacji.

**Przykład Strukturalnego RAG**

Zamiast tylko dopasowywać słowa kluczowe, Strukturalny RAG może analizować szczegóły lotu (cel, data, godzina, linia lotnicza) z e-maila i zapisywać je w ustrukturyzowany sposób. Pozwala to na precyzyjne zapytania, takie jak „Jaki lot zarezerwowałem do Paryża we wtorek?”

## Implementacja i przechowywanie pamięci

Implementacja pamięci dla agentów AI obejmuje systematyczny proces **zarządzania pamięcią**, który obejmuje generowanie, przechowywanie, wyszukiwanie, integrację, aktualizację, a nawet „zapominanie” (lub usuwanie) informacji. Wyszukiwanie jest szczególnie kluczowym aspektem.

### Specjalizowane narzędzia pamięci

#### Mem0

Jednym ze sposobów przechowywania i zarządzania pamięcią agenta jest użycie specjalizowanych narzędzi, takich jak Mem0. Mem0 działa jako trwała warstwa pamięci, umożliwiając agentom przypominanie sobie istotnych interakcji, przechowywanie preferencji użytkownika i faktograficznego kontekstu oraz uczenie się na podstawie sukcesów i porażek w czasie. Idea jest taka, że bezstanowi agenci stają się stanowymi.

Działa przez **dwufazowy pipeline pamięci: ekstrakcję i aktualizację**. Najpierw wiadomości dodane do wątku agenta są wysyłane do usługi Mem0, która przy użyciu Dużego Modelu Językowego (LLM) podsumowuje historię rozmowy i wyodrębnia nowe wspomnienia. Następnie faza aktualizacji sterowana przez LLM decyduje, czy dodać, zmodyfikować czy usunąć te wspomnienia, przechowując je w hybrydowej bazie danych, która może obejmować bazy wektorowe, grafowe i klucz-wartość. System ten wspiera także różne typy pamięci i może integrować pamięć grafową do zarządzania relacjami między encjami.

#### Cognee

Innym potężnym podejściem jest użycie **Cognee**, otwartoźródłowej pamięci semantycznej dla agentów AI, która zamienia dane strukturalne i niestrukturalne w zapytalne grafy wiedzy podparte embeddingami. Cognee oferuje **architekturę podwójnych magazynów**, łączącą wyszukiwanie według podobieństwa wektorowego z relacjami w grafie, umożliwiając agentom rozumienie nie tylko tego, które informacje są podobne, ale także jak pojęcia się ze sobą łączą.

Wyróżnia się na polu **hybrydowego wyszukiwania**, łączącego podobieństwo wektorowe, strukturę grafu oraz rozumowanie LLM – od wyszukiwania prostych fragmentów do odpowiadania z uwzględnieniem struktury grafu. System utrzymuje **żywą pamięć**, która ewoluuje i rośnie, pozostając jednocześnie zapytalna jako jeden połączony graf, wspierając zarówno krótko-, jak i długoterminowy kontekst sesji.

Samouczek w notebooku Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) demonstruje budowę tej zunifikowanej warstwy pamięci, z praktycznymi przykładami przetwarzania różnorodnych źródeł danych, wizualizacją grafu wiedzy oraz zapytaniami z wykorzystaniem różnych strategii wyszukiwania dostosowanych do potrzeb agentów.

### Przechowywanie pamięci z RAG

Poza specjalizowanymi narzędziami pamięci jak mem0, można wykorzystać solidne usługi wyszukiwania, takie jak **Azure AI Search jako backend do przechowywania i wyszukiwania pamięci**, szczególnie dla Strukturalnego RAG.

Pozwala to ugruntować odpowiedzi agenta w twoich własnych danych, zapewniając bardziej relewantne i dokładne odpowiedzi. Azure AI Search może być używany do przechowywania specyficznych dla użytkownika wspomnień podróżniczych, katalogów produktów lub jakiejkolwiek innej wiedzy z konkretnej dziedziny.

Azure AI Search wspiera funkcje takie jak **Strukturalne RAG**, które doskonale wydobywają i wyszukują gęste, ustrukturyzowane informacje z dużych zestawów danych, takich jak historie rozmów, e-maile czy nawet obrazy. Zapewnia to „nadludzką precyzję i trafność” w porównaniu do tradycyjnych podejść opartych na prostym fragmentowaniu tekstu i embeddingach.

## Tworzenie agentów AI zdolnych do samodoskonalenia

Powszechny wzorzec dla agentów samodoskonalących się to wprowadzenie **„agenta wiedzy”**. Ten oddzielny agent obserwuje główną rozmowę między użytkownikiem a agentem głównym. Jego rolą jest:

1. **Identyfikować cenne informacje**: Określić, czy któraś część rozmowy warta jest zapisania jako wiedza ogólna lub konkretna preferencja użytkownika.

2. **Ekstrahować i streszczać**: Wydzielić istotne nauki lub preferencje z rozmowy.

3. **Przechowywać w bazie wiedzy**: Zachować te informacje, często w bazie wektorowej, aby mogły być później wyszukane.

4. **Wzbogacać przyszłe zapytania**: Kiedy użytkownik inicjuje nowe zapytanie, agent wiedzy pobiera odpowiednie przechowane informacje i dołącza je do promptu użytkownika, dostarczając kluczowego kontekstu agentowi głównemu (podobnie jak RAG).

### Optymalizacje dla pamięci

• **Zarządzanie opóźnieniami**: Aby nie spowalniać interakcji użytkownika, na początku można użyć tańszego, szybszego modelu, który szybko oceni, czy warto przechowywać lub wyszukać informacje, odpalając bardziej złożony proces ekstrakcji lub wyszukiwania tylko w razie potrzeby.

• **Utrzymanie bazy wiedzy**: Dla rosnącej bazy wiedzy mniej używane informacje można przenieść do „zimnego magazynu”, aby kontrolować koszty.

## Masz więcej pytań o pamięć agentów?

Dołącz do [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), aby spotkać innych uczących się, uczestniczyć w godzinach konsultacji i uzyskać odpowiedzi na pytania dotyczące agentów AI.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczeń AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy starań, aby tłumaczenie było precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->