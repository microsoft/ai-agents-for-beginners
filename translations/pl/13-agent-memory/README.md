<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d2c9703548140bafa2d6a77406552542",
  "translation_date": "2025-10-03T14:37:21+00:00",
  "source_file": "13-agent-memory/README.md",
  "language_code": "pl"
}
-->
# Pamięć dla agentów AI  
[![Pamięć agenta](../../../translated_images/lesson-13-thumbnail.959e3bc52d210c64a614a3bece6b170a2c472138dc0a14c7fbde07306ef95ae7.pl.png)](https://youtu.be/QrYbHesIxpw?si=qNYW6PL3fb3lTPMk)

Podczas omawiania unikalnych korzyści związanych z tworzeniem agentów AI, najczęściej poruszane są dwie kwestie: zdolność do korzystania z narzędzi w celu realizacji zadań oraz zdolność do samodoskonalenia się. Pamięć jest podstawą tworzenia samodoskonalących się agentów, którzy mogą zapewniać lepsze doświadczenia dla użytkowników.

W tej lekcji przyjrzymy się, czym jest pamięć dla agentów AI, jak można ją zarządzać i wykorzystywać na korzyść naszych aplikacji.

## Wprowadzenie  

Ta lekcja obejmuje:  

• **Zrozumienie pamięci agenta AI**: Czym jest pamięć i dlaczego jest kluczowa dla agentów.  

• **Implementacja i przechowywanie pamięci**: Praktyczne metody dodawania funkcji pamięci do agentów AI, z naciskiem na pamięć krótkoterminową i długoterminową.  

• **Tworzenie samodoskonalących się agentów AI**: Jak pamięć umożliwia agentom uczenie się na podstawie wcześniejszych interakcji i doskonalenie się z czasem.  

## Cele nauki  

Po ukończeniu tej lekcji będziesz wiedzieć, jak:  

• **Rozróżniać różne typy pamięci agenta AI**, w tym pamięć roboczą, krótkoterminową, długoterminową oraz specjalistyczne formy, takie jak pamięć osobowości i epizodyczna.  

• **Implementować i zarządzać pamięcią krótkoterminową i długoterminową dla agentów AI** przy użyciu frameworka Semantic Kernel, wykorzystując narzędzia takie jak Mem0 i pamięć Whiteboard oraz integrując je z Azure AI Search.  

• **Zrozumieć zasady działania samodoskonalących się agentów AI** i jak solidne systemy zarządzania pamięcią przyczyniają się do ciągłego uczenia się i adaptacji.  

## Zrozumienie pamięci agenta AI  

W swojej istocie **pamięć dla agentów AI odnosi się do mechanizmów umożliwiających im przechowywanie i przywoływanie informacji**. Informacje te mogą dotyczyć szczegółów rozmowy, preferencji użytkownika, wcześniejszych działań czy nawet wzorców, które agent nauczył się rozpoznawać.  

Bez pamięci aplikacje AI są często bezstanowe, co oznacza, że każda interakcja zaczyna się od zera. Prowadzi to do powtarzalnych i frustrujących doświadczeń użytkownika, gdzie agent "zapomina" wcześniejszy kontekst lub preferencje.  

### Dlaczego pamięć jest ważna?  

Inteligencja agenta jest ściśle związana z jego zdolnością do przywoływania i wykorzystywania wcześniejszych informacji. Pamięć pozwala agentom być:  

• **Refleksyjnymi**: Uczyć się na podstawie wcześniejszych działań i wyników.  

• **Interaktywnymi**: Utrzymywać kontekst w trakcie trwającej rozmowy.  

• **Proaktywnymi i reaktywnymi**: Przewidywać potrzeby lub odpowiednio reagować na podstawie danych historycznych.  

• **Autonomicznymi**: Działać bardziej niezależnie, korzystając z przechowywanej wiedzy.  

Celem implementacji pamięci jest uczynienie agentów bardziej **wiarygodnymi i zdolnymi**.  

### Rodzaje pamięci  

#### Pamięć robocza  

Można ją porównać do kartki papieru, którą agent wykorzystuje podczas jednego, bieżącego zadania lub procesu myślowego. Przechowuje ona natychmiastowe informacje potrzebne do wykonania kolejnego kroku.  

Dla agentów AI pamięć robocza często przechwytuje najbardziej istotne informacje z rozmowy, nawet jeśli pełna historia czatu jest długa lub skrócona. Skupia się na wyodrębnianiu kluczowych elementów, takich jak wymagania, propozycje, decyzje i działania.  

**Przykład pamięci roboczej**  

W przypadku agenta rezerwacji podróży pamięć robocza może przechwycić bieżące żądanie użytkownika, takie jak "Chcę zarezerwować wycieczkę do Paryża". To konkretne wymaganie jest przechowywane w bieżącym kontekście agenta, aby poprowadzić interakcję.  

#### Pamięć krótkoterminowa  

Ten typ pamięci przechowuje informacje na czas trwania jednej rozmowy lub sesji. Jest to kontekst bieżącego czatu, który pozwala agentowi odwoływać się do wcześniejszych wypowiedzi w dialogu.  

**Przykład pamięci krótkoterminowej**  

Jeśli użytkownik zapyta: "Ile kosztowałby lot do Paryża?" a następnie doda: "A co z zakwaterowaniem tam?", pamięć krótkoterminowa zapewnia, że agent wie, iż "tam" odnosi się do "Paryża" w tej samej rozmowie.  

#### Pamięć długoterminowa  

To informacje, które utrzymują się przez wiele rozmów lub sesji. Pozwala agentom pamiętać preferencje użytkownika, wcześniejsze interakcje lub ogólną wiedzę przez dłuższy czas. Jest to kluczowe dla personalizacji.  

**Przykład pamięci długoterminowej**  

Pamięć długoterminowa może przechowywać informacje, takie jak "Ben lubi narciarstwo i aktywności na świeżym powietrzu, preferuje kawę z widokiem na góry i unika zaawansowanych stoków narciarskich z powodu wcześniejszej kontuzji". Te informacje, zdobyte podczas wcześniejszych interakcji, wpływają na rekomendacje w przyszłych sesjach planowania podróży, czyniąc je bardziej spersonalizowanymi.  

#### Pamięć osobowości  

Ten specjalistyczny typ pamięci pomaga agentowi rozwijać spójną "osobowość" lub "rolę". Pozwala agentowi pamiętać szczegóły o sobie lub swojej zamierzonej roli, co sprawia, że interakcje są bardziej płynne i skoncentrowane.  

**Przykład pamięci osobowości**  

Jeśli agent podróży został zaprojektowany jako "ekspert w planowaniu narciarskim", pamięć osobowości może wzmacniać tę rolę, wpływając na jego odpowiedzi, aby były zgodne z tonem i wiedzą eksperta.  

#### Pamięć epizodyczna  

Ta pamięć przechowuje sekwencję kroków, które agent podejmuje podczas realizacji złożonego zadania, w tym sukcesy i porażki. Jest to jak zapamiętywanie konkretnych "epizodów" lub wcześniejszych doświadczeń, aby się z nich uczyć.  

**Przykład pamięci epizodycznej**  

Jeśli agent próbował zarezerwować konkretny lot, ale nie udało się to z powodu braku dostępności, pamięć epizodyczna mogłaby zapisać tę porażkę, pozwalając agentowi spróbować alternatywnych lotów lub poinformować użytkownika o problemie w bardziej świadomy sposób podczas kolejnej próby.  

#### Pamięć encji  

Dotyczy wyodrębniania i zapamiętywania konkretnych encji (takich jak osoby, miejsca czy rzeczy) oraz wydarzeń z rozmów. Pozwala agentowi budować strukturalne zrozumienie kluczowych elementów omawianych.  

**Przykład pamięci encji**  

Z rozmowy o wcześniejszej podróży agent może wyodrębnić "Paryż", "Wieża Eiffla" i "kolacja w restauracji Le Chat Noir" jako encje. W przyszłej interakcji agent mógłby przypomnieć sobie "Le Chat Noir" i zaproponować nową rezerwację tam.  

#### Strukturalny RAG (Retrieval Augmented Generation)  

Choć RAG jest szerszą techniką, "Strukturalny RAG" wyróżnia się jako potężna technologia pamięci. Wyodrębnia gęste, strukturalne informacje z różnych źródeł (rozmów, e-maili, obrazów) i wykorzystuje je do zwiększenia precyzji, przywoływania i szybkości odpowiedzi. W przeciwieństwie do klasycznego RAG, który opiera się wyłącznie na podobieństwie semantycznym, Strukturalny RAG działa na podstawie wewnętrznej struktury informacji.  

**Przykład Strukturalnego RAG**  

Zamiast dopasowywać tylko słowa kluczowe, Strukturalny RAG mógłby przeanalizować szczegóły lotu (cel podróży, data, czas, linia lotnicza) z e-maila i przechowywać je w uporządkowany sposób. Umożliwia to precyzyjne zapytania, takie jak "Jaki lot zarezerwowałem do Paryża we wtorek?"  

## Implementacja i przechowywanie pamięci  

Implementacja pamięci dla agentów AI obejmuje systematyczny proces **zarządzania pamięcią**, który obejmuje generowanie, przechowywanie, przywoływanie, integrowanie, aktualizowanie, a nawet "zapominanie" (czyli usuwanie) informacji. Szczególnie istotnym aspektem jest przywoływanie.  

### Specjalistyczne narzędzia pamięci  

Jednym ze sposobów przechowywania i zarządzania pamięcią agenta jest użycie specjalistycznych narzędzi, takich jak Mem0. Mem0 działa jako warstwa pamięci trwałej, umożliwiając agentom przywoływanie istotnych interakcji, przechowywanie preferencji użytkownika i kontekstu faktów oraz uczenie się na podstawie sukcesów i porażek z czasem. Idea polega na tym, że agenci bezstanowi stają się stanowi.  

Działa to poprzez **dwufazowy proces pamięci: ekstrakcję i aktualizację**. Najpierw wiadomości dodane do wątku agenta są wysyłane do usługi Mem0, która wykorzystuje model językowy (LLM) do podsumowania historii rozmowy i wyodrębnienia nowych wspomnień. Następnie faza aktualizacji sterowana przez LLM decyduje, czy dodać, zmodyfikować lub usunąć te wspomnienia, przechowując je w hybrydowym magazynie danych, który może obejmować bazy danych wektorowe, grafowe i klucz-wartość. System ten obsługuje również różne typy pamięci i może uwzględniać pamięć grafową do zarządzania relacjami między encjami.  

### Przechowywanie pamięci z RAG  

Oprócz specjalistycznych narzędzi pamięci, takich jak Mem0, można wykorzystać solidne usługi wyszukiwania, takie jak **Azure AI Search jako zaplecze do przechowywania i przywoływania wspomnień**, szczególnie dla Strukturalnego RAG.  

Pozwala to na ugruntowanie odpowiedzi agenta w oparciu o własne dane, zapewniając bardziej trafne i dokładne odpowiedzi. Azure AI Search może być używany do przechowywania wspomnień związanych z podróżami użytkownika, katalogów produktów lub dowolnej innej wiedzy specyficznej dla danej dziedziny.  

Azure AI Search obsługuje funkcje takie jak **Strukturalny RAG**, który doskonale sprawdza się w wyodrębnianiu i przywoływaniu gęstych, strukturalnych informacji z dużych zbiorów danych, takich jak historie rozmów, e-maile czy obrazy. Zapewnia to "nadludzką precyzję i przywoływanie" w porównaniu z tradycyjnymi podejściami do dzielenia tekstu na fragmenty i osadzania.  

## Tworzenie samodoskonalących się agentów AI  

Częstym wzorcem dla samodoskonalących się agentów jest wprowadzenie **"agenta wiedzy"**. Ten oddzielny agent obserwuje główną rozmowę między użytkownikiem a agentem głównym. Jego rola polega na:  

1. **Identyfikacji wartościowych informacji**: Określeniu, czy jakakolwiek część rozmowy jest warta zapisania jako ogólna wiedza lub konkretna preferencja użytkownika.  

2. **Ekstrakcji i podsumowaniu**: Wyodrębnieniu istotnych informacji lub preferencji z rozmowy.  

3. **Przechowywaniu w bazie wiedzy**: Zachowaniu wyodrębnionych informacji, często w bazie danych wektorowych, aby można je było później przywołać.  

4. **Uzupełnianiu przyszłych zapytań**: Gdy użytkownik inicjuje nowe zapytanie, agent wiedzy przywołuje odpowiednie zapisane informacje i dodaje je do zapytania użytkownika, zapewniając kluczowy kontekst dla agenta głównego (podobnie jak RAG).  

### Optymalizacje dla pamięci  

• **Zarządzanie opóźnieniami**: Aby uniknąć spowolnienia interakcji użytkownika, można początkowo użyć tańszego, szybszego modelu do szybkiego sprawdzenia, czy warto przechowywać lub przywoływać informacje, a bardziej złożony proces ekstrakcji/przywoływania uruchamiać tylko wtedy, gdy jest to konieczne.  

• **Utrzymanie bazy wiedzy**: W przypadku rosnącej bazy wiedzy, rzadziej używane informacje można przenieść do "zimnego magazynu", aby zarządzać kosztami.  

## Masz więcej pytań dotyczących pamięci agenta?  

Dołącz do [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), aby spotkać się z innymi uczącymi się, uczestniczyć w godzinach konsultacji i uzyskać odpowiedzi na pytania dotyczące agentów AI.  

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż staramy się zapewnić dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.