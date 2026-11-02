[![Jak projektować dobre Agenty AI](../../../translated_images/pl/lesson-3-thumbnail.1092dd7a8f1074a5.webp)](https://youtu.be/m9lM8qqoOEA?si=4KimounNKvArQQ0K)

> _(Kliknij powyższy obraz, aby obejrzeć wideo z tej lekcji)_
# Zasady projektowania agentów AI

## Wprowadzenie

Istnieje wiele sposobów myślenia o budowaniu systemów agentowych AI. Biorąc pod uwagę, że niejednoznaczność jest cechą, a nie błędem w projektowaniu Generative AI, inżynierom czasami trudno jest w ogóle zacząć. Stworzyliśmy zestaw ludzkocentrycznych zasad projektowania UX, aby umożliwić deweloperom tworzenie systemów agentowych skoncentrowanych na kliencie, które rozwiązują ich potrzeby biznesowe. Te zasady projektowania nie są narzuconą architekturą, lecz raczej punktem wyjścia dla zespołów definiujących i budujących doświadczenia agentowe.

Ogólnie rzecz biorąc, agenty powinny:

- Poszerzać i zwiększać ludzkie możliwości (burze mózgów, rozwiązywanie problemów, automatyzacja itp.)
- Wypełniać luki w wiedzy (zapewniać szybkie zaznajomienie się z obszarami wiedzy, tłumaczenie itd.)
- Ułatwiać i wspierać współpracę w sposób, w jaki jako jednostki wolimy pracować z innymi
- Sprawiać, że stajemy się lepszymi wersjami samych siebie (np. trener życia/koordynator zadań, pomagający uczyć się regulacji emocji i umiejętności uważności, budowanie odporności itd.)

## Ta lekcja obejmie

- Czym są zasady projektowania agentów
- Jakie wytyczne stosować podczas wdrażania tych zasad
- Przykłady zastosowania zasad projektowania

## Cele nauki

Po ukończeniu tej lekcji będziesz potrafił:

1. Wyjaśnić, czym są zasady projektowania agentów
2. Wyjaśnić wytyczne dotyczące stosowania zasad projektowania agentów
3. Zrozumieć, jak zbudować agenta, korzystając z zasad projektowania agentów

## Zasady projektowania agentów

![Zasady projektowania agentów](../../../translated_images/pl/agentic-design-principles.1cfdf8b6d3cc73c2.webp)

### Agent (Przestrzeń)

To jest środowisko, w którym agent działa. Te zasady pomagają projektować agentów do angażowania się w światy fizyczne i cyfrowe.

- **Łączenie, nie zlewanie** – pomagają łączyć ludzi z innymi ludźmi, wydarzeniami i użyteczną wiedzą, aby umożliwić współpracę i kontakty.
- Agenty pomagają łączyć wydarzenia, wiedzę i ludzi.
- Agenty zbliżają ludzi do siebie. Nie są zaprojektowane, by zastępować lub umniejszać ludzi.
- **Łatwo dostępny, a jednocześnie czasami niewidoczny** – agent działa głównie w tle i tylko delikatnie nas wspiera, gdy jest to istotne i odpowiednie.
  - Agent jest łatwo dostępny i możliwy do znalezienia dla uprawnionych użytkowników na dowolnym urządzeniu lub platformie.
  - Agent obsługuje wielomodalne wejścia i wyjścia (dźwięk, głos, tekst itd.).
  - Agent może płynnie przechodzić między trybem pierwszego i drugiego planu; między proaktywnym a reaktywnym, w zależności od odczuwanych potrzeb użytkownika.
  - Agent może działać w formie niewidocznej, jednak jego procesy tła i współpraca z innymi agentami są przejrzyste i kontrolowane przez użytkownika.

### Agent (Czas)

To, jak agent działa w czasie. Te zasady pomagają projektować agentów współpracujących w przeszłości, teraźniejszości i przyszłości.

- **Przeszłość**: Refleksja nad historią, obejmującą zarówno stan, jak i kontekst.
  - Agent dostarcza bardziej trafne wyniki na podstawie analizy bogatszych danych historycznych wykraczających poza samą sytuację, ludzi czy stany.
  - Agent tworzy powiązania z przeszłych zdarzeń i aktywnie korzysta z pamięci, aby angażować się w bieżące sytuacje.
- **Teraz**: Delikatne wsparcie, nie tylko powiadamianie.
  - Agent stosuje kompleksowe podejście do interakcji z ludźmi. Gdy zdarzy się jakieś wydarzenie, agent wykracza poza statyczne powiadomienie czy inną statyczną formalność. Agent może uprościć procesy lub dynamicznie generować wskazówki, aby skierować uwagę użytkownika w odpowiednim momencie.
  - Agent dostarcza informacje oparte na kontekście środowiska, zmianach społecznych i kulturowych oraz dostosowane do intencji użytkownika.
  - Interakcja z agentem może być stopniowa, rozwijająca się i rosnąca w złożoności, aby wzmacniać użytkowników na dłuższą metę.
- **Przyszłość**: Adaptacja i ewolucja.
  - Agent dostosowuje się do różnych urządzeń, platform i modalności.
  - Agent dopasowuje się do zachowań użytkownika, potrzeb związanych z dostępnością i jest w pełni konfigurowalny.
  - Agent kształtuje się i rozwija poprzez ciągłą interakcję z użytkownikiem.

### Agent (Rdzeń)

To są kluczowe elementy w rdzeniu projektu agenta.

- **Akceptuj niepewność, ale buduj zaufanie**.
  - Oczekuje się pewnego poziomu niepewności agenta. Niepewność jest kluczowym elementem projektowania agenta.
  - Zaufanie i przejrzystość są fundamentem projektu agenta.
  - Ludzie kontrolują, kiedy agent jest włączony/wyłączony, a status agenta jest zawsze wyraźnie widoczny.

## Wytyczne do wdrażania tych zasad

Korzystając z powyższych zasad projektowania, stosuj następujące wytyczne:

1. **Przejrzystość**: Informuj użytkownika o zaangażowaniu AI, jak działa (w tym działania przeszłe) oraz jak przekazywać opinię i modyfikować system.
2. **Kontrola**: Umożliwiaj użytkownikowi dostosowanie, określanie preferencji i personalizację oraz kontrolę nad systemem i jego atrybutami (w tym możliwość zapomnienia).
3. **Spójność**: Dąż do spójnych, wielomodalnych doświadczeń na różnych urządzeniach i punktach końcowych. Stosuj znane elementy UI/UX tam, gdzie to możliwe (np. ikona mikrofonu dla interakcji głosowej) i minimalizuj obciążenie poznawcze klienta (np. dąż do zwięzłych odpowiedzi, pomocy wizualnych i treści „Dowiedz się więcej”).

## Jak zaprojektować Agenta Podróży, korzystając z tych zasad i wytycznych

Wyobraź sobie, że projektujesz Agenta Podróży, oto jak możesz podejść do wykorzystania Zasad Projektowania i Wytycznych:

1. **Przejrzystość** – Poinformuj użytkownika, że Agent Podróży jest agentem zasilanym AI. Podaj podstawowe instrukcje, jak rozpocząć (np. wiadomość „Witaj”, przykładowe polecenia). Wyraźnie udokumentuj to na stronie produktu. Pokaż listę poleceń, które użytkownik zadał wcześniej. Jasno pokaż, jak przekazywać opinię (kciuki w górę i w dół, przycisk „Wyślij opinię” itp.). Wyraźnie zaznacz, czy agent ma ograniczenia dotyczące użycia lub tematu.
2. **Kontrola** – Upewnij się, że użytkownik wie, jak może modyfikować Agenta po jego utworzeniu, np. za pomocą Promptu Systemowego. Pozwól użytkownikowi wybrać, jak rozbudowany jest Agent, jego styl pisania i ewentualne zastrzeżenia dotyczące tematów, których Agent nie powinien poruszać. Pozwól użytkownikowi przeglądać i usuwać powiązane pliki lub dane, promptów i wcześniejszych rozmów.
3. **Spójność** – Upewnij się, że ikony do udostępniania poleceń, dodawania plików lub zdjęć oraz oznaczania kogoś lub czegoś są standardowe i rozpoznawalne. Użyj ikony spinacza, aby wskazać przesyłanie/udostępnianie plików agentowi, a ikony obrazu do wskazania przesyłania grafiki.

## Przykładowe kody

- Python: [Agent Framework](./code_samples/03-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/03-dotnet-agent-framework.md)


## Masz więcej pytań dotyczących wzorców projektowania agentów AI?

Dołącz do [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), aby spotkać innych uczących się, uczestniczyć w dyżurach i uzyskać odpowiedzi na pytania dotyczące agentów AI.

## Dodatkowe zasoby

- <a href="https://openai.com" target="_blank">Praktyki zarządzania systemami AI Agentowymi | OpenAI</a>
- <a href="https://microsoft.com" target="_blank">Projekt HAX Toolkit - Microsoft Research</a>
- <a href="https://responsibleaitoolbox.ai" target="_blank">Odpowiedzialne narzędzia AI</a>

## Poprzednia lekcja

[Eksplorowanie ram agentowych](../02-explore-agentic-frameworks/README.md)

## Następna lekcja

[Wzorzec użycia narzędzi](../04-tool-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->