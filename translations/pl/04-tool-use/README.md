[![Jak projektować dobre agentów AI](../../../translated_images/pl/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Kliknij powyższy obraz, aby obejrzeć wideo z tej lekcji)_

# Wzorzec projektowy korzystania z narzędzi

Narzędzia są interesujące, ponieważ pozwalają agentom AI na posiadanie szerszego zakresu możliwości. Zamiast agenta mającego ograniczony zestaw działań, które może wykonać, dodanie narzędzia pozwala agentowi wykonywać szeroki zakres działań. W tym rozdziale przyjrzymy się wzorcowi projektowemu korzystania z narzędzi, który opisuje, jak agenci AI mogą używać konkretnych narzędzi do osiągania swoich celów.

## Wprowadzenie

W tej lekcji chcemy odpowiedzieć na następujące pytania:

- Czym jest wzorzec projektowy korzystania z narzędzi?
- Do jakich przypadków użycia można go zastosować?
- Jakie elementy/bloki budulcowe są potrzebne do wdrożenia tego wzorca?
- Jakie są szczególne względy dotyczące użycia wzorca korzystania z narzędzi, aby budować godnych zaufania agentów AI?

## Cele nauki

Po ukończeniu tej lekcji będziesz potrafił:

- Zdefiniować wzorzec projektowy korzystania z narzędzi i jego cel.
- Zidentyfikować przypadki użycia, w których wzorzec ten ma zastosowanie.
- Zrozumieć kluczowe elementy potrzebne do implementacji tego wzorca.
- Rozpoznać kwestie związane z zapewnieniem wiarygodności agentów AI korzystających z tego wzorca.

## Czym jest wzorzec projektowy korzystania z narzędzi?

**Wzorzec projektowy korzystania z narzędzi** koncentruje się na umożliwieniu LLM interakcji z zewnętrznymi narzędziami w celu osiągnięcia konkretnych celów. Narzędzia to kod, który może być wykonywany przez agenta, aby wykonać akcje. Narzędzie może być prostą funkcją, taką jak kalkulator, lub wywołaniem API do usługi zewnętrznej, np. wyszukiwanie cen akcji lub prognoza pogody. W kontekście agentów AI, narzędzia są projektowane tak, aby były wykonywane przez agentów jako odpowiedź na **modelowo generowane wywołania funkcji**.

## Do jakich przypadków użycia można go zastosować?

Agenci AI mogą wykorzystywać narzędzia do wykonywania złożonych zadań, pozyskiwania informacji lub podejmowania decyzji. Wzorzec korzystania z narzędzi jest często stosowany w scenariuszach wymagających dynamicznej interakcji z zewnętrznymi systemami, takimi jak bazy danych, usługi internetowe czy interpretery kodu. Ta zdolność jest użyteczna w wielu różnych zastosowaniach, w tym:

- **Dynamiczne pozyskiwanie informacji:** Agenci mogą wysyłać zapytania do zewnętrznych API lub baz danych, aby pobierać aktualne dane (np. zapytania do bazy SQLite w celu analizy danych, pobieranie cen akcji lub informacji pogodowych).
- **Wykonywanie i interpretacja kodu:** Agenci mogą wykonywać kod lub skrypty, by rozwiązywać problemy matematyczne, generować raporty lub przeprowadzać symulacje.
- **Automatyzacja workflow:** Automatyzacja powtarzalnych lub wieloetapowych procesów poprzez integrację narzędzi takich jak harmonogramy zadań, usługi e-mail lub potoki danych.
- **Obsługa klienta:** Agenci mogą współdziałać z systemami CRM, platformami zgłoszeniowymi lub bazami wiedzy, by rozwiązywać zapytania użytkowników.
- **Generowanie i edycja treści:** Agenci mogą używać narzędzi takich jak korektory gramatyczne, streszczacze tekstów lub oceny bezpieczeństwa treści do wsparcia zadań związanych z tworzeniem treści.

## Jakie elementy/bloki budulcowe są potrzebne do implementacji wzorca korzystania z narzędzi?

Te bloki budulcowe pozwalają agentowi AI wykonywać szeroki zakres zadań. Przyjrzyjmy się kluczowym elementom potrzebnym do implementacji wzorca korzystania z narzędzi:

- **Schematy funkcji/narzędzi:** Szczegółowe definicje dostępnych narzędzi, wraz z nazwą funkcji, celem, wymaganymi parametrami i oczekiwanymi wynikami. Schematy te pozwalają LLM zrozumieć, jakie narzędzia są dostępne i jak tworzyć poprawne wywołania.

- **Logika wykonywania funkcji:** Określa, jak i kiedy narzędzia są wywoływane w oparciu o intencje użytkownika oraz kontekst konwersacji. Może obejmować moduły planowania, mechanizmy kierowania lub przepływy warunkowe, które dynamicznie decydują o użyciu narzędzi.

- **System obsługi wiadomości:** Komponenty zarządzające przepływem konwersacyjnym między wejściami użytkownika, odpowiedziami LLM, wywołaniami narzędzi i ich wynikami.

- **Ramowy system integracji narzędzi:** Infrastruktura łącząca agenta z różnymi narzędziami, czy to prostymi funkcjami, czy złożonymi usługami zewnętrznymi.

- **Obsługa błędów i walidacja:** Mechanizmy radzenia sobie z błędami podczas wykonywania narzędzi, weryfikacji parametrów i zarządzania nieoczekiwanymi odpowiedziami.

- **Zarządzanie stanem:** Śledzenie kontekstu rozmowy, poprzednich interakcji z narzędziami oraz danych trwałych, aby zapewnić spójność w wielokrotnych interakcjach.

Następnie przyjrzyjmy się szczegółowo wywoływaniu funkcji/narzędzi.
 
### Wywoływanie funkcji/narzędzi

Wywoływanie funkcji jest głównym sposobem, w jaki umożliwiamy dużym modelom językowym (LLM) interakcję z narzędziami. Często zobaczysz użycie terminów 'Funkcja' i 'Narzędzie' zamiennie, ponieważ 'funkcje' (bloki wielokrotnego użytku kodu) są 'narzędziami', których agenci używają do wykonywania zadań. Aby kod funkcji mógł zostać wywołany, LLM musi porównać zapytanie użytkownika z opisem funkcji. W tym celu do LLM wysyłany jest schemat zawierający opisy wszystkich dostępnych funkcji. LLM wybiera następnie najbardziej odpowiednią funkcję do zadania i zwraca jej nazwę oraz argumenty. Wybrana funkcja jest wywoływana, jej odpowiedź jest przesyłana z powrotem do LLM, które wykorzystuje tę informację, by odpowiedzieć na zapytanie użytkownika.

Aby deweloperzy mogli zaimplementować wywoływanie funkcji dla agentów, potrzebne będą:

1. Model LLM, który obsługuje wywoływanie funkcji
2. Schemat zawierający opisy funkcji
3. Kod dla każdej opisanej funkcji

Użyjmy przykładu uzyskania aktualnego czasu w mieście, aby to zilustrować:

1. **Zainicjuj LLM, który obsługuje wywoływanie funkcji:**

    Nie wszystkie modele obsługują wywoływanie funkcji, dlatego ważne jest, aby sprawdzić czy używany LLM to wspiera. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> obsługuje wywoływanie funkcji. Możemy zacząć od inicjacji klienta Azure OpenAI. 

    ```python
    # Zainicjuj klienta Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Utwórz schemat funkcji:**

    Następnie zdefiniujemy schemat JSON, który zawiera nazwę funkcji, opis tego, co funkcja robi, oraz nazwy i opisy parametrów funkcji.
    Następnie przekażemy ten schemat do wcześniej utworzonego klienta, wraz z zapytaniem użytkownika o czas w San Francisco. Ważne jest, aby zauważyć, że **wywołanie narzędzia** jest zwracane, **nie** końcowa odpowiedź na pytanie. Jak wspomniano wcześniej, LLM zwraca nazwę wybranej funkcji do zadania oraz argumenty, które zostaną do niej przekazane.

    ```python
    # Opis funkcji do odczytu przez model
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_time",
                "description": "Get the current time in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city name, e.g. San Francisco",
                        },
                    },
                    "required": ["location"],
                },
            }
        }
    ]
    ```
   
    ```python
  
    # Początkowa wiadomość użytkownika
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}] 
  
    # Pierwsze wywołanie API: Poproś model o użycie funkcji
      response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
          tools=tools,
          tool_choice="auto",
      )
  
      # Przetwórz odpowiedź modelu
      response_message = response.choices[0].message
      messages.append(response_message)
  
      print("Model's response:")  

      print(response_message)
  
    ```

    ```bash
    Model's response:
    ChatCompletionMessage(content=None, role='assistant', function_call=None, tool_calls=[ChatCompletionMessageToolCall(id='call_pOsKdUlqvdyttYB67MOj434b', function=Function(arguments='{"location":"San Francisco"}', name='get_current_time'), type='function')])
    ```
  
1. **Kod funkcji potrzebny do wykonania zadania:**

    Gdy LLM wybrało, która funkcja ma zostać uruchomiona, kod wykonujący zadanie musi zostać zaimplementowany i wykonany.
    Możemy zaimplementować kod pobierający aktualny czas w Pythonie. Będziemy też musieli napisać kod do wydobycia nazwy i argumentów z response_message, aby uzyskać ostateczny wynik.

    ```python
      def get_current_time(location):
        """Get the current time for a given location"""
        print(f"get_current_time called with location: {location}")  
        location_lower = location.lower()
        
        for key, timezone in TIMEZONE_DATA.items():
            if key in location_lower:
                print(f"Timezone found for {key}")  
                current_time = datetime.now(ZoneInfo(timezone)).strftime("%I:%M %p")
                return json.dumps({
                    "location": location,
                    "current_time": current_time
                })
      
        print(f"No timezone data found for {location_lower}")  
        return json.dumps({"location": location, "current_time": "unknown"})
    ```

     ```python
     # Obsługa wywołań funkcji
      if response_message.tool_calls:
          for tool_call in response_message.tool_calls:
              if tool_call.function.name == "get_current_time":
     
                  function_args = json.loads(tool_call.function.arguments)
     
                  time_response = get_current_time(
                      location=function_args.get("location")
                  )
     
                  messages.append({
                      "tool_call_id": tool_call.id,
                      "role": "tool",
                      "name": "get_current_time",
                      "content": time_response,
                  })
      else:
          print("No tool calls were made by the model.")  
  
      # Drugie wywołanie API: Pobierz ostateczną odpowiedź z modelu
      final_response = client.chat.completions.create(
          model=deployment_name,
          messages=messages,
      )
  
      return final_response.choices[0].message.content
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

