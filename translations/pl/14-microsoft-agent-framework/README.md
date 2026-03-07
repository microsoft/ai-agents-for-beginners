# Poznawanie Microsoft Agent Framework

![Framework agenta](../../../translated_images/pl/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Wprowadzenie

Ta lekcja będzie obejmować:

- Zrozumienie Microsoft Agent Framework: kluczowe funkcje i wartość  
- Poznanie kluczowych koncepcji Microsoft Agent Framework
- Zaawansowane wzorce MAF: przepływy pracy, middleware i pamięć

## Cele nauki

Po ukończeniu tej lekcji będziesz potrafić:

- Budować gotowe do produkcji agentów AI przy użyciu Microsoft Agent Framework
- Zastosować podstawowe funkcje Microsoft Agent Framework do swoich przypadków użycia z agentami
- Korzystać z zaawansowanych wzorców, w tym przepływów pracy, middleware i obserwowalności

## Przykłady kodu 

Przykłady kodu dla [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) można znaleźć w tym repozytorium w plikach `xx-python-agent-framework` i `xx-dotnet-agent-framework`.

## Zrozumienie Microsoft Agent Framework

![Wprowadzenie do frameworka](../../../translated_images/pl/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framewrok) to zunifikowany framework Microsoftu do budowania agentów AI. Oferuje elastyczność do obsługi szerokiej gamy przypadków użycia agentów spotykanych zarówno w środowiskach produkcyjnych, jak i badawczych, w tym:

- **Sekwencyjna orkiestracja agentów** w scenariuszach, gdzie potrzebne są przepływy krok po kroku.
- **Równoczesna orkiestracja** w scenariuszach, gdzie agenci muszą wykonywać zadania jednocześnie.
- **Orkiestracja czatu grupowego** w scenariuszach, gdzie agenci mogą współpracować nad jednym zadaniem.
- **Handoff Orchestration** w scenariuszach, gdzie agenci przekazują sobie zadanie w miarę ukończenia podzadań.
- **Magnetic Orchestration** w scenariuszach, gdzie agent-manager tworzy i modyfikuje listę zadań oraz koordynuje podagentów w celu ukończenia zadania.

Aby dostarczać agentów AI w produkcji, MAF zawiera również funkcje dla:

- **Obserwowalności** poprzez użycie OpenTelemetry, gdzie każda akcja agenta AI, w tym wywołania narzędzi, kroki orkiestracji, przepływy rozumowania oraz monitorowanie wydajności za pośrednictwem pulpitów Microsoft Foundry.
- **Bezpieczeństwa** przez natywne hostowanie agentów na Microsoft Foundry, które obejmuje kontrole bezpieczeństwa takie jak kontrola dostępu oparta na rolach, obsługa prywatnych danych i wbudowane mechanizmy bezpieczeństwa treści.
- **Trwałości** ponieważ wątki agenta i przepływy pracy mogą być wstrzymywane, wznawiane i odzyskiwane po błędach, co umożliwia dłużej działające procesy.
- **Kontroli** ponieważ obsługiwane są przepływy pracy z udziałem człowieka, gdzie zadania są oznaczane jako wymagające zatwierdzenia przez człowieka.

Microsoft Agent Framework koncentruje się również na interoperacyjności poprzez:

- **Bycie niezależnym od chmury** - agenci mogą działać w kontenerach, lokalnie oraz w różnych chmurach.
- **Bycie niezależnym od dostawcy** - agenci mogą być tworzeni za pomocą preferowanego SDK, w tym Azure OpenAI i OpenAI
- **Integrację otwartych standardów** - agenci mogą wykorzystywać protokoły takie jak Agent-to-Agent (A2A) i Model Context Protocol (MCP) do wykrywania i używania innych agentów i narzędzi.
- **Wtyczki i konektory** - połączenia mogą być nawiązywane do usług danych i pamięci, takich jak Microsoft Fabric, SharePoint, Pinecone i Qdrant.

Spójrzmy, jak te funkcje są stosowane w niektórych kluczowych koncepcjach Microsoft Agent Framework.

## Kluczowe koncepcje Microsoft Agent Framework

### Agenci

![Komponenty agenta](../../../translated_images/pl/agent-components.410a06daf87b4fef.webp)

**Tworzenie agentów**

Tworzenie agenta polega na zdefiniowaniu usługi inferencyjnej (dostawcy LLM), zestawu instrukcji, których ma przestrzegać agent AI, oraz przypisanej `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Powyższe używa `Azure OpenAI`, ale agenci mogą być tworzeni przy użyciu różnych usług, w tym `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

Interfejsy API OpenAI `Responses`, `ChatCompletion`

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

lub zdalnych agentów używając protokołu A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Uruchamianie agentów**

Agenci są uruchamiani przy użyciu metod `.run` lub `.run_stream` dla odpowiednio odpowiedzi niestrumieniowych lub strumieniowych.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Każde uruchomienie agenta może również mieć opcje dostosowujące parametry, takie jak `max_tokens` używane przez agenta, `tools`, które agent może wywoływać, a nawet sam `model` używany przez agenta.

Jest to przydatne w przypadkach, gdy do wykonania zadania użytkownika wymagane są konkretne modele lub narzędzia.

**Narzędzia**

Narzędzia można zdefiniować zarówno podczas definiowania agenta:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Przy bezpośrednim tworzeniu obiektu ChatAgent

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

jak również podczas uruchamiania agenta:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Narzędzie dostępne tylko podczas tego uruchomienia )
```

**Wątki agenta**

Wątki agenta służą do obsługi konwersacji wieloetapowych. Wątki można tworzyć na dwa sposoby:

- Używając `get_new_thread()`, co umożliwia zapisywanie wątku w czasie
- Tworząc wątek automatycznie podczas uruchamiania agenta i pozwalając, by wątek istniał tylko podczas bieżącego uruchomienia.

Aby utworzyć wątek, kod wygląda tak:

```python
# Utwórz nowy wątek.
thread = agent.get_new_thread() # Uruchom agenta w tym wątku.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Następnie możesz zserializować wątek, aby przechować go do późniejszego użycia:

```python
# Utwórz nowy wątek.
thread = agent.get_new_thread() 

# Uruchom agenta z tym wątkiem.

response = await agent.run("Hello, how are you?", thread=thread) 

# Zserializuj wątek do przechowywania.

serialized_thread = await thread.serialize() 

# Zdeserializuj stan wątku po załadowaniu z przechowywania.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware agenta**

Agenci współdziałają z narzędziami i LLM, aby wykonać zadania użytkownika. W pewnych scenariuszach chcemy wykonać lub śledzić działania pomiędzy tymi interakcjami. Middleware agenta pozwala nam to zrobić poprzez:

*Middleware funkcji*

To middleware pozwala wykonać akcję pomiędzy agentem a funkcją/narzędziem, które będzie wywoływane. Przykładem użycia jest chęć zalogowania wywołania funkcji.

W poniższym kodzie `next` określa, czy powinno zostać wywołane następne middleware, czy właściwa funkcja.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Przetwarzanie wstępne: Zaloguj przed wywołaniem funkcji
    print(f"[Function] Calling {context.function.name}")

    # Przejdź do następnego middleware lub do wykonania funkcji
    await next(context)

    # Przetwarzanie końcowe: Zaloguj po wywołaniu funkcji
    print(f"[Function] {context.function.name} completed")
```

*Middleware czatu*

To middleware pozwala wykonać lub zalogować akcję pomiędzy agentem a żądaniami kierowanymi do LLM.

Zawiera to ważne informacje, takie jak `messages`, które są wysyłane do usługi AI.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Przetwarzanie wstępne: logowanie przed wywołaniem AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Kontynuuj do następnego middleware lub usługi AI
    await next(context)

    # Przetwarzanie końcowe: logowanie po otrzymaniu odpowiedzi AI
    print("[Chat] AI response received")

```

**Pamięć agenta**

Jak omówiono w lekcji `Agentic Memory`, pamięć jest ważnym elementem umożliwiającym agentowi działanie w różnych kontekstach. MAF oferuje kilka różnych typów pamięci:

*Pamięć w pamięci*

Jest to pamięć przechowywana w wątkach podczas działania aplikacji.

```python
# Utwórz nowy wątek.
thread = agent.get_new_thread() # Uruchom agenta z użyciem wątku.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Trwałe wiadomości*

Ta pamięć jest używana przy przechowywaniu historii konwersacji między różnymi sesjami. Jest zdefiniowana przy użyciu `chat_message_store_factory` :

```python
from agent_framework import ChatMessageStore

# Utwórz niestandardowy magazyn wiadomości
def create_message_store():
    return ChatMessageStore()

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a Travel assistant.",
    chat_message_store_factory=create_message_store
)

```

*Pamięć dynamiczna*

Ta pamięć jest dodawana do kontekstu przed uruchomieniem agentów. Te pamięci mogą być przechowywane w zewnętrznych usługach, takich jak mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Korzystanie z Mem0 w celu uzyskania zaawansowanych możliwości pamięci
memory_provider = Mem0Provider(
    api_key="your-mem0-api-key",
    user_id="user_123",
    application_id="my_app"
)

