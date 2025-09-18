<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1923cf93aba522a5f4a493597112a893",
  "translation_date": "2025-09-18T16:10:55+00:00",
  "source_file": "13-agent-memory/README.md",
  "language_code": "pl"
}
-->
# Pamięć dla Agentów AI

Podczas omawiania unikalnych korzyści związanych z tworzeniem Agentów AI, najczęściej poruszane są dwie kwestie: zdolność do korzystania z narzędzi w celu realizacji zadań oraz zdolność do samodoskonalenia się. Pamięć jest fundamentem tworzenia agentów, którzy mogą się rozwijać i oferować lepsze doświadczenia użytkownikom.

W tej lekcji przyjrzymy się, czym jest pamięć dla Agentów AI, jak ją zarządzać i wykorzystywać na korzyść naszych aplikacji.

## Wprowadzenie

Ta lekcja obejmuje:

• **Zrozumienie pamięci Agentów AI**: Czym jest pamięć i dlaczego jest kluczowa dla agentów.

• **Implementacja i przechowywanie pamięci**: Praktyczne metody dodawania funkcji pamięci do agentów AI, z naciskiem na pamięć krótkoterminową i długoterminową.

• **Tworzenie samodoskonalących się Agentów AI**: Jak pamięć umożliwia agentom uczenie się na podstawie wcześniejszych interakcji i doskonalenie się z czasem.

## Cele nauki

Po ukończeniu tej lekcji będziesz wiedzieć, jak:

• **Rozróżniać różne typy pamięci agentów AI**, w tym pamięć roboczą, krótkoterminową, długoterminową oraz specjalistyczne formy, takie jak pamięć osobowości i epizodyczna.

• **Implementować i zarządzać pamięcią krótkoterminową i długoterminową dla agentów AI** przy użyciu frameworka Semantic Kernel, narzędzi takich jak Mem0 i Whiteboard memory oraz integracji z Azure AI Search.

• **Zrozumieć zasady działania samodoskonalących się agentów AI** i jak solidne systemy zarządzania pamięcią przyczyniają się do ciągłego uczenia się i adaptacji.

## Zrozumienie pamięci Agentów AI

W swojej istocie **pamięć dla agentów AI odnosi się do mechanizmów umożliwiających im przechowywanie i przywoływanie informacji**. Mogą to być szczegóły dotyczące rozmowy, preferencje użytkownika, wcześniejsze działania czy nawet wzorce, które agent nauczył się rozpoznawać.

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

Można ją porównać do kartki papieru, na której agent zapisuje informacje potrzebne do realizacji bieżącego zadania lub procesu myślowego. Przechowuje ona najważniejsze dane potrzebne do wykonania kolejnego kroku.

Dla agentów AI pamięć robocza często przechowuje najbardziej istotne informacje z rozmowy, nawet jeśli pełna historia czatu jest długa lub skrócona. Skupia się na kluczowych elementach, takich jak wymagania, propozycje, decyzje i działania.

**Przykład pamięci roboczej**

W przypadku agenta rezerwacji podróży pamięć robocza może przechowywać bieżące żądanie użytkownika, np. "Chcę zarezerwować wycieczkę do Paryża". To konkretne wymaganie jest przechowywane w kontekście agenta, aby poprowadzić bieżącą interakcję.

#### Pamięć krótkoterminowa

Ten rodzaj pamięci przechowuje informacje na czas trwania jednej rozmowy lub sesji. Jest to kontekst bieżącego czatu, który pozwala agentowi odwoływać się do wcześniejszych wypowiedzi w dialogu.

**Przykład pamięci krótkoterminowej**

Jeśli użytkownik pyta: "Ile kosztowałby lot do Paryża?" a następnie dodaje: "A co z zakwaterowaniem tam?", pamięć krótkoterminowa zapewnia, że agent wie, że "tam" odnosi się do "Paryża" w ramach tej samej rozmowy.

#### Pamięć długoterminowa