Wywoływanie funkcji jest sercem większości, jeśli nie wszystkich projektów korzystania z narzędzi agentów, jednak implementacja od podstaw może być czasem wyzwaniem.
Jak nauczyliśmy się w [Lekcji 2](../../../02-explore-agentic-frameworks), ramy agentowe zapewniają nam gotowe bloki budulcowe do implementacji korzystania z narzędzi.
 
## Przykłady korzystania z narzędzi z ramami agentowymi

Oto kilka przykładów, jak można implementować wzorzec projektowy korzystania z narzędzi, używając różnych ram agentowych:

### Semantic Kernel

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Semantic Kernel</a> to otwartoźródłowy framework AI dla programistów .NET, Python i Java pracujących z dużymi modelami językowymi (LLM). Upraszcza proces korzystania z wywoływania funkcji, automatycznie opisując twoje funkcje i ich parametry modelowi przez proces zwany <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">serializacją</a>. Obsługuje również komunikację dwukierunkową między modelem a twoim kodem. Kolejną zaletą używania frameworka agentowego, takiego jak Semantic Kernel, jest to, że daje dostęp do gotowych narzędzi, takich jak <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step4_assistant_tool_file_search.py" target="_blank">Wyszukiwanie plików</a> oraz <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Interpreter kodu</a>.

