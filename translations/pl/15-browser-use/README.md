# Tworzenie Agentów Używających Komputera (CUA)

Agenci używający komputera mogą wchodzić w interakcje ze stronami internetowymi tak samo, jak robiłaby to osoba: otwierając przeglądarkę, przeglądając stronę i podejmując najlepszą kolejną akcję na podstawie tego, co widzą. W tej lekcji zbudujesz agenta automatyzującego przeglądarkę, który wyszukuje w serwisie Airbnb, wyodrębnia ustrukturyzowane dane ogłoszeń i identyfikuje najtańszy nocleg w Sztokholmie.

Lekcja łączy Browser-Use do nawigacji sterowanej przez AI, Playwright i Chrome DevTools Protocol (CDP) do kontroli przeglądarki, Azure OpenAI do rozumowania z wykorzystaniem widzenia oraz Pydantic do ustrukturyzowanego wyodrębniania danych.

## Wprowadzenie

Ta lekcja obejmie:

- Zrozumienie, kiedy agenci używający komputera są lepszym rozwiązaniem niż automatyzacja wyłącznie przez API
- Łączenie Browser-Use z Playwright i CDP do niezawodnego zarządzania cyklem życia przeglądarki
- Korzystanie z Azure OpenAI z wizją oraz strukturalny wynik Pydantic do wyodrębnienia danych ogłoszeń ze stron dynamicznych
- Decydowanie, kiedy użyć pracy agenta-first, actor-first lub hybrydowego workflow automatyzacji przeglądarki

## Cele nauki

Po ukończeniu tej lekcji będziesz potrafił:

- Skonfigurować Browser-Use z Azure OpenAI i Playwright
- Zbudować workflow automatyzacji przeglądarki, który porusza się po prawdziwej stronie internetowej i obsługuje dynamiczne elementy interfejsu użytkownika
- Wyodrębniać typowane wyniki z widocznych treści strony i przekształcać je w dalszą logikę biznesową
- Wybierać wzorce agenta i aktora w zależności od przewidywalności zadania w przeglądarce

## Przykład kodu

Ta lekcja zawiera jeden tutorial w notatniku:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Uruchamia sesję Chrome przez CDP, wyszukuje ogłoszenia Airbnb w Sztokholmie, wyodrębnia ceny za pomocą widzenia Browser-Use i zwraca najtańszą opcję jako ustrukturyzowane dane.

## Wymagania wstępne

- Python 3.12+
- Skonfigurowana wdrożenie Azure OpenAI w Twoim środowisku
- Lokalne zainstalowanie Chrome lub Chromium
- Zainstalowane zależności Playwright
- Podstawowa znajomość asynchronicznego Pythona

## Konfiguracja

Zainstaluj pakiety używane w notatniku:

```bash
pip install browser_use playwright python-dotenv
playwright install chromium
```

Ustaw zmienne środowiskowe Azure OpenAI używane przez notatnik:

```bash
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=...
# Opcjonalne: domyślnie najnowsza wersja API, jeśli pominięta
AZURE_OPENAI_API_VERSION=...
```

## Przegląd architektury

Notatnik demonstruje hybrydowy workflow automatyzacji przeglądarki:

1. Chrome uruchamia się z aktywowanym CDP, aby zarówno Playwright, jak i Browser-Use mogły współdzielić tę samą sesję przeglądarki.
2. Agent Browser-Use obsługuje otwarte zadania nawigacyjne, takie jak otwieranie Airbnb, zamykanie wyskakujących okienek i wyszukiwanie Sztokholmu.
3. Aktywna strona jest przeglądana ze schematem Pydantic, aby wyodrębnić tytuły ogłoszeń, ceny za noc, oceny i adresy URL.
4. Logika Pythona porównuje wyodrębnione ogłoszenia i wyróżnia najtańszą ofertę.

To podejście utrzymuje elastyczne, oparte na widzeniu rozumowanie, z którego Browser-Use słynie, jednocześnie dając deterministyczną kontrolę nad przeglądarką, gdy jest potrzebna.

## Kluczowe wnioski i najlepsze praktyki

### Kiedy używać agenta, a kiedy aktora

