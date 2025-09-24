<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "d2f04b783b9e1253100329afd698f8ff",
  "translation_date": "2025-08-30T14:26:32+00:00",
  "source_file": "05-agentic-rag/README.md",
  "language_code": "pl"
}
-->
[![Agentic RAG](../../../translated_images/lesson-5-thumbnail.20ba9d0c0ae64fae06637eb2023395d437b0152c0463c2227ff456afe5f14644.pl.png)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Kliknij obrazek powyżej, aby obejrzeć wideo z tej lekcji)_

# Agentic RAG

Ta lekcja oferuje kompleksowy przegląd Agentic Retrieval-Augmented Generation (Agentic RAG), nowego paradygmatu AI, w którym duże modele językowe (LLM) autonomicznie planują kolejne kroki, jednocześnie pozyskując informacje z zewnętrznych źródeł. W przeciwieństwie do statycznych wzorców „pobierz i przeczytaj”, Agentic RAG obejmuje iteracyjne wywołania LLM, przeplatane użyciem narzędzi lub funkcji oraz uporządkowanymi wynikami. System ocenia rezultaty, udoskonala zapytania, uruchamia dodatkowe narzędzia, jeśli to konieczne, i kontynuuje ten cykl, aż do osiągnięcia satysfakcjonującego rozwiązania.

## Wprowadzenie

W tej lekcji omówimy:

- **Zrozumienie Agentic RAG:** Poznaj nowy paradygmat w AI, w którym duże modele językowe (LLM) autonomicznie planują kolejne kroki, jednocześnie pozyskując informacje z zewnętrznych źródeł danych.
- **Iteracyjny styl Maker-Checker:** Zrozum pętlę iteracyjnych wywołań LLM, przeplatanych użyciem narzędzi lub funkcji oraz uporządkowanymi wynikami, zaprojektowaną w celu poprawy poprawności i obsługi błędnych zapytań.
- **Praktyczne zastosowania:** Zidentyfikuj scenariusze, w których Agentic RAG sprawdza się najlepiej, takie jak środowiska wymagające wysokiej poprawności, złożone interakcje z bazami danych i rozbudowane przepływy pracy.

## Cele nauki

Po ukończeniu tej lekcji będziesz wiedzieć, jak/zrozumiesz:

- **Zrozumienie Agentic RAG:** Poznaj nowy paradygmat w AI, w którym duże modele językowe (LLM) autonomicznie planują kolejne kroki, jednocześnie pozyskując informacje z zewnętrznych źródeł danych.
- **Iteracyjny styl Maker-Checker:** Zrozum koncepcję pętli iteracyjnych wywołań LLM, przeplatanych użyciem narzędzi lub funkcji oraz uporządkowanymi wynikami, zaprojektowaną w celu poprawy poprawności i obsługi błędnych zapytań.
- **Przejmowanie procesu rozumowania:** Zrozum zdolność systemu do samodzielnego podejmowania decyzji dotyczących sposobu podejścia do problemów, bez polegania na z góry określonych ścieżkach.
- **Przepływ pracy:** Dowiedz się, jak model agentowy samodzielnie decyduje o pobraniu raportów o trendach rynkowych, identyfikacji danych konkurencji, korelacji wewnętrznych metryk sprzedaży, syntezie wyników i ocenie strategii.
- **Iteracyjne pętle, integracja narzędzi i pamięć:** Poznaj zależność systemu od wzorca interakcji w pętli, utrzymującego stan i pamięć na kolejnych etapach, aby unikać powtarzających się pętli i podejmować świadome decyzje.
- **Obsługa trybów awaryjnych i autokorekta:** Zbadaj solidne mechanizmy autokorekty systemu, w tym iterację i ponowne zapytania, korzystanie z narzędzi diagnostycznych oraz powrót do nadzoru ludzkiego.
- **Granice autonomii:** Zrozum ograniczenia Agentic RAG, koncentrując się na autonomii specyficznej dla domeny, zależności od infrastruktury i przestrzeganiu zasad bezpieczeństwa.
- **Praktyczne przypadki użycia i wartość:** Zidentyfikuj scenariusze, w których Agentic RAG sprawdza się najlepiej, takie jak środowiska wymagające wysokiej poprawności, złożone interakcje z bazami danych i rozbudowane przepływy pracy.
- **Zarządzanie, przejrzystość i zaufanie:** Dowiedz się o znaczeniu zarządzania i przejrzystości, w tym wyjaśnialnego rozumowania, kontroli uprzedzeń i nadzoru ludzkiego.

