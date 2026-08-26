# Tworzenie agentów do korzystania z komputera (CUA)

Agenci do korzystania z komputera mogą wchodzić w interakcje ze stronami internetowymi tak samo, jak robiłaby to osoba: otwierając przeglądarkę, przeglądając stronę i podejmując najlepszą kolejną akcję na podstawie tego, co widzą. W tej lekcji zbudujesz agenta automatyzującego przeglądarkę, który wyszukuje w Airbnb, wyciąga ustrukturyzowane dane ofert i identyfikuje najtańszy pobyt w Sztokholmie.

Lekcja łączy Browser-Use do nawigacji sterowanej przez AI, Playwright i protokół Chrome DevTools (CDP) do kontroli przeglądarki, Azure OpenAI do wnioskowania z wykorzystaniem wizji oraz Pydantic do ustrukturyzowanego wyodrębniania danych.

## Wprowadzenie

Ta lekcja obejmie:

- Zrozumienie, kiedy agenci do korzystania z komputera są lepszym wyborem niż automatyzacja tylko przez API
- Łączenie Browser-Use z Playwright i CDP dla niezawodnego zarządzania cyklem życia przeglądarki
- Wykorzystywanie Azure OpenAI z wizją i ustrukturyzowanym wyjściem Pydantic do wydobywania danych ofert z dynamicznych stron internetowych
- Decydowanie, kiedy używać agent-first, actor-first lub hybrydowego przepływu automatyzacji przeglądarki

## Cele nauki

Po ukończeniu tej lekcji będziesz potrafił:

- Skonfigurować Browser-Use z Azure OpenAI i Playwright
- Stworzyć przepływ pracy automatyzacji przeglądarki, który nawiguję po prawdziwej stronie i obsługuje dynamiczne elementy UI
- Wyodrębniać typowane wyniki z widocznej zawartości strony i zamieniać je na logikę biznesową
- Wybrać między wzorcami agenta i aktora na podstawie przewidywalności zadania przeglądarki

## Przykład kodu

Ta lekcja zawiera jeden samouczek w notatniku:

- [15-browser-user.ipynb](./15-browser-user.ipynb): Uruchamia sesję Chrome przez CDP, wyszukuje oferty Airbnb dla Sztokholmu, wydobywa ceny przy pomocy wizji Browser-Use i zwraca najtańszą opcję jako dane ustrukturyzowane.

## Wymagania wstępne