Poniższy diagram ilustruje proces wywoływania funkcji z Semantic Kernel:

![function calling](../../../translated_images/pl/functioncalling-diagram.a84006fc287f6014.webp)

W Semantic Kernel funkcje/narzędzia nazywane są <a href="https://learn.microsoft.com/semantic-kernel/concepts/plugins/?pivots=programming-language-python" target="_blank">wtyczkami (Plugins)</a>. Możemy przekonwertować funkcję `get_current_time`, którą widzieliśmy wcześniej, na wtyczkę poprzez przekształcenie jej w klasę z tą funkcją. Możemy także zaimportować dekorator `kernel_function`, który przyjmuje opis funkcji. Kiedy następnie tworzysz kernel z GetCurrentTimePlugin, kernel automatycznie zserializuje funkcję i jej parametry, tworząc schemat do wysłania do LLM.

```python
from semantic_kernel.functions import kernel_function

class GetCurrentTimePlugin:
    async def __init__(self, location):
        self.location = location

    @kernel_function(
        description="Get the current time for a given location"
    )
    def get_current_time(location: str = ""):
        ...

```

```python 
from semantic_kernel import Kernel

# Utwórz jądro
kernel = Kernel()

# Utwórz wtyczkę
get_current_time_plugin = GetCurrentTimePlugin(location)

# Dodaj wtyczkę do jądra
kernel.add_plugin(get_current_time_plugin)
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> to nowszy framework agentowy zaprojektowany tak, aby umożliwić deweloperom bezpieczne tworzenie, wdrażanie i skalowanie wysokiej jakości, rozszerzalnych agentów AI bez konieczności zarządzania zapleczem obliczeniowym i przechowywaniem danych. Jest szczególnie przydatny dla zastosowań korporacyjnych, ponieważ jest w pełni zarządzaną usługą z zabezpieczeniami na poziomie korporacyjnym.

W porównaniu do bezpośredniej pracy z API LLM, Azure AI Agent Service oferuje kilka zalet, w tym:

- Automatyczne wywoływanie narzędzi – nie trzeba analizować wywołania narzędzia, uruchamiać narzędzia i obsługiwać odpowiedzi; wszystko to jest teraz realizowane po stronie serwera
- Bezpiecznie zarządzane dane – zamiast zarządzać własnym stanem konwersacji, można polegać na wątkach do przechowywania wszystkich potrzebnych informacji
- Narzędzia gotowe do użycia – narzędzia pozwalające na interakcję z twoimi źródłami danych, takie jak Bing, Azure AI Search i Azure Functions.

Narzędzia dostępne w Azure AI Agent Service można podzielić na dwie kategorie:

1. Narzędzia wiedzy:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Podstawy z Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Wyszukiwanie plików</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Narzędzia akcji:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Wywoływanie funkcji</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Interpreter kodu</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Narzędzia zdefiniowane przez OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service pozwala na używanie tych narzędzi razem jako `zbiór narzędzi (toolset)`. Wykorzystuje także `wątki (threads)`, które śledzą historię wiadomości z konkretnej rozmowy.

Wyobraź sobie, że jesteś agentem sprzedaży w firmie Contoso. Chcesz stworzyć agenta konwersacyjnego, który będzie odpowiadał na pytania dotyczące danych sprzedażowych.

Poniższy obraz ilustruje jak można użyć Azure AI Agent Service do analizy danych sprzedażowych:

![Agentic Service In Action](../../../translated_images/pl/agent-service-in-action.34fb465c9a84659e.webp)

Aby użyć któregokolwiek z tych narzędzi z usługą, możemy utworzyć klienta i zdefiniować narzędzie lub zbiór narzędzi. Aby praktycznie to zaimplementować, możemy użyć następującego kodu w Pythonie. LLM będzie mógł spojrzeć na toolset i zdecydować, czy użyć funkcji stworzonej przez użytkownika `fetch_sales_data_using_sqlite_query`, czy też wbudowanego Interpreter kodu, w zależności od zapytania użytkownika.

```python 
import os
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from fetch_sales_data_functions import fetch_sales_data_using_sqlite_query # funkcja fetch_sales_data_using_sqlite_query, którą można znaleźć w pliku fetch_sales_data_functions.py.
from azure.ai.projects.models import ToolSet, FunctionTool, CodeInterpreterTool