| Scenariusz | Użyj agenta | Użyj aktora |
|----------|-----------|-----------|
| Dynamiczne układy | Tak, AI może dostosować się do zmian strony | Nie, kruche selektory mogą się zepsuć |
| Znana struktura | Nie, agent jest wolniejszy niż bezpośrednia kontrola | Tak, szybki i precyzyjny |
| Znajdowanie elementów | Tak, język naturalny działa dobrze | Nie, wymagane są precyzyjne selektory |
| Kontrola czasu | Nie, mniej przewidywalne | Tak, pełna kontrola nad oczekiwaniami i ponownymi próbami |
| Złożone workflow | Tak, obsługuje nieoczekiwane stany UI | Nie, wymaga jawnych rozgałęzień |

### Najlepsze praktyki Browser-Use

1. Zacznij od agenta do eksploracji i nawigacji dynamicznej.
2. Przełącz się na bezpośrednią kontrolę strony, gdy interakcja stanie się przewidywalna.
3. Używaj ustrukturyzowanych modeli wyjściowych, aby wyodrębnione dane były zwalidowane i bezpieczne typowo.
4. Dodawaj opóźnienia strategicznie po akcjach wywołujących widoczne zmiany UI.
5. Rób zrzuty ekranu podczas iteracji, aby łatwiej debugować błędy.
6. Spodziewaj się zmian stron i projektuj strategie awaryjne dla wyskakujących okienek i przesunięć układu.
7. Łącz wzorce agenta i aktora, aby zyskać zarówno elastyczność, jak i precyzję.

### Środki bezpieczeństwa dla agentów przeglądarki

Agenci przeglądarki działają na żywych stronach internetowych, więc potrzebują ściślejszych ograniczeń niż skrypt, który wywołuje tylko znane API. Zanim przejdziesz z demonstracji w notatniku do prawdziwego workflow, zdefiniuj kontrolę nad tym, co agent może widzieć, klikać i wysyłać.

1. **Określ środowisko przeglądania.** Uruchom agenta w dedykowanym profilu przeglądarki lub sandboxie i ogranicz go do domen niezbędnych do zadania.
2. **Oddziel obserwację od działania.** Pozwól agentowi najpierw wyszukiwać, czytać i wyodrębniać dane; wymagaj jawnej aprobaty przed wysłaniem formularzy, wiadomości, rezerwacjami, zakupami, usuwaniem rekordów lub zmianą ustawień konta.
3. **Nie umieszczaj sekretów w promptach i śladach.** Nie umieszczaj haseł, danych płatności, ciasteczek sesyjnych ani surowych danych osobowych w kontekście modelu. Pozwól użytkownikowi przejąć autoryzację i redagować wrażliwe pola z logów.
4. **Traktuj zawartość strony jako niezweryfikowane dane wejściowe.** Strona internetowa może zawierać instrukcje przeznaczone dla agenta, a nie użytkownika. Agent powinien ignorować tekst na stronie, który prosi o zmianę celu, ujawnienie danych, wyłączenie zabezpieczeń lub odwiedzenie niepowiązanych witryn.
5. **Stosuj deterministyczne kontrole wokół ryzykownych kroków.** Zweryfikuj aktualny URL, tytuł strony, wybrany element, cenę, odbiorcę i podsumowanie akcji w kodzie przed poproszeniem użytkownika o zatwierdzenie końcowego kroku.
6. **Ustaw budżety i warunki zatrzymania.** Ogranicz liczbę akcji, prób ponownych, kart i minut, które agent może użyć. Zatrzymaj się, gdy stan strony jest niejednoznaczny, zamiast kontynuować klikanie.
7. **Rejestruj przydatne dowody, nie wszystko.** Zachowuj podsumowania akcji, znaczniki czasu, URL, opisy wybranych elementów i referencje zrzutów ekranu, aby można było przeanalizować błędy bez przechowywania niepotrzebnych, wrażliwych treści strony.

W przykładzie Airbnb bezpiecznym domyślnym działaniem jest wyszukiwanie ogłoszeń i wyodrębnianie cen. Logowanie, kontakt z gospodarzem lub finalizacja rezerwacji powinny być osobnymi działaniami zatwierdzanymi przez użytkownika.

