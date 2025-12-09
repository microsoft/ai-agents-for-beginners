<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a1d90991499ad697c4ad24decaf36968",
  "translation_date": "2025-12-09T12:18:43+00:00",
  "source_file": "13-agent-memory/README.md",
  "language_code": "pl"
}
-->
# Pamięć dla Agentów AI 
[![Pamięć Agenta](../../../translated_images/lesson-13-thumbnail.959e3bc52d210c64a614a3bece6b170a2c472138dc0a14c7fbde07306ef95ae7.pl.png)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Podczas omawiania unikalnych korzyści tworzenia Agentów AI, najczęściej poruszane są dwie kwestie: zdolność do korzystania z narzędzi w celu realizacji zadań oraz zdolność do samodoskonalenia się w czasie. Pamięć jest fundamentem tworzenia samodoskonalących się agentów, którzy mogą zapewniać lepsze doświadczenia użytkownikom.

W tej lekcji przyjrzymy się, czym jest pamięć dla Agentów AI, jak można ją zarządzać i wykorzystywać na korzyść naszych aplikacji.

## Wprowadzenie

W tej lekcji omówimy:

• **Zrozumienie pamięci Agenta AI**: Czym jest pamięć i dlaczego jest kluczowa dla agentów.

• **Implementacja i przechowywanie pamięci**: Praktyczne metody dodawania funkcji pamięci do agentów AI, z naciskiem na pamięć krótkoterminową i długoterminową.

• **Tworzenie samodoskonalących się Agentów AI**: Jak pamięć pozwala agentom uczyć się na podstawie wcześniejszych interakcji i poprawiać swoje działanie w czasie.

## Dostępne Implementacje

Ta lekcja zawiera dwa kompleksowe samouczki w formie notebooków:

• **[13-agent-memory.ipynb](./13-agent-memory.ipynb)**: Implementuje pamięć za pomocą Mem0 i Azure AI Search w ramach Semantic Kernel.

• **[13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)**: Implementuje ustrukturyzowaną pamięć za pomocą Cognee, automatycznie budując graf wiedzy wspierany przez osadzenia, wizualizując graf i inteligentnie wyszukując informacje.

## Cele Nauki

Po ukończeniu tej lekcji będziesz wiedzieć, jak:

• **Rozróżniać różne typy pamięci Agenta AI**, w tym pamięć roboczą, krótkoterminową, długoterminową oraz specjalistyczne formy, takie jak pamięć osobowości i epizodyczna.

• **Implementować i zarządzać pamięcią krótkoterminową i długoterminową dla Agentów AI** przy użyciu Semantic Kernel, wykorzystując narzędzia takie jak Mem0, Cognee, Whiteboard memory oraz integrację z Azure AI Search.

• **Zrozumieć zasady działania samodoskonalących się Agentów AI** i jak solidne systemy zarządzania pamięcią przyczyniają się do ciągłego uczenia się i adaptacji.

## Zrozumienie Pamięci Agenta AI

W swojej istocie **pamięć dla Agentów AI odnosi się do mechanizmów pozwalających im na przechowywanie i przypominanie informacji**. Mogą to być szczegóły rozmowy, preferencje użytkownika, wcześniejsze działania czy nawet wyuczone wzorce.

Bez pamięci aplikacje AI są często bezstanowe, co oznacza, że każda interakcja zaczyna się od zera. Prowadzi to do powtarzalnych i frustrujących doświadczeń użytkownika, gdzie agent "zapomina" wcześniejszy kontekst lub preferencje.

### Dlaczego Pamięć Jest Ważna?

Inteligencja agenta jest ściśle związana z jego zdolnością do przypominania i wykorzystywania wcześniejszych informacji. Pamięć pozwala agentom być:

• **Refleksyjnymi**: Uczyć się na podstawie wcześniejszych działań i wyników.

• **Interaktywnymi**: Utrzymywać kontekst w trakcie trwającej rozmowy.

• **Proaktywnymi i reaktywnymi**: Przewidywać potrzeby lub odpowiednio reagować na podstawie danych historycznych.

• **Autonomicznymi**: Działać bardziej niezależnie, korzystając z przechowywanej wiedzy.

Celem implementacji pamięci jest uczynienie agentów bardziej **wiarygodnymi i zdolnymi**.

### Rodzaje Pamięci

#### Pamięć Robocza

Można ją porównać do kartki papieru, na której agent zapisuje informacje potrzebne do wykonania bieżącego zadania lub procesu myślowego. Przechowuje ona natychmiastowe informacje potrzebne do obliczenia kolejnego kroku.

Dla Agentów AI pamięć robocza często przechowuje najbardziej istotne informacje z rozmowy, nawet jeśli pełna historia czatu jest długa lub skrócona. Skupia się na wyodrębnianiu kluczowych elementów, takich jak wymagania, propozycje, decyzje i działania.

**Przykład Pamięci Roboczej**

W przypadku agenta rezerwacji podróży pamięć robocza może przechowywać bieżące żądanie użytkownika, takie jak "Chcę zarezerwować wycieczkę do Paryża". To konkretne wymaganie jest przechowywane w kontekście agenta, aby poprowadzić bieżącą interakcję.

#### Pamięć Krótkoterminowa

Ten rodzaj pamięci przechowuje informacje na czas trwania jednej rozmowy lub sesji. Jest to kontekst bieżącego czatu, pozwalający agentowi odwoływać się do wcześniejszych wypowiedzi w dialogu.

**Przykład Pamięci Krótkoterminowej**

Jeśli użytkownik pyta: "Ile kosztowałby lot do Paryża?" a następnie dodaje: "A co z zakwaterowaniem tam?", pamięć krótkoterminowa zapewnia, że agent wie, że "tam" odnosi się do "Paryża" w tej samej rozmowie.

#### Pamięć Długoterminowa

To informacje, które są przechowywane przez wiele rozmów lub sesji. Pozwala agentom pamiętać preferencje użytkownika, wcześniejsze interakcje lub ogólną wiedzę przez dłuższy czas. Jest to kluczowe dla personalizacji.

**Przykład Pamięci Długoterminowej**

Pamięć długoterminowa może przechowywać informacje, że "Ben lubi narciarstwo i aktywności na świeżym powietrzu, preferuje kawę z widokiem na góry i unika zaawansowanych stoków narciarskich z powodu wcześniejszej kontuzji". Te informacje, zdobyte podczas wcześniejszych interakcji, wpływają na rekomendacje w przyszłych sesjach planowania podróży, czyniąc je bardziej spersonalizowanymi.

#### Pamięć Osobowości

Ten specjalistyczny rodzaj pamięci pomaga agentowi rozwijać spójną "osobowość" lub "rolę". Pozwala agentowi pamiętać szczegóły o sobie lub swojej zamierzonej roli, co sprawia, że interakcje są bardziej płynne i skoncentrowane.

**Przykład Pamięci Osobowości**

Jeśli agent podróży został zaprojektowany jako "ekspert w planowaniu narciarskim", pamięć osobowości może wzmacniać tę rolę, wpływając na jego odpowiedzi, aby były zgodne z tonem i wiedzą eksperta.

#### Pamięć Epizodyczna/Przepływu Pracy

Ta pamięć przechowuje sekwencję kroków, które agent podejmuje podczas złożonego zadania, w tym sukcesy i porażki. To jak zapamiętywanie konkretnych "epizodów" lub wcześniejszych doświadczeń, aby się z nich uczyć.

**Przykład Pamięci Epizodycznej**

Jeśli agent próbował zarezerwować konkretny lot, ale nie udało się to z powodu braku dostępności, pamięć epizodyczna mogłaby zapisać tę porażkę, pozwalając agentowi spróbować alternatywnych lotów lub poinformować użytkownika o problemie w bardziej świadomy sposób podczas kolejnej próby.

#### Pamięć Encji

Dotyczy wyodrębniania i zapamiętywania konkretnych encji (takich jak osoby, miejsca czy rzeczy) oraz zdarzeń z rozmów. Pozwala agentowi budować ustrukturyzowane rozumienie kluczowych elementów omawianych w rozmowie.

**Przykład Pamięci Encji**

Z rozmowy o wcześniejszej podróży agent może wyodrębnić "Paryż", "Wieża Eiffla" i "kolacja w restauracji Le Chat Noir" jako encje. W przyszłej interakcji agent mógłby przypomnieć sobie "Le Chat Noir" i zaproponować ponowną rezerwację tam.

#### Ustrukturyzowany RAG (Retrieval Augmented Generation)

Chociaż RAG jest szerszą techniką, "Ustrukturyzowany RAG" jest wyróżniany jako potężna technologia pamięci. Wyodrębnia gęste, ustrukturyzowane informacje z różnych źródeł (rozmów, e-maili, obrazów) i wykorzystuje je do zwiększenia precyzji, przypominania i szybkości odpowiedzi. W przeciwieństwie do klasycznego RAG, który opiera się wyłącznie na semantycznym podobieństwie, Ustrukturyzowany RAG działa z wrodzoną strukturą informacji.

**Przykład Ustrukturyzowanego RAG**

Zamiast tylko dopasowywać słowa kluczowe, Ustrukturyzowany RAG mógłby przeanalizować szczegóły lotu (cel, data, czas, linia lotnicza) z e-maila i przechowywać je w ustrukturyzowany sposób. To pozwala na precyzyjne zapytania, takie jak "Jaki lot zarezerwowałem do Paryża we wtorek?"

## Implementacja i Przechowywanie Pamięci

Implementacja pamięci dla Agentów AI obejmuje systematyczny proces **zarządzania pamięcią**, który obejmuje generowanie, przechowywanie, wyszukiwanie, integrowanie, aktualizowanie, a nawet "zapominanie" (lub usuwanie) informacji. Szczególnie istotnym aspektem jest wyszukiwanie.

### Specjalistyczne Narzędzia Pamięci

#### Mem0

Jednym ze sposobów przechowywania i zarządzania pamięcią agenta jest użycie specjalistycznych narzędzi, takich jak Mem0. Mem0 działa jako warstwa pamięci trwałej, pozwalając agentom przypominać sobie istotne interakcje, przechowywać preferencje użytkownika i kontekst faktów oraz uczyć się na podstawie sukcesów i porażek w czasie. Idea polega na tym, że agenci bezstanowi stają się stanowi.

Działa to poprzez **dwufazowy proces pamięci: ekstrakcję i aktualizację**. Najpierw wiadomości dodane do wątku agenta są wysyłane do usługi Mem0, która wykorzystuje model językowy (LLM) do podsumowania historii rozmowy i wyodrębnienia nowych wspomnień. Następnie faza aktualizacji napędzana przez LLM decyduje, czy dodać, zmodyfikować, czy usunąć te wspomnienia, przechowując je w hybrydowym magazynie danych, który może obejmować bazy danych wektorowe, grafowe i klucz-wartość. System ten obsługuje również różne typy pamięci i może uwzględniać pamięć grafową do zarządzania relacjami między encjami.

#### Cognee

Innym potężnym podejściem jest użycie **Cognee**, otwartoźródłowej pamięci semantycznej dla Agentów AI, która przekształca dane ustrukturyzowane i nieustrukturyzowane w zapytania w grafach wiedzy wspieranych przez osadzenia. Cognee oferuje **architekturę podwójnego magazynu**, łączącą wyszukiwanie podobieństwa wektorowego z relacjami grafowymi, umożliwiając agentom zrozumienie nie tylko tego, jakie informacje są podobne, ale także jak koncepcje się ze sobą łączą.

Cognee wyróżnia się **hybrydowym wyszukiwaniem**, które łączy podobieństwo wektorowe, strukturę grafu i rozumowanie LLM - od wyszukiwania surowych fragmentów po pytania uwzględniające graf. System utrzymuje **żywą pamięć**, która ewoluuje i rośnie, pozostając jednocześnie zapytania jako jeden połączony graf, wspierając zarówno kontekst sesji krótkoterminowej, jak i pamięć trwałą długoterminową.

Samouczek notebooka Cognee ([13-agent-memory-cognee.ipynb](./13-agent-memory-cognee.ipynb)) pokazuje, jak zbudować tę zintegrowaną warstwę pamięci, z praktycznymi przykładami wprowadzania różnych źródeł danych, wizualizacji grafu wiedzy i zapytań z różnymi strategiami wyszukiwania dostosowanymi do potrzeb agenta.

### Przechowywanie Pamięci z RAG

Poza specjalistycznymi narzędziami pamięci, takimi jak Mem0, można wykorzystać solidne usługi wyszukiwania, takie jak **Azure AI Search jako zaplecze do przechowywania i wyszukiwania wspomnień**, szczególnie dla ustrukturyzowanego RAG.

Pozwala to na ugruntowanie odpowiedzi agenta w oparciu o własne dane, zapewniając bardziej trafne i dokładne odpowiedzi. Azure AI Search można używać do przechowywania wspomnień specyficznych dla użytkownika, katalogów produktów lub dowolnej innej wiedzy specyficznej dla danej dziedziny.

Azure AI Search obsługuje funkcje takie jak **Ustrukturyzowany RAG**, który wyróżnia się wyodrębnianiem i wyszukiwaniem gęstych, ustrukturyzowanych informacji z dużych zbiorów danych, takich jak historie rozmów, e-maile czy obrazy. Zapewnia to "nadludzką precyzję i przypominanie" w porównaniu z tradycyjnymi podejściami do dzielenia tekstu i osadzania.

## Tworzenie Samodoskonalących się Agentów AI

Częstym wzorcem dla samodoskonalących się agentów jest wprowadzenie **"agenta wiedzy"**. Ten oddzielny agent obserwuje główną rozmowę między użytkownikiem a głównym agentem. Jego rola polega na:

1. **Identyfikacji wartościowych informacji**: Określeniu, czy jakakolwiek część rozmowy jest warta zapisania jako ogólna wiedza lub konkretna preferencja użytkownika.

2. **Ekstrakcji i podsumowaniu**: Wyodrębnieniu istotnych informacji lub preferencji z rozmowy.

3. **Przechowywaniu w bazie wiedzy**: Zachowaniu wyodrębnionych informacji, często w bazie danych wektorowych, aby można je było później wyszukać.

4. **Wzbogacaniu przyszłych zapytań**: Gdy użytkownik inicjuje nowe zapytanie, agent wiedzy wyszukuje odpowiednie przechowywane informacje i dołącza je do zapytania użytkownika, dostarczając kluczowego kontekstu głównemu agentowi (podobnie jak RAG).

### Optymalizacje dla Pamięci

• **Zarządzanie opóźnieniami**: Aby uniknąć spowolnienia interakcji użytkownika, można początkowo użyć tańszego, szybszego modelu do szybkiego sprawdzenia, czy informacje są warte przechowywania lub wyszukiwania, a bardziej złożony proces ekstrakcji/wyszukiwania uruchamiać tylko wtedy, gdy jest to konieczne.

• **Utrzymanie bazy wiedzy**: W przypadku rosnącej bazy wiedzy, rzadziej używane informacje można przenieść do "zimnego magazynu", aby zarządzać kosztami.

## Masz Więcej Pytań o Pamięć Agenta?

Dołącz do [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), aby spotkać się z innymi uczącymi się, uczestniczyć w godzinach konsultacji i uzyskać odpowiedzi na pytania dotyczące Agentów AI.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->