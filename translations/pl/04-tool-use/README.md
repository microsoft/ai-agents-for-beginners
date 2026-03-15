[![Jak zaprojektować dobre agenty AI](../../../translated_images/pl/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Kliknij powyższy obraz, aby obejrzeć wideo tej lekcji)_

# Wzorzec użycia narzędzi

Narzędzia są interesujące, ponieważ pozwalają agentom AI na posiadanie szerszego zakresu możliwości. Zamiast ograniczonego zestawu akcji, które agent może wykonać, dodanie narzędzia pozwala agentowi wykonywać teraz znacznie większą liczbę działań. W tym rozdziale przyjrzymy się Wzorcu użycia narzędzi, który opisuje, jak agenty AI mogą używać konkretnych narzędzi, aby osiągnąć swoje cele.

## Wprowadzenie

W tej lekcji chcemy odpowiedzieć na następujące pytania:

- Czym jest wzorzec użycia narzędzi?
- Do jakich przypadków użycia można go zastosować?
- Jakie elementy/bloki budulcowe są potrzebne do wdrożenia wzorca?
- Jakie są szczególne uwagi przy używaniu Wzorca użycia narzędzi, aby budować godne zaufania agenty AI?

## Cele nauki

Po ukończeniu tej lekcji będziesz w stanie:

- Zdefiniować Wzorzec użycia narzędzi i jego cel.
- Zidentyfikować przypadki użycia, w których Wzorzec użycia narzędzi jest stosowalny.
- Zrozumieć kluczowe elementy potrzebne do wdrożenia wzorca.
- Rozpoznać uwagi dotyczące zapewnienia zaufania w agentach AI stosujących ten wzorzec.

## Czym jest Wzorzec użycia narzędzi?

Wzorzec użycia narzędzi koncentruje się na nadaniu LLM możliwości interakcji z zewnętrznymi narzędziami w celu osiągania określonych celów. Narzędzia to kod, który może być wykonywany przez agenta, aby wykonać działania. Narzędzie może być prostą funkcją, taką jak kalkulator, lub wywołaniem API do usługi zewnętrznej, takiej jak sprawdzanie cen akcji czy prognoza pogody. W kontekście agentów AI narzędzia są projektowane tak, aby były wykonywane przez agentów w odpowiedzi na funkcjonalne wywołania generowane przez model.

## Do jakich przypadków użycia można go zastosować?

Agenty AI mogą wykorzystywać narzędzia do wykonywania złożonych zadań, pobierania informacji lub podejmowania decyzji. Wzorzec użycia narzędzi jest często stosowany w scenariuszach wymagających dynamicznej interakcji z zewnętrznymi systemami, takimi jak bazy danych, usługi internetowe czy interpretery kodu. Ta zdolność jest przydatna w wielu różnych przypadkach użycia, w tym:

- **Dynamiczne pobieranie informacji:** Agenty mogą zapytywać zewnętrzne API lub bazy danych, aby pobierać aktualne dane (np. zapytania do bazy SQLite w celu analizy danych, pobieranie cen akcji lub informacji o pogodzie).
- **Wykonywanie i interpretacja kodu:** Agenty mogą wykonywać kod lub skrypty, aby rozwiązywać problemy matematyczne, generować raporty lub przeprowadzać symulacje.
- **Automatyzacja przepływów pracy:** Automatyzowanie powtarzalnych lub wieloetapowych przepływów pracy poprzez integrację narzędzi takich jak harmonogramy zadań, usługi e-mail czy potoki danych.
- **Obsługa klienta:** Agenty mogą wchodzić w interakcje z systemami CRM, platformami zgłoszeń czy bazami wiedzy, aby rozwiązywać zapytania użytkowników.
- **Generowanie i edycja treści:** Agenty mogą wykorzystywać narzędzia takie jak korektory gramatyczne, streszczacze tekstów czy oceniacze bezpieczeństwa treści, aby wspierać zadania związane z tworzeniem treści.

## Jakie elementy/bloki budulcowe są potrzebne do wdrożenia wzorca użycia narzędzi?

Te bloki budulcowe pozwalają agentowi AI wykonywać szeroki zakres zadań. Przyjrzyjmy się kluczowym elementom potrzebnym do wdrożenia Wzorca użycia narzędzi:

- **Schematy funkcji/narzędzi:** Szczegółowe definicje dostępnych narzędzi, w tym nazwa funkcji, cel, wymagane parametry oraz oczekiwane wyjścia. Te schematy umożliwiają LLM zrozumienie, jakie narzędzia są dostępne i jak skonstruować poprawne żądania.

- **Logika wykonywania funkcji:** Określa, jak i kiedy narzędzia są wywoływane na podstawie zamiaru użytkownika i kontekstu rozmowy. Może to obejmować moduły planujące, mechanizmy routingu lub przepływy warunkowe, które dynamicznie decydują o użyciu narzędzi.

- **System obsługi wiadomości:** Komponenty zarządzające przepływem konwersacji między wejściami użytkownika, odpowiedziami LLM, wywołaniami narzędzi i wynikami narzędzi.

- **Ramowy system integracji narzędzi:** Infrastruktura łącząca agenta z różnymi narzędziami, zarówno prostymi funkcjami, jak i złożonymi usługami zewnętrznymi.

- **Obsługa błędów i walidacja:** Mechanizmy obsługi awarii wykonywania narzędzi, walidacji parametrów i zarządzania nieoczekiwanymi odpowiedziami.

- **Zarządzanie stanem:** Śledzi kontekst rozmowy, poprzednie interakcje z narzędziami i dane trwałe, aby zapewnić spójność w wieloetapowych interakcjach.

Następnie przyjrzyjmy się szczegółowo wywoływaniu funkcji/narzędzi.

### Wywoływanie funkcji/narzędzi

Wywoływanie funkcji jest podstawowym sposobem, w jaki umożliwiamy modelom językowym (LLM) interakcję z narzędziami. Często będziesz widzieć terminy 'Function' i 'Tool' używane zamiennie, ponieważ 'funkcje' (bloki wielokrotnego użytku kodu) są 'narzędziami', których agenty używają do realizacji zadań. Aby kod funkcji mógł zostać wywołany, LLM musi porównać żądanie użytkownika z opisem funkcji. W tym celu do LLM wysyła się schemat zawierający opisy wszystkich dostępnych funkcji. LLM następnie wybiera najbardziej odpowiednią funkcję do zadania i zwraca jej nazwę oraz argumenty. Wybrana funkcja jest wywoływana, jej odpowiedź jest wysyłana z powrotem do LLM, który wykorzystuje te informacje do odpowiedzi na żądanie użytkownika.

Aby deweloperzy mogli zaimplementować wywoływanie funkcji dla agentów, będą potrzebować:

1. Modelu LLM, który obsługuje wywoływanie funkcji
2. Schematu zawierającego opisy funkcji
3. Kodu dla każdej opisanej funkcji

Użyjmy przykładu pobrania aktualnego czasu w mieście, aby to zilustrować:

1. **Inicjalizacja LLM, który obsługuje wywoływanie funkcji:**

    Nie wszystkie modele obsługują wywoływanie funkcji, więc ważne jest, aby sprawdzić, czy model LLM, którego używasz, to potrafi.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> obsługuje wywoływanie funkcji. Możemy rozpocząć od zainicjowania klienta Azure OpenAI. 

    ```python
    # Zainicjalizuj klienta Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Utworzenie schematu funkcji:**

    Następnie zdefiniujemy schemat JSON zawierający nazwę funkcji, opis tego, co funkcja robi, oraz nazwy i opisy parametrów funkcji.
    Następnie weźmiemy ten schemat i przekażemy go klientowi utworzonemu wcześniej, wraz z żądaniem użytkownika dotyczącym znalezienia czasu w San Francisco. Ważne jest zauważyć, że to, co jest zwracane, to **wywołanie narzędzia**, **a nie** ostateczna odpowiedź na pytanie. Jak wspomniano wcześniej, LLM zwraca nazwę funkcji, którą wybrał do zadania, oraz argumenty, które zostaną do niej przekazane.

    ```python
    # Opis funkcji do przeczytania przez model
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
  
1. **Kod funkcji niezbędny do wykonania zadania:**

    Teraz, gdy LLM wybrał, która funkcja musi zostać uruchomiona, kod realizujący zadanie musi zostać zaimplementowany i wykonany.
    Możemy zaimplementować kod pobierający aktualny czas w Pythonie. Będziemy także musieli napisać kod do wyodrębnienia nazwy i argumentów z response_message, aby uzyskać końcowy rezultat.

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
  
      # Drugie wywołanie API: Pobierz ostateczną odpowiedź od modelu
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

Wywoływanie funkcji leży u podstaw większości, jeśli nie wszystkich projektów wykorzystujących narzędzia w agentach, jednak implementacja od podstaw może czasami być wyzwaniem.
Jak dowiedzieliśmy się w [Lekcji 2](../../../02-explore-agentic-frameworks), frameworki agentyczne dostarczają nam gotowych bloków budulcowych do implementacji użycia narzędzi.
 
## Przykłady użycia narzędzi z frameworkami agentycznymi

Oto kilka przykładów, jak można zaimplementować Wzorzec użycia narzędzi przy użyciu różnych frameworków agentycznych:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> to otwartoźródłowy framework AI do budowania agentów AI. Upraszcza proces używania wywołań funkcji, pozwalając definiować narzędzia jako funkcje Pythona z dekoratorem `@tool`. Framework obsługuje komunikację między modelem a twoim kodem. Zapewnia również dostęp do gotowych narzędzi, takich jak Wyszukiwanie plików i Interpreter kodu za pośrednictwem `AzureAIProjectAgentProvider`.

Poniższy diagram ilustruje proces wywoływania funkcji w Microsoft Agent Framework:

![wywoływanie funkcji](../../../translated_images/pl/functioncalling-diagram.a84006fc287f6014.webp)

W Microsoft Agent Framework narzędzia definiowane są jako udekorowane funkcje. Możemy przekonwertować funkcję `get_current_time`, którą widzieliśmy wcześniej, na narzędzie, używając dekoratora `@tool`. Framework automatycznie zserializuje funkcję i jej parametry, tworząc schemat do wysłania do LLM.

```python
from agent_framework import tool
from agent_framework.azure import AzureAIProjectAgentProvider
from azure.identity import AzureCliCredential

@tool
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Utwórz klienta
provider = AzureAIProjectAgentProvider(credential=AzureCliCredential())

# Utwórz agenta i uruchom go za pomocą narzędzia
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> to nowszy framework agentyczny zaprojektowany, aby umożliwić deweloperom bezpieczne budowanie, wdrażanie i skalowanie wysokiej jakości oraz rozszerzalnych agentów AI bez konieczności zarządzania zasobami obliczeniowymi i pamięcią. Jest szczególnie przydatny w aplikacjach korporacyjnych, ponieważ jest to w pełni zarządzana usługa z bezpieczeństwem klasy enterprise.

W porównaniu z tworzeniem aplikacji bezpośrednio za pomocą API LLM, Azure AI Agent Service oferuje kilka zalet, w tym:

- Automatyczne wywoływanie narzędzi – nie ma potrzeby parsowania wywołania narzędzia, wywoływania narzędzia i obsługi odpowiedzi; wszystko to odbywa się teraz po stronie serwera
- Bezpiecznie zarządzane dane – zamiast zarządzać własnym stanem konwersacji, możesz polegać na wątkach (threads), aby przechowywać wszystkie potrzebne informacje
- Narzędzia gotowe do użycia – narzędzia, które można wykorzystać do interakcji z źródłami danych, takie jak Bing, Azure AI Search i Azure Functions.

Narzędzia dostępne w Azure AI Agent Service można podzielić na dwie kategorie:

1. Narzędzia wiedzy:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding z wyszukiwarką Bing</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Wyszukiwanie plików</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Narzędzia operacyjne:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Wywoływanie funkcji</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Interpreter kodu</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Narzędzia zdefiniowane przez OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Agent Service umożliwia używanie tych narzędzi razem jako `toolset`. Wykorzystuje również `threads`, które śledzą historię wiadomości z danej konwersacji.

Wyobraź sobie, że jesteś agentem handlowym w firmie o nazwie Contoso. Chcesz opracować agenta konwersacyjnego, który potrafi odpowiadać na pytania dotyczące danych sprzedażowych.

Poniższy obraz ilustruje, jak można wykorzystać Azure AI Agent Service do analizy danych sprzedażowych:

![Usługa agentyczna w akcji](../../../translated_images/pl/agent-service-in-action.34fb465c9a84659e.webp)

Aby użyć któregokolwiek z tych narzędzi z usługą, możemy utworzyć klienta i zdefiniować narzędzie lub zestaw narzędzi. Aby zaimplementować to praktycznie, możemy użyć następującego kodu Pythona. LLM będzie mógł spojrzeć na toolset i zdecydować, czy użyć funkcji stworzonej przez użytkownika, `fetch_sales_data_using_sqlite_query`, czy predefiniowanego Interpreteru kodu, w zależności od żądania użytkownika.

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

# Zainicjalizuj zestaw narzędzi
toolset = ToolSet()

# Zainicjalizuj agenta wywołującego funkcje z funkcją fetch_sales_data_using_sqlite_query i dodaj go do zestawu narzędzi
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Zainicjalizuj narzędzie Code Interpreter i dodaj je do zestawu narzędzi
code_interpreter = code_interpreter = CodeInterpreterTool()
toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Jakie są szczególne uwagi przy użyciu Wzorca użycia narzędzi do budowy godnych zaufania agentów AI?

Częstym problemem związanym z dynamicznie generowanym SQL przez LLM są kwestie bezpieczeństwa, szczególnie ryzyko SQL injection lub złośliwych działań, takich jak usuwanie lub manipulacja bazą danych. Chociaż te obawy są uzasadnione, można je skutecznie złagodzić poprzez odpowiednią konfigurację uprawnień dostępu do bazy danych. Dla większości baz danych polega to na skonfigurowaniu bazy jako tylko do odczytu. Dla usług bazodanowych takich jak PostgreSQL czy Azure SQL aplikacja powinna mieć przydzieloną rolę tylko do odczytu (SELECT).

Uruchamianie aplikacji w bezpiecznym środowisku dodatkowo zwiększa ochronę. W scenariuszach korporacyjnych dane są zwykle ekstraktowane i przekształcane z systemów operacyjnych do bazy danych tylko do odczytu lub hurtowni danych o przyjaznym schemacie. Podejście to zapewnia, że dane są bezpieczne, zoptymalizowane pod kątem wydajności i dostępności oraz że aplikacja ma ograniczony, tylko do odczytu dostęp.

## Przykładowe kody

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Masz więcej pytań dotyczących Wzorca użycia narzędzi?

Dołącz do [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), aby spotkać się z innymi uczącymi się, uczestniczyć w godzinach konsultacji i uzyskać odpowiedzi na pytania dotyczące Twoich agentów AI.

## Dodatkowe zasoby

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Warsztat Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Contoso Creative Writer Multi-Agent Workshop</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Przegląd Microsoft Agent Framework</a>

## Poprzednia lekcja

[Zrozumienie wzorców projektowych agentycznych](../03-agentic-design-patterns/README.md)

## Następna lekcja
[Agentyczny RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Zastrzeżenie:
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI Co-op Translator (https://github.com/Azure/co-op-translator). Chociaż dążymy do jak największej dokładności, prosimy pamiętać, że tłumaczenia automatyczne mogą zawierać błędy lub niedokładności. Oryginalny dokument w języku źródłowym należy traktować jako dokument wiążący. W przypadku informacji o krytycznym znaczeniu zaleca się skorzystanie z usług profesjonalnego tłumacza. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->