To informacje, które utrzymują się przez wiele rozmów lub sesji. Pozwala agentom pamiętać preferencje użytkownika, wcześniejsze interakcje czy ogólną wiedzę przez dłuższy czas. Jest to kluczowe dla personalizacji.

**Przykład pamięci długoterminowej**

Pamięć długoterminowa może przechowywać informacje, takie jak: "Ben lubi narciarstwo i aktywności na świeżym powietrzu, preferuje kawę z widokiem na góry i unika zaawansowanych tras narciarskich z powodu wcześniejszej kontuzji". Te dane, zdobyte podczas wcześniejszych interakcji, wpływają na rekomendacje w przyszłych sesjach planowania podróży, czyniąc je bardziej spersonalizowanymi.

#### Pamięć osobowości

Ten specjalistyczny typ pamięci pomaga agentowi rozwijać spójną "osobowość" lub "rolę". Pozwala agentowi pamiętać szczegóły o sobie lub swojej zamierzonej roli, co sprawia, że interakcje są bardziej płynne i skoncentrowane.

**Przykład pamięci osobowości**

Jeśli agent podróży jest zaprojektowany jako "ekspert w planowaniu narciarskim", pamięć osobowości może wzmacniać tę rolę, wpływając na jego odpowiedzi, aby były zgodne z tonem i wiedzą eksperta.

#### Pamięć epizodyczna

Ta pamięć przechowuje sekwencję kroków, które agent podejmuje podczas realizacji złożonego zadania, w tym sukcesy i porażki. Jest to jak zapamiętywanie konkretnych "epizodów" lub wcześniejszych doświadczeń, aby się z nich uczyć.

**Przykład pamięci epizodycznej**

Jeśli agent próbował zarezerwować konkretny lot, ale nie udało się to z powodu braku dostępności, pamięć epizodyczna może zapisać tę porażkę, pozwalając agentowi spróbować alternatywnych lotów lub poinformować użytkownika o problemie w bardziej świadomy sposób podczas kolejnej próby.

#### Pamięć encji

Dotyczy wyodrębniania i zapamiętywania konkretnych encji (np. osób, miejsc, rzeczy) oraz wydarzeń z rozmów. Pozwala agentowi budować uporządkowane zrozumienie kluczowych elementów omawianych.

**Przykład pamięci encji**

Z rozmowy o wcześniejszej podróży agent może wyodrębnić "Paryż", "Wieża Eiffla" i "kolacja w restauracji Le Chat Noir" jako encje. W przyszłej interakcji agent może przypomnieć sobie "Le Chat Noir" i zaproponować nową rezerwację tam.

#### Strukturalny RAG (Retrieval Augmented Generation)

Choć RAG jest szerszą techniką, "Strukturalny RAG" wyróżnia się jako potężna technologia pamięci. Wyodrębnia gęste, uporządkowane informacje z różnych źródeł (rozmów, e-maili, obrazów) i wykorzystuje je do zwiększenia precyzji, przywoływania i szybkości odpowiedzi. W przeciwieństwie do klasycznego RAG, który opiera się wyłącznie na semantycznym podobieństwie, Strukturalny RAG działa na inherentnej strukturze informacji.

**Przykład Strukturalnego RAG**

Zamiast dopasowywać tylko słowa kluczowe, Strukturalny RAG może analizować szczegóły lotu (cel, data, czas, linia lotnicza) z e-maila i przechowywać je w uporządkowany sposób. Umożliwia to precyzyjne zapytania, takie jak "Jaki lot zarezerwowałem do Paryża we wtorek?"

## Implementacja i przechowywanie pamięci

Implementacja pamięci dla agentów AI wymaga systematycznego procesu **zarządzania pamięcią**, który obejmuje generowanie, przechowywanie, przywoływanie, integrowanie, aktualizowanie, a nawet "zapominanie" (czyli usuwanie) informacji. Szczególnie istotnym aspektem jest przywoływanie.

### Specjalistyczne narzędzia pamięci

