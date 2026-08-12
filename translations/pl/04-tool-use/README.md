[![Jak zaprojektować dobre agenty AI](../../../translated_images/pl/lesson-4-thumbnail.546162853cb3daff.webp)](https://youtu.be/vieRiPRx-gI?si=cEZ8ApnT6Sus9rhn)

> _(Kliknij powyższy obraz, aby obejrzeć wideo z tej lekcji)_

# Wzorzec projektowy użycia narzędzi

Narzędzia są interesujące, ponieważ pozwalają agentom AI posiadać szerszy zakres możliwości. Zamiast agenta dysponującego ograniczonym zestawem akcji, które może wykonać, dodając narzędzie, agent może teraz wykonywać szeroki zakres działań. W tym rozdziale przyjrzymy się Wzorcowi projektowemu użycia narzędzi, który opisuje, jak agenci AI mogą korzystać ze specyficznych narzędzi, aby osiągnąć swoje cele.

## Wprowadzenie

W tej lekcji chcemy odpowiedzieć na następujące pytania:

- Czym jest wzorzec projektowy użycia narzędzi?
- Do jakich przypadków użycia może być stosowany?
- Jakie są elementy/bloki budulcowe potrzebne do implementacji tego wzorca?
- Jakie są specjalne rozważania dotyczące korzystania z wzorca użycia narzędzi, aby budować godnych zaufania agentów AI?

## Cele nauki

Po ukończeniu tej lekcji będziesz potrafił:

- Zdefiniować wzorzec projektowy użycia narzędzi i jego cel.
- Zidentyfikować przypadki użycia, w których wzorzec użycia narzędzi jest stosowalny.
- Zrozumieć kluczowe elementy potrzebne do implementacji wzorca.
- Rozpoznać rozważania zapewniające wiarygodność agentów AI korzystających z tego wzorca.

## Czym jest wzorzec projektowy użycia narzędzi?

**Wzorzec projektowy użycia narzędzi** koncentruje się na umożliwieniu modelom LLM interakcji z zewnętrznymi narzędziami w celu osiągnięcia konkretnych celów. Narzędzia to kod, który może być wykonywany przez agenta, aby realizować działania. Narzędzie może być prostą funkcją, taką jak kalkulator, lub wywołaniem API do usługi zewnętrznej, takiej jak sprawdzanie cen akcji lub prognoza pogody. W kontekście agentów AI narzędzia są zaprojektowane tak, aby agent mógł je wywołać w odpowiedzi na **funkcje wywołane przez model**.

## Do jakich przypadków użycia można go zastosować?

Agenci AI mogą wykorzystywać narzędzia do realizacji złożonych zadań, pobierania informacji lub podejmowania decyzji. Wzorzec użycia narzędzi jest często stosowany w scenariuszach wymagających dynamicznej interakcji z zewnętrznymi systemami, takimi jak bazy danych, usługi internetowe lub interpretery kodu. Ta zdolność jest przydatna w wielu różnych przypadkach użycia, w tym:

- **Dynamiczne pobieranie informacji:** Agenci mogą wysyłać zapytania do zewnętrznych API lub baz danych, aby pobrać aktualne dane (np. zapytanie do bazy SQLite na potrzeby analizy danych, pobieranie cen akcji lub informacji pogodowych).
- **Wykonywanie i interpretacja kodu:** Agenci mogą uruchamiać kod lub skrypty, aby rozwiązywać problemy matematyczne, generować raporty lub przeprowadzać symulacje.
- **Automatyzacja przepływów pracy:** Automatyzacja powtarzalnych lub wieloetapowych procesów poprzez integrację narzędzi takich jak planery zadań, usługi e-mail albo potoki danych.
- **Wsparcie klienta:** Agenci mogą wchodzić w interakcje z systemami CRM, platformami ticketingowymi lub bazami wiedzy, aby rozwiązywać zapytania użytkowników.
- **Generowanie i edycja treści:** Agenci mogą wykorzystywać narzędzia takie jak korektory gramatyczne, streszczacze tekstu lub oceny bezpieczeństwa treści, aby pomagać w zadaniach tworzenia treści.

## Jakie są elementy/bloki budulcowe potrzebne do implementacji wzorca użycia narzędzi?

Te bloki budulcowe pozwalają agentowi AI wykonywać szeroki zakres zadań. Przyjrzyjmy się kluczowym elementom potrzebnym do implementacji Wzorca projektowego użycia narzędzi:

- **Schematy funkcji/narzędzi**: Szczegółowe definicje dostępnych narzędzi, obejmujące nazwę funkcji, cel, wymagane parametry i oczekiwane wyniki. Te schematy umożliwiają modelowi LLM zrozumienie, jakie narzędzia są dostępne i jak tworzyć poprawne zapytania.

- **Logika wykonania funkcji**: Reguluje, jak i kiedy narzędzia są wywoływane na podstawie intencji użytkownika i kontekstu rozmowy. Może to obejmować moduły planujące, mechanizmy trasowania lub warunkowe przepływy decydujące o dynamicznym użyciu narzędzi.

- **System obsługi wiadomości**: Komponenty zarządzające przepływem konwersacji między wejściami użytkownika, odpowiedziami LLM, wywołaniami funkcji narzędzi i ich wynikami.

- **Infrastruktura integracji narzędzi**: Struktura łącząca agenta z różnymi narzędziami, czy to prostymi funkcjami, czy złożonymi usługami zewnętrznymi.

- **Obsługa błędów i walidacja**: Mechanizmy obsługi niepowodzeń podczas wykonywania narzędzi, walidacji parametrów oraz zarządzania nieoczekiwanymi odpowiedziami.

- **Zarządzanie stanem**: Śledzi kontekst rozmowy, wcześniejsze interakcje z narzędziami oraz dane trwałe, aby zapewnić spójność podczas wieloetapowych interakcji.

Następnie przyjrzyjmy się szczegółowiej wywoływaniu funkcji/narzędzi.
 
### Wywoływanie funkcji/narzędzi

Wywoływanie funkcji to główny sposób, w jaki umożliwiamy dużym modelom językowym (LLM) interakcję z narzędziami. Często nazwy „Funkcja” i „Narzędzie” używane są zamiennie, ponieważ „funkcje” (bloki wielokrotnego użytku kodu) to „narzędzia”, z których agenci korzystają do wykonywania zadań. Aby wywołać kod funkcji, LLM musi porównać żądanie użytkownika z opisem funkcji. W tym celu do LLM przesyłany jest schemat zawierający opisy wszystkich dostępnych funkcji. LLM wybiera wtedy najbardziej odpowiednią funkcję do zadania i zwraca jej nazwę oraz argumenty. Wybrana funkcja jest wywoływana, jej odpowiedź wysyłana z powrotem do LLM, który używa tych informacji do odpowiedzi na prośbę użytkownika.

Aby deweloperzy mogli zaimplementować wywoływanie funkcji dla agentów, potrzebują:

1. Modelu LLM obsługującego wywoływanie funkcji
2. Schematów opisujących funkcje
3. Kodu dla każdej opisanej funkcji

Posłużmy się przykładem pobierania aktualnego czasu w mieście, aby to zilustrować:

1. **Zainicjuj model LLM obsługujący wywoływanie funkcji:**

    Nie wszystkie modele obsługują wywoływanie funkcji, dlatego ważne jest sprawdzenie, czy używany model to wspiera.     <a href="https://learn.microsoft.com/azure/ai-services/openai/how-to/function-calling" target="_blank">Azure OpenAI</a> obsługuje wywoływanie funkcji. Możemy zacząć od inicjacji klienta OpenAI z użyciem Azure OpenAI **Responses API** (stabilny endpoint `/openai/v1/` — bez potrzeby podawania `api_version`). 

    ```python
    # Zainicjuj klienta OpenAI dla Azure OpenAI (Responses API, punkt końcowy v1)
    client = OpenAI(
        base_url=f"{os.environ['AZURE_OPENAI_ENDPOINT'].rstrip('/')}/openai/v1/",
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
    )
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    ```

1. **Utwórz schemat funkcji**:

    Następnie zdefiniujemy schemat JSON zawierający nazwę funkcji, opis jej działania oraz nazwy i opisy parametrów.
    Przekażemy ten schemat do klienta stworzonego wcześniej, wraz z prośbą użytkownika o sprawdzenie czasu w San Francisco. Ważne jest, aby zaznaczyć, że zwracane jest **wywołanie narzędzia**, a **nie** ostateczna odpowiedź na pytanie. Jak wspomniano wcześniej, LLM zwraca nazwę wybranej funkcji oraz argumenty, które zostaną do niej przekazane.

    ```python
    # Opis funkcji do odczytu przez model (format narzędzia Responses API flat)
    tools = [
        {
            "type": "function",
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
    ]
    ```
   
    ```python
  
    # Początkowa wiadomość użytkownika
    messages = [{"role": "user", "content": "What's the current time in San Francisco"}]

    # Pierwsze wywołanie API: Poproś model o użycie funkcji
    response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        tool_choice="auto",
        store=False,
    )

    # API odpowiedzi zwraca wywołania narzędzi jako elementy function_call w response.output.
    # Dołącz je do konwersacji, aby model miał pełny kontekst przy następnym ruchu.
    messages += response.output

    print("Model's response:")
    print(response.output)
  
    ```

    ```bash
    Model's response:
    [ResponseFunctionToolCall(arguments='{"location":"San Francisco"}', call_id='call_pOsKdUlqvdyttYB67MOj434b', name='get_current_time', type='function_call')]
    ```
  
1. **Kod funkcji wymagany do realizacji zadania:**

    Teraz, gdy LLM wybrał, która funkcja ma zostać uruchomiona, trzeba zaimplementować i wykonać kod realizujący zadanie.
    Możemy zaimplementować kod pobierający aktualny czas w Pythonie. Musimy też napisać kod do wyodrębnienia nazwy i argumentów z `response_message`, aby uzyskać ostateczny wynik.

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
    tool_calls = [item for item in response.output if item.type == "function_call"]
    if tool_calls:
        for tool_call in tool_calls:
            if tool_call.name == "get_current_time":

                function_args = json.loads(tool_call.arguments)

                time_response = get_current_time(
                    location=function_args.get("location")
                )

                # Zwróć wynik narzędzia jako element function_call_output
                messages.append({
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": time_response,
                })
    else:
        print("No tool calls were made by the model.")

    # Drugie wywołanie API: Pobierz ostateczną odpowiedź od modelu
    final_response = client.responses.create(
        model=deployment_name,
        input=messages,
        tools=tools,
        store=False,
    )

    return final_response.output_text
     ```

     ```bash
      get_current_time called with location: San Francisco
      Timezone found for san francisco
      The current time in San Francisco is 09:24 AM.
     ```

Wywoływanie funkcji jest sercem większości, jeśli nie wszystkich, projektów użycia narzędzi w agentach, jednak implementacja od podstaw może być czasem wyzwaniem.
Jak nauczyliśmy się w [Lekcji 2](../../../02-explore-agentic-frameworks), frameworki agentyczne dostarczają gotowe bloki budulcowe do implementacji użycia narzędzi.
 
## Przykłady użycia narzędzi z frameworkami agentycznymi

Oto kilka przykładów, jak możesz zaimplementować Wzorzec projektowy użycia narzędzi przy użyciu różnych frameworków agentycznych:

### Microsoft Agent Framework

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Agent Framework</a> to otwarty framework AI do tworzenia agentów AI. Upraszcza on proces wywoływania funkcji, pozwalając definiować narzędzia jako funkcje Pythona z dekoratorem `@tool`. Framework zarządza komunikacją między modelem a twoim kodem. Ponadto zapewnia dostęp do wbudowanych narzędzi, takich jak Wyszukiwanie plików i Interpreter kodu przez `FoundryChatClient`.

Poniższy diagram ilustruje proces wywoływania funkcji w Microsoft Agent Framework:

![function calling](../../../translated_images/pl/functioncalling-diagram.a84006fc287f6014.webp)

W Microsoft Agent Framework narzędzia są definiowane jako dekorowane funkcje. Możemy przekształcić funkcję `get_current_time`, którą widzieliśmy wcześniej, w narzędzie używając dekoratora `@tool`. Framework automatycznie zserializuje funkcję i jej parametry, tworząc schemat do wysłania do LLM.

```python
import os
from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity import AzureCliCredential

@tool(approval_mode="never_require")
def get_current_time(location: str) -> str:
    """Get the current time for a given location"""
    ...

# Utwórz klienta
provider = FoundryChatClient(
    project_endpoint=os.environ["AZURE_AI_PROJECT_ENDPOINT"],
    model=os.environ["AZURE_AI_MODEL_DEPLOYMENT_NAME"],
    credential=AzureCliCredential(),
)

# Utwórz agenta i uruchom za pomocą narzędzia
agent = provider.as_agent(name="TimeAgent", instructions="Use available tools to answer questions.", tools=get_current_time)
response = await agent.run("What time is it?")
```
  
### Microsoft Foundry Agent Service

<a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Microsoft Foundry Agent Service</a> to nowszy framework agentyczny zaprojektowany tak, aby umożliwić deweloperom bezpieczne budowanie, wdrażanie i skalowanie wysokiej jakości i rozszerzalnych agentów AI bez konieczności zarządzania podstawowymi zasobami obliczeniowymi i storage. Jest szczególnie przydatny w zastosowaniach korporacyjnych, ponieważ jest to w pełni zarządzana usługa z zabezpieczeniami na poziomie przedsiębiorstwa.

W porównaniu do bezpośredniego używania API LLM, Microsoft Foundry Agent Service oferuje kilka zalet, w tym:

- Automatyczne wywoływanie narzędzi – nie trzeba samodzielnie parsować wywołania narzędzia, uruchamiać go i obsługiwać odpowiedzi; wszystko to odbywa się teraz po stronie serwera
- Bezpiecznie zarządzane dane – zamiast zarządzać własnym stanem rozmowy, można polegać na wątkach, które przechowują wszystkie potrzebne informacje
- Narzędzia gotowe do użycia – narzędzia, które można wykorzystać do interakcji z twoimi źródłami danych, takimi jak Bing, Azure AI Search oraz Azure Functions.

Dostępne narzędzia w Microsoft Foundry Agent Service można podzielić na dwie kategorie:

1. Narzędzia wiedzy:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/bing-grounding?tabs=python&pivots=overview" target="_blank">Grounding z Bing Search</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/file-search?tabs=python&pivots=overview" target="_blank">Wyszukiwanie plików</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-ai-search?tabs=azurecli%2Cpython&pivots=overview-azure-ai-search" target="_blank">Azure AI Search</a>

2. Narzędzia akcji:
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/function-calling?tabs=python&pivots=overview" target="_blank">Wywoływanie funkcji</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/code-interpreter?tabs=python&pivots=overview" target="_blank">Interpreter kodu</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/openapi-spec?tabs=python&pivots=overview" target="_blank">Narzędzia definiowane przez OpenAPI</a>
    - <a href="https://learn.microsoft.com/azure/ai-services/agents/how-to/tools/azure-functions?pivots=overview" target="_blank">Azure Functions</a>

Usługa Agent Service pozwala korzystać z tych narzędzi razem jako `zestaw narzędzi`. Korzysta też z `wątków`, które śledzą historię wiadomości danej rozmowy.

Wyobraź sobie, że jesteś agentem sprzedaży w firmie o nazwie Contoso. Chcesz stworzyć agenta konwersacyjnego, który będzie odpowiadać na pytania o dane sprzedażowe.

Poniższy obraz ilustruje, jak możesz użyć Microsoft Foundry Agent Service do analizy danych sprzedaży:

![Agentic Service In Action](../../../translated_images/pl/agent-service-in-action.34fb465c9a84659e.webp)

Aby korzystać z tych narzędzi z usługą, możemy utworzyć klienta i zdefiniować narzędzie lub zestaw narzędzi. W praktyce możemy użyć następującego kodu Python. Model LLM będzie mógł spojrzeć na zestaw narzędzi i zdecydować, czy użyć funkcji stworzonej przez użytkownika `fetch_sales_data_using_sqlite_query`, czy gotowego interpretera kodu, w zależności od prośby użytkownika.

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
code_interpreter = CodeInterpreterTool()toolset.add(code_interpreter)

agent = project_client.agents.create_agent(
    model="gpt-5-mini", name="my-agent", instructions="You are helpful agent", 
    toolset=toolset
)
```

## Jakie są specjalne rozważania dotyczące korzystania z Wzorca projektowego użycia narzędzi, aby budować godnych zaufania agentów AI?

Powszechnym zmartwieniem dotyczącym dynamicznie generowanego przez LLM SQL jest bezpieczeństwo, szczególnie ryzyko wstrzyknięcia SQL lub działania złośliwe, takie jak usuwanie czy manipulacja bazą danych. Chociaż te obawy są uzasadnione, można je skutecznie złagodzić odpowiednią konfiguracją uprawnień dostępu do bazy danych. Dla większości baz polega to na skonfigurowaniu bazy jako tylko do odczytu. Dla baz danych takich jak PostgreSQL czy Azure SQL aplikacja powinna mieć przypisaną rolę tylko do odczytu (SELECT).

Uruchamianie aplikacji w bezpiecznym środowisku dodatkowo zwiększa ochronę. W scenariuszach korporacyjnych dane są zazwyczaj wyodrębniane i transformowane z systemów operacyjnych do bazy lub hurtowni danych tylko do odczytu ze schema przyjaznym użytkownikowi. Takie podejście zapewnia, że dane są bezpieczne, zoptymalizowane pod względem wydajności i dostępności, a aplikacja ma ograniczony, tylko do odczytu dostęp.

## Przykładowe kody

- Python: [Agent Framework](./code_samples/04-python-agent-framework.ipynb)
- .NET: [Agent Framework](./code_samples/04-dotnet-agent-framework.md)

## Masz więcej pytań na temat Wzorców projektowych użycia narzędzi?

Dołącz do [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), aby spotkać innych uczących się, uczestniczyć w godzinach konsultacji i uzyskać odpowiedzi na pytania dotyczące agentów AI.

## Dodatkowe zasoby

- <a href="https://microsoft.github.io/build-your-first-agent-with-azure-ai-agent-service-workshop/" target="_blank">Warsztaty Azure AI Agents Service</a>
- <a href="https://github.com/Azure-Samples/contoso-creative-writer/tree/main/docs/workshop" target="_blank">Warsztaty Multi-Agent Contoso Creative Writer</a>
- <a href="https://learn.microsoft.com/azure/ai-services/agents/overview" target="_blank">Przegląd Microsoft Agent Framework</a>


## Testowanie wstępne tego agenta (opcjonalne)

Po nauce wdrażania agentów w [Lekcji 16](../16-deploying-scalable-agents/README.md), możesz wykonać test wstępny `TravelToolAgent` z tej lekcji (czy nadal wywołuje swoje narzędzia i odpowiada?) za pomocą [`tests/lesson-04-smoke-tests.json`](../../../tests/lesson-04-smoke-tests.json). Zobacz [`tests/README.md`](../tests/README.md), aby dowiedzieć się, jak go uruchomić.

## Poprzednia lekcja

[Zrozumienie wzorców projektowych agentów](../03-agentic-design-patterns/README.md)

## Następna lekcja

[Agentic RAG](../05-agentic-rag/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->