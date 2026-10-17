# Eksploracja Microsoft Agent Framework

![Agent Framework](../../../translated_images/pl/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Wprowadzenie

Ta lekcja obejmie:

- Zrozumienie Microsoft Agent Framework: Kluczowe funkcje i wartość  
- Eksplorację kluczowych koncepcji Microsoft Agent Framework
- Zaawansowane wzorce MAF: przepływy pracy, middleware i pamięć

## Cele nauki

Po ukończeniu tej lekcji będziesz potrafił:

- Tworzyć produkcyjne AI Agentów z wykorzystaniem Microsoft Agent Framework
- Stosować podstawowe funkcje Microsoft Agent Framework w swoich przypadkach użycia agentów
- Używać zaawansowanych wzorców, w tym przepływów pracy, middleware i obserwowalności

## Przykłady kodu 

Przykłady kodu dla [Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) znajdują się w tym repozytorium w plikach `xx-python-agent-framework` i `xx-dotnet-agent-framework`.

## Zrozumienie Microsoft Agent Framework

![Framework Intro](../../../translated_images/pl/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://learn.microsoft.com/en-us/agent-framework/overview/?wt.mc_id=youtube_26688_organicsocial_reactor&pivots=programming-language-python) to zunifikowany framework Microsoftu do tworzenia agentów AI. Oferuje elastyczność do realizacji bardzo różnorodnych przypadków użycia agentów spotykanych w środowiskach produkcyjnych i badawczych, w tym:

- **Sekwencyjna orkiestracja agentów** w scenariuszach, gdzie potrzebne są krok po kroku przepływy pracy.
- **Równoczesna orkiestracja** w scenariuszach, gdzie agenci muszą wykonywać zadania jednocześnie.
- **Orkiestracja czatu grupowego** w scenariuszach, gdzie agenci mogą współpracować nad jednym zadaniem.
- **Orkiestracja przekazywania zadań** w scenariuszach, gdzie agenci przekazują zadania między sobą w miarę wykonywania podzadań.
- **Orkiestracja magnetyczna** w scenariuszach, gdzie agent zarządzający tworzy i modyfikuje listę zadań oraz koordynuje podagentów do ukończenia zadania.

Aby dostarczać agentów AI w środowisku produkcyjnym, MAF posiada także funkcje dla:

- **Obserwowalności** dzięki wykorzystaniu OpenTelemetry, gdzie każda akcja agenta AI, w tym wywołanie narzędzi, kroki orkiestracji, przepływy rozumowania oraz monitorowanie wydajności przez pulpity Microsoft Foundry, jest śledzona.
- **Bezpieczeństwa** poprzez uruchamianie agentów natywnie na Microsoft Foundry, który zawiera kontrolę dostępu opartą na rolach, obsługę danych prywatnych i wbudowane zabezpieczenia treści.
- **Trwałości** dzięki możliwości wstrzymywania, wznawiania i odzyskiwania wątków i przepływów pracy agenta, co umożliwia dłuższe procesy.
- **Kontroli** ponieważ wspierane są przepływy pracy z udziałem człowieka, gdzie zadania oznaczane są jako wymagające zatwierdzenia przez człowieka.

Microsoft Agent Framework skupia się również na interoperacyjności przez:

- **Bycie niezależnym od chmury** - Agenci mogą działać w kontenerach, lokalnie i w wielu różnych chmurach.
- **Bycie niezależnym od dostawcy** - Agenci mogą być tworzeni za pomocą preferowanego SDK, w tym Azure OpenAI i OpenAI
- **Integrację otwartych standardów** - Agenci mogą wykorzystywać protokoły takie jak Agent-to-Agent (A2A) i Model Context Protocol (MCP) do odnajdywania i używania innych agentów i narzędzi.
- **Wtyczki i konektory** - Można nawiązywać połączenia do usług danych i pamięci, takich jak Microsoft Fabric, SharePoint, Pinecone i Qdrant.

Przyjrzyjmy się, jak te funkcje są stosowane w podstawowych koncepcjach Microsoft Agent Framework.

## Kluczowe koncepcje Microsoft Agent Framework

### Agenci

![Agent Framework](../../../translated_images/pl/agent-components.410a06daf87b4fef.webp)

**Tworzenie Agentów**

Tworzenie agenta odbywa się przez zdefiniowanie usługi wnioskowania (dostawca LLM),  
zestawu instrukcji, które AI Agent ma wykonać, oraz przypisanej `name`:

```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Powyższy kod używa `Azure OpenAI`, ale agenci mogą być tworzeni z wykorzystaniem różnych usług, w tym `Microsoft Foundry Agent Service`:

```python
AzureAIAgentClient(async_credential=credential).create_agent( name="HelperAgent", instructions="You are a helpful assistant." ) as agent
```

OpenAI `Responses`, `ChatCompletion` API

```python
agent = OpenAIResponsesClient().create_agent( name="WeatherBot", instructions="You are a helpful weather assistant.", )
```

```python
agent = OpenAIChatClient().create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

lub [MiniMax](https://platform.minimaxi.com/), który udostępnia API kompatybilne z OpenAI z dużymi oknami kontekstowymi (do 204K tokenów):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

lub agentów zdalnych wykorzystujących protokół A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Uruchamianie Agentów**

Agenci są uruchamiani za pomocą metod `.run` lub `.run_stream` dla odpowiedzi bez strumieniowania lub ze strumieniowaniem.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Podczas uruchamiania agenta można także dostosować parametry takie jak `max_tokens` używane przez agenta, `tools`, do których agent ma dostęp, a nawet sam `model` używany przez agenta.

Jest to przydatne, gdy do realizacji zadania użytkownika potrzebne są konkretne modele lub narzędzia.

**Narzędzia**

Narzędzia mogą być definiowane zarówno podczas tworzenia agenta:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Podczas bezpośredniego tworzenia ChatAgent

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

jak również podczas uruchamiania agenta:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Narzędzie dostępne tylko dla tego uruchomienia )
```

**Wątki Agenta**

Wątki agenta służą do obsługi wielokrotnych tur konwersacji. Wątki mogą być tworzone przez:

- Użycie `get_new_thread()`, które pozwala na zapisywanie wątku na dłuższy czas
- Automatyczne tworzenie wątku podczas uruchamiania agenta, który trwa jedynie podczas bieżącego uruchomienia.

Tworzenie wątku wygląda tak:

```python
# Utwórz nowy wątek.
thread = agent.get_new_thread() # Uruchom agenta wraz z wątkiem.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Można następnie zserializować wątek, aby przechować go do późniejszego użycia:

```python
# Utwórz nowy wątek.
thread = agent.get_new_thread() 

# Uruchom agenta z wątkiem.

response = await agent.run("Hello, how are you?", thread=thread) 

# Zserializuj wątek do przechowywania.

serialized_thread = await thread.serialize() 

# Deserializuj stan wątku po załadowaniu z pamięci.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware Agenta**

Agenci współdziałają z narzędziami i LLM, aby realizować zadania użytkownika. W pewnych scenariuszach chcemy wykonywać lub śledzić działania pomiędzy tymi interakcjami. Middleware agenta pozwala to osiągnąć przez:

*Middleware funkcji*

To middleware pozwala wykonywać akcję między agentem a wywoływaną funkcją/narzędziem. Przykładem zastosowania jest logowanie wywołań funkcji.

W poniższym kodzie `next` określa, czy należy wywołać kolejne middleware, czy samą funkcję.

```python
async def logging_function_middleware(
    context: FunctionInvocationContext,
    next: Callable[[FunctionInvocationContext], Awaitable[None]],
) -> None:
    """Function middleware that logs function execution."""
    # Wstępne przetwarzanie: Zaloguj przed wykonaniem funkcji
    print(f"[Function] Calling {context.function.name}")

    # Kontynuuj do następnego middleware lub wykonania funkcji
    await next(context)

    # Późniejsze przetwarzanie: Zaloguj po wykonaniu funkcji
    print(f"[Function] {context.function.name} completed")
```

*Middleware czatu*

To middleware pozwala wykonywać lub logować akcje między agentem a zapytaniami kierowanymi do LLM.

Zawiera ono ważne informacje takie jak `messages` wysyłane do usługi AI.

```python
async def logging_chat_middleware(
    context: ChatContext,
    next: Callable[[ChatContext], Awaitable[None]],
) -> None:
    """Chat middleware that logs AI interactions."""
    # Wstępne przetwarzanie: Log przed wywołaniem AI
    print(f"[Chat] Sending {len(context.messages)} messages to AI")

    # Kontynuuj do następnego middleware lub usługi AI
    await next(context)

    # Przetwarzanie po: Log po otrzymaniu odpowiedzi AI
    print("[Chat] AI response received")

```

**Pamięć Agenta**

Jak omówiono w lekcji `Agentic Memory`, pamięć jest ważnym elementem umożliwiającym agentowi działanie w różnych kontekstach. MAF oferuje kilka różnych typów pamięci:

*Pamięć w Runtimie (In-Memory Storage)*

To pamięć przechowywana w wątkach podczas działania aplikacji.

```python
# Utwórz nowy wątek.
thread = agent.get_new_thread() # Uruchom agenta wraz z wątkiem.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Trwałe wiadomości (Persistent Messages)*

Ta pamięć jest używana do przechowywania historii rozmów między różnymi sesjami. Definiuje się ją przy użyciu `chat_message_store_factory`:

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

*Pamięć dynamiczna (Dynamic Memory)*

Ta pamięć dodawana jest do kontekstu przed uruchomieniem agentów. Może być przechowywana w zewnętrznych usługach jak mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Używanie Mem0 dla zaawansowanych możliwości pamięci
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

**Obserwowalność Agenta**

Obserwowalność jest ważna dla budowania niezawodnych i łatwych w utrzymaniu systemów agentowych. MAF integruje się z OpenTelemetry, oferując śledzenie (tracing) i mierniki dla lepszej obserwowalności.

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

### Przepływy pracy (Workflows)

MAF oferuje przepływy pracy, czyli predefiniowane kroki do ukończenia zadania, w których uczestniczą agenci AI jako komponenty.

Przepływy pracy składają się z różnych komponentów, które pozwalają na lepszą kontrolę przepływu. Umożliwiają też **orkiestrację wielu agentów** oraz **checkpointing**, czyli zapisywanie stanów przepływu pracy.

Podstawowe składniki przepływu pracy to:

**Executorzy (Executors)**

Executorzy odbierają wiadomości wejściowe, wykonują przypisane zadania i produkują komunikaty wyjściowe. To przesuwa przepływ pracy naprzód w stronę zakończenia większego zadania. Executorzy mogą być agentami AI lub logiką niestandardową.

**Krawędzie (Edges)**

Krawędzie definiują przepływ wiadomości w przepływie pracy. Mogą to być:

*Krawędzie bezpośrednie (Direct Edges)* - proste połączenia jeden-do-jednego między executorami:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Krawędzie warunkowe (Conditional Edges)* - aktywowane po spełnieniu określonego warunku. Na przykład, gdy pokoje w hotelu są niedostępne, executor może zasugerować inne opcje.

*Krawędzie typu switch-case* - kierują wiadomości do różnych executorów w zależności od zdefiniowanych warunków. Na przykład, jeśli klient podróży ma dostęp priorytetowy, jego zadania będą realizowane przez inny przepływ pracy.

*Krawędzie rozdzielające (Fan-out Edges)* - wysyłają jedną wiadomość do wielu odbiorców.

*Krawędzie scalające (Fan-in Edges)* - zbierają wiele wiadomości od różnych executorów i wysyłają do jednego odbiorcy.

**Zdarzenia (Events)**

Aby zapewnić lepszą obserwowalność przepływów pracy, MAF oferuje wbudowane zdarzenia wykonania, w tym:

- `WorkflowStartedEvent` - Rozpoczęcie wykonania przepływu pracy
- `WorkflowOutputEvent` - Przepływ pracy produkuje wynik
- `WorkflowErrorEvent` - Przepływ pracy napotkał błąd
- `ExecutorInvokeEvent` - Executor zaczyna przetwarzanie
- `ExecutorCompleteEvent` - Executor kończy przetwarzanie
- `RequestInfoEvent` - Zgłoszenie żądania

## Zaawansowane wzorce MAF

Powyższe sekcje dotyczą kluczowych koncepcji Microsoft Agent Framework. Budując bardziej złożonych agentów, zwróć uwagę na następujące zaawansowane wzorce:

- **Kompozycja middleware**: Łącz wiele handlerów middleware (logowanie, uwierzytelnianie, ograniczanie tempa) używając middleware funkcji i czatu, co pozwala precyzyjnie kontrolować zachowanie agenta.
- **Checkpointing przepływów pracy**: Użyj zdarzeń przepływu pracy i serializacji, aby zapisywać i wznawiać długotrwałe procesy agentów.
- **Dynamiczny wybór narzędzi**: Połącz RAG (retrieval-augmented generation) na opisach narzędzi z rejestracją narzędzi w MAF, aby prezentować tylko odpowiednie narzędzia dla zapytania.
- **Przekazywanie między agentami**: Użyj krawędzi przepływów pracy i warunkowego routingu do orkiestracji przekazań między wyspecjalizowanymi agentami.

## Hostowanie agentów LangChain / LangGraph na Microsoft Foundry

Microsoft Agent Framework jest **interoperacyjny względem frameworków** — nie jesteś ograniczony do agentów napisanych w MAF. Jeśli masz już agenta stworzonego w **LangChain** lub **LangGraph**, możesz uruchomić go jako **agenta hostowanego na Microsoft Foundry**, który zarządza czasem działania, sesjami, skalowaniem, tożsamością i punktami końcowymi protokołów, podczas gdy logika twojego agenta pozostaje w LangGraph.

Odbywa się to za pomocą pakietu `langchain_azure_ai.agents.hosting`, który udostępnia skompilowany graf LangGraph przez te same protokoły, których używają hostowani agenci Foundry.

**1. Zainstaluj hosting extra:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Pakiet `hosting` instaluje biblioteki protokołu Foundry: `azure-ai-agentserver-responses` (kompatybilny z OpenAI endpoint `/responses`) oraz `azure-ai-agentserver-invocations` (uniwersalny endpoint `/invocations`).

**2. Wybierz protokół hostingu:**

| Protokół | Klasa hosta | Punkt końcowy | Użyj gdy |
|----------|-------------|----------------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Chcesz kompatybilnego z OpenAI chatu, strumieniowania, historii odpowiedzi i wątków rozmów — zalecane domyślne rozwiązanie dla agentów konwersacyjnych. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Potrzebujesz niestandardowego formatu JSON, endpointu webhook albo przetwarzania niekonwersacyjnego. |

Ponieważ **API Responses jest głównym API dla tworzenia agentów w Foundry**, zacznij od `ResponsesHostServer` dla większości agentów.

**3. Skonfiguruj zmienne środowiskowe**  (`az login` najpierw, aby `DefaultAzureCredential` mogło się uwierzytelnić):

```bash
export FOUNDRY_PROJECT_ENDPOINT="https://<resource>.services.ai.azure.com/api/projects/<project>"
export FOUNDRY_MODEL_NAME="gpt-5-mini"
```

Gdy agent będzie później uruchamiany jako hostowany agent w Foundry, platforma automatycznie wstrzyknie `FOUNDRY_PROJECT_ENDPOINT`.

**4. Udostępnij agenta LangGraph przez protokół Responses:**

```python
import os

from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from langchain_azure_ai.agents.hosting import ResponsesHostServer

_AZURE_AI_SCOPE = "https://ai.azure.com/.default"


def build_chat_model() -> ChatOpenAI:
    project_endpoint = os.environ["FOUNDRY_PROJECT_ENDPOINT"].rstrip("/")
    deployment = os.environ.get("FOUNDRY_MODEL_NAME", "gpt-5-mini")
    credential = DefaultAzureCredential()
    project = AIProjectClient(endpoint=project_endpoint, credential=credential)
    openai_client = project.get_openai_client()
    token_provider = get_bearer_token_provider(credential, _AZURE_AI_SCOPE)

    # ChatOpenAI tutaj kieruje się do punktu końcowego zgodnego z OpenAI (Responses) projektu Foundry.
    return ChatOpenAI(
        model=deployment,
        base_url=str(openai_client.base_url),
        api_key=token_provider,
    )


def main() -> None:
    graph = create_agent(build_chat_model(), tools=[])
    port = int(os.environ.get("PORT", "8088"))
    ResponsesHostServer(graph).run(port=port)


if __name__ == "__main__":
    main()
```

Uruchom lokalnie za pomocą `python main.py`, następnie wyślij zapytanie Responses na `http://localhost:8088/responses`.

**Kluczowe zachowania:**

- **Rozmowy**: Klienci kontynuują rozmowę, przekazując `previous_response_id` lub identyfikator `conversation`. Jeśli twój graf jest skompilowany z użyciem LangGraph checkpointera, Foundry wiąże stan rozmowy z checkpointem (w środowisku produkcyjnym użyj trwałego checkpointera; `MemorySaver` jest dobry do testów lokalnych).
- **Człowiek w pętli**: Jeśli twój graf używa funkcji LangGraph `interrupt()`, `ResponsesHostServer` ujawnia oczekujące przerwanie jako element `function_call` / `mcp_approval_request` w Responses, a klienci wznawiają z odpowiedzią `function_call_output` / `mcp_approval_response`.
- **Wdrożenie w Foundry**: Użyj Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokalnie, wymaga Dockera), następnie `azd provision` i `azd deploy`. Wdrożenie agenta hostowanego wymaga roli **Foundry Project Manager**.

Wersja do uruchomienia tego przykładu znajduje się w [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Pełny przewodnik (protokół Invocations, niestandardowe schematy żądań i rozwiązywanie problemów) znajdziesz w [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Przykłady kodu 

Przykłady kodu dla Microsoft Agent Framework są dostępne w tym repozytorium w plikach `xx-python-agent-framework` i `xx-dotnet-agent-framework`.

## Masz więcej pytań o Microsoft Agent Framework?

Dołącz do [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), aby spotkać innych uczących się, uczestniczyć w godzinach konsultacji i uzyskać odpowiedzi na pytania dotyczące agentów AI.
## Poprzednia lekcja

[Pamięć dla agentów AI](../13-agent-memory/README.md)

## Następna lekcja

[Budowanie agentów do używania komputerów (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->