Jednym ze sposobów przechowywania i zarządzania pamięcią agenta jest użycie specjalistycznych narzędzi, takich jak Mem0. Mem0 działa jako warstwa pamięci trwałej, umożliwiając agentom przywoływanie istotnych interakcji, przechowywanie preferencji użytkownika i kontekstu faktów oraz uczenie się na podstawie sukcesów i porażek. Idea polega na tym, że agenci bezstanowi stają się stanowi.

Działa to poprzez **dwufazowy proces pamięci: ekstrakcję i aktualizację**. Najpierw wiadomości dodane do wątku agenta są wysyłane do usługi Mem0, która wykorzystuje model językowy (LLM) do podsumowania historii rozmowy i wyodrębnienia nowych wspomnień. Następnie faza aktualizacji sterowana przez LLM decyduje, czy dodać, zmodyfikować lub usunąć te wspomnienia, przechowując je w hybrydowym magazynie danych, który może obejmować bazy danych wektorowe, grafowe i klucz-wartość. System ten obsługuje również różne typy pamięci i może integrować pamięć grafową do zarządzania relacjami między encjami.

### Przechowywanie pamięci z RAG

Oprócz specjalistycznych narzędzi pamięci, takich jak Mem0, można wykorzystać solidne usługi wyszukiwania, takie jak **Azure AI Search jako zaplecze do przechowywania i przywoływania wspomnień**, szczególnie dla Strukturalnego RAG.

Pozwala to na ugruntowanie odpowiedzi agenta w danych własnych, zapewniając bardziej trafne i dokładne odpowiedzi. Azure AI Search może być używany do przechowywania wspomnień związanych z podróżami użytkownika, katalogów produktów lub dowolnej innej wiedzy specyficznej dla danej dziedziny.

Azure AI Search obsługuje funkcje takie jak **Strukturalny RAG**, który doskonale radzi sobie z wyodrębnianiem i przywoływaniem gęstych, uporządkowanych informacji z dużych zbiorów danych, takich jak historie rozmów, e-maile czy obrazy. Zapewnia to "nadludzką precyzję i przywoływanie" w porównaniu do tradycyjnych podejść opartych na fragmentacji tekstu i osadzaniu.

## Tworzenie samodoskonalących się Agentów AI

Częstym wzorcem dla samodoskonalących się agentów jest wprowadzenie **"agenta wiedzy"**. Ten oddzielny agent obserwuje główną rozmowę między użytkownikiem a agentem głównym. Jego rola polega na:

1. **Identyfikacji wartościowych informacji**: Określeniu, czy jakakolwiek część rozmowy jest warta zapisania jako wiedza ogólna lub konkretna preferencja użytkownika.

2. **Ekstrakcji i podsumowaniu**: Wyodrębnieniu istotnych informacji lub preferencji z rozmowy.

3. **Przechowywaniu w bazie wiedzy**: Zapisaniu wyodrębnionych informacji, często w bazie danych wektorowych, aby można je było później przywołać.

4. **Uzupełnianiu przyszłych zapytań**: Gdy użytkownik inicjuje nowe zapytanie, agent wiedzy przywołuje odpowiednie zapisane informacje i dodaje je do zapytania użytkownika, zapewniając kluczowy kontekst dla agenta głównego (podobnie jak RAG).

### Optymalizacje dla pamięci

• **Zarządzanie opóźnieniami**: Aby uniknąć spowolnienia interakcji użytkownika, można początkowo użyć tańszego, szybszego modelu do szybkiego sprawdzenia, czy warto przechowywać lub przywoływać informacje, a bardziej złożony proces ekstrakcji/przywoływania uruchamiać tylko wtedy, gdy jest to konieczne.

• **Utrzymanie bazy wiedzy**: W przypadku rosnącej bazy wiedzy, rzadziej używane informacje można przenieść do "zimnego magazynu", aby zarządzać kosztami.

## Masz więcej pytań dotyczących inżynierii kontekstu?

Dołącz do [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), aby spotkać się z innymi uczącymi się, uczestniczyć w godzinach konsultacji i uzyskać odpowiedzi na pytania dotyczące Agentów AI.

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.