<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5cc6836626047aa055e8960c8484a7d0",
  "translation_date": "2025-08-30T14:48:16+00:00",
  "source_file": "11-agentic-protocols/code_samples/mcp-agents/README.md",
  "language_code": "pl"
}
-->
# Budowanie Systemów Komunikacji Agent-Do-Agenta z MCP

> TL;DR - Czy można zbudować komunikację Agent2Agent na MCP? Tak!

MCP znacznie ewoluował poza swoje pierwotne założenie "dostarczania kontekstu dla LLM". Dzięki ostatnim ulepszeniom, takim jak [wznawialne strumienie](https://modelcontextprotocol.io/docs/concepts/transports#resumability-and-redelivery), [elicitation](https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation), [sampling](https://modelcontextprotocol.io/specification/2025-06-18/client/sampling) oraz powiadomienia ([postęp](https://modelcontextprotocol.io/specification/2025-06-18/basic/utilities/progress) i [zasoby](https://modelcontextprotocol.io/specification/2025-06-18/schema#resourceupdatednotification)), MCP oferuje teraz solidną podstawę do budowy złożonych systemów komunikacji agent-do-agenta.

## Nieporozumienie dotyczące Agenta/Narzędzia

W miarę jak coraz więcej deweloperów bada narzędzia z zachowaniami agentowymi (działające przez dłuższy czas, wymagające dodatkowych danych wejściowych w trakcie działania itp.), pojawia się powszechne nieporozumienie, że MCP nie nadaje się do tego celu, głównie dlatego, że wczesne przykłady jego prymitywnego narzędzia koncentrowały się na prostych wzorcach żądanie-odpowiedź.

To postrzeganie jest już nieaktualne. Specyfikacja MCP została znacznie ulepszona w ciągu ostatnich kilku miesięcy, wprowadzając funkcje umożliwiające budowę długotrwałych zachowań agentowych:

- **Strumieniowanie i wyniki częściowe**: Aktualizacje postępu w czasie rzeczywistym podczas wykonywania
- **Wznawialność**: Klienci mogą ponownie połączyć się i kontynuować po rozłączeniu
- **Trwałość**: Wyniki przetrwają restart serwera (np. za pomocą linków do zasobów)
- **Wielotur**: Interaktywne dane wejściowe w trakcie wykonywania dzięki elicitation i sampling

Te funkcje można łączyć, aby umożliwić złożone aplikacje agentowe i multi-agentowe, wszystkie wdrożone w protokole MCP.

Dla odniesienia, będziemy nazywać agenta "narzędziem" dostępnym na serwerze MCP. Oznacza to istnienie aplikacji hosta, która implementuje klienta MCP, nawiązuje sesję z serwerem MCP i może wywoływać agenta.

## Co sprawia, że narzędzie MCP jest "agentowe"?

Zanim przejdziemy do implementacji, ustalmy, jakie możliwości infrastrukturalne są potrzebne do obsługi długotrwałych agentów.

> Zdefiniujemy agenta jako jednostkę, która może działać autonomicznie przez dłuższy czas, zdolną do obsługi złożonych zadań wymagających wielu interakcji lub dostosowań na podstawie informacji zwrotnych w czasie rzeczywistym.

### 1. Strumieniowanie i wyniki częściowe

Tradycyjne wzorce żądanie-odpowiedź nie sprawdzają się w przypadku długotrwałych zadań. Agenci muszą dostarczać:

- Aktualizacje postępu w czasie rzeczywistym
- Wyniki pośrednie

**Wsparcie MCP**: Powiadomienia o aktualizacji zasobów umożliwiają strumieniowanie wyników częściowych, choć wymaga to starannego projektowania, aby uniknąć konfliktów z modelem 1:1 żądanie/odpowiedź JSON-RPC.

| Funkcja                    | Przypadek użycia                                                                                                                                                                       | Wsparcie MCP                                                                                |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Aktualizacje postępu w czasie rzeczywistym | Użytkownik żąda zadania migracji kodu. Agent strumieniuje postęp: "10% - Analiza zależności... 25% - Konwersja plików TypeScript... 50% - Aktualizacja importów..."          | ✅ Powiadomienia o postępie                                                                  |
| Wyniki częściowe            | Zadanie "Generuj książkę" strumieniuje wyniki częściowe, np. 1) Zarys fabuły, 2) Lista rozdziałów, 3) Każdy ukończony rozdział. Host może sprawdzić, anulować lub przekierować na każdym etapie. | ✅ Powiadomienia mogą być "rozszerzone", aby zawierać wyniki częściowe, patrz propozycje PR 383, 776 |