project_client = AIProjectClient.from_connection_string(
    credential=DefaultAzureCredential(),
    conn_str=os.environ["PROJECT_CONNECTION_STRING"],
)

# Inicjalizacja zestawu narzędzi
toolset = ToolSet()

# Inicjalizacja agenta wywołującego funkcje z funkcją fetch_sales_data_using_sqlite_query i dodanie go do zestawu narzędzi
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inicjalizacja narzędzia Code Interpreter i dodanie go do zestawu narzędzi.
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Jakie są szczególne względy dotyczące użycia wzorca korzystania z narzędzi, aby budować godnych zaufania agentów AI?

Częstym problemem w przypadku dynamicznie generowanego przez LLM SQL jest bezpieczeństwo, a szczególnie ryzyko wstrzyknięcia SQL lub złośliwych działań, jak usunięcie lub manipulacja bazą danych. Chociaż te obawy są uzasadnione, można je skutecznie złagodzić odpowiednią konfiguracją uprawnień dostępu do bazy danych. W większości baz danych obejmuje to ustawienie bazy jako tylko do odczytu. Dla usług bazodanowych takich jak PostgreSQL czy Azure SQL, aplikacja powinna być przypisana do roli tylko do odczytu (SELECT).
Uruchamianie aplikacji w bezpiecznym środowisku dodatkowo zwiększa ochronę. W scenariuszach korporacyjnych dane są zazwyczaj wyodrębniane i przekształcane z systemów operacyjnych do bazy danych tylko do odczytu lub hurtowni danych ze schematem przyjaznym dla użytkownika. Takie podejście zapewnia, że dane są bezpieczne, zoptymalizowane pod kątem wydajności i dostępności, a aplikacja ma ograniczony, tylko do odczytu dostęp.

