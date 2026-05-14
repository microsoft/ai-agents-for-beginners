[![Jak projektować dobre agentów AI](../../../translated_images/pl/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Kliknij powyższy obraz, aby obejrzeć wideo z tej lekcji)_

# Wzorzec projektowy użycia narzędzi

Narzędzia są interesujące, ponieważ pozwalają agentom AI mieć szerszy zakres możliwości. Zamiast agenta z ograniczonym zestawem akcji, które może wykonać, poprzez dodanie narzędzia agent może wykonywać szeroki zakres działań. W tym rozdziale przyjrzymy się Wzorcu projektowemu użycia narzędzi, który opisuje, jak agenci AI mogą korzystać ze specyficznych narzędzi, by osiągać swoje cele.

## Wprowadzenie

W tej lekcji chcemy odpowiedzieć na następujące pytania:

- Czym jest wzorzec projektowy użycia narzędzi?
- Do jakich przypadków użycia można go zastosować?
- Jakie elementy/bloki budulcowe są potrzebne do implementacji tego wzorca?
- Jakie specjalne uwagi należy wziąć pod uwagę, stosując wzorzec użycia narzędzi do budowy godnych zaufania agentów AI?

## Cele nauki

Po ukończeniu tej lekcji będziesz potrafił:

- Zdefiniować wzorzec projektowy użycia narzędzi i jego cel.
- Zidentyfikować przypadki użycia, w których wzorzec jest stosowalny.
- Zrozumieć kluczowe elementy potrzebne do implementacji tego wzorca.
- Rozpoznać kwestie związane z zapewnieniem wiarygodności agentów AI wykorzystujących ten wzorzec.

## Czym jest wzorzec projektowy użycia narzędzi?

**Wzorzec projektowy użycia narzędzi** skupia się na umożliwieniu modelom LLM interakcji z zewnętrznymi narzędziami w celu osiągania konkretnych celów. Narzędzia to kod, który agent może wykonać, aby podjąć działania. Narzędzie może być prostą funkcją, taką jak kalkulator, lub wywołaniem API do usługi zewnętrznej, takiej jak pobieranie kursów akcji czy prognozy pogody. W kontekście agentów AI narzędzia są zaprojektowane tak, aby mogły być wywoływane przez agentów jako odpowiedź na **funkcje generowane przez model**.

## Do jakich przypadków użycia można go zastosować?

Agenci AI mogą wykorzystywać narzędzia do realizacji złożonych zadań, pozyskiwania informacji lub podejmowania decyzji. Wzorzec użycia narzędzi jest często stosowany w scenariuszach wymagających dynamicznej interakcji z systemami zewnętrznymi, takimi jak bazy danych, usługi internetowe czy interpretery kodu. Ta zdolność jest przydatna w wielu różnych przypadkach użycia, w tym:

- **Dynamiczne pobieranie informacji:** Agenci mogą zapytywać zewnętrzne API lub bazy danych, aby pobrać aktualne dane (np. zapytania do bazy SQLite w celu analizy danych, pobieranie cen akcji lub informacji o pogodzie).
- **Wykonywanie i interpretacja kodu:** Agenci mogą wykonywać kod lub skrypty, aby rozwiązywać problemy matematyczne, generować raporty lub przeprowadzać symulacje.
- **Automatyzacja przepływów pracy:** Automatyzacja powtarzalnych lub wieloetapowych procesów poprzez integrację narzędzi takich jak harmonogramy zadań, usługi e-mail lub potoki danych.
- **Wsparcie klienta:** Agenci mogą wchodzić w interakcję z systemami CRM, platformami zgłoszeń lub bazami wiedzy, aby rozwiązywać zapytania użytkowników.
- **Generowanie i edycja treści:** Agenci mogą korzystać z narzędzi takich jak korektory gramatyczne, streszczacze tekstu czy oceniacze bezpieczeństwa treści, aby wspierać zadania tworzenia treści.

## Jakie są elementy/bloki budulcowe potrzebne do implementacji wzorca użycia narzędzi?

Te bloki budulcowe umożliwiają agentowi AI wykonywanie szerokiego zakresu zadań. Przyjrzyjmy się kluczowym elementom potrzebnym do implementacji Wzorca użycia narzędzi:

- **Schematy funkcji/narzędzi**: Szczegółowe definicje dostępnych narzędzi, w tym nazwa funkcji, cel, wymagane parametry i oczekiwane wyniki. Schematy te umożliwiają modelowi LLM zrozumienie, jakie narzędzia są dostępne i jak skonstruować prawidłowe żądania.

- **Logika wykonywania funkcji**: Zarządza tym, jak i kiedy narzędzia są wywoływane na podstawie intencji użytkownika i kontekstu rozmowy. Może obejmować moduły planujące, mechanizmy trasowania lub warunkowe przepływy decyzyjne, które dynamicznie określają użycie narzędzi.

- **System obsługi wiadomości**: Komponenty zarządzające przebiegiem konwersacji pomiędzy wejściami użytkownika, odpowiedziami LLM, wywołaniami narzędzi i ich rezultatami.

- **Framework integracji narzędzi**: Infrastruktura łącząca agenta z różnymi narzędziami, czy to prostymi funkcjami, czy złożonymi zewnętrznymi usługami.

- **Obsługa błędów i walidacja**: Mechanizmy obsługi błędów podczas wykonywania narzędzi, walidacji parametrów i zarządzania nieoczekiwanymi odpowiedziami.

- **Zarządzanie stanem**: Śledzi kontekst rozmowy, wcześniejsze interakcje z narzędziami oraz dane trwałe, aby zapewnić spójność w wieloetapowych interakcjach.

Teraz przyjrzyjmy się wywoływaniu funkcji/narzędzi bardziej szczegółowo.

### Wywoływanie funkcji/narzędzi

Wywoływanie funkcji to podstawowy sposób, w jaki umożliwiamy modelom językowym (LLM) interakcję z narzędziami. Często słowa „Funkcja” i „Narzędzie” są używane zamiennie, ponieważ „funkcje” (bloki wielokrotnego użytku kodu) są „narzędziami”, których agent używa do realizacji zadań. Aby kod funkcji mógł zostać wywołany, LLM musi porównać żądanie użytkownika z opisem funkcji. W tym celu wysyła się do LLM schemat zawierający opisy wszystkich dostępnych funkcji. LLM następnie wybiera najbardziej odpowiednią funkcję do zadania i zwraca jej nazwę oraz argumenty. Wybrana funkcja jest wywoływana, a jej odpowiedź przekazywana z powrotem do LLM, które wykorzystuje te informacje, aby odpowiedzieć użytkownikowi.

Aby zrealizować wywoływanie funkcji w agentach, potrzebne są:

1. Model LLM obsługujący wywoływanie funkcji
2. Schemat zawierający opisy funkcji
3. Kod każdej opisywanej funkcji

Użyjmy przykładu uzyskania aktualnego czasu w mieście, aby zobrazować to na przykładzie:

1. **Inicjalizacja LLM obsługującego wywoływanie funkcji:**

    Nie wszystkie modele obsługują wywoływanie funkcji, więc ważne jest, by upewnić się, że używany model to potrafi. <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> obsługuje wywoływanie funkcji. Możemy zacząć od uruchomienia klienta Azure OpenAI.

    ```python
    # Inicjalizuj klienta Azure OpenAI
    client = AzureOpenAI(
        azure_endpoint = os.getenv("AZURE_AI_PROJECT_ENDPOINT"), 
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),  
        api_version="2024-05-01-preview"
    )
    ```

1. **Utworzenie schematu funkcji:**

    Następnie zdefiniujemy schemat JSON, który zawiera nazwę funkcji, opis tego, co funkcja robi, oraz nazwy i opisy parametrów funkcji.
    Ten schemat przekażemy klientowi utworzonemu wcześniej, wraz z żądaniem użytkownika dotyczącym uzyskania czasu w San Francisco. Ważne jest, że **wywołanie narzędzia** jest zwracane, **nie** ostateczna odpowiedź na pytanie. Jak wspomniano wcześniej, LLM zwraca nazwę wybranej funkcji i argumenty, które zostaną do niej przekazane.

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
  
    # Pierwsza wiadomość użytkownika
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

    Teraz, gdy LLM wybrał funkcję, która musi zostać uruchomiona, należy zaimplementować i wykonać kod realizujący zadanie.
    Możemy napisać kod w Pythonie, który pobierze aktualny czas. Trzeba też zaimplementować kod, który wyciąga nazwę i argumenty z response_message, aby uzyskać wynik końcowy.

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
     # Obsłuż wywołania funkcji
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
  
      # Drugie wywołanie API: Pobierz końcową odpowiedź od modelu
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

Wywoływanie funkcji jest sercem większości, jeśli nie wszystkich, wzorców użycia narzędzi w agentach, jednak implementacja od podstaw może być czasem wyzwaniem.
Jak dowiedzieliśmy się w [Lekcji 2](../../../02-explore-agentic-frameworks), frameworki agentowe dostarczają predefiniowane bloki budulcowe do implementacji użycia narzędzi.
 
## Przykłady użycia narzędzi z frameworkami agentowymi

Oto kilka przykładów, jak można zaimplementować wzorzec użycia narzędzi korzystając z różnych frameworków agentowych:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> to framework AI open-source do budowy agentów AI. Upraszcza proces używania wywoływania funkcji, pozwalając definiować narzędzia jako funkcje Pythona z dekoratorem `@tool`. Framework zarządza komunikacją między modelem a twoim kodem. Zapewnia też dostęp do gotowych narzędzi, takich jak Wyszukiwanie plików i Interpreter kodu przez `AzureAIProjectAgentProvider`.

Poniższy diagram ilustruje proces wywoływania funkcji w Microsoft Agent Framework:

![function calling](../../../translated_images/pl/functioncalling-diagram.a84006fc287f6014.webp)

W Microsoft Agent Framework narzędzia definiuje się jako funkcje ozdobione dekoratorem. Możemy przekształcić funkcję `get_current_time`, którą widzieliśmy wcześniej, w narzędzie stosując dekorator `@tool`. Framework automatycznie zserializuje funkcję i jej parametry, tworząc schemat do przesłania do LLM.

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

# Utwórz agenta i uruchom za pomocą narzędzia
agent = await provider.create_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Azure AI Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Azure AI Agent Service</a> to nowszy framework agentowy, zaprojektowany, by umożliwić deweloperom bezpieczne tworzenie, wdrażanie i skalowanie wysokiej jakości, rozszerzalnych agentów AI bez konieczności zarządzania podstawowymi zasobami obliczeniowymi i przechowywania. Jest szczególnie przydatny dla aplikacji korporacyjnych, gdyż jest w pełni zarządzaną usługą o zabezpieczeniach klasy korporacyjnej.

W porównaniu do bezpośredniego korzystania z API LLM, Azure AI Agent Service oferuje pewne zalety, w tym:

- Automatyczne wywoływanie narzędzi – nie trzeba parsować wywołania narzędzia, uruchamiać go i obsługiwać odpowiedzi; wszystko to odbywa się po stronie serwera.
- Bezpiecznie zarządzane dane – zamiast zarządzać własnym stanem rozmowy, można polegać na wątkach do przechowywania wszystkich potrzebnych informacji.
- Gotowe narzędzia – narzędzia do interakcji ze źródłami danych, takie jak Bing, Azure AI Search i Azure Functions.

Narzędzia dostępne w Azure AI Agent Service można podzielić na dwie kategorie:

1. Narzędzia wiedzy:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Podstawianie z Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Wyszukiwanie plików</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Narzędzia działań:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Wywoływanie funkcji</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Interpreter kodu</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Narzędzia definiowane przez OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Usługa Agent Service pozwala korzystać z tych narzędzi razem jako `toolset`. Wykorzystuje także `wątki`, które śledzą historię wiadomości z konkretnej rozmowy.

Wyobraź sobie, że jesteś agentem sprzedaży w firmie Contoso. Chcesz stworzyć agenta konwersacyjnego, który może odpowiadać na pytania dotyczące twoich danych sprzedażowych.

Poniższy obraz ilustruje, jak można użyć Azure AI Agent Service do analizy danych sprzedaży:

![Agentic Service In Action](../../../translated_images/pl/agent-service-in-action.34fb465c9a84659e.webp)

Aby użyć dowolnego z tych narzędzi w usłudze, możemy stworzyć klienta i zdefiniować narzędzie lub zestaw narzędzi. Praktyczna implementacja może wyglądać zgodnie z poniższym kodem Pythona. LLM będzie mógł rozważyć użycie funkcji stworzonej przez użytkownika `fetch_sales_data_using_sqlite_query` albo predefiniowanego Interpretera kodu, w zależności od zapytania użytkownika.

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

# Inicjalizuj zestaw narzędzi
toolset = ToolSet()

# Inicjalizuj agenta wywołującego funkcje z funkcją fetch_sales_data_using_sqlite_query i dodaj go do zestawu narzędzi
fetch_data_function = FunctionTool(fetch_sales_data_using_sqlite_query)
toolset.add(fetch_data_function)

# Inicjalizuj narzędzie Code Interpreter i dodaj je do zestawu narzędzi.
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-4o-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Jakie są specjalne uwagi dotyczące stosowania wzorca użycia narzędzi do budowy godnych zaufania agentów AI?

Częstym problemem związanym z dynamicznie generowanym przez LLM SQL jest bezpieczeństwo, szczególnie ryzyko SQL injection lub działania złośliwe, takie jak usunięcie bazy danych lub manipulacje w niej. Chociaż te obawy są uzasadnione, można je skutecznie złagodzić poprzez odpowiednią konfigurację uprawnień dostępu do bazy danych. Dla większości baz danych oznacza to ustawienie bazy jako tylko do odczytu. W usługach bazodanowych takich jak PostgreSQL czy Azure SQL, aplikacji powinno się przypisać rolę tylko do odczytu (SELECT).

Uruchamianie aplikacji w bezpiecznym środowisku dodatkowo podnosi ochronę. W scenariuszach korporacyjnych dane zazwyczaj są wydobywane i transformowane z systemów operacyjnych do bazy danych lub hurtowni danych tylko do odczytu, o przyjaznym dla użytkownika schemacie. Takie podejście gwarantuje, że dane są bezpieczne, zoptymalizowane pod względem wydajności i dostępności, a aplikacja ma ograniczony, tylko do odczytu dostęp.

## Przykładowe kody

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Masz więcej pytań dotyczących wzorców użycia narzędzi?

Dołącz do [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord), aby spotkać innych uczących się, uczestniczyć w godzinach konsultacji i uzyskać odpowiedzi na swoje pytania dotyczące agentów AI.

## Dodatkowe zasoby

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Warsztaty Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Warsztaty wieloagentowe Contoso Creative Writer</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Przegląd Microsoft Agent Framework</a>

## Poprzednia lekcja

[Zrozumienie wzorców agentowych](../03-agentic-design-patterns/README.md)

## Następna lekcja
[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->