agent = ChatAgent(
    chat_client=OpenAIChatClient(),
    instructions="You are a helpful assistant with memory.",
    context_providers=memory_provider
)

```

**Obserwowalność agenta**

Obserwowalność jest ważna dla budowania niezawodnych i łatwych w utrzymaniu systemów agentowych. MAF integruje się z OpenTelemetry, aby zapewnić śledzenie (tracing) i mierniki dla lepszej obserwowalności.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # zrób coś
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Przepływy pracy

MAF oferuje przepływy pracy, które są zdefiniowanymi wcześniej krokami do wykonania zadania i zawierają agentów AI jako składniki tych kroków.

Przepływy pracy składają się z różnych komponentów, które pozwalają na lepszą kontrolę przepływu. Przepływy pracy umożliwiają również **orkiestrację wielu agentów** oraz **checkpointing**, aby zapisać stany przepływu pracy.

Główne komponenty przepływu pracy to:

**Wykonawcy**

Wykonawcy otrzymują wiadomości wejściowe, wykonują przypisane im zadania, a następnie generują wiadomość wyjściową. To przesuwa przepływ pracy dalej w kierunku ukończenia większego zadania. Wykonawcy mogą być agentami AI lub niestandardową logiką.

**Krawędzie**

Krawędzie służą do definiowania przepływu wiadomości w przepływie pracy. Mogą to być:

*Krawędzie bezpośrednie* - proste połączenia jeden-do-jednego między wykonawcami:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Krawędzie warunkowe* - aktywowane po spełnieniu określonego warunku. Na przykład, gdy pokoje hotelowe są niedostępne, wykonawca może zasugerować inne opcje.

*Krawędzie typu switch-case* - przekierowują wiadomości do różnych wykonawców na podstawie zdefiniowanych warunków. Na przykład, jeśli klient podróżny ma dostęp priorytetowy, jego zadania będą obsługiwane przez inny przepływ pracy.

*Krawędzie typu fan-out* - wysyłają jedną wiadomość do wielu celów.

*Krawędzie typu fan-in* - zbierają wiele wiadomości od różnych wykonawców i wysyłają je do jednego celu.

**Zdarzenia**

Aby zapewnić lepszą obserwowalność przepływów pracy, MAF oferuje wbudowane zdarzenia dla wykonania, w tym:

- `WorkflowStartedEvent`  - Rozpoczęcie wykonania przepływu pracy
- `WorkflowOutputEvent` - Przepływ pracy generuje wyjście
- `WorkflowErrorEvent` - Przepływ pracy napotkał błąd
- `ExecutorInvokeEvent`  - Wykonawca rozpoczyna przetwarzanie
- `ExecutorCompleteEvent`  -  Wykonawca kończy przetwarzanie
- `RequestInfoEvent` - Wydano żądanie

## Zaawansowane wzorce MAF

Powyższe sekcje obejmują kluczowe koncepcje Microsoft Agent Framework. Budując bardziej złożone agenty, oto niektóre zaawansowane wzorce do rozważenia:

- **Składanie middleware**: Łączenie wielu obsługujących middleware (logowanie, uwierzytelnianie, ograniczanie szybkości) przy użyciu middleware funkcji i czatu, aby uzyskać drobnoziarnistą kontrolę nad zachowaniem agenta.
- **Checkpointing przepływu pracy**: Używaj zdarzeń przepływu pracy i serializacji, aby zapisać i wznowić długotrwałe procesy agentów.
- **Dynamiczny dobór narzędzi**: Łącz RAG nad opisami narzędzi z rejestracją narzędzi MAF, aby prezentować tylko odpowiednie narzędzia dla zapytania.
- **Przekazywanie między agentami (Multi-Agent Handoff)**: Używaj krawędzi przepływu pracy i trasowania warunkowego do orkiestracji przekazywania między wyspecjalizowanymi agentami.

## Przykłady kodu 

Przykłady kodu dla Microsoft Agent Framework można znaleźć w tym repozytorium w plikach `xx-python-agent-framework` i `xx-dotnet-agent-framework`.

## Masz więcej pytań dotyczących Microsoft Agent Framework?

Dołącz do [Microsoft Foundry Discord](https://aka.ms/ai-agents/discord) aby spotkać innych uczących się, uczestniczyć w godzinach konsultacji i uzyskać odpowiedzi na swoje pytania dotyczące agentów AI.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
Zastrzeżenie:
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI Co-op Translator (https://github.com/Azure/co-op-translator). Chociaż dokładamy starań o dokładność, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy uznać za źródło wiążące. W przypadku informacji o krytycznym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->