## Czym jest Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) to nowy paradygmat AI, w którym duże modele językowe (LLM) autonomicznie planują kolejne kroki, jednocześnie pozyskując informacje z zewnętrznych źródeł. W przeciwieństwie do statycznych wzorców „pobierz i przeczytaj”, Agentic RAG obejmuje iteracyjne wywołania LLM, przeplatane użyciem narzędzi lub funkcji oraz uporządkowanymi wynikami. System ocenia rezultaty, udoskonala zapytania, uruchamia dodatkowe narzędzia, jeśli to konieczne, i kontynuuje ten cykl, aż do osiągnięcia satysfakcjonującego rozwiązania. Ten iteracyjny styl „maker-checker” poprawia poprawność, obsługuje błędne zapytania i zapewnia wysoką jakość wyników.

System aktywnie przejmuje proces rozumowania, przepisując nieudane zapytania, wybierając różne metody pozyskiwania informacji i integrując wiele narzędzi—takich jak wyszukiwanie wektorowe w Azure AI Search, bazy danych SQL czy niestandardowe API—zanim sfinalizuje swoją odpowiedź. Charakterystyczną cechą systemu agentowego jest jego zdolność do przejmowania procesu rozumowania. Tradycyjne implementacje RAG opierają się na z góry określonych ścieżkach, ale system agentowy autonomicznie określa sekwencję kroków na podstawie jakości znalezionych informacji.

## Definicja Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) to nowy paradygmat w rozwoju AI, w którym LLM nie tylko pozyskują informacje z zewnętrznych źródeł danych, ale także autonomicznie planują kolejne kroki. W przeciwieństwie do statycznych wzorców „pobierz i przeczytaj” lub starannie zaprojektowanych sekwencji promptów, Agentic RAG obejmuje pętlę iteracyjnych wywołań LLM, przeplatanych użyciem narzędzi lub funkcji oraz uporządkowanymi wynikami. Na każdym etapie system ocenia uzyskane wyniki, decyduje, czy udoskonalić zapytania, uruchamia dodatkowe narzędzia, jeśli to konieczne, i kontynuuje ten cykl, aż osiągnie satysfakcjonujące rozwiązanie.

Ten iteracyjny styl „maker-checker” został zaprojektowany w celu poprawy poprawności, obsługi błędnych zapytań do baz danych strukturalnych (np. NL2SQL) i zapewnienia zrównoważonych, wysokiej jakości wyników. Zamiast polegać wyłącznie na starannie zaprojektowanych łańcuchach promptów, system aktywnie przejmuje proces rozumowania. Może przepisywać nieudane zapytania, wybierać różne metody pozyskiwania informacji i integrować wiele narzędzi—takich jak wyszukiwanie wektorowe w Azure AI Search, bazy danych SQL czy niestandardowe API—zanim sfinalizuje swoją odpowiedź. To eliminuje potrzebę stosowania zbyt skomplikowanych frameworków orkiestracyjnych. Zamiast tego stosunkowo prosta pętla „wywołanie LLM → użycie narzędzia → wywołanie LLM → …” może generować zaawansowane i dobrze ugruntowane wyniki.

![Agentic RAG Core Loop](../../../translated_images/agentic-rag-core-loop.c8f4b85c26920f71ed181ebb14001ac7aae47c0b0af237edcf71898645a62db3.pl.png)

## Przejmowanie procesu rozumowania

Cechą wyróżniającą system „agentowy” jest jego zdolność do przejmowania procesu rozumowania. Tradycyjne implementacje RAG często zależą od ludzi, którzy z góry definiują ścieżkę dla modelu: łańcuch myślowy, który określa, co i kiedy pobrać.
Jednak gdy system jest naprawdę agentowy, samodzielnie decyduje, jak podejść do problemu. Nie wykonuje po prostu skryptu; autonomicznie określa sekwencję kroków na podstawie jakości znalezionych informacji.
Na przykład, jeśli zostanie poproszony o stworzenie strategii wprowadzenia produktu na rynek, nie polega wyłącznie na promptach, które szczegółowo opisują cały proces badawczy i decyzyjny. Zamiast tego model agentowy samodzielnie decyduje o:

1. Pobieraniu aktualnych raportów o trendach rynkowych za pomocą Bing Web Grounding.
2. Identyfikacji istotnych danych konkurencji za pomocą Azure AI Search.
3. Korelacji historycznych wewnętrznych metryk sprzedaży za pomocą Azure SQL Database.
4. Syntezie wyników w spójną strategię za pomocą Azure OpenAI Service.
5. Oceny strategii pod kątem luk lub niespójności, co może prowadzić do kolejnej rundy pozyskiwania informacji.
Wszystkie te kroki—udoskonalanie zapytań, wybór źródeł, iteracja aż do uzyskania „zadowalającej” odpowiedzi—są podejmowane przez model, a nie z góry zaplanowane przez człowieka.

## Iteracyjne pętle, integracja narzędzi i pamięć