## Przykładowe kody

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Masz więcej pytań dotyczących użycia wzorców projektowych narzędzia?

Dołącz do [Azure AI Foundry Discord](https://aka.ms/ai-agents/discord), aby spotkać innych uczących się, uczestniczyć w godzinach konsultacji i uzyskać odpowiedzi na pytania dotyczące AI Agents.

## Dodatkowe zasoby

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Warsztaty Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Warsztaty Contoso Creative Writer Multi-Agent</a>
- <a href="https://learn.microsoft.com/semantic-kernel/concepts/ai-services/chat-completion/function-calling/?pivots=programming-language-python#1-serializing-the-functions" target="_blank">Samouczek wywoływania funkcji Semantic Kernel</a>
- <a href="https://github.com/microsoft/semantic-kernel/blob/main/python/samples/getting_started_with_agents/openai_assistant/step3_assistant_tool_code_interpreter.py" target="_blank">Interpreter kodu Semantic Kernel</a>
- <a href="https://microsoft.github.io/autogen/dev/user-guide/core-user-guide/components/tools.html" target="_blank">Narzędzia Autogen</a>

## Poprzednia lekcja

[Understanding Agentic Design Patterns](../03-agentic-design-patterns/README.md)

## Następna lekcja

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Ten dokument został przetłumaczony przy użyciu usługi tłumaczeń AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do jak największej dokładności, prosimy pamiętać, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy traktować jako źródło ostateczne. W przypadku informacji krytycznych zaleca się skorzystanie z tłumaczenia wykonanego przez profesjonalnego tłumacza. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->