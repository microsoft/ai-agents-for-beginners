<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "8164484c16b1ed3287ef9dae9fc437c1",
  "translation_date": "2025-07-24T08:19:05+00:00",
  "source_file": "10-ai-agents-production/README.md",
  "language_code": "pl"
}
-->
# Agenci AI w Produkcji: Obserwowalność i Ocena

Gdy agenci AI przechodzą od eksperymentalnych prototypów do aplikacji w rzeczywistym świecie, kluczowe staje się zrozumienie ich zachowania, monitorowanie wydajności oraz systematyczna ocena ich wyników.

## Cele Nauki

Po ukończeniu tej lekcji będziesz wiedzieć, jak:
- Zrozumieć podstawowe pojęcia związane z obserwowalnością i oceną agentów
- Stosować techniki poprawy wydajności, kosztów i skuteczności agentów
- Systematycznie oceniać swoich agentów AI
- Kontrolować koszty podczas wdrażania agentów AI do produkcji
- Instrumentować agentów zbudowanych za pomocą AutoGen

Celem jest wyposażenie Cię w wiedzę, która pozwoli przekształcić "czarne skrzynki" w przejrzyste, zarządzalne i niezawodne systemy.

_**Uwaga:** Ważne jest, aby wdrażać agentów AI, którzy są bezpieczni i godni zaufania. Sprawdź lekcję [Budowanie Godnych Zaufania Agentów AI](./06-building-trustworthy-agents/README.md)._

## Ślady i Spany

