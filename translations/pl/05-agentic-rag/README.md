[![Agentic RAG](../../../translated_images/pl/lesson-5-thumbnail.20ba9d0c0ae64fae.webp)](https://youtu.be/WcjAARvdL7I?si=BCgwjwFb2yCkEhR9)

> _(Kliknij powyższy obrazek, aby obejrzeć wideo z tej lekcji)_

# Agentic RAG

Ta lekcja przedstawia kompleksowy przegląd Agentic Retrieval-Augmented Generation (Agentic RAG), nowatorskiego paradygmatu SI, w którym duże modele językowe (LLM) autonomicznie planują swoje kolejne kroki, jednocześnie pozyskując informacje z zewnętrznych źródeł. W przeciwieństwie do statycznych wzorców pobierania-then-odczytu, Agentic RAG zakłada iteracyjne wywołania LLM, przeplatane wywołaniami narzędzi lub funkcji oraz strukturą wyjściową. System ocenia wyniki, doprecyzowuje zapytania, wywołuje dodatkowe narzędzia w razie potrzeby i kontynuuje ten cykl, aż osiągnie satysfakcjonujące rozwiązanie.

## Wprowadzenie

Ta lekcja obejmie

- **Zrozumienie Agentic RAG:** Poznanie nowego paradygmatu w SI, w którym duże modele językowe (LLM) autonomicznie planują swoje kolejne kroki, pobierając informacje z zewnętrznych źródeł danych.
- **Zrozumienie iteracyjnego stylu Maker-Checker:** Zrozumienie pętli iteracyjnych wywołań LLM, przeplatanych wywołaniami narzędzi lub funkcji oraz strukturą wyjścia, zaprojektowanych w celu poprawy poprawności i obsługi błędnych zapytań.
- **Eksploracja praktycznych zastosowań:** Zidentyfikowanie scenariuszy, gdzie Agentic RAG sprawdza się najlepiej, takich jak środowiska nastawione na poprawność, złożone interakcje z bazami danych oraz rozbudowane przepływy pracy.

## Cele nauki

Po ukończeniu tej lekcji będziesz potrafił/zrozumiesz:

- **Zrozumienie Agentic RAG:** Poznanie nowatorskiego paradygmatu SI, w którym duże modele językowe (LLM) autonomicznie planują swoje kolejne kroki, pobierając dane z zewnętrznych źródeł.
- **Iteracyjny styl Maker-Checker:** Zrozumienie koncepcji pętli iteracyjnych wywołań LLM, przeplatanych użyciem narzędzi lub funkcji oraz strukturą wyjściową, mających na celu poprawę poprawności i obsługę błędnie sformułowanych zapytań.
- **Przejęcie procesu rozumowania:** Pojęcie o zdolności systemu do zarządzania własnym procesem rozumowania, podejmowania decyzji o podejściu do problemów bez polegania na uprzednio ustalonych ścieżkach.
- **Przepływ pracy:** Zrozumienie, jak model agentowy samodzielnie decyduje o pobieraniu raportów o trendach rynkowych, identyfikowaniu danych konkurencyjnych, korelowaniu wewnętrznych wskaźników sprzedaży, syntezie wyników i ocenie strategii.
- **Iteracyjne pętle, integracja narzędzi i pamięć:** Poznanie opartego na pętli wzoru interakcji systemu, który utrzymuje stan i pamięć na kolejnych etapach, aby unikać powtarzających się cykli i podejmować przemyślane decyzje.
- **Obsługa trybów awaryjnych i samokorekta:** Poznanie solidnych mechanizmów samokorekty systemu, w tym iteracji i ponownego zapyta, użycia narzędzi diagnostycznych oraz możliwości wsparcia przez nadzór ludzki.
- **Granice autonomii:** Zrozumienie ograniczeń Agentic RAG, ze szczególnym uwzględnieniem autonomii w specyficznych domenach, zależności od infrastruktury i przestrzegania zasad bezpieczeństwa.
- **Praktyczne przypadki użycia i wartość:** Identyfikacja scenariuszy, w których Agentic RAG jest szczególnie efektywny, takich jak środowiska z naciskiem na poprawność, złożone interakcje bazodanowe i rozbudowane przepływy pracy.
- **Zarządzanie, przejrzystość i zaufanie:** Poznanie znaczenia zarządzania i przejrzystości, w tym wyjaśnialnego rozumowania, kontroli uprzedzeń oraz nadzoru ludzkiego.

## Czym jest Agentic RAG?

Agentic Retrieval-Augmented Generation (Agentic RAG) to nowatorski paradygmat SI, w którym duże modele językowe (LLM) autonomicznie planują swoje kolejne kroki, korzystając jednocześnie z informacji pozyskiwanych ze źródeł zewnętrznych. W odróżnieniu od statycznych schematów pobierania-then-odczytu, Agentic RAG polega na iteracyjnych wywołaniach LLM, przeplatanych wywołaniami narzędzi lub funkcji i generowaniu uporządkowanych wyników. System ocenia rezultaty, doprecyzowuje zapytania, w razie potrzeby wywołuje dodatkowe narzędzia i powtarza ten cykl, aż zostanie osiągnięte satysfakcjonujące rozwiązanie. Ten iteracyjny styl "maker-checker" zwiększa poprawność, reaguje na błędnie sformułowane zapytania i gwarantuje wyniki wysokiej jakości.

System aktywnie zarządza własnym procesem rozumowania, modyfikując nieudane zapytania, wybierając różne metody pobierania i integrując wiele narzędzi — takich jak wyszukiwanie wektorowe w Azure AI Search, bazy danych SQL czy niestandardowe API — zanim sfinalizuje odpowiedź. Charakterystyczną cechą systemu agentowego jest zdolność do zarządzania własnym procesem rozumowania. Tradycyjne implementacje RAG opierają się na uprzednio zdefiniowanych ścieżkach, natomiast system agentowy autonomicznie określa kolejność działań na podstawie jakości znalezionych informacji.

## Definicja Agentic Retrieval-Augmented Generation (Agentic RAG)

Agentic Retrieval-Augmented Generation (Agentic RAG) to nowy paradygmat w rozwoju SI, w którym LLM nie tylko pobierają dane ze źródeł zewnętrznych, ale również autonomicznie planują kolejne kroki. W przeciwieństwie do statycznych wzorców pobierania-then-odczytu lub starannie zaprojektowanych sekwencji promptów, Agentic RAG polega na pętli iteracyjnych wywołań do LLM, przeplatanych wywołaniami narzędzi lub funkcji oraz generowaniem uporządkowanych wyników. Na każdym etapie system ocenia otrzymane rezultaty, decyduje, czy doprecyzować zapytania, w razie potrzeby uruchamia dodatkowe narzędzia i kontynuuje cykl aż do uzyskania satysfakcjonującego wyniku.

Ten iteracyjny, styl "maker-checker" ma na celu poprawę poprawności, obsługę błędnych zapytań do baz danych strukturalnych (np. NL2SQL) oraz zapewnienie wyważonych, wysokiej jakości wyników. Zamiast opierać się wyłącznie na starannie skonstruowanych łańcuchach promptów, system aktywnie zarządza swoim procesem rozumowania. Potrafi przepisywać zapytania, które zakończyły się niepowodzeniem, wybierać różne metody pozyskiwania danych oraz integrować wiele narzędzi — takich jak wyszukiwanie wektorowe w Azure AI Search, bazy danych SQL czy niestandardowe API — zanim ostatecznie udzieli odpowiedzi. Dzięki temu nie ma potrzeby stosowania nadmiernie skomplikowanych frameworków orkiestracji. Zamiast tego stosunkowo prosta pętla „wywołanie LLM → użycie narzędzia → wywołanie LLM → …” może generować zaawansowane i dobrze ugruntowane wyniki.

![Główna pętla Agentic RAG](../../../translated_images/pl/agentic-rag-core-loop.c8f4b85c26920f71.webp)

## Zarządzanie procesem rozumowania

Cechą wyróżniającą, która czyni system „agenticznym”, jest jego zdolność do zarządzania własnym procesem rozumowania. Tradycyjne implementacje RAG często wymagają, aby ludzie wcześniej definiowali ścieżkę dla modelu: łańcuch myślenia opisujący, co i kiedy należy pozyskać.
Jednak gdy system jest naprawdę agenticznym, samodzielnie decyduje, jak podejść do problemu. Nie wykonuje jedynie skryptu — autonomicznie ustala kolejność kroków na podstawie jakości znalezionych informacji.
Na przykład, jeśli poproszony jest o stworzenie strategii wprowadzenia produktu na rynek, nie polega jedynie na promptcie, który opisuje cały proces badawczo-decyzyjny. Zamiast tego model agentowy samodzielnie decyduje o:

1. Pobieraniu aktualnych raportów o trendach rynkowych za pomocą Bing Web Grounding
2. Identyfikacji odpowiednich danych konkurencji z wykorzystaniem Azure AI Search.
3. Korelowaniu historycznych wewnętrznych wskaźników sprzedaży z bazą danych Azure SQL.
4. Syntezie wyników w spójną strategię koordynowaną przez Azure OpenAI Service.
5. Ocena strategii pod kątem braków lub niespójności, uruchamiając kolejną rundę pobierania, jeśli jest to konieczne.
Wszystkie te kroki — doprecyzowywanie zapytań, wybór źródeł, iteracje aż do zadowolenia z odpowiedzi — podejmuje model, a nie są one z góry zaprogramowane przez człowieka.

## Iteracyjne pętle, integracja narzędzi i pamięć

![Architektura integracji narzędzi](../../../translated_images/pl/tool-integration.0f569710b5c17c10.webp)

System agentowy opiera się na wzorcu interakcji opartej na pętli:

- **Pierwsze wywołanie:** Cel użytkownika (czyli prompt użytkownika) jest przekazywany do LLM.
- **Uruchomienie narzędzia:** Jeśli model rozpozna brakujące informacje lub niejasne instrukcje, wybiera narzędzie lub metodę pobierania — na przykład zapytanie wektorowe do bazy danych (np. Azure AI Search Hybrid search nad prywatnymi danymi) lub zapytanie strukturalne SQL — aby zebrać więcej kontekstu.
- **Ocena i doprecyzowanie:** Po przeglądzie zwróconych danych model decyduje, czy otrzymane informacje są wystarczające. Jeśli nie, doprecyzowuje zapytanie, próbuje innego narzędzia lub modyfikuje podejście.
- **Powtarzaj aż do satysfakcji:** Ten cykl trwa, aż model uzna, że ma wystarczającą klarowność i dowody, by dostarczyć ostateczną, dobrze uzasadnioną odpowiedź.
- **Pamięć i stan:** Ponieważ system utrzymuje stan i pamięć podczas kolejnych kroków, może przypominać sobie wcześniejsze próby i ich wyniki, unikając powtarzających się pętli i podejmując bardziej świadome decyzje podczas działania.

Z czasem tworzy się poczucie rozwijającego się zrozumienia, pozwalające modelowi realizować złożone, wieloetapowe zadania bez potrzeby stałej interwencji człowieka lub przekształcania promptu.

## Obsługa trybów awaryjnych i samokorekta

Autonomia Agentic RAG obejmuje także solidne mechanizmy samokorekty. Kiedy system napotyka na ślepe zaułki — takie jak pobieranie nieistotnych dokumentów lub natrafienie na błędne zapytania — może:

- **Iterować i ponownie wyszukiwać:** Zamiast zwracać odpowiedzi o niskiej wartości, model próbuje nowych strategii wyszukiwania, przepisuje zapytania do bazy danych lub analizuje alternatywne zbiory danych.
- **Używać narzędzi diagnostycznych:** System może uruchamiać dodatkowe funkcje mające na celu debugowanie kroków rozumowania lub potwierdzanie poprawności pobranych danych. Narzędzia takie jak Azure AI Tracing będą ważne do umożliwienia solidnej obserwowalności i monitorowania.
- **Wspierać się nadzorem ludzkim:** W scenariuszach wysokiego ryzyka lub przy powtarzających się błędach model może zgłosić niepewność i poprosić o ludzkie wsparcie. Po udzieleniu korekty przez człowieka model może tę lekcję uwzględnić przy dalszej pracy.

To iteracyjne i dynamiczne podejście pozwala modelowi na ciągłą poprawę, dzięki czemu nie jest to system jednorazowy, lecz taki, który uczy się na swoich błędach podczas danej sesji.

![Mechanizm samokorekty](../../../translated_images/pl/self-correction.da87f3783b7f174b.webp)

## Granice autonomii

Pomimo autonomii w ramach danego zadania, Agentic RAG nie jest odpowiednikiem Sztucznej Ogólnej Inteligencji. Jego możliwości „agentic” są ograniczone do narzędzi, źródeł danych i polityk dostarczonych przez programistów. Nie potrafi samodzielnie tworzyć narzędzi ani wykraczać poza ustalone granice domeny. Zamiast tego jego mocą jest dynamiczne zarządzanie dostępnych zasobów.
Kluczowe różnice w stosunku do bardziej zaawansowanych form SI to:

1. **Autonomia specyficzna dla domeny:** Systemy Agentic RAG skupiają się na osiąganiu celów zdefiniowanych przez użytkownika w znanej domenie, wykorzystując strategie takie jak przepisywanie zapytań lub wybór narzędzi w celu poprawy wyników.
2. **Zależność od infrastruktury:** Zdolności systemu opierają się na narzędziach i danych zintegrowanych przez programistów. Nie może przekraczać tych granic bez ludzkiej interwencji.
3. **Poszanowanie zasad bezpieczeństwa:** Wytyczne etyczne, przepisy i polityki biznesowe pozostają kluczowe. Wolność agenta jest zawsze ograniczona przez środki bezpieczeństwa i mechanizmy nadzoru (miejmy nadzieję).

## Praktyczne zastosowania i wartość

Agentic RAG sprawdza się w scenariuszach wymagających iteracyjnego dopracowywania i precyzji:

1. **Środowiska nastawione na poprawność:** W kontrolach zgodności, analizach regulacyjnych czy badaniach prawnych model agentowy może wielokrotnie weryfikować fakty, korzystać z wielu źródeł i przepisywać zapytania, aż uzyska w pełni zweryfikowaną odpowiedź.
2. **Złożone interakcje z bazami danych:** W przypadku pracy z danymi strukturalnymi, gdzie zapytania często zawodzą lub wymagają korekty, system samodzielnie doprecyzowuje zapytania przy użyciu Azure SQL lub Microsoft Fabric OneLake, zapewniając, że końcowe wyniki odpowiadają intencjom użytkownika.
3. **Rozbudowane przepływy pracy:** Dłuższe sesje mogą ewoluować w miarę pojawiania się nowych danych. Agentic RAG może na bieżąco włączać nowe informacje, zmieniając strategie w trakcie poznawania przestrzeni problemowej.

## Zarządzanie, przejrzystość i zaufanie

W miarę jak systemy te stają się bardziej autonomiczne w swoim rozumowaniu, zarządzanie i przejrzystość są kluczowe:

- **Wyjaśnialne rozumowanie:** Model może dostarczać ścieżkę audytową z zapytań, źródeł i kroków rozumowania, które doprowadziły do końcowego wniosku. Narzędzia takie jak Azure AI Content Safety i Azure AI Tracing / GenAIOps pomagają utrzymać przejrzystość i ograniczać ryzyko.
- **Kontrola uprzedzeń i zrównoważone pobieranie:** Programiści mogą dostosowywać strategie pobierania, aby uwzględnić wyważone, reprezentatywne źródła danych oraz regularnie audytować wyniki w celu wykrywania uprzedzeń lub nieprawidłowości, stosując modele niestandardowe dla zaawansowanych zespołów nauki o danych korzystających z Azure Machine Learning.
- **Nadzór ludzki i zgodność:** W zadaniach wrażliwych nadzór człowieka jest niezbędny. Agentic RAG nie zastępuje ludzkiego osądu w decyzjach o dużym znaczeniu — wzmacnia go, dostarczając bardziej dokładnie zweryfikowane opcje.

Posiadanie narzędzi zapewniających jasną historię działań jest kluczowe. Bez nich debugowanie wieloetapowego procesu może być bardzo trudne. Zobacz poniższy przykład z Literal AI (firma stojąca za Chainlit) przedstawiający przebieg agenta:

![Przykład działania agenta](../../../translated_images/pl/AgentRunExample.471a94bc40cbdc0c.webp)

## Podsumowanie

Agentic RAG to naturalna ewolucja w sposobie, w jaki systemy SI radzą sobie ze złożonymi, wymagającymi danych zadaniami. Dzięki przyjęciu wzoru interakcji opartego na pętli, autonomicznemu wyborowi narzędzi oraz doprecyzowywaniu zapytań aż do uzyskania wysokiej jakości wyniku, system wychodzi poza statyczne podążanie za promptem i staje się bardziej adaptacyjnym, świadomym kontekstu decydentem. Choć nadal ograniczony przez zdefiniowaną przez ludzi infrastrukturę i zasady etyczne, te agentowe możliwości umożliwiają bogatsze, bardziej dynamiczne i ostatecznie użyteczniejsze interakcje SI zarówno dla przedsiębiorstw, jak i użytkowników końcowych.

### Masz więcej pytań o Agentic RAG?

Dołącz do [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), aby spotkać innych uczących się, uczestniczyć w godzinach konsultacji i uzyskać odpowiedzi na pytania dotyczące agentów SI.

## Dodatkowe zasoby

- <a href="https://learn.microsoft.com/training/modules/use-own-data-azure-openai" target="_blank">Implementacja Retrieval Augmented Generation (RAG) z Azure OpenAI Service: Dowiedz się, jak korzystać z własnych danych z Azure OpenAI Service. Ten moduł Microsoft Learn zapewnia kompleksowy przewodnik po implementacji RAG</a>
- <a href="https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai" target="_blank">Ewaluacja aplikacji sztucznej inteligencji generatywnej z Microsoft Foundry: Artykuł omawia ewaluację i porównanie modeli na publicznie dostępnych zbiorach danych, w tym aplikacje agentowe AI i architektury RAG</a>
- <a href="https://weaviate.io/blog/what-is-agentic-rag" target="_blank">Czym jest Agentic RAG | Weaviate</a>
- <a href="https://ragaboutit.com/agentic-rag-a-complete-guide-to-agent-based-retrieval-augmented-generation/" target="_blank">Agentic RAG: Kompletny przewodnik po agentowej generacji wspomaganej wyszukiwaniem – Aktualności z generacji RAG</a>

- <a href="https://huggingface.co/learn/cookbook/agent_rag" target="_blank">Agentic RAG: przyspiesz swój RAG dzięki reformulacji zapytań i samodzielnemu wyszukiwaniu! Hugging Face Open-Source AI Cookbook</a>
- <a href="https://youtu.be/aQ4yQXeB1Ss?si=2HUqBzHoeB5tR04U" target="_blank">Dodawanie warstw agentowych do RAG</a>
- <a href="https://www.youtube.com/watch?v=zeAyuLc_f3Q&t=244s" target="_blank">Przyszłość asystentów wiedzy: Jerry Liu</a>
- <a href="https://www.youtube.com/watch?v=AOSjiXP1jmQ" target="_blank">Jak zbudować agentowe systemy RAG</a>
- <a href="https://ignite.microsoft.com/sessions/BRK102?source=sessions" target="_blank">Wykorzystanie Microsoft Foundry Agent Service do skalowania twoich agentów AI</a>

### Artykuły naukowe

- <a href="https://arxiv.org/abs/2303.17651" target="_blank">2303.17651 Self-Refine: iteracyjne udoskonalanie z własną informacją zwrotną</a>
- <a href="https://arxiv.org/abs/2303.11366" target="_blank">2303.11366 Reflexion: językowe agenty z werbalnym uczeniem przez wzmacnianie</a>
- <a href="https://arxiv.org/abs/2305.11738" target="_blank">2305.11738 CRITIC: duże modele językowe potrafią się samokorygować dzięki interaktywnemu narzędziu krytyki</a>
- <a href="https://arxiv.org/abs/2501.09136" target="_blank">2501.09136 Agentic Retrieval-Augmented Generation: przegląd agentowego RAG</a>

## Wstępne testowanie tego agenta (opcjonalne)

Po nauczeniu się wdrażania agentów w [Lekcji 16](../16-deploying-scalable-agents/README.md), możesz wstępnie przetestować agenta `TravelRAGAgent` z tej lekcji — sprawdzając, czy jego odpowiedzi są oparte na bazie wiedzy — za pomocą [`tests/lesson-05-smoke-tests.json`](../../../tests/lesson-05-smoke-tests.json). Instrukcje uruchomienia znajdziesz w [`tests/README.md`](../tests/README.md).

## Poprzednia lekcja

[Wzorzec użycia narzędzi](../04-tool-use/README.md)

## Następna lekcja

[Budowanie godnych zaufania agentów AI](../06-building-trustworthy-agents/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->