# Eksploracja Microsoft Agent Framework

![Agent Framework](../../../translated_images/pl/lesson-14-thumbnail.90df0065b9d234ee.webp)

### Wprowadzenie

Ten kurs obejmuje:

- Zrozumienie Microsoft Agent Framework: Kluczowe funkcje i wartość  
- Eksploracja kluczowych koncepcji Microsoft Agent Framework
- Zaawansowane wzorce MAF: Przepływy pracy, middleware i pamięć

## Cele nauki

Po ukończeniu tego kursu będziesz potrafił:

- Tworzyć gotowych do produkcji agentów AI za pomocą Microsoft Agent Framework
- Stosować główne funkcje Microsoft Agent Framework do swoich przypadków użycia agentów
- Wykorzystywać zaawansowane wzorce, w tym przepływy pracy, middleware i obserwowalność

## Przykłady kodu 

Przykłady kodu dla [Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) można znaleźć w tym repozytorium w plikach `xx-python-agent-framework` i `xx-dotnet-agent-framework`.

## Zrozumienie Microsoft Agent Framework

![Framework Intro](../../../translated_images/pl/framework-intro.077af16617cf130c.webp)

[Microsoft Agent Framework (MAF)](https://aka.ms/ai-agents-beginners/agent-framework) to zunifikowany framework Microsoftu do tworzenia agentów AI. Oferuje elastyczność pozwalającą sprostać szerokiemu zakresowi zastosowań agentów widzianych zarówno w środowiskach produkcyjnych, jak i badawczych, w tym:

- **Sekwencyjna orkiestracja agentów** w scenariuszach wymagających krok po kroku przepływów pracy.
- **Równoczesna orkiestracja** w scenariuszach, gdy agenci muszą wykonywać zadania jednocześnie.
- **Orkiestracja grupowego czatu** w scenariuszach, gdy agenci mogą współpracować nad jednym zadaniem.
- **Orkiestracja przekazania zadań** w scenariuszach, gdy agenci przekazują sobie zadania po ukończeniu podzadań.
- **Orkiestracja magnetyczna** w scenariuszach, gdzie agent kierujący tworzy i modyfikuje listę zadań oraz koordynuje podagentów do ich realizacji.

Aby dostarczać agentów AI na produkcję, MAF zawiera także funkcje:

- **Obserwowalności** dzięki zastosowaniu OpenTelemetry, gdzie każda akcja agenta AI, włącznie z wywołaniem narzędzi, krokami orkiestracji, przepływami logiki i monitorowaniem wydajności przez pulpity Microsoft Foundry, jest śledzona.
- **Bezpieczeństwa** przez uruchamianie agentów natywnie na Microsoft Foundry, które obejmuje kontrolę dostępu opartą na rolach, obsługę danych prywatnych i wbudowane zabezpieczenia treści.
- **Trwałości**, gdy wątki i przepływy pracy agentów mogą być wstrzymywane, wznawiane i odzyskiwać się z błędów, co umożliwia długotrwałe procesy.
- **Kontroli**, gdy obsługiwane są przepływy pracy z udziałem człowieka, gdzie zadania są oznaczane jako wymagające zatwierdzenia przez człowieka.

Microsoft Agent Framework jest również skoncentrowany na interoperacyjności poprzez:

- **Niezależność od chmury** - Agenci mogą działać w kontenerach, lokalnie i w różnych chmurach.
- **Niezależność od dostawcy** - Agenci mogą być tworzeni za pomocą preferowanego SDK, w tym Azure OpenAI i OpenAI.
- **Integrację standardów otwartych** - Agenci mogą wykorzystywać protokoły takie jak Agent-to-Agent (A2A) i Model Context Protocol (MCP), aby odnajdywać i korzystać z innych agentów i narzędzi.
- **Wtyczki i konektory** - Możliwe są połączenia z usługami danych i pamięci takimi jak Microsoft Fabric, SharePoint, Pinecone i Qdrant.

Spójrzmy, jak te funkcje są stosowane do niektórych kluczowych koncepcji Microsoft Agent Framework.

## Kluczowe koncepcje Microsoft Agent Framework

### Agenci

![Agent Framework](../../../translated_images/pl/agent-components.410a06daf87b4fef.webp)

**Tworzenie agentów**

Tworzenie agenta polega na zdefiniowaniu usługi inferencyjnej (dostawcy LLM), zestawu instrukcji dla agenta AI do wykonania oraz przypisanej `nazwy`:


```python
agent = AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent( instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender" )
```

Powyżej użyto `Azure OpenAI`, ale agentów można tworzyć za pomocą różnych usług, w tym `Microsoft Foundry Agent Service`:

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

lub [MiniMax](https://platform.minimaxi.com/), który zapewnia kompatybilne z OpenAI API z dużymi oknami kontekstowymi (do 204K tokenów):

```python
agent = OpenAIChatClient(base_url="https://api.minimax.io/v1", api_key=os.environ["MINIMAX_API_KEY"], model_id="MiniMax-M3").create_agent( name="HelpfulAssistant", instructions="You are a helpful assistant.", )
```

lub agentów zdalnych przy użyciu protokołu A2A:

```python
agent = A2AAgent( name=agent_card.name, description=agent_card.description, agent_card=agent_card, url="https://your-a2a-agent-host" )
```

**Uruchamianie agentów**

Agenci są uruchamiani przy użyciu metod `.run` lub `.run_stream` dla odpowiednio odpowiedzi nie strumieniowanych lub strumieniowanych.

```python
result = await agent.run("What are good places to visit in Amsterdam?")
print(result.text)
```

```python
async for update in agent.run_stream("What are the good places to visit in Amsterdam?"):
    if update.text:
        print(update.text, end="", flush=True)

```

Każde uruchomienie agenta może mieć również opcje dostosowania parametrów, takich jak `max_tokens` używane przez agenta, `tools`, które agent może wywoływać, a nawet `model` używany przez agenta.

Jest to przydatne w przypadkach, gdy do wykonania zadania użytkownika wymagane są konkretne modele lub narzędzia.

**Narzędzia**

Narzędzia można definiować zarówno podczas definiowania agenta:

```python
def get_attractions( location: Annotated[str, Field(description="The location to get the top tourist attractions for")], ) -> str: """Get the top tourist attractions for a given location.""" return f"The top attractions for {location} are." 


# Podczas bezpośredniego tworzenia ChatAgenta

agent = ChatAgent( chat_client=OpenAIChatClient(), instructions="You are a helpful assistant", tools=[get_attractions]

```

jak również podczas uruchamiania agenta:

```python

result1 = await agent.run( "What's the best place to visit in Seattle?", tools=[get_attractions] # Narzędzie dostępne tylko podczas tego uruchomienia )
```

**Wątki agenta**

Wątki agenta służą do obsługi rozmów wieloetapowych. Wątki można tworzyć na dwa sposoby:

- Używając `get_new_thread()`, co umożliwia zapisywanie wątku w czasie
- Tworząc wątek automatycznie podczas uruchamiania agenta, który trwa tylko podczas bieżącego uruchomienia.

Aby utworzyć wątek, kod wygląda następująco:

```python
# Utwórz nowy wątek.
thread = agent.get_new_thread() # Uruchom agenta z wątkiem.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)

```

Możesz następnie zserializować wątek, aby go przechować do późniejszego użycia:

```python
# Utwórz nowy wątek.
thread = agent.get_new_thread() 

# Uruchom agenta z wątkiem.

response = await agent.run("Hello, how are you?", thread=thread) 

# Serializuj wątek do przechowywania.

serialized_thread = await thread.serialize() 

# Deserializuj stan wątku po załadowaniu z przechowywania.

resumed_thread = await agent.deserialize_thread(serialized_thread)
```

**Middleware agenta**

Agenci współdziałają z narzędziami i LLM, aby realizować zadania użytkownika. W pewnych scenariuszach chcemy wykonać lub śledzić akcję pomiędzy tymi interakcjami. Middleware agenta umożliwia to poprzez:

*Middleware funkcji*

To middleware pozwala wykonać akcję między agentem a funkcją/narzędziem, które będzie wywoływać. Przykładem zastosowania jest rejestrowanie wywołania funkcji.

W poniższym kodzie `next` definiuje, czy wywołane zostanie następne middleware, czy właściwa funkcja.

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

    # Przetwarzanie po wykonaniu: Zaloguj po wykonaniu funkcji
    print(f"[Function] {context.function.name} completed")
```

*Middleware czatu*

To middleware pozwala wykonać lub zarejestrować akcję między agentem a żądaniami do LLM.

Zawiera ważne informacje takie jak `messages` wysyłane do usługi AI.

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

    # Przetwarzanie po: Log po odpowiedzi AI
    print("[Chat] AI response received")

```

**Pamięć agenta**

Jak omówiono w lekcji `Agentic Memory`, pamięć jest ważnym elementem umożliwiającym agentowi działanie w różnych kontekstach. MAF oferuje różne typy pamięci:

*Pamięć w pamięci operacyjnej*

To pamięć przechowywana w wątkach podczas działania aplikacji.

```python
# Utwórz nowy wątek.
thread = agent.get_new_thread() # Uruchom agenta z wątkiem.
response = await agent.run("Hello, I am here to help you book travel. Where would you like to go?", thread=thread)
```

*Wiadomości trwałe*

Ta pamięć służy do przechowywania historii konwersacji między różnymi sesjami. Definiowana jest przy użyciu `chat_message_store_factory`:

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

Ta pamięć jest dodawana do kontekstu przed uruchomieniem agentów. Może być przechowywana w zewnętrznych usługach takich jak mem0:

```python
from agent_framework.mem0 import Mem0Provider

# Używanie Mem0 do zaawansowanych możliwości pamięci
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

Obserwowalność jest ważna dla tworzenia niezawodnych i łatwych w utrzymaniu systemów agentów. MAF integruje się z OpenTelemetry, oferując śledzenie i mierniki dla lepszej obserwowalności.

```python
from agent_framework.observability import get_tracer, get_meter

tracer = get_tracer()
meter = get_meter()
with tracer.start_as_current_span("my_custom_span"):
    # zrobić coś
    pass
counter = meter.create_counter("my_custom_counter")
counter.add(1, {"key": "value"})
```

### Przepływy pracy

MAF oferuje przepływy pracy, które są predefiniowanymi krokami do realizacji zadania i zawierają agentów AI jako komponenty tych kroków.

Przepływy pracy składają się z różnych komponentów umożliwiających lepszą kontrolę przepływu. Umożliwiają również **orkiestrację wieloagentową** oraz **zapisywanie stanu** (checkpointing) dla zapisywania stanów przepływu.

Kluczowe komponenty przepływu pracy to:

**Egzekutorzy**

Egzekutorzy otrzymują wiadomości wejściowe, wykonują przypisane im zadania, a następnie generują wiadomości wyjściowe. To przesuwa przepływ pracy do przodu w kierunku ukończenia większego zadania. Egzekutorami mogą być agenci AI lub niestandardowa logika.

**Krawędzie**

Krawędzie służą do definiowania przepływu wiadomości w przepływie pracy. Mogą to być:

*Krawędzie bezpośrednie* - proste połączenia jeden-do-jednego między egzekutorami:

```python
from agent_framework import WorkflowBuilder

builder = WorkflowBuilder()
builder.add_edge(source_executor, target_executor)
builder.set_start_executor(source_executor)
workflow = builder.build()
```

*Krawędzie warunkowe* - aktywowane po spełnieniu określonych warunków. Na przykład, gdy pokoje hotelowe są niedostępne, egzekutor może zasugerować inne opcje.

*Krawędzie typu switch-case* - kierują wiadomości do różnych egzekutorów na podstawie zdefiniowanych warunków. Na przykład, jeśli klient podróżny ma dostęp priorytetowy, jego zadania będą obsługiwane przez inny przepływ.

*Krawędzie rozdzielające (fan-out)* - wysyłają jedną wiadomość do wielu odbiorców.

*Krawędzie zbierające (fan-in)* - zbierają wiele wiadomości od różnych egzekutorów i wysyłają je do jednego odbiorcy.

**Zdarzenia**

Dla lepszej obserwowalności przepływów pracy, MAF oferuje wbudowane zdarzenia wykonania, takie jak:

- `WorkflowStartedEvent`  - Rozpoczęcie wykonywania przepływu pracy
- `WorkflowOutputEvent` - Przepływ pracy generuje wynik
- `WorkflowErrorEvent` - Przepływ pracy napotkał błąd
- `ExecutorInvokeEvent`  - Egzekutor rozpoczyna przetwarzanie
- `ExecutorCompleteEvent`  -  Egzekutor kończy przetwarzanie
- `RequestInfoEvent` - Żądanie zostało złożone

## Zaawansowane wzorce MAF

Powyższe sekcje omawiają kluczowe koncepcje Microsoft Agent Framework. Budując bardziej złożonych agentów, warto rozważyć następujące zaawansowane wzorce:

- **Kompozycja middleware**: Łączenie wielu handlerów middleware (logowanie, uwierzytelnianie, ograniczanie zapytań) korzystając z middleware funkcji i czatu dla precyzyjnej kontroli zachowania agenta.
- **Checkpointing przepływów pracy**: Używanie zdarzeń przepływów i serializacji do zapisywania i wznawiania długotrwałych procesów agenta.
- **Dynamiczny wybór narzędzi**: Łączenie RAG (Retrieval-Augmented Generation) na opisach narzędzi z rejestracją narzędzi w MAF, aby prezentować tylko relewantne narzędzia dla zapytania.
- **Przekazywanie między agentami**: Korzystanie z krawędzi przepływów i warunkowego rutingu do orkiestracji przekazań między agentami specjalistycznymi.

## Hosting agentów LangChain / LangGraph na Microsoft Foundry

Microsoft Agent Framework jest **interoperacyjny w ramach różnych frameworków** — nie jesteś ograniczony do agentów napisanych w MAF. Jeśli masz już agenta zbudowanego z użyciem **LangChain** lub **LangGraph**, możesz go uruchomić jako **agenta hostowanego w Microsoft Foundry**, dzięki czemu Foundry zarządza środowiskiem uruchomieniowym, sesjami, skalowaniem, tożsamością i punktami końcowymi protokołu, podczas gdy logika agenta pozostaje w LangGraph.

Odbywa się to przy użyciu pakietu `langchain_azure_ai.agents.hosting`, który udostępnia skompilowany wykres LangGraph na tych samych protokołach, które wykorzystują agenci hostowani w Foundry.

**1. Zainstaluj dodatkowe zależności hostingu:**

```bash
pip install -U "langchain-azure-ai[hosting]>=1.2.4" azure-identity
```

Dodatkowa zależność `hosting` instaluje biblioteki protokołów Foundry: `azure-ai-agentserver-responses` (kompatybilny z OpenAI endpoint `/responses`) oraz `azure-ai-agentserver-invocations` (ogólny endpoint `/invocations`).

**2. Wybierz protokół hostingu:**

| Protokół | Klasa hosta | Punkt końcowy | Używany gdy |
|----------|-----------|----------|----------|
| **Responses** | `ResponsesHostServer` | `/responses` | Chcesz kompatybilnego z OpenAI czatu, strumieniowanych odpowiedzi, historii odpowiedzi oraz wątkowania konwersacji — zalecany domyślny dla agentów konwersacyjnych. |
| **Invocations** | `InvocationsHostServer` | `/invocations` | Potrzebujesz niestandardowego formatu JSON, endpointu typu webhook lub przetwarzania niekonwersacyjnego. |

Ponieważ **API Responses to główne API dla rozwoju agentów w Foundry**, zacznij od `ResponsesHostServer` dla większości agentów.

**3. Skonfiguruj zmienne środowiskowe** (najpierw `az login`, aby `DefaultAzureCredential` mógł się uwierzytelnić):

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

    # ChatOpenAI tutaj celuje w punkt końcowy zgodny z OpenAI (Responses) projektu Foundry.
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

Uruchom lokalnie poleceniem `python main.py`, a następnie wyślij zapytanie Responses do `http://localhost:8088/responses`.

**Kluczowe zachowania:**

- **Konwersacje**: Klienci kontynuują rozmowę, przekazując `previous_response_id` lub identyfikator `conversation`. Jeśli twój wykres jest skompilowany z użyciem LangGraph checkpointera, Foundry powiązuje stan konwersacji z checkpointem (w produkcji używaj trwałego checkpointera; `MemorySaver` jest wystarczający do testów lokalnych).
- **Człowiek w pętli**: Jeśli wykres używa LangGraph `interrupt()`, `ResponsesHostServer` ujawnia oczekujące przerwanie jako pozycję `function_call` / `mcp_approval_request` w Responses, a klienci wznawiają z pasującą odpowiedzią `function_call_output` / `mcp_approval_response`.
- **Wdrażanie do Foundry**: Użyj Azure Developer CLI — `azd ext install azure.ai.agents`, `azd ai agent init -m <manifest>`, `azd ai agent run` (lokalne, wymaga Dockera), następnie `azd provision` i `azd deploy`. Wdrażanie agenta hostowanego wymaga roli **Foundry Project Manager**.

Wersja działająca tego przykładu znajduje się w [code-samples/14-langchain-hosted-agent.py](../../../14-microsoft-agent-framework/code-samples/14-langchain-hosted-agent.py). Pełny przewodnik (protokół Invocations, niestandardowe schematy żądań oraz rozwiązywanie problemów) można znaleźć w [Host LangGraph agents as Foundry hosted agents](https://learn.microsoft.com/azure/foundry/how-to/develop/langchain-hosted-agents).

## Przykłady kodu 

Przykłady kodu dla Microsoft Agent Framework można znaleźć w tym repozytorium w plikach `xx-python-agent-framework` i `xx-dotnet-agent-framework`.

## Masz więcej pytań dotyczących Microsoft Agent Framework?

Dołącz do [Microsoft Foundry Discord](https://discord.com/invite/ATgtXmAS5D), aby spotkać się z innymi uczącymi się, brać udział w godzinach konsultacji i uzyskać odpowiedzi na pytania dotyczące agentów AI.
## Poprzednia lekcja

[Pamięć dla agentów AI](../13-agent-memory/README.md)

## Następna lekcja

[Budowanie agentów do korzystania z komputera (CUA)](../15-browser-use/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Choć dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w jego języku źródłowym należy uznawać za autorytatywne źródło. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->