Narzędzia do obserwowalności, takie jak [Langfuse](https://langfuse.com/) czy [Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry), zazwyczaj przedstawiają działania agentów jako ślady i spany.

- **Ślad** reprezentuje pełne zadanie agenta od początku do końca (np. obsługa zapytania użytkownika).
- **Spany** to poszczególne kroki w ramach śladu (np. wywołanie modelu językowego lub pobranie danych).

![Drzewo śladów w Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/trace-tree.png)

Bez obserwowalności agent AI może wydawać się "czarną skrzynką" – jego wewnętrzny stan i rozumowanie są nieprzejrzyste, co utrudnia diagnozowanie problemów lub optymalizację wydajności. Dzięki obserwowalności agenci stają się "szklanymi skrzynkami", oferując przejrzystość, która jest kluczowa dla budowania zaufania i zapewnienia, że działają zgodnie z zamierzeniami.

## Dlaczego Obserwowalność Ma Znaczenie w Środowiskach Produkcyjnych

Przeniesienie agentów AI do środowisk produkcyjnych wprowadza nowe wyzwania i wymagania. Obserwowalność przestaje być "miłym dodatkiem" i staje się kluczową funkcją:

*   **Debugowanie i Analiza Przyczynowa**: Gdy agent zawodzi lub generuje nieoczekiwany wynik, narzędzia do obserwowalności dostarczają śladów potrzebnych do zidentyfikowania źródła błędu. Jest to szczególnie ważne w przypadku złożonych agentów, które mogą obejmować wiele wywołań LLM, interakcje z narzędziami i logikę warunkową.
*   **Zarządzanie Opóźnieniami i Kosztami**: Agenci AI często polegają na LLM i innych zewnętrznych API, które są rozliczane za token lub wywołanie. Obserwowalność umożliwia precyzyjne śledzenie tych wywołań, pomagając zidentyfikować operacje, które są zbyt wolne lub kosztowne. Dzięki temu zespoły mogą optymalizować podpowiedzi, wybierać bardziej wydajne modele lub przeprojektowywać przepływy pracy, aby zarządzać kosztami operacyjnymi i zapewnić dobrą jakość doświadczenia użytkownika.
*   **Zaufanie, Bezpieczeństwo i Zgodność**: W wielu aplikacjach ważne jest, aby agenci działali bezpiecznie i etycznie. Obserwowalność zapewnia ścieżkę audytu działań i decyzji agenta. Może być używana do wykrywania i łagodzenia problemów, takich jak wstrzykiwanie podpowiedzi, generowanie szkodliwych treści czy niewłaściwe obchodzenie się z danymi osobowymi (PII). Na przykład można przejrzeć ślady, aby zrozumieć, dlaczego agent udzielił określonej odpowiedzi lub użył konkretnego narzędzia.
*   **Pętle Ciągłego Doskonalenia**: Dane z obserwowalności stanowią podstawę iteracyjnego procesu rozwoju. Monitorując, jak agenci radzą sobie w rzeczywistym świecie, zespoły mogą identyfikować obszary do poprawy, zbierać dane do dostrajania modeli i weryfikować wpływ zmian. Tworzy to pętlę sprzężenia zwrotnego, w której wnioski z oceny online informują eksperymenty offline i udoskonalenia, prowadząc do stopniowej poprawy wydajności agentów.

## Kluczowe Metryki do Śledzenia

Aby monitorować i zrozumieć zachowanie agenta, należy śledzić szereg metryk i sygnałów. Choć konkretne metryki mogą się różnić w zależności od celu agenta, niektóre są uniwersalnie ważne.

Oto niektóre z najczęściej monitorowanych metryk przez narzędzia do obserwowalności:

**Opóźnienia:** Jak szybko agent odpowiada? Długie czasy oczekiwania negatywnie wpływają na doświadczenie użytkownika. Należy mierzyć opóźnienia dla zadań i poszczególnych kroków, śledząc działania agenta. Na przykład agent, który potrzebuje 20 sekund na wszystkie wywołania modelu, może zostać przyspieszony poprzez użycie szybszego modelu lub równoległe wykonywanie wywołań modelu.

**Koszty:** Jaki jest koszt na jedno działanie agenta? Agenci AI polegają na wywołaniach LLM rozliczanych za token lub zewnętrznych API. Częste użycie narzędzi lub wiele podpowiedzi może szybko zwiększyć koszty. Na przykład, jeśli agent wywołuje LLM pięć razy dla marginalnej poprawy jakości, należy ocenić, czy koszt jest uzasadniony, czy można zmniejszyć liczbę wywołań lub użyć tańszego modelu. Monitorowanie w czasie rzeczywistym może również pomóc w identyfikacji nieoczekiwanych skoków (np. błędów powodujących nadmierne pętle API).

**Błędy Żądań:** Ile żądań agenta zakończyło się niepowodzeniem? Może to obejmować błędy API lub nieudane wywołania narzędzi. Aby uczynić agenta bardziej odpornym w produkcji, można ustawić mechanizmy awaryjne lub ponowne próby. Na przykład, jeśli dostawca LLM A jest niedostępny, można przełączyć się na dostawcę LLM B jako zapas.

**Opinie Użytkowników:** Bezpośrednie oceny użytkowników dostarczają cennych informacji. Może to obejmować oceny (👍kciuk w górę/👎w dół, ⭐1-5 gwiazdek) lub komentarze tekstowe. Stała negatywna opinia powinna być sygnałem alarmowym, że agent nie działa zgodnie z oczekiwaniami.

**Ukryte Opinie Użytkowników:** Zachowania użytkowników dostarczają pośrednich informacji zwrotnych, nawet bez wyraźnych ocen. Może to obejmować natychmiastowe przeformułowanie pytania, powtarzające się zapytania lub kliknięcie przycisku ponownego wywołania. Na przykład, jeśli użytkownicy wielokrotnie zadają to samo pytanie, jest to znak, że agent nie działa zgodnie z oczekiwaniami.

**Dokładność:** Jak często agent generuje poprawne lub pożądane wyniki? Definicje dokładności mogą się różnić (np. poprawność rozwiązywania problemów, dokładność wyszukiwania informacji, satysfakcja użytkownika). Pierwszym krokiem jest zdefiniowanie, jak wygląda sukces dla Twojego agenta. Można śledzić dokładność za pomocą automatycznych kontroli, wyników oceny lub etykiet ukończenia zadań. Na przykład oznaczanie śladów jako "udane" lub "nieudane".

**Automatyczne Metryki Oceny:** Można również ustawić automatyczne oceny. Na przykład można użyć LLM do oceny wyników agenta, np. czy są pomocne, dokładne czy nie. Istnieje również kilka bibliotek open source, które pomagają oceniać różne aspekty agenta, np. [RAGAS](https://docs.ragas.io/) dla agentów RAG lub [LLM Guard](https://llm-guard.com/) do wykrywania szkodliwego języka lub wstrzykiwania podpowiedzi.

W praktyce kombinacja tych metryk daje najlepszy obraz zdrowia agenta AI. W [przykładowym notatniku](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb) w tym rozdziale pokażemy, jak te metryki wyglądają w rzeczywistych przykładach, ale najpierw nauczymy się, jak wygląda typowy przepływ pracy oceny.

## Instrumentacja Twojego Agenta

Aby zbierać dane śledzenia, musisz zainstrumentować swój kod. Celem jest instrumentacja kodu agenta, aby emitował ślady i metryki, które mogą być przechwytywane, przetwarzane i wizualizowane przez platformę obserwowalności.

**OpenTelemetry (OTel):** [OpenTelemetry](https://opentelemetry.io/) stało się standardem branżowym w zakresie obserwowalności LLM. Zapewnia zestaw API, SDK i narzędzi do generowania, zbierania i eksportowania danych telemetrycznych.

Istnieje wiele bibliotek instrumentacji, które opakowują istniejące frameworki agentów i ułatwiają eksportowanie spanów OpenTelemetry do narzędzia obserwowalności. Poniżej znajduje się przykład instrumentacji agenta AutoGen za pomocą biblioteki [OpenLit](https://github.com/openlit/openlit):

```python
import openlit

openlit.init(tracer = langfuse._otel_tracer, disable_batch = True)
```

[Przykładowy notatnik](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb) w tym rozdziale pokaże, jak zainstrumentować swojego agenta AutoGen.

**Ręczne Tworzenie Spanów:** Chociaż biblioteki instrumentacji zapewniają dobrą bazę, często zdarzają się przypadki, w których potrzebne są bardziej szczegółowe lub niestandardowe informacje. Można ręcznie tworzyć spany, aby dodać niestandardową logikę aplikacji. Co ważniejsze, można wzbogacić automatycznie lub ręcznie tworzone spany o niestandardowe atrybuty (znane również jako tagi lub metadane). Te atrybuty mogą obejmować dane specyficzne dla biznesu, obliczenia pośrednie lub dowolny kontekst, który może być przydatny do debugowania lub analizy, takie jak `user_id`, `session_id` czy `model_version`.

Przykład ręcznego tworzenia śladów i spanów za pomocą [Langfuse Python SDK](https://langfuse.com/docs/sdk/python/sdk-v3):

```python
from langfuse import get_client
 
langfuse = get_client()
 
span = langfuse.start_span(name="my-span")
 
span.end()
```

## Ocena Agenta

Obserwowalność dostarcza metryk, ale ocena to proces analizowania tych danych (i przeprowadzania testów), aby określić, jak dobrze działa agent AI i jak można go poprawić. Innymi słowy, gdy masz ślady i metryki, jak ich użyć do oceny agenta i podejmowania decyzji?

Regularna ocena jest ważna, ponieważ agenci AI często są niedeterministyczni i mogą ewoluować (poprzez aktualizacje lub zmiany w zachowaniu modelu) – bez oceny nie wiedziałbyś, czy Twój "inteligentny agent" faktycznie dobrze wykonuje swoją pracę, czy też jego wydajność się pogorszyła.

Istnieją dwie kategorie ocen dla agentów AI: **ocena offline** i **ocena online**. Obie są wartościowe i wzajemnie się uzupełniają. Zazwyczaj zaczynamy od oceny offline, ponieważ jest to minimalny konieczny krok przed wdrożeniem agenta.

### Ocena Offline

![Elementy zbioru danych w Langfuse](https://langfuse.com/images/cookbook/example-autogen-evaluation/example-dataset.png)

Polega na ocenie agenta w kontrolowanym środowisku, zazwyczaj przy użyciu zestawów testowych, a nie zapytań użytkowników na żywo. Używasz przygotowanych zestawów danych, gdzie znasz oczekiwany wynik lub poprawne zachowanie, a następnie uruchamiasz na nich swojego agenta.

Na przykład, jeśli stworzyłeś agenta rozwiązującego matematyczne problemy tekstowe, możesz mieć [zestaw testowy](https://huggingface.co/datasets/gsm8k) zawierający 100 problemów z znanymi odpowiedziami. Ocena offline jest często przeprowadzana podczas rozwoju (i może być częścią pipeline'ów CI/CD), aby sprawdzić ulepszenia lub zapobiec regresjom. Korzyścią jest to, że jest **powtarzalna i można uzyskać jasne metryki dokładności, ponieważ masz prawdę podstawową**. Możesz również symulować zapytania użytkowników i mierzyć odpowiedzi agenta w porównaniu do idealnych odpowiedzi lub używać automatycznych metryk, jak opisano wcześniej.

Głównym wyzwaniem w ocenie offline jest zapewnienie, że Twój zestaw testowy jest wszechstronny i pozostaje aktualny – agent może dobrze radzić sobie na stałym zestawie testowym, ale napotkać zupełnie inne zapytania w produkcji. Dlatego należy regularnie aktualizować zestawy testowe o nowe przypadki brzegowe i przykłady odzwierciedlające scenariusze rzeczywiste​. Przydatne jest połączenie małych zestawów "testów dymnych" i większych zestawów oceny: małe zestawy do szybkich kontroli i większe do szerszych metryk wydajności​.

### Ocena Online

![Przegląd metryk obserwowalności](https://langfuse.com/images/cookbook/example-autogen-evaluation/dashboard.png)

Odnosi się do oceny agenta w środowisku rzeczywistym, tj. podczas rzeczywistego użytkowania w produkcji. Ocena online polega na monitorowaniu wydajności agenta w interakcjach z rzeczywistymi użytkownikami i ciągłej analizie wyników.

Na przykład możesz śledzić wskaźniki sukcesu, oceny satysfakcji użytkowników lub inne metryki na żywym ruchu. Zaletą oceny online jest to, że **uchwyca rzeczy, których możesz nie przewidzieć w warunkach laboratoryjnych** – możesz obserwować dryf modelu w czasie (jeśli skuteczność agenta pogarsza się wraz ze zmianą wzorców wejściowych) i wychwycić nieoczekiwane zapytania lub sytuacje, które nie były w Twoich danych testowych​. Dostarcza prawdziwego obrazu tego, jak agent zachowuje się w rzeczywistości.

Ocena online często obejmuje zbieranie ukrytych i jawnych opinii użytkowników, jak omówiono wcześniej, a także możliwe uruchamianie testów cieniowych lub testów A/B (gdzie nowa wersja agenta działa równolegle, aby porównać ją z starą). Wyzwaniem jest to, że może być trudno uzyskać wiarygodne etykiety lub oceny dla interakcji na żywo – możesz polegać na opiniach użytkowników lub metrykach downstream (np. czy użytkownik kliknął wynik).

### Łączenie obu metod

Oceny online i offline nie wykluczają się wzajemnie; są bardzo komplementarne. Wnioski z monitorowania online (np. nowe typy zapytań użytkowników, w których agent radzi sobie słabo) mogą być używane do uzupełniania i poprawy zestawów testowych offline. Z kolei agenci, którzy dobrze radzą sobie w testach offline, mogą być bardziej pewnie wdrażani i monitorowani online.

W rzeczywistości wiele zespołów przyjmuje pętlę:

_ocena offline -> wdrożenie -> monitorowanie online -> zbieranie nowych przypadków błędów -> dodanie do zestawu offline -> udoskonalenie agenta -> powtórzenie_.

## Typowe Problemy

Podczas wdrażania agentów AI do produkcji możesz napotkać różne wyzwania. Oto niektóre typowe problemy i ich potencjalne rozwiązania:

| **Problem**    | **Potencjalne Rozwiązanie**   |
| ------------- | ------------------ |
| Agent AI nie wykonuje zadań konsekwentnie | - Doprecyzuj podpowiedź przekazywaną agentowi AI; bądź jasny co do celów.<br>- Zidentyfikuj, gdzie podział zadań na podzadania i obsługa ich przez wielu agentów może pomóc. |
| Agent AI wpada w ciągłe pętle  | - Upewnij się, że masz jasne warunki zakończenia procesu, aby agent wiedział, kiedy zakończyć.<br>- Dla złożonych zadań wymagających rozumowania i planowania użyj większego modelu specjalizującego się w zadaniach rozumowania. |
| Wywo

- Udoskonal zdefiniowane parametry, podpowiedzi i nazewnictwo narzędzi.  |
| System Multi-Agent nie działa spójnie | - Ulepsz podpowiedzi przekazywane każdemu agentowi, aby były bardziej precyzyjne i różniły się od siebie.<br>- Zbuduj hierarchiczny system, wykorzystując agenta "routingowego" lub kontrolera, który określi, który agent jest właściwy. |

Wiele z tych problemów można skuteczniej zidentyfikować, jeśli wprowadzona jest obserwowalność. Ślady i metryki, o których wspomnieliśmy wcześniej, pomagają dokładnie określić, w którym miejscu w przepływie pracy agenta występują problemy, co znacznie ułatwia debugowanie i optymalizację.

## Zarządzanie kosztami

Oto kilka strategii zarządzania kosztami wdrażania agentów AI do produkcji:

**Korzystanie z mniejszych modeli:** Małe modele językowe (SLM) mogą dobrze sprawdzać się w niektórych przypadkach użycia agentów i znacząco obniżyć koszty. Jak wspomniano wcześniej, stworzenie systemu oceny, który pozwoli porównać wydajność w stosunku do większych modeli, jest najlepszym sposobem, aby zrozumieć, jak dobrze SLM sprawdzi się w Twoim przypadku użycia. Rozważ użycie SLM do prostszych zadań, takich jak klasyfikacja intencji czy ekstrakcja parametrów, a większe modele zarezerwuj dla bardziej złożonego rozumowania.

**Korzystanie z modelu routingowego:** Podobną strategią jest wykorzystanie różnorodnych modeli o różnych rozmiarach. Możesz użyć LLM/SLM lub funkcji bezserwerowej, aby kierować żądania w zależności od ich złożoności do najlepiej dopasowanych modeli. To również pomoże obniżyć koszty, jednocześnie zapewniając odpowiednią wydajność dla właściwych zadań. Na przykład, kieruj proste zapytania do mniejszych, szybszych modeli, a drogie, duże modele wykorzystuj tylko do złożonych zadań wymagających rozumowania.

**Buforowanie odpowiedzi:** Identyfikowanie typowych żądań i zadań oraz dostarczanie odpowiedzi przed ich przejściem przez system agentów to dobry sposób na zmniejszenie liczby podobnych żądań. Możesz nawet wdrożyć proces identyfikacji, jak bardzo dane żądanie jest podobne do już zbuforowanych, korzystając z prostszych modeli AI. Ta strategia może znacząco obniżyć koszty w przypadku często zadawanych pytań lub typowych przepływów pracy.

## Zobaczmy, jak to działa w praktyce

W [przykładowym notebooku tej sekcji](../../../10-ai-agents-production/code_samples/10_autogen_evaluation.ipynb) zobaczymy przykłady, jak możemy wykorzystać narzędzia obserwowalności do monitorowania i oceny naszego agenta.

## Poprzednia lekcja

[Wzorzec projektowy metapoznania](../09-metacognition/README.md)

## Następna lekcja

[MCP](../11-mcp/README.md)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.