![Tool Integration Architecture](../../../translated_images/tool-integration.0f569710b5c17c106757adba082f6c4be025ca0721bff7d1ee4b929a3617a600.pl.png)

System agentowy opiera się na wzorcu interakcji w pętli:

- **Początkowe wywołanie:** Cel użytkownika (tzw. prompt użytkownika) jest przedstawiany LLM.
- **Uruchomienie narzędzia:** Jeśli model zidentyfikuje brakujące informacje lub niejasne instrukcje, wybiera narzędzie lub metodę pozyskiwania informacji—np. zapytanie do bazy danych wektorowych (np. Azure AI Search Hybrid search nad danymi prywatnymi) lub strukturalne zapytanie SQL—aby uzyskać więcej kontekstu.
- **Ocena i udoskonalenie:** Po przeanalizowaniu zwróconych danych model decyduje, czy informacje są wystarczające. Jeśli nie, udoskonala zapytanie, próbuje innego narzędzia lub dostosowuje swoje podejście.
- **Powtarzanie aż do zadowolenia:** Cykl ten trwa, dopóki model nie uzna, że ma wystarczającą jasność i dowody, aby dostarczyć ostateczną, dobrze uzasadnioną odpowiedź.
- **Pamięć i stan:** Ponieważ system utrzymuje stan i pamięć na kolejnych etapach, może przypominać sobie wcześniejsze próby i ich wyniki, unikając powtarzających się pętli i podejmując bardziej świadome decyzje w miarę postępu.

Z czasem tworzy to poczucie rozwijającego się zrozumienia, umożliwiając modelowi nawigację po złożonych, wieloetapowych zadaniach bez konieczności ciągłej interwencji człowieka lub przekształcania promptu.

## Obsługa trybów awaryjnych i autokorekta

Autonomia Agentic RAG obejmuje również solidne mechanizmy autokorekty. Gdy system napotyka ślepe zaułki—np. pobierając nieistotne dokumenty lub napotykając błędne zapytania—może:

- **Iterować i ponownie zapytać:** Zamiast zwracać odpowiedzi o niskiej wartości, model próbuje nowych strategii wyszukiwania, przepisuje zapytania do bazy danych lub analizuje alternatywne zestawy danych.
- **Korzystać z narzędzi diagnostycznych:** System może uruchamiać dodatkowe funkcje zaprojektowane w celu pomocy w debugowaniu kroków rozumowania lub potwierdzaniu poprawności pobranych danych. Narzędzia takie jak Azure AI Tracing będą ważne dla zapewnienia solidnej obserwowalności i monitorowania.
- **Powrót do nadzoru ludzkiego:** W scenariuszach o wysokim ryzyku lub powtarzających się niepowodzeniach model może oznaczyć niepewność i poprosić o wskazówki od człowieka. Po udzieleniu przez człowieka informacji zwrotnej model może uwzględnić tę lekcję w przyszłości.

To iteracyjne i dynamiczne podejście pozwala modelowi na ciągłe doskonalenie, zapewniając, że nie jest to system jednorazowy, ale taki, który uczy się na swoich błędach w trakcie danej sesji.

![Self Correction Mechanism](../../../translated_images/self-correction.da87f3783b7f174bdc592c754b352884dd283814758bfeb7a68f5fd910272f3b.pl.png)

## Granice autonomii

Pomimo swojej autonomii w ramach zadania, Agentic RAG nie jest równoznaczny ze Sztuczną Inteligencją Ogólną. Jego możliwości „agentowe” są ograniczone do narzędzi, źródeł danych i polityk dostarczonych przez ludzkich programistów. Nie może tworzyć własnych narzędzi ani wychodzić poza ustalone granice domeny. Zamiast tego doskonale radzi sobie z dynamicznym zarządzaniem dostępnymi zasobami.
Kluczowe różnice w stosunku do bardziej zaawansowanych form AI obejmują:

1. **Autonomia specyficzna dla domeny:** Systemy Agentic RAG koncentrują się na osiąganiu celów zdefiniowanych przez użytkownika w znanej domenie, stosując strategie takie jak przepisywanie zapytań czy wybór narzędzi w celu poprawy wyników.
2. **Zależność od infrastruktury:** Możliwości systemu zależą od narzędzi i danych zintegrowanych przez programistów. Nie może przekroczyć tych granic bez interwencji człowieka.
3. **Przestrzeganie zasad bezpieczeństwa:** Wytyczne etyczne, zasady zgodności i polityki biznesowe pozostają bardzo ważne. Swoboda agenta jest zawsze ograniczona przez środki bezpieczeństwa i mechanizmy nadzoru (miejmy nadzieję?).

## Praktyczne przypadki użycia i wartość

Agentic RAG sprawdza się w scenariuszach wymagających iteracyjnego udoskonalania i precyzji:

1. **Środowiska wymagające wysokiej poprawności:** W kontrolach zgodności, analizach regulacyjnych czy badaniach prawnych model agentowy może wielokrotnie weryfikować fakty, konsultować się z wieloma źródłami i przepisywać zapytania, aż do uzyskania dokładnie sprawdzonej odpowiedzi.
2. **Złożone interakcje z bazami danych:** W przypadku pracy z danymi strukturalnymi, gdzie zapytania mogą często zawodzić lub wymagać dostosowania, system może autonomicznie udoskonalać swoje zapytania za pomocą Azure SQL lub Microsoft Fabric OneLake, zapewniając, że ostateczne wyniki odpowiadają intencji użytkownika.
3. **Rozbudowane przepływy pracy:** Dłuższe sesje mogą ewoluować w miarę pojawiania się nowych informacji. Agentic RAG może stale uwzględniać nowe dane, zmieniając strategie w miarę zdobywania większej wiedzy o problemie.

## Zarządzanie, przejrzystość i zaufanie

W miarę jak te systemy stają się bardziej autonomiczne w swoim rozumowaniu, zarządzanie i przejrzystość są kluczowe:

- **Wyjaśnialne rozumowanie:** Model może dostarczyć ścieżkę audytu zapytań, które wykonał, źródeł, które skonsultował, i kroków rozumowania, które podjął, aby dojść do wniosku. Narzędzia takie jak Azure AI Content Safety i Azure AI Tracing / GenAIOps mogą pomóc w utrzymaniu przejrzystości i minimalizowaniu ryzyka.
- **Kontrola uprzedzeń i zrównoważone pozyskiwanie:** Programiści mogą dostosować strategie pozyskiwania, aby zapewnić uwzględnienie zrównoważonych, reprezentatywnych źródeł danych, oraz regularnie audytować wyniki, aby wykrywać uprzedzenia lub nieprawidłowości za pomocą niestandardowych modeli dla zaawansowanych organizacji zajmujących się nauką o danych, korzystających z Azure Machine Learning.
- **Nadzór ludzki i zgodność:** W przypadku zadań wrażliwych nadzór ludzki pozostaje niezbędny. Agentic RAG nie zastępuje ludzkiego osądu w decyzjach o wysokiej stawce—wspiera go, dostarczając bardziej dokładnie sprawdzone opcje.

Posiadanie narzędzi, które zapewniają jasny zapis działań, jest kluczowe. Bez nich debugowanie wieloetapowego procesu może być bardzo trudne. Zobacz poniższy przykład od Literal AI (firmy stojącej za Chainlit) dotyczący działania agenta:

![AgentRunExample](../../../translated_images/AgentRunExample.471a94bc40cbdc0cd04c1f43c8d8c9b751f10d97918c900e29cb3ba0d6aa4c00.pl.png)

## Podsumowanie

Agentic RAG reprezentuje naturalną ewolucję w sposobie
<a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">
Implementacja Retrieval Augmented Generation (RAG) z Azure OpenAI Service: Dowiedz się, jak korzystać z własnych danych z Azure OpenAI Service. Ten moduł Microsoft Learn oferuje kompleksowy przewodnik po implementacji RAG  
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Ewaluacja aplikacji generatywnej AI z Azure AI Foundry: Ten artykuł omawia ocenę i porównanie modeli na publicznie dostępnych zbiorach danych, w tym aplikacje Agentic AI i architektury RAG</a>  
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Czym jest Agentic RAG | Weaviate</a>  
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Kompletny przewodnik po agentowym Retrieval Augmented Generation – Aktualności z generacji RAG</a>  
- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: przyspiesz swój RAG dzięki reformulacji zapytań i samodzielnemu zapytaniu! Hugging Face Open-Source AI Cookbook</a>  
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Dodawanie warstw Agentic do RAG</a>  
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Przyszłość asystentów wiedzy: Jerry Liu</a>  
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Jak budować systemy Agentic RAG</a>  
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Wykorzystanie Azure AI Foundry Agent Service do skalowania agentów AI</a>  

### Prace naukowe  

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: Iteracyjne udoskonalanie z samodzielnym sprzężeniem zwrotnym</a>  
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: Agenci językowi z werbalnym uczeniem wzmacniającym</a>  
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: Duże modele językowe mogą się samokorygować za pomocą interaktywnego narzędzia krytycznego</a>  
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation: Przegląd Agentic RAG</a>  

## Poprzednia lekcja  

[Wzorzec projektowy użycia narzędzi](../04-tool-use/README.md)  

## Następna lekcja  

[Budowanie wiarygodnych agentów AI](../06-building-trustworthy-agents/README.md)  

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji o kluczowym znaczeniu zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.