- Python 3.12+
- Wdrożenie Azure OpenAI skonfigurowane w twoim środowisku
- Lokalnie zainstalowany Chrome lub Chromium
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
# Opcjonalne: domyślnie używa najnowszej wersji API, jeśli pominięte
AZURE_OPENAI_API_VERSION=...
```

## Przegląd architektury

Notatnik demonstruje hybrydowy przepływ automatyzacji przeglądarki:

1. Chrome uruchamia się z włączonym CDP, tak aby Playwright i Browser-Use mogły dzielić tę samą sesję przeglądarki.
2. Agent Browser-Use obsługuje otwarte zadania nawigacyjne, takie jak otwieranie Airbnb, zamykanie wyskakujących okien oraz wyszukiwanie Sztokholmu.
3. Aktywna strona jest badana przy użyciu ustrukturyzowanego schematu Pydantic w celu wydobycia tytułów ofert, cen za noc, ocen i adresów URL.
4. Logika Pythona porównuje wydobyte oferty i wyróżnia najtańszą.

To podejście zachowuje elastyczne, oparte na wizji wnioskowanie, w którym Browser-Use jest dobry, jednocześnie dając deterministyczną kontrolę przeglądarki, gdy jej potrzebujesz.

## Kluczowe wnioski i najlepsze praktyki

### Kiedy używać agenta vs aktora

| Scenariusz | Użyj agenta | Użyj aktora |
|----------|--------------|-------------|
| Dynamiczne układy | Tak, AI potrafi dostosować się do zmian strony | Nie, kruche selektory mogą się zepsuć |
| Znana struktura | Nie, agent jest wolniejszy niż bezpośrednia kontrola | Tak, szybki i precyzyjny |
| Znajdowanie elementów | Tak, język naturalny działa dobrze | Nie, wymagane są dokładne selektory |
| Kontrola czasu | Nie, mniej przewidywalna | Tak, pełna kontrola nad oczekiwaniami i ponownymi próbami |
| Złożone przepływy pracy | Tak, radzi sobie z nieoczekiwanymi stanami UI | Nie, wymaga jawnego rozgałęzienia |

### Najlepsze praktyki Browser-Use

1. Zacznij od agenta do eksploracji i nawigacji dynamicznej.
2. Przejdź do bezpośredniej kontroli strony, gdy interakcja stanie się przewidywalna.
3. Używaj ustrukturyzowanych modeli wyjściowych, aby wydobyte dane były walidowane i typowane.
4. Dodawaj strategiczne opóźnienia po akcjach wywołujących widoczne zmiany UI.
5. Rób zrzuty ekranu podczas iteracji, aby łatwiej diagnozować błędy.
6. Spodziewaj się zmian stron i zaprojektuj strategie awaryjne dla wyskakujących okien i przesunięć układu.
7. Łącz wzorce agenta i aktora, by uzyskać elastyczność i precyzję.

### Zabezpieczenia dla agentów przeglądarki

Agenci przeglądarki działają na stronach na żywo, dlatego potrzebują ściślejszych granic niż skrypt wywołujący tylko znane API. Przed przejściem od demonstracji w notatniku do prawdziwego przepływu, zdefiniuj kontrolę nad tym, co agent może widzieć, kliknąć i przesłać.

1. **Określ zakres środowiska przeglądania.** Uruchom agenta w dedykowanym profilu przeglądarki lub piaskownicy i ogranicz go do domen wymaganych do zadania.
2. **Oddziel obserwację od działania.** Pozwól agentowi najpierw wyszukiwać, czytać i wydobywać dane; wymagać jawnej zgody, zanim prześle formularze, wyśle wiadomości, zarezerwuje podróż, dokona zakupów, usunie rekordy lub zmieni ustawienia konta.
3. **Nie umieszczaj sekretów w promptach i śladach.** Nie umieszczaj haseł, szczegółów płatniczych, ciasteczek sesji ani surowych danych osobowych w kontekście modelu. Pozwól użytkownikowi przejąć uwierzytelnianie i zanonimizować poufne pola w logach.
4. **Traktuj zawartość strony jako niezweryfikowane dane wejściowe.** Strona może zawierać instrukcje przeznaczone dla agenta, a nie dla użytkownika. Agent powinien ignorować tekst strony, który nakazuje zmienić cel, ujawnić dane, wyłączyć zabezpieczenia lub odwiedzić niepowiązane witryny.
5. **Używaj deterministycznych kontroli wokół ryzykownych kroków.** Sprawdź bieżący URL, tytuł strony, wybrany element, cenę, odbiorcę i podsumowanie działania w kodzie przed poproszeniem użytkownika o zatwierdzenie ostatecznego kroku.
6. **Ustal budżety i warunki zatrzymania.** Ogranicz liczbę akcji, ponownych prób, kart i minut, które agent może wykorzystać. Zatrzymaj się, gdy stan strony jest niejednoznaczny, zamiast kontynuować klikanie.
7. **Rejestruj użyteczne dowody, a nie wszystko.** Zachowuj podsumowania działań, znaczniki czasu, URL, opisy wybranych elementów oraz odniesienia do zrzutów ekranu, aby można było przejrzeć błędy bez przechowywania zbędnej wrażliwej zawartości strony.

W przykładzie Airbnb bezpiecznym domyślnym działaniem jest wyszukiwanie ofert i wydobywanie cen. Logowanie, kontakt z gospodarzem czy finalizacja rezerwacji powinny być osobnymi działaniami zatwierdzanymi przez użytkownika.

### Zastosowania w rzeczywistym świecie

- Rezerwacje podróży i monitorowanie cen
- Porównywanie cen i sprawdzanie dostępności w e-commerce
- Ustrukturyzowane wydobywanie z dynamicznych witryn internetowych
- Testowanie i weryfikacja UI z wykorzystaniem wizji
- Monitorowanie stron internetowych i powiadamianie
- Inteligentne wypełnianie formularzy w wieloetapowych procesach

## Przykład z życia: Microsoft Project Opal

Agent, którego zbudujesz w tej lekcji, jest małą, lokalną wersją **agenta do korzystania z komputera (CUA)** — programu sterującego przeglądarką tak, jak robiłaby to osoba. Microsoft wprowadza ten sam pomysł do przedsiębiorstw za pomocą **[Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)**, funkcji w Microsoft 365 Copilot.

W Project Opal opisujesz zadanie, a agent działa w twoim imieniu, korzystając z **użytkowania komputera na bezpiecznym Windows 365 Cloud PC**, operując w przeglądarkowych aplikacjach, witrynach i danych twojej organizacji. Działa **asynchronicznie w tle**, a ty możesz w każdej chwili kierować pracą lub przejąć kontrolę. Przykładowe zadania to:

- Zarządzanie prośbami o członkostwo w grupach zabezpieczeń
- Zbieranie i walidacja dowodów audytu dla przeglądów zgodności
- Obsługa incydentów IT (aktualizacja statusu zgłoszenia, przypisywanie właścicieli, zamykanie duplikatów)
- Kompilowanie danych Excel do zestawienia zamknięcia finansowego

Opal jest dobrym punktem odniesienia dla tego, jak wygląda **produkcjonowy, godny zaufania** agent do korzystania z komputera — i wzmacnia pojęcia z poprzednich lekcji:

| Koncepcja z tego kursu | Jak Project Opal ją stosuje |
|------------------------|-----------------------------|
| **Człowiek w pętli** (Lekcja 06) | Opal zatrzymuje się na dane logowania, dane wrażliwe lub niejednoznaczne instrukcje i nigdy nie wpisuje haseł ani nie wysyła formularzy bez wyraźnego potwierdzenia. Możesz *Przejąć kontrolę* i *Zwrócić kontrolę* w trakcie zadania. |
| **Godni zaufania i bezpieczni agenci** (Lekcje 06 i 18) | Uruchamia się w izolowanym Windows 365 Cloud PC, z domyślną kontrolą tylko przeglądarki (inny dostęp do komputera zablokowany, wymuszany przez Intune), używa *twojej* tożsamości, więc uzyskuje dostęp tylko do tego, do czego masz uprawnienia, i loguje każde działanie dla audytowalności. |
| **Planowanie i metapoznanie** (Lekcje 07 i 09) | Opal najpierw generuje plan zadania, następnie nadzoruje własne wnioskowanie na każdym kroku i zatrzymuje się, jeśli wykryje podejrzaną aktywność. |
| **Ponownie używalne zdolności / narzędzia** (Lekcja 04) | **Umiejętności** pozwalają pisać instrukcje dla powtarzalnych zadań (importowane z pliku `.md` lub tworzone z Opalem) i używać ich w różnych rozmowach. |

> **Dostępność:** Projekt Opal jest obecnie dostępny dla użytkowników w [programie wczesnego dostępu Frontier](https://adoption.microsoft.com/copilot/frontier-program/) z subskrypcją Microsoft 365 Copilot, a administrator musi zakończyć konfigurację. Ponieważ jest to eksperymentalna funkcja Frontier, możliwości mogą z czasem się zmieniać.

## Sprawdzenie wiedzy

Sprawdź swoje zrozumienie przed przejściem do następnej lekcji.

**1. Kiedy agent do korzystania z przeglądarki jest lepszym wyborem niż przepływ pracy tylko przez API?**

<details>
<summary>Odpowiedź</summary>

Użyj agenta przeglądarki, gdy zadanie zależy od tego, co jest widoczne w interfejsie webowym, strona nie udostępnia potrzebnego API lub strona zmienia się na tyle często, że stała logika API lub selektorów byłaby krucha. Jeśli istnieje stabilne API dla tego samego zadania, preferuj API, ponieważ jest zwykle szybsze, łatwiejsze do testowania i bezpieczniejsze.
</details>

**2. W hybrydowym przepływie pracy, które części powinny obsługiwać agent, a które bezpośredni kod Playwright?**

<details>
<summary>Odpowiedź</summary>

Pozwól agentowi obsłużyć otwartą nawigację i dynamiczne stany UI, takie jak odnalezienie właściwej strony czy zamknięcie nieoczekiwanych wyskakujących okien. Przełącz się na bezpośrednią kontrolę Playwright, gdy struktura strony jest znana, a działanie wymaga precyzji, ponownych prób, oczekiwań lub deterministycznej walidacji.
</details>

**3. Przykład Airbnb znajduje ofertę, którą użytkownik może chcieć zarezerwować. Co powinno się zdarzyć, zanim przepływ pracy się zaloguje, skontaktuje z gospodarzem lub ukończy rezerwację?**

<details>
<summary>Odpowiedź</summary>

Przepływ pracy powinien się zatrzymać i poprosić o wyraźną zgodę użytkownika. Przed tym powinien pokazać przejrzyste podsumowanie wybranej oferty, aktualnego URL, ceny, dat i zamierzonego działania. Wyszukiwanie i wydobywanie cen może być autonomiczne; dostęp do konta, wiadomości, zakupy i rezerwacje powinny być zatwierdzane przez użytkownika.
</details>

**4. Strona internetowa mówi agentowi, aby zignorował swoje pierwotne instrukcje, odwiedził inną witrynę i ujawnił zapisane dane uwierzytelniające. Jak agent powinien traktować ten tekst?**

<details>
<summary>Odpowiedź</summary>

Traktuj to jako niezweryfikowaną zawartość strony, a nie jako instrukcję dewelopera lub użytkownika. Agent powinien pozostać w dozwolonej domenie i zakresie zadania, odmówić ujawnienia sekretów oraz unikać podążania za tekstem strony, który zmienia cel, wyłącza zabezpieczenia lub wysyła go na niepowiązane witryny.
</details>

**5. Jakie dowody warto przechowywać podczas działania agenta przeglądarki, a czego należy unikać?**

<details>
<summary>Odpowiedź</summary>

Zachowuj podsumowania działań, znaczniki czasu, URL, opisy wybranych elementów, wyniki walidacji oraz odniesienia do zrzutów ekranu, aby można było przeglądnąć przebieg działania. Unikaj przechowywania haseł, danych do płatności, ciasteczek sesji, surowych danych osobowych czy pełnej zawartości strony, chyba że istnieje specyficzny powód dotyczący przechowywania i prywatności.
</details>

## Dodatkowe zasoby

- [Zacznij z Project Opal (Frontier)](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-project-opal-frontier)
- [Szablon integracji Browser-Use Playwright](https://docs.browser-use.com/examples/templates/playwright-integration)
- [Parametry aktora Browser-Use i ekstrakcja zawartości](https://docs.browser-use.com/customize/actor/all-parameters)
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