<div align="center" style="font-style: italic; font-size: 0.95em; margin-bottom: 0.5em;">
<strong>Rysunek 1:</strong> Diagram ilustruje, jak agent MCP strumieniuje aktualizacje postępu w czasie rzeczywistym i wyniki częściowe do aplikacji hosta podczas długotrwałego zadania, umożliwiając użytkownikowi monitorowanie wykonania w czasie rzeczywistym.
</div>

```mermaid
sequenceDiagram
    participant User
    participant Host as Host App<br/>(MCP Client)
    participant Server as MCP Server<br/>(Agent Tool)

    User->>Host: Start long task
    Host->>Server: Call agent_tool()

    loop Progress Updates
        Server-->>Host: Progress + partial results
        Host-->>User: Stream updates
    end

    Server-->>Host: ✅ Final result
    Host-->>User: Complete
```

### 2. Wznawialność

Agenci muszą obsługiwać przerwy w sieci w sposób płynny:

- Ponowne połączenie po rozłączeniu (klienta)
- Kontynuacja od miejsca, w którym przerwano (ponowne dostarczenie wiadomości)

**Wsparcie MCP**: Transport StreamableHTTP MCP obsługuje dziś wznawianie sesji i ponowne dostarczanie wiadomości za pomocą identyfikatorów sesji i ostatnich identyfikatorów zdarzeń. Ważne jest, aby serwer implementował EventStore, który umożliwia odtwarzanie zdarzeń po ponownym połączeniu klienta.  
Warto zauważyć, że istnieje propozycja społeczności (PR #975), która bada transport niezależny od strumieni wznawialnych.

| Funkcja      | Przypadek użycia                                                                                                                                                   | Wsparcie MCP                                                                |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------- |
| Wznawialność | Klient rozłącza się podczas długotrwałego zadania. Po ponownym połączeniu sesja jest wznawiana z odtworzeniem pominiętych zdarzeń, kontynuując płynnie od miejsca przerwania. | ✅ Transport StreamableHTTP z identyfikatorami sesji, odtwarzaniem zdarzeń i EventStore |

<div align="center" style="font-style: italic; font-size: 0.95em; margin-bottom: 0.5em;">
<strong>Rysunek 2:</strong> Diagram pokazuje, jak transport StreamableHTTP MCP i EventStore umożliwiają płynne wznawianie sesji: jeśli klient rozłączy się, może ponownie połączyć się i odtworzyć pominięte zdarzenia, kontynuując zadanie bez utraty postępu.
</div>

```mermaid
sequenceDiagram
    participant User
    participant Host as Host App<br/>(MCP Client)
    participant Server as MCP Server<br/>(Agent Tool)
    participant Store as Event Store

    User->>Host: Start task
    Host->>Server: Call tool [session: abc123]
    Server->>Store: Save events

    Note over Host,Server: 💥 Connection lost

    Host->>Server: Reconnect [session: abc123]
    Store-->>Server: Replay events
    Server-->>Host: Catch up + continue
    Host-->>User: ✅ Complete
```

### 3. Trwałość

Długotrwałe agenty potrzebują trwałego stanu:

- Wyniki przetrwają restart serwera
- Status można pobrać poza sesją
- Śledzenie postępu między sesjami

**Wsparcie MCP**: MCP obsługuje teraz typ zwracania linku do zasobu dla wywołań narzędzi. Obecnie możliwym wzorcem jest zaprojektowanie narzędzia, które tworzy zasób i natychmiast zwraca link do zasobu. Narzędzie może kontynuować realizację zadania w tle i aktualizować zasób. Z kolei klient może wybrać sprawdzanie stanu tego zasobu, aby uzyskać wyniki częściowe lub pełne (na podstawie aktualizacji zasobów dostarczanych przez serwer) lub subskrybować zasób, aby otrzymywać powiadomienia o aktualizacjach.

Jednym z ograniczeń jest to, że sprawdzanie zasobów lub subskrybowanie aktualizacji może zużywać zasoby, co ma implikacje w skali. Istnieje otwarta propozycja społeczności (w tym #992), która bada możliwość wprowadzenia webhooków lub wyzwalaczy, które serwer może wywoływać, aby powiadomić klienta/aplikację hosta o aktualizacjach.

| Funkcja    | Przypadek użycia                                                                                                                                        | Wsparcie MCP                                                        |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Trwałość | Serwer ulega awarii podczas zadania migracji danych. Wyniki i postęp przetrwają restart, klient może sprawdzić status i kontynuować z trwałego zasobu. | ✅ Linki do zasobów z trwałym przechowywaniem i powiadomieniami o statusie |

Obecnie powszechnym wzorcem jest zaprojektowanie narzędzia, które tworzy zasób i natychmiast zwraca link do zasobu. Narzędzie może w tle realizować zadanie, wydawać powiadomienia o zasobach, które służą jako aktualizacje postępu lub zawierać wyniki częściowe, i aktualizować zawartość w zasobie w razie potrzeby.

<div align="center" style="font-style: italic; font-size: 0.95em; margin-bottom: 0.5em;">
<strong>Rysunek 3:</strong> Diagram pokazuje, jak agenci MCP wykorzystują trwałe zasoby i powiadomienia o statusie, aby zapewnić, że długotrwałe zadania przetrwają restart serwera, umożliwiając klientom sprawdzanie postępu i pobieranie wyników nawet po awariach.
</div>

```mermaid
sequenceDiagram
    participant User
    participant Host as Host App<br/>(MCP Client)
    participant Server as MCP Server<br/>(Agent Tool)
    participant DB as Persistent Storage

    User->>Host: Start task
    Host->>Server: Call tool
    Server->>DB: Create resource + updates
    Server-->>Host: 🔗 Resource link

    Note over Server: 💥 Server restart

    User->>Host: Check status
    Host->>Server: Get resource
    Server->>DB: Load state
    Server-->>Host: Current progress
    Server->>DB: Complete + notify
    Host-->>User: ✅ Complete
```

### 4. Interakcje wielotur

Agenci często potrzebują dodatkowych danych wejściowych w trakcie wykonywania:

- Wyjaśnienia lub zatwierdzenia od człowieka
- Pomocy AI przy złożonych decyzjach
- Dynamicznej regulacji parametrów

**Wsparcie MCP**: W pełni obsługiwane dzięki sampling (dla danych wejściowych AI) i elicitation (dla danych wejściowych od człowieka).

| Funkcja                 | Przypadek użycia                                                                                                                                     | Wsparcie MCP                                           |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| Interakcje wielotur | Agent rezerwacji podróży prosi o potwierdzenie ceny od użytkownika, a następnie prosi AI o podsumowanie danych podróży przed zakończeniem transakcji rezerwacji. | ✅ Elicitation dla danych wejściowych od człowieka, sampling dla danych wejściowych AI |

<div align="center" style="font-style: italic; font-size: 0.95em; margin-bottom: 0.5em;">
<strong>Rysunek 4:</strong> Diagram przedstawia, jak agenci MCP mogą interaktywnie uzyskiwać dane wejściowe od człowieka lub prosić o pomoc AI w trakcie wykonywania, wspierając złożone, wieloturowe przepływy pracy, takie jak potwierdzenia i dynamiczne podejmowanie decyzji.
</div>

```mermaid
sequenceDiagram
    participant User
    participant Host as Host App<br/>(MCP Client)
    participant Server as MCP Server<br/>(Agent Tool)

    User->>Host: Book flight
    Host->>Server: Call travel_agent

    Server->>Host: Elicitation: "Confirm $500?"
    Note over Host: Elicitation callback (if available)
    Host->>User: 💰 Confirm price?
    User->>Host: "Yes"
    Host->>Server: Confirmed

    Server->>Host: Sampling: "Summarize data"
    Note over Host: AI callback (if available)
    Host->>Server: Report summary

    Server->>Host: ✅ Flight booked
```

## Implementacja długotrwałych agentów na MCP - Przegląd kodu

W ramach tego artykułu udostępniamy [repozytorium kodu](https://github.com/victordibia/ai-tutorials/tree/main/MCP%20Agents), które zawiera kompletną implementację długotrwałych agentów przy użyciu MCP Python SDK z transportem StreamableHTTP dla wznawiania sesji i ponownego dostarczania wiadomości. Implementacja pokazuje, jak możliwości MCP mogą być łączone, aby umożliwić zaawansowane zachowania agentowe.

W szczególności implementujemy serwer z dwoma głównymi narzędziami agentowymi:

- **Agent podróży** - Symuluje usługę rezerwacji podróży z potwierdzeniem ceny za pomocą elicitation
- **Agent badawczy** - Wykonuje zadania badawcze z podsumowaniami wspomaganymi przez AI za pomocą sampling

Oba agenty demonstrują aktualizacje postępu w czasie rzeczywistym, interaktywne potwierdzenia i pełne możliwości wznawiania sesji.

### Kluczowe koncepcje implementacji

Poniższe sekcje pokazują implementację po stronie serwera dla agentów oraz obsługę po stronie hosta dla każdej funkcji:

#### Strumieniowanie i aktualizacje postępu - Status zadania w czasie rzeczywistym

Strumieniowanie umożliwia agentom dostarczanie aktualizacji postępu w czasie rzeczywistym podczas długotrwałych zadań, informując użytkowników o statusie zadania i wynikach pośrednich.

**Implementacja serwera (agent wysyła powiadomienia o postępie):**

```python
# From server/server.py - Travel agent sending progress updates
for i, step in enumerate(steps):
    await ctx.session.send_progress_notification(
        progress_token=ctx.request_id,
        progress=i * 25,
        total=100,
        message=step,
        related_request_id=str(ctx.request_id)
    )
    await anyio.sleep(2)  # Simulate work

# Alternative: Log messages for detailed step-by-step updates
await ctx.session.send_log_message(
    level="info",
    data=f"Processing step {current_step}/{steps} ({progress_percent}%)",
    logger="long_running_agent",
    related_request_id=ctx.request_id,
)
```

**Implementacja klienta (host odbiera aktualizacje postępu):**

```python
# From client/client.py - Client handling real-time notifications
async def message_handler(message) -> None:
    if isinstance(message, types.ServerNotification):
        if isinstance(message.root, types.LoggingMessageNotification):
            console.print(f"📡 [dim]{message.root.params.data}[/dim]")
        elif isinstance(message.root, types.ProgressNotification):
            progress = message.root.params
            console.print(f"🔄 [yellow]{progress.message} ({progress.progress}/{progress.total})[/yellow]")

# Register message handler when creating session
async with ClientSession(
    read_stream, write_stream,
    message_handler=message_handler
) as session:
```

#### Elicitation - Żądanie danych wejściowych od użytkownika

Elicitation umożliwia agentom żądanie danych wejściowych od użytkownika w trakcie wykonywania. Jest to niezbędne do potwierdzeń, wyjaśnień lub zatwierdzeń podczas długotrwałych zadań.

**Implementacja serwera (agent żąda potwierdzenia):**

```python
# From server/server.py - Travel agent requesting price confirmation
elicit_result = await ctx.session.elicit(
    message=f"Please confirm the estimated price of $1200 for your trip to {destination}",
    requestedSchema=PriceConfirmationSchema.model_json_schema(),
    related_request_id=ctx.request_id,
)

if elicit_result and elicit_result.action == "accept":
    # Continue with booking
    logger.info(f"User confirmed price: {elicit_result.content}")
elif elicit_result and elicit_result.action == "decline":
    # Cancel the booking
    booking_cancelled = True
```

**Implementacja klienta (host dostarcza callback elicitation):**

```python
# From client/client.py - Client handling elicitation requests
async def elicitation_callback(context, params):
    console.print(f"💬 Server is asking for confirmation:")
    console.print(f"   {params.message}")

    response = console.input("Do you accept? (y/n): ").strip().lower()

    if response in ['y', 'yes']:
        return types.ElicitResult(
            action="accept",
            content={"confirm": True, "notes": "Confirmed by user"}
        )
    else:
        return types.ElicitResult(
            action="decline",
            content={"confirm": False, "notes": "Declined by user"}
        )

# Register the callback when creating the session
async with ClientSession(
    read_stream, write_stream,
    elicitation_callback=elicitation_callback
) as session:
```

#### Sampling - Żądanie pomocy AI

Sampling pozwala agentom żądać pomocy LLM przy złożonych decyzjach lub generowaniu treści w trakcie wykonywania. Umożliwia to hybrydowe przepływy pracy człowiek-AI.

**Implementacja serwera (agent żąda pomocy AI):**

```python
# From server/server.py - Research agent requesting AI summary
sampling_result = await ctx.session.create_message(
    messages=[
        SamplingMessage(
            role="user",
            content=TextContent(type="text", text=f"Please summarize the key findings for research on: {topic}")
        )
    ],
    max_tokens=100,
    related_request_id=ctx.request_id,
)

if sampling_result and sampling_result.content:
    if sampling_result.content.type == "text":
        sampling_summary = sampling_result.content.text
        logger.info(f"Received sampling summary: {sampling_summary}")
```

**Implementacja klienta (host dostarcza callback sampling):**

```python
# From client/client.py - Client handling sampling requests
async def sampling_callback(context, params):
    message_text = params.messages[0].content.text if params.messages else 'No message'
    console.print(f"🧠 Server requested sampling: {message_text}")

    # In a real application, this could call an LLM API
    # For demo purposes, we provide a mock response
    mock_response = "Based on current research, MCP has evolved significantly..."

    return types.CreateMessageResult(
        role="assistant",
        content=types.TextContent(type="text", text=mock_response),
        model="interactive-client",
        stopReason="endTurn"
    )

# Register the callback when creating the session
async with ClientSession(
    read_stream, write_stream,
    sampling_callback=sampling_callback,
    elicitation_callback=elicitation_callback
) as session:
```

#### Wznawialność - Ciągłość sesji po rozłączeniach

Wznawialność zapewnia, że długotrwałe zadania agentów mogą przetrwać rozłączenia klienta i kontynuować płynnie po ponownym połączeniu. Jest to realizowane za pomocą magazynów zdarzeń i tokenów wznawiania.

**Implementacja magazynu zdarzeń (serwer przechowuje stan sesji):**

```python
# From server/event_store.py - Simple in-memory event store
class SimpleEventStore(EventStore):
    def __init__(self):
        self._events: list[tuple[StreamId, EventId, JSONRPCMessage]] = []
        self._event_id_counter = 0

    async def store_event(self, stream_id: StreamId, message: JSONRPCMessage) -> EventId:
        """Store an event and return its ID."""
        self._event_id_counter += 1
        event_id = str(self._event_id_counter)
        self._events.append((stream_id, event_id, message))
        return event_id

    async def replay_events_after(self, last_event_id: EventId, send_callback: EventCallback) -> StreamId | None:
        """Replay events after the specified ID for resumption."""
        # Find events after the last known event and replay them
        for _, event_id, message in self._events[start_index:]:
            await send_callback(EventMessage(message, event_id))

# From server/server.py - Passing event store to session manager
def create_server_app(event_store: Optional[EventStore] = None) -> Starlette:
    server = ResumableServer()

    # Create session manager with event store for resumption
    session_manager = StreamableHTTPSessionManager(
        app=server,
        event_store=event_store,  # Event store enables session resumption
        json_response=False,
        security_settings=security_settings,
    )

    return Starlette(routes=[Mount("/mcp", app=session_manager.handle_request)])

# Usage: Initialize with event store
event_store = SimpleEventStore()
app = create_server_app(event_store)
```

**Metadane klienta z tokenem wznawiania (klient ponownie łączy się, używając przechowywanego stanu):**

```python
# From client/client.py - Client resumption with metadata
if existing_tokens and existing_tokens.get("resumption_token"):
    # Use existing resumption token to continue where we left off
    metadata = ClientMessageMetadata(
        resumption_token=existing_tokens["resumption_token"],
    )
else:
    # Create callback to save resumption token when received
    def enhanced_callback(token: str):
        protocol_version = getattr(session, 'protocol_version', None)
        token_manager.save_tokens(session_id, token, protocol_version, command, args)

    metadata = ClientMessageMetadata(
        on_resumption_token_update=enhanced_callback,
    )

# Send request with resumption metadata
result = await session.send_request(
    types.ClientRequest(
        types.CallToolRequest(
            method="tools/call",
            params=types.CallToolRequestParams(name=command, arguments=args)
        )
    ),
    types.CallToolResult,
    metadata=metadata,
)
```

Aplikacja hosta przechowuje lokalnie identyfikatory sesji i tokeny wznawiania, umożliwiając jej ponowne połączenie z istniejącymi sesjami bez utraty postępu lub stanu.

### Organizacja kodu

<div align="center" style="font-style: italic; font-size: 0.95em; margin-bottom: 0.5em;">
<strong>Rysunek 5:</strong> Architektura systemu agentów opartego na MCP
</div>

```mermaid
graph LR
    User([User]) -->|"Task"| Host["Host<br/>(MCP Client)"]
    Host -->|list tools| Server[MCP Server]
    Server -->|Exposes| AgentsTools[Agents as Tools]
    AgentsTools -->|Task| AgentA[Travel Agent]
    AgentsTools -->|Task| AgentB[Research Agent]

    Host -->|Monitors| StateUpdates[Progress & State Updates]
    Server -->|Publishes| StateUpdates

    class User user;
    class AgentA,AgentB agent;
    class Host,Server,StateUpdates core;
```

**Kluczowe pliki:**

- **`server/server.py`** - Resumowalny serwer MCP z agentami podróży i badawczymi, demonstrujący elicitation, sampling i aktualizacje postępu
- **`client/client.py`** - Interaktywna aplikacja hosta z obsługą wznawiania, handlerami callback i zarządzaniem tokenami
- **`server/event_store.py`** - Implementacja magazynu zdarzeń umożliwiająca wznawianie sesji i ponowne dostarczanie wiadomości

## Rozszerzenie na komunikację multi-agentową na MCP

Powyższa implementacja może zostać rozszerzona na systemy multi-agentowe poprzez zwiększenie inteligencji i zakresu aplikacji hosta:

- **Inteligentna dekompozycja zadań**: Host analizuje złożone żądania użytkownika i dzieli je na podzadania dla różnych wyspecjalizowanych agentów
- **Koordynacja multi-serwerowa**: Host utrzymuje połączenia z wieloma serwerami MCP, z których każdy udostępnia różne możliwości agentów
- **Zarządzanie stanem zadań**: Host śledzi postęp w wielu równoczesnych zadaniach agentów, obsługując zależności i sekwencjonowanie
- **Odporność i ponowne próby**: Host zarządza awariami, implementuje logikę ponownych prób i przekierowuje zadania, gdy agenci stają się niedostępni
- **Synteza wyników**: Host łączy wyniki od wielu agentów w spójne końcowe rezultaty

Host ewoluuje z prostego klienta do inteligentnego orkiestratora, koordynując rozproszone możliwości agentów przy zachowaniu tej samej podstawy protokołu MCP.

## Podsumowanie

Ulepszone możliwości MCP - powiadomienia o zasobach, elicitation/sampling, wznawialne strumienie i trwałe zasoby - umożliwiają złożone interakcje agent-do-agenta przy zachowaniu prostoty protokołu.

## Pierwsze kroki

Gotowy, aby zbudować własny system agent2agent? Wykonaj następujące kroki:

### 1. Uruchom demo

```bash
# Start the server with event store for resumption
python -m server.server --port 8006

# In another terminal, run the interactive client
python -m client.client --url http://127.0.0.1:8006/mcp
```

**Dostępne polecenia w trybie interaktywnym:**

- `travel_agent` - Rezerwuj podróż z potwierdzeniem ceny za pomocą elicitation
- `research_agent` - Badaj tematy z podsumowaniami wspomaganymi przez AI za pomocą sampling
- `list` - Pokaż wszystkie dostęp

---

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dokładamy wszelkich starań, aby tłumaczenie było precyzyjne, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.