### Zastosowania w świecie rzeczywistym

- Rezerwacja podróży i monitorowanie cen
- Porównywanie cen i sprawdzanie dostępności w e-commerce
- Ustrukturyzowane wyodrębnianie z dynamicznych stron internetowych
- Testowanie i weryfikacja UI z użyciem widzenia
- Monitorowanie i alarmowanie stron internetowych
- Inteligentne wypełnianie formularzy przez wieloetapowe procesy

## Przykład ze świata rzeczywistego: Microsoft Project Opal

Agent, którego tworzysz w tej lekcji, to mała, lokalna wersja **agenta używającego komputera (CUA)** — programu, który prowadzi przeglądarkę tak jak człowiek. Microsoft wprowadza tę samą ideę do przedsiębiorstw za pomocą **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, funkcji w Microsoft 365 Copilot.

W Project Opal opisujesz zadanie, a agent działa w Twoim imieniu, korzystając z **użycia komputera w bezpiecznym Windows 365 Cloud PC**, operując w aplikacjach, witrynach i danych przeglądarkowych Twojej organizacji. Działa **asynchronicznie w tle**, a Ty możesz w dowolnym momencie prowadzić pracę lub przejąć kontrolę. Przykładowe zadania obejmują:

- Zarządzanie wnioskami o członkostwo w grupach zabezpieczeń
- Zbieranie i weryfikację dowodów audytowych dla przeglądów zgodności
- Obsługę incydentów IT (aktualizacja statusu zgłoszenia, przydzielanie odpowiedzialnych, zamykanie duplikatów)
- Kompilację danych z Excela do zestawu zamknięcia finansowego

Opal jest użytecznym odniesieniem, jak wygląda **producencki, wiarygodny** agent używający komputera — i wzmacnia koncepcje z poprzednich lekcji:

| Koncepcja w tym kursie | Jak Project Opal ją stosuje |
|------------------------|-----------------------------|
| **Człowiek w pętli** (Lekcja 06) | Opal zatrzymuje się na dane logowania, dane wrażliwe lub niejednoznaczne instrukcje i nigdy nie wpisuje haseł ani nie wysyła formularzy bez wyraźnego potwierdzenia. Możesz *Przejąć kontrolę* i *Zwrócić kontrolę* w trakcie zadania. |
| **Wiarygodni i bezpieczni agenci** (Lekcje 06 i 18) | Uruchamia się w izolowanym Windows 365 Cloud PC, domyślnie tylko w przeglądarce (inne dostępy do komputera zablokowane, egzekwowane przez Intune), korzysta z *Twojej* tożsamości, więc ma dostęp tylko do tego, co jesteś uprawniony, i rejestruje każdą akcję dla audytu. |
| **Planowanie i metapoznanie** (Lekcje 07 i 09) | Opal najpierw generuje plan zadania, potem nadzoruje własne rozumowanie na każdym kroku i zatrzymuje się, jeśli wykryje podejrzaną aktywność. |
| **Możliwości / narzędzia wielokrotnego użytku** (Lekcja 04) | **Skills** pozwalają pisać instrukcje dla powtarzalnych zadań (importowane z pliku `.md` lub tworzone w Opal) i używać ich w wielu konwersacjach. |

> **Dostępność:** Project Opal jest obecnie dostępny dla użytkowników w [programie wczesnego dostępu Frontier](https://adoption.microsoft.com/copilot/frontier-program/) z subskrypcją Microsoft 365 Copilot, a administrator musi zakończyć konfigurację. Ponieważ jest to eksperymentalna funkcja Frontier, możliwości mogą się z czasem zmieniać.

## Dodatkowe zasoby

- [Rozpocznij z Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Szablon integracji Browser-Use Playwright](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Parametry aktora Browser-Use i wyodrębnianie treści](https://docs.browser-use.com/customize/actor/all-parameters)
- [Konfiguracja kursu](../00-course-setup/README.md)

## Poprzednia lekcja

[Eksploracja Microsoft Agent Framework](../14-microsoft-agent-framework/README.md)

## Następna lekcja

[Wdrażanie skalowalnych agentów](../16-deploying-scalable-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->