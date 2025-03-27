<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "969885aab5f923f67f134ce115fbbcaf",
  "translation_date": "2025-03-26T19:05:06+00:00",
  "source_file": "03-agentic-design-patterns\\README.md",
  "language_code": "pl"
}
-->
[![Jak projektować dobre agentów AI](../../../translated_images/lesson-3-thumbnail.fc00fd0f7e476e3f6dbe06f4c10d1590953810d345283f825e79bede5e97e6d6.pl.png)](https://youtu.be/m9lM8qqoOEA?si=4KimounNKvArQQ0K)

> _(Kliknij obrazek powyżej, aby obejrzeć wideo z tej lekcji)_
# Zasady projektowania agentów AI

## Wprowadzenie

Istnieje wiele sposobów na budowanie systemów agentowych AI. Biorąc pod uwagę, że niejednoznaczność jest cechą, a nie wadą w projektowaniu generatywnej sztucznej inteligencji, inżynierowie często mają trudności z ustaleniem, od czego zacząć. Stworzyliśmy zestaw zasad projektowania UX skoncentrowanych na człowieku, aby umożliwić deweloperom budowanie systemów agentowych skoncentrowanych na klientach, które odpowiadają na ich potrzeby biznesowe. Te zasady projektowania nie są sztywną architekturą, lecz punktem wyjścia dla zespołów definiujących i tworzących doświadczenia agentowe.

Ogólnie rzecz biorąc, agenci powinni:

- Rozszerzać i skalować ludzkie zdolności (burza mózgów, rozwiązywanie problemów, automatyzacja itp.)
- Wypełniać luki w wiedzy (zapewnianie szybkiego dostępu do informacji, tłumaczenia itp.)
- Ułatwiać i wspierać współpracę w sposób zgodny z preferencjami użytkownika
- Pomagać nam stawać się lepszymi wersjami siebie (np. trener życiowy, mistrz zadań, pomoc w nauce regulacji emocji i umiejętności mindfulness, budowanie odporności itp.)

## Tematy omawiane w tej lekcji

- Czym są zasady projektowania agentów
- Jakie wytyczne należy przestrzegać podczas wdrażania tych zasad
- Przykłady zastosowania zasad projektowania

## Cele nauki

Po ukończeniu tej lekcji będziesz w stanie:

1. Wyjaśnić, czym są zasady projektowania agentów
2. Wyjaśnić wytyczne dotyczące stosowania zasad projektowania agentów
3. Zrozumieć, jak zbudować agenta korzystając z zasad projektowania agentów

## Zasady projektowania agentów

![Zasady projektowania agentów](../../../translated_images/agentic-design-principles.9f32a64bb6e2aa5a1bdffb70111aa724058bc248b1a3dd3c6661344015604cff.pl.png)

### Agent (Przestrzeń)

To środowisko, w którym działa agent. Zasady te wskazują, jak projektować agentów do działania w fizycznych i cyfrowych światach.

- **Łączenie, a nie zastępowanie** – pomagają łączyć ludzi z innymi osobami, wydarzeniami i wiedzą, aby umożliwić współpracę i budowanie relacji.
- Agenci pomagają łączyć wydarzenia, wiedzę i ludzi.
- Agenci zbliżają ludzi. Nie są projektowani, aby ich zastępować lub pomniejszać ich wartość.
- **Łatwo dostępni, ale czasami niewidzialni** – agent działa głównie w tle i interweniuje tylko wtedy, gdy jest to istotne i odpowiednie.
  - Agent jest łatwo dostępny dla autoryzowanych użytkowników na dowolnym urządzeniu lub platformie.
  - Agent obsługuje wielomodalne dane wejściowe i wyjściowe (dźwięk, głos, tekst itd.).
  - Agent może płynnie przechodzić między działaniem na pierwszym planie a w tle; między proaktywnym a reaktywnym, w zależności od potrzeb użytkownika.
  - Agent może działać w formie niewidzialnej, ale jego procesy w tle oraz współpraca z innymi agentami są transparentne i kontrolowalne przez użytkownika.

### Agent (Czas)

To sposób, w jaki agent działa w czasie. Zasady te wskazują, jak projektować agentów działających w przeszłości, teraźniejszości i przyszłości.

- **Przeszłość**: Refleksja nad historią, która obejmuje zarówno stan, jak i kontekst.
  - Agent dostarcza bardziej trafne wyniki na podstawie analizy bogatszych danych historycznych, nie ograniczając się tylko do wydarzeń, osób czy stanów.
  - Agent tworzy powiązania z przeszłymi wydarzeniami i aktywnie odwołuje się do pamięci, aby zaangażować się w bieżące sytuacje.
- **Teraźniejszość**: Delikatne sugestie zamiast powiadomień.
  - Agent prezentuje kompleksowe podejście do interakcji z ludźmi. Kiedy wydarzenie ma miejsce, agent wychodzi poza statyczne powiadomienia czy inne formalności. Może uprościć procesy lub dynamicznie generować wskazówki, aby skierować uwagę użytkownika we właściwym momencie.
  - Agent dostarcza informacje dostosowane do kontekstu, zmian społecznych i kulturowych oraz zamiarów użytkownika.
  - Interakcja z agentem może być stopniowa, rozwijająca się i wzrastająca w złożoności, aby wspierać użytkownika w dłuższym okresie.
- **Przyszłość**: Adaptacja i ewolucja.
  - Agent dostosowuje się do różnych urządzeń, platform i modalności.
  - Agent dostosowuje się do zachowań użytkownika, jego potrzeb związanych z dostępnością i jest w pełni personalizowalny.
  - Agent kształtuje się i ewoluuje poprzez ciągłą interakcję z użytkownikiem.

### Agent (Rdzeń)

To kluczowe elementy w rdzeniu projektu agenta.

- **Akceptowanie niepewności, ale budowanie zaufania**.
  - Pewien poziom niepewności agenta jest oczekiwany. Niepewność jest kluczowym elementem projektowania agentów.
  - Zaufanie i transparentność są podstawowymi warstwami projektowania agentów.
  - Człowiek kontroluje, kiedy agent jest włączony/wyłączony, a status agenta jest zawsze jasno widoczny.

## Wytyczne do wdrażania tych zasad

Korzystając z powyższych zasad projektowania, stosuj następujące wytyczne:

1. **Transparentność**: Informuj użytkownika, że korzysta z AI, jak działa system (w tym działania z przeszłości) oraz jak przekazywać opinie i modyfikować system.
2. **Kontrola**: Umożliwiaj użytkownikowi personalizację, określanie preferencji i dostosowanie systemu oraz jego atrybutów (w tym możliwość zapomnienia danych).
3. **Spójność**: Dąż do spójnych, wielomodalnych doświadczeń na różnych urządzeniach i punktach końcowych. Korzystaj z dobrze znanych elementów UI/UX tam, gdzie to możliwe (np. ikona mikrofonu dla interakcji głosowej) i minimalizuj obciążenie poznawcze użytkownika (np. dążąc do zwięzłych odpowiedzi, pomocy wizualnych i treści „Dowiedz się więcej”).

## Jak zaprojektować agenta podróży korzystając z tych zasad i wytycznych

Wyobraź sobie, że projektujesz agenta podróży. Oto jak można zastosować zasady i wytyczne projektowania:

1. **Transparentność** – Informuj użytkownika, że agent podróży korzysta z AI. Podaj podstawowe instrukcje, jak zacząć (np. wiadomość powitalna, przykładowe zapytania). Jasno dokumentuj to na stronie produktu. Pokaż listę zapytań, które użytkownik zadał w przeszłości. Wyjaśnij, jak przekazywać opinie (kciuk w górę lub w dół, przycisk „Prześlij opinię” itd.). Wyraźnie określ, czy agent ma ograniczenia w zakresie użytkowania lub tematyki.
2. **Kontrola** – Upewnij się, że użytkownik wie, jak modyfikować agenta po jego utworzeniu, np. za pomocą promptów systemowych. Umożliwiaj użytkownikowi wybór, jak szczegółowe mają być odpowiedzi agenta, jego styl pisania oraz tematy, których agent powinien unikać. Daj możliwość przeglądania i usuwania powiązanych plików lub danych, zapytań i poprzednich rozmów.
3. **Spójność** – Upewnij się, że ikony do udostępniania promptów, dodawania plików lub zdjęć oraz oznaczania osób czy rzeczy są standardowe i rozpoznawalne. Używaj ikony spinacza do papieru, aby wskazać przesyłanie/udostępnianie plików agentowi, oraz ikony obrazu do przesyłania grafik.

## Dodatkowe zasoby

- 

## Poprzednia lekcja

[Badanie ram agentowych](../02-explore-agentic-frameworks/README.md)

## Następna lekcja

[Wzorzec projektowania wykorzystania narzędzi](../04-tool-use/README.md)

